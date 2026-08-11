#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Graeme Segal 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Graeme_Segal/（Wikipedia 存档）
注意：has_biography=1（已立传），本次仅补社会关系/研究领域。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Graeme Segal"
QID = "Q1398998"

RELATIONS = [
    # 导师（有向：导师 → Segal）
    ("advisor-student", "Michael Atiyah", "博士导师（牛津 1967）"),
    # 学生（有向：Segal → 学生）
    ("advisor-student", "Constantin Teleman", "学生，几何表示论"),
    ("advisor-student", "Andrew Pressley", "学生，可积系统"),
    ("advisor-student", "George Wilson", "学生，微分方程"),
    ("advisor-student", "Martin Guest", "学生，调和映射"),
    # 家族（配偶）
    ("spouse", "Marina Warner", "妻（作家、神话学者）"),
]

MARKER = "[Segal-材料待展开] "

FIELDS = [
    ("algebraic topology", "代数拓扑", 0),
    ("homotopy theory", "同伦论", 1),
    ("K-theory", "K 理论", 2),
    ("topological quantum field theory", "拓扑量子场论", 3),
    ("elliptic cohomology", "椭圆上同调", 4),
]

AWARDS = [
    ("Fellow of the Royal Society", "英国皇家学会会士", 1982),
    ("Pólya Prize (LMS)", "波利亚奖（伦敦数学会）", 1990),
    ("Sylvester Medal", "西尔维斯特奖章", 2010),
    ("Chern Medal", "陈省身奖章", 2026),
]

INSTITUTIONS = [
    ("University of Sydney", "education", None, 1961),
    ("St Catherine's College", "education", None, 1967),
    ("University of Oxford", "education", None, 1967),
    ("University of Oxford", "employment", 1964, 1990),
    ("University of Cambridge", "employment", 1990, 1999),
    ("All Souls College", "employment", 1999, 2009),
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

    # ---------- 1. Segal 本人补齐 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if not row:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',1,%s)",
            (NAME, QID),
        )
        pid0 = cur.lastrowid
    else:
        pid0 = row[0]
    cur.execute(
        "UPDATE people SET qid=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=NULL, has_social_data=1 WHERE id=%s",
        (
            QID,
            '["Graeme Bryce Segal","Atiyah–Segal 完备化定理","Segal 猜想","Chern Medal 2026"]',
            "Australian mathematician, Lowndean Professor (born 1941)",
            "1941-12-21",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Segal id={pid0} 已补齐 people 字段（has_social_data=1，在世）")

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
    cur.execute("SELECT id FROM countries WHERE name_en='Australia'")
    au = cur.fetchone()
    if not au:
        cur.execute("INSERT IGNORE INTO countries(name_en, name_zh, is_current) VALUES ('Australia','澳大利亚',1)")
        au = cur.lastrowid
        print(f"  + 新建国家: Australia (id={au})")
    else:
        au = au[0]
    cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                (pid0, au))
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
            if name == "Michael Atiyah":
                f, t = pid, pid0  # 导师 → Segal
            else:
                f, t = pid0, pid  # Segal → 学生
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Segal-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Segal 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Graeme Segal' OR b.name_en='Graeme Segal'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
