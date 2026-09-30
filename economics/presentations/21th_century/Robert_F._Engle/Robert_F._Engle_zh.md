# 经济学家立传提示词（Robert F. Engle）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2003 年得主 Robert F. Engle（罗伯特·恩格尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Robert_F._Engle/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert Fry Engle III（1942-11-10 生于纽约州雪城，在世）
- **气质关键词**：**ARCH 之父、波动聚集的测量者、风险管理的工程师**
- **诺奖获奖理由**（2003 为拆分理由年份，取**本人那条**，逐字引用）：
  > "for methods of analyzing economic time series with time-varying volatility (ARCH)"（表彰他提出了分析具有时变波动性的经济时间序列的方法（ARCH））
  - 来源：`economics/nobel_economics_citations.json` 2003 年 Robert F. Engle 条目；同句亦逐字载于本地 page.md 开篇（英文原文可引）；中译对照 `economics/economics_list_data.py` 2003 年 "||" 拆分**第一段**（官方获奖者顺序 Engle 在前、Granger 在后）
- **设计母题**：**波动聚集（volatility clustering）**——金融市场的平静与风暴交替出现：一条起伏的波动率条带，舒缓段与剧烈段相间，是「风险可以测量、风暴有迹可循」的视觉隐喻，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Robert_F._Engle/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Robert_F._Engle/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_F._Engle_zh`、`VIDEO_NAME=Robert_F._Engle_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至十二节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Engle 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | infobox Discipline；诺奖核心学科 | 封面、核心页 |
| 1 | financial econometrics | 金融计量经济学 | ARCH 与金融波动率建模 | 核心页 |
| 2 | time series analysis | 时间序列分析 | ARCH/ARCH-M/DCC 皆时间序列方法 | 核心页 |
| 3 | risk management | 风险管理 | 波动率模型的风险测度应用 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ta-Chung Liu | 师→生（博士导师） | 康奈尔经济学博士导师（1969），论文分布滞后模型时间聚合偏误 |
| influence | David Hendry | 无向 | infobox Influences 明载；1983《Exogeneity》合著 |
| co-honored | Clive Granger | 无向 | 2003 诺贝尔经济学奖共享（分析经济时间序列的方法） |
| colleague | Clive Granger | 无向 | UCSD 同事，1987 协整论文合著，联合指导 Mark Watson |
| advisor-student | Mark Watson | Engle → 学生 | 博士生（infobox 明载；与 Granger 联合指导） |
| advisor-student | Tim Bollerslev | Engle → 学生 | infobox Doctoral students 明载 |
| spouse | Marianne Eger | 无向 | 1969-08 结婚，岳母为心理学家 Edith Eger |

**不入库但提示词可叙述**：一女一子（正文不具名）；岳母 Edith Eger（著名临床心理学家、大屠杀幸存者，姻亲不入库）；Hendry/Richard、Lilien/Robins、O'Hara/Easley、Ng/Rothschild、Russell 等论文合著者（仅出版物列表列举，除 Hendry 已以 influence 收录外不逐一建边）。

## 五、配色方案 【人物专属】

- **气质**：脉动、警觉、风暴与平静的交替
- **主色**：`#52307C`（波动紫——平静与风暴交替的深邃底色；manifest 预分配，与同届共享得主 Granger 同色，同批撞色为 manifest 口径）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeARCH` ARCH 波动 — 波动紫 `#52307C`
  - `badgeRisk` 风险管理 — 深蓝 `#16324F`
  - `badgeCoint` 协整合作 — 青绿 `#0E7C7B`
  - `badgeVL` 系统性风险 V-LAB — 玫瑰红 `#C4204F`
- **背景母题**：一条横向起伏的波动率条带，舒缓段与风暴段相间，风暴段以主色渐变加深，呼应「波动聚集」的核心发现。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — ARCH 之父 / Robert F. Engle 1942– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地雪城、Williams 物理学士、Cornell 物理 MS 1966/
    经济 PhD 1969、MIT → UCSD 1975–2003 → NYU Stern 2000–、诺奖 2003、核心领域）
