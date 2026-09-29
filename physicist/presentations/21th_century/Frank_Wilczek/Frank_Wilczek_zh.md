# 物理学家立传提示词（21 世纪批次：Frank Wilczek）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传的人物专属提示词**，以 Frank Wilczek（2004 诺贝尔物理学奖，渐近自由）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Frank Anthony Wilczek（弗兰克·维尔切克），2004 诺贝尔物理学奖三位得主之一（与 David Gross、H. David Politzer 共享），横跨粒子物理与凝聚态的多产理论家。
- **设计哲学**：保留「身份信息页」+ 研究领域结构化骨架；Wilczek 篇的设计母题围绕「命名者的想象力」——axion、anyon、time crystal 皆由他命名，视觉语言可用「新词汇点亮物理版图」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Frank Anthony Wilczek（1951-05-15 生于纽约州米尼奥拉，在世）
- **气质关键词**：**渐近自由的年轻 co-发现者、命名大师（axion/anyon）、跨界的诗人物理学家**
- **诺奖理由（官方原文，禁止改写）**：
  > "for the discovery of asymptotic freedom in the theory of the strong interaction"（因发现强相互作用理论中的渐近自由）
- **设计母题**：**命名与创造**——把假设变成名词、把名词变成研究方向（axion 源自洗衣粉品牌、anyon 意为「随便什么子」）。
- **本地数据源**：
  - ✅ `physicist/presentations/21th_century/21st_century/Frank_Wilczek/page.md`（已有本地）
  - ⬜ `{Dir}.html` 与 `images/` **待下载**：Wikipedia URL `https://en.wikipedia.org/wiki/Frank_Wilczek`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`；骨架复用 20 世纪成品（如 `Kenneth_G_Wilson_zh.tex`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1951-05-15 生于美国纽约州 Mineola；在世。波兰裔与意大利裔移民家庭；父亲夜校自学成为「自学成才的工程师」。
- 教育：Queens 公立学校、Martin Van Buren High School（跳两级、13 岁入高中十年级）→ University of Chicago 数学学士（1970，Phi Beta Kappa）→ Princeton（数学 MA 1972、物理 PhD 1974）。
- 中学亮点：1967 Westinghouse Science Talent Search 决赛第四名（群论数学项目）。
- 博士导师：David Gross；博士论文 *Non-abelian gauge theories and asymptotic freedom*（1974）。
- 芝加哥关键影响：Peter Freund 的群论/对称性课程（Wilczek 自述对其影响极大）。
- 任职：MIT Herman Feshbach 讲席教授（MIT 理论物理中心）；T. D. Lee Institute（上海）创始所长；上海交大 Wilczek Quantum Center 首席科学家；Arizona State University 杰出教授（每年 2–3 月）；Stockholm University 全职教授；曾任 IAS（Princeton）、KITP（UCSB）、NORDITA 访问。
- 关键荣誉：MacArthur Fellowship（1982）；Sakurai Prize（1986）；ICTP Dirac Medal（1994）；Lorentz Medal（2002）；Lilienfeld Prize（2003）；EPS High Energy and Particle Physics Prize（2003，三人共享）；Nobel（2004）；King Faisal International Prize（2005）；Templeton Prize（2022）；NAS 院士（1990）、美国艺术与科学院院士（1993）、美国哲学学会会员（2005）、荷兰皇家艺术与科学院外籍院士（2000）。
- 配偶：Betsy Devine（1973 年结婚，两女 Amity 与 Mira；普林斯顿一起看 1972 Fisher–Spassky 国际象棋赛相识）。
- 核心贡献清单：
  1. 1973 与 Gross 发现**渐近自由**（与 Politzer 各自独立）
  2. 1978 提出并命名**轴子（axion）**（与 Weinberg 各自独立指出 PQ 机制破缺产生新粒子）
  3. 1982 提出并命名**任意子（anyon）**/二维分数字统计；1984 与 Arovas、Schrieffer 证明分数量子霍尔效应需 anyon
  4. 2012 提出**时间晶体（time crystal）**
  5. 色超导、夸克物质相结构；黑洞的移动镜模型等
- 关键时间线（15–20 节点）：1951 生 Mineola → 跳级入高中 → 1967 Westinghouse 第四名 → 1970 Chicago 数学学士（Freund 课程）→ 1972 Princeton 数学 MA → 1973 与 Gross 发现渐近自由（Princeton）→ 1974 博士 → 1977 Peccei–Quinn 机制后独立提出 axion → 1982 anyon 论文 → 1982 MacArthur → 1986 Sakurai → 1988 与妻子合著 *Longing for the Harmonies* → 1990 NAS → 1994 Dirac Medal → 2002 Lorentz Medal → 2003 Lilienfeld + EPS 三人共享 → 2004 诺贝尔奖 → 2005 King Faisal → 2012 时间晶体 → 2014 与 Hawking 等联名 AI 警告信 → 2022 Templeton Prize → 上海交大/李政道研究所任职。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | theoretical physics | 理论物理 | 粒子与凝聚态双栖 | 身份页 |
| 1 | quantum field theory | 量子场论 | 渐近自由、分数字统计 | 核心页 |
| 2 | quantum chromodynamics | 量子色动力学 | 2004 诺奖核心 | 核心页 |
| 3 | particle physics | 粒子物理 | axion、夸克物质 | axion 页 |
| 4 | condensed matter physics | 凝聚态物理 | anyon、时间晶体 | anyon/时间晶体页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致，只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | David Gross | 师→生（博士导师） | Princeton 博士导师，2004 诺奖共同得主 |
| co-honored | David Gross | 无向 | 2004 诺贝尔物理学奖共同得主；2003 EPS 高能粒子物理奖共同得主 |
| co-honored | H. David Politzer | 无向 | 2004 诺贝尔物理学奖共同得主；2003 EPS 高能粒子物理奖共同得主 |
| spouse | Betsy Devine | 无向 | 1973 结婚，合著 *Longing for the Harmonies* |
| influence | Peter Freund | 对方→Wilczek | 芝加哥大学群论/对称性课程教师，自述影响深远 |
| colleague | Steven Weinberg | 无向 | 1978 各自独立指出 PQ 机制新粒子（Wilczek 命名 axion） |

> 入库注意：Gross 用库内规范名 **`David Gross`**；Politzer 已入库（id=2981，规范名 `H. David Politzer`）；Weinberg 沿用库内 `Steven Weinberg`（id=2573）。

### 第 5 步：设计配色方案 【人物专属】

- **气质**：多产、灵动、跨界
- **配色**：主色 **深紫红 `#7A1E5A`**（新粒子的命名者之紫）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeAF` 渐近自由 — 靛蓝 `#4C5FD5`
  - `badgeAxion` 轴子 — 琥珀 `#E07B30`
  - `badgeAnyon` 任意子 — 青绿 `#0E7C7B`
  - `badgeTC` 时间晶体 — 玫瑰 `#C4204F`
