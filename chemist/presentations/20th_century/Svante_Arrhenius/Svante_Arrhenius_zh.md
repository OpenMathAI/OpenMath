# Svante Arrhenius（斯万特·阿伦尼乌斯）立传提示词

> qid=Q80956 · 1859-02-19 – 1927-10-02 · 瑞典科学家（原为物理学家，常被称作化学家）· 物理化学奠基人之一 · 诺贝尔化学奖（1903）
> 诺奖理由（总名单 OpenChemist_20th_Century_Nobel_Laureates.md 措辞）：**表彰他因提出电离理论而对化学进步所作出的杰出贡献**
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Svante_Arrhenius/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Svante_Arrhenius_01.jpg`，1909 年肖像照，下载见 §11 Review-1 指引）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 溶液中的离子\enspace·\enspace 瑞典`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、导师、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「离子」母题——带电粒子在溶液中弥散、离散而相互作用。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化——电离定义与 Arrhenius 方程、温室辐射强迫式都是天然的公式框素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Svante August Arrhenius（中文惯称：斯万特·阿伦尼乌斯）
- **生卒**：1859-02-19 生于瑞典乌普萨拉省 Vik 庄园（Vik Castle，又拼 Wik/Wijk），近乌普萨拉 → 1927-10-02 逝于斯德哥尔摩，享年 68；葬于乌普萨拉（家族墓 Arrhenius family grave）
- **国籍**：Sweden（瑞典）——1903 年诺贝尔化学奖使他成为**首位瑞典诺贝尔奖得主**
- **身份**：科学家——原本是物理学家，常被称作化学家；物理化学（physical chemistry）奠基人之一；1905 年起任诺贝尔物理研究所所长直至 1927 年退休/去世
- **家庭**：父亲 Svante Gustav Arrhenius 为乌普萨拉大学土地测量员，后升任主管；母亲 Carolina Thunberg；家庭信路德宗（Lutheran）。两度结婚：首任前学生 Sofia Rudbeck（1894–1896），一子 Olof Arrhenius；次任 Maria Johansson（1905–1927），两女一子。孙辈：细菌学家 Agnes Wold、化学家 Svante Wold、海洋生物地球化学家 Gustaf Arrhenius。气候活动家 Greta Thunberg 之父 Svante Thunberg 是其远房表亲，并以他命名
- **童年天赋**：三岁无人督促自学认字；看父亲账本上加数而成为算术神童；终生热爱数学概念、数据分析及其关系与规律的发现
- **教育轨迹**：
  - 8 岁入乌普萨拉本地座堂学校（Katedralskolan, Uppsala），直接从五年级读起，物理与数学出众
  - 1876 年以最年轻、最有才能的学生身份毕业
  - 乌普萨拉大学：对物理主讲教师不满，而化学方面唯一能指导他的 Per Teodor Cleve 亦不能令他满意 → 1881 年离开，转入瑞典科学院斯德哥尔摩物理研究所，师从物理学家 Erik Edlund
