#!/usr/bin/env python3
"""
Reorganize wolf_prize_allinone_zh.tex: from topic-based to year-based (chronological).
Groups into Parts by year ranges, starting from Part I.
"""
import re

path = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/wolf_prize_allinone_zh.tex"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split: preamble (up to and including \chapterdivider definition), slide blocks, body
# First, find all \newcommand{\xxxslide}{...} blocks

# Find the preamble end (before first \newcommand{\slide)
lines = content.split('\n')

# Identify sections:
# 0. preamble (up to first slide def)
# 1. Each slide: \newcommand{\xxxslide}{ ... }
# 2. body: \begin{document} ... \end{document}

# Find all slide definitions and their line ranges
class SlideBlock:
    pass

slide_blocks = []
i = 0
while i < len(lines):
    m = re.match(r'\\newcommand\{\\(\w+)\}', lines[i])
    if m:
        cmd_name = m.group(1)
        # Skip non-slide commands: personslide, personslideA, coverslide, chapterdivider, etc.
        if cmd_name in ('personslide', 'personslideA', 'coverslide', 'chapterdivider',
                        'sectiontitle', 'deckbackground', 'plainbar', 'portraitbox',
                        'placeholderportrait'):
            i += 1
            continue
        
        # Collect the full block including nested braces
        start = i
        brace_count = 0
        in_block = False
        while i < len(lines):
            for ch in lines[i]:
                if ch == '{':
                    brace_count += 1
                    in_block = True
                elif ch == '}':
                    brace_count -= 1
            if in_block and brace_count == 0:
                break
            i += 1
        
        block_lines = lines[start:i+1]
        block_text = '\n'.join(block_lines)
        
        # Extract year from award line: {1979（73岁）} or {1983/84（70岁）}
        ym = re.search(r'\{(\d{4})(?:/\d{2})?（\d+岁）\}', block_text)
        year = int(ym.group(1)) if ym else 9999
        
        # Extract English name (first {Name} after \personslide)
        nm = re.search(r'\\personslide(?:A)?\s*\n\s*\{([^}]+)\}', block_text)
        eng_name = nm.group(1).strip() if nm else "Unknown"
        
        # Extract award text
        award_text = ym.group(0).strip('{}') if ym else ""
        
        # Extract life: {1906--1998（享年92岁）}
        lm = re.search(r'\{(\d{4}--\d{4}（享年\d+岁）)\}', block_text)
        life_text = lm.group(1) if lm else ""
        
        # Check if has cross-content (def\crosscontent)
        has_cross = '\\def\\crosscontent' in block_text
        
        slide_blocks.append({
            'year': year,
            'eng': eng_name,
            'award': award_text,
            'life': life_text,
            'has_cross': has_cross,
            'lines': block_lines,
            'cmd': cmd_name,
            'text': block_text,
            'start_line': start,
            'end_line': i,
        })
    i += 1

# Sort by year, then by name
slide_blocks.sort(key=lambda x: (x['year'], x['eng']))

print(f"Total laureate slides: {len(slide_blocks)}")
for s in slide_blocks:
    print(f"  {s['year']:4d} | {s['award']:20s} | {s['eng']:35s} | {s['life']}")

# Now group by year
from collections import OrderedDict
year_groups = OrderedDict()
for s in slide_blocks:
    y = s['year']
    if y not in year_groups:
        year_groups[y] = []
    year_groups[y].append(s)

print(f"\nYear groups: {len(year_groups)}")
for y, group in year_groups.items():
    names = ', '.join(s['eng'].split()[-1] for s in group)
    print(f"  {y}: {len(group)} laureate(s) - {names}")

# Group years into logical Parts (about 5-7 laureates per part)
# Wolf Prize: 1978-2024, ~65 laureates, ~10 parts of ~6-7 each
all_years = sorted(year_groups.keys())
parts = []
current_part = []
part_label = 1

for y in all_years:
    # Count laureates so far in current part
    current_count = sum(len(year_groups[gy]) for gy in current_part)
    future_count = len(year_groups[y])
    
    if current_count + future_count > 7 and current_part:
        parts.append(current_part)
        current_part = [y]
    else:
        current_part.append(y)

if current_part:
    parts.append(current_part)

print(f"\nParts: {len(parts)}")
for pi, p in enumerate(parts):
    yr_range = f"{min(p)}–{max(p)}" if len(p) > 1 else str(p[0])
    total = sum(len(year_groups[y]) for y in p)
    print(f"  Part {pi+1}: {yr_range} ({total} laureates)")

# Now generate the chapter dividers
roman_map = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII'}

print("\n=== Chapter dividers ===")
for pi, p in enumerate(parts):
    yrs = sorted(p)
    yr_range = f"{min(yrs)}–{max(yrs)}" if len(yrs) > 1 else str(yrs[0])
    names = []
    for y in yrs:
        for s in year_groups[y]:
            names.append(s['eng'].split()[-1])
    name_str = ' · '.join(names)
    print(f"  Part {roman_map[pi+1]}: {yr_range} — {name_str}")
