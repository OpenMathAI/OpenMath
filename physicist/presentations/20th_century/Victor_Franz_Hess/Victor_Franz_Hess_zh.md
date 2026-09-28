# 物理学家立传提示词（Victor Franz Hess）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖得主的「人物专属立传提示词」，以 Kenneth G. Wilson 篇为结构母本（0–11 节骨架一致）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Victor Franz Hess（维克托·弗朗茨·赫斯，1936 诺贝尔物理学奖，宇宙线的发现者，与 Carl David Anderson 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Hess 篇的设计重心是**向上飞行的勇气**——1911-1912 年乘气球升至 5.3 公里、昼夜兼程、以身为器，立传以「气球—高度—辐射强度」为视觉主线。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Victor Franz Hess（1883-06-24 ~ 1964-12-17，享年 81 岁）
- **气质关键词**：**宇宙线的发现者、气球上的实验家、两次流亡的奥地利人** —— 1936 诺贝尔物理学奖获奖理由：
  > "For his discovery of cosmic radiation."（因发现宇宙辐射）
- **设计母题**：**高度（altitude）**。辐射强度随高度上升而增加的曲线，与「离开地面才能看见真相」的人生轨迹（维也纳→ Graz →因斯布鲁克→纽约 Fordham）互为隐喻。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/20th_century/Victor_Franz_Hess/page.md`（Wikipedia 全文已抓取；**本篇 page.md 较短，无载内容一律禁写**）
- **待下载**：本目录尚无 `Victor_Franz_Hess.html` 与 `images/`，第 0 步需从 `https://en.wikipedia.org/wiki/Victor_Franz_Hess` 下载页面与肖像（infobox 1936 年照片、气球返回照 `Hessballon.jpg`）。
- **参考模板**：
  - 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- page.md 已在本地（见上），**事实基准如下**（以 page.md 为唯一依据）：
  - 生卒（1883-06-24 生于奥匈帝国施蒂里亚 Deutschfeistritz 的 Waldstein Castle ~ 1964-12-17 逝于美国纽约州 Mount Vernon，死于帕金森病，享年 81 岁）
  - 国籍（奥地利；1944 入籍美国；frontmatter nationality: United States / Austria）
  - 父母（父 Vinzens Hess 为奥廷根-瓦勒施泰因亲王手下的皇家林务官；母 Serafine Edle von Grossbauer-Waldstätt）
  - 教育（1893-1901 Graz-Gymnasium → 1901-1905 格拉茨大学 → 1906 维也纳大学博士 → 1906-1910 维也纳博士后）
  - 学术导师（infobox: Franz S. Exner、Leopold Pfaundler）
  - 任职机构（1910 维也纳镭研究所 Stefan Meyer 助手 → 1920 格拉茨大学实验物理副教授 → 1921-1923 美国镭公司新泽西研究实验室主任 + 美国矿业局物理顾问 → 1923 回 Graz → 1925 正教授 → 1931 因斯布鲁克大学放射学研究所所长 → 1937 Graz 物理研究所所长 → 1938 被解职后赴美 → 1938-1958 福特汉姆大学物理学教授（1958 退休））
  - 关键荣誉（Ignaz Lieben Prize 1919、Nobel 1936、Austrian Decoration for Science and Art 1959）
  - 家庭（1920 娶 Marie Bertha Warner Breisky（1955 因癌症去世）；同年娶照顾过 Marie 的 Elizabeth M. Hoenke）
  - 信仰（罗马天主教徒；1946 年发表 "My Faith" 一文阐述科学-宗教观）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1883 Waldstein Castle 生 → 1893 入 Graz-Gymnasium → 1901 入格拉茨大学 → 1906 维也纳大学博士 → 1910 入维也纳镭研究所 → 1911-1912 系列气球飞行（昼/夜，最高 5.3 km）→ 1912 发表于奥地利科学院院刊：1 km 内下降、以上显著增加、5 km 处约两倍海平面 → 1919 Lieben 奖 → 1920 格拉茨副教授 + 结婚 → 1921-1923 赴美（美国镭公司/矿业局）→ 1923 回格拉茨 → 1925 正教授 → 1931 因斯布鲁克放射学研究所所长 → 1936 诺贝尔奖（与 Anderson 共享）→ 1937 回 Graz 任物理研究所所长 → 1938 Anschluss 后被解职、移居美国 → 1944 入籍美国 → 1946 发表 "My Faith" → 1955 Marie 去世、续娶 Elizabeth → 1958 从 Fordham 退休 → 1959 奥地利科学与艺术勋章 → 1964-12-17 Mount Vernon 逝世

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用本目录 `Victor_Franz_Hess/` 并创建 `images/`。

