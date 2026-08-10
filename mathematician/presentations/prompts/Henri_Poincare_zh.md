# 庞加莱 (Henri Poincaré) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Grothendieck、Riemann、Hilbert、Serre 成品为参考模板，为庞加莱制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Henri Poincaré (1854–1912)
- **气质关键词**: **全才、直觉、几何想象、最后一位通才、现代拓扑学之父、动力系统的缔造者**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本获取：
  - `page.md`, `metadata.json`, `images.txt`
  - 页面路径应为 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Henri_Poincaré/`
- **参考模板**:
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` — Grothendieck 完整源码（教皇气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` — Riemann 完整源码（克制天才气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/hilbert/David_Hilbert_zh.tex` — Hilbert 完整源码（王者气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/serre/Jean_Pierre_Serre_zh.tex` — Serre 完整源码（优雅气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Makefile` — 构建脚本（直接复制）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 你的任务

按照 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md) 第十一节「推荐制作流程」的步骤，依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

> **数据库同步要求**：本提示词包含「社会关系梳理 + 入库」步骤（第 4.5 步），完整规范见工作指南 **§二十**。请将 Poincaré 的社会关系（导师 Hermite/Darboux、学生 Borel/Appell、双子星 Hilbert、竞争者 Klein/Einstein 等）写入 `greatminds` 数据库 `person_relation` 表，缺失人物先建占位、关系打 `[材料待展开]` 标识。参考脚本：`MySQL/seed_poincare_relations.py`。

---

## 第 0 步：下载 Wikipedia 页面并校验

### 0.1 下载

运行下载脚本（具体命令参照指南或已有脚本），将页面下载到：
`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Henri_Poincaré/`

确认生成以下文件：
- `page.md` — Markdown 正文
- `metadata.json` — Wikidata 元数据
- `images.txt` — 图片 URL 清单
- `page.html` — HTML 原始备份（可选）

### 0.2 输出以下信息供我校验

- **生卒日期**：1854-04-29 ~ 1912-07-17，享年 58 岁（相对短寿）
- **国籍**：法国
- **出生地**：Nancy（南锡），洛林地区
- **博士导师**：Charles Hermite (埃尔米特) 或 Gaston Darboux (达布) — **此处需要从 metadata 中确认**（Wikipedia 可能记录为 Darboux，因为 Hermite 是名义导师但 Darboux 是实际指导者）
- **博士论文**：1879年，《Sur les propriétés des fonctions définies par les équations aux différences partielles》（偏微分方程定义的函数的性质）
- **主要任职机构**：巴黎大学（Sorbonne）1881–1912，巴黎综合理工学院（École Polytechnique）
- **关键荣誉**：
  - 1887: 当选法国科学院院士（年仅33岁）
  - 1900: 巴黎 ICM 主席（与 Hilbert 23 问题同一个大会）
  - 1905: Bolyai 奖
  - 1906: 当选法兰西学术院（Académie française）院士——极少数获得此项荣誉的数学家
  - 1908: 当选法兰西科学院院长
  - 多次获提名诺贝尔物理学奖（未获奖，但说明其物理学贡献受认可）
- **重要合作者/学生**：Paul Appell, Louis Bachelier (随机过程之父), Émile Borel
- **表弟**：Raymond Poincaré（法国总统，一战时期领导人）
- **Wikipedia 正文中提取出的关键时间线**（按年份列出 15–20 个关键节点）：
  - 1854: 出生于 Nancy
  - 1873: 进入巴黎综合理工学院（以第一名入学）
  - 1875: 进入国立高等矿业学校（对矿业无兴趣，同时自学数学）
  - 1879: 博士毕业
  - 1880: 发现自守函数（automorphic functions），与 Klein 的竞争
  - 1881: 任巴黎大学教授
  - 1885: 国王奥斯卡二世数学竞赛获奖（三体问题相关）
  - 1889: 发现同宿纠缠（homoclinic tangle），混沌理论的先驱
  - 1892–1899: 出版《天体力学新方法》（三卷）
  - 1895: 出版《位置分析》（Analysis Situs），拓扑学的奠基之作
  - 1898: 在物理学论文中提出光速不变假设（先于 Einstein）
  - 1900: 巴黎 ICM 主席
  - 1902: 《科学与假设》出版
  - 1904: 提出 Poincaré 猜想
  - 1905: 发表关于 Lorentz 变换的论文——几乎先于 Einstein 提出狭义相对论
  - 1908: 《科学与方法》出版
  - 1912: 因栓塞去世，年仅 58 岁
