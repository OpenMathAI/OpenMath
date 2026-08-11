#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Henri Cartan 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Henri_Cartan/（Wikipedia 存档）
注意：父 Élie Cartan(15) 与子 Henri Cartan(69) 各自独立。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Henri Cartan"
QID = "Q164405"

RELATIONS = [
    # 导师（有向：导师 → Cartan）
    ("advisor-student", "Paul Montel", "博士导师"),
    # 学生（有向：Cartan → 学生）
    ("advisor-student", "J.-P. Serre", "学生，菲尔兹奖得主"),  # 库中名 J.-P. Serre
    ("advisor-student", "René Thom", "学生，菲尔兹奖得主"),
    ("advisor-student", "Bernard Morin", "学生，曲面内翻"),
    ("advisor-student", "Joséphine Guidy Wandja", "学生，首位获数学博士学位的非洲女性"),
    ("advisor-student", "Pierre Cartier", "学生，Bourbaki 成员"),
    ("advisor-student", "Pierre Dolbeault", "学生，Dolbeault 上同调"),
    ("advisor-student", "Jean-Paul Benzécri", "学生，对应分析"),
    ("advisor-student", "Jean Cerf", "学生，微分拓扑"),
    ("advisor-student", "Jacques Deny", "学生，位势论"),
    ("advisor-student", "Adrien Douady", "学生，复动力学"),
    ("advisor-student", "Roger Godement", "学生，Godement 分解"),
    ("advisor-student", "Max Karoubi", "学生，K 理论"),
    ("advisor-student", "Jean-Louis Koszul", "学生，Koszul 复形"),
    ("advisor-student", "François Bruhat", "学生，Bruhat 分解"),
    ("advisor-student", "Jean-Pierre Ramis", "学生，渐近分析"),
    # 研讨班影响/合作（无向）
    ("collaborator", "Alexander Grothendieck", "巴黎研讨班影响，拓扑与代数几何"),
    ("collaborator", "Armand Borel", "巴黎研讨班影响"),
    ("collaborator", "Frank Adams", "巴黎研讨班影响，谱序列"),
    ("collaborator", "Samuel Eilenberg", "合著《Homological Algebra》(1956)"),
    ("collaborator", "André Weil", "Bourbaki 共同创始人，通信集 1928-1991"),
    ("collaborator", "Heinrich Behnke", "法德数学长期合作"),
    ("collaborator", "Peter Thullen", "法德数学合作"),
    # 家族（父→子有向；其余无向）
    ("parent-child", "Élie Cartan", "父亲，李群大师"),  # 父 → 子
    ("parent-child", "Anna Cartan", "姑母，数学家"),
    ("parent-child", "Jean Cartan", "弟弟，作曲家"),
    ("parent-child", "Louis Cartan", "弟弟，物理学家"),
    ("parent-child", "Hélène Cartan", "妹妹，数学家"),
    ("parent-child", "Pierre Weiss", "岳父，物理学家"),
]

MARKER = "[Cartan-材料待展开] "

FIELDS = [
    ("algebraic topology", "代数拓扑", 0),
    ("homological algebra", "同调代数", 1),
    ("complex analysis", "复分析", 2),
    ("mathematical analysis", "数学分析", 3),
]

# 全部奖项收录
AWARDS = [
    ("Wolf Prize in Mathematics", "沃尔夫数学奖", 1980),
    ("Émile Picard Medal", "埃米尔·皮卡德奖章", 1959),
    ("CNRS Gold medal", "法国国家科研中心金质奖章", 1976),
    ("Heinz R. Pagels Human Rights of Scientists Award", "海因茨·帕格尔斯科学家人权奖", 1989),
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士", 1971),
    ("Cours Peccot", "佩科课程奖", 1932),
    ("Grand Officer of the National Order of Merit", "国家功绩勋章大军官", 0),
]

INSTITUTIONS = [
    ("Lycée Hoche", "education", None, None),
    ("École Normale Supérieure", "education", 1923, 1926),
    ("University of Lille", "employment", 1929, 1931),
    ("University of Strasbourg", "employment", 1931, 1939),
    ("University of Paris", "employment", 1940, 1969),
    ("Paris-Sud University", "employment", 1969, 1975),
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

    # ---------- 1. Cartan 本人补齐 ----------
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
            "亨利·嘉当",
            '["Henri Paul Cartan","小嘉当","Bourbaki 核心成员","Cartan 定理 A 和 B"]',
            "French mathematician (1904–2008)",
            "1904-07-08",
            "2008-08-13",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Cartan id={pid0} 已补齐 people 字段（has_social_data=1）")

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
            if name == "Paul Montel":
                f, t = pid, pid0  # 导师 → Cartan
            else:
                f, t = pid0, pid  # Cartan → 学生
        elif rel == "parent-child":
            if name == "Élie Cartan":
                f, t = pid, pid0  # 父 → 子
            elif name == "Pierre Weiss":
                f, t = pid, pid0  # 岳父 → 女婿
            else:
                f, t = sorted([pid0, pid])
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Cartan-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Henri Cartan 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Henri Cartan' OR b.name_en='Henri Cartan'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
