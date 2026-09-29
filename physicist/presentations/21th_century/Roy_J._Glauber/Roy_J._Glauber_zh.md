# 物理学家立传提示词（21 世纪批次：Roy J. Glauber）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传的人物专属提示词**，以 Roy J. Glauber（2005 诺贝尔物理学奖，光的量子相干性理论）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Roy Jay Glauber（罗伊·格劳伯），2005 年诺贝尔物理学奖**一半**得主（另一半由 Hall 与 Hänsch 共享），量子光学奠基人。
- **设计哲学**：保留「身份信息页」+ 研究领域结构化骨架；Glauber 篇的设计母题围绕「给光以量子秩序」——从激光的相干态到黑体辐射的统计，视觉语言可用「波列与光子计数」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Roy Jay Glauber（1925-09-01 生于纽约市 ~ 2018-12-26 逝于马萨诸塞州牛顿，享年 93 岁）
- **气质关键词**：**量子光学之父、Los Alamos 最年轻的少年、Ig Nobel 扫帚守护者**
- **诺奖理由（官方原文，禁止改写）**：
  > "for his contribution to the quantum theory of optical coherence"（因他对光学相干性的量子理论的贡献）
- **设计母题**：**相干与计数**——1963 年光子探测模型区分激光与灯泡的光；可用「整齐波列 vs 杂乱光子雨」做视觉对比。
- **本地数据源**：
  - ✅ `physicist/presentations/21th_century/21st_century/Roy_J._Glauber/page.md`（已有本地）
  - ⬜ `{Dir}.html` 与 `images/` **待下载**：Wikipedia URL `https://en.wikipedia.org/wiki/Roy_J._Glauber`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`；骨架复用 20 世纪成品（如 `Kenneth_G_Wilson_zh.tex`）。
- **入库命名注意**：库内已有记录 `Roy Glauber`（id=2566），yaml `name_en` 沿用 **`Roy Glauber`**（勿写 Roy J. Glauber，防分裂 stub）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1925-09-01 生于纽约市 ~ 2018-12-26 逝于马萨诸塞州 Newton，享年 93 岁；葬于纽约州 Valhalla 的 Kensico 墓园。
- 家庭：父 Emanuel B. Glauber 为旅行推销员，母 Felicia（娘家姓 Fox）；有一妹；1960 与 Cynthia Rich（1933 年生）结婚，1975 离异；一子一女、五个孙辈。
- 教育：Bronx High School of Science（1941 届，该校**首届**毕业生）→ Harvard（AB 1946、PhD 1949）。
- Manhattan Project：大二结束后被征召，18 岁入 Los Alamos，是实验室最年轻的科学家之一，计算原子弹**临界质量**；Trinity 核试验最后几位在世目击者之一。
- 博士导师：Julian Schwinger；博士论文 *The relativistic theory of meson fields*（1949）。
- 任职：Harvard 全程（Mallinckrodt 讲席教授）；1951 年 Caltech 临时讲师（**顶替 Richard Feynman** 的教席）；1967 年 CERN 访问学者（sabbatical）；Arizona 大学光学科学兼职教授。
- 关键荣誉：Guggenheim Fellowship（1957）；Albert A. Michelson Medal（1985）；Max Born Award（1985）；Humboldt Prize（1989）；Dannie Heineman Prize for Mathematical Physics（1996）；英国皇家学会外籍院士 ForMemRS（1997）；Nobel（2005，一半）；西班牙 CSIC 金奖。
- 知名博士生：Leo Kadanoff、Daniel Kleitman、Daniel Frank Walls；另有学生 Victor Franco（多重散射理论合作）。
- 核心贡献清单：
  1. 1963 年建立**光子探测模型**，奠定光学相干性的量子理论（诺奖核心）
  2. **相干态（Glauber states）**——激光光的量子描述
  3. **Glauber–Sudarshan P 表示**
  4. 1963 年 Ising 模型随机动力学（**Glauber dynamics**）——一级相变动力学研究先驱
  5. **Glauber 多重散射理论**（高能强子碰撞的统计关联）
- 关键时间线（15–20 节点）：1925 生纽约 → 1937 自制反射望远镜在美国自然历史博物馆报告 → 1941 Bronx 科学高中首届毕业 → Manhattan Project 征召（18 岁，Los Alamos 临界质量）→ Trinity 试验目击 → 1946 Harvard 学士 → 1949 博士（Schwinger 门下）→ 1951 Caltech 临时讲师顶替 Feynman → 1957 Guggenheim → 1963 光子探测模型 + Glauber dynamics 同年发表 → 1967 CERN 访问 → 1985 Michelson Medal + Max Born Award → 1989 Humboldt Prize → 1996 Heineman Prize → 1997 ForMemRS → 多年担任 Ig Nobel 颁奖礼「Keeper of the Broom」（2005 因领诺奖缺席）→ 2005 诺贝尔物理学奖一半 → 2018-12-26 逝于 Newton。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum optics | 量子光学 | 开创领域，2005 诺奖核心 | 核心页 |
| 1 | optical coherence | 光学相干性 | 光子探测模型、相干态 | 核心页 |
| 2 | theoretical physics | 理论物理 | Harvard Mallinckrodt 讲席 | 身份页 |
| 3 | statistical physics | 统计物理 | Glauber dynamics（Ising 随机动力学） | 动力学页 |
| 4 | scattering theory | 散射理论 | Glauber 多重散射理论 | 散射页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致，只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Julian Schwinger | 师→生（博士导师） | Harvard 博士导师（1949） |
| advisor-student | Leo Kadanoff | Glauber→学生 | 博士生，临界现象与重整化群名家 |
| advisor-student | Daniel Kleitman | Glauber→学生 | 博士生，组合数学家 |
| advisor-student | Daniel Frank Walls | Glauber→学生 | 博士生，量子光学名家 |
| advisor-student | Victor Franco | Glauber→学生 | 学生，多重散射理论合作 |
| co-honored | John L. Hall | 无向 | 2005 诺贝尔物理学奖共同得主（Hall/Hänsch 共享另一半） |
| co-honored | Theodor W. Hänsch | 无向 | 2005 诺贝尔物理学奖共同得主（Hall/Hänsch 共享另一半） |
| spouse | Cynthia Rich | 无向 | 1960 结婚，1975 离异 |

> 入库注意：Kadanoff 沿用库内 `Leo Kadanoff`（id=1050）、Schwinger 沿用库内 `Julian Schwinger`（id=2114）；Feynman 顶替教席一事**不建关系**（非实质师承/合作）。

### 第 5 步：设计配色方案 【人物专属】

- **气质**：清澈、秩序、幽默
- **配色**：主色 **深青绿 `#145C54`**（光的量子秩序）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeCoh` 光学相干性 — 青绿 `#0E7C7B`
  - `badgeDet` 光子探测 — 靛蓝 `#4C5FD5`
  - `badgeDyn` Glauber dynamics — 琥珀 `#E07B30`
  - `badgeScat` 多重散射 — 玫瑰 `#C4204F`
