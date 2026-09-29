# Thomas Harriot（托马斯·哈里奥特）立传提示词

> qid=Q315402 · c. 1560 – 1621-07-02 · 英格兰数学家/天文学家 · 16 世纪（核心贡献跨 16–17 世纪）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Thomas_Harriot/`（@page.md + metadata.json + images.txt，事实基准以 page.md 为准）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 `images/harriot_portrait.jpg` + `draw=coveraccent!50` 细边框 + 姓名小字注。★ PORTRAITS.md 第 13 条核定：使用该像，图注**必须**写「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏）」，并注明**来历不明**（page.md 原文："Portrait often claimed to be Thomas Harriot (1602) ... The provenance of this portrait is not known, and there is little evidence to link it to Harriot."）；严禁当作确证肖像。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英格兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧肖像 `harriot_portrait.jpg`（图注同封面「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏），来历不明」）+ 右侧信息网格，至少含：生卒、本名、国籍、出生地、资助人、教育、核心领域。事实取自 Wikipedia infobox，不得杜撰；家庭与导师 page.md 无载 → 相应格写「—（无载）」，禁填人名。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应「月面图 / 手稿」的观测母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Thomas Harriot（又拼 Harriott / Hariot / Heriot；中文惯称：托马斯·哈里奥特）
- **生卒**：c. 1560 生于牛津（英格兰）→ 1621-07-02 逝于伦敦 Threadneedle Street 友人 Thomas Buckner 家中，享年 60–61
- **国籍**：英格兰（Kingdom of England，英格兰王国）
- **身份**：天文学家、数学家、民族志学者、翻译家、探险家、制图师；折射理论的归属者
- **家庭**：page.md 未记载父母与婚姻——家庭信息**全部留白，勿杜撰**
- **教育轨迹**：
  - 入牛津 St Mary Hall（1577 年注册簿有其名）
  - 牛津大学毕业后（1580 年）即投身航海研究，用星盘、六分仪等仪器研习跨大西洋航行技术，并为罗利麾下船长授课；其成果记于《Articon》，**后世遗失**
- **导师**：无载（page.md 未记载任何导师）
- **研究领域**：天文学、数学（代数）、民族志、光学、航海
- **资助人**：Sir Walter Raleigh（1580 年起聘其为数学教师/设计师/账房）、Henry Percy 第 9 世诺森伯兰伯爵（1595 年起，Syon House 长期赞助）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **早于伽利略的望月者**：1609-08-05（儒略历 07-26）用荷兰产望远镜绘下**第一幅有记录的望远镜天体观测图（月球地图）**，早于伽利略 1609-11-30 的观测近四个月；至 1613 年已绘两幅全月面图，月面环形山相对位置数十年内无人超越。
2. **太阳黑子的最早望远镜观测者**：1610-12 起以望远镜直接观日（危险方式），留下 199 幅黑子图、累计 690 次观测记录，揭示太阳自转，支持日心说——但**全部未发表**。
3. **不等号 < > 的首次广泛使用**：page.md 口径为 "he is credited with the first widespread use of the inequality signs '<' and '>'"——**勿写成「首创不等号」**；其符号随 1631 年身后出版的《Artis Analyticae Praxis》面世（生前未发表）；约 1600 年引入接近现代记法的代数符号体系，使「对未知数的运算如同对数字运算一样容易」，开创英国代数学派。
4. **罗阿诺克远征（1585–86）**：随 Raleigh 资助、Ralph Lane 率领的探险队赴罗阿诺克岛，是队中唯一懂卡罗莱纳阿尔冈昆语的英格兰人（师从 Manteo 与 Wanchese），为探险队关键成员。
5. **《弗吉尼亚新地真实简报》（1588）**：其**生前唯一出版著作**，含对北美原住民人口的早期记述，深刻影响后世英格兰探险者与殖民者。
6. **折射定律早于斯涅耳 20 年**：发现 Snell's law 早斯涅耳 20 年，未发表；与开普勒的光学通信影响了开普勒猜想。
7. **球堆积问题**：受 Raleigh 之托研究甲板炮弹最密堆叠，其理论与原子论惊人相似；1605 年后一度因此被指控信奉原子论。
8. **二进制算术的发明者**：早莱布尼茨数十年发明二进制记数与算术，**直至 1920 年代才为人所知**。
9. **身后出版的《Artis Analyticae Praxis》（1631）**：遗嘱执行人 Warner 整理出版，但编者理解不足，删去了负根与复根等内容；400 余页手稿迟至 2007/2009 年才有完整整理。
10. **无名天才**：生前几乎不发表、大量手稿散失，生前声名远逊其实际成就——「他宁愿要命也不要名」（Greenblatt 语，见 §5 引语红线）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（月岩灰蓝） | `#37474F` | 1609 年月面图 / Syon House 屋顶夜观 |
| 强调色（月色金） | `#E0A458` | 望远镜中的第一缕月光 |
| 分类色 1（代数记号 — 深紫） | `#5B2A86` | 不等号 < > / 符号代数 |
| 分类色 2（天文观测 — 深天蓝） | `#1B5E8C` | 月球绘图 / 太阳黑子 |
| 分类色 3（航海与罗阿诺克 — 青绿） | `#175E54` | 弗吉尼亚远征 / 阿尔冈昆语 |
| 分类色 4（未刊手稿 — 赭红） | `#A63A2B` | 400 余页手稿 / 身后出版 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「月面环形山 / 手稿墨迹」的观测与书写质感。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Lonesome**（AShamaluevMusic，`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`，悲伤 / 电影感 / 情感）
- **风格定调**：**孤独而深沉**（生前不发表、身后才被承认的天才）
- **匹配理由**：
  - 哈里奥特一生孤悬于赞助人门下、成果几乎全部锁进手稿箱，Lonesome 的**孤独钻研**标签与「无名天才」的叙事主线高度契合
  - 400 余页手稿迟至 20 世纪才重见天日的遗憾感，匹配悲伤 / 情感基调
  - 本组三人内不重复：Napier 用 Eternals、Briggs 用 Expedition
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（统一 14 页制：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与传承 + 终章）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格。
> 页结构（14 页，TEMPLATE_GUIDE §2 标准制）：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 个核心贡献页 + 荣誉 + 终章。原「赞助人与火药阴谋」并入荣誉页「晚年处境与身后纪念」。

