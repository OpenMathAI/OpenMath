# Leonard Adleman（伦纳德·阿德曼）立传提示词

> qid=Q918650 · 1945-12-31 – 在世留白 · 美国计算机科学家 · 20/21 世纪 · 2002 图灵奖（与 Ron Rivest、Adi Shamir 三人共享）
> 本地 Wikipedia 数据源：`turing/pages/2002/Leonard Adleman/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（RSA / DNA 计算 / APR 素性测试的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Leonard Max Adleman（中文惯称：伦纳德·阿德曼 / 莱纳德·阿德勒曼；昵称 Len）
- **生卒**：1945-12-31 生于旧金山（San Francisco, California，美国）；在世，卒年留白
- **国籍**：美国（American）
- **身份**：计算机科学家（RSA 的 A、"DNA 计算之父"）
- **家庭**：出身犹太家庭；家族原从今白俄罗斯的明斯克（Minsk）地区移民美国；在旧金山长大
- **教育轨迹**：University of California, Berkeley **数学**学士（BA，1968）→ UC Berkeley **EECS** 博士（1976），论文 *Number-Theoretic Aspects of Computational Complexity*
- **博士导师**：Manuel Blum（1995 图灵奖得主）
- **研究领域**：计算机科学、密码学（infobox Fields）
- **任职**：University of Southern California（USC）计算机科学教授（2017 年时仍在任，研究 Strata 的数学理论）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **RSA 的 A（1978）**：RSA 加密算法的三位创造者之一（与 Rivest、Shamir），2002 三人共享图灵奖。【共同部分，与本批次 Rivest/Shamir 两篇口径一致】
2. **"RSA 中的 A" 侧面**：页面正文口径是 "one of the creators of the RSA encryption algorithm"——Adleman 在三人中的角色页面无专述，**勿编造分工细节**；以"三人共同创造"立传。【本篇定位】
3. **DNA 计算之父【本篇侧重支柱】**：1994 年论文 *Molecular Computation of Solutions to Combinatorial Problems*（Science, 266(5187)）首次实验性把 **DNA 用作计算系统**——用 DNA 求解了 7 节点的哈密顿图问题（NP 完全、类似旅行商问题）；虽 7 节点实例的解本身平凡，但这是**已知首次成功用 DNA 执行算法**；被广泛称为 **"Father of DNA Computing"**。
4. **DNA 计算的再进一步（2002）**：其研究组用 DNA 计算求解了一个"非平凡"问题——20 变量 3-SAT 问题（超过 100 万个候选解）：合成逻辑上代表解空间的 DNA 链混合物，用生化技术"淘洗"掉不满足约束的链，测序剩余链即得正确解。
5. **"computer virus" 一词的创造者**：Fred Cohen 在其 1984 年论文 *Experiments with Computer Viruses* 中把 "computer virus" 这一术语归于 Adleman 首创。
6. **Adleman–Pomerance–Rumely 素性测试**：APR 素性测试的原始发现者之一（数论算法贡献，与 RSA 的数论底色呼应）。
7. **好莱坞一面**：电影 *Sneakers*（1992，密码学题材）的数学顾问。
8. **拳台上的教授**：业余拳击手，曾与世界冠军 James Toney 过招（sparred）——趣味亮点，一笔带过。
9. **学术荣誉**：1996 年因计算理论与密码学贡献当选美国国家工程院（NAE）院士；亦为美国国家科学院（NAS）院士；2006 年当选 American Academy of Arts and Sciences Fellow；2021 年 ACM Fellow。
10. **共享荣誉**：与 Rivest、Shamir 共享 1996 Paris Kanellakis Theory and Practice Award 与 2002 Turing Award（页面把图灵奖描述为 "often called the Nobel Prize of Computer Science"——可按页面口径引用）。
11. **晚期研究**：截至 2017 年致力于 **Strata 的数学理论**。
12. **奖项清单之薄**：infobox Awards 仅列 Turing Award——本篇荣誉页以正文实载为准（Kanellakis 1996、NAE 1996、NAS、AAAS 2006、ACM Fellow 2021），**勿自行补写其他奖项**。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（公钥密码 RSA — 蓝） | `#2E5A9E` | RSA 的 A / Kanellakis 奖 |
| 分类色 2（DNA 计算 — 青绿） | `#1E8E8E` | 1994 Science 论文 / 2002 3-SAT |
| 分类色 3（数论与算法 — 琥珀） | `#D9A441` | APR 素性测试 / 计算复杂性 |
| 分类色 4（文化切面 — 玫瑰） | `#C0395B` | computer virus 术语 / Sneakers / 拳台 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和双螺旋链段（稀疏曲线链），呼应「DNA 作为计算介质」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：实验 / 破界（从数论密码到 DNA 试管的跨界人生）
- **选定曲目**：Alex-Productions **Cinematic Experience**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Leonard_Adleman/CinematicExperience.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「RSA 的 A · DNA 计算之父 · 美国」+ Adleman 1945– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 家庭渊源 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1945– 生平纵览
4. **早年与教育**：旧金山犹太家庭、明斯克移民渊源、Berkeley 数学（1968）与 EECS 博士（1976）
5. **Blum 门下**：博士导师 Manuel Blum（1995 图灵奖）、数论与计算复杂性
6. **RSA 的 A（1978）**：与 Rivest/Shamir 的合作、"one of the creators"
7. **APR 素性测试**：数论算法贡献、RSA 的数论底色
8. **1994：DNA 计算诞生**：Science 论文、7 节点哈密顿图、"Father of DNA Computing"
9. **2002：DNA 求解 3-SAT**：20 变量、百万候选解、生化淘洗
10. **"computer virus" 的命名者**：Fred Cohen 1984 论文的 credit
11. **好莱坞与拳台**：Sneakers 数学顾问、与 James Toney 过招
12. **荣誉之殿**：Turing 2002、Kanellakis 1996、NAE/NAS/AAAS/ACM Fellow
13. **晚期研究**：Strata 的数学理论（2017 在任 USC）
14. **三人组对照页**：Rivest（RC 系列/算法）· Shamir（密码分析/秘密共享）· Adleman（DNA 计算/数论）——共享与侧重
15. **结尾**：在世的跨界者——密码学家、计算生物学家、命名者的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖获奖理由（核心红线，整句引用）**：2002 年与 Rivest、Shamir 共享，获奖理由 "for their ingenious contribution to making public-key cryptography useful in practice."（Rivest 篇页面口径）——三人篇目**一致**，勿改写。Adleman 本页对图灵奖的补充口径是 "often called the Nobel Prize of Computer Science"——可引用但注明这是页面表述。
- **RSA 分工勿编造**：页面只说 Adleman 是 "one of the creators"——**RSA 三人内部分工（谁提思路/谁验证）页面无载，禁写**；"RSA 中的 A" 只作篇目定位语，不作史实断言。
- **DNA 计算首例的定位**：7 节点哈密顿图实例的解是 trivial 的，页面明说 "While the solution to a seven-node instance is trivial, this paper is the first known instance of the successful use of DNA to compute an algorithm"——**必须保留"解平凡但首例"的双重表述**，勿吹成"用 DNA 解决了难题"。
- **哈密顿图 ≠ 旅行商**：页面口径是 "an NP-complete problem similar to the travelling salesman problem"——是"类似的 NP 完全问题"，勿写成同一问题。
- **"computer virus" 归属**：是 **Fred Cohen 1984 年论文 credit 给 Adleman**（coining the term）——写作时带上"由 Cohen 记载归于 Adleman"的转述口径，勿写成 Adleman 自己发表论文定义病毒。
- ** boxer 轶事**："amateur boxer and has sparred with James Toney"——sparred（过招/陪练）勿升级为"比赛战胜"。
- **家庭渊源**：犹太家庭、祖辈来自明斯克地区（今白俄罗斯）——按页面实载一笔带过，不渲染。
- **奖项之薄是事实**：infobox Awards 仅 Turing Award；正文另有 Kanellakis 1996（三人共享）、NAE 1996、NAS 院士、AAAS Fellow 2006、ACM Fellow 2021——**勿自行增补页面无载的奖项**（如 Japan Prize/Wolf 等 Shamir 篇的奖项严禁串写）。
- **在世留白**：1945-12-31 生，在世——死亡日期与死因完全留白。
- **引语红线**：全文无直接引语——**勿编造任何 Adleman 名言**。
- **共享结构**：本篇侧重 DNA 计算与"RSA 中的 A"侧面；RSA 提出经过/RC 系列归 Rivest 篇、秘密共享/密码分析归 Shamir 篇；三人共同部分口径一致，**禁写页面无载的三人内部恩怨**。
- **页面质量提示**：本条目 Wikipedia 自带 "relies excessively on primary sources" 模板（2020-05）——Review-1 时对每条事实从严核对，宁缺勿错。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 伦纳德·阿德曼 | 待写入 |
| name_en | Leonard Adleman（全名 Leonard Max Adleman） | 待写入 |
| birth_date | 1945-12-31 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / cryptography / DNA computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Manuel Blum（UC Berkeley，1995 图灵奖得主）
- **RSA 合作者**：Ron Rivest、Adi Shamir（1978 论文共同作者、2002 图灵奖共同得主）
- **同态加密合作者**：Ron Rivest、Michael Dertouzos（1978 privacy homomorphisms——见 Rivest 篇口径）
- **素性测试合作者**：Carl Pomerance、H. W. Lenstra Jr.（APR/ cyclotomy 谱系——**页面仅写 "Adleman–Pomerance–Rumely primality test"，合作者姓名以该测试命名实载为准；Rumely 名字页面未展开，勿自行补全称，Review 时核实**）
- **术语传承**：Fred Cohen（1984 论文 credit "computer virus" 术语）
- **博士生**：页面无载——**禁写**

