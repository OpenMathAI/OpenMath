#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 manifest 生成分批：29 批 × 5 人提示词（+关系入库），第 30 批 = 7 人仅关系入库。"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
man = json.loads((HERE / "prompt_manifest.json").read_text(encoding="utf-8"))
people = man["people"]

# 按人名去重（Bardeen 双年），保持年份顺序
seen = set()
uniq = []
for p in people:
    if p["name_en"] in seen:
        continue
    seen.add(p["name_en"])
    uniq.append(p)

need_prompt = [p for p in uniq if p["need_prompt"]]
rel_only = [p for p in uniq if (not p["need_prompt"]) and p["need_relations"]]
print("need_prompt:", len(need_prompt), "rel_only:", len(rel_only))

batches = []
BATCH = 5
for i in range(0, len(need_prompt), BATCH):
    batches.append(need_prompt[i:i + BATCH])
batches.append(rel_only)

out = []
for bi, b in enumerate(batches, 1):
    members = []
    for p in b:
        members.append(dict(
            name_en=p["name_en"], name_zh=p["name_zh"], year=p["year"],
            nationality=p["nationality"], dir=p["dir"], qid=p["qid"],
            need_prompt=p["need_prompt"], need_relations=p["need_relations"],
            page=str(Path("presentations/20th_century/20th_century") / p["dir"] / "page.md"),
            prompt=str(Path("presentations/20th_century") / p["dir"] / (p["dir"] + "_zh.md")),
            yaml=str(Path("MySQL/data") / (p["dir"].replace("/", "_") + ".yaml")),
        ))
    out.append(dict(batch=bi, members=members))

(HERE / "prompt_batches_2026.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
)
print("batches:", len(out), "sizes:", [len(b["members"]) for b in out])
