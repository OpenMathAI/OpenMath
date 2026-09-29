# 物理学家立传提示词（21 世纪批次：Roger Penrose）

> **本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」**，以 Roger Penrose（2020 诺贝尔物理学奖，黑洞形成是广义相对论稳健预言的发现者）为实例。
> 结构对齐标杆 `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。标注 `【模板通用】` 部分可复用；`【人物专属】` 部分为本篇定制。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家标杆 Kenneth G. Wilson 提示词 + Beamer 成品骨架（`Eugene_Wigner_zh.tex` 一系）。
- **本实例**：Sir Roger Penrose（罗杰·彭罗斯，爵士、功绩勋章成员）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达——骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Roger Penrose（1931-08-08 生于英国埃塞克斯郡科尔切斯特，在世）
- **气质关键词**：**时空拓扑的几何大师、奇点定理的证明者、跨越数学与物理的博学者** —— 2020 诺贝尔物理学奖获奖理由（独享一半）：
  > "for the discovery that black hole formation is a robust prediction of the general theory of relativity"（因发现黑洞形成是广义相对论的稳健预言）
  > 另一半授予 Reinhard Genzel 与 Andrea Ghez（银河系中心超大质量致密天体的发现），理由句不同，勿混排。
- **设计母题**：**被捕获的面（trapped surface）与不可能之形**。他用拓扑学「无需解方程」地证明坍缩必然终结于奇点；又以 Penrose 三角形/阶梯/镶嵌把「不可能」变成可见——视觉语言用经典场线收敛几何与 Penrose 镶嵌五重对称呼应。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Roger_Penrose/page.md`（**已有本地**；`Roger_Penrose.html` 与 `images/` **待下载**，Wikipedia URL：https://en.wikipedia.org/wiki/Roger_Penrose ）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（`21st_century/Roger_Penrose/page.md`，含 frontmatter：QID Q193803 / 生 1931-08-08 / 国籍 United Kingdom / 职业 mathematician, physicist, philosopher, university teacher, astronomer, astrophysicist / 博士导师 J. A. Todd / 教育 UCL、Cambridge）
- 🔲 `Roger_Penrose.html` 与 `images/` 待下载（URL：https://en.wikipedia.org/wiki/Roger_Penrose ）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1931-08-08 生于 Colchester, Essex, England，在世
  - 国籍：United Kingdom（English mathematician）
  - 家庭：父 Lionel Penrose（精神病学家/遗传学家）；母 Margaret（née Leathes，医师）；兄 Oliver Penrose（物理学家）、弟 Jonathan Penrose（国际象棋特级大师）、妹 Shirley Hodgson（遗传学家）；继父 Max Newman（数学家/计算机科学家）；二战期间随父在加拿大伦敦（安大略）度过童年；叔叔 Roland Penrose（画家）
  - 教育：University College School → UCL（1952 数学 BSc 一等荣誉）→ St John's College, Cambridge（1957 PhD，代数几何）
  - 博士导师：最终导师 John A. Todd（代数几何学家）；最初师从几何与天文学教授 W. V. D. Hodge；博士论文 *Tensor Methods in Algebraic Geometry*（1957）
  - 任职（含年份）：Bedford College 助教 1956–57 → Cambridge St John's research fellow（1959 与 Joan Wedge 结婚）→ NATO 研究奖学金 1959–61（Princeton → Syracuse）→ King's College London 研究者 1961–63 → UT Austin 访问副教授 1963–64 → Birkbeck College reader 1964 → 访问职位 Yeshiva/Princeton/Cornell（1966–67、1969）→ Rice University 1983–87 → Oxford（Rouse Ball Professor of Mathematics emeritus、Wadham College emeritus fellow）→ Penn State Francis and Helen Pentz 杰出访问教授
  - 关键荣誉：Nobel 2020（一半）；Wolf Prize 1988（与 Hawking 共享）；Eddington Medal 1975（与 Hawking 共同）；Heineman Prize（正文 1971 为 Dannie Heineman Prize for **Astrophysics**，AAS+AIP 颁发；infobox 另列 Dannie Heineman Prize for Mathematical Physics——两奖勿混）；FRS 1972；Royal Medal 1985；Dirac Medal (IOP) 1989；Albert Einstein Medal 1990；Naylor Prize 1991；Knight Bachelor 1994；Karl Schwarzschild Medal 2000；Order of Merit 2000；De Morgan Medal 2004；Dalton Medal 2005；Dirac Medal (UNSW) 2006；Copley Medal 2008；Fonseca Prize 2011；Richard R. Ernst Medal 2012；Academia Europaea 2019；1998 NAS 外籍院士；1992–95 任国际广义相对论与引力学会主席；2025 Golden Plate Award
  - 知名博士生（infobox + 正文双重明载，共 9 人）：Andrew Hodges、Lane Hughston、Richard Jozsa、Claude LeBrun、John McNamara、Tristan Needham、Tim Poston、Asghar Qadir、Richard S. Ward
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1931 生于 Colchester → 童年读 Gamow《Mr. Tompkins》立志（自述引语可引）→ 二战随父居加拿大 → 1952 UCL 数学 BSc 一等 → 1955 在读博士期间再引入 Moore–Penrose 广义逆 → 1950s 与父共创 Penrose 三角形、与 Escher 通信 → 1956–57 Bedford College 助教 → 1957 剑桥博士（Todd 指导）→ 1959 与 Joan Wedge 结婚；NATO 奖学金赴 Princeton/Syracuse → 1961–63 King's College London → 1963–64 UT Austin 访问 → 1964 Birkbeck reader（Sciama 引导转向天体物理）→ 1965 论文 "Gravitational Collapse and Space-Time Singularities"（trapped surface 拓扑方法）→ 1967 扭量理论 → 1969 弱宇宙监督猜想 + Penrose 过程 → 1971 自旋网络；Heineman 天体物理奖 → 1972 FRS → 1974 Penrose 镶嵌 → 1975 Eddington Medal（与 Hawking）→ 1979 强宇宙监督猜想 + Weyl 曲率假设 → 1983–87 Rice 大学 → 1984 准晶体中观测到 Penrose 镶嵌图案 → 1985 Royal Medal → 1988 Wolf Prize（与 Hawking）→ 1989 Dirac Medal (IOP)；《The Emperor's New Mind》获 Royal Society Science Book Prize → 1990 爱因斯坦奖章 → 1991 Naylor Prize → 1994 受封爵士；《Shadows of the Mind》 → 1996 与 Hawking 合著《The Nature of Space and Time》 → 1998 NAS 外籍院士 → 2000 功绩勋章（OM）→ 2004 De Morgan Medal；《The Road to Reality》 → 2008 Copley Medal → 2010《Cycles of Time》与共形循环宇宙学（CCC） → 2016《Fashion, Faith, and Fantasy》 → 2019 Academia Europaea → 2020 诺贝尔物理学奖（一半） → 2025 Golden Plate Award

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | mathematical physics | 数学物理 | 抽象指标记号、Newman–Penrose 形式主义 | 核心页 |
| 1 | general relativity | 广义相对论 | 奇点定理、宇宙监督、Penrose 图/过程 | 奇点页 |
| 2 | twistor theory | 扭量理论 | 1967 发明，Minkowski 空间到复几何的映射 | 扭量页 |
| 3 | cosmology | 宇宙学 | Weyl 曲率假设、共形循环宇宙学（CCC） | 宇宙页 |
| 4 | tessellations | 镶嵌与趣味数学 | Penrose 镶嵌（非周期铺砌）→ 准晶体先声 | 镶嵌页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> **只收 page.md 明载的关系**；对手方 name_en 用库内规范形式（Hodge=430、Sciama=2040、Jozsa=1891、Poston=996、Minsky=216 已在库，沿用其形式；其余按 frontmatter/infobox 全形新建 stub）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | J. A. Todd | 师→生（博士导师） | 剑桥博士导师，代数几何学家，论文 Tensor Methods in Algebraic Geometry (1957) |
| advisor-student | W. V. D. Hodge | 师→生 | 最初师从的几何与天文学教授，后由 Todd 指导完成博士论文 |
| advisor-student | Andrew Hodges | Penrose → 学生 | 博士生，Andrew Wiles 同传作者 |
| advisor-student | Lane Hughston | Penrose → 学生 | 博士生 |
| advisor-student | Richard Jozsa | Penrose → 学生 | 博士生，量子算法（Deutsch–Jozsa） |
| advisor-student | Claude LeBrun | Penrose → 学生 | 博士生 |
| advisor-student | John McNamara | Penrose → 学生 | 博士生，数学生物学家 |
| advisor-student | Tristan Needham | Penrose → 学生 | 博士生，Visual Differential Geometry 作者 |
| advisor-student | Tim Poston | Penrose → 学生 | 博士生 |
| advisor-student | Asghar Qadir | Penrose → 学生 | 博士生 |
| advisor-student | Richard S. Ward | Penrose → 学生 | 博士生，扭量理论合作者 |
| influence | Dennis Sciama | 无向 | 引导其从纯数学转向天体物理 |
| colleague | Stephen Hawking | 无向 | 共同发展大爆炸奇点定理（Penrose–Hawking 奇点定理），合著 The Nature of Space and Time |
| co-honored | Stephen Hawking | 无向 | 1988 Wolf Prize 共同得主；1975 Eddington Medal 共同得主 |
| co-honored | Reinhard Genzel | 无向 | 2020 诺贝尔物理学奖另一半得主 |
| co-honored | Andrea Ghez | 无向 | 2020 诺贝尔物理学奖另一半得主 |
| controversy | Marvin Minsky | 无向 | Minsky 强烈批评其 The Emperor's New Mind 的 Penrose–Lucas 论证 |
| parent-child | Lionel Penrose | 无向 | 父亲，精神病学家/遗传学家 |
| spouse | Vanessa Thomas | 无向 | 1988 年结婚（前妻 Joan Isabel Wedge，1959 结婚后离异） |

