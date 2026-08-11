#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Andrey Markov 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Andrey_Markov/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Andrey Markov"
QID = "Q176659"

RELATIONS = [
    # 老师（有向：导师 → Markov）
    ("advisor-student", "Pafnuty Chebyshev", "圣彼得堡大学导师；1896 接替其科学院正院士席位"),
    # 学生（有向：Markov → 学生）
    ("advisor-student", "Abram Besicovitch", "学生，几乎周期函数与几何测度论"),
    ("advisor-student", "Alexander Friedmann", "学生，宇宙学，Friedmann 方程"),
    ("advisor-student", "Veniamin Kagan", "学生，微分几何与张量分析"),
    ("advisor-student", "Jacob Tamarkin", "学生，泛函分析"),
    ("advisor-student", "J. V. Uspensky", "学生，数论与概率论"),
    ("advisor-student", "Georgy Voronoy", "学生，Voronoi 图与代数数论"),
    ("advisor-student", "Nikolai Günther", "学生，数学物理"),
    ("advisor-student", "Vsevolod Ivanovich Romanovsky", "学生，马尔可夫链统计"),
    # 家族
    ("sibling", "Vladimir Andreyevich Markov", "弟（1871–1897），Markov 兄弟不等式共同证明者"),
    ("parent-child", "Andrey Markov Jr.", "子（1903–1979），构造数学与递归函数论"),
    # 同事（无向）
    ("colleague", "Viktor Bunyakovsky", "1890 其逝世后 Markov 递补科学院特任院士"),
]

MARKER = "[Markov-材料待展开] "

FIELDS = [
    ("probability theory", "概率论", 0),
    ("stochastic process", "随机过程", 1),
    ("number theory", "数论", 2),
    ("mathematical analysis", "数学分析", 3),
]

# 全部奖项收录（政治/荣誉勋章）
AWARDS = [
    ("Order of Saint Anna, 2nd class", "圣安娜勋章二级", 0),
    ("Order of Saint Stanislaus, 2nd class", "圣斯坦尼斯劳斯勋章二级", 0),
]

INSTITUTIONS = [
    ("Saint Petersburg State University", "education", 1874, 1884),
    ("Saint Petersburg State University", "employment", 1880, 1905),
    ("Saint Petersburg Academy of Sciences", "employment", 1886, 1922),
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
    cur.execute("SELECT id FROM occupations WHERE name_en='statistician'")
    stat_id = cur.fetchone()

    # ---------- 1. Markov 本人补齐 ----------
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
            "安德雷·马尔可夫",
            '["Andrei Markov","A.A. Markov","Markoff","马尔可夫链的创立者"]',
            "Russian mathematician (1856–1922)",
            "1856-06-14",
            "1922-07-20",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if stat_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, stat_id[0]))
    print(f"Markov id={pid0} 已补齐 people 字段（has_social_data=1）")

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
        # 同机构同 relation 已有则跳过（主键约束），避免覆盖
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
    cur.execute("SELECT id FROM countries WHERE name_en='Russian Empire'")
    re_ = cur.fetchone()
    if re_:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, re_[0]))
    cur.execute("SELECT id FROM countries WHERE name_en='Russian Soviet Federative Socialist Republic'")
    rs = cur.fetchone()
    if rs:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, rs[0]))
    print("  国籍关联完成")

    # ---------- 6. 社会关系 ----------
    # 注册 sibling 关系类型（无则新增）
    cur.execute("SELECT relation_key FROM relation_types WHERE relation_key='sibling'")
    if not cur.fetchone():
        cur.execute("INSERT INTO relation_types(relation_key, name_zh, directed) VALUES ('sibling','兄弟姐妹',0)")
        print("  + 新建关系类型: sibling（兄弟姐妹）")

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
            if name == "Pafnuty Chebyshev":
                f, t = pid, pid0  # 导师 → Markov
            else:
                f, t = pid0, pid  # Markov → 学生
        elif rel == "parent-child":
            f, t = pid0, pid  # Markov → 儿子
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Markov-presentation')",
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

    print("\n=== 校验：Andrey Markov 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Andrey Markov' OR b.name_en='Andrey Markov'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
