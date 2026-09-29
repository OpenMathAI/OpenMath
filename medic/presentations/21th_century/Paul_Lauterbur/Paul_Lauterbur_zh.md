# 医学家立传提示词（Paul Lauterbur）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2003 年得主 Paul Lauterbur（保罗·劳特伯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Paul_Lauterbur/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Paul Christian Lauterbur（1929-05-06 生于俄亥俄州 Sidney ~ 2007-03-27 逝于伊利诺伊州 Urbana，享年 77 岁）
- **气质关键词**：**磁共振成像之父、餐巾纸上的灵感、被拒稿的 Classic Nature 论文**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2003 条目，Lauterbur/Mansfield 两人共享）：
  > "for their discoveries concerning magnetic resonance imaging"（因其关于磁共振成像的发现）
- **设计母题**：**梯度磁场下的空间编码（magnetic field gradients）**——磁场沿空间渐变，让核磁共振信号各自"报出坐标"；用「等势线网格中亮起的成像点」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Paul_Lauterbur/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Paul_Lauterbur/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=Paul_Lauterbur_zh`、`VIDEO_NAME=Paul_Lauterbur_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Lauterbur 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | magnetic resonance imaging | 磁共振成像 | 梯度磁场空间定位，2003 诺奖核心 | 核心页 |
| 1 | nuclear magnetic resonance | 核磁共振 | 军旅时期起接触，MRI 的物理基础 | 早年页 |
| 2 | chemistry | 化学 | 本科/博士专业，UIUC 化学教授 | 身份页 |
| 3 | radiology | 放射学 | MRI 的临床应用领域 | 核心页 |
| 4 | biophysics | 生物物理学 | metadata occupation 有载，UIUC 兼聘 | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Joan Dawson | 无向 | 妻子，1985 同赴伊利诺伊大学厄巴纳-香槟分校，共创生物医学磁共振实验室（BMRL） |
| co-honored | Peter Mansfield | 无向 | 2003 诺贝尔生理学或医学奖共享（关于磁共振成像的发现） |
| controversy | Raymond Damadian | 无向 | 2003 诺奖争议，Damadian 登报抗议委员会未将其列入得主 |
| influence | Herman Carr | 无向 | Lauterbur 在 Carr 一维 MR 成像技术基础上发展出 2D 与 3D 成像 |
| influence | Robert Gabillard | 无向 | 采用 Gabillard 1952 博士论文的磁场梯度定位思想 |

**不入库但提示词可叙述**：1952 年诺贝尔物理学奖得主 Felix Bloch 与 Edward Purcell（NMR 原理的建立者，仅背景叙述，非个人关系）；Silvano Casulli（以 Lauterbur 命名小行星的天文学家）；George W. Bush（2003 白宫合影）；硕士阶段无导师可考（page.md 未载博士导师，**不入库 advisor 边**）。

## 五、配色方案 【人物专属】

- **气质**：磁体的深蓝、梯度的秩序、临床影像的清亮
- **主色**：`#1E3A5F`（磁体深蓝——超导磁体与夜色中的实验室）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMRI` 磁共振成像 — 深蓝 `#1E3A5F`
  - `badgeNMR` 核磁共振 — 青灰 `#0E7490`
  - `badgeImage` 影像革命 — 琥珀 `#D97706`
  - `badgeHonor` 荣誉传承 — 暗红 `#8C2F1B`
- **背景母题**：等势线网格与渐变磁力线，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 磁共振成像之父 / Paul Lauterbur 1929–2007 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Sidney 出身、Case 理工学士/匹兹堡博士、
    Stony Brook/UIUC 任职、诺奖 2003、核心领域）
