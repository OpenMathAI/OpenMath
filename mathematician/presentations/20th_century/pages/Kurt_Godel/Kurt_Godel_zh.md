# 哥德尔 (Kurt Gödel) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 **Weil、Turing** 等最新成品为参考模板（含 §二十 社会关系入库 + §二十一 数据库字段核对）。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Kurt Gödel (1906–1978)
- **气质关键词**: **逻辑学巨人、数学基础的边界发现者、柏拉图主义者、隐居者、与爱因斯坦散步的人**
- **Wikipedia 页面**: ✅ **已下载**（`pages/Kurt_Godel/` 完整，含 page.md + metadata.json + images.txt）
- **参考模板**: `turing/`, `weil/`, `neumann/`, `hilbert/`, `grothendieck/`, `riemann/` 等完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`
- **数据库**: `greatminds`（MySQL），Gödel id=10 已在库

---

## 第 0 步：核对元数据（metadata.json）

对照 `pages/Kurt_Godel/metadata.json` 核对以下字段，**确保 tex 与数据库一致**：

- **qid**：Q41390（数据库中已填）
- **生卒**：1906-04-28 ~ 1978-01-14，享年 71 岁
- **国籍**：奥匈帝国（Cisleithania）→ 捷克斯洛伐克（出生地今属）→ 奥地利 → 美国（1948 年入籍）
- **出生地**：Brünn (Brno)，奥匈帝国（今捷克）
- **死亡地**：Princeton, New Jersey, USA（因拒绝进食导致的营养不良）
- **博士导师**：Hans Hahn（维也纳大学，1929 年获博士学位）
- **博士论文**：1929，《Über die Vollständigkeit des Logikkalküls》（论逻辑演算的完备性）— Gödel 完备性定理
- **主要任职机构**：
  - 1930–1938: 维也纳大学（Privatdozent）
  - 1938–1939: 圣母大学（University of Notre Dame）
  - 1940–1976: 普林斯顿高等研究院（IAS）常任成员（1946 年成为教授）
- **关键荣誉**：
  - 1951: 首届 Albert Einstein 奖（与 Julian Schwinger 共同获得）
  - 1951: 耶鲁大学 Gibbs Lecture（"Some Basic Theorems on the Foundations of Mathematics and Their Philosophical Implications"）
  - 1968: 当选英国皇家学会外籍会员 (ForMemRS)（page.md 为准）
  - 1974: 国家科学奖章（National Medal of Science，福特总统颁发，因健康原因未出席）
  - 1975: 拒绝奥地利科学院荣誉院士（后来改变主意接受了）
- **重要合作者/同事/学生**：
  - 维也纳圈子: Moritz Schlick, Hans Hahn, Rudolf Carnap, Karl Menger
  - 普林斯顿 IAS: Albert Einstein（最亲密的晚年朋友）, John von Neumann, Hermann Weyl, Oskar Morgenstern
  - 受其思想影响者: Alan Turing, Alonzo Church, Paul Cohen, Georg Kreisel, Gregory Chaitin
  - 妻子: Adele Nimbursky Porkert (Gödel) — 舞厅舞女出身，Gödel 家庭的反对但 Gödel 执意迎娶

---

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。**「现状」列已标注库中是否已有；缺失项按 §21.5 写 `MySQL/seed_godel_full.py` 补齐（`INSERT IGNORE` 幂等）。**

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q41390` | ✅ 已填 |
| 2 | `people` | name_en | `Kurt Gödel` | ✅ |
| 3 | `people` | name_zh | `库尔特·哥德尔` | ✅ |
| 4 | `people` | name_variants | `["数学基础的边界","逻辑学巨人","柏拉图主义者"]` | ✅（可补充） |
| 5 | `people` | gender | `male` | ✅ |
| 6 | `people` | birth_date | `1906-04-28` | ✅ |
| 7 | `people` | death_date | `1978-01-14` | ✅ |
| 8 | `people` | description | `Austrian-American logician, mathematician, and philosopher of mathematics (1906–1978)` | ✅ |
| 9 | `people` | primary_occupation | `mathematician` | ✅ |
| 10 | `person_occupation` | 职业（rank 排序） | `mathematician(0)`、`university teacher(1)`、`computer scientist(2)`、`physicist(3)` | ⚠️ 需补（现仅 mathematician） |
| 11 | `person_field` | 领域（rank 排序） | `mathematical logic`、`set theory`、`philosophy of mathematics`、`logic`、`mathematics`、`physics`、`theory of relativity` 等 10 项 | ✅ 10 项已有 |
| 12 | `award_laureate` | 获奖（year/note） | `Albert Einstein Award 1951`、`Josiah Willard Gibbs Lectureship 1951`、`Foreign Member of the Royal Society 1968`、`National Medal of Science 1974` | ⚠️ 全空（Albert Einstein Award 需补字典） |
| 13 | `person_institution` | 教育/任职 | `education: University of Vienna(1924–1930)`；`employment: University of Vienna(1930–1938)、University of Notre Dame(1938–1939)、Institute for Advanced Study(1940–1976)` | ⚠️ 全空（Vienna/Notre Dame 需补字典） |
| 14 | `person_nationality` | 国籍 | `United States`、`Austria`、`Cisleithania`、`Czechoslovakia` | ✅ 4 项已有 |
| 15 | `person_relation` | 社会关系 | 见第 4.5 步（11 条） | ⚠️ 已有 3 条（von Neumann/Weyl/Weil 的 IAS 同事） |
| 16 | `rankings` | 榜单（list_key/rank/status） | `OpenMath_20th_Century_Top50` 名次待查 | ⚠️ 待确认 |

