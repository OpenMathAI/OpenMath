# 文学家立传提示词（OpenLiterature：Nadine Gordimer）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Nadine Gordimer（纳丁·戈迪默），1991 年诺贝尔文学奖得主，南非反种族隔离作家。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对戈迪默，即「矿镇与禁书」：以史诗性写作凝视种族隔离南非的道德与心理张力，以被查禁与解禁的书页记录一个国家的转型；其一生与运动、审查、审判交织，须**双线并陈、客观呈现、不作评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Nadine Gordimer（纳丁·戈迪默，1923–2014），南非小说家、短篇小说家、剧作家、政治活动家；1991 年诺贝尔文学奖得主（首位南非得主、首位非洲女性得主）。
- **设计哲学**：以「矿镇与禁书」为核心叙事——东兰德金矿小镇 Springs 的童年起点，与《保守的人》《七月的人民》里「以保护自然之名冻结变革」的隐喻；书页被查禁/解禁的反复构成其命运的视觉韵律。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Nadine Gordimer（纳丁·戈迪默，1923-11-20 ~ 2014-07-13，享年 90 岁）
- **官方获奖理由（Nobel 1991，禁止改写）**：
  > "who through her magnificent epic writing has — in the words of Alfred Nobel — been of very great benefit to humanity"
  > （表彰其宏伟的史诗性写作，用阿尔弗雷德·诺贝尔的话说——「对人类有莫大裨益」）
