#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取并生成诺贝尔文学奖得主清单 md 文档。

数据来源：英文维基百科「List of Nobel laureates in Literature」。
产出：presentations/Nobel_Literature_Laureates_20th_21st_Century.md

表格结构（与物理学奖不同）：
  Year | Image | Name（含生卒年） | Country & Language | Citation
  年份之间还有 colspan=5 的分隔行需跳过。
"""
from __future__ import annotations

import re
import sys
import html as H
from pathlib import Path

import requests
from bs4 import BeautifulSoup

WIKI_PAGE = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Literature'
OUT = Path(__file__).parent / 'presentations' / 'Nobel_Literature_Laureates_20th_21st_Century.md'
# 本地缓存（requests 被 403 限流时，可用 curl 预先下载）
CACHE = Path('/tmp/nobel_lit.html')


def fetch_html() -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'}
    try:
        r = requests.get(WIKI_PAGE, headers=headers, timeout=60)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        if CACHE.exists():
            print(f'! requests 失败（{e}），改用本地缓存 {CACHE}', file=sys.stderr)
            return CACHE.read_text(encoding='utf-8')
        raise


def text(c) -> str:
    return re.sub(r'\s+', ' ', H.unescape(c.get_text(' ', strip=True))).strip()


def parse(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    tbl = soup.find_all('table', class_='wikitable')[0]
    rows = tbl.find_all('tr')

    laureates: list[dict] = []
    pending_year = 0
    cur_year = None

    for tr in rows:
        cells = tr.find_all(['td', 'th'])
        if not cells:
            continue

        # 跳过分隔行（跨整行的空单元格）
        if len(cells) == 1 and int(cells[0].get('colspan', 1) or 1) >= 4:
            continue

        year = None
        name = ''
        url = ''
        country_lang = ''

        for c in cells:
            t = text(c)
            a = c.find('a', href=True)

            # 年份单元格：纯 4 位数字
            if re.match(r'^\d{4}$', t):
                year = int(t)
                rs = int(c.get('rowspan', 1) or 1)
                pending_year = rs - 1
                cur_year = year
                continue

            # 图片/File 链接单元格 → 跳过
            if a and 'File:' in a.get('href', ''):
                continue

            # 人名单元格：含 /wiki/ 人物链接
            if a and '/wiki/' in a.get('href', '') and not name:
                href = a['href']
                if href.startswith('http'):
                    url = href
                else:
                    url = 'https://en.wikipedia.org' + href
                # 去掉姓名后附带的生卒年括号
                name = re.sub(r'\s*\([^)]*\)\s*$', '', t).strip()
                continue

            # 国家 / 语言单元格
            if t and not country_lang and not re.match(r'^\d{4}$', t):
                # "France ( French )" → "France (French)"
                country_lang = re.sub(r'\(\s*', '(', re.sub(r'\s*\)', ')', t))

        if year is None and pending_year > 0:
            year = cur_year
            pending_year -= 1

        if year and name and url:
            laureates.append({'year': year, 'name': name, 'url': url,
                              'country_lang': country_lang})

    return laureates


def write_md(laureates: list[dict]) -> None:
    # 去重（文学奖目前无重复得主，防御性处理）
    seen: set[str] = set()
    unique: list[dict] = []
    for d in laureates:
        key = d['url']
        if key not in seen:
            seen.add(key)
            unique.append(d)

    c20 = [d for d in unique if d['year'] <= 2000]
    c21 = [d for d in unique if d['year'] > 2000]

    lines = []
    lines.append('# 诺贝尔文学奖得主（20 / 21 世纪）\n')
    lines.append('> 本清单收录 1901–2025 年诺贝尔文学奖得主（共 %d 位）。\n' % len(unique))
    lines.append('> 数据来源：英文维基百科「List of Nobel laureates in Literature」。\n')
    lines.append('> 世纪划分：1901–2000 归 20 世纪，2001–2025 归 21 世纪。\n')

    for label, subset, span in (
        ('20 世纪（1901–2000）', c20, '20 世纪'),
        ('21 世纪（2001–2025）', c21, '21 世纪'),
    ):
        lines.append('\n## %s（共 %d 位）\n' % (label, len(subset)))
        lines.append('\n| 年份 | 姓名 | 国家 / 语言 |')
        lines.append('|:--:|------|------|')
        for d in subset:
            link = '[%s](%s)' % (d['name'], d['url']) if d['url'] else d['name']
            lines.append('| %d | %s | %s |' % (d['year'], link, d['country_lang'] or '—'))

    lines.append('\n')
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print('wrote:', OUT)
    print('20世纪:', len(c20), '21世纪:', len(c21), '合计:', len(unique))


def main() -> int:
    html = fetch_html()
    laureates = parse(html)
    write_md(laureates)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
