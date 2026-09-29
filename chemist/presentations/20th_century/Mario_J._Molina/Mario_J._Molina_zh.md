# Mario J. Molina（马里奥·莫利纳）立传提示词

> qid=Q19045 · 1943-03-19 – 2020-10-07 · 墨西哥物理化学家 · 20 世纪 · 诺贝尔化学奖（1995，与 Paul J. Crutzen、F. Sherwood Rowland 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Mario_J._Molina/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `pages/Mario_J._Molina/images.txt` 下载至 `images/`，404 则用装饰圆占位并在 Review-1 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe-americas}\enspace 守护臭氧层的人\enspace·\enspace 墨西哥`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（西班牙姓名序 Molina-Pasquel + Henríquez）、国籍、出生地/去世地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），呼应「自由基链式反应」母题——一个氯原子圆点在臭氧点阵间穿行引爆连锁，一圈圈扩散。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 " "。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Mario José Molina-Pasquel Henríquez（西班牙姓名序：父姓 Molina-Pasquel、母姓 Henríquez；中文惯称：马里奥·莫利纳）
- **生卒**：1943-03-19 生于墨西哥城 → 2020-10-07 逝于墨西哥城（心脏病发作），享年 77
- **国籍**：Mexico（墨西哥）→ United States（metadata 并列）
- **身份**：物理化学家（physical chemist）；CFC 破坏臭氧层理论共同提出者；**首位墨西哥出生的化学诺奖得主、第三位墨西哥出生的诺贝尔奖得主**（页面明载口径）
- **家庭**：Roberto Molina Pasquel（律师、外交官，曾任驻埃塞俄比亚、澳大利亚、菲律宾大使）与 Leonor Henríquez 之子；1973-07 娶同门化学家 Luisa Y. Tan（Berkeley 博士期间相识），1977 年生子 Felipe Jose Molina，2005 离婚；2006-02 再娶 Guadalupe Álvarez
- **教育轨迹**：
  - 墨西哥城小学与中学；11 岁赴瑞士寄宿学校 Institut auf dem Rosenberg（学德语；此前曾想当职业小提琴手）
  - National Autonomous University of Mexico（UNAM），化学工程 BS（1965）
  - Albert Ludwig University of Freiburg（西德），聚合动力学两年
  - University of California, Berkeley（1968 入学），物理化学 PhD（1972）
- **导师**：George C. Pimentel（博士导师；化学激光研究）
- **博士**：1972，《Vibrational Populations Through Chemical Laser Studies: Theoretical and Experimental Extensions of the Equal-gain Technique》
- **研究领域**：物理化学、大气化学、化学工程、环境科学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **浴室里的实验室（1943–1960）**：把家中浴室改成小实验室；姨妈 Ester Molina（职业化学家）呵护其兴趣——曾想当职业小提琴手，化学之爱最终胜出。
2. **瑞士少年（11 岁）**：11 岁被送进瑞士寄宿学校 Institut auf dem Rosenberg，学会德语；初到时失望于同学缺少对科学的共同兴趣。
3. **UNAM 与弗莱堡（1960s）**：UNAM 化学工程 BS（1965）；弗莱堡两年聚合动力学——毕业后还回墨西哥在母校开创了第一个化学工程课程项目（页面明载）。
4. **Berkeley 与化学激光（1968–1972）**：Pimentel 门下研究化学激光分子动力学、化学反应与光化学反应产物的内能分布——"hot atom" 化学的底功。
5. **奔赴 Irvine（1973）**：博士后加入 UC Irvine 的 F. Sherwood Rowland 实验室，继续 "hot atom" 化学；同年娶 Luisa Tan。
6. **关键之问**：Molina 的基本科学问题——"What is the consequence of society releasing something to the environment that wasn't there before?"（页面原文）
7. **CFC-臭氧理论（1973–1974）**：紫外光子可分解 CFC 释放氯原子；Cl· + O₃ → ClO· + O₂，ClO· 又与 O₃ 反应再生 Cl·——氯原子作为**催化剂**循环破坏臭氧；1974 与 Rowland 在 Nature 共同发表。
8. **从论文到公共辩论（1974）**：150 页 AEC 报告 + 大西洋城 ACS 记者会，呼吁全面禁止向大气排放 CFC——国家性关注由此点燃。
9. **争议与验证（1976–1985）**：产业界群起质疑；1976 美国国家科学院综述后共识渐成；1985 年 Joseph Farman 团队在 Nature 发表南极臭氧长期衰减证据；Molina 随后率队研究南极臭氧快速损耗成因——发现平流层条件正是氯活化的温床。
10. **蒙特利尔议定书（1987）**：56 国签署削减 CFC 生产与使用的协议；其后逐步走向全球淘汰 CFC——同时减缓了臭氧损耗与气候变化。
11. **1995 诺贝尔化学奖**：与 Paul J. Crutzen、F. Sherwood Rowland 共享，citation 明载 "their work in atmospheric chemistry, particularly concerning the formation and decomposition of ozone"。
12. **学术漫游者（1974–2004）**：UC Irvine → JPL/Caltech → MIT（地球大气行星科学系与化学系双聘）→ 2004-07-01 UCSD 化学与生物化学系 + Scripps 海洋学研究所大气科学中心。
13. **科学大使（2000–2020）**：2000 入选教皇科学院；2005 在墨西哥城创办 Mario Molina 能源与环境战略研究中心并任所长；墨西哥总统培尼亚·涅托气候政策顾问；2008 被 Obama 点名组建环境过渡团队、任 PCAST 成员；与 Ramanathan、Zaelke 合著《Well Under 2 Degrees Celsius》（2017）；参与教皇通谕《Laudato Si'》内容贡献；2020 年与 Renyi Zhang 等发表新冠气溶胶传播 PNAS 论文；小行星 9680 Molina 以其命名。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（松绿 pinegreen） | `#175E54` | 臭氧层守护与环境的松绿（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（CFC-臭氧理论 badgeCFC） | `#1E7A6F` | 青 Cl· 链式反应 / Nature 1974 |
| 分类色 2（科学到政策 badgePolicy） | `#37548D` | 蓝蒙特利尔议定书 / AEC 报告 |
| 分类色 3（学术漫游 badgeCampus） | `#D97B29` | 琥珀 Irvine→JPL→MIT→UCSD |
| 分类色 4（科学大使 badgeEnvoy） | `#C0395B` | 玫瑰墨西哥中心 / 教皇科学院 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「链式反应」——一点穿行、连环扩散。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（清单指定 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，不要复制 wav 文件，由 Makefile 侧引用）
- **风格**：辽阔 / 平静 / 大气层之海
- **匹配理由**：
  - "SEA" 匹配主题意象——臭氧层是包裹地球的大气之海，莫利纳是这片海域的守望者
  - "辽阔" 匹配其跨越大洋的人生——墨西哥城 → 瑞士 → 弗莱堡 → Berkeley → 全球政策舞台
  - "平静" 匹配叙事基调——从基础光化学到改变世界的公约，是耐心的科学长跑
