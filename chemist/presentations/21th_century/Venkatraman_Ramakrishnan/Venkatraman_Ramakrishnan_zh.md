# Venkatraman Ramakrishnan（文卡特拉曼·拉马克里希南）立传提示词

> qid=Q60061 · 1952 年生于印度泰米尔纳德邦奇丹巴拉姆（在世，页面仅载出生年份） · 英美双籍结构生物学家 · 21 世纪 · 诺贝尔化学奖（2009，与 Steitz / Yonath 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Venkatraman_Ramakrishnan/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本篇的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用 `images/` 目录本地文件，若缺省用装饰圆占位；可用 2009 年诺奖记者会照片）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cubes}\enspace 读懂核糖体的人\enspace·\enspace 英国 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（双籍）、出生地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「核糖体的大分子复合物」母题——成簇圆点暗示 30S 亚基中 RNA 与 20 余种蛋白的组装。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 30S 亚基 5.5 Å 分辨率、全核糖体 tRNA+mRNA 复合物原子结构。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Venkatraman Ramakrishnan（中文惯称：文卡特拉曼·拉马克里希南；惯称 Venki Ramakrishnan）
- **生卒**：1952 年生于印度泰米尔纳德邦 Cuddalore 县奇丹巴拉姆（Chidambaram，时属 Madras State）——**页面仅载出生年份**，frontmatter 双值（1952-01-01 / 1952-04-04）系噪声，正文无月日；在世（页面无卒日）
- **国籍**：Citizenship **United Kingdom + United States**（infobox 明载双籍；frontmatter 仅 United States 系噪声）；印度裔英美双重叙事
- **身份**：英裔美国结构生物学家（British-American structural biologist）；MRC 分子生物学实验室（LMB）课题组组长；Trinity College, Cambridge Fellow
- **家庭**：父 Prof. C. V. Ramakrishnan 为巴罗达 Maharaja Sayajirao 大学生化系主任（其出生时在威斯康星大学麦迪逊分校随 David E. Green 做博士后）；母 Rajalakshmi Ramakrishnan 为科学家（1959 年仅用 18 个月获 McGill 心理学博士，Hebb 亦为其指导者之一）；妹 Lalita Ramakrishnan 为剑桥大学免疫与感染病学教授、美国科学院院士。1975 娶 Vera Rosenberry（童书作家与插画家）；继女 Tanya Kapka（医师），子 Raman Ramakrishnan（大提琴家、Bard College 教授）
- **教育轨迹**：
  - 巴罗达（Vadodara）Convent of Jesus and Mary 全程就学（仅 1960–61 随家在阿德莱德一年半）
  - Maharaja Sayajirao University of Baroda：National Science Talent Scholarship；1971 获物理学 BSc（课程基于 Berkeley Physics Course 与费曼物理学讲义）
  - Ohio University：1976 获**物理学** PhD（KDP 铁电相变研究，导师 Tomoyasu Tanaka）
  - UC San Diego：两年生物学研究生，从理论物理转向生物学
