#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R.A. Fisher 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "R.A. Fisher"
RELATIONS = [
    ("advisor-student", "James Hopwood Jeans", "博士导师（剑桥）：天体物理与数学", "in"),
    ("advisor-student", "F. J. M. Stratton", "导师之一（剑桥），天文学家", "in"),
    ("advisor-student", "C. R. Rao", "最重要学生：印度统计学派奠基人", "out"),
    ("advisor-student", "Walter Bodmer", "博士生，群体遗传学", "out"),
    ("colleague", "Karl Pearson", "统计学两大巨头：Pearson–Fisher 方法论之争", "undir"),
    ("colleague", "Jerzy Neyman", "频率学派内部之争：Fisher–Neyman 假设检验分歧", "undir"),
    ("colleague", "William Sealy Gosset", "通信挚友：Student's t 分布的合作者", "undir"),
    ("colleague", "J. B. S. Haldane", "群体遗传学三巨头（Fisher–Haldane–Wright）", "undir"),
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
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Fisher')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
