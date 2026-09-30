# 经济学家立传提示词（Thomas J. Sargent）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2011 年得主 Thomas J. Sargent（托马斯·萨金特）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Thomas_J._Sargent/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Thomas John Sargent（1943-07-19 生于加州帕萨迪纳，在世）
- **气质关键词**：**理性预期的旗手、新古典宏观的建造者、递归经济学的传道人**
- **诺奖获奖理由**（2011，与 Christopher A. Sims 共享；逐字引自 manifest）：
  > "for their empirical research on cause and effect in the macroeconomy"（表彰他们对宏观经济中因果关系的实证研究）
- **设计母题**：**递归与预期（recursion & expectations）**——个体在模型里预测模型自身：嵌套的递归框与收敛螺旋构成「学习收敛于理性预期」的视觉隐喻，对应其适应性学习与自我确认均衡的研究。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Thomas_J._Sargent/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Thomas_J._Sargent/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Thomas_J._Sargent_zh`、`VIDEO_NAME=Thomas_J._Sargent_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Sargent 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | rational expectations | 理性预期 | 革命领导者之一，2011 诺奖工作的根基 | 核心页 |
| 1 | macroeconomics | 宏观经济学 | 新古典宏观经济学的演进（与 Lucas/Wallace 紧密合作） | 核心页 |
| 2 | monetary economics | 货币经济学 | 政策工具与规则、恶性通胀研究 | 货币页 |
| 3 | time series econometrics | 时间序列计量 | 使理性预期在统计上可操作 | 方法页 |
| 4 | robust control | 鲁棒控制 | 与 Hansen 合作拓展至决策者不信任自身模型的情形 | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致；共 21 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John R. Meyer | Sargent → 学生 | 哈佛博士导师（1968），论文为利率期限结构 |
| co-honored | Christopher A. Sims | 无向 | 2011 诺贝尔经济学奖共享（宏观因果关系实证研究）；哈佛同窗 |
| influence | John Muth | 无向 | 理性预期的引入者（库内规范名 John Muth） |
| influence | Robert E. Lucas, Jr. | 无向 | 紧密合作者与影响者，新古典宏观共同演进 |
| collaborator | Neil Wallace | 无向 | 1975 政策无效性命题、多篇合著 |
| collaborator | Lars Peter Hansen | 无向 | 鲁棒控制与模型不确定性系列合作 |
| collaborator | Lars Ljungqvist | 无向 | 合著 Recursive Macroeconomic Theory、欧美失业比较研究 |
| advisor-student | Robert Litterman | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Monika Piazzesi | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Mariacristina De Nardi | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Ellen McGrattan | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Albert Marcet | Sargent → 学生 | 博士生，最小二乘学习机制合作者 |
| advisor-student | Noah Williams | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Laura Veldkamp | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Richard Clarida | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Danny Quah | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Sagiri Kitao | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Martin Eichenbaum | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Lawrence J. Christiano | Sargent → 学生 | 博士生（infobox 明载） |
| advisor-student | Greg Kaplan | Sargent → 学生 | 博士生（infobox 明载） |

**不入库但提示词可叙述**：Edward C. Prescott（正文明载其把理性预期「推向更远」，但无直接合作/师承表述，禁建边）；同窗关系已并入 co-honored 行 note；2011 CME Group-MSRI 奖、QuantEcon 项目等均非人物关系。

## 五、配色方案 【人物专属】

- **气质**：理性、克制、结构感极强
- **主色**：`#2F5D50`（计量松绿，与 Sims 篇同色系以呼应共享年份）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRE` 理性预期 — 青绿 `#2F5D50`
  - `badgeNC` 新古典宏观 — 靛蓝 `#1E3A5F`
  - `badgeRobust` 鲁棒控制 — 琥珀 `#C07A2A`
  - `badgeTeach` 递归与教育 — 灰紫 `#52307C`
- **背景母题**：嵌套递归框与收敛螺旋（适应性学习收敛于理性预期），呼应「递归」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 理性预期的旗手 / Thomas J. Sargent 1943– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、帕萨迪纳出身、Berkeley BA 1964 / 哈佛 PhD 1968、
    导师 John R. Meyer、Hoover 高级研究员、诺奖 2011、核心领域）
03  核心贡献概览 — 理性预期 / 政策无效性 / 鲁棒控制 / 递归宏观
04  早年与教育 (1943–1969) — Monrovia 高中、Berkeley 大学奖章、哈佛师从 Meyer、与 Sims 同窗、
    陆军上尉 1968–69