03  核心贡献概览 — ARCH / 协整（与 Granger 合作）/ ARCH-M 与 DCC / V-LAB
04  贵格家庭与物理起点 (1942–1966) — 雪城出生、贵格家庭、Williams College 物理学士
05  康奈尔转向经济学 (1966–1969) — 物理 MS → 经济 PhD、Liu 门下、时间聚合偏误论文
06  MIT 与 UCSD (1969–2003) — 教职迁徙、1975 加入 UCSD、2003 荣休（教授荣休+研究教授）
07  ARCH：时变波动的发现（核心贡献页）— 1982 Econometrica 论文、英国通胀方差估计、波动聚集
08  风险管理的革命 — 期权与衍生品定价、套利定价理论的必备工具（page.md 口径）
09  协整合作与学术共同体 — 与 Granger 1987 论文、Mark Watson 联合指导
10  NYU Stern 岁月 (2000– ) — Michael Armellino 讲席、高级管理人员风险管理理学硕士项目
11  V-LAB 与系统性风险 — Volatility Institute 创始人与主任、每周跨国系统性风险数据
12  2003 诺贝尔经济学奖 — 与 Granger 共享、理由按人拆分（本篇用 ARCH 条）
13  荣誉与认可 — 计量学会会士、ASA 会士、AAAS 会士、Fisher-Schultz Lecture、多校荣誉博士（2024 Comillas 等）
14  遗产与结尾 — 波动率建模成为金融风险管理标准工具 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 拆分理由年份 | 2003 理由按人拆分：本篇只用 Engle 条（time-varying volatility/ARCH），**禁用** Granger 条（common trends/cointegration）；该句英文原文 page.md 开篇逐字有载，可加引号直引 |
| MIT/UCSD 年代两说 | infobox 机构年份 MIT 1969–1975、UCSD 1975–2003；正文 Biography 却作 MIT 1969–1977 且 1975 加入 UCSD，自相重叠。幻灯片按 **infobox 年份**（MIT 1969–1975 / UCSD 1975–2003），陷阱表留痕 |
| ARCH 拼写双形 | 1982 论文题作 *Heteroscedasticity*，infobox Notable ideas 链接作 *Heteroskedasticity*，两种拼写并存；标题引原文用 sced 拼法 |
| ARCH 与协整的获奖归属 | 诺奖理由仅 ARCH 属 Engle；协整是 **Granger 条**获奖理由（两人 1987 合著），叙述合作时可写、勿把协整写成 Engle 的获奖理由 |
| 博士论文题 | 《Biases From Time-Aggregation of Distributed Lag Models》（1969），勿与 ARCH 论文混淆 |
| 在世口径 | 1942 年生在世：封面写 1942–，身份页卒年留白，全文勿写卒年 |
| 名字后缀 | 全名 Robert Fry Engle III，「III」后缀非笔误，身份页用全名 |
| 岳母 Edith Eger | 正文有载（临床心理学家、《The Gift》作者身份按 page.md 口径、大屠杀幸存者）；姻亲不入库，幻灯片至多一句带过 |
| 子女不具名 | 一女一子，正文不具名，禁写具名细节 |
| 国籍口径 | United States 单一国籍（manifest 与 frontmatter 一致） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| ARCH (Autoregressive Conditional Heteroskedasticity) | 自回归条件异方差 | 获奖理由核心模型 |
| time-varying volatility | 时变波动性 | 获奖理由用词 |
| volatility clustering | 波动聚集 | 高低压期交替的现象 |
| ARCH-M | 均值 ARCH | 1987 期限结构风险溢价模型 |
| Dynamic Conditional Correlation | 动态条件相关 | 2002 多元 GARCH 类模型 |
| systemic risk | 系统性风险 | V-LAB 发布口径 |
| arbitrage pricing theory | 套利定价理论 | page.md 明载的应用域 |
| risk management | 风险管理 | 模型的实践出口 |
| GARCH 家族 | 广义 ARCH 族 | page.md 仅一句提及，勿展开成段 |
| interest rates | 利率 | page.md 明载的 ARCH 建模对象之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：波动是时间的形状——市场在平静与风暴间流转，ARCH 恰是给「时间的节律」建模的工具；流动的曲风贴合「测量时间中的风险」这一叙事。
- **本地路径**：复制 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` 到 `economics/presentations/21th_century/Robert_F._Engle/TheFlowOfTime.wav`
- **撞曲注记**：同届共享得主 Clive Granger 同曲（manifest 同批预分配）；若出片阶段需去重，由主控统一裁定。
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Robert_F._Engle/page.md` | 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Robert_F._Engle/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Robert_F._Engle/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一封面 |
| `economics/nobel_economics_citations.json` | 拆分理由英文原文 |
| `economics/economics_list_data.py` | 拆分理由中译对照（2003 年 "||" 第一段） |

## 十一、执行清单 【模板通用】

1. 通读本提示词与 page.md，建立事实卡（生卒/学位/机构/奖项/关系五组）。
2. 下载肖像（images.txt 或 Commons `Special:FilePath`，500px；404 则装饰圆占位）。
3. 复制 Makefile，设 `MAIN=Robert_F._Engle_zh`、`VIDEO_NAME=Robert_F._Engle_zh`；复制 BGM wav。
4. 按 §六逐页写 Beamer tex；每页 `make` 检查溢出（vbox≤10pt、hbox≤50pt）。
5. `make pdf` 0 error → `pdftoppm` 逐页目检 → `make images && make video` 出 mp4。
6. 数据库已由本批次入库（has_social_data=1），立传完成后由主控将 has_biography 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`；公式框前 −0.35~−0.55cm。
- 文本模式希腊字母需数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- 引号用半角 `" "`；品牌口径统一 `OpenMathAI`；`\foreach` 分隔符用 ASCII 逗号。
- 结尾页底部标注 GitHub 链接由首页模板 `\input` 继承，子 deck 不重复。
