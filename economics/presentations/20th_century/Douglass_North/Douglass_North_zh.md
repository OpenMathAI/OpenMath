# 经济学家立传提示词（Douglass North）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1993 年得主 Douglass C. North（道格拉斯·诺思）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Douglass_North/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Douglass Cecil North（1920-11-05 生于马萨诸塞州剑桥 ~ 2015-11-23 逝于密歇根州本佐尼亚夏宅，享年 95 岁，死于食道癌）
- **气质关键词**：**新制度经济学开山者、计量史学（cliometrics）推广者、「制度是游戏的规则」的言说者**
- **诺奖获奖理由**（1993，与 Robert Fogel 共享，manifest citation 逐字）：
  > "for having renewed research in economic history by applying economic theory and quantitative methods in order to explain economic and institutional change"（表彰他们运用经济理论与量化方法重新开展经济史研究，以解释经济与制度变迁）
- **设计母题**：**规则与路径（rules & path）**——North 把制度定义为「人为设计的约束」与「游戏规则」：以棋盘格线、路径分岔与逐渐凝固的轨道构成背景母题，呼应「正式规则 + 非正式约束共同塑造长期经济变迁」与路径依赖。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Douglass_North/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）
- **一句话画像**：伯克利文科三主修的「C 等生」，二战商船队的良心拒服兵役者在海上读完经济学；1960 年代与福格尔一道把计量方法带进经济史，1997 年与科斯、威廉姆森共创 ISNIE；从《西方世界的兴起》到《暴力与社会秩序》，一生追问「为什么有的国家富、有的国家穷」。

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Douglass_North/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Douglass_North_zh`、`VIDEO_NAME=Douglass_North_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。
> 布局检查照模板第 8 步：每写完一页 `make distclean && make`，`pdftoppm` 截图逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

## 三、研究领域梳理 + 入库 【人物专属】

**North 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economic history | 经济史 | 1993 诺奖核心：经济理论与量化方法重振经济史研究 | 封面、核心页 |
| 1 | new institutional economics | 新制度经济学 | 学派代表：制度提供经济的激励结构 | 核心页 |
| 2 | cliometrics | 计量史学 | 1960 年起任《Journal of Economic History》共同主编，推广 cliometrics | 方法页 |
| 3 | transaction costs | 交易成本 | 制度降低交易成本、创造稳定与可预期性的框架 | 制度页 |
| 4 | property rights | 产权 | 产权、制度基础与历史中的经济组织研究 | 制度页 |

补充说明（供立传 agent 取材）：代表作谱系——《The Economic Growth of the United States, 1790-1860》(1961)；与 Lance Davis 合著《Institutional Change and American Economic Growth》(1971)；与 Robert Paul Thomas 合著《The Rise of the Western World: A New Economic History》(1973)；《Structure and Change in Economic History》(1981)；《Institutions, Institutional Change and Economic Performance》(1990)；1991 JEP 论文《Institutions》（制度 = 正式规则 + 非正式约束）；1994 诺奖演讲 "Economic Performance through Time"；与 Wallis/Weingast 合著《Violence and Social Orders》(2009)（limited access orders vs open access orders 两类社会秩序框架）。1991 年成为首位获 John R. Commons Award 的经济史学家。

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Robert Fogel | 无向 | 1993 经济学奖共享（运用经济理论与量化方法重振经济史研究以解释经济与制度变迁） |
| spouse | Lois Heister | 无向 | 1944-06-29 结婚，1972 离异；三子 Douglass Jr./Christopher/Malcolm 之母；婚姻期间成为知名活动家与政治人物 |
| spouse | Elisabeth Case | 无向 | 1972 年离婚同年再婚 |
| advisor-student | Melvin Moses Knight | Knight → 导师 | frontmatter doctoral_advisor 明载（infobox Influences 同指 Melvin M. Knight），伯克利时期 |
| collaborator | John J. Wallis | 无向 | 合著《Violence and Social Orders》(2009)；「自然国家」到长期增长的合作研究 |
| collaborator | Barry Weingast | 无向 | 合著《Violence and Social Orders》(2009)；斯坦福政治学家 |
| colleague | Ronald Coase | 无向 | 与 Coase、Williamson 共同创立 ISNIE（国际新制度经济学学会），1997 圣路易斯首次会议 |
| colleague | Oliver E. Williamson | 无向 | ISNIE 共同创始（1997 首次会议） |
| collaborator | Lance E. Davis | 无向 | 合著《Institutional Change and American Economic Growth》(1971) |
| collaborator | Robert Paul Thomas | 无向 | 合著《The Rise of the Western World: A New Economic History》(1973) |

