# Kary Mullis（凯利·穆利斯）立传提示词

> qid=Q157224 · 1944-12-28 – 2019-08-07 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1993，与 Michael Smith 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Kary_Mullis/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `pages/Kary_Mullis/images.txt` 下载至 `images/`，404 则用装饰圆占位并在 Review-1 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 复制 DNA 的人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Kary Banks Mullis）、国籍、出生地/去世地、教育、博士导师、研究领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），呼应「链式扩增」母题——从一个小圆点按 2 的幂指数铺开成一片圆点场，暗示 PCR 的指数扩增。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 " "。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Kary Banks Mullis（中文惯称：凯利·班克斯·穆利斯）
- **生卒**：1944-12-28 生于美国北卡罗来纳州 Lenoir（蓝岭山脉附近农村）→ 2019-08-07 逝于加州 Newport Beach 自宅（肺炎并发症），享年 74
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist）；PCR（聚合酶链式反应）发明人
- **家庭**：父母 Cecil Banks Mullis 与 Bernice Barker Mullis，家世代务农；童年随家迁往南卡罗来纳州 Columbia，在祖父母地下室观察蜘蛛、给舅舅家牲口喂食逗乐；高中时代学会化学合成固体燃料火箭推进剂。结过四次婚，与其中两任妻子育有 3 个子女；去世时遗孀为第四任妻子 Nancy（娘家姓 Cosgrove），有两名孙辈
- **教育轨迹**：
  - Dreher High School（Columbia, SC），1962 届毕业
  - Georgia Institute of Technology，化学 BS（1966）——本科期间结婚并创业
  - University of California, Berkeley，生物化学 PhD（1973），J. B. Neilands 实验室
- **导师**：J. B. Neilands（博士导师；细菌铁载体 siderophore 研究名家）
- **博士**：1973，《Schizokinen: structure and synthetic work》（细菌铁载体 schizokinen 的结构与合成）；1968 年还曾以唯一作者在 Nature 发表天体物理学短文
- **研究领域**：分子生物学、生物化学、核酸化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **乡野孩子（1944–1962）**：北卡农村出身，童年痴迷观察乡间生物；高中自学化学合成固体燃料火箭——化学兴趣的起点。
2. **Georgia Tech 创业生（1962–1966）**：化学 BS；本科期间结婚并开办生意，读的是「用化学谋生」而非「用化学治学」。
3. **Berkeley 的坎坷博士（1966–1973）**：Neilands 组做 schizokinen；口试多次不过（同事回忆他不清楚一般生物化学），论文靠朋友帮忙删掉「怪东西」、导师游说委员会才被接受——1968 年却以唯一作者在 Nature 发表天体物理学论文。
4. **离开科学又回来（1973–1979）**：博士毕业后一度辞职写小说；堪萨斯大学医学中心儿科心脏学博士后（1973–1977）期间还经营面包店两年；UCSF 药物化学博士后（1977–1979）。
5. **Cetus 的 DNA 化学家（1979–1986）**：经 Berkeley 挚友 Thomas White 引荐进入 Cetus Corporation（Emeryville），任 DNA 化学家七年，后任 DNA 合成实验室主任——尽管分子生物学经验寥寥。
6. **PCR 的灵感（1983）**：驱车行经 Mendocino County 乡居附近时想到：用一对引物夹住目标 DNA 序列、以 DNA 聚合酶复制之——微量 DNA 片段的快速指数扩增。
7. **1983-12-16 首次成功**：PCR 实验首次验证成功；同事仍将信将疑，White 让他放下其他项目全职攻关 PCR。诺奖演讲中他自嘲当晚的失落（引用 "I was lonesome" 段，见 §5 引语清单）。
8. **1985 论文与并行团队**：Saiki 产出数据、Erlich 执笔首篇应用论文；Mullis 与 Saiki、Erlich 合著 1985 年 β-珠蛋白基因扩增论文——2017 年获 ACS 化学史分会 Citation for Chemical Breakthrough Award。
9. **Taq 聚合酶（1986）**：Saiki 改用嗜热水生菌的耐热 Taq DNA 聚合酶，反应无需每轮补酶——PCR 从此可自动化、大幅降价，革新生化、遗传学、医学与法医学。
10. **专利与争议**：Mullis 从 Cetus 仅得 1 万美元奖金；Cetus 将专利以 3 亿美元卖给 Roche，Mullis 斥并行团队为 "vultures"；DuPont 挑战专利败诉（1991 陪审团维持 Mullis 专利）；早在 17 年前 Khorana 与 Kleppe 已发表过 "repair replication"（1971），但 Mullis 法用的是反复热循环、可指数扩增任意序列。
11. **1993 诺贝尔化学奖**：因发明 PCR 与 Michael Smith 共享；同年获日本国际奖。NYT 评价 PCR "highly original and significant, virtually dividing biology into the two epochs of before PCR and after PCR"。
12. **争议人物**：质疑 HIV 导致 AIDS、淡化人类在气候变化中的作用、公开相信占星与超自然现象（自述见过外星浣熊）；研究生期间长期自制 LSD 并称 LSD "helped him develop the polymerase chain reaction"（Hofmann 转述）——Skeptical Inquirer 将其称为 "Nobel disease" 的例证。★ 叙事须忠于页面、克制陈述，不渲染不引申。
13. **晚年创业（1992–2019）**：创办售卖名人（Elvis、Marilyn Monroe）扩增 DNA 饰品的公司与 Atomic Tags；2011 创办 Altermune LLC 研究抗体改向技术（抗炭疽 100% 有效对比旧疗法 40%，TED 演讲口径）；2014 任 Children's Hospital Oakland Research Institute 杰出研究员。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#52307C` | 分子生物学的幽深与双螺旋的暗紫（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（PCR 发明 badgePCR） | `#7B4FA6` | 紫 PCR 灵感 / 1983-12-16 |
| 分类色 2（Taq 与自动化 badgeTaq） | `#1B7A43` | 绿嗜热聚合酶 / 指数扩增 |
| 分类色 3（法医学与医学 badgeMed） | `#D97B29` | 琥珀 DNA 指纹 / 诊断 |
| 分类色 4（争议与晚年 badgeLate） | `#C0395B` | 玫瑰 Nobel disease / 创业 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「链式反应」的指数铺开。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（清单指定 `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`，不要复制 wav 文件，由 Makefile 侧引用）
- **风格**：沉稳 / 纪录片 / 时间感
- **匹配理由**：
  - "Timeless" 匹配 PCR 的地位——一项把生物学切成「PCR 之前 / PCR 之后」两个纪元的技术，本身即超越时间
  - "沉稳" 匹配叙事基调——从乡野孩子、坎坷博士到灵光一现，传记主线是孤独的长期主义而非英雄史诗
  - "纪录片" 匹配 Cetus 实验室群像——发明人、并行团队、专利官司与 3 亿美元交易的多声部纪实
- **时长**：约 128 秒 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 复制 DNA 的人 / Kary Mullis 1944–2019 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/机构/荣誉）
03  穆利斯的一生 — 时间线（10 节点：1944→1966→1973→1979→1983→1986→1991→1993→2011→2019）
04  早年：乡野与火箭 (1944–1966) — 表格「时间|事件|结果」
05  Berkeley：坎坷的博士 (1966–1973) — 表格「时间|事件|结果」
06  Cetus 与 PCR 灵感 (1979–1983) — 表格「问题|方法|结果」+ 公式框：引物夹注 + 每轮 ×2 指数扩增
07  从验证到论文 (1983–1985) — 表格「挑战|人物|结果」
08  Taq 聚合酶 (1986) — 表格「问题|方法|结果」+ 公式框：耐热聚合酶免每轮补酶
09  专利、Roche 与诉讼 (1986–1991) — 表格「事件|经过|结果」（$10,000 奖金 vs $300M 专利；1991 陪审团维持专利）
10  1993 诺贝尔化学奖 — 表格「人物|贡献|结果」（与 Michael Smith 共享；Japan Prize）
11  PCR 改变世界 — 表格「领域|应用|意义」（生化/遗传/医学/法医学 + NYT 评价）
12  争议与 "Nobel disease" — 表格「议题|立场|页面口径」（HIV/AIDS、气候、超自然、LSD；克制陈述）
13  晚年与遗产 — 表格「时间| venture|结果」（Atomic Tags / Altermune / 2014 CHORI）+ 公式框：Citation for Chemical Breakthrough 2017
14  结尾 — 「一条引物，一座桥：从微量到无限。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 1993 与 Michael Smith **共享**（Smith 因定点突变）；勿写「独享」；本地页面无诺奖官方 citation 原句，勿杜撰，用页面表述 "In recognition of his role in the invention of the polymerase chain reaction (PCR) technique" |
| PCR 首证日期 | **1983-12-16** 首次成功演示——日期须精确 |
| Taq 归属 | 1986 年改用 Taq 聚合酶的是 **Saiki**；Cetus 同事对「Taq 引入 PCR 归功 Mullis 一人」有异议——勿写「Mullis 发明 Taq」 |
| 先行工作 | Khorana 与 Kleppe 的 "repair replication"（早 17 年）——须提及但注明 Mullis 法的关键是**反复热循环**与指数扩增 |
| 奖金对比 | Mullis 得 **$10,000** 奖金；Cetus 将专利以 **$300M** 卖给 Roche——两数字勿混 |
| 诉讼结果 | 1991 陪审团**维持** Mullis 专利（DuPont 败诉）；1999 年 Roche 另一 Taq 专利（4,889,818）被判不可执行——两案勿混 |
| 学位年份 | Georgia Tech BS **1966**、Berkeley PhD **1973**（论文 schizokinen）——勿写错 |
| 敏感议题 | HIV/AIDS 否认、气候怀疑、LSD、超自然——**按 page.md 原文克制转述**并注明 "Nobel disease" 出处（Skeptical Inquirer）；不得洗白也不得加码；页面无载的细节禁写 |
| 引语红线 | 可引用（页面原文）：NYT 评价句、诺奖演讲 "I was lonesome" 段、White 回忆 "outrageous" 句、LSD "mind-opening" 句（1994 California Monthly）；中文引号内不得出现无法在 page.md 溯源的「原话」 |
| 家庭 | 结婚 **四次**、三个子女、遗孀第四任 Nancy（née Cosgrove）——首任妻子名页面作 "Richards Haley"（疑似排版讹误），慎写全名 |
| 去世 | 2019-08-07 逝于 Newport Beach 自宅，**肺炎并发症**，享年 74——勿写「心脏病」 |
| 奖项年份 | William Allan 1990 / Robert Koch 1992 / Nobel 与 Japan Prize **1993** / National Inventors Hall of Fame **1998**——勿错位 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q157224 | ✅ |
| name_zh | 凯利·穆利斯 | ✅ |
| name_en | Kary Mullis | ✅ |
| birth_date | 1944-12-28 | ✅ |
| death_date | 2019-08-07 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | molecular biology（person_field 细分：polymerase chain reaction / molecular biology / biochemistry / nucleic acid chemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**（★ 只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | J. B. Neilands | 师→生（博士导师） | Berkeley 1973 博士，siderophore schizokinen 课题 |
| colleague | Thomas White | 无向 | Cetus 上司与长期赞助人，引荐入职并让其全职攻关 PCR |
| colleague | Randall Saiki | 无向 | 1985 PCR 论文共同作者；1986 首用 Taq 聚合酶 |
| colleague | Henry Erlich | 无向 | 1985 PCR 论文共同作者，首篇应用论文执笔人 |
| colleague | Norman Arnheim | 无向 | Cetus 并行 PCR 项目成员（β-珠蛋白扩增） |
| co-honored | Michael Smith | 无向 | 1993 诺贝尔化学奖共同得主（定点突变） |
| spouse | Nancy Cosgrove | 无向 | 第四任妻子，Mullis 2019 去世时在世 |

