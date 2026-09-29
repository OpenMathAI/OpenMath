# 和平奖得主立传提示词（OpenPeace 实例：Elie Wiesel）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」的批次实例**，
> 以 Elie Wiesel（1986 诺贝尔和平奖，大屠杀幸存者与作家）为对象。
> 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Eliezer "Elie" Wiesel（埃利·维瑟尔）——大屠杀幸存者、《夜》的作者、"人类的信使"，文学书写与社会行动合一的立传对象。
- **设计哲学**：Wiesel 立传的核心张力在于**「见证」（witness）与「沉默的打破」（breaking silence）**——版面以「黑暗中的证言」为视觉主线，书页/烛火意象贯穿，同时保留身份信息页与领域结构化骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：Eliezer "Elie" Wiesel（1928-09-30 ~ 2016-07-02，享年 87 岁）
- **诺奖年份与官方获奖理由**：1986 年诺贝尔和平奖（独得）：
  > "for being a messenger to mankind: his message is one of peace, atonement and dignity"
  > （表彰他作为人类的信使：他所传递的是和平、救赎与尊严的讯息）
  > ※ 中译以名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` 为准，禁止改写。
- **气质关键词**：**大屠杀的见证者、沉默的打破者、人类的信使**
- **设计母题**：**夜与见证（night & witness）**——代表作《Night》（夜）与集中营囚号 A-7713；版面用深底色 + 烛光/书页意象，呼应"沉默鼓励施暴者，从不鼓励受害者"的核心理念。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Elie_Wiesel/page.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地页面与事实基准 【人物专属】

- 事实基准（以本地 page.md 为准）：
  - 生卒（1928-09-30 生于罗马尼亚锡盖特（Sighet，今 Sighetu Marmației）~ 2016-07-02 逝于曼哈顿家中，享年 87 岁；葬于纽约 Valhalla 的 Sharon Gardens Cemetery，2016-07-03 下葬）
  - 国籍变迁（罗马尼亚 ~1940 → 匈牙利 1940–1944 → 无国籍 1944–1963 → 美国 1963–2016；四段口径以 infobox 为准）
  - 家庭（父 Shlomo Wiesel 代表"理性"；母 Sarah Feig 代表"信仰"；姐 Beatrice、Hilda 幸存；妹 Tzipora 与父母均死于大屠杀；妻 Marion Erster Rose（奥地利裔，1969 成婚，2025-02-02 去世，享年 94），多部著作英译者；子 Shlomo Elisha Wiesel（Elisha））
  - 教育（巴黎大学（索邦）文学/哲学/心理学；家中母语意第绪语，兼德/匈/罗语）
  - 任职履历（19 岁起任记者（法国/以色列报刊，Yedioth Ahronoth 巴黎与巡回国际通讯员）；1955 移居纽约；CUNY 卓越教授 1972–1976；波士顿大学 Andrew Mellon 人文学教授 1976 起（宗教与哲学系，BU 设立 Elie Wiesel Center for Jewish Studies）；Yale Henry Luce 访问学者 1982；Barnard/Columbia 访问教授 1997–1999；Chapman 大学杰出总统研究员 2010 起）
  - 关键荣誉（Congressional Gold Medal 1984/1985 两口径：Awards 节作 1984，正文另有 1985 口径，以 Works/Awards 清单 1984 为准；法国荣誉军团勋章 Commander 1984 / Grand Officer 1990 / Grand Cross 2000；Nobel Peace Prize 1986；Presidential Medal of Freedom 1992；美国艺术暨文学学会 1996 当选；荣誉爵士 2006-11-30；Dayton Literary Peace Prize 终身成就奖 2007）
  - 核心事业清单（见第 4 步）
  - 关键时间线（15–20 节点：1928 出生 → 1944-03 德占匈牙利、入隔离区 → 1944-05 驱逐至奥斯维辛 → 1945-04-11 布痕瓦尔德获释（囚号 A-7713）→ 1945 法国孤儿院 → 索邦求学 → 1949 赴以色列任通讯员 → 1955 移居纽约 → 1956 意第绪语回忆录《And the World Remained Silent》→ 1958 法文《La Nuit》→ 1960 英文《Night》→ 1972–76 CUNY → 1976 波士顿大学 → 1978–86 美国总统大屠杀委员会主席 → 1986 与妻创 Elie Wiesel Foundation for Humanity → 1986-12-10 诺贝尔和平奖 → 1993 美国大屠杀纪念博物馆开馆 → 1999 "The Perils of Indifference" 演讲 → 2003 披露罗马尼亚死亡营屠犹 28 万人 → 2006 陪同 Oprah 访奥斯维辛 → 2006 获英国荣誉爵士 → 2007 遭否认大屠杀者袭击未受伤 → 2009 陪同 Obama/Merkel 重访布痕瓦尔德 → 2012 抗议匈牙利"漂白"并退回大十字勋章 → 2016-07-02 辞世）
- 指定完整引语（page.md 实载原文，可整段引用）：《Night》开篇 "Never shall I forget..." 段；诺贝尔演说 "Silence encourages the tormentor, never the tormented..." 句；1990 March of the Living 演讲 "We were convinced that antisemitism perished here..." 句

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Elie_Wiesel/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=Elie_Wiesel_zh`、`VIDEO_NAME=Elie_Wiesel_zh`

