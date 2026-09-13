# Jack Dongarra（杰克·唐加拉）立传提示词

> qid=Q92670 · 1950-07-18 –（在世留白）· 美国计算机科学家、数学家 · 20/21 世纪 · 2021 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2021/Jack Dongarra/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。（真实肖像：`images/500px-Jack-dongarra-2022.jpg`）
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（线性代数库分层 / 矩阵特征值问题 / 并行消息传递模型的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jack Joseph Dongarra（中文惯称：杰克·唐加拉）；FRS（英国皇家学会外籍院士）
- **生卒**：1950-07-18 生于 Chicago, Illinois, U.S. → **在世，卒年留白**
- **国籍**：美国（American）
- **身份**：计算机科学家、数学家；University of Tennessee 电气工程与计算机科学系 University Distinguished Professor Emeritus；Manchester 大学数学学院 Turing Fellowship；Rice University 计算机系兼职教授；UTK Innovative Computing Laboratory **创始主任**
- **家庭**：页面未载家庭细节，勿编造
- **教育轨迹**：
  - 1972 年 Chicago State University **数学**学士（BSc）
  - 1973 年 Illinois Institute of Technology **计算机科学**硕士（MSc）
  - 1980 年 University of New Mexico **应用数学**博士（PhD）；论文 *Improving the Accuracy of Computed Matrix Eigenvalues*
- **博士导师**：Cleve Moler（勿添加"MATLAB 之父"等页面未载的关联）
- **研究领域**：线性代数数值算法、并行计算、先进计算机体系结构、高性能数学软件

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2021 图灵奖**：获奖理由**整句可引**："for pioneering contributions to numerical algorithms and libraries that enabled high performance computational software to keep pace with exponential hardware improvements for over four decades."——页面并评述其算法与软件"推动了高性能计算的成长"，影响从人工智能到计算机图形学。
2. **数学软件全家桶（known for 清单）**：EISPACK、LINPACK、BLAS、LAPACK、ScaLAPACK、PVM、MPI、NetSolve、TOP500、ATLAS、HPCG、PAPI——设计、实现、测试与文档全覆盖。
3. **生态辐射**：其库被 MATLAB、Maple、Wolfram Mathematica、GNU Octave、R、SciPy 等广泛集成——"数值算法的准确性 + 软件可靠性与性能"两条腿。
4. **Argonne 岁月**：在 Argonne National Laboratory 工作至 1989 年，官至 senior scientist。
5. **Netlib 先驱**：与 Eric Grosse 开创通过电子邮件与 Web 分发数值开源代码的 Netlib——软件共享基础设施的早期样板。
6. **并行标准两支柱**：PVM（Parallel Virtual Machine）与 MPI（Message Passing Interface）——并行计算消息传递事实标准（均为页面实载的参与设计/实现项目）。
7. **Top500 榜单**：页面 known for 实载 TOP500——高性能计算排名榜（细节机制页面未载，勿展开编造）。
8. **学术产出**：约 300 篇文章、论文、报告与技术备忘录，多部合著书籍。
9. **跨国任职**：Manchester 大学 Turing Fellow（2007 年起）；Texas A&M University Institute for Advanced Study faculty fellow（2014–2018）；机构履历含 Tennessee、New Mexico、Rice、Argonne、Oak Ridge、Manchester。
10. **荣誉大满贯**：NAE（2001）、NAS（2023）、英国皇家学会外籍院士 ForMemRS（2019）、俄罗斯科学院外籍院士、ACM/IEEE/SIAM/AAAS Fellow；2013 ACM/IEEE Ken Kennedy Award（表彰数学软件标准的设计与推广领导力）。
11. **两项"首位"**：2008 年**首位** IEEE Medal of Excellence in Scalable Computing 得主；2010 年**首位** SIAM Activity Group on Supercomputing Career Prize 得主（页面明载 "the first recipient"，可写）。
12. **2024 荣誉博士**：希腊 Ionian University 信息学系荣誉博士。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（数值线性代数 — 蓝） | `#2E5A9E` | LINPACK / LAPACK / BLAS |
| 分类色 2（并行计算 — 青绿） | `#1E8E8E` | PVM / MPI / ScaLAPACK |
| 分类色 3（基准与榜单 — 琥珀） | `#D9A441` | Top500 / HPCG / PAPI / ATLAS |
| 分类色 4（开源软件分发 — 玫瑰） | `#C0395B` | Netlib / EISPACK 传承 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：矩阵网格与性能曲线（稀疏网格线 + 上升折线），呼应「数值软件跟上硬件指数增长」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：深沉 / 厚积薄发（四十年如一日打磨数学软件基础设施）
- **选定曲目**：Alex-Productions **PAST**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Jack_Dongarra/PAST.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「高性能计算软件奠基人 · 美国」+ Dongarra 1950– + 右上真实肖像（Jack-dongarra-2022）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1950–至今 生平纵览
4. **芝加哥数学少年**（1950–1973）：Chicago State 数学、IIT 计算机科学
5. **新墨西哥师从 Cleve Moler**（1980）：矩阵特征值精度博士论文
6. **Argonne 岁月**（–1989）：senior scientist、数值软件起步
7. **EISPACK → LINPACK：线性代数软件的奠基**：known for 链条前半
8. **BLAS → LAPACK → ScaLAPACK：三层库体系**：公式框展示分层结构
9. **PVM 与 MPI：并行计算的消息传递标准**
10. **Netlib 与 Top500**：与 Eric Grosse 的开源分发先驱、榜单实载口径
11. **田纳西与 ICL**：Innovative Computing Laboratory 创始主任、Manchester Turing Fellow、Rice 兼职
12. **生态辐射**：MATLAB/Maple/Mathematica/Octave/R/SciPy
13. **荣誉墙**：两项"首位"奖、Ken Kennedy 2013、ForMemRS 2019、NAS 2023
14. **2021 图灵奖**：获奖理由整句引用 + 影响评述（AI 到图形学）
15. **结尾**：四十年数学软件基础设施的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：整句引用（亮点 1 原文），这是本篇核心红线；页面上另有 intro 短句，**以 ACM 整句 citation 为准**。
- **Fernbach 奖年份冲突**：infobox 作 **2003**（IEEE Computer Society Sidney Fernbach Memorial Award），正文作 "In 2004"——**两处不一致，以 infobox 2003 为准并在终审核对**，勿写错年份。
- **两项"首位"可写**：2008 IEEE Scalable Computing Medal、2010 SIAM SIAG Supercomputing Career Prize——页面明载 "the first recipient"；除此之外的"首位/第一"表述页面无载禁写。
- **导师口径**：博士导师 Cleve Moler；页面**未载** Moler 与 MATLAB 的关系，立传勿引入 MATLAB 创作叙事。
- **Top500 细节红线**：页面仅把 TOP500 列入 known for——勿编造"Top500 使用 LINPACK Benchmark"等机制细节（页面未载）。
- **MPI/PVM 口径**：表述为"参与设计与实现的开源软件包与系统"，勿写"Dongarra 发明 MPI"。
- **俄罗斯科学院外籍院士**：页面实载可列（ Fellow 清单内），一笔带过不渲染。
- **在世**：无卒年，写 `1950–`，留白；家庭/死因页面未载勿编造。
- **国籍**：美国，生于芝加哥——勿写移民背景（页面未载）。
- **引语**：除 2021 图灵奖 citation 外全文无其他直接引语，勿编造。
- **软件清单勿漏**：known for 含 EISPACK/HPCG/PAPI/ATLAS/NetSolve 等，页面分组展示时至少覆盖 EISPACK/LINPACK/BLAS/LAPACK/ScaLAPACK/PVM/MPI/Top500 四组主线。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 唐加拉（或 杰克·唐加拉） | 待写入 |
| name_en | Jack Dongarra | 待写入 |
| birth_date | 1950-07-18 | 待写入 |
| death_date | 空（在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | numerical linear algebra / parallel computing / high-performance computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Cleve Moler（University of New Mexico 应用数学）
- **合作者**：Eric Grosse（Netlib 开创者之一）
- **门生/其他**：页面未载博士学生名单，**门生关系禁写**；机构同僚（Argonne/Oak Ridge/Tennessee/Manchester/Rice）不入关系库

