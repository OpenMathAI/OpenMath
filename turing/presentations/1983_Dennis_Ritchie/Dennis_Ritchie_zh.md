# 图灵奖得主立传提示词（人物实例：Dennis Ritchie）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」实例**，以 Dennis Ritchie（丹尼斯·里奇，1983 图灵奖，C 语言与 Unix 的奠基者）为样板。
> 参照标杆实例 Donald E. Knuth（`Donald_Knuth/Donald_Knuth_zh.md`）、同届实例 Ken Thompson（`Ken_Thompson/Ken_Thompson_zh.md`）与图灵奖通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用到任何图灵奖得主；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：图灵奖通用模板 `Turing_Bio_Prompt_Template.md` 与标杆实例 Knuth。
- **本实例**：Dennis MacAlistair Ritchie（丹尼斯·麦卡利斯特·里奇，1941-09-09 生于纽约州布朗克斯维尔，2011-10-12 逝于新泽西州伯克利高地，享年 70）。
- **设计哲学**：图灵奖得主必须有「身份信息页」，贡献表现为**语言 / 系统 / 工具**而非定理——与同届的 Thompson 共享「工程 / 系统」气质，复用其四分类色骨架。

---

## 二、背景信息 【人物专属】

- **目标得主**：Dennis MacAlistair Ritchie（1941-09-09 ~ 2011-10-12，已故）
- **气质关键词**：**C 语言创造者、Unix 共创者、B 语言贡献者、K&R 作者、Plan 9/Inferno/Limbo 参与者、密码分析（M-209）** —— 1983 图灵奖官方措辞（ACM）：与 Ken Thompson 共同获奖，"for their development of generic operating systems theory and specifically for the implementation of the UNIX operating system"（本实例正文可引用此原文获奖理由，但需注明"与 Thompson 共同"）。
- **设计母题**：**语言 / 系统 / 工程**——C 的「可移植性」是核心母题。视觉语言：泡泡背景呼应 Thompson 实例；配色复用 Thompson 四分类色（操作系统 / 编程语言 / 系统软件 / 体系与密码），但将"体系与棋"替换为更贴合 Ritchie 的"体系与密码"。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/1983/Dennis Ritchie/index.html`（121 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/1983/Dennis Ritchie/metadata.json`
  - 头像：`turing/pages/1983/Dennis Ritchie/images/250px-Dennis_Ritchie_2011.jpg`（已复制到 `presentations/Dennis_Ritchie/images/Ritchie.jpg`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/1983/Dennis Ritchie/index.html` 与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/1983/Dennis Ritchie/images/250px-Dennis_Ritchie_2011.jpg`
