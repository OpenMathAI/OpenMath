# 文学家立传提示词（Jean-Paul Sartre）

> **OpenLiterature 人物专属立传提示词**：Jean-Paul Sartre（让-保罗·萨特，1964 诺贝尔文学奖·主动拒领，法国）。
> 执行 agent 按第三部分第 0–9 步逐步执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Jean-Paul Charles Aymard Sartre（让-保罗·萨特），20 世纪法国哲学与存在主义的旗手、「介入文学」的开创者。
- **设计哲学**：文学家立传无公式框，以**代表作书影、名句引文框、意象图式**替代物理公式表达；必须有「身份信息页」（Identity / Bio 速览页），务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Jean-Paul Sartre（1905-06-21 ~ 1980-04-15，享年 74 岁）
- **官方获奖理由（Nobel 官方 EN 原文 + 名录中译，禁止改写；本人主动拒领，奖项仍归属其名下）**：
  > "for his work, which, rich in ideas and filled with the spirit of freedom and the quest for truth, has exerted a far-reaching influence on our age"
  > 「表彰其思想丰富、充满自由精神与求真意志的著作，对我们时代产生了深远影响」（1964-10-22 宣布；萨特此前于 10-14 致函请求除名、23 日经《费加罗报》公开拒绝，成为首位自愿拒领者）
- **气质关键词**：**自由的哲学旗手、介入文学的创始人、咖啡馆里的公共知识分子**。
- **设计母题**：**自由与介入（Freedom & Engagement）**。花神咖啡馆的灯光、巴黎街头的传单、深渊前的抉择时刻——用咖啡馆椅、钢笔与路灯光影构成视觉母题。
- **本地数据源**：`literature/presentations/pages/20th_century/Jean-Paul_Sartre/page.md`（+ metadata.json / images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Jean-Paul_Sartre
- **肖像**：第 0 步待下载（images.txt 有 1965 速写、与波伏娃 1955 北京合影、1967 威尼斯照等真实照片可用）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；封面 `\input` 项目共享首页。

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，直接使用）

