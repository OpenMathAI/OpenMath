#!/usr/bin/env python3
"""
curl 版 Wikipedia 数学家页面抓取（规避 requests 403 限流）。

复用 fetch_full_pages.py 的清洗/转换纯函数，HTTP 层改用 curl。
每个数学家生成：
  pages/<DirName>/page.md
  pages/<DirName>/page.html
  pages/<DirName>/metadata.json
  pages/<DirName>/images.txt
并在 pages/ 下生成 INDEX.md。

用法：
  python3 fetch_pages_curl.py --century 17th
  python3 fetch_pages_curl.py --century 18th
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote, urlencode

# 复用 fetch_full_pages.py 的纯函数
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_full_pages import (
    clean_html,
    html_to_markdown,
    _build_frontmatter,
    WANTED_PROPS,
)

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# title -> 目录名（处理消歧义与目录命名）
CENTURY_17 = [
    ("Marin Mersenne", "Marin_Mersenne"),
    ("René Descartes", "René_Descartes"),
    ("Bonaventura Cavalieri", "Bonaventura_Cavalieri"),
    ("Pierre de Fermat", "Pierre_de_Fermat"),
    ("Evangelista Torricelli", "Evangelista_Torricelli"),
    ("John Wallis", "John_Wallis"),
    ("Blaise Pascal", "Blaise_Pascal"),
    ("Christiaan Huygens", "Christiaan_Huygens"),
    ("Isaac Barrow", "Isaac_Barrow"),
    ("James Gregory (mathematician)", "James_Gregory"),
    ("Isaac Newton", "Isaac_Newton"),
    ("Gottfried Wilhelm Leibniz", "Gottfried_Wilhelm_Leibniz"),
    ("Jacob Bernoulli", "Jacob_Bernoulli"),
    ("Johann Bernoulli", "Johann_Bernoulli"),
]

CENTURY_18 = [
    ("Abraham de Moivre", "Abraham_de_Moivre"),
    ("Brook Taylor", "Brook_Taylor"),
    ("Colin Maclaurin", "Colin_Maclaurin"),
    ("Daniel Bernoulli", "Daniel_Bernoulli"),
    ("Leonhard Euler", "Leonhard_Euler"),
    ("Alexis Clairaut", "Alexis_Clairaut"),
    ("Jean le Rond d'Alembert", "Jean_le_Rond_d'Alembert"),
    ("Johann Heinrich Lambert", "Johann_Heinrich_Lambert"),
    ("Étienne Bézout", "Étienne_Bézout"),
    ("Edward Waring", "Edward_Waring"),
    ("Joseph-Louis Lagrange", "Joseph-Louis_Lagrange"),
    ("Gaspard Monge", "Gaspard_Monge"),
    ("Pierre-Simon Laplace", "Pierre-Simon_Laplace"),
]


# ---------------------------------------------------------------------------
# HTTP（curl）
# ---------------------------------------------------------------------------
def curl_get(url: str, params: dict | None = None, retries: int = 6) -> str:
    if params:
        url = url + ("&" if "?" in url else "?") + urlencode(params)
    text = ""
    for attempt in range(retries):
        cmd = ["curl", "-s", "-L", "--max-time", "60", "-A", UA, url]
        r = subprocess.run(cmd, capture_output=True)
        text = r.stdout.decode("utf-8", errors="replace")
        if r.returncode != 0:
            raise RuntimeError(f"curl failed ({r.returncode})")
        if "making too many requests" in text or "too many requests" in text.lower():
            wait = 8 * (2 ** attempt)
            print(f"    ! 限流，{wait}s 后重试 (attempt {attempt + 1}/{retries})")
            time.sleep(wait)
            continue
        return text
    return text


def curl_get_json(url: str, params: dict | None = None) -> dict:
    return json.loads(curl_get(url, params))


def fetch_html(title: str, lang: str = "en") -> str:
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/html/{quote(title, safe='')}"
    return curl_get(url)


def fetch_wikidata_qid(title: str, lang: str = "en") -> str | None:
    data = curl_get_json(
        f"https://{lang}.wikipedia.org/w/api.php",
        {
            "action": "query",
            "prop": "pageprops",
            "ppprop": "wikibase_item",
            "titles": title,
            "redirects": 1,
            "format": "json",
            "formatversion": "2",
        },
    )
    pages = data.get("query", {}).get("pages", [])
    if pages:
        return pages[0].get("pageprops", {}).get("wikibase_item")
    return None


def fetch_wikidata_entity(qid: str) -> dict:
    return curl_get_json(
        f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    ).get("entities", {}).get(qid, {})


def resolve_labels(qids: list[str], lang: str = "en") -> dict[str, str]:
    out: dict[str, str] = {}
    for i in range(0, len(qids), 50):
        batch = qids[i : i + 50]
        data = curl_get_json(
            "https://www.wikidata.org/w/api.php",
            {
                "action": "wbgetentities",
                "ids": "|".join(batch),
                "props": "labels",
                "languages": lang,
                "format": "json",
            },
        )
        for qid, ent in data.get("entities", {}).items():
            label = ent.get("labels", {}).get(lang, {}).get("value")
            if label:
                out[qid] = label
    return out


def extract_metadata(qid: str, lang: str = "en") -> dict:
    ent = fetch_wikidata_entity(qid)
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
                vals.append(v.get("time", "").lstrip("+").split("T")[0])
            elif dv.get("type") == "string":
                vals.append(str(v))
        if vals:
            raw[key] = vals

    labels = resolve_labels(sorted(qids_to_resolve), lang) if qids_to_resolve else {}
    resolved = {k: [labels.get(v, v) for v in vals] for k, vals in raw.items()}

    return {
        "qid": qid,
        "label": ent.get("labels", {}).get(lang, {}).get("value"),
        "description": ent.get("descriptions", {}).get(lang, {}).get("value"),
        "properties": resolved,
    }


# ---------------------------------------------------------------------------
# 单个人物
# ---------------------------------------------------------------------------
def process_one(title: str, dirname: str, out_root: Path, lang: str = "en") -> dict:
    print(f"\n▶ {title}  →  {dirname}")
    person_dir = out_root / dirname
    person_dir.mkdir(parents=True, exist_ok=True)

    # 1) HTML
    print("  · 抓 HTML …")
    raw_html = fetch_html(title, lang)
    (person_dir / "page.html").write_text(raw_html, encoding="utf-8")

    # 2) 清洗 + 转 Markdown
    print("  · HTML → Markdown …")
    cleaned, images = clean_html(raw_html, lang)
    markdown = html_to_markdown(cleaned)

    # 3) Wikidata 元数据（失败不阻断正文写入）
    print("  · Wikidata …")
    meta: dict = {"name": title, "lang": lang, "qid": None}
    try:
        qid = fetch_wikidata_qid(title, lang)
        meta["qid"] = qid
        if qid:
            meta.update(extract_metadata(qid, lang))
    except Exception as e:
        print(f"    ! Wikidata 失败（不阻断）：{type(e).__name__}: {e}")

    (person_dir / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 4) frontmatter + markdown
    front = _build_frontmatter(title, lang, meta)
    (person_dir / "page.md").write_text(front + "\n\n" + markdown, encoding="utf-8")

    # 5) 图片清单
    (person_dir / "images.txt").write_text("\n".join(images), encoding="utf-8")

    print(f"  ✓ {person_dir}  ({len(markdown):,} chars, {len(images)} images)")
    return {"name": title, "dir": str(person_dir), "meta": meta}


def write_index(results: list[dict], out_root: Path) -> None:
    lines = [
        "# 数学家完整页面索引\n",
        f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 共 **{len(results)}** 人\n",
    ]
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


def main() -> int:
    century = sys.argv[sys.argv.index("--century") + 1] if "--century" in sys.argv else None
    if century not in ("17th", "18th"):
        print("用法: python3 fetch_pages_curl.py --century {17th|18th}")
        return 2

    people = CENTURY_17 if century == "17th" else CENTURY_18
    out_root = Path(__file__).resolve().parent / "presentations" / f"{century}_century" / "pages"
    out_root.mkdir(parents=True, exist_ok=True)

    print(f"将抓取 {len(people)} 位 {century} 世纪数学家 → {out_root}")
    results: list[dict] = []
    for i, (title, dirname) in enumerate(people, 1):
        print(f"\n===== [{i}/{len(people)}] =====")
        person_dir = out_root / dirname
        md = person_dir / "page.md"
        if md.exists() and md.stat().st_size > 2000:
            print(f"  ⏭ 跳过（已存在 {md.stat().st_size:,} 字节）")
            try:
                meta = json.loads((person_dir / "metadata.json").read_text(encoding="utf-8"))
            except Exception:
                meta = {"name": title}
            results.append({"name": title, "dir": str(person_dir), "meta": meta})
            continue
        try:
            results.append(process_one(title, dirname, out_root))
        except Exception as e:
            print(f"  ✗ 失败：{type(e).__name__}: {e}")
        time.sleep(3.0)

    write_index(results, out_root)
    print(f"\n✅ 完成。索引写入 {out_root / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
