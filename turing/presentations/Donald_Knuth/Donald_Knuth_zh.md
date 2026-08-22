# 图灵奖得主立传提示词（人物实例：Donald E. Knuth）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」首个人物实例**，以 Donald E. Knuth（高德纳，1974 图灵奖，算法分析与计算机排版奠基人）为样板。
> 格式对标物理学家侧标杆 Kenneth G. Wilson（`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`）与化学家侧标杆 Frederick Sanger（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`），并融合图灵奖通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用到任何图灵奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson 的提示词 + tex 结构）与化学家侧标杆（Frederick Sanger）。
- **本实例**：Donald Ervin Knuth（唐纳德·欧文·克努特，中文常译「高德纳」，1938-01-10 生于美国威斯康星州密尔沃基，在世）。
- **设计哲学**：图灵奖得主立传与数学家立传的核心差异，在于**图灵奖得主必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达；图灵奖得主的「贡献」常表现为**算法、语言、系统、理论**而非「定理」——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标得主**：Donald Ervin Knuth（1938-01-10 ~ ，享年待定，截至资料基准日在世）
- **气质关键词**：**算法分析之父、计算机程序设计艺术（TAOCP）的作者、TeX 排版系统的创造者、"程序即文学"的信徒、极度严谨的完美主义者** —— 1974 图灵奖获奖理由（ACM 官方措辞，需以 `amturing.acm.org` 为准再核实）：
  > "for his major contributions to the analysis of algorithms and the design of programming languages, and in particular for his contributions to 'The Art of Computer Programming'"（因其对算法分析与编程语言设计的重大贡献，尤其是对《计算机程序设计艺术》的贡献）
- **设计母题**：**算法之美 / 排版艺术（The Art）**。Knuth 毕生追求「程序的正确性与美感」——TAOCP 把算法当成艺术来写，TeX 把排版当成科学来做（TeX 版本号趋近 π、Metafont 版本号趋近 e 的细节，正是这种「追求完美」的隐喻）。视觉语言：排版网格、字母与符号（TeX/Computer Modern 字体）、算法的伪代码行、分形的递归结构。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/1974/Donald Knuth/index.html`（246 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/1974/Donald Knuth/metadata.json`（简化字段：title/url/year/image_count）
  - 头像：`turing/pages/1974/Donald Knuth/images/250px-Donald_Ervin_Knuth_cropped_.jpg`（infobox 肖像，可直接复制）
- **参考模板**：
  - 图灵奖通用模板：`turing/presentations/Turing_Bio_Prompt_Template.md`
  - 化学家标杆提示词：`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 图灵奖现有版式参考：`turing/video/episode-00-what-is-turing-award/turing_ep00_zh.tex`（图灵紫配色）
  - 项目首页模板：`turing/presentations/cover/openturing_page.tex`（待创建，统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/1974/Donald Knuth/index.html`（含 infobox + 正文）与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/1974/Donald Knuth/images/250px-Donald_Ervin_Knuth_cropped_.jpg`（Wikipedia infobox 肖像，2011 年拍摄）
