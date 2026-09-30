# 经济学家立传提示词（Eric Maskin）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2007 年得主 Eric Maskin（埃里克·马斯金）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Eric_Maskin/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Eric Stark Maskin（1950-12-12 生于纽约市，在世）
- **气质关键词**：**机制设计的实现大师、社会目标的工程师、博弈论的数学家**
- **诺奖获奖理由**（2007 与 Leonid Hurwicz、Roger Myerson 三人共享，逐字引用官方 citation）：
  > "for having laid the foundations of mechanism design theory"（表彰他们奠定了机制设计理论的基础）
- **设计母题**：**实施（implementation）**——社会目标作为输入、机制作为引擎、均衡结果作为输出：齿轮与流程图式的收敛结构，呼应「如何让自利行为达成社会既定目标」的核心问题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Eric_Maskin/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Eric_Maskin/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Eric_Maskin_zh`、`VIDEO_NAME=Eric_Maskin_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Maskin 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | mechanism design | 机制设计理论 | 诺奖理由核心词；infobox Notable ideas | 封面、核心页 |
| 1 | implementation theory | 实施理论 | 机制设计/实施理论论文尤其知名 | 核心页 |
| 2 | game theory | 博弈论 | infobox Discipline；动态博弈 | 核心页 |
| 3 | contract theory | 契约理论 | 激励经济学一翼 | 领域页 |
| 4 | social choice | 社会选择与选举方法 | 选举规则比较、Total Vote Runoff | 选举页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 9 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Kenneth Arrow | 师→生（博士导师） | 哈佛应用数学博士导师（infobox 明载） |
| advisor-student | Abhijit Banerjee | Maskin→学生 | infobox Doctoral students；2019 诺奖得主 |
| advisor-student | Michael Kremer | Maskin→学生 | infobox Doctoral students；2019 诺奖得主 |
| advisor-student | Robert W. Vishny | Maskin→学生 | infobox Doctoral students 明载 |
| co-honored | Leonid Hurwicz | 无向 | 2007 诺奖三人共享（奠定机制设计理论基础） |
| co-honored | Roger Myerson | 无向 | 2007 诺奖三人共享（奠定机制设计理论基础） |
| collaborator | Jean Tirole | 无向 | 共同提出 Markov perfect equilibrium；2014 诺奖得主 |
| collaborator | James Bessen | 无向 | 软件专利与创新实证论文合著者 |
| collaborator | Ned Foley | 无向 | 共同提出 Total Vote Runoff（Baldwin 法）选举方法 |

**不入库但提示词可叙述**：Elhanan Helpman（2026-06 接任国际经济学会主席，交接事件非持续关系）；Godfrey — 无；Jerusalem Summer School 任职机构；Infosys Prize 评审（2018）等委员会经历。

## 五、配色方案 【人物专属】

- **气质**：精密、工程感、社会目标的理性实现
- **主色**：`#175E54`（机制青——齿轮咬合般的深青绿，工程师的冷静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMech` 机制设计 — 机制青 `#175E54`
  - `badgeImpl` 实施理论 — 靛蓝 `#2A4B7C`
  - `badgeGame` 博弈与动态 — 砖红 `#8C3A2B`
  - `badgeVote` 社会选择 — 金棕 `#B08A2E`
- **背景母题**：齿轮组与输入-输出流程图（社会目标→机制→均衡），辅以收敛的映射箭头（实施理论的「目标=结果」）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 机制设计的实现大师 / Eric Maskin 1950– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年、出生地纽约、教育 Harvard BA 1972/AM 1974/PhD 1976、
    任职 MIT→Harvard→IAS→Harvard、诺奖 2007、核心领域）
