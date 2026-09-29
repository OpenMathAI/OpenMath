# 物理学家立传提示词（21 世纪批次：Andrea Ghez）

> **本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」**，以 Andrea Ghez（2020 诺贝尔物理学奖，银河系中心超大质量致密天体的发现者，物理学诺奖史上第四位女性得主）为实例。
> 结构对齐标杆 `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。标注 `【模板通用】` 部分可复用；`【人物专属】` 部分为本篇定制。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家标杆 Kenneth G. Wilson 提示词 + Beamer 成品骨架（`Eugene_Wigner_zh.tex` 一系）。
- **本实例**：Andrea Mia Ghez（安德烈娅·米娅·盖兹）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达——骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Andrea Mia Ghez（1965-06-16 生于美国纽约市，在世）
- **气质关键词**：**银心黑洞的追踪者、自适应光学的先行者、物理学诺奖第四位女性** —— 2020 诺贝尔物理学奖获奖理由（与 Reinhard Genzel 共享一半）：
  > "for the discovery of a supermassive compact object at the centre of our galaxy"（因发现我们银河系中心的超大质量致密天体）
  > 另一半授予 Roger Penrose（黑洞形成是 GR 稳健预言）；总口径 "for their discoveries relating to black holes"（黑洞性发现）。
- **设计母题**：**穿过大气与尘埃的锐利目光（the sharpened gaze）**。自适应光学把湍流大气「抹平」，Keck 10 米镜把银心 S 簇恒星的轨道一颗颗点亮——视觉语言用波前校正的同心环与收敛到一点的恒星轨道弧线呼应。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Andrea_Ghez/page.md`（**已有本地**；`Andrea_Ghez.html` 与 `images/` **待下载**，Wikipedia URL：https://en.wikipedia.org/wiki/Andrea_Ghez ）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（`21st_century/Andrea_Ghez/page.md`，含 frontmatter：QID Q493956 / 生 1965-06-16 / 国籍 United States / 职业 astronomer, university teacher, mathematician, scientist / 博士导师 Gerald（Gerry）Neugebauer / 教育 MIT、Caltech）
- 🔲 `Andrea_Ghez.html` 与 `images/` 待下载（URL：https://en.wikipedia.org/wiki/Andrea_Ghez ）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1965-06-16 生于 New York City，在世
  - 国籍：United States（American astrophysicist）
  - 家庭：父 Gilbert Ghez（犹太裔，生于罗马，家族源自突尼斯与法兰克福；1969 于 Columbia 获博士并赴 University of Chicago 任职）；母 Susanne（née Gayton，爱尔兰天主教家庭，来自马萨诸塞州北阿特尔伯勒）；已婚 Tom LaTourrette，育两子；UCLA Masters Swim Club 活跃泳者
  - 教育：University of Chicago Laboratory Schools（教师子女）→ MIT（数学专业转入物理，1987 BS 物理）→ Caltech（MS、1992 PhD）
  - 博士导师：Gerry Neugebauer（frontmatter 作 Gerald Neugebauer、infobox 作 Gerry Neugebauer，同一人；yaml 用库内形式 `Gerry Neugebauer`）；博士论文 *The Multiplicity of T Tauri Stars in the Star Forming Regions Taurus-Auriga and Ophiuchus-Scorpius: A 2.2μm Speckle Imaging Survey*（1993）
  - 任职：UCLA 物理与天文系教授、Lauren B. Leichtman & Arthur E. Levine 天体物理讲席教授
  - 关键荣誉（时间序）：Annie J. Cannon Award in Astronomy 1994；Packard Fellowship 1996；Sloan Research Fellowship；Newton Lacy Pierce Prize 1998（AAS）；Maria Goeppert-Mayer Award 1999（APS）；Discover 杂志 20 位 promising young American scientists 2000；Sackler Prize 2004；Gold Shield Faculty Prize 2004；NAS 院士 2004；Marc Aaronson Memorial Lectureship 2007；MacArthur Fellowship 2008；Crafoord Prize in Astronomy 2012（瑞典皇家科学院）；American Philosophical Society 2012；Royal Society Bakerian Medal 2015；Oxford 荣誉 DSc 2019；APS Fellow 2019；AAS Legacy Fellow 2020；**Nobel Prize in Physics 2020**
  - 知名学生：page.md 未具名——**学生不入库**
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1965 生于纽约 → 1969 随父赴芝加哥、入 Lab School → Apollo 登月点燃宇航员梦想（母亲购望远镜）→ 高中化学老师是最有影响力的女性榜样 → 数学专业转物理 → 1987 MIT BS 物理 → 1992 Caltech 博士（Neugebauer 指导，T Tauri 星多重性斑纹成像巡天）→ 1994 Annie Cannon Award → UCLA 教职（Leichtman & Levine 讲席）→ 1996 Packard → 1998 Pierce Prize；1998 ApJ 论文 "High Proper Motions in the Vicinity of Sgr A*"（大质量中心黑洞证据）→ 1999 Goeppert-Mayer Award → 2000 Nature 论文（绕银心黑洞恒星的加速度）→ 2000 Discover 20 青年科学家 → 2004 Sackler + NAS → 2007 Aaronson Lectureship → 2008 MacArthur Fellowship；2008 ApJ 恒星轨道测银心黑洞距离与性质 → 2009 TED 演讲 "The Hunt For a Supermassive Black Hole" → 2012 Crafoord Prize + 美国哲学学会；2012-10 团队证认第二颗短周期星 S0-102 → Kepler 第三定律推得 Sgr A* 质量 4.1±0.6 百万太阳质量 → 2015 Bakerian Medal → 2019 Oxford 荣誉博士 + APS Fellow → 2020 诺贝尔物理学奖（第四位物理学诺奖女性：Curie 1903 → Goeppert Mayer 1963 → Strickland 2018 → Ghez 2020）→ 第 53 届 George Gamow 纪念讲座 "From the Possibility to the Certainty of a Supermassive Black Hole"

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | infrared astronomy | 红外天文 | Keck 红外成像穿透尘埃看银心 | 核心页 |
| 1 | adaptive optics | 自适应光学 | 校正大气湍流，Known for 条目 | 仪器页 |
| 2 | astrophysics | 天体物理 | infobox Fields 主口径 | 总览页 |
| 3 | black holes | 黑洞 | Sgr A* 超大质量黑洞，2020 诺奖核心 | 核心页 |
| 4 | star formation | 恒星形成 | 早年 T Tauri 星多重性巡天 | 早期页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> **只收 page.md 明载的关系**；对手方 name_en 用库内规范形式（Neugebauer 沿用库内 `Gerry Neugebauer`(id=2868)；Genzel/Penrose 用本批已建记录同名幂等；LaTourrette 新建 stub）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gerry Neugebauer | 师→生（博士导师） | Caltech 博士导师，红外天文先驱，1992 T Tauri 巡天论文 |
| co-honored | Reinhard Genzel | 无向 | 2020 诺贝尔物理学奖共享一半 |
| co-honored | Roger Penrose | 无向 | 2020 诺贝尔物理学奖另一半得主 |
| spouse | Tom LaTourrette | 无向 | 丈夫，育两子 |

