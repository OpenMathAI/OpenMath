# 施瓦兹 (Laurent Schwartz) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Hausdorff、Cartan、Lebesgue 等成品为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Laurent Schwartz (1915–2002)
- **气质关键词**: **分布理论之父、第一个法国 Fields 奖得主、托洛茨基主义活动家、收藏了两万只蝴蝶的数学家**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本：
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Laurent_Schwartz/`
- **参考模板**: `hausdorff/`, `cartan/`, `lebesgue/`, `artin/` 四个完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Laurent_Schwartz/`

输出以下信息供校验：

- **生卒日期**：1915-03-05 ~ 2002-07-04，享年 87 岁
- **国籍**：法国
- **出生地**：巴黎第 16 区，阿尔萨斯裔犹太家庭
- **博士导师**：Georges Valiron（分析学家）
- **博士论文**：1943，《Étude des sommes d'exponentielles réelles》（实指数和的研究），战时以真实姓名发表在 Clermont-Ferrand
- **主要任职机构**：
  - 1944: 格勒诺布尔大学 (Université de Grenoble)
  - 1945–1952: 南锡大学 (Université de Nancy)，在 Delsarte 和 Dieudonné 的建议下加入
  - 1952–1958: 巴黎大学理学院 (Faculté des Sciences de Paris)
  - 1958–1980: 巴黎综合理工学院 (École Polytechnique)
  - 1961–1963: 因签署《121 人宣言》（反对阿尔及利亚战争）被 Polytechnique 停职
  - 1965: 创立 Laurent-Schwartz 数学中心 (CMLS)，任首任主任
- **关键荣誉**：
  - 1950: 菲尔兹奖 (Fields Medal) — 第一位法国籍获奖者，因分布理论获奖
  - 1973: 法国科学院通讯院士
  - 1975: 法国科学院正式院士
  - Grand prix des sciences mathématiques (1964)
  - Prix de l'État (1983)
  - Concours général (数学竞赛奖)
  - Prix Francoeur
- **重要合作者/同事/学生**：
  - 博士导师: Georges Valiron
  - 博士生: **Alexander Grothendieck**、Jacques-Louis Lions、Bernard Malgrange、Maurice Audin、Gilles Pisier、Leopoldo Nachbin 等
  - 家族: 舅公 (great-uncle-in-law) Jacques Hadamard；岳父 Paul Lévy（概率论）；妻子 Marie-Hélène Lévy（数学家，复解析几何）
  - Bourbaki 同事: Jean Delsarte、Jean Dieudonné（两人力劝 Schwartz 去南锡）

### 关键时间线（18–22 个节点）：
- 1915: 3 月 5 日生于巴黎，犹太家庭，父亲是著名外科医生
- 1920s: 在 Lycée Janson-de-Sailly 和 Lycée Louis-le-Grand 接受中学教育，拉丁语、希腊语和数学全优
- 1934: 考入巴黎高等师范学校 (ENS)
- 1937: 获法国数学 agrégation（第二名）
- 1938: 与 Marie-Hélène Lévy 结婚（概率论家 Paul Lévy 之女）
- 1939–1945: 二战期间，作为犹太裔托洛茨基主义者，化名 Laurent-Marie Sélimartin 躲藏；1943 年以真实姓名发表博士论文
- 1944: 战后首先在格勒诺布尔任教一年
- 1945: 在 Delsarte 和 Dieudonné 建议下加入南锡大学，南锡成为 Bourbaki 活动的中心
- 1945–1946: 发展分布理论——核心突破
- 1950: 获菲尔兹奖——因分布理论而获奖，在剑桥 ICM 做大会报告
- 1950s: 指导 Grothendieck 博士论文（Grothendieck 后来超越了导师）
- 1952: 转入巴黎大学理学院
- 1958: 加入巴黎综合理工学院 (École Polytechnique)，改革其数学教学与研究
- 1960: 签署《121 人宣言》(Manifesto of the 121)，抗议阿尔及利亚战争
- 1961–1963: 被 Polytechnique 军方领导层停职
- 1965: 创立 Centre de mathématiques Laurent-Schwartz (CMLS)
- 1973: 当选法国科学院通讯院士
- 1975: 升为法国科学院正式院士
- 1980: 从 Polytechnique 退休
- 1983: 获 Prix de l'État
- 1997: 出版自传《Un mathématicien aux prises avec le siècle》（一位与世纪搏斗的数学家）
- 2002: 7 月 4 日在巴黎去世，享年 87 岁