- **气质关键词**：**种族隔离的编年史家、短篇小说的信徒、审判席上的证人**
- **设计母题**：**矿镇与禁书（mining town & the banned book）**——约翰内斯堡远郊 Springs 金矿镇的竖井与矿堆构成视觉母题 A；盖着查禁印章的书影构成视觉母题 B；结尾以「路边的长椅」（Bench by the Road 的南非平行意象为 page.md 无载**禁写**，仅用矿镇—禁书双母题）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Nadine_Gordimer/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Nadine_Gordimer
- **肖像**：第 0 步优先用 page.md 内嵌图 2010 年哥德堡书展照片；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1923-11-20 生于约翰内斯堡郊外东兰德矿业小镇 Springs（时属德兰士瓦省，南非联邦）～ 2014-07-13 卒于约翰内斯堡家中（睡梦中辞世），享年 90 岁。英语写作。
- **家世与童年**：犹太父母；父 Isidore Gordimer（1887–1962）是来自沙俄帝国 Žagarė 的立陶宛犹太移民钟表匠，13 岁随家移民；母 Hannah "Nan" Myers Gordimer（1897–1973）是伦敦英国犹太移民，世俗化家庭；父亲非活动家、对黑人处境缺乏同情，母亲关心黑人贫困并创办黑人儿童日托所；少年时警察突袭家中、没收佣人房间信件日记——政府镇压的亲身体验。
- **病中起步**：因母亲「她自己才明白的奇怪理由」（疑似担心她心脏弱）常年居家，13 岁（1937）发表首篇作品——儿童短篇 "The Quest for Seen Gold"（*Children's Sunday Express*）；同期 "Come Again Tomorrow" 刊 *Forum*；16 岁发表首篇成人小说。天主教修女会学校教育背景。
- **大学与 Sophiatown**：在金山大学（University of the Witwatersrand）就读一年，首次跨肤色交往、参与 Sophiatown 文艺复兴；未完成学位；1948 迁约翰内斯堡定居。
- **《纽约客》与首作**：1951 年《纽约客》接受短篇 "A Watcher of the Dead"——长期合作之始；她自认短篇是「我们时代的文学形式」；1949 首部短篇集 *Face to Face*；1953 首部长篇《说谎的日子》（*The Lying Days*，家乡 Springs 半自传成长小说）。
- **行动主义（客观简述）**：1960 年挚友 Bettie du Toit 被捕与沙佩维尔惨案促其投身反种族隔离运动；1962 里沃尼亚审判期间与曼德拉的辩护律师 Bram Fischer、George Bizos 为友，并协助曼德拉修改著名辩词 "I Am Prepared to Die"（1990 曼德拉获释后首先想见的人之一）；在 ANC 仍属非法组织时加入；曾把 ANC 领导人藏匿家中助其逃避逮捕；自述平生最骄傲的一天是 1986 年在德尔马斯叛国罪审判中为 22 名活动人士作证。
- **查禁与解禁**：《 Late Bourgeois World》1976 被禁十年（其首次亲历个人作品被禁）；《陌生人的世界》被禁十二年；《布尔格的女儿》（1979-06 出版）一个月后被禁，上诉委员会三个月后解禁——理由是「过于偏颇而不具颠覆性」；她在《本质的姿态》（1988）中指出委员会解禁她的书时同时查禁了两本黑人作者的书；2001 年一省教育厅将《七月的人民》移出阅读书单并称其「深度种族主义、傲慢居高临下」——她视之为严重侮辱，众多文学与政治人士抗议（客观并陈）。
- **国际讲学与奖项**：1960s–70s 常短期赴美多所大学任教；1961 W. H. Smith 英联邦文学奖（首项国际大奖）；1972 詹姆斯·泰特·布莱克纪念奖（《 A Guest of Honour》）；1974 布克奖（《保守的人》，与 Stanley Middleton《 Holiday》并列）；1985 Nelly Sachs Prize；1988 Anisfield-Wolf 奖；1991-10-03 诺贝尔文学奖；1996 国际波泰夫奖；2002 英联邦作家奖最佳非洲图书（《拾荒者》）；2007 法国荣誉军团军官勋章；2008 美国哲学学会会员；15 个荣誉学位；国际笔会副主席；南非作家协会创始成员。
- **诺奖**：1991 年获诺贝尔文学奖，为**首位南非得主、首位非洲女性作者**；此前 1972–1974 由瑞典学院院士 Artur Lundkvist 多次提名，1974 年曾与 Doris Lessing 同列候选短名单、1975 年入围最后五人（**均非获奖，勿写成 shared prize**）。
- **婚姻**：1949 嫁牙医 Gerald Gavron（Gavronsky），三年内离婚，女 Oriane（1950 生，后居法国南部）；1954 嫁德裔犹太名门艺术品商 Reinhold Cassirer（创办南非苏富比、自营画廊），子 Hugo（1955 生，纽约电影人，与其合作至少两部纪录片）；「美满婚姻」持续至 2001 年 Cassirer 因肺气肿去世；两人曾购尼斯附近山居。
- **宗教与身份**：世俗犹太人，1979–80 访谈自认无神论但「基本上有宗教气质」；拒绝把反隔离斗争归因于犹太身份："I refuse to accept that one must oneself have been exposed to prejudice and exploitation to be opposed to it..."（可引原文）。
- **未授权传记风波**：2006 年 Ronald Suresh Roberts 出版 *No Cold Kitchen*——授权未谈拢（丈夫病逝叙述、1950s 婚外情、以巴立场批评等分歧），她公开否认该书并指其背信，Bloomsbury 与 FSG 退出出版（客观简述）。
- **晚年**：2006 年在自家遭抢劫引发全国震动，拒绝搬入封闭式管理社区；「被切断始终是我心中的噩梦」；2012 年在《纽约书评》发表长文谴责 ANC 政府的国家信息保护法案（客观简述）；2004 年组织约 20 位作家为艾滋病救治运动（TAC）编写义卖集 *Telling Tales*。
- **核心作品与贡献（5 条）**：
  1. 《保守的人》（*The Conservationist*, 1974，布克奖）——通过反英雄 Mehring 看祖鲁文化与白人实业家世界，「保护自然以冻结变革」的隐喻；
  2. 《布尔格的女儿》（1979）——索韦托起义后写就，她自称为 Bram Fischer 的「密码致敬」；
  3. 《七月的人民》（1981）——想象血腥革命中白人夫妇藏身旧仆 July 的村庄；
  4. 短篇小说艺术——「我们时代的文学形式」：*Face to Face*（1949）至 *Beethoven Was One-Sixteenth Black*（2007），犹太主题短篇（"A Watcher of the Dead" 的 Shemira 守灵、"Letter from His Father" 回应卡夫卡）；
  5. 后隔离三部曲——《我的儿子的故事》（1990）、《没人陪我》（1994）、《屋中枪声》（1998）。
