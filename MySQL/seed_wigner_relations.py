#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""梳理 Eugene Wigner 的社会关系（源自提示词 Eugene_Wigner_zh.md「第 4.5 步」）。

关系清单：
- 导师：Michael Polanyi（博士导师）、László Rátz（中学数学启蒙）、Richard Becker（柏林学术顾问）
- 同事/合作：Hermann Weyl（群论双子星）、John von Neumann（匈牙利天才群）、David Hilbert（哥廷根助手）
- 学生：John Bardeen（唯一两获诺奖的学生）
- 姻亲：Paul Dirac（妹夫，妹妹 Margit 嫁 Dirac）
- 曼哈顿计划伙伴：Leó Szilárd
- 诺奖共同体：Maria Goeppert Mayer、J. Hans D. Jensen（1963 共同得主）

不在库中的人物先建占位（has_biography=0），关系 note 加「[材料待展开]」前缀。
"""
import re
import unicodedata
from db_mysql import get_conn

MARKER = "[材料待展开] "
WIGNER = "Eugene Wigner"
WIGNER_ID = 352

# (relation_type, 人物, note)
RELATIONS = [
    ("advisor-student", "Michael Polanyi", "柏林 Kaiser Wilhelm 研究所时期的博士导师，推荐其入行"),
    ("advisor-student", "László Rátz", "布达佩斯 Fasori 中学的数学老师，早年启蒙者"),
    ("advisor-student", "Richard Becker", "柏林时期随其研习量子力学与统计物理"),
    ("colleague", "Hermann Weyl", "共同把群论引入物理；对称性理论的双子星"),
    ("colleague", "John von Neumann", "匈牙利「火星人」天才群体；普林斯顿同事"),
    ("colleague", "David Hilbert", "哥廷根时期任其助手，深受数学物理熏陶"),
    ("advisor-student", "John Bardeen", "学生，史上唯一两获诺贝尔物理学奖（晶体管、超导）"),
    ("spouse", "Paul Dirac", "姻亲：妹妹 Margit (Manci) 嫁 Dirac，Dirac 为妹夫"),
    ("colleague", "Leó Szilárd", "曼哈顿计划伙伴；共同促成爱因斯坦–西拉德信"),
    ("co-honored", "Maria Goeppert Mayer", "1963 诺贝尔物理学奖共同得主（核壳层结构理论）"),
    ("co-honored", "J. Hans D. Jensen", "1963 诺贝尔物理学奖共同得主（核壳层结构理论）"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM people WHERE id=%s", (WIGNER_ID,))
    if not cur.fetchone():
        print("⚠ Wigner (id=352) 不在库中")
        return

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id FROM occupations WHERE name_en='physicist'")
    occ_id = cur.fetchone()[0]

    created = 0
    added = 0
    for rel, name, note in RELATIONS:
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
            print(f"  已有: {name}")

        # 方向：导师（Polanyi/Rátz/Becker→Wigner）、学生（Wigner→Bardeen）
        if rel == "advisor-student":
            if name == "John Bardeen":
                f, t = WIGNER_ID, pid
            else:
                f, t = pid, WIGNER_ID
        else:
            f, t = sorted([WIGNER_ID, pid])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'立传-Eugene_Wigner')",
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
