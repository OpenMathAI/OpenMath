# 文学家立传提示词（OpenLiterature：Sully Prudhomme）

> **本文件是苏利·普吕多姆（1901 首届诺贝尔文学奖）的人物专属立传提示词**，结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容按文学家适配：无公式框，以**代表作书影/名句引文框/意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各学科侧共享体系）。
- **本实例**：Sully Prudhomme（苏利·普吕多姆），**诺贝尔文学奖史上第一位得主**（1901）。
- **设计哲学**：文学家立传与科学家立传的核心差异，在于以**作品意象与文学史脉络**替代公式与实验——身份信息页（★ 必做）与「文学领域」结构化表达仍须保留，构成骨架。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Sully Prudhomme（本名 René François Armand Prudhomme，1839-03-16 巴黎 ~ 1907-09-06 沙特奈-马拉布里，享年 68 岁）
- **气质关键词**：**首届诺奖桂冠、帕纳索斯派的哲人、科学诗的追梦者** —— 1901 诺贝尔文学奖官方获奖理由：
  > EN: "in special recognition of his poetic composition, which gives evidence of lofty idealism, artistic perfection and a rare combination of the qualities of both heart and intellect"
  > 中译：表彰其诗作展现出崇高的理想主义与艺术上的完美，并罕见地兼具心灵与智慧两种品质（引自 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）
- **设计母题**：**碎瓶与理想之光（Le vase brisé）**。其最著名的诗《破碎的花瓶》以裂纹暗喻人心的隐伤——立传视觉可用「瓷器裂纹 + 柔光透射」贯穿全篇，呼应「形式完美（帕纳索斯派）之下涌动的哲思与感伤」。
- **本地数据源**：`literature/presentations/pages/20th_century/Sully_Prudhomme/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Sully_Prudhomme （肖像：第 0 步**待下载**，images.txt 有 URL 则直接用，否则 Commons Special:FilePath / REST API 回退，仍缺用装饰圆占位）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面已抓取到上述路径（本提示词即其事实基准，第一轮已核对）：
  - 生卒：1839-03-16 生于巴黎（七月王朝）~ 1907-09-06 卒于沙特奈-马拉布里（法兰西第三共和国），享年 68；葬于巴黎拉雪兹神父公墓
  - 本名 René François Armand Prudhomme；父为小店主，在他 2 岁时去世；母 Clotilde Caillat；「Sully」取自父名与姓氏连用
  - 教育：Lycée Bonaparte（即 Lycée Condorcet）因眼疾中断；曾入勒克鲁佐 Schneider 钢铁厂做工；后在公证人处习法律；学生社团 Conférence La Bruyère 对其早年诗的嘉许促其转向文学；一度考虑入多明我会未果
  - 国籍：法国；语言：法语
  - 文学派别：帕纳索斯派（Parnassianism），但作品自具特色
  - 关键荣誉：Nobel 文学奖 1901（首届）；正文实载 Légion d'honneur 骑士级（1895）；Académie française 院士（1881）
  - 1902 与 Jose-Maria de Heredia、Leon Dierx 共同创立 Société des poètes français；将奖金大部分捐给 Société des gens de lettres 设立诗歌奖
  - 关键时间线（18 节点）：1839 生于巴黎 → 2 岁丧父 → Lycée Bonaparte（眼疾中断）→ 勒克鲁佐钢铁厂 → 公证人处习法 → Conférence La Bruyère 嘉许 → 1865《Stances et Poèmes》（Sainte-Beuve 盛赞，含名篇《Le vase brisé》）→ 1866《Les épreuves》→ 1868《Croquis italiens》→ 1869《Les solitudes》→ 1870–71 普法战争（健康从此受损）→ 1872《Les destins》《Impressions de la guerre》→ 1874《La France》《La révolte des fleurs》→ 1875《Les vaines tendresses》→ 1876《Le zénith》→ 1878《La justice》→ 1881 入选法兰西学术院 → 1884《L'Expression dans les beaux-arts》→ 1888《Le bonheur》→ 1890《两世界评论》论帕斯卡系列文章 → 1892《Réflexions sur l'art des vers》→ 1895 获军团骑士勋章 → 1901 首届诺奖 → 1902 创立法国诗人协会 → 1906《La Psychologie du Libre-Arbitre》→ 1907-09-06 猝逝于隐居地

### 第 1–3 步：建目录 / 复制 Makefile / 收图 【模板通用】

- 在 `literature/presentations/20th_century/Sully_Prudhomme/` 建目录与 `images/`；Makefile `MAIN=Sully_Prudhomme_zh`；肖像第 0 步下载。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | parnassian poetry | 帕纳索斯派诗歌 | 与帕纳索斯学派相连而自具特色 | 学派页 |
| 1 | philosophical poetry | 哲理诗 | 《La justice》《Le bonheur》表达其哲学 | 哲理页 |
| 2 | lyric poetry | 抒情诗 | 名篇《Le vase brisé》 | 成名页 |
| 3 | scientific poetry | 科学诗 | 自言要为现代创造「科学诗」 | 定位页 |
| 4 | aesthetics | 美学随笔 | 《L'Expression dans les beaux-arts》等 | 随笔页 |

#### 4.1 入库操作

- `MySQL/data/Sully_Prudhomme.yaml`（name_en=`Sully Prudhomme`，qid=Q42247，primary_occupation=`writer`），`python3 seed_person.py data/Sully_Prudhomme.yaml` 写入 greatminds。
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id JOIN people p ON p.id=pf.person_id WHERE p.qid='Q42247' ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Lucretius | 对方为思想影响者 | 《De rerum natura》为其明确灵感来源，曾将第一卷译为韵文 |
| colleague | Jose-Maria de Heredia | 无向 | 1902 共同创立法国诗人协会 |
| colleague | Leon Dierx | 无向 | 1902 共同创立法国诗人协会 |

> **不入库并注明**：Sainte-Beuve 对其处女作的盛赞属批评褒扬，非师承/合作，不入库；Blaise Pascal 仅为其文章写作对象，非明载影响关系，不入库。

#### 4.5.1 入库操作

- yaml `relations` 与上表完全一致；Lucretius/Heredia/Dierx 均按 stub 新建（不编造 qid）。
- 校验：`SELECT r.type, p2.name_en FROM person_relation r JOIN people p ON p.id=r.from_id JOIN people p2 ON p2.id=r.to_id WHERE p.qid='Q42247' OR p2.qid='Q42247'`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：瓷般工整、感伤内敛、理性微光
- **配色**：主色深酒红 `#8B1A1A`（首届桂冠的庄重）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 帕纳索斯派 — 靛蓝 `#4C5FD5`
  - `badgeB` 抒情诗 — 青绿 `#0E7C7B`
  - `badgeC` 科学诗 — 琥珀 `#E07B30`
  - `badgeD` 哲理诗 — 玫瑰 `#C4204F`
