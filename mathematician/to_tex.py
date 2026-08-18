#!/usr/bin/env python3
r"""
把 pages/<世纪>/<Name>/ 下的抓取数据转成一个可编译的 LaTeX 项目：
  pages/<世纪>/<Name>/
    latex/
      <Name>.tex        主文件（\documentclass + \input body）
      body.tex          由 page.html 经 pandoc 转换而来
      metadata.tex      由 metadata.json 生成的 \renewcommand
      images/           本地化的图片（下载）
      Makefile          子 Makefile
    latex_zh/           中文版（由 make_zh_skeleton.py 生成）

依赖：
    brew install pandoc
    brew install --cask mactex   # 提供 xelatex / latexmk

用法：
    python3 to_tex.py                    # 转换 pages/ 下所有人
    python3 to_tex.py --only Gauss       # 只转换名字里含 Gauss 的
    python3 to_tex.py --limit 3          # 前 3 个
    python3 to_tex.py --no-images        # 不下载图片（图片用远程 URL，编译时需联网）
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"
COMMON_DIR = ROOT / "common"

USER_AGENT = (
    "MathematicianTeX/1.0 "
    "(https://github.com/local/mathematician; ericksun@example.org) "
    "python-urllib/3"
)


# ---------------------------------------------------------------------------
# 工具
# ---------------------------------------------------------------------------
def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, text=True, **kw)


def latex_escape(s: str) -> str:
    """转义 LaTeX 特殊字符，用于元数据字段。"""
    if s is None:
        return ""
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    # 先处理反斜杠，避免二次转义
    out = s.replace("\\", "<<BS>>")
    for k, v in repl.items():
        if k == "\\":
            continue
        out = out.replace(k, v)
    out = out.replace("<<BS>>", r"\textbackslash{}")
    return out


def join_list(lst, sep=", ", limit: int | None = None) -> str:
    if not lst:
        return ""
    items = list(lst)
    if limit and len(items) > limit:
        items = items[:limit] + ["…"]
    return sep.join(latex_escape(x) for x in items)


# ---------------------------------------------------------------------------
# 1) metadata.tex
# ---------------------------------------------------------------------------
def write_metadata_tex(person_dir: Path, meta: dict, out: Path) -> None:
    props = meta.get("properties", {})
    name = meta.get("name") or meta.get("label") or person_dir.name.replace("_", " ")
    desc = meta.get("description", "") or ""
    birth = (props.get("date_of_birth") or [""])[0]
    death = (props.get("date_of_death") or [""])[0]
    pob = ", ".join(props.get("place_of_birth", []) or [])
    pod = ", ".join(props.get("place_of_death", []) or [])

    birth_full = f"{birth} {f'({pob})' if pob else ''}".strip()
    death_full = f"{death} {f'({pod})' if pod else ''}".strip()

    wiki = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"

    lines = [
        "% Auto-generated from metadata.json. DO NOT EDIT.",
        f"\\renewcommand{{\\MathematicianName}}{{{latex_escape(name)}}}",
        f"\\renewcommand{{\\MathematicianDescription}}{{{latex_escape(desc)}}}",
        f"\\renewcommand{{\\MathematicianBirth}}{{{latex_escape(birth_full) or '?'}}}",
        f"\\renewcommand{{\\MathematicianDeath}}{{{latex_escape(death_full) or '?'}}}",
        f"\\renewcommand{{\\MathematicianNationality}}{{{join_list(props.get('nationality'))}}}",
        f"\\renewcommand{{\\MathematicianFields}}{{{join_list(props.get('field_of_work'))}}}",
        f"\\renewcommand{{\\MathematicianAwards}}{{{join_list(props.get('award_received'), limit=10)}}}",
        f"\\renewcommand{{\\MathematicianWikipedia}}{{{wiki}}}",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# 2) HTML → LaTeX body（pandoc）
# ---------------------------------------------------------------------------
# 传给 pandoc 的过滤：去掉一些会引起 LaTeX 报错的脚注/引用/标签
_STRIP_SELECTORS_FOR_TEX = [
    "sup.reference",      # [1][2] 上标
    ".mw-editsection",
    ".noprint",
    ".navbox", ".vertical-navbox",
    ".sidebar",           # Wikipedia 主题侧栏（如 "Geometry"），转 LaTeX 后是嵌套
                          # longtable+minipage，会触发 \LT@nofcols 错误
    ".hatnote", ".shortdescription",
    ".mw-jump-link",
    ".reflist",
    "#References", "#Notes", "#Citations",
    "#External_links", "#Further_reading",
    "div[role='note']",
    "style", "script",
    "audio", "video",
    "table.sidebar",      # 双保险：有的 sidebar 是 <table>
    "table.vertical-navbox",
]


def prepare_html_for_pandoc(raw_html: str) -> str:
    """在 HTML→LaTeX 之前再做一轮针对性清洗。"""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(raw_html, "html.parser")

    for sel in _STRIP_SELECTORS_FOR_TEX:
        for node in soup.select(sel):
            node.decompose()

    # 去掉 'References' 章节之后的全部内容（常见尾部噪声）
    for h in soup.find_all(["h2", "h3"]):
        txt = h.get_text(strip=True).lower()
        if txt in {"references", "notes", "citations",
                   "external links", "further reading", "bibliography",
                   "see also"}:
            sib = h
            while sib is not None:
                nxt = sib.find_next_sibling()
                sib.decompose()
                sib = nxt
            break

    # 把 URL 过长（>120）或带复杂查询参数的 <a> 退化为纯文本：
    # 避免 pandoc 生成包含超长 URL 的 \href{}{}（在 xelatex 下会触发
    # "Paragraph ended before \href@split was complete"）。
    # 注意：这里使用 replace_with(NavigableString) 而非 unwrap()，
    # 后者在 a 标签里嵌套子标签时会破坏文档结构。
    from bs4 import NavigableString
    for a in list(soup.find_all("a", href=True)):
        href = a["href"]
        if len(href) > 120 or href.count("%") > 3:
            # 取其纯文本内容代替整个 <a>...</a>
            txt = a.get_text(" ", strip=True)
            a.replace_with(NavigableString(txt or ""))

    # 图片：去掉 srcset / 复杂属性，保留 src（pandoc 只认 src）
    for img in soup.find_all("img"):
        for attr in list(img.attrs):
            if attr not in ("src", "alt", "width", "height"):
                del img[attr]
        # 空 alt 兜底，避免 pandoc 把 alt 文本吞掉
        img["alt"] = img.get("alt") or ""

    # 移除 math 元素里的 <annotation-xml> / <semantics> 里的 presentation
    # （pandoc 通常能处理 MathML，但保守起见移除冗余）
    for ann in soup.select("annotation-xml, annotation"):
        ann.decompose()

    return str(soup)


def html_to_tex(html_path: Path, out: Path) -> None:
    """用 pandoc 把 HTML 转成 LaTeX 片段（不带 documentclass）。"""
    raw = html_path.read_text(encoding="utf-8")
    prepared = prepare_html_for_pandoc(raw)

    # 写到临时文件再喂给 pandoc
    tmp = out.with_suffix(".pandoc.html")
    tmp.write_text(prepared, encoding="utf-8")

    cmd = [
        "pandoc",
        str(tmp),
        "--from=html",
        "--to=latex",
        "--wrap=preserve",
        "--lua-filter", str(COMMON_DIR / "pandoc-filter.lua"),
        "-o", str(out),
    ]
    try:
        run(cmd)
    finally:
        tmp.unlink(missing_ok=True)

    # 后处理：清理 pandoc 生成的、在 XeLaTeX 下常会引起编译失败的节点
    postprocess_tex(out)


_TEX_CLEANUP_SUBS = [
    # 1) \phantomsection\label{...}  —— 在 caption 等 fragile 环境里会触发 iffalse
    (re.compile(r"\\phantomsection\\label\{[^}]*\}"), ""),
    # 2) 裸 \phantomsection
    (re.compile(r"\\phantomsection\b"), ""),
    # 3) \pandocbounded{...} —— 这个命令在 pandoc 3 里有 BUG 会吞 }
    #    直接把它替换为"就地输出内容"，避免任何隐患。
    (re.compile(r"\\pandocbounded\s*"), ""),
    # 4) 多余的空 \label{} 清理
    (re.compile(r"\\label\{\}"), ""),
]


def postprocess_tex(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for pat, repl in _TEX_CLEANUP_SUBS:
        text = pat.sub(repl, text)
    path.write_text(text, encoding="utf-8")


# pandoc 的 lua 过滤：去掉外链的 hyperref、把未知 raw html 丢弃等
PANDOC_LUA_FILTER = r"""
-- 去掉所有 RawBlock/RawInline(html) 节点，避免 LaTeX 报错
function RawBlock(el)
  if el.format == "html" then return {} end
  return nil
