# 经济学家立传提示词（Robert Solow）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1987 年得主 Robert Solow（罗伯特·索洛）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Robert_Solow/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert Merton Solow（1924-08-23 生于纽约布鲁克林 ~ 2023-12-21 逝于马萨诸塞州列克星敦，享年 99 岁）
- **气质关键词**：**增长模型的奠基人、技术进步的测量者、MIT 四十年的温和理性**
- **诺奖获奖理由**（逐字引用）：
  > "for his contributions to the theory of economic growth"（表彰他对经济增长理论的贡献）
- **设计母题**：**稳态与余量（steady state & residual）**——产出曲线、折旧线与储蓄线三线交汇于稳态点，交点之外的余量属于技术进步，是「增长从何而来」的视觉隐喻：三线交汇图与一枚金色余量扇区构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Robert_Solow/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Robert_Solow/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_Solow_zh`、`VIDEO_NAME=Robert_Solow_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Solow 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economic growth | 经济增长理论 | 诺奖核心：Solow–Swan 模型 | 核心页 |
| 1 | macroeconomics | 宏观经济学 | infobox Discipline；资本理论、菲利普斯曲线 | 全篇 |
| 2 | growth accounting | 增长核算 | 1957：美国人均产出增长的五分之四归于技术进步 | 核算页 |
| 3 | capital theory | 资本理论 | 与 Samuelson 的资本论战、 vintage capital | 资本页 |
| 4 | econometrics | 计量经济学 | MIT 任教起点：统计学与计量课程 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wassily Leontief | Solow ← 导师 | 哈佛师承与研究助理，投入产出首套资本系数（库内规范记录） |
| collaborator | Paul Samuelson | 无向 | 近四十年合作：冯诺依曼增长 1953、资本理论 1956、线性规划 1958、菲利普斯曲线 1960 |
| collaborator | Robert Dorfman | 无向 | 1958 三人合著《线性规划与经济分析》 |
| colleague | Trevor W. Swan | 无向 | 1956 各自独立提出同一增长模型，后世并称 Solow–Swan |
| colleague | Franco Modigliani | 无向 | MIT 同事；其逝世后 Solow 接任 I.S.E.O 研究所主席 |
| advisor-student | George Akerlof | Solow → 学生 | 正文明载的四位诺奖弟子之一 |
| advisor-student | Joseph Stiglitz | Solow → 学生 | 正文明载的四位诺奖弟子之一 |
| advisor-student | Peter Diamond | Solow → 学生 | 正文明载的四位诺奖弟子之一 |
| advisor-student | William Nordhaus | Solow → 学生 | 正文明载的四位诺奖弟子之一 |
| spouse | Barbara Lewis | 无向 | 1945 年退伍后结婚（相恋六周），2014 妻先逝 |

**不入库但提示词可叙述**：infobox 三十余位博士生名单（防噪声只收正文点名的四位诺奖弟子；Rothschild/Halbert White/Charlie Bean/Woodford/Harvey Wagner 叙述）；Dale W. Jorgenson（对 vintage capital 的观测等价批评，学术商榷不建边）；Greenwood/Hercowitz/Krusell（后续推进者）；Romer 与小 Lucas（内生增长替代方案）；Cournot 基金会（机构不建边）。

## 五、配色方案 【人物专属】

- **气质**：清晰的三线图、新古典的平衡、跨越世纪的温和
- **主色**：`#7A1E28`（稳态绛——三线交汇点的深红重量感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGrowth` 增长理论 — 绛红 `#7A1E28`
  - `badgeAcc` 增长核算 — 靛蓝 `#2E3A59`
  - `badgeCap` 资本理论 — 琥珀 `#C07A2A`
  - `badgeMacro` 宏观经济 — 灰紫 `#52307C`
- **背景母题**：产出/折旧/储蓄三线交汇于稳态点、交点之外一扇金色余量扇区——「技术进步是增长的余量」的图形化。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 增长模型的奠基人 / Robert Solow 1924–2023 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地布鲁克林、教育哈佛 AB/AM/PhD、
    任职 MIT 1949 起 Institute Professor Emeritus、诺奖 1987、核心领域）
03  核心贡献概览 — Solow–Swan 模型 / 增长核算 / vintage capital / 菲利普斯曲线合作
04  布鲁克林与战地译电员 (1924–1945) — 16 岁奖学金进哈佛、社会学人类学起步、Signal Corps 德语情报、
    北非西西里意大利
