# Walter Kohn（沃尔特·科恩）立传提示词

> qid=Q78510 · 1923-03-09 – 2016-04-19 · 奥地利出生 / 加拿大 / 美国 · 诺贝尔化学奖（1998，与 John Pople 共享）· 奥裔美国理论物理学家与理论化学家
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Walter_Kohn/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注——用 `images.txt` 中的 `Walter_Kohn_Oxford_University.JPG`（牛津荣誉博士学位照，真实照片，图注须写明场景），下载 250px→500px；备选 UCSB-NobelBanner-WalterKohn.png 作插图页素材。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 以密度代替波函数\enspace·\enspace 奥地利出生·美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「电子密度」母题——离散圆点的疏密暗示空间中电子密度的分布。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如 DFT 核心：以电子密度 n(r) 而非多体波函数 Ψ 描述体系；Hohenberg–Kohn 定理与 Kohn–Sham 方程以文字语义框呈现，公式符号仅用页面实载名称）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Walter Kohn（中文惯称：沃尔特·科恩；德语发音 [ˈvaltɐ ˈkoːn]，页面注音可保留）
- **生卒**：1923-03-09 生于奥地利维也纳 → 2016-04-19 逝于美国加州圣巴巴拉家中（颌部癌），享年 93
- **国籍**：奥地利出生；1957 年放弃加拿大国籍、入籍美国（正文口径）；infobox 国籍栏 Canada / United States / Austria
- **身份**：奥裔美国理论物理学家与理论化学家（theoretical physicist and theoretical chemist）；犹太家庭出身
- **家庭**：犹太家庭；父母 Salomon 与 Gittel Kohn 在大屠杀（Holocaust）中**被害**；本人有强烈犹太身份认同，参与过 UCSD 犹太研究（Judaic Studies）项目创建；自认 Deist
- **教育轨迹**：
  - 维也纳 Akademisches Gymnasium（infobox educated_at）
  - Kindertransport：德奥合并（Anschluss）后经英国转赴加拿大（1940-07；17 岁）；先羁押于魁北克 Sherbrooke 附近营地，后入多伦多大学
  - University of Toronto：战时应用数学 BA（1945，服兵役一年后修满 2½/4 年即获授）→ 应用数学 MA（1946）
  - Harvard University：物理学 PhD（1948）
