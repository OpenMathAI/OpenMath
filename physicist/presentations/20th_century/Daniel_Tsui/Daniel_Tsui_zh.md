# Daniel C. Tsui（崔琦）立传提示词

> qid=Q202138 · 1939-02-28 –（在世）· 美国华裔物理学家 · 20 世纪 · 1998 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Daniel_C._Tsui/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。⚠️ `images.txt` 为空（无任何图片 URL）——**封面头像用装饰圆占位**（`\IfFileExists` 条件包含 + `\faIcon{user}\enspace Portrait` 兜底）；Review-1 时优先尝试补真实肖像（可试 Commons `Special:FilePath` 检索 "Daniel Tsui" / "Daniel C. Tsui" 类文件名，404 或返回 HTML 即换名或保持占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`，身份页注"生于中国河南、已入籍美国"），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名·中文名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「强磁场下的二维电子 / 无序与关联」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Daniel Chee Tsui（中文名 **崔琦**，拼音 Cuī Qí）
- **生卒**：1939-02-28 生于中国河南省宝丰县范庄（Fanzhuang, Baofeng County, Henan，时为中华民国）；在世（death_date 留白）
- **国籍**：美国（公民身份 Citizenship: United States；**已入籍** naturalized U.S. citizen；生于中国）
- **身份**：物理学家（实验物理 / 电机工程）；普林斯顿大学电机工程系荣休教授
- **家庭**：生于**双亲均不识字的农家**；妻 Linda Varland（芝加哥大学读本科时相识，女方毕业后结婚）；二女 Aileen、Judith——Judith 1991 年以 magna cum laude 获普林斯顿人类学 BA，现任华盛顿大学医学院医学副教授
- **童年自述（page.md 明载原话可引）**：早年的记忆"filled with the years of drought, flood and war which were constantly on the consciousness of the inhabitants of my over-populated village"（旱、涝与战争持续萦绕在过剩人口村庄居民的心头）
- **教育轨迹**：
  - 1951 年赴英属香港，入九龙**培正中学**（Pui Ching Middle School）；入学次年从六年级程度开始接受正规教育；因不熟粤语遇到困难
  - 1957 年中学毕业，获**台湾大学医学院**录取，但因不确定能否返回大陆家人身边而留港，入政府两年制 Special Classes Centre 备考香港大学
  - 1958 年春获**全额奖学金**入奥古斯塔纳学院（Augustana College，伊利诺伊，其教会牧师的路德宗母校），Labor Day 后抵美
  - 1961 年奥古斯塔纳学院毕业（Phi Beta Kappa 荣誉学会成员，**全院唯一华裔学生**）
  - 1967 年芝加哥大学**物理学博士**，论文 *"de Haas-van Alphen effect and electronic band structure of nickel"*（镍的 de Haas-van Alphen 效应与电子能带结构），导师 **Royal Stark**
- **博士导师**：Royal Stark
- **研究领域**：实验物理、电机工程（半导体薄膜与微结构的电学性质、固体物理）
- **任职轨迹**：芝加哥大学博士后一年 → 1968 年入贝尔实验室（固体物理研究）→ 1982 年 2 月在两位诺奖得主支持下转普林斯顿大学电机工程与计算机科学系 → 2010 年荣休（普林斯顿 28 年）；另曾任哥伦比亚大学物理系兼职高级研究科学家、波士顿大学研究教授

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **河南农家的孩子（1939–1951）**：宝丰县范庄、双亲不识字的农家；生于二战战火中——旱、涝、战争的童年（引其自述原话，可溯源）。
2. **十二岁南下香港（1951）**：独自赴港入培正中学，从六年级程度读起、苦攻粤语——"13 岁赴美"是讹传，实为 12 岁赴港、19 岁赴美（见陷阱表）。
3. **港大备考路上的转折（1957–1958）**：台大医学院录取而未去（顾虑无法返乡探亲）；备考香港大学之际，一纸路德宗全额奖学金把他带向美国奥古斯塔纳学院。
4. **全院唯一的华裔毕业生（1961）**：Phi Beta Kappa、三年完成学业——小学院的顶尖生。
5. **奔着杨振宁与李政道的足迹去芝加哥（1961–1967）**：受两位在芝大读过的华裔诺奖得主影响，立志赴芝大攻物理；1967 年博士（镍的 de Haas-van Alphen 效应，导师 Royal Stark）。
6. **贝尔实验室（1968–1982）**：不入主流（不追光学、高能带结构或器件应用），专注**新兴的二维电子物理**——冷门选择的远见。
7. **1982：分数量子霍尔效应的实验发现（本篇核心页）**：与 Störmer 合作发现**分数量子霍尔效应**（page.md 口径为 1982；⚠️ Störmer 篇载 1981-10 跨篇差异，见陷阱表）；次年 Laughlin 给出理论解释。
8. **1998 年诺贝尔物理学奖**：获奖理由 "for their discovery of a new form of quantum fluid with fractionally charged excitations"（总名单中文：表彰他们发现具有分数电荷激发的新型量子流体）；与 Robert B. Laughlin、Horst L. Störmer 共享；Nobel 演讲 1998-12-08 *Interplay of Disorder and Interaction in Two-Dimensional Electron Gas in Intense Magnetic Fields*。
9. **诺奖同年转普林斯顿（1982）**：发现之后旋即在**两位诺奖得主的支持下**受聘普林斯顿电机工程与计算机科学系——1982 年 2 月入职，执教 28 年至 2010 年荣休。
10. **为科学预算发声（2008）**：20 位美国物理诺奖得主联名致函小布什总统，要求为 DOE/NSF/NIST 追加紧急经费（与 Phillips 同为署名人——两篇互查）。
11. **荣誉与院士名单**：Buckley 凝聚态奖（1984，与 Störmer 共享）、NAS（1987）、美国艺术与科学院（2000）、中国科学院外籍院士（2000）、美国国家工程院（2004）、台湾"中研院"院士；港大、北大、香港中文大荣誉博士（metadata）。
12. **从范庄到普林斯顿的弧线（遗产页）**：农家子弟 → 香港苦读 → 美国小学院 → 芝加哥 → 贝尔 → 普林斯顿——20 世纪华裔科学家的经典迁徙叙事；2010 年普林斯顿荣休。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（中原赭褐） | `#6B3A2A` | 河南黄土的乡土底色 / 从范庄出发的生命原点 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（二维电子气 — 深蓝） | `#2B5F8C` | 二维电子系统 / 半导体薄膜与微结构 |
| 分类色 2（分数量子霍尔 — 玫瑰） | `#A3355C` | FQHE 实验发现 / 新型量子流体 |
| 分类色 3（求学之路 — 深绿） | `#3A6B4F` | 培正中学 / 奥古斯塔纳 / 芝加哥 |
| 分类色 4（普林斯顿与荣誉 — 琥珀） | `#C08A2E` | 普林斯顿 28 年 / 各国院士与荣誉博士 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）叠加**一层细密网格线**，呼应「二维电子气——电子被约束在平面晶格中、强磁场下凝聚为量子流体」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：上升 / 电影感 / 学术攀登（从河南农村到普林斯顿讲席的漫长攀登）
- **选定曲目**：Really Slow Motion **Elevation**（上升 / 电影，来自 inspiring-electronic 合辑备选），匹配"一级级向上的求学之路"——范庄、香港、伊利诺伊、芝加哥、贝尔、普林斯顿。
- **落地文件**：`physicist/presentations/20th_century/Daniel_Tsui/Elevation.wav`（复制自 `music_audio/inspiring-electronic/` 目录下 Elevation 对应 wav，不入 git）。
- **匹配理由**：崔琦的叙事主线是"攀登"而非单点突破，上升感的电影配乐贴合其人生弧线；与本批次其余五人曲目不重复。