05  哈佛师从列昂季耶夫 (1945–1949) — 投入产出首套资本系数、哥伦比亚统计年、Wells 奖不出版的博士论文
06  1956：增长的分水岭（核心贡献页）— QJE 论文、与 Trevor Swan 各自独立提出、外生储蓄率
07  1957：增长的余量（核心贡献页）— 增长核算、人均产出增长的五分之四归于技术进步
08  稳态图形的语言（核心贡献页）— 三线交汇图、稳态点左右的不同增长含义
09  与 Samuelson 的四十年 — 冯诺依曼增长、资本理论、线性规划、菲利普斯曲线四座里程碑
10  vintage capital 与后续 — 新旧资本、Jorgenson 之争、投资特异性技术进步、内生增长替代方案
11  门生满门 — 四位诺奖弟子 Akerlof/Stiglitz/Diamond/Nordhaus 与更长的名单
12  荣誉与认可 — Clark 奖章 1961、Nobel 1987、国家科学奖章 1999、总统自由勋章 2014、
    1979 AEA 主席、1964 计量经济学会主席
13  公共学者与晚晴 — CEA 与收入保障委员会、MDRC 共创、Cournot 基金会、I.S.E.O 接棒、99 岁辞世
14  遗产与结尾 — 从 Solow 残差到现代增长理论 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| Solow–Swan 命名 | 模型由 Trevor W. Swan **独立发现**并发表于 The Economic Record 1956——「各自独立、后世并称」，勿写成 Swan 发展了 Solow 的模型，也勿写成两人合作 |
| 获奖理由措辞 | 官方 citation 只说 "contributions to the theory of economic growth"——勿扩大为「因 Solow 模型获奖」的现成句式；1957 余量核算是模型之外另一贡献 |
| 五分之四口径 | Solow (1957) 计算的是「美国**人均产出**增长约五分之四归于技术进步」——勿写成总量或写错比例 |
| 四位诺奖弟子 | 正文点名 Akerlof/Stiglitz/Diamond/Nordhaus 四人后获诺奖；infobox 三十余人不入库防噪声，幻灯片可展示名单但注明「仅四人入库」 |
| 政治性表态 | 2018 哈佛招生案法庭之友、2022 支持《通胀削减法案》为 page.md 明载事实——**一句客观带过、零展开零评价**，或按版面删去 |
| 引语红线 | page.md 载英文原句 "Probably this is because I *hate* writing articles."（谈从未被退稿）——引原文+译文，勿把转述当原话 |
| Barbara Lewis | 退伍后与相恋六周的 Barbara Lewis 结婚（page.md 明载），妻 2014 去世；子女未具名不入库 |
| 双「主席」年份 | 1964 任计量经济学会主席、1979 任美国经济学会主席——两主席勿换位 |
| Clark 奖章口径 | 1961 年获 John Bates Clark Medal（40 岁以下最佳经济学家）——勿与诺奖年份 1987 混写 |
| 军旅细节 | 二战服役于陆军 Signal Corps 德语情报任务（北非/西西里/意大利），1945-08 退伍——勿写成海军（与 Buchanan 的海军区分） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Solow–Swan model | Solow–Swan 增长模型 | 两人独立提出，并称 |
| exogenous growth model | 外生增长模型 | 储蓄率外生给定 |
| steady state | 稳态 | 投资恰好抵补折旧之点 |
| Solow residual | Solow 余量 | 增长中无法由要素投入解释的部分 |
| growth accounting | 增长核算 | 1957 方法论贡献 |
| technical progress | 技术进步 | 获奖理由背后的事实主角 |
| vintage capital | 代次资本 | 新资本承载新技术 |
| production function | 生产函数 | 资本-劳动-技术三要素 |
| input-output model | 投入产出模型 | 师承 Leontief 的起点 |
| John Bates Clark Medal | 克拉克奖章 | 1961，40 岁以下经济学家奖 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Cinematic drone 的宏大纵深，恰如增长理论的主题——一个经济体数十年尺度的兴衰起伏，被 Solow 拆解成资本、劳动与技术三条线；曲名的史诗感也贴合这位横跨 99 年人生、亲历大萧条到数字时代、最终把「增长的来源」变成现代经济学常识的观察者。
- **本地路径**：复制 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` 到 `economics/presentations/20th_century/Robert_Solow/EmpireCollapse.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
