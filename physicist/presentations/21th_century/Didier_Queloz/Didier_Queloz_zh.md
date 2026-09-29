# 物理学家立传提示词（21 世纪批次：Didier Queloz）

> **本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」**，以 Didier Queloz（2019 诺贝尔物理学奖，首颗绕类太阳恒星系外行星的发现者）为实例。
> 结构对齐标杆 `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节同构）。标注 `【模板通用】` 部分可复用；`【人物专属】` 部分为本篇定制。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家标杆 Kenneth G. Wilson 提示词 + Beamer 成品骨架（`Eugene_Wigner_zh.tex` 一系）。
- **本实例**：Didier Patrick Queloz（迪迪埃·帕特里克·奎洛兹）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达——骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Didier Patrick Queloz（1966-02-23 生于瑞士，在世）
- **气质关键词**：**系外行星革命的点火者、多普勒光谱的大师、生命起源的追问者** —— 2019 诺贝尔物理学奖获奖理由（与 Michel Mayor 共享一半）：
  > "for the discovery of an exoplanet orbiting a solar-type star"（因发现绕太阳型恒星运行的系外行星）
  > 官方完整口径：该发现 "resulting in contributions to our understanding of the evolution of the universe and Earth's place in the cosmos"；另一半授予 Jim Peebles（宇宙学）。
- **设计母题**：**引力摇摆中的隐匿世界（the unseen companion）**。行星不可见，只从恒星视向速度的周期性微小摆动中被「听」出来——视觉语言用恒星光谱位移条纹与环绕轨道弧线呼应「看不见的伴侣」。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Didier_Queloz/page.md`（**已有本地**；`Didier_Queloz.html` 与 `images/` **待下载**，Wikipedia URL：https://en.wikipedia.org/wiki/Didier_Queloz ）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（`21st_century/Didier_Queloz/page.md`，含 frontmatter：QID Q124013 / 生 1966-02-23 / 国籍 Switzerland / 职业 astronomer, astrophysicist, university teacher / 博士导师 Michel Mayor / 教育 University of Geneva）
- 🔲 `Didier_Queloz.html` 与 `images/` 待下载（URL：https://en.wikipedia.org/wiki/Didier_Queloz ）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1966-02-23 生于瑞士（正文只写 Switzerland，未载具体城市），在世
  - 国籍：Switzerland（Swiss astronomer）
  - 教育：University of Geneva —— MSc 物理学 1990 → DEA 天文与天体物理 1992 → PhD 1995
  - 博士导师：Michel Mayor（frontmatter `doctoral_advisor` 明载）；博士论文 *Recherches liées à la spectroscopie par corrélation croisée numérique; (INTER-TACOS: guide de l'utilisateur)*（1995）
  - 任职：University of Geneva（1995 博士后至 2013 前后，2007 任 associate professor）；University of Cambridge（2013 起，Jacksonian Professor of Natural Philosophy、Trinity College fellow）；ETH Zurich（2021 起物理学教授、Centre for the Origin and Prevalence of Life 主任；导语称 2022 为该中心 founding director——两处并存按正文各忠于所在句）；另任 Cambridge Leverhulme Centre for Life in the Universe 主任
  - 关键荣誉：Nobel 2019（与 Mayor 共享一半，Peebles 另一半）；Wolf Prize in Physics 2017（个人）；BBVA Foundation Frontiers of Knowledge Award 2011（与 Mayor 共同）；Clarivate Citation Laureates 2013；Fellow of the Royal Society 2020；AeroSuisse Award 2020（与 CHEOPS 团队共享）；National Order of the Legion of Honour 2022；小行星 177415 Queloz 以其命名
  - 知名学生：page.md 仅一处提「With his Ph.D. student they demonstrated...」（未具名）——**学生不入库、不具名**
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1966 生于瑞士 → 1990 日内瓦 MSc 物理 → 1992 DEA 天文与天体物理 → 1995 博士（导师 Mayor）+ 与 Mayor 宣布发现 51 Pegasi b（ELODIE 摄谱仪，OHP）→ 1999 首颗凌星行星宣布 → 2000 CORALIE 装上瑞士 1.2m Leonhard Euler 望远镜；以 project scientist 身份主导 HARPS 研制 → 2000 首次光谱凌星（Rossiter–McLaughlin 效应）→ 2003 HARPS 投入使用；获教职；首测 OGLE 凌星行星整体密度；发现首颗凌星海王星尺寸行星 Gliese 436 b → 2007 任 associate professor；主导 WASP/CoRoT 光谱跟进 → COROT-7b 岩质密度首证 → HARPS-N 证认 Kepler-10 类地密度；NGTS 设计与帕拉纳尔建站 → 2011 BBVA 奖（与 Mayor）→ 2013 Clarivate Citation Laureates；移居 Cambridge → 2015 起 与 Liège 大学 M. Gillon 合作催生 TRAPPIST-1 → 2017 Wolf Prize → 2019 诺贝尔物理学奖（Nobel Lecture：*Exoplanets: 51 Pegasis b and all the others …*）→ 2020 FRS；AeroSuisse Award → 2021 移任 ETH Zurich 教授、任生命起源研究中心主任；Cambridge Leverhulme 中心主任 → 2022 Legion of Honour；导语称 2022 为 ETH 中心 founding director

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | exoplanets | 系外行星 | 1995 发现 51 Pegasi b，开创系外行星研究领域 | 核心页 |
| 1 | radial velocity | 视向速度法 | 多普勒光谱测星体摆动，行星探测主手段 | 核心页 |
| 2 | astronomical instrumentation | 天文仪器 | ELODIE/CORALIE/HARPS/HARPS-3 仪器链 | 仪器页 |
| 3 | planetary formation | 行星形成与演化 | 凌星+光谱联合测密度/自转-轨道夹角统计 | 演化页 |
| 4 | astrobiology | 天体生物学 | 宜居性、生命起源、abiogenesis zone | 晚期页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> **只收 page.md 明载的关系**；对手方 name_en 用库内规范形式（经查库内现无 Mayor/Peebles 记录，按 page.md frontmatter 姓名全形书写，后续批次按同名幂等复用）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michel Mayor | 师→生（博士导师） | 日内瓦大学博士导师，1995 同发现 51 Pegasi b |
| co-honored | Michel Mayor | 无向 | 2019 诺贝尔物理学奖共享一半；2011 BBVA Frontiers of Knowledge Award 共同得主 |
| co-honored | Jim Peebles | 无向 | 2019 诺贝尔物理学奖另一半得主（宇宙学） |
| colleague | M. Gillon | 无向 | Liège 大学合作者，TRAPPIST-1 探测合作 |
| colleague | S. Zucker | 无向 | Tel-Aviv 大学同事，凌星 pink noise 统计方法合作 |

- 入库操作：`MySQL/seed_person.py data/Didier_Queloz.yaml`（幂等；Duplicate entry 撞 uq_rel 属正常跳过）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深邃夜空、精密测量、革命性发现
- **配色**：日内瓦深蓝（天文观测）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeExo` 系外行星 — 深蓝 `#1B5E8C`（主色）
  - `badgeRV` 视向速度 — 青绿 `#0E7C7B`
  - `badgeInst` 天文仪器 — 琥珀 `#E07B30`
  - `badgeBio` 天体生物学 — 玫瑰 `#C4204F`
- **背景母题**：稀疏大块实心圆（恒星）+ 细弧线（轨道），四种大小错落，呼应「看不见的行星拖动恒星摇摆」

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 系外行星革命点火者 / Didier Queloz 1966– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 51 Pegasi b / 视向速度技术 / 仪器链 / 生命起源
04  早年与教育：日内瓦 (1966–1995) — MSc 1990、DEA 1992、博士论文 INTER-TACOS
05  1995：51 Pegasi b 的发现（核心贡献页）— ELODIE 摄谱仪、Hot Jupiter、视向速度周期摆动
06  仪器时代：ELODIE → CORALIE → HARPS (1995–2003) — Euler 望远镜、ESO 3.6m
07  恒星活动噪声的甄别 — proxies、标准实践方法奠基
08  光谱凌星与自转-轨道夹角 — Rossiter–McLaughlin、WASP 合作、misaligned/retrograde
09  密度与行星结构 — OGLE、Gliese 436 b、COROT-7b、Kepler-10、pink noise 统计
10  剑桥时期与生命起源 (2013–) — TRAPPIST-1、abiogenesis zone、CHEOPS/SPECULOOS/Terra Hunting
11  荣誉与认可 — Nobel 2019 · Wolf 2017 · BBVA 2011 · FRS 2020 · Legion of Honour 2022
12  遗产：25000+ 系外行星时代的开端
13  结尾
```

- 公式框建议：视向速度多普勒摆动 `Δλ/λ = v_r/c`（或周期性 radial-velocity 曲线概念图式；page.md 无公式，注明为概念图式）

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 2019 一半 = Mayor + Queloz（系外行星发现），另一半 = Jim Peebles（宇宙学）；理由句只写 "for the discovery of an exoplanet orbiting a solar-type star"，勿把 Peebles 与该理由混排 |
| 「首颗」限定 | 是**首颗绕类太阳（主序）恒星的系外行星**；脉冲星行星（1992）在先，勿写成「首颗系外行星」 |
| Wolf 2017 | page.md 写 he received（个人获奖，未载共享）；勿写成与 Mayor 共享 |
| BBVA 2011 | 明载 co-winner with Mayor，可写共享 |
| 身份表述 | 他是 Swiss **astronomer**（infobox Fields: Astronomy），叙述以天文学家/天体物理学家为主，勿通篇写成"理论物理学家" |
| ETH 中心年份 | 2021 移任 ETH 并成为中心主任 vs 导语 2022 founding director——各忠于所在句，勿强行统一 |
| 学生 | page.md 未具名任何博士生，**禁止编造学生名单**（"his Ph.D. student" 一处不具名不入库） |
| 无载禁写 | 出生地具体城市、家庭/父母/配偶/子女、日内瓦之外早期经历——page.md 均无载 |
| 引语红线 | 唯一可引语为 The Daily Telegraph 转述 "Science inherited a lot from religions"（注明转述来源）；不得杜撰诺奖演讲引语 |
| 同名区分 | Michel Mayor（导师，2019 共同得主）勿与 Jim Peebles 混；小行星 177415 Queloz 与人名区分 |
| 51 Pegasi b 命名 | 行星名 51 Pegasi b（b 小写），恒星名 51 Pegasi；诺奖演讲标题原文拼作 "51 Pegasis b"（照原文引，勿"纠正"） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| exoplanet | 系外行星 | 非"太阳系外行星"泛称，强调绕其他恒星 |
| Hot Jupiter | 热木星 | 51 Pegasi b 类型，勿写成"巨气体行星"泛称 |
| radial velocity | 视向速度 | 多普勒法的测量量 |
| Doppler spectroscopy | 多普勒光谱法 | 与 transit 法区分 |
| Rossiter–McLaughlin effect | 罗西特–麦克劳克林效应 | 光谱凌星测自转-轨道夹角 |
| transit | 凌星 | 测半径，与 RV 互补 |
| spectrograph (ELODIE/CORALIE/HARPS) | 摄谱仪 | 仪器链谱系勿混年份 |
| spin–orbit misalignment | 自转-轨道失准 | 含 retrograde 逆行轨道 |
| pink noise | 粉红噪声 | 凌星残差系统学度量 |
| abiogenesis zone | 无生源区 | 生命前体化学最低条件概念 |
| ultra-cool dwarf | 超冷矮星 | SPECULOOS 目标天体 |
| Jacksonian Professor of Natural Philosophy | 杰克逊自然哲学讲席教授 | 剑桥讲席名，勿意译为"哲学教授" |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（66k views，探索/史诗）
- **匹配理由**: "探索/远征" 完美匹配系外行星搜寻的叙事——从日内瓦实验室到 OHP/拉西亚/帕拉纳尔观测站，再到 CHEOPS 太空任务，是一场持续 30 年的星际远征；"史诗" 匹配 1995 发现作为天文学范式转折的分量。
- **备选** (未采用): Awaken（明亮/突破，稍轻）、SEA（流动/平稳，缺探索感）。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 复制为 `presentations/21th_century/Didier_Queloz/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Didier_Queloz/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` + `MySQL/data/Didier_Queloz.yaml` | 领域+社会关系入库（第 4/4.5 步） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
