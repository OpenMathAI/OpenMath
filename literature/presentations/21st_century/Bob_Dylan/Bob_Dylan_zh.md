# 文学家立传提示词（Bob Dylan · 2016 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Kenneth G. Wilson 模板骨架为母本、按文学家侧适配。
> 标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Bob Dylan（鲍勃·迪伦），2016 诺贝尔文学奖得主，史上首位获文学奖的音乐人。
- **设计哲学**：文学家立传继承物理学家模板的「身份信息页 + 研究领域结构化」骨架；**文学家无公式框——用名句引文框 / 意象图式替代**。Dylan 的核心张力是「歌曲即文学」：诗意表达生长于美国歌曲传统之中。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Bob Dylan（本名 Robert Allen Zimmerman，1941-05-24 生于明尼苏达州德卢斯，在世）
- **气质关键词**：**美国歌曲传统的诗人、一代人的良知之声、永不停歇的巡演者** —— 2016 诺贝尔文学奖获奖理由：
  > "for having created new poetic expressions within the great American song tradition"（表彰其在伟大的美国歌曲传统中创造了全新的诗意表达）
- **设计母题**：**风中的答案（Blowin' in the Wind）**。答案随风飘散而追问不止——视觉上以公路、口琴、旋转的黑胶纹路与风的流线呼应「行走中的诗人」。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/Bob_Dylan/page.md`（含 frontmatter + infobox + 正文，事实基准已完成核对）
- **参考模板**：
  - 模板标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已核对】

