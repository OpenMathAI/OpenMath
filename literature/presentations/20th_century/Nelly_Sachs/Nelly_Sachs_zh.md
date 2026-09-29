# 文学家立传提示词（OpenLiterature 批次实例：Nelly Sachs）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Nelly Sachs（1966 诺贝尔文学奖，大屠杀诗人）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 数学家/物理学家/化学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson 提示词骨架）+ 文学家适配（无公式框，以名句引文框/意象图式/书影替代）。
- **本实例**：Nelly Sachs（内莉·萨克斯），犹太德语-瑞典语诗人与剧作家。
- **设计哲学**：文学家立传保留「身份信息页」与「领域结构化表达」骨架；视觉重心从数据转向**意象**——本篇以「灰烬与星辰」贯穿。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Nelly Sachs（1891-12-10 ~ 1970-05-12，享年 78 岁）
- **1966 诺贝尔文学奖官方获奖理由**：
  > "for her outstanding lyrical and dramatic writing, which interprets Israel's destiny with touching strength"
  > （中译：表彰其杰出的抒情与戏剧写作，以感人的力量诠释以色列的命运）
- **气质关键词**：**大屠杀的哀歌者、卡巴拉意象的炼金师、流亡中的缄默之声**
- **设计母题**：**灰烬与星辰（ash and stars）**。萨克斯的诗歌意象系统——尘埃、星辰、气息、宝石、血、舞者、离水之鱼——在毁灭中寻找宇宙论的慰藉；版式可用升腾的细小光点与沉降的灰粒对位呼应「Flucht und Verwandlung（逃亡与变形）」。
- **本地数据源**：`literature/presentations/pages/20th_century/Nelly_Sachs/page.md`（Wikipedia 全文 + frontmatter）+ 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Nelly_Sachs
- **肖像**：第 0 步待下载（infobox 1910 年照片 `Nelly_Sachs_1910_repaired.jpg`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `literature/presentations/pages/20th_century/Nelly_Sachs/`（第一轮已核对，事实基准如下）：
  - 生卒（1891-12-10 生于柏林-舍讷贝格，德意志帝国 ~ 1970-05-12 逝于斯德哥尔摩，瑞典；本名 Leonie Sachs，享年 78 岁）
  - 国籍（德国 → 1952 年入籍瑞典；frontmatter 口径 Germany、Sweden）
  - 家庭（父 Georg William Sachs 为天然橡胶与古塔胶制造商 1858–1930；母 Margarete née Karger 1871–1950；终生未婚；表亲 Manfred George）
  - 教育（因体弱在家受教育；早年有舞蹈天赋，父母不鼓励从艺）
  - 流亡经历（1940 与老母乘纳粹德国飞往瑞典的最后一班飞机出逃——出逃前一周她原定被遣送集中营；是 Lagerlöf 友谊通过瑞典王室 intervention 挽救了母女）
  - 晚年（母亲去世后多次精神病发作，幻觉/被害妄想，曾住院数年，期间持续写作；最严重一次发作起因于赴瑞士领奖途中听到德语）
  - 关键荣誉（Nobel 1966 与 Agnon 共享；Droste-Preis 1960；首届 Nelly Sachs Prize 1961——多特蒙德以其命名的双年奖；德国书业和平奖；斯德哥尔摩荣誉市民；BerliN 荣誉市民）
  - 文学影响与师承（page.md 明载：受 German Romanticism 影响——早期作品更受基督教启发；受 Gertrud Kolmar、Else Lasker-Schüler 与 Paul Celan 影响；与 Celan 为 "brother" 挚友，Celan 名诗 "Zürich, Zum Storchen" 写其bond）
  - 核心作品与贡献（4–6 条）：①《In den Wohnungen des Todes》（1947，死亡居所中的诗）；②神秘剧《Eli: Ein Mysterienspiel vom Leiden Israels》（1950，最著名剧作，1967 年由 Walter Steffens 谱成歌剧在多特蒙德首演）；③《Flucht und Verwandlung》（1959，逃亡与变形）；④《Fahrt ins Staublose》（1961，进入无尘之境）；⑤诗歌译介（Swedish↔German 翻译维生；英译本 O the Chimneys 1967 等，Suhrkamp 出版）
  - 关键时间线（15–20 节点，起草时自下列素材选取）：1891 生于柏林 / 童年体弱在家教育 / 少女时代不幸恋情（恋人为非犹太人，后死于集中营）/ 1921 出版《Legenden und Erzählungen》/ 1933-40 纳粹崛起、一度失语 / 1940 与母逃亡瑞典 / 斯德哥尔摩两居室陪伴母亲、以翻译维生 / 1947《死亡居所》出版 / 1949《Sternverdunkelung》/ 1950 神秘剧 Eli / 1952 入瑞典籍 / 1959《逃亡与变形》/ 1960 Droste-Preis / 1961 首届 Nelly Sachs Prize / 与 Celan 的通信友谊 / 1966 诺贝尔奖（典礼上朗诵 "In der Flucht"） / 1967 多特蒙德歌剧 Eli 首演 / 1970-05-12 因结肠直肠癌逝于斯德哥尔摩 / 安葬 Norra begravningsplatsen / 遗物捐赠瑞典国家图书馆

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下创建 `Nelly_Sachs/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同类目录既有 Makefile，设置 `MAIN=Nelly_Sachs_zh`、`VIDEO_NAME=Nelly_Sachs_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载（`images.txt` 的 infobox 图 Nelly_Sachs_1910_repaired.jpg，250px 改 500px；404 则用 Commons `Special:FilePath/Nelly Sachs 1910 repaired.jpg?width=600` 回退；再 404 用装饰圆占位）
- 可选插图：柏林故居纪念牌（Berliner Gedenktafel）、斯德哥尔摩 Kungsholmen 岛 Nelly Sachs 公园

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

