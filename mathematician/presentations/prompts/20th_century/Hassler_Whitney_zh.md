# 惠特尼 (Hassler Whitney) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, milnor, morse, zariski 的版式。

---

## 背景信息

- **目标**: Hassler Whitney (1907–1989)
- **气质关键词**: **微分拓扑的开山鼻祖、嵌入定理之父、Stiefel–Whitney 特征类、从音乐/登山到数学的全才**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Hassler_Whitney/`

## 第 0 步：Wikipedia 校验

- **全名**：Hassler Whitney（无中间名）
- **生卒**：1907-03-23 ~ 1989-05-10，享年 82 岁
- **国籍**：美国
- **出生地**：New York City, USA
- **去世地**：Princeton, New Jersey, USA（中风）
- **博士导师**：George David Birkhoff（哈佛大学）
- **博士论文**：1932，《The Coloring of Graphs》（图着色理论，非拓扑！）
- **教育**：Yale (BA physics 1928, BM music 1929), Harvard (PhD 1932)
- **任职**：哈佛 (1930–1952)、IAS 普林斯顿 (1952–1977)、NSF 数学委员会主席 (1953–56)
- **荣誉**：Wolf 奖 (1982)、美国国家科学奖章 (1976)、Steele 奖 (1985)、Lester R. Ford 奖 (1969)
- **学生**：Herbert Robbins, Paul Olum, James Eells, Wilfred Kaplan（注意：John Nash 不是他的博士生，Nash 的导师是 Albert Tucker）
- **家庭**：Whitney-Dwight-Sherman 世家。父 Edward Baldwin Whitney（纽约最高法院法官），母 Josepha Newcomb Whitney（艺术家），外祖父 Simon Newcomb（天文学家+数学家），高祖父 Roger Sherman（美国开国元勋），叔祖 Josiah Whitney（首测 Mount Whitney），祖父 William Dwight Whitney（耶鲁梵语教授）
- **骨灰**：按遗愿撒在瑞士 Dent Blanche 山顶 (1989-08-20)

### 时间线
- 1907-03-23: 生于纽约市，学术世家
- 1928: Yale 物理学学士
- 1929: Yale 音乐学士（小提琴/中提琴）——同年与堂弟 Bradley Gilman 首攀 Cannon Mountain 的 Whitney–Gilman 山脊，成为美东最著名的攀岩路线
- 1930–1932: 哈佛数学博士，导师 Birkhoff，论文《图的着色》
- 1930–1940s: 从图论转向拓扑——1933 年奠定拟阵(matroid)理论、1935 年引入 Stiefel–Whitney 类、1936 年证明嵌入定理
- 1936: 发表嵌入定理：任何光滑 n 维流形可嵌入 R^{2n+1}，可浸入 R^{2n}
- 1940s: 发展上同调理论——cup product（Whitney 挠积），Whitney 扩张定理。二战期间在 NDRC 工作
- 1944: Whitney trick 将嵌入维数降至 R^{2n}（n>2）
- 1950s: 奇点理论——Whitney 条件 A & B（分层理论），Whitney 折叠与尖点（fold/cusp）
- 1952: 加入 IAS 普林斯顿
- 1957: 出版《几何积分理论》——带奇点的 Stokes 定理理论基础
- 1960s-1970s: 转向数学教育——在小学教数学，倡导消除"数学焦虑"，认为数学应联系生活而非死记硬背
- 1976: 获美国国家科学奖章
- 1979–1982: 国际数学教育委员会 (ICMI) 主席
- 1982: 获 Wolf 数学奖
- 1985: 获 Steele 奖
- 1989-05-10: 在普林斯顿去世，中风。骨灰撒在瑞士 Dent Blanche 山顶

### 人格画像
Whitney 是一个文艺复兴式的全才：物理学家、音乐家（小提琴和中提琴，在普林斯顿业余乐团演奏）、登山家（瑞士阿尔卑斯俱乐部成员，攀登瑞士大多数山峰）。他的学术世家背景深厚——外祖父 Simon Newcomb 是著名天文学家和数学家，高祖父 Roger Sherman 是美国开国元勋。他的学术跨度惊人：从图论到微分拓扑，从奇点理论到数学教育。晚年他全心投入小学数学教育改革，认为数学教育应该消除恐惧、联系生活。Chen Ning Yang（杨振宁）曾回忆，Whitney 在 IAS 是"最原创的数学家之一"。René Thom 说 Whitney 是"奇点理论真正的奠基人"。

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_whitney_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q742072` | ⚠️ 待核 |
| 2 | `people` | name_zh | `哈斯勒·惠特尼` | ⚠️ NULL |
| 3 | `people` | name_variants | `["嵌入定理之王","微分流形的拼图大师","惠特尼嵌入定理"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1907-03-23` / `1989-05-10` | ⚠️ 仅年份 |
| 6 | `people` | description | `American mathematician (1907–1989)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `topology`、`graph theory`、`singularity theory`、`matroid theory`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `NMS 1976`、`Wolf 1982`（已有）、`Steele 1985`、`Ford Award` | ⚠️ 部分 |
| 10 | `person_institution` | 教育/任职 | `education: Harvard、Yale`；`employment: Harvard、IAS、Applied Mathematics Panel` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `United States` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（6 条） | ⚠️ 全空 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_whitney_relations.py`。

