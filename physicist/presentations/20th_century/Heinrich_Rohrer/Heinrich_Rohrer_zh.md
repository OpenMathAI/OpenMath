# Heinrich Rohrer（海因里希·罗雷尔）立传提示词

> qid=Q123029 · 1933-06-06 – 2013-05-16 · 瑞士物理学家 · 20 世纪 · 1986 诺贝尔物理学奖（与 Gerd Binnig 共享一半）
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Heinrich_Rohrer/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。images.txt 为空（page.md 图注有 "Heinrich Rohrer in 2008" 但无图片 URL）→ 用装饰圆占位（Review 阶段可尝试 Commons 检索 "Heinrich Rohrer 2008"）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（或装饰圆）+ 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「隧穿探针 / 原子表面起伏」母题（与 Binnig 篇同母题、不同主色，呼应二人共享的发明）。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Heinrich Rohrer（海因里希·罗雷尔）
- **生卒**：1933-06-06 生于布克斯（Buchs, St. Gallen，瑞士）→ 2013-05-16 逝于 Wollerau（瑞士），享年 79（家中，自然原因）
- **国籍**：瑞士（Switzerland）
- **身份**：物理学家
- **家庭**：比孪生妹妹晚半小时出生；乡村童年无忧，1949 年全家迁苏黎世；1961 年与 Rose-Marie Egger 结婚——蜜月旅行即包含在罗格斯大学（Rutgers University，新泽西）与 Bernie Serin 合作做 II 类超导体与金属热导研究的一段
- **教育轨迹**：
  - 1951 年入苏黎世联邦理工学院（ETH Zurich），师从 **Wolfgang Pauli** 与 **Paul Scherrer**
  - 博士导师为 P. Grassmann（低温工程方向）；论文课题承接 Jørgen Lykke Olsen 开创的项目——测量超导体在磁场诱发超导转变时的长度变化；因测量对振动极度敏感，很多实验只能在全城入睡后的深夜进行
  - 学业曾因在瑞士山地步兵服役而中断
- **博士导师**：P. Grassmann（**注意：metadata.json 的 doctoral_advisor 字段写 Wolfgang Pauli，与 page.md 冲突——以 page.md 为准，Pauli 是 ETH 本科阶段的老师**）
- **研究领域**：物理（表面科学、扫描隧道显微术）
- **任职**：IBM 苏黎世研究实验室（Rüschlikon，1963 加入，时为 Ambros Speiser 主持）

### 1.5 研究领域表（第 4 步入库用，与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | scanning tunneling microscopy | 扫描隧道显微术 | 1986 诺奖核心成果 |
| 1 | scanning probe microscopy | 扫描探针显微术 | STM 所属学科 |
| 2 | critical phenomena | 临界现象 | 磁相图研究带入的领域 |
| 3 | superconductivity | 超导 | 博士论文：超导体磁场转变长度测量 |

### 1.6 术语清单（第 9 步用）

