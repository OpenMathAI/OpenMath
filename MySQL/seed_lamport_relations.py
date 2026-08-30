#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Leslie Lamport 的社会关系（源自提示词 Leslie_Lamport_zh.md「第 4.5 步」）。

关系清单：
- 博士导师：Richard Palais（Brandeis 数学导师，advisor-student，Palais → Lamport）
- 合作者（collaborator，双向）：
  Robert Shostak、Marshall Pease、K. Mani Chandy
- 同事/后继维护（colleague，双向）：Frank Mittelbach（1989 年接管 LaTeX 维护，LaTeX3 团队）

数据来源：本地 Wikipedia (turing/pages/2013/Leslie Lamport/index.html) infobox + 正文。
不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
LAMPORT = "Leslie Lamport"

# 有向关系：博士导师（→ Lamport）
ADVISORS = {"Richard Palais"}

# (relation_type, 人物, note, 方向：advisor 表示 → Lamport，其余双向)
RELATIONS = [
    ("advisor-student", "Richard Palais", "博士导师，Brandeis 数学导师（解析偏微分方程论文指导）", "advisor"),
    ("collaborator", "Robert Shostak", "合作者，《The Byzantine Generals Problem》(1982) 共同作者", "bi"),
    ("collaborator", "Marshall Pease", "合作者，《The Byzantine Generals Problem》/《Reaching Agreement in the Presence of Faults》共同作者", "bi"),
    ("collaborator", "K. Mani Chandy", "合作者，Chandy–Lamport 分布式快照算法共同作者", "bi"),
    ("colleague", "Frank Mittelbach", "同事/后继维护者，1989 年接管 LaTeX 维护，LaTeX3 团队核心", "bi"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (LAMPORT,))
    row = cur.fetchone()
    if not row:
        print(f"⚠ Lamport 不在库中，请先运行 seed_lamport_full.py")
        return
    lamport_id = row[0]

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
    for rel, name, note, direction in RELATIONS:
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

        if rel == "advisor-student" and direction == "advisor":
            f, t = pid, lamport_id
        else:
            f, t = sorted([lamport_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Leslie_Lamport')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name}（{note[:20]}…）")

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
