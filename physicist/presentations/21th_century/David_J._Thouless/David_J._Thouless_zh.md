# 物理学家立传提示词（David J. Thouless 大卫·索利斯）

> **OpenPhysicist 21 世纪批次 · 人物专属立传提示词**。
> 目标人物：David James Thouless（1934-09-21 ~ 2019-04-06，享年 84 岁），2016 诺贝尔物理学奖得主（拓扑相变与拓扑物态）。
> 执行方式：复制本文件到新对话中，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：David James Thouless（大卫·詹姆斯·索利斯），英国凝聚态理论物理学家，BKT 相变、TKNN 拓扑量子化与拓扑量子数的奠基人。
- **设计哲学**：物理学家立传必须有「身份信息页」，且强调「研究领域」的结构化表达。Thouless 篇的叙事核心是「把拓扑学带进凝聚态的人」——从核物质微扰论出发，跨越二维体系的涡旋配对、无序电子局域化与量子化霍尔电导，让「不变量/缠绕数」成为物态分类的语言。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：David James Thouless（1934-09-21 生于苏格兰 Bearsden ~ 2019-04-06 逝于剑桥，享年 84 岁）
- **气质关键词**：**拓扑物态的引路人、BKT 相变的命名者、量子化输运的奠基者** —— 2016 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for theoretical discoveries of topological phase transitions and topological phases of matter"（拓扑相变与物态拓扑相的理论发现）
- **设计母题**：**缠绕数（winding number）**。BKT 相变的核心是涡旋的拓扑配对，TKNN 的核心是布里渊区的第一 Chern 数——视觉语言可用深琥珀底色上一枚环绕圆环的箭头，缠绕次数即拓扑不变量。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/David_J._Thouless/page.md`
- **第 0 步状态**：page.md 已有本地；`David_J._Thouless.html` 与 `images/` 待下载，Wikipedia URL：`https://en.wikipedia.org/wiki/David_J._Thouless`
- **参考模板**：
  - 物理学家成品骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对 page.md，建 Beamer 前须再对照原文）

- 生卒：1934-09-21 生于苏格兰 Bearsden ~ 2019-04-06 逝于英格兰剑桥，享年 84 岁；2016 年起患失智症（page.md 明载）
- 国籍：英国（infobox Citizenship 仅 UK；frontmatter nationality 含 US，口径以 UK 为主）
- 父母：父 Robert Thouless（心理学家、广播人）；母 Priscilla（Gorton）Thouless（英语教师）；英格兰裔
- 教育：St Faith's School → Winchester College → 剑桥大学三一学堂（Trinity Hall）自然科学 BA → 康奈尔大学博士（论文《The application of perturbation methods to the theory of nuclear matter》，1958）
- 博士导师：Hans Bethe（康奈尔）
- 任职：劳伦斯伯克利实验室博士后 + 伯克利物理系（1958–1959，授原子物理课）；剑桥 Churchill College 首任物理学业导师 1961–1965；伯明翰大学数学物理教授 1965–1978；耶鲁大学应用科学教授 1979–1980；华盛顿大学（西雅图）物理教授 1980 起
- 关键荣誉：Maxwell Medal and Prize 1973；FRS 1979；Holweck Prize 1980；Fritz London Memorial Prize 1984；Wolf Prize 1990；美国 NAS 院士 1995；IOP Dirac Medal 1993；Lars Onsager Prize 2000；Nobel 2016（与 Haldane、Kosterlitz 共享）；APS Fellow 1986；美国艺术与科学院 Fellow
- 核心贡献清单：
  1. Berezinskii–Kosterlitz–Thouless（BKT）相变——二维体系中涡旋配对的拓扑相变（1973 与 Kosterlitz 合著论文《Ordering, metastability and phase transitions in two-dimensional systems》）
  2. KTHNY 理论（二维熔化的拓扑序理论）
  3. TKNN 方程——1982 与 Kohmoto、Nightingale、den Nijs 合著《Quantized Hall Conductance in a Two-Dimensional Periodic Potential》，量子化霍尔电导的拓扑解释
  4. Thouless energy（Thouless 能）、拓扑量子数系统化（1998 专著《Topological Quantum Numbers in Nonrelativistic Physics》）
  5. 多体理论：核物质微扰方法、'rearrangement energy' 概念澄清、形变核转动惯量表达式
  6. 无序晶格中电子局域态的研究
