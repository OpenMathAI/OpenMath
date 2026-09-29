# 医学家立传提示词（Eric Kandel）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 2000 年得主（与 Carlsson/Greengard 三人共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Eric Richard Kandel（1929-11-07 生于维也纳，在世）
- **气质关键词**：**记忆存储分子机制的破译者、海兔学习与记忆大师、《追寻记忆的痕迹》的书写者、维也纳之子** —— 2000 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Carlsson/Greengard 共享同一句）：
  > "for their discoveries concerning signal transduction in the nervous system"
  > （因他们关于神经系统内信号转导的发现）
- **设计母题**：**海兔的鳃缩反射（the gill-withdrawal reflex）**。一只海蛞蝓教会人类记忆如何存储——习惯化、敏感化、经典条件化在单个神经节里上演。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Eric_Kandel/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Eric_Kandel/page.md`；目录 `medic/presentations/20th_century/Eric_Kandel/`；Makefile 改 `MAIN=Eric_Kandel_zh`；肖像优先 images.txt 所列 Commons 图（2013 照等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Eric_Kandel.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 职业主领域（infobox Fields） | 封面 |
| 1 | learning and memory | 学习与记忆 | 海兔模型，诺奖核心 | 核心页 |
| 2 | psychiatry | 精神病学 | MD 训练与执业出身 | 求学页 |
| 3 | cognitive science writing | 认知科学写作 | 《Principles of Neural Science》与《In Search of Memory》 | 著作页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Harry Grundfest | 无向 | 哥大实验室初识研究（1955-56 六个月），示波器与传导速度 |
| influence | Ladislav Tauc | 无向 | 1962 巴黎师从其学习海兔制备 |
| co-honored | Arvid Carlsson | 无向 | 2000 诺贝尔生理学或医学奖三人共享（神经系统信号转导） |
| colleague | Paul Greengard | 无向 | 1980 年合作证明 PKA 作用于该生化通路 |
| co-honored | Paul Greengard | 无向 | 2000 诺贝尔生理学或医学奖三人共享（神经系统信号转导） |
| spouse | Denise Bystryn | 无向 | 1956 结婚（神经科学家 Denise Kandel） |
| advisor-student | James H. Schwartz | 本人→学生 | infobox 明载学生；1964-72 组员，合著《Principles of Neural Science》 |
| advisor-student | Tom Carew | 本人→学生 | infobox 明载学生；1970-83 组员，SfN 前主席 |
| advisor-student | Kelsey C. Martin | 本人→学生 | infobox 明载学生；1992-99 组员，UCLA 医学院院长 |
| advisor-student | Priya Rajasethupathy | 本人→学生 | infobox 明载学生 |
| advisor-student | Scott A. Small | 本人→学生 | infobox 明载学生 |
| advisor-student | Christopher Pittenger | 本人→学生 | infobox 明载学生 |
| advisor-student | John H. (Jack) Byrne | 本人→学生 | 实验室名录 1970-75；UTHealth 神经科学中心主任、《Learning and Memory》创始主编 |
| advisor-student | Edgar T. Walters | 本人→学生 | 实验室名录 1974-80；UTHealth 教授 |

> 对手方规范名：`Alan Lloyd Hodgkin` 式教训本篇对应为 `Harry Grundfest`/`Ladislav Tauc`/`Denise Bystryn` 等均无库内记录按 page.md 形式新建；`Arvid Carlsson` 与 Greengard 篇共用同一 stub（batch-34 复用镜像合并）；`Paul Greengard` 与本批 Greengard 篇同键——**Kandel 侧多一条 colleague 边（1980 PKA 合作，page.md 明载），Greengard 侧无对称行**。**relations=14 为诚实值**（infobox 6 学生全收 + 名录 2 人，Tinbergen 前例）。

## 五、配色方案

- **气质**：维也纳九岁的逃亡少年 + 从历史与文学转向精神分析再转向分子的三次转身 + 海兔神经节的诗意
- **主色**：记忆深蓝紫 `#3A3F7A`（海兔神经与黄昏多瑙河的复合色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 海兔学习模型 — 海洋青 `#2E7D8C`
  - `badgeB` cAMP/5-HT 与敏感化 — 信号橙 `#C97B2D`
  - `badgeC` CREB 与长时记忆 — 转录紫 `#5E4B8B`
  - `badgeD` 维也纳 1900 与《The Age of Insight》 — 人文金 `#C9A227`
