#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""review medal_list_allinone/turing_beamer/turing_cross_reference.md 时发现的数据库修正。

修复项：
1. Hinton 缺 FRS（图灵+诺奖+FRS 三料，文档结论提及但正文缺失）→ 补 FRS 2020
2. Berners-Lee 缺千禧科技奖 2004（文档 §图灵+千禧科技奖）→ 补 Millennium Technology Prize 2004

幂等：INSERT IGNORE。
"""
from db_mysql import get_conn

FIXES = [
    ("Geoffrey Hinton", "Fellow of the Royal Society", 2020, "Hinton 2020 年当选英国皇家学会院士"),
    ("Tim Berners-Lee", "Millennium Technology Prize", 2004, "千禧科技奖（Millennium Technology Prize）"),
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
            "INSERT IGNORE INTO award_laureate(person_id, award_id, year, note, source) VALUES (%s,%s,%s,%s,'turing_cross_reference review')",
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
