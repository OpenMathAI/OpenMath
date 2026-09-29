# Benjamin List（本亚明·利斯特）立传提示词

> qid=Q105572 · 1968-01-11 生于德国法兰克福（在世，卒日留白） · 德国化学家 · 21 世纪 · 诺贝尔化学奖（2021，与 David W.C. MacMillan 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Benjamin_List/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Frederick Sanger 模板，★ 硬性要求）

1. **封面头像缺位 → 装饰圆占位**（★ 本篇特例）：images.txt 仅含 L-脯氨酸分子结构图，无真实肖像——右上角用主色装饰圆 + 化学分子意象占位（tikz 圆内可绘 proline 五元环简笔或双六边形骨架），并加小字注「肖像暂缺」。L-Proline.svg 分子图（`images/L-Prolin_-_L-Proline.svg.png`）可用于核心贡献页插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 有机小分子催化的奠基人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「小分子催化」母题——一个小圆催化两个大圆的键合，暗示脯氨酸在醛醇反应中的角色。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Benjamin List（中文惯称：本亚明·利斯特）
- **生卒**：1968-01-11 生于西德法兰克福（在世，卒日留白勿写）
- **国籍**：Germany（德国）
- **身份**：化学家；马克斯·普朗克煤炭研究所所长之一；科隆大学有机化学教授；*Synlett* 主编
- **家庭**：法兰克福中上层科学家与艺术家之家——心脏病学家 Franz Volhard 之曾孙、化学家 Jacob Volhard 之玄孙；姑母（母亲的姐姐）Christiane Nüsslein-Volhard 是 1995 年诺贝尔生理学或医学奖得主；母亲 Heidi List 是建筑师；3 岁时父母离异。1999 年在 La Jolla 娶 Sabine List，两子 Theo 与 Paul；全家幸存于 2004 年印度洋海啸
- **教育轨迹**：
  - Free University of Berlin（化学 Diplom，1993）
  - Goethe University Frankfurt（PhD，1997；论文《Synthese eines Vitamin B12 Semicorrins》）
- **导师**：Johann Mulzer（博士导师）；Richard Lerner 与 Carlos F. Barbas III（博后导师，其他学术导师）
- **研究领域**：有机化学——不对称有机催化、有机催化（organocatalysis）、均相催化、不对称反离子导向催化（ACDC）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **化学世家（1968）**：曾祖父辈两位都是科学家——心脏病学家 Franz Volhard 与化学家 Jacob Volhard；诺奖得主姑母 Nüsslein-Volhard 是母亲一方的姐姐。
2. **反威权教养**：父母以反威权方式育儿；他自述对子女偶尔沿用——"你可以只有 12 岁，但如果你觉得吃十块巧克力有好处，那就吃吧。我相信你。但我的建议是：我不会这么做。"（页面实载原话）
3. **柏林与法兰克福（1989–1997）**：柏林自由大学 Diplom（1993）→ 法兰克福大学 PhD（1997），维生素 B12 Semicorrin 全合成。
4. **Scripps 岁月（1997–2003）**：洪堡奖学金资助，在 Lerner 与 Barbas III 组做博后（1997–1998），后任助理教授（1999–2003）。
5. **2000 年 JACS 论文**：List、Lerner、Barbas《Proline-Catalyzed Direct Asymmetric Aldol Reactions》——脯氨酸作为高效手性催化剂直接催化分子间醛醇反应，有机催化奠基作。
6. **回到催化史源头**：其发展基于 Hajos–Parrish–Eder–Sauer–Wiechert 反应（1970 年代已知的脯氨酸催化分子内反应）——List 证明小分子脯氨酸可以取代金属与酶。
7. **脯氨酸催化版图扩张**：随后发展出首个脯氨酸催化的 Mannich、Michael 与 α-胺化反应。
8. **ACDC（2006）**：与 Sonja Mayer 提出不对称反离子导向催化（Asymmetric counteranion-directed catalysis）。
9. **有机纺织催化（2013）**：可溶性有机催化剂与纺织品结合（*Science* 2013），可用于无淡水地区的净水。
10. **马克斯·普朗克煤炭研究所（2003–）**：2003 回德国任课题组长，2005 任所长（主持均相催化系），2012–2014 任执行所长。
11. **科隆与北海道**：2004 年起科隆大学 honorary professor；2018 年起北海道大学 ICReDD principal investigator。
12. **2021 诺贝尔化学奖（2021-10-06）**：与 David MacMillan 共享，"for the development of asymmetric organocatalysis"——两位创始人在各自不知情的情况下同时开辟同一领域。
13. **Leibniz 奖与学界荣誉（2016–）**：2016 德国 Leibniz 奖；2018 入选德国国家科学院 Leopoldina；2022 获联邦十字勋章指挥官级骑士十字；h-index 95（Google Scholar，2021）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（钢蓝 steelblue） | `#123C5B` | 有机催化的严谨与克制（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（有机催化 badgeOrgano） | `#2E7D5B` | 绿脯氨酸 / 直接不对称醛醇反应 |
| 分类色 2（ACDC badgeACDC） | `#8C4A1E` | 琥珀反离子导向催化 |
| 分类色 3（Scripps 时代 badgeScripps） | `#3B5B92` | 蓝抗体催化剂 / Lerner-Barbas 组 |
| 分类色 4（工业与水处理 badgeApply） | `#7A2E4A` | 玫瑰有机纺织催化 / 药物手性合成 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），一个小圆居中催化两个大圆键合的「小分子撬动大反应」意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Pathfinder** — Ghostwriter Music（`music_audio/inspiring-electronic/23-GiwYLGgJw7w-*.wav`；不要复制 wav 文件，Makefile 指向源路径）
- **风格**：开拓感 / 明快节拍 / 探路者气质
- **匹配理由**：
  - "Pathfinder（探路者）" 直接匹配有机催化奠基人的身份——在金属与酶之外另辟蹊径
  - 明快节拍匹配脯氨酸催化的"直接、简单、高效"美学
  - 与本批其他曲目错开（Doudna=Shine Like The Sun、MacMillan=New Lands、Bertozzi=Timeless、Meldal=PAST）
