# 斯里尼瓦瑟·拉马努金 (Srinivasa Ramanujan) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Weyl、Hardy 等成品提示词为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Srinivasa Ramanujan (1887–1920)
- **气质关键词**: **印度天才、直觉穿越时代的数学家、mock theta 函数、1729、燃烧的32年、上帝以无限级数思考**
- **Wikipedia 页面**: ✅ 已下载并完成 Review
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Srinivasa_Ramanujan/`
  - Wikipedia 英文条目: `Srinivasa Ramanujan`
  - **Review 状态**: ✅ 第1轮完成 — 肖像+国籍+格式检查；第2轮完成 — 逐页 Wikipedia 交叉核查
- **Beamer 文件**: `mathematician/presentations/Srinivasa_Ramanujan/Srinivasa_Ramanujan_zh.tex` (517行, 17页)
  - 编译: `make distclean && make` — 272KB PDF, 零警告
- **Review 发现的关键修正**:
  - P0: 添加肖像标注 `S. Ramanujan, c.1913`
  - P0: Carr's Synopsis 年龄 15→16（Wikipedia: "in 1903, when he was 16"）
  - P0: Hook 页加入 Hardy 最高评价 "a mathematician of the highest quality, a man of altogether exceptional originality and power"
  - 措辞: "耗尽两位寄住大学生的数学知识" → "已无法再教他数学"
- **参考模板**: `hardy/`, `riemann/`, `grothendieck/` 的完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Srinivasa_Ramanujan/`

输出以下信息供校验：

- **全名**: Srinivasa Ramanujan Aiyangar
- **生卒日期**: 1887-12-22 ~ 1920-04-26，享年 **32** 岁
- **国籍**: 英属印度 → 印度（posthumously）
  - **封面国籍标识**: `🌐 英属印度（时为大英帝国殖民地）`
- **出生地**: Erode（埃罗德），Madras Presidency（马德拉斯管辖区），英属印度
- **逝世地**: Madras（马德拉斯，今 Chennai），英属印度
- **死因**: 诊断结核病和维生素缺乏；1994 年医学分析认为更可能是肝阿米巴病 (hepatic amoebiasis) —— 当时可治愈的疾病
- **关键事件**: 1917年末–1918年初，在伦敦地铁站跳下轨道试图自杀，苏格兰场以"企图自杀"（当时属犯罪）逮捕，Hardy 出面干预后获释
- **博士导师**: G. H. Hardy 与 J. E. Littlewood（剑桥大学，实际上 Ramanujan 未正式获得 PhD，剑桥授予其 B.A. by Research，后转为 FRS）
- **教育**: Government Arts College, Kumbakonam（因数学偏科未能毕业）；Pachaiyappa's College, Madras（同样未毕业）
  - **几乎没有正规高等数学训练，完全是自学成才**
- **主要任职**:
  - 1912–1913: Madras Port Trust 职员（月薪 30 卢比）
  - 1914–1919: Trinity College, Cambridge（Hardy 邀请）
  - 1919–1920: 回到印度，病重
- **关键荣誉**:
  - 1918: **FRS（皇家学会院士）**—— 第二位当选的印度人，也是当时最年轻的 FRS 之一
  - 1918: Trinity College 院士（Fellow）—— 第一位当选的印度人
- **重要人物关系**:
  - **G. H. Hardy**（导师、伯乐、合作者）—— "一生中唯一的浪漫事件"
  - **J. E. Littlewood**（Hardy 的合作者，对 Ramanujan 也给予高度评价）
  - **S. Narayana Iyer**（马德拉斯港务局的上司，帮助 Ramanujan 联系英国数学家）
  - **Sir Francis Spring**（马德拉斯港务局主席，支持 Ramanujan 赴英）
  - **E. H. Neville**（剑桥数学家，1914 年亲赴印度接 Ramanujan 赴剑桥）
  - **G. N. Watson**（后继者，花了数年整理 Ramanujan 的笔记）
  - **Bruce Berndt**（现代整理者，发表 Ramanujan's Notebooks 五卷）
  - **Namagiri Thayar**（Ramanujan 自称灵感来源于这位 Namakkal 女神在梦中的启示）

