# 经济学家立传提示词（Douglas Diamond）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2022 年得主 Douglas Diamond（道格拉斯·戴蒙德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Douglas_Diamond/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Douglas Warren Diamond（1953-10-25 生于美国芝加哥，在世，卒年留白）
- **气质关键词**：**银行挤兑理论的建模范式、委托监督的提出者、现代银行学的微观基础**
- **诺奖获奖理由**（2022 三人共享，逐字引自 manifest/nobel_economics_citations.json）：
  > "for research on banks and financial crises"（表彰他们关于银行与金融危机的研究）
  > ——Diamond 的具体落点：Diamond–Dybvig 模型（1983）与委托监督模型（1984）。
- **设计母题**：**到期错配与双均衡（maturity mismatch & twin equilibria）**——短期存款支撑长期贷款的天平，以及「挤兑/不挤兑」两个均衡点的分岔图，是银行脆弱性的视觉隐喻。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Douglas_Diamond/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Douglas_Diamond/`（含 page.md / page.html / metadata.json / images.txt，肖像取 images.txt 或 Commons `Special:FilePath`，page.md 引用 2022 白宫照）；Makefile 复制后设 `MAIN=Douglas_Diamond_zh`、`VIDEO_NAME=Douglas_Diamond_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Diamond 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | Discipline Economics 下的金融学讲席教授身份 | 封面、核心页 |
| 1 | banking theory | 银行理论 | Diamond–Dybvig 模型；现代银行学基础工具 | 核心页 |
| 2 | financial intermediation | 金融中介 | 委托监督模型（1984）；"首个真正微观基础的金融中介理论"（诺奖委员会语） | 中介页 |
| 3 | liquidity | 流动性 | 流动性错配与挤兑机制；2008 后政策设计支持 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Stephen A. Ross | Ross → Diamond | 耶鲁博士导师（MA/MPhil/PhD）；Diamond 与 Dybvig 同门，常在 Ross 办公室外等候时交谈 |
| co-honored | Ben Bernanke | 无向 | 2022 诺贝尔经济学奖三人共享："for research on banks and financial crises" |
| co-honored | Philip H. Dybvig | 无向 | 2022 诺贝尔经济学奖三人共享："for research on banks and financial crises" |
| collaborator | Philip H. Dybvig | 无向 | 1983 JPE《Bank Runs, Deposit Insurance, and Liquidity》合著者，长期合作者（long-time collaborator） |
| spouse | Elizabeth Cammack Diamond | 无向 | 1982 结婚 |
| parent-child | Rebecca Diamond | Diamond → 女 | 经济学家（维基有词条）；配偶与子女人数均 page.md 明载 |
| parent-child | William Diamond | Diamond → 子 | 威斯康星大学麦迪逊分校金融学教授（James M. Johannes 讲席） |
| parent-child | Leon Diamond | Diamond → 父 | 精神科医生 |
| parent-child | Margaret Gunkel Seehafer | Diamond → 母 | 社会工作者、教授 |

**不入库但提示词可叙述**：Milton Friedman 与 Anna Schwartz（《美国货币史》课程让 Diamond 从分子生物学转向经济学——思想转折点，无持续关系不入 influence）；Raghuram Rajan（两篇合著论文仅见于参考文献列表，正文无合作叙述）；Theodore O. Yntema（讲席前任，非人物关系）。

## 五、配色方案 【人物专属】

- **气质**：冷静、结构化、把银行脆弱性写成方程的建模特质
- **主色**：`#123C5B`（manifest 预分配——与本批 Bernanke 同色系，芝加哥学派深蓝）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeFin` 金融经济学 — 深蓝 `#123C5B`
  - `badgeRun` 挤兑与存款保险 — 琥珀 `#C07A2A`
  - `badgeMonitor` 委托监督 — 青绿 `#0E7C7B`
  - `badgeLiq` 流动性 — 灰紫 `#52307C`
- **背景母题**：天平两端错落的短柱与长柱（短期存款/长期贷款）+ 分岔为两支的曲线（挤兑/稳定双均衡）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 银行挤兑理论的建模者 / Douglas Diamond 1953– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（1953-10-25 生于芝加哥、Brown BA 1975、
    Yale PhD 1980、芝加哥大学 Booth（1979 起）、诺奖 2022、核心领域）
03  核心贡献概览 — Diamond–Dybvig 模型 / 委托监督 / 存款保险与政策 / 银行业研究的微观基础
04  海德公园少年 (1953–1971) — 单亲母亲抚养；本想学分子生物学，一门弗里德曼-施瓦茨《美国货币史》课转向经济学
05  Brown 与 Yale (1971–1980) — Brown BA（Phi Beta Kappa）1975；Yale MA/MPhil/PhD 1980；
    论文 "Essays on Information and Financial Intermediation"（导师 Stephen A. Ross，与 Dybvig 同门）