> 把文学领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | 核心体裁，1966 诺奖理由首语 | 核心页 |
| 1 | holocaust literature | 大屠杀文学 | 以色列命运的诠释者 | 核心页 |
| 2 | mystery play | 神秘剧 | 《Eli》一体两面的戏剧成就 | 戏剧页 |
| 3 | literary translation | 文学翻译 | 瑞典语↔德语互译（维生与志业） | 译介页 |
| 4 | german romanticism | 德国浪漫主义 | 早期诗歌的意象来源（page.md 明载影响） | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Shmuel Yosef Agnon | 无向 | 1966 诺贝尔文学奖共享 |
| colleague | Paul Celan | 无向 | "brother" 挚友，通信集《Paul Celan, Nelly Sachs: Correspondence》 |
| colleague | Selma Lagerlöf | 无向 | 长期通信友谊，1940 经其介入获瑞典王室相救 |
| colleague | Hilde Domin | 无向 | 长期通信友人 |
| colleague | Hans Magnus Enzensberger | 无向 | 战后德语作家通信往来 |
| colleague | Ingeborg Bachmann | 无向 | 战后德语作家通信往来 |
| influence | Gertrud Kolmar | 对方→本人 | page.md 明载影响者 |
| influence | Else Lasker-Schüler | 对方→本人 | page.md 明载影响者 |
| controversy | Moses Pergament | 无向 | 因其改编神秘剧 Eli 的长期争执 |

#### 4.5.1 入库操作

- 写入 `MySQL/data/Nelly_Sachs.yaml`，`python3 seed_person.py data/Nelly_Sachs.yaml` 幂等入库
- 方向约定：influence 为「对方→本人」有向（yaml 写 `direction: advisor` 语义即对方在先）；co-honored/colleague/controversy 无向自动 from<to 归一
- 缺失人物先建占位（has_biography=0）；note 含 ": " 用单引号包裹

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：哀矜、幽邃、灰烬中的微光
- **配色**：深石榴红（主色，预分配 `#8B1A1A`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeLyric` 抒情诗 — 深红 `#8B1A1A`
  - `badgeHolocaust` 大屠杀文学 — 炭灰 `#4A4A4A`
  - `badgeMystery` 神秘剧 — 靛蓝 `#2E3A59`
  - `badgeTrans` 翻译 — 灰蓝 `#5C7A99`
- **背景母题**：稀疏上升的细小星点 + 少量沉降的灰色圆粒（呼应「灰烬与星辰」母题，克制、不密集）

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 流亡地 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后，左头像 + 右信息网格（生卒/本名/国籍/出生地/流亡经历/主要荣誉/核心领域）。
4. **文学家无公式框**：用名句引文框（仅限 page.md 有英文/德文原文者，如 "When the great terror came/I fell dumb"）、书影或意象图式替代。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 大屠杀的哀歌者 / Nelly Sachs 1891–1970 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 抒情诗 / 大屠杀文学 / 神秘剧 / 翻译
04  柏林早年：庇护之宅 (1891–1940) — 体弱在家教育、舞蹈天赋、少女恋情、Legenden und Erzählungen
05  恐怖与失语 — 纳粹崛起、"When the great terror came/I fell dumb" 引文框
06  逃亡：最后一班飞机 (1940) — Lagerlöf 的营救、斯德哥尔摩两居室、翻译维生
07  《死亡居所》(1947) — 书影 + 意象图式
08  神秘剧 Eli (1950) — 以色列的受难、1967 多特蒙德歌剧化
09  意象炼金术 — 尘埃/星辰/气息/宝石/血的意象系统、卡巴拉 Shekhinah
10  灰烬后的黑暗岁月 — 母亲去世后精神病发作、住院中写作
11  与 Celan 的通信 — "Zürich, Zum Storchen"、共同的大屠杀经验
12  1966 诺贝尔奖 — 与 Agnon 共享、引文框、典礼朗诵 "In der Flucht"
13  荣誉与纪念 — Nelly Sachs Prize、柏林纪念牌、斯德哥尔摩公园
14  遗产 — 从德语诗人到犹太民族哀歌者
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照已有文学侧成品的 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Sachs 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 逃亡细节 | 1940 出逃是「纳粹德国飞往瑞典的最后一班飞机」，出逃前一周原定报告集中营；勿写成「乘船」 |
| 营救归因 | 挽救来自 Lagerlöf 的友谊（经瑞典王室 intervention），勿写成「自己申请签证成功」 |
| 国籍变迁 | 1952 才入瑞典籍；出生国籍德意志帝国；勿写「瑞典裔」 |
| 恋情归属 | 少女时代的恋人是非犹太人、死于集中营——该叙事是 page.md 明载，但具体姓名无载，禁编造 |
| 影响方向 | Kolmar / Lasker-Schüler 是影响「她」的人；Celan 是双向挚友——勿写成「萨克斯的学生/导师」 |
| 奖项归属 | Nelly Sachs Prize 1961 是首届、且以她命名（多特蒙德双年奖）；Droste-Preis 1960；勿混淆 |
| 失语事件 | 最严重精神病发作起因于「赴瑞士领奖途中听到德语」，勿写成「在瑞典听到」 |
| 死因 | 1970 死于结肠直肠癌（colorectal cancer），勿写「自杀/心脏病」 |
| 与 Agnon | 两人共享 1966 奖但分属不同语种与主题；她自述 Agnon 代表 Israel，而 "I represent the tragedy of the Jewish people"——可引用原文 |
| 无载禁写 | 师从某位具体诗人/学院的师承、具体治疗医生姓名等 page.md 无载，禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| mystery play | 神秘剧 | 非「悬疑剧」，中世纪宗教剧体裁 |
| Shekhinah | 舍金纳（神之临在） | 卡巴拉意象，勿译「女神」 |
| kabbalah | 卡巴拉 | 犹太神秘主义传统 |
| Shoah / The Holocaust | 纳粹大屠杀 | 与「以色列命运」叙事区分 |
| Flight and Metamorphosis | 《逃亡与变形》 | 书名直译保持一致 |
| In den Wohnungen des Todes | 《死亡居所》 | 1947 |
| Droste-Preis | 德罗斯特奖 | 1960，与 Nelly Sachs Prize 区分 |
| Nelly Sachs Prize | 内莉·萨克斯奖 | 1961 首届，以她命名 |
| Peace Prize of the German Book Trade | 德国书业和平奖 | 勿译「出版商奖」 |
| exile | 流亡 | 1940 起居瑞典 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Awaken**（预分配）
- **风格**: 苏醒 / 升华 / 从黑暗向光明
- **匹配理由**:
  - "Awaken" 匹配萨克斯的创作弧线——从柏林的缄默到斯德哥尔摩的哀歌，是创伤之后的醒来与作证
  - 曲名的「苏醒」意象呼应《Fahrt ins Staublose》「进入无尘之境」的升腾感与 Shekhinah 的救赎意象
  - 情绪起伏适配「灰烬与星辰」母题：低音区的沉降（灰烬）与高音区的透亮（星辰）
- **备选** (未采用): The Flow of Time（时间感强但偏温吞）、Last Hope（悲悯但戏剧化过强）
- **本地路径**: `music_audio/` 下 Awaken 曲目 → 复制到 `presentations/20th_century/Nelly_Sachs/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Nelly_Sachs/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Nelly_Sachs/metadata.json` | properties 辅助（冲突以正文为准） |
| `literature/presentations/pages/20th_century/Nelly_Sachs/images.txt` | 肖像 URL 清单（第 3 步下载源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录（获奖理由中译） |
| `literature/generate_20th_century_list.py` 的 CITATION_ZH | 官方获奖理由中译（key=(年份,姓名)） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/data/Nelly_Sachs.yaml` | 本人社会关系/领域 yaml（已入库） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
