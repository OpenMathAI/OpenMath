# 物理学家立传提示词（21 世纪批次：Alexei A. Abrikosov）

> **本文件是 OpenPhysicist「物理学家立传提示词」**，对象：Alexei A. Abrikosov（2003 诺贝尔物理学奖，II 类超导体与阿布里科索夫涡旋晶格）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 凡标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。

---

## 一、模板定位 【人物专属】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Alexei Alexeyevich Abrikosov（阿列克谢·阿列克谢耶维奇·阿布里科索夫），2003 诺贝尔物理学奖得主（三人共享之一）。
- **设计哲学**：保留物理学家模板「身份信息页 + 结构化研究领域」骨架；Abrikosov 是「朗道学派嫡传 + 冷战迁徙」双线人物，叙事上突出「1952/1957 两篇论文预言之作 → 半个世纪后获奖」的时间纵深。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Alexei Alexeyevich Abrikosov（1928-06-25 ~ 2017-03-29，享年 88 岁）
- **获奖理由（page.md 口径 + 中译，禁止改写）**：
  > "for theories about how matter can behave at extremely low temperatures"（因其关于物质在极低温下行为方式的理论）
  - ★ 注意：page.md 只载**转述句**；官方 citation（"for pioneering contributions to the theory of superconductors and superfluids"）以诺贝尔名录为准，立传执行时以名录为准、勿把转述当官方原话。
