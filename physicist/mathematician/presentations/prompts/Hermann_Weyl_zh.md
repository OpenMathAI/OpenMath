# 赫尔曼·外尔 (Hermann Weyl) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Kolmogorov、冯·诺依曼、Noether 等成品为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Hermann Weyl (1885–1955)
- **气质关键词**: **超级连接者、几何-物理双栖者、Hilbert 的传人、IAS 的良心、深度与广度并重的哲人数学家**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本：
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Hermann_Weyl/`
- **参考模板**: `grothendieck/`, `riemann/`, `hilbert/`, `serre/`, `noether/`, `neumann/`, `kolmogorov/` 七个完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Hermann_Weyl/`

输出以下信息供校验：

- **生卒日期**：1885-11-09 ~ 1955-12-08，享年 70 岁
- **国籍**：德国 → 美国（1930 年代纳粹上台后移居）
- **出生地**：Elmshorn（埃尔姆斯霍恩），德国 Schleswig-Holstein 地区
- **博士导师**：David Hilbert（哥廷根大学，1908 年获博士学位）
- **博士论文**：1908，《Singuläre Integralgleichungen mit besonderer Berücksichtigung des Fourierschen Integraltheorems》（奇异积分方程——重点关注傅里叶积分定理）
- **主要任职机构**：
  - 1908–1913: 哥廷根大学（Privatdozent）
  - 1913–1930: ETH Zürich（苏黎世联邦理工学院）—— 与 Einstein 同事
  - 1930–1933: 哥廷根大学 —— Hilbert 退休后的继任者
  - 1933–1951: 普林斯顿高等研究院（IAS）—— 纳粹上台后移居美国
  - 1951–1955: 退休后往返于普林斯顿和苏黎世
- **关键荣誉**：
  - 1923: 当选 Göttingen Academy of Sciences 院士
  - 1927: Lobachevsky Prize（罗巴切夫斯基奖）
  - 1931: 英国皇家学会外籍院士
  - 1941: 美国国家科学院院士
  - 1955: 获颁德国功勋勋章 Pour le Mérite（和平级）
- **重要合作者/同事/学生**：
  - 导师与合作者: Hilbert（终身关系）、Einstein（ETH 和 IAS 两度同事）
  - IAS 同事: Einstein, Gödel, von Neumann, Veblen
  - 哥廷根同事: Noether, Courant, Landau
  - 学生: Saunders Mac Lane（范畴论创始人之一）
  - 对立面: Brouwer（直觉主义 vs 形式主义的论战对手）

### 关键时间线（15–20 个节点）：
- 1885: 生于德国 Elmshorn，父亲是银行主管
- 1904–1908: 先后在慕尼黑大学和哥廷根大学学习数学与物理，师从 Hilbert
- 1908: 获博士学位，同年 Hilbert 帮他谋得哥廷根教职
- 1913: 受聘 ETH Zürich 正教授 —— 年仅 27 岁
- 1913–1930: 在苏黎世的黄金岁月，与 Einstein 成为亲密同事
- 1918: 出版广义相对论教材 *Raum, Zeit, Materie*（《空间、时间、物质》），4 年再版 4 次；同年出版数学基础著作 *Das Kontinuum*（《连续统》）；首次提出规范不变性的原始构想
- 1920–1921: 一度被 Brouwer 的直觉主义说服，发表《论数学的新基础危机》
- 1927: 初版《数学与自然科学哲学》
- 1928: 出版《群论与量子力学》—— 李群表示论在量子物理中的系统应用
- 1930: 回哥廷根大学接替 Hilbert 的教席
- 1933: 纳粹通过《恢复职业公务员法》—— Weyl 妻子是犹太人，全家被迫移居美国，加入 IAS
- 1939: 出版《经典群》（The Classical Groups）
- 1951–1952: 在普林斯顿发表对称系列讲座，次年出版《对称》（Symmetry）
- 1955: 12 月 8 日在苏黎世逝世，享年 70 岁