### 人格特质线索：
- "数学、政治和蝴蝶"——他的三大热爱（Angelo Guerraggio 的描述）
- 托洛茨基主义积极分子——年轻时受托洛茨基影响，反对斯大林主义；1947 年脱离托洛茨基主义
- 无神论者——"我父母是无神论者，我是无神论者，我从未真正感受到自己是犹太人。"
- 蝴蝶收藏家——个人收藏了两万只鳞翅目标本，捐赠给多家博物馆，若干物种以他的名字命名
- 一位老师对他的父母说："注意，有人会说您的儿子有语言天赋，但他只对语言的科学和数学方面感兴趣：他应该成为数学家。"
- 数学与幽默——他的名言："数学有什么用？数学对物理学有用。物理学帮助我们造冰箱。冰箱用来装龙虾，龙虾帮助数学家吃得更好从而做更好的数学……"
- 作为 Bourbaki 的"局内人"——他是 20 世纪法国数学黄金时代的核心参与者，南锡-巴黎-综合理工学院一线贯穿法国分析学
- Grothendieck 的导师——这是他最大的导师成就。Grothendieck 的博士论文题目（泛函分析）正是 Schwartz 指定的，后来 Grothendieck 完全超越了分布理论的框架

---

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_schwartz_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q212081` | ⚠️ 待核 |
| 2 | `people` | name_zh | `洛朗·施瓦茨` | ⚠️ NULL |
| 3 | `people` | name_variants | `["分布论之父","菲尔兹奖捍卫者","数学家中的昆虫学家"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1915-03-05` / `2002-07-04` | ⚠️ 仅年份 |
| 6 | `people` | description | `French mathematician (1915–2002)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)`、`entomologist(2)` | ⚠️ 需补（entomologist 补字典） |
| 8 | `person_field` | 领域 | `distribution theory`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Fields 1950`（已有）、`Grand prix des sciences mathématiques`、`Prix de l'Etat`、`Concours général`、`Prix Francoeur`、`Cours Peccot`、`Heinz R. Pagels Award` | ⚠️ 部分 |
| 10 | `person_institution` | 教育/任职 | `education: ENS、Lycée Janson-de-Sailly`；`employment: Nancy、Grenoble、École polytechnique、Paris Diderot、Paris` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `France` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（8 条） | ⚠️ 仅 2 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_schwartz_relations.py` 补足。

**入库范围（8 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Georges Valiron → Schwartz | 有向 | ⚠️ 占位 |
| 学生 | Schwartz → Alexander Grothendieck | 有向 | ✅ 在库（id=7） |
| 学生 | Schwartz → Jacques-Louis Lions | 有向 | ✅ 在库（id=49） |
| 学生 | Schwartz → Bernard Malgrange | 有向 | ⚠️ 占位 |
| 同事 | Jean Dieudonné | 无向 | ✅ 在库（id=370） |
| 同事 | André Weil | 无向 | ✅ 在库（id=8） |
| 同事 | René Thom | 无向 | ✅ 在库（id=55） |
| 夫妻 | Marie-Hélène Schwartz | 无向 | ⚠️ 占位（数学家） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 泛函分析 | 分布理论 (Theory of Distributions) —— 赋予 Dirac δ 函数和 Heaviside 阶跃函数严格的数学意义 | 1945–1950 |
| PDE | 偏微分方程的现代理论 —— 分布将 Fourier 变换推广到更广的函数类 | 1950s |
| 泛函分析 | Schwartz 核定理 (Kernel Theorem) —— 广义函数的积分核表示 | 1950s |
| 泛函分析 | Schwartz 空间 —— 速降函数空间 \(\mathcal{S}\)，Fourier 变换的自然定义域 | 1950s |
| 调和分析 | Schwartz–Bruhat 函数 —— 局部紧 Abel 群上的速降函数 | 1950s–1970s |
| Banach 空间 | 圆柱测度 (Cylinder Set Measure) 与 Radonifying 算子 | 1960s–1970s |
| 半鞅理论 | 流形上的半鞅与随机微积分 | 1980s |

### ★ 施瓦兹独有的叙事线索

1. **分布理论——"合法化的非法运算"** — 物理学家一直在用 Dirac δ 函数，但数学家说它"不存在"。Schwartz 的分布理论说：它存在，只是不是普通函数，而是一个线性泛函。他让 Heaviside 的符号运算和 Dirac 的脉冲函数都有了合法的数学身份。这不是"否定"物理学家的直觉，而是"正式承认"它。
2. **第一个法国 Fields 奖** — 1950 年 Schwartz 获奖时，Fields 奖才设立 14 年（1936 首次颁发）。他是第一位法国获奖者。因为他的托洛茨基主义背景，进入美国领奖时遇到了严重困难——但他最终还是成功了。
3. **二战下的双重生存** — 犹太人 + 托洛茨基主义者 = 纳粹的头号目标。1940 年代他化名 Laurent-Marie Sélimartin 在 Clermont-Ferrand 躲藏（斯特拉斯堡大学战时迁至此处）。但他的博士论文用真名发表——一种危险的诚实。
4. **Grothendieck 的导师** — Schwartz 指导了 Grothendieck 的博士论文（泛函分析中的核空间和张量积）。Grothendieck 后来完全超越了分布理论的框架，成为 20 世纪最伟大的数学家之一。这是一段最具戏剧性的师生关系：老师是 Fields 奖得主，学生是数学史上的巨人。
5. **政治活动家** — Schwartz 不是那种只在象牙塔里的数学家。他签署了反对阿尔及利亚战争的《121 人宣言》，为此付出了被 Polytechnique 停职两年的代价。他的自传标题 "与世纪搏斗的数学家" 准确地描述了他的一生。
6. **Bourbaki 的分析学支柱** — Schwartz 不是 Bourbaki 的创始成员，但他是 Bourbaki 黄金时代（1940s-1950s）的核心参与者。南锡大学（1945-1952）在 Delsarte 和 Dieudonné 的主持下成为 Bourbaki 活动的中心，Schwartz 的分布理论正是在这个环境中孕育。
7. **蝴蝶与数学** — 这不是一条轻浮的线索。在 Schwartz 的世界观中，科学好奇心是一体的：他研究分布理论的严谨性，与他在全球收集蝴蝶标本的热情，是同一种智力品质的不同表现。两万只蝴蝶标本——那是另一个维度的"分类学"。

### 人物关系

- **Georges Valiron（博士导师）** — 法国分析学家。Schwartz 的博士论文方向是实指数和，属于经典分析，与分布理论无关。
- **Alexander Grothendieck（学生）** — 数学史上最伟大的师生关系之一。Schwartz 指导 Grothendieck 的博士论文（泛函分析），后来 Grothendieck 超越了一切框架。
- **Jacques Hadamard（舅公）** — 传奇数学家，素数定理和泛函分析的先驱。Schwartz 妻子的舅公——家族中的数学基因。
- **Paul Lévy（岳父）** — 概率论先驱。Schwartz 娶了他的女儿 Marie-Hélène（本人也是数学家，复解析几何）。
- **Marie-Hélène Schwartz（妻子）** — 数学家，研究奇异解析空间的几何。两人是 20 世纪罕见的数学夫妻档。
- **Jean Delsarte & Jean Dieudonné（Bourbaki 同事）** — 两人力劝 Schwartz 战后去南锡。南锡因此成为 Bourbaki 活动的中心之一。
- **Maurice Audin（学生）** — 法国数学家，Schwartz 的博士生。在阿尔及利亚战争期间被法国军队逮捕并杀害。Audin 之死深刻影响了 Schwartz 的政治立场。

---

## 第 5 步：设计配色方案

- **建议配色：分析紫罗兰 + 巴黎蓝 + 激进橙 + 蝴蝶绿** —— 分布理论的优雅 + Bourbaki 的结构主义 + 政治行动的激进 + 鳞翅目的自然
- 需要与已有配色完全不同：
  - Cartan：法兰西深蓝 + 几何金
  - Hilbert：普鲁士蓝 + 金
  - Grothendieck：深靛 + 金
  - Weyl：琥珀金 + 星夜紫
  - Gödel：维也纳深棕 + 古书金
  - Turing: 英伦绿 + 机械灰
  - Kolmogorov：深松绿 + 古铜金
  - von Neumann：深黑 + 电路绿
  - Noether：深紫罗兰 + 暗玫瑰金
  - Riemann：墨绿 + 银灰
  - Lebesgue：巴黎灰 + 赤陶红
  - Banach：弗罗茨瓦夫蓝 + 蜂蜜金
  - Serre：勃艮第红 + 象牙暖金
  - Hausdorff：勃艮第深红 + 古纸象牙白 + 黑灰
- 四个分类色，对应 Schwartz 的四大面向：
  - **badgedist** (分布理论/PDE) — 分析紫罗兰 `#5B2C6F`
  - **badgeSpace** (Schwartz 空间/泛函分析) — 巴黎蓝 `#1B4F72`
  - **badgeActivism** (政治活动/人权) — 激进橙 `#D35400`
  - **badgeEnto** (蝴蝶收藏/科普) — 蝴蝶绿 `#27AE60`

