#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补录 140 位和平奖得主的 award_laureate 行（Nobel Peace Prize, award_id=857）。

口径：share_type 按当年得主人数（1 人=独享，多人=共享）；source='yaml'；
幂等 INSERT IGNORE，与既有 5 行（Pauling/King/ICRC×3）不冲突。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "peace"))
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from peace_list_data import DATA  # noqa: E402
from db_mysql import get_conn  # noqa: E402

ALIAS = {
    "Lord Boyd-Orr": "John Boyd Orr",
    "John Raleigh Mott": "John Mott",
    "United Nations Children's Fund (UNICEF)": "United Nations Children's Fund",
    "Wangari Muta Maathai": "Wangari Maathai",
}

# DATA name_en -> 当年得主人数
YEAR_N = {y: len(l) for y, (e, z, l) in DATA.items()}

m20 = json.load(open(ROOT / "prompt_manifest.json"))
m21 = json.load(open(ROOT / "prompt_manifest_21.json"))

conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id FROM awards WHERE name_en='Nobel Peace Prize'")
award_id = cur.fetchone()[0]

inserted = skipped = 0
for m in (m20, m21):
    for p in m["people"]:
        en = ALIAS.get(p["name"], p["name"])
        cur.execute("SELECT id FROM people WHERE name_en=%s", (en,))
        pid = cur.fetchone()[0]
        for y in p["years"]:
            share = "独享" if YEAR_N[y] == 1 else "共享"
            note = f"Nobel Peace Prize {y}" + ("" if YEAR_N[y] == 1 else f"（{YEAR_N[y]} 名得主共享）")
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
print("total Nobel Peace Prize rows:", cur.fetchone()[0])
