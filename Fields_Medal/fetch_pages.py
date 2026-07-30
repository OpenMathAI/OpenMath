#!/usr/bin/env python3
"""
从 Wikipedia 按分类下载 CPU/GPU 芯片相关文章，每个分类一个目录。
保留 Wikipedia 原始页面布局（表格、infobox、图片、链接样式），可离线浏览。

每个条目下载：
  pages/<section_key>/<Title>/index.html     完整 HTML（含 Wikipedia CSS，可直接浏览器打开）
  pages/<section_key>/<Title>/images/        页面内图片（自动下载）
  pages/<section_key>/<Title>/metadata.json  基础元数据

用法:
  python3 fetch_pages.py                     # 下载全部分类
  python3 fetch_pages.py --section nvidia_gpu  # 只下载某个分类
  python3 fetch_pages.py --list              # 列出所有分类
  python3 fetch_pages.py --rate 2.0          # 设置请求间隔
  python3 fetch_pages.py --no-images         # 不下载图片（只存 HTML）

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

# 导入分类定义
from search_wiki import SECTIONS, SECTION_ORDER

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
USER_AGENT = (
    "TechMaterialsBot/1.0 "
    "(https://github.com/tech-materials; educational use) "
    "python-requests"
)

PAGES_DIR = Path(__file__).parent / "pages"
RATE_LIMIT = 1.0
DOWNLOAD_IMAGES = True

# ---------------------------------------------------------------------------
# HTTP 工具
# ---------------------------------------------------------------------------
_session = None


def get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update({
            "User-Agent": USER_AGENT,
        })
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
    """
    用 action=parse API 获取渲染后的 HTML 正文（含 infobox、表格、img 标签）。
    返回 (html_content, display_title, image_filenames)
    """
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
    
    html_content = parse.get("text", "")
    display_title = parse.get("displaytitle", title)
    image_files = parse.get("images", [])
    
    return html_content, display_title, image_files


def process_html(article_html: str, title: str, lang: str, out_dir: Path) -> tuple[str, list[str], dict]:
    """
    处理 action=parse 返回的文章 HTML：
    1. 补全图片 URL 为绝对路径
    2. 下载图片到本地并替换路径
    3. 补全内链
    4. 包裹完整 HTML 模板 + Wikipedia CSS
    返回 (full_html, image_urls, img_map)
    """
    soup = BeautifulSoup(article_html, "html.parser")

    # 去掉少量不需要的元素
    for sel in [".mw-editsection", ".noprint", ".mw-empty-elt",
                ".navbox", ".vertical-navbox", ".sistersitebox"]:
        for node in soup.select(sel):
            node.decompose()

    # 收集并处理图片
    images: list[str] = []
    img_map: dict[str, str] = {}

    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src:
            continue
        # action=parse 返回的图片通常是 //upload.wikimedia.org/...
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = f"https://{lang}.wikipedia.org" + src

        # 跳过极小图标
        width = img.get("width", "")
        try:
            if width and int(width) < 15:
                continue
        except (ValueError, TypeError):
            pass

        images.append(src)

        if DOWNLOAD_IMAGES:
            local_path = f"images/{safe_image_filename(src)}"
            img_map[src] = local_path
            img["src"] = local_path
        else:
            img["src"] = src

        # 处理 srcset
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
                    images.append(url)
                    tokens[0] = lp2
                else:
                    tokens[0] = url
                new_parts.append(" ".join(tokens))
            img["srcset"] = ", ".join(new_parts)

    # 补全内链为绝对路径
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/wiki/"):
            a["href"] = f"https://{lang}.wikipedia.org" + href
        elif href.startswith("/w/"):
            a["href"] = f"https://{lang}.wikipedia.org" + href
        elif href.startswith("#"):
            pass  # 锚点保留
        elif href.startswith("/"):
            a["href"] = f"https://{lang}.wikipedia.org" + href

    article_body = str(soup)

    # 包裹完整 HTML 模板
    full_html = FULL_PAGE_TEMPLATE.format(
        title=title,
        lang=lang,
        article_body=article_body,
    )

    return full_html, images, img_map


# 完整页面模板 — 引用 Wikipedia 官方 CSS + 补充离线样式
FULL_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - Wikipedia</title>
<!-- Wikipedia 官方样式表 -->
<link rel="stylesheet" href="https://en.wikipedia.org/w/load.php?lang=en&modules=ext.cite.styles%7Cext.pygments%7Cmediawiki.skinning.content.externallinks%7Cskins.vector.styles&only=styles">
<link rel="stylesheet" href="https://en.wikipedia.org/w/load.php?lang=en&modules=site.styles&only=styles">
<style>
/* 离线补充样式 */
body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #202122;
    background: #fff;
    max-width: 980px;
    margin: 0 auto;
    padding: 20px 30px;
}}
h1 {{ font-size: 1.8em; border-bottom: 1px solid #a2a9b1; padding-bottom: 0.15em; margin-top: 0; }}
h2 {{ font-size: 1.5em; border-bottom: 1px solid #a2a9b1; padding-bottom: 0.15em; }}
h3 {{ font-size: 1.2em; }}
a {{ color: #0645ad; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a.external {{ color: #36b; }}

/* 表格 */
table {{ border-collapse: collapse; margin: 0.5em 0; }}
.infobox, .infobox-full-data {{
    border: 1px solid #a2a9b1;
    background: #f8f9fa;
    float: right;
    clear: right;
    margin: 0.5em 0 0.5em 1.4em;
    padding: 0.2em;
    max-width: 22em;
    font-size: 88%;
    line-height: 1.5;
}}
.infobox th, .infobox td {{ padding: 0.2em 0.4em; vertical-align: top; }}
.infobox th {{ text-align: left; }}
.infobox-above, .infobox-title {{
    font-size: 125%;
    font-weight: bold;
    text-align: center;
    padding: 0.3em;
    background: #ccccff;
}}
.infobox-header {{ background: #ddd; text-align: center; font-weight: bold; }}
.infobox-image {{ text-align: center; padding: 0.4em; }}
.infobox-label {{ font-weight: bold; }}

.wikitable {{
    background: #f8f9fa;
    border: 1px solid #a2a9b1;
    margin: 1em 0;
    color: #202122;
}}
.wikitable th {{
    background: #eaecf0;
    text-align: center;
    border: 1px solid #a2a9b1;
    padding: 0.2em 0.4em;
}}
.wikitable td {{
    border: 1px solid #a2a9b1;
    padding: 0.2em 0.4em;
}}

/* 图片/缩略图 */
figure, .thumb {{
    margin: 0.5em 0 0.8em 1.4em;
    float: right;
    clear: right;
    max-width: 300px;
    border: 1px solid #c8ccd1;
    background: #f8f9fa;
    padding: 3px;
}}
figure img, .thumb img {{
    display: block;
    max-width: 100%;
    height: auto;
}}
figcaption, .thumbcaption {{
    font-size: 0.88em;
    line-height: 1.4;
    padding: 3px;
    color: #555;
}}
img {{ max-width: 100%; height: auto; }}

/* 提示框 */
.ambox {{
    border: 1px solid #a2a9b1;
    background: #fbfbfb;
    margin: 0.5em 0;
    padding: 0.25em 0.5em;
    font-size: 88%;
}}

/* 引用 */
.reflist {{ font-size: 90%; }}
sup.reference {{ font-size: 0.75em; }}

/* 代码 */
code, pre {{ background: #f5f5f5; padding: 2px 4px; border-radius: 2px; font-size: 0.9em; }}

/* 隐藏部分 UI */
.mw-editsection {{ display: none; }}

/* 清除浮动 */
.mw-parser-output::after {{ content: ""; display: table; clear: both; }}

/* Gallery 画廊 — 横排排列 */
ul.gallery {{
    list-style: none;
    margin: 1em 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}}
ul.gallery li.gallerybox {{
    display: inline-block;
    vertical-align: top;
    text-align: center;
}}
ul.gallery li.gallerybox .thumb {{
    float: none;
    margin: 0;
    border: 1px solid #c8ccd1;
    background: #f8f9fa;
    padding: 3px;
}}
ul.gallery li.gallerybox .gallerytext {{
    font-size: 0.85em;
    padding: 4px;
    max-width: 180px;
}}
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


def download_image(url: str, save_path: Path) -> bool:
    """下载单张图片。"""
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


def safe_image_filename(url: str) -> str:
    """从 URL 生成安全的本地文件名：decode URL 编码 + 去除特殊字符 + 限制长度。"""
    parsed = urlparse(url)
    filename = Path(parsed.path).name
    # URL decode
    filename = unquote(filename)
    # 替换特殊字符
    filename = re.sub(r'[<>:"/\\|?*@#()&,\[\]{}]', '_', filename)
    # 合并连续下划线
    filename = re.sub(r'_+', '_', filename)
    # 限制长度
    if len(filename) > 100:
        ext = Path(filename).suffix
        filename = filename[:95] + ext
    return filename


# ---------------------------------------------------------------------------
# 检查页面是否存在
# ---------------------------------------------------------------------------
def resolve_title(title: str, lang: str = "en") -> str | None:
    """检查页面是否存在，返回真实标题或 None。"""
    base = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "format": "json",
        "formatversion": "2",
        "redirects": "1",
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


# ---------------------------------------------------------------------------
# 下载单个条目
# ---------------------------------------------------------------------------
def download_entry(section_key: str, display: str, lang: str, wiki_title: str, note: str) -> bool:
    """下载一个条目，保存到 pages/<section_key>/<safe_name>/"""
    real_title = resolve_title(wiki_title, lang)
    if not real_title:
        print(f"  ✗ ({lang}) {wiki_title} [NOT FOUND]", file=sys.stderr)
        return False

    # 创建目录
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', real_title)
    out_dir = PAGES_DIR / section_key / f"{safe_name}_{lang}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 跳过已下载的
    html_file = out_dir / "index.html"
    if html_file.exists() and html_file.stat().st_size > 1000:
        print(f"  ● ({lang}) {real_title} [已存在, 跳过]", file=sys.stderr)
        return True

    try:
        # 用 action=parse API 获取渲染后的 HTML（含 img 标签）
        article_html, display_title, image_files = fetch_full_page(real_title, lang)
        
        # 处理 HTML（补全图片、包裹模板）
        processed_html, images, img_map = process_html(article_html, real_title, lang, out_dir)

        # 保存 HTML
        html_file.write_text(processed_html, encoding="utf-8")

        # 下载图片
        if DOWNLOAD_IMAGES and img_map:
            img_dir = out_dir / "images"
            img_dir.mkdir(exist_ok=True)
            downloaded = 0
            for url, local_path in img_map.items():
                save_path = out_dir / local_path
                if download_image(url, save_path):
                    downloaded += 1
            print(f"  ✓ ({lang}) {real_title} [{downloaded}/{len(img_map)} imgs]", file=sys.stderr)
        else:
            print(f"  ✓ ({lang}) {real_title}", file=sys.stderr)

        # 保存元数据
        metadata = {
            "title": real_title,
            "display_name": display,
            "lang": lang,
            "wiki_title_input": wiki_title,
            "url": f"https://{lang}.wikipedia.org/wiki/{quote(real_title.replace(' ', '_'))}",
            "note": note,
            "section": section_key,
            "image_count": len(images),
            "download_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        (out_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        return True

    except Exception as e:
        print(f"  ✗ ({lang}) {real_title} [ERROR: {e}]", file=sys.stderr)
        return False


# ---------------------------------------------------------------------------
# 主逻辑
# ---------------------------------------------------------------------------
def run_section(key: str) -> tuple[int, int]:
    """下载一个分类下的所有条目。返回 (成功数, 失败数)。"""
    title, entries = SECTIONS[key]
    ok = 0
    fail = 0
    for display, lang, wiki_title, note in entries:
        success = download_entry(key, display, lang, wiki_title, note)
        if success:
            ok += 1
        else:
            fail += 1
        time.sleep(RATE_LIMIT)
    return ok, fail


def main():
    parser = argparse.ArgumentParser(description="下载 Wikipedia CPU/GPU 文章（保留原始格式）")
    parser.add_argument("--section", type=str, help="只下载指定分类 (如 nvidia_gpu)")
    parser.add_argument("--list", action="store_true", help="列出所有分类名")
    parser.add_argument("--rate", type=float, default=1.0, help="请求间隔秒数 (默认 1.0)")
    parser.add_argument("--no-images", action="store_true", help="不下载图片")
    args = parser.parse_args()

    global RATE_LIMIT, DOWNLOAD_IMAGES
    RATE_LIMIT = args.rate
    DOWNLOAD_IMAGES = not args.no_images

    if args.list:
        for key in SECTION_ORDER:
            title, entries = SECTIONS[key]
            print(f"  {key:25s} ({len(entries):3d} entries)  {title}")
        return

    sections_to_run = [args.section] if args.section else SECTION_ORDER

    PAGES_DIR.mkdir(exist_ok=True)

    total_ok = 0
    total_fail = 0

    for key in sections_to_run:
        if key not in SECTIONS:
            print(f"[ERROR] 未知分类: {key}", file=sys.stderr)
            continue
        title, entries = SECTIONS[key]
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"  [{key}] {title} ({len(entries)} entries)", file=sys.stderr)
        print(f"  -> pages/{key}/", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)

        ok, fail = run_section(key)
        total_ok += ok
        total_fail += fail

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"  完成: {total_ok} 成功, {total_fail} 失败", file=sys.stderr)
    print(f"  保存位置: {PAGES_DIR.resolve()}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    # 生成索引
    generate_index()


def generate_index():
    """在 pages/ 下生成 INDEX.html 总索引（可浏览器打开）。"""
    lines = [
        "<!DOCTYPE html><html><head><meta charset='utf-8'>",
        "<title>CPU/GPU Wikipedia 离线索引</title>",
        "<style>body{font-family:sans-serif;max-width:800px;margin:2em auto;padding:0 1em;}",
        "h2{color:#333;border-bottom:1px solid #ddd;} a{color:#0645ad;}",
        "ul{line-height:1.8;}</style></head><body>",
        f"<h1>CPU/GPU Wikipedia 离线索引</h1>",
        f"<p>生成时间: {time.strftime('%Y-%m-%d %H:%M')}</p>",
    ]

    for key in SECTION_ORDER:
        section_dir = PAGES_DIR / key
        if not section_dir.exists():
            continue
        title, entries = SECTIONS[key]
        lines.append(f"<h2>{title}</h2><ul>")

        # 按原始定义顺序遍历，而非目录名排序
        seen = set()
        for display, lang, wiki_title, note in entries:
            # 查找对应的下载目录
            for entry_dir in section_dir.iterdir():
                if not entry_dir.is_dir():
                    continue
                meta_file = entry_dir / "metadata.json"
                if not meta_file.exists():
                    continue
                if entry_dir.name in seen:
                    continue
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
                if meta.get("wiki_title_input") == wiki_title and meta.get("lang") == lang:
                    seen.add(entry_dir.name)
                    name = meta.get("title", entry_dir.name)
                    url = meta.get("url", "")
                    mnote = meta.get("note", "")
                    local_link = f"{key}/{entry_dir.name}/index.html"
                    lines.append(
                        f'<li><a href="{local_link}">{name}</a>'
                        f' (<a href="{url}" target="_blank">online</a>)'
                        f' {f"— {mnote}" if mnote else ""}</li>'
                    )
                    break

        lines.append("</ul>")

    lines.append("</body></html>")
    (PAGES_DIR / "INDEX.html").write_text("\n".join(lines), encoding="utf-8")
    print(f"  索引已生成: {PAGES_DIR / 'INDEX.html'}", file=sys.stderr)


if __name__ == "__main__":
    main()
