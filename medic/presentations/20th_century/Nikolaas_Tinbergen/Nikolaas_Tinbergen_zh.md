# 医学家立传提示词（Nikolaas Tinbergen）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1973 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Nikolaas "Niko" Tinbergen（1907-04-15 生于海牙 ~ 1988-12-21 逝于牛津，享年 81 岁）
- **气质关键词**：**行为学四问的提出者、超常刺激实验的设计大师、把"观察与惊叹"变成科学的实验家** —— 1973 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries concerning organization and elicitation of individual and social behaviour patterns"
  > （因他们关于个体与社会行为模式的组织与引发机制的发现）
- **设计母题**：**四问框架与超常之蛋（four questions & the supernormal egg）**。红腹木鱼模型、石膏斑蛋、海鸥巢边的实验场——"给行为研究装上四面镜子"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Nikolaas_Tinbergen/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Nikolaas_Tinbergen/page.md`；目录 `medic/presentations/20th_century/Nikolaas_Tinbergen/`；Makefile 改 `MAIN=Nikolaas_Tinbergen_zh`；肖像优先 images.txt 所列 Commons 图（Tinbergen in 1978、与 Lorenz 合照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Nikolaas_Tinbergen.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ethology | 动物行为学 | 奠基人之一，诺奖核心 | 核心页 |
| 1 | ornithology | 鸟类学 | 银鸥/穴蜂/雪鹀观察 | 研究页 |
| 2 | behavioral ecology | 行为生态学 | 行为学的当代形态 | 遗产页 |
| 3 | ethological psychology | 行为学取向心理学 | 自闭症观察法应用（存争议） | 晚年页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hilbrand Boschma | 师→本人 | 莱顿大学博士导师（1932，穴蜂视觉地标） |
| colleague | Konrad Lorenz | 无向 | 1936 相识的合作者与诤友，共创期刊与 IRM 理论 |
| co-honored | Konrad Lorenz | 无向 | 1973 诺贝尔生理学或医学奖三人共享（行为模式） |
| co-honored | Karl von Frisch | 无向 | 1973 诺贝尔生理学或医学奖三人共享（行为模式） |
| advisor-student | John Michael Cullen | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Marian Dawkins | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Richard Dawkins | 本人→学生 | infobox Doctoral students 明载，《自私的基因》作者 |
| advisor-student | Iain Douglas-Hamilton | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Aubrey Manning | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Desmond Morris | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Anthony Sinclair | 本人→学生 | infobox Doctoral students 明载 |
| spouse | Elisabeth Rutten | 无向 | 结婚，育五子 |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；`Konrad Lorenz`/`Karl von Frisch` 与本批两篇同形式镜像。**relations=12 为诚实值**（infobox 七位博士生全收——Dawkins 夫妇/Morris 等皆成名学者；兄弟 Jan/Luuk 与 Bowlby 不入库，见陷阱表）。

## 五、配色方案

- **气质**：荷兰低地的野外耐心 + 牛津讲席的清晰头脑 + 实验设计的巧思
- **主色**：行为蓝 `#2E6E9E`（北海与刺鱼腹红之外的水色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 四问框架 — 框架金 `#C9A227`
  - `badgeB` 超常刺激 — 刺激红 `#A63A2B`
  - `badgeC` 层级模型 — 本能蓝 `#3D5A80`
  - `badgeD` 野生动物影像 — 影像绿 `#3E6B4F`
