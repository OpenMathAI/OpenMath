# Raj Reddy（拉吉·雷迪）立传提示词

> qid=Q92820 · 1937-06-13 – 在世留白 · 印度裔美国计算机科学家（人工智能 / 语音识别 / 机器人）· 20 世纪 · 1994 图灵奖（与 Edward Feigenbaum 共享）
> 本地 Wikipedia 数据源：`turing/pages/1994/Raj Reddy/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 印度裔·美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Hearsay 黑板模型 / 语音识别系统谱系 / 任务导向架构的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Dabbala Rajagopal "Raj" Reddy（泰卢固语：దబ్బాల రాజగోపాల్ రెడ్డి；中文惯称：拉吉·雷迪）。**泰卢固姓名规则：姓氏为 Dabbala**（页面顶部明载 "In this Telugu name, the surname is Dabbala"）。
- **生卒**：1937-06-13 生于 Katur 村（Madras Presidency, British India，今印度安得拉邦 Chittoor 县）→ **在世留白**
- **国籍**：**公民身份 United States**（infobox Citizenship 实载）；身份表述用 "Indian-born American computer scientist"（印度出生的美国计算机科学家）——封面国籍行写「印度裔·美国」
- **身份**：AI 早期先驱之一；在 Stanford 与 Carnegie Mellon 任教逾 50 年
- **家庭**：泰卢固家庭；父 Sreenivasulu Reddy（地主）、母 Pitchamma（家庭主妇）；**家族中第一个上大学的人**（页面实载）
- **教育轨迹**：
  - College of Engineering, Guindy（今 Anna University, Chennai，隶属 University of Madras）**土木工程**学士（BEng）
  - 澳大利亚实习期间入 University of New South Wales，1960 年获 **MTech**（其间上手 English Electric Deuce Mark II 计算机——真空管 + 水银延迟线存储 + 打孔卡 I/O）
  - 1963 年入 Stanford，1966 年 PhD——**页面载为 "the first PhD in AI under John McCarthy"**（麦卡锡门下首位 AI 博士；此表述须保留页面口径）
- **博士导师**：John McCarthy（1971 图灵奖得主、AI 术语创造者）
- **研究领域**：人工智能、语音识别、机器人、人机交互

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1994 图灵奖（与 Feigenbaum 共享）**：获奖理由整句引用 "for pioneering the design and construction of large scale artificial intelligence systems, demonstrating the practical importance and potential commercial impact of artificial intelligence technology"——**篇目侧重：语音识别 / 机器人 / 大规模 AI 系统工程**（Feigenbaum 篇侧重的专家系统/知识工程不展开）。
2. **亚洲第一**：**页面明载 "Reddy was the first person of Asian origin to receive the Turing Award"**（首位亚裔图灵奖得主）——本篇独有里程碑，写时保留"页面载为"口径。
3. **IBM 岁月（1960–1963）**：UNSW 毕业后加入 IBM，在澳大利亚任 Applied Science representative。
4. **Stanford 三年（1963–1969）**：McCarthy 门下 PhD（1966）+ 助理教授（1966–1969）；1968 与 McCarthy 等合作 "A Computer with Hands, Eyes, and Ears"（AFIPS '68）——手眼耳计算机的早期愿景。
5. **CMU 五十年（1969 起）**：1969 与 AI 先驱 Allen Newell、Herb Simon 共事加入 CMU 任副教授；1973 正教授；1984 University Professor；现为 University Professor of Computer Science and Robotics、Moza Bint Nasser 讲席教授。
6. **机器人研究所创始所长（1979–1991）**：CMU Robotics Institute founding director——世界最大的大学机器人研究机构之一（"最大"页面无载勿写，只写 founding director）。
7. **SCS 院长（1991–1999）**：任计算机学院院长期间帮助创建 Language Technologies Institute、Human-Computer Interaction Institute、Center for Automated Learning and Discovery（后更名 Machine Learning Department）、Institute for Software Research。
8. **语音识别系统谱系**（本篇核心页）：**Hearsay I** 是最早能**连续语音识别**的系统之一；后续 Hearsay II、**Dragon**、**Harpy**、**Sphinx I/II** 发展出现代商用语音识别的诸多底层思想——与 Xuedong Huang、James K. Baker 合作的历史综述梳理了这段谱系；其中 **"blackboard model"（黑板模型）**——多知识源协调架构——已被应用 AI 全谱系采纳。
9. **四大方向**：Task Oriented Computer Architectures（任务导向体系结构）、Analysis of Natural Scenes（自然场景分析）、Universal Access to Information（信息普适访问）、Autonomous Robotic Systems（自主机器人系统）——页面明载 "seminal contributions"。
10. **Technology in Service of Society（技术服务社会）**：①1981 年法国 Centre mondial informatique et ressource humaine（与 Negroponte、Alan Kay、Seymour Papert、Terry Winograd 同队），任首席科学家——1984 年密特朗总统授予**法国荣誉军团勋章（Légion d'Honneur）**；②1990 年代 Universal Digital Library 项目（扫描一切藏书）→ 2001 年 **Million Book Project**（与中国 Pan Yunhe/Zhuang Yuting/Gao Wen、印度 N. Balakrishnan 合作）；③RGUKT（Rajiv Gandhi University of Knowledge Technologies，2008）创始 Chancellor（2008–2019），为安得拉邦农村天才青年办学；④IIIT Hyderabad 创始主席。
11. **PITAC 联合主席（1999–2001）**：美国总统信息技术咨询委员会 co-chair；AAAI 创始人之一、1987–1989 任主席。
12. **门生满门**：James K. Baker、Alexander Waibel、James Gosling（Java 之父）、Janet M. Baker、**Kai-Fu 李开复**、**Xuedong 黄学东**、Roni Rosenfeld、**Harry Shum 沈向洋**、Hsiao-Wuen Hon 何欢——李开复 2018 畅销书《AI Superpowers》扉页题献 "To Raj Reddy, my mentor in AI and in life"（页面实载可引）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（语音识别 — 蓝） | `#2E5A9E` | Hearsay / Dragon / Harpy / Sphinx |
| 分类色 2（机器人 — 青绿） | `#1E8E8E` | Robotics Institute / 自主系统 |
| 分类色 3（教育普惠 — 琥珀） | `#D9A441` | IIIT Hyderabad / RGUKT / Million Book |
| 分类色 4（体系结构 — 玫瑰） | `#C0395B` | 黑板模型 / 任务导向体系结构 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：声波纹（同心扩散弧线），呼应「语音识别 / 让机器听懂人话」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：辽阔 / 开创（从安得拉邦村庄到 AI 疆域的开拓）
- **选定曲目**：Alex-Productions **New Lands**（史诗 / 开阔），匹配"从印度村庄少年到首位亚裔图灵奖得主"的开疆叙事（与 Minsky/Knuth 同曲，属批次正常复用）。
- **落地文件**：`turing/presentations/Raj_Reddy/NewLands.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 先驱 · 语音识别之父级人物 · 印度裔·美国」+ Reddy 1937– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1937– 生平纵览（Katur→Guindy→UNSW→IBM→Stanford→CMU→IIIT/RGUKT）
4. **Katur 村的少年（1937–1955）**：泰卢固家庭、家族第一个大学生、土木工程——按页面实载从简
5. **从土木到计算机（UNSW–IBM，1955–1963）**：Deuce Mark II、MTech 1960、IBM 澳大利亚
6. **Stanford：McCarthy 门下（1963–1969）**：页面载为 McCarthy 首位 AI 博士（1966）、助理教授、手眼耳计算机
7. **CMU 与 Newell/Simon 共事（1969 起）**：副教授→正教授 1973→University Professor 1984
8. **Hearsay 与黑板模型**（本篇核心页，公式框）：连续语音识别、多知识源协调
9. **Dragon–Harpy–Sphinx：语音识别谱系**：现代商用语音识别思想的源头、与 Huang/Baker 的历史综述
10. **机器人研究所创始所长（1979–1991）**：CMU Robotics、任务导向体系结构、自然场景分析
11. **SCS 院长与四大机构（1991–1999）**：LTI/HCII/ML Dept/ISR 的创建
12. **技术服务社会**：法国 Centre mondial、百万书库、IIIT Hyderabad、RGUKT——普惠愿景
13. **荣誉与传承**：Turing 1994（首位亚裔得主）、Légion d'Honneur 1984、Padma Bhushan 2001、Vannevar Bush 2006、门生 Gosling/李开复/黄学东/沈向洋
14. **遗产**：让机器听懂人类语言、让技术抵达金字塔底层
15. **结尾**：品牌页 OpenMathAI

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享结构**：1994 与 Edward Feigenbaum **共享**图灵奖，获奖理由两人共用同一句——**侧重区分**：Reddy 篇 = 语音识别/机器人/CMU 机构建设/技术普惠；Feigenbaum 篇 = 专家系统/知识工程。**禁写页面无载的两人合作/矛盾细节**。
- **国籍表述**：封面与全文用「印度裔·美国」（页面：Indian-born American；infobox Citizenship: United States）——勿写"印度籍"或漏掉"印度裔"。
- **"首位亚裔图灵奖得主"**：页面明载（"the first person of Asian origin to receive the Turing Award"）——**可写**，保留页面口径。
- **"首位 AI 博士"**：页面载 "graduating in 1966 as the first PhD in AI under John McCarthy"——写「页面载为 McCarthy 门下首位 AI 博士」，勿扩写成"世界第一位 AI 博士"。
- **姓名规则**：泰卢固姓名**姓氏是 Dabbala**（页面顶部明载）——引用规范名时注意，中文叙述统一用"雷迪/Reddy"即可。
- **语音系统归属**：Hearsay I/II、Dragon、Harpy、Sphinx I/II 是 **Reddy 与同事们**的系列成果（页面口径 "Reddy and his colleagues"）——勿把全部系统写成 Reddy 一人之作；Dragon 勿与后来 Dragon NaturallySpeaking 公司混写。
- **blackboard model**：写"黑板模型——协调多知识源的架构，已被应用 AI 全谱系采纳"（页面实载）——勿写"Hearsay 是唯一黑板模型系统"。
- **中印合作口径**：Million Book Project 与中国学者（Pan Yunhe/Zhuang Yuting/Gao Wen）合作是页面实载——平实叙述即可，不渲染地缘话题；Peres Center for Peace 国际董事会成员、中国工程院外籍院士等页面实载荣誉照列，不加评论。
- **印度政治人物**：RGUKT 由 Y. S. Rajasekhara Reddy、K. C. Reddy 与 Reddy 共同创建为页面实载——**一笔带过**，不展开印度政治评价。
- **COVID 智能手表提案**：页面实载其 2020 提议（用智能传感器手表监测以消除封锁）——**作为观点提及**（"proposed"），勿写成已实施或已验证的方案。
- **生卒**：**在世**（1937-06-13 生）——时间线与结尾页写 `1937–`，勿写卒年。
- **引语红线**：全文可用直接引语仅两条——①获奖理由整句；②李开复书扉页题献 "To Raj Reddy, my mentor in AI and in life"。**其余勿编造**。
- **荣誉**：Legion of Honor 1984、Turing 1994、Padma Bhushan 2001、Okawa Prize 2004、Honda Prize 2005、Vannevar Bush Award 2006、CHM Fellow 2021；院士：NAE、American Academy of Arts and Sciences、中国工程院、Indian National Science Academy、Indian National Academy of Engineering；Fellow：AAAI、ACM、ASA、IEEE、CHM；十余个荣誉博士（可合并为一句）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 雷迪（或 拉吉·雷迪） | 待写入 |
| name_en | Raj Reddy | 待写入 |
| birth_date | 1937-06-13 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States（India-born） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | artificial intelligence / speech recognition / robotics / human-computer interaction | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：John McCarthy（Stanford，1971 图灵奖得主）
- **CMU 引路人/同事**：Allen Newell、Herbert A. Simon（1975 图灵奖得主，页面载 "to work with AI pioneers"，同事关系非师承）
- **著名博士生**：James K. Baker、Alexander Waibel、James Gosling、Janet M. Baker、Kai-Fu Lee、Xuedong Huang、Roni Rosenfeld、Harry Shum、Hsiao-Wuen Hon
- **语音识别合作者**：Xuedong Huang、James K. Baker（历史综述合著者）
- **同奖共享者**：Edward Feigenbaum（1994 共同获奖人）
- 家庭关系（父母仅背景叙述，页面信息少，不入 relation）。

## 8. 奖项清单

- Legion of Honour（法国荣誉军团勋章，1984，密特朗总统授予）
- ACM Turing Award（1994，与 Feigenbaum 共享；页面载为首位亚裔得主）
- Padma Bhushan（印度莲花士勋章，2001，印度总统授予）
- The Okawa Prize（2004）
- The Honda Prize（2005）
- Vannevar Bush Award（2006）
- Computer History Museum Fellow（2021，"groundbreaking work in AI, robotics, and computer science education"）
- 院士：NAE、American Academy of Arts and Sciences、Chinese Academy of Engineering、Indian National Science Academy、Indian National Academy of Engineering
- Fellow：AAAI、ACM、Acoustical Society of America、IEEE、Computer History Museum
- 荣誉博士十余个（SV University、UNSW、Warwick、IIT Kharagpur、HKUST、CMU 等——结尾页可合并一句带过）

## 9. 机构清单

- 教育：College of Engineering, Guindy / Anna University（BEng 土木）、University of New South Wales（MTech 1960）、Stanford University（PhD 1966）
- 任职：IBM 澳大利亚（Applied Science representative，1960–1963）、Stanford University（助理教授 1966–1969）、Carnegie Mellon University（1969 起：副教授→1973 正教授→1984 University Professor；Robotics Institute 创始所长 1979–1991；SCS 院长 1991–1999；Moza Bint Nasser 讲席教授）、IIIT Hyderabad（创始主席）、RGUKT（创始 Chancellor 2008–2019）、PITAC 联合主席（1999–2001）、AAAI（创始人之一，主席 1987–1989）

## 10. 终审清单

- [ ] 生卒 1937-06-13 / 在世留白，出生地 Katur（今安得拉邦）
- [ ] 1994 与 Feigenbaum 共享，获奖理由整句引用准确
- [ ] 「印度裔·美国」国籍表述准确；「首位亚裔图灵奖得主」保留页面口径
- [ ] 「McCarthy 门下首位 AI 博士（1966）」保留页面口径不扩写
- [ ] 泰卢固姓名姓氏 Dabbala 无混淆
- [ ] 语音系统谱系归 "Reddy and his colleagues"，不写一人独作
- [ ] 黑板模型表述准确（多知识源协调、应用 AI 全谱系采纳）
- [ ] Million Book / RGUKT / COVID 提案等按页面实载平实叙述
- [ ] 国籍用「印度裔·美国」，封面底部状态栏 `印度裔·美国 | Stanford · CMU · IIIT Hyderabad | Turing 1994`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1994/Raj Reddy/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-AAAI_2026_-_Raj_Reddy_01_cropped_.jpg`（AAAI 2026 近照，最大可用版）；`RRCMU1998.jpg`（1998 年 White House 千年晚宴照）可备用
- [ ] **国籍**：封面顶部徽章明示印度裔·美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅获奖理由 + 李开复题献两条）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Hartmanis / Stearns / Feigenbaum / Blum）格式对齐，尤其检查与 Feigenbaum 篇的详略互补

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
