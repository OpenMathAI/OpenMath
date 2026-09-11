# Martin Hellman（马丁·赫尔曼）立传提示词

> qid=Q476466 · 1945-10-02 生（在世留白） · 美国密码学家、数学家 · 20/21 世纪 · 2015 图灵奖（与 Diffie 共享）
> 本地 Wikipedia 数据源：`turing/pages/2015/Martin Hellman/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（Diffie–Hellman 密钥交换的模幂示意 / DES 56-bit / "Learning with Finite Memory" 的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Martin Edward Hellman（中文惯称：马丁·赫尔曼）
- **生卒**：1945-10-02 生于 New York City（美国）→ **在世留白**（页面无卒日，勿编造）
- **国籍**：美国（American）
- **身份**：密码学家（cryptologist）、数学家；公钥密码学发明人之一（in cooperation with Whitfield Diffie and Ralph Merkle）
- **家庭**：纽约犹太家庭出身；妻子 Dorothie Hellman（2016 年合著一书，见亮点 10）
- **教育轨迹**：
  - Bronx High School of Science（布朗克斯科学高中）毕业
  - New York University **电机工程 BS**（1966）
  - Stanford University **MS**（1967）+ **PhD**（1969），博士论文 *Learning with Finite Memory*
- **博士导师**：Thomas Cover（Stanford 信息论学家）
- **研究领域**：密码学、计算机科学、电机工程；后期国际安全/核风险分析

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **《New Directions in Cryptography》（1976，与 Diffie）**：提出**公钥密码学**与**数字签名**思想，远途解决密码学根本难题——**密钥分发**；催生 public key / asymmetric encryption 新类算法。获奖理由即此文（整句引用见 §5）。
2. **Diffie–Hellman 密钥交换**：方案以两人命名；**页面实载**：Hellman 本人主张应叫 **Diffie–Hellman–Merkle** key exchange（因 Merkle 的独立贡献）——此为 Hellman 篇专属内容，可写；Diffie 篇不展开。
3. **师承与学术谱系**：导师 Thomas Cover；博士生 **Ralph Merkle**（公钥三杰之一）与 **Taher Elgamal**（ElGamal 加密发明人）——"导师-学生两代皆入公钥史"是本篇独有叙事线。
4. **IBM Watson 岁月（1968–69）**：在 Yorktown Heights 遇到 **Horst Feistel**（DES 之父 Feistel 结构发明人）——密码学启蒙节点。
5. **MIT 助理教授（1969–71）**：电机工程助理教授两年。
6. **Stanford 教授（1971–96）**：1971 年以助理教授加入 Stanford EE，全职任教二十五年，1996 年以正教授荣休（emeritus）。
7. **与 Diffie 的斯坦福合作**：1974 年 Diffie 到访长谈 → 1975 年聘为兼职研究程序员 → 1976 年合著《New Directions》；1975–76 共同批评 DES 56-bit 密钥过短（1976 Stanford DES 评审会有录音存世）；历史证明 NSA 曾施压缩短密钥、短密钥确被并行破解机攻破（RSA DES Challenges 1997 起、2012 年 $10,000 商用机数日破 DES）。
8. **Pohlig–Hellman 算法**：与 Steve Pohlig 的合作（页面在 oral history 段落实载）。
9. **从密码学转向国际安全（1985 起）**：Beyond War 运动小册子主要编辑；1987 年与苏联学者合编 *Breakthrough: Emerging New Thinking*（与 Anatoly Gromyko 共同主编）；研究核威慑失败的**概率与风险**，NuclearRisk.org 项目；Daisy Alliance 董事会成员；NRC 国家密码政策委员会（1994–96）。
10. **与妻子合著（2016）**：*A New Map for Relationships: Creating True Love at Home and Peace on the Planet*（与 Dorothie Hellman）——"把家庭之爱与地球和平联系起来"。
11. **荣誉**：2015 图灵奖（与 Diffie）、Marconi Prize 2000、IEEE Hamming Medal 2010、NAE 2002、IEEE Fellow 1980 等。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（公钥数学 — 蓝） | `#2E5A9E` | Diffie–Hellman 密钥交换 / New Directions |
| 分类色 2（信息论谱系 — 青绿） | `#1E8E8E` | Cover 门下 / Merkle、Elgamal 门生 |
| 分类色 3（密钥之战 — 琥珀） | `#D9A441` | DES 批评 / Pohlig–Hellman |
| 分类色 4（核风险与和平 — 玫瑰） | `#C0395B` | Beyond War / Breakthrough / NuclearRisk.org |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：模幂阶梯/离散对数网格（稀疏折线），呼应「公开钥匙算出私密共识」的数学视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：深邃 / 恒久（密码学奠基 + 半生核风险求索）
- **选定曲目**：Alex-Productions **Timeless**（manifest 预分配，直接沿用），匹配"超越时代且历久弥新的密码学遗产"叙事。
- **落地文件**：`turing/presentations/Martin_Hellman/Timeless.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「公钥密码学奠基人 · 美国」+ Hellman 1945– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1945–至今 生平纵览
4. **纽约少年与布朗克斯科学高中**：犹太家庭、NYU 电机 1966
5. **Cover 门下的信息论博士**（1967/1969）：Learning with Finite Memory
6. **IBM Watson 与 Feistel 相遇**（1968–69）：密码学启蒙
7. **MIT 助理教授**（1969–71）
8. **斯坦福教授**（1971–96）：二十五载全职、1996 荣休
9. **1974 年的会面与 1976 年的论文**：Diffie 到访、New Directions、密钥分发难题
10. **Diffie–Hellman 密钥交换**：模幂/离散对数示意（公式框）；DHM 命名主张（页面实载）
11. **DES 之战**（1975–76）：56-bit 批评、NSA 干预的历史验证
12. **桃李**：Merkle、Elgamal——两代公钥人物；Pohlig–Hellman
13. **后图灵人生：核风险与和平**（1985–）：Beyond War、Breakthrough、NuclearRisk.org
14. **荣誉与共享之年**：Turing 2015（与 Diffie）、Marconi 2000、NAE 2002
15. **结尾**：在世留白；"密码学家→和平倡议者"的双程人生

## 5. 史实陷阱与敏感点（终审必须检查）

- **与 Diffie 共享结构**：2015 图灵奖由 Diffie 与 Hellman **两人共享**，Merkle 未获奖。本篇侧重 Hellman：DH 密钥交换的数学、斯坦福合作与师承谱系、DES、后半生核风险；Diffie 的流浪学者叙事与隐私政策留给 Diffie 篇——两篇勿重复。
- **Ralph Merkle**：页面实载三层——intro 的"in cooperation with Diffie and Merkle"、**博士生**关系、Hellman 主张命名 Diffie–Hellman–Merkle。仅按此三层写，**禁写页面无载的争议/恩怨**。
- **获奖理由（整句引用，核心红线）**：`"For fundamental contributions to modern cryptography. Diffie and Hellman's groundbreaking 1976 paper, "New Directions in Cryptography," introduced the ideas of public-key cryptography and digital signatures, which are the foundation for most regularly-used security protocols on the internet today."`
- **博士学位年份**：NYU BS 1966 / Stanford MS 1967 / PhD 1969——勿错位。
- **IBM 与 MIT 任职区间**：IBM Watson 1968–69（与 Stanford 博士后期并行，页面如此实载）、MIT 助理教授 1969–71、Stanford 1971 起——年份勿混。
- **DES 批评年份**：1975 年起为"最著名批评者"（most prominent critics of the short key size of DES in 1975）；1976 评审会录音。
- **"历史证明"表述**：NSA 干预与破解机验证是"subsequent history has shown"——勿写成当时已知。
- **引语**：除获奖 citation 外，**全文无其他直接引语**，勿编造（DHM 命名主张是转述，非引语）。
- **国际安全章节**：Beyond War 小册子编辑、Breakthrough 共同主编（与 Anatoly Gromyko）、NuclearRisk.org、Daisy Alliance——按页面实载平铺，不渲染政治立场；NRC 委员会（1994–96）归密码政策非核风险。
- **在世留白**：born 1945-10-02，写作 `1945–`。
- **家庭**：仅妻子 Dorothie 有载（2016 合著）；其余家庭细节勿编造。
- **Marconi 2000**：与 Diffie 同获奖项，理由含"使密码学成为合法学术研究领域"——可写。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 赫尔曼（或 马丁·赫尔曼） | 待写入 |
| name_en | Martin Hellman | 待写入 |
| birth_date | 1945-10-02 | 待写入 |
| death_date | NULL（在世） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | cryptologist | 待写入 |
| field_of_work | cryptography / computer science / electrical engineering | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Thomas Cover（Stanford）
- **合作者**：Whitfield Diffie（New Directions 1976、DES 批评、共享图灵/Marconi/Hamming/Fink）、Steve Pohlig（Pohlig–Hellman 算法）、Anatoly Gromyko（Breakthrough 共同主编）、Dorothie Hellman（2016 合著，妻子）
- **著名博士生**：Ralph Merkle（公钥密码学共同奠基人）、Taher Elgamal（ElGamal 加密）
- **相遇人物**：Horst Feistel（IBM Watson，DES 结构之父——按"encountered"表述，勿写成合作）
- **页面无载的关系**：勿补

## 8. 奖项清单

- IEEE Fellow（1980，密码学贡献）
- IEEE Donald G. Fink Prize Paper Award（1981，与 Diffie）
- IEEE Centennial Medal（1984）
- EFF Pioneer Award（1994）
- Louis E. Levy Medal, Franklin Institute（1997）
- IEEE Information Theory Society Golden Jubilee Award for Technological Innovation（1998）
- Marconi Prize（2000，与 Diffie）
- National Academy of Engineering 院士（2002，"contributions to the theory and practice of cryptography"）
- IEEE Richard W. Hamming Medal（2010）
- National Inventors Hall of Fame（2011）
- Computer History Museum Fellow（2011，"with Whitfield Diffie and Ralph Merkle, on public key cryptography"）
- ACM Turing Award（2015，与 Diffie 共享）

## 9. 机构清单

- 教育：Bronx High School of Science、New York University（BS EE 1966）、Stanford University（MS 1967 / PhD 1969）
- 任职：IBM Thomas J. Watson Research Center（1968–69）、MIT 电机工程助理教授（1969–71）、Stanford EE 助理教授→正教授（1971–1996，1996 emeritus）
- 公益/机构：National Research Council 国家密码政策委员会（1994–96）、Daisy Alliance 董事会、NuclearRisk.org

## 10. 终审清单

- [ ] 生卒 1945-10-02 / 在世留白，出生地 New York City
- [ ] 获奖理由整句引用无误（2015，与 Diffie 共享）
- [ ] NYU 1966 / Stanford MS 1967 / PhD 1969，导师 Cover
- [ ] IBM 1968–69 / MIT 1969–71 / Stanford 1971–96 年份链准确
- [ ] DHM 命名主张为页面实载，可写；其余 Merkle 争议禁写
- [ ] DES 批评 1975 起、"历史证明"表述准确
- [ ] Merkle/Elgamal 为博士生，Feistel 为"相遇"非合作
- [ ] 后半生核风险章节按页面实载平铺，无政治渲染
- [ ] 与 Diffie 篇分工明确：本篇侧重数学与师承谱系
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Stanford · IBM · MIT | Turing 2015`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2015/Martin Hellman/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Martin-Hellman.jpg`（c. 2000 肖像，目录中唯一人像文件）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅获奖 citation 可整句引用，其余无直接引语勿编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Diffie 篇格式对齐但内容分工不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