核对完成后：写 `MySQL/seed_godel_full.py`，入库后按 §21.4 一键校验并汇报：「新建/更新 X 人、职业 Y 条、领域 Z 条、奖项 A 条、机构 B 条、国籍 C 条、社会关系 D 条」。

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 数理逻辑 | Gödel 完备性定理 — 一阶逻辑的语义完备性 | 1929 |
| 数学基础 | Gödel 不完备性定理 — 任何足够强的形式系统无法证明自身一致性 | 1931 |
| 集合论 | 可构成集合 L — 选择公理与连续统假设的相对一致性 | 1938 |
| 递归论 | 原始递归函数 — 可计算性理论的先驱 | 1931 |
| 广义相对论 | Gödel 度量 — 旋转宇宙解，包含闭合时间曲线 | 1949 |
| 哲学 | 数学柏拉图主义 — 为数学实在论提供了最深层的论证 | 1940s–1970s |

### ★ 哥德尔独有的叙事线索

1. **不完备性定理不是否定，而是揭示** — Gödel 证明的不是"数学不可靠"，而是"任何足以表达算术的形式系统，其真理性永远超越其可证性"。这不是虚无主义的结论，而是对数学本性的一种深刻的**发现**。
2. **从完备性到不完备性** — Gödel 的学术生涯以"完备性定理"（一阶逻辑是完备的）开始，紧接着以"不完备性定理"（任何包含算术的系统是不完备的）震惊世界。这两者不是矛盾——完备性适用于一阶逻辑本身，不完备性适用于能表达算术的系统。
3. **Hitler、IAS、Einstein** — Gödel 是纳粹迫害下流亡普林斯顿的犹太知识分子之一。在 IAS，他与 Einstein 建立了最亲密的友谊——两个欧洲流亡者，两个寻找宇宙最深层结构的人。
4. **可构成宇宙 L** — 1938 年，Gödel 将集合论的世界"最小化"到可构成集合 L，证明了如果 ZF 是一致的，那么 ZF + AC + GCH 也是一致的。这是集合论中最重要的相对一致性证明。
5. **连续统假设的独立性** — Gödel 证明 CH 不能被反驳（1938），Cohen 证明 CH 不能被证明（1963）。这两人的工作共同构成了 20 世纪数学基础研究的最完整画卷。
6. **Gödel 宇宙** — 1949 年，献给 Einstein 70 岁生日的礼物：一个旋转的宇宙模型，在其中存在**闭合时间曲线**——理论上你可以回到过去。这是广义相对论中最有趣的精确解之一。
7. **宪法漏洞** — 1948 年入籍听证会上，Gödel 滔滔不绝地向法官解释他发现美国宪法存在逻辑漏洞——Einstein 和 Morgenstern 在旁拼命转移话题。
8. **饥饿而死** — 不是因为贫困，而是因为偏执。妻子 Adele 是唯一他信任能为他准备食物的人。当她生病住院时，Gödel 停止进食。这是逻辑天才的另一面：对现实世界的极端不信任。

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。Gödel 已有 3 条关系（von Neumann/Weyl/Weil 的 IAS 同事，由他们立传时建）；本节补足其余关系。
> 数据库全部字段核对见 §21.5（第 0.5 步）。

