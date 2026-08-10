#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Henri Poincaré 的社会关系（源自提示词 Henri_Poincare_zh.md + page.md）。

关系（提示词「人物关系」节）：
- Hermite  — 博士名义导师（advisor-student，Hermite→Poincaré）
- Darboux  — 博士实际指导者（advisor-student，Darboux→Poincaré）
- Klein    — 自守函数竞争者，优先权之争（controversy，无向）
- Hilbert  — 同代双子星（co-honored，无向）
- Lorentz  — 物理学家，Lorentz 变换（colleague，无向）
- Einstein — 相对论对话者（controversy，无向——优先权争议）
- Borel    — 学生与合作者（advisor-student，Poincaré→Borel）
- Appell   — 学生与合作者（advisor-student，Poincaré→Appell）
- Raymond Poincaré — 表弟，法国总统（parent-child 有向，但为同辈亲属→用 colleague+note）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
POINCARE = "Henri Poincaré"

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "Charles Hermite", "博士名义导师，代数与分析大师"),
    ("advisor-student", "Gaston Darboux", "博士实际指导者，微分几何"),
    ("controversy", "Felix Klein", "自守函数几乎同时独立发现，存在激烈的优先权竞争"),
    ("co-honored", "David Hilbert", "同代双子星，并称『最后两位数学全才』；Hilbert 公理主义 vs Poincaré 直觉主义"),
    ("colleague", "Hendrik Lorentz", "物理学家，电磁理论，Lorentz 变换"),
    ("controversy", "Albert Einstein", "狭义相对论优先权争议：Poincaré 建立数学框架，Einstein 赋予物理诠释"),
    ("advisor-student", "Émile Borel", "学生与合作者"),
    ("advisor-student", "Paul Appell", "学生与合作者"),
    ("colleague", "Raymond Poincaré", "表弟，法国总统（同家族）"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (POINCARE,))
    poincare = cur.fetchone()
    if not poincare:
        print("⚠ Poincaré 不在库中")
        return
    pid_p = poincare[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
        # 1) 找/建人物
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

        # 2) 建关系（有向师→生；无向按 id 排序）
        if rel == "advisor-student":
            # 判断方向：name 是 Poincaré 的导师（name→Poincaré）还是学生（Poincaré→name）
            if name in ("Charles Hermite", "Gaston Darboux"):
                f, t = pid, pid_p
            else:
                f, t = pid_p, pid
        else:
            f, t = sorted([pid_p, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Henri_Poincare')",
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