---

## 第 6 步：规划幻灯片序列（建议 17 页）

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《施瓦兹：赋予 ∞ 以意义的人》 / Laurent Schwartz 1915–2002
02  为什么施瓦兹改变了分析 —— 分布理论、菲尔兹奖、政治与蝴蝶

=== 早年 ===
03  巴黎之子 (1915–1939) — 从 ENS 到 agrégation，Hadamard 和 Lévy 的数学家族
04  二战下的双重身份 (1939–1944) — 化名躲藏，真名发表论文

=== 分布理论 ===
05  分布理论的诞生 (1945–1950) — Dirac δ 不再是"不存在的函数"
06  Schwartz 空间 \(\mathcal{S}\) 与核定理 — 速降函数、Fourier 变换的自然家园
07  菲尔兹奖 (1950) — 第一位法国获奖者，政治背景下的美国之行

=== 南锡与 Bourbaki ===
08  南锡的黄金时代 (1945–1952) — Bourbaki 的分析学支柱，Delsarte-Dieudonné 的邀请
09  Grothendieck 的导师 — 数学史上最伟大的师生关系之一

=== 巴黎与政治 ===
10  从索邦到 Polytechnique (1952–1965) — 改革法国的数学教育
11  《121 人宣言》与停职 (1960–1963) — 为了良知付出代价

