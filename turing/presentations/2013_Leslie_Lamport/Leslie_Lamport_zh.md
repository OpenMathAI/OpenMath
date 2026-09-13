# 图灵奖得主立传提示词（人物实例：Leslie Lamport）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」人物实例**，以 Leslie Lamport（莱斯利·兰波特，2013 图灵奖，分布式系统、Paxos 共识、时序逻辑、LaTeX 奠基人）为目标人物。
> 格式对标图灵奖侧首个人物实例 Donald E. Knuth（`turing/presentations/Donald_Knuth/Donald_Knuth_zh.md`），并融合图灵奖通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按 Lamport 替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：图灵奖侧标杆实例 Donald E. Knuth（提示词 + tex 结构）与通用模板 `Turing_Bio_Prompt_Template.md`。
- **本实例**：Leslie Barry Lamport（莱斯利·巴里·兰波特，1941-02-07 生于美国纽约市，在世）。
- **设计哲学**：图灵奖得主必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达；Lamport 的「贡献」主要表现为**算法、逻辑、系统、文档工具**而非「定理」——立传应突出其为「看似混乱的分布式计算」**建立清晰、良好定义的秩序（coherence）**这一主线，务必保留。

---

## 二、背景信息 【人物专属】

- **目标得主**：Leslie Barry Lamport（1941-02-07 ~ ，截至资料基准日在世）
- **气质关键词**：**分布式系统理论奠基人、逻辑时钟与 happens-before 的提出者、Paxos 共识算法作者、TLA/TLA+ 时序逻辑的创立者、LaTeX 初始开发者、以数学方式思考系统的形式主义者** —— 2013 图灵奖获奖理由（ACM 官方措辞，已核实）：
  > "for fundamental contributions to the theory and practice of distributed and concurrent systems, notably the invention of concepts such as causality and logical clocks, safety and liveness, replicated state machines, and sequential consistency"（因其对分布式与并发系统理论与实践的奠基性贡献，尤其是提出因果性与逻辑时钟、安全性与活性、复制状态机、顺序一致性等概念）
- **设计母题**：**分布式秩序 / 时间与因果（Order out of Chaos）**。Lamport 毕生主题是为「消息传递、并发、故障与不一致」的混沌世界建立可推理的数学秩序——逻辑时钟把事件排序变成因果链，Paxos 让一组机器在故障中达成共识，TLA+ 用数学规格替代含糊的自然语言。视觉语言：时钟与事件箭头、happened-before 有向无环图、消息传递节点、拜占庭将军、希腊议会（Paxos 的「兼职议会」隐喻）、LaTeX 排版网格。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/2013/Leslie Lamport/index.html`（约 84 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/2013/Leslie Lamport/metadata.json`（简化字段：title/url/year/image_count）
  - 头像：`turing/pages/2013/Leslie Lamport/images/250px-Leslie_Lamport.jpg`（infobox 肖像，2008 年拍摄，可直接复制）
- **参考模板**：
  - 图灵奖通用模板：`turing/presentations/Turing_Bio_Prompt_Template.md`
  - 图灵奖标杆提示词：`turing/presentations/Donald_Knuth/Donald_Knuth_zh.md`
  - 化学家标杆提示词：`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 图灵奖现有版式参考：`turing/video/episode-00-what-is-turing-award/turing_ep00_zh.tex`（图灵紫配色）
  - 项目首页模板：`turing/presentations/cover/openturing_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/2013/Leslie Lamport/index.html`（含 infobox + 正文）与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/2013/Leslie Lamport/images/250px-Leslie_Lamport.jpg`（Wikipedia infobox 肖像，2008 年拍摄）
