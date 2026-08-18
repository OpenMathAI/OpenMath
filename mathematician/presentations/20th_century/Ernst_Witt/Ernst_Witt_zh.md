# 维特 (Ernst Witt) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, milnor, morse, zariski, whitney, chevalley, hopf, chern, deligne 的版式。

---

## 背景信息

- **目标**: Ernst Witt (1911–1991)
- **气质关键词**: **二次型的代数大师、Witt 环与 Witt 向量的创造者、纳粹时期的沉默数学家、PBW 定理的 W**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Ernst_Witt/`

## 第 0 步：Wikipedia 校验

- **全名**：Ernst Witt
- **生卒**：1911-06-26 ~ 1991-07-03，享年 80 岁
- **国籍**：德国（包括纳粹德国时期）
- **出生地**：Alsen (Als Island), German Empire（今丹麦领土）
- **去世地**：Hamburg, Germany
- **博士导师**：**Gustav Herglotz**（哥廷根大学，1933）⚠️ 原提示词错误——Noether 只建议了博士论文题目，正式导师是 Herglotz！论文题目："Riemann-Rochscher Satz und Z-Funktion im Hyperkomplexen"
- **教育**：Freiburg → Göttingen
- **任职**：汉堡大学 (1937–1979)
- **荣誉**：—
- **政治身份**：**纳粹党员**（NSDAP, 1933 年入党），**活跃党员**（不是名义成员！）。二战期间在 OKW/Chi（德军最高统帅部密码局）工作——纳粹的密码破译单位。
- **童年**：父母是传教士，出生后不久全家移居中国。9 岁才回到欧洲。
- **学生**：Günter Harder, Ina Kersten, Walter Borho, Bernhard Banaschewski
- **Leech 格**：Witt 声称他在 1940 年就发现了 Leech 格（比 Leech 早 25 年），但从未发表。真相不明。

### 时间线
- 1911-06-26: 生于 Alsen (Als Island)，时为德意志帝国领土
- 1912: 全家移居中国——父母为传教士。在中国度过童年。
- 1920: 9 岁返回欧洲。
- 1930s: Freiburg → Göttingen 大学学习
- 1933: **加入纳粹党 (NSDAP)**——活跃成员，不是随大流的名义入党
- 1933: Göttingen 博士。导师 **Gustav Herglotz**。论文题目由 Emmy Noether 建议：超复数中的 Riemann-Roch 定理与 ζ 函数
- 1933: Noether 被纳粹驱逐出 Göttingen。Witt 保持沉默——没有公开抗议。
- 1936: Habilitation（授课资格论文），导师 Helmut Hasse
- 1936: 发明 Witt 向量——p-adic 理论的核心工具
- 1937: 发明 Witt 环——二次型的代数分类理论
- 1937: 任汉堡大学讲师
- 1937: Poincaré–Birkhoff–Witt 定理——李代数的基本定理（与 Birkhoff 独立发现）
- 1939–1945: 二战期间在 OKW/Chi 密码部门工作——与 Teichmüller, Aumann 等人一起破译密码
- 1940: Witt 声称发现了 Leech 格（24 维球堆积的最优格）——比 Leech (1965) 早 25 年
- 1950s: 继续发展二次型理论、李代数
- 1979: 从汉堡大学退休
- 1991-07-03: 在汉堡去世

### 人格画像
Witt 是 20 世纪数学中最令人不安的天才之一。他的数学是纯粹的、优雅的、影响深远的——Witt 环、Witt 向量、Witt 代数、PBW 定理——每一个都是代数的基础。但他同时是一个**活跃的纳粹党员**。1933 年纳粹一上台他就入党——不是随大流，是积极的。他在 OKW/Chi 为纳粹战争机器做密码破译。当 Noether 被驱逐出 Göttingen 时，他保持了沉默。他的故事提出了一个痛苦的数学史问题：伟大的数学和罪恶的政治可以共存于同一个人身上吗？本幻灯片不应美化也不应过度审判——而是呈现事实，让观众自己思考。

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_witt_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q68559` | ⚠️ 待核 |
| 2 | `people` | name_zh | `恩斯特·维特` | ⚠️ NULL |
| 3 | `people` | name_variants | `["Witt 向量之父","Witt 代数","Poincaré-Birkhoff-Witt 定理"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1911-06-26` / `1991-07-03` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `German mathematician (1911–1991)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `mathematics`、`algebra` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | metadata 无获奖记录（据实为准） | ⚠️ 待核 |
| 10 | `person_institution` | 教育/任职 | `education: Göttingen、Freiburg`；`employment: Hamburg、Göttingen、Wehrmacht` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `Germany`、`Nazi Germany` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（7 条） | ⚠️ 仅 1 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_witt_relations.py` 补足。

