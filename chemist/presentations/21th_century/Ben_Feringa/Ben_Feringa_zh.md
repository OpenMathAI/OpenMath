# Ben Feringa（伯纳德·费林加）立传提示词

> qid=Q3259614 · 1951-05-18 – 在世 · 荷兰合成有机化学家 · 21 世纪 · 诺贝尔化学奖（2016，与 Jean-Pierre Sauvage、Sir J. Fraser Stoddart 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Ben_Feringa/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本次执行的版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像位**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 `images.txt` **无单人清晰肖像**（仅 2016 斯德哥尔摩诺奖得主合影与 Commons 图标）——封面用主色装饰圆占位（圆内 `\faIcon{sync-alt}` 呼应分子马达旋转），图注注明「装饰圆占位 · 页面无单人肖像」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace 让分子转动的人\enspace·\enspace 荷兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（格罗宁根大学 · 分子马达 · 2016 诺贝尔化学奖）。
3. **必须有身份信息页**（★ 必做）：左侧头像（装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名 Bernard Lucas Feringa、国籍 Netherlands、出生地 Barger-Compascuum、教育（University of Groningen MSc 1974 / PhD 1978）、博士导师 Hans Wijnberg、核心领域（molecular machines / photochemistry / stereochemistry）、机构（Stratingh Institute, University of Groningen）、荣誉。事实取自本地 page.md，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「旋转 / 手性」母题——同轴双圆暗示分子马达的单向旋转。
5. **表格语义化 + 公式框**（★ 桑格版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Bernard Lucas "Ben" Feringa（荷兰语发音 [ˈbɛrnɑrt ˈlykɑz bɛn ˈfeːrɪŋɣaː]；中文惯称：伯纳德·费林加）
- **生卒**：1951-05-18 生于荷兰 Barger-Compascuum → 在世（页面无卒日，全篇留白处理）
- **国籍**：Netherlands（荷兰；metadata 作 Kingdom of the Netherlands，入库用规范名 Netherlands）
- **身份**：合成有机化学家；格罗宁根大学 Stratingh 化学研究所 Jacobus van 't Hoff 分子科学杰出教授；荷兰皇家艺术与科学院（KNAW）Academy Professor
- **家庭**：农场主 Geert Feringa（1918–1993）与 Lies Feringa（娘家姓 Hake，1924–2013）十个孩子中的第二个，天主教家庭；在德荷边境 Bourtange 沼泽的家族农场长大；有荷兰与德国血统；与妻子 Betty Feringa 育有三女，居于格罗宁根附近的 Paterswolde
- **教育轨迹**：
  - University of Groningen：1974 MSc（with distinction 优等）
  - 1978 同校 PhD（论文 *Asymmetric oxidation of phenols. Atropisomerism and optical activity*——酚的不对称氧化、阻转异构与旋光性）
  - 1979–1984 壳牌（Royal Dutch Shell，荷兰与英国）
  - 1984 回格罗宁根任讲师，1988 任正教授（接棒 Wijnberg）
- **导师**：Hans Wijnberg（格罗宁根博士导师；infobox 拼作 Wijnberg，frontmatter 另有 Wynberg 拼写变体——入库与行文统一用 **Hans Wijnberg**）
- **研究领域**：分子纳米技术、有机化学——分子马达与分子开关、均相催化与氧化催化、立体化学（手性拥挤烯烃）、光化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **沼泽农场（1951）**：十个孩子中的老二，在德荷边界的泥炭沼泽农场长大——最早的「动手建构」。
2. **优等硕士（1974）**：格罗宁根大学化学 MSc with distinction。
3. **阻转异构博士（1978）**：酚的不对称氧化与阻转异构（atropisomerism）研究——手性此后的主线。
4. **壳牌四年（1979–1984）**：在荷兰与英国的工业界历练，随后回到学术。
5. **接棒 Wijnberg（1984/1988）**：1984 讲师、1988 正教授——接过博士导师的教席。
6. **不对称催化名家**：单磷配体（monophos）用于不对称氢化；有机锂等高活性有机金属试剂的不对称共轭加成；铜催化 C–C 键生成的立体控制突破。
7. **手性光开关（1990s）**：以手性拥挤烯烃为基础的光致变色分子开关——「用光控制手性」。
8. **世界第一台单向分子马达**：光驱动的单向分子旋转马达——手性在实现天然功能（如视黄醛在视紫红质中的单向旋转）中起关键作用。
9. **分子纳米车（nanocar）**：电脉冲驱动的「分子汽车」。
10. **应用全景**：响应材料与表面、液晶、电致变色器件、光开关 DNA「分子U盘」、响应凝胶/聚合物、纳米药物递送的光开关蛋白通道、阴离子传感、光药理学（photopharmacology）与抗菌耐药新策略；多项入选 C&EN 年度最重要化学发现。
11. **表面组装的跨越**：分子马达组装到金纳米粒子与宏观金膜上仍能运转——通往「分子传送带」的关键一步；掺杂液晶可让宏观物体转动。
12. **2016 诺贝尔化学奖**：与 Sir J. Fraser Stoddart、Jean-Pierre Sauvage 共享「分子机器的设计与合成」；同年获德化学会 August Wilhelm von Hofmann Medal 与 Elsevier Tetrahedron Prize；此前 2015-11 已获 "Chemistry for the future Solvay prize"（表彰分子马达奠基性研究）。
13. **荣誉满载与荣誉市民**：Körber 欧洲科学奖 2003、Spinoza 奖 2004、荷兰 Lion 勋章骑士 2008 → 指挥官 2016-11-23（国王 Willem-Alexander 授）、格罗宁根荣誉市民 2016-12-01、家乡街道命名 Prof. Dr. B. L. Feringadam（2017-04-06）、美国 NAS 外籍院士 2019、英国皇家学会外籍会员 2020；1997 年以 12 小时完成 200 公里 Elfstedentocht 滑冰赛。

