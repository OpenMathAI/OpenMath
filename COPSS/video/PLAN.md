# COPSS Presidents' Award 视频系列 — 制作规划

> 以 `Fields_Medal/video`（13 集主题分类）、`Fields_Medal/video_timeline`（叙事时间线）、`Abel_Prize/video`（按年代 4 集）、`Chern_Medal/video`（介绍片 + 得主片）的 Beamer 版式为模板。
> 本规划确定：**如何分类、分几期、每期人物清单、素材与版式、制作流程**。

---

## 一、总体定位

- **奖项**：COPSS Presidents' Award（COPSS 会长奖），全称 Committee of Presidents of Statistical Societies Presidents' Award。
- **范围**：1981–2026 年全部 **46 位**得主，每年 1 人。
- **视频定位**：统计学科普纪录片系列。回答「统计学界最高荣誉颁给了谁、为什么、它如何折射统计学 45 年的发展史」。
- **输出形态**：每集一段 16:9 中文科普视频（Beamer 幻灯片 + 背景音乐合成），可独立观看，也可连看为一部完整的「统计学四十五年」。

---

## 二、分类方法与分集方案

### 2.1 为什么按年代分集（而不是按研究方向）

COPSS 是**年度个人奖**，与阿贝尔奖同构（每年 1 人、累积成史），因此采用与 `Abel_Prize/video` 一致的**按年代分期**策略：

| 考量 | 说明 |
|---|---|
| 叙事性 | 每年 1 人的节奏天然构成时间线，按年代可分集讲清「统计学从理论走向数据科学」的演进 |
| 均衡性 | 46 人按年代切分为 10/10/10/10/6，每集体量均衡 |
| 互补性 | 研究方向分类已见于 `copss_classification.md`（C1–C10）；人物页保留「研究方向」标签，综述页总结时代主题，两者互补 |

### 2.2 分集总表

| 集数 | 目录名（拟） | 年代 | 主题 | 人数 |
|---:|---|---|---|:---:|
| 00 | `episode-00-what-is-copss-presidents-award` | — | 什么是 COPSS 会长奖（介绍片） | — |
| 01 | `episode-01-foundations-1981-1990` | 1981–1990 | 奠基年代：统计理论大厦的奠基 | 10 |
| 02 | `episode-02-bayesian-computation-1991-2000` | 1991–2000 | 贝叶斯复兴与计算革命 | 10 |
| 03 | `episode-03-biostatistics-bioinformatics-2001-2010` | 2001–2010 | 生物统计爆发与华人崛起 | 10 |
| 04 | `episode-04-highdim-ml-2011-2020` | 2011–2020 | 高维统计与机器学习融合 | 10 |
| 05 | `episode-05-data-science-ai-2021-2026` | 2021–2026 | 数据科学、AI 与贝叶斯革新 | 6 |
| allinone | `episode-allinone` | 1981–2026 | **合集**（00–05 汇为一册） | 46 |

**得主合计：46 人**（每年 1 人，无共享年份）。

---

## 三、各集详细规划

> 每集结构：**标题页 → 人物页（每人 1 页）→ 本集综述页**。
> 人物页统一 `\personslide` 版式（左照片/占位、中信息卡、右核心贡献）。

### 第 00 集｜什么是 COPSS 会长奖（介绍片）

**核心问题**：统计学没有诺贝尔奖，那么统计学界的最高荣誉是什么？

| 要点 | 内容 |
|---|---|
| 什么是 COPSS | 五个统计学会的联席会议：ASA、SSC、IMS、ENAR、WNAR |
| 颁发机制 | 每年 1 人，在联合统计会议（JSM）上颁发 |
| 年龄规则 | 2005 年前须未满 41 岁；2005 年后放宽为「41 岁内」或「46 岁内 + 12 年内获统计学位」 |
| 地位 | 统计学界最高荣誉之一，与国际统计学奖（International Prize in Statistics）齐名 |
| 里程碑 | 首位得主 Bickel（1981）；首位女性 Reid（1992）；首位华人 Lai（1983）；9 位华人、6 位女性 |

**叙事线**：为什么需要这样一个奖 → 它如何评选 → 45 年名单里能读出统计学史的哪些章节 → 引出第 01–05 集。

### 第 01 集｜奠基年代（1981–1990）

> 主题：统计理论大厦的奠基——非参数、渐近理论、Bootstrap、试验设计、生存分析。
> 叙事线：从 Bickel 的经验过程与自适应估计奠基，经 Hinkley、Hall 的 Bootstrap 渐近理论，到 McCullagh 的 GLM 与传统建模体系——统计学「经典现代」格局成型。