- **导师**：Julian Schwinger（哈佛；三体散射问题）
- **研究领域**：凝聚态物理 / 量子化学——密度泛函理论（DFT）、半导体物理、多体问题

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **维也纳的犹太少年（1923）**：1938 年德奥合并后经 Kindertransport 抵英；对原乡的感情——"very painful"（其原话为页面直引，须逐字核对后使用）。
2. **集中营式的起步（1940）**：作为奥地利籍"敌侨"被转运加拿大——17 岁随英国护航船队穿越潜艇出没海域抵魁北克城，先羁押于 Sherbrooke 附近营地；**营地提供了少量教育设施，被他用到极致**。
3. **进不了化学楼（多伦多）**：因德国国籍**被禁止进入化学系大楼**——于是选了物理与数学；未来的化学诺奖得主由此入门。
4. **战时学位（1945–1946）**：一年兵役后以修毕 2½/4 年课程的"战时学士"毕业（应用数学），翌年 MA。
5. **哈佛与 Schwinger（1948）**：师从 Julian Schwinger 做三体散射问题获物理学博士；同期受 **J. H. Van Vleck** 影响转向固体物理。
6. **哥本哈根与卡内基（1950s）**：加拿大国家研究委员会博士后短暂在哥本哈根；1950–1960 Carnegie Mellon——完成多重散射能带结构（后称 **KKR 方法**）的奠基性工作。
7. **贝尔实验室与 Luttinger**：与贝尔实验室的关联把他带入半导体物理；与 Luttinger 长期合作——**Luttinger–Kohn 模型**（半导体能带）、Kohn–Luttinger 超导机制（1965）。
8. **UCSD 与 Kohn–Majumdar 定理（1960–1979）**：1960 转入新建的加州大学圣迭戈分校，曾任物理系主任；与学生 **Chanchal Kumar Majumdar** 发展 Kohn–Majumdar 定理（Fermi 气体束缚/非束缚态）。
9. **巴黎的决定性访问**：DFT 起于巴黎高等师范学院（École Normale Supérieure）访问期间与 **Pierre Hohenberg** 的合作，动因是合金理论——**Hohenberg–Kohn 定理**（1964，Inhomogeneous Electron Gas）。
10. **Kohn–Sham 方程（1965）**：与 **Lu Jeu Sham** 合作发展——现代材料科学的标准"主力工具"（页面原话 "standard workhorse"），甚至用于等离子体的量子理论。
11. **1998 诺贝尔化学奖**：与 **John Pople** 共享；表彰其对理解材料电子性质的贡献——Kohn 在 DFT 发展中起了**主导作用**：用量子力学方程以电子密度（而非多体波函数）计算电子结构。
12. **引用史的高峰（2004）**：对 1893–2003 年 Physical Review 全部论文引用的统计研究——Kohn 是"最高引用影响"百篇论文中**五篇**的作者，**包括前两篇**（正文原文明载，可用并注明口径）。
13. **圣巴巴拉的暮年（1979–2016）**：1979 年出任圣巴巴拉理论物理研究所（KITP 前身口径按页面 "Institute for Theoretical Physics"）创所所长；1984 年起任 UCSB 物理系教授直到生命终点；1961 Buckley 奖、1988 国家科学奖章、1998 ForMemRS。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深砖红 oxblood） | `#9E2B25` | 维也纳的砖红与补偿的沉重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（DFT badgeDFT） | `#2F5D8A` | 深蓝密度泛函理论 / HK 定理 |
| 分类色 2（半导体 badgeSemi） | `#3E6B4A` | 绿半导体物理 / KKR / Luttinger–Kohn |
| 分类色 3（流亡岁月 badgeFlight） | `#6E4A2B` | 褐 Kindertransport / 加拿大营地 |
| 分类色 4（多体问题 badgeMany） | `#7A4A6E` | 紫多体问题 / Kohn–Majumdar |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），疏密分布呼应电子密度。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（清单指定文件 `48-QL3O8MUFAm4-Cinematic-Experience.wav`；如目录内尚无软链则从 music_audio 软链，不要复制 wav）
- **风格**：史诗感 / 命运感 / 电影叙事
- **匹配理由**：
  - 电影化的命运弧线匹配其人生——Kindertransport、敌侨营地、进不了化学楼，最终以物理学摘得化学诺奖
  - 史诗感匹配 DFT 的地位——"standard workhorse of modern materials science"
  - 命运感匹配其对原乡与父母的记忆，全篇需克制的沉重
