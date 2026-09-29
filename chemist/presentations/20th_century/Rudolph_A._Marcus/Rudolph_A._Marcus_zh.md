# Rudolph A. Marcus（鲁道夫·马库斯）立传提示词

> qid=Q239067 · 1923-07-21 – 2026-07-16 · 加拿大裔美国化学家 · 20 世纪 · 诺贝尔化学奖（1992，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Rudolph_A._Marcus/`（page.md + metadata.json）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像用 Wikipedia "Marcus in 2005"（Prof. Dr. Rudolph A. Marcus (cropped).jpg）；下载失败用装饰圆占位并如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace电子转移的定律\enspace·\enspace 加拿大 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（Rudolph Arthur Marcus）、国籍（加拿大出生→1958 入籍美国）、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「电子跃迁 / 能垒曲线」母题——离散圆点如电子从给体跃向受体。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Marcus 理论框架：$\Delta G^\ddagger = \frac{(\Delta G^\circ + \lambda)^2}{4\lambda}$（活化能与重组能 λ、驱动力 ΔG° 的抛物线关系；λ=内层+外层重组能）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Rudolph Arthur Marcus（惯称 Rudolph A. Marcus / "Rudy"；中文惯称：鲁道夫·马库斯）
- **生卒**：1923-07-21 生于加拿大魁北克省蒙特利尔 → 2026-07-16 逝于美国加州帕萨迪纳（Pasadena）家中，享年 102（距 103 岁生日差 5 天）
- **国籍**：加拿大出生；1958 年入籍美国（metadata 双国籍 Canada / United States）
- **身份**：理论化学家；加州理工学院（Caltech）教授，兼新加坡南洋理工大学教授；国际量子分子科学院院士
- **家庭**：父 Myer Marcus（生于纽约）、母 Esther（娘家姓 Cohen，生于英格兰）；家族源自俄国帝国治下的立陶宛 Ukmergė；犹太家庭，童年在蒙特利尔犹太街区度过，也曾在底特律生活过一段
- **配偶与子女**：1949 年娶 Laura Hearne，2003 年妻先逝；育有 3 个子女
- **教育轨迹**：Baron Byng High School（数学出众）→ McGill University
- **博士**：1946 年 McGill；导师 Carl A. Winkler（Winkler 曾在牛津师从 Cyril Hinshelwood）；论文《Studies on the conversion of PHX to AcAn》；在 McGill 修的数学课比一般化学生多得多——日后创立电子转移理论的数学本钱
- **研究领域**：化学（理论）——电子转移理论（Marcus 理论）、RRKM 单分子反应理论、化学反应动力学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **蒙特利尔的数学少年（1923）**：立陶宛犹太移民家庭，Baron Byng 高中数学拔尖；童年在蒙特利尔与底特律之间穿梭。
2. **McGill 的数学本钱（1940s）**：在 Carl A. Winkler 门下读化学，修的数学课远超一般化学学生——多年后这成为创立电子转移理论的全部家底。
3. **B.Sc.（1943）与 Ph.D.（1946）**：二战期间完成本硕学业，1946 年以 PHX→AcAn 转化研究获博士学位。
4. **博士后两站（1946–）**：先在加拿大国家研究委员会（NRC），后赴北卡罗来纳大学教堂山分校。
5. **RRKM 理论（1952）**：在北卡把 RRK 理论与过渡态理论结合，发展出 Rice–Ramsperger–Kassel–Marcus（RRKM）单分子反应理论——动力学教科书的标准章节。
6. **布鲁克林的第一个教职**：Polytechnic Institute of Brooklyn——在纽约的开始。
7. **1950 年代的悖论**：化学家们惊讶于 Fe²⁺/Fe³⁺ 这样"简单"的电子交换反应为何**极慢**——正是这个悖论把马库斯引进了电子转移的世界。
8. **Marcus 理论（1956 起）**：为外层球单电子转移建立热力学与动力学框架——活化能与驱动力、重组能 λ 的抛物线关系；预言"反转区"（inverted region）；以二价/三价铁离子水溶液交换为核心范式。
9. **从伊利诺伊到加州理工（1964 / 1978）**：1964 年执教伊利诺伊大学；1978 年移师加州理工学院，直至百岁仍活跃。
10. **无处不在的电子转移**：呼吸作用与光合作用都靠电子转移——2 H⁺ + 2 e⁻ + ½ O₂ → H₂O + heat；Marcus 理论由此渗透化学与生物化学的每个角落。
11. **"go full tilt" 的解题法**：自述解决问题要"全力以赴"——要么解到答案，要么决定暂时搁置（Veery Journal 访谈语境）。
12. **诺奖前夜的大满贯**：Irving Langmuir 奖（1978）、Wolf 化学奖（1985）、Centenary 奖（1988/89）、Willard Gibbs 奖与 Peter Debye 奖（1988）、国家科学奖章（1989）——1992 年诺贝尔化学奖 "for his contributions to the theory of electron transfer reactions in chemical systems"。
13. **百岁科学家（2023）**：百岁生日时仍在做研究；2026-07-16 于帕萨迪纳家中去世，距 103 岁生日差 5 天——诺奖得主中的罕见长寿纪录。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫藤深紫 deepviolet） | `#46356B` | 电子在能垒间穿行的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Marcus 理论 badgeMarcus） | `#2E5A9E` | 蓝电子转移 / 重组能 λ |
| 分类色 2（RRKM badgeRRKM） | `#1B7A43` | 绿单分子反应 / 过渡态理论 |
| 分类色 3（生命中的电子 badgeLife） | `#B0413E` | 绯红呼吸 / 光合作用 |
| 分类色 4（百年科学生涯 badgeCentury） | `#D97B29` | 琥珀102 岁的实验室 / 大满贯奖项 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「电子自给体向受体的量子跃迁」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（文件：`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`；不要复制 wav 文件）
- **风格**：开阔宣言 / 新大陆气象 / 长线铺陈
- **匹配理由**：
  - "新大陆" 直指 Marcus 理论——在化学动力学版图上开辟一整块前人未至的疆域
  - "长线铺陈" 匹配其生涯——1956 年提出理论，等了几十年才被实验全面证实并获奖，一条定理走完一个世纪
  - "开阔" 匹配其绵延——从蒙特利尔到布鲁克林、厄巴纳、帕萨迪纳，百岁仍在新 lands 上行走
