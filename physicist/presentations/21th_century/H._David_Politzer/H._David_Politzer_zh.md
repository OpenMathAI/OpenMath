# 物理学家立传提示词（21 世纪批次：H. David Politzer）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传的人物专属提示词**，以 H. David Politzer（2004 诺贝尔物理学奖，渐近自由）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Hugh David Politzer（休·波利策），2004 诺贝尔物理学奖三位得主之一（与 David Gross、Frank Wilczek 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与研究领域的结构化表达；Politzer 篇的设计母题围绕「渐近自由」——距离越近、相互作用越弱的反直觉图景。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Hugh David Politzer（1949-08-30 生？实为 **1949-08-31** 生于纽约市，在世）
- **气质关键词**：**渐近自由的发现者、QCD 奠基者之一、会弹班卓琴的理论家**
- **诺奖理由（官方原文，禁止改写）**：
  > "for the discovery of asymptotic freedom in the theory of the strong interaction"（因发现强相互作用理论中的渐近自由）
- **设计母题**：**距离与耦合的反比**——夸克靠得越近、色力越弱，近乎自由粒子；可用「随尺度松弛的弹簧/渐稀的网格」做视觉隐喻。
- **本地数据源**：
  - ✅ `physicist/presentations/21th_century/21st_century/H._David_Politzer/page.md`（已有本地）
  - ⬜ `{Dir}.html` 与 `images/` **待下载**：Wikipedia URL `https://en.wikipedia.org/wiki/H._David_Politzer`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input` 首页）；骨架复用 20 世纪成品（如 `Kenneth_G_Wilson_zh.tex`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1949-08-31 生于美国纽约市；在世（享年不写）。
- 家庭：父母 1939 年自捷克斯洛伐克逃亡英国，二战后移民美国。
- 教育：Bronx High School of Science（1966 届）→ University of Michigan 物理学士（1969）→ Harvard 博士（1974）。
- 博士导师：Sidney Coleman；博士论文 *Asymptotic freedom: an approach to strong interactions*（1974）。
- 博士后/青年研究员：Harvard Society of Fellows Junior Fellow（1974–1977）。
- 任职：California Institute of Technology（Caltech，1977 起），现任 Richard Chace Tolman 讲席教授（理论物理）。
- 关键荣誉：Nobel Prize in Physics（2004，与 Gross/Wilczek 共享）；J. J. Sakurai Prize（1986）；EPS High Energy and Particle Physics Prize（2003，与 Gross/Wilczek 共享）；Guggenheim Fellowship；American Academy of Arts and Sciences 院士（2011）。
- 知名博士生：Stephen Wolfram（Mathematica 创始人）。
- 核心贡献清单：
  1. 1973 年首篇论文独立发现**渐近自由**（与 Princeton 的 Gross–Wilczek 同时独立）
  2. 与 Thomas Appelquist 合作预言**粲偶素（charmonium）**存在
  3. 对量子色动力学（QCD）发展的奠基性贡献
  4. 班卓琴的物理学研究（趣味方向）
- 关键时间线（15–20 节点）：1949 生纽约 → 父母捷克流亡背景 → 1966 Bronx 科学高中 → 1969 Michigan 学士 → 1973 渐近自由论文 → 1974 Harvard 博士（Coleman 门下）→ 1974–77 Harvard Junior Fellow → 与 Appelquist 预言 charmonium → 1977 任教 Caltech → 1986 Sakurai Prize → 1989 客串电影《Fat Man and Little Boy》饰 Robert Serber → 2003 EPS 高能粒子物理奖（三人共享）→ 2004-12-08 诺奖演讲 *The Dilemma of Attribution* → 2008 与 20 位物理诺奖得主联名致信布什总统 → 2011 美国艺术与科学院院士 → 班卓琴物理 + Professor Politzer and the Rho Mesons 主唱（单曲 "The Simple Harmonic Oscillator"）→ Erdős–Bacon 数 5。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum field theory | 量子场论 | 非阿贝尔规范场的紫外行为 | 核心页 |
| 1 | quantum chromodynamics | 量子色动力学 | 渐近自由使 QCD 成立 | 核心页 |
| 2 | particle physics | 粒子物理 | 强相互作用、粲偶素预言 | 粲偶素页 |
| 3 | theoretical physics | 理论物理 | Caltech Tolman 讲席教授 | 身份页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致，只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Sidney Coleman | 师→生（博士导师） | Harvard 博士导师 |
| advisor-student | Stephen Wolfram | Politzer→学生 | 博士生，Mathematica 创始人 |
| co-honored | David Gross | 无向 | 2004 诺贝尔物理学奖共同得主；2003 EPS 高能粒子物理奖共同得主 |
| co-honored | Frank Wilczek | 无向 | 2004 诺贝尔物理学奖共同得主；2003 EPS 高能粒子物理奖共同得主 |
| colleague | Thomas Appelquist | 无向 | 合作预言 charmonium（粲偶素） |

> 入库注意：Gross 用库内规范名 **`David Gross`**（勿写 David J. Gross，防分裂 stub）；Coleman/Wolfram 沿用库内既有记录（id=1024/2419）。

### 第 5 步：设计配色方案 【人物专属】

- **气质**：深邃、幽默、反直觉
- **配色**：主色 **深靛蓝 `#2C3E67`**（强力的色束缚与理论深度）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeAF` 渐近自由 — 靛蓝 `#4C5FD5`
  - `badgeQCD` 量子色动力学 — 青绿 `#0E7C7B`
  - `badgeChar` 粲偶素 — 琥珀 `#E07B30`
  - `badgeLife` 趣味侧面 — 玫瑰 `#C4204F`
