# 诺伯特·维纳 (Norbert Wiener) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Ramanujan、Weyl、Hardy 等成品提示词为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Norbert Wiener (1894–1964)
- **气质关键词**: **控制论之父、神童、Wiener 过程、人类与机器之间的思想家、数学向工程与生物扩散的枢纽**
- **Wikipedia 页面**: ✅ 已下载并完成 Review
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Norbert_Wiener/`
  - Wikipedia 英文条目: `Norbert Wiener`
- **Beamer 文件**: `mathematician/presentations/Norbert_Wiener/Norbert_Wiener_zh.tex` (461行, 14页)
  - 编译: `make distclean && make` — 238KB PDF, 零警告
  - **Review 状态**: ✅ 第1轮完成 — 肖像+国籍+格式检查；第2轮完成 — 逐页 Wikipedia 交叉核查
- **Review 发现的关键修正**:
  - P0: 封面页脚添加逝世地 Stockholm（Wikipedia: "died on March 18, 1964, aged 69, in Stockholm"）
  - 验证: 全部14页事实与 Wikipedia 一致（神童年表、欧洲游学、Wiener过程1923、Paley-Wiener 1934、防空火炮1941、控制论1948、Macy会议、A Scientist Rebels 1947、轶事等）
- **参考模板**: `ramanujan/`, `hardy/`, `neumann/`, `shannon/` 的完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Norbert_Wiener/`

输出以下信息供校验：

- **全名**: Norbert Wiener
- **生卒日期**: 1894-11-26 ~ 1964-03-18，享年 **69** 岁
- **国籍**: 🇺🇸 United States（美国）
- **出生地**: Columbia, Missouri（哥伦比亚市，密苏里州），美国
- **逝世地**: Stockholm（斯德哥尔摩），Sweden（瑞典）—— 心脏病发作
- **死因**: 心脏病发作（heart attack），在斯德哥尔摩访问期间
- **博士导师**: Karl Schmidt（名义）、Josiah Royce（哲学指导）
- **博士论文**: 1913, *A Comparison Between the Treatment of the Algebra of Relatives by Schroeder and that by Whitehead and Russell*（Schröder与Whitehead & Russell的关系代数处理之比较）
  - 该论文首次用集合论公理化定义有序对（ordered pair）
- **教育经历**:
  - Ayer High School → 11 岁毕业
  - Tufts College → 14 岁获 BA in Mathematics
  - Cornell University → 短暂学习哲学
  - Harvard University → 17 岁获 MA, 19 岁获 PhD
  - 博士后: Cambridge（Russell, Hardy）, Göttingen（Hilbert, Landau, Husserl）
- **主要任职机构**:
  - 1919–1960: MIT（终其职业生涯）
  - 1918: Aberdeen Proving Ground（弹道学研究）
  - 1935–1936: 清华大学访问教授
  - 1953–1954: Tata Institute of Fundamental Research（印度）
- **关键荣誉**:
  - 1933: Bôcher Memorial Prize（AMS 分析奖）
  - 1936: ICM Plenary Speaker（奥斯陆）
  - 1950: ICM Plenary Speaker（剑桥, MA）
  - 1963: National Medal of Science（国家科学奖章）—— 由总统 Johnson 在白宫颁发
  - 1965: National Book Award（《God & Golem, Inc.》）
  - 多项荣誉博士学位
- **重要合作者/同事/学生**:
  - 导师: Bertrand Russell, G.H. Hardy, David Hilbert, Edmund Husserl
  - MIT 同事: Claude Shannon, John von Neumann
  - 合作者: Arturo Rosenblueth（生理学家）, Julian Bigelow（工程师）
  - Macy 会议: Margaret Mead, Gregory Bateson, Warren McCulloch, Walter Pitts
  - 博士生: Amar Bose（Bose 音响创始人）, Norman Levinson, Shikao Ikehara, George Zames
- **关键作品**:
  - *Cybernetics: Or Control and Communication in the Animal and the Machine* (1948)
  - *The Human Use of Human Beings* (1950)
  - *I Am a Mathematician* (1956, 自传)
  - *God & Golem, Inc.* (1964)

### 关键时间线（15–20 个节点）：

