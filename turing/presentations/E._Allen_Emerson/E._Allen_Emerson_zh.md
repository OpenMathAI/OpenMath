# E. Allen Emerson（E. 艾伦·爱默生）立传提示词

> qid=Q92821 · 1954-06-02 – 2024-10-15 · 美国计算机科学家 · 20 世纪 · 2007 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2007/E. Allen Emerson/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（CTL/CTL* 时态算子的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ernest Allen Emerson II（发表署名 E. Allen Emerson；中文惯称：E. 艾伦·爱默生）
- **生卒**：1954-06-02 生于 Dallas, Texas（美国）→ 2024-10-15 逝于 Austin, Texas 家中，享年 70（**死因页面未详述，勿编造**）
- **国籍**：美国（American）
- **身份**：计算机科学家；**模型检验发明与发展者之一**；UT Austin 教授（1981–2016），荣衔 Regents Chair Emeritus
- **家庭**：页面无载禁写（讣告来源为殡仪馆页面，仅姓名 Ernest "Allen" Emerson II）
- **教育轨迹**：
  - 早年计算经历：在 **Dartmouth Time-Sharing System** 与 Burroughs 大型机上接触 **BASIC、Fortran、ALGOL 60**
  - 1976 年 University of Texas at Austin **数学** BS
  - 1981 年 Harvard University **应用数学** PhD
