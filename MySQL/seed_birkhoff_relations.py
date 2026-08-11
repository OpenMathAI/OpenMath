#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并 G.D. Birkhoff(62) 与 George David Birkhoff(454)，梳理社会关系与研究领域入库。

数据源：mathematician/pages/George_David_Birkhoff/（Wikipedia 存档）
"""
import re
import unicodedata

from db_mysql import get_conn

MAIN_ID = 62     # G.D. Birkhoff（rank 关联）
DUP_ID = 454     # George David Birkhoff（重复占位）
NAME = "George David Birkhoff"
QID = "Q327301"

# (关系类型, 人物, 方向说明, note)
RELATIONS = [
    # 老师（有向：导师 → Birkhoff）
    ("advisor-student", "Eliakim Hastings Moore", "teacher", "芝加哥大学博士导师（1907）"),
    # 学生（有向：Birkhoff → 学生）
    ("advisor-student", "Marston Morse", "student", "博士导师（哈佛，1917）；Morse 理论"),
    ("advisor-student", "Marshall Harvey Stone", "student", "博士导师（哈佛，1922）；Stone 定理"),
    ("advisor-student", "Hassler Whitney", "student", "博士导师（哈佛，1932）；微分拓扑"),
    ("advisor-student", "Bernard Koopman", "student", "博士导师（哈佛）；遍历理论"),
    ("advisor-student", "Robert Daniel Carmichael", "student", "博士导师（哈佛）；数论"),
    ("advisor-student", "Joseph Leonard Walsh", "student", "博士导师（哈佛）；复分析"),
    # 家族（有向：父子）
    ("parent-child", "Garrett Birkhoff", "son", "儿子 Garrett Birkhoff（1911–1996），数学家，格论奠基人"),
    # 同事（无向）
    ("colleague", "Oswald Veblen", "colleague", "普林斯顿同事，几何学；Veblen 撰写其传记"),
    ("colleague", "Saunders Mac Lane", "colleague", "哈佛晚辈；为 Birkhoff 反犹指控辩护"),
    # 争议（无向）：反犹指控
    ("controversy", "Albert Einstein", "controversy", "Einstein 指控其反犹（1930s 遴选犹太数学家被排除）；Mac Lane 辩护"),
    ("controversy", "Norbert Wiener", "controversy", "Wiener 指控其反犹遴选；Mac Lane 反驳"),
    # 影响（无向）：Poincaré 的数学遗产
    ("colleague", "Henri Poincaré", "colleague", "最受 Poincaré 著作影响；1913 证明 Poincaré『最后几何定理』（Poincaré–Birkhoff 定理）"),
    # 荣誉共同体：与 Ulam 亲近
    ("colleague", "Stanislaw Ulam", "colleague", "与 Ulam 亲近，曾试图留 Ulam 于哈佛"),
]

MARKER = "[Birkhoff-材料待展开] "

FIELDS = [
    ("ergodic theory", "遍历理论", 0),
    ("topology", "拓扑学", 1),
    ("differential equations", "微分方程", 2),
    ("three-body problem", "三体问题", 3),
]

# 全部奖项收录：Bôcher(1923) + Newcomb(1926) + 院士 + 名誉博士
AWARDS = [
    ("Bôcher Memorial Prize", "波谢纪念奖", 1923),
    ("Newcomb Cleveland Prize", "纽科姆·克利夫兰奖", 1926),
    ("Fellow of the Royal Society of Edinburgh", "爱丁堡皇家学会会士", 0),
    ("doctor honoris causa from the University of Paris", "巴黎大学名誉博士", 0),
    ("honorary doctor of the University of Poitiers", "普瓦捷大学名誉博士", 0),
]

INSTITUTIONS = [
    ("Harvard University", "education", 1902, 1905),
    ("University of Chicago", "education", 1905, 1907),
    ("University of Wisconsin–Madison", "employment", 1907, 1909),
    ("Princeton University", "employment", 1909, 1912),
    ("Harvard University", "employment", 1912, 1944),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # ---------- 0. 合并重复人物 454 → 62 ----------
    # 迁移关系（INSERT IGNORE 后删除旧，兼容复合主键表）
    for tbl in ("person_relation", "award_laureate", "person_occupation",
                "person_field", "person_institution", "person_nationality"):
        cols = {"person_relation": "from_id,to_id",
                "award_laureate": "person_id",
                "person_occupation": "person_id",
                "person_field": "person_id",
                "person_institution": "person_id",
                "person_nationality": "person_id"}[tbl]
        if tbl == "person_relation":
            cur.execute(f"SELECT * FROM {tbl} WHERE from_id=%s OR to_id=%s", (DUP_ID, DUP_ID))
        else:
            cur.execute(f"SELECT * FROM {tbl} WHERE person_id=%s", (DUP_ID,))
        rows = cur.fetchall()
        cur.execute("SHOW COLUMNS FROM " + tbl)
        desc = [r[0] for r in cur.fetchall()]
        for row in rows:
            data = dict(zip(desc, row))
            if tbl == "person_relation":
                data["from_id"] = MAIN_ID if data["from_id"] == DUP_ID else data["from_id"]
                data["to_id"] = MAIN_ID if data["to_id"] == DUP_ID else data["to_id"]
            else:
                data["person_id"] = MAIN_ID
            d = {k: v for k, v in data.items() if v is not None}
            cols_s = ", ".join(f"`{k}`" for k in d)
            ph = ", ".join("%s" for _ in d)
            try:
                cur.execute(f"INSERT IGNORE INTO {tbl} ({cols_s}) VALUES ({ph})", list(d.values()))
            except Exception as e:
                print(f"  ! {tbl} 迁移跳过: {e}")
    # 删除重复占位
    cur.execute("DELETE FROM people WHERE id=%s", (DUP_ID,))
    print(f"已合并: id=454 (George David Birkhoff) → id=62 (G.D. Birkhoff)")

    # ---------- 1. Birkhoff 本人补齐 ----------
    cur.execute(
        "UPDATE people SET qid=%s, name_en=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            QID,
            NAME,
            "乔治·戴维·伯克霍夫",
            '["G.D. Birkhoff","美国第一位有国际声誉的数学家","遍历理论的创立者"]',
            "American mathematician (1884–1944)",
            "1884-03-21",
            "1944-11-12",
            MAIN_ID,
        ),
    )
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (MAIN_ID, occ_id))
    cur.execute("SELECT id FROM occupations WHERE name_en='topologist'")
    top = cur.fetchone()
    if top:
        cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,1)",
                    (MAIN_ID, top[0]))
    print(f"Birkhoff id={MAIN_ID} 已补齐 people 字段（has_social_data=1）")

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
            (MAIN_ID, fid, rank),
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
            (MAIN_ID, aid, year, note),
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
            (MAIN_ID, iid, rel, sy, ey),
        )
    print("  机构关联完成")

    # ---------- 5. 国籍 ----------
    cur.execute("SELECT id FROM countries WHERE name_en='United States'")
    us = cur.fetchone()
    if us:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (MAIN_ID, us[0]))
    print("  国籍关联完成")

    # ---------- 6. 社会关系 ----------
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    created = 0
    relations_added = 0
    for rel, name, direction, note in RELATIONS:
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
            if direction == "teacher":
                f, t = pid, MAIN_ID  # 导师 → Birkhoff
            else:
                f, t = MAIN_ID, pid  # Birkhoff → 学生
        elif rel == "parent-child":
            f, t = MAIN_ID, pid  # Birkhoff → 儿子
        else:
            f, t = sorted([MAIN_ID, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Birkhoff-presentation')",
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

    print("\n=== 校验：George David Birkhoff 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en LIKE '%Birkhoff%' OR b.name_en LIKE '%Birkhoff%'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