03  核心贡献概览 — 机制设计/实施理论 / 动态博弈 / Markov 完美均衡 / 选举方法
04  早年与哈佛数学 (1950–1976) — 纽约犹太家庭、新泽西 Tenafly 中学、数学学士→应用数学博士、Arrow 门下
05  剑桥与 MIT (1976–1984) — Jesus College 研究员、1977 加入 MIT 教员
06  机制设计：让社会目标可实施（核心贡献页）— implementation theory 与激励相容路径
07  动态博弈与 Markov 完美均衡 — 与 Tirole 的概念推进
08  哈佛—普林斯顿高等研究院 (1985–2011) — Louis Berkman 讲席、IAS Hirschman 讲席、意大利央行国债拍卖顾问
09  重返哈佛 (2011–) — Adams University Professor、经济系与数学系双聘
10  学生与传承 — Banerjee/Kremer/Vishny：从机制设计到发展经济学的两代诺奖
11  软件专利之辩 — 与 Bessen 的实证：专利保护扩大后 R&D 强度未升（引原文）
12  选举方法研究 — Total Vote Runoff（与 Foley）、比较不同选举规则
13  荣誉与认可 — Nobel 2007（三人共享）· 国家科学奖章 · 计量学会主席 2003 · HEC 荣誉教授 · IEA 主席 2026
14  遗产与结尾 — 从社会选择到机制工程的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享同句理由 | 2007 与 Hurwicz、Myerson 共享，官方理由逐字 "for having laid the foundations of mechanism design theory"；勿写理由分立 |
| 学位学科 | BA 是**数学**（1972 Harvard College）、AM/PhD 是**应用数学**（1974/1976）——勿写"经济学博士"；infobox 荣誉还有 Harvard Centennial Medal |
| 对手方规范名 | 学生入库名：**Abhijit Banerjee / Michael Kremer**（2019 诺奖得主，batch-08 manifest 同名匹配）、**Robert W. Vishny**；导师 **Kenneth Arrow** 复用库内 id=2639 |
| Tirole 关系 | "With Jean Tirole, he advanced the concept of Markov perfect equilibrium"——合作推进概念，入库 collaborator；Tirole 是 2014 诺奖得主 |
| 政治红线 | 2024 年 16 位诺奖得主关于 Trump 的联名信属政治内容，**禁写入稿**；选举方法（Baldwin/Total Vote Runoff）是学术研究可写，但只述方法不涉美国党派立场 |
| 专利引语 | "patent protection may reduce overall innovation and social welfare" 与 Bessen 合著论文引文有英文原文，引原文+译文；"A natural experiment occurred in the 1980s" 句为主张转述，按 page.md 口径 |
| 无卒日 | 1950 年生、在世——封面写 1950–，身份页卒日留白；勿杜撰 |
| 机构顺序 | MIT（1977 加入教员）→ Harvard（1985–2000 Berkman 讲席）→ IAS Princeton（2000–2011）→ Harvard（2011– Adams 讲席）；1990s 意大利央行顾问勿漏 |
| 术语边界 | mechanism design 与 implementation theory 在其语境常并提（"mechanism design/implementation theory"），正文首次出现可注「机制设计/实施理论」 |
| metadata 冲突 | frontmatter 无卒日、与正文一致；educated_at 列含中小学为 Wikidata 噪声，正文口径为 Tenafly High School |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| mechanism design | 机制设计（理论） | 诺奖理由核心词，勿译"机制设计学" |
| implementation theory | 实施理论 | 目标与均衡结果一致的理论 |
| incentive compatibility | 激励相容 | 呼应 Hurwicz 首创概念 |
| Markov perfect equilibrium | 马尔可夫完美均衡 | 与 Tirole 共同推进 |
| dynamic games | 动态博弈 | 其博弈论一翼 |
| revelation principle | 显示原理 | 见 Myerson 篇，Maskin 篇按需提及 |
| social choice | 社会选择 | 选举规则比较的理论基础 |
| Total Vote Runoff | 总票数淘汰制 | 与 Foley 共同提出，Baldwin 法新名 |
| software patent | 软件专利 | 其批评立场按 page.md |
| Adams University Professor | 亚当斯大学教授 | 哈佛最高讲席之一，勿与 Berkman 混 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：沉稳、协同、陪伴感——机制设计本质是「为互动与协作设计规则」，"With Me" 的合奏感呼应博弈各方在机制下达成一致的主题；亦贴合三人共享诺奖的同行叙事。
- **本地路径**：复制 `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` 到 `economics/presentations/21th_century/Eric_Maskin/WithMe.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