- 1894: 11月26日生于密苏里州哥伦比亚市，立陶宛犹太移民家庭。父亲 Leo Wiener 是哈佛斯拉夫语教授
- 1897–1903: 3 岁开始阅读；7 岁读完达尔文和但丁；父亲在家实施极其严苛的早教——失败时打耳光
- 1903: 10 岁，撰写短文《无知论》（The Theory of Ignorance），质疑"人类知识的无限性"
- 1906: 11 岁从 Ayer High School 毕业
- 1909: 14 岁获 Tufts College 数学学士学位
- 1911: 17 岁获哈佛大学哲学硕士学位
- 1913: 19 岁获哈佛大学 PhD —— 论文首次用集合论公理化定义有序对
- 1914: 赴欧洲游学 —— Cambridge（Russell, Hardy）, Göttingen（Hilbert, Landau, Husserl）
- 1918: 加入 Aberdeen Proving Ground 从事弹道学；战后入伍参军（一战结束前数日退伍）
- 1919: 被 MIT 聘为数学讲师 —— 原因之一是哈佛反犹主义拒其长聘（Birkhoff 因素）
- 1920s–1930s: 在调和分析、Tauberian 定理、Brownian 运动等领域做出奠基性贡献
- 1926: 与 Margaret Engemann 结婚；Guggenheim 学者再访欧洲
- 1933: 获 Bôcher Memorial Prize
- 1935–1936: 清华大学访问教授
- 1940s: 二战期间为 NDRC 工作——研究防空火炮自动瞄准，发明 Wiener 滤波器
- 1943: 与 Rosenblueth & Bigelow 发表"Behavior, Purpose and Teleology"——控制论的前奏
- 1948: 出版《控制论》(Cybernetics) —— 创立控制论这门新学科。"信息就是信息，不是物质也不是能量。"
- 1946–1950s: 参与 Macy 会议；推动认知科学与人工智能的早期发展
- 1950s: 冷战期间因与苏联学者交流被怀疑；在印度政府担任顾问
- 1963: 获 National Medal of Science
- 1964: 3月18日，在斯德哥尔摩心脏病发作逝世，享年 69 岁

### 人格特质线索：

- **神童的创伤** —— 父亲 Leo Wiener 对儿子实施极度高压教育。每天数小时高强度学习，犯任何错误就打耳光。维纳晚年自传中称之为"emotional abuse"。但他也承认父亲的博学为自己奠定了无与伦比的基础。
- **心不在焉的天才** —— MIT 校园传奇人物。著名轶事：搬新家后妻女怕他找不到路，派女儿去接他。他问小女孩"你知道诺伯特·维纳的家在哪里吗？" 小女孩回答："是的，爸爸，妈妈让我来接你。"
- **另一则轶事** —— 在校园走路时被学生拦下问 Fourier 分析问题。他拿出纸详细解答后，学生感激离开。维纳叫住他："等一下——我碰到你时是往哪个方向走的？" 学生指出方向后，维纳说："好，那说明我已经吃过午饭了。"
- **伦理自觉者** —— 二战后，维纳拒绝一切军方资助和军事项目。在 1947 年《大西洋月刊》发表"A Scientist Rebels"，呼吁科学家承担伦理责任。这与 von Neumann 形成鲜明对比。
- **控制论的社会愿景** —— 他相信自动化可以提高生活水平、终结经济落后。但也对自动化武器的伦理后果发出警告。
- **与 von Neumann、Shannon 的关系** —— 三位 MIT/Princeton 天才各有不同气质。von Neumann 是实用主义通才，Shannon 是信息论的孤独天才，Wiener 是控制论的社会哲学家。
- **药物依赖** —— 自传中承认一生滥用 Benzedrine（苯丙胺），未充分意识到其危害。

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 概率论 | Wiener 过程 —— 布朗运动的严格数学模型 | 1923 |
| 调和分析 | Wiener–Khinchin 定理 —— 功率谱密度的数学基础 | 1930s |
| 调和分析 | Paley–Wiener 定理 —— Fourier 变换与解析函数的桥梁 | 1934 |
| 调和分析 | 广义调和分析 (Generalized Harmonic Analysis) | 1930 |
| 数理逻辑 | 首次用集合论公理化定义有序对 —— 关系理论无需额外公理 | 1914 |
| 滤波理论 | Wiener 滤波器 —— 二战防空火炮的副产品，信号处理的基石 | 1942–1945 |
| 控制论 | 《控制论》(Cybernetics, 1948) —— 创立跨学科新领域 | 1948 |
| 信息论 | 将信号建模为随机过程 —— 独立于 Shannon 的信息理论 | 1940s |
| 认知科学 | 推动 Macy 会议 —— 神经科学、计算机科学、AI 的早期熔炉 | 1946–1953 |
| Tauberian 定理 | Wiener's Tauberian Theorem —— 素数定理新证明的基础 | 1932 |
| 数学物理 | 量子力学的随机解释 | — |

### ★ 维纳独有的叙事线索

