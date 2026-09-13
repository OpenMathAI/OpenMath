# Joseph Sifakis（约瑟夫·斯法基斯）立传提示词

> qid=Q92781 · 1946-12-26 生（在世） · 希腊-法国计算机科学家 · 20 世纪 · 2007 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2007/Joseph Sifakis/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 希腊-法国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（时间/混合系统语义与「系统 M ⊨ 规格 φ」判定的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Joseph Sifakis（希腊文 Ιωσήφ Σηφάκης；中文惯称：约瑟夫·斯法基斯）
- **生卒**：1946-12-26 生于 Heraklion, Crete（希腊克里特岛）；**在世，死亡日期留白**（页面写"lives in France"，现居法国）
- **国籍**：**希腊-法国双重背景**（Greek-French computer scientist——页面原文；出生希腊、生活工作在法国，希腊与法国两国荣誉均详载）
- **身份**：计算机科学家；**模型检验发明与发展者之一**；嵌入式系统领域领军人物；CNRS 名誉研究总监（Research Director Emeritus）；VERIMAG 实验室创始人
- **家庭**：配偶 Olga Ioannidi（infobox 实载）；其余家庭细节无载禁写
- **教育轨迹**：
  - National Technical University of Athens（雅典国立技术大学）**电气工程** BS
  - 法国奖学金资助下赴格勒诺布尔大学（University of Grenoble）攻读**计算机科学** MS、PhD
  - 1974 年工程博士（doctorat d'ingénieur，论文《Modèles temporels des systèmes logiques》，Université Joseph-Fourier – Grenoble I）
  - 1979 年**国家博士**（state doctorate / doctorat d'état，论文《Le contrôle des systèmes asynchrones : concepts, propriétés, analyse statique》，INPG & Joseph-Fourier）——页面注：当时的法国有两级博士制，国家博士是任教授的必要条件，后被 habilitation 取代
