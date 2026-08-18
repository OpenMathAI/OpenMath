# 嘉当 (Élie Cartan) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Weyl、Artin、Lebesgue 等成品为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Élie Cartan (1869–1951)
- **气质关键词**: **李群理论的巨人、微分几何的孤独建筑师、Hermann Weyl 的对话者、陈省身的老师**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本：
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Elie_Cartan/`
- **参考模板**: `lebesgue/`, `artin/`, `weyl/`, `banach/` 四个完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Elie_Cartan/`

输出以下信息供校验：

- **生卒日期**：1869-04-09 ~ 1951-05-06，享年 82 岁
- **国籍**：法国
- **出生地**：Dolomieu（多洛米约），法国 Isère 省
- **博士导师**：Gaston Darboux（巴黎高等师范学校）、Sophus Lie（间接影响）
- **博士论文**：1894，《Sur la structure des groupes de transformations finis et continus》（论有限连续变换群的结构）
- **主要任职机构**：
  - 1894–1903: 蒙彼利埃大学 (Université de Montpellier)
  - 1903–1909: 里昂大学 (Université de Lyon)
  - 1909–1912: 南锡大学 (Université de Nancy)
  - 1912–1940: 巴黎大学 (Université de Paris, Sorbonne)
- **关键荣誉**：
  - 1931: 法国科学院院士 (Académie des Sciences)
  - 1937: 罗巴切夫斯基奖 (Lobachevsky Prize)
  - 1947: 英国皇家学会外籍院士 (Foreign Member of the Royal Society)
  - 多项法国学术大奖 (Prix Poncelet, Prix Petit d'Ormoy, Leconte Prize 1930 等)
  - 1940: 退休，离开索邦
- **重要合作者/学生**：
  - 导师与合作者: Darboux, Lie (思想影响)
  - 儿子: Henri Cartan (Bourbaki 创始成员，代数拓扑与层论)
  - 学生: 陈省身 (Shiing-Shen Chern, 整体微分几何之父)
  - 学生: Charles Ehresmann (微分几何与纤维丛)
  - 学生: Georges de Rham (de Rham 上同调)
  - 对话者: Hermann Weyl (两人对微分几何的理解相互照亮)

### 关键时间线（15–20 个节点）：
- 1869: 生于法国 Isère 省的 Dolomieu 村，父亲是铁匠
- 1888: 进入巴黎高等师范学校 (ENS)，与物理学家 Jean Perrin 成为同学
- 1891: 从 ENS 毕业，服兵役一年，晋升中士
- 1894: 完成博士论文，Darboux 和 Sophus Lie 共同指导，分类复单李代数（纠正了 Killing 的错误）
- 1894–1896: 在蒙彼利埃大学任讲师
- 1896–1903: 在里昂大学任讲师
- 1899–1904: 发展外微分形式和 Pfaff 方程组理论
- 1903: 在南锡大学晋升教授；同年与 Marie-Louise Bianconi 结婚
- 1904: 长子 Henri Cartan 出生
- 1909: 举家迁往巴黎，在索邦任讲师
- 1912: Poincaré 推荐升任索邦教授
- 1913: 发表 Cartan 子代数的核心论文；独立发现旋量 (spinors)
- 1920s: 发展 Cartan 联络理论
- 1926–1935: 完成对称空间的系统分类
- 1931: 当选法国科学院院士
- 1936: 陈省身来到巴黎跟随 Cartan 做博士后研究
- 1937: 获罗巴切夫斯基奖 (Lobachevsky Prize)
- 1940: 退休，时年 71 岁
- 1946: 任法国科学院院长 (President)
- 1947: 当选英国皇家学会外籍院士
- 1951: 在巴黎去世，享年 82 岁

### 人格特质线索：
- "孤独的巨人" — 他在 20 世纪前 30 年的工作几乎不被理解
- Weyl 对他的评价："读 Cartan 的论文像是在丛林中跋涉——繁茂、复杂、充满未被命名的宝藏。"
- 安静、谦逊，从不追逐名利——与当时巴黎数学界的喧嚣形成鲜明对比
- 极其多产：出版了 9 部专著和近 200 篇论文，但每一篇都因其"不可读性"而臭名昭著
- 他的"不可读"是因为他总是在发明新概念、新语言——而非效率低下
- 从不说自己的工作是"革命性"的——但事后看，他一个人开辟了半个微分几何
- 培养了几代法国几何学家——陈省身说："Cartan 的工作在活着的时候没人真正读懂，但他去世后每个人都在用他的语言。"

---

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_cartan_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q274639` | ⚠️ 待核 |
| 2 | `people` | name_zh | `埃利·嘉当` | ⚠️ NULL |
| 3 | `people` | name_variants | `["李群与微分几何大师","外微分形式之父"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1869-04-09` / `1951-05-06` | ⚠️ NULL |
| 6 | `people` | description | `French mathematician (1869–1951)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)`、`physicist(2)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `differential geometry`、`general relativity`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Leconte 1930`、`Poncelet`、`Lobachevsky 1937`、`Commander of the Legion of Honour`、`ForMemRS 1947` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: ENS、University of Paris`；`employment: Montpellier、Lyon、Nancy、Science Faculty of Paris` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `France` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（10 条） | ⚠️ 全空 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_cartan_relations.py`。

**入库范围（10 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Jean Gaston Darboux → Cartan | 有向 | ⚠️ 占位 |
| 导师 | Sophus Lie → Cartan | 有向 | ⚠️ 占位 |
| 学生 | Cartan → Charles Ehresmann | 有向 | ⚠️ 占位 |
| 学生 | Cartan → Georges de Rham | 有向 | ⚠️ 占位 |
| 学生 | Cartan → Kentaro Yano | 有向 | ⚠️ 占位 |
| 父子 | Cartan → Henri Cartan | 有向 | ✅ 在库（id=69） |
| 同事 | André Weil | 无向 | ✅ 在库（id=8） |
| 同事 | Jean Dieudonné | 无向 | ✅ 在库（id=370） |
| 同事 | Claude Chevalley | 无向 | ✅ 在库（id=27） |
| 同事 | Laurent Schwartz | 无向 | ✅ 在库（id=17） |

- 缺失人物（5 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 李群 | Cartan 子代数 —— 半单李代数的核心结构 | 1913 |
| 李群 | Cartan 分类 —— 所有复半单李代数的完整分类（纠正了 Killing） | 1894–1914 |
| 李群 | Cartan–Killing 形式 —— 李代数的"内积" | 1894 |
| 外微分 | 外微分形式与 Cartan 结构方程 | 1899–1904 |
| 微分几何 | Cartan 联络（仿射联络）—— 广义相对论的数学语言 | 1920s |
| 对称空间 | Cartan 对称空间的系统分类 | 1926–1935 |
| 微分几何 | 活动标架法 (méthode du repère mobile) | 1930s |
| Pfaff 系统 | Pfaff 形式与偏微分方程的外微分方法 | 1900s |
| 旋量 | Cartan 旋量理论 —— 1930 年代独立发现，后与物理学对接 | 1930s |

### ★ 嘉当独有的叙事线索

1. **"孤独的巨人"** — 这是 Cartan 最核心的叙事。他在 20 世纪前 30 年做的工作，当时几乎没有人理解。Weyl 说："读 Cartan 的论文像是在丛林中跋涉。" 但后来发现，他一个人开辟了半个现代微分几何。
2. **李群的分类** — Killing 开创了李代数分类，但充满了错误。Cartan 的博士论文 (1894) 以"极优" (très honorable) 成绩通过，纠正了 Killing 的所有错误，给出了完整的复半单李代数分类。这奠定了 20 世纪李理论的基础。
3. **Cartan 联络** — 今天广义相对论使用的数学语言（纤维丛上的联络），Cartan 在 1920 年代就已发明。Einstein 的引力理论背后，是 Cartan 的数学框架。这种"先于物理学"的数学洞见是他的标志。
4. **陈省身的老师** — 1936 年，25 岁的陈省身从汉堡来到巴黎跟随 Cartan 做博士后。陈说 Cartan 的教学方法独一无二：每两周在 Cartan 家中见面一次，讨论数学。陈省身后来成为整体微分几何之父，而他自己说：我的一切都来自 Cartan。
5. **父与子** — Élie Cartan（几何）与 Henri Cartan（代数/层论）是数学史上最伟大的父子档之一。Henri 是 Bourbaki 的创始成员，发展了层论和同调代数。一种卓越的数学基因在两代人之间传承。
6. **外微分 —— 语言的发明者** — 在 Cartan 之前，微分形式是一个混乱的领域。Cartan 创造了一套系统性的外微分运算体系——Cartan 结构方程——成为现代微分几何的基本语言。这不是发现了一个定理，而是发明了一套语法。
7. **对称空间的分类 —— 六年的孤独劳作** — 从 1926 到 1935 年，Cartan 系统地分类了所有对称空间。这项工作在当时被认为是"无人关心的巨大工程"。但后来，对称空间成了表示论、数论、调和分析的核心对象。

### 人物关系

- **Gaston Darboux（导师）** — 法国几何学家，Cartan 的博士导师。Darboux 是法国微分几何学派的领军人物。
- **Sophus Lie（思想导师）** — 挪威数学家，李群和李代数的创始人。Cartan 继承了 Lie 的纲领并将其系统化。
- **Wilhelm Killing** — Cartan 的博士论文纠正了 Killing 在李代数分类中的大量错误。两人在论文中从未直接交锋——Cartan 用精确代替了纠正。
- **Hermann Weyl（对话者）** — 两人在 1920s–1930s 对微分几何的理解相互照亮。Weyl 是最早意识到 Cartan 工作深度的人之一。
- **陈省身（学生）** — 中国的微分几何之父。1936 年在巴黎师从 Cartan。Chern 类、Chern–Simons 理论的源头都可以追溯到 Cartan 的外微分方法。
- **Charles Ehresmann（学生）** — 法国几何学家，纤维丛理论的奠基者之一。Ehresmann 的联络概念是 Cartan 联络的自然推广。
- **Henri Cartan（儿子）** — Bourbaki 创始成员，层论、同调代数的先驱。父子的数学风格截然不同：Élie 深沉、孤独、探索；Henri 系统、结构化、集体化。
- **Albert Einstein** — Cartan 和 Einstein 在 1929–1932 年间通信讨论了统一场论。Cartan 告诉 Einstein 他的数学框架早已存在。

---

## 第 5 步：设计配色方案

- **建议配色：法兰西深蓝 + 几何金 + 象牙白** —— 巴黎学派的优雅 + 几何结构的庄严 + 孤独者的安静
- 需要与已有配色完全不同：
  - Hilbert：普鲁士蓝 + 金
  - Grothendieck：深靛 + 金
  - Weyl：琥珀金 + 星夜紫
  - Artin：深林翡翠绿 + 暖铜金
  - Lebesgue：巴黎灰 + 赤陶红
  - Serre：勃艮第红 + 象牙暖金
  - Noether：深紫罗兰 + 暗玫瑰金
  - Riemann：墨绿 + 银灰
  - Kolmogorov：深松绿 + 古铜金
  - von Neumann：深黑 + 电路绿
  - Banach：弗罗茨瓦夫蓝 + 蜂蜜金
  - Gödel：维也纳深棕 + 古书金
- 四个分类色，对应 Cartan 的四大支柱：
  - **badgeLie** (李群/李代数) — 法兰西深蓝 `#002147`
  - **badgeConn** (Cartan 联络/纤维丛) — 几何金 `#DAA520`
  - **badgeSym** (对称空间/分类理论) — 古铜 `#8B6914`
  - **badgeExt** (外微分/活动标架) — 银灰 `#708090`

---

## 第 6 步：规划幻灯片序列（建议 17 页）

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《嘉当：孤独的微分几何巨人》 / Élie Cartan 1869–1951
02  为什么嘉当是"孤独的巨人" — 他一个人开辟了半个现代微分几何

=== 早年 ===
03  铁匠之子到 ENS (1869–1894) — 从 Dolomieu 村到巴黎高等师范学校
04  博士论文 (1894) — 纠正 Killing，完成复半单李代数的完整分类

=== 李群理论 ===
05  Cartan 子代数与 Cartan–Killing 形式 — 半单李代数的核心结构
06  李群的分类体系 — 1894 到 1914 的二十年工作，奠定了 20 世纪李理论

=== 微分几何 ===
07  外微分与 Cartan 结构方程 (1899–1904) — 发明现代微分几何的语法
08  Cartan 联络 (1920s) — 广义相对论的数学语言，比物理学早了十年
09  活动标架法 (1930s) — 微分几何的通用计算方法

=== 对称空间 ===
10  对称空间的分类 (1926–1935) — 六年的孤独劳作，后来的核心工具

=== 传承 ===
11  陈省身的老师 — 数学史上最成功的师徒传承之一
12  父与子 — Élie Cartan → Henri Cartan，数学基因的跨代传承

=== 孤独者 ===
13  职业生涯与荣誉 — 从蒙彼利埃到索邦，安静的上升
14  Weyl 的敬意 — "没有人比他更深地改变了微分几何"

=== 遗产 ===
15  嘉当的遗产 — 李群 · 联络 · 外微分 · 对称空间，他的语言无处不在
16  思想回响 — "他活着的时候没人读懂他，但每个人都在用他的语言"

=== 结尾 ===
17  结束页 — 主题句：他一个人，在丛林里开辟了半个微分几何。
```

---

## 第 9 步：史实审查

### 嘉当特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **Killing 的错误** | Cartan 确实纠正了 Killing 的分类错误。但措辞要谨慎——不要暗示 Killing 是"愚蠢的"或"失败的"。Killing 开创了李代数分类的整个方向，Cartan 是完成者。用"纠正""补充""完成"，而非"推翻""废除"。 |
| **Cartan–Killing 形式** | 这个名字是后来人命名的。Cartan 本人称它为"Killing 形式"——这个历史细节体现了他对 Killing 的尊重。可以提及这一点来展现人格。 |
| **与 Einstein 的关系** | Cartan 和 Einstein 在 1929-32 年间有通信，讨论统一场论。但不要夸大他们是"合作者"或"亲密朋友"。这是两位巨人之间的一种数学对话。 |
| **Weyl 的引语** | "读 Cartan 的论文像是在丛林中跋涉"——这是 Weyl 在 1949 年写的一句著名评价。可以引用，但要确认原文措辞。不确定就用"据 Weyl 日后评价"。 |
| **"现代微分几何之父"** | 这个称号也被用于陈省身。要区分：Cartan 是"现代微分几何语言的奠基者"，陈省身是"整体微分几何之父"。两者不矛盾，而是师徒传承。 |
| **Cartan 联络 vs Ehresmann 联络** | Cartan 发展了联络的概念（1920s），但现代纤维丛上的联络概念是由 Ehresmann（他的学生）在 1950s 系统化的。不要让读者误以为 Cartan 发明了全部的现代联络理论。 |
| **外微分的先驱** | Grassmann 在 1844 年引入了外代数的基本思想。Cartan 不是外代数的发明者，而是将其发展为现代微分几何的核心语言的人。 |
| **父与子** | Henri Cartan 确实是 Bourbaki 的创始成员之一。但不要把两人放在同一叙事线上——他们的数学风格和数学方向完全不同。Élie 深度探索，Henri 系统建造。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Cartan subalgebra | Cartan 子代数 | 不要与"Cartan 代数"混淆 |
| Cartan–Killing form | Cartan–Killing 形式 | 也称为"Killing 形式"的推广 |
| Cartan connection | Cartan 联络 | 区分于 Ehresmann 联络 |
| exterior differential forms | 外微分形式 | Cartan 不是发明者，是系统化者 |
| repère mobile | 活动标架法 | 法文原词，"mobile"不是"移动"而是"活动的" |
| Pfaffian forms | Pfaff 形式 | 由 Pfaff 提出，Cartan 将其系统化 |
| symmetric spaces | 对称空间 | Cartan 做了完整的分类 |
| simple Lie algebras | 单李代数 | 区分"半单 (semisimple)" 和"单 (simple)" |
| Maurer–Cartan form | Maurer–Cartan 形式 | 李群上自然的 1-形式 |
| spinors | 旋量 | Cartan 在 1913 年独立发现，早于物理学家 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一次/第一个"断言** | "第一次发明了外微分" — 改为"将外微分发展为现代微分几何的核心语言" |
| **"孤独天才"叙事过度** | 不暗示 Cartan 是"被数学界遗弃的"——他有正常的学术升迁、当选院士、有学生 |
| **伪引语** | Cartan 著作中的名言大多是法语，中文引号需格外小心。不确定就间接转述 |
| **年份精确性** | 对称空间分类 (1926-1935) 是一个持续的过程，不是"1926 年完成" |
| **人物时间线** | Ehresmann 是 Cartan 的学生，但纤维丛的工作在 1950s 才成熟。不要暗示 Cartan 活着时纤维丛就是成熟理论 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

> **核心原则：Beamer 写完后，必须回到本地 Wikipedia 存档（page.md + metadata.json），逐项对照审核。**

### 终审执行流程

```
1. 打开 pages/Elie_Cartan/page.md，从头到尾逐段阅读全文
2. 同时打开 Elie_Cartan_zh.tex 源码，逐页对照
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
| 8 | **人物关系** | metadata.json 与 Beamer 一致 | 把"合作者"写成"学生" |
| 9 | **荣誉/获奖** | metadata.json 与封面页一致 | 遗漏重大奖项 |
| 10 | **出版年份** | Wikipedia 书目栏与 Beamer 一致 | 初版与再版混淆 |

### 优先级定义

| 优先级 | 定义 | 潜在案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | 博士论文年份标错、遗漏关键任职机构、人物关系写错 |
| 🟡 P1 | **来源存疑/模糊** | 无法验证的引语、模糊的年份表述 |
| 🟢 P2 | **重要遗漏** | 未提及的标志性著作、可选轶事 |
| ⚪ P3 | **可选补充** | 冷门趣闻、衍生影响 |

### ⚠️ Cartan 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **博士论文年份** | 1894，需确认 | page.md 搜索 "thesis" 或 "1894" |
| **任职机构时间线** | 蒙彼利埃(1894-1896讲师)→里昂(1896-1903讲师)→南锡(1903起教授)→巴黎(1909讲师,1912教授)，每个阶段时长容易搞错 | page.md 搜索 "Montpellier" "Lyon" "Nancy" "professor" |
| **Cartan 子代数的发表年份** | 1913 年核心论文 | page.md 搜索 "Cartan subalgebra" |
| **对称空间分类** | 1926-1935，不是单一论文 | page.md 搜索 "symmetric spaces" |
| **Royal Society 年份** | Wikipedia 为 1947，容易误写为 1937（与 Lobachevsky Prize 年份混淆） | page.md 搜索 "Royal Society" 或 infobox |
| **陈省身师从年代** | 1936，在巴黎做博士后 | page.md 搜索 "Chern" |
| **Weyl 的"丛林"评价** | Cartan 死于 1951，**不可写成"1949 年讣告"**！该引语来自 Weyl 晚年对 Cartan 著作的评述文章 | page.md 搜索 "jungle" 或 "Weyl" |
| **与 Einstein 通信** | 1929-1932 | page.md 搜索 "Einstein" |
| **旋量 (spinors) 发现** | 1913 年，Cartan 独立发现，后成为量子力学核心工具，极易被遗漏 | page.md 搜索 "spinor" |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

嘉当的气质：**孤独的建筑师、被忽视三十年的巨人、安静的法兰西教授** — 沉稳、深沉、被重新发现的珍贵。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 沉稳纪录片风，被忽视 30 年后重新发现——恰好是 Cartan 的一生 |
| ★★★ | Expedition | alex-productions | `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` | 探索史诗，一个人开辟半个微分几何的孤独远征 |
| ★★ | With Me | alex-productions | `music_audio/alex-productions/06-Zd8WsELqFkw-With Me.wav` | 温和怀旧，Cartan 安静的巴黎教授生涯 |
| ★ | Fleeting Moments | inspiring-electronic | `music_audio/inspiring-electronic/` | 电子质感，对称空间的结构之美 |

**操作**：复制选定的 `.wav` 到 `Elie_Cartan/` 目录，`make video` 自动混入。

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Cartan 的独特性在于"孤独"——不是被遗弃，而是在大多数人理解不到的高度独自工作
> 2. 他的"不可读"不是因为写得差，而是因为他在所有人理解之前创造了新的数学语言
> 3. 陈省身的师承关系是展现 "孤独巨人的晚期回报" 的核心叙事
> 4. 父与子（Élie → Henri）是数学史上最美好的传承之一，值得一个独立 slide
> 5. Weyl 的"丛林"评语是整部演示文稿最动人的引言。**但 Cartan 死于 1951，不能写成"1949 年讣告"！**
> 6. 结尾主题句：**他一个人，在丛林里开辟了半个微分几何。**
> 7. 与已有数学家配色必须完全不同——法兰西深蓝 + 几何金是全新的组合
> 8. **⚠️ Royal Society 外籍院士是 1947 年，不是 1937 年（1937 是 Lobachevsky Prize）**
> 9. **⚠️ 职业生涯时间线务必核实：蒙彼利埃仅 2 年(1894-1896 讲师)→里昂 7 年(1896-1903 讲师)→南锡(1903 教授)→巴黎(1909 讲师,1912 教授)**
