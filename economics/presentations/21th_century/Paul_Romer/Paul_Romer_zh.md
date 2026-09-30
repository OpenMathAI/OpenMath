# 经济学家立传提示词（Paul M. Romer）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2018 年得主 Paul M. Romer（保罗·罗默）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Paul_Romer/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Paul Michael Romer（1955-11-06 生于美国科罗拉多州丹佛，在世，卒年留白）
- **气质关键词**：**内生增长理论之父、思想非竞争性的发现者、从学术界到世界银行的首席经济学家**
- **诺奖获奖理由**（2018 与 William Nordhaus 共享但**理由句各一**，逐字引自 `economics/nobel_economics_citations.json` 2018 Paul Romer 条目）：
  > "for integrating technological innovations into long-run macroeconomic analysis"
  > （表彰他将技术创新纳入长期宏观经济分析）
  > Nordhaus 那一条是 "for integrating climate change into long-run macroeconomic analysis"——两句勿互串。
- **设计母题**：**思想的非竞争性（non-rivalry of ideas）**——一个想法可以同时被所有人使用而不损耗；以复制的发光点阵/涟漪共享构成背景母题，隐喻"发现即普惠"。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Paul_Romer/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Paul_Romer/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Paul_Romer_zh`、`VIDEO_NAME=Paul_Romer_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Romer 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | endogenous growth theory | 内生增长理论 | 2018 诺奖核心；1986/1990 两篇 JEP 论文开创 | 封面、核心页 |
| 1 | macroeconomics | 宏观经济学 | 长期增长与技术创新的宏观分析 | 核心页 |
| 2 | technological change | 技术变迁 | 技术进步源于人类有意的研发行动 | 理论页 |
| 3 | non-rival goods | 非竞争性物品 | 思想的核心特性：用者不损、人人可用 | 理论页 |
| 4 | urbanization | 城市化 | NYU Marron 城市管理研究所与 Urbanization Project | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 10 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | José Scheinkman | Scheinkman → 导师 | Chicago 博士导师之一（1983 论文） |
| advisor-student | Robert Lucas Jr. | Lucas → 导师 | Chicago 博士导师之一（1983 论文），1995 诺奖得主 |
| advisor-student | Russell Davidson | Davidson → 导师 | 其他学术导师（infobox Other academic advisors 明载） |
| advisor-student | Ivar Ekeland | Ekeland → 导师 | 其他学术导师（infobox Other academic advisors 明载） |
| advisor-student | Sérgio Rebelo | Romer → 学生 | 博士生（infobox Doctoral students 明载） |
| advisor-student | Maurice Kugler | Romer → 学生 | 博士生（infobox Doctoral students 明载） |
| co-honored | William Nordhaus | 无向 | 2018 诺贝尔经济学奖共享（理由句各一：技术创新/气候变化） |
| parent-child | Roy Romer | Romer → 子 | 父，前科罗拉多州州长 |
| collaborator | George Akerlof | 无向 | 合著 Looting: The Economic Underworld of Bankruptcy for Profit（1993） |
| spouse | Caroline Weber | 无向 | 妻，Barnard 学院法国文学教授；2018 领奖当日结婚 |

**不入库但提示词可叙述**：兄弟 Chris Romer（前科罗拉多州参议员——兄弟关系无对应类型不入库，另六位兄弟姐妹未具名）；母 Beatrice "Bea" Miller（叙述）；Aplia/Cengage（公司史非人际关系）；World Bank 机构任职；Jim Yong Kim / Kaushik Basu / Shanta Devarajan（世行职务交接叙述）；Augusto Lopez-Claros（智利排名争议对手方——controversy 属机构事件非两人持续关系，不入库）。

## 五、配色方案 【人物专属】

