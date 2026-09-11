# Adi Shamir（阿迪·沙米尔）立传提示词

> qid=Q320624 · 1952-07-06 – 在世留白 · 以色列密码学家、发明家 · 20/21 世纪 · 2002 图灵奖（与 Ron Rivest、Leonard Adleman 三人共享）
> 本地 Wikipedia 数据源：`turing/pages/2002/Adi Shamir/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 以色列`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名（含希伯来名 עדי שמיר）、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Shamir 秘密共享 / Fiat–Shamir 启发式 / 差分密码分析的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Adi Shamir（希伯来语：עדי שמיר；中文惯称：阿迪·沙米尔）
- **生卒**：1952-07-06 生于特拉维夫（Tel Aviv，以色列）；在世，卒年留白
- **国籍**：以色列（Israeli）
- **身份**：密码学家、发明家（RSA 的 S）
- **教育轨迹**：
  - Tel Aviv University **数学**学士（BSc，1973）
  - Weizmann Institute of Science **计算机科学**硕士（1975）+ 博士（1977），论文 *The fixedpoints of recursive definitions*
- **博士导师**：Zohar Manna（Weizmann）
- **研究领域**：密码学（infobox Fields 仅 cryptography）
- **任职轨迹**：Warwick 大学博士后一年 → MIT 研究（1977–1980，与 Rivest/Adleman 共事期）→ 1980 年回以色列加入 Weizmann 数学与计算机科学系 → 2006 年起兼任巴黎高等师范学院（École Normale Supérieure）特邀教授

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **RSA 的 S（1978）**：与 Rivest、Adleman 共同发明 RSA 算法（Rivest–Shamir–Adleman），2002 三人共享图灵奖。【共同部分，与本批次 Rivest/Adleman 两篇口径一致】
2. **Shamir 秘密共享（Shamir's secret sharing）**：infobox "Known for" 与正文均实载的贡献——把秘密拆分成多份份额、凑齐门限才能还原。【本篇侧重的第一支柱】**注意：页面未给出年份（1979），勿在正文写具体年份。**
3. **密码分析大师【本篇侧重的第二支柱】**：
   - **攻破 Merkle–Hellman 背包密码体制**（breaking of the Merkle-Hellman knapsack cryptosystem）
   - **差分密码分析**（differential cryptanalysis）：1980 年代末与 Eli Biham 共同发现，攻击分组密码的通用方法；后来才曝光 IBM 与 NSA 早已知晓并保密——写"后来曝光"即可，勿渲染阴谋叙事
   - **A5/1 实时破译（2000）**：与 Alex Biryukov、David Wagner 提出 GSM 手机通信流密码 A5/1 的实时密码分析
   - **FMS 攻击（2001）**：与 Scott Fluhrer、Itsik Mantin 发表对 RC4 流密码的密钥恢复攻击（Fluhrer–Mantin–Shamir attack），暴露当时 Wi-Fi 的 WEP 协议的实际弱点——与 Rivest 的 RC4 形成有趣呼应
   - **声学密码分析（2014）**：与 Daniel Genkin、Eran Tromer 演示通过笔记本解密时发出的声音提取完整 4096 位 RSA 密钥；另发展了 cache attack 等一系列侧信道攻击
