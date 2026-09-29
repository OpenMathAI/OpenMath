# 文学家立传提示词（OpenLiterature · 21 世纪 · Han Kang）

> **本文件是 OpenLiterature 21 世纪批次的人物专属立传提示词**，目标人物：Han Kang（2024 年诺贝尔文学奖得主，韩国作家）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）；文学家适配：无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各人物侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Han Kang（한강/韓江，韩江），2024 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传以**作品意象与语言质地**为骨架——本篇以「白与光·线与伤」为视觉母题，强调「身份信息页」（Identity 速览页）与「文学领域表」的结构化表达，务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Han Kang（1970-11-27 生于韩国光州，在世）
- **气质关键词**：**直面历史创伤的诗性书写者、人类生命脆弱性的记录者、首位亚洲女性文学奖得主** —— 2024 年诺贝尔文学奖获奖理由：
  > "for her intense poetic prose that confronts historical traumas and exposes the fragility of human life"（表彰其浓烈的诗性散文直面历史创伤，暴露出人类生命的脆弱）
- **设计母题**：**白与线（white / light and thread）**。《白》的白色冥想、诺奖演讲《Light and Thread》（光与线）、白布仪式；视觉语言取「大面留白 / 细线贯穿 / 烛焰」，呼应"光与线"。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Han_Kang/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：`https://en.wikipedia.org/wiki/Han_Kang`
- **肖像**：第 0 步待下载（Commons `Han_Kang_-_2017.png`，见 images.txt）。
- **参考模板**：
  - 数学家/物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`literature/presentations/cover/`（OpenLiterature 共享封面）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），使用 `MySQL/seed_person.py data/Han_Kang.yaml` 幂等入库。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `page.md`（事实基准如下，第一轮已核对）
- ✅ 待下载头像到 `images/`（Commons 250px 改 500px，curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证）
- **事实基准（以正文为准）**：
  - 生卒：1970-11-27 生于光州，在世；早期小说用笔名 Han Kang-hyun
  - 名字典故：据其父所述，名字取自"汉江"（한강）之音——page.md 明载
  - 家庭：文学世家——父韩胜源（Han Seung-won，小说家）；兄 Han Dong-rim（小说家）；弟 Han Kang-in（小说家兼漫画家）；前夫 Hong Yong-hee（文学批评家、庆熙网大教授，多年已离异）；一子（2018–2024-11 与韩共同经营首尔书店）
  - 教育：Poongmoon 女子高中（1988 毕业，曾任班长）→ 延世大学韩国语言文学（1993 BA）→ 1998 爱荷华大学国际写作计划 3 个月（韩国艺术委员会资助）
  - 任职：2007–2018 首尔艺术大学创作系教授
  - 关键荣誉：Nobel 2024（**首位韩国作家、首位亚洲女性文学奖得主**）；International Booker 2016（*The Vegetarian*，韩语小说首获，与译者 Deborah Smith 共同获奖）；Yi Sang 文学奖 2005；Prix Médicis étranger 2023；Malaparte 2017；Ho-Am 艺术奖 2024；Future Library 2018 第五位受邀作家（2019-05 交付 *Dear Son, My Beloved*，白布仪式）；RSL International Writer 2023
  - 核心作品（4–6 条）：《여수의 사랑》（1995 短篇集）、《채식주의자》（The Vegetarian，2007 单行本）、《소년이 온다》（Human Acts，2014）、《희랍어 시간》（Greek Lessons，2011）、《흰》（The White Book，2016）、《작별하지 않는다》（We Do Not Part，2021）
  - 关键时间线（17 节点）：1970 生于光州 → 9 岁随家迁首尔（光州事件前 4 个月）→ 12 岁读到 Hinzpeter 秘密流通的纪念影集（深刻影响其人性观与创作）→ 1988 Poongmoon 高中毕业 → 1993 延世大学韩语韩文学毕业、《文学与社会》冬季号发表 5 首诗（含"首尔之冬"）→ 1994 以笔名 Han Kang-hyun 凭《红色锚》获首尔新闻新春文艺奖 → 1995 首部短篇集《丽水之爱》→ 1998 爱荷华写作计划 → 1999《Baby Buddha》获韩国小说奖 → 2000 文化部今日青年艺术家奖 → **2005《蒙古斑》获李箱文学奖** → 2007《素食者》单行本出版/任教首尔艺大 → 2014《소년이 온다》→ **2016 国际布克奖**（与 Deborah Smith）→ 2016《흰》→ 2018 Future Library 受邀 → 2021《작별하지 않는다》→ 2023 Médicis 外国文学奖 → **2024-10 获诺贝尔文学奖**、12-07 诺奖演讲《Light and Thread》→ 2025《Light and Thread》韩文版出版

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `literature/presentations/21st_century/` 下建 `Han_Kang/` 与 `images/`
- 复制同项目 21 世纪已有 deck 的 Makefile，设 `MAIN=Han_Kang_zh`、`VIDEO_NAME=Han_Kang_zh`
- 复制 BGM：Savage 曲目 wav → 本目录

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Han Kang 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | contemporary korean literature | 韩国当代文学 | 首位韩国文学奖得主 | 诺奖页、贡献页 |
| 1 | poetic prose | 诗性散文 | 获奖理由核心词 intense poetic prose | 风格页 |
| 2 | historical trauma | 历史创伤 | 光州事件（Human Acts）/济州四三（We Do Not Part） | 主题页 |
| 3 | violence and the body | 暴力与身体 | The Vegetarian 的拒食与人身暴力 | 主题页 |
| 4 | korean poetry | 韩国诗歌 | 1993 以诗出道、2013 诗集《把晚餐放进抽屉》 | 早年页 |

