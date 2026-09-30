# 经济学家立传提示词（Robert C. Merton）

> 本文件是 OpenMathAI OpenEcon 项目 20 世纪诺贝尔经济学奖 **1997 年得主 Robert C. Merton（罗伯特·默顿）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Robert_C._Merton/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert Cox Merton（1944-07-31 生于纽约市，在世）
- **气质关键词**：**连续时间金融的奠基人、期权定价的第一个连续时间模型、社会学世家走出的金融工程师**
- **诺奖获奖理由**（1997 与 Myron Scholes 共享，逐字引用）：
  > "for a new method to determine the value of derivatives"（表彰他们提出了确定衍生品价值的新方法）
- **设计母题**：**连续时间（continuous time）**——把离散的定价问题延展成连续曲线，视觉隐喻：密集的连续时间轴上漂移的资产路径（几何布朗运动的抽象），与 Scholes 篇的"钟形曲线对冲"形成姊妹篇。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Robert_C._Merton/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Robert_C._Merton/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_C._Merton_zh`、`VIDEO_NAME=Robert_C._Merton_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Merton 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | finance | 金融学 | infobox Fields 首位；连续时间金融 | 封面、核心页 |
| 1 | continuous-time finance | 连续时间金融 | 首个连续时间期权定价模型 | 核心页 |
| 2 | asset pricing | 资产定价 | 跨期资产组合选择、ICAPM | 核心页 |
| 3 | option pricing | 期权定价 | Black–Scholes–Merton 模型 | 核心页 |
| 4 | systemic risk | 系统性风险 | 当前研究：宏观金融风险测度 | 晚近页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 11 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul Samuelson | Samuelson → Merton | MIT 经济学博士导师（1970） |
| advisor-student | Jonathan E. Ingersoll | Merton → 学生 | infobox Doctoral students 明载 |
| advisor-student | Robert Jarrow | Merton → 学生 | infobox Doctoral students 明载 |
| parent-child | Robert K. Merton | 父 → Merton | 社会学家 |
| spouse | June Rose | 无向 | 1966 结婚，1996 分居，育二子一女 |
| colleague | Harry Markowitz | 无向 | 1968 年经导师 Samuelson 介绍进入 AMC（首家计算机化套利交易对冲基金），Markowitz 任 CEO |
| colleague | Michael Goodkin | 无向 | AMC 创始人 |
| colleague | Myron Scholes | 无向 | MIT 同侪；1993 共同创办 LTCM |
| co-honored | Myron Scholes | 无向 | 1997 诺贝尔经济学奖共享（确定衍生品价值的新方法） |

（注：Merton–Scholes 为 colleague + co-honored 双边，合计 9 个对手方 11 条中的 2 条重复计入，实际入库 11 行含双边两行。）

**不入库但提示词可叙述**：母 Suzanne Carhart（page.md 只述其出身，非学术关系）；三个子女（仅"two sons and one daughter"，无具名不入库）；LTCM 十四家银行救助团（机构不建人物边）；*Annual Review of Financial Economics* 创刊共同主编（期刊无人物边）。

## 五、配色方案 【人物专属】

- **气质**：连续、精密、学院与市场双重身份
- **主色**：`#123C5B`（manifest 预分配——与 Scholes 篇同色，1997 双子星共享主色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCT` 连续时间金融 — 靛蓝 `#372A75`
  - `badgeOpt` 期权定价 — 深蓝 `#123C5B`
  - `badgeRisk` 系统性风险 — 青绿 `#0E7C7B`
  - `badgeFam` 家学渊源 — 琥珀 `#C07A2A`
- **背景母题**：连续时间轴与漂移路径（几何布朗运动抽象），呼应"把离散定价延展为连续模型"的核心贡献。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 连续时间金融奠基人 / Robert C. Merton 1944– + 四色 badge + 右上头像 + 国籍行（USA）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽约 Hastings-on-Hudson 成长、
    哥伦比亚工程数学 BS、Caltech MS、MIT 经济学 PhD 1970、导师 Samuelson、诺奖 1997）
