# Rafael Bombelli（拉斐尔·邦贝利）立传提示词

> qid=Q358547 · 1526-01-20（受洗）– 1572 · 意大利数学家 · 16 世纪（虚数 understanding 的中心人物）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Rafael_Bombelli/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（page.md 无邦贝利本人肖像——`images.txt` 首二图是《代数》1579 博洛尼亚版扉页与 1572 版书影，**非肖像**；无真肖像则用装饰圆 `\faIcon{user}` 占位，书影可作叙事插图）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆占位）+ 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应「实部与虚部」交叠的母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Rafael Bombelli（本姓 Mazzoli，父辈为避家族恶名改姓 Bombelli；中文惯称：拉斐尔·邦贝利）
- **生卒**：1526-01-20 于博洛尼亚**受洗**（baptised，生年按 1526）→ 1572 逝于罗马
- **国籍**：教宗国（Papal States，metadata 明载；生卒地博洛尼亚/罗马均属之）——现代对应写「意大利」
- **身份**：数学家、工程师（engineer）
- **家庭**：父 Antonio Mazzoli（羊毛商，改姓 Bombelli）、母 Diamante Scudieri（裁缝之女）；六子女中最年长；祖父曾参与 1508 年 Bentivoglio 复辟博洛尼亚的政变，事败被俘处决
- **教育轨迹**：**未受大学教育**（received no college education），由工程师建筑师 Pier Francesco Clementi 传授（红链人名）
- **导师**：Pier Francesco Clementi（工程师建筑师，职业启蒙）
- **研究领域**：代数（algebra）、数学（mathematics）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **虚数运算规则的确立者**：page.md 定位——"a central figure in the understanding of imaginary numbers"、"the one who finally managed to address the problem with imaginary numbers"；学界**普遍视为复数的发明者**（generally regarded as the inventor of complex numbers）。
2. **《代数》（L'Algebra，1572）**：对当时已知代数的全面综述；写作动机——嫌同时代名家著作晦涩，要写一本**人人可读、自足**的代数书。
3. **欧洲第一个写下负数运算法则的人**：page.md 明载 "the first European to write down the way of performing computations with negative numbers"，附韵文口诀原文（"Plus times plus makes plus / Minus times minus makes plus / ..."）。
4. **"plus of minus" 与 "minus of minus"**：给负数的平方根专门命名，明确它们**既非正也非负**——避免了 Euler 时代仍会遇到的混淆；给出复数乘法口诀原文（"Plus of minus by plus of minus, makes minus / ..."）。
5. **casus irreducibilis 的突破**：用 del Ferro 方法在不可约情形下求出实解——Cardano 等人在此**放弃**的地方，邦贝利拿到了结果。
6. **印刷本中最早的指数记号**：《代数》第二卷首创 `1U3 a. 6U1 p. 40`（即 x³=6x+40）的碗形上标记号——完整符号代数随后才由韦达发展。
7. **连分数思想的先声**：用与简单连分数相关的迭代法逼近平方根（√13 的近似列 3 2/3, 3 3/5, 3 20/33, ... 收敛到 3.605550883...；265/153 与 1351/780 正是阿基米德定 π 用的界）。
8. **莱布尼茨的盛赞**：读《代数》后称邦贝利为 "an outstanding master of the analytical art"；1976 年月球环形山以他命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青） | `#1F4E5F` | 工程师数学家的冷峻底色 / 台伯河水 |
| 强调色（古铜金） | `#C9A227` | 1572《代数》刊本的 dignitas |
| 分类色 1（虚数 — 幻紫） | `#7C3AED` | plus of minus / 复数运算 |
| 分类色 2（负数 — 琥珀） | `#E07B30` | 负数四则口诀 |
| 分类色 3（记号法 — 青绿） | `#0E7C7B` | U 形指数记号 |
| 分类色 4（逼近法 — 靛蓝） | `#4C5FD5` | 平方根迭代 / 连分数先声 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「实部 ⊕ 虚部」两界交叠的结构之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Mirage**（Notan Nigres，本地文件 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`）
- **风格定调**：**梦幻 / 抽象 / 电子**（虚数——16 世纪最「不真实」的数学对象）
- **匹配理由**：
  - 「抽象思维、猜想提出」标签精确匹配负数平方根这一当时被视为怪物的对象；
  - 「梦幻」呼应 "plus of minus" 介于正负之外、如海市蜃楼般的数；
  - 与组内 Ferrari（Savage 紧张论战）、Clavius（The Flow of Time 历法时间感）风格互不重复，三人覆盖「攻克 / 虚幻 / 庄重」三种气质。
  - 时长需 ≥ 13 页 × 7 秒 ≈ 91 秒，ffmpeg `-shortest` 自动对齐。

## 4. Slide 规划（约 13 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「虚数的驯服者」+ 拉斐尔·邦贝利 1526–1572 + 右上头像（装饰圆占位，可用《代数》1572 书影小图点缀）+ 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像（装饰圆）+ 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **邦贝利的一生：时间线**（`\timelineslide`）：1526-01-20 博洛尼亚受洗 → 家族改姓 Mazzoli→Bombelli → 师从工程师 Clementi → 1572《代数》出版 → 1572 卒于罗马（page.md 仅这四个有年份锚点）
4. **家族与早年**（`\earlyslide`）：Mazzoli 家族兴衰、1506 尤利乌斯二世放逐 Bentivoglio、1508 政变失败祖父被处决、父改姓 Bombelli；六子女中最长
5. **没有大学的工程师数学家**（表格）：无大学教育、师从 Pier Francesco Clementi；「写一本人人可读的代数书」的动机
6. **《代数》（1572）：全面综述与负数运算法则**（核心贡献页，表格 + 公式框）：欧洲第一个写下负数运算者；韵文口诀原文引用框
7. **记号法：印刷本最早的指数记号**（核心贡献页，表格 + 公式框）：`1U3 a. 6U1 p. 40` ↔ x³=6x+40；碗形上标；韦达随后发展完整符号代数
8. **复数运算规则**（核心贡献页，表格 + 公式框）：discriminant 判据 (a/3)³>(b/2)²、"plus of minus"/"minus of minus" 命名、复数乘法口诀原文引用框、实部归实部虚部归虚部
9. **casus irreducibilis 的突破**（核心贡献页，表格 + 公式框）：用 del Ferro 方法在不可约情形求出实解；Cardano 等人在此放弃
10. **平方根的迭代逼近**（核心贡献页，表格 + 公式框）：n=(a±r)² 展开、√13 近似收敛列、265/153 与 1351/780（阿基米德定 π 的界）；与 Heron / Archimedes 方法对比；Cataldi 1613 版算法注记
11. **声誉与身后**（表格）：复数发明者之誉（generally regarded）、莱布尼茨 "outstanding master of the analytical art"、Crossley 评语、1976 月球环形山 Bombelli
12. **终章**：1572 卒于罗马、虚数先驱的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **★ 卒年裁定**：metadata.json date_of_death 双值 ["1573","1572"] 有噪声；page.md 正文两处明载 **1572**（"died 1572" / "Bombelli died in 1572 in Rome"）——**取 1572，弃 1573**。
- **★ 生年口径**：page.md 只载**受洗日** 1526-01-20（baptised）——生年写 1526、日期写「受洗」口径，禁写「出生于 1526-01-20」（page.md 无确切出生日）。
- **★ "wild thought" 引语禁写**：任务单提示「'wild thought' 引语若用须 page.md 原文」——**page.md 全文无 "wild thought" 字样，禁用该引语**。可用引语仅限：负数口诀韵文、复数乘法口诀韵文（均为 page.md 原文）与莱布尼茨评语。
- **「复数发明者」口径**：须按 page.md 原文 "generally regarded as the inventor of complex numbers"（**普遍视为**），禁写绝对化的「发明了复数」。
- **出生地**：metadata place_of_birth 含 Borgo Panigale，page.md 只载 Bologna——**以 page.md 为准**，写博洛尼亚。
- **师承**：Pier Francisco Clementi 为**工程师建筑师**（engineer-architect），职业启蒙而非大学导师；人名在 Wikipedia 为红链，note 照写、勿补无载生平。
- **与 Cardano**：page.md 仅载 Cardano 在 casus irreducibilis 「放弃」作对比——**无私人关系记载，禁建关系**。
- **del Ferro / Tartaglia**：page.md 载其书 "solved equations using the method of del Ferro/Tartaglia"——方法来源可写，属**著作影响**（influence），非师承或私交；del Ferro 卒于 1526、Tartaglia 论战属 Ferrari/Cardano 侧，均无与邦贝利的直接交往记载。
- **莱布尼茨**：读《代数》后盛赞——晚邦贝利约百年的**著作影响**，非同时代人交往；引用评语 ". . . outstanding master of the analytical art." 须按 page.md 原样（含省略号与句点）。
- **连分数**：邦贝利方法 "related to simple continued fraction" 但**当时尚无连分数概念**；页载算法是 Cataldi（1613）的后期版本——禁写「发明了连分数」。
- **国籍**：metadata 明载 Papal States；现代对应意大利——入库两行（Italy rank 0 现代口径可省，按 Johann Bernoulli 先例写 Papal States historical + Italy）。**裁定：入库 Papal States（era_note: historical, rank 0）+ Italy（rank 1）**，封面国籍行写「意大利」。
- **肖像红线**：`images.txt` 两图均为《代数》书影/扉页（1579 博洛尼亚版、1572 版），**非肖像**——禁充当头像；无真肖像用装饰圆占位。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q358547 | 待写入 |
| name_zh | 拉斐尔·邦贝利 | 待写入 |
| name_en | Rafael Bombelli（metadata label） | 待写入 |
| birth_date | 1526-01-20（受洗日口径） | 待写入 |
| death_date | 1572 | 待写入 |
| nationality | Papal States（era_note historical）+ Italy | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | algebra / mathematics | 待写入 |
| has_biography | false（本次只入库社会关系，Beamer 立传待做） | 待写入 |

## 7. 社会关系入库清单

- **导师**：Pier Francesco Clementi（advisor-student, direction: advisor——工程师建筑师，职业启蒙）
- **父**：Antonio Mazzoli（parent-child, direction: parent——羊毛商，改姓 Bombelli）
- **母**：Diamante Scudieri（parent-child, direction: parent——裁缝之女）
- **思想影响（方法来源）**：Scipione del Ferro（influence——1572《代数》采用其三次方程解法）
- **思想影响（方法来源）**：Niccolò Tartaglia（influence——同上；★ 规范名 "Niccolò Tartaglia"，与 Ferrari 篇/A 组保持一致防分裂）
- **思想影响（著作）**：Gottfried Wilhelm Leibniz（influence——读《代数》后盛赞，库内规范名命中 id=1221）
- **不入库**（page.md 无载或无对应类型）：祖父（参与 1508 政变者，无 grandparent 类型，且 page.md 未具名）、Cardano（仅 casus irreducibilis 对比，无私人关系）、Crossley（书评作者非关系）

## 8. 奖项清单

- 无（page.md 无任何奖项记载）
- 荣誉纪念（非奖项，可入叙事不入 awards 表）：月球环形山 Bombelli（1976 年命名）

## 9. 机构清单

- 无（page.md 无任何教育/任职机构记载；无大学教育、职业为工程师，供职机构 page.md 无载——机构表留空）

## 10. 终审清单

- [ ] 卒年 1572（弃 metadata 1573 噪声），卒地罗马；生年为受洗口径 1526-01-20
- [ ] "wild thought" 引语全文未出现，禁用
- [ ] 「复数发明者」带 "generally regarded" 框定
- [ ] 负数口诀 / 复数乘法口诀引语与 page.md 原文逐字一致
- [ ] 连分数写「相关方法、尚无概念」，禁写「发明连分数」
- [ ] 与 Cardano / del Ferro / Tartaglia 均无私人交往记载，关系类型用对（influence 非 advisor）
- [ ] 书影/扉页图不当头像，无真肖像用装饰圆
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像位 + 国籍行 + 气泡背景 + 品牌 OpenMathAI

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Rafael_Bombelli/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认装饰圆占位（无真肖像）；书影仅作插图
- [ ] **国籍**：封面顶部徽章明示意大利
- [ ] **引语核对**：负数口诀、复数口诀、莱布尼茨评语逐字核对 page.md
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Cardano / Ferrari / Viète 篇）格式对齐，复数叙事与 Ferrari 篇三四次方程口径衔接
