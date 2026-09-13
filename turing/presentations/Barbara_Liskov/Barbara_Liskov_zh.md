# Barbara Liskov（芭芭拉·利斯科夫）立传提示词

> qid=Q16080922 · 1939-11-07 – 在世留白 · 美国计算机科学家 · 20/21 世纪 · 2008 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2008/Barbara Liskov/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（数据抽象 / Liskov 替换原则 / 拜占庭容错的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Barbara Jane Liskov（本姓 Huberman；中文惯称：芭芭拉·利斯科夫）
- **生卒**：1939-11-07 生于洛杉矶（Los Angeles，加利福尼亚州，美国）→ 在世留白
- **国籍**：美国（American）
- **身份**：计算机科学家；MIT Institute Professor、Ford Professor of Engineering；Programming Methodology Group 负责人
- **家庭**：父母 Jane（née Dickhoff）与 Moses Huberman 的四个孩子中的长女；犹太家庭；1970 年与 Nathan Liskov 结婚；一子 Moses（MIT 计算机科学博士 2004，任教于 College of William & Mary）
- **教育轨迹**：
  - 1961 年 UC Berkeley **数学**学士（BA，辅修物理）；当年专业里只有她与另一位女生
  - 申请 Berkeley/Princeton 数学研究生：Princeton 数学系当时不收女生；被 Berkeley 录取却先赴波士顿
  - MITRE Corporation 工作一年 → Harvard 编程工作（语言翻译方向）
  - 1968 年 3 月 Stanford University **计算机科学**博士，论文 *A Program to Play Chess End Games*——美国最早获 CS 博士的女性之一
