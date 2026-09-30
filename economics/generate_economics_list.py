#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 OpenEcon 20 / 21 世纪诺贝尔经济学奖名录。

产出：
  presentations/20th_century/OpenEcon_20th_Century_Nobel_Laureates.md
  presentations/21th_century/OpenEcon_21st_Century_Nobel_Laureates.md

用法：python3 generate_economics_list.py
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "MySQL"))
from db_mysql import get_conn

from economics_list_data import DATA


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_'.()\u00b7,\-]", "", s).lower()


def load_social_status() -> dict[str, int]:
    """从 greatminds 库读取 has_social_data 状态，键为归一化姓名。"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name_en, has_social_data FROM people")
    out = {}
    for en, soc in cur.fetchall():
        out[_norm(en)] = int(soc or 0)
    conn.close()
    return out


def load_social_by_qid() -> dict[str, int]:
    """qid -> has_social_data（名录显示名与库内规范名有差异时的二级匹配键）。"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT qid, has_social_data FROM people WHERE qid IS NOT NULL")
    out = {qid: int(soc or 0) for qid, soc in cur.fetchall()}
    conn.close()
    return out


def load_qid_by_data_name() -> dict[str, str]:
    """归一化(DATA 显示名) -> qid，来源：pages/*/metadata.json 的 label/name。"""
    pages = ROOT / "presentations" / "pages"
    out: dict[str, str] = {}
    for century in ("20th_century", "21th_century"):
        for d in sorted((pages / century).iterdir()):
            if not d.is_dir():
                continue
            try:
                meta = json.loads((d / "metadata.json").read_text(encoding="utf-8"))
            except Exception:
                continue
            qid = meta.get("qid")
            if not qid:
                continue
            for key in (meta.get("label"), meta.get("name")):
                if key:
                    out.setdefault(_norm(key), qid)
    return out

ROOT = Path(__file__).resolve().parent
OUT20 = ROOT / "presentations" / "20th_century" / "OpenEcon_20th_Century_Nobel_Laureates.md"
OUT21 = ROOT / "presentations" / "21th_century" / "OpenEcon_21st_Century_Nobel_Laureates.md"

# 拆分理由年份的分组大小（按 DATA 获奖者顺序连续切分），如 2021 = Card 独享 + Angrist/Imbens 共享
GROUP_SIZES = {
    2000: (1, 1),
    2002: (1, 1),
    2003: (1, 1),
    2009: (1, 1),
    2018: (1, 1),
    2021: (1, 2),
    2025: (1, 2),
}


def build_rows(century: str) -> list[tuple[int, str, str, str, str, str]]:
    """返回 (year, name_en, name_zh, country, citation_en, citation_zh) 列表。

    拆分理由年份的理由串以 "||" 分隔，按 GROUP_SIZES 连续分组对应；全年份共享理由自动广播。
    """
    lo, hi = (1969, 2000) if century == "20th" else (2001, 2025)
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
    """名录显示名（经济学奖姓名无生卒括号/消歧义问题，保持原样）。"""
    return ne


FEMALE_20TH: set[str] = set()  # 1969–2000 无女性得主
FEMALE_21TH = {"Elinor Ostrom", "Esther Duflo", "Claudia Goldin"}


