#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 John Milnor 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "John Milnor"
PEOPLE_UPDATE = {
    "name_zh": "约翰·米尔诺",
    "name_variants": json.dumps(["怪球的发现者", "微分拓扑之王", "普林斯顿神童"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1931-02-20",
    "description": "American mathematician (1931–)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("topologist", 1), ("university teacher", 2)]
PERSON_FIELDS = ["differential topology", "K-theory", "dynamical systems", "topology", "mathematics"]
PERSON_INSTITUTIONS = [
    ("Princeton University", "普林斯顿大学", "education", None, None),
    ("Princeton University", "普林斯顿大学", "employment", 1956, 1970),
    ("Institute for Advanced Study", "普林斯顿高等研究院", "employment", 1962, 1968),
    ("Stony Brook University", "纽约州立大学石溪分校", "employment", 1970, 2012),
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
    if "Stony Brook University" not in inst:
        cur.execute("INSERT INTO institutions(name_en,name_zh) VALUES (%s,%s)", ("Stony Brook University", "纽约州立大学石溪分校"))
        inst["Stony Brook University"] = cur.lastrowid
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
