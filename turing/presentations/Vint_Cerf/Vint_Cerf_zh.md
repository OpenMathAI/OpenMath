# Vint Cerf（文特·瑟夫）立传提示词

> qid=Q92743 · 1943-06-23 – 在世留白 · 美国互联网先驱 · 20/21 世纪 · 2004 图灵奖（与 Robert Kahn 共享）
> 本地 Wikipedia 数据源：`turing/pages/2004/Vint Cerf/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（TCP/IP 协议分层 / 端到端原则的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Vinton Gray Cerf（中文惯称：文特·瑟夫 / 温顿·瑟夫；昵称 Vint）
- **生卒**：1943-06-23 生于康涅狄格州纽黑文（New Haven, Connecticut，美国）；在世，卒年留白
- **国籍**：美国（American）
- **身份**：互联网先驱，与 TCP/IP 共同开发者 Robert Kahn 并称 **"the fathers of the Internet"（互联网之父）**之一——页面口径：Cerf 自陈愿意自称"互联网之父之一"，并点名应与 Kahn、Kleinrock 分享此称号
- **家庭**：父母 Muriel（本姓 Gray）与 Vinton Thruston Cerf；母亲生于加拿大（英/爱/法裔加拿大血统）；父系祖先自阿尔萨斯-洛林移民肯塔基；妻子 Sigrid——两人都有听力障碍，1960 年代在助听器验配师诊所相识；两个儿子 David 与 Bennett
- **教育轨迹**：
  - Van Nuys High School（与 Steve Crocker、Jon Postel 同学——互联网史的伏笔）
  - 高中期间在 Rocketdyne 参与 Apollo 计划六个月，为 F-1 发动机无损试验编写统计分析软件
  - Stanford University **数学**学士（BS）
  - IBM 系统工程师两年（支持 QUIKTRAN）
  - UCLA **硕士**（1970）+ **博士**（1972），论文 *Multiprocessors, Semaphores, and a Graph Model of Computation*
- **博士导师**：Gerald Estrin；研究生期间在 **Leonard Kleinrock** 的分组数据网络小组工作（该组连接了 ARPANET 的头两个节点）
- **研究领域**：电信（infobox Fields：Telecommunications）
- **标志性形象**：三件套西装——在以休闲着装著称的行业中罕见；专栏笔名 "CERF'S UP"；车牌 vanity plate "CERFSUP"

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **第一份 TCP（RFC 675，1974-12）**【本篇侧重支柱】与 Yogen Dalal、Carl Sunshine 撰写 *Specification of Internet Transmission Control Program*——互联网传输控制程序的首份规范；Cerf 亦曾任 International Network Working Group（INWG）主席。
2. **TCP/IP 共同设计（1972–1976）**：Stanford 助理教授任内（1972–1976）研究分组网络互联协议，与 Kahn 共同设计 DoD TCP/IP 协议族；此前 1974-05 与 Kahn 在 IEEE Transactions on Communications 发表 *A Protocol for Packet Network Intercommunication*（两人共同署名的奠基论文）。
3. **UCLA 岁月**：在 Kleinrock 小组参与连接 ARPANET 头两个节点的工作，"contributed to a host-to-host protocol"；在 UCLA 结识了做 ARPANET 系统架构的 Bob Kahn——两人此后的全部故事由此开始。
4. **DARPA 时期（1973–1982）**：资助各团队发展 TCP/IP、分组无线电（PRNET）、分组卫星（SATNET）与分组安全技术——页面引其口述史："we absolutely wanted to bring data communications to the field..."（军事需求驱动）；1988 年起力主互联网私有化（"I pushed for privatization as early as 1988..."，Cerf 2020 数字民主论文实载）。
5. **MCI Mail：首个接入互联网的商业电子邮件服务**：1982–1986 任 MCI Digital Information Services 副总裁，主导 MCI Mail 工程——1989 年成为**第一个接入互联网的商业电子邮件服务**；1994 年重返 MCI 任 SVP Technology Strategy。
6. **CNRI 与互联网协会**：1986 年加入 Bob Kahn 创立的 Corporation for National Research Initiatives（CNRI）任副总裁（数字图书馆、Knowledge Robots、千兆网络）；**1992 年与 Kahn 等共同创立 Internet Society（ISOC）并任首任主席**。
7. **ICANN 时期**【本篇侧重的治理线】：参与筹资并建立 ICANN；1999 年进入董事会，**2000 年 11 月起任董事长**直至 2007 年 11 月离开董事会。
8. **Google 首席互联网布道师**：2005-10 至 2026-07 任 Google 副总裁兼 Chief Internet Evangelist——以对 AI、环保、IPv6、电视业变革的技术预测闻名；2026 年退休（页面载 TechCrunch/Inc. 2026-07 报道）。
9. **星际互联网（Interplanetary Internet）**：与 NASA JPL 等实验室合作的新标准——容忍时延与中断的行星间无线电/激光通信；2016-06 **时延容忍网络（DTN）部署到国际空间站**。
10. **无障碍倡导**：夫妻二人均有听力缺陷——他因此成为信息无障碍（accessibility）的长期倡导者；1997 年加入聋人大学 Gallaudet University 董事会。
11. **"数字黑暗时代"警告（2015 起）**：数字过时（digital obsolescence）风险——今天的文本/数据/图像/音乐可能因存储介质与软件环境消亡而集体失忆，成为数字"黑暗时代"或"黑洞"。
12. **其他治理与公共角色（择要）**：ACM 主席（2012-07 起两年任期）；美国国家科学委员会（National Science Board，2013–2018）；ARIN 董事会主席（2011–2016）；StopBadware 董事会主席（至 2015 秋）；People-Centered Internet 共同创立者（2015，与 Mei Lin Fung）；2006-02-07 在美国参议院就网络中立（net neutrality）作证；2008 年曾是奥巴马政府首任 CTO 的重要人选之一。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（TCP/IP 与协议设计 — 蓝） | `#2E5A9E` | RFC 675 / 1974 IEEE 论文 |
| 分类色 2（产业落地 — 青绿） | `#1E8E8E` | MCI Mail / Google 布道师 |
| 分类色 3（互联网治理 — 琥珀） | `#D9A441` | ICANN / ISOC / ACM 主席 |
| 分类色 4（未来与公共倡导 — 玫瑰） | `#C0395B` | 星际互联网 / 数字黑暗时代 / 无障碍 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和网络节点连线（稀疏点线图），呼应「网际互联把孤岛连成大陆」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：开阔 / 远征（从 ARPANET 头两个节点到星际互联网的连接者人生）
- **选定曲目**：Alex-Productions **PAST**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Vint_Cerf/PAST.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「互联网之父 · 美国」+ Cerf 1943– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域 / 家庭）
3. **时间线**（`\timelineslide`）：1943– 生平纵览
4. **早年：纽黑文与 Van Nuys**：Crocker/Postel 同学、Apollo 计划写代码、Stanford 数学、IBM 系统工程师
5. **UCLA：ARPANET 的头两个节点**：Kleinrock 小组、Estrin 门下、结识 Bob Kahn
6. **1974：RFC 675 与第一份 TCP**：与 Dalal/Sunshine、INWG 主席
7. **TCP/IP 共同设计**：1974 IEEE 论文、Stanford 助理教授期、DoD 协议族
8. **DARPA（1973–1982）**：PRNET/SATNET/分组安全、军事驱动的口述史引语
9. **MCI Mail 与商业化**：1982–1986 工程主导、1989 首个联网商业邮件、1988 私有化主张
10. **CNRI 与 ISOC**：与 Kahn 再度共事、1992 创立互联网协会、首任主席
11. **ICANN 董事长（2000–2007）**：互联网治理的顶层设计
12. **Google 布道师（2005–2026）**：首席互联网布道师、技术预测、2026 退休
13. **星际互联网与数字黑暗时代**：DTN 上空间站、2016 部署；过时风险警告
14. **荣誉之殿**：Turing 2004、总统自由勋章 2005、Queen Elizabeth Prize 2013、IEEE Medal of Honor 2023；无障碍倡导（Gallaudet）
15. **结尾**："the fathers of the Internet" 之一——在世连接者的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖获奖理由（核心红线，整句引用）**：2004 年与 Robert Kahn 共享，"for their pioneering work on internetworking, including .. the Internet's basic communications protocols .. and for inspired leadership in networking."——与 Kahn 篇一致，按页面原样引用（含 ".." 处），勿改写。
- **"互联网之父"表述**："one of the fathers of the Internet, sharing this title with TCP/IP co-developer Robert Kahn"——**是"之一"、与 Kahn 分享**；页面还载 Cerf 自陈应与 Kahn、Kleinrock 分享称号——勿写"Cerf 是互联网之父"单数表述。
- **RFC 675 是"第一份 TCP 规范"，不是 TCP/IP 全家**：作者三人 Cerf/Dalal/Sunshine，1974-12 发布——勿写成 Cerf 一人发明 TCP，也勿与 1974-05 的 IEEE 双人论文混淆（两篇不同文献）。
- **MCI 任职年份的页面内部张力**：正文既写 "From 1973 to 1982, Cerf worked at DARPA"、又写 "As vice president of MCI Digital Information Services from 1982 to 1986"、还有一句 "In the late 1980s, Cerf moved to MCI"——**以 1982–1986 VP MCI 口径为主线，"late 1980s" 句按页面原文语境（MCI Mail 1989 联网）处理，Review 时标注该不一致**。
- **ISOC 首任主席**：Cerf served as **the first president** of ISOC——与 Kahn 共同创立但首任主席是 Cerf；Kahn 篇写"共同创立"即可。
- **ICANN 角色分层**：helped fund and establish ICANN → 1999 入董事会 → **2000-11 起任董事长** → 2007-11 离开——三个时间点勿混。
- **在世留白**：1943 年生，在世——死亡日期与死因完全留白；2026 年退休信息仅写"从 Google 退休"口径，勿延伸。
- **spam 争议**：页面实载 MCI 时期因 Send-Safe.com 垃圾邮件软件 IP 被批评、MCI 拒绝终止该供应商、Spamhaus 列名——**按页面实载一笔带过或省略，不渲染、不作定罪表述**。
- **2008 CTO 传言**："a major contender to be designated the first U.S. Chief Technology Officer"——是"人选之一"而非"出任"，勿写成任职。
- **引语红线**：可引用的页面实载语料——RFC 3271 "The Internet is for Everyone"（RFC 标题即立场）、口述史两段（军事驱动、"I pushed for privatization as early as 1988..."）、"It was one of the greatest..." 属 Kay 篇勿串用；其余勿编造。
- **共享结构**：本篇侧重 TCP 设计与 ICANN/治理线；Kahn 篇侧重 ARPANET 项目管理与互联网架构；两人共同部分（1974 论文、TCP/IP、ISOC 1992、图灵奖 2004、总统自由勋章 2005、Japan Prize 2008）口径一致，**禁写页面无载的两人分工恩怨**。
- **家庭与听障**：夫妻听力缺陷、Gallaudet 董事会——按页面实载写，语气温和，不煽情。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 文特·瑟夫（或 温顿·瑟夫） | 待写入 |
| name_en | Vint Cerf（全名 Vinton Gray Cerf） | 待写入 |
| birth_date | 1943-06-23 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | internet pioneer / computer scientist | 待写入 |
| field_of_work | telecommunications / internetworking | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Gerald Estrin（UCLA）
- **导师线同事**：Leonard Kleinrock（分组网络小组，ARPANET 头两个节点）
- **TCP/IP 合作者**：Robert (Bob) Kahn（1974 IEEE 论文、DoD TCP/IP、ISOC 1992、CNRI 1986）；Yogen Dalal、Carl Sunshine（RFC 675）
- **高中同学**：Steve Crocker、Jon Postel（Van Nuys High School）
- **共同获奖者**：Kahn（图灵奖 2004 / 国家技术奖章 1997 / 总统自由勋章 2005 / Japan Prize 2008 / 发明家名人堂 2006 / Draper——**Draper 奖归属以 Kahn 篇口径为准，Cerf 本页 infobox 未列 Draper，勿在本篇写 Draper**）
- **妻子**：Sigrid Cerf

