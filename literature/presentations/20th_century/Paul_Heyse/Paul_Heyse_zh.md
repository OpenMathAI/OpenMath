# 文学家立传提示词（Paul Heyse，1910 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Kenneth G. Wilson 提示词骨架为母本，适配文学家侧。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人文史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）骨架 + 文学家适配（无公式框——用名句引文框/代表作书影/意象图式替代）。
- **本实例**：Paul Johann Ludwig von Heyse（保罗·海泽，1910 年诺贝尔文学奖得主，首位获此奖的德国作家）。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」（Identity / Bio 速览页），核心页用代表作与引文框承载文学成就。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Paul Heyse（Paul Johann Ludwig von Heyse，1830-03-15 ~ 1914-04-02，享年 84 岁）
- **官方获奖理由（EN 原文，禁止改写）**：
  > "as a tribute to the consummate artistry, permeated with idealism, which he has demonstrated during his long productive career as a lyric poet, dramatist, novelist and writer of world-renowned short stories"
- **官方获奖理由（中译，取自 `literature/generate_20th_century_list.py` CITATION_ZH，key=("1910","Paul von Heyse")，禁止改写）**：
  > 致敬其在漫长创作生涯中，作为抒情诗人、剧作家、小说家与世界闻名的短篇小说家所展现的渗透理想主义的圆熟艺术
- **气质关键词**：**Dichterfürst（诗王）、中篇小说的大师、慕尼黑文学圈的核心**
- **设计母题**：**南方的光（southern light）**。Heyse 的成名作《L'Arrabbiata》与《Lieder aus Sorrent》均源自意大利之旅——用地中海暖光、德国北部冷调的对照承载「北人到南方」的视觉语言；引文框用其歌谣体诗译（Spanisches Liederbuch / Italienisches Liederbuch）的书影意象。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Paul_Heyse/page.md`（Wikipedia 全文 + frontmatter）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Paul_Heyse
- **肖像**：待下载（page.md 内嵌 Menzel 1853 年油画肖像，Commons 文件名 `Porträt des Paul Heyse (1853) - Adolf Friedrich Erdmann von Menzel (Museum Georg Schäfer).jpg`；Nobel 官方肖像亦可）
- **参考模板**：`literature/presentations/cover/`（项目首页模板统一 `\input`）；成品骨架参照数学家/物理学家侧 15 页结构

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载到 `literature/presentations/pages/20th_century/Paul_Heyse/`（page.md / page.html / metadata.json / images.txt）
- 肖像待下载（第 3 步）
- 事实基准（以 page.md 正文为准）：
  - 生卒（1830-03-15 生于柏林 Heiliggeiststraße ~ 1914-04-02 逝于慕尼黑，享年 84 岁）
  - 国籍（普鲁士王国；逝于巴伐利亚王国·德意志帝国；1910 年封贵族）
  - 家庭（父 Karl Wilhelm Ludwig Heyse 为柏林大学语文学家，曾为 Wilhelm von Humboldt 幼子与 Felix Mendelssohn 的家庭教师；祖父 Johann Christian August Heyse 为著名语法学家、词典学家；母亲是犹太人）
  - 教育（Friedrich-Wilhelms-Gymnasium 至 1847；柏林大学两年古典语文学；1849 赴波恩学艺术史与罗曼语；1852 以行吟诗人研究获博士，导师 Friedrich Diez——德国罗曼语文学先驱）
  - 文学师承与影响（Emanuel Geibel 为其「文学导师与终生挚友」，促成其慕尼黑任命）
  - 任职（1854 起慕尼黑罗曼语文学「名誉教授」，从未授课——Geibel 说动巴伐利亚国王 Maximilian II 授予；1859-1868 任 Literaturblatt zum deutschen Kunstblatt 编辑）
  - 文学社团（1849 柏林 Tunnel über der Spree；1852 小圈 Rütli——成员含 Kugler、Lepel、Fontane、Storm、Heyse；1854 慕尼黑 Die Krokodile——成员含 Felix Dahn、Wilhelm Hertz、Hermann Lingg、Franz von Kobell、Wilhelm Heinrich Riehl、Friedrich Bodenstedt、Adolf Friedrich von Schack）
  - 婚姻（1854 与 Margarete Kugler 成婚，1862 妻逝于 Meran，四子女 Franz/Julie/Ernst/Clara；1867 与 Anna Schubart 再婚）
  - 关键荣誉（Nobel 1910；1910 封贵族；1900 慕尼黑荣誉市民；1895 美国哲学学会国际会员；Schiller prize；Bavarian Maximilian Order for Science and Art）
  - 争议归属（自然主义的早期反对者——年轻批评家攻击其作品，他以《Merlin》(1892) 回应，但对方对公众影响甚微；诺奖评委 Wirsen 评价「自歌德以来德国再无更伟大的文学天才」）
  - 核心作品与贡献（4-6 条）：中篇小说《L'Arrabbiata》(1853/1855)；歌谣集 Spanisches Liederbuch（与 Geibel，1852，经 Schumann/Hugo Wolf 谱曲传世）；Italienisches Liederbuch (1860，Wolf 1892-96 谱曲)；戏剧《Kolberg》(1865，最大舞台成功)；177 篇短篇小说与约 60 部戏剧的总量；意大利文学翻译（Leopardi、Giusti）
  - 关键时间线（15-20 节点，见第 6 步幻灯片序列的年份锚点）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下已有 `Paul_Heyse/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录邻近成品的 `Makefile`，设置 `MAIN=Paul_Heyse_zh`、`VIDEO_NAME=Paul_Heyse_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载：优先 page.md 内嵌 Menzel 1853 油画（Commons `Special:FilePath` 加 `?width=600`，UA 加 `Mozilla/5.0`）；404 则用 Nobel 官方肖像页或装饰圆占位