| 序 | 得主 | 年份 | 机构 | 核心贡献 | 照片 |
|:--:|---|---|---|---|:--:|
| 1 | Peter J. Bickel | 1981 | UC Berkeley | 经验过程、自适应估计、半参数效率界（首位得主） | ✓ |
| 2 | Stephen Fienberg | 1982 | Carnegie Mellon | 列联表分析、统计与法律、数据隐私 | ✗ |
| 3 | Tze Leung Lai | 1983 | Stanford | 序贯分析、随机逼近渐近理论（首位华人得主） | ✗ |
| 4 | David V. Hinkley | 1984 | UC Santa Barbara | Bootstrap 变换法、鞍点近似 | ✗ |
| 5 | James O. Berger | 1985 | Duke | 统计决策论、客观贝叶斯分析 | ✓ |
| 6 | Ross L. Prentice | 1986 | Fred Hutchinson | 生存分析、临床试验、营养流行病学 | ✗ |
| 7 | C. F. Jeff Wu | 1987 | Georgia Tech | 试验设计、EM 算法收敛、鲁棒参数设计 | ✓ |
| 8 | Raymond J. Carroll | 1988 | Texas A&M | 测量误差模型、函数型数据 | ✗ |
| 9 | Peter Hall | 1989 | Australian National Univ. | Bootstrap 渐近理论、非参数曲线估计 | ✓ |
| 10 | Peter McCullagh | 1990 | Univ. of Chicago | 广义线性模型（GLM）、张量方法 | ✗ |

### 第 02 集｜贝叶斯复兴与计算革命（1991–2000）

> 主题：MCMC 掀起贝叶斯复兴；小波、LASSO 开启高维与信号处理；浓度不等式夯实理论。
> 叙事线：从 Silverman 的密度估计与 Reid 的似然理论，到 Wong、Donoho、Tibshirani 的方法爆发——统计学的「计算时代」开启。

| 序 | 得主 | 年份 | 机构 | 核心贡献 | 照片 |
|:--:|---|---|---|---|:--:|
| 1 | Bernard Silverman | 1991 | Univ. of Oxford | 密度估计、非参数回归、函数型数据 | ✓ |
| 2 | Nancy Reid | 1992 | Univ. of Toronto | 复合似然、高阶渐近（首位女性得主） | ✓ |
| 3 | Wing Hung Wong | 1993 | Stanford | MCMC、贝叶斯计算、计算生物学 | ✗ |
| 4 | David L. Donoho | 1994 | Stanford | 小波分析、压缩感知、高维推断 | ✓ |
| 5 | Iain M. Johnstone | 1995 | Stanford | 随机矩阵理论、小波阈值去噪 | ✓ |
| 6 | Robert J. Tibshirani | 1996 | Stanford | LASSO、Bootstrap、交叉验证 | ✓ |
| 7 | Kathryn Roeder | 1997 | Carnegie Mellon | 统计遗传学、多重检验、混合物模型 | ✗ |
| 8 | Pascal Massart | 1998 | Université de Paris-Sud | 浓度不等式、模型选择（首位法国得主） | ✗ |
| 9 | Larry A. Wasserman | 1999 | Carnegie Mellon | 非参数推断、置信带、统计学习 | ✓ |
| 10 | Jianqing Fan | 2000 | Princeton | 非参数模型、变系数模型、高维统计 | ✓ |

### 第 03 集｜生物统计爆发与华人崛起（2001–2010）

> 主题：贝叶斯软件化、基因组时代统计、因果推断方法论、华人得主集中涌现。
> 叙事线：从 Meng、Liu 的统计计算，Gelman 的多层次模型与 Stan，到 Lin、Irizarry 的基因组数据方法，再到 van der Laan 的 TMLE——统计学生物化、计算化的十年。