- **时长**：以曲文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 电子转移的定律 / Rudolph A. Marcus 1923–2026 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍变迁/教育/博士导师/配偶子女/出生地/去世地/领域/荣誉）
03  马库斯的一生 — Sanger 式时间线（10 节点：1923→1943→1946→1952→1956→1958→1964→1978→1992→2026）
04  早年：蒙特利尔的数学少年 (1923–1940) — 表格「时间|事件|结果」
05  McGill 与两站博士后 (1940–1950) — 表格「站点|课题|结果」（Winkler / NRC / 北卡）
06  RRKM 理论 (1952) — 表格「问题|方法|结果」+ 公式框：RRK + 过渡态理论 → RRKM
07  电子转移的悖论 (1950s) — 表格「现象|困惑|切入」+ 公式框：Fe²⁺ + Fe³⁺ 交换反应为何慢
08  Marcus 理论 — 表格「要素|内容|地位」+ 公式框：ΔG‡ = (ΔG°+λ)²/4λ（含反转区预言）
09  生命中的电子转移 — 表格「过程|电子转移角色|意义」+ 公式框：2H⁺ + 2e⁻ + ½O₂ → H₂O + heat
10  1992 诺贝尔化学奖 — 独享；官方理由 "for his contributions to the theory of electron transfer reactions in chemical systems"
11  学术迁徙地图 — 表格「时间|机构|身份」（Montreal→Brooklyn→Urbana→Pasadena；Oxford 1975–76 讲席研究员）
12  荣誉与学会 — Sanger 式「类别|代表|意义」表格（Langmuir 1978 / Wolf 1985 / NMS 1989 / Nobel 1992 / ForMemRS 1987 / NAS 1970 / AAAS 1973 / APS 1990）
13  遗产：一个理论的一百年 — 四分类遗产盒（电化学 / 光合作用与呼吸 / 太阳能转换 / 动力学教科书）+ 百岁科学家注记
14  结尾 — 「一条公式，等了半个世纪，等来全世界的实验。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1992 诺奖口径 | **独享**，官方理由 "for his contributions to the theory of electron transfer reactions in chemical systems"——勿写"发明电子转移"（理论是 his contributions to the theory）；勿写共享 |
| 生卒 | 1923-07-21 蒙特利尔 → **2026-07-16 帕萨迪纳**家中，享年 102（距 103 岁生日差 5 天）——卒日与"五天之差"两处口径必须一致；勿写"103 岁" |
| 国籍变迁 | 加拿大出生 → **1958 年入籍美国**（infobox/正文）；封面与身份页写 "加拿大 / 美国" 双口径 |
| 与 Taube 的关系 | 页面 See also 提到 Henry Taube（1983 诺奖，电子转移机理）——**仅为参见条目，两人无师承/合作记载，禁建关系**；正文可比照提及但注明"同期同域" |
| Winkler 师承 | 博士导师 Carl A. Winkler（McGill）；Winkler 曾师从牛津的 **Cyril Hinshelwood**——Hinshelwood 是"导师的导师"，**禁建关系** |
| RRKM 年份 | **1952 年在北卡**发展（结合 RRK 与过渡态理论）——勿写成博士论文成果（博士论文是 PHX→AcAn） |
| Marcus 理论提出时间 | 页面导语未给具体年份；叙事亮点标 "1956 起" 须核对页面——页面只说 1950s 开始研究电子转移、二价/三价铁离子交换是其起点；Beamer 时间线节点以"1950s"或"1956 起"之一并加"据页面口径"注记，不得虚构精确日 |
| 反转区 | "预言反转区"为 Marcus 理论常识且与本页抛物线关系自洽——但**本页面未明载"反转区"字样**；如写，须标注为理论内容注记而非页面陈述，或直接省略 |
| 家庭 | 1949 娶 Laura Hearne（2003 妻先逝）；3 子女（页面未具名）——勿编造子女姓名 |
| 博士生 | infobox Doctoral students 仅 **Gregory A. Voth**；metadata doctoral_student（Donald W. Noid、Nathan Hodas、Robert J. Cave）页面无载——**禁入**；postdoc Ramakrishna Ramaswamy 页面明载（Other notable students 注明 postdoc）——以 colleague 类型入库 |
| "go full tilt" | 出自 Veery Journal 访谈语境（页面：he said echoing his interviewer）——引用时注明是访谈转述，勿写成论文原文 |
| 荣誉年份 | Langmuir 1978 / Robinson Medal 1982 / Chandler Medal 1983 / Wolf 1985 / Centenary 1988-89 / Gibbs+Debye 1988 / NMS 1989 / Pauling+Remsen 1991 / Nobel 1992 / Hirschfelder Prize 1992-93——1988 年四奖并至勿串；ForMemRS **1987**、NAS 1970、AAAS 1973、APS 1990、英国皇家化学会荣誉会士 1991、加拿大皇家学会 1993 |
| 荣誉博士 | 页面列 19 个荣誉博士（芝加哥 1983 → 圣地亚哥智利 2018）——Beamer 取代表性 5-6 个，注明"共 19 个（页面清单）" |
| 引语红线 | 直接引语仅两处：①官方获奖理由句 ②"go full tilt"（注明访谈转述）；其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q239067 | ✅ |
| name_zh | 鲁道夫·马库斯 | ✅ |
| name_en | Rudolph A. Marcus | ✅ |
| birth_date | 1923-07-21 | ✅ |
| death_date | 2026-07-16 | ✅ |
| nationality | Canada（rank 0，出生）/ United States（rank 1，1958 入籍） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |
| has_biography | false（立传 Beamer 完成后置 1） | ✅ |

