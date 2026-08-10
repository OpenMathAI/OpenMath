#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 David Hilbert 的社会关系（源自 presentations/David_Hilbert 材料）。

关系：
- 老师：Ferdinand von Lindemann
- 终身挚友：Hermann Minkowski
- 学生/门生：Weyl, Courant, Zermelo, Noether, Dehn, Hecke, Steinhaus,
             Ackermann, Hellinger, Haar, Takagi, Landau

策略：
- 不在库中的人物先新建（占位，has_biography=0, source 标识）
- 社会关系打标识：note 前缀 [Hilbert-材料待展开]，后续可展开详细介绍
"""
import re
import unicodedata
from pathlib import Path

from db_mysql import get_conn

# Hilbert 社会关系清单：(关系类型, 人物, 备注)
# 关系类型对应 relation_types: advisor-student(有向师→生) / colleague(无向) / co-honored...
# 人物别名：库中名字与材料名的差异
NAME_ALIAS = {
    "Teiji Takagi": "Takagi Teiji",   # 库中为 Takagi Teiji（高木贞治）
}

HILBERT_RELATIONS = [
    # 老师（有向：Lindemann → Hilbert）
    ("advisor-student", "Ferdinand von Lindemann", "Hilbert 1885 博士导师，π 的超越性证明者"),
    # 挚友（无向：Hilbert ↔ Minkowski）
    ("colleague", "Hermann Minkowski", "终身挚友，Hilbert 称其为『我最好、最真诚的朋友』"),
    # 学生（有向：Hilbert → 学生）
    ("advisor-student", "Hermann Weyl", "学生/继任者，数学物理·规范理论"),
    ("advisor-student", "Richard Courant", "学生，Courant 研究所创始人"),
    ("advisor-student", "Ernst Zermelo", "学生，集合论公理化 ZFC 奠基者"),
    ("advisor-student", "Emmy Noether", "学生，Hilbert & Klein 为其争取教职"),
    ("advisor-student", "Max Dehn", "学生，Göttingen 学派"),
    ("advisor-student", "Erich Hecke", "学生，Göttingen 学派"),
    ("advisor-student", "Hugo Steinhaus", "学生，Göttingen 学派"),
    ("advisor-student", "Wilhelm Ackermann", "学生，Göttingen 学派"),
    ("advisor-student", "Ernst Hellinger", "学生，Göttingen 学派"),
    ("advisor-student", "Alfréd Haar", "学生，Göttingen 学派"),
    ("advisor-student", "Teiji Takagi", "学生，证明 Hilbert 类域猜想，类域论奠基"),
    ("advisor-student", "Edmund Landau", "学生，解析数论"),
]

MARKER = "[Hilbert-材料待展开] "


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # Hilbert 本人
    cur.execute("SELECT id FROM people WHERE name_en='David Hilbert'")
    hilbert = cur.fetchone()
    if not hilbert:
        print("⚠ Hilbert 不在库中")
        return
    hilbert_id = hilbert[0]

    # 载入 people 索引
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    # 数学家职业
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = 0
    relations_added = 0
    for rel, name, note in HILBERT_RELATIONS:
        # 1) 找到或创建人物（先查别名，避免重复创建）
        lookup = NAME_ALIAS.get(name, name)
        pid = by_en.get(norm(lookup))
        if pid is None:
            pid = by_zh.get(norm(lookup))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'mathematician',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                        (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name}")
        else:
            print(f"  已有: {name}")

        # 2) 建立关系（有向 advisor-student: 师→生；colleague 无向按 id 排序）
        if rel == "advisor-student":
            # 判断方向：Hilbert 是学生（Lindemann→Hilbert）还是老师（Hilbert→学生）
            if name == "Ferdinand von Lindemann":
                f, t = pid, hilbert_id
            else:
                f, t = hilbert_id, pid
        else:  # colleague 无向
            f, t = sorted([hilbert_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Hilbert-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1
            print(f"    → {rel}: {name}（{note[:20]}…）")

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
