# 经济学家立传提示词（Merton Miller）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1990 年得主 Merton Miller（默顿·米勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Merton_Miller/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Merton Howard Miller（1923-05-16 生于波士顿 ~ 2000-06-03 逝于芝加哥，享年 77 岁）
- **气质关键词**：**MM 定理的共同作者、资本结构无关性的证明者、芝加哥商学院的定价人**
- **获奖理由**（1990 三人共享，逐字引用，中文翻译照抄总名录）：
  > "for their pioneering work in the theory of financial economics"
  > （表彰他们在金融经济学理论方面的开创性工作）
- **设计母题**：**天平与无差异（balance & irrelevance）**——MM 定理说资本结构（债/股比例）本身不改变企业价值：一架两端等重的天平、无论砝码如何摆放在哪一端都保持平衡。天平意象构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Merton_Miller/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Merton_Miller/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Merton_Miller_zh`、`VIDEO_NAME=Merton_Miller_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Miller 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | financial economics | 金融经济学 | 1990 诺奖理由核心词 | 封面、核心页 |
| 1 | corporate finance | 公司金融 | MM 定理（1958）：债股结构与资本成本无关性 | 核心页 |
| 2 | derivatives markets | 衍生品市场 | *Merton Miller on Derivatives*（1991）；CBOT/CME 公共董事 | 贡献页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Fritz Machlup | Miller → 学生 | Johns Hopkins 博士导师（infobox/正文 1952 PhD） |
| colleague | Franco Modigliani | 无向 | 1958 Carnegie Tech 合作 MM 定理论文 |
| advisor-student | Eugene Fama | Miller → 学生 | infobox Doctoral students 明载 |
| advisor-student | William Poole | Miller → 学生 | infobox Doctoral students 明载 |
| collaborator | Reuben A. Kessel | 无向 | 合编 *Essays in Applied Price Theory*（1980，与 Coase 三人） |
| collaborator | Ronald Coase | 无向 | 合编 *Essays in Applied Price Theory*（1980，与 Kessel 三人） |
| spouse | Eleanor Miller | 无向 | 首任妻子，1969 去世 |
| spouse | Katherine Miller | 无向 | 第二任妻子 |
| co-honored | Harry Markowitz | 无向 | 1990 诺贝尔经济学奖三人共享（金融经济学理论开创性工作） |
| co-honored | William F. Sharpe | 无向 | 1990 诺贝尔经济学奖三人共享（金融经济学理论开创性工作） |

**不入库但提示词可叙述**：三个女儿 Pamela(1952)/Margot(1955)/Louise(1958)（仅具名无生平、防泛化 stub 不入 parent-child）；Eugene Fama 与 Miller 合著 *The Theory of Finance*（1972）——已有 advisor-student 边体现师承，不再重复建 collaborator 边；Metallgesellschaft/CME/Chicago Board of Trade/Nasdaq 为机构不入库。**本人 yaml relations=10 为 page.md 明载诚实值。**

**并行批次入边（非本 yaml 产生，Review 勿误判）**：①Miller→Franco Modigliani 另有 collaborator 边（batch-05 Modigliani 篇按其页面所建，与本篇 colleague 边同对同向异型并存，各自有本页依据）；②Miller→Myron Scholes advisor-student 边（batch-09 Scholes 篇按 Scholes 页面 infobox 所建，本篇页面无载故不建）；③Miller→Eugene Fama advisor-student 边若 note 为「芝加哥大学博士导师之一，诺奖得主」系 batch-09 先写入保留其 note（同型同向 uq_rel 幂等去重）。

## 五、配色方案 【人物专属】

- **气质**：冷峻、芝加哥、套利论证的锋利
- **主色**：`#9E2B25`（砖红——manifest 预分配，1990 三人共享主色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMM` MM 定理 — 深蓝 `#1E3A5F`
  - `badgeArb` 无套利论证 — 灰紫 `#52307C`
  - `badgeMkt` 市场与衍生品 — 深青 `#0E4D64`
  - `badgeUch` 芝加哥岁月 — 琥珀 `#C07A2A`
- **背景母题**：天平与等值刻度（债/股两端无论组合如何，总值不变），呼应「天平与无差异」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — MM 定理的共同作者 / Merton Miller 1923–2000 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地波士顿、教育哈佛本科/Johns Hopkins PhD 1952、
    任职 Carnegie Tech → 芝加哥大学 Booth 商学院 1961–1993、诺奖 1990、核心领域）
