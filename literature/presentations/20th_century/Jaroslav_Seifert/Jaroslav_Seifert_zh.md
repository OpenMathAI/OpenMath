# 文学家立传提示词（OpenLiterature：Jaroslav Seifert）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Jaroslav Seifert（1984 诺贝尔文学奖，捷克民族诗人）为执行实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 〇、批次信息 【人物专属】

| 项 | 值 |
|----|----|
| 分批 | `literature/prompt_batches_lit.json` batch 17（agent：lit-batch-17） |
| dir / qid | Jaroslav_Seifert / Q102483 |
| 获奖年份 | 1984 |
| 主色（预分配） | `#8B1A1A` |
| BGM（预分配） | Tragedy |
| page.md | `literature/presentations/pages/20th_century/Jaroslav_Seifert/page.md` |
| prompt / yaml | `literature/presentations/20th_century/Jaroslav_Seifert/Jaroslav_Seifert_zh.md` / `MySQL/data/Jaroslav_Seifert.yaml` |

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆与文学家侧首例（Knut Hamsun 等）的实战经验。
- **本实例**：Jaroslav Seifert（雅罗斯拉夫·塞弗尔特）。
- **设计哲学**：文学家立传与物理学家立传的核心差异，在于**无公式框——用代表作书影、名句引文框、意象图式替代**；且必须保留「身份信息页」（Identity / Bio 速览页）与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Jaroslav Seifert（1901-09-23 ~ 1986-01-10，享年 84 岁）
- **气质关键词**：**捷克民族诗人、布拉格的抒情歌者、从不回头的不屈者** —— 1984 诺贝尔文学奖获奖理由（官方原文 + 中译，禁止改写）：
  > "for his poetry which endowed with freshness, sensuality and rich inventiveness provides a liberating image of the indomitable spirit and versatility of man"
  > （表彰其诗歌，以清新与丰富的独创性呈现出人类不屈精神与多面性的解放形象）
