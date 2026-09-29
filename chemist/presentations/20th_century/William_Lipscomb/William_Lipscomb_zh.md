# William Lipscomb（威廉·利普斯科姆）立传提示词

> qid=Q110935 · 1919-12-09 – 2011-04-14 · 美国无机与有机化学家 · 20 世纪 · 诺贝尔化学奖（1976，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/William_Lipscomb/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 桑格模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像下载后放 `images/`；Commons 404 则按 Wikipedia REST API 回退，再失败用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cubes}\enspace 硼烷世界的筑巢人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「硼烷笼 / 多面体」母题——笼状多面体圆点暗示硼氢化物的闭合笼结构。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：William Nunn Lipscomb Jr.（中文惯称：威廉·纳恩·利普斯科姆）
- **生卒**：1919-12-09 生于俄亥俄州克利夫兰 → 2011-04-14 逝于马萨诸塞州剑桥（肺炎），享年 91
- **国籍**：United States（美国）
- **身份**：美国无机与有机化学家，工作横跨核磁共振、理论化学、硼化学与生物化学
- **家庭**：医生世家（祖父、曾祖父皆医生，父为医生、母为家庭主妇）；1920 年举家迁肯塔基州列克星敦；1944 年娶 Mary Adele Sargent（三子女，其中一名仅存活数小时），1983 年离婚后娶 Jean Evans（养女一）；infobox 记子女 4 人
- **教育轨迹**：
  - 高中：化学老师 Frederick Jones 把大学教材（有机/分析/普通化学）赠予他只要求参加考试；州物理竞赛一等奖；痴迷狭义相对论
  - University of Kentucky：**凭音乐奖学金**入学；1941 BS（化学）；在 R. H. Baker 建议下完成首篇论文（稀水溶液中直接制备醇的衍生物）
  - Caltech：放弃 Northwestern $150/月研究助理金，选 Caltech 物理系 $20/月助教金；一学期后受 Pauling 影响转入化学系；1946 PhD（论文：四氯化钒等电子衍射 + 氯化甲铵晶体结构）
