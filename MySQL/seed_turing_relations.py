#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Alan Turing 的社会关系（源自提示词 Alan_Turing_zh.md 第 4.5 步，规范 §二十）。

关系（11 条）：
- Alonzo Church      — 博士导师（advisor-student，Church→Turing）
- Robin Gandy        — 博士生（advisor-student，Turing→Gandy）
- Beatrice Worsley   — 博士生（advisor-student，Turing→Worsley）
- Max Newman         — 同事（colleague）：剑桥讲师 + 曼彻斯特大学同事
- Gordon Welchman    — 同事（colleague）：Bletchley Park 核心合作者，Hut 6 负责人
- Joan Clarke        — 合作者（collaborator）：Bletchley Park 密码分析员，短暂未婚妻
- Jack Good          — 合作者（collaborator）：Bletchley Park 统计学家
- John von Neumann   — 同事（colleague）：普林斯顿时期（已在库 id=3）
- Claude Shannon     — 合作者（collaborator）：1943 贝尔实验室会面（已在库 id=33）
- Ludwig Wittgenstein— 同事（colleague）：剑桥数学哲学辩论
- Christopher Morcom — 挚友（colleague）：少年挚友，1930 年牛结核病早逝

缺失人物（9 人）先建占位（has_biography=0），note 加「[材料待展开]」。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
TURING = "Alan Turing"

# (relation_type, 人物, note) —— 无向关系脚本内自动按 id 归一
RELATIONS = [
    ("advisor-student", "Alonzo Church", "博士导师（1938），λ 演算发明者，Church–Turing 论题提出者"),
    ("advisor-student", "Robin Gandy", "博士生，Turing 在曼彻斯特大学的学生"),
    ("advisor-student", "Beatrice Worsley", "博士生，加拿大早期计算机科学家"),
    ("colleague", "Max Newman", "剑桥讲师（向 Turing 介绍判定问题），后任曼彻斯特大学计算机实验室主任"),
    ("colleague", "Gordon Welchman", "Bletchley Park Hut 6 负责人，Turing-Welchman Bombe 联合设计"),
    ("collaborator", "Joan Clarke", "Bletchley Park 密码分析员，Turing 短暂未婚妻"),
    ("collaborator", "Jack Good", "Bletchley Park 统计学家，发展 Banburismus 方法"),
    ("colleague", "John von Neumann", "普林斯顿时期相识，曾邀请 Turing 留任 IAS；两人独立提出存储程序架构"),
    ("collaborator", "Claude Shannon", "1943 年贝尔实验室会面，信息论×可计算性的交汇"),
    ("colleague", "Ludwig Wittgenstein", "剑桥同事，数学基础哲学多次辩论"),
    ("colleague", "Christopher Morcom", "少年挚友（非学术同事），1930 年牛结核病早逝，对 Turing 精神世界影响深远"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (TURING,))
    t = cur.fetchone()
    if not t:
        print("⚠ Turing 不在库中")
        return
    pid_t = t[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
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
            print(f"  + 新建(占位): {name}")
        else:
            print(f"  已有: {name} (id={pid})")

        # 方向：导师（Church→Turing）；学生（Turing→Gandy/Worsley）；其余无向按 id 排序
        if rel == "advisor-student":
            if name in ("Alonzo Church",):
                f, t = pid, pid_t
            else:
                f, t = pid_t, pid
        else:
            f, t = sorted([pid_t, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Alan_Turing')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name}")

    conn.commit()
    print(f"\n新建人物(占位): {created} · 新增关系: {added}")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