**入库范围（11 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师（advisor-student） | Hans Hahn → Gödel | 有向 | ⚠️ 占位 |
| 同事（colleague） | Albert Einstein | 无向 | ✅ 已在库（id=349） |
| 同事（colleague） | John von Neumann | 无向 | ✅ 已有关（id=3） |
| 同事（colleague） | Oskar Morgenstern | 无向 | ✅ 已在库（id=353） |
| 同事（colleague） | Hermann Weyl | 无向 | ✅ 已有关（id=6） |
| 对话者（colleague） | Moritz Schlick | 无向 | ⚠️ 占位（维也纳学派领袖） |
| 同事（colleague） | Rudolf Carnap | 无向 | ⚠️ 占位（维也纳学派） |
| 同事（colleague） | Karl Menger | 无向 | ⚠️ 占位（维也纳大学同事） |
| 思想传承（collaborator） | Alan Turing | 无向 | ✅ 已在库（id=9） |
| 对话者（collaborator） | Alonzo Church | 无向 | ✅ 已在库（id=381） |
| 完成者（collaborator） | Paul Cohen | 无向 | ✅ 已在库（id=113） |
| 夫妻（spouse） | Adele Gödel | 无向 | ⚠️ 占位 |

- 缺失人物（Hahn/Schlick/Carnap/Menger/Adele Gödel 共 5 人）先建占位：`INSERT INTO people (name_en, primary_occupation, has_biography) VALUES (..., 'mathematician', 0)`
- 关系 `note` 加 `[材料待展开]` 前缀打标识；配偶 Adele 的 `primary_occupation` 用 `artist`（舞女/歌手）或默认，以用户确认为准
- 幂等：`INSERT IGNORE` + 联合主键 `(from_id, to_id, relation_type)`

**校验**：
```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Kurt Gödel' OR b.name_en='Kurt Gödel';
```

---

## 第 5 步：设计配色方案

- 哥德尔的气质关键词：**深邃、理性、边界发现者、维也纳知识分子传统、数学柏拉图主义的庄严**
- **建议配色：深勃艮第红 + 古金 + 暗灰**（维也纳学术传统的深色木调 + 真理的金色光芒 + 逻辑的灰阶）

> ⚠️ 已有配色回顾（避免撞色）：
> - Hilbert：普鲁士蓝+金 | Grothendieck：深靛+金 | Noether：深紫罗兰+暗玫瑰金
> - Riemann：墨绿+银灰 | von Neumann：深黑+电路绿 | Turing：深黑+暗青+冷银
> - Kolmogorov：深松绿+古铜金 | Serre：勃艮第红+象牙暖金 | Weyl：深琥珀金+星夜紫 | Weil：勃艮第深红+石板暖灰

- Gödel 配色方案：
  - **主色 (coverprimary)**：**深勃艮第 + 暮紫** — 维也纳老咖啡馆的深色木调 + 精神世界的深邃。区别于 Serre 的勃艮第红（更亮），Gödel 的色调更深、更沉静
  - **强调色 (coveraccent)**：**古金** — 柏拉图式数学真理的光芒，也是维也纳知识黄金时代的余晖
  - 四个分类色，对应 Gödel 的四大支柱：
    - **badgelogic** (逻辑/不完备性定理) — 深暮紫 `#4A148C`（形式系统的深沉）
    - **badgeset** (集合论/可构成宇宙 L) — 古金 `#C9A84C`（数学真理的柏拉图之光）
    - **badgephysics** (广义相对论/Gödel 宇宙) — 暗青金石 `#1A5276`（时空的深邃）
    - **badgephilosophy** (哲学/柏拉图主义) — 暖灰褐 `#6D4C41`（维也纳学术传统的温润）
  - 各面板色：purplepanel(暮紫)/goldpanel(古金)/bluepanel(暗青)/graypanel(暖灰褐)

---

## 第 6 步：规划幻灯片序列

哥德尔的内容分为三层：数学（不完备性定理 + 集合论）、物理（Gödel 宇宙）、哲学（柏拉图主义），建议 17 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《哥德尔：数学基础的边界》 / Kurt Gödel 1906–1978 + 四色badge
02  为什么哥德尔改变了数学的基本面貌 — 不完备性定理 · 可构成宇宙 · 数学柏拉图主义 · Gödel 宇宙

=== 维也纳的逻辑天才 ===
03  Brünn 到维也纳 (1906–1929) — "为什么先生" · 维也纳学派 · 完备性定理博士论文
04  不完备性定理 (1931) — Königsberg 会议，震惊 Hilbert 和整个数学界

=== 不完备性定理的深度解读 ===
05  第一不完备性定理 — 任何足够强的形式系统存在不可判定命题
06  第二不完备性定理 — 一个系统不能证明自身的一致性

=== 集合论与可构成宇宙 ===
07  可构成宇宙 L (1938) — Gödel 构造了集合论的最小模型
08  连续统假设的相对一致性 — CH + AC 与 ZF 不矛盾

=== 流亡普林斯顿 ===
09  逃往美国 (1939–1940) — 纳粹吞并奥地利 · 绕道西伯利亚 · IAS 的孤岛
10  与 Einstein 的友谊 — "我去办公室的唯一理由是能和 Gödel 一起走回家"

=== 物理与哲学 ===
11  Gödel 宇宙 (1949) — 旋转宇宙中的时间旅行 · 送给 Einstein 70 岁的生日礼物
12  数学柏拉图主义 — 数学真理独立存在，超越任何形式系统的把握

=== 终章 ===
13  宪法漏洞与偏执 (1948–1970s) — 入籍听证会的趣事 · 偏执狂的逐步吞噬
14  饥饿而死 (1978) — 逻辑天才死于对食物的恐惧，71 岁，体重 29 公斤

