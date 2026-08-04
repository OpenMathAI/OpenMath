# 希尔伯特 (David Hilbert) 立传提示词

> 本提示词严格遵循 [数学家立传工作指南.md](./数学家立传工作指南.md)，以 Grothendieck 和 Riemann 成品为参考模板，为希尔伯特制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: David Hilbert (1862–1943)
- **气质关键词**: **王者、全才、乐观、20世纪数学的领航人** — "Wir müssen wissen — wir werden wissen."
- **Wikipedia 页面已下载**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/David_Hilbert/`
  - `page.md` — 正文 Markdown (~97,000 chars)
  - `page.html` — 原始 HTML 备份
  - `metadata.json` — Wikidata 元数据
  - `images.txt` — 20 张图片 URL 清单
- **参考模板**:
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` — Grothendieck 完整源码（~712 行，教皇气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` — Riemann 完整源码（~632 行，克制天才气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Makefile` — 构建脚本（直接复制）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/数学家立传工作指南.md`

---

## 你的任务

按照 [数学家立传工作指南.md](./数学家立传工作指南.md) 第十一节「推荐制作流程」的步骤，依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/David_Hilbert/metadata.json` 及 `page.md`
- 输出以下信息供我校验：
  - 生卒日期 (1862-01-23 ~ 1943-02-14，享年 81 岁)
  - 国籍变迁 (普鲁士→德意志帝国→魏玛共和国→纳粹德国)
  - 博士导师 (Ferdinand von Lindemann)、博士论文 (1885, 不变量理论)
  - 主要任职机构 (Königsberg 1886–1895 → Göttingen 1895–1943)
  - 关键荣誉 (Lobachevsky, Bolyai, Pour le Mérite, ForMemRS 等)
  - 知名学生 (Weyl, Courant, Dehn, Zermelo, von Neumann, Noether 等 69 位)
  - Wikipedia 正文中提取出的 **关键时间线**（按年份列出 15–20 个关键节点）
  - 核心贡献清单（见下方第 4 步）

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `hilbert/` 子目录
- 创建 `hilbert/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `hilbert/Makefile`
- 将 `MAIN` 变量改为 `David_Hilbert_zh`
- 将 `VIDEO_NAME` 变量改为 `David_Hilbert_zh`

---

## 第 3 步：收集图片

- 从 `pages/David_Hilbert/images.txt` 中选出 4–6 张高质量图片
- 优先级：**portrait (1912 年经典照)** > Göttingen 数学研究所 > 与 Minkowski 合影 > 墓碑/纪念物
- 下载到 `hilbert/images/`，统一命名为 `portrait.jpg`、`goettingen.jpg` 等

---

## 第 4 步：建立时间线和叙事骨架

希尔伯特的一生可以按"学术迁移"和"数学方向转变"两条线划分：

### 生平阶段

1. **Königsberg 时期 (1862–1895)**：出生、求学、博士 (1885)、Privatdozent、与 Minkowski & Hurwitz 的友谊
2. **Göttingen 黄金时代 (1895–1920)**：接替 Klein，打造世界数学中心，23 问题 (1900)
3. **晚年与纳粹阴影 (1920–1943)**：Hilbert 纲领，Gödel 不完备定理的冲击，纳粹清洗 Göttingen 数学系，81 岁离世

### 核心数学贡献（按领域排列）

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 不变量理论 | Hilbert 基定理 (Basis Theorem), Nullstellensatz | 1888–1893 |
| 代数数论 | Zahlbericht（数论报告），类域论的先驱 | 1897 |
| 几何基础 | Hilbert 公理体系，欧氏几何的严格公理化 | 1899 |
| 变分法与 PDE | Dirichlet 原理的复兴，Hilbert 空间的前身 | 1900–1910 |
| 23 问题 | 1900 年巴黎 ICM 演讲，为 20 世纪数学指明方向 | 1900 |
| 积分方程 → Hilbert 空间 | 谱理论，算子理论，泛函分析的诞生 | 1904–1912 |
| 数学物理 | Einstein–Hilbert 作用量，广义相对论 | 1915 |
| 数学基础 | Hilbert 纲领，证明论，形式系统 | 1920–1931 |
| 数理逻辑 | ε 演算，与 Gödel 的对话 | 1920s |

### 人物关系（这是希尔伯特的叙事核心）

- **Minkowski** — 终身挚友，Königsberg 时期的三人组（+ Hurwitz）
- **Klein** — 将 Hilbert 引入 Göttingen，共同打造数学帝国
- **69 位博士生** — Weyl, Courant, Dehn, Zermelo, von Neumann, Noether …
- **Gödel** — 不完备定理击碎了 Hilbert 纲领，但 Hilbert 以尊严接受
- **纳粹** — 1933 年数学系被清洗，Hilbert 目睹一生心血流逝

---

## 第 5 步：设计配色方案

- 希尔伯特的气质关键词：**王者、权威、乐观、德国学术传统的巅峰**
- **建议配色：深普鲁士蓝 + 金色**（普鲁士王国的荣耀 + Göttingen 学术黄金时代）
- 请给出完整的 `\definecolor` 方案：
  - 主色 (coverprimary)：**普鲁士蓝** (深蓝，象征王者与权威)
  - 强调色 (coveraccent)：**金色**（Göttingen 黄金时代 + 23 问题的灯塔）
  - 四个分类色，对应希尔伯特的四大支柱：
    - **badgealgebra** (代数/不变量) — 深藏青
    - **badgeaxiom** (几何/公理) — 墨绿
    - **badgeanalysis** (分析/Hilbert 空间) — 暖铜
    - **badgelogic** (逻辑/基础) — 紫罗兰
  - 各面板色 (purplepanel/amberpanel/greenpanel/bluepanel/goldpanel/graypanel)

---

## 第 6 步：规划幻灯片序列

希尔伯特内容极丰富，建议 20 页（比黎曼多 2 页，因为他有 23 问题、Hilbert 纲领、纳粹三条独特叙事线）：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 人物篇 ===
01  封面 — 《希尔伯特：数学之王》 / David Hilbert 1862–1943 + 四色badge
02  为什么希尔伯特是最后一个数学全才 — 从代数到逻辑，没有他未触碰的领域

=== 生平线 ===
03  Königsberg 岁月 (1862–1895) — 与 Minkowski 的终身友谊，博士 (1885)
04  Göttingen 黄金时代 (1895–1943) — Klein 的召唤，打造世界数学中心
05  数学家之王 — 69 位博士生，Weyl/Courant/von Neumann/Noether，一代宗师

=== 代数革命 ===
06  不变量理论 — Hilbert 基定理 (1888)，用存在性证明终结了计算时代
07  代数数论 — Zahlbericht (1897)，类域论的序曲

=== 几何与分析 ===
08  几何基础 (1899) — 公理化欧氏几何，用"桌子、椅子、啤酒杯"替代点线面
09  Hilbert 空间 — 从积分方程到泛函分析的诞生，量子力学的数学语言

=== 最高光的时刻 ===
10  23 问题 (1900) — 巴黎 ICM 演讲，为整个 20 世纪数学绘制地图
11  23 问题现状 — 已解决/部分解决/仍悬未决的概览

=== 数学物理 ===
12  与爱因斯坦的赛跑 — Einstein–Hilbert 作用量 (1915)，广义相对论的协变形式

=== 数学基础的战场 ===
13  Hilbert 纲领 — "Wir müssen wissen — wir werden wissen"（我们必须知道，我们必将知道）
14  Gödel 不完备定理 (1931) — 击碎了纲领，但 Hilbert 以尊严接受

=== 终章 ===
15  Göttingen 的黄昏 (1933) — 纳粹清洗，Hilbert 目睹一生的心血被摧毁
16  "数学没有种族" — Hilbert 对纳粹的沉默抵抗，Emmy Noether 的驱逐
17  最后的岁月 (1933–1943) — 81 岁离世，墓碑上刻着"Wir müssen wissen…"

=== 结尾 ===
18  升起海水 — Hilbert 不只是一个人，他是一个时代的标志
19  结束页
```

