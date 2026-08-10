#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Kurt Gödel 的社会关系（源自提示词 Kurt_Godel_zh.md 第 4.5 步，规范 §二十）。

Gödel 已有 3 条关系（von Neumann/Weyl/Weil 的 IAS 同事，由他们立传时建），本脚本补足其余：
- Hans Hahn          — 博士导师（advisor-student，Hahn→Gödel）【占位】
- Albert Einstein    — 同事（colleague）：IAS 最亲密的朋友【在库 id=349】
- Oskar Morgenstern  — 同事（colleague）：IAS 同事，入籍听证会救场【在库 id=353】
- Moritz Schlick     — 对话者（colleague）：维也纳学派领袖【占位】
- Rudolf Carnap      — 同事（colleague）：维也纳学派【占位】
- Karl Menger        — 同事（colleague）：维也纳大学同事【占位】
- Alan Turing        — 思想传承（collaborator）：受不完备性定理启发【在库 id=9】
- Alonzo Church      — 对话者（collaborator）：λ 演算【在库 id=381】
- Paul Cohen         — 完成者（collaborator）：forcing 证明 CH 独立【在库 id=113】
- Adele Gödel        — 夫妻（spouse）：妻子【占位】

缺失人物（5 人）先建占位（has_biography=0），note 加「[材料待展开]」。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
GODEL = "Kurt Gödel"

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "Hans Hahn", "博士导师（1929），维也纳学派核心成员"),
    ("colleague", "Albert Einstein", "IAS 最亲密的朋友，'我去办公室的唯一理由是能和 Gödel 一起走回家'"),
    ("colleague", "Oskar Morgenstern", "IAS 同事，1948 入籍听证会与 Einstein 一起保护 Gödel"),
    ("colleague", "Moritz Schlick", "维也纳学派领袖，Gödel 的思想对话者（1936 年被学生枪杀）"),
    ("colleague", "Rudolf Carnap", "维也纳学派成员，逻辑实证主义代表（Gödel 未接受其立场）"),
    ("colleague", "Karl Menger", "维也纳大学同事，数学俱乐部组织者"),
    ("collaborator", "Alan Turing", "思想传承：不完备性定理启发 Turing 定义可计算性"),
    ("collaborator", "Alonzo Church", "对话者：λ 演算与可计算性平行研究，Church–Turing 论题"),
    ("collaborator", "Paul Cohen", "完成者：1963 用 forcing 证明连续统假设独立于 ZFC，完成 Gödel 开创的工作"),
    ("spouse", "Adele Gödel", "妻子，舞厅舞女出身；Gödel 晚年唯一信任为其准备食物的人"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (GODEL,))
    t = cur.fetchone()
    if not t:
        print("⚠ Gödel 不在库中")
        return
    pid_g = t[0]

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

        # 方向：导师（Hahn→Gödel）；其余无向按 id 排序
        if rel == "advisor-student":
            f, t = pid, pid_g
        else:
            f, t = sorted([pid_g, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Kurt_Godel')",
            (f, t, rel, MARKER + note),
        )
        if cur.rowcount:
            added += 1
            print(f"    → {rel}: {name}")

    conn.commit()
    print(f"\n新建人物(占位): {created} · 新增关系: {added}（另含 3 条已有同事关系幂等跳过）")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
