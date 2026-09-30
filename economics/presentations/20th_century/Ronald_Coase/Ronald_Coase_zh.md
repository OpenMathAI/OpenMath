# 经济学家立传提示词（Ronald Coase）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1991 年得主 Ronald Coase（罗纳德·科斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Ronald_Coase/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Ronald Harry Coase（1910-12-29 生于伦敦威尔斯登 ~ 2013-09-02 逝于芝加哥，享年 102 岁，葬于芝加哥 Graceland Cemetery）
- **气质关键词**：**交易成本的发现者、产权经济学的奠基人、法律经济学开山者、102 岁的世纪学者**
- **诺奖获奖理由**（1991，独得，manifest citation 逐字）：
  > "for his discovery and clarification of the significance of transaction costs and property rights for the institutional structure and functioning of the economy"（表彰他发现并阐明了交易成本和产权对经济制度结构与运行的重要意义）
- **设计母题**：**契约与摩擦（contracts & friction）**——新古典市场假定零摩擦，科斯的洞见恰是「使用市场本身有成本」：搜寻与信息成本、议价成本、保守商业秘密的成本、监督与履约成本，皆是把交易从市场搬进企业的理由。视觉语言以交错的契约网格、被摩擦线打断的直线交易通道构成背景母题，呼应「企业与市场是可替代的协调机制」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Ronald_Coase/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）
- **一句话画像**：生于伦敦邮局电报员家庭、幼年腿疾戴腿杖进残障学校的少年，靠奖学金读完 LSE；一生只以两篇短文（《企业的性质》1937、《社会成本问题》1960）重塑经济学与法学的交界，81 岁获诺贝尔奖，102 岁辞世，墓志铭里写着他对中国的期待。

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Ronald_Coase/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Ronald_Coase_zh`、`VIDEO_NAME=Ronald_Coase_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。
> 布局检查照模板第 8 步：每写完一页 `make distclean && make`，`pdftoppm` 截图逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

## 三、研究领域梳理 + 入库 【人物专属】

**Coase 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | transaction costs | 交易成本 | 诺奖核心：《企业的性质》(1937) 引入的概念，获奖理由首词 | 封面、核心页 |
| 1 | property rights | 产权 | 《社会成本问题》(1960)：产权界定与外部性、初始权利分配的公平/效率两分 | 核心页 |
| 2 | law and economics | 法律经济学 | 学科核心奠基人；《Journal of Law and Economics》共同主编（1964 起） | 法与经济页 |
| 3 | new institutional economics | 新制度经济学 | 学派奠基人之一；晚年任 Ronald Coase Institute 研究顾问，扶持发展中国家青年学者 | 制度页 |
| 4 | theory of the firm | 企业理论 | 企业为何存在、企业边界的决定、企业家功能收益递减 | 企业页 |

补充说明（供立传 agent 取材）：科斯自述经济学家应像 Adam Smith 一样研究现实世界的财富创造——"It is suicidal for the field to slide into a hard science of choice, ignoring the influences of society, history, culture, and politics on the working of the economy."（原文在 page.md，可引）；他主张减少对价格理论/理论市场的强调，转而研究真实市场。除诺奖外获 AEA Distinguished Fellow、巴黎一大荣誉博士；诺奖演讲题为 "The Institutional Structure of Production"（1992, American Economic Review）。

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marian Ruth Hartung | 无向 | 1937-08-07 于威尔斯登结婚，妻 2012-10-17 先逝；无子女，诺奖得主中婚姻最长者之一（75 年） |
| colleague | Aaron Director | 无向 | 《Journal of Law and Economics》共同主编；1964 因接替 Director 的编辑职位赴芝加哥 |
| colleague | George Stigler | 无向 | 1960 芝加哥研讨会听众；「科斯定理」之名由 Stigler 标定 |
| colleague | Milton Friedman | 无向 | 1960 芝加哥研讨会二十位资深经济学家听众之一 |
| influence | Arnold Plant | 无向 | LSE 选其课与研讨班；科斯自述 Plant 引入「看不见的手」、采纳其许多立场，放弃青年时代社会主义信念 |
| influence | Frank Knight | 无向 | 1931-32 卡塞尔旅行奖学金游学芝加哥，跟从 Knight 学习（非学位导师） |
| influence | Jacob Viner | 无向 | 同期游学芝加哥跟从 Viner 学习（非学位导师） |
| colleague | Abba Lerner | 无向 | LSE 同窗，科斯自述「关系非常友好的优秀理论家」 |
| influence | Oliver E. Williamson | 无向 | 交易成本方法经 Williamson 重新引入现代组织经济学（market and hierarchies） |
| controversy | Arthur Cecil Pigou | 无向 | 1959 FCC 论文引芝加哥学界反对；《社会成本问题》论证庇古分析有误（牧场-农田例） |
| collaborator | Ning Wang | 无向 | 合著《How China Became Capitalist》(2012)，起于其近百岁时对中国越南经济兴起的研究 |