**入库范围（7 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Emmy Noether → Witt | 有向 | ✅ 在库（id=4） |
| 导师 | Gustav Herglotz → Witt | 有向 | ✅ 在库（id=403，正式博士导师） |
| 学生 | Witt → Günter Harder | 有向 | ⚠️ 占位 |
| 学生 | Witt → Bernhard Banaschewski | 有向 | ⚠️ 占位 |
| 学生 | Witt → Horst Leptin | 有向 | ⚠️ 占位 |
| 同事 | Emil Artin | 无向 | ✅ 在库（id=13，汉堡学派） |
| 同事 | Helmut Hasse | 无向 | ⚠️ 占位 |

- 缺失人物（4 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 二次型 | **Witt 环** —— 任意域上二次型的代数分类 | 1937 |
| 数论 | **Witt 向量** —— p-adic 理论的构造工具 | 1936 |
| 李代数 | **Witt 代数** —— 单李代数的一族 | 1930s |
| 李代数 | **Poincaré–Birkhoff–Witt 定理** | 1937 |
| 二次型 | **Witt 消去定理** —— 二次型的结构性定理 | 1937 |
| 代数几何 | **Hasse–Witt 矩阵** —— 有限域上曲线的 p-覆盖 | 1930s |
| 集合论 | **Bourbaki–Witt 定理** —— 不动点定理 | 1950s |
| 组合学 | **Witt 设计** —— 对称设计 | 1938 |
| 球堆积 | **Leech 格** —— 声称 1940 年发现（未发表） | 1940 |

### ★ 叙事主线
1. **Witt 环：二次型的代数之家** — 在 Witt 之前，二次型是分类的混乱世界。Witt 定义了二次型的"环"——通过"Witt 消去"，每个二次型有一个唯一的等价类。这是他最深刻的工作。
2. **Witt 向量：p-adic 理论的心脏** — 从特征 p 出发构造特征 0 的完备赋值环。这是从有限域构造 p-adic 数的标准方法。在现代数论中无处不在——从 p-adic Hodge 理论到 crystalline 上同调。
3. **Poincaré–Birkhoff–Witt 定理** — 李代数的包络代数的基定理。每一个李代数都可以线性化。这是李理论的基本定理——Witt 是其中的 W。
4. **纳粹阴影下的天才** — 积极纳粹党员。OKW/Chi 密码破译员。当 Noether 被驱逐时保持了沉默。他的数学是美丽的，但他的政治选择是令人不安的。如实呈现——不美化，不过度审判。
5. **中国童年** — 父母是传教士，在中国度过人生最初的九年。这个跨文化背景几乎从未在数学史讨论中被提及。
6. **Leech 格的幽灵** — 他在 1940 年就发现了 24 维空间中最优的球堆积方式——但从未发表。25 年后 Leech 重新发现并发表了它。这是否是真的？数学史学家至今争论不休。

