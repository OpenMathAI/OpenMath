#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate turing_prize_laureates_beamer.tex (1966–2025, 81 laureates)
mirroring abel_prize_laureates_beamer.tex layout:
  cover (photo grid) + per-year-range tabular frames + cross-award summary.

Cross-award badges are defined per award with brand colors, appended after
laureate names (identical rule set to turing/gen_turing.py AWARD_ICONS).
"""
import os
import re
import sys
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
TURING = os.path.abspath(os.path.join(HERE, "..", "..", "turing"))
sys.path.insert(0, TURING)
import gen_turing as gt  # DATA / HONORS / cmd_name / esc / badges_for / AWARD_ICONS

IMG_SRC = os.path.join(TURING, "video", "episode-allinone", "images")
IMG_DST = os.path.join(HERE, "images")

MAIN = "turing_prize_laureates_beamer"
TURINGCLR = "coverprimary"
TURINGBG = "turingbg"

# 每帧人数（表格行数；照片行一张大图）
ROWS_PER_FRAME = 5

# 徽标命令：符号+字母+品牌色+全称（与 gen_turing AWARD_ICONS 一致）
BADGE_DEFS = {
    "诺贝尔":      (r"\faIcon{award}",     "nobelclr",      "N", "诺贝尔奖"),
    "京都":        (r"$\blacklozenge$",    "kyotoclr",      "K", "京都奖"),
    "沃尔夫":      (r"$\bigstar$",         "wolfclr",       "W", "沃尔夫奖"),
    "哥德尔":      (r"$\diamond$",         "godelclr",      "G", "哥德尔奖"),
    "阿贝尔":      (r"$\bigstar$",         "abelclr",       "A", "阿贝尔奖"),
    "香农":        (r"$\bigstar$",         "shannonclr",    "S", "IEEE 香农奖"),
    "日本国际":    (r"$\heartsuit$",       "japanclr",      "J", "日本国际奖"),
    "内万林纳":    (r"$\blacktriangle$",   "nevanclr",      "N", "内万林纳奖"),
    "EATCS":       (r"$\square$",          "eatcsclr",      "E", "EATCS 奖"),
    "马可尼":      (r"$\bullet$",          "marconiclr",    "M", "马可尼奖"),
    "冯":          (r"$\blacktriangle$",   "neumannclr",    "V", "IEEE 冯·诺依曼奖"),
    "千禧":        (r"$\blacklozenge$",    "millenniumclr", "T", "千禧科技奖"),
    "国家科学奖章": (r"$\spadesuit$",      "nsmclr",        "M", "美国国家科学奖章"),
    "科学院院士":   (r"$\blacksquare$",    "nasclr",        "N", "美国科学院院士"),
    "皇家学会院士": (r"$\checkmark$",       "frsclr",        "R", "英国皇家学会院士"),
    "加拿大总督":   (r"$\blacklozenge$",   "govclr",        "C", "加拿大总督奖"),
    "鲁梅哈特":     (r"$\diamondsuit$",    "rumelclr",      "R", "鲁梅哈特奖"),
}

COLORS = {
    "turingclr": "41,65,122",
    "turingbg": "225,235,252",
    "nobelclr": "176,141,45",
    "kyotoclr": "91,45,142",
    "wolfclr": "150,100,0",
    "godelclr": "30,142,142",
    "abelclr": "150,40,90",
    "shannonclr": "176,141,45",
    "japanclr": "176,58,46",
    "nevanclr": "30,100,60",
    "eatcsclr": "100,100,100",
    "marconiclr": "176,141,45",
    "neumannclr": "41,65,122",
    "millenniumclr": "176,58,46",
    "nsmclr": "41,65,122",
    "nasclr": "30,100,60",
    "frsclr": "176,141,45",
    "govclr": "100,100,100",
    "rumelclr": "30,100,60",
}


def all_people():
    people = []
    for ep, lst in gt.DATA.items():
        people.extend(lst)
    people.sort(key=lambda p: (p[2], p[0]))  # (year, name)
    return people


def badge_cmds(name):
    return gt.badges_for(name)


def short_institution(inst):
    return inst


def header():
    cols = "\n".join(
        "\\definecolor{%s}{RGB}{%s}" % (name, rgb)
        for name, rgb in COLORS.items())
    badges = "\n".join(
        "\\newcommand{\\%s}{\\textsuperscript{\\normalfont\\tiny\\color{%s}%s\\kern-0.5pt %s}}"
        % (cmd, color, sym, letter)
        for key, (sym, color, letter, _full) in BADGE_DEFS.items()
        for cmd in [_badge_cmd(key)])
    # 徽标命令名：key → badge 名（仅英文首字母+奖项缩写）
    return cols, badges


def _badge_cmd(key):
    m = {
        "诺贝尔": "nobelbadge", "京都": "kyotobadge", "沃尔夫": "wolfbadge",
        "哥德尔": "godelbadge", "阿贝尔": "abelbadge", "香农": "shannonbadge",
        "日本国际": "japanbadge", "内万林纳": "nevanlinnabadge", "EATCS": "eatcsbadge",
        "马可尼": "marconibadge", "冯": "neumannbadge", "千禧": "millenniumbadge",
        "国家科学奖章": "nsmbadge", "科学院院士": "nasbadge", "皇家学会院士": "frsbadge",
        "加拿大总督": "govbadge", "鲁梅哈特": "rumelhartbadge",
    }
    return m[key]


def badges_map():
    """key → \command 映射（与 gen_turing.badges_for 等价，改用本地徽标命令名）"""
    cmds = {}
    for key in BADGE_DEFS:
        cmds[key] = _badge_cmd(key)
    return cmds


def local_badges_for(name):
    """返回本地徽标命令串（用 turing_beamer 自己的徽标宏名）"""
    h = gt.HONORS.get(name, "")
    b = ""
    for key in BADGE_DEFS:
        if key in h:
            b += "\\" + _badge_cmd(key)
    return b


def cn(name):
    """中文名：从 DATA 中找"""
    for ep, lst in gt.DATA.items():
        for p in lst:
            if p[0] == name:
                return p[1]
    return ""


def life(name):
    for ep, lst in gt.DATA.items():
        for p in lst:
            if p[0] == name:
                return p[3]
    return ""


def country(name):
    for ep, lst in gt.DATA.items():
        for p in lst:
            if p[0] == name:
                return p[4]
    return ""


def inst(name):
    for ep, lst in gt.DATA.items():
        for p in lst:
            if p[0] == name:
                return p[5]
    return ""


def contrib(name):
    for ep, lst in gt.DATA.items():
        for p in lst:
            if p[0] == name:
                return p[6]
    return ""


def img_path(name):
    return os.path.join(IMG_DST, gt.cmd_name(name) + ".jpg")


def sync_images(people):
    os.makedirs(IMG_DST, exist_ok=True)
    n = 0
    for p in people:
        src = os.path.join(IMG_SRC, gt.cmd_name(p[0]) + ".jpg")
        dst = os.path.join(IMG_DST, gt.cmd_name(p[0]) + ".jpg")
        if os.path.exists(src) and os.path.getsize(src) > 0:
            if not (os.path.exists(dst) and os.path.getsize(dst) > 0) or \
               os.path.getsize(src) != os.path.getsize(dst):
                shutil.copy(src, dst)
            n += 1
    return n


def cover_slide(people):
    """封面：标题+副标题+说明+照片网格（12×7=84 容纳 81+3 空）"""
    rows = []
    ncols = 12
    W, H, GAP = 0.50, 0.55, 0.04
    total_w = (ncols - 1) * (W + GAP)
    start_x = -total_w / 2
    nrows = (len(people) + ncols - 1) // ncols
    total_h = (nrows - 1) * (H + GAP)
    start_y = total_h / 2
    for i, p in enumerate(people):
        r, c = i // ncols, i % ncols
        x = start_x + c * (W + GAP)
        y = start_y - r * (H + GAP)
        img = os.path.join("images", gt.cmd_name(p[0]) + ".jpg")
        rows.append("      \\node[inner sep=0pt, anchor=center] at (%.2f,%.2f) {\n"
                    "        \\includegraphics[width=%.2fcm,height=%.2fcm,keepaspectratio]{%s}\n"
                    "      };" % (x, y, W, H, img))
    grid = "\n".join(rows)
    return (r"""\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[turingclr!2] (current page.north west) rectangle (current page.south east);
  \fill[turingclr!6] (current page.north west) ++(1.55,-1.35) circle (2.45cm);
  \fill[turingclr!8] (current page.south east) ++(-1.9,1.45) circle (2.70cm);
  \node[anchor=center, font=\fontsize{18}{24}\selectfont\bfseries, text=turingclr]
    at ([yshift=3.30cm]current page.center) {ACM 图灵奖：计算机科学的最高荣誉（1966–2025）};
  \node[anchor=center, font=\fontsize{11}{15}\selectfont, text=mutedgray]
    at ([yshift=2.20cm]current page.center) {ACM Turing Award\enspace·\enspace 计算机界的诺贝尔奖\enspace·\enspace 全 81 位得主};
  \draw[turingclr!50, line width=1.2pt] ([yshift=1.60cm, xshift=-5.0cm]current page.center)
    -- ([yshift=1.60cm, xshift=5.0cm]current page.center);
  \node[anchor=center, font=\fontsize{7}{10}\selectfont\bfseries, text=mutedgray]
    at ([yshift=1.05cm]current page.center) {兼录诺贝尔·沃尔夫·京都·哥德尔·阿贝尔·香农·日本国际·内万林纳·马可尼等交叉得主};
  \node[anchor=center] at ([yshift=-1.40cm]current page.center) {
    \begin{tikzpicture}[scale=1]
%s
    \end{tikzpicture}
  };
  \node[anchor=south, font=\fontsize{6}{7}\selectfont, text=mutedgray]
    at ([yshift=0.25cm]current page.south) {\faIcon{desktop}\enspace Turing Award Laureates\enspace|\enspace ACM\enspace|\enspace 1966–2025\enspace|\enspace 60 届·81 人};
