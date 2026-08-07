# 塞尔 (Jean-Pierre Serre) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Grothendieck、Riemann 和 Hilbert 成品为参考模板，为塞尔制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Jean-Pierre Serre (1926–至今)
- **气质关键词**: **优雅、简洁、博学、跨领域大师、活着的传奇** — 史上最年轻的菲尔兹奖得主（27岁），第一位阿贝尔奖得主，法国数学的"风格之神"
- **Wikipedia 页面已下载**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Jean-Pierre_Serre/`
  - `page.md` — 正文 Markdown
  - `metadata.json` — Wikidata 元数据
  - `images.txt` — 图片 URL 清单
- **参考模板**:
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` — Grothendieck 完整源码（教皇气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` — Riemann 完整源码（克制天才气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/hilbert/David_Hilbert_zh.tex` — Hilbert 完整源码（王者气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Makefile` — 构建脚本（直接复制）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 你的任务

按照 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md) 第十一节「推荐制作流程」的步骤，依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Jean-Pierre_Serre/metadata.json` 及 `page.md`
- 输出以下信息供我校验：
  - 出生日期 (1926-09-15)、国籍 (法国)
  - 博士导师 (Henri Cartan)、博士论文 (1951，代数拓扑)
  - 主要任职机构 (CNRS 1948–1954, Collège de France 1956–1994)
  - 关键荣誉 (Fields Medal 1954, Wolf Prize 2000, Abel Prize 2003 — 史上第一位)
  - 知名合作者/学生 (与 Grothendieck 合作, Borel, Tate; 学生包括 Jean-Marc Fontaine 等)
  - Bourbaki 成员身份
  - Wikipedia 正文中提取出的 **关键时间线**（按年份列出 15–20 个关键节点）
  - **人格特质线索**：关于他写作风格、教学方式、数学哲学的描述

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `serre/` 子目录
- 创建 `serre/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `serre/Makefile`
- 将 `MAIN` 变量改为 `Jean_Pierre_Serre_zh`
- 将 `VIDEO_NAME` 变量改为 `Jean_Pierre_Serre_zh`

---

## 第 3 步：收集图片

- 从 `pages/Jean-Pierre_Serre/images.txt` 中选出 4–6 张高质量图片
- 优先选择：**不同年代的肖像**（1954 年 Fields Medal 获奖照、盛年教学照、晚年照）> Collège de France 外景 > Bourbaki 合影 > 手稿或黑板板书
- 下载到 `serre/images/`，统一命名为 `portrait.jpg`、`college_france.jpg` 等
- ★ **特殊要求**：Serre 仍在世且百岁高龄，应优先选择展现他"优雅从容"气质的照片，避免暮年病态照

---

## 第 4 步：建立时间线和叙事骨架

塞尔的一生可以按"学术迁徙"和"数学方向转变"两条线划分。与之前所有数学家不同的是——**他还活着**。因此叙事终点不是"遗产"，而是"活着的传奇"。

### 生平阶段

1. **早年与天才崛起 (1926–1954)**：Bages 出生、Nîmes 中学、巴黎高师 (ENS)、博士论文 (1951)、Fields Medal (1954，年仅 27 岁)
2. **黄金时代：跨领域征服 (1954–1980)**：CNRS → Collège de France 教授、Bourbaki 活跃期、与 Grothendieck 合作、FAC/GAGA/Serre duality、Galois 表示
3. **大师风范 (1980–至今)**：荣誉等身（Wolf/Abel/Balzan）、继续发表深刻工作（Serre modularity conjecture）、百岁诞辰、在世传奇

### 核心数学贡献（按领域排列）

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 代数拓扑 | Serre 谱序列、同伦群计算、C-理论 | 1950–1953 |
| 代数几何 | FAC (1955)、GAGA (1956)、Serre 对偶 | 1955–1958 |
| 交换代数 | Serre 重数猜想、正则局部环的同调刻画 | 1950s–1960s |
| 数论 | Galois 表示、Serre 猜想 (现已成定理)、模形式 | 1960s–至今 |
| 群论 | 有限群的线性表示、树 (Trees) / Bass–Serre 理论 | 1970s |
| l-adic 上同调 | 与 Grothendieck 共同发展的核心工具 | 1960s |
| 模性猜想 | Serre 猜想 (2008 年由 Khare–Wintenberger 证明) | 1975–2008 |

### ★ 塞尔独有的叙事线索

1. **风格之神** — 他的写作以"极致简洁、不可再删一字"著称。"Serre 写五页等于别人写五十页。"
2. **跨领域的桥梁** — 他是极少数在拓扑、几何、代数、数论、群论五个领域都留下核心定理的人
3. **Bourbaki 的良心** — 作为 Bourbaki 核心成员，但始终保持独立思考
4. **Grothendieck 的合作者** — FAC 为 Grothendieck 的概形理论铺路，两人在 1960 年代密切合作
5. **菲尔兹奖最年轻得主** — 27 岁获奖，至今仍是纪录（独自获奖者中的最年轻纪录）
6. **活着的传奇** — 2026 年百岁诞辰，仍在世界数学界享有至高威望

### 人物关系（塞尔叙事的"锚点"）

- **Henri Cartan** — 博士导师，代数拓扑的引路人
- **Bourbaki** — 核心成员，数学结构的统一哲学
- **Grothendieck** — 合作者与对话者，FAC → 概形，"Serre 铺路，Grothendieck 建造"
- **Borel, Tate** — 长期合作者
- **Deligne** — 学术后代，继承并发扬光大

---

## 第 5 步：设计配色方案

- 塞尔的气质关键词：**优雅、节制、经典、法国式的知性光辉**
- **建议配色：勃艮第酒红 + 象牙暖金 + 石板灰**（法式优雅、Collège de France 古典廊柱色调）
- 请给出完整的 `\definecolor` 方案：
  - 主色 (coverprimary)：**勃艮第红** (深沉典雅，象征古典法国学术传统)
  - 强调色 (coveraccent)：**象牙暖金**（Abel 奖的金色光辉 + 百岁传奇的温润）
  - 四个分类色，对应塞尔的四大支柱领域：
    - **badgetopology** (拓扑) — 靛蓝
    - **badgealgebra** (代数/几何) — 勃艮第红 (与主色呼应)
    - **badgenumber** (数论) — 深松绿
    - **badgerep** (表示论/群论) — 暖铜
  - 各面板色 (purplepanel/amberpanel/greenpanel/bluepanel/goldpanel/graypanel)

---

## 第 6 步：规划幻灯片序列

塞尔内容极其丰富，但考虑到他**仍在世**，叙事需要与已故数学家不同——结尾不是"遗产"，而是"仍在书写的传奇"。建议 20 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 人物篇 ===
01  封面 — 《塞尔：风格即数学》 / Jean-Pierre Serre 1926– + 四色badge
02  为什么塞尔是不可替代的 — 五个领域/菲尔兹最年轻得主/第一位阿贝尔奖得主

=== 天才之路 ===
03  早年岁月 (1926–1951) — Bages → Nîmes → ENS → Henri Cartan 门下博士
04  27岁的菲尔兹奖 (1954) — 谱序列、同伦群、C-理论，代数拓扑的革命

=== 代数几何革命 ===
05  FAC (1955) — 凝聚层论文，为 Grothendieck 的概形理论奠定语言基础
06  GAGA (1956) — 代数几何与解析几何的桥梁，两套世界观的统一
07  Serre 对偶 — 代数几何中最优美的对偶定理之一

=== 数论与表示论 ===
08  Galois 表示 — 将数论问题转化为线性代数问题，开启了现代数论的新范式
09  Serre 猜想 — 1975 年提出，2008 年由 Khare–Wintenberger 证明
10  模形式之旅 — Serre 如何将模形式与 Galois 表示深刻联系在一起

=== 群论与组合 ===
11  Trees — Bass–Serre 理论，群在树上的作用，几何群论的开山之作
12  有限群的线性表示 — Serre 的教科书，几代数学家的入门圣经

=== 塞尔的方法论 ===
13  风格即数学 — Serre 的写作哲学："删到不能再删为止"
14  跨领域的大师 — 拓扑→几何→数论→群论→表示论，没有他未架起的桥梁

=== 人物风貌 ===
15  Bourbaki 岁月 — "数学结构"的统一哲学，集体创作中的独立思考
16  与 Grothendieck 的对话 — FAC → SGA，两位巨人的相互塑造

=== 活着的传奇 ===
17  荣誉等身 — Fields (1954), Balzan (1985), Steele (1995), Wolf (2000), Abel (2003)
18  百岁诞辰 (1926–2026) — 一个世纪的数学旅程，仍在继续

=== 结尾 ===
19  思想回响 — 塞尔教会我们：数学的深刻，可以用最少的语言表达
20  结束页 — 不要放肖像！肖像在01页右上角。主题句：优雅永不过时。
```

