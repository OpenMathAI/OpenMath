#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 Stefan Banach 数据库全字段（提示词 Stefan_Banach_zh.md 第 0.5 步，规范 §21.5）。

⚠️ Banach 的 people 主表字段缺失（gender/birth_date/death_date/name_zh/name_variants/description），本脚本一并补全：
1) people 主表 UPDATE
2) occupations + person_occupation 2 项
3) awards：补字典 Member of the Polish Academy of Learning + award_laureate 1 项
   ★ White Eagle（2018 追授，晚于数学家）按 §21.5 原则不入库
4) institutions + person_institution（education 3 + employment 2）
5) 检查 rankings

幂等：INSERT IGNORE + 唯一键。
"""
import json

from db_mysql import get_conn

BANACH = "Stefan Banach"

PEOPLE_UPDATE = {
    "name_zh": "斯特凡·巴拿赫",
    "name_variants": json.dumps(["泛函分析之父", "苏格兰咖啡馆的灵魂"], ensure_ascii=False),
    "gender": "male",
    "birth_date": "1892-03-30",
    "death_date": "1945-08-31",
    "description": "Polish mathematician (1892–1945)",
}

PERSON_OCCUPATIONS = [
    ("mathematician", 0),
    ("university teacher", 1),
]

NEW_AWARDS = [
    ("Member of the Polish Academy of Learning", "波兰学习院院士", "honor", None, "Polish Academy of Learning", 1872),
]

PERSON_AWARDS = [
    ("Member of the Polish Academy of Learning", 1924, None),
]

PERSON_INSTITUTIONS = [
    # education
    ("Lviv Polytechnic",        "利沃夫理工大学",   "education", None, None),
    ("Jagiellonian University", "雅盖隆大学",       "education", None, None),
    ("Lviv University",         "利沃夫大学",       "education", None, None),
    # employment
    ("Lviv Polytechnic",        "利沃夫理工大学",   "employment", 1920, 1922),
    ("Lviv University",         "利沃夫大学",       "employment", 1922, 1941),
]


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (BANACH,))
    row = cur.fetchone()
    if not row:
        print("⚠ Banach 不在库中")
        return
    pid = row[0]
    print(f"目标: {BANACH} (id={pid})")

    # ---- 0) people 主表补全 ----
    sets = ", ".join([f"{k}=%s" for k in PEOPLE_UPDATE])
    cur.execute(f"UPDATE people SET {sets} WHERE id=%s", (*PEOPLE_UPDATE.values(), pid))
    print(f"  → people 主表 UPDATE: {cur.rowcount} 行（name_zh/gender/生卒/称号/描述）")

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
            print(f"    → {BANACH}: {award} {year}")
    print(f"  → award_laureate +{n_award}（White Eagle 2018 追授未收）")

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
        print("  ⚠ rankings: Banach 无榜单记录（待补，如 OpenMath_20th_Century_Top50）")

    conn.commit()
    conn.close()
    print("完成")


if __name__ == "__main__":
    main()
