# Max Perutz（马克斯·佩鲁茨）立传提示词

> qid=Q78480 · 1914-05-19 – 2002-02-06 · 奥地利出生的英国分子生物学家 · 20 世纪 · 诺贝尔化学奖（1962，与 John Kendrew 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Max_Perutz/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 取 1962 年照 "Perutz in 1962"，或 1962 诺奖舞会夫妇照；若 images.txt 缺失则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 血红蛋白的建筑师\enspace·\enspace 英国（奥地利出生）`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（奥地利出生→英国）、出生地/去世地、教育（维也纳/Peterhouse, Cambridge）、博士（1940，Bragg 门下）、师承（Bernal 接纳入组）、核心领域（血红蛋白三维结构）、荣誉（OM CH CBE FRS）。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「X 射线穿过晶体的衍射点阵」母题——离散圆点阵暗示衍射图样。
5. **表格语义化 + 公式框**（★ 标注：实际晶体学数字随补充材料更新）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（同晶置换法：比较重原子结合前后衍射图样定相位；"polar zipper" 谷氨酰胺重复结合模型——均为 page.md 实载）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Max Ferdinand Perutz（中文惯称：马克斯·佩鲁茨；头衔 OM CH CBE FRS）
- **生卒**：1914-05-19 生于维也纳（时属奥匈帝国）→ 2002-02-06 逝于剑桥，享年 87；骨灰与父母 Hugo、Dely Perutz 同葬剑桥 Ascension Parish Burial Ground；妻 Gisela 2005-12-17 卒后骨灰同穴
- **国籍**：United Kingdom（奥地利出生；infobox 国籍含 United Kingdom/Austria）
- **身份**：分子生物学家（molecular biologist；血红蛋白结构测定者、MRC LMB 创建者与主席 1962–1979）
- **家庭**：犹太裔父母 Adele "Dely"（娘家姓 Goldschmidt）与纺织制造商 Hugo Perutz 之子，本人受洗天主教、晚年自认无神论但反对冒犯他人信仰。1942 年娶医学摄影师 Gisela Clara Mathilde Peiser（1915–2005，德国新教徒难民、其父生于犹太家庭）；子女 Vivien（1944，艺术史家）、Robin（1949，约克大学化学教授）
- **教育轨迹**：
  - Theresianum（维也纳中学）；父母望其学法律，中学时迷上化学
  - University of Vienna 化学本科（1936 年完成学位）
  - 经维也纳讲师 Fritz von Wessely 了解剑桥 Hopkins 生化团队进展，请 Herman Mark 教授到访剑桥时代为询问——Mark 遗忘询问 Hopkins，却顺访了正招研究生的 J.D. Bernal
  - 1936 年入剑桥 Cavendish Laboratory Bernal 晶体学研究组；学院先申请 King's 与 St. John's 未果，以"伙食最好"之由入选 Peterhouse（1962 年获选 Honorary Fellow）
- **导师**：J.D. Bernal（接纳其入组并鼓励用 X 射线衍射研究蛋白质）；博士论文**在 Lawrence Bragg 指导下于 1940 年完成**——infobox 博士导师只列 Bernal，frontmatter 双载 Bernal+Bragg
- **博士**：1940，University of Cambridge（马血红蛋白晶体结构）
- **研究领域**：分子生物学、X 射线晶体学——血红蛋白与肌红蛋白三维结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **维也纳的化学少年（1914–1936）**：纺织世家、父母望其当律师——他选了化学。
2. **一次遗忘改变一生（1936）**：Mark 忘了替他问 Hopkins，却把这位不懂晶体学的青年送进了 Bernal 的 Cavendish 晶体学组；"他很快学会了"——从此血红蛋白占其一生。
3. **冰川上的生存智慧（1938）**：德奥合并后父母破产、断供；凭滑雪、登山与晶体学知识加入三人小队研究瑞士冰川雪—冰转化，发表于 Proc. R. Soc. 的论文使其成为公认的冰川专家；1939 年 1 月获洛克菲勒基金会资助，3 月把父母从瑞士接到英国。
4. **敌侨拘留（1940）**：二战爆发后被作为德/奥背景人士拘留，依丘吉尔命令被送往纽芬兰数月，后回剑桥。
5. **哈巴谷计划与派克里特（1942）**：因冰川研究被征询"突击队能否藏身冰川之下"，继而受募入"哈巴谷计划"——大西洋中部冰制航空平台绝密工程；在 Smithfield 肉市地下秘密场所做冰木浆混合材料 pykrete 早期实验。
6. **分子生物学单元（1947）**：在 Bragg 支持下获 MRC 资助，于 Cavendish 建立分子生物学研究单元——吸引 Crick（1949）与 Watson（1951）先后来投。
7. **同晶置换法（1953）**：证明蛋白质晶体的 X 射线衍射可以通过比较有/无重原子结合的图样来确定相位——结构晶体学的关键突破。
8. **血红蛋白结构（1959）**：用该法测定运氧蛋白血红蛋白的分子结构；此后测定氧合/脱氧高分辨率结构，1970 年终于提出其作为分子机器的变构机制（脱氧↔氧合状态切换触发摄氧与放氧至肌肉等器官），后续二十年不断精化验证。
9. **1962 诺贝尔化学奖**：与 John Kendrew 共享——各自对血红蛋白与肌红蛋白结构的研究；2013 年（五十年后）X 射线晶体学测定的蛋白质结构已达 9,500 个。
10. **血液病的结构视角**：研究多种血红蛋白病的结构变化及对氧结合的影响；希望血红蛋白分子能用作药物受体、抑制或逆转镰状细胞贫血等遗传错误；还研究血红蛋白分子的种间变异如何适配不同栖息地与行为模式。
11. **极late岁月：极性拉链**：晚年转向亨廷顿病等神经退行性疾病的蛋白结构变化——证明发病与谷氨酰胺重复次数相关，其结合形成所谓 "polar zipper"。
12. **DNA 双螺旋的灰色一笔**：1950 年代初，Watson 与 Crick 攻关 DNA 期间，Perutz 把 Randall（King's College）实验室 1952 年未发表进展报告交给了二人——内含 Rosalind Franklin 拍摄的 X 射线衍射图像，对双螺旋结构的确立至关重要；此举未经 Franklin 知情同意，后被 Randall 等人批评；Perutz 后撰文辩护：报告内容 Franklin 在 1951 年底讲过、Watson 在场，且该报告本为 MRC 联络委员会而作。
13. **科学家—公民与作家**：1994 年剑桥 "Living Molecules" 讲座抨击 Popper、Kuhn、Dawkins（批评 Popper 假说—反驳论与 Kuhn 范式转移论对分子生物学的不适用，主张不冒犯他人宗教信仰）；9·11 后数日内致信布莱尔首相呼吁勿以军事手段回应；为 *The New York Review of Books* 常撰稿（文集 *I wish I had made you angry earlier*，1998）；1985 年《纽约客》刊出其拘留营回忆 "That Was the War: Enemy Alien"；1997 年获 Lewis Thomas Prize（科学写作奖）；1980 年皇家研究所圣诞讲座 "The Chicken, the Egg and the Molecules"。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（皇紫蓝 royalpurple） | `#283593` | 衍射点阵的深紫与分子生物学的庄重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（血红蛋白 badgeHb） | `#8E2A2A` | 绛红血红蛋白结构与变构 |
| 分类色 2（X 射线晶体学 badgeXray） | `#2E5A9E` | 蓝同晶置换 / 相位问题 |
| 分类色 3（MRC LMB badgeLMB） | `#1B7A43` | 绿分子生物学圣殿 |
| 分类色 4（冰川与战时 badgeIce） | `#D97B29` | 琥珀冰川 / pykrete / 拘留营 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落成点阵感），呼应「X 射线衍射图样」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（文件路径见 manifest `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`；**不要复制 wav 文件**）
- **风格**：怀旧 / 历史纵深 / 大陆流亡叙事
- **匹配理由**：
  - "PAST（往昔）" 匹配其身份底色——1938 年逃离维也纳的流亡者，在大英的屋檐下重建科学生命
  - "历史纵深" 匹配血红蛋白 23 年的攻关长跑（1936 入题 → 1959 结构）
  - 曲名的回望气质呼应其晚年大量写作回忆与论战（NYRB 文集）
