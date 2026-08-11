#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Richard Dedekind 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Richard_Dedekind/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Richard Dedekind"
QID = "Q76556"

RELATIONS = [
    # 导师（有向：导师 → Dedekind）
    ("advisor-student", "Carl Friedrich Gauss", "博士导师（哥廷根 1852，'last student'）"),
    ("advisor-student", "Peter Gustav Lejeune Dirichlet", "亦师亦友（哥廷根），编辑其《数论讲义》"),
    ("advisor-student", "Moritz Stern", "哥廷根数论教授（其课程主要影响）"),
    # 同窗（无向）
    ("colleague", "Bernhard Riemann", "柏林同期（1854 双获特许任教资格）"),
    # 合作者（无向）
    ("collaborator", "Heinrich Martin Weber", "合著（1882）用理想代数化黎曼曲面，证 Riemann–Roch"),
    # 相关（无向）
    ("colleague", "Georg Cantor", "1872 相识，协助其对 Kronecker；近年研究称 Cantor 剽窃其无穷证明"),
    ("colleague", "Leopold Kronecker", "Cantor 争议中的对立方"),
    ("colleague", "Giuseppe Peano", "1889 引用其自然数公理改进为 Peano 公理"),
    ("colleague", "Ernst Eduard Kummer", "其'理想数'(1843) 被 Dedekind 推广为'理想'"),
    ("colleague", "Emmy Noether", "继承并发展其理想理论"),
    ("colleague", "David Hilbert", "继承并发展其理想理论"),
]

MARKER = "[Dedekind-材料待展开] "

FIELDS = [
    ("algebraic number theory", "代数数论", 0),
    ("abstract algebra", "抽象代数", 1),
    ("ring theory", "环论", 2),
    ("number theory", "数论", 3),
    ("set theory", "集合论", 4),
]

AWARDS = [
    ("member of the Prussian Academy of Sciences", "普鲁士科学院院士", 1880),
    ("foreign member of the French Academy of Sciences", "法国科学院外籍院士", 1900),
    ("honorary doctorate of the University of Oslo", "奥斯陆大学名誉博士", 0),
    ("honorary doctorate of the University of Zurich", "苏黎世大学名誉博士", 0),
    ("honorary doctorate of the Technical University of Braunschweig", "不伦瑞克工业大学名誉博士", 0),
]

INSTITUTIONS = [
    ("Collegium Carolinum", "education", 1848, 1850),
    ("University of Göttingen", "education", 1850, 1852),
    ("Frederick William University Berlin", "education", 1852, 1854),
    ("University of Göttingen", "employment", 1854, 1858),
    ("ETH Zurich", "employment", 1858, 1862),
    ("TU Braunschweig", "employment", 1862, 1894),
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

    # ---------- 1. Dedekind 本人补齐 ----------
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
            "理查德·戴德金",
            '["Julius Wilhelm Richard Dedekind","Dedekind 分割","理想理论","无限集定义"]',
            "German mathematician (1831–1916)",
            "1831-10-06",
            "1916-02-12",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    if phil_id:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (pid0, phil_id[0]))
    print(f"Dedekind id={pid0} 已补齐 people 字段（has_social_data=1）")

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
            cur.execute("INSERT INTO awards(name_en, name_zh, award_type) VALUES (%s,%s,'honor')", (a_en, a_zh))
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
    for idx, country in enumerate(("German Empire", "Duchy of Brunswick")):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (country,))
        cid = cur.fetchone()
        if not cid:
            cur.execute("INSERT IGNORE INTO countries(name_en, name_zh, is_current) VALUES (%s,%s,0)",
                        (country, "布伦瑞克公国" if "Duchy" in country else country))
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
            if name in ("Carl Friedrich Gauss", "Peter Gustav Lejeune Dirichlet", "Moritz Stern"):
                f, t = pid, pid0  # 导师 → Dedekind
            else:
                f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Dedekind-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Dedekind 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Richard Dedekind' OR b.name_en='Richard Dedekind'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
