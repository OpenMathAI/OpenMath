# Ada Yonath（阿达·约纳特）立传提示词

> qid=Q7426 · 1939-06-22 – 2026-08-31 · 以色列晶体学家 · 21 世纪 · 诺贝尔化学奖（2009，与 Venkatraman Ramakrishnan、Thomas A. Steitz 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Ada_Yonath/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次执行的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Ada_Yonath_Weizmann_Institute_of_Science.jpg` 可从 page.md 图片链接取；若无真实肖像则用装饰圆占位，图注注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 冷冻晶体学先驱\enspace·\enspace 以色列`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「低温晶体 / 核糖体隧道」母题——离散圆点暗示冷冻固定后被逐层解析的结构。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ada Esther Yonath（希伯来文 עדה יונת；娘家姓 **Lifshitz**；中文惯称：阿达·约纳特）
- **生卒**：1939-06-22 生于英属巴勒斯坦托管地耶路撒冷 Geula 区 → 2026-08-31 去世，享年 87
- **国籍**：Israel（以色列；infobox Citizenship: Israeli）
- **身份**：晶体学家 / 结构生物学家；魏茨曼科学研究所 Helen and Milton A. Kimmelman 生物分子结构与组装中心主任；Martin S. and Helen Kimmel 讲席教授
- **家庭**：父母 Hillel 与 Esther Lifshitz 是来自波兰 Zduńska Wola 的犹太移民（1933 年抵巴勒斯坦）；父为拉比世家出身，家营杂货店，父亲 42 岁去世后家迁特拉维夫，少女时代靠帮佣与家教贴补家用；嫁 Moshe Yonath（后离异），女儿 Hagit Yonath 为 Sheba 医疗中心医生，外孙女 Noa；表亲为反占领活动家 Ruchama Marton（两人母亲是姐妹）
- **教育轨迹**：Beit HaKerem 学区学校 → Tichon Hadash 高中（付不起学费，以教数学抵学费）→ Hebrew University of Jerusalem（化学学士 1962、生物化学硕士 1964）→ Weizmann Institute of Science（PhD 1968，胶原 X 射线晶体学研究）
- **导师**：Wolfie Traub（博士导师，正文与 infobox 一致）；infobox Doctoral advisor 并列 F. Albert Cotton
- **研究领域**：晶体学——核糖体晶体学、冷冻生物结晶学（cryo bio-crystallography）、抗生素-核糖体相互作用
- **童年偶像**：幼年读居里夫人传记深受触动，但她强调居里并非其 "role model"（§5 敏感点）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **耶路撒冷贫寒起步（1939）**：Geula 区杂货店之家，父亲早逝；母亲坚持送她去富人区学校——教育的执念是叙事起点。
2. **以教抵学费的高中生**：Tichon Hadash 高中靠给同学补数学换取学费；幼年因居里夫人传记爱上科学。
3. **希伯来大学双学位（1962/1964）**：化学学士、生物化学硕士。
4. **魏茨曼博士（1968）**：胶原的 X 射线晶体学研究，师从 Wolfie Traub。
5. **美国博士后（1969–1970）**：Carnegie Mellon（1969）、MIT（1970）；在 MIT 期间到 1976 年化学诺奖得主 William N. Lipscomb, Jr.（Harvard）实验室待过，受"挑战超大结构"的启发。
6. **以色列唯一蛋白晶体学实验室（1970）**：建立此后近十年以色列唯一的蛋白质晶体学实验室。
7. **马普所岁月（1977–2004）**：芝加哥大学访问教授（1977–78）；1979–1984 与 Heinz-Günter Wittmann 在马普分子遗传学所任组长；1986–2004 领导马普所驻汉堡 DESY 研究组，与魏茨曼研究并行。
8. **二十年的孤独攻坚**：顶着国际学界大量怀疑推进核糖体晶体学——"despite considerable skepticism of the international scientific community"（page.md 原文口径）。
9. **冷冻生物结晶学**：为让核糖体晶体可测，引入 cryo bio-crystallography——后成结构生物学常规技术。
10. **核糖体隧道（1993）**：可视化新生肽链穿行的通道；其后揭示其动态元件参与停滞、门控与折叠。
11. **双亚基高分辨率结构（2000–2001）**：测定两亚基完整高分辨率结构，发现核糖体中普适对称区域——证明核糖体是核酶（ribozyme），把底物摆进成肽的立体化学位。
12. **抗生素与耐药（20 余种）**：解析 20 余种靶向核糖体的抗生素作用模式、耐药与协同机制，铺路结构导向药物设计。
13. **2009 诺贝尔化学奖与三重"第一"**：与 Ramakrishnan、Steitz 共享；page.md 明载她是以色列首位女性诺奖得主（十位以色列诺奖得主中）、**中东首位科学诺奖女性**、45 年来首位化学奖女性得主——三句均页面明载，可写（另有 2002 Israel Prize、2006 Wolf Prize 等长荣誉序列）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深红 deepcrimson） | `#9E2B25` | 低温晶体学的深红基调 / 以色列学术的庄重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（核糖体晶体学 badgeRibo） | `#2E5A9E` | 蓝双亚基结构 / 普适对称区 |
| 分类色 2（冷冻技术 badgeCryo） | `#1B7A43` | 绿 cryo bio-crystallography / DESY |
| 分类色 3（抗生素 badgeAbx） | `#D97B29` | 琥珀 20 余种抗生素 / 耐药机制 |
| 分类色 4（女性与传承 badgeFirst） | `#C0395B` | 玫瑰三重"第一" / 居里情结 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「冷冻晶体 / 核糖体隧道」的点阵结构。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（文件 `music_audio/inspiring-electronic/25-l3Fsk4R6eys-...Winds Of Freedom (Epic Heroic Orchestral).wav`；不要复制 wav 文件）
- **风格**：史诗而克制 / 英雄管弦 / 从暗到明的推进感
- **匹配理由**：
  - "自由之风" 匹配三重"第一"——从贫寒耶路撒冷到斯德哥尔摩，女性科学家破风而行的史诗感
  - 英雄管弦匹配核糖体攻坚叙事——二十年国际怀疑中的孤独坚持最终登顶
  - 由暗到明的推进匹配"寒门 → 冷冻 → 破晓"的三段式人生曲线
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 冷冻晶体学先驱 / Ada Yonath 1939–2026 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  约纳特的一生 — Sanger 式时间线（10 节点：1939→1962→1968→1969→1970→1979→1986→2000→2009→2026）
04  耶路撒冷：杂货店之女 (1939–1957) — 表格「时间|事件|结果」
05  求学：希伯来大学与魏茨曼 (1957–1968) — 表格「阶段|方向|结果」+ 公式框：胶原 X 射线晶体学
06  美国博士后与 Lipscomb 之遇 (1969–1970) — 表格「地点|经历|结果」
07  从以色列唯一到马普所 (1970–2004) — 表格「时期|据点|结果」（Weizmann / MPI Berlin / DESY Hamburg）
08  二十年攻坚：核糖体晶体学 (1990s) — 表格「困难|方法|结果」+ 公式框：cryo bio-crystallography
09  双亚基结构与核酶 (2000–2001) — 表格「问题|方法|结果」+ 公式框：核糖体 = 核酶 · 2009 诺奖
10  抗生素与耐药 — 表格「靶点|机制|意义」（20 余种抗生素 / 耐药 / 协同）
11  荣誉 — Sanger 式「类别|代表|意义」表格（Israel Prize 2002 / Wolf 2006 / Ehrlich 2007 / Einstein World Award 2008 / Nobel 2009 / ForMemRS 2020）
12  三重"第一" — 高斯 FFT 页式流程（以色列首位女性诺奖 → 中东首位科学诺奖女性 → 45 年来首位化学奖女性）
13  家人与遗产 — 四分类遗产盒 + 公式框：NYT/Times 评价与抗生素新设计
14  结尾 — 「我是科学家，不是男性或女性。一个科学家。」（page.md 明载原话，仅此一句）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2009 诺奖口径 | 与 Ramakrishnan、Steitz **三人共享**；官方理由 "for studies of the structure and function of the ribosome"（page.md 引 Nobel 表述）；勿写"独享" |
| 三重"第一" | **全部页面明载**：以色列首位女性诺奖得主（十位以色列得主中）；中东首位科学诺奖女性；45 年来首位化学奖女性（自 Dorothy Crowfoot Hodgkin 1964 以来）——可写但须三句并列呈现，勿混写"中东女性第一人"模糊句 |
| "第八位中的第四位" | page.md 又载 "the fourth of eight women ever to win the Nobel Prize in chemistry"——与前句并存，如引用须保持原文口径，勿自行更新计数 |
| 居里情结 | 幼年受居里传记触动，但她**强调居里不是其 "role model"**——勿写成"居里是她的榜样"；直接引语仅此一处可用（"I am a scientist, not male or female. A scientist."） |
| 本名与姓氏 | 本名 Ada Esther **Lifshitz**，Yonath 是夫姓；与 Moshe Yonath 婚后离异——勿写成"白头偕老" |
| 双博士导师 | infobox Doctoral advisor 载 Wolfie Traub **与 F. Albert Cotton** 并列；正文只明言 Traub——正文叙述以 Traub 为主，入库两行并列（Cotton 库内已有记录 #3493） |
| Lipscomb 之遇 | 正文口径：MIT 博士后期间"spent some time in the laboratory of" Lipscomb（Harvard）——是"在其实验室待过"，**勿写成师承或正式博士后导师**；入库用 colleague |
| 出生地 | 出生于耶路撒冷 Geula 区，当时为**英属巴勒斯坦托管地**（Mandatory Palestine）——勿写"生于以色列"（1948 年才建国）；父母 1933 年自波兰移民 |
| 政治敏感 | 页面载其表亲 Ruchama Marton 为"反占领活动家"——仅如实按 infobox 级事实入库/提及一次，**不展开巴以政治叙事**；与印度总理莫迪同框照仅作 Legacy 配图，不写政治评价 |
| 去世 | 2026-08-31 去世，享年 87（页面未载死因与地点）——**死因、去世地页面无载禁写** |
| Wolf 奖 | 2006 Wolf Prize in Chemistry 与 **George Feher** 共同获得；2007 Paul Ehrlich 奖与 **Harry Noller** 共同获得——勿漏共同得主或张冠李戴 |
| 机构头衔 | Kimmelman 中心主任；infobox 另写 "Martin S. and Helen Kimmel Professorial Chair"——两处均为页面明载，勿混成第三种头衔 |
| 引语红线 | 全页直接引语仅两处：居里非 role model 的表述与 "I am a scientist..."；The Australian 的 "crushing the lab's glass ceiling" 是媒体引语，须注明出处方可使用 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7426 | ✅（复用库内 #3709 回填） |
| name_zh | 阿达·约纳特 | ✅ |
| name_en | Ada Yonath（库内 #3709 既有形式） | ✅ |
| birth_date | 1939-06-22 | ✅ |
| death_date | 2026-08-31 | ✅ |
| nationality | Israel | ✅ |
| primary_occupation | crystallographer（修正库内误值 mathematician） | ✅ |
| field_of_work | crystallography（person_field 细分：crystallography / structural biology / ribosome / cryo bio-crystallography / molecular biology，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wolfie Traub | 师→生（博士导师） | Weizmann PhD 1968，胶原 X 射线晶体学 |
| advisor-student | F. Albert Cotton | 师→生（博士导师并列） | infobox Doctoral advisor 并列（库内已有记录） |
| colleague | William Lipscomb | 无向 | MIT 博士后期间在其 Harvard 实验室（库内既有边幂等去重） |
| colleague | Heinz-Günter Wittmann | 无向 | 1979–1984 马普分子遗传学所共同组长 |
| co-honored | Venkatraman Ramakrishnan | 无向 | 2009 诺贝尔化学奖共同得主 |
| co-honored | Thomas A. Steitz | 无向 | 2009 诺贝尔化学奖共同得主 |
| co-honored | George Feher | 无向 | 2006 Wolf 化学奖共同得主 |
| co-honored | Harry Noller | 无向 | 2007 Paul Ehrlich and Ludwig Darmstaedter 奖共同得主 |
| co-honored | Peretz Lavie | 无向 | 2006 EMET 奖共同得主（生命科学类，Lavie 属医学） |
| co-honored | Eli Keshet | 无向 | 2006 EMET 奖共同得主（生物） |
| spouse | Moshe Yonath | 无向 | 后离异 |
| parent-child | Hagit Yonath | （不写 direction，按 from<to 归一） | 女儿，Sheba 医疗中心医生 |
| other | Ruchama Marton | 无向 | 表亲（两人母亲为姐妹），反占领活动家 |