06  Diamond–Dybvig 模型（核心贡献页）— 1983 JPE《Bank Runs, Deposit Insurance, and Liquidity》：
    银行用短期存款支撑长期贷款的流动性转换；到期错配使挤兑自我实现；政府存款保险可阻断
07  委托监督 (1984) — "Financial Intermediation and Delegated Monitoring"（RES）；
    诺奖委员会评价：首个真正微观基础的金融中介理论
08  模型的政策生命 — 存款保险制度与流动性监管的理论依据；2008 后为流动性支持、紧急贷款工具提供理论支撑；
    近年扩展至货币基金与加密交易所挤兑
09  芝加哥岁月 (1979– ) — Booth 商学院；2000-07 起 Merton H. Miller 杰出服务讲席；2010–14 主持 Fama-Miller 中心
10  荣誉 — Econometric Society Fellow 1990、AAAS 院士 2001、NAS 院士 2017、
    Morgan Stanley-AFA 卓越金融奖 2012、CME-MSRI 创新数量应用奖 2016、Wilbur Cross Medal 2017
11  2022 诺贝尔经济学奖 — 与 Bernanke、Dybvig 共享；2011 年起多次被预测为热门人选（Thomson Reuters 2011 等）
12  家庭与身后之学 — 1982 与 Elizabeth Cammack 结婚；女儿 Rebecca（经济学家）、儿子 William（金融学教授）；
    父 Leon（精神科医生）母 Margaret（社工、教授）
13  访学与学会服务 — 波恩大学、日本央行（1999）、港科大、MIT Sloan、Yale SOM；
    美国金融学会主席（2003）、西部金融学会主席（2001–02）
14  遗产与结尾 — 银行学的基础工具箱 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由拆分 | 2022 官方理由只有一句 "for research on banks and financial crises"（manifest 直接给出）；Diamond 的落点是 Diamond–Dybvig 模型与委托监督——引用框写全句，正文落点句另述 |
| Dybvig 三重关系 | 同门师兄弟（同为 Ross 学生）+ 合著者 + 同届共享得主——collaborator 与 co-honored 两条边并存，note 各自独立；师兄弟情（Ross 门外交谈）只叙述不单独建边 |
| Diamond 模型归名 | "Diamond model of delegated monitoring"（1984）是 Diamond 独著；**Peter Diamond**（2010 诺奖得主）是另一人，且只是伯南克论文评阅人之一——两位 Diamond 勿混 |
| 转行叙事 | 一门弗里德曼-施瓦茨课程使其从分子生物学转向经济学——按原文转述，Milton Friedman/Anna Schwartz **不入库**（无持续关系） |
| Rajan 不入库 | 与 Rajan 两篇合著仅出现于参考文献列表，正文无合作叙述——不入 collaborator（与 Dybvig 正文 "long-time collaborator" 明载区分） |
| 子女信息 | Rebecca Diamond 的维基链接标题是 Rebecca Diamond (economist)；William Diamond 职衔 James M. Johannes Professor——两子女均入库 parent-child |
| 日期 | 1953-10-25 生于芝加哥（frontmatter 与正文一致）；在世留白写 "1953–" |
| 讲席年份 | 2000-07 起 Merton H. Miller 讲席；1979 起执教 Booth（正文 "has taught since 1979" 与 "since July 2000" 两句并存，各有所指） |
| 引语红线 | 可引原文：诺奖委员会对 Diamond(1984) 的评价 "the first truly micro-founded theory of financial intermediation"（引原文+译文）。其余叙述不加引号冒充原话 |
| 竞选预测 | 2011/2013 的诺奖人选预测（Thomson Reuters、Fromlet、Rampell）只客观陈述"多次被预测"，勿写成"呼声最高" |
| 波恩/日央行 | 1983 波恩大学访问学者、1999 日本央行访问学者——两个不同身份勿混为"任职" |
| 2022 白宫照 | page.md 引用图注 "Diamond at the White House in 2022"，仅作肖像候选说明，正文无白宫事件叙述 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| bank run | 银行挤兑 | 自我实现的均衡，勿译"银行挤提"泛称 |
| Diamond–Dybvig model | 戴蒙德–迪布维格模型 | 1983 JPE；连字符用 en dash |
| deposit insurance | 存款保险 | 模型的政策结论 |
| maturity mismatch | 期限错配 | 短存长贷的流动性转换风险 |
| liquidity transformation | 流动性转换 | 银行的核心功能表述 |
| delegated monitoring | 委托监督 | 1984 独著论文的核心概念 |
| financial intermediation | 金融中介 | 与"中介机构"表述统一 |
| micro-founded | 微观基础的 | 诺奖委员会评价用词 |
| self-fulfilling | 自我实现 | 挤兑预期的均衡性质 |
| bank runs in nonbank institutions | 非银行机构挤兑 | 货币基金/加密交易所的近年扩展 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（主控分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「上升」贴合 Diamond–Dybvig 模型的治愈性结论——存款保险把挤兑的自我实现深渊翻转回稳定均衡，银行体系从脆弱中重拾上升轨迹；曲名的科幻预告片质感也呼应模型从 1983 年论文升格为全球存款保险与流动性监管理论基石的过程。
- **本地路径**：复制 `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav` 到 `economics/presentations/21th_century/Douglas_Diamond/Ascension.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Douglas_Diamond/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Douglas_Diamond/metadata.json` | QID/生卒/国籍结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Douglas_Diamond/images.txt` | 肖像候选 URL（2022 白宫照） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input`） |
| `MySQL/data/Douglas_Diamond.yaml` | 社会关系/研究领域入库存档（本批次已入库） |
| `economics/nobel_economics_citations.json` | 2022 获奖理由英文原文（Diamond 条目） |