05  理性预期革命（核心贡献页一）— Muth 引入、Lucas/Prescott 推进、Sargent 使其可操作
06  与 Wallace 的合作 — 1975 政策无效性命题、货币与财政政策的跨期协调
07  历史与恶性通胀 — 四大恶性通胀终结的理性预期解读
08  鲁棒控制与学习（核心贡献页二）— 与 Hansen 合作的 robust control；有界理性与适应性学习收敛
09  递归经济学与教科书 — 与 Ljungqvist 合著 Recursive Macroeconomic Theory、欧美失业比较
10  门生与传承 — infobox 十四位博士生精选（Litterman / Piazzesi / Marcet / Clarida / Christiano 等）
11  荣誉与机构 — Nemmers 1996、NAS 1983、Hoover 1987 起、计量学会 Fellow 1976、AEA 会长
12  2011 斯德哥尔摩 — 与 Sims 共享、诺奖演讲 United States Then, Europe Now
13  短句大师 — 335 词毕业致辞、Ally Financial 广告一句 No（页面明载原文可引）
14  遗产与结尾 — QuantEcon 开源项目、北大汇丰 SIQEF + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由归属 | 2011 与 Sims 共享同一句 "for their empirical research on cause and effect in the macroeconomy"，勿写单人专属措辞 |
| 机构口径（页内两说） | 正文开头称 Wharton Rowan 讲席教授，又写 NYU 教授（2002 起）、infobox 兼列两者——幻灯片按「NYU 2002 起 + 现任 Wharton Rowan 讲席 + 北大汇丰 SIQEF 主管」并存口径，勿判其一 |
| 理性预期归属链 | Muth 引入 → Lucas/Prescott 推向更远 → Sargent 与 Lucas/Wallace 紧密合作完成新古典宏观；Sargent 是「领导者之一」，勿写「创始人」；Prescott 无直接合作表述禁建边 |
| 与 Sims 关系 | 哈佛同窗 + 2011 共享得主，建一条 co-honored 即可（note 内提同窗），勿再加 influence/colleague 重复边 |
| 学生名单 | infobox 十四人全收；其中 Hansen 与 Sims 篇学生边互为镜像（各自页面明载，双师承并存勿删） |
| 对手方规范名 | Muth 用库内形式 John Muth（勿写 John F. Muth）；Lucas 用 Robert E. Lucas, Jr.（infobox 形式）；Sims 用 Christopher A. Sims |
| 军旅经历 | 1968–69 服役美国陆军（first lieutenant/captain），infobox 与正文均载，时间线可写 |
| 引语红线 | 「No.」广告答句与 335 词致辞均页面明载英文原文，引语框引原文+译文；"Europe has stronger employment protection..." 引文照录，勿改写 |
| 政治边界 | Hoover Institution 仅作机构任职客观记录，禁任何政治评价与联想 |
| 诺奖演讲 | 2011-12-11 题为 United States Then, Europe Now，勿与 Sims 演讲题混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| rational expectations | 理性预期 | 获奖工作根基，Muth 引入 |
| policy-ineffectiveness proposition | 政策无效性命题 | 1975 与 Wallace 提出 |
| new classical macroeconomics | 新古典宏观经济学 | 与 Lucas/Wallace 共同演进 |
| robust control | 鲁棒控制 | 与 Hansen 合作的方向 |
| self-confirming equilibrium | 自我确认均衡 | 比理性预期更弱的概念 |
| bounded rationality / adaptive learning | 有界理性/适应性学习 | 收敛于理性预期的条件 |
| recursive economics | 递归经济学 | Sargent 开创性引入 |
| time series econometrics | 时间序列计量 | 使理性预期可操作 |
| term structure of interest rates | 利率期限结构 | 博士论文主题 |
| hyperinflation | 恶性通胀 | 四大恶性通胀历史研究 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgy**（manifest 预分配，与 Sims 篇同曲以呼应共享年份；音乐库 `music_audio/`）
- **匹配理由**：Sargent 的研究反复回望历史——四大恶性通胀、政策体制的剧烈变迁、欧美失业三十年的对照；「怀旧/回望」的曲意贴合其「历史即实验室」的方法论气质，也与同窗 Sims 篇形成共享年份的音乐呼应。
- **本地路径**：复制 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav` 到 `economics/presentations/21th_century/Thomas_J._Sargent/Nostalgy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