- 生卒：1941-05-24 生于明尼苏达州德卢斯（St. Mary's Hospital），在世（2026）
- 本名与改名：Robert Allen Zimmerman → 1962-08-09 于 Hibbing 法院合法改名 Robert Dylan；希伯来名 Shabtai Zisl ben Avraham
- 家庭：祖父母为敖德萨（1905 犹太人大屠杀后）与立陶宛犹太移民；父 Abram Zimmerman（家具电器店）、母 Beatrice "Beatty" Stone；6 岁因父患小儿麻痹症迁居 Hibbing
- 教育：Hibbing High School（1959，乐队 Golden Chords）；明尼苏达大学 1959 入学、1960 辍学
- 关键荣誉：Nobel Literature 2016（2016-10-13 公布，诺奖演讲 2017-06-05 发布）；Pulitzer 特别褒扬 2008；Presidential Medal of Freedom 2012；Kennedy Center Honors 1997；Academy Award 最佳原创歌曲 2001（"Things Have Changed"）；10 座格莱美（含 1998 Album of the Year *Time Out of Mind*）；摇滚/词曲作者名人堂；法国荣誉军团勋章 2013
- 核心作品与贡献（4–6 条）：*The Freewheelin' Bob Dylan* 1963；"Blowin' in the Wind" / "The Times They Are a-Changin'"（民权与反战圣歌）；1965 插电三部曲 *Bringing It All Back Home* / *Highway 61 Revisited* / *Blonde on Blonde*；"Like a Rolling Stone"；*Blood on the Tracks* 1975；*Chronicles: Volume One* 2004 回忆录；*Rough and Rowdy Ways* 2020
- 关键时间线（15–20 节点）：1941 德卢斯生 → 1947 迁 Hibbing → 1954 行受戒礼 → 1959 看 Buddy Holly 演出四天后其空难、入明尼苏达大学 → 1960 辍学 → 1961-01 纽约，Greystone 疗养院探望 Guthrie → 1961-09 NYT 乐评人 Robert Shelton 撰文、John Hammond 签入 Columbia → 1962-03 首专 *Bob Dylan* → 1963-05 *The Freewheelin'* → 1963-08 华盛顿大游行与 Baez 同台 → 1964 Newport 初遇 Johnny Cash → 1965-03 插电 → 1965-07 "Like a Rolling Stone" → 1965-11 与 Sara Lownds 结婚 → 1966 摩托车祸隐退七年 → 1967 Basement Tapes / Woodstock → 1975 *Blood on the Tracks* 与 Rolling Thunder Revue → 1979-81 福音时期 → 1988 Never Ending Tour 开始 → 1997 *Time Out of Mind* 格莱美年度专辑 → 2004 *Chronicles* → 2008 Pulitzer 特别褒扬 → 2016 诺奖 → 2020 *Rough and Rowdy Ways*、曲库售予 Universal（逾 3 亿美元）→ 2022 《The Philosophy of Modern Song》
- 关系事实（详见第 4.5 步）：影响者 Guthrie/Johnson/Williams/Seeger；合作者 Baez/Cash/Van Ronk/经纪人 Grossman/星探 Hammond；两任妻子；子 Jesse/Jakob

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | songwriting | 歌曲创作 | 核心身份：词曲一体，"new poetic expressions" | 封面、核心页 |
| 1 | lyricism | 歌词诗学 | 政治社会哲思入词，引经典文学入流行乐 | 歌词页 |
| 2 | american folk music | 美国民谣传统 | Guthrie 衣钵、传统歌谣改编 | 早年页 |
| 3 | folk rock | 民谣摇滚 | 1965 插电转向，改变流行乐边界 | 插电页 |
| 4 | protest song | 抗议歌曲 | 民权与反战运动的圣歌 | 六十年代页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Bob_Dylan.yaml` 完全一致；仅收 page.md 明载关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Woody Guthrie | 单向（影响 Dylan） | 民谣偶像，自认 "Guthrie's greatest disciple"，1961 纽约首访即探望 |
| influence | Robert Johnson | 单向 | 早期创作受其蓝调塑造（Chronicles 自述） |
| influence | Hank Williams | 单向 | 自述受其乡村歌 "architectural forms" 塑造 |
| influence | Pete Seeger | 单向 | 早期抗议歌曲受其对时事歌的热情影响 |
| colleague | Joan Baez | 无向 | 民权运动同台、恋人；将 Dylan 早期歌曲唱红 |
| colleague | Johnny Cash | 无向 | 1964来信力挺 "Shut up! And let him sing!"，Newport 结识成友 |
| colleague | Dave Van Ronk | 无向 | 格林尼治村民谣圈友人，互授曲目 |
| colleague | Albert Grossman | 无向 | 1962-1970 经纪人 |
| colleague | John Hammond | 无向 | Columbia 星探/制作人，1961 签约引路人 |
| spouse | Sara Lownds | 无向 | 1965-11-22 结婚，1977-06-29 离婚，四子女 |
| spouse | Carolyn Dennis | 无向 | 1986 结婚 1992 离婚，女 Desiree |
| parent-child | Jesse Dylan | 父→子 | 1966-01-06 生，导演 |
| parent-child | Jakob Dylan | 父→子 | 1969-12-09 生，The Wallflowers 主唱 |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：公路尘土、民谣木质、时代风声
- **配色**：主色深松绿 `#1B4D3E`（分批文件预分配）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeFolk` 美国民谣 — 大地棕 `#8A6D3B`
  - `badgeLyric` 歌词诗学 — 香槟金 `#C9A227`
  - `badgeElectric` 民谣摇滚 — 电光橙 `#D96C2C`
  - `badgeProtest` 抗议歌曲 — 铁灰蓝 `#4A6274`
- **背景母题**：风的流线与稀疏公路圆点，呼应 "Blowin' in the Wind"（与设计母题一致）

### 第 6 步：规划幻灯片序列 【人物专属，可微调，10–16 页】

