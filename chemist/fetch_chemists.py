#!/usr/bin/env python3
"""
从 Wikipedia 抓取所有化学家并输出到 Markdown 文档。

数据来源：
  1. 英文 Wikipedia 「List of chemists」及相关子页面
  2. 调用 MediaWiki API 的 parse 接口，获取列表页的结构化链接。
  3. 兜底使用 Category:Chemists 分类递归抓取。

用法：
  python3 fetch_chemists.py                    # 默认输出到 chemists.md
  python3 fetch_chemists.py -o out.md          # 自定义输出文件
  python3 fetch_chemists.py --with-summary     # 抓取每位化学家的简介（慢）
  python3 fetch_chemists.py --lang zh          # 中文 Wikipedia（按分类抓取）
"""

from __future__ import annotations

import argparse
import json
import re
import string
import sys
import time
from pathlib import Path
from typing import Iterable

import requests

USER_AGENT = (
    "ChemistsFetcher/1.0 "
    "(https://example.org/contact; educational use) "
    "python-requests"
)

# 英文 Wikipedia 化学家列表页 —— 主页面及按字母拆分的子页面
EN_LIST_PAGES = [
    "List of chemists",
]

# 额外补充列表页
EXTRA_EN_LIST_PAGES = [
    "List of biochemists",
    "List of Nobel laureates in Chemistry",
]


def api_endpoint(lang: str) -> str:
    return f"https://{lang}.wikipedia.org/w/api.php"


def build_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
    return s


def api_get(session: requests.Session, lang: str, params: dict) -> dict:
    """调用 MediaWiki API，带简单的重试。"""
    params = {**params, "format": "json", "formatversion": "2"}
    url = api_endpoint(lang)
    for attempt in range(4):
        try:
            r = session.get(url, params=params, timeout=30)
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, json.JSONDecodeError) as e:
            if attempt == 3:
                raise
            wait = 2 ** attempt
            print(f"  ! 请求失败 ({e})，{wait}s 后重试…", file=sys.stderr)
            time.sleep(wait)
    return {}


# ---------------------------------------------------------------------------
# 从「列表页」中抽取人物链接
# ---------------------------------------------------------------------------
def fetch_links_from_page(
    session: requests.Session, lang: str, title: str
) -> list[dict]:
    """
    用 action=parse&prop=links 获取页面内所有内链，
    然后过滤出「主命名空间(ns=0)」且「存在」的条目。
    """
    data = api_get(
        session,
        lang,
        {
            "action": "parse",
            "page": title,
            "prop": "links",
            "redirects": 1,
        },
    )
    parse = data.get("parse")
    if not parse:
        return []
    links = parse.get("links", [])
    return [
        {"title": lk["title"]}
        for lk in links
        if lk.get("ns") == 0 and lk.get("exists")
    ]


# ---------------------------------------------------------------------------
# 通过分类递归抓取（中文维基 & 兜底使用）
# ---------------------------------------------------------------------------
def fetch_category_members(
    session: requests.Session,
    lang: str,
    category: str,
    max_depth: int = 3,
    _seen: set[str] | None = None,
    _depth: int = 0,
) -> list[dict]:
    """递归遍历一个分类及其子分类中的所有页面（ns=0）。"""
    if _seen is None:
        _seen = set()
    if category in _seen or _depth > max_depth:
        return []
    _seen.add(category)

    members: list[dict] = []
    cont: dict = {}
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": category,
            "cmlimit": "500",
            "cmtype": "page|subcat",
            **cont,
        }
        data = api_get(session, lang, params)
        for m in data.get("query", {}).get("categorymembers", []):
            ns = m.get("ns")
            title = m.get("title", "")
            if ns == 0:
                members.append({"title": title})
            elif ns == 14:  # Category
                # 递归子分类（避免过度膨胀，限制深度）
                members.extend(
                    fetch_category_members(
                        session, lang, title, max_depth, _seen, _depth + 1
                    )
                )
        cont = data.get("continue", {})
        if not cont:
            break
    return members


# ---------------------------------------------------------------------------
# 可选：抓取每个人物的简介
# ---------------------------------------------------------------------------
def fetch_summaries(
    session: requests.Session, lang: str, titles: list[str]
) -> dict[str, str]:
    """批量抓取每页的 extract（简介首段）。每次最多 50 个。"""
    out: dict[str, str] = {}
    for i in range(0, len(titles), 50):
        batch = titles[i : i + 50]
        data = api_get(
            session,
            lang,
            {
                "action": "query",
                "prop": "extracts",
                "exintro": 1,
                "explaintext": 1,
                "redirects": 1,
                "titles": "|".join(batch),
            },
        )
        for p in data.get("query", {}).get("pages", []):
            title = p.get("title")
            extract = (p.get("extract") or "").strip()
            if title and extract:
                # 只保留首句/首段，避免 md 太长
                first_para = extract.split("\n")[0]
                out[title] = first_para
        print(f"  • 已抓取简介 {min(i + 50, len(titles))}/{len(titles)}")
        time.sleep(0.3)
    return out


