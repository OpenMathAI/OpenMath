# 经济学家立传提示词（Guido Imbens）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2021 年得主 Guido Imbens（吉多·因本斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Guido_Imbens/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Guido Wilhelmus Imbens（1963-09-03 生于荷兰海尔德罗普，在世，卒年留白）
- **气质关键词**：**因果推断的计量建筑师、自然实验的翻译官、LATE 框架的提出者**
- **诺奖获奖理由**（2021 拆分理由：Imbens 与 Angrist 共享一半；Card 独得另一半。英文逐字引自 `economics/nobel_economics_citations.json` 2021 Guido Imbens 条目）：
  > "for their methodological contributions to the analysis of causal relationships"（表彰他们对因果关系分析方法论的贡献）
  > ——中译对照 `economics/economics_list_data.py` 2021 年 `||` 拆分第二段。
- **设计母题**：**因果之桥（bridge from correlation to causation）**——自然实验是横跨「相关」与「因果」两岸的桥：以斜拉桥/虚线补全的散点图（反事实延伸）作为背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Guido_Imbens/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Guido_Imbens/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Guido_Imbens_zh`、`VIDEO_NAME=Guido_Imbens_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Imbens 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | Discipline 明载；斯坦福 GSB 应用计量讲席教授 | 封面、核心页 |
| 1 | causal inference | 因果推断 | 2021 诺奖获奖理由核心；LATE 框架 | 核心页 |
| 2 | statistics | 统计学 | 正文 "econometrics and statistics"；与 Rubin 合著教材 | 方法页 |
| 3 | program evaluation | 项目评估 | 与 Wooldridge 合著 "Program Evaluation" 综述 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Anthony Lancaster | Lancaster → Imbens | Hull 硕士导师随迁布朗大学，续任博士导师；PhD 1991 |
| advisor-student | Rajeev Dehejia | Imbens → 学生 | infobox Doctoral students 明载 |
| advisor-student | Alfred Galichon | Imbens → 学生 | infobox Doctoral students 明载 |
| spouse | Susan Athey | 无向 | 经济学家，2002 结婚；斯坦福 GSB 同事（Technology 经济学讲席） |
| collaborator | Susan Athey | 无向 | 2016 前后合作用机器学习（causal forests）估计异质性处理效应 |
| co-honored | Joshua Angrist | 无向 | 2021 诺奖共享一半："for their methodological contributions to the analysis of causal relationships" |
| co-honored | David Card | 无向 | 2021 诺奖同届：Angrist 与 Imbens 共享一半，Card 独得另一半 |
| collaborator | Joshua Angrist | 无向 | 1994 Econometrica 论文提出 LATE 框架；婚礼男傧相 |
| collaborator | Alan Krueger | 无向 | "Working with fellow economists including Angrist and Krueger" 明载合作 |
| collaborator | Donald Rubin | 无向 | 2001 马萨诸塞州彩票自然实验合著；2015 合著《Causal Inference for Statistics, Social, and Biomedical Sciences》 |
| collaborator | Bruce Sacerdote | 无向 | 2001 彩票自然实验论文合著者 |
| collaborator | Thomas Lemieux | 无向 | 2007 合著《Regression discontinuity designs: a guide to practice》 |
| influence | Jan Tinbergen | Tinbergen → Imbens | 高中受廷贝亨著作影响而选计量经济学；廷贝亨曾在鹿特丹伊拉斯姆斯大学创办计量项目（库内 id=7624） |

**不入库但提示词可叙述**：Angrist 婚礼男傧相细节（事件性，collaborator 边已覆盖）；Gary Chamberlain / Jeffrey Wooldridge / Alberto Abadie 等合著者（仅 Bibliography 列表，无正文合作叙述）；Chess 童年爱好（无对手方）。

## 五、配色方案 【人物专属】

- **气质**：缜密、桥接、从观测到因果的清晰链条
- **主色**：`#0E4D64`（manifest 预分配——深青蓝，与本批三人同色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEcon` 计量经济学 — 深青蓝 `#0E4D64`
  - `badgeCausal` 因果推断 — 琥珀 `#C07A2A`
  - `badgeStat` 统计学 — 灰紫 `#52307C`
  - `badgeEval` 项目评估 — 青绿 `#0E7C7B`
- **背景母题**：散点图中的虚线延伸与斜拉桥索（相关点向因果对岸的虚线外推），呼应「反事实推断」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 因果推断的计量建筑师 / Guido Imbens 1963– + 四色 badge + 右上头像 + 国籍行（United States / Netherlands）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（1963-09-03 生于 Geldrop、Erasmus 1983、Hull MSc 1986、
    Brown PhD 1991、斯坦福 GSB（2012 起）、诺奖 2021、核心领域）
