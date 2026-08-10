#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Kurt Gödel 数据库全字段（提示词 Kurt_Godel_zh.md 第 0.5 步，规范 §21.5）。

补全内容：
1) occupations + person_occupation 4 项（rank 排序）
2) awards：补字典 Albert Einstein Award + award_laureate 4 项
3) institutions + person_institution（education 1 + employment 3）
4) 检查 rankings 是否有 Gödel

幂等：INSERT IGNORE + 唯一键。
"""
from db_mysql import get_conn

GODEL = "Kurt Gödel"

PERSON_OCCUPATIONS = [
    ("mathematician", 0),
    ("university teacher", 1),
    ("computer scientist", 2),
    ("physicist", 3),
]

NEW_AWARDS = [
    ("Albert Einstein Award", "阿尔伯特·爱因斯坦奖", "honor", None, "Lewis and Rosa Strauss Memorial Fund", 1951),
]

PERSON_AWARDS = [
    ("Albert Einstein Award", 1951, "首届（与 Julian Schwinger 共同获得）"),
    ("Josiah Willard Gibbs Lectureship", 1951, "耶鲁大学，'Some Basic Theorems on the Foundations of Mathematics...'"),
    ("Foreign Member of the Royal Society", 1968, None),
    ("National Medal of Science", 1974, "福特总统颁发，因健康原因未出席"),
]

PERSON_INSTITUTIONS = [
    ("University of Vienna",           "维也纳大学",   "education", 1924, 1930),
    ("University of Vienna",           "维也纳大学",   "employment", 1930, 1938),
    ("University of Notre Dame",       "圣母大学",     "employment", 1938, 1939),
    ("Institute for Advanced Study",   "普林斯顿高等研究院", "employment", 1940, 1976),
]


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (GODEL,))
    row = cur.fetchone()
    if not row:
        print("⚠ Gödel 不在库中")
        return
    pid = row[0]
    print(f"目标: {GODEL} (id={pid})")

    # ---- 1) occupations ----
    cur.execute("SELECT id, name_en FROM occupations")
    occ_ids = {n: i for i, n in cur.fetchall()}
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
            print(f"    → {GODEL}: {award} {year}")
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
        print("  ⚠ rankings: Gödel 无榜单记录（待补，如 OpenMath_20th_Century_Top50）")

    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
