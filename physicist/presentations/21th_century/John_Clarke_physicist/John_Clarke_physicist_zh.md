# 物理学家立传提示词（21 世纪批次：John Clarke）

> **本文件是 OpenPhysicist「物理学家立传提示词」的 John Clarke 专属实例**，按标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构撰写。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 事实基准唯一来源：本地 page.md（Wikipedia 全文），**page.md 无载的内容一律禁写**。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Clarke（约翰·克拉克），英国实验物理学家，2025 诺贝尔物理学奖得主（三人共享），超导电子学与 SQUID 测量科学大家。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达；实验物理学家强调**器件—测量—发现**的因果链，用「仪器之眼」作为贯穿视觉母题。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Clarke（1942-02-10 生于英格兰剑桥，在世）
- **气质关键词**：**超导电子学教父、磁通的超灵敏之眼、宏观量子现象的开启者** —— 2025 诺贝尔物理学奖获奖理由（官方原文，禁改写）：
  > "For the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit."（因发现电路中的宏观量子力学隧穿与能量量子化）
- **设计母题**：**仪器之眼（the instrument as an eye）**。SQUID 是对不可见磁通最灵敏的「眼睛」，把看不见的磁通变成可读的电压——视觉上用同心圆干涉环、低温冷雾与微弱磁通线贯穿全篇。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/John_Clarke_physicist/page.md`
- **第 0 步标注**：page.md 已有本地；**html 与 images/ 待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/John_Clarke_(physicist)`（注意消歧义后缀 `(physicist)`，目录名 `John_Clarke_physicist`）。
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步**：本提示词的第 4 步（研究领域表）与第 4.5 步（社会关系表）已由本批次完成入库（greatminds 库），立传时**只读勿改**，核对即可。

### 第 0 步：事实基准（page.md 已核对） 【人物专属】

- **生卒**：1942-02-10 生于剑桥（England），在世。
- **国籍**：英国（United Kingdom）。
- **父母/家庭**：page.md 无载，**禁写**。
- **教育**：The Perse School → Christ's College, Cambridge（Natural Sciences，B.A. Physics 1964）→ 1965 入新设 Darwin College（首批学生之一、学生协会首任主席）→ PhD 1968（剑桥 Royal Society Mond Laboratory）。
- **博士导师**：Brian Pippard（page.md frontmatter + infobox + 正文三处明载）；博士期间发明高灵敏伏特计 "SLUG"（Superconducting Low-inductance Undulatory Galvanometer）。
- **博士后**：UC Berkeley 博士后研究职位。
- **任职机构**：UC Berkeley 终身学术生涯——Assistant Professor 1969、Associate Professor 1971、Professor of Physics 1973–2010；1969 加入 Lawrence Berkeley National Laboratory（LBNL），2010 以 Materials Sciences Division faculty senior scientist 退休。
- **与剑桥的持续纽带**：1972 当选 Christ's College Fellow；1989 Clare Hall 访问 Fellow；1998 Churchill College by-fellow；1997 Christ's 荣誉 Fellow；2023 Darwin 荣誉 Fellow；2003 获剑桥 D.Sc.。
- **关键荣誉**：Alfred P. Sloan Fellowship 1970；Guggenheim Fellowship 1977；FRS 1986；Keithley Award 1998；Comstock Prize in Physics 1999；Hughes Medal 2004；NAS International Member 2012；American Philosophical Society Member 2017；Micius Quantum Prize 2021（与 Devoret、Nakamura 共享）；Nobel Prize in Physics 2025（与 Devoret、Martinis 共享）。
- **知名学生**：John M. Martinis（infobox Doctoral students 明载）。
- **核心贡献清单**：
  1. SQUID 的发明、研制与理论（dc SQUID 噪声与优化），超导电子学的奠基性推动；
  2. 1985 与 Martinis（博士生）、Devoret（博后）演示约瑟夫森结的量子行为：低温下宏观电子态在零电压态发生量子隧穿；
  3. 同年用微波脉冲证明约瑟夫森结能级量子化——电路量子电动力学（circuit QED）的首个证据，成为超导量子计算的基础；
  4. SQUID 量子噪声极限放大器应用于轴子（暗物质候选）搜索；
  5. microtesla 磁场 NMR 与 SQUID 磁共振成像。
