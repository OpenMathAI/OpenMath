#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lebesgue 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "Henri Lebesgue"
RELATIONS = [
    ("advisor-student", "Émile Borel", "博士导师（1902）；后因积分理论谁更一般产生 1918–1920 君子之争", True),
    ("advisor-student", "Paul Montel", "博士生，正规族理论", False),
    ("advisor-student", "Georges de Rham", "博士生，de Rham 上同调", False),
    ("advisor-student", "Zygmunt Janiszewski", "博士生，拓扑学（后为波兰学派奠基人）", False),
    ("colleague", "Jacques Hadamard", "同事（法国数学界）：Hadamard 对泛函分析有深远影响", False),
    ("colleague", "René Baire", "同事：Baire 函数类深刻影响 Lebesgue 的测度与积分理论", False),
    ("colleague", "Camille Jordan", "同事：Jordan 测度为 Lebesgue 测度之前驱", False),
    ("collaborator", "Henri Poincaré", "思想对话：Lebesgue 的六理想条件回应 Poincaré 的分析批评", False),
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
    for rel, name, note, is_advisor in RELATIONS:
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
            f, t = (pid, pid_me) if is_advisor else (pid_me, pid)
        else:
            f, t = sorted([pid_me, pid])
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Lebesgue')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