- **时长**：须 make video 时以 ffmpeg `-shortest` 自动对齐 15 页时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 有机小分子催化的奠基人 / Benjamin List 1968– + 四色 badge + 右上装饰圆（肖像缺位注记）+ 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士/师承/领域/荣誉）
03  利斯特的一生 — 高斯式时间线（10 节点：1968→1993→1997→1998→2000→2003→2005→2012→2021→2024）
04  化学世家与反威权童年 (1968–1989) — 表格「时间|事件|结果」（Volhard 家族 / 诺奖姑母 / 巧克力原话）
05  柏林—法兰克福：B12 Semicorrin (1989–1997) — 表格「阶段|内容|结果」
06  Scripps：抗体催化剂与脯氨酸时刻 (1997–2003) — 表格「问题|方法|结果」+ 公式框：L-脯氨酸催化的直接不对称醛醇反应
07  马普煤炭研究所 (2003–) — 表格「年份|职务|内容」（课题组长→所长→执行所长；科隆/北海道兼职）
08  有机催化版图 — 表格「反应|贡献|年份」（Mannich/Michael/α-amination/ACDC/有机纺织催化）
09  不对称有机催化的意义 — 表格「问题|方法|结果」+ 公式框：手性药物合成对映选择性的价值
10  2021 诺贝尔化学奖 — 高斯 FFT 页式流程（2000 JACS → 与 MacMillan 平行独立 → 2021-10-06 获奖）；获奖理由原句
11  荣誉清单 — 高斯式「类别|代表|意义」表格（含 itemize：Leibniz 2016 / Mukaiyama 2013 / Otto Bayer 2012 / Leopoldina 2018）
12  家庭与生活 — 表格「主题|内容|备注」（Sabine 1999 / Theo 与 Paul / 2004 海啸幸存 / 反威权育儿）
13  遗产：小分子改变大化学 — 四分类遗产盒 + 公式框：有机催化的三大优点（简单/绿色/便宜）
14  结尾 — 「催化剂不必是金属，也不必是酶——一个氨基酸就够了。」（意译，非原话直引）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2021 诺奖口径 | 与 David W.C. MacMillan **两人共享**，官方理由 "for the development of asymmetric organocatalysis"——两人是**各自独立、同时**开创有机催化（List 在 Mülheim、MacMillan 在伯克利），勿写"师承合作"或"竞争" |
| 奖项年表 | 2000 年的突破性工作发表时他是**助理教授**（Scripps），勿写"研究生时期"；Hajos–Parrish 反应 1970 年代已有，List 的新意在**分子间**直接不对称醛醇反应 |
| 有机催化定义 | 使用**非金属、非酶**催化剂——勿写成"发现了有机催化反应"（Hajos 反应早已存在），而是确立其为通用方法学 |
| ACDC 表述 | "He found asymmetric catalysis (especially ACDC)"——ACDC 2006 年与 Sonja Mayer 共同提出（Angew. Chem. 论文第一作者是 Mayer），勿独占 |
| 职务口径 | 马普煤炭研究所是 "Max Planck Institute for Coal Research"（Mülheim），2005 起是 **director 之一**（one of the directors）；勿写"所长"单数 |
| 家族表述 | 曾孙/玄孙关系：Franz Volhard 是 great-grandson（曾祖父）、Jacob Volhard 是 2nd great-grandson（高祖父辈）；Nüsslein-Volhard 是**姑母/姨母**（母亲的姐姐）——三代方向勿颠倒；此三人**不入库**关系表（超出 parent-child/sibling 可表达范围，见 §7） |
| 妻子姓名 | Sabine List（1999 La Jolla 结婚）——随夫同姓实载如此，照写 |
| 巧克力引语 | 页面实载原话可直引，但保留英文原意完整："you may only be 12, but if you think it will do you good to eat ten chocolate bars, then go ahead and do it..."——勿截断改意 |
| 在世口径 | 1968-01-11 生，在世，卒日留白 |
| 肖像缺位 | images.txt 无真实肖像，封面与身份页用装饰圆占位并注记；L-Proline.svg 是分子结构图，只可作插图勿冒充肖像 |
| 荣誉清单 | 页面荣誉列表极长（1994–2024），Beamer 只挑代表性 6–8 条；获奖年份以列表为准（如 Mukaiyama Award 2013、Otto Bayer Award 2012） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q105572 | ✅ |
| name_zh | 本亚明·利斯特 | ✅ |
| name_en | Benjamin List | ✅ |
| birth_date | 1968-01-11 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organocatalysis / asymmetric synthesis / organic chemistry / homogeneous catalysis，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Johann Mulzer | 师→生（博士导师） | 法兰克福大学，1997 年维生素 B12 Semicorrin 合成论文 |
| advisor-student | Richard Lerner | 师→生（博后导师） | Scripps 研究所，1997–1998 洪堡奖学金博后 |
| advisor-student | Carlos F. Barbas III | 师→生（博后导师） | Scripps 研究所，2000 年脯氨酸醛醇反应论文共同作者 |
| co-honored | David W.C. MacMillan | 无向 | 2021 诺贝尔化学奖共同得主，各自独立开创不对称有机催化 |
| spouse | Sabine List | 无向 | 1999 年 La Jolla 结婚，两子 Theo 与 Paul |