- 提取 infobox 与正文，输出供校验（**事实基准如下**）：
  - 生卒日期（1941-02-07 生于纽约市 New York City，具体为布鲁克林 Brooklyn，在世）
  - 本名（Leslie Barry Lamport）；国籍（美国）
  - 家庭（犹太家庭；父 Benjamin Lamport 自俄罗斯帝国沃尔科维斯克 Volkovisk，今白俄罗斯瓦夫卡维斯克移民；母 Hannah Lamport née Lasser 自奥匈帝国、今波兰东南部移民）
  - 教育（Bronx High School of Science 毕业 → MIT 数学 BS 1960 → Brandeis University 数学 MA 1963、PhD 1972）
  - 博士导师（Richard Palais）；博士论文《The analytic Cauchy problem with singular data》(1972，关于解析偏微分方程的奇点)
  - 主要任职（Massachusetts Computer Associates 1970–1977 → Stanford Research Institute (SRI International) 1977–1985 → Digital Equipment Corporation / Compaq 1985–2001 → Microsoft Research 加州 2001 年加入，2025 年 1 月退休）
  - 关键荣誉（Turing 2013 · IEEE John von Neumann Medal 2008 · IEEE Emanuel R. Piore Award 2004 · Dijkstra Prize 2000/2005/2014 · NAE 院士 1991 · NAS 院士 2011 · ACM Fellow 2014 · 五个欧洲荣誉博士 2003–2007）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 个节点，见第 6 步）

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Leslie_Lamport/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆实例 `Donald_Knuth/Makefile`，设置 `MAIN=Leslie_Lamport_zh`、`VIDEO_NAME=Leslie_Lamport_zh`

### 第 3 步：收集图片 【人物专属】

- 复制 `turing/pages/2013/Leslie Lamport/images/250px-Leslie_Lamport.jpg` 到 `presentations/Leslie_Lamport/images/Lamport.jpg`

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Lamport 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | distributed systems | 分布式系统 | 逻辑时钟、happens-before、全局快照、复制状态机，2013 图灵奖核心 | 封面、核心页 |
| 1 | consensus algorithms | 共识算法 | Paxos、拜占庭容错、Reaching Agreement | 共识页 |
| 2 | temporal logic | 时序逻辑 | TLA、TLA+、安全性/活性（safety/liveness） | 时序逻辑页 |
| 3 | document preparation | 文档排版 | LaTeX 初始开发者与第一本手册作者 | LaTeX 页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en='Leslie Lamport'`），设置 `primary_occupation='computer scientist'`、`has_biography=1`、`has_social_data=1`（补齐 qid/gender/birth_date/description）
- 关联职业 `computer scientist`（rank 0）、`mathematician`（rank 1，因 Lamport 亦为数学背景）
- 国籍 `United States`
- 将 4 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 生成入库脚本 `MySQL/seed_lamport_full.py` 并执行，脚本末尾输出校验结果（研究领域 / 国籍 / 职业 / `person_field` 总数）

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Palais | 师→生（博士导师） | Brandeis 数学导师 |

**合作者 / 共同成果（源自本地 Wikipedia 正文）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| collaborator | Robert Shostak | 双向 | The Byzantine Generals Problem (1982) |
| collaborator | Marshall Pease | 双向 | The Byzantine Generals Problem / Reaching Agreement in the Presence of Faults |
| collaborator | K. Mani Chandy | 双向 | Chandy–Lamport 分布式快照算法 |
| successor | Frank Mittelbach | Lamport→继任者 | 1989 年移交 LaTeX 维护，LaTeX3 团队 |

- 将上述关系（导师 + 合作者 + 继任者）写入 `person_relation`（`from_id` / `to_id` / `relation_type` / `note` / `source`），`source` 记 `'立传-Leslie_Lamport'`
- **方向处理**：`advisor-student` 有向——导师 Richard Palais 为 `from_id`（Palais → Lamport）；合作者为双向；LaTeX 继任者为 Lamport → Mittelbach
- 不在库中的关联人物先建占位记录（`has_biography=0`），关系 `note` 加 `[材料待展开] ` 前缀
- 生成入库脚本 `MySQL/seed_lamport_relations.py` 并执行，脚本末尾输出校验结果（新建人物数 / 新增关系数 / `person_relation` 总数）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：形式化、理性克制、为混乱建立秩序
- **配色**：图灵紫（OpenTuring 品牌主色）+ 强调红 + 四分类色
  - `badgeDist` 分布式系统 — 蓝 `#2E5A9E`
  - `badgeConsensus` 共识算法 — 琥珀 `#D9A441`
  - `badgeTemporal` 时序逻辑 — 青绿 `#1E8E8E`
  - `badgeDocs` 文档排版 / LaTeX — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡 + 时钟/事件箭头意象（稀疏大块实心圆错落），呼应「时间、因果与共识」——以离散圆点与连线暗示消息传递与事件排序

