# Frances Arnold（弗朗西丝·阿诺德）立传提示词

> qid=Q4273363 · 1956-07-25 –（在世）· 美国化学工程师 · 21 世纪 · 诺贝尔化学奖（2018，独享二分之一；另一半由 George P. Smith 与 Greg Winter 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Frances_Arnold/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 取 page.md 首图 "Arnold in 2021"；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 进化的工程师\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Frances Hamilton Arnold）、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「定向演化的迭代轮次」母题——一轮轮突变与筛选的圆点涟漪。
5. **表格语义化 + 公式框**（★ 核心版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Frances Hamilton Arnold（中文惯称：弗朗西丝·阿诺德）
- **生卒**：1956-07-25 生于美国宾夕法尼亚州埃奇伍德（Edgewood, Allegheny County）→ 在世（2026-09 无卒日，年龄留白处理）
- **国籍**：United States（美国）
- **身份**：美国化学工程师；加州理工学院 Linus Pauling 化学工程、生物工程与生物化学教授；2018 诺贝尔化学奖得主（首位获化学诺奖的美国女性——**页面明载**，可用）
- **家庭**：父 Josephine Inman（母，娘家姓 Routheau）与核物理学家 William Howard Arnold（父）之女；祖父 William Howard Arnold 为陆军中将（**父子同名**，叙述须区分）；兄 Bill、三个弟弟 Edward/David/Thomas。1987–1991 嫁 James E. Bailey（Jay Bailey，2001 年癌逝），子 James Howard Bailey（1990）；继子 Sean Bailey（迪士尼影业制片总裁）。1994 起与加州理工天体物理学家 Andrew E. Lange 事实婚姻（common-law），子 William Andrew Lange（1995）、Joseph Inman Lange（1997）；Lange 2010 自杀，William Lange-Arnold 2016 意外离世
- **教育轨迹**：
  - Taylor Allderdice High School（1974 届）；高中时搭便车赴华盛顿抗议越战、独立生活（爵士俱乐部调酒、开出租车）
  - Princeton University 机械与航空航天工程 BS（1979，太阳能研究方向；自述选机械工程是"当时进普林斯顿最容易的路"——Nobel Prize interview 中的转述）
  - 中途休学一年赴意大利工厂（核反应堆零件）；在 Robert Socolow 领导的能源与环境研究中心接触可持续能源
  - UC Berkeley 化学工程 PhD（1985，Harvey Warren Blanch 实验室；亲和层析）
