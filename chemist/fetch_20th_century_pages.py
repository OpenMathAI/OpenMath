#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下载 20 世纪诺贝尔化学奖得主的 Wikipedia 页面到本地。

HTTP 层使用 curl（subprocess 调用），规避 Python requests/urllib 被
Wikipedia 限流（403 Too Many Reqs）的问题。
本地处理（HTML 清洗、Markdown 转换、Wikidata 解析）复用 fetch_nobel_pages.py。

输出目录：presentations/20th_century/pages/{Name}/
每个子目录含：
  page.md          正文 Markdown（由 HTML 转换，含 frontmatter）
  page.html        原始 HTML（备份）
  metadata.json    Wikidata 元数据（生卒、领域、国籍、获奖等）
  images.txt       页面内图片 URL 清单
索引：presentations/20th_century/pages/INDEX.md

用法：
  python3 fetch_20th_century_pages.py --limit 3   # 仅抓前 3 个（测试用）
  python3 fetch_20th_century_pages.py             # 抓全部 20 世纪化学家
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

import fetch_nobel_pages as fp

ROOT = Path(__file__).resolve().parent
LIST_MD = ROOT / "presentations" / "Nobel_Chemistry_Laureates_20th_21st_Century.md"
OUT_ROOT = ROOT / "presentations" / "20th_century" / "pages"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def curl_get(url: str) -> str:
    """用 curl 下载 URL 内容并返回文本，带重试。

    -f 让 HTTP 4xx/5xx 返回非零退出码，避免把错误页当作成功响应。
    """
    cmd = ["curl", "-s", "-L", "--compressed", "-f", "-A", UA, url]
    for attempt in range(6):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        except subprocess.TimeoutExpired:
            if attempt == 5:
                raise
            time.sleep(3 * (2 ** attempt))
            continue
        if out.returncode == 0 and out.stdout:
            return out.stdout
        if attempt == 5:
            raise RuntimeError(f"curl failed ({out.returncode}): {out.stderr[:200]}")
        time.sleep(3 * (2 ** attempt))
    raise RuntimeError("unreachable")


def fetch_qid(title: str) -> str | None:
    url = (
        "https://en.wikipedia.org/w/api.php"
        "?action=query&prop=pageprops&ppprop=wikibase_item"
        f"&titles={quote(title, safe='')}&redirects=1&format=json&formatversion=2"
    )
    data = json.loads(curl_get(url))
    pages = data.get("query", {}).get("pages", [])
    if pages:
        return pages[0].get("pageprops", {}).get("wikibase_item")
    return None


def fetch_entity(qid: str) -> dict:
    data = json.loads(
        curl_get(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")
    )
    return data.get("entities", {}).get(qid, {})


def resolve_labels(qids: list[str], lang: str = "en") -> dict[str, str]:
    out: dict[str, str] = {}
    for i in range(0, len(qids), 50):
        batch = qids[i : i + 50]
        url = (
            "https://www.wikidata.org/w/api.php?action=wbgetentities"
            f"&ids={'|'.join(batch)}&props=labels&languages={lang}&format=json"
        )
        data = json.loads(curl_get(url))
        for qid, ent in data.get("entities", {}).items():
            label = ent.get("labels", {}).get(lang, {}).get("value")
            if label:
                out[qid] = label
    return out


def build_metadata(qid: str, lang: str = "en") -> dict:
    """复用 fp.WANTED_PROPS 的字段映射，用 curl 下载的数据构建元数据。"""
    ent = fetch_entity(qid)
    claims = ent.get("claims", {})

    raw: dict[str, list[str]] = {}
    qids_to_resolve: set[str] = set()

    for pid, key in fp.WANTED_PROPS.items():
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
                vals.append(v.get("time", "").lstrip("+").split("T")[0])
            elif dv.get("type") == "string":
                vals.append(str(v))
        if vals:
            raw[key] = vals

    labels = resolve_labels(sorted(qids_to_resolve), lang) if qids_to_resolve else {}
    resolved = {k: [labels.get(v, v) for v in vals] for k, vals in raw.items()}

    label = ent.get("labels", {}).get(lang, {}).get("value")
    description = ent.get("descriptions", {}).get(lang, {}).get("value")

    return {
        "qid": qid,
        "label": label,
        "description": description,
        "properties": resolved,
    }


def process_one(title: str, name: str, year: int, lang: str = "en") -> dict:
    person_dir = OUT_ROOT / fp.safe_dirname(title)
    person_dir.mkdir(parents=True, exist_ok=True)

    if (person_dir / "page.md").exists() and (person_dir / "metadata.json").exists():
        print(f"  · 已存在，跳过：{name}")
        return {"name": name, "title": title, "year": year, "dir": str(person_dir), "skipped": True}

    print(f"▶ {name} ({year})")

    print("  · 抓 HTML …")
    raw_html = curl_get(
        f"https://en.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
    )
    (person_dir / "page.html").write_text(raw_html, encoding="utf-8")

    print("  · HTML → Markdown …")
    cleaned, images = fp.clean_html(raw_html, lang)
    markdown = fp.html_to_markdown(cleaned)

    print("  · Wikidata …")
    qid = None
    meta: dict = {
        "name": name,
        "title": title,
        "year": year,
        "century": "20th_century",
        "lang": lang,
        "qid": qid,
    }
    try:
        qid = fetch_qid(title)
        meta["qid"] = qid
        if qid:
            meta.update(build_metadata(qid, lang))
    except Exception as e:
        print(f"  ! Wikidata 获取失败（降级，不影响 page.md）：{e}")

    (person_dir / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    front = fp._build_frontmatter(name, lang, meta)
    (person_dir / "page.md").write_text(front + "\n\n" + markdown, encoding="utf-8")
    (person_dir / "images.txt").write_text("\n".join(images), encoding="utf-8")

    print(f"  ✓ {person_dir.name}  ({len(markdown):,} chars, {len(images)} images)")
    return {"name": name, "title": title, "year": year, "dir": str(person_dir), "skipped": False}


def write_index(results: list[dict]) -> None:
    lines = [
        "# 化学家完整页面索引（20 世纪诺贝尔化学奖得主）",
        "",
        f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 共 **{len(results)}** 人",
        "",
        "## 20 世纪",
        "",
    ]
    for r in sorted(results, key=lambda x: x["year"]):
        rel = fp.safe_dirname(r["title"]) + "/page.md"
        lines.append(f"- {r['year']} — [{r['name']}]({rel})")
    (OUT_ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0, help="仅抓前 N 个（0=全部）")
    args = ap.parse_args()

    if not LIST_MD.exists():
        print(f"✗ 找不到名单文件：{LIST_MD}", file=sys.stderr)
        return 1

    laureates = fp.parse_laureates_from_md(LIST_MD)
    c20 = [l for l in laureates if l["century"] == "20th_century"]
    if args.limit:
        c20 = c20[: args.limit]

    print(f"将抓取 {len(c20)} 位 20 世纪化学家 → {OUT_ROOT.resolve()}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    for i, l in enumerate(c20, 1):
        print(f"\n===== [{i}/{len(c20)}] =====")
        try:
            r = process_one(l["title"], l["name"], l["year"])
            results.append(r)
        except Exception as e:
            print(f"  ✗ 失败：{e}")
        time.sleep(1.2)

    write_index(results)
    print(f"\n✅ 完成。索引写入 {OUT_ROOT / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
