#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Tadashi Nakayama（中山正）的社会关系与研究领域，入库 greatminds 数据库。

注意：
- 本地页面为消歧页，已核实正确数学家页面 Tadashi Nakayama (mathematician)（1912-1964）qid=Q324943
- 数据库重复人物：id=90 (Nakayama Tadashi, rank 关联) 与 id=503 (Tadasi Nakayama, 已有生卒数据) 为同一人
- 处理：保留 90 为主记录（rank 关联），迁移 503 的关系与生卒数据，删除 503
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Nakayama Tadashi"
DUP_NAME = "Tadasi Nakayama"
QID = "Q324943"  # 正确数学家 Tadashi Nakayama (mathematician)

RELATIONS = [
    # 导师（有向：导师 → Nakayama）
    ("advisor-student", "Teiji Takagi", "博士导师（高木贞治，类域论）"),
    # 合作者（无向）
    ("collaborator", "Richard Brauer", "Brauer–Nakayama 理论（群表示论）"),
    ("collaborator", "Emil Artin", "环论/表示论交流"),
    ("collaborator", "Helmut Hasse", "代数数论交流"),
    ("collaborator", "Saunders Mac Lane", "抽象代数交流"),
]

MARKER = "[Nakayama-材料待展开] "

FIELDS = [
    ("group theory", "群论", 0),
    ("ring theory", "环论", 1),
    ("representation theory", "表示论", 2),
    ("algebra", "代数学", 3),
]

AWARDS = []

INSTITUTIONS = [
    ("Kyoto University", "education", None, None),
    ("Kyoto University", "employment", None, None),
    ("Nagoya University", "employment", None, None),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def merge_dup(cur, main_id: int, dup_id: int):
    """合并重复人物 dup_id → main_id（幂等，跳过 id 字段）。"""
    for tbl in ("person_relation", "award_laureate", "person_occupation",
                "person_field", "person_institution", "person_nationality"):
        if tbl == "person_relation":
            cur.execute("SELECT * FROM person_relation WHERE from_id=%s OR to_id=%s", (dup_id, dup_id))
        else:
            cur.execute(f"SELECT * FROM {tbl} WHERE person_id=%s", (dup_id,))
        rows = cur.fetchall()
        if not rows:
            continue
        cur.execute("SHOW COLUMNS FROM " + tbl)
        desc = [r[0] for r in cur.fetchall()]
        for row in rows:
            data = dict(zip(desc, row))
            if tbl == "person_relation":
                data["from_id"] = main_id if data["from_id"] == dup_id else data["from_id"]
                data["to_id"] = main_id if data["to_id"] == dup_id else data["to_id"]
            else:
                data["person_id"] = main_id
            d = {k: v for k, v in data.items() if k != "id" and v is not None}
            cols_s = ", ".join(f"`{k}`" for k in d)
            ph = ", ".join("%s" for _ in d)
            try:
                cur.execute(f"INSERT IGNORE INTO {tbl} ({cols_s}) VALUES ({ph})", list(d.values()))
            except Exception as e:
                print(f"  ! {tbl} 迁移跳过: {e}")
    # 迁移生卒数据到主记录（若主记录为空）
    cur.execute("SELECT birth_date, death_date FROM people WHERE id=%s", (dup_id,))
    drow = cur.fetchone()
    if drow and (drow[0] or drow[1]):
        cur.execute(
            "UPDATE people SET birth_date=COALESCE(birth_date,%s), death_date=COALESCE(death_date,%s) WHERE id=%s",
            (drow[0], drow[1], main_id),
        )
    cur.execute("DELETE FROM people WHERE id=%s", (dup_id,))
    print(f"已合并: id={dup_id} ({DUP_NAME}) → id={main_id} ({NAME})")


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: pid for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: pid for pid, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    # ---------- 0. 合并重复人物 ----------
    cur.execute("SELECT id FROM people WHERE name_en=%s", (NAME,))
    main_row = cur.fetchone()
    cur.execute("SELECT id FROM people WHERE name_en=%s", (DUP_NAME,))
    dup_row = cur.fetchone()
    if main_row and dup_row:
        merge_dup(cur, main_row[0], dup_row[0])
    pid0 = main_row[0] if main_row else None
    if pid0 is None:
        cur.execute(
            "INSERT INTO people(name_en, primary_occupation, has_biography, qid) "
            "VALUES (%s,'mathematician',0,%s)",
            (NAME, QID),
        )
        pid0 = cur.lastrowid

    # ---------- 1. Nakayama 本人补齐 ----------
    cur.execute(
        "UPDATE people SET qid=COALESCE(qid,%s), name_zh=%s, name_variants=%s, description=%s, "
        "has_social_data=1 WHERE id=%s",
        (
            QID,
            "中山正",
            '["Tadashi Nakayama","Tadasi Nakayama","中山 正","Nakayama lemma 中山引理"]',
            "Japanese mathematician (1912–1964)",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Nakayama id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    cur.execute("SELECT id FROM countries WHERE name_en='Japan'")
    jp = cur.fetchone()
    if jp:
        cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,0)",
                    (pid0, jp[0]))
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
            if name == "Teiji Takagi":
                f, t = pid, pid0  # 导师 → Nakayama
            else:
                f, t = pid0, pid
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Nakayama-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Nakayama 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Nakayama Tadashi' OR b.name_en='Nakayama Tadashi'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
