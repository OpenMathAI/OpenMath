# 物理学家立传提示词（21 世纪批次：Michel H. Devoret）

> **本文件是 OpenPhysicist「物理学家立传提示词」的 Michel H. Devoret 专属实例**，按标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构撰写。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 事实基准唯一来源：本地 page.md（Wikipedia 全文），**page.md 无载的内容一律禁写**。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Michel H. Devoret（米歇尔·德沃雷），法国出生的美国物理学家，2025 诺贝尔物理学奖得主（三人共享），超导量子电路架构大师（quantronium / transmon / fluxonium）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Devoret 的主线是**从原子到量子机器**——把一个个宏观电路变成人工原子，用「人工原子（artificial atom）」作为贯穿视觉母题。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Michel Henri Devoret（1953-03-05 生于巴黎，在世）
- **气质关键词**：**人工原子的缔造者、超导量子比特的架构师、从基础量子现象到量子技术的摆渡人** —— 2025 诺贝尔物理学奖获奖理由（官方原文，禁改写）：
  > "For the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit."（因发现电路中的宏观量子力学隧穿与能量量子化）
- **设计母题**：**人工原子（the artificial atom）**。约瑟夫森结电路就是一个可设计、可操控的「原子」——视觉上用分立能级阶梯、超导环路与人造晶格图案贯穿全篇。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Michel_H._Devoret/page.md`
- **第 0 步标注**：page.md 已有本地；**html 与 images/ 待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Michel_H._Devoret`。
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步**：本提示词的第 4 步（研究领域表）与第 4.5 步（社会关系表）已由本批次完成入库（greatminds 库），立传时**只读勿改**，核对即可。

### 第 0 步：事实基准（page.md 已核对） 【人物专属】

- **生卒**：1953-03-05 生于巴黎，在世。
- **国籍**：法国出生；Wikipedia 导语口径为 French–American（法国—美国）物理学家。
- **家庭**：page.md 载其自述父母为犹太背景、无宗教信仰（立传可一句带过或略去，勿展开）。
- **教育**：École nationale supérieure des télécommunications（今 Télécom Paris）工程师学位 1975 → Orsay（今 Paris-Saclay University）DEA 量子光学 1976 → PhD 量子凝聚态物理 1982（Orsay 注册，博士研究在 CEA Saclay 的 Anatole Abragam 组内进行，导师 Neil S. Sullivan）；博士论文 *Mise en évidence d'un ordre orientationnel de type vitreux dans l'hydrogène et le deutérium solides*（1982）。
- **博士后**：1982–1984 在 John Clarke 组（UC Berkeley）。
- **任职机构**：回法国后与 Daniel Esteve、Cristian Urbina 在 CEA Saclay Orme des Merisiers 实验室创立 Quantronics 组；1996 赴 Delft 理工 Hans Mooij 实验室研究访问；2002 起任 Yale 教授（后为应用物理荣休教授）；2007–2012 任 Collège de France 介观物理教席（就职演讲 "From the Atom to Quantum Machines"，2013 辞任）；2023 出任 Google Quantum AI 首席科学家（量子硬件，intro 口径 Chief Scientist for Quantum Hardware）；2024 转 UC Santa Barbara 物理教授。
- **关键荣誉**：Prix de la Couronne française 1970；Ampère Prize 1991；Descartes–Huygens Prize 1995；EPS Europhysics Prize 2004（超导电路量子比特概念的实现与演示）；John Stewart Bell Prize 2013；Fritz London Memorial Prize 2014（与 Martinis、Schoelkopf 共享）；Olli V. Lounasmaa Memorial Prize 2016；Micius Quantum Prize 2021；Comstock Prize in Physics 2024；Nobel Prize in Physics 2025；法国荣誉军团骑士勋章 2008；美国艺术与科学院院士 2003、法国科学院院士 2007、美国科学院院士 2023。
- **知名学生**：Vincent Bouchiat（infobox Doctoral students 明载）。
- **核心贡献清单**：
  1. 1985 与 Clarke、Martinis 首次演示约瑟夫森结的量子化能级（与宏观量子隧穿同系列实验）——2025 诺奖核心；
  2. CEA Saclay Quantronics 组：隧穿穿越时间测量、电子泵发明、库珀对电荷的直接观测、quantronium 量子比特及其 Ramsey 条纹；
  3. transmon（与 Yale 的 Girvin、Schoelkopf 共同提出）——超导电荷量子比特的去噪化设计；
  4. fluxonium（2009）——特殊类型的磁通量子比特；
  5. 微波量子极限放大器（2010），用于量子比特读出与传感；
  6. 2018 参与演示超导人工原子中量子跳变的中断与逆转。