**入库范围（6 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | George David Birkhoff → Whitney | 有向 | ⚠️ 占位（与 Morse 同导师） |
| 学生 | Whitney → Herbert Robbins | 有向 | ⚠️ 占位 |
| 学生 | Whitney → James Eells | 有向 | ⚠️ 占位 |
| 同事 | Marston Morse | 无向 | ✅ 在库（id=25） |
| 同事 | Norman Steenrod | 无向 | ⚠️ 占位（纤维丛，Whitney–Steenrod） |
| 同事 | Saunders Mac Lane | 无向 | ✅ 在库（id=39） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 微分拓扑 | **Whitney 嵌入定理** — n 流形可嵌入 R^{2n} | 1936/1944 |
| 微分拓扑 | **Whitney 浸入定理** — n 流形可浸入 R^{2n-1} | 1936 |
| 拓扑学 | **Stiefel–Whitney 特征类**（与 Stiefel 独立） | 1935 |
| 代数拓扑 | **Cup product（上同调积）** | 1940s |
| 奇点理论 | **Whitney 条件 A & B** — 分层理论基础 | 1950s |
| 奇点理论 | **Whitney 折叠与尖点 (fold/cusp)** | 1955 |
| 几何测度 | **几何积分理论** — Stokes 定理的奇点推广 | 1957 |
| 图论 | **图着色、拟阵 (matroid) 理论基础** | 1930–1933 |
| 分析 | **Whitney 扩张定理** | 1934 |
| 拓扑 | **Whitney trick** — 高维拓扑关键工具 | 1944 |

### ★ 叙事主线
1. **"任何流形都可以放入某个 R^n"** — 嵌入定理是微分拓扑最根本的定理。它回答了一个基本问题：我们能否把抽象的流形"可视化"？
2. **小提琴手·登山家·数学家** — Yale 的物理+音乐双学士，首攀以他命名的山脊。这是一个文艺复兴式的天才。晚年骨灰撒在瑞士 Dent Blanche 山顶——这是他精神的最终归宿。
3. **从图的着色到流形的嵌入** — 博士论文是图论（四色问题的先驱贡献），1930s 转向拓扑。这种跨度本身就令人惊叹。
4. **特征类的先驱** — Stiefel–Whitney 类是第一个特征类（模 2 系数），开启了一个全新的领域。Chern 类、Pontryagin 类都是其后继者。
5. **奇点理论的开山鼻祖** — Ren é Thom 说 Whitney 是奇点理论真正的奠基人。Whitney 条件 A & B 定义了"好的"分层空间。Fold 和 cusp 是光滑映射奇点的基本分类。
6. **晚年：数学教育的革命者** — 从 IAS 退休后，Whitney 走进小学教室教数学。他反对死记硬背，主张消除"数学焦虑"。1979–1982 年担任国际数学教育委员会主席。

