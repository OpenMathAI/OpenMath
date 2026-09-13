#!/usr/bin/env python3
"""将 turing/presentations 下得主意传目录重命名为 {year}_{DirName}。
年份来源：prompt_manifest.json（1975-2025）+ 手工补充早期得主。仅改目录名，不改文件内容。"""
import json, os
from pathlib import Path

PRES = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI/turing/presentations')

# manifest title -> 实际目录名 例外（与下划线直转不同者）
TITLE_EXCEPTIONS = {
    'Jim Gray (computer scientist)': 'Jim_Gray',
    'Charles H. Bennett (physicist)': 'Charles_H._Bennett',
    'David Patterson (computer scientist)': 'David_Patterson',
    'Frances E. Allen': 'Frances_Allen',
    'Butler W. Lampson': 'Butler_Lampson',
    'Ronald Rivest': 'Ron_Rivest',
}

# manifest 之外的得主（年份_目录名）
EXTRA = {
    1966: 'Alan_Perlis', 1967: 'Maurice_Wilkes', 1968: 'Richard_Hamming',
    1969: 'Marvin_Minsky', 1970: 'James_H._Wilkinson', 1971: 'John_McCarthy',
    1972: 'Edsger_W._Dijkstra', 1973: 'Charles_Bachman', 1974: 'Donald_Knuth',
    1983: 'Ken_Thompson', 1983: 'Dennis_Ritchie',
    2000: 'Andrew_Yao', 2013: 'Leslie_Lamport',
}

def main():
    manifest = json.loads((PRES.parent / 'prompt_manifest.json').read_text())
    mapping = {}
    for e in manifest:
        d = TITLE_EXCEPTIONS.get(e['title']) or e['title'].replace(' ', '_')
        mapping[d] = e['year']
    mapping.update({v: k for k, v in EXTRA.items()})

    existing = {p.name for p in PRES.iterdir() if p.is_dir()}
    targets = {d: y for d, y in mapping.items() if d in existing}
    unmatched = existing - set(targets) - {'cover'}
    print(f'匹配 {len(targets)} 个目录；未匹配（保持原样）: {sorted(unmatched)}')

    # 校验：新名不与现有冲突，且同一目标不重复
    news = {}
    for d, y in targets.items():
        n = f'{y}_{d}'
        assert n not in existing, f'目标已存在: {n}'
        assert n not in news, f'目标重复: {n}'
        news[d] = n

    for d, n in sorted(news.items()):
        os.rename(PRES / d, PRES / n)
        print(f'{d} -> {n}')
    print(f'--- 共重命名 {len(news)} 个目录')

if __name__ == '__main__':
    main()
