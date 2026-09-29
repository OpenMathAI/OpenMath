#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取诺贝尔文学奖获奖理由（Citation），解析 rowspan 表格结构。

输出：nobel_literature_citations.json
  [
    {"year": 1901, "name": "Sully Prudhomme", "country": "France",
     "citation": "in special recognition of ..."},
    ...
  ]
"""
from __future__ import annotations

import html as H
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "nobel_literature_citations.json"

LIST_PAGE = "List of Nobel laureates in Literature"


def fetch_html(title: str) -> str:
    # requests UA 会被 REST API 限流 403，改用 curl（需 -L 跟随 301 重定向）
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
    last_err = None
    for attempt in range(5):
        r = subprocess.run(
            ["curl", "-sL", "-A", USER_AGENT, "-w", "\n%{http_code}", url],
            capture_output=True, text=True, timeout=120,
        )
        body, _, code = r.stdout.rpartition("\n")
        if code == "200" and body.strip():
            return body
        last_err = RuntimeError(f"HTTP {code}")
        wait = 30 * (2 ** attempt)
        print(f"  ! HTTP {code}，{wait}s 后重试…")
        time.sleep(wait)
    raise last_err


def parse_table(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    tbl = soup.find_all("table", class_="wikitable")[0]
    rows = tbl.find_all("tr")[2:]  # 跳过两行表头

    NCOL = 5  # Year | Image | Name | Country & Language | Citation
    rowspans = [0] * NCOL
    results: list[dict] = []

    cur_year = None
    cur_country = None
    cur_citation = None

    for tr in rows:
        cells = tr.find_all(["td", "th"])
        # 跳过灰色分隔行
        if len(cells) == 1 and (cells[0].get("colspan") or ""):
            continue

        row = [None] * NCOL

        ci = 0
        col = 0
        while col < NCOL:
            if rowspans[col] > 0:
                rowspans[col] -= 1
                col += 1
                continue
            if ci >= len(cells):
                col += 1
                continue
            cell = cells[ci]
            rs = int(cell.get("rowspan", 1) or 1)
            cs = int(cell.get("colspan", 1) or 1)
            text = H.unescape(cell.get_text(" ", strip=True))
            for k in range(cs):
                if col + k < NCOL:
                    row[col + k] = text
            if rs > 1:
                rowspans[col] += rs - 1
            ci += 1
            col += cs

        if row[0] and row[0].strip():
            cur_year = row[0].strip()
        if row[3] and row[3].strip():
            cur_country = row[3]
        if row[4] and row[4].strip():
            cur_citation = row[4].strip().strip('"').strip()

        # 姓名在第 2 列（Name）；空行为共享奖延续行
        name = (row[2] or "").strip()
        # 去掉姓名中的生卒年与尾注编号，如 "Sully Prudhomme (1839–1907) [ 3 ]"
        name = re.sub(r"\s*\[\s*\d+\s*\]\s*$", "", name)
        name = re.sub(r"\s*\(\s*\d{4}\s*[–—-][^)]*\)\s*$", "", name).strip()
        if name and name.lower() != "not awarded":
            citation = cur_citation or ""
            # 去掉 citation 尾部脚注编号，如 '... unsayable" [ 124 ]'
            citation = re.sub(r"\s*\[\s*\d+\s*\]\s*$", "", citation).strip()
            results.append({
                "year": int(cur_year) if cur_year and cur_year.isdigit() else None,
                "name": name,
                "country": cur_country or "",
                "citation": citation,
            })

    return results


def main() -> int:
    html = fetch_html(LIST_PAGE)
    results = parse_table(html)
    OUT.write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"抓取 {len(results)} 项，写入 {OUT}")

    c20 = [r for r in results if r["year"] and r["year"] <= 2000]
    c21 = [r for r in results if r["year"] and r["year"] > 2000]
    print(f"20世纪: {len(c20)} 项, 21世纪: {len(c21)} 项")
    return 0


if __name__ == "__main__":
    sys.exit(main())
