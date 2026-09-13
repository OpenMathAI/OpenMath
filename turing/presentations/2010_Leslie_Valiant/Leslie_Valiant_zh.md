# Leslie Valiant（莱斯利·瓦利安特）立传提示词

> qid=Q93154 · 1949-03-28 – 在世留白 · 英国裔美国计算机科学家 · 20/21 世纪 · 2010 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2010/Leslie Valiant/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英裔美国人`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（PAC 学习 / #P 完备 / BSP 模型的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Leslie Gabriel Valiant, FRS（中文惯称：莱斯利·瓦利安特 / 瓦里安）
- **生卒**：1949-03-28 生于布达佩斯（Budapest，匈牙利共和国）→ 在世留白
- **国籍**：英国裔美国人（British American；页面原文 "a British American computer scientist and computational theorist"）
- **身份**：计算机科学家、计算理论家；Harvard University T. Jefferson Coolidge Professor of Computer Science and Applied Mathematics（Harvard SEAS）
- **家庭**：化学工程师之父、翻译家之母（页面原文 "born to a chemical engineer father and a translator mother"）；两个儿子 Gregory Valiant 与 Paul Valiant **均为理论计算机科学家**——可写"一门三理论家"
- **教育轨迹**：
  - King's College, Cambridge（BA）
  - Imperial College London（MS）
  - University of Warwick **计算机科学**博士（1974），论文 *Decision Procedures for Families of Deterministic Pushdown Automata*
- **博士导师**：Mike Paterson（Warwick）
- **研究领域**：理论计算机科学、复杂性理论、计算学习理论、理论神经科学、并行与分布式计算

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **ACM 的评价（可直接引用）**："a heroic figure in theoretical computer science and a role model for his courage and creativity in addressing some of the deepest unsolved problems in science"，以及其 "striking combination of depth and breadth"——"深度与广度的惊人结合"是本篇的叙事主轴。
2. **#P 完备性（1977/1979）**：引入 #P-completeness（"Sharp-P completeness"）解释为什么计数与可靠性问题难解；首个应用是计数匹配（矩阵积和式 permanent）；SIAM J. Comput. 1979 论文 *The Complexity of Enumeration and Reliability Problems*。
3. **PAC 学习（1984）**：论文 *A theory of the learnable*（CACM）提出 Probably Approximately Correct 学习模型，开创**计算学习理论**，成为机器学习发展的理论基础——图灵奖核心理由之一；2013 年出版大众向著作 *Probably Approximately Correct: Nature's Algorithms for Learning and Prospering in a Complex World*。
4. **图灵奖理由（整句引用，核心红线）**："For transformative contributions to the theory of computation, including the theory of probably approximately correct (PAC) learning, the complexity of enumeration and of algebraic computation, and the theory of parallel and distributed computing."——四大关键词：PAC 学习 / 计数与代数计算复杂性 / 并行与分布式计算理论。
5. **BSP 模型（1989）**：Bulk Synchronous Parallel 处理模型——类比单机 von Neumann 模型的并行计算统一模型；Google 以 MapReduce/MillWheel/Pregel/Dataflow 大规模采用，Facebook 用其思想构建处理超 1 万亿边的图分析系统；Hadoop、Spark、Giraph、Hama、Beam、Dask 等开源项目亦有显式 BSP 或衍生模型。
6. **Valiant–Vazirani 定理（1986）**：*NP is as easy as detecting unique solutions*（与 V. Vazirani）——复杂性经典结果。
7. **全息算法（Holographic Algorithms）**：受量子计算模型启发的概念创造。
8. **上下文无关文法最快算法（1975）**：早期工作给出至今仍为渐近最快的上下文无关语言识别算法（Royal Society 提名语："the asymptotically fastest algorithm known for recognising context-free languages"）。
9. **通信复杂性先驱**：同在早期工作（1975 前后）"pioneered the use of communication properties of graphs for analysing computations"（Royal Society 提名词）。
10. **计算神经科学**：关注记忆与学习的理解（theoretical neuroscience），把 PAC 思想延伸到自然界的算法（进化速率论证，见 §5 引语红线）。
11. **荣誉等身**：Nevanlinna Prize 1986、FRS 1991、Knuth Prize 1997、NAS 院士 2001、EATCS Award 2008、Turing Award 2010；1982 年起执教 Harvard，此前任教 CMU/Leeds/Edinburgh。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（计算学习理论 — 蓝） | `#2E5A9E` | PAC 学习 / A theory of the learnable |
| 分类色 2（计数复杂性 — 青绿） | `#1E8E8E` | #P 完备 / 积和式 / Valiant–Vazirani |
| 分类色 3（并行计算 — 琥珀） | `#D9A441` | BSP / 并行与分布式模型 |
| 分类色 4（算法与神经科学 — 玫瑰） | `#C0395B` | 全息算法 / CFL 快速算法 / 计算神经科学 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「大概正确（probably approximately correct）」的概率式视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：沉静 / 深思（理论家的孤独与深邃：PAC、#P、BSP 皆为一人力作）
- **选定曲目**：Alex-Productions **Lonesome**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Leslie_Valiant/Lonesome.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「计算理论英雄 · 英裔美国」+ Valiant 1949– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1949–在世 生平纵览
4. **早年：布达佩斯与英伦求学**（1949–1974）：化工工程师与翻译家之子、Cambridge/Imperial/Warwick
5. **Warwick 博士与下推自动机**（1974）：Paterson 门下、判定程序论文
6. **上下文无关语言的最快算法与通信复杂性**（1975 前后）：Royal Society 提名词双亮点
7. **#P 完备性：计数问题的复杂性**（1977/1979）：积和式、枚举与可靠性问题
8. **Valiant–Vazirani 定理**（1986）：唯一解与 NP
9. **PAC 学习：可学习的理论**（1984）：A theory of the learnable、计算学习理论的诞生
10. **从 PAC 到自然界**（2013 书）：进化的算法视角（引语按 §5 红线处理）
11. **BSP：并行的统一模型**（1989 起）：Google/Facebook/开源生态的现实影响
12. **全息算法与计算神经科学**：受量子启发的算法创造、记忆与学习
13. **荣誉与传承**：Nevanlinna 1986、Knuth 1997、Turing 2010；门生 Jerrum/Kearns/Roth；儿子 Gregory/Paul 亦是理论计算机科学家
14. **遗产**：机器学习的理论基座、并行计算的设计语言
15. **结尾**：在世、"深度与广度的惊人结合"

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由整句引用**：四大关键词（PAC learning / complexity of enumeration and of algebraic computation / parallel and distributed computing）一个都不能漏、勿改写——核心红线。
- **#P 年份口径**：页面两处表述——Royal Society 提名词写 1977 定义 #P-completeness，正文 Known for 与 1979 SIAM 论文为发表载体——写"1977 年提出（1979 年论文发表）"或直接以 Royal Society 口径为准，勿写成两个不同贡献。
- **PAC 论文年份**：*A theory of the learnable* 是 **1984**（CACM 27(11)）——勿与 2013 年书混淆；2013 年书是大众向延伸。
- **Nevanlinna Prize 表述**：1986 年获奖（现为 IMU Abacus Medal 的前身奖项），勿写成"数学三大奖"之类拔高。
- **BSP 影响**：页面说 Google "adopting it for computation at large scale via MapReduce..."——是"采用其思想/模型"，勿写"BSP 是 MapReduce 的实现"；Facebook 的数字是 "over 1 trillion edges"。
- **进化论引语（红线）**：2013 书中关于进化速率的原文引语（"The evidence for Darwin's general schema for evolution being essentially correct is convincing..."）页面有载**可用**，但必须注明出自该书且完整转达"证据可信、现有理论解释力不足"的双面立场——**勿断章成"Valiant 否定进化论"**。
- **在世**：死亡日期留白，生卒写 `1949–`。
- **国籍**：页面原文 "British American"——写"英裔美国人/英美双料"按模板口径统一，勿单写"美国人"。
- **师承**：博士导师 Mike Paterson（Warwick）为 infobox 明载，可写；Cambridge/Imperial 阶段导师无载禁写。
- **引语**：ACM 评价语（heroic figure... / striking combination of depth and breadth）、Royal Society 提名词、2013 书进化段——三处页面有载可引；**本人访谈引语页面未载，勿编造**。
- **家庭**：父亲职业与两个儿子的科学家身份为页面明载可写；其余家庭细节无载禁写。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 莱斯利·瓦利安特 | 待写入 |
| name_en | Leslie Valiant | 待写入 |
| birth_date | 1949-03-28 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United Kingdom / United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computational learning theory / complexity theory / parallel computing / theoretical neuroscience | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Mike Paterson（University of Warwick）
- **合作者**：Vijay Vazirani（Valiant–Vazirani 定理，1986）
- **著名博士生**：Mark Jerrum、Michael Kearns、Dan Roth
- **家族关系（parent-child）**：Gregory Valiant、Paul Valiant（两子，均为理论计算机科学家）
- **页面无载的关系**：禁写（如与 Knuth Prize 前辈学人的私交等）

