# Carolyn Bertozzi（卡罗琳·贝尔托齐）立传提示词

> qid=Q7442 · 1966-10-10 生于美国波士顿（在世，卒日留白） · 美国化学家 · 21 世纪 · 诺贝尔化学奖（2022，与 Morten P. Meldal、Karl Barry Sharpless 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Carolyn_Bertozzi/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Frederick Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Carolyn_Bertozzi_IMG_9372.jpg`，2011 年 Emanuel Merck Lectureship 领奖照，已就位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{syringe}\enspace 生物正交化学的命名者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「糖衣细胞」母题——细胞大圆表面缀满糖链小圆，暗示糖生物学与活体化学标记。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Carolyn Ruth Bertozzi（中文惯称：卡罗琳·贝尔托齐）
- **生卒**：1966-10-10 生于美国马萨诸塞州波士顿（在世，卒日留白勿写）
- **国籍**：United States（美国）
- **身份**：化学家；斯坦福大学 Anne T. and Robert M. Bass 人文与科学学院冠名讲席教授；HHMI 研究员（2000 至今）；LBNL Molecular Foundry 前主任
- **家庭**：Lexington（马萨诸塞）长大；父 William Bertozzi 是 MIT 物理学教授（意大利裔）、母 Norma Gloria（Berringer）；外祖父母来自加拿大新斯科舍；姐妹 Andrea Bertozzi 是 UCLA 数学系教授。出柜女同性恋（1980 年代末起公开），与妻子育有三子。大学时期曾在多支乐队弹键盘（与未来 Rage Against the Machine 吉他手 Tom Morello 同组 Bored of Education），后自修贝斯
- **教育轨迹**：
  - Lexington High School
  - Harvard University（BA 化学 summa cum laude，1988；本科随 Joe Grabowski 搭建光声量热计，获 Thomas T. Hoopes 本科论文奖；毕业后在 Bell Labs 随 Chris Chidsey 工作）
  - UC Berkeley（MS、PhD 化学，1993；论文《Synthesis and biological activity of carbon-linked glycosides》，导师 Mark D. Bednarski）
- **导师**：Mark D. Bednarski（博士导师）；Steven Rosen（博后导师，UCSF）
- **研究领域**：化学与生物学交叉——生物正交化学、糖生物学（glycobiology）、细胞表面寡糖、癌症/炎症/结核的糖科学工具

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **摇滚与化学之间（1966–1988）**：哈佛时代在乐队弹键盘、与 Tom Morello 同组；曾考虑读音乐专业，最终自觉 "always centered on the sciences"（页面实载引语）。
2. **光声量热计（哈佛本科）**：随 Joe Grabowski 设计搭建光声量热计，被要求成文并获 Hoopes 本科论文奖。
3. **Berkeley 博士的糖发现（1988–1993）**：合成寡糖类似物时发现病毒能结合人体糖——引出其毕生领域糖生物学。
4. **导师罹癌的考验（博士第三年）**：Bednarski 确诊结肠癌离职读医学院，全实验室无直接指导完成博士——自我驱动的成长。
5. **UCSF 博后（1993–1996）**：随 Steven Rosen 研究内皮寡糖促进炎症部位细胞黏附；期间实现活细胞壁蛋白与糖分子修饰（植入体可接受外源材料）。
6. **回到伯克利（1996）**：化学系 faculty + LBNL faculty scientist，后任 Molecular Foundry 主任。
7. **开创生物正交化学（1999；命名 2003）**：在活体系统中进行不干扰细胞过程的化学反应——1999 建立领域、2003 造词 "bioorthogonal chemistry"；代表作 Staudinger 反应修饰细胞表面（*Science* 2000, Saxon & Bertozzi）。
8. **无铜点击化学（2005）**：与 Prescher、Agard 发明应变促进叠氮-炔环加成（SPAAC），铜不用于活体——生物正交的标志性工具。
9. **糖寄生物与糖免疫（2000s–2010s）**：癌细胞表面糖与免疫逃逸机制；2017 年受邀斯坦福 TED 演讲 "What the sugar coating on your cells is trying to tell you"；2018 年报道海藻糖探针快速检测痰液中结核分枝杆菌。
10. **创业连环（2001–2019）**：Thios（2001，2005 解散）、Redwood Bioscience（2008，与学生 David Rabuka；SMARTag 技术；2014 被 Catalent 收购）、Enable Biosciences（2014）、Palleon Pharma（2015）、InterVenn Biosciences（2017）、Grace Science Foundation（2018，NGLY1 缺乏症）、OliLux 与 Lycia Therapeutics（2019，LYTACs）。
11. **礼来董事的底线（2017–2021）**：任 Eli Lilly 董事至 2021，因礼来与她共同创办的 Lycia 签许可协议而辞任——利益冲突的处理案例。
12. **女性与先驱纪录**：33 岁获 MacArthur"天才奖"（1999）；2010 年成为首位获 Lemelson–MIT Prize 教师奖的女性；ACS Central Science 首任主编（2014，ACS 首个完全开放获取期刊）。
13. **2022 诺贝尔化学奖**：与 Morten P. Meldal、Karl Barry Sharpless 三人共享，"for the development of click chemistry and bioorthogonal chemistry"——点击化学（Meldal/Sharpless）与生物正交化学（Bertozzi）合流；2024 获 ACS 最高荣誉 Priestley Medal。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深蓝灰 deepslate） | `#14324F` | 糖生物学的严谨底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（生物正交化学 badgeBioorth） | `#2E5A9E` | 蓝Staudinger / SPAAC 活体标记 |
| 分类色 2（糖生物学 badgeGlyco） | `#1B7A43` | 绿糖萼 / 细胞表面寡糖 |
| 分类色 3（疾病应用 badgeDisease） | `#D97B29` | 琥珀癌症 / 结核 / 炎症 |
| 分类色 4（转化与创业 badgeTransl） | `#C0395B` | 玫瑰 Redwood / Lycia / 礼来董事 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「细胞糖衣」——大圆（细胞）表面缀小圆（糖链）。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；不要复制 wav 文件，Makefile 指向源路径）
- **风格**：沉稳 / 纪录片 / 长期主义
- **匹配理由**：
  - "Timeless" 匹配糖科学的"古老分子、全新工具"叙事——糖链是生命最古老的信号语言，她为它造了新字母
  - "沉稳纪录片" 匹配其交叉学科气质——化学、生物学、产业与公共卫生一以贯之
  - 与本批其他曲目错开（Doudna=Shine Like The Sun、List=Pathfinder、MacMillan=New Lands、Meldal=PAST）
