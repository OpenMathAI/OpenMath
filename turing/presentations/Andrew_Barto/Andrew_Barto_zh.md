# Andrew Barto（安德鲁·巴托）立传提示词

> qid=Q4756294 · 1948 –（在世，卒日留白） · 美国计算机科学家 · 20/21 世纪 · 2024 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2024/Andrew Barto/`（index.html + metadata.json，**无 images 目录**）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**本篇无肖像**（页面无 images 目录），封面用装饰圆占位（内写 "RL" 或 "?" 均可，勿放无关照片）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆占位）+ 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 MDP 的 (S, A, R, P) 四元组示意 / agent-environment 交互回路示意），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Andrew Gehret Barto（中文惯称：安德鲁·巴托）
- **生卒**：1948 年生（页面仅载年份"1948 (age 77–78)"，**无出生月日，勿编造**）→ **在世，卒日留白**
- **国籍**：美国（American）
- **身份**：计算机科学家、麻省大学阿默斯特分校（UMass Amherst）计算机科学**荣休教授**（professor emeritus）、现代计算强化学习奠基人之一
- **教育轨迹**：
  - University of Michigan：**数学** BS（1970，with distinction；最初专业为**造船与轮机工程** naval architecture and engineering，后转向）
  - University of Michigan：MS、PhD（**计算机科学**，1975）；博士论文 *Cellular automata as models of natural systems*（细胞自动机作为自然系统模型）
- **博士导师**：Bernard P. Zeigler（页面 infobox 实载）
- **转折点**：读到 Michael Arbib、Warren Sturgis McCulloch、Walter Pitts 的著作后，转向"用计算机与数学为大脑建模"
- **研究领域**：计算机科学、强化学习、自适应系统、神经科学交叉

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **从造船工程到大脑建模**：Michigan 本科起初读 naval architecture，受 Arbib / McCulloch / Pitts 著作启发，转向数学与"用计算机为大脑建模"——五年内拿下 CS 博士。
2. **细胞自动机博士（1975）**：博士论文 *Cellular automata as models of natural systems*，导师 Zeigler——**博士论文不是强化学习**，勿混写。
3. **UMass 起点（1977）**：以博士后研究助理身份加入 UMass Amherst 信息与计算机科学学院；1982 副教授、1991 正教授、2007–2011 系主任；Neuroscience and Behavior 项目核心成员。
4. **Klopf 的神经元自适应思想**：入职 UMass 后加入一支以"神经元行为是人类智能之基"为纲领的研究组——该概念由计算机科学家 **A. Harry Klopf** 提出；Barto 带着博士生 Sutton 用数学将其发展为 AI 的新基础——这就是后来的**强化学习**。
5. **与 Sutton 的师生共创**：Richard Sutton 是 Barto 的**博士生**（页面明载 "was his PhD student"）；两人共同提出以 **Markov 决策过程（MDP）** 为数学基础的强化学习——关键突破是：传统 MDP 理论假设 agent 知道全部环境信息，而他们的方法**允许环境与奖励均未知**，使该类算法可广泛应用于各种问题。
6. **自主（自适应）学习实验室**：在 UMass 共同主持 Autonomous Learning Laboratory（初名 **Adaptive Network Laboratory**），孕育了强化学习的多个关键思想。
7. **教科书《Reinforcement Learning: An Introduction》**：与 Sutton 合著，MIT Press 1998 初版、2018 第二版——两人被公认的现代强化学习奠基之作（合著事实在 Sutton 篇同样写，但本篇侧重"导师与实验室"视角）。
8. **从学术到世界**：强化学习在学术界持续发展，首批重大现实应用之一是 Google **AlphaGo**（基于该概念击败人类顶尖冠军）——写"首批重大应用之一"，勿写"首个应用"；Barto 与 Sutton 被广泛誉为现代强化学习先驱，该技术是当代 AI 浪潮的基石。
9. **著述**：发表逾 100 篇论文/章节；与 Jennie Si、Warren Powell、Don Wunch II 合编 *Handbook of Learning and Approximate Dynamic Programming*（Wiley-IEEE Press, 2004）。
10. **荣誉**：IEEE Neural Network Society Pioneer Award（2004）、IJCAI Award for Research Excellence（2017，获奖引语见 §5）、UMass Neurosciences Lifetime Achievement Award（2019）。
11. **2024 图灵奖**：2025 年 3 月 5 日 ACM 宣布，与昔日博士生 **Richard S. Sutton** 共享，获奖理由（ACM citation 整句）："**For developing the conceptual and algorithmic foundations of reinforcement learning.**"

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（强化学习 — 蓝） | `#2E5A9E` | MDP 数学基础 / agent 决策 |
| 分类色 2（神经元自适应 — 青绿） | `#1E8E8E` | Klopf 思想 / 大脑建模 |
| 分类色 3（教科书与教育 — 琥珀） | `#D9A441` | RL: An Introduction / 师生传承 |
| 分类色 4（细胞自动机与自适应系统 — 玫瑰） | `#C0395B` | 1975 博士论文 / 自适应实验室 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和网格节点（稀疏小圆点 + 细连线），呼应「agent 在未知环境中试错、以奖励回传更新」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：厚重 / 奠基（现代强化学习的拓荒与回望）
- **选定曲目**：Alex-Productions **Empire Collapse**（manifest 预分配，直接沿用），匹配"从神经元自适应一路奠基到 AI 浪潮"的厚重叙事。
- **落地文件**：`turing/presentations/Andrew_Barto/EmpireCollapse.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「强化学习奠基人 · 美国」+ Barto 1948–（在世）+ 右上装饰圆占位 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1948–至今 生平纵览
4. **早年：从造船工程到大脑建模**（1948–1970）：naval architecture 起点、Arbib/McCulloch/Pitts 的启发、转数学
5. **Michigan 博士：细胞自动机**（1970–1975）：导师 Zeigler、论文 Cellular automata as models of natural systems
6. **UMass 起点（1977）**：博士后入职、副教授 1982 / 正教授 1991 / 系主任 2007–2011
7. **Klopf 的神经元自适应思想**：大脑作为智能之基的概念源头
8. **与 Sutton：师生共创强化学习（1980s）**：Sutton 是其博士生、共同将 Klopf 概念数学化为 AI 新基础
9. **MDP 数学基础**：agent-环境交互回路公式框；关键突破=环境与奖励均可未知
10. **自主（自适应）学习实验室**：Adaptive Network Laboratory → Autonomous Learning Laboratory，RL 关键思想的摇篮
11. **教科书《Reinforcement Learning: An Introduction》**（1998 / 2018）：现代 RL 的标准教材
12. **从学术到世界：AlphaGo 与 AI 浪潮**：首批重大应用之一、现代 AI 的技术基石
13. **荣誉**：Pioneer Award 2004 / IJCAI 2017（含引语）/ UMass 2019 / AAAS & IEEE Fellow
14. **2024 图灵奖：师生共享**：2025-03-05 宣布、ACM citation 整句引用
15. **结尾**：在世的奠基人、强化学习——从边缘到 AI 中心的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **出生日期**：页面仅载"1948 (age 77–78)"，**无出生月日**——写作 `b. 1948`，勿编造精确日期。
- **在世**：Barto 在世，**死亡日期一律留白**，勿写卒年。
- **博士论文是细胞自动机**（1975），**不是**强化学习——勿把 RL 写进他的博士论文。
- **本科专业**：Michigan 数学 BS（1970），最初专业是 naval architecture and engineering（造船与轮机）——是"转向"叙事，勿写成"一直学数学"。
- **师承方向**：Sutton 是 **Barto 的博士生**（页面明载）——勿写反；Barto 的博士导师是 Bernard P. Zeigler（页面 infobox 实载）。
- **Klopf 定位**：A. Harry Klopf 是"神经元行为作为智能基础"概念的提出者，Barto/Sutton 是将其数学化并发展为 AI 基础的人——勿把概念原创归给 Barto，也勿把 Klopf 写成导师。
- **AlphaGo 表述**："one of its first major real world applications"——写"首批重大现实应用**之一**"，勿写"首个应用"。
- **获奖年份口径**：infobox与页面均标 Turing Award **2024**，正文写"In 2025, he received the Turing Award"（2025-03-05 公布）——统一写"**2024 年图灵奖（2025 年 3 月 5 日公布）**"，勿混写。
- **获奖理由整句**："For developing the conceptual and algorithmic foundations of reinforcement learning."——整句引用，勿意译改写。
- **共享结构**：与 Sutton 共享（师生同奖）——本篇侧重 Barto：神经元自适应起点 / 细胞自动机博士 / UMass 实验室 / 导师视角；算法体系（TD 学习、Dyna、options、policy gradient、Bitter Lesson）**留给 Sutton 篇**，本篇不展开。
- **实验室名**：初名 Adaptive Network Laboratory，后为 Autonomous Learning Laboratory——勿倒置。
- **IJCAI 2017 引语**（页面原载，可用）："Professor Barto is recognized for his groundbreaking and impactful research in both the theory and application of reinforcement learning."
- **荣誉边界**：AAAS Fellow、IEEE Fellow & Senior Member、AAAI 与 Society for Neuroscience 会员（页面实载）；**无** National Medal、无 Nobel——勿编造。
- **肖像**：页面**无 images 目录**——无肖像，装饰圆占位，勿下载无关照片充当。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 巴托（或 安德鲁·巴托） | 待写入 |
| name_en | Andrew Barto | 待写入 |
| birth_date | 1948（无月日） | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | reinforcement learning / adaptive systems / computer science | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Bernard P. Zeigler（Michigan，infobox 实载）
- **博士生**：Richard S. Sutton（2024 图灵奖共享者）、Amy McGovern（infobox 实载）
- **合作者**：Richard Sutton（《Reinforcement Learning: An Introduction》合著）；Jennie Si / Warren Powell / Don Wunch II（Handbook 合编）
- **思想影响**：A. Harry Klopf（神经元自适应概念提出者）、Michael Arbib / Warren McCulloch / Walter Pitts（著作启发其转向；非导师关系，标注 influence，禁写成师承）
- 其余关系页面无载，禁写。

## 8. 奖项清单

- Turing Award（2024，与 Richard S. Sutton 共享；2025-03-05 公布；citation 见 §5）
- IEEE Neural Network Society Pioneer Award（2004）
- IJCAI Award for Research Excellence（2017，含引语）
- UMass Neurosciences Lifetime Achievement Award（2019）
- Fellow：AAAS；Fellow & Senior Member：IEEE
- 会员：American Association for Artificial Intelligence（AAAI）、Society for Neuroscience

## 9. 机构清单

- 教育：University of Michigan（数学 BS 1970；MS；计算机科学 PhD 1975）
- 任职：University of Massachusetts Amherst（1977 博士后研究助理 → 1982 副教授 → 1991 正教授 → 2007–2011 系主任 → 荣休教授）；Neuroscience and Behavior 项目核心成员；Autonomous Learning Laboratory 共同主持

## 10. 终审清单

- [ ] 生卒 1948（无月日）/ 在世留白，勿编造精确日期或卒年
- [ ] 博士论文=细胞自动机（1975、Michigan、导师 Zeigler），非 RL
- [ ] 本科"naval architecture → 数学"转向叙事准确
- [ ] Sutton 是 Barto 博士生，师生同奖表述准确
- [ ] Klopf 是概念提出者，Barto/Sutton 是数学化推进者
- [ ] AlphaGo 写"首批重大应用之一"
- [ ] 获奖口径"2024 图灵奖（2025-03-05 公布）"，citation 整句引用
- [ ] 实验室名 Adaptive Network → Autonomous Learning 顺序正确
- [ ] 算法体系细节（TD/Dyna/options/policy gradient/Bitter Lesson）留在 Sutton 篇，本篇不展开
- [ ] 封面装饰圆占位（无肖像），国籍徽章「美国」，底部状态栏 `美国 | UMass Amherst · Michigan | Turing 2024`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2024/Andrew Barto/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：页面无 images 目录——装饰圆占位；Review-1 核对未误用无关照片
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语（IJCAI 2017 citation、ACM Turing citation）必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与共享奖同伴 Sutton 篇格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