## 3.6 研究领域表（数据库入库用，第 4 步）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | experimental physics | 实验物理 | page.md infobox Fields 载 | 身份页 |
| 1 | condensed matter physics | 凝聚态物理 | 固体物理 / 二维电子物理研究 | 贝尔页 |
| 2 | fractional quantum Hall effect | 分数量子霍尔效应 | 与 Störmer 的实验发现（1982），1998 诺奖核心 | 核心贡献页 |
| 3 | semiconductor physics | 半导体物理 | 薄膜与微结构的电学性质 | 导语页 |
| 4 | electrical engineering | 电机工程 | 普林斯顿电机工程系讲席，infobox Fields 并载 | 普林斯顿页 |

## 3.7 术语清单（第 9 步审查用）

| 英文 | 中文 | 风险 |
|------|------|------|
| fractional quantum Hall effect | 分数量子霍尔效应 | 实验发现=Tsui+Störmer，勿写独自发现 |
| two-dimensional electrons | 二维电子 | 贝尔实验室专注的新兴领域 |
| de Haas-van Alphen effect | 德哈斯-范阿尔芬效应 | 博士论文主题（镍的能带结构） |
| thin films and microstructures | 薄膜与微结构 | 研究领域表述照 page.md |
| Pui Ching Middle School | 培正中学 | 九龙，1951 入学 |
| Augustana College | 奥古斯塔纳学院 | 路德宗母校奖学金，1961 毕业 |
| Phi Beta Kappa | 荣誉学会 | 1961 毕业时入选 |
| naturalized U.S. citizen | 已入籍美国 | 生于中国河南，勿写「13 岁赴美」 |
| Chinese Academy of Sciences | 中国科学院 | 2000 外籍院士 |
| Academia Sinica | 「中研院」 | 台北，院士，page.md 未给年份留白 |

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「分数量子霍尔效应 · 美国」+ 崔琦 1939– + 右上头像（装饰圆占位）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名·中文名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：二维电子物理 / 分数量子霍尔效应实验发现 / 普林斯顿讲席 / 华裔科学家传承
4. **河南范庄的农家少年**（1939–1951）：双亲不识字、战火童年——引其自述原话（可溯源）
5. **香港：培正中学**（1951–1957）：十二岁南下、从六年级读起、粤语难关
6. **台大录取与奖学金转折**（1957–1958）：未去台大的原因、路德宗奖学金、Labor Day 后抵美
7. **奥古斯塔纳与芝加哥**（1958–1967）：全院唯一华裔、Phi Beta Kappa、奔着杨李足迹去芝大、de Haas-van Alphen 博士论文
8. **贝尔实验室：选择冷门**（1968–1982）：放弃主流半导体方向、专注二维电子物理
9. **1982：分数量子霍尔效应的实验发现（核心页）**：与 Störmer 合作、强磁场低温实验（发现年份跨篇差异注；实验细节详见 Störmer 篇）
10. **1998 年诺贝尔物理学奖**：官方理由（总名单中文：表彰他们发现具有分数电荷激发的新型量子流体）；与 Störmer、Laughlin 共享；Nobel 演讲标题（强磁场下二维电子气中无序与关联的交织）
11. **普林斯顿二十八年**（1982–2010）：两位诺奖得主支持下受聘、电机工程系、2010 荣休
12. **为科学预算发声（2008）**：联名信（与 Phillips 篇互查、同为署名人）
13. **荣誉与院士长廊**：Buckley（1984）/ NAS（1987）/ 诺奖（1998）/ 中科院外籍院士（2000）/ NAE（2004）编年
14. **家与传承**：Linda Varland 与两个女儿（Judith 的学术轨迹）、从范庄到普林斯顿的弧线总结
15. **结尾**：在世、"在强磁场中发现新量子流体的农家子弟"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **"13 岁从河南赴美"禁写（本篇最大陷阱）**：page.md 实载为 **1951 年（12 岁）赴英属香港**、**1958 年（19 岁）赴美国**——"13 岁赴美"系讹传，**禁写**；正确表述"1951 年赴香港、1958 年赴美"。
- **赴台大未就读的原因**：page.md 载"不确定能否返回中国的家人身边"——照此表述，勿演绎成其他政治性解释。
- **发现年份跨篇差异**：Tsui page.md 载 **1982**（两处）；Störmer page.md 载 **October 1981**（MIT Bitter 实验室）——本篇以本人 page.md 的 **1982** 为主表述，加注"一说 1981 年 10 月"；Review 时三篇口径必须一致。
- **诺奖份额禁写**：三人获奖的**具体份额比例 page.md 无载**——禁写任何份额；统一"三人共享"。
- **博士导师**：Royal Stark（page.md 明载 supervisor）；论文题目 *"de Haas-van Alphen effect and electronic band structure of nickel"*（1967）——专有名词照抄。
- **杨振宁、李政道的影响**：page.md 载其"因两位华裔理论物理学家与诺奖得主 C. N. Yang 与 T. D. Lee（均曾就读芝加哥大学）的影响"立志赴芝大——是**求学志向的影响**，勿写成"师承关系"或"同门"。
- **受聘普林斯顿的"两位诺奖得主支持"**：page.md 只载"with the support of two Nobel laureates"，**未写名字**——勿补姓名。
- **1982 双事件表述**：page.md 时间线为"发现（1982）→ 不久后转普林斯顿（1982 年 2 月入职）"——两件事同年，叙述时勿写成"获奖后转普林斯顿"（1982 ≠ 1998 获奖年）。
- **涉乌表态克制**：page.md 载"截至 2022，他是三位公开支持乌克兰的华人诺奖得主之一"——涉当下政治，**建议 Beamer 正文省略**；如必须保留则照原文中性转述、不加渲染（终审时与团队口径统一）。
- **中文名与出生地**：崔琦（Cuī Qí）；出生地"河南省宝丰县范庄"（Fanzhuang, Baofeng County, Henan，时为中华民国）——地名与政权名照 page.md；勿写成"河南农村"之外的演绎。
- **引语红线**：可加引号的仅限 page.md 有原文者——童年自述段（"filled with the years of drought, flood and war…"）、2008 联名信句、获奖理由英文原文；其余一律间接转述。
- **Buckley 奖年份**：Tsui page.md 载 **1984**（与 Störmer 共享）——勿与 Laughlin 的 1986 Buckley 混同。
- **在世人物**：无卒日，death_date 留白；结尾页写"1939–"勿补卒年。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q202138 | 待写入 |
| name_zh | 崔琦 | 待写入 |
| name_en | Daniel C. Tsui | 待写入 |
| birth_date | 1939-02-28 | 待写入 |
| death_date | （空，在世） | 待写入 |
| nationality | United States（生于中国河南宝丰；已入籍） | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | experimental physics / electrical engineering（二维电子系统、FQHE） | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Royal Stark（芝加哥大学）
- **co-honored（同届共享）**：Robert B. Laughlin（斯坦福，理论解释者）、Horst L. Störmer（哥伦比亚，实验搭档）——1998 诺贝尔物理学奖三人共享
- **实验搭档**：Horst L. Störmer（贝尔实验室 FQHE 实验；另共享 1984 Buckley 奖）
- **志向影响（非师承）**：Chen-Ning Yang、Tsung-Dao Lee（受其影响选择芝加哥大学，入库用 colleague/note 注明"志向影响"或不入库，勿建 advisor 关系）
- **家庭成员（可入库）**：妻 Linda Varland；女 Judith Tsui（华盛顿大学医学院副教授）
- **建言同侪**：2008 年联名信共同签署人（含 William D. Phillips——与同批 Phillips 篇互查）

