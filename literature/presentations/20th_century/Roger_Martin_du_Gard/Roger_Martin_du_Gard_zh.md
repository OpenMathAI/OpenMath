# 文学家立传提示词（OpenLiterature 批次实例：Roger Martin du Gard）

> 本文件是 OpenLiterature 的「文学家立传提示词」，以 Roger Martin du Gard（1937 诺贝尔文学奖，《蒂博一家》）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框，以代表作书影/名句引文框/意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，结尾页品牌统一 `OpenMathAI`）。
- **本实例**：Roger Martin du Gard（罗歇·马丁·杜·加尔），1937 诺贝尔文学奖得主，法国长河小说大家。
- **设计哲学**：文学家立传以「代表作意象 + 文学领域结构化表达 + 身份信息页」为骨架；du Gard 的核心视觉语言是**长河（roman fleuve）**——分卷流淌、编年式推进的家族叙事之河。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Roger Martin du Gard（1881-03-23 ~ 1958-08-22，享年 77 岁）
- **气质关键词**：**长河小说的筑河人、档案式的客观主义者、和平主义的记录者**
- **官方获奖理由（1937）**：
  > EN: "for the artistic power and truth with which he has depicted human conflict as well as some fundamental aspects of contemporary life in his novel cycle Les Thibault"
  > 中译：表彰其小说系列《蒂博一家》以艺术的力量与真实描绘了人的冲突以及当代生活的某些基本面貌
  > （来源：`literature/generate_20th_century_list.py` CITATION_ZH[("1937","Roger Martin du Gard")] + `literature/nobel_literature_citations.json`，禁止改写）
- **设计母题**：**长河与分卷（the river and its volumes）**——roman fleuve 以多卷本顺流而下，两兄弟（Antoine 与 Jacques Thibault）是并行的两条支流，最终汇入第一次世界大战的入海口。版式可用河流分段线、卷册层叠图式。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Roger_Martin_du_Gard/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL: https://en.wikipedia.org/wiki/Roger_Martin_du_Gard
  - 肖像（第 0 步下载）：`images/` 下待下载（Wikipedia infobox / Commons，404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md）

- **生卒**：1881-03-23 生于法国 Neuilly-sur-Seine（塞纳河畔讷伊）~ 1958-08-22 卒于法国 Sérigny（奥恩省），享年 77 岁。
- **国籍**：法国（France）。
- **身份**：novelist（小说家）；frontmatter 兼载 archivist（档案学家/古文书学家）与 playwright（剧作家）。
- **教育**：Lycée Janson-de-Sailly、Lycée Condorcet；École des chartes（古文书学校，受训为 paleographer 古文书学家）、École du Louvre。古文书学与档案训练赋予其「客观精神与对细节的严谨」。
- **家庭**：page.md 未载妻子子女——**禁写**。
- **文学师承与影响**：page.md 明载两点——其虚构作品与 19 世纪**现实主义/自然主义**传统相连；他同情 Jean Jaurès 的**人道社会主义与和平主义**，并在作品中显明（这是思想影响，非师承交往）。
- **核心作品与贡献（4–6 条）**：
  1. *Les Thibault*（《蒂博一家》）——多卷本 roman fleuve，写两兄弟 Antoine 与 Jacques Thibault 从天主教资产阶级家庭成长到一战结束；六部 1922–1929 出版，第七部手稿被放弃，另有两卷 1936 与 1940 年出版（后半部分比前六部合起来还长，聚焦一战爆发前的政治局势，故事止于 1918）。
  2. *Jean Barois*（1913）——以德雷福斯事件（Dreyfus affair）为历史背景（1950 年英译）。
  3. *Confidence africaine*（1930）/ *Vieille France*（1933，英译 *The Postman*）。
  4. 战时在尼斯准备的长篇 *Souvenirs du lieutenant-colonel de Maumort*，去世时未完成，1983 年遗作出版。
  5. 回忆录 *Notes sur André Gide*（1951）——记其多年挚友 Gide。
- **关键荣誉**：Nobel 1937；Commander of the Legion of Honour（荣誉军团指挥官勋章）；Grand Prix littéraire de la Ville de Paris。
- **关键时间线（17 节点）**：
  1. 1881-03-23 生于 Neuilly-sur-Seine
  2. 就读 Lycée Janson-de-Sailly
  3. 就读 Lycée Condorcet
  4. 入 École des chartes，受训古文书学家（paleographer）
  5. 入 École du Louvre
  6. 1908 处女作 *Devenir !*
  7. 1913 *Jean Barois*（德雷福斯事件背景）
  8. 1922 *Les Thibault* 开始出版
  9. 1929 前六部出齐（1922–1929）
  10. 1930 *Confidence africaine*
  11. 1933 *Vieille France*
  12. 1936 *Les Thibault* 续卷之一出版
  13. 1937 诺贝尔文学奖
  14. 1940 *Les Thibault* 末卷出版（英译 *Summer 1914* 部分）
  15. 二战期间居尼斯，写 *Maumort*
  16. 1951 *Notes sur André Gide*
  17. 1958-08-22 卒于 Sérigny，葬于尼斯郊外 Cimiez 修道院墓园；1983 遗作 *Maumort* 出版

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- `literature/presentations/20th_century/Roger_Martin_du_Gard/`（含 `images/`）；Makefile 设 `MAIN=Roger_Martin_du_Gard_zh`；肖像按 `images.txt` 下载，404 用装饰圆占位。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | roman fleuve | 长河小说 | 多卷本家族编年叙事，《蒂博一家》为其代表 | 核心页 |
| 1 | literary realism | 现实主义 | 档案式客观精神，19 世纪传统延续 | 方法页 |
| 2 | naturalism | 自然主义 | 对社会现实与个体发展的记录式关注 | 方法页 |
| 3 | social criticism | 社会批判 | 人道社会主义与和平主义主题 | 主题页 |

