#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Constantin Carathéodory 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Constantin_Carathéodory/（Wikipedia 存档）
注意：生卒以正文 1873-09-13/1950-02-02 为准。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Constantin Carathéodory"
QID = "Q65332"

RELATIONS = [
    # 导师（有向：导师 → Carathéodory）
    ("advisor-student", "Hermann Minkowski", "博士导师（Göttingen 1904）"),
    # 学生（有向：Carathéodory → 学生）
    ("advisor-student", "Hans Rademacher", "学生，解析数论与分析"),
    ("advisor-student", "Paul Finsler", "学生，Finsler 空间"),
    ("advisor-student", "Ernst Peschl", "学生，复分析"),
    ("advisor-student", "Wladimir Seidel", "学生，函数论"),
    ("advisor-student", "Nazım Terzioğlu", "学生，土耳其数学家"),
    ("advisor-student", "Xu Ruiyun", "学生，中国数学家"),
    ("advisor-student", "Georg Aumann", "学生"),
    ("advisor-student", "Hermann Boerner", "学生"),
    ("advisor-student", "Erich Bessel-Hagen", "学生，数论/几何"),
    ("advisor-student", "Dimitrios Kappos", "学生，希腊数学家"),
    ("advisor-student", "Christos Papakyriakopoulos", "学生（雅典，1943 拓扑学博士）"),
    # 同事/联系（无向）
    ("colleague", "David Hilbert", "Göttingen 同事"),
    ("colleague", "Felix Klein", "1913 接任其 Göttingen 讲席"),
    ("colleague", "Albert Einstein", "1917 就 Hamilton–Jacobi 方程/正则变换向其求教"),
    ("colleague", "Edmund Landau", "德国学术圈联系，Landau/Schwarz 激发其复分析兴趣"),
    ("colleague", "Hermann Amandus Schwarz", "德国学术圈联系"),
    ("colleague", "Lipót Fejér", "匈牙利数学家，密切学术交往"),
    ("colleague", "Oskar Perron", "二战期间巴伐利亚科学院密切同事"),
    ("colleague", "Heinrich Tietze", "二战期间巴伐利亚科学院密切同事"),
]

MARKER = "[Carathéodory-材料待展开] "

FIELDS = [
    ("calculus of variations", "变分法", 0),
    ("measure theory", "测度论", 1),
    ("complex analysis", "复分析", 2),
    ("mathematical analysis", "数学分析", 3),
    ("convex geometry", "凸几何", 4),
]

AWARDS = [
    ("member of the Prussian Academy of Sciences", "普鲁士科学院院士", 1919),
]

INSTITUTIONS = [
    ("Technische Universität Berlin", "education", 1900, None),
    ("University of Göttingen", "education", 1900, 1905),
    ("University of Bonn", "employment", 1908, 1909),
    ("Leibniz University Hannover", "employment", 1909, 1910),
    ("University of Wrocław", "employment", 1910, 1913),
    ("University of Göttingen", "professor", 1913, 1919),  # 接 Klein 讲席
    ("Humboldt University of Berlin", "employment", 1919, 1920),
    ("Ionian University of Smyrna", "employment", 1920, 1922),  # 院长
    ("National and Kapodistrian University of Athens", "employment", 1922, 1924),
    ("Ludwig Maximilian University of Munich", "employment", 1924, 1938),
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

    # ---------- 1. Carathéodory 本人补齐 ----------
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
            "康斯坦丁·卡拉泰奥多里",
            '["Konstantinos Caratheodori","Carathéodory 定理","公理化热力学","变分法皇家大道"]',
            "Greek mathematician (1873–1950)",
            "1873-09-13",
            "1950-02-02",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Carathéodory id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("Greece", "German Empire")):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (country,))
        cid = cur.fetchone()
        if not cid:
            cur.execute("INSERT IGNORE INTO countries(name_en, name_zh, is_current) VALUES (%s,%s,1)",
                        (country, "希腊" if country == "Greece" else "德意志帝国"))
            cid = cur.lastrowid
            print(f"  + 新建国家: {country} (id={cid})")
        else:
            cid = cid[0]
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                    (pid0, cid, idx))
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
            if name == "Hermann Minkowski":
                f, t = pid, pid0  # 导师 → Carathéodory
            else:
                f, t = pid0, pid  # Carathéodory → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Carathéodory-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Carathéodory 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Constantin Carathéodory' OR b.name_en='Constantin Carathéodory'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
