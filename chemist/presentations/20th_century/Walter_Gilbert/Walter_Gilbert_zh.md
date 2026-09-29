# Walter Gilbert（沃尔特·吉尔伯特）立传提示词

> qid=Q217486 · 1932-03-21 出生（在世） · 美国生物化学家 / 物理学家 · 20 世纪 · 诺贝尔化学奖（1980，与 Frederick Sanger 共享一半；Paul Berg 独得另一半）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Walter_Gilbert/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（page.md 内嵌 National Library of Medicine 肖像 WalterGilbert2.jpg 可作候选；`images/` 缺则按常规流程下载，404 装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 从物理到生命的摆渡人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生年（在世，卒年留白）、国籍、出生地、教育（Harvard BA/MA、Cambridge PhD）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「测序阶梯 / 基因片段」母题——梯状排布的圆点暗示化学降解法的片段阶梯。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Maxam–Gilbert 化学测序示意：碱基特异性断裂 → 片段阶梯 → 读序。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Walter Gilbert（中文惯称：沃尔特·吉尔伯特；ForMemRS）
- **生卒**：1932-03-21 生于马萨诸塞州波士顿（在世，卒年留白）
- **国籍**：United States（美国）
- **身份**：生物化学家、物理学家、分子生物学先驱（1980 诺贝尔化学奖得主）
- **家庭**：犹太家庭——母 Emma（娘家姓 Cohen，儿童心理学家）、父 Richard V. Gilbert（经济学家）；7 岁随父迁华盛顿特区（父为 Harry Hopkins 的新政智库工作）；8 岁结识 I. F. Stone 之女 Celia，21 岁结婚（1953，妻 Celia Stone，育有二子女）
- **教育轨迹**：
  - Sidwell Friends School（华盛顿）
  - Harvard University（化学+物理 baccalaureate，1953；物理硕士，1954）
  - University of Cambridge（物理 PhD，1957，导师 Abdus Salam；论文《On generalised dispersion relations and meson-nucleon scattering》，登记年份 1958）
- **导师**：Abdus Salam（诺奖得主，博士导师）
- **研究领域**：分子生物学、DNA 测序、生物化学、物理学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **新政智库旁的童年（1932–1939）**：波士顿出生，7 岁迁华盛顿——经济学家之子、记者 I. F. Stone 家的常客。
2. **物理学的正规军（1953–1957）**：哈佛化学+物理本科、物理硕士，再赴剑桥师从 **Abdus Salam** 获物理 PhD——弦论与散射振幅的论文，起点是理论物理。
3. **重回哈佛（1956/1959）**：1956 年回哈佛，1959 年任物理助理教授；1964 升生物物理副教授，1968 升生物化学教授。
4. **妻子的实验室改变了他**：妻 Celia 为 **James Watson** 工作，Gilbert 因此对分子生物学产生兴趣；1960 年代大部分时间 Watson 与 Gilbert **联合主持同一个实验室**，直到 Watson 去 Cold Spring Harbor。
5. **lac 阻遏物竞赛（1960s）**：与博士生 **Benno Müller-Hill** 第一个纯化 lac 阻遏物——险胜 Mark Ptashne，拿下第一个基因调控蛋白。
6. **学生的希格斯线索（1962）**：物理博士生 **Gerald Guralnik** 延续 Gilbert 关于无质量粒子的工作——后被视为希格斯玻色子发现的重要线索。
7. **Maxam–Gilbert 测序法（1977）**：与 **Allan Maxam** 发展出化学降解测序法（利用 Andrei Mirzabekov 的化学方法）；1977 年论文 "A new method for sequencing DNA" 获 2017 年 Citation for Chemical Breakthrough Award。
8. **胰岛素竞赛的失利**：以重组 DNA 合成胰岛素的路线输给了 Genentech（用核苷酸构建基因的路线）；剑桥（马萨诸塞）的临时暂停令迫使团队把实验迁往英国一处生物武器场地。
9. **内含子与外显子（1978）**：在 Nature 的 "News and Views" 通信 "why genes in pieces?" 中首创 **intron / exon** 术语并给出内含子演化的解释。
10. **RNA 世界假说（1986）**：提出生命起源的 RNA 世界假说——基于 Carl Woese 1967 年的概念。
11. **人类基因组先行者（1986–1991）**：1986 Santa Fe 会议上宣称 "The total human sequence is the grail of human genetics"（人类总序列是人类遗传学的圣杯）；1987 提议创办 Genome Corporation；1991 在 Nature 展望基因组完成后的计算生物学图景。
12. **生物技术创业潮**：Biogen 共同创始人（与 Kenneth Murray、Phillip Sharp、Charles Weissman；离开哈佛任 CEO 后被董事会请辞）；Myriad Genetics 共同创始人（与 Mark Skolnick、Kevin Kimberlin，任首届董事长）；1996 与 Stuart B. Levy 共创 Paratek Pharmaceuticals（董事长至 2014）；Scripps 研究所科学治理委员会成员；哈佛 Society of Fellows 主席。
13. **从科学家到艺术家（2001–）**：2001 从哈佛退休后投身数字摄影艺术（作品如 Purple Swirl）——艺术与科学的第二次融合。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（海军蓝 navyblue） | `#37548D` | 物理与生物之间的深水区（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（化学测序 badgeSeq） | `#2E5A9E` | 蓝 Maxam–Gilbert 片段阶梯 |
| 分类色 2（基因调控 badgeLac） | `#1B7A43` | 绿 lac 阻遏物 / intron-exon |
| 分类色 3（RNA 世界 badgeRNA） | `#D97B29` | 琥珀生命起源假说 |
| 分类色 4（生物技术 badgeBio） | `#C0395B` | 玫瑰 Biogen / Myriad / 基因组圣杯 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「测序阶梯」梯状排布的几何。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（文件 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，不复制 wav）
- **风格**：辽阔 / 漂移 / 跨界远航
- **匹配理由**：
  - "辽阔" 匹配其多重身份——理论物理 → 分子生物学 → 基因组学 → 艺术摄影，一次次跨越学科海域
  - "漂移" 匹配其创业轨迹——哈佛讲席与 Biogen CEO 之间的往返，学界与商界间的摆渡
  - "远航" 匹配基因组圣杯的愿景——1986 年便望向人类全序列的地平线