### 5.2 背景音乐 【人物专属】

- **气质定位**：理论/算法之美（分布式系统理论奠基者、形式化推理、长期主义）
- **选定曲目**：Alex-Productions《**Timeless**》（132k views，高受众/沉稳/纪录片，与理论内敛气质匹配）
- **落地文件**：`turing/presentations/Leslie_Lamport/Timeless.wav`（待复制，不入 git）
- **选曲理由**：沉稳的纪录片基调匹配「为混沌建立秩序」的形式化叙事——从数学博士到分布式系统奠基，再到 TLA+ 的长期纲领，是思想的严谨演进而非英雄史诗
- **备选**（未采用）：
  - ★★ The Flow of Time — 「时间感/纪录片」匹配逻辑时钟与事件排序主题，但受众低于 Timeless
  - ★★ Expedition — 「探索/史诗」匹配分布式系统的开创气质，但沉稳感略弱

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自本地 `index.html` infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenTuring`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 主标题「莱斯利·兰波特」+ 音译名/英文名 + 四色 badge + 右上头像 + 国籍行
02  早年：布鲁克林少年 (1941–1960) — 犹太移民家庭、Bronx Science、MIT 数学 BS
03  身份信息页（★ 必做）— 左头像 + 右信息网格（含本名、出生地、教育、师承、任职、荣誉、核心领域）
04  核心贡献概览 — 分布式系统 / 共识算法 / 时序逻辑 / LaTeX
05  从数学到计算机 (1970–1985) — Massachusetts Computer Associates → SRI，数学博士转向并发
06  时间、时钟与事件次序 (1978) — 逻辑时钟 / happened-before / 因果（核心贡献页）
07  顺序一致性 (1979) — "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs"
08  拜占庭将军问题 (1982) — 与 Shostak、Pease，拜占庭容错
09  Paxos：兼职议会 (1998 发表) — 共识算法 / 复制状态机
10  更多以 Lamport 命名的成果 — 面包店算法 / Chandy–Lamport 快照 / Lamport 签名
11  LaTeX：文档排版系统 (1983–1989) — 基于 TeX 的宏包与第一本手册
12  TLA / TLA+：时序逻辑与形式化规格 — safety/liveness、Specifying Systems
13  职业生涯：DEC/Compaq → Microsoft Research (1985–2025)
14  荣誉 — Turing 2013 · von Neumann 2008 · Dijkstra ×3 · NAS/NAE
15  遗产：为分布式系统「建立秩序」 — 因果、逻辑时钟、共识、可验证规格
16  结尾 — "quixotic attempt to overcome engineers' antipathy towards mathematics"（征服工程师对数学的反感）
17  彩蛋 — LaTeX 继承自 TeX：底层排版引擎是 Knuth 的 TeX，Lamport 在其上开发 LaTeX 宏包；本页及整份立传真正用的是 LaTeX（XeLaTeX + Beamer），同时致敬 TeX 与 LaTeX 作者
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照通用模板 `\profileslide`。
- 头部宏定义（图灵紫配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）整体复用 `turing/video/episode-00-what-is-turing-award/turing_ep00_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Lamport 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 图灵奖理由 | 官方措辞强调 "distributed and concurrent systems" 与 "causality and logical clocks, safety and liveness, replicated state machines, and sequential consistency"；**LaTeX 不是 2013 获奖原因**，LaTeX 是另一条独立贡献线 |
| "发明 TeX" | TeX 是 Knuth 创造；Lamport 是**基于 TeX 开发宏包 LaTeX**并写第一本手册，勿写成"发明 TeX" |
| "发明 Paxos" | Paxos 是 Lamport 提出的共识算法，论文《The Part-Time Parliament》用希腊议会寓言书写，1998 年发表于 ACM TOCS；勿把寓言当历史，勿写"1998 年才发明" |
| 拜占庭将军问题 | 1982 年论文与 Robert Shostak、Marshall Pease 共同完成；Dijkstra Prize 2005 另颁给三人 1980 年论文 "Reaching Agreement in the Presence of Faults"，勿混淆两篇 |
| Chandy–Lamport | 分布式快照算法与 K. Mani Chandy 共同，勿遗漏合作者 |
| 教育经历 | 数学出身（MIT BS 1960、Brandeis MA 1963 / PhD 1972），博士论文是解析 PDE 奇点，非计算机科学；勿写成"计算机科学博士" |
| 博士时间线 | MA 1963 与 PhD 1972 间隔较大（1963–1972），是 Brandeis 数学学位，勿写成连续一气呵成 |
| 任职时间线 | 1970 才正式进入计算机行业（Massachusetts Computer Associates），此前是数学路径；SRI 1977–1985；DEC/Compaq 1985–2001；Microsoft Research 2001 加入、2025 年 1 月退休 |
| 生卒表述 | Lamport 仍在世，生卒年写作 `1941–`，勿写成已故 |
| 荣誉顺序 | 图灵奖 2013 是最高荣誉；IEEE John von Neumann Medal 2008、Piore Award 2004、Dijkstra Prize 2000/2005/2014 在前，NAS 2011、ACM Fellow 2014 在侧，勿混入"首个/唯一"表述 |
| Solana lamport | 2020 年 Solana 将最小货币单位命名为 lamport（0.000000001 SOL），属趣味细节，可放在彩蛋/遗产页，勿写成核心贡献 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| distributed systems | 分布式系统 | 与"并发系统"关联 |
| logical clock | 逻辑时钟 | Lamport 提出，勿写成"物理时钟" |
| happened-before | 先于发生 / 因果次序 | 保留英文或给出准确中文 |
| causality | 因果性 | 图灵奖官方概念 |
| sequential consistency | 顺序一致性 | 内存模型/多处理器正确性 |
| Byzantine fault tolerance | 拜占庭容错 | 与将军问题关联 |
| Paxos | Paxos 共识算法 | 勿写成"Paxos 协议"泛化 |
| replicated state machine | 复制状态机 | 图灵奖官方概念 |
| safety / liveness | 安全性 / 活性 | TLA 中核心性质 |
| temporal logic of actions (TLA) | 行为时序逻辑 | 勿与一般"时序逻辑"混同 |
| TLA+ | TLA+ 规格语言 | 附加号 |
| LaTeX | LaTeX 排版系统 | 写作 `LaTeX`，勿写成 "Latex" |
| Chandy–Lamport algorithm | Chandy–Lamport 快照算法 | 与 Chandy 共同 |
| Lamport signature | Lamport 签名 | 哈希链式一次性签名原型 |
| bakery algorithm | 面包店算法 | 互斥算法 |

---

## 四、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/2013/Leslie Lamport/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/2013/Leslie Lamport/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 图灵奖标杆成品参考 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板 |
| `turing/video/episode-00-what-is-turing-award/turing_ep00_zh.tex` | 图灵奖版式（图灵紫配色）参考 |
| `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.tex` | 化学家标杆成品参考 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 物理学家标杆成品参考 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
