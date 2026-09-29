# 物理学家立传提示词（21 世纪批次：Syukuro Manabe）

> **本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」**，以 Syukuro Manabe（2021 诺贝尔物理学奖，地球气候物理建模与全球变暖可靠预测的奠基人）为实例。
> 结构对齐标杆 `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。标注 `【模板通用】` 部分可复用；`【人物专属】` 部分为本篇定制。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家标杆 Kenneth G. Wilson 提示词 + Beamer 成品骨架（`Eugene_Wigner_zh.tex` 一系）。
- **本实例**：Syukuro "Suki" Manabe（真鍋 淑郎，真锅淑郎）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达——骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Syukuro Manabe（1931-09-21 生于日本爱媛县宇摩郡新立村，在世）
- **气质关键词**：**数字气候的开创者、CO₂ 增温的预言者、仰望天空的建模者** —— 2021 诺贝尔物理学奖获奖理由（与 Klaus Hasselmann 共享一半）：
  > "for the physical modeling of Earth's climate, quantifying variability and reliably predicting global warming"（因对地球气候的物理建模、量化变率并可靠预测全球变暖）
  > 另一半授予 Giorgio Parisi（复杂物理系统），理由句不同，勿混排。
- **设计母题**：**把天空装进计算机（the sky in the machine）**。从一维辐射-对流单柱模型到海气耦合 GCM，Manabe 用数值网格第一次让地球气候成为可计算的实验对象——视觉语言用网格球与上升的温度曲线呼应「数字地球」。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Syukuro_Manabe/page.md`（**已有本地**；`Syukuro_Manabe.html` 与 `images/` **待下载**，Wikipedia URL：https://en.wikipedia.org/wiki/Syukuro_Manabe ）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（`21st_century/Syukuro_Manabe/page.md`，含 frontmatter：QID Q3675789 / 生 1931-09-21 / 国籍 Japan、United States / 职业 climatologist, meteorologist / 博士导师 Shigekata Shōno / 教育 University of Tokyo）
- 🔲 `Syukuro_Manabe.html` 与 `images/` 待下载（URL：https://en.wikipedia.org/wiki/Syukuro_Manabe ）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1931-09-21 生于爱媛县宇摩郡新立村（Shinritsu Village, Uma District, Ehime Prefecture），在世
  - 国籍：Japanese–American（Japan + United States 两条）
  - 家庭：祖父与父亲皆为医生，经营村里唯一的诊所
  - 教育：爱媛县立三岛高等学校 → 东京大学（1953 BA、1955 MA、1958 DSc，主修气象学）
  - 博士导师：Shigekata Shono（正文作 Shigekata Shono (1911–1969)，frontmatter 长音符作 Shōno；yaml 用正文 ASCII 形式）
  - 任职（含年份）：美国气象局大气环流研究组（今 NOAA 地球物理流体动力学实验室 GFDL）1958/博士毕业后至 1997（先华盛顿后普林斯顿）；1997–2001 日本 FRONTIER 全球变化研究系统全球变暖研究 Division 主任；2002 起普林斯顿大学大气与海洋科学项目访问研究合作者、现任 senior meteorologist；名古屋大学特别招聘教授 2007-12 至 2014-03
  - 关键荣誉（时间序）：Carl-Gustaf Rossby Research Medal 1992（AMS）；Blue Planet Prize 1992（首届得主）；Roger Revelle Medal 1993（AGU）；Asahi Prize 1995；Volvo Environment Prize 1997；Milutin Milankovic Medal 1998（EGS）；William Bowie Medal 2010（AGU）；Benjamin Franklin Medal 2015；BBVA Foundation Frontiers of Knowledge Award（气候变化类）2016（与 James Hansen 共同）；Crafoord Prize in Geosciences 2018（与 Susan Solomon 共同）；**Nobel Prize in Physics 2021**（与 Hasselmann 共享一半）；Order of Culture（日本文化勋章）2021；Great Immigrants Awards 2022；AMS Second Half Century Award、Clarence Leroy Meisinger Award；NAS 院士；日本学士院/欧洲科学院/加拿大皇家学会外籍成员；NOAA 200 年十大突破（与 Bryan 的首个全球气候模式）；1998-03 普林斯顿三天的退休致敬研讨会；2005 AMS 年会 Suki Manabe Symposium
  - 知名博士生（infobox 明载，共 3 人）：Isaac Held、Kenneth Bowman、Alex Hall
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1931 生于爱媛新立村 → 小学已痴迷天气（同学回忆其台风与降雨议论，引语可引）→ 家族期望学医，自称"血冲头当不了好医生""只会仰望天空出神"（自述引语可引）→ 爱媛县立三岛高中 → 入东京大学加入 Shigekata Shono 研究组、主修气象学 → 1953 BA / 1955 MA / 1958 DSc → 赴美入美国气象局大气环流研究组（后为 NOAA GFDL），与主任 Joseph Smagorinsky 发展三维大气模式 → 1965 Manabe–Smagorinsky–Strickler 含水循环 GCM 模拟气候学论文 → 1967 Manabe–Wetherald 一维单柱辐射-对流平衡模型（水汽正反馈）：CO₂ 增加使地表与对流层升温、平流层降温 → 1969 Manabe–Bryan 首个海气耦合气候模拟 → 1975 Manabe–Wetherald GCM 中首次模拟 CO₂ 加倍的三维温度与水循环响应 → 1980 Manabe–Stouffer GCM 对 CO₂ 浓度的敏感性 → 1989–92 Stouffer/Spelman/Bryan 合作：耦合模式对渐变 CO₂ 的瞬变响应（Part I/II）→ 1992 Rossby Medal + Blue Planet 首奖 → 1995 Asahi Prize → 1997 Volvo 环境奖；转任日本 FRONTIER 全球变暖研究 Division 主任 → 1995/2000 Manabe–Stouffer 北大西洋淡水注入与突变气候（古气候记录）→ 1998 Milankovic Medal；NOAA 十大突破；3 月退休致敬研讨会 → 2002 回普林斯顿 → 2010 Bowie Medal → 2015 Franklin Medal → 2016 BBVA（与 Hansen）→ 2018 Crafoord 地球科学奖（与 Solomon）→ 2020 与 Broccoli 合著 *Beyond Global Warming* → 2021 诺贝尔物理学奖 + 日本文化勋章 → 2022 Great Immigrants Award → 2023 诺贝尔演讲刊于 *Reviews of Modern Physics*

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | climate modeling | 气候建模 | 计算机模拟全球气候变化的开创者 | 核心页 |
| 1 | climatology | 气候学 | infobox Fields 主口径 | 总览页 |
| 2 | general circulation model | 大气环流模式（GCM） | 1965 含水循环 GCM、三维响应 | GCM 页 |
| 3 | meteorology | 气象学 | 东京大学主修、AMS 系列奖 | 早年页 |
| 4 | climate change | 气候变化 | CO₂ 加倍实验、突变气候、全球变暖预测 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> **只收 page.md 明载的关系**；对手方 name_en 用库内规范形式（Hasselmann=3180、Parisi=3184 已在库沿用；其余按正文/infobox 全形新建 stub；1965 论文第三作者 Strickler 仅在论文叙述出现，不单列关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Shigekata Shono | 师→生（博士导师） | 东京大学气象学导师（1911–1969），1958 DSc |
| advisor-student | Isaac Held | Manabe → 学生 | 博士生，GFDL 气候动力学家 |
| advisor-student | Kenneth Bowman | Manabe → 学生 | 博士生 |
| advisor-student | Alex Hall | Manabe → 学生 | 博士生 |
| colleague | Joseph Smagorinsky | 无向 | NOAA GFDL 主任，共同发展三维大气模式 |
| colleague | Richard T. Wetherald | 无向 | 1967 辐射-对流模型与 1975 CO₂ 加倍 GCM 合作 |
| colleague | Kirk Bryan | 无向 | 1969 首个海气耦合气候模拟合作者 |
| colleague | Ronald Stouffer | 无向 | 1980–2000 系列 GCM 敏感性/瞬变响应/突变气候论文合作者 |
| colleague | Anthony J. Broccoli | 无向 | 合著 Beyond Global Warming (2020) |
| co-honored | Klaus Hasselmann | 无向 | 2021 诺贝尔物理学奖共享一半 |
| co-honored | Giorgio Parisi | 无向 | 2021 诺贝尔物理学奖另一半得主 |
| co-honored | James Hansen | 无向 | 2016 BBVA Frontiers of Knowledge Award（气候变化类）共同得主 |
| co-honored | Susan Solomon | 无向 | 2018 Crafoord Prize in Geosciences 共同得主 |

