# Kristen Nygaard（克里斯滕·奈加特）立传提示词

> qid=Q92744 · 1926-08-27 – 2002-08-10 · 挪威计算机科学家、程序设计语言先驱、政治活动者 · 20 世纪 · 2001 图灵奖（与 Ole-Johan Dahl 共享）
> 本地 Wikipedia 数据源：`turing/pages/2001/Kristen Nygaard/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 挪威`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（对象/类/继承/拟并行的结构化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Kristen Nygaard（中文惯称：克里斯滕·奈加特）
- **生卒**：1926-08-27 生于 Oslo, Norway → 2002-08-10 逝于 Oslo, Norway，享年 75（页面实载死因：心脏病发作 heart attack）
- **国籍**：挪威（Norway，Citizenship 栏实载）
- **身份**：计算机科学家、程序设计语言先驱、政治活动者；国际公认与 Ole-Johan Dahl 并列的面向对象编程（OOP）共同发明人（"co-inventor"，页面实载可写）
- **家庭**：1951 年与 Johanna Nygaard 结婚（任职于挪威对发展中国家援助机构，专长东非专家招募与行政支持）；三子女、七孙辈
- **教育**：University of Oslo **数学硕士**（MS，1956）；论文题为 *"Theoretical Aspects of Monte Carlo methods"*（蒙特卡洛方法的理论面向，属抽象概率论）
- **师承**：页面未载导师姓名——勿编造
- **研究领域**：计算机科学（OO 语言、系统开发、IT 的社会影响）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖（2001，与 Dahl 共享）**：2002 年 2 月 ACM 授予 Nygaard 与 Dahl 2001 图灵奖，citation 整句："For ideas fundamental to the emergence of object-oriented programming, through their design of the programming languages Simula I and Simula 67."（本篇可整句引用并注明共享。）
2. **OO 核心概念五件套**：Simula 语言引入 **objects、classes、inheritance、virtual quantities、multi-threaded（quasi-parallel）program execution**——本篇侧重 OO **思想**侧（对象如何改变编程世界观）。
3. **挪威国防研究院起步（1948–1960）**：1948–1954 从事计算与程序设计、1952–1960 运筹学（operational research）；1957–1960 领导挪威国防系统的**第一个运筹学小组**。
4. **运筹学组织者**：挪威运筹学会（Norwegian Operational Research Society）共同创始人兼首任主席（1959–1964）。
5. **挪威计算中心的建设者（1960–）**：1960 年入职 NCC，主导把 NCC 建成研究机构，1962 年任研究主任（Director of Research）——Simula 由此生长。
6. **Simula 双阶段（与 Dahl）**：Simula I（1961–1965）与 Simula 67（1965–1968）——ALGOL 60 的扩展变体与超集，起点是仿真语言。
7. **工会研究与社会参与（1971–1973）**：为挪威工会做计划、控制与数据处理研究（与 Olav Terje Bergo 合作），以有组织劳动（organised labour）的目标为评价基准——"技术为劳动者服务"的先声。
8. **DELTA 与社会影响研究（1973–1975）**：与 Erik Holbaek-Hanssen、Petter Haandlykken 合作通用系统描述语言 DELTA；持续研究计算机技术的社会影响。
9. **斯堪的纳维亚系统开发学派**：Aarhus 大学教授（1975–1976）→ Oslo 大学教授（1977 起兼职、1984–1996 全职）；其系统开发与 IT 社会影响研究成为**斯堪的纳维亚系统开发学派**的基础，与参与式设计（participatory design）紧密相连。
10. **BETA 语言（1976–1986–）**：自 1976 年参与设计、1986 年起实现通用 OO 语言 BETA（与 Bent Bruun Kristensen、Ole Lehrmann Madsen、Birger Møller-Pedersen）。
11. **GOODS 与 COOL（1995–2001）**：1997 年起主持挪威研究理事会 GOODDS（GOODS）分布式对象系统三年项目；晚期研究转向编程导论教学与信息学的过程导向概念平台（COOL）；2001 年 Simula Research Laboratory 开所即兼任研究员。
12. **政治活动者**：自由党全国执行委员会成员（1960 年代中后期）、1972 年欧共体公投中青年反欧组织的协调人、工党党员（1971–2001）、**Nei til EF** 主席（1990–1995）——1994-11-28 公投 52.2% 反对、88.8% 投票率的胜利；1996–1997 协调创建泛欧反马斯特里赫特网络 TEAM（1997-03-03 成立）。
13. **荣誉**：IEEE von Neumann Medal（2001-11，与 Dahl 共享，citation："For the introduction of the concepts underlying object-oriented programming through the design and implementation of Simula 67"）、Norbert Wiener Award（1990-10，CPSR 社会责任奖——与其社会参与互相印证）、Rosing Prize 首届（1999，与 Dahl）、St. Olav 指挥官勋章（2000-08，Harald V 国王授予）、OMG 荣誉会士（2000-06，"for his originating of object technology concepts"）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（面向对象思想 — 蓝） | `#2E5A9E` | 对象 / 类 / 继承 / BETA |
| 分类色 2（Simula 与仿真 — 青绿） | `#1E8E8E` | Simula I / Simula 67 / ALGOL 60 |
| 分类色 3（技术与社会 — 琥珀） | `#D9A441` | 工会研究 / 参与式设计 / Wiener 奖 |
| 分类色 4（公民行动 — 玫瑰） | `#C0395B` | Nei til EF / 1972 公投 / TEAM |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「对象自治与协作 / 北欧公民社会」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：悲悯 / 沉重（语言先驱与公民斗士、2002 年随 Dahl 之后离世的一年之殇）
- **选定曲目**：Alex-Productions **Tragedy**（manifest 预分配，直接沿用；化学 Buchner 篇同曲，属正常复用），匹配"2002 年 OO 双子星相继谢幕"的悲剧气质——须注意视频基调仍以成就为主，勿过度悲情。
- **落地文件**：`turing/presentations/Kristen_Nygaard/Tragedy.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「OOP 共同发明人 · 挪威」+ 奈加特 1926–2002 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1926–2002 生平纵览
4. **早年与蒙特卡洛硕士**（1926–1956）：Oslo 出生、1956 数学硕士、Monte Carlo 论文
5. **国防研究院的十年**（1948–1960）：计算与运筹、首个 OR 小组、运筹学会首任主席
6. **挪威计算中心**（1960–）：研究主任、Simula 的温床
7. **Simula：与 Dahl 的共创**（1961–1968）：Simula I → Simula 67、ALGOL 60 超集
8. **OO 思想五件套**（公式框：objects/classes/inheritance/virtual quantities/quasi-parallel）——本篇侧重思想
9. **图灵奖**：2001（共享）、citation 整句、von Neumann Medal 2001-11
10. **技术为劳动者服务**（1971–1975）：工会研究、DELTA、IT 社会影响
11. **斯堪的纳维亚学派**：Aarhus 1975–76、Oslo 1977–96、参与式设计、BETA 语言
12. **GOODS 与 COOL**（1995–2001）：分布式对象、编程教学、Simula Research Laboratory
13. **公民行动三十年**：自由党 → 1972 公投 → 工党 → Nei til EF 1994 胜利 → TEAM
14. **荣誉**：Wiener 1990、Rosing 1999、OMG 2000、St. Olav 2000、Lund/Aalborg 荣誉博士
15. **结尾**：75 岁、心脏病发作、与 Dahl 同年谢幕的 OO 奠基人

## 5. 史实陷阱与敏感点（终审必须检查）

- **与 Dahl 的侧重分工（批次红线）**：本篇侧重 **OO 思想 + 社会项目/政治参与**（工会研究、斯堪的纳维亚学派、参与式设计、Nei til EF）；语言实现/规范/合书细节归 Dahl 篇。**两人恩怨页面无载，禁写任何分歧/矛盾**。
- **"co-inventor" 表述**：页面原文明示 Nygaard 是 OOP 与 Simula 的 "co-inventor"（与 Dahl）——可写"共同发明人"，勿写"唯一发明人"。
- **图灵奖颁奖时序**：ACM 授予的是 **2001** 图灵奖，颁奖仪式在 **2002 年 2 月**（"In February 2002, he was given ... the 2001 A. M. Turing Award"）——勿写"2002 年图灵奖"；von Neumann Medal 是 **2001 年 11 月** IEEE 授予。
- **两条 citation 都可用**：图灵奖 "For ideas fundamental to the emergence of object-oriented programming, through their design of the programming languages Simula I and Simula 67."；von Neumann Medal "For the introduction of the concepts underlying object-oriented programming through the design and implementation of Simula 67"——注意措辞差异（emergence of OOP vs introduction of concepts），勿混抄。
- **政治内容红线**：政治活动仅按页面实载写（自由党执委、1972 公投协调人、工党 1971–2001、Nei til EF 主席 1990–95、TEAM 1996–97）——**一笔带过不渲染**；1994 公投数字（52.2% / 88.8%）可写；**勿写成"反欧=反欧盟本身"的政治立场引申**；1994-11-28 公投日期勿错（勿写 1994-08-28 等）。
- **Nei til EF 规模**："挪威最大政治组织（1994 年 14.5 万成员）"为页面实载，可用但建议降为小字注。
- **"first" 类表述仅两处可写**：① 1959–64 挪威运筹学会首任主席（cofounder and first chairman）；② Aalborg 大学第一位荣誉博士（1991，"the first individual"）——其余勿写；Rosing Prize 亦是 "first people to receive"（与 Dahl，1999）——三处之外禁写。
- **学位**：**硕士**（MS 1956）——页面无载博士；"professor emeritus at the University of Oslo" 的表述按页面写（part-time 1977 起、full-time 1984–1996），勿写成"1976 年起全职"。
- **GOODS 全称**：General Object-Oriented Distributed Systems（1997 起、三年、挪威研究理事会资助）——勿写错缩写；团队含 Haakon Bryhni、Dag Sjøberg、Ole Smørdal（可省）。
- **死因**：心脏病发作（heart attack，2002）——仅此一种写法；与 Dahl（2002-06-29 逝）同年、Nygaard 晚约六周（2002-08-10）——可作叙事注脚，勿渲染成"殉道"。
- **家庭**：Johanna（1951 年结婚）、三子女、七孙辈——按实载；勿写父母信息（页面未载）。
- **Danish footballer 同名**：页面顶部消歧义提示存在同名丹麦足球运动员 Kristen Nygaard——立传时注意勿混入。
- **全文无本人直接引语**：页面无 Nygaard 直接引语（"Those Were the Days"?... 是论文标题非引语）——勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | manifest 为 null，待补 |
| name_zh | 奈加特（或 克里斯滕·奈加特） | 待写入 |
| name_en | Kristen Nygaard | 待写入 |
| birth_date | 1926-08-27 | 待写入 |
| death_date | 2002-08-10 | 待写入 |
| nationality | Norway | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | object-oriented programming / Simula / system development and social impact of computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **合作者（核心）**：Ole-Johan Dahl（Simula 联合设计者、图灵奖共享——collaborator）、Bent Bruun Kristensen / Ole Lehrmann Madsen / Birger Møller-Pedersen（BETA 语言团队）、Erik Holbaek-Hanssen / Petter Haandlykken（DELTA）、Olav Terje Bergo（工会研究）
- **机构关系**：Simula Research Laboratory（2001 兼任）——仅履历
- **无载禁写**：页面未载导师与学生名单——明写"无载禁写"；勿从 Dahl 篇倒灌 Myhrhaug 关系（Myhrhaug 是 Dahl 篇 Common Base 合著者，Nygaard 页面未载其个人合作）

## 8. 奖项清单

- Turing Award（2001，与 Ole-Johan Dahl 共享；2002-02 颁发）
- IEEE John von Neumann Medal（2001-11，与 Dahl 共享，citation 见 §5）
- Norbert Wiener Award for Social and Professional Responsibility（1990-10，CPSR）
- Rosing Prize（1999，挪威数据协会，首届，与 Dahl）
- OMG Honorary Fellowship（2000-06，"for his originating of object technology concepts"）
- Commander of the Royal Norwegian Order of St. Olav（2000-08，Harald V 授予）
- Lund University 荣誉博士（1990-06）；Aalborg University 荣誉博士（1991-06，该校首位）
- 挪威科学院院士（Norwegian Academy of Sciences）
- Dahl–Nygaard Prize（AITO 2004 设立，以二人命名——身后纪念）

## 9. 机构清单

- 教育：University of Oslo（数学 MS 1956）
- 任职：Norwegian Defense Research Establishment（1948–1960：计算/编程 1948–54、运筹 1952–60）、Norwegian Operational Research Society（共同创始人首任主席 1959–64）、Norwegian Computing Center（1960 起、1962 研究主任）、Aarhus University（教授 1975–1976）、University of Oslo（兼职 1977 起、全职 1984–1996、荣休教授）、Simula Research Laboratory（2001 起兼职）
- 社会任职：Nei til EF 主席（1990–1995）、TEAM 协调人（1996–1997）、Oslo 大学信息学委员会主席（1984–1985）、挪威自然保护协会环保委员会首任主席、OECD 信息技术活动挪威代表（1970 年代十年）

## 10. 终审清单

- [ ] 生卒 1926-08-27 / 2002-08-10，享年 75，出生地/去世地均 Oslo；死因仅"心脏病发作"
- [ ] 图灵奖"2001 年奖、2002-02 颁发、与 Dahl 共享"表述准确；citation 整句无误
- [ ] von Neumann Medal 2001-11 与图灵奖年份不混淆
- [ ] "co-inventor（与 Dahl）"表述准确，无唯一化
- [ ] Simula I 1961–1965 / Simula 67 1965–1968 年份区间准确
- [ ] MS 1956 Monte Carlo 论文；无 PhD 表述
- [ ] 政治内容一笔带过：1972 公投、Nei til EF 1990–95、1994 数字（52.2%/88.8%）仅小字注
- [ ] "first" 表述仅三处（运筹学会首任主席、Aalborg 首位荣誉博士、Rosing 首届）
- [ ] 本篇侧重：OO 思想/社会项目/政治参与；实现与合书细节归 Dahl 篇
- [ ] 国籍用「挪威」，封面底部状态栏 `挪威 | NCC · Aarhus · Oslo · Simula Lab | Turing 2001`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2001/Kristen Nygaard/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Kristen-Nygaard-SBLP-1997-head.png`（SBLP '97 真肖像，已就绪）
- [ ] **国籍**：封面顶部徽章明示挪威
- [ ] **引语核对**：全文无本人直接引语——勿编造（仅两条奖项 citation 可引用）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同奖共享者 Dahl 篇格式对齐、侧重点不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
