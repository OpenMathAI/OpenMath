# 文学家立传提示词（OpenLiterature 批次实例：Frans Eemil Sillanpää）

> 本文件是 OpenLiterature 的「文学家立传提示词」，以 Frans Eemil Sillanpää（1939 诺贝尔文学奖，《少女西丽亚》）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框，以代表作书影/名句引文框/意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，结尾页品牌统一 `OpenMathAI`）。
- **本实例**：Frans Eemil Sillanpää（弗兰斯·埃米尔·西兰帕，1888–1964），1939 诺贝尔文学奖得主，**芬兰首位文学奖得主**。
- **设计哲学**：文学家立传以「代表作意象 + 文学领域结构化表达 + 身份信息页」为骨架；Sillanpää 的核心视觉语言是**田野与夏夜（fields and the summer night）**——农民与土地、人与自然的合一。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Frans Eemil Sillanpää（1888-09-16 ~ 1964-06-03，享年 75 岁）
- **气质关键词**：**农民之子的凝视者、自然的画师、反暴力的乐观主义者**
- **官方获奖理由（1939）**：
  > EN: "for his deep understanding of his country's peasantry and the exquisite art with which he has portrayed their way of life and their relationship with Nature"
  > 中译：表彰其对本国农民的深刻理解，以及描绘他们的生活方式及其与自然之关系的精湛艺术
  > （来源：`literature/generate_20th_century_list.py` CITATION_ZH[("1939","Frans Eemil Sillanpää")] + `literature/nobel_literature_citations.json`，禁止改写）
- **设计母题**：**田野与夏夜**——农田地平线、夏夜湖光、麦浪色块；呼应获奖理由中「与自然之关系」及代表作 *Ihmiset suviyössä*（夏夜的人们）。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Frans_Eemil_Sillanpää/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL: https://en.wikipedia.org/wiki/Frans_Eemil_Sillanpää
  - 肖像（第 0 步下载）：`images/` 下待下载（page.md 内嵌 1931 年 Mauno Oittinen 雕像坐像照等，404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md）

- **生卒**：1888-09-16 生于 Hämeenkyrö（时属芬兰大公国）~ 1964-06-03 卒于赫尔辛基，享年 75 岁。
- **国籍**：芬兰（frontmatter 兼载 Grand Duchy of Finland，出生时为俄国治下大公国；主条目按 Finland）。
- **出身**：Hämeenkyrö 农家，父母贫苦仍设法送其入学（Jumesniemi Church School、Haukijärvi School、Tampere Lyceum）。
- **教育**：1908 年得恩主 **Henrik Liljeroos** 资助入赫尔辛基大学**学医**（未完成，后弃医从文）；大学时期结识画家 Eero Järnefelt、Pekka Halonen，作曲家 Jean Sibelius 与作家 Juhani Aho。
- **家庭**：1914 年结识 Sigrid Maria Salomäki，1916 年结婚；1939 年妻子死于肺炎，留下 8 个孩子；其后与秘书 Anna von Hertzen（1900–1983）结婚，1941 年离婚。
- **文学立场**：原则上反对一切形式的暴力，相信科学的乐观主义；笔下乡村人「与土地合一地生活」。
- **核心作品与贡献（4–6 条）**：
  1. *Hurskas kurjuus*（Meek Heritage《神圣的贫困》，1919）——剖析芬兰内战成因，因客观立场在当时引发争议。
  2. *Nuorena nukkunut*（The Maid Silja《少女西丽亚》，1931）——为其赢得国际声誉（代表作，infobox Notable work）。
  3. *Ihmiset suviyössä*（People in the Summer Night《夏夜的人们》，1934）。
  4. 早期农村叙事：*Elämä ja aurinko*（1916）、*Hiltu ja Ragnar*（1923）、*Maan tasalta*（1924）、*Töllinmäki*（1925）、*Rippi*（1928）等。
  5. 晚期作品：*Elokuu*（1941）、*Ihmiselon ihanuus ja kurjuus*（1945）。
  6. 战时歌词 *Sillanpään marssilaulu*（长子 Esko 在卡累利阿地峡服役时作，以振士气）。
