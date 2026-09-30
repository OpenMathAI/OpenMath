# 经济学家立传提示词（Lars Peter Hansen）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2013 年得主 Lars Peter Hansen（拉尔斯·彼得·汉森）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Lars_Peter_Hansen/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Lars Peter Hansen（1952-10-26 生于美国伊利诺伊州厄巴纳，在世）
- **气质关键词**：**广义矩方法的缔造者、不确定性的度量者、连接金融与宏观的计量大师**
- **诺奖获奖理由**（2013 三人共享同句，manifest citation_en 已给出，逐字引用）：
  > "for their empirical analysis of asset prices"（表彰他们对资产价格的实证分析）
  - 共享得主：Eugene Fama / Lars Peter Hansen / Robert J. Shiller——Hansen 一翼是方法论：以 GMM 等计量工具为资产定价实证奠基。
- **设计母题**：**矩条件（moment conditions）**——无需完全设定复杂经济模型，仅凭零条件期望的矩条件即可构建可靠估计量：散落的观测点向一条隐含约束线收敛的视觉隐喻，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Lars_Peter_Hansen/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Lars_Peter_Hansen/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Lars_Peter_Hansen_zh`、`VIDEO_NAME=Lars_Peter_Hansen_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hansen 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | GMM 的发明学科；infobox occupation 含 statistician | 封面、核心页 |
| 1 | macroeconomics | 宏观经济学 | 金融部门与宏观经济的联动；infobox Discipline | 核心页 |
| 2 | financial economics | 金融经济学 | 资产估值模型的 GMM 应用 | 核心页 |
| 3 | asset pricing | 资产定价 | 2013 诺奖核心——随机贴现因子与风险冲击定价 | 贡献页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 15 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Christopher A. Sims | 对方是导师 | 明尼苏达大学博士导师（1978） |
| influence | Thomas J. Sargent | 对方影响本人 | infobox Influences 明载 |
| collaborator | Thomas J. Sargent | 无向 | 合著《Robustness》(2007)《Uncertainty Within Economic Models》(2014) |
| collaborator | Kenneth J. Singleton | 无向 | 1982 理性预期模型论文；1984 共获 Frisch Medal |
| collaborator | José Scheinkman | 无向 | 长期风险–收益权衡合作 |
| collaborator | Scott F. Richard | 无向 | GMM 资产估值合作者（正文明载） |
| collaborator | Robert Hodrick | 无向 | 1980 远期汇率论文合著者 |
| advisor-student | Ravi Jagannathan | 本人 → 学生 | infobox Doctoral students；Hansen–Jagannathan bound 合作者 |
| advisor-student | Narayana Kocherlakota | 本人 → 学生 | infobox Doctoral students 明载 |
| advisor-student | Masao Ogaki | 本人 → 学生 | infobox Doctoral students 明载 |
| advisor-student | Amir Yaron | 本人 → 学生 | infobox Doctoral students 明载 |
| colleague | Andrew Lo | 无向 | 2008 危机后共同领导 Macro Financial Modeling Group |
| spouse | Grace Tsiang | 无向 | 妻蒋人瑞，经济学家 Sho-Chieh Tsiang 之女；一子 Peter |
| co-honored | Eugene Fama | 无向 | 2013 同句理由共享诺奖 |
| co-honored | Robert J. Shiller | 无向 | 2013 同句理由共享诺奖 |

**不入库但提示词可叙述**：岳父 Sho-Chieh Tsiang（姻亲无关系类型，仅叙述）；父 Roger Gaurth Hansen（犹他州立大学教务长、生物化学教授）与兄弟 Ted Howard Hansen（免疫学家）/ Roger Hansen（水资源工程师）——家人具名仅叙述；合著者 John Heaton、J. Borovička（Selected writings 列表内出现，未在正文叙述合作脉络，防噪声不入库）；1982 GMM 论文独立署名无对手方。

## 五、配色方案 【人物专属】

- **气质**：严谨、深邃、在不确定性中寻找结构
- **主色**：`#8A1E2D`（manifest 预分配，2013 三人共享年份统一主色，芝加哥深红）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGMM` 广义矩方法 — 深红 `#8A1E2D`
  - `badgeMacro` 宏观金融 — 深蓝 `#16324F`
  - `badgeBound` Hansen–Jagannathan bound — 青绿 `#0E7C7B`
  - `badgeRobust` 稳健控制 — 琥珀 `#C07A2A`
- **背景母题**：散点向隐含约束线收敛（矩条件的估计几何），呼应「以矩条件构建可靠估计量」的方法论内核。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 不确定性的度量者 / Lars Peter Hansen 1952– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1952-10-26 厄巴纳、Utah State B.S. 1974、
    明尼苏达 PhD 1978、导师 Sims、CMU→芝加哥 1981、诺奖 2013、核心领域）
