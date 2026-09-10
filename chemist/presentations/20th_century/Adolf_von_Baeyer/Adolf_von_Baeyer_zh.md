# Adolf von Baeyer（阿道夫·冯·拜尔）立传提示词

> qid=Q57078 · 1835-10-31 – 1917-08-20 · 德国化学家 · 1905 年诺贝尔化学奖
> 诺奖官方理由（总名单措辞）：表彰他通过对有机染料和氢化芳香族化合物的研究，推动有机化学和化学工业的发展
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Adolf_von_Baeyer/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**——表格语义化 tabularx + 公式展示框 + 时间线页 + 身份信息页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 URL 见 images.txt：`Baeyer.jpg`，执行阶段下载至 `images/`）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 靛蓝的驯服者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色（靛蓝）+ 强调色（诺贝尔金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「染料 / 浸染」母题——蓝色系大圆如染缸中晕开的靛蓝。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（靛蓝 C₁₆H₁₀N₂O₂、Baeyer 张力角 109°28′ − 内角/2 等）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Johann Friedrich Wilhelm Adolf von Baeyer（中文惯称：阿道夫·冯·拜尔；一生多以 Adolf 行世，"von" 为 1885 年封爵所加）
- **生卒**：1835-10-31 生于柏林（普鲁士王国）→ 1917-08-20 逝于巴伐利亚施塔恩贝格（Starnberg，德意志帝国），享年 81
- **国籍**：German Empire（德国；1885 年获巴伐利亚王国世袭贵族身份）
- **身份**：化学家、大学教师（organic chemist；1905 年诺贝尔化学奖得主）
- **家庭**：父 Johann Jacob Baeyer 为著名大地测量学家、普鲁士皇家陆军上尉（后官至中将）；母 Eugenie（娘家姓 Hitzig，1807–1843）为 Julius Eduard Hitzig 之女、原犹太 Itzig 家族成员，婚前改宗，在生幼妹 Adelaide 时难产去世，拜尔幼年丧母。父母在其出生时均为路德宗信徒。四妹两兄。教父二人为诗人 Adelbert von Chamisso 与天文学家 Friedrich Wilhelm Bessel。1868 年娶 Adelheid（Lida）Bendemann（世交之女），育三子女：Eugenie、Hans、Otto
- **教育轨迹**：
  - Friedrich Wilhelm Gymnasium（柏林）：化学教师聘其为助手；1853 年中学毕业
  - 1853 入 Friedrich Wilhelm University of Berlin 读物理与数学；服兵役中断至 1856
  - 1856 入海德堡大学，欲师从 Robert Bunsen 学化学；与 Bunsen 争执后改投 August Kekulé
  - 1858 返回柏林完成博士；后随 Kekulé 赴根特大学（Ghent）