1. **共享封面**（`\openmathslide`）：`\input{../../cover/openmath_page.tex}`，不改
2. **人物封面**（`\titleslide`）：大标题「早于伽利略的望月者 · 未发表的天才」+ 托马斯·哈里奥特 c.1560–1621 + 右上肖像 `harriot_portrait.jpg`（图注「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏），来历不明」）+ 国籍行「英格兰」+ 底部三要素状态栏 + 四分类 badge
3. **身份信息页**（`\profileslide`，★ 必做）：左肖像 `harriot_portrait.jpg`（同上「传为」图注）+ 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 资助人 / 教育 / 核心领域；家庭与导师写「—（无载）」）
4. **托马斯·哈里奥特的一生：时间线**（`\timelineslide`，竖轴 8 节点）：c.1560 牛津出生 → 1577 入 St Mary Hall → 1585–86 罗阿诺克远征 → 1588《真实简报》→ 1595 Northumberland 赞助 → 1609 首张望远镜月图 → 1610 黑子观测 → 1621-07-02 去世（1631《Praxis》身后出版）
5. **早年与牛津**（`\earlyslide`）：St Mary Hall（1577 注册）、1580 获学士学位、毕业即研习航海（星盘 / 六分仪）、为 Raleigh 麾下船长授课、《Articon》后世遗失
6. **罗阿诺克远征与《弗吉尼亚新地真实简报》（1588）**（贡献页，表格）：1585–86 远征（Raleigh 资助、Ralph Lane 率领）、生前唯一出版物、对原住民的早期记述
7. **阿尔冈昆语与语音字母**（贡献页，表格）：师从 Manteo / Wanchese、自创语音转写字母表、探险队的翻译支柱
8. **月球绘图（1609–1613）**（贡献页，表格 + 插图框）：1609-08-05（O.S. 07-26）首幅望远镜月图、早伽利略近四月、1613 两幅全月图
9. **太阳黑子（1610）**（贡献页，表格）：1610-12 起观测、199 幅图 / 690 次记录、太阳自转与加速、支持日心说、未发表
10. **折射定律与光学**（贡献页，表格 + 公式框）：早斯涅耳 20 年、与开普勒通信、开普勒猜想之渊源；Syon House 期间研究折射定律
11. **符号代数与不等号**（贡献页，表格 + 公式框）：< > 的首次广泛使用（经 1631 年身后《Praxis》面世）、接近现代的记法、英国代数学派
12. **球堆积、二进制与复利**（贡献页，表格 + 公式框）：炮弹密堆与原子论之嫌、二进制早莱布尼茨数十年（1920 年代才为人知）、约 1620 年连续复利手稿
13. **晚年处境与身后纪念**（荣誉页，表格）：Raleigh 先失势、Northumberland 1605 火药阴谋下狱、哈里奥特受审短暂入狱后获释、Syon House 学者圈（Warner / Hues / Lower）；Syon House 铭牌（2009 Telescope400）、月球环形山 Harriot（1970，背面）、系外行星 55 Cancri Af 命名 Harriot（2015）、威廉玛丽学院天文台
14. **终章**（`\closingslide`）：60–61 岁、左鼻孔癌（疑与吸烟相关）、「宁愿要命不要名」的无名天才

