# Alan Kay（艾伦·凯）立传提示词

> qid=Q92742 · 1940-05-17 – 在世留白 · 美国计算机科学家 · 20/21 世纪 · 2003 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2003/Alan Kay/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Smalltalk 的对象与消息 / Dynabook 概念的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Alan Curtis Kay（中文惯称：艾伦·凯）
- **生卒**：1940-05-17 生于马萨诸塞州斯普林菲尔德（Springfield, Massachusetts，美国）；在世，卒年留白
- **国籍**：美国（American）
- **身份**：计算机科学家（OOP 先驱、Smalltalk 之父、现代 GUI 架构师）
- **家庭**：父亲从事生理学（physiology）职业，家庭随其多次搬迁，最终定居纽约都会区；外祖父 Clifton Johnson（作家/插画家/摄影师）、舅舅 Irving Johnson（水手/探险家/作家）；妻子 Bonnie MacBird（作家/演员/制片人）
- **教育轨迹**（曲折而传奇）：
  - Brooklyn Technical High School（修满学分即毕业）
  - Bethany College（西弗吉尼亚）：生物主修、数学辅修
  - 丹佛教吉他一年 → 应征入伍美国陆军 → 通过空军军官培训资格 → 经 Aptitude 测试成为程序员
  - University of Colorado Boulder **数学 + 分子生物学**学士（BS，1966）
  - University of Utah **电机工程**硕士（1968）→ **计算机科学**博士（1969），论文 *FLEX: A Flexible Extendable Language*
