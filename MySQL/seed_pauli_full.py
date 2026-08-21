#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wolfgang Pauli（沃尔夫冈·泡利）人物主记录 + 研究领域 + 社会关系入库。

数据源：本地 Wikipedia (physicist/presentations/pages/20th_century/Wolfgang_Pauli)
     + 提示词 Wolfgang_Pauli_zh.md（第 4 / 4.5 步）。

关系方向约定：
  advisor-student：ADVISORS 中的人 → 泡利（导师）；其余 → 学生（泡利 → 学生）
  colleague / spouse：无向
"""
import re
import unicodedata
from db_mysql import get_conn

NAME = "Wolfgang Pauli"
QID = "Q65989"

# (name_en, name_zh, rank)
FIELDS = [
    ("quantum mechanics", "量子力学", 0),
    ("spin theory", "自旋理论", 1),
    ("neutrino physics", "中微子物理", 2),
    ("quantum field theory", "量子场论", 3),
]

# 国籍：(name_en, rank)
NATIONALITIES = [
    ("Austria", 0),
    ("United States", 1),
    ("Switzerland", 2),
]

# 导师（有向：→ 泡利）
ADVISORS = {"Arnold Sommerfeld", "Max Born"}

# (relation_type, name_en, name_zh, note)
RELATIONS = [
    # 导师（→ 泡利）
    ("advisor-student", "Arnold Sommerfeld", "阿诺德·索末菲", "慕尼黑博士导师，原子模型先驱"),
    ("advisor-student", "Max Born", "马克斯·玻恩", "哥廷根任其助手一年"),
    # 门生（泡利 → 学生）
    ("advisor-student", "Charles Enz", "查尔斯·恩兹", "博士生，末任助手"),
    ("advisor-student", "Max Robert Schafroth", "马克斯·罗伯特·沙夫罗特", "博士生"),
    ("advisor-student", "Felix Villars", "费利克斯·维拉斯", "著名学生，Pauli–Villars 正则化合作者"),
    # 同事/合作者（无向）
    ("colleague", "Niels Bohr", "尼尔斯·玻尔", "哥本哈根一年，1921 Aufbau 原理合作"),
    ("colleague", "Werner Heisenberg", "维尔纳·海森堡", "挚友，晚年因统一场论决裂"),
    ("colleague", "Albert Einstein", "阿尔伯特·爱因斯坦", "称泡利为精神继承者，提名诺奖"),
    ("colleague", "Carl Jung", "卡尔·荣格", "心理治疗师兼合作者，共探共时性"),
]

# 配偶（无向，占位 primary_occupation=NULL）
SPOUSES = [
    ("Käthe Deppner", "凯特·德普纳", "配偶（1929，一年内离异）"),
    ("Franziska Bertram", "弗兰齐斯卡·伯特拉姆", "配偶（1934–1958）"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def get_or_create_field(cur, name_en, name_zh):
    cur.execute("SELECT id FROM fields WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        if name_zh:
            cur.execute(
                "UPDATE fields SET name_zh=%s WHERE id=%s AND (name_zh IS NULL OR name_zh='')",
                (name_zh, r[0]),
            )
        return r[0]
    cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh))
    return cur.lastrowid


_people_cache = None


def upsert_person(cur, name_en, name_zh, occupation, has_bio=0):
    global _people_cache
    if _people_cache is None:
        cur.execute("SELECT id, name_en, name_zh FROM people")
        _people_cache = {"en": {}, "zh": {}}
        for pid, en, zh in cur.fetchall():
            if en:
                _people_cache["en"][norm(en)] = pid
            if zh:
                _people_cache["zh"][norm(zh)] = pid
    pid = _people_cache["en"].get(norm(name_en))
    if pid is None:
        pid = _people_cache["zh"].get(norm(name_zh))
    if pid is not None:
        return pid, False
    if occupation:
        cur.execute(
            "INSERT INTO people(name_en, name_zh, primary_occupation, has_biography) "
            "VALUES (%s,%s,%s,%s)",
            (name_en, name_zh, occupation, has_bio),
        )
    else:
        cur.execute(
            "INSERT INTO people(name_en, name_zh, has_biography) VALUES (%s,%s,%s)",
            (name_en, name_zh, has_bio),
        )
    pid = cur.lastrowid
    _people_cache["en"][norm(name_en)] = pid
    if name_zh:
        _people_cache["zh"][norm(name_zh)] = pid
    return pid, True


def main():
    global _people_cache
    conn = get_conn()
    cur = conn.cursor()

    # ---------- 1. 本人主记录 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if row:
        pid0 = row[0]
        cur.execute(
            "UPDATE people SET qid=%s, name_zh=%s, gender=%s, birth_date=%s, death_date=%s, "
            "description=%s, primary_occupation=%s, has_biography=1, has_social_data=1 WHERE id=%s",
            (QID, "沃尔夫冈·泡利", "male", "1900-04-25", "1958-12-15",
             "Austrian theoretical physicist (1900–1958)", "physicist", pid0),
        )
        print(f"✓ 主记录已更新: {NAME} (id={pid0})")
    else:
        cur.execute(
            "INSERT INTO people(qid, name_en, name_zh, gender, birth_date, death_date, "
            "description, primary_occupation, has_biography, has_social_data) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1,1)",
            (QID, NAME, "沃尔夫冈·泡利", "male", "1900-04-25", "1958-12-15",
             "Austrian theoretical physicist (1900–1958)", "physicist"),
        )
        pid0 = cur.lastrowid
        print(f"✓ 主记录已新建: {NAME} (id={pid0})")

    # ---------- 2. 职业 ----------
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_phys = cur.fetchone()[0]
    cur.execute(
        "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
        (pid0, occ_phys),
    )

    # ---------- 3. 国籍 ----------
    for cname, rank in NATIONALITIES:
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (cname,))
        crow = cur.fetchone()
        if crow:
            cur.execute(
                "INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                (pid0, crow[0], rank),
            )
            print(f"✓ 国籍: {cname} (rank={rank})")

    # ---------- 4. 研究领域 ----------
    for f_en, f_zh, rank in FIELDS:
        fid = get_or_create_field(cur, f_en, f_zh)
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (pid0, fid, rank),
        )
        print(f"  + person_field: {f_en} (rank={rank})")

    # ---------- 5. 社会关系 ----------
    created = 0
    added = 0

    def add_relation(rel, name_en, name_zh, note, occupation, is_advisor):
        nonlocal created, added
        pid, is_new = upsert_person(cur, name_en, name_zh, occupation)
        if is_new:
            created += 1
            print(f"  + 新建(占位): {name_en or name_zh} (id={pid})")
            if occupation:
                cur.execute(
                    "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                    (pid, occ_phys),
                )
        else:
            print(f"  已有: {name_en or name_zh} (id={pid})")

        if rel == "advisor-student":
            f, t = (pid, pid0) if is_advisor else (pid0, pid)
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Wolfgang_Pauli')",
            (f, t, rel, note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name_en or name_zh}")

    for rel, name_en, name_zh, note in RELATIONS:
        is_advisor = name_en in ADVISORS
        add_relation(rel, name_en, name_zh, note, "physicist", is_advisor)

    for name_en, name_zh, note in SPOUSES:
        add_relation("spouse", name_en, name_zh, note, None, False)

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")

    # ---------- 6. 校验 ----------
    print("\n=== 泡利社会关系校验 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en=%s OR b.name_en=%s
        ORDER BY rt.relation_key, a.name_en, b.name_en""",
        (NAME, NAME),
    )
    for r in cur.fetchall():
        print(f"  {r[0]} |{r[1]}| {r[2]} — {(r[3] or '')[:36]}")

    cur.execute(
        "SELECT f.name_en, f.name_zh, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id "
        "WHERE pf.person_id=%s ORDER BY pf.rank",
        (pid0,),
    )
    print("\n=== 研究领域校验 ===")
    for r in cur.fetchall():
        print("  ", r)

    conn.close()


if __name__ == "__main__":
    main()
