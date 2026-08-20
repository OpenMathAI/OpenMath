#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Pieter Zeeman 的社会关系（源自提示词 Pieter_Zeeman_zh.md「第 4.5 步」）。

关系清单：
- 导师：Heike Kamerlingh Onnes（博士导师）、Hendrik Lorentz（其他学术顾问）
- 同事：Albert Einstein、Paul Ehrenfest、Johannes van der Waals
- 共同获奖：Hendrik Lorentz（1902 诺奖共同得主）
- 配偶：Johanna Elisabeth Lebret

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开] 」前缀。
"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ZEEMAN_QID = "Q79000"

# (relation_type, 人物, 方向, note)
RELATIONS = [
    ("advisor-student", "Heike Kamerlingh Onnes", "to_zeeman", "莱顿大学博士导师"),
    ("advisor-student", "Hendrik Lorentz", "to_zeeman", "其他学术顾问，塞曼是其'其他知名学生'"),
    ("colleague", "Albert Einstein", "undirected", "circa 1920 到访阿姆斯特丹"),
    ("colleague", "Paul Ehrenfest", "undirected", "同事，与 Einstein 一同到访"),
    ("colleague", "Johannes van der Waals", "undirected", "1908 接替其任正教授兼物理研究所所长"),
    ("co-honored", "Hendrik Lorentz", "undirected", "1902 诺贝尔物理学奖共同得主"),
    ("spouse", "Johanna Elisabeth Lebret", "undirected", "妻子，1895 结婚"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 定位塞曼
    cur.execute("SELECT id FROM people WHERE qid=%s", (ZEEMAN_QID,))
    r = cur.fetchone()
    if not r:
        print("⚠ 塞曼不在库中，请先运行 seed_zeeman_full.py")
        return
    zeeman_id = r[0]
    print(f"✓ 塞曼 id={zeeman_id}")

    # 加载全部人物
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, direction, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'physicist',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                        (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name}")
        else:
            print(f"  已有: {name} (id={pid})")

        # 方向判定
        if rel == "advisor-student":
            f, t = pid, zeeman_id  # 导师 → 塞曼
        else:
            f, t = sorted([zeeman_id, pid])  # 无向：MIN(id)→MAX(id)

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Pieter_Zeeman')",
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