4. **身份基密码（1984）**：提出 identity-based cryptography 概念——用户公钥可从邮箱地址等唯一标识直接导出。
5. **Fiat–Shamir 启发式（1986）**：与 Amos Fiat 共同设计，把交互式身份验证协议转化为数字签名方案的广泛使用方法；三人组合的 **Feige–Fiat–Shamir 身份识别方案**（与 Uriel Feige、Amos Fiat）亦是 infobox 实载。
6. **视觉密码学（visual cryptography）**与 **TWINKLE/TWIRL 分解设备**：页面实载的两项发明。
7. **密码学之外的贡献**：2-satisfiability 的首个线性时间算法；基于 Lund/Fortnow/Karloff/Nisan 的工作证明复杂性类 **IP = PSPACE**（1992, JACM）。
8. **机器学习安全（2010 年代末起）**：对抗样本理论研究（"Dimpled Manifold Model"）、神经网络模型参数的密码分析提取（EUROCRYPT 2024）。
9. **环签名（2001）**：与 Rivest、Yael Tauman 共同提出——成员可代表群体签名而不暴露身份（论文 "How to Leak a Secret"）。
10. **RSA Security 与 RSA Conference**：与 Rivest、Adleman 共同创立 RSA Security（RSA Conference 自 1991 年每年举办）；2019 年 Shamir 因美签未获批缺席旧金山 RSA Conference、以视频出席密码学家圆桌并建议学界重新考虑会议举办地——**按页面实载一笔带过，不渲染**。
11. **荣誉（要点）**：Israel Prize（2008）、Japan Prize（2017，第 33 届，电子信息通信领域，表彰密码学先驱性研究对信息安全的贡献）、Wolf Prize in Mathematics（2024，数学密码学根本贡献）、皇家学会外籍会士 ForMemRS（2018）、美国国家科学院外籍院士（2005）。
12. **门生**：Eli Biham、Uriel Feige、Amos Fiat（infobox 实载三人，恰好都是上述贡献的合作者）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（公钥密码 RSA — 蓝） | `#2E5A9E` | RSA 的 S / RSA Security |
| 分类色 2（密码分析 — 青绿） | `#1E8E8E` | 差分分析 / A5/1 / FMS / 声学攻击 |
| 分类色 3（秘密共享与协议 — 琥珀） | `#D9A441` | Shamir 秘密共享 / Fiat–Shamir / 身份基密码 |
| 分类色 4（理论前沿 — 玫瑰） | `#C0395B` | IP = PSPACE / 机器学习安全 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和拆分碎片（一个圆分裂为多份份额再聚合），呼应「秘密共享的门限重组」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：深邃 / 破译（攻击者视角的冷峻智性 + 密码分析大师的多线人生）
- **选定曲目**：Alex-Productions **Eternals**（manifest 预分配，直接沿用；与化学家 Ostwald 篇同曲，属跨项目正常复用）。
- **落地文件**：`turing/presentations/Adi_Shamir/Eternals.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「RSA 的 S · 密码分析大师 · 以色列」+ Shamir 1952– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名与希伯来名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1952– 生平纵览
4. **早年与教育**：特拉维夫出身、Tel Aviv 数学（1973）、Weizmann 硕博（1975/1977，Manna 门下）
5. **MIT 岁月与 RSA（1977–1980）**：与 Rivest/Adleman 的合作、1978 论文、Warwick 博士后
6. **Shamir 秘密共享**：门限拆分与重组（年份页面未载，勿写）
7. **攻破背包体制**：Merkle–Hellman knapsack 的破译
8. **差分密码分析**：与 Biham、1980 年代末、IBM/NSA 早已知晓的后来曝光
9. **身份基密码与 Fiat–Shamir**：1984 概念、1986 启发式、Feige–Fiat–Shamir 方案
10. **实时破译 A5/1 与 FMS 攻击**：GSM（2000）、RC4/WEP（2001）——与 Rivest 的 RC4 呼应
11. **声学密码分析与侧信道**：2014 年听声提取 4096 位 RSA 密钥
12. **密码学之外**：2-SAT 线性算法、IP = PSPACE、机器学习安全
13. **荣誉之殿**：Israel Prize 2008 / Japan Prize 2017 / Wolf Prize 2024 / ForMemRS 2018
14. **门生与传承**：Biham / Feige / Fiat
15. **结尾**：在世的密码学巨匠——从构造者到破译者的一生

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖获奖理由（核心红线，整句引用）**：2002 年与 Rivest、Adleman 共享，获奖理由 "for their ingenious contribution to making public-key cryptography useful in practice."——三人篇目**一致**，勿改写。
- **Shamir 秘密共享无年份**：页面仅在 "Known for" 与贡献清单中列出，**未写 1979**——正文勿写具体年份；如需年份须先经 Review 修正提示词。
- **差分密码分析时间口径**："in the late 1980s" 与 Biham 共同发现——勿写成 1990 或具体月份；IBM/NSA 早已知晓系 "It later emerged" 表述，保留"后来曝光"的语气，勿渲染成阴谋故事标题。
- **FMS 攻击对象是 RC4/WEP**：攻击揭示的是 **WEP 协议**（当时的 Wi-Fi 加密）的实际弱点——攻击的是协议用法而非"证明 RC4 全盘失败"，措辞以页面为准（"demonstrated a practical weakness in the WEP protocol"）。
- **2-SAT 线性时间算法**：页面表述为 "finding the first linear time algorithm for 2-satisfiability"，所引文献为 Even/Itai/Shamir 1976——勿写成 "Shamir 单独"（文献三位作者）。
- **IP = PSPACE**：是 "proving, building on work of Lund/Fortnow/Karloff/Nisan"——必须带"在前人工作基础上"，勿写成 Shamir 独立从零证明。
- **2019 签证事件**：按页面实载一笔带过（缺席 RSA Conference、视频出席、建议 reconsider 会议地点），**禁写**页面无载的政治评论。
- **在世留白**：1952 年生，在世——死亡日期与死因完全留白。
- **国籍表述**：Israeli，封面用「以色列」；Weizmann Institute 为研究机构勿译成"魏茨曼大学"。
- **共享结构**：本篇侧重秘密共享与密码分析；RSA 提出经过/RC 系列归 Rivest 篇、DNA 计算归 Adleman 篇；三人共同部分口径一致，**禁写页面无载的三人内部恩怨**。
- **荣誉年份红线**：Wolf Prize 是 **2024**（数学奖，数学密码学）、Japan Prize 是 **2017**（第 33 届）、Israel Prize 是 **2008**（计算机科学）——三者年份勿混。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 阿迪·沙米尔 | 待写入 |
| name_en | Adi Shamir | 待写入 |
| birth_date | 1952-07-06 | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | Israel | 待写入 |
| primary_occupation | cryptographer / inventor | 待写入 |
| field_of_work | cryptography | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Zohar Manna（Weizmann Institute）
- **RSA 合作者**：Ron Rivest、Leonard Adleman（1978 论文共同作者、2002 图灵奖共同得主）
- **差分密码分析合作者**：Eli Biham（兼博士生）
- **身份识别方案合作者**：Uriel Feige、Amos Fiat（兼博士生；Feige–Fiat–Shamir、Fiat–Shamir heuristic）
- **环签名合作者**：Ron Rivest、Yael Tauman Kalai（2001）
- **A5/1 与声学分析合作者**：Alex Biryukov、David Wagner；Daniel Genkin、Eran Tromer
- **其他**：Scott Fluhrer、Itsik Mantin（FMS 攻击）

## 8. 奖项清单

- Erdős Prize（Israel Mathematical Society，1983）
- IEEE W.R.G. Baker Award（1986）
- UAP Scientific Prize（1990）
- Pontifical Academy of Sciences PIUS XI Gold Medal（1992）
- Paris Kanellakis Theory and Practice Award（1996，三人共享）
- IEEE Koji Kobayashi Computers and Communications Award（2000，三人共享）
- Turing Award（2002，与 Rivest/Adleman 共享）
- IACR Fellow（2004）
- 美国国家科学院外籍院士（Foreign Associate of NAS，2005）
- Israel Prize for computer sciences（2008）
- Honorary DMath, University of Waterloo（2009）
- Japan Prize, 第 33 届，Electronics, Information and Communication（2017）
- Foreign Member of the Royal Society, ForMemRS（2018）
- American Philosophical Society 会员（2019）
- American Academy of Arts and Sciences International Honorary Member（2022）
- Wolf Prize in Mathematics（2024，数学密码学）
- Levchin Prize, Real World Cryptography（2025）
- Israel Academy of Sciences and Humanities 院士（1998）

## 9. 机构清单

- 教育：Tel Aviv University（数学 BSc，1973）、Weizmann Institute of Science（MSc 1975 / PhD 1977）
- 任职：University of Warwick 博士后（一年）；MIT（研究，1977–1980）；Weizmann Institute 数学与计算机科学系（1980 起）；École Normale Supérieure（巴黎，特邀教授，2006 起）

## 10. 终审清单

- [ ] 生卒 1952-07-06 / 在世留白，出生地 Tel Aviv
- [ ] 图灵奖 2002 与 Rivest/Adleman 共享，理由整句引用无误
- [ ] Shamir 秘密共享未写具体年份（页面无载）
- [ ] 差分密码分析 "late 1980s、与 Biham"、IBM/NSA "后来曝光" 语气准确
- [ ] FMS 攻击对象表述为 "practical weakness in WEP"
- [ ] IP = PSPACE 带 "building on work of Lund/Fortnow/Karloff/Nisan"
- [ ] 2-SAT 线性算法挂 Even/Itai/Shamir 1976 文献口径
- [ ] Wolf 2024 / Japan Prize 2017 / Israel Prize 2008 年份无误
- [ ] 国籍用「以色列」，封面底部状态栏 `以色列 | Weizmann · MIT · ENS | Turing 2002`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2002/Adi Shamir/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用真实肖像（`images/500px-Adi_Shamir_Royal_Society.jpg`，2018 年皇家学会照，取 500px 版）
- [ ] **国籍**：封面顶部徽章明示以色列
- [ ] **引语核对**：全文无直接引语（除获奖理由），勿编造引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 2002 共享得主（Rivest / Adleman）格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
