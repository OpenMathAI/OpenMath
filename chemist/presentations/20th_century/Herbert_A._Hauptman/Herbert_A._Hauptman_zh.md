# Herbert A. Hauptman（赫伯特·豪普特曼）立传提示词

> qid=Q107422 · 1917-02-14 – 2011-10-23 · 美国数学家 · 20 世纪 · 诺贝尔化学奖（1985，与 Jerome Karle 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Herbert_A._Hauptman/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + Sanger 式时间线 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 page.md 图注照片取：2009 年照片；若下载失败用装饰圆占位并注记）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{square-root-alt}\enspace 用数学解开晶体的相位\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Herbert Aaron Hauptman）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「衍射点阵 / 相位」母题——离散圆点暗示 X 射线衍射图上的斑点分布。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（相位问题：结构因子振幅可知而相位丢失；概率法与 Sayre 方程；邻域原理）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Herbert Aaron Hauptman（中文惯称：赫伯特·豪普特曼）
- **生卒**：1917-02-14 生于美国纽约市 → 2011-10-23 逝于纽约州布法罗（Buffalo），享年 94
- **国籍**：United States（美国）
- **身份**：数学家 / 晶体学家（mathematician, crystallographer；metadata 另载 chemist、university teacher、philosopher）；Hauptman-Woodward 医学研究所总裁；University at Buffalo 生物物理科学系研究教授与计算机系兼职教授
- **家庭**：纽约犹太家庭的长子；父 Israel Hauptman、母 Leah（娘家姓 Rosenfeld）；1940-11-10 娶 Edith Citrynell，育二女 Barbara（1947）与 Carol（1950）
- **教育轨迹**：
  - Townsend Harris High School（少年时期醉心科学与数学）
  - City College of New York：BS 1937（1936 年获该校 Belden Prize in Mathematics）
  - Columbia University：数学 MA 1939
  - 战后入 University of Maryland, College Park 博士项目：PhD 1955（数学，论文为数论分类方向）
