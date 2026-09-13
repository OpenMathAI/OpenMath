# Stephen Cook（斯蒂芬·库克）立传提示词

> qid=Q62870 · 1939-12-14 出生（在世） · 美裔加拿大计算机科学家、数学家 · 20 世纪 · 1982 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1982/Stephen Cook/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国/加拿大`，页面口径 "American-Canadian"），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（SAT ∈ NP / P vs NP 的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Stephen Arthur Cook（中文惯称：斯蒂芬·库克，通称 Steve Cook；OC、OOnt）
- **生卒**：1939-12-14 生于纽约州布法罗（Buffalo, New York）——**在世，卒年留白**；现与妻子居于多伦多，育有两子，其中一子为奥运帆船运动员 Gordon Cook
- **国籍**：美裔加拿大人（American-Canadian）
- **身份**：计算机科学家、数学家（计算复杂性理论奠基人之一，"one of the forefathers of computational complexity theory"）；University of Toronto 计算机科学与数学系 university professor emeritus
- **教育轨迹**：
  - University of Michigan：**学士**（B.A.）1961
  - Harvard University **数学系**：**硕士** 1962、**博士** 1966；论文 *On the Minimum Computation Time of Functions*
- **博士导师**：Hao Wang（王浩，数理逻辑学家）
- **研究领域**：计算复杂性理论、命题证明复杂度（兼及程序语言语义、并行计算、人工智能、有界算术、有界逆向数学、高阶函数复杂度、分析复杂度、命题证明系统下界）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **Buffalo 出生，Michigan 打底**（1939–1961）：1961 年密歇根大学学士；博士阶段研究**函数的复杂度，主要是乘法**（multiplication）。
2. **Harvard 数学系博士（1966）**：师从王浩（Hao Wang）——逻辑与计算交叉的学术起点。
3. **Berkeley 之憾（1966–1970）**：1966 年入职 UC Berkeley 数学系任助理教授，1970 年**未获连任**；Karp（同为图灵奖得主）三十年后感言："It is to our everlasting shame that we were unable to persuade the math department to give him tenure."（整句引语，计算机科学史上著名遗憾）。
4. **多伦多新家（1970– ）**：1970 年加入 University of Toronto 计算机科学与数学系任副教授，1975 年升教授，1985 年任 Distinguished Professor，现为 university professor emeritus。
5. **1971 STOC 论文**：*The Complexity of Theorem Proving Procedures*（1971 ACM SIGACT STOC）——形式化**多项式时间归约**（Cook reduction）与 **NP 完全性**，并证明 **SAT（布尔可满足性）是 NP 完全的**——NP 完全类存在性的首个证明。
6. **Cook–Levin 定理**：该定理由苏联的 **Leonid Levin 独立证明**——共享命名，"independently" 必须保留。
7. **P vs NP 之问**：同一论文提出了"计算机科学最著名的问题"——非形式化表述：答案可被高效验证的判定问题是否都可被高效求解？Cook 猜想 **P ≠ NP**；该猜想至今未解，是七大 **Millennium Prize Problems** 之一。
8. **证明复杂度开创**：1975 年论文 *Feasibly Constructive Proofs and the Propositional Calculus* 引入**等式理论 PV**（Polynomial-time Verifiable）；1979 年与学生 **Robert A. Reckhow** 合著 *The Relative Efficiency of Propositional Proof Systems*——形式化 **p-simulation** 与高效命题证明系统，开创命题证明复杂度领域；证明"每个真公式都有短证明的证明系统存在 ⇔ NP = coNP"；与学生 **Phuong The Nguyen** 合著 *Logical Foundations of Proof Complexity*。
9. **复杂度类的命名者**：以 **Nick Pippenger** 命名 **NC**；**SC** 以他命名（"Steve's class"）；**AC⁰** 及 AC 层级亦由他引入。
10. **KMP 算法渊源**：据 **Don Knuth** 所言，KMP 算法的灵感来自 Cook 的"线性时间识别拼接回文"的自动机——三项间接贡献勿写成Cook 本人发明 KMP。
11. **图灵奖 1982**：citation 见 §5 整句红线；ACM 2008 年授予 Fellow（"fundamental contributions to the theory of computational complexity"）。
12. **荣誉与门生**：Herzberg 金奖 2012（加拿大科学与工程最高荣誉）、加拿大勋章军官 2015、BBVA Frontiers 2015；FRS（伦敦皇家学会）与皇家学会（加拿大）会士、NAS 院士、美国艺术与科学院院士；**36 名博士**毕业，含 Toniann Pitassi、Walter Savitch、Mark Braverman、Arvind Gupta、Anna Lubiw。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（NP 完全性 — 蓝） | `#2E5A9E` | 1971 STOC / SAT |
| 分类色 2（P vs NP — 青绿） | `#1E8E8E` | Cook–Levin / Millennium 问题 |
| 分类色 3（证明复杂度 — 琥珀） | `#D9A441` | PV 1975 / Reckhow 1979 / p-simulation |
| 分类色 4（复杂度类与传承 — 玫瑰） | `#C0395B` | NC / SC / AC⁰ / 36 名博士 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「可验证与可求解之界」的计算复杂性美学。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：深邃 / 未竟（P vs NP 至今悬而未决的长线悬念）
- **选定曲目**：Alex-Productions **PAST**（manifest 预分配，直接沿用），匹配"回望 1971 时刻、凝视悬而未决之问"的叙事。
- **落地文件**：`turing/presentations/Stephen_Cook/PAST.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「计算复杂性之父之一 · 美国/加拿大」+ 库克 1939– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1939– 生平纵览（卒年留白）
4. **Buffalo 与 Michigan**（1939–1961）：1961 学士、博士期乘法复杂度研究
5. **Harvard：王浩门下**（1962–1966）：数学系硕博、逻辑与计算交叉
6. **Berkeley 之憾**（1966–1970）：未获连任、Karp 整句引语
7. **多伦多新家**（1970– ）：CS+Math 双聘、1975 教授、1985 Distinguished Professor
8. **1971 STOC 论文**：Cook reduction、NP 完全性、SAT
9. **Cook–Levin 定理**：Levin 苏联独立证明、共享命名
10. **P vs NP**：最著名问题、Cook 猜想 P≠NP、Millennium Prize
11. **证明复杂度**：PV 1975、Reckhow 1979、p-simulation、NP=coNP 等价
12. **复杂度类的命名**：NC（Pippenger）、SC（以他命名）、AC⁰、KMP 渊源（Knuth 之言）
13. **图灵奖 1982**：citation 整句引用
14. **荣誉与传承**：Herzberg 2012 / Order of Canada 2015 / BBVA 2015；36 名博士与 Pitassi 等
15. **结尾**：在世大师、"复杂性理论奠基人之一"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **在世留白**：Cook 生于 1939-12-14，页面为现在时叙述（"is an American-Canadian..."、"lives with his wife in Toronto"）——**卒年留白，勿写卒年**；家庭细节（妻子、两子、Gordon Cook 奥运帆船）按页面实载一笔带过。
- **图灵奖理由（核心红线）**：整句 citation："For his advancement of our understanding of the complexity of computation in a significant and profound way. His seminal paper, The Complexity of Theorem Proving Procedures, presented at the 1971 ACM SIGACT Symposium on the Theory of Computing, laid the foundations for the theory of NP-Completeness. The ensuing exploration of the boundaries and nature of NP-complete class of problems has been one of the most active and important research activities in computer science for the last decade."——长 citation 须整段准确。
- **Cook–Levin 共享**：Levin 在**苏联独立证明**——"independently" 必须保留，勿写"Levin 延续 Cook"或"Cook 独享"。
- **P vs NP 归属**：1971 论文"formulated the most famous problem"——提出问题归 Cook；但勿写"提出 NP 类本身"之类超出页面表述的断言；Cook 立场是**猜想 P ≠ NP**。
- **KMP 渊源口径**：据 **Knuth** 所言 KMP 灵感来自 Cook 的回文自动机——引语归属 Knuth，Cook 贡献是"启发性自动机"，勿写 Cook 参与设计 KMP。
- **NC/SC/AC⁰**：NC 以 Pippenger 命名、SC 以 Cook 命名、AC⁰ 及 AC 层级由他引入——三个方向勿混。
- **Berkeley 引语归属**：整句 Karp 感言出自 Karp 在 Berkeley EECS 三十周年演讲——引语页注明"Karp 语"，勿挂 Cook 名下。
- **学位学科**：Michigan 学士 + Harvard **数学系**硕士（1962）博士（1966）——无 CS 学位（勿写 CS PhD）。
- **SC 命名证据等级**：页面脚注源为 Stack Exchange（"Steve's class: origin of SC"）——可写"以他命名"，但勿加页面外的命名故事细节。
- **36 名博士**：页面明载 "36 PhD students have completed their degrees"；infobox 列 5 名（Braverman/Pitassi/Savitch/Gupta/Lubiw）——同 Floyd 篇处理法：列 infobox 5 人 + "共 36 名"注。
- **奖项**：Steacie Fellowship 1977、Killam 1982、CRM-Fields-PIMS 1999、Gödel Lecture 1999、Synge 2006、Bolzano 2008、ACM Fellow 2008、Herzberg 2012、Order of Ontario 2013、Officer of Order of Canada 2015、BBVA 2015——均页面实载；无 Kyoto/无 Kyoto 类，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 斯蒂芬·库克（或 库克） | 待写入 |
| name_en | Stephen Cook | 待写入 |
| birth_date | 1939-12-14 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Canada / United States（American-Canadian） | 待写入 |
| primary_occupation | computer scientist, mathematician | 待写入 |
| field_of_work | computational complexity theory / proof complexity / NP-completeness | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Hao Wang（王浩，Harvard 数理逻辑学家）
- **合作者**：Robert A. Reckhow（1979 证明系统合著）、Phuong The Nguyen（Logical Foundations of Proof Complexity 合著）
- **学术同侪**：Leonid Levin（Cook–Levin 定理独立证明者——independent-prover 关系）、Richard Karp（Berkeley 同事、为其未获终身教职发声）
- **博士生**（infobox 5 名，共 36 名）：Toniann Pitassi、Walter Savitch、Mark Braverman、Arvind Gupta、Anna Lubiw
- **思想承继**：Nick Pippenger（NC 命名对象）、Don Knuth（KMP 渊源转述者）
- **家庭**：Gordon Cook（儿子，奥运帆船运动员，页面实载）

## 8. 奖项清单

- NSERC E.W.R. Steacie Memorial Fellowship（1977）
- Turing Award（1982）
- Killam Research Fellowship（1982）
- CRM-Fields-PIMS Prize（1999）
- Gödel Lecture（Association for Symbolic Logic，1999）
- John L. Synge Award（2006）
- Bernard Bolzano Medal（Czech Academy of Sciences，2008）
- ACM Fellow（2008，"fundamental contributions to the theory of computational complexity"）
- Gerhard Herzberg Canada Gold Medal for Science and Engineering（2012，加拿大科学与工程最高荣誉）
- Order of Ontario（2013，安大略最高荣誉）
- Officer of the Order of Canada（2015）
- BBVA Foundation Frontiers of Knowledge Award（ICT 类，2015，"for his important role in identifying what computers can and cannot solve efficiently"）
- 会士/院士：Royal Society of London、Royal Society of Canada、NAS（美国）、American Academy of Arts and Sciences、Göttingen Academy 通讯会员

## 9. 机构清单

- 教育：University of Michigan（B.A. 1961）、Harvard University（数学系 MA 1962、PhD 1966）
- 任职：University of California, Berkeley（数学系助理教授，1966–1970，未获连任）→ University of Toronto（计算机科学与数学系，1970 副教授 → 1975 教授 → 1985 Distinguished Professor → university professor emeritus）

## 10. 终审清单

- [ ] 生卒 1939-12-14 出生、**在世留白**，出生地 Buffalo（New York），现居多伦多
- [ ] "American-Canadian" 国籍口径统一
- [ ] 1971 STOC 论文三要素（Cook reduction / NP 完全性 / SAT）表述准确
- [ ] Cook–Levin "Levin 苏联独立证明"表述准确
- [ ] Cook 猜想 P≠NP、Millennium Prize 表述准确
- [ ] Karp Berkeley 引语归属正确
- [ ] KMP 渊源"据 Knuth"归属正确，未写成 Cook 发明 KMP
- [ ] NC/SC/AC⁰ 三条命名线不混淆
- [ ] 图灵奖长 citation 整段引用无误
- [ ] 肖像文件核对：`images/500px-Prof.Cook.jpg`（2008 年照；另有 1968 年照 `500px-Stephen_A._Cook_1968_enlarged_portion_.jpg` 可用于早年页）
- [ ] 封面底部状态栏 `美国/加拿大 | Toronto · Berkeley · Harvard | Turing 1982`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1982/Stephen Cook/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Prof.Cook.jpg`（500px，2008 年照，已就绪）；时间线/早年页可配 1968 年照并注明
- [ ] **国籍**：封面顶部徽章明示美国/加拿大
- [ ] **引语核对**：Karp 感言与长 citation 必须与 Wikipedia 原文逐字一致
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一；P/NP 数学符号排版核对
- [ ] 与同期图灵奖得主（Codd / Hoare）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
