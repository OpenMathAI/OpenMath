# Frederick Sanger（弗雷德里克·桑格）立传提示词

> qid=Q151564 · 1918-08-13 – 2013-11-19 · 英国生物化学家 · 20 世纪 · 诺贝尔化学奖（1958、1980）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Frederick_Sanger/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Frederick_Sanger.jpeg` 已就位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace 生命字母表的读者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「序列 / 字母」母题——离散圆点暗示碱基/氨基酸的线性排列。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Frederick Sanger（中文惯称：弗雷德里克·桑格；头衔缩写 OM CH CBE FRS FAA）
- **生卒**：1918-08-13 生于英格兰格洛斯特郡 Rendcomb 村 → 2013-11-19 逝于剑桥 Addenbrooke's Hospital（睡梦中），享年 95
- **国籍**：United Kingdom（英国）
- **身份**：生物化学家（biochemist；两次诺贝尔化学奖得主）
- **家庭**：次子；父 Frederick Sanger 为全科医生，曾任圣公会驻华医疗传教士，因健康回国，两个儿子出生后改信贵格会（Quaker）；母 Cicely（娘家姓 Crewdson）为棉纺厂主之女、有贵格会背景但非贵格会信徒；兄 Theodore 大一岁、妹 Mary 小五岁。1940 年 12 月娶 Margaret Joan Howe（Newnham College 经济学，经剑桥科学家反战小组结识；勿与美国节育先驱 Margaret Sanger 混淆），2012 年妻先逝；三子女 Robin（1943）、Peter（1946）、Sally Joan（1960）
- **教育轨迹**：
  - 1927（9 岁）入贵格会预备学校 The Downs School（Malvern 附近）
  - 1932（14 岁）入 Bryanston School（道尔顿制；化学老师 Geoffrey Ordish 唤醒其科学志向）
  - 1935 赴德国 Schule Schloss Salem 交换（每天以诵读《我的奋斗》开始——终生难忘）
  - 1936 入 St John's College, Cambridge 读自然科学（父亲同一学院）；Part II 生物化学一等荣誉
- **导师**：Albert Neuberger（博士导师；最初导师 N.W. "Bill" Pirie 约 1 个月后离开）
- **博士**：1943，《The metabolism of the amino acid lysine in the animal body》（考官 Charles Harington、Albert Charles Chibnall）
- **研究领域**：生物化学——蛋白质测序、RNA 测序、DNA 测序、分子生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **贵格会家庭（1918）**：医生之家、贵格会教育——谦逊、和平主义与对真理的执着的根源。
2. **良心拒服兵役（1939–1940）**：和平主义者、Peace Pledge Union 成员，获无条件豁免；在贵格中心受社会救济训练、短暂任医院勤务。
3. **剑桥转折（1936–1943）**：物理与数学吃力，转向生理学与生物化学（Hopkins 创立的新系）；剑桥头两年父母先后因癌去世（父 60、母 58）。
4. **桑格试剂 FDNB（1943–1945）**：1-氟-2,4-二硝基苯标记多肽链 N 端氨基，部分水解后二维纸层析（电泳 × 层析）分离肽段——"指纹图谱"。
5. **胰岛素 A/B 链序列（1951/1952）**：B 链（1951，与 Tuppy）、A 链（1952，与 Thompson）——证明蛋白质具有确定的化学组成与独特序列，颠覆"蛋白质无定形"的旧观念。
6. **二硫键定位（1955）**：与 Ryle、Smith、Kitai 确定牛胰岛素 3 个二硫键（A6–A11 链内；A7–B7、A20–B19 链间）。
7. **1958 诺贝尔化学奖**：官方理由 "for his work on the structure of proteins, especially that of insulin"——为 Crick 的 sequence hypothesis（序列假说）奠定实证基础。
8. **MRC 与 LMB（1951/1962）**：1951 起任 MRC 外部研究员；1962 迁入新建 LMB 顶层，任蛋白质化学部主任。
9. **RNA 测序（1951–1967）**：与 Marcker 发现甲酰甲硫氨酸 tRNA（1964，细菌翻译起始）；tRNA 竞赛输给 Holley（1965，77 核苷酸丙氨酸 tRNA）；1967 组里测定 E. coli 5S rRNA（120 核苷酸）。
10. **Plus/Minus 法与 φX174（1975–1977）**：与 Coulson 发表"加减法"（一次约 80 核苷酸）；测定噬菌体 φX174 全部 5,386 核苷酸——第一个被完整测序的 DNA 基因组，意外发现基因编码区相互重叠。
11. **双脱氧链终止法（1977）**：ddNTP（缺 3'-OH）随机掺入终止延伸，四管反应 + 电泳读出阶梯——快速、准确、可规模化；用于人线粒体 DNA（16,569 bp）与噬菌体 λ（48,502 bp），最终奠定人类基因组计划的测序基础。1977 年 PNAS 论文到 2010 年 10 月已被引用超过 64,000 次（ISI）。
12. **1980 诺贝尔化学奖**：与 Walter Gilbert、Paul Berg 共享；他是仅有的三位**同一类别**两度诺奖者之一（另两位 Bardeen 物理、Sharpless 化学），也是仅有的两位两度化学奖得主之一（另一位 Sharpless）。
13. **桑格规则与谦逊**："技术效率提升两三倍，一整类全新的实验就被打开"；拒绝爵位（不想被称 "Sir"），1986 年却接受在世仅 24 人的 Order of Merit；自述 "just a chap who messed about in a lab"；门生 Rodney Porter（1972）与 Elizabeth Blackburn（2009）皆获诺奖；1992 年 Sanger Centre 以他命名（"It had better be good."）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#1E3A5F` | 分子生物学的精确与深度（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（蛋白质测序 badgeProt） | `#2E5A9E` | 蓝胰岛素序列 / 指纹图谱 |
| 分类色 2（DNA 测序 badgeDNA） | `#1B7A43` | 绿双脱氧法 / φX174 |
| 分类色 3（RNA 测序 badgeRNA） | `#D97B29` | 琥珀 5S rRNA / 起始 tRNA |
| 分类色 4（分子生物学 badgeCentral） | `#C0395B` | 玫瑰序列假说 / 中心法则 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「序列 / 字母」的线性排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（已软链至本目录 `Timeless.wav`）
- **风格**：沉稳 / 纪录片 / 谦逊的长期主义
- **匹配理由**：
  - "长期纲领" 匹配桑格贡献的本质——两次诺奖之间横跨蛋白质、RNA、DNA 测序，是一以贯之的「把生命读成字母」的纲领
  - "沉稳" 匹配其气质——自述 "just a chap who messed about in a lab" 的极度谦逊，安静革命胜过英雄史诗
  - "纪录片" 匹配传记叙事——贵格会医生之子 → 剑桥 → 胰岛素 → 双脱氧法 → 两度诺奖 → Sanger Institute
