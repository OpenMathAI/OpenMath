#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Kenneth G. Wilson 的社会关系（源自提示词 Kenneth_G_Wilson_zh.md「第 4.5 步」）。

关系清单：
- 博士导师：Murray Gell-Mann（Caltech，1969 诺奖得主）
- 同事：Michael Fisher（康奈尔同事，临界现象并肩者）、Leo Kadanoff（重整化群先驱思想来源）
- 共同荣誉：Michael Fisher / Leo Kadanoff（1980 Wolf Prize 共同得主）
- 门生：Roman Jackiw、Michael Peskin、Steven R. White、Paul Ginsparg、
        H. R. Krishnamurthy、Serge Rudaz

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
WILSON = "Kenneth G. Wilson"

# 导师（有向：→ Wilson）
ADVISORS = {"Murray Gell-Mann"}

# (relation_type, 人物, note)
RELATIONS = [
    # 博士导师（Gell-Mann → Wilson）
    ("advisor-student", "Murray Gell-Mann", "Caltech 博士导师，1969 诺贝尔物理学奖得主"),
    # 同事（无向）
    ("colleague", "Michael Fisher", "康奈尔同事，临界现象理论并肩者"),
    ("colleague", "Leo Kadanoff", "重整化群的先驱思想来源"),
    # 共同荣誉（无向，1980 Wolf Prize）
    ("co-honored", "Michael Fisher", "1980 Wolf Prize 共同得主"),
    ("co-honored", "Leo Kadanoff", "1980 Wolf Prize 共同得主"),
    # 门生（Wilson → 学生）
    ("advisor-student", "Roman Jackiw", "学生，轴子/量子反常"),
    ("advisor-student", "Michael Peskin", "学生，《An Introduction to Quantum Field Theory》作者"),
    ("advisor-student", "Steven R. White", "学生，DMRG 奠基人"),
    ("advisor-student", "Paul Ginsparg", "学生，arXiv 创始人"),
    ("advisor-student", "H. R. Krishnamurthy", "学生"),
    ("advisor-student", "Serge Rudaz", "学生"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (WILSON,))
    row = cur.fetchone()
    if not row:
        print(f"⚠ Wilson 不在库中，请先运行 seed_wilson_full.py")
        return
    wilson_id = row[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'physicist',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute(
                "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid, occ_id),
            )
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name}")
        else:
            print(f"  已有: {name}")

        # 方向：导师（Gell-Mann → Wilson）、门生（Wilson → 学生）、其余无向
        if rel == "advisor-student":
            if name in ADVISORS:
                f, t = pid, wilson_id
            else:
                f, t = wilson_id, pid
        else:
            f, t = sorted([wilson_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Kenneth_G_Wilson')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name}（{note[:18]}…）")

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