- **导师**：Tomoyasu Tanaka（俄亥俄大学物理学博士导师）；Peter Moore（耶鲁博士后导师）
- **研究领域**：结构生物学——核糖体结构与功能、大分子晶体学、染色质结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **学者之家（1952）**：父母皆为科学家，生于泰米尔纳德邦奇丹巴拉姆，长于古吉拉特邦巴罗达。
2. **物理学出身（1971）**：巴罗达大学物理 BSc——课程以伯克利物理教程与费曼讲义为蓝本。
3. **俄亥俄的物理博士（1976）**：KDP（磷酸二氢钾）铁电相变的格林函数理论研究，获物理学博士——他是"物理学博士转行生物学"的典型。
4. **转行的两年（1976–1978）**：UC San Diego 生物学研究生，完成从理论物理到生物学的跨越。
5. **耶鲁入门核糖体**：随 Peter Moore 做博士后，自此一生研究核糖体。
6. **约 50 所大学的拒绝**：博士后后在美国约 50 所大学求职未果——履历上最"失败"的一段，后来成了最好的注脚（page.md 明载）。
7. **Brookhaven 岁月（1983–1995）**：staff scientist，坚持核糖体方向。
8. **犹他教授（1995–1999）**：University of Utah 生物化学教授。
9. **落脚 LMB（1999–）**：移居剑桥 MRC 分子生物学实验室任课题组组长（1991–92 曾以 Guggenheim Fellowship 交换访问于此）；Trinity College Fellow。
10. **30S 亚基攻坚（1999–2000）**：1999 发表 30S 亚基 5.5 Å 分辨率结构；翌年测定 **30S 亚基完整分子结构**及其与多种抗生素的复合物——并给出蛋白质生物合成保真性机制的结构洞见。
11. **全核糖体原子结构（2007）**：测定核糖体整体与 tRNA、mRNA 配体的原子结构。
12. **2009 诺贝尔化学奖（三人共享）**：与 **Thomas A. Steitz**、**Ada Yonath** 共享，表彰核糖体结构与功能研究；诺奖演讲 "Unraveling the Structure of the Ribosome"（2009-12-08）。
13. **皇家学会第 62 任会长（2015–2020）**：继 Paul Nurse、后由 Adrian Smith 接任；卸任后 2022 获 Order of Merit；另著有《Gene Machine》（2018）与《Why We Die》（2024）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（绛石深红 deepribosome） | `#8A1E2D` | 核糖体结构解析的深绛红——大分子晶体学衍射图样的母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（30S 亚基 badge30S） | `#2C5F8A` | 蓝 30S 亚基结构攻坚 |
| 分类色 2（全核糖体 badge70S） | `#1B6B52` | 绿 70S 全核糖体 + tRNA/mRNA 复合物 |
| 分类色 3（抗生素 badgeAB） | `#8A5A2C` | 琥珀抗生素结合与翻译保真 |
| 分类色 4（皇家学会 badgeRS） | `#5B4A2F` | 褐 Royal Society 会长与 OM |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「核糖体大分子复合物的组装」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（文件 `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`；不要复制 wav 文件，Makefile 直接引用）
- **风格**：史诗 / 上升感 / 管弦
- **匹配理由**：
  - "上升" 匹配其弧线——被 50 所大学拒绝的落魄博士后，一路登上诺贝尔奖台与皇家学会会长之位
  - "史诗管弦" 呼应 30S 亚基这台"蛋白质合成机器"被原子级揭幕的宏大叙事
  - "Sci-Fi Trailer" 的科技感契合晶体学电子密度图渐次显影的画面感

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 读懂核糖体的人 / Venkatraman Ramakrishnan 1952– + 四色 badge + 右上头像 + 国籍行（英/美双籍）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/双籍/教育/博士导师/领域/机构/荣誉）
03  拉马克里希南的一生 — Sanger 式时间线（10 节点：1952→1971→1976→1978→1983→1995→1999→2000→2009→2015）
04  学者之家与物理学出身 (1952–1971) — 表格「时间|事件|结果」
05  从物理到生物的转行 (1971–1978) — 表格「时间|事件|结果」（Ohio 博士 / UCSD 转向）
06  耶鲁入门与求职长夜 (1978–1983) — 表格「问题|方法|结果」（Peter Moore 博士后 / 50 校拒绝）
07  Brookhaven 与犹他 (1983–1999) — 表格「时间|事件|结果」
08  30S 亚基攻坚 (1999–2000) — 表格「挑战|方法|结果」+ 公式框：30S 亚基 5.5 Å → 完整结构
09  2009 诺贝尔化学奖 — 公式框：核糖体结构与功能 + 三人共享 + 诺奖演讲标题
10  全核糖体与翻译保真 (2007–) — 表格「对象|方法|结果」+ 公式框：70S+tRNA+mRNA 原子结构
11  皇家学会会长 (2015–2020) — 高斯式流程图（FRS 2003 → 会长 2015 → OM 2022）
12  荣誉长廊 — Sanger 式「类别|代表|意义」表格（Padma Vibhushan 2010 / Knight Bachelor 2012 / Sir Hans Krebs Medal itemize）
13  遗产：翻译机器的原子级蓝图 — 四分类遗产盒 + 公式框：皇家学会当选证书引文（30S 抗生素作用模式）
14  结尾 — 「生命以核糖体书写蛋白质，他以原子级精度读出了这部书。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2009 获奖 | **三人共享**（Ramakrishnan / Thomas A. Steitz / Ada Yonath，规范全名）；口径 "research on the structure and function of ribosomes"——勿写独享或"发明核糖体" |
| 出生日期 | 页面正文**仅载 1952 年**；frontmatter 双值（1952-01-01 / 1952-04-04）系噪声——Beamer 一律写"1952 年生"，禁止杜撰月日 |
| 国籍 | infobox Citizenship 为 **United Kingdom + United States**（双籍）；frontmatter 仅 United States 系噪声；印度裔出身客观带过 |
| 博士口径 | PhD 是**物理学**（Ohio University 1976，KDP 铁电相变）——勿写成生物学/化学博士；UC San Diego 是"两年生物学研究生"非学位 |
| 博士导师 | **Tomoyasu Tanaka**（Ohio 物理学）；Peter Moore 是**耶鲁博士后导师**（advisor-student，note 注明博士后导师，非博士导师） |
| 求职被拒 | "约 50 所美国大学未果"为 page.md 明载，可写；勿加"最惨诺奖得主"类渲染 |
| 皇家学会会长 | 第 62 任，2015-12-01 – 2020-11-30；继 Paul Nurse、后接 Adrian Smith——年份口径勿错 |
| 爵位 | Knight Bachelor（2012 新年授勋）但**一般不用 "Sir" 头衔**（page.md 明载）——勿写"受封爵士并使用头衔" |
| Padma Vibhushan | 2010，印度**第二高**平民荣誉（page.md 原文口径）——勿写成最高 |
| Brexit 表述 | 任内主导议题为 Brexit 与疫情（page.md 载其公开言论）——最多一句客观带过，不展开政治评论 |
| 学生入库 | 仅 metadata `doctoral_student: William M Clemons`，page.md 正文无——**不予入库**；正文亦未列具体博士生 |
| 引语 | 仅可用 page.md 原载：皇家学会当选证书引文、Brexit 相关两段原话（如使用须完整忠实）——其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q60061 | ✅ |
| name_zh | 文卡特拉曼·拉马克里希南 | ✅ |
| name_en | Venkatraman Ramakrishnan | ✅ |
| birth_date | 1952（页面仅载年份；frontmatter 双值噪声，月日不填） | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United Kingdom + United States（双籍，UK 居前） | ✅ |
| primary_occupation | structural biologist | ✅ |
| field_of_work | structural biology（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | structural biology | 结构生物学 |
| 1 | molecular biology | 分子生物学 |
| 2 | biochemistry | 生物化学 |
| 3 | biophysics | 生物物理学 |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Tomoyasu Tanaka | 师→生（博士导师） | 俄亥俄大学物理学博士导师，1976（KDP 铁电相变） |
| advisor-student | Peter Moore | 师→生（博士后导师） | 耶鲁大学博士后导师，自此研究核糖体 |
| co-honored | Thomas A. Steitz | 无向 | 2009 诺贝尔化学奖共同得主（规范全名） |
| co-honored | Ada Yonath | 无向 | 2009 诺贝尔化学奖共同得主（规范全名） |
| spouse | Vera Rosenberry | 无向 | 1975 结婚，童书作家与插画家 |
| parent-child | C. V. Ramakrishnan | 父→本人 | 巴罗达大学生化系主任 |
| parent-child | Rajalakshmi Ramakrishnan | 母→本人 | 科学家，McGill 心理学博士 |
| parent-child | Raman Ramakrishnan | 本人→子 | 大提琴家，Bard College 教授 |
| parent-child | Tanya Kapka | 本人→继女 | 医师（page.md 明载 step-daughter） |
| sibling | Lalita Ramakrishnan | 无向 | 妹，剑桥大学免疫与感染病学教授 |