- **导师**：Linus Pauling（Caltech 博士导师；本想师从物理系 W. V. Houston 量子力学，一学期后转化学）
- **研究领域**：核磁共振与化学位移、硼化学与化学键本质、生物大分子结构与功能

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **医生世家的叛逆（1919–1941）**：本可成为 Lipscomb 家族第四代医生——却因 12 岁得到一套 Gilbert 化学玩具而拐入化学；自制烟花、从尿液中提取尿素（母亲唯一一次过问他的家庭化学实验）。
2. **音乐奖学金的化学家**：以音乐奖学金入 University of Kentucky；天文兴趣引他到肯塔基大学天文台，H. H. Downing 赠 Baker《Astronomy》——他自述从这本书获得许多直觉物理概念，Downing 成终生挚友。
3. **拒绝高薪选 Caltech（1941–）**：Northwestern 开价 $150/月，他选了 Caltech $20/月的物理助教金；Columbia 的拒信由诺奖得主 Harold Urey 署名（轶事，勿写成关系）。
4. **战时硝化甘油（1942–1945）**：二战研究分割其研究生时光——分析烟尘粒径、多次亲手处理纯硝化甘油小瓶（硝化甘油–硝化纤维素推进剂）。
5. **三大领域总纲**：核磁共振与化学位移、硼化学与化学键本质、大生物分子——时间上重叠、技术上互通；他惯于给自己立"大概率失败的大挑战"，再铺 intermediate goals。
6. **硼-11 NMR 提纲（领域一）**：主张以硼-11 核磁共振（而非 X 射线衍射）加速多硼烷/碳硼烷结构测定——部分达成；发表化学位移综合理论；与 Gareth Eaton 合著 *NMR Studies of Boron Hydrides and Related Compounds*。
7. **三中心两电子键的厘清（领域二）**：★关键裁定——三中心两电子键**不是** Lipscomb 提出的（Longuet-Higgins 1943 年还在牛津读本科时首先解释硼氢化物结构与成键）；Lipscomb 组的贡献是 1950 年代以 X 射线晶体学测定硼烷分子结构并发展解释其成键的理论。
8. **styx 规则与 DSD 重排**：与 Eberhardt、Crawford 提出 "styx rule" 归类硼氢化物成键构型；提出 diamond-square-diamond（DSD）机制解释笼顶原子游移；B10H16 结构中发现前所未有的硼-硼直接键（无端氢）。
9. **乙烷旋转势垒**：Pitzer 与 Lipscomb 以 Hartree–Fock (SCF) 方法首次准确计算乙烷绕 C–C 键旋转的势垒。
10. **Extended Hückel 与弟子群（领域二延伸）**：在 Lipscomb 指导下 Lawrence Lohr 与 Roald Hoffmann 发展 Extended Hückel 分子轨道法——Hoffmann 后获 1981 诺贝尔化学奖。
11. **1976 诺贝尔化学奖（独享）**："for his studies on the structure of boranes illuminating problems of chemical bonding"——以硼烷结构照亮化学键问题；承接其博士导师 Pauling 1954 年"化学键本质"的路线。
12. **酶的原子级解剖（领域三）**：晚期转向蛋白质 X 射线晶体学——羧肽酶 A（其组第一个蛋白结构，比以往所解大得多）、天冬氨酸氨甲酰转移酶（12 聚体：6 催化 + 6 调节）、亮氨酸氨肽酶、HaeIII 甲基转移酶、人干扰素 β、分支酸变位酶、果糖-1,6-二磷酸酶等。
13. **弟子与传承**：博士生 9 人（Dickerson、Hoffmann、Pitzer、Steitz、Voet、Wiley、Pepperberg、Rees、Christianson）；Steitz 获 2009 诺奖（50S 核糖体亚基大结构）；Ada Yonath 1970 年在 MIT 博士后期间曾在他实验室度过一段时间，与 Steitz 一同受启发 pursue very large structures（2009 共同诺奖）；矿物 lipscombite 以其名命名；低温 X 射线衍射在其实验室开创。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 deepindigo） | `#14324F` | 硼烷笼结构的深邃与秩序（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（硼烷与化学键 badgeBor） | `#2E6E8E` | 青蓝三中心两电子键 / styx 规则 |
| 分类色 2（核磁共振 badgeNMR） | `#1B7A43` | 绿 B-11 NMR / 化学位移理论 |
| 分类色 3（生物大分子 badgeEnz） | `#D97B29` | 琥珀羧肽酶 A / ATP 合酶时代的结构酶学 |
| 分类色 4（谱系传承 badgeTree） | `#C0395B` | 玫瑰 Hoffmann / Steitz / Yonath |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「硼烷笼」多面体顶点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Pathfinder** — Ghostwriter Music（`music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav`；不要复制 wav 文件，Makefile 引用即可）
- **风格**：开阔 / 探索 / 渐进上扬
- **匹配理由**：
  - "探路者" 直扣其方法论——立一个大概率失败的大目标，再铺 intermediate goals 一路叩关
  - "开阔" 匹配其横跨 NMR/理论化学/硼化学/酶结构四大领域的广度
  - "渐进上扬" 匹配从化学玩具到诺贝尔奖的七十年长跑
