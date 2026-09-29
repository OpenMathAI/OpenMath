# 文学家立传提示词（J. M. Coetzee / 约翰·马克斯韦尔·库切）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Maxwell Coetzee（约翰·马克斯韦尔·库切），南非/澳大利亚小说家、随笔作家、翻译家，2003 年诺贝尔文学奖得主（在世，行文用"生于 1940"口径）。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**"局外人的惊人卷入"与南非历史的道德审视**上——以"局外人作家谱系"与双重国籍的迁徙线支撑叙事张力。

---

## 二、背景信息 【人物专属】

- **目标文学家**：John Maxwell Coetzee（1940-02-09 生于开普敦 ~ 在世，享年栏留白）
- **诺奖年份**：2003 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "in innumerable guises portrays the surprising involvement of the outsider"
  > （中译：表彰其以无数种面貌描绘了局外人的惊人卷入）
  > 新闻稿另引 "well-crafted composition, pregnant dialogue and analytical brilliance"（可作补充转述，勿与获奖理由混排）
- **气质关键词**：**局外人的记录者、开普敦的道德审视者、英语帝国的怀疑者**
- **设计母题**：**局外人（the outsider）**——以"一道在版面上始终不落地的孤影/外缘圆环"意象图式，呼应其笔下 David Lurie、magistrate、Elizabeth Costello 等"多副面孔的局外人"谱系（James Meek 的 alter ego 评述）。
- **本地数据源**：`literature/presentations/pages/21st_century/J._M._Coetzee/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/J._M._Coetzee
- **肖像**：第 0 步待下载（2023 年照片，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1940-02-09 生于开普敦（时为南非联邦）~ 在世（2002 年移居澳大利亚，2006-03-06 入籍；居阿德莱德）。
- 国籍：南非 → 澳大利亚（2006 起；yaml 分两条，Australia 注 since 2006）。
- 家庭：父 Zacharias Coetzee（兼职律师/政府雇员，二战从军）；母 Vera（娘家 Wehmeyer，教师）；母系祖父为波兰人 Balcer Dubiel（1844 生于 Czarnylas）——波兰情结终其一生，终于 2022《The Pole》。妻 Philippa Jubber（1963-07-11 约翰内斯堡结婚，1980 离异）；子 Nicolas（1989 年坠楼身亡，年 23）、女 Gisela。伴侣 Dorothy Driver（阿德莱德大学学者，1980 至今——非婚姻，不入 spouse）。弟 David Coetzee（记者，2010 卒）。
- 教育：St. Joseph's College（Rondebosch 天主教学校）；University of Cape Town（英文荣誉 BA 1960、数学荣誉 BA 1961；MA 1963，论文论 Ford Madox Ford）；University of Texas at Austin（1965–1968 就读，1969 获 PhD——博士论文为 Samuel Beckett 英语散文的计算机辅助文体学分析；注意：Fulbright 说为误传，本人否认，注释明载）。
- 关键荣誉：诺贝尔文学奖 2003；Booker Prize 两度（1983《Life & Times of Michael K》/1999《Disgrace》——史上首位两得布克奖）；CNA Literary Award 三度（1977/1980/1983）；Jerusalem Prize 1987；James Tait Black + Geoffrey Faber（《Waiting for the Barbarians》）；The Irish Times International Fiction Prize 1995（《The Master of Petersburg》）；Commonwealth Writers' Prize 两度（1995/2000）；Prix Femina étranger；Lannan 1998；Order of Mapungubwe (gold) 2005；美国哲学会会员 2006；Companion of the Order of Australia 2025-06-09；FRSL 1988。
- 核心作品与贡献（4–6 条）：
  1. 《Dusklands》（1974，处女作，于 Buffalo 任教期间动笔）；
  2. 《Waiting for the Barbarians》（1980）——magistrate 形象（alter ego 型）；
  3. 《Life & Times of Michael K》（1983，首度布克奖）；
  4. 《Disgrace》（1999，第二度布克奖）——"自 Disgrace 起，其计划发生转变"（Meek 评：从自然主义叙事转向随笔/论战/回忆的复合体）；
  5. 自传性虚构三部：《Boyhood》（1997）、《Youth》（2002）、《Summertime》（2009，布克长/短名单）；
  6. "耶稣三部曲"（《The Childhood of Jesus》2013 /《The Schooldays of Jesus》2016 /《The Death of Jesus》2019）与《The Pole and Other Stories》（2023）；2009 年后未再写以南非为背景的长篇。
- 关键时间线（15–20 节点）：
  1. 1940-02-09 生于开普敦；8 岁随家迁伍斯特（父失公职）；
  2. St. Joseph's College 天主教会学校；家中说英语、对亲属说南非荷兰语；
  3. 1960/1961 UCT 英文、数学双荣誉 BA；
  4. 1962–1965 赴英：IBM 伦敦与 ICT Bracknell 当程序员（后写进《Youth》）；
  5. 1963 UCT MA（Ford Madox Ford 论文）；与 Philippa Jubber 约翰内斯堡结婚；
  6. 1965–1968 UT Austin（书目学/古英语课程；为语言学家 Archibald A. Hill 作 Nama/Malay/Dutch 形态学论文）；
  7. 1969 UT Austin PhD（Beckett 文体学博士论文）；
  8. 1968–1971 SUNY Buffalo 英文系任教，动笔《Dusklands》；1970-03 参与占领 Hayes Hall 被捕（45 名教员之一，1971 撤诉）；因反越战活动等未能取得美国永久居留；
  9. 1972 返南非，任 UCT 英文系讲师；
  10. 1974 《Dusklands》出版——此后约每三年一部长篇；
  11. 1977 《In the Heart of the Country》（CNA 奖）；1980 《Waiting for the Barbarians》；
  12. 1983 《Life & Times of Michael K》获布克奖；1984 任 UCT General Literature 教授；
  13. 1986 《Foe》；1987 耶路撒冷奖——"南非文学是被缚的文学"演说；
  14. 1990 《Age of Iron》；1994 《The Master of Petersburg》+ Arderne 讲席教授；1995《The Irish Times》国际小说奖 + 英联邦作家奖（非洲区）；
  15. 1997 《Boyhood》（虚构化回忆录第一部）；1999 《Disgrace》获第二度布克奖 + 英联邦作家奖（伊丽莎白二世白金汉宫颁）；
  16. 2002 退休（UCT 荣休）并移居澳大利亚阿德莱德；出版《Youth》；
  17. 2003-10-02 诺贝尔文学奖宣布（第四位非洲作家、Gordimer 之后第二位南非得主）；2003-12-10 斯德哥尔摩授奖；
  18. 2004 Voiceless 动物保护组织赞助人（动物伦理转向；素食者）；2005 Mapungubwe 金级勋章；
  19. 2006-03-06 入籍澳大利亚；当选美国哲学会会员；芝加哥大学社会思想委员会任教至 2003（与 UCT 并行）；
  20. 2013–2019 "耶稣三部曲"；2015–2018 阿根廷 San Martín 国立大学"南方文学"双年研讨班主任；2022/2023《The Pole》（西语先行）；2025-06-09 Companion of the Order of Australia。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | novel | 小说 | 布克两度；"局外人"母题贯穿 | 核心页 |
| 1 | South African literature | 南非文学 | 种族隔离时代的道德审视（耶路撒冷奖演说为明载锚点） | 南非页 |
| 2 | autobiographical fiction | 自传性虚构 | Boyhood / Youth / Summertime 三部曲 | 回忆录页 |
| 3 | literary criticism | 文学批评 | 随笔与批评、Tanner Lectures（《The Lives of Animals》） | 批评页 |
| 4 | literary translation | 文学翻译 | 自荷兰语与南非荷兰语译出；El Hilo de Ariadna 丛书策展 | 翻译页 |

#### 4.1 入库操作

- 新建/复用 `people` 记录（name_en 用 page.md frontmatter `John Maxwell Coetzee`，qid=Q43293；先 SELECT 查库内是否已有该 QID stub，**复用勿新建**），`primary_occupation='writer'`、`has_social_data=1`、`has_biography: false`
- occupations：writer(0)、novelist(1)、translator(2)
- 5 个领域写入 `person_field`（South African literature 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。Dorothy Driver 为非婚伴侣（沿用"Gatina Kuznetsova 恋情不入库"先例），仅提示词呈现；Rilke/Borges/Joyce/Eliot/Pound/Herbert 仅为其列举的"局外人谱系"，无直接互动，不入库；Beckett/Ford 为其学位论文对象，属明载学术关联，入 influence。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Philippa Jubber | 无向 | 前妻（1963 结婚，1980 离异） |
| parent-child | Zacharias Coetzee | 对方→本人 | 父，兼职律师与政府雇员 |
| parent-child | Vera Coetzee | 对方→本人 | 母，教师（娘家 Wehmeyer） |
| parent-child | Nicolas Coetzee | 本人→对方 | 子（1989 年坠楼身亡，年 23） |
| parent-child | Gisela Coetzee | 本人→对方 | 女 |
| influence | Samuel Beckett | 对方→本人 | 博士论文对象（英语散文计算机辅助文体分析）；后策展其 Watt |
| influence | Ford Madox Ford | 对方→本人 | UCT 硕士论文对象 |
| colleague | Nadine Gordimer | 无向 | 南非文学前辈（1991 文学诺奖得主）；曾评其对政治方案的整体拒斥 |
| colleague | André Brink | 无向 | 与其同列阿非利卡语文学反种族隔离前列（Fred Pfeil 评述） |
| colleague | Breyten Breytenbach | 无向 | 与其同列阿非利卡语文学反种族隔离前列（Fred Pfeil 评述） |
| colleague | Archibald A. Hill | 无向 | UT Austin 语言学家，为其作 Nama/Malay/Dutch 形态学研究 |
| colleague | John Banville | 无向 | 动物实验议题上的同道（其提请下致函 The Irish Times 反对 TCD 活体解剖） |
| controversy | Thabo Mbeki | 无向 | 移澳时以治安批评南非政府引发交锋（Mbeki 引《Disgrace》回击）；2003 诺奖时 Mbeki 又代表国家祝贺 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#0E4D64`（深青——好望角的冷海与道德审视的克制）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeNovel 靛蓝 `#4C5FD5`；badgeSA 青绿 `#0E7C7B`；badgeMemoir 琥珀 `#E07B30`；badgeAnimals 玫瑰 `#C4204F`
- **背景母题**：外缘圆环（画面主体留白、一道不闭合的环线偏于一侧，呼应"局外人"）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 局外人的卷入 / J. M. Coetzee 生于 1940 + badge + 右上头像 + 国籍行（South Africa → Australia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/婚史与伴侣/双重教职/荣誉/核心领域）
03  核心创作概览 — 小说 / 南非审视 / 自传性虚构 / 批评与翻译
04  早年：开普敦与伍斯特 (1940–1961)【意象图式：双语家庭】
05  伦敦程序员与德克萨斯博士 (1962–1971)——IBM/ICT + Beckett 论文 + Buffalo
06  回到开普敦 (1972–1986)【书影：Dusklands → Foe】
07  布克双奖 (1983 / 1999)【书影：Michael K / Disgrace】
08  耶路撒冷奖演说 (1987)【引文框："literature in bondage"，page.md 有英文原文】
09  自传性虚构三部曲 (1997–2009)【书影：Boyhood / Summertime】
10  阿德莱德与诺贝尔奖 (2002–2003)【引文框：官方获奖理由 EN+中译】
11  晚近：南方文学与动物伦理 (2013–2025)——耶稣三部曲、The Pole、Voiceless
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；外缘环线用 tikz 简单弧线，勿复杂化；身份页 `\profileslide`。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 姓名规范 | 全名 John Maxwell Coetzee（frontmatter），笔名口径 J. M. Coetzee；yaml name_en 用库内既有形式（先查 Q43293） |
| 在世口径 | 在世——生卒页写"生于 1940"，享年栏留白；2025-06-09 Companion of the Order of Australia 勿漏 |
| 布克双奖 | 史上首位两得布克奖（1983/1999）；Summertime 仅短名单勿写成获奖；后达成者 Peter Carey/Hilary Mantel/Margaret Atwood |
| Fulbright 误传 | "Fulbright 学者"说法被 page.md 注释明确证伪（本人否认+名录核查），禁写 |
| 博士论文 | 对象是 Beckett 英语散文的**计算机辅助**文体分析（1969）；Nama/Malay/Dutch 形态学论文只是为 Hill 而作，勿混为博士论文 |
| 政治红线 | 2016 巴勒斯坦文学节演说与 2026 拒绝耶路撒冷作家节事件涉及持续冲突，**本篇回避不写**；反种族隔离立场（1987 耶路撒冷奖演说 "literature in bondage"）为 page.md 明载的文学史事实可写；TRC 评论、ANC 批评《Disgrace》、Mbeki 交锋各一句客观转述，不评价不展开 |
| 婚恋表述 | Philippa Jubber 是前妻；Dorothy Driver 是 1980 年起的伴侣（非婚姻）——两者勿混写，Driver 不入 spouse |
| 丧子 | Nicolas 1989 年约翰内斯堡寓所阳台坠楼身亡（意外，年 23）——客观一句，勿渲染 |
| 引语红线 | "literature in bondage" 段落 page.md 有英文原文可引；Rian Malan "monkish self-discipline" 是其 1999 转述（附本人否认回信），引用必须带归属 |
| 南方文学 | Literatures of the South=2015–2018 San Martín 国立大学研讨班；El Hilo de Ariadna 丛书策展（Tolstoy/Beckett/Patrick White）——是"策展/总监"事实，勿写成出版人 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| the outsider | 局外人 | 官方获奖理由关键词，勿改写 |
| Dusklands | 昏暗之地 | 1974 处女作，勿意译成"暮色国度" |
| Waiting for the Barbarians | 等待野蛮人 | 1980 |
| Life & Times of Michael K | 迈克尔·K的生活和时代 | 1983，首布克 |
| Disgrace | 耻 | 1999，二布克；勿译"耻辱"定名 |
| Boyhood / Youth / Summertime | 童年/青春/夏日 | 自传性虚构三部曲 |
| apartheid | 种族隔离 | 历史制度名词，客观使用 |
| literatures of the South | 南方文学 | 2015–2018 研讨班项目 |
| The Lives of Animals | 动物的生命 | 1999，Tanner Lectures |
| Order of Mapungubwe | 马普冈布韦勋章 | 2005 金级，南非国家荣誉 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions
- **匹配理由**："历史感/深沉"匹配其以历史创伤与记忆为底色的写作（殖民史、种族隔离史、自传史）；PAST 的克制质感匹配其寡言回避公众的形象与"道德审视者"气质。
- **本地路径**：`music_audio/alex-productions/` 下 PAST 对应 wav → `presentations/21st_century/J._M._Coetzee/PAST.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/J._M._Coetzee/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/21st_century/J._M._Coetzee/images.txt` | 肖像/插图 URL 清单 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_21st_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/J._M._Coetzee.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（PAST 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox 2023 年照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `J._M._Coetzee/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=J._M._Coetzee_zh`、`VIDEO_NAME=J._M._Coetzee_zh`
4. ☐ 第 3 步：复制 PAST wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#0E4D64）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写；引语归属复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
