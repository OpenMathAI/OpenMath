#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Dennis Ritchie 的社会关系（源自提示词 Dennis_Ritchie_zh.md「第 4.5 步」。

关系清单（均源自本地 Wikipedia turing/pages/1983/Dennis Ritchie/index.html）：
- 博士导师：Patrick C. Fischer（advisor-student，Fischer → Ritchie）
- 同事 / 共同得主：Ken Thompson（Unix/C 共创 + 1983 共获图灵奖，用 colleague + co-honored 两种关系表达）
- 同事：Brian Kernighan（合著 K&R）
- 同事：Rob Pike（Plan 9/Inferno/Limbo；讣告首报者）
- 同事：Doug McIlroy（Research Unix 同事，留下"almost everything"评价）
- 同事：Robert Morris（M-209 密码分析合作）
- 同事：James Reeds（M-209 密码分析合作）

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
RITCHIE = "Dennis Ritchie"

# 导师（有向：Fischer → Ritchie）
ADVISORS = {"Patrick C. Fischer"}

# (relation_type, 人物, note)
RELATIONS = [
    # 博士导师（Fischer → Ritchie）
    ("advisor-student", "Patrick C. Fischer", "博士导师，Harvard（计算复杂性与程序结构，1968 论文草稿）"),
    # 同事：Unix/C 共创 + 1983 共同图灵奖
    ("colleague", "Ken Thompson", "Bell Labs 同事，Unix 与 C 共创者；1983 年共同获得图灵奖"),
    ("co-honored", "Ken Thompson", "1983 年图灵奖共同得主（Unix 与 C 语言）"),
    # 同事：合著 K&R
    ("colleague", "Brian Kernighan", "Bell Labs 同事，合著《The C Programming Language》(K&R, 1978)"),
    # 同事：Plan 9/Inferno/Limbo；讣告首报者
    ("colleague", "Rob Pike", "Bell Labs/Lucent 同事，参与 Plan 9/Inferno/Limbo；2011 年首报 Ritchie 离世"),
    # 同事：Research Unix；"almost everything" 评价
    ("colleague", "Doug McIlroy", "Bell Labs 同事，Research Unix 时期共事；留下对 Ritchie/Thompson 的评价"),
    # 同事：M-209 密码分析
    ("colleague", "Robert Morris", "1970s 合作对 M-209 密码机做唯密文攻击（未发表）"),
    ("colleague", "James Reeds", "1970s 合作对 M-209 密码机做唯密文攻击（未发表）"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (RITCHIE,))
    row = cur.fetchone()
    if not row:
        print(f"⚠ Ritchie 不在库中，请先运行 seed_ritchie_full.py")
        return
    ritchie_id = row[0]

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
    for rel, name, note in RELATIONS:
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
        else:
            print(f"  已有: {name}")

        # 方向：导师（Fischer → Ritchie）、其余无向（sorted 归一）
        if rel == "advisor-student":
            if name in ADVISORS:
                f, t = pid, ritchie_id
            else:
                f, t = ritchie_id, pid
        else:
            f, t = sorted([ritchie_id, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Dennis_Ritchie')",
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
