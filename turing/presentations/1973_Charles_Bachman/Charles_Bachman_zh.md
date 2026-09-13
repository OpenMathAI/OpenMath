# Charles W. Bachman（查尔斯·巴赫曼）立传提示词

> qid=Q62894 · 1924-12-11 – 2017-07-13 · 美国计算机科学家 · 20 世纪 · 1973 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1973/Charles Bachman/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（网状数据模型 set/membership / Bachman 图分层架构的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Charles William Bachman III（中文惯称：查尔斯·W·巴赫曼，昵称 Charlie）
- **生卒**：1924-12-11 生于 Manhattan, Kansas（美国堪萨斯州）→ 2017-07-13 逝于 Lexington, Massachusetts（家中，帕金森病），享年 92
- **国籍**：美国（American）
- **身份**：计算机科学家——**整个职业生涯都在产业界**（工业研究员、开发者、管理者），而非学术界
- **家庭**：父 Charles Bachman Jr.（堪萨斯州立学院橄榄球主教练，1933–1946 执教 Michigan State College，故 Bachman 在 East Lansing 读中学）；1949 年年中与 Connie Hadley 结婚
- **教育轨迹**：
  - 二战：美国陆军（1944-03 – 1946-02），西南太平洋战场（新几内亚、澳大利亚、菲律宾），防空炮兵部队（Anti-Aircraft Artillery Corps），操作 90mm 火炮的火控计算机——**人生第一次接触计算机**
  - Michigan State College：机械工程 BS（1948，Tau Beta Pi 荣誉学会成员）
  - University of Pennsylvania：机械工程 MS（1950），并修完 Wharton School MBA 三分之二的学分（**未获 MBA 学位**）
