# 经济学家立传提示词（William Nordhaus）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2018 年得主 William Nordhaus（威廉·诺德豪斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/William_Nordhaus/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：William Dawbney Nordhaus（1941-05-31 生于美国新墨西哥州阿尔伯克基，在世，卒年留白）
- **气质关键词**：**气候经济学的开山者、DICE 模型的缔造者、把自然写进国民账本的人**
- **诺奖获奖理由**（2018 与 Paul Romer 共享但**理由句各一**，逐字引自 `economics/nobel_economics_citations.json` 2018 William Nordhaus 条目）：
  > "for integrating climate change into long-run macroeconomic analysis"
  > （表彰他将气候变化纳入长期宏观经济分析）
  > Romer 那一条是 "for integrating technological innovations into long-run macroeconomic analysis"——两句勿互串。
- **设计母题**：**经济与气候的耦合演化（co-evolution of economy & climate）**——碳流与资本流在同一张图上相互缠绕；以温度曲线与增长曲线交织的网格构成背景母题，隐喻"一体化评估模型"（IAM）。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/William_Nordhaus/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/William_Nordhaus/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=William_Nordhaus_zh`、`VIDEO_NAME=William_Nordhaus_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Nordhaus 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | environmental economics | 环境经济学 | infobox Fields 明载；2018 诺奖核心 | 封面、核心页 |
| 1 | climate change economics | 气候变化经济学 | DICE/RICE 一体化评估模型 | 核心页 |
| 2 | integrated assessment modelling | 一体化评估建模 | 经济-能源-气候交互的定量模型 | 核心页 |
| 3 | macroeconomics | 宏观经济学 | 长期宏观分析框架 | 理论页 |
| 4 | national income accounting | 国民收入核算 | 对 GDP/物价指数的批评与 MEW 尝试 | 核算页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 5 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Solow | Solow → 导师 | MIT 博士导师（1967），1987 诺奖得主 |
| co-honored | Paul M. Romer | 无向 | 2018 诺贝尔经济学奖共享（理由句各一：气候变化/技术创新） |
| collaborator | Paul Samuelson | 无向 | 合著经典教科书 Economics（1985 起自第 12 版至第 19 版） |
| colleague | James Tobin | 无向 | 耶鲁同事；1972 合著 Is Growth Obsolete? 提出 MEW 环境核算 |
| collaborator | Joseph Boyer | 无向 | 合著 Warming the World: Economic Models of Global Warming（2000） |

**不入库但提示词可叙述**：妻 Barbara（page.md 仅名无姓氏，不入库）；父 Robert J. Nordhaus（Sandia Peak Tramway 共同创办人，父职仅家世叙述、按"叙述性家世不入库"裁定不建边——与 Romer 父职"州长"明载密度不同，此处 page.md 仅一句提及）；祖父 Max Nordhaus（1883 自帕德博恩移民，隔代不入）；批评者 Cline / Pindyck / Stern / Weitzman / Steve Keen（对 DICE 模型的学术批评，属模型争论非两人持续关系，不入库、正文可并列转述）；George P. Shultz 与 William A. Brock（同届 AEA Distinguished Fellow，非关系）；Freeman Dyson（NYRB 交锋，外部链接叙述）。

## 五、配色方案 【人物专属】

- **气质**：绿色、长远、科学与经济学的交汇
- **主色**：`#2E5339`（气候森林绿——manifest 缺省（null），本批次裁定补配 `#2E5339`，与 econ21th 全表无撞色；森林绿直接呼应气候经济学与 The Spirit of Green）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeClimate` 气候经济学 — 森林绿 `#2E5339`
  - `badgeDICE` DICE/RICE 模型 — 湖蓝 `#1B4D6B`
  - `badgeAccount` 国民核算批判 — 琥珀 `#C07A2A`
  - `badgeTextbook` 教科书传承 — 靛蓝 `#37474F`
