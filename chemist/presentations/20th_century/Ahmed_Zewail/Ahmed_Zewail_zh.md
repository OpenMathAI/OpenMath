# Ahmed Zewail（艾哈迈德·泽维尔）立传提示词

> qid=Q106624 · 1946-02-26 – 2016-08-02 · 埃及 / 美国 · 诺贝尔化学奖（1999，独享）· 埃及裔美国化学家、"飞秒化学之父"
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Ahmed_Zewail/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注——用 `images.txt` 中的 `Ahmed_Zewail_(2010).jpg`（2010 年照片，真实肖像），下载 250px→500px；`Ahmed_Zewail_1986.png` 可作正文插图页素材。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{camera}\enspace 用飞秒快门看化学键\enspace·\enspace 埃及·美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（含阿拉伯文 أَحْمَد حَسَن زُوَيْل，需配置专用字体族渲染）、国籍、出生地/去世地/安葬地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「飞秒快门」母题——激光脉冲的等时间隔圆点序列。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如 1 fs = 10⁻¹⁵ s；过渡态观测语义框）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ahmed Hassan Zewail（阿拉伯文：أَحْمَد حَسَن زُوَيْل；中文惯称：艾哈迈德·哈桑·泽维尔；头衔 ON、OME——埃及尼罗河勋章与一级功绩勋章）
- **生卒**：1946-02-26 生于埃及 Damanhur（在 Desouk 长大）→ 2016-08-02 逝于美国加州 Pasadena，享年 70；安葬于埃及吉萨 6th of October 城
- **国籍**：Egypt（埃及）；1982-03-05 入籍美国（正文口径）——Egypt + United States 双重
- **身份**：化学家、"飞秒化学之父"（father of femtochemistry）；加州理工学院化学与物理学教授——**首位** Linus Pauling 化学物理讲席教授（页面口径）；超快科学技术物理生物学中心主任
- **家庭**：1967 年（赴美读博前夕）与首任妻子 Mervat 结婚，育有二女 Maha、Amani，1979 年分居；1989 年娶 Dema Faham（叙利亚人），育有二子 Nabeel、Hani
- **教育轨迹**：
  - Alexandria University：化学 BS、MS
  - University of Pennsylvania：PhD（1975），论文 *Optical and magnetic resonance spectra of triplet excitons and localized states in molecular crystals*
- **导师**：Robin M. Hochstrasser（宾大博士导师）
- **博士后**：UC Berkeley，师从 Charles B. Harris
- **研究领域**：飞秒化学（femtochemistry）、超快激光光谱、超快电子衍射

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **尼罗河三角洲的少年（1946）**：生于 Damanhur、长于 Desouk——亚历山大大学的化学学士与硕士起步。
2. **跨洋读博（1967–1975）**：1967 年赴宾夕法尼亚大学，随 **Robin M. Hochstrasser** 研究分子晶体中三重态激子的光学与磁共振谱，1975 年获博士。
3. **伯克利博士后（1975–1976）**：随 **Charles B. Harris** 做博士后研究——此后的一年把他送上加州理工的讲台。
4. **Caltech（1976）**：获加州理工学院教职，此后终老于此；成为**首位** Linus Pauling 化学物理讲席教授（页面口径），并任超快科学技术物理生物学中心主任。
5. **飞秒快门**：飞秒化学——用**超短激光脉冲**（ultrashort laser flashes）研究飞秒（10⁻¹⁵ 秒）时间尺度上的化学反应，短到足以分析选定反应中的**过渡态**（transition states）。
6. **过渡态的实况转播**：化学键断裂与重组的瞬间第一次可以被"看到"——飞秒时间分辨把反应动力学从推测变成测量（措辞基于页面 "allows the description of reactions on very short time scales"）。
7. **超快电子衍射**：除激光外还有关键贡献——以**短电子脉冲**（而非光脉冲）研究化学反应动力学的超快电子衍射（ultrafast electron diffraction）。
8. **1982 双节点**：1982-03-05 入籍美国；同年当选美国物理学会 Fellow。
9. **科学界的级联荣誉**：Humboldt（1983）→ King Faisal（1989）→ Wolf 化学奖（1993）→ Debye 奖（1996）→ Tolman / E. Bright Wilson / Welch / Pauling Medal（1997）→ Franklin Medal / E. O. Lawrence 奖（1998）——诺奖前夜的密集承认。
10. **1999 诺贝尔化学奖（独享）**：表彰其在飞秒化学上的工作；诺奖演讲 "Femtochemistry: Atomic-Scale Dynamics of the Chemical Bond Using Ultrafast Lasers"。页面口径：**首位**获科学类诺贝尔奖的埃及人与阿拉伯人、**首位**获诺贝尔化学奖的非洲人——使用时注明页面口径。
11. **尼罗河大十字勋章（1999）**：获埃及最高国家荣誉 Grand Collar of the Order of the Nile（页面口径 "Egypt's highest state honour"）。
12. **科学外交（2010）**：2010 年 1 月与 Elias Zerhouni、Bruce Alberts 成为**首批**美国对穆斯林世界的科学特使（Science Envoy，页面口径），走访北非至东南亚——本页克制呈现科学外交事实，政治细节从略。
13. **Zewail City 与身后**：以他命名的 Zewail City of Science and Technology（2000 年设立、2011 年复兴；页面 See also 节称其捐出全部诺奖奖金创办，行文须注明该口径出处）；2005 年 ACS 设 Ahmed Zewail Award for Ultrafast Science and Technology；2016-08-02 病逝 Pasadena，8 月 7 日于开罗举行军葬（出席者名单从略，仅载事实）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫罗兰 royalviolet） | `#5B2A86` | 尼罗河暮色中的紫罗兰（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（飞秒化学 badgeFemto） | `#8A1E2D` | 绛红飞秒化学 / 过渡态 |
| 分类色 2（激光光谱 badgeLaser） | `#2F5D8A` | 深蓝超快激光 / 光谱 |
| 分类色 3（电子衍射 badgeUED） | `#3E6B4A` | 绿超快电子衍射 |
| 分类色 4（埃及荣光 badgeEgypt） | `#B4762E` | 琥珀尼罗河勋章 / Zewail City |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），等距脉冲序列呼应飞秒快门。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（清单指定文件 `17-_DA0mdtL-jI-Nostalgy...wav`；如目录内尚无软链则从 music_audio 软链，不要复制 wav）
- **风格**：怀旧 / 抒情 / 电影感
- **匹配理由**：
  - 怀旧气质匹配其双重人生——尼罗河三角洲的起点与加州理工的终点、身后归葬故土
  - 抒情旋律匹配"给化学反应按下快门"的诗意科学
  - 电影感匹配从亚历山大到斯德哥尔摩的完整叙事弧线
