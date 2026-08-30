#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Andrew Yao（姚期智）的社会关系（源自提示词 Andrew_Yao_zh.md「第 4.5 步」）。

关系清单：
- 博士导师（advisor-student，导师 → Yao）：
  Sheldon Glashow（哈佛物理导师）
  Chung Laung Liu（伊利诺伊 CS 导师）
- 门生（advisor-student，Yao → 学生）：William A. Dembski
- 合作者（collaborator，双向）：Danny Dolev、Yoshua Bengio、Geoffrey Hinton
- 配偶（spouse，无向）：Frances Yao

数据来源：本地 Wikipedia (turing/pages/2000/Andrew Yao/index.html) infobox + 正文。
不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
YAO = "Andrew Yao"

# 有向关系：博士导师（→ Yao）
ADVISORS = {"Sheldon Glashow", "Chung Laung Liu"}

# (relation_type, 人物, note, 方向)
# advisor：导师 → Yao；student：Yao → 学生；bi：无向
RELATIONS = [
    ("advisor-student", "Sheldon Glashow", "哈佛物理博士导师，1979 诺贝尔物理学奖得主", "advisor"),
    ("advisor-student", "Chung Laung Liu", "伊利诺伊大学 CS 博士导师", "advisor"),
    ("advisor-student", "William A. Dembski", "学生，智能设计研究", "student"),
    ("collaborator", "Danny Dolev", "合作者，Dolev–Yao 密码协议分析模型", "bi"),
    ("collaborator", "Yoshua Bengio", "合作者，2024 年 AI 极端风险专家共识论文共同作者", "bi"),
    ("collaborator", "Geoffrey Hinton", "合作者，2024 年 AI 极端风险专家共识论文共同作者", "bi"),
    ("spouse", "Frances Yao", "妻子，理论计算机科学家", "bi"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (YAO,))
    row = cur.fetchone()
    if not row:
        print(f"⚠ Yao 不在库中，请先运行 seed_yao_full.py")
        return
    yao_id = row[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    # 确保 computer scientist 职业存在（占位人物用）
    cur.execute("SELECT id FROM occupations WHERE name_en='computer scientist'")
    r = cur.fetchone()
    if r:
        occ_id = r[0]
    else:
        cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES ('computer scientist','计算机科学家')")
        occ_id = cur.lastrowid

    created = 0
    added = 0
    for rel, name, note, direction in RELATIONS:
        pid = by_en.get(norm(name))
        if pid is None:
            pid = by_zh.get(norm(name))
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'computer scientist',0)",
                (name,),
            )
            pid = cur.lastrowid
            cur.execute(
                "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (pid, occ_id),
            )
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 新建(占位): {name}")
            note = MARKER + note
        else:
            print(f"  已有: {name}")

        if rel == "advisor-student":
            if direction == "advisor":
                f, t = pid, yao_id
            elif direction == "student":
                f, t = yao_id, pid
            else:
                f, t = sorted([yao_id, pid])
        else:
            f, t = sorted([yao_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Andrew_Yao')",
            (f, t, rel, note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name}（{note[:20]}…）")

    conn.commit()
    print(f"\n新建人物: {created} · 新增关系: {added}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
