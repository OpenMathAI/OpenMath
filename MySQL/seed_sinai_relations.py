#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Yakov Sinai 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Yakov_Sinai/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Yakov Sinai"
QID = "Q950897"

RELATIONS = [
    # 导师（有向：导师 → Sinai）
    ("advisor-student", "Andrey Kolmogorov", "博士导师（1960），Kolmogorov–Sinai 熵共同提出"),
    # 学生（有向：Sinai → 学生）
    ("advisor-student", "Grigory Margulis", "学生，Fields+Wolf+Abel 奖"),
    ("advisor-student", "Marina Ratner", "学生，Ratner 定理"),
    ("advisor-student", "Leonid Bunimovich", "学生，台球/混沌，Markov 划分合作"),
    ("advisor-student", "Nikolai Chernov", "学生，台球/双曲动力系统"),
    ("advisor-student", "Dmitry Dolgopyat", "学生，动力系统"),
    ("advisor-student", "Svetlana Jitomirskaya", "学生，准周期算子"),
    ("advisor-student", "Anatole Katok", "学生，遍历理论"),
    ("advisor-student", "Konstantin Khanin", "学生，重整化/NS 方程合作"),
    ("advisor-student", "Valeriy Oseledets", "学生，Oseledets 定理（乘法遍历定理）"),
    ("advisor-student", "Leonid Polterovich", "学生，辛几何"),
    ("advisor-student", "Corinna Ulcigrai", "学生，区间交换变换"),
    ("advisor-student", "Jonathan Mattingly", "学生，随机 NS 方程合作"),
    ("advisor-student", "Pavel Bleher", "学生，Bleher–Sinai 重整化"),
    # 家族（无向）
    ("parent-child", "Veniamin Kagan", "外祖父，莫斯科大学微分几何系主任"),
    ("spouse", "Elena B. Vul", "妻（数学家/物理学家），合著多篇论文"),
    # 相关（无向）
    ("colleague", "Alexander Esenin-Volpin", "1968 年支持的异见诗人/数学家（后其教授晋升受阻）"),
]

MARKER = "[Sinai-材料待展开] "

FIELDS = [
    ("dynamical systems", "动力系统", 0),
    ("ergodic theory", "遍历理论", 1),
    ("statistical mechanics", "统计力学", 2),
    ("probability theory", "概率论", 3),
    ("mathematical physics", "数学物理", 4),
]

AWARDS = [
    ("Boltzmann Medal", "玻尔兹曼奖章", 1986),
    ("Dannie Heineman Prize for Mathematical Physics", "海涅曼数学物理奖", 1990),
    ("ICTP Dirac Medal", "ICTP 狄拉克奖章", 1992),
    ("Wolf Prize in Mathematics", "沃尔夫数学奖", 1997),
    ("Nemmers Prize in Mathematics", "内默斯数学奖", 2002),
    ("Lagrange Prize", "拉格朗日奖", 2008),
    ("Henri Poincaré Prize", "亨利·庞加莱奖", 2009),
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士", 2009),
    ("Leroy P. Steele Prize for Lifetime Achievement", "斯蒂尔终身成就奖", 2013),
    ("Abel Prize", "阿贝尔奖", 2014),
    ("Marcel Grossmann Award", "马塞尔·格罗斯曼奖", 2015),
]

INSTITUTIONS = [
    ("Lomonosov Moscow State University", "education", None, 1960),
    ("Lomonosov Moscow State University", "employment", 1960, None),
    ("Landau Institute for Theoretical Physics", "employment", 1971, None),
    ("Princeton University", "employment", 1993, None),
    ("California Institute of Technology", "employment", 2005, None),
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
    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    phys_id = cur.fetchone()

    # ---------- 1. Sinai 本人补齐 ----------
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
            "雅科夫·西奈",
            '["Yakov Grigorevich Sinai","Яков Григорьевич Синай","Kolmogorov–Sinai 熵","Sinai 台球"]',
            "Russian-American mathematician (born 1935)",
            "1935-09-21",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if phys_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, phys_id[0]))
    print(f"Sinai id={pid0} 已补齐 people 字段（has_social_data=1，在世）")

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
    for idx, country in enumerate(("Soviet Union", "Russia", "United States")):
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
            if name == "Andrey Kolmogorov":
                f, t = pid, pid0  # 导师 → Sinai
            else:
                f, t = pid0, pid  # Sinai → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 祖父 → Sinai
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Sinai-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Sinai 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Yakov Sinai' OR b.name_en='Yakov Sinai'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