- 关键时间线（15–20 节点）：1934 出生 Bearsden → St Faith's → Winchester College → 剑桥三一学堂 BA → 康奈尔 Bethe 门下博士（1958）→ 伯克利博士后 1958–59 → 1961 Churchill College 首任物理学业导师 → 1965 伯明翰数学物理教授 → 1973 Maxwell 奖 + BKT 论文 → 1978 卸任伯明翰 → 1979 FRS + 耶鲁 → 1980 华盛顿大学教授 → 1982 TKNN 论文 → 1984 Fritz London 奖 → 1990 Wolf Prize → 1993 Dirac Medal → 1995 NAS 院士 → 1998 拓扑量子数专著 → 2000 Onsager Prize → 2016 诺贝尔奖（同年患失智症报道）→ 2019 剑桥去世、奖章捐给三一学堂
- 家庭：1958 与 Margaret Elizabeth Scrase 结婚，育有三名子女；去世后家人把诺奖奖章捐赠剑桥三一学堂

### 第 4 步：研究领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | infobox Fields 明载，毕生主战场 | 身份页 |
| 1 | topological phase transitions | 拓扑相变 | BKT 相变，2016 诺奖核心 | 核心页 |
| 2 | many-body problem | 多体问题 | 核物质微扰、rearrangement energy | 早期页 |
| 3 | quantum Hall effect | 量子霍尔效应 | TKNN 拓扑解释 | TKNN 页 |
| 4 | nuclear matter | 核物质 | 博士论文与早期方向（frontmatter field_of_work） | 早年页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Albrecht Bethe | 导师 | 康奈尔大学博士导师，1967 诺贝尔物理学奖得主 |
| advisor-student | J. Michael Kosterlitz | 学生 | infobox Notable students 明载（博士后），BKT 合作论文 1973 |
| co-honored | J. Michael Kosterlitz | 无向 | 2016 诺贝尔物理学奖共同得主，BKT 相变 |
| co-honored | Duncan Haldane | 无向 | 2016 诺贝尔物理学奖共同得主，拓扑物态（库内规范名 Duncan Haldane） |
| spouse | Margaret Elizabeth Scrase | 无向 | 1958 年结婚的妻子 |

> 注：TKNN 论文共同署名 Kohmoto/Nightingale/den Nijs 为单篇合作，未建关系（防噪声）；Berezinskii 为 BKT 名称中的先导者，page.md 未载二人互动，禁写。

### 第 5 步：配色方案 【人物专属】

- **气质**：厚重、琥珀色、拓扑环的简洁几何
- **配色**：拓扑琥珀（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 主色 — 拓扑琥珀 `#8C5A10`（批内不重复）
  - `badgeBKT` BKT 相变 — 靛蓝 `#2B4C9B`
  - `badgeTKNN` TKNN/量子霍尔 — 青蓝 `#1E88C7`
  - `badgeTQN` 拓扑量子数 — 青绿 `#0E7C7B`
  - `badgeNuc` 核物质 — 玫瑰 `#C4204F`
