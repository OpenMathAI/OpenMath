# 文学家立传提示词（Maurice Maeterlinck，1911 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Kenneth G. Wilson 提示词骨架为母本，适配文学家侧。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人文史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）骨架 + 文学家适配（无公式框——用名句引文框/代表作书影/意象图式替代）。
- **本实例**：Maurice Polydore Marie Bernard Maeterlinck（莫里斯·梅特林克，1911 年诺贝尔文学奖得主，象征主义戏剧大师，《青鸟》作者）。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」（Identity / Bio 速览页），核心页用代表作与引文框承载文学成就。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Maurice Maeterlinck（Maurice Polydore Marie Bernard Maeterlinck，1862-08-29 ~ 1949-05-06，享年 86 岁；1932 年起称伯爵）
- **官方获奖理由（EN 原文，禁止改写）**：
  > "in appreciation of his many-sided literary activities, and especially of his dramatic works, which are distinguished by a wealth of imagination and by a poetic fancy, which reveals, sometimes in the guise of a fairy tale, a deep inspiration, while in a mysterious way they appeal to the readers' own feelings and stimulate their imaginations"
- **官方获奖理由（中译，取自 `literature/generate_20th_century_list.py` CITATION_ZH，key=("1911","Maurice Maeterlinck")，禁止改写）**：
  > 表彰其多方面的文学活动，尤以其戏剧著作为最——想象力丰富、诗意盎然，时而以童话的面貌传达深刻灵感，以神秘的方式触动读者的情感并激发其想象
- **气质关键词**：**静态戏剧的创造者、蓝色的青鸟、神秘的日常悲剧**
- **设计母题**：**青鸟与温室（the Blue Bird and hothouses）**。诗集 Serres chaudes（温室）+ 童话剧 The Blue Bird（青鸟）构成其视觉双联——用蓝鸟剪影、温室玻璃棚光影承载「象征主义的神秘与日常」；引文框用其「静态戏剧」论述原句（老人扶椅独白段）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Maurice_Maeterlinck/page.md`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Maurice_Maeterlinck
- **肖像**：待下载（page.md 内嵌多帧：`Maurice_de_Maeterlinck.jpg` 早年照、`Maurice_Maeterlinck's_Portrait.jpg` 1915 照、`Portrait_of_Maurice_Maurice_Maeterlinck.jpg` 前 1905 照、`Picture_of_Maurice_Maeterlinck.jpg` c.1903 照，取清晰正装一帧）
- **参考模板**：`literature/presentations/cover/`；成品骨架参照 15 页结构

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载到 `literature/presentations/pages/20th_century/Maurice_Maeterlinck/`
- 肖像待下载（第 3 步）
- 事实基准（以 page.md 正文为准）：
  - 生卒（1862-08-29 生于根特 ~ 1949-05-06 逝于法国尼斯心脏病，享年 86 岁；frontmatter 死亡日期双值 05-06/05-05，以正文 05-06 为准）
  - 国籍（比利时；佛兰芒人但以法语写作；晚年长居法国尼斯）
  - 家庭（富裕法语家庭；父 Polydore 为公证人、爱好打理自家温室；母 Mathilde Colette Françoise Van den Bossche 出身富裕家庭）
  - 教育（1874 入根特耶稣会 Sainte-Barbe 学院——法国浪漫派遭贬、只许宗教剧，种下对天主教会与组织化宗教的厌恶；1885 根特大学法学学位）
  - 文学师承与影响（巴黎数月遇象征主义，**Villiers de l'Isle Adam** 对其后续创作影响巨大；中学同窗 **Charles van Lerberghe** 的诗剧与互为影响的象征主义起点；后受东方神秘主义与 Vedanta 影响）
  - 伴侣（与歌手/演员 Georgette Leblanc 1895–1918 关系，Leblanc 影响其后二十年创作并出演其女性角色；1910 结识 18 岁演员 Renée Dahon，1919-02-15 成婚）
  - 任职/居所（1895 迁巴黎 Passy；1906 迁格拉斯；租下诺曼底圣旺德里修道院；1930 购尼斯城堡命名 Orlamonde；1939 逃里斯本、1940 赴美、1947-08-10 返尼斯）
  - 关键荣誉（Nobel 1911，经瑞典学院院士 Carl Bildt 提名；1903 比利时政府三年戏剧奖；1920 利奥波德勋章大绶；1932 国王 Albert I 封伯爵程序（未完成登记，未正式入贵族册）；1948 法兰西学术院法语奖章；1947–1949 PEN International 主席）
  - 争议（1926《白蚁的生命》抄袭南非作家 **Eugène Marais**《白蚁之魂》——伦敦大学动物学教授 David Bignell 2003 就职演说称之为"学术抄袭的经典案例"；Marais 信件原文可引；另一指控涉《Monna Vanna》与 Browning 的《Luria》）
  - 核心作品与贡献（4-6 条）：静态戏剧理论（"The Tragic in Daily Life" 1896，收于 The Treasure of the Humble）；象征主义早期四剧 Intruder/The Blind/Pelléas et Mélisande/Interior；提线木偶剧（Interior、The Death of Tintagiles、Alladine and Palomides 为木偶剧场而写）；The Blue Bird (1908)；自然史三部曲（The Life of the Bee 1901 / Termites 1926 / Ants 1930）；Princess Maleine (1889) 经 Mirbeau 盛赞一举成名
  - 音乐遗产（Pelléas et Mélisande 启 Debussy 歌剧 L.88、Fauré Op.80、Schoenberg Op.5、Sibelius Op.46 等——展示页可列表）
  - 关键时间线（约 18 节点，见第 6 步幻灯片序列年份锚点）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下已有 `Maurice_Maeterlinck/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制邻近成品 `Makefile`，设置 `MAIN=Maurice_Maeterlinck_zh`、`VIDEO_NAME=Maurice_Maeterlinck_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载：优先 c.1903 正装照（`Picture_of_Maurice_Maeterlinck.jpg`）或 1915 照，Commons `Special:FilePath` 加 `?width=600`
