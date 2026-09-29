# 文学家立传提示词（OpenLiterature：Elias Canetti）

> **本文件是 OpenLiterature 的人物专属立传提示词**，以 Kenneth G. Wilson（OpenPhysicist 模板标杆）为骨架，适配文学家。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Canetti 定制内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合 OpenPhysicist 标杆（Kenneth G. Wilson 提示词 + tex 结构）与文学家侧实战经验。
- **本实例**：Elias Canetti（埃利亚斯·卡内蒂），1981 诺贝尔文学奖得主，德语现代主义作家与群众心理学探究者。
- **设计哲学**：文学家立传**没有公式框——以代表作书影 / 名句引文框 / 意象图式替代**；仍须保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Elias Canetti（1905-07-25 ~ 1994-08-14，享年 89 岁）
- **气质关键词**：**群众的解剖者、鲁斯河畔的多语者、火与书的见证人** —— 1981 诺贝尔文学奖获奖理由：
  > "for writings marked by a broad outlook, a wealth of ideas and artistic power"
  > （表彰其视野开阔、思想丰富而具艺术力量的写作）
- **设计母题**：**群众与火（crowds and fire）**。1927 年维也纳七月暴乱中的焚书场面成为他毕生反复回想的意象；《迷惘》里的书斋与《群众与权力》里的人群构成一对核心图式——版式语言宜用密集人群的叠影、火光色块与幽闭书塔意象。
- **本地数据源**：`literature/presentations/pages/20th_century/Elias_Canetti/page.md` + 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Elias_Canetti （肖像第 0 步标「待下载」；本页 infobox 无肖像照片，仅有出生地房照与墓碑照——可用 Wikipedia REST API page/summary 查 infobox 原图，404 则装饰圆占位）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面四件套已下载
- 肖像：**待下载**（infobox 无直接照片，REST API 回退；失败装饰圆占位）
- **事实基准（正文优先）**：
  - 生卒：1905-07-25 生于保加利亚鲁塞（Ruse，多瑙河畔，时为保加利亚公国）~ 1994-08-14 逝于瑞士苏黎世，享年 89 岁
  - 家庭：塞法迪犹太人大家庭；父 Jacques Canetti（商人，1912 年猝逝）、母 Mathilde（Arditti 家族——保加利亚最古老塞法迪家族之一，可溯至 14 世纪阿拉贡宫廷医师与天文学家）；长子，三兄弟中居首；弟 Jacques Canetti（定居巴黎，复兴法国香颂的推手）
  - 姓氏源流：本姓 Cañete，得名于西班牙昆卡省村庄 Cañete；先祖自奥斯曼埃迪尔内迁入鲁塞
  - 多语童年：母语拉迪诺语（Ladino），兼通保加利亚语、英语、法语，7 岁起由母亲强制学德语——德语成为其写作语言
  - 迁徙：鲁斯（1905–1911）→ 曼彻斯特（1911–12）→ 洛桑 → 维也纳（1912–）→ 苏黎世 → 法兰克福（中学毕业）→ 维也纳（1924 复返）
  - 教育：1924 入维也纳大学学化学，然兴趣转向哲学与文学；**1929 获化学博士学位，但从未做过化学家**
  - 1927 七月暴乱：误近现场，目睹焚书，深受震动（其著作中反复回想），骑车迅速离开
  - 第一共和国维也纳文学圈开始写作；政治上左倾
  - 1938 德奥合并后迁伦敦；1952 入英国籍；1970 年代起常赴苏黎世，最后 20 年定居苏黎世
  - 婚姻：1934 维也纳与 **Veza (Venetiana) Taubner-Calderon**（1897–1963）结婚——其缪斯与忠实的文学助手；1963 Veza 去世；1971 与 **Hera Buschor**（1933–1988）结婚，1972 得女 Johanna
  - 关键荣誉：Grand Austrian State Prize 1967 · Bavarian Academy 文学奖 1969 · 奥地利科学与艺术勋章 1972 · **格奥尔格·毕希纳奖 1972** · Deutscher Schallplattenpreis 1975（朗诵「Ohrenzeuge」）· Nelly Sachs Prize 1975 · Gottfried-Keller-Preis 1977 · Pour le Mérite 1979 · Hebel 奖 1980 · 卡夫卡奖（Klosterneuburg）1981 · **Nobel 1981** · 德国联邦十字大功绩勋章 1983；曼彻斯特大学荣誉博士（1975）、慕尼黑大学荣誉博士（1976）、格拉茨大学荣誉博士、维也纳荣誉市民
  - 南极南设得兰群岛利文斯顿岛 **Canetti Peak** 以其命名
  - 核心作品（4–6 条）：剧本《虚荣的喜剧》（Komödie der Eitelkeit, 1934）；长篇《迷惘》（Die Blendung / Auto-da-Fé, 1935——Wedgwood 英译 1946，美国版名《巴别塔》）；剧作《他们的日子有数》（Die Befristeten, 1956 牛津首演）；《群众与权力》（Masse und Macht, 1960——群众行为心理学研究）；马拉喀什行记（1968）；《卡夫卡的另一种审判》（1969）；自传三部曲《获救之舌》（1977）、《耳中火炬》（1980）、《目光的游戏》（1985）
  - 关键时间线（16 节点）：1905 生于鲁塞 → 1911 迁曼彻斯特 → 1912 父猝逝·迁洛桑/维也纳·始学德语 → 1916–1921 苏黎世/法兰克福 → 1924 回维也纳学化学 → 1927 七月暴乱·目睹焚书 → 1929 化学博士 → 1934 与 Veza 成婚·《虚荣的喜剧》→ 1935《迷惘》→ 1938 德奥合并·迁伦敦 → 1952 入英国籍 → 1960《群众与权力》→ 1963 Veza 去世 → 1967–1977 欧陆诸奖连获 → 1971 与 Hera 成婚 → 1977–1985 自传三部曲 → 1981 诺贝尔奖 → 1994 逝于苏黎世

