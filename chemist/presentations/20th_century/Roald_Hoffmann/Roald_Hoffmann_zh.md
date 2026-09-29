# Roald Hoffmann（罗尔德·霍夫曼）立传提示词

> qid=Q273279 · 1937-07-18 – 在世 · 波兰裔美国理论化学家 · 20 世纪 · 诺贝尔化学奖（1981，与 Kenichi Fukui 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Roald_Hoffmann/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 目录从 page.md 图注照片取：2009 年 Roald_Hoffmann.jpg；若下载失败用装饰圆占位并注记）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 波兰裔美国理论化学家\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（出生名 Roald Safran）、国籍、出生地/去世地（在世留白）、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「分子轨道 / 对称性」母题——离散圆点暗示电子轨道的相位与对称。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（Woodward–Hoffmann 规则的热/光反应条件、扩展 Hückel 法、等瓣类似性）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Roald Hoffmann（出生名 Roald Safran；中文惯称：罗尔德·霍夫曼；ForMemRS）
- **生卒**：1937-07-18 生于波兰第二共和国 Złoczów（今乌克兰佐洛奇夫 Zolochiv）→ **在世**（去世地留白）
- **国籍**：美国（出生时为波兰第二共和国国籍；正文口径 Polish-American）
- **身份**：理论化学家 / 剧作家 / 诗人（playwright, chemist, poet, writer）；Cornell 大学 Frank H. T. Rhodes Professor of Humane Letters Emeritus
- **家庭**：波兰犹太家庭；父 Hillel Safran 为土木工程师（在劳改营因参与武装囚犯密谋被德军拷打杀害），母 Clara（娘家姓 Rosen）为教师；母亲改嫁后全家改姓 Hoffmann；1949 年随难民运输船 *Ernie Pyle* 移居美国；1960 年娶 Eva Börjesson，子女 Hillel Jan 与 Ingrid Helena
- **大屠杀经历**：1943-01 至 1944-06（5–7 岁）与母亲、两位叔叔和一位阿姨藏身当地学校阁楼与储藏室达 18 个月（乌克兰邻居 Mykola Dyuk 收留）；藏身期间母亲以教科书教他读写与地理；其余家族多死于大屠杀，仅一位祖母等少数幸存；2006 年与成年儿子重返 Zolochiv，藏身阁楼仍在、储藏室已成化学教室；2009 年在其倡议下 Zolochiv 建立大屠杀遇难者纪念碑
- **教育轨迹**：
  - 1955 毕业于纽约 Stuyvesant High School（获 Westinghouse 科学奖学金）
  - 1958 Columbia College 文学学士（BA）
  - 1960 Harvard 文学硕士（MA）；1962 Harvard 哲学博士（论文 *Theory of Polyhedral Molecules: Second Quantization and Hypochromism in Helices*）
