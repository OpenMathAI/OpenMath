#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取并生成诺贝尔化学奖得主清单 md 文档。

数据来源：英文维基百科「List of Nobel laureates in Chemistry」。
产出：presentations/Nobel_Chemistry_Laureates_20th_21st_Century.md
"""
from __future__ import annotations

import json
import re
import html as H
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

WIKI_PAGE = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Chemistry'
WIKI_TITLE = 'List of Nobel laureates in Chemistry'
OUT = Path(__file__).parent / 'presentations' / 'Nobel_Chemistry_Laureates_20th_21st_Century.md'


def fetch_html() -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0 Safari/537.36',
        'Accept': 'text/html; charset=utf-8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    from urllib.parse import quote
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(WIKI_TITLE, safe='')}"
    last_err = None
    for attempt in range(5):
        try:
            r = requests.get(url, headers=headers, timeout=60)
            r.raise_for_status()
            return r.text
        except requests.HTTPError as e:
            last_err = e
            wait = 10 * (2 ** attempt)
            print(f'  ! HTTP {e.response.status_code}，{wait}s 后重试…')
            time.sleep(wait)
    raise last_err


def parse(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    tbl = soup.find_all('table', class_='wikitable')[0]
    rows = tbl.find_all('tr')[2:]  # 跳过两行表头

    NCOL = 5  # Year | Image | Name | Nationality | Citation
    rowspans = [0] * NCOL
    results: list[dict] = []
    cur_year = None
    cur_country = None

    for tr in rows:
        cells = tr.find_all(['td', 'th'])
        # 跳过灰色分隔行（<tr bgcolor="lightgrey"><td colspan="5"></td></tr>）
        if len(cells) == 1 and (cells[0].get('colspan') or '') == '5':
            continue

        row = [None] * NCOL
        row_cells = [None] * NCOL  # 保存实际 cell 对象，用于提取姓名链接
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
            rs = int(cell.get('rowspan', 1) or 1)
            cs = int(cell.get('colspan', 1) or 1)
            text = H.unescape(cell.get_text(' ', strip=True)).strip()
            for k in range(cs):
                if col + k < NCOL:
                    row[col + k] = text
                    row_cells[col + k] = cell
            if rs > 1:
                rowspans[col] += rs - 1
            ci += 1
            col += cs

        if row[0] and row[0].strip():
            cur_year = row[0].strip()
        if row[3] and row[3].strip():
            cur_country = re.sub(r'\[\s*\d+\s*\]', '', row[3]).strip()

        # 姓名从第 2 列（Name）的 <a> 链接提取
        name = ''
        url = ''
        nc = row_cells[2]
        if nc is not None:
            a = nc.find('a', href=True)
            if a:
                title = (a.get('title') or '').strip()
                text = a.get_text(strip=True)
                if title:
                    # 去掉末尾消歧义后缀，如 "Richard Robson (chemist)" -> "Richard Robson"
                    name = re.sub(r'\s*\([a-z][^)]*\)\s*$', '', title)
                    url = 'https://en.wikipedia.org/wiki/' + title.replace(' ', '_')
                else:
                    name = text

        if name and cur_year and cur_year.isdigit() and name.lower() != 'not awarded':
            results.append({
                'year': int(cur_year),
                'name': name,
                'url': url,
                'country': cur_country or '',
            })

    return results


def write_md(laureates: list[dict]) -> None:
    c20 = [d for d in laureates if d['year'] <= 2000]
    c21 = [d for d in laureates if d['year'] > 2000]

    lines = []
    lines.append('# 诺贝尔化学奖得主（20 / 21 世纪）\n')
    lines.append('> 本清单收录 1901–2025 年诺贝尔化学奖得主（共 %d 位）。\n' % len(laureates))
    lines.append('> 数据来源：英文维基百科「List of Nobel laureates in Chemistry」。\n')
    lines.append('> 世纪划分：1901–2000 归 20 世纪，2001–2025 归 21 世纪。\n')

    lines.append('\n## 20 世纪（1901–2000，共 %d 位）\n' % len(c20))
    lines.append('\n| 年份 | 姓名 | 国籍 |')
    lines.append('|:--:|------|:--:|')
    for d in c20:
        link = '[%s](%s)' % (d['name'], d['url']) if d['url'] else d['name']
        lines.append('| %d | %s | %s |' % (d['year'], link, d['country'] or '—'))

    lines.append('\n## 21 世纪（2001–2025，共 %d 位）\n' % len(c21))
    lines.append('\n| 年份 | 姓名 | 国籍 |')
    lines.append('|:--:|------|:--:|')
    for d in c21:
        link = '[%s](%s)' % (d['name'], d['url']) if d['url'] else d['name']
        lines.append('| %d | %s | %s |' % (d['year'], link, d['country'] or '—'))

    lines.append('\n')
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print('wrote:', OUT)
    print('20世纪:', len(c20), '21世纪:', len(c21), '合计:', len(laureates))


def main() -> int:
    html = fetch_html()
    laureates = parse(html)
    write_md(laureates)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
