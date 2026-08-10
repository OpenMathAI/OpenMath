#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Claude Shannon 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "Claude Shannon"
PEOPLE_UPDATE = {
    "name_variants": json.dumps(["信息论之父", "比特的发明者", "熵的命名者"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1916-04-30",
    "death_date": "2001-02-24",
    "description": "American mathematician and information theorist (1916–2001)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("computer scientist", 1), ("cryptographer", 2), ("engineer", 3), ("inventor", 4), ("university teacher", 5), ("geneticist", 6)]
PERSON_FIELDS = ["information theory", "probability theory", "cryptography", "cybernetics", "electrical engineering"]
PERSON_INSTITUTIONS = [
    ("University of Michigan", "密歇根大学", "education", None, None),
    ("Massachusetts Institute of Technology", "麻省理工学院", "education", None, None),
    ("Bell Labs", "贝尔实验室", "employment", 1941, 1972),
    ("Massachusetts Institute of Technology", "麻省理工学院", "employment", 1956, 1978),
    ("Institute for Advanced Study", "普林斯顿高等研究院", "employment", 1940, 1941),
]
NATIONALITIES = ["United States"]


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
    for new_occ, zh in [("inventor", "发明家"), ("geneticist", "遗传学家")]:
        if new_occ not in occ:
            cur.execute("INSERT INTO occupations(name_en,name_zh) VALUES (%s,%s)", (new_occ, zh))
            occ[new_occ] = cur.lastrowid
            print(f"  + occupations: {new_occ} ({zh})")
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
    if "United States" in ctry:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)", (pid, ctry["United States"]))
        n += cur.rowcount
    print(f"  → person_nationality +{n}")
    cur.execute("SELECT list_key,`rank`,status FROM rankings WHERE person_id=%s", (pid,))
    print(f"  rankings: {cur.fetchall() or '⚠ 无'}")
    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
