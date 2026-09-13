# Charles P. Thacker（查尔斯·撒克尔）立传提示词

> qid=Q92828 · 1943-02-26 – 2017-06-12 · 美国计算机设计师 · 20/21 世纪 · 2009 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2009/Charles P. Thacker/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。（本篇**无博士师承**，网格中"师承"栏写最高学历院校即可。）
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Alto 硬件架构 / Ethernet 分组广播的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Charles Patrick "Chuck" Thacker（中文惯称：查尔斯·"查克"·撒克尔 / 塔克）
- **生卒**：1943-02-26 生于 Pasadena（加利福尼亚州，美国）→ 2017-06-12 逝于 Palo Alto（加利福尼亚州），享年 74；死因：食道癌并发症（页面明载 "complications from esophageal cancer"）
- **国籍**：美国（American）
- **身份**：计算机设计先驱（"pioneer computer designer"）；Xerox PARCComputer Systems Laboratory 核心人物；Microsoft Technical Fellow
- **家庭**：父 Ralph Scott Thacker（1906 年生，Caltech 1928 届，航空业电气工程师）；母（Mattie）Fern Cheek（1922 年生于 Oklahoma，出纳兼秘书，早年独立抚养两个儿子）
- **教育轨迹**：UC Berkeley **物理学** BS（1967）——本科物理出身，无更高学位
- **师承**：无（无博士学历，勿编造导师）
- **研究领域**：计算机体系结构、个人计算机、局域网（Ethernet）、平板计算机

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **Xerox Alto 的设计者（项目负责人）**：首台采用**鼠标驱动图形用户界面（GUI）**的计算机——Thacker 任 Alto 个人计算机系统的 project leader；图灵奖核心贡献。
2. **图灵奖 2009（2010 年公布）**：ACM 表彰其 "pioneering design and realization of the Alto, the first modern personal computer"，以及 "contributions to the Ethernet and the tablet computer"——三大关键词：Alto / Ethernet / tablet computer。
3. **Ethernet 共同发明人**：1970s 在 PARC 与他人共同发明以太局域网（LAN）。
4. **激光打印机**：参与世界首台激光打印机的诸多项目（"contributed to many other projects, including the first laser printer"）。
5. **Project Genie 起点（1968）**：加入 Berkeley "Project Genie"，参与开发 SDS 940 上的开创性 **Berkeley Timesharing System**——分时系统是 Alto 之前的技术底座。
6. **Berkeley Computer Corporation（BCC）**：与 Butler Lampson 等人离开 Berkeley 组建 BCC，Thacker 设计处理器与存储系统；BCC 商业上不成功，但这批人成为 Xerox PARC 计算机系统实验室的核心技术班底。
7. **DEC Systems Research Center（1983）**：DEC SRC 的创始人之一。
8. **Microsoft Research（1997）**：帮助建立 Microsoft Research Cambridge（英国剑桥）；回美后设计 Microsoft **Tablet PC** 硬件——灵感来自 PARC 的 "interim Dynabook" 经验与他在 DEC SRC 的笔式手持机 Lectrice。
9. **RAMP 与 RISC-V 渊源（2006–2010）**：Berkeley RAMP 项目（基于 BEE FPGA 平台）研究贡献者；RISC-V 的动因之一正是 RAMP 缺少开源处理器设计（页面明载 Asanovic 与 Patterson 为 PI、Thacker "played a role in this important future technology"）。
10. **Alan Kay 的评价（可直接引用）**："This guy is a real genius ... We don't like to sling that word around in our field, but he is one. He is magic."（Kay 与 Thacker 同为 PARC 同事兼图灵奖得主，WSJ 报道）
11. **荣誉**：Turing Award 2009、Draper Prize 2004（与 Kay/Lampson/Taylor 四人共享）、IEEE von Neumann Medal 2007、Computer History Museum Fellow 2007、Eckert–Mauchly Award 2017（身后追授）、ETH 荣誉博士。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（个人计算机 — 蓝） | `#2E5A9E` | Xerox Alto / Tablet PC |
| 分类色 2（网络 — 青绿） | `#1E8E8E` | Ethernet / 局域网 |
| 分类色 3（体系结构 — 琥珀） | `#D9A441` | SDS 940 分时 / BCC 处理器 / RAMP |
| 分类色 4（打印与外设 — 玫瑰） | `#C0395B` | 激光打印机 / Lectrice |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「一台桌面机器点亮整个图形时代」的硬件美学。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：开阔 / 器物史诗（Alto、Ethernet——现代个人计算的硬件起点）
- **选定曲目**：Alex-Productions **Mirage**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Charles_P._Thacker/Mirage.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「首台现代个人计算机设计者 · 美国」+ Thacker 1943–2017 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1943–2017 生平纵览
4. **早年：Pasadena 与 Berkeley 物理**（1943–1967）：航空业电气工程师之子、母亲独立抚养、BS 物理学位
5. **Project Genie：分时系统的洗礼**（1968–）：SDS 940、Berkeley Timesharing System
6. **BCC： processor 与存储的设计者**（1970s 初）：与 Lampson 同行、BCC 虽败而班底入 PARC
7. **Xerox Alto：第一台现代个人计算机**（1970s）：project leader、鼠标驱动 GUI
8. **Ethernet：共同发明局域网**：以太网 LAN
9. **PARC 的更多奇迹**：首台激光打印机等诸多项目
10. **DEC SRC（1983）与 Lectrice**：创立 SRC、笔式手持计算机
11. **Microsoft（1997–）**：MSR Cambridge、Tablet PC 硬件、Technical Fellow
12. **RAMP 与 RISC-V 渊源**（2006–2010）：BEE/BEE2/BEE3 FPGA、开源处理器缺位催生 RISC-V
13. **荣誉与传承**：Turing 2009、Draper 2004、von Neumann 2007、Eckert–Mauchly 2017（追授）
14. **遗产**：GUI 个人机、以太网、平板电脑——三项图灵奖关键词的当代回响
15. **结尾**：74 岁、"Chuck" 的工程师一生与 Alan Kay 的评价

