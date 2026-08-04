# 诺特 (Emmy Noether) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Grothendieck、Riemann、Hilbert、Serre 成品为参考模板，为诺特制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Emmy Noether (1882–1935)
- **气质关键词**: **开创者、坚韧、抽象代数之母、超越时代的女性、"诺特阿姨"**
- **Wikipedia 页面已下载**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Emmy_Noether/`
  - `page.md` — 正文 Markdown
  - `metadata.json` — Wikidata 元数据
  - `images.txt` — 图片 URL 清单
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

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Emmy_Noether/metadata.json` 及 `page.md`
- 输出以下信息供我校验：
  - **生卒日期**：1882-03-23 ~ 1935-04-14，享年 53 岁（相对早逝）
  - **国籍**：德国（后因纳粹迫害移居美国）
  - **出生地**：Erlangen（埃尔朗根），巴伐利亚
  - **博士导师**：Paul Gordan（戈丹，"不变量之王"）或 名义上是 Gordan，后期受 Ernst Fischer 影响 — 需要从 metadata 确认
  - **博士论文**：1907，《Über die Bildung des Formensystems der ternären biquadratischen Form》（三元双二次型的形式系统的构造）
  - **主要任职机构**：
    - 1915–1933: 哥廷根大学（长期无薪、无正式教职，仅靠 Hilbert 争取到"非官方讲师"身份）
    - 1933–1935: Bryn Mawr College（布林莫尔学院），美国
  - **关键荣誉**：
    - 1932: Ackermann–Teubner 纪念奖（与 Emil Artin 共同获奖）
    - 1932: 苏黎世 ICM 全体大会报告（首次有女性获此邀请）
    - **终身未获得德国大学正式教授职位**（性别歧视）
  - **重要合作者/学生**：
    - 核心合作者：Hilbert, Klein, Ernst Fischer
    - "诺特学派"（Noether school）：van der Waerden, Deuring, Hermann, Witt, Fitting, Levitzki 等
  - **父亲**：Max Noether（著名代数几何学家，埃尔朗根大学教授）
  - **弟弟**：Fritz Noether（应用数学家，1941 年在苏联被处决）
  - **Wikipedia 正文中提取出的关键时间线**（按年份列出 15–20 个关键节点）：
    - 1882: 出生于 Erlangen，数学世家
    - 1900: 通过教师资格考试（当时女性不能正式注册大学）
    - 1904: 获准进入 Erlangen 大学旁听（当时仅 2 名女生）
    - 1907: 获博士学位（Paul Gordan 指导）
    - 1908–1915: 在 Erlangen 数学研究所无薪研究
    - 1915: Hilbert 和 Klein 邀请她去哥廷根
    - 1915: 证明 Noether 定理（对称性与守恒律的联系）
    - 1919: 获得"非官方讲师"(Privatdozent) 资格 — 经过长达 4 年的教职争议
    - 1921: 发表《Idealtheorie in Ringbereichen》（环中的理想理论）— 现代抽象代数的宣言
    - 1922: 成为"非官方的编外教授"（nicht beamteter außerordentlicher Professor），仍无薪
    - 1920s: 抽象代数研究的黄金时期，聚集"诺特男孩"
    - 1928–1929: 访问莫斯科大学，与 Alexandroff 合作
    - 1932: 苏黎世 ICM 全体大会报告
    - 1933: 纳粹驱逐犹太裔学者，被解雇
    - 1933: 移居美国，在 Bryn Mawr College 任教
    - 1935: 因卵巢囊肿手术并发症去世，年仅 53 岁
  - **人格特质线索**：
    - 不修边幅、完全沉浸于数学——这是几乎所有同时代人对她的第一印象
    - van der Waerden 描述："她完全不在乎外表，甚至不在乎饮食，但她关心每一个学生，就像关心自己的孩子。"
    - 她对学生的指导方式不是"教"，而是"激发"——让学生在讨论中自己发现真理
    - 她的讲课风格：不照本宣科，现场思考，充满激情
    - 性格开朗乐观，即使在最困难的时期（无薪、无职称），也保持着对数学的巨大热情
    - 被学生们称为"Der Noether"（用阳性冠词，带敬畏式戏谑 —— Wikipedia注：该昵称"并非总是善意的"）
    - 她没有结婚，没有子女——她的学生就是她的孩子

