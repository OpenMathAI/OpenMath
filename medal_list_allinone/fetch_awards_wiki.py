#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Wikipedia 下载奖项定义页（Fields / Abel / Wolf / Chern / Turing / Nobel /
统计 / 跨学科等），组织方式参考 Fields_Medal/fetch_pages.py：

  pages/<category>/<Title>/index.html       完整 HTML（含 Wikipedia CSS，离线可浏览）
  pages/<category>/<Title>/images/          页面内图片
  pages/<category>/<Title>/metadata.json    元数据（标题/链接/分类/简介）

分类定义见 AWARD_SECTIONS（与 awards_list.md 对应）。
用法:
  python3 fetch_awards_wiki.py                    # 下载全部分类
  python3 fetch_awards_wiki.py --section math     # 只下载 math 分类
  python3 fetch_awards_wiki.py --list             # 列出所有分类
  python3 fetch_awards_wiki.py --no-images        # 只存 HTML 不下载图片
依赖:
  pip install requests beautifulsoup4
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, urljoin, urlparse, unquote

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
USER_AGENT = (
    "OpenMathAIBot/1.0 "
    "(https://github.com/OpenMathAI; educational use) "
    "python-requests"
)

PAGES_DIR = Path(__file__).parent / "pages"
RATE_LIMIT = 1.2
DOWNLOAD_IMAGES = True

