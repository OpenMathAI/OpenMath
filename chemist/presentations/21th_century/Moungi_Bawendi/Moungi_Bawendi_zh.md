# Moungi Bawendi（蒙吉·巴文迪）立传提示词

> qid=Q15433043 · 1961-03-15 生于巴黎（在世） · 美国化学家（法裔/突尼斯裔） · 21 世纪 · 诺贝尔化学奖（2023，与 Brus、Ekimov 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Moungi_Bawendi/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**对齐 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。`images.txt` 仅含突尼斯共和国勋章绶带图（不可作肖像）；infobox 有 "Bawendi in 2023" 实照——执行时经 Wikipedia REST API `page/summary` 查 infobox 原图名回退下载（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证），失败则用主色装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace` 量子点的化学工匠`\enspace·\enspace` 美国），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。国籍口径：美国化学家，法国出生、突尼斯裔——封面只写"美国"，血统放身份信息页。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Moungi Gabriel Bawendi）、国籍、出生地/教育、博士（双导师）、博士后、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「量子点」母题——大小错落的圆点即"尺寸决定颜色"的纳米晶粒。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——如 1993 热注入法三要素（前驱体注射温度 / 有机配体 / 尺寸分布）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Moungi Gabriel Bawendi（中文惯称：蒙吉·巴文迪）
- **生卒**：1961-03-15 生于法国巴黎（在世，页面无卒日）
- **国籍**：United States（美国；法国出生、突尼斯裔）
- **身份**：化学家（chemist）；MIT Lester Wolfe 教授；2023 诺贝尔化学奖三人共享得主之一
- **家庭**：父 Mohammed Salah Baouendi（突尼斯数学家，Purdue 数学系任职，故全家迁居美国印第安纳州 West Lafayette）；妻 Rachel Zimmerman（记者，MIT 计算机科学教授 Seth J. Teller 的遗孀）
- **教育轨迹**：
  - West Lafayette Junior-Senior High School（1978 毕业）
  - Harvard University：A.B.（1982）+ A.M.（1983）
  - University of Chicago：化学 PhD（1988），论文 From the Biggest to the Smallest Polyatomic Molecules: Statistical Mechanics and Quantum Mechanics in Action
- **导师**：双博士导师 Karl Freed（理论高分子物理）与 Takeshi Oka（H3+ hot-bands 实验，其谱线用于解读 1989 年木星观测发射光谱）
- **博士后**：Bell Labs，师从 Louis E. Brus（Oka 推荐其参加 Bell Labs 夏季项目时由 Brus 引入量子点研究）
- **研究领域**：量子点（quantum dots）合成与光学性质、胶体半导体纳米晶、量子化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **巴黎-突尼斯-美国（1961–）**：突尼斯数学家之子，生于巴黎，幼年随家迁美——数学之家长大的化学家。
2. **哈佛双学位（1982/1983）**：A.B. + A.M. 连读，为物理化学打底。
3. **芝加哥双导师（1983–1988）**：Freed 组做理论高分子物理、Oka 组做 H3+ hot-bands 红外实验——理论与光谱的双手互搏。
4. **H3+ 与木星（1989）**：其 Oka 组实验数据参与了 1989 年木星发射光谱的解读——博士期间的"天文级"注脚。
5. **Bell Labs 夏季项目（1980s 末）**：Oka 推荐 → Brus 引入量子点世界——三人诺奖链条的第一环。
6. **Brus 组博士后（1988–1990）**：与 Steigerwald（金属有机合成化学家）同组，研究缩小量子点尺寸——化学合成的"手艺"在此习得。
7. **入职 MIT（1990）**：1990 加入 MIT，1996 升教授；后任 Lester Wolfe 教授。
8. **1993 热注入法（★核心）**：与博士生 David J. Norris、Christopher B. Murray 在 JACS 发表 hot-injection 合成法——可重现、尺寸明确、高光学质量的单分散 CdE（S/Se/Te）纳米晶，攻克"高质量量子点制备"难题。
9. **尺寸可调（1993 后）**：化学合成突破使量子点可按尺寸"调谐"性质——precise and reproducible，打开大规模应用之门。
10. **应用开花**：量子点如今用于 LED、光伏、光电探测器、光导体、激光、生物成像、生物传感等。
11. **1997 (CdSe)ZnS 核壳结构**：与 Dabbousi 等发表高发光核壳量子点尺寸系列（JPCB）——合成工艺的又一里程碑（页面 Selected publications 明载）。
12. **被引用最多的化学家之一**：2000–2010 十年间被引最多的化学家之一；2020 与 Murray、Hyeon Taeghwan 同列 Clarivate Citation Laureate（纳米晶合成）。
13. **2023 诺贝尔化学奖**：与 Louis E. Brus、Alexey Ekimov 共享，官方理由 "for the discovery and synthesis of quantum dots"；2024 获突尼斯共和国勋章 Grand Officier、2025 获 Carnegie Great Immigrant Award、2026 当选美国国家工程院院士。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#372A75` | 量子点受激发光的高贵紫（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（热注入合成 badgeHot） | `#B3462E` | 橙红注射瞬间 / 单分散纳米晶 |
| 分类色 2（尺寸调谐 badgeTune） | `#1E6E8C` | 青蓝尺寸-波长调谐曲线 |
| 分类色 3（核壳结构 badgeCore） | `#2E7D4F` | 绿 (CdSe)ZnS 核壳 |
| 分类色 4（应用图景 badgeApp） | `#8C2F5B` | 玫红 LED / 生物成像 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「量子点」——粒径决定发光颜色的纳米晶粒。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（源文件 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`，执行时软链/复制至本目录，不复制 wav 入库）
- **风格**：怀旧 / 温暖 / 追忆式的抒情
- **匹配理由**：
  - "怀旧" 匹配其跨越四十年_quantum dots_ 从 1981 Ekimov 玻璃、1982 Brus 溶液到 1993 热注入法的接力叙事——本篇是"集大成者"的回望
  - "温暖" 匹配量子点的感官意象——纳米晶在紫外灯下发出的暖色荧光
  - 追忆式抒情匹配移民叙事——巴黎→突尼斯→印第安纳→剑桥（MIT），一家人的迁徙线
- **时长**：执行时用 ffprobe 核对 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 量子点的化学工匠 / Moungi Bawendi 1961– + 四色 badge + 右上头像 + 国籍行（美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/双博士导师/博士后/领域/荣誉）
03  巴文迪的一生 — 时间线（10 节点：1961→1978→1982→1983→1988→1990→1993→1996→2023→2026）
04  早年：数学家之子 (1961–1978) — 表格「时间|事件|结果」（巴黎/突尼斯/West Lafayette）
05  哈佛与芝加哥：理论与光谱 (1978–1988) — 表格「阶段|内容|结果」+ 双导师（Freed/Oka）
06  H3+ 与木星 (1989) — 表格「问题|方法|结果」+ 公式框：H3+ hot-bands 与木星发射光谱
07  Bell Labs：进入量子点世界 (1988–1990) — 表格「人物|事件|结果」（Brus 引路 + Steigerwald 合作）
08  1993 热注入法 (★核心) — 表格「问题|方法|结果」+ 公式框：单分散 CdE 纳米晶三要素
09  尺寸调谐与核壳 (1993–2000) — 表格「问题|方法|结果」+ 公式框：粒径 ↔ 发光波长
10  从实验室到千家万户 — 四分类应用盒（LED/光伏/生物成像/传感）
11  荣誉清单 — 「类别|代表|意义」表格 + itemize（Sloan 1994 → NAS 2007 → Lawrence 2006 → Nobel 2023）
12  三人接力 — 流程图页：Ekimov 1981 玻璃 → Brus 1982 溶液 → Bawendi 1993 合成法
13  遗产：纳米晶世纪 — 表格「领域|贡献|结果」+ Clarivate 2020 / NAE 2026
14  结尾 — 「把量子点从偶然变成工艺的人。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2023 诺奖共享口径 | 与 **Brus、Ekimov 三人共享**，官方理由 "for the discovery and synthesis of quantum dots"——勿写"独享"或"两人共享" |
| 三人分工 | Ekimov（1981 玻璃中首发）→ Brus（1982 溶液/胶体 + 理论框架）→ Bawendi（1993 高质量可重现合成法）——勿把"发现量子点"单独归任何人 |
| 博士导师 | **双导师 Karl Freed + Takeshi Oka**（infobox 与正文均两人并列）——勿只写一人 |
| 师承方向 | Brus 是其 **Bell Labs 博士后导师**（非博士导师）——博士在芝加哥完成 |
| 学生口径 | 正文明确 "his PhD students David J. Norris and Christopher B. Murray"（1993 论文）；infobox Doctoral students 为 Murray、Cherie Kagan——Norris/Kagan/Murray 三人均可入学生关系 |
| 1993 论文作者序 | Murray, C. B.; Norris, D. J.; Bawendi, M. G.——Murray 一作；勿写 Bawendi 一作 |
| Clarivate 2020 | "selected as a Clarivate Citation Laureate jointly with Murray and Hyeon Taeghwan"——是预测名单（同列），勿写成"共同获奖" |
| USSR/突尼斯荣誉 | 2024 突尼斯共和国勋章 Grand Officier（Decorations 节）与 Tunis University Medal of Honor——两处突尼斯荣誉勿混淆 |
| 出生国与国籍 | 生于法国巴黎、父为突尼斯人——封面国籍写"美国"（美籍化学家），血统信息放身份页 |
| 家庭成员 | 妻 Rachel Zimmerman 是记者、MIT 教授 Seth J. Teller 的遗孀——Teller 与 Bawendi 无师承/合作，勿建关系 |
| NAE 年份 | 美国国家工程院院士为 **2026** 当选——勿写 2023 |
| 页面无载禁写 | 页面无其博士论文考官、无子女信息、无直接引语——全文不编引语，改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q15433043 | ✅ |
| name_zh | 蒙吉·巴文迪 | ✅ |
| name_en | Moungi Bawendi | ✅ |
| birth_date | 1961-03-15 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States / Tunisia / France（rank 0/1/2） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | quantum dots（person_field 细分：quantum dots / nanocrystal synthesis / quantum chemistry / colloidal semiconductor nanocrystals，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 博士后 / 同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Karl Freed | 师→生（博士导师） | 芝加哥双导师之一，理论高分子物理 |
| advisor-student | Takeshi Oka | 师→生（博士导师） | 芝加哥双导师之一，H3+ hot-bands 实验；库内已有记录（id=3475） |
| advisor-student | Louis E. Brus | 师→生（博士后导师） | Bell Labs 博士后，引入量子点研究 |
| colleague | Michael L. Steigerwald | 无向 | Bell Labs 同组金属有机合成化学家，合作缩小量子点 |

**门生（Bawendi → 学生，源自正文与 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Christopher B. Murray | Bawendi → 学生 | 1993 热注入法一作博士生；2020 Clarivate 同列 |
| advisor-student | David J. Norris | Bawendi → 学生 | 正文明载的 1993 论文博士生 |
| advisor-student | Cherie Kagan | Bawendi → 学生 | infobox Doctoral students 明载 |

**共同得主 / 家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Louis E. Brus | 无向 | 2023 诺贝尔化学奖共同得主 |
| co-honored | Alexey Ekimov | 无向 | 2023 诺贝尔化学奖共同得主 |
| co-honored | Hyeon Taeghwan | 无向 | 2020 Clarivate Citation Laureate 同列 |
| spouse | Rachel Zimmerman | 无向 | 记者，Seth J. Teller 遗孀 |
| parent-child | Mohammed Salah Baouendi | 巴文迪 → 父 | 突尼斯数学家，Purdue 数学系（正文用全名 Mohammed Salah Baouendi，Wikipedia 条目题为 M. Salah Baouendi，取正文全名） |

> metadata.json `doctoral_advisor` 与 infobox 一致（Freed/Oka）；无 metadata-only 需禁入的关系。
> 注：对手方 Rachel Zimmerman / Mohammed Salah Baouendi / Karl Freed / Murray / Norris / Kagan / Hyeon Taeghwan 均为库内新建 stub，按本表规范全名建。

## 8. 奖项清单

- Nobel Prize in Chemistry（2023，与 Brus/Ekimov 共享，"for the discovery and synthesis of quantum dots"）
- Sloan Research Fellowship（1994）
- Nobel Signature Award for Graduate Education in Chemistry, ACS（1997）
- Sackler Prize in Physical Chemistry of Advanced Materials（2001）
- Ernest Orlando Lawrence Award（2006）
- AAAS Fellow（2003）；American Academy of Arts and Sciences（2004）；NAS 院士（2007）
- ACS Award in Colloid and Surface Chemistry（2010-03-23 全国会议颁发）
- SEMI Award for North America（2011，量子点研究）
- Clarivate Citation Laureate in Chemistry（2020，与 Murray、Hyeon Taeghwan 同列）
- Grand Officier of the Order of the Republic（突尼斯，2024）；Tunis University Medal of Honor
- Carnegie Corporation Great Immigrant Award（2025）；美国国家工程院院士（2026）

## 9. 机构清单

- 教育：West Lafayette Junior-Senior High School（–1978）；Harvard University（A.B. 1982、A.M. 1983）；University of Chicago（PhD 1988）
- 任职：Bell Labs 博士后（1988–1990，Brus 组）；MIT（1990 加入，1996 教授，Lester Wolfe Professor）
- 任职机构仅 MIT 一家（页面 Workplaces）——勿编造其他教职

## 10. 终审清单

- [ ] 生卒 1961-03-15 巴黎（在世）；国籍美国（法/突尼斯裔）
- [ ] 双博士导师 Freed + Oka；Brus 是博士后导师
- [ ] 1993 热注入法作者序 Murray/Norris/Bawendi；学生 Murray/Norris/Kagan 三人
- [ ] 2023 三人共享口径与官方理由英文原文无误
- [ ] Clarivate 2020 是"同列"非"共同获奖"；NAE 2026 年份无误
- [ ] 全文无编造引语；"第一次/唯一"类断言均有页面明载
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Moungi_Bawendi/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：经 REST API 回退下载 infobox 2023 实照；失败则装饰圆占位并注记
- [ ] 国籍：封面明示"美国"
- [ ] 引语核对：全文无直接引语（页面无载）——检查无编造"原话"
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐；结尾品牌 OpenMathAI

---

> **名单状态**：`chemist/generate_21th_century_list.py` 更新由主控统一收尾，本文件不改动生成器。