## 3. 配色方案（桑格式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（森林绿 emerald-deep） | `#1E5631` | 分子马达的「光与旋转」母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子马达 badgeMotor） | `#D98E04` | 琥珀·光驱动单向旋转 / nanocar |
| 分类色 2（手性开关 badgeChiral） | `#5B2A86` | 紫·手性拥挤烯烃 / 立体化学 |
| 分类色 3（催化与配体 badgeCat） | `#2E5A9E` | 蓝·monophos / 不对称氢化与共轭加成 |
| 分类色 4（应用与光药理 badgeApp） | `#A63A2B` | 砖红·photopharmacology / 响应材料 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），同轴双圆暗示单向旋转的马达桨叶。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（`music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`；不要复制 wav 文件，Makefile 里直接引用原路径）
- **风格**：电影感 / 明亮 / 有推进力
- **匹配理由**：
  - 「推进力」匹配单向分子马达——不回头的旋转
  - 「明亮」匹配光化学主线——光既是工具也是主题
  - 「电影感」匹配从沼泽农场到斯德哥尔摩的全景叙事（含 200 公里滑冰的荷兰式坚韧）
- **时长**：按 Makefile 默认 `-shortest` 对齐 15 页即可

## 4. Slide 规划（15 页，桑格式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让分子转动的人 / Ben Feringa 1951– + 四色 badge + 右上头像占位 + 国籍行「荷兰」
02  身份信息页（★ 必做）— 左头像占位 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/机构/荣誉）
03  费林加的一生 — 桑格式时间线（10 节点：1951→1974→1978→1979→1984→1988→1999→2004→2016→2020）
04  早年：沼泽农场的十个孩子 (1951–1974) — 表格「时间|事件|结果」
05  格罗宁根：阻转异构 (1974–1978) — 表格「阶段|内容|结果」+ 公式框：atropisomerism（阻转异构 = 轴手性）
06  壳牌与接棒 (1979–1988) — 表格「阶段|内容|结果」
07  不对称催化：monophos 时代 (1988–1990s) — 表格「问题|方法|结果」+ 公式框：单磷配体 → 不对称氢化
08  手性光开关到分子马达 (1990s–) — 表格「问题|方法|结果」+ 公式框：光驱动单向旋转；天然参照：视黄醛
09  2016 诺贝尔化学奖 — 公式框：官方获奖理由 "for the design and synthesis of molecular machines"（与 Sauvage / Stoddart 共享，三人三步：索烃→轮烷→马达）
10  从马达到应用 — 表格「方向|载体|意义」（photopharmacology / 分子U盘 / 响应材料 / 表面组装）
11  荣誉与学会 — 桑格式「类别|代表|意义」表格 + itemize 清单（Körber 2003 / Spinoza 2004 / Lion 勋章 2008→2016 / NAS 外籍 2019 / FRSC 外籍 2020）
12  格罗宁根 — 桑格 LMB 页式流程图（1974 求学 → 1984 讲师 → 1988 教授 → Stratingh 研究所 / van 't Hoff 杰出教授）
13  遗产：分子马达开启的纳米世界 — 四分类遗产盒 + 公式框：30+ 专利 · 650+ 论文 · h-index>90 · 100+ 博士生
14  结尾 — 「给分子一个马达，化学就有了发动机。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2016 获奖理由 | 官方措辞 "for the design and synthesis of molecular machines"；**勿泛化成「发明分子马达」之外杜撰颁奖词** |
| 共享口径 | 2016 为**三人共享**——Sauvage（索烃，第一步）/ Stoddart（轮烷与分子开关）/ Feringa（分子马达）；页面原文另有「Feringa 的分子旋转马达 + 分子车」表述；对另两人一律用规范全名 Jean-Pierre Sauvage / Sir J. Fraser Stoddart |
| 在世口径 | 页面无卒日——全篇写 1951-05-18 – 在世，**禁止编造卒年** |
| 导师拼写 | 博士导师 infobox 作 **Hans Wijnberg**（frontmatter 作 Hans Wynberg）——行文与入库统一用 Hans Wijnberg，并在 §7 注明拼写变体；「1988 接棒 Wijnberg 教席」页面明载 |
| 双重 van 't Hoff | 他是 **Jacobus van 't Hoff Distinguished Professor**（教席名）；另获 Van't Hoff Medal（2011，荷兰学会 Decennial）——两事勿混；van 't Hoff 是首届化学诺奖得主，可在插图注提及（页面链接明载） |
| 马达优先权 | 页面表述 "the world's first unidirectional molecular rotary motor"——「世界首个单向分子旋转马达」可用；**勿加「比 XX 早/晚」等页面无载的比较** |
| Solvay 奖 | "Chemistry for the future Solvay prize"（2015-11），理由页面有原文——引用须按原文；勿与诺贝尔理由混写 |
| 中国相关 | 南华师范大学名誉教授（2017-11-26）、中国「绿卡」、华东理工大学自愈合材料团队（2017-12 起）均页面明载——**只客观列举或整体略过，不加评价**；勿展开政治语境 |
| Simpsons | 2010 年《辛普森一家》将其列入诺奖候选人名单——可作趣闻一笔，勿渲染 |
| 奖项年份 | Körber 2003 / Spinoza 2004 / Prelog 金章 2005 / Norris 奖 2007 / Paracelsus 2008 / Chirality Medal 2010 / Van't Hoff Medal 2011 / Cino del Duca 2012 / Humboldt 2012 / Föster 2014 / Solvay 2015 / Nobel 2016 / Centenary 2017 / EuChemS 金章 2018——年份勿混；Solvias Ligand Contest Award 与 John Hartwig 共享（年份页面未载，如实标注） |
| 引语红线 | 本页**无直接引语**（诺奖演讲标题 "The Art of Building Small: from Molecular Switches to Motors" 仅作为条目名出现，可注明「诺奖演讲题目」使用）——中文引号内不得出现无法溯源的「原话」 |
| 数字口径 | 30+ 专利、650+ 论文、引用 30,000+、h-index>90、100+ 博士生——引用时保留「超过/以上」措辞，勿精确化 |
| 家庭成员 | 父母、妻子 Betty、三个女儿：**页面明载但仅作背景，配偶入库、其余不入库** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q3259614 | ✅ |
| name_zh | 伯纳德·费林加 | ✅ |
| name_en | Ben Feringa | ✅ |
| birth_date | 1951-05-18 | ✅ |
| death_date | 空（在世） | ✅ |
| nationality | Netherlands | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | molecular nanotechnology（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh |
|---|---|---|
| molecular nanotechnology | 0 | 分子纳米技术 |
| organic chemistry | 1 | 有机化学 |
| photochemistry | 2 | 光化学 |
| stereochemistry | 3 | 立体化学 |
| homogeneous catalysis | 4 | 均相催化 |

