#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Edmund Landau 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Edmund_Landau/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Edmund Landau"
QID = "Q58750"

RELATIONS = [
    # 导师（有向：导师 → Landau）
    ("advisor-student", "Ferdinand Georg Frobenius", "博士导师"),
    ("advisor-student", "Lazarus Fuchs", "博士导师"),
    # 学生（有向：Landau → 学生）
    ("advisor-student", "Carl Ludwig Siegel", "学生，解析数论大师"),
    ("advisor-student", "Paul Bernays", "学生，数学逻辑"),
    ("advisor-student", "Harald Bohr", "学生，几乎周期函数"),
    ("advisor-student", "Alexander Ostrowski", "学生，复分析与数值分析"),
    ("advisor-student", "Hans Heilbronn", "学生，解析数论"),
    ("advisor-student", "Grete Hermann", "学生，诺特首位博士生（后转）"),
    ("advisor-student", "Jacob Levitzki", "学生"),
    ("advisor-student", "Dunham Jackson", "学生，逼近论"),
    ("advisor-student", "Erich Kamke", "学生，微分方程"),
    ("advisor-student", "Vojtěch Jarník", "学生，解析数论"),
    ("advisor-student", "Arnold Walfisz", "学生，解析数论"),
    ("advisor-student", "Aubrey J. Kempner", "学生，数论"),
    ("advisor-student", "Gustav Doetsch", "学生，拉普拉斯变换"),
    ("advisor-student", "Binyamin Amirà", "学生，几何"),
    # 荣誉共同体（无向）
    ("co-honored", "G. H. Hardy", "'No one was ever more passionately devoted to mathematics than Landau'"),
    # 家族（姻亲）
    ("parent-child", "Paul Ehrlich", "岳父，诺贝尔生理学/医学奖得主"),
    ("spouse", "Marianne Ehrlich", "妻（1905 结婚）"),
    # 争议（无向）
    ("controversy", "Oswald Teichmüller", "1933 纳粹抵制活动的组织者"),
]

MARKER = "[Landau-材料待展开] "

FIELDS = [
    ("number theory", "数论", 0),
    ("analytic number theory", "解析数论", 1),
    ("complex analysis", "复分析", 2),
]

# 奖项（无重大奖项，仅保留科学院荣誉）
AWARDS = [
    ("honorary member of the Saint Petersburg Academy of Sciences", "圣彼得堡科学院荣誉院士", 1916),
]

INSTITUTIONS = [
    ("Humboldt University of Berlin", "education", 1894, 1899),
    ("Frederick William University Berlin", "employment", 1899, 1909),
    ("University of Göttingen", "employment", 1909, 1933),
    ("Hebrew University of Jerusalem", "employment", 1927, 1928),
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

    # ---------- 1. Landau 本人补齐 ----------
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
            "埃德蒙·兰道",
            '["Edmund Georg Hermann Landau","大 O 记号普及者","Landau 问题","解析数论奠基人"]',
            "German mathematician (1877–1938)",
            "1877-02-14",
            "1938-02-19",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Landau id={pid0} 已补齐 people 字段（has_social_data=1）")

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
            cur.execute("INSERT INTO awards(name_en, name_zh, award_type) VALUES (%s,%s,'honor')", (a_en, a_zh))
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
    for country in ("German Reich",):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (country,))
        cid = cur.fetchone()
        if cid:
            cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                        (pid0, cid[0]))
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
            if name in ("Ferdinand Georg Frobenius", "Lazarus Fuchs"):
                f, t = pid, pid0  # 导师 → Landau
            else:
                f, t = pid0, pid  # Landau → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 岳父 → Landau
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Landau-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Landau 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Edmund Landau' OR b.name_en='Edmund Landau'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
