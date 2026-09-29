# 文学家立传提示词（OpenLiterature 21 世纪批次：Tomas Tranströmer）

> **本文件是 Tomas Tranströmer（2011 诺贝尔文学奖）的人物专属立传提示词**，供后续 Beamer 立传 agent 直接复制到新对话中按步执行。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（内容适配文学家）。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 旗下，与 mathematician/physicist/chemist 侧同构）。
- **本实例**：Tomas Gösta Tranströmer（托马斯·特兰斯特勒默），瑞典诗人、心理学家与翻译家，2011 诺贝尔文学奖得主。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」两大骨架；文学家无公式框——用**名句引文框 / 代表作书影 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Tomas Gösta Tranströmer（1931-04-15 ~ 2015-03-26，享年 83 岁）
- **官方获奖理由**（2011，Wikipedia 原文照录，禁止改写）：
  > "because, through his condensed, translucent images, he gives us fresh access to reality"（表彰其通过凝练而透澈的意象，让我们以崭新的方式接近现实）
- **气质关键词**：**凝练透澈的意象、北欧冬日的静默、左手钢琴的诗人** —— 二战后斯堪的纳维亚最重要的诗人之一。
- **设计母题**：**透澈之水与光（condensed translucent images）**。其诗以日常与自然中「凝结而透明」的意象著称——波罗的海、冬日、铁路、水——视觉语言取「水与光的透澈感」：稀疏的大块冷色圆 + 一两处金色光斑，呼应「凝练而透澈」。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Tomas_Tranströmer/page.md`（Wikipedia 全文 + frontmatter）
  - `literature/presentations/pages/21st_century/Tomas_Tranströmer/metadata.json`、`images.txt`
  - Wikipedia URL: https://en.wikipedia.org/wiki/Tomas_Transtr%C3%B6mer （肖像：2014 年 Frankie Fouganthin 摄，第 0 步待下载）

---

## 三、任务流程 【逐步执行】

> 数据库同步要求：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 greatminds 库（MySQL），yaml 路径 `MySQL/data/Tomas_Tranströmer.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已下载（事实基准如下，第一轮已核对）
- 肖像待下载：infobox 照片 `Tomas_Tranströmer_in_2014-2.jpg`（Frankie Fouganthin 2014）
- **事实基准**：
  - 生卒：1931-04-15 生于斯德哥尔摩 ~ 2015-03-26 逝于斯德哥尔摩，享年 83 岁
  - 国籍：瑞典
  - 家庭：父母离异后由母亲 Helmy（小学教师）抚养；父 Gösta Tranströmer 为编辑；女儿 Emma 为音乐会女中音
  - 教育：Södra Latin 高中（开始写诗）→ 斯德哥尔摩大学 1956 年心理学毕业（兼修历史、宗教、文学）
  - 职业经历：1960–1966 Roxtuna 少年犯管教中心心理学者；1965–1990 韦斯特罗斯劳动力市场研究所心理学者
  - 写作生涯 1954–2015；15 部诗集；译成 60 余种语言
  - 关键荣誉（Nobel 2011；Neustadt 1990；北欧理事会文学奖 1990；瑞典学院北欧奖 1991；August 奖 1996；Golden Wreath 2003；Griffin 终身成就奖 2007；2011 获政府授予教授头衔等）
  - 配偶：Monika Bladh
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列展开）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Tomas_Tranströmer/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已完成人物目录的 Makefile，设置 `MAIN=Tomas_Tranströmer_zh`、`VIDEO_NAME=Tomas_Tranströmer_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：Commons `Tomas Tranströmer in 2014-2.jpg`（curl -A "Mozilla/5.0"，500px）；404 则用 images.txt 兜底，再不行用装饰圆占位
- 可选插图：《悲歌贡多拉》（Sorgegondolen）书影或波罗的海意象图

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist poetry | 现代主义诗歌 | 发展 20 世纪现代主义诗语 | 诗学页 |
| 1 | surrealist poetry | 超现实主义诗歌 | 表现主义/超现实语言中的神秘洞见 | 诗学页 |
| 2 | nature poetry | 自然诗歌 | 瑞典漫长冬天、四季节奏、自然之美 | 核心页 |
| 3 | haiku | 俳句 | 晚年瑞典语俳句尝试 | 晚年页 |
| 4 | psychology | 心理学 | 25 年心理学者职业经历 | 职业页 |

- 入库：`fields` 写入 `person_field`（带 rank）；缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> 只收 page.md 明载关系；yaml 与本表完全一致。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Monika Bladh | 无向 | 妻子 |
| parent-child | Gösta Tranströmer | 无向 | 父亲，编辑 |
| parent-child | Helmy | 无向 | 母亲，教师；离异后独自抚养 |
| parent-child | Emma | 无向 | 女儿，音乐会女中音；2011 年专辑 Dagsmeja 谱设其 18 首诗 |
| colleague | Robert Bly | 无向 | 美国诗人挚友，英译其诗；通信集 Air Mail（1964–1990） |
| colleague | Robin Fulton | 无向 | 英译者，New Collected Poems 全集译者 |
| colleague | Adunis | 无向 | 叙利亚诗人，伴其阿拉伯世界朗诵之旅并传播诗名 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：瑞典蓝 `#17435B`（深海蓝调，北欧冬日）
- **诺奖香槟金**：`C9A227`
- 四分类色（badgeA–D）：
  - `badgeA` 意象诗学 — 靛蓝 `#4C5FD5`
  - `badgeB` 自然与北方 — 青绿 `#0E7C7B`
  - `badgeC` 音乐与俳句 — 琥珀 `#E07B30`
  - `badgeD` 心理学人生 — 玫瑰 `#C4204F`
