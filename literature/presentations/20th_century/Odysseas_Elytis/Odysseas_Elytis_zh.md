# 文学家立传提示词（OpenLiterature：Odysseas Elytis）

> **本文件是 OpenLiterature 的人物专属立传提示词**，以 Kenneth G. Wilson（OpenPhysicist 模板标杆）为骨架，适配文学家。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Elytis 定制内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合 OpenPhysicist 标杆（Kenneth G. Wilson 提示词 + tex 结构）与文学家侧实战经验。
- **本实例**：Odysseas Elytis（奥季修斯·埃利蒂斯），1979 诺贝尔文学奖得主，希腊浪漫现代主义诗歌的定音者。
- **设计哲学**：文学家立传与物理学家立传的核心差异，在于**没有公式框——以代表作书影 / 名句引文框 / 意象图式替代**；仍须保留「身份信息页」（Identity / Bio 速览页）与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Odysseas Elytis（本名 Odysseas Alepoudelis，1911-11-02 ~ 1996-03-18，享年 84 岁）
- **气质关键词**：**爱琴海的太阳崇拜者、浪漫现代主义的定音者、希腊诗歌的纪念碑建造者** —— 1979 诺贝尔文学奖获奖理由：
  > "for his poetry, which, against the background of Greek tradition, depicts with sensuous strength and intellectual clear-sightedness modern man's struggle for freedom and creativeness"
  > （表彰其诗歌，以希腊传统为背景，以感性的力量与理智的清明描绘了现代人为自由与创造而进行的抗争）