### 与其他已立传数学家的关系网络

- **Hilbert** — 最坚定的支持者。Hilbert 为争取诺特的教职与哥廷根大学保守派激烈斗争，说出名言："这里是大学，不是澡堂！"（指性别不应成为教职障碍）
- **Klein** — 与 Hilbert 一同邀请诺特来哥廷根
- **Grothendieck** — 不是直接关系，但诺特的抽象代数方法为 Grothendieck 的概形理论奠定了代数学基础
- **Serre** — FAC 中使用的大量交换代数工具直接来源于诺特的工作
- **Gordan** — 博士导师，"不变量之王"，早期论文的计算风格（后来诺特完全转向抽象方法）
- **Alexandroff** — 莫斯科时期的合作者，拓扑与代数的交叉

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `noether/` 子目录
- 创建 `noether/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `noether/Makefile`
- 将 `MAIN` 变量改为 `Emmy_Noether_zh`
- 将 `VIDEO_NAME` 变量改为 `Emmy_Noether_zh`

---

## 第 3 步：收集图片

- 从 `pages/Emmy_Noether/images.txt` 中选出 4–6 张高质量图片
- 优先选择：
  1. **经典肖像（1920s 哥廷根时期）** — 诺特最广为人知的形象
  2. 哥廷根数学研究所外景
  3. 与学生的合影（如有）
  4. Bryn Mawr College 校园
  5. 手稿或论文封面
- 下载到 `noether/images/`
- ★ **特殊要求**：诺特的照片数量相对有限。她不以容貌著称，选择照片时注重真实感和学术气质，而非刻意美化

---

## 第 4 步：建立时间线和叙事骨架

诺特的一生是一个双重叙事：**学术上的辉煌革命**与**社会层面的性别斗争**。这两条线交织构成了她的独特故事。

### 生平阶段

1. **Erlangen 的数学少女 (1882–1915)**：出生于数学世家（父亲 Max Noether），克服性别障碍获得博士学位，在 Gordan 指导下完成计算风格的早期工作
2. **哥廷根的无声革命 (1915–1933)**：Noether 定理（物理学基石）、抽象代数的创立、聚集"诺特男孩"、长达十余年无薪无职的教学——最终成为 20 世纪代数学的最高权威
3. **流亡与早逝 (1933–1935)**：纳粹驱逐、移居美国、在 Bryn Mawr 找到最后的学术家园、53 岁猝然离世

### 核心数学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 理论物理 | Noether 定理 — 对称性与守恒律的等价 | 1915, 1918 发表 |
| 抽象代数 | 环上的理想理论 (Idealtheorie in Ringbereichen) — 现代抽象代数的奠基之作 | 1921 |
| 交换代数 | Noether 环、Noether 模、升链条件 (ACC) | 1920s |
| 代数几何 | 抽象代数方法进入几何 | 1920s |
| 代数数论 | 类域论的代数化 | 1920s |
| 表示论 | 群表示与代数的交叉 | 1920s |
| 同调代数 | 同调方法的代数基础 | 1920s–1930s |

### ★ 诺特独有的叙事线索

1. **性别之战** — 从"女性不能上大学"到"女性不能当教授"，诺特用数学实力击碎每一个障碍。Hilbert 为她辩护的名言："这里是大学，不是澡堂！"
2. **Noether 定理** — 这是她最广为人知的贡献（物理学家人人皆知），但讽刺的是，这反而是她最"不代数"的工作。它是现代物理学的基石之一：每一个连续对称性都对应一个守恒律
3. **从计算到抽象** — 她的博士论文（在 Gordan 指导下）充满了冗长的多项式计算（附录了 300+ 个不变量）。但转入抽象方法后，早期工作与成熟期形成极端对比。Weyl 写道："几乎无法想象更大的对比……前者是形式计算的极端案例，后者是公理化概念思维的极端而宏大的范例。"
4. **无薪的教授** — 在哥廷根近 20 年，她从未获得正式教授职位和薪酬。靠遗产和家庭支持生活。但她聚集了当时最优秀的年轻代数学家
5. **诺特男孩** — van der Waerden 的《代数学》(Moderne Algebra) 几乎是 Noether 讲义的书面版
6. **Noether 环** — 以她命名的代数结构，是整个交换代数和代数几何的基础构件
7. **纳粹迫害** — 犹太血统 + 左翼政治倾向（她曾短暂参与社会民主党活动），双重原因导致被驱逐
8. **早逝** — 53岁，手术并发症。Einstein 在悼文中称她为"自女性开始接受高等教育以来，最重要的创造性数学天才"

### 人物关系

- **Max Noether (父亲)** — 代数几何学家，学术启蒙
- **Gordan** — 博士导师，"不变量之王"，计算风格
- **Fischer** — 影响她转向抽象方法的数学家
- **Hilbert** — 最坚定的支持者，为她争取教职
- **Klein** — 与 Hilbert 一起邀请她来哥廷根
- **van der Waerden** — "诺特男孩"中最著名的一位，《代数学》作者
- **Alexandroff** — 莫斯科时期的合作者
- **Einstein** — 高度评价她，1935 年亲撰悼词

---

## 第 5 步：设计配色方案

- 诺特的气质关键词：**坚韧、温暖、开创性、女性力量、代数的纯粹之美**
- **建议配色：紫罗兰 + 象牙白 + 暗玫瑰金**（抽象代数的优雅 + 女性力量的温柔 + 哥廷根的学术传统）
- **需要与已有的 Hilbert（普鲁士蓝+金）和 Grothendieck 有所区分！**
- 请给出完整的 `\definecolor` 方案：
  - **主色 (coverprimary)**：**深紫罗兰** — 抽象代数的神秘与纯粹，也与女性气质温和呼应
  - **强调色 (coveraccent)**：**暗玫瑰金** — 温暖而有力，象征她对学生如母亲般的关怀
  - 四个分类色，对应诺特的多元贡献：
    - **badgealgebra** (抽象代数) — 紫蓝
    - **badgetheorem** (Noether 定理/物理) — 暖铜
    - **badgenumber** (数论/同调) — 深松绿
    - **badgewomen** (女性先驱/社会意义) — 玫瑰
  - 各面板色 (purplepanel/amberpanel/greenpanel/bluepanel/goldpanel/graypanel)

---

## 第 6 步：规划幻灯片序列

诺特的内容有两条主线（数学革命 + 性别斗争），建议 19 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 人物篇 ===
01  封面 — 《诺特：抽象代数之母》 / Emmy Noether 1882–1935 + 四色badge
02  为什么诺特是超越时代的人 — Noether 定理 + 抽象代数奠基人 + 女性先驱 + "诺特男孩"之母

=== 早年 ===
03  Erlangen 的数学少女 (1882–1915) — 数学世家、父亲的女儿、突破性别限制、博士 (1907)

=== Noether 定理 ===
04  Noether 定理 (1915/1918) — 对称性与守恒律的等价，物理学最深刻的定理之一

=== 抽象代数革命 ===
05  抽象代数的诞生 (1921) — 《环中的理想理论》，从计算到抽象的范式转换
06  Noether 环与升链条件 — 现代代数的基本构件，代数几何的语言基石

=== 哥廷根岁月 ===
07  无薪的教授 — 在哥廷根近20年从未获得正式教授职位，"这里是大学，不是澡堂！"
08  诺特学派 — van der Waerden, Deuring, Witt, Hermann…… 一代代数大家的共同源泉

=== 代数几何与数论 ===
09  代数的触角 — 类域论的代数化、抽象方法进入几何
10  莫斯科之旅 (1928–1929) — 与 Alexandroff 的合作，拓扑与代数的交叉

=== 纳粹与流亡 ===
11  被驱逐 (1933) — Nazi 的种族法令，哥廷根的终结
12  Bryn Mawr 的最后时光 (1933–1935) — 在美国找到学术家园，53岁猝然离世

=== 遗产 ===
13  "自女性开始接受高等教育以来，最重要的创造性数学天才" — Einstein 的悼词
14  诺特的数学遗产 — 从 Noether 环到 Grothendieck 的概形，代数方法的永恒印记

=== 结尾 ===
15  思想回响 — 诺特证明了：性别从不是数学的障碍，数学只为心灵开放
16  结束页 — 主题句：她用代数改变了世界。
```