- **时长**：以曲目实际时长为准（> 15 页 × 7 秒即由 ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 用飞秒快门看化学键 / Ahmed Zewail 1946–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名含阿拉伯文/国籍/教育/博士/师承/出生地/去世地/安葬地/领域/荣誉）
03  泽维尔的一生 — 高斯式时间线（10 节点：1946→1967→1975→1976→1982→1993→1998→1999→2010→2016）
04  亚历山大与宾大 (1946–1975) — 表格「时间|事件|结果」
05  伯克利与 Caltech (1975–1982) — 表格「人物|转折|结果」（Harris 博后 / 1976 教职 / Pauling 讲席）
06  飞秒化学：快门原理 — 表格「问题|方法|结果」+ 公式框：1 fs = 10⁻¹⁵ s / 过渡态观测
07  超快电子衍射 — 表格「挑战|方法|结果」（电子脉冲替代光脉冲）
08  诺奖前夜的荣誉级联 (1983–1998) — 表格「年份|奖项|意义」
09  1999 诺贝尔化学奖（独享） — 表格「得主|贡献|份额」+ 诺奖演讲标题页
10  埃及的荣光 — 表格「荣誉|年份|意义」（尼罗河大十字勋章 1999 / Order of Merit 1995）
11  科学外交与 Zewail City — 高斯 FFT 页式流程图（2010 科学特使 → Zewail City 2000/2011 → 以名命名奖）
12  学术殿堂 — 高斯式「机构|身份|年份」表格（NAS 1989 / AAAS 1993 / APS 1998 / ForMemRS 2001 / 瑞典皇家科学院外籍）
13  遗产：四维的化学 — 四分类遗产盒 + 荣誉博士学位列举（1991 牛津起至 2014 耶鲁，精选数条）
14  结尾 — 「化学键的一生，快过一次心跳；他让它定格。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1999 独享 | 1999 化学奖**独享**（无共同得主）——勿加 co-honored 关系 |
| "首次"口径 | "首位获科学诺奖的埃及人与阿拉伯人 / 首位化学诺奖的非洲人"为**页面明载**口径——可用但注明页面口径；其余"第一次/唯一"断言一律禁止 |
| 获奖理由 | 页面表述为 "for his work on femtochemistry"——勿改写成官方全句（本地页面无载） |
| 双导师 | 博士导师 Hochstrasser（宾大，1975）；博士后导师 Charles B. Harris（伯克利）——两个方向均入库 advisor-student，note 区分博士/博士后 |
| 国籍写法 | Egypt + United States（1982-03-05 入籍，页面明载日期）；infobox 作 Citizenship——行文"埃及裔美国化学家" |
| 政治内容 | 科学特使（2010）、PCAST 与 2011 埃及事件等为页面实载——**克制呈现**：只保留科学外交事实一行，避免展开政治叙事与人物评价；其原话 "I am a frank man..."（页面直引）如使用须逐字核对且仅用于表达"无意从政"的语境 |
| See also 口径 | "捐出全部诺奖奖金创办 Zewail City"出自页面 **See also 节**（非正文）——行文引用时注明口径，或改用正文实载的"2000 年设立、2011 年复兴、以他命名" |
| 死因口径 | 2016-08-02 晨间病逝，"正在癌症康复期，确切死因不明"（页面口径 "the exact cause of his death is unknown"）——勿写确定死因 |
| 军葬出席者 | 页面列有大量政要与宗教人士——**从略处理**，仅载"2016-08-07 于开罗 El-Mosheer Tantawy 清真寺军葬"事实 |
| 妻子两条 | Mervat（1967 结婚、1979 分居、二女 Maha/Amani）与 Dema Faham（1989 结婚、二子 Nabeel/Hani）——两行 spouse，勿合并勿混淆 |
| 阿拉伯文名 | أَحْمَد حَسَن زُوَيْل 需专用字体族（参考希伯来文 \newfontfamily 先例），编译前验证字形 |
| 引语 | 仅页面直引（"I am a frank man..."段）可用；诺奖演讲标题为实载标题非引语；其余全部间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106624 | ✅ |
| name_zh | 艾哈迈德·泽维尔 | ✅ |
| name_en | Ahmed Zewail | ✅ |
| birth_date | 1946-02-26 | ✅ |
| death_date | 2016-08-02 | ✅ |
| nationality | Egypt / United States（两条带 rank） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：femtochemistry / ultrafast science / ultrafast electron diffraction / physical biology，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robin M. Hochstrasser | 师→生（博士导师） | 宾大博士（1975），三重态激子光谱 |
| advisor-student | Charles B. Harris | 师→生（博士后） | UC Berkeley 博士后导师 |
| spouse | Mervat | 无向 | 1967 结婚；1979 分居；二女 Maha、Amani |
| spouse | Dema Faham | 无向 | 1989 结婚；二子 Nabeel、Hani（页面明载为叙利亚人） |