03  核心贡献概览 — LATE 框架 / 自然实验方法论 / 与 Rubin 的统计因果框架 / 项目评估
04  早年：海尔德罗普的棋手 (1963–1983) — 童年痴迷国际象棋；高中读到廷贝亨；Erasmus 计量经济学 1983 毕业
05  Hull 与布朗 (1983–1991) — Hull MSc with distinction 1986；随 Lancaster 迁布朗；论文 "Two essays in econometrics"
06  LATE：局部平均处理效应（核心贡献页）— 1994 Econometrica "Identification and Estimation of Local Average Treatment Effects"
07  自然实验方法论 — 受控实验昂贵/耗时/不道德时，用天然随机化推断因果
08  彩票自然实验 (2001) — 与 Rubin/Sacerdote：逐年领取的彩票奖金对劳动供给影响很小
09  与 Rubin 的因果框架 — 2015 合著《Causal Inference for Statistics, Social, and Biomedical Sciences》
10  机器学习与因果森林 — 2016 前后与 Athey 用随机森林变体估计异质性处理效应
11  2021 诺贝尔经济学奖 — 与 Angrist 共享一半；Card 独得另一半；瑞典科学院新闻稿口径
12  学术履历 — Tilburg 1989–90 / Harvard 1990–97 与 2007–12 / UCLA 1997–2001 / Berkeley 2001–07 / Stanford 2012–
13  荣誉与个人生活 — Econometric Society Fellow 2001、荷兰皇家科学院外籍院士 2017、ASA Fellow 2020；
    2002 与 Athey 结婚、Angrist 任男傧相
14  遗产与结尾 — 可信度革命的计量地基 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 2021 拆分理由 | Imbens 与 Angrist **共享一半**，理由是 "their methodological contributions..."；Card 独得另一半且理由不同——co-honored note 须区分「共享一半」与「同届另一半」 |
| 导师姓名形式 | frontmatter 作 Tony Lancaster，infobox/正文作 **Anthony Lancaster**——入库用 Anthony Lancaster，正文可括注「人称 Tony」 |
| Tinbergen 关系 | page.md 明载 "Influenced by Tinbergen's work"——influence 边（Tinbergen → Imbens）；廷贝亨是 1969 首届经济学诺奖得主，库内已有记录（id=7624 Jan Tinbergen），**必须复用勿新建** |
| 国籍口径 | manifest "United States / Netherlands"（正文 dual citizenship）；frontmatter ["Kingdom of the Netherlands", "United States"]——yaml 按 manifest 口径 |
| 引语红线 | 可引原文：瑞典科学院新闻稿 "have provided us with new insights about the labour market and shown what conclusions about cause and effect can be drawn from natural experiments..."（引原文+译文）；2021 访谈把计量经济学与童年棋艺相连（转述，勿加引号）。其余叙述不得冒充原话 |
| LATE 归属 | 1994 LATE 框架是 Imbens 与 Angrist **合著**提出，勿写成 Imbens 独创；Angrist 页 infobox 亦列 LATE 为 notable idea |
| 学生名单 | infobox 仅 Rajeev Dehejia、Alfred Galichon 两人；relations=13 为诚实值，勿硬凑 |
| Rubin 姓名 | 正文两处 "Donald Rubin"、书目一处 "Donald B. Rubin"——入库统一用 **Donald Rubin** |
| 在世留白 | 1963 生、在世；幻灯片年份写 "1963–"，卒年不写 |
| 期刊编辑 | 2019 年起任 Econometrica 主编，(截至 2022) 预计任期至 2025——写「2019 起任主编」即可，勿断言结束年 |
| 荣誉年份 | 荣誉博士 2014 圣加仑 / Horace Mann Medal 2017 / Brown LLD 2022 / 鹿特丹荣誉博士 2023——年份各自独立勿串 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| local average treatment effect (LATE) | 局部平均处理效应 | 1994 合著提出，勿写成"局部治疗效果" |
| natural experiment | 自然实验 | 受控实验昂贵/耗时/不道德时的替代路径 |
| causal inference | 因果推断 | 获奖理由核心词 |
| instrumental variables | 工具变量 | 自然实验识别的手段之一 |
| regression discontinuity | 断点回归 | 与 Lemieux 合著指南的主题 |
| counterfactual | 反事实 | 散点图虚线延伸的视觉母题 |
| credibility revolution | 可信度革命 | page.md 明载词条，可写 |
| econometrics | 计量经济学 | Discipline 原词 |
| delegated monitoring | 委托监督 | 属 Diamond 篇术语，勿混入 |
| program evaluation | 项目评估 | 与 Wooldridge 综述主题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："探路者"同样契合 Imbens——在「相关≠因果」的禁航区架桥，为自然实验提供可靠的因果推断航线；与本批三人的同批同曲亦符合同届三主同规格的批量约定。
- **本地路径**：复制 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` 到 `economics/presentations/21th_century/Guido_Imbens/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Guido_Imbens/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Guido_Imbens/metadata.json` | QID/生卒/国籍结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Guido_Imbens/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input`） |
| `MySQL/data/Guido_Imbens.yaml` | 社会关系/研究领域入库存档（本批次已入库） |
| `economics/nobel_economics_citations.json` | 2021 拆分获奖理由英文原文 |
| `economics/economics_list_data.py` | 2021 年中译对照（`||` 拆分第二段） |