03  核心贡献概览 — GMM / 资产定价实证 / 稳健控制 / 系统性风险
04  犹他与明尼苏达 (1952–1978) — 数学+政治学本科、Sims 门下博士论文（可耗竭资源市场计量建模）
05  CMU 与芝加哥 (1978–1981) — 助理/副教授，1981 转芝加哥
06  GMM：矩条件的胜利 (1982) — Econometrica 论文；比极大似然更宽松的模型假设
07  GMM 的应用版图 — 劳动经济学、国际金融、金融、宏观的全面渗透
08  资产估值的 GMM 应用 — Singleton / Richard / Hodrick 合作脉络；1984 Frisch Medal
09  Hansen–Jagannathan bound (1991) — 随机贴现因子波动下限；股权溢价之谜的联系
10  与 Sargent 合著：稳健性 — 决策者怀疑单一统计模型时的宏观建模
11  风险与不确定性（Knightian uncertainty）— 系统性风险、2008 金融危机、政策制定中的不确定性
12  诺奖时刻 (2013) — 10-14 公布、同句理由、诺奖演讲 Uncertainty Inside and Outside Economic Models
13  机构建设与荣誉 — Becker Friedman Institute 首任院长、SoFiE 创始人、BBVA 2011、Nemmers 2006
14  遗产与结尾 — 计量工具成为经济学通用语言 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享理由 | 2013 三人共享**同句理由** "for their empirical analysis of asset prices"（page.md Nobel 节明载 award cited 其语）；勿写成 Hansen 个人理由 |
| Sargent 双重定性 | infobox Influences 与正文合著皆明载：入库 **influence + collaborator 两行**，勿合并丢失信息，也勿建 advisor-student（Sargent 非其导师，导师只有 Sims） |
| Jagannathan 双重身份 | 既是 infobox Doctoral students 之一，又是 Hansen–Jagannathan bound 合作者——只建 advisor-student 一行，note 兼述 bound 合作 |
| Sims 只有师生一行 | Sims 同时是导师与 infobox Influences 之一——advisor-student 已涵盖，不再单建 influence 行 |
| GMM 等价性表述 | 正文明确 GMM 估计量与 Sargan「正交条件」/Huber「无偏估计方程」数学等价——写 GMM 时用「发展/提出」口径，勿写「独创前无古人」 |
| 任职时间线 | Utah State 1974 本科 → Minnesota 1978 博士 → CMU 助理/副教授 → **1981** 转芝加哥；勿把 CMU 写成芝加哥之前无任职 |
| 妻子拼写 | Grace Tsiang（蒋人瑞，拼音 Jiǎng Rénruì）；岳父 Sho-Chieh Tsiang——姻亲不入库，仅叙述 |
| BBVA 年份 | 正文两处口径：总述 "2010"、详述 2011 "for making fundamental contributions..."——**以详述 2011 为准**（2010 为 frontmatter 噪声），陷阱表注明 |
| 在世者生卒 | 1952-10-26 生，在世——卒日留白，全篇一致 |
| 引语红线 | 诺奖演讲题 "Uncertainty Inside and Outside Economic Models" 是标题可直引；BBVA 授奖辞引语有英文原文可引原文+译文；其余勿杜撰「原话」 |
| 南瓜派 | Miscellaneous 节 "favorite pie is pumpkin pie" 是维基趣味注脚——可作结尾彩蛋小字，勿进正史页 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| generalized method of moments (GMM) | 广义矩方法 | Hansen 1982 提出；与 Sargan/Huber 先行工作数学等价 |
| moment condition | 矩条件 | 真参数值处条件期望为零的关系 |
| stochastic discount factor | 随机贴现因子 | Hansen–Jagannathan bound 的主角 |
| Hansen–Jagannathan bound | 汉森–贾甘纳坦界 | SDF 波动率/均值之比 ≥ 任何资产 Sharpe ratio |
| equity premium puzzle | 股权溢价之谜 | bound 在实践中常常失效的现象 |
| robust control | 稳健控制 | 与 Sargent 合著主线；决策者怀疑模型本身 |
| Knightian uncertainty | 奈特式不确定性 | 风险与不确定性的区分 |
| systemic risk | 系统性风险 | 2008 金融危机语境，度量与遏制 |
| dynamic valuation decomposition | 动态估值分解 | 风险冲击期限结构的研究工具 |
| Frisch Medal | 弗里施奖章 | 计量经济学会应用论文奖，1984 与 Singleton 共获 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从可耗竭资源市场的博士论文到金融危机后的系统性风险度量，Hansen 的关键词始终是「不确定性中的希望」——GMM 让经济学家在不完全设定模型时依然可信地估计世界，恰是「last hope」的方法论回响；与 2013 三人共享年份统一用曲。
- **本地路径**：复制上述 wav 到 `economics/presentations/21th_century/Lars_Peter_Hansen/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