#### 4.1 入库操作

- 由 `MySQL/data/Han_Kang.yaml` 经 `MySQL/seed_person.py` 写入：people 主记录（qid=Q5646626、primary_occupation=writer、has_social_data=1、has_biography=0 待 Beamer 后置 1）+ 5 条 `person_field`
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；无载禁写。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Han Seung-won | 无向 | 父亲，小说家（韩胜源） |
| spouse | Hong Yong-hee | 无向 | 前夫，文学批评家、庆熙网大教授，多年已离异 |
| influence | Yi Sang | 单向（对方影响 Han Kang） | 李箱；大学时代痴迷其诗句"人应当是植物"，由此写出《素食者》 |

- **不入库说明**：兄 Han Dong-rim / 弟 Han Kang-in 系 page.md 明载的作家家人，但 relation_type 白名单无 sibling 类型（parent-child 语义不符）——禁建关系，仅在立传正文叙述"文学世家"；Deborah Smith（译者，2016 国际布克共同获奖）按惯例不入库；Katie Paterson（Future Library 组织者）系项目关系。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：纸墨深褐 `#4E342E`（本批次预分配）
- **辅色**：诺奖香槟金 `#C9A227` + 素白 `#F2F0EB`（《白》母题）
- **badgeA–D 四分类色**：
  - `badgeA` 韩国当代文学 — 纸墨褐 `#4E342E`
  - `badgeB` 诗性散文 — 香槟金 `#C9A227`
  - `badgeC` 历史创伤 — 深红 `#8B1A1A`
  - `badgeD` 暴力与身体 — 冷灰 `#37474F`
