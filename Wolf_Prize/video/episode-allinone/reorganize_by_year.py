#!/usr/bin/env python3
"""Final: extract ALL slides, sort by year, rebuild. One-shot script."""
import re, sys

fpath = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/wolf_prize_allinone_zh.tex"
with open(fpath, 'r', encoding='utf-8') as f:
    txt = f.read()
L = txt.split('\n')

# Find document boundaries
ds = next(i for i,l in enumerate(L) if r'\begin{document}' in l)
de = next(i for i,l in enumerate(L) if r'\end{document}' in l)
pre = L[:ds]
bod = L[ds+1:de]  # between \begin and \end

YR = re.compile(r'\{(\d{4})(?:/\d{2})?\uff08(\d+)岁\uff09\}')

def gyr(t): m=YR.search(t); return int(m.group(1)) if m else 9999
def gnm(t): 
    m=re.search(r'\\personslide(?:A)?\s*\n\s*\{([^}]+)\}', t)
    return m.group(1).strip() if m else "???"

# ── 1. Extract slide-data from preamble \\newcommand blocks ──
# These define \\xxxslide, used later via \\xxxslide in body
cmd_info = {}  # cmd_name -> {'year':int, 'lines':[...]}
i = 0
while i < len(pre):
    m = re.match(r'\\newcommand\{\\(\w+slide)\}\{%', pre[i].strip())
    if m:
        nm = m.group(1)
        if nm not in ('personslide','personslideA','coverslide','chapterdivider',
                      'sectiontitle','deckbackground','plainbar','portraitbox','placeholderportrait'):
            blk = [pre[i]]
            end_found = False
            for j in range(i+1, len(pre)):
                blk.append(pre[j])
                if pre[j].strip() == '}':
                    end_found = True
                    break
            if end_found:
                y = gyr('\n'.join(blk))
                if y != 9999: 
                    cmd_info[nm] = {'year':y, 'lines':blk, 'name': gnm('\n'.join(blk))}
        i += 1
    else:
        i += 1

print(f"1. Preamble cmd slides: {len(cmd_info)}")

# ── 2. Extract slide-data from body (both \\xxxslide calls and inline \\personslide) ──
# Find ALL slide blocks in body using line-range approach
import itertools

# Mark every line that starts a slide
slide_starts = []
slide_starts_raw = []  # (type, line_idx, cmd_name_or_None)
for i, l in enumerate(bod):
    s = l.strip()
    if s == r'\coverslide':
        slide_starts_raw.append(('cover', i, None))
    elif re.match(r'\\(\w+slide)$', s) and s[1:] in cmd_info:
        slide_starts_raw.append(('call', i, s[1:]))
    elif s in (r'\personslide', r'\personslideA'):
        # Check if preceded by \\def\\crosscontent...\\end{tikzpicture}}
        st = i
        if i > 0 and r'\end{tikzpicture}}' in bod[i-1].strip():
            for j in range(i-2, max(0, i-40), -1):
                if r'\def\crosscontent' in bod[j]: st = j; break
                if bod[j].strip() in (r'\personslide',r'\personslideA') or r'\chapterdivider' in bod[j]: break
        slide_starts_raw.append(('inline', st, None))

slide_starts = [s[1] for s in slide_starts_raw]  # just line numbers for boundaries
dividers = [i for i,l in enumerate(bod) if r'\chapterdivider' in l]

slide_blocks = []
for idx, (stype, start, cmd) in enumerate(slide_starts_raw):
    end = len(bod)
    for bv in sorted(set(slide_starts[idx+1:] + dividers + [len(bod)])):
        if bv > start: end = bv; break
    block_txt = '\n'.join(bod[start:end]).strip()
    
    if stype == 'call':
        ci = cmd_info[cmd]
        slide_blocks.append({'year': ci['year'], 'text': block_txt, 'name': ci['name']})
    elif stype == 'inline':
        y = gyr(block_txt)
        if y != 9999:
            slide_blocks.append({'year': y, 'text': block_txt, 'name': gnm(block_txt)})

print(f"2. Body slide blocks: {len(slide_blocks)}")

# ── 3. Combine & deduplicate ──
# We also need the \\xxxslide calls from the body. But we already have them as
# slide_blocks. The cmd_info contains the preamble DEFINITIONS (not calls).
# The slide_blocks contain BOTH the calls and inline blocks.

# Also, we should include the \\newcommand slide blocks as they appear in the body
# via calls. But the body already has the calls.

# Dedup
seen_n = set()
uniq = []
for s in slide_blocks:
    n = s['name']
    if n not in seen_n:
        seen_n.add(n); uniq.append(s)

uniq.sort(key=lambda x: (x['year'], x['name']))
print(f"3. Unique slides: {len(uniq)}")

# ── 4. Group into Parts ──
from collections import OrderedDict
yg = OrderedDict()
for s in uniq: yg.setdefault(s['year'], []).append(s)
all_y = sorted(yg.keys())
parts,cur=[],[]
for y in all_y:
    if sum(len(yg[gy]) for gy in cur)+len(yg[y])>8 and cur:
        parts.append(cur); cur=[y]
    else: cur.append(y)
if cur: parts.append(cur)

R = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII'}
print(f"4. Parts: {len(parts)}")
for pi,p in enumerate(parts):
    yrs=sorted(p); yr_r=f"{min(yrs)}–{max(yrs)}" if len(p)>1 else str(yrs[0])
    nms=[s['name'].split()[-1] for y in p for s in yg[y]]
    print(f"   Part {R[pi+1]}: {yr_r} ({sum(len(yg[y]) for y in p)}) — {', '.join(nms)}")

# ── 5. Rebuild file ──
out = pre + [r'\begin{document}']
# cover
for l in bod:
    if l.strip() == r'\coverslide': out.append(l); break
out.append('')

for pi,p in enumerate(parts):
    yrs=sorted(p); yr_r=f"{min(yrs)}–{max(yrs)}" if len(p)>1 else str(yrs[0])
    nms=[s['name'].split()[-1] for y in p for s in yg[y]]
    out.append(f'\\chapterdivider{{Part {R[pi+1]}}}{{{yr_r}}}{{{" · ".join(nms)}}}')
    for y in p:
        for s in yg[y]:
            out.append(s['text']); out.append('')
out.append(r'\end{document}')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print(f"\n✅ Done: {len(uniq)} slides, {len(parts)} Parts → {fpath}")
