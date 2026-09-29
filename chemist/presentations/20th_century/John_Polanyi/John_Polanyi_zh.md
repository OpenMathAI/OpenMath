# John Polanyi（约翰·波拉尼）立传提示词

> qid=Q237825 · 1929-01-23 – 在世 · 匈牙利裔加拿大化学家 · 20 世纪 · 诺贝尔化学奖（1986，与 Dudley R. Herschbach、Yuan T. Lee 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/John_Polanyi/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`（表格语义化 tabularx + 公式展示框 + 时间线页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面头像**：page.md 正文与 images.txt **无真实人物肖像**（唯一图片为 John Polanyi Collegiate Institute 校舍照，禁用作肖像）——右上角用**装饰圆占位**（主色渐变 + 姓名/元素符号式题字）；可尝试 Wikipedia REST API `page/summary` 查 infobox 原图（页内"Polanyi in 2019"提示存在肖像），404 则维持装饰圆。若下载成功改用真实肖像 + 细边框。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{fire}\enspace 看见反应中的光\enspace·\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（born Berlin · 育于英国 · 长于加拿大的三段地域注记可作副行）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（或装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、出生地、国籍（加拿大）、教育（Manchester）、博士导师、父亲、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），母题呼应「化学发光 / 反应释放的红外光子」——暗底上稀疏的亮圆点如光谱中的发射线。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（新生产物的微弱红外发射 → 能量归布）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：John Charles Polanyi（匈牙利语 Polányi János Károly；中文惯称：约翰·波拉尼；头衔 PC CC FRSC OOnt FRS）
- **生卒**：1929-01-23 生于德国柏林（在世，卒日留白）
- **国籍**：Canada（加拿大）——匈牙利裔（Polányi/Pollacsek 家族），生于柏林，1933 随家迁英国，长于加拿大；page.md 按 György Marx 之说他属"The Martians"（20 世纪上半叶移居美国的匈牙利杰出科学家群体，此处按 page.md 转述为移民科学家群体语境）
- **家庭**：父 Michael（Mihály）Polanyi——化学家、科学哲学家、经济学家（其大学一年级时在化学系任教，后转任新设的社会研究讲席）；母 Magda Elizabeth Kemény Polanyi；伯父 Karl Polanyi——经济史家（《大转型》作者语境，page.md 作 economic historian）；祖父 Mihaly Pollacsek 铁路工程师（Magyarise 了家族姓但本人未改）；弟 George 以捍卫市场资本主义著称
- **教育轨迹**：
  - 11 岁时为避德军轰炸被父亲送往加拿大三年，就读 Toronto 的 University of Toronto Schools
  - 回英后完成中学，入 University of Manchester：1949 本科、1952 PhD
- **导师**：Ernest Warhurst（父亲的旧生；钠焰装置测钠原子与其他分子碰撞致反应的几率——Polanyi 的博士课题以热解测化学键强度承其衣钵）
- **研究领域**：化学——化学动力学、反应动力学、过渡态、红外化学发光

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **乱世童年（1929–1945）**：柏林出生、1933 因纳粹迫害犹太人举家迁英；战时 11 岁独赴加拿大三年避炸——曾短暂想当诗人。
2. **曼彻斯特（1949–1952）**：父任化学系教授的校园里完成本科与博士；师从 Warhurst 以热解测键强。
3. **加拿大国家研究委员会（1952–1954）**：渥太华 NRC 与 E. W. R. Steacie 共事；评估过渡态理论（TST）的预测力，结论是该理论因对过渡态作用力缺乏了解而有缺陷。
4. **Herzberg 实验室（NRC 末期）**：在 Gerhard Herzberg 组用光谱研究碘分子的振动/转动能级激发——光谱学的手艺在此练成。
5. **普林斯顿（1954–1956）**：与 Sir Hugh Taylor 共事，同 Michael Boudart、David Garvin 合作；受 H + O3 振动激发产物研究的影响。
6. **多伦多起步（1956）**：讲师入职，1957 助理教授、1960 副教授、1962 正教授——六级跳；1974 获 University Professor 荣衔（沿用至今，现为 University Professor Emeritus）。
7. **化学发光（1958）**：与研究生 Kenneth Cashion 首获化学发光发现——分子/原子激发态发出的光；1958 年首次发表。
8. **红外化学发光（诺奖核心）**：测量新生成分子发出的微弱红外辐射，以考察化学反应中的能量归布（energy disposal）——反应动力学的关键窗口。
9. **1986 诺贝尔化学奖**：与 Harvard 的 Dudley Herschbach、Berkeley 的 Yuan T. Lee 三人共享，"their contributions concerning the dynamics of chemical elementary processes"（page.md 口径）；Polanyi 的贡献集中在红外化学发光技术的发展；诺奖演讲题 "Some Concepts in Reaction Dynamics"。
10. **诺奖的另一面**：自述诺奖令其研究方案与论文署名招致额外审视，并使人们质疑其对科学的投入——"There is a very reasonable suspicion that you are so busy doing the things that Nobel Prize winners do that you are actually only giving half your mind to science."（page.md 明载可引）
11. **转向 STM（1986 后）**：在瑞典领奖时结识 1986 诺贝尔物理学奖得主（电子显微镜与扫描隧道显微术，Ruska/Binnig/Rohrer）——回多伦多后引入 STM，现实验室有四台（每台约 $750,000），从红外探测转向分子尺度直接成像；2009 年 Nature Chemistry "Cooperative molecular dynamics in surface reactions"，指向纳米技术。
12. **和平与公共政策**：1960 年创立加拿大 Pugwash 小组并任主席至 1978（Pugwash 全球运动 1995 获诺贝尔和平奖）；核武危害文集《The Dangers of Nuclear War》共同编者；常在《The Globe and Mail》评论公共政策；2022 获 Andrei Sakharov Prize（表彰七十年废除核武、人权与言论自由、科学公共教育的坚持）。
13. **以他命名**：安大略省政府设 John Charles Polanyi Prizes（每项 $20,000，按诺奖分类奖给青年研究者）；NSERC 设 John C. Polanyi Award（$250,000，首届授予 Sudbury 中微子天文台，2011 授 Victoria Kaspi）；2011 年 10 月 John Polanyi Collegiate Institute 以他命名开校；2011 年 Canada Post 化学国际年邮票；奖章陈列于 Massey College（他任 Senior Fellow）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深砖红 dark brick） | `#9E2B25` | 化学发光的暖色焰心（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（化学发光 badgeChemilum） | `#2E5A9E` | 蓝红外发射 / 能量归布 |
| 分类色 2（反应动力学 badgeDyn） | `#1B7A43` | 绿过渡态 / 反应机理 |
| 分类色 3（表面与 STM badgeSTM） | `#D97B29` | 琥珀扫描隧道 / 表面反应 |
| 分类色 4（和平与公共 badgePeace） | `#6B4E16` | 棕 Pugwash / Sakharov 奖 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 篇一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题「暗室中的发射光谱线」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（清单预置 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`；执行时按项目惯例软链至本目录，不复制 wav 文件）
- **风格**：怀旧 / 纪录片 / 温情
- **匹配理由**：
  - 怀旧感匹配横跨柏林—伦敦—多伦多的流离与成家（Polányi 家族的 20 世纪迁徙史）
  - 纪录片感匹配"化学发光"意象——黑暗中映出的微光，正是其科学的诗意写照
  - 温情匹配其近一个世纪的科学+和平双人生（1960 创 Pugwash 至 2022 Sakharov 奖的七十年坚持）
- **时长核对**：执行时确认音轨时长 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 看见反应中的光 / John Polanyi 1929– + 四色 badge + 右上（肖像或装饰圆）+ 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右 2×2 信息网格（生卒/出生地柏林/国籍/教育 Manchester/博士导师 Warhurst/父亲 Michael/领域/荣誉）
03  波拉尼之路 — 时间线（10 节点：1929→1933→1940→1949→1952→1954→1956→1958→1986→2022）
04  乱世童年与家族 (1929–1949) — 表格「时间|事件|结果」（柏林/迁英/避炸赴加/父亲与伯父）
05  曼彻斯特：键强与钠焰 (1949–1952) — 表格「问题|方法|结果」+ 公式框：热解测键强
06  NRC 与普林斯顿 (1952–1956) — 表格「人物|工作|收获」（Steacie/TST 评估/Herzberg 光谱/H+O3）
07  多伦多：化学发光 (1956–1958) — 表格「问题|方法|结果」（Cashion；1958 首次发表）
08  红外化学发光 — 表格「问题|方法|结果」+ 公式框：新生分子的微弱红外发射 → 能量归布
09  1986 诺奖 — 表格「三人|方法|贡献」（与 Herschbach、Lee 共享）+ 诺奖演讲题 "Some Concepts in Reaction Dynamics"
10  从红外到 STM (1986–2009) — 表格「契机|转向|成果」（瑞典遇 1986 物理奖得主/四台 STM/2009 Nature Chemistry）
11  和平与公共政策 — 双栏页：Pugwash（1960–1978）/ Sakharov Prize 2022 / 核武文集 / 时报评论
12  荣誉清单 — 「类别|代表|意义」表格（含 itemize：诺奖/Wolf 1982/Royal Medal 1989/Faraday 2010/Order of Canada）
13  以他命名 — 四分类遗产盒：安省 Polanyi Prizes / NSERC Polanyi Award / Polanyi Collegiate Institute / 邮票与 Massey College
14  结尾 — 「反应的私语，化作一缕可见的红外之光。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | page.md 三人共享理由 "their contributions concerning the dynamics of chemical elementary processes"；Polanyi 个人贡献 = **红外化学发光技术**（infrared chemiluminescence）——勿写成"分子束"（那是 Herschbach/Lee） |
| 三人共享方向 | Herschbach/Lee=交叉分子束、Polanyi=红外化学发光——两种方法勿混 |
| 肖像红线 | images.txt 仅校舍照（John Polanyi Collegiate Institute）——**禁用校舍照冒充肖像**；装饰圆占位或 REST API 回退 |
| 出生国 vs 国籍 | 生于**柏林（德国）**、匈牙利裔家族、1933 迁英、长居加拿大——时间线三段勿压缩成"匈牙利出生"；yaml 国籍按 frontmatter Canada/Hungary/Germany 多条带 rank |
| 父亲职位 | Michael Polanyi 在其**大学一年级**时任化学系教授、后**转任**新设社会研究讲席——"转系"勿写成"同时双聘" |
| 博士导师 | Ernest Warhurst（父亲的旧生）——勿误写其父为导师；Michael Polanyi 只入 parent-child 关系 |
| The Martians | 按 page.md 转述为 György Marx 的说法（移居美国的匈牙利科学家群体）——是他人归类说法，注明"据 György Marx"，勿当既定史实铺陈；且原文语境是美国，Polanyi 主要在加拿大——降为一笔带过或省略 |
| TST 评估 | 结论是过渡态理论"有缺陷"（因过渡态作用力知识不足）——勿写成"推翻了过渡态理论" |
| Pugwash | 创立的是**加拿大** Pugwash 小组（1960，任主席至 1978）；1995 和平奖授给 Pugwash 全球运动——勿写 Polanyi 个人获和平奖 |
| 引语 | 唯一明载引语是关于诺奖额外审视的一段（"There is a very reasonable suspicion..."）——可引；其余全篇不得编造引语 |
| 妻子 | 第一任 Anne Ferrar Davidson（1929–2013，1958 结婚）；现任肖像画家 Brenda Bury（page.md 明载 "currently married to"）——两段婚姻勿混 |
| 子女 | 女 Margaret（1961，记者）、子 Michael（1963，政治学者）——有载但仅名+职业，**不入社会关系库**（防噪声） |
| Wolf Prize | 1982 年获 Wolf 化学奖为 **shared（共享）**——勿写成独享；Steacie Prize 1965 亦 shared |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q237825 | ✅ |
| name_zh | 约翰·波拉尼 | ✅ |
| name_en | John Polanyi | ✅ |
| birth_date | 1929-01-23 | ✅ |
| death_date | （空——在世） | ✅ |
| nationality | Canada（rank 0）；Hungary（rank 1，族裔/家庭）；Germany（rank 2，出生地） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：chemical kinetics / reaction dynamics / infrared chemiluminescence / transition state，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Michael Polanyi | 父→子 | 父亲：化学家/科学哲学家/经济学家；其大学一年级时在曼彻斯特化学系任教（库内既有记录 id=1041 复用） |
| advisor-student | Ernest Warhurst | 师→生（博士导师） | 曼彻斯特博士导师（1952），父亲的旧生；热解测键强、钠焰装置 |
| advisor-student | Kenneth Cashion | 师→生（学生） | 研究生，1958 年共同发表化学发光首批发现 |
| colleague | Edgar William Richard Steacie | 无向 | NRC（1952–1954）共事；期间评估过渡态理论 |
| colleague | Gerhard Herzberg | 无向 | NRC 末在其实验室用光谱研究碘分子振动/转动激发 |
| co-honored | Dudley R. Herschbach | 无向 | 1986 诺贝尔化学奖共同得主（交叉分子束） |
| co-honored | Yuan T. Lee | 无向 | 1986 诺贝尔化学奖共同得主（交叉分子束） |
| spouse | Anne Davidson | 无向 | 第一任妻子 Anne Ferrar Davidson（1929–2013），1958 结婚 |
| spouse | Brenda Bury | 无向 | 现任妻子，肖像画家（page.md 明载 currently married） |

> **禁入库名单**：子女 Margaret（1961）与 Michael（1963）（仅名+职业，防噪声）；伯父 Karl Polanyi、表亲 Kari Polanyi Levitt / Eva Zeisel（白名单无叔伯/表亲类型）；NRC/普林斯顿同僚 Hugh Taylor、Michael Boudart、David Garvin（正文泛称 colleagues，语义过宽不入库）；György Marx（The Martians 说法提出者，非个人关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1986，与 Herschbach、Lee 共享）
- Wolf Prize in Chemistry（1982，shared）
- Royal Medal, Royal Society（1989）
- Faraday Lectureship Prize, Royal Society of Chemistry（2010）
- Henry Marshall Tory Medal, Royal Society of Canada（1977）
- Marlow Medal, Faraday Society（1962）；Centenary Medal, British Chemical Society（1965）
- Steacie Prize（1965，shared）；Noranda Award（1967）；Izaak Walton Killam Memorial Prize（1988）
- John C. Polanyi Lecture Award, Canadian Society for Chemistry（1992）
- Gerhard Herzberg Canada Gold Medal for Science and Engineering（2007）
- Andrei Sakharov Prize（2022）
- FRS（1971）；Order of Canada：Officer（1974）→ Companion（1979）；Queen's Privy Council for Canada（1992）；Order of Ontario
- 33 个荣誉学位（Waterloo 1970、Harvard 1982、Ottawa 1987、Queen's 1992 等，"over 30 institutions"）

## 9. 机构清单

- 教育：University of Toronto Schools（战时旅居多伦多）；The Manchester Grammar School；University of Manchester（BS 1949 / PhD 1952）
- 任职：National Research Council, Ottawa（1952–1954，Steacie/Herzberg）；Princeton University（1954–1956 research associate）；University of Toronto（1956 讲师 → 1962 教授 → 1974 University Professor → 现为 University Professor Emeritus）
- 公共职务：加拿大 Pugwash 小组创始主席（1960–1978）；Center for Arms Control and Non-Proliferation National Advisory Board；Campaign for a UN Parliamentary Assembly 支持者；Massey College Senior Fellow

## 10. 终审清单

- [ ] 生卒 1929-01-23 / 在世留白；出生地柏林、1933 迁英时间线准确
- [ ] 三人共享方向准确：Polanyi=红外化学发光；获奖理由按 page.md 口径
- [ ] 博士导师 Warhurst（非其父）；父亲仅 parent-child 关系
- [ ] Pugwash=加拿大小组创始主席；1995 和平奖属 Pugwash 运动
- [ ] Wolf/Steacie 两奖注明 shared
- [ ] 唯一引语（诺奖审视段）按原文；无编造引语
- [ ] 肖像处理合规（装饰圆或 REST API 真图，校舍照禁用）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/John_Polanyi/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆或 REST API 实图，校舍照零出现（★ 重点核查）
- [ ] 国籍：封面明示加拿大
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由 chem-batch-19 批次产出提示词与数据入库；立传与 Review 列由主控统一收尾。
