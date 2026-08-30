#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""海森堡 (Werner Heisenberg) 人物主记录修正 + 研究领域入库（对应提示词第 4 步）。

- 修正 people 主表：补 qid='Q40904'、name_zh='海森堡'、
  primary_occupation 由误标的 'mathematician' 改为 'physicist'、has_biography=1
- 确保 fields 字典中存在其核心领域（缺失则建）
- 写入 person_field（带 rank，量子力学最高）

数据来源：本地 Wikipedia (Werner_Karl_Heisenberg/page.md + metadata.json)。
"""
from db_mysql import get_conn

HEISENBERG_ID = 704  # 库中已存在（name_en='Werner Heisenberg'，原 primary_occupation='mathematician'）

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("quantum mechanics", "量子力学", 0),
    ("theoretical physics", "理论物理", 1),
    ("nuclear physics", "核物理", 2),
    ("quantum field theory", "量子场论", 3),
]


def get_or_create_field(cur, name_en, name_zh):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh))
    return cur.lastrowid


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 1) 修正主记录
    cur.execute(
        "UPDATE people SET qid='Q40904', name_zh='海森堡', primary_occupation='physicist', "
        "has_biography=1 WHERE id=%s", (HEISENBERG_ID,)
    )
    # 同步 person_occupation：删掉误标的 mathematician，挂 physicist（rank 0）
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_math = cur.fetchone()[0]
    cur.execute("DELETE FROM person_occupation WHERE person_id=%s AND occupation_id=%s",
                (HEISENBERG_ID, occ_math))
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (HEISENBERG_ID, occ_phys),
    )
    print("✓ 主记录已修正：physicist / 海森堡 / Q40904 / has_biography=1")

    # 2) 写入研究领域
    added = 0
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (HEISENBERG_ID, fid, rank),
        )
        if cur.rowcount:
            added += 1
            print(f"  + person_field: {name_en} (rank={rank})")

    conn.commit()

    # 3) 校验
    cur.execute(
        "SELECT f.name_en, pf.rank FROM person_field pf "
        "JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=%s ORDER BY pf.rank",
        (HEISENBERG_ID,),
    )
    print("\n== Heisenberg 研究领域校验 ==")
    for r in cur.fetchall():
        print("  ", r)
    cur.execute("SELECT id, qid, name_en, name_zh, primary_occupation, has_biography "
                "FROM people WHERE id=%s", (HEISENBERG_ID,))
    print("\n== people 主记录 ==")
    print("  ", cur.fetchone())
    conn.close()


if __name__ == "__main__":
    main()