> **可以微调。** 以上只是一个建议序列。塞尔在世这一点让叙事策略不同于之前的每位数学家——"百岁诞辰"一页是独有的。征求我的意见后再开始写代码。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/serre/Jean_Pierre_Serre_zh.tex`
- 完全参照 `grothendieck/Alexander_Grothendieck_zh.tex` 或 `riemann/Bernhard_Riemann_zh.tex` 或 `hilbert/David_Hilbert_zh.tex` 的代码结构
- 每页用 `\newcommand{\xxxslide}{% ... }` 定义

### 关键要求

- **每写完一页立即编译 (`make clean && make`)，不等待全部写完**
- 编译失败立即修复，不要跳过
- 中文正文，英文术语和公式保留原文
- 塞尔的内容密度极高（每个定理背后都是整个领域），每页文字量需要严格控制

---

## 第 8 步：布局检查 ★★★ 最重要

> **这是从之前实战中学到的最大教训：必须在写代码时同步检查溢出和重叠，不能等全部写完再看。**

### 每写完一页的执行流程

```
1. make clean && make          # 编译
2. 查看 PDF                    # 肉眼检查
3. 如有溢出/重叠 → 立即修复    # 按指南 §6.2 优先级
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

### 塞尔特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 塞尔特有的高危点 |
|---------|---------------------|
| **菲尔兹奖最年轻得主** | Serre 27 岁 (1954) 是最年轻纪录。注意措辞："独自获奖者中的最年轻纪录"（因为 2022 年有四人共享，其中可能有人更年轻？不，当前 Serre 仍是最年轻的 Fields 奖得主，直到 2022 年也没有人打破。需核实）|
| **第一位 Abel 奖得主** | 2003 年首届 Abel 奖。准确说是"首位阿贝尔奖获奖者"。不要写成"唯一"。 |
| **Bourbaki 成员身份** | 不要过度强调 Bourbaki 的"集体性"而抹杀 Serre 的独立思考。他本人曾表示并非所有 Bourbaki 的决定都赞同。 |
| **Grothendieck 的合作** | FAC 是 Grothendieck 概形理论的先导，但不要写成"Serre 为 Grothendieck 工作"。两人是平等的合作者。 |
| **仍在世** | 这是最大的不同！所有关于"遗产""留给后人"的措辞需要调整。他仍在世且百岁高龄。不要用"他的一生"（过去式），改用"在他的百年数学旅程中"。 |
| **风格即数学 / 删到不能再删** | ★ page.md 未使用 "风格即数学" 或 "删到不能再删为止" 描述 Serre。他确以简洁著称，但标签语需克制，不要编造 "名言"。 |
| **Serre 写五页等于别人写五十页** | ★ 这是一个流传甚广的轶闻，但不在 page.md 正文中。如需引用，标注"据说"或删去。 |
| **Lycée Louis-le-Grand** | ★ page.md 只提及 "Lycée de Nîmes"（尼姆中学），未提 Louis-le-Grand。预科教育只说 "Classe préparatoire"，不要指定具体学校。 |
| **Dieudonné / Bourbaki 内部细节** | ★ page.md "See also" 仅一句 "Serre joined it in the late 1940s"。Dieudonné 回忆、"最简洁的反驳" 等细节不在 page.md 中。Bourbaki 页面保持克制。 |
| **Serre 猜想 (模性)** | 1975 年提出，2008 年由 Khare–Wintenberger 证明。不要写成"Serre 证明了 Serre 猜想"。 |
| **Serre 猜想 (多项式环上的投射模)** | 这是另一个 Serre 猜想 (1955)，1976 年由 Quillen 和 Suslin 独立证明（现称 Quillen–Suslin 定理）。注意区分两个不同的"Serre 猜想"。 |
| **Serre 重数猜想** | 与交换代数中的 intersection multiplicities 相关，部分仍未解决。不要写成"已证明"。 |

