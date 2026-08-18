# 尤金·维格纳 (Eugene Paul Wigner) 立传提示词

> 本提示词严格遵循 `physicist` 项目的人物立传规范，并参照数学家侧 `mathematician/presentations/prompts/20th_century/David_Hilbert_zh.md` 的结构（含「研究领域」与「社会关系 + 数据库入库」两章），为维格纳制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标物理学家**: Eugene Paul Wigner (Wigner Jenő Pál，1902-11-17 ~ 1995-01-01)
- **气质关键词**: **对称性的先知、群论进入物理的桥梁、核时代的建筑师、数学哲学家** — "因对原子核和基本粒子理论的贡献，特别是基本对称性原理的发现与应用"（1963 诺贝尔物理学奖获奖理由）
- **本地 Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner.html`
  - 已从中提取正文、肖像 `images/Wigner.jpg`
- **已生成成品**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（15 页，编译通过）
- **参考模板**:
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/cover/openphysicist_page.tex` — OpenPhysicist 项目首页（统一 `\input`）
  - 数学家侧成品 `mathematician/presentations/hilbert/David_Hilbert_zh.tex` — 卡片版式参考
- **配套数据库脚本**（见第 4.5 步）：
  - `MySQL/seed_wigner_full.py` — 人物主记录修正 + 研究领域入库（`person_field`）
  - `MySQL/seed_wigner_relations.py` — 社会关系入库（`person_relation`）

---

## 你的任务

按照本提示词的步骤依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

> **数据库同步要求**：本提示词包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤。请严格按步骤操作，将维格纳的**研究领域**与**社会关系**写入 `greatminds` 数据库（MySQL），这是 OpenPhysicist 项目人物关系网络的一部分，与 Beamer 立传并行。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取 `Eugene_Wigner.html` 正文与 infobox
- 输出供校验的信息：
  - 生卒日期 (1902-11-17 ~ 1995-01-01，享年 92 岁)
  - 国籍变迁 (奥匈帝国/匈牙利 → 美国，naturalized 1937)
  - 博士导师 (Michael Polanyi；学术顾问 László Rátz、Richard Becker)
  - 主要任职机构 (Göttingen 1926–27 → Princeton University 1930–1971；Manhattan Project；Oak Ridge / Clinton Lab 1946–47)
  - 关键荣誉 (Nobel Prize in Physics 1963；Enrico Fermi Award 1958；Max Planck Medal 1961；Franklin Medal 1950；Medal for Merit 1946)
  - 知名学生 (John Bardeen — 唯一两获诺奖；Victor Weisskopf、Marcos Moshinsky、Abner Shimony、Edwin T. Jaynes、Frederick Seitz、Conyers Herring 等)
  - Wikipedia 正文提取的**关键时间线**（按年份列出 15–20 个节点）
  - 核心贡献清单（见第 4 步）

---

## 第 1 步：建立目录

- 在 `physicist/presentations/20th_century/` 下创建 `Eugene_Wigner/` 子目录与 `images/`

---

## 第 2 步：复制 Makefile

- 参照同目录 `Makefile` 模板，设置 `MAIN=Eugene_Wigner_zh`

---

## 第 3 步：收集图片

- 使用已下载的 `images/Wigner.jpg`（维格纳肖像）作为封面图

---

## 第 4 步：研究领域梳理（★ 这是本提示词的核心新增章节）

> **目的**：把数学家提示词中的「核心数学贡献按领域」升级为**显式的研究领域清单**，并直接对应数据库 `fields` + `person_field` 表，使"研究领域"成为可检索、可图形化的结构化字段，而不只是 Beamer 里的四个彩色 badge。

### 4.1 维格纳的研究领域（按重要性 rank 排序）

| rank | 领域 (field, name_en) | 中文 | 说明 | 对应 Beamer 页 |
|:--:|------|------|------|------|
| 0 | symmetry (group theory in physics) | 对称性 / 物理中的群论 | 把群论引入量子力学，对称性原理的数学化 | 封面、对称性页 |
| 1 | nuclear physics | 原子核物理 | 核结构、壳层模型萌芽、宇称守恒 | 核心贡献页 |
| 2 | quantum mechanics | 量子力学 | Wigner 定理、Wigner–Eckart 定理、D-矩阵 | 对称性页、冷门亮点页 |
| 3 | solid-state physics | 固体物理 | Wigner 晶体、Wigner–Seitz 原胞 | 冷门亮点页 |
| 4 | mathematical physics | 数学物理 | 群论专著、Wigner 拟概率分布、随机矩阵 | 学术黄金期页 |