- **时长**：以实际文件为准 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 血红蛋白的建筑师 / Max Perutz 1914–2002 + 四色 badge + 右上头像 + 国籍行（英国·奥地利出生）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  佩鲁茨的一生 — Sanger 式时间线（10 节点：1914→1936→1938→1940→1942→1947→1953→1959→1962→2002）
04  维也纳与转折（1914–1936）— 表格「时间|事件|结果」（Theresianum → Vienna → Mark 的遗忘 → Bernal 组）
05  冰川与流亡（1938–1940）— 表格「处境|行动|结果」（断供 → 冰川研究 → 洛氏资助接父母 → 敌侨拘留）
06  哈巴谷计划（1942）— 表格「任务|材料|结局」+ 公式框：pykrete 冰木浆复合材料示意
07  分子生物学单元（1947）— 表格「支持|组建|意义」（Bragg 支持、MRC 资助、Crick/Watson 来投）
08  同晶置换法（1953）— 表格「问题|方法|意义」+ 公式框：重原子结合前后衍射图样定相位
09  血红蛋白结构（1959–1970）— 表格「阶段|成果|意义」+ 1962 诺奖（共享 Kendrew）
10  变构机制与血液病（1970–1990s）— 表格「对象|发现|方向」（1970 变构、镰状细胞、种间变异）
11  polar zipper（晚年）— 表格「疾病|假说|验证」+ 公式框：谷氨酰胺重复结合 "polar zipper"
12  DNA 报告的灰色一笔 — 表格「事件|争议|辩护」（1952 MRC 报告交给 Watson/Crick；未经 Franklin 同意；Perutz 自辩）
13  科学家—公民与作家 — Sanger 式「维度|代表|意义」表格（1994 论战 Popper/Kuhn/Dawkins、9·11 致信布莱尔、NYRB 文集、Lewis Thomas Prize）
14  结尾 — 「他用了二十三年，终于看见了血液如何抓住又放开每一口氧气。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1962 诺奖 | 与 **John Kendrew 共享**——各自研究血红蛋白（Perutz）与肌红蛋白（Kendrew）；完整官方 citation（"for their studies of the structures of globular proteins"）**页面无载，禁写**，用 page.md 口径"各自对血红蛋白与肌红蛋白结构的研究" |
| 博士导师 | 论文**在 Lawrence Bragg 指导下 1940 年完成**；Bernal 是接纳其入组、引导其做蛋白质晶体学的导师——两人均 page.md 明载，入库时 note 分写清楚，勿只写一人 |
| 姓氏区分 | William Lawrence Bragg（W. L. Bragg）——勿与其父 W. H. Bragg 混淆（页面未提其父，禁写父子叙述） |
| DNA 报告 | Perutz 把 1952 年未发表报告交给 Watson/Crick **未经 Franklin 知情同意**，被 Randall 等批评——须如实呈现，不可洗白也不可上纲为"窃取"；Perutz 自辩三点（Franklin 1951 年已讲过、Watson 在场、报告为 MRC 委员会而作）一并呈现 |
| 拘留细节 | 依**丘吉尔命令**送纽芬兰——归因明确；勿写"德国政府" |
| pykrete 用途 | 哈巴谷计划是建大西洋冰制航空加油平台——勿写成"航空母舰服役"；项目未成，只有实验 |
| 宗教叙事 | 犹太裔但受洗天主教、晚年无神论、反对冒犯他人信仰、"even if we do not believe in God, we should try to live as though we did."（page.md 唯一接近引语的句子）——口径谨慎 |
| 9·11 致信 | 致布莱尔信是 page.md 实载（原句可引）——政治敏感度高，建议一句带过或回避全文引用 |
| LMB 数据 | "十四位科学家获诺奖"（founded and chaired 1962–79）——勿写"员工"或凑具体名单 |
| 1970 机制 | 1970 年提出的是"脱氧↔氧合切换的分子机器机制"——勿写成 1959 年一并完成 |
| Huntington | 证明发病与谷氨酰胺重复次数相关、形成 "polar zipper"——勿写"治愈" |
| 学院入选 | 以"伙食最好"选 Peterhouse（本人自述口径）——勿美化成学术考量 |
| 引语红线 | 除 9·11 信与信仰句外，其余叙述一律间接转述；1985《纽约客》篇名 "That Was the War: Enemy Alien" 为篇名可引 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q78480 | ✅（复用库内 Max Perutz 记录回填） |
| name_zh | 马克斯·佩鲁茨 | ✅ |
| name_en | Max Perutz | ✅（库内既有形式） |
| birth_date | 1914-05-19 | ✅ |
| death_date | 2002-02-06 | ✅ |
| nationality | United Kingdom（出生国 Austria 单列 rank 1） | ✅ |
| primary_occupation | molecular biologist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（立传 Beamer 完成后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| haemoglobin structure | 0 | 血红蛋白结构 | 1962 诺奖理由 + 终身课题 |
| X-ray crystallography | 1 | X 射线晶体学 | 同晶置换法发明者 |
| molecular biology | 2 | 分子生物学 | infobox Fields + LMB 创建者 |
| protein allostery | 3 | 蛋白质变构调节 | 1970 机制与专著 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**
**★ 对手方规范名：John Kendrew（与 chem-batch-12 的 John Kendrew 篇互指一致，防分裂 stub）。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Desmond Bernal | 师→生 | 1936 接纳入 Cavendish 晶体学组，引导其用 X 射线研究蛋白质（infobox 博士导师） |
| advisor-student | William Lawrence Bragg | 师→生 | 博士论文在其指导下 1940 年完成；后支持其获 MRC 资助建立单元 |
| advisor-student | Francis Crick | Perutz → 学生 | infobox Doctoral students；1949 加入其单元 |
| advisor-student | John Keith Moffat | Perutz → 学生 | infobox Doctoral students |
| co-honored | John Kendrew | 无向 | 1962 诺贝尔化学奖共同得主（血红蛋白/肌红蛋白） |
| colleague | James D. Watson | 无向 | 1951 加入其分子生物学单元 |
| controversy | Rosalind Franklin | 无向 | 1952 未发表 MRC 报告（含其 X 射线衍射图）交予 Watson/Crick，未经其知情同意，后受 Randall 等批评；Perutz 撰文自辩 |
| spouse | Gisela Clara Peiser | 无向 | 1942 结婚（正文全名 Gisela Clara Mathilde Peiser，1915–2005）；医学摄影师、德国难民 |

