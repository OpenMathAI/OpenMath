# Michael Levitt（迈克尔·莱维特）立传提示词

> qid=Q6832227 · 1947-05-09 生于南非比勒陀利亚 · 在世 · 南非出生的生物物理学家（美/英/以/南非四重公民） · 诺贝尔化学奖（2013，与 Martin Karplus、Arieh Warshel 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Michael_Levitt_biophysicist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从本地 `images.txt` 列表下载，如 2013 斯德哥尔摩发布会照；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 折叠蛋白质的程序员\enspace·\enspace 美国/英国/以色列/南非`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（四重）、出生地、教育、博士导师、研究领域、任职、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「折叠与模拟」母题——圆点从线性排列渐次聚拢成团，暗合蛋白质从一级序列折叠到三维结构的计算过程。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），构象分析或序列-结构比对打分即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Michael Levitt（希伯来文 מיכאל לויט；中文惯称：迈克尔·莱维特；FRS）
- **生卒**：1947-05-09 生于南非比勒陀利亚（Pretoria）→ 在世（卒日留白）
- **国籍**：四重公民——American / British / Israeli / South African（infobox Citizenship；yaml 按 South Africa rank 0 出生 + United States rank 1 + Israel rank 2 + United Kingdom rank 3 入库）
- **身份**：生物物理学家——斯坦福大学结构生物学教授（1987–）；2018 年起为《Annual Review of Biomedical Data Science》创始共同主编
- **家庭**：比勒陀利亚犹太家庭——父系来自立陶宛 Plungė、母系来自捷克；15 岁随家迁英格兰；1967 年首访以色列时结识以色列妻子 Rina（多媒体艺术家），携妻赴剑桥，三子女均在剑桥出生；妻子 Rina 于 2017-01-23 去世；infobox 另载妻子 Shoshan Brosh
- **教育轨迹**：
  - Sunnyside Primary School → Pretoria Boys High School（1960–1962）
  - 1963 在比勒陀利亚大学修应用数学一年（时年已随家迁英）
  - King's College London：物理学一等荣誉学士（1967）
  - Peterhouse, Cambridge：计算生物学博士（1968–1972 基于剑桥 MRC 分子生物学实验室）；论文《Conformation analysis of proteins》（1972）；博士导师 Robert Diamond（infobox）
- **研究领域**：计算结构生物学——蛋白质结构预测、分子动力学模拟、生物信息学、序列-结构比对打分

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **比勒陀利亚的立陶宛犹太家庭（1947）**：父系 Plungė、母系捷克——南非出生、多国长大的世界公民起点。
2. **15 岁迁英（1962）**：Pretoria Boys High 之后举家迁英格兰，1963 年在比勒陀利亚大学修应用数学一年，随后入 King's College London。
3. **物理一等荣誉（1967）**：KCL 物理学 first-class honours 毕业同年首访以色列。
4. **剑桥与 LMB（1968–1972）**：Peterhouse 计算生物学博士生，驻剑桥 MRC 分子生物学实验室；开发研究分子构象的计算机程序——奠定其后半生全部工作的基石。
5. **首开先河**：最早对 DNA 与蛋白质做分子动力学模拟的研究者之一，并为此开发了第一套软件（页面明载 "one of the first researchers... developed the first software"）。
6. **魏茨曼岁月（1979–1987）**：回以色列加入魏茨曼科学研究所；1980 年入籍以色列；1980–1987 任化学生物物理教授（1980–1983 兼系主任）；1985 年在以色列国防军服役六周。
7. **斯坦福教授（1987–）**：任结构生物学教授至今；此后在以色列与加州两地分居生活；另获剑桥 Gonville and Caius College 研究奖学金。
8. **CASP 评审人与批评者**：多次参加蛋白质结构预测 CASP 竞赛，批评分子动力学无法精修蛋白质结构——以批评推动方法进步。
9. **简化表示与打分系统**：发展蛋白质折叠与堆积的简化表示，以及大规模序列-结构比对的打分系统。
10. **2013 诺贝尔化学奖**：与 Martin Karplus、Arieh Warshel 共享，官方理由 "the development of multiscale models for complex chemical systems"——他代表结构生物学/大分子模拟一线，与 Karplus（理论化学）、Warshel（量化路线）分工不同，勿混。
11. **门生网络**：正文明载 mentor 过 Mark Gerstein 与 Ram Samudrala 等成功科学家；infobox 博士后名单另列 Steven Brenner、Cyrus Chothia、Valerie Daggett、Julian Gough；Cyrus Chothia 同时是他的同事。
12. **荣誉线**：EMBO 会员（1983）、FRS（2001）、美国国家科学院院士（2002）、ISCB Fellow（2015）、DeLano Award for Computational Biosciences（2014）、HKUST 荣誉理学博士。
13. **以色列第六人（十年内）**：不到十年间第六位获诺贝尔化学奖的以色列人（页面明载）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士蓝 prussian） | `#14324F` | 结构生物学的深蓝与剑桥的学术底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子动力学 badgeMD） | `#2E5A9E` | 蓝 DNA/蛋白质模拟先行者 |
| 分类色 2（结构预测 badgeFold） | `#1B7A43` | 绿 CASP / 蛋白质折叠 |
| 分类色 3（计算工具 badgeCode） | `#D97B29` | 琥珀第一套模拟软件 / 打分系统 |
| 分类色 4（四重国籍 badgeWorld） | `#7A4A8B` | 紫南非—英国—以色列—美国四站人生 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——折叠过程：圆点从线到团，如氨基酸链在计算机中收拢成天然构象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（文件 `86-5ETNuoDcBg4-Nostalgia.wav`，**勿复制 wav 文件**）
- **风格**：温情 / 回望 / 带节奏感的沉思
- **匹配理由**：
  - "Nostalgia" 对应其跨半世纪的计算生涯——1968 年 LMB 的手工编程岁月到今天的 AI 时代，一路回望
  - "温情" 匹配其多站人生——南非童年、英伦求学、以色列成家、斯坦福立业，四地皆故乡
  - "沉思" 匹配 CASP 评审人的清醒——既开先河也直言方法局限