### 通用陷阱（参照指南第十四、十五节）

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个"断言 | 避免"第一个将拓扑方法引入数论"（实际上在 Serre 之前已有先例）→ "以最深刻和系统的方式将拓扑与数论融合" |
| 伪引语 | 中文引号内的"Serre 原话"必须能追溯法文或英文原文。Serre 以简洁著称，引语尤需谨慎 |
| 人物时间线 | Serre 与 Grothendieck、Deligne 等人的关系要精确："Serre 影响 Grothendieck → Grothendieck 发展概形 → Deligne 证明 Weil 猜想"这个链条要清晰 |
| 伪精确数字 | "在五个领域留下贡献" — 可以更精确地说是"代数拓扑、代数几何、数论、群论、交换代数"五个领域 |
| 现代术语包装 | Serre 知道的术语和不知道的术语要区分。他写 FAC 时，"概形"这个词还不存在 |
| 可更新数据 | Serre 的年龄是随时间变化的！如果写"今年 XX 岁"需小心。建议用"百岁诞辰 (1926–2026)"做固定锚点 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Faisceaux Algébriques Cohérents (FAC) | 代数凝聚层 | 保留法文原名 |
| Géométrie Algébrique et Géométrie Analytique (GAGA) | 代数几何与解析几何 | 保留法文原名 |
| Serre duality | Serre 对偶 | — |
| Galois representation | Galois 表示 | — |
| Serre's modularity conjecture | Serre 模性猜想 | 注意与"Serre 猜想 (Quillen–Suslin)"区分 |
| spectral sequence | 谱序列 | — |
| coherent sheaf | 凝聚层 | — |
| l-adic cohomology | l-adic 上同调 | — |
| Bass–Serre theory | Bass–Serre 理论 | 两人并列，不分先后 |
| Collège de France | 法兰西公学院 | 不译成"法兰西学院"(后者是 Académie française) |
| École Normale Supérieure (ENS) | 巴黎高等师范学院 | — |
| Bourbaki | 布尔巴基 | — |
| homotopy groups of spheres | 球面的同伦群 | — |