\end{tikzpicture}
\end{frame}
""" % grid)


def table_slide(title, subject, people):
    """一张表格帧：6 列 + 底部照片行"""
    rows = []
    for p in people:
        name, cnz, year, life_, cty, instt, contrib_ = p
        badges = local_badges_for(p[0])
        rows.append("  \\lrow{%s%s\\cn{%s}}{%d}{%s}{%s}{%s}{%s}" % (
            gt.esc(p[0]), badges, gt.esc(cnz), year, gt.esc(life_),
            gt.esc(cty), gt.esc(instt), gt.esc(contrib_)))
    table = "\n".join(rows)
    # 底部照片行
    photos = []
    n = len(people)
    total_w = 6.0  # 底部照片横排总宽
    step = total_w / (n - 1) if n > 1 else 0
    start_x = -total_w / 2
    for i, p in enumerate(people):
        x = start_x + i * step
        img = os.path.join("images", gt.cmd_name(p[0]) + ".jpg")
        photos.append("      \\node[inner sep=0pt] at (%.2f,0) {\n"
                      "        \\includegraphics[width=1.80cm,height=2.20cm,keepaspectratio]{%s}\n"
                      "      };" % (x, img))
    photos_tex = "\n".join(photos)
    return (r"""\def\framesubject{%s}