- **导师**：Harvey W. Blanch（博士导师）
- **博士**：1985，《Design and Scale-Up of Affinity Separations》——读博前无化学背景，第一年须补修本科化学课
- **研究领域**：化学工程、生物工程、生物化学——定向演化、蛋白质工程、生物催化

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **匹兹堡独立少女（1970s）**：离家独居、调酒开车、搭便车去反战——"同一种独立"后来变成挑战教科书式理性设计（rational design）的科研风格（页面行文支持的引申，间接转述）。
2. **普林斯顿的"最容易的路"（1975–1979）**：机械与航空航天工程 BS——太阳能研究埋下绿色能源的一生伏笔。
3. **世界工程师（1979–1983）**：韩国、巴西做工程师，科罗拉多太阳能研究所（今 NREL）为偏远地区设计太阳能设施、参与撰写联合国立场文件。
4. **伯克利转身（1983–1985）**：无化学底子读化学工程博士，亲和层析的放大设计——工程视角成为她日后做酶的独特武器。
5. **加州理工（1986–）**：1986 以访问副教授入职，同年任助理教授；1992 副教授、1996 正教授；2000 Dick and Barbara Dickinson 讲席教授、2017 Linus Pauling 讲席教授；2013 任 Rosen 生物工程中心主任。
6. **定向演化（1993 奠基）**：对枯草杆菌蛋白酶 E 做四轮易错 PCR 突变 + 筛选，得到在有机溶剂 DMF 中活性 **256 倍**的酶——"选择"代替"设计"，进化工程学从此诞生。**注意：她并非第一个把定向演化用于酶的人（页面明示 see e.g. Barry Hall），她的奠基性在于系统性方法与范式确立**。
7. **方法学扩展**：耐高低温酶、细胞色素 P450 催化环丙烷化与 carbene/nitrene 转移反应（天然酶没有的功能）、SCHEMA 计算法预测蛋白质嵌合体、生物合成通路共演化（异丁醇/NADH 改造）。
8. **绿色能源与生物制造**：实验室持续研究环境友好化学合成与替代能源——纤维素酶、微生物把生物质转化为燃料与化学品。
9. **创业与产业**：40 余项美国专利共同发明人；2005 共同创办 Gevo（可再生燃料）；2013 与两位昔日学生 Peter Meinhold、Pedro Coelho 创办 Provivi（农药替代）；2016 起 Illumina 董事；2019 入 Alphabet 董事会（Google 母公司**第三位女性董事**——页面明载）。
10. **三院院士第一女性**：美国国家工程院（2000）、国家医学院（2004）、国家科学院（2008）——**史上首位当选全部三个国家学院的美国女性**（页面明载 "first woman to be elected to all three National Academies"）。
11. **奖项全线**：Draper Prize（2011，**首位女性**）、国家技术创新奖章（2011）、国家发明家名人堂（2014）、千禧技术奖（2016，**首位女性**）、Sackler 奖（2017）、Garvan–Olin（2005）等。
12. **2018 诺贝尔化学奖**：独享**一半**奖金，官方理由 "for the directed evolution of enzymes"；另一半由 George P. Smith 与 Greg Winter 共享（噬菌体展示）。她是 117 年化学诺奖史上**第五位**女性得主、**首位美国女性**；也是普林斯顿本科毕业生中首位自然科学类诺奖得主。
13. **越过风暴**：2005 罹患乳腺癌治疗 18 个月；家庭多次变故（Lange 2010 自杀、William 2016 意外离世、父 2015 去世）；2019 年一篇 *Science* 论文（与 Inha Cho、Zhi-Jun Jia）因结果不可重复于 2020-01-02 撤稿——她公开坦诚，倡导科学诚实；2021 出任拜登总统 PCAST 外部共同主席；2025 获 ACS Priestley Medal。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绯红 deepcrimson） | `#8A1E2D` | 热烈而坚韧——演化迭代的红与工程胆识（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（定向演化 badgeDirEvo） | `#2E7FA8` | 蓝突变-筛选迭代环 |
| 分类色 2（酶与生物催化 badgeEnzyme） | `#1B7A43` | 绿新功能酶 / P450 |
| 分类色 3（工程与能源 badgeEnergy） | `#D97B29` | 琥珀太阳能 / 可再生燃料 |
| 分类色 4（女性先驱 badgePioneer） | `#C0395B` | 玫瑰三院院士 / 千禧奖第一女性 |
| 背景 | `#F9F5F5` | 微暖浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「定向演化的迭代轮次」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（文件 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`；不复制 wav 文件）
- **风格**：戏剧性、有力而宏大的史诗电子乐
- **匹配理由**：
  - "最后的希望" 契合其叙事内核——理性设计走入死路时，是"让进化替工程师工作"提供了新的出路
  - "有力而宏大" 匹配其人——工程学的一往无前 + 历经病痛与丧亲后依然站在科学诚信与公共政策前沿（PCAST）
  - 尾段上扬对应 2018 年独享诺奖一半的历史时刻
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 进化的工程师 / Frances Arnold 1956– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/领域/荣誉）
03  阿诺德的一生 — 时间线（10 节点：1956→1974→1979→1985→1986→1993→2005→2016→2018→2021）
04  早年：匹兹堡的独立少女 (1956–1979) — 表格「时间|事件|结果」
05  伯克利转身 (1979–1986) — 表格「时间|事件|结果」
06  定向演化奠基 (1993) — 表格「问题|方法|结果」+ 公式框：突变—筛选—迭代（subtilisin E，DMF，256×）
07  方法学扩展 — 表格「目标|策略|成果」（耐温酶/P450/SCHEMA/通路共演化）
08  绿色能源与创业 — 表格「公司|方向|创立」（Gevo/Provivi/Alphabet/Illumina）
09  荣誉全线 — 高斯式「类别|代表|意义」表格（三院院士第一女性 / Draper·千禧奖第一女性）
10  2018 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框：官方理由英文原句（"for the directed evolution of enzymes"）+ 另一半 Smith/Winter 说明
11  家庭与风暴 — 轻叙事页（癌症/丧亲/撤稿与科学诚信——克制、事实化）
12  公共服务 — PCAST 共同主席（2021，Biden）/ 教皇科学院（2019）
13  遗产：进化工程改变化学 — 四分类遗产盒
14  结尾 — 「不必设计完美，只需学会选择。」（自撰收束句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖份额 | 2018 **独享一半**（1/2）；另一半由 George P. Smith 与 Greg Winter 共享——勿写成"三人平分"或"独享全部" |
| 官方理由 | 她的半句是 "for the directed evolution of enzymes"；Smith/Winter 的半句是 "for the phage display of peptides and antibodies"——两句勿混 |
| "首位美国女性" | 页面原文 "the fifth woman to receive the award in its 117 years of existence, and the first American woman"——"第五位女性/首位美国女性"**页面明载可写**；"首位获化学诺奖的美国女性"同样成立 |
| "第一位"限语 | Draper Prize、Millennium Technology Prize 均为"首位女性得主"；三院院士"首位女性"——这些断言页面明载；其余"第一次/唯一"类断言严禁引申 |
| 非"第一个"做定向演化 | 页面明示 "not the first person to do so, see e.g. Barry Hall"——表述为"奠基系统性方法/确立范式"，勿写"发明定向演化" |
| 父子同名 | 父 William Howard Arnold（核物理学家）与祖父 William Howard Arnold（陆军中将）同名——叙述必须标明身份层级，禁止混同 |
| 丈夫姓名 | 结婚对象 James E. Bailey（页面称 Jay Bailey）；infobox Spouse 栏只写 Jay Bailey——DB 用 James E. Bailey 并注 Jay Bailey |
| Lange 关系 | 与 Andrew E. Lange 是 common-law marriage（事实婚姻 1994–2010）——infobox 列 Domestic partner；表述须用"事实婚姻"勿只写"丈夫" |
| National Medal 年份 | 正文荣誉清单作 2011，infobox 奖项栏作 2013——正文页用 **2011** 并加注 infobox 口径 |
| 撤稿事件 | 2019 Science 论文 2020-01-02 撤稿（不可重复）——如实、克制叙述，可用作科学诚信叙事素材；合作者 Inha Cho/Zhi-Jun Jia 不入关系库 |
| 政治表述 | PCAST/Alphabet 为实载职务可写；越战抗议为个人经历实载可轻写；不做政治评价与立场渲染 |
| 学生入库 | infobox Doctoral students 仅 **Christopher Voigt、Huimin Zhao**；Meinhold/Coelho 为正文明载的"昔日学生"（Provivi 共同创办）——四人均可入库；metadata 另有 Jesse D. Bloom、D. Allan Drummond（**metadata-only 禁入库**） |
| 引语 | "We have to reestablish the importance of science in policymaking..." 与 "[mechanical engineering] was the easiest option..." 均为页面原文引语，可整句引用并标注场合；其余无原文一律转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q4273363 | ✅ |
| name_zh | 弗朗西丝·阿诺德 | ✅ |
| name_en | Frances Arnold | ✅ |
| birth_date | 1956-07-25 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| gender | female | ✅ |
| primary_occupation | chemical engineer | ✅ |
| field_of_work | chemical engineering（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | directed evolution | 定向演化 |
| 1 | protein engineering | 蛋白质工程 |
| 2 | biocatalysis | 生物催化 |
| 3 | chemical engineering | 化学工程 |
| 4 | bioengineering | 生物工程 |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 家庭**（★红线：只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Harvey W. Blanch | 师→生（博士导师） | UC Berkeley 化学工程博士（1985），亲和层析 |
| advisor-student | Christopher Voigt | 生 | infobox 博士生 |
| advisor-student | Huimin Zhao | 生 | infobox 博士生 |
| advisor-student | Peter Meinhold | 生 | 昔日学生，2013 共同创办 Provivi |
| advisor-student | Pedro Coelho | 生 | 昔日学生，2013 共同创办 Provivi |
| co-honored | George P. Smith | 无向 | 2018 诺贝尔化学奖（另一半共享者，噬菌体展示） |
| co-honored | Greg Winter | 无向 | 2018 诺贝尔化学奖（另一半共享者，噬菌体展示；规范名 "Greg Winter"，与下一批 Winter 篇互指一致） |
| spouse | James E. Bailey | 无向 | 1987–1991 婚（2001 去世；页面称 Jay Bailey） |
| spouse | Andrew E. Lange | 无向 | 1994–2010 事实婚姻（common-law；infobox Domestic partner） |

> **禁入库名单**（metadata-only 或非学术关系）：Jesse D. Bloom、D. Allan Drummond（metadata.json doctoral_student 有载、正文 infobox 无——**禁入库**）；Robert Socolow（普林斯顿能源中心负责人，非导师）；Barry Hall（正文仅作先例提及）；Maria Zuber / Francis Collins（PCAST 同僚）；Sean Bailey（继子，非学术）；Inha Cho / Zhi-Jun Jia（撤稿论文合作者）；父与祖父 William Howard Arnold（同名家族成员，非学术关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2018，独享一半；第五位女性得主、首位美国女性）
- Garvan–Olin Medal，ACS（2005）
- FASEB Excellence in Science Award（2007）
- Enzyme Engineering Award（2007）
- Charles Stark Draper Prize，NAE（2011，首位女性）
- National Medal of Technology and Innovation（2011）
- National Inventors Hall of Fame（2014）
- Millennium Technology Prize（2016，首位女性）
- Raymond and Beverly Sackler Prize in Convergence Research，NAS（2017）
- Nobel 前荣誉：NAE（2000）/NAM（2004）/NAS（2008）三院院士（首位女性全三院）
- American Philosophical Society（2018）；Royal Academy of Engineering International Fellow（2018）
- Foreign Member of the Royal Society（2020）
- Perkin Medal（2023）；Oxford honorary DSc（2023）；ACS Priestley Medal（2025）
- Pontifical Academy of Sciences，教皇科学院（2019，Pope Francis 任命）
- BBC 100 Women（2018）

## 9. 机构清单

- 教育：Taylor Allderdice High School（1974）；Princeton University（BS 1979 机械与航空航天工程）；UC Berkeley（MS、PhD 1985 化学工程，Blanch 实验室）
- 任职：Solar Energy Research Institute（今 NREL）；UC Berkeley 博士后（生物物理化学）；Caltech（1986 访问副教授→助理教授；1992 副教授；1996 正教授；2000 Dickinson 讲席；2017 Linus Pauling 讲席；2013 Rosen 生物工程中心主任）
- 产业与公益：Gevo（2005 共同创办）；Provivi（2013 共同创办）；Illumina 董事（2016–）；Alphabet 董事（2019–，第三位女性董事）；Angeleno Group 顾问委员会；Packard Fellowship 顾问团主席；PCAST 外部共同主席（2021–）

## 10. 终审清单

- [ ] 生卒 1956-07-25 / 在世留白；出生地 Edgewood, PA
- [ ] 2018 独享一半；官方理由 "for the directed evolution of enzymes"；另一半 Smith/Winter 口径不混
- [ ] "第五位女性/首位美国女性/三院院士首位女性/Draper·千禧奖首位女性"均页面明载
- [ ] "非第一个做定向演化（Barry Hall 先例）"限语保留
- [ ] 父子同名区分；丈夫 James E. Bailey（Jay Bailey）；Lange 事实婚姻表述准确
- [ ] National Medal 2011（正文口径）+ infobox 2013 注记
- [ ] 学生入库四人（Voigt/Zhao/Meinhold/Coelho）；Bloom/Drummond 禁入库
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Frances_Arnold/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（2021 年照片；失败用装饰圆）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：PCAST 引语与普林斯顿 interview 引语可整句引用；其余一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