### 关键时间线（15–20 个节点）：

- 1887: 12 月 22 日生于印度南部泰米尔纳德邦的 Erode，家境贫寒的婆罗门家庭
- 1897–1903: 在 Kumbakonam 的 Town Higher Secondary School 展露惊人数学天赋 —— 12 岁独立推导出三角学公式
- 1903: 16 岁时，借到 G. S. Carr 的 *A Synopsis of Elementary Results in Pure and Applied Mathematics*（两卷本，含约 5000 条定理，无证明，仅为公式列表）—— 这本书成为 Ramanujan 的数学启蒙，并深远影响了他独特的"跳跃式"证明风格
- 1904: 获得数学奖学金进入 Government Arts College, Kumbakonam —— 但因沉迷数学、其他科目不及格而失去奖学金，最终退学
- 1906–1912: 贫困与孤独的自学岁月 —— 在马德拉斯一带靠零工为生，在石板上演算数学，极度贫困，多次患病
- 1912: 在马德拉斯港务局做三等职员（月薪 30 卢比），上司 Narayana Iyer 是印度数学会成员，发现了他的天赋
- 1913.01.16: **寄出改变命运的信** —— 给 G. H. Hardy 写了 10 页的信，附上 120 个没有证明的定理
  - Hardy 最初以为是恶作剧或疯子来信
  - 与 Littlewood 研究了一整夜后，Hardy 意识到："我从未见过类似的东西。它们一定是真的，因为如果它们不是，没有人会有想象力去发明它们。"
- 1914.03: E. H. Neville 亲赴印度接 Ramanujan；4 月抵达剑桥，入住 Trinity College
- 1914–1917: 与 Hardy 合作的黄金时期 —— 整数分拆的渐近公式、高度合成数、Ramanujan prime、Ramanujan theta 函数、Ramanujan 猜想（τ 函数）
- 1917: 健康状况急剧恶化 —— 英国气候、营养不良（严格的素食主义在战时的英国难以维持）、过度工作。疑似肺结核 + 维生素缺乏
- 1918: 当选 FRS 和 Trinity Fellow —— 在病床上收到消息
- 1919: 返回印度，健康状况持续恶化
- 1920: 1 月，在病床上写下了最后一封给 Hardy 的信，描述了 **mock theta functions**（模仿 θ 函数）—— 这是他一生最后的、也是最神秘的一批数学发现
- 1920: 4 月 26 日，在 Kumbakonam 逝世，年仅 32 岁

### 人格特质线索：

- **直觉压倒一切** —— 他声称自己的数学来自 Namagiri 女神的梦示。他说："一个方程对我来说没有意义，除非它表达了神的思考。"
- **极度虔诚** —— 严格的婆罗门素食者。每日祭祀。拒绝去英国因担心种姓制度，直到女神 Namagiri 在梦中应允。
- **孤独的天才** —— 在印度几乎无人能理解他的数学；在剑桥，他也与英国数学家格格不入。语言的隔阂和文化的差异使他始终是一个孤独者。
- **"他属于 25 岁、50 岁、100 岁之前"** —— Hardy 在悼词中写道："他所取得的成就，将在他身后一百年甚至更久的时间里被反复研究。"
- **Hardy 的 25-30-80-100** —— "在数学能力的天然天赋上，我给自己打 25 分，Littlewood 30 分，Hilbert 80 分，Ramanujan 100 分。"
- **Ramanujan 的反面** —— 他没有正规训练，不懂复分析的标准方法，不懂什么是"证明"。他的推理方式本质上是归纳和类比，像是一个来自另一个数学世界的访客。
- **1729 与出租车** —— Hardy 去医院看望他时说："我坐的出租车号码是 1729，一个相当无趣的数字。" Ramanujan 立即回答："不，Hardy，这是一个非常有趣的数字！它是可以用两种方式表示为两个立方数之和的最小正整数。"（1729 = 1³ + 12³ = 9³ + 10³）

---