## ⚠️ 史实陷阱
- **嵌入定理的精确维数** — 1936 年：嵌入 R^{2n+1}，浸入 R^{2n}。1944 年用 Whitney trick 改善为嵌入 R^{2n}（n>2）。**不是 R^{n+1}**！这是许多人常犯的错误。
- **Stiefel–Whitney 类的归属** — Eduard Stiefel（瑞士 ETH）在 1935 年独立发现了同样的特征类（整数系数）。Whitney 给出了模 2 版本。后来两者合并称为 Stiefel–Whitney 类。Whitney 在 1937 年论文中承认了 Stiefel 的优先贡献。
- **博士论文方向** — 图论（图的着色），不是拓扑！这是 Whitney 学术生涯最令人惊讶的事实。他的图论工作后来奠定了拟阵(matroid)理论的基础。
- **John Nash 的师徒关系** — **John Nash 不是 Whitney 的博士生**。Nash 的博士导师是 Albert W. Tucker。Whitney 与 Nash 同在普林斯顿，但无导师关系。原始 prompt 错误。
- **Whitney 扩张定理** — 解决了"闭子集上的光滑函数能否扩张到全空间"的问题，完整解答直到 2005 年才由 Charles Fefferman 给出。
- **Whitney umbrella (惠特尼伞)** — 这是一种奇点类型（x^2 = y z^2），不是 Whitney 本人命名，而是后来以他命名的标准奇点模型。

## ⚠️ 终审高危
| 高危点 | 正确值 | 常见错误 |
|--------|--------|----------|
| 嵌入维数 | R^{2n} (n>2) | R^{n+1} |
| 博士论文 | 图着色 (1932) | 拓扑 |
| Stiefel–Whitney | 与 Stiefel 独立 | Whitney 单独 |
| John Nash 关系 | 非博士生 (Tucker 是导师) | 师从 Whitney |
| Yale 学位 | BA physics + BM music | 只学数学 |
| 骨灰 | Dent Blanche, 瑞士 | 无记载 |