- **关键时间线（15–20 节点）**：1953 生于巴黎 → 1970 Prix de la Couronne française → 1975 Télécom Paris 工程师学位 → 1976 Orsay DEA 量子光学 → 1982 Orsay PhD（CEA Saclay Abragam 组，导师 Sullivan）→ 1982–84 Berkeley Clarke 组博士后 → 1985 与 Clarke/Martinis 演示约瑟夫森结能级量子化 → 回法国创立 CEA Saclay Quantronics 组（与 Esteve、Urbina）→ 隧穿穿越时间/电子泵/库珀对电荷/quantronium → 1991 Ampère Prize → 1995 Descartes–Huygens Prize → 1996 Delft Mooij 实验室访问 → 2002 任 Yale 教授 → 2003 美国艺术与科学院 → 2004 EPS Europhysics Prize → 2007 法国科学院院士、Collège de France 教席 → 2008 荣誉军团骑士勋章 → 2009 fluxonium → 2010 量子极限放大器 → 2012 教席止 → 2013 Bell Prize、辞任教席 → 2014 Fritz London Prize → 2016 Lounasmaa Prize → 2018 量子跳变中断与逆转 → 2021 Micius Prize → 2023 Google Quantum AI 首席科学家、NAS 院士 → 2024 Comstock Prize、转 UCSB → 2025 诺贝尔物理学奖。

### 第 4 步：研究领域表（已入库，只读） 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | superconducting quantum circuits | 超导量子电路 | quantronium / transmon / fluxonium 的统称母域 | 核心页 |
| 1 | quantum computing | 量子计算 | 超导量子比特架构与 Google Quantum AI 硬件 | 量子比特页 |
| 2 | mesoscopic physics | 介观物理 | Collège de France 教席名目；电子泵/库珀对电荷 | Quantronics 页 |
| 3 | circuit quantum electrodynamics | 电路量子电动力学 | 1985 能级量子化实验即其首个证据 | 1985 实验页 |
| 4 | quantum measurement | 量子测量 | 量子极限放大器、量子跳变的调控 | 测量页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致，已入库） 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Neil S. Sullivan | 对方是导师 | Orsay 博士导师（1982），博士研究在 CEA Saclay Abragam 组内进行 |
| advisor-student | Vincent Bouchiat | 对方是学生 | 博士生（infobox Doctoral students 明载） |
| colleague | John Clarke | 无向 | 1982–84 在其 Berkeley 组做博士后，1985 合作演示量子隧穿与能级量子化 |
| co-honored | John Clarke | 无向 | 2025 诺贝尔物理学奖共享；2021 Micius 量子奖共享 |
| colleague | John M. Martinis | 无向 | 1985 年合作演示约瑟夫森结能级量子化（其时为 Clarke 组博士生） |
| co-honored | John M. Martinis | 无向 | 2025 诺贝尔物理学奖共享 |
| colleague | Daniel Esteve | 无向 | CEA Saclay Quantronics 组共同创立者 |
| colleague | Cristian Urbina | 无向 | CEA Saclay Quantronics 组共同创立者 |
| colleague | Robert J. Schoelkopf | 无向 | Yale 同事，共同提出 transmon 量子比特 |
| co-honored | Robert J. Schoelkopf | 无向 | 2014 Fritz London Memorial Prize 共享 |
| colleague | Steven Girvin | 无向 | Yale 同事，共同提出 transmon 量子比特 |

### 第 5 步：配色方案 【人物专属】

- **气质**：量子阶梯、人造原子、法国蓝紫的精密
- **配色**：深紫（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 深紫 `#46356B`（批内唯一）
  - `badgeA` 超导量子电路 — 长春花蓝 `#7C5FD5`
  - `badgeB` 介观物理 — 青瓷 `#2E8B8B`
  - `badgeC` 量子测量 — 琥珀 `#E07B30`
  - `badgeD` 量子计算 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡 + 分立能级阶梯线，呼应人工原子的量子化能级。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（肖像待下载，2025 年照片优先）。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（France / USA 口径），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（机构 = UCSB / Yale / Collège de France）。
