# 高斯基准立传模板（OpenMath 数学家立传标准）

> 基于 **Carl Friedrich Gauss（Q6722）** 的立传全过程沉淀，作为后续所有数学家立传的**标准模板**。
> 使用方式：复制本文档骨架，把 `{{占位符}}` 替换为对应数学家的实际值即可。
> 数据源约定：本地 Wikipedia 存档位于 `presentations/{century}/pages/{Full_Name}/`（含 `page.md` + `metadata.json` + `page.html` + `images.txt`），立传时直接引用，不再重新下载。

---

## 一、目录结构与数据源

```
mathematician/presentations/
├── {century}/                     ← 19th_century / 20th_century / ancient_chinese 等
│   ├── {century}_Mathematicians.md            ← 本世纪收录清单（含立传/Review 标志位）
│   ├── pages/{Full_Name}/                     ← ★ 本地 Wikipedia 权威数据源
│   │   ├── page.md        ← 可读正文 + frontmatter（生卒/国籍/领域/获奖/导师）
│   │   ├── page.html      ← 原始 HTML 备份
│   │   ├── metadata.json  ← Wikidata 结构化字段（qid、日期、关系、获奖）
│   │   └── images.txt     ← 页面图片 URL 清单
│   └── {Full_Name}/                          ← 立传成品目录
│       ├── {Full_Name}_zh.md   ← 立传提示词（本文档骨架的实例化）
│       ├── {Full_Name}_zh.tex  ← Beamer 源码
│       ├── Makefile             ← 编译/视频（含 BGM 机制）
│       ├── images/              ← 头像等图片
│       ├── output/              ← 渲染预览 PNG
│       └── *.wav / bgm.wav      ← 背景音乐（不入 git）
└── Gauss_Biography_Template.md  ← 本文档
```

**音乐库**（与 presentations 同级）：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`，选曲必读 `curated_tracks.md`。

---

## 二、提示词模板骨架（`{Full_Name}_zh.md`）

> 高斯提示词 `Carl_Friedrich_Gauss_zh.md` 的章节结构，逐节替换即可。完整章节如下：

### 头部元信息块

```markdown
# {{中文全名}}（{{英文全名}}）立传提示词

> qid={{QID}} · {{出生日期}} – {{逝世日期}} · {{国籍}}数学家/物理学家 · {{世纪}}
> 本地 Wikipedia 数据源：`mathematician/presentations/{{century}}/pages/{{Full_Name}}/`（page.md + metadata.json + images.txt）
```

### §0 正文形式说明（参考物理学家 Kenneth G. Wilson，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（无头像则用 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍，底部状态栏给出「国籍 | 机构 | 主要成就」三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前，左头像 + 右信息网格（生卒/本名/国籍/出生地/师承/教育/主要荣誉/核心领域）。
4. **配色 + 气泡背景**：主色 + 强调色 + 三~四分类色；背景用柔和气泡（稀疏大块实心圆）。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### §1 背景信息（用于 Slide 1–3）

- **全名 / 拉丁名 / 中文惯称 / 尊称**
- **生卒**（精确到日，含享年、死因）
- **国籍**（按当时所在实体写，注明演变路径，如「莱茵邦联 → 汉诺威王国 → 现代对应德国」）
- **身份**（数学家/物理学家/统计学家等）
- **家庭**（出身、父母、婚姻、子女）
- **教育轨迹**（按时间线：就读院校 + 年份 + 学位）
- **导师**（博士导师）
- **研究领域**（列表）

### §2 核心叙事亮点（用于 Slide 4–9，约 10–13 条）

按时间线组织，每条标注年份 + 一句「贡献 + 影响」。示例（高斯）：

1. 神童轶事（1+2+…+100，注明「传说」）
2. 正十七边形（1796，19 岁）
3. 《算术研究》（1801）
4. 代数基本定理（第二、三个完整证明）
5. 谷神星与最小二乘法（1801，先于 Legendre）
6. 高斯曲率与绝妙定理（1827）
7. 非欧几何（首发现未发表）
8. 正态分布（1809）
9. 地磁学与物理（1832 绝对测量、1833 电磁电报、1821 回照器）
10. 快速傅里叶变换（早于 Cooley–Tukey 约 160 年）
11. 其他标志性工作
12. 「不发表不完整的作品」（印章 Pauca sed matura）
13. 荣誉与学生

### §3 配色方案（Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色 | `#XXXXXX` | 人物气质/地域 |
| 强调色 | `#XXXXXX` | 尊崇/称号 |
| 分类色 1 | `#XXXXXX` | 领域 A |
| 分类色 2 | `#XXXXXX` | 领域 B |
| 分类色 3 | `#XXXXXX` | 领域 C |
| 分类色 4 | `#XXXXXX` | 遗产/其他 |
| 背景 | `#XXXXXX` | 浅色底 |

