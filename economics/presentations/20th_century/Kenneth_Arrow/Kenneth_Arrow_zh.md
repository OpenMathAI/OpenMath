# 经济学家立传提示词（Kenneth Arrow）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1972 年得主 Kenneth Arrow（肯尼斯·阿罗）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Kenneth_Arrow/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Kenneth Joseph Arrow（1921-08-23 生于纽约市 ~ 2017-02-21 逝于加州帕洛阿尔托，享年 95 岁）
- **气质关键词**：**不可能定理的证明者、一般均衡的严格化者、四位诺奖门生的师尊**
- **诺奖获奖理由**（1972，与 John Hicks 共享，逐字引自 manifest）：
  > "for their pioneering contributions to general economic equilibrium theory and welfare theory"（表彰他们在一般经济均衡理论与福利理论方面的开创性贡献）
- **设计母题**：**不可能性的悖论（impossibility & equilibrium）**——个体偏好如何聚合成社会排序却无法同时满足全部条件，是「多数 arrow 汇流却无公共河道」的视觉隐喻：散点汇聚与受阻的流向构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Kenneth_Arrow/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Kenneth_Arrow/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Kenneth_Arrow_zh`、`VIDEO_NAME=Kenneth_Arrow_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Arrow 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | general equilibrium theory | 一般均衡理论 | 诺奖核心；1954 Arrow–Debreu 存在性证明 | 核心页 |
| 1 | social choice theory | 社会选择理论 | 不可能性定理（General Possibility Theorem，1951） | 核心页 |
| 2 | welfare economics | 福利经济学 | 1951 两大基本定理及证明 | 核心页 |
| 3 | information economics | 信息经济学 | 1963 医疗保险非对称信息论文开创 | 应用页 |
| 4 | endogenous growth theory | 内生增长理论 | 1962 learning-by-doing 模型为前身 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Harold Hotelling | Hotelling → 师 | 哥伦比亚大学博士导师，引导其转向经济学 |
| influence | Alfred Tarski | 无向 | infobox Influences 明载（库内 id=397 复用） |
| influence | Adam Smith | 无向 | 一般均衡工作受《国富论》影响（正文明载） |
| co-honored | John Hicks | 无向 | 1972 诺贝尔经济学奖共享（一般均衡与福利理论） |
| advisor-student | John Harsanyi | Arrow → 学生 | 正文明载四位诺奖门生之一（1994） |
| advisor-student | Eric Maskin | Arrow → 学生 | 正文明载四位诺奖门生之一（2007） |
| advisor-student | Roger Myerson | Arrow → 学生 | 正文明载四位诺奖门生之一（2007） |
| advisor-student | Michael Spence | Arrow → 学生 | 正文明载四位诺奖门生之一（2001） |
| collaborator | Gérard Debreu | 无向 | 1954 合著竞争经济均衡存在性（Econometrica） |
| colleague | Lionel McKenzie | 无向 | 平行独立证明市场出清均衡存在性 |
| colleague | Robert Solow | 无向 | 1960s 同在经济顾问委员会任职 |
| spouse | Selma Schweitzer | 无向 | 1947 结婚，芝加哥大学经济学毕业生、心理治疗师，2015 去世 |

**不入库但提示词可叙述**：infobox Doctoral students 另有 15 人（David Bradford、Michael Bruno、Joshua Gans、Nancy Gordon、Michael Schwarz、Gillian Hadfield、Jan Kmenta、Timur Kuran、Jean-Jacques Laffont、Andrea Prat、Karl Shell、Nancy Stokey、Menahem Yaari、Sebastián Piñera 等）——防噪声只收正文点名四位诺奖门生；妹妹 Anita Summers（经济学家，无 sibling 类型）、外甥 Larry Summers、姻亲 Robert Summers 与 Paul Samuelson（姻亲无类型，不入库）；二子 David Michael 与 Andrew Seth 为演员且无维基链接不入库；Philip W. Anderson→Arrow 的 Santa Fe colleague 边已由物理侧入库无需重复。

## 五、配色方案 【人物专属】

- **气质**：冷静、公理化、以数学之刃剖开社会科学
- **主色**：`#123C5B`（公理化深蓝——定理与证明的冷峻感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGE` 一般均衡 — 深蓝 `#123C5B`
  - `badgeSC` 社会选择 — 灰紫 `#52307C`
  - `badgeWF` 福利经济学 — 青绿 `#0E7C7B`
  - `badgeInfo` 信息与增长 — 琥珀 `#C07A2A`
- **背景母题**：散点汇聚与受阻流向（偏好聚合的不可能性抽象），呼应设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 不可能定理的证明者 / Kenneth Arrow 1921–2017 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地纽约、CCNY 数学学士 1940、哥伦比亚 MS 1941/PhD 1951、
    师承 Hotelling、任职 Stanford/Chicago/Harvard、诺奖 1972、核心领域）
