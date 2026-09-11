# Robin Milner（罗宾·米尔纳）立传提示词

> qid=Q92643 · 1934-01-13 – 2010-03-20 · 英国计算机科学家 · 20/21 世纪 · 1991 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1991/Robin Milner/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（ML 类型推断 / CCS 与 π 演算的通信规则的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Arthur John Robin Gorell Milner（中文惯称：罗宾·米尔纳，通称 Robin Milner）
- **生卒**：1934-01-13 生于 Yealmpton（近 Plymouth，英格兰）→ 2010-03-20 逝于 Cambridge（英格兰），享年 76（死因：心脏病发作 heart attack，页面明载）
- **国籍**：英国（British）
- **身份**：计算机科学家、理论计算机科学家
- **家庭**：出身军人家庭（military family）；妻子 Lucy 在他去世前不久离世（页面明载，细节从简勿渲染）
- **教育轨迹**：
  - 1947 年获 King's Scholarship 进入 **Eton College**（伊顿公学）
  - 1952 年获 **Tomline Prize**（伊顿数学最高奖）
  - 服役于 **Royal Engineers**（皇家工兵），军衔 Second Lieutenant（少尉）
  - **King's College, Cambridge** 本科，1957 年毕业（BA）——页面未载其博士学位，infobox 教育仅此一项
