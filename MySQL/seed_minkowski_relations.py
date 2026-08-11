#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Hermann Minkowski 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Hermann_Minkowski/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Hermann Minkowski"
QID = "Q57246"

RELATIONS = [
    # 老师（有向：导师 → Minkowski）
    ("advisor-student", "Ferdinand von Lindemann", "柯尼斯堡大学博士导师（1885，数的几何方向）"),
    # 学生（有向：Minkowski → 学生）
    ("advisor-student", "Albert Einstein", "ETH Zurich 任教时教过爱因斯坦（1896–1902），后者 1905 狭义相对论被其几何化"),
    ("advisor-student", "Constantin Carathéodory", "哥廷根学生，测度论与变分法大家"),
    ("advisor-student", "Dénes Kőnig", "学生，图论先驱（柯尼斯堡七桥问题的图论化）"),
    ("advisor-student", "Louis Kollros", "学生，几何学家，苏黎世教授"),
    # 同事（无向）
    ("colleague", "David Hilbert", "柯尼斯堡同窗、哥廷根同事、一生挚友；Hilbert 写就感人悼词"),
    ("colleague", "Max Born", "哥廷根晚辈；Minkowski 逝世时 Born 代表数学学生致悼词"),
    # 荣誉共同体（无向）：1883 共享法国科学院大奖
    ("co-honored", "Henry John Stephen Smith", "1883 年共享法国科学院数学大奖（Smith 追授）"),
    # 配偶（夫妻）
    ("spouse", "Auguste Adler", "1897 结婚，育有两个女儿"),
]

MARKER = "[Minkowski-材料待展开] "

FIELDS = [
    ("geometry of numbers", "数的几何", 0),
    ("number theory", "数论", 1),
    ("mathematical physics", "数学物理", 2),
    ("theory of relativity", "相对论", 3),
]

AWARDS = [
    ("Grand prix des sciences mathématiques", 1883),
]

INSTITUTIONS = [
    # 教育
    ("University of Königsberg", "education", 1880, 1885),
    ("Frederick William University Berlin", "education", None, None),
    # 任职
    ("University of Bonn", "employment", 1887, 1894),
    ("University of Königsberg", "employment", 1894, 1896),
    ("ETH Zurich", "employment", 1896, 1902),
    ("University of Göttingen", "employment", 1902, 1909),
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
    phys_id = cur.fetchone()[0]

    # ---------- 1. Minkowski 本人补齐 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    row = cur.fetchone()
    if not row:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',0,%s)",
            (NAME, QID),
        )
        mid = cur.lastrowid
    else:
        mid = row[0]
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            QID,
            "赫尔曼·闵可夫斯基",
            '["数的几何的创造者","Minkowski 时空的提出者"]',
            "German mathematician and physicist (1864–1909)",
            "1864-06-22",
            "1909-01-12",
            mid,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (mid, occ_id))
    if phys_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (mid, phys_id))
    print(f"Minkowski id={mid} 已补齐 people 字段（has_social_data=1）")

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
            (mid, fid, rank),
        )
    print("  领域关联完成")

    # ---------- 3. 奖项 ----------
    for a_en, year in AWARDS:
        cur.execute("SELECT id FROM awards WHERE name_en=%s", (a_en,))
        arow = cur.fetchone()
        if not arow:
            cur.execute("INSERT INTO awards(name_en) VALUES (%s)", (a_en,))
            aid = cur.lastrowid
            print(f"  + 新建奖项: {a_en} (id={aid})")
        else:
            aid = arow[0]
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, `year`, share_type, source) "
            "VALUES (%s,%s,%s,'共享','Wikipedia')",
            (mid, aid, year),
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
            "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
            "VALUES (%s,%s,%s,%s,%s)",
            (mid, iid, rel, sy, ey),
        )
    print("  机构关联完成")

    # ---------- 5. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='Kingdom of Prussia'")
    kp = cur.fetchone()
    if kp:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (mid, kp[0]))
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
            if name == "Ferdinand von Lindemann":
                f, t = pid, mid  # 导师 → Minkowski
            else:
                f, t = mid, pid  # Minkowski → 学生
        elif rel == "spouse":
            f, t = mid, pid
        else:
            f, t = sorted([mid, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Minkowski-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Hermann Minkowski 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Hermann Minkowski' OR b.name_en='Hermann Minkowski'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
