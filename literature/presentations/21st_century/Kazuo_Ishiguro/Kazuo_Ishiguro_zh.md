# 文学家立传提示词（Kazuo Ishiguro · 2017 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Kenneth G. Wilson 模板骨架为母本、按文学家侧适配。
> 标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Kazuo Ishiguro（石黑一雄），2017 诺贝尔文学奖得主，日裔英国小说家。
- **设计哲学**：文学家立传保留「身份信息页 + 领域结构化」骨架；**无公式框——用名句引文框 / 意象图式替代**。Ishiguro 的核心母题是「被欺骗的记忆」：克制的第一人称叙述者面对自身幻觉。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Sir Kazuo Ishiguro 石黒 一雄（1954-11-08 生于日本长崎，在世）
- **气质关键词**：**情感巨力小说的织造者、幻象联结之渊的勘探者、文体杂糅的冒险家** —— 2017 诺贝尔文学奖获奖理由：
  > "who, in novels of great emotional force, has uncovered the abyss beneath our illusory sense of connection with the world"（表彰其以巨大情感力量的小说，揭示了我们与世界虚幻联结感之下的深渊）
- **设计母题**：**黄昏中的长日留痕**。残烛宅邸、雾中花园与漂浮世界——克制的留白画面呼应其"深渊藏在体面之下"的美学。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/Kazuo_Ishiguro/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`；首页模板 `literature/presentations/cover/`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已核对】

- 生卒：1954-11-08 生于长崎；在世（2026）
- 国籍：日本（至 1983）→ 英国（1983 入籍）；五岁随父赴英
- 家庭：父 Shizuo Ishiguro（海洋物理学家，1960 受邀赴英国国家海洋学研究所）；妻 Lorna MacDougall（1986 结婚，相识于诺丁山无家可归者慈善机构 West London Cyreneans）；女 Naomi Ishiguro（作家，著有 *Escape Routes*）
- 教育：Woking County Grammar School → Kent 大学英语与哲学 BA（1974–1978）→ East Anglia 大学创意写作课程 MA 1980（师从 Malcolm Bradbury 与 Angela Carter），论文成为处女作
- 关键荣誉：Nobel 2017；Booker 1989（*The Remains of the Day*，另三次入围）；Whitbread 1986；Winifred Holtby 1982；OBE 1995；Knight Bachelor 2018；Companion of Honour 2024；旭日重光章 2018；Bodley Medal 2019；2023 以《Living》编剧获奥斯卡最佳改编剧本提名（史上第 6 位获奥斯卡提名的诺奖得主，唯 Shaw 与 Dylan 二人真正获奖）
- 核心作品（4–6 条）：*A Pale View of Hills* 1982；*An Artist of the Floating World* 1986；*The Remains of the Day* 1989；*The Unconsoled* 1995；*Never Let Me Go* 2005（Time 年度最佳小说）；*Klara and the Sun* 2021
- 关键时间线（15–20 节点）：1954 长崎生 → 1960 随父迁 Guildford → 1973 gap year 赴美加写歌投样带、Balmoral grouse beater → 1974 入 Kent → 1978 毕业 → 1979 入 UEA → 1980 MA → 1982 处女作出版并获 Winifred Holtby → 1983 入籍英国、Granta 最佳青年小说家 → 1986 *Floating World* 获 Whitbread → 1989 *Remains* 获 Booker、29 年后首访日本 → 1993 电影版（Hopkins/Thompson）→ 1995 *The Unconsoled*、OBE → 2000 *When We Were Orphans* 入围 Booker → 2005 *Never Let Me Go* → 2007 为 Stacey Kent 写词 *Breakfast on the Morning Tram* → 2017-10 诺奖 → 2018 封爵 → 2021 *Klara and the Sun* → 2022 *Living* → 2023 奥斯卡提名 → 2024 Companion of Honour
- 关系事实：详见第 4.5 步（导师 2、影响 6、合作 2、家庭 3）

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | psychological fiction | 心理小说 | 不可靠叙述者与自我欺骗 | 核心页 |
| 1 | historical fiction | 历史小说 | 战前战后价值受检验的时代 | 长日留痕页 |
| 2 | science fiction | 科幻元素 | Never Let Me Go / Klara and the Sun | 克拉拉页 |
| 3 | first-person narrative | 第一人称叙述 | 歌者般的私密语气（自述源自写歌） | 叙述页 |
| 4 | song lyrics | 歌词创作 | 与 Stacey Kent 合作、小说与歌的互通 | 音乐页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Kazuo_Ishiguro.yaml` 完全一致；仅收 page.md 明载关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Malcolm Bradbury | 师→生 | UEA 创意写作课程导师，MA 1980 |
| advisor-student | Angela Carter | 师→生 | UEA 创意写作课程导师 |
| influence | Fyodor Dostoyevsky | 单向 | 自列影响者（曾居最推崇小说家之首） |
| influence | Marcel Proust | 单向 | 自列影响者 |
| influence | Jun'ichirō Tanizaki | 单向 | 最常引用的日本作家 |
| influence | Yasujirō Ozu | 单向 | 自述日本电影（尤其小津）影响更著 |
| influence | Mikio Naruse | 单向 | 同上，成瀨巳喜男 |
| influence | Bob Dylan | 单向 | 自称 "great admirer of Bob Dylan"，少年习歌源头 |
| colleague | Stacey Kent | 无向 | 为其多张专辑填词，2024 歌词集成书 |
| colleague | Jim Tomlinson | 无向 | 与 Kent 夫妇共同写歌 |
| spouse | Lorna MacDougall | 无向 | 1986 结婚，社会工作者 |
| parent-child | Naomi Ishiguro | 父→女 | 作家 |
| parent-child | Shizuo Ishiguro | 父→子 | 海洋物理学家，1960 携家赴英 |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：克制、雾蓝、旧宅暖光
- **配色**：主色石板蓝灰 `#37474F`（分批文件预分配）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgePsy` 心理小说 — 雾蓝 `#5B7C99`
  - `badgeHist` 历史小说 — 旧金 `#C9A227`
  - `badgeSci` 科幻元素 — 冷青 `#3E8E8C`
  - `badgeSong` 歌词创作 — 暖赭 `#B0673B`
