# 经济学家立传提示词（Gérard Debreu）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1983 年得主 Gérard Debreu（杰拉尔·德布勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Gérard_Debreu/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Gérard Debreu（1921-07-04 生于法国加来 ~ 2004-12-31 逝于巴黎，享年 83 岁）
- **气质关键词**：**一般均衡的公理化者、把数学请进经济学的严谨派、无声的美学家**
- **诺奖获奖理由**（逐字引用）：
  > "for having incorporated new analytical methods into economic theory and for his rigorous reformulation of the theory of general equilibrium"（表彰他将新的分析方法引入经济理论，并对一般均衡理论作出了严格的重构）
- **设计母题**：**不动点与均衡（fixed point & equilibrium）**——Kakutani 不动点定理支撑的均衡存在性证明，抽象拓扑中交汇的曲线与交汇点，是「市场出清、供需在一点相遇」的视觉隐喻：交叠的拓扑曲面与一个金色的不动点构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Gérard_Debreu/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Gérard_Debreu/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Gérard_Debreu_zh`、`VIDEO_NAME=Gérard_Debreu_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Debreu 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | general equilibrium theory | 一般均衡理论 | 诺奖核心：存在性证明与公理化重构 | 核心页 |
| 1 | mathematical economics | 数理经济学 | infobox Discipline；把拓扑引入经济学 | 全篇 |
| 2 | utility theory | 效用理论 | 基数效用的可加分解 | 效用页 |
| 3 | topological methods in economics | 经济学中的拓扑方法 | 1954 论文用拓扑而非微积分方法 | 方法页 |
| 4 | differentiable economies | 可微经济 | 晚年研究：均衡的有限性 | 晚期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Léon Walras | 无向 | 一般均衡理论源头（infobox Influences 明载） |
| influence | Henri Cartan | 无向 | ENS 时期的数学影响（infobox Influences 明载） |
| influence | Maurice Allais | 无向 | infobox Influences 明载；frontmatter doctoral_advisor 无 infobox 佐证，不入 advisor 边 |
| collaborator | Kenneth Arrow | 无向 | 1954 Econometrica 合著《Existence of an Equilibrium for a Competitive Economy》 |
| collaborator | Herbert Scarf | 无向 | 1963 合著核极限定理《A limit theorem on the core of an economy》 |
| collaborator | Tjalling Koopmans | 无向 | 1982 合著《Additively decomposed quasiconvex functions》 |
| spouse | Françoise Bled | 无向 | 1946 结婚，育二女 Chantal（1946）与 Florence（1950） |
| advisor-student | Graciela Chichilnisky | Debreu → 学生 | infobox Doctoral students 明载 |
| advisor-student | Beth E. Allen | Debreu → 学生 | infobox Doctoral students 明载 |
| advisor-student | Xavier Vives | Debreu → 学生 | infobox Doctoral students 明载 |
| advisor-student | Ishac Diwan | Debreu → 学生 | infobox Doctoral students 明载 |

**不入库但提示词可叙述**：二女 Chantal 与 Florence（仅具名不入 parent-child）；Bourbaki 学派（集体笔名非个人，不入 influence）；2001 年与 Buchanan/Klein/Friedman/Solow 联署的获奖者清单短文（一次性行文，防噪声）。

## 五、配色方案 【人物专属】

- **气质**：公理、拓扑、冷峻的法式严谨
- **主色**：`#146B3A`（公理绿——公理化体系的克制与生长感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGE` 一般均衡 — 深绿 `#146B3A`
  - `badgeTopo` 拓扑方法 — 靛蓝 `#2E3A59`
  - `badgeUtil` 效用理论 — 琥珀 `#C07A2A`
  - `badgeDiff` 可微经济 — 灰紫 `#52307C`
- **背景母题**：交叠的拓扑曲面与一枚金色不动点（Kakutani 不动点的抽象化），呼应「市场在一点出清」的核心思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 一般均衡的公理化者 / Gérard Debreu 1921–2004 + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地加来、教育 ENS/巴黎大学博士 1956、
    任职 Berkeley 1962–1991、诺奖 1983、核心领域）