- **时长**：以文件实际时长为准（> 15 页 × 7 秒 ≈ 105 秒即可），ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 守护臭氧层的人 / Mario J. Molina 1943–2020 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/教育/博士导师/出生地/去世地/领域/机构/荣誉）
03  莫利纳的一生 — 时间线（10 节点：1943→1965→1972→1973→1974→1976→1985→1987→1995→2020）
04  墨西哥城与瑞士少年 (1943–1965) — 表格「时间|事件|结果」
05  Berkeley：化学激光 (1968–1973) — 表格「导师|课题|结果」
06  CFC-臭氧理论 (1973–1974) — 表格「问题|机理|结果」+ 公式框：Cl· + O₃ → ClO· + O₂；ClO· + O₃ → Cl· + 2O₂
07  从论文到公共辩论 (1974–1976) — 表格「场合|行动|反响」（Nature / AEC 报告 / ACS 记者会 / NAS 综述）
08  南极臭氧洞与验证 (1985–1987) — 表格「发现|跟进|结果」+ 公式框：蒙特利尔议定书 1987（56 国）
09  1995 诺贝尔化学奖 — 表格「得主|贡献|结果」（三人共享；citation 原句）
10  学术漫游者 (1974–2004) — 表格「机构|角色|领域」（UCI / JPL-Caltech / MIT / UCSD-Scripps）
11  科学大使 (2000–2020) — 表格「平台|角色|产出」（教皇科学院 / Mario Molina 中心 / PCAST / Well Under 2°C）
12  荣誉之殿 — 表格「类别|代表|意义」（Tyler 1983 / NASA 1989 / Willard Gibbs 1998 / 总统自由勋章 2013 / Champions of the Earth 2014）
13  遗产 — 四分类遗产盒 + 公式框：小行星 9680 Molina + 「首位墨西哥出生的化学诺奖得主」（页面口径）
14  结尾 — 「看不见的分子，看得见的责任。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 1995 与 Crutzen、Rowland **三人共享**；citation 页面原句 "their work in atmospheric chemistry, particularly concerning the formation and decomposition of ozone"；Molina 的份额是 **CFC 破坏臭氧**——勿把 Crutzen 的 NOx 工作算到他头上 |
| 「第一/第三」 | 「首位墨西哥出生的化学诺奖得主、第三位墨西哥出生的诺奖得主」为**页面明载口径**，可写但注明按 Wikipedia 页面 |
| 链式反应 | Cl· 不被消耗、作**催化剂**循环破坏 O₃——两个反应式（Cl· + O₃ → ClO· + O₂；ClO· + O₃ → Cl· + 2O₂）勿写错方向 |
| Rowland 关系 | 1973 加入 Rowland 实验室是**博士后**（postdoctoral fellow）；1974 Nature 论文共同作者；1995 又共同获奖——colleague/advisor 与 co-honored 双行 |
| Farman 与莫利纳 | 1985 南极臭氧洞由 **Joseph C. Farman** 等发表；Molina 是**随后**率队研究成因——勿写成 Molina「发现」臭氧洞 |
| 议定书 | 蒙特利尔议定书 **1987 年**由 56 国签署——勿写「Molina 发起签署」；他对后续气候协定的贡献（页面表述 helped shape）不等于巴黎协定的作者 |
| 姓名序 | 全名 **Mario José Molina-Pasquel Henríquez**（父姓 Molina-Pasquel、母姓 Henríquez）；署名 Mario J. Molina——勿把 Pasquel 当成名 |
| 婚姻 | Luisa Y. Tan：1973-07 结婚（Berkeley 相识、同行化学家）→ 2005 离婚；Guadalupe Álvarez：2006-02 结婚——两段勿混；子 Felipe（1977） |
| 学位 | UNAM BS 1965（化学工程）→ 弗莱堡两年（聚合动力学，页面未载学位名）→ Berkeley PhD **1972**（化学激光，Pimentel）——弗莱堡学位禁写 |
| 去世 | 2020-10-07 逝于墨西哥城，**心脏病发作**，享年 77——出生与去世同城；勿写其他死因 |
| 引语红线 | 可引用（页面原文）：科学之问句、Obama 颁勋章新闻稿句、citation 原句；中文引号内不得出现无法在 page.md 溯源的「原话」 |
| 政治场合 | Obama 过渡团队/PCAST、墨西哥总统顾问、教皇科学院——客观一句带过即可，不展开政治评价；Luis E. Miramontes 合照仅为合影，**不入库关系** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q19045 | ✅ |
| name_zh | 马里奥·莫利纳 | ✅ |
| name_en | Mario J. Molina | ✅ |
| birth_date | 1943-03-19 | ✅ |
| death_date | 2020-10-07 | ✅ |
| nationality | Mexico（rank 0）/ United States（rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：atmospheric chemistry / physical chemistry / chemical engineering / environmental chemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 家人 / 同事 / 共同得主 / 门生**（★ 只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George C. Pimentel | 师→生（博士导师） | Berkeley 1972，化学激光研究 |
| advisor-student | F. Sherwood Rowland | 师→生（博士后导师） | 1973 UC Irvine 博士后；1974 Nature 共同发表 CFC-臭氧理论 |
| advisor-student | Renyi Zhang | 生→师（学生） | infobox Doctoral students；2020 合著新冠气溶胶传播 PNAS 论文 |
| spouse | Luisa Y. Tan | 无向 | 1973-07 结婚（Berkeley 同门化学家），1977 年生子 Felipe，2005 离婚 |
| spouse | Guadalupe Álvarez | 无向 | 2006-02 再婚 |
| colleague | Veerabhadran Ramanathan | 无向 | 2017 合著《Well Under 2 Degrees Celsius》报告（教皇研讨会） |
| co-honored | Paul J. Crutzen | 无向 | 1995 诺贝尔化学奖共同得主（NOx-臭氧） |
| co-honored | F. Sherwood Rowland | 无向 | 1995 诺贝尔化学奖共同得主（与 1973-74 师徒/合作行并存） |

