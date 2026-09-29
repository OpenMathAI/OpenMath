# 文学家立传提示词（OpenLiterature：Derek Walcott）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Derek Walcott（德里克·沃尔科特），1992 年诺贝尔文学奖得主，圣卢西亚诗人、剧作家。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对沃尔科特，即「加勒比荷马与白鹭」：以《奥梅罗斯》把荷马史诗的回声带进圣卢西亚渔村，以水彩画家之眼写加勒比的光；其一生是殖民创痕与「再造世界」的欣悦并存的双线，须**双线并陈、客观呈现、不作评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Sir Derek Alton Walcott（德里克·阿尔顿·沃尔科特爵士，1930–2017），圣卢西亚诗人、剧作家、教授；1992 年诺贝尔文学奖得主（继 Saint-John Perse 之后第二位加勒比得主，评委报告称其为「加勒比荷马」）。
- **设计哲学**：以「加勒比荷马与白鹭」为核心叙事——《奥梅罗斯》让伊利亚特的幽灵在圣卢西亚渔夫 Achille 与 Hector 身上转世；「 shipwreck 与 Crusoe 隐喻」写殖民之后的重新开始；晚年水彩与诗互证的画家之眼。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Derek Walcott（德里克·沃尔科特，1930-01-23 ~ 2017-03-17，享年 87 岁）
- **官方获奖理由（Nobel 1992，禁止改写）**：
  > "for a poetic oeuvre of great luminosity, sustained by a historical vision, the outcome of a multicultural commitment"
  > （表彰其光彩夺目的诗歌创作，由历史视野所支撑，是多元文化承诺的结晶）
