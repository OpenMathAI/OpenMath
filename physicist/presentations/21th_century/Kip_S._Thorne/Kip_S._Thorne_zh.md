# 物理学家立传提示词（Kip S. Thorne）

> 本文件是 OpenPhysicist 21 世纪批次「物理学家立传提示词」，目标人物：Kip S. Thorne（2017 诺贝尔物理学奖，引力波天文学与 LIGO）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Kip Stephen Thorne（基普·斯蒂芬·索恩）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Thorne 篇的视觉主线是**弯曲时空（warped spacetime）**——从环猜想、膜范式到虫洞与《星际穿越》的 Gargantua，「弯曲」是贯穿其理论、探测与跨界的唯一母题。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Kip Stephen Thorne（1940-06-01 生于犹他州洛根，在世）
- **气质关键词**：**引力波天文学的预言家、黑洞理论的大师、跨界好莱坞的物理学家** —— 2017 诺贝尔物理学奖获奖理由（与 Weiss / Barish 共享）：
  > "for decisive contributions to the LIGO detector and the observation of gravitational waves"（因其对 LIGO 探测器和引力波观测的决定性贡献）
- **设计母题**：**弯曲与涟漪（curvature & ripples）**。时空被质量压弯，涟漪以光速传播——黑洞并合的「啁啾」、虫洞的 throat、银幕上的 Gargantua，都是同一弯曲几何的不同投影。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Kip_S._Thorne/page.md`
- **第 0 步状态**：page.md 已有本地；`{Dir}.html` 与 `images/` **待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Kip_S._Thorne`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 数据库同步：含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1940-06-01 生于犹他州洛根；在世（享年留白）
- 国籍：美国
- 家庭：父亲 D. Wynne Thorne（1908–1979，犹他州立大学土壤化学教授）；母亲 Alison Comish（1914–2004，经济学家，爱荷华州立学院首位经济学女博士）；摩门教（LDS）家庭长大，现自认无神论者（关于科学与宗教有明载引语）；四个同胞中两位亦成为教授
- 教育：Logan High School（Westinghouse Science Talent Search 获奖名次）；Caltech BS 物理（1962）；Princeton MS（1964）、PhD（1965，导师 John Archibald Wheeler）；博士论文《Geometrodynamics of Cylindrical Systems》
- 任职机构：Caltech 副教授（1967）→ 理论物理教授（1970，30 岁、Caltech 历史上最年轻正教授之一）→ William R. Kenan Jr. 讲席（1981）→ Richard P. Feynman 理论物理讲席（1991–2009）→ Feynman 讲席 emeritus（2009 起）；University of Utah 兼职教授（1971–1998）；Cornell Andrew D. White Professor at Large（1986–1992）
- 关键荣誉：American Academy of Arts and Sciences（1972）；NAS / 俄罗斯科学院 / 美国哲学学会院士；AIP Science Writing Award；Phi Beta Kappa Science Writing Award；Lilienfeld Prize（APS，1996）；Karl Schwarzschild Medal（德国天文学会，1996）；Robinson Prize in Cosmology；Common Wealth Awards；California Scientist of the Year（2003）；Albert Einstein Medal（伯尔尼，2009）；Leiden Lorentz 讲席（2009）；UNESCO Niels Bohr Medal（2010）；2016：Special Breakthrough Prize / Gruber / Shaw（与 Drever、Weiss）/ Kavli（与 Drever、Weiss）/ Tomalla / Georges Lemaître / Harvey（与 Drever、Weiss）/ Smithsonian American Ingenuity；2017：Cocconi Prize（与 Weiss、Barish）/ Princess of Asturias（与 Weiss、Barish）/ 诺贝尔物理学奖（与 Weiss、Barish）；Lewis Thomas Prize（2018，科学写作）；Golden Plate Award（2019）；Time 100（2016）；Claremont / 塞萨洛尼基 / 剑桥（2024）/ RIT（2026）荣誉博士；Woodrow Wilson / Danforth / Guggenheim / Fulbright Fellow
- 知名学生：infobox 明载博士生 14 人——William L. Burke、Carlton M. Caves、Lee Samuel Finn、Sándor J. Kovács、David L. Lee、Alan Lightman、Don N. Page、William H. Press、Richard H. Price、Bernard F. Schutz、Sherry Suyu、Saul Teukolsky、Michele Vallisneri、Clifford Martin Will（正文另载约 50 人在其指导下获 Caltech 博士）
- 核心贡献清单：
  1. 环猜想（hoop conjecture）：黑洞形成的临界周长判据
  2. 膜范式（membrane paradigm）：黑洞理论的膜方法，用于阐明 Blandford–Znajek 机制
  3. 黑洞熵的量子统计力学起源（与 Zurek：熵 = 构成方式数的对数）
  4. 黑洞薄吸积盘广义相对论理论（与 Novikov、Page；吸积加倍质量使自旋趋近 0.998 上限）
  5. Thorne–Żytkow 天体（红超巨星+中子星核）预言；Hartle–Thorne 度规；相对论星体脉动理论
  6. 可穿越虫洞与时间旅行物理（Morris–Thorne 虫洞、Kim 真空极化机制、ANEC 破缺条件）
  7. LIGO 共同创始人（1984）与理论支柱：波源清单、光散射挡板设计、与 Braginsky 组合作的量子不可摧毁（QND）测量设计、与 Caves 共同发明 back-action-evasion