**不入库但提示词可叙述**：三子 Douglass Jr./Christopher/Malcolm（仅具名无链接，parent-child 不入）；60 周年纪念册所列门生与合作者群像（Jonathan Hughes、Richard Sutch、Lloyd Mercer、Jim Sheperd、Donald Gordon、Gary Walton、Robert Huttenback、Roger Ransom、Gaston Rimlinger、P.J. Hill、Philip Coelho、David Knowles——名录式提及无逐一明载关系）；Copenhagen Consensus 专家与 Vipani 顾问（机构任职不建人物边）。

## 五、配色方案 【人物专属】

- **气质**：厚重、历史纵深、制度的冷峻与秩序感
- **主色**：`#1F3A5F`（manifest 未预分配，本批自选，深海蓝——制度的秩序感与历史的纵深；已向主控报备）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeNIE` 新制度经济学 — 深海蓝 `#1F3A5F`
  - `badgeClio` 计量史学 — 青绿 `#0E7C7B`
  - `badgeViol` 暴力与社会秩序 — 灰紫 `#52307C`
  - `badgeGrowth` 长期增长与路径依赖 — 琥珀 `#C07A2A`
- **背景母题**：棋盘格线与路径分岔（正式规则的秩序感 + 非正式约束的绵延），呼应「规则塑造长期变迁」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex，品牌口径 OpenMathAI）
01  封面 — 制度是游戏的规则 / Douglass C. North 1920–2015 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒（1920-11-05 Cambridge, MA ~ 2015-11-23 Benzonia, MI，
    享年 95）、教育（UC Berkeley BA 1942 / PhD 1952，论文论 1906 年前的人寿保险公司）、
    任职（Washington 1951-83 主持系务 1967-79 → Washington University in St. Louis 1983-，
    Henry R. Luce 讲席；Hoover Institution）、诺奖 1993
03  核心贡献概览 — 经济史重振 / 新制度经济学 / 计量史学 / 暴力与社会秩序（四 badge 横排）
04  早年与海上岁月 (1920–1950) — 父任职 MetLife 的多次迁居（渥太华/洛桑/纽约/沃灵福德）；
    Ashbury 与 Choate；伯克利三主修「C 等生」；商船学院毕业、三年甲板军官、二战领航员
05  摄影还是经济学 — 海上读经济学养成终生摄影爱好；战末在 Alameda 教领航；在摄影师与经济学家之间的抉择
06  伯克利博士与华盛顿大学 (1952–1960) — 1952 PhD；1955 论文《Location Theory and Regional Economic Growth》；
    华盛顿大学助教授起步
07  计量史学的推广 (1960–1970s) — 1960 起共同主编《Journal of Economic History》推广 cliometrics；
    1967-79 主持经济系；《Growth and Welfare in the American Past》(1974)
08  制度三部曲 (1971–1981) — 与 Davis 合著制度变迁 (1971)；与 Thomas 合著《西方世界的兴起》(1973)：
    产权而非技术进步解释西方兴起；《Structure and Change in Economic History》(1981)
09  制度理论 (1990–1991)（核心贡献页）— 1990《Institutions, Institutional Change and Economic Performance》；
    1991 JEP《Institutions》：正式规则 + 非正式约束；制度降低交易成本、也未必有效率（路径依赖）
10  交易成本与意识形态 (1992)（核心贡献页）— 《Transaction Costs, Institutions, and Economic Performance》：
    交易成本根于信息不对称；意识形态是「心智模型」；企业家推动的渐进制度变迁
11  荣誉与诺奖 — 1991 Commons Award（首位经济史得主）；1993 与 Fogel 共享诺贝尔奖；
    1994 诺奖演讲 Economic Performance through Time；Guggenheim Fellow
12  暴力与社会秩序 (2009)（核心贡献页）— 与 Wallis/Weingast：limited access orders vs open access orders；
    制度的首要任务是限制暴力；两步走从有限准入走向开放准入
