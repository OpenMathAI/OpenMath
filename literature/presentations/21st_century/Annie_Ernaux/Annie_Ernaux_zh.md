# 文学家立传提示词（OpenLiterature · 21 世纪 · Annie Ernaux）

> **本文件是 OpenLiterature 21 世纪批次的人物专属立传提示词**，目标人物：Annie Ernaux（2022 年诺贝尔文学奖得主，法国作家）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）；文学家适配：无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各人物侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Annie Thérèse Blanche Ernaux（安妮·埃尔诺），2022 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传以**作品意象与语言质地**为骨架——本篇以「平写的照片」（écriture plate）为视觉母题，强调「身份信息页」（Identity 速览页）与「文学领域表」的结构化表达，务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Annie Ernaux（1940-09-01 生于法国利勒博纳，在世）
- **气质关键词**：**自传书写的大师、社会学的文学近亲、个人记忆的考古者** —— 2022 年诺贝尔文学奖获奖理由：
  > "for the courage and clinical acuity with which she uncovers the roots, estrangements and collective restraints of personal memory"（表彰其以勇气与临床般的敏锐，揭示个人记忆的根源、隔阂与集体桎梏）
- **设计母题**：**平面的照片（la photo plate）**。Ernaux 的写作像一张张"平写的照片"——超市、郊区新镇、家庭合影；视觉语言取「老照片边框 / 超市货架 / 郊区街区网格」，呼应"个人记忆与集体桎梏"。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Annie_Ernaux/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：`https://en.wikipedia.org/wiki/Annie_Ernaux`
- **肖像**：第 0 步待下载（page.md 图注"Ernaux in 2022"，见 images.txt）。
- **参考模板**：
  - 数学家/物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`literature/presentations/cover/`（OpenLiterature 共享封面）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），使用 `MySQL/seed_person.py data/Annie_Ernaux.yaml` 幂等入库。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `page.md`（事实基准如下，第一轮已核对）
- ✅ 待下载头像到 `images/`（Commons 250px 改 500px，curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证）
- **事实基准（以正文为准）**：
  - 生卒：1940-09-01 生于诺曼底利勒博纳（Lillebonne），在世；本名 Duchesne，在 Yvetot 长大
  - 家庭：父母 Blanche (Dumenil) 与 Alphonse Duchesne 在工人街区经营咖啡馆兼杂货店
  - 婚姻与子女：夫 Philippe Ernaux（infobox 作 div. 1980，正文 Personal life 作 1981 离异——两说并存，立传用"1980 年代初离异"回避精确年份）；两子 Éric（1964 生）、David（1968 生）
  - 教育：鲁昂大学、波尔多大学；1971 现代文学深造文凭；曾从事 Marivaux 论文项目（未完成）
  - 任职：1960 伦敦 au pair（后写入 *Mémoire de fille*）；1970 年代初在 Bonneville/Annecy-le-Vieux/Pontoise 任教；后入国家远程教育中心（CNED）工作 23 年；1970 年代中起定居 Cergy-Pontoise
  - 关键荣誉：Nobel 2022（第 16 位法国得主、**首位法国女性**）；Renaudot 1984（*La Place*）；François-Mauriac / Marguerite Duras / Prix de la langue française（均 2008，*Les Années*）；Strega European 2016；Formentor 2019；International Booker 短名单 2019；RSL International Writer 2021
  - 核心作品（4–6 条）：*Les Armoires vides*（1974）、*La Place*（1983）、*Une femme*（1988）、*Passion simple*（1991）、*L'Événement*（2000）、*Les Années*（2008，公认代表作）
  - 关键时间线（16 节点）：1940 生于利勒博纳 → 成长于 Yvetot 父母店中 → 1960 伦敦 au pair → 鲁昂/波尔多求学、1971 文凭 → 1970 年代初外省任教 → 1974 处女作 *Les Armoires vides* → 1976 *Ce qu'ils disent ou rien*、迁居 Cergy-Pontoise → 1983 *La Place* → **1984 勒诺多奖** → 1988 *Une femme* → 1991 *Passion simple* → 2000 *L'Événement* → 2008 *Les Années*（三奖加身）→ 2016 Strega 欧洲奖 → 2019 International Booker 短名单 / Formentor → **2022-10-06 获诺贝尔文学奖** → 2021 电影 *Happening*（L'Événement 改编）获威尼斯金狮

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `literature/presentations/21st_century/` 下建 `Annie_Ernaux/` 与 `images/`
- 复制同项目 21 世纪已有 deck 的 Makefile，设 `MAIN=Annie_Ernaux_zh`、`VIDEO_NAME=Annie_Ernaux_zh`
- 复制 BGM：The Flow of Time 曲目 wav → 本目录

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Ernaux 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | autobiographical writing | 自传书写 | 从虚构转向自传，"平写"（écriture plate） | 诺奖页、风格页 |
| 1 | collective memory | 集体记忆 | *Les Années* 以"elle"写一代人的岁月 | 代表作页 |
| 2 | social class | 社会阶层 | 父母的小店、阶级跨越的羞耻与隔阂 | 主题页 |
| 3 | women's writing | 女性写作 | 堕胎/婚姻/欲望的女性经验书写 | 主题页 |

