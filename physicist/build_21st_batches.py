#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""21 世纪批次清单：68 人（2001–2025），提示词+关系入库；Hinton 已完整入库跳过。
生成 prompt_manifest_21st.json 与 prompt_batches_21st.json（14 批 × 5，末批 3）。"""
import json
import re
import sys
from pathlib import Path

ROOT = Path("/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist")
sys.path.insert(0, str(ROOT))
from generate_21st_century_list import NAME_ZH  # noqa: E402

PAGES = ROOT / "presentations" / "21th_century" / "21st_century"
idx = (PAGES / "INDEX.md").read_text(encoding="utf-8")

people = []
for m in re.finditer(r"- (\d{4}) — \[(.+?)\]\((.+?)/page\.md\)", idx):
    year, name, d = int(m.group(1)), m.group(2).strip(), m.group(3)
    pp = PAGES / d / "page.md"
    qid = None
    if pp.exists():
        mm = re.search(r'^wikidata:\s*"?([Qq]\d+)"?', pp.read_text(encoding="utf-8"), re.M)
        qid = mm.group(1) if mm else None
    people.append(dict(year=year, name_en=name, name_zh=NAME_ZH.get(name, name),
                       dir=d, qid=qid, nationality=None))

# Hinton 已在图灵奖侧完整入库（has_social_data=1），其余 67 人需入库
for p in people:
    p["need_prompt"] = True
    p["need_relations"] = p["name_en"] != "Geoffrey Hinton"

noq = [p["name_en"] for p in people if not p["qid"]]
print("people:", len(people), "need_relations:", sum(p["need_relations"] for p in people), "missing qid:", noq)

(ROOT / "prompt_manifest_21st.json").write_text(
    json.dumps(dict(total=len(people), people=people), ensure_ascii=False, indent=1), encoding="utf-8"
)

BATCH = 5
batches = [people[i:i + BATCH] for i in range(0, len(people), BATCH)]
out = []
for bi, b in enumerate(batches, 1):
    members = []
    for p in b:
        members.append(dict(
            name_en=p["name_en"], name_zh=p["name_zh"], year=p["year"], qid=p["qid"],
            need_prompt=p["need_prompt"], need_relations=p["need_relations"],
            page=f"presentations/21th_century/21st_century/{p['dir']}/page.md",
            prompt=f"presentations/21th_century/{p['dir']}/{p['dir']}_zh.md",
            yaml=f"MySQL/data/{p['dir']}.yaml",
        ))
    out.append(dict(batch=bi, members=members))
(ROOT / "prompt_batches_21st.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
)
print("batches:", len(out), "sizes:", [len(b["members"]) for b in out])