- **时长**：128 秒 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 生命字母表的读者 / Frederick Sanger 1918–2013 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  桑格的一生 — 高斯式时间线（10 节点：1918→1936→1943→1951→1955→1958→1962→1977→1980→2013）
04  早年：贵格会医生之子 (1918–1935) — 表格「时间|事件|结果」
05  剑桥：从物理转向生物化学 (1936–1943) — 表格「时间|事件|结果」
06  胰岛素测序 (1943–1955) — 表格「问题|方法|结果」+ 公式框：牛胰岛素 A/B 链一级序列
07  RNA 测序 (1951–1967) — 表格「挑战|方法|结果」
08  DNA 测序：加减法与 φX174 (1971–1977) — 表格「问题|方法|结果」+ 公式框：φX174 = 5,386 nt
09  双脱氧法 (1977–1980) — 表格「问题|方法|结果」+ 公式框：链终止原理 · 1980 诺奖
10  门生与传承 — 表格「人物|方向|结果」（Porter 1972 / Blackburn 2009 / Brownlee）
11  荣誉与谦逊 — 高斯式「类别|代表|意义」表格（含 itemize 荣誉清单）+ 拒爵位
12  Sanger Institute — 高斯 FFT 页式流程图（1992 创办 → 1993 揭幕 → HGP → 今日）
13  遗产：测序改变世界 — 四分类遗产盒 + 公式框：桑格规则 + 64,000 次引用
14  结尾 — 「生命之书，从此可以被一页页读出。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 两度获奖表述 | 仅有的三位**同一类别**两度诺奖者之一（Bardeen 物理、Sharpless 化学）；1958 **独享**、1980 与 Gilbert/Berg **共享**；勿写"两次独享" |
| 1958 诺奖理由 | 官方措辞 "for his work on the structure of proteins, especially that of insulin"（强调蛋白质结构/胰岛素），勿泛化成"发明蛋白质测序" |
| 1980 诺奖理由 | "for their contributions concerning the determination of base sequences in nucleic acids"；Berg 是重组 DNA、Gilbert 是化学降解法、桑格是双脱氧法——三者勿混 |
| 结构 vs 序列 | 桑格证明的是蛋白质有**确定的一级序列（氨基酸顺序）**；三维结构是后来 X 射线晶体学（Perutz、Kendrew）的功劳，勿混淆 |
| A/B 链年份 | **B 链 1951**（与 Tuppy）、**A 链 1952**（与 Thompson）——勿写反 |
| 二硫键 | 1955 年确定 **3 个**：A6–A11（链内）、A7–B7、A20–B19（链间）——勿写 2 个 |
| 导师变更 | 博士最初导师 N.W. "Bill" Pirie（约 1 个月后离开）→ Albert Neuberger；勿只写一人 |
| 拒服兵役 | **良心拒服兵役者**，获无条件豁免，战时做贵格中心受训与医院勤务——勿写"服役" |
| 姓名混淆 | 与美国节育先驱 Margaret Sanger 无关（其妻是 Margaret Joan Howe）；Sanger's rule 勿与 Terence Sanger's rule（Oja's rule 相关）混淆 |
| 荣誉细节 | **拒绝爵位**（"A knighthood makes you different, doesn't it, and I don't want to be different."），1986 年接受 Order of Merit（在世仅 24 人）——勿写"被封爵" |
| 去世地 | 2013-11-19 逝于剑桥 Addenbrooke's Hospital（睡梦中），享年 95——勿与出生地 Rendcomb 混淆 |
| φX174 | **第一个被完整测序的 DNA 基因组**（5,386 nt）并发现基因重叠——勿写"第一个被测序的生物" |
| tRNA 竞赛 | 桑格**输给** Robert Holley（1965 测定 77 核苷酸丙氨酸 tRNA）；5S rRNA（120 nt）是 1967 年由 Brownlee/Sanger/Barrell 测定——勿写桑格"第一个测 tRNA" |
| 门生入库 | 正文 infobox 的 Doctoral students 仅 **George Brownlee、Elizabeth Blackburn、Rodney Porter** 三人；Wikidata 另含 Gerald Edelman、Tom Maniatis 但正文无——**不予入库** |
| 引用数 | "超 64,000 次"须注明：ISI 数据库、截至 2010 年 10 月、指 1977 年 PNAS 双脱氧法论文 |
| 世界宪法签署 | 属边缘轶事（World Constituent Assembly 签署人），建议略过 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q151564 | ✅ |
| name_zh | 弗雷德里克·桑格 | ✅ |
| name_en | Frederick Sanger | ✅ |
| birth_date | 1918-08-13 | ✅ |
| death_date | 2013-11-19 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：protein sequencing / DNA sequencing / RNA sequencing / molecular biology，带 rank） | ✅ |
| has_biography | 1 | ✅ 已置 1 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Albert Neuberger | 师→生（博士导师） | 1940 接手 Sanger 博士课题（Pirie 旋即离职） |
| advisor-student | Charles Chibnall | 师→生（课题指路人 / 博士考官） | 建议 Sanger 研究胰岛素氨基 |
| colleague | Alan Coulson | 无向 | 长期合作者，Plus/Minus 与双脱氧法共同作者 |
| colleague | Kjeld Marcker | 无向 | 1964 共同发现甲酰甲硫氨酸 tRNA |
| co-honored | Walter Gilbert / Paul Berg | 无向 | 1980 诺奖共同得主 |
| competitor | Robert Holley | 无向 | tRNA 测序竞赛对手（Holley 1965 先发表，1972 诺奖） |
| other | John Sulston | 无向 | Sanger Centre 创始主任，请求以 Sanger 命名 |

