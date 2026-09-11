# Manuel Blum（曼努埃尔·布卢姆）立传提示词

> qid=Q92626 · 1938-04-26 – 在世留白 · 委内瑞拉出生的美国计算机科学家（计算复杂性理论 / 密码学）· 20 世纪 · 1995 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1995/Manuel Blum/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 委内瑞拉裔·美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Blum 公理 / 加速定理 / Blum Blum Shub 伪随机性的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Manuel Blum（中文惯称：曼努埃尔·布卢姆）
- **生卒**：1938-04-26 生于 Caracas, Venezuela（加拉加斯，委内瑞拉）→ **在世留白**
- **国籍**：委内瑞拉出生的美国计算机科学家（Venezuelan-born American）
- **身份**：计算复杂性理论奠基人之一、理论密码学先驱、传奇博导
- **家庭**：委内瑞拉犹太家庭（页面明载 born to a Jewish family in Venezuela）；**妻子 Lenore Blum**（数学家、CMU 计算机科学教授）；**儿子 Avrim Blum**（计算机科学家）——三人 1973 年合影即本篇肖像来源；2018 年与妻子一同从 CMU 辞职（见 §5 口径）
- **教育轨迹**（MIT 一步到底）：
  - 1959 年 **电气工程**学士（BS）
  - 1961 年 **电气工程**硕士（MS）
  - 在 MIT 期间被引荐给 **Warren S. McCulloch**，合作研究神经网络中的若干数学问题（1961 年 "Properties of a neuron with many inputs"）
  - 1964 年 **数学**博士，导师 Marvin Minsky（1969 图灵奖得主）——论文 *A Machine-Independent Theory of the Complexity of Recursive Functions*
