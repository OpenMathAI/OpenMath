#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""姚期智 (Andrew Chi-Chih Yao) 人物主记录 + 研究领域入库（对应提示词第 4 步）。

- 新建/更新 people 主记录：name_en='Andrew Yao'、name_zh='姚期智'、
  primary_occupation='computer scientist'、has_biography=1、has_social_data=1，
  补齐 gender/birth_date/description（qid 本地无权威来源，暂不写入）
- 职业：computer scientist（主，rank 0）+ theoretical physicist（次，rank 1）
- 国籍：People's Republic of China（当前，rank 0）、United States（rank 1）、
  Republic of China（历史，rank 2）
- 研究领域：4 大领域写入 fields + person_field（带 rank，计算理论最高）

数据来源：本地 Wikipedia (turing/pages/2000/Andrew Yao/index.html) infobox + 正文。
"""
from db_mysql import get_conn

NAME = "Andrew Yao"

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("theory of computation", "计算理论", 0),
    ("cryptography", "密码学", 1),
    ("communication complexity", "通信复杂性", 2),
    ("pseudorandomness", "伪随机性", 3),
]

# 国籍：(name_en, rank, era_note)
NATIONALITIES = [
    ("People's Republic of China", 0, "2015–present"),
    ("United States", 1, "?–2015（2015 放弃美国国籍）"),
    ("Republic of China", 2, "1946–2015"),
]


def get_or_create_field(cur, name_en, name_zh):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        cur.execute(
            "UPDATE fields SET name_zh=%s WHERE id=%s AND (name_zh IS NULL OR name_zh='')",
            (name_zh, r[0]),
        )
        return r[0]
    cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh))
    return cur.lastrowid


def get_or_create_occupation(cur, name_en, name_zh):
    cur.execute("SELECT id FROM occupations WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        cur.execute(
            "UPDATE occupations SET name_zh=%s WHERE id=%s AND (name_zh IS NULL OR name_zh='')",
            (name_zh, r[0]),
        )
        return r[0]
    cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh))
    return cur.lastrowid


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 1) 新建/更新人物主记录
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if row:
        pid = row[0]
        cur.execute(
            "UPDATE people SET name_zh=%s, name_variants=%s, gender=%s, birth_date=%s, death_date=%s, "
            "description=%s, primary_occupation=%s, has_biography=1, has_social_data=1 "
            "WHERE id=%s",
            ("姚期智", "Andrew Chi-Chih Yao; Yao Qizhi", "male", "1946-12-24", None,
             "Chinese computer scientist, theoretical physicist and computational theorist (1946–)",
             "computer scientist", pid),
        )
        print(f"✓ 人物主记录已更新: {NAME} (id={pid})")
    else:
        cur.execute(
            "INSERT INTO people(name_en, name_zh, name_variants, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1,1)",
            (NAME, "姚期智", "Andrew Chi-Chih Yao; Yao Qizhi", "male", "1946-12-24", None,
             "Chinese computer scientist, theoretical physicist and computational theorist (1946–)",
             "computer scientist"),
        )
        pid = cur.lastrowid
        print(f"✓ 人物主记录已新建: {NAME} (id={pid})")

    # 2) 职业：computer scientist（主，rank 0）+ theoretical physicist（次，rank 1）
    occ_cs = get_or_create_occupation(cur, "computer scientist", "计算机科学家")
    cur.execute(
        "INSERT INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0) "
        "ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`)",
        (pid, occ_cs),
    )
    print("✓ 职业已关联: computer scientist (rank=0)")

    occ_phys = get_or_create_occupation(cur, "theoretical physicist", "理论物理学家")
    cur.execute(
        "INSERT INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1) "
        "ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`)",
        (pid, occ_phys),
    )
    print("✓ 职业已关联: theoretical physicist (rank=1)")

    # 3) 国籍：中华人民共和国（当前） / 美国 / 中华民国（历史）
    for cname, rank, era_note in NATIONALITIES:
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (cname,))
        crow = cur.fetchone()
        if not crow:
            print(f"⚠ countries 字典中未找到 {cname}，跳过国籍关联")
            continue
        cur.execute(
            "INSERT INTO person_nationality(person_id, country_id, `rank`, era_note) "
            "VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`), era_note=VALUES(era_note)",
            (pid, crow[0], rank, era_note),
        )
        print(f"✓ 国籍已关联: {cname} (rank={rank})")

    # 4) 研究领域
    added = 0
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`)",
            (pid, fid, rank),
        )
        if cur.rowcount:
            added += 1
            print(f"  + person_field: {name_en} (rank={rank})")

    conn.commit()

    # 5) 校验
    cur.execute(
        "SELECT f.name_en, f.name_zh, pf.rank FROM person_field pf "
        "JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=%s ORDER BY pf.rank",
        (pid,),
    )
    print("\n== Yao 研究领域校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT c.name_en, pn.rank, pn.era_note FROM person_nationality pn "
        "JOIN countries c ON c.id=pn.country_id WHERE pn.person_id=%s ORDER BY pn.rank",
        (pid,),
    )
    print("\n== Yao 国籍校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT o.name_en, po.rank FROM person_occupation po "
        "JOIN occupations o ON o.id=po.occupation_id WHERE po.person_id=%s ORDER BY po.rank",
        (pid,),
    )
    print("\n== Yao 职业校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"\nperson_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