### 第 3 步：收集图片 【人物专属】

- 优先从 `images.txt` 选真实肖像（infobox 1996 照或 1987 Erling Mandelmann 照）
- 下载失败则用装饰圆占位（Commons → REST API 回退）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Wiesel 的事业领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Holocaust literature | 大屠杀文学 | 《Night》与 57 部著作，1986 诺奖根基 | 封面、文学页 |
| 1 | human rights | 人权 | 全球受迫害群体的代言与倡议 | 行动页 |
| 2 | Holocaust education | 大屠杀教育 | 大屠杀纪念委员会主席、纪念博物馆建设 | 纪念页 |
| 3 | journalism | 新闻 | 战后至纽约时期的记者生涯 | 记者页 |
| 4 | Jewish studies | 犹太研究 | 波士顿大学宗教与哲学系教席 | 教学页 |

#### 4.1 入库操作

- 更新既有 `people` 主记录（`name_en='Elie Wiesel'`，库内 id=4895，UPD 回填 qid=Q18391），`primary_occupation='writer'`、`has_social_data=1`、`has_biography=0`
- 关联职业 `writer`（rank 0）、`professor`（rank 1）、`journalist`（rank 2）；国籍 `United States`（rank 0）+ `Romania`（rank 1，出生地口径）
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先建字典项

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marion Erster Rose | 无向 | 1969 年成婚，多部著作英译者，基金会共同创始人 |
| parent-child | Elisha Wiesel | 父→子 | 独子 Shlomo Elisha Wiesel，承继基金会 |
| influence | François Mauriac | 对方→Wiesel | 1952 文学奖得主，劝说其打破十年沉默写作《Night》，后成挚友 |
| influence | Menachem Mendel Schneerson | 对方→Wiesel | 卢巴维奇拉比，长年私谈与通信，说服其成婚重建家庭 |
| colleague | Leonard Fein | 无向 | 1975 年共同创办《Moment》杂志 |
| colleague | Sigmund Strochlitz | 无向 | 大屠杀纪念委员会时期的密友与知己 |
| controversy | Bernard L. Madoff | 无向 | 基金会资产投资其庞氏骗局，损失 1500 万美元及夫妻大半积蓄 |

#### 4.5.1 入库操作

- 以 `name_en='Elie Wiesel'`（库内 id=4895）为中心写入 `person_relation`
- 方向约定：influence 有向（影响者→Wiesel）、parent-child 有向；其余无向自动归一
- 对手方沿用库内形式（`François Mauriac` 已有 id=4891 勿新建）；缺失人物先建占位（`has_biography=0`）
- 无载禁写：Oprah Winfrey / George Clooney / Buber / Sartre 仅是接触或听众关系不入库；1988 第一届 March of the Living 主席团成员是活动参与，不与任何个人建关系

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **配色**：manifest 预分配主色 **靛蓝 `#283593`** + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeNight` 见证与文学 — 深红 `#A63A2B`
  - `badgeHR` 人权行动 — 青绿 `#0E7C7B`
  - `badgeMemo` 大屠杀教育 — 琥珀 `#E07B30`
  - `badgeTeach` 教席与犹太研究 — 紫 `#52307C`
