# Richard M. Karp（理查德·卡普）立传提示词

> qid=Q92612 · 1935-01-03 –（在世留白）· 美国计算机科学家、计算理论家 · 20 世纪 · 1985 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1985/Richard M. Karp/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 NP 完全性归约 / 最大流 / 二分图匹配的表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Richard Manning Karp（中文惯称：理查德·卡普）
- **生卒**：1935-01-03 生于波士顿（Boston, Massachusetts, US）→ **在世，死亡日期留白**
- **国籍**：美国（American）
- **身份**：计算机科学家、计算理论家（UC Berkeley 教授）
- **家庭**：父 Abraham、母 Rose Karp；三个弟妹 Robert、David、Carolyn；犹太家庭，成长于波士顿 Dorchester（当时以犹太人为主的社区）的小公寓；**父母均为哈佛毕业生**（母亲 57 岁通过夜课取得哈佛学位；父亲曾想读医学院但付不起学费，改任数学教师）
- **教育轨迹**：
  - Harvard University **学士 1955、硕士 1956**
  - Harvard University **应用数学博士 1959**，论文 *Some applications of logical syntax to digital computer programming*
- **博士导师**：Anthony Oettinger（Harvard）
- **研究领域**：算法理论、组合算法、计算复杂性、运筹学、生物信息学（近期兴趣）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 1985**：获奖理由整句引用——"For his continuing contributions to the theory of algorithms including the development of efficient algorithms for network flow and other combinatorial optimization problems, the identification of polynomial-time computability with the intuitive notion of algorithmic efficiency, and, most notably, contributions to the theory of NP-completeness. Karp introduced the now standard methodology for proving problems to be NP-complete which has led to the identification of many theoretical and practical problems as being computationally difficult."
2. **NP 完全性 21 问题（1972）**：里程碑论文 *Reducibility Among Combinatorial Problems* 证明 **21 个问题为 NP 完全**，确立了此后证明 NP 完全性的标准方法学——本篇的核心页。
3. **Held–Karp 算法（1962）**：与 Michael Held 共同开发的旅行商问题**精确指数时间算法**（动态规划）。
4. **Edmonds–Karp 算法（1971）**：与 Jack Edmonds 共同开发的网络最大流算法。
5. **Hopcroft–Karp 算法（1973）**：与 John Hopcroft 共同发表，二分图最大基数匹配的（当时）最快算法——与 1986 年 Hopcroft 篇各写一侧：Karp 篇从"合作者/算法"角度写，不展开 Hopcroft 生平。
6. **Karp–Lipton 定理（1980）**：与 Richard J. Lipton——若 SAT 可由多项式规模布尔电路求解，则多项式层级坍缩到第二层。
7. **Rabin–Karp 字符串搜索算法（1987）**：与 Michael O. Rabin 共同开发。
8. **命名算法群像**：Aanderaa–Karp–Rosenberg conjecture、Karmarkar–Karp algorithm、vector addition system 等——infobox "Known for" 列表可见其"以姓冠名"的广度。
9. **Berkeley 生涯**：1968 年起任 UC Berkeley 计算机、数学与运筹学教授；CS Division（EECS 系内）**首任副系主任**（first associate chair）；除 4 年华盛顿大学教授外始终在 Berkeley；1988–1995 与 1999 年起任 International Computer Science Institute（ICSI）研究科学家、主持 Algorithms Group；**2012 年出任 Simons Institute for the Theory of Computing 创始所长**。
10. **早年 IBM**：博士毕业后入职 IBM Thomas J. Watson Research Center（Held–Karp 等成果在此完成）。
11. **荣誉**：Fulkerson Prize（1979）、Turing（1985）、von Neumann Theory Prize（1990）、NAE 院士（1992，入选理由：NP 完全性理论与应用、高效组合算法、概率方法）、Charles Babbage Award（1995）、National Medal of Science（1996）、Harvey Prize（1998）、EATCS Award（2000）、Benjamin Franklin Medal in Computer and Cognitive Science（2004）、Kyoto Prize（2008）；NAS、美国艺术与科学院、美国哲学会会员；ACM Fellow（1994）；INFORMS Fellow（2002 届）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（计算复杂性 — 蓝） | `#2E5A9E` | NP 完全性 / 21 问题 / Karp–Lipton |
| 分类色 2（组合算法 — 青绿） | `#1E8E8E` | 最大流 / 二分图匹配 / TSP / Rabin–Karp |
| 分类色 3（学术机构与传承 — 琥珀） | `#D9A441` | Berkeley / ICSI / Simons Institute |
| 分类色 4（跨领域应用 — 玫瑰） | `#C0395B` | 运筹学 / 生物信息学 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏节点-边网络（归约箭头），呼应「21 个问题彼此归约、汇于 NP 完全性」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：探索 / 希望（在难解性地图上为千百问题标定坐标）
- **选定曲目**：Alex-Productions **Last Hope**（manifest 预分配，直接沿用），匹配"为最难的问题找到归约之路"的叙事。
- **落地文件**：`turing/presentations/Richard_M._Karp/LastHope.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「NP 完全性方法学奠基人 · 美国」+ 卡普 1935– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1935– 生平纵览（在世者不画卒年终点）
4. **多切斯特的犹太少年**（1935–1955）：父母均为哈佛毕业生、母亲 57 岁夜课取学位、父亲数学教师
5. **哈佛三级跳**（1955–1959）：学士/硕士/应用数学博士、Oettinger 门下、逻辑语法与计算机程序
6. **IBM Watson 研究中心**（1959–1968）：Held–Karp（1962，TSP 动态规划）
7. **Edmonds–Karp 最大流**（1971）：与 Edmonds 的合作
8. **21 个 NP 完全问题**（1972）：Reducibility Among Combinatorial Problems、归约方法学 ★ 核心页
9. **Hopcroft–Karp 二分图匹配**（1973）：与 1986 图灵奖得主 Hopcroft 的合作（只写合作，不写对方生平）
10. **复杂性理论的延伸**：Karp–Lipton 定理（1980）、Rabin–Karp（1987）、命名算法群像
11. **Berkeley 与 Simons Institute**（1968– ）：首任副系主任、ICSI、2012 创始所长
12. **图灵奖 1985**：citation 整句展示
13. **荣誉与传承**：Kyoto 2008、National Medal of Science 1996、NAE 1992、群星门生（Karmarkar / Motwani / Nisan 等）
14. **遗产**：NP 完全性方法学成为复杂性理论的通用语
15. **结尾**：在世、算法理论巨匠的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：整句引用（见 §2 第 1 条），是长 citation，勿截断改写；核心关键词为 network flow / combinatorial optimization / polynomial-time computability / NP-completeness / standard methodology。
- **21 问题是 1972 年论文**：*Reducibility Among Combinatorial Problems*（1972）证明 21 个问题 NP 完全——勿写成 1971（1971 是 Edmonds–Karp）或"1971 的 21 问题归约"。
- **在世**：Karp 无卒日，**死亡日期留白**；勿写任何健康/去世信息。
- **Cook 与 Karp 的分工**：NP 完全性框架由 Stephen Cook（1971，1982 图灵奖）提出、Karp 1972 年推广到 21 个自然问题——页面未直接写 Cook，如需语境提及 Cook 须标注"页面外常识，轻带即可"，勿展开、勿写两人互动。
- **Hopcroft–Karp（1973）**：合作算法，勿在本篇展开 Hopcroft 生平/贡献细节（1986 篇另写）；"fastest known method"是页面当时表述，勿写成"至今最快"。
- **Rabin–Karp 年份**：1987（与 Michael O. Rabin）——勿与 Rabin 1976 图灵奖年份混淆。
- **学位**：Harvard 学士 1955 / 硕士 1956 / 应用数学博士 1959——全程哈佛，无其他学校学位。
- **UC 华盛顿 4 年**：页面只说 "a 4-year period as a professor at the University of Washington"，未给起止年份——勿编造具体年份区间。
- **Simons Institute**：2012 年**创始所长**（founding director）——勿写成"创办人之一"或提前到其他年份。
- **荣誉**：Fulkerson 1979、Turing 1985、vN Theory 1990、Babbage 1995、NMS 1996、Harvey 1998、EATCS 2000、Franklin Medal 2004、Kyoto 2008——年份勿互串；NAE 入选理由（NP 完全性、组合算法、概率方法）可整句用。
- **家庭**：Dorchester 犹太社区、父母哈佛毕业等仅按页面实载一笔带过，不渲染。
- **引语红线**：页面无 Karp 个人直接引语；可引用的只有①图灵奖 citation、②NAE 入选理由句。其余勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 卡普（或 理查德·卡普） | 待写入 |
| name_en | Richard M. Karp | 待写入 |
| birth_date | 1935-01-03 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | theory of algorithms / computational complexity / combinatorial optimization / operations research | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Anthony Oettinger（Harvard）
- **合作者**：Michael Held（Held–Karp）、Jack Edmonds（Edmonds–Karp）、John Hopcroft（Hopcroft–Karp）、Richard J. Lipton（Karp–Lipton）、Michael O. Rabin（Rabin–Karp）
- **著名博士生**：Faith Ellen、Sally Floyd、Dan Gusfield、Narendra Karmarkar、Valerie King、Michael Luby、Rajeev Motwani、Noam Nisan、Ron Shamir、Barbara Simons、Eric Xing 等（页面 infobox 实载 17 人，择要入库）
- **无其他导师信息**：页面未载本科/硕士导师，勿编造

## 8. 奖项清单

- Fulkerson Prize（1979）
- Turing Award（1985）
- John von Neumann Theory Prize（1990）
- NAE 院士（1992）
- ACM Fellow（1994）
- IEEE Computer Society Charles Babbage Award（1995）
- National Medal of Science（1996）
- Harvey Prize, Technion（1998）
- EATCS Award（2000）
- INFORMS Fellow（2002 届）
- Benjamin Franklin Medal in Computer and Cognitive Science（2004）
- Kyoto Prize, Advanced Technology（2008）

## 9. 机构清单

- 教育：Harvard University（BA 1955 / MA 1956 / PhD 应用数学 1959）
- 任职：IBM Thomas J. Watson Research Center（1959 年起，至 1968 前）、UC Berkeley 教授（1968– ，CS/数学/运筹学；CS Division 首任副系主任）、University of Washington 教授（4 年，起止年份页面未载）、ICSI 研究科学家（1988–1995、1999– ，主持 Algorithms Group）、Simons Institute for the Theory of Computing 创始所长（2012– ）

## 10. 终审清单

- [ ] 生卒 1935-01-03 / 在世留白，出生地 Boston
- [ ] 21 NP 完全问题 = 1972 论文 Reducibility Among Combinatorial Problems
- [ ] 图灵奖 citation 整句引用，未截断改写
- [ ] Hopcroft–Karp 1973 只写合作不展开对方生平
- [ ] Rabin–Karp = 1987；Held–Karp = 1962；Edmonds–Karp = 1971；Karp–Lipton = 1980
- [ ] 全程 Harvard 学位（1955/1956/1959），导师 Oettinger
- [ ] Simons Institute 2012 创始所长；UC 华盛顿 4 年不写具体年份
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | UC Berkeley · IBM Watson · Harvard | Turing 1985`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1985/Richard M. Karp/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Karp_mg_7725-b.cr2.jpg`（"Karp in 2009"）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅限 citation 与 NAE 理由）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Wirth / Hopcroft / Tarjan）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