- **时长**：以曲目实际时长为准（> 15 页 × 7 秒即由 ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 以密度代替波函数 / Walter Kohn 1923–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  科恩的一生 — 高斯式时间线（10 节点：1923→1938/40→1945→1948→1950→1960→1964/65→1979→1998→2016）
04  维也纳与流亡 (1923–1945) — 表格「时间|事件|结果」（Kindertransport / Sherbrooke 营地 / 化学楼禁入）
05  哈佛：Schwinger 与 Van Vleck (1945–1950) — 表格「时间|事件|结果」
06  KKR 与半导体 (1950–1960) — 表格「问题|方法|结果」+ 公式框：多重散射能带（KKR 方法语义框）
07  Hohenberg–Kohn 定理 (1964) — 表格「问题|方法|结果」+ 公式框：n(r) 代替 Ψ（巴黎访问、合金理论动因）
08  Kohn–Sham 方程 (1965) — 表格「挑战|合作|结果」+ 公式框：Kohn–Sham 方程语义框
09  1998 诺贝尔化学奖 — 表格「得主|贡献|份额」（与 Pople 共享；获奖理由按页面口径）
10  教学与定理 — 表格「人物|方向|结果」（Majumdar / Kohn–Majumdar 定理）
11  荣誉与年表 — 高斯式「类别|代表|意义」表格（Buckley 1961 / Davisson–Germer 1977 / NMS 1988 / ForMemRS 1998 / 奥地利Decoration 1999 与 2008）
12  KITP 与 UCSB — 高斯 FFT 页式流程图（1979 创所所长 → 1984 UCSB 教授 → 终老）
13  遗产：材料科学的工具 — 四分类遗产盒 + 公式框：2004 引用史统计（百篇中五篇含前二）
14  结尾 — 「他把多体问题化成了一片密度的云。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖学科错位 | Kohn 是**理论物理学家**获**化学**诺奖——正文口径 "Austrian-American theoretical physicist and theoretical chemist"；获奖理由按页面："their contributions to understanding the electronic properties of materials"（与 Pople 共享），勿改写成官方全句 |
| DFT 归属 | Kohn 在 DFT 发展中起**主导作用**（页面 "played the leading role"）；Hohenberg–Kohn 定理与 Hohenberg 共有；Kohn–Sham 方程与 Sham 共有——三人归属勿混 |
| 与 Pople 分工 | Pople 是**计算方法**（量子化学计算、Gaussian）；Kohn 是**理论框架**（DFT）——页面未细写 Pople 部分，本篇只按自己页面表述 |
| 父母遇害 | 父母 Salomon/Gittel Kohn **在 Holocaust 中被谋杀**（页面直引原句）——措辞克制、事实准确；相关引语（"My feelings towards Austria..."）为页面直引，须逐字核对后使用，中文引号内不得改写 |
| 国籍变迁 | 奥地利出生（1923）→ 加拿大（1940 起的羁押/求学岁月）→ 1957 放弃加拿大籍入籍美国；infobox 国籍栏 Canada/US/Austria 三条——入库三条带 rank（United States 0 / Canada 1 / Austria 2），行文按"奥地利出生、美国籍"主线 |
| 多伦多禁入化学楼 | 因德国（奥地利的行政归属口径按页面 "As a German national"）国籍被禁入化学楼——**勿写成因犹太身份** |
| 战时学位 | BA 为服一年兵役后修满 2½/4 年的战时学位（1945）；MA 1946——勿写正常四年制 |
| Van Vleck 角色 | 页面表述 "fell under the influence of"（受其影响）——入库 influence 关系，**不是博士导师**（导师是 Schwinger） |
| Majumdar | 页面明载 "his student Chanchal Kumar Majumdar"——入库 advisor-student（Kohn→学生）；Kohn–Majumdar 定理为二人合作 |
| 2004 引用统计 | "五篇/含前两篇"须注明口径：1893–2003 年 Physical Review 期刊引用研究（2004 年发表） |
| 去世地/死因 | 2016-04-19 逝于圣巴巴拉**家中**，死因颌部癌（jaw cancer），享年 93——勿写医院 |
| 妻子卒年 | Lois (Adams) 卒于 2010；Mara (Vishniac) Schiff 卒于 2018（Kohn 身后）——两任配偶均入库 spouse |
| 引语 | 仅可使用页面直引的 Kohn 自述（对奥地利感情段）；其余叙事全部间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q78510 | ✅（回填库内 stub id=2568） |
| name_zh | 沃尔特·科恩 | ✅ |
| name_en | Walter Kohn | ✅（与库内 db_name_en 精确一致） |
| birth_date | 1923-03-09 | ✅ |
| death_date | 2016-04-19 | ✅ |
| nationality | United States / Canada / Austria（三条带 rank） | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | theoretical physics（person_field 细分：density functional theory / condensed matter physics / semiconductor physics / many-body problem，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Julian Schwinger | 师→生（博士导师） | 哈佛博士（1948），三体散射问题 |
| influence | John Van Vleck | 无向 | 哈佛时期受其影响发展出固体物理兴趣（页面 "fell under the influence of"；入库用库内规范名 John Van Vleck） |
| co-honored | John Pople | 无向 | 1998 诺贝尔化学奖共享 |
| colleague | Pierre Hohenberg | 无向 | 巴黎 ENS 访问期间合作开创 DFT；Hohenberg–Kohn 定理（1964） |
| colleague | Lu Jeu Sham | 无向 | 合作发展 Kohn–Sham 方程（1965） |
| colleague | Joaquin Mazdak Luttinger | 无向 | 贝尔实验室起的长期合作；Luttinger–Kohn 模型、Kohn–Luttinger 超导机制（1965） |
| advisor-student | Chanchal Kumar Majumdar | Kohn→学生 | 学生；合作发展 Kohn–Majumdar 定理 |
| spouse | Lois Adams | 无向 | 首任（infobox 作 Lois (Adams)，卒于 2010） |
| spouse | Mara Vishniac Schiff | 无向 | 第二任（infobox 作 Mara (Vishniac) Schiff，卒于 2018） |