**不入库但提示词可叙述**：R.F. Fowler（1930s 猪周期论文合作者，仅见于文献列表，无正文关系叙述）；Richard Sandor（仅 2008 合影图注，无持续关系记载）；Coase-Sandor Institute / Ronald Coase Institute / Philadelphia Society（机构任职不建人物边）；父亲 Henry Joseph Coase 与母亲 Rosalie Elizabeth Coase（邮局电报员背景，仅生平叙述）；Norman Churchill/政府部门的战时经历（事件非关系）。

## 五、配色方案 【人物专属】

- **气质**：沉稳、契约感、跨越百年的制度洞察
- **主色**：`#7E1E23`（manifest 预分配，深绛红——契约墨色与芝加哥学派的暗红气质）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTC` 交易成本 — 深绛红 `#7E1E23`
  - `badgePR` 产权 — 深海蓝 `#1E3A5F`
  - `badgeLE` 法律经济学 — 琥珀 `#C07A2A`
  - `badgeNIE` 新制度经济学 — 青绿 `#0E7C7B`
- **背景母题**：契约网格与摩擦线（细网格上若干被斜线打断的直线通道），呼应「使用市场本身有成本」的核心洞见；共享封面版式按 `economics/presentations/cover/` 统一口径（品牌标注 OpenMathAI）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex，品牌口径 OpenMathAI）
01  封面 — 交易成本的发现者 / Ronald Coase 1910–2013 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒（1910-12-29 Willesden ~ 2013-09-02 Chicago，享年 102）、
    教育（LSE BCom 1932 / 伦敦大学 DSc 1951）、任职（Dundee 1932-34 → Liverpool 1934-35 → LSE 至 1951 →
    Buffalo → Virginia 1958 → Chicago 1964 终老，Clifton R. Musser 教席）、配偶 Marian 1937、诺奖 1991
03  核心贡献概览 — 交易成本 / 产权与科斯定理 / 法律经济学 / 企业理论（四 badge 横排）
04  早年与腿疾 (1910–1932) — 威尔斯登；父辈皆邮局电报员；腿疾戴腿杖入残障学校；
    12 岁凭奖学金入 Kilburn Grammar School；1927-29 伦敦大学校外生课程
05  LSE 与游学芝加哥 (1931–1935) — Plant 的课与研讨班（引入看不见的手、转向竞争体制信念）；
    Cassel 旅行奖学金 1931-32 访芝大听 Knight/Viner；1932 BCom；Dundee/Liverpool 助讲
06  《企业的性质》1937（核心贡献页）— 「生产可以完全在无组织中展开，为何还有企业？」：
    交易成本概念首秀，企业内部化的经济逻辑
07  交易成本的机制 — 搜寻与信息成本、议价成本、保守商业秘密、监督与履约；
    企业规模的自然极限：企业家功能收益递减、管理失误倾向
08  公用事业与广播垄断 (1935–1950) — 1935 年起在 LSE 接手公用事业经济学课程；
    水电气/邮局/广播历史研究；《British Broadcasting: A Study in Monopoly》(1950)；
    战时先后任职林业委员会与战时内阁中央统计局
09  弗吉尼亚与 FCC 论文 (1958–1959) — 1958 赴弗吉尼亚；1959《The Federal Communications Commission》
    频率定价之议引芝大教员反对；与庇古分析的表面冲突
10  《社会成本问题》1960（核心贡献页）— 牧场-农田例：无交易成本则初始产权分配不影响效率；
    正交易成本下产权与法律成为经济绩效的决定因素
11  芝加哥研讨会与科斯定理 — 1960 研讨会说服二十位资深经济学家（含 Stigler、Friedman），
    后世称为芝大法经济学创生的「范式转变时刻」；定理之名由 Stigler 标定；1990 自述担心被误解
12  芝加哥岁月与法律经济学 (1964–2013) — 与 Aaron Director 共同主编 JLE；Simons Lecture 的两部分界定；
    科斯猜想（1972 耐用品垄断）；《The Lighthouse in Economics》(1974)；芝大法学院 2003 照
13  荣誉与遗产 — Nobel 1991（演讲 The Institutional Structure of Production）；AEA 杰出会士；
    巴黎一大荣誉博士；Buffalo 2012 荣誉博士；Coase-Sandor Institute 传承
14  中国之书与结尾 — 百岁前后著《How China Became Capitalist》(2012, 与 Ning Wang)；
    墓志铭原文收束："Devoted husband and single-minded economist, whose ideas have inspired the
    great transformation of China and will continue to inspire our inquiry into the nature and
    causes of the wealth of nations." + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 享年与卒年 | 1910-12-29 ~ 2013-09-02，享年 **102 岁**；逝于芝加哥，与妻合葬 Graceland Cemetery；勿写"近百岁"模糊化 |
