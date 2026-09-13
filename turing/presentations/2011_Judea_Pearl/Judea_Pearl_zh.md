# Judea Pearl（裘德亚·珀尔）立传提示词

> qid=Q92824 · 1936-09-04 – 在世留白 · 以色列裔美国计算机科学家 · 20/21 世纪 · 2011 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2011/Judea Pearl/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 以色列裔美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（贝叶斯网络 / 概率与因果演算的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Judea Pearl（希伯来语：יהודה פרל；中文惯称：裘德亚·珀尔 / 朱迪亚·珀尔——全篇统一其一）
- **生卒**：1936-09-04 生于特拉维夫（Tel Aviv，英属巴勒斯坦托管地，今以色列）→ 在世留白
- **国籍**：以色列裔美国人（Israeli-American）
- **身份**：电气工程师、计算机科学家、哲学家（页面原文三重身份）；UCLA 计算机科学与统计学教授、Cognitive Systems Laboratory 主任；*Journal of Causal Inference* 创刊编辑之一
- **家庭**：父母 Eliezer 与 Tova Pearl 为波兰犹太移民，在 Bnei Brak 长大；祖父 Chaim Pearl 是 Bnei Brak 的创建者之一；母系为 Menachem Mendel of Kotzk 后裔；1960 年与 Ruth Pearl（née Eveline Rejwan）结婚（Ruth 2021 年去世）；育有三子，其中包括记者 Daniel Pearl
- **教育轨迹**：
  - 服役于以色列国防军（IDF）、加入 kibbutz 后，1956 年决定学工程
  - Technion（Israel Institute of Technology）**电气工程** BS（1960）
  - 1960 年移居美国：Newark College of Engineering（今 NJIT）**电气工程** MS（1961）
  - Rutgers University **物理学** MS
  - Polytechnic Institute of Brooklyn（今 NYU Tandon）**电气工程** PhD（1965），论文 *Vortex Theory of Superconductive Memories*
- **博士导师**：Leonard Strauss、Leonard Bergstein（infobox 明载两人并列）
- **研究领域**：人工智能（概率路径）、贝叶斯网络、因果推断、统计与科学哲学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖理由（整句引用，核心红线）**："for fundamental contributions to artificial intelligence through the development of a calculus for probabilistic and causal reasoning"——注意关键词是 "a calculus for probabilistic and causal reasoning"（概率与因果推理的演算），**勿写成"do-演算"**（页面未载该术语，见 §5）。
2. **超导起点（1965 前后）**：RCA Research Laboratories（Princeton）从事超导参量放大器与存储器件；后在 Electronic Memories 从事先进存储系统——第一段职业生涯是硬件工程师。
3. **半导体的"毁灭"与转向（1970）**：当半导体技术把他毕生所学的超导存储"wipe out"（页面引用 Pearl 原话 "wiped out"），1970 年加入 UCLA 工程学院，转向**概率人工智能**——一次行业巨变成就一位理论家。
4. **贝叶斯网络（1980s）**：贝叶斯网络与人工智能概率方法的先驱之一（页面明载 "one of the pioneers of Bayesian networks and the probabilistic approach to artificial intelligence"）；代表作 *Probabilistic Reasoning in Intelligent Systems*（1988）。
5. **因果革命（2000）**：基于结构模型的因果与反事实推断理论；ACM 称其因果工作 "revolutionized the understanding of causality in statistics, psychology, medicine and the social sciences"；专著 *Causality: Models, Reasoning, and Inference*（2000，Cambridge University Press）。
6. **《The Book of Why》（2018）**：与 Dana Mackenzie 合著的因果科学大众向著作——把"因果关系阶梯"带进公众视野（页面载其书名与定位，可写"面向大众的因果之书"）。
7. **Heuristics（1984）**：早期启发式方法专著——贝叶斯网络之前的 AI 系统化成果。
8. **"现代 AI 奠基人"定位**：页面引述其工作 "laying the foundations of modern artificial intelligence, so computer systems can process uncertainty and relate causes to effects"；UCLA 教授 Richard E. Korf 称其为 "one of the giants in the field of artificial intelligence"（可引用）。
9. **跨界影响**：工作被定位为高层认知模型；兴趣横跨科学哲学、知识表示、非标准逻辑与学习——"工程师-科学家-哲学家"三重身份的叙事线。
10. **Daniel Pearl（仅一句，客观）**：2002 年其子、《华尔街日报》记者 Daniel Pearl 在巴基斯坦被与基地组织关联的恐怖分子绑架杀害；家人创立 Daniel Pearl Foundation——**按任务红线仅个人生活一页一句客观陈述，勿展开、勿渲染**。
11. **荣誉长廊**：Turing Award 2011、IJCAI Research Excellence 1999、Lakatos Award 2001、NAS 2014、NAE 1995、BBVA Frontiers of Knowledge 2021、英国皇家学会外籍院士 2025 等（完整清单见 §8）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（贝叶斯网络 — 蓝） | `#2E5A9E` | 概率推理 / 1988 专著 |
| 分类色 2（因果推断 — 青绿） | `#1E8E8E` | 因果演算 / 结构模型 / Causality |
| 分类色 3（硬件起点 — 琥珀） | `#D9A441` | RCA 超导存储 / 参量放大器 |
| 分类色 4（哲学与认知 — 玫瑰） | `#C0395B` | 科学哲学 / 认知模型 / The Book of Why |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「不确定性中寻找因果之链」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：深沉 / 回望（从超导硬件到因果哲学的漫长求索、丧子之痛后的坚韧）
- **选定曲目**：Alex-Productions **Nostalgy**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Judea_Pearl/Nostalgy.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「贝叶斯网络与因果革命 · 以色列裔美国」+ Pearl 1936– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1936–在世 生平纵览
4. **早年：特拉维夫与 Bnei Brak**（1936–1956）：波兰犹太移民之子、祖父为城市创建者之一、IDF 与 kibbutz
5. **从 Technion 到布鲁克林理工**（1956–1965）：电气工程 BS→MS→物理 MS→超导存储博士
6. **RCA 岁月与行业巨变**（1965–1970）：超导参量放大器、被半导体 "wiped out" 的转折
7. **UCLA 与概率人工智能**（1970 起）：转向、Cognitive Systems Laboratory
8. **Heuristics（1984）**：启发式方法的系统化
9. **贝叶斯网络**（1988）：Probabilistic Reasoning in Intelligent Systems、AI 的概率路径
10. **因果革命**（2000）：Causality 专著、结构模型、反事实推断、ACM "revolutionized" 评价
11. **The Book of Why**（2018）：与 Dana Mackenzie 合著、因果科学大众化
12. **跨越边界**：科学哲学/知识表示/非标准逻辑、Journal of Causal Inference 创刊编辑
13. **荣誉与传承**：Turing 2011、Lakatos 2001、NAS 2014、皇家学会 2025；门生 Dechter/Geffner/Bareinboim 等
14. **个人生活**：妻子 Ruth（1960 结婚，2021 去世）、三子；**Daniel Pearl 仅一句客观陈述 + Daniel Pearl Foundation**
15. **结尾**：在世、"处理不确定性、关联因与果"的现代 AI 奠基者