## 5. 史实陷阱与敏感点（终审必须检查）

- **生年口径**：仅知 c. 1560（metadata 的 1560-01-01 中「01-01」是噪声，立传写 **c. 1560**，享年 60–61）。
- **★ 肖像口径（Review-1 更正）**：PORTRAITS.md 第 13 条核定使用 `images/harriot_portrait.jpg`（Trinity College, Oxford 藏 1602 年像）；图注**必须**写「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏）」并注明**来历不明**（page.md 原文 "The provenance of this portrait is not known, and there is little evidence to link it to Harriot."）；严禁当作确证肖像。
- **月球观测口径**：哈里奥特 1609-08-05 绘月图**早于伽利略近四个月**，是「first recorded telescopic observation」；但伽利略 1610 年《星际信使》**先发表**且更精细（识别山脉与环形山）——两个口径都要写，勿贬伽利略；批评者 Terrie Bloom 的「抄袭伽利略」指控系他人观点，客观带过或略过。哈里奥特的观测 1784 年才部分发表、部分迟至 1965 年。
- **死因口径**：1614 年起由御医 Théodore de Mayerne 诊治「左鼻孔癌」，逐渐侵蚀鼻中隔，疑与唇部癌性溃疡相关；1621-07-02 卒，「apparently from skin cancer」；**烟草致癌说是 "It was suspected" 口径，勿写成定论**。
- **殖民语境引语**：原住民「视欧洲器物为神工」引语与 "brought to civility and the embracing of true religion" 引语均为 page.md 原文，**可用但必须保持 16 世纪历史语境、不评价**；其「原住民聪慧但技术落后、学习能力受后来者忽视」的记述应如实呈现。
- **「土豆引入英伦」**：page.md 口径是 "He is sometimes credited with..."——**存疑口径，勿写成事实**。
- **夜晚学派**：page.md 仅在 See also 列出 The School of Night 链接，正文无载——**禁写**。
- **火药阴谋**：Northumberland 因与谋反者 Thomas Percy 的亲属关系 1605 年下狱；哈里奥特本人受审并短暂入狱后获释——客观陈述，勿渲染。
- **无导师无学位细节**：St Mary Hall 注册 1577、1580 年毕业获学士学位（page.md "bachelor's degree"），勿拔高为更高学位。
- **改名拼写**：Harriott / Hariot / Heriot 均见于文献，立传统一用 Thomas Harriot；诗人 Muriel Rukeyser 偏用 Hariot（若提及需注明）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q315402 | 待写入 |
| name_zh | 托马斯·哈里奥特 | 待写入 |
| name_en | Thomas Harriot | 待写入 |
| birth_date | （c.）1560-01-01 | 待写入（生年月日为噪声，仅取 1560） |
| death_date | 1621-07-02 | 待写入 |
| nationality | England（Kingdom of England 带 era_note） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / algebra / astronomy / optics / ethnography | 待写入 |
| has_biography | false | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