03  核心贡献概览 — 不可能性定理 / 福利经济学两大定理 / Arrow–Debreu 一般均衡 / 信息经济学与内生增长
04  纽约早年 (1921–1940) — 罗马尼亚犹太移民家庭、大萧条中长大、Townsend Harris 高中、CCNY 数学学士
05  哥伦比亚与 Hotelling (1940–1942) — 数学硕士、受 Hotelling 引导转向经济学
06  战时气象官与 RAND (1942–1949) — 陆军航空队 weather officer、Cowles Commission、芝加哥助理教授
07  不可能性定理 (1951) — Social Choice and Individual Values 源自博士论文、五条件与 General Possibility Theorem
08  福利经济学两大定理 (1951) — 免可微性假设、含角点解的证明
09  Arrow–Debreu 一般均衡 (1954) — 竞争经济均衡存在性首次严格证明、McKenzie 平行工作、Debreu 1983 获奖背景
10  内生增长与信息经济学 (1962/1963) — learning-by-doing、Uncertainty and the Welfare Economics of Medical Care
11  门生与传承 — Harsanyi/Spence/Maskin/Myerson 四位诺奖门生
12  荣誉与认可 — Clark Medal 1957 · 诺奖 1972 · von Neumann Theory Prize 1986 · National Medal of Science 2004 · ForMemRS 2006
13  斯坦福晚年 (1979–1991) — Joan Kenney 讲席教授、1995 锡耶纳 Fulbright、Santa Fe Institute 董事
14  遗产与结尾 — 社会选择与一般均衡的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享奖口径 | 1972 与 **John Hicks** 共享；获奖理由是"their"，表述勿写成 Arrow 独得 |
| 定理名称 | 正文称其本人命名为 **General Possibility Theorem**；通名 Arrow 不可能性定理；两称勿混为两个定理 |
| 学位时间线 | CCNY 数学学士 1940 → 哥伦比亚数学硕士 1941-06 → **1951** 才获哥伦比亚 PhD；勿写成 1941 获博士 |
| 军旅身份 | 1942–1946 任美国陆军航空队 **weather officer**（气象官），勿写成"参战飞行员" |
| 学生防噪声 | infobox Doctoral students 共 19 人；正文仅点名 Harsanyi/Maskin/Myerson/Spence 四位诺奖门生，入库只收这四人，其余 metadata 级不入库 |
| 家属类型缺口 | 妹妹 Anita Summers、姻亲 Samuelson/Robert Summers、外甥 Larry Summers 均无对应 relation 类型，不入库（正文可叙述） |
| 姻亲 Samuelson | Paul Samuelson 是其妹夫（brother-in-law），同时是 Leontief 的学生——两条线在各自主篇中体现，勿在 Arrow 篇建边 |
| 引语红线 | 1974 AEA 论文引语（Adam Smith 主题段）正文有英文原文，可引用并附译文；不得杜撰中文"原话" |
| metadata 噪声 | frontmatter field_of_work 含 "literature"、occupation 含 political scientist/writer 系 Wikidata 噪声，以正文 discipline（微观/一般均衡/社会选择）为准 |
| Santa Fe 边 | Anderson→Arrow colleague 已由物理侧入库；本篇 yaml 不重复建，提示词可在晚年页叙述 Santa Fe 董事身份 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| general possibility theorem | 一般可能性定理 | Arrow 本人的命名，通名"不可能定理" |
| impossibility theorem | 不可能性定理 | 非"不可能性原理" |
| social choice theory | 社会选择理论 | 与投票理论关联，扩展 Condorcet 悖论 |
| fundamental theorems of welfare economics | 福利经济学基本定理 | 第一定理与第二定理成对出现 |
| Arrow–Debreu model | 阿罗–德布鲁模型 | 1954 Econometrica 合著 |
| learning-by-doing | 干中学 | 1962 论文，内生增长前身 |
| asymmetric information | 非对称信息 | 1963 医疗保险市场论文 |
| general equilibrium | 一般均衡 | 勿简称"全部均衡" |
| Cowles Commission | 考尔斯委员会 | 1946–1949 研究经历 |
| weather officer | 气象官 | 二战军职，非"预报员"泛称 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：回望 20 世纪社会科学公理化的黄金年代——从大萧条中的纽约少年到斯坦福的世纪学者，"怀旧"的抒情底色贴合其贯穿冷战时代、横跨理论与政策的漫长学术生涯。
- **本地路径**：复制 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` 到 `economics/presentations/20th_century/Kenneth_Arrow/Nostalgia.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Kenneth_Arrow/page.md` | 事实基准（唯一事实来源） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |
| `MySQL/data/Kenneth_Arrow.yaml` | 入库 yaml（与本文第三、四节一致） |
| `economics/economics_list_data.py` / `nobel_economics_citations.json` | 获奖理由中文对照 |

## 十一、执行清单 【模板通用】

1. 读 page.md 建立事实基准（本文件已沉淀，直接核对即可）
2. 下载肖像（images.txt 有 URL 直接用 500px；404 用 Commons `Special:FilePath`，再 404 装饰圆占位）
3. 复制 BGM wav 到人物目录
4. 写 tex（配色按第五节、Slide 序列按第六节）
5. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt
6. pdftoppm + read_file 逐页目检
7. make images/video；Review-1 修正写回本文件
