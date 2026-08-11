#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Yuri Linnik 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Yuri_Linnik/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Yuri Linnik"
QID = "Q1384632"

RELATIONS = [
    # 导师（有向：导师 → Linnik）
    ("advisor-student", "Vladimir Tartakovsky", "博士导师（圣彼得堡大学）"),
    # 家族（无向）
    ("parent-child", "Vladimir Pavlovich Linnik", "父亲，苏联科学院院士（光学物理）"),
    # 学生/合作（有向：Linnik → 学生）
    ("advisor-student", "Jonas Kubilius", "学生，立陶宛数学家"),
    ("advisor-student", "Alfréd Rényi", "学生，匈牙利数学家"),
    ("advisor-student", "Ildar Ibragimov", "学生，概率统计"),
    ("advisor-student", "Valentin Petrov", "学生，概率论"),
    # 相关（无向）
    ("colleague", "Ivan Vinogradov", "圣彼得堡数论学派联系"),
    ("colleague", "Andrey Kolmogorov", "苏联概率学派联系"),
    ("colleague", "Pafnuty Chebyshev", "圣彼得堡数学传统（Chebyshev 学派）"),
]

MARKER = "[Linnik-材料待展开] "

FIELDS = [
    ("number theory", "数论", 0),
    ("analytic number theory", "解析数论", 1),
    ("probability theory", "概率论", 2),
    ("mathematical statistics", "数理统计", 3),
]

AWARDS = [
    ("Stalin Prize", "斯大林奖", 0),
    ("Lenin Prize", "列宁奖", 0),
    ("Order of Lenin", "列宁勋章", 0),
    ("Order of the Badge of Honour", "荣誉徽章勋章", 0),
    ("Order of the Red Banner of Labour", "劳动红旗勋章", 0),
    ("Hero of Socialist Labour", "社会主义劳动英雄", 0),
    ("Fellow of the Institute of Mathematical Statistics", "数理统计学会会士", 0),
]

INSTITUTIONS = [
    ("Saint Petersburg State University", "education", None, None),
    ("Saint Petersburg State University", "employment", None, None),
    ("Steklov Institute of Mathematics", "employment", None, None),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]
    cur.execute("SELECT id FROM occupations WHERE name_en='statistician'")
    stat_id = cur.fetchone()

    # ---------- 1. Linnik 本人补齐 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if not row:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',0,%s)",
            (NAME, QID),
        )
        pid0 = cur.lastrowid
    else:
        pid0 = row[0]
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            QID,
            "尤里·林尼克",
            '["Yuri Vladimirovich Linnik","Линник","Linnik 定理","大筛法"]',
            "Soviet mathematician (1915–1972)",
            "1915-01-08",
            "1972-06-30",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if stat_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, stat_id[0]))
    print(f"Linnik id={pid0} 已补齐 people 字段（has_social_data=1）")

    # ---------- 2. 研究领域 ----------
    for f_en, f_zh, rank in FIELDS:
        cur.execute("SELECT id FROM fields WHERE name_en=%s", (f_en,))
        frow = cur.fetchone()
        if not frow:
            cur.execute("INSERT INTO fields(name_en, name_zh) VALUES (%s,%s)", (f_en, f_zh))
            fid = cur.lastrowid
            print(f"  + 新建领域: {f_en} (id={fid})")
        else:
            fid = frow[0]
        cur.execute(
            "INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
            (pid0, fid, rank),
        )
    print("  领域关联完成")

    # ---------- 3. 奖项 ----------
    for a_en, a_zh, year in AWARDS:
        cur.execute("SELECT id FROM awards WHERE name_en=%s", (a_en,))
        arow = cur.fetchone()
        if not arow:
            cur.execute("INSERT INTO awards(name_en, name_zh, award_type) VALUES (%s,%s,'award')", (a_en, a_zh))
            aid = cur.lastrowid
            print(f"  + 新建奖项: {a_en} (id={aid})")
        else:
            aid = arow[0]
        note = None
        if year == 0:
            note = "年份待查"
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, `year`, share_type, source, note) "
            "VALUES (%s,%s,%s,'独享','Wikipedia',%s)",
            (pid0, aid, year, note),
        )
    print("  奖项关联完成")

    # ---------- 4. 机构 ----------
    for inst, rel, sy, ey in INSTITUTIONS:
        cur.execute("SELECT id FROM institutions WHERE name_en=%s", (inst,))
        irow = cur.fetchone()
        if not irow:
            cur.execute("INSERT INTO institutions(name_en) VALUES (%s)", (inst,))
            iid = cur.lastrowid
            print(f"  + 新建机构: {inst} (id={iid})")
        else:
            iid = irow[0]
        cur.execute(
            "SELECT 1 FROM person_institution WHERE person_id=%s AND inst_id=%s AND relation=%s",
            (pid0, iid, rel),
        )
        if not cur.fetchone():
            cur.execute(
                "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
                "VALUES (%s,%s,%s,%s,%s)",
                (pid0, iid, rel, sy, ey),
            )
    print("  机构关联完成")

    # ---------- 5. 国籍 ----------
    for idx, country in enumerate(("Russian Empire", "Soviet Union", "Ukrainian Soviet Socialist Republic")):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (country,))
        cid = cur.fetchone()
        if cid:
            cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                        (pid0, cid[0], idx))
    print("  国籍关联完成")

    # ---------- 6. 社会关系 ----------
    created = 0
    relations_added = 0
    for rel, name, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'mathematician',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                        (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name} (id={pid})")
        else:
            print(f"  已有: {name} (id={pid})")

        if rel == "advisor-student":
            if name == "Vladimir Tartakovsky":
                f, t = pid, pid0  # 导师 → Linnik
            else:
                f, t = pid0, pid  # Linnik → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 父 → Linnik
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Linnik-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Linnik 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Yuri Linnik' OR b.name_en='Yuri Linnik'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
