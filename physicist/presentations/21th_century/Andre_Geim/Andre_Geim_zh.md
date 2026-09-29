# 物理学家立传提示词（Andre Geim / 安德烈·海姆）

> **OpenPhysicist 21 世纪批次 · batch 6-1**。本文件为 Andre Geim（2010 诺贝尔物理学奖，石墨烯发现者）的人物专属立传提示词，结构对齐标杆 `Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir Andre Konstantin Geim（安德烈·康斯坦丁诺维奇·海姆），2010 诺贝尔物理学奖得主（与 Konstantin Novoselov 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与研究领域结构化表达；Geim 篇另需突出「诺奖 + 搞笑诺贝尔双冠」的幽默实验家气质。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Andre Geim（1958-10-21 生于苏联索契，在世）
- **气质关键词**：**石墨烯之父、周五夜实验的玩家、诺奖与搞笑诺奖双冠** —— 2010 诺贝尔物理学奖官方获奖理由：
  > "For groundbreaking experiments regarding the two-dimensional material graphene"（因 regarding 二维材料石墨烯的开创性实验）
- **设计母题**：**原子级蜂窝（honeycomb lattice）**。单原子层的六边形碳网格既是石墨烯本体的视觉图像，也隐喻「最简单材料里藏最深物理」——透明胶带撕出来的诺贝尔奖。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Andre_Geim/page.md`（**page.md 已有本地**）
- **待下载**：`Andre_Geim.html` 与 `images/`（第 0 步执行）；Wikipedia URL：`https://en.wikipedia.org/wiki/Andre_Geim`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（路径见上）；❌ `Andre_Geim.html` 与 `images/` 待下载（Wikipedia URL 见上）
- 提取 infobox 与正文核对，事实基准如下（以 page.md 为准）：
  - 生卒：1958-10-21 生于俄罗斯索契（时属苏联），在世；本名 Andrei Konstantinovich Geim
  - 国籍：生于苏联；1990 年代入荷兰籍；2012 年起英国籍；2025 年因双重英籍自动丧失荷兰籍（荷兰 1990s–2025）
  - 家庭：父 Konstantin Alekseyevich Geim、母 Nina Nikolayevna Bayer 均为德裔工程师；外祖父 Nikolay N. Bayer 是乌克兰早期自然保护先驱、卡缅涅茨-波多利斯基大学创办人/首任校长
  - 教育：两次报考莫斯科工程物理学院落榜（自述因德裔遭歧视），后入莫斯科物理技术学院（MIPT），1982 MSc；1987 于俄罗斯科学院固体物理研究所（ISSP Chernogolovka）获副博士（PhD 等价），金属物理
  - 博士导师：Victor Petrashov；论文《Investigation of mechanisms of transport relaxation in metals by a helicon resonance method》(1987)
  - 博士后：1990 起 Nottingham（两次）、Bath、Copenhagen
  - 任职：IMT RAS 研究员 → 1994 奈梅亨大学副教授（介观超导）→ 2001 曼彻斯特大学教授 → 2002 曼彻斯特介科学与纳米中心主任 → 2007–2013 Langworthy Professor（2012 让位 Novoselov）→ 皇家学会研究教授、国家石墨烯研究所 → 2026-02 获聘香港大学讲席教授（2026-04 就任）
  - 关键荣誉：Ig Nobel 2000（与 Michael Berry 共享）；Mott Medal 2007；FRS 2007；EPS Europhysics Prize 2008（与 Novoselov 共享）；Körber Prize 2009；John J. Carty Award 2010；Hughes Medal 2010；Nobel 2010；荷兰狮骑士指挥官 2010；Knight Bachelor 2012；Copley Medal 2013；Carbon Medal 2016；2018 苏丹亲王水奖；2017 Golden Plate
  - 吉尼斯纪录：史上首位个人同时获得诺贝尔奖与搞笑诺贝尔奖（截至 2025 仍唯一）
  - 知名博士生（infobox 明载）：Soren Neubeck、Konstantin Novoselov、Rashid Jalil、Da Jiang、Rahul Raveendran-Nair、Ibtsam Riaz、Gareth Young
  - 配偶：Irina Grigorieva（妻子兼长期合著者，2001 随迁曼彻斯特任讲师）
- 关键时间线（18 节点）：

