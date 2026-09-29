# 文学家立传提示词（OpenLiterature · 21 世纪 · László Krasznahorkai）

> **本文件是 OpenLiterature 21 世纪批次的人物专属立传提示词**，目标人物：László Krasznahorkai（2025 年诺贝尔文学奖得主，匈牙利小说家/编剧）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）；文学家适配：无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各人物侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：László Krasznahorkai（拉斯洛·克拉斯诺霍尔卡伊），2025 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传以**作品意象与语言质地**为骨架——本篇以「末世中的长镜头」为视觉母题，强调「身份信息页」（Identity 速览页）与「文学领域表」的结构化表达，务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：László Krasznahorkai（1954-01-05 生于匈牙利久洛，在世）
- **气质关键词**：**末世论者、长句大师、贝拉·塔尔的电影共谋者** —— 2025 年诺贝尔文学奖获奖理由：
  > "for his compelling and visionary oeuvre that, in the midst of apocalyptic terror, reaffirms the power of art"（表彰其引人入胜而富于远见的作品，在末世般的恐惧中重申了艺术的力量）
- **设计母题**：**末世中的长镜头（the long take of apocalypse）**。《撒旦探戈》的十二步探戈结构、鲸鱼驶过小镇、蒙古草原与京都枯山水；视觉语言取「长焦剪影 / 雨夜路灯 / 郸郸烟尘」，呼应"在末世恐惧中重申艺术力量"。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/László_Krasznahorkai/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：`https://en.wikipedia.org/wiki/László_Krasznahorkai`
- **肖像**：第 0 步待下载（见 images.txt；infobox 无照片则装饰圆占位）。
- **参考模板**：
  - 数学家/物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`literature/presentations/cover/`（OpenLiterature 共享封面）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），使用 `MySQL/seed_person.py data/László_Krasznahorkai.yaml` 幂等入库。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `page.md`（事实基准如下，第一轮已核对）
- ✅ 待下载头像到 `images/`（Commons 250px 改 500px，curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证）
- **事实基准（以正文为准）**：
  - 生卒：1954-01-05 生于匈牙利东部久洛（Gyula），在世；中产家庭——父 György Krasznahorkai 律师、母 Júlia Pálinkás 社保行政员
  - 家族：父系有犹太血统（本人访谈自述，11 岁左右才被告知）；祖父 1931 年把姓由 Korim（或 Korin）改为 Krasznahorkai；外祖系特兰西瓦尼亚 hajduk 后裔（本人自述）；兄 Géza 曾任久洛市图书馆馆长
  - 婚姻与子女：一婚 Anikó Pelyhe（1990–离异）；1997 娶汉学家兼平面设计师 Dóra Kopcsányi；三女，其中 Ágnes 为演员（2023 年电影《Without Air》主演）
  - 教育：1968–72 久洛 Erkel Ferenc 高中（拉丁语方向）；少年时在爵士/节拍乐队弹钢琴；1973 入塞格德 József Attila 大学（今塞格德大学）读法律三周即辍学、躲避二次兵役期间做过马夫/文化辅导员/矿工；1976–78 布达佩斯 ELTE 法律系；1978–83 ELTE 人文学院匈牙利语与文化教育专业毕业，论文研究流亡后的 Sándor Márai
  - 任职：1977–82 Gondolat 出版社文献员；毕业后自由作家；曾居柏林多年（2014 春哥伦比亚大学 Harriman 研究所驻校作家、柏林自由大学 S. Fischer 客座教授一学期）
  - 关键荣誉：Nobel 2025（**继 Imre Kertész 之后第二位匈牙利文学奖得主**）；Man Booker International 2015（首位匈牙利作家）；Best Translated Book Award 2013（*Satantango*）/2014（*Seiobo There Below*，首位两度获 BTBA）；US National Book Award Translated Literature 2019；Kossuth Prize 2004；SWR-Bestenliste 1993；Austrian State Prize for European Literature 2021；Prix Formentor 2024
  - 核心作品（4–6 条）：*Sátántangó*（1985 处女作即成名）、*Az ellenállás melankóliája*（The Melancholy of Resistance，1989）、*Háború és háború*（War and War，1999）、*Seiobo járt odalent*（Seiobo There Below，2008）、*Báró Wenckheim hazatér*（Baron Wenckheim's Homecoming，2016）、*Herscht 07769*（2021）
  - 关键时间线（18 节点）：1954 生于久洛 → 1968–72 高中（拉丁语）/乐队钢琴手 → 1973 塞格德法律三周辍学、马夫/矿工/文化辅导员 → 1977 首篇短篇小说《Tebenned hittem》刊于 *Mozgó Világ* → 1978–83 ELTE 毕业（Márai 论文）→ **1985 处女作《Sátántangó》一举成名** → 1987–88 西柏林 DAAD 柏林艺术家计划 → 1988 *Damnation*（Béla Tarr 电影，首次编剧合作）→ 1989《反抗的忧郁》→ 1990 首次东亚之行（蒙古/中国→《Urga 之囚》）→ 1994 电影《撒旦探戈》（Tarr）→ 1996/2000/2005 三度京都半年（远东美学转变其风格）→ 1999《战争与战争》（Ginsberg 协助）→ 2004 Kossuth Prize → 2008《Seiobo There Below》→ 2011《都灵之马》（与 Tarr 最后合作）→ 2013/2014 两度 BTBA → **2015 Man Booker International（首位匈牙利作家）** → 2019 美国国家图书奖翻译文学奖 → 2024 奥地利国家图书馆收存其文学档案 → **2025 获诺贝尔文学奖（2025 年度奖，2025-10 公布）**

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `literature/presentations/21st_century/` 下建 `László_Krasznahorkai/` 与 `images/`
- 复制同项目 21 世纪已有 deck 的 Makefile，设 `MAIN=László_Krasznahorkai_zh`、`VIDEO_NAME=László_Krasznahorkai_zh`
- 复制 BGM：Tragedy 曲目 wav → 本目录

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Krasznahorkai 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | postmodern fiction | 后现代小说 | page.md 明载 Movement：Postmodernism | 诺奖页、风格页 |
| 1 | apocalyptic fiction | 末世书写 | 获奖理由 apocalyptic terror、Sontag"末世大师" | 主题页 |
| 2 | dystopian fiction | 反乌托邦小说 | 忧郁/对抗/溃败的世界图景 | 主题页 |
| 3 | east asian aesthetics | 东亚美学 | 蒙古/中国/京都之行转变其风格与主题 | 东行页 |
| 4 | screenwriting | 电影编剧 | 与 Béla Tarr 六部合作 | 电影页 |

