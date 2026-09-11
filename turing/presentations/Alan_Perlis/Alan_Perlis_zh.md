# 图灵奖得主立传提示词（人物实例：Alan Perlis）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」实例**，以 Alan Perlis（艾伦·佩利斯，1966 图灵奖、**首届得主**）为样板。
> 参照标杆实例 Donald E. Knuth（`Donald_Knuth/Donald_Knuth_zh.md`）与通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用到任何图灵奖得主；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Alan Jay Perlis（艾伦·杰伊·佩利斯，1922-04-01 生于宾夕法尼亚州匹兹堡，1990-02-07 逝于康涅狄格州纽黑文，享年 67）。**1966 年首届图灵奖得主**。
- **设计哲学**：图灵奖得主必须有「身份信息页」，贡献表现为**编程语言 / 编译器 / 学科建制**而非定理——Perlis 是"计算机科学作为独立学科"的奠基者之一，气质为**先驱 / 建制 / 语言**。

---

## 二、背景信息 【人物专属】

- **目标得主**：Alan Jay Perlis（1922-04-01 ~ 1990-02-07，已故）
- **气质关键词**：**ALGOL 主要推动者、IT（Internal Translator）编译器、编程语言教学先驱、Epigrams on Programming、计算机科学学科建制者** —— 1966 图灵奖官方措辞（ACM）："for his influence in the area of advanced programming techniques and compiler construction"（先进编程技术与编译器构造领域的影响力）。
- **设计母题**：**语言 / 编译器 / 学科建制**——首届图灵奖的"开创"母题。视觉语言：泡泡背景（稀疏大块实心圆）；配色用图灵紫主色 + 四分类色（编程语言 / 编译器 / 学科建制 / 编程思想）。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/1966/Alan Perlis/index.html`（38 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/1966/Alan Perlis/metadata.json`
  - 头像：`turing/pages/1966/Alan Perlis/images/Alan_Perlis.jpg`（已复制到 `presentations/Alan_Perlis/images/Perlis.jpg`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/1966/Alan Perlis/index.html` 与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/1966/Alan Perlis/images/Alan_Perlis.jpg`
- **事实基准**（全部取自本地 index.html infobox 与正文）：
  - **生卒**：1922-04-01 生于宾夕法尼亚州匹兹堡（Pittsburgh, Pennsylvania）；1990-02-07 逝于康涅狄格州纽黑文（New Haven, Connecticut），享年 67
  - **本名**：Alan Jay Perlis；国籍：美国；犹太家庭出身
  - **教育**：
    - 1939 年 Taylor Allderdice High School 毕业
    - 1943 年 Carnegie Institute of Technology（后改名 Carnegie Mellon University）**化学**学士
    - 二战期间服役于美国陆军，对数学产生兴趣
    - 1949 年 MIT **数学**硕士、1950 年 MIT **数学**博士；博士论文 *On Integral Equations, Their Solution by Iteration and Analytic Continuation*（导师 **Philip Franklin**）
  - **任职**：
    - Purdue University 任教（1952 加入，参与 Project Whirlwind）
    - 1956 年转入 Carnegie Institute of Technology，任数学系主任，后成为**计算机科学系首任主任**
    - 1962 年当选 ACM 主席（president of ACM）
    - 1971 年转入 Yale University，任计算机科学讲座教授（Eugene Higgins 讲座）；1977 年当选美国国家工程院（NAE）院士；在 Yale 直至 1990 年去世
  - **核心成就（infobox Known for）**：IT（Internal Translator）、ALGOL、APL
  - **关键事实**：
    - **1966 年首届（inaugural）图灵奖得主**，ACM 颁奖词 "for his influence in the area of advanced programming techniques and compiler construction"
    - IT（Internal Translator，1956）被 **Donald Knuth** 称为"第一个成功的编译器"（the first successful compiler）
    - 作为团队一员参与开发编程语言 **ALGOL**（ALGOL 58 / ALGOL 60）
    - 1982 年在 ACM SIGPLAN Notices 17(9) 发表 **"Epigrams on Programming"**，广被引用的编程格言集；其中 epigram #54 创造了术语 **"Turing tarpit"**（图灵焦油坑：一切皆可能，但有趣之事皆不易）
    - 1957 与 J. W. Smith、H. R. Van Zoeren 合著 *Internal Translator (IT): A Compiler for the 650*
    - 知名博士生：Zohar Manna、David Parnas、Gary Lindstrom、John R. Levine
  - **荣誉（infobox Awards）**：Turing Award 1966 · Computer Pioneer Award 1985

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Alan_Perlis/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Donald_Knuth/Makefile`（标杆实例），设置 `MAIN=Alan_Perlis_zh`、`VIDEO_NAME=Alan_Perlis_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 复制 `turing/pages/1966/Alan Perlis/images/Alan_Perlis.jpg` 到 `presentations/Alan_Perlis/images/Perlis.jpg`

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | programming languages | 编程语言 | ALGOL（主要推动者）、APL、IT |
| 1 | compilers | 编译器 | Internal Translator（IT，1956，首个成功编译器） |
| 2 | computer science discipline | 计算机科学学科建制 | 卡内基梅隆计算机科学系首任主任、ACM 主席 |
| 3 | programming methodology | 编程方法论 | Epigrams on Programming、编程语言教学 |

