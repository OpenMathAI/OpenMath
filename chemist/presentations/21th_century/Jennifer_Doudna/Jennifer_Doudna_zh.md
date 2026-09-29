# Jennifer Doudna（珍妮弗·道德纳）立传提示词

> qid=Q56068 · 1964-02-19 生于美国华盛顿特区（在世，卒日留白） · 美国生物化学家 · 21 世纪 · 诺贝尔化学奖（2020，与 Emmanuelle Charpentier 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Jennifer_Doudna/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Frederick Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Jennifer_Doudna_by_Chris_Michel_02.jpg`，2023 年 Christopher Michel 摄，已就位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace CRISPR 基因剪刀的锻造者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「分子剪刀 / 碱基编辑」母题——圆点成对错落，暗示 gRNA 与 DNA 的靶向配对。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jennifer Anne Doudna（中文惯称：珍妮弗·道德纳；ForMemRS）
- **生卒**：1964-02-19 生于美国华盛顿特区（在世，卒日留白勿写）
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist）；UC Berkeley Li Ka Shing 冠名讲席教授；HHMI 研究员（1997 至今）；Innovative Genomics Institute 创始主任
- **家庭**：父 Martin Kirk Doudna（密歇根大学英语文学博士，夏威夷大学希洛分校美国文学教师）、母 Dorothy Jane（Williams，教育学硕士，后修亚洲史硕士在社区学院教历史）；7 岁随家迁夏威夷希洛。第一段婚姻 1988 嫁哈佛研究生同学 Tom Griffin（数年后离婚）；2000 在夏威夷嫁 Jamie Cate（科罗拉多博后期间结识的研究生，后同为伯克利教授），2002 年得一子（现 UC Berkeley 读 EECS）
- **教育轨迹**：
  - Hilo High School（1981 毕业；10 年级化学老师 Jeanette Wong 是其投身科学的重要影响者；曾在真菌学家 Don Hemmes 实验室度过一个夏天）
  - Pomona College（BA biochemistry，1985；大一通用化学课曾自我怀疑想转法语专业，法语老师劝留；化学老师 Fred Grieman 与 Corwin Hansch 影响深远；首个科研在 Sharon Panasenko 实验室）
  - Harvard Medical School（生物化学与分子药理学 PhD，1989；论文《Towards the Design of an RNA Replicase》）
- **导师**：Jack W. Szostak（博士导师）；Thomas Cech（博士后导师，其他学术导师）
- **研究领域**：生物化学——CRISPR 基因编辑、RNA 结构生物学（核糖酶 / ribozyme）、RNA 干扰、X 射线晶体学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **《双螺旋》的启发（约 1975）**：六年级时父亲给她 James Watson 的《The Double Helix》，成为其科学启蒙。
2. **夏威夷女孩（1964–1981）**：希洛的动植物激发好奇；高中化学老师 Jeanette Wong 与一位癌症细胞客座讲师坚定其科学志向。
3. **Pomona 自我怀疑与坚持（1981–1985）**：大一化学课后一度想转法语专业，被法语老师劝回；遇到名师 Grieman 与 Hansch。
4. **Szostak 组的核糖酶工程（1985–1989）**：在哈佛把四膜虫 Group I 自剪接内含子改造成能拷贝 RNA 模板的真催化核糖酶。
5. **Cech 组的晶体攻坚（1991–1996）**：意识到"看不见核糖酶的分子机制"是最大瓶颈，赴科罗拉多博尔德 Cech 实验室启动核糖酶晶体项目，1994 至耶鲁后于 1996 年完成——首次用 X 射线解出催化 RNA 三维结构。
6. **P4-P6 结构域（耶鲁）**：解析四膜虫 Group I 核糖酶催化核心——五个镁离子簇构成疏水核心，与蛋白质疏水氨基酸核心类似但化学本质不同；后续解析 HDV 核糖酶、IRES、SRP 等大 RNA 结构。
7. **Waterman 奖（2000）**：美国 NSF 35 岁以下最高荣誉，表彰核糖酶结构测定；同年升耶鲁 Henry Ford II 教授、任哈佛 Woodward 访问教授。
8. **2006 转折点**：微生物学家 Jillian Banfield 用 Google 搜 "RNAi and UC Berkeley" 找到 Doudna，把她引入 CRISPR 领域。
9. **2009 Genentech 弯路**：离职去 Genentech 领导发现研究，两个月即返伯克利（同事 Michael Marletta 协助），取消全部事务专心研究 CRISPR。
10. **CRISPR-Cas9 剪刀（2012）**：与 Emmanuelle Charpentier 首次证明可用不同 RNA 编程 Cas9 切割编辑不同 DNA——细菌免疫系统的"剪刀"变成可编程基因组编辑工具，被称为生物学史上最重要的发现之一。
11. **专利之战（2014–2018）**：UC Berkeley 与 Broad Institute（Feng Zhang）争相申请专利；2017 年初审、2018-09 上诉均判 Broad 胜，UC 拿到通用技术专利，欧洲则驳回 Broad 主张（程序瑕疵）——"crispr 分裂"局面。
12. **创业与 COVID（2011–2020）**：共同创办 Caribou（2011）、Editas（2013，2014-06 退出）、Intellia、Mammoth（2017）、Scribe（CasX）；2020-03 起组织 IGI 用 CRISPR 应对新冠，检测中心处理超 50 万份样本。
13. **《A Crack in Creation》与伦理领导（2017–）**：与学生 Samuel H. Sternberg 合著第一人称突破亲历记；呼吁世界暂停临床基因编辑应用；支持体细胞编辑、反对生殖系编辑。2025 年获美国国家技术创新奖章、ACS 宣布其为 2026 Priestley Medal 得主、当选 NAE 院士；2025 年 LBNL 宣布以她命名新超算 Doudna（Perlmutter 后继机）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深碧蓝 deepteal） | `#0E4D64` | RNA 深海般精确的结构生物学底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（CRISPR 基因编辑 badgeCRISPR） | `#2E5A9E` | 蓝 Cas9 分子剪刀 / 基因组编辑 |
| 分类色 2（核糖酶结构 badgeRibozyme） | `#1B7A43` | 绿 P4-P6 / 首个催化 RNA 三维结构 |
| 分类色 3（RNA 生物学 badgeRNA） | `#D97B29` | 琥珀 RNA 干扰 / 丙肝病毒蛋白合成 |
| 分类色 4（伦理与治理 badgeEthics） | `#C0395B` | 玫瑰 moratorium / 生殖系编辑立场 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「分子剪刀剪断双链」的成对圆点意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（`music_audio/inspiring-electronic/15-w6kT1BfvETI-*.wav`；不要复制 wav 文件，Makefile 指向源路径）
- **风格**：恢弘上扬 / 史诗而明亮 / 开拓感
- **匹配理由**：
  - "Epic Beautiful Uplifting" 匹配 CRISPR 之于生物学的开拓意义——一把剪刀照亮整个基因组编辑时代
  - "恢弘上扬" 匹配其叙事弧线——夏威夷女孩 → 核糖酶结构 → 2012 分子剪刀 → 2020 诺奖 → 伦理守护
  - 与本批其他曲目错开（List=Pathfinder、MacMillan=New Lands、Bertozzi=Timeless、Meldal=PAST）