> 领域字典 `fields` 表：已存在 `group theory`(42)、`mathematical physics`(7)、`theoretical physics`(15)、`quantum mechanics`(43)；缺失的 `atomic physics`/`nuclear physics`/`solid-state physics`/`symmetry` 由 `seed_wigner_full.py` 自动补建。

### 4.2 入库操作（见 `MySQL/seed_wigner_full.py`）

- 修正 `people` 主表中 Wigner 的 `primary_occupation` 为 `physicist`（原库误标 `mathematician`），补全 `name_zh='维格纳'`、`has_biography=1`
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 执行后校验：
  ```sql
  SELECT f.name_en, pf.rank FROM person_field pf
  JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=352 ORDER BY pf.rank;
  ```

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> **目的**：将维格纳的师承、合作、门生、家庭与历史共同体写入 `person_relation`，形成可查询的人物关系网络。这是 Beamer「门生与传承」「哥廷根岁月」等页的数据底座。

### 4.5.1 关系清单（从 Wikipedia 提取）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael Polanyi | 师→生（Polanyi 为博士导师） | 柏林 Kaiser Wilhelm 研究所时期的博士导师 |
| advisor-student | László Rátz | 师→生（中学数学老师） | Fasori 中学的数学老师，启蒙者 |
| advisor-student | Richard Becker | 师→生（学术顾问） | Göttingen 前在柏林随 Becker 研习量子力学 |
| colleague | Hermann Weyl | 无向 | 共同把群论引入物理；对称性理论的双子星 |
| colleague | John von Neumann | 无向 | 匈牙利「火星人」天才群体；普林斯顿同事 |
| colleague | David Hilbert | 无向 | Göttingen 时期任 Hilbert 助手 |
| advisor-student | John Bardeen | 生→师（Wigner 为学生） | 唯一两获诺贝尔物理学奖的学生 |
| spouse-family | Paul Dirac | 无向（姻亲） | 妹妹 Margit (Manci) 嫁 Dirac，Dirac 为妹夫 |
| colleague | Leó Szilárd | 无向 | 曼哈顿计划伙伴；爱因斯坦–西拉德信共同参与者 |
| co-honored | Maria Goeppert Mayer / J. Hans D. Jensen | 无向 | 1963 诺贝尔物理学奖共同得主（核壳层结构） |

> 关系类型键取自 `relation_types`：advisor-student / colleague / co-honored / spouse（姻亲用 spouse 表，note 注明「妹夫」）。

### 4.5.2 入库操作（见 `MySQL/seed_wigner_relations.py`）

- 连接 `greatminds` 库，以 `name_en='Eugene Wigner'`（id=352）为中心
- 库中已存在：Hilbert(1)、Weyl(6)、von Neumann(3)、Szilárd(357)、Dirac(541)
- 不在库的先建占位（`has_biography=0`），关系 note 加 `[材料待展开] ` 前缀
- 有向关系 advisor-student 按师→生；无向（colleague/co-honored/spouse）按 `MIN(id)→MAX(id)` 存储
- 执行后校验：
  ```sql
  SELECT a.name_en 甲, rt.name_zh 关系, b.name_en 乙, pr.note
  FROM person_relation pr
  JOIN people a ON a.id=pr.from_id
  JOIN people b ON b.id=pr.to_id
  JOIN relation_types rt ON rt.relation_key=pr.relation_type
  WHERE 352 IN (pr.from_id, pr.to_id);
  ```
- 汇报：新建 X 人（占位）、新增 Y 条关系

---

## 第 5 步：设计配色方案

- 维格纳气质：**沉静、对称、理性、跨越物理与数学**
- **建议配色：深海军蓝 + 香槟金**（对称与秩序）+ 四个分类色：
  - `badgeSym` 对称/群论 — 靛蓝 `#4C5FD5`
  - `badgeQm` 量子力学 — 青绿 `#0E7C7B`
  - `badgeNucl` 原子核 — 陶土 `#B85C38`
  - `badgePhil` 数学哲学 — 棕灰 `#8D6E63`
- 背景采用左右镜像对称的圆形装饰呼应"对称性"主题（已实现于成品）

### 5.1 格式硬要求（对齐 OpenMath 数学家 deck 规范）★

> 每一位物理学家的立传 deck **必须**满足以下三点，否则视为未完成：

