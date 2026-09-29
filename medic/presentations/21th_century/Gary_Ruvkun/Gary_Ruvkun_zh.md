# 医学家立传提示词（Gary Ruvkun）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2024 年得主 Gary Ruvkun（加里·鲁夫昆）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Gary_Ruvkun/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Gary Bruce Ruvkun（1952-03-26 生于美国加州伯克利，在世）
- **气质关键词**：**miRNA 机制的破译者、let-7 的发现者、衰老与地外生命的双线探索者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2024 条目，与 Victor Ambros 共享同一理由）：
  > "for the discovery of microRNA and its role in post-transcriptional gene regulation"（因发现 microRNA 及其在转录后基因调控中的作用）
- **设计母题**：**不完全的配对（imperfect base-pairing）**——miRNA 与靶 mRNA 之间不完美碱基配对却精准抑制翻译的意象：以错位咬合的双链图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Gary_Ruvkun/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Gary_Ruvkun/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Gary_Ruvkun_zh`、`VIDEO_NAME=Gary_Ruvkun_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | microRNA | 微 RNA | lin-4 机制与 let-7 保守性，2024 诺奖核心 |
| 1 | molecular biology | 分子生物学 | frontmatter field_of_work |
| 2 | genetics | 遗传学 | frontmatter field_of_work；C. elegans 遗传分析 |
| 3 | aging biology | 衰老生物学 | 胰岛素样信号通路调控代谢与寿命 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frederick M. Ausubel | 对方 → 导师 | 哈佛博士导师（1982，固氮 NIF 基因；infobox 明载） |
| advisor-student | H. Robert Horvitz | 对方 → 导师 | MIT 博士后导师；库内规范名 id=4751 |
| advisor-student | Walter Gilbert | 对方 → 导师 | 哈佛博士后导师；库内规范名 id=1127 |
| colleague | Victor Ambros | 无向 | lin-4/lin-14 互补配对合作发现者，1993 同期 Cell 论文 |
| colleague | Craig Mello | 无向 | 两实验室合作证明 RNAi 与 miRNA 共用机器组件；库内 id=4783 |
| co-honored | Victor Ambros | 无向 | 2024 诺贝尔生理学或医学奖共享（microRNA 与转录后基因调控） |
| co-honored | Cynthia Kenyon | 无向 | 2011 Dan David 奖共享（衰老研究） |

**不入库但提示词可叙述**：Hamilton 与 Baulcombe（植物 siRNA 发现，领域汇聚叙事）；Klass/Johnson（daf-2/age-1 先行工作）；Dicer/PIWI（分子组件非人物）；Maria Zuber、Chris Carr、Michael Finney（SETG 合作，项目叙述不建边）；父 Samuel 与母 Dora（家世叙述）。

## 五、配色方案 【人物专属】

- **气质**：缜密、双线的求知欲、从线虫到火星的好奇
- **主色**：`#16324F`（马萨诸塞总医院深蓝——长木街的学术底色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeMiRNA` microRNA 深蓝 `#16324F`；`badgeLet7` let-7 保守性 青绿 `#0E7C7B`；`badgeAging` 衰老与代谢 琥珀 `#C07A2A`；`badgeSETG` 地外生命 玫瑰 `#8C2F1B`
- **背景母题**：错位咬合的双链图案，呼应「不完全的配对」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — miRNA 机制的破译者 / Gary Ruvkun 1952– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1952-03-26 伯克利、UC Berkeley BA 1973
    生物物理、哈佛 PhD 1982、麻省总医院/哈佛医学院教授、诺奖 2024）
03  核心贡献概览 — lin-4 机制 / let-7 与保守性 / 胰岛素样信号与衰老 / SETG
04  伯克利少年 (1952–1973) — 犹太家庭、UC Berkeley 生物物理 BA 1973
05  哈佛博士：Ausubel 门下 (1973–1982) — 苜蓿根瘤菌共生固氮 NIF 基因的分子遗传分析
06  双站博士后 (1982–) — MIT Horvitz 实验室 + 哈佛 Walter Gilbert；C. elegans 转向
07  1993：机制的另一半（核心贡献页）— lin-14 功能获得突变缺失 3'UTR 保守元件；
    与 Ambros 比对发现 lin-4 不完全碱基配对抑制翻译；同期 Cell 背靠背
08  2000：let-7（核心贡献页）— 第二个 miRNA 靶向 lin-41；序列与调控跨动物谱系保守、
    直达人类——miRNA 是普遍规律
