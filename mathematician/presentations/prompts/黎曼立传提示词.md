# 黎曼 (Bernhard Riemann) 立传提示词

> 本提示词严格遵循 [数学家立传工作指南.md](./数学家立传工作指南.md)，以 Grothendieck 成品为参考模板，为黎曼制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Bernhard Riemann (1826–1866)
- **Wikipedia 页面已下载**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Bernhard_Riemann/`
  - `page.md` — 正文 Markdown
  - `metadata.json` — Wikidata 元数据
  - `images.txt` — 图片 URL 清单
- **参考模板**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/`
  - `Alexander_Grothendieck_zh.tex` — 完整 Beamer 源码（约 712 行，可逐页参考结构和样式）
  - `Makefile` — 构建脚本（直接复制即可，仅改 `MAIN` 变量）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/数学家立传工作指南.md`

---

## 你的任务

按照 [数学家立传工作指南.md](./数学家立传工作指南.md) 第十一节「推荐制作流程」的 13 个步骤，依次完成。每个步骤完成后向我汇报进度，遇到歧义时先征求我的意见再继续。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Bernhard_Riemann/page.md` 及 `metadata.json`
- 输出以下信息供我校验：
  - 生卒日期、国籍、研究领域
  - 博士导师、主要任职机构
  - 关键荣誉（如有）
  - Wikipedia 正文中提取出的 **关键时间线**（按年份列出 10–15 个关键节点）

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `riemann/` 子目录
- 创建 `riemann/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `riemann/Makefile`
- 将 `MAIN` 变量改为 `Bernhard_Riemann_zh`
- 将 `VIDEO_NAME` 变量改为 `Bernhard_Riemann_zh`

---

## 第 3 步：收集图片

- 从 `pages/Bernhard_Riemann/images.txt` 中选出 4–6 张高质量图片
- 优先选择：portrait（肖像）、出生地/故居、手稿、纪念物、墓碑等
- 下载到 `riemann/images/`，统一命名为 `portrait.jpg`、`manuscript.jpg` 等

---

## 第 4 步：建立时间线和叙事骨架

- 基于 Wikipedia 正文，划分黎曼生平为以下阶段（可微调）：
  1. **童年与求学** (1826–1846)：Breselenz 出生，Lüneburg 中学，Göttingen 大学
  2. **柏林与 Göttingen 深造** (1847–1851)：师从 Dirichlet、Eisenstein、Jacobi；博士论文 (1851)
  3. **Habilitation 与就职演讲** (1852–1854)："论作为几何基础的假设"（即黎曼几何的诞生）
  4. **Göttingen 任教时期** (1854–1859)：1857 年副教授，1859 年接替 Dirichlet 任正教授
  5. **晚年与遗产** (1859–1866)：1862 年健康状况恶化（肺结核），多次赴意大利疗养，1866 年病逝于 Selasca（39 岁）
- 列出 **每个阶段的核心数学贡献**：
  - 黎曼积分 (Riemann integral)
  - 柯西-黎曼方程 (Cauchy–Riemann equations)
  - 黎曼面 (Riemann surface)
  - 黎曼映射定理 (Riemann mapping theorem)
  - 黎曼几何 (Riemannian geometry) / 黎曼度量
  - 黎曼ζ函数 (Riemann zeta function) / 黎曼猜想 (Riemann hypothesis)
  - 黎曼-罗赫定理 (Riemann–Roch theorem)
  - 阿贝尔函数理论 (theory of Abelian functions)

---

## 第 5 步：设计配色方案

- 黎曼的气质关键词：**深邃、神秘、优雅、悲剧性早逝**
- 指南建议：**墨绿 + 银灰**
- 请给出完整的 `\definecolor` 方案，包括：
  - 主色 (coverprimary)、强调色 (coveraccent)
  - 四个概念分类色（根据该数学家的核心领域命名，如黎曼的 badgenumber/badgegeo/badgeanaly/badgecomplex）
  - 各面板色 (purplepanel/amberpanel/greenpanel/bluepanel/goldpanel/graypanel)
- 四个分类色建议对应：数论 (ζ函数)、几何 (黎曼几何)、分析 (积分/面)、复分析 (映射定理)

---

## 第 6 步：规划幻灯片序列

为黎曼规划以下页面序列（约 18 页）：

```
00  OpenMath 项目首页（从 grothendieck 的 tex 中直接复用 \openmathslide 命令）