- **时长**：128 秒 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 生物正交化学的命名者 / Carolyn Bertozzi 1966– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士/师承/领域/荣誉）
03  贝尔托齐的一生 — 高斯式时间线（10 节点：1966→1988→1993→1996→1999→2003→2008→2015→2022→2024）
04  早年：摇滚与化学 (1966–1988) — 表格「时间|事件|结果」（Lexington / 哈佛乐队 / Hoopes 论文奖）
05  伯克利读博：糖与病毒 (1988–1993) — 表格「问题|事件|结果」+ 导师罹癌考验
06  UCSF 博后与活细胞修饰 (1993–1996) — 表格「方法|内容|结果」（Rosen 组 / 内皮寡糖）
07  生物正交化学的诞生 (1999–2003) — 表格「问题|方法|结果」+ 公式框：Staudinger 连接与叠氮-炔环加成
08  SPAAC：无铜点击化学 (2005) — 表格「局限|突破|意义」+ 公式框：应变促进 [3+2] 环加成
09  糖生物学与疾病 (2000s–2018) — 表格「疾病|糖机制|工具」（癌症免疫逃逸 / 结核探针 / TED 演讲）
10  创业连环与利益冲突处理 (2001–2019) — 表格「公司|年份|方向」（Thios→Redwood→Enable→Palleon→InterVenn→OliLux/Lycia；礼来辞任）
11  荣誉清单 — 高斯式「类别|代表|意义」表格（含 itemize：Nobel 2022 / MacArthur 1999 / Lemelson-MIT 2010 / Wolf 2022 / Priestley 2024）
12  2022 诺贝尔化学奖 — 高斯 FFT 页式流程（Sharpless 2001 概念 → Meldal CuAAC 2002 → Bertozzi 活体应用 → 三人共享）
13  遗产：给活体化学立规矩 — 四分类遗产盒 + 公式框：生物正交三条件（活体兼容/选择性/不干扰）
14  结尾 — 「细胞表面的糖，一直在向我们诉说。」（取自其 TED 演讲标题意译，非原话直引）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2022 诺奖口径 | 与 Morten P. Meldal、Karl Barry Sharpless **三人共享**，官方理由 "for the development of click chemistry and bioorthogonal chemistry"；Bertozzi 的是**生物正交化学**那一半（Meldal/Sharpless 是点击化学 CuAAC）——分工勿混 |
| 命名年份 | 1999 建立（开创）领域、2003 **造词** "bioorthogonal chemistry"——两个年份勿混 |
| Staudinger vs SPAAC | 2000 Staudinger 反应修饰细胞表面（Saxon & Bertozzi）是首个生物正交反应；2005 SPAAC（Agard/Prescher/Bertozzi）实现无铜活体标记——顺序勿倒 |
| 首位女性断言 | 页面明载的"第一"只有一条：2010 首位获 Lemelson–MIT Prize 教师奖的女性——勿外推到其他奖项 |
| MacArthur 年龄 | "at age 33"（1999 获奖时）——勿写"29 岁" |
| 导师罹癌 | Bednarski 博士第三年确诊结肠癌、转读医学院——如实写但不渲染；此后全组无直接指导 |
| 家庭表述 | 配偶（妻子）页面**未具名**（"her wife"）——三条婚姻信息只写"与妻子育有三子、1980 年代末出柜"；姐妹 Andrea Bertozzi（UCLA 数学教授）可写 |
| Tom Morello | 大学乐队 Bored of Education 的未来 RATM 吉他手——轶事一笔带过，勿写成"音乐合作伙伴关系延续" |
| 礼来辞任 | 2017–2021 任董事、2021 因 Lilly-Lycia 许可协议辞任——如实写，这是利益冲突规范处理案例而非丑闻 |
| Sharpless 合作 | 页面无载 Bertozzi 与 Sharpless 直接合作——只有共享诺奖，勿写"师承/合作"；对手方规范名 Karl Barry Sharpless（2022 已在 batch-01 建档） |
| 在世口径 | 1966-10-10 生，在世，卒日留白 |
| 出版物 | "over 600 publications on Web of Science"——引用数口径照写；代表论文挑 3–4 篇 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7442 | ✅ |
| name_zh | 卡罗琳·贝尔托齐 | ✅ |
| name_en | Carolyn Bertozzi | ✅ |
| birth_date | 1966-10-10 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：bioorthogonal chemistry / glycobiology / chemical biology / organic chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Mark D. Bednarski | 师→生（博士导师） | UC Berkeley，1993 年碳连糖苷论文；博士第三年导师罹癌离职 |
| advisor-student | Steven Rosen | 师→生（博后导师） | UCSF，内皮寡糖与细胞黏附 |
| advisor-student | Howard Hang | Bertozzi→学生 | 博士生 |
| advisor-student | Mireille Kamariza | Bertozzi→学生 | 博士生，结核检测探针方向 |
| advisor-student | Lara Mahal | Bertozzi→学生 | 博士生 |
| advisor-student | Jennifer Prescher | Bertozzi→学生 | 博士生，2005 SPAAC 共同作者 |
| advisor-student | David Rabuka | Bertozzi→学生 | 前研究生，Redwood Bioscience 联合创办人（SMARTag） |
| co-honored | Morten P. Meldal | 无向 | 2022 诺贝尔化学奖共同得主（点击化学 CuAAC） |
| co-honored | Karl Barry Sharpless | 无向 | 2022 诺贝尔化学奖共同得主（点击化学概念） |
| sibling | Andrea Bertozzi | 无向 | 姐妹，UCLA 数学系教授 |

