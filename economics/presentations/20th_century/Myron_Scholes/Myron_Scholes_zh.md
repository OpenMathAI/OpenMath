# 经济学家立传提示词（Myron Scholes）

> 本文件是 OpenMathAI OpenEcon 项目 20 世纪诺贝尔经济学奖 **1997 年得主 Myron Scholes（迈伦·斯科尔斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Myron_Scholes/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Myron Samuel Scholes（1941-07-01 生于加拿大安大略省蒂明斯，在世）
- **气质关键词**：**期权定价的破译者、动态对冲的发明人、从学界到华尔街的跨界者**
- **诺奖获奖理由**（1997 与 Robert C. Merton 共享，逐字引用）：
  > "for a new method to determine the value of derivatives"（表彰他们提出了确定衍生品价值的新方法）
  - 瑞典皇家科学院指出：他们的工作使以科学方式观察期权价值成为可能，为全球金融市场的高速发展与经济风险管理奠定了基础（page.md 明载）。
- **设计母题**：**动态对冲与风险消除（dynamic hedging）**——连续时间市场中期权与股票之间的无风险对冲，使股票预期收益从定价方程中消失（风险中性），视觉隐喻：钟形分布曲线与反向箭头相互抵消的对称构图。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Myron_Scholes/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Myron_Scholes/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Myron_Scholes_zh`、`VIDEO_NAME=Myron_Scholes_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Scholes 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | infobox Discipline；芝加哥学派 | 封面、核心页 |
| 1 | option pricing | 期权定价 | Black–Scholes 公式，诺奖核心 | 核心页 |
| 2 | risk management | 风险管理 | 动态对冲与"希腊字母"敏感性体系 | 核心页 |
| 3 | tax planning | 税务筹划 | Scholes–Wolfson 框架（1992） | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 11 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eugene Fama | Fama → Scholes | 芝加哥大学博士导师之一（1969 论文共同指导） |
| advisor-student | Merton Miller | Miller → Scholes | 芝加哥大学博士导师之一 |
| influence | George Stigler | 无向 | McMaster 教授引其接触 Stigler 著作 |
| influence | Milton Friedman | 无向 | McMaster 教授引其接触 Friedman 著作 |
| colleague | Fischer Black | 无向 | MIT 时期相识，期权定价模型共同提出者 |
| colleague | Robert C. Merton | 无向 | MIT 同事；期权定价研究三人组；后同创 LTCM |
| colleague | Michael Jensen | 无向 | 芝加哥读研同侪；此后持续合作 |
| colleague | Richard Roll | 无向 | 芝加哥读研同侪 |
| colleague | John Meriwether | 无向 | 1994 与包括 Meriwether 在内的同侪共同创办 LTCM |
| collaborator | Mark A. Wolfson | 无向 | Scholes–Wolfson 税务筹划框架（1992）合著者 |
| co-honored | Robert C. Merton | 无向 | 1997 诺贝尔经济学奖共享（确定衍生品价值的新方法） |

**不入库但提示词可叙述**：_uncles 的生意启蒙（亲属无具名关系）；Janus Henderson / Platinum Grove / Dimensional 等任职机构（机构不建人物边）；LTCM 其他合伙人。

## 五、配色方案 【人物专属】

- **气质**：冷峻、定量、芝加哥学派的理性锋利
- **主色**：`#123C5B`（manifest 预分配——深海军蓝，定价公式的冰感与金融深水区）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeOpt` 期权定价 — 深蓝 `#123C5B`
  - `badgeHedge` 动态对冲 — 青绿 `#0E7C7B`
  - `badgeTax` 税务筹划 — 琥珀 `#C07A2A`
  - `badgeMkt` 华尔街实践 — 玫瑰 `#C4204F`
- **背景母题**：钟形曲线与反向对冲箭头（风险被逐段消除的抽象），呼应"风险中性"的核心洞见。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 期权定价的破译者 / Myron Scholes 1941– + 四色 badge + 右上头像 + 国籍行（Canada–USA）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地蒂明斯、McMaster BA 1962、
    芝加哥 MBA 1964/PhD 1969、导师 Fama & Miller、任职 MIT/芝加哥/斯坦福、诺奖 1997）
