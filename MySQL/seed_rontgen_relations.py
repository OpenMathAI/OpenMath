#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Wilhelm Conrad Röntgen 的社会关系（源自提示词 Wilhelm_Rontgen_zh.md「第 4.5 步」）。

关系清单：
- 导师：Gustav Zeuner（博士导师）、August Kundt（学术导师）
- 学生：Abram Ioffe（苏联物理学奠基人）、Rudolf Ladenburg
- 同事：Philipp Lenard（阴极射线同行，1896 共享 Rumford Medal）、
       Henri Becquerel（受 X 射线工作启发发现放射性）、Marie Curie、Pierre Curie
- 配偶：Anna Bertha Ludwig

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
RONTGEN = "Wilhelm Conrad Röntgen"
RONTGEN_QID = "Q35149"

# (relation_type, 人物, 方向, note)
# 方向：'to_rontgen' 表示对方→伦琴（伦琴是学生/被配偶），'from_rontgen' 表示伦琴→对方（伦琴是师）
RELATIONS = [
    ("advisor-student", "Gustav Zeuner", "to_rontgen", "苏黎世大学博士导师"),
    ("advisor-student", "August Kundt", "to_rontgen", "学术导师，伦琴是其最喜爱的学生"),
    ("advisor-student", "Abram Ioffe", "from_rontgen", "学生，苏联实验物理学奠基人之一"),
    ("advisor-student", "Rudolf Ladenburg", "from_rontgen", "学生，实验物理学家"),
    ("colleague", "Philipp Lenard", "undirected", "阴极射线研究同行，1896 共享 Rumford Medal"),
    ("colleague", "Henri Becquerel", "undirected", "受 X 射线工作启发发现天然放射性"),
    ("colleague", "Marie Curie", "undirected", "受 X 射线工作影响，转向放射性同位素研究"),
    ("colleague", "Pierre Curie", "undirected", "受 X 射线工作影响，转向放射性同位素研究"),
    ("spouse", "Anna Bertha Ludwig", "undirected", "妻子，1872 结婚；其手部 X 光片为史上第一张医学 X 光片"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 定位伦琴
    cur.execute("SELECT id FROM people WHERE qid=%s", (RONTGEN_QID,))
    r = cur.fetchone()
    if not r:
        print("⚠ 伦琴不在库中，请先运行 seed_rontgen_full.py")
        return
    rontgen_id = r[0]
    print(f"✓ 伦琴 id={rontgen_id}")

    # 加载全部人物
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, direction, note in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'physicist',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                        (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name}")
        else:
            print(f"  已有: {name} (id={pid})")

        # 方向判定
        if rel == "advisor-student":
            if direction == "from_rontgen":
                f, t = rontgen_id, pid  # 伦琴 → 学生
            else:
                f, t = pid, rontgen_id  # 导师 → 伦琴
        else:
            f, t = sorted([rontgen_id, pid])  # 无向：MIN(id)→MAX(id)

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Wilhelm_Rontgen')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name}（{note[:18]}…）")

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