- 生卒：1905-06-21 生于巴黎 ~ 1980-04-15 逝于巴黎（肺水肿），享年 74 岁；1973 起近乎全盲；葬礼 1980-04-19 约 5 万人送行；安葬蒙帕纳斯公墓（与波伏娃合穴）。
- 家庭：独子；父 Jean-Baptiste（法国海军军官）在其 2 岁时病逝（多因在印度支那染病）；母 Anne-Marie Schweitzer 携子回默东外家；外祖父 Charles Schweitzer（德语教师）教其数学并引其进入古典文学； Albert Schweitzer（神学家/管风琴家/医生）为其表亲；12 岁母亲改嫁迁拉罗谢尔。眼疾：右眼感觉性外斜视。
- 教育：Cours Hattemer → **巴黎高等师范学院（ENS）**，修心理学/哲学史/逻辑/伦理/社会学/物理证书，1928 高等学习文凭论文《心理生活中的形象》（导师 **Henri Delacroix**）→ agrégation 首考失利、次考与波伏娃并列第一（萨特列首）。
- 关键思想节点：少年读柏格森《时间与自由意志》入哲学 → ENS 与 Aron/Nizan 友谊 → 每周参加 **Kojève** 研讨班（page.md 称「对其哲学发展最具决定性的影响」）→ 1932 Aron 于蒙帕纳斯咖啡馆一言点醒其读胡塞尔 → 1933–34 接替 Aron 赴柏林法国研究所研胡塞尔现象学 → 战俘营读海德格尔《存在与时间》。
- 二战：1939 应征入伍任气象兵 → 1940 Padoux 被俘，特里尔 Stalag XII-D 战俘营 9 个月（写首部剧 *Bariona*）→ 1941-04 因健康获释 → 1941-10 任孔多塞中学教员（顶替被维希禁教的犹太教师）→ 与波伏娃、梅洛-庞蒂等创抵抗小组 Socialisme et Liberté（旋散）→ 写作《存在与虚无》《苍蝇》《禁闭》——三部作品均未遭德军审查；为 Camus 地下报纸《战斗报》积极撰稿。
- 战后：1944-10 接手 Gallimard「介入文学」计划 → **1945-10 创刊并主编《现代》（Les Temps modernes）**（刊名取自卓别林《摩登时代》）→ 辞教专事写作与政治参与 → 1945–1949 长篇小说三部曲《自由之路》。
- 关键荣誉：Nobel Literature **1964（主动拒领，史上首例自愿拒绝者之一，仅二人）**；1945 拒领荣誉军团勋章；Grand Prize for the Best Novels of the Half-Century；Toynbee Prize；美国艺术与科学学院外籍院士。
- 核心作品（4–6 条）：哲学——《存在与虚无》（1943）、《存在主义是一种人道主义》（1946 讲演）、《辩证理性批判》（1960，第二卷身后出版）；小说——《恶心》（1938）、《墙》（1939）、《自由之路》三部曲；戏剧——《苍蝇》（1943）、《禁闭》（1944，名句 "l'enfer, c'est les autres"）、《脏手》（1948）、《魔鬼与上帝》（1951）；自传——《文字生涯》（*Les Mots*，1964，宣布弃笔之作）；文学批评与传记——《什么是文学？》、《圣热内》（1952）、《家庭的白痴》（论福楼拜，5 卷，1971–72，未竟）。
- 关键时间线（15–20 节点）：1905 生巴黎 → 1907 丧父寄居默东 → 1917 迁拉罗谢尔 → 1920s 读柏格森立志哲学 → ENS 岁月（结识 Aron/Nizan、恶作剧事件 1927）→ 1928 文凭论文 → 1929 遇波伏娃 → 1928–29 为日本哲学家九鬼周造任私人法语教师 → 1931–45 勒阿弗尔/拉昂/巴黎任教 → 1933–34 柏林研胡塞尔 → 1936 《自我的超越性》 → 1938 《恶心》 → 1939 入伍 → 1940–41 战俘营 → 1941 Socialisme et Liberté → 1943 《存在与虚无》+初识 Camus → 1944 《禁闭》 → 1945 创刊《现代》、赴美报道 → 1946 《存在主义是一种人道主义》《反犹主义者与犹太人》 → 1948 天主教《禁书目录》列其全部作品 → 1951 与 Camus 绝交（《反抗者》论战） → 1952–56 亲 PCF 立场 → 1956 匈牙利事件后疏离 → 1960 《辩证理性批判》 → 1964 《文字生涯》+诺奖拒领 → 1965 收养 Arlette Elkaïm → 1967 罗素法庭（与 Russell 等） → 1968 五月风暴声援、被捕后戴高乐特赦（「人们不会逮捕伏尔泰」） → 1970–71 声援毛派《人民事业报》街头叫卖 → 1974 探监 Baader → 1973 失明 → 1980-04-15 逝于巴黎。
- 拒领声明（page.md 有英文原文，可引用）：始终谢绝一切官方荣誉，且 "a writer should not allow himself to be turned into an institution"（作家不应让自己变成一个机构）。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | existentialism | 存在主义 | 「存在先于本质」、自由与自欺 | 哲学页 |
| 1 | phenomenology | 现象学 | 胡塞尔—海德格尔脉络的存在论现象学 | 哲学页 |
| 2 | committed literature | 介入文学 | *littérature engagée*、《现代》发刊词 | 介入页 |
| 3 | modern drama | 现代戏剧 | 《禁闭》《苍蝇》《脏手》 | 戏剧页 |
| 4 | literary criticism | 文学批评 | 《什么是文学？》、Situations 系列 | 批评页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Simone de Beauvoir | 无向 | 1929–1980 终身伴侣（开放式关系，未正式结婚），ENS/agrégation 同榜，合葬蒙帕纳斯 |
| advisor-student | Henri Delacroix | advisor | 1928 高等学习文凭论文导师 |
| advisor-student | Jacques-Laurent Bost | student | infobox 明载 notable student |
| advisor-student | Jean-Bertrand Pontalis | student | infobox 明载 notable student |
| influence | Henri Bergson | 对方→本人 | 少年读《时间与自由意志》转向哲学 |
| influence | Edmund Husserl | 对方→本人 | 1933–34 柏林专研其现象学 |
| influence | Martin Heidegger | 对方→本人 | 战俘营读《存在与时间》，后成《存在与虚无》主要影响源 |
| influence | Alexandre Kojève | 对方→本人 | 每周研讨班，page.md 称最具决定性的哲学影响 |
| influence | Louis-Ferdinand Céline | 对方→本人 | 1932 读《茫茫黑夜漫游》受其显著影响 |
| influence | Frantz Fanon | 对方→本人 | 1950s 末受其影响转向第三世界论述（并为其《全世界受苦的人》作序） |
| colleague | Raymond Aron | 无向 | ENS 起终生的（时有摩擦的）朋友，1932 现象学引路人 |
| colleague | Paul Nizan | 无向 | ENS 挚友，视其为另一个自我 |
| colleague | Albert Camus | 无向 | 1943–1951 密友，《战斗报》撰稿人，1951 《反抗者》论战绝交，Camus 逝后作悼文 |
| colleague | Maurice Merleau-Ponty | 无向 | Socialisme et Liberté 共同创立者，后政见相左（「超布尔什维克」之讥） |
| colleague | Jean Paulhan | 无向 | 《新法兰西评论》主编，扶植其文学批评生涯 |
| colleague | Bertrand Russell | 无向 | 1967 罗素法庭（越战战争罪行调查庭）共同发起 |
| parent-child | Arlette Elkaïm-Sartre | 本人→对方 | 1965 收为养女 |

