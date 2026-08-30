#!/usr/bin/env python3
"""Generate INDEX.html for 19th-century mathematician Wikipedia data pages."""
import glob
import html
import json
import os
import urllib.parse
from pathlib import Path

BASE = Path(__file__).parent

# Accurate Chinese names (manual mapping).
ZH_NAMES = {
    'Marin_Mersenne': '马兰·梅森',
    'René_Descartes': '勒内·笛卡尔',
    'Bonaventura_Cavalieri': '博纳文图拉·卡瓦列里',
    'Pierre_de_Fermat': '皮埃尔·德·费马',
    'Evangelista_Torricelli': '埃万杰利斯塔·托里拆利',
    'John_Wallis': '约翰·沃利斯',
    'Blaise_Pascal': '布莱兹·帕斯卡',
    'Christiaan_Huygens': '克里斯蒂安·惠更斯',
    'Isaac_Barrow': '艾萨克·巴罗',
    'James_Gregory': '詹姆斯·格雷戈里',
    'Isaac_Newton': '艾萨克·牛顿',
    'Gottfried_Wilhelm_Leibniz': '戈特弗里德·威廉·莱布尼茨',
    'Jacob_Bernoulli': '雅各布·伯努利',
    'Johann_Bernoulli': '约翰·伯努利',
}


def load_entry(dirname):
    d = BASE / dirname
    meta = d / 'metadata.json'
    label = ''
    desc = ''
    birth = ''
    death = ''
    if meta.exists():
        try:
            m = json.loads(meta.read_text(encoding='utf-8'))
            label = m.get('label') or m.get('name') or dirname.replace('_', ' ')
            desc = m.get('description') or ''
            props = m.get('properties', {})
            dob = props.get('date_of_birth') or []
            dod = props.get('date_of_death') or []
            if dob:
                birth = str(dob[0])[:4]
            if dod:
                death = str(dod[0])[:4]
        except Exception:
            label = dirname.replace('_', ' ')
    if not label:
        label = dirname.replace('_', ' ')

    # Normalize negative years (BCE) for display.
    def fmt_year(y):
        y = str(y)
        if y.startswith('-'):
            return f'{y[1:]} BCE'
        return y

    years = ''
    if birth or death:
        b = fmt_year(birth)
        dy = fmt_year(death)
        years = f'{b}–{dy}' if death else f'{b}–'

    artifacts = {}
    for f in sorted(os.listdir(d)):
        if f == 'page.md':
            artifacts['md'] = f
        elif f == 'page.html':
            artifacts['html'] = f
        elif f == 'metadata.json':
            artifacts['json'] = f
        elif f == 'images.txt':
            artifacts['img'] = f

    return {
        'dir': dirname,
        'zh': ZH_NAMES.get(dirname, ''),
        'en': label,
        'years': years,
        'desc': desc,
        'artifacts': artifacts,
    }


def main():
    dirs = sorted(
        d for d in os.listdir(BASE)
        if (BASE / d).is_dir() and not d.startswith('.') and d not in ('output', 'images')
    )
    entries = [load_entry(d) for d in dirs]
    entries.sort(key=lambda e: e['en'].lower())

    cards = []
    for e in entries:
        art = e['artifacts']
        buttons = []
        for key, cls, label in [
            ('md', 'md', 'MD'),
            ('html', 'html', 'HTML'),
            ('json', 'json', 'JSON'),
            ('img', 'img', '图片'),
        ]:
            if key in art:
                href = os.path.join(e['dir'], art[key])
                buttons.append(f'<a class="btn {cls}" href="{href}">{label}</a>')
        actions = ' '.join(buttons) if buttons else '<span class="none">—</span>'

        zh = html.escape(e['zh'] or e['en'])
        en = html.escape(e['en'])
        years = html.escape(e['years'])
        years_tag = f'<span class="years">{years}</span>' if years else ''
        desc = html.escape(e['desc'])
        dir_esc = html.escape(e['dir'])

        cards.append(f'''    <div class="card" data-search="{zh.lower()} {en.lower()} {dir_esc.lower()}">
      <div class="card-head">
        <span class="zh">{zh}</span>
        {years_tag}
      </div>
      <div class="en">{en}</div>
      <div class="desc">{desc}</div>
      <div class="dir">{dir_esc}</div>
      <div class="actions">{actions}</div>
    </div>''')

    doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>17 世纪数学家 · 页面索引</title>
<style>
  :root {{
    --bg: #f6f7f9;
    --card: #ffffff;
    --ink: #1f2430;
    --muted: #6b7280;
    --line: #e5e7eb;
    --accent: #0f766e;
    --md: #0f766e;
    --html: #1d4ed8;
    --json: #7c3aed;
    --img: #b91c1c;
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
    background: linear-gradient(135deg, #064e3b 0%, #0f766e 55%, #14b8a6 100%);
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
    max-width: 1100px;
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
    max-width: 1100px;
    margin: 0 auto;
    padding: 28px 24px 64px;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
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
    box-shadow: 0 10px 28px rgba(6,78,59,.10);
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
  .desc {{ font-size: 12px; color: #9ca3af; margin-top: 4px; }}
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
  .btn.html {{ background: var(--html); }}
  .btn.json {{ background: var(--json); }}
  .btn.img {{ background: var(--img); }}
  .none {{ font-size: 12px; color: #9ca3af; }}
  .empty {{ text-align: center; color: var(--muted); padding: 48px 0; display: none; }}
  footer {{
    max-width: 1100px;
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
  <h1>17 世纪数学家 · 页面索引</h1>
  <p>OpenMathAI · 17th Century Mathematicians — Wikipedia 原始数据目录</p>
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
<footer>Generated by generate_index.py · INDEX.html</footer>
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
