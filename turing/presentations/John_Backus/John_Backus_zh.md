# John Backus（约翰·巴科斯）立传提示词

> qid=Q92746 · 1924-12-03 – 2007-03-17 · 美国计算机科学家 · 20/21 世纪 · 1977 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1977/John Backus/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰（注意：页面挂 "needs more citations"（2025-09）横幅，BNF 一节无引用——事实表述保守，见 §5）。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（BNF 产生式 / Fortran 编译目标 / FP 组合子的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Warner Backus（中文惯称：约翰·华纳·巴科斯；注意消歧：页面明示勿与声学家 John Backus (acoustician)、牧师 John Chester Backus 混淆）
- **生卒**：1924-12-03 生于费城（Philadelphia, Pennsylvania）→ 2007-03-17 逝于俄勒冈州阿什兰（Ashland, Oregon）家中，享年 82；**死因页面未载（NYT 讣闻被引但正文未述），勿编造**
- **国籍**：美国（American）
- **身份**：计算机科学家（一生唯一任职机构：**IBM**）
- **家庭**：两段婚姻——Marjorie Jamison（1947–1966）、Barbara Una（1968 结婚，2004 去世）；子女 2 人
- **教育轨迹（一波三折，本篇最大戏剧性）**：
  - The Hill School（Pottstown, PA）——"apparently not a diligent student"
  - University of Virginia 化学专业——**不到一年因缺课被开除**
  - 二战入伍（U.S. Army，最高军衔下士，佐治亚州 Fort Stewart 高射炮台指挥）
  - 军方 aptitude 测试高分 → University of Pittsburgh 学工程
  - Haverford College 预医——医院实习时查出**颅骨骨瘤**，手术成功、头部植入金属板
  - Flower and Fifth Avenue Medical School 医学院——**觉得无趣，9 个月后退学**；随后**自设计金属板**做第二次置换手术；1946 年获光荣退役（honorable medical discharge）
  - 纽约当无线电技师后对数学产生兴趣 → **Columbia University 数学 BS（1949）、MS（1950）**
