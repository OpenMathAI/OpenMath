#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取诺贝尔经济学奖获奖理由（Rationale），解析 rowspan 表格结构。

输出：nobel_economics_citations.json
  [
    {"year": 1969, "name": "Ragnar Frisch (1895–1973)", "country": "Norway",
     "citation": "for having developed and applied dynamic models ..."},
    ...
  ]
"""
from __future__ import annotations

import html as H
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "nobel_economics_citations.json"

LIST_PAGE = "List of Nobel laureates in Economics"

NCOL = 8  # Year | Portrait | Laureate | Country | Rationale | Education | Institution | Contributions


def fetch_html(title: str) -> str:
    # python-requests 指纹被 Wikipedia CDN 拦截，统一用 curl（列表参数、无 shell）
    cache = Path("/tmp/econ_list.html")
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
        proc = subprocess.run(
            ["curl", "-sL", "--fail", "--max-time", "120", "-A", USER_AGENT, url],
            capture_output=True, text=True, timeout=180,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"curl exit={proc.returncode} for {url}")
        return proc.stdout
    except Exception:
        # 抓取失败（限流/网络）时回退到本地缓存，结构与线上 REST API 渲染一致
        if cache.exists() and cache.stat().st_size > 100_000:
            print("fetch failed, use cached:", cache)
            return cache.read_text(encoding="utf-8")
        raise


def _text(cell) -> str:
    if cell is None:
        return ""
    return re.sub(r"\s+", " ", H.unescape(cell.get_text(" ", strip=True))).strip()


def parse_table(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    tbl = max(tables, key=lambda t: len(t.find_all("tr")))
    rows = tbl.find_all("tr")[1:]  # 跳过表头行

    rowspans = [0] * NCOL
    active: list = [None] * NCOL  # 各列当前 rowspan 跨行单元格（供续行取值）
    results: list[dict] = []

    cur_year = 0
    cur_country = None
    cur_citation = None

    for tr in rows:
        cells = tr.find_all(["td", "th"])
        row = [None] * NCOL

        ci, col = 0, 0
        while col < NCOL:
            if rowspans[col] > 0:
                rowspans[col] -= 1
                row[col] = active[col]
                col += 1
                continue
            if ci >= len(cells):
                col += 1
                continue
            cell = cells[ci]
            rs = int(cell.get("rowspan", 1) or 1)
            cs = int(cell.get("colspan", 1) or 1)
            for k in range(cs):
                if col + k < NCOL:
                    row[col + k] = cell
            if rs > 1:
                rowspans[col] += rs - 1
                active[col] = cell
            ci += 1
            col += cs

        if re.match(r"^\d{4}$", _text(row[0])):
            cur_year = int(_text(row[0]))

        country_cell = row[3]
        if country_cell is not None:
            links = [_text(a) for a in country_cell.find_all("a", href=True)]
            links = [l for l in links if l]
            cur_country = " / ".join(links) if links else _text(country_cell)

        cit_cell = row[4]
        if cit_cell is not None and _text(cit_cell):
            cit = _text(cit_cell)
            # 清理尾部引注噪声：" [ 5 ]" / " [ 66 ] [ 67 ]" 与包裹引号
            cit = re.sub(r"(?:\s*\[\s*\d+\s*\])+\s*\"?\s*$", "", cit).strip()
            cit = cit.strip('"“”').strip()
            cur_citation = cit

        name = _text(row[2])
        name = re.sub(r"\s*\((?:\d{4}\s*[–-]\s*(?:\d{4})?|b\.\s*\d{4})\)$", "", name).strip()
        if name and cur_year:
            results.append({
                "year": cur_year,
                "name": name,
                "country": cur_country or "",
                "citation": cur_citation or "",
            })

    return results


def main() -> int:
    html = fetch_html(LIST_PAGE)
    results = parse_table(html)
    OUT.write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"抓取 {len(results)} 项，写入 {OUT}")

    c20 = [r for r in results if r["year"] <= 2000]
    c21 = [r for r in results if r["year"] > 2000]
    print(f"20世纪: {len(c20)} 项, 21世纪: {len(c21)} 项")

    miss = [r["name"] for r in results if not r["citation"]]
    if miss:
        print("⚠ 缺获奖理由:", miss)
    return 0


if __name__ == "__main__":
    sys.exit(main())
