# 经济学家立传提示词（Harry Markowitz）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1990 年得主 Harry Markowitz（哈里·马科维茨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Harry_Markowitz/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Harry Max Markowitz（1927-08-24 生于芝加哥 ~ 2023-06-22 逝于加州圣地亚哥医院，享年 95 岁）
- **气质关键词**：**现代投资组合理论之父、均值-方差的几何学家、会写 SIMSCRIPT 的经济学家**
- **获奖理由**（1990 三人共享，逐字引用，中文翻译照抄总名录）：
  > "for their pioneering work in the theory of financial economics"
  > （表彰他们在金融经济学理论方面的开创性工作）
- **设计母题**：**有效前沿（efficient frontier）**——风险-收益平面上那条凹向原点的双曲线边界：每一个组合都是一点，理性选择只发生在边界上。散点云 + 弧形边界线构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Harry_Markowitz/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Harry_Markowitz/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Harry_Markowitz_zh`、`VIDEO_NAME=Harry_Markowitz_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Markowitz 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | 1990 诺奖理由核心词 | 封面、核心页 |
| 1 | portfolio theory | 投资组合理论 | 1952 *Portfolio Selection*、1959 专著、有效前沿 | 核心页 |
| 2 | operations research | 运筹学 | 1989 von Neumann Theory Prize 三领域之二：稀疏矩阵+模拟语言 | 贡献页 |
| 3 | optimization | 优化方法 | 临界线算法（critical line algorithm，1956） | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Milton Friedman | Markowitz → 学生 | 芝加哥大学博士导师（infobox/正文） |
| advisor-student | Jacob Marschak | Markowitz → 学生 | 论文导师（thesis advisor），鼓励选题 |
| influence | Tjalling Koopmans | 无向 | infobox Influences；求学时期的重要经济学家 |
| influence | Leonard Savage | 无向 | infobox Influences；求学时期的重要经济学家 |
| colleague | George Dantzig | 无向 | 1952 RAND 结识，在其帮助下发展临界线算法 |
| colleague | James Tobin | 无向 | 1955–56 应邀赴耶鲁 Cowles Foundation 一年 |
| colleague | Paul Samuelson | 无向 | 1968 起在 AMC 共创计算机化套利对冲基金 |
| colleague | Robert C. Merton | 无向 | 1968 起在 AMC 共创计算机化套利对冲基金（经济学家 Robert C. Merton） |
| colleague | Michael Goodkin | 无向 | 1968 加入其创办的 Arbitrage Management 公司 |
| colleague | Herb Karr | 无向 | 1962-07-17 共同创立 California Analysis Center（后为 CACI） |
| collaborator | Frank J. Fabozzi | 无向 | 合编教科书 *The Theory and Practice of Investment Management* |
| co-honored | Merton Miller | 无向 | 1990 诺贝尔经济学奖三人共享（金融经济学理论开创性工作） |
| co-honored | William F. Sharpe | 无向 | 1990 诺贝尔经济学奖三人共享（金融经济学理论开创性工作） |

**不入库但提示词可叙述**：Alfred Cowles（选题背景叙述）；John Burr Williams（现值模型对照）；Sharpe 对 Markowitz 的 advisor-student 边归属 Sharpe 篇（本篇以 co-honored 体现同届，infobox 标注 unofficial 的师承表述见 Sharpe 篇）。**relations=13 为 page.md 明载诚实值。**

## 五、配色方案 【人物专属】

- **气质**：理性、几何、风险与收益的平衡
- **主色**：`#9E2B25`（砖红——manifest 预分配，1990 三人共享主色；对应风险警示与华尔街的暖色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePort` 组合理论 — 深蓝 `#1E3A5F`
  - `badgeOR` 运筹与优化 — 灰紫 `#52307C`
  - `badgeSim` 模拟语言 SIMSCRIPT — 深青 `#0E4D64`
  - `badgeBiz` 创业与实务 — 琥珀 `#C07A2A`
- **背景母题**：风险-收益平面上的散点云与有效前沿弧线（每个点是一个组合，边界线是理性选择的极限），呼应「有效前沿」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 现代投资组合理论之父 / Harry Markowitz 1927–2023 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地芝加哥、教育芝加哥大学 PhB/MA/PhD、
    任职 UCSD Rady 商学院/Baruch College/RAND/Cowles、诺奖 1990、von Neumann Prize 1989、核心领域）
03  核心贡献概览 — 组合选择 / 有效前沿 / 临界线算法 / 稀疏矩阵与 SIMSCRIPT
04  芝加哥早年 (1927–1950) — 犹太家庭；中学迷上 Hume 与物理哲学；PhB 1950、MA 1950
05  Cowles 与选题 — Friedman/Koopmans/Marschak/Savage 门下；Marschak 鼓励股票市场选题；
    Williams 现值模型缺风险分析的关键洞察