## 5. 史实陷阱与敏感点（终审必须检查）

- **"first modern personal computer" 与 "first computer with mouse-driven GUI" 是两句不同表述**：ACM citation 用 "the first modern personal computer"；正文开头用 "the first computer that used a mouse-driven graphical user interface"——两处都可用，但勿混成"第一台 GUI 计算机即第一台现代 PC"的等同句式，按上下文分别引用。
- **Ethernet 是"共同发明"（co-inventor）**：页面原文 co-inventor of the Ethernet LAN——**勿写 Thacker 独自发明以太网**（通常并列的 Metcalfe/Boggs 等人名本页未展开，勿自行补写他人名字到发明人名单）。
- **激光打印机**：只写 "contributed to ... the first laser printer"（参与贡献），**勿写"发明了激光打印机"**。
- **图灵奖年份口径**：获奖为 **2009** 年度，**2010 年**由 ACM 公布——封面写 2009，可注"2010 年公布"。
- **学位**：仅 UC Berkeley 物理 BS（1967）；**无硕士、无博士、无导师**——勿编造研究生学历（页面另提 ETH 荣誉博士，是荣誉学位非学历，勿混入教育栏）。
- **RISC-V 表述**：页面说 RISC-V 发展的动因是 RAMP 项目缺少开源处理器设计（both Asanovic and Patterson were PIs），Thacker "played a role"——写"间接渊源/扮演角色"即可，**勿写 Thacker 参与 RISC-V 设计**。
- **死因**：食道癌并发症，页面明载可写；享年 74。
- **Draper Prize 四人共享**：与 Alan C. Kay、Butler W. Lampson、Robert W. Taylor 四人共享（2004）——写明共享结构。
- **Eckert–Mauchly Award 2017**：ACM/IEEE-CS 为**已故**的 Thacker 授予 2017 年奖（身后追授）——可写"身后追授"。
- **引语**：全文仅 Alan Kay 对 Thacker 的评价（WSJ 报道内）是可直接引用的话语；Thacker 本人**无直接引语，勿编造**。
- **名字拼写**：中文译名用「查尔斯·撒克尔」或「查尔斯·塔克」其一，全篇统一；"Chuck" 昵称可保留半角引号。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 查尔斯·撒克尔（或 查尔斯·塔克，全篇统一） | 待写入 |
| name_en | Charles P. Thacker | 待写入 |
| birth_date | 1943-02-26 | 待写入 |
| death_date | 2017-06-12 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer designer | 待写入 |
| field_of_work | computer architecture / personal computing / Ethernet / tablet computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **长期同事**：Butler Lampson（Project Genie/BCC/PARC/SRC 多度共事，非导师非学生）、Alan Kay（PARC 同事 + Draper Prize 共享 + 评价者）、Robert W. Taylor（Draper Prize 共享）
- **页面无载的师承/门生**：**无载禁写**（页面无 doctoral advisor/students 字段，关系库不得杜撰）
- **机构同事（叙事可写、关系库慎入）**：Metcalfe/Boggs 等 Ethernet 合作者本页未点名，勿入关系库