=== 人物篇 ===
01  封面 — 《黎曼：猜想永恒》/ Bernhard Riemann 1826–1866 + 四色badge
02  为什么黎曼如此重要 — 39年/十余篇奠基性工作/四个领域

=== 生平线 ===
03  童年与求学 (1826–1846) — Breselenz → Lüneburg → Göttingen
04  Göttingen → 柏林 → 博士 (1847–1851)

=== 数学革命 ===
05  黎曼积分 — 教授资格论文，可积性条件
06  黎曼面 — 多值函数的几何化
07  黎曼映射定理 — 复分析的几何革命（标题不标年份！）
08  就职演讲 (1854) — Habilitation，n维内蕴几何
09  黎曼几何 — 度量张量，广义相对论数学语言

=== 最深远的贡献 ===
10  黎曼ζ函数 — 仅约9页，奠定解析数论
11  黎曼猜想 — 大量低位零点已验证，但有限计算≠证明
12  黎曼-罗赫定理 (1857/1865) — 代数曲线基石
13  阿贝尔函数理论 — 继承Abel/Jacobi，为Jacobian簇奠定基础

=== 人物终章 ===
14  Göttingen 教授 (1857–1866) — 继承Dirichlet教席
15  病痛与早逝 (1862–1866) — 多次意大利疗养，39岁离世
16  永恒的猜想 — 160年后，进展与悬而未决

=== 结尾 ===
17  升起海水 — 把数变成函数，把函数变成空间，把空间变成几何
18  猜想永恒（结束页 — 不要在此页放肖像！肖像在01页右上角）
```

> **历史教训**：以上序列是最终成品。实际制作中，有些页面的标题/内容可能在第一版中使用了不准确的表述（如"1851"标注、"第一次严格定义"），这些会在史实审查阶段修正。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/Bernhard_Riemann_zh.tex`
- 完全参照 `grothendieck/Alexander_Grothendieck_zh.tex` 的代码结构：
  - 相同的前导区（`\documentclass`、字体、包、配色、辅助命令）
  - 相同的 `\sectiontitle`、`\plainbar`、`\deckbackground` 格式
  - 替换为你为黎曼设计的配色方案
  - 每页用 `\newcommand{\xxxslide}{% ... }` 定义
- **关键要求**：
  - 每页编写完立即编译验证 (`make`)，不等待全部写完
  - 编译失败立即修复，不要跳过
  - 中文正文，英文术语和公式保留原文

---

## 第 8–9 步：史实审查 + 术语审查

完成后逐页自查，但**不要在写第一版时就给自己加太重的史实负担。** 第一版的目标是快速出成品，史实精修是后面的事。

### 第一轮自检（写完后即刻执行）

对照指南第十四节的进阶陷阱，逐页扫描：

