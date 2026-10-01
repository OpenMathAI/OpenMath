#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补录 232 位医学诺奖得主的 award_laureate 行（Nobel Prize in Physiology or Medicine, award_id=24）。

口径对齐 peace/backfill_awards_2026.py：share_type 按当年得主人数
（1 人=独享，多人=共享）；source='yaml'；幂等 INSERT IGNORE。
数据源：medicine_list_data.py DATA（年份 → (理由en, 理由zh, [(姓名en, 姓名zh, 国籍)])）。
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "medic"))
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from medicine_list_data import DATA  # noqa: E402
from db_mysql import get_conn  # noqa: E402

conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id FROM awards WHERE name_en='Nobel Prize in Physiology or Medicine'")
award_id = cur.fetchone()[0]
print("award_id =", award_id)

inserted = skipped = 0
for y, (cite_en, cite_zh, laureates) in DATA.items():
    n = len(laureates)
    for (en, zh, country) in laureates:
        cur.execute("SELECT id FROM people WHERE name_en=%s", (en,))
        row = cur.fetchone()
        if row is None:
            print(f"!! 未匹配到 people: {en} ({y})")
            continue
        pid = row[0]
        share = "独享" if n == 1 else "共享"
        note = f"Nobel Prize in Physiology or Medicine {y}" + ("" if n == 1 else f"（{n} 名得主共享）")
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

# 终检
cur.execute("SELECT COUNT(*) FROM award_laureate WHERE award_id=%s", (award_id,))
print("total Nobel Medicine rows:", cur.fetchone()[0])