- **事实基准**：
  - 生卒：1941-09-09 生于纽约州布朗克斯维尔（Bronxville, New York）；2011-10-12（约，c.）逝于新泽西州伯克利高地（Berkeley Heights, New Jersey），享年 70
  - 本名：Dennis MacAlistair Ritchie；国籍：美国
  - 家庭：父亲 Alistair E. Ritchie，长期 Bell Labs 科学家，《The Design of Switching Circuits》合著者（开关电路理论）
  - 教育：Harvard University，物理（Physics）+ 应用数学（Applied mathematics）双学位，1963 年毕业；Summit High School（新泽西）
  - 任职：Bell Labs Computing Science Research Center 1967 入职；1990s 中 AT&T 重组转入 Lucent Technologies，2007 年以 System Software Research Department 主管身份退休
  - 博士：1968 年在 Harvard 完成 PhD 论文草稿 "Computational Complexity and Program Structure"，导师 Patrick C. Fischer；**但从未正式获得 PhD 学位**（2020 年 Computer History Museum 找回"遗失的论文"副本）
  - 核心成就（infobox Known for）：ALTRAN、B、BCPL、C、Multics、Unix
  - 其他贡献：与 James Reeds、Robert Morris 对 M-209 密码机的唯密文攻击（1970s，因 NSA 建议未发表）；参与 Plan 9、Inferno、Limbo
  - 荣誉：IEEE Piore 1982 · 图灵奖 1983（与 Ken Thompson 共同）· IEEE Hamming 1990 · Computer Pioneer 1994 · Computer History Museum Fellow 1997 · National Medal of Technology 1998（1999-04-21 由 Clinton 颁发）· Harold Pender 2003 · Japan Prize 2011（信息通信类）
  - 关键事实：
    - 与 Thompson **共同创造** Unix 与 C；Ritchie 常被归功于 Unix 原始版本（Thompson 写），Ritchie 的贡献之一是将 Unix 移植到不同机器/平台
    - B（Thompson 创）被 Ritchie 创造的 C 取代；C 由 Ritchie 在 B 基础上发展
    - 与 Brian Kernighan 合著 *The C Programming Language*（即 K&R，1978）
    - 图灵奖讲座题为 "Reflections on Software Research"
    - Doug McIlroy 评价："The names of Ritchie and Thompson may safely be assumed to be attached to almost everything not otherwise attributed."
    - 1999 访谈：视 Linux 与 BSD 为 Unix 的延续与衍生

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Dennis_Ritchie/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Ken_Thompson/Makefile`（同届、同气质），设置 `MAIN=Dennis_Ritchie_zh`、`VIDEO_NAME=Dennis_Ritchie_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 复制 `turing/pages/1983/Dennis Ritchie/images/250px-Dennis_Ritchie_2011.jpg` 到 `presentations/Dennis_Ritchie/images/Ritchie.jpg`

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | programming languages | 编程语言 | C（核心）、B、BCPL、ALTRAN、Limbo、K&R |
| 1 | operating systems | 操作系统 | Unix（共创）、Plan 9、Inferno、Multics |
| 2 | systems software | 系统软件 | Unix 可移植性、C 标准库、 crypt 工具传统 |
| 3 | cryptography and theory | 密码学与计算理论 | M-209 唯密文攻击、计算复杂性与程序结构（博士论文主题） |

- 入库脚本：`MySQL/seed_ritchie_full.py`（people 新建 id，4 领域 + 国籍 + 职业）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Patrick C. Fischer | 师→生 | 博士导师，Harvard（论文未完成学位） |
| colleague | Ken Thompson | 无向 | Unix/C 共创；1983 共同图灵奖；B→C 谱系 |
| co-honored | Ken Thompson | 无向 | 1983 图灵奖共同得主 |
| colleague | Brian Kernighan | 无向 | 合著 K&R（The C Programming Language） |
| colleague | Rob Pike | 无向 | Plan 9/Inferno/Limbo；讣告首报者 |
| colleague | Doug McIlroy | 无向 | Research Unix 同事，留下"almost everything"评价 |
| colleague | Robert Morris | 无向 | M-209 密码分析合作 |
| colleague | James Reeds | 无向 | M-209 密码分析合作 |

- 入库脚本：`MySQL/seed_ritchie_relations.py`（新建占位 + 关系）

### 第 5 步：设计配色方案 【人物专属】

- **气质**：语言 / 系统 / 工程（C 的「可移植性」是母题；与 Thompson 共享务实工程气质）
- **配色**：图灵紫（品牌主色）+ 强调红 + 四分类色（复用 Thompson 实例，保证同届视觉连贯）
  - `badgeOS` 操作系统 — 蓝 `#2E5A9E`
  - `badgeLang` 编程语言 — 青绿 `#1E8E8E`
  - `badgeTools` 系统软件 — 琥珀 `#D9A441`
  - `badgeTheory` 体系与密码 — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应 Thompson 实例的「终端字符流」逻辑节奏

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。✅
2. **封面有国籍**：底部状态栏 `美国 | Bell Labs · Lucent | Turing 1983 · National Medal 1998`。✅
3. **必须有身份信息页**：封面之后第 3 页，左头像 + 右 2×2 信息网格（含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。✅
4. **品牌口径统一**：结尾页底部写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承。✅

### 5.2 背景音乐 【人物专属】