- **气质关键词**：**加勒比荷马、水彩诗人、流浪的安的列斯之子**
- **设计母题**：**加勒比海与白鹭（caribbean sea & white egrets）**——圣卢西亚 Castries 的海港弧线与渔民双桨构成视觉母题 A；《白鹭》（2010）的水鸟剪影与水彩晕染构成视觉母题 B；莱顿墙诗《Omeros》为插图元素。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Derek_Walcott/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Derek_Walcott
- **肖像**：第 0 步优先用 page.md 内嵌图 2008 年阿姆斯特丹荣誉晚宴照或 1992 VIII Festival Internacional 照；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1930-01-23 生于圣卢西亚 Castries（时为英属向风群岛圣卢西亚殖民地）～ 2017-03-17 卒于圣卢西亚 Gros-Islet 的 Cap Estate 自宅，享年 87 岁；国葬 2017-03-25（Castries 圣母无染原罪圣殿主教座堂举行，葬 Morne Fortune）。英语写作。
- **家庭**：父 Warwick Walcott 是公务员兼有才华的画家，在孪生子一岁时去世；母 Alix（Maarlin）是教师，热爱艺术、常在家中诵诗；孪生弟弟 Roderick Walcott 亦为剧作家；妹妹 Pamela；家系英格兰、荷兰与非洲血统——他诗作中探索的复杂殖民史的镜像；家庭属少数循道宗教（Methodist）社群，被法国殖民时期确立的天主教主流文化笼罩；中学就读天主教圣玛丽学院，小学即母亲任校长的循道宗学校。
- **绘画与文学双重起点**：少年师从民俗学者兼画家 **Harold Simmons**（职业艺术家的生命为他提供了榜样）；崇拜塞尚与乔尔乔内并向其学习；画作 2007 年参加纽约 Anita Shapolsky 画廊 "The Writer's Brush" 群展；《提埃坡罗的猎犬》（2000）即以其水彩自插图。
- **早慧发表**：14 岁在《圣卢西亚之声报》发表首诗（弥尔顿式宗教诗），被一位英国天主教神父在报上回应斥为亵渎（客观简述）；19 岁前用母亲资助的印费自印前两部诗集《二十五首诗》（1948）与《青年墓志：十二歌行》（1949），卖书还印费；巴巴多斯名诗人 **Frank Collymore** 对其早期作品给予关键批评支持。
- **引文（自述诗之天赋）**："Midsummer"（1984）："Forty years gone, in my island childhood, I felt that / the gift of poetry had made me one of the chosen, / that all experience was kindling to the fire of the Muse."
- **教育**：圣玛丽学院毕业后获奖学金入西印度大学学院（牙买加金斯敦）。
- **特立尼达与剧坊**：1953 移居特立尼达任评论家、教师、记者；1959 创办特立尼达戏剧工坊（Trinidad Theatre Workshop，前身为 Little Carib Theatre Workshop）——至今国际知名、曾巡演美国（含 1995 年 Eliot Norton 奖《塞维利亚的小丑》与《猴山上的梦》制作），他生前一直任董事会成员。
- **国际成名与剧作**：1962《绿色之夜：诗 1948–1960》引起国际关注；剧作《猴山上的梦》（1967 出版/1970 发表）主角 Makak「代表殖民者压迫下殖民地原住民的处境」，1971 年由黑人剧团 Negro Ensemble Company 在外百老汇制作并获**奥比奖最佳外国戏剧**；该剧 1970 年出版当年即由 NBC 电视制作播出。英国 1972 新年荣誉授 **OBE**（表彰其对圣卢西亚文学与戏剧的贡献）。
- **波士顿岁月**：1981 年受聘波士顿大学，同年借大学与麦克阿瑟奖之助创办 Boston Playwrights' Theatre（首任艺术总监）；在波士顿大学教授文学与写作逾二十年，2007 年退休。
- **波士顿诗人群**：与流亡美国的俄国诗人**约瑟夫·布罗茨基**、亦在波士顿教书的爱尔兰诗人**谢默斯·希尼**结为挚友；三人自称「美国经验之外」的一群诗人。
- **《奥梅罗斯》（1990）**：松散呼应《伊利亚特》的史诗——渔民 Achille、Hector，退役英军军官 Plunkett 及妻 Maud，女佣 Helen，盲人 Seven Seas（象征荷马）与作者本人；主叙事在圣卢西亚，另及马萨诸塞 Brookline 与第五卷的里斯本/伦敦/都柏林/罗马/多伦多游记；以变体三行体（terza rima）写成；主题——岛屿之美、殖民重负、加勒比身份的碎片化、后殖民世界中诗人的角色；被《华盛顿邮报》与《纽约时报书评》（1990 年度好书）盛赞，为其「主要成就」。
- **诺奖**：1992 年获诺贝尔文学奖，继瓜德罗普出生的 Saint-John Perse（1960）之后第二位加勒比得主；评委会称其作为「加勒比荷马」（jury report）。
- **晚年讲席**：2007 内华达大学拉斯维加斯分校 Elias Ghanem 创意写作讲席；2008 首届 Cola Debrot 讲座；2009–2012 阿尔伯塔大学驻校学者；2010 埃塞克斯大学诗歌教授。
- **荣誉线**：1969 Cholmondeley Award → 1971 Obie → 1972 OBE → 1981 MacArthur「天才奖」→ 1988 女王金质诗歌奖章 → 1990 W. H. Smith 文学奖（*Omeros*）→ **1992 诺贝尔奖** → 2004 Anisfield-Wolf 终身成就奖 → 2011 T. S. Eliot 奖与 OCM Bocas 加勒比文学奖（均 *White Egrets*）→ 2015 Griffin 诗歌终身贡献奖 → 2016 圣卢西亚勋章首批评骑士（独立日庆典）。
- **性骚扰指控与牛津风波（客观简述，不作评价）**：1982 年哈佛大二学生指控 1981 年 9 月性骚扰（拒其求爱后得全班唯一 C）；1996 年波士顿大学学生提起性骚扰诉讼，双方和解；2009 年角逐牛津诗歌教授职位，因旧指控报道曝光而**退出**；另一领先候选者 Ruth Padel 当选后旋因被曝向记者提示指控材料在舆论压力下辞职——海尼与 Al Alvarez 等众诗人联名致信《泰晤士文学增刊》为其声援（**只按 page.md 客观事实并陈，不作道德评价**）。
- **核心作品与贡献（5 条）**：
  1. 《奥梅罗斯》（1990）——加勒比荷马史诗，批评界视作其主要成就；
  2. 剧作逾二十部——多由特立尼达戏剧工坊制作：《猴山上的梦》（奥比奖）、《提让和他的兄弟们》、《塞维利亚的小丑》等，直面西印度后殖民的边缘处境；
  3. 《绿色之夜》（1962）——国际成名诗集；自印双璧《二十五首诗》《青年墓志》（1948–49）；
  4. 散文《黄昏所言：序曲》（1970）——「我们在这里都是陌生人……我们的身体用一种语言思考，用另一种语言行动」；船难与鲁滨逊隐喻（"The Castaway"、剧作《哑剧》）写殖民之后的重建；
  5. 晚期画诗互证——《提埃坡罗的猎犬》（2000 水彩自插图）、《白鹭》（2010）、《晨光，帕拉明》（2016，与 Peter Doig 合璧）。
