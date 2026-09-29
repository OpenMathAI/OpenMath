# Fritz Pregl（弗里茨·普雷格尔）立传提示词

> qid=Q78482 · 1869-09-03 – 1930-12-13 · 斯洛文尼亚裔奥地利化学家/医师 · 20 世纪 · 诺贝尔化学奖（1923，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Fritz_Pregl/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。★ 本人物 images.txt **无真实肖像**（仅卢布尔雅那出生房屋照片，禁充当肖像）——封面与身份页均用**装饰圆占位**（主色实心圆 + 姓名首字母缩写 FP）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{balance-scale}\enspace 微量分析之父\enspace·\enspace 奥地利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、受洗名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「微量」母题——大量细小离散圆点渐次汇聚，暗示从毫克到微克的尺度跨越。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「样品需求 ↓ 50 倍」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Fritz Pregl（斯洛文尼亚语：Friderik Pregl；受洗名 Friedrich Michael Raimund Pregl；中文惯称：弗里茨·普雷格尔）
- **生卒**：1869-09-03 生于 Laibach（Duchy of Carniola, Cisleithania, Austria-Hungary，今卢布尔雅那 Ljubljana，斯洛文尼亚）→ 1930-12-13 逝于 Graz, Styria, Austria，享年 61
- **国籍**：Austria（奥地利；Slovene-Austrian 双语背景——父斯洛文尼亚语、母德语）
- **身份**：化学家、医师（chemist & physician）
- **教育轨迹**：University of Graz 学医（具体入学/毕业年份页面无载）——先习医，再以化学（尤其化学生理学）立业
- **博士导师**：Alexander Rollett（infobox Doctoral advisor 一行明载）
- **研究领域**：chemistry、medicine——定量有机微量分析（microanalysis）、元素分析（elemental analysis）、化学生理学（chemical physiology）、胆汁酸（bile acids）
- **职务**（infobox Occupations 一行）：Graz 巡回法医化学家（1907）；Graz 大学医学院院长（1916-1917）；Graz 大学副校长（Vice Chancellor，1920-1921）
- **机构**：University of Graz、University of Innsbruck

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **双语边界的医生之家（1869）**：生于奥地利-匈牙利帝国治下的卢布尔雅那（时称 Laibach），父斯洛文尼亚语、母德语——帝国边界上的混合语家庭，受洗名 Friedrich Michael Raimund Pregl。
2. **从医学转向化学**：在 University of Graz 学医，专注生理学尤其化学生理学——先有医者视角，后有分析化学利器。
3. **胆汁酸之困**：胆汁酸研究获得的样品量极少，常量元素分析根本无从下手——微量分析革命的原点是"样品不够用"。
4. **燃烧装置（combustion train）改良**：对元素分析的核心装备动刀，把常规燃烧分析压缩到微量尺度。
5. **样品需求降低 50 倍**：研究收官时，分析所需最小样品量降低了 50 倍——一整个数量级的跨越。
6. **方法开放传播**：主动邀请各地化学家来学习他的元素分析方法，方法迅速被广泛接受——不垄断、速普及。
7. **1907 巡回法医化学家**：infobox 载其任 Graz circuit forensic chemist——分析功力服务司法实践。
8. **1914 Lieben Prize**：奥地利科学界重要奖项，诺奖前 9 年的先声。
9. **行政三职**：1916-1917 任 Graz 大学医学院院长、1920-1921 任副校长——医学院出身的化学家执掌校政。
10. **1923 诺贝尔化学奖**：表彰其对定量有机微量分析的重要贡献，其一即燃烧装置技术的改良；诺奖演讲 1923-12-11《Quantitative Micro-Analysis of Organic Substances》。
11. **早逝（1930）**：1930-12-13 逝于 Graz，享年 61——获奖仅 7 年后，未及亲见方法学的全面开花。
12. **以遗产设奖（1931–）**：Fritz Pregl Prize 自 1931 年起由奥地利科学院以其留下的资金每年颁发（化学）——科学遗产的直接延续。
13. **两国的纪念版图**：1950 年 Graz 大学其工作过的系命名 Institute of Medical Chemistry and Pregl Laboratory；Graz/Innsbruck/Vienna/Klagenfurt 街道以其命名；斯洛文尼亚自 2007 年起每年颁发 Pregl Awards；卢布尔雅那有 Pregl 广场。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#2A3468` | 精密天平与深夜实验室的克制与严谨（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（微量分析 badgeMicro） | `#4A5FA5` | 靛蓝微量称量 / 燃烧装置 |
| 分类色 2（胆汁酸 badgeBile） | `#1B7A43` | 绿胆汁酸 / 化学生理学 |
| 分类色 3（公共服务 badgeAdmin） | `#D97B29` | 琥珀院长 / 副校长 / 法医化学 |
| 分类色 4（纪念传承 badgeLegacy） | `#C0395B` | 玫瑰 Pregl Prize / 纪念版图 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆 + 若干细小圆点），呼应「微量」——尺度越小、精度越高。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；不要复制 wav 文件，Makefile 引用路径即可）
- **风格**：深沉 / 悲怆 / 纪录片
- **匹配理由**：
  - "悲怆" 匹配其命运底色——1869 生于帝国边陲，1930 获奖仅 7 年后即早逝，享年 61，方法学尚未看尽花开
  - "深沉" 匹配微量分析的气质——毫厘之间的极静与极精，克制的匠心
  - "纪录片" 匹配传记叙事——卢布尔雅那 → 格拉茨学医 → 胆汁酸之困 → 微量分析革命 → 1923 诺奖 → 遗产设奖
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 微量分析之父 / Fritz Pregl 1869–1930 + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/受洗名/国籍/教育/博士导师/出生地/去世地/领域/职务/荣誉）
03  普雷格尔的一生 — Sanger 式时间线（10 节点：1869→1907→1914→1916→1920→1923→1930→1931→1950→2007）
04  双语边界的医生之家 (1869–) — 表格「时间|事件|结果」（出生地/受洗名/双语家庭）
05  从医学到化学生理学 — 表格「阶段|转向|结果」（学医→化学生理学；年份无载如实标注）
06  胆汁酸之困 — 表格「问题|方法|结果」+ 公式框：样品需求 ↓ 50 倍
07  微量分析革命 — 表格「问题|方法|结果」（燃烧装置改良 + 方法开放传播）
08  1923 诺贝尔化学奖 — 表格 + 公式框：诺奖演讲标题 Quantitative Micro-Analysis of Organic Substances (1923-12-11)
09  公共服务 — 表格「年份|职务|意义」（1907 法医化学家 / 1916-17 院长 / 1920-21 副校长）
10  早逝与以他命名的奖 — 高斯 FFT 页式流程图（1930 去世 → 1931 Fritz Pregl Prize）
11  纪念版图 — 「类别|代表|意义」表格（研究所/街道/广场/年度奖）
12  遗产：微量分析改变有机化学 — 四分类遗产盒 + 公式框
13  精神总结 — "小样品、大科学"的匠心
14  结尾 — 「毫厘之间，见微知著。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 博士导师冲突 | infobox 作 **Alexander Rollett**；frontmatter `doctoral_advisor: Wilhelm Ostwald` 与 infobox 冲突——以 infobox 为准，Ostwald 禁写入师承（§7 禁入库名单） |
| 博士年份 | 页面无载入学/毕业/博士年份——禁写"1889 年获博士"等任何编造年份 |
| 国籍口径 | 出生当时属 Austria-Hungary（Cisleithania 的 Carniola 公国，今斯洛文尼亚卢布尔雅那）；身份是 Slovene-Austrian 化学家兼医师——勿单写"斯洛文尼亚化学家"，国籍入库用 Austria |
| frontmatter 国籍噪声 | `Cisleithania / Kingdom of Yugoslavia / Kingdom of Serbs, Croats and Slovenes` 为历史政区，不作为现代国籍入库 |
| 获奖理由口径 | page.md 原文 "for making important contributions to quantitative organic microanalysis, one of which was the improvement of the combustion train technique"——勿泛化成"发明有机化学"或"发明微量天平" |
| 行政两职勿混 | 1916-1917 医学院**院长**（Dean of the Medical Faculty）、1920-1921 大学**副校长**（Vice Chancellor）——勿互换年份或混为一职 |
| 享年 | 1869-09-03 → 1930-12-13，享年 61——勿算成 62 |
| Pregl Prize vs Pregl Awards | **Fritz Pregl Prize**：1931 起、奥地利科学院、用其遗产、化学——**Pregl Awards**：2007 起、斯洛文尼亚国家化学研究所（含学生奖与中学生奖）——勿混 |
| 纪念时间 | 1950 年研究所命名（Institute of Medical Chemistry and Pregl Laboratory）——勿写 1931 |
| 肖像 | images.txt 仅有出生房屋照片——**禁用出生地照充当肖像**，封面/身份页用装饰圆占位 |
| 引语 | 页面全文无直接引语——全篇禁编造引语，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q78482 | ✅ |
| name_zh | 弗里茨·普雷格尔 | ✅ |
| name_en | Fritz Pregl | ✅ |
| birth_date | 1869-09-03 | ✅ |
| death_date | 1930-12-13 | ✅ |
| nationality | Austria | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry / medicine（person_field 细分见下表） | ✅ |
| has_biography | 0（待立传后置 1） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | microanalysis | 微量分析 |
| 1 | elemental analysis | 元素分析 |
| 2 | chemical physiology | 化学生理学 |
| 3 | bile acids | 胆汁酸 |

