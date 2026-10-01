#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补录 99 位经济学奖得主的 award_laureate 行（Nobel Memorial Prize in Economic Sciences, award_id=26）。

口径对齐 medic/backfill_awards_2026.py：share_type 按当年得主人数
（1 人=独享，多人=共享）；source='yaml'；幂等 INSERT IGNORE。
数据源：economics_list_data.py DATA（1969–2025，99 条）。
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "economics"))
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from economics_list_data import DATA  # noqa: E402
from db_mysql import get_conn  # noqa: E402

# 名单姓名 → 库内规范名（people.name_en）
ALIAS = {
    "Alvin E. Roth": "Alvin Eliot Roth",
    "Gary Becker": "Gary S. Becker",
    "John Forbes Nash Jr.": "John Forbes Nash",
    "Paul Romer": "Paul M. Romer",
    "Robert Lucas, Jr.": "Robert Lucas",
    "W. Arthur Lewis": "Arthur Lewis",
}

conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id FROM awards WHERE name_en='Nobel Memorial Prize in Economic Sciences'")
award_id = cur.fetchone()[0]
print("award_id =", award_id)

inserted = skipped = 0
for y, (cite_en, cite_zh, laureates) in DATA.items():
    n = len(laureates)
    for (en, zh, country) in laureates:
        en = ALIAS.get(en, en)
        cur.execute("SELECT id FROM people WHERE name_en=%s", (en,))
        row = cur.fetchone()
        if row is None:
            print(f"!! 未匹配到 people: {en} ({y})")
            continue
        pid = row[0]
        share = "独享" if n == 1 else "共享"
        note = f"Nobel Memorial Prize in Economic Sciences {y}" + ("" if n == 1 else f"（{n} 名得主共享）")
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, year, share_type, source, note) "
            "VALUES (%s,%s,%s,%s,'yaml',%s)",
            (pid, award_id, y, share, note))
        if cur.rowcount:
            inserted += 1
        else:
            skipped += 1
conn.commit()
print(f"inserted={inserted} skipped(existing)={skipped}")

cur.execute("SELECT COUNT(*) FROM award_laureate WHERE award_id=%s", (award_id,))
print("total Nobel Economics rows:", cur.fetchone()[0])
