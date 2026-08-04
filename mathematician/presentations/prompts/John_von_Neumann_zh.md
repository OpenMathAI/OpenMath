# 约翰·冯·诺依曼 (John von Neumann) 立传提示词

> 本提示词严格遵循 [数学家立传工作指南.md](./数学家立传工作指南.md)，以 Weyl、Weil 等成品为参考模板。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: John von Neumann (1903–1957)
- **气质关键词**: **计算机架构之父、博弈论之父、量子力学数学奠基人、曼哈顿计划核心、20世纪最广谱的天才**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本：
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/John_von_Neumann/`
- **参考模板**: `weyl/`, `weil/`, `grothendieck/`, `kolmogorov/` 等完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/数学家立传工作指南.md`

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/John_von_Neumann/`

输出以下信息供校验：

- **生卒日期**：1903-12-28 ~ 1957-02-08，享年 53 岁
- **国籍**：匈牙利 → 美国（1937 年入籍）
- **出生地**：Budapest（布达佩斯），匈牙利王国
- **死亡地**：Walter Reed Army Medical Hospital, Washington, D.C.  ⚠️ **安葬于** Princeton Cemetery — 死亡地与安葬地不同！
- **博士导师**：Lipót Fejér（布达佩斯大学, 1926 年获博士学位）
- **博士论文**：1925，《Az általános halmazelmélet axiomatikus felépítése》（一般集合论的公理化构造）—— 引入 von Neumann 层级和正则公理
- **主要任职机构**：
  - 1927–1929: 柏林大学（Privatdozent, 史上最年轻）
  - 1929–1930: 汉堡大学（Privatdozent）
  - 1930–1933: 普林斯顿大学（访问讲师 → 教授）
  - 1933–1957: 普林斯顿高等研究院（IAS）—— 创始教授（年仅 29 岁）
  - 1943–1945: Los Alamos 实验室（曼哈顿计划核心数学家）
  - 1954–1957: 美国原子能委员会委员
- **关键荣誉**：
  - 1938: Bôcher Memorial Prize
  - 1946: Medal for Merit, Navy Distinguished Civilian Service Award
  - 1955: 美国原子能委员会委员（艾森豪威尔总统任命）
  - 1956: Medal of Freedom, Enrico Fermi Award, Albert Einstein Award
  - 1957: Carl-Gustaf Rossby Research Medal
  - 月球环形山 von Neumann crater 以他命名
- **重要合作者/同事/学生**：
  - 导师与合作者: David Hilbert, Hermann Weyl, Eugene Wigner
  - 曼哈顿计划同事: J. Robert Oppenheimer, Edward Teller, Stanisław Ulam, Enrico Fermi
  - IAS 同事: Einstein, Gödel, Weyl, Veblen
  - 博弈论合作者: Oskar Morgenstern
  - 学生: Donald B. Gillies, Israel Halperin；受其深刻影响: Paul Halmos, Peter Lax, Benoit Mandelbrot
  - "火星人"群体: Wigner, Teller, Szilard — 四位匈牙利裔天才

### 关键时间线（15–20 个节点）：
- 1903: 生于布达佩斯富裕犹太银行家庭，父亲 Miksa 是银行家，拥有法学博士；1913 年受封匈牙利贵族
- 1914: 入读 Fasori Evangélikus Gimnázium（"火星人工厂"）
- 1921: 18 岁，发表第一篇数学论文；同时为满足父亲实用主义要求，决定主修化学工程
- 1921–1923: 柏林大学学习化学，同时在布达佩斯大学攻数学博士
- 1923–1926: ETH Zurich 化学工程学位 + 布达佩斯大学数学博士 —— 三校同修
- 1925: 博士论文《一般集合论的公理化构造》—— 引入 von Neumann 层级和正则公理
- 1926: 获 Rockefeller 资助赴哥廷根大学，成为 Hilbert 的助手
- 1927: 完成任教资格论文（habilitation），成为柏林大学史上最年轻 Privatdozent
- 1927–1929: 发表 von Neumann 代数基础论文、与 Wigner 合作量子力学数学基础、证明极小极大定理
- 1932: 出版《量子力学的数学基础》—— 首次严格证明 Hilbert 空间框架下量子力学的自洽性
- 1933: 年仅 29 岁成为 IAS 创始教授（最年轻的一位）
- 1937: 入籍美国
- 1943–1945: 曼哈顿计划 — 内爆式钚弹的激波流体动力学计算
- 1944: 出版《博弈论与经济行为》（与 Oskar Morgenstern 合著）
- 1945: 撰写 EDVAC 报告初稿（"First Draft"）—— 存储程序架构的蓝图
- 1946–1952: 参与氢弹设计（Teller-Ulam 方案）；推动 IAS 计算机 MANIAC 的建造
- 1949: 提出自复制自动机理论 —— 早于 DNA 双螺旋的发现
- 1955: 诊断出癌症（骨癌/胰腺癌/前列腺癌，来源对原发位置说法不一）；被总统任命为原子能委员会委员
- 1956: 获 Medal of Freedom、Enrico Fermi Award
- 1957: 2 月 8 日在华盛顿 Walter Reed 陆军医院逝世，安葬于 Princeton Cemetery

### 人格特质线索：
- "Johnny 和别人不一样，别人是聪明，他是另一种物种" —— 同事对他的普遍评价
- 过目不忘的超凡记忆力——传说能背诵整本电话簿
- 同时掌握匈牙利语、法语、德语、英语、意大利语、拉丁语、古希腊语
- 在嘈杂环境中工作效率最高——据说在 Princeton 因播放德国进行曲音量过大被邻居投诉
- 热衷派对，彻夜参加聚会后仍能清晨 8:30 准时授课
- 对同事和学生极其慷慨——Wigner 说他"非正式指导的工作量可能超过任何现代数学家"
- 临终前仍能一字不差背诵歌德《浮士德》
- Pascal's wager: 临终受洗，引用帕斯卡赌注

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 集合论 | von Neumann 层级 (V = ⋃ Vα) — 现代集合论标准框架；正则公理；NBG 公理系统 | 1925 |
| 量子力学 | Hilbert 空间数学自洽性证明；《量子力学的数学基础》(1932) | 1927–1932 |
| 算子代数 | von Neumann 代数 (W*-代数) — 算子理论核心工具 | 1929–1936 |
| 博弈论 | 极小极大定理 (1928)；《博弈论与经济行为》(1944, 与 Morgenstern) | 1928–1944 |
| 遍历理论 | von Neumann 平均遍历定理 (1931–1932) | 1931–1932 |
| 计算机科学 | EDVAC 报告 (1945) — 存储程序架构；MANIAC 计算机 (1951) | 1945–1951 |
| Monte Carlo 方法 | 与 Ulam 共同系统化随机模拟方法 | 1940s–1950s |
| 核武器 | 曼哈顿计划内爆计算；氢弹 Teller-Ulam 方案数学支持 | 1943–1952 |
| 元胞自动机 | 自复制自动机理论 (1949) — 29 状态通用构造器，早于 DNA 发现 | 1949 |
| 数值分析 | 有限精度计算、矩阵求逆、特征值计算、气象预报 | 1940s–1950s |

### ★ 冯·诺依曼独有的叙事线索

1. **"比计算机更快的人"** — von Neumann 的思维速度是传奇级别的。他能在脑中完成大多数同事需要纸笔才能完成的计算。他的同事说："他思考的速度和计算机一样快 —— 在计算机被发明之前。"
2. **三校同修** — 为满足父亲实用主义要求，同时在 ETH Zurich 学化学工程、在柏林大学听课、在布达佩斯大学攻数学博士。1926 年三线全部毕业。这种并行处理能力本身就是传奇。
3. **从 Hilbert 到核弹的弧线** — von Neumann 是 Hilbert 形式主义的忠实继承者，也是将数学暴力应用于战争的第一人。这条弧线代表了 20 世纪数学最深刻的伦理张力。
4. **核弹与博弈论并行** — von Neumann 在曼哈顿计划期间同时构建了"毁灭的数学"（核弹内爆计算）和"理性的数学"（博弈论）。他是少数同时在两个极端工作的数学家。
5. **"火星人"的故事** — von Neumann, Wigner, Teller, Szilard —— 四位匈牙利裔科学家在 Los Alamos 被称为"火星人"。他们都毕业于布达佩斯的 Fasori Gimnázium。
6. **自复制自动机 —— 比 DNA 更早的洞见** — 1949 年提出元胞自动机自复制理论，比 Watson 和 Crick 发现 DNA 双螺旋(1953)早了四年。他在完全不知道 DNA 存在的情况下，用数学推导出了生命复制的逻辑必要条件。
7. **MANIAC 和 Monte Carlo** — von Neumann 建造了 IAS 的 MANIAC 计算机，并在上面运行了历史上第一个 Monte Carlo 模拟。他将随机抽样变成了现代科学计算的基石方法。
8. **临终背诵浮士德** — 随着癌症恶化，他仍能一字不差地背诵歌德《浮士德》。这是他脑海中最后留存的光芒。

### 人物关系

- **David Hilbert（导师兼灵感来源）** — 哥廷根时期导师，继承了 Hilbert 的形式主义和公理化方法
- **Hermann Weyl** — IAS 同事，1926 年冬在哥廷根街头与 Noether 一起讨论超复数系统
- **Eugene Wigner** — 中学同学、终生挚友、1963 年诺贝尔物理学奖得主
- **Oskar Morgenstern** — 经济学家，《博弈论与经济行为》合著者
- **Stanisław Ulam** — 最亲密的美国朋友，Monte Carlo 方法共同发明者
- **J. Robert Oppenheimer** — 曼哈顿计划科学总监
- **Edward Teller** — "氢弹之父"，核武器设计密切合作者
- **Kurt Gödel** — IAS 同事，数理逻辑和集合论上的对话者
- **Albert Einstein** — IAS 同事，对 von Neumann 智力评价极高
- **Leó Szilard** — 另一位"火星人"，核链式反应概念发明者

---

## 第 5 步：设计配色方案

- **建议配色：深黑 + 电路绿 + 冷蓝** —— 计算机理性的冷峻 + 核时代科学张力 + 纯数学的抽象光芒
- 需要与已有配色完全不同！
  - Hilbert：普鲁士蓝 + 金
  - Grothendieck：深靛 + 金
  - Serre：勃艮第红 + 象牙暖金
  - Noether：深紫罗兰 + 暗玫瑰金
  - Riemann：墨绿 + 银灰
  - Kolmogorov：深松绿 + 古铜金
  - von Neumann：深黑 + 电路绿
  - Weyl：深琥珀金 + 星夜紫
  - Cartan：法兰西几何紫 + 象牙
  - Weil：勃艮第深红 + 石板暖灰
- 四个分类色，对应 von Neumann 的四大支柱：
  - **badgecomputer** (计算机/Monte Carlo/自动机) — 电路绿 `#00C853`
  - **badgephysics** (量子力学/核武器/流体动力学) — 冷蓝 `#2979FF`
  - **badgegame** (博弈论/核威慑/经济学) — 暖铜 `#B87333`
  - **badgemath** (集合论/算子代数/遍历理论) — 银灰 `#78909C`

