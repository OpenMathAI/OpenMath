# 物理学家立传提示词（Saul Perlmutter / 索尔·珀尔马特）

> **OpenPhysicist 21 世纪批次 · batch 6-3**。本文件为 Saul Perlmutter（2011 诺贝尔物理学奖，宇宙加速膨胀发现者）的人物专属立传提示词，结构对齐标杆 `Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Saul Perlmutter（索尔·珀尔马特），2011 诺贝尔物理学奖得主（独得一半，Schmidt/Riess 共享另一半）。
- **设计哲学**：物理学家立传必须有「身份信息页」与研究领域结构化表达；Perlmutter 篇另需突出「超新星宇宙学项目掌门 + 两个竞争团队的世纪竞赛」的叙事张力。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Saul Perlmutter（1959-09-22 生于美国伊利诺伊州香槟-厄巴纳，在世）
- **气质关键词**：**暗能量猎手、超新星巡天掌门、逆直觉的坚持者** —— 2011 诺贝尔物理学奖官方获奖理由：
  > "For the discovery of the accelerating expansion of the Universe through observations of distant supernovae"（因通过遥远超新星观测发现宇宙加速膨胀）
- **设计母题**：**加速远离的光（receding light）**。超新星光谱的红移与亮度衰减是本篇的视觉母题——宇宙不仅在膨胀，而且在加速膨胀；退行的星系、拉长的波长、渐暗的 Ia 型超新星。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Saul_Perlmutter/page.md`（**page.md 已有本地**）
- **待下载**：`Saul_Perlmutter.html` 与 `images/`（第 0 步执行）；Wikipedia URL：`https://en.wikipedia.org/wiki/Saul_Perlmutter`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地；❌ html 与 images/ 待下载（Wikipedia URL 见上）
- 事实基准（以 page.md 为准）：
  - 生卒：1959-09-22 生于香槟-厄巴纳（伊利诺伊），在世
  - 家庭：父 Daniel D. Perlmutter 为宾夕法尼亚大学化学与生物分子工程荣休教授；母 Felice (Feige) D. Perlmutter 为天普大学社会管理学院荣休教授；外祖父 Samuel Davidson 为意第绪语教师（比萨拉比亚→加拿大→纽约）；妹妹 Shira Perlmutter 为律师/法学教授/第 14 任美国版权登记官，妹妹 Tova 为非营利机构高管
  - 成长：费城 Mount Airy 街区；贵格会学校（Greene Street Friends School 小学 + Germantown Friends School 7–12 年级）
  - 教育：哈佛物理学 AB（1981，magna cum laude）；伯克利物理学 PhD（1986），论文《An Astrometric Search for a Stellar Companion to the Sun》（找 Nemesis 假想伴星）
  - 博士导师：Richard A. Muller；自动超新星巡天的构想源自 1968 诺奖得主 Luis Alvarez（与导师分享此想法）
  - 任职：劳伦斯伯克利国家实验室（LBNL）超新星宇宙学项目（SCP）负责人；加州大学伯克利分校物理学教授（Franklin W. and Karen Weber Dabby 讲席）；2021 起总统科学技术顾问委员会（PCAST）成员
  - 关键荣誉：E. O. Lawrence Award 2002；加州年度科学家 2003；John Scott Award 2005；Padua Prize 2005；Shaw Prize 天文学 2006（三人共享）；Feltrinelli 国际奖 2006；Gruber 宇宙学奖 2007（两团队共享）；Miller Senior Fellow 2010；Albert Einstein Medal 2011（与 Riess 同获）；Nobel 2011（独得奖金一半，Riess/Schmidt 共享另一半）；Golden Plate 2014；Breakthrough Prize 基础物理学 2015；2020 年 DOE 超级计算机以 Perlmutter 命名
  - 配偶：Laura Nelson（伯克利人类学家），女儿 Noa
- 关键时间线（18 节点）：