- **博士导师**：David C. Evans 与 Robert S. Barton（双导师，infobox 实载）
- **研究领域**：计算机科学（OOP、GUI、个人计算、教育技术）
- **个人才艺**：前职业爵士吉他手、作曲家、戏剧设计师；业余古典管风琴演奏者

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **"object-oriented" 的命名者**：在 Xerox PARC 领导开发了有影响的面向对象编程语言 **Smalltalk**，亲手设计了早期版本的大部分内容，并**创造了 "object-oriented" 这一术语**；与 PARC 同事并列为 OOP 思想之父之一——注意：'object'/'class' 等原始概念出自 Simula 67（挪威计算中心），Kay 是**命名与发扬者**。
2. **关于 "objects" 的反思（页面实载引语）**："I'm sorry that I long ago coined the term 'objects' for this topic because it gets many people to focus on the lesser idea. The big idea is 'messaging'."——本篇可用的核心直接引语（出处：Stefan L. Ram 文档/AlanKayOnMessaging）。
3. **现代 GUI 的架构师**：在 PARC 领导设计了**首个现代窗口式计算机桌面界面**；是现代重叠窗口 GUI 的架构者；"desktop metaphor"、"windows" 均入 infobox Known for。
4. **Dynabook 概念**：在 PARC 期间构想的个人计算设备——笔记本电脑、平板电脑与电子书的**关键先祖**；因 Dynabook 定位于教育平台，Kay 也被视为**移动学习**最早的研究者之一；其理念后来进入 One Laptop Per Child（OLPC）设计。
5. **Utah 门下：图形学群星**：与 "计算机图形学之父" David C. Evans 同事，受 **Ivan Sutherland**（Sketchpad 作者）影响——Kay 自陈 Sutherland 1963 年的毕业论文影响了他对 objects 与编程的看法；1968 年结识 **Seymour Papert**、了解 Logo 语言，进而接触 Piaget/Bruner/Vygotsky 与建构主义学习理论——教育基因贯穿其一生。
6. **1968-12-09 "Mother of all Demos" 现场见证者**：尽管当天高烧，仍在旧金山现场目睹 Douglas Engelbart 的里程碑式演示——Kay 回忆："It was one of the greatest experiences in my life."（页面实载引语）。
7. **职业生涯轨迹**：1969 Stanford AI Lab 访问研究员 → 1970 加入 **Xerox PARC**（整个 1970 年代开发 Smalltalk 网络化工作站原型）→ 1981–1984 **Atari 首席科学家** → 1984 **Apple Fellow** → 1997 Apple ATG 关闭后经 Bran Ferren 邀请加入 **Walt Disney Imagineering** 任 Disney Fellow → 2001 创立 **Viewpoints Research Institute**（任主席至 2018 年机构关闭）→ 2002 加入 **HP Labs** 任 senior fellow（2005-07-20 HP 解散其团队后离开）；另任 UCLA adjunct professor、Kyoto University 访问教授、MIT adjunct professor。
8. **Squeak / Etoys / Croquet / Tweak**：1995-12 在 Apple 发起开源 Smalltalk 版本 **Squeak**；1996-11 启动 **Etoys** 教育系统研究；与 David A. Smith、David P. Reed 等发起 **Croquet Project**（开源网络化 2D/3D 协作环境）；2001 年团队提出 **Tweak** 界面架构。
9. **OLPC 百元笔记本（2005）**：2005-11 信息社会世界峰会发布 $100 Laptop（XO-1，"Children's Machine"）——由 Kay 的朋友 Nicholas Negroponte 创立与维系、**基于 Kay 的 Dynabook 理念**；Kay 是核心共同开发者，专注 Squeak/Etoys 教育软件。
10. **STEPS 与"重新发明编程"（2006）**：2006-08-31 获 NSF 资助，"STEPS Toward the Reinvention of Programming"（递归缩写：STEPS Toward Expressive Programming Systems）——追问：今天的商业软件数亿行代码，一个可理解的实用 "Model T" 设计能否只需 20K–1M 行？
11. **图灵奖演讲**："The Computer Revolution Hasn't Happened Yet"（计算机革命还没有发生）——与其 OOPSLA 1997 演讲一脉相承，受 Sketchpad、Simula、Smalltalk 经历与商业软件臃肿代码的触动。
12. **荣誉**：图灵奖 2003、Kyoto Prize、Charles Stark Draper Prize 2004（与 Butler W. Lampson、Robert W. Taylor、Charles P. Thacker 共享）、NAE 院士 1997（"for inventing the concept of portable personal computing"）、Computer History Museum Fellow 1999、ACM Fellow 2008 等。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（OOP 与 Smalltalk — 蓝） | `#2E5A9E` | object-oriented 命名 / messaging |
| 分类色 2（GUI 与窗口 — 青绿） | `#1E8E8E` | 重叠窗口 / desktop metaphor |
| 分类色 3（Dynabook 与个人计算 — 琥珀） | `#D9A441` | Dynabook / 笔记本与平板先祖 |
| 分类色 4（教育与 OLPC — 玫瑰） | `#C0395B` | Logo / Etoys / Squeak / OLPC |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和重叠窗口矩形（稀疏圆角矩形层叠），呼应「overlap windows 桌面隐喻」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：明亮 / 憧憬（"计算机革命还没有发生"的未来主义教育家）
- **选定曲目**：Alex-Productions **Daylight**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Alan_Kay/Daylight.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「OOP 命名者 · Dynabook 之父 · 美国」+ Kay 1940– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域 / 个人才艺）
3. **时间线**（`\timelineslide`）：1940– 生平纵览
4. **曲折的早年**：斯普林菲尔德出生、Brooklyn Tech、Bethany 生物数学、教吉他、空军程序员——通往计算机的非典型路径
5. **Utah 岁月（1966–1969）**：FLEX 论文、双导师 Evans/Barton、Sutherland Sketchpad 的影响
6. **1968：两次相遇**：Papert 与 Logo/建构主义；Engelbart "Mother of all Demos" 现场（引语）
7. **Xerox PARC（1970–1981）**：Smalltalk、"object-oriented" 命名、现代重叠窗口 GUI
8. **"The big idea is messaging"**：对象 vs 消息的反思（核心引语页）
9. **Dynabook**：笔记本/平板/电子书的关键先祖、移动学习
10. **Atari → Apple → Disney**：1981–2001 产业界的流浪智者
11. **Squeak / Etoys / Croquet**：开源教育软件生态
12. **OLPC 百元笔记本（2005）**：Dynabook 理念的现实回响、Negroponte 与 XO-1
13. **STEPS：重新发明编程（2006）**：Viewpoints Research、NSF 资助、"Model T" 追问
14. **荣誉之殿**：Turing 2003、Kyoto Prize、Draper 2004、NAE 1997、CHM Fellow 1999
15. **结尾**："The Computer Revolution Hasn't Happened Yet"——在世理想主义者的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖获奖理由（核心红线，整句引用）**："For pioneering many of the ideas at the root of contemporary object-oriented programming languages, leading the team that developed Smalltalk, and for fundamental contributions to personal computing"（2003）——整句引用勿改写。
- **"The best way to predict the future is to invent it" 禁写**：该名言**未出现在本地 Wikipedia 页面**——按批次红线，仅在页面原文可见时收录；本页无，**整篇禁用此引语**。
- **OOP 表述是"命名者 + 之父之一"**：Kay "coined the term" object-oriented 且是 "one of the fathers of the idea of OOP"（与 PARC 部分同事并列）；'object'/'class' 概念源自 **Simula 67（挪威计算中心）**——勿写 Kay 发明了对象概念本身。
- **messaging 引语口径**："I'm sorry that I long ago coined the term..." 是页面实载引语（来源 Stefan L. Ram 文档）——引用时保持原句，勿截断改写。
- **博士论文年份**：FLEX 论文 **1968 年完成/1969 年获博士学位**（infobox 论文注 1968；正文 MS 1968、PhD 1969）——写作时口径：1968 论文、1969 学位。
- **双导师**：David C. Evans 与 Robert S. Barton——infobox 实载 "Doctoral advisors"（复数）；Sutherland 是"同事与影响者"，**勿写成博士导师**。
- **Draper Prize 是 2004**（与 Lampson/Taylor/Thacker 共享，因 Alto/个人计算）——勿与 2004 图灵奖同年混淆，也勿写错共享者名单。
- **在世留白**：1940 年生，在世——死亡日期与死因完全留白。
- **页面质量提示**：本条目 Wikipedia 自带 BLP（在世人物）补充来源模板——涉及个人评价的事实从严按页面实载，不渲染。
- **任职时间线**：Atari 首席科学家 1981–1984；Apple Fellow 1984；Disney Fellow 在 1997 ATG 关闭后；HP Labs 2002 入职、2005-07-20 离开；Viewpoints 2001 创立、2018 关闭——年份勿混。
- **OLPC 表述**：程序"由 Negroponte 创立并维系"、基于 Kay 的 Dynabook 理念、Kay 是 "prominent co-developer"——勿写 Kay 是 OLPC 创始人。
- **引语红线**：全文仅三处可考的直接话语（童年阅读自述、Mother of all Demos 回忆、messaging 反思）——除这三处与获奖理由外勿编造引语；童年阅读自述（"I had the misfortune or the fortune..."）如使用须注明为 Davis Group 教育访谈出处。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 艾伦·凯 | 待写入 |
| name_en | Alan Kay（全名 Alan Curtis Kay） | 待写入 |
| birth_date | 1940-05-17 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：David C. Evans（"计算机图形学之父"之一）、Robert S. Barton（双导师，infobox 实载）
- **影响者**：Ivan Sutherland（Sketchpad，1963 论文影响其对象观）、Seymour Papert（Logo 与建构主义，1968 相识）、Douglas Engelbart（Mother of all Demos）
- **Draper Prize 共同得主**：Butler W. Lampson、Robert W. Taylor、Charles P. Thacker（2004）
- **OLPC 合作**：Nicholas Negroponte（OLPC 创立者、Kay 之友）
- **妻子**：Bonnie MacBird（作家/演员/制片人）
- **Notable students**：David Canfield Smith（infobox 实载）
- **Squeak/Croquet 合作者**：Dan Ingalls、David A. Smith、David P. Reed、Andreas Raab 等（页面实载名单为准）