> **禁入库名单**（仅 metadata/事件性提及，不入库）：Marie Curie（童年精神触动、本人明确否认 role model——不建 influence）；Noa（外孙女）；Narendra Modi / N. Chandrababu Naidu（同框合影）；Pope Francis（2014 教皇任命宗座科学院院士——机构事件非人际）；Isaac Herzog（总统唁电评价）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2009，与 Ramakrishnan / Steitz 共享）
- Israel Prize（2002）
- Louisa Gross Horwitz Prize（2005）
- Wolf Prize in Chemistry（2006，与 George Feher 共享）
- The EMET Prize for Art, Science and Culture（2006，与 Peretz Lavie / Eli Keshet）
- Paul Ehrlich and Ludwig Darmstaedter Prize（2007，与 Harry Noller 共享）
- Albert Einstein World Award of Science（2008）
- L'Oréal-UNESCO Award for Women in Science（2008，frontmatter 载）
- Wilhelm Exner Medal（2010）；Marie Curie Medal（2011，波兰化学会）
- Foreign Member of the Royal Society（2020）
- Massry Prize、Rothschild Prize、Harvey Prize（2002）、F. A. Cotton Medal、Esther Hoffman Beller Lectureship、Erna Hamburger Prize（frontmatter 载）
- 名誉博士：Carnegie Mellon（2018）、University of Chile、Technical University of Berlin、University of Hamburg、Joseph Fourier University、USC、De La Salle University、Medical University of Lodz、University of Warwick、Jagiellonian University（2023）、Technion（2024）等
- 院士：美国国家科学院、美国艺术与科学院、以色列科学院、欧洲科学与艺术学院、EMBO、德国利奥波第那科学院（2013）、宗座科学院（2014，教皇任命）

