#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Salomon Bochner 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Salomon_Bochner/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Salomon Bochner"
QID = "Q215967"

RELATIONS = [
    # 导师（有向：导师 → Bochner）
    ("advisor-student", "Erhard Schmidt", "博士导师（柏林，论文含 Bergman 核）"),
    # 学生（有向：Bochner → 学生）
    ("advisor-student", "Eugenio Calabi", "学生，Calabi-Yau 流形"),
    ("advisor-student", "Jeff Cheeger", "学生，Cheeger 常数"),
    ("advisor-student", "Hillel Furstenberg", "学生，遍历理论/数论，Wolf+Abel 奖"),
    ("advisor-student", "Samuel Karlin", "学生，生物数学"),
    ("advisor-student", "Sigurður Helgason", "学生，对称空间"),
    ("advisor-student", "Anthony W. Knapp", "学生，表示论"),
    ("advisor-student", "Richard Askey", "学生，特殊函数"),
    ("advisor-student", "Herbert Scarf", "学生，数理经济"),
    ("advisor-student", "Robert C. Gunning", "学生，多复变"),
    ("advisor-student", "Lynn Harold Loomis", "学生，调和分析"),
    ("advisor-student", "Harry Rauch", "学生，黎曼曲面"),
    ("advisor-student", "Gilbert Hunt", "学生，Markov 过程/位势论"),
    ("advisor-student", "Israel Halperin", "学生，算子代数"),
    ("advisor-student", "Carl S. Herz", "学生，调和分析"),
    ("advisor-student", "William A. Veech", "学生，遍历理论"),
    ("advisor-student", "M. T. Cheng", "学生，多重三角级数"),
    ("advisor-student", "Joseph H. Sampson", "学生，微分几何"),
    ("advisor-student", "Gerard Washnitzer", "学生，代数拓扑"),
    ("advisor-student", "Bernard Russell Gelbaum", "学生"),
    ("advisor-student", "Charles L. Dolph", "学生"),
    ("advisor-student", "Fritz Joachim Weyl", "学生，Hermann Weyl 之子"),
    # 合作者（无向）
    ("collaborator", "Kentaro Yano", "合著《Curvature and Betti Numbers》(1953)"),
    ("collaborator", "W. T. Martin", "合著《Several Complex Variables》(1948)"),
    # 荣誉共同体（无向）
    ("co-honored", "Harald Bohr", "几乎周期函数（Bochner 简化 Bohr 方法）"),
]

MARKER = "[Bochner-材料待展开] "

FIELDS = [
    ("harmonic analysis", "调和分析", 0),
    ("probability theory", "概率论", 1),
    ("differential geometry", "微分几何", 2),
    ("mathematical analysis", "数学分析", 3),
    ("several complex variables", "多复变函数", 4),
]

AWARDS = [
    ("Leroy P. Steele Prize", "斯蒂尔奖", 1979),
]

INSTITUTIONS = [
    ("Frederick William University Berlin", "education", None, None),
    ("Ludwig Maximilian University of Munich", "employment", 1924, 1933),
    ("Princeton University", "employment", 1933, 1968),
    ("Institute for Advanced Study", "employment", 1945, 1948),
    ("Rice University", "employment", 1968, 1982),
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

    # ---------- 1. Bochner 本人补齐 ----------
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
            "所罗门·博赫纳",
            '["Solomon Bochner","Bochner 定理","Bochner 积分","Bochner 公式"]',
            "American mathematician (1899–1982)",
            "1899-08-20",
            "1982-05-02",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Bochner id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("United States", "Germany")):
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
            if name == "Erhard Schmidt":
                f, t = pid, pid0  # 导师 → Bochner
            else:
                f, t = pid0, pid  # Bochner → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Bochner-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Bochner 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Salomon Bochner' OR b.name_en='Salomon Bochner'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
