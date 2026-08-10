#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Hermann Weyl 的社会关系（源自提示词 Hermann_Weyl_zh.md）。

关系（提示词「人物关系」节，10 条）：
- Hilbert      — 导师（advisor-student，Hilbert→Weyl）
- Einstein     — 同事（ETH+IAS 两度同事，colleague）
- Noether      — 同事（colleague）
- Brouwer      — 论战对手（rival，直觉主义 vs 形式主义）
- von Neumann  — IAS 同事（colleague）
- Gödel        — IAS 同事（colleague）
- Veblen       — IAS 同事/共同筹建者（colleague）
- Mac Lane     — 学生（advisor-student，Weyl→Mac Lane）
- Dyson        — 受其著作影响的青年物理学家（advisor-student 非正式，用 colleague+note）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
WEYL = "Hermann Weyl"

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "David Hilbert", "哥廷根导师，最钟爱的学生，1908 年博士；Hilbert 退休后任其继任者"),
    ("colleague", "Albert Einstein", "ETH 与 IAS 两度同事；Einstein 指出规范理论物理缺陷但尊重其数学深度"),
    ("colleague", "Emmy Noether", "哥廷根与 IAS 同事，纳粹时代为其争取教职的重要支持者"),
    ("rival", "L.E.J. Brouwer", "直觉主义 vs 形式主义论战对手；Weyl 一度被说服又回归"),
    ("colleague", "John von Neumann", "IAS 同事，量子力学数学基础兴趣重叠"),
    ("colleague", "Kurt Gödel", "IAS 同事，数学基础深层对话"),
    ("colleague", "Oswald Veblen", "IAS 同事与共同筹建者"),
    ("advisor-student", "Saunders Mac Lane", "学生，范畴论创始人之一"),
    ("colleague", "Freeman Dyson", "深受 Weyl 著作影响的青年物理学家"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (WEYL,))
    w = cur.fetchone()
    if not w:
        print("⚠ Weyl 不在库中")
        return
    pid_w = w[0]

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

        # 方向：导师（Hilbert→Weyl）、学生（Weyl→Mac Lane）；无向按 id 排序
        if rel == "advisor-student":
            if name == "David Hilbert":
                f, t = pid, pid_w
            else:
                f, t = pid_w, pid
        else:
            f, t = sorted([pid_w, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Hermann_Weyl')",
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
