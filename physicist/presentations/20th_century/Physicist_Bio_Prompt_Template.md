# 物理学家立传提示词模板（OpenPhysicist · Beamer）

> 本文件是 OpenPhysicist 项目「20 世纪物理学家立传」的**通用提示词模板**，以 Kenneth G. Wilson（1982 诺贝尔物理学奖，重整化群理论）为标杆实例沉淀而成。
> 直接复制本文件内容到新对话中使用，按步骤执行，每完成一步汇报进度。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位与产物

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **标杆实例**：`20th_century/Kenneth_G_Wilson/`（完整成品，可对照）。
- **单一产物**：每个物理学家生成一份 Beamer deck（`.tex` → `.pdf`），外加一份人物专属提示词（`.md`）与必要的数据库脚本。
- **设计哲学**：物理学家立传与数学家立传的核心差异在于——**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达。这两点构成物理学家模板的骨架，务必保留。

### 标准目录结构

```
physicist/presentations/20th_century/
├── Physicist_Bio_Prompt_Template.md      # 本模板（通用提示词 + tex 说明）
├── Nobel_Physics_Laureates_20th_21st_Century.md
├── cover/
│   └── openphysicist_page.tex            # 项目首页模板（统一 \input）
├── Kenneth_G_Wilson/                     # 标杆实例
│   ├── Kenneth_G_Wilson.html             # 本地 Wikipedia
│   ├── Kenneth_G_Wilson_zh.tex           # Beamer 源码
│   ├── Kenneth_G_Wilson_zh.md            # 人物专属提示词
│   ├── Makefile                          # 编译/出图/合成视频
│   └── images/{Avatar}.jpg               # 肖像
└── {New_Physicist}/                      # 目标人物目录（按第 1 步创建）
    ├── {New_Physicist}.html
    ├── {New_Physicist}_zh.tex
    ├── {New_Physicist}_zh.md
    ├── Makefile
    └── images/{Avatar}.jpg
```

---

## 二、硬性格式要求（★ 必须满足，缺一不可）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。
5. **必须通过编译验证**：`make distclean && make` 返回 `EXIT=0`，无缺字、无致命溢出。

---

## 三、标准任务流程（逐步执行）【模板通用】

> 每完成一步汇报进度，遇到歧义先征求用户意见再继续。
> **数据库同步要求**：第 4 步（研究领域入库）与第 4.5 步（社会关系入库）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面【人物专属】

- 下载 `https://en.wikipedia.org/wiki/{Name}` 到 `{Name}.html`。
- 下载头像到 `images/{Avatar}.jpg`（Wikipedia infobox 照片）。
- 提取 infobox 与正文，输出供校验，形成**事实基准**：
  - 生卒日期、国籍（含变迁）、父母、教育（学校/专业/年份/论文题目）
  - 博士导师、博士论文题目、博士后机构
  - 主要任职机构（含年份）、关键荣誉（含年份）、知名学生
  - 核心贡献清单（见第 4 步）、关键时间线（15–20 个节点）

### 第 1 步：建立目录【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `{Name}/` 与 `images/`。

### 第 2 步：复制 Makefile【模板通用】

- 复制标杆实例的 `Makefile`，设置 `MAIN={Name}_zh`、`VIDEO_NAME={Name}_zh`。

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

### 第 4.5 步：社会关系梳理 + 入库【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | {博士导师} | 师→生 | {导师身份/成就} |
| colleague | {同事} | 无向 | {合作背景} |
| co-honored | {共同得主} | 无向 | {共同获奖} |

> 关系类型键取自 `relation_types`：`advisor-student` / `colleague` / `co-honored` / `spouse`。

### 第 5 步：设计配色方案【人物专属】

- **气质**：{理论深度 / 对称性 / 尺度感 …}。
- **配色**：{主色（理论气质）} + 香槟金（诺奖）+ 四分类色。
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以不同尺度呼应设计母题（如自相似性/对称性）。

### 第 6 步：规划幻灯片序列【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
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

### 第 9 步：史实审查 + 术语审查【人物专属】

- 列出该人物**特殊陷阱表**（归属争议、容易写错的年份/机构/学生、诺奖理由表述）。
- 列出**术语清单**（英文 / 中文 / 风险点）。

---

## 四、tex 模板说明（★ 核心复用资产）