- 关键时间线（15–20 节点）：1940 生于洛根 → Logan High School（Westinghouse STS）→ 1962 Caltech BS → 1964/1965 Princeton MS/PhD（Wheeler）→ 1963–64 磁场线内爆问题 → 1967 Caltech 副教授 → 1970 正教授（30 岁）→ 1971–98 Utah 兼职 → 1973《Gravitation》 → 1981 Kenan 讲席 → 1984 共同创立 LIGO → 1986–92 Cornell Professor at Large → 1991 Feynman 讲席 → 1994《Black Holes and Time Warps》（Phi Beta Kappa 奖）→ 2009 荣休 / Einstein Medal → 2010 UNESCO Bohr Medal → 2014《The Science of Interstellar》/《星际穿越》上映 → 2016-02-11 发布会 / Time 100 → 2016 七奖丰收 → 2017 诺贝尔奖 → 2018 Lewis Thomas Prize → 2017《Modern Classical Physics》（与 Blandford）→ 2024 剑桥荣誉博士 → 2026 RIT 荣誉博士

### 第 4 步：研究领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gravitational-wave astronomy | 引力波天文学 | field_of_work 明载；LIGO 理论支柱 | LIGO 页 |
| 1 | general relativity | 广义相对论 | 全部工作的理论框架 | 全篇 |
| 2 | black hole physics | 黑洞物理 | 环猜想、膜范式、熵、吸积盘 | 黑洞页 |
| 3 | relativistic astrophysics | 相对论天体物理 | 相对论星体、TŻO、Hartle–Thorne 度规 | 天体页 |
| 4 | wormhole physics | 虫洞物理 | 可穿越虫洞与时间旅行 | 虫洞页 |

### 第 4.5 步：社会关系表 【与 yaml 完全一致，仅收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Archibald Wheeler | 对方是导师 | 普林斯顿 MS（1964）/ PhD（1965）导师 |
| advisor-student | William L. Burke | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Carlton M. Caves | 对方是学生 | 博士生（infobox 明载）；与其共同发明 back-action-evasion QND 方法 |
| advisor-student | Lee Samuel Finn | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Sándor J. Kovács | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | David L. Lee | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Alan Lightman | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Don N. Page | 对方是学生 | 博士生（infobox 明载）；与其和 Novikov 共建薄吸积盘理论 |
| advisor-student | William H. Press | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Richard H. Price | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Bernard F. Schutz | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Sherry Suyu | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Saul Teukolsky | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Michele Vallisneri | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Clifford Martin Will | 对方是学生 | 博士生（infobox 明载）；与其奠定引力理论实验检验的解释框架 |
| co-honored | Rainer Weiss | 无向 | 2017 诺贝尔物理学奖共同得主（亦共享 2017 Cocconi / Princess of Asturias） |
| co-honored | Barry C. Barish | 无向 | 2017 诺贝尔物理学奖共同得主（亦共享 2017 Cocconi / Princess of Asturias） |
| co-honored | Ronald Drever | 无向 | 2016 Shaw / Kavli / Harvey Prize 共同得主 |
| spouse | Linda Jean Peterson | 无向 | 1960 年结婚，1977 年离异；育 Kares Anne 与 Bret Carter |
| spouse | Carolee Joyce Winstein | 无向 | 1984 年结婚，USC 生物运动学与物理治疗教授 |
| colleague | Charles Misner | 无向 | 《Gravitation》（1973）共同作者（与 Wheeler 三人合著） |
| colleague | Stephen Hawking | 无向 | 长期挚友与同事；Thorne–Hawking–Preskill 黑洞信息赌局；2015 曾共同写电影剧本草稿 |
| colleague | Carl Sagan | 无向 | 长期挚友；为其小说《Contact》提供虫洞物理咨询，并牵线与 Lynda Obst 相识 |
| colleague | James Hartle | 无向 | 共同导出 Hartle–Thorne 度规与相对论体运动/进动定律 |
| colleague | Anna Żytkow | 无向 | 共同预言 Thorne–Żytkow 天体（红超巨星+中子星核） |
| colleague | Igor Novikov | 无向 | 与其和 Don Page 共建黑洞薄吸积盘广义相对论理论 |
| colleague | Wojciech Zurek | 无向 | 博士后合作者，证明黑洞熵 = 构成方式数的对数 |
| colleague | Vladimir Braginsky | 无向 | 莫斯科研究组合作，发明先进探测器 QND 设计并降低热弹噪声 |
| colleague | Roger D. Blandford | 无向 | 《Modern Classical Physics》（2017）共同作者 |

