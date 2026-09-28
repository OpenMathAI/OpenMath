# J. Georg Bednorz（格奥尔格·贝德诺尔茨）立传提示词

> qid=Q76687 · 1950-05-16 –（在世）· 德国物理学家 · 20 世纪 · 1987 诺贝尔物理学奖（与 K. Alex Müller 共享）
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/J._Georg_Bednorz/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**`images.txt` 无任何人物肖像（仅国旗/站点图标）**：按既有经验经 Commons `Special:FilePath` / Wikipedia REST API 补 portrait（infobox 图注 "Bednorz in 2013"），404/返回 HTML 则换文件名重试，仍失败则装饰圆占位（`faIcon{user}\enspace Portrait`）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰（在世人物无去世地栏）。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「陶瓷晶格 / 超导转变」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Johannes Georg Bednorz（约翰内斯·格奥尔格·贝德诺尔茨）
- **生卒**：1950-05-16 生于诺伊恩基兴（Neuenkirchen，威斯特法伦，西德）——**在世，无卒日**
- **国籍**：德国（Germany；出生时西德）
- **身份**：物理学家；**高温超导电性的发现者之一**（与 K. Alex Müller）；IBM Fellow
- **家庭**：父 Anton Bednorz（小学教师），母 Elisabeth（钢琴教师），他是第四个孩子；父母均来自中欧西里西亚，二战动荡中被迫西迁；妻 Mechthild Wennemer（明斯特相识，1978 年随他赴苏黎世开始自己的博士学业）
- **童年趣闻**：父母试图让他亲近古典音乐，但他更爱动手——少年时代痴迷修摩托车和汽车（后来还是学会了小提琴和小号）；高中时代迷上化学，因为化学"能动手做实验"
- **教育轨迹**：
  - 1968 年入明斯特大学（University of Münster）学化学，因大班课堂中迷失方向，**转投冷门的结晶学**（矿物学分支，化学与物理的交汇处），1976 年毕业
  - 1972/1973 两度赴 IBM 苏黎世研究实验室做访问学生（明斯特教师 Wolfgang Hoffmann 与 Horst Böhm 安排）；1974 年赴苏黎世 6 个月完成硕士论文实验部分——生长 SrTiO₃（钙钛矿族陶瓷）晶体
  - 1976 年入苏黎世联邦理工学院（ETH Zurich）读博，导师 **Heini Gränicher 与 K. Alex Müller**，1982 年获博士，论文 *Isovalent and heterovalent ionic substitution in SrTiO3*
- **博士导师**：Heini Gränicher、K. Alex Müller（ETH Zurich）
- **研究领域**：物理学、高温超导体、材料科学

### 1.5 研究领域表（第 4 步入库用，与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | high-temperature superconductivity | 高温超导 | 1986 LaBaCuO 35 K 发现，1987 诺奖核心 |
| 1 | superconductivity | 超导 | 1982 年起加入 Müller 的研究主线 |
| 2 | ceramics | 陶瓷材料 | 诺奖理由 "superconductivity in ceramic materials" |
| 3 | materials science | 材料科学 | metadata field_of_work 明载 |

### 1.6 术语清单（第 9 步用）

