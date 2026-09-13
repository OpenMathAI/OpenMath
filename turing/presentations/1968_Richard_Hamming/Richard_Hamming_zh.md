# 图灵奖得主立传提示词（人物实例：Richard Hamming）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」实例**，以 Richard Hamming（理查德·哈明，1968 图灵奖，**第三**位得主）为样板。
> 参照标杆实例 Donald E. Knuth（`Donald_Knuth/Donald_Knuth_zh.md`）与通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用到任何图灵奖得主；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Richard Wesley Hamming（理查德·韦斯利·哈明，1915-02-11 生于伊利诺伊州芝加哥，1998-01-07 逝于加州蒙特雷，享年 82）。**1968 年图灵奖得主，第三位得主（third recipient）**。
- **设计哲学**：图灵奖得主必须有「身份信息页」，贡献表现为**纠错码 / 数值方法 / 编程系统 / 信号处理**——Hamming 是"让数字信息自我纠错的奠基者"，气质为**工程 / 实用 / 洞见**。

---

## 二、背景信息 【人物专属】

- **目标得主**：Richard Wesley Hamming（1915-02-11 ~ 1998-01-07，已故）
- **气质关键词**：**汉明码（Hamming code）、汉明距离（Hamming distance）、汉明窗（Hamming window）、汉明界（Hamming bound）、L2 编程语言、数值计算方法、Young Turks（贝尔实验室"少壮派"）** —— 1968 图灵奖 ACM 颁奖词（注意：原文署于 1979 IEEE Piore Award，但 ACM 1968）："For introduction of error correcting codes, pioneering work in operating systems and programming languages, and the advancement of numerical computation."（引入纠错码、在操作系统与编程语言上的开创性工作、以及推动数值计算）。
- **设计母题**：**纠错 / 洞见 / 工程务实**——"数字信息如何自我纠错"的母题。视觉语言：泡泡背景（稀疏大块实心圆）；配色用图灵紫主色 + 四分类色（纠错码 / 数值方法 / 编程语言 / 信号处理）。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/1968/Richard Hamming/index.html`（116 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/1968/Richard Hamming/metadata.json`（仅基础字段，正文以 index.html 为准）
  - 头像：`turing/pages/1968/Richard Hamming/images/Richard_Hamming.jpg`（已复制到 `presentations/Richard_Hamming/images/Hamming.jpg`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/1968/Richard Hamming/index.html` 与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/1968/Richard Hamming/images/Richard_Hamming.jpg`