1. **神童的炼成与创伤** —— 3 岁阅读、11 岁高中毕业、14 岁学士、19 岁 PhD。这不是童话——父亲的"自制教学法"本质是心理虐待。维纳的一生始终在天才与创伤之间摇摆。这是一个"天才养成"的反面教材。

2. **"信息就是信息，不是物质也不是能量。"** —— 《控制论》中最著名的一句话。维纳看到了信息作为一种独立于物理世界的存在形式。他的洞见远超同时代人——我们生活在信息时代，而维纳是第一个理解'信息'本身可以是一门科学的人之一。

3. **Wiener 过程——从花粉到金融** —— 1923 年用严格的测度论语言定义了布朗运动的数学模型。80 年后，Black–Scholes 期权定价公式依赖的正是 Wiener 过程。维纳当年不会想到自己的抽象概率论会成为万亿级金融衍生品市场的数学基础。

4. **防空火炮→控制论** —— 1940 年代为 NDRC 研究防空火炮自动瞄准，发明 Wiener 滤波器。这次经历让他认识到反馈机制的普遍性——动物、机器、社会系统都依赖反馈。1948 年，他将这些思想系统化为《控制论》。

5. **控制论的跨学科革命** —— 维纳的影响远超出数学。Margaret Mead（人类学）、Gregory Bateson（系统论）、Warren McCulloch（神经科学）、Walter Pitts（认知科学）——控制论在 1950 年代是连接一切学科的通用语言。

6. **伦理自觉 vs 军事工业复合体** —— 维纳是二战科学家中最早对军事化的科学发出警告的人之一。"A Scientist Rebels"（1947）是一篇开拓性的伦理宣言。他拒绝为军方工作的姿态与 von Neumann 的鹰派立场形成尖锐对比。

7. **"人类对人的使用"** —— 1950 年出版的《人有人的用处》(The Human Use of Human Beings) 以通俗笔调阐述了控制论的社会意义。维纳警告自动化可能导致大规模失业和社会撕裂——这些问题在 70 多年后的今天正是 AI 时代最核心的社会议题。

8. **MIT 的传奇** —— 维纳在 MIT 度过了整个职业生涯。他的照片曾在 Infinite Corridor 上挂了数十年（2017 年移除）。他是 MIT 数学系从教学型向研究型转变的关键人物。

---

## 人物关系

- **Leo Wiener（父亲）** — 哈佛斯拉夫语教授，制造了维纳的"神童"也制造了他的创伤
- **Bertrand Russell（博士后导师）** — 剑桥期间指导其数理逻辑研究
- **G.H. Hardy** — 剑桥期间的另一位导师
- **David Hilbert / Edmund Landau** — 哥廷根时期的老师
- **Edmund Husserl** — 哥廷根期间听了三门现象学课程
- **Arturo Rosenblueth（合作者）** — 墨西哥生理学家，控制论思想的共同孕育者
- **Julian Bigelow（合作者）** — 工程师，共同发表"Behavior, Purpose and Teleology"(1943)
- **John von Neumann** — MIT 同事、控制论与计算机思想的对话者；战后在核武和军事伦理上立场相反
- **Claude Shannon** — MIT 同事，信息论的另一位奠基人
- **Amar Bose（学生）** — Bose 音响创始人
- **Margaret Mead / Gregory Bateson** — Macy 会议的参与者，控制论的人类学影响
- **Warren McCulloch / Walter Pitts** — 神经科学与认知科学的先驱；后与维纳决裂（可能因维纳妻子之故）
- **Vannevar Bush** — NDRC 负责人，邀请维纳参与战时研究

---

## 第 5 步：设计配色方案

- **建议配色：电路绿 + 石墨灰 + 信号白 + 控制黑** —— 机器与控制 + 数学的冷峻 + 信息时代的预示
- 需要与已有配色完全不同！
  - Hilbert：普鲁士蓝 + 金
  - Ramanujan：檀香暖橙 + 印度赭石红
  - Hardy：剑桥蓝 + 板球绿 + 牛津金
  - Weyl：深琥珀金 + 星夜紫
  - Shannon：信号蓝绿 + 电路金
  - von Neumann：深黑 + 电路绿

- 主要色值建议：
  | 用途 | 色名 | 建议色值 | 说明 |
  |------|------|---------|------|
  | 背景 | `bgmain` | `#F5F7F5` | 极淡电路白 —— 实验室工作台的颜色 |
  | 主色 | `coverprimary` | `#0D1F0D` | 深墨绿 —— 控制论的冷峻与深邃 |
  | 强调色 | `coveraccent` | `#2D8C3C` | 电路绿 —— 机器与信号的活力 |
  | 深色文本 | `coverdark` | `#1A2A1A` | 石墨暗绿 |
  | 浅色文本 | `covermuted` | `#5C7A5C` | 灰绿 |