- **关键荣誉**：Nobel 1939（芬兰首位）；Aleksis Kivi Award；芬兰狮子勋章一级指挥官；小行星 **1446 Sillanpää**（1938-01-26 由 Yrjö Väisälä 发现，以其命名）。
- **1939 年的戏剧性**：获奖数日后芬苏谈判破裂、冬季战争爆发；他赴斯德哥尔摩领奖后**将金奖章捐出熔金充作战争救济**。
- **晚年**：1941 离婚，酗酒等疾患入院治疗；1943 以「Sillanpää 爷爷」（Grandpa Sillanpää）形象重返公众；1945–1963 每年圣诞夜的电台讲话成为传统，听众广泛。
- **关键时间线（17 节点）**：
  1. 1888-09-16 生于 Hämeenkyrö（芬兰大公国）
  2. Jumesniemi Church School / Haukijärvi School 启蒙
  3. Tampere Lyceum 中学（父母贫苦仍供学）
  4. 1908 得 Liljeroos 资助入赫尔辛基大学学医
  5. 大学结识 Järnefelt / Halonen / Sibelius / Juhani Aho
  6. 1913 迁回故乡村庄，专事写作
  7. 1914 为 *Uusi Suometar* 撰稿
  8. 1916 与 Sigrid Maria Salomäki 结婚；首部重要作品 *Elämä ja aurinko*
  9. 1919 *Hurskas kurjuus*（内战题材，客观立场引争议）
  10. 1923–1928 农村叙事多产期（Hiltu ja Ragnar / Maan tasalta / Töllinmäki / Rippi）
  11. 1931 *Nuorena nukkunut*（The Maid Silja），国际声誉
  12. 1934 *Ihmiset suviyössä*
  13. 1938-01-26 小行星 1446 Sillanpää 命名（Väisälä 发现）
  14. 1939 诺贝尔文学奖（芬兰首位）；冬季战争爆发，捐奖章熔金助战
  15. 1939 妻子 Sigrid 去世（肺炎），留下 8 个孩子；后再婚，1941 离婚
  16. 1943 以「Sillanpää 爷爷」重返公众；1945–1963 圣诞夜电台讲话传统
  17. 1964-06-03 卒于赫尔辛基，享年 75

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- `literature/presentations/20th_century/Frans_Eemil_Sillanpää/`（含 `images/`）；Makefile 设 `MAIN=Frans_Eemil_Sillanpää_zh`；肖像按 `images.txt` 下载，404 用装饰圆占位。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | rural realism | 乡土现实主义 | 对本国农民生活的深刻理解（获奖理由核心） | 核心页 |
| 1 | nature writing | 自然书写 | 人与自然之关系的精湛描绘 | 自然页 |
| 2 | social novel | 社会小说 | 芬兰内战题材的客观剖析 | 内战页 |
| 3 | poetic prose | 诗性散文体 | 抒情性的叙事文体 | 文体页 |

- 入库：`MySQL/data/Frans_Eemil_Sillanpää.yaml` → `python3 seed_person.py data/Frans_Eemil_Sillanpää.yaml`（primary_occupation: writer）。

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Sigrid Maria Salomäki | 无向 | 1916 结婚，1939 死于肺炎，育 8 子 |
| spouse | Anna von Hertzen | 无向 | 其秘书，丧妻后续弦，1941 离婚 |
| colleague | Eero Järnefelt | 无向 | 赫尔辛基大学时期结识的画家 |
| colleague | Pekka Halonen | 无向 | 赫尔辛基大学时期结识的画家 |
| colleague | Jean Sibelius | 无向 | 赫尔辛基大学时期结识的作曲家 |
| colleague | Juhani Aho | 无向 | 赫尔辛基大学时期结识的作家 |

> 恩主 **Henrik Liljeroos**（资助其大学学费）page.md 明载，但无对应白名单关系类型（非师承/非思想影响），本批不入库并在此注记。page.md 无师承、无弟子记载，**禁写**。

### 第 5 步：设计配色方案