- 可选插图：The Blue Bird 首演海报、1914–18 期间照片、比利时 50 欧元纪念币（2008）

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | symbolist drama | 象征主义戏剧 | La Jeune Belgique 圈内核心，象征主义运动重要一环 | 核心页 |
| 1 | static drama | 静态戏剧 | "The Tragic in Daily Life" 提出的戏剧美学 | 理论页 |
| 2 | poetry | 象征主义诗歌 | Serres chaudes (1889)、Douze chansons (1896) | 诗歌页 |
| 3 | essay | 随笔 | 神秘主义、伦理与宗教批判（1914 全集被列 Index 禁书目） | 随笔页 |
| 4 | natural history writing | 自然史写作 | 蜜蜂/白蚁/蚂蚁三部曲 | 自然史页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Auguste Villiers de l'Isle-Adam | 对方→本人 | 1885 巴黎相遇，象征主义思想影响其后续创作 |
| colleague | Charles van Lerberghe | 无向 | Sainte-Barbe 同窗，象征主义起点互为影响 |
| colleague | Octave Mirbeau | 无向 | 1890 年 Le Figaro 盛赞 Princess Maleine 使其一举成名，巴黎沙龙常客 |
| spouse | Georgette Leblanc | 无向 | 1895–1918 伴侣，演员/歌手，影响并出演其女性角色 |
| spouse | Renée Dahon | 无向 | 1910 相识，1919-02-15 成婚，相伴至终 |
| controversy | Eugène Marais | 无向 | 1926 La Vie des termites 抄袭其 Die Siel van die Mier（1925），南非舆论与国际诉讼未成 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深绿 `#1E4D3B`（分批文件预分配）
- **配色**：主色 + 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 象征主义戏剧 — 靛蓝 `#4C5FD5`
  - `badgeB` 静态戏剧 — 青绿 `#0E7C7B`
  - `badgeC` 诗歌与随笔 — 琥珀 `#E07B30`
  - `badgeD` 自然史写作 — 玫瑰 `#C4204F`
- **背景母题**：温室玻璃光斑 + 一只蓝鸟剪影（呼应设计母题）

