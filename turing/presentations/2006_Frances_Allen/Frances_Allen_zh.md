# Frances E. Allen（弗朗西丝·艾伦）立传提示词

> qid=Q9602 · 1932-08-04 – 2020-08-04 · 美国计算机科学家 · 20 世纪 · 2006 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2006/Frances Allen/`（index.html + metadata.json + images）
> 注：目录/文件名用 `Frances_Allen`；标题可写全名 Frances E. Allen（Frances Elizabeth Allen）。

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（控制流分析 / 优化变换目录的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Frances Elizabeth Allen（中文惯称：弗朗西丝·艾伦，昵称 Fran）
- **生卒**：1932-08-04 生于 Peru, New York（美国）→ 2020-08-04 逝于 Schenectady, New York（**88 岁生日当天**去世），死因：Alzheimer's disease（阿尔茨海默病）并发症
- **国籍**：美国（American）
- **身份**：计算机科学家、优化编译器先驱（pioneer in the field of optimizing compilers）；**首位女性 IBM Fellow（1989）、首位女性图灵奖得主（2006）**——两者均页面明载可用
- **家庭**：在 Peru, NY（近 Lake Champlain）的农场长大，六个孩子中的最长者；父为农民、母为小学教师。1972 年嫁 NYU 计算机科学教授、合作者 Jacob T. Schwartz，1982 年离婚
- **教育轨迹**：
  - 小学在一间离 home 一英里的**单人教室校舍**（one-room school house）就读，后入当地高中
  - 1954 年 The New York State College for Teachers（今 University at Albany, SUNY）**数学** BS；随后在 Peru, NY 教书（代数到三角）
  - 为取得教师资格证需硕士学位，1957 年 University of Michigan **数学** MS
- **博士导师**：无 PhD，页面无载禁写
- **研究领域**：计算机科学、高性能计算、并行计算、编译器、优化编译器

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **首位女性图灵奖（2006）**：图灵奖 40 年历史上首位女性得主；该奖被视为计算的"诺贝尔奖"级荣誉。获奖后她希望这能给女性带来更多"opportunities for women in science, computing, and engineering"（页面实载的直接引语）。
2. **IBM 45 年（1957–2002）**：因学生贷款所迫加入 IBM Research（Poughkeepsie）任程序员，原计划还清贷款后回学校教书，结果留下 45 年；2002 年退休后为 Fellow Emerita。
3. **教 Fortran 起家（1957）**：入职时 Fortran 才发布两个月；她**靠读编译器源码自学**，由此萌生对设计编译器的终身研究兴趣。当时研究者认为编译语言性能不可能匹敌汇编——她后来的工作正面回击了这一常识。
4. **Harvest 与 Stretch（1959）**：被派入与美国国家安全局（NSA）合作的保密**代码破译**项目 Harvest（用于监听苏联，团队许多人直到后来媒体披露才知道详情），工作于编程语言 **Alpha**；她管理 Harvest 与更早的 Stretch 两个项目的**编译器优化团队**。
5. **与 John Cocke 的系列奠基论文**：1962 年转至 Thomas J. Watson Research Center，参与 ACS-1 项目、1970 年代参与 PL/I；与 Cocke 合作写下优化编译器的一系列开创性论文，并为 Fortran 打造了优化编译器（后支持 Autocoder 与 Alpha）。Cocke 是 1978 图灵奖得主——**艾伦比她的合作者晚 19 年获奖**（页面明载）。
6. **《Program Optimization》（1966）**：图灵奖 citation 明载——奠定程序系统性分析与变换的概念基础，引入**图论结构**编码程序内容以自动高效推导关系、发现优化机会。
7. **《Control Flow Analysis》（1970）**：与《A Basis for Program Optimization》确立 **"intervals"** 作为高效数据流分析与优化的语境。
8. **《A Catalogue of Optimizing Transformations》（与 Cocke）**：**首个**对优化变换的描述与系统化——覆盖过程内联、循环展开、公共子表达式消除、代码移动、窥孔优化等关键技术。年份注意：ACM citation 作 **1971**、正文叙述作 **1972**（正式出版 1971，见 §5）。
9. **过程间数据流分析（1973/1974）与 1976 论文**：把分析扩展到整个程序；1976 年与 Cocke 的论文描述了今日优化编译器两大主流分析策略之一。
10. **PTRAN 与自动并行化（1980–1995）**：领导 IBM 并行计算方向，主持 **PTRAN（Parallel Translator）**——按程序的依赖图自动把顺序程序变换为高效并行程序；PTRAN 团队发展了新的并行性检测方案并提出**程序依赖图（program dependence graph）**概念——多数并行化编译器的基本结构方法。并为 IBM **Blue Gene** 项目贡献软件。
11. **女性与少数群体的推动者**：在 IBM 积极推动弱势群体计算机科学家参与；1970–80 年代 IBM 编译器研究团队一半为女性，她是关键原因；长期参与 IBM mentor 计划（Barbara Simons 视其为坚定的女权主义者）。
12. **荣誉**：IBM Fellow 1989（首位女性）、Turing Award 2006、NAE 1987、NAS 2010、Computer History Museum Fellow 2000、Ada Lovelace Award 2002、Computer Pioneer Award 2004 等（详见 §8）。IBM 于 2000 年设立以她命名的 Frances E. Allen Women in Technology Mentoring Award；2020 年去世后 IEEE 创设 **Allen Medal**（第二枚以女性命名的 IEEE 奖章，2022 年首颁）。
13. **登山者的一面**：美国阿尔卑斯俱乐部（American Alpine Club）成员，在加拿大最北的 Ellesmere Island 开辟新路线。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（编译器优化 — 蓝） | `#2E5A9E` | Program Optimization / Fortran 优化编译器 |
| 分类色 2（流分析 — 青绿） | `#1E8E8E` | Control Flow Analysis / intervals / 数据流 |
| 分类色 3（并行计算 — 琥珀） | `#D9A441` | PTRAN / 程序依赖图 / Blue Gene |
| 分类色 4（女性先驱 — 玫瑰） | `#C0395B` | 首位女性 IBM Fellow / 首位女性图灵奖得主 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：流图（控制流图的节点-有向边网络），呼应「Control Flow Analysis / 图论结构编码程序」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：坚毅 / 破界（首位女性图灵奖得主、45 年 IBM 一往无前）
- **选定曲目**：Alex-Productions **Empire Collapse**（manifest 预分配，直接沿用），匹配"打破四十年禁区"的磅礴叙事。
- **落地文件**：`turing/presentations/Frances_Allen/EmpireCollapse.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「优化编译器先驱 · 首位女性图灵奖得主 · 美国」+ 艾伦 1932–2020 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1932–2020 生平纵览
4. **早年：农场与单人教室校舍**（1932–1954）：Peru, NY、六子女之长、数学教师之路
5. **数学学位与讲台**（1954–1957）：Albany BS、教代数到三角、Michigan MS
6. **IBM：从教 Fortran 开始**（1957）：Poughkeepsie、读编译器源码自学、"编译语言不可能快"的挑战
7. **Harvest 与 Stretch**（1959）：NSA 代码破译、Alpha 语言、编译器优化团队负责人
8. **Watson 与 John Cocke**（1962–）：ACS-1、PL/I、Fortran 优化编译器
9. **《Program Optimization》**（1966）：图论结构编码程序、系统性分析与变换的概念基础
10. **《Control Flow Analysis》与 intervals**（1970）：数据流分析的语境
11. **《A Catalogue of Optimizing Transformations》**（1971，与 Cocke）：优化变换的首次系统化（内联/展开/CSE/代码移动/窥孔）
12. **PTRAN 与程序依赖图**（1980–1995）：自动并行化、Blue Gene、IBM Academy 主席（1995）
13. **首位女性图灵奖**（2006）：40 年历史首位女性、获奖理由、引语"opportunities for women in science, computing, and engineering"
14. **荣誉与传承**：IBM Fellow 1989、NAE/NAS、Allen Medal、Anita Borg 的老师、鼓励女性从科
15. **结尾**：88 岁（生日当天离世）、优化编译器之母的历史地位；登山者的一面

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由（citation）**：ACM citation 为长段文字，核心句必引——`Fran Allen's work has had an enormous impact on compiler research and practice. Both alone and in joint work with John Cocke, she introduced many of the abstractions, algorithms, and implementations that laid the groundwork for automatic program optimization technology.`；并列出 1966/1970/1971/1973/1974/1976 论文与 STRETCH-HARVEST/ACS、PTRAN 的落点。勿只写"对编译器的贡献"了事。
- **两个"首位"分开写**：**首位女性 IBM Fellow（1989）**与**首位女性图灵奖得主（2006）**是两个独立事实，勿混叠；且"40 年历史首位女性"仅指图灵奖。
- **《A Catalogue of Optimizing Transformations》年份**：ACM citation 作 **1971**，正文叙述作 **1972**（正式出版 1971, Rustin 编）——**以 1971 为准**，如需可加注"正文叙述作 1972"。
- **"首位/第一"边界**：页面实载的"第一"仅限——first woman IBM Fellow、first woman Turing Award、Catalogue 是 first description and systematization of optimizing transformations、Allen Medal 是 second IEEE Medal named after a woman。**勿延伸出"编译器之母/优化之母"等页面未载的头衔式表述**（"优化编译器先驱" pioneer 有载可用）。
- **与 John Cocke**：合作者为 1978 年图灵奖得主；`Allen won the Turing award 19 years after her collaborator, John Cocke, won the same award`——"晚 19 年"可写；**任何师承/冲突/分工细节页面无载禁写**。
- **Harvest 保密性质**：项目 confidential、为监听苏联（spying on the Soviet Union）、许多人不知详情直到媒体披露——按页面实载一笔带过，**不渲染情报细节**。
- **Fortran 发布时间**：她入职时 Fortran **仅发布两个月**——勿写成"参与发明 Fortran"。
- **学历**：只有 BS（1954, Albany 前身 NY State College for Teachers）与 MS（1957, Michigan），**无 PhD**——勿写博士。
- **婚姻**：Jacob T. Schwartz（NYU 教授、合作者），1972 结婚 1982 离婚——按实载一笔带过，不渲染。
- **去世**：2020-08-04，Schenectady，**88 岁生日当天**，Alzheimer's disease 并发症——死因页面明载可写。
- **登山**：American Alpine Club 成员、Ellesmere Island 新路线——可作"另一面"小页点缀，勿夸大。
- **引语**：页面仅一句直接引语——获奖后希望带来更多 `"opportunities for women in science, computing, and engineering"`；此外**全文无其他直接引语，勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 弗朗西丝·艾伦（或 艾伦） | 待写入 |
| name_en | Frances E. Allen | 待写入 |
| birth_date | 1932-08-04 | 待写入 |
| death_date | 2020-08-04 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | optimizing compilers / high-performance computing / parallel computing | 待写入 |
| has_biography | 1 | 入库时置 1 |

