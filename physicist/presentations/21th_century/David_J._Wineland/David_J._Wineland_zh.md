# 物理学家立传提示词（David J. Wineland · 2012 诺贝尔物理学奖）

> **本文件是 OpenPhysicist 21 世纪批次的人物专属立传提示词**，以 David J. Wineland（2012 诺贝尔物理学奖，离子阱与激光冷却）为目标人物。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：David Jeffery Wineland（戴维·杰弗里·瓦恩兰），2012 诺贝尔物理学奖（与 Serge Haroche 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇另需突出**精密测量的计量学主线**——从氘微波激射器博士论文到 NIST 离子储藏组，再到「最精确的原子钟」，一条以/ion 驯服时间与量子态的实验长卷。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：David J. Wineland（1944-02-24 生于威斯康星州密尔沃基，在世）
- **气质关键词**：**离子阱里的钟表匠、激光冷却的先行者、单原子逻辑门的建造者** —— 2012 诺贝尔物理学奖获奖理由：
  > "for ground-breaking experimental methods that enable measuring and manipulation of individual quantum systems"（因其能够实现测量和操控单个量子系统的突破性实验方法）
- **设计母题**：**被电磁场悬浮的单个离子（a single trapped ion）**。射频阱中一颗被激光冷却至静止的原子——既是钟摆又是量子比特，是比泛泛「精密测量」更贴合 Wineland 的视觉语言。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/David_J._Wineland/page.md`（✅ 已有本地）
- **html/images**：待下载 —— Wikipedia URL：`https://en.wikipedia.org/wiki/David_J._Wineland`（第 0 步下载 `David_J._Wineland.html` 与 infobox 肖像到 `images/`）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（事实基准如下）；html 与 images/ 待下载（URL 见上）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1944-02-24 生于威斯康星州密尔沃基（infobox 正文另记 Wauwatosa 出生/成长），在世（death_date 留白）
  - 国籍：美国
  - 家庭：妻子 Sedna Quimby-Wineland（人类学家 George I. Quimby 之女），育有两子
  - 教育：Encina High School（萨克拉门托）1961 → UC Davis 1961.9–1963.12 → UC Berkeley 物理学士 1965 → Harvard 硕士/博士，PhD 1970
  - 博士导师：Norman Foster Ramsey, Jr.（1989 诺贝尔物理学奖得主）；博士论文《The Atomic Deuterium Maser》(1971)
  - 其他学术导师：Hans Georg Dehmelt（1989 诺奖得主）；博士后 1970s 初在 Dehmelt 组（华盛顿大学）研究离子阱中的电子
  - 任职机构：1975 加入美国国家标准局（今 NIST），创建离子储藏组（Ion Storage Group），现任 Physical Measurement Laboratory；University of Colorado at Boulder 物理系教职；2018-01 转任 University of Oregon 物理系 Knight Research Professor（仍以顾问身份参与 NIST 离子储藏组）
  - 关键荣誉：Davisson-Germer Prize 1990；Meggers Award 1990；Einstein Prize for Laser Science 1996；Rabi Award 1998；Schawlow Prize 2001；Stratton Award 2003；Frederic Ives Medal 2004；National Medal of Science 2007；Herbert Walther Award 2009；Benjamin Franklin Medal 2010（与 Juan Ignacio Cirac、Peter Zoller 共享）；Nobel 2012（与 Haroche 共享）；Golden Plate 2014；OSA Honorary Member 2017；Micius Quantum Prize 2019；IRI Medal 2020；NAS 院士 1992；APS 与 OSA Fellow
  - 知名学生：page.md 无载（禁写）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点，见幻灯片序列）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Wineland 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | trapped ions | 囚禁离子 | 离子阱中的单离子操控，NIST 离子储藏组主线 | 核心贡献页 |
| 1 | laser cooling | 激光冷却 | 1978 首次激光冷却离子 | 早年页 |
| 2 | atomic clocks | 原子钟 | 2005 量子逻辑单铝离子钟，最精确原子钟 | 原子钟页 |
| 3 | quantum computing | 量子计算 | 1995 首个单原子量子逻辑门 | 量子信息页 |
| 4 | precision spectroscopy | 精密光谱学 | 基础物理检验与光谱技术 | 光谱页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Norman Ramsey | advisor（对方是导师） | 哈佛博士导师（1970 氘原子微波激射器论文），1989 诺贝尔物理学奖得主 |
| advisor-student | Hans G. Dehmelt | advisor（对方是导师） | 华盛顿大学博士后导师（离子阱电子研究），infobox 列为其他学术导师，1989 诺奖得主 |
| co-honored | Serge Haroche | 无向 | 2012 诺贝尔物理学奖共享（单量子系统测量与操控的突破性实验方法） |
| co-honored | Juan Ignacio Cirac | 无向 | 2010 Benjamin Franklin Medal in Physics 共同得主 |
| co-honored | Peter Zoller | 无向 | 2010 Benjamin Franklin Medal in Physics 共同得主 |

#### 4.5.1 入库操作

