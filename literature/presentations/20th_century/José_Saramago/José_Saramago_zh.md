# 文学家立传提示词（OpenLiterature：José Saramago）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：José Saramago（若泽·萨拉马戈），1998 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对萨拉马戈，即「失明的白色与长句的河流」：以寓言、同情与反讽把握难以捉摸的现实，以无标点的长句与首字母大写的对话独步当代；其共产主义信仰、与教会及葡萄牙政府的冲突**客观简述、不作政治评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：José de Sousa Saramago（若泽·德·索萨·萨拉马戈，1922-11-16 ~ 2010-06-18），葡萄牙作家，1998 年诺贝尔文学奖、1995 卡蒙斯奖得主；葡语世界最重要的当代小说家，作品译成 25 种语言，仅葡萄牙国内销量逾两百万册。
- **设计哲学**：以「白眼与无名的城」为核心叙事——《失明症漫记》的白色瘟疫、突然无人死去的国度、伊比利亚半岛漂离欧洲——寓言性 (allegory) 是其骨架；视觉母题围绕「白色失明与橄榄树」展开。

---

## 二、背景信息 【人物专属】

- **目标文学家**：José de Sousa Saramago（若泽·萨拉马戈，1922-11-16 ~ 2010-06-18，享年 87 岁）
- **官方获奖理由（Nobel 1998，禁止改写）**：
  > "who with parables sustained by imagination, compassion and irony continually enables us once again to apprehend an elusory reality"
  > （表彰其以想象、同情与反讽支撑的寓言，使我们一再重新把握那难以捉摸的现实）
- **气质关键词**：**寓言的织工、长句的河流、晚成的巨人**
- **设计母题**：**白色的失明与橄榄树（white blindness & the olive tree）**。《失明症漫记》的白色盲潮、里斯本 Casa dos Bicos 前的百年橄榄树（骨灰所葬）、兰萨罗特岛的火山岩——以纸白与岩黑构成对位。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/José_Saramago/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Jos%C3%A9_Saramago
- **肖像**：第 0 步优先用 page.md 内嵌图 `1999-Saramago_a_Siena.jpg`（1999 锡耶纳）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1922-11-16 生于 Santarém 区 Azinhaga 村（里斯本东北约百公里）~ 2010-06-18 逝于西班牙加那利群岛兰萨罗特岛 Tías（白血病），享年 87 岁。
- **姓名由来**：「Saramago」本是野萝卜的植物名兼村人对父亲的绰号，出生登记时被村文书误并入姓名。
- **家庭与童年**：赤贫无地农家；1924 全家迁里斯本，兄 Francisco 四岁夭折；寒暑假回 Azinhaga——祖父中风就医前逐棵拥抱院中果树告别的场景，他自述「若这不给你留下印记，你便没有感情」；成绩好但家贫，12 岁转入技工学校。
- **工匠岁月**：车工毕业，做两年汽车修理工；泡里斯本公共图书馆自学。
- **婚姻**：1944 娶 Ilda Reis（1970 离异），1947 生独女 Violante；1968 起与作家 Isabel da Nóbrega 相伴（1968–1986，其文学导师，《修道院纪事》《里卡多·雷斯之年》题献者）；1986 遇西班牙记者 Pilar del Río（小其 27 岁，其作品西语官方译者），1988 结婚，相伴至终。
- **职业轨迹**：社会福利局公务员 → 出版社编辑与译者 → 记者；1975-04 任《Diário de Notícias》副社长，当年 11-25 事件后 24 名记者被逐、他本人被解职——此后转向职业写作。
- **文学生涯**：1947 出版首部小说《Terra do Pecado》后沉默近二十年；1966/1970 两部诗集、三本新闻文章集、1975 长诗、1976 政论集；1977《绘画与书法手册》、1978《几近之物》、1980《从地面升起》、1981《葡萄牙之旅》；**1982《修道院纪事》——60 岁才获广泛承认**：18 世纪宗教裁判所时期里斯本的巴洛克寓言（断臂士兵、少女透视眼、叛教神甫的飞行梦），1988 年 Pontiero 英译使其走向国际。
- **流亡（客观简述）**：1991《耶稣基督眼中的福音》——葡政府以冒犯天主教为由将其从 Aristeion 奖短名单除名；他认为遭遇政治审查，1992 与妻迁兰萨罗特岛直至去世；同年为里斯本「保卫文化全国阵线」创始成员。
- **关键荣誉**：葡萄牙笔会奖；Independent Foreign Fiction Prize（《里卡多·雷斯之年》）；**卡蒙斯奖 1995**；**诺贝尔文学奖 1998**（12-10 斯德哥尔摩授奖，Espmark 致辞）；圣地亚哥军事圣剑大十字 1998；多所大学荣誉博士。
- **身后**：葡萄牙全国哀悼两天；葬礼 2010-06-20 逾两万人送行；2011-06-18 骨灰葬于 Casa dos Bicos（基金会）前的百年橄榄树下；2007 自建若泽·萨拉马戈基金会；遗作《天窗》（Claraboia，1950s 写成被搁置）2011 追授出版。
- **核心作品与贡献（5 条）**：
  1. 《修道院纪事》（1982）——晚期成名的巴洛克寓言；
  2. 《里卡多·雷斯之死的一年》（1984）——佩索阿异名者在诗人死后又活一年的幻想（文本内指涉，Pessoa 不入库关系）；
  3. 《耶稣基督眼中的福音》（1991）——圣经重写，引发政府除名与流亡（客观简述）；
  4. 《失明症漫记》（1995）——无名国家「白色失明」瘟疫的寓言，全篇放弃专有名词；
  5. 《石筏》（1986）、《所有的名字》（1997）、《死者的间歇》（2005）、《该隐》（2009）——寓言谱系的延伸。
