# Otto Wallach（奥托·瓦拉赫）立传提示词

> qid=Q57127 · 1847-03-27 – 1931-02-26 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1910）
> 官方理由（总名单措辞照抄）：表彰他因在脂环族化合物领域的开创性工作，对有机化学和化学工业所作出的贡献
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Otto_Wallach/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像执行阶段下载，见 §11 Review-1 头像指引；infobox 记有 "Wallach c. 1873" 照片）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 脂环世界的开路人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「脂环 / 环状结构」母题——圆环与圆点错落暗示碳骨架的六元环与精油分子。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Otto Wallach（中文惯称：奥托·瓦拉赫；德语发音 [ˈɔto ˈvalax]）
- **生卒**：1847-03-27 生于普鲁士王国柯尼斯堡（Königsberg）→ 1931-02-26 逝于德国哥廷根（魏玛共和国），享年 83；安葬于哥廷根（Stadtfriedhof 墓地，见 images.txt 墓照）
- **国籍**：German（德意志；metadata.json 记 German Empire）
- **身份**：化学家（有机化学；哥廷根大学教授）
- **家庭**：普鲁士公务员之子；父 Gerhard Wallach 出身**皈依信义宗的犹太家庭**，母 Otillie（娘家姓 Thoma）为信奉新教的德意志人；父先后调职斯德丁（Stettin，今什切青）、波茨坦
- **教育轨迹**：波茨坦文理中学（Gymnasium；在那里研习文学与艺术史——终生兴趣，同期在家开始私人化学实验）→ 1867 入哥廷根大学学化学（时值 Friedrich Wöhler 执掌有机化学）→ 柏林大学一学期（随 August Wilhelm von Hofmann）→ 1869 获哥廷根大学博士学位
- **导师**：博士导师 **Hans Hübner**（page.md infobox 明载；metadata.json 记 Hofmann——冲突，见 §5）；柏林一学期受教于 Hofmann；Bonn 任职期间与 Friedrich Kekulé 共事并开始萜烯研究
- **博士论文**：1869 年于哥廷根获博士学位（page.md 未载论文题目，禁写）
- **研究领域**：有机化学——萜烯（terpenes）、脂环族化合物（alicyclic compounds）、精油、重排反应

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **柯尼斯堡公务员之子（1847）**：生于普鲁士东陲，随父辗转斯德丁、波茨坦；文理中学里爱上文学与艺术史——化学家中的文人趣味。
2. **家里的私人实验室**：中学时代即在父母家中开始私人化学实验——与同代人如出一辙的化学启蒙路径。
3. **哥廷根求学（1867–）**：入 Wöhler 执掌有机化学的哥廷根；去柏林随 Hofmann 一学期，再回哥廷根——1869 年 22 岁获博士。
4. **Bonn 三十年（1870–1889）**：1869 博士后赴波恩大学任教 19 年；正是在与 **Kekulé 共事**期间开始对精油中**萜烯**的系统分析。
5. **一片混沌中的萜烯**：在他之前只有寥寥数种萜烯被纯化，结构信息稀少——这是 Wallach 挑战的起点。
6. **熔点比较法**：确认"同一物质"的利器——混合物熔点测定；但萜烯多为液体，必须先变成晶体。
7. **逐步衍生化**：对萜烯双键加成等逐步衍生化，把液体萜烯转化为**结晶化合物**——让经典鉴定方法得以施展（问题→方法→结果的典范）。
8. **重排追踪法**：研究环状不饱和萜烯的**重排反应**，把未知萜烯沿重排路径追到已知结构——由此打开萜烯系统研究之路。
9. **命名者**：他负责命名 **terpene（萜烯）** 与 **pinene（蒎烯）**，并对 pinene 作出首次系统研究；α-蒎烯结构图存世（images.txt）。
10. **反应遗产**：Wallach rearrangement（瓦拉赫重排）、Wallach degradation（瓦拉赫降解）、**Leuckart–Wallach reaction**（与 Rudolf Leuckart 共同发展）——三个以他命名的反应；另有结晶学 **Wallach's rule**（外消旋混合物）。
11. **《萜烯与樟脑》（1909）**：*Terpene und Campher* 汇总其在脂环族碳化合物领域的自身研究；另著 *Tabellen zur chemischen Analyse*（1880，波恩）。
12. **1910 诺贝尔化学奖（独享）**：表彰其在**脂环族化合物**上的工作；诺奖讲演 *Alicyclic Compounds*（1910-12-12）；1912 再获皇家学会 **Davy Medal**。
13. **哥廷根岁月与传承（1889–1915）**：1889 年自波恩回哥廷根任教授至 1915；博士学生中有 **Walter (Norman) Haworth**（1937 年诺贝尔化学奖）与 Adolf Sieverts——萜烯化学由学生带向糖化学的巅峰。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深林绿 forestdeep） | `#1E4D3B` | 精油与植物世界的深邃（表头 / 公式文本） |
| 强调色（诺贝尔金，OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（萜烯与精油 badgeTer） | `#2E7D5B` | 翠绿萜烯 / 精油 / 蒎烯 |
| 分类色 2（脂环族 badgeAli） | `#1D5F7A` | 青蓝脂环族化合物 / 诺奖主题 |
| 分类色 3（反应与方法 badgeRea） | `#B07A1F` | 琥珀衍生化 / 重排 / 三大命名反应 |
| 分类色 4（结晶学规则 badgeRul） | `#6B4E8E` | 紫晶 Wallach's rule / 外消旋体 |
| 背景 | `#F6F8F5` | 浅灰白偏绿 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆环与圆点组合呼应「脂环 / 碳环骨架」——精油一滴中的几何世界。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（`music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`）
- **风格**：怀旧 / 温和 / 传记段落、学派传承
- **匹配理由**：
  - "怀旧" 匹配 Wallach 的 19 世纪气质——精油、香料、波茨坦文理中学的文学与艺术史趣味，是"旧世界"的化学
  - "温和" 匹配其研究风格——不是革命性的理论颠覆，而是数十年熔点、衍生化、重排的耐心工艺；"学院传承" 匹配 Bonn→Göttingen 的漫长教席与学生 Haworth 的诺奖传承
  - 避开 epic/heroic：Wallach 的贡献是"把混沌整理成体系"的手艺活，Nostalgia 的温润叙事比史诗更贴合
