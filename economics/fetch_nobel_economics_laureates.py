#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取并生成诺贝尔经济学奖得主清单 md 文档。

数据来源：英文维基百科「List of Nobel laureates in Economics」
（Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel，1969 年起颁发）。
产出：presentations/Nobel_Economics_Laureates_20th_21st_Century.md

维基主表为 8 列（Year | Portrait | Laureate | Country | Rationale | Education |
Institution | Key contributions），且大量使用 rowspan（共享年份），此处用
rowspan 占位法逐行展开。

用法：
  python3 fetch_nobel_economics_laureates.py
"""
from __future__ import annotations

import html as H
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

WIKI_PAGE = "List of Nobel laureates in Economics"
OUT = Path(__file__).parent / "presentations" / "Nobel_Economics_Laureates_20th_21st_Century.md"

NCOL = 8  # Year | Portrait | Laureate | Country | Rationale | Education | Institution | Contributions


def fetch_html() -> str:
    # python-requests 指纹被 Wikipedia CDN 拦截（403），统一用 curl 抓取
    cache = Path("/tmp/econ_list.html")
    if cache.exists() and cache.stat().st_size > 100_000:
        print("use cached:", cache)
        return cache.read_text(encoding="utf-8")
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(WIKI_PAGE, safe='')}"
    proc = subprocess.run(
        ["curl", "-sL", "--fail", "--max-time", "120", "-A", USER_AGENT, url],
        capture_output=True, text=True, timeout=180,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"curl exit={proc.returncode} for {url}")
    return proc.stdout


def parse(html: str) -> list[dict]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    tbl = max(tables, key=lambda t: len(t.find_all("tr")))
    rows = tbl.find_all("tr")[1:]  # 跳过表头

    rowspans = [0] * NCOL
    active: list = [None] * NCOL  # 各列当前 rowspan 跨行单元格（供续行取值）
    results: list[dict] = []

    cur_year = 0

    for tr in rows:
        cells = tr.find_all(["td", "th"])
        row = [None] * NCOL

        ci, col = 0, 0
        while col < NCOL:
            if rowspans[col] > 0:
                rowspans[col] -= 1
                row[col] = active[col]  # 续行沿用跨行单元格的值
                col += 1
                continue
            if ci >= len(cells):
                col += 1
                continue
            cell = cells[ci]
            rs = int(cell.get("rowspan", 1) or 1)
            cs = int(cell.get("colspan", 1) or 1)
            if cs > 1:
                # 本表无预期中的 colspan；防御性按首列填充
                if col < NCOL:
                    row[col] = cell
                ci += 1
                col += cs
                continue
            row[col] = cell
            if rs > 1:
                rowspans[col] += rs - 1
                active[col] = cell
            ci += 1
            col += 1

        def text(cell) -> str:
            if cell is None:
                return ""
            return re.sub(r"\s+", " ", H.unescape(cell.get_text(" ", strip=True))).strip()

        # 年份：col 0
        if row[0] is not None and re.match(r"^\d{4}$", text(row[0])):
            cur_year = int(text(row[0]))

        # 姓名：col 2；国籍：col 3（多国籍时链接各自独立，按 " / " 连接）
        name_cell = row[2]
        if name_cell is None:
            continue
        name = text(name_cell)
        # 清洗姓名中的生卒年括号，如 "Ragnar Frisch (1895–1973)" / "Daron Acemoglu (b. 1967)"
        name = re.sub(r"\s*\((?:\d{4}\s*[–-]\s*(?:\d{4})?|b\.\s*\d{4})\)$", "", name).strip()
        if not name or cur_year == 0:
            continue

        country_cell = row[3]
        if country_cell is not None:
            links = [re.sub(r"\s+", " ", H.unescape(a.get_text(" ", strip=True))).strip()
                     for a in country_cell.find_all("a", href=True)]
            links = [l for l in links if l]
            country = " / ".join(links) if links else text(country_cell)
        else:
            country = ""

        a = name_cell.find("a", href=True)
        url = ""
        if a:
            href = a["href"]
            if href.startswith("/wiki/"):
                url = "https://en.wikipedia.org" + href
            elif href.startswith("./"):  # REST API 渲染的 HTML 用 ./Title 相对链接
                url = "https://en.wikipedia.org/wiki/" + href[2:]

        results.append({"year": cur_year, "name": name, "url": url, "country": country})

    return results


def write_md(laureates: list[dict]) -> None:
    c20 = [d for d in laureates if d["year"] <= 2000]
    c21 = [d for d in laureates if d["year"] > 2000]

    lines = []
    lines.append("# 诺贝尔经济学奖得主（20 / 21 世纪）\n")
    lines.append("> 本清单收录 1969–2025 年诺贝尔经济学奖得主（共 %d 位）。\n" % len(laureates))
    lines.append("> 该奖项全称为「瑞典央行纪念阿尔弗雷德·诺贝尔经济学奖」"
                 "（Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel），"
                 "1969 年首次颁发，非诺贝尔遗嘱所设五大奖。\n")
    lines.append("> 数据来源：英文维基百科「List of Nobel laureates in Economics」。\n")
    lines.append("> 世纪划分：1969–2000 归 20 世纪，2001–2025 归 21 世纪。\n")

    for label, section, data in (
        ("20 世纪（1969–2000，共 %d 位）" % len(c20), "20 世纪", c20),
        ("21 世纪（2001–2025，共 %d 位）" % len(c21), "21 世纪", c21),
    ):
        lines.append("\n## %s\n" % label)
        lines.append("\n| 年份 | 姓名 | 国籍 |")
        lines.append("|:--:|------|:--:|")
        for d in data:
            link = "[%s](%s)" % (d["name"], d["url"]) if d["url"] else d["name"]
            lines.append("| %d | %s | %s |" % (d["year"], link, d["country"] or "—"))

    lines.append("\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("wrote:", OUT)
    print("20世纪:", len(c20), "21世纪:", len(c21), "合计:", len(laureates))


def main() -> int:
    html = fetch_html()
    laureates = parse(html)
    if not laureates:
        print("ERROR: parse 出 0 行，表格结构可能已变化", file=__import__("sys").stderr)
        return 1
    write_md(laureates)
    # 顺手输出便于核对
    Path("/tmp/econ_parsed.json").write_text(
        json.dumps(laureates, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
