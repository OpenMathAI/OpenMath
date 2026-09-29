# 物理学家立传提示词（Rainer Weiss）

> 本文件是 OpenPhysicist 21 世纪批次「物理学家立传提示词」，目标人物：Rainer Weiss（2017 诺贝尔物理学奖，激光干涉引力波探测 + 宇宙微波背景测量）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Rainer Weiss（雷纳·韦斯）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Weiss 篇的视觉主线是**干涉条纹（interference fringes）**——用光的明暗起伏丈量比质子直径小万倍的时空涟漪，是他一生的方法论。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Rainer Weiss（1932-09-29 生于柏林 ~ 2025-08-25 逝于马萨诸塞州剑桥，享年 92 岁）
- **气质关键词**：**引力波探测之父、宇宙微波背景的测绘者、工匠型实验家** —— 2017 诺贝尔物理学奖获奖理由（与 Thorne / Barish 共享，获一半奖金份额）：
  > "for decisive contributions to the LIGO detector and the observation of gravitational waves"（因其对 LIGO 探测器和引力波观测的决定性贡献）
- **设计母题**：**干涉（interference）**。两束光的叠加、相长与相消，对应他双线人生——激光干涉引力波探测与宇宙微波背景测量的耦合，以及流亡者身份与 MIT 工匠传统的融合。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Rainer_Weiss/page.md`
- **第 0 步状态**：page.md 已有本地；`{Dir}.html` 与 `images/` **待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Rainer_Weiss`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 数据库同步：含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1932-09-29 生于德国柏林（魏玛共和国）~ 2025-08-25 逝于美国马萨诸塞州剑桥某医院，享年 92 岁
- 国籍：美国（口径 "German-American physicist"）；生于柏林，犹太+德共党员家庭遭纳粹迫害流亡
- 家庭：父亲 Frederick A. Weiss（医生、神经学家、精神分析学家，犹太人+德国共产党成员，被纳粹驱逐）；母亲 Gertrude Loesner（演员，基督徒）；姑母为社会学家 Hilda Weiss；妹妹为剧作家 Sybille Pearson。先逃布拉格，1938 慕尼黑协定后再度流亡，圣路易斯 Stix 家族协助获得赴美签证；少年在纽约度过
- 教育：Columbia Grammar School（纽约）；MIT（S.B. 1955，PhD 1962）——本科三年级曾辍学（恋情 + 工程/物理方向摇摆），Jerrold Zacharias 介入挽留，先在其实验室当技术员
- 博士导师：Jerrold Zacharias（本科与博士导师一体）；博士论文《Stark Effect and Hyperfine Structure of Hydrogen Fluoride》（1962）
- 任职机构：Tufts University（1960–1962 任教）→ Princeton University（1962–1964 博士后）→ MIT（1964 至今，在 Research Laboratory of Electronics 创建宇宙学与引力研究组）；Louisiana State University adjunct professor；Fermilab Holometer 实验成员
- 关键荣誉：Guggenheim Fellow；Gruber Cosmology Prize（2006，与 Mather 及 COBE 团队）；APS Einstein Prize（2007，与 Ronald Drever）；2016：Special Breakthrough Prize / Gruber / Shaw / Kavli / Harvey（与 Thorne、Drever）；2017：Willis E. Lamb Award / Cocconi Prize（EPS，与 Thorne、Barish）/ Princess of Asturias Award（与 Thorne、Barish）/ 诺贝尔物理学奖（与 Thorne、Barish）/ 挪威科学与文学院院士；Joseph Weber Award（AAS，2018，表彰干涉引力波探测器发明）；AAS Legacy Fellow（2020）；APS Fellow；Clarivate Citation Laureate；Eötvös Loránd 大学与 Almería 大学荣誉博士
- 知名学生：Nergis Mavalvala、Philip K. Chapman、Rana X. Adhikari（infobox 博士生三人；Bruce Allen / Sarah Veatch 为 other notable students，非博士生）
- 核心贡献清单：
  1. 激光干涉引力波探测技术发明（LIGO 基本原理）
  2. 1972 报告《A study of a long Baseline Gravitational Wave Antenna System》，LIGO 蓝图
  3. 1973 气球测量宇宙微波背景谱，证实大爆炸残余辐射的热谱特征
  4. COBE 卫星共同创始人与科学顾问，COBE 科学工作组主席
  5. 1967 引力波探测思想实验（自由质量间光的飞行时间测量）
  6. 基础物理实验检验（Fermilab Holometer：量子尺度时空性质与全息原理普朗克精度检验）