#### 4.1 入库操作

- 由 `MySQL/data/Annie_Ernaux.yaml` 经 `MySQL/seed_person.py` 写入：people 主记录（qid=Q1153825、primary_occupation=writer、has_social_data=1、has_biography=0 待 Beamer 后置 1）+ 4 条 `person_field`
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；无载禁写。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Philippe Ernaux | 无向 | 前夫，育二子，1980 年代初离异 |
| parent-child | Éric Ernaux | 无向 | 长子，1964 生 |
| parent-child | David Ernaux-Briot | 无向 | 次子，1968 生，纪录片《The Super 8 Years》联合导演 |
| colleague | Marc Marie | 无向 | 合著《L'Usage de la photo》（2005），以照片记录二人爱情 |
| colleague | Frédéric-Yves Jeannet | 无向 | 合著对谈《L'écriture comme un couteau》 |

- **不入库说明**：Alison L. Strayer（译者）按惯例不入库；Emmanuel Macron 仅致贺；Seven Stories Press（以其名命七位创始作者之一）系机构关系；Patrick Modiano / Claire Etcherelli 仅出现于他人论文比较——均禁建关系。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：诺奖沉静蓝 `#1E4E79`（本批次预分配）
- **辅色**：诺奖香槟金 `#C9A227` + 灰调米白 `#D8D3C8`（老照片纸色）
- **badgeA–D 四分类色**：
  - `badgeA` 自传书写 — 沉静蓝 `#1E4E79`
  - `badgeB` 集体记忆 — 香槟金 `#C9A227`
  - `badgeC` 社会阶层 — 砖红 `#A63A2B`
  - `badgeD` 女性写作 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡 + 老照片白边矩形错落，呼应"平写的照片"

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 个人记忆的考古者 / Annie Ernaux 1940– + 四色 badge + 右上头像 + 国籍行（法国）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名、出生地、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 自传书写 / 集体记忆 / 社会阶层 / 女性写作
04  早年：诺曼底小店 (1940–1960) — Yvetot、工人街区、父母的咖啡馆兼杂货店
05  求学与执教 (1960–1974) — 伦敦 au pair、鲁昂/波尔多、CNED 23 年
06  从虚构到自传 (1974–1984) — Les Armoires vides → La Place 与 1984 勒诺多奖
07  父与母 — La Place / Une femme / La Honte：阶级跨越的羞耻【引文框页】
08  身体与欲望 — Passion simple / L'Événement / Mémoire de fille【意象图式页】
09  《Les Années》(2008) — "elle"与一代人的岁月、三奖加身、国际布克短名单【书影页】
10  2022 诺贝尔文学奖 — 获奖理由全句 EN+中译、第 16 位法国得主·首位法国女性
11  写作与影像 — Happening 金狮（2021）、The Super 8 Years（与子 David 合导）
12  平写的照片（引文页）— 写作观：写作如刀、社会学的文学近亲
13  荣誉与认可 — Renaudot 1984 · Duras/Mauriac 2008 · Formentor 2019 · RSL 2021
14  遗产：个人记忆即集体记忆
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`
- 头部宏可整体复用最近文学 deck 骨架；品牌口径统一 `OpenMathAI`，引号用半角 `" "`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `latexmk -c && make pdf`，用 `pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标；溢出标准 vbox≤10pt / hbox≤50pt

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Ernaux 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 离婚年份 | infobox 作 div. 1980、正文作 divorced in 1981——两说并存，立传回避精确年份（写"1980 年代初离异"）或加注 |
| 首位口径 | "第 16 位法国作家、**首位法国女性**文学奖得主"（page.md 明载），勿写"首位法国女性诺奖得主"（居里是物理/化学奖） |
| 代表作品 | 公认 magnum opus 是 *Les Années*（2008），勿误作 *La Place* |
| 勒诺多奖 | 1984 年凭 *La Place* 获 Renaudot，勿系于其他作品 |
| 政治内容 | 黄马甲/BDS 联署等政治活动系 page.md 明载但政治敏感，立传中**禁写**，不作政治评价 |
| 引语红线 | 中文引号内不写"原话"，除非 page.md 有原文；Macron 贺语为英文转述可用 |
| 无载禁写 | 无文学师承记载（影响者禁编造）；未具名亲属禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| écriture plate | 平写（扁平写作） | 勿译"平淡写作"，指中性客观的文体 |
| autobiographical narrative | 自传性叙事 | La Place 定位 |
| Prix Renaudot | 勒诺多奖 | 1984 |
| Les Années / The Years | 《悠悠岁月》 | 通行中译名 |
| International Booker Prize | 国际布克奖 | 2019 短名单非获奖 |
| Cergy-Pontoise | 塞尔吉-蓬图瓦兹 | 巴黎郊区新镇，定居地 |
| CNED | 法国国家远程教育中心 | 任职 23 年 |
| Strega European Prize | 斯特雷加欧洲奖 | 2016 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（批次预分配）
- **匹配理由**：
  - "时间之流"直接对应代表作《Les Années》（岁月）——以"elle"写 1940 年代至今的法国社会变迁，是时间本身的作品
  - 纪录片气质匹配自传书写的"记忆考古"叙事，克制、绵长、不煽情，呼应获奖理由中的 clinical acuity
  - 与批次内其他曲目（Expedition/Daylight/Savage/Tragedy）不重复
