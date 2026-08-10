#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Alan Turing 数据库全字段（提示词 Alan_Turing_zh.md 第 0.5 步，规范 §21.5）。

补全内容：
1) occupations：补字典 cryptographer + person_occupation 6 项（rank 排序）
2) awards：补字典 Smith's Prize / OBE + award_laureate 3 项
3) institutions + person_institution（education 4 + employment 4）
4) 检查 rankings 是否有 Turing

幂等：INSERT IGNORE + 唯一键。
"""
from db_mysql import get_conn

TURING = "Alan Turing"

NEW_OCCUPATIONS = [
    ("cryptographer", "密码学家"),
]

PERSON_OCCUPATIONS = [
    ("mathematician", 0),
    ("computer scientist", 1),
    ("university teacher", 2),
    ("cryptographer", 3),
    ("logician", 4),
    ("statistician", 5),
]

NEW_AWARDS = [
    ("Smith's Prize",                        "史密斯奖",         "math_hist", 2, "University of Cambridge", 1768),
    ("Officer of the Order of the British Empire", "大英帝国官佐勋章 (OBE)", "honor", None, "United Kingdom", 1917),
]

PERSON_AWARDS = [
    ("Smith's Prize", 1936, None),
    ("Officer of the Order of the British Empire", 1946, "战时密码破译贡献"),
    ("Fellow of the Royal Society", 1951, None),
]

PERSON_INSTITUTIONS = [
    # education
    ("Sherborne School",               "舍伯恩学校",           "education", None, None),
    ("King's College",                 "剑桥大学国王学院",     "education", None, None),
    ("Princeton University",           "普林斯顿大学",         "education", None, None),
    ("Hazlehurst Community Primary School", "黑泽尔赫斯特小学", "education", None, None),
    # employment
    ("University of Cambridge",        "剑桥大学",             "employment", 1931, 1936),
    ("Government Communications Headquarters", "政府通信总部 (GCHQ/Bletchley Park)", "employment", 1939, 1945),
    ("National Physical Laboratory",   "国家物理实验室 (NPL)", "employment", 1945, 1947),
    ("Victoria University of Manchester", "曼彻斯特大学",       "employment", 1948, 1954),
]


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (TURING,))
    row = cur.fetchone()
    if not row:
        print("⚠ Turing 不在库中")
        return
    pid = row[0]
    print(f"目标: {TURING} (id={pid})")

    # ---- 1) occupations ----
    cur.execute("SELECT id, name_en FROM occupations")
    occ_ids = {n: i for i, n in cur.fetchall()}
    for en, zh in NEW_OCCUPATIONS:
        if en not in occ_ids:
            cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES (%s,%s)", (en, zh))
            occ_ids[en] = cur.lastrowid
            print(f"  + occupations: {en} ({zh})")
    n_occ = 0
    for occ, rank in PERSON_OCCUPATIONS:
        if occ not in occ_ids:
            print(f"  ⚠ occupations 缺失: {occ}")
            continue
        cur.execute(
            "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,%s)",
            (pid, occ_ids[occ], rank),
        )
        if cur.rowcount:
            n_occ += 1
    print(f"  → person_occupation +{n_occ}")

    # ---- 2) awards ----
    cur.execute("SELECT id, name_en FROM awards")
    award_ids = {n: i for i, n in cur.fetchall()}
    for en, zh, atype, tier, org, est in NEW_AWARDS:
        if en not in award_ids:
            cur.execute(
                "INSERT INTO awards(name_en, name_zh, award_type, tier, org, established) VALUES (%s,%s,%s,%s,%s,%s)",
                (en, zh, atype, tier, org, est),
            )
            award_ids[en] = cur.lastrowid
            print(f"  + awards: {en} ({zh})")
    n_award = 0
    for award, year, note in PERSON_AWARDS:
        if award not in award_ids:
            print(f"  ⚠ awards 缺失: {award}")
            continue
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, year, note, source) VALUES (%s,%s,%s,%s,'Wikipedia infobox')",
            (pid, award_ids[award], year, note),
        )
        if cur.rowcount:
            n_award += 1
            print(f"    → {TURING}: {award} {year}")
    print(f"  → award_laureate +{n_award}")

    # ---- 3) institutions ----
    cur.execute("SELECT id, name_en FROM institutions")
    inst_ids = {n: i for i, n in cur.fetchall()}
    n_inst = 0
    for en, zh, rel, sy, ey in PERSON_INSTITUTIONS:
        if en not in inst_ids:
            cur.execute("INSERT INTO institutions(name_en, name_zh) VALUES (%s,%s)", (en, zh))
            inst_ids[en] = cur.lastrowid
            print(f"  + institutions: {en} ({zh})")
        cur.execute(
            "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) VALUES (%s,%s,%s,%s,%s)",
            (pid, inst_ids[en], rel, sy, ey),
        )
        if cur.rowcount:
            n_inst += 1
    print(f"  → person_institution +{n_inst}")

    # ---- 4) rankings 检查 ----
    cur.execute("SELECT list_key, `rank`, status FROM rankings WHERE person_id=%s", (pid,))
    ranks = cur.fetchall()
    if ranks:
        for lk, rk, st in ranks:
            print(f"  rankings: {lk} #{rk} ({st})")
    else:
        print("  ⚠ rankings: Turing 无榜单记录（待补，如 OpenMath_20th_Century_Top50）")

    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
