# Ivan Sutherland（伊万·萨瑟兰）立传提示词

> qid=Q62866 · 1938-05-16 –（在世）· 美国计算机科学家 · 20/21 世纪 · 1988 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1988/Ivan Sutherland/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Sketchpad 约束求解 / 裁剪算法 / VR 的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ivan Edward Sutherland（中文惯称：伊万·萨瑟兰）
- **生卒**：1938-05-16 生于 Hastings，Nebraska（美国）→ **在世**，卒年留白
- **国籍**：美国（American）
- **身份**：计算机科学家，公认"计算机图形学之父"（"father of computer graphics"）
- **家庭**：父来自新西兰、母 Anne Sutherland 来自苏格兰；兄 Bert Sutherland 亦是计算机科学研究者；2006-05-28 与 Marly Roncken 结婚；育有二子
- **教育轨迹**：
  - Carnegie Institute of Technology（现 Carnegie Mellon University）**电机工程**学士（BS；经 ROTC 服役通道）
  - California Institute of Technology（Caltech）硕士（MS）
  - MIT **电机工程**博士（1963），论文 *Sketchpad, a Man–Machine Graphical Communication System*（1963）
- **博士导师**：Claude Shannon（信息论之父，正文明载 "Claude Shannon signed on to supervise Sutherland's computer drawing thesis"；论文委员会成员含 Marvin Minsky 与 Steven Coons）
- **研究领域**：计算机图形学、交互计算、异步系统

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **"计算机图形学之父"**：Wikipedia 明载 "widely regarded as a pioneer of computer graphics"、注释引文 "widely regarded as the 'father of computer graphics'"——可写"公认之父"，这是页面实载的少数"之父"表述之一。
2. **Sketchpad（1963 博士论文）**：运行于 Lincoln TX-2 计算机；可接受约束、绘制水平垂直线并组合成图形、图形可复制/移动/旋转/缩放且保持基本属性；含首个窗口绘制程序与裁剪（clipping）算法、支持缩放——图灵奖获奖核心（GUI 的早期前身）。
3. **图灵奖（1988）**："for the invention of the Sketchpad, an early predecessor to the sort of graphical user interface that has become ubiquitous in personal computers, and his contributions to computer graphics"——整句引用为获奖理由红线。
4. **与 David C. Evans 共创 Utah 传奇**：1968 与朋友同事 David C. Evans 共同创立 **Evans & Sutherland** 公司（实时硬件、加速 3D 图形、打印机语言先驱）；1968–1974 任 University of Utah 教授，其学生群体奠定了现代图形学基础。
5. **Utah 门生天团**：Alan Kay（Smalltalk 发明者）、Henri Gouraud（Gouraud 着色）、Frank Crow（抗锯齿）、Jim Clark（Silicon Graphics 创始人）、Edwin Catmull（Pixar 联合创始人、迪士尼/皮克斯动画工作室总裁）、Henry Fuchs、Gordon Romney 等——一家门下走出多个改变行业的人。
6. **Evans & Sutherland 的行业辐射**：前员工中走出 Adobe 创始人 John Warnock 与 Silicon Graphics 创始人 Jim Clark。
7. **首台头戴显示器与 VR 之源（1968）**：与学生 Bob Sproull、Quintin Foster、Danny Cohen 等造出首台能随观察者姿态变化渲染图像的头戴显示器 "The Sword of Damocles"（达摩克利斯之剑），成为首个虚拟现实系统——注意页面同时指出更早的 Sensorama 只能回放静态视频，Sutherland 系统的开创点在"实时随姿态渲染"。
8. **IPTO 掌门（1964–1966）**：博士毕业后 1963–1965 服兵役（以 ROTC 军官身份入美国陆军，至中尉军衔）；1964 年接替 J. C. R. Licklider 出任美国国防部 ARPA 信息处理技术办公室（IPTO）主任，任内启动图形与网络、ILLIAC IV、Macromodule 等项目。
9. **Cohen–Sutherland 线裁剪算法（1967）**：与哈佛学生 Danny Cohen 合作开发，图形学经典算法。
10. **算法谱系**：Known for 还含 **Sutherland–Hodgman 多边形裁剪算法**、Cohen–Sutherland、direct linear transformation（DLT）、zooming user interface、logical effort——多篇核心贡献可分页展开。
11. **Caltech 建系（1974–1978）**：Fletcher Jones 计算机科学教授，创办该校计算机科学系并任首任主任；后创办咨询公司 Sutherland, Sproull and Associates，1990 年被 Sun Microsystems 收购成为 Sun Labs 研究部种子；任 Sun Fellow 与副总裁。
12. **晚年：异步系统**：2005–2008 任 UC Berkeley 计算机科学访问学者；2009 年起与妻子 Marly Roncken 在 Portland State University 领导异步系统（Asynchronous Systems）研究；持有 60+ 项专利。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（计算机图形学 — 蓝） | `#2E5A9E` | Sketchpad / 裁剪算法 |
| 分类色 2（交互与 VR — 青绿） | `#1E8E8E` | 头戴显示器 / Sword of Damocles |
| 分类色 3（产业与公司 — 琥珀） | `#D9A441` | Evans & Sutherland / Sun Labs |
| 分类色 4（教育与传承 — 玫瑰） | `#C0395B` | Utah 门生天团 / Caltech 建系 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：细线框与十字准星点缀（呼应 Sketchpad 的"绘图与约束"视觉语言），稀疏点缀小圆节点（VR 姿态跟踪点）。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：自由 / 开拓（图形学的自由画布、从犹他荒原走出的产业传奇）
- **选定曲目**：Alex-Productions **Winds Of Freedom**（manifest 预分配，直接沿用）
- **落地文件**：`turing/presentations/Ivan_Sutherland/WindsOfFreedom.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「计算机图形学之父 · 美国」+ Sutherland 1938– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1938– 在世生平纵览
4. **早年：移民家庭与三校求学**（1938–1963）：新西兰裔父亲、苏格兰裔母亲、兄 Bert；Carnegie BS / Caltech MS / MIT 博士
5. **Shannon 门下：Sketchpad 诞生**（1963）：TX-2、约束求解、首个窗口与裁剪算法；委员会含 Minsky 与 Coons
6. **军旅与 IPTO 岁月**（1963–1966）：ROTC 中尉、接替 Licklider 执掌 ARPA IPTO、ILLIAC IV 与网络项目
7. **哈佛岁月与 Cohen–Sutherland**（1965–1968）：副教授、与 Danny Cohen 的线裁剪算法（1967）
8. **达摩克利斯之剑：第一个 VR 系统**（1968）：Sword of Damocles、随姿态实时渲染、与 Sensorama 之别
9. **Evans & Sutherland：与 Evans 共创公司**（1968）：实时硬件、加速 3D 图形、Adobe 与 SGI 创始人从这里走出
10. **Utah 传奇：图形学的黄埔军校**（1968–1974）：Alan Kay / Gouraud / Crow / Jim Clark / Catmull / Fuchs
11. **Caltech 建系与 Sutherland, Sproull**（1974–1990）：Fletcher Jones 讲席、创办 CS 系、公司被 Sun 收购成 Sun Labs 种子
12. **异步系统晚年**（1990– 在世）：Sun Fellow 与副总裁、Berkeley 访问、Portland State 异步研究中心、60+ 专利
13. **荣誉与传承**：Turing 1988、Kyoto 2012、NAE 1973 / NAS 1978、von Neumann Medal 1998
14. **遗产**：Sketchpad → GUI / CAD / VR 三条血脉；"father of computer graphics"
15. **结尾**：在世大师、从画布到像素世界的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由整句红线**："for the invention of the Sketchpad, an early predecessor to the sort of graphical user interface that has become ubiquitous in personal computers, and his contributions to computer graphics"——获奖点是 Sketchpad 发明 + 图形学贡献，勿写成"因 VR 获奖"。
- **Sketchpad 年份**：正文写 "Sutherland invented Sketchpad in 1962 while at MIT"，论文为 **1963**（博士论文答辩/提交年）——写"1962 年发明、1963 年博士论文"最稳妥，勿混写成一个年份。
- **师承 Claude Shannon（有载）**：正文两处明载 Shannon 是其博士导师（含 Publications 节 "His thesis supervisor was Claude Shannon, father of information theory"）——**可写**；论文委员会成员 Marvin Minsky 与 Steven Coons 亦有载，可写"委员会成员"勿写成"共同导师"。
- **VR 首创的精确口径**：1968 头戴显示器是**首个能随观察者姿态变化实时渲染图像**的系统（首个 VR 系统），更早的 Sensorama 只能回放静态视频——勿笼统写"人类第一台头戴显示器"。
- **在世留白**：Sutherland 生于 1938-05-16，**在世**，无卒日，勿编造享年。
- **IPTO 年份**：服兵役 1963–1965、infobox 记 ARPA 任期 1964–1966、正文写 1964 年接替 Licklider——以"1964 接任 IPTO 主任"为准，勿写"1963 年执掌 ARPA"。
- **Utah 任期**：1968–1974；Harvard 任期 1965–1968（副教授）；Caltech 任期 1974–1978——三条任期勿错位。
- **"之父"表述**："father of computer graphics" 是页面注释明载的称呼，可用；但 Alan Kay 等人贡献另有大拿，勿在 Sutherland 篇给他人贴"之父"标签。
- **学位口径**：infobox 写 Carnegie Mellon University (BS)，正文写 "bachelor's degree in electrical engineering from the Carnegie Institute of Technology"——写"卡内基理工学院（今卡内基梅隆大学）"两者兼容；PhD 是**电机工程**（MIT 1963），勿写成 CS。
- **婚姻**：2006-05-28 与 Marly Roncken 结婚（晚年再婚）；兄 Bert Sutherland 亦为计算机科学研究者——按实载一笔带过即可。
- **荣誉**：Turing 1988、Computer Pioneer Award 1985、IEEE von Neumann Medal 1998、ACM Fellow 1994、NAS 1978、NAE 1973、Kyoto Prize 2012（获奖理由 "pioneering achievements in the development of computer graphics and interactive interfaces"）、NIHF 2016、Washington Award 2018、BBVA 2019——无 Nobel（勿编造）。
- **引语**：页面 Quotes 节有直接引语（"A display connected to a digital computer gives us a chance to gain familiarity with concepts not realizable in the physical world. It is a looking glass into a mathematical wonderland."；"The ultimate display..."；"Well, I didn't know it was hard."；"It's not an idea until you write it down."；"Without the fun, none of us would go on!"）——只可用这些，勿编造其他引语。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 萨瑟兰（或 伊万·萨瑟兰） | 待写入 |
| name_en | Ivan Sutherland | 待写入 |
| birth_date | 1938-05-16 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer graphics / interactive computing / computer science | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Claude Shannon（MIT，信息论之父；正文明载）
- **论文委员会**：Marvin Minsky（1969 图灵奖得主）、Steven Coons（委员会成员，非导师）
- **共同创始人**：David C. Evans（Evans & Sutherland，1968）
- **著名学生**：Danny Cohen（Cohen–Sutherland）、Henri Gouraud（Gouraud 着色）、James H. Clark（Silicon Graphics 创始人）、Bui Tuong Phong（Phong 着色，infobox 实载）、Franklin C. Crow（抗锯齿）、John Warnock（Adobe 创始人）、Alan Kay（Smalltalk，正文 Utah 节实载）、Edwin Catmull（Pixar，正文实载）、Henry Fuchs、Bob Sproull（Sword of Damocles 合作者）
- **配偶**：Marly Roncken（2006 年结婚，Portland State 异步研究合作者）

## 8. 奖项清单

- Turing Award（1988，"for the invention of the Sketchpad... and his contributions to computer graphics"）
- Computer Pioneer Award（IEEE，1985）
- IEEE Emanuel R. Piore Award（1986，"For pioneering work in the development of interactive computer graphics systems and contributions to computer science education"）
- Computerworld Honors Program Leadership Award（1987）
- UNC Chapel Hill 荣誉博士（1986）
- ACM Software System Award（1993）
- EFF Pioneer Award（1994）
- ACM Fellow（1994）
- IEEE John von Neumann Medal（1998）
- R&D 100 Award（2004，团队）
- Computer History Museum Fellow（2005，"for the Sketchpad computer-aided design system and for lifelong contributions to computer graphics and education"）
- Kyoto Prize（2012，先进技术部门）
- National Inventors Hall of Fame（2016）
- Washington Award（2018）
- BBVA Foundation Frontiers of Knowledge Award（2019）
- 美国国家科学院院士（NAS，1978）、美国国家工程院院士（NAE，1973）

## 9. 机构清单

- 教育：Carnegie Institute of Technology（电机工程 BS，今 Carnegie Mellon）、Caltech（MS）、MIT（电机工程 PhD 1963）
- 任职：美国陆军军官（1963–1965）、ARPA IPTO 主任（1964–1966）、Harvard 副教授（1965–1968）、University of Utah 教授（1968–1974）、Evans & Sutherland 联合创始人（1968）、Caltech Fletcher Jones 教授兼 CS 系创办主任（1974–1978）、Sutherland, Sproull and Associates 创办人（1990 被 Sun 收购）、Sun Microsystems Fellow/副总裁、UC Berkeley 访问学者（2005–2008）、Portland State University 异步系统研究（2009–）

## 10. 终审清单

- [ ] 生卒 1938-05-16 / 在世留白，出生地 Hastings, Nebraska
- [ ] 图灵奖 1988 理由整句（Sketchpad + 图形学贡献）表述准确
- [ ] Sketchpad "1962 发明 / 1963 博士论文、TX-2"年份口径准确
- [ ] 师承 Claude Shannon（导师）+ Minsky/Coons（委员会成员）区分准确
- [ ] 1968 Sword of Damocles"首个随姿态实时渲染的 VR 系统"口径准确，不与 Sensorama 混淆
- [ ] Evans & Sutherland 1968 与 David C. Evans 共创
- [ ] Utah 门生名单仅列页面实载者（Kay/Gouraud/Crow/Clark/Catmull/Fuchs 等）
- [ ] IPTO 主任 1964 接替 Licklider 表述准确
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | MIT · Utah · Evans & Sutherland · Caltech · Sun | Turing 1988`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1988/Ivan Sutherland/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 CHM 肖像（`images/Ivan_Sutherland_at_CHM.jpg`，2008 年照；小图版 `250px-Ivan_Sutherland_at_CHM.jpg`，取大图 500px 级）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文 Quotes 节找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Kahan 等）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