- **关键时间线（18 节点）**：1923 生于 Springs → 1937 首篇儿童故事 → 16 岁首篇成人小说 → 金山大学一年 → 1948 迁约翰内斯堡 → 1949 *Face to Face*、首婚 → 1951 《纽约客》首篇 → 1953 *The Lying Days* → 1954 嫁 Reinhold Cassirer → 1960 沙佩维尔惨案、投身运动 → 1961 W. H. Smith 奖 → 1963 *Occasion for Loving* → 1966 *The Late Bourgeois World* → 1971 James Tait Black 奖 → 1974 布克奖 → 1979 *Burger's Daughter* 被禁/解禁 → 1981 *July's People* → 1986 德尔马斯审判作证 → **1991 诺贝尔文学奖** → 1998 拒 Orange 奖入围 → 2002 *The Pickup* → 2005 *Get a Life* → 2012 谴责信息法案 → 2014-07-13 卒于约翰内斯堡。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | anti-apartheid fiction | 反种族隔离小说 | 道德与种族议题的主战场 | 核心页 |
| 1 | short story | 短篇小说 | 自认「我们时代的文学形式」，《纽约客》长期合作 | 短篇页 |
| 2 | political novel | 政治小说 | 爱与政治、权力与真相的道德暧昧 | 政治页 |
| 3 | bildungsroman | 成长小说 | 《说谎的日子》：小镇白人少女的政治觉醒 | 首作页 |
| 4 | epic realism | 史诗性写实 | 获奖理由所誉「宏伟的史诗性写作」 | 诺奖页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en` 用 page.md frontmatter 的 name，`qid` 以分批文件为准），设置 `primary_occupation='writer'`、`has_social_data=1`（`has_biography` 待 Beamer 立传后置 1）
- 关联职业 `writer`（rank 0）与 page.md 明载副职业（poet/novelist/playwright/essayist 等，1–3 行），国籍按 Nobel 官方口径
- 将上表 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`（fields 应为 5）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Gerald Gavron | 无向 | 牙医，1949 年结婚，三年内离婚 |
| spouse | Reinhold Cassirer | 无向 | 艺术品商，创办南非苏富比，1954 年结婚至 2001 年去世 |
| parent-child | Oriane Gavronsky | 无向 | 女儿，1950 年生，后居法国南部 |
| parent-child | Hugo Cassirer | 无向 | 儿子，1955 年生，纽约电影人，合作两部纪录片 |
| colleague | Nelson Mandela | 无向 | 协助修改 1964 年辩词 "I Am Prepared to Die"，1990 年获释后首先想见的人之一 |
| colleague | Bram Fischer | 无向 | 曼德拉辩护律师，《布尔格的女儿》的「密码致敬」对象 |
| colleague | George Bizos | 无向 | 曼德拉辩护律师，审判期间密友 |
| colleague | Bettie du Toit | 无向 | 挚友，1960 年被捕促成其投身反种族隔离运动 |
| colleague | Artur Lundkvist | 无向 | 瑞典学院院士，1972–1974 多次提名其获诺奖 |

> Doris Lessing 仅 1974 同列候选短名单**非 co-honored 不入库**；Olive Schreiner/J. M. Coetzee 为主题比较**非关系不入库**；Stanley Middleton 仅布克并列得主**不建 co-honored**；母女/父子均具名方入库；Ronald Suresh Roberts 为未授权传记作者争议**不入库**。