#### 4.1 入库操作

- 由 `MySQL/data/László_Krasznahorkai.yaml` 经 `MySQL/seed_person.py` 写入：people 主记录（qid=Q512062、primary_occupation=writer、has_social_data=1、has_biography=0 待 Beamer 后置 1）+ 5 条 `person_field`
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；无载禁写。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Béla Tarr | 无向 | 至交；六部电影合作（Damnation 1988 至 The Turin Horse 2011，后者为最后合作） |
| colleague | Max Neumann | 无向 | 德国画家，合著《Animalinside》(2010)/《Chasing Homer》配画 |
| colleague | Allen Ginsberg | 无向 | 写《War and War》期间旅欧获其协助，曾借住其纽约公寓 |
| spouse | Anikó Pelyhe | 无向 | 第一任妻子，1990 结婚后离异 |
| spouse | Dóra Kopcsányi | 无向 | 现任妻子（1997–），汉学家兼平面设计师 |
| parent-child | Ágnes Krasznahorkai | 无向 | 女儿，演员，2023 年电影《Without Air》主演 |

- **不入库说明**：Imre Kertész 仅系"第二位匈牙利得主"排序提及；Susan Sontag / W. G. Sebald 系评论者（引语可用）；Sándor Márai 仅系论文研究对象；George Szirtes / Ottilie Mulzet / John Batki 均为译者；Péter Eötvös 等系其作品歌剧改编者——均禁建关系。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：深渊蓝绿 `#0F4C5C`（本批次预分配）
- **辅色**：诺奖香槟金 `#C9A227` + 烟灰 `#5A5A5A`（雨夜/末世）
- **badgeA–D 四分类色**：
  - `badgeA` 后现代小说 — 深渊蓝绿 `#0F4C5C`
  - `badgeB` 末世书写 — 暗红 `#7E1E23`
  - `badgeC` 东亚美学 — 香槟金 `#C9A227`
  - `badgeD` 电影编剧 — 冷灰 `#37474F`