## 核心数学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 数论 | 整数分拆的渐近公式 —— 与 Hardy 合作，用圆法得到 p(n) 的渐近公式 | 1917–1918 |
| 数论 | Ramanujan 质数、高度合成数 | 1915 |
| 数论 | Ramanujan τ 函数 —— 模形式的 Fourier 系数，Ramanujan 猜想（后来被 Deligne 证明，获 Fields 奖） | 1916 |
| 分析 | Ramanujan theta 函数、q-级数 | 1914–1919 |
| 分析 | 连分数 —— 许多惊人的恒等式，至今仍在被验证 | 1913–1920 |
| 分析 | **mock theta functions（模仿 θ 函数）** —— 1920 年临终前发现的最后一批函数，直到 21 世纪才被完全理解（Zwegers 2002 年博士论文） | 1920 |
| 级数 | Ramanujan 级数 —— 计算 π 的极快收敛级数（如 1/π = (2√2/9801) ∑ …） | 1914 |
| 组合 | Rogers–Ramanujan 恒等式 —— 分拆理论中的基本结果 | 1915 |
| 数论 | Ramanujan–Nagell 方程 | — |
| 数论 | 1729 的奇妙性质 | — |

### ★ 拉马努金独有的叙事线索

1. **"他们一定是真的，因为没有人能有想象力发明它们"** — Hardy 收到 120 个没有证明的定理时的反应。这是 Ramanujan 传奇的核心：他的数学不是来自推导，而是来自某种难以解释的直觉来源。这是数学史上独一无二的案例。

2. **没有受过正规训练的超级天才** —— Ramanujan 不懂现代复分析、不懂函数论、不懂什么是"严格的证明"。他在石板上（买不起纸）用粉笔演算，写出结果后用肘部擦掉。他的推理方式在西方数学家看来几乎不可理解——但结果正确得令人恐惧。

3. **mock theta functions** —— 1920 年临终前写给 Hardy 的最后一封信，描述了他称为"mock theta functions"的一类函数。Hardy 当时完全无法理解。直到 2002 年，荷兰数学家 Sander Zwegers 在博士论文中才揭示了其深层结构——它们与 Maass 形式有关。从 1920 到 2002，82 年的等待。

4. **Ramanujan 猜想与 Fields 奖** —— 1916 年，Ramanujan 提出了关于 τ 函数的一个猜想。这个猜想后来成为模形式理论与代数几何的桥梁。1974 年，Pierre Deligne 用代数几何中 étale cohomology 证明了 Weil 猜想（Ramanujan–Petersson 猜想作为推论），并因此获得 1978 年 Fields 奖。Deligne 在获奖演说中最先感谢的人之一是……Ramanujan。

5. **"上帝以无限级数思考"** —— Ramanujan 的数学观。他说："一个方程对我来说没有意义，除非它表达了神的思考。" 这不是修辞，而是他的真实信念。Namagiri 女神在梦中向他揭示公式 —— 他本人深信不疑。

6. **Carr 的 Synopsis** —— Ramanujan 15 岁时借到的唯一一本高等数学书。这本书只有公式、几乎没有证明。它塑造了 Ramanujan 整个数学风格：跳跃式的、直觉导向的、直接写结果而不是逐步推导。

7. **素食与饥饿** —— 在第一次世界大战的英国，严格的婆罗门素食使 Ramanujan 几乎无法获得足够营养。他经常挨饿，自己做饭（做得不好），拒绝吃任何非素食。这直接导致了他的健康崩溃和英年早逝。

8. **死后 100 年的旅程** —— Ramanujan 留下了三本笔记本（Notebooks）和一堆散页（"Lost Notebook"）。G. N. Watson 花了数十年整理。Bruce Berndt 花了 20 年出版了五卷本的评注版（Ramanujan's Notebooks）。直到 21 世纪，仍有数学家从 Ramanujan 的笔记中发现新的定理，证明它们，并发表论文。

---

## 人物关系