- **博士导师/师承**：页面无载——**禁写导师**
- **研究领域**：计算机科学（编程语言设计、语言规范、函数级编程）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1977 图灵奖**：ACM citation 整句——"for profound, influential, and lasting contributions to the design of practical high-level programming systems, notably through his work on FORTRAN, and for publication of formal procedures for the specification of programming languages"（**本篇核心红线引文**，获奖理由覆盖 FORTRAN + 形式规范两条线）
2. **IBM 与 SSEC（1950–1953）**：1950 年加入 IBM，前三年在 Selective Sequence Electronic Calculator 上工作；首个大项目是**编写计算月球位置**的程序。
3. **Speedcoding（1953）**：为 IBM 701 开发——**IBM 计算机上的第一个高级语言**（注意限定："created for an IBM computer"，勿写成"世界第一个高级语言"）。
4. **FORTRAN（1954 起）**：Backus **组建团队**为 IBM 704 定义并开发 Fortran；Fortran 是**第一个被广泛使用的高级编程语言**——"This widely used language made computers practical and accessible machines for scientists and others without requiring them to have deep knowledge of the machinery."（团队具体成员名单页面无载，**禁写**）
5. **ALGOL 与 BNF**：Backus 服务于开发 **ALGOL 58** 与极具影响的 **ALGOL 60** 的国际委员会（后者迅速成为发表算法的 de facto 世界标准）；他开发了 **Backus–Naur form（BNF）**，发表于 UNESCO 的 ALGOL 58 报告——能描述任何**上下文无关**程序设计语言的形式记法，对编译器发展至关重要；到 1970 年代随 yacc 等编译器生成器发展而成为标准。
6. **BNF 命名细节**：参考文献含 Knuth 1964 "backus normal form vs. Backus Naur form"（BNF 之名由来的经典文献）——但**正文未载 Naur 的具体贡献**，勿展开"为何有 Naur"的故事；命名本身含 Naur 即可。
7. **图灵奖演讲（1977）**："Can Programming Be Liberated from the von Neumann Style?"——提出 **FP** 函数级编程语言；"Sometimes viewed as Backus's apology for creating Fortran"（有时被视为巴科斯为创造 Fortran 的"道歉"）；此演讲更多点燃了**函数式编程**整体研究而非 FP 语言本身；其信息常被误读为与传统函数式语言相同。
8. **FP 的血统**：FP 受 **Kenneth E. Iverson 的 APL** 强烈启发（连非标准字符集都承袭）；FP 解释器曾随 **4.2BSD Unix** 发行，但实现很少、多用于教学。
9. **FL 与 J**：后半生开发 FL（Function Level，FP 后继，IBM 内部研究项目，项目结束即停，源码未公开）；FL 的许多思想现已在 **J 语言**（Iverson 的 APL 后继）中实现。
10. **荣誉线**：IBM Fellow（1963）、IEEE W. W. McDowell Award（1967，因 FORTRAN 的开发）、National Medal of Science（1975，早于图灵奖两年）、Turing Award（1977）、美国艺术与科学院 Fellow（1985）、Université Henri-Poincaré 荣誉博士（1989）、**Charles Stark Draper Prize（1993）**、Computer History Museum Fellow Award（1997，"for his development of FORTRAN, contributions to computer systems theory and software project management."）、**小行星 6830 Johnbackus 以其命名（2007-06-01）**。
11. **1991 退休**：退休后 2007-03-17 于 Ashland, Oregon 家中去世。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（Fortran 与 IBM — 蓝） | `#2E5A9E` | FORTRAN / Speedcoding / SSEC |
| 分类色 2（语言规范 — 青绿） | `#1E8E8E` | BNF / ALGOL 58 / ALGOL 60 |
| 分类色 3（函数级编程 — 琥珀） | `#D9A441` | FP / FL / J |
| 分类色 4（工程人生 — 玫瑰） | `#C0395B` | 从化学退学生到 IBM Fellow 的曲线 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和等宽字形纹理（稀疏浅色 :: 与 | 字符散点），呼应「BNF 产生式 / 打孔卡时代」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：悲怆 / 深沉（被开除的化学学生→颅骨手术→医学梦碎→为"让编程摆脱冯·诺依曼风格"而战的深沉叙事）
- **选定曲目**：Alex-Productions **Tragedy**（manifest 预分配，直接沿用），匹配"在挫败中再造计算机语言史"的叙事。
- **落地文件**：`turing/presentations/John_Backus/Tragedy.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「Fortran 与 BNF 之父 · 美国」+ 巴科斯 1924–2007 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域；师承格写"无载"或略）
3. **时间线**（`\timelineslide`）：1924–2007 生平纵览
4. **费城到特拉华：被开除的化学学生**（1924–1943）
5. **二战与颅骨肿瘤：医学梦碎**（1943–1946）：Fort Stewart 下士、两次手术与自设计金属板
6. **哥伦比亚数学与 IBM 入职**（1949–1950）：无线电技师→数学、SSEC 与月球位置
7. **Speedcoding**（1953）：IBM 计算机上的第一个高级语言
8. **FORTRAN**（1954–1957）：组建团队、第一个广泛使用的高级语言
9. **ALGOL 与 BNF**（1958–1960）：UNESCO 报告、上下文无关记法、编译器时代
10. **图灵奖演讲**（1977）："Can Programming Be Liberated from the von Neumann Style?"
11. **FP 与 FL**：函数级编程、APL 血统、4.2BSD、J 语言归宿
12. **荣誉与传承**：IBM Fellow 1963 / McDowell 1967 / NMS 1975 / Draper 1993 / 小行星 6830
13. **遗产**：高级语言、语言规范、函数式编程三线汇流
14. **结尾**：82 岁、"让科学家人人可编程"的历史地位
    （如需凑满 15 页：将 13 拆为"三线遗产"与"对后世语言的影响"两页）

## 5. 史实陷阱与敏感点（终审必须检查）

- **Speedcoding 限定**：是"**IBM 计算机上**的第一个高级语言"（first high-level language created for an IBM computer）——勿写成"世界第一个高级语言"；"第一个被广泛使用的高级语言"这一表述属于 **FORTRAN**。
- **FORTRAN 团队**：页面仅载"Backus assembled a team to define and develop Fortran"（1954）——**成员名单无载，禁写**具体人名。
- **BNF 命名**：正文只载 Backus 开发了 BNF、发表于 UNESCO 的 ALGOL 58 报告——**Naur 的贡献细节页面未载，勿展开**；Knuth 1964 文献仅出现在参考文献，勿当正文事实引用。
- **图灵奖理由**：citation 覆盖**两条线**——FORTRAN（practical high-level programming systems）+ 形式规范（formal procedures for the specification of programming languages）；两条线都要在正文呼应，勿只写 FORTRAN。
- **图灵奖演讲定位**："Sometimes viewed as Backus's apology for creating Fortran"是 Wikipedia 的评论性表述——引用时注明"有时被视为"，保留"FP 常被误读为传统函数式编程"的实载细节。
- **FL 的结局**：IBM 内部项目、开发停止、源码未公开、思想后继于 J 语言——按实载写，勿写"FL 失败/被放弃"之类评价。
- **个人健康细节**：颅骨骨瘤、金属板、自设计置换板——页面实载可写（本篇最有戏剧性的段落），但**不渲染**、不延伸病情评价。
- **婚姻**：两段婚姻（1947–1966、1968 起）与子女 2 人按 infobox 实载一笔带过。
- **死因**：2007-03-17 卒于 Ashland, Oregon 家中，享年 82——**页面未载死因，勿编造**。
- **小行星**：6830 Johnbackus，2007-06-01 命名（其去世后）——可作为结尾页彩蛋。
- **页面质量提示**：本页挂 "needs more citations"（2025-09）横幅、BNF 一节无引用——Review-1 对 BNF 相关表述逐句核对本页原文。
- **可引语**：限 citation 整句、CHM Fellow citation、"This widely used language made computers practical and accessible machines for scientists and others..."（页面原文）；Backus 个人直接引语页面未载，**勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 巴科斯（或 约翰·巴科斯） | 待写入 |
| name_en | John Backus | 待写入 |
| birth_date | 1924-12-03 | 待写入 |
| death_date | 2007-03-17 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | programming languages / FORTRAN / BNF / function-level programming | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **导师**：页面无载——**禁写**
- **团队成员/合作者**：FORTRAN 团队成员、ALGOL 委员会同仁——**页面均未载姓名，禁写具体人**
- **精神先驱（非直接合作）**：Kenneth E. Iverson（FP 强烈受 APL 启发；FL 思想后继于 J 语言）——关系类型按"灵感来源/受其影响"处理
- **门生**：页面无载——**禁写**
- **家庭**：配偶 Marjorie Jamison（1947–1966）、Barbara Una（1968–2004 卒）；子女 2 人（姓名无载）

## 8. 奖项清单

- IBM Fellow（1963）
- IEEE W. W. McDowell Award（1967，因 FORTRAN 的开发）
- National Medal of Science（1975）
- Turing Award（1977）
- Fellow of the American Academy of Arts and Sciences（1985）
- Doctor honoris causa, Université Henri-Poincaré（1989）
- Charles Stark Draper Prize（1993）
- Computer History Museum Fellow Award（1997）
- 小行星 6830 Johnbackus 命名（2007-06-01）

## 9. 机构清单

- 教育：The Hill School、University of Virginia（化学，被开除）、University of Pittsburgh（工程，军方派遣）、Haverford College（预医）、Flower and Fifth Avenue Medical School（9 个月退学）、Columbia University（数学 BS 1949 / MS 1950）
- 任职：IBM（1950–1991，唯一任职机构；SSEC → Speedcoding → FORTRAN → ALGOL/BNF → FP/FL）

## 10. 终审清单

- [ ] 生卒 1924-12-03 / 2007-03-17，享年 82，出生地 Philadelphia，去世地 Ashland, Oregon
- [ ] 图灵奖 citation 整句引用无误（FORTRAN + 形式规范两条线在正文均有呼应）
- [ ] Speedcoding "IBM 计算机上第一个高级语言" 限定词准确
- [ ] FORTRAN "第一个被广泛使用的高级语言" 表述准确、团队成员不写具体人名
- [ ] BNF 发表于 UNESCO ALGOL 58 报告、上下文无关表述准确；Naur 细节不展开
- [ ] 图灵演讲 "apology" 评论注明"有时被视为"；FP 与函数式编程的误读保留
- [ ] 颅骨手术/自设计金属板按实载、不渲染
- [ ] 死因留白（页面未载，勿编造）
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | IBM | Turing 1977 · Draper 1993`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1977/John Backus/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实（重点：BNF 一节、Speedcoding 限定词）
- [ ] **头像**：使用 `images/John_Backus_2.jpg`（1989 年照，页面顶部图注 "Backus in 1989"）；`Fortran_logo.svg.png` 可作为 FORTRAN 页插图（勿作头像）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（限 §5 所列）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐（师承格写"页面无载"）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（1970s 前后各篇）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
