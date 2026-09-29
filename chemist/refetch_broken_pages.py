#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新抓取被 Wikipedia 限流损坏（'too many requests'）的 page.md。"""
import json
import time
from pathlib import Path

import fetch_20th_century_pages as f20

OUT_ROOT = f20.OUT_ROOT

# 目录名 -> (维基标题, 中文名, 获奖年份)
BROKEN = [
    ("Adolf_Windaus", "Adolf Windaus", 1928),
    ("Alan_MacDiarmid", "Alan MacDiarmid", 2000),
    ("George_Andrew_Olah", "George Andrew Olah", 1994),
    ("Herbert_C._Brown", "Herbert C. Brown", 1979),
    ("John_Howard_Northrop", "John Howard Northrop", 1946),
    ("Leopold_Ružička", "Leopold Ružička", 1939),
    ("Paul_Flory", "Paul Flory", 1974),
    ("Robert_Burns_Woodward", "Robert Burns Woodward", 1965),
    ("Wendell_Meredith_Stanley", "Wendell Meredith Stanley", 1946),
]

for dirname, title, year in BROKEN:
    d = OUT_ROOT / dirname
    assert d.exists(), f"missing dir {d}"
    # 校验确实是损坏页
    md = (d / "page.md").read_text(encoding="utf-8", errors="ignore")
    assert "too many requests" in md.lower(), f"{dirname} 未损坏，跳过"
    # 删除损坏产物，保留目录
    for f in ("page.md", "metadata.json", "page.html", "images.txt"):
        p = d / f
        if p.exists():
            p.unlink()
    print(f"▶ 重新抓取 {dirname}")
    f20.process_one(title, title, year)
    time.sleep(2)

print("done")
