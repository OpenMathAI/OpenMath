#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""伦琴 (Wilhelm Conrad Röntgen) 人物主记录新建 + 研究领域入库（对应提示词第 4 步）。

- 新建 people 主表：name_en='Wilhelm Conrad Röntgen'、name_zh='威廉·康拉德·伦琴'、
  qid='Q35149'、primary_occupation='physicist'、has_biography=1
- 关联 occupations(physicist, rank 0)
- 确保 fields 字典中存在其 5 大领域（缺失则建）
- 写入 person_field（带 rank，X 射线物理最高）

数据来源：本地 Wikipedia (pages/20th_century/Wilhelm_Conrad_Röntgen/metadata.json + page.md)。
"""
from db_mysql import get_conn

# 伦琴基本信息（来自本地 Wikipedia metadata.json）
RONTGEN = dict(
    name_en="Wilhelm Conrad Röntgen",
    name_zh="威廉·康拉德·伦琴",
    qid="Q35149",
    gender="male",
    birth_date="1845-03-27",
    death_date="1923-02-10",
    description="German physicist (1845–1923)",
)

# (name_en, name_zh, rank) —— rank 0 为主领域
FIELDS = [
    ("X-ray physics", "X 射线物理", 0),
    ("experimental physics", "实验物理学", 1),
    ("electromagnetic radiation", "电磁辐射", 2),
    ("cathode rays", "阴极射线", 3),
    ("medical imaging", "医学成像", 4),
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

    # 1) 检查是否已存在（幂等）
    cur.execute("SELECT id FROM people WHERE qid=%s", (RONTGEN["qid"],))
    r = cur.fetchone()
    if r:
        rontgen_id = r[0]
        print(f"✓ 伦琴已存在 (id={rontgen_id})，跳过新建")
    else:
        cur.execute(
            "INSERT INTO people(name_en, name_zh, qid, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1,1)",
            (
                RONTGEN["name_en"], RONTGEN["name_zh"], RONTGEN["qid"], RONTGEN["gender"],
                RONTGEN["birth_date"], RONTGEN["death_date"], RONTGEN["description"],
                "physicist",
            ),
        )
        rontgen_id = cur.lastrowid
        print(f"✓ 已新建伦琴 (id={rontgen_id})")

    # 2) 关联职业 physicist（rank 0）
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (rontgen_id, occ_phys),
    )
    print("✓ 已关联职业：physicist (rank=0)")

    # 3) 写入研究领域
    added = 0
    for name_en, name_zh, rank in FIELDS:
        fid = get_or_create_field(cur, name_en, name_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (rontgen_id, fid, rank),
        )
        if cur.rowcount:
            added += 1
            print(f"  + person_field: {name_en} (rank={rank})")

    conn.commit()

    # 4) 校验
    cur.execute(
        "SELECT f.name_en, pf.rank FROM person_field pf "
        "JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=%s ORDER BY pf.rank",
        (rontgen_id,),
    )
    print(f"\n== 伦琴 (id={rontgen_id}) 研究领域校验 ==")
    for row in cur.fetchall():
        print("  ", row)
    cur.execute("SELECT COUNT(*) FROM fields")
    print(f"\nfields 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"person_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
