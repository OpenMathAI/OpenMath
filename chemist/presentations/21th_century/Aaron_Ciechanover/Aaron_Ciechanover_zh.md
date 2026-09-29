# Aaron Ciechanover（阿龙·切哈诺沃）立传提示词

> qid=Q233205 · 1947-10-01 生于以色列海法（在世，卒日留白） · 以色列生物学家/生物化学家 · 21 世纪 · 诺贝尔化学奖（2004，与 Avram Hershko、Irwin Rose 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Aaron_Ciechanover/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金框公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像：images.txt 无真人照片 URL——执行时先经 Wikipedia REST API `/page/summary/Aaron_Ciechanover` 查 infobox 原图名（页面有 "Ciechanover in 2023" 照片）下载（500px）；404 则用装饰圆占位，并在 Review-1 记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{recycle}\enspace 蛋白质回收系统的解密者\enspace·\enspace 以色列`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（以色列 | Technion | 泛素介导的蛋白质降解）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（含希伯来文 אהרן צ'חנובר）、国籍、出生地、教育（希伯来大学 MS/MD 1974 / Technion DSc 1981）、博士后（MIT Whitehead）、核心领域、现任（Technion 杰出研究教授）、荣誉。事实取自本地 page.md infobox，不得杜撰；在世——卒栏写「在世（1947– ）」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「泛素标签 / 蛋白酶体降解」母题——离散圆点暗示被标记待降解的蛋白链。
5. **表格语义化 + 公式框**（★ 高斯/Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——泛素缀合 = 蛋白质降解的「死刑标签」、1978 热稳定多肽因子（APF-1=泛素）即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Aaron Ciechanover（中文惯称：阿龙·切哈诺沃；希伯来文：אהרן צ'חנובר）
- **生卒**：1947-10-01 生于海法（在世，卒日页面无载——全篇卒处一律留白）
- **国籍**：Israel（以色列）
- **身份**：生物学家/生物化学家；Technion（以色列理工学院）Ruth and Bruce Rappaport 医学院杰出研究教授
- **家庭**：犹太家庭；母 Bluma（娘家姓 Lubashevsky）为英语教师，父 Yitzhak 为律师事务所职员——双亲 1920 年代自波兰移民以色列；配偶 Menucha Ciechanover（infobox）
- **教育轨迹**：
  - 高中毕业加入学术预备役（Atuda）→ Hebrew University of Jerusalem 学医
  - 希伯来大学：科学硕士（1971）、MD（1974）
  - Technion – Israel Institute of Technology：生物化学 DSc（1981）
- **师承**：博士后导师 Harvey Lodish（1981–1984，MIT Whitehead Institute）
- **研究领域**：生物学/生物化学——泛素介导的蛋白质降解、蛋白质稳态、药物靶向

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **海法之子（1947）**：波兰移民教师的儿子，生于建国前一年的海法——以色列第一代科学家的缩影。
2. **预备役与学医（1960s–1974）**：Atuda 学术预备役进入希伯来大学；1971 硕士、1974 MD。
3. **Technion 博士（1981）**：海法理工学院生物化学 DSc——此后终生扎根 Technion。
4. **MIT 岁月（1981–1984）**：Whitehead 研究所 Harvey Lodish 实验室博士后——带回细胞生物学的视野。
5. **1978 关键论文**：与 Y. Hod、Hershko 发表网织红细胞 ATP 依赖蛋白降解系统的热稳定多肽组分（BBRC）——**他的名字在该文中被从希伯来文误拼为 "Ciehanover"**（页面明载）。
6. **1980 缀合论文**：PNAS 发表 ATP 依赖的网织红细胞蛋白与降解所需多肽的缀合——泛素系统的生化奠基作之一。
7. **1982/1998 综述**：与 Hershko 先后在 Annual Review of Biochem 发表胞内蛋白分解机制与 THE UBIQUITIN SYSTEM——领域定名的里程碑。
8. **泛素-蛋白酶体途径**：细胞用泛素「贴标签」标记待降解蛋白，蛋白酶体执行降解——维持细胞稳态； believed 与癌症、肌肉与神经疾病、免疫与炎症反应的发生发展相关（页面口径 believed to be involved，勿写成定论）。
9. **2000–2004 奖项链**：Lasker 基础医学研究奖（2000）→ 以色列奖生物学（2003）→ **2004 诺贝尔化学奖**（与 Hershko、Rose，发现泛素介导的蛋白质降解）。
10. **以色列首批科学诺奖**：页面作 "one of Israel's first Nobel Laureates in science"——是 Technion 历史的中心篇章。
11. **全球学术身份**：以色列科学院、教廷科学院、乌克兰国家科学院、俄罗斯科学院成员，美国国家科学院外籍会员——五院之身。
12. **东方讲学与建院**：2008 台湾成功大学杰出访问讲座教授（后获名誉博士）；2018 在香港中文大学（深圳）开设切哈诺沃精准与再生医学研究院（深圳「诺奖得主实验室」计划）。
13. **产业与公益**：Rosetta Genomics（主席）等多家公司科学顾问；Patient Innovation 顾问委员会；2016 演讲平壤科技大学（页面仅一句记载，客观带过）。

## 3. 配色方案（高斯/Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deeppurple） | `#46356B` | 蛋白酶体降解的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（泛素系统 badgeUb） | `#2E5A9E` | 蓝泛素标签 / 缀合反应 |
| 分类色 2（蛋白酶体 badgeProt） | `#1B7A43` | 绿降解与回收 / 细胞稳态 |
| 分类色 3（医学转化 badgeMed） | `#D97B29` | 琥珀癌症与药物靶向 / 疾病关联 |
| 分类色 4（以色列科学 badgeIL） | `#C0395B` | 玫瑰 Technion / 以色列奖 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「泛素标签贴附—蛋白酶体粉碎」的循环。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`，不要复制 wav 文件，Makefile 里直接引用该路径）
- **风格**：明亮 / 上升 / 破晓感
- **匹配理由**：
  - "破晓" 匹配发现史——从一个「模糊的想法」（其诺奖演讲标题语 "From a vague idea..."，页面明载）到照亮细胞回收机制的日光
  - "上升" 匹配其轨迹——海法 → 耶路撒冷 → 波士顿 → 重返海法登上世界之巅，并引领以色列科学走上诺奖版图
  - 转化医学的乐观基调：把降解机制变成药物靶点
- **时长**：以实际 wav 为准，> 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 蛋白质回收系统的解密者 / Aaron Ciechanover 1947– + 四色 badge + 右上头像 + 国籍行（以色列）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名含希伯来文/国籍/教育/博士后/任职/领域/荣誉）
03  切哈诺沃之路 — Sanger 式时间线（10 节点：1947→1971→1974→1978→1980→1981→1984→2000→2003→2004/2018）
04  海法之子：从预备役到 MD (1947–1974) — 表格「时间|事件|结果」
05  Technion 博士与 MIT 岁月 (1974–1984) — 表格「阶段|环境|结果」
06  1978 热稳定多肽因子 — 表格「问题|方法|结果」+ 公式框：ATP 依赖降解系统的热稳定组分（误拼 Ciehanover 注记）
07  泛素缀合与系统定名 (1980–1998) — 表格「问题|方法|结果」+ 公式框：泛素「贴标签」→ 蛋白酶体降解
08  细胞稳态与疾病 — 表格「系统|功能|疾病关联」（页面 believed 口径）
09  2004 诺贝尔化学奖 — 金框页（与 Hershko、Rose 三人共享；发现泛素介导的蛋白质降解）
10  以色列首批科学诺奖 — 高斯 FFT 页式流程图（海法 → Technion → 以色列奖 2003 → 诺奖 2004 → Technion 历史）
11  五院之身与全球讲学 — 表格「机构|身份|年份」（以/教廷/乌克兰/俄/美国 NAS 外籍；成大 2008）
12  东方建院 — 表格（CUHK Shenzhen 2018 精准与再生医学研究院；深圳诺奖实验室计划）
13  产业与公益 — 高斯式「类别|代表|意义」表格（Rosetta Genomics 主席 / Patient Innovation / 荣誉博士群）
14  结尾 — 「细胞知道何时拆解自己——他们找到了那张标签。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2004 奖项口径 | **三人共享**：Ciechanover、Avram Hershko、Irwin Rose——发现泛素介导的蛋白质降解；Ciechanover 与 Hershko 互指一致、Rose 用规范名 "Irwin Rose"（在 chem21-batch-03，防分裂用其页面规范名） |
| 官方 citation | **本地页面未载官方 citation 英文全句**——可用的页面表述为 "for his discovery with Avram Hershko and Irwin Rose, of ubiquitin-mediated protein degradation"；勿编造 "for the discovery of ubiquitin-mediated protein degradation" 的单人官方口径 |
| 「以色列第一位」 | 页面作 "**one of** Israel's first Nobel Laureates in science"——勿写「以色列第一位科学诺奖得主」 |
| 博士导师 | 页面只载 1981 年 Technion DSc，**未明载博士导师是 Hershko**——勿建 Ciechanover→Hershko 的 advisor-student（二人关系用 colleague + co-honored） |
| 名字误拼 | 1978 BBRC 论文署名 "Ciehanover"（自希伯来文误拼）——页面明载，可作为 §7 公式框旁注，勿写错本篇正文 |
| 疾病关联 | 泛素-蛋白酶体途径与癌症等疾病是 "**believed to be involved**"——勿写成「已证实导致」 |
| 平壤讲学 | 2016-05 在朝鲜平壤科技大学演讲——页面仅一句记载，客观带过，不做延伸 |
| 荣誉博士群 | 特拉维夫/希伯来/巴伊兰/本古里安/华沙/海法/雅典/华中科大/罗兹等 honorary doctor 皆 infobox 载——列清单页勿逐个展开 |
| 引语红线 | 本地页面**无直接引语**——诺奖演讲标题 *Intracellular Protein Degradation: From a Vague Idea thru the Lysosome and the Ubiquitin-Proteasome System and onto Human Diseases and Drug Targeting*（页面 External links 明载）可作标题引用，其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q233205 | ✅ |
| name_zh | 阿龙·切哈诺沃 | ✅ |
| name_en | Aaron Ciechanover | ✅ |
| birth_date | 1947-10-01 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Israel | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：ubiquitin-mediated protein degradation / biochemistry / molecular biology，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**合作者 / 共同得主 / 师长 / 配偶**（仅 page.md 正文或 infobox 明载者；metadata.json 无关系字段，无 metadata-only 禁入库项）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Avram Hershko | 无向 | Technion 长期合作者；1978/1980/1982/1998 共同论文 |
| co-honored | Avram Hershko | 无向 | 2004 诺贝尔化学奖共同得主 |
| co-honored | Irwin Rose | 无向 | 2004 诺贝尔化学奖共同得主（规范名 Irwin Rose，对方在 chem21-batch-03） |
| advisor-student | Harvey Lodish | 师→生（博士后导师） | 1981–1984 MIT Whitehead 研究所博士后 |
| spouse | Menucha Ciechanover | 无向 | 妻（infobox） |
| parent-child | Yitzhak Ciechanover | 父→子 | 律师事务所职员，1920 年代自波兰移民 |
| parent-child | Bluma Ciechanover | 母→子 | 英语教师，娘家姓 Lubashevsky |

> **不建项说明**：页面未明载 Ciechanover 的博士导师（勿写 Hershko 为博士导师）；论文合著者 Y. Hod / H. Heller / S. Elias / A.L. Haas 为一次性合著，不入库（避免噪声 stub）；产业顾问公司与 Patient Innovation 非人物关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（2004，与 Hershko、Rose 三人共享；口径见 §5）
- Albert Lasker Award for Basic Medical Research（2000）
- EMET Prize（2002，infobox）
- Israel Prize（2003，生物学）
- Golden Plate Award，American Academy of Achievement（2005）
- Sir Hans Krebs Medal（2006）
- Honorary DSc，NCKU Taiwan（2008）；University of Cambodia 荣誉博士（2009）
- Humboldt Prize（2011）
- German Academy of Sciences Leopoldina 院士（2016）
- Centenary Prize（infobox 另载）；特拉维夫/希伯来/巴伊兰/本古里安/华沙/海法/雅典/华中科大/罗兹等荣誉博士

## 9. 机构清单

- 教育：Hebrew University of Jerusalem（MS 1971、MD 1974；Atuda 学术预备役）→ Technion（DSc 生物化学 1981）
- 任职：MIT Whitehead Institute Lodish 实验室博士后（1981–1984）→ Technion Ruth and Bruce Rappaport 医学院杰出研究教授（现任）
- 学术成员：Israel Academy of Sciences and Humanities、Pontifical Academy of Sciences、乌克兰国家科学院、俄罗斯科学院、美国 NAS 外籍会员、Leopoldina（2016）
- 讲座/建院：NCKU Taiwan 访问杰出讲座教授（2008）；Ciechanover Institute of Precision and Regenerative Medicine，CUHK Shenzhen（2018）

## 10. 终审清单

- [ ] 生卒 1947-10-01 / 在世留白，出生地海法
- [ ] 2004 三人共享（Hershko/Rose）表述准确；无编造官方 citation
- [ ] "one of Israel's first" 口径准确；未写「第一位」
- [ ] 未建 Ciechanover→Hershko advisor-student；1978 误拼注记准确
- [ ] 疾病关联用 believed 口径；平壤/政治内容仅一句客观
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Aaron_Ciechanover/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：REST API 查 infobox 原图下载（500px）；404 则装饰圆占位并记录
- [ ] **国籍**：封面顶部明示以色列
- [ ] **引语核对**：除诺奖演讲标题外应无引号原话
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 21 世纪批次各篇格式对齐