**门生（Sanger → 学生，源自本地 Wikipedia 正文 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rodney Porter | Sanger → 学生 | 1947 首位研究生；1972 诺奖生理学或医学奖 |
| advisor-student | Elizabeth Blackburn | Sanger → 学生 | 1971–1974 博士；2009 诺奖生理学或医学奖 |
| advisor-student | George Brownlee | Sanger → 学生 | 共同测定 5S rRNA |

> Wikidata `doctoral_student` 另含 Gerald Edelman、Tom Maniatis，但正文 infobox 无此二人，**不予入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1958，独享；1980，与 Gilbert/Berg 共享）
- Corday–Morgan Medal（1951）
- Fellow of the Royal Society，FRS（1954）
- Commander of the Order of the British Empire，CBE（1963）
- Royal Medal（1969）
- Canada Gairdner International Award（1971）
- William Bate Hardy Prize（1976）
- Copley Medal（1977）
- G.W. Wheland Award（1978）
- Louisa Gross Horwitz Prize（1979）
- Albert Lasker Award for Basic Medical Research（1979）
- Companion of Honour，CH（1981）
- Corresponding Member of the Australian Academy of Science（1982）
- Order of Merit，OM（1986；在世成员仅 24 人；曾拒绝爵位）
- ABRF Award（1994）；Golden Plate Award（2000）；Citation for Chemical Breakthrough Award（2016，ACS 化学史分会）
- 斯特拉斯堡大学荣誉博士；Croonian Medal and Lecture