- **文体特征**：长句（有时一页有余）、句点稀少、对话不加引号而以新说话者首字母大写标示；作品间互文；以同理心书写人的境况与当代都市的孤独。
- **关键时间线（14 节点）**：1922 生于 Azinhaga → 1924 迁里斯本 → 12 岁入技校 → 车工 + 图书馆自学 → 1944 娶 Ilda Reis → 1947 首部小说 → 1966 复出 → 1969 加入葡共（终身党员，晚年自认自由共产主义）→ 1975 解职 → 1982《修道院纪事》→ 1988 娶 Pilar del Río → 1992 流亡兰萨罗特 → 1995 卡蒙斯奖 → **1998 诺贝尔文学奖** → 2010-06-18 逝世。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | allegorical fiction | 寓言体小说 | 失明/石筏/无人死去皆寓言 | 核心页 |
| 1 | experimental prose | 实验文体 | 长句、无引号对话、大写标示说话者 | 文体页 |
| 2 | historical fiction | 历史小说 | 修道院纪事的 18 世纪里斯本 | 修道院页 |
| 3 | theopoetics | 神学诗学 | 福音书与该隐的圣经重写 | 福音页 |
| 4 | political satire | 政治讽刺 | 页面明载 political satire of a subtle kind | 讽刺页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Ilda Reis | 无向 | 1944 年结婚、1970 离异，女 Violante 之母 |
| spouse | Pilar del Río | 无向 | 1988 年结婚，其作品西语官方译者 |
| advisor-student | Isabel da Nóbrega | 师→生（文学导师） | 1968–1986 的伴侣兼文学导师，两大代表作题献者 |
| colleague | Giovanni Pontiero | 无向 | 《修道院纪事》英译者，将其推向国际读者 |
| colleague | Margaret Jull Costa | 无向 | 英译者，称其为最伟大的当代葡萄牙作家 |

> Fernando Pessoa 仅系小说借其异名者为角色（文本内指涉）**禁建关系**；Harold Bloom/James Wood 仅系评价者**不入库**；Cavaco Silva 系政治冲突对方**不入库**（涉政红线）。

### 第 5 步：设计配色 【人物专属】

- **主色**：砖红 `#A31621`（里斯本屋顶与寓言的暗涌）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeBlind` 白色失明 — 纸白 `#E8E4DA`（深色描边）
  - `badgeRiver` 长句河流 — 幽蓝 `#2C4A6E`
  - `badgeMonastery` 修道院纪事 — 竹青 `#3E6B5A`
  - `badgeOlive` 橄榄树 — 橄榄绿 `#6B7A3E`
