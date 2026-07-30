#!/usr/bin/env python3
"""
Download all Fields Medal winners' Wikipedia pages (with images) for offline browsing.

Output: Fields_Medal/pages/<Year>/<Winner Name>/index.html  (+ images/)

Usage:
  python3 fetch_fields_medal.py            # download all 68 winners
  python3 fetch_fields_medal.py --rate 2.0  # set request interval
  python3 fetch_fields_medal.py --no-images # HTML only, no images

Dependencies:
  pip install requests beautifulsoup4
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, urlparse, unquote

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Fields Medal winners (1936-2026, 68 winners)
# ---------------------------------------------------------------------------
WINNERS = [
    # (Year, Wikipedia title, display name for note)
    (1936, "Lars Ahlfors", ""),
    (1936, "Jesse Douglas", ""),
    (1950, "Laurent Schwartz", ""),
    (1950, "Atle Selberg", ""),
    (1954, "Kunihiko Kodaira", ""),
    (1954, "Jean-Pierre Serre", ""),
    (1958, "Klaus Roth", ""),
    (1958, "René Thom", ""),
    (1962, "Lars Hörmander", ""),
    (1962, "John Milnor", ""),
    (1966, "Michael Atiyah", ""),
    (1966, "Paul Cohen", ""),
    (1966, "Alexander Grothendieck", ""),
    (1966, "Stephen Smale", ""),
    (1970, "Alan Baker (mathematician)", ""),
    (1970, "Heisuke Hironaka", ""),
    (1970, "Sergei Novikov (mathematician)", ""),
    (1970, "John G. Thompson", ""),
    (1974, "Enrico Bombieri", ""),
    (1974, "David Mumford", ""),
    (1978, "Pierre Deligne", ""),
    (1978, "Charles Fefferman", ""),
    (1978, "Grigory Margulis", ""),
    (1978, "Daniel Quillen", ""),
    (1982, "Alain Connes", ""),
    (1982, "William Thurston", ""),
    (1982, "Shing-Tung Yau", ""),
    (1986, "Simon Donaldson", ""),
    (1986, "Gerd Faltings", ""),
    (1986, "Michael Freedman", ""),
    (1990, "Vladimir Drinfeld", ""),
    (1990, "Vaughan Jones", ""),
    (1990, "Shigefumi Mori", ""),
    (1990, "Edward Witten", ""),
    (1994, "Jean Bourgain", ""),
    (1994, "Pierre-Louis Lions", ""),
    (1994, "Jean-Christophe Yoccoz", ""),
    (1994, "Efim Zelmanov", ""),
    (1998, "Richard Borcherds", ""),
    (1998, "Timothy Gowers", ""),
    (1998, "Maxim Kontsevich", ""),
    (1998, "Curtis T. McMullen", ""),
    (2002, "Laurent Lafforgue", ""),
    (2002, "Vladimir Voevodsky", ""),
    (2006, "Andrei Okounkov", ""),
    (2006, "Grigori Perelman", ""),
    (2006, "Terence Tao", ""),
    (2006, "Wendelin Werner", ""),
    (2010, "Elon Lindenstrauss", ""),
    (2010, "Ngô Bảo Châu", ""),
    (2010, "Stanislav Smirnov", ""),
    (2010, "Cédric Villani", ""),
    (2014, "Artur Avila", ""),
    (2014, "Manjul Bhargava", ""),
    (2014, "Martin Hairer", ""),
    (2014, "Maryam Mirzakhani", ""),
    (2018, "Caucher Birkar", ""),
    (2018, "Alessio Figalli", ""),
    (2018, "Peter Scholze", ""),
    (2018, "Akshay Venkatesh", ""),
    (2022, "Hugo Duminil-Copin", ""),
    (2022, "June Huh", ""),
    (2022, "James Maynard (mathematician)", ""),
    (2022, "Maryna Viazovska", ""),
    (2026, "Yu Deng", ""),
    (2026, "John Pardon", ""),
    (2026, "Jacob Tsimerman", ""),
    (2026, "Hong Wang (mathematician)", ""),
]

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
USER_AGENT = (
    "FieldsMedalArchive/1.0 "
    "(https://github.com/tech-materials; educational use) "
    "python-requests"
)

OUT_DIR = Path(__file__).parent / "Fields_Medal" / "pages"
RATE_LIMIT = 1.0
DOWNLOAD_IMAGES = True
LANG = "en"

# ---------------------------------------------------------------------------
# HTTP utils
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
            print(f"    ! {e}, retry in {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError("unreachable")

# ---------------------------------------------------------------------------
# Fetch rendered page via Wikipedia API
# ---------------------------------------------------------------------------
def fetch_full_page(title: str) -> tuple[str, str, list[str]]:
    """
    Use action=parse to get rendered HTML (infobox, tables, images).
    Returns (html_body, display_title, image_filenames).
    """
    base = f"https://{LANG}.wikipedia.org/w/api.php"
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
    html = parse.get("text", "")
    display_title = parse.get("displaytitle", title)
    images = parse.get("images", [])
    return html, display_title, images


def process_html(article_html: str, title: str, out_dir: Path) -> tuple[str, list[str], dict]:
    """
    Process article HTML:
    1. Resolve image URLs to absolute
    2. Download images locally, rewrite paths
    3. Fix internal links
    4. Wrap in full HTML template with Wikipedia CSS
    Returns (full_html, image_urls, img_map).
    """
    soup = BeautifulSoup(article_html, "html.parser")

    # Remove clutter
    for sel in [".mw-editsection", ".noprint", ".mw-empty-elt",
                ".navbox", ".vertical-navbox", ".sistersitebox"]:
        for node in soup.select(sel):
            node.decompose()

    images: list[str] = []
    img_map: dict[str, str] = {}

    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src:
            continue
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = f"https://{LANG}.wikipedia.org" + src

        # skip tiny icons
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

        # srcset
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
                    url = f"https://{LANG}.wikipedia.org" + url
                if DOWNLOAD_IMAGES:
                    lp = f"images/{safe_image_filename(url)}"
                    img_map[url] = lp
                    images.append(url)
                    tokens[0] = lp
                else:
                    tokens[0] = url
                new_parts.append(" ".join(tokens))
            img["srcset"] = ", ".join(new_parts)

    # Fix internal links to absolute
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/wiki/") or href.startswith("/w/"):
            a["href"] = f"https://{LANG}.wikipedia.org" + href
        elif href.startswith("#"):
            pass
        elif href.startswith("/"):
            a["href"] = f"https://{LANG}.wikipedia.org" + href

    article_body = str(soup)

    full_html = FULL_PAGE_TEMPLATE.format(
        title=title,
        lang=LANG,
        article_body=article_body,
    )
    return full_html, images, img_map


# ---------------------------------------------------------------------------
# HTML Template
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
table {{ border-collapse: collapse; margin: 0.5em 0; }}
.infobox, .infobox-full-data {{
    border: 1px solid #a2a9b1; background: #f8f9fa; float: right; clear: right;
    margin: 0.5em 0 0.5em 1.4em; padding: 0.2em; max-width: 22em; font-size: 88%; line-height: 1.5;
}}
.infobox th, .infobox td {{ padding: 0.2em 0.4em; vertical-align: top; }}
.infobox th {{ text-align: left; }}
.infobox-above, .infobox-title {{
    font-size: 125%; font-weight: bold; text-align: center; padding: 0.3em; background: #ccccff;
}}
.infobox-header {{ background: #ddd; text-align: center; font-weight: bold; }}
.infobox-image {{ text-align: center; padding: 0.4em; }}
.infobox-label {{ font-weight: bold; }}
.wikitable {{
    background: #f8f9fa; border: 1px solid #a2a9b1; margin: 1em 0; color: #202122;
}}
.wikitable th {{
    background: #eaecf0; text-align: center; border: 1px solid #a2a9b1; padding: 0.2em 0.4em;
}}
.wikitable td {{ border: 1px solid #a2a9b1; padding: 0.2em 0.4em; }}
figure, .thumb {{
    margin: 0.5em 0 0.8em 1.4em; float: right; clear: right; max-width: 300px;
    border: 1px solid #c8ccd1; background: #f8f9fa; padding: 3px;
}}
figure img, .thumb img {{ display: block; max-width: 100%; height: auto; }}
figcaption, .thumbcaption {{
    font-size: 0.88em; line-height: 1.4; padding: 3px; color: #555;
}}
img {{ max-width: 100%; height: auto; }}
.ambox {{
    border: 1px solid #a2a9b1; background: #fbfbfb; margin: 0.5em 0; padding: 0.25em 0.5em; font-size: 88%;
}}
.reflist {{ font-size: 90%; }}
sup.reference {{ font-size: 0.75em; }}
code, pre {{ background: #f5f5f5; padding: 2px 4px; border-radius: 2px; font-size: 0.9em; }}
.mw-editsection {{ display: none; }}
.mw-parser-output::after {{ content: ""; display: table; clear: both; }}
ul.gallery {{
    list-style: none; margin: 1em 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px;
}}
ul.gallery li.gallerybox {{ display: inline-block; vertical-align: top; text-align: center; }}
ul.gallery li.gallerybox .thumb {{ float: none; margin: 0; border: 1px solid #c8ccd1; background: #f8f9fa; padding: 3px; }}
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
<p>Source: <a href="https://{lang}.wikipedia.org/wiki/{title}">Wikipedia</a> · Fields Medal winner · Downloaded for offline reading</p>
</footer>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Image download
# ---------------------------------------------------------------------------
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

def safe_image_filename(url: str) -> str:
    parsed = urlparse(url)
    filename = Path(parsed.path).name
    filename = unquote(filename)
    filename = re.sub(r'[<>:"/\\|?*@#()&,\[\]{}]', '_', filename)
    filename = re.sub(r'_+', '_', filename)
    if len(filename) > 100:
        ext = Path(filename).suffix
        filename = filename[:95] + ext
    return filename


# ---------------------------------------------------------------------------
# Resolve title (check existence, follow redirects)
# ---------------------------------------------------------------------------
def resolve_title(title: str) -> str | None:
    base = f"https://{LANG}.wikipedia.org/w/api.php"
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
# Download single entry
# ---------------------------------------------------------------------------
def download_entry(year: int, wiki_title: str) -> bool:
    real_title = resolve_title(wiki_title)
    if not real_title:
        print(f"  ✗ ({year}) {wiki_title} [NOT FOUND]", file=sys.stderr)
        return False

    safe_name = re.sub(r'[<>:"/\\|?*]', '_', real_title)
    entry_dir = OUT_DIR / str(year) / safe_name
    entry_dir.mkdir(parents=True, exist_ok=True)

    html_file = entry_dir / "index.html"
    if html_file.exists() and html_file.stat().st_size > 1000:
        print(f"  ● ({year}) {real_title} [exists, skip]", file=sys.stderr)
        return True

    try:
        article_html, display_title, _image_files = fetch_full_page(real_title)
        processed_html, images, img_map = process_html(article_html, real_title, entry_dir)

        html_file.write_text(processed_html, encoding="utf-8")

        if DOWNLOAD_IMAGES and img_map:
            img_dir = entry_dir / "images"
            img_dir.mkdir(exist_ok=True)
            downloaded = 0
            for url, local_path in img_map.items():
                save_path = entry_dir / local_path
                if download_image(url, save_path):
                    downloaded += 1
            print(f"  ✓ ({year}) {real_title} [{downloaded}/{len(img_map)} imgs]", file=sys.stderr)
        else:
            print(f"  ✓ ({year}) {real_title}", file=sys.stderr)

        metadata = {
            "title": real_title,
            "wiki_title_input": wiki_title,
            "year": year,
            "url": f"https://{LANG}.wikipedia.org/wiki/{quote(real_title.replace(' ', '_'))}",
            "image_count": len(images),
            "download_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        (entry_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return True

    except Exception as e:
        print(f"  ✗ ({year}) {real_title} [ERROR: {e}]", file=sys.stderr)
        return False


# ---------------------------------------------------------------------------
# Generate index page
# ---------------------------------------------------------------------------
def generate_index():
    lines = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>",
        "<title>Fields Medal Winners · Wikipedia Offline</title>",
        "<style>",
        "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:900px;margin:2em auto;padding:0 1em;color:#202122;}",
        "h1{font-size:2em;border-bottom:3px solid #0050a0;padding-bottom:0.3em;}",
        "h2{color:#0050a0;border-bottom:1px solid #ccc;margin-top:1.5em;}",
        "ul{line-height:2;list-style:none;padding-left:1em;}",
        "li::before{content:'🏅 ';}",
        "a{color:#0645ad;text-decoration:none;} a:hover{text-decoration:underline;}",
        "footer{margin-top:3em;font-size:0.85em;color:#666;border-top:1px solid #ddd;padding-top:1em;}",
        "</style></head><body>",
        f"<h1>🏅 Fields Medal Winners ({1936}-{2026})</h1>",
        f"<p>Total: {len(WINNERS)} winners · Downloaded: {time.strftime('%Y-%m-%d %H:%M')}</p>",
    ]

    current_year = None
    for year, wiki_title, _note in WINNERS:
        if year != current_year:
            if current_year is not None:
                lines.append("</ul>")
            current_year = year
            lines.append(f"<h2>{year}</h2><ul>")

        safe_name = re.sub(r'[<>:"/\\|?*]', '_', wiki_title)
        entry_dir = OUT_DIR / str(year) / safe_name
        html_file = entry_dir / "index.html"
        if html_file.exists():
            lines.append(f'<li><a href="{year}/{safe_name}/index.html">{wiki_title}</a></li>')
        else:
            lines.append(f'<li>{wiki_title} <span style="color:#999">(not downloaded)</span></li>')

    if current_year is not None:
        lines.append("</ul>")

    lines.append(
        "<footer><p>Source: Wikipedia · Fields Medal winners · Offline archive</p></footer>"
    )
    lines.append("</body></html>")

    (OUT_DIR / "INDEX.html").write_text("\n".join(lines), encoding="utf-8")
    print(f"\n  Index: {OUT_DIR / 'INDEX.html'}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Download Fields Medal winners' Wikipedia pages")
    parser.add_argument("--rate", type=float, default=1.0, help="Request interval in seconds (default 1.0)")
    parser.add_argument("--no-images", action="store_true", help="Skip image download")
    parser.add_argument("--start", type=int, default=0, help="Start from this winner index (0-based)")
    args = parser.parse_args()

    global RATE_LIMIT, DOWNLOAD_IMAGES
    RATE_LIMIT = args.rate
    DOWNLOAD_IMAGES = not args.no_images

    OUT_DIR.mkdir(exist_ok=True)

    total = len(WINNERS)
    ok = 0
    fail = 0

    print(f"{'='*60}", file=sys.stderr)
    print(f"  Fields Medal Winners: {total} pages", file=sys.stderr)
    print(f"  Output: {OUT_DIR.resolve()}", file=sys.stderr)
    print(f"  Images: {'yes' if DOWNLOAD_IMAGES else 'no'}, Rate: {RATE_LIMIT}s", file=sys.stderr)
    print(f"  Start index: {args.start}", file=sys.stderr)
    print(f"{'='*60}\n", file=sys.stderr)

    for i, (year, wiki_title, _note) in enumerate(WINNERS):
        if i < args.start:
            continue
        print(f"[{i+1}/{total}] ({year}) {wiki_title}", file=sys.stderr)
        success = download_entry(year, wiki_title)
        if success:
            ok += 1
        else:
            fail += 1
        time.sleep(RATE_LIMIT)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"  Done: {ok} ok, {fail} failed (out of {total})", file=sys.stderr)
    print(f"  Output: {OUT_DIR.resolve()}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    generate_index()


if __name__ == "__main__":
    main()