- **背景母题**：深琥珀底色上一枚圆环与绕环一周的箭头（缠绕数 = 1），旁缀淡色第二圈（缠绕数 = 2）

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 拓扑物态的引路人 / David J. Thouless 1934–2019 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — BKT 相变 / TKNN / 拓扑量子数 / 多体理论
04  苏格兰少年与剑桥 (1934–1955) — Winchester、三一学堂、自然科学 BA
05  康奈尔：Bethe 门下 (1955–1958) — 核物质微扰论博士论文
06  伯克利与 Churchill College (1958–1965) — 博士后、首任物理学业导师
07  伯明翰岁月 (1965–1978) — 数学物理教授、BKT 论文 1973
08  突破：BKT 相变 (1973)（核心贡献页）— 二维体系的涡旋配对、拓扑相变（公式框：BKT 相变温度概念式或涡旋配对概念图式，page.md 无具体公式须注明）
09  从耶鲁到西雅图 (1979–1980– ) — 应用科学教授、华盛顿大学
10  TKNN 与量子化霍尔电导 (1982) — 第一 Chern 数、拓扑输运
11  荣誉与认可 — Nobel 2016 · Wolf 1990 · Onsager 2000 · Dirac Medal 1993
12  拓扑量子数的系统化 — 1998 专著、Thouless energy
13  遗产：拓扑物态的黄金时代 — 三人共享的 2016、奖章归三一学堂
14  结尾
```

### 第 7–8 步：版式要点 + Thouless 专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for theoretical discoveries of topological phase transitions and topological phases of matter"；三人共享，勿写成独立获奖 |
| BKT 命名 | Berezinskii–Kosterlitz–Thouless：Berezinskii 有先导工作但 page.md 未载其人互动，立传只写 Kosterlitz–Thouless 1973 论文与 BKT 全称，勿展开 Berezinskii 生平 |
| Kosterlitz 双重身份 | 对 Thouless 而言 Kosterlitz 是 infobox 明载的 Notable students（postdoc）+ 2016 共同获奖者——两条关系（advisor-student / co-honored）并存，勿只建一条 |
| Bethe 规范名 | 入库用库内形式 Hans Albrecht Bethe（勿用裸 Hans Bethe 造新 stub） |
| 国籍口径 | infobox Citizenship 仅 UK；frontmatter nationality 有 UK+US——yaml 主写 United Kingdom，提示词身份页口径「英国」 |
| 与 K. Wilson 区分 | 同为康奈尔 Bethe 之后的拓扑/临界名家，但两人无直接关系，勿混写；Kenneth G. Wilson 的诺奖是 1982 |
| 晚年 | 2016 年起患失智症（page.md 明载可写）；2019-04-06 逝于剑桥，奖章由家人捐给三一学堂 |
| 无载禁写 | 博士后具体年份细节、Haldane 与 Thouless 的个人互动、子女姓名 page.md 均无载，禁写 |
| 同名区分 | Thouless 能（Thouless energy）非 Thouless 泵浦（page.md 未载后者，禁写） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| topological phase transition | 拓扑相变 | BKT 为原型 |
| vortex–antivortex pair | 涡旋–反涡旋对 | BKT 低温配对 |
| Thouless energy | Thouless 能 | 无序体系能标 |
| Chern number | 陈数 | TKNN 的拓扑不变量 |
| quantized Hall conductance | 量子化霍尔电导 | TKNN 1982 |
| topological quantum number | 拓扑量子数 | 1998 专著主题 |
| many-body problem | 多体问题 | 核物质微扰起点 |
| rearrangement energy | 重排能 | 形变核概念 |
| KTHNY theory | KTHNY 理论 | 二维熔化拓扑序 |
| localized states | 局域态 | 无序晶格电子 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（49k views，宏大/深远/长期影响）
- **匹配理由**：
  - 「宏大/深远/长期影响」匹配拓扑物态纲领——从 1973 BKT 到 2016 诺奖再到拓扑材料的时代
  - 「基础理论」匹配拓扑量子数的系统化工作
- **备选**（未采用）：Expedition（留给同批 McDonald）、The Invisible Light（留给同批 Kajita）
- **本地路径**：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`
- **时长**：约 3 分 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐
