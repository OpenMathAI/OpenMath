# 物理学家立传提示词（Barry C. Barish）

> 本文件是 OpenPhysicist 21 世纪批次「物理学家立传提示词」，目标人物：Barry C. Barish（2017 诺贝尔物理学奖，LIGO 建成与引力波观测）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Barry Clark Barish（巴里·克拉克·巴里什）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Barish 篇的视觉主线是**大科学工程（big science）**——把小科学的引力波搜寻改造成千人协作、千米臂长的观测台，是「总建造师」的叙事。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Barry Clark Barish（1936-01-27 生于内布拉斯加州奥马哈，在世）
- **气质关键词**：**LIGO 的总建造师、弱中性流的首探者、大科学的旗手** —— 2017 诺贝尔物理学奖获奖理由（与 Weiss / Thorne 共享）：
  > "for decisive contributions to the LIGO detector and the observation of gravitational waves"（因其对 LIGO 探测器和引力波观测的决定性贡献）
- **设计母题**：**巨型臂长与共振（kilometer arms & resonance）**。从 Fermilab 的中微子径迹到 LIGO 的 4 km 干涉臂，是「把假设放大到工程尺度去逼问自然」的实验家方法论。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Barry_C._Barish/page.md`
- **第 0 步状态**：page.md 已有本地；`{Dir}.html` 与 `images/` **待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Barry_C._Barish`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 数据库同步：含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1936-01-27 生于内布拉斯加州奥马哈；在世（享年留白）
- 国籍：美国；父母家族为来自今属白俄罗斯的原波兰地区犹太移民；二战后举家迁洛杉矶 Los Feliz
- 教育：John Marshall High School（洛杉矶）；UC Berkeley（BA 物理 1957，PhD 实验高能物理 1962）
- 博士导师：A. Carl Helmholz；博士论文为 310/377 MeV π⁻p → π⁻π⁰p 反应研究（1962）
- 任职机构：Caltech（1963–2005 退休后 emeritus：research fellow 1963–66 → assistant/associate/professor 1966–91 → Maxine and Ronald Linde 讲席教授 1991–2005 → Linde 讲席教授 emeritus；Caltech 高能物理组 PI 1984–96）→ UC Riverside（2018 加入，校内第二位诺奖教员）→ Stony Brook University（2023 秋，首任 President's Distinguished Endowed Chair in Physics）；Sapienza University of Rome（Fermi Chair）
- 关键荣誉：Klopsteg Memorial Award（AAPT，2002）；NAS 院士（2002）；Enrico Fermi Prize（2016）；Smithsonian American Ingenuity Award（2016）；Henry Draper Medal（NAS，2017）；Giuseppe and Vanna Cocconi Prize（EPS，2017）；Princess of Asturias Award（2017，与 Thorne、Weiss）；Fudan-Zhongzhi Science Award（2017，与 Thorne、Weiss）；Nobel Prize in Physics（2017，与 Weiss、Thorne）；UC Berkeley 年度校友（2018）；SMU / 博洛尼亚（2006）/ 佛罗里达（2007）/ 格拉斯哥（2013）/ 索菲亚大学荣誉博士；Copernicus Prize（波兰政府首届，2023）；National Medal of Science（Biden 白宫授勋，2023）；美国艺术与科学院 / NAS / National Science Board / APS Fellow（2011 年 APS 主席）/ AAAS Fellow；皇家学会外籍成员（frontmatter）；World Science Festival 2016 "Titan of Physics"；2007 明尼苏达大学 Van Vleck 讲座
- 知名学生：Kate Scholberg（infobox 明载博士生）
- 核心贡献清单：
  1. Fermilab 高能中微子实验：揭示核子夸克亚结构
  2. 首批观测到弱中性流（weak neutral current）——Salam / Glashow / Weinberg 电弱统一理论的关键证据
  3. MACRO 实验（Gran Sasso）负责人：磁单极搜寻、贯穿宇宙线、中微子质量与振荡的确证性证据
  4. LIGO PI（1994）与主任（1997）：推动 NSF 国家科学委员会 1994 批准拨款、建成 Livingston 与 Hanford 两台干涉仪（1997）
  5. 创建 LIGO Scientific Collaboration（LSC，逾千名合作者）；Advanced LIGO 提案在其任内成形
  6. ILC International Linear Collider Global Design Effort 主任（2005–2013）
