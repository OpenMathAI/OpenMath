#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 Nobel_Physics_Laureates_20th_21st_Century.md 提取 20 世纪名单，
去掉 Wikipedia 链接，参考数学家侧文档形式，生成结构化 md。"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "presentations" / "Nobel_Physics_Laureates_20th_21st_Century.md"
OUT = ROOT / "presentations" / "20th_century" / "OpenPhysicist_20th_Century_Nobel_Laureates.md"


def strip_links(text: str) -> str:
    """去掉 markdown 链接 [text](url) -> text"""
    return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)


def main() -> int:
    text = SRC.read_text(encoding="utf-8")

    # 提取 20 世纪 block（## 20 世纪 到 ## 21 世纪 之间）
    m = re.search(r"## 20 世纪.*?(?=\n## 21 世纪)", text, re.DOTALL)
    if not m:
        print("未找到 20 世纪段落")
        return 1
    block = strip_links(m.group(0))

    # 解析表格行：| 年份 | 姓名 | 国籍 |
    row_pat = re.compile(r"^\|\s*(\d{4})\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|$")
    rows: list[tuple[str, str, str]] = []
    for line in block.splitlines():
        line = line.strip()
        mm = row_pat.match(line)
        if mm:
            year = mm.group(1)
            name = mm.group(2).strip()
            country = mm.group(3).strip() or "—"
            # 跳过表头分隔行
            if set(name.replace(":", "").replace("-", "")) <= {"-", ":"}:
                continue
            rows.append((year, name, country))

    total_items = len(rows)
    unique_names = [n for _, n, _ in rows]
    unique_people = set(unique_names)

    # 两度获奖者
    cnt = Counter(unique_names)
    double = {k for k, v in cnt.items() if v > 1}

    # 女性获奖者（20 世纪已知女性）
    women = {"Marie Curie", "Maria Goeppert Mayer"}

    # 国籍分布
    country_counter = Counter(c for _, _, c in rows)

    lines: list[str] = []
    lines.append("# 20 世纪诺贝尔物理学奖得主 — OpenPhysicist 名录\n")
    lines.append(
        "> **本名录收录 1901–2000 年诺贝尔物理学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从 Röntgen 的 X 射线到 Kilby 的集成电路：一百年间，物理学奖见证了现代物理从经典走向量子的全过程。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Physics」。\n"
        % (total_items, len(unique_people))
    )
    lines.append("---\n")

    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 姓名 | 国籍 |")
    lines.append("|:--:|------|:--:|")
    for year, name, country in rows:
        lines.append("| %s | %s | %s |" % (year, name, country))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：1901–2000")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)) + "（唯一两度获诺贝尔物理学奖者）")
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
        "\n> **这不是一份排名，而是一部按时间展开的物理学历程：每一项获奖都标记着人类对自然认识的一次跃迁。**\n"
    )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
