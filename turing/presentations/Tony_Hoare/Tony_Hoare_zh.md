# Tony Hoare（托尼·霍尔）立传提示词

> qid=Q92602 · 1934-01-11 – 2026-03-05 · 英国计算机科学家 · 20/21 世纪 · 1980 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1980/Tony Hoare/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Hoare 三元组 {P} C {Q} / CSP 进程交互的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Sir Charles Antony Richard Hoare（中文惯称：托尼·霍尔 / C. A. R. 霍尔；爵士，2000 年受封）
- **生卒**：1934-01-11 生于科伦坡（Colombo，英属锡兰，今斯里兰卡）→ 2026-03-05 逝于剑桥（Cambridge，英格兰），享年 92（2026 年 3 月刚去世，页面已载讣告）
- **国籍**：英国（British）
- **身份**：计算机科学家（编程语言、算法、形式验证、并发计算奠基人；FRS、FREng）
- **家庭**：父亲为殖民地公务员，母亲为茶园主之女；1962 年与研究团队成员 Jill Pym 结婚，育有 3 个孩子
- **教育轨迹**：
  - 中学：Dragon School（牛津）、The King's School（Canterbury）
  - Merton College, Oxford：古典学与哲学（"Greats"）学士，1956 年毕业
  - 1956–1957 英国皇家海军**18 个月国民服役**，期间学习俄语
  - 1958 年返 Oxford 修**统计学研究生文凭**（postgraduate certificate），在此开始编程（Leslie Fox 教其在 Ferranti Mercury 上写 Autocode）
  - Moscow State University：英国文化协会交换生，随 **Andrey Kolmogorov** 研究机器翻译