- **时长**：以实际曲目时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 硼烷世界的筑巢人 / William Lipscomb 1919–2011 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  利普斯科姆的一生 — 高斯式时间线（10 节点：1919→1941→1946→1954→1959→1950s→1973→1976→1990→2011）
04  早年：医生世家的化学玩具 (1919–1941) — 表格「时间|事件|结果」（Gilbert 化学盒 / 音乐奖学金 / 首篇论文）
05  Caltech：从物理到 Pauling 门下 (1941–1946) — 表格「时间|事件|结果」+ 战时硝化甘油
06  硼烷与化学键 (1940s–1976) — 表格「问题|方法|结果」+ 公式框：B2H6 三中心两电子键示意
07  styx 规则与笼重排 (1950s–) — 表格「问题|方法|结果」+ 公式框：DSD 机制 · B10H16 硼-硼直接键
08  1976 诺贝尔化学奖 — 表格「人物|方向|结果」（独享 · "illuminating problems of chemical bonding"）+ 承接 Pauling 1954
09  核磁共振与化学位移 (同期) — 表格「挑战|方法|结果」+ 公式框：B-11 NMR 加速结构测定
10  酶的原子级解剖 (1960s–2000s) — 表格「对象|方法|结果」+ 公式框：羧肽酶 A / 天冬氨酸氨甲酰转移酶 12 聚体
11  弟子与传承 — 表格「人物|方向|结果」（Hoffmann 1981 / Steitz 2009 / Yonath 1970 实验室访问）
12  荣誉与晚年 — 高斯式「类别|代表|意义」表格（Guggenheim 1954 / AAAS 1960 / NAS / Debye Award 1973 / 诺奖 1976）
13  遗产：从硼烷到生命机器 — 四分类遗产盒 + 公式框：lipscombite 矿物命名 · 低温 X 射线衍射开创
14  结尾 — 「他给看不见的键画出了形状。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1976 获奖理由 | 官方原文 "for his studies on the structure of boranes illuminating problems of chemical bonding"——硼烷结构照亮化学键问题；勿写成"发现三中心两电子键" |
| 三中心两电子键 | **不是 Lipscomb 提出/发现**——Longuet-Higgins 1943（本科时期，与导师 R. P. Bell 合写）首先解释硼氢化物结构与成键；Price 1947/1948 光谱证实、Hedberg & Schomaker 1951 电子衍射再证实；Lipscomb 组是**测结构+发展理论**——本篇最高危陷阱 |
| 三领域并列 | NMR、硼化学、生物大分子三领域时间重叠技术互通——勿写成先后三期 |
| 音乐奖学金 | University of Kentucky 入学凭**音乐奖学金**——勿删此趣味事实 |
| 拒高薪 | 拒 Northwestern $150/月选 Caltech $20/月——数字勿写反 |
| 博士导师 | **Linus Pauling**（转入化学系受其影响）；本想跟物理系 W. V. Houston——勿混 |
| Urey 拒信 | Columbia 拒信由 Harold Urey 署名系轶事——**不作为关系入库**，正文一句带过 |
| 弟子口径 | infobox Doctoral students **9 人**全数明载可入库；"Other notable students"（Ludwig/Rossmann/Stevens）非博士生于库中不建关系（§7 注明）；Yonath 是 **1970 MIT 博士后期间在他实验室**——写 colleague 不写学生 |
| 死亡日期 | frontmatter 双值 2011-04-14 / 2011-04-11，正文 infobox 与正文均作 **April 14, 2011**——取 2011-04-14 |
| 去世原因 | 剑桥（马萨诸塞）死于 **pneumonia**——勿写其他 |
| 婚姻 | 1944–1983 Mary Adele Sargent（三子女，一名仅存活数小时）；1983 娶 Jean Evans（养女）——infobox「Children 4」= 3+1 收养，勿写错 |
| 保罗奖陷阱 | 1976 诺奖是**独享**——勿与 1975/1977 得主混淆 |
| 引语红线 | page.md 可引的自述段：早年家庭环境段（"My early home environment..."）、硼烷宏大目标段（"My original intention in the late 1940s..."）、NMR 主张段（"...progress in structure determination..."）；诺奖理由整句；其余不得出现引号"原话" |
| lipcombite 拼写 | 矿物名 **lipscombite**——勿拼错 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110935 | ✅ |
| name_zh | 威廉·利普斯科姆 | ✅ |
| name_en | William Lipscomb | ✅ |
| birth_date | 1919-12-09 | ✅ |
| death_date | 2011-04-14（正文口径，frontmatter 双值取 infobox） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field rank 表**：

| field | rank | 语义 |
|---|---|---|
| boron chemistry | 0 | 硼烷结构与成键（诺奖方向） |
| theoretical chemistry | 1 | 化学键理论 / Extended Hückel |
| nuclear magnetic resonance | 2 | B-11 NMR / 化学位移理论 |
| biochemistry | 3 | 蛋白质与酶 X 射线结构 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Linus Pauling | 师→生（博士导师） | Caltech PhD 1946；一学期后自物理转化学受其影响 |