\begin{frame}{%s}
\vspace{-2pt}
\centering
\scriptsize
\begin{tabular}{@{}
  >{\raggedright}m{3.6cm}
  >{\centering}m{0.95cm}
  >{\centering}m{1.05cm}
  >{\raggedright}m{1.5cm}
  >{\raggedright}m{2.4cm}
  >{\raggedright\arraybackslash}m{2.6cm}
@{}}
\toprule
\rowcolor{turingbg}
\textbf{姓名} & \textbf{年份} & \textbf{生卒} & \textbf{国籍} & \textbf{机构} & \textbf{研究领域} \\
\midrule
%s
\bottomrule
\end{tabular}
\vspace{6pt}
  {\centering
  \begin{tikzpicture}
%s
  \end{tikzpicture}}
\end{frame}
""" % (subject, title, table, photos_tex))


def summary_slide(people):
    """总结帧：拆成 2 页（8+7），每页一列布局；奖项写全称。"""
    by_award = {}
    for p in people:
        h = gt.HONORS.get(p[0], "")
        for key in BADGE_DEFS:
            if key in h:
                by_award.setdefault(key, []).append(p[0])
    items = sorted(by_award.items(), key=lambda kv: -len(kv[1]))
    # 拆成 2 页：前 8 项一帧，后 7 项一帧
    page1 = items[:8]
    page2 = items[8:]

    def block_rows(block):
        """生成一列的 rows；y 步长按行数动态。"""
        rs = []
        y = 0.0
        for key, names in block:
            sym, color, _letter, full = BADGE_DEFS[key]
            def chunk(lst, n):
                return ['\\;·\\;'.join(lst[i:i+n]) for i in range(0, len(lst), n)]
            chunks = chunk(names, 5)
            names_txt = " \\\\ ".join(chunks)
            n_lines = len(chunks)
            y_step = max(0.55, 0.22 * n_lines + 0.10)
            # 左侧徽标盒（窄，3.5cm），右侧人名（占满列宽）
            rs.append(r"""  \node[fill=%s, rounded corners=4pt, text width=3.5cm, minimum height=0.55cm,
        inner sep=0pt, align=center, anchor=north west] at (-5.4,%.2f)
    {\fontsize{5.5}{6.5}\selectfont\bfseries\color{white}%s\;\; %s\;\; %d人};
  \node[anchor=north west, text width=8.0cm, align=left,
        font=\fontsize{5.5}{6.5}\selectfont, text=%s!70!black]
    at (-1.70,%.2f) {%s};""" % (
                color, y, sym, full, len(names),
                color, y, names_txt))
            y -= y_step
        return rs, y

    def page_block(rows, y_stat, subject):
        stats = r"""  \fill[turingbg, rounded corners=4pt] (-5.5,%.2f) rectangle (5.6,%.2f);
  \node[anchor=north, font=\fontsize{5.5}{7}\selectfont\bfseries, text=turingclr]
    at (-3.6,%.2f) {首届\;\; Alan J. Perlis\;(1966)};
  \node[anchor=north, font=\fontsize{5.5}{7}\selectfont\bfseries, text=turingclr]
    at (0.0,%.2f) {60 届\;\; 81 位得主};
  \node[anchor=north, font=\fontsize{5.5}{7}\selectfont\bfseries, text=turingclr]
    at (3.6,%.2f) {图灵+诺奖\;\; Simon\;·\;Hinton};""" % (
            y_stat - 0.5, y_stat, y_stat - 0.10, y_stat - 0.10, y_stat - 0.10)
        body = "\n".join(rows + [stats])
        return (r"""\def\framesubject{%s}
