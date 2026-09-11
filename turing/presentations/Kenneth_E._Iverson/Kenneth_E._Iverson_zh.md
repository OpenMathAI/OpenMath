# Kenneth E. Iverson（肯尼斯·艾弗森）立传提示词

> qid=Q92629 · 1920-12-17 – 2004-10-19 · 加拿大计算机科学家 · 20 世纪 · 1979 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1979/Kenneth E. Iverson/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（fork 定义 `(f g h) y ←→ (f y) g (h y)` / APL 记号的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Kenneth Eugene Iverson（中文惯称：肯尼斯·艾弗森，通称 Ken Iverson）
- **生卒**：1920-12-17 生于加拿大艾伯塔省 Camrose 附近 → 2004-10-19 逝于多伦多（Toronto），享年 83（2004-10-16 在电脑前开发新 J lab 时中风，三日后去世）
- **国籍**：加拿大（Canadian）
- **身份**：计算机科学家、数学家（APL 之父）
- **家庭**：父母为农民，从北达科他州迁至艾伯塔；祖辈来自挪威特隆赫姆（Trondheim）；儿子 Eric Iverson 后创办 Iverson Software Inc. 并管理 IPSA 的 APL 组
- **教育轨迹**：
  - 1926-04-01 入一间**单室学校**（one-room school），三个月连跳两级
  - 九年级后**辍学**——大萧条时期须回农场劳作
  - 17 岁辍学期间修 De Forest Training（芝加哥）无线电函授课程，靠教科书自学微积分
  - 二战服役期间以函授课程修完高中文凭课程
  - 1950 年 Queen's University（Kingston）数学与物理学士，**应届头名**（得益于退伍军人资助）
  - Harvard University：1951 数学硕士 → 转入工程与应用物理系 → **1954 应用数学博士**；论文 *Machine Solutions of Linear Differential Equations – Applications to a Dynamic Economic Model*