**门生（infobox Doctoral students，Lipscomb → 学生，9 人全数明载）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard E. Dickerson | Lipscomb → 学生 | infobox 明载 |
| advisor-student | Roald Hoffmann | Lipscomb → 学生 | Extended Hückel 法共同发展者；1981 诺贝尔化学奖 |
| advisor-student | Russell M. Pitzer | Lipscomb → 学生 | 合作首次准确计算乙烷旋转势垒 |
| advisor-student | Thomas A. Steitz | Lipscomb → 学生 | 羧肽酶 A/ATCase 结构；2009 诺贝尔化学奖 |
| advisor-student | Donald Voet | Lipscomb → 学生 | infobox 明载 |
| advisor-student | Don C. Wiley | Lipscomb → 学生 | infobox 明载 |
| advisor-student | Irene Pepperberg | Lipscomb → 学生 | infobox 明载 |
| advisor-student | Douglas C. Rees | Lipscomb → 学生 | infobox 明载；撰其 NAS 传记回忆 |
| advisor-student | David W. Christianson | Lipscomb → 学生 | infobox 明载 |

**同事 / 其他明载**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Ada Yonath | 无向 | 1970 年 MIT 博士后期间在其实验室，受启发 pursue very large structures；2009 诺奖 |
| colleague | M. Frederick Hawthorne | 无向 | 硼化学家，早期及持续合作研究 |
| influence | H. Christopher Longuet-Higgins | 无向 | 1943 首先解释硼氢化物结构与成键，Lipscomb 工作的理论源头 |

> **禁入库名单（非个人关系或 metadata-only）**："Other notable students"（Martha L. Ludwig、Michael Rossmann、Raymond C. Stevens——infobox 有载但非博士生，防噪声不入库）；Harold Urey（拒信署名者）；W. V. Houston（原意导师未从）；H. H. Downing / Robert H. Baker（本科提携者）；Frederick Jones（中学教师）。

## 8. 奖项清单

- Guggenheim Fellow（1954）
- Fellow of the American Academy of Arts and Sciences（1960）
- Member of the United States National Academy of Sciences
- Peter Debye Award in Physical Chemistry（1973）
- Nobel Prize in Chemistry（1976，独享）
- Foreign Member of the Royal Netherlands Academy of Arts and Sciences（1976）
- Remsen Award；Centenary Prize（frontmatter 明载，正文未给年份——展示慎写）
- 矿物 lipscombite 以其命名（矿物学家 John Gruner 首次人工合成）

## 9. 机构清单

- 教育：University of Kentucky（BS 1941）；California Institute of Technology（PhD 1946）
- 任职：University of Minnesota（1946–1959）；Harvard University（1959–1990，1990 起 professor emeritus）
- 居住：俄亥俄克利夫兰（出生）→ 肯塔基列克星敦（1920）→ 马萨诸塞剑桥（至去世）
- 纪念：矿物 lipscombite（Harvard Museum of Natural History 藏，1996 其本人捐赠标本）；五本书与会议文集题献给他

## 10. 终审清单

- [ ] 生卒 1919-12-09 / 2011-04-14（正文口径），享年 91，出生地 Cleveland、去世地 Cambridge MA（pneumonia）
- [ ] 1976 **独享**；获奖理由"硼烷结构照亮化学键问题"口径准确
- [ ] 三中心两电子键归属 Longuet-Higgins——Lipscomb 组测结构+发展理论（最高危陷阱已防）
- [ ] 音乐奖学金 / 拒高薪选 Caltech / Pauling 导师 轨迹准确
- [ ] 弟子 9 人 infobox 明载；Yonath 写 colleague（1970 实验室访问）；"other notable students" 不入库
- [ ] 引语仅 §5 列出的四段，其余不得出现引号"原话"
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/William_Lipscomb/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认肖像就位（Commons/Wikipedia REST API；失败则装饰圆占位并记录）
- [ ] **国籍**：封面顶部明示"美国"
- [ ] **引语核对**：仅四段明载引语，其余不得出现引号"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
