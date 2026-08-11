#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Alfred North Whitehead 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Alfred_North_Whitehead/（Wikipedia 存档）
注意：库中主记录名 A.N. Whitehead(81)。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "A.N. Whitehead"
QID = "Q183372"

RELATIONS = [
    # 导师（有向：导师 → Whitehead）
    ("advisor-student", "Edward Routh", "博士导师（infobox）"),
    ("advisor-student", "William Davidson Niven", "博士导师"),
    # 学生（有向：Whitehead → 学生）
    ("advisor-student", "Bertrand Russell", "学生兼《数学原理》合著者（已建）"),
    ("advisor-student", "John Maynard Keynes", "学生，经济学家"),
    ("advisor-student", "W. V. O. Quine", "学生，分析哲学家"),
    ("advisor-student", "Arthur Eddington", "学生，天体物理学家"),
    ("advisor-student", "Paul Weiss", "学生，过程哲学家"),
    ("advisor-student", "William Tuthill Parry", "学生，逻辑学家"),
    ("advisor-student", "Grigoris Vlastos", "学生，古希腊哲学"),
    ("advisor-student", "Susanne Langer", "学生，符号哲学家"),
    ("advisor-student", "Dorothy Emmet", "学生，哲学家"),
    ("advisor-student", "Donald Davidson", "学生（notable），分析哲学家"),
    ("advisor-student", "Charles Hartshorne", "学生（notable），过程神学家"),
    ("advisor-student", "Raphael Demos", "学生（notable），古希腊哲学"),
    # 同事/朋友（无向）
    ("colleague", "G. E. Moore", "剑桥使徒/布卢姆斯伯里圈，哲学同道"),
    ("colleague", "Andrew Forsyth", "帝国理工首席数学教授，老友"),
    # 家族（无向）
    ("parent-child", "Henry Whitehead", "兄长，马德拉斯主教"),
    ("parent-child", "J. H. C. Whitehead", "侄子，代数拓扑学家（Whitehead 积）"),
]

MARKER = "[Whitehead-材料待展开] "

FIELDS = [
    ("mathematical logic", "数理逻辑", 0),
    ("logic", "逻辑学", 1),
    ("philosophy of science", "科学哲学", 2),
    ("metaphysics", "形而上学", 3),
    ("mathematics", "数学", 4),
]

AWARDS = [
    ("Fellow of the Royal Society", "英国皇家学会会士", 0),
    ("Sylvester Medal", "西尔维斯特奖章", 0),
    ("Order of Merit", "功绩勋章", 0),
    ("honorary doctor of the University of St Andrews", "圣安德鲁斯大学名誉博士", 0),
    ("honorary doctor of Harvard University", "哈佛大学名誉博士", 0),
    ("James Scott Prize Lectureship", "詹姆斯·斯科特奖讲座", 0),
    ("Butler Medal", "巴特勒奖章", 0),
]

INSTITUTIONS = [
    ("Sherborne School", "education", None, None),
    ("Trinity College", "education", 1880, 1884),
    ("University of Cambridge", "education", 1880, 1884),
    ("Trinity College", "employment", 1884, 1910),
    ("University College London", "employment", 1911, None),
    ("Imperial College London", "employment", 1914, 1924),
    ("Harvard University", "employment", 1924, 1937),
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

    # ---------- 1. Whitehead 本人补齐 ----------
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
            '["Alfred North Whitehead","怀特海","过程哲学","《数学原理》合著者"]',
            "English mathematician and philosopher (1861–1947)",
            "1861-02-15",
            "1947-12-30",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if phil_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, phil_id[0]))
    print(f"Whitehead id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    cur.execute("SELECT id FROM countries WHERE name_en='United Kingdom'")
    uk = cur.fetchone()
    if uk:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, uk[0]))
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
            if name in ("Edward Routh", "William Davidson Niven"):
                f, t = pid, pid0  # 导师 → Whitehead
            else:
                f, t = pid0, pid  # Whitehead → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Whitehead-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Whitehead 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='A.N. Whitehead' OR b.name_en='A.N. Whitehead'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