## 8. 奖项清单

- ACM Turing Award（2003，理由整句引用见 §5）
- Kyoto Prize（高松宫殿下纪念世界文化奖，年份页面未单列）
- Charles Stark Draper Prize（2004，与 Lampson/Taylor/Thacker 共享）
- UdK 01-Award（柏林，表彰 GUI 开创）
- J-D Warnier Prix d'Informatique
- NEC C&C Prize（2001）
- Telluride Tech Festival Award of Technology（2002）
- UPE Abacus Award（2012）
- NAE 院士（1997，"for inventing the concept of portable personal computing"）
- Computer History Museum Fellow（1999，"for his fundamental contributions to personal computing and human-computer interface development."）
- ACM Fellow（2008，"For fundamental contributions to personal computing and object-oriented programming."）
- Hasso Plattner Institute Fellow（2011）
- American Academy of Arts and Sciences / Royal Society of Arts 会士
- ACM Systems Software Award、NEC Computers & Communication Foundation Prize、Funai Foundation Prize、Lewis Branscomb Technology Award、ACM SIGCSE Award for Outstanding Contributions to Computer Science Education
- 荣誉博士：KTH 皇家理工学院（2002）、Georgia Tech（2005）、Columbia College Chicago（2005）、比萨大学（2007）、滑铁卢大学（2008）、京都大学（2009）、穆尔西亚大学（2010）、爱丁堡大学（2017）；柏林艺术大学荣誉教授

