# 经济学家立传提示词（Tjalling Koopmans）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1975 年得主 Tjalling Koopmans（佳林·库普曼斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Tjalling_Koopmans/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Tjalling Charles Koopmans（1910-08-28 生于荷兰 's-Graveland ~ 1985-02-26 逝于美国康涅狄格州纽黑文，享年 74 岁）
- **气质关键词**：**从量子化学到资源最优配置的跨界者、活动分析的构建者、Cowles 委员会的掌舵人**
- **诺奖获奖理由**（1975，与 Kantorovich 共享，逐字引用 manifest）：
  > "for their contributions to the theory of optimum allocation of resources"（因其对资源最优配置理论的贡献）
- **设计母题**：**最优配置（optimal allocation）**——把稀缺资源在约束下安置到最有效率的去处：错落的方块与流向箭头构成背景母题，呼应「在效率准则下推导最优价格体系」的核心思想。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Tjalling_Koopmans/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Tjalling_Koopmans/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位；KoopmansLeuven1967.jpg 为 1967 鲁汶大学照片）；Makefile 复制后设 `MAIN=Tjalling_Koopmans_zh`、`VIDEO_NAME=Tjalling_Koopmans_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Koopmans 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | mathematical economics | 数理经济学 | 诺奖核心：资源最优配置理论 | 封面、核心页 |
| 1 | activity analysis | 活动分析 | 投入产出交互与经济效率、价格的关系 | 核心页 |
| 2 | econometrics | 经济计量学 | 1942 序列相关系数分布论文（von Neumann 识其重要） | 方法页 |
| 3 | transport economics | 运输经济学 | Hitchcock–Koopmans 运输问题、最优路径 | 早期页 |
| 4 | quantum chemistry | 量子化学 | Koopmans' theorem（Hartree-Fock 分子结构早期工作） | 跨界页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Kramers | Koopmans → 学生 | 莱顿大学博士导师（1936，论文《经济时间序列的线性回归分析》） |
| advisor-student | Jan Tinbergen | Koopmans → 学生 | 1933 相遇后赴阿姆斯特丹师从习数理经济学；infobox 列为博士导师 |
| advisor-student | Carl Christ | Koopmans → 学生 | infobox Doctoral students 明载 |
| advisor-student | Stanley Reiter | Koopmans → 学生 | infobox Doctoral students 明载 |
| advisor-student | Rolf Mantel | Koopmans → 学生 | infobox Doctoral students 明载（红链人物仍入边） |
| advisor-student | Guillermo Calvo | Koopmans → 学生 | infobox Doctoral students 明载 |
| co-honored | Leonid Kantorovich | 无向 | 1975 诺贝尔经济学奖共享（资源最优配置理论） |
| collaborator | Gérard Debreu | 无向 | 1982 合著《加性可分解拟凸函数》（Cowles 论文；入库边由 Debreu 本人批次建立） |
| spouse | Truus Wanningen | 无向 | 1936-10 结婚，育一子二女 |
| parent-child | Sjoerd Koopmans | Koopmans → 子 | 父（中间名 Charles 或源于父系父名 Sjoerds） |
| parent-child | Wytske van der Zee | Koopmans → 子 | 母 |

**不入库但提示词可叙述**：表弟 Simon van der Meer（诺贝尔物理学奖得主，first cousins once removed，隔代远亲不入库）；兄 Jan Koopmans（神学家，《Bijna te laat》小册子作者）；子女 Henry/Anne/Helen（仅具名，无独立条目，不入库）；John von Neumann（仅「识得其 1942 论文之重要」，单向赏识非关系，禁建边）；John Denis Sargan 与 Alok Bhargava（其论文的后续影响者）。

## 五、配色方案 【人物专属】

- **气质**：理性、克制、效率之美
- **主色**：`#283593`（靛蓝——数理经济学的抽象秩序感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAlloc` 资源最优配置 — 靛蓝 `#283593`
  - `badgeAct` 活动分析 — 深蓝 `#16324F`
  - `badgeEcon` 经济计量 — 青绿 `#0E7C7B`
  - `badgeCross` 量子化学跨界 — 琥珀 `#C07A2A`
- **背景母题**：错落方块与流向箭头（稀缺资源在约束下流向最有效率的配置）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 资源最优配置理论的构建者 / Tjalling Koopmans 1910–1985 + 四色 badge + 右上头像 + 国籍行（Netherlands / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 's-Graveland、教育乌得勒支/莱顿、
    任职 Chicago Cowles Commission→Yale Cowles Foundation、1946 入籍美国、诺奖 1975、核心领域）
