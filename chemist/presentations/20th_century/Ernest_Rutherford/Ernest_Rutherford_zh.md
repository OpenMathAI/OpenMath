# Ernest Rutherford（欧内斯特·卢瑟福）立传提示词

> qid=Q9123 · 1871-08-30 – 1937-10-19 · 新西兰物理学家 / 化学家（核物理之父）· 20 世纪 · 诺贝尔化学奖（1908，表彰他对元素蜕变及放射性物质化学的研究）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Ernest_Rutherford/`（page.md + metadata.json + page.html + images.txt；images.txt 含 1892 年真实肖像 URL）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Ernest_Rutherford_1892.jpg` 由 images.txt 第 2 条 URL 下载，250px thumb 改 500px 以上）。infobox 注明 "Rutherford, c. 1920s"，正文配图为 1892 年照片——图注按实际下载文件标注年份。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 核物理之父\enspace·\enspace 新西兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。注意：**物理学家获诺贝尔化学奖**这一身份张力须在封面或身份页呈现。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、师承、任职、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「散射」母题——稀疏圆点如 α 粒子穿过金箔后偶发的大角偏转。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ernest Rutherford, 1st Baron Rutherford of Nelson（中文惯称：欧内斯特·卢瑟福；头衔缩写 OM FRS；The Right Honourable The Lord Rutherford of Nelson）
- **生卒**：1871-08-30 生于新西兰尼尔森省 Brightwater（殖民地时期）→ 1937-10-19 逝于剑桥（英国），享年 66；安葬伦敦威斯敏斯特教堂，近牛顿与达尔文
- **国籍**：New Zealand（新西兰；page.md 称其为 New Zealand physicist）
- **身份**：物理学家兼化学家，原子物理与核物理先驱；第 44 任皇家学会会长（1925–1930）；1931 年受封男爵（Baron）
- **家庭**：十二个孩子中的第四个；父 James Rutherford 为自苏格兰珀斯移民的农民兼机械师，母 Martha Thompson 为自英格兰 Hornchurch 来的教师；出生证明误写为 'Earnest'，家人昵称 Ern。1900 年在基督城 Papanui 的 St Paul's Anglican Church 娶 Mary Georgina Newton（1876–1954，婚前已订婚）；独女 Eileen Mary（1901–1930）嫁物理学家 Ralph Fowler，因生第四胎去世。女婿 Ralph Fowler
- **教育轨迹**：
  - 5 岁入 Foxhill School；1883（11 岁）随家迁 Havelock，入 Havelock School
  - 1887（第二次尝试）获奖学金入 Nelson College（1887–1889，580/600 分，1889 head boy，橄榄球队）
  - 1889（第二次尝试）获奖学金入 Canterbury College（新西兰大学，1890–1894）：1892 BA（拉丁语、英语、数学）、1893 MA（数学与物理科学）、1894 BSc（化学与地质学）
  - 1895 获 1851 Research Fellowship 赴剑桥卡文迪许实验室；1897 获剑桥 B.A. Research Degree 与三一学院 Coutts-Trotter Studentship
