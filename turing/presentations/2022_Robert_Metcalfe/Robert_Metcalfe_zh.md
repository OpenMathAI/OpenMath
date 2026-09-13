# Robert Metcalfe（罗伯特·梅特卡夫）立传提示词

> qid=Q92766 · 1946-04-07 –（在世留白）· 美国工程师、企业家 · 20/21 世纪 · 2022 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2022/Robert Metcalfe/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。（真实肖像：`images/With_Bob_Metcalfe_cropped_.jpg`，取全尺寸版）
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、家庭（妻 Robyn、二子）、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（以太网帧冲突退避 / Metcalfe 定律 V∝n² / 分组交换的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Robert Melancton Metcalfe（中文惯称：罗伯特·梅特卡夫，昵称 Bob）
- **生卒**：1946-04-07 生于 New York City, U.S. → **在世，卒年留白**
- **国籍**：美国（American）
- **身份**：工程师、企业家（internet pioneer；Ethernet co-inventor；3Com founder；Metcalfe's law 提出者）
- **家庭**：父 Robert Metcalfe（陀螺仪专业 test technician）、母 Ruth（家庭主妇，后任 Bay Shore High School 秘书）；英/爱尔兰/挪威血统；妻 Robyn，育有二子
- **教育轨迹**：
  - 1964 年毕业于 Bay Shore High School（其母后来在该校任秘书）
  - 1969 年 MIT **两个学士学位**：电气工程（BS）+ 工业管理（BS）
  - 1970 年 Harvard **应用数学**硕士（MS）
  - 1973 年 Harvard **计算机科学**博士（PhD）；论文 *Packet Communication*