> **不予入库**（页面未具名 / 关系过浅 / 一笔带过）：妻子（页面未具名，仅 "her wife"，无法建 stub）；Joe Grabowski（本科科研导师，非研究生师承且页面无独立师承细节）；Chris Chidsey（Bell Labs 短暂工作）；Laura Kiessling（2001 Chemical Glycobiology 论文合作者，无独立关系叙述）。

## 8. 奖项清单

- Phi Beta Kappa（1987）；Sloan Research Fellowship（1997）；Horace S. Isbell Award（1997）
- Beckman Young Investigators Award（1998）；Camille Dreyfus Teacher-Scholar Award（1999）
- **MacArthur Fellowship（1999，33 岁）**；Arthur C. Cope Scholar Award（1999）
- Presidential Early Career Award（2000）；ACS Award in Pure Chemistry（2001）
- AAAS Fellow（2001）；Agnes Fay Morgan Research Award（2004）
- NAS 院士（2005）；Ernst Schering Prize（2007）；Willard Gibbs Award（2008）
- Lemelson–MIT Prize（2010，首位女性得主）；Institute of Medicine（2011）；Heinrich Wieland Prize（2012）
- NAI Fellow（2013）；Arthur C. Cope Award（2017）；National Inventors Hall of Fame（2017）
- ForMemRS（2018）；John J. Carty Award（2020）；Solvay Prize（2020）；F. A. Cotton Medal（2020）
- Wolf Prize in Chemistry（2022）；Heineken Prize（2022）；Dickson Prize（2022）；Welch Award（2022）
- **Nobel Prize in Chemistry（2022，与 Meldal、Sharpless 共享）**
- Roger Adams Award（2023）；AACR 癌症化学杰出成就奖（2023）
- **Priestley Medal（2024，ACS 最高荣誉）**；宾夕法尼亚大学荣誉博士（2026）
- 其他院士/学会：American Academy of Arts and Sciences（2003）、Leopoldina（2008）、Accademia dei Lincei（2021）

