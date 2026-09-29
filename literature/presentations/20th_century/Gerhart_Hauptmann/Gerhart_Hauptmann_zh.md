# 文学家立传提示词（Gerhart Hauptmann，1912 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Kenneth G. Wilson 提示词骨架为母本，适配文学家侧。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人文史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）骨架 + 文学家适配（无公式框——用名句引文框/代表作书影/意象图式替代）。
- **本实例**：Gerhart Johann Robert Hauptmann（格哈特·霍普特曼，1912 年诺贝尔文学奖得主，德国自然主义戏剧的奠基者，《织工》作者）。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」（Identity / Bio 速览页），核心页用代表作与引文框承载文学成就。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Gerhart Hauptmann（Gerhart Johann Robert Hauptmann，1862-11-15 ~ 1946-06-06，享年 83 岁）
- **官方获奖理由（EN 原文，禁止改写）**：
  > "primarily in recognition of his fruitful, varied and outstanding production in the realm of dramatic art"
- **官方获奖理由（中译，取自 `literature/generate_20th_century_list.py` CITATION_ZH，key=("1912","Gerhart Hauptmann")，禁止改写）**：
  > 主要表彰其在戏剧艺术领域丰硕、多样而杰出的创作
- **气质关键词**：**自然主义戏剧的开创者、织工的代言人、两岸之间的摇摆者**
- **设计母题**：**织机与钟（the loom and the sunken bell）**。《织工》(Die Weber) 的织机意象承载社会剧，The Sunken Bell (Die versunkene Glocke) 的沉钟承载象征剧——用织机经纬线与青铜钟的两种图形语言并置，呈现其自然主义与象征主义的双面性。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Gerhart_Hauptmann/page.md`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Gerhart_Hauptmann
- **肖像**：待下载（page.md 内嵌多帧：Wilhelm Fechner c.1900 照、Max Liebermann 1912 油画、Lovis Corinth 1900 油画，取清晰摄影一帧）
- **参考模板**：`literature/presentations/cover/`；成品骨架参照 15 页结构

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载到 `literature/presentations/pages/20th_century/Gerhart_Hauptmann/`
- 肖像待下载（第 3 步）
- 事实基准（以 page.md 正文为准）：
  - 生卒（1862-11-15 生于下西里西亚 Obersalzbrunn（今波兰 Szczawno-Zdrój）~ 1946-06-06 逝于 Agnetendorf（今 Jagniątków）支气管炎，享年 83 岁；临终语 "Am I still in my house?"；7-28 葬于 Hiddensee 墓园，墓碑按其遗愿只刻姓名）
  - 国籍（普鲁士王国 → 德意志帝国 → 魏玛共和国；西里西亚战后归波兰）
  - 家庭（父母 Robert 与 Marie 经营旅馆；兄长 Carl Hauptmann；两段婚姻——1885-05-05 与 Marie Thienemann 成婚（Radebeul），育三子，1904-07 离婚；1904-09 与 Margarete Marschalk 成婚（1903 年生子 Benvenuto），1905/1906 因 16 岁女演员 Ida Orloff 情事陷入危机）
  - 教育（1868 村小 → 1874 布雷斯劳 Realschule（勉强过考、留级一年）→ 1878 辍学学农（Lohnig 叔父农场，因肺疾中止）→ 1880 布雷斯劳皇家艺术学校雕塑（曾因「行为不端与用功不足」被暂令退学，经教授 Robert Härtel 说情复学）→ 1882 后耶拿大学一学期哲学与文学史 → 罗马雕塑失败 → 德累斯顿皇家学院短暂 → 柏林大学学历史，心系剧场）
  - 文学师承与影响（1885 经avant-garde 社团 **Durch** 接触自然主义——上溯 Sturm und Drang 与 Hart 兄弟圈；在 Durch 讲论被遗忘的 **Georg Büchner** 并确立自然主义取向；苏黎世遇精神科医生 **August Forel** 与牧师 Johannes Guttzeit 影响 Before Sunrise；诗人 Gusto Gräser 的乌托邦社群影响其 Dionysian-Jesuanic 游方先知题材）
  - 关键合作（导演 **Otto Brahm** 领衔的剧院首演其 17 部剧作，Before Sunrise 1889 首演开启德国文学自然主义）
  - 关键荣誉（Nobel 1912，Prussian Academy 的 Erich Schmidt 提名；三度奥地利 Franz-Grillparzer-Preis；1905 牛津 Worcester College 名誉博士；1909 莱比锡名誉博士；1932 歌德奖与哥伦比亚大学名誉博士；Adlerschild des Deutschen Reiches 首位得主；1915 Red Eagle 四级；维也纳荣誉戒指；布拉格查理大学名誉博士；布雷斯劳荣誉市民）
  - 争议（Wilhelm II 否决 1896 席勒奖并称其"社会民主"诗人；1913 布雷斯劳《纪念假面剧》演出因和平主义基调被王储推动取消；1914 签署九十三人宣言；1933 签署德意志文学学院忠诚宣誓、据 Ernst Klee 载申请入党被地区党部拒绝；作品遭宣传部审查——The Shot in the Park 新版被禁、Schluck and Jau 电影被禁；1942 80 寿庆官方协同操办；1944 列入 Gottbegnadeten 名单"不可替代艺术家"）
  - 核心作品与贡献（4-6 条）：Bahnwärter Thiel (1888，第一部自然主义中篇)；Before Sunrise (Vor Sonnenaufgang, 1889，德国剧场史最大丑闻之一、开启自然主义)；The Weavers (Die Weber, 1892，1844 西里西亚织工起义，国外最知名)；The Beaver Coat (Der Biberpelz, 1893，喜剧)；The Rats (Die Ratten, 1911)；长篇小说 The Fool in Christ, Emanuel Quint (1910)、Atlantis (1912)；晚期 Atriden 四部曲 (1941-44)）
  - 批评接受（Lukács 称"资产阶级德国的代表诗人"含贬义；Thomas Mann 1922 称"共和国之王"、在《魔山》中化用其特质入 Peeperkorn 一角；Shirer《第三帝国的兴亡》记载其与 Goebbels 并肩出场一幕；战后美国占领区禁演其剧、苏联占领区礼遇）
  - 关键时间线（约 18 节点，见第 6 步幻灯片序列年份锚点）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下已有 `Gerhart_Hauptmann/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制邻近成品 `Makefile`，设置 `MAIN=Gerhart_Hauptmann_zh`、`VIDEO_NAME=Gerhart_Hauptmann_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载：优先 Wilhelm Fechner c.1900 摄影照，Commons `Special:FilePath` 加 `?width=600`
- 可选插图：The Weavers 1897 Emil Orlik 彩色石版海报、Hiddensee 墓碑、Wiesenstein 故居

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | naturalist drama | 自然主义戏剧 | Before Sunrise 开启德国文学自然主义 | 核心页 |
| 1 | social drama | 社会批判剧 | The Weavers/The Rats 与压迫、阶级题材 | 社会剧页 |
| 2 | symbolic drama | 象征剧 | The Sunken Bell、Hannele 与晚期 Atriden 四部曲 | 象征剧页 |
| 3 | novel | 长篇小说 | Emanuel Quint (1910)、Atlantis (1912) | 小说页 |
| 4 | novella | 中短篇小说 | Bahnwärter Thiel (1888)、The Heretic of Soana | 中篇页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Georg Büchner | 对方→本人 | 在 Durch 社讲论其人其作，确立自然主义取向 |
| colleague | Otto Brahm | 无向 | 自然主义导演，其剧院首演霍普特曼 17 部剧作 |
| colleague | Carl Hauptmann | 无向 | 兄长，同为作家；同赴罗马，伦敦与苏黎世岁月同行 |
| colleague | Thomas Mann | 无向 | 1922 称其为共和国之王，魔山 Peeperkorn 化用其特质 |
| controversy | Wilhelm II | 无向 | 帝王否决 1896 席勒奖，1913 王储推动布雷斯劳演出取消 |
| spouse | Marie Thienemann | 无向 | 1885 成婚，资助其早期创作，1904 离婚 |
| spouse | Margarete Marschalk | 无向 | 演员，1904 成婚，相伴至终（葬 Hiddensee 1957 迁墓合葬） |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深紫 `#372A75`（分批文件预分配）
- **配色**：主色 + 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 自然主义戏剧 — 青绿 `#0E7C7B`
  - `badgeB` 社会批判剧 — 玫瑰 `#C4204F`
  - `badgeC` 象征剧 — 琥珀 `#E07B30`
  - `badgeD` 小说 — 靛蓝 `#4C5FD5`
