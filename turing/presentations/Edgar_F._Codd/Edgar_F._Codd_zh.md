# Edgar F. Codd（埃德加·科德）立传提示词

> qid=Q92596 · 1923-08-19 – 2003-04-18 · 英裔美国计算机科学家 · 20 世纪 · 1981 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1981/Edgar F. Codd/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国→美国`，页面口径 "was a British computer scientist"；图灵奖 citation 记 United States——按 §5 红线处理），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（关系模型三元组 / Codd's theorem「关系代数=关系演算」的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Edgar Frank "Ted" Codd（中文惯称：埃德加·科德，通称 Ted Codd）
- **生卒**：1923-08-19 生于英格兰多塞特郡 Fortuneswell（波特兰岛 Isle of Portland）→ 2003-04-18 逝于佛罗里达 Williams Island（Aventura）家中，享年 79，**死因：心力衰竭（heart failure）**（页面明载）
- **国籍**：英国出生，长期在美工作（页面称 "a British computer scientist"；图灵奖页记 "United States – 1981"——见 §5 红线）
- **身份**：计算机科学家（关系数据库之父，获奖时机构 IBM）
- **教育轨迹**：
  - 中学：Poole Grammar School
  - Exeter College, Oxford：**数学与化学**（B.A.）
  - University of Michigan, Ann Arbor：**M.A.、Ph.D.**（1961–1965 在职攻读；1965 年获博士）
- **博士导师**：John Henry Holland（密歇根，遗传算法之父）
- **博士论文**：*Propagation, Computation, and Construction in Two-dimensional cellular spaces*（1965）——元胞自动机中的自复制
- **二战**：英国皇家空军海防总队（RAF Coastal Command）**飞行员**，驾驶 Sunderlands 飞艇，军衔 flight lieutenant
- **研究领域**：数据库管理、关系模型、元胞自动机、OLAP

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **波特兰岛少年与牛津**：多塞特 Fortuneswell 出生，Poole Grammar School 后入牛津 Exeter College 读数学与化学。
2. **二战 RAF 飞行员**：海防总队驾驶 Sunderland 飞艇，志愿服役升至 flight lieutenant——战后转行计算机。
3. **IBM 早年（1948–1953）**：1948 年迁纽约加入 IBM 任**数学程序员**；先参与 SSEC（Selective Sequence Electronic Calculator）项目，后参与 IBM 701、702 的开发。
4. **1953 年移居渥太华**："dismayed by Senator Joseph McCarthy"——麦卡锡时代移居加拿大渥太华；1957 年返回美国再入 IBM。
5. **密歇根博士（1961–1965）**：师从 John Holland，论文关于元胞自动机自复制——**扩展冯·诺依曼**的工作，证明 **8 个状态**足以实现通用计算与构造；其自复制计算机设计直到 **2010 年**才被实现。
6. **San Jose 与关系模型（1967/1970）**：1967 年（博士两年后）移居加州圣何塞 IBM San Jose Research Laboratory；1970 年发表 *A Relational Model of Data for Large Shared Data Banks*（CACM 13(6)）——关系数据库理论基础（此前一年已有 IBM 内部报告）。
7. **IBM 内部博弈**：IBM 为保住 IMS/DB（层级数据库）收入迟迟不实现关系模型；System R 项目交由不熟悉 Codd 思想的开发者且**将团队与 Codd 隔离**——最终未采用 Codd 的 Alpha 语言而造出非关系式起点的 SEQUEL；即便如此，SEQUEL 远超前关系系统，1979 年被 Larry Ellison 依据 Relational Software Inc 会议论文复制进 **Oracle Database**（Oracle 反而先于 IBM SQL/DS 上市）；因商标原因 SEQUEL 改名 **SQL**。
8. **理论体系**：Alpha 语言、数据库规范化（normalization）、**Boyce–Codd 范式**（与 Boyce 共同命名）、**Codd's theorem**（关系代数与关系演算表达力等价，出自其关系模型开山工作）、**Codd's 12 rules**、Codd's cellular automaton。
9. **12 rules 之战与离开 IBM**：1980s 初关系模型走红，Codd 打了一场"有时激烈"的战役，阻止厂商给旧技术披"关系外衣"（relational veneer）；发表 12 rules 定义何为真关系数据库；此举使其在 IBM 处境艰难，遂离开与 Chris Date 等创办咨询公司——与 Chris Date 长期合作扩展关系模型。
10. **OLAP 与争议**：Codd 创造 **OLAP**（Online analytical processing）术语并写"OLAP 十二法则"；但该 1993 年论文后被发现由 **Arbor Software** 赞助且未披露利益冲突，**Computerworld 撤稿**——保留争议语境。
11. **图灵奖 1981**：citation "For his fundamental and continuing contributions to the theory and practice of database management systems."（整句短）；图灵讲座 *Relational Database: A Practical Foundation for Productivity*（CACM 25(2), 1982）。
12. **身后与传承**：1976 年 IBM Fellow；1994 年 ACM Fellow；1990s 健康恶化停止工作；2004 年 **SIGMOD 将其最高奖更名为 SIGMOD Edgar F. Codd Innovations Award**。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（关系模型 — 蓝） | `#2E5A9E` | 1970 论文 / 关系代数 |
| 分类色 2（数据库规范化 — 青绿） | `#1E8E8E` | BCNF / 12 rules |
| 分类色 3（IBM 内部博弈 — 琥珀） | `#D9A441` | IMS/DB / System R / SEQUEL→SQL |
| 分类色 4（元胞自动机与 OLAP — 玫瑰） | `#C0395B` | Holland 门下博士论文 / OLAP 争议 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「关系即集合」的表格化数据美学。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：开阔 / 持守（一人一模型对抗整个产业惯性）
- **选定曲目**：Alex-Productions **Daylight**（manifest 预分配，直接沿用），匹配"拨云见日、让数据归于关系"的叙事。
- **落地文件**：`turing/presentations/Edgar_F._Codd/Daylight.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「关系数据库之父 · 英国→美国」+ 科德 1923–2003 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1923–2003 生平纵览
4. **多塞特少年与牛津**（1923–1940s）：Fortuneswell、Poole Grammar、Exeter College 数学与化学
5. **RAF 飞行员岁月**（二战）：Coastal Command、Sunderlands、flight lieutenant
6. **IBM 早年与麦卡锡时代**（1948–1957）：SSEC、701/702、1953 移居渥太华、1957 返美
7. **密歇根博士：元胞自动机**（1961–1965）：Holland 门下、8 状态自复制、2010 年才被实现
8. **San Jose 与 1970 关系模型论文**：A Relational Model of Data for Large Shared Data Banks
9. **IBM 内部博弈**：IMS/DB 收入、System R 隔离、Alpha 落选、SEQUEL→SQL、Oracle 抢跑
10. **规范化与 12 rules**：BCNF、Codd's theorem、关系"外衣"之战、与 Chris Date 离开 IBM
11. **图灵奖 1981**：citation 整句 + Relational Database: A Practical Foundation for Productivity
12. **OLAP 与撤稿争议**：术语创造、十二法则、Arbor 赞助与 Computerworld 撤稿
13. **传承**：SIGMOD Codd Innovations Award 2004、IBM Fellow 1976 / ACM Fellow 1994
14. **晚年**：1990s 健康恶化、2003-04-18 心衰逝世于佛州家中
15. **结尾**：79 岁、"关系数据库之父"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由（核心红线）**："For his fundamental and continuing contributions to the theory and practice of database management systems."——整句短 citation，勿扩写。
- **国籍口径**：正文称 "a British computer scientist"；ACM 图灵奖页记 "United States – 1981"（获奖时居美）——封面写「英国→美国」或「英裔美国」，正文可注 ACM 记 United States；勿单写"美国人"。
- **与 Bachman 的关系（禁写）**：1973 图灵奖得主 Bachman（网状模型/ CODASYL）在**本页面完全无载**——禁写 Codd 与 Bachman 的任何个人恩怨、辩论或"模型之争双雄对峙"；可写页面实载的 **IBM 内部**层级数据库（IMS/DB）商业博弈，但不得引申为"Codd vs Bachman"。
- **System R 与 SEQUEL 因果链**：页面明载——IBM 不采用 Codd 的 **Alpha** 语言、团队被隔离、造出 SEQUEL；1979 年 Ellison 依 Relational Software Inc 会议论文复制为 Oracle；因**商标专有状态** SEQUEL 更名 SQL——因果与更名原因勿写反（勿写"因为 Oracle 抢注"以外的演绎）。
- **IMS/DB 性质**：页面称其为 **hierarchical database**（层级数据库）——勿写成网状模型（network model），那是 CODASYL/Bachman 语境。
- **元胞自动机贡献**：8 状态自复制设计**扩展冯·诺依曼**工作；实现迟至 **2010 年**——勿写"早在 1965 年实现"。
- **1970 论文前提**：正式发表前一年（1969）已有 IBM **内部报告**——时间线勿混。
- **OLAP 争议**：1993 论文由 **Arbor Software**（后 Hyperion、再并入 Oracle）赞助、利益冲突未披露、**Computerworld 撤稿**——保留争议实载，勿洗白也勿扩大指控。
- **离开 IBM**：因 12 rules 战役"使其在 IBM 处境日益艰难"而与 Chris Date 等创办咨询公司——按页面实载，勿加"被解雇/被迫出走"演绎。
- **生卒与死因**：1923-08-19 ~ 2003-04-18，享年 79，死因 **heart failure**（家中）——页面明载可写。
- **MIT 迁移细节**："Two years later, he moved to San Jose"——1965 博士 + 两年 = 1967 移居圣何塞；"continued to work until the 1980s"；IBM Fellow **1976**。
- **奖项**：页面仅图灵奖 1981（+ACM Fellow 1994、IBM Fellow 1976、SIGMOD 更名 2004）——无 National Medal 等，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 埃德加·科德（或 科德） | 待写入 |
| name_en | Edgar F. Codd | 待写入 |
| birth_date | 1923-08-19 | 待写入 |
| death_date | 2003-04-18 | 待写入 |
| nationality | United Kingdom（长期居美，ACM 记 United States） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | relational model / database management systems / OLAP | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：John Henry Holland（University of Michigan，遗传算法之父）
- **合作者**：Christopher J. Date（Chris Date，关系模型长期合作者、后共同创办咨询公司）、Raymond F. Boyce（Boyce–Codd normal form 命名对方）、S. B. Codd 与 C. T. Salley（1993 OLAP 论文合著者）
- **学术谱系**：论文扩展 von Neumann 的元胞自动机自复制工作（学术思想承继，按页面实载可作 influence 关系）
- **商业博弈对象**：Larry Ellison（Oracle 借 SEQUEL 论文起家——页面实载单向事实，**禁写两人私人关系**）
- **导师线索**：Exeter College 本科导师页面无载——**无载禁写**

## 8. 奖项清单

- Turing Award（1981）
- IBM Fellow（1976）
- ACM Fellow（1994）
- SIGMOD Edgar F. Codd Innovations Award（2004 年 SIGMOD 最高奖更名以志纪念——非其生前获奖）

## 9. 机构清单

- 教育：Poole Grammar School → Exeter College, Oxford（数学与化学 B.A.）→ University of Michigan, Ann Arbor（M.A.、Ph.D. 1965，1961–1965 在职攻读）
- 任职：IBM（纽约，1948–1953）→ 渥太华（加拿大，1953–1957）→ IBM（返美，1957–1961）→ University of Michigan 在职读博（1961–1965）→ IBM San Jose Research Laboratory（1967–1980s，1976 IBM Fellow）→ 自办咨询公司（与 Chris Date 等，1980s 后）

## 10. 终审清单

- [ ] 生卒 1923-08-19 / 2003-04-18，享年 79，出生地 Fortuneswell（Dorset），去世地 Williams Island（Florida），死因 heart failure
- [ ] 国籍口径「英国出生、美国获奖」处理一致
- [ ] **全文无 Codd–Bachman 关系**（页面无载禁写）
- [ ] IMS/DB 写作"层级数据库"（非网状模型）
- [ ] System R / Alpha / SEQUEL→SQL / Oracle 因果链与页面一致
- [ ] 元胞自动机"8 状态、2010 年才实现"表述准确
- [ ] 图灵奖 citation 整句引用无误；讲座标题与年份（CACM 1982）准确
- [ ] OLAP 赞助撤稿争议按实载保留
- [ ] 肖像文件核对：`images/Edgar_F_Codd.jpg`（已就绪）
- [ ] 封面底部状态栏 `英国→美国 | IBM · Michigan · Oxford | Turing 1981`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1981/Edgar F. Codd/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Edgar_F_Codd.jpg`（已就绪；仅一张，无多尺寸可选）
- [ ] **国籍**：封面顶部徽章按「英国→美国」口径
- [ ] **引语核对**：全文无 Codd 本人直接引语（仅 ACM citation）——引语页只放 citation，**勿编造**
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Hoare / Cook）及 1973 Bachman 篇格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