- **导师**：Per Teodor Cleve（乌普萨拉化学，名义博士导师、关系不佳）；Erik Edlund（斯德哥尔摩物理学家，实际博士指导）——**两人在 infobox 并列**，勿只写一人（metadata.json 只录 Cleve，与 page.md 不一致，以 page.md 为准）
- **博士论文**：1884 年，150 页电解质电导论文提交乌普萨拉（Works 列表记 155 页，以正文叙述为准，见 §5）；56 条论纲，最重要思想：固态结晶盐溶于水后解离成带电粒子（离子）
- **研究领域**：物理学、化学——电离理论、电解质电导、化学反应速率（活化能）、温室效应计算、免疫化学、宇宙物理学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **算术神童（1859–1876）**：三岁自学识字、看账本加数成算术神童；座堂学校直接插班五年级，1876 年以最年轻且最有才能的学生毕业——数字与规律的终生之爱由此生根。
2. **从乌普萨拉出走斯德哥尔摩（1881）**：对乌普萨拉物理教学与 Cleve 均不满，转投瑞典科学院物理研究所 Erik Edlund 门下，聚焦电解质电导。
3. **电离理论的诞生（1884）**：150 页博士论文提出——无外部电流时，盐水溶液中也存在离子；溶液中的化学反应就是离子之间的反应。Faraday 命名了"ion"却认为离子须由电解产生，阿伦尼乌斯则把离子变成溶液的常态。
4. **答辩风波（1884）**：论文未打动乌普萨拉教授们，初评四等，答辩后改判三等；同年他据此提出酸碱定义——酸产生氢离子、碱产生氢氧根离子。
5. **寄往欧洲的翻盘信（1884–1885）**：他把论文寄给 Clausius、Ostwald、van 't Hoff 等物理化学先驱；Ostwald 亲自到乌普萨拉邀他赴里加，被他婉拒（父亲病重将于 1885 年去世、且已在乌普萨拉获任命）。
6. **欧洲游学（1885–）**：获瑞典科学院旅费资助，先后随 Ostwald（里加、莱比锡）、Kohlrausch（维尔茨堡）、Boltzmann（格拉茨）、van 't Hoff（阿姆斯特丹）研究。
7. **Arrhenius 方程与活化能（1889，莱比锡）**：与 Ostwald 合作期间提出活化能概念——两分子反应前须翻越的能垒；方程给出活化能与反应速率关系的定量基础。
8. **斯德哥尔摩学院（1891–1896）**：任讲师；1895 年在诸多反对声中升任物理学教授；1896 年任院长（rector）。
9. **诺贝尔体系与评审角色（约 1900 起）**：1901 年（顶着强烈反对）当选瑞典皇家科学院院士；终其一生任诺贝尔物理学委员会委员、化学委员会事实成员——曾为友人（van 't Hoff、Ostwald、Theodore Richards）安排奖项，并试图阻止对手（Paul Ehrlich、Walther Nernst、门捷列夫）获奖。
10. **1903 诺贝尔化学奖**：博士论文的延伸工作使他获奖，成为首位瑞典诺奖得主；诺奖演讲题为 "Development of the Theory of Electrolytic Dissociation"（1903-12-11）。
11. **温室效应的首算（1896）**：为解释冰期，首次用物理化学基本原理计算大气 CO2 增加对地表温度的影响；基于 Högbom 的信息，他是首位预测化石燃料燃烧排放足以导致全球变暖的人。规则 ΔF = α ln(C/C0) 沿用至今（CO2 的 α≈5.35 W/m²）；1900 年遭 Knut Ångström 依据"吸收饱和"批评，1901 年在 *Annalen der Physik* 强硬回应；*Worlds in the Making*（1908）向大众阐述"温室理论"。
12. **更广阔的疆域（1902–）**：用化学理论研究生理学问题（生物体内反应与试管反应服从同一定律）；1904 年伯克利讲座后出版 *Immunochemistry*（1907）；转向地质学（冰期成因）、天文学、宇宙学与天体物理学（星际碰撞解释太阳系起源、辐射压解释彗星/日冕/极光/黄道光）；提出生命可随孢子在行星间传播的泛种论（panspermia）设想；还设想改造英语的通用语言。
13. **命名与身后**：月球环形山、火星环形山、斯瓦尔巴 Arrheniusfjellet 山、斯德哥尔摩大学 Arrhenius Labs 皆以其命名；1922 年出席布鲁塞尔首届索尔维化学会议；1960 年代 Keeling 可靠测得大气 CO2 持续上升，温室假说进入现代气候科学核心。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（北欧极夜蓝绿 deepnordic） | `#0F4C5C` | 溶液深处的离子世界 / 物理化学的冷静与精确（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（电离理论 badgeIon） | `#1F6FB2` | 蓝离子解离 / 电导 / 酸碱定义 |
| 分类色 2（活化能与方程 badgeAct） | `#B4502A` | 赭活化能 / Arrhenius 方程 |
| 分类色 3（温室效应 badgeClim） | `#2E7D4F` | 绿 CO2 / 全球变暖首算 |
| 分类色 4（宇宙物理 badgeCosm） | `#6B4FA0` | 紫泛种论 / 宇宙物理学 / 免疫化学 |
| 背景 | `#F6F7F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「离子」——带电粒子在溶液中离散弥散、彼此作用的图景。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`）
- **风格**：流动 / 平稳 / 叙事
- **匹配理由**：
  - "流动" 匹配贡献本质——电离理论的核心意象正是离子在溶液中的离散、迁移与弥散，SEA 的流体感与之同构
  - "平稳" 匹配其叙事节奏——从乌普萨拉的冷遇到斯德哥尔摩的承认，是一段漫长而终有回响的学术漂流（游学路线：里加、莱比锡、维尔茨堡、格拉茨、阿姆斯特丹）
  - 模板 §5.3 亦将 Arrhenius 列入「探索/远征」气质（推荐 Expedition），Expedition 已由 van 't Hoff 选用，故改用同库 SEA 以避重
