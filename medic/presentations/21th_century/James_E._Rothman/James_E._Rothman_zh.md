# 医学家立传提示词（James E. Rothman）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2013 年得主 James E. Rothman（詹姆斯·罗斯曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/James_E._Rothman/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：James Edward Rothman（1950-11-03 生于美国马萨诸塞州哈弗希尔，在世）
- **气质关键词**：**囊泡交通的破译者、细胞"快递系统"的图纸绘制人、耶鲁的掌门人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2013 条目，与 Schekman、Südhof 三人共享同一理由）：
  > "for their discoveries of machinery regulating vesicle traffic, a major transport system in our cells"（因他们发现细胞囊泡运输的调控机制——细胞内主要运输系统）
- **设计母题**：**囊泡的投递（vesicle traffic）**——囊泡从供体膜出芽、精准停靠目标膜并卸货的意象：以芽生小泡+对接锁扣的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/James_E._Rothman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/James_E._Rothman/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=James_E._Rothman_zh`、`VIDEO_NAME=James_E._Rothman_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | vesicle trafficking | 囊泡运输 | 调控囊泡交通的机器，2013 诺奖核心 |
| 1 | cell biology | 细胞生物学 | infobox Fields 明载 |
| 2 | biochemistry | 生物化学 | frontmatter field_of_work；膜蛋白糖基化起步 |
| 3 | neuroscience | 神经科学 | 突触递质释放的分子基础（2010 Kavli） |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eugene Kennedy | 对方 → 导师 | 哈佛生物化学博士导师（1976，膜双层不对称性论文） |
| advisor-student | Harvey Lodish | 对方 → 导师 | MIT 博士后导师（infobox Academic advisors 明载；膜蛋白糖基化） |
| advisor-student | Gero Miesenböck | Rothman → 学生 | 博士后学生（正文 "former postdoctoral students include"） |
| advisor-student | Suzanne Pfeffer | Rothman → 学生 | 博士后学生（正文同上） |
| co-honored | Randy Schekman | 无向 | 2013 诺贝尔生理学或医学奖三人共享（囊泡运输调控机制） |
| co-honored | Thomas C. Südhof | 无向 | 2013 诺贝尔生理学或医学奖三人共享（囊泡运输调控机制） |
| co-honored | Richard Scheller | 无向 | 2010 Kavli 神经科学奖三人共享（与 Südhof） |

**不入库但提示词可叙述**：父 Martin Rothman（儿科医生）与母 Gloria Hartnick（家世叙述）；Amersham/GE Healthcare 顾问职务（机构角色非关系）；ShanghaiTech 特聘职务（机构角色）。

## 五、配色方案 【人物专属】

- **气质**：精密、物流感、分子机器的秩序
- **主色**：`#2E1A47`（耶鲁深夜蓝——组曼门户的厚重）+ 香槟金诺奖色
- **badge 四分类色**：`badgeVesicle` 囊泡运输 深紫 `#2E1A47`；`badgeFusion` 膜融合 青绿 `#0E7C7B`；`badgeNeuro` 突触递质 玫瑰 `#9E2B25`；`badgeDisease` 疾病关联 琥珀 `#C07A2A`
- **背景母题**：芽生小泡+对接锁扣图案，呼应「囊泡的投递」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 囊泡交通的破译者 / James E. Rothman 1950– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1950-11-03 Haverhill、耶鲁 BA 1971 物理、
    哈佛 PhD 1976、耶鲁细胞生物学系主任、诺奖 2013）
03  核心贡献概览 — 囊泡如何认路 / 何时卸货 / 突触递质释放 / 疾病关联
04  马萨诸塞少年 (1950–1967) — Pomfret School 1967、犹太家庭（父儿科医生）
05  耶鲁物理与哈佛生化 (1967–1976) — BA 物理 1971、Eugene Kennedy 门下 PhD 1976
    （膜双层不对称性）
06  MIT 博士后 (1976–1978) — Harvey Lodish 实验室、膜蛋白糖基化
07  斯坦福与普林斯顿 (1978–1991) — 斯坦福生物化学系 1978、普林斯顿 1988–1991
08  Sloan-Kettering 建系 (1991–2003) — 创建细胞生物化学与生物物理学系、SI 副所长
09  哥伦比亚与耶鲁 (2003–) — 哥大教授/化学生物学中心主任 2003、2008 转耶鲁
    （保留哥大部分职务）、纳米生物学研究所所长
