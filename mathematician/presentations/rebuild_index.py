#!/usr/bin/env python3
"""扫描 pages 下所有目录，重建完整 INDEX.md。"""
import json, time, re
from pathlib import Path

PAGES = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages')

def sanitize(s):
    return re.sub(r'[<>|:]*', '', str(s))

entries = []
for d in sorted(PAGES.iterdir()):
    if not d.is_dir():
        continue
    md = d / 'page.md'
    meta = d / 'metadata.json'
    if not md.exists():
        continue
    name = d.name
    birth = death = desc = ''
    if meta.exists():
        try:
            m = json.loads(meta.read_text(encoding='utf-8'))
            name = m.get('label') or name
            desc = m.get('description') or ''
        except Exception:
            pass
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
    years = f"（{birth}–{death}）" if birth or death else ''
    rel = f"{d.name}/page.md"
    entries.append((name, rel, years, desc))

lines = [
    "# 数学家完整页面索引\n",
    f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
    f"> 共 **{len(entries)}** 人\n",
]
for name, rel, years, desc in sorted(entries, key=lambda x: x[0].lower()):
    lines.append(f"- [{sanitize(name)}]({rel}) {years} — {desc}")

(PAGES / 'INDEX.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f"写入 {len(entries)} 人 → INDEX.md")
