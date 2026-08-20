#!/usr/bin/env python3
"""扫描 pages 下所有世纪目录，重建 INDEX.md（顶层总索引 + 各世纪分索引）。"""
import json, time, re
from pathlib import Path

PAGES = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages')

CENTURY_TITLES = {
    '18th_century': '18 世纪',
    '19th_century': '19 世纪',
    '20th_century': '20 世纪',
    'ancient_chinese': '中国古代',
}

def sanitize(s):
    return re.sub(r'[<>|:]*', '', str(s))

def extract_entry(d):
    """从数学家目录提取 (name, birth, death, desc)。"""
    md = d / 'page.md'
    meta = d / 'metadata.json'
    name = d.name
    birth = death = desc = ''
    if meta.exists():
        try:
            m = json.loads(meta.read_text(encoding='utf-8'))
            name = m.get('label') or name
            desc = m.get('description') or ''
            props = m.get('properties', {})
            dob = props.get('date_of_birth') or []
            dod = props.get('date_of_death') or []
            if dob:
                birth = str(dob[0])[:4]
            if dod:
                death = str(dod[0])[:4]
        except Exception:
            pass
    if md.exists():
        text = md.read_text(encoding='utf-8', errors='ignore')
        fm = re.match(r'^---\n(.*?)\n---', text, re.S)
        if fm:
            body = fm.group(1)
            for key in ('name', 'description', 'date_of_birth', 'date_of_death'):
                mm = re.search(rf'^{key}: (.*)$', body, re.M)
                if mm:
                    raw = mm.group(1)
                    try:
                        v = json.loads(raw)
                    except Exception:
                        v = raw
                    if isinstance(v, list):
                        v = v[0] if v else ''
                    if key == 'name':
                        name = v
                    elif key == 'description':
                        desc = v
                    elif key == 'date_of_birth':
                        birth = str(v)[:4]
                    elif key == 'date_of_death':
                        death = str(v)[:4]
    return name, birth, death, desc

def century_order_key(c):
    for i, k in enumerate(CENTURY_TITLES):
        if k == c:
            return i
    return len(CENTURY_TITLES)

# 收集每个世纪下的人：century -> [(name, dirname, years, desc)]
century_entries = {}
for century_dir in sorted(PAGES.iterdir()):
    if not century_dir.is_dir():
        continue
    century = century_dir.name
    items = []
    for d in sorted(century_dir.iterdir()):
        if not d.is_dir():
            continue
        if not (d / 'page.md').exists():
            continue
        name, birth, death, desc = extract_entry(d)
        years = f"（{birth}–{death}）" if birth or death else ''
        items.append((name, d.name, years, desc))
    if items:
        century_entries[century] = items

total = sum(len(v) for v in century_entries.values())
ordered = sorted(century_entries, key=century_order_key)

# 顶层总索引
lines = [
    "# 数学家完整页面索引\n",
    f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
    f"> 共 **{total}** 人\n",
]
for century in ordered:
    title = CENTURY_TITLES.get(century, century)
    items = century_entries[century]
    lines.append(f"\n## {title}（{len(items)} 人）\n")
    for name, dname, years, desc in sorted(items, key=lambda x: x[0].lower()):
        lines.append(f"- [{sanitize(name)}]({century}/{dname}/page.md) {years} — {desc}")
(PAGES / 'INDEX.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

# 各世纪分索引
for century in ordered:
    title = CENTURY_TITLES.get(century, century)
    items = century_entries[century]
    clines = [
        f"# {title} 数学家页面索引\n",
        f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 共 **{len(items)}** 人\n",
    ]
    for name, dname, years, desc in sorted(items, key=lambda x: x[0].lower()):
        clines.append(f"- [{sanitize(name)}]({dname}/page.md) {years} — {desc}")
    (PAGES / century / 'INDEX.md').write_text('\n'.join(clines) + '\n', encoding='utf-8')

print(f"写入顶层 INDEX.md（共 {total} 人）")
for century in ordered:
    print(f"  写入 {century}/INDEX.md（{len(century_entries[century])} 人）")