- 四个分类色，对应维纳的四大支柱：
  - **badgeCybernetics** (控制论/AI/反馈) — 电路绿 `#2D8C3C` —— "信息就是信息"
  - **badgeMathematics** (Wiener过程/调和分析/逻辑) — 石墨灰 `#4A5568` —— 数学的冷峻精确
  - **badgeEthics** (伦理/社会/责任) — 警示金 `#C9A84C` —— 科学家的良知
  - **badgeLegacy** (遗产/跨学科影响) — 信号蓝 `#1B5C8B` —— 从工程到生物学

---

## 第 6 步：规划幻灯片序列（建议 16–18 页）

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《维纳：秩序与混乱之间的控制论之父》 / Norbert Wiener 1894–1964
02  为什么维纳独一无二 — 神童·Wiener过程·控制论创始人·信息时代的预言家

=== 早年 ===
03  神童的炼成与创伤 (1894–1913) — 3岁阅读·11岁高中·14岁学士·19岁PhD·父亲的高压教育
04  欧洲之旅 (1914–1915) — Russell·Hardy·Hilbert·Husserl·数理逻辑与有序对

=== 数学成就 ===
05  Wiener 过程 (1923) — 布朗运动的严格数学·从花粉到金融
06  调和分析的建筑师 — Wiener–Khinchin·Paley–Wiener·Tauberian定理

=== 战争与控制论 ===
07  从防空火炮到 Wiener 滤波 (1940–1945) — 战争中的数学家·信号处理的基石
08  控制论的诞生 (1948) — 《Cybernetics》·反馈机制·"信息就是信息，不是物质也不是能量"

=== 控制论时代 ===
09  人、机器与社会 — Macy会议·认知科学·AI的预言
10  人类对人的使用 (1950) — 自动化·伦理·失业·70年前的警告

=== 伦理 ===
11  科学家的良知 — "A Scientist Rebels"·拒绝军方·与von Neumann的对立

=== 人格 ===
12  MIT 的传奇 — 心不在焉·轶事·药物依赖·教授中的教授

=== 遗产 ===
13  控制论的遗产 — AI·机器人学·自动控制·系统生物学
14  Wiener 过程的遗产 — 金融数学·随机分析·物理学

