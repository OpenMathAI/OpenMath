#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建 economics 提示词批次 manifest（prompt_manifest_20th.json / _21th.json）。

数据源：
  economics_list_data.DATA        年份/姓名(EN,ZH)/国籍
  presentations/pages/*/metadata.json  qid/label/title
  greatminds 库 people            既有记录（按 QID→归一化名 匹配）
  chemist/prompt_manifest.json    BGM 曲库与主色板（轮转预分配）

用法：python3 build_manifest.py
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from economics_list_data import DATA  # noqa: E402

sys.path.insert(0, str(ROOT.parent / "MySQL"))
from db_mysql import get_conn  # noqa: E402


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.lower())


# ---------------------------------------------------------------- pages 元数据
pages = ROOT / "presentations" / "pages"
page_meta: dict[str, dict] = {}  # dir -> meta
label_map: dict[str, tuple[str, str, str]] = {}  # norm(label/name) -> (dir, century, qid)

for century in ("20th_century", "21th_century"):
    for d in sorted((pages / century).iterdir()):
        if not d.is_dir():
            continue
        meta = json.loads((d / "metadata.json").read_text(encoding="utf-8"))
        page_meta[d.name] = meta
        for key in (meta.get("label"), meta.get("name")):
            if key and norm(key) not in label_map:
                label_map[norm(key)] = (d.name, century, meta.get("qid"))

# ---------------------------------------------------------------- 数据库既有记录
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id, name_en, qid, has_social_data FROM people")
db_rows = cur.fetchall()
conn.close()

db_by_qid = {r[2]: r for r in db_rows if r[2]}
db_by_norm: dict[str, tuple] = {}
for r in db_rows:
    db_by_norm.setdefault(norm(r[1]), r)

# ---------------------------------------------------------------- BGM 曲库 / 主色板（取自 chemist manifest）
chem = json.loads((ROOT.parent / "chemist" / "prompt_manifest.json").read_text(encoding="utf-8"))
bgm_paths: dict[str, str] = {}
colors: list[str] = []
for b in chem["batches"]:
    for p in b["people"]:
        bgm_paths.setdefault(p["bgm"], p["bgm_path"])
        if p["main_color"] not in colors:
            colors.append(p["main_color"])
bgm_cycle = list(bgm_paths.keys())

# ---------------------------------------------------------------- DATA → 页面目录匹配
alias = {
    # DATA name_en(norm) -> 页面目录名（自动匹配失败时手工指路）
}

unmatched: list[str] = []
people: list[dict] = []
for i, year in enumerate(sorted(DATA)):
    cit_en, cit_zh, laureates = DATA[year]
    for (ne, nz, ctry) in laureates:
        hit = label_map.get(norm(ne)) or (alias.get(norm(ne)) and label_map.get(alias[norm(ne)]))
        if not hit:
            unmatched.append(f"{year} {ne}")
            continue
        d, century, qid = hit
        meta = page_meta[d]
        # 数据库记录：优先 QID，其次归一化名
        rec = db_by_qid.get(qid) if qid else None
        if rec is None:
            rec = db_by_norm.get(norm(ne))
        name_en = (rec[1] if rec else (meta.get("label") or meta.get("name") or d.replace("_", " ")))
        people.append({
            "name": name_en,
            "name_zh": nz,
            "dir": d,
            "year": year,
            "century": century,
            "country": ctry,
            "citation_en": cit_en if "||" not in cit_en else "",
            "citation_zh": cit_zh if "||" not in cit_zh else "",
            "db_id": rec[0] if rec else None,
            "db_name_en": rec[1] if rec else None,
            "db_qid": rec[2] if rec else None,
            "db_social": int(rec[3] or 0) if rec else 0,
            "qid": qid,
            "bgm": bgm_cycle[i % len(bgm_cycle)],
            "bgm_path": bgm_paths[bgm_cycle[i % len(bgm_cycle)]],
            "main_color": colors[i % len(colors)],
        })

if unmatched:
    print("UNMATCHED（需补 alias）:")
    for u in unmatched:
        print(" ", u)
    sys.exit(1)

# ---------------------------------------------------------------- 按世纪拆分、5 人一批
out_files = {}
for tag, lo, hi in (("20th", 1969, 2000), ("21th", 2001, 2025)):
    sub = sorted([p for p in people if lo <= p["year"] <= hi], key=lambda p: (p["year"], p["dir"]))
    batches = []
    for k in range(0, len(sub), 5):
        grp = sub[k:k + 5]
        n = k // 5 + 1
        batches.append({
            "batch": f"econ{tag}-batch-{n:02d}",
            "mode": "prompt+db",
            "people": grp,
        })
    out = ROOT / f"prompt_manifest_{tag}.json"
    out.write_text(json.dumps(
        {"total": len(sub), "batches": batches}, ensure_ascii=False, indent=1), encoding="utf-8")
    out_files[tag] = (out, len(batches))
    print("wrote:", out, "people:", len(sub), "batches:", len(batches))

# 一致性自检：QID 唯一 / dir 唯一 / BGM·主色覆盖
allq = [p["qid"] for p in people if p["qid"]]
alld = [p["dir"] for p in people]
print("总人数:", len(people), "QID重复:", len(allq) - len(set(allq)), "目录重复:", len(alld) - len(set(alld)))