### 人格特质线索：
- "他从来不只是数学家或物理学家，他总是两者兼备。" —— Einstein 对 Weyl 的评价
- Hilbert 最钟爱的学生之一，被称为"Hilbert 的大脑继承人"
- 与 Brouwer 的论战中展现出深刻的哲学思考——他能理解直觉主义的价值，但无法放弃经典数学
- 在 IAS 期间，他是少数积极帮助欧洲战乱中流亡数学家的学者
- Weyl 在 Noether 失业时（1933 年纳粹驱逐犹太学者）积极斡旋，促成 IAS 的聘任
- 深沉而有诗意——他的著作中不仅有严密的数学推导，还有大量关于"数学之美""对称之妙"的哲学思考
- Freeman Dyson 曾说："他写书的方式像诗人写诗。"
- Weyl 本人曾说过："我的工作始终试图追随真理，不论它引向何方。"

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 黎曼面理论 | 《Die Idee der Riemannschen Fläche》（黎曼面的理念）—— 经典教科书 | 1913 |
| 谱理论 | Weyl 渐近律 —— 紧区域上 Laplace 算子的特征值分布 | 1911–1913 |
| 均匀分布 | Weyl 一致分布定理、Weyl 判据 —— 数论的基石性结果 | 1916 |
| 规范理论 | 规范不变性的原始概念 —— 现代粒子物理的数学基石 | 1918 |
| 广义相对论 | Weyl 张量（Weyl curvature tensor）；*Raum, Zeit, Materie* —— 广义相对论经典教材 | 1918–1921 |
| 数学基础 | *Das Kontinuum* (1918)；站在 Hilbert（形式主义）与 Brouwer（直觉主义）之间的调和者 | 1918–1930s |
| 李群表示论 | Weyl 特征标公式、Peter–Weyl 定理 —— 连通李群的完备表示理论 | 1925–1927 |
| 经典群 | 《The Classical Groups》 —— 不变量理论的现代重建 | 1939 |
| 数学哲学 | 《数学与自然科学哲学》（1927 初版 / 1949 修订版）—— 影响深远的哲学著作 | 1927/1949 |
| 对称 | 《对称》（Symmetry）—— 从艺术到粒子物理，最广为人知的科普经典 | 1952 |

### ★ 外尔独有的叙事线索

1. **规范理论的"美丽的失败"** — 1918 年，Weyl 试图用规范不变性统一引力和电磁学。这个物理尝试被 Einstein 指出是错误的（不满足长度不变性），但其中的数学思想——规范变换——在量子力学时代（1929）被修改为相位变换后，成为现代粒子物理标准模型的核心数学语言。这是一个"物理上失败、数学上不朽"的故事。
2. **Hilbert 的继任者** — Weyl 是 Hilbert 指定接替其在哥廷根大学教席的人选。这本身就是最高的学术认可。但 3 年后纳粹上台，他被迫离开。
3. **两个世界之间的桥梁** — Weyl 在德国数学（哥廷根传统）和美国数学（IAS 传统）之间、在纯数学和理论物理之间、在 Hilbert 形式主义和 Brouwer 直觉主义之间，始终充当连接者。
4. **Noether 的伯乐** — 1933 年，Weyl 亲自为 Noether 在 IAS 争取教职。他在 Noether 的悼词中写下了数学史上最感人的一段话。
5. **哲学家的深度** — 与 von Neumann 的"实用主义通才"不同，Weyl 的广度源于深刻的哲学思考。他相信数学和物理最终是关于"人如何理解自然"的。
6. **对称之美** — Weyl 1952 年的《对称》讲座是数学科普的经典。其中著名的开场白："对称，无论是广义还是狭义，是一种人类自古以来就试图通过它来理解和创造秩序、美和完美的观念。"
7. **"最后的古典数学家"？** — 有人认为 Weyl 是最后一位能同时掌握纯数学和理论物理所有前沿的人。在他之后，数学和物理的分化已经不可逆转。

### 人物关系

- **David Hilbert（导师）** — 哥廷根的导师，Weyl 是他最信赖的学生和继任者
- **Albert Einstein（同事）** — ETH 时期和 IAS 时期的两度同事；曾指出 Weyl 规范理论的物理缺陷，但尊重其数学深度
- **Emmy Noether** — 哥廷根时期和 IAS 时期的同事，Weyl 是她最重要的支持者之一
- **L.E.J. Brouwer** — 直觉主义的论战对手，Weyl 一度被 Brouwer 说服，后又回归形式主义
- **John von Neumann** — IAS 同事，两人在量子力学数学基础上有重叠兴趣
- **Kurt Gödel** — IAS 同事，在数学基础上有深层对话
- **Oswald Veblen** — IAS 的同事和共同筹建者
- **Saunders Mac Lane** — 学生，后来成为范畴论的创始人之一
- **Freeman Dyson** — 深受 Weyl 著作影响的青年物理学家

---

## 第 5 步：设计配色方案

