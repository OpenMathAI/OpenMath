# 物理学家立传提示词（模板标杆实例：Kenneth G. Wilson）

> **本文件是 OpenPhysicist 的「物理学家立传提示词模板标杆」**，以 Kenneth G. Wilson（1982 诺贝尔物理学奖，重整化群理论）为第一个完整实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何物理学家；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck 的提示词 + tex 结构）与物理学家侧首例（Eugene Wigner）的实战经验。
- **本实例**：Kenneth Geddes Wilson（肯尼斯·格迪斯·威尔逊）。
- **设计哲学**：物理学家立传与数学家立传的核心差异，在于**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达——这两点构成物理学家模板的骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Kenneth Geddes Wilson（1936-06-08 ~ 2013-06-15，享年 77 岁）
- **气质关键词**：**重整化群的奠基人、临界现象的征服者、格点场论的先驱** —— 1982 诺贝尔物理学奖获奖理由：
  > "for his theory for critical phenomena in connection with phase transitions"（因其关于相变相关的临界现象理论）
- **设计母题**：**自相似性（self-similarity）**。重整化群的核心思想是「在不同观察尺度上，物理规律保持形式不变」——这与分形、递归、嵌套结构天然对应，是比「对称性」更贴合 Wilson 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson.html`（第 0 步下载）
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（15 页）
  - 数学家标杆：`mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Kenneth_G._Wilson` 到 `Kenneth_G_Wilson.html`（268 KB，第一轮 review 已完成事实核对）
- ✅ 已下载头像到 `images/Wilson.jpg`（Wikipedia infobox 照片）
- 提取 infobox 与正文，输出供校验（**第一轮已核对，事实基准如下**）：
  - 生卒日期（1936-06-08 生于马萨诸塞州沃尔瑟姆 ~ 2013-06-15 逝于缅因州萨科，享年 77 岁）
  - 国籍（美国）
  - 父母（父 E. Bright Wilson 为哈佛化学家/微波光谱先驱；母 Emily Buckingham Wilson 受过物理学训练）
  - 教育（16 岁进哈佛主修数学，1954/1956 两度 Putnam 前五，田径队一英里选手；Caltech 博士 1961）
  - 博士导师（Murray Gell-Mann，1969 诺奖得主）；博士论文《An investigation of the Low equation and the Chew-Mandelstam equations》
  - 博士后（Harvard + CERN）
  - 主要任职机构（Cornell 1963–1988，1970 正教授/1974 James A. Weeks 教授，期间 SLAC；1985 康奈尔理论中心主任；Ohio State 1988–2008）
  - 关键荣誉（Nobel 1982；Wolf 1980 与 Fisher/Kadanoff 共享；Franklin 1982；Heineman 1973；Boltzmann 1975；Eringen 1984；Dirac 1989；NAS/AAAS 院士 1975、APS 会员 1984）
  - 知名博士生（Roman Jackiw、Michael Peskin、Steven R. White、Paul Ginsparg、H. R. Krishnamurthy、Serge Rudaz）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 个节点）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Kenneth_G_Wilson/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录 `Eugene_Wigner/Makefile`，设置 `MAIN=Kenneth_G_Wilson_zh`、`VIDEO_NAME=Kenneth_G_Wilson_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 已下载 Wilson 肖像到 `images/Wilson.jpg`（Wikipedia infobox 照片，162×227 JPEG）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Wilson 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | renormalization group | 重整化群 | 核心思想：尺度依赖与临界现象 | 封面、核心页 |