> metadata.json-only 的家庭细节（其余三任妻子、子女姓名等页面未具名）**不予入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1993，与 Michael Smith 共享）
- Japan Prize（1993）；Thomas A. Edison Award（1993）
- William Allan Memorial Award（1990）；Gairdner Award（1991）；John Scott Award（1991）；National Biotechnology Award（1991）；R&D Scientist of the Year（1991）
- California Scientist of the Year（1992）；Robert Koch Prize（1992）
- Honorary DSc, University of South Carolina（1994）；Golden Plate Award（1994）
- National Inventors Hall of Fame（1998）；Ronald H. Brown American Innovator Award（1998）
- Honorary degree, University of Bologna（2004）；Doctor honoris causa, Masaryk University（2010）
- Citation for Chemical Breakthrough Award（2017，ACS 化学史分会，授予 1985 论文）

## 9. 机构清单

- 教育：Dreher High School（–1962）、Georgia Institute of Technology（BS 1966）、University of California, Berkeley（PhD 1973）
- 博士后：University of Kansas Medical Center（儿科心脏学，1973–1977）、UCSF（药物化学，1977–1979）
- 任职：Cetus Corporation, Emeryville（DNA 化学家 / DNA 合成实验室主任，1979–1986）；Xytronyx, Inc., San Diego（分子生物学总监，1986–约1988）；此后为核酸化学顾问与 DNA 指纹专家证人；Atomic Tags（1992，La Jolla）；Altermune LLC（2011）；Children's Hospital Oakland Research Institute 杰出研究员（2014）

## 10. 终审清单

- [ ] 生卒 1944-12-28 / 2019-08-07，享年 74，出生地 Lenoir、去世地 Newport Beach（肺炎并发症）
- [ ] 1993 与 Michael Smith 共享表述准确；页面无诺奖 citation 原句，不杜撰
- [ ] 1983-12-16 首证日期；Taq 归属 Saiki（1986）；Khorana/Kleppe 先行工作已注明
- [ ] $10,000 奖金与 $300M 专利售出两数字未混淆；1991 专利维持
- [ ] 敏感议题按页面克制转述；引语全部可在本地 Wikipedia 原文找到
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Kary_Mullis/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像已就位（下载自 images.txt；404 则装饰圆占位并注明）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（NYT 句、"I was lonesome" 段、LSD 句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger、van 't Hoff 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 的更新由主控统一收尾（本提示词不直接改动）。
> **最重要的事：每写一页就 make，看到溢出就修。**
