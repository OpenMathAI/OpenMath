# 物理学家立传提示词（21 世纪批次：Reinhard Genzel）

> **本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」**，以 Reinhard Genzel（2020 诺贝尔物理学奖，银河系中心超大质量致密天体的发现者）为实例。
> 结构对齐标杆 `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。标注 `【模板通用】` 部分可复用；`【人物专属】` 部分为本篇定制。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家标杆 Kenneth G. Wilson 提示词 + Beamer 成品骨架（`Eugene_Wigner_zh.tex` 一系）。
- **本实例**：Reinhard Genzel（赖因哈德·根策尔，ForMemRS）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达——骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Reinhard Genzel（1952-03-24 生于西德巴特洪堡，在世）
- **气质关键词**：**银河中心的凝视者、红外与亚毫米波的大师、三十年黑洞追踪者** —— 2020 诺贝尔物理学奖获奖理由（与 Andrea Ghez 共享一半）：
  > "for the discovery of a supermassive compact object at the centre of our galaxy"（因发现我们银河系中心的超大质量致密天体）
  > 另一半授予 Roger Penrose（黑洞形成是 GR 稳健预言），理由句不同，勿混排。
- **设计母题**：**穿透尘埃的红外之眼（seeing through the dust）**。银心被尘埃遮挡、肉眼不可见——Genzel 用红外/亚毫米波 instruments 三十年追踪 S 簇恒星轨道，把不可见之物逼入证据。视觉语言用尘埃带中的一束红外光束与收敛的椭圆轨道呼应。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Reinhard_Genzel/page.md`（**已有本地**；`Reinhard_Genzel.html` 与 `images/` **待下载**，Wikipedia URL：https://en.wikipedia.org/wiki/Reinhard_Genzel ）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（`21st_century/Reinhard_Genzel/page.md`，含 frontmatter：QID Q65807 / 生 1952-03-24 / 国籍 Germany / 职业 astronomer, astrophysicist, university teacher, scientist / 教育 Freiburg、Bonn）
- 🔲 `Reinhard_Genzel.html` 与 `images/` 待下载（URL：https://en.wikipedia.org/wiki/Reinhard_Genzel ）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1952-03-24 生于 Bad Homburg vor der Höhe（时属西德），在世
  - 国籍：Germany（German astrophysicist）
  - 家庭：父 Ludwig Genzel（固体物理学家，1922–2003）；母 Eva-Maria Genzel（正文仅载姓名）；2021 年回忆访谈中提及父亲影响与与 Townes 共事经历
  - 教育：Berthold-Gymnasium Freiburg → University of Freiburg（BSc 物理）→ University of Bonn（MSc、1978 PhD 射电天文，在马普射电天文研究所完成）
  - 博士导师：Peter Georg Mezger（infobox 明载；注意 frontmatter doctoral_advisor 为 QID Q60197342 的数据噪声，以 infobox 姓名为准）；博士论文 *Beobachtung von H2O-Masern in Gebieten von OB-Sternentstehung*（1978）
  - 任职（含年份）：Harvard-Smithsonian Center for Astrophysics（1978 起）；Miller Fellow 1980–82；UC Berkeley 物理系 1981 起副教授→正教授；1986 转任马普地外物理研究所（MPE, Garching）所长、马普学会科学成员；LMU Munich 1988 起荣誉教授；1999–2016 兼任 Berkeley 全职教授（part-time joint appointment）
  - 关键荣誉（时间序）：Studienstiftung 1973–75；Otto Hahn Medal 1980；NSF Presidential Young Investigator Award 1984；APS Fellow 1985；Newton Lacy Pierce Prize 1986（AAS）；Leibniz Prize 1990；法国科学院外籍院士 1998；De Vaucouleurs Medal 2000；Prix Jules Janssen 2000；NAS 外籍院士 2000；Leopoldina 2002；Stern–Gerlach Medal 2003；Balzan Prize（红外天文）2003；Albert Einstein Medal 2007；Shaw Prize 2008；Karl Schwarzschild Medal 2011；Crafoord Prize 2012；Tycho Brahe Prize 2012；ForMemRS 2012；Pour le Mérite 2013；Harvey Prize 2014；Herschel Medal 2014；**Nobel Prize in Physics 2020**；Pontifical Academy 2020；Bavarian Maximilian Order 2021；荣誉博士：Leiden 2010、巴黎 2014、Grenoble Alpes 2023；智利大学校长奖章 2025；巴伐利亚宪法勋章 2025
  - 知名学生：page.md 未具名——**学生不入库**
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1952 生于 Bad Homburg → Freiburg 物理 BSc → Bonn MSc → 1978 博士（射电天文，H2O maser，Mezger 指导）→ 1978–80 CfA（Harvard & Smithsonian）→ 1980–82 Miller Fellow；Otto Hahn Medal → 1981 起 Berkeley 教职 → 1984 NSF PYI → 1985 APS Fellow → 1986 Pierce Prize；转任 MPE 所长 → 1988 LMU 荣誉教授 → 1990 Leibniz Prize → 1998 法国科学院外籍院士 → 1999–2016 Berkeley 兼任教授 → 银心 S 簇恒星轨道长期追踪计划（Sgr A*）→ 2000 双奖（De Vaucouleurs/Janssen）+ NAS 外籍院士 → 2003 Stern–Gerlach + Balzan → 2007 爱因斯坦奖章 → 2008 Shaw Prize → 2011 Schwarzschild Medal → 2012 Crafoord + Tycho Brahe + ForMemRS → 2013 Pour le Mérite → 2014 Harvey + Herschel Medal → 2018-07 S2 近心点观测（7,650 km/s ≈ 2.55% c，约 120 AU ≈ 1400 Schwarzschild 半径），GR 红移再获确证 → 2020 诺贝尔物理学奖（与 Ghez 共享一半；Pontifical Academy）→ 2021 Bavarian Maximilian Order → 2023 Grenoble 荣誉博士 → 2025 智利大学校长奖章 + 巴伐利亚宪法勋章

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | infrared astronomy | 红外天文 | 银心观测主手段，穿透尘埃 | 核心页 |
| 1 | submillimetre astronomy | 亚毫米波天文 | 冷气体/恒星形成研究 | 仪器页 |
| 2 | astrophysics | 天体物理 | infobox Fields 主口径 | 总览页 |
| 3 | black holes | 黑洞 | Sgr A* 超大质量致密天体，2020 诺奖核心 | 核心页 |
| 4 | galaxy formation and evolution | 星系形成与演化 | 正文明载研究方向 | 演化页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> **只收 page.md 明载的关系**；对手方 name_en 用库内规范形式（Townes 沿用库内 `Charles Hard Townes`(id=2477)；Mezger/Ludwig Genzel 新建 stub，用 infobox/正文全形）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Peter Georg Mezger | 师→生（博士导师） | 波恩大学博士导师（马普射电天文研究所），射电天文，1978 H2O maser 论文 |
| colleague | Charles Hard Townes | 无向 | UC Berkeley 共事者（2021 访谈自述共事经历），1964 诺贝尔物理学奖得主 |
| parent-child | Ludwig Genzel | 无向 | 父亲，固体物理学家（1922–2003） |
| co-honored | Andrea Ghez | 无向 | 2020 诺贝尔物理学奖共享一半 |
| co-honored | Roger Penrose | 无向 | 2020 诺贝尔物理学奖另一半得主 |

