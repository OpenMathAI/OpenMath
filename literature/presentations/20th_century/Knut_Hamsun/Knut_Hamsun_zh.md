# 文学家立传提示词（OpenLiterature：Knut Hamsun）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Knut Hamsun（克努特·汉姆生），1920 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对汉姆生，即「血液的低语」：以意识流与内心独白开创心理文学，以挪威的森林与海岸承载泛神论的自然之爱；其一生亦是文学荣耀与政治污点并存的公案，须**双线并陈、客观呈现、不作评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Knut Hamsun（本名 Knud Pedersen，1859–1952），挪威作家，创作跨度逾 70 年（1877–1949），1920 年诺贝尔文学奖得主；被誉为「近百年（约 1890–1990）最具影响力与革新性的文学文体家之一」。
- **设计哲学**：以「血液的低语与旷野」为核心叙事——他反对现实主义与自然主义，主张现代文学的对象是人类心智的幽微曲折，以内心独白开创心理文学。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Knut Hamsun（克努特·汉姆生，本名 Knud Pedersen，1859-08-04 ~ 1952-02-19，享年 92 岁）
- **官方获奖理由（Nobel 1920，禁止改写）**：
  > "for his monumental work, Growth of the Soil"
  > （表彰其不朽巨著《大地的生长》）
- **气质关键词**：**心理文学的开拓者、新浪漫反叛的旗手、漫游者母题的化身**
- **设计母题**：**血液的低语与旷野（the whisper of blood & the open road）**。其 1890 文章主张文学须写「血液的低语、骨髓的恳求」（Lyngstad 译述）；代表作反复出现「永久漫游者」母题——以挪威针叶林、海岸线与一条无尽乡路构成视觉主线。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Knut_Hamsun/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Knut_Hamsun
- **肖像**：第 0 步优先用 page.md 内嵌图 `Knut_Hamsun.jpeg`（1890）或 Munch 1896 肖像版画；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1859-08-04 生于 Gudbrandsdalen 峡谷的 Lom（时属瑞典-挪威联合王国，今挪威）～ 1952-02-19 卒于 Grimstad，享年 92 岁。挪威语写作。
- **家庭与童年**：本名 Knud Pedersen，Peder Pedersen 与 Tora Olsdatter 之子，七子女中排第四；3 岁随家迁至 Nordland 的 Hamsund（Hamarøy），家境贫寒；9 岁被送去叔叔 Hans Olsen 处帮工邮局，遭殴打与挨饿——他后来自述长期神经疾患源于此；1874 逃回 Lom，做五年杂工（店员、小贩、鞋匠学徒、治安官助手、小学教师）；17 岁当制绳学徒并开始写作；商人 **Erasmus Zahl** 资助过他，Zahl 后成为小说人物 Mack 的原型（*Pan*、*Dreamers*、*Benoni*、*Rosa*）。
- **笔名演变**：1877 首书 *Den Gaadefulde* 署 Knud Pedersen；1878 *Bjørger*（模仿 Bjørnson 文风、为后期《Victoria》雏形）署笔名 **Knud Pedersen Hamsund**；此后以 **Knut Hamsun** 行世。
- **美国岁月**：数年在美国游历打工，1889 出版观感 *Fra det moderne Amerikas Aandsliv*（《现代美国的精神生活》）。
- **婚姻**：1898 娶 Bergljot Bech，育女 Victoria，1906 婚姻破裂；1909 娶 **Marie Andersen**（1881–1969）——她原是有前途的演员，为随他定居 Hamarøy 结束演艺生涯，购农场务农（写作补帖家用），后迁 Larvik，1918 购入 Landvik 老庄园 **Nørholm**（Lillesand 与 Grimstad 之间），在此专心写作；育 Tore、Arild、Ellinor、Cecilia 四子女（共 5 子女，含 Tore Hamsun）。Marie 著有两部回忆录。
- **核心作品与贡献（6 条）**：
  1. *Hunger*（《饥饿》，1890）——半自传：青年作家在首都 Kristiania 因饥饿贫困濒临疯狂；内心独白与奇诡逻辑被视为预演卡夫卡与二十世纪小说；
  2. 新浪漫反叛核心作：*Mysteries*（1892）、*Pan*（1894）、*Victoria*（1898）——「世纪之交新浪漫主义反叛的旗手」；
  3. 「永久漫游者」母题——闯入乡村共同体的漂泊陌生人（常为叙事者），贯穿 *Mysteries*、*Pan*、*Under the Autumn Star*、*The Last Joy*、*Vagabonds*、*Rosa* 等；
  4. 泛神论自然书写——对挪威林地与海岸的狂喜描绘（可引 "No one knows God, man knows only gods."）——见 *Pan*、漫游者三部曲、*Growth of the Soil*；
  5. *Growth of the Soil*（《大地的生长》，1917 两卷）——"his monumental work"，为其赢得 1920 诺奖；晚期 Nordland 小说受挪威新现实主义影响，写乡村日常，用方言、反讽与幽默；
  6. 诗作仅一部 *The Wild Choir*（1904），被多位作曲家谱曲。