- **气质**：开阔、增长感、思想的传播与扩散
- **主色**：`#1B4D6B`（增长深湖蓝——manifest 缺省（null），本批次裁定补配 `#1B4D6B`，与 econ21th 全表无撞色；湖蓝的"扩散感"对应思想在人群中的非竞争性传播）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGrowth` 内生增长 — 湖蓝 `#1B4D6B`
  - `badgeIdeas` 思想非竞争性 — 青绿 `#0E7C7B`
  - `badgeCity` 城市化与宪章城市 — 琥珀 `#C07A2A`
  - `badgeWB` 世界银行实践 — 靛蓝 `#37474F`
- **背景母题**：发光点阵的复制涟漪（同一思想的多重使用），呼应「思想一旦被发现，人人可用」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 内生增长理论之父 / Paul M. Romer 1955– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地丹佛、教育 Phillips Exeter 1973 /
    Chicago BS 数学 / PhD 1983、师承 Scheinkman 与 Lucas Jr.、任职 Boston College、
    世行首席经济学家 2016–18、诺奖 2018、核心领域）
03  核心贡献概览 — 内生增长理论 / 思想非竞争性 / 宪章城市 / Mathiness 批评
04  家世与早年 (1955–1973) — 丹佛出生、父 Roy Romer 前科罗拉多州长、七兄弟姐妹、
    Phillips Exeter 1973 毕业
05  Chicago 博士 (1973–1983) — BS 数学；MIT 1977–79 与 Queen's 1979–80 研究生游学；
    1983 论文 Dynamic Competitive Equilibria...，师从 Scheinkman 与 Lucas Jr.
06  内生增长理论的诞生（核心贡献页）— 1986 Increasing Returns and Long Run Growth 与
    1990 Endogenous Technological Change（JPE 两篇）：技术进步是人的有意选择（研发）
07  思想的非竞争性（核心贡献页）— 「若百万人寻找同一发现，任何一人找到即人人可用」：
    知识驱动长期增长的机制；1997 Time 25 位最具影响力、2002 Recktenwald 奖、2015 Commons 奖
08  创业与教育技术 — 2001 离开学界创办 Aplia（2000 年创立，线上习题集、答案累计逾 24 亿）、
    2007 被 Cengage 收购；「A crisis is a terrible thing to waste」金句出处（2004，本意另有所指）
09  宪章城市实验 — 2009 TED 演讲提出并推广 charter cities；洪都拉斯 ZEDE 项目、
    2012-09 因政府绕过透明委员会辞职
10  NYU 岁月 — Marron 城市管理研究所创始人、Urbanization Project 主任；城市化改善安全健康与出行
11  世界银行首席经济学家 (2016-10 – 2018-01-24) — 因智利营商环境排名争议（WSJ 访谈称方法调整
    或涉政治动机、遭当事经济学家否认）辞职；双方说法并列客观呈现
12  诺贝尔奖 — 2018 与 Nordhaus 共享但理由句各一（technological innovations / climate change）；
    瑞典科学院评语（knowledge as driver of long-term growth）；2018-12-08 演讲 On the Possibility
    of Progress；领奖当日与 Caroline Weber 结婚
13  Mathiness 与当下 — coined "mathiness"（经济学研究中对数学的滥用）；Boston College
    Seidner 讲席教授；内生增长框架被用于理解 AI 投资与长期经济效应（page.md 近年节明载）
