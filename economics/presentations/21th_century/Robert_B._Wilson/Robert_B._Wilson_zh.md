# 经济学家立传提示词（Robert B. Wilson）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2020 年得主 Robert B. Wilson（罗伯特·威尔逊）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Robert_B._Wilson/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert Butler "Bob" Wilson, Jr.（1937-05-16 生于美国内布拉斯加州日内瓦，在世）
- **气质关键词**：**共同价值拍卖的分析者、赢家诅咒的量化者、斯坦福师门的大家长**
- **诺奖获奖理由**（逐字引用，2020 两人共享）：
  > "for improvements to auction theory and inventions of new auction formats"（表彰他们对拍卖理论的改进以及新拍卖形式的发明）
- **设计母题**：**赢家诅咒（winner's curse）**——共同价值拍卖中出价最高者往往高估了标的真实价值；视觉隐喻为一口油井/一段频谱上方的竞价数字与下行的阴影曲线，呼应「理性压低出价以避开诅咒」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Robert_B._Wilson/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Robert_B._Wilson/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_B._Wilson_zh`、`VIDEO_NAME=Robert_B._Wilson_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Wilson 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | auction theory | 拍卖理论 | 诺奖核心：共同价值拍卖与赢家诅咒 | 封面、核心页 |
| 1 | game theory | 博弈论 | infobox Known for；产业组织应用 | 理论页 |
| 2 | market design | 市场设计 | SMR 频谱拍卖共同设计者 | 政策页 |
| 3 | management science | 管理科学 | infobox Fields；非线性规划 | 学科页 |
| 4 | nonlinear pricing | 非线性定价 | 1993 专著与电力优先服务定价 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Howard Raiffa | Wilson ← 导师 | 哈佛商学院 DBA 导师（1963 论文凹规划单纯形算法） |
| advisor-student | Paul Milgrom | Wilson → 学生 | 博士生（infobox 明载），斯坦福同事与共同得主 |
| advisor-student | Alvin Eliot Roth | Wilson → 学生 | 博士生（infobox 明载），2012 诺奖得主；库内规范名 Alvin Eliot Roth（Roth 侧 yaml 已建，勿另建 Alvin E. Roth 分裂 stub） |
| advisor-student | Bengt Holmström | Wilson → 学生 | 博士生（infobox 明载），2016 诺奖得主 |
| advisor-student | Peter Cramton | Wilson → 学生 | infobox 明载 |
| advisor-student | Robert Gibbons | Wilson → 学生 | infobox 明载 |
| advisor-student | Matthew O. Jackson | Wilson → 学生 | infobox 明载 |
| advisor-student | Claude d'Aspremont Lynden | Wilson → 学生 | infobox 明载 |
| advisor-student | Jean-Pierre Ponssard | Wilson → 学生 | infobox 明载 |
| advisor-student | Robert W. Rosenthal | Wilson → 学生 | infobox 明载 |
| advisor-student | Benjamin Golub | Wilson → 学生 | infobox 明载 |
| advisor-student | Yuliy Sannikov | Wilson → 学生 | infobox 明载 |
| co-honored | Paul Milgrom | 无向 | 2020 两人共享（拍卖理论的改进与新拍卖形式的发明） |
| colleague | David M. Kreps | 无向 | 2018 John J. Carty Award 三人共同得主（与 Milgrom） |

**不入库但提示词可叙述**：Susan Athey/Joshua Gans 等其余门生按 Milgrom 侧归属（本篇 infobox 十一人全收，Athey/Gans 在 Milgrom infobox 侧出现，此处以 Wilson infobox 为准）；1982 声誉论文合著者 Kreps/Roberts——Roberts 本篇无载不建边；Roth 的评价引语（"haven't just profoundly changed..."）是评论非新关系。

## 五、配色方案 【人物专属】

- **气质**：深沉、稳健、机制背后的长期耐心
- **主色**：`#16324F`（manifest 预分配·频谱深蓝，与 Milgrom 同色系——2020 师徒共享的视觉家族）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAuction` 共同价值拍卖 — 深蓝 `#16324F`
  - `badgeGame` 博弈论与产业组织 — 青绿 `#146B5A`
  - `badgePrice` 非线性定价 — 琥珀 `#B07A2A`
  - `badgeSchool` 师门传承 — 玫瑰 `#A3455A`
- **背景母题**：竞价数字与下行阴影（赢家诅咒的几何化：越出价越危险），呼应共同价值拍卖的核心洞察。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 赢家诅咒的量化者 / Robert B. Wilson 1937– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒内布拉斯加日内瓦、林肯高中、哈佛 BA 1959/
    MBA 1961/DBA 1963、斯坦福商学院 1964– Adams 讲席荣休教授、诺奖 2020、核心领域）
