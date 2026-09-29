# 文学家立传提示词（OpenLiterature：Claude Simon）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Claude Simon（1985 诺贝尔文学奖，新小说派代表）为执行实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 〇、批次信息 【人物专属】

| 项 | 值 |
|----|----|
| 分批 | `literature/prompt_batches_lit.json` batch 17（agent：lit-batch-17） |
| dir / qid | Claude_Simon / Q131549 |
| 获奖年份 | 1985 |
| 主色（预分配） | `#1E4E79` |
| BGM（预分配） | With Me |
| page.md | `literature/presentations/pages/20th_century/Claude_Simon/page.md` |
| prompt / yaml | `literature/presentations/20th_century/Claude_Simon/Claude_Simon_zh.md` / `MySQL/data/Claude_Simon.yaml` |

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆与文学家侧首例（Knut Hamsun 等）的实战经验。
- **本实例**：Claude Eugène Henri Simon（克洛德·西蒙）。
- **设计哲学**：文学家立传无公式框——用**代表作书影、名句引文框、绘画意象图式**替代；保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Claude Simon（1913-10-10 ~ 2005-07-06，享年 91 岁）
- **气质关键词**：**新小说的画家、时间的测绘者、骑兵与葡萄园的叙事者** —— 1985 诺贝尔文学奖获奖理由（官方原文 + 中译，禁止改写）：
  > "who in his novel combines the poet's and the painter's creativeness with a deepened awareness of time in the depiction of the human condition"
  > （表彰其小说将诗人与画家的创造力融为一体，在对人类境况的描绘中深化了对时间的意识）
- **设计母题**：**画布上的时间（painterly time）**。获奖理由「诗人与画家的创造力」+「时间的意识」双关——长句如长镜头、跨页括号如未干的颜料；骑兵团与葡萄园是同一块画布上的两个图层。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Claude_Simon/page.md`（同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Claude_Simon
- **肖像**：⏳ 第 0 步待下载（images.txt 有 `Claude_Simon_ca_1932.jpg` 250px 缩略图，建议取 500px 原图；失败则装饰圆占位）
- **参考模板**：
  - 文学家成品参照：`literature/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`literature/presentations/cover/`（以主控实际封面文件为准）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- 生卒：1913-10-10 生于马达加斯加塔那那利佛（Tananarive，时属法属马达加斯加）~ 2005-07-06 逝于巴黎，享年 91 岁
- 国籍：法国
- 家庭：法国人家庭；父亲为职业军官，**死于第一次世界大战**；随母亲与母系家族在鲁西永葡萄酒产区佩皮尼昂长大；先祖有法国大革命时期的将军
- 教育：巴黎 Stanislas 中学；**在 André Lhote 画室修绘画课程**（明载师承，入库 advisor-student）
- 经济独立：21 岁继承一笔小遗产，经济从此自立
- 军旅与战争：1935–1936 于 Lunéville 第 31 骑兵团服役；1936 赴巴塞罗那参加国际纵队（西班牙内战）；1936 年开始写作；1937 游历西班牙/德国/苏联/意大利/希腊/土耳其；1939-08 应征入伍，1940 参加默兹河战役、5 月 17 日在骑兵中队遭屠杀中脱身，被俘后 10 月逃脱并加入抵抗运动；1944 重返巴黎与抵抗运动
- 友人：佩皮尼昂避难时期与画家 **Raoul Dufy、Jean Lurçat** 结为朋友（明载，入库 colleague）
- 任职：长居巴黎，每年部分时间住比利牛斯山 Salses；**至死坚持职业登记为「葡萄种植者」（viticulteur）而非作家**——认为种葡萄比写小说更有实在疗效
- 关键荣誉：Nobel 1985；1961 《L'Express》奖（*La Route des Flandres*）；1967 Prix Médicis（*Histoire*）；1973 东英吉利大学荣誉博士；Commandeur des Arts et des Lettres（frontmatter）
- 核心作品与贡献（4–6 条）：
  1. *La Route des Flandres*《佛兰德公路》（1960）——战争经验+骑兵在机械化战争中的荒诞，常被视为其最高成就
  2. *Le Vent*（1957）与 *L'Herbe*（1958）——新小说风格转折点
  3. *Histoire*（1967，Médicis 奖）与 *Triptyque*（1973，三故事无段落切换混排）——形式实验代表作
  4. *Les Géorgiques*（1981）与 *L'Acacia*（1989，以非顺序日期替代章节标题）——家族史叙事
  5. *Femmes: sur 23 peintures de Joan Miró*（1966）——为米罗 23 幅画作著文，绘画与写作互文
  6. 约 20 部著作，密集的自传体风格；生平约 20 部长篇存世（Pléiade 两卷本 2006/2013）
