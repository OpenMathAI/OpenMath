# 文学家立传提示词（OpenLiterature · 21 世纪 · Abdulrazak Gurnah）

> **本文件是 OpenLiterature 21 世纪批次的人物专属立传提示词**，目标人物：Abdulrazak Gurnah（2021 年诺贝尔文学奖得主，坦桑尼亚裔英国小说家）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）；文学家适配：无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各人物侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Abdulrazak Gurnah（阿卜杜勒拉扎克·古尔纳），2021 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传与科学家立传的核心差异，在于以**作品意象与语言质地**为骨架——本篇以「离散与归返」为视觉母题，强调「身份信息页」（Identity 速览页）与「文学领域表」的结构化表达，务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Abdulrazak Gurnah（1948-12-20 生于桑给巴尔苏丹国，在世）
- **气质关键词**：**后殖民叙事的沉静书写者、流亡与难民命运的记录者、英语文学的边缘改写者** —— 2021 年诺贝尔文学奖获奖理由：
  > "for his uncompromising and compassionate penetration of the effects of colonialism and the fates of the refugee in the gulf between cultures and continents"（表彰其对殖民主义之影响与难民之命运的毫不妥协而富于同情的洞察——那横亘于文化与大陆之间的鸿沟）
- **设计母题**：**两岸之间的海（the sea between shores）**。印度洋海岸、渡船、返乡与离散——Gurnah 的大多数小说发生在东非海岸，主人公多生于桑给巴尔；视觉语言取「海平线 / 船影 / 群岛轮廓」，呼应"文化与大陆之间的鸿沟"。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Abdulrazak_Gurnah/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：`https://en.wikipedia.org/wiki/Abdulrazak_Gurnah`
- **肖像**：第 0 步待下载（page.md 内嵌 Commons 图 `Abdulrazak-Gurnah_DSC06505.jpg`，2024 年 9 月摄影，250px 版 URL 可改 500px）。
- **参考模板**：
  - 数学家/物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`literature/presentations/cover/`（OpenLiterature 共享封面）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），使用 `MySQL/seed_person.py data/Abdulrazak_Gurnah.yaml` 幂等入库。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `page.md`（事实基准如下，第一轮已核对）