- 入库脚本：`MySQL/seed_perlis_full.py`（people 新建 id，4 领域 + 国籍 + 职业）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Philip Franklin | 师→生 | 博士导师，MIT（数学） |
| colleague | Donald Knuth | 无向 | Knuth 称 IT 为"第一个成功的编译器"；同属编程语言/编译器领域 |
| doctoral-student | Zohar Manna | 师→生 | 知名博士生（程序验证） |
| doctoral-student | David Parnas | 师→生 | 知名博士生（软件工程） |
| co-honored-era | 图灵奖得主序列 | 无向 | 1966 首届得主（与后续同列） |

- 入库脚本：`MySQL/seed_perlis_relations.py`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：先驱 / 建制 / 语言（首届图灵奖的"开创"母题）
- **配色**：图灵紫（品牌主色）+ 强调红 + 四分类色
  - `badgeLang` 编程语言 — 青绿 `#1E8E8E`
  - `badgeCompiler` 编译器 — 蓝 `#2E5A9E`
  - `badgeDiscipline` 学科建制 — 琥珀 `#D9A441`
  - `badgeMethod` 编程方法论 — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡（稀疏大块实心圆），呼应"开创"叙事

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。✅
2. **封面有国籍**：底部状态栏 `美国 | Carnegie Mellon · Yale · Purdue · ACM | Turing 1966（首届）`。✅
3. **必须有身份信息页**：封面之后第 3 页，左头像 + 右 2×2 信息网格（含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。✅
4. **品牌口径统一**：结尾页底部写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承。✅

### 5.2 背景音乐 【人物专属】

- **气质定位**：先驱 / 建制（首届图灵奖、计算机科学学科奠基）—— 史诗 / 开阔。
- **选定曲目**：Alex-Productions **New Lands**（史诗 / 开阔，匹配"改写计算机史的开创"叙事），与 Knuth 标杆同曲。
- **落地文件**：`turing/presentations/Alan_Perlis/NewLands.wav`（复制自音乐库，不入 git）。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 主标题「艾伦·佩利斯」+ 英文名/生卒 + 四色 badge + 右上头像 + 国籍行（标注"1966 首届图灵奖"）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 编程语言/编译器/学科建制/编程方法论
04  早年：匹兹堡的化学少年与战时转向数学 (1922–1943)
05  MIT 的数学博士与编译器萌芽 (1943–1952)
06  Project Whirlwind 与 Purdue 岁月
07  IT（Internal Translator）：被 Knuth 称为首个成功编译器
08  ALGOL：让世界拥有第一种结构化算法语言
09  卡内基梅隆：计算机科学作为一门独立学科
10  ACM 主席与学科建制者
11  Yale 岁月与"编程格言集"（Epigrams on Programming）
12  荣誉与遗产：图灵焦油坑的命名者
13  结尾 — "计算机科学不是关于计算机，就像天文学不是关于望远镜"
14  彩蛋 — 本页由 XeLaTeX + Beamer 排版
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；四分类色与 `\plainbar`/`\deckbackground`/`\sectiontitle`/`\lab` 复用 Knuth/Thompson 标杆骨架。
- ⚠ 注意：命令名不能含"字母+数字+字母"歧义（如 `\\plan9slide` 会解析失败），应写作 `\\planNslide`。