| 英文 | 中文 | 风险 |
|------|------|------|
| high-temperature superconductivity | 高温超导 | 发现者 Bednorz 与 Müller 二人 |
| lanthanum barium copper oxide (LBCO) | 镧钡铜氧化物 | Tc = 35 K，高出此前纪录 12 K |
| perovskite | 钙钛矿 | SrTiO₃ 所属晶族 |
| critical temperature (Tc) | 临界温度 | 35 K 勿写错 |
| crystallography | 结晶学 | 明斯特转向的冷门专业（矿物学分支） |
| BSCCO / YBCO | 铋锶钙铜氧 / 钇钡铜氧 | 非 Bednorz/Müller 发现，勿混 |
| IBM Fellow | IBM 院士 | 1987 年授予 |
| Zeitschrift für Physik B | 《物理学杂志 B》 | 1986 年 6 月发表论文期刊 |

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **西里西亚移民之子（1950）**：父母在二战动荡中从西里西亚西迁至威斯特法伦；父亲小学教师、母亲钢琴教师——一个重视古典音乐却养出"摩托车修理工"的家庭。
2. **从化学到结晶学的转向（1968–1976）**：明斯特大学化学系大课堂中"感到迷失"，转入选址冷门的结晶学——化学与物理交界面上的小专业，日后成为他通往材料物理的窄门。
3. **IBM 苏黎世的初遇（1972–1974）**：1972 年暑期访问学生身份初见物理部负责人 K. Alex Müller；1974 年为硕士论文再赴苏黎世生长 SrTiO₃ 晶体，Müller 力劝他继续研究——**这次相遇决定了两个人今后的共同命运**；他一生感念 IBM 实验室"创造力与自由的氛围"对其科研方式的塑造。
4. **ETH 博士岁月（1976–1982）**：师从 Gränicher 与 Müller，论文仍是 SrTiO₃——钙钛矿氧化物从此成为他的"母语"；1978 年 Mechthild Wennemer 随他赴苏黎世读博（后成婚）。
5. **入职 IBM 与转题超导（1982–1983）**：1982 年博士毕业后正式加入 IBM 苏黎世实验室，加入 Müller 已在进行的超导电性研究；1983 年起两人开始对**过渡金属氧化物陶瓷**的电学性质做系统研究。
6. **1986：LaBaCuO 的 35 K（★ 核心页）**：在镧钡铜氧化物（LaBaCuO / LBCO）中诱导出超导电性，临界温度 Tc = 35 K——**比此前纪录整整高出 12 K**（此前 75 年间纪录从 1911 年的 11 K 缓慢爬升到 1973 年的 23 K，并停滞了 13 年）。
7. **点燃全球竞赛**：LBCO 发现刺激了同类铜氧化物（cuprate）高温超导研究浪潮，很快催生 BSCCO（Tc = 107 K）与 YBCO（Tc = 92 K）——液氮温区（77 K 以上）被突破，超导研究格局从此改写。
8. **1987 诺奖：史上最快的获奖速度之一**：1986 年 6 月发表于 *Zeitschrift für Physik B*，1987 年即与 Müller 共享诺贝尔物理学奖——Müller 篇 page.md 明载这是"科学类诺奖从发现到颁奖间隔最短的一次"（本篇如实呈现发现与获奖的年份跨度，勿自行断言"史上最快"措辞）。
9. **诺奖理由**："for their important break-through in the discovery of superconductivity in ceramic materials"（表彰他们在陶瓷材料超导电性发现方面的重要突破）。
10. **同年 IBM Fellow（1987）**：获奖当年即获 IBM 最高技术荣誉 IBM Fellow——企业实验室出身诺奖得主的典范。
11. **荣誉洪流（1986–1988）**：Marcel Benoist Prize（1986，瑞士）→ 诺奖（1987）→ Fritz London Memorial Prize / Dannie Heineman Prize / Klung Wilhelmy Science Award（均 1987）→ International Prize for New Materials / EPS Europhysics Prize（均 1988）——两年之内横扫超导界全部主要奖项。
12. **晚年荣誉与在世留白**：瑞士物理学会荣誉会员（2011）、美国国家科学院国际会员（2018）、德国联邦十字勋章等；2013 年照片仍活跃于公众视野——在世人物生卒栏留白处理。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（铜氧赭红） | `#8B3A2A` | 陶瓷 / 铜氧化物晶格 / 实验台上的温度 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（早年与家庭 — 棕） | `#795548` | 西里西亚迁徙 / 摩托车与化学 / 结晶学转向 |
| 分类色 2（钙钛矿岁月 — 青） | `#00796B` | SrTiO₃ / ETH 博士 / 钙钛矿氧化物 |
| 分类色 3（高温超导突破 — 橙红） | `#D84315` | 1986 LaBaCuO / 35 K / 全球竞赛 |
| 分类色 4（诺奖与荣誉 — 金褐） | `#9C7A1E` | 1987 诺奖 / IBM Fellow / 荣誉洪流 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「陶瓷晶格中的超导转变——冷与热的临界」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：明亮 / 鼓舞 / 年轻突破（青年研究者在冷门窄门中坚持后的爆发）
- **选定曲目**：Alex-Productions **Awaken**（高受众 / 鼓舞 / 明亮），匹配"结晶学小专业出身的青年博士，坚持氧化物陶瓷路线终至 35 K"的突破气质。
- **落地文件**：`physicist/presentations/20th_century/Georg_Bednorz/Awaken.wav`（复制自音乐库，不入 git）。
- **匹配理由**：Bednorz 是 1987 年故事中"年轻的一方"——从修摩托车的少年到 35 K 的发现者，明亮鼓舞的 Awaken 匹配其逆袭与突破气质；与组内其余四曲（SEA / Cinematic Experience / Mirage / Nostalgia）区隔。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「高温超导发现者 · 德国」+ Georg Bednorz 1950– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域；在世人物不设去世地）
3. **核心贡献概览**（`\hookslide`）：钙钛矿岁月 / 高温超导突破 / 诺奖与荣誉 / IBM 企业实验室
4. **早年：西里西亚迁徙与摩托车**（1950–1968）：父母西迁、动手少年、高中化学
5. **明斯特：从化学到结晶学**（1968–1976）：大课堂迷失、转向冷门结晶学
6. **IBM 苏黎世的初遇**（1972–1974）：访问学生、初见 Müller、SrTiO₃ 晶体
7. **ETH 博士岁月**（1976–1982）：Gränicher 与 Müller 双导师、SrTiO₃ 论文、Mechthild 赴苏黎世
8. **入职 IBM 与转题超导**（1982–1983）：加入 Müller 的超导研究、系统研究过渡金属氧化物
9. **1986：LaBaCuO 的 35 K**（★ 核心页，配高斯表格页：`此前纪录 ｜ 1986 发现 ｜ 意义`）：Tc 35 K、高出 12 K、*Zeitschrift für Physik B*
10. **点燃全球竞赛**：Tanaka（东京大学）与 Paul Chu（休斯顿大学）独立确认 → BSCCO 107 K / YBCO 92 K → 液氮温区
11. **1987 诺奖**：与 Müller 共享、诺奖理由原文、"发现到颁奖最短间隔"（page.md 表述）
12. **IBM Fellow 与荣誉洪流**（1986–1988）：两年横扫超导界主要奖项
13. **晚年荣誉与在世留白**（2011–2018）：瑞士物理学会 / NAS 国际会员、2013 年照片
14. **荣誉与遗产**：35 K → 92 K 的温区跃迁、铜氧化物超导家族、"运气与坚持"的发现叙事
15. **结尾**：在世、"从冷门结晶学到高温超导"——35 K 改写 75 年纪录的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **★ 在世人物**：page.md 无卒日——生卒栏写"1950-05-16 –（在世）"，**禁写任何去世信息**；2013 年照片为最新可考影像。
- **★ 国籍口径冲突**：总名单国籍列标 Switzerland，但 page.md infobox 与 metadata.json 均为 **Germany**——以 page.md 为准写「德国」（出生西德诺伊恩基兴）；此冲突写入本表供总名单 Review 时核对。
- **诺奖理由中文口径**：用总名单"表彰他们在陶瓷材料超导电性发现方面的重要突破"；英文原文 "for their important break-through in the discovery of superconductivity in ceramic materials"。
- **"最快获奖"断言**：本篇 page.md 无此表述（Müller 篇 page.md 有 "the shortest time between the discovery and the prize award for any scientific Nobel"）——本篇只写"1986 发现、1987 获奖"的年份事实，**勿在本篇断言"史上最快"**；如需该评价须注明出自 Müller 篇事实基准。
- **发现年份层次**：1983 年起系统研究 → 1986 年实现 LaBaCuO 超导（35 K）→ 1986 年 6 月发表 → 1987 年获奖——四个时间节点勿混。
- **"35 K 高出 12 K"**：page.md 原文 "a full 12 K higher than the previous record"，此前纪录 23 K（1973）——数字勿写错。
- **BSCCO / YBCO 的发现者**：page.md 只说 LBCO 发现"刺激了研究、很快催生"这两种材料，**未载发现者姓名**——勿写成 Bednorz/Müller 发现了 BSCCO 或 YBCO。
- **硕士论文细节**：1974 年赴苏黎世 6 个月完成的是**硕士论文的实验部分**（生长 SrTiO₃ 晶体）——勿写成"硕士论文在 IBM 完成"。
- **博士导师两位**：Heini Gränicher **与** K. Alex Müller 共同指导——勿只写 Müller；社会关系入库两条 advisor 均建。
- **妻子身份**：Mechthild Wennemer 是他在明斯特结识、1978 年赴苏黎世读博（后成妻）——她本人读博的机构 page.md 未载，勿写"在 ETH 读博"。
- **引语红线**：本篇 page.md 无 Bednorz 任何直接引语——**全部间接转述**，中文引号内不得出现"贝德诺尔茨说……"；"创造力与自由的氛围"是他对 IBM 氛围的感念（page.md 转述），亦用间接表述。
- **共享奖项注明**：International Prize for New Materials（1988）与 Paul Chu、Müller 共享；EPS Europhysics Prize（1988）与 John Clarke、Jun Kondō、Müller 共享——引用出处表格 notes 有载，勿写成独得。
- **metadata 噪声**：metadata.json award 列表含 Robert Wichard Pohl Prize、联邦大十字勋章、McGroddy Prize 等，但 page.md 获奖表未列年份/引语——§8 奖项清单可列名但年份标注"年份 page.md 未载"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76687 | 待写入 |
| name_zh | 贝德诺尔茨（或 格奥尔格·贝德诺尔茨） | 待写入 |
| name_en | J. Georg Bednorz（Johannes Georg Bednorz） | 待写入 |
| birth_date | 1950-05-16 | 待写入 |
| death_date | （空——在世） | 待写入 |
| nationality | Germany | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | physics / high temperature superconductor / materials science | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：K. Alex Müller（ETH Zurich，亦为诺奖搭档与终身合作者——advisor-student，direction: advisor=对方是导师）；Heini Gränicher（ETH Zurich 共同导师——advisor-student）
- **诺奖搭档**：K. Alex Müller（1987 共享——co-honored / collaborator，"1983 年起系统研究氧化物陶瓷、1986 共同发现 LaBaCuO 35 K"）
- **竞赛与确认者**：Shoji Tanaka（东京大学，独立确认）、Paul C. W. Chu（休斯顿大学，独立确认并实现 YBCO 93 K——colleague，共享 International Prize for New Materials）、John Clarke、Jun Kondō（共享 EPS Europhysics Prize）
- **家庭**：妻 Mechthild Wennemer（spouse）
- **父母**：Anton Bednorz（父，小学教师）、Elisabeth（母，钢琴教师）
- **诺奖同届**：1987 年仅 Bednorz 与 Müller 两人共享，无第三人

