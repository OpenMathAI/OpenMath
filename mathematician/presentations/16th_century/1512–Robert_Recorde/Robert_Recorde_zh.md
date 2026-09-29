# Robert Recorde（罗伯特·雷科德）立传提示词

> qid=Q318192 · c. 1510 – 1558-06 · 威尔士数学家 · 16 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Robert_Recorde/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（**Wikipedia 无本人真实肖像**——`images.txt` 仅含「史上第一条方程」书影 First_Equation_Ever.png 与等号原页书影 Recorde_-_The_Whetstone_of_Witte_-_equals.jpg，可作封面/正文插图但非肖像；无真实肖像则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 威尔士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆）+ 右侧信息网格，至少含：生卒、国籍、出生地 Tenby、教育（Oxford/Cambridge）、任职（皇家铸币局）、核心成就（等号 =）。事实取自 Wikipedia infobox 与正文，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题可用「一对平行线」呼应等号。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Robert Recorde（中文惯称：罗伯特·雷科德）
- **生卒**：约 1510（c. 1510）生于 Tenby（彭布罗克郡，威尔士）→ 1558 年 6 月（1558-07，即 1558 年 6 月中旬前后）卒于伦敦萨瑟克 King's Bench Prison（王座监狱），享年 47 或 48
- **国籍**：威尔士（Welsh；metadata 口径 Wales / United Kingdom 为现代对应）
- **身份**：数学家、医师；「等号 =」的发明者
- **家庭**：父 Thomas Recorde、母 Rose Recorde，家行次子（第二子亦为最后一子）；配偶与子女 page.md 无载，**禁写**
- **教育轨迹**：
  - 约 1525 年入牛津大学（University of Oxford）
  - 1531 年当选牛津万灵学院（All Souls College）Fellow
  - 改行从医后赴剑桥大学，1545 年获医学博士（M.D.）
  - 后返牛津公开讲授数学（赴剑桥前亦曾讲学）
- **任职轨迹**：
  - 伦敦行医，先后任国王爱德华六世（Edward VI）与女王玛丽一世（Mary I）的御医，部分著作题献给他们
  - 皇家铸币局（Royal Mint）controller（监理）
  - 爱尔兰矿区与铸币总监（Comptroller of Mines and Monies in Ireland）
- **导师**：page.md 无载，**禁写**
- **研究领域**：数学（算术、代数、几何）、医学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **等号 = 的发明者**：1557 年在 *The Whetstone of Witte* 中首次（印刷）引入两条等长平行线「=」，理由是「避免枯燥地重复 is equalle to 这两个词」——noe .2. thynges, can be moare equalle（再没有两样东西比这更相等了）。
2. **史上第一条印刷方程**：同书载有今记法 14x + 15 = 71 的方程（解 x = 4）——数学符号史的名场面。
3. **+ 与 − 进入英语世界**：1557 年将已有的加号、减号引入英语使用者群体。
4. **英国代数之父**：*The Grounde of Artes*（1543）是**第一本英语代数书**；*The Whetstone of Witte* 使他被誉为「以系统记号把代数引入不列颠群岛」的人。
5. **对话体教科书革新者**：多数著作以师徒对话（catechism 问答体）写成，面向工匠与自学者——数学教育通俗化的先驱。
6. **著作版图**：*The Grounde of Artes*（1543，算术/代数）、*The Pathway to Knowledge*（1551，几何）、*The Castle of Knowledge*（1556，托勒密天文学、顺带提及哥白尼日心模型）、*The Whetstone of Witte*（1557，代数第二卷/开方/方程法则/根数）、医学著作 *The Urinal of Physick*（1548，多次重印）。
7. **Zenzizenzizenzic**：为数的八次幂创造的著名词汇——英语数学词汇史趣典。
8. **学者与官僚的双面人生**：牛津 Fellow → 御医 → 铸币局监理 → 爱尔兰矿区铸币总监——横跨学界、宫廷与财政系统。
9. **悲剧结局**：被政敌以诽谤罪起诉后，因债务被捕，1558 年 6 月中旬前卒于王座监狱——等号的发明者死于负债监狱，是科学史上最令人唏嘘的结局之一。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用色 | 色值 | 说明 |
|---|---|---|
| 主色（都铎深绿） | `#175E54` | 都铎时代 / 威尔士 |
| 强调色（铸币黄铜） | `#C9A227` | 皇家铸币局 / 符号的金色时刻 |
| 分类色 1（代数 — 靛蓝） | `#3D5A80` | Grounde of Artes / Whetstone |
| 分类色 2（符号史 — 正红） | `#A63A2B` | = 与 +/- 的诞生 |
| 分类色 3（几何天文 — 青绿） | `#0E7C7B` | Pathway / Castle of Knowledge |
| 分类色 4（教育与人生 — 玫红） | `#8E5572` | 对话体教科书 / 悲剧结局 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）；可加「一对平行线」细线元素呼应等号。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Awaken**（alex-productions，`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`）
- **风格定调**：**明亮 / 鼓舞 / 启蒙感**
- **匹配理由**：
  - 雷科德的叙事主轴是「符号的发明」——等号、加号、减号把代数交到英语世界手里，是数学**启蒙**叙事；Awaken 的"鼓舞 / 明亮 / 年轻数学家"定位（curated_tracks.md 场景标注「开场、突破性证明」）匹配「= 诞生」的高光时刻
  - 全篇以符号革命的明亮感定调，结尾王座监狱的悲剧一页以曲目回落段承载，避免全程阴郁
  - 本组三人 BGM 互不重复：Nunes=Expedition、Commandino=PAST、Recorde=Awaken
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐 17 世纪黄金参照模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「等号的发明者 · 英国代数之父」+ Robert Recorde c.1510–1558 + 右上装饰圆/等号书影 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右信息网格（生卒 / 国籍 / 出生地 Tenby / 教育 Oxford–Cambridge / 任职 皇家铸币局 / 核心成就 等号 =）
3. **罗伯特·雷科德的一生：时间线**（`\timelineslide`）：c.1510 Tenby 出生 → c.1525 入牛津 → 1531 万灵学院 Fellow → 1545 剑桥医学博士 → 返牛津讲学 → 伦敦御医（Edward VI / Mary I）→ 皇家铸币局监理 → 1557 The Whetstone of Witte 引入等号 → 1558-06 卒于王座监狱
4. **早年与教育**（`\earlyslide`）：Tenby、双亲、牛津 1525、万灵学院 1531、剑桥 M.D. 1545
5. **等号的诞生**（核心贡献页，表格 + 公式框）：1557 Whetstone 原页书影 + 原文引语 + 「一对等长平行线」
6. **史上第一条方程**（核心贡献页，表格 + 公式框）：14x + 15 = 71（今记法）、解 x = 4
7. **+ 与 − 进入英语**（核心贡献页，表格）：1557 引入加号减号；符号史脉络（前人已有，雷科德传入英语世界）
8. **The Grounde of Artes**（核心贡献页，表格）：1543 第一本英语代数书；对话体写法
9. **著作版图**（核心贡献页，表格）：1543/1548/1551/1556/1557 五部著作年表 + 各书主题
10. **The Castle of Knowledge**（核心贡献页，表格）：托勒密天文学为主、顺带提及哥白尼模型——严谨表述
11. **Zenzizenzizenzic 与数学英语**（表格）：八次幂词汇等英语数学词汇创造；对话体（catechism）教育革新
12. **御医与铸币监理**（表格）：Edward VI / Mary I 御医、皇家铸币局 controller、爱尔兰 Mines and Monies 总监
13. **悲剧结局**（表格）：政敌诽谤诉讼 → 因债务被捕 → 1558-06 卒于王座监狱（Southwark）
14. **终章**：47 或 48 岁辞世；「一个 = 号，四百六十年未改」的遗产与纪念（Tenby 圣玛丽教堂、威尔士纪念）

## 5. 史实陷阱与敏感点（终审必须检查）

