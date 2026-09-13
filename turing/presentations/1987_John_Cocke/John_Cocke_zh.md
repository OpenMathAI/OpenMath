# John Cocke（约翰·科克）立传提示词

> qid=Q6226492 · 1925-05-30 – 2002-07-16 · 美国计算机科学家（IBM） · 20 世纪 · 1987 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1987/John Cocke/`（index.html + metadata.json + images）
> ✅ **数据源已修复（主控更新）**：本地已按正确标题补抓完整条目 `turing/pages/1987/John Cocke (computer scientist)/`（index.html + metadata.json + images/John_Cocke_computer_scientist_.jpg）。本提示词事实基准现以**该本地页面为准**；ACM 官方图灵奖页（amturing.acm.org）作辅助核对源。

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。肖像用本地 `images/John_Cocke_computer_scientist_.jpg`（已随正确条目补抓）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧肖像位（装饰圆）+ 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。事实取自 Wikipedia 线上条目与 ACM 官方页，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 RISC 设计理念 / 编译优化变换列表的表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Cocke（中文惯称：约翰·科克）
- **生卒**：1925-05-30 生于夏洛特（Charlotte, North Carolina, US）→ 2002-07-16 逝于瓦尔哈拉（Valhalla, New York），享年 77（NYT 讣告标题 "John Cocke, a Chip Wizard From I.B.M., Is Dead at 77"；死因页面未详述，勿编造）
- **国籍**：美国（American）
- **身份**：计算机科学家、IBM 体系结构与编译器传奇（"RISC 架构之父"）
- **家庭**：**页面未载**父母/配偶/子女——勿编造，身份页相应格写"页面未载"
- **教育轨迹**（Duke University 三学位）：
  - 机械工程 **BS 1946**
  - **MS**（信息框提及；具体方向页面未详述）
  - **数学 PhD 1956**（Wikipedia 信息框作 1956；ACM 官方页正文有 1953/1956 两处表述——存疑，见 §5）
- **博士导师**：**页面未载**——勿编造
- **任职**：IBM（信息框作 1956–1992；ACM 官方传记作 1954 起，两说见 §5）；IBM Fellow（1972）
- **研究领域**：计算机体系结构、优化编译器、语音识别与机器翻译

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 1987**：citation 整句引用——"For significant contributions in the design and theory of compilers, the architecture of large systems and the development of reduced instruction set computers (RISC); for discovering and systematizing many fundamental transformations now used in optimizing compilers including reduction of operator strength, elimination of common subexpressions, register allocation, constant propagation, and dead code elimination."（ACM 官方页实载）
2. **"RISC 架构之父"**：被许多人誉为 "the father of RISC architecture"——核心理念：**指令集与编译器实际生成的相对简单指令相匹配**，以低成本实现高性能；"使用更少指令，但设计能极快执行简单指令的芯片"（The Guardian 讣告转述）。
3. **IBM 801 项目（1975 年起领导）**：其创新最受瞩目的项目，被视为**第一台 RISC 机器**；硬件与编译器**紧耦合、同步开发**的设计理念；对比此前 IBM 7030 "Stretch" 的 735 条指令；PL.8 编译器首次完整实现寄存器分配器（避免内存访问延迟）与指令调度器（隐藏分支延迟）。
4. **优化编译器的系统化者**：发现并系统化众多现代编译器基本变换——算符强度削减、公共子表达式消除、寄存器分配、常量传播、死代码消除、指令调度、数组范围检查等（citation 与 ACM 页实载）。
5. **与 Frances Allen 的区间分析**：与 **Frances Allen**（2006 图灵奖得主、IBM 同事）共同开发**区间分析**（interval analysis）——基于控制流图归约的程序分析技术。
6. **Stretch 项目（IBM 7030）**：参与共同设计指令流水线、纠错码（ECC）、指令调度、寄存器分配——Stretch 成为 System/360 的原型。
7. **ACS 项目（1960 年代）**：提出超标量处理、存储缓冲区、分支预测等概念的前身。
8. **CYK 算法的 "C"**：Cocke–Younger–Kasami 算法共同发明者（上下文无关句法分析）。
9. **语音识别与机器翻译**：参与 IBM 1970–80 年代先驱性统计方法研究；被 Frederick Jelinek 归功于提出在语音识别中使用 **trigram（三元组）语言模型**的想法。
10. **与 NYU 的编译优化专著**：与 Jacob T. Schwartz（NYU）合著**最早的综合性编译器优化研究**。
11. **产业遗产**：技术直接催生 IBM RS/6000 工作站、**PowerPC 架构**（Apple/IBM/Motorola）与 Blue Gene/L 超级计算机；Sun、MIPS、Motorola、Intel、HP 均发展 RISC 处理器。
12. **荣誉矩阵**：IEEE von Neumann Medal（1984）、Eckert–Mauchly 奖（1985）、Turing（1987）、Computer Pioneer 奖（1989）、National Medal of Technology（1991）、National Medal of Science（1994）、Seymour Cray 计算机工程奖（1999）、Benjamin Franklin Medal（2000）、Computer History Museum Fellow（2002，理由：开发并实现 RISC 体系结构与程序优化技术）；IBM Fellow（1972）；NAS/美国艺术与科学院/美国哲学会会员；20 余项专利。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（RISC 体系结构 — 蓝） | `#2E5A9E` | IBM 801 / Stretch / ACS / PowerPC |
| 分类色 2（优化编译器 — 青绿） | `#1E8E8E` | 区间分析 / 基本变换 / PL.8 编译器 |
| 分类色 3（统计方法 — 琥珀） | `#D9A441` | 语音识别 / 机器翻译 / trigram / CYK |
| 分类色 4（IBM 殿堂 — 玫瑰） | `#C0395B` | IBM Fellow / 产业遗产 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏指令方块阵列（精简指令流水线），呼应「以少胜多的 RISC 哲学」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：深沉 / 求索（在硬件与编译器的深水区追索性能）
- **选定曲目**：Alex-Productions **The Invisible Light**（manifest 预分配，直接沿用），匹配"看不见的优化变换成就看得见的性能"的叙事。
- **落地文件**：`turing/presentations/John_Cocke/TheInvisibleLight.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「RISC 架构之父 · 美国」+ 科克 1925–2002 + 右上肖像位（装饰圆占位）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左肖像位（装饰圆）+ 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 任职 / IBM Fellow / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1925–2002 生平纵览
4. **夏洛特到杜克**（1925–1956）：机械工程 BS 1946 → 数学 PhD（1956，年份存疑标注）、家庭信息页面未载
5. **加入 IBM 与 Stretch 项目**（1950s）：IBM 7030、流水线/ECC/指令调度/寄存器分配、System/360 原型
6. **ACS 项目与超前瞻**（1960s）：超标量、存储缓冲、分支预测的前身
7. **IBM Fellow 与编译器系统化**（1972 起）：优化变换清单（强度削减/公共子表达式/寄存器分配/常量传播/死代码消除）
8. **区间分析：与 Frances Allen 的合作**：控制流图归约、程序分析
9. **IBM 801 与 RISC 诞生**（1975 起）：紧耦合设计、735 条指令之减、PL.8 编译器 ★ 核心页
10. **"RISC 架构之父"**：设计理念页（用更少指令、极快执行简单指令）
11. **图灵奖 1987**：citation 整句展示
12. **统计方法的远见**：CYK 算法、语音识别/机器翻译、trigram 语言模型（Jelinek 归功）
13. **产业遗产**：RS/6000、PowerPC、Blue Gene/L、Sun/MIPS/Intel 的 RISC 世界
14. **荣誉与晚年**：Eckert–Mauchly 1985、NMT 1991、NMS 1994、Cray 奖 1999、Franklin Medal 2000、CHM Fellow 2002
15. **结尾**：77 岁、"Chip Wizard"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **数据源口径**：本地页面已补抓为正确条目 `John Cocke (computer scientist)`——tex 事实以本地为准，ACM 官方页作辅助；IBM 入职年份与 Duke PhD 年份两处页面冲突按 §5 的"1950 年代中期/1956 加注"口径执行。
- **图灵奖 citation**：整句引用 ACM 官方页长 citation（见 §2 第 1 条）——本篇核心红线；注意 citation 中编译变换枚举顺序（operator strength → common subexpressions → register allocation → constant propagation → dead code elimination）。
- **IBM 入职年份两说**：Wikipedia 信息框作 **1956**–1992；ACM 官方传记作 **1954** 起（"37 年"）。写法："1950 年代中期加入 IBM，服务至 1992"；如需具体年份写"1956（Wikipedia 信息框；ACM 传记作 1954）"两说并注。
- **Duke PhD 年份存疑**：Wikipedia 信息框作 **1956**；ACM 官方页正文出现 1953/1956 两种表述——**以 Wikipedia 信息框 1956 为准**并加脚注说明 ACM 页两说。
- **"RISC 之父"表述**："被许多人誉为"——保留誉称的"公论"属性，勿写成官方授予头衔。
- **第一台 RISC 机器**：ACM 页称 IBM 801 "被视为第一台 RISC 机器"（believed to be the first）——保留"被视为"，勿写成定论。
- **无导师/无门生**：页面未载博士导师与博士生名单——§7 写"无载禁写"，勿从 Math Genealogy 之外补人。
- **家庭未载**：父母/配偶/子女页面均无——勿编造。
- **CYK 归属**：Cocke 是 **"C"**——CYK 三人共同命名算法，勿写成 Cocke 独创或漏掉 Younger/Kasami。
- **trigram 归功方向**：是 **Jelinek 把 trigram 想法归功于 Cocke**（credited）——因果方向勿反。
- **与 Frances Allen 关系**：IBM 同事 + 区间分析合作者——勿写成师承/亲属；Allen 2006 图灵奖可提但不展开。
- **死因**：页面未详述——只写"2002-07-16 逝于 Valhalla，享年 77"，勿编造病因。
- **奖项年份**：von Neumann Medal **1984**（正文均作 1984；Wikipedia 信息框另有一处 1994 为噪声，勿采）；Eckert–Mauchly 1985；NMT 1991；NMS 1994；Cray 奖 1999；Franklin Medal 2000；CHM Fellow 2002。
- **引语红线**：可引用的只有①图灵奖 citation（ACM 官方页）、②Guardian 讣告对 RISC 理念的转述（标注"讣告转述"）、③CHM Fellow 2002 理由。**全文无 Cocke 本人直接引语，勿编造。**

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 科克（或 约翰·科克） | 待写入 |
| name_en | John Cocke | 待写入 |
| birth_date | 1925-05-30 | 待写入 |
| death_date | 2002-07-16 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer architecture / RISC / optimizing compilers / speech recognition | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：**页面未载，禁写**（仅 Math Genealogy 外链，未核实不入库）
- **合作者**：Frances Allen（区间分析，IBM 同事）、Jacob T. Schwartz（NYU，编译优化合著）、Victoria Markstein（"The Evolution of RISC Technology at IBM" 合著者，IBM JRD 1990）、Frederick Jelinek（语音识别统计方法团队，trigram 想法由 Jelinek 归功于 Cocke）
- **博士生**：**页面未载，禁写**
- **家庭**：**页面未载，禁写**

## 8. 奖项清单

- IEEE John von Neumann Medal（1984）
- Eckert–Mauchly Award（1985）
- Turing Award（1987，citation 见 §2 第 1 条）
- Computer Pioneer Award（1989）
- National Medal of Technology（1991）
- National Medal of Science（1994）
- Franklin Institute Certificate of Merit（1996）
- Seymour Cray Computer Engineering Award（1999）
- Benjamin Franklin Medal（2000）
- Computer History Museum Fellow（2002）
- IBM Fellow（1972）；NAS / American Academy of Arts and Sciences / American Philosophical Society 会员

## 9. 机构清单

- 教育：Duke University（机械工程 BS 1946 / MS / 数学 PhD 1956，年份两说见 §5）
- 任职：IBM（信息框作 1956–1992；ACM 传记作 1954 起；IBM Fellow 1972）——Stretch / ACS / 801 项目在其间

## 10. 终审清单

- [ ] 生卒 1925-05-30 / 2002-07-16，享年 77，出生地 Charlotte，去世地 Valhalla，死因勿编造
- [ ] 图灵奖 citation 整句引用（ACM 官方页），编译变换枚举顺序正确
- [ ] IBM 入职年份两说（1956 vs 1954）按"1950 年代中期"稳妥表述
- [ ] Duke PhD 1956 为准、ACM 页 1953/1956 两说加脚注
- [ ] "RISC 之父"="被许多人誉为"；"第一台 RISC 机器"保留"被视为"
- [ ] 无肖像 → 装饰圆占位（封面 + 身份页）
- [ ] 无导师/无门生/家庭未载——全部禁写
- [ ] CYK 的 "C"、trigram 归功方向（Jelinek→Cocke）、Allen 为同事合作者
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | IBM · Duke | Turing 1987`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **数据源复核**：本地 `turing/pages/1987/John Cocke (computer scientist)/index.html` 已补抓为正确条目——逐条对照本地页面核对 tex 全部事实（ACM 官方页作辅助）
- [ ] **头像**：使用 `turing/pages/1987/John Cocke (computer scientist)/images/John_Cocke_computer_scientist_.jpg`（执行时复制到 presentations/John_Cocke/images/）
- [ ] **citation 复核**：对照 amturing.acm.org 原句逐词核对
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语仅限 §5 列出的三处
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐（无肖像时装饰圆与信息网格的排版）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Wirth / Karp / Hopcroft / Tarjan）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
