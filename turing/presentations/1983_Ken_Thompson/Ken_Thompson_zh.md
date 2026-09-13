# 图灵奖得主立传提示词（人物实例：Ken Thompson）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」实例**，以 Ken Thompson（肯·汤普森，1983 图灵奖，Unix 与 C 的奠基者）为样板。
> 参照标杆实例 Donald E. Knuth（`Donald_Knuth/Donald_Knuth_zh.md`）与图灵奖通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用到任何图灵奖得主；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：图灵奖通用模板 `Turing_Bio_Prompt_Template.md` 与标杆实例 Knuth。
- **本实例**：Kenneth Lane Thompson（肯·汤普森，1943-02-04 生于美国路易斯安那州新奥尔良，在世）。
- **设计哲学**：图灵奖得主必须有「身份信息页」，贡献表现为**系统 / 语言 / 工具**而非定理——保留模板骨架。

---

## 二、背景信息 【人物专属】

- **目标得主**：Kenneth Lane Thompson（1943-02-04 ~ ，截至资料基准日在世）
- **气质关键词**：**Unix 原始作者、B 语言创造者、UTF-8 设计者、正则表达式与 grep 普及者、Plan 9 与 Belle 象棋机作者、Go 共创者** —— 1983 图灵奖官方措辞（ACM）：与 Dennis Ritchie 共同获奖，"for their development of generic operating systems theory and specifically for the implementation of the UNIX operating system"（本实例正文不引用原文获奖理由，仅作校验基准）。
- **设计母题**：**系统 / 工程 / 务实**——终端、管道、文件系统的逻辑。视觉语言：泡泡背景以离散圆点呼应「终端字符流」的节奏；配色用四分类色区分操作系统 / 编程语言 / 系统软件 / 体系与棋。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/1983/Ken Thompson/index.html`（104 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/1983/Ken Thompson/metadata.json`
  - 头像：`turing/pages/1983/Ken Thompson/images/Ken_Thompson_2019.jpg`（已复制到 `presentations/Ken_Thompson/images/Thompson.jpg`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/1983/Ken Thompson/index.html` 与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/1983/Ken Thompson/images/Ken_Thompson_2019.jpg`
- **事实基准**：
  - 生卒：1943-02-04 生于路易斯安那州新奥尔良（New Orleans, Louisiana），在世
  - 本名：Kenneth Lane Thompson；国籍：美国
  - 教育：UC Berkeley，BS 1965 / MS 1966（电气工程与计算机科学）；硕导 Elwyn Berlekamp
  - 任职：Bell Labs 1966 起（至约 2000）；Google 2006 起
  - 核心成就（infobox Known for）：Multics、Unix、B、C、Belle（象棋机）、UTF-8、Plan 9、Inferno、grep、残局库（endgame tablebase）、Go
  - 荣誉：IEEE Piore 1982 · 图灵奖 1983（与 Dennis Ritchie 共同）· NAS 院士 1985 · IEEE Hamming 1990 · Computer Pioneer 1994 · 国家技术奖 1998 · Tsutomu Kanai 1999 · Harold Pender 2003 · 日本奖 2011
  - 关键事实：与 Ritchie 在 Bell Labs 共创 Unix；Multics 期间创造 Bon 语言；为继续玩《Space Travel》移植 PDP-7 而引发 Unix 雏形；B 是 C 的直接前身；正则表达式（QED/ed）+ Thompson 构造法（NFA）；UTF-8 与 Rob Pike 为 Plan 9 设计（1992）；Belle 象棋机 + 残局库；2006 起在 Google 与 Rob Pike 等共创 Go

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Ken_Thompson/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Donald_Knuth/Makefile`，设置 `MAIN=Ken_Thompson_zh`、`VIDEO_NAME=Ken_Thompson_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 复制 `turing/pages/1983/Ken Thompson/images/Ken_Thompson_2019.jpg` 到 `presentations/Ken_Thompson/images/Thompson.jpg`

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | operating systems | 操作系统 | Unix、Plan 9、分层文件/进程/管道 |
| 1 | programming languages | 编程语言 | B（C 的前身）、Go 谱系 |
| 2 | systems software | 系统软件 | grep、QED/ed、正则、UTF-8 |
| 3 | computer architecture and chess | 计算机体系与计算机棋 | Belle、残局库、分布式系统思想 |