- **生年裁定**：metadata.json 的 date_of_birth 有 `1512 / 1510` 两个值；page.md 正文与 infobox 均 **c. 1510**（但脚注 4 ODNB 条目题名作 "c. 1512–1558"）——**以 page.md 为准取 c. 1510**，行文必须带「约」；§5 记录 1512 为 ODNB 口径并存说。
- **卒日口径**：page.md infobox 作 "June 1558 (1558-07)"、正文 "by the middle of June 1558"——**写到「1558 年 6 月中旬前」即可，禁写具体日**；metadata 的 `1558-01-01` 是占位噪声，禁用。享年 47 或 48（生年约数所致），两说并存勿取整。
- **等号首次发表于 The Whetstone of Witte（1557）**：表述为「在印刷书籍中首次引入等号」；page.md 原文措辞是 "introduced within a printed edition"——**勿写「发明了相等概念」「全世界第一个等号手写痕迹」**；引语必须用脚注 9 的原文（"a paire of paralleles, or Gemowe lines of one lengthe ... bicause noe .2. thynges, can be moare equalle"）并附今译。
- **+ / − 的准确口径**：雷科德是「引入英语世界」（introduced the pre-existing + and − signs to English speakers）——**加号减号并非他发明**，禁写「发明了加减号」。
- **死因表述**：page.md 实载链是「被政敌以诽谤罪起诉（sued for defamation by a political enemy）→ 因债务被捕（arrested for debt）→ 卒于王座监狱」——**政敌姓名 page.md 无载（未出现 William Herbert）**，禁写任何人名；表述为「因负债瘐死狱中」时保留因果链完整：先有诽谤诉讼、后有负债收监。
- **御医关系**：Edward VI 与 Mary I 是其病人/题献对象——**非师承非合作，不入库关系**；正文叙述即可。
- **家庭**：仅父 Thomas、母 Rose、家行次子为明载；配偶子女无载禁写；勿建同名自环父子（父与子同名时注意 person 匹配，此处父名 Thomas 不同名，无自环风险）。
- **Castle of Knowledge 与哥白尼**：page.md 措辞是 "explaining Ptolemaic astronomy while mentioning the Copernican heliocentric model in passing"——**是「顺带提及」而非「支持/传播日心说」**，禁拔高。
- **作者存疑著作**：*Cosmographiae isagoge*、*De Arte faciendi Horologium*、*De Usu Globorum et de Statu temporum* 三部为「作者不明、被归于他」——如提及必须注明存疑，勿计入确定著作年表。
- **引语红线**：可用引语仅脚注 9 的 Whetstone 原文一段（唯一载明出处的原文）；其余一律转述。
- **国籍**：metadata Wales / United Kingdom——封面用「威尔士」；16 世纪威尔士属都铎王朝治下，United Kingdom 为现代口径，入库时可以 Wales 为主。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q318192 | 待写入 |
| name_zh | 罗伯特·雷科德 | 待写入 |
| name_en | Robert Recorde | 待写入 |
| birth_date | 1510 | 待写入（约数，仅年份） |
| death_date | 1558-06 | 待写入（仅到月，page.md 口径） |
| nationality | Wales / United Kingdom | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / algebra / arithmetic / geometry / astronomy | 待写入 |
| has_biography | false | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

- **父母**：Thomas Recorde（父）、Rose Recorde（母）——parent-child
- **不入库**：Edward VI 与 Mary I（御医-君主关系，无对应类型且非学术关系）、政敌（page.md 未载姓名）、Woodall 等后世纪念者（page.md 无载）
- page.md 未载任何导师、学生、合作者、论战对象——**禁编造学术关系**。

## 8. 奖项清单

- page.md 无载任何奖项；**本页留空，禁编造**。万灵学院 Fellow（1531）属教育/任职，不列为奖项。

## 9. 机构清单

- 教育：University of Oxford（牛津大学，约 1525 入学，公开讲授数学）；University of Cambridge（剑桥大学，1545 医学博士）
- 任职：All Souls College, Oxford（万灵学院 Fellow，1531）；Royal Mint（皇家铸币局，controller 监理；爱尔兰 Comptroller of Mines and Monies 无独立机构名，归入皇家铸币局叙述）
- 起止年份 page.md 多数未载（除 1531/1545 外），**无载不写年份**。

## 10. 终审清单

- [ ] 生卒 c. 1510 / 1558-06，享年 47 或 48 两说并存，出生地 Tenby、卒地 King's Bench Prison（Southwark）
- [ ] 等号「1557 年 The Whetstone of Witte 印刷引入」表述准确
- [ ] 加减号「引入英语世界」非「发明」
- [ ] 死因因果链完整：诽谤诉讼 → 负债收监 → 卒于狱中；政敌无名禁写
- [ ] Castle of Knowledge 对哥白尼是「顺带提及」
- [ ] 引语仅 Whetstone 原文一段，附今译与出处
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Robert_Recorde/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无真实肖像，用装饰圆占位；等号书影仅作插图
- [ ] **国籍**：封面顶部徽章明示威尔士
- [ ] **引语核对**：引语必须在 Wikipedia 原文（脚注 9）找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 16 世纪组其他数学家（Nunes / Commandino）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
