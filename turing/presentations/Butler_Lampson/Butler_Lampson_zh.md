# Butler Lampson（巴特勒·兰普森）立传提示词

> qid=Q92644 · 1943-12-23 –（在世）· 美国计算机科学家 · 20/21 世纪 · 1992 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1992/Butler Lampson/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（两阶段提交协议 / 个人计算愿景的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Butler W. Lampson（中文惯称：巴特勒·兰普森；本任务目录名为 "Butler Lampson"，manifest title 为 "Butler W. Lampson"）
- **生卒**：1943-12-23 生于 Washington, D.C.（美国）→ **在世**，卒年留白
- **国籍**：美国（American）
- **身份**：计算机科学家，分布式个人计算的开发与实现贡献者（"contributions to the development and implementation of distributed personal computing"）
- **教育轨迹**：
  - Lawrenceville School 中学（2009 年获该校最高校友奖 Aldo Leopold Award / Lawrenceville Medal）
  - **Harvard University** 物理学 A.B.（1964，magna cum laude + 学科最高荣誉）
  - **UC Berkeley** 电机工程与计算机科学 PhD（1967），论文 *Scheduling and Protection in an Interactive Multi-Processor System*
- **博士导师**：Harry Huskey
- **研究领域**：计算机科学（个人计算、分布式系统、操作系统、计算机安全）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖（1992）**："for his contributions to personal computing and computer science"——页面正文给出的获奖理由表述（"he won the prestigious ACM Turing Award for his contributions to personal computing and computer science"）。
2. **Project GENIE 与 Berkeley 分时系统**：1960 年代 UC Berkeley Project GENIE 成员；1965 年与 Peter Deutsch 等为 Scientific Data Systems 的 **SDS 940** 开发 **Berkeley Timesharing System**——分时系统的早期里程碑。
3. **Xerox PARC 创始成员（1971）**：计算机科学实验室（CSL）principal scientist（1971–1975）、senior research fellow（1975–1983）——PARC 黄金时代的核心人物。
4. **"Why Alto?" 备忘录（1972）**：其个人计算机愿景凝聚在这份著名备忘录中；**1973 年 Xerox Alto 诞生**——三键鼠标 + 整页显示器，被认为是"canonical" GUI 操作模式意义上**第一台真正的个人计算机**（页面表述："now considered to be the first actual personal computer in terms of what has become the 'canonical' GUI mode of operation"）。
5. **Wildflower 蓝图**：Alto 之后 PARC 除 Dolphin/Dorado 外的所有机器都遵循 Lampson 写的 "Wildflower" 通用蓝图（Dandelion→Xerox Star、Dandetiger、Daybreak、Dicentra 系列）——体系结构定义者角色。
6. **PARC 革命性技术群**：激光打印机设计、**两阶段提交协议**（two-phase commit，分布式事务基石）、**Bravo**（首个 WYSIWYG 文字排版程序）、**Ethernet**（首个高速局域网）——他"helped work on"（参与研发）这些技术。
7. **Euclid 语言**：他设计的多个有影响的编程语言之一（页面明载 "designed several influential programming languages such as Euclid"）。
8. **1983 年转战 DEC**：随 CSL 经理 Bob Taylor 1983 年愤然离职（acrimonious resignation），Lampson 与 Chuck Thacker 追随 Taylor 前往 DEC Systems Research Center——senior consulting engineer（1984–1986）、corporate consulting engineer（1986–1993）、senior corporate consulting engineer（1993–1995）。
9. **Microsoft Research（1995–）**：Taylor 退休前夕转投微软——architect（1995–1999）、distinguished engineer（2000–2005）、technical fellow（2005–至今）。
10. **MIT 兼职教授**：1987 年起任 MIT 电机工程与计算机科学兼职教授（adjunct professor）至今。
11. **荣誉密度极高**：NAE 1984、ACM Software System Award 1984（与 Taylor、Thacker 同获，因 Alto）、ETH Zürich 荣誉 Sc.D. 1986、Turing 1992、American Academy of Arts and Sciences Fellow 1993、ACM Fellow 1994、IEEE Computer Pioneer Award 1996、Bologna 荣誉 Sc.D. 1996、IEEE von Neumann Medal 2001、**Charles Stark Draper Prize 2004**（与 Alan Kay、Taylor、Thacker 同获，因 Alto）、NAS 2005、CHM Fellow 2006、IFIP TC11 Kristian Beckman Award 2006（信息安全）、National Cyber Security Hall of Fame 2016、**Royal Society Foreign Member 2018**。
12. **"间接层"名言的著作权归属**："Any problem in computer science can be solved with another level of indirection"——常被归于 Lampson，但**他在 1993 年图灵奖演讲中自己将此语归于 David Wheeler**——著作权归属红线，见 §5。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（个人计算 — 蓝） | `#2E5A9E` | Why Alto? / Xerox Alto / Wildflower |
| 分类色 2（分布式系统 — 青绿） | `#1E8E8E` | 两阶段提交 / 分布式事务 |
| 分类色 3（PARC 技术群 — 琥珀） | `#D9A441` | 激光打印机 / Bravo / Ethernet / Euclid |
| 分类色 4（产业迁徙 — 玫瑰） | `#C0395B` | Berkeley → PARC → DEC → Microsoft |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏的窗口矩形与层叠方块点缀（呼应"GUI / 间接层 / 系统分层"视觉语言），克制使用。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：怀旧 / 温厚（PARC 黄金年代的回望、个人计算梦的落地）
- **选定曲目**：**Nostalgy**（manifest 预分配，直接沿用）
- **落地文件**：`turing/presentations/Butler_Lampson/Nostalgy.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「个人计算先驱 · 美国」+ Lampson 1943– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1943– 在世生平纵览
4. **早年：华盛顿与哈佛物理**（1943–1964）：Lawrenceville School、Harvard 物理 A.B. 1964（magna cum laude）
5. **Berkeley 与 Project GENIE**（1964–1967）：Huskey 门下博士、交互式多处理器系统的调度与保护
6. **SDS 940 分时系统**（1965）：与 Peter Deutsch 的 Berkeley Timesharing System
7. **Xerox PARC 创始成员**（1971）：CSL principal scientist → senior research fellow
8. **"Why Alto?" 与 Xerox Alto**（1972–1973）：个人计算愿景备忘录、三键鼠标 + 整页显示器、GUI 意义上的第一台个人计算机
9. **Wildflower：PARC 机器的总蓝图**：Dandelion / Xerox Star / Daybreak 系列谱系
10. **PARC 技术群像**：激光打印机 / 两阶段提交 / Bravo（首个 WYSIWYG）/ Ethernet / Euclid（表格页）
11. **1983 转折：追随 Taylor 去 DEC**：CSL 内部变动（一笔带过勿渲染）、DEC SRC 职级年表
12. **Microsoft Research 岁月**（1995–）：architect → distinguished engineer → technical fellow；MIT 兼职教授 1987–
13. **荣誉与传承**：Turing 1992、Draper 2004、von Neumann 2001、Software System 1984、NAS/NAE/RS
14. **遗产**：Alto→GUI 时代、两阶段提交→分布式数据库、 Ethernet→网络世界
15. **结尾**：在世大师、"系统思想家"的历史地位与间接层名言的归属故事

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由口径**：页面正文表述为 "for his contributions to personal computing and computer science"——**页面无 ACM citation 独立整句**，以此表述为准，勿杜撰更长的 citation 原文。
- **在世留白**：Lampson 生于 1943-12-23，**在世**，无卒日，勿编造享年。
- **"间接层"名言归属（★ 核心红线）**："Any problem in computer science can be solved with another level of indirection"——常被归于 Lampson，但页面明载 **他在 1993 年图灵奖演讲中自己将此语归于 David Wheeler**——如引用必须写明"常被归于 Lampson，但其本人归于 Wheeler"，勿直接写成 Lampson 名言。
- **Alto 角色分工**：Lampson 是"Why Alto?"备忘录作者与 Wildflower 蓝图作者；Alto 硬件由 Thacker 等完成——页面用 "helped work on" 描述其对 PARC 技术群（激光打印机/两阶段提交/Bravo/Ethernet）的参与，**勿写成"发明了 Ethernet/激光打印机"**；Software System Award 与 Draper Prize 均为**共享**（与 Taylor、Thacker，Draper 另含 Alan Kay）——共享结构必须写明。
- **Alto "第一"的限定词**：页面明载限定是"in terms of what has become the 'canonical' GUI mode of operation"——即"在 GUI 操作模式意义上被认为是第一台真正的个人计算机"，限定词完整保留，勿简化成"第一台个人计算机"。
- **Bob Taylor 离职**：页面明载 "acrimonious resignation"（愤然离职）——一笔带过背景即可，**勿渲染 PARC 内斗细节**（页面无载）。
- **学位口径**：Harvard 是**物理** A.B.（1964）；Berkeley PhD 是**电机工程与计算机科学**（1967）——勿互换；导师 Harry Huskey。
- **Berkeley 任教年表**：assistant professor（1967–1970）→ associate professor（1970–1971）→ 1971 转投 PARC；另 1969–1971 兼任 Berkeley Computer Corporation 系统开发总监——年份勿错位。
- **Microsoft 职级年表**：architect（1995–1999）→ distinguished engineer（2000–2005）→ technical fellow（2005–present）——页面 infobox/正文口径，勿写成"退休"或"首席科学家"。
- **家庭**：页面**未载**任何家庭/婚姻信息——禁写。
- **荣誉年份**：NAE 1984、Software System Award 1984、ETH 荣誉博士 1986、Turing 1992、AAAS Fellow 1993、ACM Fellow 1994、Computer Pioneer 1996、Bologna 荣誉博士 1996、von Neumann Medal 2001、Draper 2004、NAS 2005、CHM Fellow 2006、Beckman 2006、Cyber Security Hall of Fame 2016、Royal Society Foreign Member 2018——年份与共享人勿错位。
- **引语**：页面 Quotes 节仅"间接层"一句（含 Wheeler 归属说明）——除此之外无直接引语，勿编造；Programmers at Work（Susan Lammers 编）刊有其访谈可注出处。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 兰普森（或 巴特勒·兰普森） | 待写入 |
| name_en | Butler W. Lampson | 待写入 |
| birth_date | 1943-12-23 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | personal computing / distributed systems / operating systems / computer security | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Harry Huskey（UC Berkeley）
- **SDS 940 合作者**：Peter Deutsch（Berkeley Timesharing System，1965）
- **PARC 同僚**：Chuck Thacker（Alto 硬件、共同转投 DEC）、Robert W. Taylor（CSL 经理、Software System Award 与 Draper Prize 共享人）、Alan C. Kay（Draper Prize 共享人）
- **名言著作权归属**：David Wheeler（"another level of indirection" 的原创者，Lampson 本人归于他——按"名言归属"注记处理，非合作关系）
- **注**：页面未载师承之外的门生信息，infobox 无 doctoral students 字段——勿编造门生

## 8. 奖项清单

- Turing Award（1992，"for his contributions to personal computing and computer science"）
- ACM Software System Award（1984，因 Alto，与 Robert W. Taylor、Charles P. Thacker 共享）
- NAE 院士（1984）
- ETH Zürich 荣誉 Sc.D.（1986）
- American Academy of Arts and Sciences Fellow（1993）
- ACM Fellow（1994）
- IEEE Computer Pioneer Award（1996）
- University of Bologna 荣誉 Sc.D.（1996）
- IEEE John von Neumann Medal（2001）
- Charles Stark Draper Prize（2004，因 Alto，与 Alan C. Kay、Robert W. Taylor、Charles P. Thacker 共享）
- Member of the National Academy of Sciences（NAS，2005）
- Computer History Museum Fellow（2006，"for fundamental contributions to computer science, including networked personal workstations, operating systems, computer security and document publishing"）
- IFIP TC11 Kristian Beckman Award（2006，信息安全）
- National Cyber Security Hall of Fame（2016）
- Foreign Member of the Royal Society（2018）
- Lawrenceville School Aldo Leopold Award / Lawrenceville Medal（2009，校友最高奖）

## 9. 机构清单

- 教育：Lawrenceville School、Harvard University（物理 A.B. 1964）、UC Berkeley（EECS PhD 1967）
- 任职：UC Berkeley 助理教授（1967–1970）、副教授（1970–1971）、Berkeley Computer Corporation 系统开发总监（1969–1971）、Xerox PARC CSL principal scientist（1971–1975）/ senior research fellow（1975–1983）、DEC Systems Research Center（1984–1995，三段职级）、Microsoft Research（1995–，architect → distinguished engineer → technical fellow）、MIT 兼职教授（1987–）

## 10. 终审清单

- [ ] 生卒 1943-12-23 / 在世留白，出生地 Washington, D.C.
- [ ] 图灵奖 1992 理由表述（personal computing and computer science）准确，勿杜撰 citation
- [ ] "间接层"名言归属 Lampson 本人归于 David Wheeler——必须写明
- [ ] Alto "第一"的限定词（canonical GUI mode）完整
- [ ] Ethernet/激光打印机/Bravo 为"参与研发"（helped work on），勿写成"发明"
- [ ] Software System Award 1984 与 Draper 2004 的共享人名单准确
- [ ] Bob Taylor 离职一笔带过勿渲染内斗
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Berkeley · Xerox PARC · DEC · Microsoft | Turing 1992`
- [ ] Microsoft 职级年表（1995–1999 / 2000–2005 / 2005–）准确
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1992/Butler Lampson/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Royal Society 肖像（`images/Butler_Lampson_Royal_Society_cropped_.jpg`，已裁剪人像版）；2009 PDC 圆桌照（`Professional_Developers_Conference_2009_Technical_Leaders_Panel_6.jpg`，500px 版）可作示意图备选
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**："间接层"名言必须带 Wheeler 归属说明
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Milner / Kahan）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
