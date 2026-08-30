#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量入库 19 世纪数学家（Legendre + Fourier..Kronecker）的社会关系与研究领域。"""
import re
import sys
import unicodedata

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\'\.\(\)·,\-]", "", s).lower()


conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id, name_en, name_zh FROM people")
by_en, by_zh = {}, {}
for pid, en, zh in cur.fetchall():
    if en:
        by_en[norm(en)] = pid
    if zh:
        by_zh[norm(zh)] = pid
cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
occ_id = cur.fetchone()[0]


def gp(name):
    n = norm(name)
    if n in by_en:
        return by_en[n], False
    if n in by_zh:
        return by_zh[n], False
    cur.execute(
        "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'mathematician',0)",
        (name,),
    )
    pid = cur.lastrowid
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (pid, occ_id),
    )
    by_en[n] = pid
    return pid, True


def ef(f_en, f_zh=None):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (f_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (f_en, f_zh))
    return cur.lastrowid


def ec(c_en, c_zh=None, succ=None):
    cur.execute("SELECT id FROM countries WHERE name_en=%s", (c_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute(
        "INSERT INTO countries(name_en, name_zh, is_current, successor) VALUES (%s,%s,%s,%s)",
        (c_en, c_zh, 1 if succ is None else 0, succ),
    )
    return cur.lastrowid


def ar(pid0, rt, name, note, fwd=True):
    pid, _ = gp(name)
    if rt == "advisor-student":
        f, t = (pid0, pid) if fwd else (pid, pid0)
    else:
        f, t = sorted([pid0, pid])
    cur.execute(
        "INSERT IGNORE INTO person_relation(from_id,to_id,relation_type,note,source) VALUES (%s,%s,%s,%s,'19c-batch')",
        (f, t, rt, note),
    )
    return cur.rowcount


def proc(p):
    pid, created = gp(p["name_en"])
    cur.execute(
        "UPDATE people SET qid=%s,name_zh=%s,description=%s,birth_date=%s,death_date=%s,has_social_data=1 WHERE id=%s",
        (p["qid"], p["name_zh"], p["desc"], p["dob"], p["dod"], pid),
    )
    for c_en, c_zh, succ in p.get("nat", []):
        cid = ec(c_en, c_zh, succ)
        cur.execute(
            "INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)",
            (pid, cid),
        )
    for f_en in p.get("fields", []):
        fid = ef(f_en)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id,field_id,`rank`) VALUES (%s,%s,0)",
            (pid, fid),
        )
    for adv in p.get("advisors", []):
        ar(pid, "advisor-student", adv, "导师", fwd=False)
    for stu in p.get("students", []):
        ar(pid, "advisor-student", stu, "学生", fwd=True)
    for n2, note in p.get("colleagues", []):
        ar(pid, "colleague", n2, note)
    for n2, note in p.get("collaborators", []):
        ar(pid, "collaborator", n2, note)
    for n2, note in p.get("rivals", []):
        ar(pid, "rival", n2, note)
    print(("NEW " if created else "EXIST") + " " + p["name_en"] + " id=" + str(pid))


