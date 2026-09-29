# 物理学家立传提示词（Peter W. Higgs · 2013 诺贝尔物理学奖）

> **本文件是 OpenPhysicist 21 世纪批次的人物专属立传提示词**，以 Peter W. Higgs（2013 诺贝尔物理学奖，希格斯玻色子理论预言）为目标人物。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Peter Ware Higgs（彼得·沃恩·希格斯），2013 诺贝尔物理学奖（与 François Englert 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇另需突出**谦逊理论家的孤独预言**——1964 两篇短文、被拒稿、半个世纪的等待与 2012 LHC 的证实，一条"没有 eureka 时刻"的静水深流。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Peter Ware Higgs（1929-05-29 生于泰恩河畔纽卡斯尔 ~ 2024-04-08 逝于爱丁堡，享年 94 岁）
- **气质关键词**：**孤独的预言家、被拒稿的短文作者、厌恶"上帝粒子"绰号的谦逊学者** —— 2013 诺贝尔物理学奖获奖理由：
  > "for the theoretical discovery of a mechanism that contributes to our understanding of the origin of mass of subatomic particles, and which recently was confirmed through the discovery of the predicted fundamental particle, by the ATLAS and CMS experiments at CERN's Large Hadron Collider"（因其对亚原子粒子质量起源机制的理论发现，该机制最近由 CERN 大型强子对撞机 ATLAS 与 CMS 实验发现所预言的基本粒子而获得证实）
- **设计母题**：**弥漫空间的场（the field that fills the void）**。看不见的场赋予万物质量——48 年从预言到证实的等待，是比粒子对撞画面更贴合 Higgs 的视觉语言。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Peter_W._Higgs/page.md`（✅ 已有本地）
- **html/images**：待下载 —— Wikipedia URL：`https://en.wikipedia.org/wiki/Peter_W._Higgs`（第 0 步下载 `Peter_W._Higgs.html` 与 infobox 肖像到 `images/`）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（事实基准如下）；html 与 images/ 待下载（URL 见上）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1929-05-29 生于纽卡斯尔埃尔斯维克（Elswick）~ 2024-04-08 逝于爱丁堡家中（短暂患病后），享年 94 岁
  - 国籍：英国
  - 家庭：父 Thomas Ware Higgs（1898–1962，BBC 录音工程师）、母 Gertrude Maude née Coghill（1895–1969）；童年哮喘+父亲工作调动+二战而缺课居家自学；父迁 Bedford 后随母留布里斯托尔；1963 与美国语言学讲师 Jody Williamson 结婚（CND 战友），1972 分居（保持朋友至其 2008 去世），两子 Christopher 与 Jonny（爵士音乐家）
  - 教育：Cotham Grammar School（布里斯托尔 1941–1946，受校友 Paul Dirac 事迹启发）→ City of London School（1946–，主修数学）→ King's College London（1947–；1950 物理一等荣誉学士、1952 硕士、1954 博士）
  - 博士导师：Charles Coulson 与 Christopher Longuet-Higgins 双导师（1851 Research Fellowship 资助，分子物理方向）；博士论文《Some problems in the theory of molecular vibrations》(1954)
  - 博士生（infobox 明载）：Lewis Ryder、David Wallace、Christopher Bishop
  - 任职机构：爱丁堡大学高级研究员 1954–1956 → Imperial College London / University College London 多职（UCL 兼数学临时讲师）→ 1960 回爱丁堡任 Tait 数理物理研究所讲师 → Reader → 1980 理论物理 personal chair → 1996 退休任荣休教授
  - 关键荣誉：FRSE 1974；FRS 1983；FInstP 1991；Hughes Medal 1981；Rutherford Medal and Prize 1984；IOP Dirac Medal 1997；EPS High Energy and Particle Physics Prize 1997；Royal Medal（RSE）2000；Wolf Prize 2004（与 Brout、Englert）；Oskar Klein Medal 2009；Sakurai Prize 2010；Edinburgh Award 2011（2012-02-24 手印仪式）；Higgs Medal（RSE）2012；Nobel 2013（与 Englert）；Princess of Asturias Award 2013；Copley Medal 2015；Companion of Honour 2012（2014-07-01 Holyroodhouse 受勋）；1999 拒绝爵士；17 个荣誉博士（Bristol 1997 至 Trinity College Dublin 2016）；爱丁堡大学希格斯理论物理中心（2012-07-06 宣布，Higgs 讲席现由 Neil Turok 持有）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点，见幻灯片序列）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Higgs 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | spontaneous symmetry breaking | 自发对称性破缺 | 1964 两篇论文：规避 Goldstone 定理漏洞 | 核心贡献页 |
