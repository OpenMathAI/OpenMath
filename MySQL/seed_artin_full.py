#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Emil Artin 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "Emil Artin"
PEOPLE_UPDATE = {
    "name_zh": "埃米尔·阿廷",
    "name_variants": json.dumps(["互反律之王", "抽象代数的建筑师", "Artin 互反律"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1898-03-03",
    "death_date": "1962-12-20",
    "description": "Austrian-Armenian mathematician (1898–1962)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("university teacher", 1)]
PERSON_INSTITUTIONS = [
    ("University of Vienna", "维也纳大学", "education", None, None),
    ("Leipzig University", "莱比锡大学", "education", None, None),
    ("University of Göttingen", "哥廷根大学", "education", None, None),
    ("University of Hamburg", "汉堡大学", "employment", 1923, 1937),
    ("University of Notre Dame", "圣母大学", "employment", 1937, 1938),
    ("Indiana University", "印第安纳大学", "employment", 1938, 1946),
    ("Princeton University", "普林斯顿大学", "employment", 1946, 1958),
    ("University of Hamburg", "汉堡大学", "employment", 1958, 1962),
]


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
    cur.execute("SELECT list_key,`rank`,status FROM rankings WHERE person_id=%s", (pid,))
    print(f"  rankings: {cur.fetchall() or '⚠ 无'}")
    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
