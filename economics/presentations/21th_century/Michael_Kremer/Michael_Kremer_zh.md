# 经济学家立传提示词（Michael Kremer）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2019 年得主 Michael Kremer（迈克尔·克雷默）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Michael_Kremer/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Michael Robert Kremer（1964-11-12 生于美国纽约市，在世）
- **气质关键词**：**O 型环的洞察者、驱虫药的诺奖推手、从理论到公益的创新者**
- **诺奖获奖理由**（逐字引用，2019 三人共享）：
  > "for their experimental approach to alleviating global poverty"（表彰他们以实验性方法减轻全球贫困）
- **设计母题**：**O 型环（O-ring）**——挑战者号航天飞机因一个小密封圈失事；克雷默由此提出「复杂生产中每一步都必须正确，高技能工人互为互补」的理论；视觉隐喻为环环相扣的圆环链与其中一环的高亮断裂风险，呼应「小失效、大后果」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Michael_Kremer/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Michael_Kremer/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Michael_Kremer_zh`、`VIDEO_NAME=Michael_Kremer_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kremer 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | development economics | 发展经济学 | infobox Discipline；诺奖核心 | 封面、核心页 |
| 1 | health economics | 健康经济学 | infobox Discipline；驱虫/疫苗研究 | 研究页 |
| 2 | economic growth | 经济增长 | 博士论文主题与 O 型环理论 | 理论页 |
| 3 | randomized controlled trials | 随机对照试验 | 1998 肯尼亚驱虫 RCT 起步 | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Barro | Kremer ← 导师 | 哈佛博士导师（增长经济学，正文明载 supervised by） |
| advisor-student | Eric Maskin | Kremer ← 导师 | 哈佛博士导师之一 |
| advisor-student | Greg Mankiw | Kremer ← 导师 | 哈佛博士导师之一 |
| advisor-student | Edward Miguel | Kremer → 学生 | 博士生（infobox 明载），2004 驱虫 RCT 合作者 |
| advisor-student | Seema Jayachandran | Kremer → 学生 | infobox 明载 |
| advisor-student | Karthik Muralidharan | Kremer → 学生 | infobox 明载，缺勤研究合作者 |
| advisor-student | Nava Ashraf | Kremer → 学生 | infobox 明载 |
| advisor-student | Benjamin Olken | Kremer → 学生 | infobox 明载 |
| advisor-student | Dina Pomeranz | Kremer → 学生 | infobox 明载 |
| advisor-student | Emily Oster | Kremer → 学生 | infobox 明载 |
| advisor-student | Asim Ijaz Khwaja | Kremer → 学生 | infobox 明载 |
| co-honored | Abhijit Banerjee | 无向 | 2019 三人共享（实验性方法减轻全球贫困） |
| co-honored | Esther Duflo | 无向 | 2019 三人共享（实验性方法减轻全球贫困） |
| spouse | Rachel Glennerster | 无向 | 妻·发展经济学家，J-PAL 首任主管/CGD 主席 |
| colleague | Susan Athey | 无向 | 加速健康技术小组（COVID 疫苗咨询）共同成员 |
| colleague | Jonathan Levin | 无向 | 加速健康技术小组共同成员 |

**不入库但提示词可叙述**：Charles Morcom（象牙囤积论文唯一合著，一次性合作）；Jeffrey Hammer/Halsey Rogers/Nazmul Chaudhury（缺勤研究合著者群）；Christopher Tucker（AMC 2020 工作论文合著）；Bob Day（核心选择拍卖外的合著，载于 Milgrom 页不适用本篇）；WorldTeach 共同创立（机构事件）；Amartya Sen/Chris Blattman/Edward Miguel 的评价引语（评论者非关系）。

## 五、配色方案 【人物专属】

- **气质**：机制的、公益的、环环相扣的严谨
- **主色**：`#1E3A5F`（manifest 预分配·机制深蓝，与 2019 三人共享组同色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeO` O 型环理论 — 深蓝 `#1E3A5F`
  - `badgeHealth` 健康与驱虫 — 青绿 `#1B6B5A`
  - `badgeAMC` 疫苗市场承诺 — 琥珀 `#B07A2A`
  - `badgeDeworm` 创新与公益 — 玫瑰 `#A3455A`
- **背景母题**：相扣圆环链（一环高亮），呼应 O 型环「互补性与小失效大后果」与驱虫RCT「小投入大外溢」的双重意象。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — O 型环的洞察者 / Michael Kremer 1964– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒纽约、哈佛 AB 1985/PhD 1992、
    UChicago 大学教授、诺奖 2019、核心领域）