## 7. 社会关系入库清单

- **合作者**：John Cocke（IBM Watson、优化编译器系列论文与 Catalogue 合著；1978 图灵奖得主，type=collaborator）
- **配偶（已离异）**：Jacob T. Schwartz（NYU 计算机科学教授、合作者；type=spouse，注 1972–1982）
- **门生**：Anita Borg（Allen 是 Borg 研究生阶段唯一的女性教授——页面实载）
- **博士导师**：无 PhD，禁写

## 8. 奖项清单

- IBM Fellow（1989，首位女性）
- Fellow of the American Academy of Arts and Sciences（1994）；ACM Fellow（1994）
- IEEE Computer Society Charles Babbage Award（1997）；WITI Hall of Fame（1997）
- Computer History Museum Fellow（2000，"for her contributions to program optimization and compiling for parallel computers"）
- American Philosophical Society 会员（2001）
- Augusta Ada Lovelace Award（Association for Women in Computing，2002）
- ABIE Award for Technical Leadership（Anita Borg Institute，2004）
- IEEE Computer Society Computer Pioneer Award（2004）
- A.M. Turing Award（2006，首位女性）
- McGill University 荣誉理学博士（2009，"pioneering contributions to the theory and practice of optimizing compiler techniques…"）
- National Academy of Engineering 院士（1987）；National Academy of Sciences 院士（2010）
- IEEE Allen Medal（2020 年创设于其去世后，第二枚以女性命名的 IEEE 奖章，2022 年首颁——列入"以她命名"条目）