## 8. 奖项清单

- 诺贝尔物理学奖（1987，与 K. Alex Müller 共享）
- Marcel Benoist Prize（1986，瑞士 Marcel Benoist 基金会）
- Fritz London Memorial Prize（1987，杜克大学）
- Dannie Heineman Prize（1987，哥廷根科学院）
- Klung Wilhelmy Science Award（1987，"发现空前高转变温度的新一类超导体"）
- International Prize for New Materials（1988，美国物理学会，与 Chu、Müller 共享）
- EPS Europhysics Prize（1988，欧洲物理学会，与 Clarke、Kondō、Müller 共享）
- IBM Fellow（1987）
- （metadata.json 载、page.md 获奖表未列年份：Robert Wichard Pohl Prize、James C. McGroddy Prize for New Materials、德国联邦大十字勋带星勋章、北威州功绩勋章、明斯特/萨尔茨堡/雷根斯堡/第比利斯国立大学荣誉博士、美国物理学会会士）

## 9. 机构清单

- 教育：明斯特大学（1968–1976，化学→结晶学）、IBM 苏黎世研究实验室（1972/1973/1974 访问学生）、苏黎世联邦理工学院 ETH Zurich（博士 1982，导师 Gränicher 与 Müller）
- 任职：IBM 苏黎世研究实验室（1982 年起；研究超导电性；1987 年起 IBM Fellow）
- 会籍：瑞士物理学会荣誉会员（2011）、美国国家科学院国际会员（2018）

