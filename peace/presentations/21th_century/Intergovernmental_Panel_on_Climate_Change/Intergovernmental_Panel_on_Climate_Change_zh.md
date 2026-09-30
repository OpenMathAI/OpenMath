# OpenPeace 机构立传提示词（本实例：Intergovernmental Panel on Climate Change 政府间气候变化专门委员会）

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与 OpenPeace 20 世纪 104 位得主批次的实战经验。
- **本实例**：Intergovernmental Panel on Climate Change（IPCC，政府间气候变化专门委员会）—— 1988 年由 WMO 与 UNEP 共同设立的联合国政府间科学机构，2007 年诺贝尔和平奖得主（与 Al Gore 共享），**政府间组织机构篇**。
- **设计哲学**：机构立传以「设立 → 运作方式 → 评估报告谱系 → 认可与争议」替代个人生平；以**机构概览页**替代身份信息页；「不做原创研究、只做评估」的独特定位与六次评估报告的演进，构成骨架，务必保留。

---

## 二、背景信息 【机构专属】

- **机构全称**：Intergovernmental Panel on Climate Change（IPCC），1988 年由世界气象组织（WMO）与联合国环境规划署（UNEP）共同设立，同年获联合国背书；秘书处设日内瓦，由 WMO 托管；195 个成员国。
- **获奖**：2007 年诺贝尔和平奖，与前美国副总统 Al Gore 共享同一理由句。
- **官方获奖理由 EN**（Nobel 官方原文，照抄勿改写）：
  > "for their efforts to build up and disseminate greater knowledge about man-made climate change, and to lay the foundations for the measures that are needed to counteract such change"