- **G. H. Hardy（伯乐与导师）** — "一生中唯一的浪漫事件"。Hardy 意识到 Ramanujan 的天才，说服他来到剑桥，与他合作，保护他，最终为他的早逝哀悼。
- **J. E. Littlewood** — 与 Hardy 一起审阅了 Ramanujan 的来信，高度认可其天才
- **S. Narayana Iyer（上司与推荐人）** — 马德拉斯港务局的印度数学会成员，最早发现 Ramanujan 天赋的人之一
- **Namagiri Thayar（女神）** — Ramanujan 自称所有数学灵感来自她的梦示
- **G. N. Watson（后继者）** — 花了数十年整理 Ramanujan 的笔记
- **Bruce Berndt（现代整理者）** — 出版 Ramanujan's Notebooks 五卷（1985–1998）
- **Pierre Deligne** — 1974 年证明了 Weil 猜想（Ramanujan 猜想作为推论），获 Fields 奖
- **Sander Zwegers** — 2002 年揭示了 mock theta functions 的深层结构

---

## 第 5 步：设计配色方案

- **建议配色：檀香木暖橙 + 印度赭石红 + 象牙纸白 + 墨夜黑** —— 印度大地的温度、南方神庙的色彩、Ramanujan 在石板上演算的意象，以及直觉穿越时代的深邃
- 需要与已有配色完全不同！
  - Hilbert：普鲁士蓝 + 金
  - Grothendieck：深靛 + 金
  - Riemann：墨绿 + 银灰
  - Weyl：深琥珀金 + 星夜紫
  - Hardy：剑桥蓝 + 板球绿 + 牛津金
  - Kolmogorov：深松绿 + 古铜金

- 主要色值建议：
  | 用途 | 色名 | 建议色值 | 说明 |
  |------|------|---------|------|
  | 背景 | `bgmain` | `#FAF5EB` | 暖调象牙纸白 —— Ramanujan 石板上演算的意象 |
  | 主色 | `coverprimary` | `#5C1E03` | 印度赭石深红 —— 南方神庙的庄严 |
  | 强调色 | `coveraccent` | `#D4782F` | 檀香木暖橙 —— 印度香料与大地的温度 |
  | 深色文本 | `coverdark` | `#2C1810` | 墨夜黑 —— 直觉穿越时代的深邃 |
  | 浅色文本 | `covermuted` | `#8B7355` | 古纸色 —— 笔记与散页的质感 |

- 四个分类色，对应 Ramanujan 的四大支柱：
  - **badgeRamanujanIntuition** (直觉/梦示/天才) — 檀香暖橙 `#D4782F` —— "女神在梦中的启示"
  - **badgeRamanujanNumber** (数论/分拆/质数) — 印度赭石深红 `#8B2500` —— "数的秘密语言"
  - **badgeRamanujanAnalysis** (q-级数/mock theta/连分数) — 神庙金 `#C9A84C` —— "无限级数的神圣游戏"
  - **badgeRamanujanLegacy** (笔记本/后人整理/猜想验证) — 墨蓝 `#1B3A5C` —— "一个世纪的等待与解答"

---

## 第 6 步：规划幻灯片序列（建议 18–20 页）

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《拉马努金：以直觉穿越时代的印度天才》 / Srinivasa Ramanujan 1887–1920
02  为什么 Ramanujan 独一无二 — 无正规训练的超级天才·剑桥FRS·32年燃烧·百年回响

=== 早年 ===
03  神童在石板上 (1887–1903) — 12岁独立推导三角学·Carr的Synopsis·一个公式塑造一个天才
04  失学的数学家 (1904–1912) — 退学·贫困·在石板上孤独演算·港务局三等职员

=== 改变命运的通信 ===
05  1913年1月16日：给 Hardy 的信 — 120个没有证明的定理·"它们一定是真的，因为没有人能有想象力发明它们"
06  从马德拉斯到剑桥 (1914) — Neville 亲赴印度·女神梦中的应允·跨越大洋的旅程

=== 剑桥岁月 ===
07  Hardy–Ramanujan 合作 (1914–1917) — 分拆渐近公式·圆法·高度合成数·1729 出租车
08  Ramanujan τ 函数与猜想 (1916) — τ(n) 的神秘性质·半个世纪后被 Deligne 证明·Fields 奖的回响

=== 天才的独特风格 ===
09  "直觉压倒一切" — 梦示·Namagiri 女神·Ramanujan 的数学观·"方程必须表达神的思考"

=== 悲剧 ===
10  饥饿与疾病 (1917–1919) — 战时英国·素食饥饿·健康崩溃·病床上的 FRS
11  最后的光芒：mock theta functions (1920) — 临终前给 Hardy 的最后一封信·82年的谜·Zwegers 2002

