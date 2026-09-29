# 文学家立传提示词（OpenLiterature：Bjørnstjerne Bjørnson）

> **本文件是比昂斯滕·比昂松（1903 诺贝尔文学奖）的人物专属立传提示词**，结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容按文学家适配：无公式框，以**代表作书影/名句引文框/意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各学科侧共享体系）。
- **本实例**：Bjørnstjerne Bjørnson（比昂斯滕·比昂松），1903 诺贝尔文学奖得主，**挪威文学「四大家」之一、挪威国歌歌词作者、首位挪威诺奖得主**。
- **设计哲学**：文学家立传以**作品意象与文学史脉络**替代公式与实验——身份信息页（★ 必做）与「文学领域」结构化表达仍须保留。比昂松的特例性在于「文学 + 公共生活」双重巨影：诗、剧、小说、政论、演说五位一体，全篇须呈现「国民诗人」的公共维度。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Bjørnstjerne Martinius Bjørnson（1832-12-08 克维克内 ~ 1910-04-26 巴黎，享年 77 岁）
- **气质关键词**：**国民诗人、农民叙事的开创者、不知疲倦的公共鼓动家** —— 1903 诺贝尔文学奖官方获奖理由：
  > EN: "as a tribute to his noble, magnificent and versatile poetry, which has always been distinguished by both the freshness of its inspiration and the rare purity of its spirit"
  > 中译：表彰其高贵、宏伟而多样的诗歌，始终以灵感的清新与精神的罕见纯粹著称（引自 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）