- 入库操作：`MySQL/seed_person.py data/Roger_Penrose.yaml`（幂等；Duplicate entry 撞 uq_rel 属正常跳过）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：几何严谨、拓扑想象、跨界浪漫
- **配色**：扭量紫（数学物理深度）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeMath` 数学物理 — 扭量紫 `#4A2A6A`（主色）
  - `badgeGR` 广义相对论 — 靛蓝 `#2C4A7C`
  - `badgeTwistor` 扭量理论 — 青绿 `#0E7C7B`
  - `badgeTiling` 镶嵌/趣味数学 — 琥珀 `#D98E30`
- **背景母题**：稀疏大块实心圆 + 五重对称菱形镶嵌线稿，呼应「被捕获面」几何与 Penrose 镶嵌的非周期之美

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 时空拓扑的几何大师 / Roger Penrose 1931– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、家庭、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 奇点定理 / 扭量理论 / 自旋网络 / Penrose 镶嵌 / CCC
04  早年与家族：科尔切斯特 (1931–1952) — Penrose 家族、Gamow 启蒙、UCL 数学
05  剑桥博士：从代数几何出发 (1952–1957) — Moore–Penrose 逆、Todd 指导、Penrose 三角形与 Escher
06  转折：Sciama 与天体物理 (1961–1964) — King's College、UT Austin、Birkbeck
07  1965：Gravitational Collapse and Space-Time Singularities（核心贡献页）— trapped surface、拓扑方法
08  与 Hawking：奇点定理与宇宙监督 — Penrose–Hawking 定理、1969 弱/1979 强宇宙监督、Penrose 过程
09  扭量理论与自旋网络 (1967/1971) — 圈量子引力先声、抽象指标记号
10  Penrose 镶嵌与准晶体 (1974/1984) — 非周期铺砌、五重对称、Shechtman
11  意识与量子引力 — The Emperor's New Mind、Orch-OR（与 Hameroff）、Minsky 之辩（少数派注记）
12  共形循环宇宙学 (2010) — Weyl 曲率假设、Cycles of Time、WMAP 同心圆
13  荣誉与认可 — Nobel 2020 · Wolf 1988 · Copley 2008 · OM 2000 · 爵士 1994
14  遗产：从黑洞到不可能之形
15  结尾
```

- 公式框建议：Weyl 曲率假设的共形几何概念图式（或 trapped surface 定义示意；page.md 无显式公式，注明为概念图式）

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 2020 **一半归 Penrose 个人**（黑洞形成是 GR 稳健预言），另一半归 Genzel+Ghez（银河系中心超大质量致密天体）；勿写成三人平分或同一理由 |
| 身份表述 | English **mathematician / mathematical physicist / philosopher of science**；infobox Fields 是 Mathematical physics 与 tessellations——勿通篇写成"天文学家/观测物理学家" |
| 博士导师 | 最终导师是代数几何学家 **J. A. Todd**（论文为代数几何）；最初师从 Hodge——勿写成"物理学博士"或漏掉 Hodge 起点 |
| Hawking 关系 | Hawking 是 **Sciama 的学生**（page.md 原文 "Sciama's student Stephen Hawking"）；Penrose 与 Hawking 是合作者/共同获奖者，**非师承** |
| Sciama | 是「引导其从纯数学转向天体物理」的影响者，非正式导师——用 influence 类型入库 |
| Heineman 双奖 | 正文 1971 = Dannie Heineman Prize for **Astrophysics**（AAS+AIP）；infobox 另列 Dannie Heineman Prize for **Mathematical Physics**——两个不同奖项并存，叙述时任选其一并注明口径 |
| 准晶体 | Penrose 镶嵌（1974）**先于**准晶体发现；1984 年在原子排列中观测到该图案；准晶体是 Shechtman 的发现（2011 化学诺奖）——勿写 Penrose 发现准晶体 |
| Orch-OR | 与麻醉学家 Stuart Hameroff 共同提出，是**少数派观点**（Minsky 批评、Tegmark 退相干计算反驳），叙述须平衡，勿写成定论 |
| Escher | 是艺术通信/相互启发（Waterfall、Ascending and Descending），**非科研关系，不入库** |
| 家族同名 | Penrose 家族多人成名：Lionel（父）、Oliver（兄，物理学家）、Jonathan（弟，棋手）、Shirley（妹）——note 里写清身份，勿张冠李戴 |
| 无载禁写 | 博士后导师身份（NATO 奖学金站 Princeton/Syracuse 勿写成导师）、子女姓名（infobox 仅载 4+1 子女数）、诺奖演讲引语原文——page.md 未载即不写 |
| 引语红线 | 可引原文有：Gamow Tompkins 童年自述、Manjit Kumar 书评转述段、BBC 2010 "I'm not a believer myself"、1991 电影 universe purpose 语、De Morgan citation（LMS 官方）、Minsky 批评语；其余禁编 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| singularity theorem | 奇点定理 | trapped surface 拓扑证明，非微扰法 |
| trapped surface | 被捕获面 | 奇点定理核心概念 |
| cosmic censorship hypothesis | 宇宙监督猜想 | weak (1969) 与 strong (1979) 两版 |
| twistor theory | 扭量理论 | 复几何映射，勿译"扭量空间论" |
| spin network | 自旋网络 | 后成为圈量子引力的时空几何 |
| Penrose tiling | 彭罗斯镶嵌 | 非周期铺砌、五重对称 |
| quasicrystal | 准晶体 | Shechtman 发现，Penrose 镶嵌是其先声 |
| conformal cyclic cosmology | 共形循环宇宙学（CCC） | aeon 无限循环 |
| Weyl curvature hypothesis | 外尔曲率假设 | 初始条件与热二定律起源 |
| Penrose diagram | 彭罗斯图 | 共形因果图，勿译"彭罗斯图解法" |
| Penrose process | 彭罗斯过程 | 从旋转黑洞提取能量 |
| Moore–Penrose inverse | Moore–Penrose 广义逆 | 1955 再引入（Moore 1920 先创） |
| Orch-OR | 调谐客观还原 | 与 Hameroff 共同提出，少数派 |
| abstract index notation | 抽象指标记号 | 张量记号体系 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**: **Cinematic Experience** — Alex-Productions（47k views，电影感/高张力）
- **匹配理由**: "电影感/高张力" 匹配 Penrose 的双重叙事——1965 年拓扑学证明奇点必然形成（理论高潮）与 Penrose 三角形/镶嵌的视觉奇想（跨界高潮）；全篇 15 页从纯数学到黑洞到意识跨度极大，需要一支能撑住章节高潮的曲目。
- **备选** (未采用): Mirage（梦幻/抽象，适合扭量理论但整体偏轻）、Through the Darkness（留给 Genzel 黑洞观测叙事）。
- **本地路径**: `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` → 复制为 `presentations/21th_century/Roger_Penrose/CinematicExperience.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Roger_Penrose/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` + `MySQL/data/Roger_Penrose.yaml` | 领域+社会关系入库（第 4/4.5 步） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