- **关键时间线（15–20 节点）**：1942 生于剑桥 → Perse School → 1964 Christ's College B.A. → 1965 入 Darwin College（首批学生、学生协会首任主席）→ Pippard 门下研制 SLUG → 1968 PhD → 1969 赴 Berkeley（助理教授 + 加入 LBNL）→ 1971 副教授 → 1972 Christ's College Fellow → 1973 正教授 → 1977 Guggenheim → 1985 与 Martinis/Devoret 演示宏观量子隧穿与能级量子化 → 1986 当选 FRS → 1988 Science「宏观变量的量子力学」论文 → 1998 Keithley Award → 1999 Comstock Prize → 2003 剑桥 D.Sc. → 2004 Hughes Medal → 2010 从 Berkeley/LBNL 退休 → 2012 NAS 国际会员 → 2017 美国哲学学会 → 2021 Micius 量子奖 → 2025 诺贝尔物理学奖。

### 第 4 步：研究领域表（已入库，只读） 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | superconducting electronics | 超导电子学 | Girvin 称其为「教父」的领域 | 封面、核心页 |
| 1 | SQUID | 超导量子干涉器件 | 磁通超灵敏探测器，发明/理论/应用 | SQUID 页 |
| 2 | macroscopic quantum phenomena | 宏观量子现象 | 2025 诺奖核心：电路中的量子隧穿 | 核心页 |
| 3 | Josephson effect | 约瑟夫森效应 | 实验载体的物理基础 | 1985 实验页 |
| 4 | precision measurement | 精密测量 | SQUID 放大器、轴子搜索、微特斯拉 NMR/MRI | 应用页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致，已入库） 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Brian Pippard | 对方是导师 | 剑桥 Mond Laboratory 博士导师，1968 年获博士学位 |
| advisor-student | John M. Martinis | 对方是学生 | 博士生，1985 宏观量子隧穿实验合作者，2025 诺奖共享 |
| colleague | Michel H. Devoret | 无向 | 1982–84 在其 Berkeley 组做博士后，1985 合作演示量子隧穿与能级量子化 |
| influence | Brian Josephson | 无向 | 约瑟夫森效应预言者（1962），同为 Pippard 学生，Clarke 自述工作深受其影响 |
| co-honored | Michel H. Devoret | 无向 | 2025 诺贝尔物理学奖共享；2021 Micius 量子奖共享 |
| co-honored | John M. Martinis | 无向 | 2025 诺贝尔物理学奖共享 |
| co-honored | Yasunobu Nakamura | 无向 | 2021 Micius 量子奖共享（与 Devoret 三人） |

### 第 5 步：配色方案 【人物专属】

- **气质**：低温、精密、深海的静默与超导的纯粹
- **配色**：深海青（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 深海青 `#0F4C5C`（批内唯一）
  - `badgeA` 超导电子学 — 松绿 `#1E6B5A`
  - `badgeB` 宏观量子现象 — 靛蓝 `#4C5FD5`
  - `badgeC` 约瑟夫森效应 — 琥珀 `#E07B30`
  - `badgeD` 精密测量 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆），以同心圆干涉环呼应 SQUID 的磁通量子化干涉图样。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（肖像待下载，2025 年照片优先）。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（机构 = UC Berkeley）。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、国籍、出生地、教育（Perse/Christ's/Darwin/Mond Lab）、博士导师（Pippard）、任职（Berkeley 1969–2010 + LBNL）、主要荣誉（Nobel 2025/Hughes 2004/FRS 1986）、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 帧 + 共享首页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 超导电子学教父 / John Clarke 1942– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — SQUID / 宏观量子隧穿 / 能级量子化 / 轴子搜索
