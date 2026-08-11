#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Richard Brauer 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Richard_Brauer/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Richard Brauer"
QID = "Q65201"

RELATIONS = [
    # 老师（有向：导师 → Brauer）
    ("advisor-student", "Issai Schur", "柏林大学博士导师（1926）；Schur 学派传承"),
    ("advisor-student", "Erhard Schmidt", "柏林大学博士导师（1926）"),
    # 学生（有向：Brauer → 学生）
    ("advisor-student", "Robert Steinberg", "学生，表示论，Jantzen 学派源头"),
    ("advisor-student", "Cecil J. Nesbitt", "学生，模表示论共同奠基人（1937）"),
    ("advisor-student", "J. Carson Mark", "学生，氢弹理论物理学家，洛斯阿拉莫斯"),
    ("advisor-student", "Richard Bruck", "学生，有限几何与关联结构"),
    ("advisor-student", "I. Martin Isaacs", "学生，群特征论"),
    ("advisor-student", "Donald S. Passman", "学生，群环理论"),
    ("advisor-student", "Ralph Gordon Stanton", "学生，组合数学与设计理论"),
    ("advisor-student", "Peter Landrock", "学生，密码学与群论"),
    ("advisor-student", "Donald John Lewis", "学生，数论"),
    # 合作者（无向）
    ("collaborator", "Tadasi Nakayama", "代数表示论合作（Nakayama 引理同期）"),
    ("collaborator", "Emil Artin", "Albert–Brauer–Hasse–Noether 定理"),
    # 同事（无向）
    ("colleague", "Hermann Weyl", "1934 邀请 Brauer 至普林斯顿 IAS"),
    ("colleague", "Emmy Noether", "促成 Brauer 获得多伦多大学教职"),
    ("colleague", "Carl Ludwig Siegel", "好友；Brauer–Siegel 定理"),
    ("colleague", "Nathan Jacobson", "共同编辑 Weyl 讲义《Structure and Representation of Continuous Groups》"),
    # 家族（兄弟，直系亲属）
    ("sibling", "Alfred Brauer", "兄长 Alfred（1894–1985），柏林数学家，1939 流亡美国"),
]

MARKER = "[Brauer-材料待展开] "

FIELDS = [
    ("group theory", "群论", 0),
    ("modular representation theory", "模表示论", 1),
    ("number theory", "数论", 2),
]

# 全部奖项收录
AWARDS = [
    ("Cole Prize in Algebra", "柯尔代数奖", 1949),
    ("National Medal of Science", "国家科学奖章", 1970),
    ("Guggenheim Fellowship", "古根海姆学者奖", 0),
]

INSTITUTIONS = [
    # 教育
    ("Frederick William University Berlin", "education", 1919, 1926),
    ("University of Freiburg", "education", None, None),
    # 任职
    ("University of Kentucky", "employment", 1933, 1934),
    ("Institute for Advanced Study", "employment", 1934, 1935),
    ("University of Toronto", "employment", 1935, 1948),
    ("University of Michigan", "employment", 1948, 1952),
    ("Harvard University", "employment", 1952, 1971),
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

    # ---------- 1. Brauer 本人补齐 ----------
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
            "理查德·布饶尔",
            '["Richard Dagobert Brauer","模表示论的奠基人","Brauer 群的引入者"]',
            "mathematician (1901–1977)",
            "1901-02-10",
            "1977-04-17",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Brauer id={pid0} 已补齐 people 字段（has_social_data=1）")

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
            "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
            "VALUES (%s,%s,%s,%s,%s)",
            (pid0, iid, rel, sy, ey),
        )
    print("  机构关联完成")

    # ---------- 5. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='Germany'")
    de = cur.fetchone()
    if de:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, de[0]))
    cur.execute("SELECT id FROM countries WHERE name_en='United States'")
    us = cur.fetchone()
    if us:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, us[0]))
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
            if name in ("Issai Schur", "Erhard Schmidt"):
                f, t = pid, pid0  # 导师 → Brauer
            else:
                f, t = pid0, pid  # Brauer → 学生
        elif rel == "parent-child":
            f, t = pid0, pid  # Brauer → 儿子
        elif rel == "sibling":
            f, t = sorted([pid0, pid])  # 兄弟无向
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Brauer-presentation')",
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

    print("\n=== 校验：Richard Brauer 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Richard Brauer' OR b.name_en='Richard Brauer'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