| 英文 | 中文 | 风险 |
|------|------|------|
| scanning tunneling microscope (STM) | 扫描隧道显微镜 | "设计"而非"发现"原理 |
| scanning probe microscopy (SPM) | 扫描探针显微术 | STM 的上位学科 |
| critical phenomena | 临界现象 | 由磁相图研究引入 |
| cryogenic engineering | 低温工程 | 博士导师 Grassmann 的方向 |
| type-II superconductors | II 类超导体 | 1961 蜜月期 Rutgers 研究课题 |
| thermal conductivity | 热导 | 与 Serin 合作研究内容 |
| nuclear magnetic resonance (NMR) | 核磁共振 | 1974 UCSB 休假年课题 |
| Kondo systems | 近藤体系 | IBM 早期研究（脉冲磁场+磁阻） |
| Heinrich Rohrer Medal | 罗雷尔奖章 | 三年一届；勿与 Nano Seoul 2020 Rohrer Award 混淆 |
| IBM Fellow | IBM 院士 | 1986 年授予 |

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **晚半小时的孪生弟弟**：1933-06-06 生于 Buchs——比孪生妹妹晚半小时来到世界；此后是 Buchs 无忧的乡村童年。
2. **1949 迁居苏黎世 → 1951 入 ETH**：师从 Pauli 与 Scherrer——20 世纪物理最辉煌的讲席下的学生。
3. **深夜的博士论文**：导师 P. Grassmann（低温工程）；测量超导体磁场诱发超导转变时的长度变化，精度要求高到只能等全城入睡后深夜做实验——振动敏感的测量逼出了一位耐心的实验家。
4. **山地步兵与罗格斯蜜月**：瑞士山地步兵服役中断学业；1961 年婚后蜜月即在 Rutgers 做 II 类超导体热导研究——科研与生活无缝焊接的极致样本。
5. **1963 入 IBM Rüschlikon**：在 Ambros Speiser 主持下加入 IBM 苏黎世研究实验室——此后一生的工作主场。
6. **Kondo 体系到临界现象**：IBM 最初几年研究脉冲磁场下带磁阻的 Kondo 体系；继而研究磁相图，最终把他带入临界现象领域。
7. **1974 UCSB 休假年**：在加州大学圣塔芭芭拉分校与 Vince Jaccarino、Alan King 研究核磁共振。
8. **至 1982：扫描隧道显微镜**：与 1978 年加入的 Gerd Binnig（连同 Christoph Gerber、Edmund Weibel）合作开发 STM——在原子尺度对表面成像的仪器；page.md 表述为"直到 1982 年他致力于扫描隧道显微镜"。
9. **1986 诺贝尔物理学奖**：与 Gerd Binnig 共享一半（两人各四分之一），另一半授予 Ernst Ruska；获奖理由"表彰他们设计扫描隧道显微镜"。诺奖演讲（1986-12-08）：*Scanning Tunneling Microscopy – From Birth to Adolescence*（与 Binnig 同题联讲）。
10. **IBM Fellow 与物理部主管**（1986–1988）：1986 年任 IBM Fellow；1986–1988 领导实验室物理部。
11. **资深与年轻的搭档**：Rohrer（1933 生）与 Binnig（1947 生）相差 14 岁——非师生、是 IBM 同组层级中的资深/年轻搭档（Rohrer 1963 入 IBM，Binnig 1978 加入后与其合作）。
12. **晚年荣誉与纪念**：1990 年瑞士物理学会荣誉会员；2008 年当选"中研院"（Academia Sinica）荣誉院士；日本表面科学学会联合 IBM 苏黎世、瑞士驻日使馆与 Rohrer 夫人设立三年一届的 **Heinrich Rohrer Medal** 以志纪念（勿与 Nano Seoul 2020 会议的 Heinrich Rohrer Award 混淆）。
13. **谢幕 Wollerau**：2013-05-16 在 Wollerau 家中自然离世，享年 79。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（山峦莓紫） | `#6B2D5C` | 瑞士山地的沉稳 / 资深实验家的克制 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（STM — 靛蓝） | `#4C5FD5` | 扫描隧道显微镜 / 原子成像 |
| 分类色 2（表面与临界 — 青绿） | `#0E7C7B` | Kondo 体系 / 临界现象 / 表面科学 |
| 分类色 3（低温与深夜测量 — 琥珀） | `#E07B30` | 低温工程博士 / 深夜实验 |
| 分类色 4（荣誉与纪念 — 玫瑰） | `#C4204F` | 诺奖 / Rohrer Medal / 传承 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「隧穿探针 / 原子表面起伏」的视觉语言——与 Binnig 篇同母题，主色区分二人。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：抽象 / 梦幻 / 深沉（在看不见的微观世界摸索、以耐心驯服振动）
- **选定曲目**：Notan Nigres **Mirage**（电子 / 梦幻 / 抽象），匹配"深夜测量、隧穿电流、原子世界的抽象图景"气质。
- **落地文件**：`physicist/presentations/20th_century/Heinrich_Rohrer/Mirage.wav`（复制自音乐库，不入 git）。
- **匹配理由**：Rohrer 的科学气质是"在不可见处做最安静的测量"——Mirage 的抽象梦幻感匹配隧穿与原子表面的微观世界，也匹配这位深夜实验家内敛的一生；与本组其他五人曲目不重复。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「表面科学 · 瑞士」+ Rohrer 1933–2013 + 右上头像/装饰圆 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：扫描隧道显微镜 / 表面与临界现象 / 深夜测量者的耐心 / 1986 诺奖
4. **早年：Buchs 的乡村童年**（1933–1949）：孪生出生、1949 迁苏黎世
5. **ETH：Pauli 与 Scherrer 门下**（1951–）：大师讲席下的学生
6. **深夜的博士论文**：Grassmann、超导转变长度测量、振动敏感与深夜实验
7. **山地步兵与罗格斯蜜月**（1961–1963）：服役、Rose-Marie、蜜月科研
8. **IBM Rüschlikon**（1963–）：Speiser 时代、Kondo 体系、磁相图、临界现象
9. **UCSB 休假年**（1974）：核磁共振
10. **STM 协作**（1978–1982）：与 Binnig、Gerber、Weibel 四人组的攻坚
11. **1986 诺贝尔物理学奖**：与 Binnig 共享一半、与 Ruska 同台、联袂诺奖演讲
12. **IBM Fellow 与物理部**（1986–1988）
13. **荣誉与纪念**：瑞士物理学会荣誉会员（1990）、"中研院"荣誉院士（2008）、Heinrich Rohrer Medal
14. **与 Binnig 的对照**：资深/年轻、同母题不同色彩的双人组结构
15. **结尾**：2013 逝于 Wollerau、"让世界看见原子的瑞士耐心"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **博士导师冲突（P0）**：metadata.json 的 doctoral_advisor = Wolfgang Pauli，但 page.md 明载博士由 **P. Grassmann** 指导（低温工程）——**以 page.md 为准**；Pauli 与 Scherrer 是 ETH 就读期间的**老师**（"student of"），勿写成博士导师。这是本篇最重要的数据噪声注记。
- **诺奖切分**：Rohrer 与 Binnig **共享一半**（各四分之一），另一半是 Ruska——勿写"三人平分"；Rohrer 篇获奖理由与 Binnig 篇相同（"表彰他们设计扫描隧道显微镜"）。
- **获奖理由用词**："设计"扫描隧道显微镜——勿写"发现隧穿效应"；page.md（Binnig 篇）明载 STM 物理原理此前已知、IBM 团队率先解决实验实现难题。
- **四人组表述**：STM 开发四人组为 Binnig、Rohrer、Gerber、Weibel（Binnig 篇原文），获奖者是 Binnig 与 Rohrer——Gerber/Weibel 在叙事中致意即可，勿入获奖表述。
- **1982 时点**：page.md 表述为 "Until 1982 he worked on the scanning tunneling microscope"——写"至 1982 年致力于 STM"即可，勿自行补"1981 年发明"等具体日期。
- **与 Binnig 关系定位**：是 IBM 同组的**资深/年轻搭档**（Rohrer 1963 入 IBM、Binnig 1978 加入），page.md 未载师生或雇佣层级细节——写"搭档/合作"层级，勿写"导师-学生"。
- **孪生表述**：晚孪生妹妹半小时出生——"half an hour after his twin sister"，勿写成"双胞胎哥哥/龙凤胎"等无据展开。
- **奖章区分**：Heinrich Rohrer Medal（日本表面科学学会等设立，三年一届）≠ Nano Seoul 2020 的 Heinrich Rohrer Award——page.md 特别提示勿混淆；立传如写纪念奖，只写 Medal 并注明设立方（含 Rohrer 夫人）。
- **去世表述**：自然原因（natural causes）、家中、Wollerau、享年 79——中性表述，勿渲染病情。
- **机构注记**：infobox 的 Institutions 列写的是 Tohoku University（东北大学）——这是 infobox 字段噪声/晚近兼职信息，正文生涯主线是 **IBM 苏黎世**；如需提 Tohoku 须有 page.md 正文佐证，否则不写。
- **引语红线**：Rohrer 本人在 page.md 中无直接引语；全部间接转述。
- **肖像**：images.txt 为空，**无本人肖像**——装饰圆占位（Review 可尝试 Commons "Heinrich Rohrer 2008"）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q123029 | 待写入 |
| name_zh | 海因里希·罗雷尔 | 待写入 |
| name_en | Heinrich Rohrer | 待写入 |
| birth_date | 1933-06-06 | 待写入 |
| death_date | 2013-05-16 | 待写入 |
| nationality | Switzerland | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | physics（表面科学 / 扫描探针显微术） | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **ETH 老师**：Wolfgang Pauli、Paul Scherrer（本科/研究生授课老师，advisor-student 弱向或 teacher 关系，note 注明"非博士导师"）
- **博士导师**：P. Grassmann（低温工程；metadata 的 Pauli 字段为噪声，勿入 relation）
- **共同得主**：Gerd Binnig（1986 共享一半，co-honored）；Ernst Ruska（同届另一半，co-honored）
- **STM 合作团队**：Christoph Gerber、Edmund Weibel——**注意：此二人仅 Binnig 篇 page.md 有载，Rohrer 篇 page.md 未提及，Rohrer yaml 不入库（避免无载写入）**
- **配偶**：Rose-Marie Egger（1961 结婚）
- **科研合作者**：Bernie Serin（Rutgers，II 类超导体热导，1961 蜜月期）、Vince Jaccarino 与 Alan King（UCSB，NMR，1974）
- **机构前辈**：Ambros Speiser（1963 年加入时 IBM 苏黎世实验室主持人，note 级）
- **任职机构同事侧**：IBM 苏黎世研究实验室（1963–，Rüschlikon；1986–1988 物理部主管）、ETH Zurich
- **诺贝尔奖同届**：1986 年物理学奖三人共享（Ruska + Binnig + Rohrer，但切分不同）