- 入库操作：`MySQL/seed_person.py data/Syukuro_Manabe.yaml`（幂等；Duplicate entry 撞 uq_rel 属正常跳过）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：温厚、长期主义、把直觉变成方程
- **配色**：气候橄榄绿（大气与海洋）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeModel` 气候建模 — 橄榄绿 `#3D6B35`（主色）
  - `badgeGCM` 大气环流模式 — 深蓝 `#1C4E7A`
  - `badgeCO2` 气候变化 — 暗红 `#8C3A2B`
  - `badgeOcean` 海气耦合 — 青绿 `#0E7C7B`
- **背景母题**：稀疏大块实心圆 + 覆盖球面的细网格线 + 一条缓慢爬升的温度折线，呼应「数字地球上的百年升温」

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 数字气候的开创者 / Syukuro Manabe 1931– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 辐射-对流模型 / GCM / 海气耦合 / CO₂ 加倍实验
04  早年：爱媛的仰望天空少年 (1931–1953) — 医生世家、拒学医自述、东京大学气象学
05  博士岁月：Shono 研究组 (1953–1958) — BA/MA/DSc、气象学
06  远渡重洋：美国气象局与 GFDL (1958–) — Smagorinsky、华盛顿到普林斯顿
07  1967：辐射-对流模型（核心贡献页）— 单柱模型、水汽正反馈、地表/对流层升温 vs 平流层降温
08  从一维到三维：GCM 与 CO₂ 加倍 (1965/1975) — Manabe–Smagorinsky–Strickler、三维温度与水循环响应
09  1969：海气耦合的诞生（核心贡献页）— 与 Bryan 的首个耦合模拟、瞬变响应系列
10  突变气候与古气候 — 北大西洋淡水注入、热盐环流、Stouffer 合作线
11  荣誉与认可 — Nobel 2021 · Blue Planet 首奖 1992 · Crafoord 2018 · BBVA 2016 · 文化勋章
12  遗产：从预言到气候科学主流
13  结尾
```

- 公式框建议：辐射-对流平衡的能量收支概念式（地表+对流层升温 / 平流层降温的垂直廓线示意；page.md 无显式公式，注明为概念图式）

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 2021 一半 = Manabe + Hasselmann（气候物理建模/量化变率/可靠预测全球变暖），另一半 = Parisi（复杂系统，理由句不同）；导语概括句与官方理由句略有措辞差，引用时用官方句 "for the physical modeling of Earth's climate, quantifying variability and reliably predicting global warming" |
| 身份表述 | 正文 intro 明载 physicist + meteorologist + climatologist 三重身份；infobox Fields 全是气象/气候——叙述以"物理学家出身的气候建模者"口径，勿写成天文学家 |
| 国籍双条 | Japanese–American：Japan 与 United States 两条并列，勿只写其一 |
| 导师名形 | frontmatter 作 Shigekata Shōno（长音符），正文作 Shigekata Shono (1911–1969)；yaml/入库用 ASCII 形式 Shigekata Shono，note 写清 |
| 奖项共同者 | Hansen = BBVA 2016、Solomon = Crafoord 2018——是**非诺奖**的共同奖，note 必须写明奖项名，勿写成"诺奖共同得主" |
| Strickler | 1965 GCM 论文第三作者 Robert F. Strickler 仅出现在文献列表，正文无叙述——**不建关系** |
| Nakamura | 中村修二（2014 物理诺奖、同出爱媛）致电祝贺是**事件**，非关系，不入库 |
| 团队归属 | 1958 起 GFDL 是其主线机构（"美国气象局大气环流研究组，今 NOAA GFDL"），1997–2001 回日本、2002 起普林斯顿——三段分开写勿混 |
| 无载禁写 | 配偶/子女、博士论文题目（page.md 未载题目）、Smagorinsky 之外的 GFDL 职务细节、诺奖演讲内容原文——无载即不写 |
| 引语红线 | 可引正文英文原话：童年台风议论（同学转述，注明转述）、"whenever there's an emergency, the blood rushes to my head…"、"I had a horrible memory…"、"gaze at the sky and get lost in my thoughts"；其余禁编 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| climate model | 气候模式 | "模式"（模型），非"气候模型玩具"义 |
| general circulation model (GCM) | 大气环流模式 | 1965 首次含水循环 |
| radiative-convective equilibrium | 辐射-对流平衡 | 1967 单柱模型核心 |
| water vapor feedback | 水汽（正）反馈 | 增温放大机制 |
| CO2 doubling | CO₂ 浓度加倍 | 1975 GCM 实验设定 |
| coupled ocean–atmosphere model | 海气耦合模式 | 1969 与 Bryan 首创 |
| transient response | 瞬变响应 | 1989–92 系列论文 |
| thermohaline circulation | 热盐环流 | 1999 Tellus B 主题 |
| abrupt climate change | 突变气候 | 北大西洋淡水注入假说 |
| paleoclimatic record | 古气候记录 | 突变气候变化证据来源 |
| Order of Culture | （日本）文化勋章 | 2021，勿与诺贝尔混 |
| Carl-Gustaf Rossby Research Medal | 罗斯贝研究奖章 | 气象学界最高奖之一，1992 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions（56k views，时间感/纪录片）
- **匹配理由**: "时间感/纪录片" 完美匹配气候建模的本质——Manabe 预言的不是明天的天气而是几十到上百年的气候走向，1967 年的曲线在半个世纪后被观测验证；"纪录片" 匹配从爱媛乡村少年到诺奖得主的 70 年人生叙事。
- **备选** (未采用): Timeless（同高受众纪录片系，留给他人）、SEA（流动/平稳，缺时间纵深）。
- **本地路径**: `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` → 复制为 `presentations/21th_century/Syukuro_Manabe/TheFlowOfTime.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Syukuro_Manabe/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` + `MySQL/data/Syukuro_Manabe.yaml` | 领域+社会关系入库（第 4/4.5 步） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
