# 经济学家立传提示词（Robert J. Shiller）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2013 年得主 Robert J. Shiller（罗伯特·希勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Robert_J._Shiller/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert James Shiller（1946-03-29 生于美国密歇根州底特律，在世）
- **气质关键词**：**非理性繁荣的预警者、行为金融的开路人、 bubbles 的吹哨人**
- **诺奖获奖理由**（2013 三人共享同句，manifest citation_en 已给出，逐字引用）：
  > "for their empirical analysis of asset prices"（表彰他们对资产价格的实证分析）
  - 共享得主：Eugene Fama / Lars Peter Hansen / Robert J. Shiller——Shiller 一翼是挑战者：以「过度波动」质疑有效市场假说。
- **设计母题**：**过度波动（excess volatility）**——股价曲线远超股息贴现基本面的振幅：一条温吞的基本面线与一条剧烈震荡的价格线并行的视觉隐喻，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Robert_J._Shiller/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Robert_J._Shiller/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_J._Shiller_zh`、`VIDEO_NAME=Robert_J._Shiller_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Shiller 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | infobox Discipline 首项；资产价格动力学 | 封面、核心页 |
| 1 | behavioral finance | 行为金融学 | infobox Discipline 第二项；情绪驱动交易 | 核心页 |
| 2 | asset pricing | 资产定价 | 2013 诺奖核心——过度波动与 CAPE | 核心页 |
| 3 | real estate economics | 房地产经济学 | Case–Shiller 房价指数与房地产泡沫预警 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 10 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Franco Modigliani | 对方是导师 | MIT 博士导师（1972 论文《Rational expectations and the structure of interest rates》） |
| collaborator | George Akerlof | 无向 | 合著《Animal Spirits》(2009)《Phishing for Phools》(2015)；infobox Influences 亦列 |
| influence | John Maynard Keynes | 对方影响本人 | infobox Influences；正文引「选美竞赛」比喻说明市场非理性 |
| influence | Irving Fisher | 对方影响本人 | infobox Influences 明载 |
| advisor-student | John Y. Campbell | 本人 → 学生 | infobox Doctoral students；正文称 colleague and former student |
| colleague | Richard Thaler | 无向 | 1991–2015 共同组织 NBER 行为金融工作坊 |
| collaborator | Karl Case | 无向 | Case–Shiller 房价指数共同开发者；1991 共创 Case Shiller Weiss |
| spouse | Virginia Marie Faulstich | 无向 | 妻，心理学家；两子女（不具名不入库） |
| co-honored | Eugene Fama | 无向 | 2013 同句理由共享诺奖 |
| co-honored | Lars Peter Hansen | 无向 | 2013 同句理由共享诺奖 |

**不入库但提示词可叙述**：Allan Weiss（Case Shiller Weiss CEO，公司合伙人但学术合作主体是 Case）；David Lereah（2005 CNBC 同台观点相左，一次性事件非持续关系）；父母 Ruth R.（née Radsville）/ Benjamin Peter Shiller 与立陶宛裔背景；David Lereah 与 Shiller 的公开分歧只叙述、不建 controversy（无持续性对抗载录）；2024 年 16 位诺奖得主联署信（政治性内容不写入立传，见陷阱表）。

## 五、配色方案 【人物专属】

- **气质**：警觉、人本、在喧嚣中听见情绪的杂音
- **主色**：`#8A1E2D`（manifest 预分配，2013 三人共享年份统一主色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeVol` 过度波动 — 深红 `#8A1E2D`
  - `badgeBehav` 行为金融 — 深蓝 `#16324F`
  - `badgeIndex` 指数发明 — 青绿 `#0E7C7B`
  - `badgeWarn` 泡沫预警 — 琥珀 `#C07A2A`
- **背景母题**：双线波动图（基本面线 vs 价格震荡线），呼应「市场波动大于任何理性未来观所能解释」的核心论断。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 非理性繁荣的预警者 / Robert J. Shiller 1946– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1946-03-29 底特律、Michigan BA 1967、
    MIT SM 1968/PhD 1972、导师 Modigliani、Yale Sterling Professor、诺奖 2013、核心领域）