| 时间 | 事件 |
|------|------|
| 1958-10-21 | 生于苏联索契，德裔工程师家庭 |
| 1965 | 全家迁往纳尔奇克 |
| 高中毕业后 | 两次报考莫斯科工程物理学院落榜（自述因德裔受歧视），转考 MIPT 录取 |
| 1982 | MIPT 获 MSc（diplom） |
| 1987 | 俄科院固体物理研究所（ISSP）副博士，金属物理，导师 Petrashov |
| 1987–1990 | 俄科院微电子技术研究所（IMT）研究員 |
| 1990 起 | 欧洲博士后：Nottingham（两次）、Bath、Copenhagen |
| 1994 | 奈梅亨大学副教授（介观超导），后入荷兰籍 |
| 1997 | 磁悬浮青蛙实验（与 Berry 报告于 European Journal of Physics） |
| 2000 | 与 Michael Berry 共获搞笑诺贝尔奖 |
| 2001 | 曼彻斯特大学教授；妻子 Grigorieva 随迁任讲师 |
| 2002 | 曼彻斯特介科学与纳米技术中心主任 |
| 2004-10 | 石墨烯论文发表于 Science |
| 2007 | Mott Medal and Prize；当选 FRS |
| 2008 | 与 Novoselov 共享 EPS Europhysics Prize |
| 2010 | Carty Award、Hughes Medal、10-05 获诺贝尔奖、荷兰狮骑士指挥官 |
| 2012 | Knight Bachelor 爵士；Langworthy 讲席让位 Novoselov |
| 2013–2026 | Copley Medal 2013、Carbon Medal 2016、2025 失荷兰籍、2026 港大讲席 |

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Andre_Geim/` 与 `images/` 子目录（提示词文件已就位）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，仅改 `MAIN=Andre_Geim_zh`、`VIDEO_NAME=Andre_Geim_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像为 2018 年照片（File 页 `Nobel_Prize_2010-Press_Conference_KVA-DSC_8019.jpg` 为合影不可裁用单人头）；优先 Wikipedia REST API `page/summary` 查 infobox 原图名后经 Special:FilePath 下载 500px 到 `images/`
- 下载后 `file` 验证格式（JFIF density 异常会导致 xelatex "Dimension too large"，需 sips 改 72dpi）；404 则用装饰圆占位并在提示词补记
- 插图可选：`Frog_diamagnetic_levitation.jpg`（青蛙悬浮实验照， honors/幽默页用）

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | graphene | 石墨烯 | 2004 Science 论文，2010 诺奖核心 | 核心页 |
| 1 | condensed matter physics | 凝聚态物理 | infobox Fields 明载 | 领域页 |
| 2 | mesoscopic physics | 介观物理 | 奈梅亨与曼彻斯特主线之一 | 早年页 |
| 3 | superconductivity | 超导 | 奈梅亨介观超导研究 | 早年页 |
| 4 | nanotechnology | 纳米技术 | gecko tape、介科学纳米中心 | 发明页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致，只收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Victor Petrashov | 师→生（博士导师） | ISSP RAS 博士导师，1987 副博士 |
| advisor-student | Konstantin Novoselov | Geim→学生 | 奈梅亨博士生，后成主要研究伙伴 |
| spouse | Irina Grigorieva | 无向 | 妻子兼长期合著者，2001 任曼彻斯特讲师 |
| co-honored | Konstantin Novoselov | 无向 | 2010 诺贝尔物理学奖共同得主，2008 Europhysics Prize 共同得主 |
| co-honored | Michael Berry | 无向 | 2000 Ig Nobel Prize 共同得主（青蛙抗磁悬浮） |

### 第 5 步：设计配色方案

- **气质**：轻盈、实验玩家气、二维之美
- **主色**：石墨烯青绿 `#146B5A`（批内唯一）+ 诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeGraphene` 石墨烯 — 青绿 `#0E7C7B`
  - `badgeMeso` 介观物理 — 靛蓝 `#4C5FD5`
  - `badgeSC` 超导 — 琥珀 `#E07B30`
  - `badgeNano` 纳米技术 — 玫瑰 `#C4204F`