入库：`MySQL/seed_person.py data/Jean-Paul_Sartre.yaml`（幂等，QID 匹配）。

### 第 5 步：配色方案

- 主色：藏蓝 `#1F3A5F`（巴黎夜色与哲学的冷峻）；辅助：诺奖香槟金 `C9A227`。
- badgeA 存在主义 — 深灰蓝 `#2C4A6E`；badgeB 现象学 — 青灰 `#4E6E6E`；badgeC 介入文学 — 锈红 `#9A4A2E`；badgeD 戏剧/批评 — 暗金 `#8F7420`。
- 背景母题：咖啡馆桌椅剪影、放射状灯光、烟圈曲线（低饱和，勿喧宾夺主）。

### 5.1 格式硬要求 【★ 必须满足】

1. 封面右上角肖像 + 细边框 + 姓名小字注；顶部/底部明示国籍（France）。
2. **身份信息页**：封面之后、核心贡献之前，左头像右信息网格（生卒/全名/国籍/教育 ENS/师承 Delacroix/伴侣波伏娃/主要荣誉/核心领域）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。
4. 名句引文框替代公式框：《禁闭》"l'enfer, c'est les autres"（*No Exit*，page.md 明载其创作语境与出处）或 1964 拒领声明（英文原文在 page.md）。

### 第 6 步：幻灯片序列（14 页）

```
00 OpenLiterature 项目首页（共享封面 \input）
01 封面 — 自由的旗手 / Jean-Paul Sartre 1905–1980 + 四色 badge + 右上头像 + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 存在主义 / 现象学 / 介入文学 / 戏剧与批评
04 巴黎童年与 ENS（1905–1929）— 丧父、外祖父书房、恶作剧、波伏娃与 agrégation
05 哲学引路人（1929–1936）— Kojève 研讨班、Aron 一言、柏林研胡塞尔、Bergson/Céline
06 《恶心》与教师岁月（1931–1939）— 勒阿弗尔、首部长篇
07 战争与战俘营（1939–1941）— 气象兵、Stalag XII-D、《存在与时间》
08 占领下的写作（1941–1944）— Socialisme et Liberté、《存在与虚无》《苍蝇》《禁闭》（引文框）
09 《现代》与介入文学（1945–1950）— 创刊词、《自由之路》、《什么是文学？》
10 Camus：友谊与决裂（1943–1951）— 《反抗者》论战、悼文（客观并置）
11 诺奖 1964：主动拒领 — 首例、致函除名、《费加罗报》声明（引文框）、此前拒荣誉军团勋章
12 公共知识分子的晚年 — 罗素法庭 1967、五月 1968、「不逮捕伏尔泰」、失明与《家庭的白痴》
13 遗产 — 5 万人葬礼、蒙帕纳斯合穴、对批判理论与后殖民理论的影响
14 结尾
```