- 入库操作：`MySQL/seed_person.py data/Andrea_Ghez.yaml`（幂等；Duplicate entry 撞 uq_rel 属正常跳过）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：锐利、坚定、穿越湍流的清澈
- **配色**：凯克青（清晰视界）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeAO` 自适应光学 — 深青绿 `#14574B`（主色）
  - `badgeIR` 红外天文 — 暗红 `#8C3A2B`
  - `badgeBH` 黑洞 — 靛黑蓝 `#1C2B4A`
  - `badgeSF` 恒星形成 — 琥珀 `#D98E30`
- **背景母题**：稀疏星点 + 同心校正环 + 汇聚一点的椭圆轨道束，呼应「湍流被抹平后银心显形」

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 银心黑洞的追踪者 / Andrea Ghez 1965– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 银心恒星轨道 / 自适应光学 / Sgr A* 质量 / 第四位女性
04  早年：从 Apollo 梦想到物理 (1965–1987) — 纽约、芝加哥 Lab School、数学转物理、MIT
05  Caltech 博士：T Tauri 星巡天 (1987–1993) — 斑纹成像、Neugebauer 指导
06  UCLA 岁月与早期荣誉 (1994–2003) — Cannon/Pierce/Goeppert-Mayer、1998 与 2000 关键论文
07  自适应光学：把大气抹平（核心贡献页）— Keck 10 米镜、波前校正、银心高分辨成像
08  追踪银心恒星轨道 — S2 完整椭圆轨道、S0-102（2012）、开普勒第三定律
09  Sgr A*：4.1±0.6 百万太阳质量（核心贡献页）— 证据链、比 M31 近 100 倍
10  荣誉与认可 — Nobel 2020 · MacArthur 2008 · Crafoord 2012 · NAS 2004 · Bakerian 2015
11  第四位女性：Curie → Goeppert Mayer → Strickland → Ghez
12  科普与传承 — You Can Be a Woman Astronomer、TED 2009、Gamow 讲座
13  结尾
```

- 公式框建议：Kepler 第三定律推质量 `M = 4π²a³/(GT²)`（Sgr A* 质量测定的方法学核心；page.md 无显式公式，注明为概念图式）

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 2020 一半 = Ghez + Genzel（银心超大质量致密天体），另一半 = Penrose；总口径 "for their discoveries relating to black holes"；理由句逐字用 "for the discovery of a supermassive compact object at the centre of our galaxy" |
| 「第四位女性」 | page.md 明载 fourth woman：Marie Curie (1903) → Maria Goeppert Mayer (1963) → Donna Strickland (2018) → Ghez (2020)；顺序勿错，勿写成"第三位"（Strickland 2018 在先） |
| 博士导师名 | frontmatter 作 Gerald Neugebauer、infobox 作 Gerry Neugebauer（同一人）；库内规范记录为 `Gerry Neugebauer`(id=2868)，yaml 沿用，勿新建 Gerald 形式造成分裂 |
| 身份表述 | American **astrophysicist**；本科数学专业后转物理——叙述可写"数学起点转物理"，勿写成"数学家得诺奖" |
| 星名区分 | S2（已完整椭圆轨道）与 S0-102（2012 证认的第二颗短周期星）是两颗恒星，勿混写；S2 不是人名 |
| 数字口径 | Sgr A* 质量 4.1±0.6 百万太阳质量（Kepler 第三定律）；银心比 M31（下一最近超大质量黑洞 M31* 所在）近一百倍——两组数字勿混 |
| Genzel 关系 | 两人是共享诺奖的**竞争/并行团队**（UCLA vs MPE），page.md 只写 "shared the Nobel Prize"——只入 co-honored，勿编 rivalry/colleague |
| 科普合著 | Judith Love Cohen 是童书 *You Can Be a Woman Astronomer* 合著者，**非科研关系，不入库** |
| 无载禁写 | 两个儿子的姓名、学生名单、高中化学老师姓名、诺奖演讲引语——page.md 无载即不写 |
| 引语红线 | 正文无直接引语；TED 2009 与 Gamow 讲座只可引**标题**（"The Hunt For a Supermassive Black Hole" / "From the Possibility to the Certainty of a Supermassive Black Hole"），禁编演讲原文 |
| 同奖不同年 | Crafoord Prize：Ghez 2012、Genzel 2012（同年各自获奖口径各忠于本人页面）；Karl Schwarzschild Medal 是 Genzel 篇的，勿串 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| adaptive optics | 自适应光学 | 波前实时校正，Known for 条目 |
| speckle imaging | 斑纹成像 | 博士论文技术（2.2μm） |
| T Tauri star | 金牛 T 型星 | 年轻恒星，早期研究对象 |
| Sagittarius A* | 人马座 A* | 银心致密天体，写法带星号 |
| supermassive black hole | 超大质量黑洞 | 诺奖理由句用 compact object 措辞 |
| stellar kinematics | 恒星运动学 | 以恒星运动为探针 |
| Kepler's third law | 开普勒第三定律 | 质量测定方法核心 |
| S2 / S0-102 | S2 星 / S0-102 星 | 两颗不同恒星 |
| MacArthur Fellowship | 麦克阿瑟奖 | "天才奖"，非学会院士 |
| Annie J. Cannon Award | 安妮·坎农天文奖 | 面向女性天文学家的早期荣誉 |
| Bakerian Medal | 贝克里安奖章 | 英国皇家学会演讲奖 |
| Crafoord Prize | 克拉福德奖 | 瑞典皇家科学院，天文诺奖补位奖 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**: **Ascension** — Cold Cinema（2:32，科幻/史诗/上升）
- **匹配理由**: "上升/科幻" 匹配 Ghez 的叙事弧线——从 Apollo 登月点燃的少女梦想，到把自适应光学推向极致、让不可见银心"升出"尘埃，再到物理学诺奖第四位女性的里程碑；"史诗" 匹配 Keck 望远镜工程与三十年观测计划的分量。
- **备选** (未采用): Last Hope（戏剧性/力量，可作 Genzel 备选）、Shine Like The Sun（美丽/振奋，稍轻）。
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav` → 复制为 `presentations/21th_century/Andrea_Ghez/Ascension.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Andrea_Ghez/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` + `MySQL/data/Andrea_Ghez.yaml` | 领域+社会关系入库（第 4/4.5 步） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
