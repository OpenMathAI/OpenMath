#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Oswald Teichmüller 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Oswald_Teichmüller/（Wikipedia 存档）
注意：敏感人物（纳粹党员+Landau 抵制），关系如实记录、note 不引用种族主义内容。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Oswald Teichmüller"
QID = "Q68507"

RELATIONS = [
    # 导师（有向：导师 → Teichmüller）
    ("advisor-student", "Helmut Hasse", "博士导师（哥廷根 1935）"),
    # 学术影响（无向）
    ("colleague", "Rolf Nevanlinna", "转向复分析/拟共形映射的影响来源"),
    ("colleague", "Ludwig Bieberbach", "柏林合作者（1937-1939）"),
    # 相关（Landau 抵制事件，客观记录）
    ("controversy", "Edmund Landau", "1933-11-02 组织抵制 Landau 的课堂（纳粹时期事件，客观记录）"),
    ("controversy", "Richard Courant", "纳粹时期被迫离开哥廷根的同事之一"),
    # 老师/教授
    ("advisor-student", "Gustav Herglotz", "哥廷根教授"),
    ("advisor-student", "Hermann Weyl", "哥廷根教授"),
    ("advisor-student", "Hans Lewy", "哥廷根教授"),
    # 同事（密码部门 Wehrmacht）
    ("colleague", "Ernst Witt", "Wehrmacht 密码部门同事"),
    # 学位/审稿
    ("colleague", "Franz Rellich", "讲座来源（哥廷根）"),
    ("colleague", "Gottfried Köthe", "审稿（Main theorem 发表）"),
    # 传承/评价
    ("colleague", "Kurt Strebel", "继承者，苏黎世学派"),
    ("colleague", "Lars Ahlfors", "拟共形映射先驱之一"),
]

MARKER = "[Teichmüller-材料待展开] "

FIELDS = [
    ("complex analysis", "复分析", 0),
    ("quasiconformal mapping", "拟共形映射", 1),
    ("Riemann surface", "黎曼曲面", 2),
    ("algebra", "代数学", 3),
]

AWARDS = []

INSTITUTIONS = [
    ("University of Göttingen", "education", 1931, 1935),
    ("University of Göttingen", "employment", 1935, 1937),
    ("Humboldt University of Berlin", "employment", 1937, 1939),
    ("Wehrmacht", "employment", 1939, 1943),
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

    # ---------- 1. Teichmüller 本人补齐 ----------
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
            "奥斯瓦尔德·泰希缪勒",
            '["Paul Julius Oswald Teichmüller","Teichmüller 空间","拟共形映射","Grothendieck–Teichmüller 群"]',
            "German mathematician (1913–1943)",
            "1913-06-18",
            "1943-09-11",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Teichmüller id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    print("  奖项关联完成（无）")

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
    cur.execute("SELECT id FROM countries WHERE name_en='German Reich'")
    de = cur.fetchone()
    if not de:
        cur.execute("SELECT id FROM countries WHERE name_en='Germany'")
        de = cur.fetchone()
    if de:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, de[0]))
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
            if name in ("Helmut Hasse", "Gustav Herglotz", "Hermann Weyl", "Hans Lewy"):
                f, t = pid, pid0  # 导师/教授 → Teichmüller
            else:
                f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Teichmüller-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Teichmüller 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Oswald Teichmüller' OR b.name_en='Oswald Teichmüller'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