- **时长**：须 make video 时以 ffmpeg `-shortest` 自动对齐 15 页时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — CRISPR 基因剪刀的锻造者 / Jennifer Doudna 1964– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士/师承/领域/荣誉）
03  道德纳的一生 — 高斯式时间线（10 节点：1964→1981→1985→1989→1991→1996→2002→2012→2020→2025）
04  早年：夏威夷与《双螺旋》(1964–1985) — 表格「时间|事件|结果」
05  哈佛与 Szostak 组：RNA 催化剂工程 (1985–1989) — 表格「时间|事件|结果」
06  核糖酶晶体：第一个催化 RNA 三维结构 (1991–2000) — 表格「问题|方法|结果」+ 公式框：P4-P6 五镁离子核心
07  伯克利与 CRISPR 入场 (2002–2011) — 表格「契机|人物|结果」（Banfield 2006 / Genentech 弯路）
08  CRISPR-Cas9 分子剪刀 (2012) — 表格「问题|方法|结果」+ 公式框：gRNA 编程 Cas9 切割双链 DNA
09  专利之战与产业转化 (2014–2019) — 表格「战场|对手|结果」（Berkeley vs Broad；Caribou/Intellia/Mammoth/Scribe）
10  门生与传承 — 表格「人物|方向|结果」（Haurwitz / Chen / Qi / Sternberg）
11  荣誉清单 — 高斯式「类别|代表|意义」表格（含 itemize：2020 Nobel / Waterman / Breakthrough / Kavli / Wolf / Priestley 2026）
12  COVID-19 与 IGI — 高斯 FFT 页式流程图（2020-03 组织 → 检测中心 50 万样本 → Mammoth 快速诊断）
13  遗产：基因编辑的伦理与未来 — 四分类遗产盒 + 公式框：体细胞 vs 生殖系编辑
14  结尾 — 「我们拿到了生命的编辑器，现在要决定如何使用它。」（意译自其对 CRISPR 乐观与忧思的表态，非原话直引）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2020 诺奖口径 | 与 Emmanuelle Charpentier **两人共享**，官方理由 "for the development of a method for genome editing"——勿写"三人共享"，勿把 Šikšnys 写进诺奖（他只获 2018 Kavli 共享） |
| 诺奖理由泛化 | 勿写成 "for the development of CRISPR-Cas9"；官方原句没有 Cas9 字样 |
| CRISPR 系统发现史 | CRISPR 1987 由 Yoshizumi Ishino 等首次发现、Francisco Mojica 后续表征；Doudna/Charpentier 2012 的贡献是**首次证明可编程编辑**——勿写"发现 CRISPR" |
| 专利战表述 | 2017 初审与 2018-09 上诉均 Broad 胜；UC 获通用技术专利；欧洲驳回 Broad——三方结果并写勿简化成"谁赢了" |
| Feng Zhang 双重身份 | 2016 Canada Gairdner（与 Charpentier/Horvath/Barrangou 五人共享）与专利对手、Editas 共同创办（2014-06 Doudna 退出）——三种关系勿混 |
| Kavli vs Wolf vs Nobel | Kavli 2018（与 Charpentier、Šikšnys）、Wolf 医学奖 2020（与 Charpentier）、Nobel 2020（仅与 Charpentier）——共享名单逐年不同，勿混 |
| 出生日期 | 1964-02-19（Washington, D.C.）；在世，卒日留白 |
| 教育口径 | PhD 是 Harvard（生物化学与分子药理学，1989），勿写 Harvard Medical School MD；Pomona BA 1985 |
| 第一段婚姻 | Tom Griffin（1988 结婚、数年后离婚）可写但一笔带过；现配 Jamie Cate（2000 夏威夷结婚）——两段勿混 |
| 博后归属 | 1991–1994 科罗拉多博尔德 Cech 组（Lucille P. Markey Postdoctoral Scholar）；另在 MGH 与哈佛有分子生物学/遗传学 fellowships——勿写"在耶鲁做博后" |
| 引语红线 | 正文仅一句直接引语（对 CRISPR 乐观与分配忧思的表态）；《A Crack in Creation》只写书名与合著者；其余一律间接转述 |
| 敏感话题 | 基因编辑伦理只写其公开立场（支持体细胞、反对生殖系编辑、呼吁 moratorium）；He Jiankui 事件页面无载，**禁写** |
| 荣誉年份 | Priestley Medal 是"2026 得主"（ACS 已宣布）、NAE 2026 当选、国家技术创新奖章 2025——三个"未来年份"按页面口径写 |
| 门生入库 | infobox Doctoral students 四人：Rachel Haurwitz、Janice Chen、Lei Stanley Qi、Samuel H. Sternberg；合作者 Robert Tjian/Fyodor Urnov/Patrick Hsu/Dave Savage（COVID 团队）**不予入库** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q56068 | ✅ |
| name_zh | 珍妮弗·道德纳 | ✅ |
| name_en | Jennifer Doudna | ✅ |
| birth_date | 1964-02-19 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / CRISPR gene editing / RNA biology / X-ray crystallography，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jack Szostak | 师→生（博士导师） | 哈佛 1989 年 PhD，RNA 复制酶课题 |
| advisor-student | Thomas Cech | 师→生（博后导师） | 1991–1994 科罗拉多博尔德，核糖酶晶体项目 |
| advisor-student | Rachel Haurwitz | Doudna→学生 | 博士生，Caribou 联合创办人 |
| advisor-student | Janice Chen | Doudna→学生 | 博士生，Mammoth 联合创办人 |
| advisor-student | Lei Stanley Qi | Doudna→学生 | 博士生 |
| advisor-student | Samuel H. Sternberg | Doudna→学生 | 博士生，《A Crack in Creation》合著者 |
| co-honored | Emmanuelle Charpentier | 无向 | 2020 诺贝尔化学奖共同得主（另有 2015 Breakthrough、2018 Kavli、2020 Wolf） |
| co-honored | Virginijus Šikšnys | 无向 | 2018 Kavli 纳米科学奖共同得主 |
| spouse | Jamie Cate | 无向 | 科罗拉多博后期间相识，2000 年夏威夷结婚，同赴伯克利任教 |
| colleague | Jillian Banfield | 无向 | 2006 经 Google 检索找到 Doudna，引其进入 CRISPR 领域 |
| colleague | Michael Marletta | 无向 | 伯克利同事，2009 协助其从 Genentech 返回伯克利 |
| competitor | Feng Zhang | 无向 | Broad Institute，CRISPR-Cas9 专利之争（2017/2018 法院两审均判 Broad 胜） |

