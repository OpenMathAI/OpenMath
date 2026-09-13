# Niklaus Wirth（尼克劳斯·维尔特）立传提示词

> qid=Q92604 · 1934-02-15 – 2024-01-01 · 瑞士计算机科学家 · 20 世纪 · 1984 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1984/Niklaus Wirth/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 Pascal / 模块化 / 渐进求精的表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Niklaus Emil Wirth（中文惯称：尼克劳斯·维尔特；读音 IPA /vɛrt/）
- **生卒**：1934-02-15 生于瑞士温特图尔（Winterthur, Switzerland）→ 2024-01-01 逝于苏黎世（Zürich, Switzerland），享年 89（元旦当日去世，正文明载）
- **国籍**：瑞士（Swiss）
- **身份**：计算机科学家、程序设计语言设计大师、软件工程先驱
- **家庭**：父 Walter Wirth（中学教师）、母 Hedwig（née Keller）；子女 3 人（据 1979 年 Electronics 杂志 profile：两女一男）
- **教育轨迹**：
  - 1954–1958 年 ETH Zürich（苏黎世联邦理工学院）**电子工程**学士（B.S.）
  - 1960 年 Université Laval（拉瓦尔大学，加拿大魁北克）**硕士**（M.Sc.）
  - 1963 年 UC Berkeley **电气工程与计算机科学（EECS）博士**，论文 *A Generalization of Algol*