- **博士导师**：页面无载禁写
- **研究领域**：计算机科学；系统验证、形式方法应用于系统设计、模型检验、嵌入式系统、时序与混合系统、基于组件的严谨设计

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2007 图灵奖**：与 Clarke、Emerson 三人共享（"for his work on model checking"——页面表述）；共享 citation 见本批次 Emerson 页面：`for their role in developing Model-Checking into a highly effective verification technology that is widely adopted in the hardware and software industries.`——本篇**侧重 Verimag/CESAR/嵌入式系统与希法双重背景**（Clarke 篇侧重开创与 CMU、Emerson 篇侧重 CTL）。
2. **国家博士埋下模型检验的种子（1979）**：`In his state doctorate he studied the principles of the algorithmic verification method known later as model checking.`——他在国家博士中研究的"算法化验证方法"后来被称为 model checking——**欧洲独立研究线的源头**（Emerson 页面明载 Sifakis independently studied 该概念）。
3. **CESAR 验证工具（1982）**：该技术在 Jean-Pierre Queille 的博士论文中应用，开发出 **CESAR** 验证工具——模型检验思想在欧洲的第一次工具化落地。
4. **VERIMAG 创始人与 14 年台长**：格勒诺布尔附近 VERIMAG 实验室的**创始人**；初期为 CNRS 与 Verilog SA 的混合产业实验室；任台长 14 年。VERIMAG 与 Airbus、Schneider Electric 合作开发安全关键系统（safety critical systems）的方法与工具，尤其是基于 **Lustre 语言**的 **SCADE** 同步编程环境。
5. **CAV 会议共同创办人（1989）**：与 Edmund M. Clarke、Amir Pnueli 共同创办 **CAV**（Computer Aided Verification）会议——首届 1989 年在格勒诺布尔举办。
6. **时序与混合系统**：与 Thomas Henzinger 合作研究**时序与混合系统（timed and hybrid systems）的验证**；与 Amir Pnueli、Oded Maler 研究时序系统的**综合**（如 1995 STACS 时序控制器综合论文）。
7. **验证工具谱系**：参与开发 IF toolset、Kronos、CADP、TGV 等验证工具；发展用**抽象技术**应对状态爆炸（state explosion）的理论。
8. **BIP 组件框架**：近二十年工作聚焦基于 BIP 组件框架的**严谨组件化设计**（rigorous component-based design）；近期转向**可信自主系统**（trustworthy autonomous systems）尤其是自动驾驶。
9. **欧洲嵌入式网络 ARTIST 协调人（2004–2012）**：欧洲嵌入式系统卓越网络 ARTIST 的协调人。
10. **跨界任职**：INRIA-Schneider 产业讲席（2008–2011）；EPFL 计算与通信科学学院全职教授、"Rigorous System Design Laboratory" 主任（2011–2016）；清华大学访问教授（2011–2012）、南方科技大学（SUSTech）访问教授（2019）——与中国的联系页面实载。
11. **希腊公共科学服务**：希腊国家研究与技术委员会（National Council for Research and Technology）主席（2014–2016）。
12. **荣誉**：Turing Award 2007、法国荣誉军团勋章指挥官（Commander of the Legion of Honor, 2011）、法国国家功绩勋章大军官（Grand Officer of the National Order of Merit, 2008）、法兰西科学院院士（2010）、法兰西工程院院士（2008）、Academia Europaea（2008）、美国艺术与科学院（2015）、美国国家工程院（2017）、**中国科学院外籍院士（2019）**、美国国家科学院院士（2024）、Leonardo da Vinci Medal（2012）；著书《Understanding and Changing the World》（Springer, 2022 年 5 月）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（模型检验 — 蓝） | `#2E5A9E` | 国家博士 / CESAR / 欧洲独立线 |
| 分类色 2（安全关键系统 — 青绿） | `#1E8E8E` | VERIMAG / Airbus / SCADE / Lustre |
| 分类色 3（嵌入式与自主系统 — 琥珀） | `#D9A441` | ARTIST / BIP / 自动驾驶 |
| 分类色 4（时序与混合系统 — 玫瑰） | `#C0395B` | timed/hybrid systems / Kronos / 与 Henzinger/Pnueli 合作 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：时间轴-时钟语义（时间自动机的时钟约束意象），呼应「timed systems / 实时验证」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：自由 / 跨界（克里特到格勒诺布尔、从形式验证到自主系统的自由行旅）
- **选定曲目**：Alex-Productions **Winds Of Freedom**（manifest 预分配，直接沿用），匹配"地中海到阿尔卑斯、形式方法服务产业"的开阔叙事。
- **落地文件**：`turing/presentations/Joseph_Sifakis/WindsOfFreedom.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「模型检验与嵌入式系统 · 希腊-法国」+ 斯法基斯 1946– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 任职 / 主要荣誉 / 核心领域 / 现居）
3. **时间线**（`\timelineslide`）：1946– 生平纵览
4. **早年：克里特与雅典**（1946–）：Heraklion 出生、雅典国立技术大学电气工程
5. **赴法：格勒诺布尔**（1970s）：法国奖学金、计算机科学、1974 工程博士
6. **国家博士与模型检验的雏形**（1979）：两级博士制背景注、"后来被称为 model checking 的算法化验证方法"
7. **CESAR：欧洲的第一件工具**（1982）：Jean-Pierre Queille 博士论文应用
8. **创立 VERIMAG**：CNRS×Verilog SA 混合产业实验室、14 年台长、Airbus/Schneider、SCADE 与 Lustre
9. **CAV 会议的诞生**（1989）：与 Clarke、Pnueli 共同创办、首届格勒诺布尔
10. **时序与混合系统**：与 Henzinger 的验证、与 Pnueli/Maler 的综合、Kronos 等工具、抽象对状态爆炸
11. **从 BIP 到可信自主系统**：组件化严谨设计、自动驾驶
12. **跨界：ARTIST 与学界**：欧洲嵌入式网络协调（2004–2012）、INRIA-Schneider 讲席、EPFL 实验室主任、清华/SUSTech 访问、希腊科委会主席
13. **荣誉**：法国两勋章 + 两国科学院 + 中科院外籍院士 2019 + NAS 2024
14. **2007 图灵奖**：与 Clarke、Emerson 共享、citation 整句引用
15. **结尾**：在世、从形式验证到"理解并改变世界"的历史地位（书名点题）

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖 citation**：Sifakis 页面本身未载 citation 全文；共享 citation 见本批次 Emerson 页面（`for their role in developing Model-Checking into a highly effective verification technology…`）——引用时注明为 2007 共享 citation。
- **三人侧重区分**：Sifakis 篇**只侧重 Verimag/CESAR/嵌入式/时序混合系统**；开创叙事归 Clarke 篇、CTL 时态逻辑归 Emerson 篇；共同部分一致即可，**页面无载的三人恩怨/优先权之争禁写**。
- **"独立研究"表述**：Emerson 页面明载 model checking 概念 `was independently studied by Joseph Sifakis in Europe`——Sifakis 篇可正面写"欧洲独立研究线"（有据），但**勿升级为"独立发明了 model checking 并被亏待"之类叙事**。
- **图灵奖中文口径**：Sifakis 页面对获奖理由的表述是 `for his work on model checking`——勿写成"因创立 CAV 会议获奖"或"因 SCADE 获奖"。
- **1974/1979 两级博士**：1974 是**工程博士**（doctorat d'ingénieur）、1979 是**国家博士**（doctorat d'état，当时任教授的必要门槛、后被 habilitation 取代）——两个学位名勿互串，且页面注须交代法国旧两级制。
- **VERIMAG 属性**：初期是 CNRS 与 **Verilog SA**（公司）的混合产业实验室；现为 CNRS、Joseph Fourier 大学、Grenoble-INP 联合实验室（页面脚注）——勿写成"CNRS 下属研究所"一笔带过。
- **CAV 创办人**：与 **Clarke、Pnueli** 三人共同创办，首届 1989 格勒诺布尔——Amir Pnueli 是 1996 图灵奖得主，可点出；勿漏 Pnueli 或写成 Sifakis 独自创办。
- **SCADE 与 Lustre**：页面表述为 VERIMAG 与 Airbus/Schneider 合作开发安全关键系统方法与工具，"in particular the SCADE synchronous programming environment based on the Lustre Language"——**勿写成 Sifakis 个人发明了 Lustre 或 SCADE**。
- **中国关联**：清华大学访问教授（2011–2012）、SUSTech 访问教授（2019）、**中国科学院外籍院士（2019）**——三项均页面实载可写；注意 SUSTech 是南方科技大学（页面 Welcome Sifakis @ SUCTech 来源），勿写错校名。
- **在世**：1946-12-26 生，**死亡日期留白**；页面写 lives in France——结尾页写"现居法国"而非"卒于"。
- **院士清单多而杂**：法/美/欧/中多国机构年份互串是最大风险——Grand Officer of National Order of Merit 2008、法国工程院 2008、Academia Europaea 2008、法国科学院 2010、荣誉军团指挥官 2011、Leonardo da Vinci Medal 2012、美国艺术与科学院 2015、美国工程院 2017、**中科院外籍院士 2019**、美国科学院 2024——逐项核对勿错年。
- **引语**：**全文无直接引语，勿编造**；获奖理由用页面转述句（for his work on model checking）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 约瑟夫·斯法基斯（或 斯法基斯） | 待写入 |
| name_en | Joseph Sifakis | 待写入 |
| birth_date | 1946-12-26 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Greece / France（Greek-French） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / model checking / embedded systems / formal verification | 待写入 |
| has_biography | 1 | 入库时置 1 |

## 7. 社会关系入库清单

- **CAV 共同创办人/合作者**：Edmund M. Clarke（2007 同奖）、Amir Pnueli（1996 图灵奖得主）
- **学术合作者**：Thomas Henzinger（timed/hybrid systems 验证）、Oded Maler（timed systems 综合）、Jean-Pierre Queille（其博士论文应用开发 CESAR）
- **博士门生（infobox notable students 实载）**：Stavros Tripakis、Susanne Graf、Sergio Yovine、Ahmed Bouajjani
- **配偶**：Olga Ioannidi（type=spouse）
- **博士导师**：页面无载禁写

## 8. 奖项清单

- A.M. Turing Award（2007，与 Clarke、Emerson 共享）
- Grand Officer of the National Order of Merit（法国，2008）
- Member of the French Academy of Engineering（法国工程院，2008）
- Member of Academia Europaea（2008）
- Commander of the Legion of Honor（法国荣誉军团勋章指挥官，2011）
- Leonardo da Vinci Medal（2012）
- Member of the French Academy of Sciences（法国科学院，2010）
- Member of the American Academy of Arts and Sciences（2015）
- Member of the National Academy of Engineering（美国，2017）
- Foreign member of the Chinese Academy of Sciences（中国科学院外籍院士，2019）
- Member of the National Academy of Sciences（美国，2024）

## 9. 机构清单

- 教育：National Technical University of Athens（电气工程 BS）；University of Grenoble（计算机科学 MS、工程博士 1974《Modèles temporels des systèmes logiques》、国家博士 1979《Le contrôle des systèmes asynchrones》）
- 任职：CNRS 研究总监（荣休 Research Director Emeritus）；VERIMAG 创始人兼台长（14 年，格勒诺布尔）；ARTIST 欧洲嵌入式卓越网络协调人（2004–2012）；INRIA-Schneider 产业讲席（2008–2011）；EPFL 全职教授兼 Rigorous System Design Laboratory 主任（2011–2016）；清华大学访问教授（2011–2012）；SUSTech 访问教授（2019）；希腊国家研究与技术委员会主席（2014–2016）

## 10. 终审清单

- [ ] 生 1946-12-26 Heraklion, Crete；在世留白，现居法国
- [ ] 国籍口径 Greek-French；封面 `希腊-法国`
- [ ] 图灵奖 citation 整句引用（注明 2007 共享 citation 来源）；页面口径 "for his work on model checking"
- [ ] 三人侧重区分：本篇只写 Verimag/CESAR/嵌入式/时序混合；无恩怨编造
- [ ] "欧洲独立研究线"表述有据（Emerson 页面 independently studied），不升级叙事
- [ ] 1974 工程博士 ≠ 1979 国家博士；法国旧两级博士制注交代
- [ ] VERIMAG 属性（CNRS×Verilog SA 混合产业实验室→三方联合）与 14 年台长准确
- [ ] CAV 创办人 = Clarke + Pnueli + Sifakis 三人，首届 1989 格勒诺布尔
- [ ] SCADE/Lustre 归 VERIMAG 产业合作成果，不写成个人发明
- [ ] 十一项荣誉年份逐一核对（尤其中科院外籍院士 2019、NAS 2024）
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2007/Joseph Sifakis/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2018 年肖像（`images/500px-Joseph_Sifakis_2018.jpg`）
- [ ] **国籍**：封面顶部徽章明示希腊-法国
- [ ] **引语核对**：全文无直接引语，勿编造；获奖理由用页面转述句
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Naur / Allen / Clarke / Emerson）格式对齐；三人篇目侧重复核不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