- **时长**：`make video` 时 ffmpeg `-shortest` 自动对齐；**wav 复制在执行立传阶段进行**（`cp` 到本目录，勿现在复制）。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 脂环世界的开路人 / Otto Wallach 1847–1931 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  瓦拉赫的一生 — 高斯式时间线（10 节点：1847 柯尼斯堡出生→1867 入 Göttingen→1869 博士→1870 赴 Bonn→1889 回 Göttingen 教授→1909 Terpene und Campher→1910 诺贝尔奖→1912 Davy Medal→1915 卸任→1931 去世）
04  早年：柯尼斯堡公务员之子 (1847–1867) — 表格「时间|事件|结果」（随父辗转/波茨坦中学/文学与艺术史/家庭化学实验）
05  Göttingen 求学与柏林一学期 (1867–1870) — 表格「时间|事件|结果」（Wöhler 的哥廷根 / Hofmann 的柏林 / 1869 博士）
06  Bonn 三十年：与 Kekulé 共事 (1870–1889) — 表格「背景|契机|转向」（Kekulé 处开始精油萜烯系统分析；*Tabellen zur chemischen Analyse* 1880）
07  萜烯研究法三部曲 — 表格「问题|方法|结果」+ 公式框：萜烯通式 C₁₀H₁₆（见 §5 公式注记）
08  命名者：terpene 与 pinene — 表格「对象|工作|意义」+ α-蒎烯结构图（images/AlphaPinene.png 可用）
09  以他命名的反应 — 表格「反应|内容|传承」+ 公式框：Leuckart–Wallach / Wallach rearrangement / Wallach degradation 概念式（见 §5 公式注记）
10  Wallach's rule：结晶学的遗产 — 表格「对象|规则|意义」（外消旋混合物结晶）
11  Göttingen 岁月与学生 (1889–1915) — 表格「人物|方向|结果」（Haworth 1937 诺奖 / Sieverts）
12  《萜烯与樟脑》与著作 — 高斯「类别|代表|意义」表格（1909 初版 / 1914 第二版 / 1880 分析表）
13  荣誉：1910 诺贝尔与 Davy Medal — 表格「类别|代表|意义」（Nobel 1910 独享 / Davy Medal 1912 / Cothenius Medal 1889 / Red Eagle 3rd Class）+ 诺奖讲演 Alicyclic Compounds
14  结尾 — 「在精油的一滴液体里，看见碳原子的环。」（叙述金句，非 Wallach 引语，见 §5）+ 品牌 OpenMathAI
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 博士导师冲突 | infobox 明载 **Hans Hübner**；metadata.json 记 August Wilhelm von Hofmann。page.md 正文只说柏林一学期随 Hofmann、1869 从哥廷根获博士——**以 page.md infobox 的 Hübner 为博士导师**，Hofmann 记"柏林一学期教师"（**page.md 与 metadata 冲突点，已在 §7 同步**） |
| Kekulé 关系 | page.md 只说 "During his work with Friedrich Kekulé in Bonn" 开始萜烯系统分析——是 **Bonn 共事**，勿写"Kekulé 的学生/博士导师是 Kekulé" |
| "father of terpene chemistry" | page.md **无此说法，禁写**；忠实表述为 "opened the path to systematic research on terpenes"（打开萜烯系统研究之路） |
| 与 Emil Fischer 的关系 | page.md **无载，禁写**任何师承/合作/竞争表述 |
| 退休年份 | 任职 Göttingen **1889–1915**——1915 是**一战期间**卸任，勿写"一战后退休" |
| 诺奖表述 | 1910 **独享**；理由照抄总名单「表彰他因在脂环族化合物领域的开创性工作，对有机化学和化学工业所作出的贡献」；page.md 英文为 "for his work on alicyclic compounds"；讲演 *Alicyclic Compounds*（1910-12-12）——勿写成"因萜烯获奖"（获奖词是脂环族化合物） |
| 生卒噪声 | metadata.json date_of_birth 含 1847-01-01、date_of_death 含 1931-01-01 噪声值——**以 page.md 1847-03-27 / 1931-02-26 为准**（page.md 与 metadata 冲突点） |
| 命名贡献 | 他负责**命名** terpene 与 pinene、并首次系统研究 pinene——勿写"发现萜烯" |
| 三个 Wallach 命名体 | Wallach's rule 是**外消旋混合物**的结晶规则（勿与重排混淆）；Wallach rearrangement 是重排反应；Wallach degradation 是降解（infobox 置于 Favorskii rearrangement 词条下）；Leuckart–Wallach reaction 与 **Rudolf Leuckart 共同发展**——四者勿互相混淆 |
| 书名版次 | *Terpene und Campher* 正文称 **1909**；Works 列表给的是 **1914 第二版**（Leipzig: von Veit）——引用时注明版次，勿写成两个不同年份的书 |
| 学生姓名异写 | infobox 记 **Walter Haworth**（即 W.N. Haworth，1937 诺奖）、Adolf Sieverts；metadata.json 记 Norman Haworth、Heinrich Mallison、Abram Berkengeim——Haworth 为同一人异写，入库统一 Walter (Norman) Haworth；Mallison、Berkengeim 正文无载**不予入库** |
| 犹太血统表述 | 父系出身**皈依信义宗的犹太家庭**、母为新教德意志人；See also 含 "List of Jewish Nobel laureates"——表述须忠实原文、克制平实，勿渲染或展开 |
| 生平资料极薄 | page.md 传记仅数段：1867 前细节（斯德丁/波茨坦年份）、Bonn 40 年间事件、一战与退休生活**几乎全无载**——禁写任何具体年份事件（如"1873 年 photographed"之类），页面上 "Wallach c. 1873" 仅作照片图注年份 |
| 公式框注记 | 萜烯通式 C₁₀H₁₆ 与三个命名反应的概念式均为通用教科书形式，page.md 未给出任何方程——公式可上片但须在 §5 留痕、正文叙述不添加 page.md 无载的反应机理细节 |
| 结尾金句 | 「在精油的一滴液体里，看见碳原子的环。」为**叙述金句**，非 Wallach 原话——page.md 无任何 Wallach 直接引语，**全篇禁止给 Wallach 加引号原话**；结尾页排版不加引号或标注"——题记" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57127 | ✅ |
| name_zh | 奥托·瓦拉赫 | ✅ |
| name_en | Otto Wallach | ✅ |
| birth_date | 1847-03-27（metadata 中 1847-01-01 为噪声，弃用） | ✅ |
| death_date | 1931-02-26（metadata 中 1931-01-01 为噪声，弃用） | ✅ |
| nationality | German（German Empire） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：terpene chemistry / alicyclic compounds / essential oils / rearrangement reactions，带 rank） | ✅ |
| has_biography | 待立传后置 1 | 🔲 |

