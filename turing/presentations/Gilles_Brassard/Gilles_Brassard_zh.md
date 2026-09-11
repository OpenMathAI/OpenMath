# Gilles Brassard（吉尔·布拉萨德）立传提示词

> qid=Q92938 · 1955-04-20 –（在世，卒日留白） · 加拿大计算机科学家 · 20/21 世纪 · 2025 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2025/Gilles Brassard/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**有真实肖像**（`Gilles_Brassard_2019_.jpg`，见 §11）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 BB84 协议四态示意 / teleportation 六作者论文框 / amplitude amplification 增益示意），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Gilles Brassard（中文惯称：吉尔·布拉萨德）
- **生卒**：1955-04-20 生于魁北克省蒙特利尔（Montreal, Quebec, Canada）→ **在世，卒日留白**
- **国籍**：加拿大（Canadian）
- **身份**：计算机科学家、蒙特利尔大学（Université de Montréal）教授（1988 年起正教授）、**Canada Research Chair**（2001 年起）；量子信息科学世界最早的开创者之一（Royal Society 提名词原载 "one of the earliest pioneers of quantum information science in the world"）
- **家庭**：妻子 Lise Raymond（infobox Spouse 实载）
- **教育轨迹**：
  - Université de Montréal：BSc、MSc
  - Cornell University：**计算机科学 PhD（1979）**，方向**密码学**，导师 **John Hopcroft**；博士论文 *Relativized Cryptography*