- **师承/学术影响**：Kolmogorov（莫大交换期间导师）；Oxford 统计期启蒙编程者 Leslie Fox；**无正规博士学位**（页面未载任何博士学历，infobox 学历仅 Oxford BA, PgDip——禁写 PhD）
- **研究领域**：编程语言、算法、操作系统、形式验证、并发计算

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **锡兰出生的古典学学生**：1934 生于科伦坡，英国受教育，牛津读的是"Greats"（古典学与哲学）——**非理工科出身**。
2. **海军俄语 → 莫斯科 Kolmogorov**：服役学俄语 → 统计学研究生文凭 → 以交换生身份入莫斯科国立大学随 Kolmogorov 研究机器翻译——一条"语言"贯穿的主线。
3. **Quicksort（1959–1960）**：在莫斯科期间发展出的排序算法——计算机科学最著名的算法之一；另有 Quickselect。页面实载"developed the sorting algorithm quicksort in 1959–1960"。
4. **Elliott Brothers（1960）**：离开苏联后入职伦敦小型计算机制造商 Elliott Brothers，实现 **ALGOL 60 编译器**并开始发展主要算法。
5. **Hoare 逻辑（1969）**：*An Axiomatic Basis for Computer Programming*（CACM 1969-10）——程序正确性验证的**公理基础**；与 Floyd 1967 年工作一脉相承。
6. **Monitors（1974）**：*Monitors: An operating system structuring concept*——用 monitor 概念结构化操作系统。
7. **CSP（1978 论文 / 1985 专著）**： Communicating Sequential Processes——描述并发进程交互的形式语言，后在 occam 等语言中实现；1985 年 Prentice Hall 专著（usingcsp.com 在线可读）。
8. **哲学家就餐问题**：与 **Edsger Dijkstra** 一起表述（formulated）——共同提出，勿独揽。
9. **"十亿美元错误"（2009）**：为 1965 年在 ALGOL W 中发明 **null 引用**公开道歉——页面整段原文引语（见 §5），是最具传播度的直接引语。
10. **学术生涯三站**：1968 年 Queen's University Belfast 计算机科学教授 → 1977 年返 Oxford 任 Computing 教授、接掌 Programming Research Group（接替已故 Christopher Strachey）→ 1988 年成为**首任 Christopher Strachey Professor of Computing**，2000 年从 Oxford 荣休；晚年同为 Oxford 荣休教授与 **Microsoft Research（Cambridge）首席研究员**。
11. **图灵奖 1980**：citation "for fundamental contributions to the definition and design of programming languages"；1980-10-27 于 Nashville ACM 年会由 Walter Carlson 颁授；图灵讲座题为 **The Emperor's Old Clothes**（皇帝的新衣，CACM 1981-02）。
12. **荣誉等身**：FRS 1982、骑士 2000、Kyoto Prize 2000、IEEE von Neumann Medal 2011、**Royal Medal 2023**（90 岁前再获皇家奖章）；2026 年 3 月逝世后 ACM/The Guardian/CHM 多方发讣告。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（算法 — 蓝） | `#2E5A9E` | Quicksort / Quickselect |
| 分类色 2（形式验证 — 青绿） | `#1E8E8E` | Hoare 逻辑 / 公理基础 |
| 分类色 3（并发计算 — 琥珀） | `#D9A441` | CSP / monitors / 哲学家就餐 |
| 分类色 4（编程语言设计 — 玫瑰） | `#C0395B` | ALGOL 60 / null 反思 / Strachey 讲席 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「公理与进程」的秩序化形式语言美学。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：庄重 / 反思（公理化的一生、晚年的坦诚道歉）
- **选定曲目**：Alex-Productions **Cinematic Experience**（manifest 预分配，直接沿用），匹配"从 Quicksort 到十亿美元错误"的史诗与自省双线叙事。
- **落地文件**：`turing/presentations/Tony_Hoare/CinematicExperience.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「编程语言与形式方法大师 · 英国」+ 霍尔 1934–2026 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1934–2026 生平纵览
4. **锡兰出生与古典学教育**（1934–1956）：殖民地公务员之子、Dragon School / King's School、牛津 Greats
5. **海军、俄语与统计学**（1956–1958）：18 个月服役、Ferranti Mercury 上第一次编程
6. **莫斯科与 Kolmogorov**（1958–1960）：机器翻译、交换生岁月
7. **Quicksort**（1959–1960）：算法的诞生与 Quickselect
8. **Elliott Brothers 与 ALGOL 60**（1960–1968）：编译器、IFIP WG 2.1
9. **Hoare 逻辑**（1969）：公理化程序验证、{P} C {Q} 三元组
10. **Monitors 与 CSP**（1974–1985）：操作系统结构化、并发进程形式语言、与 Dijkstra 的哲学家就餐问题
11. **null 引用与"十亿美元错误"**（1965 / 2009）：ALGOL W、公开道歉（整段引语）
12. **图灵奖 1980**：citation 整句 + The Emperor's Old Clothes 讲座
13. **Oxford 与 Microsoft Research**：Belfast→Oxford 三站、Strachey 讲席、形式方法的 1995 反思（引语）
14. **荣誉与传承**：FRS 1982 / 骑士 2000 / Kyoto 2000 / Royal Medal 2023；门生 Cliff Jones、Bill Roscoe、Augusto Sampaio
15. **结尾**：92 岁、"程序正确性公理化"的历史地位与遗产（2026-03-05 逝世）

## 5. 史实陷阱与敏感点（终审必须检查）

- **卒年 2026（本年度）**：2026-03-05 逝于剑桥，享年 92——页面已载（BBC Last Word / Guardian 讣告 / ACM in memoriam），生卒写 `1934–2026`；死因页面未详述，勿编造。
- **无博士学位**：infobox 学历仅 Oxford BA + PgDip（统计研究生文凭）——**禁写任何 PhD**；Belfast/Oxford 教授职位均为实绩聘任。
- **Quicksort 年份与地点**：1959–1960 发展（莫斯科交换期间构思、Elliott 期间实现落地按页面口径写"developed in 1959–1960"）——勿写错年份，勿写"在 Elliott 发明"绝对化。
- **Hoare 逻辑 vs Floyd**：Floyd 1967 年 *Assigning Meanings to Programs* 是先声；Hoare 1969 给出公理基础——本篇以 Hoare 为主角时**勿贬抑 Floyd**，也勿写"Hoare 逻辑完全原创无前驱"。
- **哲学家就餐问题**：页面口径 "along with Edsger Dijkstra, formulated"——**共同表述**，勿写 Hoare 独创，也勿写 Dijkstra 独创。
- **图灵奖理由（核心红线）**："for fundamental contributions to the definition and design of programming languages"——整句引用；讲座题 *The Emperor's Old Clothes*（1980-10-27 Nashville，Walter Carlson 颁授）。
- **null 引语（整段可引）**：2009 原文 "I call it my billion-dollar mistake. It was the invention of the null reference in 1965. ... This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years."——引语归属 2009 软件会议演讲（InfoQ 记录）；1965 年语境是 **ALGOL W** 的面向对象引用类型系统设计。
- **形式方法反思引语（1995）**："Ten years ago, researchers into formal methods (and I was the most mistaken among them) predicted that the programming world would embrace with gratitude every assistance promised by formalisation..."——CSP/Z notation 未获业界预期采用后的自我检讨；保留"反思"语境，勿写成"形式方法失败论"。
- **1977 返 Oxford 的原因**：接替**已故的 Christopher Strachey** 领导 Programming Research Group——Strachey 1977 去世、Hoare 接棒，因果勿倒置；1988 年讲席以 Strachey 命名（首任）。
- **IFIP WG 2.1**：与 Floyd 同为 WG 2.1 成员（ALGOL 60/68）——两人交集仅此，勿虚构其他合作。
- **妻子**：Jill Pym 是"他的研究团队成员"，1962 年结婚——按页面实载，勿渲染。
- **奖项**：Turing 1980、Goode 1981、FRS 1982、Knighted 2000、Kyoto 2000、von Neumann Medal 2011、Royal Medal 2023 等（§8 全列）——勿编造页面外的奖项。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 托尼·霍尔（或 C. A. R. 霍尔） | 待写入 |
| name_en | Tony Hoare | 待写入 |
| birth_date | 1934-01-11 | 待写入 |
| death_date | 2026-03-05 | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | programming languages / algorithms / formal verification / concurrent computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **交换期导师**：Andrey Kolmogorov（Moscow State University，机器翻译）
- **合作者**：Edsger W. Dijkstra（哲学家就餐问题共同表述、Structured Programming 三作者之一）、Ole-Johan Dahl（Structured Programming 1972 合著）、He Jifeng（何积丰，Unifying Theories of Programming 1998 合著）、M. J. C. Gordon（Mechanised Reasoning 合著）
- **博士生**：Cliff Jones、Bill Roscoe、Augusto Sampaio
- **前任（讲席）**：Christopher Strachey（1977 去世，Hoare 接掌其 PRG 与讲席）
- **家庭**：Jill Pym（妻子，原研究团队成员）

## 8. 奖项清单

- ACM Programming Systems and Languages Paper Award（1973，"Proof of correctness of data representations"）
- Distinguished Fellow of the British Computer Society（1978）
- Turing Award（1980）
- Harry H. Goode Memorial Award（1981）
- Fellow of the Royal Society（1982）
- Honorary DSc, Queen's University Belfast（1987）；University of Bath（1993）；Kellogg College Honorary Fellow（1998）；Heriot-Watt（2007）；AUEB（2007）；Warsaw（2012）；Complutense（2013）
- Knighted（爵士，2000，for services to education and computer science）
- Kyoto Prize（Information science，2000）
- Fellow of the Royal Academy of Engineering（2005）；NAE Member（2006）
- Computer History Museum Fellow（2006，"for development of the Quicksort algorithm and for lifelong contributions to the theory of programming languages"）
- Friedrich L. Bauer Prize（TU München，2007）
- SIGPLAN Programming Languages Achievement Award（2011）
- IEEE John von Neumann Medal（2011）
- Royal Medal（Royal Society，2023）

## 9. 机构清单

- 教育：Dragon School、The King's School Canterbury → Merton College, Oxford（古典学与哲学 BA 1956）→ Oxford 统计学研究生文凭（1958）→ Moscow State University（British Council 交换生）
- 任职：Elliott Brothers Ltd（1960–1968）→ Queen's University Belfast（计算科学教授，1968–1977）→ University of Oxford（Computing 教授 1977、首任 Christopher Strachey Professor of Computing 1988–2000 荣休）→ Microsoft Research Cambridge（首席研究员，1977 年起并行的"from 1977 on, he held positions at the University of Oxford as well as at Microsoft Research"按页面口径处理为晚年并存）

## 10. 终审清单

- [ ] 生卒 1934-01-11 / 2026-03-05，享年 92，出生地 Colombo（英属锡兰），去世地 Cambridge
- [ ] "牛津古典学（Greats）出身、无 PhD"表述准确
- [ ] Quicksort 1959–1960 年份准确
- [ ] Hoare 逻辑 1969 公理基础表述准确，未贬抑 Floyd 先声
- [ ] 哲学家就餐问题"与 Dijkstra 共同表述"表述准确
- [ ] null 引语（2009 十亿美元错误）与 1995 形式方法反思引语逐字核对、出处标注正确
- [ ] 图灵奖 citation 整句引用无误；讲座 The Emperor's Old Clothes
- [ ] 1977 接替已故 Strachey、1988 首任 Strachey 讲席表述准确
- [ ] 肖像文件核对：`images/500px-Sir_Tony_Hoare_IMG_5125.jpg`（2011 年照，已就绪）
- [ ] 国籍用「英国」，封面底部状态栏 `英国 | Oxford · Belfast · Microsoft Research | Turing 1980`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1980/Tony Hoare/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Sir_Tony_Hoare_IMG_5125.jpg`（500px，2011 年照，已就绪）
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：两段长引语（billion-dollar mistake、formal methods 反思）必须与 Wikipedia 原文逐字一致
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一；Hoare 三元组符号排版核对
- [ ] 与同期图灵奖得主（Floyd / Iverson / Dijkstra 篇）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
