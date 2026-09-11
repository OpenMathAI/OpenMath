# Ron Rivest（罗纳德·里维斯特）立传提示词

> qid=Q578036 · 1947-05-06 – 在世留白 · 美国密码学家、计算机科学家 · 20/21 世纪 · 2002 图灵奖（与 Adi Shamir、Leonard Adleman 三人共享）
> 本地 Wikipedia 数据源：`turing/pages/2002/Ron Rivest/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（RSA 公钥体制 / RC 系列对称密码 / MD 哈希族），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ronald Linn Rivest（提示词标题可写 Ronald Rivest；目录/文件名用 `Ron_Rivest`；中文惯称：罗纳德·里维斯特 / 罗恩·里维斯特）
- **生卒**：1947-05-06 生于纽约州斯克内克塔迪（Schenectady, New York，美国）；在世，卒年留白
- **国籍**：美国（American）
- **身份**：密码学家、计算机科学家（MIT Institute Professor）
- **家庭**：妻子 Gail Rivest，两个儿子：Alex Rivest（电影人）、Chris Rivest（创业者、公司联合创始人）
- **教育轨迹**：
  - Yale University **数学**学士（BA，1969）
  - Stanford University **计算机科学**博士（1974），论文 *Analysis of associative retrieval algorithms*（哈希表快速匹配文档中的部分词）
- **博士导师**：Robert W. Floyd（1978 图灵奖得主）
- **研究领域**：密码学、算法与组合数学、机器学习的计算复杂性、选举安全
- **任职**：MIT 电气工程与计算机科学系（EECS）与 CSAIL；MIT 计算理论组成员、CSAIL 密码与信息安全组（CIS）创始人；2015 年 6 月起任 MIT **Institute Professor**（MIT 最高教职）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **RSA 公钥密码体制（1978）**：与 Adi Shamir、Leonard Adleman 在论文 *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*（CACM, 1978）中提出 RSA——**首个可用且公开描述的公钥密码方法**，革命性地改变了现代密码学。【本篇侧重：RSA 提出经过】
2. **酒桌上的灵感（"reportedly"）**：页面载 Rivest 在与 Shamir、Adleman 在学生住处庆祝逾越节、喝了大量葡萄酒之后想出该体制的关键思想——写作时**必须保留 "reportedly"（据传）口径**，勿写成定论。
3. **Alice 与 Bob 的诞生**：同一篇 RSA 论文**首次引入** Alice 和 Bob 两个虚构角色，成为此后无数密码协议的主角——趣味亮点。
4. **同态加密的先声（1978）**：同年与 Adleman、Michael Dertouzos 首次形式化**同态加密**（privacy homomorphisms）及其在安全云计算中的应用——这一想法 40 多年后（2009 Gentry）才真正实现。
5. **对称密码 RC 系列**：RC2、RC4、RC5 的发明者，RC6 的共同发明人（RC5 发表于 1994 FSE；RC2 见 RFC 2268, 1998）。【本篇侧重：对称密码 RC 系列】
6. **MD 哈希族**：MD4（1990, RFC 1186）、MD5（1992, RFC 1321）的设计者，另有 MD2、MD6。
7. **算法大家**：1973 年与 Blum/Floyd/Pratt/Tarjan 发表首个**不依赖随机化**的线性时间选择算法（median of medians，算法课必修）；Floyd–Rivest 算法（1975，随机化选择、接近最优比较次数）；经典教材 *Introduction to Algorithms*（CLRS）四位作者之一（首版 1990，第四版 2022）。
8. **签名与环签名**：GMR 数字签名方案（与 Goldwasser、Micali，1988，抗自适应选择消息攻击）；**环签名**（与 Shamir、Yael Tauman Kalai，2001，论文 "How to Leak a Secret"——匿名的群签名）。
9. **机器学习复杂性**：与 Hyafil 证明最优决策树构造是 NP 完全（1976）；与 Avrim Blum 证明训练 3 节点神经网络是 NP 完全（1992）。
10. **选举安全的晚期事业**：提出**软件独立性**（software independence）原则；2006 年发明 ThreeBallot 端到端可审计投票系统并**放入公有领域**以促进民主；参与 Scantegrity 光学扫描投票安全系统；曾任美国选举协助委员会技术指南发展委员会（TGDC）成员。
11. **创业者的一面**：RSA Data Security（后并入 RSA Security）、Verisign、Peppercoin（密码学微支付系统）三家公司的共同创始人。
12. **其他密码学贡献**：chaffing and winnowing、匿名密钥交换的 interlock 协议、基于摩尔定律的时间胶囊 LCS35、key whitening 与 DES-X。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（公钥密码 — 蓝） | `#2E5A9E` | RSA / Alice 与 Bob |
| 分类色 2（对称密码与哈希 — 青绿） | `#1E8E8E` | RC 系列 / MD 哈希族 |
| 分类色 3（算法 — 琥珀） | `#D9A441` | median of medians / CLRS |
| 分类色 4（选举安全 — 玫瑰） | `#C0395B` | ThreeBallot / 软件独立性 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和几何密文块（稀疏小方块），呼应「公钥/私钥的非对称结构」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：缜密 / 陪伴（密码学家的冷静构造 + 逾越节酒桌上的灵感时刻）
- **选定曲目**：Alex-Productions **With Me**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Ron_Rivest/WithMe.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「RSA 之父 · 美国」+ Rivest 1947– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域 / 家庭）
3. **时间线**（`\timelineslide`）：1947– 生平纵览
4. **早年与教育**：斯克内克塔迪出身、Yale 数学（1969）、Stanford 博士（1974，Floyd 门下，哈希检索）
5. **1977–1978：RSA 的提出经过**：与 Shamir/Adleman 的合作、逾越节酒桌灵感（"reportedly"）、1978 CACM 论文
6. **RSA：首个实用的公钥密码**：数字签名 + 公钥体制、"first usable and publicly described method"、Alice 与 Bob 的诞生
7. **同态加密的先声（1978）**：与 Adleman/Dertouzos 的 privacy homomorphisms、40 年后 Gentry 实现
8. **对称密码 RC 系列**：RC2/RC4/RC5/RC6 一门四杰
9. **MD 哈希族**：MD2/MD4/MD5/MD6
10. **算法与 CLRS**：median of medians（1973）、Floyd–Rivest（1975）、*Introduction to Algorithms*
11. **GMR 签名与环签名**：与 Goldwasser/Micali（1988）、与 Shamir/Tauman（2001）
12. **机器学习的复杂性**：决策树与 3 节点神经网络的 NP 完全
13. **选举安全**：软件独立性、ThreeBallot（公有领域）、Scantegrity、TGDC
14. **荣誉与传承**：Turing 2002、Kanellakis 1996、Marconi 2007、门生 Avrim Blum/Burt Kaliski/Anna Lysyanskaya/Robert Schapire 等
15. **结尾**：在世的密码学宗师——算法、密码、选举三线并进的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖获奖理由（核心红线，整句引用）**：2002 年与 Shamir、Adleman 共享，获奖理由 "for their ingenious contribution to making public-key cryptography useful in practice."——三人篇目**一致**使用此句，勿改写、勿拆分。
- **RSA 论文年份**：RSA 密码体制于 **1978 年**正式发表（CACM 论文）——勿写 1977（1977 是三人当时在 MIT 的提交/传闻年份，页面正文口径为 1978 introduced）。
- **酒桌灵感必须带 "reportedly"**：逾越节葡萄酒轶事页面用 "reportedly" 引出——写作时保留"据传"，勿写成实锤。
- **RC6 是共同发明**：RC2/RC4/RC5 是 Rivest 独自发明，**RC6 是 co-inventor**（与他人合作）——勿写"RC 系列全部独造"。
- **同态加密三人是 Rivest/Adleman/Dertouzos（无 Shamir）**：1978 年 privacy homomorphisms 论文作者为 Rivest、Adleman 与 Dertouzos——与 RSA 三人组是两个不同的组合，勿混。
- **Floyd 导师身份**：博士导师 Robert W. Floyd 本人是 **1978 年图灵奖得主**——可写，但勿展开成"师徒双图灵奖"之类页面无载的渲染。
- **姓氏与目录名**：页面标题为 "Ron Rivest"，全名 Ronald Linn Rivest；目录/文件名用 `Ron_Rivest`，提示词标题写 Ronald Rivest——三处口径需一致注明。
- **在世留白**：1947 年生，在世——死亡日期与死因**完全留白**，勿编造。
- **家庭**：妻子 Gail、儿子 Alex（电影人）与 Chris（创业者）——按页面实载一笔带过，不渲染。
- **ThreeBallot 放入公有领域的原因**："in the interest of promoting democracy"——这是页面实载的动机表述，可引用。
- **门生名单**：以 infobox/正文实载者为准（Avrim Blum、Benny Chor、Sally Goldman、Burt Kaliski、Anna Lysyanskaya、Margrit Betke、Ron Pinter、Robert Schapire、Alan Sherman、Mona Singh、Donna Slonim、Andrea LaPaugh）——勿自行增删。
- **共享结构**：本篇侧重 RSA 提出经过与对称密码 RC 系列；Shamir 秘密共享/密码分析归 Shamir 篇、DNA 计算归 Adleman 篇——三人共同部分（1978 论文、2002 图灵奖、2000 Koji Kobayashi 奖、Kanellakis 1996、共同创立 RSA Security）各篇口径一致，**禁写页面无载的三人内部恩怨**。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 罗纳德·里维斯特（或 罗恩·里维斯特） | 待写入 |
| name_en | Ron Rivest（全名 Ronald Linn Rivest） | 待写入 |
| birth_date | 1947-05-06 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | cryptographer / computer scientist | 待写入 |
| field_of_work | cryptography / algorithms / machine learning / election security | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Robert W. Floyd（Stanford，1978 图灵奖得主）
- **RSA 合作者**：Adi Shamir、Leonard Adleman（1978 论文共同作者、2002 图灵奖共同得主）
- **同态加密合作者**：Leonard Adleman、Michael Dertouzos（1978）
- **签名方案合作者**：Shafi Goldwasser、Silvio Micali（GMR 1988）；Yael Tauman Kalai（环签名 2001）
- **算法合作者**：Manuel Blum、Robert W. Floyd、Vaughan Pratt、Robert E. Tarjan（1973 选择算法）；Thomas H. Cormen、Charles E. Leiserson、Clifford Stein（CLRS）
- **著名博士生**：Avrim Blum、Burt Kaliski、Anna Lysyanskaya、Robert Schapire、Mona Singh 等（以页面实载为准）

