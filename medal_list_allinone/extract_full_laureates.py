#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 pages/ 四大奖页面提取完整得主名单，交叉比对生成 laurate_cross.md"""
import re
from pathlib import Path

PAGES = Path(__file__).parent / "pages"


def clean(x):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', x)).strip()


def extract_table_names(html):
    """提取 wikitable 中所有得主名（合并多列）"""
    names = set()
    tables = re.findall(r'<table[^>]*class="wikitable[^"]*"[^>]*>(.*?)</table>', html, re.S | re.I)
    for t in tables:
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S | re.I)
        for r in rows:
            cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S | re.I)
            # 得主名通常是含链接的词组（排除表头 Year/ICM 等）
            for c in cells:
                txt = clean(c)
                if re.match(r'^[A-Z][a-z]+(\s[A-Z][a-zA-Z\-\'\.]+)+$', txt) and txt not in (
                        'Year', 'ICM location', 'Medalists', 'Affiliation', 'Reasons',
                        'Laureates', 'Recipients', 'Winner', 'Winners'):
                    names.add(txt)
    return names


def extract_list_items(html):
    """提取有序/无序列表中的得主名"""
    names = set()
    for m in re.finditer(r'<li[^>]*>(.*?)</li>', html, re.S | re.I):
        txt = clean(m.group(1))
        if re.match(r'^[A-Z][a-z]+(\s[A-Z][a-zA-Z\-\'\.]+){1,4}$', txt):
            names.add(txt)
    return names


def extract_all(html):
    return extract_table_names(html) | extract_list_items(html)


def main():
    sections = {
        "Fields": "math_top/Fields Medal/index.html",
        "Wolf": "math_top/Wolf Prize in Mathematics/index.html",
        "Abel": "math_top/Abel Prize/index.html",
        "Chern": "math_top/Chern Medal/index.html",
        "Turing": "computer/Turing Award/index.html",
        "Nevanlinna": "math_icm/IMU Abacus Medal/index.html",
        "Gauss": "math_icm/Carl Friedrich Gauss Prize/index.html",
        "Godel": "math_icm/Gödel Prize/index.html",
        "Knuth": "computer/Knuth Prize/index.html",
        "Hamming": "computer/IEEE Richard W. Hamming Medal/index.html",
        "Neumann": "computer/IEEE John von Neumann Medal/index.html",
        "Shannon": "computer/Claude E. Shannon Award/index.html",
        "Marconi": "computer/Marconi Prize/index.html",
    }
    data = {}
    for name, rel in sections.items():
        p = PAGES / rel
        if not p.exists():
            print("MISSING:", rel)
            continue
        html = p.read_text(encoding="utf-8", errors="ignore")
        data[name] = extract_all(html)
        print("%-12s %3d laureates" % (name, len(data[name])))

    # 交叉：对每对奖项求交集
    out = ["# 奖项得主交叉表（从 pages/ 提取）\n"]
    keys = list(data.keys())
    out.append("## 得主数一览")
    for k in keys:
        out.append("  %s: %d" % (k, len(data[k])))
    out.append("")
    out.append("## 两两交叉（数学四大奖 + Turing 重点）")
    focus = ["Fields", "Wolf", "Abel", "Chern", "Turing"]
    for i, a in enumerate(focus):
        for b in focus[i + 1:]:
            inter = sorted(data.get(a, set()) & data.get(b, set()))
            if inter:
                out.append("### %s ∩ %s  (%d)" % (a, b, len(inter)))
                out.append("  " + " · ".join(inter))
                out.append("")
    out.append("## Turing ∩ 其它")
    for b in ["Godel", "Knuth", "Hamming", "Neumann", "Shannon", "Marconi", "Nevanlinna"]:
        inter = sorted(data.get("Turing", set()) & data.get(b, set()))
        if inter:
            out.append("### Turing ∩ %s  (%d)" % (b, len(inter)))
            out.append("  " + " · ".join(inter))
            out.append("")
    (Path(__file__).parent / "laurate_cross.md").write_text("\n".join(out), encoding="utf-8")
    print("wrote laurate_cross.md")


if __name__ == "__main__":
    main()
