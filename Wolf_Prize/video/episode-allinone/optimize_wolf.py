#!/usr/bin/env python3
"""
Optimize wolf_prize_allinone_zh.tex:
1. Cover slide: new title, no serial numbers, clean tags
2. Chapter dividers: 第X集 → Part II–XII
3. Add (享年XX岁) for deceased laureates
4. Add cross-award boxes for Wolf winners with Fields/Abel/Chern
5. Clean up section comments
"""

import re

path = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/wolf_prize_allinone_zh.tex"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# ═══════════════════════════════════════
# 1. COVER SLIDE
# ═══════════════════════════════════════
old_title = r'{沃尔夫数学奖人物谱系}'
new_title = r'{沃尔夫数学奖全景录 —— 从 Leray 到 Sullivan · Alon · Shamir}'
content = content.replace(old_title, new_title)
changes += 1

old_subtitle = r'{Wolf Prize in Mathematics\enspace·\enspace 得主合集}'
new_subtitle = r'{Wolf Prize in Mathematics\enspace·\enspace 沃尔夫数学奖得主全传}'
content = content.replace(old_subtitle, new_subtitle)
changes += 1

old_desc = r'{第 2 – 12 集\enspace|\enspace 按主题分卷的人物谱系}'
new_desc = r'{按主题分卷\enspace·\enspace 兼录菲尔兹·阿贝尔双料/大满贯得主}'
content = content.replace(old_desc, new_desc)
changes += 1

old_tags = r"""      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (-5.6,0.34) {02·代数几何基础};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (-2.95,0.34) {03·复分析与PDE};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (-0.5,0.34) {04·应用与小波};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (1.85,0.34) {05·概率};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (4.5,0.34) {06·拓扑革命};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (-5.35,-0.36) {07·微分几何};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (-2.85,-0.36) {08·数论·Langlands};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (0.05,-0.36) {09·Hodge与表示};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (2.5,-0.36) {10·群与组合};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (4.85,-0.36) {11·动力系统};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (6.15,0.34) {12·泛函·逻辑};"""

new_tags = r"""      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (-5.6,0.34) {代数几何基础};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (-2.95,0.34) {复分析与PDE};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (-0.5,0.34) {应用与小波};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (1.85,0.34) {概率};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (4.5,0.34) {拓扑革命};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (-5.35,-0.36) {微分几何};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (-2.85,-0.36) {数论·Langlands};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (0.05,-0.36) {Hodge与表示};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (2.5,-0.36) {群与组合};
      \node[t, fill=coveraccent!14, text=coveraccent!58!black] at (4.85,-0.36) {动力系统};
      \node[t, fill=coverprimary!10, text=coverprimary!85!black] at (6.15,0.34) {泛函·逻辑};"""

content = content.replace(old_tags, new_tags)
changes += 1

