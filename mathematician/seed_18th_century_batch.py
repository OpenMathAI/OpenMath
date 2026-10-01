#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量入库 18 世纪 8 位数学家的社会关系与研究领域。

数据源：presentations/18th_century/pages/<Name>/metadata.json + page.md
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
    """按 name_en 查找/创建人物（关系节点），返回 (pid, created)。"""
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

def gcountry(c_en, c_zh, successor=None):
    cur.execute("SELECT id FROM countries WHERE name_en=%s", (c_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute(
        "INSERT INTO countries(name_en, name_zh, is_current, successor) "
        "VALUES (%s,%s,%s,%s)",
        (c_en, c_zh, 1 if successor is None else 0, successor),
    )
    return cur.lastrowid

def gocc(occ_en):
    cur.execute("SELECT id FROM occupations WHERE name_en=%s", (occ_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO occupations(name_en) VALUES (%s)", (occ_en,))
    return cur.lastrowid

def gfield(f_en):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (f_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO fields(name_en) VALUES (%s)", (f_en,))
    return cur.lastrowid

def rel(pid0, rt, name, note, fwd=True):
    pid, created = gp(name)
    if rt == "advisor-student":
        f, t = (pid0, pid) if fwd else (pid, pid0)
    elif rt == "parent-child":
        f, t = pid, pid0  # 长辈 -> 本人
    else:
        f, t = sorted([pid0, pid])
    cur.execute(
        "INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) "
        "VALUES (%s,%s,%s,%s,%s)",
        (f, t, rt, note, src),
    )
    return pid, created, cur.rowcount

def run(P):
    global src
    src = P["src"]
    # 本人：按 qid 查找
    cur.execute("SELECT id FROM people WHERE qid=%s", (P["qid"],))
    r = cur.fetchone()
    if r:
        pid, new = r[0], False
    else:
        cur.execute(
            "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (P["qid"], P["name_en"], P["name_zh"], "male", P["birth"], P["death"],
             P["desc"], "mathematician", 1, 1),
        )
        pid, new = cur.lastrowid, True
    print("%s pid=%s (%s)" % (P["name_en"], pid, "NEW" if new else "EXIST"))
    # 国籍
    for c_en, c_zh, succ in P["nat"]:
        cid = gcountry(c_en, c_zh, succ)
        if cur.execute("INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)", (pid, cid)):
            print("  [nat] %s" % c_en)
    # 职业
    for occ in P["occ"]:
        oid = gocc(occ)
        if cur.execute("INSERT IGNORE INTO person_occupation(person_id,occupation_id,`rank`) VALUES (%s,%s,0)", (pid, oid)):
            print("  [occ] %s" % occ)
    # 领域
    for f in P["fields"]:
        fid = gfield(f)
        if cur.execute("INSERT IGNORE INTO person_field(person_id,field_id,`rank`) VALUES (%s,%s,0)", (pid, fid)):
            print("  [field] %s" % f)
    # 导师
    for adv, note in P.get("advisors", []):
        _, created, rc = rel(pid, "advisor-student", adv, note, fwd=False)
        if rc:
            print("  [rel] advisor %s (%s)" % (adv, "NEW" if created else "EXIST"))
    # 学生
    for stu, note in P.get("students", []):
        _, created, rc = rel(pid, "advisor-student", stu, note, fwd=True)
        if rc:
            print("  [rel] student %s (%s)" % (stu, "NEW" if created else "EXIST"))
    # 同事 / 合作
    for n2, note in P.get("colleagues", []):
        _, created, rc = rel(pid, "colleague", n2, note)
        if rc:
            print("  [rel] colleague %s (%s)" % (n2, "NEW" if created else "EXIST"))
    # 父母
    for par, note in P.get("parents", []):
        _, created, rc = rel(pid, "parent-child", par, note)
        if rc:
            print("  [rel] parent %s (%s)" % (par, "NEW" if created else "EXIST"))

DATA = [
    dict(
        src="demoivre", qid="Q200397", name_en="Abraham de Moivre", name_zh="棣莫弗",
        birth="1667-05-26", death="1754-11-27",
        desc="French mathematician (1667-1754)",
        nat=[("France", "法国", None)],
        occ=["mathematician", "statistician", "astronomer"],
        fields=["probability theory", "mathematics", "statistics", "astronomy"],
        advisors=[("Jacques Ozanam", "私人数学辅导（formal training）")],
        colleagues=[
            ("Isaac Newton", "挚友，晚年推举其解答数学难题"),
            ("Edmond Halley", "挚友，向皇家学会传达其首篇论文"),
            ("James Stirling", "Stirling 近似与阶乘研究的通信伙伴"),
        ],
    ),
    dict(
        src="maclaurin", qid="Q8755", name_en="Colin Maclaurin", name_zh="麦克劳林",
        birth="1698-02-00", death="1746-06-14",
        desc="Scottish mathematician (1698-1746)",
        nat=[("Kingdom of Scotland", "苏格兰王国", "United Kingdom"),
             ("Kingdom of Great Britain", "大不列颠王国", "United Kingdom")],
        occ=["mathematician", "physicist", "astronomer"],
        fields=["mathematics"],
        advisors=[("Robert Simson", "学术导师（academic advisor）")],
        students=[("James Hutton", "学生（地质学之父，数学受业）")],
        colleagues=[
            ("Isaac Newton", "相识于伦敦，牛顿力荐其任爱丁堡教职"),
            ("Alexis Clairaut", "椭球引力问题通信"),
            ("Pierre Louis Maupertuis", "椭球引力问题通信"),
        ],
    ),
    dict(
        src="daniel-bernoulli", qid="Q122366", name_en="Daniel Bernoulli", name_zh="丹尼尔·伯努利",
        birth="1700-02-08", death="1782-03-17",
        desc="Swiss mathematician and physicist (1700-1782)",
        nat=[("Switzerland", "瑞士", None)],
        occ=["mathematician", "physicist", "university teacher", "economist", "physician", "statistician", "botanist"],
        fields=["mathematical analysis", "probability theory", "differential calculus",
                "physics", "mechanics", "mathematical physics"],
        advisors=[("Johann Bernoulli", "父亲，私授数学（doctor 父亲）")],
        students=[("Johann III Bernoulli", "侄子兼学生")],
        colleagues=[
            ("Leonhard Euler", "挚友，共同创立 Euler-Bernoulli 梁理论"),
            ("Christian Goldbach", "合作出版《Exercitationes》"),
        ],
        parents=[("Johann Bernoulli", "父亲")],
    ),
    dict(
        src="clairaut", qid="Q28937", name_en="Alexis Clairaut", name_zh="克莱罗",
        birth="1713-05-13", death="1765-05-17",
        desc="French mathematician, astronomer, and geophysicist (1713-1765)",
        nat=[("France", "法国", None)],
        occ=["astronomer", "mathematician", "physicist", "geodesist"],
        fields=["mathematics", "mechanics", "astronomy", "geodesy"],
        students=[("Pierre Charles Le Monnier", "学生")],
        colleagues=[
            ("Pierre Louis Maupertuis", "1736 拉普兰大地测量探险同伴"),
            ("Émilie du Châtelet", "协助其翻译牛顿《原理》"),
            ("Leonhard Euler", "三体问题/月球远地点竞争"),
            ("Jean le Rond d'Alembert", "三体问题/月球远地点竞争"),
        ],
    ),
    dict(
        src="lambert", qid="Q122999", name_en="Johann Heinrich Lambert", name_zh="兰伯特",
        birth="1728-08-26", death="1777-09-25",
        desc="German mathematician, physicist and astronomer (1728-1777)",
        nat=[("Republic of Mulhouse", "米卢斯共和国", "France"), ("France", "法国", None)],
        occ=["mathematician", "astronomer", "physicist", "philosopher", "writer"],
        fields=["mathematics"],
        advisors=[("Abraham Gotthelf Kästner", "学术导师"),
                  ("Tobias Mayer", "学术导师")],
        colleagues=[
            ("Leonhard Euler", "柏林科学院同事"),
            ("Frederick the Great", "资助者，邀其入普鲁士科学院"),
            ("Immanuel Kant", "哲学通信，康德曾欲献《纯粹理性批判》"),
        ],
    ),
    dict(
        src="bezout", qid="Q289471", name_en="Étienne Bézout", name_zh="贝祖",
        birth="1730-03-31", death="1783-09-27",
        desc="French mathematician (1730-1783)",
        nat=[("Kingdom of France", "法兰西王国", "France")],
        occ=["mathematician"],
        fields=["number theory"],
        colleagues=[("Leonhard Euler", "早年深受欧拉影响")],
    ),
    dict(
        src="waring", qid="Q323028", name_en="Edward Waring", name_zh="华林",
        birth="1736-01-01", death="1798-08-15",
        desc="English mathematician",
        nat=[("Kingdom of Great Britain", "大不列颠王国", "United Kingdom")],
        occ=["mathematician", "university teacher", "scientist"],
        fields=["number theory", "mathematics", "number"],
        students=[("John Dawson", "学生（外科医生）"),
                  ("John Wilson", "学生，Wilson 定理以其命名")],
        colleagues=[("Joseph-Louis Lagrange", "评价其《Meditationes Algebraicae》为'充满卓越研究之作'")],
    ),
    dict(
        src="monge", qid="Q206832", name_en="Gaspard Monge", name_zh="蒙日",
        birth="1746-05-09", death="1818-07-28",
        desc="French mathematician, inventor of descriptive geometry (1746-1818)",
        nat=[("France", "法国", None)],
        occ=["mathematician", "politician", "physicist", "university teacher",
             "engineer", "chemist", "teacher"],
        fields=["differential geometry"],
        students=[("Jean-Victor Poncelet", "学生"),
                  ("Jean-Baptiste Biot", "学生"),
                  ("Joseph Diez Gergonne", "学生")],
        colleagues=[
            ("Napoleon Bonaparte", "挚友，随其远征埃及"),
            ("Claude Louis Berthollet", "化学合作，共同创办法国工艺学校"),
            ("Pierre-Simon Laplace", "共同创办 École Polytechnique"),
            ("Lazare Carnot", "共同创办 École Polytechnique"),
        ],
    ),
]

for P in DATA:
    run(P)

conn.commit()
print("=== COMMITTED ===")

# 回显校验
for P in DATA:
    cur.execute("SELECT id FROM people WHERE qid=%s", (P["qid"],))
    pid = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM person_field WHERE person_id=%s", (pid,))
    nf = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (pid, pid))
    nr = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM person_nationality WHERE person_id=%s", (pid,))
    nn = cur.fetchone()[0]
    print("%-22s field=%d rel=%d nat=%d" % (P["name_en"], nf, nr, nn))
conn.close()
