# 物理学家立传提示词（Adam G. Riess / 亚当·里斯）

> **OpenPhysicist 21 世纪批次 · batch 6-5**。本文件为 Adam G. Riess（2011 诺贝尔物理学奖，宇宙加速膨胀共同发现者、哈勃张力中心人物）的人物专属立传提示词，结构对齐标杆 `Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Adam Guy Riess（亚当·盖伊·里斯），2011 诺贝尔物理学奖得主（与 Perlmutter/Schmidt 共享）、SH0ES 团队领队。
- **设计哲学**：物理学家立传必须有「身份信息页」与研究领域结构化表达；Riess 篇另需突出「一作论文改写宇宙剧本 + 哈勃张力搅动标准模型」的当代性。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Adam G. Riess（1969-12-16 生于美国华盛顿特区，在世）
- **气质关键词**：**1998 论文一作、SH0ES 领队、哈勃张力中心** —— 2011 诺贝尔物理学奖官方获奖理由：
  > "For the discovery of the accelerating expansion of the Universe through observations of distant supernovae"（因通过遥远超新星观测发现宇宙加速膨胀）
- **设计母题**：**两种刻度（two rulers）**。近距超新星与 CMB 推出的哈勃常数不一致——本篇视觉母题是两把并置而读数分歧的量尺，呼应哈勃张力（Hubble tension）。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Adam_G._Riess/page.md`（**page.md 已有本地**）
- **待下载**：`Adam_G._Riess.html` 与 `images/`（第 0 步执行）；Wikipedia URL：`https://en.wikipedia.org/wiki/Adam_G._Riess`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地；❌ html 与 images/ 待下载（Wikipedia URL 见上）
- 事实基准（以 page.md 为准）：
  - 生卒：1969-12-16 生于华盛顿特区，在世；犹太家庭，在新泽西州 Warren Township 长大
  - 家庭：父 Michael Riess（1931–2007）服役海军后经营冷冻食品分销公司；母 Doris Riess 为临床心理学家；祖父 Curt Martin Riess 为记者/战地记者；姐姐 Gail Saltz 为精神科医生，姐姐 Holly Hagerman 为艺术家
  - 教育：Watchung Hills Regional High School 1988；1987 新泽西州长科学学校；MIT BS 1992（Phi Beta Kappa，Phi Delta Theta 兄弟会）；哈佛 PhD 1996，论文《Type Ia Supernova Multicolor Light Curve Shapes》，1999 获 Trumpler Award
  - 博士导师（frontmatter 明载两位）：Robert Kirshner、William H. Press
  - 任职：伯克利 Miller Fellow 1996–1999（加速膨胀首篇奠基论文在此期间发表）→ 1999 入空间望远镜科学研究所（STScI）→ 2006 入约翰斯·霍普金斯大学 → 2016 Bloomberg Distinguished Professor
  - 团队：与 Schmidt 共同领导 High-Z Team 1998 年研究（Riess et al. 1998 一作）；2002–2007 领导 Higher-Z SN Team（HST 找 z>1 超新星，证明减速→加速转变、排除天体物理污染）；2005 起领导 SH0ES 团队测哈勃常数（精度近 1%，与 CMB 模型预测矛盾——哈勃张力）
  - 关键荣誉：Trumpler Award 1999；Bok Prize 2001（哈佛）；Helen B. Warner Prize（infobox 作 2002、正文作 2003）；Sackler Prize 物理学 2004；Shaw Prize 天文学 2006（三人共享）；MacArthur "Genius" Grant 2008；美国科学院院士 2009；Albert Einstein Medal 2011（与 Perlmutter 同获）；Nobel 2011；Golden Plate 2012；Breakthrough Prize 2015；美国天文学会 Fellow 2020
  - 引用量级：Google Scholar 超 13.7 万次引用、h 指数 130；最高引论文（1998 加速膨胀）被引超 2.8 万次
  - 配偶：Nancy Joy Schondorf（1998 结婚），子女 Noah 与 Gabrielle
- 关键时间线（18 节点）：