- **背景母题**：低亮度底色 + 长焦剪影与雨丝线条，呼应"末世中的长镜头"

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 末世中的长镜头 / László Krasznahorkai 1954– + 四色 badge + 右上头像 + 国籍行（匈牙利）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 后现代小说 / 末世书写 / 反乌托邦 / 东亚美学 / 电影编剧
04  早年：久洛少年 (1954–1978) — 律师之家、拉丁语高中、爵士钢琴、法律辍学、马夫与矿工
05  ELTE 与 Márai (1978–1985) — 匈牙利语与文化教育、Márai 流亡研究、Gondolat 出版社
06  《撒旦探戈》(1985) — 处女作即成名、十二步探戈结构、匈牙利文学领军【书影页】
07  柏林与《反抗的忧郁》(1987–1993) — DAAD、SWR-Bestenliste 1993
08  与贝拉·塔尔的电影 (1988–2011) — Damnation/撒旦探戈/鲸鱼马戏/都灵马，2011 最后合作【引文框页】
09  东方之行 (1990–2005) — 蒙古/中国/三度京都、《Urga 之囚》《天穹下的毁灭与哀愁》
10  《战争与战争》与纽约 — Ginsberg 协助、Harriman 驻校、Manhattan Project 日记
11  国际声望 (2008–2020) — Seiobo 两度 BTBA、2015 国际布克（首位匈牙利）、2019 美国国家图书奖
12  2025 诺贝尔文学奖 — 获奖理由全句 EN+中译、继 Kertész 后第二位匈牙利得主
13  评论家眼中的末世大师（引文页）— Sontag"堪比果戈里与梅尔维尔"、Sebald 的评语（英文原文可引）
14  遗产：在末世恐惧中重申艺术的力量
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`
- 头部宏可整体复用最近文学 deck 骨架；品牌口径统一 `OpenMathAI`，引号用半角 `" "`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `latexmk -c && make pdf`，用 `pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标；溢出标准 vbox≤10pt / hbox≤50pt

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Krasznahorkai 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖口径 | 2025 年度奖、2025-10 公布；page.md 授奖段作 "In 2025, he was awarded"；勿写"2026 奖" |
| 匈牙利第二人 | 继 Imre Kertész 之后**第二位**匈牙利文学奖得主，勿写"首位" |
| 大学口径 | 塞格德 József Attila 大学（法律，1973 三周辍学）与 ELTE（法律 1976–78 + 人文 1978–83 毕业）两段勿混；学历终点是 ELTE 人文毕业 |
| 犹太血统 | 系本人访谈自述、祖父 1931 改姓——按 page.md 原样表述，勿渲染 |
| 电影合作 | 六部：Damnation/The Last Boat/Sátántangó/Werckmeister/The Man from London/Turin Horse；Turin Horse（2011）为最后合作，勿再续写 |
| 政治内容 | Views 节对匈政府的批评系政治敏感内容，立传中**禁写**，不作政治评价 |
| 引语红线 | Sontag/Sebald 引语为英文原文可引；Sontag 比较对象是 Gogol 与 Melville，勿换人 |
| 无载禁写 | 无大学导师/文学师承记载；两名女儿未具名禁写；三女仅 Ágnes 具名入库 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Sátántangó / Satantango | 《撒旦探戈》 | 通行中译名 |
| The Melancholy of Resistance | 《反抗的忧郁》 | 通行中译名 |
| War and War | 《战争与战争》 | 通行中译名 |
| Man Booker International Prize | 国际布克奖 | 2015，首位匈牙利作家 |
| Best Translated Book Award | 最佳翻译图书奖 | 2013/2014 两度 |
| Kossuth Prize | 科苏特奖 | 2004，匈牙利最高文化奖 |
| long take | 长镜头 | Tarr 电影美学，比喻用 |
| DAAD Artists-in-Berlin Program | DAAD 柏林艺术家计划 | 1987–88 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（批次预分配）
- **匹配理由**：
  - "悲剧"气质直接对应获奖理由中的 apocalyptic terror（末世般的恐惧）——Krasznahorkai 的作品世界正是溃败、忧郁与末世图景
  - 沉重而庄严的配器匹配《撒旦探戈》七小时长镜头式的叙事密度，压抑之下仍见"艺术的力量"（reaffirms the power of art）
  - 与批次内其他曲目（Expedition/The Flow of Time/Daylight/Savage）不重复
- **本地路径**：`music_audio/alex-productions/` Tragedy 曲目 wav → `presentations/21st_century/László_Krasznahorkai/Tragedy.wav`
- **时长**：> 16 页 × 7 秒 ≈ 112 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/László_Krasznahorkai/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_21st_century_list.py` | 官方获奖理由 EN+中译（CITATION_ZH，禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/László_Krasznahorkai.yaml` | 入库 yaml（字段母本 = `MySQL/data/Kenneth_G_Wilson.yaml`） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## 六、执行清单（一次性核对） 【模板通用】

- [ ] 肖像已下载并验证（或装饰圆占位并记录原因）
- [ ] Makefile：`MAIN=László_Krasznahorkai_zh`、`VIDEO_NAME=László_Krasznahorkai_zh`
- [ ] BGM Tragedy wav 已复制到本目录
- [ ] 编译 0 error、vbox≤10pt、hbox≤50pt
- [ ] `pdftoppm` 逐页目检（页数与第 6 步规划一致，勿合并帧）
- [ ] 提示词与 yaml 的领域表/关系表逐行一致
- [ ] 获奖理由 EN+中译与 `generate_21st_century_list.py` CITATION_ZH 逐字一致（2025 奖、2025-10 公布口径）
- [ ] Views 节政治内容零出现
- [ ] make images + make video 产出 mp4
- [ ] Review-1 修正写回本提示词 §5 对应陷阱行
