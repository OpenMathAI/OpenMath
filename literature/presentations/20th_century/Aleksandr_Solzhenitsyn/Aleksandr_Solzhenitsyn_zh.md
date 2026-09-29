# 文学家立传提示词（OpenLiterature · Aleksandr Solzhenitsyn）

> **目标项目**：OpenLiterature —— 开放文学史（与 OpenPhysicist/OpenChemist 共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Aleksandr Isayevich Solzhenitsyn（亚历山大·伊萨耶维奇·索尔仁尼琴，1970 诺贝尔文学奖）。
> **设计哲学**：文学家立传沿用「身份信息页 + 结构化研究领域」骨架；本篇无公式框，以**代表作书影/名句引文框/意象图式**替代。

---

## 一、模板定位

- **目标人物**：Aleksandr Solzhenitsyn（亚历山大·索尔仁尼琴），1970 年诺贝尔文学奖得主。
- **一句话定位**：以劳改营亲历与道德力量重建俄罗斯文学传统的苏联/俄罗斯作家、历史学家与持不同政见者。
- **适配说明**：物理学家的「公式框」在本篇一律替换为「名句引文框」（仅用 page.md 英文原文，见第 7–8 步红线）。

---

## 二、背景信息 【人物专属】

- **姓名**：Aleksandr Isayevich Solzhenitsyn（Александр Исаевич Солженицын）；中文通译 亚历山大·索尔仁尼琴。
- **生卒**：1918-12-11 生于基斯洛沃茨克（Kislovodsk，俄罗斯苏维埃联邦）～ 2008-08-03 逝于莫斯科近郊，享年 89 岁，死因心力衰竭，葬于莫斯科顿斯科伊修道院（Donskoy Monastery，本人自选墓址）。
  - ⚠️ metadata 生卒日期含 "1918-01-01/2008-01-01" 噪声值，以正文 12-11/08-03 为准。
- **获奖**：1970 年诺贝尔文学奖。官方获奖理由（EN 原文，禁止改写）：
  > "for the ethical force with which he has pursued the indispensable traditions of Russian literature"
  > 中译（名录 CITATION_ZH）：「表彰其追求俄罗斯文学不可或缺的传统时所体现的道德力量」。
  - 当时未赴斯德哥尔摩领奖（担心无法返苏），1974 年被驱逐后于当年颁奖礼受奖；1970-12-10 演讲以书面形式提交，未现场宣读。
