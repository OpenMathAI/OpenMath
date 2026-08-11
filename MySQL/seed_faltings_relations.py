#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Gerd Faltings 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Gerd_Faltings/（Wikipedia 存档）
注意：在世数学家（1954-），无死亡日期。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Gerd Faltings"
QID = "Q77137"

RELATIONS = [
    # 导师（有向：导师 → Faltings）
    ("advisor-student", "Hans-Joachim Nastold", "博士导师（明斯特大学 1978）"),
    # 学生（有向：Faltings → 学生）
    ("advisor-student", "Shinichi Mochizuki", "学生，IUT 理论（望月新一）"),
    ("advisor-student", "Wiesława Nizioł", "学生，p-adic Hodge 理论"),
    ("advisor-student", "Nikolai Durov", "学生，代数几何/同伦"),
    ("advisor-student", "Michael J. Larsen", "学生，群论/表示论"),
    ("advisor-student", "Christian Liedtke", "学生，代数曲面"),
    ("advisor-student", "Adrian Vasiu", "学生，p 可除群"),
    ("advisor-student", "Tyler Jamison Jarvis", "学生，镜像对称"),
    ("advisor-student", "Agnes Tillmann", "学生，拓扑 K 理论"),
    # 合作者（无向）
    ("collaborator", "Gisbert Wüstholz", "合著《有理点》(Rational Points)，重证 Roth 定理"),
    ("collaborator", "Paul Vojta", "扩展其方法证明 Mordell–Lang 猜想"),
    # 家族（配偶）
    ("spouse", "Angelika Tschimmel", "妻（1984 结婚，2011 去世）"),
]

MARKER = "[Faltings-材料待展开] "

FIELDS = [
    ("algebraic geometry", "代数几何", 0),
    ("arithmetic geometry", "算术几何", 1),
    ("number theory", "数论", 2),
    ("Diophantine equation", "丢番图方程", 3),
    ("p-adic Hodge theory", "p-adic Hodge 理论", 4),
]

# 全部奖项收录
AWARDS = [
    ("Dannie Heineman Prize", "丹尼·海涅曼奖", 1983),
    ("Fields Medal", "菲尔兹奖", 1986),
    ("ICM Speaker", "国际数学家大会受邀报告人", 1986),
    ("Guggenheim Fellowship", "古根海姆学者奖", 1988),
    ("Gottfried Wilhelm Leibniz Prize", "戈特弗里德·威廉·莱布尼茨奖", 1996),
    ("The Karl Georg Christian von Staudt Prize", "冯·施陶特奖", 2008),
    ("Heinz Gumin Prize for Mathematics", "海因茨·古明数学奖", 2010),
    ("King Faisal International Prize in Science", "费萨尔国王国际科学奖", 2014),
    ("The Shaw Prize in Mathematical Sciences", "邵逸夫数学科学奖", 2015),
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士", 2016),
    ("Cantor Medal", "康托尔奖章", 2017),
    ("Foreign Associate of the National Academy of Sciences", "美国国家科学院外籍院士", 2018),
    ("Pour le Mérite for Sciences and Arts", "功勋勋章（科学与艺术）", 2024),
    ("Abel Prize", "阿贝尔奖", 2026),
]

INSTITUTIONS = [
    ("University of Münster", "education", 1972, 1978),
    ("University of Münster", "employment", 1981, 1982),
    ("University of Wuppertal", "employment", 1982, 1984),
    ("Princeton University", "employment", 1985, 1994),
    ("Institute for Advanced Study", "employment", None, None),
    ("Max Planck Institute for Mathematics", "employment", 1994, 2018),
    ("University of Bonn", "employment", None, None),
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
    cur.execute("SELECT id FROM occupations WHERE name_en='university teacher'")
    uni_id = cur.fetchone()

    # ---------- 1. Faltings 本人补齐 ----------
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
        "birth_date=%s, death_date=NULL, has_social_data=1 WHERE id=%s",
        (
            QID,
            "格尔德·法尔廷斯",
            '["Gerd Faltings","莫德尔猜想证明者","Faltings 定理","算术几何"]',
            "German mathematician, Fields Medal 1986 & Abel Prize 2026 (born 1954)",
            "1954-07-28",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if uni_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, uni_id[0]))
    print(f"Faltings id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    cur.execute("SELECT id FROM countries WHERE name_en='Germany'")
    de = cur.fetchone()
    if de:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, de[0]))
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
            if name == "Hans-Joachim Nastold":
                f, t = pid, pid0  # 导师 → Faltings
            else:
                f, t = pid0, pid  # Faltings → 学生
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Faltings-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Faltings 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Gerd Faltings' OR b.name_en='Gerd Faltings'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
