#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Issai Schur 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Issai_Schur/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Issai Schur"
QID = "Q72599"

RELATIONS = [
    # 老师（有向：导师 → Schur）
    ("advisor-student", "Ferdinand Georg Frobenius", "柏林大学博士导师（1901），表示论传承"),
    ("advisor-student", "Lazarus Fuchs", "柏林大学博士导师（1901）"),
    # 学生（有向：Schur → 学生）
    ("advisor-student", "Richard Brauer", "1925 柏林博士；模表示论奠基人"),
    ("advisor-student", "Alfred Brauer", "1928 柏林博士；数论"),
    ("advisor-student", "Heinz Prüfer", "1921 柏林博士；Prüfer 群与 Prüfer 域"),
    ("advisor-student", "Richard Rado", "1933 柏林博士；组合学，Rado 定理"),
    ("advisor-student", "Bernhard Neumann", "1932 柏林博士；群论"),
    ("advisor-student", "Isaac Jacob Schoenberg", "1926 博士；样条插值，Toeplitz 矩阵"),
    ("advisor-student", "Helmut Wielandt", "1935 柏林博士；置换群，Wielandt 定理"),
    ("advisor-student", "Wilhelm Specht", "1932 柏林博士；群环与特征标"),
    ("advisor-student", "Karl Dörge", "1925 柏林博士；图论"),
    ("advisor-student", "Wolfgang Hahn", "柏林博士；特殊函数，Hahn 多项式"),
    ("advisor-student", "Félix Pollaczek", "1922 柏林博士；排队论"),
    ("advisor-student", "Robert Frucht", "柏林博士；图的自同构，Frucht 定理"),
    ("advisor-student", "Eberhard Hopf", "柏林博士；遍历理论，Hopf 纤维化"),
    ("advisor-student", "Rose Peltesohn", "柏林博士；组合设计"),
    # 同事（无向）
    ("colleague", "Erhard Schmidt", "柏林同事；纳粹时期为 Schur 复职奔走"),
    ("colleague", "George Pólya", "挚友；组织 1936 苏黎世讲座"),
    ("colleague", "Heinz Hopf", "柏林同事；高度敬重 Schur"),
    ("colleague", "Hermann Weyl", "评价 Schur 的代数贡献可与 Emmy Noether 比肩"),
    ("colleague", "Emmy Noether", "同为柏林代数大师"),
]

MARKER = "[Schur-材料待展开] "

FIELDS = [
    ("representation theory", "表示论", 0),
    ("group theory", "群论", 1),
    ("combinatorics", "组合学", 2),
    ("number theory", "数论", 3),
]

INSTITUTIONS = [
    ("Humboldt University of Berlin", "education", 1894, 1901),
    ("Humboldt University of Berlin", "employment", 1903, 1913),
    ("University of Bonn", "employment", 1913, 1916),
    ("Humboldt University of Berlin", "employment", 1916, 1935),
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

    # ---------- 1. Schur 本人补齐 ----------
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
            "伊赛·舒尔",
            '["J. Schur","Schaia Schur","Schur 引理的创造者","Schur 函数的命名者","柏林表示论学派的旗手"]',
            "Russian-German mathematician (1875–1941)",
            "1875-01-10",
            "1941-01-10",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Schur id={pid0} 已补齐 people 字段（has_social_data=1）")

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

    # ---------- 3. 机构 ----------
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
            (pid0, iid, rel, sy, ey),
        )
    print("  机构关联完成")

    # ---------- 4. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='Germany'")
    de = cur.fetchone()
    if de:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, de[0]))
    print("  国籍关联完成")

    # ---------- 5. 社会关系 ----------
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
                f, t = pid, pid0  # 导师 → Schur
            else:
                f, t = pid0, pid  # Schur → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Schur-presentation')",
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

    print("\n=== 校验：Issai Schur 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Issai Schur' OR b.name_en='Issai Schur'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