- 关键时间线（约 16 节点）：1913 生于塔那那利佛 → 父亲死于一战 → 佩皮尼昂成长 → Stanislas 中学 → Lhote 画室 → 21 岁继承遗产 → 1935–36 骑兵服役 → 1936 西班牙内战国际纵队、开始写作 → 1937 欧游 → 1939-08 应征 → 1940 默兹河战役/被俘/逃脱 → 抵抗运动、完成 *Le Tricheur*（1946 出版）→ 1946–1958 早期小说与新小说转向 → 1960 *La Route des Flandres*+L'Express 奖+《121 宣言》联署 → 1967 Médicis 奖 → 1973 荣誉博士 → 1981 *Les Géorgiques* → 1985 诺贝尔奖 → 1989 *L'Acacia* → 2001 *Le Tramway* → 2005-07-06 逝于巴黎

### 第 1–3 步：目录、Makefile 与肖像收集 【模板通用】

- 第 1 步：在 `literature/presentations/20th_century/` 下确认/创建 `Claude_Simon/` 与 `images/`
- 第 2 步：复制邻近已立传目录的 Makefile，改 `MAIN=Claude_Simon_zh`、`VIDEO_NAME=Claude_Simon_zh`
- 第 3 步：肖像下载——images.txt 有 URL 直接取（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 则改用 Commons `Special:FilePath` 或 Wikipedia REST API `page/summary` 查 infobox 原图名；仍失败用装饰圆占位，图注注明「肖像暂缺」

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nouveau roman | 新小说 | 与 Robbe-Grillet/Butor 并称的运动，但 Simon 保留叙事与人物感 | 新小说页 |
| 1 | autobiographical novel | 自传体小说 | 约 20 部著作的密集自传底色 | 全篇 |
| 2 | war narrative | 战争叙事 | 几乎全部作品的核心主题：一战/二战/西班牙内战对照 | 战争页 |
| 3 | time and memory | 时间与记忆 | 获奖理由核心；家族史=个体「存在于历史中」 | 时间页 |
| 4 | modernism | 现代主义 | 与 Proust/Faulkner 的明确承传（断裂时间线、自由间接引语） | 现代主义页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Rea Simon | 无向 | 妻子，2017 年卒 |
| advisor-student | André Lhote | direction: advisor | 在其画室修绘画课程 |
| influence | Marcel Proust | direction: 影响者 | 明载 clear influence；长句、山楂树篱互文（《佛兰德公路》中 haie d'aubépines 呼应《追忆》） |
| influence | William Faulkner | direction: 影响者 | 明载 clear influence；断裂时间线、自由间接引语、*L'Acacia* 借《喧哗与骚动》日期手法 |
| colleague | Alain Robbe-Grillet | 无向 | 新小说运动并称者 |
| colleague | Michel Butor | 无向 | 新小说运动并称者 |
| colleague | Raoul Dufy | 无向 | 佩皮尼昂避难时期画家友人 |
| colleague | Jean Lurçat | 无向 | 佩皮尼昂避难时期画家友人 |
| colleague | Joan Miró | 无向 | 为其 23 幅画作著文（*Femmes*，1966） |
| colleague | Jean Ricardou | 无向 | Cerisy 研讨会主讲；1974 专题 Claude Simon: analyse, théorie；1980 《Georgiques》写作工坊 |
| controversy | Christopher Hitchens | 无向 | Hitchens 在《Orwell's Victory》批评其对西班牙内战奥威尔叙述的解构（该批评本身又被史家 Webster 批评） |

### 第 5 步：设计配色 【人物专属】

- **气质**：画布的层积、时间的灰蓝、葡萄园的沉绿
- **配色**：主色 `#1E4E79`（预分配莫尼黑蓝）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 新小说 — 深蓝 `#1E4E79`
  - `badgeB` 战争叙事 — 铁灰红 `#8B3A3A`
  - `badgeC` 时间与记忆 — 琥珀 `#E07B30`
  - `badgeD` 绘画与写作 — 玫瑰 `#C4204F`
- **背景母题**：横贯画面的细长色带（长句的可视化）+ 稀疏马匹剪影/葡萄藤弧线；避免政治符号（国际纵队、121 宣言仅文字客观提及）。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 新小说的画家 / Claude Simon 1913–2005 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 生卒、出生地马达加斯加、父亲阵亡、教育、军旅、荣誉、核心领域
03  核心创作概览 — 新小说 / 战争叙事 / 时间与记忆 / 家族史
04  早年：从塔那那利佛到佩皮尼昂 (1913–1936) — 父亲阵亡、Stanislas、Lhote 画室、21 岁遗产独立
05  骑兵与西班牙内战 (1936–1939) — 国际纵队、开始写作、1937 欧游
06  1940：默兹河与逃脱 — 被俘/逃脱/抵抗运动；Dufy 与 Lurçat
07  早期小说与转向 (1946–1958) — Le Tricheur → Le Vent / L'Herbe
08  代表作页：《佛兰德公路》(1960)（引文框/意象图式替代公式框）— 骑兵在机械化战争中的荒诞
09  新小说与更远的现代主义 — Robbe-Grillet/Butor 并称 vs Proust/Faulkner 承传
10  时间与家族史 — Histoire / Les Géorgiques / L'Acacia（非顺序日期替代章节标题）
11  绘画与写作 — Miró 著文、Orion aveugle、"viticulteur" 的自我定位
12  荣誉与认可 — 1961 L'Express · 1967 Médicis · 1973 UEA 荣誉博士
13  1985 诺贝尔奖 — citation 官方原句引文框
14  遗产：新小说的画家视角
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