end
function RawInline(el)
  if el.format == "html" then return {} end
  return nil
end

-- 把没有 src 的 Image 去掉；把 http(s) 图片 src 保留，稍后 Python 会替换
function Image(img)
  if not img.src or img.src == "" then return {} end
  return img
end

-- 把空的段落去掉
function Para(p)
  if #p.content == 0 then return {} end
  return nil
end

-- 去掉脚注里的 href "Cite note" 等噪声
function Note(n)
  return {}
end
"""


# ---------------------------------------------------------------------------
# 3) 图片下载 & 重写 includegraphics 路径
# ---------------------------------------------------------------------------
_IMG_EXT_OK = {".png", ".jpg", ".jpeg", ".pdf"}  # gif/svg/webp 都不让 xelatex 直接吃


def download_images_in_tex(body_tex: Path, images_dir: Path,
                           skip: bool = False) -> None:
    r"""
    扫描 body.tex 里的 \includegraphics{URL}，
    如果是 http/https，则下载到 images_dir，并改写为相对文件名。
    不支持的格式（svg/webp）会被忽略，生成一个占位注释。
    """
    text = body_tex.read_text(encoding="utf-8")
    images_dir.mkdir(parents=True, exist_ok=True)

    pat = re.compile(
        r"\\includegraphics(\[[^\]]*\])?\{(?P<url>[^}]+)\}"
    )

    cache: dict[str, str] = {}

    def handle(url: str) -> str:
        if skip or not url.startswith(("http://", "https://")):
            return url
        # pandoc 会把 URL 里的 % # & _ $ 等转义成 \% \# \& \_ \$
        # 下载前必须先还原回原始字符。
        url = re.sub(r"\\([#$%&_{}])", r"\1", url)
        if url in cache:
            return cache[url]

        parsed = urlparse(url)
        fname = Path(parsed.path).name
        # 有些 URL 里带 %XX 编码
        from urllib.parse import unquote
        fname = unquote(fname)
        # 规范化文件名：只保留 ASCII 字母数字/连字符/下划线/点，
        # 其它字符（含 ü / ß / 中文 …）全部替换为 _ 以避免 xelatex
        # 在读取 \includegraphics 时触发 "Incomplete \iffalse" 之类的错误。
        fname = re.sub(r"[^A-Za-z0-9._-]+", "_", fname)
        fname = re.sub(r"_+", "_", fname).strip("_.") or "img"
        suffix = Path(fname).suffix.lower()

        if suffix not in _IMG_EXT_OK:
            # svg/webp/tif/ogv 等 xelatex 不直接支持，跳过
            cache[url] = f"__UNSUPPORTED__:{fname}"
            return cache[url]

        dst = images_dir / fname
        if not dst.exists():
            for attempt in range(3):
                try:
                    req = Request(url, headers={
                        "User-Agent": USER_AGENT,
                        "Accept": "image/*,*/*;q=0.8",
                    })
                    with urlopen(req, timeout=30) as r, open(dst, "wb") as f:
                        f.write(r.read())
                    break
                except Exception as e:
                    if attempt == 2:
                        print(f"    ! 图片下载失败 {url}: {e}")
                        cache[url] = f"__UNSUPPORTED__:{fname}"
                        return cache[url]
                    # 429 / 网络抖动：退避后重试
                    time.sleep(2 ** attempt)
            # 下载后礼貌性限速，避免 Wikimedia 429
            time.sleep(0.2)

        cache[url] = fname
        return fname

    def repl(m: re.Match) -> str:
        opt = m.group(1) or ""
        url = m.group("url").strip()
        new = handle(url)
        if new.startswith("__UNSUPPORTED__:"):
            # 直接把整条 \includegraphics 删掉（用空字符串），
            # 不要用 % 注释，否则在 table/minipage/math 内会破坏花括号匹配。
            return ""
        return f"\\includegraphics{opt}{{{new}}}"

    new_text = pat.sub(repl, text)
    body_tex.write_text(new_text, encoding="utf-8")


# ---------------------------------------------------------------------------
# 4) 主 Tex 文件与 Makefile
# ---------------------------------------------------------------------------
MAIN_TEMPLATE = r"""% Auto-generated. Edit common/preamble.tex for global style.
\input{../../../../common/preamble.tex}
\input{metadata.tex}

