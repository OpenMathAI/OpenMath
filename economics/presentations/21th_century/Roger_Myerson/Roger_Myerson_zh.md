# 经济学家立传提示词（Roger Myerson）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2007 年得主 Roger Myerson（罗杰·迈尔森）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Roger_Myerson/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Roger Bruce Myerson（1951-03-29 生于波士顿，在世）
- **气质关键词**：**显示原理的拓展者、最优拍卖的设计师、政治制度的博弈分析师**
- **诺奖获奖理由**（2007 与 Leonid Hurwicz、Eric Maskin 三人共享，逐字引用官方 citation）：
  > "for having laid the foundations of mechanism design theory"（表彰他们奠定了机制设计理论的基础）
- **设计母题**：**真实显示（truthful revelation）**——把复杂规制与拍卖环境化归为激励相容的直接机制：多条输入路径收束到一条「真话通道」，构成「让知情者自愿说真话」的视觉隐喻。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Roger_Myerson/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Roger_Myerson/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Roger_Myerson_zh`、`VIDEO_NAME=Roger_Myerson_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Myerson 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | mechanism design | 机制设计理论 | 诺奖理由核心词；infobox Notable ideas | 封面、核心页 |
| 1 | auction theory | 拍卖理论 | 1981《Optimal Auction Design》经典 | 核心页 |
| 2 | game theory | 博弈论 | infobox Discipline；1991 教科书 | 核心页 |
| 3 | revelation principle | 显示原理 | 拓展至不完全信息环境 | 理论页 |
| 4 | political institutions | 政治制度的经济学分析 | 民主制度、选举制度比较 | 制度页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 8 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Kenneth Arrow | 师→生（博士导师） | 哈佛应用数学博士导师（infobox 明载） |
| advisor-student | Scott E. Page | Myerson→学生 | infobox Doctoral students 明载 |
| advisor-student | Leonard Wantchekon | Myerson→学生 | infobox Doctoral students 明载 |
| co-honored | Leonid Hurwicz | 无向 | 2007 诺奖三人共享（奠定机制设计理论基础） |
| co-honored | Eric Maskin | 无向 | 2007 诺奖三人共享（奠定机制设计理论基础） |
| spouse | Regina Weber | 无向 | 1980 结婚（née Weber） |
| parent-child | Daniel Myerson | Myerson→子女 | 子（page.md 正文具名） |
| parent-child | Rebecca Myerson | Myerson→子女 | 女，威斯康星大学麦迪逊分校健康经济学家（正文具名） |

**不入库但提示词可叙述**：Satterthwaite（Myerson–Satterthwaite 定理以二人命名，但 page.md 未明载合作细节，**禁建边**）；Hurwicz 纪念讲座（2006 年 Econometric Society 北美会议 "Fundamental Theory of Institutions"，致敬事件非关系边）；Peter Thiel 的 Dialog 组织名录（仅一句提及，不入库不展开）。

## 五、配色方案 【人物专属】

- **气质**：锐利、分析性、直指机制内核
- **主色**：`#175E54`（机制青——与 Hurwicz/Maskin 同届共享色系，2007 三人组统一底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMech` 机制设计 — 机制青 `#175E54`
  - `badgeAuct` 拍卖理论 — 靛蓝 `#2A4B7C`
  - `badgeGame` 博弈论 — 砖红 `#8C3A2B`
  - `badgeInst` 制度分析 — 金棕 `#B08A2E`
- **背景母题**：多条信息路径收束为一条「真话通道」的漏斗结构（显示原理），辅以拍卖钟与出价阶梯的抽象线条。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 显示原理的拓展者 / Roger Myerson 1951– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年、出生地波士顿、教育 Harvard AB/SM 1973/PhD 1976、
    任职 Northwestern 1976–2001→Chicago 2001–、诺奖 2007、核心领域）
03  核心贡献概览 — 机制设计基础 / 最优拍卖 / 显示原理拓展 / 政治制度分析
04  波士顿与哈佛数学 (1951–1976) — 犹太家庭、AB summa cum laude、应用数学 SM/PhD、Arrow 门下、
    博士论文《A Theory of Cooperative Games》
