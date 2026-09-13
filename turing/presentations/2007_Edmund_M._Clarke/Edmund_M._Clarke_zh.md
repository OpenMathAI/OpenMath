# Edmund M. Clarke（埃德蒙·克拉克）立传提示词

> qid=Q92819 · 1945-07-27 – 2020-12-22 · 美国计算机科学家 · 20 世纪 · 2007 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2007/Edmund M. Clarke/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（模型检验「系统 M ⊨ 规格 φ」的判定表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Edmund Melson Clarke, Jr.（中文惯称：埃德蒙·克拉克）
- **生卒**：1945-07-27 生于 Newport News, Virginia（美国）→ 2020-12-22 逝于 Pittsburgh, Pennsylvania，享年 75；**死于 COVID-19**（2020 年宾州疫情期间；其子 James S. Clarke 在 Twitter 公布——页面实载可写）
- **国籍**：美国（American）
- **身份**：计算机科学家、学者；**模型检验（model checking）的开创者之一**；CMU **FORE Systems 计算机科学讲席教授**（FORE Systems Professor of Computer Science）
- **家庭**：页面仅载其子 James S. Clarke（讣告推文来源）；其余家庭细节无载禁写
- **教育轨迹**：
  - 1967 年 University of Virginia, Charlottesville **数学** BA
  - 1968 年 Duke University, Durham NC **数学** MA
  - 1976 年 Cornell University, Ithaca NY **计算机科学** PhD；论文《Completeness and Incompleteness Theorems for Hoare-Like Axiom Systems》
