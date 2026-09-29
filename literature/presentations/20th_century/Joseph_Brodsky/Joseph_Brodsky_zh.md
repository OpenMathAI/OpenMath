# 文学家立传提示词（OpenLiterature：Joseph Brodsky）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Joseph Brodsky（1987 诺贝尔文学奖，俄裔美国诗人）为执行实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 〇、批次信息 【人物专属】

| 项 | 值 |
|----|----|
| 分批 | `literature/prompt_batches_lit.json` batch 17（agent：lit-batch-17） |
| dir / qid | Joseph_Brodsky / Q862 |
| 获奖年份 | 1987 |
| 主色（预分配） | `#4E342E` |
| BGM（预分配） | Cinematic Experience |
| page.md | `literature/presentations/pages/20th_century/Joseph_Brodsky/page.md` |
| prompt / yaml | `literature/presentations/20th_century/Joseph_Brodsky/Joseph_Brodsky_zh.md` / `MySQL/data/Joseph_Brodsky.yaml` |

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆与文学家侧首例（Knut Hamsun 等）的实战经验。
- **本实例**：Iosif Aleksandrovich Brodsky（约瑟夫·布罗茨基，Иосиф Бродский）。
- **设计哲学**：文学家立传无公式框——用**诗集书影、名句引文框、水域意象图式**替代；保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Joseph Brodsky（1940-05-24 ~ 1996-01-28，享年 55 岁）
- **气质关键词**：**从列宁格勒到纽约的俄语诗人、英语世界的散文大家、诗歌人类学的布道者** —— 1987 诺贝尔文学奖获奖理由（官方原文 + 中译，禁止改写）：
  > "for an all-embracing authorship, imbued with clarity of thought and poetic intensity"
  > （表彰其包罗万象的写作，充满思想的清明与诗性的强度）
- **设计母题**：**水（从涅瓦河到威尼斯）**。波罗的海锌灰色的浪（*A Part of Speech* 首诗）→ 列宁格勒围城 → 流亡航线 → 威尼斯《Watermark》与圣米凯莱墓岛——水域是贯穿其一生地理与诗学的视觉主线。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Joseph_Brodsky/page.md`（同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Joseph_Brodsky
- **肖像**：⏳ 第 0 步待下载（images.txt 有 `Josef_Brodsky.jpg` 330px（Michigan 讲课照），建议取 500px 原图；失败则装饰圆占位）
- **参考模板**：
  - 文学家成品参照：`literature/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`literature/presentations/cover/`（以主控实际封面文件为准）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- 生卒：1940-05-24 生于列宁格勒（今圣彼得堡）~ 1996-01-28 逝于纽约布鲁克林高地家中（心脏病；1979 心脏手术、后两次搭桥，长期体弱），享年 55 岁。**裁定**：卒日取 1996-01-28（正文与 infobox 一致；frontmatter 双值 "1996-01-25" 为噪声）