- **设计母题**：**太阳的形而上学（the metaphysics of the sun）**。Elytis 自命为太阳的「崇拜者-偶像奉祀者」——透明、光、爱琴海的蓝与白，是其诗歌的核心意象系统；版式语言宜用大块光晕、圆形光辉与蓝白渐变呼应「透明性」的诗学追求。
- **本地数据源**：`literature/presentations/pages/20th_century/Odysseas_Elytis/page.md`（Wikipedia 全文 + frontmatter）+ 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Odysseas_Elytis （肖像第 0 步标「待下载」）
- **参考模板**：
  - 提示词结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`，以文学侧共享封面为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面已下载（`page.md` / `page.html` / `metadata.json` / `images.txt` 四件套齐备）
- 肖像：**待下载**（infobox 照片 "Elytis in 1974"；404 则用 Commons Special:FilePath 或 Wikipedia REST API 回退，仍失败用装饰圆占位）
- 提取 infobox 与正文，**事实基准如下（正文优先）**：
  - 生卒：1911-11-02 生于克里特伊拉克利翁（Heraklion）~ 1996-03-18 逝于雅典（心力衰竭），享年 84 岁
  - 本名 Odysseas Alepoudelis（Αλεπουδέλης），笔名 Elytis；家中六个孩子中最幼
  - 家庭：父 Panayiotis（肥皂与橄榄油实业家，1925 年夏死于肺炎，曾写诗未刊）；母 Maria E. Vrana（1880–1960）；姐 Myrsine 1918 年死于西班牙流感
  - 1914 年举家迁雅典；1927 年确诊肺结核，疗养期间遍读希腊诗歌、**发现卡瓦菲（Cavafy）**
  - 教育：1928 年入雅典大学法学院，未参加毕业考试、未获学位（infobox: no degree）；曾想当律师、也想像超现实主义者那样当画家，均被劝止
  - 1929 年立志只做诗人；1935 年在 Seferis 等友人促成下于《新文学》（Νέα Γράμματα）11 月号发表第一首诗，**笔名 Elytis 由此确立**
  - 1935 年与作家兼精神分析学家 Andreas Embirikos 结为终身挚友（获准翻阅其海量藏书）
  - 战争：1937 年科孚军校服役；二战任中尉，先在第一军团司令部、后调第 24 团第一线；1941 年患急性肠伤寒几乎死去，德军入侵前夜坚持转移，占领期内在雅典缓慢康复，开始构思《最初的太阳》
  - 任职：希腊国家广播基金会节目主任两任（1945–46、1953–54）；希腊国家剧院行政理事会成员；希腊广播电视行政理事会主席；雅典艺术节咨询委员
  - 巴黎岁月：1948–1952 与 1969–1972 旅居巴黎（军政府时期自我流放），旁听索邦语文与文学课程；经出版人 **Tériade** 结识先锋派（Reverdy、Breton、Tzara、Ungaretti、Matisse、Picasso、Chagall、Giacometti 等）；在巴黎与 Marianina Kriezi 共同生活
  - 1961 年应美国国务院邀请访美三月；1962 年与 Embirikos、Theotokas 访苏联；1965 年与 Theotokas 访保加利亚（向导为诗人 Elisaveta Bagryana）
  - 1967–72 军政府期间从公众视野消失；1972 年自巴黎回雅典，住 Skoufa 23 号五楼（最后居所）
  - 晚年：最后 13 年与伴侣 Ioulita Iliopoulou（小他 53 岁）共同生活；未婚
  - 关键荣誉：1960 首届国家诗歌奖（《Axion Esti》）；1965 凤凰勋章；1975 塞萨洛尼基大学荣誉博士 + 米蒂利尼荣誉市民；1979 诺贝尔文学奖；巴黎索邦大学荣誉博士
  - 核心：代表作《正当》（To Axion Esti, 1959）——「当代诗歌的纪念碑」，1964 年由 Theodorakis 谱成清唱剧首演，成为全希腊传唱的颂歌
  - 个人信仰：命理学（圣经/卡巴拉/迦勒底/毕达哥拉斯）、吠陀占星；主张火葬合法化、安乐死合法化与女性堕胎选择权（希腊东正教不允许火葬，遗愿未能实现）
  - 关键时间线（17 节点）：1911 生于伊拉克利翁 → 1914 迁雅典 → 1918 姐殁（西班牙流感）→ 1925 父殁 → 1927 肺结核·发现卡瓦菲 → 1928 入雅典大学法学院 → 1929 立志为诗人 → 1935 首诗发表·笔名确立 → 1937 科孚军校 → 1940–41 战争一线·伤寒 → 1939《方向》→ 1943《最初的太阳》→ 1945/1953 两任国家广播节目主任 → 1948–52 巴黎（先锋派·Tériade）→ 1959《正当》→ 1960 首届国家诗歌奖 → 1964《正当》清唱剧首演 → 1965 凤凰勋章 → 1967–72 军政府·自我流放巴黎 → 1975 荣誉博士 → 1979 诺贝尔奖 → 1983–95《小水手》《奥克索佩特拉挽歌》《悲伤以西》→ 1996 逝于雅典

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下建 `Odysseas_Elytis/` 与 `images/`（本提示词已在该目录中）

### 第 2 步：复制 Makefile 【模板通用】

- 复制同侧已立传成品的 Makefile，设置 `MAIN=Odysseas_Elytis_zh`、`VIDEO_NAME=Odysseas_Elytis_zh`

### 第 3 步：收集图片 【人物专属】

- 下载肖像到 `images/Elytis.jpg`（Wikipedia infobox 照片，1974 年摄）；`curl -A "Mozilla/5.0"` + `file` 验证；失败则装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Elytis 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modern Greek poetry | 现代希腊诗歌 | 四十余年主阵地，《正当》为当代诗歌纪念碑 | 封面、核心页 |
| 1 | romantic modernism | 浪漫现代主义 | 被视为希腊乃至世界浪漫现代主义的定音者 | 核心页 |
| 2 | generation of the '30s | 「三十年代一代」 | 与 Seferis/Embirikos/Ritsos/Gatsos 同代，革新战后希腊诗 | 诗派页 |
| 3 | poetry translation | 诗歌翻译 | 译萨福、《启示录》，其作被译成 11 种语言 | 翻译页 |
| 4 | essay writing | 散文随笔 | 《公开的纸牌》等理论哲学随笔、艺术评论 | 随笔页 |

#### 4.1 入库操作

- `python3 seed_person.py data/Odysseas_Elytis.yaml`（幂等；主记录 `primary_occupation='writer'`、`has_social_data=1`）
- 职业关联：writer（rank 0）、poet（rank 1）、translator（rank 2）
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | C. P. Cavafy | 单向 | 1927 年结核疗养期间发现并深读其诗 |
| colleague | George Seferis | 无向 | 同代诗人，促成 1935 年首诗发表于《新文学》 |
| colleague | Andreas Embirikos | 无向 | 1935 年起的终身挚友，共享其藏书；1977 年为他写纪念文集 |
| colleague | Nikos Gatsos | 无向 | 挚友，同代诗人 |
| colleague | Yiannis Ritsos | 无向 | 同代诗人，关系融洽 |
| colleague | Mikis Theodorakis | 无向 | 为《正当》谱曲成清唱剧，1964 年首演 |
| colleague | Giorgos Theotokas | 无向 | 挚友，1962 同访苏联、1965 同访保加利亚 |
| colleague | Tériade | 无向 | 莱斯博斯同乡出版人，1939 年出版首部诗集《方向》 |

> **不入库说明**：先锋派诸家（Breton/Picasso/Matisse 等）仅「受其接待」，非明载思想影响；Marianina Kriezi、Ioulita Iliopoulou 为未具婚姻的伴侣，无适用关系类型，仅在提示词与立传正文客观简述。

#### 4.5.1 入库操作

- 以 `name_en='Odysseas Elytis'`（Q160478）为中心写入 `person_relation`；Seferis 沿用库内既有记录（George Seferis, id=5172）
- 缺失人物自动建 stub（`has_biography=0`）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：透明、光感、爱琴海蓝白
- **配色**：深海松绿（主色）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeSun` 太阳形而上学 — 金橙 `#E07B30`
  - `badgeAegean` 爱琴海意象 — 爱琴蓝 `#1B6B8F`
  - `badgeAxion` 《正当》/ 清唱剧 — 深红 `#A31621`
  - `badgeEssay` 随笔与翻译 — 橄榄绿 `#5C6B3C`
