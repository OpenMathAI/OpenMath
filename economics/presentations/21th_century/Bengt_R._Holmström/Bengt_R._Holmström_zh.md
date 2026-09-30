# 经济学家立传提示词（Bengt Holmström）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2016 年得主 Bengt Holmström（本特·霍姆斯特罗姆）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Bengt_R._Holmström/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Bengt Robert Holmström（1949-04-18 生于芬兰赫尔辛基，在世，卒年留白）
- **气质关键词**：**契约理论的建筑师、激励设计的工程师、赫尔辛基走出的机制设计大师**
- **诺奖获奖理由**（2016 与 Oliver Hart 共享，逐字引自 manifest / `economics/nobel_economics_citations.json`）：
  > "for their contributions to contract theory"（表彰他们对契约理论的贡献）
- **设计母题**：**激励与信息不对称（incentives under uncertainty）**——委托人看不见代理人的努力，只能通过契约把信息"折算"成报酬；以错落的折线/杠杆与半透明遮挡层构成背景母题，隐喻"可观察性"与"道德风险"。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Bengt_R._Holmström/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Bengt_R._Holmström/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Bengt_R._Holmström_zh`、`VIDEO_NAME=Bengt_R._Holmström_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Holmström 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | contract theory | 契约理论 | 2016 诺奖核心（与 Hart 共享） | 封面、核心页 |
| 1 | principal-agent theory | 委托-代理理论 | page.md 明载 "particularly well known" | 核心页 |
| 2 | theory of the firm | 企业理论 | 契约与激励在企业边界中的应用 | 应用页 |
| 3 | corporate governance | 公司治理 | 激励契约的公司治理应用 | 应用页 |
| 4 | financial economics | 金融经济学 | 金融危机中的流动性问题、货币市场不透明 | 流动性页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 7 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert B. Wilson | Wilson → 导师 | Stanford GSB 博士导师（1978），2020 诺奖得主 |
| co-honored | Oliver Hart | 无向 | 2016 诺贝尔经济学奖共享（契约理论贡献） |
| advisor-student | Jonathan Levin | Holmström → 学生 | 博士生（infobox Doctoral students 明载） |
| collaborator | Paul Milgrom | 无向 | 合著多任务委托代理（1991）与企业激励系统（1994） |
| collaborator | Donald John Roberts | 无向 | 合著《The boundaries of the firm revisited》（1998） |
| collaborator | Jean Tirole | 无向 | 合著《Private and public supply of liquidity》（1998） |
| spouse | Anneli Holmström | 无向 | 妻，育一子 |

**不入库但提示词可叙述**： Helsinki/Stanford/Northwestern/Yale/MIT 任职机构（非人际关系）；各学术团体 fellow/foreign member（机构边不入库）；Nokia 董事会与 Aalto 大学董事会（机构任职）；一子未具名不入库。

## 五、配色方案 【人物专属】

- **气质**：冷静、精确、契约结构的秩序感
- **主色**：`#7E1E23`（契约深红——manifest 预分配，与 Hart 篇同色呼应 2016 共享；沉稳的深红对应契约文书的庄重）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeContract` 契约理论 — 深红 `#7E1E23`
  - `badgeAgent` 委托-代理 — 靛蓝 `#37474F`
  - `badgeFirm` 企业理论 — 深蓝 `#16324F`
  - `badgeLiq` 流动性与危机 — 琥珀 `#C07A2A`
- **背景母题**：折线与杠杆节点（激励曲线）+ 半透明遮挡层（信息不对称），呼应「把不可观察的努力折算成可执行的契约」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 契约理论的建筑师 / Bengt Holmström 1949– + 四色 badge + 右上头像 + 国籍行（Finland）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地赫尔辛基、教育 Helsinki BS 1972 /
    Stanford MS 1975 / Stanford GSB PhD 1978、师承 Robert B. Wilson、任职 MIT、诺奖 2016、核心领域）
03  核心贡献概览 — 道德风险与可观察性 / 团队道德风险 / 多任务委托代理 / 流动性
04  早年与教育 (1949–1976) — 赫尔辛基出生、芬兰瑞典语少数族裔、Helsinki 数学与自然科学 BS 1972、
    企业规划师 1972–74、Stanford 运筹学 MS 1975、1976 移居美国
05  斯坦福博士：Wilson 门下 (1976–1978) — GSB 博士，论文 On incentives and control in organizations
06  早期任教 (1978–1994) — Hanken 助教、Northwestern Kellogg 副教授、Yale SOM
    Edwin J. Beinecke 讲席教授
07  道德风险三部曲（核心贡献页）— Moral hazard and observability (1979) / Moral hazard in teams
    (1982) / 长期劳动契约 (1983)——不确定性下契约理解的奠基性推进
08  多任务委托代理（核心贡献页，与 Milgrom）— Multitask Principal–Agent Analyses (1991) /
    The firm as an incentive system (1994)：企业即激励系统
09  企业边界与管理动态视角 — Managerial incentive problems: A dynamic perspective (1999) /
    The boundaries of the firm revisited (1998, 与 Roberts)
10  流动性与金融危机 — Private and public supply of liquidity (1998, 与 Tirole)、货币市场
    「不透明的好处」、2008 危机中对政府救助的支持
