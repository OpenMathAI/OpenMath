# Robert Kahn（罗伯特·卡恩）立传提示词

> qid=Q4212034 · 1938-12-23 – 在世留白 · 美国互联网先驱、计算机科学家 · 20/21 世纪 · 2004 图灵奖（与 Vint Cerf 共享）
> 本地 Wikipedia 数据源：`turing/pages/2004/Robert Kahn/`（index.html + metadata.json + images）

> ✅ **数据源已修复（主控更新）**：本地已按正确标题补抓完整条目 `turing/pages/2004/Robert Kahn (computer scientist)/`（index.html + metadata.json + images/，含 `500px-Bob_Kahn.jpg` 真实肖像）。本提示词事实基准现以**该本地页面为准**；Review-1 直接用本地页面逐条核对，若本地与提示词冲突以本地为准并回写本文件。

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（TCP/IP 分层架构 / 数字对象架构的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Robert Elliot Kahn（中文惯称：罗伯特·卡恩；昵称 Bob Kahn）
- **生卒**：1938-12-23 生于纽约市（正文注明布鲁克林 Brooklyn，美国）；在世，卒年留白
- **国籍**：美国（American）
- **身份**：互联网先驱（TCP/IP 共同发明人、ARPANET 首席架构师、CNRI 创立者），与 Vint Cerf 并称 "the fathers of the Internet"
- **家庭**：犹太裔（阿什肯纳兹）家庭，父母 Beatrice Pauline（本姓 Tashker）与 Lawrence Kahn；通过父亲与未来学家 Herman Kahn 有亲缘关系；妻子 Patrice Ann Lyons
- **教育轨迹**：
  - City College of New York（CCNY）**电气工程**学士（1960）
  - Princeton University **文学硕士**（1962）+ **电气工程博士**（1964），论文 *Some problems in the sampling and modulation of signals*