- **关键时间线（17 节点）**：1930 生于 Castries → 1 岁丧父 → 14 岁首诗发表 → 1948–49 自印两部诗集 → 西印度大学 → 1953 迁特立尼达 → 1959 创立戏剧工坊 → 1962 *In a Green Night* → 1967 *Dream on Monkey Mountain* → 1971 奥比奖 → 1972 OBE → 1981 波士顿大学/Boston Playwrights' Theatre/MacArthur → 1984 *Midsummer* → **1990 *Omeros*** → **1992 诺贝尔文学奖** → 2009 牛津风波退选 → 2011 T. S. Eliot 奖 → 2016 封骑士 → 2017-03-17 卒于圣卢西亚。
- **身后**：1993 Castries 市中心的 Derek Walcott Square；2013 Ida Does 纪录片《诗是一座岛》；作品档案入西印度大学圣奥古斯丁主馆，1997 年入选 UNESCO「世界记忆」名录；2016 童年故居（17 Chaussée Road）整修为 Walcott House；2019 年起 Derek Walcott Prize for Poetry 年度奖。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | epic poetry | 史诗诗 | 《奥梅罗斯》松散呼应《伊利亚特》 | 奥梅罗斯页 |
| 1 | postcolonial literature | 后殖民文学 | infobox Movement；殖民创痕与身份碎片化 | 主题页 |
| 2 | caribbean poetry | 加勒比诗歌 | 「绝对加勒比作家」的自我定位与群岛意象 | 加勒比页 |
| 3 | verse drama | 诗剧 | 二十余部剧作与特立尼达戏剧工坊 | 剧场页 |
| 4 | painterly poetics | 画家诗学 | 塞尚/乔尔乔内之眼，晚期水彩与诗互证 | 绘画页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en` 用 page.md frontmatter 的 name，`qid` 以分批文件为准），设置 `primary_occupation='writer'`、`has_social_data=1`（`has_biography` 待 Beamer 立传后置 1）
- 关联职业 `writer`（rank 0）与 page.md 明载副职业（poet/novelist/playwright/essayist 等，1–3 行），国籍按 Nobel 官方口径
- 将上表 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`（fields 应为 5）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Fay Moston | 无向 | 1954 年结婚，育子 Peter，1959 年离婚 |
| spouse | Margaret Maillard | 无向 | 医院救济员，1962 年结婚，育两女，1976 年离婚 |
| spouse | Norline Metivier | 无向 | 演员，1976 年结婚，1993 年离婚 |
| parent-child | Warwick Walcott | 无向 | 父亲，公务员兼画家，孪生子一岁时去世 |
| parent-child | Alix Walcott | 无向 | 母亲，教师，家中诵诗的艺术启蒙 |
| advisor-student | Harold Simmons | Walcott ← 导师（对方） | 少年绘画导师，民俗学者兼画家 |
| influence | T. S. Eliot | Walcott ← 对方 | 深刻影响其写作的现代主义诗人 |
| influence | Ezra Pound | Walcott ← 对方 | 深刻影响其写作的现代主义诗人 |
| influence | Robert Lowell | Walcott ← 对方 | 自述影响其写作的美国诗人，亦为友人 |
| influence | Elizabeth Bishop | Walcott ← 对方 | 自述影响其写作的美国诗人，亦为友人 |
| colleague | Joseph Brodsky | 无向 | 波士顿挚友，称其诗句如「扑岸的潮浪」 |
| colleague | Seamus Heaney | 无向 | 波士顿挚友，同属「美国经验之外」的三人 |
| colleague | Frank Collymore | 无向 | 巴巴多斯诗人，对其早期作品的关键批评支持 |