## 5. 史实陷阱与敏感点（终审必须检查）

- **"do-演算 / do-calculus"术语页面未载**：全篇正文与 infobox 都未出现 "do-calculus"——**禁写该术语**，一律使用 ACM citation 的 "a calculus for probabilistic and causal reasoning"（概率与因果推理的演算）及"基于结构模型的因果与反事实推断"表述。
- **Daniel Pearl 事件红线**：仅写页面实载的最简事实（2002 年、巴基斯坦、WSJ 记者、被绑架杀害、与基地组织关联、创立 Daniel Pearl Foundation），放在"个人生活"一页**一句**带过；**不展开事件经过、不写 2009 WSJ 文章标题细节、不渲染仇恨叙事**；Jonathan Sacks 转述的 "Hate killed my son..." 引语**不采用**（转述非直接语境，且易渲染情绪）。
- **宗教/政治观点不入正文**：页面载有 "practicing disbeliever"、NGO Monitor 顾问board、与 Chief Rabbi 合拍纪录片等——**全部禁写**（政治/宗教敏感内容）。
- **图灵奖年份口径**：获奖为 **2011** 年度（ACM 2012-03 公布颁奖）——封面写 2011，可注"2012 年颁发"；勿写反。
- **Harvey Prize 年份噪声**：infobox 写 2011，正文奖项清单写 2012——**以 infobox 2011 为准并留一句存疑注**，或统一写"2011/2012（页面两处不一致）"，勿二选一定稿。
- **博士导师**：infobox 明载**两人**：Leonard Strauss 与 Leonard Bergstein——并列写，勿只写其一。
- **PhD 校名**：论文完成于 Polytechnic Institute of Brooklyn（1965），**今为 NYU Tandon**——写"布鲁克林理工（今纽约大学 Tandon 工程学院）"，勿直接写"NYU 博士"。
- **"wiped out" 引语**：页面原文是 "When semiconductors 'wiped out' Pearl's work, as he later expressed it"——可用引号引用该动词短语并注明是 Pearl 本人后来的表达。
- **国籍与出生**：生于特拉维夫（时为英属巴勒斯坦托管地）——写"英属巴勒斯坦托管地（今以色列）"，勿写"生于以色列"（1936 年以色列尚未建国）。
- **在世**：死亡日期留白，生卒写 `1936–`。
- **引语白名单**：ACM citation、ACM "revolutionized..." 评价、Korf "one of the giants..."、"laying the foundations of modern AI"（页面引述）、"wiped out"——仅此数条页面有载；**Pearl 本人长段访谈引语（Science Network 等）虽页面脚注有载，但不入正文，勿编造其它引语**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 裘德亚·珀尔（或 朱迪亚·珀尔，全篇统一） | 待写入 |
| name_en | Judea Pearl | 待写入 |
| birth_date | 1936-09-04 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Israel / United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | artificial intelligence / Bayesian networks / causal inference / statistics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Leonard Strauss、Leonard Bergstein（Polytechnic Institute of Brooklyn，infobox 明载两人并列）
- **合作者**：Dana Mackenzie（The Book of Why 合著）、Madelyn Glymour 与 Nicholas Jewell（Causal Inference in Statistics 合著）
- **著名博士生**：Rina Dechter、Hector Geffner、Elias Bareinboim、Karthika Mohan
- **家族关系（parent-child）**：Daniel Pearl（子，记者，2002 年遇害——关系库仅录 parent-child 事实，勿录事件细节）
- **页面无载的关系**：禁写