> **不予入库**（metadata/正文一笔带过、语义不符）：Tom Griffin（第一任丈夫，已离婚——避免 spouse 歧义）；Robert Tjian、Fyodor Urnov、Patrick Hsu、Dave Savage（COVID 团队，群体性合作无独立关系细节）；Don Hemmes、Jeanette Wong、Sharon Panasenko（成长影响者，非师承链）。

## 8. 奖项清单

- Alan T. Waterman Award（2000，NSF 35 岁以下最高荣誉）
- Eli Lilly Award in Biological Chemistry（2001）
- Searle Scholar / Beckman Young Investigators Award（1996）
- Breakthrough Prize in Life Sciences（2015，与 Charpentier）
- Gruber Prize in Genetics（2015）；Princess of Asturias Award（2015）
- Tang Prize（2016）；Canada Gairdner International Award（2016，与 Charpentier/Zhang/Horvath/Barrangou）；Heineken Prize（2016）
- Japan Prize（2017）；Albany Medical Center Prize（2017）
- NAS Award in Chemical Sciences（2018）；Kavli Prize in Nanoscience（2018，与 Charpentier、Šikšnys）
- Harvey Prize（2019，与 Charpentier、Zhang）；LUI Che Woo Prize（2019）
- Wolf Prize in Medicine（2020，与 Charpentier）
- **Nobel Prize in Chemistry（2020，与 Charpentier 共享）**
- Golden Plate Award（2017）；Guggenheim Fellowship（2020）；National Inventors Hall of Fame（2023）
- National Medal of Technology and Innovation（2025）；Priestley Medal（2026 得主，ACS）
- 院士：NAS（2002）、American Academy of Arts and Sciences（2003）、National Academy of Medicine（2010）、NAI（2014）、ForMemRS（2016）、Pontifical Academy of Sciences（2021，教宗任命）、NAE（2026）
- 荣誉博士：USC（2018）、Harvard（2023）

