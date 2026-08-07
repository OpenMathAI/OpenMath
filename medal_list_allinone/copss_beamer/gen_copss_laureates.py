#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate COPSS laureates compact beamer (medal_list_allinone/copss_beamer).
Mirrors abel_beamer/abel_prize_laureates_beamer.tex format.
Data: ../COPSS/video/gen_copss.py (46 laureates) + Wikipedia Awards."""
import os, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
COPSS_ALLINONE = os.path.join(HERE, "..", "..", "COPSS", "video", "episode-allinone")
spec = importlib.util.spec_from_file_location("g",
    os.path.join(HERE, "..", "..", "COPSS", "video", "gen_copss.py"))
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

# Chinese short name from subtitle ("中文名 \enspace·\enspace note" -> "中文名")
def cn_of(subtitle):
    return subtitle.split("\\enspace")[0].strip()

# Notable cross-award honors (from Wikipedia Awards fields, verified 2026-08-07)
HONORS = {
    "Peter J. Bickel":      "MacArthur 1984",
    "Stephen Fienberg":     "R.A. Fisher Lectureship",
    "James O. Berger":      "NAS 2003 · R.A. Fisher Lectureship",
    "Ross L. Prentice":     "R.A. Fisher Lectureship 2008",
    "C. F. Jeff Wu":        "Shewhart Medal · R.A. Fisher Lectureship",
    "Raymond J. Carroll":   "R.A. Fisher Lectureship 2002",
    "Peter Hall":           "Guy Medal 2011 · 澳桂冠学者",
    "Peter McCullagh":      "Guy Medal 金2026 · FRS 1994",
    "Bernard Silverman":    "Guy Medal · IMO 金牌",
    "David L. Donoho":      "★ Gauss Prize 2018 · Shaw Prize 2013",
    "Iain M. Johnstone":    "Guy Medal 银2010",
    "Jianqing Fan":         "Guy Medal 银2014 · Guggenheim",
    "Rina Foygel Barber":   "MacArthur 2024",
}

EP_RANGES = [
    ("ep01", "1981–1990", "奠基年代"),
    ("ep02", "1991–2000", "贝叶斯复兴与计算革命"),
    ("ep03", "2001–2010", "生物统计爆发与华人崛起"),
    ("ep04", "2011–2020", "高维统计与机器学习融合"),
    ("ep05", "2021–2026", "数据科学、AI 与贝叶斯革新"),
]

HEADER = r"""% COPSS Presidents' Award — Laureates (1981–2026)
% Compact tabular layout mirroring abel_prize_laureates_beamer.tex
% 46 laureates, one per year. Cross-award honors annotated in Field column.
% Compile with: xelatex copss_laureates_beamer.tex
\documentclass[aspectratio=169,9pt]{beamer}

\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{%
  \hfill{\tiny\color{mutedgray}\insertframenumber/\inserttotalframenumber}\hspace*{6pt}\vspace{4pt}%
}
\newcommand{\framesubject}{}
\setbeamertemplate{frametitle}{%
  \vspace{8pt}%
  \centering
  {\large\bfseries\color{copssclr}COPSS 会长奖 · \insertframetitle}\\[3pt]
  \textcolor{copssbg}{\rule{0.95\textwidth}{0.6pt}}%
  \vspace{-6pt}%
}

\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold]
\setCJKsansfont{PingFang SC}
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\setsansfont{Helvetica Neue}
\usepackage{booktabs}\usepackage{array}\usepackage{tikz}\usepackage{amssymb}
\usepackage{colortbl}\usepackage{graphicx}\usepackage{fontawesome5}

\definecolor{headerblue}{RGB}{41,65,122}
\definecolor{yearcolor}{RGB}{150,40,90}
\definecolor{fieldcolor}{RGB}{30,100,60}
\definecolor{mutedgray}{RGB}{100,100,100}
\definecolor{slidebg}{RGB}{250,252,255}
\definecolor{copssclr}{RGB}{33,102,172}     % 统计蓝
\definecolor{copssbg}{RGB}{222,235,250}     % 浅蓝底
\definecolor{fieldsclr}{RGB}{41,65,122}
\definecolor{abelclr}{RGB}{150,40,90}
\definecolor{wolfclr}{RGB}{180,120,0}
\definecolor{chernclr}{RGB}{15,110,92}
\definecolor{nobelclr}{RGB}{176,141,45}
\setbeamercolor{background canvas}{bg=slidebg}

