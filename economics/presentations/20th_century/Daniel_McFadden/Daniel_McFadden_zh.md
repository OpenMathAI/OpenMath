# 经济学家立传提示词（Daniel McFadden）

> 本文件是 OpenMathAI OpenEcon 项目 20 世纪诺贝尔经济学奖 **2000 年得主 Daniel McFadden（丹尼尔·麦克法登）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Daniel_McFadden/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Daniel Little McFadden（1937-07-29 生于美国北卡罗来纳州罗利，在世）
- **气质关键词**：**离散选择的计量大师、条件 logit 的发明人、从物理学到行为科学的转行者**
- **诺奖获奖理由**（2000 与 James Heckman 拆分共享，逐字引用 `nobel_economics_citations.json` 本人条目）：
  > "for his development of theory and methods for analyzing discrete choice"（表彰他发展了分析离散选择的理论与方法）
  - 注意：2000 为拆分理由年份，Heckman 那一半是 "for his development of theory and methods for analyzing selective samples"（表彰他发展了分析选择性样本的理论与方法）——本篇只写本人那条，介绍 Heckman 时可并列对照。
- **设计母题**：**离散选择（discrete choice）**——人在有限选项集中做"非此即彼"的抉择，视觉隐喻：分叉的选择树与随属性变化的概率条（多项 logit 的 0-1 之间连续概率切分）。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Daniel_McFadden/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Daniel_McFadden/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Daniel_McFadden_zh`、`VIDEO_NAME=Daniel_McFadden_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**McFadden 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | infobox Fields；核心身份 | 封面、核心页 |
| 1 | discrete choice | 离散选择 | Known for；诺奖理由核心词 | 核心页 |
| 2 | choice behavior | 选择行为 | 1964 入伯克利后的研究焦点 | 核心页 |
| 3 | health economics | 健康经济学 | USC 总统讲席教授（2011） | 晚近页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 12 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Leonid Hurwicz | Hurwicz → McFadden | 明尼苏达研究生导师；2007 经济学诺奖得主 |
| advisor-student | Axel Börsch-Supan | McFadden → 学生 | infobox Doctoral students 明载 |
| advisor-student | Philip J. Cook | McFadden → 学生 | infobox 明载 |
| advisor-student | Walter Erwin Diewert | McFadden → 学生 | infobox 明载 |
| advisor-student | Jonathan Feinstein | McFadden → 学生 | infobox 明载 |
| advisor-student | Donald J. Harris | McFadden → 学生 | infobox 明载 |
| advisor-student | Fred Mannering | McFadden → 学生 | infobox 明载 |
| advisor-student | John Rust | McFadden → 学生 | infobox 明载 |
| advisor-student | Kenneth E. Train | McFadden → 学生 | infobox 明载 |
| advisor-student | Hal Varian | McFadden → 学生 | infobox 明载 |
| advisor-student | Clifford Winston | McFadden → 学生 | infobox 明载 |
| co-honored | James Heckman | 无向 | 2000 诺贝尔经济学奖共享（本人理由：离散选择的理论与方法；Heckman：选择性样本） |

**不入库但提示词可叙述**：2024 年 16 位经济学诺奖得主联名公开信事件（涉政治人物，禁写，见陷阱表）；Econometrics Laboratory（机构不建人物边）；Economists for Peace and Security（组织不建人物边）。

## 五、配色方案 【人物专属】

- **气质**：精微、定量、把人的选择变成可计算的科学
- **主色**：`#283593`（manifest 预分配——靛蓝，概率与计量的数学冷光）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEco` 计量经济学 — 靛蓝 `#283593`
  - `badgeDisc` 离散选择 — 青绿 `#0E7C7B`
  - `badgeLogit` 条件 logit — 玫瑰 `#C4204F`
  - `badgeHealth` 健康经济学 — 琥珀 `#C07A2A`
- **背景母题**：分叉选择树与概率条（同一决策者在多选项间的概率切分），呼应"把离散选择变成可估计的模型"。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 离散选择的计量大师 / Daniel McFadden 1937– + 四色 badge + 右上头像 + 国籍行（USA）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒罗利、明尼苏达 BS 物理 + PhD 行为科学 1962、
    导师 Hurwicz、伯克利/MIT/USC 任职、克拉克奖章 1975、诺奖 2000）
