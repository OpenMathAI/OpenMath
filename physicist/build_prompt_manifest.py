#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解析名录 + INDEX + metadata QID，生成 prompt_manifest.json 待办清单。"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century")
list_md = (ROOT / "OpenPhysicist_20th_Century_Nobel_Laureates.md").read_text(encoding="utf-8")

rows = []
for line in list_md.splitlines():
    m = re.match(
        r"^\|\s*(\d{4})\s*\|\s*(.+?)\s*\((.+?)\)\s*\|\s*(.+?)\s*\|.*\|\s*(✅|🔲)\s*\|\s*(✅|🔲)\s*\|\s*(✅|🔲)\s*\|$",
        line,
    )
    if m:
        year, name_en, name_zh, nat, bio, rev, rel = m.groups()
        rows.append(
            dict(year=int(year), name_en=name_en.strip(), name_zh=name_zh.strip(),
                 nationality=nat.strip(), bio=bio, review=rev, rel=rel)
        )
print("parsed rows:", len(rows))

idx = (ROOT / "20th_century" / "INDEX.md").read_text(encoding="utf-8")
dirs = {}
for m in re.finditer(r"- (\d{4}) — \[(.+?)\]\((.+?)/page\.md\)", idx):
    year, name, d = int(m.group(1)), m.group(2), m.group(3)
    dirs.setdefault((year, name), d)

unmatched = []
for r in rows:
    d = dirs.get((r["year"], r["name_en"]))
    if not d:
        cands = {k: v for k, v in dirs.items() if k[1] == r["name_en"]}
        d = next(iter(cands.values())) if len(cands) == 1 else None
    r["dir"] = d
    if not d:
        unmatched.append((r["year"], r["name_en"]))
print("unmatched:", unmatched)

for r in rows:
    qid = None
    pp = ROOT / "20th_century" / r["dir"] / "page.md"
    if pp.exists():
        m = re.search(r'^wikidata:\s*"?([Qq]\d+)"?', pp.read_text(encoding="utf-8"), re.M)
        if m:
            qid = m.group(1)
    r["qid"] = qid

BIO_DONE = {
    "Wilhelm Conrad Röntgen", "Hendrik Antoon Lorentz", "Pieter Zeeman",
    "Eugene Paul Wigner", "Kenneth G. Wilson", "Chen Ning Yang", "Tsung-Dao Lee",
    "Wolfgang Pauli", "Werner Karl Heisenberg", "Antoine Henri Becquerel",
    "Pierre Curie", "Marie Curie", "Lord Rayleigh",
    "Philipp Eduard Anton von Lenard", "Joseph John Thomson",
    "Albert Abraham Michelson",
}
REL_DONE = {
    "Wilhelm Conrad Röntgen", "Hendrik Antoon Lorentz", "Pieter Zeeman",
    "Eugene Paul Wigner", "Kenneth G. Wilson", "Chen Ning Yang", "Tsung-Dao Lee",
    "Wolfgang Pauli", "Werner Karl Heisenberg",
}
n_prompt = n_rel = 0
seen = set()
for r in rows:
    r["need_prompt"] = r["name_en"] not in BIO_DONE
    r["need_relations"] = r["name_en"] not in REL_DONE
    if r["name_en"] in seen:
        continue
    seen.add(r["name_en"])
    n_prompt += r["need_prompt"]
    n_rel += r["need_relations"]
print("unique people:", len(seen))
print("need_prompt:", n_prompt, "need_relations:", n_rel)
noq = [r["name_en"] for r in rows if r["need_relations"] and not r["qid"]]
print("missing qid:", len(noq), noq[:10])

out = dict(total=len(rows), need_prompt=n_prompt, need_relations=n_rel, people=rows)
Path(__file__).with_name("prompt_manifest.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
)
print("manifest written")