## 7. 社会关系入库清单

**师长 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Wijnberg | 师→生（博士导师） | 格罗宁根博士导师（1978 阻转异构论文）；1988 费林加接其教席成教授 |
| co-honored | Jean-Pierre Sauvage | 无向 | 2016 诺贝尔化学奖共同得主 |
| co-honored | Fraser Stoddart | 无向 | 2016 诺贝尔化学奖共同得主 |
| co-honored | John Hartwig | 无向 | Solvias Ligand Contest Award 共享（年份页面未载，如实标注） |
| spouse | Betty Feringa | 无向 | 妻子，育有三女 |

> **禁入库名单**（页面明载但不入库）：父 Geert Feringa、母 Lies Feringa（家庭成员）；三个女儿；Johann Gerhard Bekel（祖先谱系）。Wijnberg 拼写变体（Wynberg，frontmatter）以 infobox 正文 **Hans Wijnberg** 为准，防分裂 stub。
> **对手方命名红线**：Sauvage 用 Jean-Pierre Sauvage（库内 id=4020）；Stoddart 用 Fraser Stoddart。

## 8. 奖项清单

- Fellow of the Royal Society of Chemistry，FRSC（1998）
- Novartis Chemistry Lectureship Award（2000–2001）
- Körber European Science Prize（2003）
- International Honorary Member, American Academy of Arts and Sciences（2004）
- Spinoza Prize（2004）
- Prelog Gold Medal（ETH Zürich，2005）
- KNAW 会员（2006）/ Academy Professor（2008）
- James Flack Norris Award in Physical Organic Chemistry（ACS，2007）
- ERC Advanced Grant（2008）
- Knight of the Order of the Netherlands Lion（2008，女王 Beatrix 授）
- Paracelsus Award（Swiss Chemical Society，2008）
- Chirality Medal（2010）
- Solvias Ligand Contest Award（与 John Hartwig 共享，年份页面未载）
- Organic Stereochemistry Award（RSC，2011）
- Van't Hoff Medal（Decennial，荷兰，2011）
- Grand Prix Scientifique Cino del Duca（2012）；Humboldt Award（2012）
- Nagoya Medal / Nagoya Gold Medal（2012–2013）；Yamada-Koga Award（2013）；Marie Curie Medal（波兰化学会，2013）
- Theodor Föster Award（GDCh，2014）
- Arthur C. Cope Late Career Scholars Award（ACS，2015）
- Ernest Solvay Prize（"Chemistry for the future Solvay prize"，2015-11）
- Nobel Prize in Chemistry（2016，与 Sauvage / Stoddart 共享）
- August Wilhelm von Hofmann Medal（德化学会，2016）；Tetrahedron Prize（Elsevier，2016）
- Commander of the Order of the Netherlands Lion（2016-11-23，国王 Willem-Alexander 授）；格罗宁根荣誉市民（2016-12-01）
- Honorary Member, Royal Netherlands Chemical Society（2016-10-13）
- Centenary Prize（RSC，2017）；家乡街道 Prof. Dr. B. L. Feringadam（2017-04-06）
- EuChemS European Gold Medal（2018）；Raman Chair, Indian Academy of Sciences（2019）
- Honorary doctorate, University of Johannesburg（2019）；German Academy of Sciences Leopoldina（2019）
- Foreign Member of the Royal Society（2020）；美国 NAS 外籍院士（2019-04）

