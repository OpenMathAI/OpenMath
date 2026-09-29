# 医学家立传提示词（Robert F. Furchgott）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Robert F. Furchgott（1998 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Robert_F._Furchgott/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Robert Francis Furchgott（罗伯特·弗朗西斯·弗奇戈特，1916-06-04 南卡罗来纳州查尔斯顿 ~ 2009-05-19 西雅图，享年 92 岁）
- **气质关键词**：**EDRF（血管内皮舒张因子）的发现者、一氧化氮信号的第一位指认者、八十二岁才登顶诺奖的慢工大师** —— 1998 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Ignarro、Murad 三人共享）：
  > "for their discoveries concerning nitric oxide as a signalling molecule in the cardiovascular system"
  > （因其关于一氧化氮作为心血管系统信号分子的发现）
- **设计母题**：**「血管的叹息」**。内皮细胞悄悄释放一氧化氮让血管舒张——视觉隐喻：一段血管截面舒张的瞬间，NO 分子小徽记从内皮逸出。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Robert_F._Furchgott/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Robert_F._Furchgott/`，成目录 `medic/presentations/20th_century/Robert_F._Furchgott/`，Makefile 复制后设 `MAIN=Robert_F._Furchgott_zh`、`VIDEO_NAME=Robert_F._Furchgott_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 血管药理与受体理论，1998 诺奖核心 | 总览页 |
| 1 | pharmacology | 药理学 | 四所医学院药理学教授四十年 | 生涯页 |
| 2 | nitric oxide signalling | 一氧化氮信号 | EDRF 发现（1978）与本质判定（1986） | EDRF 页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Robert_F._Furchgott.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Louis Ignarro | — | 1998 诺贝尔生理学或医学奖三人共享（一氧化氮信号） |
| co-honored | Ferid Murad | — | 1998 诺贝尔生理学或医学奖三人共享（一氧化氮信号） |
| spouse | Lenore Mandelbaum | — | 1941 年成婚，1983 年病逝 |
| spouse | Margaret Gallagher Roth | — | 晚年伴侣，2006 年卒 |
| parent-child | Arthur Furchgott | 父 | 百货店主 |
| parent-child | Pena Sorentrue Furchgott | 母 | — |
| parent-child | Susan Furchgott | 女 | 旧金山反主流文化艺术家，公社共同创始者 |

> 说明：三个女儿中仅 Susan 有叙事入库，Jane/Terry 仅具名不入库；两段婚姻均按 infobox Spouse(s) 口径建边（Margaret 系晚年伴侣，infobox 列为配偶）。无博士导师明载（西北大学 1940 PhD 无导师名）——禁编造。与 Ignarro/Murad 的三人组共建一氧化氮故事，page.md 未载三人私下交往，仅建 co-honored 边。

## 五、配色方案 【人物专属】

- **气质**：慢工细活的克制、八十二年人生的静水深流
- **主色**：内皮蓝灰 `#41607E`（血管内壁的冷静色调）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 受体青 `#1F7A6D`
  - `badgeB` 药理学 — 教鞭蓝 `#33637D`
  - `badgeC` 一氧化氮信号 — NO 紫罗兰 `#6E5AA0`
  - `badgeD` 血管舒张 — 充血红 `#B3544E`