- **背景母题**：黄昏窗格与雾中光晕（长日留痕 + 克拉拉的太阳），呼应"幻象联结之下的深渊"

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/ 共享首页）
01  封面 — 幻象之渊的勘探者 / Kazuo Ishiguro 1954– + 四色 badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍变迁、家庭、教育、荣誉、领域）
03  核心贡献概览 — 心理小说 / 历史小说 / 科幻元素 / 第一人称叙述
04  长崎与吉尔福德 (1954–1973) — 想象中的日本、合唱与学歌
05  写歌未遂与 UEA (1973–1980) — 样带、 grouse beater、Bradbury/Carter 门下
06  漂浮世界 (1982–1989) — 两部日本题材 + 长日留痕获 Booker
07  冒险的文体 (1995–2005) — The Unconsoled / Never Let Me Go【引文框：Danius 颁奖词】
08  诺奖时刻 (2017) — citation EN 原文 + 中译；Rushdie 贺词；获奖答辞【引文框页】
09  深渊之下的技法 — 不可靠叙述者 / 克制的留白（意象图式页）
10  小说与歌的互通 — Stacey Kent 合作词、The Summer We Crossed Europe in the Rain
11  克拉拉与太阳 (2021) — AI 与人性的追问；Living 与奥斯卡提名
12  影响与自辩 — Dostoyevsky/Proust/Tanizaki/Ozu；拒绝类比 Austen/James
13  荣誉与认可 — Booker 1989 · 封爵 2018 · Companion of Honour 2024
14  遗产：英国文学的移民之眼
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方句以 "who, in novels of great emotional force..." 开头，整句照引勿截断 |
| 国籍 | 日本生、1960 赴英、1983 入籍英国；frontmatter 双籍（UK+Japan）按"日本（至1983）/英国（1983起）"呈现，勿只写英国 |
| 日文 setting | 前两部小说的日本是"想象中的日本"（对 Ōe 自述），勿写成实地风物 |
| 影响排序 | 自述日本**电影**（小津/成瀨）影响大于日本文学；Tanizaki 是最常引用的日本作家——三者口径勿混 |
| Rushdie 关系 | Rushdie 是赞美者/老友（"my old friend Ish"），非师承非合作，勿建关系行 |
| Charlotte Brontë | "I owe my career... to Jane Eyre and Villette" 是其自述，但属"推崇"叙述，领域表与关系表均勿拔高为 influence 入库（保持与 yaml 一致：不入） |
| 奥斯卡口径 | 2023 以 *Living* 获**提名**（第 6 位获提名的诺奖得主；Shaw 与 Dylan 唯二真获奖），勿写成"获奥斯卡奖" |
| *The Buried Giant* | 2015；唯一例外口径：除处女作与它外均第一人称/均入围重要奖 |
| 无载禁写 | 不写大学具体老师以外的师承、不写未具名子女、不编造对 Trump/AI 评论为"立场宣言"（只客观一句） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| unreliable narrator | 不可靠叙述者 | 与第一人称叙述相伴 |
| floating world | 漂浮世界 | 书名双关浮世绘传统 |
| butler | 管家 | Remains 主角 Stevens，译"管家"非"男仆" |
| artificial friend | 人工朋友 | Klara 术语，照引 |
| creative writing course | 创意写作课程 | UEA 课程，师承出处 |
| Companion of Honour | 功绩勋章同伴 | 2024，与 Knight Bachelor 2018 区分 |
| Nobel lecture | 诺奖演讲 | — |
| Desert Island Discs | 沙漠岛唱片 | 2002 选 Dylan 歌，与 Dylan 影响行呼应 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（分批文件预分配）
- **风格**: 历史感 / 深沉
- **匹配理由**: Ishiguro 的小说几乎全部回望——战前战后、克隆人的过去式、旧管家的一生；"历史感/深沉"贴合其挽歌气质与长日留痕的黄昏色调。
- **备选**（未采用）: Timeless（本批 Dylan 已用）；The Flow of Time（与文学侧 Time 母题近，但节奏偏亮）
- **本地路径**: 对照 `music_audio/curated_tracks.md` 取 PAST → `presentations/21st_century/Kazuo_Ishiguro/PAST.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Kazuo_Ishiguro/page.md` | 本地 Wikipedia 正文 |
| `literature/generate_21st_century_list.py` → `CITATION_ZH` | 获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 模板结构母本 |
| `MySQL/data/Kazuo_Ishiguro.yaml` | 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
