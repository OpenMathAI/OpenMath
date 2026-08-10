#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Jean-Pierre Serre 数据库字段（第 0.5 步，§21.5）。奖项统一由 seed_all_awards.py 全量补。
幂等：INSERT IGNORE。"""
import json
from db_mysql import get_conn

NAME = "J.-P. Serre"
PEOPLE_UPDATE = {
    "name_zh": "让-皮埃尔·塞尔",
    "name_variants": json.dumps(["风格之神", "跨领域大师", "最年轻的菲尔兹奖得主", "Jean-Pierre Serre"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1926-09-15",
    "description": "French mathematician",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("university teacher", 1)]
PERSON_INSTITUTIONS = [
    ("University of Paris", "巴黎大学", "education", None, None),
    ("École Normale Supérieure", "巴黎高等师范学院", "education", None, None),
    ("National Center for Scientific Research", "法国国家科学研究中心", "employment", 1948, 1954),
    ("Collège de France", "法兰西公学院", "employment", 1956, 1994),
    ("Nancy-Université", "南锡大学", "employment", 1952, 1956),
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
    n = 0
    for o, r in PERSON_OCCUPATIONS:
        if o in occ:
            cur.execute("INSERT IGNORE INTO person_occupation(person_id,occupation_id,`rank`) VALUES (%s,%s,%s)", (pid, occ[o], r))
            n += cur.rowcount
    print(f"  → person_occupation +{n}")
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
    rk = cur.fetchall()
    print(f"  rankings: {rk if rk else '⚠ 无记录'}")
    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