# ---------------------------------------------------------------------------
# 奖项分类：key -> (分类中文名, [(显示名, lang, wiki_title, 简介)])
# 与 awards_list.md 的 7 大类一一对应
# ---------------------------------------------------------------------------
AWARD_SECTIONS = {
    "math_top": ("数学奖 · 第一梯队", [
        ("菲尔兹奖", "en", "Fields Medal",
         "青年数学家最高荣誉，每 4 年于 ICM 颁发，40 岁以下"),
        ("阿贝尔奖", "en", "Abel Prize",
         "数学终身成就，挪威政府颁发"),
        ("沃尔夫数学奖", "en", "Wolf Prize in Mathematics",
         "以色列沃尔夫基金会，数学终身成就"),
        ("陈省身奖章", "en", "Chern Medal",
         "IMU 数学终身荣誉，纪念陈省身"),
    ]),
    "math_icm": ("数学奖 · ICM 配套", [
        ("内万林纳奖", "en", "Rolf Nevanlinna Prize",
         "ICM 理论计算机/信息科学方向，40 岁以下"),
        ("高斯奖", "en", "Gauss Prize",
         "ICM 应用数学奖"),
        ("哥德尔奖", "en", "Gödel Prize",
         "理论计算机：算法、计算复杂性、形式方法"),
    ]),
    "computer": ("计算机奖", [
        ("图灵奖", "en", "Turing Award",
         "计算机科学最高荣誉，ACM 颁发"),
        ("高德纳奖", "en", "Knuth Prize",
         "ACM SIGACT，算法设计与编程基础终身贡献"),
        ("迪杰斯特拉奖", "en", "Edsger W. Dijkstra Prize",
         "ACM PODC + EATCS，分布式计算（Wiki 重定向到 PODC 会议页）"),
        ("IEEE 冯·诺依曼奖章", "en", "IEEE John von Neumann Medal",
         "计算机科学/工程杰出终身贡献"),
        ("IEEE 汉明奖章", "en", "IEEE Richard W. Hamming Medal",
         "信息论、编码理论、数据通信"),
        ("IEEE 香农奖", "en", "Claude E. Shannon Award",
         "信息论领域杰出贡献"),
        ("EATCS 奖", "en", "EATCS Award",
         "理论计算机科学终身贡献"),
        ("千禧科技奖", "en", "Millennium Technology Prize",
         "芬兰，促进人类福祉的创新技术"),
        ("马可尼奖", "en", "Marconi Prize",
         "通信与信息技术杰出贡献"),
    ]),
    "statistics": ("统计学奖", [
        ("考普斯会长奖", "en", "COPSS Presidents' Award",
         "统计学界青年最高荣誉"),
        ("国际统计学奖", "en", "International Prize in Statistics",
         "统计学界的诺贝尔奖（终身成就）"),
        ("R. A. Fisher 讲座", "en", "R. A. Fisher Lectureship",
         "ASA 最负盛名讲座荣誉"),
        ("C. R. 拉奥奖", "en", "C. R. Rao",
         "宾州州立大学，统计学杰出研究（无独立奖项页，用人物页）"),
        ("诺伯特·维纳奖", "en", "Norbert Wiener Prize in Applied Mathematics",
         "AMS+SIAM，应用数学与控制交叉"),
    ]),
    "nobel": ("诺贝尔奖家族", [
        ("诺贝尔物理学奖", "en", "Nobel Prize in Physics",
         "物理学最高荣誉"),
        ("诺贝尔化学奖", "en", "Nobel Prize in Chemistry",
         "化学最高荣誉"),
        ("诺贝尔生理学或医学奖", "en", "Nobel Prize in Physiology or Medicine",
         "生理/医学最高荣誉"),
        ("诺贝尔经济学奖", "en", "Nobel Memorial Prize in Economic Sciences",
         "经济学最高荣誉"),
    ]),
    "cross": ("跨学科大奖", [
        ("京都奖", "en", "Kyoto Prize",
         "稻盛和夫京都奖财团，基础科学/尖端科技/精神哲学"),
        ("邵逸夫奖", "en", "Shaw Prize",
         "东方诺贝尔奖，数学科学/生命科学/天文"),
        ("数学突破奖", "en", "Breakthrough Prize in Mathematics",
         "数学界最高奖金"),
        ("克拉福德奖", "en", "Crafoord Prize",
         "瑞典皇家科学院，补诺贝尔奖未覆盖领域"),
        ("麦克阿瑟奖", "en", "MacArthur Fellows Program",
         "天才奖，无附加条件 fellowship"),
        ("拉马努金奖", "en", "Ramanujan Prize",
         "ICTP，45 岁以下发展中国家数学家"),
        ("晨兴数学金奖", "en", "Morningside Medal",
         "青年华人数学家"),
    ]),
    "national": ("国家级学术荣誉", [
        ("美国国家科学奖章", "en", "National Medal of Science",
         "美国科学界最高荣誉"),
        ("美国国家技术奖章", "en", "National Medal of Technology and Innovation",
         "美国技术领域最高荣誉"),
        ("美国国家科学院院士", "en", "Member of the National Academy of Sciences",
         "美国科学界院士最高荣誉"),
        ("美国国家工程院院士", "en", "Member of the National Academy of Engineering",
         "美国工程界院士最高荣誉"),
        ("英国皇家学会院士", "en", "Fellow of the Royal Society",
         "英国科学界院士最高荣誉"),
        ("加拿大总督创新奖", "en", "Governor General's Awards",
         "加拿大创新领域最高荣誉（无独立奖项页，用总督奖总页）"),
    ]),
}

SECTION_ORDER = ["math_top", "math_icm", "computer", "statistics", "nobel", "cross", "national"]

# ---------------------------------------------------------------------------
# HTTP 工具
# ---------------------------------------------------------------------------
_session = None


def get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update({"User-Agent": USER_AGENT})
    return _session


def http_get(url: str, **kwargs) -> requests.Response:
    session = get_session()
    for attempt in range(4):
        try:
            r = session.get(url, timeout=60, **kwargs)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            if attempt == 3:
                raise
            wait = 2 ** attempt
            print(f"    ! {e}, {wait}s 后重试", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError("unreachable")


# ---------------------------------------------------------------------------
# 获取完整渲染页面（带格式）
# ---------------------------------------------------------------------------
def fetch_full_page(title: str, lang: str = "en") -> tuple[str, str, list[str]]:
    base = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": title,
        "prop": "text|images|displaytitle",
        "format": "json",
        "formatversion": "2",
    }
    r = http_get(base, params=params)
    data = r.json()
    parse = data.get("parse", {})
    return parse.get("text", ""), parse.get("displaytitle", title), parse.get("images", [])


