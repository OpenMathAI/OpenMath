#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Jacques Hadamard 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Jacques_Hadamard/（Wikipedia 存档）
注意：has_biography=1（已立传），本次仅补社会关系/研究领域。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Jacques Hadamard"
QID = "Q164425"

RELATIONS = [
    # 导师（有向：导师 → Hadamard）
    ("advisor-student", "Charles Émile Picard", "博士导师"),
    ("advisor-student", "Jules Tannery", "博士导师"),
    # 老师（有向：老师 → Hadamard）
    ("advisor-student", "Charles Hermite", "ENS 老师"),
    ("advisor-student", "Jean Gaston Darboux", "ENS 老师"),
    ("advisor-student", "Paul Appell", "ENS 老师"),
    ("advisor-student", "Édouard Goursat", "ENS 老师"),
    ("advisor-student", "Paul Tannery", "ENS 老师"),
    # 学生（有向：Hadamard → 学生）
    ("advisor-student", "Maurice René Fréchet", "学生，泛函分析之父"),
    ("advisor-student", "Paul Lévy", "学生，概率论大师"),
    ("advisor-student", "Szolem Mandelbrojt", "学生，复分析"),
    ("advisor-student", "André Weil", "学生，Bourbaki 核心"),
    ("advisor-student", "Marc Krasner", "学生，p 进分析"),
    ("advisor-student", "Pierre Massé", "学生"),
    ("advisor-student", "Georges Bouligand", "学生，分析"),
    ("advisor-student", "Maurice Janet", "学生"),
    ("advisor-student", "Alexander Weinstein", "学生"),
    ("advisor-student", "Pierre Boutroux", "学生，数学史"),
    # 同事/荣誉共同体（无向）
    ("colleague", "Henri Poincaré", "法国科学院院士继任者（1916，接 Poincaré 席位）"),
    ("colleague", "Camille Jordan", "巴黎中央理工前任分析讲席"),
    ("co-honored", "Charles Jean de la Vallée-Poussin", "1896 独立证明素数定理"),
]

MARKER = "[Hadamard-材料待展开] "

FIELDS = [
    ("number theory", "数论", 0),
    ("complex analysis", "复分析", 1),
    ("differential geometry", "微分几何", 2),
    ("partial differential equation", "偏微分方程", 3),
    ("functional analysis", "泛函分析", 4),
]

# 全部奖项收录
AWARDS = [
    ("CNRS Gold medal", "法国国家科研中心金质奖章", 1956),
    ("Feltrinelli Prize", "费尔特里内利奖", 0),
    ("Poncelet Prize", "庞斯莱奖", 1898),
    ("Grand Cross of the Legion of Honour", "荣誉军团大十字勋章", 0),
    ("Grand Officer of the Legion of Honour", "荣誉军团大军官", 0),
    ("Commander of the Legion of Honour", "荣誉军团指挥官", 0),
    ("Officer of the Legion of Honour", "荣誉军团军官", 0),
    ("honorary doctor of the Hebrew University of Jerusalem", "耶路撒冷希伯来大学名誉博士", 0),
    ("Grand prix des sciences mathématiques", "数学科学大奖", 1892),
    ("Concours général", "全国会考奖", 1884),
    ("Silliman Memorial Lectures", "西利曼纪念讲座", 0),
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士", 0),
    ("Estrade-Delcros award", "埃斯特拉德-德尔克罗奖", 0),
    ("Petit d'Ormoy, Carriere, Thebault Award", "小德奥尔莫瓦奖", 0),
    ("Bordin Prize", "博尔丹奖", 1896),
]

INSTITUTIONS = [
    ("Lycée Charlemagne", "education", None, None),
    ("Lycée Louis-le-Grand", "education", None, None),
    ("École Normale Supérieure", "education", 1884, None),
    ("University of Paris", "education", None, None),
    ("University of Bordeaux", "employment", 1893, 1897),
    ("Collège de France", "employment", 1909, None),
    ("École Polytechnique", "employment", 1912, None),
    ("École Centrale Paris", "employment", 1920, None),
    ("Columbia University", "employment", 1941, 1944),
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

    # ---------- 1. Hadamard 本人补齐 ----------
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
        "UPDATE people SET qid=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            QID,
            '["Jacques Salomon Hadamard","素数定理证明者","Hadamard 矩阵","适定问题"]',
            "French mathematician (1865–1963)",
            "1865-12-08",
            "1963-10-17",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Hadamard id={pid0} 已补齐 people 字段（has_social_data=1，has_biography 保持）")

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
            if name in ("Charles Émile Picard", "Jules Tannery", "Charles Hermite",
                        "Jean Gaston Darboux", "Paul Appell", "Édouard Goursat", "Paul Tannery"):
                f, t = pid, pid0  # 导师/老师 → Hadamard
            else:
                f, t = pid0, pid  # Hadamard → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Hadamard-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Hadamard 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Jacques Hadamard' OR b.name_en='Jacques Hadamard'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
