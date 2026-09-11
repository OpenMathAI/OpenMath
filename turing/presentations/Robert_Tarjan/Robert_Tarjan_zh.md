# Robert Tarjan（罗伯特·塔扬）立传提示词

> qid=Q92638 · 1948-04-30 –（在世留白）· 美国计算机科学家、数学家 · 20 世纪 · 1986 图灵奖（与 John Hopcroft 共享）
> 本地 Wikipedia 数据源：`turing/pages/1986/Robert Tarjan/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 DFS / 强连通分量 / 并查集逆 Ackermann 复杂度的表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Robert Endre Tarjan（中文惯称：罗伯特·塔扬）
- **生卒**：1948-04-30 生于波莫纳（Pomona, California, U.S.）→ **在世，死亡日期留白**
- **国籍**：美国（American）
- **身份**：计算机科学家、数学家；Princeton University James S. McDonnell 杰出大学教授（1985 年起）；现居 Princeton, NJ 与硅谷
- **家庭**：父 George Tarjan（在匈牙利长大，儿童精神病学家，专攻智力障碍领域，曾管理一所州立医院）；弟 James 为国际象棋特级大师；妻 Nayla Rizk（2013 年 NYT 结婚启事）；三女 Alice Tarjan、Sophie Zawacki、Maxine Tarjan
- **少年兴趣**：大量阅读科幻、想当天文学家；因 Martin Gardner 在 Scientific American 的数学游戏专栏转向数学；八年级遇"非常启发人"的老师；高中时打工接触 IBM 穿孔卡分类机；1964 年在 Summer Science Program 学天文时第一次用上真正的计算机
- **教育轨迹**：
  - California Institute of Technology（Caltech）**数学学士 1969**
  - Stanford University **计算机科学硕士 1971**
  - Stanford University **计算机科学博士（辅修数学）1972**，论文 *An Efficient Planarity Algorithm*
- **师承**：博士导师 **Robert W. Floyd**（1978 图灵奖得主）；另一位学术导师 **Donald Knuth**（infobox "Other academic advisors"）——两位都是顶级计算机科学家，"supervised by Robert Floyd and Donald Knuth, both highly prominent computer scientists"
- **选 CS 的理由**：他认为计算机科学是"一种能产生实际影响的做数学的方式"（页面原文转述：computer science was a way of doing mathematics that could have a practical impact）
- **研究领域**：图论算法、数据结构

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 1986（与 John Hopcroft 共享）**：获奖理由整句引用——"For fundamental achievements in the design and analysis of algorithms and data structures."。**共享结构必须写明**；本篇侧重 Tarjan 的数据结构与图算法深水区；**禁写页面无载的两人恩怨**。
2. **深度优先搜索的线性时代（1972）**：博士期间发表 *Depth-first search and linear graph algorithms*（SIAM J. Comput. 1(2), 146–160，1972，论文最高被引之一）——DFS 线性化框架是其一系列算法的母体。
3. **Tarjan 强连通分量算法**：基于 DFS 的经典算法；同族还有 Tarjan 割点/桥（bridge-finding）算法、离线最近公共祖先（off-line LCA）算法——"discoverer of several graph theory algorithms"。
4. **Hopcroft–Tarjan 平面性判定**：**首个线性时间平面性判定算法**（first linear-time algorithm for planarity testing）——与 Hopcroft 的合作成果。
5. **并查集分析**：对不相交集合（disjoint-set / union-find）数据结构的分析——**首个证明涉及逆 Ackermann 函数的最优运行时间**（first to prove the optimal runtime involving the inverse Ackermann function）。
6. **Fibonacci 堆（1987）**：与 Michael L. Fredman 合著 *Fibonacci heaps and their uses in improved network optimization algorithms*（JACM 34(3)）——由树组成的森林型堆，服务网络优化。
7. **伸展树 splay tree**：与博士生 Daniel Sleator 共同发明——自调整二叉搜索树。
8. **median of medians**：线性时间选择算法的五位共同作者之一。
9. **Goldberg–Tarjan 最大流新方法（1988）**：*A new approach to the maximum-flow problem*（JACM 35(4)，与 Andrew V. Goldberg）。
10. **产业界穿行**：Bell Labs（1980–1989）→ NYU（1981–1985，学术重合期）→ NEC Research 研究员（1989–1997）→ Intertrust（1997–2001，2014 年 10 月起重返任首席科学家）→ Compaq（2002）→ HP（2006–2013）→ Microsoft Research Silicon Valley（2013 年 4 月加入）→ 学术主线 Princeton（1985– ）；早年 Cornell（1972–73）、Berkeley（1973–1975）、Stanford（1974–1980）
11. **专利**：至少 18 项美国专利（含 Data Compaction 1989、图聚类方法 2010、人机安全通道 2012）——理论家也做工程。
12. **荣誉与影响**：Nevanlinna Prize **首届得主**、NAS Initiatives in Research 奖（1984）、三大院士（AAAS 1985 / NAS 1987 / NAE 1988 / American Philosophical Society 1990）、Paris Kanellakis Award（1999）、ACM Fellow（1994，理由 "For seminal advances in the design and analysis of data structures and algorithms."）、Caltech 杰出校友（2010）；论文总被引超 94,000 次。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（图算法 — 蓝） | `#2E5A9E` | DFS / 强连通分量 / 平面性判定 / 最大流 |
| 分类色 2（数据结构 — 青绿） | `#1E8E8E` | 并查集 / Fibonacci 堆 / 伸展树 |
| 分类色 3（师承与门生 — 琥珀） | `#D9A441` | Floyd/Knuth 门下 / Sleator 等门生 |
| 分类色 4（产业与专利 — 玫瑰） | `#C0395B` | Bell Labs / HP / Intertrust / 专利 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏 DFS 深度搜索树（嵌套弧线），呼应「深度优先搜索的线性时代」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：上升 / 深入（沿 DFS 一路探到结构最深处）
- **选定曲目**：Alex-Productions **Ascension**（manifest 预分配，直接沿用），匹配"线性时间征服图结构"的上升叙事。
- **落地文件**：`turing/presentations/Robert_Tarjan/Ascension.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「数据结构与图算法大师 · 美国」+ Tarjan 1948– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1948– 生平纵览（在世者不画卒年终点）
4. **波莫纳的天文少年**（1948–1969）：儿童精神病学家之父、棋王弟弟、Martin Gardner 专栏、Summer Science Program 1964
5. **Caltech 数学 → Stanford CS**（1969–1972）：Floyd 与 Knuth 双导师、平面性算法博士论文
6. **DFS 与线性图算法**（1972）：SIAM 论文、强连通分量/桥/LCA 母体 ★ 核心页
7. **Hopcroft–Tarjan 平面性判定**：首个线性时间算法（与 1986 共奖人合作，写合作事实）
8. **并查集与逆 Ackermann**：union-find 最优运行时间分析 ★ 核心页
9. **Fibonacci 堆**（1987）：与 Fredman、网络优化
10. **伸展树与 median of medians**：与 Sleator 的 splay tree、五作者线性选择
11. **图灵奖 1986**：与 Hopcroft 共享、citation 整句展示、共享结构说明
12. **学界与产业之间**：Bell Labs / Intertrust / HP / MSR、18 项专利
13. **荣誉**：Nevanlinna 首届、三大院士、Kanellakis 1999、ACM Fellow 1994
14. **门生与传承**：Sleator / Henzinger / Lengauer / Sitaraman / Westbrook；94,000+ 引用
15. **结尾**：在世、"good structure"追求者的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享结构**：1986 图灵奖为 Tarjan 与 Hopcroft **两人共享、同一 citation**——必须写明共享；本篇侧重数据结构（并查集/Fibonacci 堆/splay 树）与图算法；教材与教育家叙事归 Hopcroft 篇；**禁写页面无载的两人恩怨/竞争**。
- **Nevanlinna Prize 年份两说**：infobox 作 **1982**，正文奖项列表作 **1983**（均注明 first recipient）——页面自相矛盾，**以 infobox 1982 为准**并在 §11 Review-1 复核；勿两处混用。
- **Fibonacci 堆作者**：Michael L. Fredman 与 Tarjan 合著（1987）——勿漏 Fredman 或写成 Tarjan 独作。
- **伸展树**：与 **Daniel Sleator** 共同发明（Sleator 是其博士生）——勿写成 Tarjan 独创。
- **median of medians**：Tarjan 是**五位共同作者之一**（one of five co-authors）——勿写成其个人成果；页面未列其余四人姓名，勿编造。
- **并查集表述**："first to prove the optimal runtime involving the inverse Ackermann function"——写"首个证明含逆 Ackermann 函数的最优运行时间"，勿写成"发明并查集"（数据结构早已有之，Tarjan 的是**分析**）。
- **Hopcroft–Tarjan 平面性**："first linear-time algorithm for planarity testing" 是页面明载——可写；但勿把 1972 DFS 论文与平面性算法混为同一篇。
- **师承红线**：博士导师 **Robert Floyd**（1978 图灵奖得主）；Knuth 是 infobox "Other academic advisors"、正文 "supervised by Robert Floyd and Donald Knuth"——写"Floyd（博士导师）与 Knuth（共同指导/另一位导师）"，勿写成"Knuth 是博士导师"单列。
- **在世**：无卒日，**死亡日期留白**；居所 Princeton, NJ 与硅谷、婚姻（Nayla Rizk, 2013 NYT）与三女仅一笔带过。
- **机构年份交错**：Stanford（1974–1980）与 NYU（1981–1985）与 Bell Labs（1980–1989）时间有交叠（学界/业界并行）——按页面实载年份区间写，勿强行"顺序任职"叙述；Microsoft Research 2013 年 4 月、Intertrust 重返 2014 年 10 月。
- **生日童年细节**：父亲职业、弟弟棋王、Gardner 专栏——按页面实载一笔带过，不渲染。
- **引语红线**：页面无 Tarjan 个人直接引语；可引用的只有①图灵奖 citation、②ACM Fellow 1994 理由、③"very stimulating" teacher 与"way of doing mathematics that could have a practical impact"两处页面实载表述（标注为页面叙述）。其余勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 塔扬（或 罗伯特·塔扬） | 待写入 |
| name_en | Robert Tarjan | 待写入 |
| birth_date | 1948-04-30 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | graph theory algorithms / data structures / algorithms and data structures | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Robert W. Floyd（Stanford，1978 图灵奖得主）
- **另一位导师**：Donald Knuth（infobox "Other academic advisors"）
- **合作者**：John Hopcroft（平面性判定、1986 共享图灵奖）、Michael L. Fredman（Fibonacci 堆）、Andrew V. Goldberg（最大流 1988）、Daniel Sleator（伸展树，亦为门生）
- **著名博士生**：Thomas Lengauer、Monika Henzinger、Ramesh Sitaraman、Daniel Sleator、Jeff Westbrook（infobox 实载 5 人）
- **家庭**：父 George Tarjan（儿童精神病学家）、弟 James（国际象棋特级大师）、妻 Nayla Rizk——家谱事实，勿入学术关系

## 8. 奖项清单

- Turing Award（1986，与 John Hopcroft 共享，"For fundamental achievements in the design and analysis of algorithms and data structures."）
- Nevanlinna Prize in Information Science（infobox 1982 / 正文列表 1983，**首届得主**；年份取 infobox 1982，Review-1 复核）
- NAS Award for Initiatives in Research（1984）
- American Academy of Arts and Sciences 院士（1985 当选）
- National Academy of Sciences 院士（1987 当选）
- National Academy of Engineering 院士（1988 当选）
- American Philosophical Society 会员（1990 当选）
- ACM Fellow（1994，"For seminal advances in the design and analysis of data structures and algorithms."）
- Paris Kanellakis Award in Theory and Practice, ACM（1999）
- Caltech Distinguished Alumni Award（2010）

## 9. 机构清单

- 教育：California Institute of Technology（数学 BS 1969）、Stanford University（CS MS 1971 / CS PhD 1972，辅修数学）
- 学术任职：Cornell University（1972–73）、UC Berkeley（1973–1975）、Stanford University（1974–1980）、NYU（1981–1985）、Princeton University（1985– ，James S. McDonnell 杰出大学教授）
- 产业任职：AT&T Bell Labs（1980–1989）、NEC Research Institute 研究员（1989–1997）、Intertrust Technologies（1997–2001、2014– 首席科学家）、Compaq（2002）、Hewlett-Packard（2006–2013）、Microsoft Research Silicon Valley（2013 年 4 月起）

## 10. 终审清单

- [ ] 生卒 1948-04-30 / 在世留白，出生地 Pomona
- [ ] 图灵奖 1986 与 Hopcroft 共享、citation 整句引用、共享结构写明、无恩怨描写
- [ ] 本篇侧重数据结构（并查集/Fibonacci 堆/splay）与图算法；教材叙事未越界到 Hopcroft 篇
- [ ] Nevanlinna Prize 年份按 infobox 1982，正文 1983 两说不混写
- [ ] Fibonacci 堆=Fredman+Tarjan 1987；splay=Tarjan+Sleator；median of medians=五作者之一
- [ ] 并查集写"分析/首个证明逆 Ackermann 最优运行时间"，勿写"发明并查集"
- [ ] 师承写 Floyd（博士导师）+ Knuth（另一位导师）；门生 5 人按 infobox
- [ ] 机构年份区间按页面实载（含学界/业界并行），不编顺序叙述
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Princeton · Stanford · Bell Labs | Turing 1986`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1986/Robert Tarjan/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Bob_Tarjan.jpg`（infobox 同源照）
- [ ] **Nevanlinna 年份复核**：确认正文展示用 1982（infobox），如终审有新证据再改
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅限 §5 列出的三处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Wirth / Karp / Hopcroft）格式对齐；与 Hopcroft 篇侧重区分复核

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