## 8. 奖项清单

- 诺贝尔物理学奖（1998，与 Störmer、Laughlin 共享）
- Oliver E. Buckley Condensed Matter Prize（1984，与 Störmer 共享）
- Fellow of the American Physical Society（1985）
- 美国国家科学院院士（1987）
- Fellow of the American Association for the Advancement of Science（1991）
- Benjamin Franklin Medal（Physics）, Franklin Institute（1998）
- 美国艺术与科学院院士（2000）
- 中国科学院外籍院士（2000）
- 美国国家工程院院士（2004）
- 台湾"中研院"院士（Academia Sinica, Taipei，年份 page.md 未给）
- 荣誉博士：香港大学、北京大学、香港中文大学（metadata 有载）；Great Immigrants Award（metadata 有载）
- Phi Beta Kappa（1961，奥古斯塔纳学院毕业时）

## 9. 机构清单

- 教育：培正中学 Pui Ching Middle School（香港九龙，1951–1957）、Clementi Secondary School（metadata 教育经历）、奥古斯塔纳学院 Augustana College（BS 1961）、芝加哥大学（PhD 1967）
- 任职：芝加哥大学博士后（1 年）→ 贝尔实验室（1968–1982）→ 普林斯顿大学电机工程与计算机科学系（1982-02 起，2010 荣休）
- 兼职：哥伦比亚大学物理系兼职高级研究科学家、波士顿大学研究教授