- **事实基准**（全部取自本地 index.html infobox 与正文）：
  - **生卒**：1915-02-11 生于伊利诺伊州芝加哥（Chicago, Illinois）；1998-01-07 逝于加州蒙特雷（Monterey, California），享年 82；死因为心脏病发作（heart attack）。**已故**。
  - **本名**：Richard Wesley Hamming；国籍：美国。父 Richard J. Hamming（荷兰裔信用经理）、母 Mabel G. Redfield（五月花号后裔）。
  - **教育**：
    - 1937 年 University of Chicago **数学**学士（B.S.）；因大萧条仅拿得到芝加大奖学金（无工学院），转读数学，后称"幸而如此"
    - 1939 年 University of Nebraska–Lincoln **文学硕士**（M.A.）
    - 1942 年 University of Illinois at Urbana–Champaign **数学博士**（Ph.D.），博士论文 *Some Problems in the Boundary Value Theory of Linear Differential Equations*，导师 **Waldemar Trjitzinsky**（1901–1973）；研读了 George Boole《The Laws of Thought》
    - 1942-09-05 与同校学生 Wanda Little 结婚（她获英语文学硕士），婚姻持续至 Hamming 去世，无子女
    - 1944 年任 University of Louisville（J.B. Speed 工学院）助理教授
  - **曼哈顿计划**：1945-04 离开 Louisville 加入 Los Alamos Laboratory（Hans Bethe 组），用 IBM 计算器为物理学家求解方程；妻 Wanda 也到 Los Alamos 任"human computer"（为 Bethe 与 Edward Teller 工作）。自述角色为"computer janitor（计算机勤杂工）"。
  - **任职**：
    - 1946 年加入 Bell Telephone Laboratories（BTL），至 1976 年退休；在贝尔期间参与实验室几乎所有重大成就
    - 在贝尔与 **Claude Shannon** 一度同办公室；数学研究部还有 John Tukey、Donald Ling、Brockway McMillan；Shannon、Ling、McMillan、Hamming 自称为 **"Young Turks"（少壮派）**
    - 1958–1960 任 ACM 主席（president of ACM）
    - 1960 年预言贝尔实验室一半预算将用于计算（同事不信，结果预言还偏保守）
    - 1976 年转入 Naval Postgraduate School（Monterey, California）任计算机科学兼职教授 / 高级讲师，专注教学与著书；1997-06 获荣休教授（Professor Emeritus），1997-12 完成最后一次讲座，数周后去世
  - **核心成就（infobox Known for）**：Hamming code、Hamming window、Hamming numbers、sphere-packing/Hamming bound、Hamming graph、Hamming distance
  - **关键事实**：
    - **汉明码（Hamming code）**：1947 年某周五，他给机器布置周末长程计算，周一发现早期出错导致整段计算报废；由此立志——"如果计算机能发现错误，就应有办法定位错误并自我纠正"。1950 年里程碑论文提出"两个码字不同位置的个数"（即**汉明距离 Hamming distance**），并据此构造出**汉明码**族——开启了纠错码这一全新研究领域。汉明码是**完美码（perfect code）**
    - **汉明界（Hamming bound）**，又称 sphere-packing / volume bound，是分组码参数的理论上限；达到该界的码即完美码
    - **数值方法**：针对 Milne 方法的不稳定性，发展出 **Hamming predictor-corrector（汉明预测-校正法）**；后被 Adams method 取代。名言（出自 1962 *Numerical Methods for Scientists and Engineers*）：**"The purpose of computing is insight, not numbers."**（计算的目的在洞见，不在数字）
    - **数字滤波**：发明 **Hamming window（汉明窗）**，著 *Digital Filters*（1977）
    - **L2 编程语言**：1950 年代为 IBM 650 编程，与 **Ruth A. Weiss** 于 1956 年开发 **L2**（最早的程序语言之一，贝尔内部广泛使用，外部称 Bell 2），1957 年 IBM 650 升级为 IBM 704 后被 Fortran 取代
    - **"Hamming's problem"（正则数 / Hamming numbers）**：Dijkstra 在 *A Discipline of Programming*（1976）中将"高效求正则数"归功 Hamming，得名"Hamming numbers"，但文中明确"他并未发现它们"
  - **荣誉（infobox Awards / 正文 Awards 段）**：
    - Turing Award, ACM, **1968**（第三位得主）
    - IEEE Emanuel R. Piore Award, 1979（颁奖词同上述纠错码/OS/编程语言/数值计算）
    - Member of National Academy of Engineering, 1980
    - Harold Pender Award（University of Pennsylvania）, 1981
    - **IEEE Richard W. Hamming Medal**, 1988（**首届/首位得主**，以他命名；奖章背面刻有汉明码的奇偶校验矩阵）
    - Fellow of ACM, 1994
    - Eduard Rhein Foundation Basic Research Award, 1996

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Richard_Hamming/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Donald_Knuth/Makefile`（标杆实例），设置 `MAIN=Richard_Hamming_zh`、`VIDEO_NAME=Richard_Hamming_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 复制 `turing/pages/1968/Richard Hamming/images/Richard_Hamming.jpg` 到 `presentations/Richard_Hamming/images/Hamming.jpg`

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | error-correcting codes | 纠错码 | 汉明码、汉明距离、汉明界（完美码），开创纠错码领域 |
| 1 | numerical analysis | 数值分析 | Hamming 预测-校正法、数值积分 |
| 2 | programming languages | 编程语言 | L2（Bell 2，与 Ruth Weiss） |
| 3 | signal processing | 数字信号处理 | Hamming window（汉明窗）、数字滤波 |

