# 经济学家立传提示词（Leonid Hurwicz）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2007 年得主 Leonid Hurwicz（莱昂尼德·赫维奇）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Leonid_Hurwicz/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Leonid Hurwicz（1917-08-21 生于莫斯科 ~ 2008-06-24 逝于明尼阿波利斯，享年 90 岁）
- **气质关键词**：**激励相容的创始人、机制设计之父、90 岁圆梦的最年长诺奖得主**
- **诺奖获奖理由**（2007 与 Eric Maskin、Roger Myerson 三人共享，逐字引用官方 citation）：
  > "for having laid the foundations of mechanism design theory"（表彰他们奠定了机制设计理论的基础）
- **设计母题**：**激励相容（incentive compatibility）**——个体自利的小齿轮与社会目标的大齿轮相互咬合、误差归零的传动结构；辅以跨越半个世纪的等待钟面（1917→2007）呼应「最年长得主」的传奇。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Leonid_Hurwicz/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Leonid_Hurwicz/`（含 page.md / page.html / metadata.json / images.txt，肖像用 Commons `Leonid_hurwicz_1985.jpg`，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Leonid_Hurwicz_zh`、`VIDEO_NAME=Leonid_Hurwicz_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hurwicz 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | mechanism design | 机制设计理论 | 诺奖理由核心词；1959/1960/1973 奠基论文 | 封面、核心页 |
| 1 | incentive compatibility | 激励相容 | 其首创概念，改变经济学家的结果观 | 核心页 |
| 2 | game theory | 博弈论 | 最早 recognize 其价值的经济学家之一 | 核心页 |
| 3 | mathematical economics | 数理经济学 | 非线性规划、资源配置过程 | 领域页 |
| 4 | welfare economics | 资源配置与福利经济学 | 其最乐见机制设计的应用领域 | 领域页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 23 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jacob Marschak | 师→生 | Cowles Commission 时期导师（1942，正文明载） |
| advisor-student | Tjalling Koopmans | 师→生 | Cowles Commission 时期导师；1950–51 曾代其授课 |
| influence | Friedrich Hayek | 无向 | infobox Influences；LSE 求学时期随其学习 |
| influence | Nicholas Kaldor | 无向 | LSE 求学时期随其学习（studied with） |
| colleague | Paul Samuelson | 无向 | 1941 MIT 任其研究助理 |
| colleague | Oskar Lange | 无向 | 1941 芝加哥大学任其研究助理 |
| collaborator | Kenneth Arrow | 无向 | 1950s 非线性规划合作；1978 合编《Studies in Resource Allocation Processes》 |
| colleague | Walter Heller | 无向 | 1951 招募其加盟明尼苏达大学 |
| collaborator | Roy Radner | 无向 | 1975 Econometrica 论文合著者 |
| advisor-student | Clifford Hildreth | Hurwicz→学生 | infobox Doctoral students 明载 |
| advisor-student | Stanley Reiter | Hurwicz→学生 | infobox Doctoral students 明载 |
| collaborator | Stanley Reiter | 无向 | 2001《Review of Economic Design》合著、2008《Designing Economic Mechanisms》合著 |
| advisor-student | Daniel McFadden | Hurwicz→学生 | graduate advisor 明载；2000 诺奖得主 |
| advisor-student | Richard B. McHugh | Hurwicz→学生 | infobox Doctoral students 明载 |
| advisor-student | Leigh Tesfatsion | Hurwicz→学生 | infobox Doctoral students 明载 |
| advisor-student | Myrna Wooders | Hurwicz→学生 | infobox Doctoral students 明载 |
| collaborator | David Schmeidler | 无向 | 1987《Social Goals and Social Organization》合编者 |
| collaborator | Hugo Sonnenschein | 无向 | 1987《Social Goals and Social Organization》合编者 |
| spouse | Evelyn Jensen | 无向 | 1944-07-19 结婚；妻 2016 卒（93 岁） |
| parent-child | Sarah Hurwicz | Hurwicz→子女 | 四子女之一（page.md 正文具名） |
| parent-child | Michael Hurwicz | Hurwicz→子女 | 四子女之一（page.md 正文具名） |
| parent-child | Ruth Hurwicz | Hurwicz→子女 | 四子女之一（page.md 正文具名） |
| parent-child | Maxim Hurwicz | Hurwicz→子女 | 四子女之一（page.md 正文具名） |

**不入库但提示词可叙述**：John Forbes Nash（正文只说机制设计应用了 Nash 推进的博弈论，属学术史叙述非直接关系；库内另有 Nash 三条分裂记录，**一律勿建边**）；Thomas Marschak / Marcel K. Richter（单篇论文合著者，存档不入库防噪声）；Scott E. Page（持有以其命名的密歇根讲席，本人非其学生，关系见 Myerson 篇）；Robert Bruininks / Jonas Hafström（授奖仪式人物）。

## 五、配色方案 【人物专属】

- **气质**：典雅、坚韧、跨越世纪的思想长跑
- **主色**：`#175E54`（机制青——与 Maskin/Myerson 同届共享色系，齿轮咬合的深青绿）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMech` 机制设计 — 机制青 `#175E54`
  - `badgeInc` 激励相容 — 金棕 `#B08A2E`
  - `badgeAlloc` 资源配置 — 靛蓝 `#2A4B7C`
  - `badgeLife` 流亡与明尼苏达 — 砖红 `#8C3A2B`