| 时间 | 事件 |
|------|------|
| 1959-09-22 | 生于伊利诺伊州香槟-厄巴纳 |
| 童年 | 长于费城 Mount Airy，读贵格会学校（Greene Street + Germantown Friends） |
| 1981 | 哈佛物理学 AB（magna cum laude） |
| 1986 | 伯克利 PhD（Muller 门下），Nemesis 假想伴星巡天论文 |
| 1980s 中 | Alvarez 向其导师分享自动超新星巡天构想 |
| 1990 | SCP 首份技术报告（Berkeley/Anglo-Australian 高红移超新星巡天） |
| 1994 | 《Discovery of the Most Distant Supernovae and the Quest for Omega》 |
| 1997-12 | 远距超新星（半个宇宙年龄）发现报告 |
| 1998 | 与 High-Z Team 几乎同时发表宇宙加速膨胀结论 |
| 1999 | Perlmutter et al. 1999（SCP 团队定义论文） |
| 2002 | 美国能源部 E. O. Lawrence Award；加州年度科学家 2003 |
| 2005 | John Scott Award；Padua Prize |
| 2006 | 与 Riess/Schmidt 共享 Shaw 天文学奖；Feltrinelli 国际奖 |
| 2007 | 与两团队共享 Gruber 宇宙学奖（50 万美元） |
| 2010 | Miller Senior Fellow（伯克利 Miller Institute） |
| 2011 | 诺贝尔物理学奖（独得一半奖金）；与 Riess 同获 Albert Einstein Medal |
| 2014–2015 | Golden Plate 2014；Breakthrough Prize 2015 |
| 2020–2021 | DOE 超算命名 Perlmutter 2020；PCAST 成员 2021 |

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Saul_Perlmutter/` 与 `images/` 子目录（提示词文件已就位）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，仅改 `MAIN=Saul_Perlmutter_zh`、`VIDEO_NAME=Saul_Perlmutter_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像为 2024 年照片（`Saul_Perlmutter_in_2024_at_Berkeley_Lab_02.jpg`，原图 8454px 可取 500px）；优先 Special:FilePath 下载到 `images/`
- 下载后 `file` 验证格式（JFIF density 异常需 sips 改 72dpi）；404 则用装饰圆占位并在提示词补记
- 插图可选：`Shaw2006astro.jpg`（三人组 2006 Shaw 合照， Nobels 页核心插图）与 2011 Nobel lecture 照（`Nobel_Prize_2011-Nobel_lectures_KVA-DSC_7973.jpg`）

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cosmology | 宇宙学 | 加速膨胀、宇宙学常数 | 核心页 |
| 1 | dark energy | 暗能量 | 加速膨胀的推论与主线 | 核心页 |
| 2 | astrophysics | 天体物理 | infobox field_of_work 明载 | 领域页 |
| 3 | type Ia supernova | Ia 型超新星 | 标准烛光测距 | 方法页 |
| 4 | automated telescope survey | 自动化巡天 | 自动望远镜找超新星 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致，只收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard A. Muller | 师→生（博士导师） | 伯克利博士导师，Nemesis 巡天论文 |
| influence | Luis Walter Alvarez | 无向 | 超新星自动巡天构想的来源（向其导师分享） |
| co-honored | Brian P. Schmidt | 无向 | 2006 Shaw 与 2011 诺贝尔物理学奖共同得主 |
| co-honored | Adam G. Riess | 无向 | 2006 Shaw 与 2011 诺贝尔物理学奖共同得主 |
| spouse | Laura Nelson | 无向 | 妻子，伯克利人类学家 |

### 第 5 步：设计配色方案

- **气质**：深邃、宇宙尺度、逆直觉的冷静
- **主色**：深紫罗兰 `#4A2E6F`（批内唯一，暗能量之色）+ 诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeCosmo` 宇宙学 — 深紫 `#5B3A8E`
  - `badgeDE` 暗能量 — 靛蓝 `#4C5FD5`
  - `badgeSN` Ia 型超新星 — 琥珀 `#E07B30`
  - `badgeSurvey` 自动巡天 — 青绿 `#0E7C7B`