- **背景母题**：稀疏瓷白大圆 + 细裂纹线条（对应「碎瓶」母题），四档大小错落。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像（`draw=coveraccent!50` 细边框）+ 姓名小字注；封面底部状态栏给出 `国籍 | 文学派别 | 主要奖项`。
2. **身份信息页（★ 必做）**：封面之后、核心贡献之前；左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、文学派别、主要荣誉、核心领域），事实取自 page.md，不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
4. 无公式框：以**名句引文框**（《Le vase brisé》句）与**代表作书影/意象图式**替代。

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 首届诺奖桂冠 / Sully Prudhomme 1839–1907 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 帕纳索斯派 / 抒情 / 哲理 / 科学诗四徽章
04  早年：巴黎孤童 (1839–1857) — 丧父、Lycée Bonaparte、眼疾、多明我会之念
05  从钢铁厂到诗行 — Creusot Schneider、公证人习法、Conférence La Bruyère
06  成名：Stances et Poèmes (1865) — Sainte-Beuve 盛赞 + 《Le vase brisé》名句引文框
07  战争与创伤 (1870–1874) — Impressions de la guerre、La France、健康受损
08  哲理转向 — Lucretius 影响、《La justice》(1878)、《Le bonheur》(1888)
09  法兰西学术院与美学随笔 (1881–1892) — 院士、两篇重要美文、论帕斯卡
10  1901：首届诺贝尔文学奖 — 官方理由 EN+中译引文框、奖金捐设诗歌奖
11  晚年与遗产 — 隐居沙特奈-马拉布里、1902 法国诗人协会、1907 猝逝、拉雪兹墓
12  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 make 编译，pdftoppm 截图检查溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Prudhomme 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 死亡日期 | frontmatter 双值 1907-09-06 / 09-07，以正文 infobox **6 September 1907** 为准（09-06） |
| 姓名形式 | 本名 René François Armand Prudhomme；「Sully」取自父名，正文有「Sully-Prudhomme」连字形式，标题/infobox 用 **Sully Prudhomme**（无连字符），全篇统一无连字符形式 |
| Sainte-Beuve | 只是盛赞其处女作的批评家，**勿写成导师或影响者** |
| Pascal | 1890 年系列文章与 1905《La vraie religion selon Pascal》是**写作对象**，勿升格为「思想影响」关系 |
| 军团勋章 | 正文只实载骑士级（1895）；frontmatter 另列士官/指挥官/大军官诸级属层级噪声，以正文口径为主 |
| 学术院年份 | Académie française 入选 **1881**，勿与 1895 勋章年份混淆 |
| 奖金去向 | 大部分捐给 Société des gens de lettres 设立诗歌奖（非自留），1902 另创 Société des poètes français（与 Heredia、Dierx） |
| 无载禁写 | page.md 无婚姻/子女记载，禁写家庭；无直接引语原句（法文原诗名句仅《Le vase brisé》诗题与篇名层面引用，勿编造中文「原话」） |
| 同名区分 | 与 Gabriela Mistral（1945 得主，笔名取自本诗人）仅存在笔名渊源叙述，不在本篇展开 |

**术语清单**：

| 英文/原文 | 中文 | 风险 |
|------|------|------|
| Parnassianism | 帕纳索斯派（高蹈派） | 勿译「帕纳索斯主义」 |
| Le vase brisé | 《破碎的花瓶》 | 名篇，设计母题来源 |
| Stances et Poèmes | 《短句与诗》 | 1865 处女诗集 |
| La justice | 《正义》 | 1878 哲理诗 |
| Le bonheur | 《幸福》 | 1888 哲理诗 |
| De rerum natura | 《物性论》 | 卢克莱修，影响来源 |
| Académie française | 法兰西学术院 | 1881 入选 |
| Société des poètes français | 法国诗人协会 | 1902 共同创立 |
| lofty idealism | 崇高理想主义 | 获奖理由措辞 |
| Conférence La Bruyère | 拉布吕耶尔学社 | 学生社团，勿译成书名 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions
- **匹配理由**：
  - 「新大陆」贴合**首届诺奖得主**的开创身份——1901 年第一顶文学奖桂冠，文学史的新大陆由他开启
  - 曲风的开拓感匹配其「为现代创造科学诗」的野心与从工程学徒到诗人的转向
  - 纪实气质匹配从巴黎孤童到隐居逝者的沉稳叙事
- **本地路径**：对照 `music_audio/curated_tracks.md` 中 alex-productions New Lands 条目复制到本目录。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Sully_Prudhomme/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 官方理由中译（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |
