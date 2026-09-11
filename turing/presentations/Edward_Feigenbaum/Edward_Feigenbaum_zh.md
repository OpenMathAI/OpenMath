# Edward Feigenbaum（爱德华·费根鲍姆）立传提示词

> qid=Q92823 · 1936-01-20 – 在世留白 · 美国计算机科学家（人工智能 / 专家系统）· 20 世纪 · 1994 图灵奖（与 Raj Reddy 共享）
> 本地 Wikipedia 数据源：`turing/pages/1994/Edward Feigenbaum/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（EPAM 学习模型 / 知识工程原则 / 专家系统架构的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Edward Albert Feigenbaum（中文惯称：爱德华·费根鲍姆；熟称 "Ed" Feigenbaum）
- **生卒**：1936-01-20 生于 Weehawken, New Jersey（美国）→ **在世留白**（页面明载 "born January 20, 1936"，无卒日）
- **国籍**：美国（American）
- **身份**：计算机科学家、人工智能先驱——**常被称为"专家系统之父"（"father of expert systems"，页面原文 often called）**
- **家庭**：文化意义上犹太家庭（culturally Jewish family）；16 岁离家上大学，此前住在 North Bergen；高中就读 Weehawken High School（因家乡无自己的中学，选其大学预科项目），1996 年入选该校名人堂
- **教育轨迹**：Carnegie Institute of Technology（今 Carnegie Mellon University）一步到位——1956 年本科毕业、1960 年 PhD（均为页面实载，本科专业页面未细载勿编造）
- **博士导师**：Herbert A. Simon（1978 诺贝尔经济学奖得主、AI 奠基人）；博士论文中开发 **EPAM**——最早的"人是如何学习的"计算机模型之一
- **研究领域**：计算机科学、人工智能、专家系统、知识工程

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1994 图灵奖（与 Raj Reddy 共享）**：获奖理由整句引用 "pioneering the design and construction of large scale artificial intelligence systems, demonstrating the practical importance and potential commercial impact of artificial intelligence technology"——表彰其**开创大规模 AI 系统的设计与构建，证明了 AI 技术的实际重要性与潜在商业影响**。**篇目侧重：专家系统 / 知识工程**（Reddy 篇侧重的语音识别/机器人不展开）。
2. **EPAM（博士论文，1960）**：Elementary Perceiver And Memorizer——最早的人脑学习计算机模型之一，与 Simon 合作的认知建模成果。
3. **Simon 引路人的两段轶事**（页面实载，可作叙事）：本科选修 James March 的 "Ideas and Social Change" 课被引荐给 Simon；在 Simon 的 "Mathematical Models in the Social Sciences" 课上听到 Simon 宣布 Logic Theorist——"Over the Christmas holidays, Al Newell and I invented a thinking machine."（Simon 原话）；Simon 给他一本 IBM 701 手册，他一夜读完，后称其为 "born-again experience"（"重生般的体验"）——这两处是页面可见的**直接引语**，可引用但须标注说话者。
4. **DENDRAL**：与 Joshua Lederberg 等在 Stanford 开创的分子结构推断专家系统（页面在 projects 中列 Dendral；Lederberg 的 "How DENDRAL was conceived and born" 为脚注来源）——首个大规模专家系统的代表。
5. **医学专家系统矩阵**：ACME、MYCIN、SUMEX——斯坦福医学 AI 系统群（页面实载四项目 DENDRAL/MYCIN/ACME/SUMEX，逐项列出即可，勿展开各自技术细节——页面无载）。
6. **知识工程与 Knowledge Systems Laboratory**：1965 年加入 Stanford 任教（**计算机科学系创建者之一**），1965–1968 任 Stanford 计算中心主任，创建 Knowledge Systems Laboratory——"知识工程"（knowledge engineering）作为领域的确立者。
7. **创业两连**：共同创办 **IntelliCorp** 与 **Teknowledge**——Teknowledge 1981 年 7 月由来自 Stanford/MIT/Rand 的 20 位计算机科学家创立，其员工"代表世界知识系统设计开发高层专长的约 1/3"（页面引文）；目标是让未经知识工程训练的人也能将该技术用于商业工业应用。
8. **《Computers and Thought》（1963，与 Julian Feldman 合编）**：**首部人工智能文集**（来源标题页脚注 "the First Anthology on Artificial Intelligence"，可写并标注）。
9. **《The Fifth Generation》（1983，与 Pamela McCorduck）**：关于日本第五代计算机挑战的畅销著作；另有《The Rise of the Expert Company》（1988）与《Handbook of Artificial Intelligence》四卷（与 Barr/Cohen 等）。
10. **执教与门生**：2000 年成为 Stanford 荣休教授；博士生含 **Niklaus Wirth**（Pascal 之父、1984 图灵奖得主——同奖谱系彩蛋）、Peter Karp、Alon Halevy、Ramanathan V. Guha。
11. **AAAI 2026 九十寿辰致敬**：2026 年 1 月 AAAI 第 40 届年会（新加坡）为庆祝其 90 岁生日致敬，表彰其对专家系统领域的奠基性贡献——**在世且活跃**的时间线收尾。
12. **美国空军渊源**：infobox 任职机构列 United States Air Force；1997 获美国空军 Exceptional Civilian Service Award（具体职务页面无载勿编造）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（专家系统 — 蓝） | `#2E5A9E` | DENDRAL / MYCIN / "专家系统之父" |
| 分类色 2（认知建模 — 青绿） | `#1E8E8E` | EPAM / Simon 门下 |
| 分类色 3（知识工程 — 琥珀） | `#D9A441` | Knowledge Systems Lab / Handbook of AI |
| 分类色 4（产业落地 — 玫瑰） | `#C0395B` | Teknowledge / IntelliCorp / The Fifth Generation |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：知识树节点网络（中心节点向外辐射的细线簇），呼应「知识库 + 推理机」的专家系统视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：开拓 / 落地（把 AI 从实验室带到产业的第一人）
- **选定曲目**：Alex-Productions **Pathfinder**（开拓 / 探路），匹配"知识工程开路先锋"的叙事（与 Dijkstra 同曲复用，属批次正常复用）。
- **落地文件**：`turing/presentations/Edward_Feigenbaum/Pathfinder.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「专家系统之父 · 美国」+ Feigenbaum 1936– + 右上头像（1994–1997 官方肖像）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1936– 生平纵览（Weehawken→Carnegie Tech→Berkeley→Stanford→AAAI 2026）
4. **新泽西少年与 Carnegie Tech（1936–1960）**：Weehawken/North Bergen、Hall of Fame 1996、Simon 引路人、"born-again experience"
5. **EPAM：机器如何学习（1960）**：博士论文、最早的认知学习模型之一
6. **Fulbright 与 Berkeley（1960–1965）**：英国 NPL Fulbright 访学、Berkeley 商学院执教
7. **Stanford：CS 系创建者（1965）**：CS 系创始成员之一、计算中心主任（1965–1968）
8. **DENDRAL：专家系统的开端**：与 Lederberg、分子结构推断——本篇核心页（公式框：知识 + 推理 = 专家系统）
9. **MYCIN / ACME / SUMEX：医学专家系统矩阵**：斯坦福医学 AI 群像
10. **知识工程与 Knowledge Systems Laboratory**：领域命名、知识库/推理机范式
11. **《Computers and Thought》与 AI 文献奠基**（1963）：首部 AI 文集 + Handbook 四卷
12. **产业远征：Teknowledge 与 IntelliCorp**：1981 创业、"1/3 世界专长"引文、The Fifth Generation
13. **荣誉与传承**：Turing 1994（与 Reddy）、NAE 1986、Feigenbaum Prize 2011、门生 Wirth/Karp/Halevy/Guha
14. **九秩寿辰（2026）**：AAAI 40 届年会致敬、专家系统遗产
15. **结尾**：品牌页 OpenMathAI

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享结构**：1994 与 Raj Reddy **共享**图灵奖，获奖理由两人共用同一句——**侧重区分**：Feigenbaum 篇 = 专家系统/知识工程/DENDRAL/MYCIN；Reddy 篇 = 语音识别/Hearsay/Sphinx/机器人。**禁写页面无载的两人合作/矛盾细节**（页面仅载两人 AAAI 2026 同框合影照片，勿编造其他交集）。
- **"专家系统之父"**：页面原文 "He is often called the 'father of expert systems'"——写"常被称为"，**勿写成定论式的唯一称号**。
- **MYCIN 等系统细节**：页面只列名字（ACME、MYCIN、SUMEX、Dendral）——**各自的技术细节、置信度因子、开发年份页面无载，禁写**。
- **Feigenbaum test**：infobox "Known for" 有 Feigenbaum test，但正文**无任何解释**——只能列名，勿展开定义（勿编造图灵测试变体细节）。
- **引语红线**：可用直接引语仅三条——①获奖理由整句；②Simon 的 "Over the Christmas holidays, Al Newell and I invented a thinking machine."（Simon 原话，非 Feigenbaum 语）；③Feigenbaum 自述 "born-again experience"（四词短语）。**其余勿编造**。
- **本科专业**：页面只载 "completed his undergraduate degree (1956)"，**未载专业**——勿写"计算机/工程学士"。
- **USAF 角色**：infobox 机构列 United States Air Force、1997 获其 Exceptional Civilian Service Award——**具体职务/年限页面无载勿编造**。
- **Teknowledge "1/3 专长"**：页面引文是公司员工自称（"represent about 1/3 of the world's high-level expertise..."）——引用时标注出处，勿写成客观事实断言。
- **《The Fifth Generation》**：写"1983 年与 McCorduck 合著、关于日本第五代计算机对世界的挑战"——**不评价其对日美竞争叙述的对错**，不渲染日美科技战。
- **生卒**：**在世**（1936-01-20 生，2026 年 AAAI 90 岁致敬可佐证）——时间线与结尾页写 `1936–`，勿写卒年。
- **荣誉**：Turing 1994、ACMI 初始 Fellow 1984、NAE 1986（理由：knowledge engineering 与专家系统技术的开创性贡献）、AAAI Fellow 1990、USAF 奖 1997、ACM Fellow 2007、AAAI 设立 Feigenbaum Prize 2011（两年一届）、IEEE Intelligent Systems AI's Hall of Fame 2011、Computer History Museum Fellow 2012、IEEE Computer Society Computer Pioneer Award 2013——**无** Nobel（勿因 Simon 师承而混写）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 费根鲍姆（或 爱德华·费根鲍姆） | 待写入 |
| name_en | Edward Feigenbaum | 待写入 |
| birth_date | 1936-01-20 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | artificial intelligence / expert systems / knowledge engineering | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Herbert A. Simon（Carnegie Tech/CMU，1978 图灵奖前的诺奖经济学得主；AI 导引者 James March 为间接引荐人，不入 relation）
- **合作者**：Julian Feldman（Computers and Thought 合编）、Joshua Lederberg（DENDRAL，诺贝尔生理学或医学奖得主——页面经脚注出现）、Pamela McCorduck（合著者）、Avron Barr / Paul R. Cohen（Handbook 合编）
- **著名博士生**：Niklaus Wirth（1984 图灵奖得主）、Peter Karp、Alon Halevy、Ramanathan V. Guha
- **同奖共享者**：Raj Reddy（1994 共同获奖人）
- 家庭关系页面无载——禁写。

## 8. 奖项清单

- ACM Turing Award（1994，与 Raj Reddy 共享）
- American College of Medical Informatics 初始 Fellow（1984）
- National Academy of Engineering 院士（1986）
- AAAI Fellow（1990）
- AAAI 设立 Feigenbaum Prize（2011，两年一届以其命名）
- IEEE Intelligent Systems AI's Hall of Fame（2011）
- Computer History Museum Fellow（2012）
- IEEE Computer Society Computer Pioneer Award（2013）
- ACM Fellow（2007）
- U.S. Air Force Exceptional Civilian Service Award（1997）
- Weehawken High School 名人堂（1996）

## 9. 机构清单

- 教育：Carnegie Institute of Technology / Carnegie Mellon University（本科 1956、PhD 1960）
- 任职：National Physical Laboratory (UK)（Fulbright 访学）、University of California, Berkeley 商学院（1960 起）、Stanford University（1965 起，CS 系创建者之一；计算中心主任 1965–1968；Knowledge Systems Laboratory 创建人；2000 荣休）、Teknowledge / IntelliCorp（共同创办）、United States Air Force（infobox 实载）

## 10. 终审清单

- [ ] 生卒 1936-01-20 / 在世留白，出生地 Weehawken, New Jersey
- [ ] 1994 与 Reddy 共享，获奖理由整句引用准确
- [ ] "常被称为专家系统之父"表述准确（不写唯一）
- [ ] EPAM = 博士论文成果、最早的认知学习模型之一
- [ ] DENDRAL/MYCIN/ACME/SUMEX 只列名，技术细节不展开
- [ ] Feigenbaum test 只列名不定义
- [ ] Computers and Thought = 首部 AI 文集（标注来源）
- [ ] 三条引语核对无误（获奖理由 / Simon 原话 / born-again）
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Carnegie Tech · UC Berkeley · Stanford | Turing 1994`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1994/Edward Feigenbaum/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-27._Dr._Edward_A._Feigenbaum_1994-1997.jpg`（官方肖像，最大可用版）；AAAI 2025 与 Reddy 同框照（`250px-AAAI_2025_-_Edward_Feigenbaum_Raj_Reddy_01_cropped_.jpg`）仅可作照片页插图并注明"与 Reddy 同框"，勿作主肖像
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（共三条，见 §5）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Hartmanis / Stearns / Reddy / Blum）格式对齐，尤其检查与 Reddy 篇的详略互补

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
