# Yuan T. Lee（李远哲）立传提示词

> qid=Q243190 · 1936-11-19 – 在世 · 台湾物理化学家 · 20 世纪 · 诺贝尔化学奖（1986，与 Dudley R. Herschbach、John C. Polanyi 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Yuan_T._Lee/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`（表格语义化 tabularx + 公式展示框 + 时间线页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Yuan_Tseh_Lee_HD2008_Othmer_Gold_Medal_portrait.JPG` 已就位——2008 年 Othmer 金勋章官方照；中文名"李遠哲"可作为副标题小字注）。
2. **封面有国籍/出身**：顶部副标题明示出身（`\faIcon{atom}\enspace 交叉分子束的驭手\enspace·\enspace 台湾新竹`），底部状态栏给出 `出身 | 机构 | 主要成就` 三要素。**只写"台湾新竹/台湾化学家"，与政体、政权相关的表述一律回避。**
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍变迁（公民身份时间线按 infobox：1936–1945 / 1945– / 1974–1994 三段，仅作事实陈述）、教育（NTU/清华/伯克利）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），母题呼应「两束分子在反应腔中心交叉」——相向点列在中点交汇。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（交叉分子束角度/速度分布 → 反应动力学信息）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Yuan Tseh Lee（李遠哲；拼音 Lǐ Yuǎnzhé；闽南语 Lí Oán-tiat；中文惯称：李远哲）
- **生卒**：1936-11-19 生于日据台湾新竹（Shinchiku，今 Hsinchu）（在世，卒日留白）
- **公民身份变迁**（infobox 事实陈述）：1936–1945 日本帝国；1945– 中华民国（台湾）；1974–1994 美国（1994 为出任中研院院长放弃美国国籍）
- **家庭**：父李澤藩（Lee Tze-fan）是画家；母蔡配（Ts'ai P'ei）是小学教师（出身台中梧棲）；祖籍福建南安。兄李遠川（Yuan-Chuan Lee，Johns Hopkins 教授 40 年）、弟李遠鵬（Yuan-Pern Lee）、妹李季眉（Chi-Mei Lee，中兴大学教授）皆学有成
- **教育轨迹**：
  - 新竹小学（棒球队与乒乓球队）；新竹中学（网球、长号、长笛）
  - 免试直接保送 National Taiwan University，1959 BS
  - National Tsing Hua University，1961 MS
  - University of California, Berkeley，1965 PhD（论文 Photoionization of alkali-metal vapors）