- **背景母题**：血管截面舒张环与逸出的 NO 小分子、稀疏螺旋纹理，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — EDRF 的发现者 / Robert F. Furchgott 1916–2009 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职四站、家庭、荣誉、核心领域）
03  核心贡献概览 — EDRF / 一氧化氮本质判定 / 硝酸甘油机理 / Viagra 的远源
04  查尔斯顿少年 (1916–1937) — 百货店主之家、1937 北卡教堂山化学学士
05  西北大学博士 (1937–1940) — 1940 生物化学博士
06  执教四站 (1940–1989) — Cornell 1940-49 → 圣路易斯华盛顿大学 1949-56 → SUNY Downstate 1956-89 → Miami 1989-2009
07  1978：EDRF 的发现（核心页）— 内皮细胞释放未知舒张因子、命名为 endothelium-derived relaxing factor
08  1986：EDRF 就是一氧化氮（核心页）— 八年追凶、与 Ignarro 各自得出相同结论
09  1998 诺贝尔奖（核心页）— citation 原文、三人共享、与克林顿合影的 1998 得主行
10  从硝酸甘油到 Viagra — 百年老药硝酸甘油机理终于得解；心绞痛治疗与ED 药物的科学远源
11  荣誉链 — Gairdner 1991 · Lasker 1996 · Nobel 1998 · Golden Plate 1999（与 Murad 同获）· Axelrod 奖
12  家庭与信仰 — 犹太家庭、Woodmere 定居、两段婚姻、三个女儿
13  晚年 (1989–2009) — Miami 兼职、SUNY 荣休教授、2008 移居西雅图、2009 辞世
14  遗产 — 一氧化氮成为体内第一号信号气体；神经/心血管/免疫多域意义的开启
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning nitric oxide as a signalling molecule in the cardiovascular system"（their 三人共享同一理由） |
| 2 | 三人分工 | Furchgott 发现 EDRF（1978）并判定其为 NO（1986）；Ignarro 提供硬实验证据（1986 会议）；Murad 证明硝酸甘油释放 NO 升高 cGMP——三段接力勿混 |
| 3 | 年代链 | 1978 发现 EDRF → 1986 判定本质 → 1996 Lasker → 1998 Nobel——「八十二年人生、八十二岁得奖」是本篇叙事钩子（1916-1998 得奖时 82 岁） |
| 4 | 无师承 | 西北大学博士无导师名——禁编造；与 Ignarro/Murad 无私下交往明载，仅 co-honored 边 |
| 5 | Viagra 表述 | NO 研究是 ED 药物「instrumental in the development」的远源科学基础——勿写成 Furchgott 参与 Viagra 研制 |
| 6 | 引语红线 | 本篇 page.md 无直接引语，禁编造 |
| 7 | 家庭 | 两段婚姻按 infobox 建边（Lenore 1941-1983 病逝、Margaret 晚年伴侣 2006 卒）；女儿 Susan 的公社叙事一句带过、不作价值观评述 |
| 8 | 死亡地 | 逝于西雅图（2008 年移居 Ravenna 街区后），勿与长居的纽约 Woodmere 混淆 |
| 9 | Lasker 1996 | 与 Murad 两人获 Lasker（Ignarro 未在其列）——三人组中 Lasker 份额不同，勿写三人同获 |
| 10 | metadata 冲突 | frontmatter occupations 含 pharmacist 噪声；workplaces 的 Miami (1989-2009) 与 SUNY (1956-2009) 并存——按正文「SUNY 至 1989、Miami 1989 起」为准 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| EDRF | 血管内皮舒张因子 | 后被证实即一氧化氮 |
| endothelium | 内皮 | 血管内壁细胞层 |
| nitric oxide (NO) | 一氧化氮 | 体内信号分子，勿与笑气（N2O）混淆 |
| nitroglycerin | 硝酸甘油 | 释放 NO 的百年老药 |
| angina pectoris | 心绞痛 | 硝酸甘油适应症 |
| vasodilation | 血管舒张 | EDRF 的效应 |
| endothelial cell | 内皮细胞 | EDRF 来源 |
| signalling molecule | 信号分子 | citation 核心词 |
| Gairdner Award | 盖尔德纳奖 | 1991 |
| SUNY Downstate | 纽约州立大学下州医学中心 | 1956-89 主场 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「不可见之光」精准双关——一氧化氮是无形的气体信使，Furchgott 看见的是所有同行都忽略的隐形信号
  - 幽深渐亮的编曲契合「八年追凶」的叙事弧线
- **备选**（未采用）：Last Hope（本批 Carlsson 已用）、Expedition（batch-11/27 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions The Invisible Light 曲目复制至 `medic/presentations/20th_century/Robert_F._Furchgott/The_Invisible_Light.wav`，ffmpeg `-shortest` 对齐