04  剑桥求学 (1942–1968) — Perse School、Christ's College、Darwin 首批学生、Pippard 门下、SLUG
05  Berkeley 五十年 (1969–2010) — 助理→正教授 1973、LBNL、与剑桥的持续纽带
06  SQUID：磁通的超灵敏之眼 — dc SQUID 噪声与优化；公式框放约瑟夫森方程 I = Ic·sin(φ) 与磁通量子 Φ0 = h/2e
07  1984–1985：宏观量子隧穿实验 — 与博士生 Martinis、博后 Devoret，零电压态隧穿
08  能量量子化：电路的原子的诞生 — 微波脉冲共振、能级量子化、circuit QED 首个证据
09  从电路到量子计算机 — 该实验成为超导量子计算的基础（DOE Office of Basic Energy Sciences 资助）
10  SQUID 的百般应用 — 轴子搜索、microtesla NMR (2002)、SQUID-MRI (2007)
11  荣誉与认可 — Nobel 2025 · Hughes 2004 · Comstock 1999 · Keithley 1998 · FRS 1986 · NAS 2012
12  遗产：超导电子学的教父 — Girvin 引语 + 三人组开启的量子时代
13  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

**版式要点**：实验类人物多用时间线与器件示意；公式框放约瑟夫森方程与磁通量子两个短式即可，勿塞长推导；1985 实验页可用「隧穿势垒 + 分立能级」概念图式（page.md 无公式推导，用概念图式并注明）。

**Clarke 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 同名区分 | Wikipedia 条目是 John Clarke (physicist)，与计算机科学家 Edmund M. Clarke 等无关；目录名 John_Clarke_physicist 即消歧义产物，勿混淆 |
| 获奖理由措辞 | 官方原文 "macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit"（英式 quantisation），禁改写、禁转述为「量子计算先驱」类说法 |
| 两个三人组勿混 | 2025 Nobel 三人 = Clarke + Devoret + Martinis；2021 Micius 三人 = Clarke + Devoret + Yasunobu Nakamura（**不含** Martinis） |
| 三人分工 | Clarke 是团队 PI；Martinis 当时是博士生、Devoret 是博士后，勿写成三人同等资历或并列导师 |
| Josephson 关系 | Brian Josephson 是 influence（Clarke 自述受其影响），且是 Pippard 的另一位学生——**不是** Clarke 的导师，勿写成师承 |
| SLUG 命名 | SLUG（Superconducting Low-inductance Undulatory Galvanometer）是 Clarke 博士期间自研自命名的器件，非他人命名 |
| 在世 | 1942 年生、在世，生卒页留白卒年；page.md 无配偶/子女记载，家庭禁写 |
| 获奖时机构 | 2025 获奖时身份是 UC Berkeley Professor Emeritus（已 2010 退休），勿写在职 |
| 引语归属 | "the godfather of superconducting electronics" 出自 Steven Girvin 对 Clarke 的评价，引用必须注明归属 Girvin |
| 学位年份 | B.A. 1964、PhD 1968；Darwin College 入学 1965；D.Sc. 2003——勿与荣誉 Fellow 年份（1997/2023）混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| SQUID | 超导量子干涉器件 | 勿写成「超导量子干涉仪」以外的生造名 |
| Josephson effect | 约瑟夫森效应 | 1962 预言，Josephson 后获 1973 诺奖 |
| macroscopic quantum tunnelling | 宏观量子隧穿 | 诺奖理由核心词，勿简写为「量子隧穿」 |
| energy quantisation | 能量量子化 | 英式 quantisation，勿改美式 |
| magnetic flux quantum | 磁通量子 | Φ0 = h/2e |
| superconductivity | 超导电性 | 基础概念 |
| phase qubit | 相位量子比特 | 1985 实验的电路形态 |
| circuit QED | 电路量子电动力学 | 1985 实验是首个证据 |
| axion | 轴子 | 暗物质候选，SQUID 放大器搜索对象 |
| SLUG | 超导低感波动检流计 | 博士期间发明，缩写展开勿错 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（纪录片 / 电影 / 稳重）
- **风格**: 稳重 / 纪录片 / 传记主线
- **匹配理由**: 「不可见光」暗合 SQUID 的本质——把不可见的磁通变成可读信号的眼睛；纪录片气质匹配 Berkeley 五十年的持久深耕与 2025 诺奖的迟来认可。
- **备选** (未采用): SEA（流动/平稳，但已多批使用）；The Flow of Time（时间感合适但受众略低）。
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **时长**: 2:34 ≈ 154 秒 > 14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/John_Clarke_physicist/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/John_Clarke_physicist.yaml` | 研究领域 + 社会关系（已入库，只读） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