- **时长核对**：以 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒的幻灯时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 折叠蛋白质的程序员 / Michael Levitt 1947– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/四重国籍/教育/博士导师/领域/任职/荣誉）
03  莱维特的一生 — Sanger 式时间线（10 节点：1947→1962→1967→1968→1972→1979→1980→1987→2013→2018）
04  南非童年与迁英 (1947–1967) — 表格「时间|事件|结果」（Pretoria / KCL 一等荣誉）
05  剑桥与 LMB (1968–1972) — 表格「环境|工具|产出」+ 公式框：构象分析程序
06  第一套模拟软件 (1970s) — 表格「对象|方法|意义」（DNA 与蛋白质 MD 先行）
07  魏茨曼与入籍以色列 (1979–1987) — 表格「机构|职务|转变」（化学生物物理教授 / 1980 入籍）
08  斯坦福结构生物学 (1987–) — 表格「挑战|方法|结果」+ 公式框：序列-结构比对打分
09  2013 诺贝尔化学奖 — 表格「奖项|年份|理由」+ 公式框：for multiscale models（三人共享，Levitt 分工线）
10  门生与同事 — 表格「人物|方向|结果」（Gerstein / Samudrala / Chothia 等）
11  荣誉与奖项 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单）
12  四大洲人生地图 — 机构流程图（Pretoria → KCL → MRC Cambridge → Weizmann → Stanford）
13  遗产：从模拟到 AI 时代 — 四分类遗产盒 + 公式框：CASP 与结构预测的演进（页面口径内）
14  结尾 — 「把生命的分子搬进计算机，是最浪漫的务实主义。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2013 获奖口径 | 与 Martin Karplus、Arieh Warshel **三人共享**；官方理由 "the development of multiscale models for complex chemical systems"（页面明载）——勿写独享、勿漏 Warshel |
| 三人分工 | Levitt 代表**结构生物学/大分子模拟**一线（DNA/蛋白质 MD 先行 + 结构预测）；Karplus 是理论化学出身、Warshel 是量化路线——分工勿混 |
| 博士导师 | infobox 记 **Robert Diamond**（剑桥）；frontmatter 另有 Shneior Lifson——正文与 infobox 均无 Lifson，**Lifson 不入库**（见 §7） |
| 配偶矛盾 | infobox Spouse=Shoshan Brosh，正文 wife=Rina（2017-01-23 去世）且正文明确三子女与 Rina 在剑桥出生——两处均为页面实载，正文叙事以 Rina 为主线，yaml 两条 spouse 各带注记，勿互相覆盖 |
| 国籍口径 | 四重公民（American/British/Israeli/South African，infobox）；"第六位以色列化学诺奖" 是十年窗口口径——封面国籍行可写全四国或按页面 intro 以 "South African-born" 起笔 |
| COVID-19 争议 | 页面载其基于自有模型的多次错误预测（2020-03-18 以色列"少于十死"、2020-07-25 美国"八月底结束/少于 17 万"）、签署 Great Barrington Declaration、WHO 批评与 Schekman/Majumder 批评——**敏感性高**：若呈现必须双向并列（预测+批评原文），或整体略过；Schekman/Majumder 等批评者**不入库** |
| 名字消歧义 | 页面标题为 "Michael Levitt (biophysicist)"（与数学家 John Mather 无关的另有人物）——本篇只写生物物理学家 Michael Levitt；yaml name_en 用 "Michael Levitt" |
| 军役细节 | 1985 年在以色列国防军服役仅六周——如实写"六周"，勿渲染 |
| 学位 | KCL 物理学一等荣誉学士（1967）+ 剑桥 PhD（1972）——勿写"物理学家出身"的诺奖分工（那是 Karplus） |
| 在世口径 | 无卒日，封面与身份页一律 "1947–" 留白，勿虚构 |
| 中文译名 | 惯称「迈克尔·莱维特」，勿用「列维特」等其他形式 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q6832227 | ✅ |
| name_zh | 迈克尔·莱维特 | ✅ |
| name_en | Michael Levitt | ✅ |
| birth_date | 1947-05-09 | ✅ |
| death_date | NULL（在世留白） | ✅ |
| nationality | South Africa（rank 0）+ United States（rank 1）+ Israel（rank 2）+ United Kingdom（rank 3） | ✅ |
| primary_occupation | biophysicist | ✅ |
| field_of_work | computational biology（person_field 细分：computational biology / protein structure prediction / bioinformatics / molecular dynamics，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**导师 / 同事 / 门生 / 共同得主 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Diamond | 师→生 | 剑桥博士导师（infobox Doctoral advisor，论文 1972） |
| co-honored | Martin Karplus | 无向 | 2013 诺贝尔化学奖共同得主 |
| co-honored | Arieh Warshel | 无向 | 2013 诺贝尔化学奖共同得主 |
| advisor-student | Steven Brenner | 师→生 | infobox Notable students（postdocs） |
| advisor-student | Valerie Daggett | 师→生 | infobox Notable students（postdocs） |
| advisor-student | Mark Gerstein | 师→生 | 正文 "has mentored" 明载 + infobox postdocs |
| advisor-student | Ram Samudrala | 师→生 | 正文 "has mentored" 明载 + infobox postdocs |
| advisor-student | Julian Gough | 师→生 | infobox Notable students（postdocs） |
| colleague | Cyrus Chothia | 无向 | 正文 "was one of his colleagues"；infobox 另列于 postdocs |
| spouse | Rina | 无向 | 以色列妻子（多媒体艺术家），三子女之母；2017-01-23 去世 |
| spouse | Shoshan Brosh | 无向 | infobox 载妻子 |

