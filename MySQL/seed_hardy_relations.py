#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G.H. Hardy 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "G.H. Hardy"
RELATIONS = [
    ("advisor-student", "Augustus Edward Hough Love", "博士导师（剑桥），弹性力学", "in"),
    ("advisor-student", "E. T. Whittaker", "导师之一，分析与特殊函数", "in"),
    ("advisor-student", "Srinivasa Ramanujan", "最重要学生/被发掘者：1913 年慧眼识珠，改变 Ramanujan 一生", "out"),
    ("advisor-student", "Mary Cartwright", "博士生，函数论与混沌理论先驱", "out"),
    ("advisor-student", "E. C. Titchmarsh", "博士生，黎曼 zeta 函数", "out"),
    ("collaborator", "J. E. Littlewood", "终身合作者：Hardy–Littlewood 圆法与不等式（35 年合作）", "undir"),
    ("colleague", "Bertrand Russell", "同事（剑桥三一学院）：《数学原理》时代的密友", "undir"),
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
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Hardy')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
