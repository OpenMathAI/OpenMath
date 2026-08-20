#!/usr/bin/env python3
"""Generate INDEX.html for 20th-century mathematician biography presentations.

Scans the current directory for one subdirectory per mathematician, extracts
the display name (Chinese/English) and birth-death years from each *_zh.md,
and lists the key artifacts (md / tex / pdf / mp4) as clickable links.
"""
import glob
import html
import os
import re
import urllib.parse
from pathlib import Path

BASE = Path(__file__).parent

CJK = re.compile(r'[\u4e00-\u9fff]')


def to_en(dirname: str) -> str:
    """Turn a directory name into a readable English name (strip award tags)."""
    name = re.sub(r'-(FWA|FW|FA|F|W|C|A|WA)$', '', dirname)
    return name.replace('_', ' ').strip()


def extract(dirname: str):
    md_files = sorted(glob.glob(str(BASE / dirname / '*_zh.md')))
    if not md_files:
        md_files = sorted(glob.glob(str(BASE / dirname / '*.md')))
    txt = ''
    md_rel = ''
    if md_files:
        md_rel = os.path.join(dirname, os.path.basename(md_files[0]))
        txt = (BASE / md_files[0]).read_text(encoding='utf-8', errors='ignore')

    lines = txt.split('\n')
    title = ''
    if lines:
        title = re.sub(r'^#\s*', '', lines[0].strip())
    # Strip the trailing "立传提示词" and any suffix after it.
    title = re.sub(r'立传提示词.*$', '', title).strip()
    title = re.sub(r'[—–-]\s*$', '', title).strip()

    name_zh = ''
    name_en = ''
    m_title = re.match(r'^\s*(.+?)\s*[\(（]\s*(.+?)\s*[\)）]\s*$', title)
    if m_title:
        a = m_title.group(1).strip()
        b = m_title.group(2).strip()
        if CJK.search(a):
            name_zh, name_en = a, b
        else:
            name_zh, name_en = b, a
    else:
        if CJK.search(title):
            name_zh = title
        else:
            name_en = title

    years = ''
    # "目标数学家" / "目标" line: e.g. "Alan Turing (1912–1954)"
    m_target = re.search(r'目标(?:数学家)?\s*\**\s*[：:]\s*([^\n]+)', txt)
    if m_target:
        t = m_target.group(1).strip()
        mm = re.match(r'^(.+?)\s*[\(（]\s*(\d{4})\s*[–\-—~]\s*(\d{4}|在世|今|\s*)\s*[\)）]', t)
        if mm:
            if not name_en:
                name_en = mm.group(1).strip()
            end = mm.group(3).strip()
            years = f"{mm.group(2)}–{end}" if end and end not in ('在世', '今') else f"{mm.group(2)}–"
        elif not name_en:
            name_en = t

    # "人物速览" table fallback.
    if not name_zh:
        m_zh = re.search(r'中文名\s*\|\s*([^|\n]+)', txt)
        if m_zh:
            name_zh = m_zh.group(1).strip()
    if not name_en:
        m_en = re.search(r'英文名\s*\|\s*([^|\n]+)', txt)
        if m_en:
            name_en = m_en.group(1).strip()
    if not years:
        m_dob = re.search(r'生卒\s*\|\s*([^|\n]+)', txt)
        if m_dob:
            yrs = re.findall(r'\d{4}', m_dob.group(1))
            if len(yrs) >= 2:
                years = f"{yrs[0]}–{yrs[1]}"
            elif len(yrs) == 1:
                years = f"{yrs[0]}–"

    if not name_en:
        name_en = to_en(dirname)
    if not name_zh:
        name_zh = name_en

    # Key artifacts in this directory.
    artifacts = {}
    dpath = BASE / dirname
    for f in sorted(os.listdir(dpath)):
        low = f.lower()
        if f.endswith('.md') and 'zh' in f:
            artifacts.setdefault('md', f)
        elif f.endswith('.tex') and 'zh' in f:
            artifacts.setdefault('tex', f)
        elif f.endswith('.pdf') and 'zh' in f:
            artifacts.setdefault('pdf', f)
        elif f.endswith('.mp4') and 'zh' in f:
            artifacts.setdefault('mp4', f)

    return {
        'dir': dirname,
        'title': title,
        'name_zh': name_zh,
        'name_en': name_en,
        'years': years,
        'artifacts': artifacts,
    }