03  核心贡献概览 — MM 定理 / 无套利论证 / 衍生品市场实务 / 公司金融范式
04  波士顿早年与哈佛 (1923–1940s) — 犹太家庭；战时财政部税务研究部经济学家
05  Johns Hopkins 与 LSE — PhD 1952；毕业后首站 LSE 访问助理讲师
06  Carnegie 与 MM 定理诞生 (1958) — *The Cost of Capital, Corporate Finance and the Theory of Investment*
07  MM 定理：资本结构无关性（核心贡献页）— 无"正确的"债股比；管理层应最小化税负、最大化净财富；
    无套利论证（riskless money machine 会迅速消失）为后续论证定调
08  无套利：一个论证范式的诞生 — "no arbitrage" 前提在后续金融学论证中的范式地位
09  芝加哥岁月 (1961–1993) — Booth 商学院任教至退休，后又授课数年；八本著作
10  学生与传承 — Eugene Fama（合著 *The Theory of Finance* 1972）、William Poole；Fama 的有效市场后续
11  学界服务 — Econometric Society Fellow 1975；American Finance Association 主席 1976
12  市场实务与争议 — CBOT 公共董事 1983–85；CME 1990–2000；1993 Metallgesellschaft 论战
    （WSJ 撰文归因于管理层恐慌平仓）；1995 Nasdaq 定价指控的驳斥委托——均按 page.md 客观叙述
13  1990 诺贝尔奖 — 与 Harry Markowitz、William F. Sharpe 三人共享；获奖演讲 1990-12-07 *Leverage*
14  遗产与结尾 — 家庭（两任妻子、三个女儿）；2000-06-03 卒于芝加哥 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1990 三人共享 | 与 Markowitz/Sharpe 共享同句理由——Miller 的工作（MM 定理/公司金融）与另两人互不相同，勿写成分工或"因组合理论获奖"；本页 deck 三篇 BGM/主色均同（manifest 预分配） |
| MM 定理归属 | 1958 论文与 **Franco Modigliani** 合作（Carnegie Tech），定理以两人命名——Miller 1990、Modigliani 1985 各自独得诺奖，勿写成"同届"或"因此定理共同获奖" |
| Modigliani 定性 | 正文 "collaborated with his colleague Franco Modigliani"——建 colleague 单条边即可，勿写 advisor/co-honored |
| 生卒双值 | metadata frontmatter 生年双值（05-16/01-01）、卒年双值（06-03/01-01）——**以正文 1923-05-16 与 2000-06-03 为准** |
| 博士生 | Eugene Fama / William Poole 两人为 infobox Doctoral students 明载——仅此两人，勿扩写其他学生 |
| Fama 双重身份 | Fama 既是博士生又与 Miller 合著 *The Theory of Finance*（1972）——advisor-student 一条边已体现师承，合著不再另建边，防重复 |
| 家庭 | 首任妻子 Eleanor（1969 卒）、第二任 Katherine（入库 spouse 两条）；三个女儿仅具名+生年，不入库（防泛化 stub） |
| 机构职务 | CBOT 公共董事 1983–85、CME 1990–2000（至去世）——机构不入库，只在时间线叙述 |
| 争议表述 | Metallgesellschaft（1993 归因管理层恐慌平仓）与 Nasdaq（1995 驳斥定价指控）按 page.md 客观转述 Miller 立场，不作评价 |
| 获奖演讲 | 1990-12-07 *Leverage*（external links 明载），勿与获奖理由混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Modigliani–Miller theorem | MM 定理 | 资本结构无关性，1958 |
| cost of capital | 资本成本 | 定理核心变量 |
| debt-to-equity ratio | 债务股本比 | "无正确比例"是定理结论 |
| no arbitrage | 无套利 | 论证范式，影响后续金融学 |
| arbitrage | 套利 | 与无套利前提区分 |
| public director | 公共董事 | CBOT/CME 任职头衔 |
| leverage | 杠杆 | 获奖演讲题目 |
| derivative | 衍生品 | 晚年著述与实务主题 |
| corporate finance | 公司金融 | 研究领域主词 |
| rogue futures trader | 流氓期货交易员 | Metallgesellschaft 事件的表述背景 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，1990 三人共享曲目，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「自由之风」贴合 MM 定理把公司金融从"寻找最优债股比"的执念中解放出来的颠覆性；与 Markowitz/Sharpe 两篇同曲同色形成同届三人组的呼应。
- **本地路径**：复制 `music_audio/inspiring-electronic/25-l3Fsk4R6eys-...Winds Of Freedom.wav` 到 `economics/presentations/20th_century/Merton_Miller/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