- **背景母题**：素白底 + 细金线贯穿（"光与线"）+ 烛焰点，呼应《白》与诺奖演讲

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 直面历史创伤的诗性书写 / Han Kang 1970– + 四色 badge + 右上头像 + 国籍行（韩国）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 韩国当代文学 / 诗性散文 / 历史创伤 / 暴力与身体 / 韩国诗歌
04  早年：光州与首尔 (1970–1993) — 光州出生、9 岁迁首尔、12 岁读 Hinzpeter 影集、延世韩语韩文学
05  以诗登场 (1993–1995) — "首尔之冬"等 5 首诗、红色锚获奖、《丽水之爱》
06  李箱文学奖与《素食者》(2000–2007) — Yi Sang 一句"人应当是植物"的灵感链【意象图式页】
07  《少年来了》(Human Acts, 2014) — 历史创伤书写（光州事件只客观简述）【引文框页】
08  国际突破：2016 国际布克奖 — 与译者 Deborah Smith 共同获奖、韩语小说首获
09  《白》与《希腊语课》(2016–2023) — 白色冥想、夭折姐姐的自传性小说【书影页】
10  《不作告别》(We Do Not Part, 2021) — 济州四三、Médicis 外国文学奖
11  2024 诺贝尔文学奖 — 获奖理由全句 EN+中译、首位韩国作家·首位亚洲女性得主
12  光与线（引文页）— 诺奖演讲《Light and Thread》(2024-12-07)、白布仪式与 Future Library
13  荣誉与认可 — Yi Sang 2005 · 国际布克 2016 · Médicis 2023 · Ho-Am 2024
14  遗产：韩国文学的世界时刻
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`
- 头部宏可整体复用最近文学 deck 骨架；品牌口径统一 `OpenMathAI`，引号用半角 `" "`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `latexmk -c && make pdf`，用 `pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标；溢出标准 vbox≤10pt / hbox≤50pt

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Han Kang 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 光州事件 | 只客观简述（1970 生于光州、9 岁迁离、12 岁读影集、Human Acts 题材），**不展开政治叙事、不作评价**；2025 年弹劾联署等政治内容禁写 |
| 首位口径 | "首位韩国作家、首位亚洲女性文学奖得主"（page.md 明载），两口径勿混、勿写"首位亚洲作家" |
| 国际布克 | 2016 年与译者 Deborah Smith **共同获奖**；是韩语小说首次获奖，勿写"韩江个人独得" |
| 素食者年份 | 单行本 2007（Changbi）；三部结构：素食者/蒙古斑/树火；蒙古斑 2005 获李箱奖、其余两部分曾因合约问题延后 |
| 笔名 | 早期小说以笔名 Han Kang-hyun 发表（1994），勿与 Han Kang 混作两人 |
| 兄弟 | 兄妹三人均作家（父韩胜源），正文可述"文学世家"，但**禁建数据库关系**（无 sibling 类型） |
| 引语红线 | 诺奖反应"surprised but honoured"系转述；白布仪式引语与"keeping her humble"为英文原文可引 |
| 无载禁写 | 无大学导师/文学师承记载（除 Yi Sang 明载灵感链）；儿子未具名禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Vegetarian | 《素食者》 | 通行中译名 |
| Human Acts | 《少年来了》 | 通行中译名 |
| The White Book | 《白》 | 通行中译名 |
| We Do Not Part | 《不作告别》 | 通行中译名 |
| Yi Sang Literary Award | 李箱文学奖 | 2005，《蒙古斑》 |
| International Booker Prize | 国际布克奖 | 2016，与译者共同获奖 |
| Prix Médicis étranger | 美第奇外国小说奖 | 2023 |
| Future Library | 未来图书馆 | 2018 受邀、2019 交付手稿 |
| Light and Thread | 光与线 | 诺奖演讲题（2024-12-07） |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（批次预分配）
- **匹配理由**：
  - "Savage"（凛冽/原始）匹配获奖理由中的 intense（浓烈）——韩江直面暴力、创伤与身体脆弱性的书写力度
  - 张力与留白并存的气质匹配《素食者》《少年来了》的冷峻诗性，克制之下蕴含强烈情感冲击
  - 与批次内其他曲目（Expedition/The Flow of Time/Daylight/Tragedy）不重复
- **本地路径**：`music_audio/alex-productions/` Savage 曲目 wav → `presentations/21st_century/Han_Kang/Savage.wav`
- **时长**：> 16 页 × 7 秒 ≈ 112 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Han_Kang/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_21st_century_list.py` | 官方获奖理由 EN+中译（CITATION_ZH，禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Han_Kang.yaml` | 入库 yaml（字段母本 = `MySQL/data/Kenneth_G_Wilson.yaml`） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## 六、执行清单（一次性核对） 【模板通用】

- [ ] 肖像已下载并验证（500px，`file` 确认 JPEG/PNG，非 HTML）
- [ ] Makefile：`MAIN=Han_Kang_zh`、`VIDEO_NAME=Han_Kang_zh`
- [ ] BGM Savage wav 已复制到本目录
- [ ] 编译 0 error、vbox≤10pt、hbox≤50pt
- [ ] `pdftoppm` 逐页目检（页数与第 6 步规划一致，勿合并帧）
- [ ] 提示词与 yaml 的领域表/关系表逐行一致
- [ ] 获奖理由 EN+中译与 `generate_21st_century_list.py` CITATION_ZH 逐字一致
- [ ] 光州事件仅客观简述、2025 弹劾联署零出现
- [ ] make images + make video 产出 mp4
- [ ] Review-1 修正写回本提示词 §5 对应陷阱行
