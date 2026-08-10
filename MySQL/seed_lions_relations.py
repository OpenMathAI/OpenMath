#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jacques-Louis Lions 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "Jacques-Louis Lions"
RELATIONS = [
    ("advisor-student", "Laurent Schwartz", "博士导师（1954）：分布论之父", "in"),
    ("advisor-student", "Haim Brezis", "博士生，非线性分析", "out"),
    ("advisor-student", "Roger Temam", "博士生，Navier–Stokes 与数值方法", "out"),
    ("advisor-student", "Alain Bensoussan", "博士生，最优控制与随机控制", "out"),
    ("advisor-student", "Philippe Ciarlet", "博士生，有限元方法（弹性力学）", "out"),
    ("colleague", "Jean Leray", "同事（法国 PDE 传统）", "undir"),
    ("collaborator", "Enrico Magenes", "合作者：Lions–Magenes 引理（迹定理）", "undir"),
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
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Lions')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
