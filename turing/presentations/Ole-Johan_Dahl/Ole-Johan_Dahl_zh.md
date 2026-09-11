# Ole-Johan Dahl（奥利-约翰·达尔）立传提示词

> qid=Q92745 · 1931-10-12 – 2002-06-29 · 挪威计算机科学家 · 20 世纪 · 2001 图灵奖（与 Kristen Nygaard 共享）
> 本地 Wikipedia 数据源：`turing/pages/2001/Ole-Johan Dahl/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 挪威`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（类/继承/子类的结构化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ole-Johan Dahl（中文惯称：奥利-约翰·达尔）
- **生卒**：1931-10-12 生于 Mandal, Norway → 2002-06-29 逝于 Asker, Norway，享年 70（**页面未载死因，勿编造**）
- **国籍**：挪威（Norwegian）
- **身份**：计算机科学家、Oslo 大学计算机教授；与 Kristen Nygaard 并称 Simula 与面向对象编程（object-oriented programming）之父之一
- **家庭**：父 Finn Dahl（1898–1962）、母 Ingrid Othilie Kathinka Pedersen（1905–80）；7 岁随家迁 Drammen；**13 岁时二战德占期间全家逃往瑞典**——家庭叙事一笔带过，不渲染
- **教育**：战后入 University of Oslo 研究数值数学（numerical mathematics，BS, MS）
- **师承**：页面未载博士导师（无 PhD 记载）——勿编造
- **研究领域**：计算机科学（Simula 语言、程序结构、形式化方法）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖（2001，与 Nygaard 共享）**：ACM 授予 Dahl 与 Nygaard 2001 图灵奖；Nygaard 篇载有 citation 整句（"For ideas fundamental to the emergence of object-oriented programming, through their design of the programming languages Simula I and Simula 67."），Dahl 页面未另载 citation——引用时用 ACM 同句并注明二人共享。
2. **面向对象概念的首创（与 Nygaard）**：在挪威计算中心（Norwegian Computing Center, NCC/Norsk Regnesentral）率先提出 **class（类）、subclass（子类，允许隐式信息隐藏）、inheritance（继承）、dynamic object creation（动态对象创建）** 等 OO 范式核心概念——"first to develop the concepts" 为页面实载，可写。
3. **Simula 双阶段**：Simula I（1961–1965）与 Simula 67（1965–1968）——最初是 ALGOL 60 的扩展变体与超集，用于离散事件**仿真**。
4. **早期计算岁月**：1957 年首篇论文《Multiple index countings on the Ferranti Mercury computer》（挪威国防研究院 NDA/FFI 出版）；1963 年 Simscript 实现报告（NCC）——从军事计算到计算中心的轨迹。
5. **Simula 1966 CACM 论文**：Dahl & Nygaard, "Simula: an ALGOL-based simulation language", *Communications of the ACM* 9(9): 671–678——Simula 的奠基文献。
6. **1967 IFIP "Class and subclass declarations"**：Dahl 任 IFIP 仿真编程语言工作会议主席，发表论文定义类与子类声明——OO 概念定名的关键节点。
7. **Simula 67 Common Base Language（1968）**：Dahl、Bjørn Myhrhaug、Nygaard 三人合著的语言标准报告——Dahl 是语言实现与规范的核心工程师（本篇侧重实现/语言规范侧）。
8. **《Structured Programming》（1972）**：与 C.A.R. Hoare 合著的 "Hierarchical Program Structures"（大概是其影响最大的论文），收录于 Dahl、Dijkstra、Hoare 三人的 *Structured Programming*——"1970 年代最知名的软件学术著作"（页面原文明示，可写）。
9. **形式化方法的转向**：职业生涯后期日益投入 formal methods，用数学严格性论证（例如）面向对象的有效性——从"实践到形式数学基础"的全谱系专家。
10. **Oslo 大学教授（1968–）**：1968 年起任 Oslo 大学正教授，以教学天赋著称（"a gifted teacher as well as researcher"，页面实载）。
11. **挪威最伟大的计算机科学家**："widely accepted as Norway's foremost computer scientist"（页面实载，可写）。
12. **身后命名**：AITO（Association Internationale pour les Technologies Objets）以二人之名设立 **Dahl–Nygaard Prize**，每年在 ECOOP 颁发（senior + junior 两席）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（Simula 语言 — 蓝） | `#2E5A9E` | Simula I / Simula 67 / ALGOL 60 |
| 分类色 2（面向对象概念 — 青绿） | `#1E8E8E` | 类 / 子类 / 继承 / 动态对象 |
| 分类色 3（程序结构与形式化 — 琥珀） | `#D9A441` | Hierarchical Program Structures / formal methods |
| 分类色 4（挪威计算中心时代 — 玫瑰） | `#C0395B` | NCC / Ferranti Mercury 起点 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「类的层级树 / 对象的自包含结构」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：开创 / 激越（从 ALGOL 中锻造出类与继承、OO 范式席卷现代软件）
- **选定曲目**：Alex-Productions **Savage**（manifest 预分配，直接沿用；化学 Emil Fischer 篇同曲，属正常复用），匹配"语言工程开疆拓土"的力度感。
- **落地文件**：`turing/presentations/Ole-Johan_Dahl/Savage.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「Simula 之父 · 挪威」+ 达尔 1931–2002 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1931–2002 生平纵览
4. **早年：Mandal 与战争流亡**（1931–1945）：Drammen、13 岁逃往瑞典、战后 Oslo 数值数学
5. **Ferranti Mercury 起点**（1957–1963）：FFI 自动编码项目、Simscript 实现
6. **挪威计算中心**：NCC 的仿真语言项目、与 Nygaard 的合作开端
7. **Simula I（1961–1965）**：ALGOL 60 超集、离散事件仿真
8. **1966 CACM 论文**：Simula 语言的公开定义（公式框：ALGOL → Simula 的概念扩展）
9. **Simula 67：类与子类**：1967 IFIP 论文、1968 Common Base Language（含 Myhrhaug）
10. **OO 范式的四大概念**：class / subclass / inheritance / dynamic object creation
11. **《Structured Programming》（1972）**：与 Hoare 的 Hierarchical Program Structures、Dijkstra 三人书
12. **Oslo 大学与形式化方法**（1968–2002）：1968 正教授、gifted teacher、后期的 formal methods
13. **荣誉**：Turing 2001（共享）、IEEE von Neumann Medal 2002（共享）、St. Olav 指挥官勋章 2000、Dahl–Nygaard Prize
14. **遗产**：C++ 与 Java 时代的 OO 基石、"挪威最伟大的计算机科学家"
15. **结尾**：70 岁、2002-06-29 逝于 Asker、OO 大一统的奠基人

## 5. 史实陷阱与敏感点（终审必须检查）

- **与 Nygaard 的侧重分工（批次红线）**：本篇侧重 **Simula 实现与语言规范**（Ferranti Mercury 起点、CACM 论文、1967 IFIP、Common Base Language、Hoare 合书、formal methods）；OO 思想推广、社会项目、政治参与留给 Nygaard 篇。**两人恩怨页面无载，禁写任何分歧/矛盾**。
- **图灵奖 citation**：Dahl 页面本身未载 citation 整句；如需引用用 Nygaard 页面/ACM 的 "For ideas fundamental to the emergence of object-oriented programming, through their design of the programming languages Simula I and Simula 67."，并**明确写共享**（"与 Kristen Nygaard 共享 2001 图灵奖"）。
- **"first to develop" 的主语**：是"Dahl **与 Nygaard** 首次发展了 class/subclass/inheritance/dynamic object creation 概念"——**两人并列**，勿写 Dahl 独创。
- **OO 影响句**：可写"OO 方法现已遍及现代软件开发，包括 C++ 与 Java 等广泛使用的命令式语言"——仅此句，勿再延伸"一切现代语言皆受影响"。
- **Simula I / Simula 67 年份**：Simula I = 1961–1965；Simula 67 = 1965–1968（开发期）——勿把 1967 写成"发布年"以外的其他含义（1967 IFIP 会议论文与 1968 出版、1968 Common Base Language 报告）。
- **学位**：Oslo 大学 BS、MS（数值数学）——**页面无 PhD**；勿编造博士导师。
- **死因**：页面未载——写"未详述，勿编造"；享年 70。
- **St. Olav 勋章年份**：Dahl 页面写 **2000** 年获 Command of the Royal Norwegian Order of St. Olav（Nygaard 页面写 2000 年 8 月由国王 Harald V 授勋——Dahl 篇只写 2000 即可）。
- **von Neumann Medal**：**2002** 年（与 Nygaard 共享）——勿写 2001。
- **Early papers 使用红线**：早期论文（1957/1958/1963/1965/1966/1968）只取 2–3 条代表作（1957 首篇、1966 CACM、1968 Common Base），勿整清单罗列进正文页。
- **家庭细节**：仅父母生卒与流亡一笔——页面无载配偶/子女，勿编造。
- **全文无直接引语**：页面无 Dahl 本人任何直接引语——勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | manifest 为 null，待补 |
| name_zh | 达尔（或 奥利-约翰·达尔） | 待写入 |
| name_en | Ole-Johan Dahl | 待写入 |
| birth_date | 1931-10-12 | 待写入 |
| death_date | 2002-06-29 | 待写入 |
| nationality | Norway | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | Simula / object-oriented programming / formal methods | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **合作者（核心）**：Kristen Nygaard（Simula 联合设计者、图灵奖共享、von Neumann Medal 共享——collaborator）、Bjørn Myhrhaug（Simula 67 Common Base Language 合著）、C.A.R. Hoare（*Structured Programming* 合书——collaborator）、Edsger Dijkstra（同书作者，三人合著关系可入库）
- **机构同事参照**：Jan V. Garwick（1958 Ferranti Mercury 手册合著）、Vic Bell（1963 Simscript 报告合著）——按页面实载酌情入库
- **无载禁写**：页面未载博士导师/学生名单——明写"无载禁写"；勿从 Nygaard 篇倒灌研究生关系

## 8. 奖项清单

- Turing Award（2001，与 Kristen Nygaard 共享）
- IEEE John von Neumann Medal（2002，与 Kristen Nygaard 共享）
- Commander of the Royal Norwegian Order of St. Olav（2000）
- Dahl–Nygaard Prize（AITO 设立、ECOOP 年度颁发，以二人命名——身后纪念）

## 9. 机构清单

- 教育：University of Oslo（数值数学 BS、MS）
- 任职：Norwegian Defence Research Establishment（FFI，Ferranti Mercury 时代，1957–58 论文出版方）、Norwegian Computing Center（NCC，Simula I / Simula 67 研发基地）、University of Oslo（1968 年起正教授，至逝世）

## 10. 终审清单

- [ ] 生卒 1931-10-12 / 2002-06-29，享年 70，出生地 Mandal，去世地 Asker；死因留白不编造
- [ ] 图灵奖"2001 与 Nygaard 共享"表述准确；citation 引用时注明共享
- [ ] 四大 OO 概念主语为"二人"，勿写成 Dahl 独创
- [ ] Simula I 1961–1965 / Simula 67 1965–1968 年份区间准确
- [ ] CACM 1966 论文、1967 IFIP、1968 Common Base Language 三节点年份无误
- [ ] 《Structured Programming》1972 三人书（Dahl/Dijkstra/Hoare）表述准确
- [ ] 本篇侧重：实现/规范/Hoare 合书/formal methods；社会与政治内容不进入本篇
- [ ] 无 PhD / 无博士导师，页面无载禁写
- [ ] 国籍用「挪威」，封面底部状态栏 `挪威 | NCC · University of Oslo | Turing 2001`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2001/Ole-Johan Dahl/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Ole-Johan_Dahl.jpg`（真肖像，已就绪；250px 版可作降级）
- [ ] **国籍**：封面顶部徽章明示挪威
- [ ] **引语核对**：全文无本人直接引语——勿编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同奖共享者 Nygaard 篇格式对齐、侧重点不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
