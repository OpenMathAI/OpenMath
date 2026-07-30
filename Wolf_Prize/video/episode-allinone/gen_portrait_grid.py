#!/usr/bin/env python3
"""Generate portrait thumbnail grid for Wolf cover slide, then replace in tex."""
import re, os

img_dir = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/images"
tex_path = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/wolf_prize_allinone_zh.tex"

with open(tex_path) as f:
    tex = f.read()

# Extract laureate names in order
names = []
for m in re.finditer(r'\\personslide(?:A)?\s*\n\s*\{([^}]+)\}', tex):
    n = m.group(1).strip()
    if n not in names and n != "Unknown":
        names.append(n)

# Map to best image (prefer .png > .jpg > .jpeg, avoid .bak)
avail_all = os.listdir(img_dir)
# Filter: no .bak, no .tmp, and must be > 1KB (valid image)
avail = [f for f in avail_all 
         if not f.endswith('.bak') and not f.endswith('.tmp')
         and os.path.getsize(os.path.join(img_dir, f)) > 1024]
# Group by base name, prefer .png
best_img = {}
for f in avail:
    base = os.path.splitext(f)[0].lower()
    ext = os.path.splitext(f)[1]
    if base not in best_img:
        best_img[base] = f
    else:
        # Prefer png over jpg/jpeg
        old_ext = os.path.splitext(best_img[base])[1]
        if ext == '.png' and old_ext != '.png':
            best_img[base] = f

def strip_accents(s):
    """Remove diacritics for accent-insensitive matching."""
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

found = []
missing = []
for name in names:
    last = name.split()[-1].replace("'","").replace(".","").replace("-","").lower()
    last_ascii = strip_accents(last)
    img = None
    for base, fn in best_img.items():
        base_ascii = strip_accents(base.replace("-",""))
        if last in base_ascii or last_ascii in base_ascii:
            img = fn
            break
    if img:
        found.append((name, img))
    else:
        missing.append(name)

print(f"Laureates: {len(names)}, with images: {len(found)}, missing: {len(missing)}")
if missing:
    for m in missing:
        print(f"  MISSING: {m}")

# ── Generate 16×4 grid tikz code ──
N_COLS, N_ROWS = 16, 4
W, H, GAP = 0.52, 0.62, 0.06
TOTAL_W = (N_COLS-1)*(W+GAP)
TOTAL_H = (N_ROWS-1)*(H+GAP)
START_X = -TOTAL_W/2
START_Y = TOTAL_H/2

lines = []
lines.append(r'  \node[anchor=center] at ([yshift=-2.10cm]current page.center) {')
lines.append(r'    \begin{tikzpicture}[scale=1]')

count = 0
for row in range(N_ROWS):
    for col in range(N_COLS):
        if count >= len(found):
            break
        name, fn = found[count]
        x = START_X + col * (W + GAP)
        y = START_Y - row * (H + GAP)
        # Check for problematic filenames
        safe_fn = fn.replace('%','\\%').replace('#','\\#')
        lines.append(f'      \\node[inner sep=0pt] at ({x:.2f},{y:.2f}) {{')
        lines.append(f'        \\includegraphics[width={W}cm,height={H}cm,keepaspectratio]{{images/{safe_fn}}}')
        lines.append(f'      }};')
        count += 1

lines.append(r'    \end{tikzpicture}')
lines.append(r'  };')

grid_tikz = '\n'.join(lines)
print(f"\nGrid: {count} portraits, {N_COLS}×{N_ROWS}")

# ── Replace in tex file ──
# Find the old Part labels block
old_start = r'  \node[anchor=center] at ([yshift=-2.10cm]current page.center) {'
old_end_pattern = r'  };'

# Find the block in tex
idx = tex.find(old_start)
if idx < 0:
    print("ERROR: Could not find Part labels block in tex file!")
    sys.exit(1)

# Find matching closing
depth = 0
end_idx = idx
for i in range(idx, len(tex)):
    if tex[i] == '{':
        depth += 1
    elif tex[i] == '}':
        depth -= 1
        if depth == 0:
            end_idx = i + 1
            break

# The block includes the trailing "  };" so let's find the line with "  };"
# Actually the old block is:
old_block_end = '\n  };'
block_start = idx
block_end = tex.find(old_block_end, idx) + len(old_block_end)

old_block = tex[block_start:block_end]
new_tex = tex[:block_start] + grid_tikz + tex[block_end:]

with open(tex_path, 'w') as f:
    f.write(new_tex)

print(f"\n✅ Replaced Part labels with {count} portrait thumbnails")
print(f"   Grid size: {TOTAL_W:.1f}cm × {TOTAL_H:.1f}cm")