> 仅收 page.md 明载关系。

- **资助人 / 雇主**：Walter Raleigh（collaborator，1580 年起聘为数学教师，资助罗阿诺克远征）、Henry Percy 第 9 世诺森伯兰伯爵（collaborator，1595 年起长期赞助，同住 Syon House）
- **合作 / 交往**：John White（collaborator，共同制作先进航海地图）、Johannes Kepler（collaborator，光学通信，影响开普勒猜想）、Walter Warner（collaborator，友人兼遗嘱执行人，整理出版《Praxis》）、Robert Hues（collaborator，诺森伯兰门下学者圈）、William Lower（collaborator，诺森伯兰门下学者圈）
- **语言师承**：Manteo（influence，教其卡罗莱纳阿尔冈昆语）、Wanchese（influence，教其卡罗莱纳阿尔冈昆语）
- **不入库**：Ralph Lane（远征队长，无直接协作记述）、Nathaniel Torporley（原定遗嘱执行人）、Théodore de Mayerne（医生）、Galileo（无直接交往）、Henry Stevens / John Shirley（后世传记作者）

## 8. 奖项清单

- page.md 无任何获奖记录——**不设奖项页、不入库**。

## 9. 机构清单

- 教育：St Mary Hall, Oxford（1577 年注册，1580 年毕业）；University of Oxford（education，同一时期）
- 任职：无机构任职——终身受雇于私人赞助人（Raleigh、Northumberland），机构不入库。

## 10. 终审清单

- [ ] 生年写 c. 1560（勿写 1560-01-01），卒 1621-07-02，享年 60–61
- [ ] 肖像用 `harriot_portrait.jpg`，图注必须写「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏）」并注明来历不明
- [ ] 月球观测「早四个月但后发表」双向口径准确
- [ ] 死因 skin cancer + 烟草说保持 "suspected" 存疑口径
- [ ] 殖民语境引语保持原文与历史语境、不评价
- [ ] 土豆引入为 "sometimes credited" 存疑口径；夜晚学派禁写
- [ ] 家庭信息全部留白，勿杜撰
- [ ] 引语必须 page.md 原文；page.md 无载禁写
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Thomas_Harriot/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **肖像**：使用 `harriot_portrait.jpg`；图注必须写「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏）」并注明来历不明（PORTRAITS.md 第 13 条）
- [ ] **国籍**：封面顶部徽章明示英格兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如器物引语、"civility" 句、Greenblatt 句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（纳皮尔 / 布里格斯）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

## 12. Review-1 事实终审记录（2026-09-29）