| 1 | critical phenomena | 临界现象 / 相变 | 相变理论，1982 诺奖核心 | 核心页 |
| 2 | lattice gauge theory | 格点规范场论 | Wilson loop、格点 QCD | 格点页 |
| 3 | quantum field theory | 量子场论 | 算符乘积展开（OPE） | 场论方法页 |
| 4 | statistical mechanics | 统计力学 | 重整化群在统计物理的应用 | 临界页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Murray Gell-Mann | 师→生（博士导师） | Caltech 博士导师，1969 诺奖得主 |
| colleague | Michael Fisher | 无向 | 康奈尔同事，临界现象理论并肩者 |
| colleague | Leo Kadanoff | 无向 | 重整化群的先驱思想来源 |
| co-honored | Michael Fisher / Leo Kadanoff | 无向 | 1980 Wolf Prize 共同得主 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深邃、尺度感、跨越微观与宏观
- **配色**：深靛蓝（理论深度）+ 香槟金（诺奖）+ 四分类色
  - `badgeRG` 重整化群 — 靛蓝 `#4C5FD5`
  - `badgeCrit` 临界现象 — 青绿 `#0E7C7B`
  - `badgeLattice` 格点场论 — 琥珀 `#E07B30`
  - `badgeOPE` 场论方法 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆），呼应重整化群的尺度不变性

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 重整化群奠基人 / Kenneth G. Wilson 1936–2013 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含去世地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 重整化群 / 临界现象 / 格点场论 / 场论方法
04  早年：沃尔瑟姆神童 (1936–1956) — 16岁进哈佛、Putnam前五、田径、Woods Hole
05  Caltech 博士：Gell-Mann 门下 (1956–1961) — Low 方程、Chew–Mandelstam 方程
06  博士后：哈佛与 CERN (1961–1963)
07  康奈尔岁月：重整化群的诞生 (1963–1974) — SLAC、1970 正教授、1974 Weeks 教授
08  重整化群：把无穷大变成尺度（核心贡献页）
09  格点规范场论：把时空离散化 — Wilson loop、格点 QCD、Wilson 费米子
10  以 Wilson 命名的成果 — Wilson action / loop / ratio / Ginsparg–Wilson / NRG
11  门生与传承 — Roman Jackiw、Michael Peskin、Steven R. White
12  荣誉与认可 — Nobel 1982 · Wolf 1980 · Franklin 1982 · 院士
13  超级计算与物理教育 — 康奈尔理论中心主任、Science by Inquiry
14  遗产：从临界现象到现代物理
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）可整体复用本目录 `Kenneth_G_Wilson_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Wilson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 重整化群归属 | Wilson 把重整化群**系统化为临界现象理论**，但思想源头有 Kadanoff 的标度假设，勿写成"独自发明" |
| 诺奖理由 | Wikipedia 正文表述为 "for his work on critical phenomena using the renormalization group"，强调**相变/临界现象**，不是泛泛的"重整化群" |
| 早年细节 | 16 岁进哈佛（非普通年龄），主修**数学**，1954/1956 两度 Putnam 前五；还是田径队一英里选手，勿写成"物理本科" |
| 父亲身份 | 父 E. Bright Wilson 是哈佛**化学家（微波光谱先驱）**，不是"化学教授"的泛称；母亲亦受过物理学训练 |
| 去世地 | 2013-06-15 逝于**缅因州萨科（Saco, Maine）**，勿与出生地混淆 |
| 博士后 | 有 Harvard + CERN 两站博士后，勿遗漏 |
| 博士生 | Roman Jackiw（轴子/反常）、Michael Peskin（QFT 教科书作者）、Steven R. White（DMRG 奠基人）、Paul Ginsparg（arXiv 创始人）等，勿写成"学生不详" |
| 格点 QCD | Wilson 是格点规范场论奠基人之一，但完整 QCD 由多人共同发展 |
| Wilson loop | 是格点规范场论的规范不变量，不要与重整化群混淆 |
| 奖项完整性 | 除 Nobel 1982、Wolf 1980 外，还有 Franklin 1982、Heineman 1973、Boltzmann 1975、Eringen 1984、Dirac 1989；1975 年当选 NAS/AAAS 院士 |
| 康奈尔理论中心 | 1985 年任中心主任，是美国 NSF 五个国家超级计算中心之一，勿遗漏其计算物理先驱身份 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| renormalization group | 重整化群 | 非"重整群"，强调"群"是半群语义 |
| critical phenomena | 临界现象 | 与"相变"关联 |
| Wilson loop | Wilson 圈 | 格点规范场的规范不变量 |
| lattice gauge theory | 格点规范场论 | 时空离散化 |
| operator product expansion | 算符乘积展开（OPE） | 短距行为 |
| fixed point | 不动点 | 重整化流的收敛点 |

---

## 四、背景音乐选择 【人物专属】

- 待第 13 步完成后，参照 `music_audio/curated_tracks.md`，匹配 Wilson 气质（深邃、尺度感、理论纵深）选曲。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson.html` | 本地 Wikipedia 正文 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex` | 数学家标杆参考 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
