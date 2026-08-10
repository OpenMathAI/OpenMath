#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 John von Neumann 的社会关系（源自提示词 John_von_Neumann_zh.md）。

关系（提示词「人物关系」节）：
- Hilbert  — 导师兼灵感来源（advisor-student，Hilbert→von Neumann）
- Weyl     — IAS 同事（colleague，无向）
- Wigner   — 中学同学、终生挚友（colleague，无向）
- Morgenstern — 经济学家，博弈论合著者（collaborator，无向）
- Ulam     — 最亲密美国朋友，Monte Carlo 共同发明者（collaborator，无向）
- Oppenheimer — 曼哈顿计划科学总监（colleague，无向）
- Teller   — 核武器设计密切合作者（collaborator，无向）
- Gödel    — IAS 同事，数理逻辑对话者（colleague，无向）
- Einstein — IAS 同事（colleague，无向）
- Szilard  — 核链式反应概念发明者（colleague，无向）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
NEUMANN = "John von Neumann"

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "David Hilbert", "哥廷根时期导师，继承 Hilbert 形式主义与公理化方法"),
    ("colleague", "Hermann Weyl", "IAS 同事；1926 年冬哥廷根街头与 Noether 讨论超复数系统"),
    ("colleague", "Eugene Wigner", "中学同学、终生挚友，1963 年诺贝尔物理学奖得主"),
    ("collaborator", "Oskar Morgenstern", "经济学家，《博弈论与经济行为》合著者"),
    ("collaborator", "Stanisław Ulam", "最亲密的美国朋友，Monte Carlo 方法共同发明者"),
    ("colleague", "J. Robert Oppenheimer", "曼哈顿计划科学总监"),
    ("collaborator", "Edward Teller", "『氢弹之父』，核武器设计密切合作者"),
    ("colleague", "Kurt Gödel", "IAS 同事，数理逻辑和集合论对话者"),
    ("colleague", "Albert Einstein", "IAS 同事，对 von Neumann 智力评价极高"),
    ("colleague", "Leó Szilard", "另一位『火星人』，核链式反应概念发明者"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (NEUMANN,))
    neumann = cur.fetchone()
    if not neumann:
        print("⚠ von Neumann 不在库中")
        return
    pid_n = neumann[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
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

        # 有向：Hilbert 是导师（Hilbert→von Neumann）；其余无向按 id 排序
        if rel == "advisor-student":
            f, t = pid, pid_n
        else:
            f, t = sorted([pid_n, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-John_von_Neumann')",
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