- ✅ 待下载头像到 `images/`（Commons 250px 改 500px，curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证）
- **事实基准（以正文为准）**：
  - 生卒：1948-12-20 生于桑给巴尔苏丹国（今属坦桑尼亚），在世（享年按当年实算）
  - frontmatter 生年双值 `["1948-01-01","1948-12-20"]` 有噪声——**取正文/infobox 1948-12-20**
  - 血统与家庭：也门移民商人之子，阿拉伯血统；妻 Denise DeCaires Narain（圭亚那出生的文学学者）
  - 国籍：英国（公民）+ 坦桑尼亚（出生地），至今与坦桑保持紧密联系
  - 教育：Canterbury Christ Church College（学位由伦敦大学授予，BA）→ University of Kent（MA、PhD 1982，论文《Criteria in the Criticism of West African Fiction》）
  - 任职：1968 年以难民身份抵英；1980–1983 尼日利亚 Bayero University Kano 讲师；后任 Kent 英语与后殖民文学教授至 2017 年退休（荣休教授）；2024-09-01 起任 NYU Abu Dhabi 文学 Arts Professor
  - 关键荣誉：Nobel 2021；Royal Society of Literature Fellow（2006）；RFI Témoin du Monde（2007，By the Sea）；Booker/Whitbread 短名单（Paradise 1994）
  - 核心作品（4–6 条）：*Memory of Departure*（1987）、*Paradise*（1994）、*By the Sea*（2001）、*Desertion*（2005）、*Afterlives*（2020）、*Theft*（2025）
  - 关键时间线（16 节点）：1948 生于桑给巴尔 → 1968 18 岁以难民身份抵英（桑给巴尔革命之后）→ Canterbury 本科 → 1980–83 Kano 讲学 → 1982 Kent 博士 → 1987 处女作 *Memory of Departure* → 1988 *Pilgrims Way* → 1990 *Dottie* → 1994 *Paradise*（Booker/Whitbread 短名单）→ 1996 *Admiring Silence* → 2001 *By the Sea* → 2005 *Desertion* → 2006 当选 FRSL → 2007 RFI 奖 → 2017 从 Kent 退休 / *Gravel Heart* → 2020 *Afterlives* → **2021-10-07 获诺贝尔文学奖** → 2022 *Afterlives* 美国出版（诺奖后抢购潮）→ 2024-09 就任 NYU Abu Dhabi → 2025 小说 *Theft*、BBC Desert Island Discs（5-25）

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `literature/presentations/21st_century/` 下建 `Abdulrazak_Gurnah/` 与 `images/`
- 复制同项目 21 世纪已有 deck 的 Makefile（或最近一位文学得主的），设 `MAIN=Abdulrazak_Gurnah_zh`、`VIDEO_NAME=Abdulrazak_Gurnah_zh`
- 复制 BGM：`music_audio/alex-productions/` 下 Expedition 曲目 wav → 本目录

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Gurnah 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | postcolonial literature | 后殖民文学 | 获奖理由核心：殖民主义之影响 | 诺奖页、贡献页 |
| 1 | exile and displacement | 流离与离散 | 难民/移民叙事，贯穿全部小说 | 主题页 |
| 2 | colonial memory | 殖民记忆 | 桑给巴尔与东非海岸的历史书写 | 历史页 |
| 3 | historical fiction | 历史小说 | *Paradise*/*Afterlives* 的东非殖民史背景 | 作品页 |

#### 4.1 入库操作

- 由 `MySQL/data/Abdulrazak_Gurnah.yaml` 经 `MySQL/seed_person.py` 写入：people 主记录（qid=Q317877、primary_occupation=writer、has_social_data=1、has_biography=0 待 Beamer 后置 1）+ 4 条 `person_field`
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；无载禁写。文学家侧 relation_type 白名单：advisor-student / influence / colleague / spouse / parent-child / rival / controversy。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Denise DeCaires Narain | 无向 | 妻子，圭亚那出生的文学学者 |
| colleague | Salman Rushdie | 无向 | 曾主编《A Companion to Salman Rushdie》（剑桥大学出版社 2007） |

- **不入库说明**：V. S. Naipaul / Zoë Wicomb 仅因"撰文评论"被提及，非社会关系；Swahili 首译者 Ida Hadjivayanis 仅为受访译者；Hamid Dabashi / Bruce King / Felicity Hand / Maaza Mengiste 均为评论者；Achebe 仅因选集出版方关联——均禁建关系。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：诺奖深红 `#8B1A1A`（本批次预分配）
- **辅色**：诺奖香槟金 `#C9A227` + 印度洋青 `#0E7C7B`（海/海岸母题）
- **badgeA–D 四分类色**：
  - `badgeA` 后殖民文学 — 深红 `#8B1A1A`
  - `badgeB` 流离与离散 — 印度洋青 `#0E7C7B`
  - `badgeC` 殖民记忆 — 琥珀 `#E07B30`
  - `badgeD` 历史小说 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以「海平线上的船影与群岛」轮廓呼应离散母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 后殖民叙事的沉静书写者 / Abdulrazak Gurnah 1948– + 四色 badge + 右上头像 + 国籍行（英国 · 坦桑尼亚）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、国籍、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 后殖民文学 / 流离与离散 / 殖民记忆 / 历史小说
04  早年：桑给巴尔少年 (1948–1968) — 也门移民家庭、桑给巴尔革命、18 岁以难民身份抵英
05  流亡与求学 (1968–1982) — Canterbury → Kent 博士《Criteria in the Criticism of West African Fiction》
06  学者生涯 (1980–2017) — Kano 讲学、Kent 教授、荣休；NYU Abu Dhabi (2024–)
07  处女作与成名前十年 (1987–1996) — Memory of Departure / Pilgrims Way / Dottie / Admiring Silence
08  《Paradise》(1994) — Booker/Whitbread 短名单、东非殖民史的大写意象【书影/意象图式页】
09  海岸三部曲 — By the Sea (2001) / Desertion (2005) / The Last Gift (2011)【引文框页】
10  乡愁引文页 — "I am from there. In my mind I live there."（page.md 实载原文）
11  《Afterlives》与语言政治 (2020–2025) — 斯瓦希里语/阿拉伯语词汇嵌入英语、拒"异化标记"
12  2021 诺贝尔文学奖 — 获奖理由全句 EN+中译、首位 1993 后黑人得主/2007 后非洲得主
13  诺奖之后 — 美国出版抢购潮、NYU Abu Dhabi、Theft (2025)
14  遗产：难民叙事与英语文学的改写
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`
- 头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用最近文学 deck 骨架；品牌口径统一 `OpenMathAI`，引号用半角 `" "`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `latexmk -c && make pdf`，用 `pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标；溢出标准 vbox≤10pt / hbox≤50pt

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Gurnah 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生年噪声 | frontmatter 双值 `1948-01-01/1948-12-20`，**取正文 1948-12-20** |
| 出生地 | 生于**桑给巴尔苏丹国**（1964 年后属坦桑尼亚），勿写"生于坦桑尼亚"（表述为"生于桑给巴尔，今属坦桑尼亚"） |
| 抵英年份 | 正文为 1968 年抵英（18 岁离开），"1960s"是导语的模糊口径，两者并存时以 1968 为准 |
| 学位授予 | Canterbury Christ Church College 本科学位当时由**伦敦大学**授予，勿写成该校自带学位 |
| 诺奖第一 | 是"1993 年 Toni Morrison 之后的首位黑人得主 / 2007 年 Doris Lessing 之后的首位非洲得主"，两个口径勿混、勿写"首位非洲黑人得主" |
| 商业成绩 | 诺奖前"商业上不成功、部分作品未在英国以外出版"是 page.md 明载，可写；勿美化 |
| 政治联署 | 支持抵制以色列文化机构等联署系政治敏感内容，立传中**禁写** |
| 无载禁写 | 无博士导师记载、无文学师承记载（影响者禁编造）；子女未具名禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| postcolonial literature | 后殖民文学 | 非"殖民后期文学" |
| refugee | 难民 | 获奖理由关键词 |
| Sultanate of Zanzibar | 桑给巴尔苏丹国 | 1964 年前的政体名 |
| Zanzibar Revolution | 桑给巴尔革命 | 客观背景，不展开政治叙事 |
| Booker Prize (shortlist) | 布克奖（短名单） | Paradise 是 shortlist 非 winner |
| FRSL | 英国皇家文学学会会士 | 2006 年当选 |
| emeritus professor | 荣休教授 | Kent 2017 退休 |
| Swahili | 斯瓦希里语 | 母语，文学语言为英语 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（批次预分配）
- **匹配理由**：
  - "远征/旅途"标签完美匹配 Gurnah 的主题本质——从桑给巴尔到英格兰的难民之旅、小说中反复出现的渡海与归返
  - 纪录片气质匹配"流亡学者—作家"双线叙事，庄重而不失温度，呼应获奖理由中 compassionate 一词
  - 与批次内其他曲目（Timeless/PAST 等）不重复
- **本地路径**：`music_audio/alex-productions/` Expedition 曲目 wav → `presentations/21st_century/Abdulrazak_Gurnah/Expedition.wav`
- **时长**：> 16 页 × 7 秒 ≈ 112 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Abdulrazak_Gurnah/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_21st_century_list.py` | 官方获奖理由 EN+中译（CITATION_ZH，禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Abdulrazak_Gurnah.yaml` | 入库 yaml（字段母本 = `MySQL/data/Kenneth_G_Wilson.yaml`） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## 六、执行清单（一次性核对） 【模板通用】

- [ ] 肖像已下载并验证（500px，`file` 确认 JPEG/PNG，非 HTML）
- [ ] Makefile：`MAIN=Abdulrazak_Gurnah_zh`、`VIDEO_NAME=Abdulrazak_Gurnah_zh`
- [ ] BGM Expedition wav 已复制到本目录
- [ ] 编译 0 error、vbox≤10pt、hbox≤50pt
- [ ] `pdftoppm` 逐页目检（页数与第 6 步规划一致，勿合并帧）
- [ ] 提示词与 yaml 的领域表/关系表逐行一致
- [ ] 获奖理由 EN+中译与 `generate_21st_century_list.py` CITATION_ZH 逐字一致
- [ ] 政治联署内容零出现
- [ ] make images + make video 产出 mp4
- [ ] Review-1 修正写回本提示词 §5 对应陷阱行
