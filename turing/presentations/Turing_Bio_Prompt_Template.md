# 图灵奖得主立传提示词模板（OpenTuring · Beamer）

> 本文件是 OpenTuring 项目「图灵奖得主立传」的**通用提示词模板**。标杆实例为 Donald E. Knuth（1974 图灵奖，算法分析与计算机排版）。参照物理学家侧标杆 Kenneth G. Wilson（1982 诺贝尔物理学奖）与化学家侧标杆 Frederick Sanger（1958/1980 两度诺贝尔化学奖）。
> 直接复制本文件内容到新对话中使用，按步骤执行，每完成一步汇报进度。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位与产物

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **标杆实例**：Donald E. Knuth（唐纳德·克努特 / 高德纳，1938-，1974 图灵奖）。
- **单一产物**：每个图灵奖得主生成一份 Beamer deck（`.tex` → `.pdf`），外加一份人物专属提示词（`.md`）与必要的数据库脚本。
- **设计哲学**：图灵奖得主立传与数学家立传的核心差异在于——**图灵奖得主必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达；与数学家不同，图灵奖得主的「贡献」常表现为**算法、语言、系统、理论**而非「定理」，立传应突出其**奠基性工程与思想**。这两点构成模板骨架，务必保留。
- **版式双模板**：图灵奖得主 Beamer 版式 = **Wilson 骨架（气泡背景 + 身份信息页 + 卡片式）** + **高斯版式（表格语义化 + 公式框 + 时间线）**。封面、身份信息页、核心贡献概览沿用 Wilson 卡片骨架；**生平关键事件、核心贡献、荣誉传承等页面优先采用高斯模板的 `tabularx` 语义化表格 + `\fcolorbox` 公式框**（详见第四章 4.7 节）。

### 标准目录结构

```
turing/presentations/
├── Turing_Bio_Prompt_Template.md      # 本模板（通用提示词 + tex 说明）
├── cover/
│   └── openturing_page.tex            # 项目首页模板（统一 \input）
└── {Laureate}/                        # 目标人物目录（按第 1 步创建）
    ├── {Laureate}_zh.tex              # Beamer 源码
    ├── {Laureate}_zh.md               # 人物专属提示词
    ├── Makefile                        # 编译/出图/合成视频
    └── images/{Avatar}.jpg             # 肖像
```

> 图灵奖得主本地 Wikipedia 数据统一存放于 `turing/pages/{year}/{Name}/`（按获奖年份组织，如 `turing/pages/1974/Donald Knuth/`）。每个子目录含 `index.html`（原始 HTML，含 infobox + 正文）与 `metadata.json`（简化字段：title/url/year/image_count）。**注意**：图灵奖侧没有 `page.md` 可读正文，需从 `index.html` 提取 infobox 与正文作为事实基准。

---

## 二、硬性格式要求（★ 必须满足，缺一不可）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 `index.html` infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenTuring`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。
5. **必须通过编译验证**：`make distclean && make` 返回 `EXIT=0`，无缺字、无致命溢出。

---

## 三、标准任务流程（逐步执行）【模板通用】

> 每完成一步汇报进度，遇到歧义先征求用户意见再继续。
> **数据库同步要求**：第 4 步（研究领域入库）与第 4.5 步（社会关系入库）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：核对本地 Wikipedia 页面【人物专属】

- 定位本地数据：`turing/pages/{year}/{Name}/index.html`（含 infobox + 正文）与 `metadata.json`。
- 下载头像到 `images/{Avatar}.jpg`（Wikipedia infobox 照片）。
- 从 `index.html` 提取 infobox 与正文，输出供校验，形成**事实基准**：
  - 生卒日期、国籍（含变迁）、父母、教育（学校/专业/年份/论文题目）
  - 博士导师、博士论文题目、博士后机构
  - 主要任职机构（含年份）、关键荣誉（含年份）、知名学生
  - 核心贡献清单（见第 4 步）、关键时间线（15–20 个节点）

### 第 1 步：建立目录【模板通用】

- 在 `turing/presentations/` 下创建 `{Name}/` 与 `images/`。

### 第 2 步：复制 Makefile【模板通用】

- 复制标杆实例 `Donald_Knuth/Makefile`，设置 `MAIN={Name}_zh`、`VIDEO_NAME={Name}_zh`。

