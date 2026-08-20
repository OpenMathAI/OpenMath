# 德利涅 (Pierre Deligne) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, milnor, morse, zariski, whitney, chevalley, hopf, chern 的版式。

---

## 背景信息

- **目标**: Pierre Deligne (1944– , 在世)
- **气质关键词**: **Weil 猜想的征服者、Grothendieck 的火炬手、代数几何与数论融合的大师、Fields+Wolf+Abel 三冠王**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Pierre_Deligne/`

## 第 0 步：Wikipedia 校验

- **全名**：Pierre René, Viscount Deligne（2006 年被比利时国王封为子爵）
- **生卒**：1944-10-03 ~ (在世，81 岁)
- **国籍**：比利时
- **出生地**：Etterbeek, Brussels, Belgium
- **博士导师**：**Alexander Grothendieck**（巴黎南大学 Orsay, 1972 年博士）⚠️ 原提示词错误——不是 René Thom！Wikipedia 明确列出 Grothendieck 为唯一博士导师
- **博士论文**：1972，《Théorie de Hodge》（Hodge 理论）。早前 1968 年在 ULB 的本科论文题为《Théorème de Lefschetz et critères de dégénérescence de suites spectrales》
- **教育**：Athénée Adolphe Max (中学) → Université libre de Bruxelles (ULB, BS) → Paris-Sud University (Orsay, PhD 1972)
- **任职**：IHÉS (1965–1984, 永久成员 1970–)、普林斯顿高等研究院 IAS (1984–至今)
- **荣誉**：Fields 奖 (1978)、Crafoord 奖 (1988)、Balzan 奖 (2004)、Wolf 奖 (2008)、Abel 奖 (2013)
- **爵位**：2006 年被比利时国王阿尔贝二世封为**子爵 (vicomte)**
- **学生**：Lê Dũng Tráng, Miles Reid, Michael Rapoport
- **合作者**：Grothendieck (导师), Serre, Mumford, Lusztig, Griffiths, Beilinson, Bernstein

### 时间线
- 1944-10-03: 生于比利时 Etterbeek (布鲁塞尔)
- 1965: 开始在 IHÉS 与 Grothendieck 合作
- 1966: ULB 本科毕业
- 1968: 与 Serre 合作——ℓ-adic 表示、模形式的泛函方程
- 1969: 与 Mumford 合作——Deligne–Mumford 叠 (stacks)，模空间理论革命
- 1970: 成为 IHÉS 永久成员
- 1972: 在 Grothendieck 指导下获博士（Paris-Sud, Orsay），论文：《Théorie de Hodge》
- 1973: **证明 Weil 猜想**（Riemann 假设在有限域上的类比）—— 20 世纪数学最高成就之一
- 1974: 发表 Weil I —— 首次完整证明。推论：Ramanujan–Petersson 猜想
- 1976: 与 Lusztig 合作——Deligne–Lusztig 理论，有限李型群的表示论
- 1978: **Fields 奖** (33 岁，赫尔辛基 ICM)
- 1980: 发表 Weil II —— 更一般的"权 (weights)"理论框架
- 1984: 从 IHÉS 转入 IAS Princeton
- 1988: Crafoord 奖
- 1990: Tannakian 范畴——Grothendieck Festschrift 论文
- 2004: Balzan 奖
- 2006: 被封为子爵
- 2008: Wolf 奖
- 2013: **Abel 奖**——三大顶级数学奖大满贯 (Fields + Wolf + Abel)
- 至今: IAS 荣休教授，仍在活跃研究

### 人格画像
Deligne 是 Grothendieck 最杰出的学生，但他与老师的风格截然相反：Grothendieck 宏大壮阔、滔滔不绝；Deligne 极简深邃、惜字如金。他的论文以简短著称——Weil I 仅 35 页，却改变了数学史。他以沉默和思考闻名——在数学会议上常常一言不发地坐着，然后说出一句话让所有人醍醐灌顶。当 Grothendieck 号召数学家抵制学术体制时，Deligne 是少数公开拒绝的人之一，理由简单而有力："数学大于任何个人。"他对名利毫不在意——获得 Abel 奖后，他说："我只是运气好，生在了一个数学的黄金时代。"他的论文风格被誉为"数学写作的典范"——每一句都是精炼的结果，没有一句废话。

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_deligne_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q334045` | ⚠️ 待核 |
| 2 | `people` | name_zh | `皮埃尔·德利涅` | ⚠️ NULL |
| 3 | `people` | name_variants | `["Weil 猜想的终结者","动机理论的建筑师","贝尔格莱德学派之外的反叛天才"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1944-10-03` / `NULL`（在世） | ⚠️ 仅年份 |
| 6 | `people` | description | `Belgian mathematician (1944–)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `algebraic geometry`、`number theory`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Fields 1978`、`Wolf 2008`、`Abel 2013`（已有）；补 `Crafoord 1988`、`Balzan 2004`、`Cours Peccot`、`荣誉博士` | ⚠️ 部分 |
| 10 | `person_institution` | 教育/任职 | `education: Brussels、Paris-Sud`；`employment: IHÉS、IAS` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `Belgium` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（7 条） | ⚠️ 仅 3 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_deligne_relations.py` 补足。

**入库范围（7 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Alexander Grothendieck → Deligne | 有向 | ✅ 在库（id=7） |
| 学生 | Deligne → Michael Rapoport | 有向 | ⚠️ 占位 |
| 学生 | Deligne → Miles Reid | 有向 | ⚠️ 占位 |
| 合作者 | David Mumford | 无向 | ✅ 在库（id=36，Deligne–Mumford 叠） |
| 同事 | Jean-Pierre Serre | 无向 | ✅ 在库（id=12） |
| 同事 | Alexander Beilinson | 无向 | ✅ 在库（id=194） |
| 同事 | David Kazhdan | 无向 | ✅ 在库（id=439） |

- 缺失人物（2 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 代数几何 | **证明 Weil 猜想** (Riemann 假设类比) | 1973/1974 |
| 代数几何 | **Weil II —— 权 (weights) 理论** | 1980 |
| 代数几何 | **混合 Hodge 结构** | 1970s |
| 表示论 | **Deligne–Lusztig 理论** | 1976 |
| 代数几何 | **Deligne–Mumford 叠 (stacks)** | 1969 |
| 代数几何 | **Perverse sheaves (反常层)** — 与 Beilinson, Bernstein, Gabber | 1980s |
| 代数几何 | **绝对 Hodge 循环** | 1980s |
| 数论 | **Tannakian 范畴** — motives 理论的基础 | 1990 |
| 数论 | **Ramanujan–Petersson 猜想证明** | 1974 |
| 拓扑 | **Kähler 流形的实同伦论** — 与 Griffiths, Morgan, Sullivan | 1975 |
| 数学物理 | **Riemann–Hilbert 对应** 的高维推广 | 1980s |

### ★ 叙事主线
1. **Weil 猜想的证明 (1973)** — 1949 年 Weil 提出有限域上代数簇的四个猜想。前三个由 Grothendieck 团队（étale 上同调）解决。第四个——Riemann 假设的类比——所有人都认为不可能。Deligne 在 1973 年独自完成了证明。这是 20 世纪数学的最高成就之一，堪比 Andrew Wiles 证明费马大定理。
2. **Grothendieck 的火炬手** — Grothendieck 建立了 étale 上同调的宏伟框架，解决了前三个 Weil 猜想，但第四个超出了他的能力。Deligne 接过了火炬——他用 Grothendieck 的语言完成了 Grothendieck 未能完成的工作。师徒二人的关系是 20 世纪数学最动人的故事之一。
3. **权 (weights) 的瑜伽** — Deligne 的核心哲学：每一个代数簇上的上同调类都有一个"权"——一个整数，衡量它在 Frobenius 作用下的尺度。Weil II (1980) 将这一思想发展为系统的理论。权的瑜伽统一了 Hodge 理论和 Galois 表示。
4. **三冠加冕** — Fields 奖 (1978)、Wolf 奖 (2008)、Abel 奖 (2013)。历史上同时获得这三项最高数学荣誉的数学家屈指可数。加上 Crafoord 奖和 Balzan 奖——五项大奖大满贯。
5. **沉默的天才** — 他的论文短到不可思议：Weil I 仅 35 页。他能在沉默中思考数小时。Grothendieck 说他"从来不说话，但一开口就是对的"。
6. **拒绝导师的号召** — 当 Grothendieck 号召抵制学术界时，Deligne 写道："我不同意你。数学比我们所有人都重要。"这是勇气——对最敬重的人说"不"。

## ⚠️ 史实陷阱
- **博士导师** — **不是 René Thom！** Wikipedia 和 Wikidata 都列出 Grothendieck 为唯一博士导师。博士授予机构是 Paris-Sud (Orsay)，不是巴黎大学。原提示词错误。
- **博士年份** — 1972 年，不是 1968 年。1968 年他还在 IHÉS 与 Serre 合作。原提示词错误。
- **Weil 猜想证明年份** — 1973 年完成证明，1974 年发表。不要混淆。
- **Weil 猜想的四个部分** — (1) 有理性——Dwork 1960 (2) 泛函方程——Grothendieck 等人 (3) Betti 数——Grothendieck 等人 (4) Riemann 假设类比——**Deligne 1973**。四个猜想由不同人解决，不是一个人！
- **Weil I 与 Weil II** — Weil I (1974) 证明猜想。Weil II (1980) 建立一般框架。两个工作相隔六年。
- **Grothendieck 决裂** — 不是个人决裂。Grothendieck 在 1970 年离开 IHÉS 并逐渐与学术圈断绝关系。Deligne 仍尊重他，只是不同意他的政治立场。
- **爵位** — 2006 年被封为子爵 (vicomte)。全名 Pierre René, Viscount Deligne。比利时贵族。不要遗漏！
- **仍在世** — 不用过去时。

## ⚠️ 终审高危
| 高危点 | 正确值 | 常见错误 |
|--------|--------|----------|
| 博士导师 | Grothendieck (Paris-Sud 1972) | René Thom / 1968 |
| Weil 猜想归属 | 4个猜想中 Deligne 仅证第4个 | "全部由 Deligne 证明" |
| Weil I 发表年 | 1974 (证明 1973) | 1973 |
| Fields 奖 | 1978, Helsinki ICM | 1974 |
| 爵位 | 2006 被封为子爵 | 遗漏 |
| Grothendieck 关系 | 尊重但不同意 | "决裂"或"背叛" |
| 在世 | 仍然在世 (81岁) | 使用过去时 |

## 配色：比利时黑 + 金 + 红 + 代数靛
- **badgeWeil** (Weil 猜想) — 比利时黑 `#1A1A1A`
- **badgeHodge** (Hodge 结构/权) — 比利时金 `#FDDA24`
- **badgeRep** (表示论) — 比利时红 `#EF3340`
- **badgeLegacy** (遗产/IAS) — 代数靛 `#2C1A5E`
- **coveraccent** — 代数靛 `#2C1A5E`
- **coverprimary** — 墨色 `#111827`
- **bgmain** — 暖象牙白 `RGB{248,246,243}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
使用 `\openmathslide`

### 1. 封面 — 《德利涅：Weil 猜想的征服者》
- 大标题：皮埃尔·德利涅
- 副标题：Pierre Deligne · 1944 —
- 标签：Weil 猜想 · 混合 Hodge 结构 · Deligne–Lusztig 理论 · Perverse Sheaves
- 底部：Fields 1978 · Wolf 2008 · Abel 2013 · 比利时子爵 · IAS Princeton
- 顶部右侧：头像

### 2. Hook — 有限域上的 Riemann 假设
- 四个面板：(1) Weil 猜想 1973——Riemann 假设的有限域类比 (2) 权的瑜伽——每个上同调类都有"权" (3) 三冠加冕——Fields+Wolf+Abel (4) Grothendieck 的火炬手——接过了étale上同调的使命
- 底部金句："在有限域的世界里，Riemann 假设是真的——他证明了它。"

### 3. 布鲁塞尔的天才少年 (1944–1966)
- **1944** · 生于比利时 Etterbeek（布鲁塞尔）。不是巴黎高师，不是 Princeton——他是比利时人。
- **中学** · Athénée Adolphe Max——布鲁塞尔的一所普通中学。少年时期就表现出惊人的数学天赋。
- **ULB (1966)** · 布鲁塞尔自由大学毕业。论文：Lefschetz 定理与谱序列退化准则。
- 底部金句："布鲁塞尔的一个小镇男孩——没有人能预见他将征服 20 世纪数学的最高峰之一。"

### 4. Grothendieck 的火炬手 (1965–1972)
- **1965** · 开始在 IHÉS 与 Grothendieck 合作。核心课题：用概形论推广 Zariski 主定理。
- **1968** · 与 Serre 合作——模形式附带的 ℓ-adic 表示的突破性成果。
- **1969** · 与 Mumford 合作——Deligne–Mumford 叠 (stacks)，完全改变了模空间理论。
- **1972** · 在 Grothendieck 指导下获博士。论文：《Théorie de Hodge》。
- 底部金句："他来到 IHÉS 时是所有人口中的'那个比利时小孩'——离开时已经是 Grothendieck 最杰出的弟子。"

### 5. Weil 猜想 (1949–1973) — 二十四年磨一剑
- **1949 · André Weil 提出四个猜想**：有限域上代数簇的 ζ 函数的 (1) 有理性 (2) 泛函方程 (3) Betti 数 (4) Riemann 假设类比。
- **1960 · Dwork** 证明有理性。**1960s · Grothendieck** 用 étale 上同调证明 (2) 和 (3)。第四个——Riemann 假设类比——悬而未决。
- **1973 · Deligne** 独自完成第四个猜想的证明。用"权的瑜伽"——证明 Frobenius 自同态的特征值恰好具有适当的绝对值。
- 底部金句："Weil 在 1949 年提出猜想时，Deligne 才 5 岁。24 年后，他给出了答案。"

### 6. Weil I (1974) — 一篇 35 页的论文改变了数学史
- **1974 年发表**：《La conjecture de Weil. I》——仅 35 页。附有 Grothendieck 的 20 页注解。
- **核心技巧**：权的概念 + Lefschetz pencil + 对 Hodge 理论的深刻类比。每一步都精确如外科手术。
- **推论**：**Ramanujan–Petersson 猜想**——一个困扰数学界半个多世纪的数论难题。模形式的 Fourier 系数的上界估计。
- **影响力**：这篇论文的引用次数不计其数。它证明了 étale 上同调是代数几何的终极武器。
- 底部金句："35 页——没有一句多余的话。这是数学写作的极致典范。"

### 7. Weil II (1980) — 权的瑜伽
- **1980 年发表**：《La conjecture de Weil. II》——更一般的框架。
- **权的概念 (weights)**：每一个 ℓ-adic 上同调类都有一个整数——"权"，衡量 Frobenius 作用下的缩放行为。纯权类满足 Riemann 假设型估计。
- **混合 Hodge 结构**：Deligne 将 Hodge 理论与 Galois 表示统一在"权"的框架下。这是代数几何中连接复几何和数论的最深刻桥梁之一。
- **影响**：权的概念现在渗透到代数几何的每一个角落。从 Shimura 簇到 Langlands 纲领，从 motives 到 perverse sheaves。
- 底部金句："权——一个简单的整数，统一了 Hodge 理论和 Galois 表示。这就是 Deligne 的数学哲学。"

### 8. Deligne–Lusztig 理论 (1976) — 有限群的表示论
- **1976** · 与 George Lusztig 合作——用 étale 上同调构造有限李型群的不可约表示。
- **核心思想**：将 Chevalley 群的表示论问题转化为 ℓ-adic 上同调的几何问题。这是表示论数学化的经典范例。
- **影响**：Deligne–Lusztig 理论彻底改变了有限群表示论。Lusztig 在此基础上建立了"Lusztig 猜想"——有限李型群特征标理论的完整框架。
- 底部金句："他不仅证明了几何猜想——他还用几何解决了表示论的问题。这就是 Grothendieck 遗产的力量。"

### 9. Fields 奖 (1978) — 33 岁的加冕
- **1978 · Helsinki ICM**。Fields 奖授予 Pierre Deligne——此时他才 33 岁。
- **获奖理由**：证明 Weil 猜想。大会报告中，他给出了一个更优雅的证明版本——比 1974 年的证明更简洁。
- **谦逊**：当记者问他感受时，他说："我只是在合适的时间出现在合适的地方。Grothendieck 建造了这艘船，我只是把它开进了港口。"
- 底部金句："'Grothendieck 建造了这艘船，我只是把它开进了港口。'——这是数学史上最谦逊的 Fields 奖感言之一。"

### 10. IHÉS 到 IAS (1970–1984)
- **1970–1984** · IHÉS 永久成员。与 Serre, Grothendieck, Thom, Borel 为邻——这是代数几何的黄金时代。
- **1976** · 与 Deligne–Lusztig 理论。**1980** · Weil II。1970s 也是混合 Hodge 结构和绝对 Hodge 循环的集中发展期。
- **1984** · 转入 IAS Princeton。他在法国的 19 年 (1965–1984) 是代数几何史上最辉煌的时代之一。
- 底部金句："在 IHÉS 的 19 年——他从比利时少年变成了改变数学史的人。"

### 11. Perverse Sheaves 与 Riemann–Hilbert (1980s)
- **Perverse sheaves (反常层)**：与 Beilinson, Bernstein, Gabber 合作——创造了代数几何中最重要的工具之一。反常层是 D-模理论、Langlands 纲领和奇点理论的基础。
- **Riemann–Hilbert 对应**：将 Hilbert 第 21 问题的精神推广到高维。反常层是 Riemann–Hilbert 对应中 D-模的"搭档"。
- **Ngô Bảo Châu** 在证明 Fundamental Lemma 时深度使用反常层——Deligne 的工具帮助 2010 年的 Fields 奖得主。
- 底部金句："反常层——一个听起来奇怪的名字，却是代数几何中最强大的工具之一。它帮助 Ngô 证明了 Fundamental Lemma。"

### 12. Tannakian 范畴与 Motives (1990–)
- **1990 · Grothendieck Festschrift**：Deligne 重写了 Tannakian 范畴理论——用范畴语言表达 motives 理论的线性结构。
- **Tannakian 范畴**：一个带有纤维函子的张量范畴等价于某个群概形的表示范畴。这为 motives 的终极理论提供了语言——motives 应该形成某个"motivic Galois 群"的 Tannakian 范畴。
- **绝对 Hodge 循环**：在 Hodge 猜想未被证明的情况下，Deligne 发明了"绝对 Hodge 循环"作为 motive 的替代品。这是一个实用的迂回策略。
- 底部金句："Motives 是数学的终极梦想——Deligne 为这个未完成的梦想提供了最清晰的语言。"

### 13. 五奖大满贯：Fields + Wolf + Abel + Crafoord + Balzan
- **Fields 奖 (1978)** · **Crafoord 奖 (1988)** · **Balzan 奖 (2004)** · **Wolf 奖 (2008)** · **Abel 奖 (2013)**
- **子爵 (2006)**：比利时国王阿尔贝二世封 Pierre Deligne 为子爵——表彰他为比利时带来的国际声誉。
- **Abel 奖 (2013)**：挪威国王颁发。"表彰他在代数几何方面的开创性贡献及其对数论、表示论及相关领域的变革性影响。"
- **三冠+二冠**：历史上同时获得 Fields + Wolf + Abel 的数学家屈指可数。Deligne 是其中之一。
- 底部金句："Fields、Wolf、Abel——三大数学奖的大满贯。再加上 Crafoord 和 Balzan——五项大奖，无人能及。"

### 14. 遗产：那些以 Deligne 命名的概念
- **Deligne–Mumford 叠 (stacks)** — 模空间理论
- **Deligne–Lusztig 理论** — 有限李型群的表示论
- **Deligne 上同调** — 混合 Hodge 结构的实现
- **Deligne 猜想 (辫群)** — 辫群的同调
- **权的瑜伽 (yoga of weights)** — Deligne 的数学哲学
- **绝对 Hodge 循环** — motive 的替代品
- **Perverse sheaves (反常层)** — 代数几何的核心工具
- **Riemann–Hilbert 对应** — Hilbert 第 21 问题的高维推广
- **Tannakian 范畴** — Motives 理论的语言
- 底部金句："以他命名的概念超过十个——从叠到反常层，从权到 motive——他的名字是现代代数几何的语言本身。"

### 15. 结束页 — Grothendieck 的火炬手
- 大引语："La mathématique est plus grande que nous."（数学比我们所有人都大。）
- 小字：皮埃尔·德利涅 · Pierre Deligne · 1944 —
- 底部：Weil 猜想的征服者 · Fields 1978 · Wolf 2008 · Abel 2013 · 比利时子爵 · IAS Princeton

## 背景音乐选择 ✅

- **选定曲目**: **Timeless** — Alex-Productions (132k views, 最高受众)
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - "长期纲领" 完美匹配 Deligne 的贡献本质 —— Weil I (1974) 仅 35 页就改变了数学史；Weil II (1980) 六年后再建立一般框架。权的瑜伽 (yoga of weights) 统一了 Hodge 理论与 Galois 表示。Tannakian 范畴 (1990) 为 motives 终极理论提供了语言 —— Deligne 的每一件工作都不是瞬间的突破，而是持久的结构性建设
  - "沉稳" 匹配 Deligne 的极简人格 —— "从来不说话，但一开口就是对的。" 他的论文以极短著称，没有一句多余。Grothendieck 宏大壮阔、滔滔不绝；Deligne 极简深邃、惜字如金。Timeless 的克制深度与这种数学风格天然吻合
  - "纪录片" 匹配跨越 35 年的加冕弧 —— Fields 奖 (1978, 33 岁) → Wolf 奖 (2008) → Abel 奖 (2013)。同样的贡献（Weil 猜想），先后三次获得最高荣誉，是对"Timeless"最完美的证明。加上 Crafoord 和 Balzan —— 五项大奖无人能及
  - "La mathématique est plus grande que nous." —— 这是 Deligne 的结束页引语。当 Grothendieck 号召抵制学术界时，Deligne 公开拒绝："数学比我们所有人都大。" 这种超越个人的谦逊和冷静，正是 Timeless 的沉稳内核 —— 不是欢庆，不是征服，而是"数学本身就是永恒的"
  - Grothendieck 的火炬手 —— 师傅建造了étale上同调的宏大框架，徒弟用 35 页完成了师傅未能完成的工作。火炬传递本身就是 "Timeless" 的意象
- **备选** (未采用):
  - ★★ Expedition — "探索/史诗" 完全不匹配。Deligne 不是远征者，他是在已有的框架（Grothendieck 的概形论和 étale 上同调）中完成最后的精确一击。他是外科手术式精准的问题解决者，而非开拓新大陆的探索者。Expedition 属于 Morse（登山家+一战勋章）和 Whitney（骨灰撒阿尔卑斯山顶）
  - ★ Awaken — "鼓舞/明亮" 匹配 Fields 奖的年轻加冕 (33 岁)，但无法承载 Deligne 的整体气质。他是沉默的思考者，不是明亮的鼓舞者
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/Pierre_Deligne-FWA/Timeless.wav`
- **时长**: 128 秒 > 17 页 × 7 秒 = 119 秒 → ffmpeg `-shortest` 自动对齐

## Round 2 高危: 博士导师 Grothendieck (Paris-Sud 1972, 非 Thom/1968)、Weil 猜想第四个归属、Weil I 1974 发表、爵位 2006、在世不用过去时。

> **开始执行。**
