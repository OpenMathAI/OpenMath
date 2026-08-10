#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 mathematician/pages/<Name>/metadata.json 批量补充 people 元数据，
并灌入「导师/学生」社会关系（仅当双方都在库中时）。

用法：
    python3 enrich_people.py                # 处理前 10 人（默认）
    python3 enrich_people.py --n 30         # 处理前 30 人
    python3 enrich_people.py --only Hilbert  # 处理指定人（name_en 子串）
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

import pymysql
from db_mysql import get_conn, CompatCursor

PAGES = Path(__file__).resolve().parent.parent / "mathematician" / "pages"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def get_first(props, *keys):
    for k in keys:
        v = props.get(k)
        if v:
            return v[0] if isinstance(v, list) else v
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10, help="处理前 N 人")
    ap.add_argument("--only", default=None, help="只处理名字包含此子串的人")
    args = ap.parse_args()

    conn = get_conn()
    cur = conn.cursor()

    # 选目标人
    if args.only:
        cur.execute("SELECT id, name_en FROM people WHERE name_en LIKE %s", (f"%{args.only}%",))
    else:
        cur.execute("SELECT id, name_en FROM people WHERE id<=%s ORDER BY id", (args.n,))
    targets = cur.fetchall()
    print(f"待处理: {len(targets)} 人")

    # 载入 people 索引（用于导师/学生姓名归一化匹配）
    cur.execute("SELECT id, name_en FROM people")
    all_people = [(pid, en, norm(en or "")) for pid, en in cur.fetchall()]
    name_index = {n: pid for pid, en, n in all_people}

    # pages 目录 -> 归一化名索引（替代 local_dir）
    page_index = {}
    for d in PAGES.iterdir():
        if d.is_dir() and (d / "metadata.json").exists():
            page_index.setdefault(norm(d.name), d)

    updated = 0
    relations_added = 0
    rel_skipped = 0
    skipped_notfound = 0

    for pid, name_en in targets:
        # 按名字在 pages 下找匹配目录（不依赖 local_dir）
        page_dir = page_index.get(norm(name_en))
        if not page_dir or not (page_dir / "metadata.json").exists():
            print(f"  ⚠ 跳过（无 metadata）: {name_en}")
            continue
        meta = json.loads((page_dir / "metadata.json").read_text(encoding="utf-8"))
        props = meta.get("properties", {})
        qid = meta.get("qid")
        birth = get_first(props, "date_of_birth")
        death = get_first(props, "date_of_death")
        gender = get_first(props, "sex_or_gender")
        description = meta.get("description") or ""

        # 1) 更新 people 元数据
        cur.execute(
            "UPDATE people SET qid=COALESCE(%s,qid), birth_date=COALESCE(%s,birth_date), "
            "death_date=COALESCE(%s,death_date), gender=COALESCE(%s,gender), "
            "description=COALESCE(NULLIF(%s,''),description) WHERE id=%s",
            (qid, birth, death, gender, description, pid),
        )
        if cur.rowcount:
            updated += 1
            print(f"  ✓ 更新元数据: {name_en}（qid={qid} {birth}–{death}）")

        # 2) 处理社会关系（advisor-student 有向；需双方在库）
        advisors = props.get("doctoral_advisor") or props.get("doctoral_adal") or []
        for adv_name in advisors:
            adv_key = norm(adv_name)
            if adv_key in name_index:
                aid = name_index[adv_key]
                if aid != pid:  # 不自指
                    try:
                        cur.execute(
                            "INSERT INTO person_relation(from_id, to_id, relation_type, source) "
                            "VALUES (%s,%s,'advisor-student','enrich_people.py')",
                            (aid, pid),
                        )
                    except pymysql.err.IntegrityError:
                        pass
                    else:
                        if cur.rowcount:
                            relations_added += 1
                            print(f"    → 师生: {adv_name} → {name_en}")
            else:
                skipped_notfound += 1

        students = props.get("doctoral_student") or []
        for stu_name in students:
            stu_key = norm(stu_name)
            if stu_key in name_index:
                sid = name_index[stu_key]
                if sid != pid:
                    try:
                        cur.execute(
                            "INSERT INTO person_relation(from_id, to_id, relation_type, source) "
                            "VALUES (%s,%s,'advisor-student','enrich_people.py')",
                            (pid, sid),
                        )
                    except pymysql.err.IntegrityError:
                        pass
                    else:
                        if cur.rowcount:
                            relations_added += 1
                            print(f"    → 师生: {name_en} → {stu_name}")
            else:
                skipped_notfound += 1

    conn.commit()
    print(f"\n=== 完成 ===")
    print(f"元数据更新: {updated} 人")
    print(f"新增师生关系: {relations_added} 条")
    print(f"未匹配（导师/学生不在库）: {skipped_notfound} 条")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")


if __name__ == "__main__":
    main()