## 10. 终审清单

- [ ] 生卒 1950-05-16 /（在世留白），出生地 Neuenkirchen（威斯特法伦）
- [ ] 国籍写「德国」并注明与总名单 Switzerland 的冲突待核对
- [ ] 诺奖理由用总名单中文口径："表彰他们在陶瓷材料超导电性发现方面的重要突破"
- [ ] "1983 系统研究 → 1986 发现 35 K → 1986-06 发表 → 1987 获奖"时间线准确
- [ ] "高出此前纪录 12 K（23 K，1973）"数字准确
- [ ] BSCCO / YBCO 不写为 Bednorz/Müller 的发现
- [ ] 博士导师写 Gränicher 与 Müller 两人
- [ ] 全篇无伪引语（page.md 无直接引语，一律间接转述）
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/J._Georg_Bednorz/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 无肖像 → 经 Commons `Special:FilePath` / REST API 补 "Bednorz in 2013" 肖像，失败则装饰圆占位
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：全篇不得出现加引号的 Bednorz 原话
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐（在世人物信息网格适配）
- [ ] 中文标点 / 断行 / 间距统一（半角引号 " "）
- [ ] 与同批次物理学家（Alex_Muller / Leon_Lederman / Melvin_Schwartz / Jack_Steinberger）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