## 8. 奖项清单

- Turing Award（2002，与 Shamir/Adleman 共享，"for their ingenious contribution to making public-key cryptography useful in practice."）
- Paris Kanellakis Theory and Practice Award（1996，三人共享）
- IEEE Koji Kobayashi Computers and Communications Award（2000，三人共享）
- Secure Computing Lifetime Achievement Award（三人共享，年份页面未单列）
- MITX Lifetime Achievement Award（2005）
- Marconi Prize / Marconi Fellow（2007）
- BBVA Foundation Frontiers of Knowledge Award（2017）
- National Inventors Hall of Fame（2018）
- 荣誉学位：Sapienza University of Rome（laurea honoris causa）
- 院士/会士：美国国家工程院（NAE）、美国国家科学院（NAS）、ACM Fellow、IACR Fellow、American Academy of Arts and Sciences Fellow

## 9. 机构清单

- 教育：Yale University（数学 BA，1969）、Stanford University（计算机科学 PhD，1974）
- 任职：MIT（EECS / CSAIL，计算理论组成员、CIS 组创始人；2015 年 6 月起 Institute Professor）
- 创业：RSA Data Security（→ RSA Security）、Verisign、Peppercoin

## 10. 终审清单

- [ ] 生卒 1947-05-06 / 在世留白，出生地 Schenectady, New York
- [ ] 图灵奖 2002 与 Shamir/Adleman 共享，理由整句引用无误
- [ ] RSA 论文 1978 年发表（CACM）；Alice 与 Bob 首次出现于该论文
- [ ] 酒桌灵感保留 "reportedly" 口径
- [ ] RC6 为 co-inventor，RC2/RC4/RC5 为独立发明
- [ ] 同态加密 1978 三人为 Rivest/Adleman/Dertouzos（无 Shamir）
- [ ] 博士导师 Floyd、Yale 数学 1969 / Stanford PhD 1974 表述准确
- [ ] ThreeBallot 2006 + 公有领域 + "promoting democracy" 动机表述准确
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | MIT · Yale · Stanford | Turing 2002`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2002/Ron Rivest/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用真实肖像（`images/500px-Ronald_L_Rivest_photo.jpg`，2012 年照，取 500px 版）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由整句、"reportedly" 轶事）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 2002 共享得主（Shamir / Adleman）格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
