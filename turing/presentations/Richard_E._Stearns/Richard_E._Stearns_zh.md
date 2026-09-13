# Richard E. Stearns（理查德·斯特恩斯）立传提示词

> qid=Q92822 · 1936-07-05 – 在世留白 · 美国计算机科学家 · 20 世纪 · 1993 图灵奖（与 Juris Hartmanis 共享）
> 本地 Wikipedia 数据源：`turing/pages/1993/Richard E. Stearns/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（时间分层定理 / LL 解析 / 下推自动机正则性判定的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Richard Edwin Stearns（中文惯称：理查德·斯特恩斯；熟人称 "Dick" Stearns）
- **生卒**：1936-07-05 生于 Caldwell, New Jersey（美国）→ **在世留白**（页面明载 "born July 5, 1936 ... is an American computer scientist"，无卒日）
- **国籍**：美国（American）
- **身份**：计算机科学家（计算复杂性理论奠基人之一）
- **家庭**：页面无载，禁写
- **教育轨迹**：
  - 1958 年 Carleton College **数学**学士（B.A.）
  - Princeton University **数学**硕士（MA）+ 博士（PhD 1961），论文 *Three person cooperative games without side payments*（无单侧支付的三人合作博弈）
- **博士导师**：Harold W. Kuhn（Princeton 数学家、博弈论家，Kuhn–Tucker 条件之 "Kuhn"）
- **任职**：University at Albany, SUNY —— 现为 Distinguished Professor Emeritus of Computer Science（计算机科学杰出荣休教授）
- **研究领域**：计算复杂性理论、形式语言与自动机、解析算法

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1993 图灵奖（与 Hartmanis 共享）**：获奖理由整句引用 "in recognition of their seminal paper which established the foundations for the field of computational complexity theory"——**篇目侧重：这篇论文由 Stearns 与 Hartmanis 在 GE 合作完成，Stearns 的博士背景是博弈论而非自动机**（Princeton 1961 博士论文是合作博弈论）——从"博弈论数学家到复杂性理论奠基人"是本篇叙事主线。
2. **1965 奠基论文**：与 Hartmanis 合著 *On the computational complexity of algorithms*（Trans. AMS 117: 285–306），包含**时间分层定理**（time hierarchy theorem）——页面明载 "one of the theorems that shaped the field of computational complexity theory"（塑造了计算复杂性理论领域的定理之一）。
3. **1963 前奏**：与 Hartmanis 合著 *Regularity preserving modifications of regular expressions*（Information and Control 6(1): 55–69）——**首次系统研究保持正则语言的语言运算**（页面原文 "A first systematic study"，可写"首个系统性研究"）。
4. **下推自动机正则性判定（1967）**：*A Regularity Test for Pushdown Machines*——回答确定性下推自动机的一个基本问题：**判定给定 DPDA 是否接受正则语言是可判定的**。
5. **LL 解析器的引入（1968）**：与 P.M. Lewis II 合著 *Syntax-Directed Transduction*（JACM 15(3): 465–488）——**引入 LL 解析器（LL parsers）**，在编译器设计中扮演重要角色——这是 Stearns 篇区别于 Hartmanis 篇的**独有亮点**（编译器技术落地）。
6. **空间复杂度合作（与 Lewis、Hartmanis）**：基于空间占用的复杂度类、首个空间分层定理、上下文无关语言 (log n)² 确定性空间结果（此部分两人共享，Hartmanis 篇详述框架、本篇一笔带过避免重复）。
7. **GE 岁月**：与 Hartmanis 在 General Electric Research Laboratory 合作完成奠基工作——本篇从"工业实验室出基础理论"的独特视角切入。
8. **Albany 教学生涯**：University at Albany（SUNY）长期执教至 Distinguished Professor Emeritus——页面未载具体入职年份，勿编造。
9. **荣誉**：Turing Award 1993、ACM Fellow 1994（页面明载 "In 1994 he was inducted as a Fellow of the ACM"）、Frederick W. Lanchester Prize 1995。
10. **门生**：Madhav V. Marathe、Thomas O'Connell（页面 infobox 实载）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（计算复杂性 — 蓝） | `#2E5A9E` | 1965 奠基论文 / 时间分层定理 |
| 分类色 2（形式语言 — 青绿） | `#1E8E8E` | 正则表达式 / 下推自动机正则性 |
| 分类色 3（编译器技术 — 琥珀） | `#D9A441` | LL 解析器 / Syntax-Directed Transduction |
| 分类色 4（博弈论出身 — 玫瑰） | `#C0395B` | Princeton 合作博弈论博士论文 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：嵌套方括号层级图形（[ [ ] [ ] ]），呼应「分层定理 / 语法导向转译」的形式语言视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：求索 / 落地（从博弈论到复杂性理论，再到编译器的实用馈赠）
- **选定曲目**：Alex-Productions **Expedition**（进取 / 探索），匹配"从 Princeton 博弈论青年到 GE 复杂性奠基"的求索叙事。
- **落地文件**：`turing/presentations/Richard_E._Stearns/Expedition.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「计算复杂性理论奠基人 · 美国」+ Stearns 1936– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1936– 生平纵览（Carleton→Princeton→GE→Albany）
4. **新泽西与 Carleton（1936–1958）**：Caldwell 出生、Carleton 数学学士——页面仅此信息，从简不虚构童年
5. **Princeton 博弈论博士（1958–1961）**：Kuhn 门下、三人合作博弈论文——"复杂性理论家的起点是博弈论"
6. **GE 研究实验室**：与 Hartmanis 的相遇与合作（页面未载两人相识细节，勿编造，写"在 GE 合作"即可）
7. **1963 前奏**：正则表达式的保正则运算——首个系统性研究
8. **1965 奠基论文**：时间分层定理（公式框；共享内容，从 Stearns 视角精炼呈现）
9. **下推自动机正则性判定（1967）**：DPDA 接受正则语言的可判定性
10. **LL 解析器（1968）**：Syntax-Directed Transduction、编译器设计中的角色——**本篇独有亮点页**
11. **Albany 执教岁月**：SUNY Albany、杰出荣休教授
12. **荣誉与传承**：Turing 1993、ACM Fellow 1994、Lanchester Prize 1995、门生 Marathe/O'Connell
13. **遗产**：复杂性理论的基石之一、与 Hartmanis 的双星并立
14. **结尾**：品牌页 OpenMathAI

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享结构**：1993 与 Juris Hartmanis **共享**图灵奖；两人篇目侧重区分——**Stearns 篇独有亮点 = 博弈论博士出身 + LL 解析器 + 下推自动机正则性 + Lanchester Prize**；Hartmanis 篇专属 = Cornell CS 系 + 国家政策 + 哥德尔信件 + Berman–Hartmanis 猜想。1965 论文与空间复杂度两块共享内容两侧都写但**详略互补**，禁写页面无载的两人恩怨/分工细节。
- **页面极短警告**：本地 Wikipedia 页面是 **stub**（仅 198 行），可用事实极少——**一切超出本文所列事实的内容均禁写**（家庭、童年、出生地细节、GE 入职年份、Albany 入职年份、去世信息等全无载）。
- **在世留白**：Stearns **在世**（页面用 "is"），无卒日——时间线与结尾页写 `1936–`，勿写卒年。
- **Lanchester Prize 1995**：页面 infobox 实载 Frederick W. Lanchester Prize (1995)——**可列**，但获奖理由页面无载勿编造（该奖实为 ORSA 运筹学著作奖，理由禁写）。
- **"first"红线**：仅 1963 论文的 "A first systematic study of language operations that preserve regular languages"（首个系统研究保正则语言运算）为页面实载可写；LL 解析器写"引入/Introduces"（页面实载），勿写"发明第一个解析器"。
- **引语红线**：全文可用直接引语仅获奖理由整句 "in recognition of their seminal paper which established the foundations for the field of computational complexity theory"——**无其他直接引语，勿编造**。
- **师承**：博士导师 Harold W. Kuhn（Princeton，博弈论）；**勿与 Hartmanis 写成师生关系**（两人是 GE 同事/合作者，页面无载师承）。
- **学位口径**：Carleton BA math 1958、Princeton MA + PhD math 1961（论文三人合作博弈、无单侧支付）——**无 CS 学位**（当时无 CS 博士）。
- **荣誉**：Turing 1993、ACM Fellow 1994、Lanchester Prize 1995——**仅此三项**，无 NAS/NAE（勿编造）。
- **P≟NP**：页面底部导航条有 P≟NP 主题标记，但正文**未载** Stearns 对 P vs NP 的具体立场/贡献——勿引申。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 斯特恩斯（或 理查德·斯特恩斯） | 待写入 |
| name_en | Richard E. Stearns | 待写入 |
| birth_date | 1936-07-05 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computational complexity theory / formal languages / parsing algorithms | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Harold W. Kuhn（Princeton 数学家、博弈论家）
- **核心合作者**：Juris Hartmanis（1963/1965/1966 多篇合著，GE 同事）、P.M. Lewis II（1965 空间复杂度三重论文、1968 LL 解析器）
- **博士生**：Madhav V. Marathe、Thomas O'Connell
- 家庭关系页面无载——禁写。

## 8. 奖项清单

- ACM Turing Award（1993，与 Hartmanis 共享）
- ACM Fellow（1994）
- Frederick W. Lanchester Prize（1995）

## 9. 机构清单

- 教育：Carleton College（数学 B.A. 1958）、Princeton University（数学 MA/PhD 1961）
- 任职：General Electric Research Laboratory（与 Hartmanis 合作期间，页面未载年份区间勿写具体年份）、University at Albany, SUNY（Distinguished Professor Emeritus，入职年份页面无载勿写）

## 10. 终审清单

- [ ] 生卒 1936-07-05 / 在世留白，出生地 Caldwell, New Jersey
- [ ] 1993 与 Hartmanis 共享，获奖理由整句引用准确
- [ ] 博弈论博士出身（Princeton 1961、Kuhn 门下）表述准确
- [ ] LL 解析器 1968 引入表述准确（与 Lewis II 合著）
- [ ] 1967 DPDA 正则性可判定表述准确
- [ ] Lanchester Prize 1995 只列名不写理由
- [ ] stub 页面限制遵守：无载事实一概禁写
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Carleton · Princeton · SUNY Albany | Turing 1993`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1993/Richard E. Stearns/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实（页面极短，全部事实必须能回溯到这 198 行文本）
- [ ] **头像**：使用 `images/Dick_Stearns.jpg`（500px，实际文件名无 500px- 前缀，已核实）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅获奖理由一条）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Hartmanis / Feigenbaum / Reddy / Blum）格式对齐，尤其检查与 Hartmanis 篇的详略互补

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
