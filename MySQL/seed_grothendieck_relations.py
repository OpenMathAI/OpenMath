#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Alexander Grothendieck 的社会关系（源自 presentations/Alexander_Grothendieck_zh.tex）。

关系（tex 材料）：
- Schwartz    — 南锡博士导师之一（advisor-student，Schwartz→Grothendieck）
- Dieudonné   — 南锡博士导师之一（advisor-student，Dieudonné→Grothendieck）
- Serre       — IHÉS 同事（colleague，无向）
- Deligne     — 最著名学生（advisor-student，Grothendieck→Deligne）
- Illusie     — 学生（advisor-student）
- Verdier     — 学生（advisor-student）
- Raynaud     — 学生（advisor-student）
- M. Artin    — 学生/学派成员（advisor-student）
- Mumford     — 学派深度参与者（advisor-student，非正式）
- Hartshorne  — 学生（advisor-student，非正式）
- Dieudonné   — EGA 合著者（collaborator，已在导师关系外补充）
- Schneps / Lochak — 晚年最后接触的数学家（colleague）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
别名：Jean-Pierre Serre -> J.-P. Serre（库中名）
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
G = "Alexander Grothendieck"

NAME_ALIAS = {
    "Jean-Pierre Serre": "J.-P. Serre",
}

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "Laurent Schwartz", "南锡博士导师之一，泛函分析"),
    ("advisor-student", "Jean Dieudonné", "南锡博士导师之一；后合著 EGA"),
    ("colleague", "Jean-Pierre Serre", "IHÉS 同事，拓扑学与代数几何交叉对话"),
    ("advisor-student", "Pierre Deligne", "最著名学生，1974 年完成 Weil 猜想关键步骤，1978 菲尔兹奖"),
    ("advisor-student", "Luc Illusie", "学生，étale 上同调与 crystalline 上同调"),
    ("advisor-student", "Jean-Louis Verdier", "学生，导出范畴理论奠基者"),
    ("advisor-student", "Michel Raynaud", "学生，代数几何（Raynaud 环）"),
    ("advisor-student", "Michael Artin", "学派成员，代数空间与 étale 上同调"),
    ("advisor-student", "David Mumford", "学派深度参与者，代数几何与模空间"),
    ("advisor-student", "Robin Hartshorne", "学生，《代数几何》(Hartshorne) 作者"),
    ("colleague", "Leila Schneps", "晚年最后接触他的数学家之一"),
    ("colleague", "Pierre Lochak", "晚年最后接触他的数学家之一"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (G,))
    g = cur.fetchone()
    if not g:
        print("⚠ Grothendieck 不在库中")
        return
    pid_g = g[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
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

        # 方向：导师（→Grothendieck）、学生（Grothendieck→）；同事/合作无向
        if rel == "advisor-student":
            if name in ("Laurent Schwartz", "Jean Dieudonné"):
                f, t = pid, pid_g
            else:
                f, t = pid_g, pid
        else:
            f, t = sorted([pid_g, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Alexander_Grothendieck')",
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