## 8. 奖项清单

- ACM Fellow（1994）
- NAE 院士（1995，"for contributions to the design and development of network protocols and leadership in the evolution of the Internet"）
- Yuri Rubinsky Memorial Award（1996）；Franklin Institute Certificate of Merit（1996）
- SIGCOMM Award（"contributions to the Internet [spanning] more than 25 years, from development of the fundamental TCP/IP protocols"）
- IEEE Alexander Graham Bell Medal（1997）
- National Medal of Technology（1997，与 Kahn 共享，Clinton 总统颁发，"for creating and sustaining development of Internet Protocols..."）
- Marconi Prize（1998）
- Stibitz-Wilson Award（1999）；Library of Congress Living Legend Medal（2000-04）
- Computer History Museum Fellow（2000）；AWIS Fellow（2000）
- Prince of Asturias Award（科学与技术，2002）
- Turing Award（2004，与 Kahn 共享，理由整句引用见 §5）
- Presidential Medal of Freedom（2005-11，George W. Bush 总统颁发）
- National Inventors Hall of Fame（2006-05，与 Kahn 共同入选）
- Japan Prize（2008-01，与 Kahn 共享）
- Harold Pender Award（2010）
- HPI Fellowship（2011）；BCS Distinguished Fellow（2011）
- Internet Hall of Fame Pioneer（2012）
- Queen Elizabeth Prize for Engineering（2013，首届五位互联网与万维网先驱之一）
- Order of the Cross of Terra Mariana 1st class（2014，爱沙尼亚）；French Légion d'honneur Officer（2014）
- Foreign Member of the Royal Society, ForMemRS（2016）
- Benjamin Franklin Medal（2018）；Catalonia International Award（2018）
- IEEE Medal of Honor（2023，"for co-creating the Internet architecture and providing sustained leadership in its phenomenal growth in becoming society's critical infrastructure"）
- California Hall of Fame（2024）
- 荣誉博士二十余项（Yale、ETH Zurich、Keio、清华、北邮、RPI、St Andrews 等，页面实载）