- **设计母题**：**捷克 Lyons 与布拉格的街巷（Žižkov 街区的声音与苹果）**。塞弗尔特的诗歌始终扎根布拉格的市井——苹果、夜莺、钟声、瘟疫柱，是与「民族命运」互为表里的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Jaroslav_Seifert/page.md`（同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Jaroslav_Seifert
- **肖像**：⏳ 第 0 步待下载（images.txt 有 `Jaroslav_Seifert_1931.jpg` 250px 缩略图，建议取 500px 原图；失败则装饰圆占位）
- **参考模板**：
  - 文学家成品参照：`literature/presentations/20th_century/` 下已立传目录（如 Knut_Hamsun）
  - 项目首页模板：`literature/presentations/cover/openliterature_page.tex`（统一 `\input`，以主控实际封面文件为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报进度，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- 生卒：1901-09-23 生于布拉格 Žižkov（时属奥匈帝国）~ 1986-01-10 逝于布拉格（捷克斯洛伐克），享年 84 岁
- 国籍：奥匈帝国（出生时）→ 捷克斯洛伐克；yaml 按库内口径收 Czechoslovakia（page.md frontmatter 为 Czechoslovakia）
- 职业：writer / poet / journalist / translator / essayist / 编辑
- 教育：无大学记载（自学成才，via 新闻界成长）
- 政治轨迹：早年为捷共（KSČ）党员，主编多份共产主义报刊 *Rovnost*、*Sršatec*、*Reflektor*，任职共产主义出版社；**1929-03 与另六位作家签署宣言抗议新领导层布尔什维克化倾向后集体退党**（客观简述，不作政治评价）；1930–40 年代为社会民主党与工会报刊记者；1977 为《七七宪章》联署人之一
- 任职：1949 年离开新闻界专事文学；1968–1970 任捷克斯洛伐克作家协会正式主席
- 关键荣誉：Nobel 1984（因病未出席，**由女儿 Jana 代领**；国控媒体仅简讯提及）；1936/1955/1968 国家奖；1967 获「民族艺术家」（Národní umělec）称号；T. G. Masaryk 一级勋章（frontmatter）
- 逝世与身后：1986-01-10 逝于布拉格，葬于 Kralupy nad Vltavou 家族墓；葬礼现场秘密警察 StB 高度到场、压制悼念者任何异见表示（客观事实，一句带过）
- 核心作品与贡献（4–6 条）：
  1. 《泪城》*Město v slzách*（1921）——首部诗集，无产阶级诗风起点
  2. 《只因为爱》*Samá láska*（1923）等 1920 年代爱情抒情诗——捷克先锋派（Devětsil 创刊人之一）的代表
  3. 《鲍日娜·聂姆曹娃的扇子》*Vějíř Boženy Němcové*（1940）、《泥土的头盔》*Přilba hlíny*（1945）——战时与战后民族抒情
  4. 《妈妈》*Maminka*（1954）——广受爱戴的母题抒情诗集
  5. 《布拉格十四行花环》*Praha a Věnec sonetů*（1956，英译者 Jan Křesadlo）——献给布拉格的十四行花环
  6. 《瘟疫纪念柱》*Morový sloup*（1968–1970）、《世上一切美》*Všecky krásy světa*（1979）、《做一个诗人》*Býti básníkem*（1983）——晚年回忆性与证言性写作
- 关键时间线（约 18 节点）：1901 生于 Žižkov → 1921 首部诗集+入 KSČ → 1920 年代先锋派代表、Devětsil 创刊 → 1923 *Samá láska* → 1925 *Na vlnách TSF* → 1926 *Slavík zpívá špatně* → 1929 三部诗集（*Básně*/*Poštovní holub*/*Hvězdy nad Rajskou zahradou*）→ 1929-03 退党 → 1933 *Jablko z klína* → 1936 国家奖 → 1938 *Zhasněte světla* → 1940 *Vějíř Boženy Němcové*/*Světlem oděná* → 1945 *Přilba hlíny* → 1949 弃新闻专文学 → 1954 *Maminka* → 1955 国家奖 → 1956 *Praha a Věnec sonetů* → 1965 *Zrnka révy*/*Koncert na ostrově* → 1967 民族艺术家 + *Halleyova kometa* → 1968–70 作协主席、*Morový sloup* → 1977 七七宪章 → 1979 *Deštník z Picadilly*/*Všecky krásy světa* → 1983 *Býti básníkem* → 1984 诺贝尔奖（女儿代领）→ 1986-01-10 逝世

### 第 1–3 步：目录、Makefile 与肖像收集 【模板通用】

- 第 1 步：在 `literature/presentations/20th_century/` 下确认/创建 `Jaroslav_Seifert/` 与 `images/`
- 第 2 步：复制邻近已立传目录的 Makefile，改 `MAIN=Jaroslav_Seifert_zh`、`VIDEO_NAME=Jaroslav_Seifert_zh`
- 第 3 步：肖像下载——images.txt 有 URL 直接取（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 则改用 Commons `Special:FilePath` 或 Wikipedia REST API `page/summary` 查 infobox 原图名；仍失败用装饰圆占位，图注注明「肖像暂缺」

### 第 4 步：文学领域梳理 + 入库 【人物专属】

> 把文学领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Seifert 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | czech poetry | 捷克诗歌 | 民族诗人本体，捷克语写作 | 全篇 |
| 1 | avant-garde poetry | 先锋派诗歌 | 1920 年代捷克斯洛伐克艺术先锋派代表人物 | 先锋派页 |
| 2 | love poetry | 爱情抒情诗 | *Samá láska*、*Jablko z klína* 一线 | 抒情页 |
| 3 | civic poetry | 公民诗歌 | 从退党宣言到七七宪章的证言性写作背景 | 宪章页 |
| 4 | Prague in poetry | 诗歌中的布拉格 | *Kniha o Praze*、*Praha a Věnec sonetů* 的城市母题 | 布拉格页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> **只收 page.md 明载关系**；无载禁写（见第 8 步陷阱表）。文学家侧类型白名单：`advisor-student` / `influence` / `colleague` / `co-honored` / `spouse` / `parent-child` / `rival` / `controversy`。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Jana Seifert | 无向 | 女儿，1931 年合影；1984 年因父亲健康原因代赴斯德哥尔摩领奖 |
| colleague | Jan Křesadlo | 无向 | 英译其《Praha a Věnec sonetů》（A Wreath of Sonnets） |

**诚实注记**：Devětsil 同人、1929 共同退党的六位作家、七七宪章其他联署人在 page.md 均**未具名**，一律不入库；本篇 relations=2 为诚实值。

### 第 5 步：设计配色 【人物专属】

- **气质**：市井的暖、布拉格的旧、暮年的克制
- **配色**：主色 `#8B1A1A`（捷克红，预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 捷克诗歌 — 深红 `#8B1A1A`
  - `badgeB` 先锋派诗歌 — 靛蓝 `#4C5FD5`
  - `badgeC` 爱情抒情诗 — 玫瑰 `#C4204F`
  - `badgeD` 公民诗歌 — 琥珀 `#E07B30`
- **背景母题**：苹果与星（稀疏圆点+小体量果实图形），呼应 *Jablko z klína*、*Chlapec a hvězdy* 的意象；避免政治符号。