> **禁入库名单（转述提及、无人际明载或非学术人际）**：Vivien Perutz / Robin Perutz（子女虽 page.md 明载，按本批口径不入库，仅叙事呈现）、Herman Mark（遗忘传话的非人际事件）、Gowland Hopkins / Fritz von Wessely（仅提及）、John Randall / Maurice Wilkins（批评与报告归属语境）、Karl Popper / Thomas Kuhn / Richard Dawkins（学术论战对象非合作者）、Tony Blair（通信对象）、Winston Churchill（命令归因）。

## 8. 奖项清单

- Nobel Prize for Chemistry（1962，与 John Kendrew 共享；各自对血红蛋白与肌红蛋白结构的研究）
- Fellow of the Royal Society，FRS（1954）
- Commander of the Order of the British Empire，CBE（1963）；American Academy of Arts and Sciences（1963）
- Austrian Decoration for Science and Art（1967）；Wilhelm Exner Medal（1967）
- Sir Hans Krebs Medal（1968）；American Philosophical Society（1968）；美国国家科学院（1970）
- Royal Medal（1971）
- Member of the Order of the Companions of Honour，CH（1975）
- Copley Medal（1979）
- Member of the Order of Merit，OM（1988）
- Otto Warburg Medal；Croonian Medal and Lecture；EMBO Membership（1964）；Leopoldina（1964）
- 荣誉博士：University of Vienna（1965）、Salzburg University、University of Paris-XI
- Lewis Thomas Prize for Writing about Science（1997）
- Honorary Fellow of Peterhouse（1962）；Honorary member of the British Biophysical Society
- 纪念：European Crystallographic Association 设 Max Perutz Prize