- **建议配色：深琥珀金 + 星夜紫 + 象牙白** —— 对称与秩序的庄严感 + 黎曼面/广义相对论的宇宙深邃 + 哲学沉思的温暖
- 需要与已有配色完全不同！
  - Hilbert：普鲁士蓝 + 金
  - Grothendieck：深靛 + 金
  - Serre：勃艮第红 + 象牙暖金
  - Noether：深紫罗兰 + 暗玫瑰金
  - Riemann：墨绿 + 银灰
  - Kolmogorov：深松绿 + 古铜金
  - von Neumann：深黑 + 电路绿
- 四个分类色，对应 Weyl 的四大支柱：
  - **badgegroup** (李群/表示论) — 琥珀金 `#C9A227`
  - **badgegauge** (规范理论/广义相对论/物理) — 星夜紫 `#3D2B6B`
  - **badgegeometry** (黎曼面/谱理论/均匀分布) — 深海蓝 `#1B4D6B`
  - **badgephilosophy** (数学基础/哲学) — 砂岩暖 `#A08C6B`

---

## 第 6 步：规划幻灯片序列（建议 18 页）

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《赫尔曼·外尔：几何与物理之间的超级连接者》 / Hermann Weyl 1885–1955
02  为什么 Weyl 是"连接者" — 群论↔物理↔几何↔哲学，四维交织的一生

=== 早年 ===
03  哥廷根的学生 (1904–1913) — Hilbert 最钟爱的弟子，27 岁成为正教授
04  黎曼面的理念 (1913) — 《Die Idee der Riemannschen Fläche》，几何直觉的巅峰

=== 规范理论与物理 ===
05  规范理论的诞生 (1918) — 一个"美丽的数学失败"，后来成为粒子物理的基石
06  群论与量子力学 (1928) — 李群表示论如何改变物理学家对对称性的理解

=== 数学基础 ===
07  Hilbert 与 Brouwer 之间 — 形式主义 vs 直觉主义，一个人如何站在两座高峰之间

=== 哥廷根→普林斯顿 ===
08  继承 Hilbert 衣钵 (1930–1933) — 回到哥廷根，3 年后被迫离开
09  为 Noether 而战 (1933) — 纳粹之下，为犹太同事争取 IAS 职位
10  IAS 岁月 (1933–1951) — 普林斯顿的新家园，美国数学的黄金时代

=== 主要成就 ===
11  经典群与不变量理论 (1939) — 《The Classical Groups》—— 一座数学丰碑
12  谱理论与均匀分布 — Weyl 渐近律 · Weyl 一致分布定理

=== 哲人数学家 ===
13  对称之美 (1952) — 从雪花到基本粒子，一门关于秩序的普遍科学
14  数学与自然科学哲学 (1927/1949) — 一位数学家如何看待自然世界

=== 遗产 ===
15  外尔的遗产 — 规范理论 · 李群 · 黎曼面 · 对称 —— 他的思想贯穿现代数学物理
16  思想回响 — 他用对称和规范的思想，提前 50 年预言了基本粒子的数学结构

