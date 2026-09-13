# James H. Wilkinson（詹姆斯·H·威尔金森）立传提示词

> qid=Q62877 · 1919-09-27 – 1986-10-05 · 英国数值分析学家 · 20 世纪 · 1970 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1970/James H. Wilkinson/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（向后误差分析 / 舍入误差 / 特征值问题的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：James Hardy Wilkinson（中文惯称：詹姆斯·H·威尔金森，人称 Jim Wilkinson）
- **生卒**：1919-09-27 生于 Strood（英格兰）→ 1986-10-05 逝于 Teddington（英格兰），享年 67（在家中因心脏病去世）
- **国籍**：英国（British / England）
- **身份**：数值分析学家（numerical analysis，应用数学与计算机科学的交叉领域）
- **家庭**：1945 年与 Heather Ware 结婚；身后遗有妻子和一个儿子（一个女儿先于他去世）
- **教育轨迹**：
  - 中学：凭 Foundation Scholarship 奖学金入读 Sir Joseph Williamson's Mathematical School（Rochester）
  - Trinity College, Cambridge，修读 Cambridge Mathematical Tripos，以 **Senior Wrangler**（数学荣誉学位考试第一名）毕业（BA）
- **领域**：Numerical Analysis、Numerical linear algebra
- **任职**：National Physical Laboratory（NPL，1946 年起直至去世；1940 年起先从事弹道学战时工作）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **与 Alan Turing 共事**：1946 年转入 NPL 后与图灵同在 **ACE 计算机项目**工作——图灵奖得主中的"图灵同事"（1980 年还撰写了关于 Turing 在 NPL 工作与 Pilot ACE 建造的历史回顾文章）。
2. **Senior Wrangler**：剑桥数学 Tripos 荣誉榜首——英国数学界的传奇名次（历史上 Senior Wrangler 名单包括 Rayleigh、Kelvin 等名家，但勿延伸罗列，本页 Wikipedia 无载）。
3. **向后误差分析（backward error analysis）**：Wilkinson 的标志性贡献——把浮点舍入误差解释为"对输入的扰动"，使数值算法的稳定性可以严格证明；1970 年图灵奖理由中特别点名 "'backward' error analysis"。
4. **矩阵特征值算法**：在线性代数计算（尤其特征值问题）上发现许多重要算法；QR 类特征值方法时代的奠基人物之一（本页以 "computations in linear algebra" 概括，勿展开命名具体算法细节）。
5. **两本经典专著**：*Rounding Errors in Algebraic Processes*（1963，简称 REAP）、*The Algebraic Eigenvalue Problem*（1965，简称 AEP，牛津 Clarendon）；与 Christian Reinsch 合编 *Handbook for Automatic Computation, Vol. II: Linear Algebra*（Springer, 1971）。
6. **以其命名之物**：Wilkinson 矩阵（Wilkinson matrix）、Wilkinson 多项式（Wilkinson's polynomial）——数值分析的著名病态实例；其 1984 年论文 *The Perfidious Polynomial*（"奸诈的多项式"）即讲多项式求根的病态性，为此获 1987 年 MAA **Chauvenet Prize**。
7. **两个以其命名的奖项**：SIAM 于 1982 年设立 *James H. Wilkinson Prize in Numerical Analysis and Scientific Computing*；1991 年设立 *J. H. Wilkinson Prize for Numerical Software*——数值分析界的青年学者荣誉传承。
8. **图灵奖（1970）**：获奖理由原文 "for his research in numerical analysis to facilitate the use of the high-speed digital computer, having received special recognition for his work in computations in linear algebra and 'backward' error analysis"（为促进高速数字计算机的使用而在数值分析领域的研究，在线性代数计算与"向后"误差分析方面的工作尤受表彰）。
9. **同年 von Neumann Lecture**：1970 年还获邀作 SIAM **John von Neumann Lecture**。
10. **荣誉清单**：FRS 皇家学会院士（1969）、Heriot-Watt University 荣誉博士（1973）、British Computer Society **Distinguished Fellow**（1974，表彰其在计算机科学的开创性工作）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（数值分析 — 蓝） | `#2E5A9E` | 数值分析 / NPL |
| 分类色 2（误差分析 — 青绿） | `#1E8E8E` | 向后误差分析 / 舍入误差 |
| 分类色 3（线性代数 — 琥珀） | `#D9A441` | 特征值问题 / 两本专著 |
| 分类色 4（传承 — 玫瑰） | `#C0395B` | Wilkinson 奖项 / 命名遗产 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏细网格线，呼应「误差、精度、计算表」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：严谨 / 沉静（数值分析家的精确与时间感）
- **选定曲目**：Alex-Productions **The Flow of Time**（沉稳 / 纪录片），匹配"为高速计算机奠基数值基石"的叙事；与 Minsky/Knuth 等的 New Lands、Lamport 的 Timeless 区分。
- **落地文件**：`turing/presentations/James_H._Wilkinson/TheFlowOfTime.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「数值分析奠基人 · 英国」+ Wilkinson 1919–1986 + 右上头像（与图灵奖奖杯合影）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1919–1986 生平纵览
4. **早年：Strood 少年与剑桥榜首**（1919–1940）：奖学金中学、Trinity College、Senior Wrangler
5. **战时弹道与 NPL**（1940–1946）：弹道学战时工作、1946 转入 NPL
6. **与图灵共事 ACE**（1946–）：ACE 计算机项目、Pilot ACE、1980 年历史回顾文章
7. **向后误差分析**：舍入误差的"输入扰动"解释、算法稳定性的严格证明
8. **矩阵特征值计算**：线性代数算法、Wilkinson 矩阵
9. **Wilkinson 多项式与病态问题**：*The Perfidious Polynomial*（1984）、病态多项式
10. **两本经典专著**：REAP 1963 / AEP 1965 / Handbook with Reinsch 1971
11. **图灵奖 1970**：获奖理由原文（数值分析 + 线性代数 + 向后误差分析）、同年 von Neumann Lecture
12. **荣誉**：FRS 1969、Heriot-Watt 1973、DFBCS 1974、Chauvenet Prize 1987
13. **以他命名的奖项**：SIAM Wilkinson Prize（1982）/ Wilkinson Prize for Numerical Software（1991）
14. **遗产**：数值分析与数值线性代数的奠基者、NPL 传统
15. **结尾**：67 岁、病态多项式的"奸诈"与数值分析家的严谨

## 5. 史实陷阱与敏感点（终审必须检查）

- **Senior Wrangler**：是剑桥数学荣誉学位考试（Mathematical Tripos）**第一名**的名次称谓——勿误写为"博士第一名"或"一等奖学金"。
- **与图灵的关系**：是 NPL ACE 项目的**同事**（1946 年起），**无师承关系**——勿写"图灵的学生/博士导师"。
- **获奖理由**：必须包含三要素——数值分析研究促进高速数字计算机的使用、线性代数计算、"'backward' error analysis"（带引号的 backward）——勿简化为只写其一。
- **教育学位**：页面只载 Cambridge BA（Tripos）——**未载硕士/博士学位**，勿编造。
- **Chauvenet Prize 1987**：他 1986-10-05 去世，奖为 1987 年（因 1984 年论文）——写明年份即可，"身后获奖"的措辞可保留时间线事实（先卒后奖），但勿渲染。
- **Wilkinson 多项式/矩阵**：页面仅在 Known for 提及名称——可写"以其命名"，病态性解释限于 *The Perfidious Polynomial* 论文与多项式求根的关联，勿展开页面无载的细节（如具体病态根的数值例子，若需须另行核实）。
- **生卒**：1919-09-27 ~ 1986-10-05，享年 67，出生地 Strood，去世地 Teddington（家中，心脏病）；女儿先于他去世——家庭表述须准确。
- **荣誉边界**：FRS 1969、Heriot-Watt 荣誉博士 1973、DFBCS 1974、Chauvenet 1987、图灵奖 1970、von Neumann Lecture 1970——**无** Nobel、无 National Medal（勿编造）。
- **国籍**：英国；机构终身 NPL（1946 起）——总表"获奖时机构 National Physical Laboratory"正确。
- **两本专著缩写**：REAP（1963）、AEP（1965）——年份与出版社（Prentice-Hall / Oxford Clarendon）勿混淆。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q62877 | 待写入 |
| name_zh | 威尔金森（或 詹姆斯·威尔金森） | 待写入 |
| name_en | James H. Wilkinson | 待写入 |
| birth_date | 1919-09-27 | 待写入 |
| death_date | 1986-10-05 | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | numerical analyst / computer scientist | 待写入 |
| field_of_work | numerical analysis / numerical linear algebra | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **同事**：Alan Turing（NPL ACE 计算机项目）、Christian Reinsch（合编 Handbook for Automatic Computation Vol. II）
- **无载禁写**：页面未载其博士导师（Tripos 本科无导师信息）、未载著名学生——**勿编造导师/门生关系**。

## 8. 奖项清单

- ACM Turing Award（1970，图灵奖）
- SIAM John von Neumann Lecture（1970，受邀演讲）
- FRS 皇家学会院士（1969）
- Heriot-Watt University Honorary Doctorate（1973）
- Distinguished Fellow of the British Computer Society（1974）
- Chauvenet Prize（Mathematical Association of America，1987，因论文 *The Perfidious Polynomial*）
- 纪念奖项：SIAM James H. Wilkinson Prize in Numerical Analysis and Scientific Computing（1982 设立）、J. H. Wilkinson Prize for Numerical Software（1991 设立）

## 9. 机构清单

- 教育：Sir Joseph Williamson's Mathematical School（Rochester）、Trinity College, Cambridge（BA，Senior Wrangler）
- 任职：战时弹道学工作（1940–1946）→ National Physical Laboratory（1946 起，与图灵共事 ACE 项目，此后终身 NPL）

## 10. 终审清单

- [ ] 生卒 1919-09-27 / 1986-10-05，享年 67，出生地 Strood，去世地 Teddington（家中心脏病）
- [ ] Senior Wrangler = 剑桥数学 Tripos 第一名，表述准确
- [ ] 与图灵为 NPL ACE 项目同事、无师承关系
- [ ] 图灵奖理由三要素齐全（数值分析 / 线性代数计算 / 向后误差分析）
- [ ] REAP 1963 / AEP 1965 / Handbook（with Reinsch）1971 年份准确
- [ ] Chauvenet 1987（因 1984 论文）与 FRS 1969 / DFBCS 1974 年份准确
- [ ] 国籍用「英国」，封面底部状态栏 `英国 | National Physical Laboratory | Turing 1970`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1970/James H. Wilkinson/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `turing/pages/1970/James H. Wilkinson/images/James_H._Wilkinson.jpg`（与图灵奖奖杯合影，已就绪）
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由可整句引用）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Knuth/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（Minsky / McCarthy）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
