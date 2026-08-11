#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Paul Lévy 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Paul_Lévy/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Paul Lévy"
QID = "Q441127"

RELATIONS = [
    # 老师（有向：导师 → Lévy）
    ("advisor-student", "Jacques Hadamard", "博士导师"),
    ("advisor-student", "Vito Volterra", "博士导师"),
    # 学生（有向：Lévy → 学生）
    ("advisor-student", "Wolfgang Doeblin", "学生，1940 阵亡的概率论天才"),
    ("advisor-student", "Michel Loève", "学生，《Probability Theory》教科书作者"),
    ("advisor-student", "Benoît Mandelbrot", "学生，分形几何之父"),
    ("advisor-student", "Georges Matheron", "学生，地质统计学"),
    ("advisor-student", "Pierre Rosenstiehl", "学生，图论与组合学"),
    # 家族（父→女 + 姻亲）
    ("parent-child", "Marie-Hélène Schwartz", "女儿，数学家"),
    ("parent-child", "Laurent Schwartz", "女婿，分布论创始人"),  # 姻亲用 parent-child 近似（直系）
    # 同事（无向）
    ("colleague", "Aleksandr Khinchin", "独立发现 Lévy–Khintchine 表示"),
    ("colleague", "Joseph L. Doob", "鞅理论继承者，发展为一般理论"),
    ("colleague", "Norbert Wiener", "布朗运动（Wiener 过程）共同奠基者"),
    ("spouse", "Suzanne Lévy", "妻（1913 结婚）"),
]

MARKER = "[Lévy-材料待展开] "

FIELDS = [
    ("probability theory", "概率论", 0),
    ("stochastic process", "随机过程", 1),
    ("functional analysis", "泛函分析", 2),
]

# 全部奖项收录
AWARDS = [
    ("Cours Peccot", "佩科课程奖", 1920),
    ("Poncelet Prize", "庞斯莱奖", 1932),
    ("Commander of the Legion of Honour", "荣誉军团司令", 0),
    ("Émile Picard Medal", "埃米尔·皮卡德奖章", 1953),
    ("Concours général", "全国会考奖", 0),
]

INSTITUTIONS = [
    ("École Polytechnique", "education", 1904, 1907),
    ("Mines ParisTech", "education", 1910, 1913),
    ("University of Paris", "education", None, None),
    ("École des Mines", "employment", 1913, 1920),
    ("École Polytechnique", "employment", 1920, 1959),
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
    cur.execute("SELECT id FROM occupations WHERE name_en='engineer'")
    eng_id = cur.fetchone()

    # ---------- 1. Lévy 本人补齐 ----------
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
            "保罗·列维",
            '["Paul Pierre Lévy","Lévy 过程的命名者","稳定分布的引入者","鞅理论的先驱"]',
            "French mathematician (1886–1971)",
            "1886-09-15",
            "1971-12-15",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if eng_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, eng_id[0]))
    print(f"Lévy id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    cur.execute("SELECT id FROM countries WHERE name_en='France'")
    fr = cur.fetchone()
    if fr:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, fr[0]))
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
            if name in ("Jacques Hadamard", "Vito Volterra"):
                f, t = pid, pid0  # 导师 → Lévy
            else:
                f, t = pid0, pid  # Lévy → 学生
        elif rel == "parent-child":
            f, t = pid0, pid  # Lévy → 女儿/女婿
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Lévy-presentation')",
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

    print("\n=== 校验：Paul Lévy 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Paul Lévy' OR b.name_en='Paul Lévy'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