03  核心贡献概览 — 共同价值拍卖 / 赢家诅咒 / SMR 拍卖设计 / 非线性定价
04  内布拉斯加与哈佛三学位 (1937–1963) — 日内瓦镇、全额奖学金、DBA 论文引入序列二次规划 SQP
05  斯坦福岁月 (1964–) — Adams 讲席、哈佛法学院 1993-2001 兼职、管理科学重镇
06  辛迪加理论 (1968) — Econometrica 论文：群体在帕累托最优风险分摊下的期望效用表示
07  共同价值拍卖与赢家诅咒（核心贡献页）— 理性出价低于最优估计以避诅咒、频谱与矿产例
08  声誉效应与产业组织 — 1982 四人组论文、掠夺性定价/价格战的基本研究
09  非线性定价 (1993) — 公用事业费率设计的百科全书、1995 Leo Melamed 奖、电力优先服务定价落地
10  FCC 频谱拍卖 (1993-94) — 与 Milgrom 共同提出同步加价拍卖、太平洋贝尔咨询背景
11  师门传承（核心特色页）— Roth/Holmström/Milgrom 三位诺奖门生、十一位博士生
12  2020 诺贝尔奖 — 师徒共享、Roth 评语引用、瑞典科学院口径
13  荣誉与影响 — Golden Goose 2014/BBVA 2015/Carty 2018、NAS 院士、AEA 杰出会士
14  遗产与结尾 — 拍卖从博弈论文献变成全球基础设施 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 同名区分 | 与物理学家 Robert W. Wilson（1964 宇宙微波背景诺奖）同名不同人；库内另有 Kenneth G. Wilson（1982 物理诺奖）——yaml name_en 用 **Robert B. Wilson**，图灵奖侧的 Kenneth G. Wilson 勿混 |
| 学位三连 | 哈佛 BA(1959)+MBA(1961)+**DBA**(1963)——博士是工商管理学博士（Harvard Business School），勿写成经济学 PhD |
| 获奖理由主体 | citation 主语是 "their"；瑞典科学院补充语 "improved auction theory and invented new auction formats, benefitting sellers, buyers and taxpayers around the world" 可引；其个人侧重点是**共同价值拍卖与赢家诅咒**（与 Milgrom 侧重互补，勿互换） |
| 师徒双向 | Milgrom 对 Wilson 是"同事+前学生"——advisor-student（Wilson→学生）与 co-honored 两边并行；三人门生获诺奖（Roth 2012/Holmström 2016/Milgrom 2020）是本篇特色可点题 |
| 页面单薄 | page.md 仅 81 行、无 Early life 细节之外的家世/婚姻信息——幻灯片按 14 页规划宁缺毋滥，家人（无载）禁写 |
| 政治敏感红线 | page.md "Political views" 节载 2024 联名公开信批评 Trump 政策——**全部禁写** |
| Wilson doctrine | See also 挂 Wilson doctrine (economics)——正文未展开，提示词不写术语表 |
| Carty Award 归属 | 2018 John J. Carty Award 是与 Kreps、Milgrom 三人共享（"With colleagues David M. Kreps and Paul Milgrom"）——勿写成个人奖 |
| Roth 评语引语 | "haven't just profoundly changed the way we understand auctions – they have changed how things are auctioned" page.md 载英文原文，引原文+译文 |
| 出生地名 | 生于 Geneva, **Nebraska**（内布拉斯加州日内瓦镇），勿与瑞士日内瓦混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| common value auction | 共同价值拍卖 | 诺奖个人侧核心概念 |
| winner's curse | 赢家诅咒 | 理性压价规避，勿写成"诅咒效应"泛化 |
| sequential quadratic programming (SQP) | 序列二次规划 | DBA 论文方法学贡献 |
| syndicate theory | 辛迪加理论 | 1968 Econometrica 群体决策论文 |
| nonlinear pricing | 非线性定价 | 1993 专著主题 |
| simultaneous ascending auction | 同步加价拍卖 | FCC SMR 设计的机制名 |
| priority service pricing | 优先服务定价 | 电力行业已实施的定价方案 |
| DBA | 工商管理学博士 | 哈佛商学院学位，勿写 PhD |
| Adams Distinguished Professor | Adams 杰出讲席教授 | 斯坦福商学院职衔（荣休） |
| Leo Melamed Prize | Leo Melamed 奖 | 芝加哥大学 1995，非线性定价专著获奖 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：与 Milgrom 篇同曲（2020 师徒共享组的听觉家族）；管弦的厚重感贴合 Wilson 一甲子的学术纵深——从 SQP 到辛迪加理论到赢家诅咒再到师门三位诺奖得主，是"长期主义"的交响。
- **本地路径**：复制 `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav` 到 `economics/presentations/21th_century/Robert_B._Wilson/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
