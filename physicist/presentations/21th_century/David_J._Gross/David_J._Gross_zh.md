# 物理学家立传提示词（21 世纪批次：David J. Gross）

> **本文件是 OpenPhysicist「物理学家立传提示词」**，对象：David J. Gross（2004 诺贝尔物理学奖，渐近自由与 QCD）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 凡标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。

---

## 一、模板定位 【人物专属】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：David Jonathan Gross（戴维·乔纳森·格罗斯），2004 诺贝尔物理学奖得主（三人共享之一）。
- **设计哲学**：保留物理学家模板「身份信息页 + 结构化研究领域」骨架；Gross 是「QCD 奠基人 + 弦论推手 + KITP 掌门人」三线人物，叙事主线取「1973 与首位博士生 Wilczek 发现渐近自由 → QCD 补全标准模型 → 异规范弦」，辅线取其公共行动（科学预算、气候、核风险请愿）。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：David Jonathan Gross（1941-02-19 生，在世）
- **获奖理由（官方英文原文 + 中译，page.md 明载，禁止改写）**：
  > "for the discovery of asymptotic freedom in the theory of the strong interaction"（因发现强相互作用理论中的渐近自由）
- **共享格局**：2004 奖由 Gross 与 Frank Wilczek、H. David Politzer 三人共享（渐近自由的发现）。
- **气质关键词**：**渐近自由的发现者、QCD 的定名者、普林斯顿弦乐四重奏的第一小提琴**
- **设计母题**：**渐近自由（asymptotic freedom）**。夸克越靠近、色作用越弱，越远则越强——以「两枚靠近后几乎无连线、拉开后连线绷紧发亮的粒子对」为核心视觉概念。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/David_J._Gross/page.md`
- **第 0 步状态**：page.md 已有本地；**html 与 images/ 待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/David_J._Gross`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`、`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 数据库同步含「研究领域 + 入库」（第 4 步）与「社会关系 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ☐ 待下载 `https://en.wikipedia.org/wiki/David_J._Gross` 到 `{Dir}.html` 与 `images/` 肖像（2007 年照，Commons 查 infobox 原图名；404 则 REST API 回退）
- 事实基准（以本地 page.md 为准，第一轮已核对）：
  - 生卒：1941-02-19 生于华盛顿特区（犹太家庭，祖辈来自奥匈帝国/匈牙利）；在世（page.md 无卒日）
  - 家庭：父母 Nora (Faine) 与 Bertram Myron Gross（1912–1997）；三兄弟——Larry Gross（传播学教授）、Samuel R. Gross（法学教授）、Theodore (Teddy) Gross（剧作家）；第一任妻 Shulamith (Toaff) Gross（离婚，育 2 子）；第二任妻 Jacquelyn Savani（育 1 继女）
  - 教育：耶路撒冷希伯来大学附属中学 → 1962 希伯来大学学士 → 1966 加州大学伯克利分校物理博士（导师 Geoffrey Chew，论文《Investigation of the many-body, multichannel partial-wave scattering amplitude》；1963–66 NSF 研究生奖学金）
  - 任职轨迹：1966–69 Harvard junior fellow → 1970–74 Sloan Fellowship → 普林斯顿大学 Eugene Higgins 物理教授（至 1997，此后任 Thomas Jones 数学物理荣誉教授）→ KITP（UCSB 卡弗里理论物理研究所）所长、Frederick W. Gluck 理论物理讲席 → 现任 UCSB Chancellor's Chair 理论物理教授 + Chapman 大学量子研究所 affiliated；中科院外籍院士
  - 核心贡献清单（4–6 条）：①1973 与首位博士生 Frank Wilczek 在普林斯顿发现渐近自由（非阿贝尔规范理论的首要特征）；②据此与 Wilczek 构建量子色动力学 QCD（强核力理论），补全标准模型；③与 Harvey/Martinec/Rohm（绰号「普林斯顿弦乐四重奏」）共创异规范弦（heterotic string）理论；④Gross–Neveu 模型（infobox known for）；⑤渐近自由的反面——夸克禁闭解释（原子核永不可拆出自由夸克）
  - 关键荣誉：APS Fellow 1974；美国艺术与科学院 1985；NAS 1986；J. J. Sakurai 奖 1986；AAAS Fellow 1987；MacArthur Fellowship 1987；ICTP Dirac Medal 1988；Oskar Klein 奖章 2000；Harvey 奖 2000；EPS 高能与粒子物理奖 2003；法国科学院 Grande Médaille d'Or 2004；Nobel 2004；Golden Plate 2005；Tata 研究所荣誉 Fellow 2005；美国哲学学会 2007；印度科学院/发展中世界科学院 2007；中科院外籍院士 2011；Prange 奖 2013；JINR Dubna 荣誉奖章 2016；俄罗斯科学院外籍院士 2016；APS 主席团任期 2016–2020；基础科学终身成就奖 2025；基础物理学特别突破奖 2026
  - 公共行动：2003 人道主义宣言 22 位诺奖得主签名者之一；2008 联名致函总统 Bush 要求追加 DOE/NSF/NIST 科学预算；2015 林道会议签署气候变化《美因瑙宣言 2015》（76 位诺奖得主，递交 Hollande/COP21）；2026 第 75 届林道会议发布核战争风险警告（基于 2024 美因瑙核武器宣言，104 位签名）；2026-07 梵蒂冈诺贝尔大会共同组织者（罗马宣言）
  - 知名学生（infobox 明载）：Natan Andrei、Frank Wilczek、Edward Witten、William E. Caswell、Eric D'Hoker、Rajesh Gopakumar、Nikita Nekrasov、Stephen Bernard Libby
  - 关键时间线（15–20 节点）：1941-02-19 生于华盛顿 → 耶路撒冷希伯来大学附中 → 1962 希伯来大学学士 → 1963–66 NSF 研究生奖学金 → 1966 伯克利博士（Chew 门下）→ 1966–69 Harvard junior fellow → 1970–74 Sloan Fellowship → 1973 与 Wilczek 发现渐近自由 + 构建 QCD → 1974 APS Fellow → 1985 美国艺术与科学院 → 1986 Sakurai 奖 + NAS → 1987 MacArthur Fellowship → 1988 Dirac Medal → 异规范弦（与「弦乐四重奏」三人，年份 page.md 无载禁写）→ 1997 Princeton 荣退 → KITP 所长/Gluck 讲席 → 2000 Klein + Harvey 奖 → 2003 EPS 奖 + 人道主义宣言 → 2004 法国金质大奖 + 诺贝尔奖 → 2005 Golden Plate → 2007 三院院士 → 2011 中科院外籍院士 → 2013 Prange 奖 → 2015 美因瑙气候宣言 → 2016 Dubna 奖章 + 俄科院外籍 + APS 主席团 → 2025 基础科学终身成就奖 → 2026 特别突破奖 + 林道核风险警告 + 罗马宣言共同组织

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `David_J._Gross/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 20 世纪成品目录 Makefile，设 `MAIN=David_J._Gross_zh`、`VIDEO_NAME=David_J._Gross_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：infobox 2007 年照；404 则装饰圆占位

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum chromodynamics | 量子色动力学 | 1973 与 Wilczek 共建，诺奖落点 | 核心页 |
| 1 | string theory | 弦理论 | 异规范弦，「弦乐四重奏」 | 弦论页 |
| 2 | particle physics | 粒子物理 | 标准模型补全者 | 概览页 |
| 3 | quantum field theory | 量子场论 | 非阿贝尔规范理论紫外行为 | 理论页 |
| 4 | strong interaction | 强相互作用 | 渐近自由与夸克禁闭 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> **只收 page.md 明载**；对手方 name_en 已查库，沿用库内/将建规范形式。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Geoffrey Chew | 师→生（博士导师） | 1966 伯克利博士导师 |
| advisor-student | Frank Wilczek | Gross → 学生 | 首位博士生，1973 共同发现渐近自由并共建 QCD |
| co-honored | Frank Wilczek | 无向 | 2004 诺贝尔物理学奖共享（渐近自由） |
| co-honored | H. David Politzer | 无向 | 2004 诺贝尔物理学奖共享（渐近自由） |
| colleague | Jeffrey A. Harvey | 无向 | 「普林斯顿弦乐四重奏」，共创异规范弦 |
| colleague | Emil Martinec | 无向 | 「普林斯顿弦乐四重奏」，共创异规范弦 |
| colleague | Ryan Rohm | 无向 | 「普林斯顿弦乐四重奏」，共创异规范弦 |
| advisor-student | Edward Witten | Gross → 学生 | 博士生，后成弦论领军人物 |
| advisor-student | Natan Andrei | Gross → 学生 | infobox 明载博士生 |
| advisor-student | William E. Caswell | Gross → 学生 | infobox 明载博士生 |
| advisor-student | Eric D'Hoker | Gross → 学生 | infobox 明载博士生 |
| advisor-student | Rajesh Gopakumar | Gross → 学生 | infobox 明载博士生 |
| advisor-student | Nikita Nekrasov | Gross → 学生 | infobox 明载博士生 |
| advisor-student | Stephen Bernard Libby | Gross → 学生 | infobox 明载博士生 |
| spouse | Shulamith Toaff Gross | 无向 | 第一任妻，离婚，育 2 子 |
| spouse | Jacquelyn Savani | 无向 | 第二任妻，育 1 继女 |

