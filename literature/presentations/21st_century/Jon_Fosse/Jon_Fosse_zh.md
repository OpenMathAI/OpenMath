# 文学家立传提示词（OpenLiterature · 21 世纪 · Jon Fosse）

> **本文件是 OpenLiterature 21 世纪批次的人物专属立传提示词**，目标人物：Jon Fosse（2023 年诺贝尔文学奖得主，挪威剧作家/小说家）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）；文学家适配：无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各人物侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Jon Olav Fosse（约恩·福瑟），2023 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传以**作品意象与语言质地**为骨架——本篇以「沉默与峡湾的留白」为视觉母题，强调「身份信息页」（Identity 速览页）与「文学领域表」的结构化表达，务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Jon Fosse（1959-09-29 生于挪威豪格松，在世）
- **气质关键词**：**易卜生之后被上演最多的挪威剧作家、新挪威语的诗性守护者、为不可言说者发声的极简主义者** —— 2023 年诺贝尔文学奖获奖理由：
  > "for his innovative plays and prose which give voice to the unsayable"（表彰其创新的戏剧与散文，为不可言说者发出了声音）
- **设计母题**：**留白与光（the unsayable / the shining light）**。七岁溺水濒死经验中的"微光"、Septology 的静默句法、峡湾与石屋；视觉语言取「大面留白 / 海雾 / 烛光点」，呼应"沉默的语言"。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Jon_Fosse/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：`https://en.wikipedia.org/wiki/Jon_Fosse`
- **肖像**：第 0 步待下载（infobox 无照片时可用 Haugesund 壁画图 `Jon_Foss_Mural_Haugesund_2025.jpg` 作插图页，肖像缺位则用装饰圆占位）。
- **参考模板**：
  - 数学家/物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`literature/presentations/cover/`（OpenLiterature 共享封面）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），使用 `MySQL/seed_person.py data/Jon_Fosse.yaml` 幂等入库。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `page.md`（事实基准如下，第一轮已核对）