- **官方获奖理由中译**（照抄名录 `OpenPeace_21st_Century_Nobel_Laureates.md`，禁止改写）：表彰他们为积累与传播人为气候变化的知识、并为应对此类变化所需的措施奠定基础所做的努力。
- **气质关键词**：**气候科学的评估中枢、最大规模的同行评议、科学政策的翻译者**。
- **设计母题**：**大气层的同心圈层（atmospheric circles）**——地球大气分层弧线 + 报告谱系的时间刻度，呼应「把万千论文凝练成给决策者的一页」的机构使命；背景沿用柔和气泡母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Intergovernmental_Panel_on_Climate_Change/page.md`（Wikipedia 全文 + frontmatter，事实基准以此为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「使命领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【机构专属，已核对 page.md】

- **机构性质**：联合国体系内的政府间科学机构；使命是「向各级政府提供可用于制定气候政策的科学信息」；**不做原创研究**，只评估同行评议文献；被专家称为科学界规模最大的同行评议过程；是全球三个科学—政策评估机构中的第一个（后继者 IPBES 2012、ISPCWP 2025）。
- **设立**：1988 年由 WMO 与 UNEP 共同设立；前身为 1986 年三家机构（ICSU/UNEP/WMO）设立的温室气体咨询组（AGGG）；美国环保署寻求国际公约、里根政府担忧独立科学家影响过大，促成政府间形态；1988 年联合国大会决议背书。
- **治理结构**：Panel（全会，约一年两次，批准报告与预算）→ Chair + Bureau（34 人）→ 三个工作组（WG I 物理科学 / WG II 影响与适应 / WG III 减缓）+ 国家温室气体清单任务组（TFI）+ 执行委员会 + 秘书处；工作组联席主席由发达国家与发展中国家各一名担任。
- **报告背书三级**：Approval（逐行批准）/ Adoption（逐节通过）/ Acceptance（整体接受）。
- **经费**：1989 年设立信托基金，成员国自愿捐款；2021 年约 600 万欧元、2022 年约 800 万欧元；WMO 承担秘书处运行费用。
- **历任主席（5 位）**：Bert Bolin（1988 当选，首任）→ Robert Watson（1997）→ Rajendra K. Pachauri（2002）→ Hoesung Lee（2015）→ Jim Skea（2023-07-28，英国能源科学家，现任）。
- **关键荣誉**：Nobel Peace Prize 2007（12 月领取，与 Al Gore 共享）；Gulbenkian Prize for Humanity 2022（与 IPBES 共享）。
- **评估报告谱系（6 次评估 + 特别报告）**：
  1. FAR（1990）：温室气体因人类活动增加导致增温的确证，直接催生 UNFCCC
  2. SAR（1995）：「可辨识的人类影响」，为《京都议定书》谈判提供素材
  3. TAR（2001）：过去 50 年增温主要源于人类活动；「曲棍球杆」曲线成为标志图像
  4. AR4（2007）：「气候系统变暖是毋庸置疑的（unequivocal）」；诺奖当年出版
  5. AR5（2013/2014）：人类影响清晰；成为 2015 年《巴黎协定》的科学基础
  6. AR6（2021–2023）：WG I（2021-08，Guterres 称「人类的红色警报」）/ WG II（2022-02）/ WG III（2022-04）+ 综合报告（2023-03）
  7. 特别报告：SR15《1.5°C 全球增温特别报告》（2018）、《气候变化与土地》（2019）、《海洋与冰冻圈》（2019）；方法学报告（1994/1996/2006 清单指南 + 2019 修订）
- **关键时间线（20 节点）**：
  1. 1986 ICSU/UNEP/WMO 设立温室气体咨询组（AGGG）
  2. 1988 WMO 与 UNEP 共同设立 IPCC；联合国大会决议背书
  3. 1988 Bert Bolin 当选首任主席
  4. 1989 设立信托基金；WMO 承担秘书处费用
  5. 1990 FAR 发布，促成 UNFCCC 谈判
  6. 1992 补充报告；UNFCCC 开放签署（1992 里约）
  7. 1995 SAR 发布，支撑《京都议定书》谈判
  8. 1997 Robert Watson 当选主席
  9. 2000 特别报告《排放情景》（SRES）
  10. 2001 TAR 发布，「曲棍球杆」曲线进入公众视野
  11. 2002 Rajendra K. Pachauri 当选主席
  12. 2007 AR4 发布（「unequivocal」）；同年与 Al Gore 共获诺贝尔和平奖
  13. 2009 哥本哈根大会前 «Climatic Research Unit email controversy» 引发媒体审视（客观记录）
  14. 2010 IAC 受托独立评估 IPCC 流程（9 月发布报告，7 项建议）
  15. 2012 IAC 建议大部分落实；AR5 筹备按新流程推进
  16. 2013–2014 AR5 发布，成为 2015《巴黎协定》的科学基础
  17. 2015 Hoesung Lee 当选主席
  18. 2018 SR15 发布，1.5°C 目标进入气候行动中心
  19. 2021–2023 AR6 三卷 + 综合报告；2023-07-28 Jim Skea 当选新主席，第七评估周期启动
  20. 2022 与 IPBES 共享 Gulbenkian 人类奖；2026-01 美国宣布将退出该机构（客观记录）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Intergovernmental_Panel_on_Climate_Change/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 OpenPeace 已完成篇目 Makefile，设置 `MAIN=Intergovernmental_Panel_on_Climate_Change_zh`、`VIDEO_NAME=Intergovernmental_Panel_on_Climate_Change_zh`

### 第 3 步：收集图片 【机构专属】

- 可用 page.md 内嵌图：IPCC 报告谱系页数图（Ipcc_assessments_pages）、SR15 决策者摘要通过现场（2018）、John T. Houghton 展示「曲棍球杆」图（2005）
- 封面用报告谱系图或 SR15 会场照构图；机构无「肖像」，勿用主席照冒充机构徽识

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | climate science | 气候科学 | 对文献的物理/生态/社会影响综合评估 | 评估报告页 |
| 1 | climate change assessment | 气候变化评估 | 六次评估报告谱系与三级背书 | 报告谱系页 |
| 2 | climate policy | 气候政策 | 为 UNFCCC/巴黎协定提供科学输入 | 政策影响页 |
| 3 | science-policy interface | 科学与政策接口 | 「给决策者的摘要」逐行批准机制 | 运作方式页 |
| 4 | greenhouse gas inventories | 温室气体清单 | TFI 方法学报告（1994–2019） | 方法学页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，机构专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Al Gore | 无向 | 2007 诺贝尔和平奖共同得主 |
| colleague | Bert Bolin | 无向 | 首任主席（1988 当选） |
| colleague | Rajendra K. Pachauri | 无向 | 2002 当选主席，2007 诺奖时任主席 |
| other | World Meteorological Organization | 无向 | 与 UNEP 于 1988 年共同设立 IPCC |
| other | United Nations Environment Programme | 无向 | 与 WMO 于 1988 年共同设立 IPCC |

- **不 入 库（仅叙述）**：Robert Watson/Hoesung Lee/Jim Skea（历任主席仅 Bolin/Pachauri 入库， Watson 因 2002 ExxonMobil 备忘录事件属争议叙事）；AGGG（前身机构）；IPBES/UNFCCC（后续姊妹机构与框架公约，时间线呈现）；Guterres/Hansen/Landsea（引语与争议当事人）。

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：大气的深蓝、科学的透明、制度的耐心
- **配色**：主色 `#37548D`（大气蓝，评估报告与全球合作的空间感，manifest 预分配勿改）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeScience` 气候科学 — 靛蓝 `#4C5FD5`
  - `badgeReport` 评估报告 — 青绿 `#0E7C7B`
  - `badgePolicy` 政策接口 — 琥珀 `#E07B30`
  - `badgeNobel` 诺贝尔 — 香槟金 `#C9A227`（强调用）