> **禁入库名单**（页面无载或非本人直接关系）：Shneior Lifson（frontmatter-only 博士导师，正文/infobox 无载）、Randy Schekman 与 Maia Majumder（COVID 争议批评者，不建关系）、三子女（未具名）、Gonville and Caius College 等机构、CASP 组织。

## 8. 奖项清单

- Nobel Prize in Chemistry（2013，与 Martin Karplus、Arieh Warshel 共享）
- EMBO Member（1983）
- Fellow of the Royal Society，FRS（2001）
- National Academy of Sciences 院士（2002）
- DeLano Award for Computational Biosciences（2014）
- ISCB Fellow（2015，国际计算生物学会）
- Hong Kong University of Science and Technology 荣誉理学博士（honoris causa）
- Clarivate Citation Laureates（frontmatter 载）

## 9. 机构清单

- 教育：Sunnyside Primary School；Pretoria Boys High School（1960–1962）；University of Pretoria（1963，应用数学）；King's College London（BSc 物理学一等荣誉 1967）；Peterhouse, University of Cambridge（PhD 1972，基于 MRC LMB）
- 任职履历（页面明载）：
  - Royal Society Exchange Fellow，魏茨曼科学研究所（1967–1968）
  - Staff Scientist，MRC Laboratory of Molecular Biology，剑桥（1973–1980）
  - Professor of Chemical Physics，魏茨曼科学研究所（1980–1987，系主任 1980–1983）
  - Professor of Structural Biology，斯坦福大学（1987–）
- 其他：Gonville and Caius College, Cambridge 研究奖学金；《Annual Review of Biomedical Data Science》创始共同主编（2018）；多家公司科学顾问委员会（Dupont Merck、AMGEN、Affymetrix、StemRad 等）

## 10. 终审清单

- [ ] 生卒 1947-05-09 / 在世留白；出生地比勒陀利亚表述准确
- [ ] 2013 **三人共享**（Karplus/Levitt/Warshel），官方理由 "the development of multiscale models for complex chemical systems" 表述准确
- [ ] 三人分工（Levitt=结构生物学/大分子模拟）表述准确，勿交叉错写
- [ ] 博士导师只写 Robert Diamond；Shneior Lifson 标注为 frontmatter-only 不入库
- [ ] 配偶双源（正文 Rina / infobox Shoshan Brosh）各自如实带注记，不互相覆盖
- [ ] COVID-19 争议：要么双向并列呈现，要么整体略过——绝不单向引用批评或预测
- [ ] "one of the first researchers...first software" 与 "sixth Israeli in under a decade" 均有页面明载
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Michael_Levitt_biophysicist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 `images.txt` 列表下载（2013 斯德哥尔摩发布会照优先），失败用装饰圆占位
- [ ] **国籍**：封面顶部明示四重国籍或 "South African-born" 口径
- [ ] **引语核对**：本篇几乎无直接引语——凡引号内容须在原文找到（"development of multiscale models..." 为诺奖理由原句），否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本提示词不直接改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