05  西北大学廿五载 (1976–2001) — Kellogg 商学院经济学教授，诺奖研究主要在此完成
06  显示原理的拓展（核心贡献页）— 不完全信息环境下复杂规制与拍卖环境化归为激励相容直接机制
07  最优拍卖设计 (1981)（核心贡献页）— Optimal Auction Design；拍卖理论的数学基础
08  博弈论教科书与精炼 (1978/1991) — Nash 均衡精炼、Game Theory: Analysis of Conflict
09  芝加哥岁月 (2001–) — David L. Pearson 全球冲突研究讲席、Harris 公共政策学院
10  政治制度的经济学分析 — 民主制度结构-行为-绩效、选举制度理论比较（1995/1999 综述）
11  荣誉与认可 — Nobel 2007（三人共享）· 美国艺术与科学院/NAS/美国哲学学会 2019 · 巴塞尔名誉博士 2002 ·
    Laffont Prize 2009
12  机制设计的现实回响 — 规制、拍卖（频谱）、投票、谈判定价的应用图谱（按 page.md 口径）
13  以 Myerson 命名 — Myerson–Satterthwaite 定理 / Myerson 机制 / Myerson ironing / Myerson value
14  遗产与结尾 — 从激励相容到制度工程 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享同句理由 | 2007 与 Hurwicz、Maskin 共享，官方理由逐字 "for having laid the foundations of mechanism design theory"；勿写理由分立；本页获奖贡献小节另述 "path-breaking contribution"（配置与货币转移的基本联系） |
| 学位学科 | AB/SM 1973 与 PhD 1976 均为**应用数学**（Harvard）——勿写"经济学博士"；AB 是 summa cum laude |
| Satterthwaite 禁建边 | Myerson–Satterthwaite 定理同名但 page.md 未载二人合作过程，**一律不入库**，仅概念页叙述 |
| 对手方规范名 | 导师 **Kenneth Arrow** 复用库内 id=2639；co-honored 用 **Leonid Hurwicz / Eric Maskin**（本批三人 yaml 互指零分裂）；学生 **Scott E. Page / Leonard Wantchekon** 新建 stub |
| 显示原理归属 | page.md 口径是 Myerson "extending the revelation principle to accommodate incomplete information"——**拓展者**而非首创者，勿写"发明显示原理" |
| 政治红线 | 2024 年 16 位诺奖得主关于 Trump 的联名信**禁写入稿**；占领伊拉克美国政策的批判性问题仅客观列出论文标题（2013 QJPS 等）、禁展开立场；"Stabilization Lessons from the British Empire" 仅列篇名 |
| 无卒日 | 1951 年生、在世——封面写 1951–，身份页卒日留白；勿杜撰 |
| 家庭 | 妻 Regina（née Weber）1980 结婚；子女 Daniel 与 Rebecca 具名入库，Rebecca 职业信息（UW-Madison 健康经济学家）可写入 note/叙述 |
| 机构线 | Northwestern Kellogg 1976–2001（诺奖研究主要在此）→ Chicago 2001–；1978–79 Bielefeld 访问、1985–86 与 2000–01 芝加哥访问教授——年份勿混 |
| metadata 冲突 | frontmatter field_of_work 含 probability theory（2005 教科书 Probability Models for Economic Decisions 支撑）；生卒 frontmatter 与正文一致 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| mechanism design | 机制设计（理论） | 诺奖理由核心词 |
| revelation principle | 显示原理 | 拓展至不完全信息是 Myerson 贡献 |
| incentive-compatible | 激励相容 | 呼应 Hurwicz 首创概念 |
| direct mechanism | 直接机制 | 化归的终点形态 |
| optimal auction design | 最优拍卖设计 | 1981 论文标题 |
| Myerson–Satterthwaite theorem | 迈尔森-萨特斯韦特定理 | 双人命名，合作细节 page.md 无载 |
| Myerson ironing | 迈尔森熨平法 | 以其命名的技术术语 |
| Bayesian equilibrium | 贝叶斯均衡 | 不完全信息博弈的均衡概念 |
| cooperative games | 合作博弈 | 博士论文主题（1976） |
| political institutions | 政治制度 | 其后期研究重心 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：理性、协同、秩序感——机制设计是「为多方互动谱写规则」，"With Me" 的协奏质感呼应博弈各方在机制下彼此确认的主题；2007 三人共享的同行叙事亦由此延续（与 Hurwicz/Maskin 同曲成组）。
- **本地路径**：复制 `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` 到 `economics/presentations/21th_century/Roger_Myerson/WithMe.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