M = [
    dict(name_en="Adrien-Marie Legendre", name_zh="勒让德", qid="Q191021",
         dob="1752-09-18", dod="1833-01-09", desc="French mathematician (1752-1833)",
         nat=[("France", "法国", None)],
         fields=["number theory", "elliptic function", "geometry", "mathematical analysis", "least squares"],
         advisors=["Joseph-Louis Lagrange"], students=[],
         colleagues=[("Carl Friedrich Gauss", "最小二乘法优先权"),
                     ("Peter Gustav Lejeune Dirichlet", "费马大定理n=5独立证明"),
                     ("Niels Henrik Abel", "椭圆函数承前"),
                     ("Carl Gustav Jacob Jacobi", "椭圆函数"),
                     ("Joseph Fourier", "同期法国数学家")],
         rivals=[("Carl Friedrich Gauss", "最小二乘法优先权争议")], collaborators=[]),
    dict(name_en="Joseph Fourier", name_zh="傅里叶", qid="Q8772",
         dob="1768-03-21", dod="1830-05-16", desc="French mathematician and physicist (1768-1830)",
         nat=[("France", "法国", None)],
         fields=["mathematical analysis", "Fourier series", "mathematical physics", "heat conduction"],
         advisors=["Jean-Baptiste Biot", "Joseph-Louis Lagrange"],
         students=["Peter Gustav Lejeune Dirichlet"],
         colleagues=[("Adrien-Marie Legendre", "同期法国数学家")], rivals=[], collaborators=[]),
    dict(name_en="Sophie Germain", name_zh="热尔曼", qid="Q7103",
         dob="1776-04-01", dod="1831-06-27", desc="French mathematician (1776-1831)",
         nat=[("France", "法国", None)],
         fields=["number theory", "mechanics", "elasticity theory"],
         advisors=["Carl Friedrich Gauss"], students=[],
         colleagues=[("Joseph-Louis Lagrange", "通信指导")], rivals=[], collaborators=[]),
    dict(name_en="Carl Friedrich Gauss", name_zh="高斯", qid="Q6722",
         dob="1777-04-30", dod="1855-02-23", desc="German mathematician (1777-1855)",
         nat=[("Germany", "德国", None)],
         fields=["number theory", "differential geometry", "mathematical analysis", "statistics", "astronomy"],
         advisors=["Johann Friedrich Pfaff"],
         students=["Richard Dedekind", "Bernhard Riemann", "Gotthold Eisenstein"],
         colleagues=[("Adrien-Marie Legendre", "最小二乘法优先权"), ("Sophie Germain", "通信指导")],
         rivals=[("Adrien-Marie Legendre", "最小二乘法优先权争议")], collaborators=[]),
    dict(name_en="Bernhard Bolzano", name_zh="波尔查诺", qid="Q184735",
         dob="1781-10-05", dod="1848-12-18", desc="Bohemian mathematician and philosopher (1781-1848)",
         nat=[("Kingdom of Bohemia", "波西米亚王国", "Czechia")],
         fields=["mathematical analysis", "logic", "set theory", "philosophy"],
         advisors=[], students=[],
         colleagues=[("Karl Weierstrass", "波尔查诺-魏尔斯特拉斯定理")], rivals=[], collaborators=[]),
    dict(name_en="Siméon Denis Poisson", name_zh="泊松", qid="Q190772",
         dob="1781-06-21", dod="1840-04-25", desc="French mathematician and physicist (1781-1840)",
         nat=[("France", "法国", None)],
         fields=["mathematical analysis", "probability theory", "mechanics", "theoretical physics"],
         advisors=["Joseph-Louis Lagrange", "Pierre-Simon Laplace"],
         students=["Joseph Liouville", "Peter Gustav Lejeune Dirichlet", "Michel Chasles"],
         colleagues=[], rivals=[], collaborators=[]),
    dict(name_en="Jean-Victor Poncelet", name_zh="庞斯莱", qid="Q168452",
         dob="1788-07-01", dod="1867-12-22", desc="French mathematician and engineer (1788-1867)",
         nat=[("France", "法国", None)],
         fields=["projective geometry", "mechanics"],
         advisors=["Gaspard Monge"], students=[],
         colleagues=[], rivals=[], collaborators=[]),
    dict(name_en="Augustin-Louis Cauchy", name_zh="柯西", qid="Q8814",
         dob="1789-08-21", dod="1857-05-23", desc="French mathematician (1789-1857)",
         nat=[("France", "法国", None)],
         fields=["mathematical analysis", "complex analysis", "mechanics", "abstract algebra"],
         advisors=[], students=["Viktor Bunyakovsky", "Francesco Faà di Bruno"],
         colleagues=[("Niels Henrik Abel", "巴黎定理被其搁置")], rivals=[], collaborators=[]),
    dict(name_en="Carl Gustav Jacob Jacobi", name_zh="雅可比", qid="Q76564",
         dob="1804-12-10", dod="1851-02-18", desc="German mathematician (1804-1851)",
         nat=[("Germany", "德国", None)],
         fields=["differential geometry", "number theory", "elliptic function", "mechanics"],
         advisors=["Enno Dirksen"],
         students=["Carl Wilhelm Borchardt", "Paul Gordan", "Otto Hesse"],
         colleagues=[("Adrien-Marie Legendre", "椭圆函数")],
         rivals=[("Niels Henrik Abel", "椭圆函数双周期性竞争")], collaborators=[]),
    dict(name_en="Peter Gustav Lejeune Dirichlet", name_zh="狄利克雷", qid="Q29193",
         dob="1805-02-13", dod="1859-05-05", desc="German mathematician (1805-1859)",
         nat=[("Germany", "德国", None)],
         fields=["number theory", "mathematical analysis", "analytic number theory"],
         advisors=["Siméon Denis Poisson", "Joseph Fourier", "Carl Friedrich Gauss"],
         students=["Gotthold Eisenstein", "Leopold Kronecker", "Richard Dedekind", "Bernhard Riemann"],
         colleagues=[("Adrien-Marie Legendre", "费马大定理n=5独立证明")], rivals=[], collaborators=[]),
    dict(name_en="William Rowan Hamilton", name_zh="哈密顿", qid="Q11887",
         dob="1805-08-04", dod="1865-09-02", desc="Irish mathematician (1805-1865)",
         nat=[("United Kingdom", "英国", None)],
         fields=["mechanics", "quaternion", "optics", "mathematical physics"],
         advisors=["John Brinkley"], students=[],
         colleagues=[], rivals=[], collaborators=[]),
    dict(name_en="Joseph Liouville", name_zh="刘维尔", qid="Q214549",
         dob="1809-03-24", dod="1882-09-08", desc="French mathematician (1809-1882)",
         nat=[("France", "法国", None)],
         fields=["mathematical analysis", "algebra", "number theory", "differential calculus"],
         advisors=["Siméon Denis Poisson", "Louis Jacques Thénard"],
         students=["Charles Hermite", "Eugène Charles Catalan"],
         colleagues=[], rivals=[], collaborators=[]),
    dict(name_en="Ernst Kummer", name_zh="库默尔", qid="Q57245",
         dob="1810-01-29", dod="1893-05-14", desc="German mathematician (1810-1893)",
         nat=[("Germany", "德国", None)],
         fields=["number theory", "ideal theory", "applied mathematics"],
         advisors=["Heinrich Scherk"],
         students=["Gotthold Eisenstein", "Ferdinand Georg Frobenius", "Georg Cantor"],
         colleagues=[], rivals=[], collaborators=[]),
    dict(name_en="James Joseph Sylvester", name_zh="西尔维斯特", qid="Q310781",
         dob="1814-09-03", dod="1897-03-15", desc="British mathematician (1814-1897)",
         nat=[("United Kingdom", "英国", None)],
         fields=["algebra", "combinatorics", "matrix theory"],
         advisors=["John Hymers", "Augustus De Morgan"], students=[],
         colleagues=[], rivals=[], collaborators=[("Arthur Cayley", "不变量理论")]),
    dict(name_en="George Boole", name_zh="布尔", qid="Q134661",
         dob="1815-11-02", dod="1864-12-08", desc="English mathematician and logician (1815-1864)",
         nat=[("United Kingdom", "英国", None)],
         fields=["mathematical logic", "algebra"],
         advisors=[], students=[],
         colleagues=[("Augustus De Morgan", "逻辑学同侪")], rivals=[], collaborators=[]),
    dict(name_en="Karl Weierstrass", name_zh="魏尔斯特拉斯", qid="Q57103",
         dob="1815-10-31", dod="1897-02-19", desc="German mathematician (1815-1897)",
         nat=[("Germany", "德国", None)],
         fields=["complex analysis", "mathematical analysis", "elliptic function"],
         advisors=["Christoph Gudermann"],
         students=["Georg Cantor", "Ferdinand Georg Frobenius", "Sofia Kovalevskaya", "Hermann Schwarz"],
         colleagues=[("Bernhard Bolzano", "波尔查诺-魏尔斯特拉斯定理")], rivals=[], collaborators=[]),
    dict(name_en="Arthur Cayley", name_zh="凯莱", qid="Q159430",
         dob="1821-08-16", dod="1895-01-26", desc="British mathematician (1821-1895)",
         nat=[("United Kingdom", "英国", None)],
         fields=["graph theory", "group theory", "matrix theory", "algebra"],
         advisors=["George Peacock", "William Hopkins"],
         students=["H. F. Baker", "Andrew Forsyth"],
         colleagues=[], rivals=[], collaborators=[("James Joseph Sylvester", "不变量理论")]),
    dict(name_en="Charles Hermite", name_zh="埃尔米特", qid="Q168401",
         dob="1822-12-24", dod="1901-01-14", desc="French mathematician (1822-1901)",
         nat=[("France", "法国", None)],
         fields=["algebra", "number theory", "mathematical analysis", "orthogonal polynomials"],
         advisors=["Eugène Charles Catalan", "Joseph Liouville"],
         students=["Henri Poincaré", "Thomas Stieltjes"],
         colleagues=[], rivals=[], collaborators=[]),
    dict(name_en="Gotthold Eisenstein", name_zh="艾森斯坦", qid="Q61047",
         dob="1823-04-16", dod="1852-10-11", desc="German mathematician (1823-1852)",
         nat=[("Germany", "德国", None)],
         fields=["number theory", "elliptic function", "mathematical analysis"],
         advisors=["Ernst Kummer", "Nikolaus Wolfgang Fischer"], students=[],
         colleagues=[("Carl Friedrich Gauss", "受其赏识")], rivals=[], collaborators=[]),
    dict(name_en="Leopold Kronecker", name_zh="克罗内克", qid="Q76410",
         dob="1823-12-07", dod="1891-12-29", desc="German mathematician (1823-1891)",
         nat=[("Germany", "德国", None)],
         fields=["number theory", "logic", "determinant"],
         advisors=["Johann Encke", "Peter Gustav Lejeune Dirichlet"],
         students=["Kurt Hensel", "Adolf Kneser"],
         colleagues=[("Georg Cantor", "有限主义vs集合论之争")],
         rivals=[("Georg Cantor", "数学基础之争")], collaborators=[]),
]


if __name__ == "__main__":
    for p in M:
        proc(p)
    conn.commit()
    print("=== ALL DONE ===")
    conn.close()