## 8. 奖项清单

- Paris Kanellakis Theory and Practice Award（1996，与 Rivest/Shamir 共享）
- Turing Award（2002，与 Rivest/Shamir 共享，"often called the Nobel Prize of Computer Science" 为页面表述）
- National Academy of Engineering 院士（1996，"for contributions to the theory of computation and cryptography"）
- National Academy of Sciences 院士（年份页面未载）
- American Academy of Arts and Sciences Fellow（2006）
- ACM Fellow（2021）

## 9. 机构清单

- 教育：University of California, Berkeley（数学 BA 1968；EECS PhD 1976）
- 任职：University of Southern California（USC）计算机科学教授（截至 2017 在任）
- 其他：电影 *Sneakers* 数学顾问

## 10. 终审清单

- [ ] 生卒 1945-12-31 / 在世留白，出生地 San Francisco
- [ ] 图灵奖 2002 与 Rivest/Shamir 共享，理由整句引用无误
- [ ] DNA 计算 "7 节点实例解平凡、但为已知首例" 双重表述准确
- [ ] 2002 年 DNA 3-SAT：20 变量、超百万候选解表述准确
- [ ] "computer virus" 术语经 Fred Cohen 1984 论文 credit
- [ ] RSA 三人分工无编造、页面无载的内部恩怨禁写
- [ ] 博士导师 Manuel Blum、Berkeley 数学 1968 / EECS 1976 表述准确
- [ ] 奖项清单未超出页面实载范围
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | USC · UC Berkeley | Turing 2002`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2002/Leonard Adleman/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实（注意本条目自带 primary sources 质量模板，从严核对）
- [ ] **头像**：使用真实肖像（`images/500px-Len-mankin-pic.jpg`，取 500px 版；`Question_book-new.svg` 系质量模板图标，**非肖像禁用**）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：全文无直接引语，勿编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 2002 共享得主（Rivest / Shamir）格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