- 入库脚本：`MySQL/seed_hamming_full.py`（people 新建 id，4 领域 + 国籍 + 职业）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Waldemar Trjitzinsky | 师→生 | 博士导师，Illinois（数学，边值理论） |
| colleague | Claude Shannon | 无向 | 贝尔同办公室；Young Turks 成员 |
| colleague | John Tukey | 无向 | 贝尔数学研究部；Young Turks 成员（"bit" 一词提出者） |
| colleague | Brockway McMillan | 无向 | 贝尔；Young Turks 成员 |
| coauthor | Ruth A. Weiss | 无向 | L2 编程语言共同开发者 |
| co-honored-era | 图灵奖得主序列 | 无向 | 1968 第三位得主（与 Perlis/Wilkes 同列） |

- 入库脚本：`MySQL/seed_hamming_relations.py`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：工程 / 实用 / 洞见（数字信息自我纠错、计算为洞见）
- **配色**：图灵紫（品牌主色）+ 强调红 + 四分类色
  - `badgeCode` 纠错码 — 蓝 `#2E5A9E`
  - `badgeNum` 数值分析 — 青绿 `#1E8E8E`
  - `badgeLang` 编程语言 — 琥珀 `#D9A441`
  - `badgeSignal` 数字信号处理 — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡（稀疏大块实心圆），呼应"纠错"的密度/网格叙事

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。✅
2. **封面有国籍**：底部状态栏 `美国 | Bell Labs · Naval Postgraduate School · ACM | Turing 1968（第三位）`。✅
3. **必须有身份信息页**：封面之后第 3 页，左头像 + 右 2×2 信息网格（含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。✅
4. **品牌口径统一**：结尾页底部写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承。✅

### 5.2 背景音乐 【人物专属】

- **气质定位**：工程 / 实用 / 洞见（纠错码奠基、计算为洞见）—— 史诗 / 开阔。
- **选定曲目**：Alex-Productions **New Lands**（史诗 / 开阔，匹配"让数字世界自我修复"的开创叙事），与 Knuth / Perlis / Wilkes 同曲。
- **落地文件**：`turing/presentations/Richard_Hamming/NewLands.wav`（复制自音乐库，不入 git）。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 主标题「理查德·哈明」+ 英文名/生卒 + 四色 badge + 右上头像 + 国籍行（标注"1968 第三位得主"）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 纠错码/数值分析/编程语言/数字信号处理
04  早年：芝加哥的数学少年与大萧条下的求学 (1915–1937)
05  Nebraska 与 Illinois：从硕士到边值理论博士 (1937–1942)
06  曼哈顿计划：洛斯阿拉莫斯的"计算机勤杂工"与原子弹算术核查
07  Bell Labs 与"少壮派"（Young Turks）：与 Shannon 同办公室
08  1947 年的那个周末：从一次计算崩溃到纠错码的诞生
09  汉明码与汉明距离：让数字信息自我纠错 (1950)
10  汉明界与完美码：打开纠错码研究大门
11  "计算的目的在洞见，不在数字"：数值方法与预测-校正
12  汉明窗、L2 语言与工程全才
13  海军研究生院：最后一位教师 (1976–1997)
14  荣誉与遗产：以他命名的 IEEE 奖章
15  结尾 — "如果计算机能发现错误，就应有办法定位并纠正它"
16  彩蛋 — 本页由 XeLaTeX + Beamer 排版
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；四分类色与 `\plainbar`/`\deckbackground`/`\sectiontitle`/`\lab` 复用 Knuth/Thompson 标杆骨架。
- ⚠ 注意：命令名不能含"字母+数字+字母"歧义（如 `\\l2slide` 易混淆），可写作 `\\ltwo` 或 `\\lIIslide`（避免数字字母粘连）。

### 第 8 步：布局检查 【模板通用】