## 9. 机构清单

- 教育：The Downs School（1927–1932）、Bryanston School（1932–1935）、Schule Schloss Salem（1935 交换）、St John's College, University of Cambridge（1936–，BA、PhD 1943）
- 任职：Cambridge 生物化学系（1943 加入 Chibnall 组；1944–1951 Beit Memorial Fellowship）；MRC 外部研究员（1951–）；LMB 蛋白质化学部主任（1962–）；1983 年 65 岁退休，居于剑桥郊外 Swaffham Bulbeck "Far Leys"
- 命名机构：Sanger Centre（1992 年由 Wellcome Trust 与 MRC 创办，现 Wellcome Sanger Institute；1993-10-04 由桑格亲自揭幕，初始员工不足 50 人）

## 10. 终审清单

- [x] 生卒 1918-08-13 / 2013-11-19，享年 95，出生地 Rendcomb、去世地剑桥 Addenbrooke's Hospital
- [x] 1958 独享 / 1980 共享（Gilbert、Berg）表述准确；"同类别两度仅三人"表述准确
- [x] B 链 1951、A 链 1952；二硫键 3 个（A6–A11、A7–B7、A20–B19，1955）
- [x] 博士导师 Pirie→Neuberger 表述准确；良心拒服兵役表述准确
- [x] φX174 = 第一个完整测序的 DNA 基因组（5,386 nt）+ 基因重叠
- [x] tRNA 竞赛"输给 Holley"表述准确；5S rRNA 120 nt（1967）
- [x] 拒绝爵位、1986 接受 OM（在世 24 人）表述准确
- [x] 引用数注明"ISI、截至 2010-10、1977 PNAS 论文"
- [x] 引语全部可在本地 Wikipedia 原文找到（1958/1980 获奖理由、"It had better be good."、"A knighthood makes you different..."、"just a chap who messed about in a lab"、桑格规则原句）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Frederick_Sanger/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/Frederick_Sanger.jpeg` 已就位（Wikipedia 1960 年照片）
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由两条、Sulston 请求、拒爵位、桑格规则）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与数学家侧（高斯）及化学家侧既有格式对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 中 `BIOGRAPHIES_DONE` / `REVIEWS_DONE` 均已含 Frederick Sanger（总名单 ✅/✅）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