- **博士导师**：John McCarthy（Stanford，AI 契基人之一，1971 图灵奖得主）——页面明载师承，可写
- **研究领域**：程序设计语言、数据抽象、分布式计算、容错（Byzantine fault tolerance）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **数据抽象的奠基人**：引入抽象数据类型（abstract data types）与数据抽象原理——图灵奖核心；1974 与 Zilles 论文 *Programming with abstract data types*。
2. **女性先驱**：美国最早获计算机科学博士的女性之一（Stanford，1968-03）；**第二位**图灵奖女性得主（页面原文 "the second woman to receive the Turing Award"——有载可写）。
3. **CLU 语言（1970s）**：设计与实现，抽象机制论文 *Abstraction mechanisms in CLU*（1977, CACM）；CLU/Argus 后来深刻影响 Java、C++、C#、Ada 等语言。
4. **Venus 操作系统**：小型低成本分时系统（time-sharing）——早期系统工作。
5. **Argus 语言（1980s）**：**首个**支持分布式程序实现的高级语言，并演示了 promise pipelining 技术——注意"首个"限定语是页面原文（"the first high-level language to support the implementation of distributed programs"）。
6. **Thor**：面向对象数据库系统——四项 Known for 系统（Venus/CLU/Argus/Thor）之一。
7. **Liskov 替换原则（LSP）**：与 Jeannette Wing 合作提出子类型的行为化定义（"A behavioral notion of subtyping", TOPLAS 1994），把数据抽象思想应用于面向对象编程的子类型与继承；已成为软件工程教科书中的形式化判据。
8. **拜占庭容错**：与 Miguel Castro 的 *Practical Byzantine fault tolerance*（OSDI '99）——实用拜占庭容错里程碑；当前研究焦点即 BFT 与分布式计算。
9. **1968 博士论文的另一面**：国际象棋残局程序，发展出重要的 **killer heuristic**（杀手启发式）——从 AI 起步的博士论文。
10. **学术影响**：5 本专著（如与 John Guttag 合著 *Abstraction and Specification in Program Development* 1986、*Program Development in Java* 2000）+ 百余篇技术论文（截至 2023-02）。
11. **荣誉等身**：图灵奖 2008（2009-03 领奖）、von Neumann Medal 2004、National Inventors Hall of Fame 2012、Computer Pioneer Award 2018、Benjamin Franklin Medal 2023；NAE/NAS 成员、AAAS/ACM Fellow；2002 年 Discover 杂志"科学界 50 位最重要女性"。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（程序设计语言 — 蓝） | `#2E5A9E` | CLU / Argus / Venus |
| 分类色 2（数据抽象 — 青绿） | `#1E8E8E` | 抽象数据类型 / 数据抽象原理 |
| 分类色 3（面向对象 — 琥珀） | `#D9A441` | Liskov 替换原则 / 子类型 |
| 分类色 4（分布式与容错 — 玫瑰） | `#C0395B` | Argus 分布式 / 拜占庭容错 / Thor |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「抽象层次包裹实现细节」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：明亮 / 开创（第二位女性图灵奖得主、数据抽象奠基）
- **选定曲目**：Alex-Productions **Shine Like The Sun**（明亮 / 昂扬），manifest 预分配，直接沿用。
- **落地文件**：`turing/presentations/Barbara_Liskov/ShineLikeTheSun.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「数据抽象奠基人 · 美国」+ Liskov 1939– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1939–在世 生平纵览
4. **早年：洛杉矶长女与伯克利数学**（1939–1961）：犹太家庭、Berkeley 数学（专业仅两名女生）、Princeton 数学系不收女生的年代背景
5. **MITRE 与 Harvard：转向计算机**（1961–1968）：MITRE 一年、Harvard 语言翻译编程工作
6. **Stanford 博士：McCarthy 门下的国际象棋程序**（1968）：残局程序、killer heuristic、美国最早 CS 博士女性之一
7. **数据抽象与 CLU**（1970s）：abstract data types、CLU 语言的抽象机制、影响 Java/C++/C#/Ada
8. **Venus 与系统工作的起点**：小型分时系统
9. **Argus：首个分布式高级语言**（1980s）：promise pipelining
10. **Liskov 替换原则**（与 Wing，1994）：行为化子类型定义、面向对象设计的教科书判据
11. **Thor 与分布式数据库**：面向对象数据库系统
12. **实用拜占庭容错**（Castro & Liskov, OSDI '99）：BFT 走向实用
13. **荣誉与传承**：Turing 2008、von Neumann 2004、Inventors HOF 2012、门生 Herlihy/Ghemawat 等
14. **女性先驱与遗产**：第二位女性图灵奖得主、Discover 50 女性、ETH 荣誉博士（与 Knuth 同台）
15. **结尾**：在世、数据抽象与容错的当代回响

## 5. 史实陷阱与敏感点（终审必须检查）

- **"第二位女性图灵奖得主"**：页面原文有载（"the second woman to receive the Turing Award"），**可写**；但"第三位/首位"等其它序数表述勿延伸。
- **"美国最早 CS 博士女性之一"**：页面原文 "one of the first women in the United States to be awarded a Ph.D. from a computer science department at Stanford University"——是"**之一**"且限定 Stanford CS 系（1968-03），勿写"全美第一位 CS 博士"。
- **Princeton 不收女生**：页面说的是当时 Princeton **数学**研究生项目不收女生（她申请的是数学），勿写成"Princeton 拒绝了她的 CS 申请"。
- **师承**：博士导师 John McCarthy 为 infobox + 正文（"At Stanford, she worked with John McCarthy"）明载，**可写**；勿再加别的导师。
- **viewstamped replication / Paxos**：**页面未载，禁写**。分布式部分只写页面实载的 Argus/promise pipelining/懒复制论文（Ladin-Liskov 1992 "Providing high availability using lazy replication"）与 BFT。
- **获奖理由（ACM citation）**：整句引用 "programming language and system design, especially related to data abstraction, fault tolerance, and distributed computing"（"contributions to the practical and theoretical foundations of" 为引导语）——这是核心红线，勿改写。
- **图灵奖年份口径**：获奖为 **2008** 年度，2009 年 3 月正式颁奖领奖——封面写 2008，叙事页可注"2009-03 授予"。
- **CLU/Argus 影响表述**：页面说 "would later have influence on many well-known programming languages such as Java, C++, C#, and Ada"——是"影响"而非"直接继承"，勿写"CLU 是 Java 的前身"。
- **LSP 合作者**：LSP 是**与 Jeannette Wing 合作**提出——勿单归 Liskov；论文 1994 年发表。
- **在世**：死亡日期留白，生卒写 `1939–`，勿写卒年。
- **引语**：仅收录页面可见的颁奖词（von Neumann Medal 2004 引文 "fundamental contributions to programming languages, programming methodology, and distributed systems"；Franklin Medal 2023 引文 "seminal contributions to computer programming languages and methodology..."）。正文**无本人直接引语，勿编造**。
- **家族**：丈夫 Nathan Liskov（1970 结婚）、儿子 Moses 是可写的一笔个人生活；勿渲染更多。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 芭芭拉·利斯科夫 | 待写入 |
| name_en | Barbara Liskov | 待写入 |
| birth_date | 1939-11-07 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | programming languages / data abstraction / distributed computing / fault tolerance | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：John McCarthy（Stanford，1971 图灵奖得主）
- **重要合作者**：Jeannette Wing（LSP 合作者）、John Guttag（合著者）、Miguel Castro（Practical Byzantine fault tolerance）、Stephen Zilles（1974 抽象数据类型论文）
- **著名博士生**：Maurice Herlihy、J. Eliot Moss、Sanjay Ghemawat、Andrew Myers、Dan R.K. Ports
- **同奖/同台**：Donald E. Knuth（2005 同获 ETH 荣誉博士，非师承非合作，勿入关系库，可入叙事）

## 8. 奖项清单

- A.M. Turing Award（2008，2009-03 授予；ACM citation 如 §5）
- IEEE John von Neumann Medal（2004）
- National Inventors Hall of Fame（2012）
- Computer Pioneer Award（IEEE Computer Society，2018）
- Benjamin Franklin Medal（Franklin Institute，2023）
- ETH Honorary Doctorate（2005-11-19，与 Donald E. Knuth 同批）
- University of Lugano 荣誉博士（2011）；Universidad Politécnica de Madrid 荣誉博士（2018）
- NAE 成员、NAS 成员、American Academy of Arts and Sciences Fellow、ACM Fellow
- Discover 杂志"科学界 50 位最重要女性"（2002）；MIT 顶级女教师（2002）
- Infosys Prize 工程-计算机科学初届评审团成员（2009）

## 9. 机构清单

- 教育：UC Berkeley（数学 BA，辅修物理，1961）、Stanford University（MS + PhD，1968-03）
- 任职：MITRE Corporation（两段：毕业后研究岗 + Harvard 编程岗之前各一段）、Harvard（编程工作，语言翻译）、MIT（Programming Methodology Group 负责人；2008-07 起 Institute Professor 兼 Ford Professor of Engineering）

## 10. 终审清单

- [ ] 生卒 1939-11-07 / 在世留白，出生地 Los Angeles
- [ ] "第二位女性图灵奖得主"与"美国最早 CS 博士女性之一（Stanford 1968-03）"表述精确
- [ ] 图灵奖理由整句引用且年份口径 2008（2009-03 颁发）
- [ ] LSP"与 Jeannette Wing 合作、1994 论文"表述准确
- [ ] CLU/Argus 对 Java/C++/C#/Ada 是"影响"非"前身"
- [ ] viewstamped replication / Paxos 未出现在正文（页面无载禁写）
- [ ] 博士导师 John McCarthy 表述准确
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | MIT · Stanford · UC Berkeley | Turing 2008`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2008/Barbara Liskov/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 MIT 2010 肖像（`images/Barbara_Liskov_MIT_2010.jpg`，已就绪；原文写 500px-Barbara_Liskov_MIT_computer_scientist_2010.jpg 与实际文件名不符，执行时已按实际文件纠正）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅颁奖词类引文）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Thacker / Valiant）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
