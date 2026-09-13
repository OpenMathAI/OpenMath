# Yoshua Bengio（约书亚·本吉奥）立传提示词

> qid=Q3572699 · 1964-03-05 生（在世，死亡日期留白） · 加拿大计算机科学家 · 20/21 世纪 · 2018 图灵奖（与 Hinton、LeCun 共享）
> 本地 Wikipedia 数据源：`turing/pages/2018/Yoshua Bengio/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（神经概率语言模型 / 注意力机制的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Yoshua Bengio（中文惯称：约书亚·本吉奥；infobox 头衔 OC OQ FRS FRSC）
- **生卒**：1964-03-05 生于巴黎（Paris，法国）；在世，死亡日期**留白**
- **国籍**：加拿大（Canadian）；生于法国
- **身份**：计算机科学家，人工神经网络与深度学习先驱；"Godfathers of AI"（AI 教父）之一
- **家庭**：生于摩洛哥犹太移民家庭（先移民法国、后迁加拿大）；父 Carlo Bengio 是药剂师兼剧作家（在蒙特利尔经营犹太-阿拉伯语塞法迪剧团）；母 Célia Moreno 是 1970 年代摩洛哥戏剧演员；弟弟 Samy Bengio 亦是神经网络领域有影响力的计算机科学家（Apple AI/ML 研究高级总监）；兄弟俩曾在摩洛哥随父服役生活一年
- **教育轨迹**：McGill University 计算机工程学士（BEng）→ 计算机科学硕士（MSc）→ 计算机科学博士（PhD，1991），博士论文 *Artificial Neural Networks and their Application to Sequence Recognition*
- **博士导师**：Renato De Mori
- **博士后**：MIT（导师 Michael I. Jordan）与 AT&T Bell Labs
- **研究领域**：机器学习、深度学习、人工智能；infobox "Known for"：深度学习、神经机器翻译、GAN、注意力模型、词嵌入、去噪自编码器、语言模型、learning to learn、生成流网络

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2018 图灵奖（共享）**：与 Geoffrey Hinton、Yann LeCun 因深度学习奠基性工作共同获奖（2019-03-27 宣布），图灵奖常被称为 "Nobel Prize of Computing"；三人并称 "Godfathers of AI"。记者 Cade Metz 称三人是 1990-2000 年代推动深度学习最关键的三人。
2. **神经概率语言模型（2003）**：Bengio 等提出 neural probabilistic language model（JMLR 2003），用分布式表示（**词嵌入 word embeddings**）克服 NLP 的"维度灾难"——本篇**侧重亮点**：序列建模的奠基。
3. **注意力机制早期工作（2014）**：与 Bahdanau、Cho 合著 *Neural Machine Translation by Jointly Learning to Align and Translate*（arXiv 1409.0473）——神经机器翻译 + 注意力对齐，本篇**侧重亮点**。
4. **引用之王**：全球被引最多的计算机科学家（总引用与 h-index 双第一）、全领域在世科学家总引用第一；2025 年 11 月成为首位 Google Scholar 引用破百万的 AI 研究者。
5. **MILA 创立者**：Université de Montréal 教职自 1993 年至今，创立魁北克 AI 研究所 Mila（Montreal Institute for Learning Algorithms）并任科学主任至 2025 年；兼 CIFAR "Learning in Machines & Brains" 项目联合主任。
6. **《Deep Learning》教科书（2016）**：与 Ian Goodfellow、Aaron Courville 合著（MIT Press），深度学习标准教材。
7. **GAN 的培养者**：著名学生 Ian Goodfellow 是生成对抗网络（GAN）发明人——Bengio 篇以"师承产出"角度写 GAN，勿写成其本人发明。
8. **Element AI 创业（2016–2020）**：2016 年 10 月联合创立蒙特利尔 AI 孵化器 Element AI，2020 年 11 月业务售予 ServiceNow（Bengio 留任顾问）。
9. **AI 安全旗手**：2023 年 3 月签署 FLI 暂停 GPT-4 级训练公开信；2023-2025 主导国际 AI 安全报告（2023-11 Sunak 宣布委托、2025-01 全文发布并持续任主席）；2025 年 6 月创立非营利机构 **LawZero**（构建可拦截自主智能体有害行为的 "Scientist AI" 护栏）；2026 年 2 月获任联合国 AI 独立国际科学专家小组成员并任联席主席（与诺奖得主 Maria Ressa）。
10. **争议中的"迷失"与转向乐观**：2023-05 BBC 访谈自陈对毕生工作感到 "lost"；2023-07 在《The Economist》撰文 "the risk of catastrophe is real enough that action is needed now"；2026 年初经 LawZero 技术研究渐趋乐观。
11. **其他荣誉**：Time 100（2024）、Erdős 数 3（2019 年一篇 RNN 架构论文）、2018 年起 h-index≥100 的计算机科学家中近期日引用最高者。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（深度学习 — 蓝） | `#2E5A9E` | 深度学习先驱 / Mila |
| 分类色 2（序列与注意力 — 青绿） | `#1E8E8E` | 神经语言模型 / 神经机器翻译与注意力 |
| 分类色 3（表示与教材 — 琥珀） | `#D9A441` | 词嵌入 / Deep Learning 教科书 / GAN 师承 |
| 分类色 4（AI 安全与治理 — 玫瑰） | `#C0395B` | 国际 AI 安全报告 / LawZero |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和词向量星云（稀疏小圆点渐次连线），呼应「词嵌入 / 序列对齐」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：回望 / 深思（序列的记忆、对一生的重新审视）
- **选定曲目**：Alex-Productions **Nostalgia**（manifest 预分配，沿用勿改）
- **落地文件**：`turing/presentations/Yoshua_Bengio/Nostalgia.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 教父 · 加拿大」+ Bengio 1964– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1964– 在世生平纵览
4. **早年：从巴黎到蒙特利尔**（1964–）：摩洛哥犹太移民家庭、药剂师兼剧作家之父、演员之母、弟弟 Samy
5. **McGill 求学与序列识别博士**（–1991）：De Mori 门下、神经网络应用于序列识别
6. **MIT 与 Bell Labs 博后**（1991–1993）：Michael I. Jordan 指导
7. **扎根蒙特利尔与 Mila**（1993–）：Université de Montréal 教职、CIFAR 联合主任
8. **神经概率语言模型与词嵌入**（2003）：克服维度灾难（侧重页）
9. **注意力机制的先声**（2014）：Bahdanau/Cho/Bengio 神经机器翻译对齐（侧重页）
10. **教科书与学派**：Deep Learning 2016、Goodfellow 与 GAN、Hugo Larochelle、David Krueger
11. **Element AI 创业**（2016–2020）：研究产业化的一课
12. **引用之王**：全球最被引计算机科学家、2025 引用破百万
13. **AI 安全旗手**：暂停公开信、国际 AI 安全报告、LawZero、联合国专家小组
14. **荣誉与共享的荣耀**：Turing 2018（与 Hinton/LeCun）、Princess of Asturias 2022、Queen Elizabeth Prize 2025
15. **结尾**：在世、从深度学习缔造者到 AI 守夜人

## 5. 史实陷阱与敏感点（终审必须检查）

- **获奖理由口径**：Bengio 页表述为 "for their foundational work on deep learning"；ACM 官方全句（Hinton 页实载）为 "conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing"——**统一采用 ACM 全句**，勿自造第三种表述。
- **共享结构**：2018 为 Bengio/Hinton/LeCun **三人共享**，须明写共享；本篇侧重序列建模/注意力/语言模型，AlexNet 等复兴叙事一笔带过（Hinton 篇主写），禁写三人内部恩怨（页面无载）。
- **"AI 教父"是三人并称**："Godfathers of AI / Deep Learning"，勿写 Bengio 独享；也勿写"深度学习之父"单数。
- **GAN 归属**：GAN 发明人是学生 Goodfellow；Bengio 的角色是**导师与 GAN 论文共同作者群的一环**——页面仅写 "Known for: Generative adversarial networks"，口径写"领域标签/其学生所创"，勿写"Bengio 发明 GAN"。
- **OBE 疑点**：infobox 头衔串含 "OBE" 但**正文零记载**——禁写任何 OBE 相关表述。
- **注意力归属**：2014 NMT 论文作者是 **Bahdanau、Cho、Bengio**（第一作者 Bahdanau），口径写"与两位学生/合作者提出"，勿写成 Bengio 单独发明注意力机制；也勿拔高为"Transformer 发明人"。
- **Element AI 结局**：2020 年售予 ServiceNow（报道提及"创始人价值大多蒸发"、裁员）——可写出售事实，**勿渲染亏损金额与裁员细节渲染**。
- **在世者**：死亡日期留白；无配偶/子女信息（页面无载禁写）。
- **引语**：页面实载引语仅有 BBC "lost"（《Fortune》转述标题）、Economist "the risk of catastrophe is real enough that action is needed now."；其余引语**勿编造**。
- **争议表述**："most-cited" 表述限定为页面原话（计算机科学家总引用与 h-index 全球第一、全领域在世科学家总引用第一），勿外推为"史上第一"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 本吉奥（或 约书亚·本吉奥） | 待写入 |
| name_en | Yoshua Bengio | 待写入 |
| birth_date | 1964-03-05 | 待写入 |
| death_date | 在世留白 | 待写入 |
| nationality | Canada | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | machine learning / deep learning / artificial intelligence | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Renato De Mori（McGill）
- **博士后导师**：Michael I. Jordan（MIT）
- **著名学生**：Ian Goodfellow（GAN 发明人）、Hugo Larochelle、David Krueger（页面明确列名）
- **合作者**：Geoffrey Hinton、Yann LeCun（2015 Nature *Deep learning* 综述合著者、同届图灵奖得主）；Dzmitry Bahdanau、Kyunghyun Cho（NMT/注意力论文合作者）；Aaron Courville（Deep Learning 教科书合著者）；Léon Bottou、Patrick Haffner、Patrice Simard（DjVu 论文合作者，与 LeCun 同署）
- **兄弟**：Samy Bengio（同为神经网络计算机科学家，Apple AI/ML 研究高级总监）

## 8. 奖项清单

- ACM A.M. Turing Award（2018，与 Hinton、LeCun 共享，2019-03-27 宣布）
- Marie-Victorin (Quebec) Prize（2017）
- Officer of the Order of Canada（2017）；Fellow of the Royal Society of Canada（2017）
- AAAI Fellow（2019）
- Fellow of the Royal Society（2020）
- Princess of Asturias Award, Scientific Research（2022，与 LeCun、Hinton、Hassabis）
- Knight of the Legion of Honour（法国荣誉军团骑士，2022 年获任、2023 见载）
- UN 科学咨询委员会（2023）；ACM Fellow（2023）
- Time 100 Most Influential People（2024）
- VinFuture Prize 大奖（2024，与 Hinton、LeCun、Huang、Fei-Fei Li）
- Queen Elizabeth Prize for Engineering（2025，与 Dally、Hinton、Hopfield、LeCun、Huang、Fei-Fei Li）
- McGill 荣誉博士（2025）；Officer of the National Order of Quebec（2025）

## 9. 机构清单

- 教育：McGill University（BEng 计算机工程 / MSc / PhD 计算机科学 1991）
- 博后：MIT（Michael I. Jordan 指导）、AT&T Bell Labs
- 任职：Université de Montréal 教授（1993–至今）；MILA 创始人·科学主任（至 2025）；CIFAR Learning in Machines & Brains 联合主任；Element AI 联合创始人（2016–2020 售予 ServiceNow）；LawZero 联合主席·科学主任（2025–）；Recursion Pharmaceuticals 科学技术顾问、Valence Discovery 科学顾问

## 10. 终审清单

- [ ] 生卒 1964-03-05 巴黎；在世留白
- [ ] 2018 图灵奖为**三人共享**，获奖理由采用 ACM 全句 "conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing"
- [ ] 本篇侧重：神经概率语言模型（2003）、词嵌入、NMT/注意力（2014）；AlexNet 复兴叙事一笔带过不与 Hinton 篇重复
- [ ] GAN 归属 Goodfellow（学生），Bengio 是导师视角
- [ ] 无 OBE、无配偶子女、无三人恩怨（页面无载禁写）
- [ ] 引语仅 BBC "lost" 与 Economist 灾难风险句，标注出处
- [ ] 国籍用「加拿大」（生于法国），封面底部状态栏 `加拿大 | McGill · Université de Montréal · Mila | Turing 2018`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] 头像使用 `images/500px-ICLR_2025_-_Yoshua_Bengio_02.jpg`（500px 真实肖像）
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2018/Yoshua Bengio/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 ICLR 2025 肖像（`images/500px-ICLR_2025_-_Yoshua_Bengio_02.jpg`，备选 `500px-SD_2025_-_Yoshua_Bengio_04_cropped_.jpg`）
- [ ] **国籍**：封面顶部徽章明示加拿大
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Hinton / LeCun）格式对齐、共同部分表述不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
