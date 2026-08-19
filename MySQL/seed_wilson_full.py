#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""肯尼斯·威尔逊 (Kenneth G. Wilson) 人物主记录 + 研究领域入库（对应提示词第 4 步）。

- 新建/更新 people 主记录：name_en='Kenneth G. Wilson'、name_zh='肯尼斯·威尔逊'、
  primary_occupation='physicist'、has_biography=1、has_social_data=1，
  补齐 qid/gender/birth_date/death_date/description
- 职业：physicist
- 国籍：United States（美国）
- 研究领域：5 大领域写入 fields + person_field（带 rank，重整化群最高）

数据来源：本地 Wikipedia (Kenneth_G_Wilson.html) infobox + 正文。
"""
from db_mysql import get_conn

NAME = "Kenneth G. Wilson"
QID = "Q193503"

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("renormalization group", "重整化群", 0),
    ("critical phenomena", "临界现象 / 相变", 1),
    ("lattice gauge theory", "格点规范场论", 2),
    ("quantum field theory", "量子场论", 3),
    ("statistical mechanics", "统计力学", 4),
]


def get_or_create_field(cur, name_en, name_zh):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        # 顺带补齐缺失的中文名
        cur.execute(
            "UPDATE fields SET name_zh=%s WHERE id=%s AND (name_zh IS NULL OR name_zh='')",
            (name_zh, r[0]),
        )
        return r[0]
    cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh))
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
            (QID, "肯尼斯·威尔逊", "male", "1936-06-08", "2013-06-15",
             "American theoretical physicist (1936–2013)", "physicist", pid),
        )
        print(f"✓ 人物主记录已更新: {NAME} (id={pid})")
    else:
        cur.execute(
            "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1,1)",
            (QID, NAME, "肯尼斯·威尔逊", "male", "1936-06-08", "2013-06-15",
             "American theoretical physicist (1936–2013)", "physicist"),
        )
        pid = cur.lastrowid
        print(f"✓ 人物主记录已新建: {NAME} (id={pid})")

    # 2) 职业：physicist
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (pid, occ_phys),
    )
    print("✓ 职业已关联: physicist (rank=0)")

    # 3) 国籍：United States
    cur.execute("SELECT id FROM countries WHERE name_en='United States'")
    us = cur.fetchone()
    if us:
        cur.execute(
            "INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
            (pid, us[0]),
        )
        print("✓ 国籍已关联: United States (rank=0)")

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
    print("\n== Wilson 研究领域校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT c.name_en, pn.rank FROM person_nationality pn "
        "JOIN countries c ON c.id=pn.country_id WHERE pn.person_id=%s",
        (pid,),
    )
    print("\n== Wilson 国籍校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"\nperson_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
