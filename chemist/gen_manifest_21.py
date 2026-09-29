#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 21 世纪 chem-batch 分配清单 prompt_manifest_21.json：64 位按年代 5 人/批（末批 4 人）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
db_map = json.loads((ROOT / "prompt_db_map_21.json").read_text(encoding="utf-8"))
ma20 = json.loads((ROOT / "prompt_manifest.json").read_text(encoding="utf-8"))

# 复用 20 世纪的 BGM 文件映射（从其批次记录中收集曲目->路径）
BGM = {}
for b in ma20["batches"]:
    for p in b["people"]:
        if p.get("bgm") and p.get("bgm_path"):
            BGM.setdefault(p["bgm"], p["bgm_path"])
print("可用曲目:", len(BGM))

# 年代序 64 人（已按年份序）
ORDER = [
    "William Standish Knowles", "Ryōji Noyori", "Karl Barry Sharpless",
    "John Fenn", "Koichi Tanaka", "Kurt Wüthrich",
    "Peter Agre", "Roderick MacKinnon",
    "Aaron Ciechanover", "Avram Hershko", "Irwin Rose",
    "Yves Chauvin", "Robert H. Grubbs", "Richard R. Schrock",
    "Roger D. Kornberg", "Gerhard Ertl",
    "Osamu Shimomura", "Martin Chalfie", "Roger Y. Tsien",
    "Venkatraman Ramakrishnan", "Thomas A. Steitz", "Ada Yonath",
    "Richard F. Heck", "Ei-ichi Negishi", "Akira Suzuki",
    "Dan Shechtman",
    "Robert Lefkowitz", "Brian Kobilka",
    "Martin Karplus", "Michael Levitt", "Arieh Warshel",
    "Eric Betzig", "Stefan Hell", "William E. Moerner",
    "Tomas Lindahl", "Paul L. Modrich", "Aziz Sancar",
    "Jean-Pierre Sauvage", "Fraser Stoddart", "Ben Feringa",
    "Jacques Dubochet", "Joachim Frank", "Richard Henderson",
    "Frances Arnold", "George P. Smith", "Greg Winter",
    "John B. Goodenough", "M. Stanley Whittingham", "Akira Yoshino",
    "Emmanuelle Charpentier", "Jennifer Doudna",
    "Benjamin List", "David W.C. MacMillan",
    "Carolyn Bertozzi", "Morten P. Meldal",
    "Moungi Bawendi", "Louis E. Brus", "Alexey Ekimov",
    "David Baker", "Demis Hassabis", "John M. Jumper",
    "Susumu Kitagawa", "Richard Robson", "Omar M. Yaghi",
]
assert set(ORDER) == set(db_map), (
    set(ORDER) ^ set(db_map)
)

PALETTE = ["#1E3A5F", "#16324F", "#0E4D64", "#123C5B", "#0F4C5C", "#14324F",
           "#283593", "#372A75", "#46356B", "#52307C", "#2A3468", "#37548D",
           "#0B5351", "#175E54", "#146B3A", "#1E5631", "#1E6B52", "#2F5D50",
           "#7A1E28", "#8A1E2D", "#A63A2B", "#9E2B25", "#7E1E23", "#5B2A86"]

track_names = list(BGM.keys())
batches = []
n_batch = (len(ORDER) + 4) // 5
for i in range(n_batch):
    chunk = ORDER[i * 5:(i + 1) * 5]
    people = []
    for j, name in enumerate(chunk):
        info = db_map[name]
        db = info["db"] if isinstance(info["db"], dict) else None
        track = track_names[(i * 5 + j) % len(track_names)]
        people.append({
            "name": name,
            "dir": info["dir"],
            "year": info["year"],
            "db_id": db["id"] if db else None,
            "db_name_en": db["name_en"] if db else None,
            "db_qid": db["qid"] if db else None,
            "db_social": db["social"] if db else 0,
            "bgm": track,
            "bgm_path": BGM[track],
            "main_color": PALETTE[(i * 5 + j) % len(PALETTE)],
        })
    batches.append({"batch": f"chem21-batch-{i + 1:02d}", "mode": "prompt+db", "people": people})

out = {"total": len(ORDER), "batches": batches}
(ROOT / "prompt_manifest_21.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("批次数:", len(batches))
for b in batches:
    print(b["batch"], [p["name"] for p in b["people"]])
