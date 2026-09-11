# Peter Naur（彼得·诺尔）立传提示词

> qid=Q92618 · 1928-10-25 – 2016-01-03 · 丹麦计算机科学家 · 20 世纪 · 2005 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2005/Peter Naur/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 丹麦`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（BNF 产生式 / ALGOL 60 报告要素的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Peter Naur（中文惯称：彼得·诺尔）
- **生卒**：1928-10-25 生于 Frederiksberg（丹麦）→ 2016-01-03 逝于 Herlev（丹麦），享年 87（死因：短期疾病 after a short illness，仅此一笔，勿渲染）
- **国籍**：丹麦（Danish）——**页面明载"唯一获图灵奖的丹麦人"（the only Dane to have won the Turing Award）**，可用
- **身份**：计算机科学先驱（computer science pioneer）
- **家庭**：配偶 Christiane Floyd（计算机科学家）；其余家庭细节页面未载，禁写
- **教育轨迹**：
  - University of Copenhagen（BS、MS、PhD 全部）
  - 职业起点是**天文学家**：1957 年获天文学博士学位，博士论文《Minor planet 51 Nemausa and the fundamental system of declinations》（小行星 51 Nemausa 与赤纬基本系统）
  - 与计算机的相遇使其转行——"his encounter with computers led to a change of profession"
- **博士导师**：页面未载（天文学阶段导师无名），禁写
- **研究领域**：计算机程序与算法的设计、结构、性能；软件工程与软件架构先驱；后转向认知与思维理论（Synapse-State Theory of Mental Life）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **ALGOL 60 报告编辑（1960）**：图灵奖核心——任 *Report on the Algorithmic Language ALGOL 60* 的 **editor**，该报告开创性地使用 BNF；1963 年又任 *Revised Report on the Algorithmic Language ALGOL 60* 编辑。获奖理由即"定义 ALGOL 60 的工作，尤其是作为该报告编辑的角色"。
2. **BNF（Backus–Naur form）**：与 John Backus 一道被铭记于 BNF 之名——但注意 §5 红线：**Naur 本人不喜欢这一命名**。
3. **IFIP Working Group 2.1 成员**：该工作组负责 specification、支持与维护 ALGOL 60 与 ALGOL 68。
4. **Regnecentralen 十年（1959–1969）**：丹麦计算公司 Regnecentralen 任职，同时在 Niels Bohr Institute 与丹麦技术大学（Technical University of Denmark）讲学。
5. **哥本哈根大学教授（1969–1998）**：任计算机科学教授近 30 年；与 Regnecentralen 时期一道发展出"哥本哈根传统"（Copenhagen Tradition of Computer Science）——与实际应用及其他知识领域紧密联系、课程中大量项目实践。
6. **datalogy 之父**：不喜欢 "computer science" 一词，倡议改称 **datalogy**（丹麦与瑞典采纳为 datalogi）或 data science；自 1960 年代中期起丹麦的学科实践即以其术语展开。
7. **反形式主义立场**：在 *Computing: A Human Activity*（1992，其计算机科学贡献文集）中**拒绝把编程视为数学分支的形式主义学派**。
8. **经验主义与思维理论**：晚期可归入经验主义（empiricist）学派——主张只依据可观察事实、不寻求事物间更深层的联系；由此批评哲学与心理学的某些流派；提出"心智生活的突触-状态理论"（Synapse-State Theory of Mental Life）。
9. **BIT 期刊编委（1960–1993）**：数值分析期刊 *BIT Numerical Mathematics* 编委 33 年。
10. **软件工程会议（1968 Garmisch）**：与 Brian Randell、J.N. Buxton 合编 *The Conference on Software Engineering, 7–11 October 1968*（Garmisch 会议文献）——软件工程先驱的一环。
11. **《Programming as Theory Building》（1985）**：页面参考文献载此论文标题（仅标题层面有载，正文未展开其内容——写作时勿虚构其论点细节，只可点出"编程即理论构建"的标题主张）。
12. **荣誉**：Turing Award 2005（ACM，"for his work on defining the programming language ALGOL 60"）、IEEE Computer Society Computer Pioneer Award 1986。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（程序语言 — 蓝） | `#2E5A9E` | ALGOL 60 / IFIP WG 2.1 |
| 分类色 2（语法记法 — 青绿） | `#1E8E8E` | BNF / 报告编辑 |
| 分类色 3（软件工程 — 琥珀） | `#D9A441` | Garmisch 会议 / Theory Building |
| 分类色 4（datalogy 与认知 — 玫瑰） | `#C0395B` | datalogy / Synapse-State 理论 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：细线语法网络（稀疏节点连线），呼应「BNF 产生式 / ALGOL 语法定义」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：沉静 / 学人本色（天文学家转行的定义者、反形式主义的坚持者）
- **选定曲目**：Alex-Productions **Last Hope**（manifest 预分配，直接沿用），匹配"从星空到程序语言"的沉静叙事。
- **落地文件**：`turing/presentations/Peter_Naur/LastHope.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「ALGOL 60 定义者 · 丹麦」+ 诺尔 1928–2016 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1928–2016 生平纵览
4. **早年：哥本哈根的天文学家**（1928–1957）：Frederiksberg 出生、哥本哈根大学 BS/MS/PhD、小行星 51 Nemausa 博士论文
5. **转行：与计算机相遇**（1957–1959）：天文学 PhD 之后改换行业
6. **Regnecentralen 十年**（1959–1969）：丹麦计算公司、Niels Bohr Institute 与 DTU 讲学
7. **ALGOL 60 报告**（1960）：editor 角色、开创性使用 BNF、1963 修订报告
8. **BNF：被冠名的遗憾**：与 Backus 并名、Naur 更愿称 "Backus normal form"、Knuth 归名
9. **IFIP WG 2.1 与 BIT 编委**：ALGOL 60/68 的维护者、BIT 编委 1960–1993
10. **datalogy：为学科命名**：反对 "computer science" 术语、丹麦/瑞典采纳 datalogi、哥本哈根传统
11. **反形式主义与《Computing: A Human Activity》**（1992）：拒绝编程=数学的形式主义学派
12. **经验主义与思维理论**：empiricist 立场、Synapse-State Theory of Mental Life
13. **《Programming as Theory Building》与 Garmisch**：1985 论文（仅标题层面）、1968 软件工程会议文献合编
14. **荣誉与传承**：Turing 2005、Computer Pioneer Award 1986、唯一丹麦裔图灵奖得主
15. **结尾**：87 岁、天文学家出身的语言定义者的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：`for his work on defining the programming language ALGOL 60. In particular, his role as editor of the influential Report on the Algorithmic Language ALGOL 60 with its pioneering use of BNF was recognized.`（页面原文）——核心是**报告编辑角色**，勿写成"发明 BNF"或"设计 ALGOL 语言"。
- **BNF 命名红线**：BNF 的 "N"（Naur）之名是 **Donald Knuth 归名**的结果；**Naur 本人不喜欢与 BNF 关联，更愿称 "Backus normal form"**——这一态度是页面实载，必须保留，勿写成"以他命名是他的荣誉"式正面叙述。
- **"唯一丹麦人"**：`Naur is the only Dane to have won the Turing Award` 页面明载，可用；但仅限"丹麦人"口径，勿延伸为"北欧唯一"。
- **职业起点是天文学**：PhD（1957）是天文学博士（小行星 51 Nemausa 论文），计算机是转行——勿写成"计算机科班出身"。
- **《Programming as Theory Building》**：仅在页面**参考文献**中出现（1985），正文无内容展开——只写标题与年份，**勿虚构论文论点**。
- **与 Backus 关系**：页面实载仅有——ALGOL 60 报告共同署名（Backus 名列编辑名单之首）、BNF 并名、Naur 愿称 "Backus normal form"；**任何"师承/密切合作/恩怨"细节页面无载，禁写**。
- **ALGOL 60 报告编辑名单**：Backus, Wegstein, van Wijngaarden, Woodger, Bauer, Green, Katz, McCarthy, Perlis, Rutishauser, Samelson, Vauquois（Naur 任 editor）——引用名单时以此为准，勿遗漏或添加。
- **datalogy vs data science**：Naur 倡议的两个术语都要交代——datalogy 被丹麦/瑞典采纳（datalogi）；data science 后来指数据分析了——勿把 data science 写成现代数据科学运动的先驱宣言。
- **配偶**：Christiane Floyd 是计算机科学家、Naur 配偶——页面实载可写；其余家庭细节禁写。
- **去世**：2016-01-03，Herlev，87 岁，`after a short illness`（短期疾病）——仅此一笔，勿编造具体病名。
- **教育**：BS/MS/PhD 均为 University of Copenhagen（infobox）；年份页面只载 PhD 1957——本硕年份勿编。
- **荣誉**：仅 Computer Pioneer Award（1986）与 Turing Award（2005）页面实载；**无**其他奖章（勿编造）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 彼得·诺尔（或 诺尔） | 待写入 |
| name_en | Peter Naur | 待写入 |
| birth_date | 1928-10-25 | 待写入 |
| death_date | 2016-01-03 | 待写入 |
| nationality | Denmark | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / informatics / programming languages / software engineering | 待写入 |
| has_biography | 1 | 入库时置 1 |

## 7. 社会关系入库清单

- **合作者（ALGOL 60 报告共同署名）**：John Backus、J.H. Wegstein、A. van Wijngaarden、M. Woodger、F.L. Bauer、J. Green、C. Katz、John McCarthy、A.J. Perlis、H. Rutishauser、K. Samelson、B. Vauquois（Naur 任 editor）
- **配偶**：Christiane Floyd（computer scientist，type=spouse）
- **编务合作**：Brian Randell、J.N. Buxton（1968 Garmisch 软件工程会议文献合编者）
- **博士导师**：页面无载禁写（天文学阶段导师无名）

## 8. 奖项清单

- Turing Award（2005，"for his work on defining the programming language ALGOL 60"）
- IEEE Computer Society Computer Pioneer Award（1986）

## 9. 机构清单

- 教育：University of Copenhagen（BS、MS；PhD 1957，天文学，论文《Minor planet 51 Nemausa and the fundamental system of declinations》）
- 任职：Regnecentralen（1959–1969，丹麦计算公司）；Niels Bohr Institute 与 Technical University of Denmark 兼职讲学（与 Regnecentralen 时期并行）；University of Copenhagen 计算机科学教授（1969–1998）；*BIT Numerical Mathematics* 编委（1960–1993）；IFIP Working Group 2.1 成员

## 10. 终审清单

- [ ] 生卒 1928-10-25 / 2016-01-03，享年 87，出生地 Frederiksberg，去世地 Herlev，死因"短期疾病"
- [ ] 图灵奖理由整句引用（defining ALGOL 60 + editor of the Report），不写成"发明 BNF"
- [ ] BNF 命名态度：Knuth 归名、Naur 愿称 "Backus normal form"——必写
- [ ] "唯一获图灵奖的丹麦人"表述准确（仅丹麦口径）
- [ ] 天文学博士（1957，51 Nemausa）为职业起点，计算机为转行
- [ ] Regnecentralen 1959–1969、哥本哈根教授 1969–1998 年份准确
- [ ] 《Programming as Theory Building》仅写标题与 1985 年份，不展开内容
- [ ] datalogy 与 data science 两个术语的后续走向不混淆
- [ ] 国籍用「丹麦」，封面底部状态栏 `丹麦 | Regnecentralen · Copenhagen | Turing 2005`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2005/Peter Naur/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2008 年肖像（`images/500px-Peternaur.JPG`，页面明注 "Naur in 2008"，图注如实写）
- [ ] **国籍**：封面顶部徽章明示丹麦
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（本篇正文无直接引语，勿编造；获奖理由为页面转述可整句引用）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2005–2007 批次（Allen / Clarke / Emerson / Sifakis）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
