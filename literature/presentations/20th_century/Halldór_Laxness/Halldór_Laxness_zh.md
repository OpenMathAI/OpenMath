# 文学家立传提示词（Halldór Laxness / 哈尔多尔·拉克斯内斯）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Halldór Kiljan Laxness（哈尔多尔·拉克斯内斯，本名 Halldór Guðjónsson），冰岛作家，1955 年诺贝尔文学奖得主。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**以现代笔法更新冰岛萨迦叙事传统**的社会史诗上。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Halldór Kiljan Laxness（1902-04-23 ~ 1998-02-08，享年 95 岁）
- **诺奖年份**：1955 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for his vivid epic power, which has renewed the great narrative art of Iceland"
  > （中译：表彰其生动的史诗力量，更新了冰岛伟大的叙事艺术）
- **气质关键词**：**萨迦传统的更新者、弱者之笔、讽刺的怜悯**
- **设计母题**：**熔岩原上的长卷（the saga renewed）**——以"冰岛地貌横卷线 + 古抄本纹样"呼应：史诗力量（Elias Wessén 授奖辞）与叙事的现代更新。
- **本地数据源**：`literature/presentations/pages/20th_century/Halldór_Laxness/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Halld%C3%B3r_Laxness
- **肖像**：第 0 步待下载（1955 年照片；另有 Einar Hákonarson 1984 绘像，见正文插图）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1902-04-23 生于雷克雅未克（时为丹麦治下冰岛）~ 1998-02-08 逝于雷克雅未克（护理院，晚年患阿尔茨海默病），享年 95 岁。
- 国籍：冰岛。
- 家庭：3 岁随家迁居 Mosfellssveit 的 Laxnes 农场（笔名 Laxness 即取自农庄名）；祖母 Guðný Klængsdóttir 抚养并极大影响他（"会说话前就唱古老歌谣"，授奖演说引祖母教诲，英文原文在 page.md 可引）。婚姻三段关系：Málfríður Jónsdóttir 生长女 María（1923）；首任妻 Ingibjörg Einarsdóttir（1930–1940，生子 Einar 1931）；第二任妻 Auður Sveinsdóttir（1945 结婚，兼秘书与经纪人，1945 年迁入 Gljúfrasteinn），育二女 Sigríður（1951）、Guðný（1954，电影导演）。
- 教育：雷克雅未克技术学校（1915–16）；雷克雅未克 Lyceum（1918 毕业）。
- 宗教插曲：1922 年入卢森堡 Clervaux 本笃会修道院；1923 年受洗入天主教，取姓 Laxness、增名 Kiljan（爱尔兰殉道圣基利安的冰岛拼法）；此宗教期不长。
- 关键荣誉：诺贝尔文学奖 1955；世界和平理事会文学奖金 1952；Sonning Prize 1969。
- 核心作品与贡献（4–6 条）：
  1. 《Barn náttúrunnar》（Child of Nature，1919）——19 岁首部长篇；
  2. 《Vefarinn mikli frá Kasmír》（The Great Weaver from Kashmir，1927）——冰岛批评家誉为"当代冰岛诗与小说平原上耸立的悬崖"（转述可引）；
  3. 《Salka Valka》（1931–32）开社会小说长卷 →《Sjálfstætt fólk》（Independent People，1934–35，"二十世纪最好的书之一"之评）→ 四部曲《Heimsljós》（World Light，1937–40，多评者视其为最重要的作品）；
  4. 三部曲历史小说《Íslandsklukkan》（Iceland's Bell，1943–46）——"1940 年代最重要的冰岛小说"之评；
  5. 讽刺《Atómstöðin》（The Atom Station，1948）——《Gerpla》（1952，取材 Fóstbræðra saga）；
  6. 语言与翻译：自创贴近发音的拼写体系（译文中失落）；1941 年将海明威《A Farewell to Arms》译入冰岛语（因新造词引发争议）；以现代冰岛语重版萨迦（《Hrafnkels saga》1942 版权案，先判违版权法、后以出版自由获胜）。
- 关键时间线（15–20 节点）：
  1. 1902 生于雷克雅未克；1905 迁 Laxnes 农场；
  2. 1916 最早作品刊于《Morgunblaðið》与儿童刊物；
  3. 1918 Lyceum 毕业；
  4. 1919 首部长篇《Barn náttúrunnar》出版，旋即开始欧陆之行；
  5. 1922–23 Clervaux 修道院；受洗入天主教；
  6. 1924 《Undir Helgahnúk》；
  7. 1927 《Vefarinn mikli frá Kasmír》；
  8. 1927–29 旅居美国（演讲、好莱坞编剧尝试），转向社会主义；《Alþýðubókin》（1929）讽刺文集；因批评美国的文章遭指控、护照被扣，得 Upton Sinclair 与 ACLU 协助脱身回国；
  9. 1931–32 《Salka Valka》；
  10. 1934–35 《Independent People》；
  11. 1937–40 四部曲《World Light》；1938 访苏联并著《Gerska ævintýrið》；
  12. 1941 译《A Farewell to Arms》（新造词争议）；1942–43 萨迦现代语重版与版权案（终胜）；
  13. 1943–46 三部曲《Iceland's Bell》；
  14. 1945 与 Auður 结婚、迁入 Gljúfrasteinn；
  15. 1946 英译《Independent People》入选美国月读书 club，售逾 45 万册；
  16. 1948 《The Atom Station》（凯夫拉维克美军基地讽刺；其小说一度在美国遭封禁）；
  17. 1952 《Gerpla》；获世界和平理事会文学奖金；
  18. 1955 获诺贝尔文学奖（Elias Wessén 致授奖辞："Compassion is the source of the highest poetry" 引文在 page.md）；
  19. 1956 匈牙利事件后对苏联阵营日渐幻灭；1957 夫妇环球行（文化大使）；
  20. 1957《The Fish Can Sing》、1960《Paradise Reclaimed》、1966 剧作《Dúfnaveislan》、1968《Under the Glacier》、1969 Sonning 奖、1970 生态随笔《The War Against the Land》；1998 卒。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | epic narrative | 史诗叙事 | 官方诺奖理由"vivid epic power" | 核心页 |
| 1 | social novel | 社会小说 | Salka Valka → Independent People → World Light 长卷 | 核心页 |
| 2 | saga fiction | 萨迦题材小说 | Iceland's Bell、Gerpla——以现代笔法续写萨迦 | 萨迦页 |
| 3 | satire | 讽刺 | The Atom Station、Gerpla 的辛辣 | 讽刺页 |
| 4 | translation | 翻译 | 译海明威入冰岛语、现代冰岛语重版萨迦 | 语言页 |

#### 4.1 入库操作

- 新建 `people` 记录（name_en=`Halldór Laxness`，qid=Q80321），`primary_occupation='writer'`、`has_social_data=1`
- occupations：writer(0)、novelist(1)、translator(2)
- 5 个领域写入 `person_field`（epic narrative / saga fiction 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。影响者清单为 page.md 开篇明载（"Writers who influenced Laxness include…"）。政治议题（访苏、匈牙利事件、和平奖金）客观一句带过，不入库、不展开。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Ingibjörg Einarsdóttir | 无向 | 首任妻（1930–1940），子 Einar |
| spouse | Auður Sveinsdóttir | 无向 | 第二任妻（1945 起），兼秘书与经纪人 |
| parent-child | Guðný Halldórsdóttir | 本人→对方 | 女，电影导演，改编其作品 |
| influence | August Strindberg | 对方→本人 | page.md 明载影响者 |
| influence | Sigmund Freud | 对方→本人 | page.md 明载影响者 |
| influence | Knut Hamsun | 对方→本人 | 1920 年文学奖得主，page.md 明载影响者 |
| influence | Sinclair Lewis | 对方→本人 | 1930 年文学奖得主，page.md 明载影响者 |
| influence | Upton Sinclair | 对方→本人 | 影响者；1929 年助其脱诉 |
| influence | Bertolt Brecht | 对方→本人 | page.md 明载影响者 |
| influence | Ernest Hemingway | 对方→本人 | 影响者；1941 年译其《A Farewell to Arms》 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#14324F`（冰岛峡湾深蓝——熔岩与极夜的冷冽）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeEpic 靛蓝 `#4C5FD5`；badgeSaga 青绿 `#0E7C7B`；badgeSatire 琥珀 `#E07B30`；badgeLand 玫瑰 `#C4204F`
- **背景母题**：熔岩原横卷线（低饱和深蓝底 + 金色叙事线）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 萨迦的更新者 / Halldór Laxness 1902–1998 + badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/家庭/Gljúfrasteinn/荣誉/核心领域）
03  核心创作概览 — 史诗长卷 / 萨迦续写 / 讽刺 / 翻译与语言
04  早年：Laxnes 农场与祖母 (1902–1919)【引文框：授奖演说忆祖母】
05  修道院与天主教岁月 (1922–1927)——取姓 Laxness、增名 Kiljan
06  美国岁月与转向 (1927–1929)
07  社会长卷：《萨尔卡·瓦尔卡》《独立的人们》《世界之光》 (1931–1940)【书影】
08  《冰岛钟声》：萨迦的现代续写 (1943–1946)【书影】
09  《原子车站》与《Gerpla》 (1948–1952)
10  1955 诺贝尔文学奖 — 官方理由 EN 原文页 + Wessén 授奖辞要点
11  晚年与遗产：Gljúfrasteinn 博物馆、国际拉克斯内斯奖 (1957–1998)
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；身份页 `\profileslide`；冰岛专名保留 ð/þ 字符（XeLaTeX + 合适字体）。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 卒日噪声 | frontmatter death_date 三值（1998-02-08 / 1998-02-09 / 1988-02-08），以正文 **1998-02-08** 为准 |
| 姓名 | 本名 Halldór Guðjónsson；1923 年受洗后取姓 Laxness（农庄名）+ 名 Kiljan（圣基利安）——勿写成"笔名而已"的泛称 |
| 独立的人们定性 | "one of the best books of the twentieth century"是评论转述，可注明评论界 |
| 影响者清单 | Strindberg/Freud/Hamsun/Lewis/U. Sinclair/Brecht/Hemingway 七人全为 page.md 开篇明载——Hamsun 与 Lewis 是文学奖得主，注明年份区分"获奖者影响者"非"共同获奖" |
| 译作年份 | 1941 译《A Farewell to Arms》——Laxness 影响者名单里的 Hemingway，勿倒果为因写成 Hemingway 提携他 |
| 版权案 | Hrafnkels saga 案：先判违法、后以出版自由判胜诉，方向勿写反 |
| 政治线 | 访苏（1938）、《The Atom Station》、美国封禁、和平奖金（1952）、匈牙利事件后幻灭——全部一句客观事实，不评价、不展开 |
| 非婚长女 | María 之母 Málfríður Jónsdóttir 非配偶，关系表不建 spouse；如需呈现只入提示词正文 |
| Sigríður | 二女无维基链接，关系表不收（防无意义 stub） |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Independent People | 独立的人们 | Sjálfstætt fólk，1934–35 两部 |
| Iceland's Bell | 冰岛钟声 | Íslandsklukkan 三部曲 |
| World Light | 世界之光 | Heimsljós 四部曲 |
| The Atom Station | 原子车站 | 讽刺小说，非科幻 |
| Gerpla | 《杰普拉》 | 英译名 The Happy Warriors / Wayward Heroes 两版并存 |
| saga | 萨迦 | 冰岛中世纪散文叙事传统 |
| Gljúfrasteinn | 格尤弗拉斯泰因 | 故居，现政府运营博物馆 |
| Clervaux Abbey | 克莱沃修道院 | 卢森堡本笃会院 |
| Sonning Prize | 松宁奖 | 1969，丹麦 |
| Icelandic spelling system | 自创拼写体系 | 译文中失落，提示词需专页说明 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions
- **匹配理由**：The Flow of Time 的"时间之流"气质匹配其横贯整个 20 世纪（1902–1998）的创作生命与"史诗长卷"母题；由缓至阔的推进匹配从农场少年到诺奖巨匠的叙事弧线。
- **本地路径**：`music_audio/alex-productions/` 下 The Flow of Time 对应 wav → `presentations/20th_century/Halldór_Laxness/TheFlowOfTime.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Halldór_Laxness/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Halldór_Laxness/images.txt` | 肖像/插图 URL 清单（1955 照片 / 1984 Hákonarson 绘像） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_20th_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/Halldór_Laxness.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（The Flow of Time 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `Halldór_Laxness/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=Halldór_Laxness_zh`、`VIDEO_NAME=Halldór_Laxness_zh`
4. ☐ 第 3 步：复制 The Flow of Time.wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2，已完成）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#14324F；确认 XeLaTeX 字体支持 ð/þ）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（冰岛专名拼写；政治线一句带过复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
