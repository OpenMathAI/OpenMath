#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Emmy Noether 的社会关系（源自提示词 Emmy_Noether_zh.md）。

关系（提示词「人物关系」节 + 诺特学派）：
- Max Noether     — 父亲（parent-child，Max→Noether）
- Paul Gordan     — 博士导师（advisor-student，Gordan→Noether）
- Ernst Fischer   — 影响者（advisor-student，Fischer→Noether，非正式导师）
- David Hilbert   — 最坚定支持者，争取教职（colleague，无向）
- Felix Klein     — 邀请者（colleague，无向）
- van der Waerden — 学生（advisor-student，Noether→vdW）
- Alexandrov      — 莫斯科合作者（collaborator，无向）
- Albert Einstein — 高度评价、亲撰悼词（colleague，无向）
- 诺特学派学生：Deuring / Hermann / Witt / Fitting / Levitzki（advisor-student）

缺失人物先建占位（has_biography=0），关系 note 加「[材料待展开]」标识。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
NOETHER = "Emmy Noether"

# (relation_type, 人物, note)
RELATIONS = [
    ("parent-child", "Max Noether", "父亲，著名代数几何学家，埃尔朗根大学教授"),
    ("advisor-student", "Paul Gordan", "博士导师，『不变量之王』；名义导师，计算风格"),
    ("advisor-student", "Ernst Fischer", "影响其转向抽象方法的数学家"),
    ("colleague", "David Hilbert", "最坚定的支持者，为她争取哥廷根教职"),
    ("colleague", "Felix Klein", "与 Hilbert 一起邀请她来哥廷根"),
    ("advisor-student", "Bartel Leendert van der Waerden", "『诺特男孩』中最著名，《代数学》(Moderne Algebra) 作者"),
    ("collaborator", "Pavel Alexandrov", "莫斯科时期合作者，拓扑与代数交叉"),
    ("colleague", "Albert Einstein", "高度评价，1935 年亲撰悼词"),
    ("advisor-student", "Max Deuring", "诺特学派成员，算术代数几何"),
    ("advisor-student", "Grete Hermann", "诺特首位博士生（1925 年答辩）"),
    ("advisor-student", "Ernst Witt", "诺特学派成员，Witt 向量"),
    ("advisor-student", "Hans Fitting", "诺特学派成员，Fitting 引理"),
    ("advisor-student", "Jacob Levitzki", "诺特学派成员，Levitzki 定理"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (NOETHER,))
    noether = cur.fetchone()
    if not noether:
        print("⚠ Noether 不在库中")
        return
    pid_n = noether[0]

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

        # 方向：有向（父→子 / 师→生）
        if rel == "parent-child":
            f, t = pid, pid_n                 # Max Noether → Noether
        elif rel == "advisor-student":
            if name in ("Paul Gordan", "Ernst Fischer"):
                f, t = pid, pid_n             # 导师 → Noether
            else:
                f, t = pid_n, pid             # Noether → 学生
        else:
            f, t = sorted([pid_n, pid])       # 无向

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Emmy_Noether')",
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
