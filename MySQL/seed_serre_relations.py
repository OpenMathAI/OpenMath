#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Serre 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "J.-P. Serre"
RELATIONS = [
    ("advisor-student", "Henri Cartan", "博士导师，代数拓扑引路人；Cartan 学派核心"),
    ("advisor-student", "Jean-Marc Fontaine", "博士生，算术代数几何"),
    ("advisor-student", "Michel Broué", "博士生，表示论"),
    ("advisor-student", "Pierre Gabriel", "博士生，代数几何"),
    ("colleague", "Alexander Grothendieck", "合作者与对话者：FAC 为概形理论铺路，l-adic 上同调共同发展"),
    ("colleague", "André Weil", "同事：Weil 猜想对 Serre 深有影响，Bourbaki 共同成员"),
    ("collaborator", "Claude Chevalley", "合作者：Bourbaki 核心成员"),
    ("collaborator", "Armand Borel", "长期合作者：代数群与拓扑，Borel–Serre 紧化"),
    ("collaborator", "John Tate", "合作者：数论，Serre–Tate 定理"),
    ("colleague", "Pierre Deligne", "学术后代：Deligne 继承并证明 Weil 猜想，两人交情深厚"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM people WHERE name_en=%s", (ME,))
    me = cur.fetchone()
    if not me:
        print("⚠ 不在库"); return
    pid_me = me[0]
    cur.execute("SELECT id,name_en,name_zh FROM people")
    rows = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in rows if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in rows if nz}
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]
    created = added = 0
    for rel, name, note in RELATIONS:
        pid = by_en.get(norm(name)) or by_zh.get(norm(name))
        if pid is None:
            cur.execute("INSERT INTO people(name_en,primary_occupation,has_biography) VALUES (%s,'mathematician',0)", (name,))
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id,occupation_id,`rank`) VALUES (%s,%s,0)", (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 占位: {name}")
        else:
            print(f"  已有: {name} (id={pid})")
        if rel == "advisor-student":
            if name == "Henri Cartan":
                f, t = pid, pid_me
            else:
                f, t = pid_me, pid
        else:
            f, t = sorted([pid_me, pid])
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Serre')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