=== 人物的多面 ===
12  数学、政治与蝴蝶 — "他的三大热爱"：分布、托洛茨基、两万只鳞翅目标本
13  Maurice Audin — 学生之死与政治觉醒

=== 遗产 ===
14  施瓦兹的遗产 — 分布 · 核定理 · \(\mathcal{S}\) 空间 · Bourbaki 分析
15  思想回响 — 他让物理学家可以合法使用 δ 函数

=== 结尾 ===
16  结束页 — 主题句：他赋予了 Dirac 的 δ 函数以数学意义上的存在。然后，他为良知付出了被驱逐的代价。
```

---

## 第 9 步：史实审查

### 施瓦兹特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **分布理论 ≠ 他发明了 δ 函数** | Dirac 在 1927 年引入 δ 函数，但它是形式化的。Schwartz 的工作是给了它严格的数学基础（作为广义函数的线性泛函）。**不要写"Schwartz 发明了 Dirac δ 函数"——他"合法化"了它。** |
| **Grothendieck 的论文方向** | Grothendieck 的博士论文是关于泛函分析中的核空间和张量积，这是 Schwartz 指定的方向。后来 Grothendieck 完全转向代数几何。两者不是"共同工作"——是导师指定了一个方向，学生完成了它，然后走向了完全不同的领域。 |
| **Bourbaki 的身份** | Schwartz 不是 Bourbaki 的创始成员。他是 Bourbaki 黄金时代的核心参与者。措辞要准确。 |
| **托洛茨基主义的年限** | Schwartz 1947 年脱离托洛茨基主义。不要暗示他终身是托洛茨基主义者。 |
| **Maurice Audin** | Audin 是 Schwartz 的学生，在阿尔及利亚战争中被法国军队杀害。这是法国殖民史上最黑暗的篇章之一。Schwartz 签署《121 人宣言》与此事有关。措辞要尊重历史，不煽情。 |
| **与 Hadamard 的关系** | 不是直系血亲。Schwartz 的妻子 Marie-Hélène Lévy 的母亲是 Hadamard 的侄女。所以 Hadamard 是 Schwartz 的 "great-uncle-in-law"（舅公）。 |
| **菲尔兹奖的政治困难** | 因为托洛茨基主义背景，Schwartz 进入美国领奖遇到严重困难，但最终成功了。不要夸大他"被拒绝入境"——他最终进入了。 |
| **自传标题** | 法语原标题：《Un mathématicien aux prises avec le siècle》（1997）。英译本：*A Mathematician Grappling with His Century*（2001）。中文可译为《一位与世纪搏斗的数学家》。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| distribution | 分布 / 广义函数 | 不要译为"分配"。Sobolev 也独立发展了类似概念 |
| Schwartz space | Schwartz 空间 / \(\mathcal{S}\) 空间 | \(\mathcal{S}\) 是速降函数空间 |
| Schwartz kernel theorem | Schwartz 核定理 | 不要与"积分核"混淆——是广义函数的核表示 |
| Dirac delta function | Dirac δ 函数 | Schwartz 将其合法化为分布，不是发明它 |
| tempered distribution | 缓增分布 | \(\mathcal{S}'\) — Schwartz 空间的对偶 |
| cylinder set measure | 圆柱集测度 | 无穷维空间上的测度推广 |
| Radonifying operator | Radonifying 算子 | Banach 空间理论 |
| Centre de mathématiques Laurent-Schwartz | Laurent-Schwartz 数学中心 (CMLS) | 1965 年创立 |
| Manifesto of the 121 | 《121 人宣言》 | 1960 年，反对阿尔及利亚战争 |
| Lepidoptera | 鳞翅目 | 蝴蝶和蛾类——Schwartz 收藏了两万只 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一次/第一个"断言** | "第一个定义分布理论的人" — 要加上：Sobolev 在苏联独立发展了类似概念。Schwartz 的贡献是给出了完整的对偶框架和核定理。 |
| **"δ 函数不存在"的叙事** | 不要过度渲染 "Dirac 被数学家嘲笑"——实际上 Dirac 的符号运算在物理学中运行良好。分布理论是"形式化"，不是"拯救"。 |
| **Bourbaki 过度简化** | Bourbaki 是集体笔名，不是"一个学派"。不要暗示 Schwartz "代表 Bourbaki"做分析。 |
| **自传引语** | Schwartz 的自传是 1997 年出版的，引用的语气和措辞要一致。 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

> **核心原则：Beamer 写完后，必须回到本地 Wikipedia 存档（page.md + metadata.json），逐项对照审核。**

### 终审执行流程

```
1. 打开 pages/Laurent_Schwartz/page.md，从头到尾逐段阅读全文
2. 同时打开 Laurent_Schwartz_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### 10 项终审清单