## 8. 奖项清单

- A.M. Turing Award（2009 年度，2010 年公布：Alto + Ethernet + tablet computer）
- Charles Stark Draper Prize（2004，与 Alan C. Kay、Butler W. Lampson、Robert W. Taylor 共享）
- IEEE John von Neumann Medal（2007）
- Computer History Museum Fellow（2007，颁奖词 "leading development of the Xerox PARC Alto, and for innovations in networked personal computer systems and laser printing technologies"）
- Eckert–Mauchly Award（2017，身后追授）
- ACM Fellow（1994）；UC Berkeley 计算机科学杰出校友（1996）
- 瑞士联邦理工学院（ETH）荣誉博士

## 9. 机构清单

- 教育：UC Berkeley（物理 BS，1967）
- 任职：Project Genie, UC Berkeley（1968 起）→ Berkeley Computer Corporation（处理器与存储）→ Xerox PARC Computer Systems Laboratory（1970s–1980s，Alto 项目负责人）→ DEC Systems Research Center 创始人（1983）→ Microsoft Research（1997 起，协助建立 MSR Cambridge；后返美设计 Tablet PC；Technical Fellow；2006–2010 兼 Berkeley RAMP 研究贡献者）

## 10. 终审清单

- [ ] 生卒 1943-02-26 / 2017-06-12，享年 74，死因食道癌并发症，出生地 Pasadena、去世地 Palo Alto
- [ ] 图灵奖理由含 "the first modern personal computer"（Alto）+ Ethernet + tablet computer 三关键词，2009 年度/2010 公布口径正确
- [ ] Ethernet 为 co-inventor（共同发明），激光打印机为"参与贡献"
- [ ] 学历仅 Berkeley 物理 BS 1967，无研究生学位、无师承
- [ ] Draper Prize 四人共享（Kay/Lampson/Thacker/Taylor）
- [ ] Eckert–Mauchly 2017 写明身后追授
- [ ] RISC-V 仅写"间接渊源/played a role"，勿写参与设计
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Xerox PARC · DEC SRC · Microsoft | Turing 2009`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2009/Charles P. Thacker/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2008 年肖像（`images/Chuckthacker_cropped_.jpg`，已就绪；原文写 500px-Chuckthacker_cropped_.jpg 与实际文件名不符，执行时已按实际文件纠正）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅 Alan Kay 评价语可引用（WSJ），Thacker 本人无直接引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Liskov / Valiant）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