## ⚠️ 史实陷阱
- **博士导师** — **不是 Noether！** Noether 只建议了论文题目。正式导师是 Gustav Herglotz。原提示词错误。
- **纳粹身份** — 是**活跃党员**（1933 入党），不只是名义上的。在 OKW/Chi 工作——纳粹密码破译单位。不要在幻灯片中美化或辩护。如实呈现。
- **Noether 驱逐** — Noether 1933 年被纳粹驱逐后，Witt 没有公开说过任何话。这是一个历史事实——毋需渲染。
- **Witt 向量 ≠ Witt 环** — 两个完全不同的概念。Witt 向量是 p-adic 构造，Witt 环是二次型分类。
- **PBW 定理** — Poincaré–Birkhoff–Witt。Witt 和 Birkhoff 在 1937 年独立证明。Poincaré 在 1900 年发现了部分结果。W 是最后一个字母。
- **Leech 格声明** — 1970 年代 Witt 声称他在 1940 年就发现了 Leech 格。学术界一般认为可能属实但无法完全确认——因为他没有留下任何手稿或笔记。用"声称"而非"证明"。

## ⚠️ 终审高危
| 高危点 | 正确值 | 常见错误 |
|--------|--------|----------|
| 博士导师 | Gustav Herglotz (Noether 仅建议题目) | Noether 是导师 |
| 纳粹身份 | 活跃党员, OKW/Chi 密码破译员 | 弱化为"战时服役" |
| 中国童年 | 1912–1920 在中国 | 遗漏 |
| Witt 环 año | 1937 | 1936 |
| Witt 向量 año | 1936 | 1937 |
| PBW | 1937, 与 Birkhoff 独立 | 独自证明 |
| Leech 格 | "声称"1940 发现, 未发表 | 确凿 |