> **可以微调。** 以上只是一个建议序列，你觉得哪页多余、哪页缺了就调整。征求我的意见后再开始写代码。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/hilbert/David_Hilbert_zh.tex`
- 完全参照 `grothendieck/Alexander_Grothendieck_zh.tex` 或 `riemann/Bernhard_Riemann_zh.tex` 的代码结构
- 每页用 `\newcommand{\xxxslide}{% ... }` 定义

### 关键要求

- **每写完一页立即编译 (`make clean && make`)，不等待全部写完**
- 编译失败立即修复，不要跳过
- 中文正文，英文术语和公式保留原文
- 希尔伯特的内容密度极高，每页文字量需要严格控制，必要时拆分为多页

---

## 第 8 步：布局检查 ★★★ 最重要

> **这是从黎曼实战中学到的最大教训：必须在写代码时同步检查溢出和重叠，不能等全部写完再看。**

### 每写完一页的执行流程

```
1. make clean && make          # 编译
2. 查看 PDF                    # 肉眼检查
3. 如有溢出/重叠 → 立即修复    # 按指南 §6.2 优先级
```

### 自我截图 + OCR 观察法

当肉眼难以判断是否溢出时：

```bash
# 生成当前页的高清截图
pdftoppm -png -r 300 -f N -l N output/David_Hilbert_zh.pdf output/check

