# Alfred Aho（阿尔弗雷德·阿霍）立传提示词

> qid=Q62898 · 1941-08-09 –（在世留白）· 加拿大计算机科学家 · 20/21 世纪 · 2020 图灵奖（与 Jeffrey Ullman 共享）
> 本地 Wikipedia 数据源：`turing/pages/2020/Alfred Aho/`（index.html + metadata.json；**无 images 目录，无肖像**）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。（本人物无肖像 → 装饰圆占位，见 §11）
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（正则表达式匹配 / Aho–Corasick 自动机 / 索引文法的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Alfred Vaino Aho（中文惯称：阿尔弗雷德·阿霍）
- **生卒**：1941-08-09 生于 Timmins（安大略省，加拿大）→ **在世，卒年留白**
- **国籍**：加拿大（Canadian）——勿写美国人
- **身份**：计算机科学家（programming languages、compilers、算法与教材作者）
- **家庭**：页面未载家庭细节，勿编造
- **教育轨迹**：
  - 1963 年 University of Toronto **工程物理**学士（B.A.Sc.）
  - 1965 年 Princeton University 硕士（M.A.）
  - 1967 年 Princeton University **博士**（Electrical Engineering/Computer Science）；论文 *Indexed Grammars: An Extension of Context Free Grammars*（infobox 论文标注 1968 为 JACM 发表年，勿写"1968 年获博士"）
