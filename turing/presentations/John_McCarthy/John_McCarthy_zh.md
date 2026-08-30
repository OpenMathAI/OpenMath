# John McCarthy（约翰·麦卡锡）立传提示词

> qid=— · 1927-09-04 – 2011-10-24 · 美国计算机科学家、认知科学家 · 20 世纪 · 1971 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1971/John McCarthy (computer scientist)/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Lisp 的 S-表达式 / 条件表达式 / lambda 记号 / 递归定义），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John McCarthy（中文惯称：约翰·麦卡锡）
- **生卒**：1927-09-04 生于波士顿（Boston, Massachusetts，美国）→ 2011-10-24 逝于斯坦福（Stanford, California），享年 84（未详述死因）
- **国籍**：美国（American）
- **身份**：计算机科学家、认知科学家（AI 奠基人之一）
- **家庭**：父 John Patrick McCarthy（爱尔兰移民，来自 Kerry 郡 Cromane 渔村）、母 Ida Glatt（立陶宛犹太移民）；父母 1930 年代均为美国共产党积极分子，鼓励学习与批判性思考；三任妻子——Martha Coyote、Vera Watson（程序员+登山家，1978 年登 Annapurna 遇难）、Carolyn Talcott（计算机科学家，SRI）
- **教育轨迹**：
  - 中学：Belmont High School（洛杉矶），提前两年毕业；1944 年入 Caltech
  - Caltech 数学 BS（1948）——少年自学大学数学，跳过前两年；因未上体育课被停学，后入伍（US Army）再返校
  - Princeton 数学 PhD（1951）——论文《Projection operators and partial differential equations》
