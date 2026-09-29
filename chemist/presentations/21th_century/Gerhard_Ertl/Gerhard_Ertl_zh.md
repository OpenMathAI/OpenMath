# Gerhard Ertl（格哈德·埃特尔）立传提示词

> qid=Q60066 · 1936-10-10 生于斯图加特巴特坎施塔特（在世） · 德国物理学家 · 21 世纪 · 诺贝尔化学奖（2007，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Gerhard_Ertl/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本篇的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用 `images/` 目录本地文件，若缺省用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 表面化学的奠基人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「表面 / 界面」母题——大圆象征晶体表面吸附层上的反应位点。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（体系 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Haber–Bosch 合氨、CO 氧化、振荡反应周期。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Gerhard Ertl（中文惯称：格哈德·埃特尔）
- **生卒**：1936-10-10 生于 Stuttgart-Bad Cannstatt（巴登-符腾堡）；**在世**（页面无卒日，一律留白）
- **国籍**：Germany（德国）
- **身份**：德国物理学家（页面 description 即 "German physicist"），马普学会 Fritz Haber 研究所物理化学系荣休教授
- **家庭**：妻子 Barbara，育有两名子女，另有数名孙辈；爱好弹钢琴、与猫为伴；自称基督徒（page.md Personal life 明载）
- **教育轨迹**：
  - 1955–1957 Technische Hochschule Stuttgart 学物理
  - 1957–1958 University of Paris（巴黎大学）
  - 1958–1959 LMU Munich（慕尼黑大学）
  - 1961 于 Technische Hochschule Stuttgart 获物理学 Diplom
  - 随导师 Heinz Gerischer 从斯图加特马普金属研究所赴慕尼黑，1965 于 Technische Hochschule München 获博士学位