| # | 检查项 | 方法 | 高危信号 |
|:--:|------|------|---------|
| 1 | **事实性错误** | 每个日期/人名/机构与 page.md 逐条对照 | 任何与 Wikipedia 不一致的年份、地名、人名 |
| 2 | **翻译/术语错误** | 所有数学术语与 Wikipedia 英文原词对照 | 概念性误译 |
| 3 | **重大遗漏** | 扫描 Wikipedia 目录，对比 Beamer 覆盖 | 标志性专著/定理遗漏 |
| 4 | **结构性错误** | 检查时间线是否按生平顺序 | 时间跳跃混乱、因果倒置 |
| 5 | **编译告警** | 分析 Overfull hbox/vbox | vbox > 10pt 或 hbox > 50pt 需修复 |
| 6 | **引语来源** | 每个加引号的句子必须在 page.md 中能找到 | 中文引号内的句子无法验证 |
| 7 | **年份精确性** | slide 标题中的年份 | 写作年份 ≠ 发表年份 |
| 8 | **人物关系** | metadata.json 与 Beamer 一致 | 把 Hadamard 写成"祖父"而非"舅公" |
| 9 | **荣誉/获奖** | metadata.json 与封面页一致 | 遗漏 Fields 奖 |
| 10 | **出版年份** | Wikipedia 书目栏与 Beamer 一致 | 分布理论专著 1950 vs 1951，自传 1997 法文原版 vs 2001 英译 |

### 优先级定义

| 优先级 | 定义 | 潜在案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | 博士论文年份标错、遗漏关键任职机构、人物关系写错 |
| 🟡 P1 | **来源存疑/模糊** | 无法验证的引语、模糊的年份表述 |
| 🟢 P2 | **重要遗漏** | 未提及的标志性著作、可选轶事 |
| ⚪ P3 | **可选补充** | 冷门趣闻、衍生影响 |

### ⚠️ Schwartz 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **分布理论 ≠ 发明 δ 函数** | 最容易犯的错误 | page.md 搜索 "Dirac" |
| **Hadamard 关系** | 是舅公 (great-uncle-in-law)，不是祖父 | page.md 搜索 "Hadamard" |
| **化名 vs 真名** | 战时化名 Laurent-Marie Sélimartin，但论文真名发表 | page.md 搜索 "Sélimartin" |
| **Grothendieck 论文方向** | 泛函分析（核空间），不是代数几何 | page.md 搜索 "Grothendieck" |
| **菲尔兹奖年份** | 1950，剑桥 ICM | page.md 搜索 "Fields Medal" 或 "1950" |
| **南锡 → 巴黎 → Polytechnique** | 1945-1952 南锡，1952 巴黎，1958 Polytechnique | page.md 搜索 "Nancy" "Polytechnique" |
| **停职年份** | 1961–1963，因签署《121 人宣言》 | page.md 搜索 "suspend" 或 "Manifesto" |
| **CMLS 创立年份** | 1965，非 1958 | page.md 搜索 "Centre" |
| **自传标题** | 法文原版 1997，英译 2001 | page.md 搜索 "autobiography" 或 "prises" |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

