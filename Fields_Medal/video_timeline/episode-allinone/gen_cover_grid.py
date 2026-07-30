#!/usr/bin/env python3
"""Fields Medal: remove topic labels, compress titles upward, add portrait thumbnails."""
import re, os, unicodedata

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

img_dir = "/Users/ericksun/workspace/codebuddy/math/Fields_Medal/video_timeline/episode-allinone/images"
tex_path = "/Users/ericksun/workspace/codebuddy/math/Fields_Medal/video_timeline/episode-allinone/fields_medal_allinone_zh.tex"

with open(tex_path) as f:
    tex = f.read()

# ── Extract laureate names (from \personslide calls) ──
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
         and f not in ('FieldsMedalBack_1080px.jpg', 'FieldsMedalFront_1080px.jpg')
         and os.path.getsize(os.path.join(img_dir, f)) > 1024]

best_img = {}
for f in avail:
    base = os.path.splitext(f)[0].lower().replace("-","").replace("_","").replace(" ","")
    ext = os.path.splitext(f)[1]
    if base not in best_img:
        best_img[base] = f
    elif ext == '.png' and os.path.splitext(best_img[base])[1] != '.png':
        best_img[base] = f

found, missing = [], []
for name in names:
    last = name.split()[-1].replace("'","").replace(".","").replace("-","").lower()
    last_ascii = strip_accents(last)
    img = None
    for base, fn in best_img.items():
        base_ascii = strip_accents(base)
        if last_ascii in base_ascii or last_ascii.replace(" ","") in base_ascii:
            img = fn
            break
    if img:
        found.append((name, img))
    else:
        missing.append(name)

print(f"Images: {len(found)}/{len(names)}, missing: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")

# ── Generate portrait grid ──
N_COLS, N_ROWS = 17, 4
W, H, GAP = 0.48, 0.58, 0.05
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

# ── Find and replace coverslide block ──
coverslide_start = tex.find(r'\newcommand{\coverslide}')
coverslide_end = tex.find('\n}\n\n% ---- Full-page chapter divider', coverslide_start)
old_coverslide = tex[coverslide_start:coverslide_end+1]

# Build new coverslide: compressed titles + portrait grid
new_coverslide = r'''\newcommand{\coverslide}{%
\begin{frame}[plain]
\deckbackground
\begin{tikzpicture}[remember picture, overlay]
  \node[anchor=center, font=\fontsize{24}{30}\selectfont\bfseries, text=coverdark]
    at ([yshift=2.80cm]current page.center) {群星闪耀九十年 —— 菲尔兹奖得主全传};
  \node[anchor=center, font=\fontsize{13}{17}\selectfont, text=coverprimary!82!black]
    at ([yshift=1.50cm]current page.center) {菲尔兹奖时间线\enspace·\enspace 全 68 位得主合集};
  \draw[covergold, line width=1.4pt] ([yshift=0.80cm, xshift=-5.3cm]current page.center)
    -- ([yshift=0.80cm, xshift=5.3cm]current page.center);
  \node[anchor=center, font=\fontsize{11}{14}\selectfont\bfseries, text=covergold!62!black]
    at ([yshift=0.05cm]current page.center) {68位菲尔兹奖得主谱系\enspace·\enspace 兼录沃尔夫·阿贝尔双料·大满贯得主};
''' + grid_tikz + r'''
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace Fields Medal Timeline\enspace|\enspace 合集\enspace|\enspace 现代数学九十年};
\end{tikzpicture}
\end{frame}
}'''

# ── Fix: check for extra }} ──
# The issue: find('\n}\n\n% ----') matches at \n, so coverslide_end = position of \n
# tex[coverslide_end+1] = }, tex[coverslide_end+2] = \n
# old_coverslide = tex[start:coverslide_end+1] → does NOT include }
# But tex[coverslide_end+1:] starts with }\n\n... → doubles with new_coverslide's trailing }
# Fix: change to coverslide_end+2
new_tex = tex[:coverslide_start] + new_coverslide + tex[coverslide_end+2:]

with open(tex_path, 'w') as f:
    f.write(new_tex)

print(f"\n✅ Coverslide updated: titles compressed upward, topic labels removed, {count} thumbnails added")
print(f"   Title yshift: 2.15→2.80, subtitle: 1.0→1.50, line: 0.32→0.80, 3rd-line: -0.5→0.05")
