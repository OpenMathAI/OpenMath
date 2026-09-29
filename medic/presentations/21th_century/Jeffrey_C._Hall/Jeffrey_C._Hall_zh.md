# 医学家立传提示词（Jeffrey C. Hall）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2017 年得主 Jeffrey C. Hall（杰弗里·霍尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Jeffrey_C._Hall/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Jeffrey Connor Hall（1945-05-03 生于纽约布鲁克林，**在世**），美国遗传学家/时间生物学家，布兰迪斯大学生物学荣休教授，现居缅因州剑桥镇
- **气质关键词**：**克隆 period 基因的人、果蝇求偶歌的聆听者、愤而离场的脾气学者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2017 条目，Hall/Rosbash/Young 三人共享）：
  > "for their discoveries of molecular mechanisms controlling the circadian rhythm"（因其发现控制昼夜节律的分子机制）
- **设计母题**：**一只果蝇的午夜与黎明（per gene → PER 蛋白 → TTFL 负反馈环）**——PER 蛋白抑制自身转录形成约 24 小时的分子钟；用「果蝇剪影与 24 小时负反馈环曲线」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Jeffrey_C._Hall/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Jeffrey_C._Hall/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=Jeffrey_C._Hall_zh`、`VIDEO_NAME=Jeffrey_C._Hall_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：封面写 b.1945。Rosbash/Young 两对手方由 med21-batch-09 入库，yaml 已按其 manifest 名建 stub。

## 三、研究领域梳理 + 入库 【人物专属】

**Hall 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | infobox Fields 明载；果蝇行为遗传学 | 身份页 |
| 1 | chronobiology | 时间生物学（昼夜节律） | 2017 诺奖核心，PER/TTFL 分子钟 | 核心页 |
| 2 | neurogenetics | 神经遗传学 | 果蝇求偶行为的神经系统定位 | 核心页 |
| 3 | behavioral genetics | 行为遗传学 | 求偶歌节律、fruitless 主控基因 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Philip Ives | 对方 → 本科毕业论文导师 | 阿默斯特学院，果蝇重组/易位研究，自述影响最大者之一 |
| advisor-student | Lawrence Sandler | 对方 → 博士导师 | 华盛顿大学（1971，果蝇减数分裂染色体行为的遗传控制） |
| advisor-student | Herschel L. Roman | 对方 → 指导教师 | 华盛顿大学博士阶段指导教师，鼓励赴 Benzer 实验室并推荐教职 |
| advisor-student | Seymour Benzer | 对方 → 博士后导师 | 加州理工学院（1971，正向遗传学先驱） |
| colleague | Doug Kankel | 无向 | Benzer 实验室博士后同事，教其果蝇神经解剖学与神经化学 |
| advisor-student | Bambos Kyriacou | Hall → 博士后合作者 | 实验室博士后，共同发现果蝇求偶歌约一分钟节律 |
| colleague | Paul Hardin | 无向 | 1990 年三人共同发现 PER 自抑制，提出 TTFL 负反馈模型 |
| colleague | Michael Rosbash | 无向 | 布兰迪斯大学长期合作同事，昼夜节律分子机制并肩者 |
| co-honored | Michael Rosbash | 无向 | 2017 诺贝尔生理学或医学奖三人共享 |
| co-honored | Michael W. Young | 无向 | 2017 诺贝尔生理学或医学奖三人共享 |

**在世者诚实值说明**：Hall 在世；以上 10 边全部 page.md 明载。**不入库但提示词可叙述**：Bruce Baker（斯坦福）与 Barbara Taylor（俄勒冈州立）——fruitless 克隆三人组，合著合作按择要口径未建边；Florian von Schilcher（1970 年代末求偶歌神经系统合作）；Ron Konopka（period 突变体原创者，文献渊源非个人关系）；父亲 Joseph W. Hall（美联社驻参议院记者，早年影响）；Susan Renn/Jae Park/Paul Taghert（1997/1999 合著者）。

## 五、配色方案 【人物专属】

- **气质**：果蝇的琥珀翅、凌晨与黄昏的双色、布兰迪斯的学院绿
- **主色**：`#37474F`（蓝灰——果蝇复眼与凌晨四点的实验室）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePer` period 基因 — 蓝灰 `#37474F`
  - `badgeClock` 分子钟 TTFL — 深青 `#14647E`
  - `badgeCourt` 求偶神经遗传学 — 琥珀 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：果蝇剪影与 24 小时正弦负反馈曲线，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — period 基因的克隆者 / Jeffrey C. Hall b.1945 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、布鲁克林出身、阿默斯特学院/华盛顿大学、
    布兰迪斯/缅因大学任职、诺奖 2017、核心领域）
03  核心贡献概览 — 求偶歌节律 / PER 自抑制 TTFL / fruitless 主控基因 / PDF 细胞同步
04  华盛顿郊区的报童之子 (1945–1963) — 父亲美联社记者、Walter Johnson 高中、原计划学医
05  阿默斯特与 Ives 实验室 (1963–1967) — 从医学转向生物学、果蝇重组研究、"影响最大者之一"
06  华盛顿大学双导师 (1967–1971) — Sandler 门下读博、Roman 的实验室文化与人生指点
07  Benzer 实验室 (1971–1974) — 加州理工博士后、Kankel 传授神经解剖学、未发表即离开
08  布兰迪斯与求偶歌 (1974–1980s) — 1974 助理教授、与 von Schilcher 定位求偶歌脑区、
    与 Kyriacou 发现约一分钟节律