def resolve_title(title: str, lang: str = "en") -> str | None:
    base = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query", "titles": title, "format": "json",
        "formatversion": "2", "redirects": "1",
    }
    try:
        r = http_get(base, params=params)
        data = r.json()
        for page in data.get("query", {}).get("pages", []):
            if not page.get("missing", False):
                return page["title"]
        return None
    except Exception:
        return None


def safe_image_filename(url: str) -> str:
    parsed = urlparse(url)
    filename = unquote(Path(parsed.path).name)
    filename = re.sub(r'[<>:"/\\|?*@#()&,\[\]{}]', '_', filename)
    filename = re.sub(r'_+', '_', filename)
    if len(filename) > 100:
        ext = Path(filename).suffix
        filename = filename[:95] + ext
    return filename


def download_image(url: str, save_path: Path) -> bool:
    if save_path.exists():
        return True
    try:
        r = get_session().get(url, timeout=30, stream=True)
        r.raise_for_status()
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# 处理 HTML
# ---------------------------------------------------------------------------
FULL_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - Wikipedia</title>
<link rel="stylesheet" href="https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%7Cmediawiki.skinning.content.externallinks%7Cskins.vector.styles&only=styles">
<link rel="stylesheet" href="https://en.wikipedia.org/w/load.php?lang=en&modules=site.styles&only=styles">
<style>
body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6; color: #202122; background: #fff;
    max-width: 980px; margin: 0 auto; padding: 20px 30px;
}}
h1 {{ font-size: 1.8em; border-bottom: 1px solid #a2a9b1; padding-bottom: 0.15em; margin-top: 0; }}
h2 {{ font-size: 1.5em; border-bottom: 1px solid #a2a9b1; padding-bottom: 0.15em; }}
a {{ color: #0645ad; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
table {{ border-collapse: collapse; margin: 0.5em 0; }}
.infobox {{ border: 1px solid #a2a9b1; background: #f8f9fa; float: right; clear: right;
    margin: 0.5em 0 0.5em 1.4em; padding: 0.2em; max-width: 22em; font-size: 88%; line-height: 1.5; }}
.infobox th, .infobox td {{ padding: 0.2em 0.4em; vertical-align: top; }}
.infobox th {{ text-align: left; }}
.infobox-title {{ font-size: 125%; font-weight: bold; text-align: center; padding: 0.3em; background: #ccccff; }}
.wikitable {{ background: #f8f9fa; border: 1px solid #a2a9b1; margin: 1em 0; color: #202122; }}
.wikitable th {{ background: #eaecf0; text-align: center; border: 1px solid #a2a9b1; padding: 0.2em 0.4em; }}
.wikitable td {{ border: 1px solid #a2a9b1; padding: 0.2em 0.4em; }}
figure, .thumb {{ margin: 0.5em 0 0.8em 1.4em; float: right; clear: right; max-width: 300px;
    border: 1px solid #c8ccd1; background: #f8f9fa; padding: 3px; }}
figure img, .thumb img {{ display: block; max-width: 100%; height: auto; }}
figcaption, .thumbcaption {{ font-size: 0.88em; line-height: 1.4; padding: 3px; color: #555; }}
img {{ max-width: 100%; height: auto; }}
.mw-editsection {{ display: none; }}
.mw-parser-output::after {{ content: ""; display: table; clear: both; }}
ul.gallery {{ list-style: none; margin: 1em 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px; }}
ul.gallery li.gallerybox {{ display: inline-block; vertical-align: top; text-align: center; }}
ul.gallery li.gallerybox .gallerytext {{ font-size: 0.85em; padding: 4px; max-width: 180px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<div class="mw-parser-output">
{article_body}
</div>
<hr>
<footer style="font-size:0.85em;color:#666;margin-top:2em;">
<p>Source: <a href="https://{lang}.wikipedia.org/wiki/{title}">Wikipedia</a> | Downloaded for offline reading</p>
</footer>
</body>
</html>"""


def process_html(article_html: str, title: str, lang: str) -> tuple[str, dict]:
    soup = BeautifulSoup(article_html, "html.parser")
    for sel in [".mw-editsection", ".noprint", ".mw-empty-elt",
                ".navbox", ".vertical-navbox", ".sistersitebox"]:
        for node in soup.select(sel):
            node.decompose()

    img_map: dict[str, str] = {}
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src:
            continue
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = f"https://{lang}.wikipedia.org" + src
        width = img.get("width", "")
        try:
            if width and int(width) < 15:
                continue
        except (ValueError, TypeError):
            pass
        if DOWNLOAD_IMAGES:
            local_path = f"images/{safe_image_filename(src)}"
            img_map[src] = local_path
            img["src"] = local_path
        srcset = img.get("srcset", "")
        if srcset:
            new_parts = []
            for part in srcset.split(","):
                part = part.strip()
                if not part:
                    continue
                tokens = part.split(None, 1)
                url = tokens[0]
                if url.startswith("//"):
                    url = "https:" + url
                elif url.startswith("/"):
                    url = f"https://{lang}.wikipedia.org" + url
                if DOWNLOAD_IMAGES:
                    lp2 = f"images/{safe_image_filename(url)}"
                    img_map[url] = lp2
                    tokens[0] = lp2
                new_parts.append(" ".join(tokens))
            img["srcset"] = ", ".join(new_parts)

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("/wiki/", "/w/", "/")):
            a["href"] = f"https://{lang}.wikipedia.org" + href

    article_body = str(soup)
    full_html = FULL_PAGE_TEMPLATE.format(title=title, lang=lang, article_body=article_body)
    return full_html, img_map


# ---------------------------------------------------------------------------
# 下载单个奖项
# ---------------------------------------------------------------------------
def download_entry(section_key: str, display: str, lang: str, wiki_title: str, note: str) -> bool:
    real_title = resolve_title(wiki_title, lang)
    if not real_title:
        print(f"  ✗ ({lang}) {wiki_title} [NOT FOUND]", file=sys.stderr)
        return False

    safe_name = re.sub(r'[<>:"/\\|?*]', '_', real_title)
    out_dir = PAGES_DIR / section_key / safe_name
    out_dir.mkdir(parents=True, exist_ok=True)

    html_file = out_dir / "index.html"
    if html_file.exists() and html_file.stat().st_size > 1000:
        print(f"  ● ({lang}) {real_title} [已存在, 跳过]", file=sys.stderr)
        return True

    try:
        article_html, display_title, image_files = fetch_full_page(real_title, lang)
        processed_html, img_map = process_html(article_html, real_title, lang)
        html_file.write_text(processed_html, encoding="utf-8")

        if DOWNLOAD_IMAGES and img_map:
            img_dir = out_dir / "images"
            img_dir.mkdir(exist_ok=True)
            downloaded = 0
            for url, local_path in img_map.items():
                if download_image(url, out_dir / local_path):
                    downloaded += 1
            print(f"  ✓ ({lang}) {real_title} [{downloaded}/{len(img_map)} imgs]", file=sys.stderr)
        else:
            print(f"  ✓ ({lang}) {real_title}", file=sys.stderr)

        metadata = {
            "title": real_title,
            "display_name": display,
            "lang": lang,
            "wiki_title_input": wiki_title,
            "url": f"https://{lang}.wikipedia.org/wiki/{quote(real_title.replace(' ', '_'))}",
            "note": note,
            "section": section_key,
            "image_count": len(image_files),
            "download_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        (out_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    except Exception as e:
        print(f"  ✗ ({lang}) {real_title} [ERROR: {e}]", file=sys.stderr)
        return False


def generate_index():
    lines = [
        "<!DOCTYPE html><html><head><meta charset='utf-8'>",
        "<title>奖项 Wikipedia 离线索引</title>",
        "<style>body{font-family:sans-serif;max-width:800px;margin:2em auto;padding:0 1em;}",
        "h2{color:#333;border-bottom:1px solid #ddd;} a{color:#0645ad;}",
        "ul{line-height:1.8;}</style></head><body>",
        f"<h1>全球数学·计算·统计·跨学科奖项 Wikipedia 离线索引</h1>",
        f"<p>生成时间: {time.strftime('%Y-%m-%d %H:%M')} · 共 {sum(len(v) for _, v in AWARD_SECTIONS.items())} 个奖项</p>",
    ]
    for key in SECTION_ORDER:
        section_dir = PAGES_DIR / key
        if not section_dir.exists():
            continue
        cname, entries = AWARD_SECTIONS[key]
        lines.append(f"<h2>{cname}</h2><ul>")
        for display, lang, wiki_title, note in entries:
            real = resolve_title(wiki_title, lang)
            if not real:
                continue
            safe_name = re.sub(r'[<>:"/\\|?*]', '_', real)
            entry_dir = section_dir / safe_name
            idx = entry_dir / "index.html"
            if not idx.exists():
                continue
            meta_file = entry_dir / "metadata.json"
            meta = {}
            if meta_file.exists():
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
            url = meta.get("url", f"https://{lang}.wikipedia.org/wiki/{quote(real.replace(' ', '_'))}")
            lines.append(
                f'<li><a href="{key}/{safe_name}/index.html">{display}</a>'
                f' (<a href="{url}" target="_blank">online</a>)'
                f' {f"— {note}" if note else ""}</li>')
        lines.append("</ul>")
    lines.append("</body></html>")
    (PAGES_DIR / "INDEX.html").write_text("\n".join(lines), encoding="utf-8")
    print(f"  索引已生成: {PAGES_DIR / 'INDEX.html'}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="下载奖项 Wikipedia 页面（离线可浏览）")
    parser.add_argument("--section", type=str, help="只下载指定分类")
    parser.add_argument("--list", action="store_true", help="列出所有分类名")
    parser.add_argument("--rate", type=float, default=1.2, help="请求间隔秒数")
    parser.add_argument("--no-images", action="store_true", help="不下载图片")
    args = parser.parse_args()

    global RATE_LIMIT, DOWNLOAD_IMAGES
    RATE_LIMIT = args.rate
    DOWNLOAD_IMAGES = not args.no_images

    if args.list:
        for key in SECTION_ORDER:
            cname, entries = AWARD_SECTIONS[key]
            print(f"  {key:12s} ({len(entries):2d} entries)  {cname}")
        return

    sections_to_run = [args.section] if args.section else SECTION_ORDER
    PAGES_DIR.mkdir(exist_ok=True)
    total_ok = total_fail = 0
    for key in sections_to_run:
        if key not in AWARD_SECTIONS:
            print(f"[ERROR] 未知分类: {key}", file=sys.stderr)
            continue
        cname, entries = AWARD_SECTIONS[key]
        print(f"\n{'='*60}\n  [{key}] {cname} ({len(entries)} entries)\n  -> pages/{key}/\n{'='*60}", file=sys.stderr)
        for display, lang, wiki_title, note in entries:
            if download_entry(key, display, lang, wiki_title, note):
                total_ok += 1
            else:
                total_fail += 1
            time.sleep(RATE_LIMIT)

    print(f"\n{'='*60}\n  完成: {total_ok} 成功, {total_fail} 失败\n  保存位置: {PAGES_DIR.resolve()}\n{'='*60}", file=sys.stderr)
    generate_index()


if __name__ == "__main__":
    main()