- **博士导师**：正文明确"supervised by computer design pioneer **Harry Huskey**"；infobox 同时列 **Edward Feigenbaum**——两说并存，正文只提 Huskey，以正文为准（infobox 两人均列，写"Huskey（正文明载）；infobox 另列 Feigenbaum"）
- **研究领域**：程序设计语言、软件工程、编译器、操作系统、数字硬件设计

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 1984**：获奖理由整句引用——"for developing a sequence of innovative computer languages"（因其开发的一系列创新计算机语言）；正文明言图灵奖是"generally recognized as the highest distinction in computer science"。
2. **语言谱系一以贯之**：首席设计师生涯纵览——Euler（1965）、PL360（1966）、ALGOL W（1966）、**Pascal（1970）**、Modula（1975）、Modula-2（1978）、Oberon（1987）、Oberon-2（1991）、Oberon-07（2007）——一条"简化"主线贯穿 40 余年。
3. **从 ALGOL 标准之争到个人语言**：作为 IFIP WG 2.1（Algorithmic Languages and Calculi）成员参与 ALGOL 60 / ALGOL 68 标准制定，因对标准委员会讨论感到失望（frustrated），转而以**个人工作**形式发表 Pascal、Modula-2、Oberon——这是"简化哲学"的起源叙事。
4. **Pascal（1970）**：代表作，成为 1970–80 年代欧美教学与实现的基础语言；1974 年与 Kathleen Jensen 合著 *The Pascal User Manual and Report*，成为众多语言实现（如 BSD Pascal）的蓝本。
5. **渐进求精（Stepwise Refinement, 1971）**：*Program Development by Stepwise Refinement*（CACM 1971 年 4 月）被认为是软件工程经典、最早正式提出程序设计**自顶向下方法**的著作；被 Fred Brooks 在《人月神话》中讨论，ACM 图灵奖小传称之为 "seminal"。
6. **Algorithms + Data Structures = Programs（1975）**：广受认可的名著；1986 与 2004 年修订改题为 *Algorithms & Data Structures*（示例语言依次由 Pascal 换为 Modula-2、Oberon）。
7. **系统构建者**：不只是语言设计者——操作系统 Medos-2（1983，Lilith 工作站）与 Oberon 系统（1987，Ceres 工作站）的设计实现团队成员；Oberon 操作系统完整文档由 Wirth 与 Jürg Gutknecht 于 1992 年出版（*Project Oberon*）；硬件描述语言 Lola（1995）。
8. **ETH Zürich 教授生涯**：1963–1967 年任 Stanford 与 University of Zürich 助理教授；1968 年任 ETH Zürich 信息学教授；1976–1977 与 1984–1985 两度在 Xerox PARC 学术休假；1999 年退休。
9. **Wirth's law（维尔特定律）**：1995 年论文 *A Plea for Lean Software* 中转述 Martin Reiser 的说法并使之流行："Software is getting slower more rapidly than hardware becomes faster."（软件变慢的速度快于硬件变快的速度）——注意：这是**转述 Reiser**，勿写成 Wirth 原创。
10. **教学著作**：1973 年 *Systematic Programming: An Introduction*（被 1974 年书评认为面向把算法构造视为数学训练一部分的读者）。
11. **荣誉与小行星**：IEEE Emanuel R. Piore Award（1983）、Marcel Benoist Prize（1989）、ACM Fellow（1994）、ACM SIGSOFT Outstanding Research Award（1999）、SIGPLAN Programming Languages Achievement Award、Computer History Museum Fellow（2004，理由含 Euler/Algol-W/Pascal/Modula/Oberon）；小行星 21655 Niklauswirth 以其命名。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（程序设计语言 — 蓝） | `#2E5A9E` | Pascal / Euler / ALGOL W / Modula / Oberon 谱系 |
| 分类色 2（软件工程 — 青绿） | `#1E8E8E` | 渐进求精 / Stepwise Refinement |
| 分类色 3（系统构建 — 琥珀） | `#D9A441` | Lilith / Oberon 系统 / Lola |
| 分类色 4（工程哲学 — 玫瑰） | `#C0395B` | Wirth's law / 简化哲学 / Lean Software |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏同心圆环（递归/嵌套结构），呼应「Pascal → Modula → Oberon 一脉相承的简化谱系」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：沉稳 / 构建（一以贯之的语言谱系、瑞士式的严谨与简化）
- **选定曲目**：Alex-Productions **Through the Darkness**（manifest 预分配，直接沿用），匹配"从 ALGOL 标准之争的暗流中走出、自建一套语言谱系"的叙事。
- **落地文件**：`turing/presentations/Niklaus_Wirth/ThroughTheDarkness.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「Pascal 之父 · 瑞士」+ 维尔特 1934–2024 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1934–2024 生平纵览
4. **温特图尔的少年与 ETH 求学**（1934–1960）：中学教师之子、ETH 电子工程、Laval 硕士
5. **Berkeley 博士与 ALGOL 结缘**（1960–1963）：Huskey 门下、论文 A Generalization of Algol
6. **Stanford / Zürich 助理教授与 IFIP WG 2.1**（1963–1968）：ALGOL 60/68 标准、委员会失望、Euler/PL360/ALGOL W
7. **Pascal 诞生**（1970）：个人语言路线、Jensen 合著 User Manual and Report（1974）
8. **渐进求精**（1971）：Stepwise Refinement、自顶向下、Brooks《人月神话》讨论
9. **ETH 教授与 Modula-2**（1968–1980s）：Modula（1975）、Modula-2（1978）
10. **系统构建：Lilith 与 Oberon**（1983–1987）：Medos-2、Ceres、Project Oberon、Gutknecht
11. **图灵奖 1984**：获奖理由整句引用、Xerox PARC 学术休假背景
12. **Wirth's law 与 Lean Software**（1995）：转述 Reiser、A Plea for Lean Software
13. **荣誉与传承**：Piore 1983、Benoist 1989、CHM Fellow 2004、门生 Martin Odersky / Michael Franz、小行星 21655
14. **遗产**：Pascal 家族对教学与工程的影响、简化哲学
15. **结尾**：89 岁、元旦辞世、"a sequence of innovative computer languages"的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：整句引用 "for developing a sequence of innovative computer languages"——是"一系列语言"的整体理由，勿单独挂在 Pascal 名下。
- **博士导师两说**：正文只写 Harry Huskey；infobox 另列 Edward Feigenbaum。写法："导师 Huskey（正文明载），infobox 另列 Feigenbaum"——勿只写 Feigenbaum，也勿断言二选一。
- **Wirth's law 出处**：Wirth 是**转述/流行化者**（1995 *A Plea for Lean Software* 中将此话归于 Martin Reiser 的表述），勿写成 Wirth 原创。
- **ALGOL 标准与个人语言的关系**：因 IFIP 标准委员会讨论失望而将后续语言作为**个人工作发表**——保留这一因果，勿写成"被 ALGOL 68 委员会开除"之类页面无载情节。
- **语言年份红线**：Euler 1965、PL360 1966、ALGOL W 1966、Pascal 1970、Modula 1975、Modula-2 1978、Oberon 1987、Oberon-2 1991、Oberon-07 2007——勿把 PL360 / ALGOL W 与 Pascal 混年。
- **Oberon 三重身份**：Oberon 既是语言（1987）也是操作系统（1987，Ceres 工作站）——分清"语言 Oberon"与"Oberon 系统/OS"，勿混写。
- **Medos-2 与 Oberon OS**：Medos-2（1983）是 Lilith 工作站的 OS、Knudsen 的博士论文（Wirth 概念统筹）；Oberon OS（1987）配 Ceres——勿把 Medos-2 写成 Wirth 独立写成或挂在 Ceres 上。
- **生卒**：1934-02-15 冬季图尔 → 2024-01-01 苏黎世，享年 89，元旦去世（正文明载），死因未详述勿编造。
- **家庭**：父为中学教师、母 Hedwig；子女 3 人（1979 杂志 profile 的两女一男）——细节仅一笔带过，勿渲染。
- **退休年份**：1999 年从 ETH 退休；两度 Xerox PARC 学术休假（1976–1977、1984–1985）——勿把 PARC 写成任职。
- **荣誉**：Piore 1983、Turing 1984、Benoist 1989、ACM Fellow 1994、SIGSOFT ORA 1999、CHM Fellow 2004、SIGPLAN PLAA——**无** National Medal（勿编造）。
- **引语红线**：页面正文无 Wirth 本人直接引语；可引用的只有①图灵奖理由（ACM citation）、②CHM Fellow 理由（"for seminal work in programming languages and algorithms..."）、③Wirth's law 那句（须注明转述 Martin Reiser）。其余勿编造引语。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 维尔特（或 尼克劳斯·维尔特） | 待写入 |
| name_en | Niklaus Wirth | 待写入 |
| birth_date | 1934-02-15 | 待写入 |
| death_date | 2024-01-01 | 待写入 |
| nationality | Switzerland | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | programming languages / software engineering / compilers / operating systems | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Harry Huskey（UC Berkeley，计算机设计先驱；infobox 另列 Edward Feigenbaum，两说并存）
- **IFIP WG 2.1 同仁**：ALGOL 60/68 标准工作组（页面无具体人名，勿编造具体同仁）
- **合著者**：Kathleen Jensen（Pascal User Manual and Report）、Jürg Gutknecht（Project Oberon）、Martin Reiser（Programming in Oberon）
- **著名博士生**：Martin Odersky（Scala 设计者）、Michael Franz（页面 infobox 实载两名）
- **著作影响圈**：Fred Brooks（《人月神话》讨论其 1971 论文，非师承关系）

## 8. 奖项清单

- Turing Award（1984，"for developing a sequence of innovative computer languages"）
- IEEE Emanuel R. Piore Award（1983）
- Marcel Benoist Prize（1989，瑞士）
- ACM Fellow（1994）
- ACM SIGSOFT Outstanding Research Award（1999）
- SIGPLAN Programming Languages Achievement Award（年份页面未载，勿写具体年份）
- Computer History Museum Fellow（2004）

## 9. 机构清单

- 教育：ETH Zürich（电子工程 B.S. 1958）、Université Laval（M.Sc. 1960）、UC Berkeley（EECS PhD 1963）
- 任职：Stanford University 助理教授（1963–1967 期间）、University of Zürich 助理教授（1963–1967 期间）、ETH Zürich 信息学教授（1968–1999 退休）、Xerox PARC 学术休假（1976–1977、1984–1985）

## 10. 终审清单

- [ ] 生卒 1934-02-15 / 2024-01-01，享年 89，出生地 Winterthur，去世地 Zürich
- [ ] 图灵奖理由整句引用 "for developing a sequence of innovative computer languages"
- [ ] 博士导师写 Huskey（正文）+ infobox 另列 Feigenbaum 的两说口径
- [ ] Wirth's law 标注"转述 Martin Reiser"，不写 Wirth 原创
- [ ] 语言谱系年份逐一对表（Euler 1965 / PL360 1966 / ALGOL W 1966 / Pascal 1970 / Modula 1975 / Modula-2 1978 / Oberon 1987 / Oberon-2 1991 / Oberon-07 2007）
- [ ] Oberon 语言 vs Oberon 系统两重身份分清；Medos-2=1983/Lilith，Oberon OS=1987/Ceres
- [ ] IFIP WG 2.1"失望→个人语言"因果保留，不加戏
- [ ] 国籍用「瑞士」，封面底部状态栏 `瑞士 | ETH Zürich · Stanford · Berkeley | Turing 1984`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1984/Niklaus Wirth/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Niklaus_Wirth_UrGU.jpg`（UrGU 2005 年照片，infobox "Wirth in 2005" 同源；备用 `Niklaus_Wirth_large.jpg`）
- [ ] **国籍**：封面顶部徽章明示瑞士
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅限 §5 列出的三处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Karp / Hopcroft / Tarjan）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