=== 结尾 ===
17  结束页 — 主题句：他从来不只是数学家或物理学家，他总是两者兼备。
```

---

## 第 9 步：史实审查

### 外尔特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **"规范理论"的物理史实** | Weyl 1918 年的原始规范理论是"失败的"——Einstein 指出它违背了长度不变性。1929 年量子力学出现后，规范变换被重新解释为相位变换（Weyl 本人参与了这一修正）。不要写"他发明了现代规范理论"，而写"他种下了规范不变性的种子。" |
| **Hilbert 的"继任者"** | Weyl 确实受邀接替 Hilbert 在哥廷根的教席。但他在 1930 年接受后仅 3 年就因纳粹而上偏离。不要暗示他是 Hilbert"唯一的"或"理所当然的"继任者。Courant 等人也有资格。 |
| **与 Brouwer 的关系** | Weyl 一度被 Brouwer 的直觉主义说服（1920–1921），写了《论数学的新基础危机》表示支持。但后来他与 Brouwer 决裂并回归形式主义。不应用"背叛""背叛"等道德化词汇。这是一场学术立场转变。 |
| **Noether 的 IAS 聘任** | Weyl 和 Einstein 共同为 Noether 在 IAS 争取职位。但职位只是"访问学者"级别的（因为她是女性），不是终身教授。1935 年 Noether 在 Bryn Mawr 去世，Weyl 前往亲致悼词。不要夸大职位性质。 |
| **规范变换的命名** | "gauge"（规范）这个英文词来自 Weyl 的原始德文术语 Eichinvarianz（刻度不变性）。他最初的想法是：在时空每一点独立选择测量标尺。这被 Einstein 否定后，1929 年被量子力学重新解释。 |
| **Weyl 张量** | 在广义相对论中，Weyl 张量是 Riemann 曲率张量的零迹部分，描述真空引力场中的潮汐力。不要混淆 Weyl 张量（物理/几何）和 Weyl 规范场（物理/量子）。 |
| **Peter–Weyl 定理** | 这个定理是与 Fritz Peter 合作在 1927 年发表的。不要只说"Weyl 定理"，应说"Peter–Weyl 定理"。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| gauge invariance | 规范不变性 | 也译"刻度不变性"（德文原始含义），但在现代物理中"规范"已成标准 |
| Weyl tensor | Weyl 张量 | 广义相对论中的曲率张量，不要与"Weyl 旋量"混淆 |
| Peter–Weyl theorem | Peter–Weyl 定理 | Fritz Peter 是合作者，不要遗漏 |
| Weyl equidistribution theorem | Weyl 一致分布定理 | 也译"均匀分布定理" |
| Weyl character formula | Weyl 特征标公式 | 李群表示论的核心工具 |
| The Classical Groups | 《经典群》 | 不要翻译成"古典群" |
| Raum, Zeit, Materie | 《空间、时间、物质》 | Weyl 1918 年的广义相对论教材 |
| Eichinvarianz | 刻度不变性 → 规范不变性 | 德文原词，"Eich" = 刻度/校准 |
| symmetry | 对称 | Weyl 最著名的科普主题 |
| Riemann surface | 黎曼面 | Weyl 1913 年著作的核心概念 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一次/第一个"断言** | "第一个提出规范不变性" — 改为"最早系统研究规范不变性的数学家之一" |
| **学科归属** | Weyl 同时是数学家和物理学家。不要只说"数学家 Weyl"或"物理学家 Weyl"，用"数学家和理论物理学家" |
| **"最后的古典数学家"** | 这个称号也用于 Poincaré 和 Weyl。避免排他性。用"20 世纪最具广度的人物之一" |
| **纳粹叙事** | 聚焦 Weyl 离开的个人原因（妻子是犹太人），不过度渲染政治。他的选择是数学家的尊严 |
| **伪引语** | Weyl 的名言"我的工作始终试图追随真理，不论它引向何方"需要确认来源。不确定就用间接转述 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

> **核心原则：Beamer 写完后，必须回到本地 Wikipedia 存档（page.md + metadata.json），逐项对照审核。**
> 这一步不是"再读一遍"，而是系统性地、逐页逐字地交叉验证。
> 
> 只有写完全部页面后，才能以"第三方审阅者"的视角来审视细节是否与 Wikipedia 一致。

### 终审执行流程

```
1. 打开 pages/Hermann_Weyl/page.md，从头到尾逐段阅读全文
2. 同时打开 Hermann_Weyl_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### 10 项终审清单

| # | 检查项 | 方法 | 高危信号 |
|:--:|------|------|---------|
| 1 | **事实性错误** | Beamer 中每个日期/人名/机构，与 page.md 逐条对照 | 任何与 Wikipedia 不一致的年份、地名、人名 |
| 2 | **翻译/术语错误** | 将所有数学术语与 Wikipedia 英文原词对照 | 概念性误译（如 gauge→规范而非刻度，在适当上下文需要标注原始含义） |
| 3 | **重大遗漏** | 扫描 Wikipedia 目录，列出 page.md 覆盖的主要成就；对比 Beamer 是否都涉及 | 标志性专著/定理在 Beamer 中只字未提（如 *Raum, Zeit, Materie*） |
| 4 | **结构性错误** | 检查时间线是否按生平顺序，同一时期的成就是否被拆散 | 时间跳跃混乱、因果倒置 |
| 5 | **编译告警** | 分析 `Overfull \hbox` 和 `Overfull \vbox` | vbox > 10pt 或 hbox > 50pt 需修复 |
| 6 | **引语来源** | 每个加引号的句子，必须在 page.md 或可靠来源中找到对应原文 | **中文引号内的句子无法在 Wikipedia 中找到** |
| 7 | **年份精确性** | 尤其注意 slide 标题中的年份——观众会当作"正式发表年份" | 写作年份 ≠ 发表年份，初版年份 ≠ 修订版年份 |
| 8 | **人物关系** | metadata.json 的 `doctoral_advisor` / `doctoral_student` / `employer` 与 Beamer 一致 | 把"合作者"写成"学生"，把"访问学者"写成"教授" |
| 9 | **荣誉/获奖** | metadata.json 的 `award_received` 与封面页一致 | 遗漏重大奖项，或奖项年份标错 |
| 10 | **出版年份** | Wikipedia 书目栏中的出版年份与 Beamer 中标注的一致 | 初版与再版混淆（如《经典群》1939 而非 1938） |

