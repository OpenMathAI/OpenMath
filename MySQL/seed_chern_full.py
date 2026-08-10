#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 陈省身 (Shiing-Shen Chern) 数据库字段（第 0.5 步，§21.5）。奖项由 seed_all_awards 全量补。幂等。"""
import json
from db_mysql import get_conn

NAME = "陈省身"
PEOPLE_UPDATE = {
    "name_variants": json.dumps(["整体微分几何之父", "Chern 类之父", "数学大师", "Shiing-Shen Chern"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1911-10-26",
    "death_date": "2004-12-03",
    "description": "Chinese-American mathematician (1911–2004)",
}
PERSON_OCCUPATIONS = [("mathematician", 0), ("university teacher", 1), ("poet", 2)]
PERSON_FIELDS = ["differential geometry", "topology", "mathematics"]
PERSON_INSTITUTIONS = [
    ("Nankai University", "南开大学", "education", None, None),
    ("Tsinghua University", "清华大学", "education", None, None),
    ("University of Hamburg", "汉堡大学", "education", None, None),
    ("University of Paris", "巴黎大学", "education", None, None),
    ("National Southwestern Associated University", "国立西南联合大学", "employment", 1938, 1943),
    ("Peking University", "北京大学", "employment", 1945, 1948),
    ("University of Chicago", "芝加哥大学", "employment", 1949, 1960),
    ("University of California, Berkeley", "加州大学伯克利分校", "employment", 1960, 1979),
    ("Mathematical Sciences Research Institute", "数学科学研究所 (MSRI)", "employment", 1982, 1984),
    ("Nankai University", "南开大学", "employment", 1985, 2004),
]
NATIONALITIES = ["China", "United States"]


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