### 第 6 步：规划幻灯片序列 【人物专属，14 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 捷克民族诗人 / Jaroslav Seifert 1901–1986 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、国籍变迁、职业、任职、荣誉、核心领域）
03  核心创作概览 — 抒情 / 先锋派 / 战时民族诗 / 晚年证言
04  早年：Žižkov 的少年 (1901–1921) — 工人区出身、首部诗集《泪城》
05  先锋派与 Devětsil (1921–1929) — 三份报刊编辑、《只因为爱》
06  1929：退党的诗人 — 七作家宣言、社会民主与工会报刊岁月 (1929–1948)
07  战时抒情：《盲女尼姆科娃的扇子》《泥土的头盔》(1940–1945)
08  代表作页（名句引文框/书影替代公式框）— 《妈妈》(1954) 与《布拉格十四行花环》(1956)
09  1968–1977：作协主席与七七宪章 — 《瘟疫纪念柱》
10  1984 诺贝尔奖 — "freshness, sensuality and rich inventiveness" 引文框；女儿 Jana 代领
11  晚年与逝世 (1983–1986) — 《做一个诗人》；Kralupy 家族墓
12  遗产：布拉格永远的诗
13  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

**Seifert 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 必须用官方原句 "for his poetry which endowed with freshness, sensuality and rich inventiveness provides a liberating image of the indomitable spirit and versatility of man"；中译从 CITATION_ZH 原样取，禁止改写 |
| 女儿代领 | page.md 明载因病未出席、由女儿代领；照片图注只有 "daughter Jana"，**勿编其全名以外的信息**（yaml stub 用 Jana Seifert，勿写生卒） |
| 退党叙事 | 1929 退党只写 page.md 事实（七作家+宣言+抗议布尔什维克化倾向），**不评价、不展开政治叙事**；1977 七七宪章同理 |
| 葬礼细节 | StB 到场压制异见是 page.md 明载事实，一句客观带过，不加渲染 |
| 国家奖年份 | page.md 明载 1936/1955/1968 三次国家奖；1967 是「民族艺术家」称号，勿与国家奖混淆 |
| 无载禁写清单 | 与 Nezval 的师承/决裂、具体恋情、Seifert 与哈维尔的私交、获奖演讲内容（因未出席而无演讲）——page.md 均无载，一律禁写 |
| 同名区分 | 勿与波兰诗人同名混淆；Jan Křesadlo 是捷克流亡作家兼英译者（其《A Wreath of Sonnets》译本），不是诗人本人 |
| 作品年表 | 约 30 部诗集，页面上只列代表作 6–8 部，勿把 *Všecky krásy světa* 的 "1981?" 噪声年份写死（取 1979） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Žižkov | 日日科夫区 | 布拉格工人区，出生地 |
| Devětsil | 德维齐尔（艺术家社团/刊物） | 先锋派团体，勿译成普通杂志 |
| Město v slzách | 《泪城》 | 1921 首部诗集 |
| Samá láska | 《只因为爱》 | 1923，勿译《纯爱》歧义 |
| Přilba hlíny | 《泥土的头盔》 | 1945 战后诗集 |
| Praha a Věnec sonetů | 《布拉格十四行花环》 | 十四行花环诗体（crown of sonnets） |
| Morový sloup | 《瘟疫纪念柱》 | 1968–1970，勿与布拉格实体的瘟疫柱混写 |
| Národní umělec | 民族艺术家 | 1967 荣誉称号 |
| Charter 77 | 七七宪章 | 1977 联署，客观表述 |
| StB | 捷克斯洛伐克秘密警察 | 葬礼背景，一句带过 |

---

### 第 9 步：执行终检清单 【模板通用】

- [ ] 页数与第 6 步序列一致（`pdftoppm` 逐页目检；出 mp4 后核时长）
- [ ] 获奖理由 EN 原句与 CITATION_ZH 中译逐字核对（含标点）
- [ ] 生卒/享年三处一致（封面、身份页、结尾页）
- [ ] 溢出：vbox ≤10pt、hbox ≤50pt；引文框不破行
- [ ] yaml 关系与第 4.5 步表逐行一致；note 无裸冒号/引号头
- [ ] 品牌口径：结尾页底部 `OpenMathAI`，引号半角

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Tragedy** — Alex-Productions（预分配）
- **风格**: 深沉 / 历史感 / 挽歌气质
- **匹配理由**:
  - "历史感" 匹配塞弗尔特贯穿 20 世纪捷克全部动荡的一生 —— 从奥匈帝国的 Žižkov 到七七宪章，诗与国运同构
  - "深沉/挽歌" 匹配暮年诗人气质 —— 《瘟疫纪念柱》《做一个诗人》的证言式低语，胜过任何戏剧高音
  - 曲名 Tragedy 只取其历史纵深，不暗示生平悲剧化 —— 排版与文案保持克制
- **备选** (未采用): ★★ PAST（历史感匹配捷克 20 世纪，但 2026 批次已多处占用）；★ The Flow of Time（时间纵深，受众偏低）
- **本地路径**: `music_audio/alex-productions/` 下 Tragedy 对应 wav（复制到 `literature/presentations/20th_century/Jaroslav_Seifert/Tragedy.wav`）
- **时长**: 以实际文件为准，ffmpeg `-shortest` 自动对齐

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：引语只用 page.md 英文原句；无载禁写；关系表与 yaml 完全一致。**