% Award badges (cross-award annotation)
\newcommand{\fieldsbadge}{\textsuperscript{\normalfont\tiny\color{fieldsclr}$\blacklozenge$\kern-0.5pt F}}
\newcommand{\wolfbadge}{\textsuperscript{\normalfont\tiny\color{wolfclr}$\bigstar$\kern-0.5pt W}}
\newcommand{\chernbadge}{\textsuperscript{\normalfont\tiny\color{chernclr}$\blacksquare$\kern-0.5pt C}}
\newcommand{\gaussbadge}{\textsuperscript{\normalfont\tiny\color{copssclr}$\blacklozenge$\kern-0.5pt G}}

% Chinese name suffix
\newcommand{\cn}[1]{\newline{\scriptsize\color{mutedgray}#1}}
% #1=Name(+badges) #2=Year #3=Birth-Death #4=Nationality #5=Institution #6=Field
\newcommand{\lrow}[6]{%
  {\bfseries\color{copssclr}#1} & {\color{yearcolor}#2} & {#3} & {#4} & {\scriptsize #5} & {\scriptsize\color{fieldcolor}#6} \\[2.5pt]
}

\begin{document}
"""

COVER = r"""\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[copssclr!2] (current page.north west) rectangle (current page.south east);
  \fill[copssclr!6] (current page.north west) ++(1.55,-1.35) circle (2.45cm);
  \fill[copssclr!8] (current page.south east) ++(-1.9,1.45) circle (2.70cm);
  \node[anchor=center, font=\fontsize{18}{24}\selectfont\bfseries, text=copssclr]
    at ([yshift=2.80cm]current page.center) {COPSS 会长奖：统计学界的最高礼赞（1981–2026）};
  \node[anchor=center, font=\fontsize{11}{15}\selectfont, text=mutedgray]
    at ([yshift=1.60cm]current page.center) {COPSS Presidents' Award（考普斯会长奖）\enspace·\enspace 全 46 位得主};
  \draw[copssclr!50, line width=1.2pt] ([yshift=0.90cm, xshift=-5.0cm]current page.center)
    -- ([yshift=0.90cm, xshift=5.0cm]current page.center);
  \node[anchor=center, font=\fontsize{9}{12}\selectfont\bfseries, text=mutedgray]
    at ([yshift=0.20cm]current page.center) {与菲尔兹·沃尔夫·阿贝尔·陈省身奖无交叉；Donoho 另获高斯奖 2018 与邵逸夫奖 2013};
  \node[anchor=center] at ([yshift=-1.90cm]current page.center) {
    \begin{tikzpicture}[scale=1]
"""

GRID_COLS, GRID_ROWS = 16, 3
W, H, GAP = 0.60, 0.70, 0.05
TOTAL_W = (GRID_COLS - 1) * (W + GAP)
START_X = -TOTAL_W / 2
START_Y = ((GRID_ROWS - 1) * (H + GAP)) / 2


def photo_grid(all_people, img_dir="images"):
    lines = []
    for i, p in enumerate(all_people):
        name, subtitle, year, life, country, inst, tag, contrib, img, credit = p
        base = g.cmd_name(name)
        ext = ".jpg"
        cand = os.path.join(HERE, img_dir, base + ext)
        if not os.path.exists(cand):
            cand = os.path.join(HERE, img_dir, base + ".png")
            ext = ".png"
        r, c = i // GRID_COLS, i % GRID_COLS
        x = START_X + c * (W + GAP)
        y = START_Y - r * (H + GAP)
        lines.append('      \\node[inner sep=0pt] at (%.2f,%.2f) {' % (x, y))
        lines.append('        \\includegraphics[width=%scm,height=%scm,keepaspectratio]{%s/%s%s}' % (W, H, img_dir, base, ext))
        lines.append('      };')
    return "\n".join(lines)


def make_table_frame(ep_key, rng, subject):
    people = g.PEOPLE[ep_key]
    rows = []
    for p in people:
        name, subtitle, year, life, country, inst, tag, contrib, img, credit = p
        cn = cn_of(subtitle)
        age = g.compute_age(year, life)
        year_str = "%d（%s）" % (year, age) if age else str(year)
        country_s = country.split("（")[0].replace("&", "\\&")
        # simplify long institution
        inst_s = (inst.replace("University of ", "U of ").replace("University", "Univ.")
                  .replace("&", "\\&"))
        badge = "\\gaussbadge" if name == "David L. Donoho" else ""
        field = tag.replace("&", "\\&")
        if name in HONORS:
            field += "；亦获 %s" % HONORS[name].replace("&", "\\&")
        rows.append("\\lrow{%s%s\\cn{%s}}{%s}{%s}{%s}{%s}{%s}" % (
            name, badge, cn, year_str, life, country_s, inst_s, field))
    return r"""\begin{frame}{%s}
\vspace{-2pt}
\centering
\scriptsize
\resizebox{\textwidth}{!}{\begin{tabular}{@{}
  >{\raggedright}m{2.55cm}
  >{\centering}m{2.45cm}
  >{\centering}m{2.10cm}
  >{\raggedright}m{1.60cm}
  >{\raggedright}m{2.00cm}
  >{\raggedright\arraybackslash}m{2.40cm}
@{}}
\toprule
\rowcolor{copssbg}
\textbf{姓名} & \textbf{获奖} & \textbf{生卒} & \textbf{国籍} & \textbf{机构} & \textbf{研究领域} \\
\midrule
%s
\bottomrule
\end{tabular}}
\vspace{4pt}
\end{frame}
""" % (rng, "\n".join(rows))


def sync_photos(all_people):
    """Copy laureate photos into ./images using canonical cmd_name filenames."""
    os.makedirs(os.path.join(HERE, "images"), exist_ok=True)
    for p in all_people:
        name, *_ = p
        img_rel = g.resolve_img(p, "episode-allinone")  # e.g. images/bickel.jpg
        src = os.path.join(COPSS_ALLINONE, img_rel)
        ext = os.path.splitext(img_rel)[1]
        dst = os.path.join(HERE, "images", g.cmd_name(name) + ext)
        if os.path.exists(src):
            shutil.copy(src, dst)
    print("photos synced:", len(os.listdir(os.path.join(HERE, "images"))), "files")


def main():
    all_people = []
    for ep_key, rng, subject in EP_RANGES:
        all_people.extend(g.PEOPLE[ep_key])
    sync_photos(all_people)

    out = [HEADER]
    # cover
    cover = COVER + photo_grid(all_people) + r"""
    \end{tikzpicture}
  };
  \node[anchor=south, font=\scriptsize, text=mutedgray]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace COPSS Presidents' Award\enspace|\enspace 1981–2026\enspace|\enspace 全 46 位得主};
\end{tikzpicture}
\end{frame}
"""
    out.append(cover)
    # table frames (define framesubject BEFORE each frame so the title shows it)
    for ep_key, rng, subject in EP_RANGES:
        out.append("\\def\\framesubject{%s}\n" % subject)
        out.append(make_table_frame(ep_key, rng, subject))
    # cross-award summary frame: no subject, large text, compact layout
    out.append("\\def\\framesubject{}\n")
    out.append(r"""\begin{frame}{交叉获奖与荣誉}
\vspace{0.20cm}
\begin{center}
{\Large\bfseries\color{copssclr} COPSS 得主与四大数学奖交叉情况}
\end{center}
\vspace{0.25cm}
{\large
\begin{itemize}\setlength\itemsep{14pt}\setlength\leftmargin{0.6cm}
  \item[\textcolor{fieldsclr}{$\blacklozenge$}] \textbf{菲尔兹 / 沃尔夫 / 阿贝尔 / 陈省身奖章}：46 位 COPSS 得主中 \textbf{无人} 同时获得（统计学与纯数学领域不同，2026 年为止）。
  \item[\textcolor{wolfclr}{$\bigstar$}] \textbf{David L. Donoho（1994）}：另获 \textbf{IMU 高斯奖 2018}（应用数学最高荣誉）与 \textbf{邵逸夫奖 2013}——COPSS 得主中与数学界奖项交叉最显著者。
  \item[\textcolor{copssclr}{$\blacklozenge$}] \textbf{统计领域荣誉交叉}：R.A. Fisher Lectureship（9 人）；Guy 奖章（6 人）；MacArthur 天才奖（Bickel 1984·Barber 2024）。
\end{itemize}
}
\end{frame}
""")
    out.append(r"\end{document}" + "\n")
    path = os.path.join(HERE, "copss_laureates_beamer.tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", path, "|", len(all_people), "laureates")


if __name__ == "__main__":
    main()
