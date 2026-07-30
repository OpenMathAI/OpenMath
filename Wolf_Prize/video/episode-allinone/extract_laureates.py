#!/usr/bin/env python3
"""Extract all Wolf laureates with award years - simpler approach."""
import re

path = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/wolf_prize_allinone_zh.tex"
with open(path) as f:
    lines = f.readlines()

laureates = []
i = 0
while i < len(lines):
    line = lines[i]
    # Find award year lines: "{1979（73岁）}," or "{1983/84（70岁）},"
    m = re.search(r'\{(\d{4})(?:/\d{2})?（(\d+)岁）\}', line)
    if m and ('\\personslide' in lines[i-1] or '\\personslideA' in lines[i-2] or '\\personslide' in lines[i-2] or '\\personslideA' in lines[i-3]):
        year = int(m.group(1))
        award_str = m.group(0).strip('{},')
        
        # Find English name (lines above)
        eng_name = ""
        chn_name = ""
        full_block = ""
        for j in range(max(0,i-10), i+3):
            full_block += lines[j]
        
        # The name is usually 2-3 lines above the year
        # Structure:
        # \personslide
        #   {English Name}       <- this line
        #   {Chinese Name...}
        #   {images/...}
        #   {Photo: ...}
        #   {1979（73岁）}        <- current line (year)
        
        # Find name by going up from year line
        for j in range(i-4, max(0, i-6), -1):
            nm = re.match(r'\s*\{(.+?)\}', lines[j].strip())
            if nm:
                name = nm.group(1)
                if 'Photo' in name or 'images/' in name or name.strip().startswith('{'):
                    continue
                if not eng_name:
                    eng_name = name
                elif not chn_name:
                    chn_name = name
                if eng_name and chn_name:
                    break
        
        # Get life line
        life = ""
        for j in range(i+1, min(len(lines), i+3)):
            lm = re.match(r'\s*\{(.+?)\}', lines[j].strip())
            if lm and ('--' in lm.group(1) or '---' in lm.group(1)):
                life = lm.group(1)
                break
        
        laureates.append({
            'year': year, 'award': award_str,
            'eng': eng_name, 'chn': chn_name,
            'life': life,
            'line_idx': i
        })
    i += 1

# Deduplicate by line index
seen = set()
unique = []
for l in laureates:
    if l['line_idx'] not in seen:
        seen.add(l['line_idx'])
        unique.append(l)

unique.sort(key=lambda x: (x['year'], x['eng']))

print(f"Total: {len(unique)} laureates\n")
for l in unique:
    print(f"{l['year']:4d} | {l['award']:20s} | {l['eng']:30s} | {l['life']:25s} | line {l['line_idx']}")