- **导师**：Heinz Gerischer（博士导师；Ertl 随其从斯图加特转赴慕尼黑）
- **研究领域**：表面化学（surface chemistry）——多相催化、表面反应分子机理、振荡反应、表面分析方法（LEED / UPS / STM / 光电电子显微术）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **斯图加特之子（1936）**：生于 Stuttgart-Bad Cannstatt，战后的德国少年选择物理学。
2. **三校游学（1955–1959）**：斯图加特—巴黎—慕尼黑的物理学训练，奠定实验与理论并重的底色。
3. **追随 Gerischer（1961–1965）**：导师转赴慕尼黑，他随行并完成博士论文；这段师承开启了他一生的表面研究。
4. **执教德国多校（1965–1986）**：慕尼黑助教/讲师（1965–1968）→ Hannover 教授兼所长（1968–1973）→ LMU Munich 物理化学研究所教授（1973–1986）。
5. **海外客座（1976–1982）**：Caltech（1976–1977）、Wisconsin–Milwaukee（1979）、UC Berkeley（1981–82）访问教授。
6. **执掌 Fritz Haber 研究所（1986–2004）**：任马普 Fritz Haber 研究所所长直至 2004 年退休；同年获柏林自由大学与工业大学"荣誉教授"，1996 洪堡大学荣誉教授。
7. **Haber–Bosch 合氨机理（核心贡献之一）**：确定铁表面上合成氨催化反应的详细分子机理——把百年工业过程还原到原子尺度。
8. **CO 氧化与汽车催化转化器（核心贡献之二）**：确定铂表面上 CO 催化氧化的机理——催化净化汽车尾气的科学基础。
9. **振荡反应（核心贡献之三）**：发现铂表面上的振荡反应现象，并用光电电子显微术首次成像反应中表面结构与覆盖度的振荡变化。
10. **方法学的先行者**：生涯早期用 LEED，其后引入 UPS 与 STM，"始终使用新的观测技术"获得突破性结果（page.md 原文口径）。
11. **Wolf 奖（1998，与 Somorjai 共享）**：与 UC Berkeley 的 Gabor A. Somorjai 共享 Wolf 化学奖，表彰其对表面科学与单晶表面多相催化机理的奠基性贡献。
12. **2007 诺贝尔化学奖（独享）**："for his studies of chemical processes on solid surfaces"；奖金 1000 万瑞典克朗，宣布当天恰逢其 71 岁生日；"I am speechless... I was not counting on this."（对美联社原话，page.md 明载）。
13. **晚年与遗产**：2015 在第 65 届林道诺奖得主大会上签署《气候变化梅瑙宣言》（76 位诺奖得主联署交予法国总统奥朗德）；据 Scopus，截至 2022 年 11 月 h-index 达 124；2023 出版自传 *My Life with Science*。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深催化绿 deepcatal） | `#1E5631` | 表面科学的沉稳深绿——铁催化剂与晶体表面的母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（表面分析 badgeLEED） | `#2C5F8A` | 蓝 LEED / UPS / STM 方法学 |
| 分类色 2（合氨机理 badgeNH3） | `#8A5A2C` | 琥珀 Haber–Bosch 合氨 |
| 分类色 3（CO 氧化 badgeCO） | `#7A1E28` | 绛红 CO 氧化 / 催化转化器 |
| 分类色 4（振荡反应 badgeOsc） | `#1B6B7A` | 青 表面振荡反应与成像 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「表面 / 吸附位点」的界面意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（文件 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`；不要复制 wav 文件，Makefile 直接引用）
- **风格**：感伤 / 纪录片 / 沉思
- **匹配理由**：
  - "纪录片" 匹配传记叙事——斯图加特 → 三校游学 → 执掌 Fritz Haber 研究所 → 71 岁生日当天获诺奖
  - "沉思" 匹配表面化学的气质——数十年潜心于肉眼不可见的原子尺度世界
  - "感伤" 呼应其稳健而克制的科学家形象与漫长的荣誉前夜（Wolf 奖到诺奖间隔近十年）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 表面化学的奠基人 / Gerhard Ertl 1936– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/领域/机构/荣誉）
03  埃特尔的一生 — Sanger 式时间线（10 节点：1936→1955→1965→1968→1973→1986→1998→2004→2007→2015）
04  早年与游学 (1936–1961) — 表格「时间|事件|结果」
05  师承 Gerischer 与博士岁月 (1961–1965) — 表格「时间|事件|结果」
06  表面化学纲领 (1965–1986) — 表格「体系|方法|结果」+ 公式框：LEED/UPS/STM 方法链
07  Haber–Bosch 合氨机理 — 表格「体系|方法|结果」+ 公式框：N2 + 3H2 → 2NH3（铁表面）
08  CO 氧化与催化转化器 — 表格「体系|方法|结果」+ 公式框：2CO + O2 → 2CO2（铂表面）
09  振荡反应与成像 — 表格「现象|方法|结果」+ 公式框：表面结构/覆盖度振荡
10  执掌 Fritz Haber 研究所 (1986–2004) — 高斯式流程图（1986 就任 → 柏林三校荣誉教授 → 2004 退休）
11  荣誉长廊 — Sanger 式「类别|代表|意义」表格（Wolf 1998 / Japan Prize 1992 / Otto Hahn 2007 / Faraday 2007 等 itemize）
12  2007 诺贝尔化学奖 — 公式框：获奖理由原句 + 生日当天宣布 + "I am speechless" 引语
13  遗产：从表面到清洁能源 — 四分类遗产盒 + 公式框：燃料电池 / 尾气净化 / 铁锈 / 平流层冰晶臭氧
14  结尾 — 「在原子尺度读懂表面，就读懂了催化的世界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2007 获奖 | **独享**（无共同得主）；官方理由 "for his studies of chemical processes on solid surfaces"——勿加写"共享"或泛化成"发明表面化学" |
| 「首位德国化学诺奖」 | page.md **无载**，禁止写"德国首位诺贝尔化学奖得主"类断言 |
| 宣布日期 | 2007-10-10 获奖宣布恰逢其 **71 岁生日**（page.md 明载）——是"宣布日"而非"颁奖日" |
| 身份口径 | 页面 description 为 "German physicist"，他是物理学家出身获化学奖；infobox Fields 亦为 Surface chemistry——勿写"德国化学家"开场 |
| 生卒 | 1936-10-10 生于 Stuttgart-Bad Cannstatt；**在世**（页面无卒日），所有"享年/卒于"表述禁写 |
| 博士导师 | **Heinz Gerischer**（随其从斯图加特马普金属研究所转赴慕尼黑）；勿与后文研究所混淆 |
| Wolf 奖 | 1998 **与 Gabor A. Somorjai 共享**——勿写独享 |
| 博士生口径 | 正文 infobox Doctoral students 仅 **Martin Wolf** 一人；metadata 另有 Peter Strasser、Jochen Lauterbach 但正文无——**不予入库** |
| 奖项年份 | EPS Europhysics Prize 与 Japan Prize 均 1992；Otto Hahn Prize 与 Faraday Lectureship Prize 均 2007——勿错配 |
| h-index | "124" 须注明：Scopus、截至 2022 年 11 月 |
| 家庭 | 妻子 Barbara（页面仅此名）、两子女——细节页面无载勿扩写；弹钢琴/养猫/基督徒为 Personal life 原载 |
| 政治议题 | 2015 梅瑙宣言（气候）按 page.md 客观一句带过；其余政治话题页面无载禁写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q60066 | ✅ |
| name_zh | 格哈德·埃特尔 | ✅ |
| name_en | Gerhard Ertl | ✅ |
| birth_date | 1936-10-10 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | surface chemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | surface chemistry | 表面化学 |
| 1 | heterogeneous catalysis | 多相催化 |
| 2 | surface science | 表面科学 |
| 3 | physical chemistry | 物理化学 |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Heinz Gerischer | 师→生（博士导师） | 随导师从斯图加特马普金属研究所转赴慕尼黑，1965 获博士 |
| advisor-student | Martin Wolf | Ertl → 学生 | 正文 infobox Doctoral students 唯一明载 |
| co-honored | Gabor A. Somorjai | 无向 | 1998 Wolf 化学奖共同得主 |

> metadata.json `doctoral_student` 另含 Peter Strasser、Jochen Lauterbach，但 page.md 正文 infobox 无此二人，**不予入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（2007，独享）
- EPS Europhysics Prize（1992）；Japan Prize（1992）
- Wolf Prize in Chemistry（1998，与 Gabor A. Somorjai 共享）
- Otto Hahn Prize（2007）；Faraday Lectureship Prize（2007）
- Gottfried Wilhelm Leibniz Prize；Alwin Mittasch Prize；Karl Ziegler Prize
- Bunsen Medal；Carl Engler Medal；Carl Friedrich Gauss Medal；Liebig Medal
- Bourke Award；Medard W. Welch Award；Centenary Prize；Rudolf-Diesel-Medaille
- Bavarian Maximilian Order for Science and Art；Order of Merit of Baden-Württemberg
- Knight Commander's Cross / Commander's Cross of the Order of Merit of the Federal Republic of Germany
- 多校荣誉博士（Humboldt University of Berlin、Maria Curie-Skłodowska University、Ruhr University Bochum、University of Münster、Katholieke Universiteit Leuven、Comenius University）
- Hall of Fame of German Research；荣誉博士等多项（以 metadata award_received 与 page.md infobox 为准，逐条可溯源）

## 9. 机构清单

- 教育：Technische Hochschule Stuttgart（1955–1957；Diplom 1961）、University of Paris（1957–1958）、LMU Munich（1958–1959）、Technische Hochschule München（PhD 1965）
- 任职：Technische Hochschule München 助教/讲师（1965–1968）→ Leibniz University Hannover 教授兼所长（1968–1973）→ LMU Munich 物理化学研究所教授（1973–1986）→ Fritz Haber Institute of the MPG 所长（1986–2004 退休）
- 客座：Caltech（1976–1977）、University of Wisconsin–Milwaukee（1979）、UC Berkeley（1981–82）
- 荣誉教授：Free University of Berlin 与 TU Berlin（1986）、Humboldt University of Berlin（1996）；TU Darmstadt 大学理事会成员（2008–2016）

## 10. 终审清单

- [x] 生卒 1936-10-10，在世留白；出生地 Stuttgart-Bad Cannstatt
- [x] 2007 **独享**表述准确；获奖理由英文原句忠实；宣布日=71 岁生日
- [x] 「首位德国化学诺奖」等 page.md 无载断言禁写
- [x] 博士导师 Gerischer（斯图加特→慕尼黑随迁）表述准确；Wolf 1998 与 Somorjai 共享
- [x] 博士生仅 Martin Wolf 入库；Strasser/Lauterbach 标注 metadata-only 禁入
- [x] 引语仅 "I am speechless... I was not counting on this." 与获奖理由句（均在 page.md 原文）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Gerhard_Ertl/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 目录 2007 年照片就位（缺省装饰圆占位）
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：引语必须在 page.md 原文找到（获奖理由、美联社两句）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