### 优先级定义

| 优先级 | 定义 | Weyl 实际案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** — 专业读者一眼看出 | 《经典群》标 1938，Wikipedia 为 [1939]；缺慕尼黑大学教育经历 |
| 🟡 P1 | **来源存疑/模糊** — 经不起推敲 | 引语"德国离开了我"无 Wikipedia 来源；数学哲学书只标 1949 而非 1927/1949 |
| 🟢 P2 | **重要遗漏** — 缺了不会错，补了更好 | *Raum, Zeit, Materie* (1918)；*Das Kontinuum* (1918) |
| ⚪ P3 | **可选补充** — 锦上添花 | Weyl 半金属 (2015 实验发现)；Husserl 现象学影响 |

### 输出格式

终审完成后，输出结构化 Review 报告：

```markdown
## 🔍 Hermann Weyl Beamer — Wikipedia 本地文档终审

### 🔴 事实性错误 (需修复)
| # | 位置 | 当前内容 | 问题 | 修正 |

### 🟡 来源存疑/术语审查
| # | 位置 | 当前内容 | 问题 | 修正 |

### 🟢 重要遗漏
| # | 遗漏内容 | Wikipedia 记载 | 建议 |

### 🟠 结构性/叙事性问题
| # | 位置 | 问题 | 建议 |

### 📊 逐页对照
| # | 标题 | 事实准确性 | 遗漏 | 评价 |

### 📋 修复优先级汇总
| 优先级 | 数量 | 类型 |
```

### ⚠️ Weyl 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **《经典群》年份** | 初版 1939，非 1938。Wikipedia 书目明确标注 [1939] | 打开 page.md 搜索 "Classical Groups"，核对年份 |
| **慕尼黑大学** | Weyl 在慕尼黑大学也学过，不只是哥廷根 | page.md 搜索 "Munich" 或 "München" |
| **"德国离开了我"** | 这是 Thomas Mann 的名言，非 Weyl | 在 page.md 中搜索 "Germany left me" 或 "Deutschland" |
| **哲学书初版年份** | 1927 初版，1949 是修订版 | page.md 搜索 "Philosophy of Mathematics" |
| **《对称》出版年份** | 讲座 1951，出版 1952，非 1946 | page.md 搜索 "Symmetry" |
| **规范理论的叙述** | 1918 原始想法"物理上失败" / 1929 量子重解释 —— 两个不同节点 | page.md 逐段阅读 "Geometry and theoretical physics" 章节 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Weyl 的独特性在于"连接"——不是 von Neumann 的广度，不是 Kolmogorov 的深度，而是**架桥**的能力
> 2. 规范理论的叙事是核心亮点："一个物理上失败的idea，50 年后成为粒子物理的数学基石"
> 3. Weyl 的哲学写作（《对称》、《数学与自然科学哲学》）是区分于其他数学家的独特标签
> 4. 与 Noether 的关系 —— 在纳粹时代保护同事、为死者亲致悼词 —— 是展现人格温暖的关键节点
> 5. 他是少数能与 Einstein 在物理上平等对话、同时与 Hilbert 在数学上平等对话的人
> 6. 结尾主题句："他从来不只是数学家或物理学家，他总是两者兼备。"（Einstein 原话）

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

外尔的气质：**超级连接者、几何-物理双栖、Hilbert 的传人、哲人数学家** — 庄严深沉，对称与秩序的美感。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 沉稳纪录片风，Weyl 在数学与物理之间的永恒连接 |
| ★★★ | Symphony No. 7 | beethoven-karajan | `music_audio/beethoven-karajan/07-W5NsPOgyALI-Beethoven "Symphony No 7" Karajan.wav` | 律动庄严，对称之美 |
| ★★ | Eternals | alex-productions | `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` | 宏大深远，规范理论50年的回响 |
| ★ | Expedition | alex-productions | `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` | 探索史诗，从黎曼面到规范场的跨越 |

**操作**：复制选定的 `.wav` 到 `Hermann_Weyl/` 目录，`make video` 自动混入。
