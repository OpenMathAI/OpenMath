#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""入库 Leonhard Euler（欧拉）的社会关系与研究领域。

数据源：
  - mathematician/presentations/18th_century/pages/Leonhard_Euler/metadata.json
  - mathematician/presentations/18th_century/pages/Leonhard_Euler/page.md（infobox）
"""
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
        "VALUES (%s,%s,%s,%s,'euler')",
        (f, t, rt, note),
    )
    return pid, created, cur.rowcount


# ============ 1. 创建 / 查找欧拉本人 ============
cur.execute("SELECT id FROM people WHERE qid='Q7604'")
r = cur.fetchone()
if r:
    euler_pid, euler_new = r[0], False
else:
    cur.execute(
        "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
        "description, primary_occupation, has_biography, has_social_data) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        ("Q7604", "Leonhard Euler", "欧拉", "male", "1707-04-15", "1783-09-18",
         "Swiss mathematician, physicist, and engineer (1707-1783)",
         "mathematician", 1, 1),
    )
    euler_pid, euler_new = cur.lastrowid, True
print("Euler pid=%s (%s)" % (euler_pid, "NEW" if euler_new else "EXIST"))

# ============ 2. 国籍 ============
for c_en, c_zh in [
    ("Old Swiss Confederacy", "旧瑞士邦联"),
    ("Russian Empire", "俄罗斯帝国"),
    ("Kingdom of Prussia", "普鲁士王国"),
]:
    cur.execute("SELECT id FROM countries WHERE name_en=%s", (c_en,))
    r = cur.fetchone()
    if not r:
        print("  [warn] country not found: %s" % c_en)
        continue
    rc = cur.execute(
        "INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) "
        "VALUES (%s,%s,0)", (euler_pid, r[0]),
    )
    if rc:
        print("  [nat] %s (%s)" % (c_en, c_zh))

# ============ 3. 职业 ============
for occ_en in ["mathematician", "physicist", "astronomer", "university teacher"]:
    cur.execute("SELECT id FROM occupations WHERE name_en=%s", (occ_en,))
    r = cur.fetchone()
    if not r:
        print("  [warn] occupation not found: %s" % occ_en)
        continue
    rc = cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) "
        "VALUES (%s,%s,0)", (euler_pid, r[0]),
    )
    if rc:
        print("  [occ] %s" % occ_en)

# ============ 4. 研究领域 ============
FIELDS = [
    "mathematical analysis", "number theory", "shipbuilding",
    "calculus of variations", "astronomy", "mechanics",
    "theory of differential equations", "ballistics", "optics",
    "mathematics", "music theory", "differential calculus",
    "graph theory", "physics", "logic",
]
for f_en in FIELDS:
    fid = ef(f_en)
    rc = cur.execute(
        "INSERT IGNORE INTO person_field(person_id,field_id,`rank`) "
        "VALUES (%s,%s,0)", (euler_pid, fid),
    )
    if rc:
        print("  [field] %s" % f_en)

# ============ 5. 社会关系 ============
# 导师（欧拉是学生）fwd=False
for adv, note in [("Johann Bernoulli", "导师（每周末答疑）")]:
    _, created, rc = ar(euler_pid, "advisor-student", adv, note, fwd=False)
    if rc:
        print("  [rel] advisor %s (%s)" % (adv, "NEW" if created else "EXIST"))

# 学生（欧拉是导师）fwd=True
for stu, note in [
    ("Johann Hennert", "博士学生"),
    ("Nicolas Fuss", "学生"),
    ("Stepan Rumovsky", "学生"),
    ("Anders Johan Lexell", "学生"),
    ("Joseph-Louis Lagrange", "书信指导（epistolary correspondent）"),
]:
    _, created, rc = ar(euler_pid, "advisor-student", stu, note, fwd=True)
    if rc:
        print("  [rel] student %s (%s)" % (stu, "NEW" if created else "EXIST"))

# 合作 / 通信
for col, note in [
    ("Christian Goldbach", "哥德巴赫猜想通信"),
    ("Daniel Bernoulli", "流体力学合作"),
]:
    _, created, rc = ar(euler_pid, "collaborator", col, note)
    if rc:
        print("  [rel] collaborator %s (%s)" % (col, "NEW" if created else "EXIST"))

# 同事
for col, note in [("Pierre Louis Maupertuis", "柏林科学院同事")]:
    _, created, rc = ar(euler_pid, "colleague", col, note)
    if rc:
        print("  [rel] colleague %s (%s)" % (col, "NEW" if created else "EXIST"))

conn.commit()
print("=== COMMITTED ===")

# ============ 6. 回显校验 ============
cur.execute("SELECT COUNT(*) FROM person_field WHERE person_id=%s", (euler_pid,))
print("person_field rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (euler_pid, euler_pid))
print("person_relation rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_nationality WHERE person_id=%s", (euler_pid,))
print("person_nationality rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_occupation WHERE person_id=%s", (euler_pid,))
print("person_occupation rows: %d" % cur.fetchone()[0])
conn.close()