## 8. 奖项清单（页面实载，择要）

- A.M. Turing Award（2011 年度，2012 颁发："a calculus for probabilistic and causal reasoning"）
- IJCAI Award for Research Excellence（1999）
- Lakatos Award（London School of Economics，2001）
- Benjamin Franklin Medal in Computers and Cognitive Science（Franklin Institute，2008）
- ACM Allen Newell Award（2004）
- David E. Rumelhart Prize（2011）；IEEE Intelligent Systems AI's Hall of Fame（2011）
- Harvey Prize（Technion；infobox 2011/正文 2012，两处不一致，注明）
- National Academy of Engineering（NAE，1995）；National Academy of Sciences（NAS，2014）
- Ulf Grenander Prize（American Mathematical Society，2018）；Dickson Prize（CMU，2015）
- Fellow：IEEE（1988）、AAAI（1990）、ACM（2015）、ASA（2019）、American Academy of Arts and Sciences（2012）、Royal Statistical Society Honorary Fellow（2020）
- BBVA Foundation Frontiers of Knowledge Award（2021）
- Foreign Member of the Royal Society（2025）
- 荣誉博士：Chapman（2008）、Toronto（2007）、CMU（2015）、Texas A&M（2014）、Hebrew University（2018）、Yale（2018）等
- RCA Laboratories Achievement Award（1965）——最早的职业奖项

## 9. 机构清单

- 教育：Technion（EE BS 1960）→ Newark College of Engineering（今 NJIT，EE MS 1961）→ Rutgers University（物理 MS）→ Polytechnic Institute of Brooklyn（今 NYU Tandon，EE PhD 1965）
- 任职：RCA Research Laboratories, Princeton（超导参量放大器与存储器件）→ Electronic Memories, Inc.（先进存储系统）→ UCLA School of Engineering（1970 起；计算机科学与统计学教授、Cognitive Systems Laboratory 主任）；*Journal of Causal Inference* 创刊编辑之一

## 10. 终审清单

- [ ] 生卒 1936-09-04 / 在世留白，出生地"特拉维夫（英属巴勒斯坦托管地，今以色列）"
- [ ] 图灵奖理由整句引用 "a calculus for probabilistic and causal reasoning"；全篇无 "do-演算/do-calculus" 字样
- [ ] 贝叶斯网络"先驱之一"与 1988 专著年份正确；Causality 2000、The Book of Why 2018（与 Mackenzie）
- [ ] 博士导师两人并列（Strauss + Bergstein）；PhD 校名"布鲁克林理工（今 NYU Tandon）"
- [ ] 图灵奖 2011 年度/2012 颁发口径正确；Harvey Prize 年份不一致已注明
- [ ] Daniel Pearl 仅个人生活一页一句客观陈述，无渲染、无相关引语
- [ ] 宗教观点 / NGO Monitor / 纪录片等政治宗教内容未出现
- [ ] 封面底部状态栏 `以色列裔美国 | UCLA · Technion · Brooklyn Polytechnic | Turing 2011`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2011/Judea Pearl/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 NIPS 2013 肖像（`images/500px-Judea_Pearl_at_NIPS_2013_11781981594_.jpg`，已就绪）
- [ ] **国籍**：封面顶部徽章明示以色列裔美国
- [ ] **引语核对**：仅 §5 白名单引语可用；Daniel Pearl 相关引语一律不用
- [ ] **敏感复查**：无宗教/政治内容、无 Daniel Pearl 事件渲染
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Goldwasser / Micali）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
