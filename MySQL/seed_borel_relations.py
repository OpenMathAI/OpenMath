#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Émile Borel 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Émile_Borel/（Wikipedia 存档）
注意：id=402 Armand Borel 是另一位数学家，勿混淆/合并。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Émile Borel"
QID = "Q154356"

RELATIONS = [
    # 导师（有向：导师 → Borel）
    ("advisor-student", "Jean Gaston Darboux", "博士导师"),
    # 学生（有向：Borel → 学生）
    ("advisor-student", "Henri Lebesgue", "学生，测度论与积分理论"),
    ("advisor-student", "Paul Montel", "学生，复分析"),
    ("advisor-student", "Georges Valiron", "学生，整函数理论"),
    ("advisor-student", "Robert Deltheil", "学生，概率与几何"),
    ("advisor-student", "Paul Dienes", "学生，级数理论"),
    ("advisor-student", "Ervand Kogbetliantz", "学生，级数与算法"),
    ("advisor-student", "Tadeusz Ważewski", "学生，微分方程"),
    ("advisor-student", "Ernest Esclangon", "学生，天文学家、弹道学"),
    ("advisor-student", "René Gosse", "学生"),
    ("advisor-student", "Henri Milloux", "学生，整函数理论"),
    ("advisor-student", "Francis Perrin", "学生，物理学家"),
    ("advisor-student", "René Risser", "学生，数理统计"),
    ("advisor-student", "Rokuro Yamamoto", "学生，日本数学家"),
    # 合作者/先驱同伴（无向）
    ("collaborator", "René-Louis Baire", "测度论先驱三巨头之一"),
    ("collaborator", "Henri Lebesgue", "测度论先驱三巨头之一"),
    # 争议（无向）
    ("controversy", "John von Neumann", "博弈论优先权争议（1953 Econometrica）"),
    # 同事（无向）
    ("colleague", "Paul Painlevé", "政治同僚，1925 内阁总理"),
    # 家族
    ("parent-child", "Paul Appell", "岳父，巴黎大学同事"),
    ("spouse", "Marguerite Borel", "妻（1901 结婚），笔名 Camille Marbo 的小说家"),
]

MARKER = "[Borel-材料待展开] "

FIELDS = [
    ("measure theory", "测度论", 0),
    ("probability theory", "概率论", 1),
    ("game theory", "博弈论", 2),
    ("complex analysis", "复分析", 3),
]

# 全部奖项收录
AWARDS = [
    ("Grand Cross of the Legion of Honour", "荣誉军团大十字勋章", 0),
    ("Croix de guerre 1939–1945", "1939–1945 战争十字勋章", 0),
    ("Resistance Medal", "抵抗勋章", 1950),
    ("CNRS Gold medal", "法国国家科研中心金质奖章", 0),
    ("Poncelet Prize", "庞斯莱奖", 0),
    ("Grand prix des sciences mathématiques", "数学科学大奖", 0),
    ("Cours Peccot", "佩科课程奖", 0),
    ("Honorary Member of the World Esperanto Association", "世界语协会名誉会员", 0),
    ("honorary doctor of Sofia University", "索菲亚大学名誉博士", 0),
]

INSTITUTIONS = [
    ("Lycée Louis-le-Grand", "education", None, None),
    ("École Normale Supérieure", "education", 1889, 1892),
    ("University of Lille", "employment", 1893, 1897),
    ("École Normale Supérieure", "employment", 1897, 1941),
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

    # ---------- 1. Borel 本人补齐 ----------
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
            "埃米尔·博雷尔",
            '["Félix Édouard Justin Émile Borel","Borel 集命名者","无穷猴子定理","博弈论首创"]',
            "French mathematician and politician (1871–1956)",
            "1871-01-07",
            "1956-02-03",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Borel id={pid0} 已补齐 people 字段（has_social_data=1）")

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
            if name == "Jean Gaston Darboux":
                f, t = pid, pid0  # 导师 → Borel
            else:
                f, t = pid0, pid  # Borel → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 岳父 → Borel
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Borel-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Borel 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Émile Borel' OR b.name_en='Émile Borel'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
