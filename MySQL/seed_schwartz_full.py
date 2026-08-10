#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Laurent Schwartz 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "Laurent Schwartz"
PEOPLE_UPDATE = {
    "name_zh": "洛朗·施瓦茨",
    "name_variants": json.dumps(["分布论之父", "菲尔兹奖捍卫者", "数学家中的昆虫学家"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1915-03-05",
    "death_date": "2002-07-04",
    "description": "French mathematician (1915–2002)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("university teacher", 1), ("entomologist", 2)]
PERSON_FIELDS = ["distribution theory", "mathematics"]
PERSON_INSTITUTIONS = [
    ("École Normale Supérieure", "巴黎高等师范学院", "education", None, None),
    ("Lycée Janson-de-Sailly", "让松德萨伊中学", "education", None, None),
    ("Nancy-Université", "南锡大学", "employment", 1940, 1944),
    ("University of Grenoble", "格勒诺布尔大学", "employment", 1944, 1952),
    ("École Polytechnique", "巴黎综合理工学院", "employment", 1959, 1973),
    ("University of Paris", "巴黎大学", "employment", 1953, 1959),
]
NATIONALITIES = ["France"]


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
    if "entomologist" not in occ:
        cur.execute("INSERT INTO occupations(name_en,name_zh) VALUES (%s,'昆虫学家')", ("entomologist",))
        occ["entomologist"] = cur.lastrowid
        print("  + occupations: entomologist")
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
    if "France" in ctry:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id,country_id,`rank`) VALUES (%s,%s,0)", (pid, ctry["France"]))
        n += cur.rowcount
    print(f"  → person_nationality +{n}")
    cur.execute("SELECT list_key,`rank`,status FROM rankings WHERE person_id=%s", (pid,))
    print(f"  rankings: {cur.fetchall() or '⚠ 无'}")
    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
