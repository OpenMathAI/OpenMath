# 和平奖得主立传提示词（OpenPeace 21 世纪批次：Al Gore）

> 本文件是 OpenPeace 项目 21 世纪诺贝尔和平奖批次的人物专属立传提示词。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（OpenMathAI 共享仓库 `peace/` 侧）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词结构）与和平奖侧 20 世纪批次实战经验。
- **本实例**：Albert Arnold Gore Jr.（阿尔·戈尔，2007 诺贝尔和平奖，与 IPCC 共享）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Albert Arnold Gore Jr.（1948-03-31 生于华盛顿特区，在世，享年——）
- **官方获奖理由（照抄，禁止改写）**：
  > "for their efforts to build up and disseminate greater knowledge about man-made climate change, and to lay the foundations for the measures that are needed to counteract such change."
  > 表彰他们为积累与传播人为气候变化的知识、并为应对此类变化所需的措施奠定基础所做的努力
  - ★ 注意主语是 **"their"**：2007 年与政府间气候变化专门委员会（IPCC）**共享**，勿写成个人独得。
- **气质关键词**：**气候行动的旗手、信息的传播者、败选后的转型者**
- **设计母题**：**气候曲线与警钟（rising curve）**。上升的温度曲线既是其气候传播事业的核心意象，也隐喻「把知识传播出去、把基础奠定下来」的获奖理由——用曲线/波形元素贯穿封面与章节页。
- **本地数据源**：`peace/presentations/pages/21th_century/Al_Gore/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 和平奖侧成品参照：`peace/presentations/20th_century/` 下已立传目录（如 Henry_Dunant 等）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（第一轮已核对，来源 = 本地 page.md） 【人物专属】

- 生卒：1948-03-31 生于华盛顿特区（在世，无卒日）；父 Albert Gore Sr.（田纳西州联邦众议员→参议员，库内已有记录 id=7109）；母 Pauline LaFon Gore（范德堡法学院早期女性毕业生之一）；姊 Nancy LaFon Gore 1984 年死于肺癌
- 国籍：美国
- 教育：St. Albans School（1956–1965，橄榄球队队长）；Harvard College（1965 入学，政府学专业，毕业论文获 A，1969-06 以 A.B. cum laude 毕业；高年级选修 Roger Revelle 课程，点燃全球变暖兴趣；室友 Tommy Lee Jones）
- 军旅：1969-08 应征入伍，Fort Dix 基础训练→Fort Rucker 记者；1971-01-02 赴越南，20th Engineer Brigade，战地报纸 The Castle Courier 记者；1971-05 荣誉退伍
- 此后：Vanderbilt Divinity School（1971–1972，洛克菲勒基金会奖学金）；The Tennessean 调查记者（1971 起）；Vanderbilt Law School（1974–1976，未毕业）
- 国会：联邦众议员（TN 第 4 选区，1977–1985）；联邦参议员（1985–1993）；1979-03-19 首位上 C-SPAN 的国会议员；1982 提出 Gore Plan 军控方案；1991 主导 High Performance Computing Act（Gore Bill）；1976 年任众议员后即主持首批国会气候变化听证
- 1988 年首度角逐民主党总统提名（超级星期二，名列第三）
- 副总统（1993–2001，克林顿政府两届）：1997《京都议定书》谈判与强力支持；1994 GLOBE 计划；推广 "Information Superhighway"
- 2000 年大选：普选票胜出约 54 万张（正文 543,895），选举人票 266:271 落败；Bush v. Gore 案最高法院 5–4 终止佛罗里达重新计票；2000-12-13 发表败选演说
- 副总统卸任后：2006 纪录片《难以忽视的真相》（An Inconvenient Truth，2007 获奥斯卡最佳纪录长片）；2004 联合创办 Generation Investment Management 并任董事长；创办 Alliance for Climate Protection（后发起 We Campaign）；The Climate Reality Project 创始人兼董事长；Live Earth 演唱会共同组织；Kleiner Perkins 风投合伙人（主管气候方案组）；2020 协助发起 Climate TRACE
- 关键荣誉：诺贝尔和平奖 2007（与 IPCC 共享）；Primetime Emmy 2007（Current TV）；Webby Award 2005；Prince of Asturias Award 2007（国际合作）；Dan David Prize 2008；Grammy 最佳诵读专辑 2009（An Inconvenient Truth 有声书）；American Philosophical Society 2008；Presidential Medal of Freedom 2024
- 家庭：1970-05-19 与 Mary Elizabeth "Tipper" Aitcheson 在华盛顿国家教堂成婚（2010-06 宣布分居）；四子女：Karenna（1973）、Kristin（1977）、Sarah LaFon（1979）、Albert III（1982）
- 关键时间线（15–20 节点）：1948 出生 → 1965 St. Albans 毕业 → 1965 入哈佛 → 1969 毕业+入伍 → 1971 越南服役归国 → 1971–72 神学院 → 1971 记者 → 1974 法学院 → 1976 当选众议员 → 1979 首位 C-SPAN 议员 → 1982 Gore Plan → 1984 当选参议员 → 1988 首度竞选总统 → 1989 长子车祸（转折点）→ 1992 Earth in the Balance + 副总统当选 → 1997 京都议定书 → 2000 大选败选 → 2004 Generation IM → 2006 《难以忽视的真相》→ 2007 诺贝尔和平奖 → 2024 总统自由勋章

### 第 4 步：事业领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | climate activism | 气候行动 | 1976 年首批气候听证至今，2007 诺奖核心 | 核心页 |
| 1 | environmental policy | 环境政策 | 京都议定书、Global Marshall Plan、碳税主张 | 政策页 |
| 2 | climate change communication | 气候传播 | 《难以忽视的真相》、The Climate Reality Project | 传播页 |
| 3 | information technology policy | 信息技术政策 | Gore Bill 1991、Information Superhighway | 科技页 |
| 4 | politics | 政治生涯 | 众议员/参议员/副总统/2000 大选候选人 | 履历页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Tipper Gore | 无向 | 1970-05-19 成婚，2010-06 宣布分居 |
| parent-child | Albert Gore Sr. | 无向 | 父亲，田纳西州联邦参议员（库内 id=7109 复用） |
| parent-child | Pauline LaFon Gore | 无向 | 母亲，范德堡法学院早期女性毕业生之一 |
| influence | Roger Revelle | 无向 | 哈佛高年级课程导师级人物，点燃其全球变暖兴趣 |
| colleague | Bill Clinton | 无向 | 1992/1996 竞选搭档，1993–2001 副总统任期 |
| colleague | Newt Gingrich | 无向 | 共同主持国会未来问题交流中心（Clearinghouse on the Future） |
| rival | George W. Bush | 无向 | 2000 年大选对手，普选票胜出而选举人票落败 |

- ★ **Gore↔IPCC co-honored 由批次 2（IPCC 侧 yaml）负责写入**，本篇 yaml **不写**该边（避免与对方批次重复劳动）；IPCC 落库后关系自动连通。

### 第 5 步：设计配色方案 【manifest 预分配，勿改】

- **主色**：`#7E1E23`（深绯红——警钟与决断）
- **诺奖香槟金**：`C9A227`
- badge 四分类色（建议）：气候行动 青绿 `#0E7C7B`；环境政策 森林绿 `#1E4E79`；气候传播 琥珀 `#E07B30`；信息技术 靛蓝 `#4C5FD5`
- **背景母题**：上升曲线与稀疏圆点（呼应「气候曲线与警钟」母题）

