# Fernando J. Corbató（费尔南多·科尔巴托）立传提示词

> qid=Q92625 · 1926-07-01 – 2019-07-12 · 西班牙裔美国计算机科学家 · 20/21 世纪 · 1990 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1990/Fernando J. Corbató/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`，西班牙裔），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（分时系统时间片轮转 / Corbató's Law 的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Fernando José "Corby" Corbató（中文惯称：费尔南多·科尔巴托，昵称 "Corby"）
- **生卒**：1926-07-01 生于 Oakland, California（美国）→ 2019-07-12 逝于 Newburyport, Massachusetts（美国），享年 93（死因：糖尿病并发症，complications from diabetes，页面明载）
- **国籍**：西班牙裔美国人（Spanish-American，页面明载）
- **身份**：计算机科学家，分时操作系统先驱
- **家庭**：父 Hermenegildo Corbató（西班牙 Villarreal 出身的西班牙文学教授）、母 Charlotte (Jensen) Corbató（丹麦裔美国人）；1930 年因父就职 UCLA 迁居 Los Angeles；1962 年与程序员 Isabel Blandford 结婚（1973 年去世）；续弦 Emily (née Gluck)；与 Isabel 育有二女 Carolyn Corbató Stone、Nancy Corbató，继子 David Gish、Jason Gish；弟 Charles；五位孙辈
- **教育轨迹**：
  - 1943 年入学 UCLA，一年级时因二战被海军（Navy）招募；战时"调试各种令人难以置信的设备"，启发其未来职业
  - 1946 年离开海军，入 California Institute of Technology，1950 年获**物理学**学士
  - MIT **物理学**博士（1956），论文 *A calculation of the energy bands of the graphite crystal by means of the tight-binding method*（紧束缚法计算石墨晶体能带）
- **博士导师**：John C. Slater（MIT 物理学家）
- **研究领域**：计算机科学（分时操作系统）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **分时系统先驱**：页面明载 "a pioneer in the development of time-sharing operating systems"——CTSS 与 Multics 两大系统的组织者与领军人。
2. **图灵奖（1990）**："for his pioneering work in organizing the concepts and leading the development of the general-purpose, large-scale, time-sharing and resource-sharing computer systems"——整句引用为获奖理由红线（关键词：organizing concepts + leading development + general-purpose, large-scale, time-sharing and resource-sharing）。
3. **CTSS（兼容分时系统）**：他参与的首个分时系统，MIT Compatible Time-Sharing System，早期版本 **1961 年演示**——一台计算机同时服务多个用户的范式由此确立。
4. **Multics**：CTSS 经验引出的第二个项目，被通用电气（GE，后并入 Honeywell）用于其高端计算机系统；首创多项现代操作系统概念：**层次文件系统、环形安全（ring-oriented security）、访问控制列表（ACL）、单级存储（single-level store）、动态链接、在线重配置**——逐条可列成表格页。
5. **Multics → Unix 的直接血脉**：页面明载 "Multics, while not particularly commercially successful in itself, directly inspired Ken Thompson to develop Unix"——商业上不算特别成功，但直接启发了 Unix，影响至今——"失败的系统孕育最成功的系统"叙事张力。
6. **第一个计算机密码**：Corbató 被公认首次在大计算机系统上用**密码**保护文件访问；但他本人后来称这种初级的安全方法"扩散后变得不可管理"——"密码之父的懊悔"叙事点。
7. **Corbató's Law**："The number of lines of code a programmer can write in a fixed period of time is the same, independent of the language used."（程序员在固定时间内能写出的代码行数与所用语言无关）——源头是其 1969 年 *PL/I As a Tool for System Programming*（"the number of debugged lines of source code per day is about the same!"）。
8. **物理学家出身**：加州理工物理学士（1950）→ MIT 物理博士（1956，石墨能带计算，导师 Slater）→ 毕业即加入 MIT Computation Center，1965 年任教授，留在 MIT 直至退休——从计算石墨能带到构建分时系统的转型叙事。
9. **二战海军岁月**：1943 年入学 UCLA 后因战争被海军招募，战时调试各种设备——"在设备调试中遇见计算机"的早年叙事。
10. **图灵奖演讲《On Building Systems That Will Fail》**（1991）——其获奖演讲标题本身即是名言级观点，可单独引用。
11. **荣誉**：Turing Award 1990、Computer History Museum Fellow 2012（"for his pioneering work on timesharing and the Multics operating system"）。
12. **门生**：Jerome H. Saltzer（infobox 实载；Multics 核心成员、MIT 著名教授）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（分时系统 — 蓝） | `#2E5A9E` | CTSS / 分时概念 |
| 分类色 2（操作系统遗产 — 青绿） | `#1E8E8E` | Multics / 层次文件系统 / ACL |
| 分类色 3（Unix 血脉 — 琥珀） | `#D9A441` | Multics → Unix → 现代操作系统 |
| 分类色 4（安全与人文 — 玫瑰） | `#C0395B` | 第一个密码 / Corbató's Law |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏的终端字符与时间片方块点缀（呼应"分时 / 命令行终端"视觉语言），克制使用。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：悠远 / 回望（分时系统的时代长镜、从 Multics 到 Unix 的历史纵深）
- **选定曲目**：**Mirage**（manifest 预分配，直接沿用）
- **落地文件**：`turing/presentations/Fernando_J._Corbató/Mirage.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「分时系统先驱 · 美国西班牙裔」+ Corbató 1926–2019 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1926–2019 生平纵览
4. **早年：西班牙文学教授之子**（1926–1946）：Oakland 出生、Villarreal 根脉、1930 迁洛杉矶、二战海军岁月
5. **从物理到计算**（1946–1956）：Caltech 物理学士 1950、MIT 物理博士 1956（石墨能带、导师 Slater）
6. **MIT Computation Center**（1956–）：毕业即入职、1965 年教授、终身 MIT
7. **CTSS：第一次分时**（1961）：Compatible Time-Sharing System、早期版本演示、多人共用一台计算机
8. **第一个计算机密码**：大系统文件访问的密码首创、本人晚年称其"变得不可管理"
9. **Multics：现代操作系统的摇篮**：层次文件系统 / 环形安全 / ACL / 单级存储 / 动态链接 / 在线重配置（表格页）
10. **Multics → Unix：失败的系统孕育成功**：GE → Honeywell 的产业轨迹、直接启发 Ken Thompson
11. **Corbató's Law 与图灵奖演讲**：代码行数定律、On Building Systems That Will Fail（1991）
12. **荣誉与传承**：Turing 1990、CHM Fellow 2012、门生 Saltzer
13. **学术著作一览**：CTSS Programmer's Guide 1963、Multics–The First Seven Years 1972 等
14. **遗产**：今天每一台多用户/多任务计算机里都有 CTSS 与 Multics 的基因
15. **结尾**：93 岁、"分时先驱与密码之父"的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由整句红线**："for his pioneering work in organizing the concepts and leading the development of the general-purpose, large-scale, time-sharing and resource-sharing computer systems"——勿简化成"发明了分时系统"。
- **生卒与死因**：1926-07-01 ~ 2019-07-12，享年 93；死因=糖尿病并发症（complications from diabetes，正文实载），勿编造其他死因。
- **国籍口径**：页面明载 "Spanish-American computer scientist"——写"西班牙裔美国人"；父辈根脉 Villarreal, Spain 可写，勿写"西班牙籍"。
- **CTSS 年份**：早期版本 **1961 年演示**（"an early version of which was demonstrated in 1961"）——勿写成"1961 年发明"或"1962 年"。
- **密码首创口径**："credited with the first use of passwords to secure access to files on a large computer system"——是**公认首创**（credited），且他本人后来批评其不可管理——保留"懊悔"语境；WSJ 采访标题引语（"Man Behind the First Computer Password: It's Become a Nightmare"）可用并标注出处。
- **Multics 商业成败**：页面明载 "not particularly commercially successful in itself, directly inspired Ken Thompson to develop Unix"——**必须保留"商业不算特别成功但启发 Unix"的对照**，勿写成纯成功故事；"失败"表述勿过头（页面用 not particularly commercially successful）。
- **学位口径**：Caltech 学位是**物理**（BS 1950）、MIT 博士也是**物理**（1956）——勿写成计算机/EE；infobox 另列 UCLA（1943 年入学、被海军招募中断，勿写成 UCLA 学位）。
- **博士导师**：John C. Slater（MIT 物理学家）——勿杜撰导师轶事。
- **Corbató's Law 出处**：原句出自 1969 年 *PL/I as a Tool for System Programming*（"Regardless of whether one is dealing with assembly language or compiler language, the number of debugged lines of source code per day is about the same!"）；流行版本是"The number of lines of code a programmer can write in a fixed period of time is the same, independent of the language used."——两版都可用但注明来历。
- **家庭**：两任婚姻、二女二继子、弟 Charles、五孙辈——页面实载，按实载一笔带过；Isabel Blandford 是**程序员**，1973 年去世（死因未载，勿编造）。
- **荣誉**：Turing 1990、CHM Fellow 2012——页面奖项仅此两项；NAE Memorial Tribute 存在但 infobox 无 NAE member 记录，勿写"NAE 院士"。
- **引语**：可用引语仅有——①战时 "debug[ged] an incredible array of equipment"（叙述转述）；②Corbató's Law 两版表述；③密码 "It's become a nightmare"（WSJ 采访转述）；④图灵奖演讲标题 On Building Systems That Will Fail。其余勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 科尔巴托（或 费尔南多·科尔巴托） | 待写入 |
| name_en | Fernando J. Corbató | 待写入 |
| birth_date | 1926-07-01 | 待写入 |
| death_date | 2019-07-12 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | operating systems / time-sharing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：John C. Slater（MIT 物理学家）
- **著名博士生**：Jerome H. Saltzer（Multics 核心成员、MIT 教授，infobox 实载唯一博士生）
- **启发的后辈**：Ken Thompson（Unix 作者，Multics 直接启发其开发 Unix——按单向影响关系处理，非师承）
- **配偶**：Isabel Blandford（1962 结婚，1973 去世，程序员）；Emily Gluck（续弦）
- **注**：Vyssotsky、Daggett、Clingen 等为论文合作者，如入库按 co-author 关系处理，勿写成师承

## 8. 奖项清单

- Turing Award（1990，"for his pioneering work in organizing the concepts and leading the development of the general-purpose, large-scale, time-sharing and resource-sharing computer systems"）
- Computer History Museum Fellow（2012，"for his pioneering work on timesharing and the Multics operating system"）

## 9. 机构清单

- 教育：UCLA（1943 年入学，因二战中断）、California Institute of Technology（物理 BS 1950）、Massachusetts Institute of Technology（物理 PhD 1956）
- 任职：美国海军（二战，1943–1946）、MIT Computation Center（1956 年起）、MIT 教授（1965 年起，直至退休）

## 10. 终审清单

- [ ] 生卒 1926-07-01 / 2019-07-12，享年 93，出生地 Oakland，去世地 Newburyport，死因糖尿病并发症
- [ ] 图灵奖 1990 理由整句（organizing concepts + leading development + time-sharing and resource-sharing）表述准确
- [ ] CTSS "1961 年早期版本演示"年份口径准确
- [ ] 密码首创为 credited 口径 + 本人"懊悔"语境保留
- [ ] Multics "商业不算特别成功 + 直接启发 Unix"对照表述准确
- [ ] 国籍「美国（西班牙裔）」，封面底部状态栏 `美国 | MIT · Caltech | Turing 1990`
- [ ] 学位口径：Caltech 物理 BS、MIT 物理 PhD（勿写成 CS/EE）
- [ ] Corbató's Law 出处（1969 PL/I 论文）标注准确
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1990/Fernando J. Corbató/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Fernando_Corbato.jpg`（取 `Fernando_Corbato.jpg` 大图版；小图版 `250px-Fernando_Corbato.jpg`）
- [ ] **国籍**：封面顶部徽章明示美国（西班牙裔可注小字）
- [ ] **引语核对**：引语必须能在 Wikipedia 原文找到（Corbató's Law / 密码懊悔 / 演讲标题）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同期图灵奖得主（Kahan / Milner）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
