#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 OpenPeace 20 / 21 世纪诺贝尔和平奖名录。

产出：
  presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md
  presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md

用法：python3 generate_peace_list.py
"""
from __future__ import annotations

import re
import time
from collections import Counter
from pathlib import Path

from peace_list_data import DATA

ROOT = Path(__file__).resolve().parent
OUT20 = ROOT / "presentations" / "20th_century" / "OpenPeace_20th_Century_Nobel_Laureates.md"
OUT21 = ROOT / "presentations" / "21th_century" / "OpenPeace_21st_Century_Nobel_Laureates.md"

NO_AWARD_YEARS = "1914–1916、1918、1923、1924、1928、1932、1939–1943、1948、1955、1956、1966、1967、1972"
ORG_LABEL = "International organization"


def _norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_'.()\u00b7,\-]", "", s).lower()


_SOCIAL_CACHE: dict[str, int] | None = None

# 名录显示名 → 库内 name_en 的别名（库内用全名/规范名形式）
SOCIAL_ALIAS = {
    "Lord Boyd-Orr": "John Boyd Orr",
    "John Raleigh Mott": "John Mott",
    "United Nations Children's Fund (UNICEF)": "United Nations Children's Fund",
    "Wangari Muta Maathai": "Wangari Maathai",
}


def _social_done(name_en: str) -> bool:
    """直查 greatminds 库：该获奖者 has_social_data 是否为 1。"""
    name_en = SOCIAL_ALIAS.get(name_en, name_en)
    global _SOCIAL_CACHE
    if _SOCIAL_CACHE is None:
        _SOCIAL_CACHE = {}
        try:
            import sys
            sys.path.insert(0, str(ROOT.parent / "MySQL"))
            from db_mysql import get_conn
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT name_en, has_social_data FROM people")
            for en, soc in cur.fetchall():
                if en:
                    _SOCIAL_CACHE[_norm(en)] = soc
            conn.close()
        except Exception as e:
            print("WARN: 数据库不可达，社会关系入库列按 🔲 处理：", e)
    return bool(_SOCIAL_CACHE.get(_norm(name_en)))

# 国家级机构获奖者（非 International organization 口径的组织）
NATIONAL_ORGS = {"Institute of International Law", "Friends Service Council",
                 "American Friends Service Committee", "Amnesty International",
                 "Grameen Bank", "Tunisian National Dialogue Quartet", "Memorial",
                 "Centre for Civil Liberties", "Nihon Hidankyo"}


def build_rows(century: str) -> list[tuple[int, str, str, str, str, str]]:
    """返回 (year, name_en, name_zh, country, citation_en, citation_zh) 列表。

    全年份共享理由（理由串无 "||"）自动广播给当年所有获奖者；
    按人拆分理由的年份（如 1901/1902/1925/1946/1974）理由数须与获奖者数一致。
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
            assert p == n, f"{year} 拆分理由 {p} 组与获奖者 {n} 位不匹配"
            groups = [[l] for l in laureates]
        for g, (zen, zzh) in enumerate(zip(en_parts, zh_parts)):
            for (ne, nz, ctry) in groups[g]:
                rows.append((year, ne, nz, ctry, zen, zzh))
    return rows


def is_org_row(ctry: str, name: str) -> bool:
    return ctry == ORG_LABEL or name in NATIONAL_ORGS


