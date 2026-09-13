# Michael O. Rabin（迈克尔·拉宾）立传提示词

> qid=Q357965 · 1931-09-01 – 2026-04-14 · 以色列/美国计算机科学家 · 20/21 世纪 · 1976 图灵奖（与 Dana Scott 共享）
> 本地 Wikipedia 数据源：`turing/pages/1976/Michael O. Rabin/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 以色列`，页面无明确国籍字段——见 §5），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名（含希伯来文 מִיכָאֵל עוזר רַבִּין）、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（非确定性自动机 / Miller–Rabin 素性测试 / rolling hash 的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Michael Oser Rabin（希伯来文：מִיכָאֵל עוזר רַבִּין；中文惯称：迈克尔·奥瑟·拉宾；注意勿与小提琴家 Michael Rabin 混淆，页面明示消歧）
- **生卒**：1931-09-01 生于布雷斯劳（Breslau, Lower Silesia, Prussia, Germany；今波兰弗罗茨瓦夫 Wrocław）→ 2026-04-14 逝于耶路撒冷，享年 94；**死因页面未载，勿编造**
- **国籍**：页面 infobox 无明确 nationality 字段——生于德国、1935 年随家移居委任统治时期巴勒斯坦、学术生涯在以色列与美国——封面建议用「以色列」（希伯来大学/以色列奖口径），**勿写"德裔/双重国籍"等页面无载表述**
- **身份**：计算机科学家
- **家庭**：拉比（rabbi）之子；女儿 Tal Rabin 亦是杰出计算机科学家（页面实载）；婚姻/配偶页面无载，**禁写**
- **教育轨迹**：
  - 海法 Hebrew Reali School 毕业（1948）；高中受数学家 Elisha Netanyahu（时任中学教师）教导
  - Hebrew University of Jerusalem（M.Sc.；BS/MS per infobox）
  - University of Pennsylvania 研究生 → **Princeton University 博士（1956）**