## 十一、执行清单（供 Beamer agent 核对） 【模板通用】

1. 核对事实基准：所有事实与 page.md 逐条对照，冲突一律以 page.md 为准并在陷阱表记录裁定。
2. 复制 Makefile：`MAIN=Douglas_Diamond_zh`、`VIDEO_NAME=Douglas_Diamond_zh`。
3. 肖像：优先 images.txt 真实肖像；404 则装饰圆占位。
4. 配色：主色 `#123C5B` + badge 四色 + 背景母题（期限错配天平与双均衡分岔曲线）。
5. 幻灯片序列：按第六节 15 页规划，第 02 页身份信息页必做。
6. 编译循环：`make distclean && make`，0 error、vbox ≤ 10pt、hbox ≤ 50pt；pdftoppm 逐页目检。
7. 引语红线：只有第七节列出的诺奖委员会评语可入引文框（引原文+译文）。
8. 结尾页品牌口径：底部标注 `OpenMathAI`，引号用半角 " "。
9. 完成后 `make images && make video` 产出 mp4，向主控汇报页数与体积。

## 十二、版式补遗 【模板通用】

- **共享封面**：第 00 页 `\input` OpenEcon 统一封面，子 deck 不重复 GitHub 链接。
- **封面页**：主标题字号沿用模板；badge 主字体 scriptsize、副行 `\fontsize{6.5}{7.8}`；右上肖像细边框 + 姓名小字注。
- **身份信息页**：左头像 + 右信息网格，含至少生卒/出生地/教育/师承/任职/主要荣誉/核心领域七要素。
- **表格页安全负间距**：顶部 -0.35cm、`arraystretch 0.78-0.82`；荣誉多时用两列小表。
- **时间线页**：`\foreach` 分隔符必须 ASCII 逗号；勿给 foreach 节点套 tikz style。
- **获奖理由引用框**：英文原句 + 中文翻译两行制，英文逐字 "for research on banks and financial crises"。

## 十三、关键时间线速查 【人物专属】

| 年份 | 事件（均出自 page.md） |
|------|------|
| 1953-10-25 | 生于伊利诺伊州芝加哥；海德公园街区，单亲母亲抚养 |
| 少年 | 本想学分子生物学；在 Brown 的一门弗里德曼-施瓦茨《美国货币史》课后转向经济学 |
| 1975 | Brown 经济学 BA（Phi Beta Kappa） |
| 1976 / 1977 | Yale 两个硕士学位 |
| 1980 | Yale 经济学 PhD；论文 "Essays on Information and Financial Intermediation"（导师 Stephen A. Ross） |
| 1982 | 与 Elizabeth Cammack Diamond 结婚 |
| 1983 | Diamond–Dybvig 模型发表于 Journal of Political Economy；波恩大学访问学者 |
| 1984 | "Financial Intermediation and Delegated Monitoring"（RES），提出委托监督 |
| 1979 至今 | 芝加哥大学 Booth 商学院任教 |
| 1990 / 2001 | Econometric Society Fellow / AAAS 院士 |
| 1999 | 日本央行访问学者 |
| 2000-07 | Merton H. Miller 杰出服务讲席（此前 Theodore O. Yntema 讲席） |
| 2001–02 / 2003 | 西部金融学会主席 / 美国金融学会主席 |
| 2010–2014 | 主持 Fama-Miller 金融研究中心 |
| 2012 / 2013 | Morgan Stanley-AFA 卓越金融奖 / 苏黎世大学荣誉博士 |
| 2016 / 2017 | CME Group-MSRI 创新数量应用奖 / Wilbur Cross Medal、NAS 院士 |
| 2018 | Onassis 金融奖 |
| 2011 / 2013 | 被预测为诺奖热门人选（Thomson Reuters；Fromlet/WSJ/Rampell） |
| 2022-10-10 | 诺贝尔经济学奖（与 Bernanke、Dybvig 共享） |
| 2023 | Brown 名誉博士（Doctor of Humane Letters） |

> 表内每条均有 page.md 明载；子女职业与父母职业见第七节陷阱表，人物页第 12 页呈现。
