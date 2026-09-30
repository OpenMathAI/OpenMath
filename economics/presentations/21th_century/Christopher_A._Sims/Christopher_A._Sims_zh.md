# 经济学家立传提示词（Christopher A. Sims）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2011 年得主 Christopher A. Sims（克里斯托弗·西姆斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Christopher_A._Sims/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Christopher Albert Sims（1942-10-21 生于华盛顿特区 ~ 2026-03-14 逝于明尼阿波利斯，享年 83 岁）
- **气质关键词**：**VAR 的布道者、贝叶斯的旗手、货币政策的测绘师**
- **诺奖获奖理由**（2011，与 Thomas J. Sargent 共享；逐字引自 manifest）：
  > "for their empirical research on cause and effect in the macroeconomy"（表彰他们对宏观经济中因果关系的实证研究）
- **设计母题**：**双向因果（feedback loops）**——货币供给影响通胀、利率与通胀又反过来影响货币供给：环形箭头与时间序列波纹构成「因果互馈」视觉隐喻，正是 Sims 对货币因果关系测量的核心洞见。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Christopher_A._Sims/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Christopher_A._Sims/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Christopher_A._Sims_zh`、`VIDEO_NAME=Christopher_A._Sims_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Sims 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | 实证方法的武器库，2011 诺奖核心 | 核心页 |
| 1 | vector autoregression | 向量自回归（VAR） | 实证宏观的主要推动者（infobox Notable ideas） | 核心页 |
| 2 | macroeconomics | 宏观经济学 | 货币政策效应的因果测量 | 核心页 |
| 3 | Bayesian statistics | 贝叶斯统计 | 主张其在经济政策评估中的威力 | 方法页 |
| 4 | fiscal theory of the price level | 价格水平的财政理论 | 与理性疏忽理论共同发展 | 理论页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致；共 6 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hendrik S. Houthakker | Sims → 学生 | 哈佛博士导师（1968），论文为生产率变化的动态研究 |
| advisor-student | Lars Peter Hansen | Sims → 学生 | 博士生（infobox Doctoral students 明载，2013 诺奖得主） |
| advisor-student | Harald Uhlig | Sims → 学生 | 博士生（infobox Doctoral students 明载） |
| co-honored | Thomas J. Sargent | 无向 | 2011 诺贝尔经济学奖共享（宏观因果关系实证研究） |
| parent-child | Ruth Bodman | Bodman → 子 | 母，娘家姓 Leiserson，政界人士 |
| parent-child | Albert Sims | Sims 父 → 子 | 父，国务院职员 |

**不入库但提示词可叙述**：外祖父 William Morris Leiserson（经济学家，隔代按项目惯例不入 parent-child，可在身份页叙述）；舅公 Mark Leiserson（耶鲁经济学家，红链人物禁建库边）；Milton Friedman（Sims 的研究「印证了」其货币主义理论，属理论呼应非社会关系）；2024 年 16 位诺奖得主联署公开信事件（政治红线，全篇禁写）。

## 五、配色方案 【人物专属】

- **气质**：严谨、数据驱动、不动声色的颠覆
- **主色**：`#2F5D50`（计量松绿——时间序列波纹的深色底）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeVAR` 向量自回归 — 青绿 `#2F5D50`
  - `badgeBayes` 贝叶斯方法 — 靛蓝 `#1E3A5F`
  - `badgeCaus` 因果测量 — 琥珀 `#C07A2A`
  - `badgeFiscal` 财政与价格 — 灰紫 `#52307C`
- **背景母题**：环形箭头与波纹曲线（货币↔通胀的双向因果回路），呼应「互馈」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — VAR 的布道者 / Christopher A. Sims 1942–2026 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、华盛顿特区出身、哈佛 AB 数学 1963/PhD 1968、
    导师 Houthakker、Princeton Sherrerd 讲席、诺奖 2011、核心领域）
03  核心贡献概览 — VAR / 贝叶斯 / 因果测量 / 价格水平财政理论与理性疏忽
04  早年与哈佛 (1942–1968) — 华盛顿特区出身、数学 AB magna cum laude、Berkeley 研究生一年、
    Houthakker 门下博士