### 第 2 步：复制 Makefile 【模板通用】

- 复制参照成品 `Makefile`，设置 `MAIN=Victor_Franz_Hess_zh`、`VIDEO_NAME=Victor_Franz_Hess_zh`。

### 第 3 步：收集图片 【人物专属】

- 下载 infobox 1936 肖像到 `images/`；404 用 Commons `Special:FilePath` 试名（候选：`Hessballon.jpg` 气球返回照）。本篇 page.md 无更多插图来源，图片不足时用装饰圆占位。

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Hess 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cosmic rays | 宇宙线 | 1912 气球飞行发现来自外太空的穿透辐射 | 核心页 |
| 1 | ionizing radiation | 电离辐射 | 大气电离度随高度的精确测量 | 核心页 |
| 2 | radiology | 放射学 | 1931 因斯布鲁克放射学研究所所长 | 任职页 |
| 3 | experimental physics | 实验物理 | 验电器精度改造 + 亲乘气球测量 | 贯穿页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Franz S. Exner | 导师→本人 | infobox 学术导师（亦是薛定谔的 habilitation 导师） |
| advisor-student | Leopold Pfaundler | 导师→本人 | infobox 学术导师 |
| spouse | Marie Breisky | 无向 | 1920 年结婚，1955 年病逝 |
| spouse | Elizabeth Hoenke | 无向 | 1955 年续娶 |
| colleague | Stefan Meyer | 无向 | 1910 年镭研究所上司 |
| co-honored | Carl David Anderson | 无向 | 1936 诺贝尔物理学奖共享（宇宙线 / 正电子） |
| colleague | Robert Millikan | 无向 | 证实其发现并命名 cosmic rays |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：高空、清冽、向上的勇气
- **配色**：高空紫（主色 `#4A2E6F`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeCos` 宇宙线 — 高空紫 `#4A2E6F`
  - `badgeIon` 电离辐射 — 钢青 `#46707E`
  - `badgeRad` 放射学 — 玫瑰 `#C4204F`
  - `badgeExp` 实验物理 — 琥珀 `#E07B30`
