#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 pages/ 离线 Wikipedia 页面提取各奖项得主名单（年份: 得主），
输出 laureates_extract.md 供人工核对 all_cross_reference.md。
"""
import os
import re
import json
from pathlib import Path

PAGES = Path(__file__).parent / "pages"


def text_of(html):
    """粗略转纯文本（去标签）"""
    html = re.sub(r'<style.*?</style>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<script.*?</script>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<[^>]+>', ' ', html)
    return re.sub(r'\s+', ' ', html)


def laureate_lines(html):
    """匹配 '年份：A, B, C' 或列表中的得主行"""
    text = text_of(html)
    # 形如 1936: Lars Ahlfors ... / 1936 – Ahlfors, Douglas
    lines = []
    for m in re.finditer(
            r'(19|20)\d{2}\s*[:–\-]\s*([A-Z][A-Za-z\'\-\. ]+(?:[,;&]|and|，)[A-Za-z\'\-\. ,&;]+)',
            text):
        year = m.group(1)
        names = m.group(2)
        lines.append((year, names[:120]))
    return lines


def main():
    out = []
    for cat in sorted(os.listdir(PAGES)):
        cdir = PAGES / cat
        if not cdir.is_dir():
            continue
        for entry in sorted(os.listdir(cdir)):
            edir = cdir / entry
            if not edir.is_dir():
                continue
            idx = edir / "index.html"
            if not idx.exists():
                continue
            html = idx.read_text(encoding="utf-8", errors="ignore")
            text = text_of(html)
            # infobox 里字段名 + 正文年份列表
            out.append("## %s/%s" % (cat, entry))
            # 得主年份行
            found = 0
            for y, names in laureate_lines(html):
                out.append("  %s: %s" % (y, names))
                found += 1
                if found > 12:
                    break
            if found == 0:
                out.append("  (未匹配到年份:得主 模式)")
            out.append("")
    (Path(__file__).parent / "laureates_extract.md").write_text("\n".join(out), encoding="utf-8")
    print("wrote laureates_extract.md")


if __name__ == "__main__":
    main()
