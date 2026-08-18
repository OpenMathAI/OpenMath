#!/usr/bin/env python3
"""
为 pages/<世纪>/<Name>/latex/ 创建对应的 latex_zh/ 中文翻译目录骨架。

骨架内容：
  - 复制 images/（共享同一份图片）→ 用 symlink 节省磁盘
  - 复制 Makefile（修改 NAME 为 <Name>_zh）
  - 复制 body.tex 和 metadata.tex（待人工/翻译脚本逐步替换为中文）
  - 创建 <Name>_zh.tex：引用 ../../../../common/preamble_zh.tex

用法：
  python make_zh_skeleton.py             # 处理所有 pages/<世纪>/<Name>/latex 目录
  python make_zh_skeleton.py --only Gauss
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"

MAIN_ZH_TEMPLATE = r"""% Auto-generated 中文版主文件。Edit common/preamble_zh.tex for global style.
\input{../../../../common/preamble_zh.tex}
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

SUB_MAKEFILE = r"""# Auto-generated 中文版 per-person Makefile.
NAME := {name}
TEX  := $(NAME).tex
PDF  := $(NAME).pdf

.PHONY: all pdf build clean distclean

all: pdf

build: $(PDF)

pdf: $(PDF)
	@$(MAKE) --no-print-directory clean

$(PDF): $(TEX) body.tex metadata.tex ../../../../common/preamble_zh.tex
	latexmk -xelatex -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	@latexmk -c $(TEX) >/dev/null 2>&1 || true
	@rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz *.xdv

distclean: clean
	rm -f $(PDF)
"""


def make_skeleton(src_dir: Path) -> Path:
    person_dir = src_dir.parent
    name = person_dir.name
    zh_name = f"{name}_zh"
    zh_dir = person_dir / "latex_zh"
    zh_dir.mkdir(exist_ok=True)

    # 1) 主 tex
    (zh_dir / f"{zh_name}.tex").write_text(MAIN_ZH_TEMPLATE, encoding="utf-8")

    # 2) Makefile
    (zh_dir / "Makefile").write_text(SUB_MAKEFILE.format(name=zh_name), encoding="utf-8")

    # 3) body.tex / metadata.tex：先复制原文，后续手动翻译
    for f in ("body.tex", "metadata.tex"):
        src = src_dir / f
        dst = zh_dir / f
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)

    # 4) images：用 symlink 共享原图，节省磁盘
    img_src = src_dir / "images"
    img_link = zh_dir / "images"
    if img_src.exists() and not img_link.exists():
        img_link.symlink_to("../latex/images")

    return zh_dir


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", help="仅处理名字含此子串的目录")
    args = ap.parse_args()

    # 收集所有英文 latex 目录：pages/<世纪>/<Name>/latex
    src_dirs = sorted(
        d
        for century in PAGES.iterdir()
        if century.is_dir()
        for person in century.iterdir()
        if person.is_dir()
        for d in person.iterdir()
        if d.is_dir() and d.name == "latex"
    )
    if args.only:
        src_dirs = [d for d in src_dirs if args.only.lower() in d.parent.name.lower()]

    print(f"将创建 {len(src_dirs)} 个 latex_zh 骨架")
    created = []
    for d in src_dirs:
        zh = make_skeleton(d)
        print(f"  ✓ {zh.relative_to(PAGES)}")
        created.append(zh.name)

    print(f"\n完成 {len(created)} 个中文骨架")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