## 8. 奖项清单

- 诺贝尔物理学奖（1986，与 Gerd Binnig 共享一半）
- EPS Europhysics Prize（1984）
- King Faisal Prize（King Faisal International Prize in Science，1984）
- The Elliott Cresson Medal（1987）
- IBM Fellow（1986）
- Fritz London Memorial Lecture（1992）
- 瑞士物理学会荣誉会员（1990）
- "中研院"（Academia Sinica）荣誉院士（2008）
- National Inventors Hall of Fame（入选，metadata 有载）
- 艾克斯-马赛第二大学荣誉博士（metadata 有载）
- Heinrich Rohrer Medal（身后纪念，日本表面科学学会 × IBM 苏黎世 × 瑞士驻日使馆 × Rohrer 夫人，三年一届）

## 9. 机构清单

- 教育：ETH Zurich（1951 入学；师从 Pauli / Scherrer；博士导师 P. Grassmann，低温工程）
- 任职：IBM 苏黎世研究实验室（Rüschlikon，1963–；1986–1988 物理部主管；1986 IBM Fellow）
- 学术访问：Rutgers University（1961，Serin 组）、UCSB（1974 休假年，NMR）
- 纪念机构：IBM Research – Zurich 联合设立的 Heinrich Rohrer Medal

## 10. 终审清单

- [ ] 生卒 1933-06-06 / 2013-05-16，享年 79，出生地 Buchs，去世地 Wollerau
- [ ] 博士导师 = P. Grassmann（metadata Pauli 噪声已弃用，Pauli/Scherrer 为 ETH 老师）
- [ ] 诺奖切分 = Rohrer/Binnig 共享一半 + Ruska 一半
- [ ] 获奖理由"设计扫描隧道显微镜"，无"发现隧穿效应"表述
- [ ] "至 1982 年致力于 STM"表述，无自造发明日期
- [ ] 与 Binnig = 资深/年轻搭档，无师生表述
- [ ] Rohrer Medal 与 Rohrer Award 不混淆
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像/装饰圆 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/Heinrich_Rohrer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；如 Review 阶段从 Commons 取得真人照则替换并记录来源
- [ ] **国籍**：封面顶部徽章明示瑞士
- [ ] **引语核对**：无 Rohrer 直接引语，全部间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪物理学家（Ruska / Binnig）格式对齐

---

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