### 第 1 步：建立目录 【模板通用】

- 已在 `literature/presentations/20th_century/Elias_Canetti/`（本提示词所在目录）

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=Elias_Canetti_zh`、`VIDEO_NAME=Elias_Canetti_zh`

### 第 3 步：收集图片 【人物专属】

- 下载肖像到 `images/Canetti.jpg`（REST API 回退），`curl -A "Mozilla/5.0"` + `file` 验证；失败装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Canetti 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | German-language literature | 德语文学 | 母语拉迪诺、写作语言德语的跨文化写作者 | 封面、核心页 |
| 1 | modernist novel | 现代主义小说 | 《迷惘》——infobox 运动标签 modernism | 核心页 |
| 2 | crowd psychology | 群众心理学 | 《群众与权力》：从暴民暴力到宗教集会 | 核心页 |
| 3 | memoir | 自传/回忆录 | 三部曲《获救之舌》《耳中火炬》《目光的游戏》 | 回忆页 |
| 4 | drama | 戏剧 | 《虚荣的喜剧》《他们的日子有数》 | 剧作页 |

#### 4.1 入库操作

- `python3 seed_person.py data/Elias_Canetti.yaml`（幂等；主记录 `primary_occupation='writer'`、`has_social_data=1`）
- 职业关联：writer（rank 0）、novelist（rank 1）、playwright（rank 2）
- 校验 person_field / person_relation 计数

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Veza Canetti | 无向 | 1934 年维也纳成婚，缪斯与忠实的文学助手（1963 年卒） |
| spouse | Hera Buschor | 无向 | 1971 年成婚（1988 年卒），1972 年得女 Johanna |
| parent-child | Johanna Canetti | — | 女（1972 生） |

> **不入库说明**：Anna Mahler（短暂恋情，马勒之女、雕塑家）、Marie-Louise von Motesiczky（多年亲密伴侣、画家）、Frieda Benedikt/Anna Sebastian（亲密关系）、Iris Murdoch（情人之一；其夫 John Bayley 回忆录称其「the Dichter」「the monster of Hampstead」）——均非婚姻关系，无适用类型，仅在立传正文客观简述；弟 Jacques Canetti（无 sibling 类型）；《卡夫卡的另一种审判》是对卡夫卡书信的研究，非个人关系，禁写 colleague/influence。**Nelly Sachs Prize（1975）仅为以其命名的奖项，与 Nelly Sachs 本人无任何明载关系，严禁据此建边。**

#### 4.5.1 入库操作

- 以 `name_en='Elias Canetti'`（Q80064）为中心写入 `person_relation`（库内此前无该人记录，本次新建）
- parent-child 不写 direction

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：幽深书塔、群众涌动、火光一瞬
- **配色**：深海蓝绿（主色 `#0B5351`）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeCrowd` 群众与权力 — 铁灰 `#37474F`
  - `badgeFire` 火/焚书意象 — 火橙 `#C2451E`
  - `badgeTower` 《迷惘》书塔 — 藏蓝 `#1F3A5F`
  - `badgeMemoir` 自传三部曲 — 橄榄金 `#8A7A2A`
