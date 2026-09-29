# 医学家立传提示词（Henry Hallett Dale）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Henry Hallett Dale（1936 年诺贝尔生理学或医学奖得主，英国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Henry_Hallett_Dale/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Henry Hallett Dale（亨利·哈利特·戴尔，1875-06-09 伦敦伊斯灵顿 ~ 1968-07-23 剑桥，享年 93 岁）
- **气质关键词**：**乙酰胆碱的鉴定者、化学传递学说的旗手、英国生理学的掌门人** —— 1936 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Otto Loewi 共享）：
  > "for their discoveries relating to chemical transmission of nerve impulses"
  > （因其关于神经冲动化学传递的发现）
- **设计母题**：**「突触间隙的一滴递质」**。两个神经元之间的缝隙里，一枚小分子（乙酰胆碱）跨越间隙——视觉隐喻：双神经元轮廓与其间放大的分子徽记。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Henry_Hallett_Dale/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Henry_Hallett_Dale/`，成目录 `medic/presentations/20th_century/Henry_Hallett_Dale/`，Makefile 复制后设 `MAIN=Henry_Hallett_Dale_zh`、`VIDEO_NAME=Henry_Hallett_Dale_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | NIMR 生化与药理学部主任，交感神经递质研究 | 总览页 |
| 1 | physiology | 生理学 | 剑桥 Langley 门下训练，神经-肌肉传递 | 师承页 |
| 2 | neuroscience | 神经科学 | 乙酰胆碱作为神经递质（1914 鉴定） | 乙酰胆碱页 |
| 3 | neurotransmission | 神经传递 | 化学传递学说、Dale's principle、递质分类法 | 原理页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Henry_Hallett_Dale.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Newport Langley | 师 | 剑桥三一学院师从，1909 年剑桥医学博士 |
| influence | Paul Ehrlich | — | 1903 年法兰克福短期师从数月 |
| co-honored | Otto Loewi | — | 1936 诺奖共享（神经冲动化学传递），终生挚友 |
| controversy | John Eccles (neurophysiologist) | — | 1940s 突触信号化学派与电学派之争 |
| spouse | Ellen Harriett Hallett | — | 1904 年成婚，表亲 |
| parent-child | Alison Sarah Dale | 女 | 嫁 1957 诺贝尔化学奖得主 Alexander R. Todd |
| parent-child | Charles James Dale | 父 | 斯塔福德郡陶瓷制造商 |
| parent-child | Frances Anne Hallett | 母 | — |

> 说明：对手方均用库内/manifest 规范名——Paul Ehrlich(766, Q57089)、John Newport Langley(4620，他批已建)；Eccles 用 manifest 规范形式 John Eccles (neurophysiologist)（其本人记录属 med-batch-17，本批只建自己侧边）。★ Todd 侧协作：Alexander R. Todd 所在批次已先建 Dale–Todd 边（库内 8522，type other，note 岳父、翁婿二人先后任皇家学会会长）——本篇女婿关系由该边承载，女儿 Alison 行 note 不重复建边。Starling/Bayliss 仅一次协助实验（Brown Dog affair 语境），不建边；儿子与另一女儿未具名不入库；弟弟 Benjamin Dale（作曲家）无兄弟类关系类型，不入库；Tomas Hökfelt 为共存原理的下游命名者，不入库。

## 五、配色方案 【人物专属】

- **气质**：英式学统的雍容、机构掌门人的稳重、化学传递的锋利
- **主色**：突触蓝 `#274B6D`（神经间隙的深海色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 药理学 — 麦角紫 `#5E4B8B`（其早期麦角研究语境）
  - `badgeB` 生理学 — 肌电青 `#2E7A8C`
  - `badgeC` 神经科学 — 递质金橙 `#C8862E`
  - `badgeD` 神经传递 — 间隙银蓝 `#6E8CA0`
