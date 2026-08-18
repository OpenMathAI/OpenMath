#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""维格纳 (Eugene Wigner) 人物主记录修正 + 研究领域入库（对应提示词第 4 步）。

- 修正 people 主表：primary_occupation 由误标的 'mathematician' 改为 'physicist'，
  补全 name_zh='维格纳'、has_biography=1
- 确保 fields 字典中存在其 5 大领域（缺失则建）
- 写入 person_field（带 rank，对称性/群论最高）

数据来源：本地 Wikipedia (Eugene_Wigner.html) infobox + 正文。
"""
from db_mysql import get_conn

WIGNER_ID = 352  # 库中已存在（原 primary_occupation='mathematician'）

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("symmetry (group theory in physics)", "对称性 / 物理中的群论", 0),
    ("nuclear physics", "原子核物理", 1),
    ("quantum mechanics", "量子力学", 2),
    ("solid-state physics", "固体物理", 3),
    ("mathematical physics", "数学物理", 4),
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
        "UPDATE people SET primary_occupation='physicist', name_zh='维格纳', has_biography=1 "
        "WHERE id=%s", (WIGNER_ID,)
    )
    # 同步 person_occupation：删掉误标的 mathematician，挂 physicist（rank 0）
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_math = cur.fetchone()[0]
    cur.execute("DELETE FROM person_occupation WHERE person_id=%s AND occupation_id=%s",
                (WIGNER_ID, occ_math))
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (WIGNER_ID, occ_phys),
    )
    print("✓ 主记录已修正：physicist / 维格纳 / has_biography=1")

    # 2) 写入研究领域
    added = 0
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (WIGNER_ID, fid, rank),
        )
        if cur.rowcount:
            added += 1
            print(f"  + person_field: {name_en} (rank={rank})")

    conn.commit()

    # 3) 校验
    cur.execute(
        "SELECT f.name_en, pf.rank FROM person_field pf "
        "JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=%s ORDER BY pf.rank",
        (WIGNER_ID,),
    )
    print("\n== Wigner 研究领域校验 ==")
    for r in cur.fetchall():
        print("  ", r)
    cur.execute("SELECT COUNT(*) FROM fields")
    print(f"\nfields 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"person_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