- ✅ 待下载头像到 `images/`（Commons 250px 改 500px，curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证）
- **事实基准（以正文为准）**：
  - 生卒：1959-09-29 生于 Rogaland 豪格松（Haugesund），在 Strandebarm 长大，在世
  - 家庭：贵格会/虔信派家庭（自认塑造其灵性观）；三婚——Bjørg Sissel（1980–1992，护士，一子）、Grethe Fatima Syéd（1993–2009，印度裔挪威翻译家/作家，两女一子）、Anna（2011–，斯洛伐克人，居 Hainburg an der Donau 与挪威西部）；子女共 6 人（正文未逐一点名者禁写）
  - 教育：卑尔根大学比较文学（BA；1987 硕士）
  - 关键经历：七岁溺水濒死见"微光"（自认"或许因此成为作家"）；少年志在摇滚吉他手，弃乐从文；2012–2013 皈依天主教并自愿戒酒康复；2011 年起获国王授予奥斯陆王宫区 Grotten 荣誉居所
  - 关键荣誉：Nobel 2023（**首位新挪威语作家**、继 Bjørnson 1903 / Hamsun 1920 / Undset 1928 后第四位挪威得主）；Nordic Council Literature Prize 2015（三部曲）；International Booker 短名单 2022（Septology VI-VII，Damion Searls 译）；Swedish Academy Nordic Prize 2007；International Ibsen Award 2010；法国国家功勋骑士 2003；圣奥拉夫勋章司令 2005
  - 核心作品（4–6 条）：*Raudt, svart*（1983 处女作）、*Melancholia I–II*（1995–96）、戏剧 *Namnet*/*Natta syng sine songar*/*Draum om hausten*（1990s）、三部曲 *Andvake/Olavs draumar/Kveldsvævd*（2007–2014）、*Septologien*（2019–2021）、*Kvitleik*（2023）
  - 关键时间线（17 节点）：1959 生于豪格松 → 7 岁溺水濒死"微光"经验 → 12 岁左右开始写作 → 少年摇滚吉他/小提琴 → 卑尔根大学比较文学、改用新挪威语写作 → 1983 处女作 *Raudt, svart*（受 Vesaas 影响、反社会现实主义）→ 1985 *Stengd gitar* → 1986 诗集 *Engel med vatn i augene* → 1987 硕士/*Blod. Steinen er* → 1989 *Naustet* → 1992 新挪威语文学奖 → **1994 首部戏剧 *Og aldri skal vi skiljast* 上演/出版** → 1995–96 *Melancholia I–II* → 2000 Nestroy 戏剧奖 → 2007 瑞典学院北欧奖 → 2010 国际易卜生奖 → 2011 迁入 Grotten → 2015 北欧理事会文学奖（三部曲）→ 2019–2021 *Septologien* 三卷 → 2022 国际布克短名单 → **2023-10 获诺贝尔文学奖**、12-07 诺奖演讲《The Silent Language》→ 2025 歌剧剧本 *Asle og Alida*（Bent Sørensen 谱曲）与小说 *Vaim*

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `literature/presentations/21st_century/` 下建 `Jon_Fosse/` 与 `images/`
- 复制同项目 21 世纪已有 deck 的 Makefile，设 `MAIN=Jon_Fosse_zh`、`VIDEO_NAME=Jon_Fosse_zh`
- 复制 BGM：Daylight 曲目 wav → 本目录

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Fosse 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | minimalist drama | 极简主义戏剧 | 后戏剧剧场传统、上千舞台在上演 | 诺奖页、戏剧页 |
| 1 | lyric prose | 抒情性散文 | 散文近于诗、句法反常规 | 风格页 |
| 2 | nynorsk literature | 新挪威语文学 | 首位新挪威语诺奖得主 | 语言页 |
| 3 | postdramatic theatre | 后戏剧剧场 | page.md 明载的归类 | 戏剧页 |
| 4 | mysticism | 神秘主义 | 濒死微光、皈依天主教、"近乎神秘的感受力" | 精神页 |

#### 4.1 入库操作

- 由 `MySQL/data/Jon_Fosse.yaml` 经 `MySQL/seed_person.py` 写入：people 主记录（qid=Q443868、primary_occupation=writer、has_social_data=1、has_biography=0 待 Beamer 后置 1）+ 5 条 `person_field`
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；无载禁写。influence（思想影响者）类型可用。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Samuel Beckett | 单向（对方影响 Fosse） | Fosse 自列的"selective relatives"之一 |
| influence | Georg Trakl | 单向（对方影响 Fosse） | Fosse 自列的"selective relatives"之一 |
| influence | Thomas Bernhard | 单向（对方影响 Fosse） | Fosse 自列的"selective relatives"之一 |
| influence | Olav H. Hauge | 单向（对方影响 Fosse） | page.md 明载影响其生活与创作的作者 |
| influence | Knut Hamsun | 单向（对方影响 Fosse） | page.md 明载；1920 年文学奖得主 |
| influence | Tarjei Vesaas | 单向（对方影响 Fosse） | 新挪威语前辈，处女作受其影响 |
| influence | Franz Kafka | 单向（对方影响 Fosse） | page.md 明载 |
| influence | William Faulkner | 单向（对方影响 Fosse） | page.md 明载 |
| influence | Virginia Woolf | 单向（对方影响 Fosse） | page.md 明载 |
| spouse | Bjørg Sissel | 无向 | 第一任妻子（护士），1980–1992 |
| spouse | Grethe Fatima Syéd | 无向 | 第二任妻子（翻译家/作家），1993–2009，曾合译多部作品 |
| spouse | Anna Fosse | 无向 | 第三任妻子（斯洛伐克人），2011 结婚 |
| colleague | Bent Sørensen | 无向 | 2025 歌剧《Asle og Alida》作曲，Fosse 作脚本 |

- **不入库说明**：Henrik Ibsen 仅系"易卜生之后上演最多/传统延续"的批评定位，非明载师承（勿建 influence）；Damion Searls / Sarah Cameron Sunde / May-Brit Akerholt 均为译者，按惯例不入库；Anders Olsson（诺奖颁奖词）系评委。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：峡湾深青蓝 `#0E4D64`（本批次预分配）
- **辅色**：诺奖香槟金 `#C9A227` + 雾白 `#DCE3E6`（留白母题）
- **badgeA–D 四分类色**：
  - `badgeA` 极简主义戏剧 — 峡湾青蓝 `#0E4D64`
  - `badgeB` 抒情性散文 — 雾灰绿 `#175E54`
  - `badgeC` 新挪威语文学 — 香槟金 `#C9A227`
  - `badgeD` 神秘主义 — 深紫 `#46356B`
- **背景母题**：大面积留白 + 稀疏光点（烛光/微光），呼应"为不可言说者发声"

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 为不可言说者发声 / Jon Fosse 1959– + 四色 badge + 右上头像 + 国籍行（挪威）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、婚姻、荣誉、核心领域）
03  核心贡献概览 — 极简主义戏剧 / 抒情性散文 / 新挪威语文学 / 后戏剧剧场 / 神秘主义
04  早年：濒死的微光 (1959–1983) — 豪格松/Strandebarm、贵格-虔信派家庭、摇滚少年弃乐从文
05  卑尔根与新挪威语 (1983–1994) — Raudt, svart、反社会现实主义、Vesaas 影响
06  转向戏剧 (1994–2000) — Og aldri skal vi skiljast、Namnet、Natta syng sine songar
07  易卜生之后 — 上演最多的挪威剧作家、上千舞台、后戏剧剧场定位【意象图式页】
08  Melancholia 与三部曲 (1995–2015) — 北欧理事会文学奖
09  Septology (2019–2021) — 七部曲、Damion Searls 译本、国际布克短名单【书影页】
10  沉默的语言（引文页）— 诺奖演讲 The Silent Language：口头与书面语言、沉默之用
11  2023 诺贝尔文学奖 — 获奖理由全句 EN+中译、首位新挪威语得主、第四位挪威得主
12  信仰与孤独 — 濒死经验、2012–13 皈依天主教、戒酒、Grotten 隐居式写作【引文框页】
13  荣誉与认可 — Ibsen 2010 · 北欧理事会 2015 · 瑞典学院北欧奖 2007 · 圣奥拉夫司令
14  遗产：当代被上演最多的剧作家之一
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`
- 头部宏可整体复用最近文学 deck 骨架；品牌口径统一 `OpenMathAI`，引号用半角 `" "`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `latexmk -c && make pdf`，用 `pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标；溢出标准 vbox≤10pt / hbox≤50pt

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Fosse 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 语言 | 写作语言是**新挪威语（Nynorsk）**，勿与挪威语书面语（Bokmål）混同；"首位新挪威语诺奖得主"是 page.md 明载 |
| 挪威第四人 | 继 Bjørnson（1903）、Hamsun（1920）、Undset（1928）之后**第四位**挪威文学奖得主，顺序勿乱 |
| 易卜生关系 | "易卜生之后上演最多的挪威剧作家"是事实定位；"现代延续易卜生传统"是批评界观点——均**非**明载师承，禁建 influence |
| 自我定位 | Fosse 自认"首先是一位诗人，无论使用何种文学形式"，立传口径勿只写剧作家 |
| 三婚 | 三段婚姻与 6 名子女按 page.md 概述；未具名子女禁逐一点名 |
| 获奖反应 | NRK 采访"surprised but also not"为英文转述可引；评论家 Wolfe/Testard 引语为报道转述，慎用引号 |
| 无载禁写 | 无大学导师记载；"Daily Telegraph 百大在世天才 83 位"系媒体排名，慎用 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Nynorsk | 新挪威语 | 非一般"挪威语" |
| postdramatic theatre | 后戏剧剧场 | Lehmann 概念，page.md 明载 |
| Septology | 七部曲 | Septologien，2019–2021 |
| the unsayable | 不可言说者 | 获奖理由关键词 |
| Nordic Council Literature Prize | 北欧理事会文学奖 | 2015，三部曲 |
| International Ibsen Award | 国际易卜生奖 | 2010 |
| Grotten | 格罗滕（荣誉居所） | 挪威国王授予的艺术贡献荣誉 |
| selective relatives | 精神亲族 | Fosse 自述 Beckett/Trakl/Bernhard |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（批次预分配）
- **匹配理由**：
  - "天光/白昼"呼应贯穿 Fosse 一生的"濒死微光"意象与 Septology 的神性之光——作品的核心正是黑暗中对光的等待
  - 明亮而克制的气质匹配"沉默的语言"：极简、留白、不喧哗，呼应获奖理由中的 innovative plays and prose
  - 与批次内其他曲目（Expedition/The Flow of Time/Savage/Tragedy）不重复
- **本地路径**：`music_audio/alex-productions/` Daylight 曲目 wav → `presentations/21st_century/Jon_Fosse/Daylight.wav`
- **时长**：> 16 页 × 7 秒 ≈ 112 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Jon_Fosse/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_21st_century_list.py` | 官方获奖理由 EN+中译（CITATION_ZH，禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Jon_Fosse.yaml` | 入库 yaml（字段母本 = `MySQL/data/Kenneth_G_Wilson.yaml`） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