=== 结尾 ===
15  结束页 — 主题句："信息就是信息，不是物质也不是能量。"
```

---

## 第 9 步：史实审查

### 维纳特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **Wiener ≠ Weiner** | "i 在 e 前" —— 经常被拼错。Wiener，不是 Weiner。 |
| **"计算机的发明者"** | 维纳不是计算机的发明者。他贡献的是计算机的**理论基础**（控制论、信息处理、反馈）。 |
| **"控制论之父"** | 准确，但需注明控制论的希腊词源 `kybernetes`（舵手）。他创造了这个词，但思想根源可追溯到 Leibniz、Maxwell、Gibbs。 |
| **Wiener 过程 ≠ 一般随机过程** | Wiener 过程特指连续时间、连续状态、独立增量、Gauss 分布的随机过程——即布朗运动的数学模型。 |
| **Harvard 反犹主义** | 维纳未能获得哈佛长期教职，他自己归因于反犹主义和 Birkhoff 的个人敌意。这一说法的客观性有争议，但维纳本人深信不疑。 |
| **与 McCulloch/Pitts 决裂** | 控制论团队突然解散，传闻是维纳妻子 Margaret 驱动的。维纳之后再未联系他们。这影响了对认知科学早期史的理解。 |
| **Benzedrine 滥用** | 维纳自述使用苯丙胺一生。不要用"吸毒"等贬义词。用"药物依赖"或"他自己承认滥用兴奋剂"。 |
| **National Medal of Science** | 1963 年获奖（总统 Johnson 颁发），1964 年 1 月白宫典礼。维纳两个月后去世。不是死后追授。 |
| **Macy 会议** | 正确的全称是 Macy Conferences on Cybernetics（1946–1953）。不要省略"控制论"。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| cybernetics | 控制论 | 也译"赛博论"，但"控制论"已是标准 |
| Wiener process | Wiener 过程 / 维纳过程 | 金融数学中也称"Brownian motion model" |
| Wiener filter | Wiener 滤波器 | 信号处理的核心概念 |
| Wiener–Khinchin theorem | Wiener–Khinchin 定理 | Khinchin 是苏联数学家 |
| Paley–Wiener theorem | Paley–Wiener 定理 | R.E.A.C. Paley 1933 年死于雪崩，年仅 26 岁 |
| feedback | 反馈 | 控制论的核心概念 |
| The Human Use of Human Beings | 《人有人的用处》 | 1950 年出版的通俗读物 |
| ordered pair | 有序对 | 维纳 1914 年首次用集合论公理化定义 |
| Tauberian theorem | Tauberian 定理 | 维纳的 Tauberian 定理是素数定理新证明的关键 |
| Aberdeen Proving Ground | 阿伯丁试验场 | 美国陆军弹道学研究基地 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一次/第一个"断言** | "第一个提出控制论" — 改为"创始了控制论这门学科" |
| **学科归属** | Wiener 是数学家，但他的影响遍及计算机科学、生物学、哲学、工程学。不限定为"纯数学家"。 |
| **von Neumann 对比** | 不要将维纳与 von Neumann 简单对立为"好人vs坏人"。两人的伦理立场差异有复杂背景。 |
| **父亲 Leo Wiener** | 强调父亲的天才和博学，但也不回避其教育方式的严酷性。不要将 Leo 简化为"坏父亲"。 |
| **伪引语** | "信息就是信息"来自 *Cybernetics* 原文。精准确认原文：*"Information is information, not matter or energy. No materialism which does not admit this can survive at the present day."* |
| **神童叙事** | 不要将维纳简化为"神童成功故事"。他的自传明确揭示神童经历的心理代价。 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

> 详见 Ramanujan 或 Weyl 提示词中的完整终审流程。

### ⚠️ Wiener 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **Wiener 拼写** | i-e 顺序常被颠倒 | 全文搜索 "Weiner" |
| **"信息就是信息"引语** | 引用频率极高但常有删节 | 对照 *Cybernetics* 原文 |
| **有序对定义年份** | 1914(发表) vs 1913(论文完成) | page.md 搜索 "ordered pair" |
| **自杀未遂？** | 部分来源称维纳有抑郁症和自杀倾向，Wikipedia 未明确记载 | 如提及，必须基于可靠来源 |
| **Norbert Wiener Prize** | 1967 年由 MIT 数学系设立，AMS + SIAM 联合颁发 | 不要写成"他设立" |
| **清华大学访问** | 1935–1936，与李郁荣合作 | 不要遗漏这段中美数学交流史 |

---

## 第 14 步：背景音乐选择 ✅

- **选定曲目**: **Timeless** — Alex-Productions (132k views, 最高受众)
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - "沉稳" 匹配控制论的冷峻理性与 Wiener 的智性气质 —— 他不像 von Neumann 那样是鹰派英雄，更像一个跨越时代的先知
  - "纪录片" 匹配传记体叙事 —— 从神童创伤到 AI 遗产的 14 页旅程
  - "Timeless" = 永恒 —— 信息时代在他笔下首先成为一门科学，"他比时代早了 50 年"
  - 不像 Expedition 过于"史诗"（Wiener 不是征服者），不像 Through the Darkness 过于"黑暗"（创伤是底色但不是基调）
- **备选** (未采用):
  - ★★ Expedition — "远征式叙事" 匹配跨学科旅程，但"史诗"标签过重
  - ★ Through the Darkness — "黑暗/推进" 匹配神童创伤与战时研究，但整体过于灰暗
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/Norbert_Wiener/Timeless.wav`
- **时长**: 128 秒 (≈2.1 分钟) > 14 页 × 7 秒 = 98 秒 → ffmpeg `-shortest` 自动对齐
- **Makefile**: `BGM = $(wildcard *.wav)` — 自动检测并混入

---

## 第 18 步：Makefile

复制 Hardy/Makefile，修改：

```makefile
MAIN = Norbert_Wiener_zh
```

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. **"信息就是信息，不是物质也不是能量。"** —— 这是维纳最核心的一句话，必须贯穿整个演示
> 2. **神童 ≠ 童话** —— 父亲的压力教育是双刃剑。不回避创伤叙事，但也不将 Leo 妖魔化
> 3. **控制论 ≠ 冷门学科** —— 它是 AI、机器人学、系统生物学、认知科学的共同祖先
> 4. **Wiener 过程** —— 从花粉的随机运动到 Black–Scholes 期权定价。80 年后的回响
> 5. **伦理自觉是他的独特标签** —— 在 von Neumann、Shannon 等同代人中，维纳是唯一公开拒绝军方的
> 6. **心不在焉的轶事** —— 适当加入，展现他的人格魅力，但不过度渲染
> 7. **结尾主题句**："信息就是信息，不是物质也不是能量。任何一种不承认这一点的唯物主义，在今天都无法生存。"