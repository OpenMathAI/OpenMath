# 物理学家立传提示词（Serge Haroche · 2012 诺贝尔物理学奖）

> **本文件是 OpenPhysicist 21 世纪批次的人物专属立传提示词**，以 Serge Haroche（2012 诺贝尔物理学奖，腔量子电动力学）为目标人物。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Serge Haroche（塞尔日·阿罗什），2012 诺贝尔物理学奖（与 David J. Wineland 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇另需突出**实验量子物理的「控制-测量」主线**——从激光光谱学到单光子操控，一条把量子世界逐个粒子驯服的实验长卷。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Serge Haroche（1944-09-11 生于卡萨布兰卡，在世）
- **气质关键词**：**单光子的驯兽师、腔量子电动力学的旗手、量子退相干的目击者** —— 2012 诺贝尔物理学奖获奖理由：
  > "for ground-breaking experimental methods that enable measuring and manipulation of individual quantum systems"（因其能够实现测量和操控单个量子系统的突破性实验方法）
- **设计母题**：**被囚禁的光（light in a box）**。超导微波腔中仅存数个光子、被里德堡原子逐个"目送"——镜子盒子里的光在量子与经典边界上起舞，是比泛泛「量子」更贴合 Haroche 的视觉语言。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Serge_Haroche/page.md`（✅ 已有本地）
- **html/images**：待下载 —— Wikipedia URL：`https://en.wikipedia.org/wiki/Serge_Haroche`（第 0 步下载 `Serge_Haroche.html` 与 infobox 肖像到 `images/`）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（事实基准如下）；html 与 images/ 待下载（URL 见上）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1944-09-11 生于卡萨布兰卡（时属法属摩洛哥），在世（death_date 留白）
  - 国籍：法国（French citizenship）；家族 1956 年法属摩洛哥保护领终结后离开摩洛哥定居法国
  - 家庭：父 Albert Haroche（1920–1998，拉巴特受训律师，摩洛哥犹太家庭）；母 Valentine（出生敖德萨，医师家庭）；塞法迪与阿什肯纳兹混合血统；妻子社会学家 Claudine Haroche，育有两子；歌手 Raphaël 是其侄
  - 教育：Lycée Louis-le-Grand → 巴黎高等师范学院（ENS）；巴黎第六大学（Pierre and Marie Curie University）博士 1971
  - 博士导师：Claude Cohen-Tannoudji（1997 诺贝尔物理学奖得主）；论文方向「缀饰原子」（dressed atoms，1967–1971）
  - 博士后：斯坦福大学 1972–1973，Arthur Leonard Schawlow 团队
  - 任职机构：CNRS 研究员 1967–1975（Kastler–Brossel 实验室）；巴黎第六大学教授 1975–；兼任 École polytechnique（1973–1984）、MIT（1980）、Harvard（1981）、Yale（1984–1993）、CNAM（2000）；ENS 物理系主任 1994–2000；法兰西公学院量子物理讲席教授 2001–；2012-09 当选法兰西公学院院长（administrator）；罗马第一大学费米讲席 2022
  - 关键荣誉：Einstein Prize for Laser Science 1988；APS Fellow 1990；Humboldt Prize 1992；Albert A. Michelson Medal 1993；Charles Hard Townes Award 2007；CNRS Gold Medal 2009；Herbert Walther Award 2010；Nobel 2012（与 Wineland 共享）；IEEE Honorary Membership 2017；Grand Officer of the Legion of Honour 2017
  - 知名学生：page.md 无载（禁写）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点，见幻灯片序列）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Haroche 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cavity quantum electrodynamics | 腔量子电动力学 | 里德堡原子 × 超导微波腔，单光子操控 | 核心贡献页 |
| 1 | quantum optics | 量子光学 | 量子拍、超辐射、激光光谱新方法 | 早期研究页 |
| 2 | atomic physics | 原子物理 | 里德堡原子、缀饰原子理论 | 早年/核心页 |
| 3 | laser spectroscopy | 激光光谱学 | 博士后起发展的新光谱方法 | 早期研究页 |
| 4 | quantum decoherence | 量子退相干 | 1996 ENS 实验观测，量子-经典边界 | 退相干页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Claude Cohen-Tannoudji | advisor（对方是导师） | 巴黎六大博士导师（1967–1971 缀饰原子论文），1997 诺贝尔物理学奖得主 |
| co-honored | David J. Wineland | 无向 | 2012 诺贝尔物理学奖共享（单量子系统测量与操控的突破性实验方法） |
| colleague | Arthur Schawlow | 无向 | 1972–1973 斯坦福访问博士后，在 Schawlow（1981 诺奖得主）团队 |
| colleague | Jean-Michel Raimond | 无向 | 长期腔 QED 合作者，合著《Exploring the Quantum》（Oxford 2006） |

#### 4.5.1 入库操作