# ---------------------------------------------------------------------------
# 清洗与分组
# ---------------------------------------------------------------------------
_BAD_TITLE_PATTERNS = [
    re.compile(r"^List of\b", re.I),
    re.compile(r"^Lists of\b", re.I),
    re.compile(r"^Category:", re.I),
    re.compile(r"^Wikipedia:", re.I),
    re.compile(r"^Portal:", re.I),
    re.compile(r"^Template:", re.I),
    re.compile(r"^File:", re.I),
    re.compile(r"\(disambiguation\)$", re.I),
    re.compile(r"^Timeline\b", re.I),
    re.compile(r"^History of\b", re.I),
    re.compile(r"^Glossary of\b", re.I),
    re.compile(r"^Outline of\b", re.I),
    re.compile(r"^Index of\b", re.I),
]

# 化学概念/非人物关键词 —— 包含这些词的不太可能是人物名
_NON_PERSON_KEYWORDS = [
    re.compile(r"\beffect\b", re.I),
    re.compile(r"\baction\b", re.I),
    re.compile(r"\btheory\b", re.I),
    re.compile(r"\btheorem\b", re.I),
    re.compile(r"\bmodel\b", re.I),
    re.compile(r"\bequation\b", re.I),
    re.compile(r"\bprinciple\b", re.I),
    re.compile(r"\bparadox\b", re.I),
    re.compile(r"\bexperiment\b", re.I),
    re.compile(r"\bproblem\b", re.I),
    re.compile(r"\blaw\b", re.I),
    re.compile(r"\bphenomenon\b", re.I),
    re.compile(r"\bforce\b", re.I),
    re.compile(r"\bfield\b", re.I),
    re.compile(r"\bmolecule\b", re.I),
    re.compile(r"\bcompound\b", re.I),
    re.compile(r"\bbond\b", re.I),
    re.compile(r"\breaction\b", re.I),
    re.compile(r"\bsynthesis\b", re.I),
    re.compile(r"\bcatalyst\b", re.I),
    re.compile(r"\bcatalysis\b", re.I),
    re.compile(r"\bpolymer\b", re.I),
    re.compile(r"\bmonomer\b", re.I),
    re.compile(r"\bion\b", re.I),
    re.compile(r"\bacid\b", re.I),
    re.compile(r"\balkali\b", re.I),
    re.compile(r"\boxid\b", re.I),
    re.compile(r"\breduction\b", re.I),
    re.compile(r"\belement\b", re.I),
    re.compile(r"\bsolvent\b", re.I),
    re.compile(r"\bsolute\b", re.I),
    re.compile(r"\bmechanism\b", re.I),
    re.compile(r"\bsystem\b", re.I),
    re.compile(r"\bdevice\b", re.I),
    re.compile(r"\bdetector\b", re.I),
    re.compile(r"\bapparatus\b", re.I),
    re.compile(r"\bspectroscopy\b", re.I),
    re.compile(r"\bspectrometer\b", re.I),
    re.compile(r"\bchromatography\b", re.I),
    re.compile(r"\blaboratory\b", re.I),
    re.compile(r"\binstrument\b", re.I),
    re.compile(r"\bminist(er|ry)\b", re.I),
    re.compile(r"\bpresident\b", re.I),
    re.compile(r"\bdepartment\b", re.I),
    re.compile(r"\buniversity\b", re.I),
    re.compile(r"\binstitute\b", re.I),
    re.compile(r"\bacademy\b", re.I),
    re.compile(r"\bsociety\b", re.I),
    re.compile(r"\bprize\b", re.I),
    re.compile(r"\bmedal\b", re.I),
    re.compile(r"\baward\b", re.I),
    re.compile(r"\bconference\b", re.I),
    re.compile(r"\bsymposium\b", re.I),
    re.compile(r"\bAges\b"),
    re.compile(r"\bcentury\b", re.I),
    re.compile(r"\bancient\b", re.I),
    re.compile(r"\bmodern\b", re.I),
    re.compile(r"\bclassical\b", re.I),
    re.compile(r"\bquantum\b", re.I),
    re.compile(r"\bmechanics\b", re.I),
    re.compile(r"\bdynamics\b", re.I),
    re.compile(r"\bthermodynamics\b", re.I),
    re.compile(r"\bkinetics\b", re.I),
    re.compile(r"\bchemistry\b", re.I),
    re.compile(r"\bmathematics\b", re.I),
    re.compile(r"\bbiology\b", re.I),
    re.compile(r"\bphysics\b", re.I),
    re.compile(r"\bastronomy\b", re.I),
    re.compile(r"\btechnolog\b", re.I),
    re.compile(r"\bengineer\b", re.I),
]