person_field 细分（rank 表）：

| field | rank | 说明 |
|---|---|---|
| theoretical chemistry | 0 | 页面 Fields=Chemistry（理论方向主导） |
| electron transfer | 1 | Marcus 理论 / 外层球电子转移 |
| reaction kinetics | 2 | RRKM / 单分子反应动力学 |
| biochemistry (electron transfer) | 3 | 呼吸与光合中的电子转移 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Carl A. Winkler | 师→生（博士导师） | McGill，1946 博士 |
| colleague | Ramakrishna Ramaswamy | 无向 | infobox Other notable students 明载（postdoc） |
| spouse | Laura Hearne | 无向 | 1949 结婚，2003 妻先逝 |
| advisor-student | Gregory A. Voth | Marcus→学生 | infobox Doctoral students 明载 |

> **禁入库名单**：Donald W. Noid、Nathan Hodas、Robert J. Cave（仅 metadata.json doctoral_student 有载，页面无载——**禁入**）；Cyril Hinshelwood（导师的导师，页面无本人直接关系记载——**禁建**）；Henry Taube（See also 参见条目，无师承/合作记载——**禁建**）；Caltech / NTU / NRC / UNC / Brooklyn Polytechnic / UIUC 等机构非人际。

## 8. 奖项清单

- Nobel Prize in Chemistry（1992，独享）
- Irving Langmuir Award in Chemical Physics（1978）
- Robinson Medal, Faraday Division, Royal Society of Chemistry（1982）
- Chandler Medal, Columbia University（1983）
- Wolf Prize in Chemistry（1985）
- Centenary Prize（1988/89）
- Willard Gibbs Award（1988）；Peter Debye Award（1988）
- National Medal of Science（1989）
- William Lloyd Evans Award, Ohio State（1990）；Theodore William Richards Medal, NESACS（1990）
- Linus Pauling Award（1991）；Remsen Award（1991）
- Hirschfelder Prize in Theoretical Chemistry（1992-93）
- Golden Plate Award, American Academy of Achievement（1993）
- Fray International Sustainability Award, FLOGEN Star Outreach（2019）
- 学会：NAS（1970）、AAAS（1973）、American Philosophical Society（1990）、皇家化学会荣誉会士（1991）、加拿大皇家学会（1993）、ForMemRS（1987）、美国物理学会 Fellow、国际量子分子科学院院士
- 荣誉博士：共 19 个（页面清单 1983–2018：芝加哥、哥德堡、布鲁克林理工、McGill、女王大学、UNB、牛津、北卡教堂山、横滨国立、UIUC、Technion、瓦伦西亚理工、西北、滑铁卢、南洋理工、Tumkur、海得拉巴、卡尔加里、圣地亚哥智利）

