#!/usr/bin/env python3
"""
修复已抓取的 pages/*/page.html 与 page.md：
- 把 <img src="./..."> 等相对地址补全为 Wikipedia 绝对地址
- 补全 <a href> 与 srcset
- 在 <head> 插入 <base href="https://..."> 让本地 file:// 打开也能显示图片
- 重新用 markdownify 生成 page.md

用法：
    python3 fix_existing_pages.py            # 默认 ./pages
    python3 fix_existing_pages.py --root pages --lang en
"""
from __future__ import annotations

import argparse
from pathlib import Path

# 复用主脚本里的函数
from fetch_full_pages import clean_html, html_to_markdown, _build_frontmatter
import json


def fix_one(person_dir: Path, lang: str) -> None:
    html_path = person_dir / "page.html"
    md_path = person_dir / "page.md"
    meta_path = person_dir / "metadata.json"
    if not html_path.exists():
        print(f"  ✗ skip (no page.html): {person_dir.name}")
        return

    raw_html = html_path.read_text(encoding="utf-8")
    cleaned, images = clean_html(raw_html, lang)
    # 回写修复后的 html
    html_path.write_text(cleaned, encoding="utf-8")

    # 重新生成 markdown
    markdown = html_to_markdown(cleaned)
    meta = json.loads(meta_path.read_text("utf-8")) if meta_path.exists() else {}
    name = meta.get("name") or person_dir.name.replace("_", " ")
    front = _build_frontmatter(name, lang, meta)
    md_path.write_text(front + "\n\n" + markdown, encoding="utf-8")

    # 更新图片清单
    (person_dir / "images.txt").write_text("\n".join(images), encoding="utf-8")
    print(f"  ✓ {person_dir.name}  ({len(images)} images)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path("pages"))
    ap.add_argument("--lang", default="en")
    args = ap.parse_args()

    dirs = sorted(p for p in args.root.iterdir() if p.is_dir())
    print(f"共 {len(dirs)} 个子目录")
    for d in dirs:
        fix_one(d, args.lang)
    print("完成")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