- 关键时间线（15–20 节点）：1932 生于柏林 → 纳粹上台家庭流亡布拉格 → 1938 后再流亡纽约 → Columbia Grammar School → MIT 本科（三年级辍学，Zacharias 挽留）→ 1955 S.B. → 1960–62 Tufts 任教 → 1962 PhD（Zacharias 指导）→ 1962–64 Princeton 博士后 → 1964 MIT 教员（RLE 宇宙学与引力组）→ 1966 发表危机与 Burke 建议 → 1967 引力波思想实验 → 1972 长基线天线报告 / 向 Thorne 提议 LIGO → 1973 军费削减转向 NSF 申请 / CMB 气球测量 → 1970s 原型干涉仪 → 1984 Caltech-MIT LIGO 协议（Drever/Weiss/Thorne 共同领导）→ 2015-09 首次直接探测 → 2016-02 发布会 → 2016 大奖丰收 → 2017 诺贝尔奖 → 2018 Weber Award → 2020 AAS Legacy Fellow → 2025-08-25 去世

### 第 4 步：研究领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gravitational wave detection | 引力波探测 | LIGO 奠基人，2017 诺奖核心 | LIGO 页 |
| 1 | laser interferometry | 激光干涉测量 | 探测器基本原理 | 干涉页 |
| 2 | cosmic microwave background | 宇宙微波背景 | 气球谱测量 + COBE | CMB 页 |
| 3 | experimental gravitation | 实验引力物理 | 基础物理实验检验 | 贡献页 |
| 4 | astrophysics | 天体物理 | field_of_work 明载 | 全篇 |

### 第 4.5 步：社会关系表 【与 yaml 完全一致，仅收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jerrold Zacharias | 对方是导师 | MIT 本科与博士导师（S.B. 1955、PhD 1962），曾干预其辍学挽留 |
| advisor-student | Nergis Mavalvala | 对方是学生 | 博士生（infobox 明载），LIGO 引力波天文学家 |
| advisor-student | Rana X. Adhikari | 对方是学生 | 博士生（infobox 明载） |
| advisor-student | Philip K. Chapman | 对方是学生 | 博士生（infobox 明载） |
| spouse | Rebecca Young | 无向 | 1959 年结婚直至 2025 年去世，育有二子 |
| co-honored | Kip S. Thorne | 无向 | 2017 诺贝尔物理学奖共同得主 |
| co-honored | Barry C. Barish | 无向 | 2017 诺贝尔物理学奖共同得主 |
| co-honored | Ronald Drever | 无向 | 2007 APS Einstein Prize 共同得主（亦共享 2016 Harvey Prize） |
| co-honored | John C. Mather | 无向 | 2006 Gruber Cosmology Prize 共同得主（COBE 团队） |

> 无载不入库：Bruce Allen / Sarah Veatch 为 infobox "other notable students"，非博士生，防噪声不入库；Robert L. Forward 仅「早前工作」提及，无师承/合作记载；Joseph Weber 为被质疑的共振棒先行者，非合作关系；Bernard Burke 仅提建议。

### 第 5 步：配色方案 【人物专属】

- **气质**：精密、克制、光与时空的丈量者
- **配色**：干涉蓝（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 干涉蓝 `#163A63`（本批专属，勿与他篇重复）
  - `badgeA` 引力波探测 — 靛蓝 `#4C5FD5`
  - `badgeB` 激光干涉 — 琥珀 `#E07B30`
  - `badgeC` 宇宙微波背景 — 青绿 `#0E7C7B`
  - `badgeD` 实验引力 — 玫瑰 `#C4204F`
- **背景母题**：干涉条纹场（明暗相间的细条纹带随页错动、局部畸变如时空涟漪掠过），呼应干涉仪臂长变化 $\Delta L$ 的视觉语言