- **博士导师**：John Hopcroft（1986 图灵奖得主）
- **研究领域**：编程语言、编译器、算法、量子计算（2010 年起的兴趣之一）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2020 图灵奖（与 Jeffrey Ullman 共享）**：表彰两人奠定编程语言编译器与算法的基础；2021-03-31 宣布——与 Ullman 篇明确分工：**本篇侧重 awk/正则表达式/编译器理论**，Ullman 篇侧重数据库理论/合作教学线。
2. **索引文法与嵌套栈自动机（1968 博士论文）**：扩展上下文无关语言的能力、保留可判定性与封闭性质；应用之一是建模并行重写系统（生物应用）。
3. **Bell Labs 正则与字符串匹配（1967–1991）**：设计高效正则表达式与字符串模式匹配算法，实现于 Unix 工具 `egrep` 与 `fgrep` 的最早版本。
4. **Aho–Corasick 算法（1975）**：`fgrep` 的算法，与 Margaret J. Corasick 合著 CACM 论文 *Efficient String Matching: An Aid to Bibliographic Search*——用于书目检索等多种字符串搜索应用。
5. **lex 与 yacc 生态**：与 Steve Johnson、Ullman 共同开发语言分析与翻译算法；Johnson 用自底向上 LALR 分析创建 `yacc`；Michael E. Lesk 与 Eric Schmidt 用 Aho 的正则匹配算法创建 `lex`——lex/yacc 及其衍生工具成为后世编译器前端的基石。
6. **龙书三部曲**：1977 与 Ullman 合著 *Principles of Compiler Design*（封面绿龙，"green dragon book"）；1986 加入 Ravi Sethi 出新版（"red dragon book"，曾在 1995 年电影 *Hackers* 中一闪而过）；2006 再加入 Monica Lam（"purple dragon book"）——大学课程与工业界参考双料标准。
7. **1974 算法经典**：与 Hopcroft、Ullman 合著 *The Design and Analysis of Computer Algorithms*——数十年来 CS 最高引著作之一，推动"算法与数据结构"成为 CS 核心课程。
8. **AWK 语言（1979）**：与 Peter J. Weinberger、Brian Kernighan 合写（AWK 的 "A" 就是 Aho）；1988 出版 *The AWK Programming Language*。
9. **编译理论巨著**：与 Ullman 合著 *The Theory of Parsing, Translation, and Compiling* 两卷（1972/1973）。
10. **任职轨迹**：Bell Labs 1967–1991，1997–2002 回任计算科学研究中央副总裁；1995 年起 Columbia University Lawrence Gussman 讲席教授，1995–1997 任系主任、2003 春季再任。
11. **学术影响**：截至 2019-05-08 论文被引 81,040 次、h-index 66；两度任 NSF CISE 咨询委员会主席、曾任 ACM SIGACT 主席。
12. **荣誉**：IEEE John von Neumann Medal（2003）、NAE 院士（1999，表彰算法与编程工具贡献）、NAS 院士、2017 C&C Prize（NEC，与 Hopcroft、Ullman 三人同获）、多伦多/滑铁卢/赫尔辛基荣誉博士。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（编程语言与编译器 — 蓝） | `#2E5A9E` | 龙书 / 编译理论 |
| 分类色 2（字符串匹配 — 青绿） | `#1E8E8E` | 正则 / Aho–Corasick / egrep·fgrep |
| 分类色 3（教材传承 — 琥珀） | `#D9A441` | 1974 算法书 / 教科书育人线 |
| 分类色 4（Unix 工具文化 — 玫瑰） | `#C0395B` | awk / lex / yacc |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：细密字符流（稀疏竖排短线/字符点阵），呼应「模式匹配与文本处理」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：电影感 / 厚重铺垫（编译器理论奠基、教科书传世）
- **选定曲目**：Alex-Productions **Cinematic Experience**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Alfred_Aho/CinematicExperience.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「编译器理论奠基人 · 加拿大」+ Aho 1941– + 右上装饰圆占位（无肖像）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1941–至今 生平纵览
4. **加拿大少年与多伦多工程物理**（1941–1963）：Timmins 出生、多伦多 B.A.Sc.
5. **Princeton 师从 Hopcroft**（1965–1967）：索引文法 + 嵌套栈自动机
6. **Bell Labs 与 Unix 文本工具**（1967–1991）：egrep / fgrep、正则表达式算法
7. **Aho–Corasick 算法**（1975）：与 Corasick、书目检索
8. **lex 与 yacc：编译器前端的基石**：Johnson / Lesk / Schmidt 与 Aho 算法的关系
9. **龙书三部曲**（1977/1986/2006）：绿→红→紫、Sethi 与 Lam 加入
10. **1974 算法经典**：与 Hopcroft、Ullman 三人组
11. **AWK：以姓氏首字母命名的语言**（1979/1988）：Weinberger、Kernighan
12. **Columbia 岁月**（1995–）：Gussman 讲席、系主任、Bell Labs 副总裁（1997–2002）
13. **荣誉墙**：von Neumann Medal 2003、NAE 1999、C&C 2017 等
14. **2020 图灵奖**（与 Ullman 共享）：编译器与算法基础的"龙书二人组"
15. **结尾**：教科书改变一代程序员的遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：页面仅载 ACM 新闻标题 *"ACM Turing Award Honors Innovators Who Shaped the Foundations of Programming Language Compilers and Algorithms"*——正文以此口径表述（"表彰其对编程语言编译器与算法基础的贡献"），**勿自行杜撰整句 ACM citation**；执行时如需整句，须另行核对 ACM 官方页面。
- **共享结构**：2020 与 Ullman 共享；本篇侧重 awk/正则/编译器理论，Ullman 篇侧重数据库理论——两人篇目避免整页重复；**两人恩怨/分歧页面无载，禁写**。
- **AWK 三作者**：Aho + Peter J. Weinberger + Brian Kernighan，"A" stands for "Aho"——三人缺一不可，勿只写 Aho 或漏 Kernighan。
- **龙书颜色与年份**：1977 绿龙（Aho+Ullman）/ 1986 红龙（+Sethi）/ 2006 紫龙（+Sethi+Lam）；红龙书曾出现于 1995 电影 *Hackers*——年份勿错位。
- **Aho–Corasick**：合作者 **Margaret J. Corasick**；论文署名 Aho, Corasick（1975）——勿写反顺序、勿改性别称呼。
- **lex/yacc 归属**：`yacc` 是 Steve Johnson 用 LALR 创建；`lex` 是 Lesk 与 Eric Schmidt 用 **Aho 的算法**创建——勿把 lex/yacc 的作者都归到 Aho 本人名下。
- **博士年份**：1967（M.A. 1965）；infobox 论文标 1968 是 JACM **发表年**——勿写"1968 年获博士"。
- **国籍**：加拿大人（生于安大略 Timmins）——勿写美国人、勿写"移民美国后改籍"（页面未载）。
- **AAAS 年份冲突**：infobox 作 FAAAS (1986)，正文作"2003 当选 American Academy of Arts and Sciences Fellow"——**两处不一致，以 infobox 1986 为准并在终审核对，勿混写**。
- **在世**：无卒年，写 `1941–`，留白；家庭/死因页面未载勿编造。
- **引语**：全文无直接引语，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 阿霍（或 阿尔弗雷德·阿霍） | 待写入 |
| name_en | Alfred Aho | 待写入 |
| birth_date | 1941-08-09 | 待写入 |
| death_date | 空（在世留白） | 待写入 |
| nationality | Canada | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | programming languages / compilers / algorithms | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：John Hopcroft（Princeton，1986 图灵奖得主）
- **长期合作者**：Jeffrey Ullman（龙书/算法书/文法理论合著）、John Hopcroft（1974 算法书）
- **AWK 合作者**：Peter J. Weinberger、Brian Kernighan
- **Aho–Corasick**：Margaret J. Corasick
- **lex/yacc 生态**：Steve Johnson（yacc）、Michael E. Lesk、Eric Schmidt（lex，用 Aho 算法）、Ravi Sethi、Monica Lam（龙书新版合著者）
- **博士学生**：Krysta Svore
- **C&C Prize 三人组**：John Hopcroft、Jeffrey Ullman（2017 同获）