def write_list(path: Path, header_title: str, year_range: str, source: str,
               rows: list, years: int, extra_note: str = "", female: set[str] | None = None,
               closing: str = "", social_done: dict[str, int] | None = None,
               social_by_qid: dict[str, int] | None = None,
               qid_by_data_name: dict[str, str] | None = None) -> None:
    female = female or set()
    social_done = social_done or {}
    social_by_qid = social_by_qid or {}
    qid_by_data_name = qid_by_data_name or {}

    def _is_social_done(name_en: str) -> bool:
        if social_done.get(_norm(name_en)) == 1:
            return True
        qid = qid_by_data_name.get(_norm(name_en))
        return bool(qid) and social_by_qid.get(qid) == 1

    lines = []
    lines.append(f"# {header_title}\n")
    lines.append(f"> **本名录收录 {year_range} 年诺贝尔经济学奖得主，共 {years} 个颁奖年份 / {len(rows)} 位。**\n")
    lines.append(">")
    lines.append("> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，"
                 "「Review」表示是否已完成事实核查，「社会关系入库」表示是否已将研究领域与社会关系写入 "
                 "greatminds 数据库（people / person_relation / person_field）。")
    lines.append(">")
    lines.append(f"> 数据来源：{source}；国籍沿用 Wikipedia 表格 country 口径（多国籍得主以 \" / \" 连接）。")
    if extra_note:
        lines.append(">")
        lines.append(f"> {extra_note}")
    lines.append("\n---\n")
    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review | 社会关系入库 |")
    lines.append("|:--:|------|------|------|:--:|:--:|:--:|")
    for year, ne, nz, ctry, _zen, zzh in rows:
        # 注意：按 has_social_data 值判断（库内存在记录但未入库显示 🔲）；名称差异时按 QID 二级匹配
        soc = "✅" if _is_social_done(ne) else "🔲"
        lines.append(f"| {year} | {_display(ne)} ({nz}) | {ctry} | {zzh} | 🔲 | 🔲 | {soc} |")

    # ------------------------- 二、统计说明 -------------------------
    persons = sorted({_display(ne) for _, ne, *_ in rows})
    countries: dict[str, int] = {}
    for _, ne, _nz, ctry, _zen, _zzh in rows:
        countries[ctry] = countries.get(ctry, 0) + 1
    females = [p for p in persons if p in female]

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append(f"\n- **获奖年份跨度**：{year_range}")
    lines.append(f"- **颁奖年份**：{years} 个")
    lines.append(f"- **获奖总人数**：{len(persons)} 位")
    lines.append("- **已立传**：0 位")
    lines.append("- **已 Review**：0 位")
    lines.append(f"- **已社会关系入库**：{sum(1 for _, ne, *_ in rows if _is_social_done(ne))} 位")
    lines.append("- **两度获奖者**：无（诺贝尔经济学奖至今无人两度获奖）")
    if females:
        lines.append(f"- **女性获奖者**：{len(females)} 位（{'、'.join(females)}）")
    else:
        lines.append("- **女性获奖者**：无")
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
    years20 = sum(1 for y in sorted(DATA) if 1969 <= y <= 2000)
    years21 = sum(1 for y in sorted(DATA) if y > 2000)
    social_done = load_social_status()
    social_by_qid = load_social_by_qid()
    qid_by_data_name = load_qid_by_data_name()

    write_list(
        OUT20,
        "20 世纪诺贝尔经济学奖得主 — OpenEcon 名录",
        "1969–2000",
        "英文维基百科「List of Nobel laureates in Economics」+ Nobel 官方获奖理由",
        rows20, years20,
        extra_note="诺贝尔经济学奖全称为「瑞典央行纪念阿尔弗雷德·诺贝尔经济学奖」，1969 年增设并首次颁发，"
                   "非诺贝尔遗嘱所设五大奖；1969–2000 年间每年颁发，无未颁奖年份。",
        female=FEMALE_20TH,
        closing="从弗里希与廷贝亨创立经济计量学，到卢卡斯的理性预期革命，20 世纪最后三十年的经济学奖"
                "勾勒出这门学科数学化、精细化与现代宏观经济学成型的完整轨迹。",
        social_done=social_done,
        social_by_qid=social_by_qid,
        qid_by_data_name=qid_by_data_name,
    )
    write_list(
        OUT21,
        "21 世纪诺贝尔经济学奖得主 — OpenEcon 名录",
        "2001–2025",
        "英文维基百科「List of Nobel laureates in Economics」+ Nobel 官方获奖理由",
        rows21, years21,
        extra_note="2001–2025 年间每年颁发，无未颁奖年份。",
        female=FEMALE_21TH,
        closing="进入新世纪，经济学奖不断拓展学科的边界：从行为经济学到机制设计，从自然实验到随机对照试验，"
                "从契约理论到制度与繁荣的长期之问。",
        social_done=social_done,
        social_by_qid=social_by_qid,
        qid_by_data_name=qid_by_data_name,
    )

    total = len(rows20) + len(rows21)
    print(f"\n合计：{years20 + years21} 个颁奖年份 / {total} 位（含共享年份重复计数，去重后以维基名录 99 人为准）")
    print(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