**Simon 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方原句 "who in his novel combines the poet's and the painter's creativeness with a deepened awareness of time in the depiction of the human condition"；中译从 CITATION_ZH 原样取，禁止改写 |
| 出生地 | 塔那那利佛（马达加斯加），勿写成法国本土；父亲是「职业军官、死于一战」，勿写具体战役 |
| 121 宣言 | 1960 支持阿尔及利亚独立的《121 宣言》联署，**客观一句带过，不展开政治叙事** |
| 国际纵队 | 1936 志愿参加国际纵队是 page.md 事实；Hitchens 争议只按第 4.5 步口径一句呈现，双方批评并置，**不站队、不评价** |
| viticulteur | 「职业登记为葡萄种植者」是 page.md 明载轶事，勿写成幽默段子或过度阐释 |
| 新小说归属 | 与 Robbe-Grillet/Butor 并称 nouveau roman，但 page.md 强调 Simon 保留叙事与人物感、更近 Proust/Faulkner——勿写成「新小说代表旗手」单一定性 |
| Dufy/Lurçat | 两人是「朋友」（friends），入库 colleague，note 勿写「师承」或「合作画室」 |
| 无载禁写清单 | 具体恋情、子女、诺贝尔演讲内容、Robbe-Grillet 的私人交往细节——page.md 均无载，一律禁写 |
| 作品年份 | *Le Tricheur* 战前动笔 1946 出版；*La Route des Flandres* 1960（L'Express 奖 1961）勿混 |
| 三种拼写 | Tananarive/Antananarivo、La Route des Flandres（书名单数 des）按 page.md 原文 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| nouveau roman | 新小说 | 勿译「新浪漫主义」 |
| La Route des Flandres | 《佛兰德公路》 | 通行中译名 |
| analepsis | 倒叙/闪回 | 叙事学术语 |
| free indirect speech | 自由间接引语 | Faulkner 影响的载体 |
| haie d'aubépines | 山楂树篱 | Proust 互文细节 |
| viticulteur | 葡萄种植者 | 本人坚持的职业身份 |
| Prix Médicis | 美第奇奖 | 1967，*Histoire* |
| Manifesto of the 121 | 121 人宣言 | 1960，客观表述 |
| Cerisy | 瑟西研讨会 | Ricardou 主持的专题 |
| Bibliothèque de la Pléiade | 七星文库 | 2006/2013 两卷 |

---

### 第 9 步：执行终检清单 【模板通用】

- [ ] 页数与第 6 步序列一致（`pdftoppm` 逐页目检；出 mp4 后核时长）
- [ ] 获奖理由 EN 原句与 CITATION_ZH 中译逐字核对（含标点）
- [ ] 生卒/享年三处一致（封面、身份页、结尾页）
- [ ] 溢出：vbox ≤10pt、hbox ≤50pt；引文框不破行
- [ ] yaml 关系与第 4.5 步表逐行一致；note 无裸冒号/引号头
- [ ] 品牌口径：结尾页底部 `OpenMathAI`，引号半角

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions（预分配）
- **风格**: 温和 / 陪伴感 / 坚韧低回
- **匹配理由**:
  - "陪伴" 匹配 Simon 的写作本质 —— 从战场幸存到晚年仍写 *Le Tramway*，写作是与战争记忆一生同行的行为
  - "温和低回" 匹配其克制的文风 —— 长句缓行、括号回旋，情绪从不外露
  - 避开本批已用曲（Tragedy/Eternals/Cinematic Experience/New Lands），无撞曲
- **备选** (未采用): ★★ The Flow of Time（时间意识主题直配，但受众偏低且本批避免曲名直白化）；★ SEA（克制辽阔，电影感略弱）
- **本地路径**: `music_audio/alex-productions/` 下 With Me 对应 wav（复制到 `literature/presentations/20th_century/Claude_Simon/With Me.wav`）
- **时长**: 以实际文件为准，ffmpeg `-shortest` 自动对齐

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：引语只用 page.md 英文原句；无载禁写；关系表与 yaml 完全一致。**