## 9. 机构清单

- 教育：Lexington High School；Harvard University（BA 1988）；UC Berkeley（MS、PhD 1993）
- 任职：Bell Labs（1988 毕业后，Chris Chidsey）；UCSF（博后，Steven Rosen）；UC Berkeley 化学系 + LBNL（1996–2015，Molecular Foundry 主任）；HHMI 研究员（2000–）；Stanford University（2015–，ChEM-H 研究所，Anne T. and Robert M. Bass 讲席教授）；Arc Institute 科学顾问委员会（2024–）
- 编辑：*ACS Central Science* 创刊主编（2014，ACS 首个完全开放获取期刊）
- 创业：Thios Pharmaceuticals（2001–2005）、Redwood Bioscience（2008，2014 被 Catalent 收购）、Enable Biosciences（2014）、Palleon Pharma（2015）、InterVenn Biosciences（2017）、Grace Science Foundation（2018）、OliLux Biosciences（2019）、Lycia Therapeutics（2019）
- 董事：Eli Lilly 董事会（2017–2021，因 Lilly-Lycia 许可协议辞任）

## 10. 终审清单

- [ ] 生卒 1966-10-10 / 在世留白，出生地 Boston
- [ ] 2022 诺奖"三人共享"与分工（点击化学 vs 生物正交化学）表述准确
- [ ] 1999 建立领域 / 2003 造词 两个年份不混淆
- [ ] Staudinger 2000 → SPAAC 2005 顺序正确
- [ ] "首位女性"断言仅限 Lemelson–MIT 2010（页面明载）
- [ ] 配偶未具名照实处理；姐妹 Andrea 入库 sibling
- [ ] 礼来辞任表述客观（利益冲突规范处理）
- [ ] 引语（"always centered on the sciences" 等）可溯源；TED 标题引用注明
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Carolyn_Bertozzi/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/Carolyn_Bertozzi_IMG_9372.jpg` 已就位（2011 Emanuel Merck Lectureship）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：直接引语必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与本批其他篇目（Doudna/List/MacMillan/Meldal）格式对齐

---

> **名单状态**：由主控统一收尾（`chemist/generate_21th_century_list.py`）。
