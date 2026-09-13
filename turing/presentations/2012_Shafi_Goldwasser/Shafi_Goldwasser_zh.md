# Shafi Goldwasser（沙菲·戈德瓦瑟）立传提示词

> qid=Q11609 · 1959-11-14 – 在世留白 · 以色列-美国计算机科学家 · 20/21 世纪 · 2012 图灵奖（与 Silvio Micali 共享）
> 本地 Wikipedia 数据源：`turing/pages/2012/Shafi Goldwasser/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 以色列-美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（概率加密 / 零知识证明 / 可证明安全的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Shafrira Goldwasser（希伯来语：שפרירה גולדווסר；通称 Shafi Goldwasser；中文惯称：沙菲·戈德瓦瑟）
- **生卒**：1959-11-14 生于纽约市（New York City，美国）→ 在世留白
- **国籍**：以色列-美国双籍（infobox Citizenship: Israel, United States；页面称 Israeli-American computer scientist）
- **身份**：计算机科学家、密码学家；MIT 电气工程与计算机科学 RSA 教授（1997 年首任讲席教授）、Weizmann Institute of Science 数学科学教授（1993 年起兼任）、Simons Institute for the Theory of Computing 前所长（2018-01–2024-08）、Duality Technologies 联合创始人兼首席科学家
- **家庭**：在纽约出生、特拉维夫长大；育有两子（页面仅此一句）
- **教育轨迹**：
  - Carnegie Mellon University **数学与科学** BS（1979）
  - UC Berkeley **MS**（1981）+ **PhD**（1984），论文 *Probabilistic Encryption: Theory and Applications*
- **博士导师**：Manuel Blum（1995 图灵奖得主——师徒双图灵奖，可写）
- **研究领域**：密码学、计算复杂性理论、计算数论

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖 2012（与 Micali 共享）**：颁奖理由（整句引用，核心红线）："for having pioneered the field of provable security, which laid the mathematical foundations that made modern cryptography possible"——关键词是 **provable security（可证明安全）**。
2. **概率加密（1984，与 Micali）**：研究生时代的合作成果——一条消息可概率地加密成多个不同密文，对选择明文攻击（chosen-plaintext attacks）更具抵抗力；已成为**大多数公钥密码方案的基础**（页面原文 "has become the basis for most public-key cryptographic schemes"）。
3. **零知识证明（1985，与 Micali、Rackoff）**：论文 *The knowledge complexity of interactive proof-systems*（STOC '85）——概率性、交互式地证明断言有效而不泄露任何额外知识；现代密码学的基本原语。
4. **交互式证明**：从更广的 interactive proofs 研究出发；1980s 后期 Micali 组与 Babai–Moran 二人组分别发表交互式证明论文——后来共享 1993 年 Gödel Prize。
5. **复杂性理论侧翼**：难近似性（hardness of approximation）与交互式证明、PCP 定理的联系；与 Kilian 用椭圆曲线做素性测试；为不可信服务器设计计算委托协议（delegating computation）。
6. **Blum–Goldwasser 密码系统**：与导师 Blum 在 Berkeley 期间提出——概率加密之外的另一经典构造。
7. **两次 Gödel Prize**：1993（与 Babai/Micali/Moran/Rackoff，"The knowledge complexity of interactive proof systems"）+ 2001（与 Arora/Feige/Lund/Lovász/Motwani/Safra/Sudan/Szegedy，"Interactive Proofs and the Hardness of Approximating Cliques"）——1993 与 2001 两次理由不同，勿混。
8. **产业与机构领导**：2016-11 与 Vinod Vaikuntanathan 等联合创立 Duality Technologies 商业化**全同态加密**；QED-it（零知识区块链）与 Algorand（Micali 创办的 PoS 区块链）科学顾问；2018-01–2024-08 任 Simons Institute 所长。
9. **Project CETI**：跨学科计划解读抹香鲸通信的负责人之一——"从密码学到鲸语"的叙事彩蛋（页面有载）。
10. **女性科学家标杆**：L'Oréal-UNESCO for Women in Science Award 2021（计算机科学）、Suffrage Science award 2016、Notable Women in Computing cards、ACM 委员会 Athena Lecturer 2008–09。
11. **荣誉等身**：Grace Murray Hopper Award 1996、RSA 数学卓越奖 1998、NAS 2004、NAE 2005、IACR Fellow 2007、Benjamin Franklin Medal 2010、IEEE Piore Award 2011、BBVA 2018（与 Micali/Rivest/Shamir 共享）、英国皇家学会 Fellow 2023；2002 年北京国际数学家大会特邀报告。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（概率加密 — 蓝） | `#2E5A9E` | 概率加密 / Blum–Goldwasser / 语义安全 |
| 分类色 2（零知识证明 — 青绿） | `#1E8E8E` | 零知识证明 / 交互式证明 / Gödel×2 |
| 分类色 3（复杂性理论 — 琥珀） | `#D9A441` | PCP 定理 / 难近似性 / 委托计算 |
| 分类色 4（产业与前沿 — 玫瑰） | `#C0395B` | 全同态加密 Duality / Project CETI / Simons 所长 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「证明你知道却不说出你知道」的零知识视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：绵长 / 沉淀（可证明安全三十年：从 Berkeley 研究生到 Simons 所长）
- **选定曲目**：Alex-Productions **The Flow of Time**（manifest 预分配，直接沿用；与 Wilkinson 同曲属正常复用）。
- **落地文件**：`turing/presentations/Shafi_Goldwasser/TheFlowOfTime.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「可证明安全奠基人 · 以色列-美国」+ Goldwasser 1959– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1959–在世 生平纵览
4. **早年：纽约出生、特拉维夫长大**（1959–1979）：回美求学、CMU 数学与科学 BS
5. **Berkeley 与 Manuel Blum**（1979–1984）：密码学与算法数论、Blum–Goldwasser 密码系统、概率加密论文
6. **概率加密**（1984，与 Micali）：一消息多密文、抗选择明文攻击、公钥方案的基础
7. **交互式证明**（1980s）：Micali 组与 Babai–Moran 平行发表
8. **零知识证明**（1985，与 Micali、Rackoff）：证明而不泄露、现代密码学基本原语
9. **两次 Gödel Prize**（1993 / 2001）：知识复杂性与团难近似两条线
10. **PCP 与难近似性**：交互式证明的复杂性侧翼、素性测试椭圆曲线、委托计算
11. **MIT RSA 教授与 Weizmann**（1983–）：首任 RSA 讲席、双岸执教
12. **产业与 Simons**：Duality 全同态加密、Algorand/QED-it 顾问、Simons Institute 所长（2018–2024）
13. **Project CETI**：解读抹香鲸通信——密码学家的跨界
14. **荣誉与传承**：Turing 2012、Hopper 1996、L'Oréal-UNESCO 2021、皇家学会 2023；门生 Håstad/Kalai/Vadhan/Vaikuntanathan 等
15. **结尾**：在世、"奠定现代密码学的数学基础"

## 5. 史实陷阱与敏感点（终审必须检查）

- **"第三位女性图灵奖得主"表述页面未载，禁写**：页面只写 L'Oréal-UNESCO 女性科学家奖等，未写图灵奖女性序数——女性先驱叙事用页面实载奖项表达；序数表述一律不写。
- **图灵奖理由整句引用**："pioneered the field of provable security, which laid the mathematical foundations that made modern cryptography possible"——关键词 **provable security**，勿替换成"现代密码学奠基人"之类的泛称。
- **共享结构**：2012 与 **Silvio Micali** 两人共享——本篇侧重 Goldwasser 视角（复杂性理论、PCP/难近似、Duality/Simons/CETI、女性科学奖线），零知识证明与概率加密的共同历史点到即止，细节叙事留给 Micali 篇。
- **零知识证明是三人成果**：1985 年论文作者是 **Goldwasser + Micali + Charles Rackoff**——勿写"与 Micali 两人发明"；Rackoff 未获图灵奖但论文署名必须完整。
- **交互式证明的双组平行**：Micali 组与 **Babai–Moran** 分别发表——"分别独立发表、共享 Gödel Prize"，勿写单方发明。
- **1993 与 2001 两次 Gödel Prize 理由不同**：1993 = 知识复杂度/交互式证明系统；2001 = 交互式证明与团难近似（PCP 线）——勿互换。
- **概率加密年份**：1984 年与 Micali 引入（本人 PhD 论文同为 1984 *Probabilistic Encryption: Theory and Applications*）；加入 MIT 是 **1983**（早于博士毕业，页面明载），勿写"毕业后加入"。
- **RSA 教授**：1997 年成为 RSA 讲席的**首任**（"the first holder of the RSA Professorship"）——"首个"限定语为页面原文，可用。
- **BBVA 2018 共享名单**：与 Micali、Rivest、Shamir 共享（四人）——勿写成两人奖。
- **在世**：死亡日期留白，生卒写 `1959–`。
- **引语**：正文**无本人直接引语**（页面仅有获奖理由与论文题名）；勿编造访谈引语。
- **家庭**：仅"育有两子"一句；丈夫/家庭其余细节无载禁写。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 沙菲·戈德瓦瑟 | 待写入 |
| name_en | Shafi Goldwasser | 待写入 |
| birth_date | 1959-11-14 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Israel / United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | cryptography / computational complexity theory / computational number theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Manuel Blum（Berkeley，1995 图灵奖得主）
- **核心合作者**：Silvio Micali（概率加密 1984、零知识 1985、Gödel 1993、BBVA 2018——共享多条）、Charles Rackoff（零知识证明 1985）、Manuel Blum（Blum–Goldwasser）
- **Gödel Prize 共享者**：László Babai、Shlomo Moran（1993）；Sanjeev Arora、Uriel Feige、Carsten Lund、László Lovász、Rajeev Motwani、Shmuel Safra、Madhu Sudan、Mario Szegedy（2001）
- **著名博士生**：Elette Boyle、Johan Håstad、Yael Tauman Kalai、Tal Malkin、Amit Sahai、Salil Vadhan、Vinod Vaikuntanathan
- **页面无载的关系**：禁写

## 8. 奖项清单

- A.M. Turing Award（2012，与 Silvio Micali 共享；provable security citation）
- Gödel Prize（1993、2001 两次，理由不同见 §5）
- ACM Grace Murray Hopper Award（1996）
- RSA Award for Excellence in Mathematics（1998）
- AAAS Fellow（2000）；American Academy of Arts and Sciences（2001）
- NAS 院士（2004）；NAE 院士（2005，"for contributions to cryptography, number theory, and complexity theory, and their applications to privacy and security"）
- Berkeley CS 杰出校友奖（2006）；IACR Fellow（2007）；Athena Lecturer（2008–09）
- Benjamin Franklin Medal in Computer and Cognitive Science（Franklin Institute，2010）
- IEEE Emanuel R. Piore Award（2011）
- Suffrage Science award（2016）；ACM Fellow（2017）
- BBVA Foundation Frontiers of Knowledge Award（2018，与 Micali/Rivest/Shamir 共享）
- CMU 荣誉学位（2018）；Oxford 荣誉理学博士（2019）
- L'Oréal-UNESCO for Women in Science Award（2021，计算机科学）
- Royal Society Fellow（2023）
- 2002 年北京国际数学家大会（ICM）特邀报告

## 9. 机构清单

- 教育：Carnegie Mellon University（BS 1979）、UC Berkeley（MS 1981、PhD 1984）
- 任职：MIT（1983 加入；1997 起 RSA Professor；CSAIL 理论计算组）→ Weizmann Institute of Science（1993 起兼任教授）→ Duality Technologies 联合创始人兼首席科学家（2016-11 起）→ Simons Institute for the Theory of Computing 所长（2018-01–2024-08）；QED-it、Algorand 科学顾问

## 10. 终审清单

- [ ] 生卒 1959-11-14 / 在世留白，出生地 New York City、成长地 Tel Aviv
- [ ] 图灵奖理由整句引用 "provable security..."，2012 与 Micali 共享
- [ ] 零知识证明三人署名（+Rackoff）；交互式证明双组平行（+Babai–Moran）
- [ ] 两次 Gödel Prize 年份与理由不混淆
- [ ] 全篇无"第三位女性图灵奖得主"序数表述
- [ ] MIT 1983 加入早于 1984 博士毕业，表述准确
- [ ] 博士导师 Manuel Blum（师徒双图灵奖）表述准确
- [ ] 封面底部状态栏 `以色列-美国 | MIT · Weizmann · Berkeley | Turing 2012`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2012/Shafi Goldwasser/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用肖像（`images/500px-Shafi_Goldwasser.JPG`，已就绪）
- [ ] **国籍**：封面顶部徽章明示以色列-美国
- [ ] **引语核对**：正文无本人直接引语，仅获奖理由与颁奖词可引
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Silvio_Micali 篇格式对齐且叙事侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