- **导师**：Alexander Bickerton（Canterbury College）与 J. J. Thomson（卡文迪许；Cambridge 首批 "aliens"——无剑桥学位而可做研究者之一）
- **博士论文**：page.md 无载——禁写
- **研究领域**：原子物理、核物理、放射化学（infobox Fields）；另涉无线电通信与超声

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **新西兰十二子之四（1871）**：移民农民与教师之子，两次靠奖学金层层晋级——殖民地天才的上升通道。
2. **无线电与师从 Thomson（1895–1898）**：检出 0.5 英里（800 m）外无线电波，一度保持电磁波检出距离世界纪录；1896 英国科学促进会会议上发现已被 Marconi（近 10 英里）超越。
3. **X 射线与铀放射性（1896–1899）**：随 Thomson 研究 X 射线对气体的导电效应（通往电子发现）；闻 Becquerel 铀实验后转向放射性，发现两种穿透力不同于 X 射线的辐射。
4. **α / β 射线命名（1899，加拿大）**：在 McGill 期间首创 "alpha ray" 与 "beta ray" 两词。
5. **McGill 岁月（1898–1907）**：经 Thomson 推荐任 Macdonald 讲席物理教授；与 Geiger 发展硫化锌闪烁屏与电离室计数 α 粒子，测得 α 粒子电荷为 2。
6. **与 Soddy：蜕变理论（1900–1903）**：钍的放射性 "射气" 命名 thoron（后知为 ²²⁰Rn）；发现半衰期——与 R.B. Owens 发现任何尺寸放射性样品总在相同时间衰变一半（thoron 为 11½ 分钟），首创 "half-life" 一词；1902/1903 发表 "Law of Radioactive Change"，证明放射性是原子自发蜕变为其他物质的过程——彻底动摇 "原子不可毁灭" 的信条。
7. **γ 射线命名（1903）**：识别 Villard 1900 年发现但未命名的第三种辐射，命名为 gamma ray——α/β/γ 三词沿用至今。
8. **1904 放射性与地球年龄**：在 Kelvin 在场的讲演中指出放射性可解释太阳长期能量来源，化解 Kelvin "地球太年轻" 之争。
9. **1908 诺贝尔化学奖——物理学家的化学奖**：官方理由 "for his investigations into the disintegration of the elements, and the chemistry of radioactive substances"；1907 年回英国任曼彻斯特维多利亚大学 Langworthy 讲席教授，获奖时主业仍是物理学家。
10. **α 粒子 = 氦核（1907–1909）**：与 Thomas Royds 让 α 粒子穿过薄窗进入抽真空管，随放电光谱逐渐呈现氦的特征谱线，证明 α 粒子是电离氦原子（很可能是氦核）。
11. **金箔实验与原子核（1909–1911）**：在其指导下 Geiger 与 Marsden 用 α 粒子轰击金箔发现罕见大角散射；他对此的解读提出原子电荷集中于极小核——原子核理论诞生（1911 论文 "The Scattering of α and β Particles by Matter and the Structure of the Atom"）。
12. **人工核反应与质子（1917–1920）**：α 粒子轰击氮核实现首例人工核反应（¹⁴N + α → ¹⁷O + p，氧产物由 Blackett 证实）；被击出的 "氢原子" 1920 年被正式命名为 proton；同年在 Bakerian Lecture 中提出中子概念，1932 年由 Chadwick 证实。
13. **卡文迪许掌门（1919–1937）**：继 Thomson 任 Cavendish 教授直至去世；任内 Chadwick 发现中子（1932，1935 诺奖）、Cockcroft 与 Walton 实现加速器 "splitting the atom"（1932，1951 诺奖）、Appleton 证实电离层（诺奖）——门生诺奖成群。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#14324F` | 卡文迪许 / 精密实验的严谨与深度（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（α/β/γ 三射线 badgeRays） | `#B23A48` | 红 α/β 命名（1899）/ γ 命名（1903） |
| 分类色 2（蜕变与半衰期 badgeDecay） | `#2E6E4E` | 绿放射性蜕变 / half-life / 与 Soddy 合作 |
| 分类色 3（原子核 badgeNucleus） | `#3B5BA5` | 蓝金箔实验 / 核式模型（1911） |
| 分类色 4（质子中子与传承 badgeParticles） | `#C8862A` | 金橙人工核反应 / 质子 / 卡文迪许门生 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「散射」——绝大多数 α 粒子径直穿过，极少数撞上原子核偏转。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（本地文件 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`）
- **风格**：史诗 / 开阔 / 高受众
- **匹配理由**：
  - "新大陆" 匹配其科学气质——从原子内部开辟全新疆域（原子核 → 人工核反应 → 质子），核物理因他而得名
  - "开阔" 匹配空间叙事——从新西兰殖民地到剑桥卡文迪许，横跨 McGill / Manchester / Cambridge 三站的远征式人生
  - "时代转折" 匹配其历史地位——"father of nuclear physics"、1933 Times 讲话启发了 Szilárd 的链式反应构想（尽管他本人断言原子能 "moonshine"），时代在他身后转向
- **时长对齐**：BGM 略短于 slides 总时长时 ffmpeg `-shortest` 自动对齐
- **注意**：wav 复制在执行立传阶段进行（`cp` 到 `Ernest_Rutherford/` 子目录），本提示词阶段不复制

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 核物理之父 / Ernest Rutherford 1871–1937 + 四色 badge + 右上头像 + 国籍行（新西兰·物理学家获化学奖）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/师承/任职/出生地/去世地/领域/荣誉）
03  卢瑟福的一生 — 高斯式时间线（10 节点：1871→1895→1899→1903→1907→1908→1911→1917→1919→1937）
04  早年：新西兰十二子之四 (1871–1894) — 表格「时间|事件|结果」（Nelson College→Canterbury 三学位）
05  剑桥与师承：Thomson 门下 (1895–1898) — 表格「阶段|工作|结果」+ 公式框：无线电 0.5 英里纪录
06  McGill 岁月：α/β 命名与半衰期 (1898–1907) — 表格「问题|方法|结果」+ 公式框：half-life（thoron 11½ min）
07  与 Soddy：蜕变理论 (1900–1903) — 表格「旧观念|新事实|影响」+ 公式框：原子自发蜕变；γ 命名 1903
08  1908 诺贝尔化学奖 — 物理学家的化学奖 — 表格「年份|奖项|理由」+ 公式框：α 粒子 = 氦核（与 Royds）
09  Manchester：金箔实验与原子核 (1907–1911) — 表格「实验|观察|结论」+ 公式框：核式原子（1911 论文）
10  人工核反应与质子 (1913–1920) — 表格「发现|年份|意义」+ 公式框：¹⁴N + α → ¹⁷O + p
11  卡文迪许掌门 (1919–1937) — 表格「人物|成就|年份」（Chadwick 中子 / Cockcroft-Walton / Appleton）
12  门生与传承 — 表格「人物|方向|结果」（Bohr 模型 / Blackett / Moseley / Fowler 女婿）
13  荣誉与遗产 — 高斯式「类别|代表|意义」表格（Rumford 1904 → Nobel 1908 → Copley 1922 → OM 1925 → Baron 1931）+ rutherfordium 1997 + 新西兰 100 元纸币
14  结尾 — 金句收束（用 page.md 实载的 "talking moonshine" 语段或 Jeans 1938 悼词间接转述，勿杜撰）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| **物理学家获化学奖（P0）** | 1908 年诺奖是**化学奖**，而其主要身份是**物理学家**——这一张力是本篇母题；获奖理由为元素蜕变与放射性物质化学。勿写成诺贝尔物理学奖 |
| 诺奖理由措辞 | 中文照总名单：**"表彰他对元素蜕变及放射性物质化学的研究"**；英文 "for his investigations into the disintegration of the elements, and the chemistry of radioactive substances"——勿写成"发现原子核"（那是 1911，在获奖**之后**） |
| 1908 独享、无 co-honored | 1908 化学奖一人独得；勿与 Soddy 混为共同得主（Soddy 1921 才因同位素获化学奖） |
| 原子核时序 | 金箔实验 1909（Geiger–Marsden 执行）→ 1911 提出原子核——**均在 1908 获奖之后**，勿倒置为"因发现原子核获奖" |
| 射线命名归属 | α/β 由卢瑟福 **1899** 命名；γ 由卢瑟福 **1903** 命名（Villard 1900 发现但未命名）——发现者与命名者勿混；勿写"发现 γ 射线" |
| Thorium X 同位素 | page.md 载 Thorium X "later identified as ²²⁴Rn"——**照 page.md 抄写**或规避该同位素编号；thoron 后知为 ²²⁰Rn（radon 同位素）勿写错 |
| 半衰期合作者 | 半衰期概念是卢瑟福与 **R.B. Owens** 研究 thoron 时确立（11½ 分钟）；"Law of Radioactive Change" 是与 **Soddy** 发表——两组合作勿互换 |
| α=氦证明 | 与 **Thomas Royds**（1907 底开始、1909 发表）证明 α 粒子是氦（核）；勿写 Geiger |
| Poisson 论文 | 1910 与 Geiger 及数学家 **Harry Bateman** 发射分布论文（今称 Poisson 分布）——Bateman 勿漏、勿误作学生 |
| 质子命名时序 | 1917–1919 轰击氮实验中被击出的粒子先叫 "hydrogen atom"，**1920** 才命名为 proton（确认并扩展了 Wien 1898 的工作）——命名年份勿提前 |
| 中子理论 | 中子概念见其 **1920 Bakerian Lecture**；1932 由 **Chadwick** 证实（1935 诺奖）；勿写卢瑟福"发现中子" |
| sonar 误解 | page.md 明言 "卢瑟福发明声呐" 是**误解**：一战潜艇探测用了压电效应（与 Langevin 各自提出）、他做了测量装置，但换能器是 Langevin 的——立传须照此口径或规避 |
| 无线电纪录 | 检出距离 0.5 英里（800 m），1896 年被 Marconi（近 10 英里/16 km）超越——方向勿写反 |
| 出生地 | Brightwater（Nelson Province；metadata 另列 Nelson、Spring Grove 别名）——正文用 Brightwater，勿写奥克兰/基督城 |
| 死因细节 | 疝气绞窄 → 伦敦紧急手术 → 四日后卒于剑桥（1937-10-19，"intestinal paralysis"，享年 66）→ Golders Green 火化 → 威斯敏斯特教堂安葬——链条勿压缩为"病逝" |
| 出生证明笔误 | 误写 'Earnest'，家中昵称 Ern——可作花絮，勿写成"改名为 Ernest" |
| 学生入库边界 | **只收 page.md infobox 明确为学生的**：Doctoral students 11 人（Chadwick 1921 / Smyth 1923 / Nazir Ahmed 1925 / Leslie H. Martin 1926 / Cecil Powell 1927 / Cockcroft 1928 / Oliphant 1929 / Feather 1931 / Walton 1931 / Rafi Chaudhry 1932 / Zhang Wenyu 1938）+ Other notable students 15 人；metadata.json `doctoral_student` 另含 Kapitsa、Khariton、Hartree、Harriet Brooks、Appleton、Boyle、Shoenberg、Wynn-Williams、Bates、McAulay、Laurence 等 page.md infobox 无载者——**不予入库**；且 metadata 列表本身有重复（Cockcroft、Marsden、Oliphant、Walton、Smyth 两种拼写均出现两遍） |
| Bohr 身份 | Bohr 在 page.md 是 "other notable students"（1912 应邀加入其实验室，导致 Bohr 模型）——可入库为学生，note 注明非博士 |
| 引语纪律 | 可用引语仅限 page.md 实载三处：金箔 "most incredible event…15-inch shell" 段（注明 "in one of his last lectures, Rutherford was quoted as saying"）、1933-09-12 Times "talking moonshine" 段、Jeans 1938 印度科学大会悼词段——此外一律间接转述；"father of nuclear physics" 与 "the greatest experimentalist since Faraday" 是 Wikipedia 叙述性称呼，可转述勿作原话加引号 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q9123 | ✅ |
| name_zh | 欧内斯特·卢瑟福 | ✅ |
| name_en | Ernest Rutherford | ✅ |
| birth_date | 1871-08-30 | ✅ |
| death_date | 1937-10-19 | ✅ |
| nationality | New Zealand | ✅ |
| primary_occupation | nuclear physicist / chemist | ✅ |
| field_of_work | physics, nuclear physics, chemistry, radioactivity（person_field 细分建议：nuclear physics / radioactivity / atomic physics，带 rank） | ✅ |
| has_biography | 1 | ✅ 执行立传后置 1 |

## 7. 社会关系入库清单

**师长 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | J. J. Thomson | 师→生（卡文迪许导师） | 1895 入剑桥随其研究；X 射线导电效应合作；1919 继其任 Cavendish 教授 |
| advisor-student | Alexander Bickerton | 师→生（本科导师） | Canterbury College（metadata 与 page.md infobox 一致） |
| colleague | Frederick Soddy | 无向 | 1900–1903 McGill 合作，蜕变理论与 "Law of Radioactive Change"（Soddy 为 1921 化学奖得主，非 1908 共同得主） |
| colleague | Hans Geiger | 无向 | 闪烁计数与电离室、Geiger–Marsden 实验、1910 Poisson 分布论文 |
| colleague | Thomas Royds | 无向 | 证明 α 粒子为氦（1907–1909） |
| colleague | R.B. Owens | 无向 | 半衰期发现（thoron 11½ 分钟） |
| colleague | Harry Bateman | 无向 | 1910 发射时间分布（Poisson 分布）论文合作数学家 |
| colleague | Paul Langevin | 无向 | 一战潜艇探测各自提出压电方案（sonar 归 Langevin 换能器） |

**门生（Rutherford → 学生，仅收 page.md infobox 明确者）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James Chadwick | Rutherford → 学生 | 博士 1921；1932 发现中子，1935 诺奖 |
| advisor-student | John Cockcroft | Rutherford → 学生 | 博士 1928；1932 与 Walton 分裂原子，1951 诺奖 |
| advisor-student | Ernest Walton | Rutherford → 学生 | 博士 1931；1951 诺奖 |
| advisor-student | Cecil Powell | Rutherford → 学生 | 博士 1927；1950 诺奖 |
| advisor-student | Mark Oliphant | Rutherford → 学生 | 博士 1929 |
| advisor-student | Henry DeWolf Smyth | Rutherford → 学生 | 博士 1923 |
| advisor-student | Norman Feather | Rutherford → 学生 | 博士 1931 |
| advisor-student | Nazir Ahmed | Rutherford → 学生 | 博士 1925 |
| advisor-student | Leslie H. Martin | Rutherford → 学生 | 博士 1926 |
| advisor-student | Rafi Chaudhry | Rutherford → 学生 | 博士 1932 |
| advisor-student | Zhang Wenyu（张文裕） | Rutherford → 学生 | 博士 1938（infobox 原文年份；卢瑟福 1937 已去世，note 注明） |
| advisor-student | Niels Bohr | Rutherford → 学生（非博士） | 1912 应邀加入实验室；Bohr 模型 |
| advisor-student | Ernest Marsden | Rutherford → 学生（非博士） | 金箔实验执行者之一；Geiger–Marsden |
| advisor-student | Henry Moseley | Rutherford → 学生（非博士） | 1913 共同建立原子序数体系 |
| advisor-student | Patrick Blackett | Rutherford → 学生（非博士） | 证实 ¹⁴N+α 反应氧产物；1948 诺奖 |
| advisor-student | Otto Hahn | Rutherford → 学生（非博士） | infobox other notable students；1944 化学奖 |
| advisor-student | George de Hevesy | Rutherford → 学生（非博士） | infobox other notable students；1943 化学奖 |
| advisor-student | Frederick Soddy | Rutherford → 学生（非博士） | 既是合作者亦列于 other notable students；1921 化学奖 |
| advisor-student | Hans Geiger | Rutherford → 学生（非博士） | 兼列 other notable students（关系类型取 colleague 为主表） |
| advisor-student | Kazimierz Fajans / Charles Drummond Ellis / Charles Galton Darwin / George Gamow / Kenneth Bainbridge / Maria Goeppert Mayer / Philip Burton Moon | Rutherford → 学生（非博士） | infobox other notable students 其余 7 人（Goeppert Mayer 1963 诺奖） |
| other | Ralph Fowler | 无向（女婿） | 物理学家，娶独女 Eileen Mary；metadata 列其为 doctoral_student 但 page.md 仅载姻亲，note 如实注明 |
| other | Mary Georgina Newton | 无向（配偶） | 1900 年结婚 |

> metadata.json `doctoral_student` 共 30 条（含重复），其中 Kapitsa、Yulii Khariton、Douglas Hartree、Harriet Brooks、Robert William Boyle、David Shoenberg、C. E. Wynn-Williams、Leslie Fleetwood Bates、Alexander McAulay、George Laurence、Edward Victor Appleton 等 page.md infobox **无载**——**不予入库**。

## 8. 奖项清单

- Rumford Medal（1904，皇家学会；引文：放射性研究，特别是放射性气体射气的存在与性质）
- **Nobel Prize in Chemistry（1908，独享；"for his investigations into the disintegration of the elements, and the chemistry of radioactive substances"）**
- Elliott Cresson Medal（1910，Franklin Institute；"for distinguished work in electrical theory"）
- Matteucci Medal（1913，Accademia dei XL）
- Hector Memorial Medal（1916，新西兰皇家学会）
- Copley Medal（1922，皇家学会；"For his researches in radio activity & atomic structure"）
- Franklin Medal（1924，Franklin Institute；"For knowledge of the chemical elements, their constitution and relationship"）
- Albert Medal（1928，Royal Society of Arts）
- Faraday Medal（1930，Institution of Electrical Engineers）
- Faraday Lectureship Prize（1936，Royal Society of Chemistry）
- Wilhelm Exner Medal（1936，奥地利）
- 爵位：Knight Bachelor（1914，乔治五世）→ Order of Merit（1925）→ Baron（1931，1st Baron Rutherford of Nelson）
- 会籍：FRS（1903）、American Philosophical Society 国际会员（1904）、Royal Society of Edinburgh 荣誉会士（1921）；皇家学会会长（1925–1930，第 44 任）
- metadata.json 另载但 page.md 未给年份者（如实列出，立传中不标年份）：Royal Society Bakerian Medal（其 1920 Bakerian Lecture 见正文）、Guthrie Lecture、T. K. Sidey Medal、Bressa Prize、Silliman Memorial Lectures、Barnard Medal for Meritorious Service to Science、IET Kelvin Lecture、Faraday Medal and Prize、Echegaray Medal、Dalton Medal、巴黎大学荣誉博士、新西兰大学荣誉博士、Person of National Historic Significance

## 9. 机构清单

- 教育：Foxhill School（约 1876–）、Havelock School（1883–）、Nelson College（1887–1889）、Canterbury College, University of New Zealand（1890–1894；BA 1892 / MA 1893 / BSc 1894）、Cavendish Laboratory, University of Cambridge（1895–；Trinity College 1897 B.A. Research Degree、Coutts-Trotter Studentship）
- 任职：McGill University（1898–1907，Macdonald 讲席物理教授，经 Thomson 推荐）→ Victoria University of Manchester（1907–1919，Langworthy 讲席教授）→ University of Cambridge（1919–1937，Cavendish Professor of Physics / 实验室主任，继 J. J. Thomson）→ 皇家学会会长（1925–1930）
- 命名机构与遗产：化学元素 **rutherfordium**（Rf, Z=104，1997 年命名）；新西兰 100 元纸币肖像（1999 年起）；曼彻斯特 Withington 故居 Rutherford Lodge（2012 年蓝牌）；page.md See also 另列 Rutherford (unit)（放射性单位）与 Rutherfordine（矿物）——See also 有载可提及，正文细节无展开不深写

## 10. 终审清单

- [ ] 生卒 1871-08-30 / 1937-10-19，享年 66，出生地 Brightwater、去世地剑桥、安葬威斯敏斯特教堂
- [ ] 1908 **化学奖**、独享、理由中文措辞照总名单；"物理学家获化学奖" 表述贯穿全篇
- [ ] 原子核（1909 金箔 → 1911 理论）在获奖**之后**，因果未倒置
- [ ] α/β（1899）、γ（1903，Villard 发现）命名归属与年份准确
- [ ] 半衰期（与 Owens）与蜕变理论（与 Soddy）两组合作未互换；Thorium X 同位素写法与 page.md 一致或已规避
- [ ] 质子 1920 命名、中子 1920 提出/1932 Chadwick 证实、sonar 归属误解口径正确
- [ ] 学生仅收 page.md infobox 明确者；metadata 无载者未入库
- [ ] 引语仅三处 page.md 实载（15-inch shell / moonshine / Jeans 悼词），其余为间接转述
- [ ] 奖项年份表（1904/1908/1910/1913/1916/1922/1924/1928/1930/1936×2）与爵位（1914/1925/1931）无误
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ernest_Rutherford/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 已有真实肖像 URL `https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Ernest_Rutherford_1892.jpg/250px-Ernest_Rutherford_1892.jpg`——下载时 250px 改 500px 以上；404 则用 Wikipedia REST API page/summary 查 infobox 原图名或 Commons Special:FilePath 回退，再 404 则装饰圆占位
- [ ] **国籍**：封面顶部明示新西兰（New Zealander）
- [ ] **引语核对**：仅三处实载引语可加引号（15-inch shell / moonshine / Jeans 悼词），须逐字对照 page.md
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧（Frederick Sanger）及数学家侧（高斯）既有格式对齐

---

> **名单状态**：本提示词已完成；Beamer 立传待执行。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（执行立传完成后再同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