> 以下骨架源自标杆实例 `Kenneth_G_Wilson_zh.tex`。
> 代码块内的 `<...>` 为需替换的人物专属占位符（如 `<AVATAR>` → `Wilson`、`<NAME_ZH>` → `肯尼斯·威尔逊`）。

### 4.1 tex 文件整体结构

```
[1] 文件头注释        —— 模板说明 / 设计母题 / 资料来源
[2] documentclass     —— aspectratio=169,14pt
[3] 主题与模板设置    —— navigation symbols / footline（页码）
[4] 字体包            —— fontspec + xeCJK（PingFang SC / Helvetica Neue）
[5] 其他包            —— xcolor/tikz/graphicx/fix-cm/adjustbox/fontawesome5/amsmath/amssymb
[6] tikz 库           —— positioning,calc,arrows.meta,shadows
[7] 配色定义          —— \definecolor（主色/强调色/四分类色/面板色）
[8] 核心宏定义        —— \plainbar / \deckbackground / \sectiontitle / \lab
[9] 每页 slide 宏     —— \titleslide / \profileslide / \xxxslide / \closingslide
[10] document 主体    —— 按序 \openphysicistslide \titleslide ... \closingslide
```

### 4.2 导言区骨架（可直接复制）

```latex
% =============================================================
%  OpenPhysicist physicist biography template (Beamer)
%  Design motif: {self-similarity / symmetry / ...}
%  Source: local Wikipedia (<NAME>.html)
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
\usetikzlibrary{positioning,calc,arrows.meta,shadows}\graphicspath{{images/}}
```

### 4.3 配色变量约定

| 变量 | 语义 | 标杆值 |
|------|------|--------|
| `bgmain` | 画布底色 | `RGB{247,246,249}` |
| `coverprimary` | 主色（理论气质） | `HTML{1A237E}` 深靛蓝 |
| `coveraccent` | 强调色（诺奖金） | `HTML{C9A227}` |
| `coverdark` | 深文字色 | `HTML{1F2937}` |
| `covermuted` | 弱文字色 | `HTML{64748B}` |
| `titlecolor` | 标题色 | `RGB{24,26,64}` |
| `muteddark` | 副标题色 | `RGB{72,68,96}` |
| `badgeA~D` | 四分类色 | 如 `#4C5FD5` / `#0E7C7B` / `#E07B30` / `#C4204F` |
| `panelA~D` | 四分类面板底色 | 与 badge 同色系浅色 |
| `goldpanel` | 金色面板 | `RGB{255,245,225}` |
| `silverpanel` | 银色面板 | `RGB{240,240,244}` |

```latex
\setbeamercolor{background canvas}{bg=bgmain}
```

### 4.4 核心宏定义（可直接复制）

```latex
% Bottom decorative bar (used by content pages)
\newcommand{\plainbar}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverdark, opacity=0.06] (current page.south west) rectangle ([yshift=0.4cm]current page.south east);
  \draw[coveraccent, opacity=0.40, line width=0.8pt] ([yshift=0.4cm]current page.south west) -- ([yshift=0.4cm]current page.south east);
\end{tikzpicture}%
}

% Bubble background (sparse solid circles, four sizes) — used by cover/closing
\newcommand{\deckbackground}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coveraccent!4] (current page.north west) rectangle (current page.south east);
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
  {\fontsize{7.5}{9.5}\selectfont\itshape\color{muteddark} #2}\\[3pt]
  \textcolor{coveraccent}{\rule{2.6cm}{1.6pt}}
\end{center}
\vspace{0.06cm}
}

% Field label for the profile slide
\newcommand{\lab}[1]{{\fontsize{7.0}{8.8}\selectfont\bfseries\color{coveraccent!88!black} #1}}
```

### 4.5 封面（`\titleslide`）要点

- 顶部标签：`\faIcon{expand-alt}\enspace {领域标签}\enspace·\enspace {国籍}`，字号 13/17pt，强调色。
- 主标题：姓名，字号 27/33pt；副行：英文名 + 生卒年，字号 12/16pt。
- 四色 badge：`rounded corners=7pt, text width=2.55cm, minimum height=1.78cm, inner sep=6pt`。
- 头像（右上角）：`\IfFileExists` 条件包含，`draw=coveraccent!50, width=2.0cm,height=2.8cm`。
- 底部状态栏：`国籍 | 机构 | 主要奖项` 三要素，`anchor=south`。