> 禁入库名单：父母 Salomon/Gittel Kohn（家庭亲属，非学术白名单关系）；H. Hohenberg 之外的 DFT 后续引用者、访客与荣誉授予机构均不入库。Kohn 无具名 doctoral students 清单（Majumdar 为正文明载唯一学生），勿脑补。

## 8. 奖项清单

- Oliver E. Buckley Condensed Matter Prize（American Physical Society，1961，半导体物理）
- Davisson–Germer Prize（American Physical Society，1977）
- Feenberg Medal（多体问题贡献）
- National Medal of Science（1988）
- Nobel Prize in Chemistry（1998，与 John Pople 共享）
- Foreign Member of the Royal Society，ForMemRS（1998）
- Austrian Decoration for Science and Art（1999）
- Grand Decoration of Honour in Silver with Star for Services to the Republic of Austria（2008）
- Harvard University Honorary Doctor of Science（2012-05）；另有维也纳/德累斯顿工大/魏茨曼/巴黎 XI 等荣誉博士（infobox，年份多数页面未载，勿写）
- Member：American Academy of Arts and Sciences（1963）/ National Academy of Sciences（1969）/ American Philosophical Society（1994）/ 奥地利科学院荣誉成员（2011）/ International Academy of Quantum Molecular Science

## 9. 机构清单

- 教育：Akademisches Gymnasium（维也纳）；University of Toronto（1945 BA、1946 MA）；Harvard University（1948 PhD）
- 任职：National Research Council of Canada 博士后（哥本哈根短期）；Carnegie Mellon University（1950–1960）；UC San Diego（1960–1979，曾任物理系主任）；Institute for Theoretical Physics, Santa Barbara 创所所长（1979–）；UC Santa Barbara 物理系教授（1984–2016）
- 关联：Bell Labs（半导体物理合作渊源）

## 10. 终审清单

- [ ] 生卒 1923-03-09 / 2016-04-19，享年 93，出生地维也纳、去世地圣巴巴拉家中（颌部癌）
- [ ] 1998 与 Pople 共享；获奖理由按页面口径（电子性质 / DFT 主导作用）
- [ ] Hohenberg / Sham / Luttinger / Majumdar 四组归属准确
- [ ] Van Vleck = influence、Schwinger = 导师——两行不混
- [ ] 战时学位 2½/4 与"禁入化学楼"细节按页面
- [ ] 直引原话逐字核对（对奥地利感情段）；其余间接转述
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Walter_Kohn/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`Walter_Kohn_Oxford_University.JPG` 已就位（250px→500px；图注写明牛津荣誉博士场景）
- [ ] **国籍**：封面顶部明示"奥地利出生·美国"
- [ ] **引语核对**：仅"对奥地利感情"段为页面直引，逐字核对
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
