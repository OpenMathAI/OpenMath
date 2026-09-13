# Juris Hartmanis（尤里斯·哈特马尼斯）立传提示词

> qid=Q92628 · 1928-07-05 – 2022-07-29 · 拉脱维亚裔美国计算机科学家、计算理论家 · 20 世纪 · 1993 图灵奖（与 Richard E. Stearns 共享）
> 本地 Wikipedia 数据源：`turing/pages/1993/Juris Hartmanis/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 拉脱维亚裔·美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（复杂度类 / 时间分层定理 / 空间复杂度 (log n)² 的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Juris Hartmanis（中文惯称：尤里斯·哈特马尼斯）
- **生卒**：1928-07-05 生于里加（Riga，拉脱维亚）→ 2022-07-29 去世，享年 94（页面未载去世地点与死因，勿编造）
- **国籍**：拉脱维亚出生，美国（Latvian-born American）
- **身份**：计算机科学家、计算理论家（计算复杂性理论奠基人之一）
- **家庭**：父 Mārtiņš Hartmanis（拉脱维亚陆军将军，1940 苏联占领拉脱维亚后被捕、死于狱中）；母 Irma Marija Hartmane；姐姐是诗人 Astrid Ivask（Hartmanis 为其弟）
- **流亡轨迹**：1944 年二战中随家人离开拉脱维亚赴德国（惧怕苏联再次占领）
- **教育轨迹**：
  - Marburg 大学（德国）：物理学同等硕士学位
  - 1951 年 University of Kansas City（今 University of Missouri–Kansas City）**应用数学**硕士
  - 1955 年 Caltech **数学**博士，论文 *Some embedding theorems for lattices*（格的嵌入定理）
- **博士导师**：Robert P. Dilworth（Caltech 数学家）
- **研究领域**：计算复杂性理论、自动机理论、代数结构理论

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1993 图灵奖（与 Stearns 共享）**：获奖理由整句引用 "in recognition of their seminal paper which established the foundations for the field of computational complexity theory"——表彰其开创性论文**奠定了计算复杂性理论领域的基础**。
2. **1965 奠基论文**：与 Stearns 合著 *On the computational complexity of algorithms*（Trans. AMS 117: 285–306）——定义了**复杂度类**这一基础概念（按求解所需时间对计算问题分类），并证明多个基本结果如**时间分层定理**。
3. **Karp 的历史定位**（可直接引用，出处 Karp 1986 图灵奖演讲）："[I]t is the 1965 paper by Juris Hartmanis and Richard Stearns that marks the beginning of the modern era of complexity theory."——"1965 年的这篇论文标志着复杂性理论现代时期的开端"。
4. **空间复杂度三重奏**（与 P.M. Lewis II、Stearns）：基于空间占用的复杂度类定义、证明**首个空间分层定理**；同年证明每个上下文无关语言的确定性空间复杂度为 (log n)²——其**核心思想直接导向 Savitch 定理**（注意：是"核心思想导向"，Savitch 定理本身不是三人证明的）。
5. **GE 研究实验室岁月（1958）**：在 Cornell、Ohio State 任数学教职后加入 General Electric Research Laboratory——**在 GE 期间发展了计算复杂性理论的许多原理**（1964 与 Stearns 的 "Computational complexity of recursive sequences" 是前奏）。
6. **Cornell CS 系创始主任（1965）**：1965 年成为 Cornell 教授，是 Cornell 计算机科学系的**创建者之一与第一任系主任**；该系是**世界最早的 CS 系之一**（勿写"第一个"——页面脚注明载 Purdue 1962 年创建首个 CS 系，Cornell/Stanford/CMU 均为 1965 年前后第一批）。
7. **Berman–Hartmanis 同构猜想（1977，与 Leonard Berman）**：证明所有自然 NP-完全语言在多项式时间同构，并猜想对全部 NP-完全集成立——猜想至今未决，但催生大量研究，最终结出 **Mahaney 定理**（稀疏 NP-完全集不存在）。
8. **布尔分层（Boolean hierarchy）**：与 Cai、Gundermann、Hemachandra 等合作者共同定义。
9. **哥德尔信件的考古（1989）**：对一封 1956-03-20 哥德尔致冯·诺依曼的信的解读，为复杂性理论的**史前史**带来新洞见——哥德尔在该信中**首次**质疑 NP-完全等价问题能否在二次或线性时间内求解，预示 P=NP? 问题。
10. **国家层面的学科建设者**：主持 National Research Council 研究，成果为 1992 年报告 *Computing the Future – A Broad Agenda for Computer Science and Engineering*；1996–1998 任 NSF CISE（计算机与信息科学工程部）助理主任。
11. **门生**：Allan Borodin（1969）、Dexter Kozen（1977）、Neil Immerman（1980）、Jin-Yi Cai（1986）——个个是复杂性理论名家。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（计算复杂性 — 蓝） | `#2E5A9E` | 1965 奠基论文 / 复杂度类 |
| 分类色 2（分层定理 — 青绿） | `#1E8E8E` | 时间/空间分层定理 |
| 分类色 3（代数结构 — 琥珀） | `#D9A441` | 序贯机代数结构理论 / 格论博士出身 |
| 分类色 4（学科建设 — 玫瑰） | `#C0395B` | Cornell CS 系 / Computing the Future / NSF |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：分层谱系线（自上而下渐细的水平细线组），呼应「时间/空间分层定理」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：流亡与奠基（里加少年→GE 车库岁月→复杂性理论的现代纪元）
- **选定曲目**：Alex-Productions **The Flow of Time**（深沉 / 流逝），匹配"从战乱流亡到奠定一个学科"的时间叙事。
- **落地文件**：`turing/presentations/Juris_Hartmanis/TheFlowOfTime.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「计算复杂性理论奠基人 · 拉脱维亚裔·美国」+ Hartmanis 1928–2022 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1928–2022 生平纵览（里加→德国→美国→GE→Cornell→NSF）
4. **里加的将军之子（1928–1944）**：父被捕死于狱中、诗人姐姐、1944 全家流亡德国——按页面实载一笔带过，不渲染
5. **从物理到数学（1944–1955）**：Marburg 物理、Kansas City 应用数学、Caltech 格论博士（Dilworth 门下）
6. **GE 研究实验室（1958–1965）**：工业实验室里的理论萌芽，1964 递归序列复杂度
7. **1965 奠基论文**：复杂度类 + 时间分层定理 + Karp 引语（公式框）
8. **空间复杂度三重奏**：与 Lewis/Stearns 的空间分层定理、(log n)² 与 Savitch 定理的渊源
9. **Cornell CS 系创始主任（1965）**：世界最早 CS 系之一的创建
10. **Berman–Hartmanis 猜想**：NP-完全同构、Mahaney 定理、布尔分层
11. **哥德尔信件考古（1989）**：1956-03-20 信件、P=NP? 的史前史
12. **学科建设的国家视野**：Computing the Future（1992）、NSF CISE（1996–1998）
13. **荣誉与传承**：Turing 1993、NAE/NAS/AAAS、门生 Borodin/Kozen/Immerman/Cai
14. **遗产**：现代复杂性理论的起点、94 岁谢幕
15. **结尾**：品牌页 OpenMathAI

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享结构**：1993 与 Richard E. Stearns **共享**图灵奖，两人篇目侧重区分——Hartmanis 篇侧重**奠基论文的复杂度类/分层定理框架 + Cornell 学科建设 + 国家政策**，Stearns 篇侧重 LL 解析器等个人后续工作；**禁写页面无载的两人内部恩怨/分工细节**。
- **"第一个 CS 系"**：Cornell CS 系是**世界最早之一**（页面脚注明载 Purdue 1962 为第一个，Cornell 1965）——勿写"全世界第一个 CS 系"。
- **Savitch 定理**：三人 1965 年 (log n)² 结果包含**导向 Savitch 定理的核心思想**——勿写成"三人证明了 Savitch 定理"。
- **"首位/第一"红线**：时间分层定理、首个空间分层定理为页面实载可写；其余"唯一/第一"表述页面无载禁写。
- **家庭流亡史**：父 Mārtiņš 被苏联逮捕死于狱中、1944 全家离拉赴德——**按页面实载一笔带过**，不渲染战争细节，不做政治评价。
- **哥德尔信件表述**：写"哥德尔在该信中首次质疑 NP-完全等价问题能否二次/线性时间求解，预示 P=NP?"——是 Hartmanis 1989 年解读的转述，勿扩写成"P=NP 由哥德尔提出"。
- **Berman–Hartmanis 猜想**：**至今开放**（页面明载 remains open）——勿写"已被证明"。
- **学位口径**：Marburg=物理**同等硕士**（页面作 equivalent of a master's degree in physics）；Kansas City=应用数学硕士 1951；Caltech=数学博士 1955，导师 Dilworth——勿写成"物理学博士"。
- **生卒**：1928-07-05 ~ 2022-07-29，享年 94；去世地点与死因页面未载，勿编造。
- **引语红线**：全文可用的直接引语仅两条——①图灵奖获奖理由整句；②Karp 1986 图灵奖演讲中的 "1965 paper ... marks the beginning of the modern era of complexity theory" 句。**其余勿编造引语**。
- **荣誉**：NAE 1989、NAS 2013、AAAS Fellow 1981、American Academy of Arts and Sciences 1992、Latvian Academy 外籍院士 1990 + Grand Medal 2001、Humboldt 1993、ACM Charter Fellow 1994、CRA 杰出服务奖 2000、ACM 杰出服务奖 2013、AMS 首批 Fellow 2013、UMKC 荣誉博士 1999——**无** Nobel/美国国家科学奖章（勿编造）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 哈特马尼斯（或 尤里斯·哈特马尼斯） | 待写入 |
| name_en | Juris Hartmanis | 待写入 |
| birth_date | 1928-07-05 | 待写入 |
| death_date | 2022-07-29 | 待写入 |
| nationality | United States（Latvia-born） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computational complexity theory / automata theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Robert P. Dilworth（Caltech 数学家，格论）
- **核心合作者**：Richard E. Stearns（1965 奠基论文、《序贯机代数结构理论》1966 合著）、P.M. Lewis II（空间复杂度三重论文）、Leonard Berman（Berman–Hartmanis 猜想）、Jin-Yi Cai（布尔分层）
- **著名博士生**：Allan Borodin（1969）、Dexter Kozen（1977）、Neil Immerman（1980）、Jin-Yi Cai（1986）
- **历史人物（仅叙事关联，不入 relation）**：Gödel、von Neumann（1956 信件解读对象）
- 页面对 Stearns 的导师/门生关系**无载**（两人是同事合作者而非师生）——勿写师生关系。

## 8. 奖项清单

- ACM Turing Award（1993，与 Stearns 共享）
- AAAS Fellow（1981）
- National Academy of Engineering 院士（1989）
- Latvian Academy of Sciences 外籍院士（1990）、Grand Medal（2001）
- American Academy of Arts and Sciences 院士（1992）
- Humboldt Foundation Research Award（1993）
- ACM Charter Fellow（1994）
- Honorary Doctor of Humane Letters, University of Missouri–Kansas City（1999）
- CRA Distinguished Service Award（2000）
- ACM Distinguished Service Award（2013）
- American Mathematical Society 首批 Fellow（2013）
- National Academy of Sciences 院士（2013）

## 9. 机构清单

- 教育：University of Marburg（物理同等硕士）、University of Missouri–Kansas City（应用数学 MS 1951）、Caltech（数学 PhD 1955）
- 任职：Cornell University 数学教职、Ohio State University 数学教职、General Electric Research Laboratory（1958–1965）、Cornell University 教授 + CS 系创始主任（1965 起）、NSF CISE 助理主任（1996–1998）

## 10. 终审清单

- [ ] 生卒 1928-07-05 / 2022-07-29，享年 94，出生地 Riga，去世地/死因留白
- [ ] 1993 与 Stearns 共享，获奖理由整句引用准确
- [ ] 1965 论文 = Trans. AMS 117，复杂度类 + 时间分层定理
- [ ] Cornell CS 系为"最早之一"（非第一个），创始主任表述准确
- [ ] (log n)² 与 Savitch 定理的"核心思想导向"关系准确
- [ ] Berman–Hartmanis 猜想"至今开放"表述准确
- [ ] 家庭流亡史一笔带过不渲染
- [ ] 国籍用「拉脱维亚裔·美国」，封面底部状态栏 `拉脱维亚裔·美国 | GE · Cornell · NSF | Turing 1993`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1993/Juris Hartmanis/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Juris_Hartmanis_2002_.jpg`（2002 年肖像，取最大可用版）
- [ ] **国籍**：封面顶部徽章明示拉脱维亚裔·美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅获奖理由 + Karp 引语两条）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Stearns / Feigenbaum / Reddy / Blum）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