- **博士导师**：Howard Aiken（Harvard Mark I 之父）与 Wassily Leontief（投入产出模型、后获诺贝尔经济学奖）**双导师**
- **研究领域**：编程语言、数学记号、数组语言、教育计算

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **农场少年的逆袭**：单室学校跳级 → 九年级辍学务农 → 自学微积分 → 二战空军 → Queen's 头名毕业——"受教育之路非直线"的叙事主线。
2. **Harvard 双导师博士（1954）**：为 Leontief 的投入产出模型在 Harvard Mark IV 上写矩阵求值程序（Leontief 因此工作后来获诺奖）；Aiken 门下"学徒制"学术训练。
3. **世界首个"自动数据处理"研究生课程**（Harvard 1955–1960）：Aiken 亲自点将："这些机器对商业将极为重要"（Brooks 转述）——Iverson 因此开发教学记号。
4. **记号的诞生**：因"惊恐地"发现传统数学记号不敷使用，融合矩阵代数、张量分析、Heaviside 算子思想，发展出 Iverson 记号；1957 年 McKinsey & Company 六个月业界试用；首篇用该记号的论文 *The Description of Finite Sequential Processes*。
5. **Harvard 未获终身教职**："（我）除了那本小书什么都没发表"——1960 年转投 IBM（薪水翻倍）。
6. **IBM 二十年与 Falkoff**：与 Adin Falkoff 合作二十年；合著 *A Programming Language*（APL 由此得名）与（与 Fred Brooks）*Automatic Data Processing*；用 Iverson 记号形式化描述 IBM System/360——1964 年 IBM Systems Journal 双刊号"灰皮书"。
7. **APL\360 的实现（1965–1966）**：Larry Breed 与 Phil Abrams 造出 FORTRAN 版 IVSYS（7090），1966 年初时分交互模式；Breed、Lathwell、Moore 的 System/360 实现获 **1973 Grace Murray Hopper Award**（**给三人的，不是 Iverson**）；"Iverson notation" 更名 "APL" 由 Falkoff 拍板。
8. **APL 教育运动**：Fox Lane High School（1964）、NASA Goddard、多所中小学——有学校学生为抢 APL 机时深夜潜入机房。
9. **1970 IBM Fellow；1979 图灵奖**：citation 见 §5 整句红线；图灵讲座 *Notation as a Tool of Thought*（1980 CACM）——"记号是思维的工具"。
10. **IPSA 与字典 APL（1980–1987）**：转投 APL 分时公司 I. P. Sharp Associates；*A Dictionary of APL*（1987-09）——语法由 9×6 表驱动；Arthur Whitney 一页 APL 模型（1981）并发明 rank 算子。
11. **fork（1988）与 J 语言**：为在 APL 中写 `f+g`（如微积分般）求索十年，1988 年赴 APL88 悉尼长途航班上与 McDonnell 敲定 fork；Roger Hui 1989-08-27 写下 J 实现第一行代码；儿子 Eric 创办 Iverson Software Inc.（1990-02，后更名 Jsoftware）——J 用 ASCII 字符与自然语言术语（noun/verb/adverb）。
12. **荣誉与纪念**：IBM Fellow 1970、Harry H. Goode Memorial Award 1975、NAE 1979、Turing 1979、IEEE Computer Pioneer Award（宪章受奖者）1982、York University 荣誉博士 1998；2015 年新蛾种 *Agdistis iversoni* 以其命名；数学中的 **Iverson bracket** 亦以其名传世。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（APL 与数组语言 — 蓝） | `#2E5A9E` | APL\360 / System/360 灰皮书 |
| 分类色 2（数学记号 — 青绿） | `#1E8E8E` | Notation as a Tool of Thought / Iverson bracket |
| 分类色 3（交互系统实现 — 琥珀） | `#D9A441` | IVSYS / 分时交互 |
| 分类色 4（教育与 J — 玫瑰） | `#C0395B` | APL 教育运动 / fork 与 J 语言 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「记号即思维工具」的极简数组语言美学。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：绵长 / 坚守（二十年打磨一门记号、从农场到 IBM）
- **选定曲目**：Alex-Productions **Eternals**（manifest 预分配，直接沿用），匹配"以一生守一套记号"的长线叙事。
- **落地文件**：`turing/presentations/Kenneth_E._Iverson/Eternals.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「APL 之父 · 加拿大」+ 艾弗森 1920–2004 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1920–2004 生平纵览
4. **艾伯塔农场少年**（1920–1939）：单室学校、九年级辍学、自学微积分
5. **战争与 Queen's**（1939–1950）：加拿大陆军→皇家空军、函授修完高中、头名毕业
6. **Harvard：Aiken 与 Leontief 双导师**（1950–1954）：Mark IV 上的经济模型矩阵程序、应用数学博士
7. **世界首个自动数据处理课程**（1955–1960）：Aiken 点将、与 Brooks 合著、记号初步成形
8. **记号是思维的工具**：Iverson 记号的思想渊源（矩阵代数 / 张量 / Heaviside 算子）与 McKinsey 试用
9. **IBM 与 Falkoff 二十年**（1960–1980）：A Programming Language、System/360 灰皮书
10. **APL\360：从记号到语言**：IVSYS 1965、1966 交互模式、Breed/Lathwell/Moore 与 Hopper Award、命名 APL
11. **APL 教育运动**：中小学与 NASA Goddard、Philadelphia Scientific Center、IBM Fellow
12. **图灵奖 1979**：整句引用 ACM citation + Notation as a Tool of Thought
13. **IPSA 与字典 APL**（1980–1987）：9×6 语法表、Whitney 一页模型与 rank 算子
14. **fork 与 J**（1988–2004）：APL88 航班、Roger Hui 1989-08-27 第一行代码、Jsoftware、ASCII 与自然语言术语
15. **结尾**：83 岁、Iverson bracket 与 Agdistis iversoni 的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由（核心红线）**：1979 整句 citation："for his pioneering effort in programming languages and mathematical notation resulting in what the computing field now knows as APL; for his contributions to the implementation of interactive systems, to educational uses of APL, and to programming language theory and practice"——勿改写删减。
- **Hopper Award 归属**：1973 Grace Murray Hopper Award 给的是 **Breed、Lathwell、Moore 三人**（APL\360 的设计与实现）——**不是 Iverson 本人**，勿张冠李戴。
- **APL 更名**："Iverson notation" 改名 "APL" 是 **Falkoff** 所为——勿写 Iverson 自己改名。
- **双导师**：博士导师为 Aiken 与 Leontief **两人**——勿只写其一；Leontief 诺奖是"后来获得"，且因投入产出模型，勿写"因 Iverson 的工作获奖"。
- **辍学与学位**：九年级辍学（大萧条务农）→ 二战函授补高中 → 1950 Queen's 学士（数学+物理，头名）→ 1951 Harvard 硕士（数学系）→ 1954 博士（**应用数学**，工程与应用物理系）——学位学科勿混。
- **Harvard 未获终身教职**：原因是"[自己]除了那本小书什么都没发表"（Iverson 自述，页面引语）——可引用但注明自述语境，勿渲染成学术阴谋。
- **记号→APL 时间线**：记号诞生于 Harvard 教学时期（1955–1960），*A Programming Language* 一书在 IBM 出版后才使 "APL" 得名；APL\360 服务 IBM 内部始于 1966-11 之前数周、对外 1968——年份勿混。
- **fork 的求索链**：scalar operators 1978 → til 1982 → catenate/reshape 1984 → union/intersection 1987 → yoke 1988 → forks 1988——勿把 fork 直接写成"1988 凭空发明"；灵感浮现于 APL88 悉尼航班。
- **J 的归属**：Roger Hui 1989-08-27 写下实现第一行代码；**Arthur Whitney** 的一页解释器片段是契机；Eric Iverson（儿子）创办公司——三人贡献勿混。
- **Iverson bracket**：数学中的 Iverson bracket 以其命名（See also 实载）——可提，但勿展开为正文贡献（页面无详述）。
- **生卒与死因**：1920-12-17 ~ 2004-10-19，享年 83；死因 = 中风（2004-10-16 开发 J lab 时，三日后去世）——按页面实载可写。
- **奖项**：IBM Fellow 1970、Goode Award 1975、NAE 1979、Turing 1979、Computer Pioneer Award（charter recipient）1982、York 荣誉博士 1998——页面无 Kyoto/其他，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 肯尼斯·艾弗森（或 艾弗森） | 待写入 |
| name_en | Kenneth E. Iverson | 待写入 |
| birth_date | 1920-12-17 | 待写入 |
| death_date | 2004-10-19 | 待写入 |
| nationality | Canada | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | programming languages / mathematical notation / array languages (APL, J) | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Howard Aiken（Harvard Mark I 之父）、Wassily Leontief（投入产出模型，诺奖经济学家）——双导师
- **核心合作者**：Adin Falkoff（二十年搭档、APL 命名）、Fred Brooks（Automatic Data Processing 合著、Harvard 同事）、Roger Hui（J 实现）、Arthur Whitney（一页 APL 模型、rank 算子）、Eugene McDonnell（fork 细节）
- **APL\360 实现者**：Larry Breed、Phil Abrams、Dick Lathwell、Roger Moore（Hopper Award 三人为 Breed/Lathwell/Moore）
- **家庭**：Eric Iverson（儿子，Iverson Software/Jsoftware 创办人）

## 8. 奖项清单

- IBM Fellow（1970）
- Harry H. Goode Memorial Award（IEEE Computer Society，1975）
- Member, National Academy of Engineering（USA，1979）
- Turing Award（ACM，1979）
- Computer Pioneer Award（IEEE Computer Society，宪章受奖者 charter recipient，1982）
- Honorary doctorate, York University（1998）

## 9. 机构清单

- 教育：Queen's University（数学与物理 B.A. 1950）、Harvard University（MA 1951、应用数学 PhD 1954）
- 任职：Harvard University（助理教授，1955–1960，未获终身教职）→ IBM Research（1960–1980，1970 IBM Fellow）→ I. P. Sharp Associates（1980–1987）→ Jsoftware Inc.（1990–2004，荣休后）

## 10. 终审清单

- [ ] 生卒 1920-12-17 / 2004-10-19，享年 83，出生地 Camrose（Alberta），去世地 Toronto，死因中风
- [ ] "九年级辍学 → 自学微积分 → 战时函授 → 头名毕业"求学线表述准确
- [ ] 双导师 Aiken + Leontief 表述准确，Leontief 诺奖语境正确
- [ ] Harvard 未获终身教职的自述引语归属正确
- [ ] Hopper Award 归属 Breed/Lathwell/Moore 三人，非 Iverson
- [ ] APL 命名归 Falkoff；APL\360 年份（IVSYS 1965 / 交互 1966 / 对外 1968）准确
- [ ] 图灵奖 citation 整句引用无误；图灵讲座 *Notation as a Tool of Thought* 1980
- [ ] fork 求索链与 APL88 航班细节准确；J 第一行代码 1989-08-27 归 Roger Hui
- [ ] 肖像文件核对：`images/500px-KEI_Hui.jpg`（1989 与 Whitney 或 1996 与 Hui 合照；若需单人头像用 `KEI_with_ATW_NY_Aug_1989_cropped_-_Ken_Iverson.png` 裁剪版）
- [ ] 国籍用「加拿大」，封面底部状态栏 `加拿大 | IBM · Harvard · IPSA · Jsoftware | Turing 1979`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1979/Kenneth E. Iverson/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/` 目录肖像（KEI_Hui.jpg 500px 或 1989 裁剪单人版，已就绪），图注写明合影裁剪与否
- [ ] **国籍**：封面顶部徽章明示加拿大
- [ ] **引语核对**：引语（citation、Aiken 学徒制、Brooks 点将、J 缘起自述）必须在 Wikipedia 原文找到；Brooks 段落是 Brooks 的话、Aiken 学徒制段是 Cohen 书中引 Iverson 回忆——出处勿错挂
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一；APL 特殊符号（⍤ 等）缺字时用文字描述替代
- [ ] 与同期图灵奖得主（Floyd / Hoare）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
