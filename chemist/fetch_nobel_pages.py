#!/usr/bin/env python3
"""
抓取诺贝尔化学奖得主的完整 Wikipedia 页面（复用数学家侧 fetch_full_pages.py 的下载方式）。

每个人物会生成：
  pages/<世纪>/<Name>/page.md          正文 Markdown（由 HTML 转换）
  pages/<世纪>/<Name>/page.html        原始 HTML（备份）
  pages/<世纪>/<Name>/metadata.json    Wikidata 元数据（生卒、领域、国籍、获奖等）
  pages/<世纪>/<Name>/images.txt       页面内图片 URL 清单

并在 pages/INDEX.md 生成总索引。

数据来源：presentations/Nobel_Chemistry_Laureates_20th_21st_Century.md
世纪划分：1901–2000 → 20th_century，2001–2025 → 21st_century

用法：
  python3 fetch_nobel_pages.py --limit 5          # 仅抓前 5 个（测试用）
  python3 fetch_nobel_pages.py                    # 抓全部
  python3 fetch_nobel_pages.py --only Curie    # 只抓名字含 Curie 的

依赖：
  pip install requests beautifulsoup4 markdownify
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, unquote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

USER_AGENT = (
    "OpenMathAI-ChemistFetcher/1.0 "
    "(https://github.com/OpenMathAI/OpenMath; educational use) python-requests"
)

ROOT = Path(__file__).resolve().parent
LIST_MD = ROOT / "presentations" / "Nobel_Chemistry_Laureates_20th_21st_Century.md"
OUT_ROOT = ROOT / "presentations" / "pages"


# ---------------------------------------------------------------------------
# HTTP 工具
# ---------------------------------------------------------------------------
def build_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def http_get(session: requests.Session, url: str, **kw) -> requests.Response:
    for attempt in range(4):
        try:
            r = session.get(url, timeout=60, **kw)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            if attempt == 3:
                raise
            wait = 2**attempt
            print(f"    ! {e}，{wait}s 后重试")
            time.sleep(wait)
    raise RuntimeError("unreachable")


# ---------------------------------------------------------------------------
# 1) 抓取页面 HTML（REST API，已渲染）
# ---------------------------------------------------------------------------
def fetch_html(session: requests.Session, title: str, lang: str = "en") -> str:
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
    r = http_get(session, url, headers={"Accept": "text/html; charset=utf-8"})
    return r.text


# ---------------------------------------------------------------------------
# 2) HTML -> Markdown（清洗 + 转换）
# ---------------------------------------------------------------------------
_REMOVE_SELECTORS = [
    "style", "script", "link", "meta",
    "sup.reference",
    ".mw-editsection",
    ".mw-empty-elt",
    ".noprint",
    ".navbox", ".vertical-navbox",
    ".metadata",
    ".hatnote", ".shortdescription",
    ".mw-jump-link",
    ".reflist",
    "#References ~ *",
    "table.infobox .infobox-image img",
]


def clean_html(html: str, lang: str) -> tuple[str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")

    for sel in _REMOVE_SELECTORS:
        for node in soup.select(sel):
            node.decompose()

    images: list[str] = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        src = _absolutize(src, lang)
        images.append(src)
        img["src"] = src
        if img.has_attr("srcset"):
            img["srcset"] = _absolutize_srcset(img["srcset"], lang)

    for a in soup.find_all("a", href=True):
        a["href"] = _absolutize(a["href"], lang, wiki_prefix=True)

    head = soup.find("head")
    if head is None:
        head = soup.new_tag("head")
        if soup.html:
            soup.html.insert(0, head)
        else:
            soup.insert(0, head)
    if not head.find("base"):
        base = soup.new_tag("base", href=f"https://{lang}.wikipedia.org/wiki/")
        head.insert(0, base)
    if not head.find("meta", attrs={"charset": True}):
        head.insert(0, soup.new_tag("meta", charset="utf-8"))

    return str(soup), images


def _absolutize(url: str, lang: str, wiki_prefix: bool = False) -> str:
    if not url:
        return url
    if url.startswith(("http://", "https://", "data:", "mailto:", "#")):
        return url
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return f"https://{lang}.wikipedia.org" + url
    if url.startswith("./"):
        prefix = f"https://{lang}.wikipedia.org/wiki/" if wiki_prefix else f"https://{lang}.wikipedia.org/"
        return prefix + url[2:]
    return url


def _absolutize_srcset(srcset: str, lang: str) -> str:
    out = []
    for item in srcset.split(","):
        item = item.strip()
        if not item:
            continue
        parts = item.split(None, 1)
        parts[0] = _absolutize(parts[0], lang)
        out.append(" ".join(parts))
    return ", ".join(out)


def html_to_markdown(html: str) -> str:
    text = md(html, heading_style="ATX", bullets="-", strip=["span"])
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# 3) Wikidata 元数据
# ---------------------------------------------------------------------------
def fetch_wikidata_qid(session: requests.Session, title: str, lang: str = "en") -> str | None:
    r = http_get(
        session,
        f"https://{lang}.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "prop": "pageprops",
            "ppprop": "wikibase_item",
            "titles": title,
            "redirects": 1,
            "format": "json",
            "formatversion": "2",
        },
    )
    pages = r.json().get("query", {}).get("pages", [])
    if pages:
        return pages[0].get("pageprops", {}).get("wikibase_item")
    return None


WANTED_PROPS = {
    "P31": "instance_of",
    "P106": "occupation",
    "P27": "nationality",
    "P19": "place_of_birth",
    "P20": "place_of_death",
    "P569": "date_of_birth",
    "P570": "date_of_death",
    "P101": "field_of_work",
    "P184": "doctoral_advisor",
    "P185": "doctoral_student",
    "P69": "educated_at",
    "P108": "employer",
    "P166": "award_received",
    "P800": "notable_work",
    "P21": "sex_or_gender",
}


def fetch_wikidata_entity(session: requests.Session, qid: str) -> dict:
    r = http_get(
        session,
        f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json",
    )
    return r.json().get("entities", {}).get(qid, {})


def resolve_labels(session: requests.Session, qids: list[str], lang: str = "en") -> dict[str, str]:
    out: dict[str, str] = {}
    for i in range(0, len(qids), 50):
        batch = qids[i : i + 50]
        r = http_get(
            session,
            "https://www.wikidata.org/w/api.php",
            params={
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "labels",
                "languages": lang,
                "format": "json",
            },
        )
        for qid, ent in r.json().get("entities", {}).items():
            label = ent.get("labels", {}).get(lang, {}).get("value")
            if label:
                out[qid] = label
    return out


def extract_metadata(session: requests.Session, qid: str, lang: str = "en") -> dict:
    ent = fetch_wikidata_entity(session, qid)
    claims = ent.get("claims", {})

    raw: dict[str, list[str]] = {}
    qids_to_resolve: set[str] = set()

    for pid, key in WANTED_PROPS.items():
        vals: list[str] = []
        for c in claims.get(pid, []):
            dv = c.get("mainsnak", {}).get("datavalue")
            if not dv:
                continue
            v = dv.get("value")
            if dv.get("type") == "wikibase-entityid":
                qid_ref = v.get("id")
                if qid_ref:
                    vals.append(qid_ref)
                    qids_to_resolve.add(qid_ref)
            elif dv.get("type") == "time":
                t = v.get("time", "").lstrip("+").split("T")[0]
                vals.append(t)
            elif dv.get("type") == "string":
                vals.append(str(v))
        if vals:
            raw[key] = vals

    labels = resolve_labels(session, sorted(qids_to_resolve), lang) if qids_to_resolve else {}
    resolved: dict[str, list[str]] = {}
    for key, vals in raw.items():
        resolved[key] = [labels.get(v, v) for v in vals]

    label = ent.get("labels", {}).get(lang, {}).get("value")
    description = ent.get("descriptions", {}).get(lang, {}).get("value")

    return {
        "qid": qid,
        "label": label,
        "description": description,
        "properties": resolved,
    }


# ---------------------------------------------------------------------------
# 单个人物总流程
# ---------------------------------------------------------------------------
def safe_dirname(name: str) -> str:
    return re.sub(r"[^\w\-\.]+", "_", name).strip("_") or "unnamed"


def process_one(
    session: requests.Session,
    title: str,
    name: str,
    year: int,
    century: str,
    out_root: Path,
    lang: str = "en",
) -> dict:
    print(f"\n▶ {name} ({year})")
    person_dir = out_root / century / safe_dirname(title)
    person_dir.mkdir(parents=True, exist_ok=True)

    # 断点续传：已完成的跳过
    if (person_dir / "page.md").exists() and (person_dir / "metadata.json").exists():
        print("  · 已存在，跳过")
        return {"name": name, "title": title, "year": year, "century": century, "dir": str(person_dir), "skipped": True}

    print("  · 抓 HTML …")
    raw_html = fetch_html(session, title, lang)
    (person_dir / "page.html").write_text(raw_html, encoding="utf-8")

    print("  · HTML → Markdown …")
    cleaned, images = clean_html(raw_html, lang)
    markdown = html_to_markdown(cleaned)

    print("  · Wikidata …")
    qid = fetch_wikidata_qid(session, title, lang)
    meta: dict = {"name": name, "title": title, "year": year, "century": century, "lang": lang, "qid": qid}
    if qid:
        meta.update(extract_metadata(session, qid, lang))

    (person_dir / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    front = _build_frontmatter(name, lang, meta)
    (person_dir / "page.md").write_text(front + "\n\n" + markdown, encoding="utf-8")
    (person_dir / "images.txt").write_text("\n".join(images), encoding="utf-8")

    print(f"  ✓ {person_dir}  ({len(markdown):,} chars, {len(images)} images)")
    return {"name": name, "title": title, "year": year, "century": century, "dir": str(person_dir), "skipped": False}


def _build_frontmatter(name: str, lang: str, meta: dict) -> str:
    props = meta.get("properties", {}) if meta else {}
    lines = ["---", f"name: {json.dumps(name, ensure_ascii=False)}"]
    if meta.get("qid"):
        lines.append(f"wikidata: {meta['qid']}")
    if title := meta.get("title"):
        lines.append(f"wikipedia: https://{lang}.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}")
    if desc := meta.get("description"):
        lines.append(f"description: {json.dumps(desc, ensure_ascii=False)}")
    for key in ("date_of_birth", "date_of_death", "nationality",
                "field_of_work", "occupation", "award_received",
                "doctoral_advisor", "educated_at"):
        if vals := props.get(key):
            lines.append(f"{key}: {json.dumps(vals, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 索引
# ---------------------------------------------------------------------------
def write_index(results: list[dict], out_root: Path) -> None:
    lines = ["# 化学家完整页面索引（诺贝尔化学奖得主）\n",
             f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
             f"> 共 **{len(results)}** 人\n"]

    for century in ("20th_century", "21st_century"):
        subset = [r for r in results if r.get("century") == century]
        if not subset:
            continue
        label = "20 世纪" if century == "20th_century" else "21 世纪"
        lines.append(f"\n## {label}\n")
        for r in sorted(subset, key=lambda x: x["year"]):
            name = r["name"]
            title = r.get("title", name)
            year = r["year"]
            rel = Path(century) / safe_dirname(title) / "page.md"
            lines.append(f"- {year} — [{name}]({rel})")

    (out_root / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# 从上一步的诺贝尔奖名单 md 里解析 (year, name, url, century)
# ---------------------------------------------------------------------------
def parse_laureates_from_md(path: Path) -> list[dict]:
    laureates: list[dict] = []
    current_century: str | None = None
    row_pat = re.compile(r"^\|\s*(\d{4})\s*\|\s*\[([^\]]+)\]\((.+)\)\s*\|")

    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("## 20 世纪"):
            current_century = "20th_century"
            continue
        if s.startswith("## 21 世纪"):
            current_century = "21st_century"
            continue
        m = row_pat.match(s)
        if m and current_century:
            year = int(m.group(1))
            name = m.group(2).strip()
            url = m.group(3).strip()
            # 从 URL 提取精确的 wiki title（去掉 /wiki/ 前缀，URL 解码）
            title = unquote(url.rstrip("/").split("/wiki/")[-1]).replace("_", " ")
            laureates.append({"year": year, "name": name, "url": url, "title": title, "century": current_century})

    # 去重（如 John Bardeen 两次获奖），保留首次出现的世纪
    seen: set[str] = set()
    unique: list[dict] = []
    for l in laureates:
        key = l["title"]
        if key not in seen:
            seen.add(key)
            unique.append(l)
    return unique


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0, help="仅抓前 N 个（0=全部）")
    ap.add_argument("--only", type=str, default="", help="仅抓名字含此字符串的")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--sleep", type=float, default=0.5, help="请求间隔秒数")
    args = ap.parse_args()

    if not LIST_MD.exists():
        print(f"✗ 找不到名单文件：{LIST_MD}", file=sys.stderr)
        return 1

    laureates = parse_laureates_from_md(LIST_MD)
    if args.only:
        laureates = [l for l in laureates if args.only.lower() in l["name"].lower()]
    if args.limit:
        laureates = laureates[: args.limit]

    print(f"将抓取 {len(laureates)} 位化学家 → {OUT_ROOT.resolve()}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    session = build_session()
    results: list[dict] = []
    for i, l in enumerate(laureates, 1):
        print(f"\n===== [{i}/{len(laureates)}] =====")
        try:
            r = process_one(session, l["title"], l["name"], l["year"], l["century"], OUT_ROOT, args.lang)
            results.append(r)
        except Exception as e:
            print(f"  ✗ 失败：{e}")
        time.sleep(args.sleep)

    write_index(results, OUT_ROOT)
    print(f"\n✅ 完成。索引写入 {OUT_ROOT / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
