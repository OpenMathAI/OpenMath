# Fred Brooks（弗雷德·布鲁克斯）立传提示词

> qid=Q92609 · 1931-04-19 – 2022-11-17 · 美国计算机体系结构师、软件工程师 · 20 世纪 · 1999 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1999/Fred Brooks/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Brooks's law / 8-bit byte 决策的表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Frederick Phillips Brooks Jr.（中文惯称：弗雷德·布鲁克斯）
- **生卒**：1931-04-19 生于 Durham, North Carolina（美国）→ 2022-11-17 逝于 Chapel Hill, North Carolina，享年 91（页面实载：中风后健康状况不佳 poor health following a stroke）
- **国籍**：美国（American）
- **身份**：计算机体系结构师（computer architect）、软件工程师、计算机科学家；以管理 IBM System/360 研发并写下《人月神话》闻名
- **家庭**：1956 年与 Nancy Lee Greenwood 结婚，育三子女；长子的名字取自 Kenneth E. Iverson；福音派基督徒，积极参与 InterVarsity Christian Fellowship
- **教育轨迹**：
  - Duke University 物理学学士（BS，1953）
  - Harvard University 应用数学（计算机科学方向）博士（PhD，1956）；论文 *The Analytic Design of Automatic Data Processing Systems*
- **博士导师**：Howard Aiken（Harvard，Mark I 之父——"Mark I 之父"为常识性注解，页面未载此称谓，**正文仅写 Howard Aiken 即可**）
- **研究领域**：计算机科学、操作系统、软件工程

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖**：1999 年 ACM Turing Award（页面 infobox 仅列年份，未载整句 citation——**勿编造 citation**）。
2. **Harvard 全球首个"自动数据处理"研究生项目**：在 Ken Iverson 门下担任研究生助教——哈佛的 "automatic data processing" 项目是**世界上第一个**此类项目（页面原文明示 "the first such program in the world"，可写）。
3. **IBM 早年（1956–）**：1956 年加入 IBM，先后在 Poughkeepsie 与 Yorktown 工作；参与 IBM 7030 Stretch（千万美元级科学超级计算机，售出九台）与 NSA 专用的 IBM 7950 Harvest。
4. **System/360 与 OS/360**：担任 IBM **System/360 大型机家族与 OS/360 软件包**的研发经理——计算机史上最著名的家族化工程。
5. **"计算机体系结构"术语的提出者**：在此期间创造（coined）了 "computer architecture" 一词（页面实载，可写）。
6. **8-bit byte 决策**：Brooks 自述其最重要的单一决策是把 IBM 360 系列从 6-bit byte 改为 **8-bit byte**，从而支持小写字母，"这一改变传遍各处"（2004 CHM 演讲与 2010 Wired 采访实载的直接引语）。
7. **《人月神话》（The Mythical Man-Month, 1975）**：离开 IBM 数年后写成；种子来自 IBM 时任 CEO Thomas J. Watson Jr. 在离职面谈中的提问（"为什么软件项目管理比硬件难得多"）；1995 年出 20 周年纪念版增四章。
8. **Brooks's law**："Adding manpower to a late software project makes it later"（向延期项目加人只会更延期）——页面原文明示此句出自本书并被称为 Brooks's law，可整句引用。
9. **《没有银弹》**："No Silver Bullet – Essence and Accident in Software Engineering"（1987, *Computer* 20(4)）——软件工程本质与偶然的经典论述。
10. **UNC 教育家（1964–2015）**：1964 年应邀创立 UNC Chapel Hill 计算机科学系并任系主任二十年（至 1984）；首任 Kenan 讲席教授，2015 年荣休；UNC 校园的 Brooks Computer Science Building 以其命名；晚年研究转向虚拟环境（virtual environments）与科学可视化。
11. **著述**：*Automatic Data Processing*（与 Iverson 合著，System/360 版 1969）、*Computer Architecture: Concepts and Evolution*（与 Gerrit A. Blaauw 合著，1997）、*The Design of Design*（2010）；名句 "The scientist builds in order to study; the engineer studies in order to build"（出自其 1996 年 "The computer scientist as toolsmith II"，参考文献实载）。
12. **国家服务与荣誉长河**：Defense Science Board（1983–86）、National Science Board（1987–92）；从 IEEE Fellow（1968）到 Eckert–Mauchly Award（2004）的长荣誉清单；2005 年发表图灵讲座 "Collaboration and Telecollaboration in Design"。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（计算机体系结构 — 蓝） | `#2E5A9E` | System/360 / computer architecture 术语 |
| 分类色 2（操作系统与软件工程 — 青绿） | `#1E8E8E` | OS/360 / No Silver Bullet |
| 分类色 3（项目管理智慧 — 琥珀） | `#D9A441` | 人月神话 / Brooks's law |
| 分类色 4（虚拟现实与可视化 — 玫瑰） | `#C0395B` | UNC 虚拟环境 / 科学可视化 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「大型机家族的模块化 / 人月的天平」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：怀旧 / 沉思（System/360 的黄金年代、《人月神话》五十年不衰的箴言）
- **选定曲目**：Alex-Productions **Nostalgia**（manifest 预分配，直接沿用），匹配"工程老兵回望软件工程半生"的叙事。
- **落地文件**：`turing/presentations/Fred_Brooks/Nostalgia.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「人月神话之父 · 美国」+ 布鲁克斯 1931–2022 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 导师 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1931–2022 生平纵览
4. **早年：北卡罗来纳的少年**（1931–1953）：Durham 出生、Duke 物理本科
5. **Harvard：Aiken 门下**（1953–1956）：应用数学博士、全球首个 ADP 项目、Iverson 助教
6. **IBM：Stretch 与 Harvest**（1956–）：Poughkeepsie/Yorktown、超级计算机与 NSA 主机
7. **System/360 与 OS/360**：家族化体系、经理职责、"computer architecture" 术语
8. **8-bit byte 决策**（公式框：6-bit vs 8-bit 的信息表达）——Wired 采访引语
9. **《人月神话》（1975）**：Watson Jr. 的离职面谈之问、20 周年版
10. **Brooks's law**：整句引用 + 语义解读
11. **《没有银弹》（1987）**：本质与偶然、工具匠论文 "toolsmith II"
12. **UNC 教育家**（1964–2015）：建系二十年、Kenan 讲席、虚拟环境与可视化
13. **荣誉**：Turing 1999、National Medal of Technology 1985、von Neumann Medal 1993、NAS/NAE 院士、Eckert–Mauchly 2004
14. **遗产**：《人月神话》与《没有银弹》至今仍是软件工程必读
15. **结尾**：91 岁、"科学家为求知而建造，工程师为建造而求知"

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖 citation**：页面 infobox 与正文**均未给出整句 citation**——勿编造 ACM 引语，表述"1999 年获图灵奖"即可。
- **可用的整句引语仅三条**：① Brooks's law "Adding manpower to a late software project makes it later"；② 8-bit byte 自述（"The most important single decision I ever made was to change the IBM 360 series from a 6-bit byte to an 8-bit byte, thereby enabling the use of lowercase letters. That change propagated everywhere."）；③ "The scientist builds in order to study; the engineer studies in order to build"——三条均有页面出处，勿再增编引语。
- **"世界第一"仅一处可写**：Harvard 的 "automatic data processing" 项目是 "the first such program in the world"（页面实载）；其余"首位/第一"表述禁写。
- **Stretch 数字**：$10 million 级、售出九台——数字勿改。
- **Watson Jr. 之问**：出处是"Brooks 离职面谈中 Watson Jr. 提出的问题"——勿写成 Watson 下令写书。
- **8-bit byte 归属**：是 Brooks **自述**的个人决策（2004 CHM 演讲/2010 Wired）——写明"Brooks 自述"，勿写成已定论的单一归属。
- **UNC 时间线**：1964 年受邀建系 → 任系主任 **二十年**（至 1984）→ Kenan 讲席至 **2015** 荣休——三个年份勿混。
- **死因**：中风后健康不佳（poor health following a stroke）——按此写，勿写"自然衰老"等其他。
- **家庭/信仰**：福音派基督徒、InterVarsity——按实载一笔带过，不渲染；长子取名致敬 Iverson。
- **荣誉年份红线**：National Medal of Technology **1985**、NAE 院士 **1976**、NAS 院士 **2001**、von Neumann Medal **1993**、Eckert–Mauchly **2004**、CHM Fellow **2001**、图灵讲座 **2005**——勿互串。
- **No Silver Bullet 年份**：论文刊于 *Computer* 20(4)，**1987**——勿写 1986/1975。
- **博士导师**：Howard Aiken——勿写成别人；页面未载硕士导师（BS 在 Duke，无硕士环节表述），勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | manifest 为 null，待补 |
| name_zh | 布鲁克斯（或 弗雷德·布鲁克斯） | 待写入 |
| name_en | Fred Brooks | 待写入 |
| birth_date | 1931-04-19 | 待写入 |
| death_date | 2022-11-17 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer architect / software engineer / computer scientist | 待写入 |
| field_of_work | operating systems / software engineering | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Howard Aiken（Harvard）
- **合作者/同事**：Ken Iverson（Harvard ADP 项目导师角色+《Automatic Data Processing》合著——兼具"导师/合作者"两重，入库时按页面角色写"Harvard 研究生项目导师（助教经历）+ 合著者"）、Gerrit A. Blaauw（*Computer Architecture* 合著者、IBM System/360 同事）
- **著名博士生**：Andrew Glassner（infobox 实载）
- **纪念/评价者**：Grady Booch（ACM 图灵奖页面撰写者）——不入关系表
- **无载禁写**：页面未载本科导师（Duke 阶段）——勿编造

## 8. 奖项清单

- Turing Award（1999）；Turing Lecture（2005，"Collaboration and Telecollaboration in Design"）
- IEEE Fellow（1968）；W. Wallace McDowell Award（1970）
- Computer Sciences Distinguished Information Services Award（1970）
- Guggenheim Fellowship（1975，Cambridge，计算机体系结构与人为因素研究）
- NAE 院士（1976）；American Academy of Arts and Sciences Fellow（1976）
- IEEE Computer Society Computer Pioneer Award（1982）
- National Medal of Technology and Innovation（1985）
- Thomas Jefferson Award, UNC（1986）；ACM Distinguished Service Award（1987）
- Harry Goode Memorial Award（1989）
- 荷兰皇家艺术与科学院外籍院士（1991）；ETH Zürich 荣誉技术科学博士（1991）
- IEEE John von Neumann Medal（1993）；ACM Fellow（1994）
- Distinguished Fellow of the British Computer Society（1994）；Royal Academy of Engineering 国际会士（1994）
- ACM Allen Newell Award（1994）；Franklin Institute Bower Award and Prize in Science（1995）
- CyberEdge Journal Annual Sutherland Award（1997）
- NAS 院士（2001）；Computer History Museum Fellow Award（2001）
- ACM/IEEE-CS Eckert–Mauchly Award（2004）
- IEEE Virtual Reality Career Award（2010）

## 9. 机构清单

- 教育：Duke University（物理 BS 1953）、Harvard University（应用数学/计算机科学 PhD 1956）
- 任职：IBM（1956 年起，Poughkeepsie / Yorktown；Stretch、Harvest、System/360 与 OS/360 研发经理）、UNC Chapel Hill（1964 年创系并任系主任至 1984；首任 Kenan 讲席教授，2015 荣休）
- 国家服务：Defense Science Board（1983–86）、National Science Board（1987–92）

## 10. 终审清单

- [ ] 生卒 1931-04-19 / 2022-11-17，享年 91，出生地 Durham, NC，去世地 Chapel Hill, NC
- [ ] 图灵奖"1999"年份正确，未编造 citation
- [ ] Brooks's law / 8-bit byte / toolsmith 三条引语出处标注无误
- [ ] "全球首个 ADP 项目"为唯一"第一"表述
- [ ] Stretch $10M/九台、Harvest/NSA 数字准确
- [ ] UNC 1964 建系 / 主任二十年至 1984 / 2015 荣休
- [ ] 《人月神话》1975、《没有银弹》1987、20 周年版 1995
- [ ] 死因仅"中风后健康不佳"
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | IBM · UNC Chapel Hill | Turing 1999`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1999/Fred Brooks/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Fred_Brooks_cropped_square_.jpg`（2007 年真肖像，最大版）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（限三条实载引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（1996 Pnueli / 1997 Engelbart / 1998 Gray）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