- **背景母题**：散落的发光新词标签（axion / anyon / time crystal）漂浮于深紫背景。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；封面有国籍。
2. **必须有身份信息页**：左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域），事实取自 infobox 不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 命名新物理的人 / Frank Wilczek 1951– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 渐近自由 / axion / anyon / time crystal
04  早年：皇后区的跳级生 (1951–1970) — Westinghouse 第四名、Chicago 数学
05  Princeton：Gross 门下 (1970–1974) — 数学转物理、博士论文
06  1973：渐近自由（核心贡献页）— 公式框放非阿贝尔规范理论紫外行为示意（page.md 无显式公式，注明为概念图式）
07  轴子：从洗衣粉到暗物质 — PQ 机制、与 Weinberg 独立、命名轶事
08  任意子：二维的分数字统计 — Leinaas–Myrheim 前驱、1984 分数量子霍尔
09  时间晶体 — 2012 提出、2018 实现
10  MIT 与全球 — Feshbach 讲席、上海交大/李政道所、ASU、Stockholm
11  家庭与写作 — Betsy Devine、三本科普书、Templeton 2022
12  荣誉与认可 — Nobel 2004 · MacArthur 1982 · Lorentz 2002 · Dirac 1994
13  遗产：给物理起名字的人
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 每写完一页 make，用 pdftoppm 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Wilczek 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 渐近自由归属 | 与 Gross 合作发现，且与 Politzer **各自独立**；勿写"Wilczek 师承 Politzer"或单方首创 |
| 轴子命名 | 名字来自**洗衣粉品牌 Axion**；Weinberg 独立得出后称 "Higglet"，后采纳 axion——三方细节勿混 |
| 轴子提出年份 | 1977 Peccei–Quinn 提出机制；1978 Wilczek 与 Weinberg 各自独立指出新粒子（勿写 1977 由 Wilczek 提出） |
| anyon 前驱 | Leinaas & Myrheim（Oslo）1977 已算出二维统计，Wilczek 1982 命名——勿写成"发明二维统计" |
| 博士学位 | 数学 MA（1972）+ 物理 PhD（1974）双轨，勿写成"数学博士" |
| 配偶 | Betsy Devine 是科普合著者，勿只写"妻子" |
| Weinberg 关系 | 两人是**各自独立**提出者，非合作者，note 措辞注意 |
| Templeton | 2022 年获奖理由涉及"数学之美/自然定律"，引用须用 page.md 原句 |
| 国籍 | 美国（infobox 单一），勿因波兰裔写"波兰/美国" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| asymptotic freedom | 渐近自由 | 距离越近耦合越弱 |
| axion | 轴子 | 冷暗物质候选 |
| anyon | 任意子 | 仅二维系统 |
| fractional statistics | 分数统计 | 介于玻色/费米之间 |
| time crystal | 时间晶体 | 2012 提出 |
| color superconductivity | 色超导 | 高密度夸克物质 |
| Peccei–Quinn mechanism | PQ 机制 | 强 CP 问题解 |
| running coupling | 跑动耦合常数 | 随能标变化 |
| Westinghouse Science Talent Search | 西屋科学天才奖 | 1967 第四名 |
| Templeton Prize | 邓普顿奖 | 2022，跨界宗教/科学语境谨慎 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（高受众 / 探索 / 史诗）
- **匹配理由**: 「探索、远征式叙事」贴合 Wilczek 从渐近自由到 axion、anyon、时间晶体的连续开拓轨迹——他不断为新领域命名并远征。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`
- **备注**: 批内曲不重复（Politzer 用 Savage）。

---

## 五、关键参考文件 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Frank_Wilczek/page.md` | 本地 Wikipedia 事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Frank_Wilczek.yaml` | 社会关系入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
