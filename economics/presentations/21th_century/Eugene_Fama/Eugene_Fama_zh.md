# 经济学家立传提示词（Eugene Fama）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2013 年得主 Eugene Fama（尤金·法马）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Eugene_Fama/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Eugene Francis "Gene" Fama（1939-02-14 生于美国马萨诸塞州波士顿，在世）
- **气质关键词**：**现代金融之父、有效市场假说的奠基人、用数据丈量市场的实证主义者**
- **诺奖获奖理由**（2013 三人共享同句，manifest citation_en 已给出，逐字引用）：
  > "for their empirical analysis of asset prices"（表彰他们对资产价格的实证分析）
  - 共享得主：Eugene Fama / Lars Peter Hansen / Robert J. Shiller——三人工作路径互异，诺奖授的是「资产价格实证分析」这一方法传统本身。
- **设计母题**：**随机游走（random walk）**——价格序列在时间轴上不可预测地跳跃铺展，恰是「短期价格变动近似随机游走」的视觉隐喻：错落的散点与步进轨迹构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Eugene_Fama/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Eugene_Fama/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Eugene_Fama_zh`、`VIDEO_NAME=Eugene_Fama_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Fama 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | infobox Discipline 首项；「现代金融之父」的学科根基 | 封面、核心页 |
| 1 | asset pricing | 资产定价 | 2013 诺奖核心——对资产价格的实证分析 | 核心页 |
| 2 | macroeconomics | 宏观经济学 | infobox Discipline 第三项；时变贴现率解释收益可预测性 | 收益页 |
| 3 | organizational economics | 组织经济学 | infobox Discipline 第二项 | 贡献概览页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 9 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Merton Miller | 对方是导师 | 芝加哥大学博士导师之一，诺奖得主 |
| advisor-student | Harry V. Roberts | 对方是导师 | 芝加哥大学博士导师之二 |
| influence | Benoît Mandelbrot | 对方影响本人 | 正文明载 important influence（非正式导师） |
| advisor-student | Cliff Asness | 本人 → 学生 | infobox Doctoral students 明载 |
| advisor-student | Myron Scholes | 本人 → 学生 | infobox Doctoral students 明载，1997 诺奖得主 |
| advisor-student | Mark Carhart | 本人 → 学生 | infobox Doctoral students 明载 |
| collaborator | Kenneth French | 无向 | Fama–French 三因子/五因子长期合著者 |
| co-honored | Robert J. Shiller | 无向 | 2013 同句理由共享诺奖 |
| co-honored | Lars Peter Hansen | 无向 | 2013 同句理由共享诺奖 |

**不入库但提示词可叙述**：DFA（Dimensional Fund Advisors）董事会任职（机构非人物关系）；书名编者 John H. Cochrane 与 Toby Moskowitz（《The Fama Portfolio》2017 编者，仅编辑关系非合作研究）；父母 Angelina（née Sarraceno）/ Francis Fama 与意大利移民祖辈（无独立成就叙述需要）。infobox frontmatter `doctoral_advisor` 三人并列含 Mandelbrot，属 Wikidata 噪声——以正文裁定为准：Mandelbrot 用 influence 类型入库。

## 五、配色方案 【人物专属】

- **气质**：冷峻、理性、数据洪流中的秩序感
- **主色**：`#8A1E2D`（manifest 预分配，芝加哥深红——芝加哥学派的学术血统与市场数据的厚重感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEMH` 有效市场 — 深红 `#8A1E2D`
  - `badgeFactor` 因子模型 — 深蓝 `#16324F`
  - `badgeEvent` 事件研究 — 青绿 `#0E7C7B`
  - `badgeSkep` 泡沫怀疑论 — 琥珀 `#C07A2A`
- **背景母题**：随机游走散点轨迹（价格步进序列的抽象），呼应「短期价格变动不可预测」的核心思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 现代金融之父 / Eugene Fama 1939– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1939-02-14 波士顿、Tufts BA 1960、
    芝加哥 MBA/PhD、导师 Miller & Roberts、任职芝加哥 Booth、诺奖 2013、核心领域）
