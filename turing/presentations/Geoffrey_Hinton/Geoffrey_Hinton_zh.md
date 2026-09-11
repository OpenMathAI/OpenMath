# Geoffrey Hinton（杰弗里·辛顿）立传提示词

> qid=Q92894 · 1947-12-06 生（在世，死亡日期留白） · 英裔加拿大计算机科学家 · 20/21 世纪 · 2018 图灵奖（与 Bengio、LeCun 共享） · 2024 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`turing/pages/2018/Geoffrey Hinton/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国/加拿大`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（反向传播 / Boltzmann 机 / 注意力的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Geoffrey Everest Hinton（中文惯称：杰弗里·辛顿/欣顿；中间名 Everest 来自亲属 George Everest——印度测绘总监、珠峰命名由来）
- **生卒**：1947-12-06 生于伦敦温布尔登（Wimbledon, London, England, UK）；在世，死亡日期**留白**
- **国籍**：英国-加拿大（British-Canadian）
- **身份**：计算机科学家、认知科学家、认知心理学家、2024 诺贝尔物理学奖得主；"the Godfather of AI"；University of Toronto University Professor Emeritus
- **家庭（家族谱系页素材）**：父 Howard Everest Hinton（昆虫学家）；外高祖父辈——逻辑学家 **George Boole** 与数学家教育家 **Mary Everest Boole**（高祖父母）；另一位高祖父母为外科医生 James Hinton（数学家 Charles Howard Hinton 之父）；高叔祖 George Everest（珠峰 Mount Everest 命名来源）；舅公 Colin Clark（经济学家）；表亲 Joan Hinton（核物理学家、曼哈顿计划仅有的两名女物理学家之一，first cousin once removed）
- **婚姻**：首任妻子 Rosalind Zalin（1994 年死于卵巢癌）；第二任妻子 Jacqueline "Jackie" Ford（1997 年结婚，2018 年死于胰腺癌）——按页面实载一笔带过，不渲染
- **健康**：19 岁背伤导致久坐疼痛；一生与抑郁共处——可如实一笔，不渲染
- **教育轨迹**：Clifton College（布里斯托尔）→ 1967 入 King's College, Cambridge（先后转向自然科学/艺术史/哲学）→ 1970 实验心理学 BA → 木工学徒一年 → University of Edinburgh 1972–1975 研读、**1978 获 AI 博士**，论文 *Relaxation and Its Role in Vision*
- **博士导师**：Christopher Longuet-Higgins（符号 AI 学派，与 Hinton 的神经网络取向相反）
- **研究领域**：机器学习、心理学、人工智能、认知科学、计算机科学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2018 图灵奖（共享）**：与 Bengio、LeCun 共享，ACM 获奖理由全句 "for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing"（使深度神经网络成为计算的关键组件的概念与工程突破）——三人并称 "Godfathers of Deep Learning" 且仍常联袂公开演讲。本篇为**复兴主叙事篇**（AlexNet 归此）。
2. **反向传播的普及者（1986）**：与 David Rumelhart、Ronald J. Williams 在 *Nature* 发表 "Learning representations by back-propagating errors"，使多层网络训练普及——**但并非首个提出者**（Linnainmaa 1970 反向自动微分、Werbos 1974 提议用于神经网络）；Hinton 2018 访谈原话："David Rumelhart came up with the basic idea of backpropagation, so it's his invention."
3. **Boltzmann 机（1985）**：与 David Ackley、Terry Sejnowski 共同发明；**2024 诺贝尔物理学奖颁奖词明确提及 Boltzmann machine**（与 John Hopfield 共享，理由 "for foundational discoveries and inventions that enable machine learning with artificial neural networks"）。
4. **连接主义阵营（1980s CMU PDP 小组）**：与 Sejnowski、Crick、Rumelhart、McClelland 同组，在 AI 寒冬中坚持连接主义；两卷本 *Parallel Distributed Processing*；与符号主义（symbolists）的路线之争是页面实载的背景叙事。
5. **AlexNet 与深度学习复兴（2012）**：与学生 Alex Krizhevsky、Ilya Sutskever 设计 AlexNet 出战 ImageNet 2012，计算机视觉突破——本篇**侧重亮点**；同年 Coursera 开免费神经网络课；2012 与两位学生共同创立 DNNresearch，2013 年 3 月被 Google 以 **4400 万美元**收购。
6. **多伦多学派与大辉柏阵地**：1987 年起任教 University of Toronto 并任 CIFAR 首批 Fellow；2004 年在 CIFAR 发起 NCAP（今 Learning in Machines & Brains）项目并领导十年，Bengio、LeCun 皆在其中。
7. **其他重要贡献**：分布式表示、时延神经网络、混合专家、Helmholtz 机、专家乘积、wake-sleep 算法（1995，Science）、t-SNE（2008，与 van der Maaten）、胶囊网络（2011 提出/2017 两论文）、GLOM（2021）、对比学习框架（2020 SimCLR 一作 Chen 等）、**Forward-Forward 算法**（2022 NeurIPS）与 "mortal computation"。
8. **Google 十年与告别（2013–2023）**：2013–2023 分身 Google Brain 与多伦多大学；2023 年 5 月公开辞职以 "freely speak out about the risks of AI"，自陈"部分的我如今后悔毕生工作"；2017 年共同创立 Vector Institute 并任首席科学顾问。
9. **AI 风险警告者**：担忧恶意滥用、技术性失业、AGI 存在性风险；2024 年 12 月称 30 年内 AI 灭绝人类概率 "10 to 20 per cent"；主张 UBI 与政府监管；LeCun 公开不同意其灭绝论——**只写页面实载的观点分歧一句话，勿渲染争吵**。
10. **门生满天下**：博士/博后序列含 Ilya Sutskever（OpenAI）、Alex Krizhevsky、Ruslan Salakhutdinov、Radford Neal、Brendan Frey、Yee Whye Teh、Richard Zemel、Peter Brown、Peter Dayan、Max Welling、Zoubin Ghahramani、Alex Graves 等；**Yann LeCun 在页面 "other notable students" 名单中**（多伦多博后）。
11. **诺奖趣闻**：获诺奖后对《纽约时报》记者引用 Richard Feynman："Listen, buddy, if I could explain it in a couple of minutes, it wouldn't be worth the Nobel Prize."

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 · 诺贝尔 |
| 分类色 1（反向传播 — 蓝） | `#2E5A9E` | 1986 Nature 论文 / 连接主义 |
| 分类色 2（能量模型 — 青绿） | `#1E8E8E` | Boltzmann 机 / 2024 诺贝尔物理学奖 |
| 分类色 3（深度学习复兴 — 琥珀） | `#D9A441` | AlexNet 2012 / DNNresearch · Google |
| 分类色 4（风险与警示 — 玫瑰） | `#C0395B` | 离开 Google / AI 安全警告 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：层叠神经层片（稀疏竖向条纹渐变），呼应「多层网络逐层学表示」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：磅礴 / 先锋（从寒冬孤守到诺奖加冕的史诗感）
- **选定曲目**：Alex-Productions **Savage**（manifest 预分配，沿用勿改）
- **落地文件**：`turing/presentations/Geoffrey_Hinton/Savage.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 教父 · 英国/加拿大」+ Hinton 1947– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1947– 在世生平纵览
4. **布尔的后代**：家族谱系页——George Boole 高祖父、Mary Everest Boole 高祖母、珠峰的 Everest、曼哈顿计划的表亲 Joan Hinton、昆虫学家之父
5. **求学歧路**：剑桥心理学（自然科学/艺术史/哲学的辗转）、木工一年、Edinburgh AI 博士（1978）、符号派导师 Longuet-Higgins
6. **寒冬中的连接主义**：Sussex/MRC→UCSD/CMU、PDP 小组、两卷本 PDP
7. **反向传播（1986）**：Rumelhart/Williams、Nature 论文、非首提的澄清（侧重页）
8. **Boltzmann 机（1985）**：Ackley/Sejnowski、能量模型（侧重页，衔接 2024 诺贝尔）
9. **AlexNet：ImageNet 2012**（侧重页）：Krizhevsky/Sutskever、计算机视觉突破、DNNresearch→Google 4400 万
10. **多伦多学派与 CIFAR**：1987 起、NCAP 2004、Bengio/LeCun 同programme
11. **发明长廊**：t-SNE、wake-sleep、胶囊网络、对比学习、Forward-Forward
12. **告别 Google（2023）**："freely speak out"、后悔与警示
13. **2024 诺贝尔物理学奖**：与 Hopfield 共享、Boltzmann machine 载入颁奖词、Feynman 趣闻
14. **荣誉年表**：Turing 2018 · Nobel 2024 · 双奖同辉（2018 CC、2022 Asturias、2025 QE Prize 等一表列）
15. **结尾**：在世、"the Godfather of AI" 的历史地位与未竟之问

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由口径**：ACM 全句 "for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing"——本篇为三杰中**采用全句的基准篇**；与 Bengio/LeCun 共享，勿写 Hinton 独得。
- **反向传播**：Hinton 团队是**普及者非首提者**（Linnainmaa 1970 / Werbos 1974 页面明载）；Rumelhart 是"基本想法的发明者"（Hinton 2018 原话）——勿写"Hinton 发明反向传播"。
- **AlexNet 表述**：设计是与学生 Krizhevsky、Sutskever **协作**完成；ImageNet 2012 是 ILSVRC 挑战突破——勿写 Hinton 单独完成或写错年份。
- **Boltzmann 机年份与署名**：**1985**，与 Ackley、Sejnowski 共同发明——勿写成 Hinton 独创或漏掉合作者。
- **PhD 时间线疑点**：正文 "From 1972 to 1975, he continued his study... awarded a PhD in 1978"，论文标 1977——**以正文口径：1972–1975 研读、1978 获 PhD**；勿写"1975 年毕业"。
- **优先权争议**：Schmidhuber 曾主张 Werbos/Amari 1970s 工作未被充分致谢（页面实载）——**建议不写**；若采用务必中性一笔带过，勿渲染恩怨（三人内部恩怨页面无载，禁写）。
- **LeCun 观点分歧**：仅写"LeCun 不同意灭绝论、认为 AI 可拯救人类"一句；勿扩写为论战。
- **家族表述**：Boole 是 **great-great-grandfather（高祖父）**；Joan Hinton 是 **first cousin once removed**（infobox 简写 cousin）——辈分勿错；珠峰 Everest 是 great-great-granduncle（高叔祖）。
- **在世者**：死亡日期留白；两任妻子病逝年份如实一笔（1994/2018），勿渲染病情细节。
- **引语**：可用引语限定为——Rumelhart 发明句（2018 访谈）、Feynman 转述句、辞职理由 "freely speak out about the risks of AI"、2025 "ask a chicken" 句、灭绝概率 "10 to 20 per cent"（2024-12）；其余**勿编造**。
- **2012 年 Google 收购金额**：**$44 million**（2013-03）——勿写错。
- **诺奖是物理学奖**：与 Hopfield 共享，理由句整句引用 "for foundational discoveries and inventions that enable machine learning with artificial neural networks"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 辛顿（或 杰弗里·辛顿） | 待写入 |
| name_en | Geoffrey Hinton | 待写入 |
| birth_date | 1947-12-06 | 待写入 |
| death_date | 在世留白 | 待写入 |
| nationality | United Kingdom / Canada | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | machine learning / artificial intelligence / cognitive science / neural networks | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Christopher Longuet-Higgins（Edinburgh，符号 AI 学派）
- **反向传播合作者**：David Rumelhart、Ronald J. Williams（1986 Nature）
- **Boltzmann 机合作者**：David Ackley、Terry Sejnowski（1985）
- **PDP 小组同事**：Terrence Sejnowski、Francis Crick、James McClelland（CMU）
- **著名博士生**：Ilya Sutskever、Alex Krizhevsky、Ruslan Salakhutdinov、Radford M. Neal、Brendan Frey、Yee Whye Teh、Richard Zemel、Peter Brown
- **其他著名学生/博后**：Yann LeCun（多伦多博后，页面 "other notable students" 明列）、Peter Dayan、Max Welling、Zoubin Ghahramani、Alex Graves、Sam Roweis
- **同programme同仁**：Yoshua Bengio、Yann LeCun（CIFAR NCAP/Learning in Machines & Brains）
- **家庭**：George Boole（高祖父）、Mary Everest Boole（高祖母）、Joan Hinton（表亲）、Howard Everest Hinton（父，昆虫学家）

## 8. 奖项清单

- Fellow, AAAI（1990）；FRSC（1996）；FRS 伦敦皇家学会（1998）
- Rumelhart Prize 首位得主（2001）；Edinburgh 荣誉 DSc（2001）
- 美国艺术与科学院国际荣誉会员（2003）；认知科学学会 Fellow（2003）
- IJCAI Research Excellence Award（2005）
- Herzberg Canada Gold Medal（2011）；Sussex 荣誉 DSc（2011）
- Killam Prize, Engineering（2012）；Sherbrooke 荣誉博士（2013）
- 西班牙皇家工程院荣誉外籍院士（2015）
- 美国国家工程院院士（2016）；IEEE/RSE James Clerk Maxwell Award（2016）；BBVA Frontiers of Knowledge Award（2016）
- **ACM A.M. Turing Award（2018，与 Bengio、LeCun 共享）**；Companion of the Order of Canada（2018）
- Dickson Prize（CMU，2021）；Princess of Asturias Award（2022，与 LeCun/Bengio/Hassabis）；U of T 荣誉 DSc（2022）
- ACM Fellow（2023）；美国国家科学院院士（2023）；Lifeboat Foundation Guardian Award（2023，与 Sutskever）
- **诺贝尔物理学奖（2024，与 John Hopfield 共享）**；VinFuture Prize（2024）
- Queen Elizabeth Prize for Engineering（2025）；King Charles III Coronation Medal；Sandford Fleming Medal（2025）；Harvard 荣誉 DSc（2026）

## 9. 机构清单

- 教育：Clifton College（中学）；King's College, Cambridge（BA 实验心理学 1970）；University of Edinburgh（PhD AI 1978）
- 任职：University of Sussex；MRC Applied Psychology Unit；UC San Diego（博后）；Carnegie Mellon University；UCL Gatsby 计算神经科学单元创始主任；University of Toronto（1987–至今，University Professor Emeritus）；CIFAR Fellow（1987–）与 NCAP 项目领导（2004 起）；DNNresearch（2012，售 Google 2013）；Google/Google Brain（2013–2023）；Vector Institute 首席科学顾问（2017–）

## 10. 终审清单

- [ ] 生卒 1947-12-06 伦敦温布尔登；在世留白
- [ ] 图灵奖 2018 三人共享 + ACM 全句获奖理由；诺贝尔物理学奖 2024 与 Hopfield 共享、理由句整句引用
- [ ] 反向传播"普及者非首提者"、Rumelhart 发明基本想法的表述准确
- [ ] Boltzmann 机 1985 与 Ackley/Sejnowski 共同发明
- [ ] AlexNet 2012 与 Krizhevsky/Sutskever 协作
- [ ] 家族谱系辈分准确（Boole 高祖父、Everest 高叔祖、Joan Hinton first cousin once removed）
- [ ] Edinburgh PhD 口径 1978（1972–1975 研读）
- [ ] 两任妻子病逝、背伤、抑郁按实载一笔带过不渲染
- [ ] Schmidhuber 争议不写或中性一笔；三人恩怨禁写
- [ ] 国籍用「英国/加拿大」，封面底部状态栏 `英国/加拿大 | Edinburgh · CMU · UCL · Toronto · Google | Turing 2018 · Nobel 2024`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] 头像使用 `images/500px-Geoffrey_Hinton_in_2026.jpg`（500px 真实肖像）
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2018/Geoffrey Hinton/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2026 居家肖像（`images/500px-Geoffrey_Hinton_in_2026.jpg`，备选 `500px-SD_2025_-_Geoffrey_Hinton_01.jpg`）
- [ ] **国籍**：封面顶部徽章明示英国/加拿大
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Bengio / LeCun）格式对齐、共同部分表述不重复（AlexNet 复兴主叙事归本篇）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
