# Allen Newell（艾伦·纽厄尔）立传提示词

> qid=Q439245 · 1927-03-19 – 1992-07-19 · 美国计算机科学家、认知心理学家 · 20 世纪 · 1975 图灵奖（与 Herbert A. Simon 共享）
> 本地 Wikipedia 数据源：`turing/pages/1975/Allen Newell/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（物理符号系统假说 / 手段-目的分析 / Soar 认知架构的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Allen Newell（中文惯称：艾伦·纽厄尔；注意勿与同名研究者 Alan Newell 混淆，页面明示 "Not to be confused with"）
- **生卒**：1927-03-19 生于旧金山（San Francisco, California）→ 1992-07-19 逝于匹兹堡（Pittsburgh, Pennsylvania），享年 65；死因页面未载（NYT 讣闻标题仅写 "Allen Newell, 65; Scientist Founded A Computing Field"），**勿编造**
- **国籍**：美国（American）
- **身份**：计算机科学家、认知心理学家（RAND Corporation 与 Carnegie Mellon University 计算机学院 / Tepper 商学院 / 心理学系）
- **家庭**：配偶 Noel McKenna（1947 年结婚）
- **教育轨迹**：
  - Stanford University **物理**学士（BS，1949）
  - Princeton University 数学研究生（1949–1950，仅一年，未获学位——因接触博弈论后确信更偏好实验+理论结合的研究，遂离开）
  - Carnegie Mellon University（时为 Carnegie Tech / 现称 Tepper School of Business）**硕士+博士**（MS, PhD），博士在商学院完成
- **博士导师**：Herbert A. Simon（1978 年诺贝尔经济学奖得主）——注意：本篇主角是**学生**，Simon 是**导师**
- **研究领域**：计算机科学、认知心理学、人工智能、认知架构

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1975 图灵奖（与 Simon 共享）**：获奖理由是 "for their contributions to artificial intelligence and the psychology of human cognition"（对人工智能与人类认知心理学的贡献）——共享结构必须写明。
2. **早年曲线**：斯坦福物理学士（1949）→ Princeton 数学研究生一年（接触**博弈论**后转向）→ 1950 加入 RAND Corporation（"a group that was studying logistics problems of the Air Force" 空军后勤问题研究组）。
3. **组织决策实验期**：与 John Kennedy、Bob Chapman、Bill Biel 在空军预警站研究机组组织过程（1952 获空军资助建模拟器），由此确立信念——**信息处理是组织的中心活动**。
4. **1954-09 转折点**：参加 Oliver Selfridge 研讨会，Selfridge "described a running computer program that learned to recognize letters and other patterns"——Newell 从此相信可造出含智能、能自适应的系统。
5. **《The Chess Machine》（1955）**：提出以"类人方式"下棋的程序设想，引起经济学家（未来的诺奖得主）Herbert A. Simon 注意。
6. **Logic Theorist（1956）**：与 Simon、程序员 J. C. (Cliff) Shaw 共同开发，**通常被认为是第一个真正的 AI 程序**——但必须带页面脚注限定：Arthur Samuel 的跳棋程序更早发布、Christopher Strachey 1951 年也写过跳棋程序。
7. **三大发明**：list processing（此后 AI 最重要的编程范式）、把 **means-ends analysis（手段-目的分析）** 应用于一般推理（"reasoning as search"）、用 **heuristics** 限制搜索空间。
8. **Dartmouth 会议（1956）**：Logic Theorist 在会上展示；该会现被视为 "birth of artificial intelligence"，与会者成为此后二十年 AI 领袖，Newell 在其中。
9. **GPS（1957，General Problem Solver）**：与 Simon 持续合作的高影响力成果，means–ends analysis 的高影响力实现。
10. **物理符号系统假说（physical symbol systems hypothesis）**：与 Simon 提出——**有争议的哲学主张**：一切智能行为都可还原为其程序所演示的那种符号操作。保留"争议性"语境，勿写成公论。
11. **Soar 与统一认知理论（Unified Theories of Cognition，1990）**：其工作以 Soar 认知架构与 1990 年的统一认知理论达到顶点，直至去世仍以此为目标；他开创的**认知架构领域**至今活跃。
12. **荣誉注脚**：ACM–AAAI **Allen Newell Award** 以其命名；CMU 计算机学院的 Award for Research Excellence 亦以其命名。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（人工智能 — 蓝） | `#2E5A9E` | Logic Theorist / GPS / Dartmouth |
| 分类色 2（符号与推理 — 青绿） | `#1E8E8E` | 物理符号系统假说 / means-ends analysis |
| 分类色 3（认知架构 — 琥珀） | `#D9A441` | Soar / Unified Theories of Cognition |
| 分类色 4（认知心理学 — 玫瑰） | `#C0395B` | 组织决策 / 信息处理 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和节点连线（稀疏圆点 + 细连线），呼应「符号搜索 / 推理即搜索」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：唤醒 / 开创（从物理学生到 AI 奠基者的觉醒之路）
- **选定曲目**：Alex-Productions **Awaken**（manifest 预分配，直接沿用），匹配"信息处理唤醒智能"的叙事。
- **落地文件**：`turing/presentations/Allen_Newell/Awaken.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 奠基者 · 美国」+ 纽厄尔 1927–1992 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1927–1992 生平纵览
4. **早年：旧金山少年与斯坦福物理**（1927–1949）
5. **Princeton 一年与 RAND 岁月**（1949–1954）：博弈论的冲击、空军后勤、机组组织实验
6. **转折点：Selfridge 研讨会与《The Chess Machine》**（1954–1955）
7. **Logic Theorist：第一个真正的 AI 程序**（1956，与 Simon/Shaw；带 Samuel/Strachey 限定脚注）
8. **Dartmouth 会议与 IPL / list processing**（1956）
9. **GPS 与手段-目的分析**（1957）
10. **物理符号系统假说**（与 Simon，争议性主张）
11. **Soar 与统一认知理论**（1990）
12. **CMU 学派：导师 Simon 与门生成林**（Berliner/Card/Laird/Ritter/Tambe）
13. **荣誉与传承**：Turing 1975、NMS 1992、以其命名的 ACM–AAAI Allen Newell Award
14. **遗产**：AI、认知科学、认知架构的开创者
15. **结尾**：65 岁、AI 与认知科学交汇处的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享奖结构**：1975 图灵奖由 Newell 与 **Simon 两人共享**，封面与正文必须写明共享；本篇侧重 **Newell 的程序实现与认知架构**（Logic Theorist/GPS/Soar），Simon 篇侧重有限理性与诺贝尔经济学奖，避免两篇完全重复；**禁写**页面无载的两人恩怨（页面载的是 lasting partnership）。
- **师生关系方向**：Newell 的博士导师是 **Herbert A. Simon**（在 CMU/Tepper 商学院获 PhD）——勿写反。
- **Logic Theorist 表述**："usually considered the first true AI program" 必须**带限定**（Samuel 跳棋更早、Strachey 1951 也写过跳棋程序）；勿写"人类第一个 AI 程序"这种绝对化表述。
- **Princeton 一年**：1949–1950 在 Princeton **读数学、未获学位**（infobox 无 Princeton 学位），离开原因是受博弈论影响——勿写成 Princeton 博士或肄业之外的说法。
- **物理符号系统假说**：页面原文称 "controversial philosophical assertion"——**争议性主张**，保留争议语境。
- **Dartmouth 会议**：1956 年，Newell 是**参与者**（展示 Logic Theorist），会议被视为 "birth of AI"——勿写其发起。
- **图灵奖理由**：正文口径 "for their contributions to artificial intelligence and the psychology of human cognition"——勿延伸成"AI 之父"之类称号。
- **死因**：1992-07-19 卒于匹兹堡，享年 65，**页面未载死因，勿编造**。
- **可引语**：仅限页面原文可见引句："a group that was studying logistics problems of the Air Force"、"turned to the design and conduct of laboratory experiments on decision making in small groups"、（Selfridge）"described a running computer program that learned to recognize letters and other patterns"。
- **荣誉**：Turing 1975、IJCAI 1989、IEEE Piore 1990、National Medal of Science 1992、Louis E. Levy Medal 1992 等（详见 §8）——无 Nobel，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 纽厄尔（或 艾伦·纽厄尔） | 待写入 |
| name_en | Allen Newell | 待写入 |
| birth_date | 1927-03-19 | 待写入 |
| death_date | 1992-07-19 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist / cognitive psychologist | 待写入 |
| field_of_work | computer science / cognitive psychology / artificial intelligence / cognitive architecture | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Herbert A. Simon（CMU/Tepper 商学院；亦是 1975 共享奖得主、1978 诺奖得主）
- **长期合作者**：Herbert A. Simon、J. C. (Cliff) Shaw（RAND 三人组：IPL / Logic Theorist / GPS）
- **RAND 同事**：John Kennedy、Bob Chapman、Bill Biel（空军机组组织实验）
- **著名博士生**：Hans Berliner、Stuart Card、John E. Laird、Frank Ritter、Milind Tambe

## 8. 奖项清单

- A. M. Turing Award（1975，与 Herbert A. Simon 共享）
- Harry Goode Memorial Award（AFIPS，1971）
- 美国国家科学院院士（NAS，1972）、美国艺术与科学院 Fellow（1972）
- Guggenheim Fellowship（1976–77）
- Alexander C. Williams Jr. Award（Human Factors Society，1979，与 Biel/Chapman/Kennedy）
- 美国国家工程院院士（NAE，1980）；AAAI 首任主席（1980）
- IEEE Computer Society Computer Pioneer Award（1981，charter recipient）
- APA Distinguished Scientific Contribution Award（1985）
- 荣誉博士：University of Pennsylvania（1986）、University of Groningen（1989）
- IJCAI Award for Research Excellence（1989）；APS William James Fellow Award（1989，charter recipient）
- IEEE Emanuel R. Piore Award（1990）；IEEE W.R.G. Baker Prize Paper Award（1990）；AAAI Fellow（1990）
- U.S. National Medal of Science（1992）；Franklin Institute Louis E. Levy Medal（1992）
- 纪念奖项：ACM–AAAI Allen Newell Award、CMU School of Computer Science Award for Research Excellence（以其命名）

## 9. 机构清单

- 教育：Stanford University（物理 BS 1949）、Princeton University（数学研究生 1949–1950）、Carnegie Mellon University（MS/PhD，Tepper School of Business）
- 任职：RAND Corporation（1950 起，Santa Monica）、Carnegie Mellon University（计算机学院 + Tepper 商学院 + 心理学系）

## 10. 终审清单

- [ ] 生卒 1927-03-19 / 1992-07-19，享年 65，出生地 San Francisco，去世地 Pittsburgh
- [ ] 1975 图灵奖写明"与 Herbert A. Simon 共享"
- [ ] 师生关系方向正确：Newell 的博士导师是 Simon
- [ ] Logic Theorist "first true AI program" 带 Samuel/Strachey 限定脚注
- [ ] Princeton 仅数学研究生一年（1949–1950），无学位
- [ ] 物理符号系统假说保留 "controversial" 争议语境
- [ ] Dartmouth 会议 1956"参与者"表述准确
- [ ] 死因留白（页面未载，勿编造）
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | RAND · Carnegie Mellon | Turing 1975`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1975/Allen Newell/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Allen_Newell.jpg`（目录另有 250px-Allen_Newell.jpg，取大图版）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（限 §5 所列三条）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Simon 1975）篇目侧重区分度检查，格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