> metadata.json-only 的关系（如 Ester Molina 为姨母属家庭指引页面有载但按惯例以 household 记述不单独建亲属类型、Miramontes 仅合影、Durwood Zaelke 为报告共同作者第三人不重复建边）**不予入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1995，与 Crutzen、Rowland 共享）
- Tyler Prize for Environmental Achievement（1983）；Esselen Award, ACS 东北分会（1987）
- Newcomb Cleveland Prize, AAAS（1988）；NASA Exceptional Scientific Achievement Medal（1989）
- UNEP Global 500 Award（1989）；Pew Scholars Program 资助（1990，$150,000）
- 美国国家科学院院士（1993）；Institute of Medicine（1996）；Golden Plate Award（1996）
- Willard Gibbs Award（1998）；ACS 环境技术与科学创造性进展奖（1998）；UNEP Sasakawa Environment Prize（1999）
- Pontifical Academy of Sciences（2000）；Heinz Award in the Environment（2003）；Colegio Nacional（墨西哥，2003）
- Volvo Environment Prize（2004）；American Philosophical Society（2007）
- Presidential Medal of Freedom（2013，Obama 颁发）；Champions of the Earth 终身成就奖（2014）
- 荣誉学位 30 余个（Yale 1997、Harvard 2012、UNAM 1996、Cambridge 侧 British Columbia 2011 等）；Knight of the Legion of Honour；Grand Cross of the Order of Isabella the Catholic；Polanyi Medal；小行星 9680 Molina