| 陷阱类型 | 检查点 | 黎曼案例参考 |
|---------|--------|------------|
| 论文计数 | 是否用了精确数字（"10篇"）？ | → 改为"十余篇奠基性工作" |
| "第一"断言 | 是否声称"第一次/第一个"？ | → 改为"核心贡献""里程碑式" |
| 标题年份 | 标题中是否有无法确认的年份？ | → 如"黎曼映射定理 (1851)"应去掉1851 |
| 机构术语 | 德国大学制度(Habilitation等)是否正确？ | → 查原文术语 |
| 伪引语 | 中文引号内是否声称是数学家原话？ | → 有原文才用引号，否则用间接引语 |
| 人物时间线 | "后来被X发展"—X的生卒年是否晚于该数学家？ | → Abel比黎曼早，不能写"后来" |
| 过度简化 | 是否把复杂理论写成了等式？ | → "素分布=ζ零点"太绝对 |
| 伪精确数字 | 是否写了具体计算验证数字？ | → 不写$10^{13}$，用"大量低位零点" |
| 现代术语包装 | 是否用21世纪术语描述19世纪数学家？ | → 加"今天我们称之为…" |
| 传记轶事 | 是否把轶事当确定史实？ | → 加"据传"或改用间接叙述 |
| 母亲去世时间 | 是否暗示童年丧母？ | ★ page.md 明确：母亲 1846 年去世，黎曼时年 19 岁，非"早逝" |
| Schmalfuss / 中学轶闻 | 是否出现校长名字或伪造引语？ | ★ page.md 未提 "Schmalfuss"（仅在外部传记中出现）；黎曼中学轶闻不要在无可靠来源时使用引号 |
| Moritz Stern 身份 | 是否出现"第一位犹太裔正教授"？ | ★ page.md 仅列出 Moritz A. Stern 为 Other academic advisors，犹太裔细节不在 page.md |
| 1857 副教授 | 是否写成"1857 年被任命为副教授"？ | ★ **这是致命错误！** page.md 明确写 "attempt failed"——晋升未通过，仅获得固定薪水 |
| Gauss 对就职演讲的反应 | 是否写"Gauss 激动不已/高度评价"？ | ★ page.md 明确写 "Its early reception appears to have been slow"(反响缓慢)，与此矛盾 |
| 胸膜炎 | 是否出现"染上胸膜炎"？ | ★ page.md 仅写 tuberculosis，未提及 pleurisy |
| Dedekind 整理出版 | 是否写 Riemann 积分论文由 Dedekind 出版？ | ★ Dedekind 出版的是几何演讲 (1868)；Fourier 级数论文发表于 1867 年 Abhandlungen |
| 博士论文引语 | 是否伪造了 Gauss 对博士论文的赞美引语？ | ★ page.md 无 Gauss 对博士论文的直接引语评价 |

### 第二轮外审（给数学史背景的人看）

外审关注的不再是"事实错"，而是"专业上站不稳"。常见反馈：
- 引号问题（最严重）→ 坚决改
- 宣传化措辞（"每一篇都改变了数学"）→ 改为纪录片化的稳当表述
- 历史意识（现代语言包装古代数学家）→ 加"为后来…奠定基础"

### 术语清单（对照指南第五章）

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Riemann hypothesis | 黎曼猜想 | 不译成"黎曼假设" |
| Riemann zeta function | 黎曼ζ函数 | ζ 保留希腊字母 |
| Riemann surface | 黎曼面 | — |
| Riemann integral | 黎曼积分 | — |
| Riemannian geometry | 黎曼几何 | Riemannian ≠ Riemann |
| Riemann–Roch theorem | 黎曼-罗赫定理 | 不翻成"黎曼-洛赫" |
| conformal mapping | 共形映射 | — |
| Abelian functions | 阿贝尔函数 | — |
| meromorphic | 亚纯 | — |
| Habilitation | 教授资格演讲 | 不译成"就职演讲" |
| Privatdozent | 编外讲师 | 德国特有职称 |
| pseudo-Riemannian | 拟黎曼 | 注意与正定黎曼几何的区分 |

### 音乐选择

参照指南 §15.7，根据数学家气质选择 BGM：
- 革命者/教皇气质 → Heroic/宏大
- **克制天才/悲剧早逝/猜想悬而未决 → Timeless/沉稳纪录片风**
- 判断标准：不是所有人都需要 epic 风格
---

## 第 10 步：布局微调

- 逐页检查是否有底部溢出，按指南第六章 6.2 优先级处理
- 检查序号圆圈是否与文字重叠
- 每页间距是否均匀

---

## 第 11 步：插入 OpenMath 项目首页

- 从 `grothendieck/Alexander_Grothendieck_zh.tex` 中复制 `\openmathslide` 命令定义
- 在 `\begin{document}` 后调用 `\openmathslide`，然后再调用黎曼的封面 `\titleslide`

---

## 第 12 步：最终编译

- 确认 `make` 无错误，PDF 输出正常
- 确认总页数在 18–20 页之间

---

## 关键参考文件清单

在执行上述步骤时，请随时参考以下文件获取细节：

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/数学家立传工作指南.md` | 完整操作手册 |
| `mathematician/pages/Bernhard_Riemann/page.md` | 黎曼 Wikipedia 正文 |
| `mathematician/pages/Bernhard_Riemann/metadata.json` | 黎曼 Wikidata 元数据 |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码（模板）|
| `mathematician/presentations/grothendieck/Makefile` | 构建脚本（直接复制）|

---

> 开始执行。每完成一步向我汇报。
