#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Hendrik Antoon Lorentz 的社会关系（源自提示词 Hendrik_Lorentz_zh.md「第 4.5 步」）。

关系清单：
- 导师：Pieter Rijke（博士导师）、Frederik Kaiser（学术引路人）
- 学生：Pieter Zeeman（其他知名学生）、Geertruida de Haas-Lorentz（长女）、
       Adriaan Fokker、Leonard Ornstein
- 同事：Albert Einstein、Henri Poincaré、Paul Ehrenfest、Joseph Larmor
- 共同获奖：Pieter Zeeman（1902 诺奖共同得主）
- 配偶：Aletta Catharina Kaiser

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开] 」前缀。
"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
LORENTZ_QID = "Q41688"

# (relation_type, 人物, 方向, note)
# 方向：'to_lorentz' 表示对方→洛伦兹（洛伦兹是学生/被配偶），'from_lorentz' 表示洛伦兹→对方（洛伦兹是师）
RELATIONS = [
    ("advisor-student", "Pieter Rijke", "to_lorentz", "莱顿大学博士导师"),
    ("advisor-student", "Frederik Kaiser", "to_lorentz", "莱顿天文学教授，引导其转向物理"),
    ("advisor-student", "Pieter Zeeman", "from_lorentz", "其他知名学生，塞曼效应发现者"),
    ("advisor-student", "Geertruida de Haas-Lorentz", "from_lorentz", "长女，亦为其博士生，物理学家"),
    ("advisor-student", "Adriaan Fokker", "from_lorentz", "博士生，福克-普朗克方程"),
    ("advisor-student", "Leonard Ornstein", "from_lorentz", "博士生，Ornstein-Uhlenbeck 过程"),
    ("colleague", "Albert Einstein", "undirected", "深厚友谊，Einstein 称其一生最敬重之人"),
    ("colleague", "Henri Poincaré", "undirected", "命名'洛伦兹变换'，高度评价其理论"),
    ("colleague", "Paul Ehrenfest", "undirected", "1912 年继任莱顿教席"),
    ("colleague", "Joseph Larmor", "undirected", "1897 年独立使用相同变换"),
    ("co-honored", "Pieter Zeeman", "undirected", "1902 诺贝尔物理学奖共同得主"),
    ("spouse", "Aletta Catharina Kaiser", "undirected", "妻子，1881 结婚"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 定位洛伦兹
    cur.execute("SELECT id FROM people WHERE qid=%s", (LORENTZ_QID,))
    r = cur.fetchone()
    if not r:
        print("⚠ 洛伦兹不在库中，请先运行 seed_lorentz_full.py")
        return
    lorentz_id = r[0]
    print(f"✓ 洛伦兹 id={lorentz_id}")

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
            if direction == "from_lorentz":
                f, t = lorentz_id, pid  # 洛伦兹 → 学生
            else:
                f, t = pid, lorentz_id  # 导师 → 洛伦兹
        else:
            f, t = sorted([lorentz_id, pid])  # 无向：MIN(id)→MAX(id)

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Hendrik_Lorentz')",
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