| 1 | particle physics | 粒子物理 | 希格斯玻色子预言、标准模型要素 | 玻色子页 |
| 2 | quantum field theory | 量子场论 | 规范玻色子质量机制 | 机制页 |
| 3 | molecular physics | 分子物理 | 博士论文：分子振动理论 | 博士页 |
| 4 | general relativity | 广义相对论 | 早期工作：1958 量子化引力约束、1959 二次拉格朗日量 | 早期研究页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Charles Coulson | advisor（对方是导师） | KCL 博士导师之一（分子物理，1851 研究奖学金资助） |
| advisor-student | Christopher Longuet-Higgins | advisor（对方是导师） | KCL 博士导师之一（分子物理） |
| advisor-student | Lewis Ryder | student（对方是学生） | infobox 明载博士生 |
| advisor-student | David Wallace | student（对方是学生） | infobox 明载博士生 |
| advisor-student | Christopher Bishop | student（对方是学生） | infobox 明载博士生 |
| spouse | Jody Williamson | 无向 | 1963 结婚，1972 分居（爱丁堡美国语言学讲师，CND 战友） |
| influence | Yoichiro Nambu | 单向（对方是思想源头） | Higgs 工作的思想基础：基于超导的自发对称性破缺理论 |
| influence | Philip Warren Anderson | 单向（对方是思想先驱） | 1962 年先提出该机制（但缺关键相对论模型） |
| colleague | Robert Brout | 无向 | 1964 三篇里程碑论文同行，Higgs 发表版引用其与 Englert |
| co-honored | François Englert | 无向 | 2013 诺贝尔物理学奖共享；1997 EPS、2004 Wolf、2010 Sakurai、2013 Asturias 亦共同 |
| co-honored | Robert Brout | 无向 | 1997 EPS、2004 Wolf、2010 Sakurai 共同得主 |
| co-honored | Gerald Guralnik | 无向 | 2010 J. J. Sakurai Prize 共同得主（GHK 第三篇 1964 论文作者） |
| co-honored | C. R. Hagen | 无向 | 2010 J. J. Sakurai Prize 共同得主（GHK 第三篇 1964 论文作者） |
| co-honored | Tom Kibble | 无向 | 2010 J. J. Sakurai Prize 共同得主（GHK 第三篇 1964 论文作者） |

#### 4.5.1 入库操作

- 以 `name_en='Peter W. Higgs'`（qid Q192112，库内无记录，seed 新建）为中心写入 `person_relation`
- 对手方规范名（先查库）：`Christopher Longuet-Higgins`（id=1791）、`Yoichiro Nambu`（id=2974）、`Philip Warren Anderson`（id=2628，Q190770 规范记录——**勿用 id=2607 'Philip W. Anderson' 裸 stub**）；`Charles Coulson`（非 'Alan Coulson' id=1125，注意同名库外）、`Jody Williamson`、`Lewis Ryder`、`David Wallace`、`Christopher Bishop`、`Robert Brout`、`Gerald Guralnik`、`C. R. Hagen`、`Tom Kibble` 库内无记录建 stub（勿编 qid）
- 方向约定：师生有向（advisor/student）；influence 单向（对方是思想源头）；其余无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：静水深流、苏格兰的灰蓝、半个世纪的等待
- **配色**：深海军蓝（苏格兰的深沉）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeField` 希格斯场 — 靛蓝 `#4C5FD5`
  - `badgeBoson` 希格斯玻色子 — 深红 `#A63A2B`
  - `badgeSsb` 自发对称性破缺 — 青绿 `#0E7C7B`
  - `badgeMol` 分子物理/早期工作 — 琥珀 `#E07B30`
