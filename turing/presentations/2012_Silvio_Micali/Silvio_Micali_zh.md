# Silvio Micali（西尔维奥·米卡利）立传提示词

> qid=Q93080 · 1954-10-13 – 在世留白 · 意大利计算机科学家 · 20/21 世纪 · 2012 图灵奖（与 Shafi Goldwasser 共享）
> 本地 Wikipedia 数据源：`turing/pages/2012/Silvio Micali/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（语义安全 / 伪随机生成 / 零知识证明的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Silvio Micali（中文惯称：西尔维奥·米卡利）
- **生卒**：1954-10-13 生于巴勒莫（Palermo，意大利）→ 在世留白
- **国籍**：意大利（Italian）
- **身份**：计算机科学家、密码学家；MIT 电气工程与计算机科学系教授（1983 起）、MIT CSAIL 研究者；Algorand 创始人（PoS 区块链协议）
- **家庭**：页面无家庭细节载录——**禁写**
- **教育轨迹**：
  - Sapienza University（罗马一大）**数学** BS（1978，页面原文 "graduated in mathematics at La Sapienza University of Rome"）
  - UC Berkeley **计算机科学** PhD（1982），论文 *Randomness versus Hardness*
- **博士导师**：Manuel Blum（1995 图灵奖得主——与 Goldwasser 同门，师徒双图灵奖，可写）
- **研究领域**：密码学、零知识、伪随机生成、安全协议、机制设计、信息安全

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 2012（与 Goldwasser 共享）**：页面表述 "for their work in the field of cryptography"（密码学领域的工作）；页面另载定位句 "The Turing Award is considered the Nobel Prize of computing"（图灵奖被视为计算界的诺贝尔奖）。
2. **可证明安全传统（与 Goldwasser 共同奠基）**：两人作为 Berkeley 研究生共同开创的概率加密传统，使密码学从工程技艺变为可数学证明的科学——共享叙事但本篇侧重 Micali 视角（见 §5 分工红线）。
3. **概率加密与语义安全（与 Goldwasser）**：一条消息可随机加密成多个不同密文；即使攻击者可选择明文，两个密文也**不可区分**（indistinguishable）——"semantic security"（语义安全）是 Micali 篇的关键词（infobox Known for 有载）。
4. **Blum–Micali 算法（与导师 Blum）**：研究生期间与 Blum 共同开发的**伪随机数生成器**——密码学伪随机性的基石；infobox Known for 有载。
5. **交互式证明与零知识证明（与 Goldwasser、Rackoff）**：1980s 与 Goldwasser、Rackoff 发明交互式证明（与 Babai–Moran 同期独立）；1985 年引入其特类**零知识证明**——证明者与验证者交互证明定理而不泄露额外知识。
6. **公开密钥基础设施的早期工作**：公钥密码系统、**数字签名**、**不经意传输（oblivious transfer）**、**安全多方计算（secure multiparty computation）**、伪随机函数、claw-free permutation、可验证秘密分享（verifiable secret sharing）、GMR 算法——infobox Known for 全列表，择要分页。
7. **三度创业**：CoreStreet Ltd（2001 年联合创立，剑桥市，数字证书状态检查专利，任 Chief Scientist，2009 年被 ActivIdentity 收购）→ Peppercoin（2000s 初的微支付系统，2007 年被收购）→ **Algorand**（2017 年创立的 PoS 区块链加密货币协议）——理论家企业家线。
8. **多国教职**：MIT EECS（1983 起）为主；曾在 University of Pennsylvania、University of Toronto、**清华大学（Tsinghua University）**任教——infobox 任职有载。
9. **荣誉**：Gödel Prize 1993（与 Goldwasser/Rackoff/Babai/Moran）、RSA 数学卓越奖 2004、NAS 院士 2007、IACR Fellow 2007、NAE 院士、American Academy of Arts and Sciences 院士、University of Salerno 荣誉学位 2015、ACM Fellow 2017。
10. **门生成林**：Mihir Bellare、Bonnie Berger、Alessandro Chiesa、Claude Crépeau、Shai Halevi、Rafail Ostrovsky、Phillip Rogaway——现代密码学中坚（页面明载）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（语义安全 — 蓝） | `#2E5A9E` | 概率加密 / 不可区分性 / Goldwasser–Micali 密码系统 |
| 分类色 2（伪随机性 — 青绿） | `#1E8E8E` | Blum–Micali 算法 / 伪随机函数 |
| 分类色 3（零知识与协议 — 琥珀） | `#D9A441` | 零知识证明 / 数字签名 / 安全多方计算 |
| 分类色 4（创业与区块链 — 玫瑰） | `#C0395B` | CoreStreet / Peppercoin / Algorand |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「密文不可区分、证明不泄密」的零知识视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：进取 / 开拓（从巴勒莫到 MIT，从理论证明到区块链创业）
- **选定曲目**：Alex-Productions **Expedition**（manifest 预分配，直接沿用；与 1999 't Hooft 等同曲属正常复用）。
- **落地文件**：`turing/presentations/Silvio_Micali/Expedition.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「密码学可证明安全 · 意大利」+ Micali 1954– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1954–在世 生平纵览
4. **早年：巴勒莫与罗马一大**（1954–1978）：南意岛城、数学本科
5. **Berkeley 与 Manuel Blum**（1978–1982）：Randomness versus Hardness 博士论文、随机性对困难性
6. **Blum–Micali 算法**：与导师合作的伪随机数生成器
7. **概率加密与语义安全**（与 Goldwasser）：一消息多密文、不可区分性
8. **交互式证明与零知识证明**（与 Goldwasser、Rackoff，1985）：证明而不泄露
9. **密码学协议全景**：数字签名 / 不经意传输 / 安全多方计算 / 可验证秘密分享
10. **Gödel Prize 1993**：交互式证明的双组平行与共享
11. **MIT 教授与多国讲席**（1983–）：CSAIL、Penn/Toronto/清华
12. **三度创业**：CoreStreet（2001，→ActivIdentity 2009）、Peppercoin（→2007）、Algorand（2017）
13. **荣誉与传承**：Turing 2012、RSA 2004、NAS/NAE 院士；门生 Bellare/Rogaway/Halevi/Chiesa 等
14. **遗产**：可证明安全的数学化、密码学走向区块链时代
15. **结尾**：在世、"计算界的诺贝尔奖"与 Algorand 的当下

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由口径与 Goldwasser 篇不同**：Micali 页面无独立 ACM citation 整句，仅有 "for their work in the field of cryptography"——本篇用该句 + Goldwasser 篇的 provable security 完整 citation 可在"共享结构"处出现一次；**勿把 Goldwasser citation 当作 Micali 页面原文**（写"两人共享的完整颁奖理由为……"即可）。
- **零知识证明是三人成果**：1985 年论文作者 Goldwasser + Micali + **Charles Rackoff**——三人署名完整，勿写两人发明。
- **交互式证明双组平行**：Micali/Goldwasser/Rackoff 与 **Babai/Moran** 同期独立发表（页面明载 "at the same time as"）——共享 1993 Gödel Prize，勿写单方发明。
- **与 Goldwasser 篇的叙事分工**（避免重复）：Micali 篇侧重——Blum–Micali 伪随机生成器、语义安全/不可区分性、数字签名/安全多方计算/不经意传输等协议全景、三度创业（CoreStreet/Peppercoin/Algorand）、清华教职；Goldwasser 篇专属——PCP 定理/难近似性、椭圆曲线素性测试、Duality/Simons 所长/Project CETI、女性科学奖线。
- **Algorand 表述**：2017 年创立，"a proof-of-stake blockchain cryptocurrency protocol"——是"创始人"（页面明载 founder）；Goldwasser 只是其科学顾问——勿写 Goldwasser 共同创立 Algorand。
- **Peppercoin 收购年**：2007 被收购；CoreStreet 2009 被 ActivIdentity 收购——两个年份勿互换。
- **清华教职**：infobox Institutions 有载 Tsinghua University（"has also served on the faculty of ... Tsinghua University"）——可写"曾在其任教"，**勿编造具体年份/职务**。
- **NIZK（Blum-Feldman-Micali 1988 非交互零知识）**：仅出现在页面参考文献题名中，正文未叙述——**不展开**（如需提及写"另在参考文献可见其 1988 年非交互零知识工作"或直接不写）。
- **在世**：死亡日期留白，生卒写 `1954–`。
- **家庭**：页面无载，**禁写**。
- **引语**：正文**无本人直接引语**（页面仅有叙事句与 "Nobel Prize of computing" 定位句）；勿编造。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 西尔维奥·米卡利 | 待写入 |
| name_en | Silvio Micali | 待写入 |
| birth_date | 1954-10-13 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Italy | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | cryptography / zero-knowledge proofs / pseudorandomness / secure protocols / blockchain | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Manuel Blum（Berkeley，1995 图灵奖得主）
- **核心合作者**：Shafi Goldwasser（概率加密/零知识/Gödel 1993/图灵 2012 共享）、Charles Rackoff（零知识证明 1985）、Manuel Blum（Blum–Micali 算法）
- **Gödel Prize 共享者**：Goldwasser、Rackoff、Babai、Moran（1993）
- **著名博士生**：Mihir Bellare、Bonnie Berger、Alessandro Chiesa、Claude Crépeau、Shai Halevi、Rafail Ostrovsky、Phillip Rogaway
- **页面无载的关系**：禁写

## 8. 奖项清单

- A.M. Turing Award（2012，与 Shafi Goldwasser 共享，"for their work in the field of cryptography"）
- Gödel Prize（1993，与 Goldwasser/Rackoff/Babai/Moran）
- RSA Award for Excellence in Mathematics（2004）
- NAS 院士（2007）；IACR Fellow（2007）
- NAE 院士；American Academy of Arts and Sciences 院士
- University of Salerno 荣誉学位（2015）
- ACM Fellow（2017）

## 9. 机构清单

- 教育：Sapienza University of Rome（数学，1978）、UC Berkeley（MS + PhD CS 1982）
- 任职：MIT 电气工程与计算机科学系（1983 起；MIT CSAIL）——曾兼任 University of Pennsylvania、University of Toronto、Tsinghua University 教职；CoreStreet Ltd 联合创始人兼 Chief Scientist（2001，→ActivIdentity 2009 收购）；Peppercoin 创始人（2000s 初，2007 被收购）；Algorand 创始人（2017）

## 10. 终审清单

- [ ] 生卒 1954-10-13 / 在世留白，出生地 Palermo
- [ ] 图灵奖 2012 与 Goldwasser 共享、理由口径正确（cryptography / provable security）
- [ ] 零知识证明三人署名（+Rackoff）；交互式证明双组平行（+Babai/Moran）
- [ ] Blum–Micali 算法与语义安全叙事准确、与 Goldwasser 篇分工不重复
- [ ] 三度创业年份与收购年（CoreStreet→2009、Peppercoin→2007）不混淆
- [ ] Algorand 为 Micali 独立创立，Goldwasser 仅顾问
- [ ] 博士导师 Manuel Blum 表述准确
- [ ] 封面底部状态栏 `意大利 | MIT · Sapienza · UC Berkeley | Turing 2012`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2012/Silvio Micali/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用肖像（`images/500px-Silvio_Micali.jpg`，已就绪）
- [ ] **国籍**：封面顶部徽章明示意大利
- [ ] **引语核对**：正文无本人直接引语，仅获奖表述与 "Nobel Prize of computing" 定位句可引
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Shafi_Goldwasser 篇格式对齐且叙事侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