| 国籍口径 | yaml 按 manifest 填 **United Kingdom**；page.md 明载 1950 年代移居美国后**保留英国国籍**（retained his British citizenship），勿写"入籍美国" |
| 无子女 | 与 Marian Ruth Hartung 结婚 75 年、无子女，page.md 明载 "one of the longest-married Nobel Prize laureates"；勿杜撰后代 |
| 学位口径 | LSE 商学士 1932 + 伦敦大学 **DSc 1951**（earned doctorate）；无 PhD 论文与博士导师，勿编造 advisor 关系 |
| 《社会成本问题》发表地 | 1960 发表时科斯在 **弗吉尼亚大学** 经济系（正文明载），1964 才定居芝加哥；勿写成"在芝大期间发表" |
| 科斯定理命名 | "This seminal argument forms the basis of the famous Coase theorem **as labelled by Stigler**"——定理之名出自 Stigler；科斯 1990 自述担心该文被广泛误解，可叙述 |
| 1931-32 游学 | Cassel 奖学金访芝大 "studying with Frank Knight and Jacob Viner"——**非学位导师**，入库用 influence；且正文明载芝大同仁后来"不记得这次访问"，叙述时保留此趣笔 |
| Pigou 关系 | 学术争论（controversy）：1959 FCC 论文引芝大教员反对；科斯自述在芝加哥会议上"证明自己正确、庇古分析有误"（英文原文在 page.md）；勿写成师生或私交 |
| 政治底色 | 早年社会主义者，1931 Plant 研讨班后逐步转变；正文明载其政治自述 "I really don't know"——叙述克制、忠于原文，勿贴意识形态标签 |
| 引语红线 | page.md 有英文原文的引语（"It is suicidal for the field..."、Simons Lecture 各段、政治自述、墓志铭全文）可引原文+译文；中文引号内不得出现无原文支撑的"原话" |
| 墓志铭 | 结尾页可整句引原文（见第六节 14 页规划），点明其思想与中国转型、与《国富论》追问的呼应即可，勿引申政治评价 |
| 中国之书 | 2012 与 **Ning Wang** 合著《How China Became Capitalist》，源自其百岁前对中国越南经济兴起的研究与 Coase China Society 愿景；Buffalo 经济系 2012-05 授荣誉博士；只写 page.md 事实 |
| metadata 噪声 | metadata.json 国籍含 "United Kingdom of Great Britain and Ireland"（历史政权口径）、职业含 historian 等，以正文/manifest 的 United Kingdom 为准；获奖理由以 manifest citation 逐字为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| transaction costs | 交易成本 | 搜寻、议价、保守秘密、监督与履约成本总称；获奖理由核心词 |
| property rights | 产权 | 零交易成本下初始分配只涉公平/收入分配，不涉效率 |
| Coase theorem | 科斯定理 | 零（低）交易成本下谈判达帕累托有效，与初始产权分配无关；名称出自 Stigler |
| Coase conjecture | 科斯猜想 | 耐用品垄断者因无法承诺未来不降价而丧失市场势力（1972）；勿与定理混写 |
| theory of the firm | 企业理论 | 《企业的性质》(1937)：企业 vs 市场两种协调机制 |
| externality | 外部性 | page.md 标准例是牧场牛群踩踏农田，勿替换成工业污染例 |
| law and economics | 法律经济学 | 科斯界定的两部分：用经济学分析法律系统 + 研究法律系统对经济运行的影响（其自称对后者更感兴趣） |
| new institutional economics | 新制度经济学 | 科斯 1984 年有同名论文；与 Williamson、North 共同奠基的学派脉络 |
| The Nature of the Firm | 《企业的性质》 | 1937；勿与 1960《社会成本问题》年份互换 |
| The Problem of Social Cost | 《社会成本问题》 | 1960；JLE 3(1): 1-44 |
| marginal cost controversy | 边际成本论战 | 1946-47 两篇 Economica 论文，可作时间线节点 |
| durable goods monopolist | 耐用品垄断者 | 科斯猜想的主语，勿写成"所有垄断者" |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：交易成本的本质是「市场并非无摩擦运转」——"Falling Apart" 的意象恰好对应**无制度约束时协调的解体**：企业出现是为了内部化这些成本，产权界定是为了让谈判免于崩溃；曲目的电子质感与克制张力，也贴合一位以两篇短文重塑整个学科、却始终冷静自持、活到 102 岁的世纪学者。
- **本地路径**：复制 `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` 到 `economics/presentations/20th_century/Ronald_Coase/FallingApart.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