- 入库注意：本人复用库内 stub `David Gross`(id=1023, yaml name_en 沿用此形式回填 QID=Q40262)；Wilczek 用库内 `Frank Wilczek`(2982)、Politzer 用库内 `H. David Politzer`(2981)（二人均由 batch 3 已完整入库）、Witten 用库内 `Edward Witten`(130)；Chew/其余学生/弦乐四重奏三人/两任配偶新建 stub；Wilczek/Politzer 关系与 batch 3 篇目互为镜像，撞 uq_rel 跳过即可。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：强作用的张力、粒子的锋锐、弦的延展
- **配色**：深紫罗兰（主色，批内唯一）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `mainclr` 主色 — 深紫罗兰 `#4A235A`
  - `badgeQCD` 量子色动力学 — 强作用红 `#C0392B`
  - `badgeAF` 渐近自由 — 琥珀 `#D68910`
  - `badgeString` 弦论 — 深青绿 `#0B5345`
  - `badgeKITP` 机构与公共行动 — 石板灰 `#5D6D7E`
- **背景母题**：柔和气泡——中央两枚圆点接近时几乎无线相连、以细弱虚线示意，四角绷紧的亮线示意拉远后增强的色力

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍，底部状态栏给 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 渐近自由的发现者 / David J. Gross 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 渐近自由 / QCD / 异规范弦 / 夸克禁闭
04  早年：华盛顿与耶路撒冷 (1941–1962) — 奥匈犹太移民家庭、希伯来大学附中与学士
05  伯克利与 Chew 门下 (1962–1966) — 多体多道分波散射振幅论文、Harvard junior fellow
06  1973：渐近自由的发现（核心贡献页）— 与首位博士生 Wilczek、非阿贝尔规范理论紫外行为（公式框放跑动耦合常数 αs 随距离减小的示意式/概念图式并注明）
07  QCD 与夸克禁闭 — 强核力理论补全标准模型；反面：拉得越远力越强、核子永不可拆出自由夸克
08  普林斯顿弦乐四重奏 — Gross/Harvey/Martinec/Rohm 与异规范弦
09  门生与传承 — Wilczek、Witten、Andrei 等八位博士生（infobox 口径）
10  KITP 掌门与公共行动 — UCSB 卡弗里研究所所长、2008 科学预算请愿、2015 美因瑙气候宣言、2026 核风险警告与罗马宣言
11  2004 诺贝尔物理学奖 — 三人共享格局页（Gross+Wilczek / Politzer 独立计算，同一发现）
12  荣誉与认可 — Sakurai 1986 · MacArthur 1987 · Dirac 1988 · 中科院外籍 2011 · 特别突破奖 2026
13  遗产：从渐近自由到万物之理
14  结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式；每写完一页 `make` 并 `pdftoppm` 截图检查；公共行动页与荣誉页条目多，用分栏+小字号防溢出。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Gross 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方原句 "for the discovery of asymptotic freedom in the theory of the strong interaction"——落点在**强相互作用中的渐近自由**，勿写成「因发现 QCD 获奖」 |
| 三人格局 | Gross 与 Wilczek 是**师生合作**发现，Politzer 是**独立计算**同获；三人 co-honored，但 Gross–Wilczek 另有 advisor-student 关系，勿把 Politzer 写成合作者 |
| Wilczek 身份 | 1973 年时是 Gross 的**首位博士生**——既是学生（advisor-student）又是 2004 共同得主（co-honored），两种关系并存入库，勿混为一行 |
| 渐近自由方向 | 距离越短/能量越高→作用越弱（近乎自由）；拉得越远→力越强→夸克禁闭。两个方向勿写反 |
| Harvard 学历 | 1966–69 是 **junior fellow**（青年研究员），frontmatter educated_at 含 Harvard 易误导——Harvard **不是**其学位授予点，学历写希伯来大学（学士）+ 伯克利（博士） |
| 异规范弦年份 | page.md 未载 heterotic string 提出年份——禁写 1984/1985，只写「与 Harvey/Martinec/Rohm 共创」；「Princeton String Quartet」是绰号（whimsically nicknamed），照引 |
| KITP 头衔序列 | 曾任 KITP 所长 + Frederick W. Gluck 讲席 → 现任 Chancellor's Chair 理论物理教授；Princeton 端：Eugene Higgins 教授（至 1997）→ Thomas Jones 数学物理荣誉教授——三段勿混 |
| 院士年份 | APS Fellow 1974 / AAAS（艺术与科学院）1985 / NAS 1986 / AAAS（科学促进会）Fellow 1987——两个 AAAS 是不同机构，勿混 |
| Dirac Medal | ICTP Dirac Medal 1988（非 IOP Dirac Medal，与本批 Leggett 篇的 IOP 口径区分） |
| 政治叙述 | 2008 致 Bush 信、2015 美因瑙宣言、2026 核风险警告与罗马宣言——客观列事实即可，勿扩写政治评论 |
| 家庭 | 第一任妻 Shulamith (Toaff)（离婚，2 子）、第二任 Jacquelyn Savani（1 继女）；三兄弟职业各不相同（传播学/法学/剧作家），勿张冠李戴 |
| 在世口径 | page.md 无卒日——生卒行写「1941-02-19 生，在世」，death_date 省略 |
| 库内记录 | 本人 name_en 用库内 stub 形式 `David Gross`（非 `David J. Gross`），防分裂 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| asymptotic freedom | 渐近自由 | 短距弱耦合，诺奖核心 |
| quantum chromodynamics (QCD) | 量子色动力学 | 强核力理论 |
| non-Abelian gauge theory | 非阿贝尔规范理论 | 渐近自由的载体 |
| color charge | 色荷 | 强作用的荷 |
| quark confinement | 夸克禁闭 | 渐近自由的反面 |
| heterotic string | 异规范弦 | 「弦乐四重奏」共创 |
| Gross–Neveu model | 格罗斯–涅韦模型 | infobox known for |
| Standard Model | 标准模型 | QCD 补全其强作用部分 |
| Kavli Institute for Theoretical Physics | 卡弗里理论物理研究所 | KITP，UCSB |
| junior fellow | 青年研究员 | Harvard 1966–69，非学位 |
| Chancellor's Chair | 校长讲席教授 | UCSB 现职 |
| Mainau Declaration | 美因瑙宣言 | 2015 气候 / 2024 核武器两个版本勿混 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions（52k views，强推进 / 紧张）
- **匹配理由**: 「强推进」匹配渐近自由发现的冲击力——1973 年一篇论文扭转对强作用的理解、补全标准模型；「紧张」匹配夸克禁闭的物理意象：拉得越紧、力越强的那根无形之弦。
- **备选**（未采用）: Cinematic Experience（电影感，但更宜大定理高潮页且本批未用可留给后续批次）；Last Hope（20 世纪批次已多次占用）。
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`
- 批内 BGM 不重复备案：Giacconi=The Invisible Light、Abrikosov=PAST、Ginzburg=Through the Darkness、Leggett=SEA、Gross=Savage。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/David_J._Gross/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 关系入库引擎（幂等） |
| `MySQL/data/David_J._Gross.yaml` | yaml 数据文件 |

> **开始执行。每完成一步汇报。**