> **不予入库**（家族关系超出关系类型可表达范围 / 正文一笔带过）：Christiane Nüsslein-Volhard（姑母——无 aunt 类型，且她是 1995 诺奖得主易与 advisor-student 混淆）；Franz Volhard、Jacob Volhard（曾祖/高祖父辈——非 parent-child 直系）；Theo 与 Paul（未成年子女，页面无独立事迹）。

## 8. 奖项清单

- NaFöG-Award, City of Berlin（1994）；Feodor Lynen Fellowship（1997）
- Synthesis-Synlett Journal Award（2000）；Carl-Duisberg-Memorial Award（2003）
- Degussa Prize for Chiral Chemistry（2004）；Lieseberg Prize（2004）
- Novartis Young Investigator Award（2005）；JSPS Fellowship（2006）
- Otto Bayer Award（2012）；Novartis Chemistry Lectureship（2012）
- Horst-Pracejus-Preis（2013）；Mukaiyama Award（2013）；Ruhrpreis, Mülheim（2013）
- Cope Scholar Award（2014）
- **Gottfried Wilhelm Leibniz Prize（2016）**
- Leopoldina 院士（2018）；Herbert C. Brown Award（2022）
- **Nobel Prize in Chemistry（2021，与 MacMillan 共享）**
- 联邦十字勋章指挥官级骑士十字（Knight Commander's Cross of the Order of Merit，年份以 frontmatter 为准）

## 9. 机构清单

- 教育：Free University of Berlin（Diplom 1993）、Goethe University Frankfurt（PhD 1997）
- 任职：Scripps Research Institute 分子生物学系（1997–1998 博后，1999–2003 助理教授）；Max Planck Institute for Coal Research（2003 课题组长，2005 所长之一/均相催化系主任，2012–2014 执行所长）；University of Cologne（2004 至今 honorary professor）；Hokkaido University ICReDD（2018 至今 principal investigator）
- 编辑：*Synlett* 主编

## 10. 终审清单

- [ ] 生卒 1968-01-11 / 在世留白，出生地 Frankfurt（西德）
- [ ] 2021 诺奖"两人共享、各自独立"表述准确；官方理由原句
- [ ] 2000 JACS 论文三位作者（List/Lerner/Barbas）勿漏；发表时身份是助理教授
- [ ] ACDC 2006 与 Mayer 合著勿独占
- [ ] 马普煤炭研究所 director 口径（one of the directors）准确
- [ ] 家族三代关系（曾祖/玄孙/姑母）方向准确且不入库
- [ ] 巧克力引语可溯源；结尾页引语标注"意译"
- [ ] 封面装饰圆占位并注明肖像缺位
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Benjamin_List/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆占位（肖像缺位注记）；L-Proline.svg 仅作分子插图
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：巧克力引语等必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与本批其他篇目（Doudna/MacMillan/Bertozzi/Meldal）格式对齐

---

> **名单状态**：由主控统一收尾（`chemist/generate_21th_century_list.py`）。