## 7. 社会关系入库清单

**★ 红线**：只收 page.md 正文或 infobox 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alexander Rollett | 师→生（博士导师） | infobox Doctoral advisor 明载 |

**禁入库名单（metadata.json-only / 仅 frontmatter 有载，页面正文与 infobox 无载）**：

> Wilhelm Ostwald（frontmatter `doctoral_advisor` 有载，但与 infobox 的 Alexander Rollett 冲突，按红线禁入库）；其余页面无任何明载社会关系（无配偶、无子女、无门生记载）——relations=1 为诚实值。

## 8. 奖项清单

- Nobel Prize in Chemistry（1923，独享；诺奖演讲 1923-12-11 Quantitative Micro-Analysis of Organic Substances）
- Lieben Prize（1914）
- Fritz Pregl Prize（1931 起，奥地利科学院以其遗产设立——纪念性质）

## 9. 机构清单

- 教育：University of Graz（医学）
- 任职：University of Graz（巡回法医化学家 1907；医学院院长 1916-1917；副校长 1920-1921）、University of Innsbruck（infobox Institutions 载名，细节无载）
- 命名机构：Institute of Medical Chemistry and Pregl Laboratory（1950，Graz 大学）

## 10. 终审清单

- [ ] 生卒 1869-09-03 / 1930-12-13，享年 61，出生地 Laibach（今 Ljubljana）、去世地 Graz
- [ ] 博士导师只写 Alexander Rollett（infobox 口径）；Ostwald 不出现于师承
- [ ] 全篇不出现编造的求学/博士年份
- [ ] 获奖理由忠实 page.md 原文（微量分析 + 燃烧装置改良）
- [ ] Pregl Prize（1931，奥地利科学院）与 Pregl Awards（2007，斯洛文尼亚）两处分清
- [ ] 全篇无直接引语；引号内不出现 page.md 无法溯源的"原话"
- [ ] 封面/身份页装饰圆占位；封面国籍行明示奥地利
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Fritz_Pregl/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **肖像**：确认为装饰圆占位（无真实肖像），未误用出生房屋照片
- [ ] **国籍**：封面顶部明示奥地利；Slovene-Austrian 双背景表述准确
- [ ] **引语核对**：全篇无引语——若有引语一律删除或改为间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger / van 't Hoff 等）对齐