=== 数学贡献 ===
12  Ramanujan 的数论宇宙 — 分拆·1729·质数·Rogers–Ramanujan 恒等式
13  q-级数与连分数 — 惊世骇俗的恒等式·至今仍在被验证
14  Ramanujan 的 π 公式 — 1/π 的极快收敛级数·现代计算 π 的核心工具

=== 遗产 ===
15  三本笔记本与"Lost Notebook" — Watson 的40年·Berndt 的20年·五卷评注·仍在发现新定理
16  Ramanujan 猜想 → Deligne → Fields 奖 — 一个1916年的直觉，1974年被证明，1978年获最高荣誉

=== 结尾 ===
17  拉马努金的遗产 — 他的思想跨越了一个世纪，而我们的理解才刚刚开始
18  结束页 — 主题句："一个方程对我来说没有意义，除非它表达了神的思考。"
```

---

## 第 9 步：史实审查

### 拉马努金特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **Ramanujan 的"证明"风格** | 不要说他"不会证明"——更准确地说：他的推理方式与现代数学的公理-演绎体系完全不同，是归纳、类比与直观洞察的混合体。他写的"证明"在西方数学家看来不完整，但他几乎从不出错。 |
| **"没有受过正规教育"** | Ramanujan 上过大学（Government Arts College 和 Pachaiyappa's College），只是因偏科未毕业。不是从未上过学。他是"未完成正规高等数学教育"，而非"文盲"。 |
| **mock theta functions** | 这不是 Ramanujan 自己命名的。他称之为"mock ϑ-functions"。名称的精确性很重要。直到 2002 年才被 Zwegers 完全理解——这是核心叙事点。 |
| **1729 轶事** | Hardy 去看 Ramanujan 时，Ramanujan 正卧病在床。Hardy 说出租车号码是 1729，"一个相当无趣的数字"。Ramanujan 并不是"当场"算出 1³+12³=9³+10³——他早就知道这个性质。正确的引述是："不，这是一个非常有趣的数字——它是可以用两种不同方式表示为两个立方数之和的最小正整数。" |
| **Hardy 的 25-30-80-100** | 精确数字，不要写"约"。原话是：Hardy 给自己 25 分（作为数学家），Littlewood 30 分，Hilbert 80 分，Ramanujan 100 分（作为"天然数学天赋"natural mathematical genius）。 |
| **FRS 年份** | 1918 年，不是 1917。他是第二个当选 FRS 的印度人，也是当时最年轻的 FRS 之一。 |
| **Ramanujan 猜想** | 正确的名称是 **Ramanujan–Petersson 猜想**（Petersson 在 1930 年代给出了推广形式）。Deligne 1974 年证明的是更广义的 Weil 猜想（Ramanujan 猜想作为一个推论）。不要写"Deligne 证明了 Ramanujan 猜想获 Fields 奖（1978）"——他是因为证明了 Weil 猜想获 Fields 奖。 |
| **素食与饥饿** | 一战期间英国实行食品配给，Ramanujan 的婆罗门素食使他极难获得足量蛋白质。他自己做饭但做得不好。这不是"不适应英国生活"——这是严格宗教规条与战时物资匮乏的致命冲突。 |
| **Lost Notebook** | "Lost Notebook" 是 G. N. Watson 和后来者用的称呼。实际上 Watson 在 1965 年去世后，这本笔记在 Trinity College 图书馆"丢失"了一段时间。George Andrews 在 1976 年在 Trinity 图书馆重新发现了它。所谓"失落的笔记本"更多是一种文学修辞——它一直保存在 Trinity，只是被遗忘了。 |
| **Ramanujan 与 Namagiri 女神** | 这是他本人的真诚信仰，不是后人附会的传说。处理时应尊重其宗教虔诚，不以猎奇或嘲笑的口吻叙述。用"他自称…""按照他的说法…"。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| mock theta functions | 模仿 θ 函数 / mock theta 函数 | 也译"模拟 θ 函数"，学术文献中两种译法都有。建议括号双语 |
| Ramanujan conjecture | Ramanujan 猜想 / Ramanujan–Petersson 猜想 | 不要漏掉 Petersson |
| Ramanujan tau function | Ramanujan τ 函数 | τ 是希腊字母 tau |
| partition function | 分拆函数 | 不要与"配分函数"（统计力学）混淆 |
| q-series | q-级数 | 标准译法 |
| continued fraction | 连分数 | 标准译法 |
| highly composite number | 高度合成数 / 高合成数 | 两种译法均可 |
| Ramanujan prime | Ramanujan 质数 | 标准译法 |
| Rogers–Ramanujan identities | Rogers–Ramanujan 恒等式 | Rogers 先于 Ramanujan 发现，但 Ramanujan 独立重新发现 |
| Ramanujan's Lost Notebook | Ramanujan 遗失笔记 | 也可译"失落笔记" |
| A Synopsis of Elementary Results | 《纯粹数学与应用数学基础结果纲要》 | Carr 1886 年的书 |
| Erode / Kumbakonam | 埃罗德 / 贡伯戈讷姆 | 泰米尔纳德邦地名 |
| Madras Presidency | 马德拉斯管辖区 | 英属印度行政单位 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一次/第一个"断言** | "最早发现 mock theta functions" — 他就是唯一发现者，不存在第一/第二争议 |
| **引语准确性** | Ramanujan 的名言几乎都是 Hardy 转述的。确认来源时标注"据 Hardy 回忆…" |
| **过度传奇化** | Ramanujan 的故事本身就足够传奇，不需要添加戏剧性修饰。事实已是最佳叙事 |
| **"他证明了…" vs "他断言了…"** | Ramanujan 提出的许多公式没有给出（现代意义下的）证明。用"断言""列出""提出"比"证明"更准确。 |
| **与印度的关系** | Ramanujan 是泰米尔人，生于英属印度。不要简单地写"印度数学家"——当时不存在独立的印度国家。封面国籍为 `英属印度`。 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

> **核心原则：Beamer 写完后，必须回到本地 Wikipedia 存档（page.md + metadata.json），逐项对照审核。**

### 终审执行流程

```
1. 打开 pages/Srinivasa_Ramanujan/page.md，从头到尾逐段阅读全文
2. 同时打开 Srinivasa_Ramanujan_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### 10 项终审清单