```
00  OpenLiterature 项目首页（\input cover/ 共享首页）
01  封面 — 美国歌曲传统的诗人 / Bob Dylan 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名/改名、国籍、出生地、家庭、
    荣誉、核心领域）
03  核心贡献概览 — 歌曲创作 / 歌词诗学 / 民谣传统 / 插电转向
04  早年：德卢斯与 Hibbing (1941–1959) — 犹太移民家庭、Buddy Holly 之夜、Golden Chords
05  纽约：Guthrie 的门徒 (1961–1962) — Gerde's Folk City、Shelton 乐评、Hammond 签约
06  圣歌年代 (1963–1964) — Freewheelin'、华盛顿大游行、Baez、Times They Are a-Changin'
07  插电惊雷 (1965–1966) — 三部曲、Like a Rolling Stone、Newport 1965【名句引文框页】
08  隐退与变形 (1966–1974) — 车祸、Basement Tapes、乡村三部曲
09  血染轨迹与 Rolling Thunder (1975–1978) — Blood on the Tracks【意象图式页】
10  福音、低谷与再起 (1979–1997) — Never Ending Tour、Time Out of Mind
11  文学的正名 (1996–2016) — Gordon Ball 二十年提名、Pulitzer 2008、2016-10-13 宣布
    【诺奖引文框：citation EN 原文 + 中译】
12  诺奖演讲与争议 — 首位音乐人得奖、演讲与 Moby-Dick 引用、Song tradition 之辩
13  永不落幕 — Rough and Rowdy Ways、曲库交易、The Philosophy of Modern Song
14  遗产：从吟游诗人到文学奖 — Engdahl "希腊吟游诗人旁的位置"
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 音乐人获文学奖口径 | 2016 奖官方理由 "for having created new poetic expressions within the great American song tradition"，须整句照引，勿改写为"因其歌词获诺奖" |
| 首位口径 | "第一位获文学奖的音乐人"（NYT: the first musician to win the award），勿扩大为"第一位非作家" |
| 生地 | 生于 Duluth（St. Mary's Hospital），童年主要在 Hibbing，两城勿混 |
| 改名 | 1962-08-09 合法改名 Robert Dylan；此前艺名 Elston Gunnn/Blind Boy Grunt 等，举一两例即可 |
| 得奖反应 | 获奖后数日沉默，后对 Edna Gundersen 称 "amazing, incredible"；勿编造获奖感言 |
| 诺奖演讲争议 | Pitzer 指其 Moby-Dick 段落疑似取自 SparkNotes——只作客观注记，不定性 |
| 引语红线 | 正文引语仅限 page.md 载英文原文者（如 Guthrie "greatest disciple"、Cash 信、Maslin/Oates 评论），中译注记 |
| 配偶与子女 | Sara Lownds 四子女（Jesse/Anna/Samuel/Jakob）+ 收养 Maria；Carolyn Dennis 之女 Desiree；婚姻曾保密至 2001 Sounes 传记 |
| 宗教叙述 | 犹太 upbringing → 1979 福音时期 → 后自述"歌即我的宗教"，只按 page.md 客观简述，不评价 |
| 无载禁写 | 不写 Bob Johnston 制作细节、不写具体巡演城市全表、不写与 Beatles 会面细节（page.md 未载者一律不写） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| singer-songwriter | 创作歌手 | 非"歌手"泛称，强调词曲一体 |
| folk revival | 民谣复兴 | 五六十年代美国背景 |
| protest song | 抗议歌曲 | 与 topical song（时事歌）近义 |
| going electric | 插电转向 | 1965 Newport 争议，"Electric Dylan controversy" |
| Never Ending Tour | 永不落幕巡演 | 1988-06-07 起，年均约百场 |
| Bootleg Series | 私录系列 | 官方盗辑档案系列，非盗版 |
| Great American Songbook | 美国经典歌曲集 | 与 "great American song tradition"（诺奖语）不同，勿混 |
| Nobel lecture | 诺奖演讲 | 2017-06-05 发布 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions（分批文件预分配）
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**: "Timeless（超越时代）" 正合 Dylan —— 从 1962 首专到 2020 *Rough and Rowdy Ways* 六十年常青，诺奖把流行歌词纳入文学正典即是"超越时代"的裁决；"纪录片"匹配传记叙事（德卢斯 → 纽约 → 插电 → 诺奖）。
- **备选**（未采用）: New Lands（开拓感，但本批次已用于他人）；The Flow of Time（时间感，节奏偏柔）
- **本地路径**: `music_audio/` 对照 `curated_tracks.md` 取 Timeless 曲目文件 → 复制到 `presentations/21st_century/Bob_Dylan/Timeless.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Bob_Dylan/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_21st_century_list.py` → `CITATION_ZH` | 获奖理由中译（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 模板结构母本 |
| `MySQL/data/Bob_Dylan.yaml` | 社会关系/领域入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库对照 |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
