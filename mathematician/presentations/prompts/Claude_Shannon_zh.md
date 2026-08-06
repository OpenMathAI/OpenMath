# 香农 (Claude Shannon) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, milnor, morse, zariski, whitney, chevalley, hopf, chern, deligne, witt, fisher 的版式。

---

## 背景信息

- **目标**: Claude Elwood Shannon (1916–2001)
- **气质关键词**: **信息论之父、数字时代的真正奠基人、比特的命名者、独轮车上的魔术师、贝尔实验室和MIT的天才发明家**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Claude_Shannon/`

## 第 0 步：Wikipedia 校验

- **全名**：Claude Elwood Shannon
- **生卒**：1916-04-30 ~ 2001-02-24，享年 84 岁
- **国籍**：美国
- **出生地**：Petoskey（实际在密歇根州 Gaylord 长大）—— Petoskey 是医院所在地
- **去世地**：Medford, Massachusetts (⚠️ 原提示词未提及)
- **教育**：Gaylord 高中 → 密歇根大学（BS 电机工程 + BS 数学，1936 双学位）→ MIT（MS 1937 电机工程 → PhD 1940 数学）
- **博士导师**：Frank Lauren Hitchcock + **Vannevar Bush**（⚠️ 原提示词遗漏 Bush！Bush 建议他去 Cold Spring Harbor 做遗传学博士）
- **博士论文**：1940，《An Algebra for Theoretical Genetics》——在 Cold Spring Harbor Laboratory 完成。将代数框架应用于群体遗传学。因 Shannon 失去兴趣而未发表——但包含了重要原创结果。
- **硕士论文**：1937，《A Symbolic Analysis of Relay and Switching Circuits》——被 Howard Gardner 称为"可能是一个世纪以来最重要、最著名的硕士论文"。Akira Nakashima 在同年独立发现了类似原理，但 Shannon 的更抽象和数学化。
- **任职**：IAS Princeton 研究员 (1940–1941) → 贝尔实验室 (1941–1972) → MIT 教授 (1956–1978)
- **IAS 经历**：1940 年在 IAS 与 Hermann Weyl, John von Neumann, Albert Einstein, Kurt Gödel 交流——跨学科自由探索促成了信息论
- **荣誉**：Alfred Noble 奖 (1939, 硕士论文)、IEEE 荣誉奖章 (1966)、美国国家科学奖章 (1966)、Kyoto 奖 (1985)、Claude E. Shannon 奖 (1973, 首届)、英国皇家学会外籍院士、Marconi 奖 (2000)
- **婚姻**：Norma Levor (1940–1941 离异) → Betty Shannon (1949–2001)
- **远程表亲**：Thomas Edison——两人都是殖民领袖 John Ogden (1609–1682) 的后代
- **学生**：Ivan Sutherland (计算机图形学之父), Danny Hillis (Connection Machine), Elwyn Berlekamp (编码理论), Leonard Kleinrock (ARPANET/互联网先驱)
- **合作者**：Warren Weaver (科普推广, 不是合作证明!)——1949 年合著书《通信的数学理论》，Weaver 写了科普前言
- **图灵会面**：1943 年在贝尔实验室茶歇时见面。图灵给他看了 1936 年图灵机论文。两人讨论了"机器能否思考"——但图灵没透露 Bletchley Park 的工作。

### 时间线
- 1916-04-30: 生于密歇根 Petoskey（在 Gaylord 长大）
- 1932: Gaylord 高中毕业。童年偶像：Thomas Edison（后来发现是远亲）
- 1932–1936: 密歇根大学——电机工程 + 数学双学士学位
- 1937: MIT 硕士论文——布尔代数 → 数字电路。"可能是一个世纪以来最重要的硕士论文"
- 1939: 硕士论文获 Alfred Noble 奖
- 1940: MIT 数学博士——遗传学代数（Cold Spring Harbor Laboratory）
- 1940: IAS Princeton——与 Weyl, von Neumann, Einstein, Gödel 交流
- 1941: 加入贝尔实验室
- 1942: 发明信号流图 (signal-flow graph)
- 1943: 与 Alan Turing 在贝尔实验室见面——讨论了图灵机
- 1945: 《密码学的通信理论》(Communication Theory of Secrecy Systems)——"宣布古典密码学的终结和现代密码学的开始"
- 1948: 《通信的数学理论》——信息论的诞生。在 Bell System Technical Journal 分两期发表
- 1949: 与 Weaver 合著出版——Weaver 写科普前言
- 1950: 国际象棋编程论文——AI 先驱
- 1950: Theseus——能走迷宫的机械老鼠（第一个"通过试错学习"的电子设备）
- 1951: CIA 特别密码学顾问组成员
- 1956: MIT 教授；**Dartmouth 研讨会**——AI 的奠基事件——与 McCarthy, Minsky, Rochester 共同组织
- 1961: 关于"垃圾邮件"的幽默演讲
- 1966: IEEE 荣誉奖章 + 国家科学奖章（同一年！）
- 1978: 从 MIT 退休
- 1985: Kyoto 奖——基础科学类
- 2001-02-24: 在 Medford, MA 因阿尔茨海默病去世

### 人格画像
Shannon 可能是 20 世纪最"好玩"的天才。他在贝尔实验室的走廊里骑着独轮车。他发明了能走迷宫的机械老鼠 Theseus、平衡的独轮车、喷火的小号、火箭驱动的飞盘。他的同事说："他'玩'出了一门新科学。"他不在乎论文和基金——他在乎的是"这个东西有趣吗？"他在 MIT 的办公室里堆满了玩具。他的最大遗产不是任何具体的定理——而是证明了**玩耍是创造力的最高形式**。"My mind wanders and I try to think about things that interest me"——他这样描述自己的工作方式。

但不要被他的玩具所迷惑。他在二战期间为美国国防部做密码分析和火力控制——用数学拯救生命。他的密码学论文（1945 年写成，1949 年公开）至今仍是现代密码学的基础。他还是可穿戴计算机的发明者之一——1961 年他和 Ed Thorp（后来的量化投资先驱）一起发明了能预测轮盘赌的隐藏计算机。

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 信息论 | **Shannon 熵** —— 信息的量化，$H = -\sum p_i \log_2 p_i$ | 1948 |
| 信息论 | **信源编码定理** —— 无损压缩的理论极限 | 1948 |
| 信息论 | **信道容量定理** —— 噪声信道下可靠传输的最大速率 | 1948 |
| 信息论 | **Nyquist–Shannon 采样定理** | 1948 |
| 数字电路 | **布尔代数 → 开关电路** —— 数字电路的理论基础 | 1937 |
| 密码学 | **完美保密 (一次一密)** —— 现代密码学的数学基础 | 1945 |
| 密码学 | **混淆与扩散** —— 现代分组密码的核心原则 | 1945 |
| 通信 | **脉冲编码调制 (PCM)** —— 与 Bernard Oliver 共同发明 | 1940s |
| AI | **国际象棋编程** —— 第一个完整的棋局评估算法 | 1950 |
| AI | **Dartmouth 研讨会** (1956) —— AI 作为独立学科的诞生 | 1956 |
| 图论 | **信号流图** | 1942 |
| 数学 | **Shannon 数** —— 国际象棋下界 $10^{120}$ | 1950 |
| 数学 | **Shannon 展开** —— 布尔函数分解 | — |
| 发明 | **Theseus** —— 第一个通过试错学习的电子设备 (AI 前身) | 1950 |
| 发明 | **可穿戴计算机** —— 与 Ed Thorp 的轮盘赌预测器 | 1961 |

### ★ 叙事主线
1. **比特的诞生 (1948)** — Shannon 的《通信的数学理论》被《科学美国人》称为"信息时代的大宪章"。他定义了信息的基本单位——bit。在此之前，信息是模糊的直觉；之后，它是可以量化、压缩、传输的数学实体。
2. **硕士论文改变世界 (1937)** — 22 岁的 Shannon 证明了布尔代数可以实现所有数字逻辑电路。这篇硕士论文被 Howard Gardner 称为"可能是一个世纪以来最重要的硕士论文"。它是数字革命的"出生证明"——从你的手机到互联网，一切都始于这篇论文。
3. **Shannon 熵** — $H = -\sum p_i \log_2 p_i$。这个公式出现在从通信工程到统计力学、从神经科学到黑洞物理的各个领域。它与热力学熵形式相同——von Neumann 建议他用"熵"这个名字，说："反正没有人真正懂熵，你在辩论中就有优势了。"
4. **图灵的下午茶 (1943)** — Shannon 和图灵在贝尔实验室的茶歇时见面。图灵给他看了 1936 年的图灵机论文。两人讨论了机器能否思考——但图灵不能透露 Bletchley Park 的 Enigma 破译工作。这是两个定义了数字时代的头脑之间唯一的已知会面。
5. **密码学奠基人** — 他的 1945 年论文《密码学的通信理论》被描述为"一个转折点——宣布古典密码学的终结和现代密码学的开始"。完美保密、混淆与扩散——Shannon 定义了现代密码学的基本概念。
6. **独轮车上的魔术师** — Theseus（走迷宫的老鼠）、喷火小号、火箭飞盘、独轮车、杂耍——他的发明清单像个玩具店。但正是这种"玩耍"的心态让他能跨越学科边界——从数学到工程到生物到密码学。玩耍不是他的副业——玩耍是他的方法论。
7. **Dartmouth 1956: AI 的诞生** — Shannon 与 McCarthy, Minsky, Rochester 共同组织了 Dartmouth 夏季研讨会——这被公认为人工智能学科的诞生事件。他是那个时代的召集人。
8. **可穿戴计算机与 Ed Thorp** — 1961 年，Shannon 和 Ed Thorp 发明了隐藏的计算机来预测轮盘赌。这是世界上第一台可穿戴计算机——不是为了健康监测，而是为了击败赌场。Thorp 后来用量化投资赚了数十亿美元。

## ⚠️ 史实陷阱
- **博士论文** — 遗传学代数（不是信息论！）。信息论的种子在贝尔实验室萌芽，不是在博士论文中。在 Cold Spring Harbor Lab 完成。
- **博士导师** — **两人**！Frank Lauren Hitchcock 是正式导师，但 Vannevar Bush 也是学术指导者。Bush 建议他去 Cold Spring Harbor 做遗传学论文。
- **Shannon 熵 ≠ 热力学熵** — 形式相同，概念不同。von Neumann 建议用"熵"这个名字——不是因为它们是同一个东西，而是因为相似性。
- **"bit" 的命名** — John W. Tukey 在 1947 年创造了 "bit" 作为 "binary digit" 的缩写。Shannon 在他的 1948 年论文中采纳了它，让它成为世界通用的术语。所以：Tukey 命名，Shannon 推广。（⚠️ 原提示词说"bit 来自 Shannon"不够精确！）
- **与图灵的会面** — 1943 年贝尔实验室茶歇时间。图灵给 Shannon 看了 1936 年图灵机论文。两人讨论了机器思考。但图灵没有透露 Bletchley Park 的工作（当时是绝密）。这次会面发生在 1943 年 1–3 月，持续约 2 个月。
- **信号流图 (1942)** — Shannon 在分析差分分析仪（模拟计算机）时发明了这个图论工具——它后来成为控制系统工程的标准语言。
- **硕士论文 ≠ 唯一的先驱** — Akira Nakashima (中岛章) 在同一年独立发现了类似结果。Shannon 的优势在于更一般化、更抽象的数学框架。
- **Weaver 不是共同作者** — Weaver 写了 1949 年书的前言（科普解释），但没有参与 Shannon 的数学工作。"Shannon–Weaver 模型"这个名称有时被使用，但 Shannon 是唯一作者。

## ⚠️ 终审高危
| 高危点 | 正确值 | 常见错误 |
|--------|--------|----------|
| 博士导师 | Hitchcock + Vannevar Bush | 只有 Hitchcock |
| 博士论文 | 遗传学代数, Cold Spring Harbor Lab | "信息论" |
| bit 命名 | Tukey 1947 命名, Shannon 推广 | "Shannon 创造了 bit" |
| 图灵会面 | 1943 茶歇, 图灵给看图灵机论文 | "一起工作" |
| IAS 经历 | 1940, 见 Weyl/von Neumann/Einstein/Gödel | 遗漏 |
| 密码学论文 | 1945 写成, 1949 公开 | 遗漏 |
| Weaver 角色 | 科普推广, 非共同作者 | "合作证明" |
| 可穿戴计算机 | 1961, 与 Ed Thorp | 遗漏 |
| Dartmouth | 1956, AI 奠基事件 | 遗漏 |
| Thomas Edison | 远程表亲 | 遗漏 |

## 配色：电路绿 + 比特黑 + 熵紫 + 玩耍橙
- **badgeInfo** (信息论) — 电路绿 `#00BFA5`
- **badgeCircuit** (数字电路) — 比特黑 `#1F2937`
- **badgeCrypto** (密码学/熵) — 熵紫 `#6A0572`
- **badgePlay** (玩耍/发明) — 暖橙 `#FF7F50`
- **coveraccent** — 电路绿 `#00BFA5`
- **coverprimary** — 墨色 `#111827`
- **bgmain** — 暖象牙白 `RGB{248,246,243}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
### 1. 封面 — 《香农：信息时代的奠基人》
- Claude Shannon · 1916 — 2001
- 比特 · 信息熵 · 密码学 · AI
- IEEE Medal 1966 · National Medal of Science 1966 · Kyoto 1985
- 美国 · Bell Labs 1941-72 · MIT 1956-78

### 2. Hook — 四面板：信息熵 · 数字电路 · 密码学 · AI先驱
- 底部："他量化了'信息'，定义了比特——一个人缔造了信息时代的基础。"

### 3. 早年：Gaylord 的少年发明家 (1916–1936)
- 无线电船、铁丝电报……童年偶像 Edison（后来发现是远亲）
- 密歇根大学电机+数学双学士

### 4. 硕士论文：布尔代数 → 数字电路 (1937)
- "可能是一个世纪以来最重要的硕士论文"
- 1939 Alfred Noble 奖

### 5. 博士：遗传学与 IAS (1938–1941)
- 遗传学代数，Cold Spring Harbor Lab
- IAS Princeton 与 Weyl/von Neumann/Einstein/Gödel 交流
- 博士导师: Hitchcock + Vannevar Bush

### 6. 通信的数学理论 (1948) — 信息论的诞生
- Shannon 熵：H = -∑ p_i log₂ p_i
- von Neumann: "叫它熵——没人在讨论中能赢你"
- "信息时代的大宪章"

### 7. 信道容量定理 — 噪声下的通信极限
- 信源编码定理 + 信道编码定理
- Nyquist–Shannon 采样定理
- 这些定理定义了所有数字通信的理论极限

### 8. 密码学之父 (1945–1949) — 完美保密
- 1945 《密码学的通信理论》:"古典密码学的终结，现代密码学的开始"
- 完美保密 + 一次一密 + 混淆与扩散
- 这篇论文直到 DES 和 AES 都仍然是基础

### 9. 图灵在贝尔实验室 (1943) — 两个天才的下午茶
- Shannon 看了图灵 1936 论文
- 讨论机器思考——但图灵不能提 Enigma

### 10. Theseus 与 AI 先驱 (1950–1956)
- Theseus 走迷宫老鼠——第一个通过试错学习的电子设备
- 国际象棋编程——Shannon 数 10^120
- Dartmouth 1956——AI 诞生

### 11. 独轮车上的魔术师：玩耍的哲学
- Theseus, 喷火小号, 独轮车, 杂耍
- 可穿戴计算机 (1961, 与 Ed Thorp 轮盘赌)
- "玩耍是创造力的最高形式"

### 12. 二战贡献：火力控制与信号流图
- 防空火力控制系统
- 1942 发明信号流图
- Data Smoothing and Prediction (1945)

### 13. 贝尔实验室 → MIT (1941–1978) —— 37 年的黄金时代
- 贝尔实验室: 信息论 + 密码学
- MIT 1956–78: AI + 教学
- 学生：Sutherland, Hillis, Berlekamp, Kleinrock

### 14. 遗产：以 Shannon 命名的概念
- Shannon 熵 · 信道容量 · 采样定理 · Shannon–Fano 编码 · Shannon 展开 · Shannon 数 · Shannon–Hartley 定理 · 信源编码定理 · 信号流图

### 15. 结束页
- "My mind wanders and I try to think about things that interest me."
- Claude Shannon · 1916 — 2001

## 音乐: Fleeting Moments + Timeless

## Round 2 高危: bit 来自 Tukey、博士导师 Bush、图灵会面 1943、密码学论文 1945/1949、可穿戴计算机+Thorp、Dartmouth 1956、IAS 经历。

> **开始执行。**
