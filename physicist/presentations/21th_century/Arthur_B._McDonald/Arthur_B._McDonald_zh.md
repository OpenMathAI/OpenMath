# 物理学家立传提示词（Arthur B. McDonald 阿瑟·麦克唐纳）

> **OpenPhysicist 21 世纪批次 · 人物专属立传提示词**。
> 目标人物：Arthur Bruce McDonald（1943-08-29 ~ 在世），2015 诺贝尔物理学奖得主（SNO 太阳中微子振荡）。
> 执行方式：复制本文件到新对话中，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Arthur Bruce McDonald（阿瑟·布鲁斯·麦克唐纳），加拿大天体物理学家，萨德伯里中微子观测站（SNO）长期领导者，重水探测器直接证实太阳中微子振荡。
- **设计哲学**：物理学家立传必须有「身份信息页」，且强调「研究领域」的结构化表达。McDonald 篇的叙事核心是「两公里岩层下的重水天平」——用 1000 吨重水同时测全部味与电子味的通量之差，把太阳中微子问题变成振荡的直接证据。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Arthur Bruce McDonald（1943-08-29 生于加拿大新斯科舍省悉尼，在世）
- **气质关键词**：**重水探测的掌舵人、太阳中微子问题的终结者、深地天体物理的奠基者** —— 2015 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for the discovery of neutrino oscillations, which shows that neutrinos have mass"（发现中微子振荡，表明中微子具有质量）
- **设计母题**：**重水之球（heavy water sphere）**。SNO 的 12 米丙烯酸球与 1000 吨重水悬于 2100 米井下——视觉语言可用深蓝底色中央一颗透明球体，内外两层光环分别代表「全味」与「电子味」两条测量通道。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Arthur_B._McDonald/page.md`
- **第 0 步状态**：page.md 已有本地；`Arthur_B._McDonald.html` 与 `images/` 待下载，Wikipedia URL：`https://en.wikipedia.org/wiki/Arthur_B._McDonald`
- **参考模板**：
  - 物理学家成品骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对 page.md，建 Beamer 前须再对照原文）

- 生卒：1943-08-29 生于新斯科舍省悉尼，在世
- 国籍：加拿大
- 教育：达尔豪西大学物理学 B.Sc. 1964、M.Sc. 1965；加州理工学院 Ph.D. 1969；中学：Sydney Academy
- 博士导师：infobox 明载 Charles A. Barnes（★ frontmatter/wikidata 作 William Alfred Fowler，口径冲突见陷阱表）；博士论文《Excitation energies and decay properties of T = 3/2 states in 17O, 17F and 21Na》（infobox 标注 1970）
- 任职：Chalk River 核实验室研究员 1969–1982；普林斯顿大学物理教授 1982–1989；皇后大学教授 1989–2013（2013 荣休教授）；Gordon and Patricia Gray 粒子天体物理讲席教授 2006–2013；SNO 合作组领导人（自 1989）
- 访问职位：CERN（1988？列于 Queen's 1988；2003、2004、2009）、华盛顿大学 1978、洛斯阿拉莫斯 1981、夏威夷大学 2004/2009、牛津大学 2003/2009
- 关键荣誉：APS Fellow 1983；Killam Research Fellowship 1998；Herzberg 加拿大金质奖章 2003；Bruno Pontecorvo Prize 2005；加拿大勋章 Officer 2006 → Companion 2015；Benjamin Franklin Medal 2007（与 Yoji Totsuka 共享）；英国皇家学会 FRS 2009；加拿大科学与工程名人堂 2009；Killam Prize 2010；Tory Medal 2011；Cocconi Prize 2011（与 Yoichiro Suzuki 共享）；安大略勋章 2012；Nobel 2015（与 Kajita 共享）；小行星 229781 Arthurmcdonald 2016；Breakthrough Prize 2016（与 SNO 合作组共享）；美国 NAS 外籍院士 2016；新斯科舍勋章 2016
- 核心贡献清单：
  1. 领导 SNO 用 1000 吨重水同时灵敏于「全部味」与「仅电子味」两类反应，直接测量中微子振荡
  2. 2001 年 8 月 SNO 报告太阳电子中微子在途中振荡为 μ/τ 中微子的直接证据
  3. 与 Super-K 的 Kajita 工作共同解决太阳中微子问题、证明中微子有质量
  4. 1984 与 Herb Chen 等人共同创立 SNO 合作组（Chen 提出重水探测器构想，1987-11 因白血病去世）
  5. SNOLAB 暗物质研究（SNO+、DEAP-3600、DarkSide-20k）
  6. 2020 COVID 期间领导加拿大团队低成本量产机械呼吸机（MVM 项目）