03  核心贡献概览 — 期权定价公式 / 动态对冲 / 希腊字母 / 税务筹划
04  早年：蒂明斯与汉密尔顿 (1941–1962) — 大萧条迁居、视力障碍至 26 岁手术、高中开户炒股
05  McMaster 与芝加哥之门 (1962–1964) — 母亲病逝留汉密尔顿读本科；教授引读 Stigler/Friedman
06  芝加哥博士：Fama 与 Miller 门下 (1964–1969) — 金融经济学新领域、MBA 1964、PhD 1969
07  MIT 岁月：三人组成形 (1968–1973) — 遇 Black（Arthur D. Little 顾问）、Merton 1970 加入
08  期权定价公式（核心贡献页）— 1973 论文；无风险对冲使预期收益消失、 replaced by 无风险利率
09  Black–Scholes 公式与"希腊字母" — Delta/Gamma/Vega/Theta/Rho 敏感性体系
10  从公司债到信用风险 — 把公司股权视为总资产上的期权，系统性为公司债定价
11  Scholes–Wolfson 框架 (1992) — All Taxes / All Parties / All Costs 三支柱
12  华尔街与 LTCM (1990–1998) — Salomon Brothers；1994 与 Meriwether/Merton 共创 LTCM；
    40% 年化 → 1998 四个月亏 46 亿美元崩溃
13  荣誉与晚年 — 诺奖 1997（与 Merton 共享）、Econometric Society Fellow、斯坦福讲席教授荣休、
    Janus Henderson 首席投资策略师
14  遗产与结尾 — 衍生品市场的科学基础 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 博士导师有两位 | frontmatter `doctoral_advisor` 只列 Merton Miller，但 infobox 与正文明载论文由 **Eugene Fama 与 Merton Miller 共同指导**；以正文为准，两位都入库 |
| 国籍口径 | 正文 Canadian–American economist；nationalities 按 manifest 拆 Canada + United States 两条 |
| 模型命名 | Scholes 页作 **Black–Scholes**，Merton 页作 **Black–Scholes–Merton**；本篇忠于本人页面，勿擅自改写对方篇目口径 |
| 获奖与 LTCM 的时序 | 1994 共创 LTCM、1997 获诺奖、**1998 年**基金在亚洲/俄罗斯危机后四个月亏损 46 亿美元崩溃；勿写成"因 LTCM 获奖或因获奖而崩溃" |
| Fischer Black | page.md 未载其卒年与未获奖缘由，**禁写**（无载禁写）；只写 MIT 相识与 1973 论文合作 |
| 全文无直接引语 | page.md 无英文原话引语，中文引号内禁写"原话"；获奖理由为官方 citation 可逐字引 |
| 税务诉讼 | 2005 *Long-Term Capital Holdings v. United States*：法院驳回 4000 万美元税收主张（1.06 亿美元为无经济实质的形式亏损）——客观陈述，勿加道德评价 |
| 视力障碍 | "fighting with his impaired vision……finally getting an operation when he was twenty-six"——勿写成失明 |
| Jensen/Roll 关系 | 正文原话 "Scholes was a colleague with Michael Jensen and Richard Roll"（芝加哥读研同侪），勿升级为合著者 |
| LTCM 规模数字 | 起点 10 亿美元投资者资本、年化收益超 40%、1998 亏损 46 亿——三个数字勿混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Black–Scholes model | Black–Scholes 模型 | 期权定价模型，本篇命名口径（勿混 Black–Scholes–Merton） |
| derivative | 衍生品 | 获奖理由核心词 |
| dynamic hedging | 动态对冲 | 连续时间市场中消除风险的手段 |
| risk-neutral | 风险中性 | 预期收益被无风险利率替代后的定价视角 |
| strike price | 行权价 K | 公式变量 |
| volatility | 波动率 σ | 公式变量；"希腊字母" Vega 的对象 |
| Greeks | 希腊字母 | Delta/Gamma/Vega/Theta/Rho 五敏感性 |
| call option | 看涨期权 | 公式 C 的对象 |
| Scholes–Wolfson Framework | Scholes–Wolfson 框架 | 1992 税务筹划三支柱 |
| Chicago school of economics | 芝加哥学派 | infobox School or tradition |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Black–Scholes 公式 1973 年发表至今仍是全球衍生品市场的基础设施——"超越时间的"恰合其方法论的生命力；沉稳的节奏也贴合定量金融的冷峻气质与"学界—华尔街"的跨县长弧线。
- **本地路径**：复制 `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` 到 `economics/presentations/20th_century/Myron_Scholes/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