13  晚年与新制度经济学建制 — 1997 与 Coase/Williamson 创 ISNIE（圣路易斯首会）；
    1984-90 主持政治经济学中心；手稿存杜克 Rubenstein Library
14  遗产与结尾 — 「制度提供经济的激励结构；随结构演化，经济走向增长、停滞或衰落」+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享奖口径 | 1993 与 **Robert Fogel** 共享、同一句理由（manifest citation 逐字）；诺奖委员会原句见 page.md 首段引文，两篇立传用同一口径 |
| 博士导师口径 | frontmatter doctoral_advisor = **Melvin Moses Knight**（infobox Influence 行作 Melvin M. Knight）；正文未展开——advisor-student 边依 frontmatter/infobox 建立，勿与表兄 Fantius 无关人物混淆 |
| 名字拼写 | Douglass（双 s）；中文名用「道格拉斯·诺思」（manifest name_zh），勿写「诺斯」 |
| 良心拒服兵役者 | page.md 明载 conscientious objector 身份加入商船队（非拒一切服役）——表述精确，勿写成「拒服兵役逃兵」 |
| 哈佛 vs 伯克利 | 被哈佛录取，因父调任西海岸而选伯克利——常被略过的细节，可作早年页趣笔 |
| 华盛顿大学两所 | University of Washington（西雅图，1951-83）≠ Washington University in St. Louis（圣路易斯，1983-）——年份与机构勿串 |
| ISNIE 归属 | page.md 明载 North 与 Coase、Williamson 共同创建 ISNIE、1997 圣路易斯首会；勿写成 North 一人创建 |
| 两类「秩序」 | limited access orders（精英控制、租金提取、抑制增长）vs open access orders（政治控制军队、创造性破坏、增长更稳）——框架归 North/Wallis/Weingast 三人，勿单独归于 North |
| 制度未必有效 | North 强调制度可能因历史约束与政治激励而低效延续（path dependence）——勿把他写成「制度总是促进增长」 |
| 引语红线 | "Institutions provide the incentive structure of an economy..."（page.md 首段英文原文）与诺奖委员会引句可引原文+译文；中文引号内不得出现无原文支撑的「原话」 |
| 门生群像 | 60 周年纪念册名录（Hughes/Sutch/Mercer 等 12 人）是集体致献非逐一明载关系，一律不入库 |
| metadata 噪声 | metadata.json 无异常大项；生卒以正文为准（1920-11-05 / 2015-11-23）；国籍 United States（Nobel/manifest 口径） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| institutions | 制度 | North 定义：人为设计的约束（正式规则 + 非正式约束）；「游戏的规则」 |
| informal constraints | 非正式约束 | 制裁、禁忌、习俗、传统、行为规范 |
| cliometrics | 计量史学 | 经济理论与量化方法进经济史；North/Fogel 共同推广 |
| transaction costs | 交易成本 | North 框架：根植于信息不对称，制度的核心功能是控制它 |
| path dependence | 路径依赖 | 过去的制度选择限制未来可能性；低效制度可长期延续 |
| limited access order | 有限准入秩序 | 精英控制政治经济以提取租金、以垄断维稳（与 Wallis/Weingast 合著框架） |
| open access order | 开放准入秩序 | 政治控制的军队限暴力 + 无人为准入门槛 → 创造性破坏 |
| property rights | 产权 | 《西方世界的兴起》的解释核心：有效率的经济组织 |
| natural state | 自然国家 | 与 Wallis/Weingast 合作研究：国家如何走出「自然状态」进入长期增长 |
| ideology（mental models） | 意识形态/心智模型 | North 1992 框架：决策基于不完全的意识形态；勿译成一般「思想体系」泛化 |
| ISNIE | 国际新制度经济学学会 | 1997 首会；后改名 SIOE，勿混 |
| John R. Commons Award | 康芒斯奖 | 1991 North 是首位获此奖的经济史学家；Omicron Delta Epsilon 设立 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：North 一生的主题是「从黑暗的自然国家走向制度化的光明秩序」——Shine Like The Sun 的上扬史诗感，恰好对应「长期经济变迁中制度逐渐照亮增长路径」的叙事弧线：从商船甲板上的自学者，到把经济史从编年叙事改造成制度科学的世纪学者。
- **本地路径**：复制 `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav` 到 `economics/presentations/20th_century/Douglass_North/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