### 4.6 身份信息页（`\profileslide`）实现模板 ★

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
    {\lab{出生地}\quad <BIRTHPLACE>\\[2pt]\lab{去世地}\quad <DEATHPLACE>\\[2pt]\lab{教育}\quad <EDUCATION>};
  \node[infob, fill=<PANEL_C>, draw=<BADGE_C>!45, anchor=south] at (3.8,-2.01)
    {\lab{主要荣誉}\quad <HONORS>\\[2pt]\lab{核心领域}\quad <FIELDS>};
\end{tikzpicture}\end{center}\end{frame}}
```

> **对齐关键**：上排两张卡用 `anchor=north`（上边缘对齐），下排两张卡用 `anchor=south`（下边缘对齐），保证四张卡上下左右整齐。

### 4.7 内容页版式参数速查

| 元素 | 参数 |
|------|------|
| 章节标题 | `\sectiontitle{20/24pt 主标题}{7.5/9.5pt 副标题}` |
| 内容条目卡 | `rounded corners=4~5pt, inner xsep=10pt, inner ysep=5~10pt, text width=12.4~12.6cm, font=7.0/9.0pt` |
| 三卡片页 | 上卡 y=2.55、中卡 y=0.85、下卡 y=-0.65，底部总结卡 y=-2.0 |
| 四列 leg 卡 | `text width=3.05cm, font=6.6~6.8/8.6~8.8pt, x=±5.4/±1.8` |
| 底部总结条 | `fill=silverpanel, draw=coveraccent!55~65, inner sep=6~12pt, text width=13.0cm` |

### 4.8 结尾页（`\closingslide`）要点

- 使用 `\deckbackground`（气泡背景）。
- 主题金句 + 分隔线 + 致敬行 + 生卒年行。
- **底部品牌统一写 `OpenMathAI`**（不写 `OpenPhysicist`）。

---

## 五、背景音乐选择（★ 借鉴数学家指南 §15.7）

> **音乐库位置**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`（物理学家与数学家共享同一音乐库）。
> **精选曲目汇总**：`music_audio/curated_tracks.md`（★ 选曲前必读）。
> **工作机制**：每位物理学家 Makefile 中有 `BGM = $(wildcard *.wav)`。将选定的 `.wav` 复制到该物理学家子目录下，`make video` 自动检测并混入；BGM 略短于 slides 总时长时，ffmpeg `-shortest` 自动对齐。`.wav` 不入 git。

### 5.1 音乐库概览

| 来源 | 目录 | 风格 | 适合场景 |
|------|------|------|------|
| Alex-Productions | `alex-productions/` | 史诗/纪录片/沉稳 | 宏大叙事、时间线、人物回顾 |
| Beethoven · Karajan | `beethoven-karajan/` | 古典交响乐 | 里程碑、结尾升华、古典气质 |
| Inspiring Electronic | `inspiring-electronic/` | 电子/电影/情感 | 悲剧人物、现代感、攻克难题 |
| LAKEY INSPIRED | `lakey-inspired/` | 轻电子/Chill | 轻松段落、过渡页 |

### 5.2 选曲原则

- 音乐气质应与物理学家气质匹配（而非简单选"好听"的）。
- 优先从 `curated_tracks.md` 精选列表挑选。
- 不是所有物理学家都需要 epic/heroic 风格。

### 5.3 按物理学家气质推荐

| 物理学家气质 | 推荐来源 | 推荐曲目示例 | 理由 |
|-----------|---------|------------|------|
| **史诗/奠基/革命**（Einstein, Feynman） | Alex-Productions | New Lands, Expedition | 宏大开阔，匹配"改写物理史"的气质 |
| **深沉/理性/尺度**（Wilson, Wigner） | Alex-Productions | Timeless, PAST | 内敛的深度，而非宏伟征服 |
| **悲剧/战争/反思**（Szilárd, Oppenheimer） | Inspiring Electronic | Lonesome, Through the Darkness | 暗色调，情感深沉 |
| **探索/远征**（Dirac, 玻尔） | Alex-Productions | Expedition, Eternals | 远征式叙事，理论探索 |
| **古典/庄严**（Planck, Lorentz） | Beethoven · Karajan | Symphony No.3 "Eroica", No.9 | 古典音乐的庄严与永恒 |
| **现代/科技/计算**（von Neumann 跨界, Wigner 计算） | Inspiring Electronic | Falling Apart, Mirage | 电子质感，现代感 |
| **鼓舞/突破/年轻天才**（Galois 式早熟, 杨振宁） | Alex-Productions | Awaken, Daylight | 明亮轻快，天才之光 |

