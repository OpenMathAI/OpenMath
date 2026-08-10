#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Stephen Smale 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "Stephen Smale"
PEOPLE_UPDATE = {
    "name_zh": "斯蒂芬·斯梅尔",
    "name_variants": json.dumps(["高维庞加莱猜想的证明者", "混沌动力学的先驱", "斯梅尔猜想"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1930-07-15",
    "description": "American mathematician (1930–)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("computer scientist", 1), ("university teacher", 2)]
PERSON_FIELDS = ["topology", "differential geometry", "mathematics"]
PERSON_INSTITUTIONS = [
    ("University of Michigan", "密歇根大学", "education", None, None),
    ("University of Chicago", "芝加哥大学", "employment", 1956, 1960),
    ("Columbia University", "哥伦比亚大学", "employment", 1960, 1964),
    ("University of California, Berkeley", "加州大学伯克利分校", "employment", 1964, 1994),
    ("Institute for Advanced Study", "普林斯顿高等研究院", "employment", 1958, 1959),
    ("City University of Hong Kong", "香港城市大学", "employment", 1995, 2010),
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
