# Whitfield Diffie（惠特菲尔德·迪菲）立传提示词

> qid=Q462089 · 1944-06-05 生（在世留白） · 美国密码学家、数学家 · 20/21 世纪 · 2015 图灵奖（与 Hellman 共享）
> 本地 Wikipedia 数据源：`turing/pages/2015/Whitfield Diffie/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（公钥/私钥双钥体制 / 密钥分发问题 / DES 56-bit 密钥 的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Bailey Whitfield "Whit" Diffie（中文惯称：惠特菲尔德·迪菲）
- **生卒**：1944-06-05 生于 Washington, D.C.（美国）→ **在世留白**（页面无卒日，勿编造）
- **国籍**：美国（American）
- **身份**：密码学家、数学家；公钥密码学先驱之一（with Martin Hellman and Ralph Merkle）
- **家庭**：父 Bailey Wallys Diffie（City College of New York 教授，讲授伊比利亚历史与文化）、母 Justine Louise（旧姓 Whitfield，作家与学者）；妻子 Mary Fischer（原女友、后成婚，1973 年后协助其游历查档）
- **教育轨迹**：
  - 10 岁迷上密码学——父亲从 City College 图书馆把整架密码学书籍搬回家
  - Jamaica High School（Queens, New York）：拿的是 local diploma（因已凭标准化考试高分被 MIT 录取，未考 Regents）
  - MIT **数学 BS**（1965）；自认"纯数学家"，兴趣在偏微分方程与拓扑
  - 1975 年 6 月曾入 Stanford EE 博士班（Hellman 资助），因未完成体格检查等退学——**无 PhD，勿编造学位**
- **师承**：无传统导师；Stanford AI Lab 时期在 **John McCarthy** 庇护下（under the aegis of）工作——是工作环境非读博师承，勿写成"师从 McCarthy"
- **研究领域**：密码学、计算机安全、隐私政策

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **《New Directions in Cryptography》（1976，与 Hellman）**：提出**公钥密码学**与**数字签名**思想，直击密码学根本难题——**密钥分发**；直接催生非对称密钥算法新类别。这是全篇核心，获奖理由即此文。
2. **打破政府垄断**：1976 年论文发表后，"NSA 的密码垄断事实上终结"——从此每家公司、每个公民都能获得密码技术（引语见 §5，出处 Steven Levy, NYT Magazine 1994）。
3. **十年流浪学者**：1973 年 5 月离开 SAIL 独立研究密码学——当时该领域研究多在 NSA 密级管控之下，他"到图书馆挖稀有手稿、开车串大学访友"，女友（后为妻子）Mary Fischer 协助查档。
4. **命运的会面（1974）**：在 IBM Watson 研究中心遇到 Alan Konheim（因保密令不能多说，只提点一句"去找 Martin Hellman"）→ 与 Hellman 原定半小时的会面聊了数小时 → 1975 年春受聘为 grant-funded 兼职研究员。
5. **DES 之战（1975–76）**：与 Hellman 批评 NBS 的 DES **56-bit 密钥过短**、难防暴力破解；1976 年 Stanford DES 评审会有录音存世。历史证明正确：NSA 曾施压缩短密钥长度，短密钥最终被 EFF DES cracker 类的并行破解机攻破。
6. **MITRE 与 MATHLAB（1965–69）**：MIT 数学毕业后在 MITRE 当研究助理，参与开发 MATHLAB（早期符号计算系统，Macsyma 的基础之一）；作为反战派（pacifist、反对越战）借国防承包商职位避兵役。
7. **Stanford AI Lab（1969–1973）**：研究程序员，做 LISP 1.6（分发于 PDP-10/TOPS-10）与程序正确性问题，同时培育密码学兴趣。
8. **产业界二十年**：Northern Telecom（1978–91，Secure Systems Research 经理，为 X.25 网络设计 PDSO 密钥管理架构）→ Sun Microsystems（1991–2009，distinguished engineer → Chief Security Officer / VP / **Sun Fellow**，主攻密码学公共政策）。
9. **后期机构**：ICANN 信息安全与密码学 VP（2010–2012）、Stanford CISAC visiting scholar/affiliate/consulting scholar、Royal Holloway ISG 访问教授（2008）、浙江大学访问教授（2018，Cryptic Labs 合作）。
10. **著作**：《Privacy on the Line》（与 Susan Landau，1998；扩充版 2007）——电报窃听与加密的政治。
11. **荣誉**：2015 图灵奖（与 Hellman 共享）、Marconi Prize 2000、IEEE Hamming Medal 2010、CHM Fellow 2011、ForMemRS 2017（英国皇家学会外籍院士）、NAE 2017、IEEE Fellow 2025 等。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（公钥革命 — 蓝） | `#2E5A9E` | New Directions 1976 / 双钥体制 |
| 分类色 2（密码破晓 — 青绿） | `#1E8E8E` | 密钥分发问题 / 数字签名 |
| 分类色 3（密钥之战 — 琥珀） | `#D9A441` | DES 批评 / NSA 垄断终结 |
| 分类色 4（隐私与政策 — 玫瑰） | `#C0395B` | Privacy on the Line / 公共政策 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：交错的钥齿/网格线（稀疏细线段），呼应「公钥-私钥配对」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：开拓 / 反叛（流浪学者掀翻密码学垄断）
- **选定曲目**：Alex-Productions **New Lands**（manifest 预分配，直接沿用），匹配"为个人隐私闯入政府禁区"的开荒叙事。
- **落地文件**：`turing/presentations/Whitfield_Diffie/NewLands.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「公钥密码学先驱 · 美国」+ Diffie 1944– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 影响者 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1944–至今 生平纵览
4. **少年与密码学启蒙**：10 岁父亲搬回整架密码学书、Queens 高中、MIT 数学
5. **MITRE 与 MATHLAB**（1965–69）：符号计算、反战者避兵役
6. **Stanford AI Lab 岁月**（1969–73）：LISP 1.6、McCarthy 庇护下的密码学萌芽
7. **流浪学者（1973–74）**：离开 SAIL、图书馆挖手稿、Mary Fischer 同行
8. **1974 年的会面**：Konheim 的指点、与 Hellman 数小时长谈
9. **New Directions in Cryptography（1976）**：公钥密码、数字签名、密钥分发
10. **DES 之战**（1975–76）：56-bit 密钥批评、NSA 干预、EFF cracker 的验证
11. **从 Northern Telecom 到 Sun**（1978–2009）：密钥管理、首席安全官、Sun Fellow
12. **政策与 privacy 布道**：ICANN、CISAC、Privacy on the Line（与 Landau）
13. **荣誉与共享之年**：Turing 2015（与 Hellman）、Marconi 2000、ForMemRS 2017
14. **遗产**：互联网安全协议的基石（TLS 时代的公钥地基——按获奖理由表述）
15. **结尾**：在世留白；"iconoclast（反传统者）"的自我定位

## 5. 史实陷阱与敏感点（终审必须检查）

- **与 Hellman 共享结构**：2015 图灵奖由 Diffie 与 Hellman **两人共享**，Merkle 未获奖。本篇侧重 Diffie：思想倡导、流浪学者、《New Directions》、隐私/政策；DH 密钥交换的**数学推导**留给 Hellman 篇——两篇不要写成同一篇文章。
- **Ralph Merkle 角色**：仅按页面实载提及——开头段"public-key cryptography 沿 with Martin Hellman and Ralph Merkle"、CHM Fellow 理由"with Martin Hellman and Ralph Merkle"。Merkle 的博士关系、DHM 命名之争等**在 Diffie 页面无展开，禁写争议细节**（Hellman 建议改名 Diffie-Hellman-Merkle 一事属 Hellman 页面实载，若两篇内容有交叉仅 Hellman 篇可写）。
- **获奖理由（整句引用，核心红线）**：`"For fundamental contributions to modern cryptography. Diffie and Hellman's groundbreaking 1976 paper, 'New Directions in Cryptography', introduced the ideas of public-key cryptography and digital signatures, which are the foundation for most regularly-used security protocols on the internet today."`
- **学位**：只有 MIT 数学 BS（1965）；Stanford 博士班 1975 入学后**辍学**（连体格检查都没做）——**勿写 PhD**。
- **师承表述**：SAIL 时期是 "under the aegis of John McCarthy"（工作庇护），非师承；勿写"师从 McCarthy 读博"。
- **避兵役表述**：页面明载 MITRE 职位使其作为反战派得以 avoid the draft——可一笔带过，不渲染政治立场。
- **可引语**（页面实载，须标注出处）：
  - "From the moment Diffie and Hellman published their findings..., the National Security Agency's crypto monopoly was effectively terminated. ... Every company, every citizen now had routine access to the sorts of cryptographic technology that not many years ago ranked alongside the atom bomb as a source of power."（Steven Levy, NYT Magazine, 1994）
  - "was always concerned about individuals, an individual's privacy as opposed to government secrecy."（Levy）
  - 10 岁启蒙句："age 10 when his father, a professor, brought home the entire crypto shelf of the City College Library in New York."
- **年份红线**：SAIL 1969-11 入职 / 1973-05 离开；与 Hellman 会面 1974 夏；论文 1976；Sun 1991–2009-11；ICANN 2010-05–2012-10。
- **NSA 干预 DES**：页面表述为"subsequent history has shown"——写"历史证明"而非"当时即知"。
- **在世留白**：born 1944-06-05，写作 `1944–`。
- **Kanellakis Award 1996**：infobox 实载名"Kanellakis Award"，写全称时勿加未载细节（ACM 全称 Paris Kanellakis 页面未展开，可写 ACM Kanellakis Award）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 迪菲（或 惠特菲尔德·迪菲） | 待写入 |
| name_en | Whitfield Diffie | 待写入 |
| birth_date | 1944-06-05 | 待写入 |
| death_date | NULL（在世） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | cryptographer | 待写入 |
| field_of_work | cryptography / computer security | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **合作者**：Martin Hellman（New Directions 1976 合著、DES 批评、Marconi/Hamming/图灵共享）、Susan Landau（Privacy on the Line 合著）
- **共同奠基人**：Ralph Merkle（页面实载并列提及）
- **影响庇护者**：John McCarthy（SAIL 时期 aegis，注意是工作庇护非师承）
- **关键引路人**：Alan Konheim（1974 指点去找 Hellman）
- **页面无载的关系**：勿补（如与 RSA 三人、与 EFF 的关系等）

## 8. 奖项清单

- ACM Turing Award（2015，与 Martin Hellman 共享）
- IEEE Donald G. Fink Prize Paper Award（1981，与 Hellman）
- Honorary doctorate, Swiss Federal Institute (ETH)（1992）
- ACM Kanellakis Award（1996）
- Louis E. Levy Medal, Franklin Institute（1997）
- IEEE Information Theory Society Golden Jubilee Award for Technological Innovation（1998）
- Marconi Prize（2000）
- IEEE Richard W. Hamming Medal（2010）
- National Inventors Hall of Fame + Computer History Museum Fellow（2011，理由含 Merkle）
- Foreign Member of the Royal Society, ForMemRS（2017）
- National Academy of Engineering 院士（2017）
- IEEE Fellow（2025，"for the development of public key cryptography and its applications"）

## 9. 机构清单

- 教育：Jamaica High School（Queens）、MIT（数学 BS 1965）、Stanford EE 博士班（1975 入学后辍学）
- 任职：MITRE Corporation（1965–69）、Stanford AI Lab（1969-11–1973-05）、Stanford/Hellman 组研究助理（至 1978-06）、Northern Telecom（1978–91）、Sun Microsystems（1991–2009）、ICANN（2010–2012）、Stanford CISAC（2009– 至今 consulting scholar）、Royal Holloway ISG（2008 访问教授）、浙江大学（2018 访问教授）

## 10. 终审清单

- [ ] 生卒 1944-06-05 / 在世留白，出生地 Washington, D.C.
- [ ] 获奖理由整句引用无误（2015，与 Hellman 共享）
- [ ] MIT 数学 BS，无 PhD（Stanford 辍学）表述准确
- [ ] McCarthy 为"工作庇护"非师承
- [ ] Merkle 仅按页面实载并列提及，无争议细节
- [ ] 1974 会面→1975 兼职→1976 论文时间链准确
- [ ] DES 批评 1975–76、"历史证明"表述准确
- [ ] Sun 1991–2009 / ICANN 2010–2012 年份准确
- [ ] 与 Hellman 篇分工明确：本篇侧重思想倡导与政策，不重复 DH 数学推导
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Sun · ICANN · Stanford CISAC | Turing 2015`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2015/Whitfield Diffie/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用皇家学会肖像（`images/500px-Whitfield_Diffie_Royal_Society.jpg`，2017 London admissions day，取最大可用版；备选 `500px-Whit_Diffie_at_CFP_2007.jpg`）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：三条可引语均须在 Wikipedia 原文找到并标注出处（Levy 1994）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Hellman 篇格式对齐但内容分工不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