- **气质关键词**：**劳改营的见证者、俄罗斯文学良知的化身、流亡中的编年史家**。
- **设计母题**：**群岛与铁丝网（Archipelago & Barbed Wire）**——散落雪原的岛屿链呼应《古拉格群岛》书名与「群岛即国家」的隐喻；铁丝网、雪原、蜡烛光可作为贯穿背景的稀疏装饰元素。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Aleksandr_Solzhenitsyn/page.md`（Wikipedia 全文，已核对）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL：https://en.wikipedia.org/wiki/Aleksandr_Solzhenitsyn
- **肖像**：第 0 步待下载（page.md 内嵌 RIAN archive 1974 年照等，可用 infobox 照）。

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准（已核对 page.md，禁止再杜撰）

- **家庭**：父 Isaakiy Semyonovich Solzhenitsyn（帝俄军官，哥萨克出身），1918-06 在亚历山大出生前死于打猎事故；母 Taisiya Zakharovna（娘家姓 Shcherbak，乌克兰裔）独自抚养，1944 去世；家产 1930 年被并入集体农庄。
- **教育**：罗斯托夫国立大学数学与物理；同时函授莫斯科哲学、文学与历史学院课程。本人自述在被判入营前从未质疑国家意识形态。
- **服役与被捕**：二战红军炮兵上尉（声测炮兵连指挥官），两度受勋（1944-07-08 红星勋章）；1945-02 在东普鲁士被 SMERSH 逮捕，罪名是与友人 Nikolai Vitkevich 私下通信批评斯大林，1945-07-07 被判劳改营 8 年。
- **服刑与流放**：先入普通劳改营 → 萨拉什卡（sharashka 特种科研所，结识 Lev Kopelev，《第一圈》列夫·鲁宾原型）→ 1950 起 Ekibastuz 特别营（矿工/砖匠，《伊万·杰尼索维奇的一天》素材）→ 1953-03 期满后终身流放哈萨克 Birlik 村；癌症未确诊恶化，1954 获准在塔什干治疗缓解（《癌症楼》素材）。狱中凭记忆写诗（Prussian Nights、The Trail）。
- **婚姻与子女**：1940-04-07 与 Natalia Alekseyevna Reshetovskaya 结婚，1952 离婚（劳改营家属处境所迫），1957 复婚，1972 再离；1973 与数学家 Natalia Dmitrievna Svetlova 结婚；三子 Yermolai(1970)、Ignat(1972)、Stepan(1973)，均为美国公民；Ignat 为钢琴家与指挥家。
- **发表与封杀**：1960 向《新世界》主编 Aleksandr Tvardovsky 提交《伊万·杰尼索维奇的一天》，1962 经赫鲁晓夫首肯刊出，轰动一时；1963 《玛特廖娜的家》等三短篇（苏联时期最后发表作品，直到 1990）；1966 《癌症楼》、1968 《第一圈》（国外出版）；1965 KGB 抄走手稿；1969 被作协作协开除；1973 《古拉格群岛》（1958–1967 写成，三卷七部，256 名前囚犯证词，售逾三千万册、35 种语言）。
- **流亡**：1974-02-12 被捕次日驱逐至法兰克福并剥夺苏联国籍 → 借住海因里希·伯尔（Heinrich Böll）Langenbroich 家 → 苏黎世 → 1976 佛蒙特 Cavendish（此前斯坦福/胡佛研究所暂居）；1978-06-08 哈佛毕业典礼演讲；1990 国籍恢复，1994-05 经海参崴乘火车横穿西伯利亚返俄，定居莫斯科西郊 Troitse-Lykovo；1995 电视节目停播后深居简出。
- **关键荣誉**：Nobel 1970；Templeton Prize 1983；Lomonosov Gold Medal 1998；1998 拒绝受圣安德烈勋章（自述理由）；State Prize of the Russian Federation 2007；International Botev Prize 2008；Harvard 荣誉文学博士 1978、Holy Cross 学院荣誉博士 1984。
- **关键时间线（16 节点）**：1918 基斯洛沃茨克出生 → 1936 起构思《1914 年 8 月》素材 → 1941-45 红军声测炮兵连长、两度受勋 → 1945-02 被捕、7 月判 8 年 → 1947-52 狱中默写《The Trail》与 28 首诗 → 1950-53 Ekibastuz 特别营 → 1953-56 哈萨克终身流放 → 1954 塔什干治病 → 1956 平反、白天教书夜间秘密写作 → 1962 《一天》经赫鲁晓夫批准刊出 → 1966-68 《癌症楼》《第一圈》国外出版 → 1969 开除出作协 → 1970 诺贝尔文学奖（未亲领）→ 1973-12 《古拉格群岛》巴黎出版 → 1974-02 驱逐出境 → 1976-94 佛蒙特隐居写作《红轮》→ 1994 返俄 → 2008-08-03 逝世。

### 第 4 步：文学领域表（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gulag literature | 劳改营文学 | 《伊万·杰尼索维奇的一天》《古拉格群岛》 | 核心页 |
| 1 | dissident literature | 持不同政见写作 | 《致苏联领袖们的信》《橡实与牛犊》 | 封杀页 |
| 2 | epic historical fiction | 史诗性历史小说 | 《红轮》（August 1914 等） | 红轮页 |
| 3 | autobiographical fiction | 自传性小说 | 《癌症楼》《第一圈》皆取自身经历 | 病房页 |
| 4 | political essay writing | 政论随笔 | 哈佛演讲、《重建俄国》 | 流亡页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致，仅收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Natalia Alekseyevna Reshetovskaya | 无向 | 1940 结婚，1952 与 1972 两度离婚 |
| spouse | Natalia Dmitrievna Svetlova | 无向 | 1973 结婚，数学家 |
| parent-child | Ignat Solzhenitsyn | 无向 | 次子，钢琴家与指挥家 |
| colleague | Aleksandr Tvardovsky | 无向 | 《新世界》主编，1962 力促《一天》刊出 |
| colleague | Lev Kopelev | 无向 | 萨拉什卡狱中相识，《第一圈》人物原型 |
| colleague | Arnold Susi | 无向 | 卢比扬卡狱中结识，手稿藏于爱沙尼亚 |
| colleague | Mstislav Rostropovich | 无向 | 挚友并收容庇护，因声援而被迫流亡 |
| colleague | Heinrich Böll | 无向 | 1974 流亡首站借住其 Langenbroich 家中 |
| colleague | Nikolai Vitkevich | 无向 | 战时友人，私下通信成为 1945 被捕主因 |

> 三子中仅 Ignat 入库（有独立词条且 infobox 链接）；Yermolai/Stepan 仅具名不入库。涉苏经历只按 page.md 客观简述，不作政治评价。

### 第 5 步：配色方案

- **主色**（预分配）：深靛蓝 `#2A4B7C`（凛冽的北方群岛意象）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeGulag` 劳改营文学 — 冷灰蓝 `#5B7085`
  - `badgeDissident` 持不同政见写作 — 铁锈红 `#8C3B2E`
  - `badgeEpic` 史诗历史小说 — 暗金 `#B08A3E`
  - `badgeExile` 流亡政论 — 苔原绿 `#4E6B5A`
