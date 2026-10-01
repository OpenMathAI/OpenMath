#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""入库 William Rowan Hamilton（哈密顿）的完整字段与社会关系。

数据源：
  - mathematician/presentations/19th_century/pages/William_Rowan_Hamilton/metadata.json
  - mathematician/presentations/19th_century/pages/William_Rowan_Hamilton/page.md
  - 立传提示词 §6（数据库字段核对表）/ §7（社会关系清单）
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

# ============ 字典 get-or-create ============
def gocc(occ_en, occ_zh=None):
    cur.execute("SELECT id FROM occupations WHERE name_en=%s", (occ_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES (%s,%s)", (occ_en, occ_zh))
    return cur.lastrowid

def gfield(f_en, f_zh=None):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (f_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (f_en, f_zh))
    return cur.lastrowid

def gaward(a_en, a_zh, a_type="honor"):
    cur.execute("SELECT id FROM awards WHERE name_en=%s", (a_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO awards(name_en, name_zh, award_type) VALUES (%s,%s,%s)",
                (a_en, a_zh, a_type))
    return cur.lastrowid

def ginstitution(i_en, i_zh):
    cur.execute("SELECT id FROM institutions WHERE name_en=%s", (i_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO institutions(name_en, name_zh) VALUES (%s,%s)", (i_en, i_zh))
    return cur.lastrowid

def gp(name, occ_en="mathematician"):
    """按 name_en 查找/创建关系节点占位，返回 (pid, created)。"""
    n = norm(name)
    if n in by_en:
        return by_en[n], False
    cur.execute(
        "INSERT INTO people(name_en, primary_occupation, has_biography) "
        "VALUES (%s,%s,0)", (name, occ_en),
    )
    pid = cur.lastrowid
    if occ_en:
        oid = gocc(occ_en)
        cur.execute(
            "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) "
            "VALUES (%s,%s,0)", (pid, oid),
        )
    by_en[n] = pid
    return pid, True

def rel(pid0, rt, name, note, direction=None, occ_en="mathematician"):
    pid, created = gp(name, occ_en)
    if rt in ("advisor-student", "parent-child"):
        if direction in ("advisor", "parent"):
            f, t = pid, pid0   # 对方是师/父
        elif direction in ("student", "child"):
            f, t = pid0, pid   # 对方是生/子
        else:
            f, t = sorted([pid0, pid])
    else:
        f, t = sorted([pid0, pid])
    cur.execute(
        "INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) "
        "VALUES (%s,%s,%s,%s,'hamilton')",
        (f, t, rt, note),
    )
    return pid, created, cur.rowcount

# ============ 1. Hamilton 本人 ============
cur.execute("SELECT id FROM people WHERE qid='Q11887'")
r = cur.fetchone()
if r:
    pid = r[0]
    cur.execute(
        "UPDATE people SET has_biography=1, has_social_data=1, gender='male' WHERE id=%s", (pid,),
    )
    print("Hamilton pid=%s (EXIST, has_biography -> 1)" % pid)
else:
    cur.execute(
        "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
        "description, primary_occupation, has_biography, has_social_data) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        ("Q11887", "William Rowan Hamilton", "哈密顿", "male", "1805-08-04", "1865-09-02",
         "Irish mathematician, physicist, and astronomer (1805-1865)",
         "mathematician", 1, 1),
    )
    pid = cur.lastrowid
    print("Hamilton pid=%s (NEW)" % pid)

# ============ 2. 国籍 ============
for c_en, c_zh in [("United Kingdom", "英国")]:
    cur.execute("SELECT id FROM countries WHERE name_en=%s", (c_en,))
    r = cur.fetchone()
    if not r:
        print("  [warn] country not found: %s" % c_en)
        continue
    if cur.execute("INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)", (pid, r[0])):
        print("  [nat] %s" % c_en)

# ============ 3. 职业 ============
for occ_en, occ_zh in [
    ("mathematician", "数学家"), ("physicist", "物理学家"), ("astronomer", "天文学家"),
    ("university teacher", "大学教师"), ("theoretical physicist", "理论物理学家"),
]:
    oid = gocc(occ_en, occ_zh)
    if cur.execute("INSERT IGNORE INTO person_occupation(person_id,occupation_id,`rank`) VALUES (%s,%s,0)", (pid, oid)):
        print("  [occ] %s" % occ_en)

# ============ 4. 研究领域 ============
for f_en, f_zh in [
    ("mathematics", "数学"), ("quaternion", "四元数"), ("mechanics", "力学"),
    ("optics", "光学"), ("mathematical physics", "数学物理"),
    ("astronomy", "天文学"), ("physics", "物理学"),
]:
    fid = gfield(f_en, f_zh)
    if cur.execute("INSERT IGNORE INTO person_field(person_id,field_id,`rank`) VALUES (%s,%s,0)", (pid, fid)):
        print("  [field] %s" % f_en)

# ============ 5. 机构 ============
for i_en, i_zh, reln, sy, ey in [
    ("Trinity College Dublin", "都柏林三一学院", "education", 1823, 1837),
    ("Trinity College Dublin", "都柏林三一学院", "employment", 1827, 1865),
    ("Dunsink Observatory", "邓辛克天文台", "employment", 1827, 1865),
]:
    iid = ginstitution(i_en, i_zh)
    if cur.execute(
        "INSERT IGNORE INTO person_institution(person_id,inst_id,relation,start_year,end_year) "
        "VALUES (%s,%s,%s,%s,%s)", (pid, iid, reln, sy, ey),
    ):
        print("  [inst] %s (%s)" % (i_en, reln))

# ============ 6. 奖项 ============
for a_en, a_zh, yr, note in [
    ("Cunningham Medal", "坎宁安奖章", 1834, "锥形折射预言"),
    ("Cunningham Medal", "坎宁安奖章", 1848, None),
    ("Knight Bachelor", "下级勋位爵士", 1835, None),
    ("Royal Medal", "皇家奖章", 1835, None),
    ("Fellow of the American Academy of Arts and Sciences", "美国艺术与科学院院士", 0, "年份待查"),
    ("Foreign Associate of the National Academy of Sciences", "美国国家科学院外籍院士", 1864, None),
]:
    aid = gaward(a_en, a_zh)
    if cur.execute(
        "INSERT IGNORE INTO award_laureate(person_id,award_id,year,share_type,note,source) "
        "VALUES (%s,%s,%s,'独享',%s,'hamilton')", (pid, aid, yr, note),
    ):
        print("  [award] %s (%s)" % (a_en, yr))

# ============ 7. 社会关系 ============
# 导师
_, created, rc = rel(pid, "advisor-student", "John Brinkley", "导师，称其'现在就是同龄人中第一数学家'", direction="advisor")
if rc:
    print("  [rel] advisor John Brinkley (%s)" % ("NEW" if created else "EXIST"))

# 合作者
for n2, note in [
    ("Carl Gustav Jacob Jacobi", "Hamilton–Jacobi 方程"),
    ("Arthur Cayley", "Cayley–Hamilton 定理"),
]:
    _, created, rc = rel(pid, "collaborator", n2, note)
    if rc:
        print("  [rel] collaborator %s (%s)" % (n2, "NEW" if created else "EXIST"))

# 同事 / 学术相关
for n2, note in [
    ("Joseph Liouville", "扩展其四元数与力学工作"),
    ("Augustus De Morgan", "通信"),
    ("Niels Henrik Abel", "五次方程研究"),
]:
    _, created, rc = rel(pid, "colleague", n2, note)
    if rc:
        print("  [rel] colleague %s (%s)" % (n2, "NEW" if created else "EXIST"))

# 诗人交往（占位职业标记为 poet）
for n2, note in [
    ("William Wordsworth", "诗人交往，自称'诗意门徒'"),
    ("Samuel Taylor Coleridge", "诗人交往，深受其哲学影响"),
    ("Felicia Hemans", "听其天文讲座后作诗"),
]:
    _, created, rc = rel(pid, "colleague", n2, note, occ_en="poet")
    if rc:
        print("  [rel] colleague(poet) %s (%s)" % (n2, "NEW" if created else "EXIST"))

# 亲属（子）
_, created, rc = rel(pid, "parent-child", "William Edwin Hamilton", "子，出版《四元数原理》", direction="child")
if rc:
    print("  [rel] child William Edwin Hamilton (%s)" % ("NEW" if created else "EXIST"))

conn.commit()
print("=== COMMITTED ===")

# ============ 8. 回显校验 ============
cur.execute("SELECT COUNT(*) FROM person_field WHERE person_id=%s", (pid,))
print("person_field rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (pid, pid))
print("person_relation rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_nationality WHERE person_id=%s", (pid,))
print("person_nationality rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_occupation WHERE person_id=%s", (pid,))
print("person_occupation rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM award_laureate WHERE person_id=%s", (pid,))
print("award_laureate rows: %d" % cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM person_institution WHERE person_id=%s", (pid,))
print("person_institution rows: %d" % cur.fetchone()[0])
conn.close()
