# Herbert A. Simon（赫伯特·西蒙）立传提示词

> qid=Q181529 · 1916-06-15 – 2001-02-09 · 美国学者（经济学/计算机科学/认知心理学） · 20 世纪 · 1975 图灵奖（与 Allen Newell 共享）· 1978 诺贝尔经济学奖
> 本地 Wikipedia 数据源：`turing/pages/1975/Herbert A. Simon/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（有限理性 / 满意化 / 满意化-最优化对比的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Herbert Alexander Simon（中文惯称：赫伯特·亚历山大·西蒙；注意勿与 NBA Indiana Pacers 老板 Herbert Simon 混淆，页面明示消歧）
- **生卒**：1916-06-15 生于密尔沃基（Milwaukee, Wisconsin）→ 2001-02-09 逝于匹兹堡（Pittsburgh, Pennsylvania），享年 84；2001-01 在 UPMC Presbyterian 手术切除腹部肿瘤，**术后并发症去世**（死因页面实载，可写"术后并发症"）
- **国籍**：美国（American）
- **身份**：学者——横跨计算机科学、经济学、认知心理学、政治科学、公共管理（"American scholar"）
- **家庭**：父 Arthur Simon（1881–1948，德国 Darmstadt 出身的犹太电气工程师、发明家、专利律师，1903 年赴美）；母 Edna Marguerite Merkel（1888–1969，钢琴家）；舅舅 Harold Merkel（1892–1922，其经济学启蒙）；配偶 Dorothea Isabel Pye（**婚年存疑：正文写 1938，infobox 写 m. 1939**——见 §5）；子女 3 人（Katherine、Peter、Barbara）
- **教育轨迹**：University of Chicago——BA（1936）、MA（infobox 载）、PhD（1943），均为**政治科学**（PhD 论文主题：组织决策）
- **博士导师**：Henry Schultz（计量经济学家）；其他学术指导：Rudolf Carnap、Nicholas Rashevsky、Harold Lasswell、Charles Merriam、John R. Commons（影响）
- **研究领域**：决策（decision-making，一生主线）、组织理论、有限理性、人工智能、认知心理学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1975 图灵奖（与 Newell 共享）**：ACM citation 整句——"In joint scientific efforts extending over twenty years, initially in collaboration with J.C. (Cliff) Shaw at the RAND Corporation, and subsequentially [sic] with numerous faculty and student colleagues at Carnegie Mellon University, they have made basic contributions to artificial intelligence, the psychology of human cognition, and list processing."（**本篇核心红线引文**）
2. **1978 诺贝尔经济学奖**（Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel）："for his pioneering research into the decision-making process within economic organizations"（对经济组织内部决策过程的开创性研究）——图灵奖+诺奖双冠是其最大叙事差异点。
3. **有限理性（bounded rationality）与满意化（satisficing）**：与 "homo economicus" 对抗——备选与后果只能部分知晓，人只能"足够好"而非最优；这是**行为经济学**的核心主题；他区分"程序性理性"（procedural，心理学家）与"实质性理性"（substantive，经济学家）。
4. **《Administrative Behavior》（1947）**：基于博士论文、一生工作的基石——决策的正确性 = 达成目标的充分性 + 获得结果的效率；组织中的权威与忠诚/认同两要素。
5. **密尔沃基少年**：中学即写信给 Milwaukee Journal 为无神论者的公民自由辩护；辩论队中"from conviction"为 George 的**单一税（single tax / Georgism）**辩护——1979 年仍主张以土地价值税取代工资税。
6. **芝加哥教育**：1933 入学；因**色盲与实验室笨拙**放弃生物；受 Schultz 最深；1936 BA / 1943 PhD（其间 1939–1942 在 UC Berkeley 任运筹组主任、通信答辩）。
7. **CMU 五十二年（1949–2001）**：1949 入 Carnegie Tech 任工业管理系教授兼系主任；1967 年校名改为 Carnegie-Mellon University；后兼授心理学与计算机科学；**帮助创建 CMU 计算机学院**（世界最早的计算机学院之一）。
8. **与 Newell 共创 AI**：Logic Theory Machine（1956）、GPS（1957）、IPL（1956，与 Newell/Shaw）——Knuth 记载 IPL 的 list processing 发展出 linked list，原名 **"NSS memory"**（以三发明者命名）。
9. **心理学线**：与 Feigenbaum 提出 **EPAM**（最早实现为程序的学习理论之一）；与 Ericsson 发展**口头协议分析**（verbal protocol analysis）；专长 = 约 10 年经验 + 约 50,000 chunks（国际象棋专家习得约 50,000 个棋局模式）；与 Gobet 扩展为 CHREST 模型。
10. **经济学的其他贡献**：与 David Hawkins 发现证明 **Hawkins–Simon 定理**（投入产出矩阵正解存在条件）；1955 "A Behavioral Model of Rational Choice"；与 James G. March 合著 *Organizations*（1958，现代组织理论奠基）；早期分析**复杂性的架构**并提出**优先连接（preferential attachment）**机制解释幂律分布。
11. **AI 预言（正反都要写）**：1957 预言计算机国际象棋十年内超越人类（实际用了约四十年）；1965 预言 "machines will be capable, within twenty years, of doing any work a man can do"——作为"乐观误判"如实呈现，勿粉饰。
12. **人情味**：钢琴家、登山爱好者、开过一门法国大革命本科课；27 本书、近千篇论文；截至 2016 年是 Google Scholar 上 AI 与认知心理学领域**被引最多**的人。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 / 诺贝尔奖 |
| 分类色 1（决策与经济学 — 蓝） | `#2E5A9E` | 有限理性 / Administrative Behavior / 诺贝尔奖 |
| 分类色 2（人工智能 — 青绿） | `#1E8E8E` | Logic Theorist / GPS / IPL |
| 分类色 3（认知心理学 — 琥珀） | `#D9A441` | EPAM / 口头协议分析 / 50,000 chunks |
| 分类色 4（组织理论 — 玫瑰） | `#C0395B` | Organizations / 复杂性架构 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和棋盘格淡纹理（稀疏方块），呼应「满意化 vs 最优化的抉择 / 棋盘 chunks」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：沉思 / 跨界（经济学-心理学-AI 三栖的广度与深度）
- **选定曲目**：Alex-Productions **SEA**（manifest 预分配，直接沿用），匹配"在知识的海洋中跨界航行"的叙事。
- **落地文件**：`turing/presentations/Herbert_A._Simon/SEA.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「图灵奖 + 诺贝尔奖双冠 · 美国」+ 西蒙 1916–2001 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1916–2001 生平纵览
4. **密尔沃基的少年**（1916–1933）：电气工程师之子、无神论信件、单一税辩论
5. **芝加哥岁月**（1933–1943）：色盲弃生物、Schultz 门下、1936 BA / 1943 PhD
6. **Berkeley 与 IIT**（1939–1949）：运筹组主任、Cowles Commission、Hawkins–Simon 定理（1950s）
7. **《Administrative Behavior》**（1947）：决策正确性的双标准、权威与认同
8. **有限理性与满意化**（bounded rationality / satisficing）：对抗 homo economicus
9. **CMU 五十二年**（1949–2001）：工业管理系、帮助创建计算机学院
10. **与 Newell 共创 AI**：Logic Theorist / GPS / IPL / NSS memory
11. **Human Problem Solving（1972）与 EPAM**：口头协议分析、50,000 chunks
12. **1978 诺贝尔经济学奖**：组织决策研究的加冕
13. **预言家与误判**：1957 十年象棋、1965 二十年通用机器——如实呈现
14. **荣誉与传承**：27 部著作、千篇论文、门生成林（Feigenbaum/Newell/Williamson/Muth/Korf 等）
15. **结尾**：84 岁、图灵奖+诺奖双冠的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享奖结构**：1975 图灵奖与 **Allen Newell 共享**，必须写明；本篇侧重**有限理性/决策/诺贝尔经济学奖**，AI 部分点到 IPL/LT/GPS 与 Newell 篇区分；**禁写**页面无载的两人恩怨（页面叙事是长达二十余年的联合科学努力）。
- **婚年冲突**：正文 "Simon married Dorothea Pye in 1938" vs infobox "m. 1939"——**以正文为准（1938）并在提示词与 Review 中标注存疑**，或回避具体年份写"与 Dorothea Pye 结婚，婚姻持续 63 年至其去世"。
- **诺贝尔奖名称**：官方为 "Nobel Memorial Prize in Economic Sciences"（瑞典央行纪念阿尔弗雷德·诺贝尔经济学奖），页面明写 "Nobel Prize in Economics" 的口语用法可并用，首次出现用全称。
- **图灵奖 citation 引文**：整句引用时注意原文有 "[sic]"（subsequential 拼写）——中文页可忠实引用英文原文，勿"顺手改正"。
- **AI 预言**：1957"十年内象棋超人类"（实际约四十年）、1965"二十年内机器能做人类一切工作"——**如实写为误判**，保留对比语境，勿写成远见卓识。
- **与 Neisser 的争论**：1963/1967 Simon 撰文回应 Neisser 的 "cold/hot cognition" 之辩，情绪认知论文长期被 AI 界忽视、后被 Sloman/Picard 的工作重新关注——按实载写，勿拔高。
- **Oliver Williamson**：仅作为博士生列入（infobox 有），页面**未载其 2009 诺奖**，勿写。
- **政治/宗教细节**：无神论立场、单一税主张仅按实载一笔带过，不渲染；他服务过 Johnson 总统科学顾问委员会、参与创建 Economic Cooperation Administration（1948，马歇尔计划援助管理）——如实列，不评论。
- **死因**：2001-01 腹部肿瘤手术，术后并发症去世——页面实载可写；勿写"癌症去世"之外的延伸。
- **可引语**：Administrative Behavior 书中句 "[If] there were no limits to human rationality administrative theory would be barren..." 与 "The human being striving for rationality..."、1965 预言句、Turing citation——均页面原文可见；其余勿编造。
- **Portrait 佐料**：Rappaport 为其画过委托肖像（CMU 藏）；c.1958 与 Newell 国际象棋对弈照片在 images 目录——可用于"与 Newell"页插图。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 西蒙（或 赫伯特·西蒙） | 待写入 |
| name_en | Herbert A. Simon | 待写入 |
| birth_date | 1916-06-15 | 待写入 |
| death_date | 2001-02-09 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | scholar (economist / computer scientist / cognitive psychologist) | 待写入 |
| field_of_work | decision-making / bounded rationality / artificial intelligence / cognitive science / organization theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Henry Schultz（芝加哥大学计量经济学）
- **其他学术指导**：Rudolf Carnap、Nicholas Rashevsky、Harold Lasswell、Charles Merriam、John R. Commons
- **长期合作者**：Allen Newell（学生+共同获奖者）、J. C. (Cliff) Shaw（RAND）、James G. March（Organizations）、Edward Feigenbaum（EPAM）、K. Anders Ericsson（口头协议分析）、Fernand Gobet（CHREST）、David Hawkins（Hawkins–Simon 定理）、Clarence Ridley（首部合著）
- **著名博士生**：Edward Feigenbaum（1994 图灵奖）、Allen Newell（1975 图灵奖）、Richard E. Korf、John Muth、William F. Pounds、Saras Sarasvathy、Oliver E. Williamson、Richard Waldinger

## 8. 奖项清单

- ACM Turing Award（1975，与 Allen Newell 共享）
- 诺贝尔经济学奖（Nobel Memorial Prize in Economic Sciences，1978）
- 美国艺术与科学院 Fellow、美国哲学学会会员（1959）
- 美国国家科学院院士（NAS，1967）
- APA Award for Distinguished Scientific Contributions to Psychology（1969）
- National Medal of Science（1986）
- Harold Pender Award（1987）
- von Neumann Theory Prize（1988）
- APA Award for Outstanding Lifetime Contributions to Psychology（1993）
- ACM Fellow（1994）；IJCAI Award for Research Excellence（1995）
- 荣誉学位：Lund 商学院（1968）、University of Pavia（1988）、Harvard LL.D.（1990）、University of Buenos Aires（1999）

## 9. 机构清单

- 教育：University of Chicago（BA 1936 / MA / PhD 1943，政治科学）
- 任职：UC Berkeley 运筹研究组主任（1939–1942）、Illinois Institute of Technology 政治科学教授兼系主任（1942–1949）、Carnegie Institute of Technology / Carnegie Mellon University（1949–2001，工业管理系教授兼首任系主任，后兼授心理学与计算机科学）

## 10. 终审清单

- [ ] 生卒 1916-06-15 / 2001-02-09，享年 84，出生地 Milwaukee，去世地 Pittsburgh
- [ ] 1975 图灵奖写明"与 Allen Newell 共享"，citation 整句引用无误（含 [sic] 处理）
- [ ] 1978 诺贝尔经济学奖获奖理由原句引用无误
- [ ] 婚年 1938/1939 冲突处理一致（以正文 1938 或回避年份，全文统一）
- [ ] AI 预言（1957/1965）如实写为误判
- [ ] Williamson 仅列博士生、不提其诺奖
- [ ] 有限理性/满意化表述与 homo economicus 对照准确
- [ ] 死因"腹部肿瘤手术后并发症"表述准确
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Chicago · CMU | Turing 1975 · Nobel 1978`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1975/Herbert A. Simon/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Herbert_Simon_RIT_NandE_Vol13Num11_1981_Mar19_Complete.jpg`（1981 年 RIT 照，取 500px 版）；c.1958 与 Newell 对弈照可作插图（`Herbert_A._Simon_and_Allen_Newell_Chess_Match.jpg`）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（限 §5 所列）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Newell 1975）篇目侧重区分度检查，格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
