#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Ernst Zermelo 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Ernst_Zermelo/（Wikipedia 存档）

关系：
- 老师：Lazarus Fuchs, Hermann Schwarz（柏林博士导师）
- 同事：Max Planck（1894-97 助手）, David Hilbert（哥廷根同事）, Georg Cantor, Richard Dedekind
- 合作者：Abraham Fraenkel, Thoralf Skolem（1922 扩展 ZF）
- 学生：Walter Benz, Stefan Straszewicz, Pessach Hebroni
- 配偶：Gertrud Seekamp
"""
import re
import unicodedata

from db_mysql import get_conn

ZERMELO_NAME = "Ernst Zermelo"
ZERMELO_QID = "Q57248"

RELATIONS = [
    # 老师（有向：导师 → Zermelo）
    ("advisor-student", "Lazarus Fuchs", "柏林大学博士导师（1894，变分法论文）"),
    ("advisor-student", "Hermann Schwarz", "柏林大学博士导师（1894）"),
    # 同事（无向）
    ("colleague", "Max Planck", "1894–1897 任 Planck 助手，研究水动力学"),
    ("colleague", "David Hilbert", "哥廷根同事；1900 巴黎问题第一问激励良序定理"),
    ("colleague", "Georg Cantor", "集合论先驱，Zermelo 深受其影响"),
    ("colleague", "Richard Dedekind", "1908 改进证明采用 Dedekind 的『chain』概念"),
    # 合作者（无向）
    ("collaborator", "Abraham Fraenkel", "1922 扩展 ZF 公理（替换公理）"),
    ("collaborator", "Thoralf Skolem", "1922 独立扩展 ZF 公理（替换公理+正则公理）"),
    # 学生（有向：Zermelo → 学生）
    ("advisor-student", "Walter Benz", "学生，几何学家"),
    ("advisor-student", "Stefan Straszewicz", "学生，几何学家"),
    ("advisor-student", "Pessach Hebroni", "学生，以色列数学家"),
    # 配偶（有向：夫妻）
    ("spouse", "Gertrud Seekamp", "1944 结婚"),
]

MARKER = "[Zermelo-材料待展开] "

FIELDS = [
    ("set theory", "集合论", 0),
    ("mathematical logic", "数理逻辑", 1),
    ("foundations of mathematics", "数学基础", 2),
]

AWARDS = [
    ("Ackermann–Teubner Memorial Award", 1916),
]

INSTITUTIONS = [
    # 教育
    ("Humboldt University of Berlin", "education", 1889, 1894),
    ("University of Göttingen", "education", 1897, 1899),
    ("University of Freiburg", "education", None, None),
    ("Martin Luther University Halle-Wittenberg", "education", None, None),
    # 任职
    ("Humboldt University of Berlin", "employment", 1894, 1897),
    ("University of Göttingen", "employment", 1899, 1910),
    ("University of Zurich", "employment", 1910, 1916),
    ("University of Freiburg", "employment", 1926, 1935),
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

    # ---------- 1. Zermelo 本人补齐 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (ZERMELO_NAME,))
    row = cur.fetchone()
    if not row:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',0,%s)",
            (ZERMELO_NAME, ZERMELO_QID),
        )
        zermelo_id = cur.lastrowid
    else:
        zermelo_id = row[0]
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            ZERMELO_QID,
            "恩斯特·策梅罗",
            '["ZFC 公理体系的奠基人","选择公理的引入者","良序定理的证明者"]',
            "German mathematician (1871–1953)",
            "1871-07-27",
            "1953-05-21",
            zermelo_id,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (zermelo_id, occ_id))
    print(f"Zermelo id={zermelo_id} 已补齐 people 字段（has_social_data=1）")

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
            (zermelo_id, fid, rank),
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
            "VALUES (%s,%s,%s,'独享','Wikipedia')",
            (zermelo_id, aid, year),
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
            (zermelo_id, iid, rel, sy, ey),
        )
    print("  机构关联完成")

    # ---------- 5. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='Germany'")
    de = cur.fetchone()
    if de:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (zermelo_id, de[0]))
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
            if name in ("Lazarus Fuchs", "Hermann Schwarz"):
                f, t = pid, zermelo_id  # 导师 → Zermelo
            else:
                f, t = zermelo_id, pid  # Zermelo → 学生
        elif rel == "spouse":
            f, t = zermelo_id, pid
        else:
            f, t = sorted([zermelo_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Zermelo-presentation')",
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

    print("\n=== 校验：Ernst Zermelo 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Ernst Zermelo' OR b.name_en='Ernst Zermelo'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