## 9. 机构清单

- 教育：Hilo High School（–1981）、Pomona College（BA 1985）、Harvard Medical School（PhD 1989）
- 任职：Massachusetts General Hospital 与 Harvard（研究员）；University of Colorado Boulder（1991–1994 博后，Cech 组）；Yale 分子生物物理与生物化学系（1994 助理教授 → 2000 Henry Ford II 教授）；UC Berkeley（2002 至今，生物化学与分子生物学教授，Li Ka Shing 冠名讲席）；HHMI 研究员（1997–）；LBNL faculty scientist；Gladstone Institutes senior investigator；UCSF 兼职教授
- 创办：Innovative Genomics Institute（2014，伯克利与 UCSF 合作，任主任）；Caribou Biosciences（2011）、Editas Medicine（2013–2014）、Intellia Therapeutics、Mammoth Biosciences（2017）、Scribe Therapeutics
- 命名机构：Doudna 超算（2025 宣布，NERSC/LBNL，Perlmutter 后继机）

## 10. 终审清单

- [ ] 生卒 1964-02-19 / 在世留白，出生地 Washington, D.C.
- [ ] 2020 诺奖"两人共享"表述准确；官方理由原句无 Cas9 字样
- [ ] CRISPR 发现史（Ishino 1987 → Mojica 表征 → Doudna/Charpentier 2012 可编程化）表述准确
- [ ] 专利战三结果（初审/上诉/欧洲）表述准确
- [ ] Kavli/Wolf/Gairdner 各年共享名单不混淆
- [ ] 博后导师 Cech、博士导师 Szostak 勿混；Pomona/ Harvard 教育口径准确
- [ ] 引语仅一句且可在 page.md 溯源；其余间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Jennifer_Doudna/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/Jennifer_Doudna_by_Chris_Michel_02.jpg` 已就位（2023 Christopher Michel 摄）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：直接引语必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与本批其他篇目（List/MacMillan/Bertozzi/Meldal）格式对齐

---

> **名单状态**：由主控统一收尾（`chemist/generate_21th_century_list.py`）。