- 国籍：苏联（1940–72）→ **无国籍（1972–77）** → 美国（1977–96），三分段必须写全
- 家庭：俄国犹太家庭，拉比世家 Schorr（Shor）后裔（直系先祖 Joseph ben Isaac Bekhor Shor）；父 Aleksandr 为苏联海军摄影师，母 Maria Volpert 为职业口译；住公共公寓、贫困；幼年经历**列宁格勒围城**，险些饿死
- 教育：15 岁辍学；曾想当医生、在 Kresty 监狱停尸房做工；铣工/锅炉房/地质勘探队等多工；**完全自学**——学波兰语为译米沃什，学英语为译约翰·多恩；自学古典哲学、神话、英美诗歌（educated_at 的 Annenschule/Clare Hall 为 frontmatter 口径，正文无大学学历记载，tex 以「无大学学历」呈现）
- 文学起点：1955 开始写诗，地下刊物 *Sintaksis*；1958 以《列宁格勒近郊的犹太墓地》《朝圣者》闻名文学圈；1959 雅库茨克书店读 Baratynsky 的自述「使命时刻」
- 师承：**1960 结识 Anna Akhmatova，受其鼓励并成为其门生（mentor）**（"Akhmatova's Orphans" 群体）
- 迫害与流亡（客观简述，不作政治评价）：1963 诗作被报界点名；1964 以「社会寄生」受审判五年苦役，服 18 个月（阿尔汉格尔斯克州 Norenskaya 农场——自传笔下的黄金岁月，夜读 Auden/Frost）；1965 因 Akhmatova、Evtushenko、Shostakovich、Sartre 等声援改判获释；**1972-06-04 被强行送上飞机驱逐出境（维也纳），此后终生未回俄罗斯**
- 美国：Auden 与 Proffer 协助定居安阿伯，Michigan 驻校诗人一年 → Queens College（1973–74）/Smith/Columbia/剑桥 → Michigan（1974–80）→ **Mount Holyoke College Andrew Mellon 讲席教授、Five College 文学教授**；1980 迁格林尼治村
- 关键荣誉：Nobel 1987（第五位俄裔得主）；1978 Yale 荣誉文学博士；1979 美国艺术暨文学学会会员；1981 MacArthur「天才奖」；1986 全美书评人协会评论奖（*Less Than One*）+ 牛津荣誉博士；1991 美国桂冠诗人 + Struga 金冠奖
- 核心作品与贡献（4–6 条）：
  1. *A Part of Speech*（1980）——英语世界代表诗集（Hecht/Moss/Walcott/Wilbur 译笔汇萃）
  2. *Less Than One: Selected Essays*（1986）——英语散文集，全美书评人协会评论奖
  3. *Watermark*（1992）——威尼斯散文沉思
  4. *To Urania*（1988）、*So Forth*（1996）、*Nativity Poems*——诗歌序列
  5. 剧作 *Marbles*（1989，与 Alan Myers 合译）
  6. 俄语写作贯穿终生（*Novye stansy k Avguste* 献 M.B. 诗 1962–1982 等）；「诗歌是人类学/遗传学的目标」的诗歌本体论
- 晚年与身后：1990 在法国教书时与 Maria Sozzani 结婚，1993 女儿 Anna 出生；1996-01-28 逝世；葬威尼斯圣米凯莱墓岛（与 Pound、Stravinsky 为邻）；1997 圣彼得堡故居纪念牌；挚友 Derek Walcott 在《The Prodigal》（2004）中悼念
- 关键时间线（约 18 节点）：1940 生于列宁格勒 → 围城幸存 → 15 岁辍学做工 → 1955 开始写诗 → 1958 两诗成名 → 1959 Baratynsky 时刻 → 1960 结识 Akhmatova → 1962 相识 Basmanova → 1963 诗作被点名 → 1964 受审判苦役、服 18 个月 → 1965 声援获释、首部诗集华盛顿出版 → 1967 子 Andrei 出生 → 1970 *A Stop in the Desert* → 1972-06-04 驱逐出境（维也纳）→ 1972–80 安阿伯/各校任教 → 1978 Yale 荣誉博士 → 1979 美国艺术暨文学学会 → 1981 MacArthur → 1986 *Less Than One* 获奖 → 1987 诺贝尔奖 → 1990 与 Maria Sozzani 结婚 → 1991 美国桂冠诗人 → 1996-01-28 逝于纽约

### 第 1–3 步：目录、Makefile 与肖像收集 【模板通用】