11  MIT 岁月与门生传承 — 1994 起执教 MIT、Paul A. Samuelson 讲席教授（荣休）；博士生 Jonathan Levin
12  荣誉与认可 — Nobel 2016 · Econometric Society 主席 2011 · 各院院士/fellow · 荣誉博士
    （SSE/Vaasa/Hanken）· Banque de France-TSE Prize 2012 · Ross Prize 2013 · CME-MSRI Prize 2013
13  产业界与公共实践 — Nokia 董事会 1999–2012 · Aalto 大学董事会 2008–2017 ·
    2016-12-08 诺奖演讲 Pay for Performance and Beyond
14  遗产与结尾 — 契约理论从理论到政策应用的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖共享表述 | 2016 与 Oliver Hart 共享，理由同一句 "for their contributions to contract theory"；勿写成"霍姆斯特罗姆独得"或"各一半" |
| 姓名拼写 | 目录/yaml 文件名用 `Bengt_R._Holmström`（含 R. 与变音符 ö），但 name_en 用 manifest 形式 `Bengt Holmström`；全名 Bengt Robert Holmström 勿写成 Bengt R. Holmström 当正式名 |
| 国籍 | 仅 Finland（Nobel 口径）；是芬兰瑞典语少数族裔（Finland-Swedes）——这是语言群体事实，勿写成"瑞典籍" |
| 博士导师 | Robert B. Wilson（Stanford GSB 1978）；他是 2020 诺贝尔经济学奖得主（与 Milgrom 共享）——奖项年份勿写成本批次事实以外的推论，仅注"2020 诺奖得主" |
| 撞名风险 |对手方 Robert B. Wilson 勿与库内 Robert R. Wilson(2390)/Robert Woodrow Wilson(2611, 物理 1978) 混淆；合著者 John Roberts（Stanford 商学院经济学家）勿与库内化学家 Richard J. Roberts 之父 John Roberts(6650) 混淆，规范名用 Donald John Roberts |
| 学位细节 | Helsinki BS 1972 是"数学与自然科学"（mathematics and science）、Stanford MS 1975 是运筹学（operations research）、PhD 1978 属 Graduate School of Business——三段学科勿互串 |
| Yale 头衔 | Edwin J. Beinecke Professor of Management（1983–1994，School of Management）；MIT 1994 起为 economics and management 教授，现为 Paul A. Samuelson Professor (Emeritus) |
| Milgrom 关系 | Holmström 与 Milgrom 是合著者（1991/1994 两篇），非师生；Milgrom 是 Wilson 的学生（2020 与 Wilson 共享诺奖）——两条链勿交叉错接 |
| 无直接引语 | page.md 无 Holmström 本人原话引语，引文框只能用诺奖 citation 原句或获奖演讲标题；禁杜撰名言 |
| metadata 噪声 | metadata.json 无冲突项；frontmatter doctoral_advisor 与 infobox 一致（Robert B. Wilson），无需裁定 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| contract theory | 契约理论 | 获奖理由核心词，勿译"合同理论" |
| principal-agent theory | 委托-代理理论 | 勿与"博弈论"混称 |
| moral hazard | 道德风险 | 1979/1982 两篇论文主题 |
| observability | 可观察性 | 信息不对称的技术条件 |
| multitask principal-agent model | 多任务委托-代理模型 | 1991 与 Milgrom 合著 |
| theory of the firm | 企业理论 | "企业即激励系统"（1994） |
| liquidity | 流动性 | 金融危机研究关键词 |
| opacity | 不透明（的好处） | 货币市场研究立场，勿写成贬义 |
| Econometric Society | 计量经济学会 | 2011 年主席 |
| operations research | 运筹学 | MS 专业，勿写成"经济学硕士" |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：契约理论处理的是"看不见的激励与信息"——委托人永远无法直接观察代理人的努力，只能靠契约间接引导；"不可见之光"的隐喻恰好对应「把不可见的努力变为可设计的行为」。曲名的纪录片感也贴合从赫尔辛基到 MIT 的学术演进叙事。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/21th_century/Bengt_R._Holmström/TheInvisibleLight.wav`（与 Hart 篇同曲，共享年份双人同曲有先例）
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Bengt_R._Holmström/page.md` | ★ 唯一事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一首页模板 |
| `MySQL/data/Bengt_R._Holmström.yaml` | 入库 yaml（已执行） |
| `economics/nobel_economics_citations.json` | 获奖理由英文原文 |

## 十一、执行清单 【模板通用】

1. 读本提示词 + page.md 建立事实基准；2. 下载肖像（250px 改 500px，Commons 404 则装饰圆占位）；3. 复制 Makefile 设 `MAIN=Bengt_R._Holmström_zh`；4. 按 §六写 15 页 Beamer；5. `make distclean && make` 编译循环（0 error、vbox≤10pt、hbox≤50pt）；6. pdftoppm 逐页目检；7. 两轮 Review；8. DB `has_biography` 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 -0.35cm、arraystretch 0.78-0.82；公式框前 -0.35~-0.55cm。
- 时间线 `\foreach` 分隔符必须 ASCII 逗号；文本模式希腊字母须数学模式；宏名禁数字。
- 引语框：仅诺奖 citation 原句（英中对照）；半角引号；品牌口径 `OpenMathAI`。