- 以 `name_en='Serge Haroche'`（qid Q109588，复用库内 stub id=2446）为中心写入 `person_relation`
- 对手方用库内规范名：`Claude Cohen-Tannoudji`（id=2445）、`David J. Wineland`（id=2834）、`Arthur Schawlow`（id=2488）；Raimond 库内无记录，seed 以规范全名 `Jean-Michel Raimond` 建 stub
- 方向约定：师生有向（advisor=对方是导师）；同事/共同荣誉无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深邃、精密、量子边界的光影感
- **配色**：深紫（囚禁之光的神秘）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeCavity` 腔量子电动力学 — 靛蓝 `#4C5FD5`
  - `badgeRydberg` 里德堡原子 — 青绿 `#0E7C7B`
  - `badgeDecoherence` 量子退相干 — 玫瑰 `#C4204F`
  - `badgeSpectro` 激光光谱学 — 琥珀 `#E07B30`
- **主色**：`#52307C`（深紫，批内唯一）
- **背景母题**：柔和气泡（稀疏实心圆）——腔中离散驻波光子，大小错落呼应「单量子系统的可数性」

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）：左头像 + 右信息网格（生卒、出生地、国籍、教育、师承、任职、主要荣誉、核心领域）。
4. 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 腔量子电动力学旗手 / Serge Haroche 1944– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地卡萨布兰卡、ENS/巴黎六大、师承 Cohen-Tannoudji、法兰西公学院、Nobel 2012、核心领域）
03  核心贡献概览 — 激光光谱学 / 里德堡原子 / 腔 QED / 量子退相干
04  早年：卡萨布兰卡到巴黎 (1944–1967) — 犹太家庭、1956 迁法、Louis-le-Grand、ENS
05  博士：Cohen-Tannoudji 门下 (1967–1971) — 缀饰原子、量子拍、超辐射
06  博士后与讲席岁月 (1972–1993) — 斯坦福 Schawlow 团队、巴黎六大教授、Yale 1984–1993
07  里德堡原子与微波腔：把光关进盒子 (核心贡献页)
08  1996 量子退相干：亲眼目睹薛定谔猫（ENS，与同事共同完成）
09  单量子系统的测量与操控 — 诺奖方法：无损目击光子、量子逻辑操作
10  荣誉与认可 — Nobel 2012 · CNRS Gold Medal 2009 · Townes 2007 · 2017 IEEE/Légion d'honneur
11  《Exploring the Quantum》与科学传播 — 与 Raimond 合著、法兰西公学院院长 (2012)
12  遗产：量子信息时代的实验基石
13  结尾
```

- 公式框：page.md 无公式，用**概念图式**——「原子 ↔ 腔模耦合（Rabi 振荡示意）」，并注明"示意图，非 page.md 公式"。

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

- 版式：每页写完 `make clean && make`，pdftoppm 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

**Haroche 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方措辞强调"测量与操控单个量子系统的突破性实验方法"，勿写成"量子纠缠实验"（那是 Aspect 2022）或"激光冷却"（那是导师 Cohen-Tannoudji 1997） |
| 与 Wineland 分工 | Haroche 用**超导微波腔 + 里德堡原子**，Wineland 用**离子阱**；两条路线共享 2012 奖，方法勿混淆 |
| 博士导师 | Cohen-Tannoudji 是 1997 诺奖得主（激光冷却），获奖晚于学生 Haroche，勿写"同年"或"早于" |
| Schawlow 身份 | 斯坦福 1972–73 是**博士后站**，Schawlow（1981 诺奖）不是博士导师，方向勿写反 |
| Raimond 身份 | 是长期合作者与合著者，page.md 未载师生关系，勿写"学生" |
| 出生地 | 卡萨布兰卡（时属法属摩洛哥），国籍口径 France，勿写"摩洛哥裔物理学家" |
| 退相干实验 | 1996 年是"与 ENS 同事共同完成"（page.md 原文 with colleagues），勿写独自完成 |
| 荣誉年份 | CNRS Gold Medal 2009、Herbert Walther 2010、Townes 2007、Michelson 1993、Einstein Prize for Laser Science 1988，勿错位 |
| 在世者 | death_date 留白，幻灯片生卒行写 `1944–` 勿加卒年 |
| 家庭关系 | 侄子 Raphaël 是歌手/演员，仅属个人生活花絮，不是科学关系，不入关系库 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| cavity quantum electrodynamics | 腔量子电动力学（腔 QED） | 非"量子电动力学腔" |
| Rydberg atom | 里德堡原子 | 巨型高激发态原子，对微波敏感 |
| quantum decoherence | 量子退相干 | 非"去相干"，指量子叠加的相干性丢失 |
| dressed atom | 缀饰原子 | 原子+场模的联合量子态，博士论文主题 |
| quantum beat | 量子拍 | 相干叠加能级的振荡 |
| superradiance | 超辐射 | 集体增强辐射 |
| superconducting cavity | 超导微波腔 | 囚禁少量光子的反射腔 |
| quantum logic | 量子逻辑 | 量子信息处理的基本操作 |
| individual quantum systems | 单量子系统 | 诺奖理由核心词，勿译"个体量子系统" |
| photon | 光子 | 被测量的对象，"光的粒子" |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（纪录片 / 电影 / 稳重）
- **匹配理由**:
  - "纪录片/稳重" 匹配 Haroche 半个世纪的实验长跑——从 1967 缀饰原子到 1996 退相干到 2012 诺奖
  - "光" 意象与被囚禁于腔中的微波光子天然呼应，是曲库中与本人物最贴的隐喻
- **备选**（未采用）: The Flow of Time（时间感稍泛）、SEA（平稳但意象弱）
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Serge_Haroche/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
