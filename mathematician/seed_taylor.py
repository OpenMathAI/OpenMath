#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""入库 Brook Taylor（泰勒）的社会关系与研究领域。

数据源：
  - mathematician/presentations/18th_century/pages/Brook_Taylor/metadata.json
  - mathematician/presentations/18th_century/pages/Brook_Taylor/page.md（infobox）
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
        "VALUES (%s,%s,%s,%s,'taylor')",
        (f, t, rt, note),
    )
    return pid, created, cur.rowcount

# ============ 0. 确保国籍 "Kingdom of England" 存在 ============
cur.execute("SELECT id FROM countries WHERE name_en='Kingdom of England'")
r = cur.fetchone()
if r:
    england_id = r[0]
    print("Kingdom of England already exists id=%s" % england_id)
else:
    cur.execute(
        "INSERT INTO countries(name_en, name_zh, is_current, successor) "
        "VALUES (%s,%s,%s,%s)",
        ("Kingdom of England", "英格兰王国", 0, "United Kingdom"),
    )
    england_id = cur.lastrowid
    print("Kingdom of England created id=%s" % england_id)

# ============ 1. 创建 / 查找泰勒本人 ============
cur.execute("SELECT id FROM people WHERE qid='Q212085'")
r = cur.fetchone()
if r:
    taylor_pid, taylor_new = r[0], False
else:
    cur.execute(
        "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
        "description, primary_occupation, has_biography, has_social_data) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        ("Q212085", "Brook Taylor", "泰勒", "male", "1685-08-18", "1731-12-29",
         "English mathematician (1685-1731)",
         "mathematician", 1, 1),
    )
    taylor_pid, taylor_new = cur.lastrowid, True
print("Taylor pid=%s (%s)" % (taylor_pid, "NEW" if taylor_new else "EXIST"))

# ============ 2. 国籍 ============
rc = cur.execute(
    "INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) "
    "VALUES (%s,%s,0)", (taylor_pid, england_id),
)
if rc:
    print("  [nat] Kingdom of England (英格兰王国)")

# ============ 3. 职业 ============
for occ_en in ["mathematician"]:
    cur.execute("SELECT id FROM occupations WHERE name_en=%s", (occ_en,))
    r = cur.fetchone()
    if not r:
        print("  [warn] occupation not found: %s" % occ_en)
        continue
    rc = cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) "
        "VALUES (%s,%s,0)", (taylor_pid, r[0]),
    )
    if rc:
        print("  [occ] %s" % occ_en)

# ============ 4. 研究领域 ============
FIELDS = [
    "mathematical analysis", "mathematics", "calculus", "finite difference",
]
for f_en in FIELDS:
    fid = ef(f_en)
    rc = cur.execute(
        "INSERT IGNORE INTO person_field(person_id,field_id,`rank`) "
        "VALUES (%s,%s,0)", (taylor_pid, fid),
    )
    if rc:
        print("  [field] %s" % f_en)

# ============ 5. 社会关系 ============
# 导师（泰勒是学生）fwd=False
for adv, note in [
    ("John Machin", "学术指导者（academic advisor）"),
    ("John Keill", "学术指导者（academic advisor）"),
]:
    _, created, rc = ar(taylor_pid, "advisor-student", adv, note, fwd=False)
    if rc:
        print("  [rel] advisor %s (%s)" % (adv, "NEW" if created else "EXIST"))

# 优先权争议
for opp, note in [
    ("Johann Bernoulli", "中心振荡问题解的优先权争议"),
]:
    _, created, rc = ar(taylor_pid, "controversy", opp, note)
    if rc:
        print("  [rel] controversy %s (%s)" % (opp, "NEW" if created else "EXIST"))

# 同事 / 同代英国数学
for col, note in [
    ("Isaac Newton", "皇家学会微积分优先权之争裁定委员会同席"),
    ("Roger Cotes", "同代英国数学家，能与伯努利家族抗衡"),
]:
    _, created, rc = ar(taylor_pid, "colleague", col, note)
    if rc:
        print("  [rel] colleague %s (%s)" % (col, "NEW" if created else "EXIST"))

conn.commit()
print("=== COMMITTED ===")

# ============ 6. 回显校验 ============
cur.execute("SELECT COUNT(*) FROM person_field WHERE person_id=%s", (taylor_pid,))
print("person_field rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (taylor_pid, taylor_pid))
print("person_relation rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_nationality WHERE person_id=%s", (taylor_pid,))
print("person_nationality rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_occupation WHERE person_id=%s", (taylor_pid,))
print("person_occupation rows: %d" % cur.fetchone()[0])
conn.close()