---

## 第 6 步：规划幻灯片序列（建议 17 页）

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《比计算机更快的人》 / John von Neumann 1903–1957
02  为什么 von Neumann 是另一种天才 — 集合论→量子力学→计算机→核弹→博弈论→自动机

=== 早年 ===
03  布达佩斯的神童 (1903–1926) — 传说 8 岁通晓微积分 · 三校同修 · "火星人"的起点
04  哥廷根与量子力学 (1926–1933) — Hilbert 的助手 · 量子力学的数学基础 · IAS 创始教授

=== 纯数学 ===
05  集合论与算子代数 — von Neumann 层级 · von Neumann 代数 · 遍历定理

=== 博弈论与计算机 ===
06  博弈论的诞生 (1928/1944) — 极小极大定理 · 《博弈论与经济行为》
07  计算机之父 — EDVAC 报告 (1945) — 存储程序架构的蓝图
08  MANIAC 与 Monte Carlo — 第一代计算机 · 随机数的力量

=== 战争岁月 ===
09  原子弹与数学 — 洛斯阿拉莫斯 — 内爆设计的数学
10  氢弹与战略博弈 — 核威慑 · 博弈论在冷战中的应用

=== 跨学科传奇 ===
11  "火星人" — 匈牙利裔科学家群体 — von Neumann · Wigner · Teller · Szilard
12  自复制自动机 — 生命的数学理论 — 早于 DNA 双螺旋发现