## 9. 机构清单

- 教育：The New York State College for Teachers（今 University at Albany, SUNY；数学 BS 1954）；University of Michigan（数学 MS 1957）
- 任职：IBM Research, Poughkeepsie 程序员（1957 起）；Harvest/Stretch 编译器优化团队负责人（1959–）；Thomas J. Watson Research Center（1962–）；IBM 并行计算负责人（1980–1995）；IBM Academy 主席（1995）；IBM 退休（2002，Fellow Emerita）；NYU 兼职副教授（1970–71 学术休假后数年）；Stanford 学术休假（1977）；Berkeley Chancellor's Distinguished Lecturer & Mackay Lecturer、UCSD Regents Lecturer

## 10. 终审清单

- [ ] 生卒 1932-08-04 / 2020-08-04（88 岁生日当天），出生地 Peru NY，去世地 Schenectady NY，死因 Alzheimer's 并发症
- [ ] 两个"首位"分开写：首位女性 IBM Fellow（1989）≠ 首位女性图灵奖（2006）
- [ ] Catalogue 年份以 1971 为准（ACM citation 口径）
- [ ] 图灵奖 citation 核心句整句引用，论文年份序列 1966/1970/1971/1973/1974/1976 准确
- [ ] 与 Cocke"晚 19 年获奖"表述准确，无师承/恩怨编造
- [ ] Harvest 保密背景一笔带过不渲染；Fortran"发布仅两个月"不写成参与发明
- [ ] 无 PhD；BS 1954 / MS 1957 准确
- [ ] 引语仅一句（opportunities for women…），无编造引语
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | IBM | Turing 2006`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2006/Frances Allen/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 infobox 肖像（`images/500px-Allen_mg_2528-3750K-b.jpg`；另一张 `500px-Allen_mg_2545-b.jpg` 备用）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅 opportunities for women… 一句 + ACM citation 整段）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2005–2007 批次（Naur / Clarke / Emerson / Sifakis）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