- 核对基准：`pages/Thomas_Harriot/page.md`（+ metadata.json）
- 生卒 / 享年：**c. 1560** 生于牛津（England）→ 1621-07-02 卒于伦敦 Threadneedle Street 友人 Thomas Buckner 家中，享年 60–61（page.md "aged 60–61"）；metadata date_of_birth 1560-01-01 中的「01-01」为噪声 → 立传只写 **c. 1560**；卒前三日立遗嘱（1876 年 Henry Stevens 发现）；死因：左鼻孔癌（1614 年起由御医 Théodore de Mayerne 诊治），page.md 口径 "apparently from skin cancer"，烟草致癌为 "It was suspected"
- 国籍口径：英格兰（Kingdom of England；metadata nationality: Kingdom of England）→ 封面国籍行「英格兰」，入库加 era_note historical
- 肖像结论：**有（★ 须加「传为」）** → `harriot_portrait.jpg`，图注**必须**写「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏）」并注明来历不明（PORTRAITS.md 第 13 条；page.md infobox 原文 "Portrait often claimed to be Thomas Harriot (1602) ... The provenance of this portrait is not known, and there is little evidence to link it to Harriot."）
- 引语核对：① 原住民视欧洲器物为神工之引语（page.md line 56 "Many things they sawe with us...as mathematical instruments, sea compasses...[and] spring clocks that seemed to goe of themselves..."）逐字 ✅；② "Whereby it may be hoped, if means of good government be used, that they may in short time be brought to civility and the embracing of true religion."（page.md line 60）逐字 ✅；③ Greenblatt 句 "... he preferred life to fame. And who can blame him?"（page.md line 116）逐字 ✅——三条均须保持 16 世纪历史语境、不评价
- 本轮修正：① §0/§0-3/§4/§5/§10/§11 共 6 处肖像条款由「或用装饰圆占位」改为**必须使用** `harriot_portrait.jpg` 并强制「传为…（1602 年像，Trinity College, Oxford 藏）」+ 来历不明限定语（依 PORTRAITS.md 第 13 条）；② §2-3 不等号口径由「首创者」改为 page.md 原文 "the first widespread use of the inequality signs '<' and '>'"（**禁写「首创不等号」**），并补「其符号随 1631 年身后《Artis Analyticae Praxis》面世」的发表时间；③ §4 重排为 14 页制：补入共享封面为第 1 页、人物封面为第 2 页，7 贡献页为 6–12，原「赞助人与火药阴谋」并入第 13 页荣誉页「晚年处境与身后纪念」（避免堆砌）；④ §4-4 时间线按 TEMPLATE_GUIDE 收敛为 **8 节点**（c.1560 → 1577 → 1585–86 → 1588 → 1595 → 1609 → 1610 → 1621），1607 Halley 彗星笔记移入正文页而非时间线；⑤ §0-3 明确家庭与导师「—（无载）」、禁填人名；⑥ §4-10 补「Syon House 期间研究折射定律」（page.md line 68）
- 遗留不确定项：① 出生月日无载（metadata 01-01 为噪声），享年按 60–61 写；② 「土豆引入英伦」为 "He is sometimes credited with..." 存疑口径，勿写成事实；③ The School of Night 仅见于 page.md See also，正文无载 → **禁写**；④ 1609 月图「早伽利略近四个月」与「伽利略先发表且更精细」两口径并存，须双向写、勿贬伽利略；Terrie Bloom 抄袭指控系他人观点，可略；⑤ 手稿散失严重（British Museum / Petworth House / Alnwick Castle），400 余页；《Praxis》完整英译 2007 年、《Magisteria magna》影印 2009 年；⑥ 1 幅 1610 晚月图存在「新月照亮范围与环形山位置失真」的技术批评（page.md 原文），如入正文须如实；⑦ 背景曲 Lonesome 与 Napier（Eternals）、Briggs（Expedition）不重复，未查同世纪其他篇目撞曲（按纪律仅记录不改）

## 13. 立传期记录（Beamer 立传，2026-09-29）

- 产出：`Thomas_Harriot_zh.tex` + `Makefile`，`make distclean && make` 通过。
- 编译：**0 error**；`Overfull` 仅 1 处 0.48pt，位于**不可修改的共享封面**（<10pt 可接受）；无 `Underfull`。PDF **14 页**。
- 肖像：`images/harriot_portrait.jpg`（图注「传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏），来历不明」）；另以 `harriot_moon_1609.jpg`（thumb.wikimedia.org 下载，已 `file` 验证为 JPEG）作月球绘图页插图。
- 不等号：仅写「首次广泛使用 $<$ 与 $>$」+ 1631 年身后《Praxis》面世，**未写「首创者」**；School of Night 未出现；生年写 **c. 1560**（未用 1560-01-01）。
- 时间线：按 §4-4 的 8 节点（c.1560 → 1577 → 1585–86 → 1588 → 1595 → 1609 → 1610 → 1621）。
- 事实核对：逐条对照 `pages/Thomas_Harriot/page.md`，**未发现提示词与 page.md 冲突**。
