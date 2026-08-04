# 米尔诺 (John Milnor) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Weyl、Cartan、Lebesgue 等成品为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: John Milnor (1931– )
- **气质关键词**: **微分拓扑的革命者、1962 年 Fields 奖得主、优雅的写作者、百科全书式的几何学家、少年天才**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本：
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/John_Milnor/`
- **参考模板**: `cartan/`, `weyl/`, `lebesgue/`, `artin/` 四个完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/John_Milnor/`

输出以下信息供校验：

- **生卒日期**：1931-02-20 ~ (在世，2026 年 95 岁)
- **国籍**：美国
- **出生地**：Orange, New Jersey, USA
- **博士导师**：Ralph Fox（普林斯顿大学）
- **博士论文**：1954，《Isotopy of Links》（纽结的同痕）—— 年仅 23 岁
- **主要任职机构**：
  - 1954–1968: 普林斯顿大学 (Princeton University)
  - 1968–1970: MIT
  - 1970–1989: 普林斯顿高等研究院 (IAS)
  - 1989–至今: SUNY Stony Brook（纽约州立大学石溪分校）
- **关键荣誉**：
  - 1962: Fields 奖（因证明七维球面上存在 28 种微分结构）
  - 1989: Wolf 奖
  - 2011: Abel 奖
  - 1965: 美国国家科学奖章
  - 1982: Steele 奖（数学写作）
- **重要合作者/学生**：
  - 导师: Ralph Fox（纽结理论）
  - 受影响者: William Thurston（三维流形）、Michael Freedman（四维流形）
  - 合作者: Michel Kervaire（怪球面）、James Stasheff、John Moore

### 关键时间线（15–20 个节点）：
- 1931: 生于新泽西州 Orange
- 1944: 13 岁，自学微积分
- 1948: 17 岁，进入普林斯顿大学
- 1951: 20 岁，本科毕业，继续在普林斯顿读研
- 1954: 23 岁，获博士学位（导师 Ralph Fox）
- 1956: 25 岁，证明七维球面存在非标准的微分结构（"怪球面"）—— 震惊数学界
- 1957: 出版《微分拓扑》(Differential Topology) 讲义
- 1961: 与 Michel Kervaire 合作完成怪球面分类
- 1962: 31 岁，获 Fields 奖
- 1963: 出版《Morse 理论》(Morse Theory) —— 经典教材
- 1968: 出版《代数 K-理论导论》(Introduction to Algebraic K-Theory)
- 1970: 转入普林斯顿高等研究院 (IAS)
- 1974: 出版《复超曲面奇点》(Singular Points of Complex Hypersurfaces)
- 1985: 出版《全纯动力学》(Dynamics in One Complex Variable)
- 1989: 转入 SUNY Stony Brook，成立几何研究所
- 2004: 出版《Hairy Ball Theorem and Fixed Points》
- 2011: 80 岁，获 Abel 奖
- 至今: 仍在石溪分校活跃

### 人格特质线索：
- "数学界的莫扎特"——23 岁做出震惊世界的发现，此后 70 年持续产出
- 极其优秀的数学写作者——Steele 奖（1982）表彰他的写作
- 以"教科书式清晰"著称——他写的每一本书都成为该领域的标准教材
- 以解决"最简单的难题"闻名——不是堆积技术，而是找到本质的洞见
- 60 多岁开始进入全新的研究领域（复动力系统），并再次写出经典著作
- 谦虚低调——从不自夸，被同行尊为"活着的传奇"却从不以此自居
- 他证明怪球面的论文只有 8 页——展现了"少即是多"的数学美学

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 微分拓扑 | 七维怪球面 (exotic spheres) —— 证明 S⁷ 存在 28 种微分结构 | 1956 |
| 微分拓扑 | Milnor–Kervaire 怪球面分类 | 1961 |
| K-理论 | 代数 K-理论的开创性贡献 | 1960s |
| Morse 理论 | 《Morse 理论》经典教材，推广 Morse 不等式到流形 | 1963 |
| 奇点理论 | 复超曲面奇点的 Milnor 纤维化 | 1968 |
| 代数 K-理论 | Milnor K-群 K₂(F) | 1970 |
| 微分几何 | Milnor–Wood 不等式 | 1970s |
| 复动力系统 | 一维复动力系统中的里程碑工作 | 1985–2000 |
| 纽结理论 | Milnor 不变量、Milnor 纽结群 | 1954 |

### ★ 米尔诺独有的叙事线索

1. **怪球面 —— 23 岁的炸弹** — 1956 年，25 岁的 Milnor 证明了一个爆炸性的事实：在七维球面上，可以放置 28 种不同的微分结构——也就是说，存在 27 种"看起来像球面、但不是标准球面"的七维流形。这是微分拓扑作为独立学科诞生的标志。论文只有 8 页。
2. **普林斯顿的神童轨道** — 本科、博士、教授，全在普林斯顿。17 岁入学，20 岁毕业，23 岁博士，25 岁做出革命性发现。这是一条完美的天才轨迹——但 Milnor 的谦逊让这一切看起来毫不张扬。
3. **教科书革命的隐形推手** — Milnor 写的每一本教材都改写了该领域的教学方式。Morse 理论、微分拓扑、复动力系统——在这些领域，学习者的第一句话往往是"先读 Milnor"。
4. **60 岁后的新生涯** — 1980 年代，50 多岁的 Milnor 进入一个全新领域：复动力系统。大多数数学家在这个年龄已经"完成"了。但 Milnor 不仅掌握了新领域，还写了两本经典著作：*Dynamics in One Complex Variable* (1999) 和 *Laminations and Foliations*。他是"终身学习"的终极化身。
5. **写作者的天赋** — 1982 年 AMS 颁发 Steele 数学写作奖给 Milnor。在数学界，大家都承认：如果有 Milnor 写的版本，就读他的版本。他不需要抽象的形式主义——他用例子、直觉和透彻的理解来说明一切。
6. **三冠王** — Fields (1962)、Wolf (1989)、Abel (2011)——同时获得数学界三大最高荣誉的人屈指可数。Milnor 是其中之一。
7. **从纽结到奇点到动力系统** — 他的职业生涯轨迹展现了罕有的数学广度：纽结理论 (1954) → 微分拓扑 (1956) → K-理论 (1960s) → 奇点理论 (1968) → 动力系统 (1980s+)。没有哪两个领域相距太远——他看到了它们之间的隐藏连接。

### 人物关系

- **Ralph Fox（博士导师）** — 普林斯顿拓扑学家、纽结理论先驱。Fox 的"非标准思维"（他追求形式化简化的极限）影响了 Milnor 终生。
- **Michel Kervaire（合作者）** — 瑞士数学家。与 Milnor 合作完成了怪球面的完整分类。
- **William Thurston（影响的后辈）** — Milnor 的工作直接为 Thurston 的几何化和三维流形工作提供了语言和工具。
- **John Nash（普林斯顿同事）** — 两人在同一个数学系。Nash 的博弈论与 Milnor 的拓扑学是普林斯顿黄金时代的两大支柱。
- **Stephen Smale（同代人）** — 另一位 Fields 奖得主。两人在动力系统和流形拓扑上有交集。
- **IAS 同事** — 在普林斯顿高等研究院期间与 Borel、Langlands 等有广泛交流。

---

## 第 5 步：设计配色方案

- **建议配色：普林斯顿橙 + 石板黑 + 银白** —— 常春藤的经典优雅 + 几何的精确 + 写作的清晰
- 需要与已有配色完全不同：
  - Cartan, Weyl, Hilbert, Hausdorff, Schwartz 等均已有独特配色
- 四个分类色，对应 Milnor 的四大支柱：
  - **badgetopo** (微分拓扑/怪球面) — 普林斯顿橙 `#E87722`
  - **badgeMorse** (Morse 理论/奇点) — 石板黑 `#2F3542`
  - **badgeKtheory** (K-理论/代数) — 深绿 `#2E5A40`
  - **badgedyn** (动力系统/后期) — 银灰 `#C0C0C0`

---

## 第 6 步：规划幻灯片序列（建议 16 页）

```
00  OpenMath 项目首页（从 cover 模板 \input）

=== 封面与总览 ===
01  封面 — 《米尔诺：微分拓扑的革命者》 / John Milnor 1931–
02  为什么 Milnor 是"活着的传奇" — 23 岁改变拓扑学，70 年持续创新

=== 早年 ===
03  普林斯顿的神童 (1931–1954) — 17 岁入学，23 岁博士
04  怪球面 (1956) — 25 岁的 8 页论文，微分拓扑的诞生

=== 主要成就 ===
05  微分拓扑的革命 — 怪球面·Milnor–Kervaire 分类·h-配边定理
06  Morse 理论 — 从 Bott 周期律到流形拓扑
07  代数 K-理论 — Milnor K-群，K₂(F) 的诞生
08  复超曲面奇点 — Milnor 纤维化，拓扑与代数的奇点连接

=== 写作者 ===
09  教科书的革命 — Morse 理论·微分拓扑·复动力系统——他写的都是经典

=== 晚年新生 ===
10  60 岁后的新生涯 — 复动力系统，证明"永远不会太晚"

=== 遗产 ===
11  三冠王的荣誉 — Fields (1962) · Wolf (1989) · Abel (2011)
12  继承者 — Thurston·Smale·Freedman —— 一个领域的建筑师
13  米尔诺的遗产 — 怪球面 · K-理论 · 奇点 · 动力系统

=== 结尾 ===
14  思想回响 — "他定义了什么是好的数学写作"
15  结束页 — 主题句：他 25 岁时用 8 页论文改变了拓扑学。70 年后，他还在改变它。
```