## 9. 机构清单

- 教育：Baron Byng High School（Montreal）、McGill University（B.Sc. 1943、Ph.D. 1946，导师 Carl A. Winkler）
- 任职：National Research Council Canada（1946– 博士后）、University of North Carolina（博士后；1952 在此发展 RRKM）、Polytechnic Institute of Brooklyn（第一个教职）、University of Illinois at Urbana-Champaign（1964–）、California Institute of Technology（1978–，百岁仍活跃）、University College Oxford（1975–76 教授研究员）、Nanyang Technological University（新加坡，兼职教授）

## 10. 终审清单

- [ ] 生卒 1923-07-21 / 2026-07-16，享年 102（距 103 岁生日差 5 天）；蒙特利尔 → 帕萨迪纳
- [ ] 1992 独享；获奖理由官方句准确
- [ ] 博士导师 Carl A. Winkler（McGill 1946）；RRKM=1952 北卡；两说年份注记
- [ ] Marcus 理论表述只写页面实载（外层球电子转移热力学+动力学框架、Fe²⁺/Fe³⁺ 起点）；"反转区"如写须加注记
- [ ] 国籍变迁 1958 入籍美国；双国籍口径统一
- [ ] Taube / Hinshelwood / metadata 三博士生禁入清单执行
- [ ] 荣誉年份逐项对照（1988 四奖勿串；ForMemRS 1987）
- [ ] 引语仅官方获奖理由句与 "go full tilt"（访谈转述），均可回溯
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Rudolph_A._Marcus/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：Wikipedia "Marcus in 2005" 肖像或装饰圆占位（如实标注）
- [ ] 国籍：封面顶部明示 加拿大 / 美国
- [ ] 引语核对：获奖理由句与 "go full tilt" 须在 page.md 原文找到
- [ ] 卒日复核：2026-07-16 与"距 103 岁生日差 5 天"口径一致
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本文件由 chem-batch-21 执行生成；`chemist/generate_20th_century_list.py` 状态列由主控统一收尾，本批次不改动。