- **背景母题**：低透明度四象限框架线 + 巢中并排的蛋（真蛋与石膏超常蛋）。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 行为学四问的提出者 / Nikolaas Tinbergen 1907–1988 + badge + 右上头像 + 国籍行（United Kingdom，生于荷兰）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、海牙、莱顿大学 1932 博士、二战战俘、Oxford 教席、诺奖 1973）
03  核心贡献概览 — 四问框架 / 层级模型 / 超常刺激 / 野生动物影像
04  海牙与诺贝尔兄弟之家 (1907–1932) — 五兄妹、兄 Jan 获首届诺贝尔经济学奖（兄弟档唯一）、兄 Luuk 亦生物学家、莱顿学生时代
05  1932 博士：穴蜂的地标导航 — 欧洲穴蜂（蜂狼）雌蜂凭视觉地标回巢——野外实验的起点
06  二战与战后转向 — Kamp Sint-Michielsgestel 战俘经历；与 Lorenz 因战争产生数年龃龉后和解（page.md 明载一句带过）；战后移居英国
07  Oxford 建组 (1949–) — 牛津动物学教授、Merton/Wolfson College Fellow、1951《本能的研究》
08  层级模型（核心页一）— 在 Lorenz 心理水力模型上加层级闸门：动机冲动逐级释放；蜜蜂觅食实验（颜色+气味链式释放）
09  超常刺激（核心页二）— 石膏斑蛋:更大更多斑更艳者更受青睐、带黑点的荧光蛋胜过真蛋；三刺鱼攻红腹木鱼胜过真鱼；纸板蝴蝶交配偏好——超常刺激划清引发本能的关键特征
10  四问框架（核心页三）— 因果/发育/功能/演化（近因 vs 终因）；与亚里士多德四因的暗合（页面对照注记）；现代行为学与社会生物学的基石
11  1973 诺贝尔奖 — 与 Lorenz、Frisch 共享；官方理由全句；诺奖演讲为"mere animal watchers"正名、"watching and wondering"可助减轻人类痛苦（可引）；致谢辞大谈 Alexander 技巧的趣闻
12  野生动物影像 — 与导演 Hugh Falkus 合作《秃鼻乌鸦之谜》1972、《生存的信号》1969 获 Italia 奖与 1971 美国蓝丝带奖
13  晚年与争议（客观一页）— 自闭症观察法与"拥抱疗法"推荐缺乏科学支持、被指有争议甚至有害（page.md 明载，含自闭症社群批评）——如实呈现，不作辩护
14  家庭与身后 — 妻 Elisabeth Rutten（1912-1990）五子；晚年抑郁（兄 Luuk 系自杀，其深有恐惧）、友人 Bowlby 医治；1988-12-21 卒于牛津家中；无神论者、反协和飞机顾问委员
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1973 三人共享同一句理由；分工：Tinbergen=实验验证与四问框架（页面称其贡献为以"comprehensive, careful, and ingenious experiments"检验 Lorenz/Frisch 假说）——勿混写 |
| 兄弟档 | 兄 Jan Tinbergen 获 1969 首届经济学奖——**唯一兄弟档诺奖**，叙事亮点但非同奖；兄弟不入库（sibling 无关系类型），仅叙述 |
| 与 Lorenz 的战争龃龉 | Tinbergen 曾是纳粹战俘、与 Lorenz 数年不合后和解——page.md 明载，一句客观带过；Lorenz 纳粹背景细节不在本篇展开 |
| 自闭症"拥抱疗法" | 缺乏科学支持、被批有争议甚至有害（尤其自闭症社群）——page.md 明载，**如实写**不作辩护；属科学争议非政治敏感 |
| 抑郁与 Bowlby | 晚年抑郁、友人 Bowlby 施治且其思想曾深受 Tinbergen 影响——家庭/医疗私密内容，一句即可，Bowlby 不入库 |
| 七博士生全收 | infobox Doctoral students 七人（Cullen/M. Dawkins/R. Dawkins/Douglas-Hamilton/Manning/Morris/Sinclair）全入库——与 Koch 七学生同例；正文举 Dawkins/Morris 为代表即可 |
| 鹰/雁效应 | 该效应在页面列为 Known for 之一（与 Lorenz 共享的行为学概念）——归本能释放语境，勿写成 Tinbergen 独创 |
| 1978 合影 | 页面有 1978 诺奖得主聚会照（Lorenz/Lynen/Ochoa 等）——仅配图素材，无关系可入 |
| 引语红线 | 可引：诺奖演讲"watching and wondering"一句、四问原文列表；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Tinbergen's four questions | 廷贝亨四问 | 因果/发育/功能/演化 |
| proximate / ultimate | 近因/终因 | 四问的现代分组 |
| supernormal stimulus | 超常刺激 | 假蛋/红腹木鱼/纸板蝶 |
| hierarchical model | 层级模型 | 本能释放的级联结构 |
| innate releasing mechanism | 先天释放机制 | 与 Lorenz 共同发展 |
| European beewolf | 欧洲穴蜂（蜂狼） | 博士论文对象 |
| three-spined stickleback | 三刺鱼 | 红腹攻击实验 |
| The Study of Instinct | 《本能的研究》 | 1951 奠基著作 |
| holding therapy | 拥抱疗法 | 晚年争议（无科学支持） |

## 九、背景音乐选择

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配）
- **匹配理由**："野性/原始"贴合其研究对象——刺鱼的红腹、鸥巢的争夺、蜂狼的猎杀，行为学正是直面动物世界的野性；带节奏张力的曲式匹配其实验设计中的锋利巧思。
- **本地路径**：music_audio/ 下 Alex-Productions Savage 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