#### 4.5.1 入库操作

- 以 `name_en` 为中心写入 `person_relation`（yaml 路径见分批文件 `MySQL/data/Nadine_Gordimer.yaml`，引擎 `MySQL/seed_person.py`，幂等按 QID → name_en 匹配）
- 方向约定：`advisor-student` 有向（direction: advisor=对方是导师 / student=对方是学生）；`spouse` / `parent-child` / `colleague` / `influence` 无向（seed 自动 from<to 归一，yaml 勿写 direction）
- 对手方无库内记录时建 stub（不编造 qid，name_en 用规范全名）；库内已有同名记录按名幂等匹配并回填 QID；note 含 `: ` 须整体单引号包裹
- 校验：`SELECT COUNT(*) FROM person_relation WHERE from_id=<id> OR to_id=<id>`

- 校验本人物 relations 应为 9 行

### 第 5 步：设计配色 【人物专属】

- **主色**：深绿 `#145C54`（约翰内斯堡高原的矿脉与草原）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeMine` 矿镇/童年 — 铜矿褐 `#8C5A2B`
  - `badgeBan` 查禁/审查 — 封条红 `#A63A2B`
  - `badgeJuly` 革命/想象 — 玄武灰 `#4A4A55`
  - `badgeEpic` 史诗/诺奖 — 深金 `#B08A2E`
- **背景母题**：柔和气泡 + 矿井升降梯竖线与横向岩层线（矿镇母题），查禁页用斜向封条纹理。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有肖像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明「肖像待补」。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 代表作 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧肖像 + 右侧信息网格，含至少：本名/笔名演变、生卒（含享年）、国籍、婚姻子女、教育与讲席任职、主要荣誉、核心领域。事实取自 page.md infobox 与正文，不得杜撰。
4. **文学家替代公式框**：代表作书影框 / 名句引文框 / 意象图式三选一——核心贡献页与诺奖页至少各出现一处；引语只允许使用第 7–8 步「引语白名单」内的条目，其余禁杜撰。
5. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenLiterature`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 矿镇与禁书 / Nadine Gordimer 1923–2014 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、婚姻、荣誉、核心领域）
03  核心贡献概览 — 反隔离小说 / 短篇 / 政治小说 / 史诗性写实
04  矿镇童年 (1923–1937) — Springs、犹太移民父母、病中写作起步（引文框①：获奖理由 EN 原文）
05  金山大学与《纽约客》 (1937–1953) — Sophiatown、首篇成人小说、Face to Face、The Lying Days
06  行动主义起点 (1960–1964) — 沙佩维尔、du Toit、里沃尼亚审判与曼德拉辩词
07  查禁与解禁 (1966–1988) — 三部被禁书、布尔格的女儿的上诉反转（意象图式②：封条书影）
08  保守的人 (1974) — 布克奖、Mehring 与「冻结变革」的隐喻（书影框③）
09  七月的人民 (1981) — 革命想象与道德抉择
10  审判席上的证人 (1986) — 德尔马斯审判作证、藏匿 ANC 领导人（客观简述）
11  1991 诺贝尔奖 — 首位南非得主、首位非洲女性得主 + Nobel 引言
12  后隔离岁月 (1990–2005) — 三部后隔离小说、艾滋病运动、Telling Tales
13  争议与私人生活 — 未授权传记、2006 入室劫案、拒绝离南（客观简述）
14  遗产 — 纪录片改编、Gordimer 短篇奖、南非犹太社群的悼词
15  结尾
```

