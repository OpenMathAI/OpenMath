# Jeffrey Ullman（杰弗里·厄尔曼）立传提示词

> qid=Q92794 · 1942-11-22 –（在世留白）· 美国计算机科学家 · 20/21 世纪 · 2020 图灵奖（与 Alfred Aho 共享）
> 本地 Wikipedia 数据源：`turing/pages/2020/Jeffrey Ullman/`（index.html + metadata.json；**无 images 目录，无肖像**）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。（本人物无肖像 → 装饰圆占位，见 §11）
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地（页面未载→写"页面未载"）、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（数据库理论 / 自动机与语言理论 / 形式语言的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jeffrey David Ullman（中文惯称：杰弗里·厄尔曼）
- **生卒**：1942-11-22 生（**出生地页面未载，勿编造**）→ **在世，卒年留白**
- **国籍**：美国（American）
- **身份**：计算机科学家；Stanford W. Ascherman Professor of Engineering, Emeritus（斯坦福荣休教授）
- **家庭**：页面未载家庭细节，勿编造
- **教育轨迹**：
  - 1963 年 Columbia University **工程数学**学士（BS）
  - 1966 年 Princeton University **电气工程**博士（PhD）；论文 *Synchronization Error Correcting Codes*
- **博士导师**：Arthur Bernstein、Archie McKellar（两位，Princeton）
- **研究领域**：数据库理论、数据库系统、形式语言理论、数据集成、数据挖掘、在线教育

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2020 图灵奖（与 Alfred Aho 共享）**：表彰奠定编程语言编译器与算法的基础；2021-03-31 宣布——**本篇侧重数据库理论奠基 + 龙书合作教学线**，Aho 篇侧重 awk/正则表达式/编译器理论。
2. **龙书合作教学线**：与 Aho 合著 1977 *Principles of Compiler Design*（绿龙）；1986 加入 Ravi Sethi（红龙）；2006 再加入 Monica Lam（紫龙）——Ullman 是三版全部在列的合著者。
3. **灰姑娘书**：*Introduction to Automata Theory, Languages, and Computation*（与 Hopcroft、Motwani；1969/1979/2000 多版）——自动机与语言理论的标准教材。
4. **数据库理论奠基人之一**：页面明言 "one of the founders of the field of database theory"；代表作 *Principles of Database and Knowledge-Base Systems* 两卷（1988/1989）、*A First Course in Database Systems*（与 Widom，1997/2002）、*Database Systems: The Complete Book*（与 Garcia-Molina、Widom，2002）。
5. **1974 算法经典**：与 Aho、Hopcroft 合著 *The Design and Analysis of Computer Algorithms*（与 Aho 篇共享条目，本篇从"教学线"角度一句带过即可）；另有 *Data Structures and Algorithms*（1983）、*Foundations of Computer Science*（与 Aho，1992/1995）。
6. **大规模数据挖掘与在线教育**：*Mining of Massive Datasets*（与 Leskovec、Rajaraman，第二版 2014）；在 Stanford Online 开设 automata 与 mining massive datasets 课程；创办 Gradiance Corporation（高校作业批改平台）；任 TheOpenCode Foundation 顾问委员会成员。
7. **任职轨迹**：Bell Labs 三年（1966–1969）→ Princeton 副教授（1969）/正教授（1974）→ Stanford（1979）→ 系主任（1990–1994）→ W. Ascherman 教授（1994）→ 荣休（2003）。
8. **Sergey Brin 的博士导师**：Google 联合创始人 Sergey Brin 师从 Ullman；Ullman 曾任 Google 技术顾问委员会成员——**勿写"Ullman 参与创办 Google"**。
9. **桃李满门**：页面列出 13 位博士学生（Surajit Chaudhuri、Dan Hirschberg、Anna Karlin、Kevin Karplus、David Maier、Harry Mairson、Alberto O. Mendelzon、Jeffrey F. Naughton、Anand Rajaraman、Yehoshua Sagiv、Ravi Sethi、Mihalis Yannakakis 等），多人成为数据库领域中坚。
10. **荣誉**：IEEE John von Neumann Medal（2010，与 Hopcroft 共获）获奖理由整句可引："For laying the foundations for the fields of automata and language theory and many seminal contributions to theoretical computer science."；Knuth Prize（2000）、ACM Fellow（1994）、C&C Prize（2017，与 Hopcroft、Aho 同获）、NAS 院士（2020）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（数据库理论 — 蓝） | `#2E5A9E` | 数据库理论奠基 / DB 教材 |
| 分类色 2（自动机与语言理论 — 青绿） | `#1E8E8E` | 灰姑娘书 / von Neumann Medal |
| 分类色 3（编译器教材 — 琥珀） | `#D9A441` | 龙书三部曲 |
| 分类色 4（教育与传承 — 玫瑰） | `#C0395B` | 桃李 / Gradiance / Stanford Online |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：规整数据表网格（稀疏细线表格/关系代数符号点缀），呼应「数据库理论与教材」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：明亮 / 昭朗（数据库理论奠基、桃李天下的教学线）
- **选定曲目**：Alex-Productions **Daylight**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Jeffrey_Ullman/Daylight.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「数据库理论奠基人 · 美国」+ Ullman 1942– + 右上装饰圆占位（无肖像）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地·页面未载 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1942–至今 生平纵览
4. **哥伦比亚工程数学起步**（1942–1963）：Columbia BS
5. **Princeton 电气工程博士**（1963–1966）：Bernstein 与 McKellar 门下、纠错码论文
6. **Bell Labs 与 Princeton 任教**（1966–1979）：与 Aho 的长期合作起点
7. **龙书三部曲：编译器教学的圣经**（1977/1986/2006）：Aho–Sethi–Lam 递进
8. **灰姑娘书：自动机与语言理论**（1969/1979/2000）：与 Hopcroft、Motwani
9. **数据库理论的奠基人**：Principles of Database and Knowledge-Base Systems 等三套 DB 教材
10. **斯坦福岁月**（1979–2003）：系主任、Ascherman 讲席、荣休
11. **Brin 的导师与 Google 顾问**：博士导师关系、技术顾问委员会
12. **桃李满门**：13 位博士学生与数据库一代
13. **在线教育与 Gradiance**：Mining of Massive Datasets、Stanford Online
14. **荣誉墙与 2020 图灵奖**（与 Aho 共享）：von Neumann Medal 2010 引语、Knuth 2000、NAS 2020
15. **结尾**：教材塑造两代计算机科学家的遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由**：页面仅载 ACM 新闻标题 *"ACM Turing Award Honors Innovators Who Shaped the Foundations of Programming Language Compilers and Algorithms"*——正文以此口径表述，**勿自行杜撰整句 ACM citation**（与 Aho 篇同一红线）。
- **共享结构**：2020 与 Aho 共享；本篇侧重数据库理论/龙书教学线，Aho 篇侧重 awk/正则/编译器理论；**两人恩怨/分歧页面无载，禁写**。
- **争议段禁写**：页面"Controversies"一节实载 2011 年伊朗学生言论风波与 2021 年 CSForInclusion 公开信、ACM 回应——**属政治敏感内容，立传正文一律禁写**，不渲染不引申。
- **von Neumann Medal 2010**：是与 **John Hopcroft** 共获（非 Aho）——获奖理由整句可引（见亮点 10），勿写错共获人。
- **灰姑娘书 ≠ 龙书**：*Introduction to Automata Theory, Languages, and Computation* 是自动机/语言理论（Hopcroft/Ullman/Motwani）；龙书是编译器（Aho/Ullman/Sethi/Lam）——书名、作者、主题三者勿混。
- **Sergey Brin**：Ullman 是 Brin 的**博士导师**、曾任 Google 技术顾问委员会成员——勿写"共同创办 Google"或"Google 导师"以外的延伸。
- **学位**：Columbia 工程数学 BS（1963）、Princeton **电气工程** PhD（1966）——勿写"计算机科学学位"。
- **出生地页面未载**：身份页写"页面未载"，勿编造。
- **在世**：无卒年，写 `1942–`，留白。
- **Knuth Prize 2000** 属 Ullman（Aho 无此奖），两人荣誉墙勿串。
- **引语**：除 von Neumann Medal 获奖理由整句外，全文无其他直接引语，勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 厄尔曼（或 杰弗里·厄尔曼） | 待写入 |
| name_en | Jeffrey Ullman | 待写入 |
| birth_date | 1942-11-22 | 待写入 |
| death_date | 空（在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | database theory / database systems / formal language theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Arthur Bernstein、Archie McKellar（Princeton，两位）
- **长期合作者**：Alfred Aho（龙书/算法书/Foundations of CS）、John Hopcroft（灰姑娘书/算法书/von Neumann Medal 共获）、Rajeev Motwani（灰姑娘书第三版）
- **龙书新版合著者**：Ravi Sethi（亦为其博士学生）、Monica Lam
- **数据库教材合作者**：Jennifer Widom、Hector Garcia-Molina、Jure Leskovec、Anand Rajaraman（亦为其博士学生）
- **著名博士学生**：Sergey Brin（Google 联合创始人）、Surajit Chaudhuri、Dan Hirschberg、Anna Karlin、Kevin Karplus、David Maier、Harry Mairson、Alberto O. Mendelzon、Jeffrey F. Naughton、Anand Rajaraman、Yehoshua Sagiv、Ravi Sethi、Mihalis Yannakakis
- **C&C Prize 三人组**：John Hopcroft、Alfred Aho（2017 同获）

