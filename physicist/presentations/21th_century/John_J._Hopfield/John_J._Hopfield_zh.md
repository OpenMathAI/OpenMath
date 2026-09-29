# 物理学家立传提示词（OpenPhysicist 21 世纪批次：John J. Hopfield）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主「人物专属立传提示词」，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Joseph Hopfield（约翰·霍普菲尔德，2024 诺贝尔物理学奖两位得主之一，Hopfield 网络的提出者，凝聚态物理 → 生物物理 → 神经科学的三级跳）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达，此两点为骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Joseph Hopfield（1933-07-15 生于芝加哥；在世）
- **气质关键词**：**联想记忆网络的提出者、物理学生物的摆渡人、AI 寒冬中的点火者** —— 2024 诺贝尔物理学奖获奖理由（与 Geoffrey Hinton 共享）：
  > "for foundational discoveries and inventions that enable machine learning with artificial neural networks"（因基于人工神经网络实现机器学习的基础性发现和发明）
- **设计母题**：**能量谷底（energy basin）**。Hopfield 网络的核心是"记忆 = 能量面 attractor"——视觉上可用一张带多个谷底的能量曲面（谷底放记忆图样）表达，与自旋玻璃的崎岖能量景观同构。
- **本地数据源（已有）**：`physicist/presentations/21th_century/21st_century/John_J._Hopfield/page.md`
- **待下载（第 0 步执行）**：`John_J._Hopfield.html` 与 `images/` 肖像尚未下载；Wikipedia URL：`https://en.wikipedia.org/wiki/John_J._Hopfield`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对事实基准 【人物专属】