- 入库脚本：`MySQL/seed_thompson_full.py`（people id=232，4 领域 + 国籍 + 职业）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Elwyn Berlekamp | 师→生 | 硕导，UC Berkeley |
| colleague | Dennis Ritchie | 无向 | Unix 共创；1983 共同图灵奖 |
| co-honored | Dennis Ritchie | 无向 | 1983 图灵奖共同得主 |
| colleague | Brian Kernighan | 无向 | 1970 从 Multics 双关命名 Unix |
| colleague | Rob Pike | 无向 | Google 时期共创 Go、UTF-8 |

- 入库脚本：`MySQL/seed_thompson_relations.py`（新建 3 人占位 + 5 条关系）

### 第 5 步：设计配色方案 【人物专属】

- **气质**：系统 / 工程 / 务实
- **配色**：图灵紫（品牌主色）+ 强调红 + 四分类色
  - `badgeOS` 操作系统 — 蓝 `#2E5A9E`
  - `badgeLang` 编程语言 — 青绿 `#1E8E8E`
  - `badgeTools` 系统软件 — 琥珀 `#D9A441`
  - `badgeTheory` 体系与棋 — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「终端字符流」的逻辑节奏

### 5.2 背景音乐 【人物专属】

- **气质定位**：工程 / 系统（Unix、C、工具链，现代科技感）
- **选定曲目**：Michael FK & Andy Leech《**Falling Apart**》（5:32，电子 / 渐进 / 情感）
- **落地文件**：`turing/presentations/Ken_Thompson/FallingApart.wav`（已复制，不入 git）
- **选曲理由**：渐进电子质感匹配"长时间工程打磨"的叙事——从 PDP-7 游戏到运行世界的服务器，是工程师长波长的耐心

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。✅
2. **封面有国籍**：底部状态栏 `美国 | Bell Labs | Turing 1983 · National Medal 1998`。✅
3. **必须有身份信息页**：封面之后第 3 页，左头像 + 右 2×2 信息网格（含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。✅
4. **品牌口径统一**：结尾页底部写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承。✅

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 主标题「肯·汤普森」+ 英文名/生年 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 操作系统/编程语言/系统软件/体系与棋
04  早年：新奥尔良的逻辑迷 (1943–1966)
05  Multics 到 Unix 的偶然 — PDP-7 与《Space Travel》
06  Unix：分层文件/进程/管道
07  B：C 语言的前身
08  正则与 grep
09  UTF-8：让世界写进同一份文件
10  Plan 9 与 Inferno
11  Belle：会下棋的机器
12  Go：在 Google 重新出发
13  荣誉
14  遗产：你正站在他的肩膀上
15  结尾 — "把系统握在手里"
16  彩蛋 — 本页及整份立传均由 XeLaTeX + Beamer 排版（底层土壤是 Unix/C）
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；四分类色与 `\plainbar`/`\deckbackground`/`\sectiontitle`/`\lab` 复用 Knuth 标杆骨架。
- ⚠ 注意：命令名不能含"字母+数字+字母"歧义（如 `\plan9slide` 会被解析为 `\plan`+`9` 引发灾难），应写作 `\planNslide`。

### 第 8 步：布局检查 【模板通用】

