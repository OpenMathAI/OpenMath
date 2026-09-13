# Robert W. Floyd（罗伯特·弗洛伊德）立传提示词

> qid=Q92641 · 1936-06-08 – 2001-09-25 · 美国计算机科学家 · 20 世纪 · 1978 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1978/Robert W. Floyd/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Floyd–Warshall 递推 / 程序验证断言的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Robert Willoughby Floyd（中文惯称：罗伯特·弗洛伊德；中间名 Willoughby 曾依法改为 "W"，Knuth 2003 记载）
- **生卒**：1936-06-08 生于纽约市（New York City，美国）→ 2001-09-25 逝于斯坦福（Stanford，加利福尼亚州），享年 65（晚年被 Pick 病困扰，页面未详述死因细节，勿编造）
- **国籍**：美国（American）
- **身份**：计算机科学家（程序设计方法学先驱）
- **家庭**：结过两次婚并离异——Jana M. Mason、后为计算机科学家 Christiane Floyd（née Riedl）；育有 4 个孩子
- **教育轨迹**：
  - 14 岁完成高中学业（早慧）
  - University of Chicago **文学士**（B.A.，liberal arts）1953 年——时年仅 17 岁
  - University of Chicago 第二个学士：**物理学**（B.S.）1958 年
  - **无博士学位**——全凭工作实绩晋升教授
  - 芝加哥大学室友：Carl Sagan（天文学家）