| 时间 | 事件 |
|------|------|
| 1969-12-16 | 生于华盛顿特区，犹太家庭，长于新泽西 Warren Township |
| 1987 | 新泽西州长科学学校 |
| 1988 | Watchung Hills Regional High School 毕业 |
| 1992 | MIT BS（Phi Beta Kappa） |
| 1996 | 哈佛 PhD（Kirshner 与 Press 双导师），Ia 型超新星多色光变曲线 |
| 1996–1999 | 伯克利 Miller Fellow；加速膨胀首篇奠基论文在此期间发表 |
| 1998 | Riess et al. 1998（AJ 116, 1009）一作论文；Science 年度突破 |
| 1999 | Trumpler Award；入空间望远镜科学研究所（STScI） |
| 2001 | 哈佛 Bok Prize |
| 2002/2003 | Helen B. Warner Prize（infobox 2002、正文 2003 两说） |
| 2002–2007 | 领导 Higher-Z SN Team（HST，z>1，证明减速→加速转变） |
| 2004 | Sackler Prize（发现宇宙加速） |
| 2005 | 创建并领导 SH0ES 团队 |
| 2006 | 与 Perlmutter/Schmidt 共享 Shaw 天文学奖；入约翰斯·霍普金斯大学 |
| 2008–2009 | MacArthur "Genius" Grant 2008；美国科学院院士 2009 |
| 2011 | 诺贝尔物理学奖；与 Perlmutter 同获 Albert Einstein Medal |
| 2012–2016 | Golden Plate 2012；Breakthrough Prize 2015；Bloomberg Distinguished Professor 2016 |
| 2020 | 美国天文学会 Fellow；哈勃张力辩论持续 |

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Adam_G._Riess/` 与 `images/` 子目录（提示词文件已就位）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，仅改 `MAIN=Adam_G._Riess_zh`、`VIDEO_NAME=Adam_G._Riess_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像为 2011 年照片；优先 Wikipedia REST API `page/summary` 查 infobox 原图名后经 Special:FilePath 下载 500px 到 `images/`
- 下载后 `file` 验证格式（JFIF density 异常需 sips 改 72dpi）；404 则用装饰圆占位并在提示词补记
- 插图可选：`Shaw2006astro.jpg`（三人组合照）与 2011 Nobel lecture 照

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cosmology | 宇宙学 | 加速膨胀、暗能量 | 核心页 |
| 1 | type Ia supernova | Ia 型超新星 | 多色光变曲线、标准化测距 | 博士页 |
| 2 | astrophysics | 天体物理 | infobox field_of_work 明载 | 领域页 |
| 3 | hubble constant | 哈勃常数 | SH0ES 团队 1% 精度测量 | 张力页 |
| 4 | dark energy | 暗能量 | 加速膨胀的推论 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致，只收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Kirshner | 师→生（博士导师） | 哈佛博士导师（论文监督两位之一） |
| advisor-student | William H. Press | 师→生（博士导师） | frontmatter 明载的另一位博士导师 |
| advisor-student | Daniel Scolnic | Riess→学生 | infobox 明载博士生 |
| co-honored | Saul Perlmutter | 无向 | 2006 Shaw 与 2011 诺贝尔物理学奖共同得主 |
| co-honored | Brian P. Schmidt | 无向 | 2006 Shaw 与 2011 诺贝尔物理学奖共同得主，1998 论文共同领导 |
| spouse | Nancy Joy Schondorf | 无向 | 妻子，1998 年结婚 |

### 第 5 步：设计配色方案

- **气质**：精确、锐利、当下进行时
- **主色**：张力深红 `#7A1E28`（批内唯一，哈勃张力之色）+ 诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeCosmo` 宇宙学 — 深紫 `#5B3A8E`
  - `badgeSN` Ia 型超新星 — 琥珀 `#E07B30`
  - `badgeH0` 哈勃常数 — 青绿 `#0E7C7B`
  - `badgeDE` 暗能量 — 靛蓝 `#4C5FD5`
