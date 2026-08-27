#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""肯·汤普森 (Ken Thompson) 人物主记录 + 研究领域入库（对应提示词第 4 步）。

- 新建/更新 people 主记录：name_en='Ken Thompson'、name_zh='肯·汤普森'、
  primary_occupation='computer scientist'、has_biography=1、has_social_data=1，
  补齐 qid/gender/birth_date/description
- 职业：computer scientist（主，rank 0）
- 国籍：United States（美国）
- 研究领域：4 大领域写入 fields + person_field（带 rank，操作系统最高）

数据来源：本地 Wikipedia (turing/pages/1983/Ken Thompson/index.html) infobox + 正文。
"""
from db_mysql import get_conn

NAME = "Ken Thompson"
QID = "Q172552"

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("operating systems", "操作系统", 0),
    ("programming languages", "编程语言", 1),
    ("systems software", "系统软件", 2),
    ("computer architecture and chess", "计算机体系与计算机棋", 3),
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
            (QID, "肯·汤普森", "male", "1943-02-04", None,
             "American pioneer of computer science; co-creator of Unix, B, UTF-8, Go (1943–)",
             "computer scientist", pid),
        )
        print(f"✓ 人物主记录已更新: {NAME} (id={pid})")
    else:
        cur.execute(
            "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1,1)",
            (QID, NAME, "肯·汤普森", "male", "1943-02-04", None,
             "American pioneer of computer science; co-creator of Unix, B, UTF-8, Go (1943–)",
             "computer scientist"),
        )
        pid = cur.lastrowid
        print(f"✓ 人物主记录已新建: {NAME} (id={pid})")

    # 2) 职业：computer scientist（主，rank 0）
    occ_cs = get_or_create_occupation(cur, "computer scientist", "计算机科学家")
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (pid, occ_cs),
    )
    print("✓ 职业已关联: computer scientist (rank=0)")

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
    print("\n== Thompson 研究领域校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT c.name_en, pn.rank FROM person_nationality pn "
        "JOIN countries c ON c.id=pn.country_id WHERE pn.person_id=%s",
        (pid,),
    )
    print("\n== Thompson 国籍校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute(
        "SELECT o.name_en, po.rank FROM person_occupation po "
        "JOIN occupations o ON o.id=po.occupation_id WHERE po.person_id=%s ORDER BY po.rank",
        (pid,),
    )
    print("\n== Thompson 职业校验 ==")
    for r in cur.fetchall():
        print("  ", r)

    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"\nperson_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