def main():
    entries = []
    for d in sorted(os.listdir(BASE)):
        if not (BASE / d).is_dir() or d.startswith('.') or d in ('output', 'images'):
            continue
        entries.append(extract(d))

    # Sort by English name (case-insensitive).
    entries.sort(key=lambda e: (e['name_en'].lower(), e['dir']))

    now = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cards = []
    for e in entries:
        art = e['artifacts']
        links = []
        if 'md' in art:
            links.append(f'<a class="btn md" href="{urllib.parse.quote(os.path.join(e["dir"], art["md"]))}">MD</a>')
        if 'tex' in art:
            links.append(f'<a class="btn tex" href="{urllib.parse.quote(os.path.join(e["dir"], art["tex"]))}">TeX</a>')
        if 'pdf' in art:
            links.append(f'<a class="btn pdf" href="{urllib.parse.quote(os.path.join(e["dir"], art["pdf"]))}">PDF</a>')
        if 'mp4' in art:
            links.append(f'<a class="btn mp4" href="{urllib.parse.quote(os.path.join(e["dir"], art["mp4"]))}">MP4</a>')
        links_html = ' '.join(links) if links else '<span class="none">—</span>'

        zh = html.escape(e['name_zh'])
        en = html.escape(e['name_en'])
        years = html.escape(e['years']) if e['years'] else ''
        years_tag = f'<span class="years">{years}</span>' if years else ''
        dir_esc = html.escape(e['dir'])

        cards.append(f'''    <div class="card" data-search="{zh.lower()} {en.lower()} {dir_esc.lower()}">
      <div class="card-head">
        <span class="zh">{zh}</span>
        {years_tag}
      </div>
      <div class="en">{en}</div>
      <div class="dir">{dir_esc}</div>
      <div class="actions">{links_html}</div>
    </div>''')

    doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>20 世纪数学家立传 · 索引</title>
<style>
  :root {{
    --bg: #f6f7f9;
    --card: #ffffff;
    --ink: #1f2430;
    --muted: #6b7280;
    --line: #e5e7eb;
    --accent: #1d4ed8;
    --md: #0f766e;
    --tex: #7c3aed;
    --pdf: #b91c1c;
    --mp4: #b45309;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
      "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    background: var(--bg);
    color: var(--ink);
    line-height: 1.5;
  }}
  header {{
    background: linear-gradient(135deg, #1e3a8a 0%, #1d4ed8 55%, #3b82f6 100%);
    color: #fff;
    padding: 40px 24px 32px;
    text-align: center;
  }}
  header h1 {{ margin: 0 0 8px; font-size: 28px; letter-spacing: .5px; }}
  header p {{ margin: 0; opacity: .9; font-size: 15px; }}
  header .stat {{
    display: inline-block;
    margin-top: 14px;
    padding: 6px 16px;
    background: rgba(255,255,255,.18);
    border-radius: 999px;
    font-size: 14px;
  }}
  .toolbar {{
    max-width: 1200px;
    margin: -20px auto 0;
    padding: 0 24px;
    position: sticky;
    top: 0;
    z-index: 5;
  }}
  .toolbar input {{
    width: 100%;
    padding: 14px 18px;
    font-size: 16px;
    border: 1px solid var(--line);
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,.08);
    outline: none;
    background: var(--card);
  }}
  .toolbar input:focus {{ border-color: var(--accent); }}
  main {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 28px 24px 64px;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 16px;
  }}
  .card {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 16px 18px;
    transition: transform .12s ease, box-shadow .12s ease;
  }}
  .card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(30,58,138,.10);
  }}
  .card-head {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 8px;
  }}
  .zh {{ font-size: 17px; font-weight: 700; color: var(--ink); }}
  .years {{
    font-size: 12px;
    color: var(--muted);
    white-space: nowrap;
    font-variant-numeric: tabular-nums;
  }}
  .en {{ font-size: 13px; color: var(--muted); margin-top: 2px; }}
  .dir {{
    font-size: 11px;
    color: #9ca3af;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    margin-top: 6px;
    word-break: break-all;
  }}
  .actions {{ margin-top: 12px; display: flex; gap: 6px; flex-wrap: wrap; }}
  .btn {{
    font-size: 12px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 7px;
    text-decoration: none;
    color: #fff;
    background: #6b7280;
    transition: opacity .12s ease;
  }}
  .btn:hover {{ opacity: .8; }}
  .btn.md {{ background: var(--md); }}
  .btn.tex {{ background: var(--tex); }}
  .btn.pdf {{ background: var(--pdf); }}
  .btn.mp4 {{ background: var(--mp4); }}
  .none {{ font-size: 12px; color: #9ca3af; }}
  .empty {{ text-align: center; color: var(--muted); padding: 48px 0; display: none; }}
  footer {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px 40px;
    color: #9ca3af;
    font-size: 12px;
    text-align: center;
  }}
</style>
</head>
<body>
<header>
  <h1>20 世纪数学家立传 · 索引</h1>
  <p>OpenMathAI · Mathematician Biography Presentations</p>
  <span class="stat">共 {len(entries)} 位数学家</span>
</header>
<div class="toolbar">
  <input id="search" type="text" placeholder="搜索中英文姓名或目录名…" autocomplete="off">
</div>
<main>
  <div class="grid" id="grid">
{''.join(cards)}
  </div>
  <div class="empty" id="empty">没有匹配的结果</div>
</main>
<footer>Generated {now} · INDEX.html</footer>
<script>
  const input = document.getElementById('search');
  const cards = Array.from(document.querySelectorAll('.card'));
  const empty = document.getElementById('empty');
  input.addEventListener('input', () => {{
    const q = input.value.trim().toLowerCase();
    let visible = 0;
    cards.forEach(c => {{
      const hit = !q || c.dataset.search.includes(q);
      c.style.display = hit ? '' : 'none';
      if (hit) visible++;
    }});
    empty.style.display = visible ? 'none' : 'block';
  }});
</script>
</body>
</html>
'''

    out = BASE / 'INDEX.html'
    out.write_text(doc, encoding='utf-8')
    print(f'Generated {out} ({len(entries)} mathematicians)')


if __name__ == '__main__':
    main()