=== 终曲与遗产 ===
13  53 岁的终曲 (1957) — 癌症 · 《计算机与人脑》· 背诵浮士德
14  冯·诺依曼的遗产 — 从你的手机到核武器，他的思想无处不在

=== 结尾 ===
15  升起海水 — "他是第一个理解'计算'本身可以成为一门科学的数学家"
16  结束页 — "他思考的速度和计算机一样快 —— 在计算机被发明之前。"
```

---

## 第 9 步：史实审查

### 冯·诺依曼特有的史实陷阱（★ 高危）

| 陷阱类型 | 高危点 |
|---------|--------|
| **"计算机之父"的单一归属** | von Neumann 的贡献在于**存储程序架构**（EDVAC 报告），而非硬件发明。ENIAC 工程由 Eckert 和 Mauchly 完成，Turing 更早提出了通用机理论。Beamer 中应写"存储程序架构之父"。 |
| **"8 岁学会微积分"是传说** | Wikipedia 明确标注为 "According to a **legend**"。Beamer 中必须写"传说 8 岁通晓微积分"而非陈述事实。 |
| **癌症类型的模糊性** | Wikipedia 说癌种来自骨骼/胰腺/前列腺，**来源对原发位置说法不一**。不要在 Beamer 中断言是某一种特定癌症。 |
| **辐射病因的确定性** | Wikipedia 写 "The malignancy **may have been** caused by exposure to radiation"。是可能性而非确定性。不要写"几乎确定"。 |
| **死亡地点 vs 安葬地点** | 死于 Washington, D.C. 的 Walter Reed Army Medical Hospital，**安葬于** Princeton Cemetery。两者不同，务必区分。 |
| **Pólya 引语** | "Johnny 是唯一让我感到害怕的学生" —— 此引语在 Wikipedia page.md 中**无记载**。可用 Szegő 初次见面落泪的轶事代替（Wikipedia 有记载）。 |
| **"我们必须建造计算机"引语** | "我们必须建造计算机，因为原子弹需要它" —— **Wikipedia 无此引语**。删除或间接转述。 |
| **"同一个夏天"叙事** | "核弹和博弈论 —— 他在同一个夏天同时建立毁灭的数学和理性的数学" —— 叙事有效但不可作为精确史实。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| stored-program architecture | 存储程序架构 | von Neumann 的核心贡献 |
| von Neumann algebra | von Neumann 代数 | 也作 W*-代数 |
| minimax theorem | 极小极大定理 | 博弈论的数学基石 |
| cellular automaton | 元胞自动机 | 也译"细胞自动机" |
| Monte Carlo method | Monte Carlo 方法 | 随机模拟方法 |
| explosive lens | 爆炸透镜 | 曼哈顿计划核心贡献 |
| axiom of foundation | 正则公理 | 也译"基础公理" |
| game theory | 博弈论 | 不要译作"游戏理论" |
| ergodic theorem | 遍历定理 | von Neumann 版和 Birkhoff 版并列为两大基石 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"计算机之父"争议** | 改为"存储程序计算机架构之父"——这是无可争议的贡献 |
| **"天才"过度使用** | 通过具体事例（三校同修、自复制自动机早于 DNA）而非标签来展现 |
| **伪引语** | von Neumann 逸闻多来自二手回忆（Ulam, Wigner），需格外注意可验证性 |
| **曼哈顿计划的道德判断** | 客观呈现，不美化也不谴责。聚焦"纯数学家→炸弹设计师"的智力弧线 |
| **死亡叙事的戏剧化** | "临终背诵浮士德"和 Pascal's wager 有可靠来源，但不要过度渲染 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/John_von_Neumann/page.md，从头到尾逐段阅读全文
2. 同时打开 John_von_Neumann_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ von Neumann 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **"计算机之父"的绝对化** | 争议性称号 | page.md 搜索 "EDVAC" "stored-program" |
| **癌种断言** | Wikipedia 明确说 3 种可能 | page.md 搜索 "cancer" "pancreas" "skeleton" |
| **"8 岁学会微积分"** | Wikipedia 标注为 legend | page.md 搜索 "legend" "eight" |
| **辐射病因确定性** | Wikipedia 说 "may have been" | page.md 搜索 "radiation" "malignancy" |
| **Pólya 引语** | page.md 中无此引语 | page.md 搜索 "Pólya" "Szegő" |
| **死亡地点** | 死于 D.C. 医院，葬于 Princeton | page.md 搜索 "died" "buried" |
| **"我们必须建造计算机"** | 无 Wikipedia 来源 | page.md 中搜索相关段落 |

### 优先级定义

| 优先级 | 定义 | von Neumann 实际案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | 癌种断言为 2 种而非 3 种；死亡地点写 Princeton |
| 🟡 P1 | **来源存疑/模糊** | "8 岁学会微积分"未标注为传说；Pólya 引语；无法验证的引语 |
| 🟢 P2 | **重要遗漏** | 气象预报先驱；ICBM 导弹项目；Navy Distinguished Civilian Service Award |
| ⚪ P3 | **可选补充** | 月球环形山命名；Pascal's wager 临终细节 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. von Neumann 的独特性在于**广度**——没有人在纯数学、物理、计算机、经济学、核武器所有维度上同时达到世界顶级
> 2. EDVAC 报告的叙事是计算机史的核心节点：**存储程序架构 = von Neumann 最确切的遗产**
> 3. 核弹与博弈论并行的叙事是情感张力最强的亮点
> 4. 自复制自动机早于 DNA——这是最能展现 von Neumann 超前思维的故事
> 5. "火星人"群体是独树一帜的叙事角度——Fasori Gimnázium 的传奇
> 6. 尸体地点和死亡地点不同：Washington D.C. (死) ≠ Princeton (葬)
> 7. 结尾主题句的核心意象："他思考的速度和计算机一样快 —— 在计算机被发明之前"