def write_list(path: Path, header_title: str, year_range: str, source: str,
               rows: list, years: int, extra_note: str = "",
               female: set[str] | None = None, closing: str = "") -> None:
    female = female or set()
    lines = []
    lines.append(f"# {header_title}\n")
    lines.append(f"> **本名录收录 {year_range} 年诺贝尔和平奖得主，共 {years} 个颁奖年份 / {len(rows)} 次获奖（含组织机构）。**\n")
    lines.append(">")
    lines.append("> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，"
                 "「Review」表示是否已完成事实核查，「社会关系入库」表示是否已将研究领域与社会关系写入 "
                 "greatminds 数据库（people / person_relation / person_field）。")
    lines.append(">")
    lines.append(f"> 数据来源：{source}；国籍沿用维基百科「List of Nobel Peace Prize laureates」口径"
                 "（个人为获奖时国籍；跨国/政府间组织统一标注 International organization，国家级机构保留所在国）。")
    if extra_note:
        lines.append(">")
        lines.append(f"> {extra_note}")
    lines.append("\n---\n")
    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍/所在国 | 获奖理由 | 立传 | Review | 社会关系入库 |")
    lines.append("|:--:|------|------|------|:--:|:--:|:--:|")
    for year, ne, nz, ctry, _zen, zzh in rows:
        rel = "✅" if _social_done(ne) else "🔲"
        lines.append(f"| {year} | {ne} ({nz}) | {ctry} | {zzh} | 🔲 | 🔲 | {rel} |")

    # ------------------------- 二、统计说明 -------------------------
    individuals = sorted({ne for _, ne, _, ctry, *_ in rows if not is_org_row(ctry, ne)})
    org_count = sum(1 for _, ne, _, ctry, *_ in rows if is_org_row(ctry, ne))
    females = [p for p in individuals if any(p == f or f in p for f in female)]

    cnt = Counter(ne for _, ne, *_ in rows)
    multi = [(name, c) for name, c in cnt.items() if c > 1]

    countries: dict[str, int] = {}
    for _, _ne, _nz, ctry, _zen, _zzh in rows:
        countries[ctry] = countries.get(ctry, 0) + 1

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append(f"\n- **获奖年份跨度**：{year_range}")
    lines.append(f"- **颁奖年份**：{years} 个")
    lines.append(f"- **获奖总次数**：{len(rows)} 次（个人 {len(rows) - org_count} / 组织机构 {org_count}）")
    lines.append(f"- **个人获奖者**：{len(individuals)} 位")
    lines.append("- **已立传**：0 位")
    lines.append("- **已 Review**：0 位")
    rel_done = sum(1 for ne in {ne for _, ne, *_ in rows} if _social_done(ne))
    lines.append(f"- **已社会关系入库**：{rel_done} / {len({ne for _, ne, *_ in rows})} 位")
    if multi:
        lines.append("- **多次获奖**：" + "；".join(f"{name}（{c} 次）" for name, c in multi))
    lines.append("- **拒绝领奖**：黎德寿（1973，诺贝尔和平奖历史上唯一拒绝领奖的得主）")
    lines.append(f"- **未颁奖年份**：{NO_AWARD_YEARS}")
    if females:
        lines.append(f"- **女性获奖者**：{len(females)} 位（{'、'.join(females)}）")
    lines.append("\n### 国籍/机构分布\n")
    lines.append("\n| 国籍/所在国 | 次数 |")
    lines.append("|------|:--:|")
    for ctry, c in sorted(countries.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {ctry} | {c} |")
    lines.append("\n---\n")
    if closing:
        lines.append(f"\n> **{closing}**\n")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print("wrote:", path)
    print("  颁奖年份:", years, " 获奖行数:", len(rows))


FEMALE_20TH = {"Bertha von Suttner", "Jane Addams", "Emily Greene Balch",
               "Betty Williams", "Mairead Corrigan", "Mother Teresa",
               "Alva Myrdal", "Aung San Suu Kyi", "Rigoberta Menchú", "Jody Williams"}
FEMALE_21TH = {"Shirin Ebadi", "Wangari Muta Maathai", "Ellen Johnson Sirleaf",
               "Leymah Gbowee", "Tawakkol Karman", "Malala Yousafzai",
               "Nadia Murad", "Maria Ressa", "Narges Mohammadi", "María Corina Machado"}


def main() -> int:
    rows20 = build_rows("20th")
    rows21 = build_rows("21th")
    years20 = sum(1 for y in sorted(DATA) if 1901 <= y <= 2000)
    years21 = sum(1 for y in sorted(DATA) if y > 2000)

    write_list(
        OUT20,
        "20 世纪诺贝尔和平奖得主 — OpenPeace 名录",
        "1901–2000",
        "英文维基百科「List of Nobel Peace Prize laureates」",
        rows20, years20,
        extra_note=f"1901–2000 年间未颁奖年份：{NO_AWARD_YEARS}（两次世界大战及冷战期间的否决）。",
        female=FEMALE_20TH,
        closing="这不是一份排名，而是一部按时间展开的和平历程：从国际法与人道救援，到裁军谈判与种族和解，"
                "每一次颁奖都在标注人类为远离战争所做的一次努力。",
    )
    write_list(
        OUT21,
        "21 世纪诺贝尔和平奖得主 — OpenPeace 名录",
        "2001–2025",
        "英文维基百科「List of Nobel Peace Prize laureates」",
        rows21, years21,
        female=FEMALE_21TH,
        closing="进入新世纪，和平奖的视野不断拓展：从气候变迁与粮食安全，到言论自由与妇女生存权，"
                "和平的内涵正被赋予更广阔的时代意义。",
    )

    total = len(rows20) + len(rows21)
    print(f"\n合计：{years20 + years21} 个颁奖年份 / {total} 次获奖")
    print(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