- **背景母题**：柔和气泡 + 大气分层同心弧线（低密度）

### 第 6 步：规划幻灯片序列 【机构专属，13 页 + 项目首页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 政府间气候变化专门委员会 / IPCC 1988– + 四色 badge + 报告谱系图
02  机构概览页（★ 必做）— 性质/设立/总部/成员国数/主席/三工作组+任务组/不做原创研究定位
03  缘起（1986–1988）— AGGG → 里根政府的担忧 → 政府间形态的折中
04  运作方式 — 不做原创研究、只做评估；三阶段评审与三级背书
05  评估报告谱系 — FAR→SAR→TAR（1990–2001）
06  AR4 与 2007 诺奖 — 「unequivocal」与获奖同年
07  AR5 与巴黎协定 — 2013/2014 报告成为 2015 协定科学基础
08  特别报告 — SR15（2018）、土地（2019）、海洋与冰冻圈（2019）
09  AR6 与第七周期 — 2021–2023 四卷、Jim Skea 当选、第七周期（2023–）
10  治理与经费 — Panel/Bureau/工作组、195 国自愿捐款
11  2007 诺贝尔和平奖 — 官方理由 + 与 Al Gore 共享
12  认可与争议 — IAC 评估（2010）、保守性之辩、影响力质疑（两说并陈、全部客观）
13  结尾
```

### 第 7 步：版式要点 【模板通用】

- 机构概览页参照个人篇 `\profileslide` 实现模式：左侧机构图 + 右侧信息网格（性质/设立/总部/成员国/主席/结构），事实取自 infobox，不得杜撰。
- 时间线页 20 节点拆两页（2007 诺奖分界），`\foreach` 分隔符必须 ASCII 逗号。
- 报告谱系页用六行表（报告/年份/关键句/政策影响），`arraystretch 0.62` + 顶部 `-0.35cm` 防溢出；AR4 的 "unequivocal" 引语 page.md 有英文原文可入引文框。
- 争议页用双栏「批评 / 回应」框，每栏 ≤3 条，只记 page.md 归属到人的观点。
- 编译硬指标：0 error、vbox ≤10pt、hbox ≤50pt，每写一页即 make 并 `pdftoppm` 目检。

### 第 8 步：史实审查 + 机构专属陷阱表 【机构专属】

| 陷阱 | 说明 |
|------|------|
| 勿写创始人 | IPCC 由 WMO 与 UNEP 两组织共同设立，**无个人创始人**；Bolin 是首任主席，禁写「缔造者/创立者」 |
| 勿写成研究机构 | 页面明载 "does not conduct its own original research"——定位是评估（assessment）不是科研，勿写「气候研究中心」 |
| 设立方口径 | WMO + UNEP（1988）；AGGG（1986）是前身不是设立方；联合国是「背书」不是共同设立方 |
| 主席谱系 | Bolin(1988)/Watson(1997)/Pachauri(2002)/Lee(2015)/Skea(2023) 五人顺序勿错；Slea 2023-07-28 就任 |
| 诺奖共享结构 | 理由句主语 "their"，本篇与 Al Gore 个人篇共用同一 EN+中译；获奖主体是机构+Gore 两人/两主体 |
| 引语边界 | 可引：AR4 "Warming of the climate system is unequivocal"、Guterres 对 AR6 WG I 的 "code red for humanity"（page.md 明载）；**禁引** Hansen 2024 语（含粗俗词，只可转述其海平面批评观点） |
| 争议两说 | 保守性之辩（Hansen/Pielke Sr. 批评 vs Rahmstorf「保守是优点」）、Climategate（2010 IAC 评估回应）、喜马拉雅冰川 2035 错误、ExxonMobil 备忘录与 Watson 去职、2023 巴西/阿根廷牛肉压力：全部按 page.md 客观记录、归属到人，禁单侧叙事 |
| 政治敏感 | 2026-01 美国宣布退出：仅客观一句记时间线，不作任何评价；当代政治人物一律不评价 |
| 缩写区分 | IPCC ≠ IPBES（2012，生物多样性）≠ ISPCWP（2025，化学品）；UNFCCC 是框架公约（客户）不是 IPCC 本体 |
| 机构身份 | 页面底部品牌标注统一 `OpenMathAI`；本篇获奖理由中译与 Gore 篇逐字一致 |

### 第 9 步：术语清单 【机构专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Assessment Report | 评估报告 | FAR/SAR/TAR/AR4/AR5/AR6 谱系 |
| Summary for Policymakers | 决策者摘要 | 逐行批准（approval）机制 |
| Working Group I/II/III | 第一/二/三工作组 | 物理/影响适应/减缓三分工 |
| mitigation | 减缓 | 勿译「缓解」 |
| adaptation | 适应 | 与 mitigation 并列 |
| Task Force on National Greenhouse Gas Inventories (TFI) | 国家温室气体清单任务组 | 方法学报告主管 |
| unequivocal | 毋庸置疑的 | AR4 关键句，照原文引 |
| hockey stick graph | 曲棍球杆曲线 | TAR 标志图像 |
| consensus | 共识机制 | 政府背书+科学家评估双轨 |
| peer review | 同行评议 | 「最大规模」为页面明载表述 |

---

## 四、背景音乐选择 ✅ 【机构专属，manifest 预分配勿改】

- **选定曲目**: **Last Hope** — Victor Cooper（inspiring-electronic 合集）
- **风格**: 戏剧性 / 史诗 / 宏大有力
- **匹配理由**:
  - 「宏大有力」匹配六次评估报告、195 国共识与「给人类的红色警报」的分量
  - 「Hope」呼应 SR15 之后 1.5°C 目标与《巴黎协定》的气候行动叙事
  - 戏剧性承载争议与自我改革的冲突弧线，收束于制度韧性
- **备选**（未采用，仅记录）: Cinematic Experience（已配 IAEA 篇）、Empire Collapse（偏衰落叙事，气质不合）
- **本地路径**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`
- **时长处理**: 曲目时长 > 13 页 × 7 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Intergovernmental_Panel_on_Climate_Change/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 获奖理由中译照抄来源 |
| `peace/PROMPTS_WORKFLOW.md` + `peace/PROMPTS_WORKFLOW_21ST.md` | 工作流与政治敏感红线（第 2 节机构规则） |
| `MySQL/data/Intergovernmental_Panel_on_Climate_Change.yaml` | 入库 yaml（与本文件第 4/4.5 步同步） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