- **导师**：Bruce H. Mahan（伯克利博士导师）；博士后导师 Dudley R. Herschbach（1967，哈佛）
- **研究领域**：物理化学——化学动力学、交叉分子束、反应动力学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **新竹少年（1936）**：画家之子、小学教师之母；棒球、乒乓、网球、长号、长笛——体艺俱全的理科少年。
2. **免试保送（1955 前后）**：免入学考试直接进入台湾大学，1959 化学学士；1961 清华硕士。
3. **负笈伯克利（1961–1965）**：在 Bruce H. Mahan 指导下研究碱金属蒸气的光电离，1965 PhD。
4. **转战哈佛（1967-02）**：加入 Dudley Herschbach 实验室做博士后——研究氢原子与双原子碱金属分子的反应，并参与建造通用交叉分子束装置。
5. **芝加哥执教（1968）**：博士后一年后加入 University of Chicago 教鞭。
6. **回归伯克利（1974）**：任化学教授、Lawrence Berkeley National Laboratory 首席研究员；同年入籍美国。
7. **交叉分子束技术**：以突破性的"crossed molecular beams technique"测量**角度分布与速度分布**，从中读出基元化学反应的动力学信息。
8. **研究纲领**：控制反应物能量、理解化学反应性对分子取向的依赖、反应中间体本性、衰变动力学、复杂反应机理的识别。
9. **1986 诺贝尔化学奖**：与 Herschbach、Polanyi 三人共享，理由 "contributions to the dynamics of chemical elementary processes"（page.md 口径）； Lee 是**第一位获诺贝尔奖的台湾人**。
10. **中研院院长（1994–2006）**：1994-01-18 就任第七任院长（至 2006-10-18）；为就任放弃美国国籍；任内创设新研究所、延揽顶尖学者、推进台湾科研。
11. **国际科学界领袖**：1977–1984 Chemistry International Board 成员；2008 当选国际科学理事会（ICSU）主席、2011 就任；Malta Conferences 中东科学家合作倡议——为台湾同步辐射光源提供六个奖学金名额。
12. **气候与公益**：2015 签署 Mainau 宣言（关注人为气候变化）；2021 将诺贝尔奖章捐给台湾历史博物馆展出；吴健雄学术基金会四位发起诺奖得主之一。
13. **荣誉等身**：Sloan Fellow（1969）、美国艺术与科学院 Fellow（1975）、美国物理学会 Fellow（1976）、Guggenheim（1977）、美国国家科学院院士（1979）、中研院院士（1980）、E.O. Lawrence Award（1981）、Harrison Howe Award（1983）、Peter Debye Award（1986）、National Medal of Science（1986）、Golden Plate（1987）、Faraday Lectureship Prize（1992）、Othmer Gold Medal（2008）、Fray International Sustainability Award（2019）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（赭红 brick red） | `#A63A2B` | 反应腔中交叉束流的热点（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（交叉分子束 badgeBeam） | `#2E5A9E` | 蓝交叉束 / 角度与速度分布 |
| 分类色 2（反应动力学 badgeDyn） | `#1B7A43` | 绿基元反应 / 能量控制 |
| 分类色 3（分子取向 badgeOrient） | `#D97B29` | 琥珀取向依赖 / 中间体 |
| 分类色 4（科学领导 badgeLead） | `#6B4E16` | 棕中研院 / ICSU / 气候公益 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 篇一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题「两束分子相向而行、于反应中心交汇」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（清单预置 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`；执行时按项目惯例软链至本目录，不复制 wav 文件）
- **风格**：内省 / 情感纵深 / 纪录片
- **匹配理由**：
  - 内省感匹配交叉分子束实验"在真空腔体中静静守候一次碰撞"的工作气质
  - 情感纵深匹配跨越太平洋的求学与归返（新竹→伯克利→哈佛→芝加哥→伯克利→中研院）
  - 纪录片感匹配 1986 三人共享诺奖与四十年科学生涯的传记叙事
- **时长核对**：执行时确认音轨时长 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 交叉分子束的驭手 / Yuan T. Lee 李遠哲 1936– + 四色 badge + 右上头像 + 出身行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/公民身份三段时间线/教育/博士导师/领域/荣誉）
03  李远哲之路 — 时间线（10 节点：1936→1959→1961→1965→1967→1968→1974→1986→1994→2021）
04  新竹少年 (1936–1959) — 表格「时间|事件|结果」（家庭/体艺/免试保送 NTU）
05  从清华到伯克利 (1961–1965) — 表格「时间|事件|结果」+ 公式框：碱金属蒸气光电离（PhD 1965）
06  哈佛博士后：通用装置 (1967) — 表格「人物|工作|成果」（Herschbach 组 supermachine）
07  芝加哥与伯克利 (1968–) — 表格「时间|事件|结果」
08  交叉分子束技术 — 表格「问题|方法|结果」+ 公式框：角度/速度分布 → 反应动力学
09  1986 诺奖 — 表格「三人|方法|贡献」（与 Herschbach、Polanyi 共享）+ 公式框：基元过程动力学
10  中研院院长 (1994–2006) — 表格「举措|内容|意义」（放弃美籍就任/设所揽才）
11  国际科学与公益 — 双栏页：ICSU 主席（2008 当选/2011 就任）/ Malta Conferences / Mainau 宣言 / 奖章捐赠
12  荣誉清单 — 「类别|代表|意义」表格（含 itemize：诺奖/National Medal of Science/各奖章/院士头衔）
13  遗产：第一位台湾诺奖得主 — 四分类遗产盒 + 吴健雄学术基金会
14  结尾 — 「在真空的舞台中央，看见分子相遇的每一瞬间。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 政治内容（★ 红线） | page.md Politics 一节（2000/2004/2012 选举立场、政党支持、组阁提名）与 APEC 代表经历**一律禁写**；只写学术、科研行政与国际科学公益；国籍/身份只按 infobox 三段时间线作事实陈述，不做政权评价 |
| 获奖理由口径 | page.md intro 作 "for his contributions to the development of reaction dynamics"；三人共享理由作 "contributions to the dynamics of chemical elementary processes"——两处均按 page.md 原文，勿混写、勿另编官方全句 |
| 三人共享方向 | Lee 与 Herschbach 做**交叉分子束**；Polanyi 做**红外化学发光**——勿混；Polanyi 与 Lee 之间无师生关系 |
| 与 Herschbach 的关系 | 1967 年李远哲是 Herschbach 组的**博士后**——"post-doctoral supervisor"（page.md Recognition 节明载）；非博士导师 |
| 博士导师 | Bruce H. Mahan（伯克利，1965）——勿与博士后导师 Herschbach 混淆 |
| ICSU 年份 | page.md 内部两说（intro 作 2011 elected、后文作 2008 elected/2011 started）——统一口径"2008 当选、2011 就任"，勿写成"2011 当选" |
| 公民身份 | 1974 入籍美国、1994 为任中研院院长**放弃**美国国籍——方向勿写反 |
| 免试保送 | 免入学考试直接进入 NTU——"保送"语义以 page.md "exempted from the entrance examination" 为准 |
| 兄弟姓名 | 兄 Yuan-Chuan Lee（李遠川）、弟 Yuan-Pern Lee（李遠鵬）、妹 Chi-Mei Lee（李季眉）——三位 L 遠/季同名易混，且**不入社会关系库**（白名单无 sibling 类型） |
| Ryoji Noyori | 与野依良治同为名古屋大学高等研究院名誉院长——机构并任非个人关系，不入库 |
| 引语 | 气候议题两段引语（"We will have to learn to live the simple lives of our ancestors." 等）page.md 明载可引，但属公共议题语境；科学叙事部分全篇无实验室引语——不得编造 |
| 奖章捐赠 | 2021 捐给 National Museum of Taiwan History——勿写成"中央研究院"或"故宫" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q243190 | ✅ |
| name_zh | 李远哲 | ✅ |
| name_en | Yuan T. Lee | ✅（清单指定规范形式，防与本批 Herschbach/Polanyi yaml 对手指名分裂） |
| birth_date | 1936-11-19 | ✅ |
| death_date | （空——在世） | ✅ |
| nationality | Taiwan（rank 0）；United States（rank 1，1974–1994） | ✅（1936–1945 日本帝国身份仅 §1 事实陈述，不入库） |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：physical chemistry / chemical kinetics / reaction dynamics / crossed molecular beams，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bruce H. Mahan | 师→生（博士导师） | 伯克利博士导师（1965，碱金属蒸气光电离） |
| advisor-student | Dudley R. Herschbach | 师→生（博士后导师） | 1967 哈佛博士后，共建通用交叉分子束装置（page.md 明载 post-doctoral supervisor） |
| advisor-student | Laurie Butler | 生←师（学生） | infobox 博士生 |
| advisor-student | Daniel M. Neumark | 生←师（学生） | infobox 博士生 |
| co-honored | Dudley R. Herschbach | 无向 | 1986 诺贝尔化学奖共同得主（交叉分子束） |
| co-honored | John C. Polanyi | 无向 | 1986 诺贝尔化学奖共同得主（红外化学发光） |

> **禁入库名单**：兄 Yuan-Chuan Lee、弟 Yuan-Pern Lee、妹 Chi-Mei Lee（白名单无 sibling 类型）；Ryoji Noyori（机构并任）；Eugene Chien（2024 委员会同僚）；政治人物与 APEC 相关人名（红线禁写）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1986，与 Herschbach、Polanyi 共享）
- National Medal of Science（1986）
- Peter Debye Award in Physical Chemistry（1986）
- Ernest Orlando Lawrence Award（1981）
- Harrison Howe Award（1983）
- Faraday Lectureship Prize（1992）
- Othmer Gold Medal（2008）
- Fray International Sustainability Award（2019）
- Sloan Fellow（1969）；Guggenheim Fellow（1977）；Camille Dreyfus Teacher-Scholar
- Fellow：美国艺术与科学院（1975）、美国物理学会（1976）；美国国家科学院院士（1979）；中研院院士（1980）
- 多校荣誉博士（Ottawa、HKU、香港中文、Waterloo、早稻田、Louis Pasteur 等）

## 9. 机构清单

- 教育：新竹小学、新竹中学；National Taiwan University（BS 1959）；National Tsing Hua University（MS 1961）；University of California, Berkeley（PhD 1965）
- 任职：Harvard University（1967-02，Herschbach 组博士后）；University of Chicago（1968 教鞭）；University of California, Berkeley + Lawrence Berkeley National Laboratory（1974 教授/PI）；Academia Sinica 第七任院长（1994-01-18 – 2006-10-18）；名古屋大学高等研究院名誉院长（与 Ryoji Noyori 并任）
- 公职：Senior Advisor to the President（2000–2001、2016–2020）；National Climate Change Committee 顾问（2024-07 就任）；International Council for Science 主席（2008 当选、2011 就任）

## 10. 终审清单

- [ ] 生卒 1936-11-19 / 在世留白；出生地新竹
- [ ] 公民身份三段时间线只作事实陈述；政治内容零出现
- [ ] 博士导师 Mahan / 博士后导师 Herschbach 双线区分准确
- [ ] 1986 三人共享、理由两处按 page.md 口径；"第一位台湾诺奖得主"表述有载可用
- [ ] ICSU 2008 当选/2011 就任口径统一
- [ ] 2021 奖章捐赠去向准确；引语不编造
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Yuan_T._Lee/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像：Othmer Gold Medal 2008 官方照已就位
- [ ] 出身：封面明示台湾新竹；政治内容零出现（★ 重点核查）
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由 chem-batch-19 批次产出提示词与数据入库；立传与 Review 列由主控统一收尾。
