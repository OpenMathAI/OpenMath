# 物理学家立传提示词（21 世纪批次 · Eric A. Cornell）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传提示词**，目标人物：Eric A. Cornell（2001 诺贝尔物理学奖，玻色–爱因斯坦凝聚）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Eric Allin Cornell（埃里克·康奈尔），21 世纪（2001）诺奖得主系列。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域表」；Cornell 篇以「把原子冷却到绝对零度附近、让百万原子凝成一个量子态」为叙事主线。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Eric Allin Cornell（1961-12-19 生于加州帕洛阿尔托，在世）
- **气质关键词**：**碱金属气体中的第一个玻色–爱因斯坦凝聚、激光冷却与蒸发冷却的联姻者、JILA/NIST 的超冷原子旗手** —— 2001 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the achievement of Bose-Einstein condensation in dilute gases of alkali atoms, and for early fundamental studies of the properties of the condensates"（因实现稀薄碱金属气体中的玻色–爱因斯坦凝聚，以及对凝聚体性质的早期基础研究）
- **设计母题**：**宏相干（macroscopic coherence）**。1995 年 6 月，康奈尔与维曼把铷原子气体冷却到约 170 nK，数十万原子「凝」入同一个量子基态——封面视觉用密集小圆点逐渐归并为单一波纹环带，呼应「百万原子，一个波函数」。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Eric_A._Cornell/page.md`（**已有本地**）
- **页面 HTML 与图片**：`Eric_A._Cornell.html` 与 `images/` **待下载**，Wikipedia URL：`https://en.wikipedia.org/wiki/Eric_A._Cornell`
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求意见再继续。
> 数据库写入 `greatminds`（MySQL），yaml 母本 `MySQL/data/Kenneth_G_Wilson.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（21th_century/21st_century/Eric_A._Cornell/）
- 🔲 待下载 `Eric_A._Cornell.html` 与 infobox 头像 `images/`（Commons/Wikipedia REST API 回退，404 则装饰圆占位）
- 事实基准（已按 page.md 核对）：
  - 生卒：1961-12-19 生于 Palo Alto, California（在世）；父母当时在斯坦福完成研究生学业，两岁后随父迁 Cambridge, MA，父亲为 MIT 土木工程教授；幼年随父学术休假暂居伯克利与里斯本
  - 国籍：美国
  - 教育：Cambridge Rindge and Latin School；高中最后一年回加州入旧金山 Lowell High School（磁石学校）；Stanford BS 1985（以 honors and distinction 毕业；本科在低温物理实验室打工；曾赴中国与台湾九个月教英语并学中文；在斯坦福结识后来的妻子 Celeste Landry）；MIT PhD 1990
  - 博士导师：David E. Pritchard（MIT）；博士论文《Mass spectroscopy using single ion cyclotron resonance》(1990)；参与氚 β 衰变测电子中微子质量实验，未测得质量
  - 博士后：1990 起在科罗拉多大学博尔德分校 Carl Wieman 组（小规模激光冷却实验，约两年）
  - 任职：JILA/NIST 获永久职位（基于其 BEC 提案）；现任 University of Colorado Boulder 教授 + 美国商务部 NIST Fellow；实验室在 JILA
  - 关键荣誉：Fritz London 1996 · Zeiss 1996 · King Faisal 1997 · Waterman 1997 · I. I. Rabi 1997 · Lorentz 1998 · R. W. Wood 1999 · Benjamin Franklin 1999/2000（正文两处年份，infobox 作 2000，引用时注明）· NAS 2000 · Nobel 2001 · AAAS Fellow 2005 · Ioannes Marcus Marci Medal 2012
  - 知名学生：Laura C. Sinclair（infobox 博士生）；Deborah S. Jin 1997 加入其 JILA 小组（同事，非本页博士生栏）
  - 核心贡献：①1995-06 与 Wieman 实现首个玻色–爱因斯坦凝聚（稀薄碱金属气体）；②提出激光冷却+蒸发冷却+磁阱的 BEC 路线；③凝聚体早期基本性质研究；④超冷原子与精密测量长期纲领
  - 个人生活：1995 年（BEC 成功前数月）娶 Celeste Landry；两个女儿 1996/1998；2004-10 因坏死性筋膜炎截去左臂与肩，2005-04 重返部分工作；移居 Boulder 后多次参加 Bolder Boulder 跑步赛（最近 2022）
  - 诺奖演讲：2001-12-08 "Bose-Einstein Condensation in a Dilute Gas; The First 70 Years and Some Recent Experiments"
  - 关键时间线（≥15 节点）：1961 生帕洛阿尔托 → 幼年迁 Cambridge → Lowell HS → 1985 Stanford 毕业 → 中国/台湾九个月 → MIT Pritchard 组 → 1990 博士（单离子回旋共振质谱）→ 1990 赴 Boulder Wieman 组博后 → 提出 BEC 方案 → 入职 JILA/NIST → 1995-06 首个 BEC → 1995 Gamow 纪念演讲（与 Wieman）→ 1996 London/Franklin 前奏奖项潮 → 1997 Faisal/Waterman/Rabi → 1998 Lorentz → 2000 NAS → 2001 诺奖 → 2004 截臂与康复 → 2005 AAAS Fellow → 至今 CU Boulder/NIST

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Bose-Einstein condensate | 玻色–爱因斯坦凝聚 | 1995 首次实现，2001 诺奖核心 | 核心页 |
| 1 | ultracold atoms | 超冷原子 | 磁阱中的稀释原子气体 | 核心页 |
| 2 | laser cooling | 激光冷却 | 与蒸发冷却联姻的降温路线 | 方法页 |
| 3 | atomic physics | 原子物理 | JILA/NIST 主业 | 身份页 |
| 4 | low-temperature physics | 低温物理 | 本科即入行，London 奖领域 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | David E. Pritchard | 师→生（博士导师） | MIT 博士导师，中微子质量/原子阱实验 |
| colleague | Carl E. Wieman | 无向 | Boulder 博士后导师与 BEC 合作者（1995） |
| co-honored | Carl E. Wieman | 无向 | 2001 诺贝尔物理学奖共享 |
| co-honored | Wolfgang Ketterle | 无向 | 2001 诺贝尔物理学奖共享 |
| colleague | Deborah S. Jin | 无向 | 1997 加入其 JILA 小组，2003 率队产出费米子凝聚 |
| advisor-student | Laura C. Sinclair | Cornell→学生 | infobox 博士生 |
| spouse | Celeste Landry | 无向 | 1995 年结婚（BEC 成功前数月） |

> 方向约定：导师（Pritchard→Cornell）有向；学生（Cornell→Sinclair）有向；同事/共同荣誉/配偶无向。

### 第 5 步：设计配色方案

- **气质**：极寒、凝聚、量子宏观相
- **配色**：深冷蓝（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 深冷蓝 `#16477C`
  - `badgeBEC` 玻色–爱因斯坦凝聚 `#3E6FB0`
  - `badgeUltra` 超冷原子 `#0E7C7B`
  - `badgeLaser` 激光冷却 `#E07B30`
  - `badgeAtomic` 原子物理 `#C4204F`
