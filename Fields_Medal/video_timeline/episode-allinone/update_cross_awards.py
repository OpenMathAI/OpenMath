#!/usr/bin/env python3
"""
Add cross-award boxes to Fields Medal laureate slides.
Strategy: use global \crosscontent command, set by each slide before \personslide.
"""
import re

path = "/Users/ericksun/workspace/codebuddy/math/Fields_Medal/video_timeline/episode-allinone/fields_medal_allinone_zh.tex"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Add \def\crosscontent{} into preamble
content = content.replace(
    r'\definecolor{graypanel}{RGB}{243,246,250}',
    r'\definecolor{graypanel}{RGB}{243,246,250}\def\crosscontent{}',
)

# Step 2: Modify \personslide macro to render \crosscontent and reset
old_macro = r"""\newcommand{\personslide}[9]{%
\begin{frame}
\plainbar
\vspace{-0.45cm}
\begin{center}
  {\fontsize{22}{26}\selectfont\bfseries\color{coverdark} #1}\\[2pt]
  {\fontsize{9.5}{11.5}\selectfont\color{muteddark} #2}
\end{center}
\vspace{0.1cm}
\begin{columns}[c]
\begin{column}{0.22\textwidth}
  \centering
  \begin{tikzpicture}
    \node[draw=coverprimary!28, line width=0.7pt, fill=white, rounded corners=3pt, inner sep=2.5pt, drop shadow={shadow xshift=0.5pt, shadow yshift=-0.5pt, opacity=0.12}] {
      \includegraphics[width=2.2cm,height=2.7cm,keepaspectratio]{#3}
    };
  \end{tikzpicture}
  {\par\vspace{1pt}\fontsize{6.2}{7.2}\selectfont\color{covermuted} #4\par}
\end{column}
\begin{column}{0.28\textwidth}
  \begin{tikzpicture}
    \node[fill=goldpanel, rounded corners=4pt, inner xsep=6pt, inner ysep=5pt, text width=3.8cm, align=left] {
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 获奖}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #5}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 生卒}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #6}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 国别}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #7}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{tikzpicture}
    \node[draw=coverprimary!35, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, anchor=north west] at (0,0) {
      {\fontsize{8.2}{10}\selectfont\bfseries\color{coverprimary!82!black} 核心贡献}\\[3pt]
      {\fontsize{7}{8.5}\selectfont\color{coverdark!84} #9}
    };
  \end{tikzpicture}
\end{column}
\end{columns}
\end{frame}
}"""

new_macro = r"""\newcommand{\personslide}[9]{%
\begin{frame}
\plainbar
\vspace{-0.45cm}
\begin{center}
  {\fontsize{22}{26}\selectfont\bfseries\color{coverdark} #1}\\[2pt]
  {\fontsize{9.5}{11.5}\selectfont\color{muteddark} #2}
\end{center}
\vspace{0.1cm}
\begin{columns}[c]
\begin{column}{0.22\textwidth}
  \centering
  \begin{tikzpicture}
    \node[draw=coverprimary!28, line width=0.7pt, fill=white, rounded corners=3pt, inner sep=2.5pt, drop shadow={shadow xshift=0.5pt, shadow yshift=-0.5pt, opacity=0.12}] {
      \includegraphics[width=2.2cm,height=2.7cm,keepaspectratio]{#3}
    };
  \end{tikzpicture}
  {\par\vspace{1pt}\fontsize{6.2}{7.2}\selectfont\color{covermuted} #4\par}
\end{column}
\begin{column}{0.28\textwidth}
  \begin{tikzpicture}
    \node[fill=goldpanel, rounded corners=4pt, inner xsep=6pt, inner ysep=5pt, text width=3.8cm, align=left] {
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 获奖}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #5}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 生卒}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #6}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 国别}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #7}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{covergold!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
  \crosscontent
\end{column}
\begin{column}{0.48\textwidth}
  \begin{tikzpicture}
    \node[draw=coverprimary!35, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, anchor=north west] at (0,0) {
      {\fontsize{8.2}{10}\selectfont\bfseries\color{coverprimary!82!black} 核心贡献}\\[3pt]
      {\fontsize{7}{8.5}\selectfont\color{coverdark!84} #9}
    };
  \end{tikzpicture}
\end{column}
\end{columns}
\gdef\crosscontent{}
\end{frame}
}"""