## 9. 机构清单

- 教育：University of Groningen（MSc 1974 with distinction / PhD 1978）
- 任职：Royal Dutch Shell（1979–1984，荷兰与英国）；University of Groningen（1984 讲师 → 1988 正教授；Stratingh Institute for Chemistry；Jacobus van 't Hoff Distinguished Professor of Molecular Sciences；KNAW Academy Professor）
- 学术服务：RSC 期刊编委（Chem. Commun. 至 2012）、Organic & Biomolecular Chemistry 创刊科学主编（2002–2006）、Chemistry World 编委会主席；Bürgenstock 会议主席（2009）；Academia Europaea 会员（2010）
- 创办：Selact（合同研究公司，后并入 Kiadis）

## 10. 终审清单

- [ ] 生卒 1951-05-18 – 在世（全篇无卒日留白一致）；出生地 Barger-Compascuum
- [ ] 2016 三人共享（Sauvage / Stoddart）表述准确；获奖理由 "for the design and synthesis of molecular machines" 口径准确
- [ ] 三人分工不串位：Sauvage=索烃（1983）/ Stoddart=轮烷/分子梭 / Feringa=分子马达
- [ ] 博士导师统一用 Hans Wijnberg；1984 讲师 / 1988 教授（接棒 Wijnberg）准确
- [ ] 「世界首个单向分子旋转马达」表述有页面依据；无页面外比较
- [ ] 荣誉年份逐条核对（Körber 2003 / Spinoza 2004 / Nobel 2016 / 指挥官 2016-11-23）
- [ ] 中国相关内容零评价、仅客观或略过；全篇无编造引语
- [ ] 正文采用桑格式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make pdf` 编译通过，0 错误、vbox≤10pt、hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Ben_Feringa/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆占位（页面无单人肖像），图注注明
- [ ] 国籍：封面顶部明示荷兰
- [ ] 引语核对：本篇无引语；诺奖演讲标题仅作条目名使用
- [ ] 编译验证：`make distclean && make pdf`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Modrich / Sancar / Sauvage / Stoddart）及桑格既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，执行者不改。
> **数据事实来源唯一**：`chemist/presentations/21th_century/pages/Ben_Feringa/page.md`；页面无载的数据如实标注「页面无载」，禁止编造。