### 第 3 步：收集图片【人物专属】

- 使用 Wikipedia infobox 肖像作为封面图。

### 第 4 步：研究领域梳理 + 入库【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | {field A} | {中文} | {说明} | 封面、核心页 |
| 1 | {field B} | {中文} | {说明} | 核心页 |
| 2 | {field C} | {中文} | {说明} | 专属页 |
| 3 | {field D} | {中文} | {说明} | 专属页 |

#### 4.1 研究领域入库操作（★ 必做，写入 greatminds 库 MySQL）

> 参照化学家标杆 Sanger 的入库脚本 `MySQL/seed_sanger_full.py`（人物主记录 + 研究领域）模式执行。

- 新建/更新 `people` 主记录（`name_en='{Name}'`），设置 `primary_occupation='{主职业}'`、`has_biography=1`、`has_social_data=1`，补齐 `qid`/`gender`/`birth_date`/`death_date`/`description`
- 关联职业（`person_occupation`，主职业 rank 0、次要职业 rank 1）
- 关联国籍（`person_nationality`）
- 将上表 N 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项（含 `name_zh`）
- 生成入库脚本 `MySQL/seed_{name}_full.py` 并执行，脚本末尾输出校验结果（研究领域 / 国籍 / 职业 / `person_field` 总数）

### 第 4.5 步：社会关系梳理 + 入库【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | {博士导师} | 师→生 | {导师身份/成就} |
| colleague | {同事} | 无向 | {合作背景} |
| co-honored | {共同得主} | 无向 | {共同获奖} |

> 关系类型键取自 `relation_types`：`advisor-student` / `colleague` / `co-honored` / `spouse`。

#### 4.5.1 社会关系入库操作（★ 必做，写入 greatminds 库 MySQL）

> 参照化学家标杆 Sanger 的入库脚本 `MySQL/seed_sanger_relations.py`（社会关系）模式执行。

- 将上表关系写入 `person_relation`（`from_id` / `to_id` / `relation_type` / `note` / `source`），`source` 记 `'立传-{Name}'`
- **方向处理**：`advisor-student` 有向（导师 → 学生）；`colleague` / `co-honored` 无向（`from_id`/`to_id` 用 `sorted()` 归一，避免重复）
- 不在库中的关联人物先建占位记录（`has_biography=0`），关系 `note` 加 `[材料待展开] ` 前缀
- 生成入库脚本 `MySQL/seed_{name}_relations.py` 并执行，脚本末尾输出校验结果（新建人物数 / 新增关系数 / `person_relation` 总数）

### 第 5 步：设计配色方案【人物专属】

- **气质**：{理论深度 / 计算之美 / 系统性 …}。
- **配色**：图灵紫（OpenTuring 品牌主色）+ 强调色 + 四分类色。
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应设计母题。

> **OpenTuring 品牌色（固定，勿改）**：
> `coverprimary` 图灵紫 `#5B2D8E` · `coveraccent` 强调红 `#B03A2E` · `coveramber` 琥珀 `#D9A441` · `coverpurple` 青绿 `#1E8E8E`