- **背景母题**：柔和气泡——稀疏小圆点群向单一环带收拢，呼应「凝聚」母题

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. 封面明示国籍，底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域），事实取自 page.md，不得杜撰。
4. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列（14 页）

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 玻色–爱因斯坦凝聚实现者 / Eric A. Cornell 1961– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 首个 BEC / 冷却路线 / 凝聚体性质 / 超冷原子纲领
04  早年：从帕洛阿尔托到剑桥 (1961–1985) — MIT 土木教授之子、Lowell HS、斯坦福、中国九个月
05  MIT 博士：Pritchard 门下 (1985–1990) — 中微子质量实验、单离子回旋共振质谱
06  博后与提案：Boulder 两年 (1990–1992) — 激光冷却+蒸发冷却+磁阱的 BEC 路线
07  JILA/NIST：永久职位与团队
08  1995：实现首个玻色–爱因斯坦凝聚（核心贡献页；公式框放概念图式——nK 级温度轴与原子云凝聚示意，page.md 无公式，注明）
09  凝聚体性质的早期基础研究
10  奖项长廊 — London 1996 · Lorentz 1998 · Franklin 1999/2000 · Nobel 2001
11  同侪与传承 — Wieman/Ketterle 共享诺奖、Deborah S. Jin 费米子凝聚
12  逆境与复原 — 2004 坏死性筋膜炎截臂、2005 复工、Bolder Boulder
13  遗产：超冷原子时代的开场人
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 表格页安全负间距：顶部 −0.35cm、arraystretch 0.78–0.82；公式框前 −0.35~−0.55cm；希腊字母一律数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 只写官方原句（见上），勿缩写成"因实现 BEC"一笔带过 |
| Franklin 奖年份 | 正文荣誉列表作 1999，infobox 作 2000——两说并存时统一按 awards 列表 1999 并加注，勿混写 |
| 首个 BEC 归属 | 是 Cornell+Wieman 合作实现（Ketterle 数月后独立实现钠原子 BEC），勿写成 Cornell 单独或三人同时 |
| Jin 的身份 | Deborah S. Jin 是 1997 加入其 JILA 小组的同事（她率队 2003 产出费米子凝聚），不是 infobox 博士生栏里的学生；infobox 博士生仅 Laura C. Sinclair |
| 博士后导师 | Wieman 是其博士后导师（page.md 明载），关系用 colleague + note 体现，白名单无 postdoc 类型 |
| 出生地与成长地 | 生于 Palo Alto，成长于 Cambridge, MA，勿混淆 |
| 在世留白 | 在世人物 death_date 省略，勿写"享年" |
| 妻子身份 | Celeste Landry 是斯坦福本科时期结识，勿写成"BEC 后成家" |
| 截臂叙事 | 2004 截臂为坏死性筋膜炎所致，客观一句即可，勿渲染 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Bose-Einstein condensate (BEC) | 玻色–爱因斯坦凝聚 | 勿漏"凝聚态"与"凝聚体"区分 |
| evaporative cooling | 蒸发冷却 | 与激光冷却互补，勿混 |
| magnetic trap | 磁阱 | 中性原子约束手段 |
| alkali atoms | 碱金属原子 | 获奖理由原文用词 |
| dilute gas | 稀薄气体 | 强调相互作用弱 |
| NIST Fellow | NIST 特级研究员 | 商务部下属研究机构职衔，勿译"院士" |
| JILA | JILA（联合实验室） | 科罗拉多大学与 NIST 联合研究所，不翻译 |
| fermionic condensate | 费米子凝聚 | 归 Jin 团队，勿算作 Cornell 获奖 |
| necrotizing fasciitis | 坏死性筋膜炎 | 医学术语客观使用 |
| single ion cyclotron resonance | 单离子回旋共振 | 博士论文主题 |

---

## 四、背景音乐选择 ✅

- **选定曲目**：**Awaken** — Alex-Productions（79k views，鼓舞/明亮）
- **匹配理由**："突破性证明/开场" 场景标签正合 1995 首个 BEC 的历史性突破；明亮底色匹配超冷原子中"点亮新态"的视觉母题；21 世纪批次开篇人物亦呼应 Awaken 之名。
- **本地路径**：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 复制为 `presentations/21th_century/Eric_A._Cornell/Awaken.wav`
- **备选**：Expedition（探索/史诗）、Daylight（明亮/轻快）

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Eric_A._Cornell/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