- page.md 已有本地，事实基准如下：
  - 生卒（1933-07-15 生于芝加哥伊利诺伊州；在世）
  - 国籍（美国）
  - 父母（父 John Joseph Hopfield 为物理学家，波兰出生原名 Jan Józef Chmielewski——光谱学家条目；母 Helen Hopfield 娘家姓 Staff，亦是物理学家）
  - 教育（Swarthmore College 物理学士 1954；Cornell 大学物理学博士 1958，论文《A Quantum-Mechanical Theory of the Contribution of Excitons to the Complex Dielectric Constant of Crystals》）
  - 博士导师（Albert Overhauser，frontmatter + infobox + 正文三处明载）
  - 任职机构（Bell 实验室理论组两年（与 David Gilbert Thomas 合作半导体光学性质，后与 Robert G. Shulman 合作血红蛋白协同行为定量模型）；UC Berkeley 物理系 1961–1964；Princeton 物理系 1964–1980；Caltech 化学与生物 1980–1997；1997 年再回 Princeton 现为 Howard A. Prior 分子生物学荣休教授）
  - 关键荣誉（Sloan Fellow 1962；Guggenheim Fellow 1968（承其父）；APS 会士 1969；Oliver E. Buckley 凝聚态物理奖 1969 与 David Gilbert Thomas；NAS 院士 1973；美国艺术与科学院院士 1975；美国哲学学会会员 1988；MacArthur 奖 1983；Golden Plate 奖 1985；Max Delbrück 生物物理奖 1985；Michelson–Morley 奖 1988；IEEE 神经网络先驱奖 1997；ICTP Dirac 奖章 2001；Harold Pender 奖 2002；Albert Einstein 世界科学奖 2005；APS 会长 2006；IEEE Frank Rosenblatt 奖 2009；Swartz 奖 2012；Benjamin Franklin 物理学奖章 2019；Boltzmann 奖章 2022 与 Deepak Dhar 共享；2024 诺贝尔物理学奖；2025 Queen Elizabeth 工程奖七人共享）
  - 知名博士生（正文 + infobox 明载八人：Gerald Mahan 1964、Bertrand Halperin 1965、Steven Girvin 1977、Terry Sejnowski 1978、José Onuchic 1987、Li Zhaoping 1990、David J. C. MacKay 1992、Erik Winfree 1998）
  - 核心贡献清单：
    1. 1958 博士工作提出激子-光子耦合准粒子并首创 polariton 一词（Hopfield dielectric）
    2. 1959–1963 与 D. G. Thomas 研究硫化镉激子结构，奠定 II-VI 族半导体光谱理解
    3. 1973 年与 William C. Topp 引入 norm-conserving 赝势概念
    4. 1974 年提出 kinetic proofreading（动力学校读）解释 DNA 复制精度
    5. 1982 年发表《Neural networks and physical systems with emergent collective computational abilities》，提出 Hopfield network（内容寻址记忆）；1984 年扩展到连续激活函数（两篇为其最高被引）
    6. 1994 年开创临界脑假说，首个把神经网络与自组织临界性联系；2016 年与 Dimitry Krotov 提出现代 Hopfield 网络
  - 关键时间线（20 节点）：1933 生于芝加哥 → 1954 Swarthmore 学士 → 1958 Cornell 博士（激子/介电常数，polariton） → Bell 实验室理论组两年 → 1959–1963 与 Thomas 硫化镉激子 → 1961–1964 Berkeley → 1962 Sloan → 1964–1980 Princeton → 1968 Guggenheim → 1969 Buckley 奖 + APS 会士 → 1973 NAS 院士 → 1974 kinetic proofreading → 1975 艺术与科学院 → 1976 与 Pauling 合拍血红蛋白结构科普片 → 1980–1997 Caltech → 1981–1983 与 Feynman、Mead 开"计算的物理学"课 → 1982 Hopfield network 论文 → 1983 MacArthur 奖 → 1984 连续激活函数扩展 → 1986 共创 Caltech CNS 博士项目 → 1988 美国哲学学会 → 1994 临界脑假说 → 1997– 回 Princeton → 2001 Dirac 奖章 → 2006 APS 会长 → 2016 现代 Hopfield 网络 → 2019 Franklin 奖章 → 2022 Boltzmann 奖章 → 2024 诺贝尔奖

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `John_J._Hopfield/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品（如 `Serge_Haroche/Makefile`），设置 `MAIN=John_J._Hopfield_zh`、`VIDEO_NAME=John_J._Hopfield_zh`

### 第 3 步：收集图片 【人物专属】

- 下载 2024 诺贝尔演讲上的 infobox 肖像（Commons `Special:FilePath`：`John J. Hopfield and Geoffrey E. Hinton, 2024 Nobel Prize Laureate in Physics.jpg` 为合影，优先找单人照；REST API 回退；curl 加 `-A "Mozilla/5.0"`，`file` 验证）；404 则装饰圆占位并注明

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | artificial neural network | 人工神经网络 | Hopfield network，2024 诺奖核心 | 核心页 |
| 1 | condensed matter physics | 凝聚态物理 | polariton、II-VI 半导体、Anderson 杂质模型 | 早年页 |
| 2 | statistical physics | 统计物理 | 自旋玻璃灵感、Boltzmann 奖章 | 网络页 |
| 3 | biophysics | 生物物理 | kinetic proofreading、血红蛋白模型 | 生物页 |
| 4 | molecular biology | 分子生物学 | Caltech 化学与生物系、Howard A. Prior 教席 | Caltech 页 |

- 入库：`cd MySQL && python3 seed_person.py data/John_J._Hopfield.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；对手方无 qid 不编造。库内既有记录沿用规范名：Terry Sejnowski(id=1795)、Geoffrey Hinton(id=280, Q92894)、Philip Warren Anderson(id=2628)、Richard P. Feynman(id=2410)。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Albert Overhauser | 师→生（博士导师） | Cornell 博士导师，激子介电常数论文 |
| advisor-student | Gerald Mahan | Hopfield → 学生 | 博士生 1964 |
| advisor-student | Bertrand Halperin | Hopfield → 学生 | 博士生 1965 |
| advisor-student | Steven Girvin | Hopfield → 学生 | 博士生 1977 |
| advisor-student | Terry Sejnowski | Hopfield → 学生 | 博士生 1978，计算神经科学先驱 |
| advisor-student | José Onuchic | Hopfield → 学生 | 博士生 1987 |
| advisor-student | Li Zhaoping | Hopfield → 学生 | 博士生 1990 |
| advisor-student | David J. C. MacKay | Hopfield → 学生 | 博士生 1992，《Information Theory》作者 |
| advisor-student | Erik Winfree | Hopfield → 学生 | 博士生 1998，DNA 计算 |
| co-honored | Geoffrey Hinton | 无向 | 2024 诺贝尔物理学奖共同得主 |
| co-honored | David Gilbert Thomas | 无向 | 1969 Oliver E. Buckley 奖共同得主 |
| co-honored | Deepak Dhar | 无向 | 2022 Boltzmann 奖章共同得主 |
| colleague | Philip Warren Anderson | 无向 | Anderson 自述 Hopfield 是其 1961–1970 杂质模型研究的 hidden collaborator（未署名） |
| colleague | David Gilbert Thomas | 无向 | Bell 实验室合作者，II-VI 族半导体光谱 |
| colleague | Carver Mead | 无向 | 1981–1983 Caltech 合开 The Physics of Computation 课程 |
| colleague | Richard P. Feynman | 无向 | 1981–1983 Caltech 合开 The Physics of Computation 课程 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：跨界的桥、能量谷底、沉静的颠覆
- **主色**：石墨蓝灰 `#37474F` + 诺奖香槟金 `C9A227`
- badgeA–D 四分类色：badgeNet Hopfield 网络 — 靛蓝 `#4C5FD5`；badgeCM 凝聚态 — 青绿 `#0E7C7B`；badgeBio 生物物理 — 琥珀 `#E07B30`；badgeCrit 临界脑 — 玫瑰 `#C4204F`
- **背景母题**：多谷底能量曲面（等高线 + 数个谷底亮点），记忆即吸引子

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页：封面之后、核心贡献之前，左头像 + 右信息网格（含父母物理学家背景、四段任职、师承），事实取自 page.md infobox。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 联想记忆之父 / John J. Hopfield 1933– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — polariton / kinetic proofreading / Hopfield network / 临界脑
04  物理学家的家庭 (1933–1954) — 芝加哥、父母皆物理学家、Swarthmore
05  Cornell 博士 (1954–1958) — Overhauser 门下、激子、首创 polariton
06  Bell 实验室与 Berkeley (1958–1964) — D. G. Thomas 硫化镉、1969 Buckley 奖
07  Princeton 二十年 (1964–1980) — 赝势 1973、kinetic proofreading 1974
08  Caltech 转身 (1980–1997) — 化学与生物系、与 Feynman/Mead 的"计算的物理学"课
09  1982：Hopfield network（核心贡献页一）— 能量谷底图式、内容寻址记忆、AI 寒冬中的点火
10  1984–1986 — 连续激活函数、与 Tank 的模拟退火优化
11  从自旋玻璃到神经网络 — 灵感源自与 P. W. Anderson 的合作（hidden collaborator 注记）
12  临界脑与现代回归 — 1994 临界脑假说、2016 现代 Hopfield 网络（Krotov）
13  门生谱系 — Mahan/Halperin/Girvin/Sejnowski/Onuchic/Zhaoping/MacKay/Winfree
14  荣誉矩阵（高斯表格版式）— Buckley 1969 / MacArthur 1983 / Dirac 2001 / Boltzmann 2022
15  2024 诺贝尔物理学奖 — 与 Hinton 共享、citation 原句 + AI 忧思一句
16  遗产：物理学生物的摆渡人
17  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）整体复用同目录成品骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hopfield 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 父子同名 | 父亲亦名 John Joseph Hopfield（光谱学家，波兰出生原名 Jan Józef Chmielewski），引用时须区分，勿把父亲的史实混入本人 |
| 教育前置 | frontmatter educated_at 有 Universidad Nacional Federico Villarreal（秘鲁），但 page.md 正文教育节只载 Swarthmore + Cornell——正文为准，秘鲁学位禁写 |
| AI 寒冬表述 | "Hopfield's work revitalized large-scale interest"——是复兴兴趣，勿写成"发明了神经网络"或"终结 AI 寒冬" |
| hidden collaborator | Anderson 杂质模型的贡献是 Anderson 自述（未署名合作），勿写成 Anderson 的导师/学生或正式合作者 |
| 1982 论文标题 | 《Neural networks and physical systems with emergent collective computational abilities》，投稿刊物 PNAS 可写但标题勿改写 |
| polariton 首创 | 首创术语出自 1958 博士工作原句 "The polarization field 'particles' analogous to photons will be called 'polaritons'"——引语可用原文 |
| Boltzmann 奖章 | 2022 与 Deepak Dhar 共享（统计物理），勿写成独得 |
| QEPrize 七人 | 2025 Queen Elizabeth 工程奖与 Bengio、Dally、Hinton、LeCun、Huang、Fei-Fei Li 七人共享——可在荣誉页列名，勿写成"三人"或漏 Hinton 之外的顺序 |
| 引语红线 | "as a physicist, I'm very unnerved by something which has no control" 是 page.md 实载原句可用；其余 AI 风险表述只转述勿编造引语 |
| Feynman 关系 | 与 Feynman 是合开课程同事（1981–1983），非师生，勿建 advisor-student |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Hopfield network | Hopfield 网络 | 人名不翻译 |
| content-addressable memory | 内容寻址记忆 | 联想记忆的技术表述 |
| polariton | 极化激元 | 本人首创术语 |
| kinetic proofreading | 动力学校读 | 生化纠错机制 |
| exciton | 激子 | 半导体中电子-空穴束缚态 |
| spin glass | 自旋玻璃 | 网络灵感的物理来源 |
| attractor | 吸引子 | 能量面谷底即记忆 |
| self-organized criticality | 自组织临界性 | 临界脑假说核心 |
| modern Hopfield network | 现代 Hopfield 网络 | 2016 与 Krotov 大容量扩展 |
| AI winter | AI 寒冬 | 1982 前的领域低潮期 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（alex-productions 合辑）
- **风格**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：Hopfield 的生涯是一条从凝聚态物理经生物物理到神经科学的长期摆渡线——1982 年的"冷门论文"四十年后获诺奖，"Timeless / 长期纲领"是最贴合的时间气质。
- **本地路径**：`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`
- **批内去重**：本曲在本批（batch 13）内不与 Agostini / Krausz / L'Huillier / Hinton 重复。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/John_J._Hopfield/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/John_J._Hopfield.yaml` | 社会关系 + 领域入库 yaml |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
