#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Felix Klein 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Felix_Klein/（Wikipedia 存档）
注意：has_biography=1（已立传），本次仅补社会关系/研究领域。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Felix Klein"
QID = "Q76641"

RELATIONS = [
    # 导师（有向：导师 → Klein）
    ("advisor-student", "Julius Plücker", "博士导师（波恩 1868）"),
    ("advisor-student", "Rudolf Lipschitz", "博士导师"),
    # 学术引路人/合作者（无向）
    ("colleague", "Alfred Clebsch", "赏识者/引路人，称其将成为当时最伟大数学家"),
    ("collaborator", "Alexander von Brill", "慕尼黑合教（1875-1880）"),
    ("colleague", "Eduard Study", "莱比锡同事"),
    ("colleague", "Friedrich Engel", "莱比锡同事"),
    # 学生（有向：Klein → 学生）
    ("advisor-student", "Adolf Hurwitz", "学生，数论/复分析"),
    ("advisor-student", "Ludwig Bieberbach", "学生，几何/复分析"),
    ("advisor-student", "Ferdinand von Lindemann", "学生，π 超越性证明"),
    ("advisor-student", "Alexander Ostrowski", "学生，复分析/数值分析"),
    ("advisor-student", "Grace Chisholm Young", "学生，哥廷根第一位女性数学博士（1896）"),
    ("advisor-student", "Maxime Bôcher", "学生，分析/代数"),
    ("advisor-student", "Frank Nelson Cole", "学生，数论（美国数学会主席）"),
    ("advisor-student", "Philipp Furtwängler", "学生，代数数论"),
    ("advisor-student", "Edward Kasner", "学生，几何（googol 命名者）"),
    ("advisor-student", "Walther von Dyck", "学生，群论/几何"),
    ("advisor-student", "Robert Fricke", "学生，模函数"),
    ("advisor-student", "Carl Runge", "学生，数值分析（Runge-Kutta）"),
    ("advisor-student", "Henry Burchard Fine", "学生，普林斯顿数学奠基者"),
    ("advisor-student", "Oskar Bolza", "学生，变分法"),
    ("advisor-student", "Axel Harnack", "学生，实分析"),
    # 同事/被招募者（无向）
    ("colleague", "David Hilbert", "1895 招募至哥廷根"),
    ("colleague", "Emmy Noether", "1915 与 Hilbert 共同邀请至哥廷根"),
    ("colleague", "Max Planck", "慕尼黑时期听课生（后物理学家）"),
    ("colleague", "Luigi Bianchi", "慕尼黑时期影响的意大利学生"),
    ("colleague", "Gregorio Ricci-Curbastro", "慕尼黑时期影响的意大利学生（张量分析）"),
    # 家族
    ("spouse", "Anne Hegel", "妻（1875），哲学家黑格尔之孙女"),
]

MARKER = "[Klein-材料待展开] "

FIELDS = [
    ("geometry", "几何学", 0),
    ("group theory", "群论", 1),
    ("differential geometry", "微分几何", 2),
    ("complex analysis", "复分析", 3),
    ("mathematical education", "数学教育", 4),
]

AWARDS = [
    ("De Morgan Medal", "德摩根奖章", 1893),
    ("Copley Medal", "科普利奖章", 1912),
    ("Ackermann–Teubner Memorial Award", "阿克曼-托伊布纳纪念奖", 1914),
    ("Pour le Mérite for Sciences and Arts", "功勋勋章（科学与艺术）", 0),
    ("Bavarian Maximilian Order for Science and Art", "巴伐利亚科学与艺术马克西米利安勋章", 0),
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士", 1885),
]

INSTITUTIONS = [
    ("University of Bonn", "education", 1865, 1868),
    ("Humboldt University of Berlin", "education", None, None),
    ("University of Göttingen", "employment", 1871, 1872),
    ("University of Erlangen-Nuremberg", "employment", 1872, 1875),
    ("Ludwig Maximilian University of Munich", "employment", 1875, 1880),
    ("Leipzig University", "employment", 1880, 1886),
    ("University of Göttingen", "professor", 1886, 1913),
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

    # ---------- 1. Klein 本人补齐 ----------
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
            "费利克斯·克莱因",
            '["Felix Christian Klein","埃尔朗根纲领","克莱因瓶","Klein 群"]',
            "German mathematician, author of the Erlangen Program (1849-1925)",
            "1849-04-25",
            "1925-06-22",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Klein id={pid0} 已补齐 people 字段（has_social_data=1，has_biography 保持）")

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
    for idx, country in enumerate(("Kingdom of Prussia", "German Empire", "Weimar Republic")):
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
            if name in ("Julius Plücker", "Rudolf Lipschitz"):
                f, t = pid, pid0  # 导师 → Klein
            else:
                f, t = pid0, pid  # Klein → 学生
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Klein-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Klein 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Felix Klein' OR b.name_en='Felix Klein'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
