#!/usr/bin/env python3
"""
Optimize abel_prize_laureates_beamer.tex:
1. Add Nobel Economics / Turing badges
2. Replace cover with reference-style layout + portrait thumbnails
3. Update data rows (Nash → Nobel badge, Wigderson → Turing badge)
"""
import re, os, unicodedata

tex_path = "/Users/ericksun/workspace/codebuddy/math/medal_list_allinone/abel_beamer/abel_prize_laureates_beamer.tex"
img_dir = "/Users/ericksun/workspace/codebuddy/math/medal_list_allinone/abel_beamer/images"

with open(tex_path, 'r', encoding='utf-8') as f:
    tex = f.read()

# ── 1. Add Nobel/Turing colors ──
if 'nobelclr' not in tex:
    insert_pos = tex.find(r'\definecolor{wolfclr}{RGB}{150,100,0}') + len(r'\definecolor{wolfclr}{RGB}{150,100,0}') + 1
    add_colors = r'\definecolor{nobelclr}{RGB}{176,141,45}   % Nobel Economics — gold'
    tex = tex[:insert_pos] + add_colors + '\n' + tex[insert_pos:]

# ── 2. Add \nobelbadge and \turingbadge commands ──
# Find the chernbadge definition, add after it
chern_pos = tex.rfind(r'\newcommand{\chernbadge}')
end_chern = tex.find('\n', chern_pos)
new_badges = r'''
\newcommand{\nobelbadge}{\textsuperscript{\normalfont\tiny\color{nobelclr}\faIcon{award}\kern-0.5pt N}}
\newcommand{\turingbadge}{\textsuperscript{\normalfont\tiny\color{coverprimary}\faIcon{desktop}\kern-0.5pt T}}'''
tex = tex[:end_chern] + new_badges + tex[end_chern:]

# ── 3. Add fontawesome5 if not present (for \faIcon) ──
if r'\usepackage{fontawesome5}' not in tex:
    tex = tex.replace(r'\usepackage{graphicx}', r'\usepackage{graphicx}\usepackage{fontawesome5}')

# ── 4. Add additional color for turingbadge ──
if r'\definecolor{coverprimary}' not in tex:
    add_turing_clr = r'\definecolor{coverprimary}{HTML}{1A56DB}   % Turing — blue'
    tex = tex.replace(r'\definecolor{nobelclr}{RGB}{176,141,45}',
                      r'\definecolor{coverprimary}{HTML}{1A56DB}\n\definecolor{nobelclr}{RGB}{176,141,45}')

# ── 5. Update data: Nash → add nobelbadge, Wigderson → turingbadge ──
tex = tex.replace(
    r'\lrow{John F. Nash Jr.\cn{约翰·纳什}}{2015}{1928–2015}{美国}{Princeton University}{非线性偏微分方程}',
    r'\lrow{John F. Nash Jr.\nobelbadge\cn{约翰·纳什}}{2015}{1928–2015}{美国}{Princeton University}{非线性偏微分方程；亦获 N1994}'
)
tex = tex.replace(
    r'\lrow{Avi Wigderson\cn{阿维·维格森}}{2021}{1956–}{以色列/美国}{IAS Princeton}{理论计算机科学；亦获 2023 图灵奖}',
    r'\lrow{Avi Wigderson\turingbadge\cn{阿维·维格森}}{2021}{1956–}{以色列/美国}{IAS Princeton}{理论计算机科学；亦获 T2023}'
)

# ── 6. Update summary slide to add Nobel/Turing legend ──
tex = tex.replace(
    r'{\footnotesize\color{mutedgray} 2003–2026 · 挪威科学与文学院颁发 · 共 29 位 \quad 交叉获奖：{\color{fieldsclr}$\blacklozenge$F} 菲尔兹奖 · {\color{wolfclr}$\bigstar$W} 沃尔夫奖 · {\color{chernclr}$\blacksquare$C} 陈省身奖章}',
    r'{\footnotesize\color{mutedgray} 2003–2026 · 挪威科学与文学院颁发 · 共 29 位 \quad 交叉获奖：{\color{fieldsclr}$\blacklozenge$F} 菲尔兹奖 · {\color{wolfclr}$\bigstar$W} 沃尔夫奖 · {\color{chernclr}$\blacksquare$C} 陈省身奖章 · {\color{nobelclr}\faIcon{award}N} 诺贝尔经济学奖 · {\color{coverprimary}\faIcon{desktop}T} 图灵奖}'
)

# ── 7. Replace cover slide ──
# Find old cover block
cover_start = tex.find(r'\begin{frame}')
# Find the first frame — the title slide
title_begin = tex.find(r'\begin{frame}')
title_end = tex.find(r'\end{frame}', title_begin) + len(r'\end{frame}')