- 入库操作：`MySQL/seed_person.py data/Reinhard_Genzel.yaml`（幂等；Duplicate entry 撞 uq_rel 属正常跳过）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深邃、隐匿、穿透尘埃的执着
- **配色**：红外深红（不可见波段）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeIR` 红外天文 — 红外深红 `#8C2F1B`（主色）
  - `badgeSubmm` 亚毫米波 — 暗橙 `#B45A2B`
  - `badgeBH` 黑洞 — 靛黑蓝 `#1C2B4A`
  - `badgeGalaxy` 星系演化 — 青绿 `#0E7C7B`
- **背景母题**：深空底色上稀疏散布的星点 + 一束楔形红外光锥扫过尘埃带，呼应「穿透尘埃看见银心」

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 银河中心的凝视者 / Reinhard Genzel 1952– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — Sgr A* 黑洞 / S2 轨道 GR 检验 / 红外亚毫米仪器 / 星系演化
04  早年与教育：从巴特洪堡到波恩 (1952–1978) — 物理学家之父、Freiburg、Bonn 射电天文博士
05  博士岁月：H2O maser 与 Mezger (1978) — 马普射电天文研究所、OB 星形成区
06  跨越大西洋：CfA 与 Berkeley (1978–1986) — Miller Fellow、1981 教职、Pierce Prize
07  执掌 MPE：马普地外物理研究所 (1986–) — Garching、LMU 荣誉教授、仪器研制
08  银心三十年：追踪 S 簇恒星（核心贡献页）— Sgr A*、开普勒轨道、超大质量黑洞证据链
09  2018：S2 的相对论时刻 — 7,650 km/s、120 AU ≈ 1400 Schwarzschild 半径、GR 红移检验
10  星系的形成与演化 — 冷气体、亚毫米波巡天
11  荣誉与认可 — Nobel 2020 · Shaw 2008 · Crafoord 2012 · Balzan 2003 · Pour le Mérite 2013
12  遗产：从猜想到银心成像时代
13  结尾
```

- 公式框建议：S2 轨道的开普勒/相对论红移概念式 `z ≈ GM/(rc²)`（或近心点轨道示意；page.md 无显式公式，注明为概念图式）

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 2020 一半 = Genzel + Ghez（银心超大质量致密天体），另一半 = Penrose（黑洞形成 GR 预言）；理由句逐字用 "for the discovery of a supermassive compact object at the centre of our galaxy"，勿写成"发现黑洞" |
| 博士导师噪声 | frontmatter `doctoral_advisor: ["Q60197342"]` 是 QID 数据噪声；以 infobox 姓名 **Peter Georg Mezger** 为准入库 |
| 身份表述 | German **astrophysicist / astronomer**（infobox Fields: Astrophysics）；勿写成"理论物理学家" |
| Townes | 是 Berkeley 共事者（正文 2021 访谈明载 "experiences working with"），**不是导师**——用 colleague 入库，勿升格师承 |
| 父亲 | Ludwig Genzel 是固体物理学家（1922–2003），2021 访谈提及影响——入 parent-child；母 Eva-Maria 仅姓名无细节，note 勿编 |
| 任职口径 | 1986「离开 Berkeley」转任 MPE 所长，但 1999–2016 又兼任 Berkeley 全职教授——两段分开写，勿写成"1986 后仍在 Berkeley 常任" |
| S2 数据 | 7,650 km/s ≈ 2.55% 光速；近心点 2018-05 约 120 AU ≈ 1400 Schwarzschild 半径——三组数字勿混写 |
| 无载禁写 | 具体学生名单（未具名）、配偶/子女、出生城市细节外的家庭信息、诺奖演讲引语——page.md 无载即不写 |
| 引语红线 | page.md 正文**无任何直接引语**（2021 访谈只述及主题），全篇禁引语、禁转述"原话" |
| 同奖不同年 | Karl Schwarzschild Medal：Genzel 2011、Penrose 2000——各忠于本人页面 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| infrared astronomy | 红外天文 | 穿透尘埃观测银心的主手段 |
| submillimetre astronomy | 亚毫米波天文 | 冷气体/恒星形成 |
| Sagittarius A* | 人马座 A* | 银心致密天体，写法带星号 |
| supermassive compact object | 超大质量致密天体 | 诺奖理由原句用词，勿直接改写为 black hole |
| S2 (star) | S2 星 | 绕 Sgr A* 的恒星，勿与"二号源"混 |
| pericentre | 近心点 | 2018 年 5 月通过 |
| Schwarzschild radius | 史瓦西半径 | 120 AU ≈ 1400 倍 |
| gravitational redshift | 引力红移 | GR 检验观测量 |
| H2O maser | 水微波激射源 | 博士论文主题 |
| Otto Hahn Medal | 奥托·哈恩奖章 | 马普学会青年奖，非诺贝尔系 |
| Pour le Mérite | 功勋勋章 | 普鲁士/德国科学艺术最高勋章 |
| Crafoord Prize | 克拉福德奖 | 瑞典皇家科学院，天文诺奖补位奖 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（3:07，史诗/黑暗/推进）
- **匹配理由**: "黑暗/推进" 完美匹配银心观测叙事——尘埃与不可见性是 Genzel 三十年研究的对手，红外之眼在黑暗中层层推进，2018 年 S2 近心点是黑暗中的高潮时刻；"史诗" 匹配 MPE 团队工程化观测的规模感。
- **备选** (未采用): The Invisible Light（纪录片/稳重，同样贴题但留给别篇）、Last Hope（戏剧性更强，留给 Ghez 篇备选）。
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → 复制为 `presentations/21th_century/Reinhard_Genzel/ThroughTheDarkness.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Reinhard_Genzel/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` + `MySQL/data/Reinhard_Genzel.yaml` | 领域+社会关系入库（第 4/4.5 步） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