## 8. 奖项清单

- Turing Award（2020，与 Jeffrey Ullman 共享；2021-03-31 宣布）
- Bell Labs Fellow（1984）
- Fellow of AAAS（American Association for the Advancement of Science，1986）
- IEEE Fellow（1988）
- ACM Fellow（FACM，1996）
- NAE 院士（1999，"contributions to the fields of algorithms and programming tools"）
- IEEE John von Neumann Medal（2003）
- American Academy of Arts and Sciences Fellow（正文作 2003 / infobox 作 1986，两处冲突见 §5）
- Great Teacher Award（Society of Columbia Graduates，2003）
- C&C Prize（NEC C&C Foundation，2017，与 Hopcroft、Ullman 同获）
- NAS 院士（年份页面未载，勿编）
- 荣誉博士：University of Waterloo、University of Helsinki、University of Toronto

## 9. 机构清单

- 教育：University of Toronto（工程物理 B.A.Sc. 1963）、Princeton University（MA 1965 / PhD 1967）
- 任职：Bell Labs（1967–1991；1997–2002 任 Computing Sciences Research Center 副总裁）、Columbia University（1995 年起 Lawrence Gussman 讲席教授；系主任 1995–1997 及 2003 春季）；NSF CISE 咨询委员会主席（两度）、ACM SIGACT 前主席

## 10. 终审清单

- [ ] 生卒 1941-08-09 / 在世留白，出生地 Timmins, Ontario, Canada
- [ ] 国籍用「加拿大」，封面底部状态栏 `加拿大 | Bell Labs · Columbia · Princeton | Turing 2020`
- [ ] 与 Ullman 共享 2020 图灵奖，本篇侧重 awk/正则/编译器理论，无两人恩怨内容
- [ ] AWK 三作者（Aho/Weinberger/Kernighan）齐全
- [ ] 龙书绿(1977)/红(1986)/紫(2006) 年份与作者准确
- [ ] Aho–Corasick 合作者 Margaret J. Corasick 表述准确
- [ ] lex(Lesk/Schmidt)/yacc(Johnson) 归属未张冠李戴
- [ ] 博士 1967（论文发表 1968）、导师 Hopcroft 表述准确
- [ ] AAAS 1986/2003 冲突已按 §5 口径处理
- [ ] 无肖像 → 装饰圆占位，封面与身份页不出现虚构头像
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2020/Alfred Aho/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：**无肖像（pages/2020/Alfred Aho/ 无 images 目录）→ 装饰圆占位**，勿用网络图片替代
- [ ] **国籍**：封面顶部徽章明示加拿大
- [ ] **引语核对**：全文无直接引语，正文中不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky / John_McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次 Ullman 篇格式与侧重对齐（避免整页重复）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