06  1952：Portfolio Selection（核心贡献页）— *Journal of Finance* 1952-03；
    风险/收益/相关性/分散化的组合理论
07  RAND 与 Dantzig：临界线算法 — 1956 发表；Markowitz frontier；1959 专著
    *Portfolio Selection: Efficient Diversification of Investments*
08  答辩风波 (1954) — Friedman 在答辩中主张"这不是经济学"；PhD 照常授予——按 page.md 客观叙述
09  运筹学三领域 (1989 von Neumann Prize) — 组合理论 / 稀疏矩阵方法 / 模拟语言 SIMSCRIPT；
    Buddy 内存分配法亦出其手
10  创业岁月 — 1962 与 Herb Karr 共创 CACI；1968 加入 Goodkin 的 AMC，
    与 Samuelson、Robert C. Merton 共创计算机化套利对冲基金，1970 任 CEO，1971 售出
11  组合理论的完成 — Markowitz-efficient portfolio 与有效前沿的定义；
    这些效率概念是 CAPM 发展的重要基础
12  1990 诺贝尔奖 — 与 Merton Miller、William F. Sharpe 三人共享；时任 Baruch College 金融教授
13  晚年与传承 — UCSD Rady 兼职教授；2018 捐诺奖奖章与证书给 Geisel Library；2023-06-22
    因肺炎与败血症并发症辞世
14  遗产与结尾 — 从均值-方差到现代资产管理的日常实践 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1990 三人共享 | Markowitz/Miller/Sharpe 三人共享同句理由 "for their pioneering work in the theory of financial economics"——三人工作各不相同（组合理论/公司金融/CAPM），勿写成分工或拆分理由；本页 deck 三篇 BGM/主色均同（manifest 预分配） |
| 双博士导师 | 博士导师两位：Milton Friedman（infobox Doctoral advisor + 正文 "study under"）与 Jacob Marschak（正文 "who was the thesis advisor"）——两人都建 advisor-student，勿只写其一 |
| 答辩轶事 | Friedman 在答辩中论证其贡献"不是经济学"——按 page.md 客观叙述，勿演绎成两人交恶 |
| Robert C. Merton 消歧义 | 对手方是经济学家 **Robert C. Merton**（1997 诺奖得主），不是社会学家 Robert K. Merton |
| Koopmans/Savage 定性 | 两人是 infobox Influences + 正文求学时期经济学家——建 influence 而非 advisor-student（无导师明载） |
| von Neumann Prize | 1989 年由 ORSA（今 INFORMS）授予，获奖理由=三领域（组合理论/稀疏矩阵/SIMSCRIPT）——勿与 1990 诺奖混淆、勿提前写"1989 诺奖" |
| SIMSCRIPT 细节 | 首个模拟编程语言之一；SIMSCRIPT (I) 含 Buddy memory allocation；CACI 1962-07-17 与 Herb Karr 共创——年份勿混 |
| 生卒 | 1927-08-24 芝加哥 ~ 2023-06-22 圣地亚哥医院（肺炎与败血症并发症），享年 95；frontmatter 单值无冲突 |
| 捐奖章 | 2018 捐诺奖奖章与证书给 UCSD Geisel Library（"love for the campus"）——与 2023 卒分开叙述 |
| Sharpe 师承归属 | Markowitz 是 Sharpe 的**非正式**导师（RAND 共事、"filled a role similar to that of dissertation advisor"）——该 advisor-student 边由 Sharpe 篇建（其页面 infobox 明载 unofficial），本篇不再重复建边 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| modern portfolio theory | 现代投资组合理论 | 诺奖核心贡献 |
| efficient frontier | 有效前沿 | 每一风险水平的最高期望收益组合集 |
| mean-variance | 均值-方差 | 框架的两要素 |
| critical line algorithm | 临界线算法 | 1956 发表的优化算法 |
| diversification | 分散化 | 风险管理的核心机制 |
| sparse matrix methods | 稀疏矩阵方法 | von Neumann Prize 三领域之一 |
| SIMSCRIPT | SIMSCRIPT 模拟语言 | 首个模拟编程语言之一 |
| capital asset pricing model | 资本资产定价模型（CAPM） | Markowitz 效率概念是其发展基础；CAPM 本体系 Sharpe 等人工作 |
| John von Neumann Theory Prize | 冯·诺伊曼理论奖 | 1989 运筹学奖，勿与诺奖混 |
| present value model | 现值模型 | John Burr Williams 的旧范式，Markowitz 的出发点 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，1990 三人共享曲目，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「自由之风」贴合金融经济学把投资者从旧范式（只看收益不看风险）中解放出来的开创性；史诗感配乐亦呼应组合理论从论文到全球资产管理实践的宏大落点。
- **本地路径**：复制 `music_audio/inspiring-electronic/25-l3Fsk4R6eys-...Winds Of Freedom.wav` 到 `economics/presentations/20th_century/Harry_Markowitz/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