## 十一、执行清单（供 Beamer agent 核对） 【模板通用】

1. 核对事实基准：所有事实与 page.md 逐条对照，冲突一律以 page.md 为准并在陷阱表记录裁定。
2. 复制 Makefile：`MAIN=Guido_Imbens_zh`、`VIDEO_NAME=Guido_Imbens_zh`。
3. 肖像：优先 images.txt 真实肖像（page.md 引用图 Guido_Imbens_Lemley_Lecture_2.jpg 为 2022 布朗演讲照）；404 则装饰圆占位（勿用无授权图）。
4. 配色：主色 `#0E4D64` + badge 四色 + 背景母题（虚线延伸散点图/斜拉桥索）。
5. 幻灯片序列：按第六节 15 页规划，第 02 页身份信息页必做。
6. 编译循环：`make distclean && make`，0 error、vbox ≤ 10pt、hbox ≤ 50pt；pdftoppm 逐页目检。
7. 引语红线：只有第八节列出的 page.md 原文可入引文框（引原文+译文），其余叙述不加中文引号。
8. 结尾页品牌口径：底部标注 `OpenMathAI`（与共享 GitHub 一致），引号用半角 " "。
9. 完成后 `make images && make video` 产出 mp4，向主控汇报页数与体积。

## 十二、版式补遗 【模板通用】

- **共享封面**：第 00 页 `\input` OpenEcon 统一封面，子 deck 不重复 GitHub 链接。
- **封面页**：主标题字号沿用模板（26/32 折叠口径）；badge 主字体 scriptsize、副行 `\fontsize{6.5}{7.8}`；右上肖像 `draw=coveraccent!50` 细边框 + 姓名小字注。
- **身份信息页**：左头像 + 右信息网格，含至少生卒/出生地/教育/师承/任职/主要荣誉/核心领域七要素。
- **表格页安全负间距**：顶部 -0.35cm、`arraystretch 0.78-0.82`、公式框前 -0.35~-0.55cm；表格页拥挤时优先 `itemize` 的 `topsep=0pt`。
- **时间线页**：`\foreach` 分隔符必须 ASCII 逗号；节点样式套用会触发 pgffor 错误，改行内字色。
- **年份留白**：在世者卒年一律 "1963–"，不得虚构或写"至今"以外的猜测值。
- **获奖理由引用框**：英文原句 + 中文翻译两行制，英文逐字来自 `nobel_economics_citations.json`，不得改写。

## 十三、关键时间线速查 【人物专属】

| 年份 | 事件（均出自 page.md） |
|------|------|
| 1963-09-03 | 生于荷兰 Geldrop |
| 童年 | 国际象棋爱好者；2021 访谈把对计量经济学的热情与童年棋艺相连 |
| 高中 | 读到荷兰经济学家 Jan Tinbergen 的著作 |
| 1983 | 鹿特丹伊拉斯姆斯大学计量经济学 Candidate 学位毕业 |
| 1986 | 英国 Hull 大学经济学与计量 MSc（with distinction） |
| 1986 | 导师 Anthony Lancaster 由 Hull 迁往布朗大学，Imbens 随迁 |
| 1989 / 1991 | 布朗大学经济学 AM / PhD；论文 "Two essays in econometrics"（1991） |
| 1989–1990 | Tilburg 大学任教 |
| 1990–1997 | 哈佛大学任教（第一段） |
| 1994 | 与 Angrist 在 Econometrica 发表 LATE 论文 |
| 1997–2001 | UCLA 任教 |
| 2001–2007 | UC Berkeley 任教；Econometric Society Fellow（2001） |
| 2001 | 与 Rubin、Sacerdote 发表马萨诸塞州彩票自然实验研究 |
| 2002 | 与经济学家 Susan Athey 结婚（婚礼男傧相为 Angrist） |
| 2007–2012 | 哈佛大学任教（第二段）；American Academy Fellow（2009） |
| 2012 至今 | 斯坦福 GSB 应用计量与经济学教授；SIEPR 高级研究员 |
| 2014 / 2017 | 圣加仑荣誉博士 / 荷兰皇家科学院外籍院士、布朗 Horace Mann Medal |
| 2015 | 与 Rubin 合著《Causal Inference for Statistics, Social, and Biomedical Sciences》出版 |
| 2016 前后 | 与 Athey 研究因果森林（causal forests）估计异质性处理效应 |
| 2019–（约 2025） | 任 Econometrica 主编 |
| 2020 / 2021 | ASA Fellow / 诺贝尔经济学奖（与 Angrist 共享一半） |
| 2022 / 2023 | 布朗名誉博士 / 鹿特丹伊拉斯姆斯大学荣誉博士 |

> 表内每条均有 page.md 明载；未列年份的条目（童年/高中）写「约」或不带年份呈现。