03  核心贡献概览 — 均衡存在性 / Theory of Value / 效用理论 / 可微经济
04  加来早年与战火中断 (1921–1945) — 父殉母亡、Vichy 备考、1944 诺曼底登陆中断会考投军、阿尔及尔与驻德
05  ENS 与转向经济学 (1941–1946) — Cartan 与 Bourbaki 的影响、Agrégation、Walras 一般均衡的吸引
06  Cowles 委员会岁月 (1950–1955) — 芝加哥五年、1954 与 Arrow 合作论文、1955 转耶鲁
07  1954：均衡存在性的拓扑证明（核心贡献页）— 与 Arrow 合著，拓扑方法取代微积分
08  1959《价值理论》：公理化的经济学（核心贡献页）— Kakutani 不动点、或有商品、Arrow–Debreu 证券
09  Berkeley 四十年 (1962–1991) — University Professor、1958 级经济学与数学讲席教授（荣休）
10  可微经济与均衡的有限性 — 晚年研究主线
11  门生与传承 — Chichilnisky、Beth E. Allen、Xavier Vives
12  荣誉与认可 — Nobel 1983、1976 荣誉军团勋章、AAAS/NAS/美国哲学会、1990 AEA 主席
13  数理模式的经济学 — 1983 诺奖演讲 Economic Theory in the Mathematical Mode
14  遗产与结尾 — Arrow–Debreu 证券与金融经济学、公理化范式 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 入职 Berkeley 年份 | 正文 Biography 段作「In 1960 he became a professor at the University of California」，而 Academic career 段明载 **1960-61 在斯坦福行为科学高等研究中心、1962 年 1 月入职 Berkeley**；幻灯片统一按 **1962 年 1 月入职 Berkeley**，1960 为概述性表述，陷阱表留痕 |
| Allais 关系口径 | frontmatter `doctoral_advisor: [Maurice Allais]`，但 infobox 无 Doctoral advisor 行、正文亦无载，infobox 将 Allais 列于 **Influences**；按 page.md 口径入 **influence** 边，禁写「博士导师」 |
| Arrow–Debreu 归属 | 1954 存在性论文是 Debreu 与 Kenneth Arrow **合著**；勿写成 Debreu 独自证明，也勿写成 Arrow 一人主导 |
| 存在性证明方法 | 用 **拓扑方法**（Kakutani 不动点定理），非微积分方法；page.md 明载这一对照，勿混淆 |
| Arrow–Debreu 证券 | 是《价值理论》第七章**或有商品**概念在金融经济学中的名称，勿把证券概念前置到 1954 论文 |
| 两位博士生页 | infobox 四位博士生全部入库；metadata.json 无更宽名单，防噪声不外扩 |
| 死亡日期修辞 | 2004-12-31 逝于巴黎（新年前夜），享年 83 岁；「natural causes」按原文客观转述 |
| 诺奖演讲标题 | 1983-12-08 诺奖演讲 *Economic Theory in the Mathematical Mode*，与获奖理由分开，勿混写 |
| 奖项完整性 | 除诺奖外：1976 荣誉军团勋章、洪堡奖、Guggenheim Fellowship、Fisher-Schultz Lecture、AEA 杰出会士、多校荣誉博士；1990 年任 **美国经济学会主席**，勿遗漏 |
| 国籍口径 | yaml 按 frontmatter 填 France + United States（manifest country 仅 France）；幻灯片国籍行按 Nobel 官方口径 France，正文提法国出生、美国执教即可，勿写「入籍年份」（page.md 无载） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| general equilibrium | 一般均衡 | 获奖理由核心词，勿译「全局均衡」 |
| existence of equilibrium | 均衡存在性 | 1954 论文标题，拓扑方法 |
| Kakutani fixed-point theorem | 角谷不动点定理 | 存在性证明的技术支柱 |
| Theory of Value | 《价值理论》 | 1959 专著副题 An Axiomatic Analysis of Economic Equilibrium |
| contingent commodity | 或有商品 | 依赖自然状态实现的交货承诺 |
| Arrow–Debreu security | Arrow–Debreu 证券 | 金融经济学对或有商品的称呼 |
| cardinal utility | 基数效用 | 可加分解问题 |
| differentiable economies | 可微经济 | 晚年方向，均衡有限性 |
| Cowles Commission | 考尔斯委员会 | 芝加哥时期（1950–1955） |
| Agrégation de Mathématiques | 数学学衔会考 | 1945 底–1946 初通过 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Debreu 一生以沉默与秩序著称——孤儿出身、战火中失学、以近乎隐士的方式在公理体系里独自行走；「孤寂而深情」的 cinematic 曲风贴合这位把经济学写成数学诗的严谨派，也呼应其传记作者笔下「order and silence」的一生。
- **本地路径**：复制 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav` 到 `economics/presentations/20th_century/Gérard_Debreu/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
