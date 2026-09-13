# Pat Hanrahan（帕特·汉拉汉）立传提示词

> qid=Q7143512 · 1955-05-08 生（在世，死亡日期留白） · 美国计算机图形学研究者 · 20/21 世纪 · 2019 图灵奖（与 Edwin Catmull 共享）
> 本地 Wikipedia 数据源：`turing/pages/2019/Pat Hanrahan/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Reyes 渲染架构 / 着色语言的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Patrick M. Hanrahan（中文惯称：帕特·汉拉汉）
- **生卒**：1955-05-08 生于 Milwaukee, Wisconsin（美国）；在世，死亡日期**留白**
- **国籍**：美国（American）
- **身份**：计算机图形学研究者；斯坦福大学计算机科学与电气工程 **Canon USA 讲席教授**（计算机图形学实验室）
- **成长地**：威斯康星州 Green Bay 长大
- **教育轨迹**：University of Wisconsin–Madison：核工程 BS（1977）→ 留校读研期间于 **1981 年开设并讲授一门新的图形学课程**（第一批学生含艺术系研究生 Donna Cox，今著名艺术与科学可视化专家）→ **生物物理学 PhD（1985）**
- **博士导师**：Antony Stretton
- **研究领域**：计算机图形学（渲染算法、GPU、科学插画与可视化）
- **个人生活**：页面**无个人生活章节**——无载禁写

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2019 图灵奖（共享）**：与 Edwin Catmull 因计算机生成图像（CGI）的开创性工作共享（2020-03 宣布）。本篇为 **RenderMan/Reyes 架构 + 斯坦福教学线主叙事篇**。
2. **RenderMan 之父（侧重页）**：作为 **Pixar 创始员工**（1986–1989），参与设计 **RenderMan Interface Specification** 与 **RenderMan Shading Language**——影业标准渲染工业的基石；此前 1980 年代已在 NYIT 计算机图形实验室与 DEC 于 **Catmull 麾下**工作。
3. **着色语言论文（1990）**："A language for shading and lighting calculations"（SIGGRAPH 1990，与 Jim Lawson）——着色语言奠基文献，日后 GPU 着色语言的思想源头（本句延伸表述需克制，页面仅载论文事实）。
4. **Pixar 署名作品**：The Magic Egg（1984）、Tin Toy（1988）、**Toy Story（1995）**片尾致谢名单在列。
5. **学界流转**：1989 年入 Princeton 教职 → 1995 年转 Stanford 至今；2003 年联合创办 **Tableau Software** 并任首席科学家（数据可视化巨头的学术源头）。
6. **可视化国家级平台**：2005-02 斯坦福被美国国土安全部选为首个区域可视化与分析中心（信息可视化/可视分析）；2011-05 Intel 资助视觉计算中心（与 Intel 的 Jim Hurley 共同领导）。
7. **三座奥斯卡科技奖**：1993（RenderMan，与 Pixar 创始员工们共享科学与工程奖）、2004（次表面散射模拟，与 Stephen R. Marschner、Henrik Wann Jensen）、2014（**Physically Based Rendering** 一书的概念形式化与参考实现，与 Matt Pharr、Greg Humphreys）。
8. **SIGGRAPH 双奖与学院**：1993 Computer Graphics Achievement Award；**2003 Steven A. Coons Award**（图形学终身创意贡献最高奖之一，理由 "leadership in rendering algorithms, graphics architectures and systems, and new visualization methods"）；2018 入选 ACM SIGGRAPH Academy **创始班**。
9. **三大院士身份**：美国国家工程院院士（1999）、美国艺术与科学院院士（2007）、ACM Fellow（2008）；IEEE VGTC 可视化职业成就奖（2006）；斯坦福三获教学奖。
10. **桃李满门（侧重页）**：博士生含 Maneesh Agrawala、Ren Ng、Matt Pharr、Tamara Munzner、Peter Schröder——渲染、可视化、计算摄影诸领域的中坚。
11. **一句话信条**：页面 Quotes 栏目载 "Curiosity and passion determine success"（好奇心与热情决定成功）——可作结尾页点题（注意这是页面栏目短句，标注出处、勿扩写成演讲引文）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（渲染架构 — 蓝） | `#2E5A9E` | RenderMan / Reyes / 着色语言 |
| 分类色 2（图形学奖坛 — 青绿） | `#1E8E8E` | 三座奥斯卡科技奖 / Coons Award |
| 分类色 3（可视化创业 — 琥珀） | `#D9A441` | Tableau / DHS 可视分析中心 |
| 分类色 4（教学传承 — 玫瑰） | `#C0395B` | 斯坦福教学线 / 桃李满门 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：光线追踪射线束（稀疏细线从一点散射），呼应「渲染 = 光的模拟」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：恒久 / 深沉（工业标准背后的长期主义者）
- **选定曲目**：Alex-Productions **Eternals**（manifest 预分配，沿用勿改）
- **落地文件**：`turing/presentations/Pat_Hanrahan/Eternals.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「渲染大师 · 美国」+ Hanrahan 1955– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 成长地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1955– 在世生平纵览
4. **绿湾少年与核工程本科**（1955–1977）：威斯康星麦迪逊、跨界的起点
5. **1981：研究生上讲台**：新设图形学课、学生 Donna Cox、生物物理博士（1985，Stretton 门下）
6. **NYIT 与 DEC：Catmull 麾下**（1980s）：进入图形工业的心脏
7. **Pixar 创始员工：RenderMan**（1986–1989）（侧重页）：接口规范 + 着色语言双基石
8. **着色语言论文**（1990）：SIGGRAPH 1990 与 Lawson
9. **Princeton → Stanford**（1989/1995）：学界深耕
10. **Tableau 与可视化**（2003–）：首席科学家、DHS 中心、Intel 中心（侧重页）
11. **三座奥斯卡科技奖**（1993/2004/2014）：RenderMan、次表面散射、Physically Based Rendering
12. **SIGGRAPH 荣誉**：Coons Award 2003、Achievement Award 1993、SIGGRAPH Academy 创始班 2018
13. **桃李满门**：Agrawala/Ng/Pharr/Munzner/Schröder、三获斯坦福教学奖
14. **荣誉年表**：三大院士、VGTC 职业奖、Turing 2019（与 Catmull 共享）
15. **结尾**：在世、"Curiosity and passion determine success"

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由口径**：Hanrahan 页作 "for their pioneering efforts on computer-generated imagery"（Catmull 页作 "work"）——统一写「计算机生成图像（CGI）的开创性工作」，2020 年 3 月宣布，勿写 2019 年颁。
- **共享结构**：2019 两人共享；本篇侧重 **RenderMan/Reyes/着色语言/斯坦福教学**；皮克斯公司史与《玩具总动员》管理线归 Catmull 篇，本篇只从"创始员工参与 RenderMan 设计"与"片尾署名"角度触碰，勿重复展开公司史。
- **Reyes 表述红线**：页面参考文献列表含 Cook/Carpenter/Catmull 1987 "The Reyes image rendering architecture"，但**正文未载 Hanrahan 参与 Reyes 论文**——"Reyes 架构"相关表述限于"RenderMan 工业标准的学术背景"，**勿写"Hanrahan 发明 Reyes"**（页面无载禁写）。
- **学位反差**：本科**核工程**、博士**生物物理学**——图形学是中途进入的领域（研究生 1981 年教图形学课），勿写成"计算机科学博士"。
- **NYIT/DEC 归属**：页面原文 "went to work at the New York Institute of Technology Computer Graphics Laboratory and at Digital Equipment Corporation under Edwin Catmull"——"under Catmull" 修饰两处工作；勿写"在 Pixar 之前加入 Catmull 的初创公司"之类引申。
- **Tableau 创办年**：2003（SEC Form D 佐证）；至今任首席科学家——"remains" 为页面原话，表述勿写成"已卸任"。
- **在世者**：死亡日期留白；页面无家庭/个人生活信息——**无载禁写**。
- **引语**：页面仅 "Curiosity and passion determine success"（Quotes 栏）一句——标注出处；其余**勿编造**。
- **奥斯卡奖种**：三项均为**科学技术奖**（Sci-Tech），勿写"奥斯卡最佳视觉效果"等竞赛奖。
- **获奖时身份**：获图灵奖时任斯坦福 Canon USA 讲席教授——机构头衔勿写错。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 汉拉汉（或 帕特·汉拉汉） | 待写入 |
| name_en | Pat Hanrahan | 待写入 |
| birth_date | 1955-05-08 | 待写入 |
| death_date | 在世留白 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer graphics researcher | 待写入 |
| field_of_work | computer graphics / rendering / visualization | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Antony Stretton（UW–Madison，生物物理学）
- **老上级**：Edwin Catmull（NYIT 与 DEC 时期的工作上级、同届图灵奖得主）
- **早期学生**：Donna Cox（1981 年图形学课上的艺术系研究生，今科学可视化名家）
- **RenderMan 同事**：Pixar 创始员工群体（1993 年奥斯卡科技奖共享者）；着色语言论文合作者 Jim Lawson
- **著名博士生**：Maneesh Agrawala、Ren Ng、Matt Pharr、Tamara Munzner、Peter Schröder
- **奖项共享合作者**：Stephen R. Marschner、Henrik Wann Jensen（次表面散射 2004）；Matt Pharr、Greg Humphreys（PBR 2014）
- **家庭**：页面无载——禁写

## 8. 奖项清单

- SIGGRAPH Computer Graphics Achievement Award（1993）
- Academy Scientific and Engineering Award（1993，RenderMan，与 Pixar 创始员工共享）
- 美国国家工程院院士（1999）
- Academy Technical Achievement Award（2004，次表面散射，与 Marschner、Jensen 共享）
- SIGGRAPH Steven A. Coons Award（2003）
- IEEE VGTC Career Award for Visualization Research（2006）
- 美国艺术与科学院院士（2007）；ACM Fellow（2008）
- ACM SIGGRAPH Academy 创始班（2018）
- Academy Technical Achievement Award（2014，Physically Based Rendering，与 Pharr、Humphreys 共享）
- 斯坦福大学教学奖 × 3
- **ACM A.M. Turing Award（2019，与 Edwin Catmull 共享，2020-03 宣布）**

## 9. 机构清单

- 教育：University of Wisconsin–Madison（BS 核工程 1977；PhD 生物物理学 1985）
- 任职：NYIT 计算机图形实验室、Digital Equipment Corporation（1980s，Catmull 麾下）；Pixar 创始员工（1986–1989，RenderMan）；Princeton University（1989–1995）；Stanford University（1995–至今，Canon USA 讲席教授）；Tableau Software 联合创始人·首席科学家（2003–）

## 10. 终审清单

- [ ] 生卒 1955-05-08 Milwaukee（Green Bay 长大）；在世留白
- [ ] 图灵奖 2019 与 Catmull 共享（2020-03 宣布），CGI 开创性工作口径
- [ ] 本篇侧重：RenderMan 接口规范+着色语言、1990 着色语言论文、Tableau、斯坦福教学
- [ ] Reyes 架构不写"Hanrahan 发明"（页面无载）
- [ ] 学位口径：核工程 BS 1977 + 生物物理 PhD 1985，勿写 CS 博士
- [ ] NYIT/DEC "under Catmull" 表述准确，不引申
- [ ] 三项奥斯卡均为科技奖，年份 1993/2004/2014 勿混
- [ ] 无家庭信息（无载禁写）；引语仅 "Curiosity and passion determine success" 一句
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | UW–Madison · Pixar · Princeton · Stanford · Tableau | Turing 2019`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] 头像使用 `images/Pat_Hanrahan_Tableau_2009.jpg`（500px 真实肖像，文件名以目录实际为准）
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2019/Pat Hanrahan/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Tableau 2009 肖像（`images/Pat_Hanrahan_Tableau_2009.jpg`）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Catmull）格式对齐、共同部分（RenderMan）表述不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