| # | 检查项 | 方法 | 高危信号 |
|:--:|------|------|---------|
| 1 | **事实性错误** | Beamer 中每个日期/人名/机构，与 page.md 逐条对照 | 任何与 Wikipedia 不一致的年份、地名、人名 |
| 2 | **翻译/术语错误** | 将所有数学术语与 Wikipedia 英文原词对照 | 概念性误译（如 mock → 模拟 vs 模仿） |
| 3 | **重大遗漏** | 扫描 Wikipedia 目录，列出 page.md 覆盖的主要成就 | 标志性贡献未提及（如 Rogers–Ramanujan 恒等式） |
| 4 | **结构性错误** | 检查时间线是否按生平顺序 | 时间跳跃混乱、因果倒置 |
| 5 | **编译告警** | 分析 `Overfull \hbox` 和 `Overfull \vbox` | vbox > 10pt 或 hbox > 50pt 需修复 |
| 6 | **引语来源** | 每个加引号的句子，必须在 page.md 或可靠来源中找到对应原文 | **中文引号内的句子无法在 Wikipedia 中找到** |
| 7 | **年份精确性** | 特别注意 1729 轶事年份（1919 或 1920）、FRS 年份（1918）、mock theta 年份（1920） | 年份标注不精确 |
| 8 | **人物关系** | metadata.json 与 Beamer 一致 | 把 Hardy 称为"博士导师"（Ramanujan 没有正式博士学位） |
| 9 | **荣誉/获奖** | FRS 1918、Trinity Fellow 1918，确认无误 | 获奖年份标错 |
| 10 | **笔记本细节** | Lost Notebook 的再发现者是 George Andrews（1976），确认此信息准确 | 把 Watson 或 Berndt 误称为发现者 |

