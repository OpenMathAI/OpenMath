#!/usr/bin/env python3
"""
完整抓取 Wikipedia 数学家页面 —— 示例版。

每个人物会生成：
  pages/<Name>/page.md          正文 Markdown（由 HTML 转换）
  pages/<Name>/page.html        原始 HTML（备份）
  pages/<Name>/metadata.json    Wikidata 元数据（生卒、领域、国籍、获奖等）
  pages/<Name>/images.txt       页面内图片 URL 清单

并在 pages/INDEX.md 生成总索引。

用法：
  # 示例：抓 5 位著名数学家
  python3 fetch_full_pages.py --sample

  # 从一个 txt 文件（每行一个人名）批量抓
  python3 fetch_full_pages.py --from-list names.txt

  # 指定数量（与上一步生成的 mathematicians.md 联动）
  python3 fetch_full_pages.py --from-md mathematicians.md --limit 20

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
from typing import Iterable
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

USER_AGENT = (
    "MathematiciansFetcher/1.0 "
    "(https://example.org/contact; educational use) python-requests"
)

SAMPLE_NAMES = [
    "Carl Friedrich Gauss",
    "Leonhard Euler",
    "Bernhard Riemann",
    "Emmy Noether",
    "Alexander Grothendieck",
]


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
    """
    使用 Wikimedia REST API 获取渲染后的 HTML。
    文档：https://en.wikipedia.org/api/rest_v1/#/Page%20content/get_page_html__title_
    """
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
    r = http_get(session, url, headers={"Accept": "text/html; charset=utf-8"})
    return r.text


# ---------------------------------------------------------------------------
# 2) HTML -> Markdown（清洗 + 转换）
# ---------------------------------------------------------------------------
# 需要从正文中剔除的节点（侧栏、编辑按钮、脚注回链等）
_REMOVE_SELECTORS = [
    "style", "script", "link", "meta",
    "sup.reference",                  # 脚注 [1][2] 的上标
    ".mw-editsection",                # "[edit]" 小按钮
    ".mw-empty-elt",
    ".noprint",
    ".navbox", ".vertical-navbox",    # 底部巨型导航框
    ".metadata",
    ".hatnote", ".shortdescription",
    ".mw-jump-link",
    ".reflist",                       # 超长的参考文献列表（保留引用编号但不要全文）
    "#References ~ *",                # References 之后的所有内容（粗暴但常见）
    "table.infobox .infobox-image img",  # infobox 里直接嵌的图（下方会单独处理）
]


def clean_html(html: str, lang: str) -> tuple[str, list[str]]:
    """
    清洗 HTML，并返回 (cleaned_html, image_urls)。
    图片 URL 补全为绝对地址。
    """
    soup = BeautifulSoup(html, "html.parser")

    # 去掉明显冗余的节点
    for sel in _REMOVE_SELECTORS:
        for node in soup.select(sel):
            node.decompose()

    # 收集图片 URL（补全协议 & 相对路径）
    images: list[str] = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        src = _absolutize(src, lang)
        images.append(src)
        # 保留 img 节点以便 markdownify 生成 ![]()
        img["src"] = src
        # srcset 里还有多分辨率候选，统一补全
        if img.has_attr("srcset"):
            img["srcset"] = _absolutize_srcset(img["srcset"], lang)

    # 维基的内链相对地址 -> 绝对地址
    for a in soup.find_all("a", href=True):
        a["href"] = _absolutize(a["href"], lang, wiki_prefix=True)

    # 插入 <base> 作为兜底（本地打开 html 时，相对路径也能正确解析）
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

    # 确保有 <meta charset>
    if not head.find("meta", attrs={"charset": True}):
        head.insert(0, soup.new_tag("meta", charset="utf-8"))

    return str(soup), images


def _absolutize(url: str, lang: str, wiki_prefix: bool = False) -> str:
    """把 MediaWiki REST API 返回的各种相对地址补全成绝对地址。"""
    if not url:
        return url
    if url.startswith(("http://", "https://", "data:", "mailto:", "#")):
        return url
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return f"https://{lang}.wikipedia.org" + url
    if url.startswith("./"):
        # REST 返回的 ./Foo_bar 相对路径；a 标签要加 /wiki/，img 标签已经是图片资源
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
    """用 markdownify 转换，并做一些善后清理。"""
    text = md(
        html,
        heading_style="ATX",       # #、## …
        bullets="-",
        strip=["span"],            # 去掉 <span> 让文本更干净
    )
    # 去掉多余空行（3+ 连续空行 → 2 行）
    text = re.sub(r"\n{3,}", "\n\n", text)
    # 去掉行尾空格
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# 3) Wikidata 元数据
# ---------------------------------------------------------------------------
def fetch_wikidata_qid(session: requests.Session, title: str, lang: str = "en") -> str | None:
    """通过 wiki title 反查 Wikidata QID。"""
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


# 感兴趣的属性 → 人类可读标签
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
    """批量把 QID 翻译成人类可读的 label。"""
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


def extract_metadata(
    session: requests.Session, qid: str, lang: str = "en"
) -> dict:
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
                # "+1777-04-30T00:00:00Z" -> "1777-04-30"
                t = v.get("time", "").lstrip("+").split("T")[0]
                vals.append(t)
            elif dv.get("type") == "string":
                vals.append(str(v))
        if vals:
            raw[key] = vals

    # 把 QID 批量翻译成 label
    labels = resolve_labels(session, sorted(qids_to_resolve), lang) if qids_to_resolve else {}
    resolved: dict[str, list[str]] = {}
    for key, vals in raw.items():
        resolved[key] = [labels.get(v, v) for v in vals]

    # 顶层常用字段
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
    session: requests.Session, name: str, out_root: Path, lang: str = "en"
) -> dict:
    print(f"\n▶ {name}")
    person_dir = out_root / safe_dirname(name)
    person_dir.mkdir(parents=True, exist_ok=True)

    # 1) HTML
    print("  · 抓 HTML …")
    raw_html = fetch_html(session, name, lang)
    (person_dir / "page.html").write_text(raw_html, encoding="utf-8")

    # 2) 清洗 + 转 Markdown
    print("  · HTML → Markdown …")
    cleaned, images = clean_html(raw_html, lang)
    markdown = html_to_markdown(cleaned)

    # 3) Wikidata 元数据
    print("  · Wikidata …")
    qid = fetch_wikidata_qid(session, name, lang)
    meta: dict = {"name": name, "lang": lang, "qid": qid}
    if qid:
        meta.update(extract_metadata(session, qid, lang))

    (person_dir / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 4) 在 Markdown 顶部加入 YAML frontmatter，便于静态站点 / 检索
    front = _build_frontmatter(name, lang, meta)
    (person_dir / "page.md").write_text(front + "\n\n" + markdown, encoding="utf-8")

    # 5) 图片清单
    (person_dir / "images.txt").write_text("\n".join(images), encoding="utf-8")

    print(f"  ✓ {person_dir}  ({len(markdown):,} chars, {len(images)} images)")
    return {"name": name, "dir": str(person_dir), "meta": meta}


def _build_frontmatter(name: str, lang: str, meta: dict) -> str:
    props = meta.get("properties", {}) if meta else {}
    lines = ["---", f"name: {json.dumps(name, ensure_ascii=False)}"]
    if meta.get("qid"):
        lines.append(f"wikidata: {meta['qid']}")
    lines.append(f"wikipedia: https://{lang}.wikipedia.org/wiki/{quote(name.replace(' ', '_'))}")
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
    lines = ["# 数学家完整页面索引\n",
             f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
             f"> 共 **{len(results)}** 人\n"]
    for r in sorted(results, key=lambda x: x["name"].lower()):
        meta = r.get("meta", {})
        props = meta.get("properties", {})
        desc = meta.get("description") or ""
        birth = (props.get("date_of_birth") or [""])[0]
        death = (props.get("date_of_death") or [""])[0]
        years = f"（{birth[:4]}–{death[:4]}）" if birth else ""
        rel = Path(r["dir"]).relative_to(out_root) / "page.md"
        lines.append(f"- [{r['name']}]({rel}) {years} — {desc}")
    (out_root / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# 从上一步的 md 里抽取人名
# ---------------------------------------------------------------------------
def parse_names_from_md(path: Path) -> list[str]:
    names: list[str] = []
    pat = re.compile(r"^- \[([^\]]+)\]\(")
    for line in path.read_text(encoding="utf-8").splitlines():
        m = pat.match(line)
        if m:
            names.append(m.group(1))
    return names


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sample", action="store_true", help="示例：抓 5 位著名数学家")
    g.add_argument("--from-list", type=Path, help="从 txt 文件读取人名（每行一个）")
    g.add_argument("--from-md", type=Path, help="从上一步的 mathematicians.md 读取人名")

    ap.add_argument("--limit", type=int, default=0, help="仅抓前 N 个")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--out", type=Path, default=Path("pages"), help="输出目录")
    ap.add_argument("--sleep", type=float, default=0.5, help="请求间隔秒数")
    args = ap.parse_args()

    if args.sample:
        names = SAMPLE_NAMES
    elif args.from_list:
        names = [ln.strip() for ln in args.from_list.read_text("utf-8").splitlines() if ln.strip()]
    else:
        names = parse_names_from_md(args.from_md)

    if args.limit:
        names = names[: args.limit]

    print(f"将抓取 {len(names)} 位数学家 → {args.out.resolve()}")
    args.out.mkdir(parents=True, exist_ok=True)

    session = build_session()
    results: list[dict] = []
    for i, name in enumerate(names, 1):
        print(f"\n===== [{i}/{len(names)}] =====")
        try:
            r = process_one(session, name, args.out, args.lang)
            results.append(r)
        except Exception as e:
            print(f"  ✗ 失败：{e}")
        time.sleep(args.sleep)

    write_index(results, args.out)
    print(f"\n✅ 完成。索引写入 {args.out / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
