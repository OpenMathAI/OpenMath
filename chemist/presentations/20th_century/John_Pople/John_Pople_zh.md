# John Pople（约翰·波普尔）立传提示词

> qid=Q233973 · 1925-10-31 – 2004-03-15 · 英国 · 诺贝尔化学奖（1998，与 Walter Kohn 共享）· 英国理论化学家
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/John_Pople/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面头像**：右上角肖像位。`images.txt` 无人物肖像（仅站标图标）、本地 infobox 亦无照片行——用**装饰圆占位**（主色渐变圆 + 姓名首字母），可尝试 Wikipedia REST API `page/summary` 回退查 infobox 原图名，失败则保留装饰圆，**不得使用其他人物照片冒充**。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{square-root-alt}\enspace 量子化学的计算革命\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像位 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「基组展开」母题——大圆由小圆叠加而成，暗示高斯型轨道对分子波函数的逼近。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如模型化学语义框：方法 × 基组 → 系统化学精度；PPP/CNDO/INDO 方法谱系）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir John Anthony Pople（中文惯称：约翰·安东尼·波普尔；头衔 Sir、KBE、FRS）
- **生卒**：1925-10-31 生于英格兰萨默塞特 Burnham-on-Sea → 2004-03-15 逝于美国芝加哥（肝癌），享年 78
- **国籍**：United Kingdom（英国）；1964 年移居美国并终老，**保留英国国籍**（正文口径）
- **身份**：理论化学家；自认"更像数学家而非化学家"（页面口径），而理论化学家视其为最重要的同行之一
- **家庭**：1952 年娶 Joy Bowers，直至她 2002 年因癌症去世；身后有女儿 Hilary 与儿子 Adrian、Mark、Andrew；基督徒
- **教育轨迹**：
  - Bristol Grammar School
  - 1943 年获奖学金入 Trinity College, Cambridge；1946 年 BA
  - 1945–1947 任职于 Bristol Aeroplane Company（飞机公司）
  - 返剑桥后 1951 年获**数学**博士学位（lone pair electrons）
- **导师**：John Lennard-Jones（博士导师）
- **博士**：1951，剑桥数学博士；infobox 论文 *Lone Pair Electrons*
- **研究领域**：理论化学 / 量子化学 / 计算化学——水分子统计力学、NMR 理论、半经验 MO 方法、从头算电子结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **萨默塞特少年（1925）**：Burnham-on-Sea 出身，Bristol Grammar School 起步；1943 年凭奖学金入剑桥三一学院。
2. **战时插曲（1945–1947）**：学位之间在 Bristol Aeroplane Company 工作两年——数学家的工业间隙。
3. **数学博士（1951）**：师从 John Lennard-Jones，以孤对电子（lone pair electrons）获数学博士——分子中的电子结构是他一生的主战场。
4. **水的统计力学**：早期关于水分子统计力学的论文——据 Michael J. Frisch 的评价（页面转述），"多年间一直是标准"。
5. **NMR 理论先行者**：核磁共振早期研究底层理论；1959 年与 W.G. Schneider、H.J. Bernstein 合著教科书 *High Resolution Nuclear Magnetic Resonance*。
6. **PPP 方法（Pariser–Parr–Pople）**：与 Pariser、Parr 各自独立发展出同一 π 电子体系近似 MO 方法——三人名字合称 Pariser–Parr–Pople method。
7. **CNDO/INDO（1965 起）**：完全忽略/中间忽略微分重叠方法——三维分子近似 MO 计算的系统方案；1970 年与 David Beveridge 合著 *Approximate Molecular Orbital Theory*。
8. **从头算革命**：以 Slater 型或**高斯型轨道**基组逼近波函数的 ab initio 方法——早期计算极其昂贵，高速微处理器的到来使其可行。
9. **Gaussian 程序**：最广泛使用的计算化学软件包之一的核心开发者；**Gaussian 70** 第一版的共同作者之一。
10. **模型化学（model chemistry）**：他最重要的原创贡献之一——让一种方法在一**系列分子**上被严格评估（G1、G2 复合方法由此而来）。
11. **Gaussian 的告别与争议（1991）**：停止参与 Gaussian 开发；数年后与开发者另起 Q-Chem——其离开及随后多位知名科学家（包括他本人）被禁止使用该软件，在量子化学界引发相当争议（页面口径）。
12. **1998 诺贝尔化学奖**：与 Walter Kohn 共享——表彰其在**量子化学计算方法**上的发展（页面口径："for his development of computational methods in quantum chemistry"）。
13. **身后与纪念**：2003 年封 KBE；2004 年 3 月 15 日病逝芝加哥；家人依其遗愿于 2009-10-05 将诺贝尔奖章赠予 Carnegie Mellon University；Bristol Grammar School 有以其命名的 IT 教室与奖学金，匹兹堡超算中心有以其命名的超级计算机。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绛紫 burgundy） | `#7E1E23` | 剑桥绛红与数学家的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（从头算 badgeAbInitio） | `#2F5D8A` | 蓝ab initio / Gaussian 程序 |
| 分类色 2（半经验方法 badgeSemi） | `#B4762E` | 琥珀 PPP / CNDO / INDO |
| 分类色 3（水与 NMR badgeEarly） | `#3E6B4A` | 绿水的统计力学 / NMR 理论 |
| 分类色 4（模型化学 badgeModel） | `#6E4A2B` | 褐model chemistry / G1、G2 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），基组叠加的层次感。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（清单指定文件 `16-xBLYHNv7C4Q-Lonesome...wav`；如目录内尚无软链则从 music_audio 软链，不要复制 wav）
- **风格**：忧伤 / 沉思 / 电影感
- **匹配理由**：
  - 沉思气质匹配"更像数学家"的孤独理性与模型化学的严谨
  - 忧伤底色匹配其暮年——Gaussian 争议、2002 年丧妻、2004 年病逝
  - 电影感匹配从战时飞机工厂到量子化学软件帝国的时代跨度