- 第 1 步：在 `literature/presentations/20th_century/` 下确认/创建 `Joseph_Brodsky/` 与 `images/`
- 第 2 步：复制邻近已立传目录的 Makefile，改 `MAIN=Joseph_Brodsky_zh`、`VIDEO_NAME=Joseph_Brodsky_zh`
- 第 3 步：肖像下载——images.txt 有 URL 直接取（330px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 则改用 Commons `Special:FilePath` 或 Wikipedia REST API `page/summary` 查 infobox 原图名；仍失败用装饰圆占位，图注注明「肖像暂缺」

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Russian poetry | 俄语诗歌 | 「俄语诗人」的自我认同；俄语诗集贯穿终生 | 诗歌页 |
| 1 | English essays | 英语散文 | 「英语散文家」——*Less Than One*/*On Grief and Reason* | 散文页 |
| 2 | exile literature | 流亡文学 | 1972 驱逐后的写作母题：记忆/家园/丧失 | 流亡页 |
| 3 | literary translation | 文学翻译 | 自译（俄↔英）+ 与名诗人译者合作 | 翻译页 |
| 4 | poetics | 诗学 | 「诗歌是人类学的、遗传学的目标」的诗歌本体论 | 诗学页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Anna Akhmatova | direction: advisor | 1960 相识的文学导师（mentor），Akhmatova's Orphans 群体 |
| influence | John Donne | direction: 影响者 | 自学英语为译多恩；明载受玄学派诗 deep influence（自 Donne 至 Auden） |
| colleague | W. H. Auden | 无向 | 1972 协助其定居美国、为《Selected Poems》作序、署名传统抒情诗人 |
| colleague | Carl Ray Proffer | 无向 | 维也纳接洽、Michigan 同事、Ardis 出版社俄语作品出版人 |
| spouse | Maria Sozzani | 无向 | 1990 年结婚，1993 女儿 Anna 出生 |
| colleague | Czesław Miłosz | 无向 | 自学波兰语以译其诗 |
| colleague | Derek Walcott | 无向 | 挚友；为其诗作翻译并在《The Prodigal》（2004）中悼念 |
| colleague | Octavio Paz | 无向 | 多篇作品题献对象 |
| colleague | Robert Lowell | 无向 | 作品题献对象 |
| colleague | Tomas Venclova | 无向 | 作品题献对象 |
| controversy | Dmitri Bobyshev | 无向 | 挚友因 Basmanova 反目，被广泛认为告发布罗茨基致其 1964 受审 |

**诚实注记**：Marina Basmanova（1962–67 伴侣、M.B. 诗的献身者）与 Maria Kuznetsova 为 page.md 明载伴侣，但关系类型白名单无对应类型（非 spouse），**不入库**，tex 中以文字呈现；Evtushenko/Shostakovich/Sartre（声援者）为一次性事件，不入库。

### 第 5 步：设计配色 【人物专属】

- **气质**：波罗的海的锌灰、威尼斯的暮金、纽约的冷峻
- **配色**：主色 `#4E342E`（预分配深褐）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 俄语诗歌 — 深褐 `#4E342E`
  - `badgeB` 英语散文 — 靛蓝 `#3A5A7A`
  - `badgeC` 流亡文学 — 铁灰 `#5A6B75`
  - `badgeD` 诗学 — 玫瑰 `#C4204F`
- **背景母题**：横向水纹细线（涅瓦河→大西洋→潟湖）+ 稀疏雨点圆；引文框首选《A Part of Speech》首句 "I was born and grew up in the Baltic marshland..." 与《Six Years Later》（Wilbur 译）。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 从涅瓦河到纽约 / Joseph Brodsky 1940–1996 + 四色 badge + 右上头像 + 国籍三分段行
02  身份信息页（★ 必做）— 生卒、国籍三分段、犹太家庭、无大学学历、师承 Akhmatova、任职、荣誉、核心领域
03  核心创作概览 — 俄语诗 / 英语散文 / 流亡写作 / 翻译 / 诗学
04  早年：围城与自学 (1940–1955) — 列宁格勒围城、15 岁辍学、停尸房与锅炉房、多恩与米沃什
05  诗歌起点 (1955–1960) — Sintaksis、两诗成名、Baratynsky 时刻
06  Akhmatova 门下 (1960–1962) — mentor 关系、Akhmatova's Orphans
07  受审与苦役 (1963–1965) — 「社会寄生」审判、Norenskaya 18 个月（客观简述）
08  1972：驱逐出境 — 维也纳中转、Auden 与 Proffer、终生不归（引文框：《The End of a Beautiful Era》节选）
09  美国：讲席岁月 (1972–1991) — 安阿伯/Mount Holyoke/Mellon 教授
10  代表作页：《Less Than One》（1986）与《A Part of Speech》（引文框替代公式框）
11  诗学：诗歌作为人类学的目标 — 桂冠诗人演讲引文框
12  荣誉与认可 — MacArthur 1981 · NBCC 1986 · Nobel 1987 · 桂冠诗人 1991
13  1987 诺贝尔奖 — citation 官方原句引文框；「俄语诗人、英语散文家、美国公民」的自答
14  威尼斯与身后 — *Watermark*、圣米凯莱墓岛、Walcott 悼念
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

**Brodsky 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方原句 "for an all-embracing authorship, imbued with clarity of thought and poetic intensity"；中译从 CITATION_ZH 原样取，禁止改写 |
| 卒日噪声 | frontmatter 双值（01-28/01-25），**取 1996-01-28**（正文+infobox 一致），tex 单一口径 |
| 流亡表述 | 「被驱逐/被『强烈建议』出境」按 page.md 原文客观呈现；围城、审判、苦役一句带过，**不评价苏联、不展开政治叙事**；乌克兰诗争议（时政）禁写 |
| 国籍三分段 | Soviet Union (1940–72) / Stateless (1972–77) / United States (1977–96)，三段并列勿合并为「俄裔美国人」一笔带过 |
| 身份自答 | 诺贝尔访谈自答 "I'm Jewish; a Russian poet, an English essayist – and, of course, an American citizen" 是唯一身份定位句，可直接引用 |
| Akhmatova 关系 | 「mentor/protégé」明载 → advisor-student（direction: advisor）；勿拔高为学院导师，也勿降格为纯影响 |
| Basmanova | 伴侣与 M.B. 诗系列是生平重要线索，但**非 spouse**——tex 文字呈现、不入库关系；子 Andrei 1967 生、随母姓，一句带过 |
| 教育口径 | 无大学学历（自学成才）必须明写；勿从 Clare Hall（剑桥访问）反推学历 |
| 教职清单 | Michigan/Mount Holyoke（Mellon 讲席）为主线，Queens/Smith/Columbia/Cambridge 系访问，勿堆砌 |
| 无载禁写清单 | 与布罗茨基基金会的细节、1996 死因诊断细节（只写心脏病发作）、政治评论类言论——禁写 |
| 同名区分 | 页面英文 Josep/Josip/Josef 拼写变体见 Notes；中译固定「约瑟夫·布罗茨基」 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| A Part of Speech | 《言语的一部分》 | 1980 英语诗集 |
| Less Than One | 《小于一》 | 1986 散文集，通行译名 |
| Watermark | 《水印》 | 1992 威尼斯散文 |
| To Urania | 《致乌拉尼亚》 | 1988 诗集 |
| social parasitism | 社会寄生罪 | 1964 罪名，客观引用 |
| samizdat | 萨米兹达特（地下出版物） | 地下流通 |
| Akhmatova's Orphans | 阿赫玛托娃的孤儿们 | 门生群体名 |
| US Poet Laureate | 美国桂冠诗人 | 1991 |
| Struga Golden Wreath | 斯特鲁加金冠奖 | 1991 |
| Isola di San Michele | 圣米凯莱墓岛 | 威尼斯葬地 |

---

### 第 9 步：执行终检清单 【模板通用】

- [ ] 页数与第 6 步序列一致（`pdftoppm` 逐页目检；出 mp4 后核时长）
- [ ] 获奖理由 EN 原句与 CITATION_ZH 中译逐字核对（含标点）
- [ ] 生卒/享年三处一致（封面、身份页、结尾页；卒日统一 1996-01-28）
- [ ] 溢出：vbox ≤10pt、hbox ≤50pt；引文框不破行
- [ ] yaml 关系与第 4.5 步表逐行一致；note 无裸冒号/引号头
- [ ] 品牌口径：结尾页底部 `OpenMathAI`，引号半角

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Cinematic Experience** — Alex-Productions（预分配）
- **风格**: 电影感 / 叙事性 / 时空流转
- **匹配理由**:
  - "电影感" 匹配其一生的地理跨度 —— 列宁格勒→维也纳→安阿伯→纽约→威尼斯，天然的多幕剧结构（2018 传记片《Dovlatov》、2008《A Room and a Half》皆以其为主角）
  - "叙事性" 匹配其散文的沉思独白 —— 《Watermark》本就是献给城市的影像化写作
  - 避开本批已用曲（Tragedy/With Me/Eternals/New Lands），无撞曲
- **备选** (未采用): ★★ The Flow of Time（时间隐喻直配，但受众偏低）；★ Lonesome（流亡孤独感直配，情绪过单一，弱于多幕电影结构）
- **本地路径**: `music_audio/alex-productions/` 下 Cinematic Experience 对应 wav（复制到 `literature/presentations/20th_century/Joseph_Brodsky/Cinematic Experience.wav`）
- **时长**: 以实际文件为准，ffmpeg `-shortest` 自动对齐

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：引语只用 page.md 英文原句；无载禁写；流亡/苏联经历客观简述不评价；关系表与 yaml 完全一致。**