## 8. 奖项清单

- Turing Award（2020，与 Alfred Aho 共享；2021-03-31 宣布）
- ACM Fellow（1994）
- Knuth Prize（2000）
- IEEE John von Neumann Medal（2010，与 John Hopcroft 共获；理由整句见亮点 10）
- C&C Prize（NEC C&C Foundation，2017，与 Hopcroft、Aho 同获）
- NAS 院士（2020）

## 9. 机构清单

- 教育：Columbia University（工程数学 BS 1963）、Princeton University（电气工程 PhD 1966）
- 任职：Bell Labs（1966–1969，三年）、Princeton University（副教授 1969 / 正教授 1974）、Stanford University（1979 起；系主任 1990–1994；W. Ascherman Professor 1994；Emeritus 2003）；Gradiance Corporation 创始人；TheOpenCode Foundation 顾问委员会

## 10. 终审清单

- [ ] 生卒 1942-11-22 / 在世留白，出生地标注"页面未载"
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Stanford · Princeton · Bell Labs | Turing 2020`
- [ ] 与 Aho 共享 2020 图灵奖，本篇侧重数据库理论/龙书教学线，无两人恩怨内容
- [ ] Controversies（2011/2021）内容未进入立传正文
- [ ] von Neumann Medal 2010 共获人为 Hopcroft，引语整句与原文一致
- [ ] 灰姑娘书与龙书书名/作者/主题未混淆
- [ ] Sergey Brin 表述为"博士导师 + Google 技术顾问委员会"，无"共同创办"延伸
- [ ] 学位：Columbia 工程数学 BS、Princeton 电气工程 PhD，无"CS 学位"误写
- [ ] 无肖像 → 装饰圆占位，封面与身份页不出现虚构头像
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2020/Jeffrey Ullman/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：**无肖像（pages/2020/Jeffrey Ullman/ 无 images 目录）→ 装饰圆占位**，勿用网络图片替代
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅 von Neumann Medal 理由整句可在 Wikipedia 原文找到，其余不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky / John_McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次 Aho 篇格式与侧重对齐（避免整页重复）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