## 9. 机构清单

- 教育：Van Nuys High School；Stanford University（数学 BS）；UCLA（MS 1970 / PhD 1972）
- 任职：IBM（系统工程师，约两年）；UCLA（研究生）；Stanford University 助理教授（1972–1976）；DARPA（1973–1982）；MCI Digital Information Services 副总裁（1982–1986，MCI Mail）；CNRI 副总裁（1986 起）；MCI SVP Technology Strategy（1994 起）；ISOC 首任主席（1992 起）；ICANN 董事（1999–2007，董事长 2000-11–2007）；Google VP & Chief Internet Evangelist（2005-10–2026-07）；ACM 主席（2012 起）；National Science Board（2013–2018）；ARIN 董事会主席（2011–2016）

## 10. 终审清单

- [ ] 生卒 1943-06-23 / 在世留白，出生地 New Haven, Connecticut
- [ ] 图灵奖 2004 与 Kahn 共享，理由整句按页面原样引用
- [ ] "互联网之父"为"之一、与 Kahn 分享"表述
- [ ] RFC 675（1974-12，三人）与 IEEE 论文（1974-05，双人）两篇文献不混
- [ ] ICANN：1999 董事 / 2000-11 董事长 / 2007-11 离开
- [ ] MCI Mail：1982–1986 VP 口径为主线，页面内部不一致已标注
- [ ] ISOC 首任主席归 Cerf；共同创立归两人
- [ ] spam 争议一笔带过不渲染；2008 CTO 仅"人选之一"
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | DARPA · MCI · CNRI · ICANN · Google | Turing 2004`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2004/Vint Cerf/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用真实肖像（首选 `images/500px-Dr_Vint_Cerf_ForMemRS_cropped_.jpg` 皇家学会官方裁剪照；备选 `500px-Vint_Cerf_-_2010.jpg`、`500px-CerfKahnMedalOfFreedom.jpg` 总统自由勋章双人照——双人照建议用于 Slide 14 荣誉页插图；`Signature_of_Vint_Cerf.png` 签名可作封面装饰性小注，非肖像）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：RFC 3271 标题、口述史引语逐字核对
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与共享得主 Kahn 篇格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