- **导师**：Martin Gouterman 与 William N. Lipscomb Jr. **联合指导**（joint supervision；Lipscomb 为 1976 诺贝尔化学奖得主）
- **博士**：1962，Harvard University
- **研究领域**：理论化学——分子轨道理论、扩展 Hückel 法、Woodward–Hoffmann 规则、等瓣类似性、有机金属与固态化学、极端高压下的化学键

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **出生与命名（1937）**：生于 Złoczów 犹太家庭，以挪威探险家 Roald Amundsen 命名。
2. **阁楼中的童年（1943–1944）**：18 个月藏身学校阁楼——母亲以教材启蒙；"a cocoon of love"（被爱包裹的茧）。
3. **父之死与改姓（1943–1944）**：父亲在劳改营被拷打杀害；母亲改嫁，全家改姓 Hoffmann。
4. **移居美国（1949）**：乘运输船 *Ernie Pyle* 赴美；1955 年 Stuyvesant 高中毕业获 Westinghouse 奖学金。
5. **Columbia → Harvard（1958–1962）**：BA 1958；在 Harvard 于 Gouterman 与 Lipscomb 联合指导下读博，研究多面体分子的分子轨道理论。
6. **扩展 Hückel 法（1963）**：在 Lipscomb 指导下与 Lawrence Lohr 共同发展、后由 Hoffmann 扩展——半经验分子轨道计算工具，1963 年提出用于确定分子轨道。
7. **入职 Cornell（1965）**：此后一直任教 Cornell，直至 Frank H. T. Rhodes 讲座荣休教授。
8. **Woodward–Hoffmann 规则（1965 前后）**：与 Robert Burns Woodward 合作，从复杂分子电子轨道的微妙对称与不对称性近似预言化学转化——加热与光照活化的产物类型不同。
9. **1981 诺贝尔化学奖**：与日本化学家 Kenichi Fukui 共享，官方理由 "for their theories, developed independently, concerning the course of chemical reactions"——**两人各自独立**发展理论；Woodward 未获此奖（1965 年已因其他工作获奖，页面表述为该奖只授予在世者）。
10. **等瓣类似性（Isolobal Analogy）**：在诺贝尔演讲中提出，用于预言有机金属化合物的成键性质。
11. **高压化学（近期）**：与 Neil Ashcroft、Vanessa Labet 研究极端高压下的键合——"氢在极端压力下的行为，正如 1 个大气压下的无机分子！"
12. **科学与人文双栖**：1988 年主持 PBS 26 集教学系列 *The World of Chemistry*；2001 年起在纽约 Cornelia Street Cafe 主持月度 *Entertaining Science*；诗集 *The Metamict State*（1987）、*Gaps and Verges*（1990）、*Chemistry Imagined*（1993）；与 Carl Djerassi 合写剧本 *Oxygen*；自传性剧本 "Something That Belongs to You"（2009）。
13. **记忆与和解**：2006 重返 Zolochiv、2009 推动建纪念碑；2018 年以其名命名的 Hoffmann Institute of Advanced Materials 在深圳成立（2019-05 亲自出席开幕）；自述 "an atheist who is moved by religion"。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青绿 deep teal） | `#175E54` | 分子轨道的深邃与稳定（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（轨道与成键 badgeOrbital） | `#2E5A9E` | 蓝扩展 Hückel 法 / 多面体分子 |
| 分类色 2（周环反应 badgePericyclic） | `#1B7A43` | 绿 Woodward–Hoffmann 规则 / 热与光 |
| 分类色 3（有机金属 badgeOrganometallic） | `#D97B29` | 琥珀等瓣类似性 / 有机金属 |
| 分类色 4（科学与人文 badgeHumanities） | `#C0395B` | 玫瑰诗与剧 / 科学传播 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「轨道 / 对称」的相位分布。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`；执行 Beamer 时复制为本目录 `The_Flow_of_Time.wav`，勿直接引用外部路径）
- **风格**：沉静 / 时间流逝 / 纪录片式回望
- **匹配理由**：
  - "时间之流" 匹配其人生跨度的重量——从 1943 年阁楼到 2025 年仍在世的 88 年，从大屠杀幸存者到诺奖得主与诗人
  - "沉静" 匹配其理论化学气质——轨道与对称性的安静洞察，而非爆炸性实验
  - "纪录片式回望" 匹配传记叙事——Złoczów → 阁楼 → 纽约 → Columbia/Harvard → Cornell → 诺奖 → 诗与剧
- **时长对齐**：ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 轨道上的诗人 / Roald Hoffmann 1937– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/出生名/国籍/教育/博士/师承/出生地/领域/荣誉/在世留白）
03  霍夫曼的一生 — Sanger 式时间线（10 节点：1937→1943→1949→1955→1958→1962→1963→1965→1981→今日）
04  阁楼中的童年 (1937–1949) — 表格「时间|事件|结果」（藏身 18 个月 / 父之死 / 改姓 / 移美）
05  从 Stuyvesant 到 Harvard (1955–1962) — 表格「时间|事件|结果」+ 公式框：博士论文主题（多面体分子二阶量子化）
06  扩展 Hückel 法 (1963) — 表格「问题|方法|结果」+ 公式框：扩展 Hückel 法
07  Woodward–Hoffmann 规则 (1965) — 表格「问题|方法|结果」+ 公式框：热反应 vs 光反应
08  1981 诺贝尔化学奖 — 表格「人物|贡献|结果」（Hoffmann / Fukui 各自独立；Woodward 注记）+ 官方理由公式框
09  等瓣类似性与高压化学 — 表格「概念|内容|意义」+ 公式框：isolobal 类比
10  科学与人文 — 表格「领域|作品|年份」（The World of Chemistry / 诗集 / Oxygen / Should've）
11  荣誉与纪念 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单：ForMemRS 1984 / Priestley 1990 等）
12  记忆与和解 — Sanger FFT 页式流程图（2006 重返 Zolochiv → 2009 纪念碑 → 2018 深圳研究所）
13  遗产：规则改变化学 — 四分类遗产盒 + 公式框：Woodward–Hoffmann 规则的普适性
14  结尾 — 「对称性，是自然写给化学家的密码。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1981 共享结构 | 与 **Kenichi Fukui 共享**，官方理由 "for their theories, developed independently, concerning the course of chemical reactions"——**developed independently（各自独立发展）** 必须保留；勿写三人共享 |
| Woodward 未获奖 | Woodward 是合作者但**未获 1981 奖**；page.md 表述为该奖 "is given only to living persons"、他已因其他工作获 1965 奖——按此口径转述，勿自行发挥"诺奖不追授"等页面无载解释 |
| 出生地 | 生于 **波兰第二共和国 Złoczów（今乌克兰佐洛奇夫）**——勿写"波兰 Zolochiv"或"乌克兰出生"；国籍口径 Polish-American |
| 出生名 | 出生名 **Roald Safran**，母改嫁后改姓 Hoffmann；命名自 Roald Amundsen——勿混淆本名与现名 |
| 大屠杀细节 | 藏身地点是**当地学校的阁楼与储藏室**（1943-01~1944-06 共 18 个月，5–7 岁）；收留者是邻居 Mykola Dyuk；父 Hillel Safran 在劳改营被拷打杀害——仅写 page.md 实载 |
| 博士导师 | **Gouterman 与 Lipscomb 联合指导**（joint supervision）——勿只写 Lipscomb 一人 |
| 扩展 Hückel 法 | 由 **Lawrence Lohr 与 Roald Hoffmann** 在 Lipscomb 指导下发展、后由 Hoffmann 扩展——勿写"Hoffmann 独自发明" |
| 等瓣类似性 | 在**诺贝尔演讲中**引入——勿写具体年份（页面无载） |
| 高压合作者 | 近期高压键合工作合作者是 Neil Ashcroft 与 Vanessa Labet——人名勿写错 |
| 妻子 | Eva Börjesson（1960 年结婚）——勿与诗人/剧作家合作者混淆 |
| 文学作品 | 诗集三部实载（The Metamict State 1987 / Gaps and Verges 1990 / Chemistry Imagined 1993）；剧本 *Oxygen* 与 **Carl Djerassi 合写**；"Should've"（2006）；"Something That Belongs to You"（2009）——勿编造其他作品 |
| 自我描述 | "an atheist who is moved by religion" 是 page.md 原句——**唯一可引原话**；其他中文引号内容一律改为间接转述 |
| 荣誉年份 | NAS 1972 / ForMemRS 1984 / Priestley 1990 / National Medal of Science 1983 / Cope Award 1973（与 Woodward）——年份勿错 |
| 深圳研究所 | Hoffmann Institute of Advanced Materials **2018-02 成立、2019-05 开幕**（其本人出席）——勿写错顺序 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q273279 | ✅ |
| name_zh | 罗尔德·霍夫曼 | ✅ |
| name_en | Roald Hoffmann | ✅ |
| birth_date | 1937-07-18 | ✅ |
| death_date | （在世留白） | ✅ |
| nationality | United States（rank 0）/ Poland（rank 1，出生时为波兰第二共和国） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | theoretical chemistry（person_field 细分：theoretical chemistry / organometallic chemistry / solid-state chemistry / chemical education，带 rank） | ✅ |
| has_biography | 0（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 合作者 / 共同得主**（只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Martin Gouterman | 师→生（博士联合导师） | Harvard 博士联合导师 |
| advisor-student | William Lipscomb | 师→生（博士联合导师） | Harvard 博士联合导师，1976 诺贝尔化学奖得主 |
| advisor-student | Jing Li | Hoffmann → 学生 | infobox Doctoral students |
| advisor-student | Jeffrey R. Long | Hoffmann → 学生 | infobox Other notable students（undergraduate） |
| advisor-student | Karen Goldberg | Hoffmann → 学生 | infobox Other notable students（undergraduate） |
| co-honored | Kenichi Fukui | 无向 | 1981 诺贝尔化学奖共同得主（各自独立发展理论） |
| colleague | Robert Burns Woodward | 无向 | 合作发展 Woodward–Hoffmann 规则；1973 Cope Award 共同得主 |
| colleague | Lawrence Lohr | 无向 | 扩展 Hückel 法共同发展者 |
| colleague | Neil Ashcroft | 无向 | 极端高压下键合研究合作者 |
| colleague | Carl Djerassi | 无向 | 合写剧本 Oxygen |
| spouse | Eva Börjesson | 无向 | 1960 年结婚 |

> **禁入库名单（metadata.json-only）**：doctoral_student 另含 Michael John Bucknum、Timothy Ray Hughbanks、Ji Feng、Qiang Liu、Ralph A. Wheeler、Chong Zheng、Garegin A Papoian 七人，正文 infobox 无——**不予入库**。Don Showalter 仅系 PBS 节目演示搭档，非学术关系，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1981，与 Kenichi Fukui 共享）
- ACS Award in Pure Chemistry（1969）；International Academy of Quantum Molecular Science Award（1970）
- American Academy of Arts and Sciences Fellow（1971）；NAS 院士（1972）
- Arthur C. Cope Award（1973，与 Robert B. Woodward）
- American Chemical Society Inorganic Chemistry Award（1982）
- National Medal of Science（1983）
- American Philosophical Society Fellow（1984）；Foreign Member of the Royal Society, ForMemRS（1984）
- Foreign Member of the Royal Swedish Academy of Sciences（1985）；Finnish Society of Sciences and Letters（1988）
- Priestley Medal（1990）；Harvard Centennial Medal（1994）；Pimentel Award in Chemical Education（1996）
- E.A. Wood Science Writing Award（1997）；Literaturpreis der Verband der Chemischen Industrie（1997）；Kołos Medal（1998）
- American Institute of Chemists Gold Medal（2006）；Lichtenberg Medal（2008）；Grady-Stack Award（2009）
- Marie Curie Medal of the Polish Chemical Society（2019）；Great Immigrants Award（2023）
- 25+ honorary degrees

## 9. 机构清单

- 教育：Stuyvesant High School（–1955）、Columbia University（BA 1958）、Harvard University（MA 1960、PhD 1962）
- 任职：Cornell University（1965–，Frank H. T. Rhodes Professor of Humane Letters Emeritus）
- 命名机构：Hoffmann Institute of Advanced Materials（深圳，2018 年成立、2019-05 开幕）

## 10. 终审清单

- [ ] 生卒 1937-07-18 / 在世留白；出生地波兰第二共和国 Złoczów（今乌克兰 Zolochiv）
- [ ] 1981 与 Fukui 共享、"developed independently" 保留、Woodward 未获奖口径按 page.md
- [ ] 出生名 Roald Safran、父 Hillel Safran、母 Clara、改姓缘由
- [ ] 博士导师 Gouterman + Lipscomb 双列；扩展 Hückel 法 Lohr+Hoffmann
- [ ] 引语仅 "an atheist who is moved by religion"（page.md 原句），其余全为间接转述
- [ ] 荣誉年份逐条对照 page.md
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Roald_Hoffmann/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像已就位或装饰圆占位并注记
- [ ] 国籍：封面顶部明示波兰裔美国
- [ ] 引语核对：仅 "an atheist who is moved by religion" 可直引
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`（执行者不改）。