03  核心贡献概览 — 梯度编码 / 首批 MRI 图像 / Nature 论文风波 / 与 Mansfield 的接力
04  Sidney 少年与地下室实验室 (1929–1951) — 卢森堡裔、自制实验室、老师课后纵容实验
05  军旅与 NMR 结缘 (1950s) — 陆军化学中心、早期 NMR 机器、离役前已发 4 篇论文
06  Mellon 研究所与匹兹堡博士 (1950s–1962) — Dow Corning 实验室、在职读博、1962 PhD
07  Stony Brook 岁月 (1963–1985) — 副教授起步、1969-70 斯坦福访问、夜里借用化学系 NMR 仪
08  餐巾纸上的 MRI（核心贡献页）— Eat'n Park 大男孩餐厅、梯度磁场定位、Gabillard 1952 思想
09  首批图像：蛤蜊、青椒与重水（核心页）— 女儿捡的 4mm 蛤蜊、两种水第一次被影像区分
10  被拒稿的经典 — Nature 退稿、坚持复审、1998 经典论文；"科学史半部是拒稿史"引语
11  Damadian 与 Carr — 1971 T1/T2 论文的启发、扩展 Carr 一维成像为 2D/3D
12  2003 诺奖与争议 — 与 Mansfield 共享；Damadian 整版广告 "The Shameful Wrong That Must Be Righted"
13  UIUC 与家庭 (1985–2007) — 与妻子 Joan Dawson 共创 BMRL、22 年执教至逝世
14  遗产与结尾 — 每天拯救生命的 MRI、荣誉年表、小行星 Paullauterbur + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | 全名 Paul Christian Lauterbur，**yaml/入库用 manifest 形式 "Paul Lauterbur"** |
| 2003 两人共享 | 与 Peter Mansfield 共享同一句获奖理由 "for their discoveries concerning magnetic resonance imaging"；两人工作属接力而非合作（Mansfield 把投影重建法推进为频率/相位编码+傅里叶变换），勿写成共同实验 |
| 无博士导师边 | page.md 只载匹兹堡 1962 年 PhD，**未载导师姓名**——勿杜撰 advisor-student 边 |
| 思想来源归属 | 梯度定位思想来自 Robert Gabillard（1952 博士论文），成像灵感受 Damadian 1971 论文触动、技术承接 Herman Carr 一维成像——三条影响链 page.md 明载，叙述时各归其位，勿写成 Lauterbur 凭空发明 |
| Damadian 争议口径 | Damadian 登三大报整版广告称诺奖遗漏他；NYT 社论立场=承认其早期专利，但 Lauterbur/Mansfield 拓展 Carr 技术才是诺奖级工作——两条都写，勿单边定性；1988 National Medal of Technology 两人确实共享 |
| Nature 拒稿引语 | "You could write the entire history of science in the last 50 years in terms of papers rejected by Science or Nature." 为 page.md 明载英文原话，可引；1986 年关于 Damadian 报告的引语亦明载可引 |
| 首批图像内容 | 4mm 蛤蜊（女儿在长岛海峡捡的）、青椒、普通水中重水试管——"区分两种水"是关键卖点，因人体大部分是水 |
| 专利命运反差 | SUNY 决定不为 Lauterbur 的 MRI 构想申请专利（后悔）；诺丁汉大学为 Mansfield 申请专利使其致富——反差如实写 |
| 死因 | 2007-03-27 死于肾病（kidney disease），逝于 Urbana 家中，勿写医院 |
| 荣誉年份 | Lasker 1984、Kettering+Gairdner 1985、Harvey 1986、NMS+IEEE Medal of Honor 1987、National Medal of Technology 1988（与 Damadian 共享）、Bower 1990（首得主）、Kyoto 1994、Dickson 1993、NAS 化学服务奖 2001、发明家名人堂 2007——勿串 |
| 国籍口径 | metadata 仅 United States；本人卢森堡裔（Luxembourgish ancestry）是血统叙述非国籍 |
| 2003 同届合影 | 白宫合影六位 2003 美国诺奖得主含 Agre/Leggett/Abrikosov 等——插图可用但图注勿张冠李戴 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| magnetic resonance imaging (MRI) | 磁共振成像 | 获奖理由核心词 |
| nuclear magnetic resonance (NMR) | 核磁共振 | 1952 物理奖原理基础 |
| magnetic field gradient | 磁场梯度 | 空间定位的核心思想，源自 Gabillard |
| projection-reconstruction | 投影重建 | Lauterbur 原始方法，后被 Mansfield 方法取代 |
| frequency and phase encoding | 频率与相位编码 | Mansfield 的推进 |
| Fourier transformation | 傅里叶变换 | 由 Larmor 进动支撑的图像重建 |
| Larmor precession | 拉莫尔进动 | 核磁共振的基础物理 |
| T1/T2 relaxation | T1/T2 弛豫 | Damadian 1971 观察肿瘤组织差异的量 |
| glomerulus | （嗅觉）肾小球 | 勿与 Axel/Buck 篇术语混淆，本篇不涉及 |
| heavy water | 重水 | 首批图像区分重水与普通水 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从地下室自制实验室到餐巾纸上画出第一台 MRI 的构想，Lauterbur 的一生是一场向"看见人体内部"的远征；Expedition 的行进感对应梯度磁场里一步步逼近的空间编码，也对应他把核磁共振从化学结构分析带进临床影像的开拓航程。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Paul_Lauterbur/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