- **时长**：以实际文件为准；略短于 slides 总时长时 ffmpeg `-shortest` 自动对齐
- **注**：wav 复制在执行立传阶段进行（`cp` 到本目录，Makefile `BGM = $(wildcard *.wav)` 自动检测）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 溶液中的离子 / Svante Arrhenius 1859–1927 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/导师/师承/出生地/去世地/领域/荣誉）
03  阿伦尼乌斯的一生 — 高斯式时间线（10 节点：1859→1876→1881→1884→1885→1889→1896→1903→1905→1927）
04  早年：乌普萨拉的算术神童 (1859–1881) — 表格「时间|事件|结果」（座堂学校/自学识字/出走斯德哥尔摩）
05  博士论文与答辩风波 (1884) — 表格「问题|方法|结果」+ 公式框：电离定义（盐→带电粒子；酸→H+，碱→OH−）
06  欧洲游学与物理化学共同体 (1885–1891) — 表格「城市|导师|收获」（里加/莱比锡 Ostwald、维尔茨堡 Kohlrausch、格拉茨 Boltzmann、阿姆斯特丹 van 't Hoff）
07  Arrhenius 方程与活化能 (1889) — 表格「问题|方法|结果」+ 公式框：k = A·e^(−Ea/RT)
08  温室效应首算 (1896) — 表格「问题|方法|结果」+ 公式框：ΔF = α·ln(C/C0)，α≈5.35 W/m²；Ångström 批评与回应
09  1903 诺贝尔化学奖 — 表格「背景|评审|意义」（首位瑞典得主；诺奖演讲 1903-12-11）
10  诺贝尔体系中的角色 — 表格「人物|关系|结果」（为友人安排：van 't Hoff/Ostwald/Richards；阻止：Ehrlich/Nernst/门捷列夫——措辞按 page.md 间接转述）
11  更广阔的疆域 — 高斯式「领域|代表|意义」表格（免疫化学 Immunochemistry 1907 / 冰期与宇宙物理 / 泛种论 / 通用语言）
12  荣誉与学会 — 高斯式「类别|代表|意义」表格（Davy 1902、Willard Gibbs 首奖 1911、Faraday 1914、Franklin 1920、ForMemRS 1910、多所大学荣誉博士）
13  遗产：从离子到气候 — 四分类遗产盒（物理化学奠基 / Arrhenius 方程沿用至今 / 现代气候科学源头 / 命名：月球·火星环形山·Arrheniusfjellet·Arrhenius Labs）
14  结尾 — 「溶液虽静，离子自行；大气无声，碳已在数。」（自拟金句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1903 独享 | 1903 年诺贝尔化学奖为阿伦尼乌斯**独享**；勿写与他人共享。他也是**首位瑞典**诺贝尔奖得主 |
| 诺奖理由措辞 | 总名单官方措辞「表彰他因提出电离理论而对化学进步所作出的杰出贡献」——表彰对象是**电离理论**，勿写成"因 Arrhenius 方程"或"因温室效应"获奖 |
| 方程与电离理论勿混 | **电离理论（1884，诺奖理由）**与 **Arrhenius 方程/活化能（1889，莱比锡与 Ostwald 合作）**是两项不同贡献、相隔五年——勿把方程写成获奖理由，勿把活化能写进 1884 年论文 |
| 答辩评级叙事 | 事实链：论文"未打动教授们"→ 初评**四等** → 答辩后改判**三等** → 该工作的延伸使他获 1903 诺奖。勿夸大为"被当众羞辱"或编造"委员会正式道歉/平反仪式"（page.md 无载） |
| 博士导师是两人 | infobox 并列 **Per Teodor Cleve**（乌普萨拉化学，关系不佳）与 **Erik Edlund**（斯德哥尔摩物理，实际指导）；metadata.json 只录 Cleve，与 page.md 不一致——**以 page.md 为准，两人都写**，勿把 Cleve 写成支持者 |
| 离子概念的归属 | "ion"一词是 **Faraday** 命名，且 Faraday 认为离子须由电解（外部电流）产生；阿伦尼乌斯的贡献是提出**无电流时溶液中亦有离子**——勿写他"命名离子"或"发现离子" |
| Ostwald 招募被拒 | Ostwald 亲赴乌普萨拉邀他加入里加团队，他**婉拒**（父亲病重、已在乌普萨拉获任命）；1885 年才以旅费资助赴里加/莱比锡——勿写成"随即加入 Ostwald 团队" |
| 温室效应有载、但措辞须精确 | page.md 明载 1896 温室计算，**可以写**；但 Fourier/Tyndall/Pouillet 是前驱（他"建立在先辈工作之上"），他做的是"首次用物理化学原理**计算** CO2 增温幅度"——勿写"发现温室效应"；"首个预测化石燃料排放足以致暖"须归因于 Högbom 提供的信息与他的计算 |
| 泛种论有载 | page.md 明载：他认为生命可能由孢子在行星间搬运（今称 panspermia）——可写，措辞用"他认为/他设想"，勿写成"证明" |
| CO2 与"碳酸" | 阿伦尼乌斯原文把 CO2 称作 "carbonic acid"（现代用法仅指水溶液形态 H2CO3）——若引原文须保留原词并注明，勿悄然改成 CO2 |
| 评审政治（敏感） | page.md 明载其为友人（van 't Hoff、Ostwald、Theodore Richards）安排奖项、试图阻止 Ehrlich、Nernst、门捷列夫获奖——可写但必须间接转述、逐字核对 page.md，勿添油加醋或写成"贿选" |
| 种族卫生协会（敏感） | page.md 载其曾任瑞典种族卫生学会（1909 年创立）董事会成员——**建议略过**；若写须严格照实一句话，不得展开或洗白 |
| 宗教信仰 | Gordon Stein 称其为无神论者，另有资料称路德宗——page.md 两种说法并存，**勿断言其一** |
| 引语纪律 | page.md 可溯源英文原话仅限：Arrhenius "rule" 原句（"if the quantity of carbonic acid increases in geometric progression..."）与 *Worlds in the Making* 各页引文（p.46/51/53/61/63）。其余一律间接转述；中文引号内禁止出现无法溯源的"原话" |
| 论文页数 | 正文叙述"150 页论文"，Works 列表记 155 页——Beamer 用 150 页（以正文为准），或笼统写"逾百页" |
| 去世细节 | 1927 年 9 月患急性肠卡他（acute intestinal catarrh），10 月 2 日逝于斯德哥尔摩，葬于乌普萨拉——勿写"病逝于乌普萨拉"或死因含糊成"年老" |
| 1905 职务表述 | 首段写"1905 任诺贝尔研究所所长直至去世"，后文写"任该所所长（rector）直至 1927 年退休"——统一表述为"1905 年出任诺贝尔物理研究所所长，直至 1927 年去世/退休"，勿写两种任期终点 |
| 入院年份噪声 | metadata.json `educated_at` 含 Stockholm University（实为 Stockholms Högskola 学院，现大学）——身份页写"斯德哥尔摩大学学院（今斯德哥尔摩大学）" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q80956 | ✅ |
| name_zh | 斯万特·阿伦尼乌斯 | ✅ |
| name_en | Svante Arrhenius（label：Svante August Arrhenius） | ✅ |
| birth_date | 1859-02-19 | ✅ |
| death_date | 1927-10-02 | ✅ |
| nationality | Sweden | ✅ |
| primary_occupation | chemist / physicist（page.md：原为物理学家，常被称作化学家；metadata 兼有 astronomer——以 page.md 为主导口径） | ✅ |
| field_of_work | physical chemistry（person_field 细分：ionic dissociation / activation energy / greenhouse effect / cosmophysics，带 rank） | ✅ |
| has_biography | 1 | ✅ 入库时置 1 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同先驱**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Per Teodor Cleve | 师→生（名义博士导师） | 乌普萨拉化学导师，关系不佳；metadata 只录此人，page.md infobox 并列两人 |
| advisor-student | Erik Edlund | 师→生（实际博士指导） | 1881 年转入其斯德哥尔摩物理研究所门下 |
| colleague | Wilhelm Ostwald | 无向 | 1884 亲赴乌普萨拉招募被婉拒；1885 里加/莱比锡游学、1889 合作提出活化能；为其安排诺奖的友人 |
| colleague | Jacobus Henricus van 't Hoff | 无向 | 游学至阿姆斯特丹；物理化学先驱；为其安排诺奖的友人 |
| colleague | Friedrich Kohlrausch | 无向 | 维尔茨堡游学导师 |
| colleague | Ludwig Boltzmann | 无向 | 格拉茨游学导师 |
| colleague | Arvid Högbom | 无向 | 温室效应计算的信息来源同事 |
| colleague | Oskar Benjamin Klein | 见左注 | **阿伦尼乌斯 → 学生**（infobox/metadata 一致的唯一博士生）——单独一行：advisor-student，方向 生←师 |
| competitor | Walther Nernst | 无向 | 诺奖评审中被其试图阻止的对手（page.md 载） |
| competitor | Dmitri Mendeleev | 无向 | 同上；门捷列夫终生未获诺奖 |
| other | Svante Thunberg | 无向 | 远房表亲，Greta Thunberg 之父，以其命名 |

