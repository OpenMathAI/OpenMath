#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 E.C. Zeeman 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/E._C._Zeeman/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "E.C. Zeeman"
QID = "Q931311"

RELATIONS = [
    # 导师（有向：导师 → Zeeman）
    ("advisor-student", "Shaun Wylie", "博士导师（剑桥 1955）"),
    # 学生（有向：Zeeman → 学生）
    ("advisor-student", "C. T. C. Wall", "学生，手术理论奠基人"),
    ("advisor-student", "David B. A. Epstein", "学生，几何群论"),
    ("advisor-student", "Jenny Harrison", "学生，分析/拓扑"),
    ("advisor-student", "Ray Lickorish", "学生，纽结理论"),
    ("advisor-student", "Colin P. Rourke", "学生，PL 拓扑"),
    ("advisor-student", "Tim Poston", "学生，突变论"),
    ("advisor-student", "David Trotman", "学生，奇点理论"),
    ("advisor-student", "Peter Buneman", "学生，数据库理论"),
    # 相关（无向）
    ("colleague", "René Thom", "突变论理论创始者（Zeeman 将其推广普及）"),
    ("colleague", "Dennis Sullivan", "建议研究 Zeeman 谱序列（交同调先声）"),
]

MARKER = "[Zeeman-材料待展开] "

FIELDS = [
    ("topology", "拓扑学", 0),
    ("geometric topology", "几何拓扑", 1),
    ("singularity theory", "奇点理论", 2),
    ("catastrophe theory", "突变论", 3),
    ("knot theory", "纽结理论", 4),
]

AWARDS = [
    ("Senior Whitehead Prize", "高级怀特黑德奖", 1982),
    ("Michael Faraday Prize", "迈克尔·法拉第奖", 1988),
    ("David Crighton Medal", "大卫·克莱顿奖章", 2006),
    ("Forder Lectureship", "福德讲席", 0),
    ("Fellow of the Royal Society", "英国皇家学会会士", 0),
    ("Knight Bachelor", "下级勋位爵士", 1991),
    ("honorary doctor of Louis Pasteur University", "路易·巴斯德大学名誉博士", 0),
]

INSTITUTIONS = [
    ("Christ's College", "education", None, 1955),
    ("University of Cambridge", "education", None, 1955),
    ("University of Cambridge", "employment", 1955, 1964),
    ("University of Chicago", "employment", None, None),
    ("Institut des Hautes Études Scientifiques", "employment", None, None),
    ("University of Warwick", "employment", 1964, None),
    ("Gresham College", "employment", None, None),
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

    # ---------- 1. Zeeman 本人补齐 ----------
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
            "克里斯托弗·齐曼",
            '["Erik Christopher Zeeman","Sir Christopher Zeeman","突变论","华威数学研究所"]',
            "British mathematician (1925–2016)",
            "1925-02-04",
            "2016-02-13",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Zeeman id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("United Kingdom", "United Kingdom of Great Britain and Ireland")):
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
            if name == "Shaun Wylie":
                f, t = pid, pid0  # 导师 → Zeeman
            else:
                f, t = pid0, pid  # Zeeman → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Zeeman-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Zeeman 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='E.C. Zeeman' OR b.name_en='E.C. Zeeman'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