03  核心贡献概览 — 条件 logit 分析 / 离散选择理论与方法 / 计量实验室 / 健康经济学
04  从物理学到行为科学 (1937–1962) — 罗利出生、明尼苏达物理 BS、五年后行为科学（经济学）PhD、
    论文 Factor Substitution in the Economic Analysis of Production
05  Hurwicz 门下 — 明尼苏达研究生导师（2007 年经济学诺奖得主——师生两代诺奖）
06  伯克利与选择行为 (1964–1977) — 联结经济理论与测量的研究纲领
07  条件 logit 的诞生 (1974)（核心贡献页）— 离散选择分析的条件 logit 方法
08  离散选择的理论与方法 — 诺奖理由展开：从个体选择到可估计模型
09  克拉克奖章与 MIT (1975–1991) — 1975 Clark Medal；1977 转往 MIT；1981 当选 NAS
10  重返伯克利 (1991–2011) — 创办 Econometrics Laboratory（经济学统计计算）
11  2000 诺贝尔经济学奖 — 与 Heckman 共享、理由分立（discrete choice vs selective samples）、
    诺奖演讲 Economic Choices（2000-12-08）
12  USC 与健康经济学 (2011– ) — Presidential Professor of Health Economics（经济系 + Price 政策学院联聘）
13  荣誉与认可 — Frisch Medal 1986、Nemmers Prize 2000、美国哲学学会 2006、NAS 1981、
    计量学会 Fellow、Guggenheim Fellow
14  遗产与结尾 — 从出行方式选择到健康政策的离散选择革命 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| **政治观点节禁写** | page.md "Political views" 一节（2024 年 16 位诺奖得主关于 Trump 政策的联名信）**禁写**；本页正文极短，勿为凑内容引入政治事件 |
| Nemmers 奖年份页内矛盾 | 正文作 "won the Erwin Plein Nemmers Prize in Economics in 2020"，而 infobox 与 External links 均作 **2000**——以 infobox 2000 为准（正文系笔误），陷阱表留档 |
| 拆分理由年份 | 2000 年理由按人拆分：本篇只引本人那条 "for his development of theory and methods for analyzing discrete choice"；介绍 Heckman 时并列对照其 "selective samples" 条，勿互换 |
| 师生两代诺奖 | 导师 Hurwicz 2007 获经济学诺奖——师生两代得主的叙事点，年份勿写错 |
| 博士生名单长 | infobox Doctoral students 十人全部入库（含 Hal Varian）；幻灯片页只列 3-4 位代表（如 Varian、Train、Rust、Diewert）防溢出 |
| 学位口径 | BS 是 **Physics**、PhD 是 **Behavioral Science (Economics)**，两者勿混；PhD 1962 年（入学五年后） |
| 论文名 | 博士论文 *Factor Substitution in the Economic Analysis of Production*（1962），勿与条件 logit 论文混写 |
| 全文无直接引语 | page.md 无英文原话引语，中文引号内禁写"原话"；获奖理由为官方 citation 可逐字引 |
| 机构变迁 | 明尼苏达→伯克利(1964)→MIT(1977)→伯克利(1991)→USC(2011，伯克利 Graduate School 荣衔并行)——五段勿错序 |
| 在世 | 1937 年生，在世，卒年留白 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| discrete choice | 离散选择 | 诺奖理由核心词，勿译"随机选择" |
| conditional logit analysis | 条件 logit 分析 | 1974 年提出的方法 |
| econometrics | 计量经济学 | infobox Fields 核心身份 |
| choice behavior | 选择行为 | 其研究纲领的联结点：经济理论与测量 |
| selective samples | 选择性样本 | Heckman 那一半获奖理由，对照用勿混 |
| John Bates Clark Medal | 克拉克奖章 | 1975 年获，两年一度的青年经济学家奖（勿写"每年"） |
| Frisch Medal | 弗里施奖章 | 1986 年获（计量学会） |
| behavioral science | 行为科学 | 其 PhD 学位口径 |
| Econometrics Laboratory | 计量经济学实验室 | 1991 年在伯克利创办 |
| logit | logit 模型 | 概率模型，0-1 之间的概率切分 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："觉醒"呼应其学术转折——从物理学的连续世界转向人类决策的离散世界，让经济学看见"选择"本身；也贴合 1974 年条件 logit 横空出世的突破时刻。
- **本地路径**：复制 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` 到 `economics/presentations/20th_century/Daniel_McFadden/Awaken.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