- **文学史定位**：以意识流与内心独白开创心理文学，影响 Thomas Mann、Franz Kafka、Maxim Gorky、Stefan Zweig、Henry Miller、Hermann Hesse、John Fante、James Kelman、Charles Bukowski、Ernest Hemingway 等；Isaac Bashevis Singer 称其为「现代文学流派在各方面之父——主观性、片段性、倒叙、抒情性；二十世纪整个现代小说流派都源自汉姆生」；Thomas Mann 称其为「陀思妥耶夫斯基与尼采的后裔」；与 Strindberg、Ibsen、Undset 并称国际知名的斯堪的纳维亚四杰。1898 年为 Sigurd Ibsen 创办的杂志 *Ringeren* 撰稿。
- **种族主义与亲纳粹（客观简述，不作评价）**：自青年时代起持种族主义与反平等主义观点（1889 年美国书中含抨击种族通婚的言论，**原文侮辱性语句禁引**）。一战中其亲德态度已被注意（1918 *The Atlantic* 猜测源于「爱唱反调」）。二战中支持德国战争努力：撰文（1940 称「德国人在为我们而战」）、1943 将诺贝尔奖章赠予宣传部长戈培尔（传记作者 Thorkild Hansen 视为求见希特勒的策略）、会见希特勒——会上他抱怨德国驻挪民政长官 Terboven 并要求释放被囚挪威公民，激怒希特勒（Otto Dietrich 回忆录称这是唯一有人能让希特勒插不上话的会面，归因于汉姆生的耳聋）；他另曾多次协助因抵抗活动被囚的挪威人。希特勒死后一周发表悼文（原文 "He was a warrior, a warrior for mankind, and a prophet of the gospel of justice for all nations."）。
- **战后审判（客观简述）**：1945-06-13 以叛国罪被拘，因高龄入住 Grimstad 医院；1947 受审，精神鉴定认定「永久性心智损伤」而免于刑事定罪，改课民事罚——1948 被罚 325,000 克朗（最高法院由 575,000 减至 325,000），事由为被指加入 Nasjonal Samling 及给德国人道义支持，但**洗清任何直接纳粹关联**；他自陈从未加入任何政党，是否入会与心智是否受损至今仍有争议。战后其书在挪威大城市被公众焚毁，并被拘禁于精神病院数月。
- **绝笔与身后**：1949 在 Landvik 半软禁中写成 *Paa giengrodde Stier*（*On Overgrown Paths*，《长满野草的小径》）——申辩心智健全、痛斥精神科医生与法官；1954 出 15 卷全集，2009（诞辰 150 周年）出 27 卷全集；1996 Jan Troell 传记片《Hamsun》（Max von Sydow 主演）；2009-08-04 Knut Hamsun Centre 于 Hamarøy 开幕；三处故居（Hamsund gård、Hamsunstugu、Nørholm）辟为博物馆；作品 25 次影视改编（1916 起）；骨灰葬于 Nørholm 家园花园。
- **关键时间线（18 节点）**：1859 生于 Lom → 3 岁迁 Hamsund → 9 岁寄养叔父家受虐 → 1874 逃回 Lom 打杂五年 → 17 岁制绳学徒开始写作、Zahl 资助 → 1877 *Den Gaadefulde* → 1878 *Bjørger* → 美国游历多年 → 1889 《现代美国的精神生活》→ **1890 *Hunger*** → 1892 *Mysteries* → 1894 *Pan* → 1895–1910 六部剧作 → 1898 娶 Bergljot Bech、为 *Ringeren* 撰稿 → 1906–12 漫游者三部曲 → 1909 娶 Marie Andersen → 1917 *Growth of the Soil* → **1920 诺贝尔文学奖** → 1927–33 August 三部曲 → 1936 *The Ring is Closed* → 1940–43 二战亲德言论、赠奖章、会见希特勒 → 1945 被拘 → 1947–48 审判与罚款 → 1949 *On Overgrown Paths* → 1952-02-19 卒于 Grimstad。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | psychological novel | 心理小说 | *Hunger*/*Mysteries*：意识流与内心独白的开创 | 核心页 |
| 1 | neo-romanticism | 新浪漫主义 | 世纪之交新浪漫反叛的旗手 | 反叛页 |
| 2 | Norwegian new realism | 挪威新现实主义 | 晚期 Nordland 小说：乡村日常、方言、反讽幽默 | 晚期页 |
| 3 | nature writing | 自然书写 | 泛神论：挪威林地与海岸的狂喜描绘 | 自然页 |
| 4 | modernism | 现代主义 | infobox Movements 之一；现代小说源头之一 | 影响页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Bergljot Bech | 无向 | 1898–1906，育女 Victoria |
| spouse | Marie Andersen | 无向 | 1909 年结婚，相伴终身，著两部回忆录 |
| influence | Thomas Mann | Hamsun → 对方 | Mann 受其影响；并称汉姆生为陀思妥耶夫斯基与尼采的后裔 |
| influence | Franz Kafka | Hamsun → 对方 | Hunger 的内心独白被视为预演卡夫卡 |
| influence | Maxim Gorky | Hamsun → 对方 | page.md 明载受影响者 |
| influence | Stefan Zweig | Hamsun → 对方 | page.md 明载受影响者 |
| influence | Henry Miller | Hamsun → 对方 | page.md 明载受影响者 |
| influence | Hermann Hesse | Hamsun → 对方 | page.md 明载受影响者 |
| influence | John Fante | Hamsun → 对方 | page.md 明载受影响者 |
| influence | James Kelman | Hamsun → 对方 | page.md 明载受影响者 |
| influence | Charles Bukowski | Hamsun → 对方 | page.md 明载受影响者 |
| influence | Ernest Hemingway | Hamsun → 对方 | page.md 明载受影响者 |

> Bjørnson（早年 *Bjørger* 模仿其文风）属少年习作模仿**不入库**；Singer 为推崇者兼意第绪语译者非受影响者**不入库**；Ibsen 批评（"dramatized wood pulp"）系小说角色 Nagel 台词**不入库**。

### 第 5 步：设计配色 【人物专属】

- **主色**：暗砖红 `#6E2B2B`（血液的低语 + 大地的颜色）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgePsy` 心理小说 — 幽蓝 `#2C4A6E`
  - `badgeNeo` 新浪漫主义 — 绛紫 `#6B3FA0`
  - `badgeSoil` 大地/自然 — 泥土褐 `#7A5C3E`
  - `badgeTrial` 争议/审判 — 铁灰 `#4A4A55`
- **背景母题**：柔和气泡 + 一条从挪威森林延伸至海岸的乡路曲线（漫游者母题），晚期页面转为灰阶基调。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 血液的低语 / Knut Hamsun 1859–1952 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像（Munch 1896 版画）+ 右信息网格（本名/笔名演变、生卒、国籍、故居、荣誉、核心领域）
03  核心贡献概览 — 心理小说 / 新浪漫主义 / 自然书写 / 现代主义源头
04  早年：Lom 与 Hamsund (1859–1874) — 贫困、叔父虐待、五年杂役
05  学徒与写作起点 (1874–1888) — Zahl 资助、Den Gaadefulde、Bjørger、美国岁月
06  Hunger (1890) — Kristiania 的饥饿与疯狂、内心独白（引文框①：whisper of the blood 段落）
07  神秘与漫游 (1892–1898) — Mysteries、Pan、Victoria、永久漫游者母题（意象图式②）
08  剧作与杂志 (1895–1910) — 六部剧、Ringeren 撰稿
09  婚姻与庄园 (1898–1918) — Bergljot、Marie、农场计划、Nørholm
10  大地的生长 (1917) — 泛神论、土地与人（获奖理由 EN 原文引文框）
11  1920 诺贝尔奖 — Singer 评价引文框：二十世纪现代小说源自汉姆生
12  晚期多产 (1920–1936) — August 三部曲、The Ring is Closed、挪威新现实主义转向
13  二战岁月 (1940–1945) — 亲德立场、赠奖章、会见希特勒（客观简述）
14  审判与绝笔 (1945–1952) — 叛国指控、民事罚款、On Overgrown Paths、身后争议与纪念馆
15  遗产 — 意识流与内心独白的源头、影视改编、结尾
```

> 文学家无公式框：第 6/10/11 页用**代表作书影框 / 意象图式 / 获奖理由与评价原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for his monumental work, Growth of the Soil"（json 引号噪声清理后引用）——诺奖**独得**，理由单指《大地的生长》 |
| 姓名三段演变 | 本名 Knud Pedersen（1877）→ 笔名 Knud Pedersen Hamsund（1878）→ Knut Hamsun；出生时属瑞典-挪威联合王国，国籍按 Nobel 口径写挪威 |
| 政治内容红线 | 二战亲德、种族主义言论、审判：**只按 page.md 客观事实简述，不作政治评价、不展开政治叙事**；1889 书中种族主义原文（侮辱性语句）禁引，只转述"抨击种族通婚" |
| 可用引语白名单 | ① "No one knows God, man knows only gods."（page 明载其语）；② whisper of the blood 段落（1890 文章，Lyngstad 译述，注明转译）；③ Singer 评价长句；④ Hitler 悼文原句（只在争议页客观引用）——其余禁杜撰 |
| Nagel 台词 | "dramatized wood pulp" 是 *Mysteries* 虚构角色台词，是汉姆生借角色发声，勿写成他本人直接骂 Ibsen |
| Dietrich 轶事 | 「唯一能让希特勒插不上话的人」出自 Otto Dietrich 回忆录并归因于耳聋——注明出处归属，勿写成定论 |
| 协助抗德囚徒 | 「多次帮助因抵抗活动被囚的挪威人、试图影响德国在挪政策」须与亲德立场**并列呈现**，勿只写一面 |
| 罚款数字 | 检方 575,000 → 最高法院减至 325,000 克朗；"cleared of any direct Nazi affiliation"（无直接纳粹关联认定）与「被指入党」并存，勿合并简化 |
| Singer 身份 | Singer 是诺奖得主兼意第绪语译者、推崇者，**勿列入受影响作者名单** |
| 泛神论 | "has been linked with" 泛神论——写「被认为与泛神论灵性运动相关联」，勿写成教义信徒 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Hunger / Sult | 《饥饿》 | 1890，成名作 |
| Mysteries / Mysterier | 《神秘》 | 1892 |
| Growth of the Soil / Markens Grøde | 《大地的生长》 | 1917 两卷，诺奖理由所指 |
| Pan | 《潘》 | 1894，泛神论代表作 |
| Victoria | 《维多利亚》 | 1898 爱情小说 |
| On Overgrown Paths / Paa giengrodde Stier | 《长满野草的小径》 | 1949 绝笔 |
| The Wild Choir / Det vilde Kor | 《野合唱》 | 1904，唯一诗集 |
| stream of consciousness | 意识流 | 其开创技法之一 |
| interior monologue | 内心独白 | 与意识流并提 |
| neo-romanticism | 新浪漫主义 | 世纪之交反叛运动 |
| Kristiania | 克里斯蒂安尼亚 | 奥斯陆旧称 |
| Nørholm | 诺霍尔姆 | 晚年庄园与安葬地 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（Alex-Productions）
- **风格标签**：辽阔 / 漂泊 / 深沉
- **匹配理由**：汉姆生的文字反复回到挪威海岸与林地的狂喜描绘（*Pan*、*Growth of the Soil*），其漫游者母题即是陆上漂泊的海员气质——「辽阔」匹配旷野与海岸的画幅；「漂泊」匹配漫游者与流亡美国、客居德国的一生；「深沉」匹配晚年审判的沉重。
- **本地路径**：`music_audio/` 下 Alex-Productions SEA（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Knut_Hamsun/SEA.wav`。

> **开始执行。每完成一步汇报；无载禁写与政治内容红线是最高红线。**
