#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Lev Pontryagin 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Lev_Pontryagin/（Wikipedia 存档）

奖项全部收录原则（21.2.4）：含苏联勋章/政治奖，年份缺失置 0 + 年份待查。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Lev Pontryagin"
QID = "Q451319"

RELATIONS = [
    # 老师（有向：导师 → Pontryagin）
    ("advisor-student", "Pavel Alexandrov", "莫斯科大学博士导师；Alexandrov 学派传承"),
    # 学生（有向：Pontryagin → 学生）
    ("advisor-student", "Vladimir Boltyansky", "学生，最优控制与几何学家"),
    ("advisor-student", "Mikhail Postnikov", "学生，同伦论与代数拓扑大家"),
    ("advisor-student", "Revaz Gamkrelidze", "学生，控制论与数学史家"),
    ("advisor-student", "Dmitri Anosov", "学生，动力系统与遍历理论"),
    ("advisor-student", "Mikhail Zelikin", "学生，最优控制理论"),
    ("advisor-student", "Vladimir Rokhlin", "学生，拓扑学与测度论"),
    # 合作者（无向）：配边理论共同奠基
    ("collaborator", "René Thom", "配边理论共同奠基人（framed cobordism ≈ stable homotopy）"),
    # 争议（无向）：反犹指控对象 Margulis
    ("controversy", "Grigory Margulis", "1978 反对其获 Fields 奖（反犹指控）；Margulis 被苏联拒签未能参会"),
]

MARKER = "[Pontryagin-材料待展开] "

FIELDS = [
    ("algebraic topology", "代数拓扑", 0),
    ("optimal control", "最优控制", 1),
    ("topology", "拓扑学", 2),
    ("differential topology", "微分拓扑", 3),
]

# 奖项全部收录：(name_en, year)；年份不确定的置 0
AWARDS = [
    ("Stalin Prize", 1941),
    ("USSR State Prize", 0),
    ("Order of Lenin", 0),
    ("Hero of Socialist Labour", 1969),
    ("Order of the October Revolution", 0),
    ("Order of the Red Banner of Labour", 0),
    ("Order of the Badge of Honour", 0),
    ("Lenin Prize", 1962),
    ("Lobachevsky Prize", 0),
]

INSTITUTIONS = [
    ("Lomonosov Moscow State University", "education", 1925, 1929),
    ("Lomonosov Moscow State University", "employment", 1929, 1934),
    ("Steklov Institute of Mathematics", "employment", 1934, 1988),
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

    # ---------- 1. Pontryagin 本人补齐 ----------
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
            "列夫·庞特里亚金",
            '["Pontriagin","Pontrjagin","Leon Pontryagin","14 岁失明的苏联拓扑学大师"]',
            "Soviet mathematician (1908–1988)",
            "1908-09-03",
            "1988-05-03",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Pontryagin id={pid0} 已补齐 people 字段（has_social_data=1）")

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

    # ---------- 3. 奖项（全部收录）----------
    for a_en, year in AWARDS:
        cur.execute("SELECT id FROM awards WHERE name_en=%s", (a_en,))
        arow = cur.fetchone()
        if not arow:
            cur.execute("INSERT INTO awards(name_en) VALUES (%s)", (a_en,))
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
    print("  奖项关联完成（9 项全部收录）")

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
            (pid0, iid, rel, sy, ey),
        )
    print("  机构关联完成")

    # ---------- 5. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='Soviet Union'")
    su = cur.fetchone()
    if su:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, su[0]))
    cur.execute("SELECT id FROM countries WHERE name_en='Russian Empire'")
    re_ = cur.fetchone()
    if re_:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, re_[0]))
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
            if name == "Pavel Alexandrov":
                f, t = pid, pid0  # 导师 → Pontryagin
            else:
                f, t = pid0, pid  # Pontryagin → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Pontryagin-presentation')",
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

    print("\n=== 校验：Lev Pontryagin 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Lev Pontryagin' OR b.name_en='Lev Pontryagin'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