- **博士论文**：*Recursive Unsolvability of Group Theoretic Problems*（1957/1956 年获学位）
- **博士导师**：Alonzo Church
- **研究领域**：计算机科学（自动机理论、计算复杂度、随机算法、密码学）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1976 图灵奖（与 Dana Scott 共享）**：ACM citation 整句——"For their joint paper 'Finite Automata and Their Decision Problems,' which introduced the idea of nondeterministic machines, which has proved to be an enormously valuable concept. Their (Scott & Rabin) [sic] classic paper has been a continuous source of inspiration for subsequent work in this field."（**本篇核心红线引文**；注意 citation 内原文即有 "(Scott & Rabin) [sic]"）
2. **拉比之子与迁徙**：1931 生于布雷斯劳，1935 年随家移居巴勒斯坦；海法最好中学、1948 毕业即遇 1948 阿以战争入伍——**数学家 Abraham Fraenkel 亲自向军方说情**，1949 年退伍得以入学。
3. **Lamb Estate 之夏（1950s 末）**：IBM 邀其至 Westchester County 的 Lamb Estate 与一批青年数学家共研——**正是在此与 Dana Scott 写下 "Finite Automata and Their Decision Problems"（1959）**：用非确定性自动机重新证明 Kleene 的"有限状态机恰接受正则语言"。
4. **计算复杂度之源**：翌年夏天重返 Lamb Estate，**John McCarthy 向他提出间谍-警卫-口令谜题**，由此写出 "Degree of Difficulty of Computing a Function and Hierarchy of Recursive Sets"（1960）；非确定性机器成为复杂度理论关键概念（P/NP 的描述核心）。**1966 年引入多项式时间**（Cobham 与 Edmonds 独立且稍早提出）。
5. **概率自动机（1960）**：受 Edward F. Moore 邀至 Bell Labs，引入以掷硬币决定状态转移的概率自动机——正则语言状态数的指数级缩减。
6. **无限树自动机（1969）**：引入 infinite-tree automata 并证明 n 个后继的一元二阶理论（n=2 时为 S2S）**可判定**；证明关键部分隐含给出 parity games 的 determinacy（位于 Borel 层级第三层）。
7. **希伯来大学神速**：29 岁任希伯来大学数学研究所副教授兼所长、33 岁正教授；其 recall 引语："There was absolutely no appreciation of the work on the issues of computing. Mathematicians did not recognize the emerging new field."
8. **Miller–Rabin 素性测试（1975）**：结束希伯来大学 Rector 任期后赴 MIT 任访问教授期间发明——基于 Gary Miller 在广义黎曼假设下的确定性工作，Rabin 版本**无需该假设**；快速素性测试是公钥密码实现的关键；2003 年与 Miller、Solovay、Strassen 获 **Paris Kanellakis Award**；1976 年在 CMU 演讲，Traub 称之为 "revolutionary"。
9. **密码学三连**：**Rabin 签名算法（1978）**——首个安全性等价于大整数分解困难性的非对称密码系统；**不经意传输（oblivious transfer，1981）**——再造 Wiesner 以 "multiplexing" 之名的弱变体；**Rabin–Karp 字符串搜索（1987，与 Richard Karp）**——以 rolling hash 闻名。
10. **学术迁徙**：Berkeley 访问（1961–62）、MIT 访问（1962–63）、**Harvard University Gordon McKay 讲席教授（1981）**；后任 Harvard Thomas J. Watson Sr. 荣休教授 + 希伯来大学荣休教授；2007 年春哥伦比亚大学访问教授（讲授密码学导论）。
11. **五院院士级荣誉**：美国国家科学院**外籍**院士、美国哲学学会、美国艺术与科学院、法国科学院、英国皇家学会**外籍**院士。
12. **奖项满贯**：Weizmann Prize 1959、Harvey Prize 1980、Gibbs Lecture 1985、Israel Prize 1995（计算机科学）、IEEE Babbage Award 2000、Paris Kanellakis Award 2003、EMET Prize 2004、Gödel Lecture 2004、Dan David Prize 2010（Future 类，与 Kleinrock、Gordon Moore 共享）、Dijkstra Prize 2015、Harvard 荣誉博士 2017。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（自动机理论 — 蓝） | `#2E5A9E` | 非确定性自动机 / Rabin–Scott |
| 分类色 2（复杂度与逻辑 — 青绿） | `#1E8E8E` | 多项式时间 / S2S 可判定性 |
| 分类色 3（随机算法 — 琥珀） | `#D9A441` | Miller–Rabin / 概率自动机 |
| 分类色 4（密码学 — 玫瑰） | `#C0395B` | Rabin 签名 / 不经意传输 / Rabin–Karp |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和分支节点（稀疏分叉连线），呼应「非确定性：一个状态多条出路」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：回望 / 隽永（从布雷斯劳到耶路撒冷与哈佛的漫长学术旅程）
- **选定曲目**：Alex-Productions **Nostalgia**（manifest 预分配，直接沿用），匹配"九十四载漂泊与回归"的叙事。
- **落地文件**：`turing/presentations/Michael_O._Rabin/Nostalgia.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「非确定性自动机之父 · 以色列」+ 拉宾 1931–2026 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名含希伯来文 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1931–2026 生平纵览
4. **布雷斯劳到海法：拉比之子**（1931–1948）
5. **战火中的大学路**（1948–1949）：入伍与 Fraenkel 说情、希伯来大学 M.Sc.
6. **Princeton：Church 门下**（1956 博士）：群论问题的递归不可解性
7. **Lamb Estate：与 Scott 的 1959 论文**——非确定性机器
8. **McCarthy 谜题与多项式时间**（1960/1966）：复杂度理论之源
9. **概率自动机**（1960，Bell Labs）：掷硬币的状态转移
10. **无限树自动机与 S2S 可判定性**（1969）：parity games determinacy
11. **Miller–Rabin 素性测试**（1975，MIT）：无需广义黎曼假设
12. **密码学三连**（1978/1981/1987）：签名、不经意传输、Rabin–Karp
13. **荣誉满贯**：Israel Prize 1995、Dan David 2010、五院院士
14. **传承**：女儿 Tal Rabin、Harvard + Hebrew University 双聘荣休
15. **结尾**：94 岁、随机算法与密码学的奠基者

## 5. 史实陷阱与敏感点（终审必须检查）

- **共享奖结构**：1976 图灵奖与 **Dana Scott 共享**，且获奖对象是**两人 1959 年合著的一篇论文**（"for a paper written in 1959"）——必须写明；本篇侧重 Rabin 的后续独立工作（复杂度/随机算法/密码学），Scott 篇侧重语义学与逻辑，避免重复；两篇可各引同一 citation 但侧重不同。
- **获奖理由口径**：页面导语写 "for their work on computational complexity"（概述性说法），**ACM citation 原文针对 "Finite Automata and Their Decision Problems" 与非确定性机器**——引用以 citation 原文为准，勿把导语当 citation。
- **论文标题单复数**：Rabin 页与 citation 均作 "Finite Automata and Their Decision **Problems**"（复数），Scott 页 bibliography 作单数 "Problem"——**以 citation/本页为准用复数**，Review 时核对。
- **多项式时间**：1966 年 Rabin 引入，**Cobham 与 Edmonds 独立且稍早**——勿写"Rabin 首创多项式时间"。
- **Miller–Rabin 因果链**：Miller 先行（确定性版本、依赖广义黎曼假设）→ Rabin 版本去掉假设；勿颠倒。
- **不经意传输**：1981 年 Rabin **再造**的是 Wiesner 已发明的技术的弱变体（Wiesner 称 multiplexing）——勿写"Rabin 首创不经意传输"。
- **国籍**：页面无明确 nationality 字段；封面用「以色列」需谨慎（基于希伯来大学/以色列奖/耶路撒冷卒地口径），**勿编造"以色列-美国双重国籍"**。
- **婚姻/家庭**：页面仅载拉比之父与女儿 Tal Rabin；**配偶与婚姻无载，禁写**。
- **死因**：2026-04-14 卒于耶路撒冷，享年 94，**页面未载死因，勿编造**。
- **可引语**：限原文两条——citation 整句、Rabin recall "There was absolutely no appreciation of the work on the issues of computing. Mathematicians did not recognize the emerging new field."、Traub "revolutionary"（转述可）。
- **荣誉**：Israel Prize 1995 是以色列国家级奖（勿写"以色列诺贝尔奖"之类比喻）；Dan David 2010 与 Kleinrock/Gordon Moore 共享，类别 "Future"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 拉宾（或 迈克尔·拉宾） | 待写入 |
| name_en | Michael O. Rabin | 待写入 |
| birth_date | 1931-09-01 | 待写入 |
| death_date | 2026-04-14 | 待写入 |
| nationality | Israel（页面无明确字段，以以色列学术生涯/以色列奖口径为准；Review-1 复核） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | automata theory / computational complexity / randomized algorithms / cryptography | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Alonzo Church（Princeton）
- **关键合作者**：Dana Scott（1959 论文、1976 共享图灵奖）、Richard Karp（Rabin–Karp，1987）、Gary Miller（素性测试基础）
- **合作/激励者**：John McCarthy（间谍谜题）、Edward F. Moore（Bell Labs 邀请）、Joseph Traub（CMU 邀请）
- **著名博士生**：Judit Bar-Ilan、Dov Gabbay、Moshé Machover、Saharon Shelah、Michael A. Bender
- **家庭**：女儿 Tal Rabin（计算机科学家）
- **高中老师**：Elisha Netanyahu（时任海法中学数学教师）
- **说情恩人**：Abraham Fraenkel（数学家，使其退伍入学）

## 8. 奖项清单

- Turing Award（1976，与 Dana Scott 共享）
- Weizmann Prize（1959）
- Harvey Prize（1980）
- Gibbs Lecture（AMS，1985）
- Israel Prize（1995，计算机科学）
- IEEE Computer Society Charles Babbage Award（2000）
- Paris Kanellakis Award（ACM，2003，与 Miller/Solovay/Strassen，素性测试）
- EMET Prize（2004）；Gödel Lecture（2004）
- Dan David Prize（2010，"Future" 类，与 Leonard Kleinrock、Gordon E. Moore 共享）
- Dijkstra Prize（2015）
- Harvard 荣誉理学博士（2017）
- 院士：美国国家科学院（外籍）、美国哲学学会、美国艺术与科学院、法国科学院、英国皇家学会（外籍）

## 9. 机构清单

- 教育：Hebrew Reali School 海法（1948 毕业）、Hebrew University of Jerusalem（BS/MS）、University of Pennsylvania（研究生）、Princeton University（PhD 1956）
- 任职：Hebrew University of Jerusalem（29 岁任数学研究所所长、33 岁正教授、后任 Rector 至 1975）、Bell Labs（1960 访问）、UC Berkeley（1961–62 访问）、MIT（1962–63 与 1975 访问）、Harvard University（1981 起 Gordon McKay Professor，后 Thomas J. Watson Sr. 荣休教授）、Columbia University（2007 春访问）

## 10. 终审清单

- [ ] 生卒 1931-09-01 / 2026-04-14，享年 94，出生地 Breslau（今 Wrocław），去世地 Jerusalem
- [ ] 1976 图灵奖写明"与 Dana Scott 共享、获奖对象为 1959 合著论文"，citation 整句引用无误
- [ ] 多项式时间"独立且稍早有 Cobham/Edmonds"表述准确
- [ ] Miller–Rabin 因果链（Miller 在先、Rabin 去假设）表述准确
- [ ] 不经意传输写"再造 Wiesner 弱变体"，勿写首创
- [ ] 国籍「以色列」口径统一，无双重国籍编造
- [ ] 婚姻无载禁写；家庭仅拉比之父与女儿 Tal Rabin
- [ ] 死因留白（页面未载，勿编造）
- [ ] 封面底部状态栏 `以色列 | Hebrew University · Harvard · Princeton | Turing 1976`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1976/Michael O. Rabin/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-M_O_Rabin.jpg`（取 500px 版）
- [ ] **国籍**：封面顶部徽章明示以色列
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（限 §5 所列）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一（希伯来文字符注意字体覆盖，若缺字可省略希伯来原文）
- [ ] 与同批次（Scott 1976）篇目侧重区分度检查，格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
