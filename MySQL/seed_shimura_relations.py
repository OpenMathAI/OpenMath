#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Goro Shimura（志村五郎）的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Goro_Shimura/（Wikipedia 存档）
注意：库中 name_en=`Shimura Goro`（日式姓名顺序）。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Shimura Goro"
QID = "Q353411"

RELATIONS = [
    # 合作者/挚友（无向）
    ("collaborator", "Yutaka Taniyama", "挚友，谷山–志村猜想共同提出者"),
    ("collaborator", "Martin Eichler", "Eichler–Shimura 同余关系/同构的共同奠基"),
    ("collaborator", "Pierre Deligne", "Eichler–Shimura 同构用于 Weil 猜想证明"),
    ("colleague", "André Weil", "引荐其赴普林斯顿大学"),
    # 费马大定理链条（无向）
    ("co-honored", "Andrew Wiles", "1995 证明谷山–志村猜想的半稳定情形（费马大定理）"),
    ("collaborator", "Kenneth Ribet", "1990 Ribet 定理：半稳定情形蕴含费马大定理"),
    # 学生（有向：Shimura → 学生）
    ("advisor-student", "Bill Casselman", "学生，自守形式"),
    ("advisor-student", "Melvin Hochster", "学生，交换代数"),
    ("advisor-student", "Robert Rumely", "学生，数论"),
    ("advisor-student", "Alice Silverberg", "学生，椭圆曲线"),
    ("advisor-student", "Don Blasius", "学生，motives"),
    ("advisor-student", "Hiroyuki Yoshida", "学生，自守形式"),
    ("advisor-student", "Jerry Shurman", "学生，模形式"),
]

MARKER = "[Shimura-材料待展开] "

FIELDS = [
    ("number theory", "数论", 0),
    ("algebraic number theory", "代数数论", 1),
    ("automorphic forms", "自守形式", 2),
    ("algebraic geometry", "代数几何", 3),
]

# 全部奖项收录
AWARDS = [
    ("Cole Prize in Number Theory", "柯尔数论奖", 1977),
    ("Asahi Prize", "朝日奖", 1991),
    ("Steele Prize for Lifetime Achievement", "斯蒂尔终身成就奖", 1996),
    ("Guggenheim Fellowship", "古根海姆学者奖", 1970),
]

INSTITUTIONS = [
    ("University of Tokyo", "education", None, None),
    ("University of Tokyo", "employment", None, None),
    ("Osaka University", "employment", None, None),
    ("Institute for Advanced Study", "employment", None, None),
    ("Princeton University", "employment", 1964, 1999),
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

    # ---------- 1. Shimura 本人补齐 ----------
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
            '["Goro Shimura","Gorō Shimura","志村五郎","谷山–志村猜想","Shimura variety"]',
            "Japanese mathematician (1930–2019)",
            "1930-02-23",
            "2019-05-03",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Shimura id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("United States", "Japan")):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (country,))
        cid = cur.fetchone()
        if not cid:
            cur.execute("INSERT IGNORE INTO countries(name_en, name_zh, is_current) VALUES (%s,%s,1)",
                        (country, "日本" if country == "Japan" else country))
            cid = cur.lastrowid
            print(f"  + 新建国家: {country} (id={cid})")
        else:
            cid = cid[0]
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                    (pid0, cid, idx))
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
            f, t = pid0, pid  # Shimura → 学生
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Shimura-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Shimura 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Shimura Goro' OR b.name_en='Shimura Goro'
           OR a.name_en='Goro Shimura' OR b.name_en='Goro Shimura'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