- **主色**：`#16324F`（深海军蓝，批内唯一）
- **背景母题**：柔和气泡——弥漫的场以稀疏光点表现，中心一点渐亮呼应"粒子从场中获得质量"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）：左头像 + 右信息网格（生卒、出生地、国籍、教育、双导师、任职、主要荣誉、核心领域）。
4. 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 希格斯玻色子的预言者 / Peter W. Higgs 1929–2024 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地 Newcastle、KCL、双导师 Coulson/Longuet-Higgins、爱丁堡大学、Nobel 2013、核心领域）
03  核心贡献概览 — 自发对称性破缺 / 希格斯场 / 玻色子预言 / 早期引力与分子物理
04  早年：纽卡斯尔到布里斯托尔 (1929–1947) — 哮喘居家自学、Cotham、Dirac 校友启发、City of London School
05  KCL 学子 (1947–1954) — 一等荣誉、1851 奖学金、分子振动博士论文
06  爱丁堡的回归 (1954–1960) — 研究员、Imperial/UCL、1960 Tait 研究所讲师
07  思想源头：Nambu 与 Anderson (1962–1964) — 超导启发的对称性破缺、1962 Anderson 先声
08  1964：两篇论文与一次拒稿（核心贡献页）— Physics Letters 短文、PRL 被拒补一段、预言新玻色子
09  1966 与后续：从机制到标准模型 — PR 长文、W/Z 玻色子质量
10  2012-07-04：CERN 的宣告 — 126 GeV、"It's really an incredible thing that it's happened in my lifetime."
11  荣誉与认可 — Nobel 2013 · Wolf 2004 · Copley 2015 · CH 2012 · 17 个荣誉博士
12  公共生活与个性 — 拒绝爵士、接受 CH、"上帝粒子"绰号的厌恶、CND/Greenpeace 经历
13  遗产：希格斯中心与奖章遗赠
14  结尾
```

- 公式框：page.md 无公式，用**概念图式**——「场渗漏：粒子穿过希格斯场获得质量示意」，并注明"示意图，非 page.md 公式"。

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

- 版式：每页写完 `make clean && make`，pdftoppm 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

**Higgs 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖归属 | 2013 诺奖**只颁给 Higgs 与 Englert 两人**；Guralnik/Hagen/Kibble 未获诺奖，勿写"六人共享诺奖" |
| 机制命名 | 1964 三篇论文各自独立（PRL 50 周年齐认里程碑）；机制全名 Englert–Brout–Higgs–Guralnik–Hagen–Kibble；Anderson 1962 已提出（缺相对论模型）；勿写 Higgs 独创 |
| 无 eureka | Higgs 明言理论发展"no eureka moment"，且灵感场景是**失败的周末高地露营返回后**（非露营中），勿戏剧化 |
| 拒稿梗 | Physics Letters 编辑评价 "of no obvious relevance to physics"；补充一段后投 PRL 获发——两个细节都属 page.md 明载，勿混用次序 |
| 博士导师是双导师 | Coulson + Longuet-Higgins 并列（分子物理），勿只写一人；**Charles Coulson ≠ 库内 Alan Coulson（id=1125，生物学家）** |
| Anderson 规范名 | 用 `Philip Warren Anderson`（id=2628, Q190770），勿用库内裸 stub 'Philip W. Anderson'（id=2607） |
| "上帝粒子" | 绰号归 Lederman 书名（出版社建议，原拟 "goddamn particle"）；Higgs 明言厌恶该绰号；"God particle 预言在 Torah/Qur'an/佛经"是他抱怨收到的信件内容，勿写成事实 |
| 引语 | 2012 seminar "It's really an incredible thing that it's happened in my lifetime."、2013 Guardian 长引语、"honorary Swiss" 玩笑均有原文，可引；其余禁编 |
| 荣典细节 | 1999 **拒绝**爵士、2012 接受 Companion of Honour（自称被"错误保证"后接受）、2014-07-01 受勋；Wolf 2004 未赴耶路撒冷领奖（抗议以色列对待巴勒斯坦人）——只写 page.md 明载事实，不展开评论 |
| 政治社团 | CND（因扩纲反核能而退会）、Greenpeace（因反转基因而退出）、AUT 工会活动——明载可写，勿扩展引申 |
| 去世 | 2024-04-08 爱丁堡家中，短病后；2025-11 报道诺贝尔奖章遗赠爱丁堡大学 |
| 家庭 | 1972 与 Jody Williamson **分居**（非离婚措辞），保持朋友至其 2008 去世；两子两孙，勿写"婚姻美满" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Higgs boson | 希格斯玻色子 | 预言的新粒子，spin-zero |
| Higgs field | 希格斯场 | 弥漫空间、赋予粒子质量 |
| Higgs mechanism | 希格斯机制 | 全名 Englert–Brout–Higgs–GHK，勿让 Higgs 独占 |
| spontaneous symmetry breaking | 自发对称性破缺 | 源自 Nambu 超导类比 |
| Goldstone's theorem | 戈德斯通定理 | Higgs 利用其漏洞（局域对称性破缺下无质量玻色子可不出现） |
| W and Z bosons | W 与 Z 玻色子 | 获得质量的规范玻色子 |
| Standard Model | 标准模型 | 机制是其重要成分 |
| electroweak theory | 电弱理论 | 1964 论文语境 |
| molecular vibrations | 分子振动 | 博士论文主题 |
| God particle | "上帝粒子" | 绰号带引号使用，并注 Lederman 出处 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（较高受众 / 宏大 / 深远）
- **匹配理由**:
  - "宏大/深远" 匹配 48 年从预言到证实的理论寿命——机制被写进标准模型，影响超越个人
  - 沉稳的推进感匹配 Higgs "静水深流"的谦逊气质（与批内其他曲目不重复）
- **备选**（未采用）: The Invisible Light（已用于 Haroche）、Cinematic Experience（张力过高，不符其低调）
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Peter_W._Higgs/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