> 孪生弟弟 Roderick Walcott（剧作家）与妹妹 Pamela——白名单无 sibling 类型**不入库**（提示词身份页仍须写明孪生关系）；晚年伴侣 Sigrid Nama 无对应类型**不入库**；Robert Graves/Adam Kirsch/William Logan 为评论者**不入库**；Paul Simon 仅《The Capeman》词曲合作且属音乐剧商业项目**不入库**；Peter Doig 为画集合作者（2016）**不入库**。

#### 4.5.1 入库操作

- 以 `name_en` 为中心写入 `person_relation`（yaml 路径见分批文件 `MySQL/data/Derek_Walcott.yaml`，引擎 `MySQL/seed_person.py`，幂等按 QID → name_en 匹配）
- 方向约定：`advisor-student` 有向（direction: advisor=对方是导师 / student=对方是学生）；`spouse` / `parent-child` / `colleague` / `influence` 无向（seed 自动 from<to 归一，yaml 勿写 direction）
- 对手方无库内记录时建 stub（不编造 qid，name_en 用规范全名）；库内已有同名记录按名幂等匹配并回填 QID；note 含 `: ` 须整体单引号包裹
- 校验：`SELECT COUNT(*) FROM person_relation WHERE from_id=<id> OR to_id=<id>`

- 校验本人物 relations 应为 13 行

### 第 5 步：设计配色 【人物专属】

- **主色**：深赭褐 `#5C3A1E`（火山岛土色与旧船木）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeOmeros` 奥梅罗斯/史诗 — 爱琴蓝 `#1F5E8C`
  - `badgeCarib` 加勒比/海 — 珊瑚青 `#0E7C7B`
  - `badgeStage` 剧场 — 幕布红 `#8B1A1A`
  - `badgeAquarelle` 水彩/白鹭 — 雾青 `#7FA6A0`
- **背景母题**：柔和气泡 + 波浪弧线（加勒比海母题），史诗页用三行体斜纹，晚期页转为水彩晕染。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有肖像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明「肖像待补」。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 代表作 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧肖像 + 右侧信息网格，含至少：本名/笔名演变、生卒（含享年）、国籍、婚姻子女、教育与讲席任职、主要荣誉、核心领域。事实取自 page.md infobox 与正文，不得杜撰。
4. **文学家替代公式框**：代表作书影框 / 名句引文框 / 意象图式三选一——核心贡献页与诺奖页至少各出现一处；引语只允许使用第 7–8 步「引语白名单」内的条目，其余禁杜撰。
5. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenLiterature`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 加勒比荷马与白鹭 / Derek Walcott 1930–2017 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、头衔线 KCSL·OBE·OM·OCC、讲席、荣誉、核心领域）
03  核心贡献概览 — 史诗 / 后殖民诗 / 诗剧 / 画家诗学
04  Castries 童年 (1930–1947) — 循道宗家庭、父画家早逝、母亲诵诗（引文框①：Midsummer 自述）
05  自印双璧与西印度大学 (1948–1953) — 25 Poems、Epitaph、母亲印费、Collymore、奖学金
06  特立尼达与戏剧工坊 (1953–1970) — 评论/教师/记者、1959 建坊（意象图式②：工坊舞台）
07  猴山上的梦 (1967–1971) — Makak 与殖民处境、奥比奖、NBC 电视
08  绿色之夜与船难隐喻 (1962–1978) — In a Green Night、The Castaway、Crusoe 意象
09  波士顿岁月 (1981–2007) — 波士顿大学、Boston Playwrights' Theatre、布罗茨基与希尼
10  奥梅罗斯 (1990) — 渔民与荷马、三行体、双城叙事（书影框③：获奖理由 EN 原文）
11  1992 诺贝尔奖 — 「加勒比荷马」与官方理由引文框
12  晚期画诗互证 (2000–2016) — 提埃坡罗的猎犬、白鹭、晨光帕拉明
13  牛津风波与晚年（客观简述）— 指控报道、退选、Padel 事件、诗人联名信
14  遗产 — Derek Walcott Square、UNESCO 世界记忆、Walcott House、年度诗歌奖
15  结尾
```

