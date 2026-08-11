#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Émile Picard 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Émile_Picard/（Wikipedia 存档）
同时合并重复人物：id=744 (Charles Émile Picard) → id=78 (Émile Picard)。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Émile Picard"
DUP_NAME = "Charles Émile Picard"
QID = "Q286375"

RELATIONS = [
    # 导师（有向：导师 → Picard）
    ("advisor-student", "Jean Gaston Darboux", "博士导师（1877）"),
    # 学生（有向：Picard → 学生）
    ("advisor-student", "Jacques Hadamard", "学生，素数定理证明者"),
    ("advisor-student", "André Weil", "学生，Bourbaki 核心"),
    ("advisor-student", "Gaston Julia", "学生，Julia 集"),
    ("advisor-student", "Paul Painlevé", "学生，后任法国总理"),
    ("advisor-student", "Sergei Bernstein", "学生，Bernstein 多项式"),
    ("advisor-student", "Stanisław Zaremba", "学生"),
    ("advisor-student", "René-Louis Baire", "学生，Baire 范畴定理"),
    ("advisor-student", "Simion Stoilow", "学生"),
    ("advisor-student", "Ernest Vessiot", "学生，Picard–Vessiot 理论"),
    ("advisor-student", "Henri Villat", "学生"),
    ("advisor-student", "Traian Lalescu", "学生，积分方程"),
    ("advisor-student", "Mihailo Petrović", "学生"),
    ("advisor-student", "Gheorghe Călugăreanu", "学生"),
    ("advisor-student", "Philippe Le Corbeiller", "学生"),
    ("advisor-student", "Paul Dubreil", "学生，代数"),
    # 家族
    ("parent-child", "Charles Hermite", "岳父，大数学家"),
    ("spouse", "Marie Picard", "妻（1881 结婚，Charles Hermite 之女）"),
    # 同事/相关
    ("colleague", "Henri Poincaré", "同时代法国数学家，函数论大师"),
    ("advisor-student", "Louis Couturat", "1891-92 随其学习积分学并详记笔记"),
]

MARKER = "[Picard-材料待展开] "

FIELDS = [
    ("complex analysis", "复分析", 0),
    ("mathematical analysis", "数学分析", 1),
    ("algebraic geometry", "代数几何", 2),
    ("differential equation", "常微分方程", 3),
]

# 全部奖项收录
AWARDS = [
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士", 1909),
    ("Poncelet Prize", "庞斯莱奖", 1886),
    ("Grand Cross of the Legion of Honour", "荣誉军团大十字勋章", 0),
    ("Grand prix des sciences mathématiques", "数学科学大奖", 0),
    ("Fellow of the American Academy of Arts and Sciences", "美国艺术与科学院院士", 0),
    ("Jean Reynaud Prize", "让·雷诺奖", 0),
]

INSTITUTIONS = [
    ("Lycée Henri-IV", "education", None, None),
    ("Lycée Michelet, Vanves", "education", None, None),
    ("École Normale Supérieure", "education", 1874, None),
    ("University of Toulouse", "employment", None, None),
    ("University of Paris", "employment", None, None),
    ("École Centrale Paris", "employment", None, None),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def merge_dup(cur, main_id: int, dup_id: int):
    """合并重复人物 dup_id → main_id（幂等，跳过 id 字段避免主键冲突）。"""
    for tbl in ("person_relation", "award_laureate", "person_occupation",
                "person_field", "person_institution", "person_nationality"):
        if tbl == "person_relation":
            cur.execute("SELECT * FROM person_relation WHERE from_id=%s OR to_id=%s", (dup_id, dup_id))
        else:
            cur.execute(f"SELECT * FROM {tbl} WHERE person_id=%s", (dup_id,))
        rows = cur.fetchall()
        if not rows:
            continue
        cur.execute("SHOW COLUMNS FROM " + tbl)
        desc = [r[0] for r in cur.fetchall()]
        for row in rows:
            data = dict(zip(desc, row))
            if tbl == "person_relation":
                data["from_id"] = main_id if data["from_id"] == dup_id else data["from_id"]
                data["to_id"] = main_id if data["to_id"] == dup_id else data["to_id"]
            else:
                data["person_id"] = main_id
            d = {k: v for k, v in data.items() if k != "id" and v is not None}
            cols_s = ", ".join(f"`{k}`" for k in d)
            ph = ", ".join("%s" for _ in d)
            try:
                cur.execute(f"INSERT IGNORE INTO {tbl} ({cols_s}) VALUES ({ph})", list(d.values()))
            except Exception as e:
                print(f"  ! {tbl} 迁移跳过: {e}")
    cur.execute("DELETE FROM people WHERE id=%s", (dup_id,))
    print(f"已合并: id={dup_id} ({DUP_NAME}) → id={main_id} ({NAME})")


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    # ---------- 0. 合并重复人物 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    main_row = cur.fetchone()
    cur.execute("SELECT id FROM people WHERE name_en=%s", (DUP_NAME,))
    dup_row = cur.fetchone()
    if main_row and dup_row:
        merge_dup(cur, main_row[0], dup_row[0])
    pid0 = main_row[0] if main_row else None
    if pid0 is None:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',0,%s)",
            (NAME, QID),
        )
        pid0 = cur.lastrowid

    # ---------- 1. Picard 本人补齐 ----------
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            QID,
            "埃米尔·皮卡",
            '["Charles Émile Picard","皮卡定理","Picard 群","Picard–Vessiot 理论"]',
            "French mathematician (1856–1941)",
            "1856-07-24",
            "1941-12-11",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Picard id={pid0} 已补齐 people 字段（has_social_data=1）")

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
                f, t = pid, pid0  # 导师 → Picard
            else:
                f, t = pid0, pid  # Picard → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 岳父 → Picard
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Picard-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Picard 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Émile Picard' OR b.name_en='Émile Picard'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