- **背景母题**：两把分歧的量尺 + 光变曲线（multicolor light curve 既是其博士论文也是测距方法的根基）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）、封面有国籍（底部状态栏三要素）。
2. 必须有身份信息页：左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域），事实取自 page.md，不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 宇宙加速的共同发现者 / Adam G. Riess 1969– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 加速膨胀 / Ia 光变曲线 / Higher-Z / SH0ES
04  早年：新泽西 (1969–1992) — 州长科学学校、MIT
05  哈佛读博 (1992–1996) — Kirshner 与 Press 双导师、光变曲线方法
06  1998：那篇一作论文（核心贡献页）— Riess et al. 1998
07  Higher-Z 团队 (2002–2007) — HST、z>1、减速到加速
08  荣誉前奏 (1999–2009) — Trumpler/Warner/Sackler/MacArthur/NAS
09  2011 诺贝尔奖 — 三人共享口径
10  SH0ES 与哈勃张力 — 1% 精度、与 CMB 的分歧
11  荣誉与认可 — Shaw 2006 · Breakthrough 2015 · AAS Fellow 2020
12  引用量级 — h 指数 130、最高引 2.8 万次
13  遗产：标准模型的压力测试
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 表格页负间距：顶部 −0.35cm、arraystretch 0.78–0.82；量尺示意用概念图式（page.md 无公式）。

| 陷阱 | 说明 |
|------|------|
| 官方理由 | Nobel citation 为 "For the discovery of the accelerating expansion of the Universe through observations of distant supernovae"（三人同句）；page.md 导语作 "for providing evidence that..."，两者勿混用 |
| Warner Prize 年份 | infobox 奖项行作 2002、正文段落作 2003——两说并存，引用时任选其一并保持全篇一致，勿自造第三种 |
| 一作身份 | 1998 关键论文（Riess et al. 1998, AJ 116, 1009）Riess 是**一作**；High-Z Team 的共同领导是 Schmidt——署名顺序勿颠倒 |
| 双导师 | frontmatter doctoral_advisor 两位：Robert Kirshner + William H. Press，正文确认"supervised by both"——两条均入库 advisor |
| Bok Prize | 2001 年获（哈佛）；Schmidt 的 Bok 是 2000 年——勿互换 |
| Einstein Medal | 2011 年 Riess 与 Perlmutter 为共同得主（page.md 明载），勿写成单独获得 |
| 家庭成员 | 姐姐 Gail Saltz（精神科医生）与祖父 Curt Martin Riess（战地记者）可写；勿把祖父与任何物理学家混淆 |
| 哈勃张力 | 表述为"近距超新星测量与 CMB 推断的膨胀率存在分歧、对标准宇宙学模型构成压力"；勿写成"哈勃常数已错"或"标准模型已被推翻" |
| 媒体花絮 | NPR 问答节目 Wait Wait... Don't Tell Me! 2011 出场可作花絮一句，勿扩展 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| accelerating universe | 加速膨胀的宇宙 | 1998 年发现 |
| dark energy | 暗能量 | 加速膨胀的推论 |
| Type Ia supernova | Ia 型超新星 | 标准烛光 |
| multicolor light curve | 多色光变曲线 | 博士论文核心 |
| distance indicator | 距离指示器 | 尘埃与不均匀性改正 |
| Hubble constant | 哈勃常数 H0 | SH0ES 测量对象 |
| Hubble tension | 哈勃张力 | 近距 vs CMB 分歧 |
| SH0ES | SH0ES 团队 | 2005 年起领队 |
| Higher-Z SN Team | 更高红移团队 | 2002–2007，HST |
| Space Telescope Science Institute | 空间望远镜科学研究所 | STScI，1999 入职 |
| Bloomberg Distinguished Professor | 彭博杰出教授 | 2016 受聘 |
| Breakthrough of the Year | 《科学》年度突破 | 1998 加速膨胀 |

---

## 四、背景音乐选择 【人物专属建议】

- **选定曲目**：**The Flow of Time** — Alex-Productions（56k views，高受众 / 时间感 / 纪录片）
- **匹配理由**："时间之流"匹配其研究的对象——宇宙膨胀率本身就是时间的刻度；从 1998 一作论文到今日哈勃张力，是其不断给宇宙"重新校表"的三十年；纪录片的沉稳感匹配测量科学家的精确气质。
- **本地路径**：`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`
- **备选**：The Invisible Light（纪录片/稳重，匹配暗能量之不可见）、Falling Apart（渐进/情感，匹配标准模型承压的悬念）

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Adam_G._Riess/page.md` | 事实基准（唯一数据源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Adam_G._Riess.yaml` | 社会关系/领域入库（本批新建） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
