#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Donald Knuth 的社会关系（源自提示词 Donald_Knuth_zh.md「第 4.5 步」）。

关系清单：
- 博士导师：Marshall Hall, Jr.（Caltech 数学导师，advisor-student，Hall → Knuth）
- 门生 7 人（advisor-student，Knuth → 学生）：
  Robert Sedgewick、Leonidas J. Guibas、Vaughan Pratt、Michael Fredman、
  Jeffrey Vitter、Scott Kim、Andrei Broder

门生名单以本地 Wikipedia 正文 infobox（turing/pages/1974/Donald Knuth/index.html）
的 `Doctoral students` 字段为准。

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
KNUTH = "Donald Knuth"

# 导师（有向：→ Knuth）
ADVISORS = {"Marshall Hall, Jr."}

# (relation_type, 人物, note)
RELATIONS = [
    # 博士导师（→ Knuth）
    ("advisor-student", "Marshall Hall, Jr.", "博士导师，Caltech 数学导师（有限半域与射影平面论文指导）"),
    # 门生（Knuth → 学生）
    ("advisor-student", "Robert Sedgewick", "学生，《算法》作者，普林斯顿大学"),
    ("advisor-student", "Leonidas J. Guibas", "学生，计算几何"),
    ("advisor-student", "Vaughan Pratt", "学生，Pratt 解析，KMP 算法合作者"),
    ("advisor-student", "Michael Fredman", "学生，斐波那契堆"),
    ("advisor-student", "Jeffrey Vitter", "学生，外部存储算法"),
    ("advisor-student", "Scott Kim", "学生，字体设计"),
    ("advisor-student", "Andrei Broder", "学生，信息检索"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (KNUTH,))
    row = cur.fetchone()
    if not row:
        print(f"⚠ Knuth 不在库中，请先运行 seed_knuth_full.py")
        return
    knuth_id = row[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    # 确保 computer scientist 职业存在（占位人物用）
    cur.execute("SELECT id FROM occupations WHERE name_en='computer scientist'")
    r = cur.fetchone()
    if r:
        occ_id = r[0]
    else:
        cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES ('computer scientist','计算机科学家')")
        occ_id = cur.lastrowid

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'computer scientist',0)",
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

        # 方向：导师（→ Knuth）、门生（Knuth → 学生）
        if rel == "advisor-student":
            if name in ADVISORS:
                f, t = pid, knuth_id
            else:
                f, t = knuth_id, pid
        else:
            f, t = sorted([knuth_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Donald_Knuth')",
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
