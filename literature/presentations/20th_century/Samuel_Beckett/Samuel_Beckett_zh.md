# 文学家立传提示词（OpenLiterature 批次实例：Samuel Beckett）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Samuel Beckett（1969 诺贝尔文学奖，荒诞派戏剧巨擘）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 数学家/物理学家/化学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson 提示词骨架）+ 文学家适配（无公式框，以名句引文框/意象图式/书影替代）。
- **本实例**：Samuel Barclay Beckett（塞缪尔·贝克特），爱尔兰剧作家、小说家、诗人，英法双语写作，公认的 20 世纪最重要作家之一、现代戏剧的改造者。
- **设计哲学**：文学家立传保留「身份信息页」与「领域结构化表达」骨架；视觉重心转向**空舞台**——本篇以「空舞台与两个等待者（empty stage & waiting figures）」贯穿。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Samuel Barclay Beckett（1906-04-13 ~ 1989-12-22，享年 83 岁）
- **1969 诺贝尔文学奖官方获奖理由**：
  > "for his writing, which – in new forms for the novel and drama – in the destitution of modern man acquires its elevation"
  > （中译：表彰其写作——以小说与戏剧的新形式——在现代人赤贫的境况中获得升华）
- **气质关键词**：**荒诞派戏剧的巨擘、减法的文体家、以法文「无风格」写作的爱尔兰人**
- **设计母题**：**空舞台（empty stage）**。光秃的舞台、一树、两人——戈多的舞台指示即其视觉纲领；版式以大面积空白、极简单色块、一束顶光的意象图式贯穿；晚期作品越写越短。
- **本地数据源**：`literature/presentations/pages/20th_century/Samuel_Beckett/page.md`（Wikipedia 全文 + frontmatter）+ 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Samuel_Beckett
- **肖像**：第 0 步待下载（infobox 1977 年照片；备选 Reginald Gray 1961 肖像画）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `literature/presentations/pages/20th_century/Samuel_Beckett/`（第一轮已核对，事实基准如下）：
  - 生卒（1906-04-13 生于都柏林 Foxrock 郊区 ~ 1989-12-22 逝于巴黎，享年 83 岁；安葬蒙帕纳斯公墓——与 Suzanne 合葬，墓碑灰色的遗愿 "any colour, so long as it's grey"）
  - 国籍（爱尔兰；成年后大半生定居巴黎）
  - 家庭（父 William Frank Beckett 为测量师、法国胡格诺后裔 1871–1933；母 Maria Jones Roe 爱尔兰护士；兄 Frank Edward 1902–1954；新教圣公会家庭、后成不可知论者）
  - 教育（Portora Royal School（Enniskillen，王尔德母校）；Trinity College Dublin 1923–1927 攻读现代文学与罗曼语族、1926 当选 Scholar、1927 BA；板球左打者，参加过两场 first-class 比赛入 Wisden——唯一打过 first-class 板球的诺奖文学奖得主；A. A. Luce 是导师式人物（非 TCD 教职）引其读 Bergson）
  - 任职（1928-30 巴黎高师 lecteur d'anglais；1930-31 返 TCD 任讲师一年后辞职——短暂学院生涯的终点；1946 圣洛爱尔兰红十字会医院仓库管理员）
  - 战时（法国沦陷后加入法国抵抗组织 Réseau Gloria 当信使、1942 网络被出卖与 Suzanne 徒步南逃鲁西永；1945-03-30 获 Croix de Guerre 与 Médaille de la Reconnaissance Française；自称 "boy scout stuff"；战时在鲁西永写《Watt》）
  - 关键荣誉（Nobel 1969——Suzanne 称之为 "catastrophe"；1961 首届 Prix International/Prix Formentor 与 Borges 共享；1959 TCD 荣誉博士；1968 美国艺术与科学学院外籍荣誉院士；Aosdána 首位 Saoi 1984；Obies 多座；Croix de Guerre 1945）
  - 文学影响与师承（page.md 明载：James Joyce 是挚友与最大灵感源——MacGreevy 引荐、协助《Finnegans Wake》研究、首篇论文 "Dante... Bruno. Vico.. Joyce" 为其辩护；Proust 论文受叔本华悲观主义影响；1935 起读 Geulincx；1931-33 父丧后在 Tavistock Clinic 随 Bion 接受两年心理治疗——成为《Watt》《Godot》的底色；1945 母亲房间里的「启示」：乔伊斯走「知」的路，他走「贫乏/无知/减法」的路）
  - 核心作品与贡献（4–6 条）：①《Waiting for Godot》（1948-49 法文写就、1952 出版 1953 巴黎首演，1998 年英国国家剧院公投「20 世纪最重要英语剧作」）；②小说三部曲 Molloy / Malone meurt / L'innommable（1951-53，正文从繁到简）；③《Endgame》/《Krapp's Last Tape》/《Happy Days》（1957-61，中期四大剧作序列）；④《How It Is》（Comment c'est，1961，中期散文终点、无标点段落）；⑤晚期极简序列（《Not I》《Rockaby》《Breath》35 秒无人物、Company/Ill Seen Ill Said/Worstward Ho 三部「closed space」）；⑥法国抵抗运动经历与双语自我翻译实践
  - 关键时间线（15–20 节点）：1906 生于都柏林 Foxrock / 5 岁学音乐 / Portora 求学 / 1923-27 TCD / 1926 Scholar / 1927 BA / 1928-30 巴黎高师 lecteur / 1929 经 MacGreevy 结识 Joyce / 1929 首篇论文与 "Assumption" / 1930 "Whoroscope" 获奖、返 TCD 讲师 / 1931 辞职漫游欧陆 / 1931《Proust》/ 1932 写 Dream of Fair to Middling Women（身后 1992 出版）/ 1933 父丧、Bion 治疗 / 1934《More Pricks Than Kicks》/ 1935《Echo's Bones》、写作《Murphy》/ 1936-37 德国行看画 / 1938《Murphy》出版、巴黎遇刺、Suzanne 走近 / 1939 战争爆发选择「交战中的法国」/ 1940-42 Réseau Gloria 信使 / 1942 南逃鲁西永写 Watt / 1945 Croix de Guerre、圣洛、母亲房间的「启示」/ 1946 Sartre 刊出《Suite》/ 1948-49 法文写 Godot / 1951-53 三部曲 / 1953 Godot 巴黎首演、Blin 导演 / 1957 Endgame / 1961 与 Suzanne 秘密成婚、Prix Formentor、How It Is / 1969 诺贝尔奖 / 1984 Aosdána 首位 Saoi / 1989-07-17 Suzanne 去世 / 1989-12-22 贝克特去世、合葬蒙帕纳斯

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下创建 `Samuel_Beckett/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同类目录既有 Makefile，设置 `MAIN=Samuel_Beckett_zh`、`VIDEO_NAME=Samuel_Beckett_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载（infobox 1977 照；images.txt 有 URL 直接用，250px 改 500px；404 用装饰圆占位）
- 可选插图：Godot 演出照（2010 Doon School）、蒙帕纳斯墓、都柏林 Samuel Beckett Bridge

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | theatre of the absurd | 荒诞派戏剧 | Esslin 命名的中坚、Godot 为旗帜 | 核心页 |
| 1 | tragicomedy | 悲喜剧 | Godot 副标题体裁、黑色幽默 | 戏剧页 |
| 2 | minimalist prose | 极简散文 | 晚期越写越短、mirlitonnades 六词诗 | 晚期页 |
| 3 | modernist literature | 现代主义文学 | 「最后一位现代主义者」 | 核心页 |
| 4 | bilingual writing | 双语写作 | 法语「无风格」写作+自我翻译 | 语言页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | James Joyce | 对方→本人 | 挚友与最大灵感源；协助 Finnegans Wake 研究；首篇论文为其辩护 |
| colleague | Thomas MacGreevy | 无向 | 挚友诗人，引荐 Joyce；为其诗集写书评 |
| colleague | Suzanne Dechevaux-Dumesnil | 无向 | 终身伴侣 1961 秘密成婚；Godot 手稿推销人 |
| colleague | Jorge Luis Borges | 无向 | 1961 首届 Prix Formentor 共同得主 |
| colleague | Jérôme Lindon | 无向 | Minuit 出版社社长，晚期法语作品的坚定支持者 |
| colleague | Roger Blin | 无向 | Godot 首演导演 |
| colleague | Billie Whitelaw | 无向 | 25 年合作者，Not I 的「嘴」，称其「最高诠释者」 |
| colleague | Jack MacGowran | 无向 | 首位单人剧演员；Eh Joe 与 Embers 为其而写 |