- **背景母题**：温度曲线与增长曲线交织的网格（经济-气候耦合相空间），呼应「用一体化模型模拟经济与气候的共同演化」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 气候经济学的开山者 / William Nordhaus 1941– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地阿尔伯克基、教育 Yale BA 1963 / MA 1972 /
    Sciences Po 证书 1962 / MIT PhD 1967、师承 Robert Solow、任职 Yale、诺奖 2018、核心领域）
03  核心贡献概览 — 国民核算批判（MEW）/ DICE-RICE 模型 / 气候俱乐部 / 碳税
04  家世与早年 (1941–1963) — 阿尔伯克基出生、父为 Sandia Peak Tramway 共同创办人、德裔犹太家世、
    Phillips Academy Andover、Sciences Po 1962、Yale BA 1963（Skull and Bones 会员叙述）
05  MIT 博士：Solow 门下 (1963–1967) — 论文 A theory of endogenous technological change；
    1970–71 Clare Hall（剑桥）访问研究员
06  耶鲁岁月 (1967– ) — 经济系与环境学院双聘、教务长 1986–88、主管财务与行政副校长 1992–93、
    Brookings Panel 1972 起成员
07  国民核算的批判与重构（核心贡献页）— 1996 物价指数之问（马与汽车、Pony Express 与传真机的
    跨时代比价难题）；1972 与 Tobin 合著 Is Growth Obsolete?：MEW/ISEW 首次环境核算尝试
08  DICE 与 RICE：给气候定价的模型（核心贡献页）— 经济-能源-气候一体化评估模型；
    「人类正在与自然环境掷骰子」（1993 Reflections 引语，page.md 原文）
09  气候政策的争论 — 2007 批评 Stern Review 的低贴现率（引语原文）；2013 主持 NRC 化石燃料
    补贴报告；2015 气候俱乐部（climate club）：碳定价+边境费，2025 Econometrica 论文的 33–68% 检验
10  教科书经济学 — 与 Samuelson 合著 Economics 教科书（1985 起第 12 至 19 版）：
    1948 初版、19 版、17 种语言、数十年畅销与「canonical textbook」地位
11  公共服务与学界领导 — Carter 任内 CEA 委员 1977–79（客观一句）；Fed Boston 董事会主席
    2014–15；AEA Distinguished Fellow 2004 / 会长 2014–15；NAS、美国哲学会、AAAS 各院
12  诺贝尔奖 — 2018 与 Romer 共享但理由句各一（climate change / technological innovations）；
    瑞典科学院评语（integrated assessment model 原文）；诺奖演讲 Climate Change: The Ultimate
    Challenge for Economics
13  争论与评价 — 批评者并列（贴现率/模型复杂度/损失函数/肥尾四条）；部分气候学者对其低碳税
    立场失望；2020 NZZ 访谈称 2°C 目标 "impossible"（引语原文）；BBVA Frontiers 2017、
    Moynihan Prize 2020