\title{\MathematicianName}
\author{}
\date{\MathematicianBirth\ \textendash\ \MathematicianDeath}

\begin{document}

\maketitle

\begin{abstract}
\noindent \MathematicianDescription
\end{abstract}

\InfoBox

\vspace{1em}
\hrule
\vspace{1em}

\input{body.tex}

\end{document}
"""


SUB_MAKEFILE = r"""# Auto-generated per-person Makefile.
NAME := {name}
TEX  := $(NAME).tex
PDF  := $(NAME).pdf

.PHONY: all pdf build clean distclean

# 默认目标：编译 + 清理中间产物，只保留 PDF
all: pdf

# 仅编译，不清理（保留 .aux/.log 等，方便调试）
build: $(PDF)

# 编译完成后调用 clean 清掉中间产物
pdf: $(PDF)
	@$(MAKE) --no-print-directory clean

$(PDF): $(TEX) body.tex metadata.tex ../../../../common/preamble.tex
	latexmk -xelatex -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	@latexmk -c $(TEX) >/dev/null 2>&1 || true
	@rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz *.xdv

distclean: clean
	rm -f $(PDF)
"""



# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def convert_one(person_dir: Path, download_imgs: bool) -> str | None:
    name = person_dir.name
    meta_path = person_dir / "metadata.json"
    html_path = person_dir / "page.html"
    if not html_path.exists():
        print(f"  ✗ skip {name} (no page.html)")
        return None

    meta = json.loads(meta_path.read_text("utf-8")) if meta_path.exists() else {}

    sub = person_dir / "latex"
    sub.mkdir(parents=True, exist_ok=True)
    (sub / "images").mkdir(exist_ok=True)

    # metadata.tex
    write_metadata_tex(person_dir, meta, sub / "metadata.tex")

    # body.tex via pandoc
    body_tex = sub / "body.tex"
    html_to_tex(html_path, body_tex)

    # 本地化图片
    download_images_in_tex(body_tex, sub / "images", skip=not download_imgs)

    # 主 .tex
    (sub / f"{name}.tex").write_text(MAIN_TEMPLATE, encoding="utf-8")

    # 子 Makefile
    (sub / "Makefile").write_text(SUB_MAKEFILE.format(name=name), encoding="utf-8")

    return name

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", type=Path, default=PAGES_DIR)
    ap.add_argument("--only", help="仅处理名字里含此子串的目录")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--no-images", action="store_true", help="不下载图片")
    ap.add_argument("--jobs", type=int, default=4, help="并行下载/转换 worker 数")
    args = ap.parse_args()

    if not args.pages.exists():
        print(f"✗ pages 目录不存在：{args.pages}")
        return 1

    # 写 common 资源（pandoc lua 过滤器）
    COMMON_DIR.mkdir(parents=True, exist_ok=True)
    (COMMON_DIR / "pandoc-filter.lua").write_text(PANDOC_LUA_FILTER, encoding="utf-8")

    # pages/ 下是世纪目录（18th_century 等），递归到具体人名目录
    dirs = sorted(
        p
        for century in args.pages.iterdir()
        if century.is_dir()
        for p in century.iterdir()
        if p.is_dir()
    )
    if args.only:
        dirs = [d for d in dirs if args.only.lower() in d.name.lower()]
    if args.limit:
        dirs = dirs[: args.limit]

    print(f"将转换 {len(dirs)} 位 → 各人名目录下的 latex/")

    done: list[str] = []
    for i, d in enumerate(dirs, 1):
        print(f"\n[{i}/{len(dirs)}] {d.name}")
        try:
            name = convert_one(d, download_imgs=not args.no_images)
            if name:
                done.append(name)
        except subprocess.CalledProcessError as e:
            print(f"  ✗ pandoc 失败：{e}")
        except Exception as e:
            print(f"  ✗ {e}")

    print(f"\n✅ 转换完成 {len(done)} 位。可进入 pages/<世纪>/<Name>/latex/ 运行 make。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
