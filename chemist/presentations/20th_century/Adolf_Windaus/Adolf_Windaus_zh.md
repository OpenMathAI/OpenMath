# Adolf Windaus（阿道夫·温道斯）立传提示词

> qid=Q77142 · 1876-12-25 – 1959-06-09 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1928，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Adolf_Windaus/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。★ 本人物 images.txt **无真实肖像**（仅哥廷根墓碑照 + 维生素 D3/7-脱氢胆固醇结构图，均禁充当肖像）——封面与身份页用**装饰圆占位**（主色实心圆 + 缩写 AW）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{sun}\enspace 阳光维生素的解构者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：左侧装饰圆 + 右侧 2×2 信息网格，至少含：生卒、全名、国籍、出生地/去世地、教育、博士导师、博士学生、配偶、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡呼应「甾体四环」母题——四枚大圆环错落排布。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：tabularx 三列表格 + 金色边框浅金底公式展示框，如「7-脱氢胆固醇 --UV--> 维生素 D3」或「ergosterol --UV--> 维生素 D2」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Adolf Otto Reinhold Windaus（中文惯称：阿道夫·温道斯）
- **生卒**：1876-12-25 生于柏林（德意志帝国）→ 1959-06-09 逝于哥廷根（西德），享年 82
- **国籍**：Germany（德国）
- **身份**：化学家、大学教师
- **家庭**：出身经营布料生意（drapery）之家；1915 年娶 Elizabeth Resau，三子女 Günter、Gustav、Margarete
- **教育轨迹**：柏林著名法语文法学校（Französisches Gymnasium Berlin，主修文学）→ 约 1895 年起 Humboldt-Universität zu Berlin 学医 → 转至 University of Freiburg 学化学；**博士学位是医学（PhD in medicine）**
- **博士导师**：Heinrich Kiliani
- **博士学生**：Adolf Butenandt（后获 1939 诺贝尔化学奖，page.md 明载）、Erhard Fernholz（infobox 明载）
- **研究领域**：organic chemistry、biochemistry——甾醇（sterols）、维生素（尤其维生素 D）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **柏林布商之家（1876）**：圣诞日 1876-12-25 生于柏林；全名 Adolf Otto Reinhold Windaus。
2. **从文学到医学再到化学**：法语文法学校主修文学 → 约 1895 柏林学医 → 弗莱堡转化学——三段转向，终点是甾体化学。
3. **医学博士的化学人生**：PhD in medicine 出身，博士导师 Heinrich Kiliani——先懂生命，再解分子。
4. **甾醇版图**：胆固醇（人胆石中最先发现）研究起步；zoosterols（昆虫/棘皮动物/海绵，spongosterol 为饱和型例外）、phytosterols（sitosterols 为主）、mycosterols（ergosterol 含三个双键）；发现细菌中不存在甾醇。
5. **胆固醇体内波动**：着迷于胆固醇水平随妊娠升高、随疾病下降的波动——临床视角的化学家。
6. **1928 诺贝尔化学奖**：表彰其甾醇研究及其与维生素的联系；诺奖演讲 1928-12-12《Constitution of Sterols and Their Connection with Other Substances Occurring in Nature》。
7. **胆固醇 → 维生素 D3**：发现胆固醇经数步转化为维生素 D3（cholecalciferol）的路径；专利交予 Merck 与 Bayer，1927 年 Vigantol 上市。
8. **"纯胆固醇"之谜**：受其指导的研究者发现完全纯化（成二溴化物重结晶）的胆固醇照射后失去抗佝偻效力——真正的维生素 D 前体是随"化学纯"胆固醇一路走来的杂质。
9. **ergosterol = 唯一前体**：与 A. F. Hess、O. Rosenheim、T. A. Webster 磋商评估，确定 ergosterol 是可在 253–302 nm 波长转化为维生素 D 的唯一前体。
10. **维生素 D2（calciferol）**：对佝偻病（rachitis）完全奏效，效力是鱼肝油的 **10 万倍**；与 ergosterol 同分异构（一个羟基 + 三个共轭双键），正确结构 1936 年确认。
11. **7-脱氢胆固醇 → 维生素 D3**：从猪皮（后及人皮、全奶、动物肝脏）分离鉴定 7-脱氢胆固醇，光照产物即维生素 D3——以光化学反应确定结构。
12. **正直的坐标**：一战拒绝研究毒气；纳粹时期是极少数不与纳粹合作的德国化学家之一、公开反对其政权，并以哥廷根化学所所长身份保护一名犹太研究生免于解雇。
13. **门生与身后**：学生 Adolf Butenandt 获 1939 诺贝尔化学奖（师门两代诺奖）；1959-06-09 逝于哥廷根，享年 82。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深翠绿 deep emerald） | `#146B3A` | 生命分子的绿与阳光维生的暖（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（甾醇 badgeSterol） | `#2F5D50` | 墨绿甾醇 / 胆固醇 |
| 分类色 2（维生素 D badgeVitD） | `#B8860B` | 暗金维生素 D2/D3 / 阳光转化 |
| 分类色 3（工业转化 badgeIndustry） | `#4A5FA5` | 靛蓝 Vigantol / Merck·Bayer 专利 |
| 分类色 4（正直风骨 badgeIntegrity） | `#C0395B` | 玫瑰拒毒气 / 护学生 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆 + 四环轮廓），呼应「甾体四环骨架」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`；不要复制 wav 文件，Makefile 引用路径即可）
- **风格**：孤独 / 沉静 / 情感纪录片
- **匹配理由**：
  - "孤独" 匹配其风骨——一战中拒绝毒气研究、纳粹时期公开反对政权，是"极少数不合作者"的清冷位置
  - "沉静" 匹配其科学节奏——从杂质线索到 10 万倍效力的维生素 D2，是漫长定力下的结晶
  - "情感纪录片" 匹配传记叙事——柏林 → 弗莱堡 → 哥廷根 30 年 → 1928 诺奖 → 阳光维生素
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 阳光维生素的解构者 / Adolf Windaus 1876–1959 + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/全名/国籍/教育/博士导师/博士学生/配偶/出生地/去世地/领域/荣誉）
03  温道斯的一生 — Sanger 式时间线（10 节点：1876→1895→1915→1927→1928→1936→1939→1944→1952→1959）
04  从文学到医学再到化学 (1876–1900s) — 表格「阶段|转向|结果」
05  甾醇版图 — 表格「类别|代表|特征」（胆固醇 / zoosterols / phytosterols / mycosterols / 细菌无甾醇）
06  "纯胆固醇"之谜 — 表格「现象|排查|结论」+ 公式框：杂质即前体
07  ergosterol 与维生素 D2 — 表格「合作者|发现|意义」+ 公式框：ergosterol --UV 253–302 nm--> D2（效力 10 万倍）
08  维生素 D3 与 Vigantol — 表格「前体|产物|去向」+ 公式框：7-脱氢胆固醇 --UV--> D3
09  1928 诺贝尔化学奖 — 公式框：诺奖演讲标题 (1928-12-12)
10  师门两代诺奖 — 表格「人物|方向|结果」（Butenandt 1939 / Fernholz）
11  正直的坐标 — 表格「时代|抉择|结果」（一战拒毒气 / 纳粹护犹太学生）
12  荣誉清单 — 「类别|代表|意义」表格（Pour le Mérite 1952 / Goethe Medal 1941 / Adolf-von-Baeyer Gold Medal / Pasteur Medal）
13  遗产：阳光维生素 — 四分类遗产盒 + 公式框
14  结尾 — 「解开甾醇之环，点亮阳光维生素。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 学位口径 | **PhD in medicine**（医学博士）——先医学后化学；勿写"化学博士" |
| 博士导师 | Heinrich Kiliani（frontmatter + infobox 双载，一致）——可入库 |
| 求学年份 | 仅"约 1895 年起柏林学医"——弗莱堡转学年份、博士年份页面无载，禁编造 |
| 早期任职 | 求学与 1915 年任哥廷根化学所所长之间的任职经历页面无载——禁脑补 |
| 获奖理由口径 | page.md 原文 "for his work on sterols and their relation to vitamins"——勿混入 Wieland 的胆汁酸口径 |
| 10 万倍 | 维生素 D2 对佝偻病效力是鱼肝油的 100,000 倍——勿写 10 倍/千倍 |
| D2 vs D3 | **D2 = ergosterol 经 UV（253–302 nm）**；**D3 = 7-脱氢胆固醇经 UV**（猪皮→人皮/全奶/动物肝脏）；1936 年确认的是 D2 结构——勿互换前体 |
| Vigantol | 1927 年由 Merck 与 Bayer（用其专利）推出——勿写"温道斯创办公司" |
| 合作者 | 维生素 D 前体评估"in consultation with A. F. Hess, O. Rosenheim, T. A. Webster"——是磋商合作，勿写成师承；三人全名页面未载，入库用页面缩写形式 |
| 纳粹时期 | "one of the very few German chemists who did not work with the Nazis and openly opposed their regime" + 保护一名犹太研究生——如实客观呈现，勿加页面未载细节 |
| Butenandt | 1939 诺贝尔化学奖 page.md 明载——note 可写；Fernholz 获奖信息无载禁写 |
| 肖像 | images.txt 仅有墓碑照与分子结构图——**禁充当肖像**，装饰圆占位 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q77142 | ✅ |
| name_zh | 阿道夫·温道斯 | ✅ |
| name_en | Adolf Windaus | ✅ |
| birth_date | 1876-12-25 | ✅ |
| death_date | 1959-06-09 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待立传后置 1） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | sterols | 甾醇 |
| 1 | vitamin D | 维生素 D |
| 2 | organic chemistry | 有机化学 |
| 3 | biochemistry | 生物化学 |

## 7. 社会关系入库清单

**★ 红线**：只收 page.md 正文或 infobox 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Heinrich Kiliani | 师→生（博士导师） | frontmatter 与 infobox 双载一致 |
| advisor-student | Adolf Butenandt | 师→生 | infobox Doctoral students 明载；后获 1939 诺贝尔化学奖（page.md 明载） |
| advisor-student | Erhard Fernholz | 师→生 | infobox Doctoral students 明载 |
| spouse | Elizabeth Resau | 无向 | 1915 年结婚，三子女 Günter/Gustav/Margarete |
| colleague | A. F. Hess | 无向 | 维生素 D 前体评估磋商合作（页面用缩写形式，全名无载） |
| colleague | O. Rosenheim | 无向 | 维生素 D 前体评估磋商合作（页面用缩写形式，全名无载） |
| colleague | T. A. Webster | 无向 | 维生素 D 前体评估磋商合作（页面用缩写形式，全名无载） |

**禁入库名单（无对应关系类型 / 仅列举）**：

> 子女 Günter、Gustav、Margarete（防噪声不入库）；Merck 与 Bayer（公司非人物）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1928，独享；诺奖演讲 1928-12-12 Constitution of Sterols and Their Connection with Other Substances Occurring in Nature）
- Pour le Mérite for Sciences and Arts（1952）
- Goethe Medal for Art and Science（1941）
- Adolf-von-Baeyer Gold Medal（年份页面无载）
- Pasteur Medal（正文载名，年份无载）
- Commander's Cross of the Order of Merit of the Federal Republic of Germany（年份页面无载）

## 9. 机构清单

- 教育：Französisches Gymnasium Berlin（法语文法学校）、Humboldt-Universität zu Berlin（约 1895 起学医）、University of Freiburg（转化学）
- 任职：University of Göttingen 化学所所长（1915–1944）
- 产业：专利交予 Merck KGaA 与 Bayer；Vigantol（1927 上市）

## 10. 终审清单

- [ ] 生卒 1876-12-25 / 1959-06-09，享年 82，出生地柏林、去世地哥廷根
- [ ] 学位口径：PhD in medicine；求学年份无载处不编造
- [ ] 获奖理由忠实 page.md（sterols and their relation to vitamins）；与 Wieland 胆汁酸口径区分
- [ ] D2（ergosterol）/D3（7-脱氢胆固醇）前体不互换；效力 10 万倍、Vigantol 1927、结构确认 1936 表述准确
- [ ] 七条关系均有 page.md 出处；Hess/Rosenheim/Webster 用页面缩写形式
- [ ] 一战拒毒气 / 纳粹时期护学生客观呈现；与 Wieland 篇对照时各自忠实本页
- [ ] 全篇无编造引语；引号内不出现 page.md 无法溯源的"原话"
- [ ] 封面/身份页装饰圆占位；封面国籍行明示德国
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Adolf_Windaus/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **肖像**：确认为装饰圆占位（无真实肖像），未误用墓碑照/结构图
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：全篇无引语——若有引语一律删除或改为间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger / van 't Hoff 等）对齐