# ═══════════════════════════════════════
# 2. CHAPTER DIVIDERS: 第X集 → Part II-XII
# ═══════════════════════════════════════
roman = {2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII'}
for n in range(2, 13):
    content = content.replace(r'\chapterdivider{第' + str(n) + '集}', r'\chapterdivider{Part ' + roman[n] + '}')
changes += 11

# ═══════════════════════════════════════
# 3. ADD (享年XX岁)
# ═══════════════════════════════════════
def add_age(m):
    birth, death = int(m.group(1)), int(m.group(2))
    return '{' + str(birth) + '--' + str(death) + '（享年' + str(death - birth) + '岁）}'
content, n_age = re.subn(r'\{(\d{4})--(\d{4})\}', add_age, content)
changes += n_age
print(f"✓ Added 享年 for {n_age} deceased laureates")

# ═══════════════════════════════════════
# 4. PREAMBLE: add amssymb, \def\crosscontent{}
# ═══════════════════════════════════════
content = content.replace(
    r'\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{fontawesome5}\usetikzlibrary{positioning,calc,arrows.meta,shadows}',
    r'\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{fontawesome5}\usepackage{amssymb}\usetikzlibrary{positioning,calc,arrows.meta,shadows}\def\crosscontent{}',
)
changes += 1

# Add \crosscontent into personslide macro (single line)
# Insert after greenpanel box: }};\end{tikzpicture}\end{column} → }};\end{tikzpicture}\crosscontent\end{column}
old_person_mid = r'}};\end{tikzpicture}\end{column}\begin{column}{0.48\textwidth}'
new_person_mid = r'}};\end{tikzpicture}\crosscontent\end{column}\begin{column}{0.48\textwidth}'
content = content.replace(old_person_mid, new_person_mid, 1)  # only first occurrence (macro def)
changes += 1

# Add reset at end of personslide: };\end{tikzpicture}\end{column}\end{columns}\end{frame}}
old_person_end = r'};\end{tikzpicture}\end{column}\end{columns}\end{frame}}'
new_person_end = r'};\end{tikzpicture}\end{column}\end{columns}\gdef\crosscontent{}\end{frame}}'
content = content.replace(old_person_end, new_person_end, 1)
changes += 1

# ═══════════════════════════════════════
# 5. CLEAN COMMENTS
# ═══════════════════════════════════════
content = re.sub(r'% ===== [^=]*得主宏[^=]*=====', '% ===== 得主宏 =====', content)
changes += 1

# ═══════════════════════════════════════
# 6. CROSS-AWARD BOXES
# ═══════════════════════════════════════
lines = content.split('\n')

def make_cross_box(lines_list):
    inner = r'\\[1.5pt]'.join(lines_list)
    return (r'\def\crosscontent{\vspace{3pt}' + '\n'
          + r'  \begin{tikzpicture}' + '\n'
          + r'    \node[draw=coveraccent!45, fill=panel!60, rounded corners=3pt, inner xsep=5pt, inner ysep=4pt, text width=3.8cm, align=left] {' + '\n'
          + r'      ' + inner + '\n'
          + r'    };' + '\n'
          + r'  \end{tikzpicture}}')

def aline(sym, name, yr, age):
    return r'{\fontsize{6}{7}\selectfont\bfseries\color{coveraccent!65!black} ' + sym + ' ' + name + r'}\enspace{\fontsize{6}{7}\selectfont\color{coverdark!80} ' + yr + '（' + age + '岁）}'

# Name-map: {English Name} → cross-award content
NAME_TO_CROSS = {}

# F+W+A → show Fields & Abel
for name, f_yr, f_age, a_yr, a_age in [
    ("Jean-Pierre Serre", "1954", "27", "2003", "77"),
    ("John Milnor", "1962", "31", "2011", "80"),
    ("John G. Thompson", "1970", "39", "2008", "76"),
    ("Pierre Deligne", "1978", "34", "2013", "69"),
    ("Grigory Margulis", "1978", "32", "2020", "74"),
]:
    NAME_TO_CROSS[name] = make_cross_box([
        aline(r"$\blacklozenge$", "菲尔兹奖", f_yr, f_age),
        aline(r"$\blacktriangle$", "阿贝尔奖", a_yr, a_age),
    ])

# F+W → show Fields
for name, yr, age in [
    ("Lars Ahlfors", "1936", "29"),
    ("Atle Selberg", "1950", "33"),
    ("Kunihiko Kodaira", "1954", "39"),
    ("Lars Hörmander", "1962", "31"),
    ("Stephen Smale", "1966", "36"),
    ("Sergei Novikov", "1970", "32"),
    ("David Mumford", "1974", "37"),
    ("Charles Fefferman", "1978", "29"),
    ("Shing-Tung Yau", "1982", "33"),
    ("Simon Donaldson", "1986", "28"),
    ("Vladimir Drinfeld", "1990", "36"),
]:
    NAME_TO_CROSS[name] = make_cross_box([aline(r"$\blacklozenge$", "菲尔兹奖", yr, age)])

# W+A → show Abel
for name, yr, age in [
    ("Peter Lax", "2005", "79"),
    ("Lennart Carleson", "2006", "78"),
    ("Jacques Tits", "2008", "78"),
    ("Mikhail Gromov", "2009", "65"),
    ("Andrew Wiles", "2016", "63"),
    ("Robert Langlands", "2018", "82"),
    ("Yakov Sinai", "2014", "79"),
    ("László Lovász", "2021", "73"),
    ("John Tate", "2010", "85"),
    ("Hillel Furstenberg", "2020", "85"),
    ("Dennis Sullivan", "2022", "81"),
    ("Luis Caffarelli", "2023", "75"),
]:
    NAME_TO_CROSS[name] = make_cross_box([aline(r"$\blacktriangle$", "阿贝尔奖", yr, age)])

# W+C → show Chern
NAME_TO_CROSS["Phillip Griffiths"] = make_cross_box([aline(r"$\blacksquare$", "陈省身奖章", "2014", "76")])

# ── Insert before \personslide calls by matching names ──
# Strategy: scan for \personslide{Name}... pattern, look up Name, insert \def before
PERSON_RE = re.compile(r'^\s*\\personslide\s*$')
PERSONA_RE = re.compile(r'^\s*\\personslideA\s*$')
NEWCMD_RE = re.compile(r'\\newcommand\{\\(\w+slide)\}')

inserted = 0
i = 0
while i < len(lines):
    # Case A: \newcommand{\xxxslide}{ ... \personslideA ... }
    m_cmd = NEWCMD_RE.search(lines[i])
    if m_cmd and m_cmd.group(1) != 'personslide':
        # Find the \personslide or \personslideA call within this command (next 15 lines)
        for j in range(i+1, min(i+20, len(lines))):
            if '\\personslide' in lines[j] and lines[j].strip().startswith('\\personslide'):
                # Extract name from the NEXT line
                name_line = lines[j+1].strip().strip('{}')
                if name_line in NAME_TO_CROSS:
                    indent = lines[j][:len(lines[j]) - len(lines[j].lstrip())]
                    lines.insert(j, indent + NAME_TO_CROSS[name_line])
                    inserted += 1
                    i += 1  # account for insertion
                    print(f"  ✓ {name_line}")
                break
    i += 1

# Case B: inline \personslide calls (not inside \newcommand)
i = 0
while i < len(lines):
    stripped = lines[i].strip()
    if stripped == '\\personslide':
        # Check if this is inside a \newcommand (skip if preceded by \newcommand)
        is_in_newcmd = False
        for k in range(max(0, i-20), i):
            if '\\newcommand' in lines[k]:
                is_in_newcmd = True
                # But we already handled those above, so only skip if it was actually found
                # Check if the line above was a cross-award insertion
                if i > 0 and '\\def\\crosscontent' in lines[i-1]:
                    is_in_newcmd = True
                break
        if not is_in_newcmd:
            name_line = lines[i+1].strip().strip('{}')
            if name_line in NAME_TO_CROSS:
                indent = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
                lines.insert(i, indent + NAME_TO_CROSS[name_line])
                inserted += 1
                i += 1
                print(f"  ✓ {name_line} (inline)")
    i += 1

content = '\n'.join(lines)
changes += inserted
print(f"✓ Cross-awards added for {inserted} slides")

# ── Write ──
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n═══ DONE: {changes} changes made ═══")