#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Werner Heisenberg 的社会关系（源自提示词 Werner_Heisenberg_zh.md「第 7 节」）。

关系清单：
- 导师：Arnold Sommerfeld（博士导师）、Max Born（habil 导师）
- 合作：Pascual Jordan（矩阵力学）、Wolfgang Pauli（量子场论、挚友）
- 同事/师承：Niels Bohr（哥本哈根合作）
- 学生：Edward Teller、Felix Bloch、Carl Friedrich von Weizsäcker、Rudolf Peierls
- 对立：Philipp Lenard、Johannes Stark（"德国物理学"运动）
- 诺奖同届：Erwin Schrödinger、Paul Dirac（1932/1933 年度共同得主）

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
HEISENBERG = "Werner Heisenberg"
HEISENBERG_ID = 704

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "Arnold Sommerfeld", "慕尼黑大学博士导师，量子理论的引路人"),
    ("advisor-student", "Max Born", "哥廷根 habilitation 导师；亦为矩阵力学合作者"),
    ("collaborator", "Pascual Jordan", "共同完成矩阵力学（Dreimännerarbeit 三人论文）"),
    ("collaborator", "Wolfgang Pauli", "共同奠定相对论量子场论；终身挚友与通信伙伴"),
    ("colleague", "Niels Bohr", "哥本哈根研究合作，哥本哈根诠释的核心人物"),
    ("advisor-student", "Edward Teller", "莱比锡时期博士生，后成为氢弹之父"),
    ("advisor-student", "Felix Bloch", "莱比锡时期博士生，1952 诺贝尔物理学奖得主"),
    ("advisor-student", "Carl Friedrich von Weizsäcker", "莱比锡时期博士生，核计划核心助手"),
    ("advisor-student", "Rudolf Peierls", "莱比锡时期博士生，后赴英国曼哈顿计划"),
    ("rival", "Philipp Lenard", "「德国物理学」运动领袖，攻击其为「白犹太人」"),
    ("rival", "Johannes Stark", "「德国物理学」运动代表，发起 SS 调查"),
    ("co-honored", "Erwin Schrödinger", "1933 年度诺贝尔物理学奖得主（波动力学）"),
    ("co-honored", "Paul Dirac", "1933 年度诺贝尔物理学奖得主（量子电动力学）"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE id=%s", (HEISENBERG_ID,))
    if not cur.fetchone():
        print("⚠ Heisenberg (id=704) 不在库中")
        return

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_id = cur.fetchone()[0]

    # 学生名单：这些关系的方向是 Heisenberg -> 学生
    STUDENTS = {
        "Edward Teller",
        "Felix Bloch",
        "Carl Friedrich von Weizsäcker",
        "Rudolf Peierls",
    }

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
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                        (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name}")
        else:
            print(f"  已有: {name}")

        # 方向：导师（Sommerfeld/Born→Heisenberg）、学生（Heisenberg→Teller 等）
        if rel == "advisor-student":
            if name in STUDENTS:
                f, t = HEISENBERG_ID, pid
            else:
                f, t = pid, HEISENBERG_ID
        else:
            f, t = sorted([HEISENBERG_ID, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Werner_Heisenberg')",
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
