# Hans von Euler-Chelpin（汉斯·冯·奥伊勒-切尔平）立传提示词

> qid=Q76613 · 1873-02-15 – 1964-11-06 · 德国出生的瑞典生物化学家 · 诺贝尔化学奖（1929，与 Arthur Harden 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Hans_von_Euler-Chelpin/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地页面 infobox 无肖像（images.txt 为空）：先试 Commons `Special:FilePath/Hans von Euler-Chelpin.jpg?width=600`，再退 Wikipedia REST API `page/summary` 查 infobox 原图名（其诺贝尔官方肖像常见）；全部失败用装饰圆占位（主色渐变 + 姓名首字母），并在 §11 Review 注明。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 发酵的物理化学解读者\enspace·\enspace 瑞典`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素；国籍口径写「德国出生 · 瑞典」（1902 年入瑞典籍并保留德国籍）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（双籍）、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「发酵 / 酶反应」母题——离散圆点暗示发酵体系中酶与底物的分子碰撞。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Hans Karl August Simon von Euler-Chelpin（中文惯称：汉斯·冯·奥伊勒-切尔平；1884-07-28 起冠 von）
- **生卒**：1873-02-15 生于德国巴伐利亚王国 Augsburg → 1964-11-06 逝于瑞典斯德哥尔摩，享年 91
- **国籍**：Germany + Sweden（1902 年入瑞典籍，保留德国籍；变迁两条均入库）
- **身份**：生物化学家（biochemist；1929 诺贝尔化学奖共同得主；斯德哥尔摩大学教授）
- **家庭**：父 Rigas Georg Sebastian von Euler-Chelpin 为巴伐利亚王室步兵卫队上尉（后至少将），母 Gabriele（娘家姓 Furtner）；童年多在 Wasserburg am Inn 的祖母家度过；与数学家 Leonhard Euler **远亲**（仅叙述，不入库）；两次婚姻——1902 年娶化学家 Astrid Cleve（瑞典第一位获科学博士学位的女性，Uppsala 化学家 Per Teodor Cleve 之女；1912 离婚），五子女 Sten（1903–1991）、Ulf Svante（1905–1983）、Karin Maria（1907–2003）、Hans Georg Rigas（1908–2003）、Birgit（1910–2000）；1913 年娶 Elisabeth "Beth" Baroness af Ugglas（1887–1973，曾参与其合作研究），四子女 Rolf Sebastian Ugglas（1914–2005）、Hans Roland Ugglas（1916–2013）、Curt Leonhard Ugglas（1918–2001）、Johan Erik Ugglas "Jan"（1929–1954）
- **教育轨迹**：
  - Augsburg 皇家初中（Holbein Gymnasium 前身），亦就学于 Würzburg 与 Ulm
  - 巴伐利亚第一野战炮兵团一年志愿兵役
  - 1891–1893 慕尼黑美术学院学画（师从 Schmid-Reutte 与 Lenbach；因色彩理论兴趣转向科学）
  - 柏林大学学化学（师从 Emil Fischer 与 A. Rosenheim）、物理（师从 E. Warburg 与 Max Planck）
- **导师**：Carl Friedheim（infobox 博士导师）；Emil Fischer 为 Other academic advisors（柏林化学老师）
- **博士**：1895 年于柏林大学获博士
- **研究领域**：生物化学——糖发酵的物理化学、酶的作用、肿瘤生化

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **军官之子，先学画后学化学（1873–1893）**：巴伐利亚将军之子，因对色彩理论的兴趣从慕尼黑美术学院转向化学——艺术训练成为科学生涯的意外起点。
2. **柏林名师群（1893–1895）**：化学随 Emil Fischer 与 A. Rosenheim，物理随 E. Warburg 与 Max Planck；1895 年获博士。
3. **斯德哥尔摩立足（1899）**：任皇家大学（今斯德哥尔摩大学）Privatdozent；开始走访 van 't Hoff 实验室——van 't Hoff 与 Nernst 是激发其科学兴趣的人。
4. **双重国籍（1902）**：入瑞典籍并保留德国籍——此后一生在两国之间穿梭。
5. **教授任命（1906）**：任斯德哥尔摩皇家大学普通化学与有机化学教授（1906–1941）。
6. **1929 诺贝尔化学奖**：与 Arthur Harden 共享，官方口径 "for their investigations on the fermentation of sugar and fermentative enzymes"。
7. **他的诺奖贡献：物理化学解读发酵**：以物理化学方法令人信服地描述糖发酵过程中发生了什么、发酵酶如何作用——这一解释导向对肌肉供能重要过程的理解。
8. **与哈登的分工**：哈登证明 zymase（Buchner 发现的酶）只有与辅酶 cozymase（NAD）相互作用才产生发酵；冯·奥伊勒-切尔平则给出物理化学层面的机理图景——两者互补，勿混。
9. **一战服役（1914–1918）**：以志愿身份加入德意志帝国陆军巴伐利亚炮兵（1. Feldartillerie-Regiment），1915 转入空军（Luftstreitkräfte），军衔至上尉（Hauptmann）。
10. **研究所创建（1929/1938）**：1929 年 Knut and Alice Wallenberg 基金会与国际教育委员会（洛克菲勒基金会）在斯德哥尔摩建立维生素研究所与生化研究所，任所长；1938–1948 任有机化学研究所所长。
11. **两次世界大战之间的身份张力**：二战期间在德国一方执行外交使命——瑞典科学家与德国效忠者的双重身份是其一生最复杂的注脚（事实陈述，不加评判）。
12. **肿瘤生化专著**：与 Boleslaw Skarzynski 合著《Biochemistry of Tumours》（1942）；又著《The Chemotherapy and Prophylaxis of Cancer》（1962）。
13. **诺奖之家（1970）**：其子 Ulf von Euler 因去甲肾上腺素突触化学性质的研究获 1970 年诺贝尔生理学或医学奖——父子双诺奖的稀有个案；1964-11-06 逝于斯德哥尔摩，享年 91。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（松绿 pinegreen） | `#1E6B52` | 发酵与北欧实验室的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（发酵物理化学 badgePhysChem） | `#2E7D64` | 青绿糖发酵机理 / 酶动力学 |
| 分类色 2（酶与辅酶 badgeEnzyme） | `#8A6A1E` | 赭金酶作用 / cozymase 呼应 |
| 分类色 3（北欧学派 badgeNordic） | `#31456E` | 藏青斯德哥尔摩大学 / 北欧生化 |
| 分类色 4（家族传承 badgeFamily） | `#6B2A4A` | 玫瑰紫 Ulf von Euler / 诺奖之家 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「发酵泡沫 / 分子碰撞」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（文件 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`，不要复制 wav 文件）
- **风格**：史诗 / 穿越 / 深沉张力
- **匹配理由**：
  - "穿越黑暗" 匹配其一生张力——两次世界大战之间在瑞典学者与德国服役者双重身份间穿行
  - "史诗" 匹配 91 岁人生的跨度——从巴伐利亚军官之子到斯德哥尔摩诺奖教授
  - 与批次内其他曲目（Harden=Nostalgy 等）不重复，北欧学派的冷峻质感与 Audiomachine 的深沉音色契合
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐（15 页 × 7 秒 ≈ 105 秒）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 发酵的物理化学解读者 / Hans von Euler-Chelpin 1873–1964 + 四色 badge + 右上头像 + 国籍行（德国出生·瑞典）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/双重国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  奥伊勒-切尔平的一生 — 时间线（10 节点：1873→1891→1895→1899→1902→1906→1929→1938→1941→1964）
04  早年：军官之子与美术学院 (1873–1893) — 表格「时间|事件|结果」
05  柏林名师群 (1893–1899) — 表格「老师|科目|结果」（Emil Fischer/Rosenheim；Warburg/Planck）
06  斯德哥尔摩立足 (1899–1906) — 表格「阶段|事件|结果」（Privatdozent、走访 van 't Hoff 实验室、1902 入籍）
07  1929 诺贝尔化学奖 — 表格「人物|贡献|结果」+ 公式框：zymase + cozymase(NAD) ↔ 发酵（哈登分工对照）
08  发酵的物理化学图景 — 表格「问题|方法|结果」+ 公式框：糖发酵 → 肌肉供能
09  两次大战之间 — 表格「时期|身份|结果」（一战炮兵/空军上尉；二战外交使命）——事实陈述页
10  研究所建设 (1929–1948) — 表格「机构|创办方|结果」（Wallenberg 基金会 + 洛克菲勒 IEB）
11  肿瘤生化 — 表格「著作|合作者|年份」（Biochemistry of Tumours 1942 / 化疗与预防 1962）
12  诺奖之家 — 高斯式「人物|关系|成就」表格（Astrid Cleve 瑞典首位女科学博士 / Ulf von Euler 1970 医学奖）
13  遗产：从发酵到肌肉供能 — 四分类遗产盒 + 公式框：发酵解释 → 能量代谢
14  结尾 — 「他用物理化学之光，照亮了发酵的黑箱。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 博士导师冲突 | frontmatter `doctoral_advisor` 写 Hermann Emil Fischer，但正文 infobox **Doctoral advisor = Carl Friedheim**、Emil Fischer 在 **Other academic advisors**——以 infobox 为准，勿把 Emil Fischer 写成博士导师 |
| 1929 获奖口径 | 官方措辞 "for their investigations on the fermentation of sugar and fermentative enzymes"；与 Harden **共享**——勿写独享 |
| 两人分工 | Harden：发酵化学 + 辅酶 cozymase；冯·奥伊勒-切尔平：物理化学机理解读——勿互换 |
| 战时身份 | 一战志愿加入**德军**炮兵/空军（上尉）；二战在**德国一方**执行外交使命——均为正文实载，客观陈述即可；瑞典籍 + 德军服役的张力如实呈现，不加褒贬 |
| 双重国籍 | 1902 年入瑞典籍**并保留德国籍**——国籍写 Germany + Sweden 两条，勿只写一国 |
| Euler 远亲 | 与 Leonhard Euler 是远亲（distantly related）——可叙述，**不入库**任何关系 |
| Astrid Cleve | 首任妻子，瑞典第一位获科学博士的女性、Per Teodor Cleve 之女——1912 离婚，两个配偶关系均入库 |
| Ulf von Euler | 1970 诺贝尔生理学或医学奖（去甲肾上腺素）——父子关系 parent-child（child 方向）入库 |
| Karin 婚姻 | 女儿 Karin 1931 年嫁作家 Sven Stolpe——姻亲不入库 |
| 生卒地 | 生于 Augsburg（德国），逝于斯德哥尔摩（瑞典）——勿混淆 |
| 页面无载禁写 | page.md **未载**其具体获奖演讲内容细节、纳粹时期更多政治细节——勿扩写 |
| 引语红线 | page.md 无任何直接引语——全文用间接转述，不得杜撰引号原话 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76613 | ✅ |
| name_zh | 汉斯·冯·奥伊勒-切尔平 | ✅ |
| name_en | Hans von Euler-Chelpin | ✅ |
| birth_date | 1873-02-15 | ✅ |
| death_date | 1964-11-06 | ✅ |
| nationality | Germany（rank 0）+ Sweden（rank 1） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | chemistry（person_field 细分：biochemistry / enzymology / organic chemistry / physical chemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 影响者 / 合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Carl Friedheim | 师→生（infobox 博士导师） | 柏林大学博士导师 |
| advisor-student | Hermann Emil Fischer | 师→生（柏林化学老师） | 柏林大学化学老师，Other academic advisors；非博士导师 |
| influence | Max Planck | 无向 | 柏林大学物理老师 |
| influence | Emil Warburg | 无向 | 柏林大学物理老师 |
| influence | Jacobus Henricus van 't Hoff | 无向 | 斯德哥尔摩时期走访其实验室，激发科学兴趣 |
| influence | Walther Nernst | 无向 | 正文明载的科学兴趣影响者 |
| colleague | Boleslaw Skarzynski | 无向 | 《Biochemistry of Tumours》（1942）合著者 |
| co-honored | Arthur Harden | 无向 | 1929 诺贝尔化学奖共同得主 |

**配偶 / 子女**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Astrid Cleve | 无向 | 1902 结婚，1912 离婚；瑞典第一位科学女博士 |
| spouse | Elisabeth af Ugglas | 无向 | 1913 结婚 |
| parent-child | Ulf von Euler | Euler-Chelpin → 子 | 1970 诺贝尔生理学或医学奖 |

> **禁入库名单（metadata/叙事 only）**：Leonhard Euler（远亲，非直系）、Sven Stolpe（女婿，姻亲）、Lisette Schulman（外孙女）、Per Teodor Cleve（岳父，姻亲）、A. Rosenheim（仅"随其学化学"一句，与 Fischer 并列已覆盖师资）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1929，与 Arthur Harden 共享）
- Knight Commander's Cross of the Order of Merit of the Federal Republic of Germany
- Goethe Medal for Art and Science
- 荣誉博士：University of Zurich、University of Bern、Rutgers University、Stockholm University、Christian Albrechts University of Kiel（frontmatter award_received 明载 5 项）

## 9. 机构清单

- 教育：Augsburg 皇家初中（Holbein Gymnasium 前身）→ 慕尼黑美术学院（1891–1893）→ 柏林大学（化学：Emil Fischer、A. Rosenheim；物理：E. Warburg、Max Planck；1895 博士）
- 任职：皇家大学斯德哥尔摩（今斯德哥尔摩大学）Privatdozent（1899–）→ 普通化学与有机化学教授（1906–1941）→ 维生素研究所与生化研究所所长（1929–）→ 有机化学研究所所长（1938–1948）；1941 年退休教学，继续研究
- 军役：巴伐利亚第一野战炮兵团一年志愿兵（青年时期）；一战德意志帝国陆军志愿服役（1915 转空军，至上尉）

## 10. 终审清单

- [ ] 生卒 1873-02-15 / 1964-11-06，享年 91，出生地 Augsburg、去世地斯德哥尔摩
- [ ] 1929 共享（Harden）表述准确；官方获奖理由英文原句完整呈现
- [ ] 博士导师 Carl Friedheim（infobox 为准），Emil Fischer 写作柏林老师而非博士导师
- [ ] 双重国籍 Germany + Sweden 表述准确；战时身份事实陈述无褒贬
- [ ] Ulf von Euler 1970 医学奖父子关系准确；Leonhard Euler 仅叙述远亲不入库
- [ ] 无编造引语——page.md 无任何直接引语，全文用间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Hans_von_Euler-Chelpin/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：本地页面无肖像，检查装饰圆占位或 REST API 回退结果并记录
- [ ] **国籍**：封面顶部明示「德国出生 · 瑞典」
- [ ] **引语核对**：全文不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
