#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Edward Witten 的数据库字段与社会关系，入库 greatminds 数据库。

数据源：提示词 Edward_Witten_zh.md + Fields_Medal/pages/1990/Edward Witten
注意：在世物理学家（1951-），无死亡日期。
"""
import re
import unicodedata
import json

from db_mysql import get_conn

NAME = "Edward Witten"
QID = "Q160633"

# 关系：(relation_type, 人物, note)
# 方向约定：
#   advisor-student：ADVISORS 中的人 → Witten（导师）；其余 → 学生（Witten → 学生）
#   parent-child：Louis Witten → Witten（父）
#   其余（collaborator/co-honored）：无向
RELATIONS = [
    # 导师（→ Witten）
    ("advisor-student", "David Gross", "博士导师（普林斯顿大学 1976），2004 诺贝尔物理学奖得主"),
    ("advisor-student", "Michael Atiyah", "学术导师/伯乐，1990 菲尔兹奖书面致辞人"),
    ("advisor-student", "Sidney Coleman", "学术顾问（哈佛时期）"),
    # 学生（Witten →）
    ("advisor-student", "Cumrun Vafa", "学生，弦论学家"),
    ("advisor-student", "Xiao-Gang Wen", "学生（文小刚），凝聚态理论物理学家"),
    ("advisor-student", "Dror Bar-Natan", "学生，纽结理论与量子不变量"),
    ("advisor-student", "Eva Silverstein", "学生，弦论宇宙学"),
    ("advisor-student", "Sergei Gukov", "学生，数学物理"),
    ("advisor-student", "Shamit Kachru", "学生，弦论与紧化"),
    # 合作者（无向）
    ("collaborator", "Nathan Seiberg", "合作者，Seiberg–Witten 理论（4-流形拓扑）"),
    ("collaborator", "Anton Kapustin", "合作者，S-对偶与几何 Langlands 对应"),
    ("collaborator", "Ruth Britto", "合作者，BCFW 递推关系"),
    ("collaborator", "Pierre Deligne", "合编《Quantum Fields and Strings》"),
    ("collaborator", "Michael Green", "合著《Superstring Theory》两卷本"),
    ("collaborator", "John Schwarz", "合著《Superstring Theory》两卷本"),
    ("collaborator", "Juan Maldacena", "AdS/CFT 对应提出者，Witten 在其基础上做奠基工作"),
    # 同获荣誉（无向）
    ("co-honored", "Vladimir Drinfeld", "同获 1990 菲尔兹奖"),
    ("co-honored", "Vaughan Jones", "同获 1990 菲尔兹奖；Witten 用 TQFT 重新诠释其 Jones 多项式"),
    ("co-honored", "Shigefumi Mori", "同获 1990 菲尔兹奖（森重文）"),
    # 父亲
    ("parent-child", "Louis Witten", "父亲，理论物理学家（引力与广义相对论）"),
]

ADVISORS = {"David Gross", "Michael Atiyah", "Sidney Coleman"}

FIELDS = [
    ("theoretical physics", "理论物理", 0),
    ("mathematical physics", "数学物理", 1),
    ("superstring theory", "超弦理论", 2),
]

OCCUPATIONS = [("physicist", 0), ("mathematician", 1)]

INSTITUTIONS = [
    ("Brandeis University", "education", 1967, 1971),
    ("Princeton University", "education", 1973, 1976),
    ("Harvard University", "employment", 1976, 1980),
    ("Oxford University", "employment", 1977, 1978),
    ("Institute for Advanced Study", "employment", 1980, None),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # ---------- 1. Witten 本人字段补齐 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if not row:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'physicist',1,%s)",
            (NAME, QID),
        )
        pid0 = cur.lastrowid
    else:
        pid0 = row[0]
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "gender=%s, birth_date=%s, death_date=NULL, primary_occupation=%s, "
        "has_biography=1, has_social_data=1 WHERE id=%s",
        (
            QID,
            "爱德华·威滕",
            json.dumps(["Edward Witten", "M理论之父", "拓扑量子场论", "第一位获菲尔兹奖的物理学家"], ensure_ascii=False),
            "American theoretical physicist, Fields Medal 1990 (born 1951)",
            "male",
            "1951-08-26",
            "physicist",
            pid0,
        ),
    )
    print(f"Witten id={pid0} 已补齐 people 字段（has_biography=1, has_social_data=1）")

    # ---------- 2. 职业 ----------
    for occ, rank in OCCUPATIONS:
        cur.execute("SELECT id FROM occupations WHERE name_en=%s", (occ,))
        orow = cur.fetchone()
        if not orow:
            cur.execute("INSERT INTO occupations(name_en) VALUES (%s)", (occ,))
            oid = cur.lastrowid
        else:
            oid = orow[0]
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,%s)",
                    (pid0, oid, rank))
    print("  职业关联完成")

    # ---------- 3. 领域 ----------
    for f_en, f_zh, rank in FIELDS:
        cur.execute("SELECT id FROM fields WHERE name_en=%s", (f_en,))
        frow = cur.fetchone()
        if not frow:
            cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (f_en, f_zh))
            fid = cur.lastrowid
        else:
            fid = frow[0]
        cur.execute("INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
                    (pid0, fid, rank))
    print("  领域关联完成")

    # ---------- 4. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='United States'")
    us = cur.fetchone()
    if us:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, us[0]))
    print("  国籍关联完成")

    # ---------- 5. 机构 ----------
    for inst, rel, sy, ey in INSTITUTIONS:
        cur.execute("SELECT id FROM institutions WHERE name_en=%s", (inst,))
        irow = cur.fetchone()
        if not irow:
            cur.execute("INSERT INTO institutions(name_en) VALUES (%s)", (inst,))
            iid = cur.lastrowid
        else:
            iid = irow[0]
        cur.execute(
            "SELECT 1 FROM person_institution WHERE person_id=%s AND inst_id=%s AND relation=%s",
            (pid0, iid, rel),
        )
        if not cur.fetchone():
            cur.execute(
                "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
                "VALUES (%s,%s,%s,%s,%s)",
                (pid0, iid, rel, sy, ey),
            )
    print("  机构关联完成")

    # ---------- 6. 社会关系 ----------
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_math = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'mathematician',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                        (pid, occ_math))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name} (id={pid})")
        else:
            print(f"  已有: {name} (id={pid})")

        if rel == "advisor-student":
            if name in ADVISORS:
                f, t = pid, pid0  # 导师 → Witten
            else:
                f, t = pid0, pid  # Witten → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 父 → Witten
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Edward_Witten')",
            (f, t, rel, note),
        )
        if cur.rowcount:
            added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")

    print("\n=== 校验：Edward Witten 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Edward Witten' OR b.name_en='Edward Witten'
        ORDER BY rt.relation_key, a.name_en, b.name_en"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:36]}")

    conn.close()


if __name__ == "__main__":
    main()
