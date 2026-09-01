#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""入库 Bernhard Riemann 与 Ferdinand Georg Frobenius 的社会关系与研究领域。"""
import re
import sys
import unicodedata

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_'.()\u00b7,\-]", "", s).lower()


conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id, name_en FROM people")
by_en = {norm(en): pid for pid, en in cur.fetchall() if en}
cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
occ_id = cur.fetchone()[0]


def gp(name):
    n = norm(name)
    if n in by_en:
        return by_en[n], False
    cur.execute(
        "INSERT INTO people(name_en, primary_occupation, has_biography) "
        "VALUES (%s,'mathematician',0)", (name,),
    )
    pid = cur.lastrowid
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) "
        "VALUES (%s,%s,0)", (pid, occ_id),
    )
    by_en[n] = pid
    return pid, True


def ef(f_en):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (f_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO fields(name_en) VALUES (%s)", (f_en,))
    return cur.lastrowid


def ar(pid0, rt, name, note, fwd=True):
    pid, created = gp(name)
    if rt == "advisor-student":
        f, t = (pid0, pid) if fwd else (pid, pid0)
    else:
        f, t = sorted([pid0, pid])
    cur.execute(
        "INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) "
        "VALUES (%s,%s,%s,%s,'riemann-frobenius')",
        (f, t, rt, note),
    )
    return pid, created, cur.rowcount


def run(P, label):
    pid = P["pid"]
    for c_en, c_zh, succ in P["nat"]:
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (c_en,))
        cid = cur.fetchone()[0]
        cur.execute(
            "INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) "
            "VALUES (%s,%s,0)", (pid, cid),
        )
    for f_en in P["fields"]:
        fid = ef(f_en)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id,field_id,`rank`) "
            "VALUES (%s,%s,0)", (pid, fid),
        )
    for adv, note in P["advisors"]:
        _, created, rc = ar(pid, "advisor-student", adv, note, fwd=False)
        if rc:
            print("  [rel] advisor %s (%s)" % (adv, "NEW" if created else "EXIST"))
    for stu, note in P["students"]:
        _, created, rc = ar(pid, "advisor-student", stu, note, fwd=True)
        if rc:
            print("  [rel] student %s (%s)" % (stu, "NEW" if created else "EXIST"))
    for n2, note in P["colleagues"]:
        _, created, rc = ar(pid, "colleague", n2, note)
        if rc:
            print("  [rel] colleague %s (%s)" % (n2, "NEW" if created else "EXIST"))
    print("done " + label)


R = dict(
    pid=876,
    nat=[("Kingdom of Hanover", "汉诺威王国", "Germany")],
    fields=["differential geometry", "complex analysis", "number theory",
            "mathematical analysis", "mathematical physics"],
    advisors=[
        ("Carl Friedrich Gauss", "博士导师"),
        ("Peter Gustav Lejeune Dirichlet", "柏林求学老师"),
        ("Carl Gustav Jacob Jacobi", "柏林求学老师"),
        ("Gotthold Eisenstein", "学术导师"),
        ("Moritz A. Stern", "学术导师"),
        ("Carl W. B. Goldschmidt", "学术导师"),
        ("Jakob Steiner", "柏林求学老师"),
    ],
    students=[
        ("Gustav Roch", "学生"),
        ("Eduard Selling", "学生"),
        ("Carl Anton Bjerknes", "学生"),
    ],
    colleagues=[
        ("Richard Dedekind", "整理出版几何演讲与传记"),
        ("Karl Weierstrass", "阿贝尔函数竞争，但欣赏其工作"),
    ],
)

F = dict(
    pid=670,
    nat=[("Kingdom of Prussia", "普鲁士王国", "Germany")],
    fields=["group theory", "algebra", "representation theory",
            "number theory", "differential equations"],
    advisors=[
        ("Karl Weierstrass", "博士导师"),
        ("Ernst Kummer", "柏林受业教师"),
        ("Leopold Kronecker", "柏林受业教师"),
    ],
    students=[
        ("Issai Schur", "学生"),
        ("Edmund Landau", "学生"),
        ("Konrad Knopp", "学生"),
        ("Richard Fuchs", "学生"),
        ("Walter Schnee", "学生"),
        ("Ernst Jacobsthal", "学生"),
        ("Robert Remak", "学生"),
    ],
    colleagues=[],
)

run(R, "Riemann")
run(F, "Frobenius")
conn.commit()
print("=== COMMITTED ===")
conn.close()