- **背景母题**：稀疏雪原上散落的实心圆（群岛意象），辅以细铁丝网线段装饰。

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 俄罗斯文学的道德力量 / Aleksandr Solzhenitsyn 1918–2008 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/国籍变迁/教育/服役/婚姻/荣誉/核心领域）
03  核心贡献概览 — 劳改营文学 / 持不同政见写作 / 史诗历史小说 / 政论随笔
04  早年：寡母与数理少年 (1918–1941) — 父早亡、东正教家庭、罗斯托夫大学数学物理
05  战争与被捕 (1941–1945) — 声测炮兵连长、红星勋章、SMERSH 逮捕与 8 年判决
06  群岛八年：萨拉什卡与 Ekibastuz (1945–1953) — Kopelev、狱中默诗、《一天》素材
07  流放与重生 (1953–1956) — 哈萨克流放、塔什干治疗、信仰转向
08  《伊万·杰尼索维奇的一天》(1962)（核心贡献页·书影替代公式框）— Tvardovsky 与赫鲁晓夫
09  《癌症楼》与《第一圈》(1966–1968)（名句引文框）— 国外出版与 KGB 抄稿
10  《古拉格群岛》(1973)（核心贡献页）— 三卷七部、256 份证词、三千万册
11  诺贝尔奖 1970 — 未亲领、1974 补受奖、书面演讲
12  流亡岁月 (1974–1994) — 伯尔家、苏黎世、佛蒙特、哈佛演讲
13  《红轮》：俄国革命的编年史 — 1914/1916/1917 四部曲
14  归乡与晚年 (1994–2008) — 特罗伊采-雷科沃、拒绝勋章、顿斯科伊修道院
15  结尾
```

### 第 7 步：版式要点

- 身份信息页参照 OpenPhysicist `\profileslide` 模式（左肖像 + 右信息网格）。
- 公式框位置用「书影框/引文框」：`tikz` 圆角框 + 斜体书名 + 页边留白 0.3cm。
- 国籍行注意四段变迁：Soviet Union (1922–1974) → Stateless (1974–1990) → Soviet Union (1990–1991) → Russia (from 1991)，封面上只写「苏联/俄罗斯」即可，细节入身份页。

### 第 8 步：专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 生卒日期噪声 | metadata 有 "1918-01-01/2008-01-01"，以正文 1918-12-11 / 2008-08-03 为准 |
| 获奖理由口径 | 只用官方句 "for the ethical force with which he has pursued the indispensable traditions of Russian literature"，勿转述改写 |
| 领奖年份 | 1970 获奖但 1974 才补受奖，勿写成 1970 亲赴斯德哥尔摩 |
| 《一天》发表年份 | 1962 刊出（1960 交稿给 Tvardovsky），勿写 1960 发表 |
| 流放地点 | 哈萨克斯坦 Birlik 村（南哈 Baidibek 区），勿与 Ekibastuz 混淆 |
| 《第一圈》原型 | Lev Kopelev → Lev Rubin，明载；勿把 Kopelev 写成师生关系 |
| 伯尔关系 | 1974 借住 Heinrich Böll 家，是事实；勿写成两人合著或师承 |
| 子女入库 | 仅 Ignat 入库；Yermolai/Stepan 仅具名不入库 |
| 政治红线 | 涉苏经历（被捕/驱逐/批评西方面）只按 page.md 客观陈述，不作政治评价、不引用争议言论；Pearce/Muggeridge 等访谈内容不入库不入片 |
| Reshetovskaya 回忆录 | 其负面回忆录系 page.md 转述且有 KGB 代笔争议（Christopher Andrew 说），立传中不展开 |
| 无载禁写 | 不编造文学师承（page.md 无任何导师）；不从颁奖词反推与俄国文学前辈的私人关系；Dostoevsky 仅出现在批评者言论中，禁建关系 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| Gulag | 古拉格 | 苏联劳改营管理总局的通称，非本书专名 |
| The Gulag Archipelago | 《古拉格群岛》 | 三卷七部，1973 巴黎首版 |
| One Day in the Life of Ivan Denisovich | 《伊万·杰尼索维奇的一天》 | 1962 中篇 |
| The Red Wheel | 《红轮》 | 系列史诗总题，含 August 1914 等 |
| sharashka | 萨拉什卡 | 特种科研劳改所 |
| SMERSH | 反间谍总局 | 1945 执行逮捕的机构 |
| Khrushchev Thaw | 赫鲁晓夫解冻 | 《一天》刊出的时代背景 |
| Novy Mir | 《新世界》 | Tvardovsky 主编的文学月刊 |
| Templeton Prize | 邓普顿奖 | 1983，勿与诺奖混淆 |
| internal exile | 国内流放 | 哈萨克 Birlik 村 |
| sound-ranging battery | 声测炮兵连 | 二战任职，勿泛写成"步兵" |
| Donskoy Monastery | 顿斯科伊修道院 | 安葬地 |

---

## 四、BGM 建议

- **选定曲目**：**Savage** — Alex-Productions（预分配）。
- **匹配理由**：标题 "Savage" 的粗粝质感与铁丝网、西伯利亚寒风的意象同构；曲风冷峻有力，匹配劳改营文学「直面苦难而不煽情」的道德力量；节奏沉稳，匹配编年史家的传记叙事。
- **备选**（未采用）：The Flow of Time（时间感弱于「群岛」空间感）；Tragedy（悲剧标签过直，与"道德力量"基调不合）。
- **时长**：以 `music_audio/curated_tracks.md` 为准，>15 页 × 7 秒即可，ffmpeg `-shortest` 对齐。

---

## 五、数据入库说明（已完成）

- **yaml**：`MySQL/data/Aleksandr_Solzhenitsyn.yaml`，name_en=`Aleksandr Solzhenitsyn`（frontmatter 原形），qid=Q34474，primary_occupation=`writer`，fields 5 条（第 4 步表），relations 9 条（第 4.5 步表）。
- **入库**：`python3 seed_person.py data/Aleksandr_Solzhenitsyn.yaml`（幂等，按 QID → name_en 匹配）。
- **验证**：has_social_data=1、person_field≥4、person_relation≥2。

> **开始执行 Beamer 立传时，每写一页就 make，看到溢出就修。**