03  核心贡献概览 — 有效市场假说 / 事件研究 / Fama–French 因子模型 / 泡沫怀疑论
04  早年波士顿 (1939–1960) — 意大利移民家庭、Malden Catholic 体育名人堂、Tufts 罗曼语系 magna cum laude
05  芝加哥博士 (1960–1964) — Miller 与 Roberts 门下，Mandelbrot 影响，1964 博士论文
06  随机游走：1965 开山之作 — "The Behavior of Stock Market Prices"、肥尾分布
07  有效市场假说：三种形态 (1970) — 弱式/半强式/强式效率，信息集定价
08  联合假设问题 — 市场效率须与均衡模型联合检验（Fama 1970/1991）
09  事件研究开山 (1969) — CRSP 数据、"The Adjustment of Stock Prices to New Information"
10  Fama–French 三因子模型 (1993) — 市场贝塔之外的规模（SMB）与价值（HML）
11  五因子模型 (2015) — 盈利（RMW）与投资（CMA），HML 常变冗余
12  泡沫怀疑论与比特币 — 泡沫须实时可判定；比特币的波动性、无内在价值
13  荣誉与业界影响 — 诺奖 2013、Deutsche Bank Prize 2005、DFA 董事会 1982 起、RePEc 史上第 9
14  遗产与结尾 — 金融经济学的实证地基 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享理由 | 2013 三人共享**同句理由** "for their empirical analysis of asset prices"；勿写成 Fama 个人理由，勿自行扩写 |
| 三人观点互异 | Fama 是有效市场假说奠基人，Shiller 以「过度波动」挑战之——同届获奖不等于观点一致，诺奖授的是实证分析传统；两人可用 controversy 吗？**不可**：page.md 未载两人直接交锋，禁建关系 |
| Mandelbrot 定性 | 正文明确 doctoral supervisors 是 Merton Miller 与 Harry V. Roberts，Mandelbrot 只是 "also an important influence"；frontmatter 三人并列 doctoral_advisor 系噪声，入库用 influence 类型 |
| 学生归属 | Cliff Asness / Myron Scholes / Mark Carhart 三人为 infobox Doctoral students 明载；page.md **未载** Asness 创办 AQR、Scholes 获奖细节——只写姓名与师生关系，禁编机构与事迹 |
| Kenneth French 定性 | French 是长期合著者（collaborator），**不在** Doctoral students 列表，勿建 advisor-student |
| 两代论文年份 | 博士论文 1964（*The Distribution of the Daily Differences of the Logarithms of Stock Prices*）；其内容 1965-01 发表于 Journal of Business 题为 "The Behavior of Stock Market Prices"——两年代勿混 |
| 三/五因子年份 | 三因子模型 1993 文章提出；五因子 2015 扩展（RMW 盈利、CMA 投资，HML 在部分数据集变冗余）；年份勿写反 |
| DFA 口径 | 1982 年起任 DFA 董事；$786 billion 是**2024 年底**资产管理规模口径，勿写成当前时点泛称 |
| 在世者生卒 | 1939-02-14 生，在世——卒日留白，全篇一致 |
| 引语红线 | "the father of modern finance" 是 page.md 转述（regarded as），中文引号内勿标「原话」；全篇无直接引语，勿杜撰 |
| RePEc 排名 | "9th-most influential economist of all time" 是 RePEc 项目 **as of 2019** 口径，注明统计时点 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| efficient-market hypothesis (EMH) | 有效市场假说 | Fama 奠基；勿与「市场 always 有效」划等号 |
| joint hypothesis problem | 联合假设问题 | 市场效率只能与均衡模型联合检验 |
| random walk | 随机游走 | 短期价格变动近似随机游走 |
| fat tail distribution | 肥尾分布 | 1965 年提出，极端变动比正态假设更常见 |
| event study | 事件研究 | 1969 年首篇重要事件研究，CRSP 数据 |
| SMB (Small Minus Big) | 规模因子 | 规模溢价 |
| HML (High Minus Low) | 价值因子 | 账面市值比溢价 |
| RMW / CMA | 盈利因子 / 投资因子 | 五因子模型 2015 新增 |
| alpha | 阿尔法 | 模型未解释的异常收益信号 |
| CRSP | 证券价格研究中心（数据库） | 事件研究的数据来源，勿译作公司名 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从波士顿移民家庭到「现代金融之父」，是一条以半个世纪实证积累铺就的长路——「最后的希望」的史诗感对应有效市场假说这一金融学大厦地基的分量；2013 三人共享的时刻亦是芝加哥学派实证传统的加冕。
- **本地路径**：复制上述 wav 到 `economics/presentations/21th_century/Eugene_Fama/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
