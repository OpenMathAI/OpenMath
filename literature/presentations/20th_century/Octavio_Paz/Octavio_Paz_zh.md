# 文学家立传提示词（OpenLiterature：Octavio Paz）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Octavio Paz（奥克塔维奥·帕斯），1990 年诺贝尔文学奖得主，墨西哥诗人、散文家、外交官。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对帕斯，即「太阳石与迷宫」：以超现实主义诗艺写爱与时间的旋转回环，以《孤独的迷宫》剖析墨西哥性；其一生横跨诗歌、外交与论争，须**双线并陈、客观呈现、不作评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Octavio Paz Lozano（奥克塔维奥·帕斯，1914–1998），墨西哥哲学家、诗人、外交官；耶路撒冷奖（1977）、塞万提斯奖（1981）、纽斯塔特国际文学奖（1982）、1990 年诺贝尔文学奖得主。
- **设计哲学**：以「太阳石与迷宫」为核心叙事——《太阳石》以单节回环诗写时间的旋转，《孤独的迷宫》以论说文剖析「戴孤独面具的本能虚无主义者」的墨西哥灵魂。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Octavio Paz（奥克塔维奥·帕斯，1914-03-31 ~ 1998-04-19，享年 84 岁）
- **官方获奖理由（Nobel 1990，禁止改写）**：
  > "for impassioned writing with wide horizons, characterized by sensuous intelligence and humanistic integrity"
  > （表彰其视野开阔、充满激情的写作，以感性的智慧与人道的完整为特征）