（高斯基准：主色普鲁士深蓝 `#1F3A93` + 强调数学金 `#C9A227` + 数论靛蓝 `#4C5FD5` + 几何青绿 `#0E7C7B` + 天文琥珀 `#E07B30` + 遗产石版灰 `#4A5568`，背景 `#F7F6F9`）

### §3.5 背景音乐选择（★ 人物专属）

- **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`，详见 `curated_tracks.md`
- **风格定调**：一句话（如高斯「古典庄严 / 宏大理性」）
- **匹配理由**：2–3 条
- **候选方向**：首选/备选风格 + 时长要求（≥ 页数 × 7 秒 ≈ N 秒，ffmpeg `-shortest` 自动对齐）

### §4 Slide 规划（约 12 页，Wilson 式结构）

1. 封面（`\titleslide`）
2. 身份信息页（`\profileslide`，★ 必做）
3. 核心贡献概览（`\hookslide`）
4. 神童与早年
5–10. 核心贡献页（按领域拆分）
11. 荣誉与传承
12. 终章

### §5 史实陷阱与敏感点（终审必须检查，逐条列出）

### §6 数据库字段核对表（见本文档 §七）

### §7 社会关系入库清单（见工作指南 §二十）

### §8 奖项清单 / §9 机构清单

### §10 终审清单（checkbox 形式）

### §11 Review 流程规范（两轮）

---

## 三、Beamer tex 版式规范

### 3.1 preamble 骨架（可直接复制）

```latex
\documentclass[aspectratio=169,14pt]{beamer}
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{\hfill{\scriptsize\color{covermuted}\insertframenumber/\inserttotalframenumber}\hspace{0.4cm}\vspace{0.15cm}}
\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold, ItalicFont=PingFang SC]
\setCJKsansfont{PingFang SC}[BoldFont=PingFang SC Semibold, ItalicFont=PingFang SC]
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{fix-cm}\usepackage{adjustbox}\usepackage{fontawesome5}
\usepackage{amsmath}\usepackage{amssymb}
\usepackage{booktabs}\usepackage{tabularx}\usepackage{array}\usepackage{colortbl}
\usetikzlibrary{positioning,calc,arrows.meta,shadows}
\graphicspath{{images/}}
\renewcommand{\tabularxcolumn}[1]{m{#1}}
```

### 3.2 配色变量命名规范

| 变量 | 用途 |
|---|---|
| `bgmain` | 整篇底色 |
| `{主色}`（如 `prussiablue`） | 标题、主文本、表头 |
| `{强调色}`（如 `mathgold`） | 分隔线、点缀、第一列 |
| `badgeNumber` / `badgeGeometry` / `badgeAstro` / `badgeLegacy` | 分类色（按人物领域重命名） |
| `coverdark` / `covermuted` / `titlecolor` / `muteddark` | 文本层级 |
| `numberpanel` / `geometrypanel` / `astropanel` / `legacypanel` | 分类面板底色 |
| `goldpanel` / `graypanel` | 强调/中性面板 |

### 3.3 三个核心宏（★ 所有页面复用）

```latex
% 底部装饰线
\newcommand{\plainbar}{% ... 底部细横线 + 金色分隔线 ... }

% 封面/结尾气泡背景
\newcommand{\deckbackground}{% ... 稀疏大块实心圆 + 底部线 ... }

% 统一样式的标题区
\newcommand{\sectiontitle}[2]{%
\vspace{-0.52cm}
\begin{center}
  {\fontsize{20}{24}\selectfont\bfseries\color{titlecolor} #1}\\[2pt]
  {\fontsize{7.5}{9.5}\selectfont\itshape\color{muteddark} #2}
\end{center}
\vspace{0.06cm}
}
```

---

## 四、核心设计模式（★ 高斯版式的精髓）

### 4.1 表格语义化设计（核心贡献页通用）

每页用 `tabularx` 三列表格，**列头按页面主题语义化**，第一列加粗、用强调色：

| 页面主题 | 列头示例 |
|---|---|
| 数论 | `问题 ｜ 高斯的工作 ｜ 后来影响` |
| 代数 | `年份 ｜ 证明 ｜ 特点` |
| 天文/最小二乘 | `问题 ｜ 方法 ｜ 结果` |
| 概率 | `概念 ｜ 高斯的贡献 ｜ 今天` |
| 几何 | `概念 ｜ 高斯发现 ｜ 突破` |
| 大地测量 | `任务 ｜ 工具 ｜ 成果` |
| 地磁 | `研究问题 ｜ 实验/方法 ｜ 贡献` |
| 非欧几何 | `人物 ｜ 观点 ｜ 结果` |

**通用模式**：`{实体/概念/年份} ｜ {该人物做了什么} ｜ {影响/结果/今天}`

表格骨架（含配色）：

```latex
\begin{tabularx}{12.4cm}{>{\bfseries\scriptsize}m{4.4cm}|>{\scriptsize}X|>{\scriptsize}X}
\toprule
\rowcolor{prussiablue}\multicolumn{1}{c|}{\footnotesize\color{white}\textbf{列1}} &
  \multicolumn{1}{c|}{\footnotesize\color{white}\textbf{列2}} &
  \multicolumn{1}{c}{\footnotesize\color{white}\textbf{列3}} \\
\midrule
\cellcolor{goldpanel}\textcolor{mathgold!88!black}{第一列内容} &
  \cellcolor{numberpanel}\textcolor{badgeNumber!82!black}{第二列内容} &
  \cellcolor{geometrypanel}\textcolor{badgeGeometry!82!black}{第三列内容} \\
\midrule
... （重复，每行间 \midrule）
\bottomrule
\end{tabularx}
```

### 4.2 公式展示框（★ 高斯版式的标志性元素）

在表格下方展示核心数学公式，用金色边框 + 浅金底：

```latex
\begin{center}
\fcolorbox{mathgold!70}{goldpanel}{%
  \begin{minipage}{11.7cm}
  \centering
  {\fontsize{9}{12}\selectfont\bfseries\color{mathgold!85!black} {{公式标题（含年份）}}}\\[2pt]
  {\fontsize{11}{14}\selectfont\color{prussiablue!88!black}${{公式内容}}$}
  \end{minipage}%
}
\end{center}
```

**要点**：
- 长公式用 `\resizebox{11.4cm}{!}` 自动缩放单行；复杂多行用 `\begin{aligned}` / `\begin{cases}` / `\begin{vmatrix}`
- 标题含年份与出处（如「二次互反律（Gauss，1796；1801 年系统阐述）」）
- 公式框通常**替换**页底金句（公式即是最好的具象化）

### 4.3 年份标注模式

| 场景 | 写法 | 示例 |
|---|---|---|
| 单年 | `（YYYY）` 或 `YYYY：` | `曲率（1827）`、`1795：同余如何系统表达？` |
| 区间 | `YYYY–YYYY` | `1795–1801：二次剩余如何判断？` |
| 约略 | `约 YYYY` | `约 1792：素数分布猜想` |
| 年代 | `YYYYs` | `1820s` |
| 发现 vs 发表 | 分开标注 | `约 1795；1809 年发表` |

### 4.4 溢出修复策略（★ 每写一页就 make，看到溢出就修）

优先级从轻到重：
1. 删装饰元素（`\plainbar` / `\deckbackground`）
2. 缩 `inner sep` / `\arraystretch`
3. 缩字号
4. 减空行间距（`\\[3pt]` → `\\[1pt]`）
5. 增大顶部负间距（`\vspace{-0.45cm}` → `-0.9cm`）或公式框前负间距
6. 最后才调 TikZ 坐标

**验收标准**：`Overfull \vbox > 10pt` 必须修复；`\hbox > 50pt` 必须修复；`< 5pt` 可忽略。

---

## 五、背景音乐机制（★ Makefile 已内置，只需放文件）

- Makefile 中 `BGM = $(wildcard *.wav)`，`make video` 时自动检测并混入。
- **推荐用软链接**（不复制大文件）：

```bash
cd presentations/{century}/{Full_Name}
ln -sf /Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/{分类}/{曲目}.wav ./bgm.wav
```

- 视频时长自动对齐（`ffmpeg -stream_loop -1 ... -shortest`）。
- 选曲原则：音乐气质匹配数学家气质（见 `curated_tracks.md` 按气质推荐表，如「古典庄严」→ Beethoven Karajan）。

---

## 六、史实审查要点（★ 通用红线 + 人物专属）

### 6.1 通用红线（任何数学家适用）

| 绝对不要 | 正确做法 |
|---|---|
| 中文引号内写数学家「原话」 | 间接引语；有原文才加引号 |
| 声称「第一次/第一个」 | 「核心贡献」「里程碑式成就」 |
| 标题中标注无法确认的年份 | 年份放正文，标题保留核心概念 |
| 固定写具体计算验证数字 | 「大量」「持续推进的」 |
| 「只有 N 篇论文」 | 「十余篇奠基性工作」「主要著作」 |
| 用 21 世纪术语包装早期数学家 | 「今天我们称之为…」「为后来…奠定基础」 |

### 6.2 人物专属陷阱（从 §5 提取，逐条终审）

以高斯为例的典型陷阱：
- **优先权**：「Gauss 先发现、Legendre 先发表」（最小二乘）——勿写 Gauss 发表了最小二乘。
- **未发表**：「非欧几何 Gauss 首发现未发表、Bolyai/Lobachevsky 独立发表」。
- **证明次序**：「代数基本定理第二、三个完整证明」——勿写第一个。
- **轶事标注**：1+100 是「传说（apocryphal）」。
- **学位机构**：博士机构 vs 常被误写的机构（高斯 Helmstedt，非哥廷根）。
- **国籍**：按当时所在实体，现代对应「德国」。

---

## 七、数据库入库字段（★ 立传并行推进）

> 详见 `Mathematician_Biography_Guide.md` §二十（社会关系）与 §二十一（全字段）。立传时需梳理并入库：

| 表 | 字段 | 数据来源 |
|---|---|---|
| `people` | qid / name_en / name_zh / 生卒 / description / primary_occupation / has_biography | metadata.json |
| `person_occupation` | 职业（rank 排序） | metadata.json |
| `person_field` | 研究领域（rank 排序） | metadata.json `field_of_work` |
| `award_laureate` | 获奖记录（year 必填，全部收录） | metadata.json `award_received` + page.md |
| `person_institution` | 教育/任职机构（relation + 起止年） | metadata.json `educated_at`/`employer` |
| `person_nationality` | 国籍（历史政权用 successor 归并） | metadata.json `nationality` |
| `person_relation` | 社会关系（师/生/同事/对手/争议/并称） | metadata.json + page.md |
| `rankings` | 榜单状态联动 | 排名文件 |

缺失人物先建占位（`has_biography=0`），全部 `INSERT IGNORE` 幂等。

---

## 八、Review 流程（两轮）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读 `pages/{Full_Name}/page.md` 建立事实基准，逐页对照 tex
- [ ] 头像、国籍、引语核对
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回提示词

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家格式对齐

---

## 九、快速启动清单（从零到成品）

```
第 0 步：确认 pages/{Full_Name}/ 数据源存在（page.md + metadata.json）
第 1 步：复制本文档骨架 → {Full_Name}_zh.md，替换 {{占位符}}
第 2 步：建目录 presentations/{century}/{Full_Name}/，复制 Makefile 改 MAIN
第 3 步：收集头像（images.txt 选标准肖像）
第 4 步：设计配色（反映人物气质，与已有人物区分）
第 5 步：写 tex（preamble 骨架 → 三个核心宏 → 逐页 slide）
第 6 步：每写一页就 make，看到溢出就修（§4.4）
第 7 步：核心贡献页用表格语义化 + 公式框（§4.1 / §4.2）
第 8 步：背景音乐软链接（§五）
第 9 步：数据库入库（§七）+ 社会关系（工作指南 §二十）
第 10 步：两轮 Review（§八）
第 11 步：make images → make video
```

---

> **核心心法**：为数学家立传 = 「史实精修 + 数学深化」的迭代。第一版必然有错，关键是建立严谨核查流程。**写完不是终点，终审才是。**