- **时长**：以曲目实际时长为准（> 15 页 × 7 秒即由 ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 量子化学的计算革命 / John Pople 1925–2004 + 四色 badge + 右上头像位 + 国籍行
02  身份信息页（★ 必做）— 左头像位 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  波普尔的一生 — 高斯式时间线（10 节点：1925→1943→1951→1954→1958→1964→1965→1970→1998→2004）
04  萨默塞特与剑桥 (1925–1951) — 表格「时间|事件|结果」（奖学金 / 飞机公司 / 数学博士）
05  水的统计力学与 NMR — 表格「问题|方法|结果」+ 公式框：水分子统计力学语义框
06  半经验方法谱系 (1950s–1965) — 表格「问题|方法|结果」+ 公式框：PPP → CNDO → INDO
07  从头算与基组 — 表格「挑战|方法|结果」+ 公式框：高斯型轨道基组语义框
08  Gaussian 与模型化学 — 表格「问题|方法|结果」+ 公式框：model chemistry（G1/G2）
09  1998 诺贝尔化学奖 — 表格「得主|贡献|份额」（与 Kohn 共享；Pople 半项理由按页面口径）
10  学生与传承 — 表格「人物|方向|结果」（Buckingham / Head-Gordon / M. S. Gordon / Raghavachari）
11  荣誉与年表 — 高斯式「类别|代表|意义」表格（Mayhew 1948 / FRS 1961 / Langmuir 1970 / Davy 1988 / Wolf 1992 / Copley 2002 / KBE 2003）
12  告别 Gaussian — 高斯式事件页（1991 停止参与 → Q-Chem → 禁用争议 → 身后奖章归档 CMU）
13  遗产：计算化学的日常 — 四分类遗产盒 + 公式框：从纸笔到软件
14  结尾 — 「他让每一个化学家，都拥有一台可以求解薛定谔方程的机器。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 与 Kohn 分工 | Kohn 是 **DFT 理论框架**；Pople 是**量子化学计算方法**——1998 共享但贡献方向不同，勿混写；Pople 半项理由按页面口径 "for his development of computational methods in quantum chemistry" |
| 博士学科 | 1951 博士学位是**数学**（mathematics）博士——勿写化学博士；infobox 论文 *Lone Pair Electrons* |
| 论文主题两说 | Research 节称"水的统计力学"是博士论文课题（Lennard-Jones 指导）；infobox 论文题为 *Lone Pair Electrons*——两处口径并存，行文以 infobox 题名为准、Research 节表述作补充并注明，勿强行合并 |
| "更像数学家" | 页面口径 "Pople considered himself more of a mathematician than a chemist"——可写但注明为页面转述 |
| Frisch 评价 | 水论文"多年是标准"是**页面转述 Frisch 的评价**，非 Pople 自述——归因勿错 |
| PPP 方法 | Pariser、Parr 与 Pople **各自独立**发展出同一方法——勿写"师承"或"合作"；方法名三姓合称 |
| Gaussian 争议 | 页面口径：1991 年停止参与；数年后与开发者另建 Q-Chem；其离开与多位知名科学家被禁用软件引发"相当争议"（considerable controversy）——按页面克制表述，不加判词 |
| 妻子与子女 | Joy Bowers 1952 年结婚、2002 年因癌症去世；子女 Hilary（女）/Adrian/Mark/Andrew——未具名子女不入库 |
| 奖章去向 | 诺贝尔奖章 2009-10-05 由家人按其遗愿赠予 Carnegie Mellon University——日期与流向准确 |
| KBE 年份 | 2003 年封 Knight Commander (KBE)——勿与 1988 Davy、2002 Copley 混淆 |
| 学生名单 | 博士生四人：A. David Buckingham / Martin Head-Gordon / Mark S. Gordon / Krishnan Raghavachari（infobox 明载）——以此为准，勿增删 |
| 引语 | 本地页面**无 Pople 直接引语**——全部改间接转述，禁止编造引号原话 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q233973 | ✅ |
| name_zh | 约翰·波普尔 | ✅ |
| name_en | John Pople | ✅ |
| birth_date | 1925-10-31 | ✅ |
| death_date | 2004-03-15 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | theoretical chemistry（person_field 细分：quantum chemistry / computational chemistry / ab initio methods / semi-empirical methods，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Lennard-Jones | 师→生（博士导师） | 剑桥数学博士（1951）导师 |
| advisor-student | A. David Buckingham | Pople→学生 | infobox Doctoral students |
| advisor-student | Martin Head-Gordon | Pople→学生 | infobox Doctoral students |
| advisor-student | Mark S. Gordon | Pople→学生 | infobox Doctoral students |
| advisor-student | Krishnan Raghavachari | Pople→学生 | infobox Doctoral students |
| co-honored | Walter Kohn | 无向 | 1998 诺贝尔化学奖共享 |
| colleague | Rudolph Pariser | 无向 | Pariser–Parr–Pople 方法（各自独立发展 π 电子近似 MO 方法） |
| colleague | Robert G. Parr | 无向 | Pariser–Parr–Pople 方法（各自独立发展 π 电子近似 MO 方法） |
| colleague | William G. Schneider | 无向 | 1959 合著教科书 High Resolution Nuclear Magnetic Resonance |
| colleague | H.J. Bernstein | 无向 | 1959 合著教科书 High Resolution Nuclear Magnetic Resonance（页面作 H.J. Bernstein） |
| colleague | David Beveridge | 无向 | 1970 合著 Approximate Molecular Orbital Theory |
| spouse | Joy Bowers | 无向 | 1952 结婚；2002 年因癌症去世 |

