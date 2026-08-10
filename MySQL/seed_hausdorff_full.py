#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Felix Hausdorff 数据库字段（第 0.5 步，§21.5）。幂等。"""
import json
from db_mysql import get_conn

NAME = "Felix Hausdorff"
PEOPLE_UPDATE = {
    "name_zh": "费利克斯·豪斯多夫",
    "name_variants": json.dumps(["拓扑空间之父", "豪斯多夫维数", "Hausdorff 空间"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1868-11-08",
    "death_date": "1942-01-26",
    "description": "German mathematician (1868–1942)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("topologist", 1), ("university teacher", 2), ("writer", 3), ("astronomer", 4)]
PERSON_FIELDS = ["topology", "set theory"]
PERSON_INSTITUTIONS = [
    ("Leipzig University", "莱比锡大学", "education", None, None),
    ("University of Greifswald", "格赖夫斯瓦尔德大学", "employment", 1913, 1921),
    ("University of Bonn", "波恩大学", "employment", 1921, 1935),
    ("Leipzig University", "莱比锡大学", "employment", 1902, 1910),
]
NATIONALITIES = ["German Reich"]


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
