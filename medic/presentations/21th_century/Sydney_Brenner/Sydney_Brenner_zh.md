# 医学家立传提示词（Sydney Brenner）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2002 年得主 Sydney Brenner（悉尼·布伦纳）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Sydney_Brenner/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sydney Brenner（1927-01-13 生于南非 Germiston ~ 2019-04-05 逝于新加坡，享年 92 岁）
- **气质关键词**：**线虫的驯化者、信使 RNA 的助产士、分子生物学的先知**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2002 条目，三人共享同一理由）：
  > "for their discoveries concerning 'genetic regulation of organ development and programmed cell death '"（因他们发现器官发育和细胞程序性死亡的遗传调控）
- **设计母题**：**一条线虫的细胞谱系树（C. elegans lineage tree）**——从单个受精卵分叉至 959 个体细胞的树状图：以细线分叉生长的谱系树作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Sydney_Brenner/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Sydney_Brenner/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Sydney_Brenner_zh`、`VIDEO_NAME=Sydney_Brenner_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Brenner 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | 遗传密码/mRNA/接头假说，1960s 奠基性贡献 | 封面、核心页 |
| 1 | genetics | 遗传学 | 遗传密码三联性证明、基因共线性 | 核心页 |
| 2 | developmental biology | 发育生物学 | 建立 C. elegans 模式生物，2002 诺奖核心 | 核心页 |
| 3 | biotechnology | 生物技术 | 核酸矩阵分析、Molecular Sciences Institute 创立 | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Cyril Norman Hinshelwood | 对方 → 导师 | 牛津 Exeter College DPhil 导师（1954，大肠杆菌噬菌体抗性的物理化学研究） |
| advisor-student | Gerald M. Rubin | Brenner → 学生 | infobox Doctoral students 明载 |
| advisor-student | John G. White | Brenner → 学生 | infobox Doctoral students 明载 |
| spouse | May Covitz | 无向 | 1952-12 结婚至 2010-01 妻逝；子女 Belinda/Carla/Stefan 及继子 Jonathan Balkind |
| colleague | Francis Crick | 无向 | 卡文迪什实验室与 MRC LMB 长期并肩（mRNA 概念、三联密码等）；库内规范名 id=1796 |
| colleague | John Sulston | 无向 | LMB 同事，C. elegans 细胞谱系合作；库内 stub id=4265（其本人 yaml 由 med21-batch-02 批次回填 QID） |
| colleague | H. Robert Horvitz | 无向 | 1974 起 Horvitz 在 LMB 与其共事（C. elegans 遗传学与细胞谱系） |
| co-honored | H. Robert Horvitz | 无向 | 2002 诺贝尔生理学或医学奖三人共享（器官发育与程序性细胞死亡的遗传调控） |
| co-honored | John Sulston | 无向 | 2002 诺贝尔生理学或医学奖三人共享（器官发育与程序性细胞死亡的遗传调控） |

**不入库但提示词可叙述**：Francis Crick/James Watson 的 DNA 模型 1953 首批观摩（Dunitz/Hodgkin/Orgel/Oughton 同行，一次性事件）；François Jacob、Matthew Meselson（mRNA 验证合作，1960）；Leslie Barnett、Richard Watts-Tobin（1961 三联码实验合作者）；George Pieczenik、Aaron Klug（计算机矩阵分析/密码起源论文）；Esther/Joshua Lederberg、Gunther Stent（1965 合影人物）；Errol Friedberg（传记作者）；Sarabhai/Stretton/Bolle（1964 amber 突变合作）——均为 page.md 明载但关系属单篇合作/事件，不设边。

## 五、配色方案 【人物专属】

- **气质**：锐利、诙谐、显微镜下的秩序
- **主色**：`#1E4E79`（剑桥蓝——LMB 的分子生物学摇篮）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeWorm` 线虫与谱系 — 青绿 `#0E7C7B`
  - `badgeCode` 遗传密码 — 深蓝 `#1E4E79`
  - `badgeMrna` mRNA 与接头假说 — 琥珀 `#C07A2A`
  - `badgeSingapore` 新加坡事业 — 玫瑰 `#A63A2B`
- **背景母题**：从受精卵分叉的细线谱系树，呼应「C. elegans 的 959 个体细胞」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 线虫的驯化者 / Sydney Brenner 1927–2019 + 四色 badge + 右上头像 + 国籍行（South Africa / United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1927-01-13 Germiston ~ 2019-04-05 新加坡、
    Witwatersrand MSc/MBBCh、牛津 DPhil 1954、MRC LMB 二十年、诺奖 2002、核心领域）
03  核心贡献概览 — mRNA / 三联密码 / C. elegans / 程序性细胞死亡的铺垫
04  杰米斯顿少年 (1927–1945) — 立陶宛/拉脱维亚犹太移民之子、15 岁入 Witwatersrand、
    改读解剖生理 BSc、实验室技术员自持