03  核心贡献概览 — 连续时间期权定价 / 跨期组合选择 ICAPM / 公司债定价 / 系统性风险
04  社会学世家 (1944–1966) — 父 Robert K. Merton、Hastings-on-Hudson 童年
05  工程数学到经济学 — 哥伦比亚 BS、Caltech MS、转向 MIT 经济学
06  Samuelson 门下 (1966–1970) — 1968 AMC 首个计算机化套利对冲基金经历
07  MIT 斯隆学院 (1970–1988) — 与 Scholes/Black 的期权定价研究
08  连续时间期权定价（核心贡献页）— Black–Scholes–Merton 模型、1973 Theory of Rational Option Pricing
09  跨期金融 — Merton's portfolio problem、ICAPM、*Continuous-Time Finance*
10  哈佛岁月与荣衔 (1988–2010) — George Fisher Baker 教席、McArthur 大学教授、2010 荣休；
    2010 重返 MIT Sloan
11  LTCM 的教训 (1993–2000) — 共同创办、1998 亏损 46 亿、14 家银行 36 亿救助、2000 清盘
12  荣誉与认可 — 诺奖 1997（与 Scholes）、美国 Finance Association 主席 1986、NAS 1993、
    Kolmogorov 奖章 2010 等精选
13  晚近研究 — 生命周期投资与退休融资、宏观金融系统性风险、金融创新与机构变迁
14  遗产与结尾 — 衍生品定价的连续时间范式 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生年口径 | page.md 正文 1944-07-31；External links 的 econlib 条目作 "(1945– )"——以正文 infobox 与首段 1944 为准 |
| 模型命名 | Merton 页作 **Black–Scholes–Merton**，Scholes 页作 **Black–Scholes**；本篇忠于本人页面；Fischer Black 在本页仅以模型名出现，无互动叙述，**不建边** |
| 与 Scholes 的双边 | colleague（MIT 同侪 + LTCM 共同创办）与 co-honored（1997 共享）两条并存，勿合并成一条 |
| AMC 时间线 | 1968 年经 Samuelson 介绍加入 Arbitrage Management Company；1971 售予 Stuart & Co.；LTCM 是 **1993** 年共同创办的另一只基金，两个基金勿混 |
| LTCM 数字 | 起初四年高回报、1998 亏 46 亿、14 家银行 36 亿美元救助、2000 年初清盘——与 Scholes 篇口径一致 |
| 国籍 | 美国；born in New York City |
| 全文无直接引语 | page.md 无英文原话引语，中文引号内禁写"原话"；获奖理由为官方 citation 可逐字引 |
| 荣誉取舍 | 荣誉清单 20 余条，幻灯片只精选 Nobel/1986 AFA 主席/1993 NAS/Kolmogorov 奖章等 4-5 条防溢出 |
| 2021 在职 | "He remained on the faculty at MIT in 2021"——在世，生卒页留白卒年 |
| 子女 | 三名子女无具名，不入库 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| continuous-time finance | 连续时间金融 | Merton 的标志性贡献框架 |
| Black–Scholes–Merton model | BSM 模型 | 本篇命名口径（三姓氏全） |
| ICAPM | 跨期资本资产定价模型 | Intertemporal CAPM |
| Merton's portfolio problem | 默顿组合问题 | 跨期最优组合选择 |
| Merton model | 默顿模型 | 把公司股权视为资产期权的信用风险模型 |
| derivative securities | 衍生证券 | 获奖理由核心词 |
| lifecycle investing | 生命周期投资 | 晚近研究方向 |
| systemic risk | 系统性风险 | 宏观金融研究主题 |
| option pricing | 期权定价 | 与 Scholes 共享的核心领域 |
| warrant | 认股权证 | 早期期权类工具语境 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，与 Scholes 篇同曲——1997 双子星共享 BGM 设计）
- **匹配理由**：与 Scholes 篇构成"同届同曲"的姊妹篇；"超越时间的"呼应连续时间金融把瞬时定价延展为永恒框架的贡献。
- **本地路径**：复制 `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` 到 `economics/presentations/20th_century/Robert_C._Merton/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
