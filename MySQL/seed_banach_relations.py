#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Stefan Banach 的社会关系（源自提示词 Stefan_Banach_zh.md 第 4.5 步，规范 §二十）。

关系（8 条）：
- Hugo Steinhaus      — 导师/发现者（advisor-student，Steinhaus→Banach）【在库 id=341】
- Stanisław Mazur     — 博士生/合作者（advisor-student，Banach→Mazur）【占位】
- Stanisław Ulam      — 同事（colleague）：Lwów 学派，后 Los Alamos【占位】
- Juliusz Schauder    — 合作者（collaborator）：Schauder 不动点定理，1943 被纳粹杀害【占位】
- Alfred Tarski       — 合作者（collaborator）：Banach–Tarski 悖论共同提出者【占位】
- Andrey Kolmogorov   — 同事（colleague）：苏联占领期访问 Lwów【在库 id=5】
- Sergei Sobolev      — 同事（colleague）：苏联占领期与战后联系【在库 id=44】
- Władysław Orlicz    — 同事（colleague）：Lwów 学派核心成员，Orlicz 空间【占位】

缺失人物（5 人）先建占位（has_biography=0），note 加「[材料待展开]」。
"""
import re
import unicodedata

from db_mysql import get_conn

MARKER = "[材料待展开] "
BANACH = "Stefan Banach"

RELATIONS = [
    ("advisor-student", "Hugo Steinhaus", "发现者（1916 公园长椅偶遇）与非正式导师；终生合作者，共同创办《Studia Mathematica》"),
    ("advisor-student", "Stanisław Mazur", "博士生与最重要合作者；苏格兰咖啡馆问题集联合提出者（问题 153 活鹅奖励）"),
    ("colleague", "Stanisław Ulam", "Lwów 学派核心成员；后赴 Los Alamos，与 von Neumann 发明 Monte Carlo 方法"),
    ("collaborator", "Juliusz Schauder", "Lwów 学派核心成员，Schauder 不动点定理与拓扑度共同发明者；1943 年被纳粹盖世太保杀害"),
    ("collaborator", "Alfred Tarski", "Banach–Tarski 悖论共同提出者（1924）；后成为 20 世纪最重要的逻辑学家之一"),
    ("colleague", "Andrey Kolmogorov", "苏联占领期（1939–1941）访问 Lwów，与 Banach 建立专业联系"),
    ("colleague", "Sergei Sobolev", "苏联数学家，占领期间与战后均与 Banach 保持联系"),
    ("colleague", "Władysław Orlicz", "Lwów 学派核心成员，Orlicz 空间以他命名"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE name_en=%s", (BANACH,))
    t = cur.fetchone()
    if not t:
        print("⚠ Banach 不在库中")
        return
    pid_b = t[0]

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

        # 方向：导师（Steinhaus→Banach）；学生（Banach→Mazur）；其余无向按 id 排序
        if rel == "advisor-student":
            if name == "Hugo Steinhaus":
                f, t = pid, pid_b
            else:
                f, t = pid_b, pid
        else:
            f, t = sorted([pid_b, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Stefan_Banach')",
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