- **主色**（批次预分配）：深湖青 `#0B5351`（夏夜湖水与田野的深邃）
- **辅色**：诺奖香槟金 `#C9A227`
- **badgeA–D**：badgeA 乡土现实主义 — 麦金 `#B08D3E`；badgeB 自然书写 — 苔绿 `#4E6E58`；badgeC 社会小说 — 铁灰 `#5A6472`；badgeD 诗性散文 — 暮紫 `#5B4A6B`
- **背景母题**：地平线分层 + 夏夜渐变色块（深青→暮紫）。

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享首页）
01  封面 — 田野与夏夜 / Frans Eemil Sillanpää 1888–1964 + 主色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、出身、教育、家庭、荣誉、核心领域）
03  核心贡献概览 — Meek Heritage / 少女西丽亚 / 夏夜的人们 / 农民与自然
04  农家之子 (1888–1908) — Hämeenkyrö、坦佩雷中学、Liljeroos 资助
05  赫尔辛基：弃医从文 (1908–1913) — 学医未成、艺术家友人圈、1913 返乡
06  早期写作 (1914–1919) — Uusi Suometar 撰稿、Elämä ja aurinko、Hurskas kurjuus 内战争议
07  多产期与国际声誉 (1923–1934) — 少女西丽亚 (1931)、夏夜的人们 (1934)
08  官方获奖理由引文框（EN 原文 + 中译，禁止改写）
09  1939：芬兰首位诺奖与冬季战争 — 赴斯德哥尔摩领奖、捐奖章熔金助战、丧妻
10  晚年 (1941–1964) — 离婚与病困、Sillanpää 爷爷、圣诞夜电台讲话
11  荣誉与纪念 — 小行星 1446 Sillanpää、Aleksis Kivi Award、狮子勋章、1980 邮票
12  作品改编 — 1937–1988 七部电影的对应表
13  遗产 — 芬兰乡土叙事的坐标、农民与土地的文学纪念碑
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- 版式：作品年表页用两栏小表；1939 页（诺奖+战争+丧妻）信息密度高，注意 itemize 行距；引文框用 tcolorbox。
- **陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名重音 | Frans Eemil Sillanpää（ä 双写），目录名与 MAIN 文件名均含 ä，Makefile/tex 注意 UTF-8 |
| 国籍口径 | 出生时为芬兰大公国（Grand Duchy of Finland），主条目按 Finland；勿写「俄国作家」 |
| 芬兰首位 | 「首位获诺贝尔文学奖的芬兰作家」（page.md 明载 first Finnish writer） |
| 诺奖理由 | 官方 EN 整句 + CITATION_ZH 中译，禁止改写；核心是「农民+与自然的关系」 |
| 捐章史实 | 捐出金奖章熔金助战是 page.md 明载（冬季战争爆发数日后），勿改写成「卖章」 |
| 内战立场 | *Hurskas kurjuus* 因「客观approach」引发争议——只写 page.md 这一笔，不站队 |
| 恩主不入库 | Liljeroos 资助入学 page.md 明载但无白名单类型，不入关系表（提示词内可叙述） |
| 学医未成 | 大学专业是医学，后弃医从文；勿写成文学科班 |
| 无直接引语 | page.md 无本人原话引用，禁编造名句 |
| 同名区分 | 页面 See also 的 Juhani Aho 是其大学相识的作家，非亲属；小行星 1446 勿写成「星座」 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| rural realism | 乡土现实主义 | 与「自然主义」区分，核心是农民+自然 |
| Hurskas kurjuus / Meek Heritage | 神圣的贫困 | 1919，内战题材 |
| Nuorena nukkunut / The Maid Silja | 少女西丽亚 | 1931，代表作，infobox Notable work |
| Ihmiset suviyössä / People in the Summer Night | 夏夜的人们 | 1934，设计母题来源 |
| Winter War | 冬季战争 | 1939-11 爆发，与领奖几乎同时 |
| Sillanpään marssilaulu | 西兰帕进行曲 | 战时歌词 |
| Henrik Liljeroos | 恩主 | 资助入学，不入关系库 |
| Yrjö Väisälä | 小行星发现者 | 天文学家兼物理学家 |
| Grandpa Sillanpää | 西兰帕爷爷 | 1943 复出形象 |
| Christmas Eve broadcast | 圣诞夜广播 | 1945–1963 年度传统 |
| 1446 Sillanpää | 小行星 | 1938 发现命名 |
| Grand Duchy of Finland | 芬兰大公国 | 出生时政体 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（批次预分配）
- **匹配理由**：「原野感/原始自然之力」匹配其文学世界的两极——笔下原始而丰饶的土地生命力，以及 1939 年冬季战争的凛冽突袭（领奖与战争、捐章与丧妻同月）。曲名的野性张力对应「反对一切暴力却直面暴力年代」的命运反差，也呼应北欧荒野的自然书写传统。
- **对照**：`music_audio/curated_tracks.md`（alex-productions 系列）。封面主色 `#0B5351`，批次内唯一。
