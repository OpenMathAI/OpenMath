# 文学家立传提示词（OpenLiterature 21 世纪批次：Alice Munro）

> **本文件是 Alice Munro（2013 诺贝尔文学奖）的人物专属立传提示词**，供后续 Beamer 立传 agent 直接复制到新对话中按步执行。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（内容适配文学家）。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 旗下，与 mathematician/physicist/chemist 侧同构）。
- **本实例**：Alice Ann Munro（艾丽丝·门罗，娘家姓 Laidlaw），加拿大短篇小说大师，2013 诺贝尔文学奖得主——首位获此奖的加拿大人、第 13 位女性。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」两大骨架；文学家无公式框——用**名句引文框 / 代表作书影 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Alice Ann Munro（1931-07-10 ~ 2024-05-13，享年 92 岁）
- **官方获奖理由**（2013，Wikipedia 原文照录，禁止改写）：
  > cited as a "master of the contemporary short story"（中译照录 `generate_21st_century_list.py` CITATION_ZH：当代短篇小说大师）
- **气质关键词**：**当代短篇小说大师、安大略小镇的时间魔术师、不动声色的叙事者** —— 被认为革新了短篇小说这一形式。
- **设计母题**：**往复的时间（forward and backward in time）**。其作在时间中前后穿行、以连缀短篇织出史诗——视觉语言取「小镇街景与老照片色块」：暖褐与紫色层次 + 时间线节点，呼应「在几页之内容纳小说的全部史诗复杂性」（瑞典学院语）。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Alice_Munro/page.md`（Wikipedia 全文 + frontmatter）
  - `literature/presentations/pages/21st_century/Alice_Munro/metadata.json`、`images.txt`
  - Wikipedia URL: https://en.wikipedia.org/wiki/Alice_Munro （肖像：infobox「Munro in 2006」，第 0 步待下载）

---

## 三、任务流程 【逐步执行】

> 数据库同步要求：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 greatminds 库（MySQL），yaml 路径 `MySQL/data/Alice_Munro.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已下载（事实基准如下，第一轮已核对）
- 肖像待下载：infobox 照片（Munro in 2006）
- **事实基准**：
  - 生卒：1931-07-10 生于安大略省 Wingham（大萧条中）~ 2024-05-13 逝于安大略省 Port Hope 自宅，享年 92 岁；患失智症至少 12 年
  - 本名 Alice Ann Laidlaw；父 Robert Eric Laidlaw 为狐貂农（后改火鸡养殖）；母 Anne Clarke Laidlaw（娘家姓 Chamney）为教师，1940 年代初患帕金森病
  - 爱尔兰与苏格兰后裔；苏格兰诗人 James Hogg 为远祖
  - 教育：1949 起在西安大略大学读英语（两年奖学金），1950 年发表首篇故事 "The Dimensions of a Shadow"；1951 年为结婚辍学
  - 家庭：1951 嫁同学 James Munro（1972 离婚）；女 Sheila 1953 / Catherine 1955（出生当日夭折）/ Jenny 1957 / Andrea Robin 1966；1963 迁维多利亚开 Munro's Books；1976 嫁 Gerald Fremlin（退休地图学家/地理学家，二战皇家空军老兵），2013-04-17 逝
  - 健康与晚年：2009 透露曾治癌症并做冠状动脉搭桥；约 2013 年起停笔；2024-05-13 逝
  - 关键荣誉：Governor General's Award 三度（1968/1978/1986）· Giller Prize 两度（1998/2004）· Man Booker International 2009 · Nobel 2013；O. Henry Award 三度（2006/2008/2012）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列展开）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Alice_Munro/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已完成人物目录的 Makefile，设置 `MAIN=Alice_Munro_zh`、`VIDEO_NAME=Alice_Munro_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：infobox 照片（curl -A "Mozilla/5.0"，500px）；404 则用 images.txt 兜底，再不行用装饰圆占位