09  period 基因的三种节律（核心贡献页）— Konopka 突变体：perS≈40 秒 / perL≈76 秒 / perO 无节律
10  1990：PER 自抑制与 TTFL（核心页）— 与 Rosbash/Hardin 的 Nature 论文、负反馈转录-翻译环
11  从 per 到 fru — 1990s 克隆 fruitless 主控调节基因、CRY 光受体、CLOCK/CYC 异二聚体（1998）
12  2003：PDF 与细胞同步 — 色素分散因子、sLNv 腹侧外侧神经元为主振荡器
13  2017 诺奖：三人共享 — 与 Rosbash（布兰迪斯同事）+ Young（洛克菲勒）共享，获奖理由逐字呈现
14  遗产与结尾 — 直言不讳的退场（经费体制之弊）、GSJ 讲台上的 eccentric 讲授 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Jeffrey C. Hall"**；1945-05-03 生于纽约（布鲁克林），**在世**——封面写 b.1945；现居缅因州 Cambridge, Maine，勿写成"逝于" |
| 2017 三人共享 | 与 Rosbash（其布兰迪斯长期同事）+ Young（洛克菲勒，平行独立工作）共享；Rosbash=colleague+co-honored 双边，Young=仅 co-honored（page.md 无两人直接合作记载，勿加边） |
| 四条师承链 | Ives（本科毕业论文）→ Sandler（博士导师）+ Roman（博士阶段指导教师）→ Benzer（博士后导师）——四条 advisor-student 边并行，勿合并；Sandler 页面链接名 "Larry Sandler"，**yaml 用 infobox 形式 Lawrence Sandler** |
| Kyriacou 方向 | Bambos Kyriacou 是 Hall 实验室的博士后 fellow（Hall→学生方向），note 写"实验室博士后合作者"，方向勿颠倒 |
| Konopka 不建边 | period 突变体由 Ron Konopka 于 1960 年代末产生，Hall 借用其突变体研究求偶歌——文献渊源，不建 influence 边 |
| 合著者择要 | Hardin（1990 TTFL 三人组）与 Kyriacou 建边；von Schilcher/Baker/Taylor/Renn/Park/Taghert 不入库，在"不入库"段交代口径 |
| "Academic adversities" 叙事 | Hall 因经费体制与学界层级之弊离开时间生物学一线——page.md 明载其不满，可客观转述，**无引语可引，禁编引语**（page.md 全篇无直接引语） |
| 果蝇数据 | perS 短周期约 40 秒、perL 长周期约 76 秒、perO 无规则振荡——三数字勿串；正常求偶歌周期约 1 分钟 |
| TTFL 时间线 | 1990 PER 自抑制/TTFL（与 Rosbash/Hardin）→1997 TTFL 基因周身表达（Renn/Park/Rosbash/Taghert 组）→1998 CRY 光受体+per/tim 调控+CLOCK/CYC 异二聚体→2003 PDF 同步发现（sLNvs 主振荡器）——年份勿串 |
| Wieschaus 防混 | page.md 果蝇图片说明误写 "the object of Wieschaus's science"（Wieschaus 为 1995 诺奖得主，与本页无关）——**图片说明噪声，勿在正文引用此句** |
| 学位口径 | Amherst BA → 华盛顿大学 MS+PhD（1971）——博士论文题目为重组缺陷突变体遗传分析，方向是减数分裂/染色体行为而非节律，勿倒置 |
| 教学风格 | "eccentric lecturing style"（特立独行的讲课风格）page.md 明载可写一笔 |
| 对手方名 | Rosbash="Michael Rosbash"、Young="Michael W. Young"（batch-09 manifest 形式，yaml 已建 stub 待其回填） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| circadian rhythm | 昼夜节律 | 获奖理由核心词 |
| period gene (per) | period 基因 | 1980s 被 Hall/Rosbash/Young 各自团队克隆 |
| PER protein | PER 蛋白 | 抑制自身转录的负反馈核心 |
| TTFL | 转录-翻译负反馈环 | 分子钟核心机制模型 |
| timeless (tim) | timeless 基因 | 与 per 并联的节律基因 |
| CLOCK/CYC heterodimer | CLOCK/CYC 异二聚体 | 经 PAS 域二聚、结合 E box |
| cryptochrome (CRY) | 隐花色素 | 光受体/振荡器双重角色 |
| fruitless (fru) | fruitless 基因 | 求偶行为主控调节基因 |
| pigment dispersing factor (PDF) | 色素分散因子 | 细胞间同步信号（2003） |
| courtship song | 求偶歌 | 雄蝇振翅脉冲，约 1 分钟周期 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Hall 的科学岁月有一种"逆行者"的孤独——遗传学方法闯入传统时间生物学遭遇冷眼、因经费体制愤而退场、最终在缅因州乡下安住；Lonesome 的孤高气质对应这份不妥协，也对应凌晨与午夜时分那只被观察的果蝇——分子钟本身，就是孤独的 24 小时循环。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Jeffrey_C._Hall/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