### 第 8 步：布局检查 【模板通用】

- `make distclean && make` 返回 EXIT=0，15–17 页，无缺字、无致命溢出（仅 ≤9.53pt 轻微 Overfull，可接受）。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Perlis 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 首届得主 | 1966 是**首届（inaugural）**图灵奖，Perlis 是**第一位**得主；勿写成"之一"或模糊为"早期" |
| 颁奖词 | ACM 原文 "for his influence in the area of advanced programming techniques and compiler construction"；可引用但需注明出处，勿擅自改写 |
| IT 归属 | IT（Internal Translator，1956）由 Perlis 团队开发，**Knuth 称其为第一个成功的编译器**；勿写成"Perlis 发明了编译器" |
| ALGOL 归属 | Perlis 是 ALGOL 的**主要推动者 / 团队成员**，非唯一发明者；ALGOL 是委员会成果（Backus、Naur、Perlis 等） |
| 学位 | 本科化学（Carnegie Tech，1943），硕士+博士数学（MIT，1949/1950）；**博士是数学不是计算机科学**（当时无 CS 博士） |
| 任职时序 | Purdue（1952）→ Carnegie Tech（1956，首任 CS 系主任）→ ACM 主席（1962）→ Yale（1971） |
| 图灵焦油坑 | "Turing tarpit" 术语出自 Perlis 1982 年 *Epigrams on Programming* 的 epigram #54；勿张冠李戴 |
| 生卒 | 已故：1922-04-01 ~ 1990-02-07，写作 `1922–1990` |
| 荣誉 | 图灵奖 1966、Computer Pioneer Award 1985；**无** National Medal、无 IEEE 等（勿编造） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| ALGOL | ALGOL 语言 | Perlis 主要推动者，委员会成果 |
| Internal Translator (IT) | 内部翻译器 | 1956 编译器，首个成功编译器（Knuth 评） |
| APL | APL 语言 | Perlis 晚年推崇（"A Language for Lyrical Programming"） |
| Epigrams on Programming | 编程格言集 | 1982 SIGPLAN，广被引用 |
| Turing tarpit | 图灵焦油坑 | Perlis 造词（epigram #54） |
| Carnegie Mellon University | 卡内基梅隆大学 | 当时称 Carnegie Institute of Technology |
| ACM | 美国计算机协会 | Perlis 1962 年任主席 |

**遗产页布局红线（★ 实测踩坑，来自 Ken Thompson 立传）**：

- ⚠ **禁止用 2×2 网格 + `text width=5.6cm`**：下排卡片与底部总结框在 16:9 画布上**纵向重叠**。
- ✅ **必须对齐 Andrew_Yao / Leslie_Lamport 标杆的 1×4 横排布局**：四张小卡 `text width=3.05cm`、`node[leg] style` 含 `rounded corners=6pt, inner xsep=6pt, inner ysep=8pt, font=\fontsize{6.4}{8.4}`，横排 `x = -5.4 / -1.8 / 1.8 / 5.4`、`y=1.3`；底部总结框 `y=-1.6`、`text width=13.0cm`。经 `make distclean && make` 验证无重叠。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（史诗 / 开阔）
- **来源**：与 Knuth 标杆同曲（先驱/奠基气质）；本地路径 `music_audio/alex-productions/...New Lands.wav` → `turing/presentations/Alan_Perlis/NewLands.wav`
- **匹配理由**：首届图灵奖的"开创"叙事，匹配"把计算机科学确立为一门学科"的宏大与开阔。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/1966/Alan Perlis/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/1966/Alan Perlis/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（统一 `\input`） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 通用标杆实例 Beamer 源码 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