- **博士导师**：Robert Lee Constable（Cornell，infobox 明载）
- **研究领域**：计算机科学；软件与硬件验证、自动定理证明

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **模型检验开创者（1981，与博士生 Emerson）**：`In 1981 he and his Ph.D. student E. Allen Emerson first proposed the use of model checking as a verification technique for finite-state concurrent systems.`——对有限状态并发系统的形式验证技术；本篇**侧重开创叙事**：从定理证明的困境转向"自动检验有限状态系统"的新思路（与 Emerson 篇侧重 CTL 时态逻辑、Sifakis 篇侧重 Verimag/嵌入式区分）。
2. **博士论文的伏笔（1976）**：证明某些程序语言控制结构**没有**好的 Hoare 式证明系统——为"换一条验证路线"埋下伏笔；此消彼长引出模型检验。
3. **1981/1982 论文**：与 Emerson 的 *Design and synthesis of synchronization skeletons using branching time temporal logic*（分叉时间时态逻辑的同步骨架设计与综合，工作 1981、LNCS 131 出版 1982，见 Emerson 页参考文献）——模型检验的奠基文献。
4. **CMU 四十年**：Duke 任教两年（1976–1978）→ Harvard 应用科学部助理教授（1978–1982）→ 1982 年加入 Carnegie Mellon 计算机科学系；1989 年正教授；**1995 年成为 FORE Systems 讲席的首位获得者**；2008 年 university professor；2015 年荣休（emeritus）。
5. **硬件验证的先驱团队**：他的研究组**开创了模型检验在硬件验证中的应用**。
6. **符号模型检验与 BDD**：使用**二元决策图（binary decision diagrams, BDD）**的符号模型检验由其团队发展；这是 **Kenneth L. McMillan 博士论文**的主题，该论文获 ACM Doctoral Dissertation Award。
7. **定理证明器的两面**：团队开发了首个并行归结定理证明器 **Parthenon** 与基于符号计算系统的定理证明器 **Analytica**——"验证"两条腿（模型检验 + 定理证明）兼备。
8. **CMACS 中心（2009）**：主持创建 NSF 资助的 Computational Modeling and Analysis of Complex Systems 中心——多校团队把抽象解释与模型检验用于**生物与嵌入式系统**。
9. **巴黎 Kanellakis 奖（1999）**：与 Randal Bryant、E. Allen Emerson、Kenneth L. McMillan 同获 ACM Paris Kanellakis Award——**符号模型检验**的开发。
10. **学术谱系**：著名博士生 E. Allen Emerson、Bhubaneswar Mishra、David L. Dill、Kenneth L. McMillan（infobox 实载）——一门两代同列图灵奖（Clarke 2007 / Emerson 2007）+ McMillan 承其 BDD 路线。
11. **荣誉**：Herbrand Award 2008（"recognition of his role in the invention of model checking and his sustained leadership in the area for more than two decades"——页面实载引文）、NAE 2005、Bower Award 2014、TU Wien 荣誉博士 2012 等（详见 §8）；ACM 与 IEEE Fellow、Sigma Xi 与 Phi Beta Kappa 成员。
12. **2007 图灵奖**：与 Emerson、Sifakis 三人共享；citation（本页面未载、见本批次 Emerson 页面实载）：`for their role in developing Model-Checking into a highly effective verification technology that is widely adopted in the hardware and software industries.`

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（模型检验 — 蓝） | `#2E5A9E` | 1981 与 Emerson 论文 / 有限状态并发系统 |
| 分类色 2（符号模型检验 — 青绿） | `#1E8E8E` | BDD / McMillan / Kanellakis 奖 |
| 分类色 3（定理证明 — 琥珀） | `#D9A441` | Hoare 式系统不可能性 / Parthenon / Analytica |
| 分类色 4（产业与交叉应用 — 玫瑰） | `#C0395B` | 硬件验证产业 / CMACS 生物与嵌入式 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：状态迁移图（圆角状态节点 + 标注迁移边），呼应「有限状态系统 / model checking」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：升腾 / 奠基（从"证明不可能"到"检验一切硬件"的开创）
- **选定曲目**：Alex-Productions **Ascension**（manifest 预分配，直接沿用），匹配"模型检验升格为产业标准技术"的上升叙事。
- **落地文件**：`turing/presentations/Edmund_M._Clarke/Ascension.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「模型检验开创者 · 美国」+ 克拉克 1945–2020 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1945–2020 生平纵览
4. **早年与数学训练**（1945–1968）：Newport News 出生、Virginia 数学 BA、Duke 数学 MA
5. **Cornell 博士：证明"不可能"**（1976）：Constable 门下、Hoare 式公理系统的不完备定理
6. **Duke 与 Harvard**（1976–1982）：Duke 两年、Harvard 应用科学部助理教授
7. **1981：模型检验的诞生**：与博士生 Emerson、有限状态并发系统验证、synchronization skeletons 论文
8. **落脚 CMU**（1982–）：加入 CMU CS 系、1989 正教授、1995 首任 FORE Systems 讲席
9. **硬件验证的先驱**：研究组开创模型检验的硬件应用
10. **符号模型检验与 BDD**：binary decision diagrams、McMillan 博士论文、ACM 博士论文奖
11. **定理证明的另一条腿**：Parthenon（首个并行归结定理证明器）与 Analytica
12. **CMACS：走向生物与嵌入式**（2009）：NSF 中心、抽象解释 + 模型检验
13. **荣誉与谱系**：Kanellakis 1999、Herbrand 2008、NAE 2005；博士生 Emerson/Mishra/Dill/McMillan
14. **2007 图灵奖**：与 Emerson、Sifakis 共享、citation 整句引用
15. **结尾**：75 岁（COVID-19 离世）、模型检验从论文走向芯片产业的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖 citation**：Clarke 页面本身**未载 citation 全文**；共享 citation 见本批次 Emerson 页面——写作时引用 `for their role in developing Model-Checking into a highly effective verification technology that is widely adopted in the hardware and software industries.`，并在核查备注注明来源为 2007 共享 citation。
- **三人侧重区分**：Clarke 篇**只侧重开创叙事 + CMU 团队工程化**；CTL 时态逻辑细节归 Emerson 篇、Verimag/CESAR/嵌入式归 Sifakis 篇；共同部分一致即可，**页面无载的三人恩怨/优先权之争禁写**。
- **"独立研究"表述**：Emerson 页面明载 model checking 概念 `was independently studied by Joseph Sifakis in Europe`——在 Clarke 篇只写"1981 与 Emerson 首先提出"（页面原文 first proposed），**勿写"三人共同发明"抹平 Sifakis 的独立线，也勿写"Clarke 独创"**。
- **1981 vs 1982**：提出于 **1981**（页面明载 In 1981… first proposed）；synchronization skeletons 论文 LNCS 131 **出版于 1982**——两个年份都要交代清楚，勿混为一谈。
- **博士论文是"否定性结果"**：1976 论文证明某些控制结构**没有**好的 Hoare 式证明系统——是"证明不可能"，勿写成"完善 Hoare 逻辑"。
- **BDD 符号模型检验的归属**：页面明载"由他的团队发展"（developed by his group），是 **McMillan 博士论文**主题——归功表述为"Clarke 团队 / McMillan 论文"，勿写成 Clarke 个人单独发明。
- **去世原因**：**COVID-19**，2020-12-22，Pittsburgh，享年 75——页面明载可写；其子推文作为信息来源一笔带过即可。
- **学位口径**：BA 数学（Virginia 1967）/ MA 数学（Duke 1968）/ PhD 计算机科学（Cornell 1976）——Duke 是**硕士**勿写成"博士前任教"混淆；Duke 任教是 PhD 之后两年。
- **FORE Systems 讲席**：1995 年成为该讲席**首位获得者**（first recipient）——"首位"限定于此。
- **Harvard 职衔**：Division of Applied Sciences 的 **assistant professor**——勿拔高为正教授。
- **荣誉年份**：SRC Technical Excellence 1995、Allen Newell 奖 1999（CMU CS 系）、Kanellakis 1999、Harry H. Goode 2004、NAE 2005、Herbrand 2008、TU Wien 荣誉博士 2012、AAAS 2011、Bower Award 2014——年份勿互串；无 Nobel、无 Japan Prize（勿编造）。
- **引语**：页面仅 Herbrand Award 的授奖语引文（…invention of model checking…sustained leadership…more than two decades）为实载引文；**其余无直接引语，勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 埃德蒙·克拉克（或 克拉克） | 待写入 |
| name_en | Edmund M. Clarke | 待写入 |
| birth_date | 1945-07-27 | 待写入 |
| death_date | 2020-12-22 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / model checking / formal verification | 待写入 |
| has_biography | 1 | 入库时置 1 |

## 7. 社会关系入库清单

- **博士导师**：Robert Lee Constable（Cornell，infobox 明载，type=advisor-student，direction=advisor）
- **博士门生**：E. Allen Emerson（2007 图灵奖）、Bhubaneswar Mishra、David L. Dill、Kenneth L. McMillan（infobox 实载）
- **共享奖项同仁**：Randal Bryant、E. Allen Emerson、Kenneth L. McMillan（1999 Kanellakis 奖，符号模型检验）；Joseph Sifakis（2007 图灵奖共享）
- **其他**：页面未载明其他师承/合作者（Harvard/CMU 同事无实名，禁写）

## 8. 奖项清单

- A.M. Turing Award（2007，与 Emerson、Sifakis 共享）
- Semiconductor Research Corporation Technical Excellence Award（1995）
- Allen Newell Award for Excellence in Research（CMU 计算机科学系，1999）
- ACM Paris Kanellakis Award（1999，与 Bryant/Emerson/McMillan，符号模型检验）
- IEEE Computer Society Harry H. Goode Memorial Award（2004）
- National Academy of Engineering 院士（2005）
- Herbrand Award（2008，授奖语见 §5）
- American Academy of Arts and Sciences 院士（2011）
- TU Wien 荣誉博士（2012）
- Franklin Institute Bower Award and Prize for Achievement in Science（2014）
- ACM Fellow、IEEE Fellow；Sigma Xi、Phi Beta Kappa 成员

## 9. 机构清单

- 教育：University of Virginia（数学 BA 1967）；Duke University（数学 MA 1968）；Cornell University（计算机科学 PhD 1976，论文《Completeness and Incompleteness Theorems for Hoare-Like Axiom Systems》）
- 任职：Duke University 计算机科学系（1976–1978，两年）；Harvard University Division of Applied Sciences 助理教授（1978–1982）；Carnegie Mellon University 计算机科学系（1982–，1989 正教授、1995 首任 FORE Systems 讲席、2008 university professor、2015 emeritus）；CMACS 中心主任（2009，NSF）

## 10. 终审清单

- [ ] 生卒 1945-07-27 / 2020-12-22，享年 75，出生地 Newport News VA，去世地 Pittsburgh PA，死因 COVID-19
- [ ] 图灵奖 citation 整句引用（注明为 2007 共享 citation）
- [ ] "1981 first proposed（与博士生 Emerson）+ 1982 论文出版"两个年份分开交代
- [ ] 三人侧重区分：本篇只写开创 + CMU 工程化；CTL 归 Emerson 篇、Verimag 归 Sifakis 篇；无恩怨编造
- [ ] 博士论文"否定性结果"（Hoare 式系统不可能性）表述准确
- [ ] 符号模型检验归"Clarke 团队 / McMillan 博士论文"，非个人独揽
- [ ] 学位口径 BA/MA/PhD 与任职序列 Duke→Harvard→CMU 准确；FORE 讲席"首位获得者"限定语保留
- [ ] 引语仅 Herbrand 授奖语，无编造
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Cornell · Harvard · CMU | Turing 2007`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2007/Edmund M. Clarke/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 FLoC 2006 会议照（`images/Edmund_Clarke_FLoC_2006.jpg` 或其 250px 版；目录中 red question mark 占位图勿用）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（Herbrand 授奖语 + 2007 共享 citation）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Naur / Allen / Emerson / Sifakis）格式对齐；三人篇目侧重复核不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
