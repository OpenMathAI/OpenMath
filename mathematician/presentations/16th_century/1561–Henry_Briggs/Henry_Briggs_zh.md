# Henry Briggs（亨利·布里格斯）立传提示词

> qid=Q335086 · 1561-02-01 – 1630-01-26 · 英格兰数学家 · 16 世纪（核心贡献跨 16–17 世纪）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Henry_Briggs/`（@page.md + metadata.json + images.txt，事实基准以 page.md 为准）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（page.md/images.txt 无人物肖像，只有对数表书影、1625 北美地图与月球环形山照片——**用装饰圆 `\faIcon{user}` 占位**，可在插图页用 `Logarithmorum Chilias Prima` 书影）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英格兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、教育、教席、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应「对数表 / 航海图」的计算母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Henry Briggs（中文惯称：亨利·布里格斯；metadata 条目名 Henry Briggs (mathematician)，消歧义括号不入正文与库）
- **生卒**：1561-02-01 生于约克郡哈利法克斯附近 Warleywood 的 Daisy Bank（Sowerby Bridge 旁）→ 1630-01-26 逝于牛津，享年 68，安葬于牛津 Merton College 礼拜堂
- **国籍**：英格兰（Kingdom of England，英格兰王国）
- **身份**：数学家、天文学家、大学教授；虔诚的清教徒（Puritan），其时代有影响力的教授
- **家庭**：有两个儿子——Henry（后移居弗吉尼亚）与 Thomas（留在英格兰）；page.md 无妻子记载——**配偶勿写**
- **教育轨迹**：
  - 本地文法学校习拉丁文与希腊文
  - 1577 年入剑桥大学 St John's College，1581 年毕业
  - 1588 年当选 St John's College Fellow
  - 1592 年任 Thomas Linacre 创设的物理讲席 reader，并兼授部分数学讲席；同期与 Edward Wright 合作研习航海与天文
- **导师**：无载（page.md 未记载任何导师）
- **研究领域**：数学（对数、数值表格、长除法）、天文学、航海

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **把纳皮尔对数改造成常用对数**：将纳皮尔原制对数改造为以 10 为底的常用对数（log 10 = 1），后世称 **Briggsian logarithms**（布里格斯对数）以志纪念。
2. **两访爱丁堡**：为商讨对数改造两度从伦敦赴爱丁堡面见纳皮尔（见 §5 年份口径）；会谈中布里格斯的重标度方案获得采纳。
3. **《Logarithmorum Chilias Prima》（1617）**：第二次访爱丁堡归来的当年出版——1–1000 整数的 14 位十进制对数表（首千对数）。
4. **《Arithmetica Logarithmica》（1624）**：对开本巨著，1–20000 与 90001–100000 共三万个自然数的 14 位对数表；其间 20001–90000 后由 Adriaan Vlacq 补齐（10 位）。**布里格斯是最早用有限差分法编制函数表的人之一**。
5. **《Trigonometria Britannica》（1633 身后出版，Gouda 印刷）**：每度百分之一的对数正弦与正切表（14 位）+ 15 位自然正弦表 + 10 位正切/正割表；系 1617《Chilias Prima》的后继之作。
6. **首任格雷沙姆学院几何教授（1596）**：在伦敦新创的 Gresham College 任首任几何教授近 23 年，兼授天文与航海，使格雷沙姆学院成为**英格兰数学的中心**，并从那里支持开普勒的新学说。
7. **首任 Savilian 几何教授（1619）**：1619 年出任牛津大学首任 Savilian Professor of Geometry，1620-07 辞去格雷沙姆教席；抵牛津后不久获授 M.A.（incorporated）。
8. **现代长除法算法（c. 1600）**：今日通用的长除法具体算法由布里格斯约 1600 年引入。
9. **航海与地理学**：与 Edward Wright 合作；1602 年《磁偏角求极高表》、1610 年赖特《航海误差》第二版附录「航海改进用表」；1619 年投资伦敦公司；1622 年《西北航道论》小册子。
10. **品格与身后**：Dr Smith《格雷沙姆教授传》称其「品行端方、轻视财富、安于本分」；月球环形山 Briggs 以其命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（学院深红） | `#7A1E28` | 剑桥圣约翰学院 / Savilian 教席的学院红 |
| 强调色（黄铜仪器金） | `#D08C2E` | 象限仪 / 星盘的黄铜计算时代 |
| 分类色 1（常用对数 — 靛蓝） | `#1E4E79` | 布里格斯对数 / 两访纳皮尔 |
| 分类色 2（对数表工程 — 深绿） | `#2F6B4F` | 14 位对数表 / 有限差分法 |
| 分类色 3（航海与制图 — 航海赭） | `#B5651D` | 西北航道 / 磁偏角表 |
| 分类色 4（教席传承 — 石板灰） | `#4A5A6A` | 格雷沙姆 / 牛津双教席 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「对数表格线 / 航海图经纬」的计算秩序感。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Expedition**（Alex-Productions，`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，探索 / 史诗）
- **风格定调**：**开拓与远征**（两访爱丁堡的计算远征 + 航海制图的时代使命）
- **匹配理由**：
  - 布里格斯的核心事业是「把对数变成可用的计算工具」并服务于航海远航时代——Expedition 的**探索 / 远征式叙事**标签与航海、西北航道、伦敦公司投资等经历高度契合
  - 「两个爱丁堡之行的制度化坚韧」匹配史诗推进感
  - 本组三人内不重复：Napier 用 Eternals、Harriot 用 Lonesome
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「常用对数的缔造者」+ 亨利·布里格斯 1561–1630 + 右上装饰圆头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 教席 / 核心领域）
3. **亨利·布里格斯的一生：时间线**（`\timelineslide`）：1561 约克郡出生 → 1577 入剑桥圣约翰 → 1581 毕业 / 1588 Fellow → 1592 Linacre 讲席 reader → 1596 首任格雷沙姆几何教授 → 1616/1617 两访爱丁堡 → 1617《Chilias Prima》→ 1619 Savilian 教授 → 1624《Arithmetica Logarithmica》→ 1630 去世
4. **早年与剑桥**（`\earlyslide`）：约克郡文法学校、圣约翰学院、Linacre 讲席、与 Wright 合作航海天文
5. **格雷沙姆学院：英格兰数学的中心**（核心贡献页，表格）：1596 首任几何教授、近 23 年讲席、支持开普勒新学说
6. **两访纳皮尔：对数的改造**（核心贡献页，表格 + 公式框）：以 10 为底、log 10 = 1、重标度方案获采纳（年份口径见 §5）
7. **《Logarithmorum Chilias Prima》（1617）**（核心贡献页，表格 + 公式框）：1–1000 的 14 位常用对数表
8. **《Arithmetica Logarithmica》（1624）**（核心贡献页，表格 + 公式框）：三万个数的 14 位对数表、有限差分法、Vlacq 补算区间
9. **《Trigonometria Britannica》（1633）**（核心贡献页，表格）：对数正弦正切表 14 位、自然正弦 15 位、Gouda 印刷身后出版
10. **长除法算法（c. 1600）**（核心贡献页，表格 + 公式框）：今日通用长除法的引入者
11. **航海、磁偏角与西北航道**（表格）：1602 磁偏角表、1610 赖特书附录、1619 伦敦公司、1622《西北航道论》
12. **清教徒与反占星**（表格）：与占星作家 Christopher Heydon 之谊、本人以宗教理由拒绝占星（"a mere system of groundless conceits"）
13. **身后与传承**（表格）：Vlacq 续算、Thompson 1952 年 20 位表、月球环形山 Briggs、Merton College 礼拜堂安葬
14. **终章**：68 岁、「让对数可用的工程师头脑」的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **姓名消歧义**：维基条目名 Henry Briggs (mathematician)——正文与数据库 name_en 均写 **Henry Briggs**，括号消歧义不入正文；与同代同姓者勿混。
- **两访爱丁堡年份口径**：Briggs 本人页作 **1616 年首访、次年（1617）再访**；而 Napier 页作 **1615 年 Briggs 来访**——两页口径不一。**本篇沿用 Briggs 页 1616/1617**；任务单若写 1615 以本人页面为准；入库 note 不写具体年份（见 §7）。
- **Bürgi / Dee 渠道说**：page.md 明言 "It has also been suggested"——布里格斯可能经 John Dee 知晓 Jost Bürgi《Fundamentum Astronomiae》之法**仅系推测**，勿写成事实，建议不展开。
- **加州岛制图神话**：1622 年《西北航道论》是 Island of California 制图神话的**已知源头**——客观表述「后世视为该神话之源」，注明其依据是自称见过荷兰带来的地图；1625 年在 Purchas《Pilgrimes》重刊。**不评价其学术失误、不写「愚蠢」等定性词**。
- **占星立场**：布里格斯以宗教理由拒绝占星，名言 "a mere system of groundless conceits"（page.md 原文，可直接引用）；与占星作家 Heydon 是朋友——「友人是占星家而本人反占星」的对照可写。
- **儿子同名**：长子 Henry 与本人同名——正文可写「长子 Henry 移居弗吉尼亚、次子 Thomas 留在英格兰」，**入库时父子关系全部不入库**（Henry 与本人同名会造成自环/分裂 stub，Thomas 仅具名）。
- ** metadata-only 关系**：metadata.json 的 doctoral_student 列有 John Pell——**page.md 正文无载，按 frontmatter-only 纪律不入库**（§7 同步注明）。
- **死亡与安葬**：1630-01-26 卒于牛津（享年 68），葬 Merton College 礼拜堂——「安葬于 Merton」非「任职 Merton」（metadata employer 列 Merton College 系噪声，正文无载任职，勿写）。
- **无获奖记录**：月球环形山命名属身后纪念（eponym），勿写成奖项。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q335086 | 待写入 |
| name_zh | 亨利·布里格斯 | 待写入 |
| name_en | Henry Briggs | 待写入 |
| birth_date | 1561-02-01 | 待写入 |
| death_date | 1630-01-26 | 待写入 |
| nationality | England（Kingdom of England 带 era_note） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / astronomy / navigation | 待写入 |
| has_biography | false | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

> 仅收 page.md 明载关系；note 不写两访爱丁堡具体年份（与 Napier 页口径不一，见 §5）。

- **合作 / 交往**：John Napier（collaborator，面见商讨对数重标度并受纳皮尔之托续算）、Edward Wright（collaborator，剑桥时期合作航海天文、为其著作撰写附录）、Christopher Heydon（collaborator，友人，占星作家）、Adriaan Vlacq（collaborator，续算对数表 20001–90000 区间）
- **思想影响**：Johannes Kepler（influence，在格雷沙姆学院讲席上支持并传播开普勒新学说）
- **不入库**：John Pell（metadata doctoral_student，page.md 无载，frontmatter-only 纪律）、长子 Henry 与次子 Thomas（仅具名；Henry 与本人同名防自环分裂）、James Ussher（仅书目列两封信）、Thomas Linacre（讲席创设者，非个人关系）、Jost Bürgi / John Dee（推测性渠道说，禁写）

## 8. 奖项清单

- page.md 无任何获奖记录——**不设奖项页、不入库**（月球环形山 Briggs 为身后纪念）。

## 9. 机构清单

- 教育：St John's College, Cambridge（1577 年入学，1581 年毕业，1588 年 Fellow）；University of Cambridge
- 任职：Gresham College（首任几何教授，1596–1620）；University of Oxford（Savilian Professor of Geometry，1619–1630）

## 10. 终审清单

- [ ] 生卒 1561-02-01 / 1630-01-26，享年 68，出生地约克郡 Warleywood
- [ ] name_en 用 Henry Briggs（消歧义括号不入库）
- [ ] 两访爱丁堡年份本篇用 1616/1617（沿用本人页面），yaml note 不写年份
- [ ] Bürgi/Dee 渠道保持推测口径或不展开
- [ ] 加州岛神话客观表述不评价
- [ ] John Pell 不入库（metadata-only）；两子不入库（同名防自环）
- [ ] Merton 是安葬地非任职机构
- [ ] 引语必须 page.md 原文；page.md 无载禁写
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Henry_Briggs/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：page.md 无人物肖像——装饰圆占位，插图页可用 Chilias Prima 书影
- [ ] **国籍**：封面顶部徽章明示英格兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "a mere system of groundless conceits"、Dr Smith 品评句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（纳皮尔 / 哈里奥特）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