- **导师**：August Kekulé（博士导师；最初属意 Robert Bunsen，因争执改投）
- **博士论文**：*De arsenici cum methylo conjunctionibus*（1858，二甲基胂基氯 / cacodylic chloride）
- **研究领域**：有机化学——有机染料（靛蓝、酞类）、氢化芳香族化合物、尿酸衍生物、张力学说、环状化合物命名法

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **13 岁的终身之约（1848）**：13 岁生日当天花两塔勒买下一块靛蓝，开启第一批染料实验——此后一生与靛蓝纠缠到底。
2. **神童实验室（约 1844–1848）**：9 岁在柏林开始化学实验；三年后合成一种此前未知的化合物——铜钠复碳酸盐；童年在外祖父 Müggelsheim 农场做植物营养实验。
3. **师承抉择（1856–1858）**：海德堡投奔 Bunsen，因争执改投 Kekulé；1858 随 Kekulé 完成博士（二甲胂基氯），并随其转赴根特——Kekulé 学派的核心成员。
4. **慕尼黑讲席（1875）**：接替 Justus von Liebig 出任慕尼黑大学化学教授——德国化学的最高教席之一，此后终身执教。
5. **巴比妥酸（1864）**：尿酸衍生物研究（1860 年起）中 发现巴比妥酸——barbiturates（巴比妥类药物）的母体化合物。
6. **吲哚（1866/1869）**：1866 年发表吲哚的首次合成，1869 年首先提出吲哚的正确结构式。
7. **1871 双丰收——酚酞**：苯酐与两当量苯酚在酸性条件下缩合制得酚酞（名称即由此而来）。
8. **1871 双丰收——荧光素**：同一年首次人工获得荧光素（从苯酐与间苯二酚合成，他命名为 "resorcinphthalein"；"fluorescein" 一词 1878 年才开始使用）。
9. **酚醛树脂前身（1872）**：苯酚与甲醛实验所得树脂状产物——后来 Leo Baekeland 商业化 Bakelite（电木）的前身。
10. **靛蓝的合成与阐释**：靛蓝的合成与结构描述为其 Chief achievement，1881 年凭此获皇家学会戴维奖章。
11. **张力学说（Spannung）**：三键的"张力"理论 + 小碳环的 Baeyer 张力学说——page.md 明言 Baeyer strain theory 是 "(which granted him the Nobel Prize)" 的获奖工作之一。
12. **Von Baeyer 命名法**：环状化合物的命名体系，后被扩展并采纳为 IUPAC 有机命名法的一部分——写进国际规则的化学语言。
13. **荣誉与身后（1885–2009）**：1885 年 50 岁生日由巴伐利亚国王路德维希二世授予世袭贵族 "von"；1905 年独享诺贝尔化学奖；执教至去世前一年仍是世界最著名的有机化学教师之一；1911 年起每年颁发 Adolf von Baeyer 奖章；2009 年月球环形山 Von Baeyer 以他命名。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#283593` | 靛蓝染料之本色——毕生母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（靛蓝与染料 badgeIndigo） | `#3F51B5` | 亮靛蓝靛蓝合成 / 染料工业 |
| 分类色 2（酞类荧光 badgePhthalein） | `#1B7A43` | 荧光绿酚酞 / 荧光素 |
| 分类色 3（张力学说与命名 badgeStrain） | `#0E7C7B` | 青绿环张力 / Von Baeyer 命名法 |
| 分类色 4（师承与荣誉 badgeLegacy） | `#C0395B` | 玫瑰慕尼黑学派 / 荣誉序列 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「染料 / 浸染」——蓝色晕染如靛蓝在染缸中扩散。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions
- **风格**：时间感 / 纪录片 / 历史纵深
- **匹配理由**：
  - "时间感" 匹配拜尔的一生跨度——1835 至 1917 横跨 19、20 两个世纪，从 13 岁买靛蓝到 81 岁离世，一条贯穿 70 余年的单线母题
  - "纪录片" 匹配其叙事气质——不是爆发式天才，而是一个世纪的德国化学建制本身（根特→柏林→斯特拉斯堡→慕尼黑）
  - "历史纵深" 匹配其遗产——命名法进入 IUPAC、奖章每年颁发、2009 年月球环形山，时间越长越见其重