| 序 | 得主 | 年份 | 机构 | 核心贡献 | 照片 |
|:--:|---|---|---|---|:--:|
| 1 | Xiao-Li Meng | 2001 | Harvard | EM 算法理论、MCMC 收敛诊断 | ✗ |
| 2 | Jun Liu | 2002 | Harvard | MCMC、序贯蒙特卡洛、计算生物学 | ✗ |
| 3 | Andrew Gelman | 2003 | Columbia | 多层次贝叶斯模型、Stan 概率编程 | ✓ |
| 4 | Michael A. Newton | 2004 | Univ. of Wisconsin | 计算生物学、基因表达分析 | ✗ |
| 5 | Mark J. van der Laan | 2005 | UC Berkeley | TMLE、超级学习者、半参数因果推断 | ✗ |
| 6 | Xihong Lin | 2006 | Harvard | GWAS、基因-环境交互、统计遗传学 | ✓ |
| 7 | Jeff Rosenthal | 2007 | Univ. of Toronto | MCMC 收敛理论、随机过程 | ✓ |
| 8 | T. Tony Cai | 2008 | Univ. of Pennsylvania | 高维协方差估计、非参数极小极大 | ✓ |
| 9 | Rafael Irizarry | 2009 | Harvard | 基因组数据标准化、数据可视化 | ✗ |
| 10 | David Dunson | 2010 | Duke | 贝叶斯非参数、高维潜变量模型 | ✗ |

### 第 04 集｜高维统计与机器学习融合（2011–2020）

> 主题：高维统计理论成熟、因果推断与多重检验方法论、数据科学工具革命。
> 叙事线：从 Wainwright 的高维统计体系、Samworth 的高维非参数，到 Storey 的 q-value、Barber 的选择性推断，再到 Wickham 的 ggplot2/tidyverse——统计学与机器学习、数据科学全面融合。

| 序 | 得主 | 年份 | 机构 | 核心贡献 | 照片 |
|:--:|---|---|---|---|:--:|
| 1 | Nilanjan Chatterjee | 2011 | Johns Hopkins | 多基因风险评分、癌症风险建模 | ✓ |
| 2 | Samuel Kou | 2012 | Harvard | 单分子生物物理、随机过程推断 | ✗ |
| 3 | Marc A. Suchard | 2013 | UCLA | 贝叶斯系统发生学、BEAST 软件 | ✗ |
| 4 | Martin J. Wainwright | 2014 | UC Berkeley | 高维统计、图模型、信息论 | ✗ |
| 5 | John D. Storey | 2015 | Princeton | q-value、FDR 控制、统计基因组学 | ✗ |
| 6 | Nicolai Meinshausen | 2016 | ETH Zürich | 高维变量选择、不变因果预测 | ✗ |
| 7 | Tyler J. VanderWeele | 2017 | Harvard | 因果中介分析、效应分解 | ✓ |
| 8 | Richard J. Samworth | 2018 | Univ. of Cambridge | 高维非参数、变点检测、聚类 | ✓ |
| 9 | Hadley Wickham | 2019 | RStudio / Posit | ggplot2、tidyverse、数据科学工具革命 | ✓ |
| 10 | Rina Foygel Barber | 2020 | Univ. of Chicago | 选择性推断、Knockoff、FDR 后选择控制 | ✗ |

### 第 05 集｜数据科学、AI 与贝叶斯革新（2021–2026）

> 主题：数据科学教育、分布推断新范式、贝叶斯高维革新、AI 时代的统计学。
> 叙事线：从 Leek 的数据科学教育、Witten 的高维无监督学习，到 R. Tibshirani 的保形预测、Ročková 的尖峰平板先验，再到 Mackey 的大规模机器学习与 Su 的深度学习理论——统计学站上 AI 前沿。

| 序 | 得主 | 年份 | 机构 | 核心贡献 | 照片 |
|:--:|---|---|---|---|:--:|
| 1 | Jeffrey T. Leek | 2021 | Fred Hutchinson | 数据科学教育、可重复研究 | ✓ |
| 2 | Daniela Witten | 2022 | Univ. of Washington | 高维无监督学习、稀疏聚类 | ✗ |
| 3 | Ryan Tibshirani | 2023 | UC Berkeley | 保形预测、分布推断、非参数回归 | ✓ |
| 4 | Veronika Ročková | 2024 | Univ. of Chicago | 尖峰平板先验、贝叶斯高维选择 | ✗ |
| 5 | Lester Mackey | 2025 | Microsoft Research | 大规模核方法、概率推理与优化（首位工业界得主） | ✗ |
| 6 | Weijie Su | 2026 | Univ. of Pennsylvania | 深度学习理论、差分隐私、RL 数学基础 | ✗ |

### 合集（episode-allinone）

将全部 **46 位**得主汇为单一文档：1 张总封面 + 5 张分章标题页 + 46 张人物页（约 52 页），复用同一 `\personslide` 版式，便于一次浏览或整片输出。

---

## 四、素材盘点

### 4.1 人物照片（46 人中 21 人有真人照片）

