# 文学家立传提示词（Harold Pinter / 哈罗德·品特）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Harold Pinter（哈罗德·品特），英国剧作家/编剧/演员/导演，2005 年诺贝尔文学奖得主；"Pinteresque" 已进入英语词典的剧作家。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**"威胁喜剧→记忆戏剧→政治戏剧"三段式与"日常闲谈之下的深渊"**上——以停顿与沉默的戏剧张力支撑版面。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Harold Pinter（1930-10-10 ~ 2008-12-24，享年 78 岁）
- **诺奖年份**：2005 年诺贝尔文学奖，官方获奖理由（EN 原文，取自 `nobel_literature_citations.json`，禁止改写；尾部引号噪声须清理）：
  > "who in his plays uncovers the precipice under everyday prattle and forces entry into oppression's closed rooms"
  > （中译：表彰其戏剧揭开日常闲谈之下的深渊，强行闯入压迫的封闭房间）
- **气质关键词**：**威胁喜剧的锻造者、沉默与停顿的大师、晚年的政治良心**
- **设计母题**：**封闭的房间（the closed room）**——以"一扇半开的门与强光切入的暗室"意象图式，呼应其从《The Room》到《One for the Road》的"房间—闯入者—权力"母题。
- **本地数据源**：`literature/presentations/pages/21st_century/Harold_Pinter/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Harold_Pinter
- **肖像**：第 0 步待下载（1962 年照片，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1930-10-10 生于伦敦东部哈克尼 ~ 2008-12-24（圣诞前夜）逝于伦敦哈默史密斯医院（肝癌），享年 78 岁；2001-12 确诊食道癌（手术+化疗后继续工作）；2005 起患天疱疮与败血症并发症。葬礼 2008-12-31 Kensal Green Cemetery 墓边世俗仪式（自选八篇诵读：本人作品七段+乔伊斯《The Dead》，Antonia Fraser 引《哈姆雷特》"晚安，亲爱的王子"作结）。
- 国籍：英国。
- 家庭：东欧犹太移民家庭的独子——父 Hyman "Jack" Pinter（女装裁缝）、母 Frances（娘家 Moskowitz，家庭主妇）；"塞法迪与宗教裁判所传说"为讹传（Antonia Fraser 考证：三位祖辈来自波兰、一位来自敖德萨，阿什肯纳兹犹太人——早年笔名 Pinta/da Pinto 由此而来）。子 Daniel（1958 生；后改姓母系外祖母婚前姓 Brand，与父疏离，未出席葬礼——客观一句，勿渲染）。
- 婚姻：Vivien Merchant（演员，《Alfie》主演，1956 结婚，1975 分居、1980 离异，1982 死于急性酒精中毒，年 53）；Lady Antonia Fraser（1969 三人合作为国家美术馆玛丽女王节目共事相识；1975-01-08/09 相恋，1980-11-27 结婚——"33 年，直到终老"）；与 BBC 主持人 Joan Bakewell 的隐秘恋情（1962–1969）为《Betrayal》(1978) 灵感来源（非婚姻，不入 spouse）。六名继子女、17 名继孙。
- 教育：Hackney Downs School（1944–1948，短跑纪录保持者、板球痴迷者、英语教师 Joseph Brearley 主持其主演《罗密欧》1947《麦克白》1948）；RADA 两学期辍学（1949）；Central School of Speech and Drama（1951 年 1–7 月）；拒服兵役的良心拒服兵役者（两次被起诉并罚款，CO 登记最终获准）。
- 关键荣誉：诺贝尔文学奖 2005；Georg Büchner 系以外的 Avrupa 奖项略——核心：CBE 1966；Companion of Honour 2002（1996 拒绝骑士爵位）；David Cohen Prize 1995；Laurence Olivier Special Award 1996；BAFTA Fellowship 1997；Europe Theatre Prize 2006；Légion d'honneur 2007（法国总理 de Villepin 授勋， praising 其诗《American Football》）；Franz Kafka Prize；Wilfred Owen Award for Poetry（授奖演说 2007-03-18，page.md 有英文原句）；Tony Award for Best Play 1967（《The Homecoming》）+ 全剧共获四项托尼；Evening Standard Award 1960（《The Caretaker》）；2013 塞尔维亚 Sretenje Order（身后）。
- 核心作品与贡献（4–6 条）：
  1. 《The Room》（1957，三天写就，Bristol 大学学生制作、挚友 Henry Woolf 导演并首演 Mr. Kidd）——剧作生涯起点；
  2. 《The Birthday Party》（1957 写/1958 演，八场即停——Harold Hobson《Sunday Times》书评力挽狂澜："Make a note of their names"）；《The Dumb Waiter》（1959）；《The Caretaker》（1960，444 场，确立声誉）；
  3. 《The Homecoming》（1964）——百老汇四项托尼、1967 最佳戏剧托尼；
  4. "记忆戏剧"系列：《Landscape》（1968）/《Old Times》（1971）/《No Man's Land》（1975）/《Betrayal》（1978）/《A Kind of Alaska》（1982）；
  5. "公开的政治戏剧"：《One for the Road》（1984）/《Mountain Language》（1988，源于 1985 与 Arthur Miller 赴土耳其调查被囚作家受刑的经历与库尔德语禁令）/《Party Time》（1991）/《Ashes to Ashes》（1996）；最后一部舞台剧《Celebration》（2000）；
  6. 编剧 27 部：Losey 三部曲《The Servant》（1963）/《Accident》（1967）/《The Go-Between》（1971），《The French Lieutenant's Woman》（1981，奥斯卡提名）与《Betrayal》（1983，奥斯卡提名），《The Trial》（1993），收官之作《Sleuth》（2007，Jude Law 委约）；29 部剧作+15 部戏剧小品。
- 关键时间线（15–20 节点）：
  1. 1930-10-10 生于哈克尼犹太裁缝家庭；
  2. 1940–41 大轰炸中疏散康沃尔与雷丁——"孤独、困惑、分离与丧失"成为终身母题（Billington）；
  3. 12 岁开始写诗；1947 校刊首发；1950《Poetry London》刊出（笔名 Harold Pinta）；
  4. 1944–48 Hackney Downs：板球/短跑/Brearley 的文学散步；
  5. 1948 拒服兵役（冷战与麦卡锡主义刺激，1985 自述可引）；1949 RADA 辍学；
  6. 1949–50 Chesterfield 哑剧小角色；1951 Central School；
  7. 1951–52 Anew McMaster 剧团爱尔兰巡演（十余角色）；1953–54 Donald Wolfit 剧团；
  8. 1954–1959 以艺名 David Baron 演出 20+ 角色；兼职侍者/邮差/保镖/铲雪工；
  9. 1956 与 Vivien Merchant 结婚；1958 子 Daniel 生；
  10. 1957 《The Room》（Woolf 导演，Bristol）；1958 《The Birthday Party》八场即停 + Hobson 书评；
  11. 1959–60 《The Dumb Waiter》德国首演；《The Caretaker》Arts Theatre Club → Duchess 剧院 444 场 + Evening Standard Award；
  12. 1963 首部电影编剧《The Servant》（Losey）；1966 CBE；
  13. 1964 《The Homecoming》；1967 百老汇四托尼——成名剧作家；
  14. 1971–1978 "记忆戏剧"成熟期（Old Times / No Man's Land / Betrayal）；1973 任 National Theatre 副艺术总监；
  15. 1975-01 与 Fraser 相恋；1975-03-21 对 Merchant 说 "I've met somebody"；1975-04-28 搬出（No Man's Land 首演五天后）；1980-11-27 结婚；
  16. 1980 重写并亲自导演 1958 年搁置的《The Hothouse》（Hampstead）；1982 Merchant 去世；
  17. 1984《One for the Road》起"公开政治戏剧"阶段（Mountain Language 1988 ← 1985 土耳其 PEN 之行）；
  18. 2001-12 确诊食道癌；2002 手术+化疗；2002 Companion of Honour；2004 Kafka Prize + Wilfred Owen Award；
  19. 2005-10-10 75 岁生日广播《Voices》；10-13 诺贝尔文学奖宣布；同年宣布停写剧作（"I think I've written 29 plays. I think it's enough for me…"）转向诗歌与政治；
  20. 2006 皇家宫廷剧院 50 周年演 Beckett《Krapp's Last Tape》主角（轮椅演出九场满座）；2006 Europe Theatre Prize；2007 荣誉军团勋章；2008-10 出任 Central School 校长（第 20 个荣誉学位，未到场合）；2008-12-24 卒。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | comedy of menace | 威胁喜剧 | 早期标签（Wardle 1958 借自 Campton 副题）；《The Birthday Party》《The Caretaker》 | 核心页 |
| 1 | memory play | 记忆戏剧 | 中期系列（Landscape→Betrayal） | 记忆页 |
| 2 | political theatre | 政治戏剧 | One for the Road / Mountain Language / Party Time（权力与压迫的直写） | 政治页 |
| 3 | screenwriting | 电影编剧 | Losey 三部曲、两度奥斯卡提名、Sleuth 收官 | 编剧页 |
| 4 | poetry | 诗歌 | 12 岁起笔、晚年回归（War 2003、Six Poems for A.） | 诗歌页 |

#### 4.1 入库操作

- 新建/复用 `people` 记录（name_en 用 page.md frontmatter `Harold Pinter`，qid=Q41042；先 SELECT 查库内是否已有该 QID stub，**复用勿新建**），`primary_occupation='writer'`、`has_social_data=1`、`has_biography: false`
- occupations：writer(0)、playwright(1)、screenwriter(2)
- 5 个领域写入 `person_field`（comedy of menace 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。Joan Bakewell 为隐秘恋情（非婚姻，沿用先例不入库）；Blair/Bush 仅为其单向政治言论对象，不建关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Vivien Merchant | 无向 | 第一任妻子（1956–1980），演员，多次出演其剧作 |
| spouse | Antonia Fraser | 无向 | 第二任妻子（1980–2008），传记作家；考证其家族为阿什肯纳兹 |
| parent-child | Hyman Pinter | 对方→本人 | 父（Hyman "Jack"），女装裁缝 |
| parent-child | Frances Moskowitz | 对方→本人 | 母，家庭主妇 |
| parent-child | Daniel Brand | 本人→对方 | 子（1958 生，后改姓 Brand，与父疏离） |
| influence | Samuel Beckett | 对方→本人 | 其自认的早期影响者；两人互寄草稿切磋的挚友 |
| influence | Joseph Brearley | 对方→本人 | Hackney Downs 英语教师，主持其校园演剧（"a major influence"） |
| colleague | Henry Woolf | 无向 | 挚友，《The Room》导演并首演 Mr. Kidd |
| colleague | Harold Hobson | 无向 | 《Sunday Times》剧评人，其书评救活《The Birthday Party》 |
| colleague | Joseph Losey | 无向 | 三部合作电影（The Servant / Accident / The Go-Between）的挚友导演 |
| colleague | Arthur Miller | 无向 | 1985 同赴土耳其 PEN 调查被囚作家受刑（Helsinki Watch 合办） |
| colleague | Simon Gray | 无向 | 其执导 Gray 剧作达 10 部（含 Butley） |
| colleague | Michael Billington | 无向 | 官方传记作者，多年访谈与合作 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#0F4C5C`（深青蓝——伦敦东区的冷雾与舞台顶光的暗角）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeMenace 靛蓝 `#4C5FD5`；badgeMemory 青绿 `#0E7C7B`；badgePolitical 琥珀 `#E07B30`；badgeScreen 玫瑰 `#C4204F`
- **背景母题**：半开的门与强光切入的暗室（tikz 简单矩形+门缝光带，呼应"压迫的封闭房间"）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 日常闲谈之下的深渊 / Harold Pinter 1930–2008 + badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/两任妻子/艺名 David Baron/荣誉/核心领域）
03  核心创作概览 — 威胁喜剧 / 记忆戏剧 / 政治戏剧 / 编剧
04  哈克尼少年 (1930–1950)——大轰炸疏散、Brearley、板球与诗歌【引文框：Hobson 书评可选】
05  David Baron 岁月 (1951–1959)——爱尔兰/英国巡演与打零工【意象图式】
06  《The Room》与《The Birthday Party》(1957–1960)【书影：The Birthday Party】
07  《The Caretaker》与《The Homecoming》(1960–1967)【书影+引文框：四托尼】
08  记忆戏剧 (1968–1982)【书影：Betrayal / No Man's Land】
09  政治戏剧 (1984–2000)【引文框：官方获奖理由 EN+中译】
10  诺贝尔奖与晚年 (2005–2008)——停写剧作声明、Krapp's Last Tape、校长任命
11  遗产——PEN Pinter Prize (2009)、Harold Pinter Theatre (2011)、身后致意
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；门缝光带图式用 tikz 矩形+细亮条，勿复杂化；身份页 `\profileslide`。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 月份日期 | 生 1930-10-10、卒 2008-12-24（圣诞前夜）；宣布诺奖 2005-10-13（75 岁生日广播三天后）——三组日期勿混 |
| Pinteresque | 该词"已进入英语"（page.md 明载），但 Pinter 本人厌恶此词、认为无意义——引用须带此反注 |
| 威胁喜剧出处 | 标签借自 David Campton《The Lunatic View》副题（Irving Wardle 1958），勿写成评论界凭空发明 |
| 家族渊源 | 塞法迪/宗教裁判所传说是错的（Fraser 考证为阿什肯纳兹：波兰×3+敖德萨×1）——可写为"早年自误信"对照，勿写成正史 |
| 政治红线 | 反战立场与对伊拉克战争等的批评**只按 page.md 客观转述其言论存在**（"bandit act... state terrorism" 引文有英文原文，须带 2007-03-18 Wilfred Owen 演说归属），不评价、不站队；ICDSM/Milošević 事件、中东相关联署（2005–2008）**回避不展开**；被批"叛国"式指控只写"被联盟支持者指责"的存在（若有），不引申 |
| 私生活 | Joan Bakewell 恋情（1962–69）与《Betrayal》的灵感关联为 page.md 明载，一句客观即可；"Cleopatra" 绰号可提可不提；Merchant 死因"急性酒精中毒"客观一句 |
| Hobson 书评 | "Make a note of their names" 等引文 page.md 有英文原文，可引；注明"剧终后才刊出、未能救场"的语境 |
| 编剧冷知识 | 《The Handmaid's Tale》《The Remains of the Day》《Lolita》为未署名/未出版剧本（page.md 明载），勿写成"未参与" |
| 29 部剧作 | 29 部剧+15 部小品+2 部合著——"29"是他 2005 停笔声明中的数字，勿与总创作数混算 |
| 无载禁写 | 与 Beckett 的关系止于"影响+互寄草稿+演出其作品"；勿编造师承或合著戏剧 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Pinteresque | 品特式的 | 进入英语的形容词；本人厌恶此词 |
| comedy of menace | 威胁喜剧 | 早期作品标签 |
| memory play | 记忆戏剧 | 中期系列标签 |
| The Birthday Party | 生日晚会 | 1957/1958；勿译"生日聚会"定名 |
| The Caretaker | 看管人 | 1960；444 场 |
| The Homecoming | 归家 | 1964；四托尼 |
| Betrayal | 背叛 | 1978；逆向时序叙事 |
| Mountain Language | 山里的语言 | 1988；库尔德语禁令背景 |
| conscientious objector | 良心拒服兵役者 | 1948 事件关键词 |
| David Baron | 艺名大卫·巴伦 | 1954–1959 演员艺名 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions
- **匹配理由**：Awaken 的"警醒/张力"质感匹配其从暗室威胁到晚年政治呐喊的觉醒弧线；停顿—爆发交替的戏剧节奏与曲目的起伏同构；契合"强行闯入压迫的封闭房间"的破门意象。
- **本地路径**：`music_audio/alex-productions/` 下 Awaken 对应 wav → `presentations/21st_century/Harold_Pinter/Awaken.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Harold_Pinter/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/21st_century/Harold_Pinter/images.txt` | 肖像/插图 URL 清单 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_21st_century_list.py` + `literature/nobel_literature_citations.json` | 获奖理由 EN 原文+中译（禁止改写脚本） |
| `MySQL/data/Harold_Pinter.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（Awaken 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox 1962 年照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `Harold_Pinter/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=Harold_Pinter_zh`、`VIDEO_NAME=Harold_Pinter_zh`
4. ☐ 第 3 步：复制 Awaken wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#0F4C5C）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/剧名拼写；引语归属复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