- **设计母题**：**山间农庄与峡湾之光（Bjørgan 农庄 + Aulestad）**。其「农民小说」（bonde-fortellinger）把挪威乡土写成史诗——视觉母题用「山谷农舍剪影 + 峡湾冷光 + 白桦林」，配以国歌《Ja, vi elsker dette landet》的乐谱线条元素。
- **本地数据源**：`literature/presentations/pages/20th_century/Bjørnstjerne_Bjørnson/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Bj%C3%B8rnstjerne_Bj%C3%B8rnson （肖像：第 0 步**待下载**，正文有 1909 年照与 1882 全家福）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面已抓取到上述路径（本提示词即其事实基准，第一轮已核对）：
  - 生卒：1832-12-08 生于克维克内（Bjørgan 农庄，瑞典-挪威联合王国）~ 1910-04-26 卒于巴黎（晚年常在巴黎过冬），享年 77；遗体由海防舰 HNoMS Norge 护送回国，备极哀荣下葬
  - 家庭：父 Peder Bjørnson 为牧师（1837 调任 Nesset 教区，童年于 Nesset 牧师宅度过）；母 Inger Elise Nordraach；1858 娶 Karoline Reimers（1835–1934），育六子五人成人：Bjørn（1859–1942）、Einar（1864–1942）、Erling（1868–1959）、Bergliot（1869–1953，嫁 Ibsen 家）、Dagny 两夭一存（1876–1974）；1860 于丹麦与女演员 Magda von Dolcke 有私情（1861 年底与妻和好后终止）；五十岁出头与 Guri Andersdotter 有私生子 Anders Underdal（1880–1973，诗人，其女为作家 Margit Sandemo）——此事为其家庭秘密（Thorsen 1999 专著）
  - 教育：17 岁入 Christiania 的 Heltberg Latin School（与 Ibsen、Jonas Lie、Vinje 同校）；1852 入奥斯陆大学，随即投身新闻与戏剧评论
  - 任职：1857 年底任卑尔根剧院院长两年；1860–1863 周游欧洲；1865 主持 Christiania 剧院；定居 Aulestad 庄园（Gausdal）
  - 关键荣誉：Nobel 文学奖 1903（首位挪威得主）；挪威诺贝尔委员会创始委员（1901–1906，授和平奖）
  - 关键时间线（18 节点）：1832 生于克维克内 → 1837 迁 Nesset → 17 岁入 Heltberg 学校 → 1852 入奥斯陆大学 → 1855《Mellem Slagene》（1857 上演）→ 1857《Synnøve Solbakken》（首部农民小说）+ 卑尔根剧院院长 → 1858《Arne》、与 Karoline 成婚 → 1859《En glad Gut》→ 1860–63 欧游 → 1861《Kong Sverre》→ 1862《Sigurd Slembe》三部曲 → 1865 主持 Christiania 剧院（《De Nygifte》）→ 1870《Poems and Songs》与史诗环《Arnljot Gelline》（含名篇《Bergliot》）→ 1870s 与 Grieg 友谊与合作 → 1874《En fallit》《Redaktøren》（社会问题剧转向）→ 1874–76 自愿流外恢复创作力 → 1877《Kongen》《Magnhild》→ 1879《Leonarda》→ 1881 Wergeland 纪念碑演说 → 1882 叛国指控后避居德国，同年归国 → 1883《En Handske》《Over Ævne I》→ 1884《Det flager i Byen og paa Havnen》→ 1889《Paa Guds Veje》→ 1895《Over Ævne II》→ 1898 为《Ringeren》撰稿、Dreyfus 案声援 → 1899 国家剧院开幕庆典 → 1901–06 挪威诺贝尔委员会委员 → 1903 诺贝尔文学奖 → 1905 挪瑞分裂之际倡节制 → 1910 卒于巴黎

### 第 1–3 步：建目录 / 复制 Makefile / 收图 【模板通用】

- 在 `literature/presentations/20th_century/Bjørnstjerne_Bjørnson/` 建目录与 `images/`；Makefile `MAIN=Bjørnstjerne_Bjørnson_zh`；肖像第 0 步下载。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peasant novels | 农民小说 | bonde-fortellinger：《Synnøve Solbakken》《Arne》等 | 核心页 |
| 1 | national romanticism | 民族浪漫主义 | 民族戏剧 folke-stykker 与萨迦剧 | 定位页 |
| 2 | lyric poetry | 抒情诗 | 国歌歌词、《Poems and Songs》《Bergliot》 | 诗歌页 |
| 3 | social drama | 社会问题剧 | 《En fallit》《Redaktøren》《Leonarda》 | 戏剧页 |
| 4 | polemical journalism | 政论杂文 | 欧洲各大报数百篇文章、演说鼓动 | 公共页 |

#### 4.1 入库操作

- `MySQL/data/Bjørnstjerne_Bjørnson.yaml`（name_en=`Bjørnstjerne Bjørnson`，qid=Q46405，primary_occupation=`writer`），`python3 seed_person.py data/Bjørnstjerne_Bjørnson.yaml`。
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id JOIN people p ON p.id=pf.person_id WHERE p.qid='Q46405' ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Karoline Reimers | 无向 | 1858 年成婚，相伴至终（Karoline 卒于 1934） |
| parent-child | Bjørn Bjørnson | — | 长子，剧场导演 |
| parent-child | Einar Bjørnson | — | 子 |
| parent-child | Erling Bjørnson | — | 子 |
| parent-child | Bergliot Ibsen | — | 女（嫁 Ibsen 家），回忆录作者 |
| colleague | Edvard Grieg | 无向 | 挚友，格里格为其诗谱曲（Landkjenning、Sigurd Jorsalfar），歌剧合作未成 |
| colleague | Henrik Ibsen | 无向 | 挪威文学「四大家」并称；同出 Heltberg 学校 |
| colleague | Jonas Lie | 无向 | 挪威文学「四大家」并称 |
| colleague | Alexander Kielland | 无向 | 挪威文学「四大家」并称 |
| colleague | Ivar Aasen | 无向 | 支持其语言事业，1860–70 年代并肩政治斗争 |
| colleague | Sigurd Ibsen | 无向 | 为其主编的反 Union 杂志《Ringeren》（1898）撰稿 |
| influence | Henrik Wergeland | 对方为思想影响者 | 自青年时代敬仰，1881 年 Wergeland 纪念碑演说人 |
| influence | Jens Immanuel Baggesen | 对方为思想影响者 | 早期民族戏剧创作期明言受其研究影响（哥本哈根之行） |
| influence | Adam Gottlob Oehlenschläger | 对方为思想影响者 | 早期民族戏剧创作期明言受其研究影响（哥本哈根之行） |
| controversy | Georg Brandes | 无向 | 北欧性道德论战（sedelighetsdebatten）中因观点相左决裂 |

> **不入库并注明**：Magda von Dolcke（1860 私情）、Guri Andersdotter 与私生子 Anders Underdal（家庭秘密）不建关系行，仅可在提示词事实层简述；作曲家 Fredrikke Waaler、Anna Teichmüller 及七位据《Arne》谱曲的丹麦作曲家属作品改编关系，不入库。

#### 4.5.1 入库操作

- yaml `relations` 与上表完全一致（parent-child 不写 direction，引擎按 from<to 归一）；stub 不编造 qid。
- 校验：`SELECT r.type, p2.name_en FROM person_relation r JOIN people p ON p.id=r.from_id JOIN people p2 ON p2.id=r.to_id WHERE p.qid='Q46405' OR p2.qid='Q46405'`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：山野的清新、公民的热忱、北国的澄澈
- **配色**：主色峡湾深青 `#0E4D64` + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 农民小说 — 麦田金 `#C89B3C`
  - `badgeB` 抒情诗/国歌 — 靛蓝 `#2C4E80`
  - `badgeC` 社会问题剧 — 砖红 `#A34A2A`
  - `badgeD` 萨迦剧/民族浪漫 — 苔绿 `#4A6741`
- **背景母题**：稀疏山形剪影 + 峡湾冷色大圆（四档错落），呼应「山间农庄」母题。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像（1909 照优先）+ 姓名小字注；底部状态栏 `国籍 | 身份 | 主要奖项`。
2. **身份信息页（★ 必做）**：左头像 + 右信息网格（生卒、国籍、出生地、教育、家庭、任职、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`；挪威字符 ø/å 用 XeLaTeX 原生字体直接排（无需特殊字体族）。
4. 无公式框：以**国歌歌词原句引文框**（Ja, vi elsker dette landet）与**农民小说书影/农庄意象图式**替代。

### 第 6 步：规划幻灯片序列 【人物专属，14 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 国民诗人 / Bjørnstjerne Bjørnson 1832–1910 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 农民小说 / 抒情诗 / 社会剧 / 萨迦剧四徽章
04  牧师宅童年 (1832–1852) — Kvikne、Nesset、Bjørgan 农庄意象
05  Heltberg 与奥斯陆 — 与 Ibsen/Lie/Vinje 同校、大学、新闻与剧评
06  农民小说开创 (1857–1868) — Synnøve Solbakken、Arne、En glad Gut、Fiskerjenten
07  萨迦与史诗 — Mellem Slagene、Kong Sverre、Sigurd Slembe、Arnljot Gelline
08  剧院掌门 — 卑尔根院长、Christiania 剧院、De Nygifte、Mary Stuart
09  与格里格 — 友谊、谱曲合作、Peer Gynt 风波与和解
10  社会问题剧转向 (1874–1883) — En fallit、Redaktøren、Leonarda、Over Ævne
11  公共鼓动家 — Wergeland 演说、语言之争、Dreyfus 案、性道德论战与 Brandes 决裂（客观简述）
12  1903：诺贝尔文学奖 — 官方理由 EN+中译引文框、首位挪威得主、诺委会委员身份的趣味张力
13  晚年与国葬 — 挪瑞分裂倡节制、1910 卒于巴黎、HNoMS Norge 护灵、Aulestad
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 make 编译，pdftoppm 截图检查溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Bjørnson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生卒双值 | frontmatter 出生有 1832-12-08 / 1832-01-01、死亡有 1910-04-26 / 1910-01-01 两值；以正文 infobox **1832-12-08 ~ 1910-04-26** 为准 |
| 诺委会张力 | 1903 获文学奖时他本人正任挪威诺贝尔委员会（和平奖）委员（1901–1906）——正文实载，可作趣点客观呈现，勿演绎为丑闻 |
| 政治内容 | Pan-Germanist 言论（1901）、挪瑞分裂立场、Černová 惨案文章：只按 page.md 客观事实一笔带过，**不作政治评价**；宜回避或极简处理 |
| 四大家 | Ibsen/Lie/Kielland 并称出自正文，四人关系用 colleague，勿写成师承 |
| Grieg 风波 | 歌剧《Olav Trygvason》因词曲先后之争搁浅，Grieg 转为 Ibsen《Peer Gynt》配乐「自然触怒了比昂松」——正文原话口径，后来友谊恢复 |
| 农民言论 | 1899「农民的开垦到此为止」名言与对农民态度的矛盾（其父即农夫之子）——按正文呈现其态度的 ambiguous，勿简化 |
| 私生活 | Magda von Dolcke 私情与 Guri Andersdotter 私生子为正文实载，提示词可简述、**不入库关系**；呈现时克制 |
| 作品年份 | 《Digte og Sange》书目作 1880 而正文叙事作 1870《Poems and Songs》——两说并存时叙事页用 1870、书目页照书目，加注即可 |
| 叛国指控 | 政治言论曾被控叛国、避居德国（1882 归国）——客观一句，不展开 |
| 同名区分 | Bergliot Ibsen 是其女（嫁入 Ibsen 家），与 Henrik Ibsen 无血缘；Sigurd Ibsen 是 Henrik 之子，两人勿混 |

**术语清单**：

| 英文/原文 | 中文 | 风险 |
|------|------|------|
| bonde-fortellinger | 农民小说 | 其代表文体，勿译「农场故事」 |
| folke-stykker | 民族戏剧（民众剧） | 与萨迦剧区分 |
| Ja, vi elsker dette landet | 《是，我们热爱这片土地》 | 挪威国歌歌词 |
| Synnøve Solbakken | 《叙内芙·索尔巴肯》 | 首部农民小说 |
| Sigurd Slembe | 《西格德·斯伦贝》三部曲 | 1862 代表剧 |
| En fallit | 《破产》 | 1874 社会剧 |
| Redaktøren | 《主编》 | 1874 社会剧 |
| Over Ævne | 《超越人力》I/II | 宗教狂热题材 |
| sedelighetsdebatten | 北欧性道德论战 | 与 Brandes 决裂背景 |
| Heltberg Latin School | 赫尔特贝格学校 | 四大家共同母校 |
| Aulestad | 奥勒斯塔庄园 | 1874 起定居地 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions
- **匹配理由**：
  - 「历史感/深沉」匹配 19 世纪挪威民族文学的黄金时代与国歌作者的历史地位
  - 曲目的岁月质感匹配从 Kvikne 农庄到巴黎国葬的八十年长跨度叙事
  - 深沉而不失暖意，匹配「农民小说」的乡土温度与公共鼓动家的赤忱
- **本地路径**：对照 `music_audio/curated_tracks.md` 中 alex-productions PAST 条目复制到本目录。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Bjørnstjerne_Bjørnson/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 官方理由中译（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |
