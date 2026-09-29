# 文学家立传提示词（Imre Kertész / 伊姆雷·凯尔泰斯）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Imre Kertész（伊姆雷·凯尔泰斯），匈牙利小说家/翻译家，2002 年诺贝尔文学奖得主（首位匈牙利籍文学奖得主），奥斯维辛与布痕瓦尔德幸存者。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**"大屠杀作为文化"的书写与个体经验对历史野蛮性的抵抗**上——以集中营的"幸存"与流亡柏林的"无家"支撑叙事张力。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Imre Kertész（1929-11-09 ~ 2016-03-31，享年 86 岁）
- **诺奖年份**：2002 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for writing that upholds the fragile experience of the individual against the barbaric arbitrariness of history"
  > （中译：表彰其写作在历史的野蛮专断面前，维护了个体脆弱的经验）
- **气质关键词**：**大屠杀记忆的守夜人、极权下的个体书写者、无命运命运的命名者**
- **设计母题**：**命运lessness（无命运）**——以"一条被抹去终点的列车线：布达佩斯 → 奥斯维辛 → 布痕瓦尔德 → 泽茨 → 布达佩斯 → 柏林"的意象图式，呼应《无命运的人生》中"以平常语气叙述非常之事"的美学。
- **本地数据源**：`literature/presentations/pages/21st_century/Imre_Kertész/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Imre_Kert%C3%A9sz
- **肖像**：第 0 步待下载（Oliver Mark 摄，柏林 2005，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1929-11-09 生于布达佩斯 ~ 2016-03-31 逝于布达佩斯家中，享年 86 岁。
- 国籍：匈牙利 → 德国（常居柏林；yaml 按 page.md 口径分两条）。
- 家庭：犹太中产家庭，父 László Kertész、母 Aranka Jakab；约 5 岁时父母分居，入寄宿学校。两任妻子：Albina Vas（卒于 1995）、Magda Ambrus（1996 结婚，卒于 2016）。
- 教育：Madách Imre High School（1948 年毕业）；1940 年入中学时被编入犹太学生特别班。
- 集中营经历：1944 年 14 岁被驱逐至奥斯维辛（自报 16 岁工人躲过立即灭绝），后转布痕瓦尔德；1945 年获释返布达佩斯。
- 关键荣誉：诺贝尔文学奖 2002；Kossuth Prize 1997；Herder Prize 2000；Pour le Mérite 2001；Goethe Medal 2004；Milán Füst Prize 1983；Jean Améry Prize 2009；匈牙利圣斯蒂芬勋章 2014；布达佩斯荣誉市民 2002；柏林艺术科学院遗赠。
- 核心作品与贡献（4–6 条）：
  1. 《Fatelessness / Sorstalanság》（1975）——15 岁的 György Köves 在奥斯维辛/布痕瓦尔德/泽茨的经历；1969–1973 写成、遭共产主义政权出版拒绝；今为匈牙利中学课程书目；2005 年改编电影（他本人编剧）；
  2. 《Fiasco / A kudarc》（1988）与《Kaddish for an Unborn Child / Kaddis a meg nem született gyermekért》（1990）——"大屠杀三部曲"第二、三部；
  3. 《Liquidation / Felszámolás》（2003）——匈牙利从共产主义向民主转型时期；主人公自杀（他本人与抑郁缠斗的文学转化）；
  4. 其他虚构：《The Pathseeker》（1977）、《Detective Story》（1977）、《The Union Jack》（1991）、《Dossier K》（2006，自传体档案）；
  5. 非虚构/日记：《Gályanapló》（1992，划桨日记）、《A holocaust mint kultúra》（1993，"作为文化的大屠杀"三讲）、《A száműzött nyelv》（2001，被放逐的语言）；
  6. 翻译家：自德语译入匈牙利语——尼采《悲剧的诞生》、维特根斯坦思想残篇、弗洛伊德、卡内蒂，以及 Dürrenmatt、Schnitzler、Tankred Dorst 剧作。
- 关键时间线（15–20 节点）：
  1. 1929-11-09 生于布达佩斯犹太中产家庭；
  2. 约 1934 父母分居，入寄宿学校；
  3. 1940 入中学，被编入犹太学生特别班；
  4. 1944（14 岁）与匈牙利犹太人一同被驱逐至奥斯维辛，自报 16 岁工人躲过立即灭绝；
  5. 1944–45 转布痕瓦尔德；1945 获释返布达佩斯；
  6. 1948 高中毕业；当记者、翻译；
  7. 1951《Világosság》改奉共产党路线，失业；短暂做工人工人，后入重工业部新闻处；
  8. 1953 起自由撰稿 + 翻译（尼采/弗洛伊德/维特根斯坦/卡内蒂）；
  9. 1969–1973 写《Fatelessness》（Sorstalanság）；
  10. 1975 《Fatelessness》出版（此前遭拒）——在匈国内长期无人问津；
  11. 1983 Milán Füst Prize；
  12. 1988 《Fiasco》出版（三部曲之二）；
  13. 1990 《Kaddish for an Unborn Child》（三部曲之三）；同年迁居德国——在德国获得出版界与评论界更积极的接纳；
  14. 1992/1995 Soros Prize；1995 Brandenburg Literature Prize；1996 娶 Magda Ambrus；
  15. 1997 Kossuth Prize；2000 Herder Prize + Welt-Literaturpreis；
  16. 2001 Pour le Mérite；2002 诺贝尔文学奖（首位匈牙利籍文学奖得主）+ 布达佩斯荣誉市民；
  17. 2003 《Liquidation》；2004 Goethe Medal；2005 电影《Fateless》上映（本人编剧）；
  18. 2009 Die Welt 访谈自称"Berliner"、称布达佩斯"完全巴尔干化"——匈国内舆论风波；后于 Duna TV 澄清"建设性"、匈牙利仍是"他的祖国"；同年 Jean Améry Prize；
  19. 2013 摔伤致右髋手术；确诊帕金森病；抑郁复发；
  20. 2014 匈牙利圣斯蒂芬勋章；2016-03-31 卒于布达佩斯家中；遗赠留给柏林艺术科学院。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Holocaust literature | 大屠杀文学 | "大屠杀三部曲"；官方理由"个体经验对历史野蛮性"核心 | 核心页 |
| 1 | novel | 小说 | 《Fatelessness》《Fiasco》《Liquidation》 | 小说页 |
| 2 | literary translation | 文学翻译 | 尼采/维特根斯坦/弗洛伊德/卡内蒂及德语戏剧译入匈语 | 翻译页 |
| 3 | autobiographical fiction | 自传性虚构 | 《Fatelessness》常被作准自传解读，但本人否认强传记关联 | 核心页 |
| 4 | journal writing | 日记/讲稿写作 | 《Gályanapló》划桨日记、"作为文化的大屠杀"三讲 | 日记页 |

#### 4.1 入库操作

- 新建/复用 `people` 记录（name_en 用 page.md frontmatter `Imre Kertész`，qid=Q47755；先 SELECT 查库内是否已有该 QID stub，**复用勿新建**），`primary_occupation='writer'`、`has_social_data=1`、`has_biography: false`
- occupations：writer(0)、novelist(1)、translator(2)
- 5 个领域写入 `person_field`（Holocaust literature 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。翻译对象哲学家（尼采/维特根斯坦）与英译者 Tim Wilkinson 均为 page.md 明载的职业互动，入 influence/colleague；Spielberg 争议入 controversy。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Albina Vas | 无向 | 第一任妻子（卒于 1995） |
| spouse | Magda Ambrus | 无向 | 第二任妻子（1996 结婚，卒于 2016） |
| parent-child | László Kertész | 对方→本人 | 父 |
| parent-child | Aranka Jakab | 对方→本人 | 母 |
| influence | Friedrich Nietzsche | 对方→本人 | 曾译《悲剧的诞生》入匈牙利文 |
| influence | Ludwig Wittgenstein | 对方→本人 | 曾译其思想残篇入匈牙利文 |
| influence | Sigmund Freud | 对方→本人 | 曾译其著作入匈牙利文 |
| colleague | Elias Canetti | 无向 | 曾译其著作入匈牙利文（1981 文学诺奖得主） |
| colleague | Tim Wilkinson | 无向 | 其多部作品的英译者（Fatelessness/Kaddish/Liquidation 等） |
| controversy | Steven Spielberg | 无向 | 批评《辛德勒的名单》对大屠杀的表现为 kitsch（page.md 明载引语） |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#1E4E79`（莫尼黑蓝——多瑙河的冷与集中营记忆的灰）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeHolocaust 靛蓝 `#4C5FD5`；badgeNovel 青绿 `#0E7C7B`；badgeTranslation 琥珀 `#E07B30`；badgeExile 玫瑰 `#C4204F`
- **背景母题**：被抹去终点的列车线（一条细线穿过版面，中段断裂，呼应"无命运"）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 无命运的命运 / Imre Kertész 1929–2016 + badge + 右上头像 + 国籍行（Hungary → Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/两任妻子/集中营经历/荣誉/核心领域）
03  核心创作概览 — 大屠杀文学 / 三部曲 / 翻译家 / 日记与讲稿
04  早年：布达佩斯犹太少年 (1929–1944)
05  奥斯维辛与布痕瓦尔德 (1944–1945)【意象图式：自报 16 岁】
06  极权下的新闻与翻译 (1948–1973)——Világosság 失业 → 自由撰稿
07  《无命运的人生》(1975)【书影+引文框：写作 1969–1973、出版遭拒】
08  大屠杀三部曲 (1988–1990)【书影：Fiasco / Kaddish】
09  柏林流亡与迟来的认可 (1990–2002)【引文框：官方获奖理由 EN+中译】
10  《清算》与晚年 (2003–2016)——抑郁/帕金森按事实一句陈述；遗赠柏林艺术科学院
11  争议（客观一页）——Die Welt 访谈风波与 Spielberg 批评均按 page.md 客观简述，不评价
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；列车线图式用 tikz 简单折线+断口，勿复杂化；身份页 `\profileslide`。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| "首位"表述 | 首位**匈牙利籍**诺贝尔文学奖得主（page.md 明载 "the first Hungarian to win the Nobel in Literature"），勿写成"首位匈牙利诺奖得主"（物理学/化学等已有） |
| 自传性 | 《Fatelessness》常被解读为准自传，但 page.md 明载 Kertész "disavowed a strong biographical connection"——书名/叙述者 György Köves 与本人经历相似但勿等同 |
| 集中营细节 | 奥斯维辛 → 布痕瓦尔德（→ 泽茨见小说）；自报 16 岁是救命细节（page.md 明载），勿写成"隐瞒年龄未遂" |
| 出版史 | 1969–1973 写作、遭共产主义政权拒绝出版、1975 出版——三个年份勿混 |
| 争议红线 | Die Welt "Balkanized" 风波须同时呈现其 Duna TV 澄清（"建设性"、匈牙利仍是祖国）；匈牙利国内批评只客观转述"hypocritical"标签的存在，**不站队不评价**；2014 NYT 未刊访谈事件同此 |
| Spielberg 引语 | "I regard as kitsch any representation of the Holocaust that is incapable of understanding..."——page.md 有英文原文，可引；须标明是本人原话 |
| 抑郁与死因 | 帕金森病 + 复发性抑郁（page.md 明载其"transform into literature"）；《Liquidation》主人公自杀与本人经历勿混淆；卒于布达佩斯家中，非医院 |
| 两任妻子 | Albina Vas 卒于 1995；Magda Ambrus 1996 结婚、卒于 2016——勿写反 |
| 德语译名 | 他翻译的是 The Birth of Tragedy（尼采）、Dürrenmatt/Schnitzler/Tankred Dorst 剧作——勿写成译自英语 |
| 无载禁写 | 不编造导师/师承；与 Canetti 仅限"翻译其著作"这一明载事实，勿写私人交往 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Fatelessness / Sorstalanság | 无命运的人生（又译非命运性） | 1975；英译 Fateless/Fatelessness 两版并存 |
| Kaddish for an Unborn Child | 给未出生孩子做安魂祈祷 | 1990；Kaddish=犹太祷文 |
| Fiasco | 惨败 | 1988，三部曲之二 |
| Liquidation | 清算 | 2003；Felszámolás |
| Holocaust trilogy | 大屠杀三部曲 | Fatelessness→Fiasco→Kaddish 顺序勿倒 |
| kitsch | 媚俗 | Spielberg 批评引语关键词 |
| Holocaust as culture | 作为文化的大屠杀 | 1993 三讲标题意译 |
| Kaddish | 卡迪什祷文 | 犹太哀祷，勿译成"圣歌" |
| Világosság | 《光明》杂志 | 1951 失业的刊物，勿意译 |
| Duna TV | 多瑙电视台 | 澄清访谈的媒体 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions
- **匹配理由**："沉稳/纪录片/长期纲领"匹配其一生从集中营少年到 73 岁才获世界承认的漫长等待；《Fatelessness》以平静语气承载非常之事，与 Timeless 的克制质感同构；"长期纲领"对应其"大屠杀作为文化"的持续书写。
- **本地路径**：`music_audio/alex-productions/` 下 Timeless 对应 wav → `presentations/21st_century/Imre_Kertész/Timeless.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Imre_Kertész/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/21st_century/Imre_Kertész/images.txt` | 肖像/插图 URL 清单（Oliver Mark 2005） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_21st_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/Imre_Kertész.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（Timeless 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox Oliver Mark 2005 照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `Imre_Kertész/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=Imre_Kertész_zh`、`VIDEO_NAME=Imre_Kertész_zh`
4. ☐ 第 3 步：复制 Timeless wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#1E4E79）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写；引语归属复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
