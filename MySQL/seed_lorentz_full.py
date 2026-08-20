#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""洛伦兹 (Hendrik Antoon Lorentz) 人物主记录修正 + 研究领域入库（对应提示词第 4 步）。

- 修正 people 主表：库中已有占位记录 name_en='Hendrik Lorentz' (id=348)，
  补全 name_en='Hendrik Antoon Lorentz'、name_zh='亨德里克·安东·洛伦兹'、qid='Q41688'、
  primary_occupation 由误标的 'mathematician' 改为 'physicist'，has_biography=1、has_social_data=1
- 同步 person_occupation：删掉误标的 mathematician，挂 physicist（rank 0）
- 确保 fields 字典中存在其 5 大领域（缺失则建）
- 写入 person_field（带 rank，electron theory 最高）

数据来源：本地 Wikipedia (pages/20th_century/Hendrik_Antoon_Lorentz/metadata.json + page.md)。
"""
from db_mysql import get_conn

LORENTZ_QID = "Q41688"

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("electron theory", "电子论", 0),
    ("electrodynamics", "电动力学", 1),
    ("relativity theory", "相对论", 2),
    ("magneto-optics", "磁光学", 3),
    ("hydrodynamics", "流体力学", 4),
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

    # 1) 定位 Lorentz 记录（优先 qid，其次 name_en）
    cur.execute("SELECT id FROM people WHERE qid=%s", (LORENTZ_QID,))
    r = cur.fetchone()
    if r:
        lorentz_id = r[0]
        print(f"✓ 洛伦兹已按 qid 定位 (id={lorentz_id})")
    else:
        cur.execute("SELECT id FROM people WHERE name_en='Hendrik Lorentz'")
        r = cur.fetchone()
        if not r:
            print("⚠ 库中无 Lorentz 占位记录，需先确认")
            return
        lorentz_id = r[0]
        print(f"✓ 已定位占位记录 (id={lorentz_id})")

    # 2) 更新主记录
    cur.execute(
        "UPDATE people SET qid=%s, name_en=%s, name_zh=%s, gender=%s, birth_date=%s, "
        "death_date=%s, description=%s, primary_occupation='physicist', "
        "has_biography=1, has_social_data=1 WHERE id=%s",
        (
            LORENTZ_QID, "Hendrik Antoon Lorentz", "亨德里克·安东·洛伦兹", "male",
            "1853-07-18", "1928-02-04", "Dutch physicist (1853–1928)", lorentz_id,
        ),
    )
    print(f"✓ 主记录已更新：Hendrik Antoon Lorentz / 亨德里克·安东·洛伦兹 / physicist")

    # 3) 同步 person_occupation：删掉误标的 mathematician，挂 physicist（rank 0）
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_math = cur.fetchone()[0]
    cur.execute("DELETE FROM person_occupation WHERE person_id=%s AND occupation_id=%s",
                (lorentz_id, occ_math))
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (lorentz_id, occ_phys),
    )
    print("✓ 已关联职业：physicist (rank=0)")

    # 4) 写入研究领域
    added = 0
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (lorentz_id, fid, rank),
        )
        if cur.rowcount:
            added += 1
            print(f"  + person_field: {name_en} (rank={rank})")

    conn.commit()

    # 5) 校验
    cur.execute(
        "SELECT f.name_en, pf.rank FROM person_field pf "
        "JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=%s ORDER BY pf.rank",
        (lorentz_id,),
    )
    print(f"\n== 洛伦兹 (id={lorentz_id}) 研究领域校验 ==")
    for row in cur.fetchall():
        print("  ", row)
    cur.execute("SELECT COUNT(*) FROM fields")
    print(f"\nfields 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"person_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
