#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Élie Cartan 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "Élie Cartan"
# (rel, name, note, dir)  dir: 'in'=此人→Cartan, 'out'=Cartan→此人, 'undir'=无向
RELATIONS = [
    ("advisor-student", "Jean Gaston Darboux", "博士导师（1894），微分几何传统", "in"),
    ("advisor-student", "Sophus Lie", "思想导师：李群理论奠定 Cartan 的方向", "in"),
    ("advisor-student", "Charles Ehresmann", "博士生，纤维丛理论", "out"),
    ("advisor-student", "Georges de Rham", "博士生，de Rham 上同调", "out"),
    ("advisor-student", "Kentaro Yano", "博士生，微分几何", "out"),
    ("parent-child", "Henri Cartan", "儿子，也是著名数学家（代数拓扑）", "out"),
    ("colleague", "André Weil", "同事（法国数学界），同为布尔巴基精神源头之一", "undir"),
    ("colleague", "Jean Dieudonné", "同事：Cartan–Dieudonné 定理合作者", "undir"),
    ("colleague", "Claude Chevalley", "同事（法国学派）", "undir"),
    ("colleague", "Laurent Schwartz", "同事：外微分形式对分布论的深刻影响", "undir"),
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
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Cartan')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
