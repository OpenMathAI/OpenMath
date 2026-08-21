#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 nobel_chemistry_citations.json 读取 20 世纪诺贝尔化学奖得主（含获奖理由），
参考数学家侧文档形式，生成含「获奖理由 / 立传 / Review」列的结构化 md。

先运行 fetch_nobel_citations.py 生成 nobel_chemistry_citations.json，再运行本脚本。
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "nobel_chemistry_citations.json"
OUT = ROOT / "presentations" / "20th_century" / "OpenChemist_20th_Century_Nobel_Laureates.md"

# 已立传的化学家（姓名需与获奖者名单精确匹配）。
# 新增立传时在此补充姓名。
BIOGRAPHIES_DONE = set()

# 已完成 Review（两轮事实核查）的化学家（姓名需与获奖者名单精确匹配）。
# 完成两轮 Review 后在此补充姓名。
REVIEWS_DONE = set()

# 获奖者英文名 → 中文名（诺贝尔化学奖得主常用中译）。
NAME_ZH = {}

# 获奖理由（Citation）英文原文 → 中文翻译（诺贝尔奖官方获奖理由中译）。
CITATION_ZH = {}


def _norm_citation(s: str) -> str:
    """规范化获奖理由文本：折叠空白、去掉标点前空格，使其与字典 key 对齐。"""
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([.,;:])", r"\1", s)
    return s


def main() -> int:
    if not SRC.exists():
        print(f"✗ 缺少获奖理由数据：{SRC}")
        print("  请先运行：python3 fetch_nobel_citations.py")
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    # 仅保留 20 世纪（1901–2000）
    rows = [r for r in data if r.get("year") and r["year"] <= 2000]
    rows.sort(key=lambda r: r["year"])

    total_items = len(rows)
    names = [r["name"] for r in rows]
    unique_people = set(names)

    # 两度获奖者
    cnt = Counter(names)
    double = {k for k, v in cnt.items() if v > 1}

    # 女性获奖者（20 世纪）
    women = set()

    # 国籍分布
    country_counter = Counter(r["country"] for r in rows)

    # 立传 / Review 状态
    done_count = sum(1 for r in rows if r["name"] in BIOGRAPHIES_DONE)
    review_count = sum(1 for r in rows if r["name"] in REVIEWS_DONE)

    lines: list[str] = []
    lines.append("# 20 世纪诺贝尔化学奖得主 — OpenChemist 名录\n")
    lines.append(
        "> **本名录收录 1901–2000 年诺贝尔化学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从 van 't Hoff 的化学动力学到 Sanger 的基因测序：一百年间，化学奖见证了现代化学从分子结构走向生命科学的全过程。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Chemistry」。\n"
        % (total_items, len(unique_people))
    )
    lines.append("---\n")

    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review |")
    lines.append("|:--:|------|------|------|:--:|:--:|")
    for r in rows:
        name = r["name"]
        zh = NAME_ZH.get(name)
        name_display = f"{name} ({zh})" if zh else name
        country = r["country"] or "—"
        citation_en = _norm_citation(r["citation"])
        citation = CITATION_ZH.get(citation_en, citation_en).replace("|", "/")  # 转义表格竖线
        bio = "✅" if name in BIOGRAPHIES_DONE else "🔲"
        review = "✅" if name in REVIEWS_DONE else "🔲"
        lines.append("| %d | %s | %s | %s | %s | %s |" % (r["year"], name_display, country, citation, bio, review))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：1901–2000")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    lines.append("- **已立传**：%d 位（%s）" % (done_count, "、".join(sorted(BIOGRAPHIES_DONE)) if BIOGRAPHIES_DONE else "暂无"))
    lines.append("- **已 Review**：%d 位（%s）" % (review_count, "、".join(sorted(REVIEWS_DONE)) if REVIEWS_DONE else "暂无"))
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)) + "（唯一两度获诺贝尔化学奖者）")
    if women:
        w = [x for x in sorted(women) if x in unique_people]
        if w:
            lines.append("- **女性获奖者**（20 世纪）：" + "、".join(w))

    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for c, n in country_counter.most_common():
        lines.append("| %s | %d |" % (c, n))

    lines.append("\n---\n")
    lines.append(
        "\n> **这不是一份排名，而是一部按时间展开的化学历程：每一项获奖都标记着人类对自然认识的一次跃迁。**\n"
    )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    print("已立传:", done_count, "位", "已 Review:", review_count, "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