### 第 6 步：规划幻灯片序列 【人物专属，13-15 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 青鸟诗人 / Maurice Maeterlinck 1862–1949 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、全名、国籍、出生地、教育、影响者、荣誉、核心领域）
03  核心贡献概览 — 象征主义戏剧 / 静态戏剧 / 诗歌与随笔 / 自然史
04  根特与耶稣会 (1862–1885) — 富裕家庭、温室与公证人之父、Sainte-Barbe 的压抑
05  巴黎与象征主义 (1885–1889) — 法学学位、Villiers de l'Isle Adam、Serres chaudes
06  一举成名 (1889–1893) — Princess Maleine 与 Mirbeau、Intruder、The Blind、Pelléas et Mélisande
07  静态戏剧（核心贡献页·引文框替代公式框）— 老人扶椅独白引文、木偶剧场、命运如提线人
08  巴黎岁月与 Leblanc (1895–1906) — Passy、Aglavaine et Sélysette、Treasure of the Humble
09  修道院与青鸟 (1906–1908) — 格拉斯、圣旺德里修道院、The Blue Bird 与 Stanislavsky 莫斯科制作
10  音乐中的梅特林克 — Pelléas 的 Debussy/Fauré/Schoenberg/Sibelius 谱系（列表页）
11  诺贝尔与战争 (1911–1918) — Carl Bildt 提名、1911 诺奖、外籍军团被拒、Stilmonde 市长
12  白蚁风波 — Eugène Marais 抄袭指控（Bignell 2003 定评、Marais 信件引文、辩护未成诉讼）
13  晚年与遗产 — 封伯爵、流亡里斯本与纽约、PEN 主席、Bulles bleues、1949 卒于尼斯
14  遗产与结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Maeterlinck 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名拼写 | 官方诺奖页拼写 Maurice (Mooris) Polidore Marie Bernhard Maeterlinck（notes 载），deck 用通行形式即可；入库 name_en 用 `Maurice Maeterlinck` |
| 伯爵身份 | 1932 年 Royal Decree 启动封伯爵程序，但**从未完成 letters patent 登记**（含纹章义务与税款），本人与家人未正式入比利时贵族册——勿写成"正式伯爵"；_intro 中的 "Count/Comte Maeterlinck from 1932" 按原文口径行文 |
| 卒日双值 | frontmatter 1949-05-06 与 05-05 双值，以正文 05-06 为准 |
| 死因 | 心脏病发作，卒于尼斯，勿写成"逝于比利时" |
| 抄袭案 | 只写 page.md 载明事实：Marais 1923-1925 发表于南非报刊、Maeterlinck 1926 出版、Marais 试图国际诉讼因财力未成、Bignell 2003 定评、Ardrey 归因 Marais 自杀与 Rousseau 异说并存——**不加重也不翻案** |
| Pelléas 首演 | 剧本 1892 出版、1893-05-17 首演；Debussy 歌剧 1893–1902 创作、1902 巴黎首演——年份勿混 |
| The Blue Bird | 首演 1908-09-30，但主要写于 1906（格拉斯时期），两说并写 |
| 政治内容 | 一战反德演讲与 1913 亲工会罢工只按 page.md 客观简述，**不作政治评价**；1914 全集被列 Index 一句客观即可 |
| 引语红线 | "Poems die when living people get into them" 与老人扶椅独白为 page.md 英文原文可引；Marais 两段信件原文可引并注明出处 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| symbolism | 象征主义 | 勿混同写实主义 |
| static drama | 静态戏剧 | 其独创戏剧美学 |
| marionette | 提线木偶 | 命运操控的隐喻 |
| La Jeune Belgique | 青年比利时 | 文学社团名保留法语 |
| The Blue Bird | 青鸟 | 童话剧代表作 |
| The Intruder | 不速之客 | 早期三剧之一 |
| The Blind | 群盲 | 早期三剧之一 |
| Pelléas et Mélisande | 佩利亚斯与梅丽桑德 | 保留法语标题 |
| The Life of the Bee | 蜜蜂的生活 | 自然史散文 |
| Serres chaudes | 温室 | 1889 诗集，保留法语名 |
| Bulles bleues | 蓝色的气泡 | 1948 回忆录 |
| Index Librorum Prohibitorum | 禁书目录 | 天主教会名目 |
| oceanic feeling | （无） | 属 Rolland-Freud 通信概念，勿误植到本篇 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions（分批文件预分配）
- **匹配理由**:
  - "With Me" 的静谧陪伴感匹配静态戏剧的内核——人物在命运静默的注视下生活，灯光低垂、几乎无动作的舞台美学
  - 曲名的温柔贴合青鸟意象——幸福与陪伴的追寻是 The Blue Bird 的主题
  - 中段的神秘气质呼应其神秘主义随笔与温室诗篇的幽光
- **备选** (未采用):
  - ★★ Eternals — 宏大感适配其"欧洲智者"声望，但少一分青鸟童话的轻盈
  - ★ Mirage — 神秘与幻象感贴合象征主义，唯温柔陪伴感不及 With Me
  - ★ The Invisible Light — 幽光气质契合温室诗篇，然缺命运的静默底色
- **本地路径**: 从 `music_audio/` 曲库复制对应曲目到 `presentations/20th_century/Maurice_Maeterlinck/`（对照 `curated_tracks.md`）
- **时长**: 按页数 × 7 秒估算，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Maurice_Maeterlinck/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Maurice_Maeterlinck.yaml` | 社会关系/领域入库 yaml（与本文件同步） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