- **气质定位**：工程 / 系统（C、Unix、可移植性，现代科技感）—— 与 Thompson 同届同气质。
- **选定曲目**：Michael FK & Andy Leech《**Falling Apart**》（5:32，电子 / 渐进 / 情感），与 Thompson 实例同曲（同届、共享 Unix/C 叙事母题）。
- **落地文件**：`turing/presentations/Dennis_Ritchie/FallingApart.wav`（复制自音乐库，不入 git）。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 主标题「丹尼斯·里奇」+ 英文名/生卒 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 编程语言/操作系统/系统软件/密码与理论
04  早年：布朗克斯维尔的开关电路之子 (1941–1963)
05  Harvard 双学位与"遗失的博士论文"
06  Bell Labs 与 Multics：通往 Unix 的前夜 (1967)
07  B → C：一门可移植语言的诞生
08  Unix：用 C 重写，走向可移植
09  K&R：让 C 成为世界的语言
10  Plan 9 / Inferno / Limbo：一切皆文件之后
11  M-209 密码分析与"未发表的贡献"
12  荣誉
13  遗产：你每天敲下的 C，仍在运行世界
14  结尾 — "让语言先把世界统一"
15  彩蛋 — 本页及整份立传均由 XeLaTeX + Beamer 排版（底层土壤是 Unix/C）
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；四分类色与 `\plainbar`/`\deckbackground`/`\sectiontitle`/`\lab` 复用 Knuth/Thompson 标杆骨架。
- ⚠ 注意：命令名不能含"字母+数字+字母"歧义（如 `\plan9slide` 会被解析为 `\plan`+`9` 引发灾难），应写作 `\planNslide`。

### 第 8 步：布局检查 【模板通用】

- `make distclean && make` 返回 EXIT=0，15–17 页，无缺字、无致命溢出（仅 ≤9.53pt 轻微 Overfull，可接受）。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Ritchie 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 图灵奖理由 | 1983 与 Thompson **共同**获奖，理由围绕"generic operating systems theory and specifically the implementation of the UNIX operating system"；勿写成 Ritchie 独享 |
| C 的归属 | Ritchie **创造 C**，在 Thompson 的 B 基础上发展；B 是 C 的前身（脱胎于 BCPL）。勿写成"Thompson 发明 C" |
| Unix 归属 | Ritchie 与 Thompson **共同创造** Unix；Thompson 写原始版本，Ritchie 贡献之一是**将 Unix 移植到不同机器/平台**。勿写成"Ritchie 单独发明 Unix" |
| 生卒表述 | Ritchie **已故**：1941-09-09 ~ 2011-10-12（约 c.），写作 `1941–2011`；勿与 Thompson（在世）混淆 |
| 博士学历 | 1968 在 Harvard 完成论文草稿，**从未正式获得 PhD**（导师 Patrick C. Fischer）；infobox Education 仅列 Harvard BS（双学位 1963）。勿写"Harvard 博士" |
| K&R | *The C Programming Language* 与 **Brian Kernighan** 合著（1978），常称 K&R；勿写成 Ritchie 独著 |
| 荣誉年份 | Piore 1982 · 图灵奖 1983 · Hamming 1990 · Computer Pioneer 1994 · CHM Fellow 1997 · National Medal 1998（1999 颁）· Pender 2003 · Japan Prize 2011。注意 National Medal 是 1998 年度、1999-04-21 颁发 |
| Plan 9/Inferno/Limbo | Ritchie **参与**开发（与 Thompson/Pike 等）；Limbo 是 Plan 9 的伴生语言。勿夸大为"Ritchie 主导" |
| M-209 密码分析 | 1970s 与 Reeds、Morris 合作，因 NSA 建议**未发表**；勿写成已发表成果 |
| 名言引用 | Ritchie 名言（1999 访谈）：Linux/BSD "the continuation of ideas that were started by Ken and me and many others" 可引用；Doug McIlroy 的 "almost everything not otherwise attributed" 是 McIlroy 的评价，非 Ritchie 自述，需注明出处 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| C (programming language) | C 语言 | Ritchie 创造，B 的后继 |
| B (programming language) | B 语言 | Thompson 创，C 的前身 |
| BCPL | BCPL 语言 | B 的祖先 |
| ALTRAN | ALTRAN | Ritchie 早年的代数化简语言 |
| Unix | Unix 操作系统 | 与 Thompson 共创 |
| Plan 9 from Bell Labs | Plan 9 操作系统 | "一切皆文件"；Ritchie 参与 |
| Inferno (operating system) | Inferno 操作系统 | Ritchie 参与 |
| Limbo (programming language) | Limbo 语言 | Plan 9 伴生语言；Ritchie 参与 |
| The C Programming Language | C 程序设计语言（K&R） | 与 Kernighan 合著 |
| Multics | Multics 操作系统 | Unix 前身项目 |
| crypt (M-209) | M-209 密码机分析 | 唯密文攻击，未发表 |
| Research Unix | Research Unix | Bell Labs 研究分支 |

