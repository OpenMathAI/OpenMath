#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 André Weil 的社会关系（源自提示词 Andre_Weil_zh.md）。

关系（提示词「人物关系」节，12 条）：
- Simone Weil    — 妹妹（parent-child 有向，Weil→Simone；或 sibling——用 parent-child+note 表示血缘）
- Hadamard       — 博士导师（advisor-student，Hadamard→Weil）
- Henri Cartan   — 布尔巴基联合创始人，终生密友（collaborator，无向）
- Chevalley      — 布尔巴基创始人，代数群合作者（collaborator，无向）
- Delsarte       — 布尔巴基创始人（collaborator，无向）
- Dieudonné      — 布尔巴基最狂热拥护者（collaborator，无向）
- Mandelbrojt    — 布尔巴基成员（collaborator，无向）
- de Possel      — 布尔巴基成员（collaborator，无向）
- Deligne        — 学术继承人（advisor-student 非正式，用 collaborator+note 或 advisor-student）
- Einstein/Gödel/von Neumann/Oppenheimer — IAS 同事（colleague，无向）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
WEIL = "André Weil"

# (relation_type, 人物, note)
RELATIONS = [
    ("parent-child", "Simone Weil", "妹妹，20 世纪最重要的哲学家之一；两兄妹代表法国知识界的数学与哲学两个方向"),
    ("advisor-student", "Jacques Hadamard", "博士导师（1928），法国分析大师，素数定理证明者"),
    ("collaborator", "Henri Cartan", "布尔巴基联合创始人，终生密友"),
    ("collaborator", "Claude Chevalley", "布尔巴基创始人之一，代数群理论合作者"),
    ("collaborator", "Jean Delsarte", "布尔巴基创始人之一"),
    ("collaborator", "Jean Dieudonné", "布尔巴基最狂热的拥护者和执行者"),
    ("collaborator", "Szolem Mandelbrojt", "布尔巴基创始成员"),
    ("collaborator", "René de Possel", "布尔巴基创始成员"),
    ("advisor-student", "Pierre Deligne", "学术继承人，1973 证明 Weil 猜想，Fields 奖得主"),
    ("colleague", "Albert Einstein", "IAS 同事"),
    ("colleague", "Kurt Gödel", "IAS 同事"),
    ("colleague", "John von Neumann", "IAS 同事"),
    ("colleague", "J. Robert Oppenheimer", "IAS 同事（Oppenheimer 任所长时期）"),
    ("advisor-student", "Alexander Grothendieck", "代数几何后继者，Étale 上同调建筑师，深受 Weil 猜想推动"),
    ("colleague", "Rolf Nevanlinna", "1939 年芬兰帮助 Weil 脱险（提示词标注谨慎表述）"),
    ("colleague", "Oswald Veblen", "战时帮助 Weil 在美国找到教职"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (WEIL,))
    w = cur.fetchone()
    if not w:
        print("⚠ Weil 不在库中")
        return
    pid_w = w[0]

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
            print(f"  已有: {name}")

        # 方向：导师（Hadamard→Weil）、学生（Weil→Deligne）、兄妹（Weil→Simone）；无向按 id 排序
        if rel == "advisor-student":
            if name == "Jacques Hadamard":
                f, t = pid, pid_w
            else:
                f, t = pid_w, pid
        elif rel == "parent-child":
            f, t = pid_w, pid      # André → Simone（兄弟姐妹用 parent-child+note 表示血缘）
        else:
            f, t = sorted([pid_w, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Andre_Weil')",
            (f, t, rel, MARKER + note),
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