> **可以微调。** 征求我的意见后再开始写代码。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Emmy_Noether/Emmy_Noether_zh.tex`
- 完全参照已有模板的代码结构
- 每页用 `\newcommand{\xxxslide}{% ... }` 定义

### 关键要求

- **每写完一页立即编译 (`make clean && make`)，不等待全部写完**
- 编译失败立即修复，不要跳过
- 中文正文，英文术语和公式保留原文

---

## 第 8 步：布局检查 ★★★

同已有模板，每写完一页检查溢出。

---

## 第 9 步：史实审查 + 术语审查

### 诺特特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 诺特特有的高危点 |
|---------|---------------------|
| **"第一位女数学家"** | ★ 绝对不能说。在她之前有 Hypatia、Sophie Germain、Sofia Kovalevskaya 等。正确表述："自女性开始接受高等教育以来，最重要的创造性数学天才"（Einstein 原话） |
| **博士导师** | Paul Gordan 是名义导师。但博士论文是计算风格的，后来诺特完全转向抽象方法——这不能说是"背叛"，而是"超越" |
| **Noether 定理的归属** | 定理是 1915 年证明的，1918 年正式发表。有时被归功于 Hilbert 的启发，但定理本身是 Noether 独立证明的。不要写"Hilbert 和 Noether 共同发现"。 |
| **Hilbert 的名言** | "这里是大学，不是澡堂！" — 这是 Hilbert 在教授会议上为诺特争取教职资格时说的话。故事真实，但原话是德文 "Eine Universität ist doch keine Badeanstalt!" |
| **无薪** | 诺特在哥廷根长期无偿教学，靠家庭遗产生活。这是事实，但不要过度渲染"贫困"——Noether 家族是富裕的学术家庭 |
| **纳粹驱逐** | 诺特在被解雇后还短暂在哥廷根逗留，她还在自己家里继续为学生上课（纳粹初期尚未强制执行禁令） |
| **死因** | 卵巢囊肿手术并发症。术后前三天恢复良好，第四天突然昏迷、高烧至 42.8°C 去世。**不要说"最后一天仍在讨论数学"** —— Wikipedia 无此记载。 |
| **左翼倾向** | 诺特曾参与社会民主党活动，被纳粹视为"犹太人 + 马克思主义者"双重目标。这个事实要提及但不需要政治渲染 |
| **★ 首位博士生** | ★ Grete Hermann (1925 年 2 月答辩) 是诺特的首位博士生，不是 Max Deuring (1930 年)。Wikipedia: "Her first was Grete Hermann"。如果 Beamer 只列一个学生并标注"首位"，必须是 Hermann。 |
| **★ "诺特男孩"名单** | ★ Hasse 是合作者（非学生），Mac Lane 仅出现在参考书目中（非 Noether school 成员）。Wikipedia Noether school 章节列出的实际成员包括：van der Waerden, Deuring, Hermann, Witt, Fitting, Levitzki, Tsen, Schilling 等。不要编造名单。 |
| **★ Weyl 悼词核实** | ★ Weyl 在 page.md 中可验证的悼词是计算与抽象的对比段落，而非"她是最伟大的数学家…"。其他 Weyl 引语需从 page.md 逐字核实后再使用。 |
| **★ 死亡叙述核实** | ★ Wikipedia 记载：术后第四天昏迷→去世。无"最后一天讨论数学"记载。不要自行添加温情细节。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Noether's theorem | Noether 定理 | 不要翻译成"诺特定理"然后和环论混淆 |
| Noetherian ring | Noether 环 | 注意大小写 Noetherian ≠ noetherian |
| ascending chain condition (ACC) | 升链条件 | — |
| Idealtheorie in Ringbereichen | 《环中的理想理论》 | 保留德文原名 + 中文翻译 |
| Noether's boys | 诺特男孩 | 非正式称呼，但历史传统如此 |
| symmetry & conservation law | 对称性与守恒律 | — |
| Bryn Mawr College | 布林莫尔学院 | 宾夕法尼亚州，女子学院 |
| Privatdozent | 编外讲师 | 保留德文 |
| außerordentlicher Professor | 编外教授 | — |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个"断言 | 不说"第一个抽象代数学家"→"抽象代数的奠基人之一" |
| 女性叙事过重 | 诺特首先是一位伟大的数学家，然后才是女性先驱。叙事比例：数学70%+生平/社会30% |

---

## 第 10–13 步：同已有模板

（布局微调、OpenMath首页、最终编译、音乐选择）

### 音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

诺特的气质：**坚韧、温暖、开创性、代数的纯粹之美** — 温暖而坚定的室内乐，抒情但不感伤，有力但不张扬。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Awaken | alex-productions | `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` | 鼓舞明亮，开创者的光芒 |
| ★★★ | With Me | alex-productions | `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` | 温和稳定，代数的纯粹之美 |
| ★★ | Daylight | alex-productions | `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` | 明亮轻快，Noether 的乐观与坚韧 |
| ★ | Nostalgia | alex-productions | `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` | 怀旧温和，哥廷根学派的传承 |

**操作**：复制选定的 `.wav` 到 `Emmy_Noether/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 完整操作手册 |
| `mathematician/pages/Emmy_Noether/page.md` | Noether Wikipedia 正文 |
| `mathematician/pages/Emmy_Noether/metadata.json` | Noether Wikidata 元数据 |
| `mathematician/pages/Emmy_Noether/images.txt` | 图片 URL 清单 |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码 |
| `mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` | Riemann 完整源码 |
| `mathematician/presentations/hilbert/David_Hilbert_zh.tex` | Hilbert 完整源码 |
| `mathematician/presentations/serre/Jean_Pierre_Serre_zh.tex` | Serre 完整源码 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/Emmy_Noether/page.md，从头到尾逐段阅读全文
2. 同时打开 Emmy_Noether_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ 诺特特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **"首位博士生"归属** | Grete Hermann 才是首位(1925.2), Deuring 是 1930 年 | page.md 搜索 "Her first was Grete Hermann" |
| **Mac Lane 是否为学生** | 仅在参考书目出现，不在 Noether school 正文 | page.md 搜索 "Mac Lane" → 确认仅出现在参考书目 |
| **Hasse 是合作者非学生** | Hasse 接手了 Schilling 的论文指导，非 Noether 的学生 | page.md 搜索 "Hasse" → 确认身份 |
| **Weyl 悼词原文** | 引语可能被捏造，需逐字与 page.md 对照 | page.md 搜索 "Weyl wrote" → 获取原文 |
| **"计算？我不懂计算"** | page.md 中无此引语 | page.md 全文搜索 "计算" → 确认不存在 |
| **死亡叙事** | 术后第4天昏迷去世，非"最后一天讨论数学" | page.md 搜索 "unconscious" → 获取精确描述 |
| **"Der Noether"含义** | 褒贬不一，非纯亲昵 | page.md 搜索 "nickname was not always used in a well-meaning manner" |

