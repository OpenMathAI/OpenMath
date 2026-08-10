#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Henri Lebesgue 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "Henri Lebesgue"
PEOPLE_UPDATE = {
    "name_zh": "亨利·勒贝格",
    "name_variants": json.dumps(["积分的革命者", "现代实分析的奠基人", "巴黎的安静巨人"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1875-06-28",
    "death_date": "1941-07-26",
    "description": "French mathematician (1875–1941)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("university teacher", 1)]
PERSON_INSTITUTIONS = [
    ("École Normale Supérieure", "巴黎高等师范学院", "education", None, None),
    ("Lycée Louis-le-Grand", "路易大帝中学", "education", None, None),
    ("University of Rennes", "雷恩大学", "employment", 1902, 1906),
    ("University of Poitiers", "普瓦捷大学", "employment", 1906, 1910),
    ("University of Paris", "巴黎大学", "employment", 1910, 1919),
    ("Collège de France", "法兰西公学院", "employment", 1921, 1941),
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
