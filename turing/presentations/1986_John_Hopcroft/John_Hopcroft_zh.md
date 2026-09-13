# John Hopcroft（约翰·霍普克洛夫特）立传提示词

> qid=Q62874 · 1939-10-07 –（在世留白）· 美国理论计算机科学家 · 20 世纪 · 1986 图灵奖（与 Robert Tarjan 共享）
> 本地 Wikipedia 数据源：`turing/pages/1986/John Hopcroft/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如自动机/形式语言、平面图判定、二分图匹配的表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Edward Hopcroft（中文惯称：约翰·霍普克洛夫特）
- **生卒**：1939-10-07 生于西雅图（Seattle, Washington, U.S.）→ **在世，死亡日期留白**
- **国籍**：美国（American）
- **身份**：理论计算机科学家、教育家；Cornell 大学荣休教授；北京大学计算与数字智能交叉学科研究中心（Center on Frontiers of Computing Studies）联合主任；上海交通大学 John Hopcroft 计算机科学中心主任；华中科技大学 Hopcroft 计算中心主任
- **家庭**：外祖父 Jacob Nist 于 1889 年创办 Seattle-Tacota Box Company（Seattle-Tacoma Box Company）——这是页面唯一家庭信息，一笔带过勿渲染
- **教育轨迹**：
  - Seattle University **电气工程学士 1961**
  - Stanford University **电气工程硕士 1962**
  - Stanford University **电气工程博士 1964**，论文 *Synthesis of Threshold Logic Networks*
- **博士导师**：Richard Mattson（Stanford）
- **研究领域**：计算机科学（算法设计与分析、自动机与形式语言、数据结构）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 1986（与 Robert Tarjan 共享）**：获奖理由整句引用——"for fundamental achievements in the design and analysis of algorithms and data structures"。**共享结构必须写明**：两人同年同理由获奖；本篇侧重 Hopcroft 的算法与自动机理论、教材与教育家面向；Tarjan 篇侧重数据结构；**禁写页面无载的两人恩怨或内部分工争议**。
2. **"Cinderella book"**：其计算理论教材（*Introduction to Automata Theory, Languages, and Computation*）被业界通称 "Cinderella book"，被视为领域标准——正文明载。
3. **经典三部曲（与 Aho、Ullman）**：*Formal Languages and Their Relation to Automata*（1969，与 Ullman）→ *The Design and Analysis of Computer Algorithms*（1974，Aho+Hopcroft+Ullman）→ *Data Structures and Algorithms*（1983，Aho+Hopcroft+Ullman）；另有 2001 年第二版（Hopcroft+Motwani+Ullman）与 *Foundations of Data Science*（2017，与 Avrim Blum、Ravindran Kannan）——"coauthoring field-defining texts" 是 Karlstrom 奖理由原文。
4. **平面图工作（与 Tarjan）**：Hopcroft–Tarjan 平面性判定算法（planarity testing）是**首个线性时间**平面性判定算法（细节在 Tarjan 篇展开，本篇一句话带过即可）。
5. **Hopcroft–Karp 算法（1973）**：与 Richard Karp 合作，二分图最大基数匹配最快算法——从 Hopcroft 侧写合作即可，勿展开 Karp 生平。
6. **Princeton 三年 → Cornell 一生**：博士后在 Princeton 工作三年，此后长期任教 Cornell University。
7. **教育家身份**：2008 年 Karl V. Karlstrom Outstanding Educator Award 理由整句可用——"for his vision of and impact on computer science, including co-authoring field-defining texts on theory and algorithms, which continue to influence students 40 years later, advising PhD students who themselves are now contributing greatly to computer science, and providing influential leadership in computer science research and education at the national and international level."
8. **与中国**：2017 年上海交通大学设立 John Hopcroft Center for Computer Science；2020 年港中深设立 Hopcroft Institute for Advanced Information Sciences 并聘其为 Einstein 教授；2016 年获中国**友谊奖**（Friendship Award）——中国相关内容是本篇区别于 Tarjan 篇的特色素材。
9. **NSB 提名**：1992 年由 George H. W. Bush 提名进入 National Science Board。
10. **IEEE von Neumann Medal（2010，与 Ullman 共同获得）**：理由整句——"laying the foundations for the fields of automata and language theory and many seminal contributions to theoretical computer science."
11. **荣誉矩阵**：NAE 院士（1989，理由：计算机算法的根本贡献与杰出 CS 教材）、ACM Fellow（1994）、Harry H. Goode Memorial Award（2005，理由："for fundamental contributions to the study of algorithms and their applications in information processing"）、荣誉博士（University of Sydney 2005、圣彼得堡 ITMO 2009）；NAS/NAE 院士、中科院外籍院士、AAAS（艺术与科学院）Fellow、AAAS（科学促进会）Fellow、IEEE Fellow。
12. **门生**：Alfred Aho（1986 前后合作者/学生）、Gilles Brassard、Cynthia Dwork、Zvi Galil、Daniela L. Rus 等（infobox 实载）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（算法设计与分析 — 蓝） | `#2E5A9E` | 图灵奖理由 / 平面图 / Hopcroft–Karp |
| 分类色 2（自动机与形式语言 — 青绿） | `#1E8E8E` | Cinderella book / 与 Ullman 的 von Neumann Medal |
| 分类色 3（计算机教育 — 琥珀） | `#D9A441` | Karlstrom 奖 / 经典教材 / 门生 |
| 分类色 4（国际化与中国 — 玫瑰） | `#C0395B` | 友谊奖 / 交大与港中深中心 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏状态节点与转移箭头（自动机状态图），呼应「形式语言与自动机的教学经典」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：宏阔 / 奠基（为一代人写教材、把理论变标准）
- **选定曲目**：Alex-Productions **Empire Collapse**（manifest 预分配，直接沿用），匹配"奠定学科版图的宏阔叙事"。
- **落地文件**：`turing/presentations/John_Hopcroft/EmpireCollapse.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「算法与自动机理论教育家 · 美国」+ Hopcroft 1939– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1939– 生平纵览（在世者不画卒年终点）
4. **西雅图的少年**（1939–1961）：外祖父 Seattle-Tacoma Box Company、Seattle University 电机系
5. **Stanford 电机工程三级跳**（1961–1964）：硕士 1962 / 博士 1964、阈值逻辑网络论文、Mattson 门下
6. **Princeton 三年与 Cornell 起点**（1964–1970s）：Princeton 三年 → Cornell 长期执教
7. **与 Aho、Ullman 的教材三部曲**（1969–1983）：Formal Languages 1969 / Design and Analysis 1974 / Data Structures 1983 ★ 核心页
8. **Cinderella book**：计算理论教材的领域标准地位
9. **Hopcroft–Karp 二分图匹配**（1973）：与 Karp 的合作（只写合作）
10. **图灵奖 1986**：与 Tarjan 共享、citation 整句展示、共享结构说明
11. **平面图与 Tarjan 的合作**：一句话带过，细节归 Tarjan 篇
12. **教育家**：Karlstrom 2008 理由整句、Goode 奖 2005、von Neumann Medal 2010（与 Ullman）
13. **与中国**：友谊奖 2016、交大中心 2017、港中深 2020、北大联合主任
14. **荣誉与门生**：NAE 1989、NSB 1992 提名、Aho/Brassard/Dwork/Rus 等门生
15. **结尾**：在世、教材塑造两代人的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享结构**：1986 图灵奖为 Hopcroft 与 Tarjan **两人共享、同一 citation**（"for fundamental achievements in the design and analysis of algorithms and data structures"）——必须写明共享；侧重分工按本篇 §2 第 1 条执行；**禁写页面无载的两人恩怨/竞争/评优细节**。
- **本篇侧重**：教材（《算法设计与分析》等三部曲+Cinderella book）、自动机与形式语言、教育家身份、中国中心——数据结构深水区（并查集、splay 树等）归 Tarjan 篇，本篇勿展开。
- **学位口径**：Seattle University EE 学士 1961；Stanford EE 硕士 1962、EE 博士 1964——**全部是电气工程学位**，勿写成 CS 学位。
- **博士导师**：Richard Mattson——勿编造成 Knuth/Aho 等名人。
- **Cinderella book 版本**：教材 1969 年初版书名 *Formal Languages and Their Relation to Automata*（与 Ullman）；"Cinderella book" 通称对应 *Introduction to Automata Theory, Languages, and Computation*（2001 第二版 Hopcroft+Motwani+Ullman）——书名与作者名单逐版对表，勿混。
- **Hopcroft–Karp（1973）**：与 Karp 合作，"fastest known method" 是页面当时表述——勿写"至今最快"、勿展开 Karp 生平（Karp 篇 1985 另写）。
- **平面性算法**：Hopcroft–Tarjan 是"first linear-time algorithm for planarity testing"（此表述在 Tarjan 页面，本页面只说 "along with his work with Tarjan on planar graphs"）——本篇写"与 Tarjan 的平面图合作"，细节归 Tarjan 篇。
- **在世**：无卒日，**死亡日期留白**。
- **NSB 提名**：1992 年由老布什**提名**进入 National Science Board——是"提名"，勿写成"担任/领导 NSF"。
- **von Neumann Medal**：2010、与 Ullman **共同**获得——勿写成 Hopcroft 单独获奖。
- **中国奖项**：2016 Friendship Award（中国友谊奖）——勿与"中科院外籍院士"混年混奖项。
- **引语红线**：页面无 Hopcroft 个人直接引语；可引用的只有①图灵奖 citation、②Karlstrom 2008 理由、③Goode 2005 理由、④von Neumann Medal 2010 理由、⑤NAE 1989 入选理由。其余勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 霍普克洛夫特（或 约翰·霍普克洛夫特） | 待写入 |
| name_en | John Hopcroft | 待写入 |
| birth_date | 1939-10-07 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | design and analysis of algorithms / automata and formal language theory / data structures / computer science education | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Richard Mattson（Stanford EE）
- **教材合作者**：Alfred Aho、Jeffrey Ullman（三部曲）；Rajeev Motwani（2001 第二版）；Avrim Blum、Ravindran Kannan（Foundations of Data Science 2017）
- **合作者**：Robert Tarjan（平面图，1986 共享图灵奖）、Richard M. Karp（Hopcroft–Karp 算法）
- **著名博士生**：Alfred Aho、Chandrajit Bajaj、Gilles Brassard、Richard J. Cole、Cynthia Dwork、Zvi Galil、Daniela L. Rus（infobox 实载 7 人）
- **家庭**：外祖父 Jacob Nist（Seattle-Tacoma Box Company 创办人）——仅家谱事实，勿入学术关系

## 8. 奖项清单

- Turing Award（1986，与 Robert Tarjan 共享，"for fundamental achievements in the design and analysis of algorithms and data structures"）
- NAE 院士（1989）
- ACM Fellow（1994）
- Harry H. Goode Memorial Award（2005）
- 荣誉博士：University of Sydney（2005）、Saint Petersburg ITMO（2009）
- Karl V. Karlstrom Outstanding Educator Award（2008）
- IEEE John von Neumann Medal（2010，与 Jeffrey Ullman 共同获得）
- Friendship Award（China，2016）
- 院士身份：NAS、NAE、中国科学院外籍院士、American Academy of Arts and Sciences Fellow、AAAS（科学促进会）Fellow、IEEE Fellow

## 9. 机构清单

- 教育：Seattle University（EE BS 1961）、Stanford University（EE MS 1962 / EE PhD 1964）
- 任职：Princeton University（三年，起止年份页面未载）、Cornell University（此后长期，现为荣休教授）、北京大学 Center on Frontiers of Computing Studies 联合主任、上海交通大学 John Hopcroft Center for Computer Science 主任（中心 2017 年设立）、华中科技大学 Hopcroft 计算中心主任

## 10. 终审清单

- [ ] 生卒 1939-10-07 / 在世留白，出生地 Seattle
- [ ] 图灵奖 1986 与 Tarjan 共享、citation 整句引用、共享结构写明、无恩怨描写
- [ ] 本篇侧重教材/自动机/教育家/中国中心；数据结构细节未越界到 Tarjan 篇
- [ ] 学位全部为电气工程（Seattle 1961 / Stanford 1962、1964），导师 Mattson
- [ ] 教材三部曲书名-年份-作者逐版对表（1969 / 1974 / 1983 / 2001 / 2017）
- [ ] Hopcroft–Karp 1973 只写合作；平面性算法细节归 Tarjan 篇
- [ ] von Neumann Medal 2010 与 Ullman 共同获得；NSB 1992 是"提名"
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Cornell · Stanford · Princeton | Turing 1986`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1986/John Hopcroft/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Hopcrofg_cropped2_.jpg`（2006 年 ITMO 大学照片）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅限 §5 列出的 citation/理由句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Wirth / Karp / Tarjan）格式对齐；与 Tarjan 篇侧重区分复核

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