def looks_like_person(title: str) -> bool:
    if not title:
        return False
    for pat in _BAD_TITLE_PATTERNS:
        if pat.search(title):
            return False
    # 过滤掉纯主题页（如 "Chemistry", "Quantum mechanics"）——极少会误伤人物
    if title.islower():
        return False
    # 排除明确为化学概念的条目
    for pat in _NON_PERSON_KEYWORDS:
        if pat.search(title):
            return False
    return True


def sort_key_by_surname(title: str) -> tuple[str, str]:
    """按姓氏（最后一个空格后的词）排序，辅以全名。"""
    base = re.sub(r"\s*\(.*?\)\s*$", "", title).strip()
    parts = base.split()
    surname = parts[-1] if parts else base
    return (surname.lower(), base.lower())


def group_by_initial(people: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for name in people:
        key = sort_key_by_surname(name)[0][:1].upper()
        if not key.isalpha():
            key = "#"
        groups.setdefault(key, []).append(name)
    for k in groups:
        groups[k].sort(key=sort_key_by_surname)
    return groups


# ---------------------------------------------------------------------------
# Markdown 输出
# ---------------------------------------------------------------------------
def wiki_url(lang: str, title: str) -> str:
    slug = title.replace(" ", "_")
    return f"https://{lang}.wikipedia.org/wiki/{requests.utils.quote(slug, safe='_()/,')}"


def write_markdown(
    path: Path,
    lang: str,
    people: list[str],
    summaries: dict[str, str] | None,
    source_desc: str,
) -> None:
    groups = group_by_initial(people)
    letters = sorted(groups.keys(), key=lambda c: (c == "#", c))

    lines: list[str] = []
    lines.append("# 维基百科化学家列表\n")
    lines.append(
        f"> 数据来源：{source_desc}\n"
        f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"> 总人数：**{len(people)}**\n"
    )
    lines.append("\n## 目录\n")
    lines.append(" ".join(f"[{c}](#{c.lower()})" for c in letters))
    lines.append("\n")

    for c in letters:
        lines.append(f"\n## {c}\n")
        for name in groups[c]:
            url = wiki_url(lang, name)
            if summaries and name in summaries:
                lines.append(f"- [{name}]({url}) — {summaries[name]}")
            else:
                lines.append(f"- [{name}]({url})")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def collect_english(session: requests.Session) -> tuple[set[str], str]:
    """通过英文 Wikipedia 的化学家列表页收集。"""
    all_titles: set[str] = set()
    pages = EN_LIST_PAGES + EXTRA_EN_LIST_PAGES
    for idx, page in enumerate(pages, 1):
        print(f"[{idx}/{len(pages)}] 抓取列表页：{page}")
        links = fetch_links_from_page(session, "en", page)
        kept = [lk["title"] for lk in links if looks_like_person(lk["title"])]
        print(f"  → 提取到 {len(kept)} 个条目")
        all_titles.update(kept)
        time.sleep(0.3)
    return all_titles, "英文维基百科「List of chemists」及相关列表页"


def collect_by_category(
    session: requests.Session, lang: str, category: str
) -> tuple[set[str], str]:
    print(f"通过分类递归抓取：{category}（lang={lang}）")
    members = fetch_category_members(session, lang, category, max_depth=3)
    titles = {m["title"] for m in members if looks_like_person(m["title"])}
    return titles, f"{lang}.wikipedia «{category}» 及其子分类"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "-o",
        "--output",
        default="chemists.md",
        help="输出的 Markdown 路径（默认 chemists.md）",
    )
    ap.add_argument(
        "--lang",
        default="en",
        help="Wikipedia 语言代码，如 en / zh（默认 en）",
    )
    ap.add_argument(
        "--category",
        default=None,
        help="改用分类递归方式抓取，例如 'Category:Chemists'（zh 默认使用 'Category:化学家'）",
    )
    ap.add_argument(
        "--with-summary",
        action="store_true",
        help="同时抓取每位化学家的简介（较慢）",
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=0,
        help="仅保留前 N 个（调试用，0=全部）",
    )
    args = ap.parse_args()

    session = build_session()

    if args.lang == "en" and not args.category:
        titles, source_desc = collect_english(session)
    else:
        category = args.category
        if not category:
            category = "Category:化学家" if args.lang == "zh" else "Category:Chemists"
        titles, source_desc = collect_by_category(session, args.lang, category)

    people = sorted(titles, key=sort_key_by_surname)
    if args.limit:
        people = people[: args.limit]

    print(f"\n共收集到 {len(people)} 位化学家。")

    summaries: dict[str, str] | None = None
    if args.with_summary:
        print("开始抓取简介…")
        summaries = fetch_summaries(session, args.lang, people)

    out_path = Path(args.output).resolve()
    write_markdown(out_path, args.lang, people, summaries, source_desc)
    print(f"\n✅ 已写入：{out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())