- **背景母题**：柔和气泡中以「自下而上渐密的圆点列」模拟辐射强度随高度的曲线，呼应设计母题。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页：左侧头像 + 右侧信息网格（生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
3. 结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 宇宙线的发现者 / Victor Franz Hess 1883–1964 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含教育、任职、荣誉、核心领域）
03  核心贡献概览 — 宇宙线 / 电离辐射 / 放射学 / 气球实验
04  林务官之子（1883–1910）— Waldstein Castle、Graz 与维也纳、镭研究所
05  大气电离之谜 — 验电器的反常读数、两种假说的对峙
06  1912：五千米上的发现（核心贡献页）— 昼夜气球飞行、1 km 拐点、5 km 两倍读数
07  公式框页 — 辐射强度—高度曲线示意 I(h)（page.md 无公式，此为概念图式并注明）
08  命名与证实 — Millikan 命名 cosmic rays；正电子/μ子由宇宙线中寻得（Anderson）
09  1936：半个诺贝尔 — 与 Anderson 共享、工作互不相关（宇宙线一半 / 正电子一半）
10  两次跨大西洋（1921 & 1938）— 美国镭公司/矿业局；Anschluss 后流亡
11  Fordham 与信仰 — 1944 入籍、"My Faith"（1946）
12  荣誉与认可 — Lieben 1919 · Nobel 1936 · 奥地利科学与艺术勋章 1959
13  遗产：粒子天体物理的起点
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；头部宏定义整体复用结构母本骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make distclean && make pdf`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hess 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "For his discovery of cosmic radiation."；1936 与 Anderson 共享——Hess 一半宇宙线、Anderson 一半正电子，**工作互不相关**（同 1978 年 Kapitsa/Penzias 结构），勿写成共同研究 |
| 命名权 | "cosmic rays" 一名由 Robert Millikan 所起（其证实了 Hess 的发现）；勿写"Hess 命名宇宙线" |
| 数值口径 | 辐射 1 km 内下降、以上显著增加；5 km 处约为海平面两倍；气球最高 5.3 km——三组数字勿混 |
| 博士归属 | 1901-1905 就读**格拉茨大学**、1906 博士由**维也纳大学**授予——两校勿混（frontmatter educated_at 只列 Graz，infobox 两者并载） |
| 导师口径 | 学术导师为 Exner 与 Pfaundler（infobox）；Exner 亦是薛定谔的 habilitation 导师，跨篇注意一致性 |
| 解职原因 | 1938 因 Anschluss 被 Graz 解职——page.md 明载 "dismissed from his post"，勿写成主动辞职 |
| 生卒地 | 生于施蒂里亚 Deutschfeistritz（Waldstein Castle）、逝于纽约州 Mount Vernon，勿互换 |
| 死因 | 帕金森病，勿写"卒于纽约市"泛称 |
| 妻子 | 两任妻子 Marie Breisky（d. 1955）与 Elizabeth Hoenke（m. 1955，曾照顾 Marie）——年份与关系勿混 |
| 材料边界 | 本篇 page.md 很短：无博士论文题目、无知名学生名单、无 1912 飞行赞助细节——**无载一律禁写**，不从他处补料 |
| 同名区分 | Victor Franz Hess（德语发音），中名有时英化作 Francis（note 明载）；勿与别的 Hess 混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| cosmic rays | 宇宙线 | Millikan 命名；亦作宇宙射线 |
| cosmic radiation | 宇宙辐射 | 获奖理由原文用词 |
| ionizing radiation | 电离辐射 | 大气电离度测量的对象 |
| electroscope | 验电器 | 当时的辐射测量仪器 |
| balloon flight | 气球飞行 | 1911-1912 系列观测 |
| Institute for Radium Research | （维也纳）镭研究所 | 1910 起点勿译作"镭学院" |
| positron | 正电子 | Anderson 在宇宙线中发现 |
| muon | μ 子 | 同在宇宙线中发现（Anderson） |
| astroparticle physics | 粒子天体物理 | 其遗产所在领域 |
| Ignaz Lieben Prize | 伊格纳兹·利本奖 | 1919，奥地利科学院 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（66k views）
- **风格**: 探索 / 史诗 / 远征
- **匹配理由**: 1911-1912 的气球飞行本质是一场以生命为赌注的科学远征——昼夜升空、直上五千米；Expedition 的远征式叙事与其"以身为器、向上飞行"的设计母题严丝合缝。
- **备选**（未采用）: Ascension（上升感匹配高度母题但气质偏科幻）；Winds Of Freedom（史诗/英雄，匹配流亡与自由但戏剧性盖过实验家的朴素）。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → `presentations/20th_century/Victor_Franz_Hess/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Victor_Franz_Hess/page.md` | 本地 Wikipedia 正文（事实基准，较短、无载禁写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库引擎 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；本篇材料薄，所有事实以 page.md 为准，无载禁写。**