- 以 `name_en='David J. Wineland'`（qid Q61045，复用库内 stub id=2834）为中心写入 `person_relation`
- 对手方用库内规范名：`Norman Ramsey`（id=2113）、`Hans G. Dehmelt`（id=2835）；Cirac/Zoller 库内无记录，seed 以规范全名 `Juan Ignacio Cirac`、`Peter Zoller` 建 stub
- 方向约定：师生有向（advisor=对方是导师）；共同荣誉无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：精密、冷峻、计量学的克制
- **配色**：深青（离子阱的冷光）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeIon` 囚禁离子 — 深青 `#0E7C7B`
  - `badgeCool` 激光冷却 — 冰蓝 `#3A7CA5`
  - `badgeClock` 原子钟 — 琥珀 `#E07B30`
  - `badgeGate` 量子逻辑门 — 玫瑰 `#C4204F`
- **主色**：`#1B4D6B`（深青蓝，批内唯一）
- **背景母题**：柔和气泡——悬浮在电极之间的单点光源，呼应「单个离子的可视性」

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）：左头像 + 右信息网格（生卒、出生地、国籍、教育、师承、任职、主要荣誉、核心领域）。
4. 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 离子阱里的钟表匠 / David J. Wineland 1944– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地威斯康星、Berkeley/Harvard、师承 Ramsey/Dehmelt、NIST、Nobel 2012、核心领域）
03  核心贡献概览 — 激光冷却 / 囚禁离子 / 原子钟 / 量子逻辑门
04  早年：威斯康星到加州 (1944–1965) — Wauwatosa、丹佛、萨克拉门托、UC Davis→Berkeley
05  哈佛博士：Ramsey 门下 (1965–1970) — 氘原子微波激射器
06  博士后：Dehmelt 组与离子阱 (1970–1975) — 华盛顿大学、阱中电子
07  NIST 离子储藏组 (1975–) — 创建团队、CU Boulder 教职
08  1978 首次激光冷却离子（核心贡献页）
09  1995 首个单原子量子逻辑门 — 2004 巨型粒子量子隐形传态
10  2005 最精确的原子钟 — 单铝离子 + 量子逻辑
11  荣誉与认可 — Nobel 2012 · National Medal of Science 2007 · Franklin Medal 2010 · NAS 1992
12  2018 转任 Oregon Knight 教授 — NIST 顾问
13  遗产：离子阱量子计算与计量学
14  结尾
```

- 公式框：page.md 无公式，用**概念图式**——「射频 Paul 阱中单离子的能级与边带冷却示意」，并注明"示意图，非 page.md 公式"。

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

- 版式：每页写完 `make clean && make`，pdftoppm 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

**Wineland 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方措辞"测量与操控单个量子系统的突破性实验方法"，勿写成"发明离子阱"（Paul 1989）或"激光冷却理论"（Chu/Phillips/Cohen-Tannoudji 1997） |
| 与 Haroche 分工 | Wineland 用**离子阱**，Haroche 用**微波腔 + 里德堡原子**；两条路线共享 2012 奖，方法勿混淆 |
| 双导师口径 | 博士导师 Ramsey（哈佛 PhD 1970）；Dehmelt 是**博士后导师 + infobox "other academic advisors"**，两位均为 1989 诺奖得主，勿把 Dehmelt 写成博士导师 |
| 出生城市 | infobox 表格作 Milwaukee，正文首句作 Wauwatosa（密尔沃基都会区），页面内两说并存，幻灯片以 Milwaukee 为准并可加注 |
| 教育 | UC Davis 1961–63 两年后转 Berkeley 获学士 1965，勿写成"本科毕业于 Davis" |
| 机构变迁 | 1975 是 National Bureau of Standards（1988 改组为 NIST），勿写"1975 加入 NIST"；2018 转 Oregon 仍以顾问身份留在 NIST 离子储藏组 |
| Franklin Medal | 2010 与 **Cirac + Zoller 三人共享**，勿写成独得 |
| 在世者 | death_date 留白，幻灯片生卒行写 `1944–` 勿加卒年 |
| 家庭关系 | 妻子 Sedna 与其人类学家父亲 Quimby 属个人生活花絮，不是科学关系，不入关系库 |
| See also 清单 | Cat state/Doppler cooling/Quantum Zeno effect 只在"参见"节出现，未入正文，禁当作正文事实展开 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| ion trap | 离子阱 | 电磁场囚禁离子的装置，勿译"离子陷阱" |
| laser cooling | 激光冷却 | 1978 首次用于离子 |
| atomic clock | 原子钟 | 计量学核心 |
| quantum logic gate | 量子逻辑门 | 1995 单原子实现 |
| quantum teleportation | 量子隐形传态 | 2004 巨型粒子首次 |
| trapped ion | 囚禁离子 | 单离子操控对象 |
| spectroscopy | 光谱学 | 基础物理检验工具 |
| ground state | 基态 | 激光冷却目标 |
| entangled states | 纠缠态 | NIST 组演示制备 |
| individual quantum systems | 单量子系统 | 诺奖理由核心词，勿译"个体量子系统" |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions（高受众 / 时间感 / 纪录片）
- **匹配理由**:
  - "时间感" 与原子钟/精密计量的主旨天然同构——Wineland 的事业就是把时间测量推到极限
  - "纪录片" 匹配 NIST 半世纪的实验长跑叙事
- **备选**（未采用）: SEA（平稳但意象偏流体）、The Invisible Light（已用于批内 Haroche）
- **本地路径**: `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/David_J._Wineland/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