## 9. 机构清单

- 教育：Theresianum（维也纳）；University of Vienna（BSc，1936）；Peterhouse, Cambridge；University of Cambridge（PhD 1940）
- 任职：Cavendish Laboratory（1936 入 Bernal 晶体学组）；MRC 分子生物学研究单元（1947 于 Cavendish 创建）；MRC Laboratory of Molecular Biology, LMB（1962–1979 创建者兼主席；旗下十四位科学家获诺奖）；1952 King's College（Randall 实验室）MRC 联络委员会报告提交者
- 战时：瑞士冰川三人小队（1938）；Project Habakkuk（1942，pykrete 实验，Smithfield 肉市地下）
- 纪念：Max Perutz Prize（ECA）；剑桥 Ascension Parish Burial Ground 长眠地；著作 *Proteins and Nucleic Acids*（1962）、*Is Science Necessary?*（1989）、*I Wish I'd Made You Angry Earlier*（1994/1998）、*Science is Not a Quiet Life*（1997）、书信集 *What a Time I Am Having*（2009）

## 10. 终审清单

- [ ] 生卒 1914-05-19 / 2002-02-06，享年 87，出生地维也纳、去世地剑桥；骨灰葬 Ascension Parish Burial Ground
- [ ] 1962 **共享**（John Kendrew）；获奖口径用 page.md"各自对血红蛋白与肌红蛋白结构的研究"
- [ ] Bernal（入组导师）与 Bragg（论文导师）双导师表述清楚；对手方规范名 John Kendrew / William Lawrence Bragg
- [ ] 同晶置换 1953 → 血红蛋白结构 1959 → 变构机制 1970 → polar zipper 晚年——时间链勿压缩
- [ ] DNA 报告事件：未经 Franklin 知情同意 + Perutz 三点自辩——双向呈现
- [ ] 唯一可引原句：9·11 致信原文与信仰句（建议回避 9·11 全文）；其余间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Max_Perutz/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：核对 images/（1962 年照或诺奖舞会照）
- [ ] **国籍**：封面顶部明示英国（奥地利出生）
- [ ] **引语核对**：引语必须在 page.md 原文找到（信仰句；9·11 信如引用）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 等）对齐；与物理学家侧 Bragg 相关篇目核对规范名

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