- 入库：`MySQL/data/Roger_Martin_du_Gard.yaml` → `python3 seed_person.py data/Roger_Martin_du_Gard.yaml`（primary_occupation: writer）。

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | André Gide | 无向 | 长期挚友，1951 年出版回忆录 Notes sur André Gide |
| influence | Jean Jaurès | Jaurès → du Gard | 其人道社会主义与和平主义思想在作品中显明 |

> page.md 仅明载以上两条：Jaurès 是「同情其思想」，**不是**师承/交往；Gide 是挚友非师生。妻子、子女、弟子均无载，**禁写**。

### 第 5 步：设计配色方案

- **主色**（批次预分配）：深松绿 `#1B4D3E`（河流纵深与档案的沉稳）
- **辅色**：诺奖香槟金 `#C9A227`
- **badgeA–D**：badgeA 长河小说 — 河蓝 `#2C6E8F`；badgeB 现实主义 — 档案灰 `#6B7280`；badgeC 自然主义 — 苔绿 `#4E6E58`；badgeD 社会批判 — 赭红 `#A34730`
- **背景母题**：水平向的河流分段线 + 稀疏卷册圆角矩形（象征分卷流淌）。

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享首页）
01  封面 — 长河小说的筑河人 / Roger Martin du Gard 1881–1958 + 主色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、出生地、教育、荣誉、核心领域）
03  核心贡献概览 — 蒂博一家 / Jean Barois / 档案式方法 / Gide 回忆录
04  早年：讷伊与古文书学校 (1881–1908) — Janson-de-Sailly、Condorcet、École des chartes、École du Louvre
05  早期作品 — Devenir! (1908) 与 Jean Barois (1913，德雷福斯事件背景)
06  《蒂博一家》：长河的诞生 (1922–1929) — 两兄弟并行叙事、前六部
07  战争阴影下的续卷 (1936–1940) — 第七部放弃手稿、末两卷聚焦一战前夜
08  档案式客观性（意象图式页，替代公式框）— paleographer 训练 → documentation 方法 → realism/naturalism
09  官方获奖理由引文框（EN 原文 + 中译，禁止改写）
10  荣誉与认可 — Nobel 1937、荣誉军团指挥官勋章、巴黎文学大奖
11  Gide 友谊 — 挚友与 Notes sur André Gide (1951)
12  二战与晚年 — 居尼斯、Sérigny 辞世、Cimiez 葬地
13  遗产 — 遗作 Maumort (1983)、roman fleuve 传统的坐标
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- 版式：引文框用 tcolorbox/quotestyle；时间线页节点 ≥15 用两栏；身份页左图右网格。
- **陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓氏书写 | 姓是 Martin du Gard 整体，正式名 Roger Martin du Gard；勿拆成 "Roger Martin" + "du Gard" 两名 |
| 诺奖理由 | 必须引用官方 EN 原文整句 + CITATION_ZH 中译，禁止改写或缩写 |
| 蒂博卷数 | 前六部 1922–1929 + 放弃的第七部手稿 + 1936/1940 两卷；英译分 *The Thibaults* 与 *Summer 1914* 两册，勿写「七卷本」 |
| Jaurès 关系 | 是「同情其人道社会主义与和平主义（思想影响）」，非师承、非交往，禁写成导师或战友 |
| Gide 关系 | longtime friend + 1951 回忆录；非师生、非合作著述 |
| 三个地名 | 生于 Neuilly-sur-Seine、卒于 Sérigny（奥恩省）、葬于 Cimiez（尼斯郊外），三地勿混 |
| 无直接引语 | page.md 无本人原话引用，禁编造名句；第 9 页引文框只用官方获奖理由 |
| 家庭无载 | 妻子/子女 page.md 未载，禁写 |
| 政治内容 | 只写 page.md 明载的「人道社会主义与和平主义的同情」一笔，不展开政治叙事 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| roman fleuve | 长河小说 | 多卷本家族/编年小说，非「河流小说」字面 |
| paleographer | 古文书学家 | École des chartes 训练背景 |
| archivist | 档案学家 | 职业字段明载 |
| Les Thibault / The Thibaults | 蒂博一家 | 法文原题与英译题勿混 |
| Jean Barois | 让·巴鲁瓦 | 德雷福斯事件背景 |
| Dreyfus affair | 德雷福斯事件 | 历史背景框架 |
| humanist socialism | 人道社会主义 | 归属 Jaurès 思想 |
| pacifism | 和平主义 | 与 Jaurès 思想并提 |
| naturalism | 自然主义 | 与 realism 并提的 19 世纪传统 |
| Confidence africaine | 非洲密谈（1930） | 中篇 |
| Vieille France / The Postman | 老法兰西（1933） | 英译题不同 |
| Grand Prix littéraire de la Ville de Paris | 巴黎市文学大奖 | 与军团勋章并列荣誉 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（批次预分配）
- **匹配理由**：长河小说 roman fleuve 本身就是「时间之流」的文学形态——分卷顺流、编年推进、终入一战海口；曲名的「时间流逝感」与母题「长河」直接同构。沉稳纪录片气质匹配档案式客观主义者的克制叙事。
- **对照**：`music_audio/curated_tracks.md`（alex-productions 系列）。封面主色 `#1B4D3E`，批次内唯一。