- **背景母题**：稀疏的双曲线神经元轮廓与间隙小圆点（递质囊泡），低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 化学传递的旗手 / Henry Hallett Dale 1875–1968 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、荣誉长链、核心领域）
03  核心贡献概览 — 乙酰胆碱 / 化学传递 / Dale's principle / 机构领袖
04  伊斯灵顿少年 (1875–1894) — 七子之家、作曲家弟弟、The Leys School（其名命宿舍）
05  剑桥与法兰克福 (1894–1909) — Langley 门下、1903 Ehrlich 处数月、1909 医学博士
06  1903 年的两桩公案 — Brown Dog affair 中的协助实验（如实一句）；UCL 结识 Loewi
07  NIMR 部主任 (1914–) — 生化与药理学部、1914 当选 FRS
08  乙酰胆碱：从麦角到神经递质（核心页）— 1914 鉴定其可能递质身份
09  1936 诺贝尔奖（核心页）— citation 原文（与 Loewi 共享）、1936-12-12 诺奖演讲
10  双线合璧 — Loewi 证明其神经重要性（蛙心实验回叙）、Dale 鉴定物质本体
11  突触之争 — 1940s 化学派 vs Eccles 电学派；「多数化学、少数电」的最终图景
12  Dale's principle — 递质分类命名法（肾上腺素能/GABA 能…）、单递质解读已被修正（共存原理）
13  荣誉与机构生涯 — Royal Society 主席 1940-45 · OM 1944 · Copley 1937 · Wellcome Trust 主席 1938-60 · Lady Dale 医疗船
14  遗产 — Sir Henry Dale Fellowships、Dale Medal；突触化学传递的现代基石
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries relating to chemical transmission of nerve impulses"（their 与 Loewi 共享）；勿写成「因发现乙酰胆碱」独享口径 |
| 2 | 双人分工 | Dale 系 1914 年鉴定乙酰胆碱（"first identified as a possible neurotransmitter"），Loewi 证明其在神经系统中的作用——先后与分工勿倒置 |
| 3 | Dale's principle | 「一个神经元只释放一种递质」的解读已被证伪（共存原理）——正文要写 Dale 原理的两层含义并注明错误解读已被修正，勿当定论 |
| 4 | Brown Dog affair | 1903 年协助 Starling/Bayliss 的活体解剖事件是 page.md 明载史实，一笔带过即可，勿展开动物实验伦理争论 |
| 5 | 与 Loewi 友谊 | 「met and became friends」+ Loewi 篇「lifelong friend that helped to inspire」——友谊与合作是双篇互证的明载事实，可写 |
| 6 | Eccles 之争 | 1940s 突触化学/电性质之争建 controversy 边；结论「多数化学信号、少数电突触」须写明，Eccles 后来获 1963 诺奖，勿写成「被证明全错」 |
| 7 | 师承口径 | Langley 用正文 "working under"（剑桥）建师生边；frontmatter 的 Starling 导师行因正文仅载「一次协助」不建边；Ehrlich 仅 1903 数月，建 influence |
| 8 | 家族 | 妻 Ellen Harriett Hallett 是其表亲（first cousin）——如实记；女儿 Alison Sarah Dale 嫁 Alexander R. Todd（1957 化学诺奖、Royal Society 主席 1975-80）—— Todd 是女婿不建边，仅在女儿行 note 体现 |
| 9 | 荣誉年代链 | FRS 1914 · Cameron 1926 · knighthood 1932 · Nobel 1936 · Copley 1937 · GBE 1943 · OM 1944 · RS 主席 1940-45 · RSM 主席 1948-50 · Wellcome 主席 1938-60，勿错置 |
| 10 | metadata 冲突 | 生卒、国籍一致；award_received 列表与正文一致，以正文年代链为准 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| acetylcholine | 乙酰胆碱 | 首个被鉴定的神经递质 |
| neurotransmission | 神经传递 | 诺奖理由核心词 |
| chemical synapse | 化学突触 | 与电突触（electrical synapse）相对 |
| Dale's principle | 戴尔原理 | 「 erroneously referred to as Dale's Law」——勿写「定律」 |
| cotransmission / coexistence | 共传递 / 共存原理 | 修正单递质解读的现代概念 |
| noradrenergic / GABAergic | 肾上腺素能 / GABA 能 | 其分类法的产物 |
| vagus nerve | 迷走神经 | Loewi 实验语境（Vagusstoff） |
| ergot | 麦角 | 其早期药理研究对象（背景） |
| Wellcome Trust | 惠康基金会 | 1938-60 任主席 |
| Brown Dog affair | 棕狗事件 | 1903 年历史公案，一句带过 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「恒久/宏大」匹配其体制性遗产——Royal Society 主席、Wellcome 掌门、Dale Fellowship 与 Dale Medal 至今颁授，是「制度化的永恒」
  - 冷峻大气的编曲贴合化学传递学说的跨世纪确证
- **备选**（未采用）：Timeless（意象更贴但高频占用）、SEA（节奏过缓，压不住争辩帧的张力）
- **本地路径**：按 music_audio/ 内 Alex-Productions Eternals 曲目复制至 `medic/presentations/20th_century/Henry_Hallett_Dale/Eternals.wav`，ffmpeg `-shortest` 对齐