14  遗产与结尾 — 增长理论从 Solow 外生技术到内生创新的格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生日 infobox/正文冲突 | infobox 与 frontmatter 均作 **1955-11-06**，正文首句作 November 7——以 infobox **1955-11-06** 为准（yaml 填 11-06），陷阱表注记两说 |
| 获奖理由各一 | 2018 是"拆分理由"年份：Romer 一句 technological innovations、Nordhaus 一句 climate change；两篇各忠于本人那条 citation，勿互串、勿合写成一句 |
| 博士双导师 | Scheinkman 与 Lucas Jr. 并列（infobox 与正文一致）；勿只写一人。另有 Other academic advisors Russell Davidson 与 Ivar Ekeland（infobox 明载，按先例入库 advisor-student 加注） |
| Lucas 奖项 | Robert Lucas Jr. 是 1995 诺贝尔经济学奖得主——年份勿写成 2018 或漏写 |
| Akerlof 规范名 | 合著者规范名 **George Akerlof**（2001 诺奖得主）；库内另有 Gosta Akerlof(4105, 主职业 mathematician, 系 Fenn 化学批次误建) 勿复用——本批新建 George Akerlof stub，分裂项已报主控 |
| 宪章城市争议 | 洪都拉斯项目"有人认为属新殖民主义（neo-colonialism）"是 page.md 明载的他方观点，用「有人认为」转述，勿作断言 |
| 世行辞职争议 | 智利排名事件：Romer 指控与 Lopez-Claros 否定两说并列；涉智利前总统 Bachelet 的段落仅客观转述时间背景、不评价；不建任何 controversy 库边 |
| 政治内容红线 | page.md Political views 节（2024 年 16 位诺奖得主公开信涉美国政治人物）一律不写入幻灯片与提示词叙事，不入库任何关系 |
| 金句归属 | "A crisis is a terrible thing to waste" 是 Romer 2004-11 在加州风投会议所说（本意指他国教育水平快速追赶美国），后被大衰退语境挪用——引用须带出处与本意说明 |
| 兄弟不入库 | Chris Romer 系兄弟（无 sibling 类型）；父 Roy Romer 用 parent-child（Romer → 子方向，Roy 为 parent） |
| 配色裁定 | manifest main_color=null，本批补配 #1B4D6B（Nordhaus 补配 #2E5339），已核对 econ21th 全表无撞色 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| endogenous growth theory | 内生增长理论 | 获奖核心；勿写成"内部增长论" |
| non-rival | 非竞争性 | 思想的经济学特性，与"排他性"（excludability）区分 |
| increasing returns | 收益递增 | 1986 论文标题关键词 |
| technological change | 技术变迁 | 内生化对象 |
| charter city | 宪章城市 | Romer 提出（TED 2009），勿译"特许城市"泛化 |
| mathiness | 数学腔/数学滥用 | Romer 自创词，指数学形式滥用于经济研究 |
| integrated assessment | （非本篇术语） | 勿与 Nordhaus 的 IAM 混淆——2018 两人主题不同 |
| Chief Economist of the World Bank | 世界银行首席经济学家 | 2016-10 至 2018-01-24 |
| Solow–Swan model | 索洛-斯旺模型 | 外生增长参照系（正文叙述背景） |
| Aplia | 教育科技公司 | 创办叙事，勿写成"咨询公司" |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：曲名的张力感对应 Romer 叙事中的对抗弧线——世行辞职争议、宪章城市实验受挫、对学界 mathiness 的公开批评；而在裂痕之下，思想非竞争性的涟漪仍在扩散，形成"破坏与生长并存"的双主题。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/21th_century/Paul_Romer/FallingApart.wav`（与 Nordhaus 篇同曲，共享年份双人同曲有先例）
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Paul_Romer/page.md` | ★ 唯一事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一首页模板 |
| `MySQL/data/Paul_Romer.yaml` | 入库 yaml（已执行） |
| `economics/nobel_economics_citations.json` | 获奖理由英文原文（2018 拆分两条） |

## 十一、执行清单 【模板通用】

1. 读本提示词 + page.md 建立事实基准；2. 下载肖像（250px 改 500px，Commons 404 则装饰圆占位）；3. 复制 Makefile 设 `MAIN=Paul_Romer_zh`；4. 按 §六写 15 页 Beamer；5. `make distclean && make` 编译循环（0 error、vbox≤10pt、hbox≤50pt）；6. pdftoppm 逐页目检；7. 两轮 Review；8. DB `has_biography` 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 -0.35cm、arraystretch 0.78-0.82；公式框前 -0.35~-0.55cm。
- 时间线 `\foreach` 分隔符必须 ASCII 逗号；文本模式希腊字母须数学模式；宏名禁数字。
- 引语框：citation 与瑞典科学院评语用英文原文+译文；Romer 本人引语（发现与想法的问答）为 page.md 明载原话可整段引用；半角引号；品牌口径 `OpenMathAI`。