> 文学家无公式框：第 4/8/10/11 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for a poetic oeuvre of great luminosity, sustained by a historical vision, the outcome of a multicultural commitment"，逐词照引禁止改写 |
| 「加勒比荷马」 | 出自 jury report，勿与授奖词正文混写为同一句 |
| 第二位口径 | 「第二位加勒比得主，继瓜德罗普出生的 Saint-John Perse（1960）之后」——勿写成「首位加勒比得主」 |
| 头衔堆叠 | KCSL·OBE·OM·OCC 四头衔：OBE=1972 大英帝国官佐勋章；OM 处为**牙买加功绩勋章**（Order of Merit (Jamaica)，infobox 链接口径），勿写成英国功绩勋章；KCSL=2016 圣卢西亚骑士指挥官勋位；OCC=加勒比共同体勋章——infobox 链接与正文授勋年表冲突时以正文年表为准并注 |
| 头韵年份 | Dream on Monkey Mountain 出版 1967（infobox）/正文两说 1970——**两处各忠于上下文**，幻灯片统一用 1967 并在陷阱表注明 1970 为发表年两说 |
| 意识红线 | 1981/1996 指控与 2009 牛津退选、Padel 辞职：**只按 page.md 客观事实并陈，不作道德评价、不用煽情措辞**；「misogyny 归因」是部分记者观点，注明归属 |
| 引语白名单 | ① Midsummer 四行自述；② "I have never separated the writing of poetry from prayer..."；③ "We are all strangers here..."；④ Graves 与布罗茨基两条评语（page 明载）——其余禁杜撰 |
| Logan 差评 | William Logan 的负面评论（Omeros "clumsy"）与 Kirsch 的正面评论**并陈**，勿只取一面 |
| 孪生弟弟 | Roderick Walcott 身份页写明「孪生弟弟，亦为剧作家」，但关系库无 sibling 类型不入库 |
| 自印资金 | 母亲以裁缝兼教师薪水垫付两卷印费——「两美元成本自筹」的叙事以 page.md 原话转述为准 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Omeros | 《奥梅罗斯》 | 1990 史诗，主要成就 |
| Dream on Monkey Mountain | 《猴山上的梦》 | 奥比奖最佳外国戏剧 |
| In a Green Night | 《绿色之夜》 | 1962 国际成名诗集 |
| Another Life | 《另一种生活》 | 1973 自传性长诗，Kirsch 称「第一座主峰」 |
| White Egrets | 《白鹭》 | 2010，T. S. Eliot 奖 |
| Ti-Jean and His Brothers | 《提让和他的兄弟们》 | 1958，Mi-Jean 的殖民知识批判 |
| Trinidad Theatre Workshop | 特立尼达戏剧工坊 | 1959 创立 |
| terza rima | 三行体（但丁体） | 奥梅罗斯的变体 |
| Castries | 卡斯特里 | 圣卢西亚首都，出生地 |
| Morne Fortune | 幸运山 | 安葬地 |
| shipwreck / Crusoe | 船难与鲁滨逊隐喻 | 后殖民重建意象 |
| Walcott House | 沃尔科特故居 | 2016 开放的童年故居 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（Alex-Productions）
- **风格标签**：觉醒 / 昂扬 / 开阔
- **匹配理由**：沃尔科特的底色是「被剥夺即特权」的欣悦——在无人书写过的群岛上第一次为世界命名（"There was a great joy in making a world..."）——「觉醒」匹配其「为第一次写下岛屿与人而狂喜」的一代人心态；「开阔」匹配加勒比海与史诗的画幅；「昂扬」匹配布罗茨基所谓「如潮浪扑岸」的诗句能量。赭褐主色配 Awaken 的开阔，与「加勒比荷马」的母题同构。
- **本地路径**：`music_audio/` 下 Alex-Productions Awaken（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Derek_Walcott/Awaken.wav`。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Derek_Walcott/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Derek_Walcott/images.txt` | 内嵌图片 URL 清单（肖像第 0 步下载） |
| `literature/generate_20th_century_list.py` | 名录与获奖理由 CITATION_ZH（EN 原文+中译，禁止改写） |
| `literature/prompt_batches_lit.json` | 分批清单（qid/year/color/bgm 预分配） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 统一封面 `\input` 模板 |
| `MySQL/data/Derek_Walcott.yaml` | 人物 fields + relations 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步汇报；无载禁写与敏感内容红线是最高红线。**