- **博士导师**：Donald C. Spencer（Princeton 数学家）
- **早年关键**：Caltech 时期听 John von Neumann 讲座，激发其学术志向
- **研究领域**：人工智能、编程语言（Lisp）、逻辑与知识表示、分时系统

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **"AI 之父"之一**：与 Alan Turing、Marvin Minsky、Allen Newell、Herbert A. Simon 并列为 AI 奠基人（"founding fathers"）。
2. **创造 "artificial intelligence" 一词（1956）**：与 Minsky、Nathaniel Rochester、Claude E. Shannon 共同撰写 Dartmouth 会议（达特茅斯会议）提案，首次使用并命名"人工智能"——该会议开创了 AI 这一领域。
3. **Lisp 语言（1958 发现，1960 发表）**：发现原始递归函数可扩展以计算符号表达式，由此创立 Lisp——第二个高级编程语言（Fortran 之后），函数式编程先驱，引入 lambda 记号（借自 λ 演算），后启发 Scheme。
4. **Advice Taker（1958）**：提出 Advice Taker 构想，启发后来的问答系统与逻辑编程。
5. **垃圾回收（约 1959）**：为解决 Lisp 内存问题发明垃圾回收（自动内存管理）。
6. **ALGOL 60 贡献（1959）**：提议递归与条件表达式，成为 ALGOL 的一部分；后参与 IFIP WG 2.1 国际标准制定。
7. **分时系统（time-sharing）**：参与最早三个分时系统（CTSS、BBN、Dartmouth）的创建；Lester Earnest 评价"没有 McCarthy 开创分时，互联网不会那么早到来"——分时即今之服务器/云计算。
8. **Utility computing（1961）**：MIT 百年校庆演讲中首次公开提出"效用计算"（计算力像水电一样按需出售）——云计算思想的先驱。
9. **Project MAC 与 Stanford AI Lab**：MIT 期间推动 Project MAC 创立；斯坦福期间建立 Stanford AI Laboratory，与 Project MAC 多年良性竞争。
10. **国际象棋程序（1966）**：与团队开发 Kotok-McCarthy 象棋程序，与苏联棋手程序对弈（两负两和）。
11. **Circumscription（1978–1986）**：发展非单调推理的限定法（circumscription），处理常识推理。
12. **情境演算（situation calculus）**：提出情境演算框架，为形式化动作与变化奠基。
13. **哲学与世界观**：AI 乐观主义者、逻辑派 AI 代表；1979 年《Ascribing Mental Qualities to Machines》引发 John Searle"中文屋"争论；与 Hubert Dreyfus 长期论战；名言"拒绝做算术的人注定胡言乱语"（"He who refuses to do arithmetic is doomed to talk nonsense"）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（人工智能 — 蓝） | `#2E5A9E` | AI 奠基 / Dartmouth 会议 |
| 分类色 2（Lisp 语言 — 青绿） | `#1E8E8E` | Lisp / 函数式编程 |
| 分类色 3（分时系统 — 琥珀） | `#D9A441` | time-sharing / 云计算先驱 |
| 分类色 4（逻辑与知识 — 玫瑰） | `#C0395B` | circumscription / situation calculus |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「符号 / 递归 / 智能」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：史诗 / 奠基 / 革命（AI 之父、Lisp 创造者）
- **选定曲目**：Alex-Productions **New Lands**（史诗 / 开阔），与 Knuth / Minsky 同曲，匹配"创造人工智能"这一改写计算机史的开创叙事。
- **落地文件**：`turing/presentations/John_McCarthy/NewLands.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 之父 · 美国」+ 麦卡锡 1927–2011 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1927–2011 生平纵览
4. **早年：波士顿与 Caltech**（1927–1948）：移民家庭、von Neumann 讲座、数学神童、休学入伍
5. **Princeton 博士与 AI 的召唤**（1948–1951）：Spencer 门下、数学博士论文
6. **Dartmouth 会议：命名"人工智能"**（1956）：与 Minsky/Rochester/Shannon 共创 AI 一词
7. **Lisp 的诞生**（1958）：符号表达式、函数式编程、lambda 记号（公式框：S-表达式 / 条件表达式）
8. **垃圾回收与 ALGOL**（1959）：自动内存管理、递归与条件表达式
9. **分时系统与效用计算**（1959–1961）：CTSS/BBN/Dartmouth、云计算思想先驱
10. **MIT 与斯坦福：Project MAC 与 SAIL**（1958–1962）
11. **逻辑 AI：Circumscription 与情境演算**（1978–1986）：非单调推理、形式化常识
12. **哲学与论战**：逻辑派 AI、中文屋争论、与 Dreyfus 论战
13. **荣誉与传承**：Turing 1971、门生 Liskov/Reddy、30 名博士生
14. **遗产**：AI、Lisp、分时、云计算的思想源头
15. **结尾**：84 岁、"AI 之父"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **"AI 之父"表述**：与 Turing、Minsky、Newell、Simon 并列为 "founding fathers"，是**之一**，勿写"唯一之父"。
- **"人工智能"一词归属**：1956 Dartmouth 会议提案由 McCarthy、Minsky、Rochester、Shannon **四人共同**撰写，McCarthy 是发起人与主导者——表述为"与 Minsky 等人共同创造"，勿写"独自创造"。
- **Lisp 发表年份**：1958 年发现/提出，**1960 年正式发表**（论文《Recursive Functions of Symbolic Expressions and Their Computation by Machine》）；勿写"1958 年发表"。
- **Lisp 的地位**：是**第二个**高级编程语言（Fortran 1957 之后），勿写"第一个"。
- **垃圾回收**：约 1959 年发明，为**解决 Lisp 内存问题**；表述为"发明垃圾回收"时注明这是自动内存管理。
- **分时系统**：参与创建最早**三个**（CTSS、BBN、Dartmouth），是**先驱之一**，勿写"独自发明分时"。
- **效用计算**：1961 年 MIT 百年校庆演讲首次**公开提议**效用计算；"首次"可谨慎使用，但应表述为"最早公开提出者之一"。
- **博士**：1951 年 Princeton **数学**博士（导师 Spencer），论文是偏微分方程——**非计算机科学**（当时无 CS 博士）。
- **本科停学**：因**未上体育课**被 Caltech 停学，后入伍（US Army）再返校——轶事可提，勿写"被开除"。
- **政治立场**：出身共产主义家庭，后因 1968 年访问捷克斯洛伐克（苏联入侵后）转为**保守派共和党人**；无神论者——属个人背景，谨慎表述。
- **中文屋争论**：1979 年论文引发 John Searle 1980 年"中文屋"反驳——是**论战**，勿写成"McCarthy 被证明错误"。
- **死亡**：2011-10-24 逝于斯坦福家中，享年 84；文中未详述死因，勿编造。
- **图灵奖理由**：1971 年图灵奖表彰其对 AI 领域的贡献，官网表述为 "for his major contributions to the field of Artificial Intelligence"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q92739（John McCarthy, computer scientist） | 待核对 |
| name_zh | 麦卡锡（或 约翰·麦卡锡） | 待写入 |
| name_en | John McCarthy | 待写入 |
| birth_date | 1927-09-04 | 待写入 |
| death_date | 2011-10-24 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | artificial intelligence / programming languages / logic | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Donald C. Spencer（Princeton 数学家）
- **AI 之父同仁**：Marvin Minsky、Claude E. Shannon、Nathaniel Rochester（Dartmouth 会议共同提案）
- **著名博士生**：Barbara Liskov（2008 图灵奖得主）、Raj Reddy（1994 图灵奖得主）、Ruzena Bajcsy、Hans Moravec、Ramanathan V. Guha 等（共指导 30 名博士生）
- **同事/合作**：Lester Earnest（Stanford AI Lab）、Seymour Papert、John von Neumann（早年讲座启发）
- **论战对手**：John Searle（中文屋）、Hubert Dreyfus（AI 怀疑论）

## 8. 奖项清单

- Turing Award（1971，图灵奖）
- Computer Pioneer Award（1985）
- IJCAI Award for Research Excellence（1985）
- Kyoto Prize（1988，京都奖）
- National Medal of Science（1990，美国国家科学奖章）
- Computer History Museum Fellow（1999）
- Benjamin Franklin Medal（2003，富兰克林奖章）

## 9. 机构清单

- 教育：California Institute of Technology（BS 数学 1948）、Princeton University（PhD 数学 1951）
- 任职：Dartmouth College（助理教授 1955）、MIT（research fellow 1956–1962）、Stanford University（正教授 1962–2000，退休）

## 10. 终审清单

- [ ] 生卒 1927-09-04 / 2011-10-24，享年 84，出生地 Boston，去世地 Stanford
- [ ] "AI 之父"表述为"之一"，与 Turing/Minsky/Newell/Simon 并列
- [ ] "人工智能"一词为 1956 Dartmouth 会议四人共同提案
- [ ] Lisp"1958 提出、1960 发表"表述准确，且是"第二个"高级语言
- [ ] 博士"Princeton 数学、Spencer 导师"表述准确
- [ ] 分时系统"三个之一、先驱"表述准确
- [ ] 效用计算"1961 最早公开提议之一"表述准确
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | MIT · Stanford | Turing 1971`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1971/John McCarthy (computer scientist)/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Stanford 肖像（images 中 250px-John_McCarthy_Stanford.jpg）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如"拒绝做算术的人注定胡言乱语"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Knuth 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（Minsky / Knuth）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