\begin{frame}{交叉奖项总览}
\vspace{-4pt}
\centering
\begin{tikzpicture}
%s
\end{tikzpicture}
\end{frame}
""" % (subject, body))

    rows1, y_after1 = block_rows(page1)
    page1_tex = page_block(rows1, y_after1 - 0.40,
                            "诺贝尔·沃尔夫·京都·哥德尔·阿贝尔·香农等交叉得主（I · 顶级交叉）")
    rows2, y_after2 = block_rows(page2)
    page2_tex = page_block(rows2, y_after2 - 0.40,
                            "（II · 其他重要荣誉）")
    return page1_tex + "\n" + page2_tex


def build():
    people = all_people()
    n_photos = sync_images(people)
    print("photos:", n_photos)

    color_defs, badge_defs = header()
    # badge 定义已生成
    frames = [cover_slide(people)]
    # 分年分组
    groups = []
    cur = []
    for p in people:
        cur.append(p)
        if len(cur) == ROWS_PER_FRAME:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    for gi, grp in enumerate(groups):
        y1 = grp[0][2]
        y2 = grp[-1][2]
        title = "%d–%d" % (y1, y2)
        subj = "·".join(gt.esc(p[6].split("，")[0][:14]) for p in grp)
        frames.append(table_slide(title, subj, grp))
    frames.append(summary_slide(people))

    # 徽标命令文本
    badge_cmds_tex = "\n".join(
        "\\newcommand{\\%s}{\\textsuperscript{\\normalfont\\tiny\\color{%s}%s\\kern-0.5pt %s}}"
        % (_badge_cmd(key), BADGE_DEFS[key][1], BADGE_DEFS[key][0], BADGE_DEFS[key][2])
        for key in BADGE_DEFS)

    tex = r"""% Turing Award — Laureates (1966–2025)