- **Known for**（页面实载列表，择用）：quantum cryptography、quantum counting algorithm、quantum teleportation、quantum entanglement distillation、quantum pseudo-telepathy、amplitude amplification、commitment scheme、**BB84**、BHT algorithm
- **研究领域**：量子密码学、量子计算、密码学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **蒙特利尔本地少年**：1955-04-20 生于蒙特利尔——本篇开篇与 Bennett 篇的"纽约—Brandeis 化学"相对照，强调魁北克本地成长、UdeM 本硕、再赴 Cornell。
2. **Cornell 密码学博士（1979）**：师从 John Hopcroft，论文 *Relativized Cryptography*——**密码学出身**是他日后把 BB84 做成"可用的密码系统"的底色（区别于 Bennett 篇的物理出身）。
3. **蒙特利尔大学学术生涯**：1988 年起正教授、2001 年起 Canada Research Chair——一生一校。
4. **BB84（1984，与 Bennett）**："In 1984, together with Charles H. Bennett, he invented the BB84 protocol for quantum cryptography"——与 IBM 的 Bennett 共同发明量子密码协议 BB84（Wiesner 理念来源见 Bennett 篇，本篇按"共同发明"口径写）。
5. **Cascade 纠错协议**：将 BB84 工作扩展至 **Cascade error correction protocol**——对量子密码信号因窃听产生的噪声进行高效检测与纠正——让 BB84 从理念走向可用系统（本篇侧重，区别于 Bennett 篇）。
6. **隐私放大（privacy amplification）**：与 Bennett、Crépeau、Maurer 合著 *Generalized privacy amplification*（IEEE Trans. Inf. Theory, 1995）——Royal Society 提名词列为"other influential discoveries"之一。
7. **量子遥控传态（1993）**：与 Bennett、Crépeau、Jozsa、Peres、Wootters 六人合著 *Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels*（Physical Review Letters 70, 1895–1899, 1993）——**本篇侧重论文署名与 PRL 出处**；Royal Society 提名词将 quantum cryptography 与 quantum teleportation 并称"universally recognized as fundamental cornerstones of the entire discipline"。
8. **量子算法贡献**：amplitude amplification（振幅放大）、quantum counting（量子计数）、**BHT algorithm**（量子碰撞搜索算法）——Known for 列表与提名词均实载"amplitude amplification and the first lower bound on the power of quantum computers"；quantum pseudo-telepathy 与纠缠的经典模拟。
9. **纠缠蒸馏（1996）**：与 Bennett、Popescu、Schumacher、Smolin、Wootters 合著 *Purification of Noisy Entanglement and Faithful Teleportation via Noisy Channels*（PRL 1996）。
10. **Bell 定理之外（1992）**：与 Bennett、Mermin 合著 *Quantum cryptography without Bell's theorem*（PRL 1992）。
11. **《Journal of Cryptology》主编（1991–1998）**：密码学旗舰期刊的主编经历。
12. **荣誉纵览**（详见 §8）：Prix Marie-Victorin（2000，魁北克省政府最高科学奖）、IACR Fellow（2006，**首位加拿大人**）、Gerhard Herzberg Canada Gold Medal（2010-06，**加拿大最高科学荣誉**）、FRSC + FRS（伦敦皇家学会，2013）、**加拿大勋章官佐（Officer, Order of Canada，2013-12-30，总督 David Johnston 宣布）**、Wolf Prize in Physics（2018）、BBVA Frontiers of Knowledge（2019）、Micius Quantum Prize（2019）、Breakthrough Prize in Fundamental Physics（2023 届，2022-09 公布，"the world's largest science prize"）、Eduard Rhein Foundation Prize in Technology（2023）；**2025 图灵奖**（2026-03 公布，与 Bennett 共享）。
13. **Royal Society 提名词引语（2013，页面原载整段，本篇核心引语）**："Gilles Brassard is one of the earliest pioneers of quantum information science in the world... Through his visionary thinking and groundbreaking research, Professor Brassard has played a pivotal role in transforming the field of quantum information science from what was initially perceived to be merely a fringe pursuit into an area of vigorous and dynamic international activity."

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（经典密码学 — 蓝） | `#2E5A9E` | Cornell 博士 / Journal of Cryptology |
| 分类色 2（BB84 量子密码 — 青绿） | `#1E8E8E` | BB84 / Cascade / privacy amplification |
| 分类色 3（量子算法 — 琥珀） | `#D9A441` | amplitude amplification / quantum counting / BHT |
| 分类色 4（量子纠缠与传态 — 玫瑰） | `#C0395B` | teleportation 1993 / entanglement distillation / pseudo-telepathy |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：极光横带（稀疏水平波纹），呼应「北国蒙特利尔 + 密钥在噪声中浮现」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：开阔 / 自由（把"不可破译的通信自由"从边缘推向世界）
- **选定曲目**：Alex-Productions **Winds Of Freedom**（manifest 预分配，直接沿用），匹配" fringe pursuit → 国际热潮"的破风叙事。
- **落地文件**：`turing/presentations/Gilles_Brassard/WindsOfFreedom.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「量子密码学之父 · 加拿大」+ Brassard 1955–（在世）+ 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1955–至今 生平纵览
4. **蒙特利尔少年与 Cornell 密码学博士**（1955–1979）：UdeM 本硕、Hopcroft 门下、Relativized Cryptography
5. **一生一校：蒙特利尔大学**（1988– / 2001–）：正教授、Canada Research Chair
6. **BB84：与 Bennett 发明量子密码**（1984）：共同发明口径、不确定性原理
7. **Cascade 与隐私放大**：纠错协议、Generalized privacy amplification（1995）
8. **量子密码的理论骨架（1992）**：without Bell's theorem（与 Bennett、Mermin）
9. **量子遥控传态（1993）**：PRL 六作者论文、双通道方案（侧重署名与出处）
10. **纠缠蒸馏（1996）**：Purification of Noisy Entanglement、噪声信道忠实传态
11. **量子算法**：amplitude amplification / quantum counting / BHT / 首个量子计算能力下界
12. **主编与学会**：Journal of Cryptology 主编（1991–1998）、IACR Fellow 2006
13. **荣誉**：Marie-Victorin 2000 / Herzberg 2010 / FRS 2013 / Order of Canada 2013 / Wolf 2018 / BBVA & Micius 2019 / Breakthrough / Eduard Rhein
14. **2025 图灵奖**：与 Bennett 共享、ACM citation 整句、Royal Society 提名词引语
15. **结尾**：从 fringe pursuit 到国际热潮、量子信息时代的共同奠基

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒**：1955-04-20（页面精确到日）；**在世，死亡日期一律留白**。
- **导师 Hopcroft 的额外头衔禁写**：页面仅载"advisor John Hopcroft"——**"Hopcroft 是 1986 年图灵奖得主"本地页面无载，禁写**；如需写先另行核对。
- **BB84 口径**：本篇写"与 Charles H. Bennett **共同发明**（invented together, 1984）"；Wiesner 理念来源在 Bennett 篇按实载提及，本篇不展开亦不省略"共同"二字。
- **teleportation 归属**：1993 年 PRL 论文为 **六作者**（Bennett, Brassard, Crépeau, Jozsa, Peres, Wootters）——本篇侧重"六人论文"，勿写成 Brassard 独创或纯实验成就；与 Bennett 篇（机制描述）分工。
- **Breakthrough Prize 年份（两篇疑点）**：Brassard 页正文写"In September 2022 ... awarded the Breakthrough Prize"，Bennett 页写 2023——统一口径"**2023 届 Breakthrough Prize in Fundamental Physics（2022 年 9 月公布）**"，两篇保持一致。
- **获奖理由**（ACM citation，页面实载）："for work on the foundations of quantum information science and secure communication and computing"——整句引用，与 Bennett 篇一致；获奖口径"**2025 年图灵奖（2026 年 3 月公布）**"。
- **"首位/最高"表述**（页面原载可写，勿放大）："first Canadian to be so honored"（IACR Fellow 2006）；"the highest scientific award of the government of Quebec"（Marie-Victorin）；"Canada's highest scientific honour"（Herzberg）；"the world's largest science prize"（Breakthrough）——均标注语境。
- **提名词引语**：Royal Society 2013 提名词整段为页面实载引语——选用其中一至两句并标注出处（FRS nomination, 2013）；勿编造其他引语。
- **共享结构**：与 Bennett 共享——本篇侧重密码学出身 / BB84+Cascade / privacy amplification / 量子算法 / PRL 论文署名；Bennett 侧重可逆计算 / Maxwell's demon / 逻辑深度 / 1989 演示 / 机制描述。**禁写两人恩怨或贡献多寡之争**（页面无载）。
- **荣誉边界**：Order of Canada 写"Officer（官佐）"，2013-12-30 由总督 David Johnston 宣布——勿升格为 Commander； spouse Lise Raymond 仅身份页一笔，不展开家庭叙事。
- **Portrait**：`Gilles_Brassard_2019_.jpg`（2019 照，250px/500px 两版取 500px）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 布拉萨德（或 吉尔·布拉萨德） | 待写入 |
| name_en | Gilles Brassard | 待写入 |
| birth_date | 1955-04-20 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Canada | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | quantum cryptography / quantum computing / cryptography | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：John Hopcroft（Cornell；页面仅载 advisor 身份）
- **博士生**：Anne Broadbent（infobox 实载）
- **合作者**：Charles H. Bennett（BB84 / teleportation / 蒸馏 / privacy amplification / 2025 图灵奖共享者）；Claude Crépeau（teleportation / privacy amplification）；Richard Jozsa、Asher Peres、William K. Wootters（teleportation 1993）；Ueli Maurer（privacy amplification）；N. David Mermin（without Bell's theorem 1992）；Popescu / Schumacher / Smolin（蒸馏 1996）
- 其余关系页面无载，禁写。

## 8. 奖项清单

- Turing Award（2025，与 Charles H. Bennett 共享；2026-03 公布；citation 见 §5）
- Prix Marie-Victorin（2000，魁北克省政府最高科学奖）
- IACR Fellow（2006，首位加拿大人）
- Gerhard Herzberg Canada Gold Medal（2010-06，加拿大最高科学荣誉）
- Fellow, Royal Society of Canada；Fellow, Royal Society（London，2013）
- Officer, Order of Canada（2013-12-30，总督 David Johnston 宣布）
- Wolf Prize in Physics（2018，与 Bennett 同年）
- BBVA Foundation Frontiers of Knowledge Award in Basic Sciences（2019）
- Micius Quantum Prize（2019）
- Breakthrough Prize in Fundamental Physics（2023 届，2022-09 公布）
- Eduard Rhein Foundation Prize in Technology（2023）

## 9. 机构清单

- 教育：Université de Montréal（BSc、MSc）、Cornell University（计算机科学 PhD 1979）
- 任职：Université de Montréal（正教授 1988–；Canada Research Chair 2001–）；Journal of Cryptology 主编（1991–1998）

## 10. 终审清单

- [ ] 生卒 1955-04-20 / 在世留白
- [ ] Cornell PhD 1979 密码学、导师 John Hopcroft（不写 Hopcroft 的图灵奖）
- [ ] BB84"与 Bennett 共同发明（1984）"，共同二字不省略
- [ ] Cascade / privacy amplification 归本篇侧重，年份准确（GPA 1995）
- [ ] teleportation 1993 = PRL 六作者论文，署名完整
- [ ] 量子算法（amplitude amplification / quantum counting / BHT）按 Known for 与提名词实载表述
- [ ] "首位加拿大人 / 最高奖"表述逐条标注语境，不放大
- [ ] 获奖口径"2025 图灵奖（2026-03 公布）"，citation 整句引用；Breakthrough 统一"2023 届（2022-09 公布）"
- [ ] Royal Society 提名词引语标注出处，无编造引语
- [ ] 与 Bennett 篇侧重分工明确，无恩怨渲染
- [ ] 封面头像 `Gilles_Brassard_2019_.jpg`（500px），底部状态栏 `加拿大 | Université de Montréal | Turing 2025`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2025/Gilles Brassard/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Gilles_Brassard_2019_.jpg`（2019 年照）
- [ ] **国籍**：封面顶部徽章明示加拿大
- [ ] **引语核对**：Royal Society 提名词引语与 ACM citation 必须在 Wikipedia 原文找到
- [ ] **奖项年份**：Breakthrough "2023 届（2022-09 公布）"口径与 Bennett 篇一致性复核
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与共享奖同伴 Bennett 篇格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
