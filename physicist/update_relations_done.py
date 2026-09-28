#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 prompt_manifest.json 的 161 位得主全部写入 generate_20th_century_list.py 的
RELATIONS_DONE 集合（幂等替换），并重新生成名录。"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist")
gen = ROOT / "generate_20th_century_list.py"
man = json.loads((ROOT / "prompt_manifest.json").read_text(encoding="utf-8"))
names = sorted({p["name_en"] for p in man["people"]})
print("names:", len(names))

src = gen.read_text(encoding="utf-8")
m = re.search(r"RELATIONS_DONE\s*=\s*\{.*?\n\}", src, re.S)
assert m, "RELATIONS_DONE block not found"
body = "\n".join(f'    "{n}",' for n in names)
new_block = "RELATIONS_DONE = {\n" + body + "\n}"
src = src[: m.start()] + new_block + src[m.end():]
gen.write_text(src, encoding="utf-8")
print("RELATIONS_DONE rewritten")