- **气质关键词**：**旋转的太阳石、迷宫的剖析者、超现实主义的墨西哥传人**
- **设计母题**：**太阳石与迷宫（sunstone & labyrinth）**——阿兹特克太阳历石（Sunstone）的旋转回环对应《太阳石》单节回环诗；迷宫曲线对应《孤独的迷宫》；印度岁月的曼陀罗纹样为第三视觉元素。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Octavio_Paz/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Octavio_Paz
- **肖像**：第 0 步优先用 page.md 内嵌图 Paz0.jpg（1988）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1914-03-31 生于墨西哥城 ～ 1998-04-19 卒于墨西哥城（癌症），享年 84 岁；骨灰与妻子 Marie-José Tramini 的骨灰同藏于墨西哥城 Colegio de San Ildefonso 纪念处。西班牙语写作。（metadata.json 卒日有 04-02 等噪声，以正文 04-19 为准。）
- **家世**：墨西哥显赫自由主义政治世家，有西班牙与原住民血统；祖父 **Ireneo Paz**（改革战争老兵、记者兼出版人，办多份报纸）——帕斯的文学启蒙即来自祖父满藏墨西哥与欧洲经典的书房；父 **Octavio Paz Solórzano** 在革命中支持萨帕塔并为其写早期传记，帕斯随父命名但童年多随祖父度过，其父后死于非命。家族在墨西哥革命后破产，曾短暂迁洛杉矶。
- **蓝眼睛与身份**：蓝眼睛常被孩子们误认作外国人；据其多年助手、史家 Enrique Krauze 的传记，萨帕塔派革命者 Antonio Díaz Soto y Gama 见到小帕斯时说："*Caramba*, you didn't tell me you had a Visigoth for a son!"；Krauze 引帕斯自述："I felt myself Mexican but they wouldn't let me be one."（可引原文）。
- **文学起点**：1931 年 17 岁发表首批诗作（含 "Cabellera"）；1932 年 18 岁与友人创办首份文学评论 *Barandal*；1933 年出版首部诗集 *Luna silvestre*（19 岁零一月）。在国立墨西哥大学学习法律与文学（未完成），其间结识聂鲁达等左翼诗人。
- **尤卡坦与欧洲（1936–1938）**：1936 弃法学赴尤卡坦 Mérida 的农民子弟学校任教，开始写首部长诗 "Entre la piedra y la flor"（1941 修订 1976；**受 T. S. Eliot 影响**，写佃农在大地主权威下的处境）；1937-07 赴欧出席瓦伦西亚—巴塞罗那—马德里第二届国际作家大会（同席 Malraux、海明威、Stephen Spender、聂鲁达），声援西班牙共和国；在巴黎邂逅**超现实主义**运动，留下深刻影响。
- **杂志人生**：1938 回墨合办 *Taller*（写至 1941）→ 1970–1976 创办并主编 *Plural*（1975 被墨西哥政府关闭）→ 1976 创办 *Vuelta*，主编至 1998 年去世（杂志同年停刊）。
- **外交生涯**：1945 入外交界（纽约一段）→ 派巴黎，写《孤独的迷宫》（*El Laberinto de la Soledad*, 1950；NYT 称其把同胞描述为「藏在孤独与繁文缛节面具之后的本能虚无主义者」）→ 1952 首访印度，同年任东京临时代办 → 调日内瓦 → 1954 回墨城 → 1959 再派巴黎 → **1962 任墨西哥驻印度大使**（新德里完成《语法猿》与《东坡》，并深刻影响 Hungry Generation 作家群）→ **1968 年为抗议特拉特洛尔科学生示威屠杀辞去外交职务**（客观简述）。
- **讲席**：1969–70 剑桥 Simón Bolívar 讲席教授；1972–74 康奈尔 A. D. White 常驻教授；1974 哈佛 Charles Eliot Norton 诗歌讲席（成果《泥沼之子》*Los hijos del limo*）。
- **婚姻**：1937 娶 **Elena Garro**（墨西哥最优秀的作家之一，1935 相识），女 Helena，1959 离婚；1965 娶法国人 **Marie-José Tramini**，相伴至终。
- **政治思想（客观简述，不作评价）**：早年支持西班牙共和国；友人被斯大林秘密警察杀害后逐渐幻灭；1950 年代初在巴黎受 **David Rousset、André Breton、Albert Camus** 影响开始公开批判极权主义；在 *Plural*/*Vuelta* 揭露共产主义政权人权侵害（含古巴），遭拉美左翼敌视；自认属「民主的、自由主义的左翼」；1990 柏林墙倒塌后邀米沃什、丹尼尔·贝尔、Vargas Llosa 等赴墨城召开 The Experience of Freedom 讨论共产主义崩溃；1994 批评萨帕塔起义并主张「军事解决」（**只客观陈述立场，不展开政治叙事**）。政治光谱复杂：Grenier 称其「同时是浪漫主义者、自由主义者、保守主义者与社会主义者」。
- **核心作品与贡献（5 条）**：
  1. 《孤独的迷宫》（1950）+ 续作 *Posdata*（1970）——墨西哥民族文化心理的经典剖析，深刻影响 Fuentes 等墨西哥作家；
  2. "Piedra de sol"（《太阳石》，1957）——诺奖演说词誉为「宏伟的」超现实主义诗篇；
  3. 诗合集 *Libertad bajo palabra*（1949）与晚期诗集《东坡》《内在的树》（1987 前诗选）；
  4. 文学批评：*El arco y la lira*（1956）、*Los hijos del limo*（1974）；
  5. 《信仰的陷阱》（1982，修女诗人 Sor Juana Inés de la Cruz 分析传记）；剧作 *La hija de Rappaccini*（1956，改编 Hawthorne 并融印度 Vishakadatta、日本能剧、西班牙圣礼剧与叶芝影响；1992 年 Daniel Catán 改编为歌剧）。
- **翻译与跨艺术**：西译松尾芭蕉《奥之细道》（*Sendas de Oku*，1957，与 Eikichi Hayashiya 合作）与佩索阿选集（1962）；与 André Previn 合作歌曲套曲 *Honey and Rue*；其诗英译者含贝克特、Elizabeth Bishop、Charles Tomlinson、Mark Strand 等。
- **关键时间线（17 节点）**：1914 生于墨城 → 童年随祖父书房 → 1931 首批诗作 → 1932 *Barandal* → 1933 *Luna silvestre* → 1936 尤卡坦教书 → 1937 娶 Elena Garro、赴欧作家大会、遇超现实主义 → 1938 *Taller* → 1943 Guggenheim 研究金赴 Berkeley → 1945 入外交界、巴黎写《孤独的迷宫》→ 1950 出版 → 1952 首访印度/东京临时代办 → 1954 回墨城 → 1957 《太阳石》/《自由与誓言》/译《奥之细道》→ 1962 驻印度大使 → 1965 娶 Marie-José Tramini → 1968 辞职抗议屠杀 → 1970 *Plural* → 1974 哈佛 Norton 讲席 → 1976 *Vuelta* → 1977 耶路撒冷奖/国家艺术科学奖 → 1981 塞万提斯奖 → 1982 Neustadt 奖/《信仰的陷阱》→ 1990 诺贝尔文学奖 → 1998-04-19 卒于墨城。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | surrealist poetry | 超现实主义诗歌 | 1937 巴黎邂逅；《太阳石》被诺奖演说誉为宏伟典范 | 太阳石页 |
| 1 | cultural essay | 文化论说文 | 《孤独的迷宫》剖析墨西哥性与孤独面具 | 迷宫页 |
| 2 | modernist poetry | 现代主义诗歌 | T. S. Eliot《荒原》的震撼与早期诗艺 | 早期页 |
| 3 | literary criticism | 文学批评 | 《弓与琴》《 modem 的儿子们》：浪漫主义到先锋派 | 批评页 |
| 4 | poetry translation | 诗歌翻译 | 芭蕉《奥之细道》与佩索阿西译 | 印度页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en` 用 page.md frontmatter 的 name，`qid` 以分批文件为准），设置 `primary_occupation='writer'`、`has_social_data=1`（`has_biography` 待 Beamer 立传后置 1）
- 关联职业 `writer`（rank 0）与 page.md 明载副职业（poet/novelist/playwright/essayist 等，1–3 行），国籍按 Nobel 官方口径
- 将上表 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`（fields 应为 5）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Elena Garro | 无向 | 墨西哥名作家，1937 年结婚，1959 年离婚，育女 Helena |
| spouse | Marie-José Tramini | 无向 | 法国妻子，1965 年结婚，相伴至终，骨灰同藏 |
| parent-child | Octavio Paz Solórzano | 无向 | 父亲，萨帕塔支持者并为其作传 |
| influence | Ireneo Paz | Paz ← 对方 | 祖父，记者兼出版人，书房是其文学启蒙 |
| influence | Gerardo Diego | Paz ← 对方 | 1920s 发现的西班牙诗人，深刻影响早期写作 |
| influence | Juan Ramón Jiménez | Paz ← 对方 | 1920s 发现的西班牙诗人，深刻影响早期写作 |
| influence | Antonio Machado | Paz ← 对方 | 1920s 发现的西班牙诗人，深刻影响早期写作 |
| influence | T. S. Eliot | Paz ← 对方 | 《荒原》令其倾倒；Entre la piedra y la flor 受其影响 |
| influence | André Breton | Paz ← 对方 | 巴黎超现实主义引路人；1950s 反极权思想来源之一 |
| influence | Albert Camus | Paz ← 对方 | 1950s 批判极权主义的思想来源之一 |
| colleague | Pablo Neruda | 无向 | 左翼诗人；1937 年第二届国际作家大会同席 |
| colleague | Carlos Fuentes | 无向 | 早年至交，《迷宫》曾深刻影响其创作；1980s 因政见失和 |

> David Rousset（反极权思想来源之一）为次要思想来源**不入库**；恩里克·克劳泽（传记作者/助手）属史家记述关系**不入库**；1988 Vuelta 圆桌的十余人（米沃什/Bell/Vargas Llosa 等）为会议出席**不入库**；贝克特/Bishop 为译者关系非思想影响**不入库**。

#### 4.5.1 入库操作

- 以 `name_en` 为中心写入 `person_relation`（yaml 路径见分批文件 `MySQL/data/Octavio_Paz.yaml`，引擎 `MySQL/seed_person.py`，幂等按 QID → name_en 匹配）
- 方向约定：`advisor-student` 有向（direction: advisor=对方是导师 / student=对方是学生）；`spouse` / `parent-child` / `colleague` / `influence` 无向（seed 自动 from<to 归一，yaml 勿写 direction）
- 对手方无库内记录时建 stub（不编造 qid，name_en 用规范全名）；库内已有同名记录按名幂等匹配并回填 QID；note 含 `: ` 须整体单引号包裹
- 校验：`SELECT COUNT(*) FROM person_relation WHERE from_id=<id> OR to_id=<id>`

- 校验本人物 relations 应为 12 行

### 第 5 步：设计配色 【人物专属】

- **主色**：靛蓝 `#283593`（太阳石的深蓝与墨西哥高原夜色）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeSun` 太阳石/诗 — 日冕橙 `#D2691E`
  - `badgeLaby` 迷宫/论说 — 石板青 `#3E5C6B`
  - `badgeIndia` 印度岁月 — 藏红花黄 `#C8951C`
  - `badgeCrit` 批评/杂志 — 鼠尾草绿 `#5F7161`
- **背景母题**：柔和气泡 + 旋转同心圆环（太阳石历轮母题），迷宫页用单线回廊曲线。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有肖像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明「肖像待补」。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 代表作 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧肖像 + 右侧信息网格，含至少：本名/笔名演变、生卒（含享年）、国籍、婚姻子女、教育与讲席任职、主要荣誉、核心领域。事实取自 page.md infobox 与正文，不得杜撰。
4. **文学家替代公式框**：代表作书影框 / 名句引文框 / 意象图式三选一——核心贡献页与诺奖页至少各出现一处；引语只允许使用第 7–8 步「引语白名单」内的条目，其余禁杜撰。
5. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenLiterature`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 太阳石与迷宫 / Octavio Paz 1914–1998 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名、生卒、国籍、外交职务、讲席、荣誉、核心领域）
03  核心贡献概览 — 超现实主义诗 / 文化论说 / 批评 / 翻译
04  家世与书房 (1914–1931) — Ireneo Paz 书房、革命后的家道、蓝眼睛的墨西哥人
05  少年编辑与尤卡坦 (1931–1937) — Cabellera、Barandal、Luna silvestre、Mérida 学校
06  欧洲之夜 (1937–1938) — 作家大会、超现实主义邂逅、Taller（引文框①："I felt myself Mexican..."）
07  外交巴黎：孤独的迷宫 (1945–1954) — 墨西哥性剖析（意象图式②：迷宫回廊）
08  《太阳石》(1957) — 单节回环诗与阿兹特克历石（书影框③：获奖理由 EN 原文）
09  印度岁月 (1962–1968) — 大使、《语法猿》、Hungry Generation、芭蕉与佩索阿翻译
10  抗议与杂志 (1968–1976) — 辞职、Plural、剑桥/康奈尔/哈佛讲席
11  Vuelta 与批评体系 (1976–1982) — Los hijos del limo、信仰的陷阱
12  1990 诺贝尔奖 — 获奖理由引文框 + 三奖（耶路撒冷/塞万提斯/Neustadt）
13  政治思想（客观简述）— 幻灭、自由左翼自我定位、Experience of Freedom
14  引语与回响 — "There can be no society without poetry..."（page 明载引文）+ Xirau 评价
15  遗产 — 圣伊尔德丰索学院的骨灰、《太阳石》的回环、结尾
```

> 文学家无公式框：第 6/7/8/12/14 页用**代表作书影框 / 意象图式 / 引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for impassioned writing with wide horizons, characterized by sensuous intelligence and humanistic integrity"，逐词照引禁止改写 |
| 政治内容红线 | 特拉特洛尔科辞职、反极权批判、古巴、桑地诺、萨帕塔 1994 立场：**只按 page.md 客观事实简述，不作政治评价、不展开政治叙事** |
| 卒日噪声 | metadata.json 卒日有 04-02/04-20 多值，以正文 **1998-04-19** 为准并在提示词 §0 注明 |
| 祖孙同名 | 本人 Octavio **Paz Lozano**；父 Octavio **Paz Solórzano**；祖父 Ireneo Paz——三人勿混 |
| 《太阳石》 | 1957 年写的单节回环长诗（584 行回环，正文未载行数**禁写行数**），诺奖演说词誉其为「宏伟的」超现实主义诗篇——此评价归属演说词，勿写成委员会授奖语 |
| 迷宫出版年 | 《孤独的迷宫》1950 西语首版（正文 Works 列表口径），1951–1961 年代英译时间口径不一，幻灯片统一用 1950 |
| 两任妻子 | Elena Garro（1937–1959，作家）与 Marie-José Tramini（1965–1998）——勿把 Elena 写成「含冤 divorcio」等无载叙事 |
| Fuentes 失和 | 因**桑地诺立场分歧**（Paz 反对/Fuentes 支持）+ 1988 Vuelta 刊 Krauze 批评文所致——两因并列，勿简化为「因政见绝交」单线 |
| Hungry Generation | 「had a profound influence on them」是**帕斯影响对方**，方向勿反写 |
| 引语白名单 | ① "I felt myself Mexican but they wouldn't let me be one."（Krauze 引帕斯）；② "There can be no society without poetry..."（page 明载归属）；③ Soto y Gama 的 Visigoth 轶事（Krauze 传记转述，注明出处）；④ Xirau 诗学评语——其余禁杜撰 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Piedra de sol / Sunstone | 《太阳石》 | 1957，单节回环诗 |
| El Laberinto de la Soledad | 《孤独的迷宫》 | 1950，墨西哥性论说 |
| Posdata | 《附录/再论迷宫》 | 1970，《迷宫》续作 |
| Los hijos del limo | 《泥沼之子》 | 1974，浪漫主义到先锋派 |
| El arco y la lira | 《弓与琴》 | 1956，诗学批评 |
| Sor Juana Inés de la Cruz | 索尔·胡安娜 | 1982 传记《信仰的陷阱》主角 |
| El mono gramático | 《语法猿》 | 1974，印度岁月作品 |
| Ladera este | 《东坡》 | 1969，印度时期诗集 |
| Luna silvestre | 《野月》 | 1933，首部诗集 |
| Sendas de Oku | 《奥之细道》西译 | 1957，与 Hayashiya 合译 |
| Taller / Plural / Vuelta | 《工坊》《复数》《回归》 | 三份创办/主编杂志 |
| Tlatelolco | 特拉特洛尔科 | 1968 屠杀与辞职事由 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（Alex-Productions）
- **风格标签**：历史感 / 深沉 / 回溯
- **匹配理由**：帕斯一生在革命后的家道中落、西班牙内战的声援、超现实主义的巴黎与印度古国之间反复回溯——「历史感」匹配太阳石历轮的文明纵深；「深沉」匹配《孤独的迷宫》的自我审视；「回溯」匹配其晚期对时间与东方的沉思。靛蓝主色配 PAST 的暗调，与「太阳石与迷宫」的双母题同构。
- **本地路径**：`music_audio/` 下 Alex-Productions PAST（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Octavio_Paz/PAST.wav`。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Octavio_Paz/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Octavio_Paz/images.txt` | 内嵌图片 URL 清单（肖像第 0 步下载） |
| `literature/generate_20th_century_list.py` | 名录与获奖理由 CITATION_ZH（EN 原文+中译，禁止改写） |
| `literature/prompt_batches_lit.json` | 分批清单（qid/year/color/bgm 预分配） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 统一封面 `\input` 模板 |
| `MySQL/data/Octavio_Paz.yaml` | 人物 fields + relations 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步汇报；无载禁写与政治内容红线是最高红线。**