### 第 6 步：幻灯片序列 【人物专属，13 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 引力波探测之父 / Rainer Weiss 1932–2025 + 四色 badge + 右上头像 + 国籍行（Germany → United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 激光干涉引力波探测 / LIGO 蓝图 / CMB 谱测量 / COBE
04  从柏林到纽约 (1932–1955) — 纳粹迫害两次流亡、Stix 家族签证、Columbia Grammar、MIT 辍学插曲与 Zacharias 挽留
05  MIT 博士与早年 (1955–1964) — S.B./PhD 一体师承、Tufts、Princeton 博士后、1964 RLE 建组
06  宇宙微波背景 (1973–1989) — 气球谱测量证实热谱、COBE 共同创始人 / 科学工作组主席
07  引力波思想实验 (1967–1972) — Weber 共振棒争议、自由质量飞行时间思想实验、以激光干涉取代「不可能的时钟」
08  LIGO 诞生 (1972–1984) — 1972 向 Thorne 提议、四地原型机、1984 Caltech-MIT 协议与三人共同领导
09  探测与诺贝尔奖 (2015–2017) — 2015-09 首次直接探测、2016-02 发布会、诺奖份额口径（Weiss 1/2）
10  门生与传承 — Nergis Mavalvala、Rana X. Adhikari、Philip K. Chapman
11  荣誉与认可 — Nobel 2017 · Shaw/Kavli/Breakthrough/Gruber 2016 · Einstein 2007 · Weber Award 2018
12  结尾 — 底部品牌 OpenMathAI
```

公式框建议：page.md 无公式 → 第 07 页放干涉仪自由质量思想实验概念图式（两自由质量 + 光往返 + 「不可能精确的时钟」→ 激光干涉替代），并注明为示意。

### 第 7–8 步：版式要点 + 陷阱表

版式照标杆（身份信息页左头像右网格、每页 make 后 pdftoppm 目检）。**Weiss 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日 | 2025-08-25 逝于马萨诸塞州剑桥（享年 92），本地页面已载；frontmatter 双值无歧义 |
| 国籍口径 | "German-American physicist"、citizenship 美国；生于柏林勿写成「德国物理学家」单口径，badge 写 Germany → United States |
| 诺奖份额 | 官网口径：Weiss 得**一半**奖金，Barish / Thorne 各四分之一；三人并列但份额不同，勿写「平分」 |
| 诺奖分工 | 理由为 "decisive contributions to the LIGO detector and the observation..."，Weiss 侧重**探测器**，勿与 Thorne（理论）/ Barish（领导管理）混写 |
| 库内规范名 | 导师用库内 stub 形式 `Jerrold Zacharias`（id=2121，勿用 Jerrold R. Zacharias）；Mather 用 `John C. Mather`（id=2977，勿用 stub `John Mather` id=426）；Thorne / Barish 新 stub 用 `Kip S. Thorne` / `Barry C. Barish` 与本批 yaml 名一致 |
| 辍学插曲 | 本科三年级辍学原因正文两说并存（恋情为主因 + 工程/物理摇摆），照原文并列，勿写成单一原因 |
| Weber 双重身份 | Joseph Weber 是共振棒主张者（1967 未证实）非合作者；AAS 的 Joseph Weber Award（2018）恰以他命名，两处勿混 |
| Forward | Robert L. Forward 仅有「earlier work」一句，禁写成师承或合作 |
| COBE 头衔 | 「共同创始人 + 科学顾问 + COBE 科学工作组主席」，勿泛写「COBE 负责人」 |
| Thorne 评价引语 | "by a large margin, the most influential person this field has seen" 为 page.md 明载引语，可整句引用并注明出自 Kip Thorne |
| 学生名单 | 博士生仅 Mavalvala / Adhikari / Chapman 三人；Bruce Allen、Sarah Veatch 是 other notable students，勿写成博士生 |
| 家庭成员 | 父母/姑母/妹妹仅身份事实可写，非学术关系不入库 |

### 第 9 步：术语清单 【8–12 条】

| 英文 | 中文 | 风险 |
|------|------|------|
| LIGO | 激光干涉引力波天文台 | 缩写直用，全称 Laser Interferometer Gravitational-Wave Observatory |
| gravitational wave | 引力波 | 勿译「重力波」 |
| laser interferometry | 激光干涉测量 | 探测器基本原理 |
| Weber bar | 韦伯棒 | 共振棒探测器，与 Joseph Weber Award 区分 |
| time of flight | 飞行时间 | 1967 思想实验核心量 |
| free mass | 自由质量 | 思想实验中的测试体 |
| cosmic microwave background | 宇宙微波背景（CMB） | 大爆炸残余辐射 |
| COBE | 宇宙背景探测者卫星 | NASA，1989 发射（发射年份 page.md 无载勿写） |
| kilometer-scale arms | 千米级臂长 | Weiss 对探测器尺度的判断 |
| Special Breakthrough Prize | 基础物理学特别突破奖 | 2016 |
| Shaw Prize | 邵逸夫奖 | 2016，勿与 Kavli 混淆 |
| Princess of Asturias Award | 阿斯图里亚斯亲王奖 | 2017，与 Thorne/Barish 共享 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（标签：纪录片 / 电影 / 稳重）
- **匹配理由**: 「不可见之光」一语双关——引力波本身不可见，而 Weis 的全部工作是用**激光**这束不可见世界的尺子去丈量时空涟漪；纪录片的稳重感匹配其从流亡儿童到诺奖得主的漫长实验生涯（1967 思想实验 → 2015 探测，整整 48 年）。
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **备选**: The Flow of Time（时间感）；Mirage（干涉条纹的抽象感）。

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Rainer_Weiss/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Rainer_Weiss.yaml` | 社会关系入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID → name_en 匹配） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