- **背景母题**：稀疏大块实心圆（冷蓝系）+ 一两处金色光斑，呼应「透澈之水与光」

### 5.1 文学家格式硬要求 【★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 身份 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心内容之前。左头像 + 右信息网格，含至少：生卒、国籍、出生地、家庭、教育、职业（诗人/心理学者/翻译家）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注 `OpenMathAI`；引号用半角 `" "`；中文引号内不写「原话」，除非 page.md 有英文原文。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 凝练透澈的意象 / Tomas Tranströmer 1931–2015 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  早年与教育 (1931–1956) — 斯德哥尔摩、母亲抚养、Södra Latin 起笔、17 Poems 1954、心理学毕业
04  心理学者生涯 (1960–1990) — Roxtuna 少年犯中心 → 韦斯特罗斯劳动力市场研究所
05  诗歌历程 — 15 部诗集时间轴（17 Poems 1954 → The Great Enigma 2004）
06  诗学特质（核心贡献页）— 凝练透澈的意象 / 现代主义-超现实主义语言 / 神秘与宗教维度
07  代表作深读 — Baltics（波罗的海，1974）与 The Sorrow Gondola（悲歌贡多拉，1996）引文框/意象图式
08  译介网络 — Robert Bly 挚友与 Air Mail、Robin Fulton 全集英译、60 余种语言
09  音乐 — 终生钢琴，中风后左手演奏；女儿 Emma 的 Dagsmeja；诸作曲家为其诗谱曲
10  1990 中风与坚持 — 部分瘫痪失语仍写作至 2000 年代；Minnena ser me 自传 1993
11  荣誉长廊 — Bellman 1966 · Neustadt 1990 · 北欧理事会 1990 · August 1996 · Nobel 2011
12  遗产与结尾 — 二战后斯堪的纳维亚最重要诗人之一
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现参照成品 `\profileslide`。
- 引文框/意象图式替代公式框：代表作页用 tikz 引文框呈现 page.md 明载的作品名与年份（勿杜撰诗句原文）。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删装饰元素 → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Tranströmer 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方原文 "because, through his condensed, translucent images, he gives us fresh access to reality"，勿改写成 "for his..." 句式 |
| 1970 年代批评 | 有诗人批评其诗不直面社会政治议题（脱离时代）——客观简述即可，勿展开论战叙事 |
| 「基督徒诗人」 | 正文作 "has been described as a Christian poet"（转述口径），勿写成直陈信仰 |
| 1990 中风 | 部分瘫痪、失语，仍持续写作出版至 2000 年代初；左手钢琴是他自述「继续活下去的方式」 |
| 俳句 | 是「晚年尝试瑞典语俳句」，勿说成主要体裁 |
| Adunis 拼写 | 正文作 Adunis（叙利亚诗人），勿写成 Adonis |
| Emma 专辑 | Dagsmeja（2011）含 18 首其诗的谱曲作品；Emma 为音乐会女中音 |
| Bhopal | 1984 毒气悲剧后赴博帕尔，与印度诗人（K. Satchidanandan 等）在厂外参加诗歌朗诵——客观一句即可 |
| 无载禁写 | 女儿 Emma 出生年、结婚年份、Monika Bladh 职业等 page.md 未载者一律不写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| condensed, translucent images | 凝练而透澈的意象 | 获奖理由原词，勿意译改写 |
| modernist poetry | 现代主义诗歌 | 与表现主义/超现实主义并提 |
| surrealism | 超现实主义 | 20 世纪诗歌语言脉络 |
| haiku | 俳句 | 晚年瑞典语尝试 |
| Baltic sea | 波罗的海 | Baltics 组诗母题 |
| prose memoir | 散文自传 | Memories Look at Me（1993） |
| psychology | 心理学 | 其职业身份，非「精神分析」 |
| mezzo-soprano | 女中音 | 女儿 Emma 身份 |
| stroke | 中风 | 1990 年，勿写「心脏病」 |
| poet laureate 语境勿混 | — | 2011 头衔是 Professors namn（教授名衔），非桂冠诗人 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**: **Tragedy** — Alex-Productions（52k views，高受众 / 深色 / 戏剧性）
- **匹配理由**:
  - 「深色」匹配其诗的底色 —— 北欧漫长冬天、静默与神秘感、悲歌贡多拉的挽歌气质
  - 「戏剧性」匹配人生转折 —— 1990 中风夺走言语与半身，却以左手钢琴与诗继续，是含蓄的悲剧性而非控诉
  - 「高受众」保证成片听感稳妥，与冷蓝主色 #17435B 的克制冷调相称
- **备选**（未采用）：★★ With Me（温和/稳定，契合心理学者职业段但整体张力不足）
- **本地路径**: `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` → 复制到本目录 `Tragedy.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Tomas_Tranströmer/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `literature/generate_21st_century_list.py` | 获奖理由中译（CITATION_ZH）对照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