- **背景母题**：低透明度海兔剪影与鳃缩反射回路 + 突触连接数增减的意象。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 记忆存储分子机制的破译者 / Eric Kandel b.1929 + badge + 右上头像 + 国籍行（United States，生于奥地利）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年维也纳、Erasmus Hall、哈佛历史与文学、NYU MD 1955（正文 1952 入学）、NIH/NYU/哥大、诺奖 2000）
03  核心贡献概览 — 海兔学习模型 / 习惯化-敏感化-条件化的突触机制 / cAMP-PKA-CREB 链 / 短期→长期记忆的转换
04  维也纳与逃亡 (1929–1939) — 玩具店之家、1938 Anschluss 后犹太人境遇恶化、九岁与兄 Ludwig 乘 Gerolstein 号赴布鲁克林、全家团聚
05  三次转身 (1944–1956) — Flatbush 犹太学堂、哈佛历史与文学（论三位德国作家对国家社会主义的态度）、文学导师 Viëtor 骤逝与 Anna Kris/弗洛伊德圈的影响、1952 入 NYU 医学院
06  Grundfest 与电生理起点 (1955–1957) — 哥大六个月初识研究（示波器/传导速度与轴突直径）、Kuffler 无脊椎思路启发、跟 Stanley Crain 学微电极
07  NIH 与海马 (1957–1960) — 海马锥体神经元胞内记录、与 Alden Spencer 发现树突动作电位与回返抑制、HM 病例（Scoville/Milner）背景、意识到记忆在于突触连接的改变
08  巴黎与海兔（核心页一）— 1962 从 Tauc 学海兔；行为主义大师 Lorenz/Tinbergen/von Frisch 比较行为学的启示——选简单动物模型研究学习的突触机制（ senior 学界普遍怀疑的前卫决定）
09  习惯化、敏感化与条件化（核心页二）— NYU 期与 Kupferman/Pinsker 建立鳃缩反射范式、1965 突触前易化、1981 Walters/Abrams/Hawkins 扩展到经典条件化
10  与 Greengard 的会师 (1966–1980) — Schwartz 合作生化分析、cAMP 在海兔神经节生成、5-HT-第二信使通路、1980 与 Greengard 合作证明 PKA 作用、Siegelbaum 钾通道
11  CREB 与长时记忆 — 1983 协建哥大 HHMI、CREB 转录因子与长时记忆存储（与 Glanzman/Bailey 合作）、突触数目增长；2008 与 Pollak "习得性安全"抗抑郁效应
12  2000 诺贝尔奖 — 与 Carlsson、Greengard 共享；官方理由全句；Lasker 1983/Wolf 1999/Gerard 1997/Gairdner 1987/NAS 评审奖 1988 预演
13  荣誉与著作长廊 — 《Principles of Neural Science》1981 起六版、回忆录《In Search of Memory》2006 洛杉矶时报图书奖、《The Age of Insight》2012 维也纳 1900；NAS 1974、HHMI 高级研究员 1984-2022
14  在世者与维也纳和解 — 现居纽约；"a Jewish-American Nobel"原话与 Klestil 总统通话、Doktor-Karl-Lueger-Ring 更名倡议（2012 落实）、维也纳荣誉市民 2009；奥地利授勋 2005/2012/2024
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 三人共享 | 2000 三人共享同一句理由；分工：Carlsson=多巴胺神经递质、Greengard=信号转导级联、Kandel=记忆存储的突触机制——三线并列勿混写 |
| Greengard 双边 | Kandel 侧有 colleague（1980 PKA 合作，page.md 明载）+ co-honored 两行；Greengard 侧仅 co-honored——不对称系诚实值 |
| 学生全收 | infobox Notable students 6 人（Schwartz/Carew/Martin/Rajasethupathy/Small/Pittenger）全收 + 实验室名录 Byrne/Walters 2 人（page.md 给出成就）——共 8 条 advisor-student（Tinbergen 前例）；Siegelbaum/Kupferman/Pinsker 等正文散提者不入库（陷阱表留痕） |
| 无博士导师 | MD 训练无 PhD 导师——Grundfest 系研究启蒙（六个月）用 influence、Tauc 系海兔制备学习（1962 巴黎）用 influence，均勿升师承 |
| Lorenz/Tinbergen/von Frisch | 仅"比较行为学研究揭示简单学习"的学术背景提及——不入库（三人已在本项目库中，防误连） |
| 维也纳叙事（最高敏感）| Anschluss/犹太迫害系史实客观一句；"a Jewish-American Nobel" 原话与 Lueger 更名倡议系 page.md 明载可引——**只作个人经历陈述，不展开政治评价** |
| 在世者 | 在世：无卒日；relations=14 诚实值（关系多因学生名录全收）；HHMI 1984-2022 收官年份勿漏 |
| MD 年份 | infobox 无 MD 年份；正文"1952 入学/毕业入 NIH 1957"——时间线按正文叙事，勿外推具体毕业年 |
| 引语红线 | 可引：Jewish-American Nobel 段原话、Klestil 通话概述、Pearl Meister 同款公益线（Greengard 篇呼应）；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Aplysia californica | 加州海兔 | 诺奖核心动物模型 |
| gill-withdrawal reflex | 鳃缩反射 | 学习范式载体 |
| habituation / sensitization | 习惯化/敏感化 | 简单学习形式 |
| classical conditioning | 经典条件化 | 1981 扩展 |
| serotonin (5-HT) | 5-羟色胺 | 敏感化的调制递质 |
| cAMP / PKA | cAMP/蛋白激酶 A | 与 Greengard 会师点 |
| CREB | cAMP 反应元件结合蛋白 | 长时记忆转录开关 |
| hippocampus | 海马 | 早期 NIH 研究对象 |
| Anschluss | （德奥合并）| 1938 历史背景（客观一句） |
| Hebbian theory | 赫布学习理论 | 实验支持章节 |

## 九、背景音乐选择

- **选定曲目**：**Mirage** — Alex-Productions（manifest 预分配）
- **匹配理由**："海市蜃楼"贴合记忆的本质——并非实景重现而是突触连接的重塑，也贴合九岁离开的维也纳在暮年书页中的重现；迷离而克制的曲式承载"追寻记忆的痕迹"的一生。
- **本地路径**：music_audio/ 下 Alex-Productions Mirage 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
