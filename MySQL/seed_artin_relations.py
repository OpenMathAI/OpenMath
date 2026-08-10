#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Artin 社会关系入库（第 4.5 步，§二十）。"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
ME = "Emil Artin"
# (rel, name, note, is_advisor)  is_advisor=True 表示此人→Artin；None 表示 Artin→此人(学生)
RELATIONS = [
    ("advisor-student", "Gustav Herglotz", "博士导师（莱比锡，1921），应用数学与数学物理", True),
    ("advisor-student", "Otto Hölder", "导师之一（莱比锡），Hölder 不等式", True),
    ("advisor-student", "John Tate", "最重要的学生，Artin–Tate 类域论讲义合著者", False),
    ("advisor-student", "Serge Lang", "学生，多产数学作家，深受 Artin 影响", False),
    ("advisor-student", "Max Zorn", "学生，Zorn 引理命名者", False),
    ("advisor-student", "Hans Zassenhaus", "学生，群论与计算代数先驱", False),
    ("advisor-student", "Bernard Dwork", "学生，p-adic 分析先驱", False),
    ("colleague", "Emmy Noether", "知识盟友：Artin 的公理化代数受 Noether 深刻影响", False),
    ("colleague", "Hermann Weyl", "同事（Göttingen 时期），两人同为汉堡-哥廷根代数传统", False),
    ("colleague", "Helmut Hasse", "同事与竞争者：类域论并行工作", False),
    ("collaborator", "Otto Schreier", "合作者：Artin–Schreier 理论", False),
    ("colleague", "Richard Brauer", "同事：证明 Artin L-函数亚纯性（Artin 猜想关键步骤）", False),
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
        cur.execute("INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'立传-Artin')", (f, t, rel, MARKER + note))
        added += cur.rowcount
    conn.commit()
    print(f"\n占位: {created} · 新增关系: {added}")
    conn.close()


if __name__ == "__main__":
    main()