- `make distclean && make` 返回 EXIT=0，16–18 页，无缺字、无致命溢出（仅 ≤9.53pt 轻微 Overfull，可接受）。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hamming 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 得主序位 | 1968 图灵奖是**第三位**得主（third recipient），不是"之一"；前有 Perlis(1966)、Wilkes(1967) |
| 颁奖词归属 | "For introduction of error correcting codes, pioneering work in operating systems and programming languages, and the advancement of numerical computation" 是 **IEEE Piore Award 1979** 的颁奖词，但 ACM 也用以概括其图灵奖贡献；可引用但**注明出处**，勿擅自改写或张冠李戴为纯图灵奖词 |
| 汉明码年份 | 1947 年萌念（周末计算崩溃），**1950 年**正式发表里程碑论文并提出 Hamming distance；勿写成"1947 年发明"或"1948 年" |
| 完美码 | 汉明码是 **perfect code（完美码）**，因达到 Hamming bound；勿称"最优码"或泛化 |
| 学位 | 本科数学（Chicago 1937）、硕士（Nebraska 1939）、博士数学（Illinois 1942，导师 Trjitzinsky）；**无计算机科学学位**（当时无 CS 博士） |
| 曼哈顿计划角色 | 自述"computer janitor（计算机勤杂工）"，用 IBM 计算器为物理学家解边值方程；**非**核心物理学家；妻 Wanda 是 human computer |
| Young Turks | 贝尔"少壮派"成员 = Shannon、Ling、McMillan、Hamming；"bit" 一词是 **Tukey** 提出（文中明确），勿归给 Hamming |
| 汉明数与 Hamming's problem | "Hamming numbers（正则数）"是 Dijkstra 在 1976 书里将"高效求正则数"归功 Hamming 而得名，但**他并未发现它们（he did not discover them）**——勿写成"Hamming 发现了正则数" |
| L2 / Bell 2 | 与 **Ruth A. Weiss** 于 1956 开发，**外部用户称 Bell 2**；1957 年被 Fortran 取代 |
| 生卒 | 已故：1915-02-11 ~ 1998-01-07，写作 `1915–1998`，享年 82；死因心脏病 |
| 荣誉 | 图灵奖 1968、Piore 1979、NAE 1980、Pender 1981、IEEE Hamming Medal 1988（**首届/首位得主**，奖章背面刻汉明码奇偶校验矩阵）、ACM Fellow 1994、Eduard Rhein 1996；**无** National Medal、无 Nobel 等（勿编造） |
| ACM 主席 | 1958–1960 任 ACM 主席；勿漏 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Hamming code | 汉明码 | 1950 提出，完美码 |
| Hamming distance | 汉明距离 | 两码字不同位数，1950 提出 |
| Hamming bound | 汉明界 / 球面包 | 分组码参数上界，达到者为完美码 |
| Perfect code | 完美码 | 汉明码即完美码 |
| Hamming window | 汉明窗 | 数字滤波窗函数 |
| Parity bit | 奇偶校验位 | 纠错码前置概念 |
| L2 (Bell 2) | L2 编程语言 | 与 Ruth Weiss，1956，最早语言之一 |
| Young Turks | 少壮派（贝尔） | Shannon/Tukey/Ling/McMillan/Hamming |
| Bell Labs | 贝尔电话实验室 | 1946–1976 任职 |
| Naval Postgraduate School | 海军研究生院 | 1976 起，Monterey |

**遗产页布局红线（★ 实测踩坑，来自 Ken Thompson 立传）**：

- ⚠ **禁止用 2×2 网格 + `text width=5.6cm`**：下排卡片与底部总结框在 16:9 画布上**纵向重叠**。
- ✅ **必须对齐 Andrew_Yao / Leslie_Lamport 标杆的 1×4 横排布局**：四张小卡 `text width=3.05cm`、`node[leg] style` 含 `rounded corners=6pt, inner xsep=6pt, inner ysep=8pt, font=\fontsize{6.4}{8.4}`，横排 `x = -5.4 / -1.8 / 1.8 / 5.4`、`y=1.3`；底部总结框 `y=-1.6`、`text width=13.0cm`。经 `make distclean && make` 验证无重叠。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（史诗 / 开阔）
- **来源**：与 Knuth / Perlis / Wilkes 标杆同曲（工程/奠基气质）；本地路径 `music_audio/alex-productions/...New Lands.wav` → `turing/presentations/Richard_Hamming/NewLands.wav`
- **匹配理由**："让数字世界自我修复"的开创叙事，匹配工程务实与洞见的史诗感。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/1968/Richard Hamming/index.html` | 本地 Wikipedia 正文（116 KB，精准事实来源） |
| `turing/pages/1968/Richard Hamming/metadata.json` | 基础元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（统一 `\input`） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 通用标杆实例 Beamer 源码 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
