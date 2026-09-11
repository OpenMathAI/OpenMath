# William Kahan（威廉·卡亨）立传提示词

> qid=Q92782 · 1933-06-05 –（在世）· 加拿大数学家、计算机科学家 · 20/21 世纪 · 1989 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1989/William Kahan/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Kahan 求和算法 / IEEE 754 舍入规则的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：William Morton Kahan（昵称 "Velvel"；中文惯称：威廉·卡亨）
- **生卒**：1933-06-05 生于 Toronto, Ontario（加拿大）→ **在世**，卒年留白
- **国籍**：加拿大（Canadian；生于多伦多的加拿大犹太家庭）
- **身份**：数学家、计算机科学家；UC Berkeley 数学与电机工程及计算机科学（EECS）荣休教授
- **教育轨迹**：University of Toronto 一站式三学位，均为数学——学士（1954）、硕士（1956）、博士（1958）；博士论文 *Gauss–Seidel Methods of Solving Large Systems of Linear Equations*（1958）
- **博士导师**：Byron Griffith（University of Toronto）
- **研究领域**：数学、计算机科学；数值分析、浮点运算
- **家庭**：页面仅载 "born to a Canadian Jewish family"，其余家庭细节**无载禁写**

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **IEEE 754 浮点标准总架构师**：IEEE 754-1985 二进制浮点运算标准的 primary architect；其与进制无关的后继 IEEE 854 亦出自其手；后又持续贡献于 IEEE 754 修订（现行标准）——**一人定义了全世界计算机的算术**。
2. **图灵奖（1989）**："for his fundamental contributions to numerical analysis"——整句引用为获奖理由红线，核心是**数值分析**而非仅 "IEEE 754"。
3. **"浮点之父"**：页面明载 "He has been called 'The Father of Floating Point', since he was instrumental in creating the original IEEE 754 specification"——是"被称作"，可用但注明来源。
4. **Kahan 求和算法**：最小化有限精度浮点数序列求和误差的重要算法——教科书级经典，可做公式框展示（补偿求和思想）。
5. **Paranoia 测试程序（1980s）**：检测大范围潜在浮点缺陷的基准程序——浮点正确性的"体检工具"。
6. **Table-maker's dilemma**：他创造（coined）的术语，指超越函数按预定精度正确舍入的未知代价——"术语命名者"视角可作独立亮点。
7. **数学家的一面：Davis–Kahan–Weinberger 膨胀定理**：Hilbert 空间算子膨胀理论的里程碑结果，已应用于多个领域——Kahan 根在纯数学（可强调其"数学 PhD 出身"叙事）。
8. **HP 计算器的幕后功臣**：HP-35 袖珍科学计算器超越函数精度欠佳时，HP 与 Kahan 深度合作大幅改进算法精度（Hewlett-Packard Journal 有载）；又实质性贡献 HP Voyager 系列算法设计并撰写部分中高级手册——工程落地的绝佳素材。
9. **浮点教育的直言斗士**："outspoken advocate of better education of the general computing population about floating-point issues"，经常公开抨击他认为损害浮点运算的计算机与编程语言设计决策（如《How Java's Floating-Point Hurts Everyone Everywhere》）——人物个性页。
10. **Toronto → Berkeley 的学术轨迹**：多伦多大学数学三学位（1954/1956/1958）→ UC Berkeley 荣休教授（数学 + EECS 双聘）。
11. **门生**：James Demmel（infobox 实载唯一博士生，Berkeley 数值计算领军者）。
12. **荣誉**：Turing Award 1989、IEEE Emanuel R. Piore Award 2000、ACM Fellow 1994、NAE 2005。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（浮点标准 — 蓝） | `#2E5A9E` | IEEE 754 / IEEE 854 |
| 分类色 2（数值分析 — 青绿） | `#1E8E8E` | Kahan 求和 / 数值分析 |
| 分类色 3（纯数学 — 琥珀） | `#D9A441` | Davis–Kahan–Weinberger 定理 |
| 分类色 4（工程与教育 — 玫瑰） | `#C0395B` | HP 计算器 / Paranoia / 浮点教育 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：极淡的数字与舍入符号散点（呼应"浮点 / 舍入误差"主题，如极淡 `1.00×10⁰` 小字），克制使用。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：明亮 / 昂扬（"浮点之父"为世界计算立规矩的成就感）
- **选定曲目**：Alex-Productions **Shine Like The Sun**（manifest 预分配，直接沿用）
- **落地文件**：`turing/presentations/William_Kahan/ShineLikeTheSun.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「浮点之父 · 加拿大」+ Kahan 1933– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1933– 在世生平纵览
4. **多伦多的犹太少年与数学三学位**（1933–1958）：BS 1954 / MS 1956 / PhD 1958、Gauss–Seidel 博士论文、导师 Griffith
5. **数值分析的根基**：从线性方程组到误差分析；数学家的一面（Davis–Kahan–Weinberger 定理）
6. **Berkeley 岁月**：数学 + EECS 双聘荣休教授
7. **IEEE 754：给全世界计算机定算术**（1985）：primary architect、radix-independent 的 IEEE 854、后续修订
8. **Kahan 求和算法**：补偿求和、误差最小化（公式框重点页）
9. **Paranoia：浮点的体检程序**（1980s）
10. **Table-maker's dilemma**：他命名的难题——超越函数正确舍入的未知代价
11. **HP 计算器幕后功臣**：HP-35 精度改进、Voyager 系列算法与手册
12. **直言的浮点斗士**：浮点教育倡导、公开批评损害浮点的设计决策
13. **荣誉与传承**：Turing 1989、Piore 2000、ACM Fellow 1994、NAE 2005、门生 James Demmel
14. **遗产**：IEEE 754 无处不在——从智能手机到超算都在跑他定的规则
15. **结尾**：在世大师、"The Father of Floating Point"的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由整句红线**："for his fundamental contributions to numerical analysis"——获奖理由是**数值分析**的整体贡献；IEEE 754 是其最著名工作但勿写成"因 IEEE 754 获奖"。
- **在世留白**：Kahan 生于 1933-06-05，**在世**，无卒日，勿编造享年。
- **"浮点之父"口径**：是 "He has been called 'The Father of Floating Point'"——**被称作**，写作"被业界誉为"而非自封；勿写成某机构官方授予。
- **IEEE 754 角色**：primary architect（总架构师）+ "instrumental in creating the original IEEE 754 specification"——勿写"独力完成"；IEEE 754 是委员会标准，Kahan 是主架构师。
- **国籍**：Canadian（加拿大），生于 Toronto——勿写成美国数学家；UC Berkeley 是任职不是国籍依据。
- **学位**：三个学位**全部是多伦多大学数学**（1954/1956/1958），勿写成伯克利或写错年份；PhD 论文是 Gauss–Seidel 迭代法解大型线性方程组（1958）。
- **Davis–Kahan–Weinberger**：是**膨胀理论（dilation theory）**的定理（Hilbert 空间算子），与浮点无关——勿与浮点工作混为一谈。
- **HP 合作**：正文只载 HP-35 超越函数精度改进（Hewlett-Packard Journal 有载）与 Voyager 系列算法贡献——勿添加未载的 HP 型号或轶事。
- **家庭**：页面仅载"加拿大犹太家庭"一句，其余家庭/婚姻/子女细节**无载禁写**。
- **引语**：页面**无直接引语节**——全文无直接引语，勿编造；其"直言"形象只可用叙述性转述（outspoken advocate / regularly denounces）。
- **荣誉**：Turing 1989、Piore 2000、ACM Fellow 1994、NAE 2005（inducted）——页面未载 Kyoto/NAS/其他奖章，勿编造。
- **Intel 8087**：页面 See also 提及 Intel 8087——可作背景一笔（8087 是 754 的硬件先声），但正文未展开 Kahan 与 Intel 的具体职务细节，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 卡亨（或 威廉·卡亨） | 待写入 |
| name_en | William Kahan | 待写入 |
| birth_date | 1933-06-05 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Canada | 待写入 |
| primary_occupation | mathematician and computer scientist | 待写入 |
| field_of_work | numerical analysis / floating-point arithmetic | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Byron Griffith（University of Toronto）
- **定理合作者**：Chandler Davis、H. F. Weinberger（Davis–Kahan–Weinberger 膨胀定理，1982 发表）
- **著名博士生**：James Demmel（infobox 实载唯一博士生）
- **机构合作**：Hewlett-Packard（HP-35 / Voyager 系列算法合作）——按"机构合作"而非人际关系处理

## 8. 奖项清单

- Turing Award（1989，"for his fundamental contributions to numerical analysis"）
- IEEE Emanuel R. Piore Award（2000）
- ACM Fellow（1994）
- 美国国家工程院院士（NAE，2005）

## 9. 机构清单

- 教育：University of Toronto（数学 BS 1954 / MS 1956 / PhD 1958）
- 任职：University of California, Berkeley（数学与 EECS 荣休教授，professor emeritus）

## 10. 终审清单

- [ ] 生卒 1933-06-05 / 在世留白，出生地 Toronto, Ontario
- [ ] 图灵奖 1989 理由整句（numerical analysis）表述准确，不写成"因 IEEE 754 获奖"
- [ ] "浮点之父"为"被称作"口径（The Father of Floating Point）
- [ ] IEEE 754 角色=primary architect，勿写"独力完成"
- [ ] 国籍「加拿大」，封面底部状态栏 `加拿大 | Toronto · UC Berkeley | Turing 1989`
- [ ] 三个学位均为多伦多大学数学（1954/1956/1958）
- [ ] Davis–Kahan–Weinberger 定理与浮点工作分开叙述
- [ ] 全文无直接引语，勿编造
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1989/William Kahan/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2008 年肖像（`images/William_Kahan_2008.jpg`，取 `500px-William_Kahan_2008.jpg` 大图版）
- [ ] **国籍**：封面顶部徽章明示加拿大
- [ ] **引语核对**：页面无引语节，tex 中不得出现任何"直接引语"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Sutherland / Corbató）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