# ── 8. Generate portrait grid ──
# Extract names from \lrow calls, in order
names = []
for m in re.finditer(r'\\lrow\{([A-Z][^{}]+?)(?:\\[a-z]+badge)*\\cn\{[^}]+\}', tex):
    name = m.group(1).strip()
    if name not in names:
        names.append(name)

# Also extract from the tex in table rows
# Better: parse \lrow{Name... pattern
all_names = []
for m in re.finditer(r'\\lrow\{([A-Z][^}\\]*?)(?:\\[a-z]+badge)*\\cn\{([^}]+)\}', tex):
    eng = m.group(1).strip()
    if eng not in all_names:
        all_names.append(eng)
    print(f"  {eng:40s}  →  {m.group(2)}")

print(f"\nLaureates: {len(all_names)}")

# Map to images
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

avail = [f for f in os.listdir(img_dir)
         if not f.endswith('.bak') and os.path.getsize(os.path.join(img_dir, f)) > 1024]

best_img = {}
for f in avail:
    base = strip_accents(os.path.splitext(f)[0].lower().replace("-","").replace("_","").replace(" ",""))
    if base not in best_img:
        best_img[base] = f

found, missing = [], []
for name in all_names:
    parts = [p.strip().rstrip('Jr\.').lower() for p in name.split() if p not in ('Jr.', 'S.','R.')]
    matched = None
    for search_name in parts[::-1]:  # try last name first
        sn = strip_accents(search_name)
        for base, fn in best_img.items():
            if sn in base:
                matched = fn; break
        if matched: break
    if matched:
        found.append((name, matched))
    else:
        missing.append(name)

print(f"Images: {len(found)}/{len(all_names)}")
for m in missing:
    print(f"  MISSING: {m}")

# Build portrait grid: 29 laureates → N_COLS × N_ROWS
N_COLS, N_ROWS = 15, 2
W, H, GAP = 0.48, 0.58, 0.05
TOTAL_W = (N_COLS-1)*(W+GAP)
TOTAL_H = (N_ROWS-1)*(H+GAP)
START_X = -TOTAL_W/2
START_Y = TOTAL_H/2

grid_lines = []
grid_lines.append(r'  \node[anchor=center] at ([yshift=-1.55cm]current page.center) {')
grid_lines.append(r'    \begin{tikzpicture}[scale=1]')

count = 0
for row in range(N_ROWS):
    for col in range(N_COLS):
        if count >= len(found):
            break
        name, fn = found[count]
        x = START_X + col * (W + GAP)
        y = START_Y - row * (H + GAP)
        grid_lines.append(f'      \\node[inner sep=0pt] at ({x:.2f},{y:.2f}) {{')
        grid_lines.append(f'        \\includegraphics[width={W}cm,height={H}cm,keepaspectratio]{{images/{fn}}}')
        grid_lines.append(f'      }};')
        count += 1

grid_lines.append(r'    \end{tikzpicture}')
grid_lines.append(r'  };')
grid_tikz = '\n'.join(grid_lines)

# Build new cover
new_cover = r'''\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[abelclr!2] (current page.north west) rectangle (current page.south east);
  \fill[abelclr!6] (current page.north west) ++(1.55,-1.35) circle (2.45cm);
  \fill[abelclr!8] (current page.south east) ++(-1.9,1.45) circle (2.70cm);
  \node[anchor=center, font=\fontsize{18}{24}\selectfont\bfseries, text=abelclr]
    at ([yshift=2.80cm]current page.center) {阿贝尔奖：数学家的终身成就奖（2003–2026）};
  \node[anchor=center, font=\fontsize{11}{15}\selectfont, text=mutedgray]
    at ([yshift=1.60cm]current page.center) {Abel Prize\enspace·\enspace 数学界的诺贝尔奖\enspace·\enspace 全 29 位得主};
  \draw[abelclr!50, line width=1.2pt] ([yshift=0.90cm, xshift=-5.0cm]current page.center)
    -- ([yshift=0.90cm, xshift=5.0cm]current page.center);
  \node[anchor=center, font=\fontsize{9}{12}\selectfont\bfseries, text=mutedgray]
    at ([yshift=0.20cm]current page.center) {兼录菲尔兹·沃尔夫·陈省身·诺贝尔经济学·图灵奖双料·大满贯得主};
''' + grid_tikz + r'''
  \node[anchor=south, font=\fontsize{6}{7}\selectfont, text=mutedgray]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace Abel Prize Laureates\enspace|\enspace 挪威科学与文学院\enspace|\enspace 2003–2026};
\end{tikzpicture}
\end{frame}'''

# Replace old cover
old_cover = tex[title_begin:title_end]
new_tex = tex[:title_begin] + new_cover + '\n\n' + tex[title_end+1:]

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(new_tex)

print(f"\n✅ Done: {count} portraits, Nobel+{missing=}")