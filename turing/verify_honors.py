#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对照本地 Wikipedia infobox Awards 逐项核验 HONORS 正确性。
对每个 HONORS 奖项，在对应 Wikipedia Awards 原文中搜索关键词，
报告「原文缺失」项（可能误标）与「原文新增」项（可能遗漏）。
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_turing as gt

PAGES = os.path.join(HERE, "pages")

# 奖项关键词 → 应出现在 Awards 原文的匹配词
AWARD_KEYS = {
    "诺贝尔":      ["Nobel"],
    "京都":        ["Kyoto"],
    "沃尔夫":      ["Wolf"],
    "哥德尔":      ["Gödel", "Godel"],
    "阿贝尔":      ["Abel"],
    "香农":        ["Shannon"],
    "日本国际":    ["Japan Prize"],
    "内万林纳":    ["Nevanlinna"],
    "EATCS":       ["EATCS"],
    "马可尼":      ["Marconi"],
    "冯":          ["von Neumann", "Neumann"],
    "千禧":        ["Millennium"],
    "国家科学奖章": ["National Medal of Science"],
    "科学院院士":   ["National Academy of Sciences", "NAS Member", "Member of the National Academy"],
    "皇家学会院士": ["Royal Society", "ForMemRS", "FRS"],
    "加拿大总督":   ["Governor General"],
    "鲁梅哈特":     ["Rumelhart"],
}


def get_awards(year, name):
    p = os.path.join(PAGES, year, name, "index.html")
    if not os.path.exists(p):
        return ""
    html = open(p, encoding="utf-8", errors="ignore").read()
    m = re.search(r'<th[^>]*>\s*Awards\s*</th>\s*<td[^>]*class="infobox-data[^"]*"[^>]*>(.*?)</td>',
                  html, re.S | re.I)
    seg = m.group(1) if m else ""
    seg = re.sub(r'<[^>]+>', ' ', seg)
    seg = re.sub(r'\s+', ' ', seg)
    return seg


def find_person(name):
    for ep, lst in gt.DATA.items():
        for p in lst:
            if p[0] == name:
                return ep.split("-")[-1], name
    return None, None


def main():
    problems = []
    for name, honors in gt.HONORS.items():
        # 用年份目录定位页面（DATA 里没存年份目录，用 cmd 匹配页面）
        year, _ = find_person(name)
        # 直接遍历 pages 找匹配页面
        found = None
        for y in os.listdir(PAGES):
            ydir = os.path.join(PAGES, y)
            if not os.path.isdir(ydir):
                continue
            for n in os.listdir(ydir):
                if n.lower().replace(" ", "") == name.lower().replace(" ", ""):
                    found = (y, n)
                    break
            if found:
                break
        if not found:
            problems.append((name, "NO_PAGE", ""))
            continue
        y, n = found
        aw = get_awards(y, n)
        # 1) 检查 HONORS 中的奖项在原文是否出现
        for key, pats in AWARD_KEYS.items():
            if key in honors:
                hit = any(re.search(pat, aw, re.I) for pat in pats)
                if not hit:
                    problems.append((name, "MISSING_IN_WIKI: %s" % key, honors))
    # 输出
    print("=== HONORS 中在 Wikipedia 找不到的奖项 ===")
    if not problems:
        print("  （无）")
    for name, kind, h in problems:
        print("  [%s] %s" % (name, kind))
    print()
    # 2) 汇总输出每人 Awards 便于人工复核
    print("=== 全量 Awards 提取（截取前 260 字符）===")
    for name in gt.HONORS:
        y, n = None, name
        for yy in os.listdir(PAGES):
            ydir = os.path.join(PAGES, yy)
            if not os.path.isdir(ydir):
                continue
            for nn in os.listdir(ydir):
                if nn.lower().replace(" ", "") == name.lower().replace(" ", ""):
                    y, n = yy, nn
                    break
            if y:
                break
        if not y:
            print("### %s  (无页面)" % name)
            print()
            continue
        aw = get_awards(y, n)
        print("### %s (%s)" % (name, y))
        print("HONORS: %s" % gt.HONORS[name])
        print("WIKI  : %s" % aw[:260])
        print()


if __name__ == "__main__":
    main()
