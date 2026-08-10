#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Vladimir Arnold 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "Vladimir Arnold"
PEOPLE_UPDATE = {
    "name_zh": "弗拉基米尔·阿诺尔德",
    "name_variants": json.dumps(["KAM 定理的 A", "奇点理论大师", "Hilbert 第13问题的解决者"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1937-06-12",
    "death_date": "2010-06-03",
    "description": "Russian mathematician (1937–2010)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("topologist", 1), ("university teacher", 2), ("physicist", 3)]
PERSON_FIELDS = ["dynamical systems", "topology", "mathematical analysis", "differential calculus", "chaos theory", "mechanics", "algebraic geometry", "mathematics"]
PERSON_INSTITUTIONS = [
    ("Lomonosov Moscow State University", "莫斯科国立大学", "education", None, None),
    ("Lomonosov Moscow State University", "莫斯科国立大学", "employment", 1959, 1986),
    ("Steklov Institute of Mathematics", "斯捷克洛夫数学研究所", "employment", 1986, 2010),
    ("Paris Dauphine University", "巴黎第九大学", "employment", 1986, 2010),
    ("Utrecht University", "乌得勒支大学", "employment", None, None),
    ("Independent University of Moscow", "莫斯科独立大学", "employment", 1991, 2010),
]
NATIONALITIES = ["Soviet Union", "Russia"]


def main():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if not row:
        print("⚠ 不在库"); return
    pid = row[0]
    print(f"目标: {NAME} (id={pid})")
    sets = ", ".join(f"{k}=%s" for k in PEOPLE_UPDATE)
    cur.execute(f"UPDATE people SET {sets} WHERE id=%s", (*PEOPLE_UPDATE.values(), pid))
    print(f"  → people UPDATE ({cur.rowcount})")
    cur.execute("SELECT id,name_en FROM occupations")
    occ = {n: i for i, n in cur.fetchall()}
    n = 0
    for o, r in PERSON_OCCUPATIONS:
        if o in occ:
            cur.execute("INSERT IGNORE INTO person_occupation(person_id,occupation_id,`rank`) VALUES (%s,%s,%s)", (pid, occ[o], r))
            n += cur.rowcount
    print(f"  → person_occupation +{n}")
    cur.execute("SELECT id,name_en FROM fields")
    fid = {n: i for i, n in cur.fetchall()}
    n = 0
    for f in PERSON_FIELDS:
        if f not in fid:
            cur.execute("INSERT INTO fields(name_en) VALUES (%s)", (f,))
            fid[f] = cur.lastrowid
        cur.execute("INSERT IGNORE INTO person_field(person_id,field_id,`rank`) VALUES (%s,%s,0)", (pid, fid[f]))
        n += cur.rowcount
    print(f"  → person_field +{n}")
    cur.execute("SELECT id,name_en FROM institutions")
    inst = {n: i for i, n in cur.fetchall()}
    n = 0
    for en, zh, rel, sy, ey in PERSON_INSTITUTIONS:
        if en not in inst:
            cur.execute("INSERT INTO institutions(name_en,name_zh) VALUES (%s,%s)", (en, zh))
            inst[en] = cur.lastrowid
        cur.execute("INSERT IGNORE INTO person_institution(person_id,inst_id,relation,start_year,end_year) VALUES (%s,%s,%s,%s,%s)", (pid, inst[en], rel, sy, ey))
        n += cur.rowcount
    print(f"  → person_institution +{n}")
    cur.execute("SELECT id,name_en FROM countries")
    ctry = {n: i for i, n in cur.fetchall()}
    n = 0
    for c in NATIONALITIES:
        if c in ctry:
            cur.execute("INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)", (pid, ctry[c]))
            n += cur.rowcount
    print(f"  → person_nationality +{n}")
    cur.execute("SELECT list_key,`rank`,status FROM rankings WHERE person_id=%s", (pid,))
    print(f"  rankings: {cur.fetchall() or '⚠ 无'}")
    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