10  囊泡如何认路（核心贡献页）— 囊泡携带激素/生长因子的投递逻辑：
    到达正确目的地、在正确时间地点卸货
11  细胞快递的生理意义 — 细胞分裂、脑内神经通讯、胰岛素分泌、营养摄取；
    缺陷导致糖尿病与肉毒中毒等
12  荣誉与认可 — Wieland 1990、King Faisal 1996、Lounsbery 1997、Horwitz/Lasker 2002、
    E. B. Wilson Medal 2010、Kavli 2010、Nobel 2013、英国皇家学会外籍院士
13  三人分工 — Schekman（酵母筛选运输缺陷）、Südhof（递质释放时钟）、
    Rothman（囊泡对接与融合机器）——citation 同一句、侧重分层
14  遗产与结尾 — 从膜不对称到囊泡机器的完整链条；耶鲁细胞生物学的今天
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 两位"导师"阶段不同 | **Eugene Kennedy** 是哈佛博士导师（1976，正文 "working with Eugene Patrick Kennedy"）；**Harvey Lodish** 是 MIT 博士后导师（infobox Academic advisors 明载）——两条 advisor-student 边方向相同但阶段注记不同，立传勿混为同站 |
| 博士后学生 | Gero Miesenböck（光遗传学先驱，正文特别标注 postdoc）与 Suzanne Pfeffer 均为 "former postdoctoral students"——用学生边（postdoc 注记），勿写博士生 |
| 三人分工 | Schekman 酵母遗传筛选、Südhof 突触递质释放、Rothman 囊泡对接融合机器——官方理由同一句，个人侧重分层，勿互串 |
| SNARE 禁写 | SNARE/SNAP/NSF 等具体分子名 **page.md 未载**——立传写"囊泡对接与融合的蛋白质机器"层面即可，不得自补分子术语（无载禁写纪律） |
| 疾病关联 | 囊泡运输缺陷涉及糖尿病与肉毒中毒等（page.md 明载两种）——举例勿越名单 |
| Kavli 与 Nobel 双线 | 2010 Kavli 神经科学奖（与 Scheller、Südhof）与 2013 Nobel（与 Schekman、Südhof）是两条独立奖项线，Südhof 两条都在——年份与同奖人勿串 |
| 机构年表 | 斯坦福 1978 → 普林斯顿 1988–91 → Sloan-Kettering 1991–2003（建系+SI 副所长）→ 哥伦比亚 2003 → 耶鲁 2008（保留哥大部分职务）——五站顺序勿乱 |
| 职务现状 | 耶鲁 Fergus F. Wallace 教授、细胞生物学系主任、纳米生物学研究所所长；兼哥大 adjunct 与 UCL Queen Square 研究教授——多头任职如实呈现 |
| 在世者生卒 | 仅生年 1950-11-03，无卒年——封面用 1950– 开放区间 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| vesicle traffic | 囊泡运输 | 获奖理由核心词（machinery regulating vesicle traffic） |
| vesicle | 囊泡 | 芽状运输小泡，勿译"液泡" |
| budding | 出芽 | 囊泡自供体膜生成 |
| docking / fusion | 对接 / 融合 | Rothman 侧的机器概念 |
| transbilayer asymmetry | 膜双层不对称性 | 博士论文主题 |
| glycosylation | 糖基化 | MIT 博士后方向（膜蛋白） |
| neurotransmitter release | 神经递质释放 | Kavli 获奖主题 |
| insulin secretion | 胰岛素分泌 | 囊泡运输的生理例证 |
| botulism | 肉毒中毒 | 囊泡运输缺陷相关疾病 |
| nanobiology | 纳米生物学 | 其在耶鲁主持的研究所 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：囊泡在正确的时间抵达正确的地点"唤醒"细胞间的通讯——"Awaken" 匹配递质释放的瞬时性与 Rothman 为细胞物流系统绘制图纸的觉醒式贡献。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/James_E._Rothman/Awaken.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
