# Edwin Catmull（埃德温·卡特穆尔）立传提示词

> qid=Q93161 · 1945-03-31 生（在世，死亡日期留白） · 美国计算机科学家 · 20/21 世纪 · 2019 图灵奖（与 Pat Hanrahan 共享）
> 本地 Wikipedia 数据源：`turing/pages/2019/Edwin Catmull/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（纹理映射 / 细分曲面的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Edwin Earl Catmull（中文惯称：埃德温·卡特穆尔，常称 Ed Catmull）
- **生卒**：1945-03-31 生于 Parkersburg, West Virginia（美国）；在世，死亡日期**留白**
- **国籍**：美国（American）
- **身份**：计算机科学家、动画师；Pixar 联合创始人、曾任 Walt Disney Animation Studios 总裁
- **家庭**：幼年随家迁居犹他州盐湖城；父先后任 Granite High School、Taylorsville High School 校长；妻 Susan Anderson，育有 3 个孩子（截至 2006 年居加州 Marin County）
- **特质**：**aphantasia（心像盲）**——无法在脑中形成心理图像（BBC 专访自陈 "my mind's eye is blind"），却成为图像科学的奠基人——天然的反差叙事点
- **童年志向**：《彼得潘》《木偶奇遇记》点燃动画梦，想当动画师，但当时没有动画学校；又喜欢数学与物理，遂选科学之路（还用翻页手绘小书做动画）
- **教育轨迹**：University of Utah 物理与计算机科学 BS（1969）→ 计算机科学 PhD（1974），论文 *A Subdivision Algorithm for Computer Display of Curved Surfaces*
- **博士导师**：Robert E. Stephenson；进入 Ivan Sutherland（Sketchpad 发明人）门下，属 DARPA 项目学生，同窗有 James H. Clark、John Warnock、Alan Kay
- **研究领域**：计算机科学（3D 计算机图形学）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2019 图灵奖（共享）**：与 Pat Hanrahan 因计算机生成图像（CGI）的开创性工作共享（2020-03 宣布）。本篇为**图形学发明 + 皮克斯管理线主叙事篇**。
2. **学生时代的两大发现（侧重页）**：犹他大学期间完成两项计算机图形学基础发现——**纹理映射（texture mapping）**与**双三次面片（bicubic patches）**；并发明空间抗锯齿算法与细分曲面精化算法。
3. **Z-buffer 的独立发现**：独立发现 **Z-buffering**——早 8 个月由 Wolfgang Straßer 在其博士论文（TU Berlin，1974-04 提交）中描述——**必须写"独立发现"而非"发明"**。
4. **《计算机动画的手》（1972）**：与 Fred Parke 在犹他大学制作一分钟的左手动画 *A Computer Animated Hand*；被好莱坞制片人采用嵌入 1976 年电影《Futureworld》（首部使用 3D 计算机图形的电影）；2011-12 入选国会图书馆**国家电影登记表**。
5. **NYIT 与 Tween（1974–1979）**：1974 博士毕业先入 Applicon，同年 11 月受 Alexander Schure 之邀任纽约理工学院（NYIT）新计算机图形实验室主任；1977 发明 2D 中间帧自动生成软件 **Tween**；团队短板是不会用电影讲故事。
6. **Lucasfilm（1979–1986）**：George Lucas 相邀，1979 年任副总裁筹建"计算机部门"；设三个项目组：图形组（Alvy Ray Smith）、音频（Andy Moorer）、非线性剪辑（Ralph Guggenheim）；1982 年《星际迷航 2》ILM 计算机图形有所贡献。
7. **Pixar 与乔布斯（1986）**：Steve Jobs 收购 Lucasfilm 数字部门成立 Pixar，Catmull 为联合创始人；2006 年 Pixar 被迪士尼收购。
8. **《玩具总动员》（1995）**：署名 **Executive Producer** + RenderMan Software Development——管理线里程碑（首部全 CGI 长片由 Pixar 产出；页面片单实载其署名，勿写"导演"）。
9. **执掌三大工作室（2007–2018）**：2007-06 与 John Lasseter 共同接管 Disneytoon Studios；分别任总裁与首席创意官，统管 Pixar、迪士尼动画、Disneytoon 三条产线（每周两天通勤迪士尼动画）；2014-11 两工作室总经理升总裁仍向其汇报。
10. **反垄断风波（一笔带过）**：High-Tech Employee Antitrust 诉讼中被点名；deposition 原话 "While I have responsibility for the payroll, I have responsibility for the long term also."；迪士尼系最终 1 亿美元和解——按实载中性一笔，勿渲染。
11. **《Creativity, Inc.》（2014）**：与 Amy Wallace 合著，入围 FT & Goldman Sachs 年度商业书（2014）、入选扎克伯格读书会（2015-03）。
12. **退而不休**：2018-10-23 宣布从 Pixar/迪士尼动画退休（顾问至 2019-07）；2022-03 出任 Thatgamecompany 创意文化与战略增长首席顾问。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（图形学发明 — 蓝） | `#2E5A9E` | 纹理映射 / Z-buffer / 细分曲面 |
| 分类色 2（渲染与电影 — 青绿） | `#1E8E8E` | 计算机动画的手 / Futureworld / Toy Story |
| 分类色 3（皮克斯创业 — 琥珀） | `#D9A441` | NYIT → Lucasfilm → Pixar / 乔布斯 |
| 分类色 4（管理与文化 — 玫瑰） | `#C0395B` | 迪士尼三工作室 / Creativity, Inc. |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：胶片帧格与渲染网格（稀疏矩形帧框渐次点亮），呼应「从像素到电影」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：陪伴 / 温暖（一个心像盲的人为世界造像的柔性叙事）
- **选定曲目**：Alex-Productions **With Me**（manifest 预分配，沿用勿改）
- **落地文件**：`turing/presentations/Edwin_Catmull/WithMe.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「图形学先驱 · 美国」+ Catmull 1945– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1945– 在世生平纵览
4. **盐湖城的动画梦**：迪士尼电影点燃、翻页手书、校长之家、心像盲的反差
5. **犹他大学与 Sketchpad 门下**（1969–1974）：Sutherland/DARPA、同窗 Clark/Warnock/Kay
6. **两大发现与 Z-buffer**（侧重页）：纹理映射、双三次面片、抗锯齿、细分曲面；Z-buffer 独立发现（早 8 个月的 Straßer）
7. **《计算机动画的手》**（1972）：Fred Parke、Futureworld、国家电影登记表
8. **NYIT 与 Tween**（1974–1979）：Schure、中间帧软件、讲故事短板
9. **Lucasfilm 时代**（1979–1986）：三项目组、ILM、数字电影工业
10. **Pixar 与乔布斯**（1986）：收购、联合创始人、2006 迪士尼并购
11. **《玩具总动员》**（1995）：Executive Producer + RenderMan 开发、全 CGI 长片时代
12. **执掌三大工作室**（2007–2018）：与 Lasseter 分工、三产线管理
13. **Creativity, Inc. 与管理哲学**（2014）：创意文化、书作荣誉
14. **荣誉年表**：四座奥斯卡科技奖、von Neumann Medal、Turing 2019（与 Hanrahan 共享）
15. **结尾**：在世、"让计算机画出电影"的奠基人

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由口径**：Catmull 页表述 "for their pioneering work on computer-generated imagery"（Hanrahan 页作 "pioneering efforts"）——统一写「计算机生成图像（CGI）的开创性工作」，2020 年 3 月宣布，勿写 2019 年颁。
- **Z-buffer 红线**：Catmull 是**独立发现**（independently discovered），Straßer 博士论文早 8 个月描述——勿写"发明 Z-buffer"。
- **Toy Story 署名红线**：页面片单署名是 **Executive Producer + RenderMan Software Development**——勿写"导演"（导演是 John Lasseter 等，页面未载其执导任何影片）。
- **博士导师**：infobox 载 **Robert E. Stephenson**；Sutherland 是影响其转向的"进入其门下的老师"（student of Sutherland）——两者并存时，学位导师写 Stephenson，师承叙事写 Sutherland，勿混一人。
- **Pixar 创立表述**：1986 年 **Steve Jobs 收购 Lucasfilm 数字部门并创立 Pixar**——勿写"C atmull 创立 Pixar 公司于 1979"。
- **首部 3D CG 电影**：《Futureworld》(1976) 是**首部使用 3D 计算机图形的电影**，《Westworld》(1973) 是首部使用计算机像素化图像的（续集关系勿颠倒）。
- **反垄断风波**：只写实载三点（被点名、deposition 引语、$100M 和解），中性一笔，勿展开"工资盗窃"指控细节渲染。
- **von Neumann Medal 表述疑点**：infobox/正文均作 "IEEE John von Neumann All-Medal Crown Of Trophies"（罕见写法）——**以 "IEEE John von Neumann Medal"（2006）为准**，理由 "pioneering contributions to the field of computer graphics in modeling, animation, and rendering"。
- **奥斯卡奖种**：4 项均为**科技奖/戈登·索耶奖**（1993/1996/2001/2008），非竞赛表演类奥斯卡——勿写"奥斯卡最佳影片"。
- **在世者**：死亡日期留白；家庭仅妻/3 子/居住地一句。
- **引语**：可用引语限定为 deposition "While I have responsibility for the payroll..."、BBC "my mind's eye is blind"（报道标题原话）；其余**勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 卡特穆尔（或 埃德温·卡特穆尔） | 待写入 |
| name_en | Edwin Catmull | 待写入 |
| birth_date | 1945-03-31 | 待写入 |
| death_date | 在世留白 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / computer graphics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Robert E. Stephenson（University of Utah）
- **师承/影响**：Ivan Sutherland（Sketchpad，Catmull 转向数字图像的关键人物，student of Sutherland）
- **同窗**：James H. Clark、John Warnock、Alan Kay（犹他 DARPA 项目同学）
- **长期搭档**：Alvy Ray Smith（NYIT/Lucasfilm 图形组/Pixar）
- **体制合作者**：Fred Parke（计算机动画的手）、George Lucas（雇主）、Steve Jobs（Pixar 收购者）、John Lasseter（Disneytoon 共同管理层）
- **团队组建**：Andy Moorer（音频）、Ralph Guggenheim（非线性剪辑）
- **下级/受其提携**：Pat Hanrahan（在 NYIT/DEC 于其麾下工作——出自 Hanrahan 页，Catmull 页自身无载）
- **门生**：页面**无载**（无 notable students 列表）——禁写

## 8. 奖项清单

- Academy Scientific and Technical Award（1993，RenderMan 开发，与 Thomas K. Porter 共享）
- ACM Fellow（1995）
- Academy Scientific and Technical Award（1996，数字图像合成开创性发明）
- 美国国家工程院院士（2000，数字影像创建领导力）
- Academy Award（2001，电影渲染领域的重大进步/Pixar RenderMan）
- IEEE John von Neumann Medal（2006，图形学建模/动画/渲染的开创性贡献）
- Gordon E. Sawyer Award（2008 年度、2009-02 颁，第 81 届奥斯卡）
- Computer History Museum Fellow（2013）
- **ACM Turing Award（2019，与 Pat Hanrahan 共享，2020-03 宣布）**
- Creativity, Inc.：FT & Goldman Sachs Business Book of the Year 入围（2014）

## 9. 机构清单

- 教育：University of Utah（BS 物理与计算机科学 1969；PhD 计算机科学 1974）
- 任职：Applicon（1974）；NYIT 计算机图形实验室主任（1974–1979）；Lucasfilm 副总裁·计算机部门（1979–1986）；Pixar 联合创始人·总裁（1986–2018/19，2006 年起兼 Walt Disney Animation Studios 总裁，Disneytoon 2007 起共管）；退休顾问（2018-10 宣布，至 2019-07）；Thatgamecompany 首席顾问（2022–）

## 10. 终审清单

- [ ] 生卒 1945-03-31 Parkersburg；在世留白
- [ ] 图灵奖 2019 与 Hanrahan 共享（2020-03 宣布），CGI 开创性工作口径
- [ ] Z-buffer 写"独立发现"、注明 Straßer 早 8 个月
- [ ] Toy Story 署名为 Executive Producer + RenderMan 开发，勿写导演
- [ ] 博士导师 Robert E. Stephenson 与师承 Ivan Sutherland 并存不混
- [ ] Futureworld（1976，首部 3D CG 电影）与 Westworld（1973，首部像素化图像）关系不颠倒
- [ ] 4 项奥斯卡均为科技类（1993/1996/2001/2008）
- [ ] aphantasia 叙事一笔带过、反垄断风波中性、无渲染
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Utah · NYIT · Lucasfilm · Pixar · Disney | Turing 2019`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] 头像使用 `images/500px-Ed_Catmull_at_Web_Summit_2015_cropped_.jpg`（500px 真实肖像）
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2019/Edwin Catmull/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Web Summit 2015 肖像（`images/500px-Ed_Catmull_at_Web_Summit_2015_cropped_.jpg`）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Hanrahan）格式对齐、共同部分（RenderMan）表述不重复（皮克斯管理线归本篇）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