- **背景母题**：六边形蜂窝网格 + 悬浮气泡（呼应磁悬浮青蛙与二维蜂窝晶格）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）、封面有国籍（底部状态栏 `国籍 | 机构 | 主要奖项` 三要素）。
2. 必须有身份信息页：左头像 + 右信息网格（生卒、本名、国籍变迁、教育、师承、任职、荣誉、核心领域），事实取自 page.md，不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 石墨烯之父 / Andre Geim 1958– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 石墨烯 / 抗磁悬浮 / gecko tape / 介观物理
04  早年：索契到莫斯科 (1958–1987) — 落榜两次、MIPT、ISSP 副博士
05  博士后西行 (1990–1994) — Nottingham/Bath/Copenhagen、决意离开苏联
06  奈梅亨岁月 (1994–2001) — 介观超导、遇见 Novoselov
07  曼彻斯特 (2001– ) — 介科学中心主任、Langworthy 讲席
08  石墨烯：胶带撕出的二维世界（核心贡献页）
09  周五夜实验 — 磁悬浮青蛙、gecko tape、仓鼠合著者
10  诺奖与搞笑诺奖双冠 — 2010 Nobel、2000 Ig Nobel、吉尼斯纪录
11  门生与传承 — Novoselov 接棒 Langworthy 讲席
12  荣誉与认可 — Copley 2013 · Hughes 2010 · FRS 2007 · 爵士
13  遗产：二维材料时代 — 国家石墨烯研究所、低维水
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 表格页负间距：顶部 −0.35cm、arraystretch 0.78–0.82；希腊字母/特殊符号缺字时改数学模式。

| 陷阱 | 说明 |
|------|------|
| 政治敏感 | 正文「观点与言论」节的国际政治评论（中东抵制联署、和平奖评论、脱欧引语风波）一律**禁写** |
| 国籍口径 | 出生苏联 → 荷兰（1990s–2025）→ 英国（2012 起）；2025 自动丧失荷兰籍；获奖时（2010）持荷兰籍，勿写成"英国人获奖" |
| 双冠定位 | 「首位个人同时获诺贝尔奖与搞笑诺贝尔奖」为吉尼斯纪录明载，可写；勿写成"唯一获双奖的人（含团队）" |
| Ig Nobel 归属 | 2000 Ig Nobel 是 Geim 与 Michael Berry **共享**（青蛙实验 1997 报告），勿写成 Geim 独得 |
| 博士导师 | Victor Petrashov（ISSP），勿与 MIPT 本科阶段混淆 |
| 学位口径 | 1987 是苏联 Candidate of Sciences（副博士，PhD 等价），论文题目为螺旋共振法输运弛豫 |
| Novoselov 博士 | Novoselov 的 PhD 是 2004 年在**奈梅亨**获的（导师 Geim），不是曼彻斯特 |
| 落榜原因 | 自述两次落榜莫斯科工程物理学院因德裔受歧视——按其自述口径写，勿写成"成绩不够" |
| 仓鼠合著 | 2001 论文合著者 H.A.M.S. ter Tisha 是其爱仓鼠——可作趣闻但注明为论文署名玩笑 |
| 港大任职 | 2026-02 获聘、2026-04 就任，用「2026 年起」口径 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| graphene | 石墨烯 | 单原子层碳，勿写"石墨" |
| two-dimensional crystal | 二维晶体 | 自由支撑的原子层 |
| diamagnetic levitation | 抗磁悬浮 | 靠水的抗磁性，非超导悬浮 |
| mesoscopic physics | 介观物理 | 介于微观与宏观之间 |
| gecko tape | 壁虎胶带 | 仿生黏附 |
| helicon resonance | 螺旋共振 | 博士论文方法 |
| Candidate of Sciences | 副博士 | 苏联学位体系，PhD 等价 |
| Langworthy Professor | 兰沃西讲席教授 | 曼彻斯特捐赠讲席，2012 传于 Novoselov |
| Ig Nobel Prize | 搞笑诺贝尔奖 | 先幽默后真实的典范 |
| National Graphene Institute | 国家石墨烯研究所 | 曼彻斯特，2015 启用 |
| low-dimensional water | 低维水 | 2012 起新方向，2018 水奖来源 |
| Guinness World Records | 吉尼斯世界纪录 | 双奖第一人口径来源 |

---

## 四、背景音乐选择 【人物专属建议】

- **选定曲目**：**New Lands** — Alex-Productions（152k views，高受众 / 史诗 / 开阔）
- **匹配理由**："新大陆"匹配 Geim 五换研究方向、"敢于尝试，至少是一场冒险"的人生底色；从索契到西欧再到曼彻斯特，正是不断开辟新天地的远征叙事；石墨烯本身就是材料科学的"新大陆"。
- **本地路径**：`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`
- **备选**：Awaken（明亮/鼓舞，匹配周五夜实验的玩家气）、SEA（流动/平稳，匹配多次跨界）

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Andre_Geim/page.md` | 事实基准（唯一数据源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Andre_Geim.yaml` | 社会关系/领域入库（本批新建） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
