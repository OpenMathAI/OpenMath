# Karl Ziegler（卡尔·齐格勒）立传提示词

> qid=Q76624 · 1898-11-26 – 1973-08-12 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1963，与 Giulio Natta 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Karl_Ziegler/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` / REST API / Special:FilePath 下载；404 则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 塑料时代的催化剂大师\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「聚合物长链」母题——链状圆点串暗示聚乙烯的碳链生长。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），催化反应式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Karl Waldemar Ziegler（中文惯称：卡尔·齐格勒）
- **生卒**：1898-11-26 生于德国帝国 Helsa（近 Kassel）→ 1973-08-12 逝于西德 Mülheim，享年 74
- **国籍**：Germany（德国）
- **身份**：化学家（organiker；亦为工程师、大学教师、艺术品收藏家）
- **家庭**：路德会牧师 Karl Ziegler 之次子，母 Luise Rall Ziegler；1922 年娶 Maria Kurtz，子女 Erhart（物理学家/专利律师）与 Marianna（医学博士）；1972 年带孙辈看日食的邮轮上染病，一年后去世；夫妻酷爱绘画收藏，42 幅藏画遗赠 Mülheim Ziegler Art Museum
- **教育轨迹**：
  - Kassel-Bettenhausen 小学；Kassel 中学（毕业年度最杰出学生奖）
  - 一本入门物理教科书点燃科学兴趣——在家做实验、超纲阅读
  - University of Marburg（凭雄厚背景免修前两学期；1918 曾被征召赴一战前线）
  - 博士：1920，师从 Karl von Auwers，论文 "Studies on semibenzole and related compounds"（衍出 3 篇论文）
- **导师**：Karl von Auwers（马尔堡大学博士导师）
- **研究领域**：有机化学——自由基、大环化合物、有机金属化学（有机锂/有机铝）、聚合反应

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **牧师之家（1898）**：父亲引荐他结识包括白喉疫苗发现者 Behring 在内的名流；一本物理教科书开启自学实验之路。
2. **战火中的博士（1918–1920）**：学业被一战征召打断，复员后 1920 年在 von Auwers 门下获博士学位。
3. **三价碳自由基（1923–1925）**：制备 1,2,4,5-四苯基烯丙基（1923）与五苯基环戊二烯基（1925）——远比三苯甲基稳定的自由基，颠覆"必须芳香基团"的旧印象。
4. **大环化学（1933）**：Ruggli–Ziegler 高稀释原理；C14–C33 大环脂环酮 60–80% 收率；专著《Vielgliedrige Ringsysteme》——1935 年获 Liebig 奖章。
5. **有机锂试剂（1930）**：金属锂 + 卤代烃直接合成烷基锂/芳基锂（金属-卤素交换）——有机锂试剂从此成为合成化学家最趁手的工具之一。
6. **活性聚合前夜（1927）**：苯基异丙基钾与茋的加成导致红→黄变色——首次观察到有机碱金属化合物跨 C=C 加成；丁二烯逐次加成得带活性末端的长链——"living polymers" 的前身。
7. **海德堡十年（1926–1936）**：教授；三价碳自由基稳定性 → 有机金属 → 大环 → 聚合的研究主线在此成形。
8. **哈勒与米尔海姆（1936–1943）**：哈勒大学化学研究所教授兼所长、芝加哥大学访问讲师；1943 起任 Max Planck Institute for Coal Research（前身 Kaiser-Wilhelm 研究所）所长直至 1969——接替 Franz Fischer。
9. **镍盐的意外（约 1953）**：乙烯-烷基铝反应本应得高级烷基铝，却几乎只出二聚体 1-丁烯——追查发现是痕量镍盐作祟；逆向推理：换一种金属或许能推迟消除反应、加速链增长。
10. **钛的力量（与 Breil）**：铬、锆、尤其钛盐不促进消除反而极大加速链增长；常压下把乙烯通入催化量 TiCl₃ + Et₂AlCl 的烷烃溶液，立即析出聚乙烯——分子量 > 30,000 的低压高密度聚乙烯，优于既有全部工艺。
11. **Natta 与 Montecatini（1952）**：向意大利 Montecatini 公司披露催化剂（Natta 任顾问）；Natta 把这类催化剂命名为 "Ziegler catalysts" 并将其推向 α-烯烃立构规整聚合；Ziegler 自己专注于聚乙烯与乙烯/丙烯共聚物。
12. **1963 诺贝尔化学奖**：与 Giulio Natta 共享，表彰其有机金属化合物的杰出工作意外地引出了新的聚合反应、为全新且极具实用价值的工业过程铺平道路。
13. **战后重建者与富有的科学家**：战后德国化学研究复兴的中坚——1949 年参与创建德国化学会（GDCh）并任主席五年（1954–1957 任石油科学与煤化学学会主席）；与研究所的专利协议让他成为富翁，斥资约 4000 万马克设 Ziegler Fund 支持研究所研究；1971 当选皇家学会外籍会员。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫罗兰 deepviolet） | `#46356B` | 有机金属催化的深沉与工业厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（聚合反应 badgePoly） | `#5A4AA0` | 蓝紫低压聚乙烯 / 活性聚合 |
| 分类色 2（有机金属 badgeOrgano） | `#1B6B8F` | 青有机锂 / 烷基铝 / TiCl₃ |
| 分类色 3（自由基与大环 badgeRing） | `#B0432A` | 砖红三价碳自由基 / 大环酮 |
| 分类色 4（工业与学会 badgeIndustry） | `#2E6B4F` | 绿 MPI 煤炭研究所 / GDCh |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应聚合物长链上重复单元的排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`，不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：觉醒 / 上扬 / 史诗感
- **匹配理由**：
  - "觉醒" 匹配其科学直觉——从镍盐异常中"醒来"看穿催化本质的顿悟时刻
  - "上扬" 匹配工业革命气质——实验室发现到塑料时代的产业浪潮
  - "史诗感" 匹配叙事跨度——牧师之子 → 一战前线 → 米尔海姆 → 诺贝尔奖
- **时长**：对齐 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 塑料时代的催化剂大师 / Karl Ziegler 1898–1973 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  齐格勒的一生 — 高斯式时间线（10 节点：1898→1920→1926→1930→1933→1936→1943→1953→1963→1973）
04  早年：牧师之家与一战 (1898–1920) — 表格「时间|事件|结果」
05  自由基与大环 (1923–1935) — 表格「对象|方法|结果」+ 公式框：Ruggli–Ziegler 高稀释原理 · C14–C33
06  有机金属化学 (1927–1930) — 表格「问题|方法|结果」+ 公式框：Li + RX → RLi（金属-卤素交换）
07  米尔海姆岁月 (1943–1969) — 表格「机构|角色|结果」
08  镍盐异常与钛催化 (1953–1954) — 表格「异常|推理|结果」+ 公式框：乙烯 + TiCl₃/Et₂AlCl → HDPE（常压）
09  1963 诺贝尔化学奖（与 Natta 共享） — 表格「人物|贡献|结果」+ 公式框：官方获奖理由英文原文
10  Ziegler–Natta 催化剂的分工 — 表格「人物|方向|结果」（Ziegler 聚乙烯 / Natta 立构规整聚丙烯）
11  荣誉与纪念 — 高斯式「类别|代表|意义」表格（Liebig 1935 / Siemens Ring 1960 / Pour le Mérite 1969 / FRS 1971）
12  战后德国化学的重建 — 高斯式流程图（GDCh 1949 → 主席五年 → Ziegler Fund 4000 万马克 → Karl-Ziegler-Schule）
13  遗产：塑料时代 — 四分类遗产盒 + 公式框：Ziegler–Natta 催化剂 → 全球聚烯烃工业
14  结尾 — 「一次意外的二聚，长出了整个塑料时代。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖获奖理由 | 官方英文原文 page.md 明载：`[His] excellent work on organometallic compounds has unexpectedly led to new polymerization reactions and thus paved the way for new and highly useful industrial processes.`——可整句引用，勿改写 |
| 共享方向 | 1963 与 **Giulio Natta 共享**；Ziegler 主攻聚乙烯与乙烯/丙烯共聚物、Natta 主攻丙烯立构规整聚合——勿把聚丙烯的功劳写成 Ziegler 的 |
| "Ziegler catalysts" 命名 | 该名称是 **Natta** 取的（1952 年向 Montecatini 披露后）——勿写成 Ziegler 自命名 |
| 镍盐异常方向 | 痕量镍盐导致**消除反应**（出 1-丁烯二聚体）而非链增长——勿写成"镍催化聚合"；加速链增长的是 **Ti（及 Cr/Zr）** |
| muscone 归属 | page.md 原句是"该合成路线的杰出实例是 **Ružička** 制备麝香酮"——是方法对照，**勿写 Ziegler 合成了麝香酮** |
| 一战经历 | 1918 年被征召赴前线，学业中断——勿写"免服兵役" |
| 博士年份 | 1920（Marburg，von Auwers 门下）——勿写 1923 |
| 战时身份 | page.md 明载其为党卫队资助会员（Patron Member of the SS）、1940 获二级战功十字章——如呈现须严格按 page.md 措辞并保持史实中性；立传建议一笔带过或回避展开 |
| 政治与种族法 | Ziegler 篇无相关内容，禁引入 Natta 篇的 Levi 事件 |
| 妻子 | Maria Kurtz（1922 结婚，1980 年去世）——勿与研究所/基金混淆 |
| fields 口径 | metadata.json 的 field_of_work 写 "inorganic chemistry"，与 infobox "Organic chemistry" 矛盾——**以 page.md infobox 为准**，fields 用 organometallic/polymer/organic chemistry |
| 同名区分 | Karl Ziegler（化学家，1898–1973）≠ Karl von Auwers（导师）；论文标题 "semibenzole" 按 page.md 原文拼写，勿"纠正"为现代命名 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76624 | ✅ |
| name_zh | 卡尔·齐格勒 | ✅ |
| name_en | Karl Ziegler（page.md 规范名；库内无既有记录） | ✅ |
| birth_date | 1898-11-26 | ✅ |
| death_date | 1973-08-12 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organometallic chemistry / polymer chemistry / organic chemistry / free radical chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Karl von Auwers | 师→生（博士导师） | Marburg，1920 年博士 |
| advisor-student | H. Breil | 齐格勒→学生 | 共同发现钛盐极大加速乙烯链增长 |
| co-honored | Giulio Natta | 无向 | 1963 诺贝尔化学奖共同得主 |
| colleague | Otto Bayer | 无向 | 1960 年 Werner von Siemens Ring 同获 |
| colleague | Walter Reppe | 无向 | 1960 年 Werner von Siemens Ring 同获 |
| colleague | Franz Fischer | 无向 | 接其任 Kaiser-Wilhelm/Max Planck 煤炭研究所所长 |
| spouse | Maria Kurtz | 无向 | 1922 结婚，育 Erhart 与 Marianna |

> **禁入库名单**（page.md 提及但无个人实质关系）：Emil Adolf von Behring（父亲引荐的名流）、Leopold Ružička（muscone 方法对照非个人交往）、Cordula Witte（孙女）、子女 Erhart/Marianna（按批次惯例不入库）。metadata-only 无新增。

## 8. 奖项清单

- Nobel Prize in Chemistry（1963，与 Giulio Natta 共享）
- Liebig Medal（1935，大环体系与稳定三价碳自由基）
- War Merit Cross 2nd Class（1940-10-19）
- Carl Duisberg Plakette（1953）
- Lavoisier Medal（1955，法国化学会）
- Carl Engler Medal（1958）
- Werner von Siemens Ring（1960，与 Otto Bayer、Walter Reppe 同获）
- Swinburne Medal, Plastics Institute, London（1964）
- Grand Merit Cross with Star and Sash, Federal Republic of Germany（1964）
- International Synthetic Rubber Medal（1967）
- Grand Federal Cross of Merit（1969）；Pour le Mérite for Arts and Sciences（1969）
- Foreign Member of the Royal Society（1971）；Wilhelm Exner Medal（1971）
- Honorary doctorates：Hannover、Giessen、Heidelberg、Darmstadt
- GDCh Historic Landmarks of Chemistry 纪念牌（2008，米尔海姆研究所）；Karl Ziegler Prize（GDCh 设立，5 万欧元）

## 9. 机构清单

- 教育：Kassel 中小学、University of Marburg（免修前两学期；PhD 1920）
- 任职：Marburg / Frankfurt 讲师；University of Heidelberg 教授（1926–1936）；University of Halle-Saale 化学研究所教授兼所长（1936–）；University of Chicago 访问讲师；Max Planck Institute for Coal Research 所长（1943–1969，米尔海姆）
- 学会：德国化学会 GDCh 创建人之一（1949）与主席（五年）；German Society for Petroleum Science and Coal Chemistry 主席（1954–1957）；Royal Society 外籍会员（1971）
- 命名机构：Karl-Ziegler-Schule（米尔海姆，1974-12-04 更名成立）；Ziegler Fund（约 4000 万马克）；42 幅藏画遗赠 Mülheim Ziegler Art Museum

## 10. 终审清单

- [x] 生卒 1898-11-26 / 1973-08-12，享年 74，出生地 Helsa、去世地 Mülheim
- [x] 1963 与 Natta 共享；官方获奖理由英文原文整句引用无误
- [x] 镍盐=意外（消除反应）、钛=加速链增长；HDPE MW>30,000、常压
- [x] "Ziegler catalysts" 由 Natta 命名；muscone 归 Ružička
- [x] 博士 1920（von Auwers）；一战 1918 征召表述准确
- [x] Siemens Ring 1960 三人（Otto Bayer、Walter Reppe）；FRS 1971
- [x] 战时 Patron Member of SS 表述中性且不展开（或回避）
- [x] 引语全部可在本地 Wikipedia 原文找到（诺奖理由原句、1972 日食邮轮染病句）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 链状气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Karl_Ziegler/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 下载并核验（page.md 内嵌图为研究所与纪念牌照片，肖像 404 则装饰圆占位）
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（诺奖理由整句、Siemens Ring 三人句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐；与 Giulio Natta 篇（本批）共享口径互查

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`，本文件不改总表。
