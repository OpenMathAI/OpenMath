# 医学家立传提示词（Louis Ignarro）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Louis Ignarro（1998 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Louis_Ignarro/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Louis Joseph Ignarro（路易斯·约瑟夫·伊格纳罗，1941-05-31 纽约布鲁克林 ~ 在世）
- **气质关键词**：**用硬实验证据钉死 EDRF 本质的人、「NO 教父」、一氧化氮学会的创始人** —— 1998 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Furchgott、Murad 三人共享）：
  > "for their discoveries concerning nitric oxide as a signalling molecule in the cardiovascular system"
  > （因其关于一氧化氮作为心血管系统信号分子的发现）
- **设计母题**：**「法庭式证据」**。1986 年会议上他用一连串药理学证据把 EDRF=NO 钉死——视觉隐喻：证据链环环相扣指向同一枚 NO 徽记。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Louis_Ignarro/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Louis_Ignarro/`，成目录 `medic/presentations/20th_century/Louis_Ignarro/`，Makefile 复制后设 `MAIN=Louis_Ignarro_zh`、`VIDEO_NAME=Louis_Ignarro_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | UCLA 分子与医学药理学系教授，1998 诺奖核心 | 总览页 |
| 1 | nitric oxide signalling | 一氧化氮信号 | NO 舒血管与抗血小板聚集皆经 cGMP 介导 | NO 页 |
| 2 | cyclic GMP | 环鸟苷酸 | 从 Geigy 到 Tulane 的 cGMP 研究主线 | cGMP 页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Louis_Ignarro.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Robert F. Furchgott | — | 1998 诺贝尔生理学或医学奖三人共享（一氧化氮信号） |
| co-honored | Ferid Murad | — | 1998 诺贝尔生理学或医学奖三人共享（一氧化氮信号） |
| influence | Paul D. Boyer | — | 明尼苏达求学期间师从，1997 诺贝尔化学奖得主 |
| colleague | Salvador Moncada | — | 共享 1994 Roussel Uclaf 奖与 1995 CIBA 高血压研究奖 |
| spouse | Sharon Ignarro | — | 妻，麻醉科医生 |

> 说明：父母为意大利移民（父亲系 Torre del Greco 木匠）但未具名——不入库，仅家世一句。无正式博士导师明载（明尼苏达药理学 PhD），Boyer 系「studied under」建 influence 不建师生边。与 Furchgott「各自独立得出相同结论」——page.md 明载并行发现，勿写成师生或直接合作。Moncada 建 colleague（两次共享奖项）。

## 五、配色方案 【人物专属】

- **气质**：布鲁克林木匠之子的锐气、证据链式的严密、南加州的阳光
- **主色**：NO 亮紫 `#7B4FA0`（一氧化氮在科普图谱里的标志色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 药理学 — 处方蓝 `#33637D`
  - `badgeB` 一氧化氮信号 — NO 紫 `#7B4FA0`
  - `badgeC` 环鸟苷酸 — cGMP 青 `#1F7A6D`
  - `badgeD` 科普写作 — 讲台橙 `#C07A2E`
