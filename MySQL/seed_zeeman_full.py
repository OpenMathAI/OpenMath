#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""塞曼 (Pieter Zeeman) 人物主记录修正 + 研究领域入库（对应提示词第 4 步）。

- 修正 people 主表：库中已有占位记录 name_en='Pieter Zeeman' (id=1069)，
  补全 name_zh='彼得·塞曼'、qid='Q79000'、gender、birth_date、death_date、description，
  has_biography=1、has_social_data=1
- 同步 person_occupation：挂 physicist（rank 0，INSERT IGNORE 防重复）
- 确保 fields 字典中存在其 4 大领域（缺失则建）
- 写入 person_field（带 rank，Zeeman effect 最高）

数据来源：本地 Wikipedia (pages/20th_century/Pieter_Zeeman/metadata.json + page.md)。
"""
from db_mysql import get_conn

ZEEMAN_QID = "Q79000"

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("Zeeman effect", "塞曼效应", 0),
    ("magneto-optics", "磁光学", 1),
    ("spectroscopy", "光谱学", 2),
    ("atomic physics", "原子物理", 3),
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

    # 1) 定位 Zeeman 记录（优先 qid，其次 name_en）
    cur.execute("SELECT id FROM people WHERE qid=%s", (ZEEMAN_QID,))
    r = cur.fetchone()
    if r:
        zeeman_id = r[0]
        print(f"✓ 塞曼已按 qid 定位 (id={zeeman_id})")
    else:
        cur.execute("SELECT id FROM people WHERE name_en='Pieter Zeeman'")
        r = cur.fetchone()
        if not r:
            print("⚠ 库中无 Zeeman 占位记录，需先确认")
            return
        zeeman_id = r[0]
        print(f"✓ 已定位占位记录 (id={zeeman_id})")

    # 2) 更新主记录
    cur.execute(
        "UPDATE people SET qid=%s, name_en=%s, name_zh=%s, gender=%s, birth_date=%s, "
        "death_date=%s, description=%s, has_biography=1, has_social_data=1 WHERE id=%s",
        (
            ZEEMAN_QID, "Pieter Zeeman", "彼得·塞曼", "male",
            "1865-05-25", "1943-10-09", "Dutch physicist (1865–1943)", zeeman_id,
        ),
    )
    print(f"✓ 主记录已更新：Pieter Zeeman / 彼得·塞曼 / physicist")

    # 3) 同步 person_occupation：挂 physicist（rank 0）
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (zeeman_id, occ_phys),
    )
    print("✓ 已关联职业：physicist (rank=0)")

    # 4) 写入研究领域
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (zeeman_id, fid, rank),
        )
        if cur.rowcount:
            print(f"  + person_field: {name_en} (rank={rank})")

    conn.commit()

    # 5) 校验
    cur.execute(
        "SELECT f.name_en, pf.rank FROM person_field pf "
        "JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=%s ORDER BY pf.rank",
        (zeeman_id,),
    )
    print(f"\n== 塞曼 (id={zeeman_id}) 研究领域校验 ==")
    for row in cur.fetchall():
        print("  ", row)
    conn.close()


if __name__ == "__main__":
    main()