- **背景母题**：柔和气泡 + 一条长句式的连绵曲线横贯页面（省略句读的河）；晚期页面加入火山岩纹理。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 失明的白色与长句的河流 / José Saramago 1922–2010 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（全名、姓名由来、生卒、婚姻、荣誉、核心领域）
03  核心贡献概览 — 寓言体 / 实验文体 / 历史小说 / 神学诗学 / 政治讽刺
04  Azinhaga 的赤贫童年 (1922–1936) — 野萝卜的姓氏、祖父与橄榄树的告别
05  车间与图书馆 (1936–1966) — 车工、修理工、公共图书馆的自学
06  沉默与复出 (1947–1975) — 首部小说、二十年沉默、Diário 解职（客观简述）
07  晚成的巨人 (1982) — 修道院纪事：60 岁的巴洛克寓言（意象图式①：飞行机械）
08  里卡多·雷斯之死的一年 (1984) — 佩索阿异名者的延续（意象图式②：两位诗人的对影）
09  福音与流亡 (1991–1992) — 政府除名、迁兰萨罗特（客观简述，不评价）
10  失明症漫记 (1995) — 白色瘟疫与无名之国、卡蒙斯奖
11  1998 诺贝尔奖 — 寓言、想象、同情与反讽（引文框①：获奖理由 EN 原文 + Espmark 致辞摘句）
12  文体的革命 — 长句、无引号对话（引文框②：I write two pages 自述）
13  晚期寓言 (1997–2009) — 所有的名字、死者的间歇、该隐
14  身后与遗产 — 两万人送行、橄榄树下、基金会与天窗遗作
15  结尾 — 「以两页写作，再以阅读回应」：难以捉摸的现实的把握者
```

> 文学家无公式框：第 7/9/11/12 页用**书影框 / 意象图式 / 获奖理由与自述原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | 库内用 José Saramago；全名 José de Sousa Saramago；野萝卜登记轶事如实呈现 |
| 获奖理由措辞 | 官方 "who with parables sustained by imagination, compassion and irony continually enables us once again to apprehend an elusory reality"，勿改写 |
| 流亡叙事 | 政府除名 → 他自认审查 → 迁岛，按 page.md 客观表述，**不评价政府、不展开政治** |
| 宗教内容 | 《福音》《该隐》与教会争议一句带过；自评引语「我尊重信者，但不尊重机构」可用（page.md 有原文） |
| Pessoa | 异名者 Ricardo Reis 系小说角色设定——**禁建关系**；写「借其异名者入小说」即可 |
| 两段婚姻 | Ilda Reis（1944–1970）、Pilar del Río（1988–）；中间 Isabel da Nóbrega（1968–1986）伴侣兼导师——三条并行勿混 |
| 党籍年份 | 1969 加入葡共、终身党员——客观陈述 |
| 成名年龄 | 广泛承认始于 1982《修道院纪事》——「did not achieve widespread recognition until he was sixty」 |
| 遗作 | Claraboia（Skylight）系 1950s 手稿 2011 追授——勿写「临终新作」 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| parable | 寓言 | 获奖理由核心词 |
| elusory reality | 难以捉摸的现实 | 获奖理由核心词 |
| Blindness | 《失明症漫记》 | 1995；原名 Ensaio sobre a Cegueira |
| Baltasar and Blimunda | 《修道院纪事》 | 1982；原名 Memorial do Convento |
| heteronym | 异名者 | Pessoa 的文学装置 |
| theopoetics | 神学诗学 | 页面明载词 |
| Casa dos Bicos | 棱堡之家 | 基金会与骨灰安置地 |
| Lanzarote | 兰萨罗特岛 | 流亡地与日记系列 |
| Camões Prize | 卡蒙斯奖 | 1995 葡语文学最高奖 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Tragedy** — Alex-Productions
- **匹配理由**:
  - "悲怆" 匹配其寓言的底色 —— 失明症、石筏、无人死去的国度皆是文明的悲剧寓言，Tragedy 的深沉弦乐与《失明症漫记》的白色恐怖同构
  - "历史感" 匹配其晚成巨匠的一生 —— 车工二十年沉默、六十岁成名、流亡终老，命运感浓于戏剧性
  - "庄重" 匹配其文体 —— 长句河流需要沉着的低音推进
- **本地路径**: `music_audio/alex-productions/…/Tragedy.wav`（对照 `music_audio/curated_tracks.md` 取实际编号）→ `presentations/20th_century/José_Saramago/Tragedy.wav`
- **时长**: 约 150 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/José_Saramago/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 项目首页模板（统一 `\input`） |
| `MySQL/seed_person.py` | 人物主记录 + 研究领域 + 社会关系入库 |
| `MySQL/data/José_Saramago.yaml` | 入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