if old_macro not in content:
    print("ERROR: old macro not found!")
else:
    content = content.replace(old_macro, new_macro, 1)
    print("✓ Macro updated")

# Step 3: Add \def\crosscontent{...} before \personslide in cross-award slides
# Build cross-award content per slide
def make_cross_box(lines):
    """Wrap list of award lines into a tikzpicture box."""
    inner = r'\\[1.5pt]'.join(lines)
    return r"""\def\crosscontent{\vspace{4pt}
  \begin{tikzpicture}
    \node[draw=covergold!45, fill=panel!60, rounded corners=3pt, inner xsep=5pt, inner ysep=4pt, text width=3.8cm, align=left] {
      """ + inner + r"""
    };
  \end{tikzpicture}}"""

def award_line(symbol, name, year, age):
    return r"""{\fontsize{6}{7}\selectfont\bfseries\color{covergold!70!black} """ + symbol + ' ' + name + r"""}\enspace{\fontsize{6}{7}\selectfont\color{coverdark!80} """ + year + r"""（""" + age + """岁）}"""

CROSS = {
    # ★★★ F+W+A
    "serreslide": make_cross_box([
        award_line(r"$\bigstar$", "沃尔夫奖", "2000", "74"),
        award_line(r"$\blacktriangle$", "阿贝尔奖", "2003", "77"),
    ]),
    "milnorslide": make_cross_box([
        award_line(r"$\bigstar$", "沃尔夫奖", "1989", "58"),
        award_line(r"$\blacktriangle$", "阿贝尔奖", "2011", "80"),
    ]),
    "thompsonslide": make_cross_box([
        award_line(r"$\bigstar$", "沃尔夫奖", "1992", "60"),
        award_line(r"$\blacktriangle$", "阿贝尔奖", "2008", "76"),
    ]),
    "deligneslide": make_cross_box([
        award_line(r"$\bigstar$", "沃尔夫奖", "2008", "64"),
        award_line(r"$\blacktriangle$", "阿贝尔奖", "2013", "69"),
    ]),
    "margulisslide": make_cross_box([
        award_line(r"$\bigstar$", "沃尔夫奖", "2005", "59"),
        award_line(r"$\blacktriangle$", "阿贝尔奖", "2020", "74"),
    ]),
}

# ★★ F+W
for name, year, age in [
    ("ahlforsslide", "1981", "74"), ("selbergslide", "1986", "69"),
    ("kodairaslide", "1984", "69"), ("hormanderslide", "1988", "57"),
    ("smaleslide", "2006", "76"), ("novikovslide", "2005", "67"),
    ("mumfordslide", "2008", "71"), ("feffermanslide", "2017", "68"),
    ("yauslide", "2010", "61"), ("donaldsonslide", "2020", "63"),
    ("drinfeldslide", "2018", "64"),
]:
    CROSS[name] = make_cross_box([award_line(r"$\bigstar$", "沃尔夫奖", year, age)])

# ★★ F+A
CROSS["atiyahslide"] = make_cross_box([award_line(r"$\blacktriangle$", "阿贝尔奖", "2004", "75")])
CROSS["faltingsslide"] = make_cross_box([award_line(r"$\blacktriangle$", "阿贝尔奖", "2026", "72")])

# Now insert \def\crosscontent{...} before each \personslide call in cross-award slides
lines = content.split('\n')
updated = 0

for i, line in enumerate(lines):
    m = re.match(r'\\newcommand\{\\(\w+slide)\}', line)
    if m and m.group(1) in CROSS:
        slide_name = m.group(1)
        cross_def = CROSS[slide_name]
        # Find the \personslide line within this slide definition
        j = i + 1
        while j < len(lines) and j < i + 20:
            if r'\personslide' in lines[j]:
                # Insert \def\crosscontent before \personslide
                indent = lines[j][:len(lines[j]) - len(lines[j].lstrip())]
                lines.insert(j, indent + cross_def)
                updated += 1
                print(f"  ✓ {slide_name}")
                break
            j += 1

content = '\n'.join(lines)

# Step 4: Add amssymb for the symbols
content = content.replace(
    r'\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{adjustbox}\usepackage{fontawesome5}',
    r'\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{adjustbox}\usepackage{fontawesome5}\usepackage{amssymb}',
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone! {updated} slides updated with cross-awards.")