03  核心贡献概览 — 资源最优配置 / 活动分析 / 经济计量学 / 运输问题 / Koopmans' theorem
04  荷兰早年：从数学到物理 (1910–1933) — 17 岁进乌得勒支主修数学，1930 转向理论物理
05  转向经济学：Tinbergen 门下 (1933–1936) — 阿姆斯特丹习数理经济学，莱顿 PhD（Kramers 指导）
06  国际联盟岁月 — 经济与金融组织任职，运输经济学与最优路径
07  赴美与 Cowles 委员会 (1940–1948) — 华盛顿政府机构→芝加哥 Cowles，1946 入籍，1948 出任主任
08  活动分析：效率与价格（核心贡献页）— 投入产出交互、效率准则推出最优价格体系
09  Koopmans' theorem — Hartree-Fock 早期工作在量子化学的深远影响（跨界页）
10  Cowles 迁往耶鲁 (1955) — 芝加哥经济系敌意环境下说服 Cowles 家族迁址，更名 Cowles Foundation
11  最优增长理论 — 晚期研究重心：Ramsey–Cass–Koopmans 模型脉络
12  1975 诺贝尔经济学奖 — 与 Kantorovich 共享；诺奖演讲 Concepts of optimality and their uses (1975-12-11)
13  以 Koopmans 命名 — Koopmans' theorem / Hitchcock–Koopmans 运输问题 / Ramsey–Cass–Koopmans 模型
14  遗产与结尾 — 从线性规划到现代资源配置理论 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 博士导师双师 | infobox 列 Kramers 与 Tinbergen 两人为 doctoral advisor；正文口径：莱顿 PhD（1936）师从 Kramers，1933 起在阿姆斯特丹随 Tinbergen 学数理经济学。两行入库均合法，note 须区分两段经历，勿合并成一句 |
| Kramers 姓名形式 | 正文链接作 Hendrik Kramers，infobox/frontmatter 作 Hans Kramers；库内规范记录为 **Hans Kramers**（id=2129），yaml 用库内形式，提示词可括注「即 Hendrik Kramers」 |
| 全名 | Tjalling **Charles** Koopmans，中间名 Charles 可能源于父名 Sjoerds 的父名（patronymic）转写，勿写成中间名「查尔斯」随意发挥 |
| 国籍口径 | Nobel/manifest 口径 Netherlands / United States（1946 入籍美国）；frontmatter 作 Kingdom of the Netherlands，yaml 按 manifest 拆两条 |
| 1975 共享理由 | 与 Kantorovich 共享，官方理由 "for **their** contributions..."（复数），诺奖演讲仅本人一场（Concepts of optimality and their uses）；勿写「独得」或「平分」等无载表述 |
| Kantorovich 关系 | 仅 co-honored 一条边（两人工作互不隶属，page.md 无任何合作记载，禁写「共同发展」「师承影响」） |
| von Neumann 禁建边 | page.md 仅载 von Neumann「识得」其 1942 序列相关论文之重要——单向赏识非社会关系，不入库 |
| 家族远亲 | Simon van der Meer（1984 诺贝尔物理学奖）是其表侄（first cousins once removed），叙述可一句带过，禁建库边 |
| 兄长事迹 | 兄 Jan Koopmans 1940 年印发反纳粹小册子《Bijna te laat》（3 万份）、1945 目睹人质处决时被流弹重伤身亡——客观简述即可，不展开战争叙事 |
| Cowles 两段 | 1948 出任芝加哥 **Cowles Commission** 主任；1955 随机构迁耶鲁更名 **Cowles Foundation**——两名称勿混用 |
| Koopmans' theorem | 属量子化学（Hartree-Fock 分子结构），与其经济学贡献无关，勿与运输问题/活动分析混写 |
| 无直接引语 | page.md 无任何 Koopmans 原话引语，全篇禁写「原话」，引用仅限获奖理由与论文名 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| optimum allocation of resources | 资源最优配置 | 获奖理由核心词 |
| activity analysis | 活动分析 | 生产投入产出交互的研究框架 |
| Hitchcock–Koopmans transportation problem | Hitchcock–Koopmans 运输问题 | 最优路径研究，勿简写为「运输模型」 |
| Koopmans' theorem | Koopmans 定理 | 量子化学概念，与经济学无关 |
| Ramsey–Cass–Koopmans model | 拉姆齐–卡斯–库普曼斯模型 | 最优增长理论命名，三人并列勿漏 |
| serial correlation | 序列相关 | 1942 论文主题，von Neumann 识其重要 |
| Cowles Commission / Foundation | 考尔斯委员会/基金会 | 同一机构两阶段两名称 |
| econometrics | 经济计量学 | 与数理经济学层次不同 |
| dynamic models | 动态模型 | 1969 首届得主 Tinbergen/Frisch 的获奖理由用词，勿错挂到 Koopmans |
| League of Nations | 国际联盟 | 其经济与金融组织任职经历 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从乌得勒支的数学少年到量子化学前沿、再跨界经济计量与资源最优配置，Koopmans 一生是一次跨越学科疆界的远征——「Expedition」的行进感贴合其从荷兰到美国、从物理到经济的多段旅程；曲风的理性节奏也匹配活动分析的秩序之美。
- **本地路径**：复制 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` 到 `economics/presentations/20th_century/Tjalling_Koopmans/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
