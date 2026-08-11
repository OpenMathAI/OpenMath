#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Ernst Lindelöf 的社会关系与研究领域，入库 greatminds 数据库。

数据源：mathematician/pages/Ernst_Lindelöf/（Wikipedia 存档）
同时合并重复人物：id=517 (Ernst Leonard Lindelöf) → id=92 (Ernst Lindelöf)。
"""
import re
import unicodedata

from db_mysql import get_conn

NAME = "Ernst Lindelöf"
DUP_NAME = "Ernst Leonard Lindelöf"
QID = "Q924443"

RELATIONS = [
    # 导师（有向：导师 → Lindelöf）
    ("advisor-student", "Hjalmar Mellin", "博士导师（赫尔辛基 1893）"),
    # 学生（有向：Lindelöf → 学生）
    ("advisor-student", "Lars Ahlfors", "学生，首届菲尔兹奖得主"),
    ("advisor-student", "Rolf Nevanlinna", "学生，Nevanlinna 理论"),
    ("advisor-student", "Pekka Myrberg", "学生"),
    # 家族（无向）
    ("parent-child", "Lorenz Leonard Lindelöf", "父亲，赫尔辛基数学教授"),
    ("parent-child", "Uno Lindelöf", "弟弟，英语语言学家"),
    ("parent-child", "Edvard Rudolf Neovius", "堂兄，前任数学讲席"),
    # 合作者（无向）
    ("collaborator", "Émile Borel", "邀请其为系列首位外国作者（1905 留数专著）"),
    ("collaborator", "Lars Edvard Phragmén", "Phragmén–Lindelöf 原理共同命名"),
]

MARKER = "[Lindelöf-材料待展开] "

FIELDS = [
    ("complex analysis", "复分析", 0),
    ("topology", "拓扑学", 1),
    ("mathematical analysis", "数学分析", 2),
    ("number theory", "数论", 3),
]

AWARDS = [
    ("Grand Cross of the Order of the White Rose of Finland", "芬兰白玫瑰大十字勋章", 0),
    ("Order of Saint Anna, 3rd class", "圣安娜勋章三等", 0),
    ("Knight of the Order of the Polar Star", "北极星勋章骑士", 0),
]

INSTITUTIONS = [
    ("University of Helsinki", "education", None, 1893),
    ("University of Göttingen", "education", None, None),
    ("University of Helsinki", "employment", 1895, 1938),
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

    # ---------- 1. Lindelöf 本人补齐 ----------
    cur.execute(
        "UPDATE people SET qid=%s, name_zh=%s, name_variants=%s, description=%s, "
        "birth_date=%s, death_date=%s, has_social_data=1 WHERE id=%s",
        (
            QID,
            "恩斯特·林德洛夫",
            '["Ernst Leonard Lindelöf","Lindelöf 空间","Picard–Lindelöf 定理","Phragmén–Lindelöf 原理"]',
            "Finnish mathematician (1870–1946)",
            "1870-03-07",
            "1946-06-04",
            pid0,
        ),
    )
    cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid0, occ_id))
    print(f"Lindelöf id={pid0} 已补齐 people 字段（has_social_data=1）")

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
    for idx, country in enumerate(("Grand Duchy of Finland", "Finland")):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (country,))
        cid = cur.fetchone()
        if not cid:
            cur.execute("INSERT IGNORE INTO countries(name_en, name_zh, is_current) VALUES (%s,%s,1)",
                        (country, "芬兰大公国" if "Duchy" in country else "芬兰"))
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
            if name == "Hjalmar Mellin":
                f, t = pid, pid0  # 导师 → Lindelöf
            else:
                f, t = pid0, pid  # Lindelöf → 学生
        elif rel == "parent-child":
            f, t = pid, pid0  # 父/弟/堂兄 → Lindelöf（祖先方向）
        else:
            f, t = sorted([pid0, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'Lindelöf-presentation')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            relations_added += 1

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {relations_added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")

    print("\n=== 校验：Lindelöf 社会关系 ===")
    cur.execute(
        """SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
        FROM person_relation pr
        JOIN people a ON a.id=pr.from_id
        JOIN people b ON b.id=pr.to_id
        JOIN relation_types rt ON rt.relation_key=pr.relation_type
        WHERE a.name_en='Ernst Lindelöf' OR b.name_en='Ernst Lindelöf'"""
    )
    for r in cur.fetchall():
        print(f"  {r[0]} {r[1]} {r[2]} — {(r[3] or '')[:40]}")

    conn.close()


if __name__ == "__main__":
    main()