施瓦兹的气质：**分析的结构优雅 + 政治行动的激进 + 蝴蝶收藏的宁静** — 紫色到绿色的光谱。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Cinematic Experience | alex-productions | `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` | 高张力电影感——分布理论与 Bourbaki 的结构主义，理性的戏剧 |
| ★★★ | The Flow of Time | alex-productions | `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` | 时间感纪录片风——穿越战争、南锡、巴黎、Polytechnique 的一生 |
| ★★ | Awaken | alex-productions | `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` | 明亮鼓舞——年轻 Schwartz 的智力觉醒 |
| ★ | Daylight | alex-productions | `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` | 明亮轻快——蝴蝶收藏与科普精神 |

---

## 第 16 步：第二次 Wikipedia Review（Round 2）

> **核心原则：第一次 review 修复完所有 P0 后，必须进行第二次 review。**
> 第二轮的重点是：**检查第一轮修复是否引入了新的错误**，以及**逐页细读 Wikipedia 中容易被忽略的段落**。

### Round 2 执行流程

```
1. 重新打开 Wikipedia page.md，换一个角度阅读（这次从末尾往前读）
2. 对照已修复的 Beamer 源码，逐页 check
3. 特别注意：第一轮修复的 P0 项是否留下了新的不一致
4. 输出 Round 2 Review 报告
5. 修复新发现的问题 → 重新编译 → 提交
```

---

## 第 18 步：Makefile

> **模板来源**：直接复制 `Henri_Lebesgue/Makefile` 或 `Elie_Cartan/Makefile`，只需修改 `MAIN` 变量。

### 创建步骤

1. 在 Beamer 目录下创建 `Makefile`（参照 `Henri_Lebesgue/Makefile` 逐字复制）
2. 修改第 1 行：`MAIN = Laurent_Schwartz_zh`
3. 修改第 2 行：`VIDEO_NAME = Laurent_Schwartz_zh`
4. 其余不变

### 目标说明

| 目标 | 命令 | 效果 |
|:--|------|------|
| `make` / `make pdf` | `latexmk -xelatex` | 编译 PDF，自动处理交叉引用 |
| `make images` | `pdftoppm -png -r 600` | 将 PDF 每页转为 600dpi PNG |
| `make video` | `ffmpeg` concat PNG + BGM | 合成幻灯片视频（如目录下有 .wav 则自动混音） |
| `make clean` | 删除 aux/log/out/xdv | 清理中间文件 |
| `make distclean` | clean + 删除 PDF/PNG/MP4 | 完全清理 |

### 验证

```bash
# 在 Beamer 目录下运行
cd mathematician/presentations/Laurent_Schwartz
make clean && make
# 应输出：Successfully generated Laurent_Schwartz_zh.pdf
```

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Schwartz 的独特性在于"多面性"——纯数学家、政治活动家、蝴蝶收藏家。这三个维度缺一不可。
> 2. **分布理论 ≠ 发明 δ 函数**。Dirac 发明了 δ 函数（形式化），Schwartz 给了它数学合法性。用"合法化"而非"发明"。
> 3. Grothendieck 的师生关系是最大的戏剧性——导师是 Fields 奖得主，学生超越了整个数学。
> 4. 化名与真名的对比（Sélimartin 躲藏 vs 论文真名发表）是二战叙事的核心张力。
> 5. 蝴蝶收藏不是肤浅的花絮——它和分布理论来自同一种分类思维。
> 6. 《121 人宣言》和停职：Schwartz 为良知付出了代价，这让他的故事不止于数学。
> 7. Maurice Audin 之死（学生被法国军队杀害）是政治觉醒的关键事件，需要尊重地处理。
> 8. 结尾主题句应体现他的双重贡献：数学上——他赋予了 δ 函数以存在；道德上——他为良知付出了被驱逐的代价。
> 9. **⚠️ 与 Hadamard 的关系务必核对**：不是直系血亲，而是舅公（great-uncle-in-law，通过妻子的家族）。
> 10. **⚠️ 不要暗示 Schwartz 是 Bourbaki 创始人**——他是活跃参与者，但不是创始成员。
