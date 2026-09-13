#!/usr/bin/env python3
"""将全部图灵奖立传封面（titleslide 块内）对齐 Dijkstra 版式：
标题 30/36 -> 26/32；badge 主字体 footnotesize -> scriptsize；副行 scriptsize -> 6.5/7.8。
不做编译。"""
from pathlib import Path
import re

PRES = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI/turing/presentations')
SKIP = {'Edsger_W._Dijkstra'}  # 已手工改好

def process(path: Path):
    src = path.read_text()
    m = re.search(r'\\newcommand\{\\titleslide\}\{.*?(?=\\newcommand\{\\|% ---)', src, re.S)
    if not m:
        return None
    block = m.group(0)
    orig = block
    stats = []
    n1 = block.count(r'\fontsize{30}{36}')
    block = block.replace(r'\fontsize{30}{36}', r'\fontsize{26}{32}')
    if n1: stats.append(f'title x{n1}')
    n2 = block.count(r'font=\footnotesize\bfseries')
    block = block.replace(r'font=\footnotesize\bfseries', r'font=\scriptsize\bfseries')
    if n2: stats.append(f'badgefont x{n2}')
    # 副行：逐行处理，行尾 ;} 需补一个右括号
    out_lines, n3 = [], 0
    for line in block.split('\n'):
        if r'\par\scriptsize ' in line:
            eol = ''
            core = line
            while core and core[-1] in '\r\n':
                eol = core[-1] + eol
                core = core[:-1]
            stripped = core.rstrip()
            trail_ws = core[len(stripped):]
            if stripped.endswith('};'):
                stripped = stripped[:-2] + '}};'
                n3 += 1
            elif stripped.endswith('}'):
                stripped = stripped[:-1] + '}}'
                n3 += 1
            core = stripped + trail_ws
            core = core.replace(r'\par\scriptsize ', r'\par{\fontsize{6.5}{7.8}\selectfont ')
            line = core + eol
        out_lines.append(line)
    block = '\n'.join(out_lines)
    if n3: stats.append(f'subline x{n3}')
    if block != orig:
        src = src[:m.start()] + block + src[m.end():]
        path.write_text(src)
    return stats

def main():
    done = skipped = 0
    for path in sorted(PRES.glob('*/*_zh.tex')):
        if path.parent.name in SKIP or path.parent.name == 'cover':
            continue
        s = process(path)
        if s is None:
            print(f'{path.parent.name}: NO titleslide block, skip')
            skipped += 1
        elif not s:
            print(f'{path.parent.name}: no change')
            skipped += 1
        else:
            done += 1
            print(f'{path.parent.name}: ' + ', '.join(s))
    print(f'--- modified {done}, unchanged/skip {skipped}')

if __name__ == '__main__':
    main()
