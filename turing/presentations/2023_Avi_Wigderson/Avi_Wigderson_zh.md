# Avi Wigderson（阿维·威格德森）立传提示词

> qid=Q92957 · 1956-09-09 –（在世留白）· 以色列计算机科学家、数学家 · 20/21 世纪 · 2023 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2023/Avi Wigderson/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。（真实肖像：`images/Avi_Wigderson_London_2012_Cropped.jpg`）
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 以色列`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名（含希伯来文 אבי ויגדרזון）、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（去随机化 / Zig-zag 图乘积 / 零知识证明的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Avi Wigderson（希伯来文：אבי ויגדרזון；中文惯称：阿维·威格德森）
- **生卒**：1956-09-09 生于 Haifa（海法，以色列）→ **在世，卒年留白**
- **国籍**：以色列（Israeli）
- **身份**：计算机科学家、数学家；Institute for Advanced Study（IAS，普林斯顿高等研究院）数学学院 Herbert H. Maass Professor
- **家庭**：父母是大屠杀（Holocaust）幸存者（按实载一笔带过，不渲染）；在 Technion 结识妻子 Edna；儿子 Yuval Wigderson 为奥地利科学技术研究所（ISTA）数学教授
- **教育轨迹**：
  - 中学：海法 Hebrew Reali School
  - 1977–1980 年 Technion（Israel Institute of Technology）本科（BS），1980 年毕业
  - Princeton University 硕士+博士（MS, PhD）；1983 年获计算机科学博士，论文 *Studies in Computational Complexity*
- **博士导师**：Richard Lipton
- **研究领域**：计算复杂性理论、并行算法、图论、密码学、分布式计算（页面评述：显著扩展了计算复杂性领域）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2023 图灵奖**（2024 年 4 月宣布）：ACM 获奖理由**整句可引**："for reshaping our understanding of the role of randomness in computation, and for decades of intellectual leadership in theoretical computer science."——本篇主线：随机性在计算中的作用。
2. **双最高奖**：2021 年 **Abel Prize**（与 László Lovász 共享，理由整句可引："for their foundational contributions to theoretical computer science and discrete mathematics, and their leading role in shaping them into central fields of modern mathematics."）+ 2023 年图灵奖——两奖理由勿互串，本篇以图灵奖为主线、Abel 一页并立。
3. **海法少年与大屠杀幸存者之子**（1956–）：Hebrew Reali School、Technion 1977 入学 1980 毕业、在 Technion 遇见妻子 Edna。
4. **Princeton 复杂性博士**（1980–1983）：Lipton 门下，*Studies in Computational Complexity*；此后短期职位：UC Berkeley、IBM Almaden 研究中心（San Jose）、MSRI（Berkeley）。
5. **希伯来大学岁月**（1986–1999）：1986 入职、1987 获终身教职、1991 正教授。
6. **全职 IAS**（1999–）：1999 年起兼任 IAS 职位，2003 年放弃希伯来大学职位、全职定居 IAS——IAS 数学学院 Herbert H. Maass Professor。
7. **随机性与去随机化**：与 Noam Nisan、Russell Impagliazzo 合作发现——对于靠抛硬币求解的算法，只要满足预设条件，存在几乎一样快的不用抛硬币的算法（**三人合作，勿独归 Wigderson**；细节机制按页面转述口径，勿展开教科书式展开）。
8. **Zig-zag 乘积**：与 Omer Reingold、Salil Vadhan 共同提出——连接复杂性理论、图论与群论；例如可帮助理解"如何走出迷宫"；用于构造 expander graphs（2009 Gödel Prize 获奖工作）。
9. **零知识证明**：与 Silvio Micali、Oded Goldreich 合作证明零知识证明可用于"在保密的前提下公开地证明秘密数据上的结果"——复杂性理论今日在密码学中的应用之一。
10. **荣誉满贯**：Nevanlinna Prize（1994，因计算复杂性工作）、Gödel Prize（2009，zig-zag product 与 expander graphs）、American Academy of Arts and Sciences 院士（2011）、ACM Fellow（2018）、Knuth Prize（2019，理由涉及随机计算/密码学/电路复杂性/证明复杂性/并行计算/图性质等"foundations of computer science"）、Carnegie Corporation Great Immigrant Award（2025）。
11. **数学-计算机桥梁角色**：页面评述 Wigderson "credited with significantly expanding the field of computational complexity"——Abel 委员会口径"塑造理论计算机科学与离散数学成为现代数学中心领域"的 leading role。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（随机性与计算 — 蓝） | `#2E5A9E` | 去随机化 / 图灵奖主线 |
| 分类色 2（图与扩张网络 — 青绿） | `#1E8E8E` | Zig-zag product / expander graphs |
| 分类色 3（密码学 — 琥珀） | `#D9A441` | 零知识证明 |
| 分类色 4（IAS 与数学桥梁 — 玫瑰） | `#C0395B` | Abel Prize / IAS 岁月 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：硬币与迷宫（稀疏散落的抛硬币圆点 + 一条蜿蜒浅线），呼应「随机性如何被确定性驯服」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：希望 / 长路（复杂性世界的漫长智力远征终获双奖认可）
- **选定曲目**：Alex-Productions **Last Hope**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Avi_Wigderson/LastHope.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「随机性与计算 · 以色列」+ Wigderson 1956– + 右上真实肖像（London 2012 照）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右 2×2 信息网格（生卒 / 本名含希伯来文 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 家庭 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1956–至今 生平纵览
4. **海法少年**（1956–1980）：大屠杀幸存者之子一笔带过、Reali School、Technion、遇 Edna
5. **Princeton 复杂性博士**（1980–1983）：Lipton 门下、*Studies in Computational Complexity*
6. **漂泊与扎根**（1983–1999）：Berkeley/Almaden/MSRI 短期 → 希伯来大学 1986/1987/1991
7. **全职 IAS**（1999–2003）：Maass 讲席、普林斯顿高等研究院
8. **公式框：抛硬币的算法可以去掉硬币吗**：Nisan–Impagliazzo–Wigderson 去随机化
9. **Zig-zag 乘积**（与 Reingold、Vadhan）：图×群×复杂性、expander graphs、走出迷宫
10. **零知识证明**（与 Micali、Goldreich）：秘密数据的公开证明
11. **复杂性理论的扩展者**：parallel algorithms / cryptography / distributed computing 的版图
12. **荣誉墙（上）**：Nevanlinna 1994、Gödel 2009、AAAS 2011、ACM Fellow 2018、Knuth 2019
13. **荣誉墙（下）：Abel Prize 2021**：与 Lovász 共享、理由整句引用
14. **2023 图灵奖**：ACM 整句 citation + 随机性主线回望
15. **结尾**：理论计算机科学成为现代数学中心学科的塑造者

