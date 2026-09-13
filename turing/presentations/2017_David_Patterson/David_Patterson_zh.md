# David Patterson（大卫·帕特森）立传提示词

> qid=Q92851 · 1947-11-16 生（在世留白） · 美国计算机科学家 · 20/21 世纪 · 2017 图灵奖（与 Hennessy 共享）
> 本地 Wikipedia 数据源：`turing/pages/2017/David Patterson (computer scientist)/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（RISC 简化指令译码 / RAID 冗余阵列 / register windows 的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：David Andrew Patterson（中文惯称：大卫·帕特森）
- **生卒**：1947-11-16 生于 Evergreen Park, Illinois（美国）→ **在世留白**（页面无卒日，勿编造）
- **国籍**：美国（American）
- **身份**：计算机科学家、教育家；"computer pioneer"（页面原话）；RISC 术语创造者（coined the term "RISC"）、Berkeley RISC 项目领导者
- **家庭**：妻子 Linda Patterson（1967 结婚）——仅一笔带过
- **教育轨迹**：
  - South High School（Torrance, California）
  - UCLA **BA 数学**（1969）→ **MS**（1970）→ **PhD 计算机科学**（1976），博士论文 *Verification of Microprograms*
- **博士导师**：David F. Martin、Gerald Estrin（UCLA，双导师）
- **研究领域**：计算机系统（computer systems）
- **任职**：UC Berkeley 计算机科学教授（1976 起，近四十年）；2016 宣布退休 → Google distinguished engineer；RISC-V Foundation 董事会副主席；UC Berkeley Pardee Professor Emeritus；2025 起 Laude Institute 董事会主席（与 Jeff Dean、Joelle Pineau、Andy Konwinski 共事）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **"RISC" 术语的创造者**：页面明载 "having coined the term RISC"；1980 年与 David Ditzel 发表 *The Case for the Reduced Instruction Set Computer*（ACM SIGARCH CAN）——RISC 概念的宣言式论文。
2. **Berkeley RISC 项目（1980 起）**：与 **Carlo H. Sequin** 共同领导，引入 **register windows**（寄存器窗口）技术；RISC-I 是 **1981 年**由 Berkeley 学生设计建造的**首台 VLSI 精简指令集计算机**。
3. **IEEE Milestone 铭牌（2015-02-12）**：IEEE 在 Berkeley Soda Hall 为 RISC-I 立牌，铭文（可整段引用）："UC Berkeley students designed and built the first VLSI reduced instruction-set computer in 1981... RISC-I influenced instruction sets widely used today, including those for game consoles, smartphones and tablets."——本篇最有画面感的实证。
4. **RAID（1988）**：与 **Randy Katz、Garth Gibson** 发表 *A Case for Redundant Arrays of Inexpensive Disks (RAID)*（ACM SIGMOD Record）——存储工业的标准词汇由此而来。
5. **Network of Workstations（NOW）**：1995 年与 Thomas Anderson、David Culler 发表 *A Case for NOW*（IEEE Micro）——Berkeley 计算机集群早期工作。
6. **教科书双雄**：与 Hennessy 合著 7 本书中最重要的两本——《Computer Architecture: A Quantitative Approach》（7 版）与《Computer Organization and Design》（6 版，RISC-V Edition）；自 1990 年起成为全球标准教材；另有与 Andrew Waterman 合著的《The RISC-V Reader》。
7. **从 RISC 到 RISC-V**：任 **RISC-V Foundation 董事会副主席**——开放指令集是 Berkeley RISC 精神的当代延续（叙事闭环）。
8. **学界领袖**：ACM **主席（2004–06）**、CRA 主席、Berkeley CS Division 主任、美国总统信息技术顾问委员会 PITAC（2003–05）。
9. **桃李满门**：David Ditzel（Transmeta 创始人）、Garth Gibson（RAID 共同发明人、Vector Institute 首 CEO）、David Ungar（Self 语言设计者）、Remzi Arpaci-Dusseau、Christos Kozyrakis 等。
10. **Google 第二幕（2016–）**：宣布退休后成为 Google distinguished engineer——从体系结构转向软件工程/ML 基建（按页面表述）。
11. **荣誉**：2017 图灵奖、2022 Draper Prize、2008 Eckert–Mauchly Award、NAS 2006、NAE、约 50 项研究/教学/服务奖项。
12. **人生彩蛋（页面实载，结尾页可用）**：1966 年 El Camino College 摔跤队加州州冠军成员（2018 入队 Hall of Fame）；2013 年加州力量举锦标赛创下本体重/年龄组四项州纪录（卧推/硬拉/深蹲/三项合计）——"图灵奖得主的硬核体能"，一笔带过增趣。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（RISC 与 Berkeley — 蓝） | `#2E5A9E` | RISC-I / register windows / Ditzel 宣言 |
| 分类色 2（存储革命 — 青绿） | `#1E8E8E` | RAID / Katz & Gibson |
| 分类色 3（系统与集群 — 琥珀） | `#D9A441` | NOW / RISC-V Foundation |
| 分类色 4（教育与领袖 — 玫瑰） | `#C0395B` | 教科书双雄 / ACM 主席 / 教学奖 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：寄存器窗口堆叠/阵列方块（稀疏嵌套矩形），呼应「简化指令 + 冗余阵列」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：昂扬 / 普惠（一套指令集装进 99% 的芯片）
- **选定曲目**：Alex-Productions **SEA**（manifest 预分配，直接沿用），匹配"开源指令集奔流入海"的开阔叙事。
- **落地文件**：`turing/presentations/David_Patterson/SEA.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「RISC 命名者 · RAID 先驱 · 美国」+ Patterson 1947– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1947–至今 生平纵览
4. **伊利诺伊少年与加州成长**：Evergreen Park 出生、Torrance 高中、UCLA 数学→CS
5. **UCLA 博士**（1976）：微程序验证、双导师 Martin & Estrin
6. **Berkeley 执教与 RISC 项目**（1976–1981）：与 Sequin 共同领导、register windows
7. **"The Case for RISC"**（1980）：与 Ditzel、术语的诞生
8. **RISC-I 与 IEEE Milestone**（1981 / 2015 铭牌）：VLSI 首例、铭文引用
9. **RAID**（1988）：与 Katz、Gibson；存储工业标准词汇
10. **NOW 与集群**（1995）：Network of Workstations
11. **教科书双雄**：与 Hennessy 的 CAQA/COD、DLX、RISC-V Edition
12. **学界领袖**：ACM 主席 2004–06、PITAC、CRA
13. **从 RISC 到 RISC-V 与 Google**：RISC-V Foundation 副主席、2016 Google distinguished engineer、Laude Institute 2025
14. **荣誉与桃李**：Turing 2017、Draper 2022、Eckert–Mauchly 2008；Ditzel/Gibson/Ungar 等门生
15. **结尾**：在世留白；"99% 芯片 + 力量举纪录"的完整人生彩蛋页

## 5. 史实陷阱与敏感点（终审必须检查）

- **与 Hennessy 共享结构**：2017 图灵奖两人共享。本篇侧重 Patterson：RISC 术语/RISC-I/RAID/NOW/Berkeley/学界服务；Hennessy 篇侧重 MIPS/斯坦福/Alphabet——教科书与定量方法两篇均可提，但叙事重心勿重复。
- **"coined the term RISC" 归属**：页面明载 RISC 术语由 Patterson 创造（**本篇专属亮点**）；Hennessy 篇不得写此。同时 1981 年 MIPS 项目是 Hennessy "following preliminary investigations at Berkeley"——Berkeley 在先，勿颠倒。
- **获奖理由（整句引用，核心红线）**：两人共享，表述为 `"pioneering a systematic, quantitative approach to the design and evaluation of computer architectures with enduring impact on the microprocessor industry"`（页面原句 "The award attributed them for pioneering..."）。
- **RISC-I 年份**：IEEE 铭牌铭文写 **1981 年设计建造**；Berkeley RISC 项目 **1980 年启动**（与 Sequin）——项目年 vs 芯片年勿混。
- **RAID 全称两写**：inexpensive（1988 论文标题）与 independent（正文后段 "redundant arrays of independent disks"）——按所引文献语境选择，勿混用于同一句。
- **图灵奖公布日期**：2018-03-21（页面实载），获奖年 2017——"2017 图灵奖（2018 年 3 月公布）"。
- **Draper Prize 2022**：与 Hennessy、Steve Furber、Sophie Wilson 四人共享——勿写两人。
- **学位**：UCLA BA 数学 1969 / MS 1970 / PhD CS 1976——BA 是**数学**、PhD 才是 CS，勿互换。
- **退休表述**：2016 "announced retirement" → Google distinguished engineer；RISC-V Foundation 为 vice chair（副主席），勿写主席。
- **Eckert–Mauchly Award 2008**：infobox 实载；页面另载 Chuck Thacker 2017 获同名奖（参考文献标题）——勿张冠李戴。
- **力量举/摔跤彩蛋**：页面实载，仅限结尾页一笔带过增趣，勿占主线篇幅。
- **在世留白**：born 1947-11-16，写作 `1947–`。
- **可引语**：IEEE Milestone 铭文（整段可引）；本人无直接引语，**勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 帕特森（或 大卫·帕特森） | 待写入 |
| name_en | David Patterson | 待写入 |
| birth_date | 1947-11-16 | 待写入 |
| death_date | NULL（在世） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer systems / computer architecture | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：David F. Martin、Gerald Estrin（UCLA，双导师）
- **合作者**：John L. Hennessy（教科书双雄、共享图灵/Draper/BBVA）、Randy Katz（RAID）、Garth Gibson（RAID）、Carlo H. Sequin（Berkeley RISC 共同领导）、David Ditzel（Case for RISC）、David Culler & Thomas Anderson（NOW）、Andrew Waterman（RISC-V Reader）、Michael Stonebraker & John Ousterhout（XPRS 1988 论文——选写）
- **著名博士生**：David Ditzel（Transmeta）、Garth Gibson（Panasas/Vector Institute）、David Ungar（Self）、Remzi Arpaci-Dusseau、Christos Kozyrakis、Michael Dahlin、Mark D. Hill、Kimberly Keeton
- **页面无载的关系**：勿补

## 8. 奖项清单

- Karlstrom Outstanding Educator Award（1991）
- ACM Fellow（1994）、IEEE Fellow
- National Academy of Engineering + National Academy of Sciences 院士（NAS 2006）
- American Academy of Arts and Sciences（2006）、AAAS Fellow（2007）
- Computer History Museum Fellow（2007，"fundamental contributions to engineering education, advances in computer architecture..."）
- ACM-IEEE Eckert–Mauchly Award（2008）
- ACM Distinguished Service Award（2008）、SIGARCH/SIGOPS 服务奖、IFIP Jean-Claude Laprie Award（2012）、Richard A. Tapia Achievement Award（2016）
- Silicon Valley Engineering Hall of Fame
- 日本 Computer & Communication 奖（2005，与 Hennessy 共享）
- ACM Turing Award（2017，与 Hennessy 共享，2018-03-21 公布）
- BBVA Foundation Frontiers of Knowledge Award, ICT（2020）
- Charles Stark Draper Prize, NAE（2022，与 Hennessy/Furber/Wilson）

## 9. 机构清单

- 教育：South High School（Torrance, CA）、UCLA（BA 数学 1969 / MS 1970 / PhD CS 1976）
- 任职：UC Berkeley（1976 起教授近四十年；CS Division 主任；Pardee Professor Emeritus）、Google distinguished engineer（2016–）、RISC-V Foundation 董事会副主席、Laude Institute 董事会主席（2025–）
- 服务：ACM 主席（2004–06）、CRA 主席、美国总统 PITAC（2003–05）

## 10. 终审清单

- [ ] 生卒 1947-11-16 / 在世留白，出生地 Evergreen Park, IL
- [ ] 获奖理由整句引用无误（2017，与 Hennessy 共享，2018-03-21 公布）
- [ ] "coined the term RISC" 属本篇专属，表述准确
- [ ] Berkeley RISC 1980 项目 / RISC-I 1981 芯片年份不混
- [ ] RAID 1988 论文与 inexpensive/independent 全称语境正确
- [ ] UCLA BA 数学 1969 / PhD CS 1976，双导师 Martin & Estrin
- [ ] ACM 主席 2004–06、RISC-V Foundation vice chair
- [ ] Draper 2022 四人共享；Eckert–Mauchly 2008 归属正确
- [ ] 力量举/摔跤仅结尾彩蛋一笔带过
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | UC Berkeley · Google · RISC-V | Turing 2017`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2017/David Patterson (computer scientist)/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/David_A_Patterson_cropped_.jpg`（目录中唯一人像文件）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅 IEEE Milestone 铭文与奖项 citation，本人无直接引语勿编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Hennessy 篇格式对齐但内容分工不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