### 第 6 步：规划幻灯片序列【人物专属，可微调】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 顶部标签 + 姓名 生卒年 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 四大研究领域
04  早年 — 教育/天赋起点
05  …（按生平/贡献分段，10–16 页）
NN  结尾
```

### 第 7 步：编写 Beamer 源码【模板通用】

- 每页用 `\newcommand{\xxxslide}{...}` 定义。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）整体复用标杆实例骨架（见第四章）。

### 第 8 步：布局检查【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
- **遗产页（legacy）格式红线【⚠ 实测踩坑，来自 Ken Thompson 立传】**：
  - ❌ 禁止用 `2×2` 网格 + `text width=5.6cm`：下排卡片（`y=-1.05`）与底部总结框（`y=-2.55`）在 16:9 画布上**纵向重叠**。
  - ✅ 必须对齐 Andrew_Yao / Leslie_Lamport 标杆的 **1×4 横排**：四卡 `text width=3.05cm`，`node[leg] style={rounded corners=6pt, inner xsep=6pt, inner ysep=8pt, font=\fontsize{6.4}{8.4}}`，横排 `x = -5.4 / -1.8 / 1.8 / 5.4`、`y=1.3`；底部框 `y=-1.6`、`text width=13.0cm`。经 `make distclean && make` 验证无重叠。

### 第 9 步：史实审查 + 术语审查【人物专属】

- 列出该人物**特殊陷阱表**（归属争议、容易写错的年份/机构/学生、获奖理由表述）。
- 列出**术语清单**（英文 / 中文 / 风险点）。

### 第 10 步：更新总名单 turing_award_winners.md【模板通用，★ 易遗漏】

> **立传完成（PDF 编译通过）后，必须同步更新总名单的「立传」列**，否则名单会一直停留在 🔲。

- 编辑 `turing/turing_award_winners.md`，把该得主所在行的「立传」列由 `🔲` 改为 `✅`。
- 两轮 Review 全部完成后，再把「Review」列由 `🔲` 改为 `✅`。
- 社会关系入库（第 4 步 + 第 4.5 步执行完毕）后，再把「社会关系入库」列由 `🔲` 改为 `✅`。
- 校验：该得主行末尾应为 `| ✅ | ✅ | ✅ |`（立传 + Review + 社会关系入库三通过）。

> **总名单列结构**（含三列标志位）：`| 年份 | 得主 | 生卒年 | 国籍/身份 | 获奖时机构 | 主要成果概括 | 备注 | 立传 | Review | 社会关系入库 |`

---

## 四、tex 模板说明（★ 核心复用资产）

> 以下骨架源自标杆实例（Donald Knuth 的 `Donald_Knuth_zh.tex`）。
> 代码块内的 `<...>` 为需替换的人物专属占位符。

### 4.1 tex 文件整体结构

```
[1] 文件头注释        —— 模板说明 / 设计母题 / 资料来源
[2] documentclass     —— aspectratio=169,14pt
[3] 主题与模板设置    —— navigation symbols / footline（页码）
[4] 字体包            —— fontspec + xeCJK（PingFang SC / Helvetica Neue）
[5] 其他包            —— xcolor/tikz/graphicx/fix-cm/adjustbox/fontawesome5/amsmath/amssymb
                       + booktabs/tabularx/array/colortbl（高斯版式表格所需，★ 见 4.7）
[6] tikz 库           —— positioning,calc,arrows.meta,shadows
[7] 配色定义          —— \definecolor（图灵紫/强调色/四分类色/面板色）
[8] 核心宏定义        —— \plainbar / \deckbackground / \sectiontitle / \lab
[9] 每页 slide 宏     —— \titleslide / \profileslide / \timelineslide / \xxxslide / \closingslide
                       （\timelineslide 时间线页 + 表格语义化页 + 公式框页，见 4.7）
[10] document 主体    —— 按序 \openturingslide \titleslide ... \closingslide
```

### 4.2 导言区骨架（可直接复制）

```latex
% =============================================================
%  OpenTuring laureate biography template (Beamer)
%  Design motif: {algorithm / typesetting / ...}
%  Source: local Wikipedia (turing/pages/{year}/{Name}/index.html)
% =============================================================
\documentclass[aspectratio=169,14pt]{beamer}
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{\hfill{\scriptsize\color{covermuted}\insertframenumber/\inserttotalframenumber}\hspace{0.4cm}\vspace{0.15cm}}
\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold, ItalicFont=PingFang SC]
\setCJKsansfont{PingFang SC}[BoldFont=PingFang SC Semibold, ItalicFont=PingFang SC]
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold, ItalicFont=Helvetica Neue Italic]
\setsansfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold, ItalicFont=Helvetica Neue Italic]
\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{fix-cm}\usepackage{adjustbox}\usepackage{fontawesome5}
\usepackage{amsmath}\usepackage{amssymb}
\usepackage{booktabs}\usepackage{tabularx}\usepackage{array}\usepackage{colortbl} % ★ 高斯版式表格所需
\usetikzlibrary{positioning,calc,arrows.meta,shadows}\graphicspath{{images/}}
\renewcommand{\tabularxcolumn}[1]{m{#1}}
```

### 4.3 配色变量约定（OpenTuring 品牌色固定）

| 变量 | 语义 | 标杆值 |
|------|------|--------|
| `bgmain` | 画布底色 | `RGB{247,245,251}` |
| `coverprimary` | 主色（图灵紫） | `HTML{5B2D8E}` |
| `coveraccent` | 强调色（红） | `HTML{B03A2E}` |
| `coveramber` | 琥珀 | `HTML{D9A441}` |
| `coverpurple` | 青绿 | `HTML{1E8E8E}` |
| `coverdark` | 深文字色 | `HTML{241A33}` |
| `covermuted` | 弱文字色 | `HTML{6B6478}` |
| `titlecolor` | 标题色 | `RGB{36,26,51}` |
| `muteddark` | 副标题色 | `RGB{96,90,110}` |
| `badgeA~D` | 四分类色 | 人物专属 |
| `panelA~D` | 四分类面板底色 | 与 badge 同色系浅色 |

```latex
\setbeamercolor{background canvas}{bg=bgmain}
```

### 4.4 核心宏定义（可直接复制，参照 episode-00 版式）

```latex
% Bottom decorative bar (used by content pages)
\newcommand{\plainbar}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverdark, opacity=0.06] (current page.south west) rectangle ([yshift=0.4cm]current page.south east);
  \draw[coverprimary, opacity=0.40, line width=0.8pt] ([yshift=0.4cm]current page.south west) -- ([yshift=0.4cm]current page.south east);
\end{tikzpicture}%
}