## 9. 机构清单

- 教育：墨西哥城中小学；Institut auf dem Rosenberg（瑞士，11 岁起）；UNAM（BS 1965）；Albert Ludwig University of Freiburg（两年聚合动力学）；University of California, Berkeley（1968–1972，PhD）
- 任职：UNAM（回墨开创首个化学工程课程项目）；UC Irvine（1973 Rowland 组博士后 → 教职）；Jet Propulsion Laboratory / Caltech；MIT（地球大气行星科学系与化学系双聘）；UC San Diego 化学与生物化学系 + Scripps 海洋学研究所大气科学中心（2004-07-01 起）；Mario Molina Center for Energy and Environment 所长（2005 创办，墨西哥城）；Science Service/Society for Science & the Public 董事（2000–2005）；MacArthur Foundation 董事（2004–2014）

## 10. 终审清单

- [ ] 生卒 1943-03-19 / 2020-10-07，享年 77，出生地与去世地均为墨西哥城（心脏病发作）
- [ ] 1995 三人共享表述准确；citation 用页面原句；Cl· 链式反应两式方向无误
- [ ] Rowland 三重关系（博士后导师/合作者/共同得主）分行表述未混
- [ ] Farman 1985 发现与 Molina 跟进口径准确；蒙特利尔议定书 1987·56 国
- [ ] 「首位墨西哥出生的化学诺奖得主」注明按页面口径
- [ ] 引语全部可在本地 Wikipedia 原文找到；Miramontes 合照未建关系
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Mario_J._Molina/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像已就位或装饰圆占位（注明理由）
- [ ] **国籍**：封面顶部明示墨西哥
- [ ] **引语核对**：科学之问句、citation 原句、Obama 新闻稿句须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger、Kary_Mullis 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 的更新由主控统一收尾（本提示词不直接改动）。
> **最重要的事：每写一页就 make，看到溢出就修。**
