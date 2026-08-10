#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""review turing_allinone_zh.tex 发现的数据库缺失荣誉补录。

tex 的「其他殊荣」栏包含、但数据库缺失的记录（史实经核实）：
1. John McCarthy   NMS 1990（tex 京都1988+NMS1990）
2. Donald Knuth    NMS 1979（tex 京都1996+NMS1979）
3. Herbert Simon   NMS 1986（tex 诺奖1978+NMS1986）
4. Tony Hoare      IEEE von Neumann 2011（tex 京都2000+冯诺依曼2011）
5. Leslie Lamport  NAS 2011（tex 冯诺依曼2008+NAS2011）
6. Whitfield Diffie FRS 2015（tex 汉明2010+马可尼2000+FRS2015）
7. Robert Metcalfe NMTI 2003（tex 马可尼2003+NMTI，补年份）

幂等：INSERT IGNORE。
"""
from db_mysql import get_conn

FIXES = [
    ("John McCarthy", "National Medal of Science", 1990, "国家科学奖章"),
    ("Donald E. Knuth", "National Medal of Science", 1979, "国家科学奖章"),
    ("Herbert A. Simon", "National Medal of Science", 1986, "国家科学奖章"),
    ("Tony Hoare", "IEEE John von Neumann Medal", 2011, "IEEE 冯·诺依曼奖章"),
    ("Leslie Lamport", "Member of the National Academy of Sciences", 2011, "美国科学院院士"),
    ("Whitfield Diffie", "Fellow of the Royal Society", 2015, "英国皇家学会院士"),
    ("Robert Metcalfe", "National Medal of Technology and Innovation", 2003, "美国国家技术奖章"),
]


def main():
    conn = get_conn()
    cur = conn.cursor()
    added = 0
    for name, award, year, note in FIXES:
        cur.execute("SELECT id FROM people WHERE name_en=%s", (name,))
        p = cur.fetchone()
        cur.execute("SELECT id FROM awards WHERE name_en=%s", (award,))
        a = cur.fetchone()
        if not p or not a:
            print(f"⚠ 缺失: {name} 或 {award}")
            continue
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, year, note, source) VALUES (%s,%s,%s,%s,'turing_allinone_zh.tex review')",
            (p[0], a[0], year, note),
        )
        if cur.rowcount:
            added += 1
            print(f"  + {name}: {award} {year}")
    conn.commit()
    print(f"新增 {added} 条")
    conn.close()


if __name__ == "__main__":
    main()