- **背景母题**：深底 + 烛光光晕 + 书页线条（"夜"的母题）

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 人类的信使 / Elie Wiesel 1928–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、国籍四段变迁、教育、教席、荣誉、核心领域）
03  核心事业概览 — 大屠杀文学 / 人权 / 大屠杀教育 / 新闻 / 犹太研究
04  早年：锡盖特 (1928–1944) — 意第绪语家庭、父之理性母之信仰、拉比世家溯源
05  大屠杀：从隔离区到布痕瓦尔德 (1944–1945) — A-7713、与父亲、1945-04-11 获释
06  重建与沉默 (1945–1955) — 法国孤儿院、索邦、记者生涯、十年拒绝书写
07  Mauriac 与《Night》的诞生 — 劝写经历、意第绪语原稿 → 法文 La Nuit → 英文 Night
08  波士顿大学与教学生涯 (1972–) — CUNY、BU、Yale、Barnard、Chapman
09  大屠杀记忆的制度化 (1978–1993) — 总统委员会主席、纪念博物馆、Strochlitz
10  1986 诺贝尔和平奖 — 获奖理由原句 + "Silence encourages the tormentor" 演说句
11  见证者的行动版图 — 苏联犹太人/埃塞俄比亚犹太人/达尔富尔/罗兴亚等倡议清单
12  基金会与Madoff风波 (1986–2009) — 与妻共创基金会、损失 1500 万（仅客观事实）
13  晚年与荣誉 — 荣誉爵士、Dayton 终身成就、退回匈牙利大十字（客观记录）
14  遗产：《夜》的百年回响 — "No human being is illegal" 与 "The Perils of Indifference"
15  结尾 — OpenMathAI 品牌口径
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Wiesel 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方措辞 "for being a messenger to mankind: his message is one of peace, atonement and dignity"；挪威诺奖委员会另称其 "messenger to mankind"，两处同源勿改写；1986 为独得年份 |
| 国籍口径 | 四段变迁（罗马尼亚→匈牙利→无国籍→美国）在身份信息页完整呈现，封面/尾页只用 "United States" |
| Congressional Gold Medal 年份 | Awards 清单作 1984，正文获奖理由节另有 1985 口径——两处均为 page.md 实载，采用清单 1984 并在陷阱表注记，勿擅自归一 |
| 《Night》版本链 | 意第绪语原稿《Un di velt hot geshvign》→ 法文《La Nuit》→ 英文《Night》(1960)；Awards 节年份作 1956、正文叙述作 1955/1958，按上下文引用并注记两说 |
| Mauriac 角色 | Mauriac 是「劝说打破沉默的引路人」，非导师/合著者；用 influence 不用 advisor-student |
| Schneerson | 卢巴维奇拉比与 Wiesel 的私谈/通信（Igrot Kodesh）为 page.md 明载，说服其成婚；用 influence，勿写"导师" |
| Madoff 事件 | 仅客观记录损失金额（基金会 1500 万美元 + 个人积蓄），不加评价性语句 |
| 政治敏感红线 | 以色列–巴勒斯坦立场、亚美尼亚种族灭绝会议事件（1982 应以色列外交部要求辞职并施压）、2015 内塔尼亚胡国会演讲背书等一律只作 page.md 明载的客观事实记录，禁加评价；勿大段引用政治性原文 |
| 袭击事件 | 2007 年 Eric Hunt 袭击仅客观一句（Holocaust denier 身份、未被拘捕受伤细节按原文）；勿渲染 |
| 子女 | 独子 Elisha（Shlomo Elisha Wiesel）；2017 年代父出席 March of the Living，一句带过 |
| 妻子卒年 | Marion Wiesel 2025-02-02 去世（94 岁），可写入晚年节 |
| 兄妹 | 姐 Beatrice/Hilda 幸存、妹 Tzipora 遇难——家庭页一句客观记录 |
| 演讲年份 | "The Perils of Indifference" 为 1999-04（华盛顿），勿写 1995 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Holocaust | 大屠杀 | 专指纳粹屠犹，首字母大写 |
| witness | 见证者 | Wiesel 自我定位核心词 |
| messenger to mankind | 人类的信使 | 诺奖委员会用语 |
| Night | 《夜》 | 回忆录代表作，书名斜体 |
| Sighet | 锡盖特 | 今 Sighetu Marmației |
| Buchenwald | 布痕瓦尔德 | 1945-04-11 美军第三军团解放 |
| Auschwitz | 奥斯维辛 | 1944-05 驱逐目的地 |
| statelessness | 无国籍 | 1944–1963 段 |
| Yiddish | 意第绪语 | 原稿语言 |
| refusenik | 拒绝移民者 | 苏联犹太人议题用语 |
| Elie Wiesel Foundation for Humanity | 埃利·维瑟尔人道基金会 | 1986 与妻共创 |
| posthumous baptism | 代理死后洗礼 | 2012 抗议事件术语 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Tragedy** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 悲怆 / 深沉 / 庄重
- **匹配理由**:
  - "Tragedy"（悲怆）直面大屠杀主题的重量——《Night》与 A-7713 无法用轻快配乐托举
  - 悲怆之后的余韵契合"作证以防重演"的信使使命，而非沉溺
  - 庄重的节奏匹配诺贝尔演说 "Silence encourages the tormentor" 的断句感
- **本地路径**: `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` → `presentations/20th_century/Elie_Wiesel/Tragedy.wav`
- **时长**: 以实际文件为准，16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Elie_Wiesel/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/presentations/cover/openpeace_page.tex` | 项目首页模板 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，UPD 回填库内 id=4895） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；政治敏感内容只作客观事实记录。**
