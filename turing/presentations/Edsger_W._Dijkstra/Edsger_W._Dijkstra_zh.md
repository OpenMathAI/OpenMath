# Edsger W. Dijkstra（艾兹赫尔·W·戴克斯特拉）立传提示词

> qid=Q8556 · 1930-05-11 – 2002-08-06 · 荷兰计算机科学家 · 20 世纪 · 1972 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1972/Edsger W. Dijkstra/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 荷兰`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（最短路径松弛 / 信号量 P-V 操作 / 卫式命令的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Edsger Wybe Dijkstra（中文惯称：艾兹赫尔·W·戴克斯特拉；发音 DYKE-strə）
- **生卒**：1930-05-11 生于鹿特丹（Rotterdam，荷兰）→ 2002-08-06 逝于 Nuenen（荷兰），享年 72（与癌症长期抗争后去世；曾言"想在 Austin 退休，但要在荷兰去世"）
- **国籍**：荷兰（Dutch）
- **身份**：计算机科学家、程序员、数学家、科学随笔作家（essayist）
- **家庭**：父 Douwe Wybe Dijkstra（1898–1970，化学家，鹿特丹化学 circle 主席、中学校长级教师）、母 Brechtje Cornelia Kluijver（1900–1994，数学家但从未正式任职）；1957 年与 Maria "Ria" C. Debets 结婚；三子女：Marcus、Femke、Rutger M. Dijkstra（计算机科学家）
- **教育轨迹**：
  - 中学：Gymnasium Erasmianum（鹿特丹），1948 年毕业；曾想学法律、梦想代表荷兰进联合国
  - Leiden University：数学与物理、后转理论物理（BS, MS）
  - University of Amsterdam：PhD（1959），论文 *Communication with an Automatic Computer*（为荷兰首台商用计算机 Electrologica X1 设计的汇编语言）
- **博士导师**：Adriaan van Wijngaarden（阿姆斯特丹数学中心计算部主任）
- **研究领域**：理论计算机科学、结构化编程、并发与分布式计算、形式化方法

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **荷兰第一位"程序员"（1952-03）**：经导师 Haantjes 教授引荐，被 van Wijngaarden 雇为阿姆斯特丹数学中心（Mathematisch Centrum）程序员——荷兰官方承认的第一位 programmer；1957 年结婚登记时报"职业：程序员"竟被当局拒绝（荷兰当时不存在这个职业）。
2. **最短路径算法（1956 构思，1959 发表）**：为 ARMAC 计算机正式揭幕演示而构思并解决最短路径问题；因当时无自动计算期刊，直到 1959 年才发表（"A Note on Two Problems in Connexion with Graphs", *Numerische Mathematik*）——今为 CS 本科必修内容，OSPF、IS-IS 路由协议的核心。
3. **首个 ALGOL 60 编译器（1960-08）**：与同事 Jaap Zonneveld 合作完成，比另一组早一年多；ALGOL 60 是结构化编程兴起的关键一步。
4. **THE 多程序系统（1960s 末）**：以所在大学（Technische Hogeschool Eindhoven）命名；分层（layers）操作系统设计的早期典范，其基于软件的分页虚拟内存影响后世系统设计。
5. **并发原语**：*Cooperating Sequential Processes*（EWD-123, 1965）、**信号量（semaphore）** 用于多进程协调、银行家算法（资源分配死锁避免）、互斥问题解法（1965）。
6. **"Go To Statement Considered Harmful"（1968）**：致 *CACM* 编辑的信，引发大辩论——结构化编程运动的号角；现代程序员普遍遵循结构化范式。
7. **结构化编程与图灵奖（1972）**：获奖理由 "for fundamental contributions to developing structured programming languages"；图灵奖演讲 *The Humble Programmer*（"谦逊的程序员"）：'We must not forget that it is not our business to make programs, it is our business to design classes of computations that will display a desired behaviour.'
8. **EWD 手稿传统**：以自己姓名缩写编号的技术手稿（EWD 系列），40 年跨度、编号至 EWD1318（2002-04-14），逾 1300 篇已被扫描存档（UT Austin Dijkstra Archive）；Burroughs 十年写了近 500 篇；1972 年后几乎全为手写（Montblanc 大师级钢笔）。
9. **自稳定（self-stabilization, 1974）**：分布式计算容错方法；为此获 ACM PODC Influential-Paper Award（2002，去世前不久），次年该奖更名为 **Dijkstra Prize**。
10. **Tuesday Afternoon Club**：Burroughs 年代每周二固定研讨班（大学只留周三一天——注意：原文载大学减为 one day a week，而 Tuesday Afternoon Club 在"那一天"举行；表述为"每周一天"即可），1984 年后在 Austin 延续出分部。
11. **个性与风格**：书著无参考文献（'For the absence of a bibliography I offer neither explanation nor apology.'）；多年拒用计算机写作；给 60 岁纪念文集的 61 位撰稿人每人一封手写感谢信；强反对教 BASIC；称软件工程为 'The Doomed Discipline'；虚构"Mathematics, Inc."公司系列随笔；名言 "The question of whether Machines Can Think (...) is about as relevant as the question of whether Submarines Can Swim."、"A picture may be worth a thousand words, a formula is worth a thousand pictures."、给研究者的建议 "Do only what only you can do."
12. **荣誉**：荷兰皇家艺术与科学院院士（1971）、BCS 首位 Distinguished Fellow（1971，该奖 1969 获批设立后的首次授予）、Goode Award 1974、ACM Fellow 1994、日本 C&C Prize（2002，生前获通知、由家人在典礼上代领）等。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（算法与系统 — 蓝） | `#2E5A9E` | 最短路径 / THE 系统 |
| 分类色 2（并发 — 青绿） | `#1E8E8E` | 信号量 / 银行家算法 / 自稳定 |
| 分类色 3（结构化编程 — 琥珀） | `#D9A441` | Go To 有害论 / ALGOL 60 |
| 分类色 4（思想与文风 — 玫瑰） | `#C0395B` | EWD 手稿 / The Humble Programmer |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：有向图节点与最短路径线段（稀疏细线连接小圆点），呼应「最短路径」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：求索 / 探路（最短路径的"探路者"意象）
- **选定曲目**：Alex-Productions **Pathfinder**（探路者），与 Dijkstra 算法的"最短路径"意象绝妙呼应；与同代已用的 New Lands / Timeless / Falling Apart 区分。
- **落地文件**：`turing/presentations/Edsger_W._Dijkstra/Pathfinder.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「结构化编程之父 · 荷兰」+ Dijkstra 1930–2002 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1930–2002 生平纵览
4. **早年：鹿特丹的律师梦与理论物理**（1930–1952）：Gymnasium Erasmianum、Leiden 数学物理、联合国梦想
5. **荷兰第一位程序员**（1952–1959）：van Wijngaarden 的邀请、"程序员"婚姻登记轶事、X1 博士论文
6. **最短路径算法**（1956/1959）：ARMAC 揭幕演示、1959 年才发表、OSPF/IS-IS 传承
7. **首个 ALGOL 60 编译器**（1960）：与 Zonneveld、早其他组一年多
8. **THE 多程序系统**（1960s 末）：分层结构、软件分页虚拟内存
9. **信号量与并发原语**：Cooperating Sequential Processes、P-V 操作、银行家算法
10. **"Go To Statement Considered Harmful"**（1968）：一封信引发的大辩论
11. **图灵奖 1972 与 The Humble Programmer**：结构化编程、谦逊的程序员
12. **EWD 手稿与个人风格**：Montblanc 钢笔、1300+ 篇手稿、Mathematics Inc. 随笔、名言集
13. **Burroughs 与 UT Austin**（1973–1999）：唯一 research fellow、Tuesday Afternoon Club、Schlumberger Centennial Chair
14. **荣誉与传承**：Dijkstra Prize、Goode Award、C&C Prize、博士生 Habermann / van de Snepscheut
15. **结尾**：72 岁、"想在 Austin 退休，但要在荷兰去世"——结构化编程范式的永久遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **最短路径年份**：**1956 年构思**（为 ARMAC 揭幕演示）、**1959 年发表**——勿写"1959 年发明"或"1956 年发表"。
- **"Go To Statement Considered Harmful"**：标题是信件见报时的处理结果——**页面未载是谁加的标题，勿写"Niklaus Wirth 起的标题"**（其他来源有此说，但本页无载禁写）。
- **图灵奖理由**：'fundamental contributions to developing structured programming languages'——是"结构化编程**语言**的发展"，勿写成"发明结构化编程"或"Go To 有害论获奖"（Go To 信是获奖相关叙事但不是官方理由原文）。
- **EWD 数量**：全系列 1300+ 篇（编号至 EWD1318）、**Burroughs 十年近 500 篇**——两个数字勿混用。
- **Burroughs 身份**：是公司**唯一的 research fellow**、在家（Nuenen 书房）工作、偶尔赴美——大学减为每周一天；Tuesday Afternoon Club 即在那一日。
- **博士信息**：PhD 是 **University of Amsterdam**（1959，导师 van Wijngaarden），**不是 Leiden**（Leiden 是本硕数学/理论物理）——勿混淆。
- **自稳定获奖时间**：PODC Influential-Paper Award 于 2002 年去世前不久获得，**次年**（2003）奖项更名 Dijkstra Prize——勿写"去世后获奖"或更名年份错误。
- **C&C Prize 2002**：本人收到获奖通知但已去世，由家人在颁奖典礼代领——表述须准确。
- **引语核对**：可引用的原话——The Humble Programmer 的 'We must not forget...'、'Submarines Can Swim'、'a formula is worth a thousand pictures'、'Do only what only you can do'、'The Doomed Discipline'、无参考文献的 'neither explanation nor apology'；母亲"超过五行就错了"是 Dijkstra 转述母亲的话，须保持转述口吻。
- **生卒**：1930-05-11 ~ 2002-08-06，享年 72，出生地 Rotterdam，去世地 Nuenen（癌症）——勿写死因为"未详述"之外的猜测。
- **Dijkstra 算法应用**：OSPF 与 IS-IS——勿扩大到"所有路由协议"。
- **名字发音**：中文惯译"戴克斯特拉"，正文首次出现给出英文全名 Edsger Wybe Dijkstra 即可，注音 DYKE-strə 可不写。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q8556 | 待写入 |
| name_zh | 戴克斯特拉（或 艾兹赫尔·戴克斯特拉） | 待写入 |
| name_en | Edsger W. Dijkstra | 待写入 |
| birth_date | 1930-05-11 | 待写入 |
| death_date | 2002-08-06 | 待写入 |
| nationality | Netherlands | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | theoretical computer science / structured programming / concurrent computing / formal methods | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Adriaan van Wijngaarden（阿姆斯特丹数学中心计算部主任）
- **合作者**：Jaap Zonneveld（首个 ALGOL 60 编译器）、Carel S. Scholten（硬件伙伴、合著 *Predicate Calculus and Program Semantics* 1990）、Bram Jan Loopstra（数学中心硬件）、Ole-Johan Dahl / C.A.R. Hoare（*Structured Programming* 1972 三人合著）
- **引路人**：Johannes Haantjes（Leiden 导师，引荐 van Wijngaarden）
- **著名博士生**：Nico Habermann、Jan van de Snepscheut
- **思想同路人（慎用）**：与 Tony Hoare 的关联限于合著书籍与 Dijkstra Memorial Lecture 首讲——关系类型用 collaborator 即可，勿写"师承"。

## 8. 奖项清单

- ACM A.M. Turing Award（1972，图灵奖）
- 皇家荷兰艺术与科学院院士（1971）
- Distinguished Fellow of the British Computer Society（1971，该奖设立后首位）
- Harry H. Goode Memorial Award（IEEE Computer Society，1974）
- Foreign Honorary Member of the American Academy of Arts and Sciences（1975）
- Honorary DSc, Queen's University Belfast（1976）
- IEEE Computer Society Computer Pioneer Charter Recipient（1982）
- ACM/SIGCSE Outstanding Contributions to Computer Science Education（1989）
- ACM Fellow（1994）
- Honorary doctorate, Athens University of Economics & Business（2001）
- C&C Prize（日本 C&C 基金会，2002）
- ACM PODC Influential-Paper Award（2002）→ 次年更名为 Edsger W. Dijkstra Prize

## 9. 机构清单

- 教育：Gymnasium Erasmianum（1948）、Leiden University（数学物理/理论物理 BS/MS）、University of Amsterdam（PhD 1959）
- 任职：Mathematisch Centrum, Amsterdam（1952–1962，荷兰首位程序员）→ Eindhoven University of Technology 数学系教授（1962–1984，含 THE 系统）→ Burroughs Corporation 唯一 research fellow（1973–，在家工作）→ University of Texas at Austin Schlumberger Centennial Chair（1984–1999-11 退休）

## 10. 终审清单

- [ ] 生卒 1930-05-11 / 2002-08-06，享年 72，出生地 Rotterdam，去世地 Nuenen（癌症）
- [ ] "荷兰第一位程序员 1952"与"婚姻登记程序员轶事 1957"表述准确
- [ ] 最短路径"1956 构思、1959 发表"年份准确
- [ ] ALGOL 60 首编译器"1960-08、与 Zonneveld"表述准确
- [ ] 图灵奖理由 'structured programming languages' 原文表述准确
- [ ] EWD "1300+ 篇全系列 / Burroughs 十年近 500 篇"数字不混淆
- [ ] Go To 信"1968、致 CACM 编辑"表述准确，不写标题来历
- [ ] 自稳定 PODC 奖 2002 / 更名 Dijkstra Prize 次年，表述准确
- [ ] 国籍用「荷兰」，封面底部状态栏 `荷兰 | MC Amsterdam · TU Eindhoven · UT Austin | Turing 1972`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1972/Edsger W. Dijkstra/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `turing/pages/1972/Edsger W. Dijkstra/images/Edsger_Dijkstra_1994.jpg`（infobox 肖像，已就绪；500px 版同目录）
- [ ] **国籍**：封面顶部徽章明示荷兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（本页引语丰富，§5 已列白名单）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Knuth/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（Wilkinson / Bachman）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