- **共享格局**：2003 奖由 Abrikosov 与 Vitaly Ginzburg（超导理论）、Anthony J. Leggett（超流理论）三人共享。
- **气质关键词**：**II 类超导体的预言者、朗道学派嫡传、从莫斯科到阿贡的迁徙者**
- **设计母题**：**涡旋晶格（vortex lattice）**。磁通线以规则阵列穿透 II 类超导体——以六角/正方点阵中的螺旋线束为核心视觉概念，呼应「有序中的穿透」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Alexei_A._Abrikosov/page.md`
- **第 0 步状态**：page.md 已有本地；**html 与 images/ 待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Alexei_A._Abrikosov`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`、`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 数据库同步含「研究领域 + 入库」（第 4 步）与「社会关系 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ☐ 待下载 `https://en.wikipedia.org/wiki/Alexei_A._Abrikosov` 到 `{Dir}.html` 与 `images/` 肖像（2003 年照，404 则 REST API 回退）
- 事实基准（以本地 page.md 为准，第一轮已核对）：
  - 生卒：1928-06-25 生于莫斯科（俄罗斯苏维埃联邦/苏联）~ 2017-03-29 逝于美国加州帕洛阿尔托，享年 88 岁
  - 国籍/公民权：苏联（1928–1991）→ 俄罗斯（1992–）→ 美国（1999–）
  - 家庭：父母皆为医生——父 Alexei Ivanovich Abrikosov（1875–1955）、母 Fania Davidovna Woolf（1895–1965，犹太人）；姑母 Anna Abrikosova（殉道天主教修女）；妹 Maria Alekseevna Abrikósova（1929–1998，医生）；妻 Svetlana Yuriyevna Bunkova（1977 结婚），育 3 子
  - 教育：1943 中学毕业后先学能源技术；1948 莫斯科大学毕业；物理学问题研究所（苏联科学院）1951 博士（等离子体热扩散理论）、1955 物理数学科学博士（高能量子电动力学）
  - 博士导师：Lev Landau（frontmatter doctoral_advisor + infobox 明载）
  - 任职轨迹：物理学问题研究所 1948–1965 → Landau 理论物理研究所 1965–1988 → 莫斯科大学教授（1965 起）→ 莫斯科物理技术学院 1972–1976 → 莫斯科钢与合金学院 1976–1991 → 苏联科学院院士 1964（对应）/1987（全权）→ 俄罗斯科学院全权院士 1991 → 1991 移居美国，Argonne 国家实验室任职至退休（凝聚态理论组 Argonne Distinguished Scientist）
  - 关键荣誉：苏联科学院对应院士 1964；列宁奖 1966；Fritz London 纪念奖 1972；洛桑大学名誉博士 1975；劳动荣誉勋章 1975；苏联国家奖 1982；劳动红旗勋章 1988；Landau 金质奖章 1989；John Bardeen 奖 1991；美国艺术与科学院外籍荣誉院士 1991；NAS 院士 2000；英国皇家学会外籍院士 ForMemRS 2001；Nobel 2003；Golden Plate 2004；乌克兰 NAS Vernadsky 金质奖章 2015；奥尔良/洛桑/波尔多一大名誉博士
  - 知名学生：page.md **无载**，禁写
  - 核心贡献清单（4–6 条）：①1952/1957 两篇论文阐明磁通如何穿透一类超导体（II 类超导体）；②Abrikosov 涡旋晶格；③与 Gor'kov、Dzyaloshinskii 合著《Methods of Quantum Field Theory in Statistical Physics》（统计物理中的量子场论方法经典教科书）；④Fermi liquid theory、quantum triviality（infobox known for）；⑤获奖时研究磁阻起源
  - 关键时间线（15–20 节点）：1928 生于莫斯科 → 1943 中学毕业/学能源技术 → 1948 莫斯科大学毕业 → 1948–1965 物理学问题研究所 → 1951 博士（等离子体热扩散）→ 1952 II 类超导体首篇 → 1955 物理数学科学博士（高能 QED）→ 1957 涡旋晶格论文 → 1964 苏联科学院对应院士 → 1965–1988 Landau 研究所 + 1965 起 MSU 教授 → 1966 列宁奖 → 1972 Fritz London 奖 → 1972–1976 MIPT → 1975 洛桑名誉博士/劳动荣誉勋章 → 1976–1991 钢与合金学院 → 1982 苏联国家奖 → 1987 科学院全权院士 → 1988 劳动红旗勋章 → 1989 Landau 金章 → 1991 移美 + Argonne + Bardeen 奖 + AAAS 外籍 + 俄科院院士 → 1999 美国公民 → 2000 NAS → 2001 ForMemRS → 2003 诺贝尔物理学奖 → 2004 Golden Plate → 2015 Vernadsky 金章 → 2017-03-29 逝于帕洛阿尔托

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Alexei_A._Abrikosov/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 20 世纪成品目录 Makefile，设 `MAIN=Alexei_A._Abrikosov_zh`、`VIDEO_NAME=Alexei_A._Abrikosov_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：infobox 2003 年照（Commons `Abrikosov_in_2003.jpg` 一类，以 REST API 查实际文件名）；404 则装饰圆占位

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | 主领域，2003 诺奖核心 | 核心页 |
| 1 | superconductivity | 超导电性 | II 类超导体与涡旋晶格 | 核心页 |
| 2 | theoretical physics | 理论物理 | frontmatter field_of_work | 概览页 |
| 3 | quantum field theory | 量子场论 | 统计物理中的 QFT 方法教科书 | 教科书页 |
| 4 | fermi liquid theory | 费米液体理论 | infobox known for | 方法页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> **只收 page.md 明载**；对手方 name_en 已查库，沿用库内/将建规范形式。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Lev Landau | 师→生（博士导师） | 物理学问题研究所博士导师，1962 诺奖得主，朗道学派核心 |
| co-honored | Vitaly Ginzburg | 无向 | 2003 诺贝尔物理学奖共享（超导理论） |
| co-honored | Anthony J. Leggett | 无向 | 2003 诺贝尔物理学奖共享（超流理论） |
| colleague | Lev Gor'kov | 无向 | 合著《Methods of Quantum Field Theory in Statistical Physics》 |
| colleague | Igor Dzyaloshinskii | 无向 | 合著《Methods of Quantum Field Theory in Statistical Physics》 |
| spouse | Svetlana Yuriyevna Bunkova | 无向 | 1977 结婚，育 3 子 |

- 入库注意：本人复用库内 stub `Alexei Abrikosov`(id=2424, yaml name_en 沿用此形式回填 QID=Q188128)；Ginzburg 复用 stub id=2431（name_en=`Vitaly Ginzburg`）；Gor'kov=`Lev Gor'kov`(2427)、Dzyaloshinskii=`Igor Dzyaloshinskii`(2426)、Landau=`Lev Landau`(2130) 均为库内既有记录；Leggett 由本批新建（name_en=`Anthony J. Leggett`）；Ginzburg/Leggett 由本批各自 yaml 并行入库，撞 uq_rel 跳过即可。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深冷、磁通有序、铁幕两端的迁徙
- **配色**：低温钢蓝（主色，批内唯一）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `mainclr` 主色 — 低温钢蓝 `#0F3B5C`
  - `badgeVortex` 涡旋晶格 — 湖蓝 `#2E86C1`
  - `badgeSC` 超导 — 深绿 `#117864`
  - `badgeQFT` 统计物理 QFT — 紫罗兰 `#7D3C98`
  - `badgeLife` 苏联岁月与迁徙 — 砖红 `#A93226`