---

## 第 10 步：第二轮布局微调

全部页面写完后：

- 从头到尾翻看 PDF，逐页标记溢出/重叠
- 对标记页按 §8 优先级处理
- 确保每页间距均匀（参照指南 §14.13 面板间距均匀化）
- 封面肖像在右上角（参照 Grothendieck/Riemann/Hilbert 模板）
- 结束页不要放肖像（只放主题句 + 生卒年份。注意：Serre 仍在世，用 "1926–" 表示）

---

## 第 11 步：插入 OpenMath 项目首页

- ★ **使用统一 cover 模板**：从 `../cover/OpenMath_Cover.tex` 复制 `\openmathslide` 命令定义（或直接 `\input`）
- 在 `\begin{document}` 后调用 `\openmathslide`，然后调用塞尔的封面 `\titleslide`

---

## 第 12 步：最终编译

- 确认 `make clean && make` 无错误
- 确认 PDF 输出正常，总页数在 19–21 页之间
- 从头到尾翻看确认无误
- 准备接受外审（找熟悉塞尔的人挑错）

---

## 第 13 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

塞尔的气质：**优雅、深度、跨五领域的丰碑、非科室内乐** — 雄壮慷慨但保持品味。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 沉稳纪录片风，Serre 的优雅风格 |
| ★★★ | Expedition | alex-productions | `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` | 探索史诗，跨五领域的远征 |
| ★★ | Eternals | alex-productions | `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` | 宏大深远，仍在书写的传奇 |
| ★ | Nostalgia | alex-productions | `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` | 怀旧温和，巴黎学派的传承 |

**操作**：复制选定的 `.wav` 到 `Jean_Pierre_Serre/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 完整操作手册 (§16 快速启动清单) |
| `mathematician/pages/Jean-Pierre_Serre/page.md` | Serre Wikipedia 正文 |
| `mathematician/pages/Jean-Pierre_Serre/metadata.json` | Serre Wikidata 元数据 |
| `mathematician/pages/Jean-Pierre_Serre/images.txt` | 图片 URL 清单 |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码（教皇模板） |
| `mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` | Riemann 完整源码（克制天才模板） |
| `mathematician/presentations/hilbert/David_Hilbert_zh.tex` | Hilbert 完整源码（王者模板） |
| `mathematician/presentations/grothendieck/Makefile` | 构建脚本（直接复制） |

---

> **开始执行。每完成一步向我汇报。**
>
> **最重要的事：每写一页就 make，看到溢出就修，不要攒到最后一起修。**
>
> **特别提醒：塞尔是这四位数学家中唯一仍在世的。叙事策略需要区别于已故数学家："遗产"→"仍在书写的传奇"，"他的一生"→"他的百年数学旅程"。百岁诞辰 (1926–2026) 是独有的高光时刻，善加利用。**

... EOF no more lines ...