## 配色：丹麦灰蓝 + 德国深灰 + 代数酒红 + 银灰
- **badgeRing** (Witt 环/二次型) — 丹麦灰蓝 `#2C4A6B`
- **badgeVector** (Witt 向量/数论) — 酒红 `#722F37`
- **badgeLie** (李代数/PBW) — 德国深灰 `#1F2937`
- **badgeLegacy** (遗产) — 银灰 `#A8A8A8`
- **coveraccent** — 丹麦灰蓝 `#2C4A6B`
- **coverprimary** — 墨色 `#111827`
- **bgmain** — 暖象牙白 `RGB{248,246,243}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
使用 `\openmathslide`

### 1. 封面 — 《维特：二次型的代数大师》
- 大标题：恩斯特·维特
- 副标题：Ernst Witt · 1911 — 1991
- 标签：Witt 环 · Witt 向量 · PBW 定理 · 二次型
- 底部：汉堡大学 1937-79 · Witt 环 1937 · Witt 向量 1936
- 顶部右侧：头像（如可用）

### 2. Hook — 二次型的代数之家
- 四个面板：(1) Witt 环——任意域上二次型的代数分类 (2) Witt 向量——p-adic 理论的核心构造 (3) PBW 定理——李代数包络代数的基 (4) Noether 的沉默学生——天才与道德的两难
- 底部金句："他给了二次型一个代数之家——但他的道德选择让后人永远无法只看他的数学。"

### 3. 早年：中国→德国 (1911–1930)
- **1911** · 生于 Alsen 岛（时为德意志帝国，今属丹麦）。父母为路德宗传教士。
- **1912** · 全家移居中国传教。Witt 在中国度过了人生的前九年——一个几乎从未被讨论的跨文化童年。
- **1920** · 9 岁回到欧洲。Freiburg → Göttingen 求学。
- 底部金句："生于丹麦海岸，长于中国内陆——一个注定不凡的童年。"

### 4. 博士与 Noether (1931–1933)
- **Göttingen** · 在哥廷根大学学习。论文题目由 **Emmy Noether 建议**——超复数中的 Riemann-Roch 定理与 ζ 函数。但正式博士导师是 **Gustav Herglotz**。
- **1933** · 博士毕业。同年 Noether 因犹太血统被纳粹驱逐出 Göttingen。Witt **保持了沉默**——没有公开抗议，没有辞职抗议。
- **1933** · 加入 NSDAP（纳粹党）——**活跃成员**。
- 底部金句："Noether 给了他的博士论文一个题目，纳粹夺走了他的导师。他选择了沉默。"

### 5. Witt 环 (1937) — 二次型的代数之家
- **Witt 消去定理**：如果两个二次型加同一个二次型后等价，则它们等价。这是二次型理论的基石。
- **Witt 环**：所有非退化二次型的等价类构成一个交换环。加法 = 直和，乘法 = 张量积。Witt 环是域的不变量——刻画了该域上所有可能的二次型结构。
- **意义**：从"分类每一个二次型"转变为"理解二次型的代数结构"。这体现了代数思维的最高境界。
- 底部金句："在 Witt 之前，二次型是一个一个的分类问题。在 Witt 之后，二次型有了自己的代数。"

### 6. Witt 向量 (1936) — p-adic 世界的建造工具
- **问题**：如何从特征 p 的有限域出发，构造特征 0 的完备离散赋值环？
- **Witt 的构造**：对于任意素数 p，Witt 向量 $W(\mathbb{F}_p)$ 给出 p-adic 整数环 $\mathbb{Z}_p$。这是从有限域到 p-adic 数的标准桥梁。
- **应用**：p-adic Hodge 理论、crystalline 上同调、Serre 的局部类域论——Witt 向量是现代数论的基础语言。
- 底部金句："从有限域出发，他用 Witt 向量建造了 p-adic 数的世界。这是数学构造力量的最美展示。"

### 7. 二次型专题：Witt 定理与 Witt 设计
- **Witt 定理 (1937)**：给定向量空间上的二次型，任何两个子空间之间的等距映射都可以扩展为全空间的等距映射。这是二次型理论的"刚性"定理。
- **Witt 设计 (1938)**：5-(12,6,1) 设计——具有极大对称性的组合结构。与 Mathieu 群 M12 相关联。组合学中最重要的设计之一。
- 底部金句："一个定理让二次型变得刚硬——一个设计让对称变得可见。"

### 8. Poincaré–Birkhoff–Witt 定理 (1937)
- **定理**：李代数的泛包络代数具有基 $\{x_1^{e_1} \cdots x_n^{e_n}\}$，其中 $\{x_i\}$ 是李代数的有序基。
- **意义**：李代数可以"线性化"为结合代数。这是李理论中最基本的定理——从李代数的表示到量子群，一切都从 PBW 开始。
- **历史**：Poincaré (1900) 发现部分结果。Birkhoff 和 Witt 在 1937 年独立给出完整证明。W 是最后一个字母——也是最简洁的证明。
- 底部金句："Poincaré 猜想它，Birkhoff 证明了它，Witt 让它变得如此简单——以至于我们现在称之为 PBW。"

### 9. OKW/Chi：纳粹密码破译员 (1939–1945)
- **OKW/Chi**：德军最高统帅部密码局 (Cipher Department of the High Command of the Wehrmacht)。Witt 被 Wilhelm Fenner 招募，与 Teichmüller, Aumann, Aigner 一起组成了数学研究部门的核心。
- **工作内容**：密码分析和密码设计。他的代数专长很可能被用于设计或破解代数密码系统。
- **历史评价**：这是数学史的一个黑暗角落。Witt 的数学才能被用于服务纳粹战争机器。他在 OKW/Chi 的具体贡献因保密而不完全清楚。
- 底部金句："他的代数天才被用于密码破译——不是为了保护，而是为了毁灭。这是数学史上一个沉重的现实。"

### 10. 汉堡大学三十年 (1937–1979)
- **1937** · 获讲师资格（Habilitation），导师 Helmut Hasse。同年入职汉堡大学。
- **战后** · 继续在汉堡大学任教。培养了一批德国代数家：Günter Harder, Ina Kersten, Walter Borho 等。
- **教学风格** · 以清晰和严格著称。在汉堡大学建立了强大的代数研究传统。
- **1979** · 退休。42 年在同一所大学——汉堡大学因为 Witt 成为了代数研究的重镇。
- 底部金句："他在同一间办公室里坐了 42 年——汉堡大学因为 Witt 成为了代数的圣地。"

### 11. Leech 格的幽灵 (1940 / 1970)
- **1970 年代** · Witt 声称他在 1940 年就发现了 Leech 格——24 维空间中球堆积的最优格。Leech 在 1965 年发表了这个格。
- **Leech 格**：24 维空间中最密集的球堆积方式。与 Golay 码、Mathieu 群 M24、魔群月光 moonshine 相关联。它是数学和物理中最迷人的结构之一。
- **真相？** · Witt 确实留下了一些笔记。学界一般认为他可能确实独立发现了这个格——但因为没有发表，荣誉归于 Leech。这个故事提醒我们：发表很重要。
- 底部金句："他在 1940 年就看见了 Leech 格——但战争让他沉默了。25 年后，荣誉归于另一个人。"

### 12. Bourbaki–Witt 定理与其他
- **Bourbaki–Witt 定理**：完备偏序集上任意保序映射的不动点定理。被 Bourbaki 在《集合论》卷中使用——以 Witt 命名。集合论和计算机科学中的基本工具。
- **Hasse–Witt 矩阵**：有限域上代数曲线的半线性 Frobenius 作用的矩阵。决定曲线的 p-秩。现代算术几何中的关键不变量。
- **Witt 代数**：单李代数的一族。Witt 代数是多项式环上导子李代数——与 Virasoro 代数有深刻联系。
- 底部金句："从集合论的不动点定理到有限域的几何——Witt 的触角伸向了代数的每一个角落。"

### 13. 沉默的代价：天才与道德
- **一个不可回避的问题**：Witt 是伟大的数学家，也是纳粹政权的积极参与者。他利用数学为战争服务，对同事的遭遇保持沉默。
- **Noether 的沉默**：1933 年 Noether 被驱逐。Witt 保持了沉默。不是因为他不能抗议——他选择了不抗议。
- **数学与道德**：我们可以欣赏 Witt 的数学而不认可他的政治选择吗？数学之美是否可以脱离数学家的道德？这个幻灯片不提供答案——只呈现问题。
- 底部金句："他的数学是纯粹的美。他的选择是沉重的历史。两者都不可否认——两者都必须面对。"

### 14. 遗产：以 Witt 命名的概念
- **Witt 环** — 二次型的代数分类
- **Witt 向量** — p-adic 理论的核心工具
- **Poincaré–Birkhoff–Witt 定理** — 李代数基本定理
- **Witt 代数** — 单李代数的一族
- **Witt 消去定理** — 二次型刚性定理
- **Witt 设计** — 5-(12,6,1) 设计
- **Bourbaki–Witt 定理** — 不动点定理
- **Hasse–Witt 矩阵** — 算术几何
- **Witt 群** — 二次型的 K-理论
- 底部金句："以他命名的概念超过十个——从二次型到李代数，从 p-adic 数到有限域几何——他的名字是代数本身的语言。"

### 15. 结束页
- 大引语："Jedes quadratische Form hat eine Heimat."（每一个二次型都有一个家。）
- 小字：恩斯特·维特 · Ernst Witt · 1911 — 1991
- 底部：Witt 环的创造者 · PBW 的 W · 汉堡大学 42 年

## 音乐: Tragedy + Timeless

## Round 2 高危: 博士导师 Herglotz (非 Noether)、纳粹活跃党员+OKW/Chi、中国童年、Leech 格"声称"、PBW 归属三人。

> **开始执行。**