- 关键时间线（15–20 节点）：1943 出生悉尼 → Sydney Academy → 1964/1965 达尔豪西学士/硕士 → 1969 Caltech 博士 → 1969 Chalk River 研究员 → 1983 APS Fellow → 1984 SNO 合作组创立 → 1989 回加拿大接掌 SNO + 皇后大学教授 → 1998 Killam Fellowship → 2001-08 SNO 振荡证据发布 → 2003 Herzberg 金奖 → 2005 Pontecorvo 奖 → 2006 加拿大勋章 Officer + Gray 讲席 → 2007 Franklin Medal（与 Totsuka）→ 2009 FRS → 2010 Killam Prize → 2011 Tory Medal + Cocconi Prize → 2012 安大略勋章 → 2013 荣休 → 2015 诺贝尔奖 + Companion → 2016 Breakthrough/NAS/小行星命名 → 2018 McDonald 研究所冠名 → 2020 呼吸机项目
- 其他：2018 加拿大粒子天体物理研究中心冠名为 Arthur B. McDonald Canadian Astroparticle Physics Research Institute；皇后大学名誉教授

### 第 4 步：研究领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | astrophysics | 天体物理学 | infobox Fields 明载 | 身份页 |
| 1 | neutrino physics | 中微子物理 | SNO 毕生主战场 | 核心页 |
| 2 | neutrino oscillations | 中微子振荡 | 2001 SNO 直接证据，2015 诺奖核心 | 核心页 |
| 3 | dark matter | 暗物质 | SNOLAB：DEAP-3600、DarkSide-20k | 遗产页 |
| 4 | particle astrophysics | 粒子天体物理 | McDonald 研究所冠名领域 | 机构页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Charles A. Barnes | 导师 | Caltech 博士导师（infobox 明载；frontmatter 作 W. A. Fowler，口径冲突见陷阱表） |
| co-honored | Takaaki Kajita | 无向 | 2015 诺贝尔物理学奖共同得主，Super-K 大气中微子 |
| co-honored | Yoji Totsuka | 无向 | 2007 本杰明·富兰克林奖章共享，Super-K 领导者 |
| co-honored | Yoichiro Suzuki | 无向 | 2011 欧洲物理学会 Cocconi Prize 共同得主 |
| colleague | Herb Chen | 无向 | 加州大学尔湾分校合作者，1984 提出重水探测器构想、SNO 合作组共同创始人 |
| colleague | Cristiano Galbiati | 无向 | 普林斯顿教授，2020 MVM 呼吸机项目发起人、DarkSide-20k 合作 |

> 注：1984 SNO 创始名单中的 George Ewan、David Sinclair 为 page.md 明载合作组共同创始人，但无个人化互动叙述，暂不入库（防噪声）；配偶 page.md 无载。

### 第 5 步：配色方案 【人物专属】

- **气质**：深蓝、克制、地下深处的恒心
- **配色**：深水蓝绿（主色，呼应重水与深地实验室）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 主色 — 深水蓝绿 `#175E73`（批内不重复）
  - `badgeSNO` SNO — 青蓝 `#1E88C7`
  - `badgeOsc` 中微子振荡 — 靛蓝 `#2B4C9B`
  - `badgeDM` 暗物质 — 紫黑 `#46356B`
  - `badgeAstro` 粒子天体物理 — 琥珀 `#E07B30`
