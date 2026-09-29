# Linus Pauling（莱纳斯·鲍林）立传提示词

> qid=Q48983 · 1901-02-28 – 1994-08-19 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1954，独享）+ 诺贝尔和平奖（1962，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Linus_Pauling/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次书写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位；若无真实肖像按 Review-1 流程先补图，全部 404 才允许装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 化学键的解锁者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「化学键 / 螺旋」母题——圆点连线暗示原子成键、肽链成螺旋。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Linus Carl Pauling（中文惯称：莱纳斯·卡尔·鲍林）
- **生卒**：1901-02-28 生于俄勒冈州波特兰 → 1994-08-19 逝于加州大苏尔（Big Sur）家中（前列腺癌），享年 93
- **国籍**：United States（美国）
- **身份**：化学家、和平活动家；**史上唯一两获不共享诺贝尔奖者**（化学 1954 + 和平 1962）；与居里夫人并列仅有的两位"不同领域双诺奖"得主
- **家庭**：长子；父 Herman Henry William Pauling（药剂师，1910 年病逝），母 Lucy Isabelle "Belle" Darling；1923-06-17 娘家课偶遇的 Ava Helen Miller 成为其妻（人权活动家，1981 年去世，婚姻持续 58 年）；四子女：Linus Jr.（精神病学家）、Peter（晶体学家）、Edward Crellin（生物学家）、Linda（嫁地质学家 Barclay Kamb）
- **教育轨迹**：
  - 高中学分已够入大学，却因缺两门美国史课程被拒发毕业证——45 年后母校补授荣誉文凭（时已双诺奖）
  - 1917 入俄勒冈州立大学（时名 Oregon Agricultural College），边读书边打工教书；1922 化工学士
  - 加州理工 Caltech 博士，1925 以 *The Determination with X-Rays of the Structures of Crystals* 获物理化学与数学物理博士（summa cum laude）