05  明尼苏达二十年 (1970–1990) — 经济系任教、VAR 方法论的孕育期
06  向量自回归（核心贡献页一）— 1980《Macroeconomics and Reality》、把宏观带入数据驱动时代
07  因果的方向（核心贡献页二）— 货币供给影响通胀、但因果双向；印证 Friedman 又超越之
08  贝叶斯与政策评估 — 主张贝叶斯统计在经济政策制定与评估中的威力
09  异端立场（核心贡献页三）— 理性预期是「warning footnote」的论断、对 RBC 的怀疑（引语原文）
10  晚年新理论 — 价格水平的财政理论（FTPL）与理性疏忽（rational inattention）
11  门生与传承 — Lars Peter Hansen（2013 诺奖）/ Harald Uhlig
12  荣誉与学会 — 计量学会 Fellow 1974/会长 1995、AAAS 1988、NAS 1989、AEA 会长 2012
13  2011 斯德哥尔摩 — 与 Sargent 共享、诺奖演讲 Statistical Modeling of Monetary Policy and its Effects
14  遗产与结尾 — VAR 进入各国央行工具箱 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 卒日与死因 | 2026-03-14 逝于明尼阿波利斯家中，系家中跌倒受伤所致，享年 83；「died from injuries sustained in a fall」措辞照录，勿渲染 |
| 政治红线 | 2024 年 16 位诺奖得主联署公开信（涉特朗普与美联储独立性）整段禁写——本篇完全规避该节 |
| 理性预期立场 | Sims 是理性预期革命的「公开反对者」，其原话 "cautionary footnote" 与 "a deep objection to its foundations" 页面有英文原文，入引语框须引原文+译文；勿改写成中文「原话」 |
| 与 Friedman 关系 | Sims 的方法「confirmed the theories of monetarists like Milton Friedman」但因果双向——是理论呼应，不建任何关系边 |
| 双会长年份 | 计量学会会长 1995、AEA 会长 2012，勿互换；Fellow 自 1974 |
| 学生名单 | 仅 Hansen 与 Uhlig 两人（infobox 明载），Sargent infobox 亦列 Hansen 为其学生——两处各自明载，双师承并存，勿删 |
| 家庭三代 | 外祖父 William Morris Leiserson（经济学家）、母 Ruth Bodman（娘家 Leiserson）、父 Albert Sims（国务院）均明载入库；uncle Mark Leiserson 红链不入库 |
| 诺奖演讲 | 2011-12-08 题为 Statistical Modeling of Monetary Policy and its Effects，勿与 Sargent 演讲题（United States Then, Europe Now）混淆 |
| 在校顺序 | 明尼苏达 1970–90 → Harvard/Yale → 1999 起 Princeton（职业生涯最长段），正文口径照录 |
| metadata 噪声 | metadata.json description 作 "American econometrician and macroeconomist (1942-2026)"，身份页可沿用 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| vector autoregression (VAR) | 向量自回归 | Sims 1980 推广，勿写「他发明」 |
| cause and effect | 因果关系 | 获奖理由核心词 |
| Bayesian statistics | 贝叶斯统计 | 先验-后验更新框架 |
| fiscal theory of the price level | 价格水平的财政理论 | FTPL，Sims 与他人共同发展 |
| rational inattention | 理性疏忽 | 信息处理能力有限的建模 |
| rational expectations | 理性预期 | Sims 持批评立场，勿写成支持者 |
| real business cycle | 实际经济周期（RBC） | Sims 对其价值持怀疑 |
| cautionary footnote | 警示性脚注 | 理性预期评价的原话 |
| Econometric Society | 计量经济学会 | Fellow 1974 / 会长 1995 |
| monetary policy | 货币政策 | 因果测量的应用对象 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Sims 一生在明尼苏达与普林斯顿之间把宏观经济学带回数据与历史序列，「怀旧/回望」的抒情曲意贴合其用时间序列回看经济因果的学术气质；2011 与同窗 Sargent 共享诺奖的故人重逢，也正是 Nostalgy 的情绪注脚。
- **本地路径**：复制 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav` 到 `economics/presentations/21th_century/Christopher_A._Sims/Nostalgy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