- **背景母题**：随距离渐稀的点阵网格（呼应耦合常数随距离减小）。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；封面有国籍。
2. **必须有身份信息页**：左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域），事实取自 infobox 不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 渐近自由的发现者 / H. David Politzer 1949– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 渐近自由 / QCD / 粲偶素 / 趣味物理
04  早年：纽约移民之子 (1949–1966) — 捷克流亡家庭、Bronx 科学高中
05  Michigan 与 Harvard (1966–1974) — Coleman 门下、博士论文
06  1973：渐近自由（核心贡献页）— 公式框放 β(g) 负号/耦合常数跑动示意式（page.md 无显式公式，可用 αs(Q²) 随 Q 减小示意图并注明）
07  独立发现的三重奏 — Politzer（Harvard）与 Gross–Wilczek（Princeton）同时独立
08  粲偶素预言 — 与 Appelquist 的合作
09  Harvard Junior Fellow 与 Caltech (1974– ) — Tolman 讲席教授
10  荣誉与认可 — Nobel 2004 · Sakurai 1986 · EPS 2003 · AAAS 2011
11  学生与传承 — Stephen Wolfram
12  舞台之外 — 电影客串、班卓琴物理、Rho Mesons 乐队、Erdős–Bacon 数
13  遗产：QCD 的基石
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 每写完一页 make，用 pdftoppm 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Politzer 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日 | **1949-08-31**（勿写 08-30） |
| 渐近自由归属 | 三人**各自独立**发现（Politzer 与 Gross–Wilczek），勿写成师承或单方首创 |
| 诺奖理由 | 官方为 "for the discovery of asymptotic freedom in the theory of the strong interaction"，勿改写为"量子色动力学发明" |
| 粲偶素 | 是**预言**（与 Appelquist），勿写"发现" |
| 博士导师 | Sidney Coleman（Harvard），勿与 Princeton 的 Gross 混淆 |
| 学生 | infobox 博士生仅 Stephen Wolfram 一人，勿扩写 |
| Guggenheim | frontmatter 有载但 page.md 正文无年份，年份禁写 |
| 电影 | 1989《Fat Man and Little Boy》饰 **Robert Serber**（Manhattan Project 物理学家），是配角客串 |
| 名字 | 全名 Hugh David Politzer，通行名 H. David Politzer；中文「休·波利策」 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| asymptotic freedom | 渐近自由 | 距离越近耦合越弱 |
| quantum chromodynamics | 量子色动力学 | 简称 QCD |
| strong interaction | 强相互作用 | 勿与"强力"泛称混用 |
| charmonium | 粲偶素 | c 与 c̄ 束缚态 |
| running coupling | 跑动耦合常数 | 随能标变化 |
| beta function | β 函数 | 符号为负 ⇒ 渐近自由 |
| junior fellow | 初级研究员 | Harvard Society of Fellows |
| Erdős–Bacon number | 埃尔德什–培根数 | 论文合作链 + 影视合作链 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions（高受众 / 强推进 / 紧张）
- **匹配理由**: 「竞争、难题攻克、革命性转折」贴合 1973 年 Harvard 与 Princeton 两队同时冲刺渐近自由的发现叙事；强推进节奏匹配理论突破的锋利感。
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`
- **备注**: 批内曲不重复；时长不足时 ffmpeg 循环/`-shortest` 对齐。

---

## 五、关键参考文件 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/H._David_Politzer/page.md` | 本地 Wikipedia 事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/H._David_Politzer.yaml` | 社会关系入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