> Wikidata `doctoral_student` 仅 Oskar Klein，与正文 infobox 一致，入库无冲突。

## 8. 奖项清单

- Nobel Prize in Chemistry（1903，独享；首位瑞典诺奖得主）
- Davy Medal（1902）
- Willard Gibbs Award（1911；该奖首位得主）
- Faraday Lectureship Prize（1914）
- Franklin Medal（1920）
- Foreign Member of the Royal Society，ForMemRS（1910）
- International Member, U.S. National Academy of Sciences（1908）
- Honorary Member, Netherlands Chemical Society（1909）
- International Member, American Philosophical Society（1911）
- Foreign Honorary Member, American Academy of Arts and Sciences（1912）
- Foreign Member, Royal Netherlands Academy of Arts and Sciences（1919）
- Echegaray Medal；Silliman Memorial Lectures（metadata.json）
- 荣誉博士：Edinburgh、Cambridge、Groningen、Heidelberg、Leipzig、Oxford、Birmingham、Paris（metadata.json）

## 9. 机构清单

- 教育：Katedralskolan, Uppsala（8 岁入五年级，1876 毕业）；Uppsala University；Physical Institute of the Swedish Academy of Sciences, Stockholm（1881 起，Edlund 门下）
- 任职：Uppsala University（1884 起获任命）；Stockholm University College（Stockholms Högskola）讲师（1891）→ 物理学教授（1895，多有反对）→ 院长（1896）；诺贝尔物理研究所所长（1905–1927 去世/退休）
- 命名机构/地标：Arrhenius Labs（斯德哥尔摩大学）；月球环形山 Arrhenius；火星环形山 Arrhenius；斯瓦尔巴 Arrheniusfjellet