**遗产页布局红线（★ 实测踩坑，来自 Ken Thompson 立传）**：

- ⚠ **禁止用 2×2 网格 + `text width=5.6cm`**：下排卡片与底部总结框在 16:9 画布上**纵向重叠**。
- ✅ **必须对齐 Andrew_Yao / Leslie_Lamport 标杆的 1×4 横排布局**：四张小卡 `text width=3.05cm`、`node[leg] style` 含 `rounded corners=6pt, inner xsep=6pt, inner ysep=8pt, font=\fontsize{6.4}{8.4}`，横排 `x = -5.4 / -1.8 / 1.8 / 5.4`、`y=1.3`；底部总结框 `y=-1.6`、`text width=13.0cm`。经 `make distclean && make` 验证无重叠。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（电子 / 渐进 / 情感，5:32）
- **来源**：与 Thompson 实例同曲（同届、共享 Unix/C 工程母题）；本地路径 `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → `turing/presentations/Dennis_Ritchie/FallingApart.wav`
- **匹配理由**：渐进电子质感匹配"可移植性"叙事——C 让同一份代码跑遍全世界机器，是工程师长波长的耐心。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/1983/Dennis Ritchie/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/1983/Dennis Ritchie/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（统一 `\input`） |
| `turing/presentations/Ken_Thompson/Ken_Thompson_zh.tex` | 同届标杆 Beamer 源码（四分类色骨架） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 通用标杆实例 Beamer 源码 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

---

## 六、Review 记录

### 第一轮 Review（factually wrong，2026-08-27）✅

- **三要素核查**：① 封面头像 ✅（右上角 `images/Ritchie.jpg` + `draw=coveraccent!50` 边框 + 姓名小字注）；② 封面国籍 ✅（副标题"美国" + 底部状态栏 `美国 | Bell Labs · Lucent | Turing 1983 · National Medal 1998`）；③ 身份信息页 ✅（`\profileslide`，封面后第 2 页，左头像 + 右 2×2 信息网格，含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。
- **事实核查**：身份信息页字段与本地 infobox 一致（生卒 1941-09-09 ~ 2011-10-12、本名 Dennis MacAlistair Ritchie、国籍 美国、任职 Bell Labs 1967– / Lucent 至 2007、出生地 布朗克斯维尔、教育 Harvard 物理+应用数学 1963、荣誉 Turing 1983 · National Medal 1998 · Piore 1982 · Hamming 1990 · Japan Prize 2011）。无事实错误。
- **待第二轮复核（专业表述）**：身份信息页「师承」写 `Patrick C. Fischer（博士导师）`，但 Ritchie **从未正式获得 PhD**（infobox Education 仅列 Harvard BS）。严格意义上"博士导师"与"未获 PhD"存在表述张力，属第二轮（professionally unstable）复核项，第一轮暂不判定为事实错误。
- **编译验证**：`make distclean && make` 返回 EXIT=0，16 页，无缺字、无致命溢出。

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