- **时长**：以实际曲目时长为准，超过 15 页 × 7 秒由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 从物理到生命的摆渡人 / Walter Gilbert 1932– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生年留白/国籍/教育/博士导师/出生地/领域/荣誉）
03  吉尔伯特的一生 — 时间线（10 节点：1932→1953→1957→1959→1960s→1977→1979/80→1986→2001→今日）
04  早年：新政智库旁的童年 (1932–1950) — 表格「时间|事件|结果」
05  物理学博士 (1953–1959) — 表格「阶段|机构|结果」+ 剑桥 Salam 门下
06  转向分子生物学 (1960s) — 表格「契机|行动|结果」（Watson 联合实验室/lac 阻遏物）
07  Maxam–Gilbert 测序法 (1977) — 表格「问题|方法|结果」+ 公式框：化学降解 → 片段阶梯 → 读序
08  内含子、外显子与 RNA 世界 (1978/1986) — 表格「概念|内容|意义」+ 公式框：why genes in pieces?
09  1980 诺贝尔化学奖 — 表格「人物|半份|贡献」+ 公式框：Gilbert/Sanger=测序；Berg=重组 DNA
10  生物技术创业潮 — 表格「公司|角色|结果」（Biogen/Myriad/Paratek）
11  荣誉清单 — 「类别|代表|意义」表格（含 itemize 荣誉清单）
12  人类基因组圣杯 — 流程图页（1986 Santa Fe → 1987 Genome Corp → 1991 Nature 展望）
13  遗产：第二人生 — 四分类遗产盒 + 公式框：从测序阶梯到数字摄影
14  结尾 — 「物理教会他方程，生命教会他读序。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1980 诺奖分配 | Gilbert 与 Sanger **共享一半**（核苷酸测序方法）；Berg **独得另一半**（重组 DNA）——页面口径 "Gilbert and Sanger were recognized for their pioneering work in devising methods for determining the sequence of nucleotides in a nucleic acid"；勿写三人平分 |
| PhD 年份张力 | 正文作 1957（"supervised by Abdus Salam in 1957"），论文登记页作 1958——二选一并在提示词/正文加注 |
| 回哈佛年份张力 | 正文 "returned to Harvard in 1956" 与 PhD 1957 存在张力——照原文转述，勿自行"修正" |
| Watson 实验室 | 1960 年代大部分时间 Watson 与 Gilbert **联合主持**实验室——勿写 Gilbert "在 Watson 手下工作" |
| lac 阻遏物 | Gilbert 与 Müller-Hill "just beating out Mark Ptashne"——竞争表述照原文，勿写成 Ptashne 无贡献 |
| 测序法分工 | 化学方法由 **Andrei Mirzabekov** 发展——勿把化学全归 Maxam–Gilbert 二人原创 |
| 胰岛素竞赛 | 输给 Genentech 是**事实叙述**；剑桥马萨诸塞临时暂停令迫其迁往英国"生物武器场地"——照原文口径，勿美化或渲染 |
| RNA 世界 | 1986 年 Gilbert 提出，**基于 Carl Woese 1967 年概念**——归属勿只写 Gilbert |
| 争议内容 | 对 David Baltimore 案的批评与 AIDS 起因之争（HIV/AIDS denialism）属敏感争议——Beamer 篇建议**略过**或仅中性一句，不展开 |
| 在世口径 | 1932-03-21 生，无卒日——生卒行留白三处（封面/身份页/时间线）保持一致 |
| 公司角色 | Biogen：被董事会"asked to resign"；Myriad：**首届董事长**；Paratek：董事长至 2014——角色与结局勿混 |
| frontmatter 噪声 | field_of_work 含 physics——正文双领域 biochemistry + physics 可写，但主身份以 biochemist 为准 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q217486 | ✅（UPD 回填 stub #1127） |
| name_zh | 沃尔特·吉尔伯特 | ✅ |
| name_en | Walter Gilbert | ✅（与库内 #1127 精确一致） |
| birth_date | 1932-03-21 | ✅ |
| death_date | 无（在世） | ✅ 留白 |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry + physics（person_field 细分：molecular biology / DNA sequencing / biochemistry / genomics，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 竞争对手**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Abdus Salam | 师→生（博士导师） | 剑桥物理 PhD，Salam 为诺奖得主 |
| colleague | James Watson | 无向 | 1960 年代大部分时间联合主持实验室 |
| colleague | Allan Maxam | 无向 | 共同发明 Maxam–Gilbert 化学测序法 |
| colleague | Andrei Mirzabekov | 无向 | 其化学方法用于 Maxam–Gilbert 测序 |
| colleague | Kenneth Murray / Phillip Sharp / Charles Weissman | 无向 | Biogen 共同创始人 |
| colleague | Mark Skolnick / Kevin Kimberlin | 无向 | Myriad Genetics 共同创始人 |
| colleague | Stuart B. Levy | 无向 | 1996 共同创立 Paratek Pharmaceuticals |
| competitor | Mark Ptashne | 无向 | lac 阻遏物纯化竞赛中险胜 |
| influence | Carl Woese | 无向 | 1986 RNA 世界假说基于其 1967 年概念 |
| co-honored | Frederick Sanger | 无向 | 1980 诺贝尔化学奖共享一半 |
| co-honored | Paul Berg | 无向 | 1980 诺贝尔化学奖，Berg 独得另一半 |