略作压缩（含 OpenMath 首页共 16 页）。

---

## 第 9 步：史实审查

### 米尔诺特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **怪球面的"发现"** | 严格来说，Milnor 证明了存在性（构造），而非"发现了预先存在的对象"。他是创造者而非发现者。 |
| **28 种结构的数字** | S⁷ 有 28 种微分结构。这个数字不应该用在其他维数！不同维数有不同数量。 |
| **"h-配边定理"归属** | Stephen Smale 证明 h-配边定理（1961 Fields 奖的核心）。Milnor 的工作是怪球面的分类——两者相关但不同。不要混淆。 |
| **K-理论的先驱** | Atiyah–Hirzebruch 创立拓扑 K-理论。Milnor 的贡献是代数 K-理论。两码事。 |
| **仍在世** | Milnor 2026 年 95 岁，仍在 SUNY Stony Brook。不要用过去时描述他！ |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| exotic sphere | 怪球面 | 不是"奇异球面"（"奇异"通常指 singularity） |
| differentiable structure | 微分结构 | 不是"可微结构" |
| h-cobordism | h-配边 | Smale 的定理 |
| Morse theory | Morse 理论 | 写作为 Morse 理论，不是"莫尔斯理论" |
| Milnor fibration | Milnor 纤维化 | 奇点理论核心 |
| K₂(F) | Milnor K₂ | 不是 "K-2" |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **年龄相关** | 不要用过去时描述尚在世的人。所有涉及"Milnor 是..."用现在时 |
| **Fields 的年龄限制** | 1962 年 Milnor 31 岁刚好在 40 岁限制内 |
| **三冠王名单** | Fields+Wolf+Abel 三冠王目前人数极少，注意不要把"几"个人写成确切数字 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

> **核心原则：Beamer 写完后，必须回到本地 Wikipedia 存档（page.md + metadata.json），逐项对照审核。**

### 10 项终审清单
（同上模板）

### ⚠️ Milnor 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **怪球面维数** | S⁷ 的 28 种结构——数字不能错 | page.md 搜索 "exotic" "sphere" "28" |
| **博士论文题目** | 1954 "Isotopy of Links"，不是怪球面 | page.md 搜索 "thesis" |
| **Fields 奖年份** | 1962，确认 | page.md 搜索 "Fields" |
| **Abel 奖年份** | 2011，确认 | page.md 搜索 "Abel" |
| **K-理论归属** | 区分代数 K-理论 (Milnor) 和拓扑 K-理论 (Atiyah) | page.md 搜索 "K-theory" |
| **与 Smale 的关系** | h-配边定理是 Smale 的 | page.md 搜索 "Smale" "h-cobordism" |
| **当前任职** | SUNY Stony Brook，不是 IAS（1989 年已离开） | page.md 搜索 "Stony Brook" |
| **出生地** | Orange, NJ（不是 Orange County CA） | page.md 搜索 "Orange" |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`

| 优先级 | 曲目 | 来源 | 理由 |
|:--:|------|------|------|
| ★★★ | Timeless | alex-productions | 活着的传奇——70 年不变的质量 |
| ★★★ | Eternals | alex-productions | 经典与永恒——教科书的标准 |
| ★★ | Expedition | alex-productions | 60 岁后的新生涯——永不停止探索 |

---

## 第 16 步：第二次 Wikipedia Review（Round 2）

> Round 2 重点：怪球面的发现叙事、与 Smale 的 h-配边关系、K-理论归属不混淆。

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Milnor **仍在世**（2026 年 95 岁）。所有描述用现在时或"至今"
> 2. 怪球面是他最著名的贡献——但博士论文是纽结理论，不是怪球面
> 3. **28 种**只适用于 S⁷——不要写成"所有维数"
> 4. Milnor 是写作者的天才——Steele 奖 (1982) 不能遗漏
> 5. K-理论要区分：代数 K-理论 (Milnor) ≠ 拓扑 K-理论 (Atiyah)
> 6. 结尾主题句：**他 25 岁时用 8 页论文改变了拓扑学。70 年后，他还在改变它。**
