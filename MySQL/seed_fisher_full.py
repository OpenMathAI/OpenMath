#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 R.A. Fisher 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "R.A. Fisher"
PEOPLE_UPDATE = {
    "name_zh": "罗纳德·艾尔默·费希尔",
    "name_variants": json.dumps(["统计学的巨人", "现代统计学的奠基人", "R.A. Fisher", "遗传学与统计学之父"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1890-02-17",
    "death_date": "1962-07-29",
    "description": "British statistician and geneticist (1890–1962)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("statistician", 1), ("geneticist", 2), ("astronomer", 3), ("biostatistician", 4)]
PERSON_FIELDS = ["statistics", "genetics"]
PERSON_INSTITUTIONS = [
    ("University of Cambridge", "剑桥大学", "education", None, None),
    ("Harrow School", "哈罗公学", "education", None, None),
    ("Rothamsted Research", "罗森斯特农业试验站", "employment", 1919, 1933),
    ("University College London", "伦敦大学学院", "employment", 1933, 1943),
    ("University of Cambridge", "剑桥大学", "employment", 1943, 1957),
    ("University of Adelaide", "阿德莱德大学", "employment", 1959, 1962),
]
NATIONALITIES = ["United Kingdom"]


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
    if "biostatistician" not in occ:
        cur.execute("INSERT INTO occupations(name_en,name_zh) VALUES (%s,'生物统计学家')", ("biostatistician",))
        occ["biostatistician"] = cur.lastrowid
        print("  + occupations: biostatistician")
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
    if "United Kingdom" in ctry:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)", (pid, ctry["United Kingdom"]))
        n += cur.rowcount
    print(f"  → person_nationality +{n}")
    cur.execute("SELECT list_key,`rank`,status FROM rankings WHERE person_id=%s", (pid,))
    print(f"  rankings: {cur.fetchall() or '⚠ 无'}")
    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