- **背景母题**：大块柔和实心圆错落（光辉/太阳隐喻），蓝白渐变底呼应爱琴海与「透明性」

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注。
2. **封面有国籍**：明示 Greece；底部状态栏给出 `国籍 | 语言 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前，左头像 + 右信息网格（生卒、本名/笔名、国籍、出生地、教育、任职、主要荣誉、核心领域）。
4. **无公式框**：以《正当》名句引文框（"Greek the language they gave me; poor the house on Homer's shores."）与代表作书影、意象图式替代。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover 共享首页）
01  封面 — 太阳的形而上学家 / Odysseas Elytis 1911–1996 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名/笔名、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 《正当》/ 爱琴海意象 / 三十年代一代 / 随笔与翻译
04  早年：克里特与雅典 (1911–1934) — 六子之末、肺结核与卡瓦菲、立志为诗人
05  1935：笔名的诞生 — 《新文学》首诗、Embirikos 与藏书
06  战争与伤寒 (1937–1945) — 阿尔巴尼亚前线、中尉、《最初的太阳》构思
07  《方向》与《最初的太阳》— 早期诗集与「内在建筑」
08  《正当》(1959)（核心页·名句引文框）— 当代诗歌的纪念碑
09  Theodorakis 与清唱剧 (1964) — 从诗到全民族传唱的颂歌
10  巴黎岁月与 Tériade — 先锋派、萨福翻译、莱斯博斯同乡
11  军政府与自我流放 (1967–1972) — 从公众视野消失、拒绝军政府资助
12  晚期诗集 — 《光之树》《玛丽亚·奈弗利》《小水手》《奥克索佩特拉挽歌》
13  荣誉与认可 — Nobel 1979 · 国家诗歌奖 1960 · 凤凰勋章 1965 · 荣誉博士
14  遗产：为自由与创造而歌
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 宏名禁数字、禁 `\u00b7`；`\foreach` 分隔符用 ASCII 逗号。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
- 取日志单遍 xelatex 后须重新 `make pdf`（防 remember picture 错乱）。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Elytis 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名与笔名 | 本名 Odysseas Alepoudelis，笔名 Elytis 为 1935 年首次发表时确立；勿把 Alepoudelis 写成姓氏变体 |
| 生卒 | 1911-11-02 生于伊拉克利翁（克里特）；1996-03-18 逝于雅典（心力衰竭）；享年 84 岁 |
| 学位 | 雅典大学法学院**未获学位**（infobox: no degree），勿写「法学毕业」 |
| 与 Seferis 关系 | 是同代挚友与文坛引路人（促成首诗发表），**非师承**；不要写成师生关系 |
| 《正当》年份 | 诗集 1959 年出版；清唱剧由 Theodorakis 谱曲、**1964 年首演**；两处年份勿混 |
| 荣誉双份 | 1960 首届国家诗歌奖（First State/First National Prize for poetry）与 1979 诺贝尔奖分列；索邦荣誉博士与塞萨洛尼基大学荣誉博士（1975）并列 |
| 巴黎年份 | 两段：1948–1952 与 1969–1972（自我流放）；勿合并成一段 |
| 伴侣 | Marianina Kriezi（巴黎时期）、Ioulita Iliopoulou（最后 13 年）均**未婚伴侣**，客观简述、不写「妻子」 |
| 引语红线 | 名句 "Greek the language they gave me; poor the house on Homer's shores." 出自《正当》(1959)，page.md 有英文原文可引；其余不得编造中文「原话」 |
| 政治内容 | 军政府时期自我流放只按 page.md 客观事实简述（拒绝军政府资助、旅居巴黎），不作政治评价 |
| 信仰内容 | 命理学/占星与火葬、安乐死、堕胎权主张均为 page.md 明载，客观简述即可，不展开不评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| To Axion Esti | 《正当》/《值得称颂》 | 通行《正当》；礼文用语 "It Is Worthy" |
| the metaphysics of the sun | 太阳的形而上学 | Elytis 自命「崇拜者-偶像奉祀者」 |
| Generation of the '30s | 三十年代一代 | 希腊现代主义诗派，非泛指年代 |
| romantic modernism | 浪漫现代主义 | infobox 用的运动标签 |
| inner architecture | 内在建筑 | 其诗歌技法概念 |
| Tériade | 特里亚德 | 出版人艺名，莱斯博斯同乡 |
| oratorio | 清唱剧 | 《正当》的音乐化形态 |
| AICA | 国际艺术评论协会 | 其为希腊艺评协会会员 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions
- **风格**: 辽阔 / 空灵 / 海洋感
- **匹配理由**:
  - "海洋感" 直接对应 Elytis 的爱琴海意象系统——蓝色、白色、日光与岛屿是其诗歌的底色
  - "辽阔" 匹配其诗歌的空间性——从伊拉克利翁到雅典到巴黎，诗行始终朝向开放的地中海
  - "空灵" 匹配「透明性」诗学与太阳形而上学的轻盈质感
- **本地路径**: `music_audio/alex-productions/` 下 SEA 曲目 → `presentations/20th_century/Odysseas_Elytis/SEA.wav`
- **时长**: 以实际曲目为准，`ffmpeg -shortest` 自动对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；引语只用 page.md 英文原文。**