### 5.4 操作步骤

```bash
# 1. 打开 curated_tracks.md，根据物理学家气质挑选曲目
# 2. 复制选定的 .wav 到该物理学家子目录
cp /Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav \
   /Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/{Name}/

# 3. make video 自动检测并使用
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/{Name}/
make video
```

> **实战案例**（Wilson 标杆）：选定 **Timeless**（Alex-Productions，沉稳/纪录片/长期纲领），匹配"重整化群不是单一突破，而是贯穿现代物理的纲领"这一气质。

---

## 六、Review 流程（★ 借鉴数学家指南 §16 / §14 / §15）

> **核心原则：第一版几乎必然存在史实错误，必须经过多轮核查。写完不是终点，终审才是。**
> Review 的本质：第一轮解决"factually wrong"（事实错误），第二轮解决"professionally unstable"（专业上站不住）。

### 6.1 两轮 Review 的分工

| 轮次 | 目标 | 关键词 |
|------|------|--------|
| **第一轮** | 事实错误（年份、人名、机构、奖项、引语来源） | "对" |
| **第二轮** | 专业上站不住（引号对应原文、过度宣传化、现代语言包装历史人物） | "稳" |

### 6.2 Wikipedia 本地文档终审清单（第一轮必做）

| # | 检查项 | 方法 | 高危信号 |
|:--:|------|------|---------|
| 1 | **事实性错误** | Beamer 每个日期/人名/机构与本地 `.html` 逐条对照 | 与 Wikipedia 不一致的年份、地名、人名 |
| 2 | **翻译/术语错误** | 术语与 Wikipedia 英文原词对照 | 概念性误译 |
| 3 | **重大遗漏** | 扫描 Wikipedia 目录，对比 Beamer 是否覆盖主要贡献 | 标志性定理/论文只字未提 |
| 4 | **结构性错误** | 时间线是否按生平顺序 | 时间跳跃混乱、因果倒置 |
| 5 | **编译告警** | 分析 `Overfull \hbox` / `Overfull \vbox` | vbox > 10pt 或 hbox > 50pt |
| 6 | **引语来源** | 每个加引号的句子须能在 Wikipedia 找到原文 | 中文引号内句子无法溯源 |
| 7 | **年份精确性** | 标题年份会被当作"正式发表年份" | 初版年 ≠ 修订年，写作年 ≠ 发表年 |
| 8 | **人物关系** | 导师/学生/合作者与 Wikipedia 一致 | "合作者"写成"学生"、"访问学者"写成"教授" |
| 9 | **荣誉/获奖** | 封面/身份页/荣誉页与 Wikipedia 一致 | 遗漏重大奖项、年份标错 |

### 6.3 优先级定义

| 优先级 | 定义 | 示例 |
|:--:|------|------|
| 🔴 **P0** | 事实错误 — 专业读者一眼看出 | 年份标错、遗漏关键经历、人物关系写错 |
| 🟡 **P1** | 来源存疑/模糊 — 经不起推敲 | 无法验证的引语、模糊年份表述 |
| 🟢 **P2** | 重要遗漏 — 补上更好 | 未提及的标志性成果、深入背景 |
| ⚪ **P3** | 可选补充 — 锦上添花 | 衍生影响、冷门趣闻 |

### 6.4 Review 报告输出格式

每轮 Review 完成后，输出结构化报告：

```markdown
## 🔍 {Name} Beamer — 第 N 轮 Review

### 🔴 事实性错误（需修复）
| # | 位置 | 当前内容 | 问题 | 修正 |
|---|------|------|------|------|

### 🟡 来源存疑/术语审查
| # | 位置 | 当前内容 | 问题 | 修正 |
|---|------|------|------|------|

### 🟢 重要遗漏
| # | 遗漏内容 | Wikipedia 记载 | 建议 |
|---|------|------|------|

### 📊 逐页对照
| # | 标题 | 事实准确性 | 遗漏 | 评价 |
|---|------|:--:|:--:|------|

### 📋 修复优先级汇总
| 优先级 | 数量 | 类型 |
|:--:|:--:|------|
```

### 6.5 史实审查通用红线（任何物理学家通用）