- **博士导师**：Edmund M. Clarke（infobox 明载——即 2007 同奖导师，"一门双奖"）
- **研究领域**：计算机科学；时态逻辑（temporal logic）与模态逻辑（modal logic）、形式验证

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2007 图灵奖**：与导师 Clarke、Sifakis 三人共享；citation（页面实载整句必引）：`for their role in developing Model-Checking into a highly effective verification technology that is widely adopted in the hardware and software industries.`——本篇**侧重时态逻辑 CTL/CTL* 与"命名"故事**（Clarke 篇侧重开创与 CMU 工程化、Sifakis 篇侧重 Verimag/嵌入式）。
2. **与导师共同提出 model checking 并"命名"**：1980 年代初，Emerson 与其博士导师 Edmund M. Clarke 发展了对有限状态系统按形式规格验证的技术，**为他们提出的概念创造了术语 "model checking"（coined the term）**；该概念在欧洲被 Joseph Sifakis 独立研究（页面原文 independently studied）。
3. **CTL 的引入**：对时态逻辑与模态逻辑的贡献包括引入**计算树逻辑（Computation Tree Logic, CTL）**及其扩展 **CTL\***——用于并发系统验证的核心规格语言。
4. **1982 奠基论文**：与 Clarke 合著 *Design and synthesis of synchronization skeletons using branching time temporal logic*（用分叉时间时态逻辑设计与综合同步骨架，LNCS 131, 1982）——模型检验的奠基文献（工作于 1981）。
5. **CTL\* 与分叉 vs 线性时间（1986）**：与 Joseph Y. Halpern 合著 *"Sometimes" and "not never" revisited: on branching versus linear time temporal logic*（JACM 1986）——分叉时间与线性时间时态逻辑关系的经典工作。
6. **状态爆炸的对手**：模型检验的许多算法面临**组合爆炸**（combinatorial explosion / state space explosion）；Emerson 因与他人共同发展**符号模型检验**应对组合爆炸而获认可。
7. **1998 Paris Kanellakis Award**：与 Randal Bryant、Clarke、Kenneth L. McMillan 同获——citation（页面实载整句必引）：`For their invention of symbolic model checking, a method of formally checking system designs, which is widely used in the computer hardware industry and is beginning to show significant promise also in software verification and other areas.`
8. **UT Austin 三十五年（1981–2016）**：1981 年博士毕业即加入 UT Austin 计算机科学系，执教 35 年，2016 年退休，荣衔 Regents Chair Emeritus。
9. **ACM 评价**：ACM 页面称其"撰写了创立模型检验这一高度成功领域的奠基性论文"（`authored seminal papers that founded what has become the highly successful field of Model Checking`——页面引文实载）。
10. **"model" 的语义注**：model checking 中的 "model" 是数理逻辑**模型论**意义上的 model（系统是规格的 model）——页面 Notes 实载，可作技术注解页的点睛。
11. **荣誉**：Turing Award 2007、Paris Kanellakis Award 1998（两奖年份以页面为准：正文写 1998、infobox 亦作 1998；注意 Clarke 页面叙述作 1999——见 §5 裁定）。
12. **身后**：2024-10-15 于 Austin 家中去世，享年 70；CAV 2025 会议与 Heidelberg Laureate Forum 均发悼念（页面实载）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（时态逻辑 — 蓝） | `#2E5A9E` | CTL / CTL\* / 分叉 vs 线性时间 |
| 分类色 2（模型检验 — 青绿） | `#1E8E8E` | 术语命名 / 与 Clarke 的 1981–82 工作 |
| 分类色 3（符号模型检验 — 琥珀） | `#D9A441` | 组合爆炸 / Kanellakis 奖 |
| 分类色 4（并发系统验证 — 玫瑰） | `#C0395B` | 并发系统规格 / 形式验证 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：分叉时间树（计算树的时间分支节点），呼应「CTL 计算树 / 分叉时间」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：澄澈 / 逻辑之光（时态逻辑的形式之美、照亮并发系统的不可见结构）
- **选定曲目**：Alex-Productions **The Invisible Light**（manifest 预分配，直接沿用），匹配"为不可见的并发行为点亮形式之光"的叙事。
- **落地文件**：`turing/presentations/E._Allen_Emerson/TheInvisibleLight.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「时态逻辑与模型检验 · 美国」+ 爱默生 1954–2024 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1954–2024 生平纵览
4. **早年：Dallas 与分时系统**（1954–1976）：Dartmouth Time-Sharing System、BASIC/Fortran/ALGOL 60、UT Austin 数学 BS
5. **Harvard 应用数学博士**（1976–1981）：师从 Edmund M. Clarke
6. **1981–82：与导师提出并命名 model checking**：synchronization skeletons 论文、coined the term、Sifakis 欧洲独立研究
7. **CTL：计算树逻辑**：并发系统验证的规格语言
8. **CTL\* 与"Sometimes and not never revisited"**（1986，与 Halpern）：分叉 vs 线性时间
9. **组合爆炸与符号模型检验**：state space explosion、应对之道
10. **1998 Kanellakis 奖**：与 Bryant/Clarke/McMillan、citation 整句引用
11. **UT Austin 三十五年**（1981–2016）：Regents Chair Emeritus
12. **"model" 的模型论语义**：系统是规格的 model——技术注解页
13. **荣誉与谱系**：Turing 2007、一门双奖（导师 Clarke 2007 / 自己 2007）、ACM"奠基性论文"评价
14. **身后与纪念**：2024 年 10 月离世、CAV 2025 悼念
15. **结尾**：70 岁、为并发系统写下时间逻辑的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖 citation（整句必引）**：`for their role in developing Model-Checking into a highly effective verification technology that is widely adopted in the hardware and software industries.`——本篇三页中唯一页面实载 citation 全文者。
- **Kanellakis 奖年份裁定**：Emerson 页面（正文与 infobox）均作 **1998**；Clarke 页面正文作 1999——**以 Emerson 本篇页面 1998 为准**，可加注"Clarke 页面叙述作 1999"。入库核对表同口径。
- **命名权表述**：`They coined the term model checking`——Emerson 与 Clarke **创造了术语**；概念在欧洲被 Sifakis **独立研究**（independently studied）——"命名归师生二人、独立研究归 Sifakis"，勿写成"三人共同命名"或"Emerson 独自发明"。
- **本名与署名**：本名 **Ernest Allen Emerson II**，发表署名 **E. Allen Emerson**——标题与正文用 E. Allen Emerson，身份页注本名；勿与 E. Allen Emerson 的 "E." 误展开为 Edmund（那是导师）。
- **学位口径**：UT Austin **数学** BS（1976）→ Harvard **应用数学** PhD（1981）——勿写成计算机科学学位。
- **师承即同奖**：博士导师 Edmund M. Clarke 与其同获 2007 图灵奖——"一门双奖"是页面可推的实载事实（infobox advisor + 2007 共奖），可写；但**勿写"Emerson 是 Clarke 的学术继承人"之类页面无载的定位语**。
- **与 Halpern 论文**：1986 JACM 论文主题是**分叉时间 vs 线性时间时态逻辑**的关系（"Sometimes" and "not never" revisited）——勿把该论文写成"CTL 的提出"（CTL 提出在 1981/82 与 Clarke 的工作中）。
- **死因**：2024-10-15 于 Austin 家中去世，页面只写 died at his home…at the age of 70——**死因未详述，勿编造**。
- **符号模型检验归属**：Emerson `is also recognized along with others for developing symbolic model checking`——是"与其他人一道"（Kanellakis 四人组：Bryant/Clarke/McMillan）；BDD 细节在 Clarke 篇展开，本篇只写"应对组合爆炸"的角色。
- **早期计算经历**：Dartmouth Time-Sharing System + Burroughs 大型机 + BASIC/Fortran/ALGOL 60——是**中学-本科时代的接触**，勿写成正式计算机教育。
- **荣誉**：页面实载仅 Turing 2007 与 Kanellakis 1998 两项；**无**其他奖章（勿编造 NAE/Fellow 等页面未载荣誉）。
- **引语**：页面实载引文三处——2007 citation、1998 Kanellakis citation、ACM "seminal papers that founded…"；**其余无直接引语，勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | E. 艾伦·爱默生（或 爱默生） | 待写入 |
| name_en | E. Allen Emerson | 待写入 |
| birth_date | 1954-06-02 | 待写入 |
| death_date | 2024-10-15 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / temporal logic / model checking / formal verification | 待写入 |
| has_biography | 1 | 入库时置 1 |

## 7. 社会关系入库清单

- **博士导师**：Edmund M. Clarke（Harvard；2007 同奖导师，type=advisor-student，direction=advisor）
- **合作者**：Joseph Y. Halpern（1986 JACM CTL\*/分叉 vs 线性时间论文合著）
- **共享奖项同仁**：Randal Bryant、Edmund M. Clarke、Kenneth L. McMillan（Kanellakis 奖）；Joseph Sifakis（2007 图灵奖共享）
- **其他师承/门生**：页面无载禁写

## 8. 奖项清单

- A.M. Turing Award（2007，与 Clarke、Sifakis 共享）
- ACM Paris Kanellakis Award（1998，与 Bryant/Clarke/McMillan；注：Clarke 页面叙述作 1999，以本篇页面 1998 为准）

## 9. 机构清单

- 教育：University of Texas at Austin（数学 BS 1976）；Harvard University（应用数学 PhD 1981，导师 Clarke）
- 任职：University of Texas at Austin 计算机科学系（1981–2016，执教 35 年；退休荣衔 Regents Chair Emeritus）

## 10. 终审清单

- [ ] 生卒 1954-06-02 / 2024-10-15，享年 70，出生地 Dallas TX，去世地 Austin TX 家中，死因未详述勿编造
- [ ] 图灵奖 citation 与 Kanellakis citation 两句整句引用无误
- [ ] Kanellakis 年份以 1998 为准（本篇页面口径），注明 Clarke 页面差异
- [ ] "coined the term model checking（与 Clarke）+ Sifakis independently studied"表述准确
- [ ] 本名 Ernest Allen Emerson II / 署名 E. Allen Emerson 区分清楚
- [ ] "一门双奖"表述有据（infobox advisor + 2007 共奖），无过度定位语
- [ ] CTL 提出归 1981/82 与 Clarke 的工作；1986 论文只写分叉 vs 线性时间
- [ ] 学位口径：UT Austin 数学 BS、Harvard 应用数学 PhD
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Harvard · UT Austin | Turing 2007`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2007/E. Allen Emerson/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2022 年肖像（`images/500px-E-allen-emerson_3x4_cropped_.jpg`，页面明注 "Emerson in 2022"）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（三处 citation/评价引文）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Naur / Allen / Clarke / Sifakis）格式对齐；三人篇目侧重复核不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