- **背景母题**：密集人群剪影层叠 + 火光色块 + 幽闭塔状书堆

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + 细边框 + 姓名小字注（无真实肖像则装饰圆占位并注）。
2. 封面明示国籍（United Kingdom / Bulgaria）；底部状态栏 `国籍 | 语言 | 主要奖项`。
3. **必须有身份信息页**：左头像 + 右信息网格（生卒、多语背景、化学博士、迁徙路线、任职、荣誉、核心领域）。
4. **无公式框**：用《迷惘》书影 /《群众与权力》意象图式 / 1927 年焚书场景图式替代。
5. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页
01  封面 — 群众的解剖者 / Elias Canetti 1905–1994 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含多语背景、化学博士、迁徙、荣誉）
03  核心贡献概览 — 《迷惘》/《群众与权力》/ 自传三部曲 / 剧作
04  鲁塞与多语童年 (1905–1912) — 塞法迪家族、Cañete 姓氏源流、五语环境
05  父殁与迁徙 (1912–1924) — 曼彻斯特/洛桑/维也纳/苏黎世/法兰克福、母亲强授德语
06  维也纳：化学博士与文学圈 (1924–1931) — 兴趣转向、七月暴乱焚书
07  《迷惘》(1935)（核心页·书影）— 预演 mob 与群体思维的现代主义长篇
08  流亡伦敦 (1938–1952) — 德奥合并、入英国籍
09  《群众与权力》(1960)（核心页·意象图式）— 三十余年心血的群众行为研究
10  自传三部曲 (1977–1985) — 《获救之舌》《耳中火炬》《目光的游戏》
11  荣誉长廊 — 毕希纳奖 1972 · Nelly Sachs Prize 1975 · Pour le Mérite 1979 · Nobel 1981
12  苏黎世晚境与身后 — 最后 20 年、1994 辞世、Canetti Peak
13  遗产：视野开阔、思想丰富、艺术有力
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；宏名禁数字；`\foreach` 分隔符 ASCII 逗号。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；单遍取日志后须重新 `make pdf`。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Canetti 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 国籍口径 | 名录/infobox 记 United Kingdom / Bulgaria；正文另提晚年定居瑞士（描述含 Swiss）——立传统一以「保加利亚出生 → 英国国籍（1952）→ 定居苏黎世」呈现，勿写「瑞士作家」 |
| 化学博士 | 1929 年维也纳大学化学博士，**从未执业**——这是身份页必须呈现的反差事实，勿删勿写成文学博士 |
| 母语与写作语言 | 母语拉迪诺语（Judaeo-Spanish），5 岁前已通保加利亚语；德语是 7 岁后由母亲教授、后成为写作语言；infobox Language: German |
| 姓氏 | 本姓 Cañete（西班牙地名），勿写成加泰罗尼亚或意第绪来源 |
| 《迷惘》译名 | 德文原名 Die Blendung；英译 Auto-da-Fé（1946，Wedgwood）；美国首版名 The Tower of Babel——三个书名体系勿混 |
| 婚姻 | 两段：Veza（1934–1963 卒）、Hera（1971–1988 卒）；与 Motesiczky/Murdoch 等的亲密关系客观简述、不渲染 |
| 女儿 | Johanna 1972 年生（Hera 所出），Infobox 未列子栏，正文 personal life 明载 |
| 兄弟 | 弟 Jacques Canetti 在巴黎推动法国香颂复兴——是弟弟，勿写成儿子或侄子 |
| 奖项年份 | 毕希纳奖与奥地利科学与艺术勋章同为 1972；Nelly Sachs Prize 1975；Pour le Mérite 1979；Nobel 1981——勿错位 |
| Nelly Sachs | Nelly Sachs Prize 是奖项名，**与 Nelly Sachs 本人无关，禁建关系** |
| 卡夫卡 | 《卡夫卡的另一种审判》是其对卡夫卡致 Felice 书信的研究著作，禁据此写「师承/挚友」关系 |
| 涉政内容 | 1938 流亡、七月暴乱、对纳粹德国与政治混乱的反思均按 page.md 客观简述，不作政治评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Crowds and Power | 《群众与权力》 | Masse und Macht；通行译名 |
| Auto-da-Fé | 《迷惘》 | 英译书名（宗教裁判行刑仪式语义）；德文 Die Blendung（眩惑） |
| The Tongue Set Free | 《获救之舌》 | 自传第一部 |
| The Torch in My Ear | 《耳中火炬》 | 自传第二部 |
| The Play of the Eyes | 《目光的游戏》 | 自传第三部 |
| Ladino | 拉迪诺语 | 犹太-西班牙语，其母语 |
| Sephardic Jews | 塞法迪犹太人 | 家族背景，勿与阿什肯纳兹混淆 |
| July Revolt of 1927 | 1927 年七月暴乱 | 维也纳司法宫焚书事件 |
| Georg Büchner Prize | 格奥尔格·毕希纳奖 | 1972，德语文学最高奖之一 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions
- **风格**: 时间感 / 纪录片 / 沉静
- **匹配理由**:
  - "时间感" 对应自传三部曲的回溯结构——从获救之舌到目光的游戏，一生在三卷书中被时间重新照亮
  - "纪录片" 匹配其写作的双轨：文学与人类学式的《群众与权力》研究
  - 沉静底色呼应「幽闭书塔」与流亡者内省的气质
- **本地路径**: `music_audio/alex-productions/` 下 The Flow of Time 曲目 → `presentations/20th_century/Elias_Canetti/The_Flow_of_Time.wav`
- **时长**: 以实际曲目为准，`ffmpeg -shortest` 自动对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；Nelly Sachs Prize ≠ Nelly Sachs 关系。**