03  核心贡献概览 — 过度波动 / Case–Shiller 指数 / CAPE / 泡沫预警
04  底特律与求学 (1946–1972) — Kalamazoo 两年转 Michigan Phi Beta Kappa、MIT 门下
05  有效市场假说的挑战者 (1981) — 波动性大于理性未来观可解释范围；AEA 百年 top 20 论文
06  1987 股灾与行为金融的转机 — 问卷调查：情绪驱动交易，1989 起连续采集
07  Case–Shiller 指数 — 重复销售法；1991 Case Shiller Weiss；Fiserv/S&P 收购与开发
08  CAPE 周期调整市盈率 — 十年均值盈利；长期投资者的择时启示
09  《非理性繁荣》(2000) — 2000-03 市场顶部预警；2005 二版房地产警告；书内引语原文
10  次贷危机的预警线 — 2006 WSJ 警告、2007-09 预测房市崩盘与金融恐慌
11  诺奖时刻 (2013) — 10-14 公布；获奖演讲论证市场为何无效；Campbell 线性化现值模型
12  叙事经济学 (2019) — 故事像病毒般传播；FT 年度好书
13  荣誉与公共写作 — Deutsche Bank Prize 2009、AEA 2016 主席、Project Syndicate 专栏
14  遗产与结尾 — 行为金融进入主流 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享理由 | 2013 三人共享**同句理由** "for their empirical analysis of asset prices"；勿写成 Shiller 个人理由 |
| 三人观点互异 | Fama 奠基有效市场、Shiller 挑战之——获奖演讲明确论证 EMH 有误（excess volatility puzzle），但 page.md **未载**两人私人交锋，Fama/Shiller 之间禁建 controversy；「同奖不同调」是立传叙事张力，不是关系边 |
| Akerlof 双重定性 | 合著两书与 infobox Influences 皆明载——入库只建 **collaborator** 一行（note 兼述 Influences），避免同人双边冗余；Keynes/Fisher 才用 influence |
| Campbell 定性 | 学生（infobox）+ 正文 "colleague and former student"——只建 advisor-student 一行 |
| 与 Fama 演讲交锋 | 获奖典礼演讲中 Shiller 论证 EMH fallacious、批评 Fama 断言——这是**学术观点对立的公开记录**，可叙述；但禁写成私人恩怨或建关系边 |
| 书内引语 | 《Irrational Exuberance》二版前言与 WSJ 2006 警告均有 page.md 英文原文，可引原文+译文；其余「非理性繁荣」等格林斯潘名言 page.md 未载，**禁写** |
| 凯恩斯比喻 | 选美竞赛比喻是 page.md 明载的 Shiller 援引 Keynes——写「希勒援引凯恩斯」，勿写成希勒原创 |
| 政治红线 | 2024 年 16 位诺奖得主联署公开信涉美国政党政治，立传**不写**（客观记录获奖事实与学术贡献即可） |
| 在世者生卒 | 1946-03-29 生，在世——卒日留白，全篇一致 |
| Bitcoin 口径 | 2017 年称比特币是当时最大金融泡沫（quoted as），转述口径；勿写成权威断言 |
| AEA 主席年份 | 副主席 2005、主席 **2016**、东部经济学会主席 2006–2007——三个年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| excess volatility | 过度波动 | 股价波动大于理性预期可解释范围；诺奖核心 |
| Irrational Exuberance | 《非理性繁荣》 | 2000 畅销书；书名本身禁写成格林斯潘语录出处 |
| Case–Shiller index | 凯斯–希勒房价指数 | 重复销售法房价指数；Case 共同开发 |
| CAPE (cyclically adjusted price-to-earnings ratio) | 周期调整市盈率 | 十年通胀调整盈利均值 |
| behavioral finance | 行为金融学 | 情绪与心理驱动市场决策 |
| Linearized Present Value model | 线性化现值模型 | 与学生 Campbell 合作；股息仅解释 1/2–1/3 波动 |
| repeat-sales index | 重复销售指数 | Case–Shiller 指数的技术内核 |
| Narrative Economics | 叙事经济学 | 2019 专著；故事传播驱动经济事件 |
| contingent capital | 或有资本 | 2010 危机修复提案 |
| Sterling Professor | 斯特林讲席教授 | 耶鲁最高教席，as of 2022 口径 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：泡沫顶点的孤声预警常被讥为乌鸦，但 2008 危机印证了「最后的希望」恰是敢于逆流的数据良心——从 1981 过度波动论文到次贷预警，Shiller 的叙事弧线是理性者在喧嚣中坚守；与 2013 三人共享年份统一用曲。
- **本地路径**：复制上述 wav 到 `economics/presentations/21th_century/Robert_J._Shiller/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
