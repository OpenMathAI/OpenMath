# John L. Hennessy（约翰·轩尼诗）立传提示词

> qid=Q92854 · 1952-09-22 生（在世留白） · 美国计算机科学家、斯坦福第 10 任校长、Alphabet 董事长 · 20/21 世纪 · 2017 图灵奖（与 Patterson 共享）
> 本地 Wikipedia 数据源：`turing/pages/2017/John L. Hennessy/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（RISC 指令集 / 定量分析方法 performance = f(指令数, CPI, 时钟) 的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Leroy Hennessy（中文惯称：约翰·轩尼诗/亨尼斯）
- **生卒**：1952-09-22 生于 Huntington, New York（美国）→ **在世留白**（页面无卒日，勿编造）
- **国籍**：美国（American）
- **身份**：计算机科学家；MIPS Technologies 与 Atheros 共同创始人；斯坦福大学第 10 任校长（2000–2016）；Alphabet 董事长（2018 起）
- **家庭**：六兄妹之一；父为航空工程师、母为教师（育儿前）；爱尔兰天主教移民后代（部分先祖于 19 世纪大饥荒期间抵美）；妻子 Andrea Berti（高中相识）——各一笔带过
- **教育轨迹**：
  - Villanova University **电机工程 BS**
  - Stony Brook University **计算机科学 MS + PhD**（1977），博士论文 *A real-time language for small processors: design, definition and implementation*
- **博士导师**：Richard Kieburtz（Stony Brook）
- **研究领域**：计算机体系结构（computer architecture）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **RISC 与定量体系结构学派**：与 Patterson 共获 2017 图灵奖，获奖理由（整句引用见 §5）：开创"系统化、定量的计算机体系结构设计与评估方法"，对微处理器产业影响深远；RISC 架构现已用于 **99% 的新芯片**（页面实载数字）。
2. **MIPS 项目（1981）**：在 Stanford 启动 MIPS 项目研究 RISC 处理器——**页面明载是"following preliminary investigations at Berkeley by David A. Patterson"**（跟随 Patterson 在 Berkeley 的先行研究）——两篇分工时注意此因果表述。
3. **学术创业：MIPS Computer Systems（1984）**：利用休假年（sabbatical）创办 MIPS Computer Systems Inc. 商业化研究成果；亦为 **Atheros** 共同创始人。
4. **教科书双雄（1988 起）**：1988 年与 Patterson 开始三年之功写成《Computer Architecture: A Quantitative Approach》第一版（描述 RISC 指令集与性能-成本权衡）；另有《Computer Organization and Design》——两书自 1990 年起广泛用于本科/研究生课程，引入 **DLX** 教学架构。
5. **斯坦福学术行政阶梯**：Stanford CS 系教师（1977 起）→ 计算机系统实验室 CSL 主任（1989–93）→ 计算机科学系主任（1994–96）→ 工学院院长（1996–99）→ **教务长 Provost（1999–2000，接 Condoleezza Rice）**→ **第 10 任校长（2000-09-01–2016-08-31）**，继任 Marc Tessier-Lavigne。
6. **1987 Bell 教席**：成为 Willard and Inez Kerr Bell Endowed Professor of EE+CS。
7. **Alphabet 董事长（2018-02）**：2018 年 2 月接替 Eric Schmidt 出任 Google 母公司 Alphabet 董事长；另有 Google、Cisco、Atheros、Moore Foundation 董事会经历——**有载可写**（任务提示核实）。
8. **Knight-Hennessy Scholars（2016）**：共同创办学者项目并任首任所长，**$750M** 捐赠全额资助研究生；首届 51 名学者来自 21 国（2018 秋入学）。
9. **"硅谷教父"**：Marc Andreessen 称其为 "the godfather of Silicon Valley"（页面实载引语）。
10. **MMIX**：为 Donald Knuth 的 TAOCP 更新模型机——把 MIX 更新为 **MMIX**（"Knuth's DLX equivalent"）——连接两位图灵奖得主的趣点。
11. **DASH/FLASH 多处理器**：1990 年代共享内存多处理器研究（directory-based cache coherence、memory consistency 论文；1989 cache 层次论文获 ISCA Influential Paper Award 2004）。
12. **荣誉**：Turing 2017、IEEE Medal of Honor 2012（"for pioneering the RISC processor architecture and for leadership in computer engineering and higher education"）、NAE 1992、NAS 2002、Draper Prize 2022（与 Patterson、Steve Furber、Sophie Wilson）、BBVA 2020、Clark Kerr Award 2020。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（RISC 与 MIPS — 蓝） | `#2E5A9E` | MIPS 项目 / MIPS Computer Systems |
| 分类色 2（定量方法 — 青绿） | `#1E8E8E` | Quantitative Approach / 性能评估 |
| 分类色 3（斯坦福校长 — 琥珀） | `#D9A441` | 校长十年 / Knight-Hennessy |
| 分类色 4（硅谷产业 — 玫瑰） | `#C0395B` | Atheros / Google/Alphabet 董事长 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：流水线节拍/阶梯块（稀疏水平条），呼应「指令流水线 + 学术行政阶梯」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：恢弘 / 传承（学术领袖与体系结构宗师）
- **选定曲目**：Alex-Productions **Awaken**（manifest 预分配，直接沿用），匹配"唤醒整个微处理器时代"的叙事。
- **落地文件**：`turing/presentations/John_L._Hennessy/Awaken.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「RISC 先驱 · 斯坦福第 10 任校长 · 美国」+ Hennessy 1952– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1952–至今 生平纵览
4. **纽约长岛少年**：六兄妹、航空工程师之父、爱尔兰移民后代、Villanova
5. **Stony Brook 博士**（1977）：Kieburtz 门下、实时语言
6. **Stanford 与 MIPS 项目**（1977–1984）：跟随 Berkeley 的先行研究、1984 休假年创业
7. **MIPS Computer Systems 与 Atheros**：学术创业双例
8. **定量方法与教科书革命**（1988）：与 Patterson 三年之功、DLX、MMIX（连接 Knuth）
9. **DASH/FLASH 与共享内存**：cache coherence、ISCA Influential Paper 2004
10. **斯坦福行政阶梯**：CSL 主任→系主任→工学院院长→教务长→校长
11. **校长十年（2000–2016）**：第 10 任、Knight-Hennessy Scholars $750M
12. **Alphabet 董事长**（2018）：董事会履历、"硅谷教父"（Andreessen 引语）
13. **荣誉大满贯**：Turing 2017 / IEEE MoH 2012 / NAS+NAE / Draper 2022 / BBVA 2020
14. **桃李**：Anant Agarwal、Norman Jouppi、Lawrence Paulson、Josep Torrellas
15. **结尾**：在世留白；"体系结构 + 教育 + 产业"三重遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **与 Patterson 共享结构**：2017 图灵奖两人共享。本篇侧重 Hennessy：MIPS/斯坦福/行政领袖/Alphabet；Patterson 篇侧重 RISC-I/RAID/Berkeley——教科书与定量方法两篇均可提，但叙事重心勿重复。
- **RISC 因果表述**：页面明载 MIPS 项目是 "following preliminary investigations at Berkeley by David A. Patterson"——写"MIPS 跟随 Berkeley 的先行探索"，**勿写 Hennessy 首创 RISC 概念**（"coined the term RISC" 在 Patterson 页面，属 Patterson）。
- **获奖理由（整句引用，核心红线）**：`"for pioneering a systematic, quantitative approach to the design and evaluation of computer architectures with enduring impact on the microprocessor industry"`（2017，与 Patterson 共享）。
- **Alphabet 董事长**：2018 年 2 月就任（页面实载 "chairman of Alphabet Inc." 于开头段）——有载可写，写明 2018；勿写 CEO。
- **校长任期**：2000-09-01 就任 / 2016-08-31 离任，是**第 10 任**校长；教务长 1999–2000 接 Rice——年份勿混。
- **MIPS 创业年份**：1981 项目 / **1984** 公司（页面原文 "On 1984"）——勿写 1983。
- **教科书分工**：《CAQA》1988 起三年写成第一版；《Computer Organization and Design》1994（Patterson-Hennessy 1994 页面实载）——两书名勿互串。
- **Draper Prize 2022**：与 Steve Furber、David Patterson、Sophie Wilson 四人共享（RISC 芯片）——勿写两人共享。
- **薪资条目**：2008 年薪酬超 $1M 居美国大学校长第 23 位——页面实载但属花边，建议不写或极简。
- **政治/宗教场合条目**：Dalai Lama 赠 khata（2010）、DREAM Act 联名社论（2010）页面实载——**建议禁写**（与主线无关且涉政治敏感，页面虽载但立传不必收录；若 Review 认为可留，仅客观一句）。
- **学位**：Villanova BS（电机）/ Stony Brook MS+PhD（CS，1977）——勿写成 Stanford 读博。
- **在世留白**：born 1952-09-22，写作 `1952–`。
- **可引语**：仅 "the godfather of Silicon Valley"（Andreessen 评语）与各奖项 citation；本人无直接引语，**勿编造**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 轩尼诗（或 约翰·轩尼诗） | 待写入 |
| name_en | John L. Hennessy | 待写入 |
| birth_date | 1952-09-22 | 待写入 |
| death_date | NULL（在世） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer architecture | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Richard Kieburtz（Stony Brook）
- **合作者**：David Patterson（教科书双雄、共享图灵/Draper/BBVA/日本 Computer & Communication 奖——Hennessy 页面实载 2005 年两人共享日本该奖）、Donald Knuth（MMIX 更新合作）
- **著名博士生**：Anant Agarwal、Lawrence Paulson、Josep Torrellas、Norman Jouppi
- **评语人物**：Marc Andreessen（"godfather of Silicon Valley"）
- **页面无载的关系**：勿补

## 8. 奖项清单

- National Academy of Engineering 院士（1992，RISC 创新 + 定量评估方法）
- IEEE Emanuel R. Piore Award（1994）
- ACM Fellow（1997）
- Golden Plate Award, American Academy of Achievement（2001）
- National Academy of Sciences 院士（2002）
- ACM SIGARCH ISCA Influential Paper Award（2004，1989 cache 层次论文）
- Computer History Museum Fellow（2007）
- IEEE Medal of Honor（2012）
- Honorary Degree in Mathematics, University of Waterloo（2012）
- Fellow of the Royal Academy of Engineering, FREng（2017）
- ACM Turing Award（2017，与 Patterson 共享）
- BBVA Foundation Frontiers of Knowledge Award, ICT（2020）
- Clark Kerr Award, UC Berkeley（2020）
- Charles Stark Draper Prize, NAE（2022，与 Furber/Patterson/Wilson）
- HKU honorary doctorate of science（2023）
- 日本 Computer & Communication 奖（2005，与 Patterson 共享）

## 9. 机构清单

- 教育：Villanova University（BS EE）、Stony Brook University（MS/PhD CS 1977）
- 任职：Stanford University（1977 起：CSL 主任 1989–93 → CS 系主任 1994–96 → 工学院院长 1996–99 → 教务长 1999–2000 → 第 10 任校长 2000–2016；1987 Bell 教席）
- 创办/董事：MIPS Computer Systems（1984）、Atheros、Knight-Hennessy Scholars（2016，首任所长）；Google/Alphabet（2018 起董事长）、Cisco、Gordon and Betty Moore Foundation 董事会

## 10. 终审清单

- [ ] 生卒 1952-09-22 / 在世留白，出生地 Huntington, NY
- [ ] 获奖理由整句引用无误（2017，与 Patterson 共享）
- [ ] Villanova / Stony Brook 1977 博士，导师 Kieburtz
- [ ] MIPS 项目 1981（跟随 Berkeley 先行研究）、公司 1984
- [ ] 校长第 10 任 2000–2016、教务长 1999–2000 年份准确
- [ ] Alphabet 董事长 2018 有载可写，勿写 CEO
- [ ] "coined RISC" 属 Patterson，本篇不写
- [ ] Draper 2022 四人共享
- [ ] Dalai Lama/DREAM Act 条目不写（或仅极简客观）
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Stanford · MIPS · Alphabet | Turing 2017`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2017/John L. Hennessy/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-John_L._Hennessy_by_Christopher_Michel_in_2024_01.jpg`（2024 肖像，取最大可用版）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅 "godfather of Silicon Valley" 与奖项 citation，本人无直接引语勿编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Patterson 篇格式对齐但内容分工不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