## 7. 社会关系入库清单

**师长 / 同侪 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Hübner | 师→生（博士导师） | page.md infobox 明载；1869 哥廷根博士 |
| advisor-student | August Wilhelm von Hofmann | 师→生（柏林一学期教师） | metadata.json 记为博士导师——与 infobox 冲突，note 注明"柏林一学期受教" |
| colleague | Friedrich Wöhler | 无向 | 求学时期哥廷根有机化学主任 |
| colleague | Friedrich Kekulé | 无向 | Bonn 共事；在其任内开始萜烯系统分析 |
| colleague | Rudolf Leuckart | 无向 | 共同发展 Leuckart–Wallach reaction |

**门生（Wallach → 学生，源自本地 Wikipedia 正文 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter (Norman) Haworth | Wallach → 学生 | infobox 记 Walter Haworth；1937 年诺贝尔化学奖 |
| advisor-student | Adolf Sieverts | Wallach → 学生 | infobox 博士学生 |

> metadata.json `doctoral_student` 另含 Heinrich Mallison、Abram Berkengeim，但正文 infobox 无此二人，**不予入库**。
> page.md 载其为诺奖得主、See also 指向犹太诺奖得主名录，但正文无其他 co-honored / competitor 关系，不予虚构。

## 8. 奖项清单