- **背景母题**：大小齿轮咬合（个体激励与社会目标传动），辅以一根从 1917 华沙延伸到 2007 斯德哥尔摩（明尼阿波利斯受奖）的长针钟面。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 激励相容的创始人 / Leonid Hurwicz 1917–2008 + 四色 badge + 右上头像 + 国籍行（Poland / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、生于莫斯科的波兰犹太家庭、华沙大学 LL.M. 1938、
    无经济学学位、任职 Iowa State→Minnesota 1951–、诺奖 2007、核心领域）
03  核心贡献概览 — 机制设计 / 激励相容 / 信息分散化 / 决策准则
04  战火中的求学路 (1917–1940) — 华沙、十月革命前夕出生、1939 逃亡伦敦→瑞士→葡萄牙→1940 美国
05  Cowles 岁月 (1941–1951) — Samuelson/Lange 门下研究助理、Marschak/Koopmans 导师、Iowa State 副教授
06  机制设计的诞生（核心贡献页）— 1959 "Optimality and Informational Efficiency"、1960/1973 论文
07  激励相容（核心贡献页）— 首创概念：为什么中央计划经济可能失灵、个体激励如何改变决策
08  明尼苏达六十年 (1951–2008) — Heller 招募、Regents Professor 1969、Carlson 讲席 1989、荣誉退休后仍执教至 2006
09  与 Arrow 的合作 — 非线性规划、1978 合编文集
10  Hurwicz 准则 (1950) — Wald+Laplace 综合、悲观-乐观指数；Savage 1954 修正
11  门生与传承 — McFadden（2000 诺奖）等六位 infobox 博士生、Reiter 合著传承
12  90 岁的诺贝尔时刻 — 2007-10 电话、明尼阿波利斯受奖（健康原因未赴斯德哥尔摩、瑞典大使亲自颁发）
13  荣誉与认可 — National Medal of Science 1990 · 计量学会主席 1969 · NAS 1974 · 六个名誉博士
14  遗产与结尾 — Heller-Hurwicz Economics Institute 2010、从机制到制度 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享同句理由 | 2007 与 Maskin、Myerson 共享，官方理由逐字 "for having laid the foundations of mechanism design theory"；勿写理由分立 |
| 导师口径 | **无经济学博士学位**（华沙 LL.M. 1938）；Marschak/Koopmans 是 Cowles Commission 时期 advisors（正文 "About 1942 his advisors were..."），infobox 归 Influences——**裁定：入库 advisor-student 并在 note 注明 Cowles 时期导师**，防 Review 误判；Hayek/Kaldor 入 influence |
| 年龄之最 | 2007 获奖时 90 岁，**当时最年长诺奖得主**（诺奖基金会电话告知表述）；2008-06-24 卒于肾衰竭，享年 90；勿写"迄今最年长"绝对化 |
| 受奖方式 | 因健康未赴斯德哥尔摩，在明尼苏达大学校园受奖、瑞典大使 Jonas Hafström 亲自颁发——勿写"亲赴斯德哥尔摩领奖" |
| 引语红线 | "Whatever economics I learned I learned by listening and learning."（2007 自述）与 "I hope that others who deserve it also got it." 均有英文原文，引原文+译文 |
| 政治红线 | 1968 年任 McCarthy 代表与民主党纲领委员会成员、walking subcaucus 方法——仅一句客观带过，**禁展开党派立场**；布尔什维克/纳粹迫害与父母劳改营经历按 page.md 客观历史叙述、不作评价 |
| 子女入库 | 四子女 Sarah/Michael/Ruth/Maxim 为 page.md 正文具名，入库 parent-child（note 注明"正文具名"防 Review 误判）；妻 Evelyn Jensen 卒于 2016（93 岁），与 Hurwicz 卒年 2008 并存勿混 |
| Nash 勿建边 | 正文 "a field advanced by mathematician John Forbes Nash" 属学术史叙述，**不入库**；库内 Nash 有三条分裂记录（205/429/967），本篇一律不建边 |
| 机构线 | Warsaw LL.M. 1938 → LSE → Geneva → 1941 MIT/Chicago 研究助理 → Cowles 1942–46 → Iowa State 1946 → Minnesota 1951–（1959 斯坦福发表机制设计论文）；访问教授多地勿漏 1965 班加罗尔与 1980s 东京/人大/印尼 |
| metadata 冲突 | frontmatter nationality 列 United States/Poland 顺序与 infobox Citizenship（Poland-United States）相反——按 manifest "Poland / United States" 口径；生卒 frontmatter 与正文一致 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| mechanism design | 机制设计（理论） | 诺奖理由核心词；其 1973 论文标题用 "design of mechanisms" |
| incentive compatibility | 激励相容 | 其首创概念，勿写成他人提出 |
| informational decentralization | 信息分散化 | 1969 论文核心 |
| Hurwicz criterion | 赫维茨准则 | 1950 不确定性决策，α 悲观-乐观指数 |
| resource allocation process | 资源配置过程 | 1959/1960 论文语境 |
| non-linear programming | 非线性规划 | 与 Arrow 1950s 合作方向 |
| incentive-compatible mechanism | 激励相容机制 | 机制设计基本构件 |
| Regents' Professor | 校董教授 | 明尼苏达最高教职之一，1969 |
| walking subcaucus | 行进式分组党代会方法 | 1968 政治经历中一笔带过 |
| Fisher-Schultz Lecture | 费希尔-舒尔茨讲座 | 1963 年其主讲，计量学会 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：温暖、陪伴、终得回响——"With Me" 的同行感对应与妻 Evelyn 相伴六十年、明尼苏达校园里全家见证受奖的画面；90 岁圆梦的迟来荣光在温柔旋律中落定。
- **本地路径**：复制 `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` 到 `economics/presentations/21th_century/Leonid_Hurwicz/WithMe.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