- 关键时间线（15–20 节点）：1936 生于奥马哈 → 二战后迁洛杉矶 → John Marshall High School → 1957 Berkeley BA → 1962 Berkeley PhD（Helmholz 指导）→ 1963 入 Caltech（research fellow）→ 1966–91 教职阶梯 → Fermilab 中微子实验（弱中性流）→ 1980s MACRO（Gran Sasso）→ 1984–96 Caltech HEP 组 PI → 1990s GEM（SSC，L* 被 Schwitters 否决后）→ 1994 LIGO PI / NSF 批准 → 1997 LIGO 主任、两台干涉仪建成、创建 LSC → 2001–02 HEPAP 长期规划共同主席 / NRC「Neutrinos and Beyond」主席 → 2005–2013 ILC Global Design Effort 主任 → 2011 APS 主席 → 2015-09-14 首次直接探测（30 倍太阳质量双黑洞并合）→ 2016-02-11 CERN 科学界首报 → 2016 Fermi Prize → 2017 Draper Medal / 诺奖 → 2018 加入 UC Riverside → 2023 Copernicus Prize / National Medal of Science / Stony Brook 讲席

### 第 4 步：研究领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | experimental physics | 实验物理 | field_of_work 明载主领域 | 全篇 |
| 1 | particle physics | 粒子物理 | Fermilab 中微子实验、SSC/ILC | 粒子页 |
| 2 | gravitational wave detection | 引力波探测 | LIGO 建成与 LSC，2017 诺奖核心 | LIGO 页 |
| 3 | neutrino physics | 中微子物理 | 弱中性流、MACRO 振荡证据 | 中微子页 |
| 4 | astrophysics | 天体物理 | field_of_work 明载 | 全篇 |

### 第 4.5 步：社会关系表 【与 yaml 完全一致，仅收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | A. Carl Helmholz | 对方是导师 | UC Berkeley 博士导师（PhD 1962） |
| advisor-student | Kate Scholberg | 对方是学生 | 博士生（infobox 明载） |
| colleague | Samuel Chao Chung Ting | 无向 | SSC 时代：Ting 领导的 L* 实验被否决后 Barish 出任 GEM 发言人，曾任 L* 合作委员会主席 |
| co-honored | Kip S. Thorne | 无向 | 2017 诺贝尔物理学奖共同得主（亦共享 2017 Princess of Asturias 与 Fudan-Zhongzhi 奖） |
| co-honored | Rainer Weiss | 无向 | 2017 诺贝尔物理学奖共同得主（亦共享 2017 Princess of Asturias 与 Fudan-Zhongzhi 奖） |
| spouse | Samoan Barish | 无向 | 妻子，育有二子 |
| parent-child | Kenneth Barish | 对方是孩子 | 之子，UC Riverside 物理与天文系教授兼系主任 |

> 无载不入库：Roy Schwitters 仅作为否决 L* 的 SSC 主任出现，非合作关系；Ronald Drever 与本篇无直接共同获奖记载（Einstein Prize 2007 在 Weiss 篇），勿跨篇转写；三个孙辈非学术关系。

### 第 5 步：配色方案 【人物专属】

- **气质**：工程、厚重、大科学的静默决心
- **配色**：工程暗红（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 工程暗红 `#6B2737`（本批专属，勿与他篇重复）
  - `badgeA` 引力波探测 — 靛蓝 `#4C5FD5`
  - `badgeB` 粒子物理 — 琥珀 `#E07B30`
  - `badgeC` 中微子物理 — 青绿 `#0E7C7B`
  - `badgeD` 大科学管理 — 玫瑰 `#C4204F`
- **背景母题**：巨型 L 形干涉臂剪影与光束线（两条垂直长臂、激光往返的亮点序列），呼应 Livingston / Hanford 千米级装置

