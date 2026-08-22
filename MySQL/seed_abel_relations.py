#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Niels Henrik Abel 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/presentations/19th_century/pages/Niels_Henrik_Abel/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Niels Henrik Abel"
QID = "Q124115"

RELATIONS = [
    # 导师（有向：导师 → Abel）
    ("advisor-student", "Bernt Michael Holmboe", "大教堂学校数学教师，终身支持者"),
    # 学术贵人 / 同行（无向）
    ("colleague", "August Leopold Crelle", "柏林结识，《Crelle's Journal》创刊者，创刊年刊其 7 文"),
    ("colleague", "Augustin-Louis Cauchy", "巴黎提交代数微分加法定理，被其搁置遗忘"),
    ("colleague", "Carl Friedrich Gauss", "五次方程论文寄送对象（被其未看即弃）"),
    ("rival", "Carl Gustav Jacob Jacobi", "椭圆函数双周期性的竞争者（1828 竞相发表）"),
    ("colleague", "Adrien-Marie Legendre", "赏识者，称其椭圆函数工作「比青铜更持久」"),
    ("colleague", "Ludwig Sylow", "遗作全集编者（1881，与 Lie 合作）"),
    ("colleague", "Sophus Lie", "遗作全集编者（1881，与 Sylow 合作）"),
    # 未婚妻
    ("spouse", "Christine Kemp", "未婚妻（1824 年订婚，未及成婚）"),
]

MARKER = "[Abel-材料待展开] "

FIELDS = [
    ("group theory", "群论", 0),
    ("elliptic function", "椭圆函数", 1),
    ("abelian group", "阿贝尔群", 2),
    ("algebraic equation", "代数方程", 3),
    ("calculus", "微积分", 4),
]

AWARDS = [
    ("Grand prix des sciences mathématiques", "法国科学院数学大奖", 1830),
]

INSTITUTIONS = [
    ("Oslo Cathedral School", "education", 1815, None),
    ("University of Oslo", "education", 1821, 1822),
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

    # ---------- 1. Abel 本人补齐 ----------
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
            "尼尔斯·亨里克·阿贝尔",
            '["Niels Henrik Abel","阿贝尔","阿贝尔群","Abel–Ruffini 定理"]',
            "Norwegian mathematician (1802–1829)",
            "1802-08-05",
            "1829-04-06",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Abel id={pid0} 已补齐 people 字段（has_social_data=1）")

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
        note = "追授，与 Carl Gustav Jacob Jacobi 分享" if year == 1830 else None
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, `year`, share_type, source, note) "
            "VALUES (%s,%s,%s,'共享','Wikipedia',%s)",
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
    for idx, country in enumerate(("Norway",)):
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
            if name == "Bernt Michael Holmboe":
                f, t = pid, pid0  # 导师 → Abel
            else:
                f, t = pid0, pid
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Abel-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")

    print("\n=== 校验：Abel 社会关系 ===")
    cur.execute(
        "SELECT a.name_en, rt.name_zh, b.name_en, pr.note "
        "FROM person_relation pr "
        "JOIN people a ON a.id=pr.from_id "
        "JOIN people b ON b.id=pr.to_id "
        "JOIN relation_types rt ON rt.relation_key=pr.relation_type "
        "WHERE a.name_en=%s OR b.name_en=%s",
        (NAME, NAME),
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:50]}")

    conn.close()


if __name__ == "__main__":
    main()