- Nobel Prize in Chemistry（1910，独享；表彰脂环族化合物工作；讲演 *Alicyclic Compounds*，1910-12-12）
- Davy Medal（1912，英国皇家学会）
- Cothenius Medal（1889）
- Order of the Red Eagle 3rd Class（红鹰勋章三等；metadata.json 有载，年份无）
- honorary member of the Physics Association, Frankfurt am Main（metadata.json 有载）

## 9. 机构清单

- 教育：Potsdam Gymnasium（文学与艺术史）；University of Göttingen（1867 入学，1869 博士）；University of Berlin（一学期，随 Hofmann；metadata.json 记 Humboldt-Universität zu Berlin）
- 任职：University of Bonn（1870–1889，教授）；University of Göttingen（1889–1915，教授）
- 命名机构：无（page.md 无以其命名的机构/博物馆记载；哥廷根 Stadtfriedhof 有其墓地）

## 10. 终审清单

- [x] 生卒 1847-03-27 / 1931-02-26，享年 83；出生地柯尼斯堡、去世地哥廷根；metadata 01-01 噪声值已弃用
- [x] 1910 独享；诺奖理由中文与总名单逐字一致（脂环族化合物）；勿写成"因萜烯获奖"
- [x] 博士导师 Hans Hübner（Hofmann 注明"柏林一学期"，metadata 冲突已留痕）
- [x] Kekulé 写"共事"，禁写师生；"father of terpene chemistry" 禁写；Emil Fischer 禁写
- [x] terpene/pinene 为"命名"非"发现"；三个命名反应与 Wallach's rule 不混淆
- [x] *Terpene und Campher* 1909 初版 / 1914 第二版注明版次；卸任 1915（一战期间）
- [x] 学生 Walter (Norman) Haworth 统一异写；Mallison/Berkengeim 不入库
- [x] 全篇无 Wallach 加引号"原话"；结尾金句为叙述题记
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Otto_Wallach/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt **无肖像 URL**（仅哥廷根墓照与 α-蒎烯结构图）；infobox 记有 "Wallach c. 1873" 照片——执行时经 Wikipedia REST API `page/summary` 查 infobox 原图文件名下载（250px→500px），或 Commons `Special:FilePath` 回退；404 则装饰圆占位
  - 【执行留痕 2026-09-10】REST API 查得 infobox 原图 `Otto_Wallach_1880s.jpg`（Archivio Mondadori 藏 "portrait de OTTO WALLACH"），已下载 500px（500×642 JPEG）至 `images/Otto_Wallach.jpg`；α-蒎烯结构图 AlphaPinene.png 亦已下载用于 Slide 08
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：page.md 无 Wallach 直接引语——任何引号内容出现即为错误（获奖理由与书名除外）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；引号半角
- [ ] 与数学家侧（高斯）及化学家侧既有格式（Sanger 标杆）对齐

---

> **名单状态**：本提示词已完成；Beamer 立传待执行。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（执行立传完成后再同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
