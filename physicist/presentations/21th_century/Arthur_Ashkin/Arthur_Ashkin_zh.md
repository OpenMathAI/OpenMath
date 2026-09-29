# 物理学家立传提示词（Arthur Ashkin）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」。
> 目标人物：Arthur Ashkin（2018 诺贝尔物理学奖，光镊发明者，时年 96 岁的最年长诺奖得主）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Arthur Ashkin（亚瑟·阿斯金），2018 年诺贝尔物理学奖（一半奖金），「光镊之父」。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达；Ashkin 篇另需突出「以光驯服物质」的实验物理叙事。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Arthur Ashkin（1922-09-02 ~ 2020-09-21，享年 98 岁）
- **气质关键词**：**光镊之父、贝尔实验室四十年老将、最年长的诺奖得主**
- **官方获奖理由（2018，一半奖金）**：
  > "for the optical tweezers and their application to biological systems"（因光镊及其在生物系统中的应用）
  - 另一半由 Gérard Mourou 与 Donna Strickland 共享（啁啾脉冲放大），本篇提及但重心在 Ashkin。
- **设计母题**：**光的力（the force of light）**。辐射压把「科幻旧梦」变成抓取原子、病毒与活细胞的「激光手指」——视觉上以光束、微粒、阱势为核心意象。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Arthur_Ashkin/page.md`（**已有本地**）
- **待下载**：`{Dir}.html` 与 `images/` 肖像待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Arthur_Ashkin`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1922-09-02 生于纽约布鲁克林 ~ 2020-09-21 逝于新泽西州拉姆森（Rumson, NJ），享年 98 岁
- **国籍**：美国（乌克兰犹太移民家庭：父 Isadore 原姓 Aschkinase，18 岁自敖德萨移民；母 Anna 来自加利西亚）
- **家庭**：兄 Julius Ashkin（物理学家，曼哈顿计划参与者）、姐 Ruth、另一姐 Gertrude 早夭；妻 Aline（康奈尔相识，结缡 60 余年，Holmdel 高中化学教师），三子五孙；子 Michael Ashkin 为康奈尔大学艺术教授
- **教育**：James Madison High School 1940 届 → 哥伦比亚大学物理学士 1947（期间任 MIT 辐射实验室技术员，造军用雷达磁控管；1945-07-31 入美国陆军预备役）→ 康奈尔大学核物理 MS、PhD 1952
- **博士导师**：William M. Woodward（infobox 明载）；博士论文 *A measurement of positron-electron scattering and electron-electron scattering*（1952）
- **关键引路人**：Sidney Millman（哥伦比亚大学时期的导师，其推荐使 Ashkin 进入贝尔实验室）
- **任职机构**：贝尔实验室 1952–1992（四十年；1992 后 Lucent Technologies 名下，退休后在家中实验室继续工作）
- **关键荣誉**：Nobel 2018（一半）；Charles Hard Townes Medal 1988；Frederic Ives Medal 1998；Keithley Award 2003；Harvey Prize 2004；NAE 院士 1984；NAS 院士 1996；National Inventors Hall of Fame 2013；OSA/APS/IEEE Fellow；47 项专利
- **诺奖演讲**：2018-12-08 *Optical Tweezers and their Application to Biological Systems*
- **核心贡献清单**：
  1. 光镊（optical tweezers，1986 年发明）——抓取粒子、原子、病毒与活细胞
  2. 辐射压的梯度力/散射力分解与微粒加速、捕获（1970 PRL *Acceleration and Trapping of Particles by Radiation Pressure*）
  3. 光阱技术奠基原子冷却与捕获（Steven Chu 1997 诺奖工作之基础）
  4. 光折变效应（photorefractive effect）的共同发现者（1960s，压电晶体）
  5. 非线性光学、光纤、参量振荡器与参量放大器研究
- **关键时间线（18 节点）**：1922 生于布鲁克林 → 1940 高中毕业 → 1940s 哥伦比亚 + MIT 辐射实验室 → 1945 入陆军预备役 → 1947 哥大本科 → 1952 康奈尔博士 → 1952 入贝尔实验室（Millman 推荐）→ 1960s 初 转向激光研究 → 1960s 共同发现光折变效应 → 1960s 后期 开始激光操控微粒研究 → 1970 PRL 辐射压加速与捕获粒子 → 1984 NAE 院士 → 1986 发明光镊 → 1988 Townes Medal → 1992 退休（40 年贝尔生涯）→ 1996 NAS 院士 → 2018-10-02 获诺奖（96 岁）→ 2020-09-21 逝于拉姆森

### 第 4 步：研究领域表 【人物专属，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | optical tweezers | 光镊 | 1986 年发明，2018 诺奖核心 | 核心贡献页 |
| 1 | radiation pressure | 辐射压 | 梯度力与散射力的分解 | 光之力页 |
| 2 | laser physics | 激光物理 | 1960s 初由微波转向激光 | 贝尔岁月页 |
| 3 | nonlinear optics | 非线性光学 | 光纤、参量振荡与放大 | 贝尔岁月页 |
| 4 | atomic physics | 原子物理 | 光阱为原子冷却/捕获奠基 | 传承页 |

