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
from pathlib import Path

import requests
from bs4 import BeautifulSoup

WIKI_PAGE = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Chemistry'
OUT = Path(__file__).parent / 'presentations' / 'Nobel_Chemistry_Laureates_20th_21st_Century.md'


def fetch_html() -> str:
    headers = {'User-Agent': 'OpenMathAI/1.0 (educational use)'}
    r = requests.get(WIKI_PAGE, headers=headers, timeout=60)
    r.raise_for_status()
    return r.text


def parse(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    tbl = soup.find_all('table', class_='wikitable')[0]
    rows = tbl.find_all('tr')[2:]  # 跳过表头两行

    def text(c):
        return re.sub(r'\s+', ' ', H.unescape(c.get_text(' ', strip=True))).strip()

    def is_year_cell(c):
        return bool(re.match(r'^\d{4}$', text(c)))

    def get_name_url(c):
        if c.find('img'):
            return None, ''
        a = c.find('a', href=True)
        if not a:
            return None, ''
        href = a['href']
        if '/wiki/' not in href or 'File:' in href:
            return None, ''
        t = text(c)
        if not t or re.match(r'^\d{4}$', t) or t.startswith('"'):
            return None, ''
        url = href if href.startswith('http') else 'https://en.wikipedia.org' + href
        return t, url

    def get_country(c):
        if not c.find('img'):
            return ''
        a = c.find('a', href=True)
        if not a:
            return ''
        href = a['href']
        if '/wiki/' not in href or 'File:' in href:
            return ''
        return text(c)

    laureates = []
    pending_year = 0
    pending_country = 0
    cur_year = None
    cur_country = ''

    for tr in rows:
        cells = tr.find_all(['td', 'th'])
        year = None
        name = ''
        url = ''
        country = ''

        for c in cells:
            if is_year_cell(c):
                year = int(text(c))
                rs = int(c.get('rowspan', 1) or 1)
                pending_year = rs - 1
                cur_year = year
            elif get_name_url(c)[0]:
                name, url = get_name_url(c)
            elif get_country(c):
                country = get_country(c)
                rs = int(c.get('rowspan', 1) or 1)
                pending_country = rs - 1
                cur_country = country

        if year is None and pending_year > 0:
            year = cur_year
            pending_year -= 1
        if not country and pending_country > 0:
            country = cur_country
            pending_country -= 1

        if year and name:
            laureates.append({'year': year, 'name': name, 'url': url, 'country': country})

    return laureates


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