% Bubble background (sparse solid circles, four sizes) — used by cover/closing
\newcommand{\deckbackground}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!5] (current page.north west) rectangle (current page.south east);
  \fill[badgeA!12] (current page.north west) ++(2.0,-2.0) circle (2.6cm);
  \fill[badgeB!10] (current page.south east) ++(-2.4,2.0) circle (3.0cm);
  \fill[badgeC!10] (current page.north east) ++(-3.2,-2.4) circle (1.6cm);
  \fill[coveraccent!10] (current page.south west) ++(2.8,2.2) circle (1.2cm);
  \fill[coverdark, opacity=0.06] (current page.south west) rectangle ([yshift=0.42cm]current page.south east);
\end{tikzpicture}%
}

% Section title: {main title} {subtitle}
\newcommand{\sectiontitle}[2]{%
\vspace{-0.52cm}
\begin{center}
  {\fontsize{20}{24}\selectfont\bfseries\color{titlecolor} #1}\\[2pt]
  {\fontsize{7.5}{9.5}\selectfont\itshape\color{muteddark} #2}
\end{center}
\vspace{0.06cm}
}

% Field label for the profile slide
\newcommand{\lab}[1]{{\fontsize{7.0}{8.8}\selectfont\bfseries\color{coveraccent!88!black} #1}}
```

### 4.5 身份信息页（`\profileslide`）实现模板 ★

```latex
\newcommand{\profileslide}{\begin{frame}\plainbar
\sectiontitle{<NAME_ZH> - <SUBTITLE>}{生卒 · 本名 · 国籍 · 师承 · 任职 · 荣誉}
\begin{center}\begin{tikzpicture}[
    infob/.style={rounded corners=6pt, inner xsep=10pt, inner ysep=9pt, text width=4.8cm,
      font=\fontsize{7.4}{9.4}\selectfont, align=left}
  ]
  % left avatar
  \node[draw=coveraccent!55, line width=1.2pt, rounded corners=5pt, fill=white, inner sep=3pt]
    at (-6.15,0.15) {\IfFileExists{images/<AVATAR>.jpg}{\includegraphics[width=3.0cm,height=3.9cm,keepaspectratio]{<AVATAR>.jpg}}{\textcolor{covermuted}{\faIcon{user}\enspace Portrait}}};
  \node[anchor=north, font=\fontsize{6.2}{7.4}\selectfont\itshape, text=covermuted]
    at (-6.15,-2.2) {<FULL_NAME> (<YEAR>)};
  % right 2x2 info grid (top row: north-aligned, bottom row: south-aligned)
  \node[infob, fill=goldpanel, draw=coveraccent!45, anchor=north] at (-1.8,2.35)
    {\lab{生卒}\quad <DATES>\\[2pt]\lab{本名}\quad <FULL_NAME_ZH>\\[2pt]\lab{国籍}\quad <NATIONALITY>};
  \node[infob, fill=<PANEL_B>, draw=<BADGE_B>!45, anchor=north] at (3.8,2.35)
    {\lab{师承}\quad <ADVISOR>\\[2pt]\lab{任职}\quad <POSITIONS>};
  \node[infob, fill=<PANEL_A>, draw=<BADGE_A>!50, anchor=south] at (-1.8,-2.01)
    {\lab{出生地}\quad <BIRTHPLACE>\\[2pt]\lab{教育}\quad <EDUCATION>};
  \node[infob, fill=<PANEL_C>, draw=<BADGE_C>!45, anchor=south] at (3.8,-2.01)
    {\lab{主要荣誉}\quad <HONORS>\\[2pt]\lab{核心领域}\quad <FIELDS>};
\end{tikzpicture}\end{center}\end{frame}}
```

> **对齐关键**：上排两张卡用 `anchor=north`（上边缘对齐），下排两张卡用 `anchor=south`（下边缘对齐），保证四张卡上下左右整齐。

### 4.6 结尾页（`\closingslide`）要点

- 使用 `\deckbackground`（气泡背景）。
- 主题金句 + 分隔线 + 致敬行 + 生卒年行。
- **底部品牌统一写 `OpenMathAI`**（不写 `OpenTuring`）。

### 4.7 高斯模板版式设计模式（★ 生平/贡献/荣誉页首选）

> 图灵奖得主 Beamer 的**生平关键事件、核心贡献、荣誉传承、算法/系统专题**等页面，优先采用高斯模板的表格语义化 + 成果框版式（而非 Wilson 的卡片式），以更清晰地结构化「概念 → 贡献 → 意义」。封面、身份信息页、核心贡献概览仍用 Wilson 卡片骨架。以下骨架源自 `mathematician/presentations/Gauss_Biography_Template.md` 第四章，色名按图灵品牌色变量替换（`prussiablue`→`coverprimary`、`mathgold`→`coveraccent`、`badgeX`→`badgeA~D`、`Xpanel`→`panelA~D`）。

#### 4.7.1 表格语义化设计（核心贡献页通用）

每页用 `tabularx` 三列表格，**列头按页面主题语义化**，第一列加粗、用强调色：

| 页面主题 | 列头示例 |
|---|---|
| 早年 / 教育 | `时间 ｜ 事件 ｜ 影响` |
| 核心贡献（通用） | `问题 ｜ 该得主的贡献 ｜ 意义` |
| 算法 / 系统专题 | `问题 ｜ 方法/算法 ｜ 结果` |
| 荣誉 / 传承 | `类别 ｜ 代表 ｜ 意义` |
| 争议 / 历史事件 | `事件 ｜ 经过 ｜ 结果` |

**通用模式**：`{时间/概念/问题} ｜ {该人物做了什么} ｜ {影响/结果/意义}`

表格骨架（含配色）：

```latex
\begin{center}
\footnotesize
\arrayrulecolor{coveraccent!65}
\begin{tabularx}{12.4cm}{>{\bfseries\scriptsize}m{3.2cm}|>{\scriptsize}X|>{\scriptsize}p{3.0cm}}
\toprule
\rowcolor{coverprimary}\multicolumn{1}{c|}{\footnotesize\color{white}\textbf{列1}} &
  \multicolumn{1}{c|}{\footnotesize\color{white}\textbf{列2}} &
  \multicolumn{1}{c}{\footnotesize\color{white}\textbf{列3}} \\
\midrule
\cellcolor{goldpanel}\textcolor{coveraccent!88!black}{第一列内容} &
  \cellcolor{panelA}\textcolor{badgeA!82!black}{第二列内容} &
  \cellcolor{panelB}\textcolor{badgeB!82!black}{第三列内容} \\
\midrule
... （重复，每行间 \midrule）
\bottomrule
\end{tabularx}
\end{center}
```

> **注意**：`\arrayrulecolor`、`\rowcolor`、`\cellcolor` 需 `colortbl` 包（已在 4.2 导言区补充）；`>{\bfseries\scriptsize}m{...}` 需 `array` 包。

#### 4.7.2 核心成果框（★ 高斯版式的标志性元素，图灵适配）

在表格下方展示该得主**最标志性的成果**——算法、复杂度记号、形式化定义或代码片段（图灵奖得主的「公式」常表现为算法与形式系统，而非物理公式）：

```latex
\begin{center}
\fcolorbox{coveraccent!70}{goldpanel}{%
  \begin{minipage}{11.7cm}
  \centering
  {\fontsize{9}{12}\selectfont\bfseries\color{coveraccent!85!black} {{成果标题（含年份）}}}\\[2pt]
  {\fontsize{11}{14}\selectfont\color{coverprimary!88!black}${{成果内容}}$}
  \end{minipage}%
}
\end{center}
```

**要点**：
- 成果内容可以是：复杂度记号（如 Cook 的 `SAT ∈ NP-complete`、姚期智的通信复杂度下界）、核心算法伪代码、形式化定义（如 BNF 文法、Hoare 逻辑三元组 `{P} C {Q}`）
- 长公式用 `\resizebox{11.4cm}{!}` 自动缩放单行；复杂多行用 `\begin{aligned}` / `\begin{cases}` / `\begin{vmatrix}`
- 标题含年份与出处（如「快速排序（Hoare，1960）」）
- 成果框通常**替换**页底金句（成果即是最好的具象化）

#### 4.7.3 时间线页（`\timelineslide`）

生平纵览页用竖线 + 节点的 TikZ 时间线（置于身份信息页之后、核心贡献之前）：

```latex
\newcommand{\timelineslide}{\begin{frame}\plainbar\sectiontitle{<NAME_ZH> 的一生}{<生卒年>}
\vspace{-0.45cm}
\begin{center}
\begin{tikzpicture}[
  event/.style={font=\fontsize{7}{9}\selectfont, align=left, text width=8.6cm},
  yr/.style={font=\fontsize{8.5}{10.5}\selectfont\bfseries\color{coveraccent!88!black}}
]
  \draw[coveraccent!70, line width=1.4pt] (0,3.1) -- (0,-3.1);
  \foreach \y/\year/\txt in {
    3.1/{年份}/{事件1},
    2.4/{年份}/{事件2},
    ...（按生平顺序排列 10 个左右节点）
  }{
    \fill[coveraccent!80] (0,\y) circle (2.2pt);
    \node[yr, anchor=east] at (-0.25,\y) {\year};
    \node[event, anchor=west] at (0.35,\y) {\txt};
  }
\end{tikzpicture}
\end{center}
\end{frame}}
```

#### 4.7.4 年份标注模式

| 场景 | 写法 | 示例 |
|---|---|---|
| 单年 | `（YYYY）` 或 `YYYY：` | `快速排序（1960）` |
| 区间 | `YYYY–YYYY` | `1968–1974：TAOCP 前三卷` |
| 约略 | `约 YYYY` | `约 1970：TeX 雏形` |
| 年代 | `YYYYs` | `1970s` |
| 发现 vs 发表 | 分开标注 | `1962 提出；1969 发表` |

#### 4.7.5 溢出修复策略（★ 每写一页就 make，看到溢出就修）

优先级从轻到重：
1. 删装饰元素（`\plainbar` / `\deckbackground`）
2. 缩 `inner sep` / `\arraystretch`
3. 缩字号
4. 减空行间距（`\\[3pt]` → `\\[1pt]`）
5. 增大顶部负间距（`\vspace{-0.45cm}` → `-0.9cm`）或成果框前负间距
6. 最后才调 TikZ 坐标

**验收标准**：`Overfull \vbox > 10pt` 必须修复；`\hbox > 50pt` 必须修复；`< 5pt` 可忽略。

---

## 五、背景音乐选择（★ 与数学/物理/化学家共享同一音乐库）

> **音乐库位置**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`（各学科共享）。
> **精选曲目汇总**：`music_audio/curated_tracks.md`（★ 选曲前必读）。
> **工作机制**：每位得主 Makefile 中有 `BGM = $(wildcard *.wav)`。将选定的 `.wav` 复制到该得主子目录下，`make video` 自动检测并混入；BGM 略短于 slides 总时长时，ffmpeg `-shortest` 自动对齐。`.wav` 不入 git。

### 按人物气质推荐

| 得主气质 | 推荐来源 | 示例曲目 | 理由 |
|-----------|---------|------------|------|
| **史诗/奠基**（Knuth、Dijkstra） | Alex-Productions | New Lands, Expedition | 宏大开阔，匹配"改写计算机史" |
| **理论/算法之美**（Cook、Karp、姚期智） | Alex-Productions | Timeless | 内敛深度，理论纵深 |
| **工程/系统**（Ritchie、Thompson） | Inspiring Electronic | Falling Apart, Mirage | 现代科技感 |
| **AI/智能**（Minsky、Hinton） | Alex-Productions | Awaken, Daylight | 未来感、突破 |
| **悲剧/早逝**（Floyd、Allen） | Inspiring Electronic | Lonesome, Through the Darkness | 暗色调 |

### 选曲落地步骤【模板通用】

> 对标化学家标杆 Sanger 与物理学家标杆 Wilson（二者均选 `Timeless.wav`，与理论内敛气质匹配）。

1. **先读 `music_audio/curated_tracks.md`**，按得主气质在推荐表定位来源与候选曲目。
2. **选定 1 首**（首选优先级最高、受众最广、气质最贴合者），复制到得主子目录 `{Laureate}/`。
3. **命名规范**：简洁无空格、无博主前缀，如 `NewLands.wav`（对标 Sanger/Wilson 的 `Timeless.wav`），便于 Makefile `BGM = $(wildcard *.wav)` 自动识别。
4. **验证**：`make video` 合成后确认 BGM 已混入（`-stream_loop -1` 循环 + `-shortest` 对齐 slides 总时长）；`.wav` 不入 git（已在 `.gitignore`）。
5. **在人物专属提示词「第 5 步」末尾记录**：选曲名 + 来源博主 + 气质理由，便于 Review 追溯。

> **Knuth 标杆实例**：气质「史诗/奠基」（算法分析之父、TAOCP 作者、TeX 创造者），选 Alex-Productions 的 **New Lands**（152k views，高受众/史诗/开阔，匹配"改写计算机史"的奠基叙事），落地文件 `turing/presentations/Donald_Knuth/NewLands.wav`。

---

## 六、Review 流程（★ 两轮，缺一不可）

> **核心原则：第一版几乎必然存在史实错误，必须经过多轮核查。**
> 第一轮解决"factually wrong"（事实错误），第二轮解决"professionally unstable"（专业上站不住）。

### 6.1 两轮 Review 的分工

| 轮次 | 目标 | 关键词 |
|------|------|--------|
| **第一轮** | 事实错误（年份、人名、机构、奖项、引语来源） | "对" |
| **第二轮** | 专业上站不住（引号对应原文、过度宣传化、现代语言包装历史人物） | "稳" |

### 6.2 史实审查通用红线（任何得主通用）

| 绝对不要 | 正确做法 |
|---------|---------|
| 中文引号内写得主"原话" | 间接引语；有原文才加引号 |
| 声称"第一次/第一个/唯一" | "核心贡献""里程碑式成就" |
| 标题中标注无法确认的年份 | 年份放正文，标题保留核心概念 |
| 用 21 世纪术语包装历史人物 | "今天我们称之为…""为后来…奠定基础" |
| 编造戏剧性因果 | 查权威来源（ACM 官网、Wikipedia 引注） |

### 6.3 Review 完成后更新总名单 ★（易遗漏）

- 两轮 Review 全部完成后，把 `turing_award_winners.md` 中该得主的「Review」列改为 `✅`。

---

## 七、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `turing/pages/{year}/{Name}/index.html` | 本地 Wikipedia 正文（infobox + 正文） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 标杆实例 Beamer 源码（Wilson 卡片骨架母本） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.md` | 标杆实例人物专属提示词 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（统一 `\input`） |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review/社会关系入库三列标志位） |
| `mathematician/presentations/Gauss_Biography_Template.md` | ★ 高斯立传模板（第四章 4.7 版式设计模式母本） |
| `physicist/presentations/20th_century/Werner_Heisenberg/Werner_Heisenberg_zh.tex` | ★ 高斯版式适配成品（表格语义化 + 公式框 + 时间线） |
| `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md` | 化学家标杆提示词参考 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 物理学家标杆提示词参考 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
