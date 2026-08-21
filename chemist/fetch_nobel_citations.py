#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取诺贝尔化学奖获奖理由（Citation），解析 rowspan 表格结构。

输出：nobel_chemistry_citations.json
  [
    {"year": 1901, "name": "Jacobus Henricus van 't Hoff", "country": "Netherlands",
     "citation": "In recognition of ..."},
    ...
  ]
"""
from __future__ import annotations

import html as H
import json
import sys
from pathlib import Path
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "OpenMathAI/1.0 (https://github.com/OpenMathAI/OpenMath; educational use) "
    "python-requests"
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "nobel_chemistry_citations.json"

LIST_PAGE = "List of Nobel laureates in Chemistry"


def fetch_html(session: requests.Session, title: str) -> str:
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
    r = session.get(url, headers={"Accept": "text/html; charset=utf-8"}, timeout=60)
    r.raise_for_status()
    return r.text


def parse_table(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    tbl = soup.find_all("table")[0]
    rows = tbl.find_all("tr")[2:]  # 跳过两行表头

    NCOL = 6  # Year | Image | Name | Country | Citation | Ref
    # rowspans[c] 表示该列还有多少"额外行"被上一个跨行单元格占据
    rowspans = [0] * NCOL
    results: list[dict] = []

    cur_year = None
    cur_country = None
    cur_citation = None

    for tr in rows:
        cells = tr.find_all(["td", "th"])
        row = [None] * NCOL

        ci = 0
        col = 0
        while col < NCOL:
            # 该列被上一行的 rowspan 占据，跳过（不消费 cell）
            if rowspans[col] > 0:
                rowspans[col] -= 1
                col += 1
                continue
            # 单元格已用完，但后续列若仍有 rowspan 则继续递减，否则跳过
            if ci >= len(cells):
                col += 1
                continue
            cell = cells[ci]
            rs = int(cell.get("rowspan", 1) or 1)
            cs = int(cell.get("colspan", 1) or 1)
            text = H.unescape(cell.get_text(" ", strip=True))
            # 填充 colspan 跨越的所有列
            for k in range(cs):
                if col + k < NCOL:
                    row[col + k] = text
            # rowspan：记录未来行占位
            if rs > 1:
                rowspans[col] += rs - 1
            ci += 1
            col += cs

        # 更新当前年度/国籍/获奖理由（若本行提供了新值）
        if row[0]:
            cur_year = row[0]
        if row[3]:
            cur_country = row[3]
        if row[4]:
            cur_citation = row[4].strip('"').strip()

        # 获奖者姓名在第 2 列
        name = (row[2] or "").strip()
        # 过滤未颁奖年份（如 "No award"）
        if name and name.lower() != "no award":
            results.append({
                "year": int(cur_year) if cur_year and cur_year.isdigit() else None,
                "name": name,
                "country": cur_country or "",
                "citation": cur_citation or "",
            })

    return results


def main() -> int:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    html = fetch_html(session, LIST_PAGE)
    results = parse_table(html)
    OUT.write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"抓取 {len(results)} 项，写入 {OUT}")

    # 简要统计
    c20 = [r for r in results if r["year"] and r["year"] <= 2000]
    c21 = [r for r in results if r["year"] and r["year"] > 2000]
    print(f"20世纪: {len(c20)} 项, 21世纪: {len(c21)} 项")
    return 0


if __name__ == "__main__":
    sys.exit(main())