- **师承**：无正规博士导师（页面未载硕士/博士履历，禁写任何导师）
- **研究领域**：算法分析、解析理论（parsing）、程序设计语言语义、程序验证与综合、图算法
- **职业轨迹**：1950s 入 Armour Research Foundation（今 IIT Research Institute，属 Illinois Institute of Technology）；1960s 初成为计算机操作员并开始大量发表论文；27 岁前获聘 Carnegie Mellon University 副教授；六年后升任 Stanford University 正教授

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **14 岁中学毕业、17 岁大学学士**：1936 年生于纽约，1953 年芝加哥大学文科学士（17 岁），1958 年再获物理学士——两段跨学科履历。
2. **无博士的正教授**：从 Armour Research Foundation 的计算机操作员起步，27 岁前任 CMU 副教授，约 33 岁任 Stanford 正教授——**全程无 PhD**，强调"以实绩立足"。
3. **解析理论奠基**：算符优先文法（operator-precedence grammars）先驱，编译器/解析论文大量发表于 1960s 早期。
4. **程序语义与验证开创（1967）**：论文 *Assigning Meanings to Programs* 用**逻辑断言**做程序验证，开创程序语言语义领域，是后来 **Hoare 逻辑**的先声——注意口径：是"贡献于后来成为 Hoare 逻辑的工作"，勿写"Hoare 逻辑由 Floyd 创立"。
5. **Floyd–Warshall 算法**：高效求图中**所有点对最短路径**，与 Stephen Warshall **各自独立**提出——"独立"两字必须保留。
6. **Floyd 判圈算法（cycle-finding）**：检测序列中的环，归功于 Floyd。
7. **Floyd–Steinberg 抖动（dithering）**：单篇论文引入图像渲染的**误差扩散**重要概念；注意 Floyd 本人**区分 dithering 与 diffusion** 两个概念。
8. **Floyd 三角**：以他命名的数字三角形结构。
9. **与 Knuth 的深度协作**：是 Knuth《The Art of Computer Programming》的**主要审稿人**，也是该书中**被引用最多的人**；与 Knuth 合著 *The Bose-Nelson sorting problem*（1970）；与 Beigel 合著教材 *The Language of Machines*（1994）。
10. **IFIP WG 2.1 成员**：参与制定、维护 ALGOL 60 与 ALGOL 68 的国际工作组。
11. **门生传承**：指导 7 名博士毕业，infobox 载 Jay Earley、Zohar Manna、David Plaisted、Ron Rivest、Robert Tarjan——其中 Rivest、Tarjan 均为图灵奖级人物。
12. **爱好的一面**：远足与双陆棋（backgammon）——Lipton 转述：Floyd 潜心研究双陆棋数学、近乎职业水准（ airport 双陆棋轶事为 Lipton 所述，引语归属注意）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（解析理论 — 蓝） | `#2E5A9E` | 算符优先文法 / 编译器 |
| 分类色 2（程序语义与验证 — 青绿） | `#1E8E8E` | Assigning Meanings to Programs / Hoare 逻辑先声 |
| 分类色 3（算法分析 — 琥珀） | `#D9A441` | Floyd–Warshall / 判圈算法 |
| 分类色 4（图像计算与普及 — 玫瑰） | `#C0395B` | Floyd–Steinberg 误差扩散 / TAOCP 审稿 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「从断言到语义、从图到像素」的普适算法语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：沉静 / 求真（无博士的正教授、以断言验证程序）
- **选定曲目**：Alex-Productions **With Me**（manifest 预分配，直接沿用），匹配"安静的完美主义者以逻辑锻造可靠软件"的叙事。
- **落地文件**：`turing/presentations/Robert_W._Floyd/WithMe.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「程序设计方法学先驱 · 美国」+ 弗洛伊德 1936–2001 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1936–2001 生平纵览
4. **早慧少年与芝加哥大学**（1936–1958）：14 岁中学毕业、17 岁文学士、物理学士、Sagan 室友
5. **无博士的教授之路**（1950s–1960s）：Armour Research Foundation、计算机操作员、CMU 27 岁副教授、Stanford 正教授
6. **解析理论先驱**（1960s）：算符优先文法、编译器与解析论文
7. **Assigning Meanings to Programs**（1967）：逻辑断言、程序验证、Hoare 逻辑的先声
8. **Floyd–Warshall：全源最短路径**：与 Warshall 各自独立
9. **弗洛伊德算法群像**：判圈算法、Floyd 三角、Floyd–Steinberg 误差扩散（含"dithering vs diffusion 区分"注记）
10. **与 Knuth 的协作**：TAOCP 主要审稿人、被引最多者、Bose-Nelson 合著
11. **IFIP WG 2.1 与 ALGOL**：ALGOL 60 / ALGOL 68 的国际标准工作
12. **图灵奖 1978**：整句引用 ACM citation
13. **门生与传承**：Rivest / Tarjan / Manna / Earley / Plaisted，共 7 名博士
14. **晚年与爱好**：1994 年因 Pick 病提前退休、远足与双陆棋（Lipton 轶事）
15. **结尾**：65 岁、"程序设计方法学奠基人"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **无博士学位**：Floyd 全程无 PhD——勿编造任何博士导师或博士学位；"27 岁副教授、六年后 Stanford 正教授"均按页面表述。
- **Floyd–Warshall 独立性**：与 Stephen Warshall **各自独立**设计——"independently" 一词必须保留，勿写"师承/引用关系"。
- **Hoare 逻辑归属**：1967 年 *Assigning Meanings to Programs* 是"贡献于后来成为 Hoare 逻辑的工作"——逻辑本身以 Hoare 命名，勿写"Floyd 创立 Hoare 逻辑"。
- **dithering vs diffusion**：Floyd 本人**区分** dithering（抖动）与 diffusion（扩散）两概念——勿混为一谈。
- **判圈算法归属**："attributed to him"（归功于他）——是归属表述，勿扩展成"首个发现者"的绝对表述。
- **图灵奖理由（核心红线）**：1978 整句 citation："for having a clear influence on methodologies for the creation of efficient and reliable software, and for helping to found the following important subfields of computer science: the theory of parsing, the semantics of programming languages, automatic program verification, automatic program synthesis, and analysis of algorithms"——五大子领域列举勿增删。
- **双陆棋引语归属**：O'Hare 机场轶事三段均为 **Richard J. Lipton** 所述（引语出处：Lipton, 2010），是 Lipton 的话而非 Floyd 原话——引语页注明"据 Lipton 转述"。
- **门生数字**：页面明载 "supervised seven Ph.D. graduates"（7 名博士），infobox 只列 5 名——表格列 infobox 5 人并加"共 7 名"注，勿把 infobox 5 人当全量。
- **中间名**：Robert **Willoughby** Floyd，后依法改为 "W"——身份页写全名时可加注。
- **生卒与死因**：1936-06-08 ~ 2001-09-25，享年 65；晚年患 Pick 病（neurodegenerative）并于 **1994 年提前退休**——死因页面未明写，勿编造。
- **奖项**：图灵奖 1978、IEEE Computer Pioneer Award 1991、AAAS Fellow 1974——页面无其他大奖，勿编造（无 Kyoto、无 National Medal）。
- **机构顺序**：Illinois Institute of Technology（Armour Research Foundation）→ Carnegie Mellon University → Stanford University——勿乱序。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 罗伯特·弗洛伊德（或 弗洛伊德） | 待写入 |
| name_en | Robert W. Floyd | 待写入 |
| birth_date | 1936-06-08 | 待写入 |
| death_date | 2001-09-25 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | algorithms / parsing / programming language semantics / program verification | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **合作者**：Donald Knuth（TAOCP 主要审稿人、Bose-Nelson 问题合著）、Richard Beigel（The Language of Machines 合著）、Jeffrey D. Ullman（1980 正则表达式编译入 IC 论文）、Alan J. Smith（1972 合著）
- **博士生**：Jay Earley、Zohar Manna、David Plaisted、Ron Rivest、Robert Tarjan（infobox 所列 5 人；共 7 名博士）
- **家庭**：Christiane Floyd（前妻，计算机科学家）——如需录入 spouse 关系按页面实载
- **导师**：无正规博士导师，**无载禁写**

## 8. 奖项清单

- Turing Award（1978，五大子领域奠基 citation）
- Fellow of the American Academy of Arts and Sciences（1974）
- IEEE Computer Pioneer Award（1991）

## 9. 机构清单

- 教育：University of Chicago（B.A. 1953、B.S. 物理学 1958）
- 任职：Armour Research Foundation / Illinois Institute of Technology（1950s–1960s 初）→ Carnegie Mellon University（副教授，约 27 岁）→ Stanford University（正教授，六年后；1994 年提前退休）

## 10. 终审清单

- [ ] 生卒 1936-06-08 / 2001-09-25，享年 65，出生地 New York City，去世地 Stanford
- [ ] "无博士学位的教授"表述准确（17 岁 BA / 1958 物理 BS / 无 PhD）
- [ ] Floyd–Warshall "与 Warshall 各自独立"表述准确
- [ ] 1967 论文"Hoare 逻辑先声"口径准确，未抢功
- [ ] dithering / diffusion 区分注记在位
- [ ] 图灵奖 citation 五大子领域整句引用无误
- [ ] 门生"共 7 名博士 + infobox 5 人"表述准确
- [ ] 双陆棋轶事标注"据 Lipton 转述"
- [ ] 肖像文件核对：`images/Robert_W._Floyd.jpg`（或 250px 版，c. 1970s）
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Stanford · CMU · IIT | Turing 1978`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1978/Robert W. Floyd/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Robert_W._Floyd.jpg`（约 1970s 肖像，已就绪；250px 版可用则取 500px/原版）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语（ACM citation、Lipton 轶事）必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Iverson / Hoare）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