| 状态 | 数量 | 说明 |
|---|---|:---:|
| ✓ 有真人照片 | 21 | 取自 `COPSS/pages/<年份>/<姓名>/images/`（Wikipedia 离线页） |
| ✗ 无照片 / 仅占位图标 | 25 | 如 Fienberg、Lai、Hinkley、Prentice、Carroll、McCullagh、Wong、Roeder、Massart、Meng、Liu、Newton、van der Laan、Irizarry、Dunson、Kou、Suchard、Wainwright、Storey、Meinshausen、Barber、Witten、Ročková、Mackey、Su |

> 注：McCullagh 的 images/ 内仅存牛顿画像（NewtonDetail）等通用图标，Dunson 仅存系统图标，均非本人照片，按「无照片」处理。

### 4.2 无照片处理方案

- 人物页照片位改用 **tikz 姓名缩写圆盘占位符**（首字母缩写 + 年份），配色用主题色，保持版式统一。
- 若后续找到公开照片（如大学官方页、学术会议照），直接替换对应 `images/` 文件即可，无需改版式。

### 4.3 背景音乐

- 复用 `Abel_Prize/video` / `Chern_Medal/video` 各集已有的 `awaken.wav` 作为 BGM（Makefile 自动探测 `*.wav`，有则循环配音）。

---

## 五、版式规划

| 项 | 方案 |
|---|---|
| 引擎 | XeLaTeX + Beamer，16:9（`aspectratio=169`，14pt），中文 PingFang SC |
| 配色 | **统计蓝主色**（`#2166AC`）+ 统计红强调（`#B2182B`）+ 暖金（`#E0913A`）+ 紫罗兰（`#6A51A3`），面板色派生——区别于菲尔兹奖（金）、阿贝尔奖（深蓝+翠绿）、陈省身奖章（深青+金）系列 |
| 人物页 | `\personslide` 宏：左照片/缩写圆盘、中间信息卡（获奖/生卒/国别/机构）、右侧核心贡献 |
| 综述页 | 每集末以「本集综述」时间线/主题块收束，给出时代关键词 |
| 角标 | 每页右下角页码；标题页带 `\faIcon{medal}` 徽标 |

---

## 六、制作流程与工具

| 阶段 | 命令 | 产物 |
|---|---|---|
| 1. 生成 tex | 由本规划 + `copss_winners.md` 数据生成各集 Beamer 文档 | `episode-*/copss_epXX_zh.tex` |
| 2. 编译 PDF | `make pdf`（latexmk -xelatex） | `copss_epXX_zh.pdf` |
| 3. 幻灯片图 | `make images`（pdftoppm -r 600） | `output/images/slide_*.png` |
| 4. 合成视频 | `make video`（ffmpeg concat + BGM） | `output/copss_epXX_zh.mp4` |
| 5. 清理 | `make clean` / `make distclean` | — |

依赖：`xelatex`（TeX Live）、`pdftoppm`（poppler）、`ffmpeg`、`python3`（均已就绪）。

目录结构（拟）：

```
COPSS/video/
├── Makefile                  # 顶层：make / pdf / images / video / clean
├── README.md                 # 制作完成后补齐（剧集目录 + 编译说明）
├── PLAN.md                   # 本文档
├── cover/                    # 封面图
├── episode-00-what-is-copss-presidents-award/
├── episode-01-foundations-1981-1990/
├── episode-02-bayesian-computation-1991-2000/
├── episode-03-biostatistics-bioinformatics-2001-2010/
├── episode-04-highdim-ml-2011-2020/
├── episode-05-data-science-ai-2021-2026/
└── episode-allinone/
```

---

## 七、输出清单与里程碑

| 阶段 | 输出 | 状态 |
|---|---|---|
| P0 | 本规划文档 | ✅ 本文档 |
| P1 | 第 00 集介绍片（tex → pdf → mp4） | 待制作 |
| P2 | 第 01–05 集（每集 10 人左右，tex → pdf → mp4） | 待制作 |
| P3 | 合集 allinone（46 人单文档） | 待制作 |
| P4 | video/README.md 补齐 + git 提交 | 待制作 |

**总计 7 个视频输出**（00–05 六集 + 合集），每集时长 ≈ 幻灯片数 × 7 秒（可调 `DURATION`）。

---

## 八、资料来源

- 离线人物页面：`COPSS/pages/<年份>/<姓名>/`
- 得主名录与获奖理由：`COPSS/copss_winners.md`
- 研究方向分类：`COPSS/copss_classification.md`（C1–C10）
- COPSS 官网：<https://community.amstat.org/copss/home>
- Wikipedia：<https://en.wikipedia.org/wiki/COPSS_Presidents%27_Award>
