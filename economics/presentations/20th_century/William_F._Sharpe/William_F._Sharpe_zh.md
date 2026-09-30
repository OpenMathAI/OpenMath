# 经济学家立传提示词（William F. Sharpe）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1990 年得主 William F. Sharpe（威廉·夏普）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/William_F._Sharpe/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：William Forsyth Sharpe（1934-06-16 生于波士顿，**在世**）
- **气质关键词**：**CAPM 的缔造者之一、夏普比率的发明人、学术与硅谷的两栖者**
- **获奖理由**（1990 三人共享，逐字引用，中文翻译照抄总名录）：
  > "for their pioneering work in the theory of financial economics"
  > （表彰他们在金融经济学理论方面的开创性工作）
- **设计母题**：**证券市场线（security market line）**——CAPM 的几何化身：横轴 β（系统性风险）、纵轴期望收益，一条截距为无风险利率的直线，所有定价资产沿线上下分布。斜线 + 散点构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/William_F._Sharpe/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/William_F._Sharpe/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=William_F._Sharpe_zh`、`VIDEO_NAME=William_F._Sharpe_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Sharpe 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | 1990 诺奖理由核心词 | 封面、核心页 |
| 1 | asset pricing | 资产定价 | CAPM（1964）：期望收益=无风险利率+β 溢价 | 核心页 |
| 2 | portfolio management | 投资组合管理 | 组合配置、养老基金咨询、梯度法 | 贡献页 |
| 3 | performance measurement | 业绩衡量 | Sharpe ratio（1966/1994）、returns-based style analysis（1988） | 贡献页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Armen Alchian | Sharpe → 学生 | UCLA 博士导师、本科时代的 mentor |
| advisor-student | J. Fred Weston | Sharpe → 学生 | 金融学教授，首次引其读 Markowitz 组合理论论文 |
| advisor-student | Harry Markowitz | Sharpe → 学生 | 非正式导师（infobox 标 unofficial；RAND 共事"实践上近似博导"） |
| advisor-student | Howard Sosin | Sharpe → 学生 | 博士生（infobox Doctoral students 明载） |
| co-honored | Harry Markowitz | 无向 | 1990 诺贝尔经济学奖三人共享（金融经济学理论开创性工作） |
| co-honored | Merton Miller | 无向 | 1990 诺贝尔经济学奖三人共享（金融经济学理论开创性工作） |
| colleague | John Lintner | 无向 | CAPM 独立发展者之一 |
| colleague | Jan Mossin | 无向 | CAPM 独立发展者之一 |
| colleague | Jack Treynor | 无向 | CAPM 独立发展者之一 |
| colleague | Joseph Grundfest | 无向 | 1996 共同创立 Financial Engines（斯坦福同事） |
| colleague | Craig W. Johnson | 无向 | 1996 共同创立 Financial Engines（硅谷律师） |

**不入库但提示词可叙述**：Theta Xi / Phi Beta Kappa（学社）；Merrill Lynch / Wells Fargo / Frank Russell Company（咨询机构）；Markowitz 对 Sharpe 的 advisor 边系本篇所建（Markowitz 篇不再重复建，其篇仅 co-honored 边体现同届）；2024 年 16 位经济学诺奖得主联署公开信——**仅一句客观记录联署事实，不展开信件内容与政策立场**（政治敏感红线）。**relations=11 为 page.md 明载诚实值。**

## 五、配色方案 【人物专属】

- **气质**：明快、线性、风险与收益的定量美学
- **主色**：`#9E2B25`（砖红——manifest 预分配，1990 三人共享主色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCAPM` 资产定价 — 深蓝 `#1E3A5F`
  - `badgeRatio` 业绩衡量 — 灰紫 `#52307C`
  - `badgeStyle` 风格分析 — 深青 `#0E4D64`
  - `badgeVC` 创业与硅谷 — 琥珀 `#C07A2A`
- **背景母题**：证券市场线与 β 散点（无风险利率为截距、风险溢价为斜率），呼应「证券市场线」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — CAPM 的缔造者之一 / William F. Sharpe 1934– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生 1934-06-16 波士顿、教育 UCLA BA 1955/MA 1956/PhD 1961、
    任职华盛顿大学 1961–68 → UC Irvine → 斯坦福 1970 起、STANCO 25 教授 Emeritus、诺奖 1990、核心领域）
03  核心贡献概览 — CAPM / Sharpe ratio / 二叉树期权方法 / 风格分析
04  早年波士顿到 Riverside (1934–1951) — 父亲国民警卫队、战时数度迁居；Riverside Polytechnic 1951
05  UCLA 的两次转向 — Berkeley 医学预科→UCLA 商科→不喜会计转经济学；Alchian（mentor）与 Weston 两位教授
06  RAND 岁月与 Markowitz (1956–1961) — 1956 入 RAND；Weston 建议向 Markowitz 请教选题；
    Markowitz "实践上近似博导"（infobox 标 unofficial）