> 禁入库名单：子女 Hilary/Adrian/Mark/Andrew（家庭亲属，非学术白名单关系）；Michael J. Frisch（评价转述者，非合作者）；1986 年 *Ab initio molecular orbital theory* 合著者 Warren Hehre / Leo Radom / Paul v.R. Schleyer——行文可提及但**默认不入库**以控制噪声，Review 如需补入为 colleague 再议。

## 8. 奖项清单

- Mayhew Prize（1948）
- Smith's Prize（年份页面未载，勿写）
- Fellow of the Royal Society，FRS（1961）
- Irving Langmuir Award in Chemical Physics（1970）
- Davy Medal（1988）
- Wolf Prize in Chemistry（1992）
- Nobel Prize in Chemistry（1998，与 Walter Kohn 共享）
- Copley Medal（2002）
- Knight Commander of the Order of the British Empire，KBE（2003）
- ACS Award in Theoretical Chemistry / Marlow Award / Centenary Prize / Humboldt Prize 等（infobox 有载、年份页面未载——行文勿写年份）
- International Academy of Quantum Molecular Science 创始成员

## 9. 机构清单

- 教育：Bristol Grammar School；Trinity College, University of Cambridge（1943 奖学金入学；1946 BA；1951 PhD）
- 任职：Bristol Aeroplane Company（1945–1947）；Trinity College research fellow；剑桥数学系讲师（1954–）；National Physical Laboratory 基础物理部主任（1958–）；Carnegie Mellon University（1964–1993；1961–1962 曾学术休假）；Northwestern University（1993–2004，Trustees Professor of Chemistry）
- 纪念：Bristol Grammar School 的 Pople IT 教室与奖学金；Pittsburgh Supercomputing Center 的 Pople 超级计算机

## 10. 终审清单

- [ ] 生卒 1925-10-31 / 2004-03-15，享年 78，出生地 Burnham-on-Sea、去世地芝加哥（肝癌）
- [ ] 1998 与 Kohn 共享；Pople 半项理由按页面口径（量子化学计算方法）
- [ ] 数学博士（1951）与论文两说处理准确
- [ ] 博士生四人名单与 infobox 一致；PPP 三人独立归因准确
- [ ] Gaussian 争议表述克制、按页面口径
- [ ] 引语零编造（页面无直接引语，全部间接转述）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Pople/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 无肖像——装饰圆占位，图注不得虚构照片来源
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：页面无直接引语，任何带引号的"原话"都必须删除
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像位 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