- **博士导师**：Marvin Minsky（Minsky 篇 §7 已列 Blum 为门生，两人篇目互证）
- **研究领域**：计算复杂性理论、密码学、程序检验、归纳推理

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **1995 图灵奖（独得）**：获奖理由整句引用 "In recognition of his contributions to the foundations of computational complexity theory and its application to cryptography and program checking"——表彰其**对计算复杂性理论基础的贡献及其在密码学与程序检验中的应用**。
2. **机器无关的复杂性理论（1960s）**：基于 **Gödel 编号（Gödel numberings）与 Blum 公理**建立**不依赖具体机器模型的公理化复杂性理论**——本篇核心页。
3. **公理化的 Concrete 结果**：尽管不基于任何机器模型，该理论产出压缩定理（compression theorem）、间隙定理（gap theorem）、诚实性定理（honesty theorem）与 **Blum 加速定理（Blum speedup theorem）**——"从抽象公理到具体定理"的叙事主线。
4. **中位数的中位数（1973）**：与 Floyd、Pratt、Rivest、Tarjan 合著 *Time bounds for selection*——**线性时间选择算法**（median of medians），五位巨头合署的算法经典。
5. **Blum Blum Shub（1986）**：与 Lenore Blum、Michael Shub 合著 *A Simple Unpredictable Pseudo-Random Number Generator*——以两代 Blum 姓氏命名的伪随机数生成器，理论密码学基石之一。
6. **密码学一整廊**：Blum 整数（Blum integer）、**Blum–Goldwasser 密码系统**、**Blum–Micali 算法**、承诺方案（commitment scheme）、**电话掷硬币协议**（coin flipping over a telephone）——"用复杂性假设换密码学安全"的群像页。
7. **CAPTCHA 与 reCAPTCHA（2003）**：与门生 Luis von Ahn 等合著 *CAPTCHA: Using Hard AI Problems for Security*（EUROCRYPT 2003）——**把困难 AI 问题变成安全工具**； Known for 列表含 CAPTCHA 与 reCAPTCHA。
8. **归纳推理理论（1975）**：与 Lenore Blum 合著 *Toward a mathematical theory of inductive inference*（Information and Control）——夫妻合作的归纳推理数学理论。
9. **传奇博导**：博士生名单横跨计算生物学、密码学、复杂性、算法——**Leonard Adleman**（RSA）、**Shafi Goldwasser 与 Silvio Micali**（2012 图灵奖）、Michael Sipser、Gary Miller、Umesh/Vijay Vazirani、Moni Naor、Russell Impagliazzo、Steven Rudich、Ronitt Rubinfeld、Dana Angluin、Jeffrey Shallit、Mor Harchol-Balter、**Luis von Ahn**（reCAPTCHA/Duolingo）、**Ryan Williams** 等——"门下已出 4+ 位图灵奖级谱系"的师承叙事（Adleman/Goldwasser/Micali/von Ahn 相关荣誉按各自页面，勿在本篇写"图灵奖门生人数"，只列名）。
10. **三大教学奖**：UC Berkeley Distinguished Teaching Award（1977）、Sigma Xi Monie A. Ferst Award（1991）、CMU Herbert A. Simon Teaching Award（2007）——"教学与科研同辉"。
11. **双院院士**：2002 年入选美国国家科学院（NAS）、2006 年入选国家工程院（NAE，理由：抽象复杂性理论、归纳推理、密码协议、程序检验器理论与应用）。
12. **Berkeley → CMU → 辞职（2018）**：UC Berkeley 计算机科学教授至 2001；2001–2018 任 CMU Bruce Nelson 讲席教授（与 Lenore 同校执教）；2018 年因 Project Olympus 管理结构变更导致对妻子（时任总监）的性别歧视待遇及排挤其他女性，与 Lenore 一同辞职抗议——**按页面实载一句带过**。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（公理复杂性 — 蓝） | `#2E5A9E` | Blum 公理 / 加速定理 / 间隙定理 |
| 分类色 2（理论密码学 — 青绿） | `#1E8E8E` | BBS / Blum–Goldwasser / 电话掷硬币 |
| 分类色 3（算法 — 琥珀） | `#D9A441` | median of medians / 线性时间选择 |
| 分类色 4（人机验证与教育 — 玫瑰） | `#C0395B` | CAPTCHA / reCAPTCHA / 三大教学奖 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：嵌套同心方块（层层抽象向上收敛），呼应「公理化复杂性——从公理层生成本体定理」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：恒久 / 抽象（公理之上，时间之外）
- **选定曲目**：Alex-Productions **Timeless**（深邃 / 恒常），匹配"机器无关、时间无关的公理化理论"气质（与 Wilkins 篇同曲，属批次正常复用）。
- **落地文件**：`turing/presentations/Manuel_Blum/Timeless.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「计算复杂性理论奠基人 · 委内瑞拉裔·美国」+ Blum 1938– + 右上头像（1973 全家合影）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1938– 生平纵览（Caracas→MIT→Berkeley→CMU）
4. **加拉加斯到 MIT（1938–1959）**：委内瑞拉犹太家庭、电气工程本科
5. **McCulloch 与神经网络（1959–1961）**：硕士期间的神经数学、多输入神经元模型（1961）
6. **Minsky 门下博士（1961–1964）**：机器无关复杂性理论论文——与导师 Minsky 篇互证的师承页
7. **Blum 公理与加速定理**（本篇核心页，公式框）：Gödel 编号、公理化、压缩/间隙/诚实性定理
8. **线性时间选择（1973）**：与 Floyd/Pratt/Rivest/Tarjan 的 median of medians
9. **夫妻合作的归纳推理（1975）**：与 Lenore Blum 的数学理论
10. **Blum Blum Shub（1986）**：三代姓氏的伪随机生成器、密码学一整廊（Blum–Goldwasser/Blum–Micali/电话掷硬币/承诺方案）
11. **CAPTCHA：用难题筑防线（2003）**：与 von Ahn、把困难 AI 问题变成安全工具
12. **传奇博导**：Adleman/Goldwasser/Micali/Sipser/von Ahn/Williams 谱系墙 + 三大教学奖
13. **Berkeley–CMU 双院岁月**：NAS 2002 / NAE 2006、2018 与 Lenore 辞职（一句带过）
14. **遗产**：复杂性理论、密码学、程序检验的三重奠基
15. **结尾**：品牌页 OpenMathAI

## 5. 史实陷阱与敏感点（终审必须检查）

- **在世留白**：Blum **在世**（1938-04-26 生，页面无卒日）——时间线与结尾页写 `1938–`，勿写卒年。
- **肖像即全家福**：infobox 图为 **1973 年 Manuel（左）与妻子 Lenore、儿子 Avrim 的合影**（Blum_manuel_lenore_avrim.jpg）——封面使用时**图注必须写明"1973 年与妻子 Lenore、儿子 Avrim 合影"**，勿伪装成个人单人肖像；无单人照可用，**不做装饰圆替换**（真实照片优先）。
- **"唯一拉美裔图灵奖得主"禁写**：页面脚注引用的西语报道标题称其为 "el único latinoamericano en ganar el Premio Turing"（唯一拉美裔图灵奖得主）——**这是报道标题、非页面正文叙述**，正文未载此断言——**禁写**（如需提，只能加"有报道称"存疑注记，建议干脆不写）。
- **Blum 整数定义禁展开**：infobox 与正文均列名 "Blum integer"——**页面无载定义**（两素数乘积 ≡3 mod 4 之类的细节）——只列名勿定义。
- **BBS 细节口径**：写"与 Lenore Blum、Michael Shub 合著（1986）、Simple Unpredictable Pseudo-Random Number Generator"——**二次剩余/模数结构等技术细节页面无载勿展开**。
- **CAPTCHA vs reCAPTCHA**：论文页（2003 EUROCRYPT，与 von Ahn/Hopper/Langford）为 CAPTCHA；**reCAPTCHA 仅出现在 Known for 列表**——写"Known for 含 CAPTCHA 与 reCAPTCHA"，勿展开 reCAPTCHA 演变史/谷歌收购（页面无载）。
- **2018 辞职事件**：页面实载（Project Olympus 管理变更、对 Lenore 的性别歧视待遇、其他女性被排除、夫妻双双辞职抗议）——**一句带过、不渲染、不加评论**，归入 CMU 岁月页末或荣誉页注脚。
- **师承谱系**：博士导师 **Marvin Minsky**；MIT 硕士期间与 **Warren S. McCulloch** 合作——**McCulloch 是合作者/引荐人，不是博士导师**（页面写 "recommended to ... and they collaborated"，勿写成导师）。
- **学位口径**：MIT BS EE 1959 / MS EE 1961 / **数学** PhD 1964——本科硕士是电气工程、博士是数学，勿混写。
- **引语红线**：全文可用直接引语仅获奖理由整句一条——**无其他直接引语，勿编造**。
- **荣誉**：Turing 1995、Berkeley Distinguished Teaching 1977、Sigma Xi Monie A. Ferst 1991、Simon Teaching Award 2007、NAS 2002、NAE 2006——**仅此六项**，无其他奖章（勿编造）。
- **家庭篇幅**：Lenore 与 Avrim 按页面实载写入（夫妻合作论文/BBS 合著/同校执教/2018 同辞职；Avrim 为儿子、计算机科学家）——**不渲染家庭故事**，合作事实为纲。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 布卢姆（或 曼努埃尔·布卢姆） | 待写入 |
| name_en | Manuel Blum | 待写入 |
| birth_date | 1938-04-26 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States（Venezuela-born） | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computational complexity theory / cryptography / program checking | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Marvin Minsky（MIT，1969 图灵奖得主）
- **合作者**：Warren S. McCulloch（神经网络数学问题）、R. W. Floyd / V. R. Pratt / R. L. Rivest / R. E. Tarjan（1973 选择算法）、Lenore Blum（妻，1975 归纳推理、1986 BBS 合著）、Michael Shub（BBS 合著）、Silvio Micali（Blum–Micali）、S. Goldwasser（Blum–Goldwasser）、Luis von Ahn / N. J. Hopper / J. Langford（CAPTCHA 2003）
- **著名博士生**（页面全列 18 人，入库取页面 infobox 名单）：Leonard Adleman、Dana Angluin、C. Eric Bach、Shafi Goldwasser、Mor Harchol-Balter、Russell Impagliazzo、Silvio Micali、Gary Miller、Moni Naor、Ronitt Rubinfeld、Steven Rudich、Jeffrey Shallit、Michael Sipser、Umesh Vazirani、Vijay Vazirani、Luis von Ahn、Ryan Williams
- **家庭关系**：spouse=Lenore Blum（数学家/CMU 教授）、parent-child=Avrim Blum（子，计算机科学家）——页面实载可入库。

## 8. 奖项清单

- ACM A.M. Turing Award（1995）
- Distinguished Teaching Award, UC Berkeley（1977）
- Sigma Xi Monie A. Ferst Award（1991）
- Herbert A. Simon Teaching Award, CMU（2007）
- United States National Academy of Sciences 院士（2002）
- National Academy of Engineering 院士（2006，理由：abstract complexity theory, inductive inference, cryptographic protocols, and the theory and applications of program checkers）

## 9. 机构清单

- 教育：Massachusetts Institute of Technology（BS EE 1959、MS EE 1961、PhD math 1964）
- 任职：University of California, Berkeley（计算机科学教授，至 2001）、Carnegie Mellon University（Bruce Nelson Professor of Computer Science，2001–2018；2018 与 Lenore 一同辞职）

## 10. 终审清单

- [ ] 生卒 1938-04-26 / 在世留白，出生地 Caracas, Venezuela
- [ ] 1995 独得图灵奖，获奖理由整句引用准确
- [ ] 肖像为 1973 全家合影，图注写明三人身份
- [ ] "唯一拉美裔图灵奖得主"禁写合规
- [ ] Blum 整数/reCAPTCHA 只列名不展开
- [ ] Blum 公理 + 四定理（压缩/间隙/诚实性/加速）表述准确
- [ ] McCulloch 写"合作者"非导师；博士导师 Minsky
- [ ] 2018 辞职一句带过不渲染
- [ ] 国籍用「委内瑞拉裔·美国」，封面底部状态栏 `委内瑞拉裔·美国 | MIT · UC Berkeley · CMU | Turing 1995`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1995/Manuel Blum/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Blum_manuel_lenore_avrim.jpg`（1973 全家合影，最大可用版）——**核对图注写明三人**；页面无单人照，勿用装饰圆替换
- [ ] **国籍**：封面顶部徽章明示委内瑞拉裔·美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅获奖理由一条）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Hartmanis / Stearns / Feigenbaum / Reddy）格式对齐；门生墙页与 Minsky 篇"门生 Manuel Blum"互证

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