### 第 4.5 步：社会关系表 【人物专属，与 yaml relations 一致；只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William M. Woodward | 师→生（博士导师） | 康奈尔博士导师，1952 博士论文正负电子散射 |
| advisor-student | Sidney Millman | 师→生 | 哥伦比亚大学时期的导师，推荐其进入贝尔实验室 |
| co-honored | Gérard Mourou | 无向 | 2018 诺贝尔物理学奖共享（Ashkin 得一半，Mourou/Strickland 共享另一半） |
| co-honored | Donna Strickland | 无向 | 2018 诺贝尔物理学奖共享（同上） |
| influence | Steven Chu | 无向 | Ashkin 光阱工作奠定 Chu 原子冷却与捕获研究，Chu 获 1997 诺贝尔奖 |
| spouse | Aline Ashkin | 无向 | 康奈尔相识，结缡 60 余年，Holmdel 高中化学教师 |
| parent-child | Michael Ashkin | 子 | 康奈尔大学艺术教授 |

### 第 5 步：配色方案 【人物专属】

- **气质**：清澈、精准、以柔克刚
- **主色**：深海青蓝 `#0E4D64`（激光的冷静与穿透力）+ 诺奖香槟金 `C9A227`
  - `badgeTweezer` 光镊 — 湖青 `#0E7C7B`
  - `badgeRad` 辐射压 — 琥珀 `#E07B30`
  - `badgeLaser` 激光物理 — 玫瑰 `#C4204F`
  - `badgeBio` 生物应用 — 苔绿 `#3E7C4F`
- **背景母题**：柔和气泡（稀疏大块实心圆），以一束细光线贯穿气泡群，呼应「激光手指抓取微粒」

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；无真实肖像则用装饰圆占位。
2. 封面有国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）。
4. 结尾页品牌标注统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 光镊之父 / Arthur Ashkin 1922–2020 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 光镊 / 辐射压 / 光折变 / 非线性光学
04  布鲁克林少年与战时哥伦比亚 (1922–1947) — MIT 辐射实验室磁控管技术员
05  康奈尔博士：核物理 (1947–1952) — 正负电子散射测量、导师 Woodward
06  贝尔实验室四十年 (1952–1992) — 微波→激光转向、非线性光学、47 项专利
07  光之力：辐射压与微粒捕获（核心贡献页，公式框放辐射压 F = 2(nP/c)Q 或梯度力/散射力分解概念图式）
08  光镊诞生 (1986) — 抓取原子、病毒与活细胞
09  从光阱到原子冷却 — Steven Chu 1997 诺奖工作的基础
10  2018 诺贝尔奖 — 96 岁最年长得主；与 Mourou/Strickland 共享 2018
11  荣誉与认可 — Townes 1988 · Ives 1998 · Harvey 2004 · NAE/NAS 院士
12  遗产：光镊与生物物理
13  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖份额 | Ashkin 独得 **一半**，Mourou 与 Strickland **共享另一半**；勿写成三人平分 |
| 最年长得主口径 | 96 岁获奖是「当时最年长」，2019 被 97 岁获奖的 John B. Goodenough（化学奖）超越，勿写成「史上最年长」的现在时 |
| 获奖理由 | 官方措辞 "for the optical tweezers and their application to biological systems"；强调生物系统应用，勿泛化为「激光捕获技术」 |
| 光镊年份 | 光镊发明于 **1986**；1970 PRL 是辐射压加速与捕获粒子（前驱工作），两个年份勿混 |
| 光折变效应 | 只写「共同发现者（co-discoverer）」，不具名另一位 |
| Bethe/Feynman | page.md 只写经兄长引荐「认识」康奈尔的 Bethe、Feynman 等人——仅一面之缘，**禁写成师承或合作** |
| 兄长 Julius | 是物理学家、曼哈顿计划参与者，但无对应关系类型，**不入库**；正文可提 |
| 家庭 | 妻 Aline、子 Michael Ashkin（康奈尔艺术教授）page.md 明载可写；但 Michael 是艺术家，勿误写成科学家 |
| Millman 身份 | Sidney Millman 是**哥伦比亚大学时期的导师**（非康奈尔博士导师），其贡献是推荐进入贝尔实验室 |
| 任职名 | 退休前单位写 Bell Laboratories；Lucent Technologies 是 1996 年后贝尔实验室的归属名，任职主线写贝尔 |
| Goodenough | 2019 超越者是**化学奖**得主，勿写成物理学奖 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| optical tweezers | 光镊 | 勿译「光学镊子钳」；单束光阱 |
| radiation pressure | 辐射压 | 与梯度力/散射力分解关联 |
| optical trapping | 光捕获/光阱 | 与光镊同源概念 |
| gradient force / scattering force | 梯度力 / 散射力 | 辐射压的两个分量 |
| photorefractive effect | 光折变效应 | 共同发现者口径 |
| second harmonic generation | 二次谐波产生 | 非线性光学方向 |
| parametric oscillator | 参量振荡器 | 贝尔时期研究方向 |
| chirped-pulse amplification | 啁啾脉冲放大 | Mourou/Strickland 一半奖金的技术（对比提及） |
| laser machining | 激光加工 | CPA 应用，勿与光镊混同 |
| atom laser | 原子激光 | 光阱下游成果 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（纪录片/电影/稳重）
- **匹配理由**：「不可见之光」贴合激光操控微粒的一生主题；纪录片气质匹配贝尔实验室四十年 + 96 岁终获诺奖的长线叙事。
- **备选**（未采用）：Shine Like The Sun（光明/振奋，但更匹配「突破瞬间」而非长线耐心）；SEA（平稳，弱于光学意象）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Arthur_Ashkin/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Arthur_Ashkin.yaml` | 社会关系/领域入库数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
