#!/usr/bin/env python3
"""Abel Prize cover: new title, remove topic labels, add portrait thumbnails."""
import re, os, unicodedata

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

img_dir = "/Users/ericksun/workspace/codebuddy/math/Abel_Prize/video/episode-allinone/images"
tex_path = "/Users/ericksun/workspace/codebuddy/math/Abel_Prize/video/episode-allinone/abel_prize_allinone_zh.tex"

with open(tex_path) as f:
    tex = f.read()

# ── Extract laureate names from \personslide calls (in order) ──
names = []
for m in re.finditer(r'\\personslide\s*\n\s*\{([^}]+)\}', tex):
    n = m.group(1).strip()
    if n not in names and n != "Unknown":
        names.append(n)

print(f"Laureates: {len(names)}")

# ── Map to images ──
avail_all = os.listdir(img_dir)
avail = [f for f in avail_all
         if not f.endswith('.bak') and not f.endswith('.tmp')
         and os.path.getsize(os.path.join(img_dir, f)) > 1024]

best_img = {}
for f in avail:
    base = os.path.splitext(f)[0].lower().replace("-","").replace("_","").replace(" ","")
    if base not in best_img:
        best_img[base] = f

found, missing = [], []
for name in names:
    last = name.split()[-1].replace("'","").replace(".","").replace("-","").lower()
    # Also try second-to-last for "John F. Nash Jr." → "nash"
    p2 = name.split()[-2].replace("'","").replace(".","").replace("-","").lower() if len(name.split())>=2 else last
    last_ascii = strip_accents(last)
    p2_ascii = strip_accents(p2)
    img = None
    for base, fn in best_img.items():
        base_ascii = strip_accents(base)
        if last_ascii in base_ascii or p2_ascii in base_ascii:
            img = fn; break
    if img:
        found.append((name, img))
    else:
        missing.append(name)

print(f"Images: {len(found)}/{len(names)}, missing: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")

# ── Generate portrait grid: 30 laureates → 10×3 or 15×2 ──
# Use 15 cols × 2 rows for Abel (fewer laureates, bigger thumbs)
N_COLS, N_ROWS = 15, 2
W, H, GAP = 0.55, 0.65, 0.06
TOTAL_W = (N_COLS-1)*(W+GAP)
TOTAL_H = (N_ROWS-1)*(H+GAP)
START_X = -TOTAL_W/2
START_Y = TOTAL_H/2

lines = []
lines.append(r'  \node[anchor=center] at ([yshift=-1.55cm]current page.center) {')
lines.append(r'    \begin{tikzpicture}[scale=1]')

count = 0
for row in range(N_ROWS):
    for col in range(N_COLS):
        if count >= len(found):
            break
        name, fn = found[count]
        x = START_X + col * (W + GAP)
        y = START_Y - row * (H + GAP)
        safe_fn = fn.replace('%','\\%').replace('#','\\#')
        lines.append(f'      \\node[inner sep=0pt] at ({x:.2f},{y:.2f}) {{')
        lines.append(f'        \\includegraphics[width={W}cm,height={H}cm,keepaspectratio]{{images/{safe_fn}}}')
        lines.append(f'      }};')
        count += 1

lines.append(r'    \end{tikzpicture}')
lines.append(r'  };')

grid_tikz = '\n'.join(lines)
print(f"\nGrid: {count} portraits, {N_COLS}×{N_ROWS}, {TOTAL_W:.1f}cm×{TOTAL_H:.1f}cm")

# ── Build new coverslide ──
new_coverslide = r'''\newcommand{\coverslide}{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!7] (current page.north west) rectangle (current page.south east);
  \fill[coverprimary!12] (current page.north west) ++(1.55,-1.35) circle (2.45cm);
  \fill[covergold!12] (current page.south east) ++(-1.9,1.45) circle (2.70cm);
  \node[anchor=center, font=\fontsize{24}{30}\selectfont\bfseries, text=coverdark]
    at ([yshift=2.80cm]current page.center) {阿贝尔奖：数学家的终身成就奖（2003–2026）};
  \node[anchor=center, font=\fontsize{13}{17}\selectfont, text=coverprimary!82!black]
    at ([yshift=1.55cm]current page.center) {Abel Prize\enspace·\enspace 数学界的诺贝尔奖\enspace·\enspace 全 29 位得主合集};
  \draw[coverprimary, line width=1.4pt] ([yshift=0.85cm, xshift=-5.2cm]current page.center)
    -- ([yshift=0.85cm, xshift=5.2cm]current page.center);
  \node[anchor=center, font=\fontsize{10.5}{14}\selectfont\bfseries, text=covergold!58!black]
    at ([yshift=0.15cm]current page.center) {兼录菲尔兹·沃尔夫·陈省身·诺贝尔奖双料·大满贯得主};
''' + grid_tikz + r'''
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace Abel Prize\enspace|\enspace 挪威科学与文学院\enspace|\enspace 合集};
\end{tikzpicture}
\end{frame}
}'''

# ── Replace in tex file ──
coverslide_start = tex.find(r'\newcommand{\coverslide}')
# Find end: the next '\newcommand{\chapterslide}' or '}\n\n% ---- Chapter divider'
end_marker = tex.find('\n% ---- Chapter divider', coverslide_start)
coverslide_end = tex[:end_marker].rfind('}')

old_block = tex[coverslide_start:coverslide_end+1]
new_tex = tex[:coverslide_start] + new_coverslide + tex[coverslide_end+1:]

with open(tex_path, 'w') as f:
    f.write(new_tex)

print(f"\n✅ Coverslide updated")
print(f"   Old title: '阿贝尔奖' → New: '阿贝尔奖：数学家的终身成就奖（2003–2026）'")
print(f"   Removed: topic labels, cross-award annotation line")
print(f"   Added: {count} portrait thumbnails")