#### 4.5.1 入库操作

- 写入 `MySQL/data/Samuel_Beckett.yaml`，`python3 seed_person.py data/Samuel_Beckett.yaml` 幂等入库
- 方向约定：influence 为对方影响本人；colleague 无向自动 from<to 归一；note 含 ": " 用单引号包裹
- **Peggy Guggenheim / Barbara Bray 裁定**：短暂恋情与晚年平行关系 page.md 虽有载，但白名单无对应类型且涉隐私叙事——**不入库**，仅在陷阱表注明

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：荒凉、克制、黑幽默
- **配色**：深青灰（主色，预分配 `#0F4C5C`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeAbsurd` 荒诞派戏剧 — 深青灰 `#0F4C5C`
  - `badgeGodot` 等待戈多 — 黄土 `#B08D3E`（一棵树+一土丘）
  - `badgeMinimal` 极简散文 — 石墨灰 `#3A3A3A`
  - `badgeParis` 巴黎岁月 — 灰蓝 `#5C7A99`
- **背景母题**：极简空舞台——底部一条地平线、稀疏两个小圆（Vladimir/Estragon 的背影抽象），其余留白

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 定居地 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后，左头像 + 右信息网格（生卒/国籍/教育/战时抵抗/巴黎定居/主要荣誉/核心领域）。
4. **文学家无公式框**：用名句引文框（仅限 page.md 有英文原文者，如 "you must go on, I can't go on, I'll go on"、"I realised that my own way was in impoverishment… subtracting rather than in adding"、"Nothing is funnier than unhappiness"）、书影或意象图式替代。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 荒诞派戏剧的巨擘 / Samuel Beckett 1906–1989 + badge + 头像
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — Godot / 三部曲 / 中期四大剧作 / 晚期极简
04  都柏林与三一学院 (1906–1927) — Foxrock、Portora、Scholar、板球与 Wisden
05  巴黎：Joyce 的引力 (1928–1930) — MacGreevy 引荐、首篇论文、lecteur 岁月
06  漫游与减法的开端 (1930–1938) — Proust 论文、Bion 治疗、Murphy、1938 遇刺与 Suzanne
07  战争与抵抗 (1939–1945) — Réseau Gloria、鲁西永写 Watt、"boy scout stuff"
08  母亲房间的启示 (1945) — 减法宣言引文框、转向法语
09  《等待戈多》(1953) — 空舞台意象图式、"a play in which nothing happens, twice"
10  小说三部曲 — Molloy→Malone→Unnamable、终句引文框
11  中期剧场 — Endgame/Krapp's Last Tape/Happy Days、Nell 的台词引文框
12  1969 诺贝尔奖 — 引文框、Suzanne 的 "catastrophe"、突尼斯听闻
13  晚期极简 — Breath 35 秒、Not I 的嘴、Company 三部曲
14  合作者与传承 — Whitelaw/MacGowran/Herbert/Asmus、影响谱系（Pinter/Fosse 等）
15  遗产 — 蒙帕纳斯灰色墓碑、都柏林大桥、结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照已有文学侧成品的 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Beckett 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 三部曲称谓 | Molloy/Malone/Unnamable 被人称为「三部曲」但**违背作者本人明确意愿**——叙述时加此注记 |
| 民族认定 | 爱尔兰剧作家；圣公会家庭→不可知论者；「被误标为存在主义者」是 page.md 明载的辨析（Camus 是荒诞派/他本人对存在主义缺乏亲和），Review 勿补写「存在主义者」标签 |
| Godot 首演 | 1953 巴黎（Blin 导演）；1955 伦敦首演评论不佳后由 Hobson/Tynan 扭转——年份与城市勿混 |
| 结婚年份 | 1961 英格兰秘密登记（因法国继承法）；Suzanne 1989-07-17 去世、Beckett 1989-12-22 去世，同年合葬 |
| 战时表述 | 抵抗运动自嘲 "boy scout stuff"、晚年绝口不提——篇幅一句带过，不戏剧化 |
| 「学院生涯」 | 1930-31 TCD 讲师一年即辞职；勿写成长期教授；A. A. Luce 是引路导师式人物（非 TCD 教职）勿写成正式导师 |
| 诺奖反应 | Suzanne 称之为 "catastrophe"；本人避名誉、酒店大堂会客——细节可写但克制 |
| 与 Borges | 仅 Prix Formentor 1961 共享，非诺奖共享——关系类型用 colleague 而非 co-honored |
| 板球 | 唯一入 Wisden 的诺奖文学奖得主——趣味点可写，勿升格为「体育家」 |
| 无载禁写 | 与 Giacometti/Duchamp 私谊虽明载可写但库中不收（列表裁剪）；具体死因（肺气肿/疑似帕金森）如实一句；Barbara Bray 关系不展开 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Theatre of the Absurd | 荒诞派戏剧 | Esslin 命名 |
| tragicomedy | 悲喜剧 | Godot 副标题 |
| Waiting for Godot | 《等待戈多》 | En attendant Godot |
| poioumenon | 元虚构小说 | 三部曲方法论术语 |
| mirlitonnades | 芦笛诗 | 晚期法语极短诗 |
| lecteur d'anglais | 英语助教 | 巴黎高师职位 |
| Réseau Gloria | 格洛里亚网络 | 抵抗组织代号 |
| Croix de Guerre | 战争十字勋章 | 1945-03-30 |
| Saoi | 贤者 | Aosdána 最高荣衔、1984 首位 |
| Prix Formentor | 福门托奖 | 1961 首届与 Borges 共享 |
| Les Éditions de Minuit | 子夜出版社 | Lindon 主政 |
| Cimetière du Montparnasse | 蒙帕纳斯公墓 | 合葬地 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Daylight**（预分配）
- **风格**: 昼光 / 清醒 / 冷峻的白
- **匹配理由**:
  - "Daylight" 的冷峻白光匹配空舞台的顶光与戈多世界的裸露地形
  - 昼光（而非黄昏）的意象呼应贝克特的清醒减法——不悲情、不升华，只是继续
  - 曲目的克制情绪适配晚期极简作品的 35 秒《Breath》式的空
- **备选** (未采用): With Me（陪伴感强但「等待」主题已有黄土 badge 承担）、Tragedy（戏剧化过强，违背其反抒情）
- **本地路径**: `music_audio/` 下 Daylight 曲目 → 复制到 `presentations/20th_century/Samuel_Beckett/Daylight.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Samuel_Beckett/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Samuel_Beckett/metadata.json` | properties 辅助（冲突以正文为准） |
| `literature/presentations/pages/20th_century/Samuel_Beckett/images.txt` | 肖像 URL 清单（第 3 步下载源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录（获奖理由中译） |
| `literature/generate_20th_century_list.py` 的 CITATION_ZH | 官方获奖理由中译（key=(年份,姓名)） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/data/Samuel_Beckett.yaml` | 本人社会关系/领域 yaml（已入库） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
