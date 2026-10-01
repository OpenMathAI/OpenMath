#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补录化学诺奖得主的 award_laureate 行（Nobel Prize in Chemistry, award_id=23）。

口径对齐 medic/literature/economics 的 backfill_awards_2026.py：
share_type 按当年得主人数（1 人=独享，多人=共享）；source='yaml'；幂等 INSERT IGNORE。
数据源：nobel_chemistry_citations.json（1901–2025，200 条，Sharpless 两度获奖）。
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from db_mysql import get_conn  # noqa: E402

ALIAS = {
    "Alan MacDiarmid": "Alan G. MacDiarmid",
    "Dorothy Hodgkin": "Dorothy Crowfoot Hodgkin",
}

conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id FROM awards WHERE name_en='Nobel Prize in Chemistry'")
award_id = cur.fetchone()[0]
print("award_id =", award_id)

data = json.load(open(ROOT / "nobel_chemistry_citations.json"))
year_n = Counter(r["year"] for r in data)

inserted = skipped = 0
for r in data:
    en = ALIAS.get(r["name"], r["name"])
    cur.execute("SELECT id FROM people WHERE name_en=%s", (en,))
    row = cur.fetchone()
    if row is None:
        print(f"!! 未匹配到 people: {en} ({r['year']})")
        continue
    pid = row[0]
    n = year_n[r["year"]]
    share = "独享" if n == 1 else "共享"
    note = f"Nobel Prize in Chemistry {r['year']}" + ("" if n == 1 else f"（{n} 名得主共享）")
    cur.execute(
        "INSERT IGNORE INTO award_laureate(person_id, award_id, year, share_type, source, note) "
        "VALUES (%s,%s,%s,%s,'yaml',%s)",
        (pid, award_id, r["year"], share, note))
    if cur.rowcount:
        inserted += 1
    else:
        skipped += 1
conn.commit()
print(f"inserted={inserted} skipped(existing)={skipped}")

cur.execute("SELECT COUNT(*) FROM award_laureate WHERE award_id=%s", (award_id,))
print("total Nobel Chemistry rows:", cur.fetchone()[0])
