#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""弗雷德里克·桑格 (Frederick Sanger) 人物主记录 + 研究领域入库（对应提示词第 4 步）。

- 新建/更新 people 主记录：name_en='Frederick Sanger'、name_zh='弗雷德里克·桑格'、
  primary_occupation='biochemist'、has_biography=1、has_social_data=1，
  补齐 qid/gender/birth_date/death_date/description
- 职业：biochemist（主，rank 0）+ chemist（次，rank 1）
- 国籍：United Kingdom（英国）
- 研究领域：4 大领域写入 fields + person_field（带 rank，蛋白质测序最高）

数据来源：本地 Wikipedia (pages/Frederick_Sanger/page.md) infobox + 正文。
"""
from db_mysql import get_conn

NAME = "Frederick Sanger"
QID = "Q151564"

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("protein sequencing", "蛋白质测序", 0),
    ("DNA sequencing", "DNA 测序", 1),
    ("RNA sequencing", "RNA 测序", 2),
    ("molecular biology", "分子生物学", 3),
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
            "UPDATE people SET qid=%s, name_zh=%s, gender=%s, birth_date=%s, death_date=%s, "
            "description=%s, primary_occupation=%s, has_biography=1, has_social_data=1 "
            "WHERE id=%s",
            (QID, "弗雷德里克·桑格", "male", "1918-08-13", "2013-11-19",
             "British biochemist (1918–2013)", "biochemist", pid),
        )
        print(f"✓ 人物主记录已更新: {NAME} (id={pid})")
    else:
        cur.execute(
            "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1,1)",
            (QID, NAME, "弗雷德里克·桑格", "male", "1918-08-13", "2013-11-19",
             "British biochemist (1918–2013)", "biochemist"),
        )
        pid = cur.lastrowid
        print(f"✓ 人物主记录已新建: {NAME} (id={pid})")

    # 2) 职业：biochemist（主，rank 0）+ chemist（次，rank 1）
    occ_bio = get_or_create_occupation(cur, "biochemist", "生物化学家")
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (pid, occ_bio),
    )
    print("✓ 职业已关联: biochemist (rank=0)")

    occ_chem = get_or_create_occupation(cur, "chemist", "化学家")
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
        (pid, occ_chem),
    )
    print("✓ 职业已关联: chemist (rank=1)")

    # 3) 国籍：United Kingdom
    cur.execute("SELECT id FROM countries WHERE name_en='United Kingdom'")
    uk = cur.fetchone()
    if uk:
        cur.execute(
            "INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
            (pid, uk[0]),
        )
        print("✓ 国籍已关联: United Kingdom (rank=0)")

    # 4) 研究领域
    added = 0
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
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
    print("\n== Sanger 研究领域校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT c.name_en, pn.rank FROM person_nationality pn "
        "JOIN countries c ON c.id=pn.country_id WHERE pn.person_id=%s",
        (pid,),
    )
    print("\n== Sanger 国籍校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT o.name_en, po.rank FROM person_occupation po "
        "JOIN occupations o ON o.id=po.occupation_id WHERE po.person_id=%s ORDER BY po.rank",
        (pid,),
    )
    print("\n== Sanger 职业校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"\nperson_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