## 5. 史实陷阱与敏感点（终审必须检查）

- **两奖理由勿互串**：Abel 2021 理由（与 Lovász 共享）与 Turing 2023 理由（随机性）是两句不同 citation，各自整句引用、不得互换；intro 短句 "for his contributions to the understanding of randomness in the theory of computation" 与 ACM 整句版本并存时，**以 ACM 整句 citation 为准**。
- **Abel 是共享**：2021 Abel Prize 明载 "Shared ... with László Lovász"——勿写独得；Lovász 名字拼写勿错。
- **去随机化三人组**：Nisan、Impagliazzo 与 Wigderson 三人合作——勿独归 Wigderson；"presets are met" 口径按页面转述，勿编造 PRG/_hardness-vs-randomness_ 术语展开（页面未载）。
- **Zig-zag 两人勿漏**：Reingold、Vadhan 与 Wigderson 三人；零知识：Micali、Goldreich 与 Wigderson 三人——两组名单各自齐全。
- **Holocaust 背景**：仅"出生于大屠杀幸存者家庭"一句带过，不渲染不展开。
- **Technion 时间**：1977 年入学、1980 年毕业——勿写间隔年或其他无载细节；与 Edna 相识于 Technion 有载可写一句。
- **在世**：无卒年，写 `1956–`，留白。
- **Nevanlinna Prize**：1994 年"因计算复杂性工作"获——勿写成"图灵奖前奏"等延伸。
- **Knuth Prize 理由**：页面载 ACM SIGACT 授奖口径（随机计算、密码学、电路复杂性、证明复杂性、并行计算、基本图性质）——引述时勿增删领域名。
- **引语**：仅 ACM 图灵奖 citation 与 Abel citation 可整句引用；其余全文无直接引语，勿编造。
- **国籍**：以色列（生于海法）——封面写「以色列」，勿写"美国科学家"（IAS 在美国但国籍为以色列）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 威格德森（或 阿维·威格德森） | 待写入 |
| name_en | Avi Wigderson | 待写入 |
| birth_date | 1956-09-09 | 待写入 |
| death_date | 空（在世留白） | 待写入 |
| nationality | Israel | 待写入 |
| primary_occupation | computer scientist / mathematician | 待写入 |
| field_of_work | computational complexity / randomness in computation / cryptography / graph theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Richard Lipton（Princeton）
- **合作者**：Noam Nisan、Russell Impagliazzo（去随机化）、Omer Reingold、Salil Vadhan（Zig-zag product）、Silvio Micali、Oded Goldreich（零知识证明）、László Lovász（2021 Abel 共享得主）
- **博士学生**：Dorit Aharonov、Ran Raz、Eli Ben-Sasson
- **家庭成员**：妻 Edna（Technion 相识）、子 Yuval Wigderson（ISTA 数学教授）——家庭成员不入关系库