1. **封面有头像**：右上角放置人物肖像（如 `Wigner.jpg`），配 `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（如"匈牙利—美国"），且底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（Identity / Bio 速览页）：置于封面之后、核心贡献之前。布局为**左侧头像 + 右侧信息网格**，含至少：生卒、本名、国籍、出生地、师承（博士导师/中学老师/学术顾问）、任职（机构与年份）、主要荣誉、核心领域。事实取自本地 Wikipedia infobox（见第 0 步），不得杜撰。

---

## 第 6 步：规划幻灯片序列（实际成品 15 页）

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 《对称性的先知》/ Eugene Wigner 1902–1995 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒 / 本名 / 国籍 / 出生地 / 师承 / 任职 / 主要荣誉 / 核心领域
03  核心贡献概览 — 对称性 / 群论 / 原子核 / 数学哲学
04  早年：布达佩斯 — Fasori 中学、与 von Neumann 同窗、妹妹嫁 Dirac
05  哥廷根岁月 — Hilbert 助手、Wigner D-矩阵
06  学术黄金期 — 普林斯顿、1931 群论专著、Wigner–Seitz 原胞
07  对称性与群论 — Wigner 定理、Wigner–Eckart 定理
08  鲜为人知的「维格纳家族」 — Jordan–Wigner、Wigner 晶体、Wigner 拟概率、Wigner's friend
09  曼哈顿计划 — 爱因斯坦–西拉德信、反应堆设计
10  橡树岭与官僚之战 — Clinton Lab、AEC 冲突
11  门生与传承 — John Bardeen（两获诺奖）、匈牙利「火星人」
12  数学的有效性与荣誉 — 不可思议的有效性、诺贝尔奖、费米奖
13  代表著作 — 1931 群论德文原著、中子链式反应堆、回忆录
14  遗产 — 对称性贯穿现代物理
15  结尾
```

---

## 第 7 步：编写 Beamer 源码

- 文件名：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
- 每页用 `\newcommand{\xxxslide}{...}` 定义，配色与卡片版式见成品
- **身份信息页实现模式**（参照成品 `\profileslide`）：
  - 用 `\newcommand{\lab}[1]{...}` 定义字段标签样式（小号加粗金色）
  - 左：`\includegraphics[width=2.7cm,height=3.5cm,keepaspectratio]{Wigner.jpg}` + 姓名注
  - 右：4 个 `infob` 圆角卡片（text width≈11cm，居中于 x=1.4），分别放 生卒+本名 / 国籍+出生地 / 师承+任职 / 荣誉+核心领域
  - 任职务必含 `Göttingen 1926–27（Hilbert 助手）· 普林斯顿 1930–1971 · 曼哈顿计划 · 橡树岭`，与封面底部状态栏一致

---

## 第 8 步：布局检查 ★★★ 编译即查

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图肉眼检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

---

## 第 9 步：史实审查 + 术语审查

### 维格纳特殊陷阱

| 陷阱 | 说明 |
|------|------|
| 群论引入 | 与 Weyl **共同**引入，不要写成"独自" |
| Wigner 定理 | 1931，量子对称变换的幺正/反幺正分类，不要与 Wigner–Eckart 混 |
| 核壳层模型 | 维格纳是早期思想萌芽，完整模型由 Mayer/Jensen（诺奖共同得主）完成 |
| 曼哈顿计划角色 | 反应堆设计主导者之一，不是炸弹直接设计者 |
| 「不可思议的有效性」 | 1960 年论文，是哲学之问，不要写成"结论" |

### 术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Wigner's theorem | Wigner 定理 | 幺正/反幺正 |
| Wigner–Eckart theorem | Wigner–Eckart 定理 | 约化矩阵元 |
| Wigner D-matrix | Wigner D-矩阵 | 角动量旋转 |
| Jordan–Wigner transformation | Jordan–Wigner 变换 | 自旋↔费米子 |
| Wigner crystal | Wigner 晶体 | 低温电子晶格 |
| Wigner quasiprobability distribution | Wigner 拟概率分布 | 相空间，可取负值 |
| Wigner's friend | Wigner 的朋友（佯谬） | 量子测量哲学 |

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner.html` | 本地 Wikipedia 正文 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 成品 Beamer（15 页） |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_wigner_full.py` | 研究领域入库（第 4 步） |
| `MySQL/seed_wigner_relations.py` | 社会关系入库（第 4.5 步） |
| `maintenance_guide/database_schema.md` | 数据库表结构（fields / person_field / person_relation） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