05  牛津 DPhil (1949–1954) — 1851 奖学金、Exeter College、Hinshelwood 门下噬菌体抗性物理化学
06  1953 年 4 月：第一批见到 DNA 模型 — 与 Dunitz/Hodgkin/Orgel/Oughton 同赴剑桥
07  分子生物学的黄金年代 (1960s)（核心贡献页）— 证明重叠密码不可能、命名接头假说 (1955)、
    1960-04 与 Crick/Jacob 对话孕育 mRNA 概念、与 Jacob/Meselson 证实其存在
08  三联密码 (1961) — Crick–Brenner–Barnett–Watts-Tobin 移码突变实验
09  驯化线虫 (1960s–)（核心贡献页）— 选定 C. elegans：简单/易批量培养/便于遗传分析、
    UNC 筛选、诺奖讲演 "Nature's Gift to Science"（2002-12-08）
10  晚期机构 — 1976 加入 Salk；1996 创立 Berkeley Molecular Sciences Institute；
    2005 OIST 首任校长；Scripps 遗传学教授
11  新加坡与远东 — 新加坡生物医学研究战略贡献、2006 国科奖章、2017 旭日大绶章、
    兰花 Dendrobium Sydney Brenner（1998）
12  荣誉与认可 — Lasker 1971、Royal Medal 1974、Kyoto 1990、Copley 1991、Nobel 2002、
    Dan David 2002、March of Dimes 2002、Mapungubwe 金勋章
13  Loose Ends 与文风 — Current Biology 专栏、"Uncle Syd" 的诙谐、慷慨予人的思想慷慨者
14  遗产与结尾 — C. elegans 全球研究共同体、Caenorhabditis brenneri 与 Euprymna brenneri 的致敬
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 国籍双口径 | Nobel 官方口径（citations json）country=**South Africa**；项目总表列 United Kingdom；page.md frontmatter 双值 ["South Africa","United Kingdom"]、正文首句 "was a South African biologist"——裁定：yaml 双国籍 SA(rank0)+UK(rank1)，正文以"南非出生的英国科学家/南非生物学家"表述，两口径并存在封面国籍行 |
| 1953 观摩 vs 参与 | Brenner 是 1953-04 **第一批见到 DNA 模型的人之一**，不是双螺旋共同发现者——勿与 Watson/Crick 混同 |
| mRNA 概念 | 1960-04 与 Crick、François Jacob 的对话中形成 mRNA 概念，随后与 Jacob、Meselson 证实存在——三方各有贡献，勿独归 Brenner |
| 接头假说 | "adaptor hypothesis" 的**命名**由 Brenner 1955 给出（概念源头经 Gamow 至 Crick 提议 tRNA）——写"命名"勿写"发明" |
| 三联密码实验 | 1961 实验作者序 Crick, Brenner, Barnett, Watts-Tobin——Crick 为首，勿写成"Brenner 单独证明三联码" |
| 共享理由 | 官方理由三人同一句 "for their discoveries concerning 'genetic regulation of organ development and programmed cell death '"；Brenner 的贡献主要是建立 C. elegans 体系（并含程序性细胞死亡铺垫）——个人侧重勿越界到 Horvitz 的 ced 基因细节 |
| Hinshelwood 是化学家 | 博士导师 Cyril Norman Hinshelwood 是牛津化学教授（1956 诺贝尔化学奖得主），用库内规范名 'Cyril Norman Hinshelwood'（id=3871）；Brenner DPhil 题目是细菌噬菌体抗性的物理化学 |
| 卒地 | 逝于**新加坡**（2019-04-05，享年 92），勿写剑桥/Ely（Ely 是长居地） |
| 三位诺奖作者论文 | 与 Crick、Klug、Pieczenik 的密码起源论文"三位作者独立成为诺奖得主"——属趣闻可写，勿与 2002 共享奖混淆 |
| 学生边界 | infobox 仅 Gerald M. Rubin 与 John G. White 两位博士生入边；Leslie Barnett 等长期助手/合作者不设师生边 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Caenorhabditis elegans | 秀丽隐杆线虫 | Brenner 建立的模式生物，勿译"蛔虫" |
| messenger RNA (mRNA) | 信使 RNA | 1960 概念孕育、同年实验证实 |
| adaptor hypothesis | 接头假说 | 1955 Brenner 命名，后落实为 tRNA |
| genetic code | 遗传密码 | 三联性 1961 证明 |
| frameshift mutation | 移码突变 | 1961 实验的发现 |
| amber mutant | 琥珀突变体 | 1964 共线性证明的 T4 工具 |
| cell lineage | 细胞谱系 | C. elegans 研究的骨架概念 |
| programmed cell death | 程序性细胞死亡 | 2002 诺奖理由核心词 |
| central dogma | 中心法则 | 信息流向核酸→蛋白， adaptor 洞见的延伸表述 |
| C. brenneri / Euprymna brenneri | 以 Brenner 命名的物种 | 线虫与短尾乌贼各一，致敬性命名 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从 1953 年双螺旋模型前的观摩者到 2002 年诺奖讲演 "Nature's Gift to Science"——Brenner 的一生纵贯分子生物学整个黄金年代；"Nostalgia" 匹配这条跨越七十年、从 Germ斯顿到剑桥再到新加坡的回望式传记线。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Sydney_Brenner/Nostalgia.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