14  遗产与结尾 — 从《绿色精神》到碳定价的全球实践 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由各一 | 2018 是"拆分理由"年份：Nordhaus 一句 climate change、Romer 一句 technological innovations；两篇各忠于本人 citation，勿互串、勿合写 |
| 配色裁定 | manifest main_color=null，本批补配 #2E5339（Romer 补配 #1B4D6B），已核对 econ21th 全表无撞色 |
| 生平职务密度 | CEA 委员（Carter 任内 1977–79）与 Fed Boston 董事会主席是 page.md 明载事实，客观一句即可；Skull and Bones 仅作教育段叙述、不渲染 |
| 妻子不入库 | 妻仅名 Barbara（Yale Child Study Center 退休社工），无姓氏不入库 |
| 父职不入库 | 父 Robert J. Nordhaus 仅一句家世叙述（与 Romer 篇父职"前州长"不同），按叙述性家世不建 parent-child 边 |
| Stern Review 引语 | 2007 批评引语为 page.md 英文原文（"The Review's unambiguous conclusions...will not survive the substitution of discounting assumptions..."），引用须原文+译文；勿概括为中文"原话" |
| DICE 引语 | 1993 "Mankind is playing dice with the natural environment..." 是 page.md 明载原文（模型名 DICE 的双关），可入引文框 |
| 批评者不建边 | Cline/Pindyck/Stern/Weitzman/Keen 的批评是对模型的学术争论——正文并列转述、不入库任何关系；Keen 的尖锐措辞（"misrepresented"等）须以「Keen 认为」转述、不照录整段 |
| 2°C 争议 | 2020 NZZ "impossible" 判断是 Nordhaus 本人立场（自称半数模拟支持），客观呈现其说法与争议背景，勿写成学界共识 |
| Samuelson 教科书 | Economics 教科书 1948 年初版是 Samuelson 独著项目，Nordhaus 自 1985 年第 12 版起加入至第 19 版——勿写成"共同创作于 1948" |
| carbon tax 叙事 | 早期支持碳税的"第一波经济学家"是媒体报道口径（page.md 明载）；部分气候学者对其低碳税额失望也是明载事实——两说并列，不评价 |
| metadata 噪声 | metadata.json 与 page.md 无实质冲突；frontmatter doctoral_advisor 与 infobox 一致（Robert Solow） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| integrated assessment model | 一体化评估模型（IAM） | 获奖核心，勿译"综合评估"泛化 |
| DICE / RICE | 气候-经济动态模型（区域版 RICE） | 模型名双关 "playing dice"，保持缩写 |
| carbon tax | 碳税 | 叙事主线，客观呈现 |
| discount rate | 贴现率 | Stern 争论焦点 |
| climate club | 气候俱乐部 | 2015 概念，勿写成"气候联盟" |
| Measure of Economic Welfare | 经济福利度量（MEW） | 1972 与 Tobin 合创 |
| environmental accounting | 环境核算 | MEW 的学科定位 |
| political business cycle | 政治经济周期 | AEA 授予词提及其开创工作 |
| Sterling Professor | 斯特林讲席教授 | 耶鲁最高教席（frontmatter award_received 有载） |
| social cost of carbon | （页内隐含） | 若正文未载该词组则不用，防越界 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：曲名的紧张感对应气候叙事的"临界压力"——DICE 模型处理的正是灾难性风险与贴现的世纪之争；"掷骰子"的双关与断裂式配乐相互呼应，而争论之后仍在建构（气候俱乐部、碳定价）的韧性构成第二主题。与 Romer 篇同曲，呼应 2018 共享得主的双人叙事。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/21th_century/William_Nordhaus/FallingApart.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/William_Nordhaus/page.md` | ★ 唯一事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一首页模板 |
| `MySQL/data/William_Nordhaus.yaml` | 入库 yaml（已执行） |
| `economics/nobel_economics_citations.json` | 获奖理由英文原文（2018 拆分两条） |

## 十一、执行清单 【模板通用】

1. 读本提示词 + page.md 建立事实基准；2. 下载肖像（250px 改 500px，Commons 404 则装饰圆占位）；3. 复制 Makefile 设 `MAIN=William_Nordhaus_zh`；4. 按 §六写 15 页 Beamer；5. `make distclean && make` 编译循环（0 error、vbox≤10pt、hbox≤50pt）；6. pdftoppm 逐页目检；7. 两轮 Review；8. DB `has_biography` 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 -0.35cm、arraystretch 0.78-0.82；公式框前 -0.35~-0.55cm。
- 时间线 `\foreach` 分隔符必须 ASCII 逗号；文本模式希腊字母须数学模式；宏名禁数字。
- 引语框：英文原文+译文（Stern Review 批评、DICE 双关句、NZZ 访谈均为 page.md 明载原文）；半角引号；品牌口径 `OpenMathAI`。
