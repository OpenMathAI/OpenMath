#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 OpenMedic 20 / 21 世纪诺贝尔生理学或医学奖名录。

产出：
  presentations/20th_century/OpenMedic_20th_Century_Nobel_Laureates.md
  presentations/21th_century/OpenMedic_21st_Century_Nobel_Laureates.md

用法：python3 generate_medicine_list.py
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from medicine_list_data import DATA

ROOT = Path(__file__).resolve().parent
OUT20 = ROOT / "presentations" / "20th_century" / "OpenMedic_20th_Century_Nobel_Laureates.md"
OUT21 = ROOT / "presentations" / "21th_century" / "OpenMedic_21st_Century_Nobel_Laureates.md"

# 拆分理由年份的分组大小（按 DATA 获奖者顺序连续切分），如 1947 = Cori 夫妇共享 + Houssay 独享
GROUP_SIZES = {
    1922: (1, 1),
    1929: (1, 1),
    1947: (2, 1),
    1949: (1, 1),
    1953: (1, 1),
    1958: (2, 1),
    1966: (1, 1),
    1977: (2, 1),
    1981: (1, 2),
    2008: (1, 2),
    2011: (2, 1),
    2015: (2, 1),
}


def build_rows(century: str) -> list[tuple[int, str, str, str, str, str]]:
    """返回 (year, name_en, name_zh, country, citation_en, citation_zh) 列表。

    拆分理由年份的理由串以 "||" 分隔，按 GROUP_SIZES 连续分组对应；全年份共享理由自动广播。
    """
    lo, hi = (1901, 2000) if century == "20th" else (2001, 2025)
    rows: list[tuple[int, str, str, str, str, str]] = []
    for year in sorted(DATA):
        if not (lo <= year <= hi):
            continue
        cit_en, cit_zh, laureates = DATA[year]
        en_parts = [p.strip() for p in cit_en.split("||")]
        zh_parts = [p.strip() for p in cit_zh.split("||")]
        assert len(en_parts) == len(zh_parts), f"{year} 中英文理由拆分数不匹配"
        n, p = len(laureates), len(en_parts)
        if p == 1:
            groups = [list(laureates)]
        else:
            sizes = GROUP_SIZES[year]
            assert sum(sizes) == n and len(sizes) == p, f"{year} 分组大小 {sizes} 与获奖者 {n}/理由 {p} 不匹配"
            groups, idx = [], 0
            for sz in sizes:
                groups.append(laureates[idx:idx + sz])
                idx += sz
        for g, (zen, zzh) in enumerate(zip(en_parts, zh_parts)):
            for (ne, nz, ctry) in groups[g]:
                rows.append((year, ne, nz, ctry, zen, zzh))
    return rows


def _display(ne: str) -> str:
    """名录显示名：去掉维基消歧义括号（如 "William C. Campbell (scientist)"）。"""
    return re.sub(r"\s*\([^)]*\)$", "", ne)


FEMALE_20TH = {"Gerty Cori", "Barbara McClintock", "Rita Levi-Montalcini", "Rosalyn Sussman Yalow"}
FEMALE_21TH = {"Linda B. Buck", "Françoise Barré-Sinoussi", "Carol W. Greider", "May-Britt Moser",
               "Tu Youyou", "Katalin Karikó"}


def write_list(path: Path, header_title: str, year_range: str, source: str,
               rows: list, years: int, extra_note: str = "", female: set[str] | None = None,
               closing: str = "") -> None:
    female = female or set()
    lines = []
    lines.append(f"# {header_title}\n")
    lines.append(f"> **本名录收录 {year_range} 年诺贝尔生理学或医学奖得主，共 {years} 个颁奖年份 / {len(rows)} 位。**\n")
    lines.append(">")
    lines.append("> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，"
                 "「Review」表示是否已完成事实核查，「社会关系入库」表示是否已将研究领域与社会关系写入 "
                 "greatminds 数据库（people / person_relation / person_field）。")
    lines.append(">")
    lines.append(f"> 数据来源：{source}；国籍沿用 Nobel 官方 country 口径（Wikipedia 表格 rowspan 合并导致的获奖理由/国籍串行已按官方口径修正）。")
    if extra_note:
        lines.append(">")
        lines.append(f"> {extra_note}")
    lines.append("\n---\n")
    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review | 社会关系入库 |")
    lines.append("|:--:|------|------|------|:--:|:--:|:--:|")
    for year, ne, nz, ctry, _zen, zzh in rows:
        lines.append(f"| {year} | {_display(ne)} ({nz}) | {ctry} | {zzh} | 🔲 | 🔲 | 🔲 |")

    # ------------------------- 二、统计说明 -------------------------
    persons = sorted({_display(ne) for _, ne, *_ in rows})
    countries: dict[str, int] = {}
    for _, ne, _nz, ctry, _zen, _zzh in rows:
        countries[ctry] = countries.get(ctry, 0) + 1
    females = [p for p in persons if any(p == f or p.endswith(f) or f in p for f in female)]

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append(f"\n- **获奖年份跨度**：{year_range}")
    lines.append(f"- **颁奖年份**：{years} 个")
    lines.append(f"- **获奖总人数**：{len(persons)} 位")
    lines.append("- **已立传**：0 位")
    lines.append("- **已 Review**：0 位")
    lines.append("- **已社会关系入库**：0 位")
    lines.append("- **两度获奖者**：无（诺贝尔生理学或医学奖至今无人两度获奖）")
    if females:
        lines.append(f"- **女性获奖者**：{len(females)} 位（{'、'.join(females)}）")
    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for ctry, cnt in sorted(countries.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {ctry} | {cnt} |")
    lines.append("\n---\n")
    if closing:
        lines.append(f"\n> **{closing}**\n")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print("wrote:", path)
    print("  颁奖年份:", years, " 得主行数:", len(rows))


def main() -> int:
    rows20 = build_rows("20th")
    rows21 = build_rows("21th")
    years20 = sum(1 for y in sorted(DATA) if 1901 <= y <= 2000)
    years21 = sum(1 for y in sorted(DATA) if y > 2000)

    write_list(
        OUT20,
        "20 世纪诺贝尔生理学或医学奖得主 — OpenMedic 名录",
        "1901–2000",
        "英文维基百科「List of Nobel laureates in Physiology or Medicine」+ Nobel 官方获奖理由",
        rows20, years20,
        extra_note="1901–2000 年间未颁奖年份：1915–1918、1921、1925、1940–1942（两次世界大战期间）。",
        female=FEMALE_20TH,
        closing="这不是一份排名，而是一部按时间展开的医学历程：从血清疗法到基因组编辑，每一项获奖都标记着人类战胜疾病的一次跃迁。",
    )
    write_list(
        OUT21,
        "21 世纪诺贝尔生理学或医学奖得主 — OpenMedic 名录",
        "2001–2025",
        "英文维基百科「List of Nobel laureates in Physiology or Medicine」+ Nobel 官方获奖理由",
        rows21, years21,
        female=FEMALE_21TH,
        closing="进入新世纪，生理学或医学奖持续改写人类对生命的认知：从细胞自噬到 mRNA 疫苗，从大脑定位系统到丙肝病毒的攻克。",
    )

    total = len(rows20) + len(rows21)
    print(f"\n合计：{years20 + years21} 个颁奖年份 / {total} 位（含共享年份重复计数，去重后以维基名录 232 人为准）")
    print(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