**门生（Gilbert → 学生，源自本地 Wikipedia 正文 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Benno Müller-Hill | Gilbert → 学生 | 共同首个纯化 lac 阻遏物 |
| advisor-student | Gerald Guralnik | Gilbert → 学生 | 1962 延续其无质量粒子工作，后成希格斯发现重要线索 |
| advisor-student | George M. Church | Gilbert → 学生 | 博士生 |
| advisor-student | Didier Stainier | Gilbert → 学生 | 博士生 |
| advisor-student | Helen Donis-Keller | Gilbert → 学生 | 博士生 |
| advisor-student | Jack Greenblatt | Gilbert → 学生 | 博士生 |

> **禁入库名单**：I. F. Stone（岳父，仅家庭叙事）；Harry Hopkins（父亲上司）；David Baltimore / Thereza Imanishi-Kari（争议事件当事人，非个人关系）。metadata.json 无其他 page.md 未载关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1980，与 Sanger 共享一半；Berg 独得另一半）
- NAS Award in Molecular Biology（1968，US Steel Foundation）
- Harvard Ledlie Prize（1969）
- Warren Triennial Prize, Massachusetts General Hospital（1977）
- Louis and Bert Freedman Foundation Award（1977）
- Prix Charles-Leopold Mayer, 法国科学院（1977）
- Canada Gairdner International Award（1979）
- Louisa Gross Horwitz Prize, Columbia University（1979，与 Frederick Sanger 同获奖）
- Albert Lasker Award for Basic Medical Research（1979）
- Foreign Member of the Royal Society, ForMemRS（1987）
- Biotechnology Heritage Award（2002）
- Citation for Chemical Breakthrough Award（2017，ACS 化学史分会，授予哈佛分子与细胞生物学系）
- Guggenheim Fellowship；Humboldt Prize；American Physical Society Fellow（年份未载）

## 9. 机构清单

- 教育：Sidwell Friends School → Harvard University（BA 1953、MA 1954）→ University of Cambridge（PhD 1957，导师 Abdus Salam）
- 任职：Harvard 物理助理教授（1959）→ 生物物理副教授（1964）→ 生物化学教授（1968）→ American Cancer Society 分子生物学教授（1972）→ Biogen CEO（离哈佛期间）→ 1985 回哈佛 → 2001 退休
- 创业：Biogen（共同创始人、首届董事长之一、曾任 CEO）、Myriad Genetics（共同创始人、首届董事长）、Paratek Pharmaceuticals（1996，董事长至 2014）
- 其他：Scripps 研究所科学治理委员会成员；哈佛 Society of Fellows 主席

## 10. 终审清单

- [ ] 生年 1932-03-21、在世留白三处一致
- [ ] 1980 诺奖"与 Sanger 共享一半 / Berg 独得另一半"表述准确
- [ ] PhD 1957/1958 与回哈佛 1956 两处年份张力已加注
- [ ] Watson 联合主持实验室、lac 竞赛险胜 Ptashne 表述照原文
- [ ] intron/exon（1978）与 RNA 世界（1986，基于 Woese）归属准确
- [ ] Baltimore 案与 AIDS 争议未在正文展开
- [ ] 引语全部可在本地 Wikipedia 原文溯源（"The total human sequence is the grail of human genetics"、"why genes in pieces?"、1980 获奖口径）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Walter_Gilbert/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：下载 Wikipedia 肖像（National Library of Medicine 版 2008 照；404 用 REST API；仍失败装饰圆占位）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（圣杯句、why genes in pieces?）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