- **导师**：Roscoe G. Dickinson、Richard Chace Tolman（Caltech 博士导师，双导师）；游学私人顾问 Arnold Sommerfeld、Niels Bohr（infobox Other academic advisors）
- **研究领域**：量子化学、化学键本质、结构化学、生物化学、分子生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **波特兰少年（1901）**：友人家中一套化学实验箱令他"被化学现象迷住"；高中靠废钢厂捡设备做实验、办 Palmon Laboratories 失败。
2. **俄勒冈州立（1917–1922）**：家贫打工——杂货店周薪 8 美元、机工学徒月薪 50 美元；大二起当定量分析助教自养学业；在家政专业化学课上遇见 Ava Helen。
3. **Caltech 与 X 射线（1922–1925）**：博士期间发表七篇矿物晶体结构论文。
4. **欧洲游学（1926–1927）**：Guggenheim 奖金下先后师从 Sommerfeld（慕尼黑）、Bohr（哥本哈根）、Schrödinger（苏黎世）；受 Heitler–London 氢分子键量子处理启发，确立终生方向——用量子力学解化学键。
5. **杂化轨道与电负性（1931–1932）**：提出轨道杂化概念解析碳四价（自称最重要的论文）；1932 建立电负性标度（Pauling 电负性标度沿用至今）。
6. **Pauling 规则（1929）**：五条离子晶体结构规则，预言与解释复杂矿物结构。
7. **《化学键的本质》（1939）**：在 Cornell 十九场讲座成书——"本世纪化学最有影响的书、其实效圣经"，头 30 年被引超 16,000 次；1954 诺奖主要依据："for his research into the nature of the chemical bond and its application to the elucidation of the structure of complex substances"（独享）。
8. **共振论**：苯不是两种 Kekulé 结构的快速互变，而是它们的叠加——"共振"概念重塑芳香化学。
9. **α 螺旋与 β 折叠（1951）**：与 Robert Corey、Herman Branson 提出蛋白质二级结构基本单元——关键是非整圈假设（α 螺旋每圈 3.7 个氨基酸残基）。
10. **分子病（1949）**：与 Itano、Singer、Wells 论证镰状细胞贫血是"分子疾病"——首个在分子层面理解的人类遗传病，分子遗传学之 dawn。
11. **DNA 之憾（1952–1953）**：提出三螺旋模型含基础错误；Watson/Crick 随后得双螺旋正确结构；鲍林自述这是他一生 "the biggest disappointment"。护照风波（1952 被拒发）并非主因——他数周后即取回护照，却未去 Franklin 实验室。
12. **和平运动（1946–1963）**：加入 Einstein 主持的原子科学家紧急委员会；1955 签署 Russell–Einstein 宣言；1958 向联合国递交 50 国 11,021 科学家反核试请愿、与 Teller 电视辩论、出版 *No More War!*；1963-10-10《部分禁止核试验条约》生效当日获授 1962 年诺贝尔和平奖。
13. **维生素C 争议晚年（1966–1994）**：经 Irwin Stone 引入大剂量维 C；1968 创"orthomolecular（正分子）"一词；1970 《Vitamin C and the Common Cold》；与 Cameron 合作抗癌研究遭 Mayo Clinic 临床试验否定，主流医学界不认可——鲍林至死坚持并斥其结论 "fraud and deliberate misrepresentation"；1973 创立 Linus Pauling Institute。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深血红 crimson） | `#7E1E23` | 化学键的能量与和平运动的赤诚（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（化学键 badgeBond） | `#2E5A9E` | 蓝杂化轨道 / 电负性 |
| 分类色 2（蛋白质结构 badgeHelix） | `#1B7A43` | 绿 α 螺旋 / β 折叠 |
| 分类色 3（分子遗传学 badgeGene） | `#B4632A` | 琥珀分子病 / 分子钟 |
| 分类色 4（和平运动 badgePeace） | `#6E4E7E` | 紫反核试 / 双诺奖 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点成键呼应「原子 → 分子 → 螺旋」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（文件：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`；勿复制 wav，视频阶段直接引用路径）
- **风格**：纪录片 / 内省 / 光与暗交织
- **匹配理由**：
  - "看不见的光" 匹配其一生主题——化学键、螺旋、分子病皆是肉眼不可见却决定一切的结构
  - "纪录片" 匹配双线叙事——实验室的量子化学与街头的和平请愿交替推进
  - 内省气质匹配其晚年争议——维生素C 之辩与"一生最大失望"，比英雄史诗更真实
- **时长**：以实际文件为准，视频合成用 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 化学键的解锁者 / Linus Pauling 1901–1994 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  鲍林的一生 — 时间线（10 节点：1901→1922→1925→1927→1931→1939→1951→1954→1962→1994）
04  早年：波特兰与俄勒冈 (1901–1922) — 表格「时间|事件|结果」
05  Caltech 与欧洲游学 (1922–1927) — 表格「时间|事件|结果」（Dickinson/Tolman → Sommerfeld/Bohr/Schrödinger）
06  化学键的本质 (1928–1939) — 表格「问题|方法|结果」+ 公式框：杂化轨道 sp3 / 电负性差 Δχ 判键性
07  α 螺旋与 β 折叠 (1951) — 表格「问题|方法|结果」+ 公式框：α 螺旋每圈 3.7 残基 + 氢键
08  分子病与分子钟 (1949–1960s) — 表格「对象|发现|意义」（镰状细胞贫血 / Zuckerkandl 分子钟）
09  DNA 之憾 (1952–1953) — 表格「模型|错误|结果」+ 三螺旋 vs Watson-Crick 双螺旋对照
10  双诺奖与和平之路 (1946–1963) — 表格「时间|事件|结果」（紧急委员会/请愿/Teller 辩论/1962 和平奖）
11  荣誉清单 — 「类别|代表|意义」表格 + itemize（1954 化学/1962 和平/Davy 1947/Priestley 1984/National Medal of Science 1974 等）
12  维生素 C 争议 (1966–1994) — 流程图式：Stone 引入 → orthomolecular → 专著 → Mayo 否证 → 坚持至终
13  遗产 — 四分类遗产盒（量子化学/分子生物学/和平主义/ Linus Pauling Institute）+ 公式框：唯一双不共享诺奖
14  结尾 — 「化学键连起原子，良知连起世界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 双诺奖表述 | **唯一两获不共享诺贝尔奖者**；"不同领域双诺奖仅两位，另一位是居里夫人"——三处口径一致，勿写"唯一双诺奖"（Sanger/Bardeen 属同类别） |
| 1954 诺奖理由 | 官方措辞 "for his research into the nature of the chemical bond and its application to the elucidation of the structure of complex substances"（独享）——勿泛化成"创立量子化学" |
| 1962 和平奖 | 授奖年份 1962、颁授在 1963-10-10（条约生效当日）——页面口径 "Nobel Peace Prize (1962)"，写作时注明 1963 年 10 月颁授 |
| α 螺旋作者序 | Pauling、**Corey、Branson** 三人 1951 共同提出（页面亦作 Pauling–Corey–Branson alpha helix）——勿独写 Pauling |
| DNA 错误 | 三螺旋模型的错误是**中性磷酸基团**假设等；"错失 DNA"有政治传说成分——页面明载"politics did not play a critical role"（他取回护照后未去 Franklin 实验室），勿渲染"因麦卡锡主义错过诺奖" |
| 引语红线 | "the biggest disappointment in his life" 为页面原句可引；"I was simply entranced by chemical phenomena..."（自述入行）为页面引文可引；其余无出处引语禁写 |
| 学生态 | infobox Doctoral students 共 **11 人**（含 Lipscomb 1976 化学诺奖、Karplus 2013 化学诺奖）；Edwin McMillan 是**本科生**（Other notable students Undergrads）——勿写成博士生 |
| Oppenheimer 关系 | 密友反目：Oppenheimer 邀约 Ava Helen 致绝交；曼哈顿计划曾邀鲍林主持化学部被婉拒——按页面客观一句，勿添戏剧化细节 |
| 敏感点：优生学 | 页面载 Pauling 支持有限优生学（缺陷基因携带者强制标记）——**建议整页回避**；若写仅客观一句置于争议小节 |
| 敏感点：政治 | 参议员小组委员会传唤、National Review 诽谤诉讼、越南战争言论等按页面事实克制陈述；Ho Chi Minh 通信仅一句带过或回避 |
| 维生素 C 口径 | 必须写明"主流科学界/医学界不认可、Mayo Clinic 试验否定"——不得写成"大剂量维 C 有效"；其抗辩原话 "fraud and deliberate misrepresentation" 可引并注明为其个人指控 |
| 奖项年份 | Davy Medal 1947、Nobel Chemistry 1954、Nobel Peace 1962、Lenin Peace Prize 1968–1969（页面 Awards 表口径）、National Medal of Science 1974、Priestley 1984——勿错位 |
| 入行契机 | 归功友人 Lloyd A. Jeffress 的化学实验箱（页面明载）；Palmon Laboratories 是与 Lloyd Simon 合办的失败生意——两个 Lloyd 勿混 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48983 | ✅ |
| name_zh | 莱纳斯·鲍林 | ✅ |
| name_en | Linus Pauling | ✅（复用库内 id=2034 记录回填 QID，勿另建全名 stub） |
| birth_date | 1901-02-28 | ✅ |
| death_date | 1994-08-19 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | quantum chemistry（person_field 细分：quantum chemistry / chemical bonding / biochemistry / molecular biology，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 游学导师**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Roscoe G. Dickinson | 师→生（博士导师） | Caltech，X 射线晶体结构方向 |
| advisor-student | Richard Chace Tolman | 师→生（博士导师） | 双导师之一 |
| influence | Arnold Sommerfeld | 无向 | 1926–27 Guggenheim 欧洲游学导师（慕尼黑） |
| influence | Niels Bohr | 无向 | 1926–27 欧洲游学导师（哥本哈根） |

**门生（Pauling → 学生，源自本地 infobox Doctoral students 11 人）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William Lipscomb | Pauling → 学生 | 1976 诺贝尔化学奖 |
| advisor-student | Martin Karplus | Pauling → 学生 | 2013 诺贝尔化学奖 |
| advisor-student | Jerry Donohue | Pauling → 学生 | infobox Doctoral students |
| advisor-student | Harvey Itano | Pauling → 学生 | 1949 镰状细胞贫血分子病论文合作者 |
| advisor-student | Barclay Kamb | Pauling → 学生 | 后为 Caltech 地质学家，娶其女 Linda |
| advisor-student | Matthew Meselson | Pauling → 学生 | infobox Doctoral students |
| advisor-student | Leonard Lerman | Pauling → 学生 | infobox Doctoral students |
| advisor-student | Kurt Mislow | Pauling → 学生 | infobox Doctoral students |
| advisor-student | Arthur Pardee | Pauling → 学生 | infobox Doctoral students |
| advisor-student | Robert E. Rundle | Pauling → 学生 | infobox Doctoral students |
| advisor-student | Edgar Bright Wilson | Pauling → 学生 | infobox Doctoral students |

**同事 / 合作者 / 论战对手 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Robert Corey | 无向 | 长期合作者，α 螺旋与 β 折叠共同提出者 |
| colleague | Herman Branson | 无向 | 1951 α 螺旋/β 折叠共同提出者 |
| colleague | Charles D. Coryell | 无向 | 血红蛋白结构研究合作（正文称 his student，infobox 列 postdoc） |
| colleague | J. Robert Oppenheimer | 无向 | Caltech 年度访客密友，后因私人龃龉决裂；曾邀其主持曼哈顿计划化学部被婉拒 |
| competitor | Edward Teller | 无向 | 1958 电视辩论核试验放射性尘埃致突变风险 |
| influence | James Watson | 无向 | 页面明载其化学键与蛋白质结构工作启发了 Watson/Crick 的 DNA 研究 |
| influence | Francis Crick | 无向 | 同上；Crick 称其为"分子生物学之父" |
| spouse | Ava Helen Pauling | 无向 | 1923-06-17 结婚（本名 Ava Helen Miller），人权活动家，1981 去世 |

> **禁入库名单**（页面 infobox 有载但本批不入库的裁定）：Edwin McMillan（仅本科生 notable students，非博士生，库内另有独立记录易混淆）；10 位 postdoc（Coryell、Dunitz、Fox、Gordy、Heilbronner、Ketelaar、Hans Kuhn、Orgel、Rich、Singer）——非博士生防 stub 噪声；Emile Zuckerkandl（分子钟合作者，正文称 his student，如 Review 认定入库可补 advisor-student）；Warren Weaver、Thomas Hunt Morgan、William Astbury、Robert Mulliken 等为叙事语境提及，非直接关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1954，独享）；Nobel Peace Prize（1962，1963-10-10 颁授）
- ACS Award in Pure Chemistry（1931）；Irving Langmuir Award（1931）
- 美国国家科学院院士（1933）；美国哲学学会（1936）；AAAS Fellow
- Davy Medal（1947）；Presidential Medal for Merit（1948，杜鲁门颁）
- Roebling Medal（1967）；Gandhi Peace Award；Lenin International Peace Prize（1968–1969）
- National Medal of Science（1974）；Lomonosov Gold Medal（1977）
- NAS Award in Chemical Sciences（1979）；Priestley Medal（1984）
- Vannevar Bush Award（1989）；California Hall of Fame（2008 入选）
- 约 47 个荣誉学位（剑桥、牛津、普林斯顿、耶鲁等）；小行星 4674 Pauling（1991，90 岁生日命名）；俄勒冈州 "Linus Pauling Day"（2 月 28 日）

## 9. 机构清单

- 教育：Washington High School（ Portland，未获文凭，45 年后补荣誉文凭）、Oregon State University（BS 1922）、Caltech（PhD 1925）
- 任职：Caltech（1927–1963，1936 起任化学与化工分部主任兼 Gates & Crellin 实验室主任至 1958）；Center for the Study of Democratic Institutions（1963–1967）；UC San Diego（1967–1969）；Stanford（1969–1975）；访问：Cornell（1937–38 Baker 讲座）、Oxford（1948 George Eastman 教授）
- 命名机构：Linus Pauling Institute（1973 创立，1996 迁俄勒冈州立大学）；Oregon State Linus Pauling Science Center

## 10. 终审清单

- [ ] 生卒 1901-02-28 / 1994-08-19（享年 93），出生地 Portland、去世地 Big Sur
- [ ] "唯一两获不共享诺奖者"与"不同领域双诺奖仅两位（另一位居里夫人）"两处口径一致
- [ ] 1954 化学奖独享、理由用官方原文；1962 和平奖注明 1963-10-10 颁授
- [ ] α 螺旋三作者（Pauling/Corey/Branson，1951）；分子病论文四作者（1949）
- [ ] DNA 三螺旋错误 + "politics did not play a critical role" 口径落实
- [ ] 博士生 11 人入库；McMillan 本科生、postdoc 10 人不入库裁定保留
- [ ] 维生素 C 争议写明主流医学界否定；优生学与政治敏感点按 §5 口径回避或克制
- [ ] 引语均可溯源（entranced 自述、biggest disappointment、诺奖理由两句）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Linus_Pauling/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像就位与图注核对（页面有 1940s/1955/1962 等多张照片可选）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：引语必须在 Wikipedia 原文找到（获奖理由、entranced、biggest disappointment）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
> **数据入库**：yaml 见 `MySQL/data/Linus_Pauling.yaml`（复用库内记录 UPD 回填 QID，含 4 fields / 23 relations）。