- **博士导师**：**页面未载**（infobox 无 doctoral advisor 字段）——禁写导师
- **研究领域**：计算机科学（理论计算机科学：定理证明、类型系统、并发理论）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **三大贡献总纲**：页面明载 "Milner is generally regarded as having made three major contributions to computer science"——**LCF（定理证明）、ML（语言）、并发演算（CCS 与 π 演算）**——全篇骨架即此三贡献。
2. **图灵奖（1991）**：1991 年 ACM 图灵奖；其获奖演讲题为 *Elements of Interaction*（发表于 Communications of the ACM 1993，36 卷 78–89 页）——演讲标题可引。
3. **LCF（Logic for Computable Functions）**：最早的自动定理证明工具之一——可计算函数的逻辑，交互式定理证明的鼻祖系谱起点。
4. **ML：为 LCF 而生的语言革命**：ML 最初是为 LCF 开发的元语言（Meta Language），成为**首个具有多态类型推断（polymorphic type inference）、类型安全异常处理、自动类型推断系统（algorithm W）的语言**——现代类型化函数式语言的共同祖先。
5. **Hindley–Milner 类型系统**：他"rediscovered"了 Hindley–Milner 类型系统——"重新发现"一词页面原文（rediscovering），保留该口径。
6. **CCS（calculus of communicating systems，通信系统演算，1980）**：分析并发系统的第一个理论框架；专著 *A Calculus of Communicating Systems*（Springer LNCS 92, 1980）。
7. **π 演算（π-calculus）**：CCS 的后继，支持移动性（mobility）的并发演算；专著 *Communicating and Mobile Systems: the π-Calculus*（CUP, 1999）。
8. **bigraphs（晚年的最后战场）**：临终时正在研究 bigraphs——面向普适计算（ubiquitous computing）的形式化，意图统一涵盖 CCS 与 π 演算；他提出 bigraphs 应成为"Ubiquitous Abstract Machine"，扮演冯·诺依曼机之于顺序计算的奠基角色（页面引文可标注出处）。
9. **从教师到程序员到学者**：剑桥毕业后先做**中学教师**，再入 **Ferranti** 任程序员，其后才进学界（City University, London → Swansea → Stanford）——非典型学术路径叙事。
10. **Edinburgh 与 LFCS（1973–）**：1973 年起任教 University of Edinburgh，是**计算机科学基础实验室（Laboratory for Foundations of Computer Science, LFCS）的共同创始人**。
11. **剑桥 Computer Laboratory 主任（1995）**：回归剑桥出任计算机实验室主任，后卸任但仍留在实验室；2009 年起任 Scottish Informatics & Computer Science Alliance Advanced Research Fellow 并兼任 Edinburgh 计算机科学讲席（part-time）。
12. **荣誉**：FRS 与 British Computer Society Distinguished Fellow（均 1988）、Turing Award 1991、ACM Fellow 1994、爱丁堡皇家学会 Royal Medal 2004（"bringing about public benefits on a global scale"）、NAE Foreign Associate 2008（"fundamental contributions to computer science, including the development of LCF, ML, CCS, and the π-calculus"）；**以他命名的奖项**：Royal Society Milner Award、ACM SIGPLAN Robin Milner Young Researcher Award——身后荣誉叙事点。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（定理证明 — 蓝） | `#2E5A9E` | LCF / 自动定理证明 |
| 分类色 2（类型与语言 — 青绿） | `#1E8E8E` | ML / Hindley–Milner / algorithm W |
| 分类色 3（并发演算 — 琥珀） | `#D9A441` | CCS / π 演算 / bigraphs |
| 分类色 4（学术传承 — 玫瑰） | `#C0395B` | LFCS / Cambridge / Milner Award |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏的进程通信弧线与通道节点点缀（呼应"通信演算 / 进程代数"视觉语言），克制使用。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：沉静 / 孤高（理论家的优雅独奏、三大贡献的静水深流）
- **选定曲目**：**Lonesome**（manifest 预分配，直接沿用）
- **落地文件**：`turing/presentations/Robin_Milner/Lonesome.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「并发理论之父级学者 · 英国」+ Milner 1934–2010 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1934–2010 生平纵览
4. **早年：军人家庭与伊顿岁月**（1934–1957）：King's Scholarship 1947、Tomline Prize 1952、皇家工兵少尉、剑桥国王学院 1957
5. **非典型起点：教师与 Ferranti 程序员**：中学教师 → Ferranti 编程 → 进学界（City University / Swansea / Stanford）
6. **LCF：可计算函数的逻辑**：最早自动定理证明工具之一
7. **ML：为定理证明而生的语言**：多态类型推断、algorithm W、类型安全异常处理——首个此类语言
8. **Hindley–Milner 类型系统**：一次"重新发现"（rediscovering 口径）
9. **CCS：通信系统演算**（1980）：并发系统第一框架、LNCS 92 专著
10. **π 演算：移动的并发**：CCS 后继、移动性、1999 专著
11. **bigraphs：最后的战场**：普适计算的形式化、Ubiquitous Abstract Machine 愿景
12. **Edinburgh 与 LFCS**：1973 起、实验室共同创始人；剑桥实验室主任 1995
13. **荣誉与传承**：FRS 1988、Turing 1991、Royal Medal 2004、NAE 2008；Milner Award 与 SIGPLAN Young Researcher Award 以其命名
14. **遗产**：ML→OCaml/Haskell/F# 的类型血脉、CCS/π 演算→进程代数与验证工具
15. **结尾**：76 岁、"优雅的实用主义者"（the elegant pragmatist，CACM 讣闻标题）的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：页面未给出 ACM citation 整句（只写 "he won the 1991 ACM Turing Award"）——正文表述写"因 LCF、ML、CCS、π 演算等对计算机科学的奠基性贡献获奖"时，应以 NAE 2008 授奖理由为近似锚点（页面有载），**勿杜撰图灵奖 citation 原文**。
- **三大贡献结构**：页面明载三大贡献=LCF / ML / 并发演算两框架——全篇按此骨架组织，勿自行增加"第四大贡献"。
- **ML 与 LCF 的因果关系**：ML 是**为 LCF 开发的语言**（The language he developed for LCF, ML）——勿写成独立设计的新语言项目。
- **"首个"红线**：ML 是 "the first language with polymorphic type inference, type-safe exception handling, and an automatically inferred type system"——**这三个限定词必须完整保留**，勿简写成"第一个函数式语言"或"第一个类型推断语言"。
- **Hindley–Milner 口径**：页面明载 "rediscovering the Hindley–Milner type system"——是**重新发现**（Hindley 在先），勿写成"发明"。
- **bigraphs 定位**：是"subsuming CCS 和 π 演算"的普适计算形式化，**未完成即去世**——勿写成已完成的成熟体系；"Ubiquitous Abstract Machine" 类比引语可标注出处（The Bigraphical Model 页面）。
- **学位红线**：页面仅载 King's College, Cambridge BA（1957 毕业）——**未载博士学位与博士导师**，勿编造 PhD 或导师。
- **军旅**：Royal Engineers、Second Lieutenant——一笔带过，勿渲染。
- **去世与家庭**：2010-03-20 于剑桥死于心脏病（heart attack 实载）；妻子 Lucy "died shortly before he did"——按实载一句带过，勿展开。
- **CCS/π 演算专著年份**：CCS 1980（LNCS 92）、Communication and Concurrency 1989、π 演算专著 1999、The Definition of Standard ML 1990（合作者 Mads Tofte、Robert Harper）——年份勿错位。
- **门生**：Mads Tofte（1988）、Faron Moller、Chris Tofts、Davide Sangiorgi（1993）——infobox 实载，勿添加页面未载者（如 Gordon Plotkin 是纪念文集编者非门生）。
- **引语**：页面无独立引语节——正文直接引语仅限：①NAE 2008 授奖理由；②RSE Royal Medal 2004 授奖理由（"bringing about public benefits on a global scale"）；③bigraphs 的 Ubiquitous Abstract Machine 页面引文；④CACM 讣闻标题 "the elegant pragmatist"。其余勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 米尔纳（或 罗宾·米尔纳） | 待写入 |
| name_en | Robin Milner | 待写入 |
| birth_date | 1934-01-13 | 待写入 |
| death_date | 2010-03-20 | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | theory of computer science / type theory / concurrency | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：无载禁写（页面 infobox 无 advisor 字段）
- **著名博士生**：Mads Tofte（1988，Standard ML 合作者）、Faron Moller、Chris Tofts、Davide Sangiorgi（1993，π 演算移动性方向）
- **Standard ML 合作者**：Mads Tofte、Robert Harper、David MacQueen（The Definition of Standard ML 作者群，按 collaborator 处理）
- **纪念文集编者**：Gordon Plotkin、Colin Stirling、Mads Tofte（Proof, Language, and Interaction, 2000——按纪念文集编者处理，勿写成门生）

## 8. 奖项清单

- Turing Award（1991，ACM；获奖演讲 Elements of Interaction）
- Fellow of the Royal Society（FRS，1988）
- Distinguished Fellow of the British Computer Society（DFBCS，1988）
- ACM Fellow（1994）
- Royal Medal（Royal Society of Edinburgh，2004，"bringing about public benefits on a global scale"）
- Foreign Associate of the National Academy of Engineering（NAE，2008，"fundamental contributions to computer science, including the development of LCF, ML, CCS, and the π-calculus"）
- 以其命名：The Royal Society Milner Award；ACM SIGPLAN Robin Milner Young Researcher Award

## 9. 机构清单

- 教育：Eton College（King's Scholarship 1947）、King's College, Cambridge（BA，1957 毕业）
- 任职：中学教师（毕业后）、Ferranti（程序员）、City University, London、Swansea University、Stanford University、University of Edinburgh（1973 起，LFCS 共同创始人）、University of Cambridge（Computer Laboratory 主任，1995 起）、University of Edinburgh（2009 起 part-time 讲席 + SICSA Advanced Research Fellow）

## 10. 终审清单

- [ ] 生卒 1934-01-13 / 2010-03-20，享年 76，出生地 Yealmpton，去世地 Cambridge，死因心脏病
- [ ] 图灵奖 1991，勿杜撰 ACM citation 原文
- [ ] 三大贡献骨架（LCF / ML / CCS+π）准确
- [ ] ML"首个具有多态类型推断 + 类型安全异常处理 + 自动类型推断的语言"限定词完整
- [ ] Hindley–Milner 为"重新发现"口径
- [ ] bigraphs 为"未竟事业"口径，不写成完成体系
- [ ] 无 PhD / 无博士导师（页面未载禁写）
- [ ] 国籍用「英国」，封面底部状态栏 `英国 | Cambridge · Edinburgh · LFCS | Turing 1991`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1991/Robin Milner/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Robin_Milner.jpg`（取 `Robin_Milner.jpg` 大图版；小图版 `250px-Robin_Milner.jpg`）
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须能在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Corbató / Lampson）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