- **Known for**：Integrated Data Store（IDS）、Bachman 图（分层架构技术以其命名）
- **主要机构**：Dow Chemical → General Electric → Honeywell Information Systems → Cullinet → Bachman Information Systems

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **火控计算机里的二战**：太平洋战场上用火控计算机瞄准 90mm 高炮——从炮兵到计算机科学家的起点（1944–1946）。
2. **业界而非学界**：与多数图灵奖得主不同，Bachman 终生是"practicing software engineer or manager in industry"——图灵奖史上罕见的纯工业背景得主。
3. **Dow Chemical 与首任数据处理经理**（1950–1960）：1957 年成为 Dow 首任 data processing manager；与 IBM 用户组 SHARE 合作开发新版报表生成器 9PAC（后 IBM 709 订单取消）。
4. **Integrated Data Store（IDS，1963）**：在 GE 期间于 MIACS（Manufacturing Information And Control System）产品中开发——**最早的数据库管理系统之一**，采用后来被称为"导航式（navigational）数据库"的模型；1973 年图灵奖的核心贡献。
5. **早期 OLTP 先行者 WEYCOS（1965）**：为客户 Weyerhaeuser Lumber 开发——首个对 IDS 数据库的多程序网络访问，早期在线事务处理系统。
6. **dataBasic**：在 GE 开发、为 Basic 语言分时用户提供数据库支持的产品。
7. **GE→Honeywell（1970）**：GE 计算机业务卖给 Honeywell，举家从 Phoenix 搬到 Lexington, Massachusetts。
8. **IDMS 与 Cullinet（1981）**：加入 Cullinane Information Systems（后 Cullinet）——其 IDS 版本 IDMS 支持 IBM 大型机（网状数据库的商业生命力延续）。
9. **Bachman Information Systems（1983）**：创办 CASE（计算机辅助软件工程）公司，核心产品 BACHMAN/Data Analyst 为 Bachman 图的创建维护提供图形支持；1991 年 NASDAQ 上市（代码 BACH，1992-02 高点 $37.75，1995 跌至 $1.75）；1996 年与 Cadre Technology 合并为 Cayenne Software，任总裁一年后退休至 Tucson（后任董事长至 1998 年 Cayenne 被 Sterling Software 收购）。
10. **Bachman 图**：分层架构（layered architecture）技术以他命名——数据库设计的经典表达工具；1969 年发表 *Data Structure Diagrams* 奠基。
11. **图灵奖（1973）**：获奖理由 "for his outstanding contributions to database technology"（对数据库技术的杰出贡献）；图灵奖演讲 *The Programmer as Navigator*（"作为领航员的程序员"，CACM 1973-11）——第一位因数据库工作获图灵奖的得主（本页未明载"第一位"，禁写；只写获奖事实）。
12. **荣誉**：Distinguished Fellow of the British Computer Society（1977）、美国国家技术创新奖章 National Medal of Technology and Innovation（2012，"for fundamental inventions in database management, transaction processing, and software engineering"）、ACM Fellow（2014）、Computer History Museum Fellow（2015）；退休后志愿整理早期软件开发史——2002 年 CHM 讲座 "Assembling the Integrated Data Store"、2004 年 ACM 口述史、2011 年 IEEE 口述史；1951–2007 年个人文件藏于明尼苏达大学 Charles Babbage Institute。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（数据库 — 蓝） | `#2E5A9E` | IDS / 数据库奠基 |
| 分类色 2（网状模型 — 青绿） | `#1E8E8E` | 导航式模型 / Bachman 图 |
| 分类色 3（工业生涯 — 琥珀） | `#D9A441` | Dow / GE / Honeywell / Cullinet |
| 分类色 4（软件工程 — 玫瑰） | `#C0395B` | CASE / Bachman Information Systems |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：网状节点连线（record-set 环形小圈相连），呼应「CODASYL 网状模型结构图」（本地有插图 `CodasylB.png` 可用于贡献页）。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：拓荒 / 远征（数据库工业拓荒者的叙事）
- **选定曲目**：Alex-Productions **Expedition**（远征 / 开阔），匹配"从太平洋炮兵到数据库奠基人"的工业远征叙事；与同代已用的 New Lands / Timeless / Falling Apart / Pathfinder 区分。
- **落地文件**：`turing/presentations/Charles_Bachman/Expedition.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「数据库奠基人 · 美国」+ Bachman 1924–2017 + 右上头像（2012 年照）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1924–2017 生平纵览
4. **早年：橄榄球教练之子与太平洋战场**（1924–1946）：Kansas → East Lansing、陆军防空炮兵、火控计算机初体验
5. **工程师的养成**（1946–1950）：Michigan State 机械工程、Penn 硕士、Wharton 三分之二 MBA
6. **Dow Chemical：首任数据处理经理**（1950–1960）：SHARE、9PAC
7. **IDS：最早的数据库管理系统之一**（1963）：GE、MIACS、导航式模型
8. **WEYCOS 与早期 OLTP**（1965）：Weyerhaeuser、多程序网络访问、dataBasic
9. **Bachman 图**：Data Structure Diagrams（1969）、分层架构以其命名
10. **GE→Honeywell→Cullinet**（1970–1981）：IDMS 与 IBM 大机
11. **图灵奖 1973**：'for his outstanding contributions to database technology'、演讲 The Programmer as Navigator
12. **Bachman Information Systems**（1983–1996）：CASE、BACH 上市、Cayenne 合并
13. **荣誉与晚年**：国家技术创新奖章 2012、ACM Fellow 2014、CHM Fellow 2015、口述史与档案
14. **遗产**：数据库技术的奠基者、业界图灵奖得主的样本
15. **结尾**：92 岁、"程序员作为领航员"的历史回声

## 5. 史实陷阱与敏感点（终审必须检查）

- **父与子的名字**：父 Charles Bachman **Jr.**、本人 Charles William Bachman **III**——后缀勿写混。
- **Wharton MBA**：只**修完三分之二学分**、**未获得 MBA 学位**——勿写"MBA 学位"。
- **获奖时机构**：1973 年获奖时供职 **Honeywell Information Systems**（GE 计算机业务 1970 年出售给 Honeywell；CBI 档案注明 GE 1960–1970、Honeywell 1970–1981）——总表"获奖时机构 —"应据此更正为 Honeywell Information Systems；勿写"GE"或"Cullinet"。
- **IDS 与 CODASYL 的关系**：页面只说 IDS 用"后来被称为导航式数据库的模型"、图注为 "Basic structure of navigational CODASYL database model"、且列有 Bachman 的多篇 CODASYL 相关论文——**页面未明写"IDS 是 CODASYL 规范的基础"**，此因果链禁写；表述限于"导航式模型"与"Bachman 参与 CODASYL 相关工作"。
- **"数据库奠基"表述**：获奖理由原文是 'outstanding contributions to database technology'——勿延伸为"发明数据库"或"关系数据库之父"（关系模型属 Codd，1981）。
- **首位数据库图灵奖得主**：页面**无载**，禁写"第一位因数据库获奖的人"。
- **NASDAQ 曲线**：1991 IPO（BACH）、1992-02 高点 $37.75、1995 跌至 $1.75——数字方向勿写反（是暴跌不是上涨）。
- **退休地点**：从 Cayenne 退休后居 **Tucson, Arizona**；去世地是 **Lexington, Massachusetts** 家中（帕金森病，92 岁）——两个地点勿混淆。
- **军旅细节**：1944-03 – 1946-02、South West Pacific Theater、Anti-Aircraft Artillery Corps、新几内亚/澳大利亚/菲律宾、90mm 火炮火控计算机——年份与地点勿写混。
- **荣誉边界**：Turing 1973、DFBCS 1977、National Medal 2012、ACM Fellow 2014、CHM Fellow 2015——**无** Nobel（勿编造）。
- **妻子**：Connie Hadley（1949 年年中结婚）——页面仅此一笔，勿展开。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q62894 | 待写入 |
| name_zh | 巴赫曼（或 查尔斯·巴赫曼） | 待写入 |
| name_en | Charles W. Bachman | 待写入 |
| birth_date | 1924-12-11 | 待写入 |
| death_date | 2017-07-13 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | database management systems / navigational database / software engineering | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **业界同事与合作**：Thomas Haigh（数据库史家，为其作传与访谈——历史学者关系，可视需要略去）
- **无载禁写**：页面未载其博士导师（机械工程背景、无导师信息）、未载学术门生——**勿编造导师/门生关系**；与 Codd 的"关系模型 vs 网状模型"对比可在正文提（学界公论），但**不建两人关系条目**（页面无直接互动记载）。

## 8. 奖项清单

- ACM Turing Award（1973，图灵奖，"for his outstanding contributions to database technology"）
- Distinguished Fellow of the British Computer Society（1977）
- National Medal of Technology and Innovation（2012）
- ACM Fellow（2014）
- Computer History Museum Fellow（2015）

## 9. 机构清单

- 教育：Michigan State College（机械工程 BS 1948）、University of Pennsylvania（机械工程 MS 1950 + Wharton 2/3 MBA）
- 任职：Dow Chemical（1950–1960，1957 年起首任 data processing manager）→ General Electric（1960–1970，IDS/WEYCOS/dataBasic）→ Honeywell Information Systems（1970–1981，GE 计算机业务并入）→ Cullinane/Cullinet（1981–，IDMS）→ Bachman Information Systems 创始人（1983–1996）→ Cayenne Software 总裁/董事长（1996–1998）

## 10. 终审清单

- [ ] 生卒 1924-12-11 / 2017-07-13，享年 92，出生地 Manhattan, Kansas，去世地 Lexington, MA（家中帕金森病）
- [ ] "终生业界非学界"定位表述准确
- [ ] IDS 1963 / WEYCOS 1965 / dataBasic / IDMS 时间线准确
- [ ] 图灵奖理由 'outstanding contributions to database technology' 原文表述准确
- [ ] 获奖时机构更正为 Honeywell Information Systems
- [ ] Wharton"修完 2/3 学分未获学位"表述准确
- [ ] NASDAQ BACH"1992 高点 $37.75 → 1995 跌至 $1.75"方向正确
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Dow · GE · Honeywell · Cullinet | Turing 1973`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1973/Charles Bachman/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `turing/pages/1973/Charles Bachman/images/Charles_Bachman_2012.jpg`（2012 年照，已就绪；330px 版同目录）
- [ ] **插图**：贡献页可用 `images/CodasylB.png`（CODASYL 网状模型结构图）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由、国家奖章理由、演讲标题）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Knuth/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（Wilkinson / Dijkstra）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