| 绝对不要 | 正确做法 |
|---------|---------|
| 中文引号内写物理学家"原话" | 间接引语；有原文才加引号 |
| 声称"第一次/第一个/唯一" | "核心贡献""里程碑式成就" |
| 标题中标注无法确认的年份 | 年份放正文，标题保留核心概念 |
| 固定写具体计算验证数字 | "大量""持续增长的""不断推进的" |
| "只有 N 篇论文" | "十余篇奠基性工作""主要著作" |
| 用 21 世纪术语包装 20 世纪物理学家 | "今天我们称之为…""为后来…奠定基础" |
| 编造戏剧性因果 | 查权威来源（Nobel 官网、AIP、Wikipedia 引注） |

### 6.6 多轮校改心态

- **三条独立意见指向同一问题 → 必改**；只有一条 → 判断后决定。
- **引号问题审阅者提出 → 坚决改**（引号是专业读者的红线）。
- 可尝试审阅者建议，也可回退——尝试是尊重，回退是判断。

---

## 七、LaTeX 告警检测重叠与溢出（★ 借鉴数学家指南 §13）

> **核心发现**：TikZ 节点间重叠（视觉可见）≠ LaTeX 能直接报错。LaTeX 只能检测"内容超出页面边界"的溢出，无法检测"两个节点在页面内部相互重叠"。因此需**告警分析 + 视觉审查**双管齐下。

### 7.1 告警解读规则

| 告警类型 | 严重度 | 含义 | 处理 |
|---------|------|------|------|
| `Overfull \hbox` < 20pt | 低 | 极轻微溢出，通常不可见 | 可忽略 |
| `Overfull \hbox` > 50pt | 高 | URL 或长英文单词未断行 | 必须修复 |
| `Overfull \vbox` < 5pt | 低 | 极轻微底部溢出 | 可忽略 |
| `Overfull \vbox` > 10pt | **严重** | 页面内容明显超出底部 | **必须修复** |

### 7.2 检测命令

```bash
# 编译后只抓告警行
xelatex -interaction=nonstopmode {Name}_zh.tex 2>&1 | grep "Overfull"
```

### 7.3 视觉审查盲区（LaTeX 无法检测，必须人工确认）

| 盲区类型 | 确认方法 |
|---------|---------|
| 节点间距离过近（文字几乎贴在一起） | `make images` 导出 PNG 逐页翻看 |
| 文字被裁切 | 打开 PDF 检查每个 panel |
| 颜色/对比度问题 | 普通屏幕（非 Retina）查看 |
| TikZ 内部元素碰撞 | 逐页检查 node 位置 |

---

## 八、史实审查进阶陷阱（★ 借鉴数学家指南 §14，物理学家适配）

> 这些不是低级错误，而是"看似合理、实则必须深究"的进阶陷阱。

| 陷阱 | 物理学家适配案例 | 教训 |
|------|----------------|------|
| **"N 篇论文"计数** | "只发表 X 篇论文" | 论文计数有争议，用"主要著作""开创性论文" |
| **"第一"断言** | "第一个提出 X 理论" | 物理学史少有严格"第一"，多来源交叉验证 |
| **年份标注** | 标题标"理论 (1905)" | 写作年 ≠ 发表年，标题不标无法确认的年份 |
| **理论归属过度** | "独自发明 X" | 查清共同贡献者（如 Wilson 重整化群有 Kadanoff 思想源头） |
| **伪引语（最危险）** | 中文引号内"物理学家原话" | 无原文不加引号，用间接引语 |
| **伪精确数字** | "已精确到小数点后 X 位" | 随时间变化的数字不固定 |
| **人物时间线** | "后来被 X 发展"但 X 其实更早 | 核实每个引用人物生卒年 |
| **现代语言包装历史人物** | 用"规范场论""重整化群"包装 19 世纪物理 | "今天我们称之为…""为后来…奠定基础" |
| **奖项归属** | "诺贝尔奖表彰 X" | 核对官方获奖理由原文（如 Wilson 是"相变相关的临界现象"而非泛泛"重整化群"） |

---

## 九、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆实例 Beamer 源码 |
| `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 标杆实例人物专属提示词 |
| `20th_century/Kenneth_G_Wilson/Makefile` | 编译/出图/视频 Makefile 模板 |
| `cover/openphysicist_page.tex` | 项目首页模板（统一 `\input`） |
| `20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `../../mathematician/presentations/Mathematician_Biography_Guide.md` | 数学家立传指南（背景音乐/Review/告警检测的完整母本） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