- 提取 infobox 与正文，输出供校验（**事实基准如下**）：
  - 生卒日期（1938-01-10 生于威斯康星州密尔沃基 Milwaukee, Wisconsin，在世）
  - 国籍（美国）；父母（父 Ervin Henry Knuth 经营小型印刷厂并教簿记；母 Louise Marie Bohning）
  - 教育（Milwaukee Lutheran High School → Case Institute of Technology 物理奖学金入学后转数学，1960 同时获 BS + MS → Caltech PhD 1963）
  - 博士导师（Marshall Hall, Jr.）；博士论文《Finite Semifields and Projective Planes》(1963)
  - 配偶（Nancy Jill Carter）；子女 2 人
  - 主要任职（Caltech 助理教授 1963 → Stanford 教授 1968 至今，名誉教授；曾为 Burroughs 顾问）
  - 关键荣誉（Turing 1974 · Grace Murray Hopper 1971 · National Medal of Science 1979 · Kyoto 1996 · von Neumann Medal 1995 · Harvey 1995 · NAS 院士 1975 · 英国皇家学会外籍院士 2003 · Faraday 2011 · BBVA 2010）
  - 知名博士生（Leonidas J. Guibas、Michael Fredman、Scott Kim、Vaughan Pratt、Robert Sedgewick、Jeffrey Vitter、Andrei Broder）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 个节点，见第 6 步）

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Donald_Knuth/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆实例的 `Makefile`（可先从物理学家 `Kenneth_G_Wilson/Makefile` 复制），设置 `MAIN=Donald_Knuth_zh`、`VIDEO_NAME=Donald_Knuth_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 复制 `turing/pages/1974/Donald Knuth/images/250px-Donald_Ervin_Knuth_cropped_.jpg` 到 `presentations/Donald_Knuth/images/Knuth.jpg`

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Knuth 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | analysis of algorithms | 算法分析 | 计算复杂度的严格分析，Big O 记号推广，1974 图灵奖核心 | 封面、核心页 |
| 1 | computer typesetting | 计算机排版 | TeX / METAFONT / Computer Modern | 排版页 |
| 2 | programming languages | 编程语言 | 编程语言设计、LR 分析、编译器 | 语言页 |
| 3 | theoretical computer science | 理论计算机科学 | 组合数学、算法理论、文学编程 | 理论页 |

#### 4.1 入库操作

> 参照化学家标杆 Sanger 的入库脚本 `MySQL/seed_sanger_full.py`（人物主记录 + 研究领域）模式执行。

- 新建/更新 `people` 主记录（`name_en='Donald Knuth'`），设置 `primary_occupation='computer scientist'`、`has_biography=1`、`has_social_data=1`（补齐 qid/gender/birth_date/description）
- 关联职业 `computer scientist`（rank 0）、`mathematician`（rank 1，因 Knuth 亦有数学贡献）
- 国籍 `United States`
- 将 4 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 生成入库脚本 `MySQL/seed_knuth_full.py` 并执行，脚本末尾输出校验结果（研究领域 / 国籍 / 职业 / `person_field` 总数）

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Marshall Hall, Jr. | 师→生（博士导师） | Caltech 数学导师 |

**门生（Knuth → 学生，源自本地 Wikipedia infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Sedgewick | Knuth → 学生 | 《算法》作者 |
| advisor-student | Leonidas J. Guibas | Knuth → 学生 | 计算几何 |
| advisor-student | Vaughan Pratt | Knuth → 学生 | Pratt 解析、KMP 合作者 |
| advisor-student | Michael Fredman | Knuth → 学生 | 斐波那契堆 |
| advisor-student | Jeffrey Vitter | Knuth → 学生 | 外部存储算法 |
| advisor-student | Scott Kim | Knuth → 学生 | 字体设计 |
| advisor-student | Andrei Broder | Knuth → 学生 | 信息检索 |

> 说明：Knuth 无「共同得主」（1974 年独享图灵奖）；无 spouse 入库需求（可选）。

#### 4.5.1 社会关系入库操作（★ 必做，写入 greatminds 库 MySQL）

> 参照化学家标杆 Sanger 的入库脚本 `MySQL/seed_sanger_relations.py`（社会关系）模式执行。

- 将上表 8 条关系（1 位导师 + 7 位门生）写入 `person_relation`（`from_id` / `to_id` / `relation_type` / `note` / `source`），`source` 记 `'立传-Donald_Knuth'`
- **方向处理**：`advisor-student` 有向——导师 Marshall Hall 为 `from_id`（Hall → Knuth）、门生为 `to_id`（Knuth → 学生）
- 不在库中的关联人物（Hall 及 7 位门生）先建占位记录（`has_biography=0`、`primary_occupation='computer scientist'`），关系 `note` 加 `[材料待展开] ` 前缀
- 生成入库脚本 `MySQL/seed_knuth_relations.py` 并执行，脚本末尾输出校验结果（新建人物数 / 新增关系数 / `person_relation` 总数）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：严谨、完美主义、算法与排版的双重艺术
- **配色**：图灵紫（OpenTuring 品牌主色）+ 强调红 + 四分类色
  - `badgeAlg` 算法分析 — 蓝 `#2E5A9E`
  - `badgeType` 计算机排版 — 琥珀 `#D9A441`
  - `badgeLang` 编程语言 — 青绿 `#1E8E8E`
  - `badgeTheory` 理论计算机 — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「算法 / 排版」——以离散圆点暗示程序指令与排版字符的节奏感

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自本地 `index.html` infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenTuring`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 算法分析之父 / Donald Knuth 1938– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 算法分析 / 计算机排版 / 编程语言 / 理论计算机科学
04  早年：密尔沃基少年 (1938–1956) — 印刷厂、单词比赛、路德宗德裔
05  Case：从物理到数学 (1956–1960) — IBM 650、篮球程序、双学位
06  Caltech 博士：Marshall Hall 门下 (1960–1963) — 有限半域与射影平面
07  TAOCP：计算机程序设计艺术 (1962–) — 一部未完的史诗
08  算法分析：Big O 与计算复杂度（核心贡献页）
09  TeX：排版的艺术 (1977–) — 版本号趋近 π
10  文学编程：WEB / CWEB — 程序即文学
11  以 Knuth 命名的成果 — KMP / Knuth–Bendix / up-arrow / LR
12  门生与传承 — Sedgewick、Guibas、Pratt
13  荣誉 — Turing 1974 · National Medal 1979 · Kyoto 1996
14  反对软件专利：程序员的立场
15  遗产：程序即文学
16  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照通用模板 `\profileslide`。
- 头部宏定义（图灵紫配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）整体复用 `turing/video/episode-00-what-is-turing-award/turing_ep00_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Knuth 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 图灵奖理由 | 官方措辞强调 "analysis of algorithms" 与 "design of programming languages"，以及 "The Art of Computer Programming"；勿写成泛泛的"发明 TeX"——TeX 是 1977 年后才开始，**不是 1974 获奖原因** |
| "算法分析之父" | 称号是 "father of the analysis of algorithms"，勿写成"计算机科学之父"（后者是 Alan Turing） |
| Big O 记号 | Knuth **推广/系统化**了渐近记号（asymptotic notation），但记号本身源于 Bachmann/Landau，勿写成"发明 Big O" |
| KMP 算法 | 是 Knuth–Morris–Pratt 三人共同成果，勿写成 Knuth 独有 |
| Knuth–Bendix | 是 Knuth 与 Peter Bendix 共同，勿遗漏合作者 |
| TeX 的动机 | Knuth 因对 TAOCP 第二版校样的排版质量不满，暂停写书去开发 TeX（1977–），勿写成"为赚钱/商业" |
| 教育经历 | Case Institute 是**物理奖学金**入学，后转数学，勿只写"数学专业"；1960 年因成绩特别优异同时获 BS + MS |
| 生卒表述 | Knuth 仍在世，生卒年写作 `1938–`，勿写成已故 |
| 版本号趣味 | TeX 版本号趋近 π、Metafont 版本号趋近 e，属趣味细节，勿写成"版本号等于 π" |
| 反对软件专利 | 是 Knuth 的公开立场，可客观陈述，勿过度政治化 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| analysis of algorithms | 算法分析 | 与"计算复杂度"关联 |
| The Art of Computer Programming (TAOCP) | 计算机程序设计艺术 | 多卷本，未完结 |
| TeX | TeX 排版系统 | 读音 /tɛx/，勿写成"Tex" |
| METAFONT | METAFONT 字体定义语言 | 与 TeX 配套 |
| Computer Modern | Computer Modern 字体 | TeX 默认字体 |
| Big O notation | 大 O 记号 / 渐近记号 | Knuth 推广非发明 |
| literate programming | 文学编程 | WEB / CWEB |
| LR parser | LR 分析器 | Knuth 1965 提出 |
| Knuth–Morris–Pratt algorithm | KMP 算法 | 三人共同 |
| Knuth–Bendix completion algorithm | Knuth–Bendix 完备化算法 | 与 Bendix 共同 |
| up-arrow notation | 上箭头记号 | 大数表示 |
| MIX / MMIX | MIX / MMIX 指令集架构 | TAOCP 教学用 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions（沉稳 / 纪录片 / 长期纲领，与化学家标杆 Sanger 同款）
- **风格**: 沉稳 / 纪录片 / 严谨的长期主义
- **匹配理由**:
  - "长期纲领" 匹配 Knuth 贡献的本质——TAOCP 自 1962 年动笔至今未完结，TeX 为排版质量投入十年（1977–1986），是一以贯之的「把程序与排版都做成艺术」的纲领
  - "沉稳" 匹配其气质——极度严谨、完美主义，自述 "Premature optimization is the root of all evil"（过早优化是万恶之源）的理性克制
  - "纪录片" 匹配传记叙事——密尔沃基少年 → Case 转数学 → Caltech 博士 → TAOCP → 图灵奖 → TeX → 文学编程，是思想的演进而非英雄史诗
- **备选** (未采用):
  - ★★ PAST — "历史感/深沉" 匹配计算机科学奠基背景，但沉稳感略弱于 Timeless
  - ★★ The Flow of Time — "时间感/纪录片" 匹配算法分析的时间隐喻，但受众偏低
  - ★ Eternals — "宏大/深远" 匹配 TAOCP 的史诗气质，但受众偏低
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `turing/presentations/Donald_Knuth/Timeless.wav`
- **时长**: 128 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/1974/Donald Knuth/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/1974/Donald Knuth/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（待创建） |
| `turing/video/episode-00-what-is-turing-award/turing_ep00_zh.tex` | 图灵奖版式（图灵紫配色）参考 |
| `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.tex` | 化学家标杆成品参考 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 物理学家标杆成品参考 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