- **背景母题**：渐暗的星点 + 红移光谱线（亮度-红移图即 1998 年那篇论文的核心图像）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）、封面有国籍（底部状态栏三要素）。
2. 必须有身份信息页：左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域），事实取自 page.md，不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 暗能量猎手 / Saul Perlmutter 1959– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 加速膨胀 / 暗能量 / Ia 标准烛光 / SCP
04  早年：费城贵格会学校 (1959–1981) — 双教授家庭、哈佛 AB
05  伯克利读博 (1981–1986) — Muller 门下、Nemesis 巡天、Alvarez 构想
06  超新星宇宙学项目 SCP — 自动望远镜、标准烛光原理
07  两队竞赛 (1994–1998) — SCP vs High-Z Team
08  1998：宇宙在加速膨胀（核心贡献页）
09  荣誉前奏 (2002–2010) — Lawrence/Shaw/Gruber
10  2011 诺贝尔奖 — 独得一半奖金、Einstein Medal 同年
11  暗能量时代 — SNAP、后续证据线
12  荣誉与认可 — Breakthrough 2015 · PCAST 2021 · Perlmutter 超算
13  遗产：重新点燃宇宙学
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 表格页负间距：顶部 −0.35cm、arraystretch 0.78–0.82；亮度-红移示意用概念图式（page.md 无公式）。

| 陷阱 | 说明 |
|------|------|
| 奖金分配 | 2011 诺贝尔奖金 1000 万瑞典克朗：Perlmutter 独得一半，Riess/Schmidt 共享另一半——这是「SCP 首发论文」口径，勿写成三人平分 |
| 官方理由 | Nobel citation 为 "For the discovery of the accelerating expansion of the Universe through observations of distant supernovae"（三人同句）；page.md 导语另作 "for providing evidence that the expansion of the universe is accelerating"，两者勿混用 |
| 团队竞赛 | SCP（Perlmutter 主导）与 High-Z Team（Schmidt 领队/Riess 一作）是竞争团队、两报告相隔数周发表——"同时"指几乎同时，勿写成合作或抄袭 |
| Alvarez 角色 | Alvarez 只是把自动超新星巡天**构想**分享给其导师 Richard Muller（1968 诺奖得主），并非 Perlmutter 导师，也非合作者——关系类型用 influence |
| 高中口径 | 贵格会学校（Greene Street + Germantown Friends），勿写成"犹太学校"；家庭为犹太裔但教育经历是贵格会 |
| 妹妹身份 | Shira Perlmutter 是第 14 任美国版权登记官（律师/法学教授），勿与 Tova 混淆 |
| 大爆炸理论剧 | 《生活大爆炸》台词提及可作花絮但须标明为剧集桥段，勿当事实引用 |
| 气候项目 | 参加 Berkeley Earth 地表温度项目按 page.md 写，勿扩展其气候立场 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| accelerating universe | 加速膨胀的宇宙 | 1998 年发现 |
| dark energy | 暗能量 | 加速膨胀的推论 |
| Type Ia supernova | Ia 型超新星 | 标准烛光 |
| standard candle | 标准烛光 | 内禀光度已知的天体 |
| Chandrasekhar limit | 钱德拉塞卡极限 | 白矮星质量上限 |
| redshift | 红移 | 退行速度指示 |
| Supernova Cosmology Project | 超新星宇宙学项目 | SCP，LBNL 团队 |
| High-Z Supernova Search Team | 高红移超新星搜索队 | 竞争团队 |
| Nemesis | 涅墨西斯假想伴星 | 博士论文对象 |
| cosmological constant | 宇宙学常数 | Λ，爱因斯坦项 |
| Supernova/Acceleration Probe | SNAP | 超卫星计划负责人项目 |
| PCAST | 总统科学技术顾问委员会 | 2021 起成员 |

---

## 四、背景音乐选择 【人物专属建议】

- **选定曲目**：**Eternals** — Alex-Productions（49k views，较高受众 / 宏大 / 深远）
- **匹配理由**："永恒"匹配宇宙学的时间尺度——发现的是百亿年前超新星的退行；暗能量研究重写了宇宙的终局叙事，是典型的基础理论长期影响；曲风的深远感匹配亮度-红移图的沉默张力。
- **本地路径**：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`
- **备选**：The Flow of Time（时间感/纪录片，匹配宇宙时间线）、Mirage（梦幻/抽象，匹配暗能量之不可见）

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Saul_Perlmutter/page.md` | 事实基准（唯一数据源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Saul_Perlmutter.yaml` | 社会关系/领域入库（本批新建） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
