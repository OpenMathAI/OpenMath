# 物理学家立传提示词（OpenPhysicist 21 世纪批次：Geoffrey Hinton）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主「人物专属立传提示词」，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Geoffrey Everest Hinton（杰弗里·辛顿，2024 诺贝尔物理学奖两位得主之一，"AI 教父"，反向传播的推广者与深度学习先驱）。**本篇是 2018 图灵奖与 2024 物理学奖的双冠条目**——OpenMathAI 图灵奖侧已完成其 Beamer 立传与社会关系入库，本篇按物理侧口径整理，两处事实须一致。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达，此两点为骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Geoffrey Everest Hinton（1947-12-06 生于伦敦温布尔登；在世，英国/加拿大双归属）
- **气质关键词**：**联结主义的坚守者、深度学习的点火人、AI 风险的吹哨人** —— 2024 诺贝尔物理学奖获奖理由（与 John J. Hopfield 共享）：
  > "for foundational discoveries and inventions that enable machine learning with artificial neural networks"（因基于人工神经网络实现机器学习的基础性发现和发明）
- **设计母题**：**层级表征（layered representation）**。深层网络逐层提取特征——视觉上可用一层层渐次抽象的特征金字塔表达；与 Hopfield 的"能量谷底"母题形成 2024 双得主篇的对照。
- **本地数据源（已有）**：`physicist/presentations/21th_century/21st_century/Geoffrey_Hinton/page.md`
- **待下载（第 0 步执行）**：`Geoffrey_Hinton.html` 与 `images/` 肖像尚未下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Geoffrey_Hinton`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对事实基准 【人物专属】

- page.md 已有本地，事实基准如下：
  - 生卒（1947-12-06 生于伦敦温布尔登；在世）
  - 国籍（英国 → 加拿大，双归属；frontmatter United Kingdom + Canada）
  - 家世（父 H. E. Hinton 昆虫学家条目；高祖外祖父辈：George Boole 是其高曾祖父、Mary Everest Boole 高曾祖母、George Everest 高曾叔祖、Colin Clark 舅公、Joan Hinton 表亲——身份页只列明载条目勿展开）
  - 婚姻（三段：Joanne；Rosalind Zalin 卒于 1994；Jacqueline Ford 1997 结婚、2018 去世——infobox 明载，身份页可简列）
  - 教育（布里斯托尔 Clifton College 中学；1967 入剑桥国王学院，在自然科学/艺术史/哲学间辗转后 1970 获实验心理学 BA；学徒木工一年；1972–1975 爱丁堡大学，1978 获人工智能 PhD，导师 Christopher Longuet-Higgins——导师偏好符号 AI 路线）
  - 博士后/早期任职（Sussex 大学 + MRC 应用心理学组；后赴美 UC San Diego、Carnegie Mellon；UCL Gatsby 计算神经科学单元创始主任；1987 年起多伦多大学至今，University Professor Emeritus；1987 入 CIFAR）
  - 产业界（2012 与学生 Krizhevsky、Sutskever 共创 DNNresearch，2013-03 被 Google 以 4400 万美元收购；2013–2023 Google Brain 与多伦多大学两头兼顾；2017 共创 Vector Institute 任首席科学顾问；2023-05 公开宣布离开 Google 以自由谈论 AI 风险）
  - 关键荣誉（Rumelhart 奖首奖 2001；Herzberg 加拿大金质奖章 2011；Killam 奖 2012；NAE 国际院士 2016；Wolfson Maxwell 奖 2016；BBVA 前沿知识奖 2016；**2018 图灵奖**与 Bengio、LeCun；Order of Canada 同伴勋位 2018；Dickson 奖 2021；阿斯图里亚斯亲王奖 2022；ACM Fellow + 美国科学院国际院士 2023；**2024 诺贝尔物理学奖**与 Hopfield；VinFuture 大奖 2024；2025 Queen Elizabeth 工程奖七人共享 + King Charles III 加冕勋章 + Sandford Fleming 奖章；2026 哈佛荣誉 DSc）
  - 知名学生（博士生 Zemel/Frey/Neal/Teh/Salakhutdinov/Sutskever/Krizhevsky/Brown；other notable students LeCun/Dayan/Welling/Ghahramani/Graves——本篇不入库，图灵奖侧已入库）
  - 核心贡献清单：
    1. 1986 与 Rumelhart、Williams 推广反向传播算法训练多层网络（非首个提出者；2018 访谈原句承认基本思路出自 Rumelhart）
    2. 1985 与 Ackley、Sejnowski 共同发明 Boltzmann 机
    3. 分布式表征、时延网络、专家混合、Helmholtz 机、专家乘积、wake-sleep 算法 1995
    4. 2008 与 van der Maaten 开发 t-SNE 可视化
    5. 2012 AlexNet（与 Krizhevsky、Sutskever）ImageNet 突破
    6. 2017 胶囊网络、2021 对比学习框架、2022 NeurIPS 提出 Forward-Forward 算法
  - 关键时间线（20 节点）：1947 生于温布尔登 → Clifton College → 1967 入剑桥国王学院 → 1970 实验心理学 BA → 木工学徒一年 → 1972–1975 爱丁堡 → 1978 AI PhD（Longuet-Higgins 门下） → Sussex + MRC → UCSD + CMU（联结主义 PDP 小组） → 1985 Boltzmann 机 → 1986 反向传播论文 → 1987 多伦多 + CIFAR → 1998 FRS → 2001 Rumelhart 奖 → 2004 CIFAR NCAP 项目创立并掌舵十年 → 2008 t-SNE → 2012 AlexNet + Coursera 课程 + DNNresearch → 2013 Google 收购 → 2017 Vector Institute → 2018 图灵奖 + 同伴勋位 → 2023 离开 Google → 2024 诺贝尔奖

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Geoffrey_Hinton/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品（如 `Serge_Haroche/Makefile`），设置 `MAIN=Geoffrey_Hinton_zh`、`VIDEO_NAME=Geoffrey_Hinton_zh`

### 第 3 步：收集图片 【人物专属】

- 下载 NeurIPS 2025 infobox 肖像（Commons 文件 `SD 2025 - Geoffrey Hinton 01.jpg`，Special:FilePath 下载，curl 加 `-A "Mozilla/5.0"`，`file` 验证）；404 则用 2024 诺奖周 Hopfield-Hinton 合影或装饰圆占位并注明

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> **本篇只出领域表供 Beamer 篇目使用；人员记录（fields/relations）已由图灵奖侧入库（has_social_data=1），勿重复执行 seed。**

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | deep learning | 深度学习 | 2018 图灵奖与 2024 诺奖共同主线 | 封面、核心页 |
| 1 | artificial neural network | 人工神经网络 | Boltzmann 机、AlexNet | 核心页 |
| 2 | machine learning | 机器学习 | 诺奖 citation 用语 | 核心页 |
| 3 | cognitive science | 认知科学 | 剑桥实验心理学、联结主义 | 早年页 |
| 4 | artificial intelligence | 人工智能 | 爱丁堡 AI 博士、2023 风险论述 | 晚年页 |

### 第 4.5 步：社会关系 【已入库，此处仅备查】

> **need_relations=false**：Hinton 在库内 id=280（Q92894，has_social_data=1），图灵奖侧 yaml `MySQL/data/Geoffrey_Hinton.yaml` 已含完整关系（导师 Longuet-Higgins、学生 Sutskever/Krizhevsky 等、co-honored Bengio/LeCun、2024 诺奖 co-honored Hopfield 已由本批 Hopfield yaml 对向写入）。**不要重跑 seed，不要新建 yaml 记录。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Christopher Longuet-Higgins | 师→生（博士导师） | 爱丁堡 AI 博士导师（图灵侧已入库） |
| co-honored | John J. Hopfield | 无向 | 2024 诺贝尔物理学奖共同得主（本批 Hopfield yaml 已对向写入） |
| co-honored | Yoshua Bengio / Yann LeCun | 无向 | 2018 图灵奖共同得主（图灵侧已入库） |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：层次、深度、警醒
- **主色**：深砖红 `#8C1F28` + 诺奖香槟金 `C9A227`
- badgeA–D 四分类色：badgeDL 深度学习 — 靛蓝 `#4C5FD5`；badgeBoltz Boltzmann 机 — 青绿 `#0E7C7B`；badgeAlex AlexNet 时刻 — 琥珀 `#E07B30`；badgeRisk AI 风险 — 玫瑰 `#C4204F`
- **背景母题**：特征金字塔（逐层抽象的嵌套矩形/圆环），与 Hopfield 篇能量谷底对照

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏 `国籍 | 机构 | 主要奖项` 三要素（国籍写 United Kingdom / Canada）。
3. 必须有身份信息页：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md infobox。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
5. **双冠一致性**：2018 图灵奖与 2024 诺贝尔奖并列时，图灵理由用 ACM 口径（"conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing"），诺奖理由用 Nobel 口径，两者勿互相代写。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — AI 教父 / Geoffrey Hinton 1947– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（家世 Boole 一行带过）
03  核心贡献概览 — 反向传播 / Boltzmann 机 / AlexNet / 深度学习
04  辗转的青年 (1947–1970) — 温布尔登、剑桥三换专业、实验心理学 BA、木工一年
05  爱丁堡的异端 (1972–1978) — Longuet-Higgins 门下、符号 AI 与联结主义之争
06  大洋两岸 (1978–1986) — Sussex/MRC → UCSD/CMU、PDP 联结主义小组
07  1985–1986：双重点火（核心贡献页一）— Boltzmann 机 + 反向传播推广（Rumelhart 归属注记）
08  多伦多长跑 (1987–2011) — CIFAR、NCAP 十年、分布式表征系列
09  2012：AlexNet 时刻（核心贡献页二）— ImageNet、Krizhevsky/Sutskever、深度学习元年
10  产业十年 (2012–2023) — DNNresearch 4400 万收购、Google Brain、Vector Institute
11  荣誉矩阵（高斯表格版式）— FRS 1998 / 图灵奖 2018 / Order of Canada 2018 / 诺奖 2024
12  2024 诺贝尔物理学奖 — 与 Hopfield 共享、citation 原句 + Feynman"值不值得"轶事注
13  吹哨人 (2023–) — 离开 Google、AI 风险论述（只转述 page.md 实载观点）
14  遗产：从 AI 寒冬到智能时代
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）整体复用同目录成品骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hinton 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 反向传播归属 | 1986 论文是"推广/普及"而非首创——Linnainmaa 1970 反向模式自动微分、Werbos 1974 已提出；2018 访谈原句承认基本思路出自 Rumelhart，归属注记必须带 |
| 双诺奖口径 | 2018 图灵奖（与 Bengio/LeCun）与 2024 诺贝尔物理学奖（与 Hopfield）是两组不同的"共享"，勿混 |
| 家世 | George Boole 是高曾祖父（great-great-grandfather）、Mary Everest Boole 高曾祖母——只列明载称谓，勿写"布尔之孙" |
| "AI 教父" | page.md 载 "the Godfather of AI" 称号，可用；"深度学习教父三人组"（Godfathers of Deep Learning）指 Hinton/Bengio/LeCun，勿加 Hopfield |
| 诺奖理由侧重 | citation 强调 machine learning with artificial neural networks；Boltzmann 机被诺奖声明明确提及——Boltzmann 页勿漏 |
| 离开 Google | 2023-05 辞职"以便自由谈论 AI 风险"，勿写成"被解雇"或"退休" |
| Schmidhuber 争议 | page.md 载其对 Hinton 学派未充分引用前人工作的批评——可作争议注，勿扩写为人身论战 |
| 生年 | 1947-12-06 无争议（与图灵侧一致）；在世，卒日留白 |
| 政治内容 | AI 风险/军事/监管观点只忠实转述 page.md 实载段落，不添加任何立场发挥 |
| 引语红线 | "Listen, buddy, if I could explain it in a couple of minutes, it wouldn't be worth the Nobel Prize."（转述 Feynman）与 "as a physicist..." 系 Hopfield 语——两条引语主人勿互换 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| backpropagation | 反向传播 | 非首创，1986 是推广 |
| Boltzmann machine | 玻尔兹曼机 | 诺奖声明点名成果 |
| restricted Boltzmann machine | 受限玻尔兹曼机 | 二部图结构 |
| deep belief network | 深度置信网络 | 2006 前传脉络 |
| AlexNet | AlexNet | 专名不翻译 |
| ImageNet | ImageNet | 图像识别挑战赛 |
| t-SNE | t-SNE | 可视化方法，缩写不翻译 |
| capsule neural network | 胶囊神经网络 | 2017 论文 |
| Forward-Forward algorithm | Forward-Forward 算法 | 2022 提出，两次前向传播 |
| connectionism | 联结主义 | 与符号主义对立路线 |
| knowledge distillation | 知识蒸馏 | "dark knowledge" 别名 |
| mortal computation | 必死计算 | Forward-Forward 配套概念，译法需加注原文 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（inspiring-electronic 合辑）
- **风格**：史诗 / 黑暗 / 推进
- **匹配理由**："突破前夕的黑暗与推进"精确对应 Hinton 的叙事弧线——AI 寒冬中坚守联结主义四十年，AlexNet 一夜翻盘，晚年又亲手拉响风险警报；黑暗与上行的双重性贯穿全篇。
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`
- **批内去重**：本曲在本批（batch 13）内不与 Agostini / Krausz / L'Huillier / Hopfield 重复。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Geoffrey_Hinton/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Geoffrey_Hinton.yaml` | 既有 yaml（图灵侧已入库，勿改勿重跑） |
| `MySQL/seed_person.py` | 幂等入库引擎（本篇不执行） |

> **开始执行。每完成一步向我汇报。**