> 无载不入库：Sung-Won Kim / Mike Morris / Ulvi Yurtsever 为单篇论文合作者（虫洞方向），防噪声仅正文提及不入库；Lynda Obst 为电影制片人（《星际穿越》共同构思），非学术关系；Christopher Nolan / Cillian Murphy 为媒体合作；Thorne–Hawking–Preskill 赌局的 Preskill 仅赌局命名出现。

### 第 5 步：配色方案 【人物专属】

- **气质**：弯曲、深邃、理论与实践与银幕的三重奏
- **配色**：时空深靛（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 时空深靛 `#241F4E`（本批专属，勿与他篇重复）
  - `badgeA` 引力波天文学 — 靛蓝 `#4C5FD5`
  - `badgeB` 黑洞物理 — 琥珀 `#E07B30`
  - `badgeC` 相对论天体 — 青绿 `#0E7C7B`
  - `badgeD` 虫洞 — 玫瑰 `#C4204F`
- **背景母题**：弯曲网格（规则坐标网在页面局部被「质量」压弯、涟漪圈层扩散），呼应环猜想与引力波波形

### 第 6 步：幻灯片序列 【人物专属，14 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 引力波天文学预言家 / Kip S. Thorne 1940– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 环猜想 / 膜范式与黑洞熵 / 虫洞物理 / LIGO 理论支柱
04  洛根少年与普林斯顿 (1940–1965) — 学者家庭、Westinghouse STS、Caltech BS、Wheeler 门下几何动力学
05  Caltech 教授岁月 (1967–2009) — 30 岁正教授、Kenan 讲席 1981、Feynman 讲席 1991、Utah/Cornell 兼职
06  黑洞物理（核心贡献页）— 环猜想 + 膜范式 + 熵 = ln N + 吸积盘 0.998 自旋上限；公式框放环判据 C = 4πGM/c²
07  相对论天体 — Thorne–Żytkow 天体、Hartle–Thorne 度规、脉动与引力辐射理论
08  虫洞与时间旅行 — Morris–Thorne 可穿越虫洞、Kim 真空极化遏制闭合类时曲线、ANEC 破缺、无悖论结论
09  LIGO 与 2017 诺贝尔奖 — 1984 共同创立、波源清单与挡板设计、QND（Caves/Braginsky）、2015-09 首测
10  书写相对论 — 《Gravitation》1973（与 Misner/Wheeler）、《Black Holes and Time Warps》1994、《Modern Classical Physics》2017
11  跨界好莱坞 — Sagan《Contact》咨询、与 Obst/Nolan《星际穿越》、《Tenet》、《奥本海默》顾问、TBBT 客串
12  荣誉与认可 — Nobel 2017 · Shaw/Kavli 2016 · Einstein Medal 2009 · Lewis Thomas Prize 2018
13  结尾 — 底部品牌 OpenMathAI
```

### 第 7–8 步：版式要点 + 陷阱表

版式照标杆（身份信息页左头像右网格、每页 make 后 pdftoppm 目检）。**Thorne 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 官网口径：Weiss 得一半奖金，Barish / Thorne 各四分之一；本篇写 Thorne 份额 1/4，勿写「三人平分」 |
| 诺奖分工 | Thorne 侧重**理论预言与 LIGO 理论支持**（波源/波形/QND），勿与 Weiss（原理发明）/ Barish（工程建成）混写 |
| 导师规范名 | 用库内 `John Archibald Wheeler`（id=2359），勿用 stub `John Wheeler`（id=2133）或 `David Wheeler` |
| 博士生规模 | 正文「约 50 人获 PhD」是概述，关系表只收 infobox 明载的 14 人名单，勿扩列 |
| 虫洞合作者 | Kim / Morris / Yurtsever 仅单篇合作，防噪声不入库，正文可提 |
| Thorne–Hawking–Preskill bet | Hawking 可入 colleague（挚友+赌局），Preskill 仅赌局命名不单独建关系 |
| Sagan 双线 | 《Contact》虫洞咨询 + 牵线 Obst 相识，两条都明载可写；Obst 本人非学术关系不入库 |
| 家庭 | 两段婚姻均明载（Peterson 1960–1977；Winstein 1984–，USC 生物运动学教授），两条 spouse 关系均入库；子女 Kares Anne / Bret Carter 仅姓名可写不入库 |
| LDS 背景 | 摩门教家庭 + 现无神论者 + 母亲临终劝退教（因歧视女性）均明载；科学与宗教引语可整句引用，勿引申宗教评论 |
| 环猜想公式 | C = 4πGM/c² 为 page.md 载明的判据，可直接用；「set into rotation」表述照原文 |
| 电影 | Interstellar（与 Obst 共同构思 + 科学顾问）、Tenet 顾问、Oppenheimer 顾问 Cillian Murphy、TBBT 客串、The Theory of Everything 中被扮演（Enzo Cilenti）均明载；勿写「监制」等无载头衔 |
| 书籍 | 《Gravitation》1973 三人合著（Misner/Wheeler/Thorne）；《The Warped Side of Our Universe》与艺术家 Lia Halloran 合著（诗+插画），Halloran 不入库 |

### 第 9 步：术语清单 【8–12 条】

| 英文 | 中文 | 风险 |
|------|------|------|
| hoop conjecture | 环猜想 | 黑洞形成判据 C = 4πGM/c²，勿写成「环定理」 |
| membrane paradigm | 膜范式 | 黑洞「膜」等效描述 |
| Thorne–Żytkow object | Thorne–Żytkow 天体（TŻO） | 红超巨星包层+中子星核 |
| Hartle–Thorne metric | Hartle–Thorne 度规 | 慢旋转轴对称体外解 |
| traversable wormhole | 可穿越虫洞 | 需奇异物质/负能量维持 |
| closed timelike curve | 闭合类时曲线（CTC） | 时间旅行的几何载体 |
| averaged null energy condition | 平均零能量条件（ANEC） | 虫洞需其破缺 |
| quantum nondemolition measurement | 量子不可摧毁测量（QND） | 先进探测器噪声压制 |
| thermoelastic noise | 热弹噪声 | 镜面热噪声 |
| Blandford–Znajek mechanism | Blandford–Znajek 机制 | 黑洞为类星体/活动星系核供能 |
| chirp | 啁啾信号 | 双黑洞并合引力波波形 |
| Lynda Obst | 琳达·奥布斯特 | 电影制片人，《星际穿越》共同构思者 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Cinematic Experience** — Alex-Productions（47k views，标签：电影感 / 高张力）
- **匹配理由**: Thorne 是三位 2017 得主中唯一「从黑板走进电影院」的人——《星际穿越》的 Gargantua 正是其理论可视化；「电影感 / 大定理 / 章节高潮」的曲风同时覆盖黑洞理论的宏大与诺奖之夜的高潮。
- **本地路径**: `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`
- **备选**: Ascension（科幻上升感，已配 Barish 篇）；Winds Of Freedom（管弦史诗）。

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Kip_S._Thorne/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Kip_S._Thorne.yaml` | 社会关系入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID → name_en 匹配） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