- **背景母题**：织机经纬线网格 + 沉钟剪影（呼应设计母题）

### 第 6 步：规划幻灯片序列 【人物专属，13-15 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 织工与沉钟 / Gerhart Hauptmann 1862–1946 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、全名、国籍、出生地、教育、影响者、任职、荣誉、核心领域）
03  核心贡献概览 — 自然主义戏剧 / 社会批判剧 / 象征剧 / 小说
04  西里西亚少年 (1862–1880) — 旅馆之家、Realschule 挫折、学农与肺疾、布雷斯劳雕塑学校
05  雕塑梦与耶拿 (1880–1885) — 罗马失败、Liebesfrühling、Marie Thienemann、Erkner 定居
06  Durch 社与自然主义 (1885–1889) — Büchner 讲论、苏黎世 Forel、Bahnwärter Thiel
07  Before Sunrise 之夜（核心贡献页一·引文框替代公式框）— 1889 首演、Brahm 执导、德国剧场史丑闻
08  织工 (1892) — 1844 起义入剧、世界声誉顶点（Orlik 海报插图）
09  喜剧与象征 — The Beaver Coat、Hannele、The Sunken Bell、木偶意象
10  婚变与双城 — Margarete Marschalk、Agnetendorf 的神秘庇护所、Ida Orloff 危机
11  诺贝尔 1912 — Erich Schmidt 提名、颁奖词原文、Atlantis 与泰坦尼克巧合
12  帝国到共和国 — 席勒奖被否、九十三人宣言、Adlerschild 首位得主、歌德奖
13  纳粹岁月与终局 — 忠诚宣誓、审查与 80 寿庆、Gottbegnadeten、德累斯顿轰炸、1946 卒与 Hiddensee 下葬
14  遗产与结尾 — Lukács 与 Mann 的两副面孔、1962 百年纪念
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hauptmann 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生卒 | 1862-11-15 ~ 1946-06-06；frontmatter 生日双值（11-15/01-01）以正文 11-15 为准 |
| 代表作对 | 自然主义代表剧作实为 Arno Holz/Johannes Schlaf 的 Die Familie Selicke（Payrhuber 观点），Before Sunrise 是"划时代之作"但**非**自然主义戏剧的范本——勿颠倒表述 |
| 死亡地 | 卒于 Agnetendorf（Agnieszków，今 Jagniątków，Jelenia Góra 之一部），葬于 Hiddensee——两地勿混 |
| 入党申请 | 据 Ernst Klee 载 1933 年申请入党**被拒**——是"被拒"不是"入党" |
| 九十三人宣言 | 1914 签署支持德国军事行动，后又在其手稿中划掉 supportive 诗行——两面性如实呈现 |
| 与纳粹关系 | 呈现三事实（宣誓/被拒申请/接受 80 寿庆与 Gottbegnadeten 名单）+ 审查事实（Shot in the Park 被禁因黑人角色），**不作政治评价、不写"与纳粹合作"或"反抗纳粹"定性** |
| Ida Orloff | 1905/1906 与 16 岁女演员的情事危机——page.md 明载可写，措辞克制 |
| 引语红线 | "Whoever had forgotten how to cry learned again at the destruction of Dresden" 为 page.md 英文原文可引；Shirer 段落为转述材料，引须注 Shirer；临终语 "Am I still in my house?" 注 reported |
| Atlantis 巧合 | 小说写成于泰坦尼克沉没前一个月、丹麦电影 1913 年上映、挪威禁映——三个年份勿混 |
| Carl Hauptmann | 兄长 Carl 亦是作家（.page 仅一句"elder brother"），勿展开其生平 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| naturalism | 自然主义 | 文学运动，勿混 nature writing |
| The Weavers | 织工 | 保留 Die Weber 副标 |
| The Beaver Coat | 獭皮 | 喜剧代表作 |
| The Rats | 群鼠 | 1911 剧作 |
| Before Sunrise | 日出之前 | Vor Sonnenaufgang |
| The Sunken Bell | 沉钟 | 象征剧 |
| Bahnwärter Thiel | 道岔夫梯尔 | 中篇名保留 |
| Gottbegnadeten list | 天才名录 | 纳粹时期免征名单，客观名目 |
| Manifesto of the Ninety-Three | 九十三人宣言 | 一战文件 |
| Durch | 贯穿社 | 柏林自然主义 avant-garde 社团 |
| Adlerschild des Deutschen Reiches | 帝国雄鹰盾 | 首位得主 |
| Vor Sonnenaufgang | 日出之前 | 保留德语原名一并列出 |
| Hiddensee | 希登泽岛 | 夏居与安葬地 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（分批文件预分配）
- **匹配理由**:
  - "Eternals" 的宏大绵长匹配其 60 余年创作生涯与 Atriden 四部曲的古典终章——从 1889 Before Sunrise 到 1944 伊菲革涅亚，跨度近乎现代德国戏剧史本身
  - 曲名的"恒久"贴合 The Sunken Bell 的象征意象——沉入湖底的钟声仍在鸣响
  - 低音弦乐的厚重适配织机意象与西里西亚劳工叙事的分量
- **备选** (未采用):
  - ★★ Empire Collapse — 帝国崩塌感匹配其横跨四朝的经历，但情绪过于激烈
  - ★ Tragedy — 悲剧张力贴合织工与群鼠，然已在同批他篇预配
  - ★ The Flow of Time — 时间感匹配 84 年生涯，唯象征剧一侧的神秘感不足
- **本地路径**: 从 `music_audio/` 曲库复制对应曲目到 `presentations/20th_century/Gerhart_Hauptmann/`（对照 `curated_tracks.md`）
- **时长**: 按页数 × 7 秒估算，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Gerhart_Hauptmann/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Gerhart_Hauptmann.yaml` | 社会关系/领域入库 yaml（与本文件同步） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