- **博士导师**：Jeffrey P. Buzen
- **研究领域**：计算机网络（局域网、分组通信）、创新与创业

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2022 图灵奖**（2023 年 3 月宣布）：表彰"contributions to the invention of Ethernet technology"——NYT 标题即 *"Turing Award Won by Co-Inventor of Ethernet Technology"*，**以太网是 co-invent**（与 David Boggs）。
2. **ARPAnet 岁月**：读博期间 Harvard 拒绝为其接入 ARPAnet，遂入职 MIT Project MAC，负责搭建连接 MIT 小型机与 ARPAnet 的部分硬件；博士论文即以 ARPAnet 为题。
3. **哈佛拒稿与 ALOHA 转机**：1972 年 6 月博士论文答辩**最初被 Harvard 拒绝**；在 Xerox PARC 期间读到夏威夷大学 ALOHA 网络论文，找出并修复 AlohaNet 模型的若干 bug，将成果并入修改后的论文——Harvard 随即接受并授予 PhD（1973）。
4. **以太网的"两个生日"**：Metcalfe 本人主张 **1973-05-22**（散发 "Alto Ethernet" 备忘录之日，内含粗略原理图，并回忆"coax as ether... packets... collisions, and retransmissions, and back-off"）；Boggs 主张 **1973-11-11**（系统首次真正运行之日）——两说并写。
5. **3Com 创业（1979）**：离开 PARC，在 Palo Alto 自家公寓联合创办网络设备制造商 3Com；以太网随后成为局域网（LAN）主导标准。
6. **1980 Grace Hopper 奖**：ACM 授予，表彰其对局域网发展（specifically Ethernet）的贡献。
7. **1990 年离开 3Com**：董事会任命 Éric Benhamou 而非 Metcalfe 出任 CEO，Metcalfe 随即离开——按实载，勿写"功成身退"。
8. **评论员与投资人**：十年 InfoWorld 互联网专栏出版人/评论员；1996 联合创办 Pop!Tech 高管技术会议；2001 年成为风险投资人、Polaris Venture Partners 普通合伙人。
9. **教授与回归 MIT**：2011–2021 任 UT Austin Cockrell 工程学院 innovation and entrepreneurship 教授；2019 年赴南非作 Bernard Price Memorial Lecture；2022 年 6 月回归 MIT CSAIL 任 research affiliate 与 computational engineer（与 MIT Julia Lab 合作）。
10. **"吃掉自己的话"**：1995 年预测互联网将在次年"灾难性崩溃"并承诺言而无验则食言；1997 年第六届国际 WWW 大会主题演讲上把预测专栏放进搅拌机打碎后吞下（曾建议印在超大蛋糕上被观众否决）——保留自嘲语境。
11. **荣誉集**：IEEE Medal of Honor（1996，理由整句可引："exemplary and sustained leadership in the development, standardization, and commercialization of Ethernet"）、NAE 院士（1997）、National Medal of Technology（2003，"for leadership in the invention, standardization, and commercialization of Ethernet"）、Marconi Prize（2003）、National Inventors Hall of Fame（2007）、Computer History Museum Fellow（2008）。
12. **Metcalfe's law**：描述电信网络效应的定律；Marconi 授奖理由提及"his Law of network utility based on the square of the nodes"（节点平方的网络效用律）——按实载一句带过。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（以太网 — 蓝） | `#2E5A9E` | 1973 发明 / LAN 标准 |
| 分类色 2（分组通信学术线 — 青绿） | `#1E8E8E` | ALOHA / ARPAnet / 博士论文 |
| 分类色 3（创业商业线 — 琥珀） | `#D9A441` | 3Com / 风投 / Pop!Tech |
| 分类色 4（网络思想 — 玫瑰） | `#C0395B` | Metcalfe's law / 评论员岁月 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：总线拓扑（一条横向总线 + 垂直短节点线，稀疏分布），呼应「同轴电缆上多站接入」的以太网视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：暗夜求索 / 破晓而立（PARC 深夜的备忘录 → 以太网照亮局域网时代）
- **选定曲目**：Alex-Productions **Through the Darkness**（manifest 预分配，直接沿用）。
- **落地文件**：`turing/presentations/Robert_Metcalfe/ThroughtheDarkness.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「以太网共同发明人 · 美国」+ Metcalfe 1946– + 右上真实肖像（Metcalfe 2004 照）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 家庭 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1946–至今 生平纵览
4. **纽约少年与 MIT 双学位**（1946–1969）：陀螺仪技师之子、EE+工业管理两 BS
5. **Harvard 与 ARPAnet 之门**（1969–1972）：哈佛拒绝接入、Project MAC、论文被拒
6. **ALOHA 转机与博士论文**（1972–1973）：PARC 读 ALOHA 论文、修 bug、论文获接受
7. **以太网的诞生**（1973）：5-22 备忘录说 vs 11-11 首次运行说、coax as ether
8. **公式框：以太网与 Metcalfe's law**：冲突退避与节点平方律
9. **3Com 创业**（1979）：Palo Alto 公寓、LAN 主导标准
10. **离开 3Com 与转身**（1990）：Benhamou 任 CEO、InfoWorld 十年
11. **评论员·会议·风投**（1996–2010）：Pop!Tech、Polaris
12. **"吃掉自己的话"**（1995/1997）：崩溃预测与搅拌机时刻
13. **教授与回归 MIT**（2011–2022）：UT Austin、Bernard Price Lecture、CSAIL Julia Lab
14. **荣誉墙与 2022 图灵奖**：IEEE MoH 1996 引语、NMT 2003、Marconi 2003
15. **结尾**：从以太网到互联网生态的工程-商业双线遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **Co-inventor 红线**：以太网是 Metcalfe 与 **David Boggs** 共同发明（页面正文 "he and David Boggs invented Ethernet"、NYT 标题 Co-Inventor）——勿写 Metcalfe 独自发明。
- **两个生日并写**：1973-05-22（Metcalfe："Alto Ethernet" 备忘录）与 1973-11-11（Boggs：系统首次运行）——两说均保留，勿只取其一。
- **创业线红线**：任务提示中的"HyperLAN"**页面无载，禁写**；实载线为 ALOHA（夏威夷大学）→ Project MAC → Xerox PARC → 3Com。
- **1990 离职表述**：董事会任命 Benhamou 为 CEO、Metcalfe 离开——按实载，勿美化写"主动退位"。
- **哈佛论文被拒**：1972-06 答辩被拒（口述史料 "thrown out on my ass" 原话过粗，**立传用中性转述**"最初被拒绝"）→ PARC 修 ALOHA → 1973 获接受——叙事顺序勿倒置。
- **"吃掉自己的话"**：1995 预测 / 1997 WWW6 搅拌机事件有载可写，保留自嘲语境，勿写成尴尬丑闻或全然吹捧。
- **Metcalfe's law**：页面仅载"描述电信网络效应"+ Marconi 理由中的"square of the nodes"——勿扩展成现代修正公式叙事。
- **在世**：无卒年，写 `1946–`，留白。
- **引语**：可引 IEEE MoH / NMT / Marconi / CHM 授奖理由（页面有载）；"Alto Ethernet" 回忆段（"That is the first time Ethernet appears as a word..."）为 Metcalfe 回忆，可引但注明出处；其余无直接引语勿编造。
- **血统一笔带过**：英/爱尔兰/挪威血统有载，仅身份页或家庭页一句，不渲染。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 梅特卡夫（或 罗伯特·梅特卡夫） | 待写入 |
| name_en | Robert Metcalfe | 待写入 |
| birth_date | 1946-04-07 | 待写入 |
| death_date | 空（在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | engineer / entrepreneur | 待写入 |
| field_of_work | computer networks (Ethernet) / entrepreneurship | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Jeffrey P. Buzen（Harvard）
- **共同发明人**：David Boggs（以太网，1973，Xerox PARC）
- **其他**：页面未载师承网络与门生名单，**门生关系禁写**；妻 Robyn、二子属家庭成员不入关系库

## 8. 奖项清单

- Turing Award（2022，2023-03 宣布，"contributions to the invention of Ethernet technology"）
- ACM Grace Murray Hopper Award（1980，局域网发展贡献）
- IEEE Medal of Honor（1996，理由整句见亮点 11）
- NAE 院士（1997，因以太网发展当选）
- National Medal of Technology（2003，理由见亮点 11）
- Marconi Prize（2003，"For inventing the Ethernet and promulgating his Law of network utility based on the square of the nodes"）
- National Inventors Hall of Fame（2007）
- Computer History Museum Fellow Award（2008，理由见亮点 11）
- Internet Hall of Fame、IEEE Alexander Graham Bell Medal（infobox 载，年份页面未明示，勿编）

## 9. 机构清单

- 教育：MIT（EE + 工业管理双 BS 1969）、Harvard University（应用数学 MS 1970 / 计算机科学 PhD 1973）
- 任职：MIT Project MAC（读博期间）、Xerox PARC（–1979）、3Com（1979 联合创办；1990 离开）、InfoWorld（专栏十年，1990s）、Pop!Tech（1996 联合创办）、Polaris Venture Partners（2001 起 general partner）、UT Austin Cockrell 工程学院（2011–2021）、MIT CSAIL（2022 起 research affiliate / Julia Lab）

## 10. 终审清单

- [ ] 生卒 1946-04-07 / 在世留白，出生地 New York City
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | Xerox PARC · 3Com · MIT | Turing 2022`
- [ ] 以太网表述为与 David Boggs 共同发明，无"独发明"措辞
- [ ] 以太网两个生日（5-22 / 11-11）并写
- [ ] 创业线为 ALOHA→PARC→3Com，无"HyperLAN"内容
- [ ] 1990 离职表述中性（董事会另任 CEO）
- [ ] 哈佛论文被拒→ALOHA→接受的叙事顺序正确
- [ ] Metcalfe's law 表述不超出页面实载
- [ ] "吃掉自己的话"事件保留自嘲语境
- [ ] 肖像使用 `images/With_Bob_Metcalfe_cropped_.jpg`（全尺寸版，非 250px 版）
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2022/Robert Metcalfe/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 infobox 肖像（`images/With_Bob_Metcalfe_cropped_.jpg`，全尺寸；250px 前缀版不用）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：授奖理由与 Alto Ethernet 回忆段须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky / John_McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Aho/Ullman/Dongarra/Wigderson）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