03  核心贡献概览 — O 型环理论 / 驱虫 RCT / 疫苗预先市场承诺 / 发展创新实验
04  早年：堪萨斯的少年大学生 (1964–1985) — 五年级旁听堪萨斯州立、高中提前一年入哈佛
05  肯尼亚教书与 WorldTeach (1985–1986) — 忘买卫生纸的轶事与 O 型环灵感的伏笔
06  哈佛博士：三导师与 Wells 奖 (1986–1992) — Barro/Maskin/Mankiw，论文 Two Essays on Economic Growth
07  O 型环理论（核心贡献页）— 挑战者号隐喻、技能互补、人才外流与跨国工资差距
08  人口与技术：从一百万年前到 1990 — QJE 1993 著名论文
09  驱虫实验：RCT 的开端（核心贡献页）— 1998 肯尼亚、2004 Econometrica、缺勤率降 25%
10  Deworm the World 与 PxD — 18 亿剂次治疗、短信农业建议增产 8%
11  疫苗预先市场承诺 AMC — 与 Glennerster 合著 Strong Medicine、15 亿美元承诺、1.5 亿儿童接种
12  2019 诺贝尔奖 — 三人共享、奖金捐 Weiss Fund、诺奖演讲 Experimentation, Innovation, and Economics
13  荣誉与角色 — MacArthur 1997、NAS 2020、USAID DIV、2026 世界银行首席经济学家
14  遗产与结尾 — 实验方法主导发展经济学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三位博士导师 | 正文明载 dissertation supervised by Robert Barro, Eric Maskin, Greg Mankiw 三人；metadata.json 只载前两位——按 page.md 三人全收 |
| O 型环命名 | 得名于挑战者号航天飞机失事的 O 型密封圈，是**理论隐喻**，勿写成他研究航天工程 |
| 驱虫研究外溢 | 2004 Econometrica 与 Miguel 合著；2021 PNAS 二十年随访第一作者是 Hamory（Kremer 列第四）——勿写成 Kremer-Miguel 双人署名 |
| Duflo 合著论文 | 肥料使用研究（2008/2011 AER）与追迹研究（2011 AER）是 Kremer-Duflo 合著线——叙述可写，关系边已有 co-honored 不另建 |
| 缺勤研究分工 | 教师缺勤 25%/健康工作者缺勤 35% 是与 Muralidharan/Hammer/Rogers/Chaudhury 的合作——合著者仅 Muralidharan 是其学生，其余不入库 |
| 授予时点表述 | 2020 年诺奖得主意指其 2019 年获奖——所有"2020 获诺奖"表述禁用，统一 2019 |
| 世界银行任命 | page.md 载 2026-09 宣布、2026-10-01 就任世界银行首席经济学家——时间口径写"2026 年 10 月就任" |
| 政治敏感 | Operation Warp Speed/美国政府咨询段仅客观一句，不展开美国政治评价；Duflo 页 BJP 段与本篇无关 |
| 诺奖捐赠 | 三人将奖金捐给芝加哥大学 Weiss Fund——Kremer 页明载，**只有本篇可写**（Banerjee/Duflo 页无载） |
| 引语红线 | Duflo 评语 "was there from the very beginning... He is a visionary"、Sen 评语、Kremer 捐赠说明均有英文原文，引原文+译文；Weber 式转述不得加引号 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| O-ring theory of economic development | 经济发展 O 型环理论 | 挑战者号隐喻，勿直译"橡胶圈" |
| deworming | 驱虫 | 研究主线，勿译"除虫/打虫"口语化 |
| advance market commitment (AMC) | 预先市场承诺 | 疫苗采购机制，勿译"预付市场" |
| randomized controlled trials (RCT) | 随机对照试验 | 获奖理由核心词 |
| WorldTeach | 世界教学（非营利组织） | 共同创立，保留英文名 |
| Development Innovation Ventures (DIV) | 发展创新风险投资 | USAID 项目，保留缩写 |
| Giving What We Can | 尽己所能捐赠 | 有效利他组织，保留英文名 |
| hold-up problem | 套牢问题 | AMC 理论术语 |
| human capital flight | 人才外流 | O 型环理论解释对象 |
| Strong Medicine | 《强效良药》 | 2004 与 Glennerster 合著，书名译法以通行译名为准 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：2019 三人共享组统一用曲；Mirage 的递进电子节拍贴合 Kremer「一个实验接一个实验推进」的渐进感——从肯尼亚教室的卫生纸轶事到 18 亿剂驱虫药与 15 亿美元疫苗承诺，是幻象（援助直觉）被实证逐步替换的过程。
- **本地路径**：复制 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` 到 `economics/presentations/21th_century/Michael_Kremer/Mirage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