- **导师**：metadata 载 doctoral advisor 为 Jerome Karle 与 Richard Albert Good——**正文 page.md 未载导师**，Beamer 只呈现"University of Maryland PhD 1955"与"NRL 与 Karle 合作"的实载事实（详见 §5、§7）
- **博士**：1955，University of Maryland, College Park
- **研究领域**：数学——X 射线晶体学的**直接法**（direct methods）、相位问题、概率方法、数论

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **纽约犹太家庭长子（1917）**：生于纽约市，Leah 与 Israel Hauptman 的第一个孩子。
2. **Townsend Harris 与 CCNY（1930s）**：少年即醉心科学与数学；1936 年 CCNY 数学 Belden Prize；1937 年 BS 毕业。
3. **Columbia 数学硕士（1939）**。
4. **军旅与战后（1940s）**：二战服役（page.md 表述 "After the war..."，具体军旅细节无载，略写）；1947 年起任 Naval Research Laboratory（NRL）数学家与多部门主管。
5. **与 Karle 的合作（战后）**：在华盛顿 NRL 与 Jerome Karle 开启长期合作——数学 + 物理化学的互补组合，正面强攻 X 射线晶体学的**相位问题**（phase problem）。
6. **半工半读的博士（1955）**：同期入读马里兰大学，1955 年以数论分类论文获 PhD。
7. **1953 年里程碑专著**：与 Karle 合著 *Solution of the Phase Problem I. The Centrosymmetric Crystal*——核心思想是经由 Sayre 方程的发展引入**概率方法**。
8. **"不可解"的骂名**：当时相位问题被普遍认为不可解——其工作一度饱受批评；他们仍奠立了直接法（direct methods）的基础。
9. **1985 诺贝尔化学奖（与 Karle 共享）**：瑞典皇家科学院表彰两人把这一数学方法应用于广泛化学结构——直接法从此**例行**用于解析复杂结构（page.md 口径）。
10. **布法罗岁月（1970–2011）**：加入 Buffalo 医学基金会（后更名 Hauptman-Woodward 医学研究所）晶体学组，1972 年任研究主任；早年提出**邻域原理**（neighborhood principle）与**扩展概念**（extension concept），此后数十年持续发展。
11. **第五位以其名命名的机构**：Hauptman-Woodward Medical Research Institute——生前一直任总裁；2011-10-23 于布法罗辞世。
12. **世俗人文主义者（2003）**：作为无神论者与世俗人文主义者，成为签署《人文主义宣言》（Humanist Manifesto 2003）的 22 位诺奖得主之一；2006 年获美国人文主义协会 Isaac Asimov Science Award。
13. **学术公共服务**：1969–1970 年任华盛顿哲学学会会长；1979–1980 年任独立研究机构协会主席；170 余篇论著。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松灰绿 deep pine） | `#2F5D50` | 相位问题的深奥与概率方法的冷静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（相位问题 badgePhase） | `#2E5A9E` | 蓝相位问题 / 结构因子 |
| 分类色 2（直接法 badgeDirect） | `#C0395B` | 玫瑰直接法 / 概率方法 / Sayre 方程 |
| 分类色 3（晶体学应用 badgeCrystal） | `#D97B29` | 琥珀晶体结构解析 / 邻域原理 |
| 分类色 4（数学底色 badgeMath） | `#1E4E79` | 藏青数论 / 数学训练 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「衍射斑点 / 相位复原」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`；执行 Beamer 时复制为本目录 `With_Me.wav`，勿直接引用外部路径）
- **风格**：陪伴感 / 坚定 / 双人行
- **匹配理由**：
  - "With Me（与我同行）" 匹配其成就的合作本质——与 Jerome Karle 数十年同行，两人共享 1985 诺奖
  - "坚定" 匹配逆流而上的科研叙事——全世界都说相位问题不可解，他们用概率方法正面攻克
  - "陪伴感" 匹配其布法罗四十年——一座研究所、一任总裁、一生只做一件事
- **时长对齐**：ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 用数学解开晶体相位的人 / Herbert A. Hauptman 1917–2011 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士/领域/荣誉）
03  豪普特曼的一生 — Sanger 式时间线（10 节点：1917→1937→1939→1947→1953→1955→1970→1972→1985→2011）
04  纽约数学少年 (1917–1939) — 表格「时间|事件|结果」（Belden Prize / CCNY / Columbia）
05  NRL 与 Karle 合作（战后–1955） — 表格「人物|互补|结果」（数学+物理化学强攻相位问题）
06  1953 里程碑专著 — 表格「问题|方法|结果」+ 公式框：相位问题（振幅可知、相位丢失）
07  概率方法与直接法 — 表格「旧观念|新方法|结果」+ 公式框：Sayre 方程与概率方法
08  1985 诺贝尔化学奖（与 Karle 共享） — 表格「人物|贡献|结果」+ 获奖口径公式框（page.md 转述口径）
09  邻域原理与扩展概念 — 表格「概念|内容|意义」
10  Hauptman-Woodward 研究所 — Sanger FFT 页式流程图（1970 加入 → 1972 研究主任 → 终身总裁 → 2011 辞世）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Patterson Award 1984 / Nobel 1985 / Dirac Medal 1991 / NAS 1988 / 九所大学荣誉博士）
12  人文主义者 — 表格「年份|事件|意义」（2003 Humanist Manifesto / 2006 Asimov Award / 学会服务）
13  遗产：直接法改变晶体学 — 四分类遗产盒 + 公式框：直接法例行解析复杂结构
14  结尾 — 「晶体把答案写在衍射图上，数学负责把它读出来。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1985 共享结构 | 与 **Jerome Karle 共享**（page.md 两处明载 "jointly with Jerome Karle"）——勿写独享，也勿写第三人（1985 化学奖仅两人） |
| 获奖理由 | **官方 citation 英文整句页面无载**——禁止杜撰；用 page.md 转述口径：发展了测定晶体结构的数学方法（直接法），瑞典皇家科学院据此授奖 |
| Karle 的关系 | 正文口径是与 Karle 在 **NRL 的合作者**（collaboration）；"doctoral advisor: Jerome Karle, Richard Albert Good" 仅 metadata.json 有载，正文 infobox 无导师栏——**Karle 入 colleague + co-honored 两行；Good 不入库**（详见 §7） |
| 出生地与卒地 | 生于纽约市、逝于布法罗——勿混；享年 94 |
| 日期噪声 | metadata.json 生卒含 "1917-00-00" / "2011-00-00" 噪声值——一律取正文 1917-02-14 / 2011-10-23 |
| 数学家的化学奖 | 他是**数学家**（PhD 数论方向）获诺贝尔化学奖——交叉叙事是本篇主轴；但勿写"唯一/第一位数学家获化学奖"类页面无载断言 |
| 1953 专著 | *Solution of the Phase Problem I. The Centrosymmetric Crystal* 与 Karle 合著——最重要的思想是**经 Sayre 方程发展引入概率方法**；勿写 Sayre 本人参与其研究 |
| 直接法地位 | page.md：Hauptman 的直接法 "routinely used to solve complicated structures"（例行使用）——勿写"彻底取代其他方法" |
| 军旅 | page.md 仅 "After the war..."——具体服役细节无载，略写勿编 |
| Humanist Manifesto | 2003 年 **22 位诺奖得主之一**签署——勿写"组织者/发起人" |
| 引语 | 本地页面**无任何其个人直接引语**——中文引号内容一律间接转述 |
| 荣誉博士数 | 实载九所（Maryland 1985 / CCNY 1986 / Parma 1989 / D'Youville 1989 / Bar-Ilan 1990 / Columbia 1990 / Lodz 1992 / Queen's 1993 / SUNY Buffalo 2009）——逐条对照勿凑整 |
| Dirac Medal | **UNSW（新南威尔士大学）Dirac Medal for the Advancement of Physics, 1991**——勿与 ICTP Dirac Medal 混淆 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q107422 | ✅ |
| name_zh | 赫伯特·A·豪普特曼 | ✅ |
| name_en | Herbert A. Hauptman | ✅ |
| birth_date | 1917-02-14 | ✅ |
| death_date | 2011-10-23 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | mathematician | ✅ |
| field_of_work | mathematics（person_field 细分：mathematics / X-ray crystallography / direct methods / structural chemistry，带 rank） | ✅ |
| has_biography | 0（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**合作者 / 共同得主 / 家人**（只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Jerome Karle | 无向 | 1985 诺贝尔化学奖共同得主（jointly） |
| colleague | Jerome Karle | 无向 | 战后于华盛顿 Naval Research Laboratory 开启长期合作；1953 合著相位问题专著 |
| spouse | Edith Citrynell | 无向 | 1940-11-10 结婚，育二女 |

> **禁入库名单（metadata.json-only）**：doctoral_advisor 含 Richard Albert Good，正文 page.md 未载导师——**不予入库**；Jerome Karle 的 advisor 身份同样仅 metadata 有载，按正文口径只入 colleague + co-honored，**不建 advisor-student 行**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1985，与 Jerome Karle 共享）
- Belden Prize in Mathematics, City College of New York（1936）
- Scientific Research Society of America Pure Science Award, Naval Research Laboratory（1959）
- Patterson Award, American Crystallographic Association（1984）
- UNSW Dirac Medal for the Advancement of Physics（1991）
- Jacob F. Schoellkopf Medal, ACS Western New York Chapter（1986）
- Norton Medal, SUNY（1986）；Cooke Award, SUNY（1987）；Citizen of the Year Award, Buffalo Evening News（1986）；Golden Plate Award（1986）
- National Academy of Sciences 院士（1988）
- Humanist Laureate Award, International Humanist and Ethical Union（1988）；Isaac Asimov Science Award, American Humanist Association（2006）
- 荣誉博士：University of Maryland（1985）、CCNY（1986）、University of Parma（1989）、D'Youville College（1989）、Bar-Ilan University（1990）、Columbia University（1990）、Technical University of Lodz（1992）、Queen's University, Kingston（1993）、SUNY at Buffalo（2009）

## 9. 机构清单

- 教育：Townsend Harris High School、City College of New York（BS 1937）、Columbia University（MA 1939）、University of Maryland, College Park（PhD 1955）
- 任职：Naval Research Laboratory, Washington D.C.（1947–，数学家与多部门主管）；Medical Foundation of Buffalo → Hauptman-Woodward Medical Research Institute（1970–，研究主任 1972，总裁至去世）；University at Buffalo（生物物理科学系研究教授 + 计算机系兼职教授）
- 学术服务：President, Philosophical Society of Washington（1969–1970）；President, Association of Independent Research Institutes（1979–1980）

## 10. 终审清单

- [ ] 生卒 1917-02-14 / 2011-10-23（享年 94），出生地纽约市、去世地布法罗
- [ ] 1985 与 **Jerome Karle 共享**；获奖理由用 page.md 转述口径，官方 citation 整句禁写
- [ ] Karle = colleague + co-honored 双行；Richard Good 不入库
- [ ] 1953 专著与概率方法/Sayre 方程表述准确；直接法 "routinely used" 口径
- [ ] 数学 PhD（数论）与化学奖的交叉叙事成立；无"第一/唯一"断言
- [ ] 全文无直接引语（页面无载）——中文引号内容全部间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Herbert_A._Hauptman/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像已就位或装饰圆占位并注记
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：全文无直引（页面无其原话）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`（执行者不改）。