## 8. 奖项清单

- A.M. Turing Award（2010，citation 见 §2-4）
- Nevanlinna Prize（1986）
- Knuth Prize（1997）
- EATCS Award（2008）
- Fellow of the Royal Society（FRS，1991）
- AAAI Fellow（1992）
- United States National Academy of Sciences 院士（2001）

## 9. 机构清单

- 教育：King's College, Cambridge（BA）、Imperial College London（MS）、University of Warwick（PhD 1974）
- 任职：Carnegie Mellon University、University of Leeds、University of Edinburgh（1982 前）→ Harvard University（1982 起；T. Jefferson Coolidge Professor of Computer Science and Applied Mathematics，SEAS）

## 10. 终审清单

- [ ] 生卒 1949-03-28 / 在世留白，出生地 Budapest
- [ ] 图灵奖理由整句引用，四大关键词齐全
- [ ] #P 年份口径（1977 定义/1979 论文）一致
- [ ] PAC 论文 1984 与 2013 书不混淆
- [ ] 进化论引语完整、注明出处、不断章
- [ ] BSP 影响表述为"模型被采用"而非"实现等同"
- [ ] 国籍"英裔美国人"、博士导师 Mike Paterson
- [ ] 封面底部状态栏 `英裔美国 | Harvard · Warwick · Cambridge | Turing 2010`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2010/Leslie Valiant/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2011 年肖像（`images/500px-Leslie_Valiant_34913684313_.jpg`，已就绪；注意目录里的 Creative_Commons_by_small.svg.png 是徽标勿用作肖像）
- [ ] **国籍**：封面顶部徽章明示英裔美国
- [ ] **引语核对**：ACM 评价语/Royal Society 提名词/2013 书引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Liskov / Thacker）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