> 禁入库名单：子女 Maha/Amani/Nabeel/Hani（未具名学术身份，家庭亲属不入库）；Obama/PCAST/Science Envoy 同僚（Zerhouni、Alberts）与 2011 埃及政治人物（Nour、ElBaradei 等）——政治敏感与噪声防护，**一律不入库**；军葬出席者全部不入库。1999 独享诺奖，无 co-honored。relations=4 为诚实值。

## 8. 奖项清单

- Alexander von Humboldt Senior Scientist Award（1983）
- King Faisal International Prize for Science（1989）
- Wolf Prize in Chemistry（1993）
- Earle K. Plyler Prize（1993）
- Herbert P. Broida Prize（1995）
- Grand Cross of the Order of Merit, Egypt（1995）
- Peter Debye Award（1996）
- Tolman Award / E. Bright Wilson Award in Spectroscopy / Robert A. Welch Award / Linus Pauling Medal（1997）
- Grand Cordon of the Order of the Arab Republic of Egypt（1998）
- E. O. Lawrence Award / Franklin Medal / Paul Karrer Gold Medal（1998）
- **Nobel Prize in Chemistry（1999，独享）**
- Grand Collar of the Order of the Nile（1999，埃及最高国家荣誉——页面口径）
- Golden Plate Award（2000）
- ForMemRS / Fellow of the African Academy of Sciences（2001）
- Albert Einstein World Award of Science（2006，颁奖理由页面有直引——如使用须逐字核对）
- Othmer Gold Medal（2009）
- Priestley Medal / Davy Medal（2011）
- 外国勋章：法国荣誉军团骑士 / 法国国家功勋军官 / 黎巴嫩雪松大绶 / 苏丹双尼罗大军官 / 突尼斯共和国指挥官 / 阿联酋扎耶德大军官（年份多数页面未载，勿写）
- 院士：APS Fellow（1982）/ NAS（1989）/ AAAS（1993）/ American Philosophical Society（1998）/ ForMemRS（2001）/ 瑞典皇家科学院外籍成员

## 9. 机构清单

- 教育：Alexandria University（BS、MS）；University of Pennsylvania（1975 PhD）
- 任职：UC Berkeley 博士后（Harris 组，1975–1976）；California Institute of Technology（1976–2016；首位 Linus Pauling 化学物理讲席教授；Physical Biology Center for Ultrafast Science and Technology 主任）
- 关联机构（infobox）：UC Berkeley / Caltech / Zewail City of Science, Technology and Innovation / Tohoku University
- 纪念：Zewail City of Science and Technology（2000 设立、2011 复兴，以他命名）；Ahmed Zewail Award for Ultrafast Science and Technology（2005，ACS 与 Newport Corporation 设立）；Ahmed Zewail Prize in Molecular Sciences（2010，Chemical Physics Letters 设立）

## 10. 终审清单

- [ ] 生卒 1946-02-26 / 2016-08-02，享年 70，出生地 Damanhur、去世地 Pasadena、安葬地吉萨 6th of October 城
- [ ] 1999 独享表述准确；获奖理由按页面口径（femtochemistry）
- [ ] "首位/第一次"断言全部注明页面口径
- [ ] 博士/博士后双导师区分准确；配偶两行不混
- [ ] 政治内容克制呈现（科学外交一行）；死因按"不明"口径
- [ ] 阿拉伯文名字形编译通过
- [ ] 直引原话逐字核对；其余间接转述
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ahmed_Zewail/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`Ahmed_Zewail_(2010).jpg` 已就位（250px→500px）
- [ ] **国籍**：封面顶部明示"埃及·美国"
- [ ] **引语核对**：仅"I am a frank man..."段为页面直引，逐字核对
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