07  博士论文与单因子模型 (1961) — 证券价格单因子模型；证券市场线的早期版本
08  CAPM 的诞生与被拒 (1961–1964) — 华盛顿大学推广至均衡定价理论；1962 投稿 *Journal of Finance*
    被斥"无关"拒稿，编辑部换人后 1964 发表——按 page.md 客观叙述（"ironically"）
09  独立并行的三重发现 — Lintner / Mossin / Treynor 各自独立发展 CAPM——「各自独立」措辞勿写主从
10  Sharpe ratio 与业绩分析 — 1966 Mutual Fund Performance；1994 The Sharpe Ratio；二叉树方法；
    1988 'Determining a Fund's Effective Asset Mix' 与 returns-based style analysis
11  斯坦福与实务 (1970–1989) — 投资组合与养老基金研究；Merrill Lynch / Wells Fargo 咨询；
    1986 与 Frank Russell Company 创 Sharpe-Russell Research；1989 退休转顾问公司
12  Financial Engines (1996) — 与 Grundfest、Craig W. Johnson 共创；自动化退休投资咨询；
    2018 年 3 月被 30 亿美元现金收购
13  1990 诺贝尔奖 — 与 Harry Markowitz、Merton Miller 三人共享；获奖演讲 1990-12-07
    *Capital Asset Prices with and without Negative Holding*
14  遗产与结尾 — 从 CAPM 到日常投资实践（全球资管的定价底座）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1990 三人共享 | 与 Markowitz/Miller 共享同句理由——Sharpe 的工作（CAPM/Sharpe ratio）与另两人互不相同；本页 deck 三篇 BGM/主色均同（manifest 预分配） |
| 三位"导师" | Alchian 是正式博导（UCLA supervision）；Weston 是引路人（建议向 Markowitz 请教选题，infobox Doctoral advisor 行有载）；Markowitz 是**非正式**导师（infobox 明标 "(unofficial)"，正文引语 "filled a role similar to that of dissertation advisor"）——三条 advisor-student 边的 note 必须区分强弱，Markowitz 条禁写成正式导师 |
| CAPM 被拒发表 | 1962 投稿被拒、编辑部换人后 1964 发表——按 page.md 口径（含 "ironically"）客观叙述，勿演绎为学界打压叙事 |
| 独立发现 | CAPM 由 Sharpe / Lintner / Mossin / Treynor 各自独立发展——写「各自独立」，勿写谁先谁后主从（page.md 未排序） |
| 在世 | 1934-06-16 生，无卒日；留白三处一致（封面/身份页/结尾），勿补卒年 |
| CAPM 公式页 | E(Ri)=Rf+βi(E(Rm)−Rf) 各项含义按 page.md 列表转述；勿引入 page.md 未载的扩展公式 |
| 政治红线 | 2024 年 16 位经济学诺奖得主联署公开信——只写「联署」这一事实一句，不展开内容、立场与评价 |
| 机构 | RAND/U Washington 1961–68/UC Irvine 1968–70/Stanford 1970 起——任期年份勿混；Financial Engines 1996 共创、2018-03 被 3B 美元收购 |
| 学社不入库 | Theta Xi 联谊会、Phi Beta Kappa 学社仅叙述；DePaul/维也纳大学荣誉博士、UCLA Medal 只入荣誉页 |
| 博士生仅一人 | infobox Doctoral students 仅 Howard Sosin 一人——勿扩写 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| capital asset pricing model | 资本资产定价模型（CAPM） | 诺奖核心贡献 |
| security market line | 证券市场线 | CAPM 的几何表达 |
| Sharpe ratio | 夏普比率 | 风险调整后收益衡量 |
| beta (β) | 贝塔 | 系统性风险敏感度 |
| risk-free rate | 无风险利率 | 公式截距项 |
| systematic risk | 系统性风险 | β 对应的概念，勿与总风险混淆 |
| binomial method | 二叉树方法 | 期权估值贡献之一 |
| returns-based style analysis | 基于收益的风格分析 | 1988 论文确立的模型 |
| negative holding | 负持有 | 获奖演讲题目用词 |
| gradient method | 梯度法 | 资产配置优化的贡献 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，1990 三人共享曲目，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「自由之风」贴合 CAPM 把风险定价变成一条自由市场均衡直线的气质；与 Markowitz/Miller 两篇同曲同色形成同届三人组呼应。
- **本地路径**：复制 `music_audio/inspiring-electronic/25-l3Fsk4R6eys-...Winds Of Freedom.wav` 到 `economics/presentations/20th_century/William_F._Sharpe/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