### 第 7–8 步：Beamer 源码与布局检查

- 每页 `\newcommand{\xxxslide}` 定义；骨架复用 Kenneth_G_Wilson_zh.tex。
- 每写完一页 `latexmk -c` 清理后 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查

**Sartre 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 拒领性质 | 1964 奖项**归属其名下但他主动拒绝**——页面口径：获奖者 Jean-Paul Sartre（declined）；勿写成「未获奖」或「被撤回」；1975 年曾有人代为索要奖金被瑞典学院拒绝（Gyllensten 记载，客观一句） |
| 伴侣称谓 | 与波伏娃为终身伴侣（开放式、未婚），幻灯片勿写「妻子/wife」；infobox 用 Partner |
| 《禁闭》语境 | "l'enfer, c'est les Autres" 部分针对德占时期告密氛围——引句时交代语境，勿泛化为鸡汤格言 |
| 政治红线 | 苏联/阿尔及利亚/古巴/毛派/越战等全部政治立场：只按 page.md 客观陈述事实（如 1969 联署声援 Solzhenitsyn、拒共而不入党、OAS 两次炸弹袭击 1961–62），**不作政治评价、不展开政治叙事、不选边** |
| 争议节 | Lamblin 等人的指控与 1977 联署：仅在「争议」处客观一句带过（事后追述性质），不作叙述性展开 |
| 序言风波 | 为 Fanon《全世界受苦的人》作序；1967 后部分版本删去其序（六日战争亲以立场）——两处事实分开写，不合并因果 |
| Heidegger 关系 | 受其影响但也有公开分歧（《论人道主义》批评），勿写成单线师承 |
| 与 Gide/Malraux | 1941 曾求援被「未决」——可作时间线一句，不建关系 |
| Camus 口径 | 按 Camus 语「他是抵抗的作家，不是写作的抵抗者」转述归属明确；1951 绝交与 1960 悼文并置不矛盾 |
| 学位 | ENS 文凭论文 1928（导师 Delacroix）；无博士学位——勿写「博士」 |
| 无载禁写 | 不编造 Nizan 之死细节、不写与加缪之外的哲学论战对手关系（Althusser 之争可一句带过不入库） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| existentialism | 存在主义 | 勿与「实存主义」混用；页面统一 |
| Being and Nothingness | 《存在与虚无》 | 1943 |
| Nausea | 《恶心》 | 1938，勿译《呕吐》 |
| No Exit / Huis clos | 《禁闭》 | 名句出自此剧 |
| bad faith | 自欺 | *mauvaise foi* |
| existence precedes essence | 存在先于本质 | 核心命题 |
| committed literature | 介入文学 | *littérature engagée* |
| Les Temps modernes | 《现代》 | 刊名取自卓别林《摩登时代》 |
| The Roads to Freedom | 《自由之路》 | 三部曲 |
| The Words | 《文字生涯》 | 1964 自传，勿译《词语》 |
| Critique of Dialectical Reason | 《辩证理性批判》 | 1960 |
| The Family Idiot | 《家庭的白痴》 | 论福楼拜五卷 |

---

## 四、背景音乐建议

- **选定曲目**：**PAST**（分批文件预分配）。
- **匹配理由**：历史感/深沉气质匹配战时巴黎、抵抗运动与战后思想论战的黑白底片感；与「介入」一词的时代重量同构。
- **备选**（未采用）：Tragedy（悲情过重）、With Me（双人叙事向，偏波伏娃视角）。
- **本地路径**：按 `music_audio/curated_tracks.md` 索引拷贝至 `presentations/20th_century/Jean-Paul_Sartre/PAST.wav`。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Jean-Paul_Sartre/page.md` | 事实基准（唯一来源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录与中译理由 |
| `MySQL/data/Jean-Paul_Sartre.yaml` | 入库 yaml（本提示词第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
