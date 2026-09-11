# Dana Scott（达纳·斯科特）立传提示词

> qid=Q49823 · 1932-10-11 – 在世留白 · 美国逻辑学家 · 20/21 世纪 · 1976 图灵奖（与 Michael O. Rabin 共享）
> 本地 Wikipedia 数据源：`turing/pages/1976/Dana Scott/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰（注意：该页面缺内联引用横幅，个人生活信息无载——见 §5）。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（域理论 / 非确定性自动机 / Boolean-valued model 的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Dana Stewart Scott（中文惯称：达纳·斯图尔特·斯科特）
- **生卒**：1932-10-11 生于伯克利（Berkeley, California）；**在世**——页面载"now retired and lives in Berkeley, California"，死亡日期**在世留白**
- **国籍**：美国（American）
- **身份**：逻辑学家（Carnegie Mellon University 计算机科学、哲学与数理逻辑 **Hillman University Professor emeritus**）
- **家庭/婚姻**：**页面无载，禁写**（页面缺内联引用横幅，infobox 无 spouse 字段）
- **教育轨迹**：
  - University of California, Berkeley **数学 BA**（1954）——本科即随 Tarski 进修、进入 Tarski 圈子（与 Richard Montague、Solomon Feferman 同侪）
  - Princeton University **MA、PhD**（博士论文 *Convergent Sequences of Complete Theories*，1958 答辩）
- **博士导师**：Alonzo Church（Princeton）
- **研究领域**：计算机科学、数学、哲学（自动机理论、数理逻辑、集合论、模态逻辑、程序语言语义、拓扑、范畴论）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1976 图灵奖（与 Michael O. Rabin 共享）**：ACM citation 针对 1959 合著论文（同 Rabin 篇引文："For their joint paper 'Finite Automata and Their Decision Problems,' which introduced the idea of nondeterministic machines..."）——本篇侧重 Scott 的**逻辑与语义学**贡献，AI 自动机仅是起点。
2. **Tarski 圈子与决裂（本科时期）**：Scott 在 Berkeley 本科即被认可天资、进入 Tarski 周边小组（Feferman、Montague），本已内定随 Tarski 读博，但因故决裂赴 Princeton 师从 Church——**后修补**，Tarski 对他说："I hope I can call you my student."（Feferman 2005 转述，**可用引语**）
3. **1959 论文与图灵奖**：与 Princeton 同侪 Rabin 合著 *Finite Automata and Their Decision Problem[s]*（IBM Journal 3(2), 114–125, 1959）——引入**非确定性机器**到自动机理论，成为计算复杂度理论的基本概念。
4. **回到伯克利（1960–1963）**：数学助理教授；**证明构造性公理与可测基数存在不相容**——集合论演化中的开创性结果；期间开始指导博士生（James Halpern、Edgar Lopez-Escobar）。
5. **模态逻辑三线**：与 **John Lemmon** 合作（Lemmon 1966 去世后 Scott 整理遗稿，1977 出版 *An Introduction to Modal Logic*）；与 **Richard Montague** **各自独立**发现 Kripke 语义的重要推广——**Scott–Montague 语义**；引入 **filtrations（滤构造）** 与典范模型的精化——现代 Kripke 语义核心概念。
6. **Boolean-valued models 与连续统假设（1967）**：循 Robert Solovay 的初步观察，Scott 形式化 Boolean-valued model 概念（Solovay 与 Vopěnka 亦同期独立给出），以之对 Paul Cohen 的连续统假设独立性给出另一分析——获 **1972 Leroy P. Steele Prize**。
7. **Oxford（1972–1981）**：哲学系**数理逻辑教授**、Merton College 院士（今荣誉院士）；此期与 **Christopher Strachey** 合作——**Scott–Strachey 方法（指称语义 denotational semantics）**，理论计算机科学的奠基性贡献。
8. **域理论（domain theory）**：Scott 的关键贡献——使含递归函数与循环控制结构的程序获得指称语义；又以域理论与**信息系统（information systems）**理论为无穷与连续信息提供基础；Scott domain / Scott topology / Scott information system / Scott encoding 皆以其命名。
9. **CMU（1981–2003）**：提出 **equilogical spaces** 作为域理论的后继理论（其范畴是笛卡尔闭范畴，而 domains 范畴不是）；1994 当选 ACM Fellow、2012 当选 AMS Fellow。
10. **荣誉与讲席**：Tarski Lectures（1989）、Gödel Lecture（1991）、Harold Pender Award（1990，"application of concepts from logic and algebra to the development of mathematical semantics of programming languages"）、**Rolf Schock Prize**（1997，瑞典皇家科学院，逻辑与哲学——citation："his conceptually oriented logical works, especially the creation of domain theory, which has made it possible to extend Tarski's semantic paradigm to programming languages as well as to construct models of Curry's combinatory logic and Church's calculus of lambda conversion"）、Bolzano Prize（2001，捷克科学院）、EATCS Award（2007）。
11. **门生成林**：14 位著名博士生——Peter Mosses、David Turner（自由函数式语言 SASL）、Kenneth Kunen、Angus Macintyre、Andrej Bauer、Krister Segerberg、Jack Copeland 等（见 §7）。
12. **晚景**：荣休后居伯克利；ACM 系列访谈（2020–2021，Gordon Plotkin 主持四部曲）；DOMAIN 2002 工作会以其 70 寿辰纪念。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（自动机理论 — 蓝） | `#2E5A9E` | Rabin–Scott / 非确定性自动机 |
| 分类色 2（逻辑与集合论 — 青绿） | `#1E8E8E` | 可测基数 / Boolean-valued models / 模态逻辑 |
| 分类色 3（指称语义 — 琥珀） | `#D9A441` | Scott–Strachey / 域理论 / information systems |
| 分类色 4（范畴论与新基础 — 玫瑰） | `#C0395B` | equilogical spaces / Scott topology |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和分层网格（稀疏半透明方格渐变），呼应「从集合到域、从语法到语义」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：锐利 / 奠基（以逻辑之力为程序语言立语义根基）
- **选定曲目**：Alex-Productions **Savage**（manifest 预分配，直接沿用），匹配"逻辑之刃剖开语义混沌"的叙事。
- **落地文件**：`turing/presentations/Dana_Scott/Savage.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「逻辑学家 · 美国」+ 斯科特 1932– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域；在世者卒年留白）
3. **时间线**（`\timelineslide`）：1932– 生平纵览（终点写"在世·Berkeley"）
4. **伯克利少年与 Tarski 圈子**（1932–1954）：本科入组、决裂远走
5. **Princeton：Church 门下**（1954–1958）：*Convergent Sequences of Complete Theories*
6. **Lamb Estate 之外：与 Rabin 的 1959 论文**——非确定性自动机与图灵奖伏笔
7. **回到伯克利**（1960–1963）：构造性公理 vs 可测基数
8. **模态逻辑的黄金期**：Lemmon 遗稿、Montague、Scott–Montague 语义、filtrations
9. **Boolean-valued models 与连续统假设**（1967）→ Steele Prize 1972
10. **Oxford 岁月**（1972–1981）：与 Strachey 共铸指称语义
11. **域理论**：DCPO、Scott domain/topology/encoding、information systems
12. **CMU 与新基础**（1981–2003）：equilogical spaces、Hillman 讲席
13. **荣誉与讲席**：Steele 1972 / Pender 1990 / Schock 1997 / EATCS 2007
14. **门生成林与遗产**：Turner/Bauer/Kunen 等 14 位博士生
15. **结尾**：在世荣休于 Berkeley、"以语义安放程序"的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享奖结构**：1976 图灵奖与 **Rabin 共享**、获奖对象为 **1959 合著论文**——必须写明；本篇侧重 Scott 的逻辑/集合论/语义学主线，自动机仅第 6 页一节，Rabin 篇侧重复杂度与密码学。
- **论文标题单复数**：Scott 页 bibliography 作 "Finite Automata and Their Decision **Problem**"（单数），Rabin 页与 ACM citation 作复数 "Problems"——**引用 citation 时用原文（复数）**；正文叙述统一用复数，Review-1 核对全文一致。
- **在世者**：**无死亡日期，卒年留白**——时间线/身份页/结尾页一律写"在世"；页面载其荣休后居 Berkeley, California。
- **Tarski 决裂原因**：页面明确写 "for reasons explained in our biography"（引 Feferman）**未载具体原因**——决裂事实可写，原因**禁写/勿编造**；修补后的引语 "I hope I can call you my student." 必须注明出自 Feferman 2005 转述。
- **Boolean-valued models**：Solovay 与 Vopěnka **同期独立**给出，Scott 是"formulated the concept"（循 Solovay 的观察）——勿写"Scott 独创"。
- **Scott–Montague 语义**：两人**各自独立**发现——勿写师承或共同研究。
- **Lemmon 遗稿**：*An Introduction to Modal Logic*（1977）是 Lemmon 1966 年去世后 Scott 整理出版的**未完成专著**——勿写成两人同期合著的完整教科书。
- **个人生活**：页面**无婚姻、子女、宗教、政治信息**——全部禁写。
- **页面质量提示**：本页挂 "lacks sufficient corresponding inline citations"（2018-02）横幅——事实表述宜保守，凡争议性评价语（如 "seminal"）注明是 Wikipedia 引述。
- **可引语**：限三条——ACM citation、Tarski "I hope I can call you my student."（Feferman 转述）、Pender/Schock 两段 citation（原文可见可整引）；其余勿编造。
- **荣誉**：无 Nobel、无 Israel Prize 类国家级大奖表述；Schock Prize 属瑞典皇家科学院——勿写"瑞典国王亲自颁发"之类无载细节。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 斯科特（或 达纳·斯科特） | 待写入 |
| name_en | Dana Scott | 待写入 |
| birth_date | 1932-10-11 | 待写入 |
| death_date | 空（在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | logician / computer scientist | 待写入 |
| field_of_work | automata theory / mathematical logic / set theory / modal logic / denotational semantics / domain theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Alonzo Church（Princeton）
- **伯克利早年导师**：Alfred Tarski（决裂后修补；"I hope I can call you my student."）
- **关键合作者**：Michael O. Rabin（1959 论文、1976 共享图灵奖）、Christopher Strachey（指称语义）、John Lemmon（模态逻辑）、Richard Montague（Scott–Montague 语义，独立发现）
- **著名博士生**：Jack Copeland、Michael Fourman、Kenneth Kunen、Angus Macintyre、Peter Mosses、Roy Dyckhoff、Ketan Mulmuley、Marko Petkovšek、Fred S. Roberts、David Turner、Martin Davies、Krister Segerberg、Andrej Bauer、Joseph Almog
- **早年学生（Berkeley 期）**：James Halpern、Edgar Lopez-Escobar

## 8. 奖项清单

- Turing Award（1976，与 Michael O. Rabin 共享）
- Leroy P. Steele Prize（1972，连续统假设独立性证明）
- Tarski Lectures（1989）
- Harold Pender Award（1990）
- Gödel Lecture（1991）
- Rolf Schock Prize（1997，瑞典皇家科学院，逻辑与哲学）
- Bolzano Prize（2001，捷克科学院）
- EATCS Award（2007）
- ACM Fellow（1994）；American Mathematical Society Fellow（2012）
- Merton College, Oxford 荣誉院士；CMU Hillman University Professor emeritus

## 9. 机构清单

- 教育：University of California, Berkeley（数学 BA 1954）、Princeton University（MA/PhD 1958）
- 任职：University of Chicago instructor（至 1960）、UC Berkeley 数学助理教授（1960–1963）、Stanford（1963 起，页面载"Stanford, Amsterdam and Princeton, 1963–1972"阶段，具体职务页面未细载勿编）、University of Oxford 数理逻辑教授（1972–1981，Merton College）、Carnegie Mellon University（1981–2003，Hillman University Professor，荣休）

## 10. 终审清单

- [ ] 生年 1932-10-11、出生地 Berkeley，卒年**在世留白**（时间线/身份页/结尾页一致）
- [ ] 1976 图灵奖写明"与 Rabin 共享、获奖对象为 1959 合著论文"，citation 整句引用无误
- [ ] Tarski 决裂只写事实、不写原因；修补引语注明 Feferman 转述
- [ ] Boolean-valued models 写"三人同期独立"，勿写独创
- [ ] Scott–Montague 语义写"各自独立发现"
- [ ] Lemmon 遗稿（1977 出版）性质表述准确
- [ ] 个人生活全无载禁写（婚姻/子女/政治/宗教）
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Berkeley · Princeton · Oxford · CMU | Turing 1976`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1976/Dana Scott/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Scott_Dana_small.jpg`（取 500px 版；目录中的 `Text_document_with_red_question_mark.svg.png` 是占位问号图标，**勿用**）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（限 §5 所列）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐（在世者卒年格子写"—/在世"）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Rabin 1976）篇目侧重区分度检查，格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