## 配色：Yale 蓝 + 深雪白 + 墨黑 + 暖铜
- **badgeEmbed** (嵌入) — Yale 蓝 `#00356B`
- **badgeClass** (特征类) — 深雪白 `#D4D4D4`（需要深色文字）
- **badgeSing** (奇点) — 墨黑 `#1A1A2E`
- **badgeLegacy** (遗产/教育) — 暖铜 `#B87333`
- **coveraccent** — Yale 蓝 `#00356B`
- **coverprimary** — 墨色 `#111827`
- **bgmain** — 暖象牙白 `RGB{248,246,243}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
使用 `\openmathslide`

### 1. 封面 — 《惠特尼：微分拓扑的开山鼻祖》
- 大标题：哈斯勒·惠特尼
- 副标题：Hassler Whitney · 1907 — 1989
- 标签：嵌入定理 · Stiefel–Whitney 类 · 奇点理论 · 几何积分
- 底部：Wolf 奖 1982 · 国家科学奖章 1976 · Steele 奖 1985

### 2. Hook — 弯曲世界中的平坦空间
- 四个面板：(1) 嵌入定理——任何 n 维流形都是某个 R^{2n} 的子集 (2) 特征类——Stiefel–Whitney 类是向量丛的拓扑指纹 (3) 奇点分类——fold/cusp，所有光滑映射奇点的基本构造块 (4) 从图论到数学教育——跨领域的天才
- 底部金句："他证明了：我们永远可以把弯曲的世界放入平坦的空间。"

### 3. 出身与早年：学术世家 + 小提琴 + 登山 (1907–1929)
- **1907** · 生于纽约市。Whitney-Dwight-Sherman 世家：父为法官，母为艺术家。外祖父 Simon Newcomb 是天文学家+数学家。高祖父 Roger Sherman 是美国开国元勋。祖父 William Dwight Whitney 是耶鲁梵语教授。叔祖 Josiah Whitney 首测 Mount Whitney。
- **1928** · Yale 物理学学士。**1929** · Yale 音乐学士（小提琴/中提琴）。
- **1929** · 与堂弟 Bradley Gilman 首攀 Cannon Mountain 的 Whitney–Gilman 山脊——美东最著名的攀岩路线。瑞士阿尔卑斯俱乐部成员。
- 底部金句："物理学训练了他的严谨，音乐训练了他的直觉，登山训练了他的勇气。"

### 4. 图论的开端：从着色到拟阵 (1930–1933)
- **1932** · 哈佛数学博士，导师 Birkhoff。论文《图的着色》——这是 Whitney 的学术起点，与后来的拓扑工作完全不同。
- **1933** · 奠定拟阵(matroid)理论的基础。Whitney 证明了 Whitney 2-同构定理：两个图没有孤立顶点时，它们的拟阵同构当且仅当图是 2-同构的。
- **意义**：拟阵理论现在是组合学和表示论的基础语言。Whitney 和 van der Waerden 在 1930s 中期各自独立引入了拟阵概念。
- 底部金句："博士论文关于图的着色——但在几年之内，他从离散转向了连续，从图转向了流形。"

### 5. 嵌入定理 (1936) — 微分拓扑的基石
- **Whitney 嵌入定理**：任何光滑 n 维流形可嵌入 R^{2n+1} (1936)，后改善为 R^{2n} (n>2) (1944)。
- **Whitney 浸入定理**：任何光滑 n 维流形可浸入 R^{2n-1}。
- **意义**：在此之前，流形的内蕴定义和外蕴定义是分离的。嵌入定理证明了它们是等价的——任何抽象的流形都可以放在欧氏空间里。这为微分拓扑提供了基本框架。
- **Whitney trick (1944)**：通过取消带相反符号的交点，将嵌入维数从 2n+1 降至 2n。这个技巧后来成为高维拓扑的核心工具——Smale 用它证明了高维 Poincaré 猜想。
- 底部金句："流形不必是抽象的。任何光滑流形都是某个 R^{2n} 的子集——这是微分拓扑的第一定理。"

### 6. Stiefel–Whitney 类 (1935) — 第一个特征类
- **发现**：Eduard Stiefel（ETH 苏黎世）和 Whitney 在 1935 年独立发现了向量丛的特征类。Stiefel 给出整数系数版本，Whitney 给出模 2 版本。
- **定义**：Stiefel–Whitney 类 w_i ∈ H^i(M; Z_2) 是向量丛的拓扑不变量——向量丛的"指纹"。w_1 = 0 当且仅当丛可定向；最高类 w_n 是 Euler 类的模 2 约化。
- **意义**：这是第一个被发现的**特征类**，开启了整个领域。Chern 类（陈省身，1946）、Pontryagin 类都是其后继者。Whitney 在 1937 年论文中承认了 Stiefel 的优先贡献。
- 底部金句："特征类的概念由此诞生——向量丛从此有了拓扑指纹。"

### 7. Cup Product 与上同调理论 (1940s)
- **Cup product (Whitney 挠积)**：Whitney 在 1940s 定义了上同调环的乘法结构——cup product ⌣。这是代数拓扑的核心运算。
- **重要性**：上同调比同调多了一个环结构——这使得上同调成为比同调更强大的工具。Poincaré 对偶、特征类、谱序列都依赖 cup product。
- **相关贡献**：Whitney 扩张定理 (1934)——闭子集上的光滑函数能否扩张到全空间？完整解答直到 2005 年由 Charles Fefferman 给出。
- 底部金句："他给上同调装上了乘法——代数拓扑从此有了代数结构。"

### 8. 奇点理论：Fold 与 Cusp (1955)
- **Whitney 折叠 (fold)** 与 **Whitney 尖点 (cusp)**：Whitney 在 1955 年分类了平面到平面的光滑映射的所有稳定奇点——只有两种：fold 和 cusp。
- **Whitney 条件 A & B**：定义了"好的"分层空间(stratified space)。A 条件保证边界沿法向收敛，B 条件保证横截性在极限下保持。
- **影响力**：René Thom 说 Whitney 是奇点理论真正的奠基人。Thom 的突变理论(catastrophe theory)、John Mather 的奇点分类都建立在 Whitney 的工作之上。Whitney umbrella（伞形奇点 x^2 = y z^2）是三维空间中最基本的奇点模型。
- 底部金句："一朵云的形状、一道海浪的破碎——从数学上看，都只是 fold 与 cusp 的组合。"

### 9. 几何积分理论 (1957) — Stokes 定理的终极形式
- **出版**：《Geometric Integration Theory》(1957)，Princeton Mathematical Series。XV+387 页。
- **内容**：为带奇点边界的 Stokes 定理建立理论基础。将微分形式的积分推广到非光滑区域——这是几何测度论的里程碑。
- **后续影响**：Jenny Harrison 在 1990s 的"非光滑链的 Stokes 定理"直接继承了 Whitney 的思路。Federer 的几何测度论巨著也是在同一方向上。
- 底部金句："Stokes 定理的美在于它的简洁——Whitney 让它适用于一切边界，包括那些不光滑的。"

### 10. Whitney trick 与高维拓扑 (1944)
- **Whitney trick**：在高维流形中，可以消除两个子流形的交点。核心技巧是沿着一个圆盘(Whitney disk)滑移，使带相反符号的交点相互抵消。
- **重要性**：这是高维拓扑最基本的技术工具。Smale 用它证明了 n≥5 的广义 Poincaré 猜想(Fields 奖 1966)。Milnor 用它构造异种球面(Fields 奖 1962)。Kervaire-Milnor 用它分类了异种球面。
- **Whitney disk**：两个嵌入子流形之间的二维圆盘，边界一半在一个子流形上，一半在另一个上。如果这样的圆盘存在，交点就可以消除。
- 底部金句："一个简单的技巧——消除交点的圆盘——成为了高维拓扑最强大的武器。"

### 11. IAS 普林斯顿黄金岁月 (1952–1977)
- **1952** · 从哈佛转入 IAS 普林斯顿数学学院。同事：Oppenheimer, von Neumann, Gödel, Weyl, Morse。
- **1953–1956** · 兼任 NSF 数学委员会主席——为美国数学研究奠定制度基础。
- **IAS 时期工作**：几何积分理论 (1957)、奇点理论 (1950s-60s)、复解析簇 (1972)。
- **人格魅力**：杨振宁回忆 Whitney 是"IAS 最原创的数学家之一"。他在普林斯顿业余乐团演奏中提琴，周末攀登瑞士阿尔卑斯山。
- 底部金句："在 IAS 的 25 年——他既是数学家，也是登山家、音乐家、制度构建者。"

### 12. 晚年：数学教育的革命者 (1967–1989)
- **1967** · 全职投入教育问题——在小学教了四个月预代数，为教师举办暑期课程。
- **理念**：消除"数学焦虑"（他发明的术语）。数学教育应该联系学生的生活，而不是死记硬背。他走遍美国和世界各地讲学推广这一理念。
- **1979–1982** · 担任国际数学教育委员会 (ICMI) 主席——将教育理念推向全球。
- **评语**：New York Times 1986 年报道他在小学教室里的工作——《About Education: Learning Math by Thinking》。
- 底部金句："Wolf 奖得主教小学数学——他说孩子们不需要害怕数学，数学就在他们身边。"

### 13. 荣誉满身：Wolf 奖、国家科学奖章、Steele 奖
- **美国国家科学奖章 (1976)**：美国最高科学荣誉。表彰他在微分拓扑、奇点理论、几何积分理论方面的开创性贡献。
- **Wolf 数学奖 (1982)**：与 Mark Krein 共同获奖。表彰他在代数拓扑、微分拓扑和奇点理论方面的基础性贡献。
- **Leroy P. Steele 奖 (1985)**：AMS 终身成就奖——表彰他的论文全集。
- **Lester R. Ford 奖 (1969)**：表彰论文"The Mathematics of Physical Quantities"（物理量的数学）。
- **其他荣誉**：国家科学院院士、美国哲学学会会员、伦敦数学会荣誉会员、瑞士数学会荣誉会员、巴黎科学院外籍院士。
- 底部金句："从国家科学奖章到 Wolf 奖到小学教室——Whitney 证明了数学可以同时是最深刻的科学和最贴近生活的事业。"

### 14. 遗产：那些以 Whitney 命名的概念
列出所有以 Whitney 命名的概念（从 Wikidata notable_work）：
- **Whitney 嵌入定理** — n流形 ⊂ R^{2n}
- **Whitney 浸入定理** — n流形 → R^{2n-1}
- **Stiefel–Whitney 类** — 向量丛的模2特征类
- **Whitney 条件 A & B** — 分层空间
- **Whitney 折叠/尖点** (fold/cusp) — 奇点基本分类
- **Whitney trick** — 高维拓扑核心工具
- **Whitney disk** — 消除交点的圆盘
- **Whitney 扩张定理** — 光滑函数扩张
- **Whitney umbrella** — 基本奇点模型
- **Whitney 不等式 / Loomis–Whitney 不等式** — 几何分析
- **Whitney 覆盖引理** — 测度论
- **Whitney 平面性判据** — 图论
- **Whitney 拓扑** — 函数空间上的拓扑
- **拟阵 (matroid) 理论** — 组合学基础
- 底部金句："以他命名的概念超过十四个——从拓扑到奇点，从测度论到图论——几乎覆盖纯数学的每一个角落。"

### 15. 结束页 — 山巅的骨灰
- 大引语："The abstraction of modern mathematics is not an obstacle but a liberation."
- 配图意境：瑞士 Dent Blanche 山顶——Whitney 骨灰的安息之地。
- 小字：哈斯勒·惠特尼 · Hassler Whitney · 1907 — 1989
- 底部：微分拓扑奠基人 · 奇点理论先驱 · 数学教育的革命者 · 骨灰撒在 Dent Blanche 之巅

## 背景音乐选择 ✅

- **选定曲目**: **Expedition** — Alex-Productions (66k views, 探索/史诗/远征)
- **风格**: 探索 / 史诗 / 远征式叙事
- **匹配理由**:
  - "远征式叙事" 是 Whitney 的生命底色——他本身就是登山家：1929 年与堂弟首攀 Cannon Mountain 的 Whitney–Gilman 山脊（美东最著名攀岩路线），瑞士阿尔卑斯俱乐部成员，攀登了瑞士大多数山峰，骨灰撒在 Dent Blanche 山顶（4357m）。没有哪位数学家的音乐选择比 Whitney 更适合 Expedition——他的骨灰就在阿尔卑斯山巅
  - "探索" 匹配他的学术远征：图论(1932) → 嵌入定理(1936) → Stiefel–Whitney 类(1935) → 奇点分类 fold/cusp(1955) → 几何积分理论(1957) → 数学教育改革(1967-1989)——从离散到连续，从拓扑到教育，跨度无人能及。Yale 物理+音乐双学士，小提琴手，文艺复兴式的全才
  - "史诗" 匹配嵌入定理的革命性：任何 n 维流形都是 R^{2n} 的子集——微分拓扑的第一定理、第一基石。Whitney trick 成为 Smale 证明高维 Poincaré 猜想、Milnor 构造异种球面的核心工具
  - 结尾页直接是"山巅的骨灰——Dent Blanche"——这不是隐喻，而是 Whitney 真实的人生终点。Expedition 的史诗感与之天然呼应
- **备选** (未采用):
  - ★★ Timeless — "沉稳/纪录片/长期纲领" 匹配嵌入定理和 Stiefel–Whitney 类的持久影响，但 Whitney 的气质远非"沉稳"——他是登山家、音乐家、全才，Timeless 太安静
  - ★ Awaken — "鼓舞/明亮" 匹配他的教育改革热情，但受众偏低 (79k) 且过于明亮，无法承载骨灰撒山巅的深沉
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → `presentations/Hassler_Whitney-W/Expedition.wav`
- **时长**: 128 秒 > 17 页 × 7 秒 = 119 秒 → ffmpeg `-shortest` 自动对齐

## Round 2 高危: 嵌入维数 R^{2n} 非 R^{n+1}、John Nash 非其博士生、Stiefel 独立发现、博士论文图着色、Yale 音乐学位、骨灰 Dent Blanche。

> **开始执行。**