> 禁入库：William M Clemons（metadata.json `doctoral_student` 有载而 page.md 正文无）；David E. Green（父亲在美的博士后导师，与本人无关系）；Donald O. Hebb（母亲的指导者之一）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2009，与 Steitz / Yonath 三人共享）
- Padma Vibhushan（2010，印度第二高平民荣誉）
- Order of Merit, OM（2022）；Knight Bachelor（2012 新年授勋，一般不用 Sir 头衔）
- Louis-Jeantet Prize for Medicine（2007）；Datta Lectureship and Medal, FEBS（2007）
- Sir Hans Krebs Medal, FEBS（2012）；Heatley Medal, Biochemical Society（2008）
- XLVI Jiménez-Díaz Prize（2014）；Golden Plate Award（2017）
- Fellow of the Royal Society, FRS（2003）；EMBO Member（2002）；U.S. National Academy of Sciences（2004）
- German Academy of Sciences Leopoldina；Honorary Fellow of the Academy of Medical Sciences（2010）
- Indian National Science Academy 外籍会士（2008）；American Philosophical Society（2020）
- Guggenheim Fellowship（1991–92 交换访问 LMB）
- 荣誉学位：Maharaja Sayajirao University of Baroda、University of Utah、Ohio University、University of Cambridge
- NDTV "25 Greatest Global Living Indians"（2013-12-14）

## 9. 机构清单

- 教育：Convent of Jesus and Mary（巴罗达）；Maharaja Sayajirao University of Baroda（BSc 物理学 1971）；Ohio University（PhD 物理学 1976）；UC San Diego（两年生物学研究生）
- 任职：Yale University（Peter Moore 组博士后）→ Brookhaven National Laboratory（staff scientist，1983–1995）→ University of Utah（生物化学教授，1995–1999）→ MRC Laboratory of Molecular Biology, Cambridge（课题组组长，1999–；Trinity College Fellow）
- 荣职：President of the Royal Society（第 62 任，2015–2020）；British Library 董事会成员（2020–）

## 10. 终审清单

- [x] 生年 1952（无月日，页面口径），在世留白；出生地奇丹巴拉姆
- [x] 2009 三人共享（Steitz / Yonath 规范全名）；"核糖体结构与功能"口径忠实
- [x] 双籍 UK + US 表述准确；博士为物理学（Ohio 1976）转行叙事准确
- [x] 博士导师 Tanaka / 博士后导师 Moore 双关系注记清晰
- [x] Knight Bachelor 不用 Sir、Padma Vibhushan 第二高平民荣誉口径准确
- [x] 引语仅皇家学会证书等 page.md 原载
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Venkatraman_Ramakrishnan/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 目录 2009 年诺奖记者会照片就位（缺省装饰圆占位）
- [ ] 国籍：封面顶部明示英国/美国双籍
- [ ] 引语核对：引语必须在 page.md 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