- **背景母题**：证据链环扣与 NO 分子（N=O 双键）徽记，稀疏布鲁克林棋盘格，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 用证据钉死 NO 的人 / Louis Ignarro 1941– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（2013 照）+ 右信息网格（生卒、教育、任职、荣誉、核心领域）
03  核心贡献概览 — EDRF=NO 的实验确证 / cGMP 介导机制 / 一氧化氮学会
04  布鲁克林 (1941–1959) — 意大利移民木匠之子、八岁获第一套化学盒、长滩高中
05  哥伦比亚与明尼苏达 (1959–1966) — 1962 药学学士、1966 药理学博士、Boyer 门下求学
06  NIH 与 Geigy (1966–1973) — 化学药理学博士后、工业界新药研发、cGMP 研究起点
07  图兰大学 (1973–1985) — 助理教授起步、读到 Murad 的论文：NO 升高 cGMP
08  推理与追索 — 大胆假设 NO 可能就是舒血管钥匙、舒血管+抗血小板聚集皆由 cGMP 介导
09  1984-1986：EDRF=NO（核心页）— 与 Furchgott 各自独立得出同一结论、1986 年会议上的硬证据
10  1998 诺贝尔奖（核心页）— citation 原文、三人共享、AHA 基础研究奖同年
11  「Viagra 之父」的绰号 — NO 间接参与该药物机理、ED 药物开发的科学远源（绰号按 page.md 口径转述）
12  学会与期刊 — 一氧化氮学会创始人、Nitric Oxide Biology and Chemistry 创刊主编、NAS/AAAS
13  荣誉链 — Roussel Uclaf 1994（与 Moncada/Furchgott 共享）· CIBA 1995（与 Moncada）· AHA 1998 · NAS 1998 · Golden Plate 2014
14  科普与商业边界 — 面向大众的多本健康著作；Herbalife 顾问关系（2003 起）的 page.md 实载记录（见陷阱 5）
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（their 三人共享）；本篇主打「硬实验证据确证 EDRF=NO」的分段 |
| 2 | 三人分工 | Murad 发现 NO 释放→cGMP、Furchgott 发现 EDRF 并疑其为 NO、Ignarro 用实验证据钉死并确证 cGMP 介导的舒血管与抗血小板机制——接力勿混 |
| 3 | 并行发现 | 「Furchgott and Ignarro came to similar conclusions...around the same time, but it was Ignarro who presented hard experimental evidence」——并行与先后的措辞须照 page.md 分寸 |
| 4 | Herbalife（★ 争议段） | 2003 年起任顾问、Niteworks 保健品、12 个月逾 100 万美元、累计逾 1500 万美元报酬、Herbalife 系多层次直销公司——page.md 明载，以「商业顾问关系及金额为 page.md 实载记录」的克制口径一句带过，不作褒贬、不展开直销争议 |
| 5 | 「Viagra 之父」 | page.md 明载「sometimes referred to as the Father of Viagra」——转述绰号须保留 sometimes referred to 的分寸，注明系 NO 机理「indirectly involved」 |
| 6 | 引语红线 | 国会证词 "Only in America could the son of an uneducated carpenter receive the Nobel Prize in Medicine"（2000）有英文原文可引；其余禁编造 |
| 7 | 师承 | Boyer 系「studied under」建 influence；明尼苏达药理学 PhD 无正式导师名——勿编造 |
| 8 | 在世 | 1941 年生、在世——生卒栏卒年留白 |
| 9 | 个性细节 | 铁路模型迷、骑行者、13 个马拉松——人物侧写帧可一句带过 |
| 10 | metadata 冲突 | frontmatter field_of_work=endothelium（噪声级窄化）；yaml fields 按正文三主题 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| EDRF | 血管内皮舒张因子 | 即 NO，Ignarro 确证 |
| cyclic GMP | 环鸟苷酸（cGMP） | NO 信号的胞内第二信使 |
| vasorelaxant | 血管舒张剂/效应 | NO 的功能 |
| platelet aggregation | 血小板聚集 | NO 抑制之 |
| guanylate cyclase | 鸟苷酸环化酶 | NO 的靶酶 |
| S-nitrosothiols | S-亚硝基硫醇 | 其早期论文的活性中间体 |
| Nitric Oxide Society | 一氧化氮学会 | 其创始人 |
| Herbalife | 康宝莱 | 商业顾问关系，克制叙述 |
| Niteworks | Niteworks 保健品 | 其参与开发的补充剂 |
| CIBA-GEIGY | 汽巴-嘉基 | 早年工业经历（今诺华） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「如太阳般闪耀」匹配其高光人格——布鲁克林木匠之子站上斯德哥尔摩讲台的美国梦弧线（其国会引语正是这一主题）
  - 明亮大气的编曲也贴合南加州与「NO 教父」的开创者气场
- **备选**（未采用）：SEA（batch-27 Hubel 已用）、Daylight（batch-27 Samuelsson 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Shine Like The Sun 曲目复制至 `medic/presentations/20th_century/Louis_Ignarro/Shine_Like_The_Sun.wav`，ffmpeg `-shortest` 对齐