## 9. 机构清单

- 教育：Hebrew University of Jerusalem（BSc 1962 / MSc 1964）→ Weizmann Institute of Science（PhD 1968）
- 博士后：Carnegie Mellon University（1969）→ MIT（1970；其间在 Harvard 的 Lipscomb 实验室待过）
- 任职：Weizmann Institute of Science（1970 起建以色列唯一蛋白晶体学实验室；Kimmelman 中心主任；Kimmel 讲席教授）
- 兼职：University of Chicago 访问教授（1977–1978）；Max Planck Institute for Molecular Genetics 组长（1979–1984，与 Wittmann）；MPI 驻 DESY Hamburg 研究组负责人（1986–2004）

## 10. 终审清单

- [x] 生卒 1939-06-22 / 2026-08-31，享年 87，出生地耶路撒冷 Geula（英属巴勒斯坦托管地）
- [x] 2009 三人共享（Ramakrishnan / Steitz）表述准确；三重"第一"均页面明载且并列呈现
- [x] 博士导师 Traub（正文）+ Cotton（infobox 并列）双行口径一致
- [x] Lipscomb 是"在其实验室待过"，非师承——colleague 口径正确
- [x] 直接引语仅 "I am a scientist..." 一句 + 居里非 role model 转述；其余无杜撰
- [x] 居里"非 role model"表述保留原意；政治人物仅同框照不展开
- [x] 死因与去世地页面无载——留白
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ada_Yonath/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 内真实肖像已就位，否则装饰圆占位并注明
- [ ] **国籍**：封面顶部明示以色列
- [ ] **引语核对**：中文引号内原话必须能在 page.md 找到；无原话一律改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2009 另两篇（Ramakrishnan、Steitz）口径互查：共享得主名、诺奖理由一致