- **背景母题**：深蓝底色中央一颗透明重水球，球外两层同心光环（全味/电子味）

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 重水天平的掌舵人 / Arthur B. McDonald 1943– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — SNO 重水探测器 / 太阳中微子振荡直接证据 / 暗物质 / 呼吸机项目
04  新斯科舍与 Caltech (1943–1969) — 达尔豪西、Chalk River 前夜、博士论文
05  Chalk River 与普林斯顿 (1969–1989) — 核实验室研究员二十年、1982 转普林斯顿
06  重水构想与 SNO 创立 (1984) — Herb Chen 提议、16 人合作组、1987 Chen 早逝
07  突破：SNO 直接证据 (2001)（核心贡献页）— 全味 vs 电子味、振荡定案（公式框：两条反应通道对比概念图式，page.md 无具体公式须注明）
08  太阳中微子问题的终结 — 与 Kajita 的 Super-K 互证、中微子有质量
09  荣誉与认可 — Nobel 2015 · Herzberg 2003 · Franklin 2007 · Tory 2011 · Companion
10  SNOLAB 与暗物质 — SNO+、DEAP-3600、DarkSide-20k
11  冠名与传承 — 2018 McDonald 研究所、皇后大学荣休教授
12  人道主义：MVM 呼吸机 (2020) — Galbiati 发起、加拿大团队、CERN 开源硬件许可
13  遗产：加拿大粒子天体物理的黄金时代
14  结尾
```

### 第 7–8 步：版式要点 + McDonald 专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 博士导师口径冲突 | infobox 明载 Charles A. Barnes，frontmatter/wikidata 作 William Alfred Fowler——入库以 infobox 为准（Barnes），提示词与 Review 须保留冲突注记，禁自行改写为 Fowler |
| 学位年份 | 正文作 Ph.D. 1969，infobox 论文条目标注 1970——两处口径并存，写「1969 年获博士学位（论文条目标注 1970）」或取 1969 并加注 |
| 获奖理由措辞 | 官方原文与 Kajita 相同 "for the discovery of neutrino oscillations, which shows that neutrinos have mass"；两人共享各半 |
| SNO 领导起点 | McDonald 自 1989 年领导 SNO；1984 年是合作组创立（Chen 构想），勿把创立年写成领导起点 |
| Chen 早逝 | Herb Chen 1987-11 因白血病去世，未能见证 2001 结果——叙事页可用，勿写成共同领奖 |
| 集体奖项 | 2016 Breakthrough Prize 是「与 SNO 合作组共享」，非个人独得；Franklin Medal 2007 与 Totsuka 共享、Cocconi Prize 2011 与 Suzuki 共享，逐条注明 |
| 出生地 | 悉尼（Sydney, Nova Scotia）是加拿大城镇，勿与澳大利亚悉尼混淆 |
| 无载禁写 | 配偶/子女 page.md 无载；「诺奖之后的活动」只写 page.md 明载的 SNOLAB/SNO+/DEAP-3600/DarkSide-20k 与 2020 呼吸机项目 |
| 机构区分 | Chalk River Nuclear Laboratories（研究）≠ CNL Chalk River（2020 呼吸机参与方口径），同一地点不同时期表述 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Sudbury Neutrino Observatory (SNO) | 萨德伯里中微子观测站 | 安大略省萨德伯里 |
| heavy water | 重水 | D₂O，1000 吨 |
| charged current | 带电电流反应 | 仅电子味灵敏 |
| neutral current | 中性电流反应 | 全味灵敏 |
| electron neutrino | 电子中微子 | 太阳中微子主要成分 |
| neutrino oscillation | 中微子振荡 | 与 Kajita 共享诺奖的发现 |
| SNOLAB | SNOLAB 地下实验室 | SNO 扩建 |
| dark matter | 暗物质 | DEAP-3600/DarkSide-20k |
| ventilator | 机械呼吸机 | 2020 MVM 项目 |
| asteroid naming | 小行星命名 | 229781 Arthurmcdonald |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（66k views，探索/史诗）
- **匹配理由**：
  - 「探索/史诗」匹配深地实验的远征感——从 Chalk River 到 2100 米井下重水球
  - 「远征式叙事」匹配 SNO 十六年的长跑：构想→创立→掌舵→2001 定案
- **备选**（未采用）：The Invisible Light（留给同批 Kajita）、Eternals（留给同批 Thouless）
- **本地路径**：`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`
- **时长**：约 3 分 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐
