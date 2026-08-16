#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Martin Hairer 的数据库字段与社会关系，入库 greatminds 数据库。

数据源：提示词 Martin_Hairer_zh.md + Fields_Medal/pages/2014/Martin Hairer
注意：在世数学家（1975-），无死亡日期。双重国籍（奥地利+英国），出生瑞士日内瓦。
"""
import re
import unicodedata
import json

from db_mysql import get_conn

NAME = "Martin Hairer"
QID = "Q1420765"

# 关系：(relation_type, 人物, note)
# 方向约定：
#   advisor-student：Jean-Pierre Eckmann → Hairer（导师）
#   parent-child：Ernst Hairer → Hairer（父）
#   spouse：无向
#   co-honored：无向（2014 Fields Medal 同届）
RELATIONS = [
    # 导师（→ Hairer）
    ("advisor-student", "Jean-Pierre Eckmann", "博士导师（日内瓦大学 2001，物理学博士）"),
    # 父亲
    ("parent-child", "Ernst Hairer", "父亲，日内瓦大学数学家（数值分析与常微分方程）"),
    # 妻子（无向）
    ("spouse", "Li Xue-Mei", "妻子（李雪梅），数学家（随机分析），2003 年结婚"),
    # 同获 2014 菲尔兹奖（无向）
    ("co-honored", "Artur Avila", "同获 2014 菲尔兹奖"),
    ("co-honored", "Maryam Mirzakhani", "同获 2014 菲尔兹奖（首位女性获奖者）"),
    ("co-honored", "Manjul Bhargava", "同获 2014 菲尔兹奖"),
]

FIELDS = [
    ("probability theory", "概率论", 0),
    ("stochastic analysis", "随机分析", 1),
    ("stochastic partial differential equations", "随机偏微分方程", 2),
    ("regularity structures", "正则结构理论", 3),
    ("rough path theory", "粗糙路径理论", 4),
]

OCCUPATIONS = [("mathematician", 0), ("physicist", 1)]

INSTITUTIONS = [
    ("University of Geneva", "education", 1994, 2001),
    ("University of Warwick", "employment", 2001, 2017),
    ("Imperial College London", "employment", 2017, 2022),
    ("École Polytechnique Fédérale de Lausanne", "employment", 2022, None),
    ("Courant Institute of Mathematical Sciences", "employment", None, None),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # ---------- 1. Hairer 本人字段补齐 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if not row:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',1,%s)",
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
            "马丁·海尔",
            json.dumps(["Martin Hairer", "正则结构理论之父", "随机偏微分方程", "Amadeus 软件作者"], ensure_ascii=False),
            "Austrian-British mathematician, Fields Medal 2014 (born 1975)",
            "male",
            "1975-11-14",
            "mathematician",
            pid0,
        ),
    )
    print(f"Hairer id={pid0} 已补齐 people 字段（has_biography=1, has_social_data=1）")

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

    # ---------- 4. 国籍（奥地利 + 英国双重国籍） ----------
    cur.execute("SELECT id, name_en FROM countries WHERE name_en IN ('Austria','United Kingdom')")
    for cid, cname in cur.fetchall():
        rank = 0 if cname == "Austria" else 1
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                    (pid0, cid, rank))
        print(f"  国籍 + {cname} (rank={rank})")
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
            f, t = pid, pid0  # 导师 → Hairer
        elif rel == "parent-child":
            f, t = pid, pid0  # 父 → Hairer
        else:
            f, t = sorted([pid0, pid])  # 无向

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Martin_Hairer')",
            (f, t, rel, note),
        )
        if cur.rowcount:
            added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")

    print("\n=== 校验：Martin Hairer 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Martin Hairer' OR b.name_en='Martin Hairer'
        ORDER BY rt.relation_key, a.name_en, b.name_en"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