## 9. 机构清单

- 教育：Brooklyn Technical High School；Bethany College（生物/数学）；University of Colorado Boulder（数学 + 分子生物学 BS，1966）；University of Utah（MS EE 1968 / PhD CS 1969，FLEX 论文）
- 任职：Stanford Artificial Intelligence Lab 访问研究员（1969）；Xerox PARC（1970–1981，Smalltalk/Dynabook/GUI）；Atari 首席科学家（1981–1984）；Apple Fellow（1984–1997）；Walt Disney Imagineering Disney Fellow（1997–2001 前后）；Viewpoints Research Institute 创立者与主席（2001–2018）；HP Labs senior fellow（2002–2005）；UCLA adjunct / Kyoto University 访问教授 / MIT adjunct

## 10. 终审清单

- [ ] 生卒 1940-05-17 / 在世留白，出生地 Springfield, Massachusetts
- [ ] 图灵奖 2003，理由整句引用无误
- [ ] "The best way to predict the future..." 全篇禁用（页面无载）
- [ ] "object-oriented" 命名者 + OOP 之父之一；Simula 67 概念源头已注明
- [ ] messaging 引语原句引用无误
- [ ] 博士论文 FLEX 1968 / 博士学位 1969；双导师 Evans + Barton；Sutherland 是影响者非导师
- [ ] Draper Prize 2004 与 Lampson/Taylor/Thacker 共享
- [ ] OLPC 表述：Negroponte 创立、基于 Dynabook 理念、Kay 为共同开发者
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Xerox PARC · Atari · Apple · Disney · HP | Turing 2003`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2003/Alan Kay/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实（注意 BLP 模板，从严核对）
- [ ] **头像**：使用真实肖像（首选 `images/500px-Alan_Kay_-_Receiving_the_Kyoto_Prize.jpg` 京都奖领奖照；备选 `500px-Alan_Kay_receiving_the_Turing_Award.jpg` 领奖照或 `500px-Alan_Kay_and_the_prototype_of_the_Dynabook_3009206205_.jpg` Dynabook 模型照——Dynabook 照可作 Slide 9 插图；`Ambox_important.svg` 系质量模板图标禁用）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：三处页面实载引语逐字核对（messaging 反思 / Mother of all Demos 回忆 / 童年阅读自述）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与本批次（RSA 三人 / Cerf / Kahn）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