- **时长**：见 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`；15 页 × 7 秒 ≈ 105 秒，超出则 ffmpeg `-shortest` 自动对齐
- **注意**：wav 复制在执行立传阶段进行，本阶段不复制任何音频文件

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 靛蓝的驯服者 / Adolf von Baeyer 1835–1917 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  拜尔的一生 — 高斯式时间线（10 节点：1835→1853→1858→1860→1871→1875→1881→1885→1905→1917）
04  早年：测量学家之子与靛蓝之约 (1835–1858) — 表格「时间|事件|结果」
05  师承 Kekulé：从海德堡到根特 (1856–1860) — 表格「时间|事件|结果」
06  靛蓝与染料 (1860s–1880s) — 表格「问题|方法|结果」+ 公式框：靛蓝 C16H10N2O2 · 吲哚结构
07  酞类染料 (1871) — 表格「问题|方法|结果」+ 公式框：酚酞缩合（苯酐 + 2 苯酚）
08  尿酸衍生物与巴比妥酸 (1860s–) — 表格「问题|方法|结果」+ 公式框：巴比妥酸
09  张力学说与命名法 (1880s–) — 表格「问题|方法|结果」+ 公式框：Baeyer 张力角 109°28′ − 内角/2
10  酚醛树脂前身与工业化学 (1872) — 表格「时间|事件|结果」（Bakelite 前身）
11  慕尼黑学派与门生 — 表格「人物|方向|结果」（Emil Fischer 1902 诺奖 / Willstätter 1915 诺奖等）
12  荣誉与贵族封号 — 高斯式「类别|代表|意义」表格（1881 戴维 / 1903 李比希 / 1905 诺贝尔 / 1885 封爵）+ 拒绝项核查
13  遗产：写进 IUPAC 的名字 — 四分类遗产盒 + 公式框：Von Baeyer 命名法 · 1911 年起年度奖章 · 2009 月球环形山
14  结尾 — 金句（须与 page.md 事实相容的原创概括，不杜撰引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 与拜耳公司勿混淆 | Bayer AG 得名于创始人 Friedrich Bayer，与 Adolf von Baeyer **无关**；拼写勿混（Baeyer ≠ Bayer）。page.md 全文无涉该公司 |
| 1905 诺奖理由 | 官方措辞（总名单）「表彰他通过对有机染料和氢化芳香族化合物的研究，推动有机化学和化学工业的发展」；英文 "in recognition of his services in the advancement of organic chemistry and the chemical industry, through his work on organic dyes and hydroaromatic compounds"（page.md 有载）；1905 **独享**，无共享者；勿泛化为"因发明靛蓝染料获奖" |
| hydroaromatic 译法 | 氢化芳香族化合物——勿误译为"芳香族氢化物"或"芳香氢化合物" |
| 张力学说与诺奖关系 | page.md 称 Baeyer strain theory "(which granted him the Nobel Prize)"，但获奖理由原文是染料 + 氢化芳香族——表述为"张力学说属其获奖工作范围"，勿倒置为"因张力学说获奖" |
| 反应名有载范围 | Baeyer–Drewson 靛蓝合成、Baeyer–Emmerling 吲哚合成、Baeyer–Villiger 氧化、Baeyer's reagent 仅见于 infobox "Known for" 条目名，正文未展开——Beamer 中只写反应名与"以他命名"，**不得展开任何正文无载的机理/年份细节** |
| 荧光素命名 | 他将自己的产物命名为 "resorcinphthalein"；"fluorescein" 一词 **1878 年**才开始使用——勿写"他命名了 fluorescein" |
| 荣誉清单年份噪声 | page.md 荣誉清单载 "1989: International Member of the US National Academy of Sciences"——生于 1835 卒于 1917，1989 显系来源笔误，**此条不写**；另 1884 American Academy 两行重复、1885 "foreign member of the Royal Society" 链接误指 Royal Society of Chemistry——按文字表述取 Royal Society |
| metadata 冲突①去世地 | metadata place_of_death 为 ["Starnberg", "Munich"]，page.md 仅 Starnberg——**以 Starnberg 为准**（正文两处：infobox 与 Personal life 均为 Starnberg） |
| metadata 冲突②学生名单 | metadata doctoral_student 11 人（含 Zeidler、Perkin、Willstätter 等）与 page.md infobox 6 人（Emil Fischer、Nef、Villiger、Liebermann、Gräbe、Karl Andreas Hofmann）不一致——入库策略见 §7；Willstätter 有其本人本地页面 doctoral_advisor=[Alfred Einhorn, Adolf von Baeyer] 交叉印证 |
| 1875 接任教席 | 接替 Justus von Liebig 出任慕尼黑化学教授——page.md 只说 "succeeded"，勿添加 Liebig 卒年或交接细节（无载禁写） |
| 巴比妥酸 | 1864 年发现的是 barbituric acid（巴比妥类药物的母体化合物）——勿写"发明/合成了巴比妥类药物" |
| 酚醛树脂 | 1872 年产物只是 Bakelite 的 "precursor"——勿写"发明电木" |
| 封爵性质 | 1885 年 50 岁生日由巴伐利亚国王路德维希二世授予**世袭贵族** "von"——勿写成英国式"册封爵士"；出生名无 von |
| 教职身份 | 从未获"英国皇家学会法拉第讲座"之类荣誉——page.md 无载，禁止添加（任务提示中 RSC 法拉第讲座一项**无载禁写**） |
| 引语纪律 | page.md 几乎无 Baeyer 原话——**禁止杜撰任何"拜尔名言"**；1905-12-10 诺奖致辞是皇家科学院院长 Anders Lindstedt 所作，勿写"拜尔的诺奖演讲" |
| 早年化学起点 | 12 岁左右合成的是"此前未知的铜钠复碳酸盐"——勿夸大为"首次合成某化合物"；靛蓝购买时间表述为"13 岁生日"（page.md 原文 on his 13th birthday） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57078 | ✅ |
| name_zh | 阿道夫·冯·拜尔 | ✅（与总名单一致） |
| name_en | Adolf von Baeyer | ✅ |
| birth_date | 1835-10-31 | ✅ |
| death_date | 1917-08-20 | ✅ |
| nationality | German Empire | ✅ |
| primary_occupation | chemist（兼 university teacher） | ✅ |
| field_of_work | organic chemistry（person_field 细分建议：organic dyes / indigo synthesis / strain theory / nomenclature，带 rank） | ✅ |
| has_biography | 执行立传并入库后置 1 | 🔲 |

## 7. 社会关系入库清单

**师长 / 同事 / 前任**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | August Kekulé | 师→生（博士导师） | 海德堡改投；1858 随其返柏林完成博士并赴根特 |
| advisor-student | Robert Bunsen | 师→生（最初导师） | 1856 海德堡初投，因争执改投 Kekulé |
| other | Justus von Liebig | 无向 | 1875 接替其慕尼黑化学教授讲席 |
| other | Leo Baekeland | 无向 | 1872 酚醛树脂产物为 Bakelite 前身 |

**门生（Baeyer → 学生）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Emil Fischer | Baeyer → 学生 | infobox 有载；1902 诺贝尔化学奖 |
| advisor-student | Victor Villiger | Baeyer → 学生 | Baeyer–Villiger 氧化以二人命名 |
| advisor-student | John Ulric Nef | Baeyer → 学生 | infobox + metadata 一致 |
| advisor-student | Carl Theodore Liebermann | Baeyer → 学生 | infobox + metadata 一致 |
| advisor-student | Carl Gräbe | Baeyer → 学生 | **仅见 page.md infobox**（metadata 无） |
| advisor-student | Karl Andreas Hofmann | Baeyer → 学生 | **仅见 page.md infobox**（metadata 无） |
| advisor-student | Richard Willstätter | Baeyer → 学生 | **仅 metadata**，但 Willstätter 本人本地页面 doctoral_advisor 有 Baeyer，交叉印证可入库 |
| advisor-student | Othmar Zeidler / William Henry Perkin / Paul Friedländer / Rudolf Pummerer / Arthur Weinberg / Christian Stolz | Baeyer → 学生 | **仅 metadata**，正文无载——入库时 note 注明来源，或暂缓 |

> Wikidata `doctoral_student` 与 page.md infobox 名单不一致（见 §5）；入库以两处一致的优先，单源者逐条注明来源。正文（page.md）无载的关系不虚构任何合作细节。

## 8. 奖项清单

- Nobel Prize in Chemistry（1905，独享）
- Davy Medal（1881，皇家学会，因靛蓝工作）
- Liebig Medal（1903，德国化学会）
- Elliott Cresson Medal（1912）
- Order Pour le Mérite for Sciences and Arts（1895）
- Fellow of the American Academy of Arts and Sciences（1884；同年 Prussian Academy of Sciences）
- Foreign member of the Royal Society（1885）
- Honorary member of the Manchester Literary and Philosophical Society（1892）
- International Member of the American Philosophical Society（1910）
- Bavarian Maximilian Order for Science and Art（仅 metadata 有载，年份无载，注来源）
- International Member of the US National Academy of Sciences（page.md 载 1989 系笔误，**不写**）
- Adolf von Baeyer Medal：1911 年起每年颁发（以他命名的奖章，非其本人获奖）

## 9. 机构清单

- 教育：Friedrich-Wilhelms-Gymnasium（中学，任化学教师助手；1853 毕业）；Friedrich Wilhelm University of Berlin（1853 入学读物理与数学；1858 完成博士）；Heidelberg University（1856–，Bunsen → Kekulé）；Ghent University（随 Kekulé）
- 任职：Gewerbeinstitut Berlin（皇家贸易学院）讲师（1860–）；University of Strasbourg 教授（1871–）；Ludwig-Maximilians-Universität München 化学教授（1875–，接替 Liebig，终身执教至去世前一年）
- 命名机构/命名物：Adolf von Baeyer Medal（1911 年起年度颁发）；月球环形山 Von Baeyer（2009）

## 10. 终审清单（Beamer 执行完毕 2026-09-10，15 页全部核实）

- [x] 生卒 1835-10-31 / 1917-08-20，享年 81，出生地柏林、去世地施塔恩贝格（不用 metadata 的 Munich）
- [x] 1905 诺奖独享，理由中文措辞与总名单一致（染料 + 氢化芳香族化合物）
- [x] 张力学说表述为"获奖工作范围之一"，不倒置为获奖理由
- [x] 荧光素命名 resorcinphthalein、fluorescein 一词 1878 年起用——表述准确
- [x] 反应名（Baeyer–Villiger 等）仅写名，不展开正文无载细节
- [x] 与 Bayer AG 公司无关联表述；拼写 Baeyer 全文统一
- [x] 1989 年 NAS 笔误条目已剔除；1884/1885 荣誉表述与 page.md 文字一致
- [x] 学生入库名单与 §7 策略一致，单源者有 note
- [x] 引语全部可在本地 Wikipedia 原文找到（几乎为零——全部间接转述）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误（Overfull vbox 最大 5.8pt ≤10pt）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Adolf_von_Baeyer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 有真实肖像 URL（`Baeyer.jpg`，250px 缩略图）——下载时改 500px；Commons Special:FilePath 回退：`https://commons.wikimedia.org/wiki/Special:FilePath/Baeyer.jpg?width=600`；404 则用 Wikipedia REST API page/summary 查 infobox 原图名；仍失败则装饰圆占位
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（预计仅诺奖理由英文一句；其余全部间接转述）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有成品（Frederick Sanger）及数学家侧（高斯）格式对齐

---

> **名单状态**：Beamer 立传已于 2026-09-10 执行完成（15 页 PDF + mp4，肖像 Baeyer.jpg 500px 下载成功，BGM The Flow of Time）；`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**，由主控统一置 ✅。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
