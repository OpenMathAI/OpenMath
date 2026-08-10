#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Andrey Kolmogorov 的社会关系（源自提示词 Andrey_Kolmogorov_zh.md）。

关系（提示词「人物关系」节）：
- Luzin       — 博士导师（advisor-student，Luzin→Kolmogorov；鲁金事件使关系复杂）
- Alexandrov  — 终身挚友（colleague，无向）
- Khinchin    — 早期概率论合作者（collaborator，无向）
- Arnold      — 学生，KAM 定理合作者（advisor-student，Kolmogorov→Arnold）
- Gelfand     — 学生，泛函分析大师（advisor-student，Kolmogorov→Gelfand）
- Sinai       — 学生，动力系统大师，Abel 奖得主（advisor-student，Kolmogorov→Sinai）
- Weyl        — 哥廷根学术交流（colleague，无向）
- Courant     — 哥廷根学术交流（colleague，无向）
- von Neumann — 同时代全才型对手（rival，无向）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
别名：Israel Gelfand -> I.M. Gelfand（库中名）
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
KOLMOGOROV = "Andrey Kolmogorov"

NAME_ALIAS = {
    "Israel Gelfand": "I.M. Gelfand",
}

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "Nikolai Luzin", "博士导师，莫斯科数学学派创始人；1936『鲁金事件』使关系蒙上阴影"),
    ("colleague", "Pavel Alexandrov", "终身挚友，同门师兄，莫斯科学派双璧"),
    ("collaborator", "Aleksandr Khinchin", "早期概率论合作者，Khinchin-Kolmogorov 定律"),
    ("advisor-student", "Vladimir Arnold", "最杰出学生之一，KAM 定理共同创立者"),
    ("advisor-student", "Israel Gelfand", "学生，泛函分析大师"),
    ("advisor-student", "Yakov Sinai", "学生，动力系统与遍历理论大师，Abel 奖得主"),
    ("colleague", "Hermann Weyl", "1930 年哥廷根访问期间学术交流"),
    ("colleague", "Richard Courant", "1930 年哥廷根访问对象"),
    ("rival", "John von Neumann", "同时代全才型对手，概率论与动力系统均有基础贡献"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (KOLMOGOROV,))
    k = cur.fetchone()
    if not k:
        print("⚠ Kolmogorov 不在库中")
        return
    pid_k = k[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
        lookup = NAME_ALIAS.get(name, name)
        pid = by_en.get(norm(lookup))
        if pid is None:
            pid = by_zh.get(norm(lookup))
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

        # 方向：有向（Luzin 是导师→Kolmogorov；学生是 Kolmogorov→学生）；无向按 id 排序
        if rel == "advisor-student":
            if name == "Nikolai Luzin":
                f, t = pid, pid_k
            else:
                f, t = pid_k, pid
        else:
            f, t = sorted([pid_k, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Andrey_Kolmogorov')",
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
