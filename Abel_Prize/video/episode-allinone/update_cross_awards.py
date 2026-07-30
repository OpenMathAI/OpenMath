#!/usr/bin/env python3
"""
Add cross-award boxes to Abel Prize laureate slides.
Mirrors Fields_Medal/video_timeline/episode-allinone/update_cross_awards.py.
Badges: Fields (blacklozenge), Wolf (bigstar), Chern (blacksquare),
        Nobel Economics (faIcon award) — the latter for John Nash.
Strategy: global \crosscontent command, set by each slide before \personslide.
"""
import re

path = "/Users/ericksun/workspace/codebuddy/math/Abel_Prize/video/episode-allinone/abel_prize_allinone_zh.tex"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: define empty \crosscontent in preamble (after last color definition)
if r'\def\crosscontent{}' not in content:
    content = content.replace(
        r'\definecolor{graypanel}{RGB}{242,245,249}',
        r'\definecolor{graypanel}{RGB}{242,245,249}\def\crosscontent{}',
        1,
    )

# Step 2: inject \crosscontent into the \personslide macro (2nd column) + reset
old_col = r"""      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
\end{column}"""
new_col = r"""      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
  \crosscontent
\end{column}"""
assert old_col in content, "personslide 2nd column not found"
content = content.replace(old_col, new_col, 1)

# reset \crosscontent at end of frame
content = content.replace(
    r"""\end{columns}
\end{frame}
}""",
    r"""\end{columns}
\gdef\crosscontent{}
\end{frame}
}""",
    1,
)

# Step 3: ensure amssymb loaded (for blacklozenge/blacksquare/bigstar)
if r'\usepackage{amssymb}' not in content:
    content = content.replace(
        r'\usetikzlibrary{positioning,calc,arrows.meta,shadows}',
        r'\usetikzlibrary{positioning,calc,arrows.meta,shadows}' + '\n' + r'\usepackage{amssymb}',
        1,
    )

# ---- cross-award box builders ----
def make_cross_box(lines):
    inner = r'\\[1.5pt]'.join(lines)
    return (r"""\def\crosscontent{\vspace{4pt}
  \begin{tikzpicture}
    \node[draw=covergold!55, fill=graypanel, rounded corners=3pt, inner xsep=5pt, inner ysep=4pt, text width=3.8cm, align=left] {
      {\fontsize{6.5}{7.8}\selectfont\bfseries\color{coverprimary!75!black} 亦获其他顶级奖项}\\[2pt]
      """ + inner + r"""
    };
  \end{tikzpicture}}""")

def award_line(symbol, name, year, age):
    return (r"""{\fontsize{6}{7}\selectfont\bfseries\color{covergold!45!black} """ + symbol + ' ' + name +
            r"""}\enspace{\fontsize{6}{7}\selectfont\color{coverdark!80} """ + year +
            r"""（""" + age + """岁）}""")

F = r"$\blacklozenge$"   # Fields
W = r"$\bigstar$"        # Wolf
C = r"$\blacksquare$"    # Chern
N = r"\faIcon{award}"    # Nobel (Economics)

CROSS = {
    # Fields + Wolf (triple with Abel)
    "serreslide":     make_cross_box([award_line(F, "菲尔兹奖", "1954", "27"), award_line(W, "沃尔夫奖", "2000", "74")]),
    "milnorslide":    make_cross_box([award_line(F, "菲尔兹奖", "1962", "31"), award_line(W, "沃尔夫奖", "1989", "58")]),
    "thompsonslide":  make_cross_box([award_line(F, "菲尔兹奖", "1970", "38"), award_line(W, "沃尔夫奖", "1992", "60")]),
    "deligneslide":   make_cross_box([award_line(F, "菲尔兹奖", "1978", "33"), award_line(W, "沃尔夫奖", "2008", "64")]),
    "margulisslide":  make_cross_box([award_line(F, "菲尔兹奖", "1978", "32"), award_line(W, "沃尔夫奖", "2005", "59")]),
    # Fields only
    "atiyahslide":    make_cross_box([award_line(F, "菲尔兹奖", "1966", "37")]),
    "faltingsslide":  make_cross_box([award_line(F, "菲尔兹奖", "1986", "32")]),
    # Wolf only
    "laxslide":         make_cross_box([award_line(W, "沃尔夫奖", "1987", "61")]),
    "carlesonslide":    make_cross_box([award_line(W, "沃尔夫奖", "1992", "64")]),
    "titsslide":        make_cross_box([award_line(W, "沃尔夫奖", "1993", "63")]),
    "gromovslide":      make_cross_box([award_line(W, "沃尔夫奖", "1993", "50")]),
    "tateslide":        make_cross_box([award_line(W, "沃尔夫奖", "2002", "77")]),
    "sinaislide":       make_cross_box([award_line(W, "沃尔夫奖", "1996", "61")]),
    "wilesslide":       make_cross_box([award_line(W, "沃尔夫奖", "1995", "42")]),
    "langlandsslide":   make_cross_box([award_line(W, "沃尔夫奖", "1995", "59")]),
    "furstenbergslide": make_cross_box([award_line(W, "沃尔夫奖", "2006", "71")]),
    "lovaszslide":      make_cross_box([award_line(W, "沃尔夫奖", "1999", "51")]),
    "sullivanslide":    make_cross_box([award_line(W, "沃尔夫奖", "2010", "69")]),
    "caffarellislide":  make_cross_box([award_line(W, "沃尔夫奖", "2012", "64")]),
    # Chern only
    "nirenbergslide":   make_cross_box([award_line(C, "陈省身奖章", "2010", "85")]),
    "kashiwaraslide":   make_cross_box([award_line(C, "陈省身奖章", "2018", "71")]),
    # Nobel Prize in Economics — John Nash
    "nashslide":        make_cross_box([award_line(N, "诺贝尔经济学奖", "1994", "66")]),
}

# Step 4: for each targeted slide, set \crosscontent right after \newcommand{\xslide}{
# The macro body starts with \personslide; prepend the \def so it runs at expansion time.
updated = 0
for slide, box in CROSS.items():
    marker = r'\newcommand{\%s}{\personslide' % slide
    if marker not in content:
        print(f"  MISS {slide}")
        continue
    # single-line \def (no raw newlines) so it stays valid inside the macro body
    box_oneline = ' '.join(box.split('\n'))
    replacement = r'\newcommand{\%s}{%s\personslide' % (slide, box_oneline)
    content = content.replace(marker, replacement, 1)
    updated += 1
    print(f"  ok {slide}")
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"\nDone! {updated} slides updated with cross-awards.")