- **人格特质线索**：
  - 庞加莱是典型的"直觉型"数学家——先有几何洞察，后有严格证明
  - 他说："用逻辑来证明，用直觉来发明"（On démontre par la logique, on invente par l'intuition）
  - 他的工作习惯：每天在同一时间工作，但每次不超过 2 小时
  - 他的自传体文章《数学创造》(L'invention mathématique, 1908) 是数学创造心理学研究的经典
  - 他在《科学与方法》中描述了自己如何在上马车时突然想到 Fuchsian 函数与双曲几何的联系——所谓"顿悟时刻"的著名案例
  - 他是"哲学家中最好的数学家，数学家中最好的哲学家"
  - 他的科学哲学（约定主义/conventionalism）深刻影响了 20 世纪的科学哲学

### 0.3 与其他已立传数学家的关系网络

- **Hilbert** — 同代双子星，两人被并称为"最后两位数学全才"。Hilbert 1900 年 ICM 提出 23 问题；Poincaré 是同届大会主席。两人互相尊重但风格迥异——Hilbert 公理主义，Poincaré 直觉主义
- **Riemann** — 庞加莱继承了 Riemann 的拓扑思想，将其系统化为 Analysis Situs
- **Klein** — 与庞加莱在自守函数理论上有激烈竞争；Erlangen 纲领也对庞加莱有影响
- **Lorentz** / **Einstein** — 相对论的先驱与对话者。庞加莱在 1905 年前后几乎独立提出狭义相对论的数学框架
- **Darboux** — 博士（实质）导师，微分几何

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `poincare/` 子目录
- 创建 `poincare/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `poincare/Makefile`
- 将 `MAIN` 变量改为 `Henri_Poincare_zh`
- 将 `VIDEO_NAME` 变量改为 `Henri_Poincare_zh`

---

## 第 3 步：收集图片

- 从 `pages/Henri_Poincaré/images.txt` 中选出 4–6 张高质量图片
- 优先选择：
  1. **经典肖像（中年时期，约1890–1905年间）** — 最广为人知的形象
  2. 巴黎大学（索邦）外景
  3. Nancy 故居或纪念碑
  4. 与同时代科学家的合影（如有）
  5. 手稿或 Analysis Situs 的封面
- 下载到 `poincare/images/`，统一命名（如 `portrait.jpg`、`sorbonne.jpg` 等）
- ★ **特殊要求**：庞加莱58岁去世，属于英年早逝。照片选择应体现他精力充沛、目光锐利的盛年形象，避免暮年病态照

---

## 第 4 步：建立时间线和叙事骨架

庞加莱的一生可以按"数学版图拓展"为叙事主线。与 Hilbert 不同，庞加莱的学术生涯更短（58岁），但密度更高——几乎在每个领域都留下了开创性贡献。

### 生平阶段

1. **Nancy 的天才少年 (1854–1875)**：南锡望族出身，父亲是医学教授；5岁患白喉导致语言能力受损，但展现出超常的数学直觉与空间想象能力；进入巴黎综合理工学院（第一名入学）
2. **数学全才的崛起 (1875–1895)**：博士论文（PDE）、自守函数（与 Klein 竞争）、三体问题（国王 Oscar II 奖）、拓扑学奠基（Analysis Situs）、同宿纠缠（混沌理论的先驱）
3. **科学哲学与相对论先驱 (1895–1912)**：科学哲学三部曲《科学与假设》《科学的价值》《科学与方法》；几乎独立提出狭义相对论的数学框架；Poincaré 猜想（1904）；当选法兰西学术院院士（极少数数学家获此殊荣）；58岁英年早逝

### 核心数学贡献（按领域排列）

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 自守函数 | Fuchsian 函数、Kleinian 函数、与双曲几何的深刻联系 | 1880–1884 |
| 天体力学 | 三体问题的定性理论、周期轨道的存在性 | 1885–1899 |
| 动力系统 | 同宿纠缠（homoclinic tangle）— 混沌理论的最早发现 | 1889–1890 |
| 拓扑学 | Analysis Situs (1895) — 代数拓扑的开山之作 | 1895–1904 |
| 代数拓扑 | 同调论、基本群、Poincaré 对偶、Euler–Poincaré 公式 | 1895–1904 |
| Poincaré 猜想 | 1904 年提出，2002–2003 年由 Perelman 证明（七大千禧年难题之一） | 1904 → 2003 |
| 数学物理 | Lorentz–Poincaré 变换、相对论先驱 | 1895–1905 |
| 分析 | PDE、积分方程 | 1879–1890 |
| 数论 | 自守形式与数论的联系（为后来 Langlands 纲领播下种子） | 1880s |
| 科学哲学 | 约定主义（conventionalism）、《科学与假设》《科学与方法》 | 1902–1908 |

### ★ 庞加莱独有的叙事线索

1. **直觉 vs 逻辑** — 庞加莱是"直觉派"的旗手，与 Hilbert"形式主义"形成鲜明对照。他说："用逻辑来证明，用直觉来发明。"
2. **顿悟时刻** — 在《科学与方法》中自述：上马车时突然想到 Fuchsian 函数与双曲几何的联系，这是数学创造心理学的经典案例
3. **相对论的交错** — 庞加莱在 1904–1905 年发表了关于 Lorentz 变换和相对性原理的深刻工作，几乎早于 Einstein 建立狭义相对论。学术界至今争论：谁是狭义相对论的真正创始人？
4. **Poincaré 猜想** — 1904 年随口提出的一个猜想，100 年后成为七大千禧年难题之一，最终由 Perelman 证明（2002–2003）
5. **最后一位通才** — 与 Hilbert 共享"最后一位数学全才"称号。但庞加莱更偏向直觉与几何，Hilbert 更偏向公理与形式
6. **早逝的悲剧** — 58 岁因栓塞去世，仍处于创造力巅峰。如果多活 20 年，20 世纪数学会有什么不同？
7. **家族传奇** — 表弟 Raymond Poincaré 是法国总统。数学家与政治家，同一个家族的两个世界
8. **法兰西学术院** — 极少数数学家（Poincaré, d'Alembert, Laplace）获选进入这所以文学为主的权威机构

### 人物关系

- **Hermite** — 博士名义导师，代数与分析大师
- **Darboux** — 博士实际指导者，微分几何
- **Klein** — 自守函数的竞争者，Erlangen 纲领的思想来源
- **Hilbert** — 同时代的双子星，"最后两位数学全才"
- **Lorentz** — 物理学家，电磁理论，Lorentz 变换
- **Einstein** — 相对论的对话者（实际上两人几乎没有直接交流）
- **Borel, Appell** — 学生与合作者
- **Raymond Poincaré** — 表弟，法国总统

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。参考脚本：`MySQL/seed_poincare_relations.py`。
> 数据库全部字段（职业/领域/奖项/机构/国籍/排行榜）梳理规范见工作指南 **§二十一**；补全时使用 §21.5 内嵌核对表逐项填值并写入库脚本。

1. **入库范围**：上表全部 8 类关系（导师 Hermite/Darboux、学生 Borel/Appell、双子星 Hilbert、竞争者 Klein/Einstein、同事 Lorentz、表弟 Raymond Poincaré）；
2. **缺失人物先建占位**：Hermite、Darboux、Lorentz、Einstein、Appell、Raymond Poincaré（`has_biography=0`）；
3. **关系打标识**：`note` 加 `[材料待展开]` 前缀；
4. **校验**（一人一行）：
   ```sql
   SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
   FROM person_relation pr JOIN people a ON a.id=pr.from_id
   JOIN people b ON b.id=pr.to_id JOIN relation_types rt ON rt.relation_key=pr.relation_type
   WHERE a.name_en='Henri Poincaré' OR b.name_en='Henri Poincaré';
   ```
5. **汇报**：新建 X 人（占位）、新增 Y 条关系 + 校验结果。

---

## 第 5 步：设计配色方案

- 庞加莱的气质关键词：**直觉、几何、优雅、法兰西的知性光辉、星空下的沉思**
- **建议配色：午夜蓝 + 象牙白 + 星空银**（法兰西学院的知性 + 天体力学的神秘 + 拓扑学的严谨）
- 请给出完整的 `\definecolor` 方案：
  - **主色 (coverprimary)**：**午夜蓝** — 深沉如夜空，象征庞加莱深邃的数学直觉和天体力学
  - **强调色 (coveraccent)**：**象牙暖金** — 法兰西学术院的荣耀，与 Serre 共用此色但稍暖
  - 四个分类色，对应庞加莱的四大支柱：
    - **badgetopology** (拓扑/几何) — 普鲁士蓝 → 稍偏紫，呼应 Analysis Situs
    - **badgedynamics** (动力系统/天体力学) — 深铜色 → 三体问题的混乱与秩序
    - **badgephysics** (数学物理/相对论) — 银灰 → 光速不变，Lorentz 变换
    - **badgephilosophy** (科学哲学) — 松绿 → 智慧与沉思
  - 各面板色 (purplepanel/amberpanel/greenpanel/bluepanel/goldpanel/graypanel)

---

## 第 6 步：规划幻灯片序列

庞加莱内容密度极高，且有很多独有叙事线（相对论、混沌、科学哲学、早逝悲剧），建议 20 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 人物篇 ===
01  封面 — 《庞加莱：直觉之王》 / Henri Poincaré 1854–1912 + 四色badge
02  为什么庞加莱是最后一个通才 — 拓扑学之父、动力系统缔造者、相对论先驱、科学哲学家

=== 天才之路 ===
03  Nancy 的天才少年 (1854–1875) — 医学世家、白喉后遗症、超常的空间直觉、第一名考入综合理工学院
04  博士与早年突破 (1875–1885) — PDE 博士论文、自守函数的发现、与 Klein 的著名竞争

=== 拓扑学之父 ===
05  Analysis Situs (1895) — 拓扑学的开山之作，同调论与基本群的起源
06  Poincaré 猜想 (1904) — 随口提出的猜想，100年后成为千禧年难题，Perelman 的证明

=== 动力系统与混沌 ===
07  三体问题 — 国王 Oscar II 奖 (1885–1889)，定性理论的创立
08  同宿纠缠 — 混沌理论的最早发现，不可预测性的数学根源

=== 相对论的前夜 ===
09  光速不变与 Lorentz 变换 — 庞加莱几乎早于 Einstein 建立了狭义相对论的数学框架
10  谁发明了相对论？ — 庞加莱 vs Einstein，优先权争议的历史公案

=== 天体力学 ===
11  《天体力学新方法》 — 三卷巨著 (1892–1899)，一个时代的总结

=== 科学哲学 ===
12  约定主义 — 几何公理不是先验真理，而是约定（convention）
13  "用逻辑来证明，用直觉来发明" — 《科学与假设》《科学与方法》，数学创造的心理学

=== 庞加莱的世界 ===
14  法兰西学术院 — 极少数数学家获此殊荣，家族的荣耀（与表弟 Raymond Poincaré 法国总统）
15  与 Hilbert 的双子星 — 同时代两位数学巨人：多元贡献者的不同风格

=== 终章 ===
16  英年早逝 (1912) — 58 岁因栓塞去世，仍处于创造力巅峰
17  庞加莱的遗产 — 拓扑学、动力系统、混沌理论、相对论……他开辟了半个 20 世纪的数学

=== 结尾 ===
18  思想回响 — 庞加莱说：星辰不是为了被认识而存在，但认识星辰是我们存在的意义
19  结束页 — 主题句：直觉是数学的灵魂。
```

> **可以微调。** 征求我的意见后再开始写代码。特别需要确认：相对论优先权的处理方式（第 10 页比较敏感）。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/poincare/Henri_Poincare_zh.tex`
- 完全参照已有模板的代码结构（grothendieck/riemann/hilbert/serre）
- 每页用 `\newcommand{\xxxslide}{% ... }` 定义

### 关键要求

- **每写完一页立即编译 (`make clean && make`)，不等待全部写完**
- 编译失败立即修复，不要跳过
- 中文正文，英文术语和公式保留原文
- 庞加莱的内容密度极高（58年塞满了别人100年的成就），每页文字量需要严格控制

---

## 第 8 步：布局检查 ★★★ 最重要

### 每写完一页的执行流程

```
1. make clean && make          # 编译
2. 查看 PDF                    # 肉眼检查
3. 如有溢出/重叠 → 立即修复    # 按指南 §6.2 优先级
```

### 溢出修复优先级

| 优先级 | 手段 | 何时用 |
|:--:|------|------|
| 1 | 删 `\plainbar` 或缩减 | 最先尝试，对信息无损 |
| 2 | 缩 `inner sep` (9→5→3pt) | 面板内容刚好超出一点 |
| 3 | 缩字号 | 多行文字导致溢出 |
| 4 | 减行间距 (`\\[2pt]`→`\\[1pt]`) | 压缩面板内部空白 |
| 5 | 调 y 坐标 | **最后手段**，容易打破视觉平衡 |

---

## 第 9 步：史实审查 + 术语审查

### 庞加莱特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 庞加莱特有的高危点 |
|---------|---------------------|
| **"最后一个数学全才"** | ★ page.md 记载 E.T. Bell 称 Poincaré 为 "The Last Universalist"（**仅指 Poincaré 一人**）。不要把 Hilbert 也写成 "最后一位"、"百科全书式数学家"。正确表述："Poincaré 被 E.T. Bell 称为 'The Last Universalist'。" |
| **Hilbert 对比框架** | ★ ★ 整页对比（直觉派 vs 公理派、巴黎 vs 哥廷根）**完全不在 Poincaré 的 page.md 中**。page.md 提到 Hilbert 仅限 Hilbert–Poincaré 级数、两本含 Hilbert 名字的书。不要编造对比叙事。Subtile 保持中性如 "同时代两位数学巨人：多元贡献者的不同风格"。 |
| **Smale / KAM 人物名单** | ★ Slide 8 "影响深远"面板中不要列出 "Smale、Kolmogorov、Arnold、Moser"——**这些人都不在 Poincaré 的 page.md 中**。Birkhoff 出现在 Poincaré–Birkhoff 定理中，可保留。其余人名属于捏造。 |
| **"美学敏感性"** | ★ "美学敏感性"（aesthetic sensibility）不在 page.md 中。page.md 确有 "sudden illumination" 和 "unconscious work" 的直接引语，但未使用 "美学" 一词。改为 "富有成果的组合被筛选出来"。 |
| **博士导师** | 名义导师是 Hermite，但实际论文由 Darboux 指导。两者关系要写清楚。 |
| **自守函数的发现** | Poincaré 和 Klein 独立发现自守函数理论。Poincaré 先发表，但两人实际上从不同方向接近同一目标。不要写成"Poincaré 独自发现"或"Klein 被抢先"，措辞："几乎同时独立发现，两人之间存在激烈的优先权竞争。" |
| **相对论优先权** | ★ 最大敏感话题。庞加莱 1898 年提出光速不变，1905 年发表 Lorentz 变换的完整数学表述。Einstein 同年 1905 年发表狭义相对论。措辞："庞加莱建立了狭义相对论的数学框架，但 Einstein 赋予了它革命性的物理诠释。历史上存在关于优先权的复杂争议。" 不要写"庞加莱发明了相对论"或"Einstein 抄袭了庞加莱"。 |
| **Poincaré 猜想** | 1904 年提出，2002–2003 年由 Perelman 证明。不要写成"2006 年证明"（2006 是 Fields Medal 年份）。正确写法："2002–2003 年，Perelman 在 arXiv 发表三篇论文给出证明，并在 2006 年获得菲尔兹奖（但拒绝领奖）。2010 年，Clay 研究所正式颁发千禧年大奖。" |
| **"Chaos theory" 的命名** | 庞加莱发现了混沌现象（同宿纠缠），但"混沌理论"这个词是 1970s 才出现的。不能说"庞加莱创立了混沌理论"。正确说法："庞加莱发现了同宿纠缠（homoclinic tangle），这一发现被后来视为混沌理论的最早数学源头。" |
| **顿悟故事** | 庞加莱在《科学与方法》中自述的"上马车顿悟"故事是他自己写的，来源可靠但经过了文学加工。引用时应注明出自其自述。 |
| **法兰西学术院** | 法语：Académie française。注意区分"法兰西学术院"（文学/语言）和"法兰西科学院"（科学）。庞加莱是数学家中极少数进入"学术院"的。 |
| **58 岁去世** | 因栓塞（embolism）去世。不要写成"心脏病"或"中风"。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Analysis Situs | 《位置分析》 | 保留拉丁文书名 + 中文翻译。这是拓扑学的奠基之作 |
| automorphic functions | 自守函数 | — |
| Fuchsian functions | Fuchs 函数、Fuchsian 函数 | 两种译法均可，统一用"Fuchsian 函数" |
| homoclinic tangle | 同宿纠缠 | 不要译成"同宿缠结"或"同宿乱麻" |
| Poincaré conjecture | Poincaré 猜想 | — |
| Poincaré duality | Poincaré 对偶 | — |
| fundamental group | 基本群 | — |
| homology | 同调 | — |
| Lorentz transformation | Lorentz 变换 | Poincaré 给 Lorentz 变换起了名字，这是一个有趣的历史注脚 |
| conventionalism | 约定主义 | Poincaré 的科学哲学核心概念 |
| La Science et l'Hypothèse | 《科学与假设》(1902) | — |
| La Valeur de la Science | 《科学的价值》(1905) | — |
| Science et Méthode | 《科学与方法》(1908) | — |
| Les Méthodes nouvelles de la mécanique céleste | 《天体力学新方法》 | 三卷本巨著 |
| École Polytechnique | 巴黎综合理工学院 | — |
| Sorbonne | 巴黎大学（索邦） | — |
| Académie française | 法兰西学术院 | 注意与"法兰西科学院"的区别 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个"断言 | 不说"第一个创立拓扑学"（Leibniz/Euler 已有先驱工作）→ "系统化拓扑学，使之成为独立学科的奠基人" |
| 伪引语 | "用逻辑来证明，用直觉来发明" — 原文："On démontre par la logique, on invente par l'intuition." 有可靠来源 |
| 人物时间线 | Poincaré 与 Einstein 的关系要精确：两人几乎无直接通信，但彼此知道对方工作 |
| 伪精确数字 | "三体问题"不一定严格是"三个天体"；有时也包括限制性三体问题（restricted three-body problem） |

---

## 第 10 步：第二轮布局微调

全部页面写完后：

- 从头到尾翻看 PDF，逐页标记溢出/重叠
- 对标记页按 §8 优先级处理
- 确保每页间距均匀
- 封面肖像在右上角（参照已有模板）
- 结束页不要放肖像（只放主题句 + 生卒年份 1854–1912）

---

## 第 11 步：插入 OpenMath 项目首页

- ★ **使用统一 cover 模板**：从 `../cover/OpenMath_Cover.tex` 复制 `\openmathslide` 命令定义（或直接 `\input`）
- 在 `\begin{document}` 后调用 `\openmathslide`，然后调用庞加莱的封面 `\titleslide`

---

## 第 12 步：最终编译

- 确认 `make clean && make` 无错误
- 确认 PDF 输出正常，总页数在 19–21 页之间
- 从头到尾翻看确认无误
- 准备接受外审

---

## 第 13 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

庞加莱的气质：**直觉、深远、法兰西的知性、星空的浩瀚、早逝的悲剧感** — 深沉优雅略带忧郁。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 沉稳纪录片风，58岁戛然而止的永恒 |
| ★★★ | Eternals | alex-productions | `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` | 宏大深远，Poincaré 猜想的百年等待 |
| ★★ | Tragedy | alex-productions | `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` | 深色戏剧性，早逝的悲剧感 |
| ★ | Cinematic Experience | alex-productions | `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` | 电影感高张力，百科全书式全才 |

**操作**：复制选定的 `.wav` 到 `Henri_Poincare/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 完整操作手册 |
| `mathematician/pages/Henri_Poincaré/page.md` | Poincaré Wikipedia 正文（需下载） |
| `mathematician/pages/Henri_Poincaré/metadata.json` | Poincaré Wikidata 元数据（需下载） |
| `mathematician/pages/Henri_Poincaré/images.txt` | 图片 URL 清单（需下载） |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码（教皇模板） |
| `mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` | Riemann 完整源码（克制天才模板） |
| `mathematician/presentations/hilbert/David_Hilbert_zh.tex` | Hilbert 完整源码（王者模板） |
| `mathematician/presentations/serre/Jean_Pierre_Serre_zh.tex` | Serre 完整源码（优雅模板） |
| `mathematician/presentations/grothendieck/Makefile` | 构建脚本（直接复制） |

---

> **开始执行。每完成一步向我汇报。**
>
> **最重要的事：每写一页就 make，看到溢出就修，不要攒到最后一起修。**
>
> **特别提醒：**
> 1. 庞加莱是 58 岁英年早逝（不是寿终正寝），叙事需要有"戛然而止"的悲剧感
> 2. 相对论优先权是最敏感的话题——保持中立、不偏袒任何一方
> 3. Poincaré 猜想（1904→2003）是贯穿百年的完美叙事弧——善加利用
> 4. ★ 与 Hilbert 的对比页（Slide 15）：**不要编造对比叙事**。Page.md 仅提到 Hilbert 四次（Hilbert–Poincaré 级数、两本书名、人物导航列表）。不要使用 "直觉派 vs 公理派"、"巴黎 vs 哥廷根"、"最后两位全才" 等不在 page.md 中的框架
> 5. 庞加莱是"哲学家中最好的数学家"——科学哲学三本书是不可或缺的一页
> 6. ★ Slide 8 "混沌理论" 面板：不要列出 Smale、Arnold、Moser 等后人名（不在 page.md 中），Birkhoff 可保留
> 7. ★ Slide 13 直觉与创造："美学敏感性"不在 page.md 中，改为更中性的表述
> 8. ★ Slide 15 底部：不要写"最后两位百科全书式数学家"（不在 page.md 中），改用 "各自时代的最后一位数学全才"