> 文学家无公式框：第 4/7/8/11 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文含 "in the words of Alfred Nobel" 插入语与破折号，逐词照引禁止改写、不得删插入语 |
| 「第一」口径 | 首位南非诺贝尔文学奖得主 + 首位非洲女性作者——两个「第一」并列写，勿写成「非洲首位得主」（1986 Soyinka 尼日利亚人在先） |
| 候选短名单 | 1974 年与 Lessing 同列短名单、1975 年入围最后五人均为**提名阶段事实**，勿写成「与 Lessing 共获奖」 |
| 政治内容红线 | 加入 ANC、藏匿领导人、谴责信息法案、以巴立场（2008 耶路撒冷 Writers Festival 辩护）：**只按 page.md 客观事实简述，不作政治评价、不展开政治叙事** |
| 《布尔格的女儿》 | 被禁一个月后上诉委员会解禁，理由是「过于偏颇而不具颠覆性」——反讽逻辑原样呈现，勿润色 |
| 2001 移出书单 | 「deeply racist, superior and patronising」是省教育厅的原话引述 + 她视为严重侮辱——双方并陈勿偏侧 |
| 婚姻年份 | 首婚 1949（三年内离）；再婚 **1954**–2001；女 Oriane 生 1950、子 Hugo 生 1955——年份勿混 |
| 引语白名单 | ① 获奖理由官方原句；② "I refuse to accept that one must oneself have been exposed to prejudice..."（page 明载）；③ "It's always been a nightmare in my mind, to be cut off."（page 明载）；④ Lelyveld 1985 与其自评两条 quote（page 明载）——其余禁杜撰 |
| 短篇主义 | 「short story was the literary form for our age」是其**自述**，勿写成批评界定论 |
| 书名省字号 | *July's People*、*Burger's Daughter*、*Gordimer's* 等省字号在 tex 中统一 `'{}` 或 `{\,}` 处理，防 lmodern 引号歧义 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Conservationist | 《保守的人》 | 1974 布克奖 |
| Burger's Daughter | 《布尔格的女儿》 | 1979，被禁/解禁公案 |
| July's People | 《七月的人民》 | 1981，革命想象 |
| The Lying Days | 《说谎的日子》 | 1953 首部长篇 |
| Occasion for Loving | 《爱的机会》 | 1963，跨种族爱情被定罪年代 |
| The Pickup | 《拾荒者》 | 2002，流散与移民 |
| I Am Prepared to Die | 《我已准备好赴死》 | 曼德拉 1964 辩词，她协助修改 |
| Sharpeville massacre | 沙佩维尔惨案 | 1960，行动主义起点 |
| Rivonia Trial | 里沃尼亚审判 | 1962–64，曼德拉受审 |
| Delmas Treason Trial | 德尔马斯叛国罪审判 | 1986，她出庭作证 |
| Springs, Transvaal | 斯普林斯（德兰士瓦） | 出生矿镇，勿写成约翰内斯堡市区 |
| Telling Tales | 《讲述的故事》 | 2004 艾滋病义卖文集，她主编 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（Alex-Productions）
- **风格标签**：怀旧 / 深情 / 回望
- **匹配理由**：戈迪默的一生是对「失去中的铭记」的写作——矿镇童年的病中阅读、被禁书页的反复、丈夫去世后的《拾荒者》与《把握生活》——「怀旧」匹配其回望式史诗笔法；「深情」匹配其「克制的怜悯」之外的另一面：对国家近乎固执的留守；「回望」匹配其九十年生涯横跨隔离前后两个南非的独特位置。
- **本地路径**：`music_audio/` 下 Alex-Productions Nostalgia（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Nadine_Gordimer/Nostalgia.wav`。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Nadine_Gordimer/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Nadine_Gordimer/images.txt` | 内嵌图片 URL 清单（肖像第 0 步下载） |
| `literature/generate_20th_century_list.py` | 名录与获奖理由 CITATION_ZH（EN 原文+中译，禁止改写） |
| `literature/prompt_batches_lit.json` | 分批清单（qid/year/color/bgm 预分配） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 统一封面 `\input` 模板 |
| `MySQL/data/Nadine_Gordimer.yaml` | 人物 fields + relations 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步汇报；无载禁写与政治内容红线是最高红线。**