% Compact tabular layout mirroring abel_prize_laureates_beamer.tex
% Cross-award badges per AWARD_ICONS in turing/gen_turing.py
% Compile with: xelatex turing_prize_laureates_beamer.tex

\documentclass[aspectratio=169,9pt]{beamer}

% ---- Theme ----
\usetheme{default}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{%
  \hfill{\tiny\color{mutedgray}\insertframenumber/\inserttotalframenumber}\hspace*{6pt}\vspace{4pt}%
}
\newcommand{\framesubject}{}
\setbeamertemplate{frametitle}{%
  \vspace{8pt}%
  \centering
  {\large\bfseries\color{turingclr}ACM 图灵奖 \insertframetitle}\\[3pt]
  {\footnotesize\color{mutedgray}\framesubject}\\[4pt]
  \textcolor{turingbg}{\rule{0.95\textwidth}{0.6pt}}%
  \vspace{-6pt}%
}

% ---- Fonts & Language ----
\usepackage{fontspec}
\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold]
\setCJKsansfont{PingFang SC}
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\setsansfont{Helvetica Neue}

% ---- Packages ----
\usepackage{booktabs}
\usepackage{array}
\usepackage{tikz}
\usepackage{amssymb}
\usepackage{colortbl}
\usepackage{graphicx}\usepackage{fontawesome5}

% ---- Colors ----
\definecolor{headerblue}{RGB}{41,65,122}
\definecolor{yearcolor}{RGB}{150,40,90}
\definecolor{fieldcolor}{RGB}{30,100,60}
\definecolor{mutedgray}{RGB}{100,100,100}
\definecolor{slidebg}{RGB}{250,252,255}
@@COLORS@@

% ---- Beamer Colors ----
\setbeamercolor{background canvas}{bg=slidebg}
\setbeamercolor{title}{fg=turingclr}

% ---- Cross-award badges ----
@@BADGES@@

% Table row for a laureate
\newcommand{\cn}[1]{\newline{\scriptsize\color{mutedgray}#1}}
\newcommand{\lrow}[6]{%
  {\bfseries\color{turingclr}#1} & {\color{yearcolor}#2} & {#3} & {#4} & {\scriptsize #5} & {\scriptsize\color{fieldcolor}#6} \\[2.5pt]
}

% ---- Document ----
\begin{document}

@@FRAMES@@

\end{document}
"""
    tex = tex.replace("@@COLORS@@", color_defs)
    tex = tex.replace("@@BADGES@@", badge_cmds_tex)
    tex = tex.replace("@@FRAMES@@", "\n\n".join(frames))

    tex_path = os.path.join(HERE, MAIN + ".tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)
    print("wrote", tex_path)


if __name__ == "__main__":
    build()
