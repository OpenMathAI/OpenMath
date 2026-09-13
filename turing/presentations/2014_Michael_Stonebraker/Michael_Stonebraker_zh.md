# Michael Stonebraker（迈克尔·斯通布雷克）立传提示词

> qid=Q92758 · 1943-10-11 生（在世留白） · 美国计算机科学家 · 20/21 世纪 · 2014 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2014/Michael Stonebraker/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（关系模型 / Ingres 架构要点 / 列存 vs 行存 的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Michael Ralph Stonebraker（中文惯称：迈克尔·斯通布雷克）
- **生卒**：1943-10-11 生于 Newburyport, Massachusetts（美国）→ **在世留白**（页面无卒日，勿编造）
- **成长地**：Milton Mills, New Hampshire 长大
- **国籍**：美国（American）
- **身份**：计算机科学家，专攻数据库系统（database systems）
- **家庭**：妻子 Beth（页面 infobox 实载，仅一笔带过）
- **教育轨迹**：
  - Princeton University 电机工程 **B.S.E.**（1965）
  - University of Michigan **M.S.**（1967）+ **Ph.D.**（1971），博士论文 *The Reduction of Large Scale Markov Models for Random Chains*（注意：是随机链马尔可夫模型，**不是数据库方向**）
- **博士导师**：Arch Waugh Naylor（Michigan）
- **研究领域**：数据库系统、关系数据库、列存/流数据管理
- **任职**：UC Berkeley（Berkeley 阶段）、University of Michigan、MIT（2001 起，CSAIL）；现为 UC Berkeley 荣休教授 + MIT CSAIL adjunct professor emeritus

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **职业生涯两阶段**：Berkeley 时代（Ingres / Postgres 关系数据库）+ 2001 年起 MIT 时代（C-Store / H-Store / SciDB / DBOS 等新型数据管理）——页面原文即此两分法，时间线据此展开。
2. **Ingres（1973）**：与同事 **Eugene Wong** 读到 Edgar F. Codd 关系模型论文后启动；与 IBM System R 并列、最早证明关系模型可被高效实用实现的系统之一。遗留思想至今通用：B-trees、primary-copy 复制、视图/完整性约束的 query rewrite、rules/triggers、事务锁系统。
3. **学术创业第一波**：与 Berkeley 同事 Larry Rowe、Eugene Wong 共同创办 **Relational Technology, Inc.**（后称 Ingres Corporation）→ 售予 Computer Associates → 2005 年独立 → 更名 **Actian**；学生 Robert Epstein 由 Ingres 派生创办 **Sybase**（其代码后来成为 Microsoft SQL Server 的基础）。
4. **POSTGRES（"post-Ingres"）**：与 Larry Rowe 启动，针对关系模型的局限（对象关系扩展）；页面仅载项目名 POSTGRES（POST inGRES）与设计论文（1986）。
5. **MIT 时代：Aurora 与 StreamBase**：与 Brandeis / Brown / MIT 同事做流数据管理——关系系统"拉"数据逐条处理，Aurora 中数据被"推"入系统（股票行情、新闻源、传感器），输出本身是结果流。
6. **C-Store 与 Vertica（2005）**：并行、shared-nothing、**列存** DBMS 用于数据仓库；按列存储减少 I/O、压缩率更高（同名数据相邻 Name,Name,Name… vs Name,Address,Zip…）；2005 年共同创办 **Vertica** 商业化。
7. **SciDB（2008）**：与 David DeWitt 及 Brown/MIT/Portland State/SLAC/UW/UW–Madison 研究者共同启动的**科学应用**开源 DBMS；与 Marilyn Matz 创办 **Paradigm4**（客户含 Novartis、Foundation Medicine、NIH）。
8. **批评 NoSQL（2010–2011）**：在 Communications of the ACM 发文批评 NoSQL 运动——保留"论战者"语境，按页面实载表述。
9. **连续创业者**：创办/共同创办 Ingres Corporation、Illustra、Paradigm4、StreamBase、Tamr、Vertica、VoltDB、Hopara，并曾任 **Informix 首席技术官**——"学者型连续创业者"是本篇最大人设。
10. **H-Store / DBOS**：MIT 阶段页面提及的新数据管理技术（仅列出，无展开——不要过度铺陈细节）。
11. **荣誉**：2014 图灵奖（2015 年 3 月公布）、IEEE John von Neumann Medal 2005、首个 SIGMOD Edgar F. Codd Innovations Award、ACM Fellow 1994、NAE 院士 1997（理由：关系与对象关系数据库系统的开发与商业化）、2015 Commonwealth Award（MassTLC）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（关系数据库 — 蓝） | `#2E5A9E` | Ingres / Codd 关系模型 |
| 分类色 2（对象关系 — 青绿） | `#1E8E8E` | POSTGRES |
| 分类色 3（列存与流 — 琥珀） | `#D9A441` | C-Store / Vertica / Aurora / StreamBase |
| 分类色 4（学术创业 — 玫瑰） | `#C0395B` | Vertica / VoltDB / Tamr / Paradigm4 等公司群像 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和数据块（稀疏竖条/列状矩形），呼应「行存 vs 列存」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：沉稳 / 重构（数据库四十年的迭代者）
- **选定曲目**：Alex-Productions **Pathfinder**（manifest 预分配，直接沿用），匹配"一次次推倒重来的数据库探索者"叙事。
- **落地文件**：`turing/presentations/Michael_Stonebraker/Pathfinder.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「数据库宗师 · 美国」+ Stonebraker 1943– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 成长地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1943–至今 生平纵览（Berkeley 阶段 / MIT 阶段两段式）
4. **早年与教育**：Newburyport 出生、Milton Mills 长大、Princeton 电机 1965、Michigan 硕博 1967/1971（马尔可夫模型论文）
5. **Codd 的召唤：Ingres 启动**（1973）：与 Eugene Wong 读 Codd 论文、与 System R 并列的可行性证明
6. **Ingres 的技术遗产**：B-trees、primary-copy 复制、query rewrite、rules/triggers、锁系统
7. **学术创业第一波**：Relational Technology → Ingres Corp → Actian；Sybase / Britton Lee；SQL Server 渊源
8. **POSTGRES：超越关系模型**：与 Larry Rowe、对象关系扩展
9. **移师 MIT（2001）**：两阶段职业的转折点
10. **Aurora 与 StreamBase：流数据**："推"模型 vs "拉"模型
11. **C-Store 与 Vertica：列存革命**（2005）：列存 I/O 与压缩优势
12. **SciDB 与科学数据**（2008）：与 DeWitt、Paradigm4
13. **论战者 Stonebraker**：批评 NoSQL（2010–2011，CACM）
14. **荣誉与传承**：Turing 2014、von Neumann Medal 2005、Codd Innovations Award；门生 Hellerstein / Seltzer / Hearst 等
15. **结尾**：在世留白；"从 Ingres 到 DBOS"的数据库四十年

## 5. 史实陷阱与敏感点（终审必须检查）

- **"database dinosaurs" 观点**：本地页面**无载**，**禁写**该说法及其任何相关轶事。
- **PostgreSQL 演化**：页面只写 **POSTGRES**（POST inGRES）项目本身；"POSTGRES → PostgreSQL 更名演化"在页面**无载**，禁写演化叙事，勿把 PostgreSQL 当获奖理由。
- **图灵奖获奖理由（ACM citation）**：页面**未载完整 citation**，只载 "often described as 'the Nobel Prize for computing'"。执行时勿自行编写 citation 全文，写"因其对数据库研究的贡献获 2014 图灵奖"即可，或标注"citation 以 ACM 官方为准"。
- **博士论文方向**：Michigan 1971 博士论文是**随机链马尔可夫模型约简**（控制论方向），**不是数据库**——勿写成"数据库博士"。
- **学位名称**：Princeton 是 **B.S.E.**（电机工程）；勿写 CS 学位。
- **Ingres 全称**：页面作 Interactive Graphics and Retrieval System——若写全称以此为准。
- **公司归属**：Ingres 出售后 2005 年重立、后更名 Actian；Sybase 是学生 Robert Epstein 创办、非 Stonebraker 本人创办；SQL Server 基于 Sybase 代码——因果链按页面写，勿加戏。
- **两阶段结构勿混**：Ingres/Postgres 属 Berkeley 阶段；C-Store/H-Store/SciDB/DBOS 属 MIT 阶段（2001 起）——年份与阶段勿错配。
- **C-Store 与 Vertica 同为 2005**：项目启动与公司创办同年，勿写成不同年份。
- **在世留白**：born 1943-10-11，页面无卒日，写作 `1943–`。
- **家庭**：仅妻子 Beth 有载；其余家庭细节勿编造。
- **引语**：全文无直接引语（"the Nobel Prize for computing" 是转述描述非本人原话），**勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 斯通布雷克（或 迈克尔·斯通布雷克） | 待写入 |
| name_en | Michael Stonebraker | 待写入 |
| birth_date | 1943-10-11 | 待写入 |
| death_date | NULL（在世） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | database systems / relational databases | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Arch Waugh Naylor（University of Michigan）
- **合作者**：Eugene Wong（Ingres 共同启动）、Larry Rowe（POSTGRES、Relational Technology 共同创办）
- **学术对手/参照**：Edgar F. Codd（关系模型奠基，读其论文而起）、David DeWitt（SciDB 合作者）
- **著名学生**：Joseph M. Hellerstein、Margo Seltzer、Marti Hearst、Sunita Sarawagi、Clifford A. Lynch、Dale Skeen、Leilani Battle；学生 Robert Epstein 创办 Sybase
- **页面无载的关系**：勿补（如与 PostgreSQL 社区关系、与各公司后继者关系）

## 8. 奖项清单

- ACM Turing Award（2014，2015 年 3 月公布；"the Nobel Prize for computing"）
- IEEE John von Neumann Medal（2005）
- SIGMOD Edgar F. Codd Innovations Award（首个，年份页面未载勿写具体年）
- ACM Fellow（1994）
- National Academy of Engineering 院士（1997，"关系与对象关系数据库系统的开发与商业化"）
- Commonwealth Award（MassTLC，2015）

## 9. 机构清单

- 教育：Princeton University（B.S.E. EE 1965）、University of Michigan（MS 1967 / PhD 1971）
- 任职：University of Michigan、UC Berkeley（教授，至荣休）、MIT CSAIL（2001–，adjunct professor emeritus）
- 创办企业：Relational Technology/Ingres Corp（→ Actian）、Illustra、StreamBase、Vertica、VoltDB、Tamr、Paradigm4、Hopara；Informix CTO

## 10. 终审清单

- [ ] 生卒 1943-10-11 / 在世留白，出生地 Newburyport, MA
- [ ] 博士论文为马尔可夫模型（非数据库），Michigan 1971，导师 Naylor
- [ ] "database dinosaurs" 无载禁写；PostgreSQL 演化无载禁写
- [ ] 图灵奖 citation 不自行编造（页面未载全文）
- [ ] Ingres 1973 与 Eugene Wong、System R 并列表述准确
- [ ] C-Store 与 Vertica 均为 2005
- [ ] Berkeley/MIT 两阶段结构不混
- [ ] Sybase 归属学生 Robert Epstein
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | UC Berkeley · MIT | Turing 2014`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2014/Michael Stonebraker/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2015 图灵讲座肖像（`images/500px-Michael_Stonebraker_P1120062.jpg`，取最大可用版）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：全文无直接引语，勿编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Diffie / Hellman）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