3. **必须有身份信息页**：含至少：生卒、国籍、出生地、教育（Télécom Paris/Orsay/CEA Saclay）、博士导师（Sullivan）、任职（Quantronics → Yale → Collège de France → Google → UCSB）、主要荣誉（Nobel 2025/Fritz London 2014/三位院士）、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 帧 + 共享首页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 人工原子的缔造者 / Michel H. Devoret 1953– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 1985 能级量子化 / quantronium / transmon / fluxonium / 量子极限放大器
04  巴黎求学 (1953–1982) — Télécom Paris、Orsay DEA 与博士、CEA Saclay Abragam 组
05  Berkeley 博士后 (1982–1984) — Clarke 组、1985 与 Martinis 演示能级量子化
06  Quantronics：CEA Saclay 的量子工坊 — 与 Esteve/Urbina、穿越时间、电子泵、库珀对电荷
07  quantronium：第一个固体量子比特之一 — Ramsey 条纹（公式框放约瑟夫森能级 E(φ) 或概念图式，注明）
08  耶鲁时代：transmon 的诞生 — 与 Girvin/Schoelkopf、去噪化的电荷量子比特
09  fluxonium 与量子极限放大器 — 2009/2010、2018 量子跳变的调控
10  从原子到量子机器 — Collège de France 教席、Google Quantum AI 首席科学家、UCSB
11  荣誉与认可 — Nobel 2025 · Comstock 2024 · Fritz London 2014 · Bell 2013 · 三院院士
12  遗产：超导量子计算的三块基石
13  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

**版式要点**：架构类人物多用「器件演进时间线」；公式框建议放约瑟夫森结势能 `U(φ) = -EJ·cos(φ) + (1/2)EC·n²`（page.md 无公式推导，属概念性呈现，需注明为示意）。

**Devoret 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | 全名 Michel Henri Devoret；条目与目录名用 Michel_H._Devoret；法语发音 dəvɔʁɛ，中译「德沃雷」 |
| 国籍口径 | 导语 "French–American"，frontmatter France；写「生于巴黎、长期在美任教」的法国—美国双口径，勿只写法国 |
| 博士导师 | 是 Neil S. Sullivan（page.md infobox + 正文明载）；Anatole Abragam 是 CEA Saclay 组长，**不是**导师，勿混 |
| transmon 归属 | transmon 由 Devoret + Girvin + Schoelkopf 在 Yale 共同提出，禁写成 Devoret 独创 |
| quantronium 归属 | quantronium 是 CEA Saclay Quantronics 组成果（与 Esteve/Urbina），与 Yale/Google 无关 |
| Google 职位措辞 | intro 作 "Chief Scientist for Quantum Hardware"（2023），正文作 "Chief Scientist for Hardware"——立传统一用 intro 口径，勿再发明第三种 |
| Collège de France 年份 | 教席 2007–2012、2013 辞任；就职演讲题 "From the Atom to Quantum Machines"，勿把 2013 写成教席结束年 |
| 两个三人组勿混 | 2025 Nobel = Clarke + Devoret + Martinis；2021 Micius = Clarke + Devoret + Yasunobu Nakamura（page.md Devoret 篇 Notes 明载） |
| 2014 Fritz London 三人 | 与 Martinis、Schoelkopf 共享（Martinis 篇正文 + Devoret 篇 Notes 明载），勿写成两人 |
| 在世 | 1953 年生、在世，生卒页留白卒年 |
| Delft 1996 | 是在 Hans Mooij 实验室的研究访问，非任职，勿写成教职 |
| 授勋 | 2008 获法国荣誉军团骑士勋章；立传只写奖项本身，不展开授勋人 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| transmon | 传输子量子比特 | transmon qubit，Yale 三人共同提出 |
| fluxonium | 磁通子量子比特 | 特殊磁通量子比特，2009 |
| quantronium | 夸子比特/quantonium 量子比特 | CEA Saclay 命名，中译不统一时保留原文 |
| artificial atom | 人工原子 | 约瑟夫森结电路的类比 |
| Cooper pair | 库珀对 | 电荷直接观测对象 |
| electron pump | 电子泵 | Quantronics 组发明 |
| Ramsey fringes | Ramsey 条纹 | quantronium 相干性证据 |
| quantum limited amplifier | 量子极限放大器 | 2010，读出与传感 |
| quantum jumps | 量子跳变 | 2018 中断与逆转实验 |
| mesoscopic physics | 介观物理 | Collège de France 教席名目 |
| DEA | 深入研究文凭（法国学位） | 法国教育体制术语，勿直译「深奧」 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（科幻 / 史诗 / 上升）
- **风格**: 上升 / 电影 / 开创性成果
- **匹配理由**: 「上升」暗合从介观物理到量子技术的跃迁——人工原子一级级登上能级阶梯，最终把实验室电路送进量子计算机；科幻感匹配 Google Quantum AI 的工程前沿气质。
- **备选** (未采用): Expedition（探索感合适但更偏地理叙事）；Cinematic Experience（高潮张力强但已多批使用）。
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **时长**: 2:32 ≈ 152 秒 > 14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Michel_H._Devoret/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Michel_H._Devoret.yaml` | 研究领域 + 社会关系（已入库，只读） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
