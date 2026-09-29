#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取并生成诺贝尔和平奖得主清单 md 文档。

数据来源：英文维基百科「List of Nobel Peace Prize laureates」。
产出：presentations/Nobel_Peace_Laureates_20th_21st_Century.md

和平奖特点（与生理学或医学奖列表的差异）：
  - 主表列结构为 Year | Laureate(Image, Name) | Country | Citation；
  - 部分得主是组织/机构（如红十字国际委员会），姓名列同样带 wiki 链接；
  - 存在未颁奖年份，以 colspan=4 的「Not awarded ...」行标注，解析时跳过；
  - 共享年份各位得主的 Citation 可能不同（按人对应，非全年份共通）。

用法：
  python3 fetch_nobel_peace_laureates.py
"""
from __future__ import annotations

import html as H
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup

WIKI_PAGE = "List of Nobel Peace Prize laureates"
OUT = Path(__file__).parent / "presentations" / "Nobel_Peace_Laureates_20th_21st_Century.md"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def fetch_html() -> str:
    # 本网络下 python-requests 指纹被 Wikipedia CDN 拦截（403），统一用 curl 抓取。
    # 优先用本地缓存（避免重复请求触发限流）。
    cache = Path("/tmp/peace_list.html")
    if cache.exists() and cache.stat().st_size > 100_000:
        print("use cached:", cache)
        return cache.read_text(encoding="utf-8")
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(WIKI_PAGE, safe='')}"
    for attempt in range(6):
        proc = subprocess.run(
            ["curl", "-sL", "--fail", "--max-time", "120", "-A", USER_AGENT, url],
            capture_output=True, text=True, timeout=180,
        )
        if proc.returncode == 0:
            return proc.stdout
        wait = min(2 ** attempt * 2, 30)
        print(f"curl exit={proc.returncode}，{wait}s 后重试")
        time.sleep(wait)
    raise RuntimeError(f"无法抓取 {url}")


def clean_name(raw: str) -> str:
    """去掉姓名中的生卒年/注释括号，如 'Henry Dunant (1828–1910)'、
    'Institute of International Law (founded 1873)'。"""
    return re.sub(r"\s*\([^)]*\)\s*$", "", raw).strip()


def name_and_title(cell) -> tuple[str, str]:
    """从姓名单元格提取 (显示名, wiki 标题)。REST API HTML 中链接为 ./Title 形式。"""
    a = cell.find("a", href=True)
    title = ""
    if a:
        href = a["href"]
        if href.startswith("./"):
            title = unquote(href[2:]).replace("_", " ").split("#")[0]
        elif "/wiki/" in href:
            title = unquote(href.split("/wiki/")[-1]).replace("_", " ").split("#")[0]
        label = a.get_text(" ", strip=True)
        if label:
            return clean_name(label), title
    return clean_name(cell.get_text(" ", strip=True)), title


def parse(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    tbl = max(tables, key=lambda t: len(t.find_all("tr")))

    NCOL = 5  # Year | Image | Name | Country | Citation
    rowspans = [0] * NCOL
    carry = [None] * NCOL   # 跨行单元格在后续行的延续值
    laureates: list[dict] = []

    for tr in tbl.find_all("tr"):
        cells = tr.find_all(["td", "th"])
        row = [None] * NCOL
        nodes = [None] * NCOL  # 记录每列归属的单元格节点（供姓名列取链接）
        ci, col = 0, 0
        while col < NCOL:
            if rowspans[col] > 0:
                # 该列被上一行的 rowspan 占据：回填延续值
                rowspans[col] -= 1
                row[col] = carry[col]
                col += 1
                continue
            if ci >= len(cells):
                col += 1
                continue
            cell = cells[ci]
            rs = int(cell.get("rowspan", 1) or 1)
            cs = int(cell.get("colspan", 1) or 1)
            text = re.sub(r"\s+", " ", H.unescape(cell.get_text(" ", strip=True))).strip()
            for k in range(cs):
                if col + k < NCOL:
                    row[col + k] = text
                    nodes[col + k] = cell
                    if rs > 1:
                        carry[col + k] = text
            if rs > 1:
                rowspans[col] += rs - 1
            ci += 1
            col += cs

        # 未颁奖年份行：整行被一个 colspan>=4 的「Not awarded ...」占据
        joined = " ".join(x for x in row if x)
        if "not awarded" in joined.lower():
            continue
        if not row[0] or not re.match(r"^\d{4}$", row[0] or ""):
            continue
        name, title = name_and_title(nodes[2]) if nodes[2] else ("", "")
        if not name:
            continue
        laureates.append({
            "year": int(row[0]),
            "name": name,
            "title": title,
            "country": (row[3] or "").strip(),
            "citation": (row[4] or "").strip().strip('"').strip(),
        })

    return laureates


def write_md(laureates: list[dict]) -> None:
    c20 = [d for d in laureates if d["year"] <= 2000]
    c21 = [d for d in laureates if d["year"] > 2000]

    lines = []
    lines.append("# 诺贝尔和平奖得主（20 / 21 世纪）\n")
    lines.append("> 本清单收录 1901–2025 年诺贝尔和平奖得主（共 %d 次获奖，部分年份颁给组织机构）。\n" % len(laureates))
    lines.append("> 数据来源：英文维基百科「List of Nobel Peace Prize laureates」。\n")
    lines.append("> 世纪划分：1901–2000 归 20 世纪，2001–2025 归 21 世纪；未颁奖年份不列行。\n")

    lines.append("\n## 20 世纪（1901–2000，共 %d 次获奖）\n" % len(c20))
    lines.append("\n| 年份 | 获奖者 | 国籍/所在国 |")
    lines.append("|:--:|------|:--:|")
    for d in c20:
        link = f"[{d['name']}](https://en.wikipedia.org/wiki/{d['title'].replace(' ', '_')})" if d["title"] else d["name"]
        lines.append(f"| {d['year']} | {link} | {d['country'] or '—'} |")

    lines.append("\n## 21 世纪（2001–2025，共 %d 次获奖）\n" % len(c21))
    lines.append("\n| 年份 | 获奖者 | 国籍/所在国 |")
    lines.append("|:--:|------|:--:|")
    for d in c21:
        link = f"[{d['name']}](https://en.wikipedia.org/wiki/{d['title'].replace(' ', '_')})" if d["title"] else d["name"]
        lines.append(f"| {d['year']} | {link} | {d['country'] or '—'} |")

    lines.append("\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("wrote:", OUT)
    print("20世纪:", len(c20), "21世纪:", len(c21), "合计:", len(laureates))


def main() -> int:
    html = fetch_html()
    laureates = parse(html)
    if not laureates:
        print("ERROR: parse 出 0 行，表格结构可能已变化", file=sys.stderr)
        return 1
    write_md(laureates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