# 观察截图：
# - 底部文字是否被 \plainbar 切断？
# - 两个相邻面板是否重叠？
# - 标题区是否压到了第一个面板？
# - 金色金句面板是否跑出了页面底部？
```

### 溢出修复优先级（指南 §6.2 统一策略）

| 优先级 | 手段 | 何时用 |
|:--:|------|------|
| 1 | 删 `\plainbar` 或缩减 | 最先尝试，对信息无损 |
| 2 | 缩 `inner sep` (9→5→3pt) | 面板内容刚好超出一点 |
| 3 | 缩字号 | 多行文字导致溢出 |
| 4 | 减行间距 (`\\[2pt]`→`\\[1pt]`) | 压缩面板内部空白 |
| 5 | 调 y 坐标 | **最后手段**，容易打破视觉平衡 |

---

## 第 9 步：史实审查 + 术语审查

> **不要在写第一版时就给自己加太重的史实负担。** 第一版的目标是快速出成品，史实精修是后面的事。

### 希尔伯特的特殊史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 希尔伯特特有的高危点 |
|---------|---------------------|
| **"最后一个数学全才"** | ★ page.md 从未称 Hilbert 为 "最后一个全才"、"百科全书式数学家"、"The Last Universalist"。page.md 称他为 "one of the most influential mathematicians of all time"。不要编造 "全才"、"百科全书式" 标签。Hilbert 的核心叙事是 "议程制定者"，不是 "全才"。 |
| **Hilbert 纲领** | Gödel 不完备定理"击碎"了纲领，但不是完全否定。Hilbert 之后的证明论（Gentzen, Kreisel）仍在发展。措辞要准确。 |
| **Einstein–Hilbert 作用量** | 有史学争议：Hilbert 和 Einstein 谁先推导出场方程？不要声称"Hilbert 先于 Einstein"。写"几乎同时独立推导"即可。 |
| **23 问题** | 问题 1 (CH)、问题 2 (一致性)、问题 6 (公理化物理)、问题 8 (RH) 仍未解决。不要给人"大部分已解决"的印象。 |
| **纳粹清洗** | 1933 年大批犹太裔数学家被驱逐，包括 Emmy Noether, Richard Courant, Max Born 等。Rust 宴会逸闻 page.md 有直接记载："About a year after the purge, Hilbert attended a banquet…"。Hilbert 回答："Suffered? It doesn't exist any longer, does it?" 直接用原文即可。 |
| **墓碑铭文** | "Wir müssen wissen. Wir werden wissen." — 1930 年 Königsberg 演讲的结尾。这是他的墓志铭，但注意：这两句是在 Gödel 不完备定理发表 (1931) **之前**说的。 |
| **博士导师** | Lindemann (π 超越性的证明者)，但 Lindemann 不是代数几何/不变量理论专家。Hilbert 的博士论文方向主要靠自学。 |
| **Heidelberg 短暂求学** | ★ metadata 列出 "Heidelberg University" 在 educated_at 中，但 page.md 正文未描述。Beamer 提及时需克制，不要添油加醋。 |
| **Hilbert 空间相关人物** | ★ Slide 9 中 "Schmidt, Fréchet, Riesz" — 只有 Schmidt 作为博士生出现在 page.md。Fréchet 和 Riesz 不在 page.md 中。Banach 在 page.md 中（"Banach amplified the concept"）。可保留 Schmidt 和 Banach，其他删去。 |

### 通用陷阱（参照指南第十四节）

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个"断言 | 避免"第一个严格公理化欧氏几何"（Pasch 已有公理化尝试）→ "给出了最完整、最有影响力的公理化体系" |
| 伪引语 | 中文引号内的"Hilbert 原话"必须有德文或英文原文对应。不确定 → 用间接引语 |
| 人物时间线 | "后来被 Gödel 发展" — Gödel 比 Hilbert 晚，措辞正确 |
| 伪精确数字 | "69 位博士生" 这个数字有据可查 (Mathematics Genealogy Project)，可以用 |
| 现代术语包装 | Hilbert 不知道"泛函分析"这个词 — 用"Hilbert 空间理论为后来泛函分析奠基" |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Hilbert's basis theorem | Hilbert 基定理 | ≠ 泛函分析中的"基" |
| Hilbert's Nullstellensatz | Hilbert 零点定理 | Nullstelle = 零点，不译成"空集定理" |
| Zahlbericht | 数论报告 | 保留德文原名 + 中文翻译 |
| Hilbert space | Hilbert 空间 | — |
| Hilbert's program | Hilbert 纲领 | 不译成"Hilbert 计划" |
| Entscheidungsproblem | 判定问题 | 保留德文原名 |
| Einstein–Hilbert action | Einstein–Hilbert 作用量 | 两人并列，不分先后 |
| Wir müssen wissen… | 我们必须知道，我们必将知道 | 保留德文原文 |

---

## 第 10 步：第二轮布局微调

全部页面写完后：

- 从头到尾翻看 PDF，逐页标记溢出/重叠
- 对标记页按 §8 优先级处理
- 确保每页间距均匀（参照指南 §14.13 面板间距均匀化）
- 封面肖像在右上角（参照 Grothendieck/Riemann 模板）
- 结束页不要放肖像（只放主题句 + 生卒年份）

---

## 第 11 步：插入 OpenMath 项目首页

- ★ **使用统一 cover 模板**：从 `../cover/OpenMath_Cover.tex` 复制 `\openmathslide` 命令定义（或直接 `\input`）
- 在 `\begin{document}` 后调用 `\openmathslide`，然后调用希尔伯特的封面 `\titleslide`

---

## 第 12 步：最终编译

- 确认 `make clean && make` 无错误
- 确认 PDF 输出正常，总页数在 19–21 页之间
- 从头到尾翻看确认无误
- 准备接受外审（找熟悉希尔伯特的人挑错）

---

## 第 13 步：音乐选择

参照指南 §15.7：

- 希尔伯特的气质：**王者、权威、德国学术传统的巅峰、20 世纪的领航人**
- **推荐：Heroic / 史诗风格**（类似 Grothendieck，但更注重"庄严"而非"革命"）
- 从 `/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/curated_tracks.md` 中查询具体曲目

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/数学家立传工作指南.md` | 完整操作手册 (§16 快速启动清单) |
| `mathematician/pages/David_Hilbert/page.md` | Hilbert Wikipedia 正文 (97K chars) |
| `mathematician/pages/David_Hilbert/metadata.json` | Hilbert Wikidata 元数据 |
| `mathematician/pages/David_Hilbert/images.txt` | 20 张图片 URL |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码（教皇模板） |
| `mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` | Riemann 完整源码（克制天才模板） |
| `mathematician/presentations/riemann/Makefile` | 构建脚本（直接复制） |

---

> **开始执行。每完成一步向我汇报。**
> 
> **最重要的事：每写一页就 make，看到溢出就修，不要攒到最后一起修。** 希尔伯特内容极多，溢出风险比黎曼更高。