## 8. 奖项清单

- Turing Award（2021）
- Fellow of AAAS（1994）
- IEEE Fellow（1999）
- ACM Fellow（2001）、NAE 院士（2001）
- IEEE Computer Society Sidney Fernbach Memorial Award（infobox 2003 / 正文 2004，两处冲突以 infobox 为准）
- IEEE Medal of Excellence in Scalable Computing（2008，首位得主）
- SIAM SIAG on Supercomputing Career Prize（2010，首位得主）
- IEEE Computer Society Charles Babbage Award（2011）
- ACM/IEEE Ken Kennedy Award（2013）
- SIAM/ACM Prize in Computational Science and Engineering（2019）
- 英国皇家学会外籍院士 ForMemRS（2019）
- IEEE Computer Pioneer Award（2020）
- NAS 院士（2023）
- SIAM Fellow（2009）、俄罗斯科学院外籍院士
- Ionian University 荣誉博士（2024）

## 9. 机构清单

- 教育：Chicago State University（数学 BSc 1972）、Illinois Institute of Technology（计算机科学 MSc 1973）、University of New Mexico（应用数学 PhD 1980）
- 任职：Argonne National Laboratory（至 1989，senior scientist）、University of Tennessee（University Distinguished Professor Emeritus；ICL 创始主任）、University of Manchester（Turing Fellow，2007 年起）、Rice University（兼职教授）、Texas A&M University IAS（faculty fellow 2014–2018）；机构履历另含 Oak Ridge National Laboratory、University of New Mexico

## 10. 终审清单

- [ ] 生卒 1950-07-18 / 在世留白，出生地 Chicago, Illinois
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Tennessee · Argonne · Manchester | Turing 2021`
- [ ] 图灵奖理由整句引用与原文逐字一致
- [ ] Fernbach 奖年份按 infobox 2003 处理（正文 2004 冲突已注记）
- [ ] 两项"首位"（2008/2010）表述准确，无其他杜撰"首位"
- [ ] Top500/MPI/PVM 表述不超出页面实载口径
- [ ] Cleve Moler 未被添加 MATLAB 关联
- [ ] 无门生名单 → 社会关系仅导师 + Grosse 合作者
- [ ] 肖像使用 `images/500px-Jack-dongarra-2022.jpg`（取 500px 最大版）
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2021/Jack Dongarra/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2022 年肖像（`images/500px-Jack-dongarra-2022.jpg`，取最大可用版；250px 版不用）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅图灵奖 citation 可在 Wikipedia 原文找到，其余不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky / John_McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Aho/Ullman/Metcalfe/Wigderson）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