- 可选插图：《Dear Life》（2012）书影或 Munro's Books 书店照

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | short story | 短篇小说 | 当代短篇小说大师（诺奖理由） | 核心页 |
| 1 | short story cycle | 连缀短篇（短篇循环） | 前后穿行的时间 + 集成短篇循环 | 形式页 |
| 2 | Southern Ontario Gothic | 南安大略哥特 | 其作多属该文学亚类型 | 风格页 |
| 3 | regional fiction | 地域小说 | Huron County 小镇世界 | 主题页 |
| 4 | literary fiction | 文学小说 | frontmatter field_of_work 口径 | 风格页 |

- 入库：`fields` 写入 `person_field`（带 rank）；缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> 只收 page.md 明载关系；yaml 与本表完全一致。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | James Munro | 无向 | 第一任丈夫，1951 结婚，1972 离婚；书店合开者 |
| spouse | Gerald Fremlin | 无向 | 第二任丈夫，1976 结婚，2013 逝 |
| parent-child | Robert Eric Laidlaw | 无向 | 父亲，狐貂农/火鸡养殖 |
| parent-child | Anne Clarke Laidlaw | 无向 | 母亲，教师，1940 年代初患帕金森病 |
| parent-child | Sheila Munro | 无向 | 女儿，2002 出版童年回忆录 |
| parent-child | Jenny Munro | 无向 | 女儿 |
| parent-child | Andrea Skinner | 无向 | 幼女（原名 Andrea Robin），2024 年披露童年受继父虐待 |
| colleague | Douglas Gibson | 无向 | 长期合作编辑与出版人，1986 追随其转投 McClelland & Stewart |
| colleague | Margaret Atwood | 无向 | 长年挚友；为其选集作序；称其为女性与加拿大人的先驱 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深紫 `#372A75`（暮色中的安大略小镇与往复时光的沉静）
- **诺奖香槟金**：`C9A227`
- 四分类色（badgeA–D）：
  - `badgeA` 短篇小说大师 — 靛蓝 `#4C5FD5`
  - `badgeB` 连缀短篇与时间 — 青绿 `#0E7C7B`
  - `badgeC` 地域书写 — 琥珀 `#E07B30`
  - `badgeD` 女性与成长 — 玫瑰 `#C4204F`
- **背景母题**：暖褐老照片色块 + 紫色时间线节点，呼应「往复的时间」

