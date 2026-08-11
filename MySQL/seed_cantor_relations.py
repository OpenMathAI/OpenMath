#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Georg Cantor 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Georg_Cantor/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Georg Cantor"
QID = "Q76420"

RELATIONS = [
    # 导师（有向：导师 → Cantor）
    ("advisor-student", "Ernst Kummer", "博士导师（柏林 1867）"),
    ("advisor-student", "Karl Weierstrass", "博士导师（柏林 1867）"),
    # 学生
    ("advisor-student", "Alfred Barneck", "博士生"),
    # 同事/好友（无向）
    ("colleague", "Richard Dedekind", "挚友与长期通信者（1872 起）"),
    ("colleague", "Eduard Heine", "哈雷同事，促其转向分析（三角级数）"),
    ("colleague", "Gösta Mittag-Leffler", "重要通信者（1882 起），1885 撤稿事件后疏远"),
    ("colleague", "Philip Jourdain", "通信者与英文翻译者（1905 起）"),
    # 对手/反对者（无向）
    ("controversy", "Leopold Kronecker", "柏林数学领袖，攻击其集合论（'科学骗子'）"),
    ("controversy", "Henri Poincaré", "对其超穷数理论持反对态度"),
    ("controversy", "Hermann Weyl", "对集合论的建构主义批评者之一"),
    ("controversy", "L.E.J. Brouwer", "直觉主义立场反对其集合论"),
    ("controversy", "Ludwig Wittgenstein", "哲学上批评集合论（'nonsense'）"),
    # 捍卫者/认可（无向）
    ("colleague", "David Hilbert", "'无人能把我们从康托尔创造的乐园中驱逐出去'"),
    ("colleague", "Ernst Zermelo", "1904 驳斥 König 的（错误）证明"),
    ("colleague", "Adolf Hurwitz", "1897 ICM 上赞赏其工作"),
    ("colleague", "Jacques Hadamard", "1897 ICM 上赞赏其工作"),
    ("colleague", "Charles Sanders Peirce", "美国哲学家，赞赏其集合论"),
    # 相关（无向）
    ("colleague", "Julius König", "1904 ICM 给出（错误）反证，被 Zermelo 驳斥"),
    ("colleague", "Henry John Stephen Smith", "Cantor 集的发现者（1875）"),
    # 家族
    ("spouse", "Vally Guttmann", "妻（1874 结婚），育有 6 个孩子"),
]

MARKER = "[Cantor-材料待展开] "

FIELDS = [
    ("set theory", "集合论", 0),
    ("mathematical logic", "数理逻辑", 1),
    ("number theory", "数论", 2),
    ("topology", "拓扑学", 3),
    ("mathematical analysis", "数学分析", 4),
]

AWARDS = [
    ("Sylvester Medal", "西尔维斯特奖章", 1904),
    ("honorary doctorate of the University of St Andrews", "圣安德鲁斯大学名誉博士", 1912),
]

INSTITUTIONS = [
    ("Technische Universität Darmstadt", "education", 1860, 1862),
    ("ETH Zurich", "education", 1862, 1863),
    ("Frederick William University Berlin", "education", 1863, 1867),
    ("University of Göttingen", "education", None, None),
    ("Martin Luther University Halle-Wittenberg", "employment", 1869, 1913),
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
    cur.execute("SELECT id FROM occupations WHERE name_en='philosopher'")
    phil_id = cur.fetchone()

    # ---------- 1. Cantor 本人补齐 ----------
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
            "格奥尔格·康托尔",
            '["Georg Ferdinand Ludwig Philipp Cantor","集合论创始人","超穷数","康托尔乐园"]',
            "German mathematician, inventor of set theory (1845–1918)",
            "1845-03-03",
            "1918-01-06",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if phil_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, phil_id[0]))
    print(f"Cantor id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("German Empire", "German Reich")):
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
            if name in ("Ernst Kummer", "Karl Weierstrass"):
                f, t = pid, pid0  # 导师 → Cantor
            else:
                f, t = pid0, pid  # Cantor → 学生
        elif rel == "spouse":
            f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Cantor-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Cantor 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Georg Cantor' OR b.name_en='Georg Cantor'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
