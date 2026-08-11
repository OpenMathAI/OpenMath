#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Erich Hecke 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Erich_Hecke/（Wikipedia 存档）

关系：
- 老师：David Hilbert
- 学生：Kurt Reidemeister, Heinrich Behnke, Hans Petersson, Bruno Schoeneberg,
         Wilhelm Maak, Hans Maass, Ernst-August Behrens, Erna Witt
- 荣誉共同体/同事：André Weil（Weil 在前言盛赞 Hecke）
- 同事：Emil Artin（汉堡学派）

入库内容：
- people: 补齐 qid/name_variants/description/birth/death，has_social_data=1
- person_field: number theory / modular forms / analytic number theory（补字典）
- award_laureate: Ackermann–Teubner Memorial Award 1938
- person_institution: 教育(education)/任职(employment)
- person_nationality: German Empire → Germany
- person_relation: 社会关系
"""
import re
import unicodedata

from db_mysql import get_conn

# Hecke 本人
HECKE_NAME = "Erich Hecke"
HECKE_QID = "Q687638"

# 社会关系清单：(关系类型, 人物, 备注)
# advisor-student 有向（师→生）；colleague 无向
HECKE_RELATIONS = [
    # 老师（有向：Hilbert → Hecke）
    ("advisor-student", "David Hilbert", "哥廷根博士导师，Hilbert 学派数论传承"),
    # 学生（有向：Hecke → 学生）
    ("advisor-student", "Kurt Reidemeister", "学生，拓扑学，马堡/哥尼斯堡/哥廷根教授"),
    ("advisor-student", "Heinrich Behnke", "学生，复分析，明斯特学派开创者"),
    ("advisor-student", "Hans Petersson", "学生，模形式，Petersson 度量"),
    ("advisor-student", "Bruno Schoeneberg", "学生，模形式与椭圆函数，汉堡学派"),
    ("advisor-student", "Wilhelm Maak", "学生，离散子群与自守函数，汉堡学派"),
    ("advisor-student", "Hans Maass", "学生，Maass 形式，自守形式"),
    ("advisor-student", "Ernst-August Behrens", "学生，汉堡学派"),
    ("advisor-student", "Erna Witt", "学生，汉堡学派（Ernst Witt 的妹妹）"),
    # 荣誉共同体（无向）：Weil 在《Basic Number Theory》前言盛赞 Hecke
    ("co-honored", "André Weil", "Weil 在《Basic Number Theory》前言称『在经典路径上超越 Hecke 是徒劳且不可能的』"),
    # 同事（无向）：汉堡学派共同缔造者
    ("colleague", "Emil Artin", "汉堡学派共同缔造者，代数数论与类域论同事"),
]

MARKER = "[Hecke-材料待展开] "

# 研究领域（rank 排序）
FIELDS = [
    ("number theory", "数论", 0),
    ("modular forms", "模形式", 1),
    ("analytic number theory", "解析数论", 2),
]

# 奖项
AWARDS = [
    ("Ackermann–Teubner Memorial Award", 1938),
]

# 机构：(name_en, relation, start, end)
INSTITUTIONS = [
    # 教育
    ("University of Göttingen", "education", 1906, 1910),
    ("University of Wrocław", "education", None, None),
    # 任职
    ("University of Basel", "employment", 1915, 1918),
    ("University of Göttingen", "employment", 1918, 1919),
    ("University of Hamburg", "employment", 1919, 1947),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 载入 people 索引
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    # 数学家职业
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    # ---------- 1. Hecke 本人补齐字段 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (HECKE_NAME,))
    row = cur.fetchone()
    if not row:
        print("⚠ Hecke 不在库中，先建占位")
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',0,%s)",
            (HECKE_NAME, HECKE_QID),
        )
        hecke_id = cur.lastrowid
    else:
        hecke_id = row[0]
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            HECKE_QID,
            "埃里希·赫克",
            '["Hecke 算子的创造者","模形式理论的奠基人","Langlands 纲领的数学源头"]',
            "German mathematician (1887–1947)",
            "1887-09-20",
            "1947-02-13",
            hecke_id,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (hecke_id, occ_id))
    print(f"Hecke id={hecke_id} 已补齐 people 字段（has_social_data=1）")

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
            (hecke_id, fid, rank),
        )
    print(f"  领域关联完成")

    # ---------- 3. 奖项 ----------
    for a_en, year in AWARDS:
        cur.execute("SELECT id FROM awards WHERE name_en=%s", (a_en,))
        arow = cur.fetchone()
        if not arow:
            cur.execute("INSERT INTO awards(name_en) VALUES (%s)", (a_en,))
            aid = arow_id = cur.lastrowid
            print(f"  + 新建奖项: {a_en} (id={aid})")
        else:
            aid = arow[0]
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, `year`, share_type, source) "
            "VALUES (%s,%s,%s,'独享','Wikipedia')",
            (hecke_id, aid, year),
        )
    print(f"  奖项关联完成")

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
            (hecke_id, iid, rel, sy, ey),
        )
    print(f"  机构关联完成")

    # ---------- 5. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='German Empire'")
    ge = cur.fetchone()
    if ge:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (hecke_id, ge[0]))
    cur.execute("SELECT id FROM countries WHERE name_en='Germany'")
    de = cur.fetchone()
    if de:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,1)",
                    (hecke_id, de[0]))
    print("  国籍关联完成")

    # ---------- 6. 社会关系 ----------
    created = 0
    relations_added = 0
    for rel, name, note in HECKE_RELATIONS:
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
            if name == "David Hilbert":
                f, t = pid, hecke_id  # Hilbert → Hecke
            else:
                f, t = hecke_id, pid  # Hecke → 学生
        else:
            f, t = sorted([hecke_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Hecke-presentation')",
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

    # 校验：Hecke 全维度
    print("\n=== 校验：Erich Hecke 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Erich Hecke' OR b.name_en='Erich Hecke'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