### 第 6 步：幻灯片序列 【人物专属，13 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — LIGO 总建造师 / Barry C. Barish 1936– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 弱中性流 / MACRO / LIGO 建成与 LSC / ILC
04  奥马哈到伯克利 (1936–1962) — 犹太移民家庭、洛杉矶、Berkeley BA/PhD、Helmholz 门下 π⁻p 反应
05  Caltech 粒子物理岁月 (1963–1991) — research fellow 到教授、Caltech HEP 组 PI
06  Fermilab 中微子实验 — 夸克亚结构、首批弱中性流观测（电弱统一的关键证据）
07  MACRO 与 GEM — Gran Sasso 磁单极/宇宙线/中微子振荡；SSC 时代 L* 否决与 GEM 发言人
08  接手 LIGO (1994–2005) — PI 1994、NSF 批准、1997 主任、Livingston+Hanford 建成、创建 LSC
09  探测与诺贝尔奖 (2015–2017) — 2015-09-14 双黑洞并合、2016-02-11 CERN 首报、诺奖（Barish 份额 1/4）
10  大科学旗手 — ILC Global Design Effort 2005–2013、HEPAP/IUPAP/NRC 政策角色、APS 主席 2011
11  荣誉与认可 — Nobel 2017 · National Medal of Science 2023 · Fermi Prize 2016 · Draper Medal 2017 · Copernicus 2023
12  结尾 — 底部品牌 OpenMathAI
```

公式框建议：page.md 无公式 → 第 09 页放双黑洞并合「啁啾」波形概念图式（频率振幅随时间上升的 chirp 曲线示意），并注明为示意；第 06 页放弱中性流 ν + N → ν + X 过程示意。

### 第 7–8 步：版式要点 + 陷阱表

版式照标杆（身份信息页左头像右网格、每页 make 后 pdftoppm 目检）。**Barish 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 官网口径：Weiss 得一半奖金，Barish / Thorne 各四分之一；本篇写 Barish 份额 1/4，勿写「三人平分」 |
| 诺奖分工 | 理由 "decisive contributions to the LIGO detector..."，Barish 侧重**探测器的建成与 LSC 组织**（leadership），勿与 Weiss（原理发明）/ Thorne（理论预言）混写 |
| 引语 | "I didn't know if I would succeed. I was afraid I would fail, but because I tried, I had a breakthrough." 为 page.md 明载原话，可整句引用 |
| 弱中性流 | 表述为「首批观测到 weak neutral current」，是 Salam/Glashow/Weinberg 电弱统一的 linchpin；勿写「发现 Z 玻色子」（Z 由 CERN 1983 发现，page.md 无载） |
| Ting 关系 | L* 由 Samuel Ting 领导、Barish 任合作委员会主席；L* 被 SSC 主任 Roy Schwitters 否决后 Barish 率 GEM。是项目管理/合作维度，勿写成师承；Schwitters 不入关系库 |
| 库内规范名 | 导师用库内 stub `A. Carl Helmholz`（id=2393）；Ting 用 `Samuel Chao Chung Ting`（id=2617，勿用短名 Samuel Ting）；Weiss / Thorne 沿用本批已建 `Rainer Weiss`(3139) / `Kip S. Thorne` 形式 |
| 妻子姓名 | Samoan Barish 是人名，勿与萨摩亚（Samoa）混淆 |
| 儿子 | Kenneth Barish 是 UC Riverside 物理与天文系教授兼系主任（page.md 明载），可入 parent-child；Stephanie 与孙辈不入库 |
| 2023 双奖 | Copernicus Prize（波兰政府首届，"对世界科学发展做出卓越贡献者"）与 National Medal of Science（Biden 白宫）同年，勿混 |
| APS President | 2011 年任 APS 主席（Fellow 条目内括注），勿写成 2011 当选 Fellow |
| ILC | 主任身份是 Global Design Effort for ILC（2005–2013）；ILC 为「拟建」装置，勿写成已建成 |
| 皇家学会 | Foreign Member of the Royal Society 仅见 frontmatter，正文无年份，年份禁写 |

### 第 9 步：术语清单 【8–12 条】

| 英文 | 中文 | 风险 |
|------|------|------|
| weak neutral current | 弱中性流 | 电弱统一关键证据，勿写「中性流电流」 |
| LIGO | 激光干涉引力波天文台 | Barish 主持建成 |
| LIGO Scientific Collaboration | LIGO 科学合作组织（LSC） | Barish 创建，逾千人 |
| Advanced LIGO | 先进 LIGO | 升级提案，在其主任任内成形 |
| MACRO | MACRO 实验 | Gran Sasso 地下实验，磁单极+宇宙线 |
| magnetic monopole | 磁单极子 | MACRO 搜寻对象 |
| neutrino oscillation | 中微子振荡 | MACRO 确证质量证据 |
| International Linear Collider | 国际直线对撞机（ILC） | 拟建，Global Design Effort 主任 |
| Superconducting Super Collider | 超导超级对撞机（SSC） | 已下马项目，L*/GEM 背景 |
| Henry Draper Medal | 德雷珀奖章 | NAS 2017，天体物理方向 |
| National Medal of Science | 美国国家科学奖章 | 2023 |
| Enrico Fermi Prize | 费米奖 | 2016，意大利，表彰 LIGO 形成 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Ascension** — Cold Cinema（标签：科幻 / 史诗 / 上升）
- **匹配理由**: 「上升」匹配 Barish 的工程叙事——LIGO 从纸面提案到 NSF 拨款、两台千米干涉仪落成、Advanced LIGO 升级、直到 2015-09-14 信号抵达的直线爬升；大科学建造的史诗感需要管弦张力。
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **备选**: Winds Of Freedom（管弦英雄）；Last Hope（革命性突破）。

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Barry_C._Barish/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Barry_C._Barish.yaml` | 社会关系入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID → name_en 匹配） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