- **本地路径**：`music_audio/alex-productions/` The Flow of Time 曲目 wav → `presentations/21st_century/Annie_Ernaux/The_Flow_of_Time.wav`
- **时长**：> 16 页 × 7 秒 ≈ 112 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Annie_Ernaux/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_21st_century_list.py` | 官方获奖理由 EN+中译（CITATION_ZH，禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Annie_Ernaux.yaml` | 入库 yaml（字段母本 = `MySQL/data/Kenneth_G_Wilson.yaml`） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## 六、执行清单（一次性核对） 【模板通用】

- [ ] 肖像已下载并验证（500px，`file` 确认 JPEG/PNG，非 HTML）
- [ ] Makefile：`MAIN=Annie_Ernaux_zh`、`VIDEO_NAME=Annie_Ernaux_zh`
- [ ] BGM The Flow of Time wav 已复制到本目录
- [ ] 编译 0 error、vbox≤10pt、hbox≤50pt
- [ ] `pdftoppm` 逐页目检（页数与第 6 步规划一致，勿合并帧）
- [ ] 提示词与 yaml 的领域表/关系表逐行一致（含两位子 parent-child 方向语义核对）
- [ ] 获奖理由 EN+中译与 `generate_21st_century_list.py` CITATION_ZH 逐字一致
- [ ] 政治活动内容（BDS/黄马甲等）零出现
- [ ] make images + make video 产出 mp4
- [ ] Review-1 修正写回本提示词 §5 对应陷阱行