## 10. 终审清单

- [ ] 生卒 1859-02-19 / 1927-10-02，享年 68，出生地 Vik（近乌普萨拉）、去世地斯德哥尔摩、葬于乌普萨拉
- [ ] 1903 独享、首位瑞典诺奖得主表述准确；诺奖理由为电离理论（总名单措辞）
- [ ] 电离理论（1884）与 Arrhenius 方程/活化能（1889）分离表述，未混淆
- [ ] 答辩评级链（四等→答辩后三等→延伸工作获奖）无夸大、无"平反仪式"
- [ ] 博士导师两人并列（Cleve + Edlund），metadata 冲突已在 §5 注明
- [ ] Faraday 命名 ion、阿伦尼乌斯提出无电流亦有离子——归属正确
- [ ] 温室效应 1896 首算、Fourier/Tyndall/Pouillet 前驱、Högbom 信息来源、Ångström 1900 批评/1901 回应——均有 page.md 依据
- [ ] 泛种论、免疫化学（1904 伯克利讲座/1907 出版）、宇宙物理均有载且措辞为"设想/认为"
- [ ] 评审政治（友人/对手名单）逐字对照 page.md 间接转述；种族卫生学会建议略过
- [ ] 引语全部可在 page.md 找到原文（Arrhenius rule 原句、Worlds in the Making 各页引文）；其余全部间接转述
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Svante_Arrhenius/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 有真实肖像可用——推荐 `Svante_Arrhenius_01.jpg`（1909 年肖像照，infobox 采用），下载 URL（250px 改 500px）：`https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Svante_Arrhenius_01.jpg/500px-Svante_Arrhenius_01.jpg`；备选 `1922_Svante_Arrhenius.jpg`（1922 年 Auguste Léon 彩色 autochrome）。**陷阱**：`Arrhenius...Lehrbuch...jpg` 是 1903 年著作书影、`Arrhenius_family_grave.jpg` 是墓碑照，均**禁作肖像**；下载后 `file` 验证为 JPEG
- [ ] **国籍**：封面顶部明示瑞典
- [ ] **引语核对**：引语必须在 page.md 原文找到（rule 原句、Worlds in the Making 引文）；中文引号内禁止无源"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；引号用半角
- [ ] 与化学家侧既有格式（Sanger 版式）及数学家侧（高斯）对齐

---

> **名单状态**：本提示词已完成；Beamer 立传**待执行**。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（执行立传完成后再同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
