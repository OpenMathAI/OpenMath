#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Nikolai Luzin 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Nikolai_Luzin/（Wikipedia 存档）
注意：死亡日期以正文 infobox 1950-02-28 为准。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Nikolai Luzin"
QID = "Q374024"

RELATIONS = [
    # 导师（有向：导师 → Luzin）
    ("advisor-student", "Dmitri Egorov", "博士导师（莫斯科大学）"),
    ("advisor-student", "Edmund Landau", "哥廷根时期（1910-14）影响者"),
    # 学生（有向：Luzin → 学生）
    ("advisor-student", "Pavel Alexandrov", "学生，拓扑学家"),
    ("advisor-student", "Andrey Kolmogorov", "学生，概率论大师"),
    ("advisor-student", "Aleksandr Khinchin", "学生，概率论/数论"),
    ("advisor-student", "Mikhail Suslin", "学生，描述集合论（解析集）共同奠基"),
    ("advisor-student", "Mikhail Lavrentyev", "学生，复分析/流体力学"),
    ("advisor-student", "Nina Bari", "学生，三角级数"),
    ("advisor-student", "Lev Schnirelmann", "学生，数论（密度方法）"),
    ("advisor-student", "Pavel Urysohn", "学生，拓扑学"),
    ("advisor-student", "Pyotr Novikov", "学生，群论/数理逻辑"),
    ("advisor-student", "Alexander Kronrod", "学生，数值分析"),
    ("advisor-student", "Lazar Lyusternik", "学生，拓扑方法/泛函分析"),
    ("advisor-student", "Alexey Lyapunov", "学生，控制论/集合论"),
    ("advisor-student", "Dmitrii Menshov", "学生，三角级数"),
    # 相关（无向）
    ("colleague", "Pavel Florensky", "前数学同窗，神学家（宗教影响）"),
]

MARKER = "[Luzin-材料待展开] "

FIELDS = [
    ("descriptive set theory", "描述集合论", 0),
    ("function theory", "函数论", 1),
    ("mathematical analysis", "数学分析", 2),
    ("real analysis", "实分析", 3),
    ("point-set topology", "点集拓扑", 4),
]

AWARDS = [
    ("Order of the Red Banner of Labour", "劳动红旗勋章", 0),
    ("Stalin Prize", "斯大林奖", 1946),
]

INSTITUTIONS = [
    ("Lomonosov Moscow State University", "education", 1901, 1905),
    ("University of Göttingen", "education", 1910, 1914),
    ("Lomonosov Moscow State University", "employment", 1920, None),
    ("Steklov Institute of Mathematics", "employment", None, None),
    ("Ivanovo State University of Chemistry and Technology", "employment", 1918, 1920),
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

    # ---------- 1. Luzin 本人补齐 ----------
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
            "尼古拉·鲁津",
            '["Nikolai Nikolayevich Luzin","Lusin","Николай Николаевич Лузин","描述集合论奠基人"]',
            "Soviet mathematician, founder of descriptive set theory (1883–1950)",
            "1883-12-09",
            "1950-02-28",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Luzin id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("Russian Empire", "Soviet Union")):
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
            if name in ("Dmitri Egorov", "Edmund Landau"):
                f, t = pid, pid0  # 导师 → Luzin
            else:
                f, t = pid0, pid  # Luzin → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Luzin-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Luzin 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Nikolai Luzin' OR b.name_en='Nikolai Luzin'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