### ⚠️ Ramanujan 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **1729 轶事的细节** | 无数版本在流传，其中很多是错的 | page.md 搜索 "1729" 或 "taxicab"，核对 Hardy 与 Ramanujan 的精确对话 |
| **mock theta functions 的定义** | 流行科普常过度简化 | page.md 搜索 "mock theta"，确认定义表述准确 |
| **Ramanujan 猜想与 Deligne** | Deligne 获 Fields 奖是因为 Weil 猜想，非直接因为 Ramanujan 猜想 | page.md 搜索 "Ramanujan conjecture"，同时在 Deligne 的 Wikipedia 页交叉验证 |
| **Lost Notebook 的"丢失"** | 它不是真的"丢失"，而是被遗忘在 Trinity 图书馆 | page.md 搜索 "Lost Notebook" 或 "Andrews"，确认再发现过程 |
| **日记/自述中的引语** | Ramanujan 留下的文字很少，大部分来自 Hardy 或他人的回忆 | 引用时标注"据 Hardy 回忆…""Ramanujan 曾说…" |
| **Ramanujan 在剑桥的孤独** | 容易过度渲染"受排挤"，实际上剑桥给予了他非常高的荣誉 | page.md 阅读 "Life in England" 章节，平衡叙述 |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

Ramanujan 的气质：**印度天才、孤独燃烧、直觉穿越时代、东方神秘与剑桥学术的碰撞、悲剧英雄**

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 永恒——mock theta 函数等了 82 年；笔记本至今仍有未解之谜 |
| ★★ | Through the Darkness | inspiring-electronic | `music_audio/inspiring-electronic/`（确认路径） | 黑暗中的光芒——32年的燃烧，贫困中诞生的数学奇迹 |
| ★★ | Lonesome | inspiring-electronic | `music_audio/inspiring-electronic/`（确认路径） | 孤独的旅者——从马德拉斯石板到剑桥病床，始终是一个局外人 |
| ★ | Expedition | alex-productions | `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` | 远征——跨越大洋，从英属印度到 Cambridge Trinity |

> **注意**：选曲时应按照 §15.7 按数学家气质推荐表进行最终选择。Ramanujan 的跨度包含"悲剧/黑暗/孤独"（Turing/Cantor 类 → Inspiring Electronic）和"史诗/远征"（Grothendieck/Weil 类 → Alex-Productions）两种气质。建议以深沉内敛为主、不应过于明亮或英雄式。

**操作**：复制选定的 `.wav` 到 `Srinivasa_Ramanujan/` 目录，`make video` 自动混入。

---

## 第 18 步：Makefile

复制任一已有 Makefile（如 `G_H_Hardy/Makefile` 或 `Bernhard_Riemann/Makefile`），修改：

```makefile
MAIN = Srinivasa_Ramanujan_zh
```

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. **Ramanujan 是数学史上唯一一个"没有受过正规训练却成为 FRS"的人** —— 这是他最独特的标签
> 2. **直觉来源的叙事是核心但也是最危险的** —— 尊重他的宗教信仰（Namagiri 女神），不以猎奇口吻叙述
> 3. **Hardy 的 25-30-80-100 必须在恰当位置出现** —— 这是 Hardy 对 Ramanujan 最终极的评价
> 4. **mock theta functions 是整个演示的情感高潮** —— 临终前，在病床上，向 Hardy 寄出最后一封信，描述了一种完全新型的函数。82 年后才被理解。
> 5. **1729 轶事是必讲点但也是最容易被讲错的** —— 核对每一个细节
> 6. **他留下的不是"已完成的工作"，而是"一个世纪的探索任务"** —— 三本笔记本 + Lost Notebook，至今仍在产生新论文
> 7. **结尾应提炼的核心思想**：他不是在"计算"数学——他是在"接收"数学。他的故事不是关于一个人如何学习数学，而是关于数学如何在一个人身上显现。
> 8. **与 Hardy 的关系** —— Hardy 认为发现 Ramanujan 是他一生最大的贡献。Ramanujan 的传记不可能不与 Hardy 交织。但演示的主视角应始终是 Ramanujan 本人。
> 9. **回避"东方神秘主义"的陈词滥调** —— 不要用"东方的直觉 vs 西方的理性"这种简单的二元对立。Ramanujan 的独特之处是个体性的，不是文化符号式的。