=== 遗产 ===
15  哥德尔的遗产 — Turing、Cohen、Chaitin……不完备性定理开启的整个追问
16  思想回响 — 哥德尔证明了：真理永远大于证明
17  结束页 — "数学真理独立存在，我们只能不断接近它，却永远无法完全捕获它。"
```

> **可以微调。** 征求我的意见后再开始写代码。

---

## 第 9 步：史实审查 + 术语审查

### 哥德尔特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 哥德尔特有的高危点 |
|---------|---------------------|
| **不完备性定理的技术表述** | ★ 第一定理：任何包含 PA（皮亚诺算术）、ω-一致的、能递归公理化的一致系统，存在一个不可判定的命题 G，使得 G 和 ¬G 都不能被证明。第二定理：这样的系统不能证明自身的一致性。**不要说"任何数学系统都不完备"**——这只是对算术有效。 |
| **完备性 vs 不完备性** | 博士论文（1929）是一阶逻辑的**完备性**定理；1931 年论文是包含算术的系统的**不完备性**定理。两者针对的是不同的逻辑层次。不能混淆。 |
| **"否定 Hilbert 纲领"** | ★ Gödel 的第二不完备性定理确实证明了 Hilbert 原始纲领（用有穷方法证明算术一致性）是不可能的。但 Hilbert 纲领后来的发展（Gentzen 用超穷归纳法证明了 PA 一致性）仍然有意义。不要说"Hilbert 纲领被彻底摧毁"。 |
| **与 Turing 的关系** | Gödel 不完备性定理启发了 Turing 定义可计算性（Turing 机），但不是 Turing 的直接导师。关系是思想上的继承，不是师徒。 |
| **Gödel 宇宙的时间旅行** | Gödel 度量确实包含闭合时间曲线 (CTCs)，但模型要求宇宙整体旋转且无膨胀——不符合观测。不要给人"Gödel 证明了时间旅行可能"的错觉。 |
| **精神疾病的精确描述** | 偏执狂 (paranoia) 而非"精神分裂"或"抑郁症"。他害怕被下毒，害怕冰箱排放气体。不要使用模糊的精神疾病术语。 |
| **死因** | "malnutrition and inanition caused by personality disturbance" — 拒绝进食导致的营养不良。不要说"饿死"二字太轻浮，用"因偏执导致拒绝进食而死于营养不良"。 |
| **入籍听证会** | 1948 年 12 月 5 日，Trenton 法院。Gödel 对法官 Phillip Forman 解释宪法漏洞。Einstein 和 Morgenstern 在场作证/救场。Judge Forman 本人也曾在 Princeton 学习法律——他理解 Gödel 不是在找麻烦。 |
| **国籍** | 奥地利 → 美国（1948 年入籍）。不是德国！虽然出生在奥匈帝国的德语区。 |
| **"为什么先生" (Herr Warum)** | 童年绰号，Wikipedia 有记载。可以使用。 |
| **维也纳学派的非完全从属** | Gödel 参加维也纳学派聚会，但从不接受逻辑实证主义。他是柏拉图主义者，认为数学对象真实存在——这与实证主义的"一切知识来自经验"根本冲突。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| completeness theorem | 完备性定理 | 注意是 Gödel 完备性而非不完备性 |
| incompleteness theorems | 不完备性定理 | 不要简化为"不完备定理"——这是两个定理 |
| ω-consistent | ω-一致性 | Omega 一致性，技术术语 |
| constructible universe (L) | 可构成宇宙 (L) | 区别于 von Neumann 的 V |
| continuum hypothesis (CH) | 连续统假设 | — |
| relative consistency | 相对一致性 | "如果 ZF 是一致的，那么 ZF+AC+GCH 也是一致的" |
| Gödel metric | Gödel 度量 | 广义相对论中的旋转宇宙解 |
| closed timelike curve (CTC) | 闭合时间曲线 | 物理术语 |
| mathematical Platonism | 数学柏拉图主义 | Gödel 的哲学立场 |
| primitive recursive function | 原始递归函数 | Gödel 1931 年引入的概念 |
| Entscheidungsproblem | 判定问题 | Hilbert 提出的问题，Turing 和 Church 解决了它 |
| forcing | 力迫法 | Cohen 发明的方法，Gödel 没有使用 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"否定一切"叙事** | 不完备性定理不是"一切形式系统都不完备"，只说"足够强的系统"。Presburger 算术就是完备的 |
| **技术过度简化** | 不完备性定理的技术内容非常精确。如果感到不确定，宁愿写简单但准确，也不写复杂但错误 |
| **悲剧过度渲染** | Gödel 的晚年非常悲惨，但叙事重点应该是他的思想和贡献。"饥饿而死"是结局，不是故事的全部 |
| **伪引语** | Gödel 的很多"名言"来自二手回忆（如王浩的传记）。不要在 Beamer 中使用无法在 page.md 中验证的引语 |
| **Platonism 的过度简化** | Gödel 的柏拉图主义非常复杂——不是简单的"数字在天上飘"。如果不能用 2 页讲清楚，就用半页简述 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/Kurt_Godel/page.md，从头到尾逐段阅读全文
2. 同时打开 Kurt_Godel_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ Gödel 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **不完备性定理的技术表述** | 最容易犯错的地方 | page.md 搜索 "incompleteness" "ω-consistent" |
| **"Hilbert 纲领被摧毁"** | 过度简化 | page.md 搜索 "Hilbert's program" |
| **Gödel 宇宙的时间旅行断言** | CTCs 的物理意义有争议 | page.md 搜索 "closed timelike" "time travel" |
| **精神疾病的诊断名称** | 偏执狂不是精神分裂 | page.md 搜索 "paranoia" "personality" |
| **死因精确描述** | 不是简单的"饿死" | page.md 搜索 "malnutrition" "inanition" |
| **国籍归属** | 奥地利 → 美国，不是德国 | page.md 搜索 "Austrian" |
| **宪法漏洞事件的真实性** | 有可靠记载但需准确 | page.md 搜索 "citizenship" "constitution" "loophole" |
| **ForMemRS 年份** | 提示词曾记 1961，page.md infobox 为 1968 | page.md 搜索 "Foreign Member" |

### 优先级定义

| 优先级 | 定义 | Gödel 实际案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | "Gödel 证明了所有数学系统都不完备"（严重错误）；"Gödel 是德国人" |
| 🟡 P1 | **来源存疑/捏造** | 无法验证的引语；"Hilbert 纲领被彻底毁灭"（过度简化） |
| 🟢 P2 | **重要遗漏** | Gödel–Gentzen 翻译；Cohen forcing 补完 CH 独立性；王浩传记的核心记录 |
| ⚪ P3 | **可选补充** | Gödel 对 Husserl 现象学的兴趣；Gödel 本体论证明的草稿 |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

哥德尔的气质：**深邃、理性、孤独、维也纳知识分子的庄重** — 不应该是史诗或英雄风格，而是深沉克制的音乐。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | PAST | alex-productions | `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` | 历史感、深沉，匹配 Gödel 的孤独沉思 |
| ★★★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 内敛的深度，猜想与永恒 |
| ★★ | The Flow of Time | alex-productions | `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` | 时间感，匹配不完备性定理的永恒性 |
| ★ | Nostalgia | alex-productions | `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` | 维也纳的怀旧，Einstein 友谊的情感锚 |

**操作**：复制选定的 `.wav` 到 `Kurt_Godel/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 完整操作手册（§二十 社会关系 / §二十一 字段梳理） |
| `mathematician/pages/Kurt_Godel/page.md` | Gödel Wikipedia 正文 |
| `mathematician/pages/Kurt_Godel/metadata.json` | Gödel Wikidata 元数据 |
| `mathematician/pages/Kurt_Godel/images.txt` | 图片 URL 清单 |
| `MySQL/seed_godel_relations.py` | 社会关系入库脚本（第 4.5 步） |
| `MySQL/seed_godel_full.py` | 全字段补全脚本（第 0.5 步） |
| `mathematician/presentations/turing/Alan_Turing_zh.tex` | Turing 完整源码（最新参考） |
| `mathematician/presentations/neumann/John_von_Neumann_zh.tex` | von Neumann 完整源码 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Gödel 的独特性在于他不是一个"建造者"——他是一个"测绘边界的人"
> 2. 不完备性定理不是虚无主义——Gödel 是柏拉图主义者，他相信数学真理的客观存在
> 3. 完备性 → 不完备性：博士论文和开创性论文的对比是绝佳叙事
> 4. Einstein 的友谊是叙事的情感锚——两个流亡者，两个探索终极真理的人
> 5. 可构成宇宙 L 是 Gödel 技术成就的巅峰——不要只讲不完备性定理而忽略集合论
> 6. Gödel 宇宙是数学家的诗——Einstein 70 岁生日的礼物，时间旅行的严格解
> 7. "饥饿而死"是悲剧但不是全部——叙事重点应该是他发现了什么，而不是他死于什么
> 8. **数据库同步**：先完成第 0.5 步（字段核对表逐项填值）与第 4.5 步（补足社会关系、5 人占位），再开始立传
> 9. 结尾主题句：**"真理永远大于证明——这是 Gödel 留给数学最深层的洞见。"**