### 5.1 文学家格式硬要求 【★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 身份 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心内容之前。左头像 + 右信息网格，含至少：生卒、本名、国籍、出生地、家庭（两段婚姻/女儿）、教育、职业（短篇小说作家）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注 `OpenMathAI`；引号用半角 `" "`；中文引号内不写「原话」，除非 page.md 有英文原文。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 当代短篇小说大师 / Alice Munro 1931–2024 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  Wingham 童年 (1931–1949) — 大萧条农家、养狐场、母亲的病、少女起笔
04  大学与第一段婚姻 (1949–1963) — 西安大略大学、1950 首篇发表、主妇写作、Munro's Books
05  短篇小说的日常革命 — 家务间隙写作；"Housewife Finds Time to Write Short Stories" 标题页
06  成名 — Dance of the Happy Shades 1968 首夺总督奖 → 三度总督奖 → Booker 国际奖 2009
07  作品长廊 — 14 部原创集时间轴（Dance of the Happy Shades 1968 → Dear Life 2012）
08  风格（核心贡献页）— 时间往复 / 连缀短篇 / 南安大略哥特 / 全知叙述者；"Powers" 八易其稿
09  主题世界 — 少女成长 → 中年与老年的漂泊女性；Huron County 意象图式
10  挚友与出版人 — Margaret Atwood 与 Douglas Gibson（退还预付款追随转社）
11  荣誉长廊 — 总督奖 1968/1978/1986 · Giller 1998/2004 · Booker International 2009 · Nobel 2013
12  身后与再评价 — 2024 身后 Andrea Skinner 披露事件与文坛再评价，客观简述（见第 9 步陷阱）
13  遗产与结尾 — 革新短篇小说形式；加拿大「国宝」；2014 银币与 2015 邮票
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现参照成品 `\profileslide`。
- 引文框/意象图式替代公式框：代表作页用 tikz 引文框呈现书名与年份（勿杜撰句子原文；获诺奖后被问及小镇生活有何趣味时答 "You just have to be there." 为 page.md 明载，可用）。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删装饰元素 → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Munro 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 身后虐待事件红线 | 2024 年 Andrea Skinner 披露继父 Gerald Fremlin 自 1976 年起性虐待（Munro 1992 年知情后仍留在婚姻中；2005 年 Fremlin 认罪获缓刑）——只按 page.md 客观简述一页/一段，不作道德评判、不展开细节、不作心理分析；置于「身后与再评价」页 |
| Giller 年份噪声 | 正文将 Runaway 的 Giller 记作 2002、View from Castle Rock 记作 2004，infobox 口径为 1998/2004 两度——采用 infobox 1998（The Love of a Good Woman）与 2004（Runaway），正文年份噪声加注 |
| 契诃夫类比 | 与 Chekhov/Cheever 并列系批评界评价，**非本人师承或影响关系，禁入关系表** |
| Catherine | 三女 Catherine 出生当日夭折（1955）——可入时间线，不入关系库 |
| 两段婚姻 | 1951 James Munro（1972 离婚）/ 1976 Gerald Fremlin（2013 逝）；「离婚原因双方不忠」一句客观带过即可 |
| 获奖理由口径 | "master of the contemporary short story"（瑞典学院语），勿改写；「首位加拿大人 + 第 13 位女性」为 page.md 明载 |
| 版本学 | "Powers" 写了 8 个版本；"Wood"（1980/2009）与 "Home"（1974/2006/2014）隔多年重写——体现「不知疲倦的自我修订者」 |
| 13 种语言 | 作品集译成 13 种语言（非 60 语言的 Tranströmer，勿串） |
| 改编 | 5 部电影改编（Away from Her 2006、Julieta 2016 等），一句带过即可 |
| 无载禁写 | James Munro 职业（仅知百货公司工作）、Fremlin 具体生年、孙辈等 page.md 未载者不写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| short story cycle | 连缀短篇/短篇循环 | 其标志性形式 |
| Southern Ontario Gothic | 南安大略哥特 | 文学亚类型，勿译「哥特式」泛称 |
| Huron County | 休伦县 | 安大略文学地图核心 |
| omniscient narrator | 全知叙述者 | 叙事特征 |
| verisimilitude | 逼真感 | Thacker 评语用词 |
| epiphanic moment | 顿悟时刻 | 与契诃夫类比的核心 |
| Governor General's Award | 总督奖 | 三度得主（1968/1978/1986） |
| Man Booker International Prize | 布克国际奖 | 2009 终身成就性质 |
| master of the contemporary short story | 当代短篇小说大师 | 诺奖理由原词 |
| self-editor | 自我修订者 | 版本学关键词 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（49k views，较高受众 / 宏大 / 深远）
- **匹配理由**:
  - 「宏大/深远」匹配其形式遗产 —— 把小说的史诗复杂性装进几页短篇，革新一种文体的影响是长期而深远的
  - 沉静的长线旋律匹配其叙事气质 —— 不动声色、时间往复、结尾的暧昧余韵
  - 与深紫主色 #372A75 的暮色调相称，衬「老照片色块」的设计母题
- **备选**（未采用）：★★ Nostalgia（怀旧/温和，匹配小镇记忆但略轻）
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` → 复制到本目录 `Eternals.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Alice_Munro/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `literature/generate_21st_century_list.py` | 获奖理由中译（CITATION_ZH）对照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
