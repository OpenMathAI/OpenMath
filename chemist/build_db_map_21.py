#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 21 世纪化学诺奖得主 -> greatminds 库存量记录对照清单 prompt_db_map_21.json。
目录名从 pages/INDEX.md 解析（- 年份 — [姓名](目录/page.md)）。
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "MySQL"))
from db_mysql import get_conn

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "presentations" / "21th_century" / "pages" / "INDEX.md"

# 1) 从 INDEX.md 解析 (年份, 姓名, 目录名)
rows = []
pat = re.compile(r"^- (\d{4}) — \[(.+)\]\((.+)/page\.md\)")
for line in INDEX.read_text(encoding="utf-8").splitlines():
    m = pat.match(line.strip())
    if m:
        rows.append((int(m.group(1)), m.group(2).strip(), m.group(3).strip()))
print("INDEX 解析:", len(rows), "行")

# 2) 去重（Sharpless 两度获奖，目录唯一）
seen: dict[str, tuple] = {}
for year, name, d in rows:
    if name not in seen:
        seen[name] = (year, d)
    else:
        y0, _ = seen[name]
        seen[name] = (min(y0, year), d)
people = [(n, y, d) for n, (y, d) in seen.items()]
print("去重后人数:", len(people))


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\s_'.()\u00b7,\-]", "", s)
    return s.lower()


conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id, name_en, qid, has_social_data, has_biography FROM people")
by_exact = {}
by_norm: dict[str, list] = {}
for pid, en, qid, soc, bio in cur.fetchall():
    if en:
        rec = {"id": pid, "name_en": en, "qid": qid, "social": soc, "bio": bio}
        by_exact[en] = rec
        by_norm.setdefault(norm(en), []).append(rec)

out = {}
missing = []
for name, year, d in people:
    hits = [by_exact[name]] if name in by_exact else by_norm.get(norm(name), [])
    if len(hits) == 1:
        out[name] = {"dir": d, "year": year, "db": hits[0]}
    elif len(hits) == 0:
        out[name] = {"dir": d, "year": year, "db": None}
        missing.append(name)
    else:
        out[name] = {"dir": d, "year": year, "db": hits}
        missing.append(name + " (多记录!)")

Path(ROOT / "prompt_db_map_21.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
)
print("无库记录:", len(missing))
for m in missing:
    print(" -", m)
print("\n== 已有库记录（须复用/回填 QID）==")
for name, year, d in people:
    db = out[name]["db"]
    if isinstance(db, dict):
        print(f"  {name} ({year}) -> #{db['id']} {db['name_en']} qid={db['qid']} social={db['social']}")
    elif isinstance(db, list):
        print(f"  {name} ({year}) -> 多记录: {db}")