### 优先级定义

| 优先级 | 定义 | 诺特实际案例（本轮） |
|:--:|------|------|
| 🔴 P0 | **事实错误** | Deuring 被标注为"首位博士生" |
| 🟡 P1 | **来源存疑/捏造** | "计算？我不懂计算"、Weyl 悼词捏造、Mac Lane 非学生、"最后一天讨论数学" |
| 🟢 P2 | **重要遗漏** | 术后三天恢复良好→第四天昏迷的细节、骨灰安放于 Bryn Mawr Old Library |
| ⚪ P3 | **可选补充** | Einstein 致 Hilbert 信中称赞诺特的原文 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. 诺特是唯一一位女性，叙事需要平衡"数学家"与"女性先驱"两条线——以数学为主
> 2. Noether 定理和 Noether 环是完全不同的两个东西——每页要明确说的是哪一个
> 3. Hilbert 的名言"这里是大学，不是澡堂"必须要出现——这是最有力的一句话
> 4. 她的故事不应该被讲成"苦情戏"——她热爱数学，心态乐观，这不是一个受害者叙事
> 5. **引语必须来自 page.md** —— 不要使用任何无法在 page.md 中逐字验证的引语
> 6. **"Noether's Boys" → "Noether School"** —— Wikipedia 正式用语是 Noether school
> 7. **Grete Hermann 是首位博士生 (1925)** —— 不是 Max Deuring (1930)