- **博士导师**：Bede Liu（刘必治，普林斯顿）
- **研究领域**：电信、计算机网络（infobox Fields）
- **任职轨迹**：Bell Labs → MIT → **BBN**（ARPANET 时期）→ **DARPA IPTO**（1972 起，后任主任）→ **CNRI**（1986 创立，截至 2022 年任董事长、CEO 兼总裁）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **ARPANET 的首席架构师（BBN 时期）**【本篇侧重支柱】：在 Bolt Beranek and Newman（BBN）任内是 **ARPANET 的主要设计者**——ARPANET 项目管理与系统架构是 Kahn 的底色。
2. **1972 ICCC：分组交换的"分水岭时刻"**：1972 年秋在国际计算机通信大会（ICCC）上公开展示 ARPANET，连接 20 台不同的计算机——Kahn 的页面实载引语称之为 "the watershed event that made people suddenly realize that packet switching was a real technology"（本篇唯一的直接引语，整句引用）。
3. **TCP 的最初构想者**：在 SATNET 卫星分组网络项目工作期间提出 TCP 最初构想，意在**取代 ARPANET 当时的 NCP 协议**；设计目标：网关（今称路由器）转发分组、无单点故障、序列号排序与丢包检测、ACK 确认、超时重传、校验和。**1973 年春 Vint Cerf 加入**，共同完成早期 TCP 版本；后协议拆分为两层——TCP 管主机到主机、IP 管网际互联。
4. **1974 IEEE 奠基论文**：与 Cerf 在 IEEE Transactions on Communications 发表 *A Protocol for Packet Network Intercommunication*（1974-05）——与 Cerf 篇共享口径。
5. **DARPA IPTO 主任与战略计算计划**：1972 年加入 DARPA 信息处理技术办公室（IPTO）；任 IPTO 主任期间启动美国政府的**战略计算计划（Strategic Computing Initiative）**——美国联邦政府迄今最大的计算机研发项目（十亿美元级）。在 DARPA 工作 13 年。
6. **CNRI（1986 创立）**：创立 Corporation for National Research Initiatives 并长期执掌——数字图书馆（Digital Libraries）、Knowledge Robots、千兆网络的早期推动（与 Cerf 共事）；数字对象基础设施与数字知识产权保护技术是其 ACM Fellow 表彰语中的关键词。
7. **互联网协会（ISOC，1992）**：与 Cerf 等共同创立 Internet Society——**首任主席是 Cerf**（Cerf 篇口径），Kahn 篇写"共同创立"。
8. **1988-1997 国家技术奖章与领导力**：1997-12 与 Cerf 同获 National Medal of Technology（Clinton 总统颁发，"for creating and sustaining development of Internet Protocols and continuing to provide leadership in the emerging industry of internetworking."——整句引用）。
9. **荣誉之殿**：图灵奖 2004、Marconi Prize 1994、Draper Prize 2001（回退源口径）、总统自由勋章 2005、Queen Elizabeth Prize for Engineering 2013（首届五位得主之一）、**IEEE Medal of Honor 2024**（"Pioneering technical and leadership contributions in packet communication technologies and foundations of the Internet"）。
10. **院士与会士**：IEEE Fellow（1981，因分组交换移动无线电通信的原创工作）、NAE 院士（1987）、AAAI 创始会士（1990）、ACM Fellow（2001）。
11. **产业参与**：曾任 Qualcomm（高通）董事。
12. **学术谱系**：博士导师 Bede Liu；**页面正文无学生章节、无博士生列表**——社会关系入库时"门生"一栏明写"页面无载"。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（ARPANET 与网络架构 — 蓝） | `#2E5A9E` | BBN 架构师 / 1972 ICCC |
| 分类色 2（TCP/IP 协议设计 — 青绿） | `#1E8E8E` | TCP 构想 / 1974 IEEE 论文 |
| 分类色 3（DARPA 与战略计算 — 琥珀） | `#D9A441` | IPTO 主任 / 战略计算计划 |
| 分类色 4（CNRI 与数字对象 — 玫瑰） | `#C0395B` | 数字图书馆 / 数字对象基础设施 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和网关节点拓扑（稀疏圆点 + 连线），呼应「网关转发、无单点故障」的互联网架构视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：深沉 / 长夜行军（ARPANET 暗夜架网到战略计算的宏观管理者气质）
- **选定曲目**：Alex-Productions **Through the Darkness**（manifest 预分配，直接沿用；与化学家 Moissan 篇同曲，属跨项目正常复用）。
- **落地文件**：`turing/presentations/Robert_Kahn/ThroughTheDarkness.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「互联网之父 · ARPANET 架构师 · 美国」+ Kahn 1938– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域 / 家庭）
3. **时间线**（`\timelineslide`）：1938– 生平纵览
4. **早年与教育**：布鲁克林犹太家庭、CCNY 电机工程（1960）、普林斯顿硕博（1962/1964，Bede Liu 门下，信号采样与调制）
5. **Bell Labs → MIT → BBN**：进入 ARPANET 主战场
6. **ARPANET 首席架构师**：BBN 时期的项目管理与系统架构
7. **1972 ICCC：分水岭时刻**：20 台机器的公开展示（整句引语页）
8. **TCP 的最初构想（SATNET 期）**：取代 NCP、网关转发、无单点故障——TCP/IP 分层
9. **与 Cerf 的双引擎**：1973 春 Cerf 加入、1974 IEEE 论文、DoD TCP/IP
10. **DARPA IPTO 主任**：战略计算计划——十亿美元级联邦项目
11. **CNRI（1986–）**：数字图书馆、Knowledge Robots、数字对象基础设施
12. **ISOC 与互联网治理**：1992 共同创立（首任主席是 Cerf）
13. **荣誉之殿**：Turing 2004、Marconi 1994、国家技术奖章 1997、总统自由勋章 2005、Queen Elizabeth 2013、IEEE Medal of Honor 2024
14. **双雄对照页**：Kahn（ARPANET 管理/架构构想）· Cerf（TCP 规范/治理）——共享与侧重
15. **结尾**："the fathers of the Internet" 之一——架构师的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **数据源口径**：本地页面已补抓为正确条目 `Robert Kahn (computer scientist)`——tex 事实以本地为准；Review-1 用本地页面逐条核对。
- **图灵奖获奖理由（核心红线，整句引用）**：2004 年与 Cerf 共享，"for their pioneering work on internetworking, including .. the Internet's basic communications protocols .. and for inspired leadership in networking."——与 Cerf 篇一致，按页面原样引用，勿改写。
- **"互联网之父"表述**：与 Cerf 分享的 "the fathers of the Internet"（"之一"口径）；正文引语 "the watershed event..." 是**对 1972 ICCC 展示的描述**，勿误用作自封头衔。
- **TCP 构想与 TCP 规范的分工**：Kahn 是 TCP **最初构想的提出者**（SATNET 期、意在取代 NCP）；**第一份 TCP 规范（RFC 675）署名是 Cerf/Dalal/Sunshine**——Kahn 篇写"构想者与共同完成者"，勿写 Kahn 执笔 RFC 675；也勿在 Cerf 篇写 Cerf 独创 TCP。
- **Draper Prize 口径**：在线回退源列 Kahn 为 Draper Prize **2001** 得主（共同获奖者名单在回退源中未详列）；而 Kay 篇页面载 2004 Draper 共享者为 Kay/Lampson/Taylor/Thacker——**两个年份对应不同届次，Kahn 篇写 2001 且注明"共同获奖者页面未详列，勿自行补写"**；Cerf 本页 infobox 未列 Draper，Cerf 篇禁写。
- **战略计算计划**：IPTO 主任期间启动、页面称 "the United States federal government's largest computer research and development project"（十亿美元级）——按页面口径写"迄今最大"，勿加军事细节渲染。
- **出生地口径**：infobox 作 New York City，正文注明 Brooklyn——写作时取"纽约市（布鲁克林）"即可，勿纠结先后。
- **在世留白**：1938 年生，在世——死亡日期与死因完全留白。
- **Herman Kahn 亲缘**："through his father" 与未来学家 Herman Kahn 有亲缘关系——一笔带过，勿展开家族考据。
- **学生信息缺失**：回退源正文无学生章节——**"门生/博士生"一栏写"页面无载，禁写"**；Kahn 并非 BBN 创始人（页面只说其在 BBN 任职），勿写"BBN 创始人"。
- **共享结构**：本篇侧重 ARPANET 项目管理与互联网架构；Cerf 篇侧重 TCP 规范与 ICANN 治理；共同部分（1974 论文、TCP/IP、ISOC 1992、Turing 2004、总统自由勋章 2005、Japan Prize 2008、发明家名人堂 2006）口径一致，**禁写页面无载的两人分工恩怨**。
- **引语红线**：全篇唯一直接引语为 1972 ICCC "watershed event" 一句——除此之外勿编造任何 Kahn 名言。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 罗伯特·卡恩 | 待写入 |
| name_en | Robert Kahn（全名 Robert Elliot Kahn） | 待写入 |
| birth_date | 1938-12-23 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist / internet pioneer | 待写入 |
| field_of_work | telecommunications / computer networks | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Bede Liu（刘必治，Princeton）
- **TCP/IP 合作者**：Vint Cerf（1974 IEEE 论文、DoD TCP/IP、ISOC 1992、CNRI 1986 共事、图灵奖 2004 共享）
- **ISOC 共同创立者**：Vint Cerf 等（首任主席为 Cerf）
- **妻子**：Patrice Ann Lyons
- **亲缘**：Herman Kahn（未来学家，父系亲缘）
- **博士生**：页面无载——**禁写**

## 8. 奖项清单

- SIGCOMM Award（1993，"Visionary technical contributions and leadership in the development of information systems technology"）
- Marconi Prize（1994）
- Stibitz-Wilson Award（1999，"通过 ARPANET NCP 协议的主要设计与开发贡献开创互联网，并共同发明互联网 TCP/IP 协议"）
- National Medal of Technology（1997，与 Cerf 共享，Clinton 颁发，理由整句见 §2-8）
- IEEE Alexander Graham Bell Medal（1997）
- Charles Stark Draper Prize（2001，回退源口径；共同获奖者页面未详列，勿自行补写）
- Prince of Asturias Award（2002）
- Turing Award（2004，与 Cerf 共享，理由整句引用见 §5）
- Townsend Harris Medal（2005）；日本 C&C 奖（2005）
- Presidential Medal of Freedom（2005-11，与 Cerf 同获，George W. Bush 颁发）
- Computer History Museum Fellow（2006）
- National Inventors Hall of Fame（2006-05，与 Cerf 共同入选）
- Japan Prize（2008-01，与 Cerf 共享）
- Internet Hall of Fame（2012）
- Queen Elizabeth Prize for Engineering（2013，首届五位得主之一）
- IEEE Medal of Honor（2024，"Pioneering technical and leadership contributions in packet communication technologies and foundations of the Internet"）
- IEEE Fellow（1981）、NAE 院士（1987）、AAAI 创始会士（1990）、ACM Fellow（2001）
- 荣誉学位：Princeton、帕维亚大学（1998）、ETH Zurich、马里兰大学、乔治梅森大学、中佛罗里达大学、比萨大学等；伦敦大学学院荣誉会士；ITMO 荣誉博士（2012）

## 9. 机构清单

- 教育：City College of New York（电机工程 BS，1960）；Princeton University（MA 1962 / PhD EE 1964，信号采样与调制论文）
- 任职：Bell Labs；MIT；BBN（ARPANET 主要设计者时期）；DARPA IPTO（1972 起，后任主任，共 13 年）；CNRI 创立者（1986 起，截至 2022 年任董事长、CEO 兼总裁）；Qualcomm 董事（曾任）

## 10. 终审清单

- [ ] 本地消歧义页已重抓为正确条目（✅ 主控已完成补抓 `pages/2004/Robert Kahn (computer scientist)/`）并逐条核对全部事实（Review-1 第一项）
- [ ] 生卒 1938-12-23 / 在世留白，出生地 New York City（Brooklyn）
- [ ] 图灵奖 2004 与 Cerf 共享，理由整句按页面原样引用
- [ ] Kahn = TCP 构想者；RFC 675 执笔 = Cerf/Dalal/Sunshine——分工表述不越界
- [ ] 1972 ICCC "watershed event" 引语整句、语境正确
- [ ] 战略计算计划 "迄今最大联邦计算机研发项目" 按页面口径
- [ ] Draper Prize 写 2001 且注明共同获奖者未详列；Cerf 篇无 Draper
- [ ] ISOC 共同创立、首任主席是 Cerf
- [ ] 门生栏写"页面无载禁写"
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | BBN · DARPA · CNRI | Turing 2004`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **★ 重抓数据源**：以 `Robert Kahn (computer scientist)` 为标题重抓本地 Wikipedia 页面（替换 `turing/pages/2004/Robert Kahn/index.html` 或存入新目录），逐条对照本提示词全部事实；冲突处**以重抓页面为准并回写本文件**
- [ ] **头像**：使用 `turing/pages/2004/Robert Kahn (computer scientist)/images/500px-Bob_Kahn.jpg`（执行时复制到 presentations/Robert_Kahn/images/；另有 CerfKahnMedalOfFreedom.jpg 可作 TCP/IP 页插图）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：唯一引语 "the watershed event..." 逐字核对
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与共享得主 Cerf 篇格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