## 8. 奖项清单

- Turing Award（2023，2024 年 4 月宣布；ACM citation 整句见亮点 1）
- Nevanlinna Prize（1994，计算复杂性）
- Gödel Prize（2009，zig-zag product 与 expander graphs）
- American Academy of Arts and Sciences 院士（2011）
- ACM Fellow（2018，"contributions to theoretical computer science and mathematics"）
- Knuth Prize（2019，授奖口径见 §5）
- Abel Prize（2021，与 László Lovász 共享；citation 整句见亮点 2）
- Carnegie Corporation of New York Great Immigrant Award（2025）

## 9. 机构清单

- 教育：Hebrew Reali School（海法，中学）、Technion（BS，1977 入学 / 1980 毕业）、Princeton University（MS/PhD 1983）
- 任职：UC Berkeley、IBM Almaden Research Center、MSRI（短期职位）；Hebrew University（1986 入职 / 1987 终身 / 1991 正教授 / 2003 离任）；Institute for Advanced Study（1999 起兼职、2003 起全职；Herbert H. Maass Professor）

## 10. 终审清单

- [ ] 生卒 1956-09-09 / 在世留白，出生地 Haifa, Israel
- [ ] 国籍用「以色列」，封面底部状态栏 `以色列 | IAS · Hebrew University · Princeton | Turing 2023`
- [ ] 图灵奖 ACM citation 与 Abel citation 两句各自整句一致、未互串
- [ ] Abel 2021 写明与 Lovász 共享
- [ ] 去随机化（Nisan/Impagliazzo）、Zig-zag（Reingold/Vadhan）、零知识（Micali/Goldreich）三组名单齐全
- [ ] Holocaust 背景仅一句带过
- [ ] Technion 1977–1980 与 Princeton 1983 博士时间线准确
- [ ] Knuth Prize 授奖口径未增删
- [ ] 肖像使用 `images/Avi_Wigderson_London_2012_Cropped.jpg`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2023/Avi Wigderson/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2012 伦敦肖像（`images/Avi_Wigderson_London_2012_Cropped.jpg`）
- [ ] **国籍**：封面顶部徽章明示以色列
- [ ] **引语核对**：仅两句 citation 可在 Wikipedia 原文找到，其余不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky / John_McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Aho/Ullman/Dongarra/Metcalfe）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