- **背景母题**：柔和气泡——六角点阵排布的小圆内嵌螺旋线束，呼应涡旋晶格

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍，底部状态栏给 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — II 类超导体预言者 / Alexei A. Abrikosov 1928–2017 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — II 类超导体 / 涡旋晶格 / 统计物理 QFT / 磁阻
04  莫斯科早年 (1928–1948) — 医生家庭、1943 能源技术、1948 MSU 毕业
05  物理学问题研究所与朗道门下 (1948–1965) — 1951 等离子体热扩散博士、1955 高能 QED 博士
06  1952/1957：II 类超导体的预言（核心贡献页）— 磁通穿透、涡旋晶格（公式框放 II 类超导体磁通穿透概念图式，page.md 无具体公式，注明）
07  Landau 研究所岁月 (1965–1988) — 兼教 MSU/MIPT/钢与合金学院、苏联科学院院士
08  统计物理中的量子场论 — 与 Gor'kov/Dzyaloshinskii 合著经典教科书
09  1991：跨过铁幕 — 移居美国、Argonne 凝聚态理论组
10  2003 诺贝尔物理学奖 — 三人共享格局页（Abrikosov+Ginzburg 超导 / Leggett 超流）
11  荣誉与认可 — 列宁奖 1966 · London 奖 1972 · Landau 金章 1989 · NAS 2000 · ForMemRS 2001
12  遗产：涡旋晶格到实用超导体
13  结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式；每写完一页 `make` 并 `pdftoppm` 截图检查。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Abrikosov 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | page.md 只载转述句 "for theories about how matter can behave at extremely low temperatures"；官方 citation 以诺贝尔名录为准（超导与超流理论），勿把转述当官方原话 |
| 三人格局 | Abrikosov+Ginzburg=超导、Leggett=超流；三人是 co-honored，无合作禁写 |
| 与 Landau 关系 | 博士导师（frontmatter + infobox 明载），物理学问题研究所 1951 博士；勿把「Landau 研究所工作」与「Landau 指导」混为一谈 |
| 两个博士头衔 | 1951 Ph.D.（等离子体热扩散）与 1955 Doctor of Physical and Mathematical Sciences（高能 QED，higher doctorate）是两回事，勿合并 |
| 1952 vs 1957 | 「两篇论文（1952 与 1957）阐明磁通穿透」——1952 是首篇、1957 是涡旋晶格系统化，勿写成单一年份 |
| 国籍三段 | 苏联（1928–1991）/俄罗斯（1992–）/美国（1999–），勿简化为「俄裔美国」；1991 移美与 1999 入籍是两件事 |
| 家庭 | 父母皆医生；父 Alexei Ivanovich Abrikosov（1875–1955）与本人同名不同人（Alexei Alexeyevich），勿混；姑母 Anna Abrikosova 是殉道修女，涉及宗教叙事从简 |
| 教科书 | 合著者 Lev Gor'kov 与 Igor Dzyaloshinskii，书名《Methods of Quantum Field Theory in Statistical Physics》（1975 Dover 版），勿写成独著 |
| 学生 | page.md 无载，禁写（勿从 Landau 学派反推） |
| Argonne 头衔 | Argonne Distinguished Scientist，凝聚态理论组（材料科学部）；获奖时研究磁阻起源，勿写成「获奖时研究超导」 |
| 奖项年份 | Lenin 1966 / London 1972 / USSR State 1982 / Landau Gold Medal 1989 / Bardeen 1991 / NAS 2000 / ForMemRS 2001 / Nobel 2003 / Golden Plate 2004 / Vernadsky 2015，勿错位 |
| 库内记录 | 本人 name_en 用库内 stub 形式 `Alexei Abrikosov`（非 `Alexei A. Abrikosov`），防分裂 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| type-II superconductor | II 类超导体 | 磁通可穿透的一类 |
| Abrikosov vortex lattice | 阿布里科索夫涡旋晶格 | 磁通线规则排列 |
| magnetic flux | 磁通 | 穿透行为的载体 |
| Fermi liquid theory | 费米液体理论 | 朗道框架的延续 |
| quantum triviality | 量子平庸性 | infobox known for |
| thermal diffusion in plasmas | 等离子体热扩散 | 1951 博士论文主题 |
| Doctor of Physical and Mathematical Sciences | 物理数学科学博士 | 苏联 higher doctorate |
| Institute for Physical Problems | 物理学问题研究所 | 卡皮察创办、朗道所在 |
| Landau Institute for Theoretical Physics | 朗道理论物理研究所 | 1965–1988 |
| Argonne National Laboratory | 阿贡国家实验室 | 1991 起 |
| magnetoresistance | 磁阻 | 获奖时研究方向 |
| Methods of Quantum Field Theory in Statistical Physics | 《统计物理中的量子场论方法》 | 三人合著教科书 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（86k views，历史感 / 深沉）
- **匹配理由**: 「历史感/深沉」匹配其跨越苏联 60 年与美国 26 年的双段人生——1952/1957 的预言等了半个世纪才获奖，铁幕两端的学术迁徙自带冷战年代的历史纵深。
- **备选**（未采用）: Falling Apart（渐进/情感，时长 5:32 偏长）；Through the Darkness（留给本批 Ginzburg）。
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`
- 批内 BGM 不重复备案：Giacconi=The Invisible Light、Abrikosov=PAST、Ginzburg=Through the Darkness、Leggett=SEA、Gross=Savage。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Alexei_A._Abrikosov/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 关系入库引擎（幂等） |
| `MySQL/data/Alexei_A._Abrikosov.yaml` | yaml 数据文件 |

> **开始执行。每完成一步汇报。**