- `make distclean && make` 返回 EXIT=0，17 页，无缺字、无致命溢出（仅 285 行 ≤9.53pt 轻微 Overfull，可接受）。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Thompson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 图灵奖理由 | 1983 与 Ritchie **共同**获奖，理由围绕"通用操作系统理论与 UNIX 实现"；勿写成 Thompson 独享 |
| B 与 C 关系 | B 是 C 的**直接前身**（脱胎于 BCPL），C 由 Ritchie 在 B 基础上发展；勿写成"Thompson 发明 C" |
| Unix 命名 | 1970 年 **Brian Kernighan** 从 Multics 双关提出 "Unix" 一名；勿写成 Thompson 命名 |
| UTF-8 | 与 **Rob Pike** 共同为 Plan 9 设计（1992）；勿写成 Thompson 单独发明 |
| 正则构造法 | Thompson 构造法（NFA）是他对正则的贡献；"几乎所有正则程序用其记法变体"可写，但勿夸大为"发明正则"（正则源于 1950s 理论） |
| Go | 2006 起在 Google 与 **Rob Pike 等人**共创；勿写成 Thompson 单独创造 |
| 生卒表述 | Thompson 在世，写作 `1943–`；勿写已故 |
| Bell Labs 任职 | 1966 入职，约 2000 年离开；Google 2006 起；勿混同年份 |
| 名言引用 | 封面引语 "I was always fascinated with logic…" 出自本地 Wikipedia 正文（小学二进制算术），可引用 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Unix | Unix 操作系统 | 注意命名源自 Kernighan |
| B (programming language) | B 语言 | C 的前身 |
| C (programming language) | C 语言 | Ritchie 在 B 基础上发展 |
| regular expression | 正则表达式 | 理论源于 1950s，Thompson 贡献记法与构造法 |
| grep | grep | Unix 文本搜索工具 |
| UTF-8 | UTF-8 编码 | 与 Pike 共为 Plan 9 设计 |
| Plan 9 from Bell Labs | Plan 9 操作系统 | 分布式"一切皆文件" |
| Belle (chess machine) | Belle 象棋机 | 含残局库 endgame tablebase |
| Go (programming language) | Go 语言 | 与 Pike 等共创 |
| pipe | 管道 | Unix 进程间通信核心 |

**遗产页布局红线（★ 实测踩坑）**：

- ⚠ **禁止用 2×2 网格 + `text width=5.6cm`**。初版因下排卡片 (`y=-1.05`) 与底部总结框 (`y=-2.55`) 间距过近，在 16:9 画布上**纵向重叠**，被 user 截图指出。
- ✅ **必须对齐 Andrew_Yao / Leslie_Lamport 标杆的 1×4 横排布局**：四张小卡 `text width=3.05cm`、`node[leg] style` 含 `rounded corners=6pt, inner xsep=6pt, inner ysep=8pt, font=\fontsize{6.4}{8.4}`，横排 `x` 坐标为 `-5.4 / -1.8 / 1.8 / 5.4`、`y=1.3`；底部总结框 `y=-1.6`、`text width=13.0cm`。该布局经 `make distclean && make` 验证无重叠。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（电子 / 渐进 / 情感，5:32）
- **本地路径**：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → `turing/presentations/Ken_Thompson/FallingApart.wav`
- **匹配理由**：渐进电子质感匹配"长时间工程打磨"的叙事；时长 332 秒 ≫ 17 页 × 7 秒 ≈ 119 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/1983/Ken Thompson/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/1983/Ken Thompson/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（统一 `\input`） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 标杆实例 Beamer 源码 |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.md` | 标杆实例人物提示词 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

---

## 六、Review 记录

### 第一轮 Review（factually wrong，2026-08-27）✅

- **三要素核查**：① 封面头像 ✅（右上角 `images/Thompson.jpg` + `draw=coveraccent!50` 边框 + 姓名小字注）；② 封面国籍 ✅（副标题"美国" + 底部状态栏 `美国 | Bell Labs | Turing 1983 · National Medal 1998`）；③ 身份信息页 ✅（`\profileslide`，封面后第 2 页，左头像 + 右 2×2 信息网格，含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。
- **事实核查**：身份信息页全部字段与本地 infobox 一致（生卒 1943-02-04、本名 Kenneth Lane Thompson、国籍 美国、师承 Elwyn Berlekamp、任职 Bell Labs 1966– / Google 2006–、出生地 新奥尔良、教育 UC Berkeley BS 1965 / MS 1966、荣誉 Turing 1983 · National Medal 1998 · Piore 1982 · NAS 1985 · Japan Prize 2011）。无事实错误。
- **修正项**：封面引语由 `"…fascinated with logic — even…"` 修正为 `"…fascinated with logic and even…"`（`and` 误作破折号，已对齐 Wikipedia 原文，并保留 `, stuff like that.` 尾部）。
- **编译验证**：`make distclean && make` 返回 EXIT=0，17 页，无缺字、无致命溢出。

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