## 10. 终审清单

- [ ] 生卒 1939-02-28 / 在世留白，出生地河南宝丰范庄（时为中华民国）
- [ ] "1951 赴港、1958 赴美"表述准确；**"13 岁赴美"未出现**
- [ ] 中文名"崔琦"（Cuī Qí）标注准确
- [ ] FQHE 发现"1982（本人 page.md）+ 注 1981-10 跨篇差异"表述准确
- [ ] 诺奖份额比例未出现（三人共享表述）
- [ ] 授奖页用总名单官方理由"发现具有分数电荷激发的新型量子流体"
- [ ] 杨李影响写为"求学志向影响"，非师承
- [ ] "两位诺奖得主支持下受聘普林斯顿"未补姓名
- [ ] 涉乌表态未出现在正文（或中性转述、团队口径统一）
- [ ] 引语均可溯源至 page.md（童年自述、联名信句、获奖理由英文）
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像（装饰圆占位）+ 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/Daniel_C._Tsui/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；优先尝试补真实肖像（Commons 检索失败即保持占位）
- [ ] **国籍**：封面顶部徽章明示美国（身份页注"生于中国河南、已入籍"）
- [ ] **引语核对**：引语必须在 page.md 找到原文（童年自述段）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一（半角引号 " "）
- [ ] 与同世纪物理学家（Heisenberg / Rabi / Wilson）格式对齐；与同批 Störmer / Laughlin 篇口径互查（1998 三人叙事、FQHE 发现年份、Buckley 年份三处一致；与 Chu 篇互查华裔诺奖得主表述、与 Phillips 篇互查联名信共同署名）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