- **背景母题**：整齐波列与散乱光子点的双态对比。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；封面有国籍。
2. **必须有身份信息页**：左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域），事实取自 infobox 不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 量子光学之父 / Roy J. Glauber 1925–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 光学相干性 / 相干态 / Glauber dynamics / 多重散射
04  少年与 Los Alamos (1925–1946) — 首届 Bronx 科学高中、18 岁临界质量、Trinity 目击
05  Harvard 与 Schwinger (1946–1951) — 介子场相对论理论、Caltech 顶替 Feynman 讲师
06  1963：光的量子理论（核心贡献页）— 公式框放相干态定义式 |α⟩（page.md 无显式公式，注明为概念图式）
07  激光 vs 灯泡 — 光子探测模型、Glauber–Sudarshan P 表示
08  Glauber dynamics — Ising 模型随机动力学、一级相变
09  多重散射理论 — 高能碰撞的统计关联
10  门生与传承 — Kadanoff、Kleitman、Walls
11  荣誉与认可 — Nobel 2005（一半）· Heineman 1996 · ForMemRS 1997 · Born 1985
12  舞台之外 — Ig Nobel「Keeper of the Broom」、军控与防扩散委员会
13  遗产：量子光学的基石
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 每写完一页 make，用 pdftoppm 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Glauber 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | Glauber 得**一半**，Hall 与 Hänsch 共享**另一半**（每人工分之一）；勿写成"三人平分" |
| 获奖理由 | 官方为 "for his contribution to the quantum theory of optical coherence"；Hall/Hänsch 的"激光精密光谱"理由勿安在 Glauber 头上 |
| 肖像描述 | infobox 为 "Glauber in 2012" 照片；生卒 1925-09-01 ~ 2018-12-26，享年 93 |
| Feynman 一节 | 1951 年在 Caltech 顶替 Feynman 任临时讲师——是事实但**非师承/合作关系**，叙事可用、关系库不建 |
| Los Alamos 年龄 | 18 岁、最年轻科学家**之一**，勿写"唯一"；工作是**临界质量计算** |
| 首届毕业 | 1941 届是 Bronx 科学高中**首届**毕业班 |
| 学生名单 | infobox 博士生 Kadanoff/Kleitman/Walls 三人 + 正文 Victor Franco；勿再扩写 |
| 配偶 | Cynthia Rich，1960–1975，后离异——勿写成"白头偕老" |
| Ig Nobel | 「Keeper of the Broom」扫纸飞机是真实传统；2005 因领诺奖缺席 |
| 出生地 | 纽约市出生、晚年居马州 Arlington，逝于 Newton——三地勿混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| quantum optics | 量子光学 | 他开创的领域 |
| optical coherence | 光学相干性 | 诺奖理由核心词 |
| coherent state | 相干态（Glauber states） | 激光的量子态 |
| photodetection | 光子探测 | 1963 模型 |
| Glauber–Sudarshan P representation | Glauber–Sudarshan P 表示 | 与 Sudarshan 共享命名 |
| Glauber dynamics | Glauber 动力学 | Ising 模型随机演化，非光学 |
| multiple scattering theory | 多重散射理论 | 高能碰撞 |
| critical mass | 临界质量 | Los Alamos 时期 |
| Manhattan Project | 曼哈顿计划 | 18 岁参与 |
| Ig Nobel | 搞笑诺贝尔奖 | 扫帚守护者 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（纪录片 / 电影 / 稳重）
- **匹配理由**: 曲名「不可见之光」与光学主题天然呼应；纪录片气质贴合从 Los Alamos 少年到量子光学奠基人的传记主线。
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **备注**: 批内曲不重复（前两人用 Savage/Expedition）。

---

## 五、关键参考文件 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Roy_J._Glauber/page.md` | 本地 Wikipedia 事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Roy_J._Glauber.yaml` | 社会关系入库 yaml（name_en 写库内形式 Roy Glauber） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