- 可选插图：Waldfriedhof 墓、Paul-Heyse-Strasse 街牌

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | novelle | 中短篇小说 | 177 篇短篇，L'Arrabbiata 为世界名篇 | 核心页 |
| 1 | lyric poetry | 抒情诗 | 两部 Liederbuch 经作曲家谱曲传世 | 诗歌页 |
| 2 | drama | 戏剧 | 约 60 部，Kolberg 为最大成功 | 戏剧页 |
| 3 | literary translation | 文学翻译 | 意大利文学（Leopardi、Giusti） | 翻译页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Emanuel Geibel | 对方→本人 | 文学导师与终生挚友，促成慕尼黑名誉教授任命 |
| colleague | Theodor Storm | 无向 | Rütli 同社，海泽对 Storm 稿件的激赏奠定二人友谊 |
| colleague | Theodor Fontane | 无向 | Tunnel über der Spree 与 Rütli 同社成员 |
| spouse | Margarete Kugler | 无向 | 1854 成婚，1862 逝于 Meran，育四子女 |
| spouse | Anna Schubart | 无向 | 1867 再婚 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深海蓝 `#17435B`（分批文件预分配）
- **配色**：主色 + 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 中篇小说 — 青绿 `#0E7C7B`
  - `badgeB` 抒情诗 — 琥珀 `#E07B30`
  - `badgeC` 戏剧 — 玫瑰 `#C4204F`
  - `badgeD` 翻译 — 靛蓝 `#4C5FD5`
- **背景母题**：柔和气泡 + 一道南方暖光斜带（呼应设计母题）

### 第 6 步：规划幻灯片序列 【人物专属，13-15 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — Dichterfürst / Paul Heyse 1830–1914 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名、国籍、出生地、教育、导师、任职、荣誉、核心领域）
03  核心贡献概览 — 中篇小说 / 抒情诗 / 戏剧 / 翻译
04  柏林早年 (1830–1849) — 语文学家之家、模范学生、Geibel 引入艺术圈
05  Tunnel 与 Rütli (1849–1852) — 1849 入社、Storm 友谊之源、Frühlingsanfang 1848
06  波恩与博士 (1849–1852) — 艺术史与罗曼语、Diez 门下、行吟诗人研究
07  意大利之光 (1852–1853) — 奖学金游学、梵蒂冈抄本风波、南方光母题
08  成名之作（核心贡献页·引文框替代公式框）— L'Arrabbiata 与 Lieder aus Sorrent
09  慕尼黑 (1854–1914) — 名誉教授、Die Krokodile、Nordlichtern
10  歌谣与音乐 — Spanisches / Italienisches Liederbuch 经 Schumann、Hugo Wolf 谱曲
11  戏剧与晚年创作 — Kolberg (1865)、Merlin (1892)、Letzten Novellen (1914)
12  诗王与反对者 — Dichterfürst、与自然主义的论战、Wirsen 的评价
13  荣誉与诺贝尔 — 1900 荣誉市民、1910 封贵族、Nobel 1910（Pückler 伯爵代为出席）
14  遗产与结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照成品 `\profileslide` 模式。
- 头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\infob`）可复用近期成品骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Heyse 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | 全名 Paul Johann Ludwig von Heyse；入库 name_en 用 `Paul Heyse`（任务分配明确指定，勿用 frontmatter 的 `Paul von Heyse`）；1910 才封贵族，获诺奖同年 |
| 生卒双值 | frontmatter 生日有三个值（1830-03-15/03-13/01-01），以正文 infobox 1830-03-15 为准；卒日 1914-04-02（正文），勿用 frontmatter 的 1914-01-01 |
| 名誉教授 | 1854 年慕尼黑罗曼语文学「名誉教授」，**从未在该大学授课**，勿写成"慕尼黑大学教授" |
| 自然主义立场 | Heyse 是自然主义的**早期反对者**，勿写成自然主义作家 |
| Wirsen 引语 | "Germany has not had a greater literary genius since Goethe" 出自诺奖评委 Wirsen，非颁奖词正文，引用须注明归属 |
| 领奖缺席 | 无法出席斯德哥尔摩典礼，由 Count von Pückler 代表，勿写成"亲赴领奖" |
| 与拜罗伊特无关 | page.md 无任何瓦格纳/拜罗伊特记载，勿联想补充 |
| 母亲血统 | 母亲是犹太人（page.md 明载一句），可客观提及，勿展开叙事 |
| 博士导师 | 论文在 Friedrich Diez 指导下撰写、1852 因行吟诗人研究获博士；Diez 属教育经历，非文学师承关系 |
| 最年长得主 | 他是文学奖第五年长的得主（在 Munro、Seifert、Mommsen、Lessing 之后），勿写成"最年长" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Dichterfürst | 诗王 | 德语尊称，音译加注 |
| novelle | 中短篇小说 | 德国文体传统，勿混同 short story |
| Tunnel über der Spree | 施普雷河隧道社 | 柏林文学社团 |
| Die Krokodile | 鳄鱼社 | 慕尼黑文学社团 |
| Rütli | 吕特利社 | Tunnel 分裂出的小圈 |
| L'Arrabbiata | 怒姑娘 / 愤怒的女人 | 意大利语标题保留 |
| Spanisches Liederbuch | 西班牙歌谣集 | 保留德语原名 |
| Italienisches Liederbuch | 意大利歌谣集 | 保留德语原名 |
| Romance philology | 罗曼语文学 | 与"爱情小说"勿混 |
| troubadours | 行吟诗人 | 博士论文主题 |
| Lieder aus Sorrent | 索伦托之歌 | 1852/53 成名歌集 |
| Waldfriedhof | 森林墓园 | 慕尼黑安葬地（Nr. 43-W-27） |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Tragedy** — Alex-Productions（分批文件预分配）
- **匹配理由**:
  - "Tragedy" 的深沉张力匹配其两部悲剧性事实——1862 年发妻 Margarete 早逝（Meran 病故）与 1914 年 4 月辞世数月后一战爆发，作品里理想主义的圆满与个人命运的低音形成对照
  - 曲名的戏剧性也贴合其约 60 部戏剧创作的舞台气质（Kolberg、Ludwig der Bayer 均为历史悲剧题材）
  - 纪录片式的叙事节奏适配「柏林神童 → 意大利之光 → 慕尼黑诗王 → 1910 诺奖」的漫长创作生涯
- **备选** (未采用):
  - ★★ The Flow of Time — 时间感匹配其 84 岁漫长生涯，但戏剧命运感弱于 Tragedy
  - ★ Nostalgia — 契合意大利岁月的怀旧南光，但对 Dichterfürst 的公共气质稍显私人化
  - ★ Timeless — 长期纲领感合适，然比 Tragedy 少一层个人命运的低音
- **本地路径**: 从 `music_audio/` 曲库复制对应曲目到 `presentations/20th_century/Paul_Heyse/`（对照 `curated_tracks.md`）
- **时长**: 按页数 × 7 秒估算，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Paul_Heyse/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Paul_Heyse.yaml` | 社会关系/领域入库 yaml（与本文件同步） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