### 第 6 步：规划幻灯片序列 【人物专属，可微调；共 16 页 = 共享封面 + 15 帧】

```
00  OpenPeace 项目首页（\input cover 共享页）
01  封面 — 气候行动的旗手 / Al Gore b. 1948 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心事业概览 — 气候行动 / 环境政策 / 气候传播 / 信息技术政策
04  早年：华盛顿与田纳西农场 (1948–1965) — St. Albans、家庭农场、姐姐南希
05  哈佛与军旅 (1965–1971) — Revelle 课程、毕业论文、越南战地记者
06  神学院与新闻记者 (1971–1976) — Vanderbilt、The Tennessean 调查报道
07  国会岁月 (1976–1993) — 众议院/参议院、Gore Plan、气候听证、Gore Bill
08  副总统岁月 (1993–2001) — 京都议定书、GLOBE、信息高速公路
09  2000 年大选 — 普选票胜出与 Bush v. Gore、败选演说
10  《难以忽视的真相》(2006) — 纪录片与奥斯卡、气候传播新范式
11  诺贝尔和平奖 (2007) — 与 IPCC 共享、官方理由 EN+中译、奥斯陆领奖
12  气候事业的组织者 — Climate Reality / Generation IM / Live Earth / Climate TRACE
13  荣誉与认可 — Emmy/Webby/Dan David/Grammy/2024 总统自由勋章
14  遗产：从政客到气候传播先行者
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照已有和平奖成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用同项目已立传目录骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Gore 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 共享奖主语 | 官方理由是 "their"，与 IPCC 共享；勿写"独得"，勿把获奖理由改写成环保主义口号 |
| 2000 大选数字 | 普选票多约 54 万（正文 543,895）≠ 选举人票 266:271；Bush v. Gore 是 7–2（重计标准违宪）+ 5–4（无法按期完成重计）两段裁定，勿混为一谈 |
| "发明互联网" | 正文实为 Cerf/Kahn 背书其倡导高性能计算法案；"I invented the internet" 这类讹传引语**禁用** |
| 妻子口径 | Mary Elizabeth "Tipper" Aitcheson，1970 成婚、2010-06 **分居**（separated）——勿写"离婚" |
| 父子同名 | 父 Albert Gore Sr.（库内 id=7109）；本人全名 Albert Arnold **Gore Jr.**——行文注意 Jr. 后缀 |
| 奖章同名 | 2024 年获拜登颁 Presidential Medal of Freedom；勿与其他获奖者的同名奖章混淆 |
| 当代政治评价 | 对布什政府的批评、气候变化政治争论等段落一律**只客观记录 page.md 明载事实**，不加评价性语句 |
| 无载禁写 | 本页未载的环保活动细节（如独立主页面 Environmental activism 内容）禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| man-made climate change | 人为气候变化 | 官方理由原词，勿改"全球变暖" |
| IPCC | 政府间气候变化专门委员会 | 2007 共享得主，勿只写个人 |
| Kyoto Protocol | 京都议定书 | 1997 年谈判，美国未批准——客观表述 |
| An Inconvenient Truth | 《难以忽视的真相》 | 2006 纪录片 + 2006 同名书，两件作品 |
| information superhighway | 信息高速公路 | 1990 年代用语 |
| High Performance Computing Act | 高性能计算法（Gore Bill） | 1991，勿与互联网发明混淆 |
| Bush v. Gore | 布什诉戈尔案 | 2000 最高法院裁定 |
| Generation Investment Management | 代际投资管理公司 | 2004 联合创办，勿写成独资 |
| Climate Reality Project | 气候现实项目 | 创始人兼董事长 |
| Presidential Medal of Freedom | 总统自由勋章 | 2024 年获颁 |

---

## 四、背景音乐选择 【manifest 预分配，勿改】

- **选定曲目**：**Empire Collapse** — Cold Cinema（inspiring-electronic 曲库）
- **风格**: 史诗 / 戏剧性 / 重建感
- **匹配理由**：
  - "帝国崩塌后的重建" 匹配戈尔的叙事弧线——2000 年大选败选后的政治转折，转身成为全球气候传播事业的奠基者
  - 史诗配器匹配其事业的全球尺度：京都议定书、42 国立法者会议、Live Earth 全球演唱会
  - 曲名的戏剧张力匹配 2000 年最高法院裁定与 2007 年诺奖两个命运节点
- **本地路径**: `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Al_Gore/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
