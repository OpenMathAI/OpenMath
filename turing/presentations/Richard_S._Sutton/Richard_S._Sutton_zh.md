# Richard S. Sutton（理查德·萨顿）立传提示词

> qid=Q7328833 · 1957/1958 –（在世，卒日留白） · 加拿大（美裔）计算机科学家 · 20/21 世纪 · 2024 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2024/Richard S. Sutton/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**有真实肖像**（见 §11 Review-1）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 加拿大`，可小注 American-born），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 TD 误差 / agent-environment 回路 / Dyna 三通路示意），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Richard Stuart Sutton，FRS、FRSC（中文惯称：理查德·萨顿）
- **生卒**：1957 **或** 1958 年生（页面两说"1957 or 1958 (age 68–69)"，勿二选一），生于俄亥俄州 Toledo（Toledo, Ohio），长于伊利诺伊州 Oak Brook（芝加哥近郊）→ **在世，卒日留白**
- **国籍**：2015 年起加拿大公民；此前为美国公民（2017 年见诸报道放弃美国国籍）
- **身份**：计算机科学家、University of Alberta 计算机科学教授、Alberta Machine Intelligence Institute（Amii）Fellow 兼首席科学顾问、Keen Technologies 研究科学家；**现代计算强化学习奠基人之一**、"the Father of Reinforcement Learning"（媒体称号，页面引用源标题实载）
- **教育轨迹**：
  - Stanford University：**心理学** BA（1978）
  - University of Massachusetts Amherst：计算机科学 MS（1980）、PhD（1984），**导师 Andrew Barto**
  - 博士论文 *Temporal credit assignment in reinforcement learning*（1984）——引入 **actor-critic 架构**与 temporal credit assignment
- **思想源头**：1970 年代受 **Harry Klopf** 影响——监督学习不足以解释智能行为，必需由"行为享乐面"驱动的试错学习；由此聚焦强化学习
- **研究领域**：人工智能、强化学习、机器学习、认知科学、计算机科学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **Toledo 出生的心理学学士**：Stanford 1978 心理学 BA——与 Barto 篇的"造船→数学"相对照，本篇开篇强调"心理学视角的 AI 人"。
2. **UMass 师承（1980–1984）**：MS/PhD 均师从 Andrew Barto；博士论文引入 actor-critic 架构与 temporal credit assignment；1980 年代初加入 Barto 的神经元自适应研究，与 Barto 用数学将 Klopf 概念发展为 AI 新基础——**强化学习由此得名**。
3. **TD 学习奠基（1988）**：论文 *Learning to predict by the methods of temporal differences*（Machine Learning 3, 9–44）——引入时序差分方法用于预测与控制，建立收敛性质与实用算法；TD 学习是 Sutton 的标志性贡献。
4. **Dyna 架构（1991）**：*Dyna, an integrated architecture for learning, planning, and reacting*（ACM SIGART Bulletin）——学习、规划、反应的整合架构。
5. **Options 框架（1999）**：与 Doina Precup、Satinder Singh 合著 *Between MDPs and semi-MDPs*（Artificial Intelligence 112, 181–211）——强化学习中的时间抽象框架。
6. **Policy gradient 奠基（2000）**：与 McAllester、Singh、Mansour 合著 *Policy Gradient Methods for Reinforcement Learning with Function Approximation*（NeurIPS 12）——页面称其为"co-authored the first modern policy gradient formulation with function approximation"（首个现代 policy gradient 形式化，页面原载可写）。
7. **GQ(λ)（2010）**：带资格迹的时序差分预测学习通用梯度算法（与 H. R. Maei，off-policy TD with gradients）。
8. **教科书《Reinforcement Learning: An Introduction》**：与 Andrew Barto 合著，MIT Press 1998 初版、2018 第二版（合著事实两篇都写，本篇侧重"体系化 RL 领域"视角）。
9. **The Bitter Lesson（2019）**：发表于 incompleteideas.net 的短文——批评 AI 界"building in how we think we think does not work in the long run"，主张"70 年的 AI 研究表明，利用算力的一般方法最终最有效、且大幅领先"，胜过依赖人类领域知识的路径（计算机视觉、语音识别、国际象棋、围棋皆然）。
10. **对 LLM 的立场与 Era of Experience**：他主张大语言模型无法"在岗学习"（learning on-the-job），需要新模型架构实现持续学习；专门训练阶段将不必要，agent 将即时学习——2025 年与 David Silver 合著 *Welcome to the Era of Experience*（Google DeepMind）。**这些是观点表述，写"他认为/argues"，勿写成事实断言。**
11. **与 John Carmack 的 AGI 合作（2023）**：两人宣布合作加速通用人工智能（AGI）开发。
12. **职业生涯纵览**：1984 UMass 博士后 → 1985–1994 GTE Laboratories（Waltham）principal member of technical staff → 1995–1998 UMass 高级研究科学家 → 1998–2002 AT&T Labs Shannon Laboratory → 2003 至今 Alberta 教授（协助创建 RLAI 实验室）→ 2017 协助创建 DeepMind Alberta（Edmonton）→ 2024 至今 Keen Technologies。
13. **荣誉**：AAAI Fellow（2001）、INNS President's Award（2003）、UMass Outstanding Achievement in Research（2013）、FRSC 皇家学会加拿大院士（2016）、FRS 英国皇家学会院士（2021）；**2024 图灵奖**（2025-03-05 公布，与 Andrew Barto 共享；citation 见 §5）。
14. **AlphaGo 与传承**：其博士生包括 David Silver（AlphaGo 核心人物——页面仅载师生关系，勿过度演绎）与 Doina Precup；AlphaGo 被页面列为强化学习首批重大现实应用之一。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（时序差分学习 — 蓝） | `#2E5A9E` | TD learning / GQ(λ) |
| 分类色 2（架构与算法 — 青绿） | `#1E8E8E` | Dyna / options / policy gradient |
| 分类色 3（思想宣言 — 琥珀） | `#D9A441` | The Bitter Lesson / Era of Experience |
| 分类色 4（师承与传承 — 玫瑰） | `#C0395B` | Barto 门下 / Silver、Precup / AlphaGo |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：上升折线（稀疏斜向线段 + 节点），呼应「时序差分：预测随时间逐步爬升收敛」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：攀升 / 登顶（从 TD 算法到 AI 浪潮之巅的上升叙事）
- **选定曲目**：Alex-Productions **Ascension**（manifest 预分配，直接沿用），匹配"算法一步步爬升、终成 AI 基石"的上行叙事。
- **落地文件**：`turing/presentations/Richard_S._Sutton/Ascension.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「强化学习之父 · 加拿大」+ Sutton 1957/58–（在世）+ 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1957/58–至今 生平纵览
4. **早年：Toledo 与 Stanford 心理学**（1957/58–1978）：俄亥俄出生、芝加哥近郊长大、Klopf 思想的启蒙
5. **UMass：师从 Barto**（1980–1984）：actor-critic 与 temporal credit assignment、RL 由此得名
6. **TD 学习奠基（1988）**：Learning to predict by the methods of temporal differences、收敛性质与实用算法
7. **Dyna：学习、规划与反应的整合（1991）**：架构示意公式框
8. **Options 与 policy gradient（1999 / 2000）**：时间抽象、与函数逼近结合的首个现代 policy gradient
9. **教科书《Reinforcement Learning: An Introduction》**（1998 / 2018）：与 Barto 合著、体系化 RL
10. **Alberta 岁月（2003–）**：RLAI 实验室、加拿大归乡、2015 入籍
11. **DeepMind 与 Keen（2017–）**：DeepMind Alberta、AlphaGo 的涟漪、2023 与 Carmack 的 AGI 合作
12. **The Bitter Lesson（2019）**：一般方法 × 算力 > 人类知识注入；引语标注出处
13. **Era of Experience（2025）**：对 LLM 的观点、与 Silver 合著——写"argues"，勿写成事实
14. **荣誉**：AAAI 2001 / INNS 2003 / FRSC 2016 / FRS 2021 / Turing 2024
15. **结尾**：在世的"RL 之父"、师生同奖的历史时刻

## 5. 史实陷阱与敏感点（终审必须检查）

- **出生年两说**：页面载"1957 or 1958"——写作 `1957/1958`，勿二选一、勿编造月日。
- **在世**：Sutton 在世，**死亡日期一律留白**。
- **国籍表述**：2015 年入籍加拿大、2017 年见诸报道放弃美国国籍——写"2015 年起加拿大公民（此前美国公民）"，封面国籍徽章用「加拿大」；勿简单写"美国人"或把弃籍渲染成政治叙事。
- **学位口径**：Stanford BA 是**心理学**（1978）——勿写成计算机/数学；PhD 是 UMass 计算机科学（1984、导师 Barto）。
- **师承方向**：Sutton 的博士导师是 **Andrew Barto**（勿写反）；"Sutton 是 Barto 的博士生"在两篇都实载可写。
- **博士论文内容**：引入 actor-critic 与 temporal credit assignment（1984）——勿把 TD(λ) 全书体系或 1988 TD 论文倒填进博士论文。
- **"first"表述**："first modern policy gradient formulation with function approximation"为页面原载，可写但注明范围（现代 + 函数逼近）；TD 学习写"奠基/引入"，勿泛化成"发明了机器学习"。
- **获奖年份口径**：infobox与页面均标 Turing Award **2024**，NYT 报道 2025-03-05——统一写"**2024 年图灵奖（2025 年 3 月 5 日公布）**"，勿混写。
- **获奖理由整句**："For developing the conceptual and algorithmic foundations of reinforcement learning."——整句引用，与 Barto 篇一致。
- **共享结构**：与 Barto 共享（师生同奖）——本篇侧重算法体系（TD/Dyna/options/policy gradient/GQ(λ)）与思想宣言（Bitter Lesson/Era of Experience）；Barto 篇侧重神经元自适应起点 / 细胞自动机 / UMass 实验室 / 导师视角。**禁写两人恩怨**（页面无载）。
- **The Bitter Lesson 引语**（页面原载，须标注出自该文）："building in how we think we think does not work in the long run"；"70 years of AI research [had shown] that general methods that leverage computation are ultimately the most effective, and by a large margin"。
- **人物引语**（页面引源实载，Amii 2025-03-05）："So I'm 67 years old, but I want to still try to do some amazing things."——可用，标注出处。
- **LLM 观点**：写"他认为/argues"（LLM 无法在岗学习、需要新架构、专门训练阶段将不必要）——**观点勿写成定论**；"LLMs are a dead end"是播客标题用语，勿写成 Sutton 原话断言。
- **DeepMind 时间**：2017 年起任 distinguished research scientist（时间线 2017–2023），2024 起 Keen Technologies——勿写"至今仍在 DeepMind"。
- **AlphaGo 归因**：页面写 AlphaGo 是 RL 首批重大现实应用之一、其博士生 Silver 为 AlphaGo 核心人物——师生关系实载，但**勿写"AlphaGo 由 Sutton 发明/主导"**。
- **肖像**：images 目录有两个候选（`500px-SD_2025_-_Richard_Sutton_01_cropped_.jpg` 近照 / `500px-Rich_Sutton_on_Reinforcement_Learning-_Alpha_Go_Zero_to_60.jpg`）；infobox 图注为 "Sutton at NeurIPS 2025"——Review-1 时目检两图择优（优先清晰正面近照）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 萨顿（或 理查德·萨顿） | 待写入 |
| name_en | Richard S. Sutton | 待写入 |
| birth_date | 1957 或 1958（页面两说） | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Canada（2015 起；原 United States） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | reinforcement learning / temporal difference learning / artificial intelligence | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Andrew Barto（UMass，2024 图灵奖共享者）
- **博士生**：David Silver、Doina Precup（infobox 实载）
- **合作者**：Andrew Barto（教科书合著）；Doina Precup / Satinder Singh（options）；David McAllester / Satinder Singh / Yishay Mansour（policy gradient）；H. R. Maei（GQ(λ)）；W. T. Miller III / P. J. Werbos（Neural Networks for Control 合编）；David Silver（Era of Experience 2025 合著）
- **产业合作**：John Carmack（2023 AGI 合作伙伴，标注 collaborator-industry 或 partner）
- **思想影响**：Harry Klopf（1970 年代思想源头，influence 非师承）

## 8. 奖项清单

- Turing Award（2024，与 Andrew Barto 共享；2025-03-05 公布；citation 见 §5）
- AAAI Fellow（2001；提名词页面原载："For significant contributions to many topics in machine learning, including reinforcement learning, temporal difference techniques, and neural networks."）
- INNS President's Award（International Neural Network Society，2003）
- UMass Amherst Outstanding Achievement in Research（2013）
- Fellow, Royal Society of Canada（FRSC，2016）
- Fellow, Royal Society（FRS，London，2021）

## 9. 机构清单

- 教育：Stanford University（心理学 BA 1978）、University of Massachusetts Amherst（MS 1980、PhD 1984）
- 任职：UMass Amherst 博士后（1984）→ GTE Laboratories（1985–1994）→ UMass 高级研究科学家（1995–1998）→ AT&T Labs Shannon Laboratory（1998–2002）→ University of Alberta 教授（2003–至今，RLAI 实验室创建者之一）→ Google DeepMind / DeepMind Alberta（2017–2023）→ Keen Technologies（2024–至今）；Amii Fellow 兼首席科学顾问

## 10. 终审清单

- [ ] 生年写作 1957/1958（页面两说），在世留白
- [ ] 国籍"2015 加拿大（此前美国、2017 弃籍见诸报道）"，封面徽章「加拿大」
- [ ] Stanford BA=心理学 1978；UMass PhD=CS 1984、导师 Barto
- [ ] 博士论文=actor-critic + temporal credit assignment（1984）
- [ ] TD 学习 1988 / Dyna 1991 / options 1999 / policy gradient 2000 / GQ(λ) 2010 年份准确
- [ ] 获奖口径"2024 图灵奖（2025-03-05 公布）"，citation 整句引用
- [ ] Bitter Lesson 两处引语标注出处；LLM 表述用"argues"
- [ ] 与 Barto 篇侧重分工明确，无恩怨渲染
- [ ] DeepMind 2017–2023、Keen 2024– 时间线准确
- [ ] 封面头像真实（Review-1 目检二选一），底部状态栏 `加拿大 | Alberta · DeepMind · Keen | Turing 2024`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2024/Richard S. Sutton/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：候选 `images/500px-SD_2025_-_Richard_Sutton_01_cropped_.jpg`（NeurIPS 2025 近照）或 `images/500px-Rich_Sutton_on_Reinforcement_Learning-_Alpha_Go_Zero_to_60.jpg`——目检择优；infobox 图注为 "Sutton at NeurIPS 2025"
- [ ] **国籍**：封面顶部徽章明示加拿大
- [ ] **引语核对**：引语（Bitter Lesson 两句、Amii 一句、AAAI 提名词、ACM Turing citation）必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与共享奖同伴 Barto 篇格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
