#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stephen Smale 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "Stephen Smale"
RELATIONS = [
    ("advisor-student", "Raoul Bott", "博士导师（密歇根，1957）", "in"),
    ("advisor-student", "Morris Hirsch", "博士生，微分拓扑", "out"),
    ("advisor-student", "Michael Shub", "博士生，计算复杂度（BSS 机器）", "out"),
    ("advisor-student", "Jacob Palis", "博士生，动力系统（Palis–Smale 猜想）", "out"),
    ("advisor-student", "Robert Devaney", "博士生，混沌动力学", "out"),
    ("colleague", "John Milnor", "同事：微分拓扑黄金时代的双雄", "undir"),
    ("colleague", "René Thom", "同事：奇点与动力学结构", "undir"),
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
    for rel, name, note, d in RELATIONS:
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
        if d == "in":
            f, t = pid, pid_me
        elif d == "out":
            f, t = pid_me, pid
        else:
            f, t = sorted([pid_me, pid])
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Smale')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