09  miRNA 与 siRNA 合流 — 1999 植物 siRNA 同尺寸发现；与 Mello 实验室合作证明
    Dicer/PIWI 组件共用；2003 哺乳动物神经元 miRNA
10  衰老与代谢 — 胰岛素样信号（daf-2/age-1→daf-16 FOXO）调控线虫寿命；
    全基因组 RNAi 文库筛选；糖尿病药物靶点远景
11  SETG：寻找地外基因组 — 与 Zuber/Carr/Finney 研制火星 DNA 测序仪；
    泛种论式论证（2019）；NASA 使命倡议
12  荣誉与认可 — Rosenstiel 2004、NAS 2008、Gairdner/Franklin/Lasker 2008、
    Horwitz/Massry 2009、Dan David 2011、Janssen 2012、Wolf 2014、
    Breakthrough 2015、March of Dimes 2016、美国哲学会 2019、Nobel 2024
13  先亚当诺奖的师门佳话 — 博士后导师 Horvitz 是 2002 诺奖得主；
    本 yaml 先于其 2024 诺奖入库（2026-09-29 batch-01 由 Horvitz 学生边建 stub）
14  遗产与结尾 — 小 RNA 的大世界：从翻译抑制到人类疾病与衰老的普遍语言
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 导师三层结构 | 博士导师 **Frederick M. Ausubel**（infobox Doctoral advisor 明载，固氮基因）；博士后导师 **Horvitz（MIT）与 Gilbert（哈佛）**（正文明载两站）——frontmatter 把 Baltimore/Horvitz 列为 doctoral_advisor 系 metadata 噪声，以 page.md infobox/正文为准：Ausubel 博士 + 两站博士后导师 |
| 与 Ambros 的分工 | Ambros 发现 lin-4 编码小 RNA（"什么"）；Ruvkun 揭示其经不完全配对抑制 lin-14 翻译的机制（"怎么"）+ 发现 let-7 及保守性——诺奖共享但侧重分层，勿互串 |
| 发现年份双口径 | Ruvkun 篇作 lin-4 小 RNA "discovered in 1992 by Ambros' lab"、1993 发表——本篇忠于 Ruvkun 页面表述，Ambros 篇忠于其页面（1993），两篇各按本人页面写、避免交叉改写 |
| let-7 归属 | 2000 年 let-7 鉴定与跨谱系保守性均为 **Ruvkun 实验室**独立成果——这是 Ruvkun 侧最重的诺奖拼图，勿让渡给 Ambros |
| 衰老线与诺奖线分开 | 胰岛素样信号/衰老工作（daf-2/age-1/daf-16、FOXO）**不在获奖理由内**——立传分线呈现，勿混入诺奖理由 |
| Kenyon 定位 | Cynthia Kenyon 是 daf-2 延寿先行的作者之一 + 2011 Dan David 共享——co-honored 边承载，Klass/Johnson 仅叙述 |
| SETG 定位 | 地外基因组搜索是严肃研究方向（page.md 有专节）——可写，但注明是 Ruvkun 的"第二曲线"，与诺奖工作分开；泛种论表述照页面措辞，勿引申 |
| 在世者生卒 | 仅生年 1952-03-26，无卒年——封面用 1952– 开放区间 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| imperfect base-pairing | 不完全碱基配对 | miRNA 抑制翻译的关键特征 |
| lin-4 / lin-14 | lin-4 / lin-14 | 首对 miRNA-靶基因 |
| let-7 | let-7 | 第二个 miRNA，保守性证明 |
| 3' UTR | 3' 非翻译区 | miRNA 结合位点 |
| gain-of-function mutation | 功能获得突变 | lin-14 3'UTR 缺失分析的切入点 |
| daf-2 / age-1 / daf-16 | 衰老通路基因 | 胰岛素样信号轴 |
| FOXO | FOXO 转录因子 | daf-16 哺乳类同源 |
| RNA interference (RNAi) | RNA 干扰 | 与 miRNA 机制合流 |
| Dicer / PIWI | Dicer / PIWI 蛋白 | miRNA 与 siRNA 共用组件 |
| SETG | 地外基因组搜索 | 火星测序仪项目 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从根瘤菌固氮基因到线虫小 RNA、从衰老时钟到火星测序仪——Ruvkun 的科学人生是一场不断换地图的远征；"Expedition" 匹配其跨领域的好奇心与探索气质。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Gary_Ruvkun/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
