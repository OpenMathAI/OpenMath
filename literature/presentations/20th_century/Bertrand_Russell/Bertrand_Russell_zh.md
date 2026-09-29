# 文学家立传提示词（OpenLiterature：Bertrand Russell）

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，与数学/物理/化学侧同构）。
- **本实例**：Bertrand Arthur William Russell, 3rd Earl Russell（伯特兰·罗素），1950 年诺贝尔文学奖得主——以哲学家/逻辑学家身份获文学奖的特例，人道主义理想与思想自由的旗手。
- **设计哲学**：文学家立传以「身份信息页 + 研究领域表」为骨架（与物理学家模板同构），但以**代表作书影 / 名句引文框 / 意象图式**替代公式框——罗素的视觉母题是「思想自由的三重奏」：《西方哲学史》的千年思想长卷、《婚姻与道德》的风波、罗素—爱因斯坦宣言的签名页。
- **★ 特别注意（跨库复用记录）**：罗素几乎必然已存在于 greatminds 库（数学/哲学侧已建）。本篇执行前必须先查 `SELECT id,name_en,has_biography FROM people WHERE qid='Q33760'`；本次查明为 **id=74，name_en='Bertrand Russell'，has_biography=1，primary_occupation='mathematician'，数学逻辑侧已有 4 fields + 15 relations**。yaml 一律复用该记录：name_en 沿用库内形式、has_biography 保持 1、primary_occupation 沿用 mathematician（勿改 writer）；fields 只补文学侧增量（存量 4 条按原 rank 原样列出防 rank 被覆盖）、relations 撞唯一键幂等跳过。

## 二、背景信息 【人物专属】

- **目标文学家**：Bertrand Russell（1872-05-18 ~ 1970-02-02，享年 97 岁）
- **姓名**：Bertrand Arthur William Russell, 3rd Earl Russell ／ 伯特兰·罗素
- **诺奖年份**：1950 年诺贝尔文学奖，官方获奖理由（禁止改写）：
  > "in recognition of his varied and significant writings in which he champions humanitarian ideals and freedom of thought"（表彰其多样而重要的著述，在其中他捍卫人道主义理想与思想自由）
  > 注：1950-12 斯德哥尔摩晚宴上与 1949 年度奖得主 Faulkner 同席受奖（两人奖项独立，非共享）。
- **气质关键词**：思想自由的捍卫者、分析哲学的奠基人、九十七年岁的良心
- **设计母题**：**「思想自由的长卷」**——《西方哲学史》（1945，畅销终身的收入来源）的哲学谱系图、罗素悖论集合圈的自指图形、罗素—爱因斯坦宣言（1955）的签名页；辅以彭布罗克庄园（Pembroke Lodge）童年与威尔士 Plas Penrhyn 晚年居所。
- **本地数据源**：`literature/presentations/pages/20th_century/Bertrand_Russell/page.md`（+ metadata.json、images.txt）
- **Wikipedia**：https://en.wikipedia.org/wiki/Bertrand_Russell （肖像第 0 步下载：infobox 用 1936 年照；备选 1954 年照 File:Bertrand_Russell_1954.jpg、1893 剑桥照）

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇歧义先征求意见。含「研究领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库（MySQL）。

### 第 0 步：事实基准（已核对，以正文为准）

- **生卒**：1872-05-18 生于蒙茅斯郡特雷莱克（Trellech）Ravenscroft 乡宅 ～ 1970-02-02 晚八点后逝于威尔士彭里恩德拉伊斯（Penrhyndeudraeth）家中（流感），享年 97 岁；2-05 于科尔温湾火化（仅五人在场，无宗教仪式、静默一分钟），骨灰后撒威尔士群山。
- **国籍**：英国（出生于威尔士的蒙茅斯郡、自认 English——口径按 page.md 并写）。
- **家庭**：英国贵族自由派名门；祖父 John Russell, 1st Earl Russell 曾两度出任英国首相；父 John Russell, Viscount Amberley 与母 Katharine 均为节育主张的早期倡导者；父请哲学家 John Stuart Mill 为其**世俗教父**（Mill 于罗素出生次年去世，著述影响其一生）。4 岁成孤儿（1874 母与姐 Rachel 死于白喉，1876 父死于支气管炎），由祖母 Countess Russell 抚养于里士满公园 Pembroke Lodge——祖母对社会正义与坚守原则的影响伴随其终身。1931 年兄长 Frank 去世后袭封第三代罗素伯爵，上议院议员（1931–1970）。
- **教育**：1890 奖学金入剑桥三一学院读数学 Tripos（教练 Robert Rumsey Webb），1893 数学一等第七 Wrangler 毕业；1895 哲学 Fellowship；与 Moore 相识、受 Whitehead 影响（引其入剑桥使徒社）。11 岁时兄长 Frank 引其读欧几里得——自述「一生大事之一，如初恋般目眩」；15 岁起怀疑基督教义→无自由意志→无来世，18 岁读 Mill《自传》后放弃「第一因」论证成为无神论者。
- **文学/思想师承与影响（仅收 page.md 明载）**：少年时代沉浸雪莱（「把所有闲暇用于读他、背他」）；Euclid 之启蒙；Mill 著述之影响；1900 巴黎首届国际哲学大会遇 Peano（掌握其符号系统，归英后读其文献时发现罗素悖论）；剑桥同窗 G. E. Moore 友谊使其转向分析哲学（二人领导的英国「反观念论」起义）。
- **任职**：剑桥三一学院讲师（1910；1916 因反战被开除，1919 复职，1920 辞职，1944–1949 重返）；LSE（1896、1937 讲权力学）；1920–1921 访华讲学一年（在京罹肺炎、日媒误发讣告）；美国岁月：芝加哥大学、UCLA、纽约城市学院（CCNY，1940 年因《婚姻与道德》观点被法院判「道德上不适合任教」而取消聘任——Dewey 领衔抗议、Einstein 发公开信声援）、Barnes Foundation（西方哲学史讲稿之源）；1949 获功绩勋章（George VI 打趣「你有时表现得不值得效仿」）；BBC 利思讲座首讲人（1948《权威与个人》）；1957 Kalinga 科普奖、1963 耶路撒冷奖。
- **关键荣誉**：De Morgan Medal（1932）、Sylvester Medal（1934）、FRS（1908）、OM（1949）、1950 诺贝尔文学奖、Kalinga Prize（1957）、Jerusalem Prize（1963）、Sonning Prize。
- **核心著作与贡献（4–6 条）**：
  1. 《数学原理》（Principia Mathematica，与 Whitehead 合著，1910–1913 三卷，逻辑主义里程碑）
  2. 《数学原则》（The Principles of Mathematics，1903，提出逻辑主义论题与罗素悖论初解）
  3. 论文〈论指称〉（On Denoting，1905，被誉为「哲学的范式」）
  4. 《婚姻与道德》（1929——CCNY 风波源头，亦是其获文学奖的争议性著作之一）
  5. 《西方哲学史》（1945，畅销终身、奠定其公共作家身份）
  6. 《罗素—爱因斯坦宣言》（1955，核裁军呼吁，Pugwash 运动之源）
- **关键时间线（15–20 节点）**：1872 生于 Trellech → 1874–1876 母/姐/父相继去世 → 祖母抚养于 Pembroke Lodge → 11 岁读欧几里得 → 1890 入剑桥三一学院 → 1893 数学一等毕业 → 1895 Fellowship → 1894 与 Alys Pearsall Smith 成婚 → 1896《德国社会民主主义》/LSE 授课 → 1897《几何基础论文》→ 1900 巴黎遇 Peano → 1903《数学原则》→ 1905〈论指称〉→ 1908 FRS → 1910–1913《数学原理》三卷；1910 剑桥讲师、Wittgenstein 来投 → 1914 一战转向和平主义 → 1916 被三一学院开除/罚款百镑 → 1918 布里斯托监狱六月（狱中写《数学哲学导论》）→ 1919 复职 → 1920 访苏（会列宁一小时，幻灭）/访华讲学 → 1921 与 Alys 离婚、与 Dora Black 成婚 → 1927 与 Dora 共创 Beacon Hill 实验学校 → 1929《婚姻与道德》→ 1931 袭爵 → 1936 与 Patricia Spence 成婚（子 Conrad）→ 1938–1944 美国讲学（CCNY 风波 1940）→ 1944 重返三一 → 1945《西方哲学史》→ 1948 机场空难幸存（Bukken Bruse，24/43 生还）/BBC 利思讲座 → 1949 OM → 1950 诺贝尔文学奖 → 1952 与 Edith Finch 成婚（终老良伴）→ 1955 罗素—爱因斯坦宣言 → 1957 Kalinga 奖 → 1962 古巴导弹危机通电肯尼迪与赫鲁晓夫 → 1964 组「谁杀了肯尼迪委员会」 → 1967–1969 三卷自传 → 1970-01-31 最后政治声明（斥以色列扩张）→ 1970-02-02 逝于 Penrhyndeudraeth。
- **文学侧定位**：获奖理由强调「多样而重要的著述」——散文、时评、通俗读物（向大众阐释物理/伦理/教育）、自传三卷（1967–1969）与《西方哲学史》共同构成其文学身位；战时 BBC 广播与报刊专栏使其成为 20 世纪「公共知识分子」原型。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `literature/presentations/20th_century/Bertrand_Russell/`（+ `images/`），Makefile 设 `MAIN=Bertrand_Russell_zh`；肖像下载（curl `-A "Mozilla/5.0"`，file 验证；失败用 Commons Special:FilePath 回退）。

### 第 4 步：研究领域梳理 + 入库 【人物专属，注意跨库增量】

> 库内存量 fields（person_id=74，勿改 rank）：mathematical logic(0)、set theory(1)、logic(2)、philosophy of language(3)。本篇只**补文学侧增量**（存量 4 条在 yaml 中按原 rank 原样列出，防止 seed 的 ON DUPLICATE KEY UPDATE 覆盖 rank）。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0–3 | （库内存量）mathematical logic / set theory / logic / philosophy of language | 数理逻辑 / 集合论 / 逻辑 / 语言哲学 | 数学逻辑侧既有四条，原样保留 | — |
| 4 | analytic philosophy | 分析哲学 | 与 Moore 共同奠基的哲学流派（补） | 哲学页 |
| 5 | social criticism | 社会批评 | 和平主义/教育/婚姻伦理的公共写作（补） | 时评页 |
| 6 | essay | 随笔 | 获奖理由所指「多样著述」的文体（补） | 文学页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

> 库内存量 15 条（数学侧：Moore/Frege/Wittgenstein/Copi/Demos/Pitts/Whitehead/McTaggart/Ward/Hardy/Mill/Powell/Yukawa/Bridgman）一律不重复写；本篇只补文学侧明载关系。注：库内 Mill 行为遗留 co-honored 类型（note 世俗教父），本 yaml 不再新增 Mill 行，避免同对多人重复。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Alys Pearsall Smith | 无向 | 1894 成婚，1921 离异 |
| spouse | Dora Black | 无向 | 1921 成婚，1935 离异，共创 Beacon Hill 学校 |
| spouse | Patricia Spence | 无向 | 1936 成婚（其子女家庭教师），1952 离异 |
| spouse | Edith Finch | 无向 | 1952 成婚，幸福终老至 1970 |
| parent-child | John Russell, 4th Earl Russell | 罗素→子 | 长子，曾患精神疾病（与 Dora 争执之源） |
| parent-child | Katharine Tait | 罗素→女 | 女（Lady Katharine Tait） |
| parent-child | Conrad Russell, 5th Earl Russell | 罗素→子 | 幼子，历史学家、自由民主党要角 |
| colleague | Giuseppe Peano | 无向 | 1900 巴黎哲学大会相识，掌握其符号系统后发现罗素悖论 |
| colleague | John Dewey | 无向 | CCNY 事件中领衔抗议的哲学家，1920–21 同在中国讲学 |
| colleague | Albert Einstein | 无向 | 1940 公开信声援其 CCNY 任职；1955 罗素—爱因斯坦宣言共同发起人 |
| colleague | V. K. Krishna Menon | 无向 | 印度联盟友人合作者，罗素 1932–1939 任主席 |
| colleague | T. S. Eliot | 无向 | 1915 年新婚的艾略特夫妇曾借住其公寓 |
| influence | Percy Bysshe Shelley | 影响→罗素 | 少年时代沉浸背诵的诗人 |
| influence | Euclid | 影响→罗素 | 11 岁读《几何原本》自述为「一生大事之一」 |
| influence | Willard Van Orman Quine | 罗素→影响 | 自述罗素著作对其影响最大 |

#### 4.5.1 入库操作

- `MySQL/data/Bertrand_Russell.yaml`（增量）+ `cd MySQL && python3 seed_person.py data/Bertrand_Russell.yaml`（幂等，UPD #74）；校验 fields≥7（4 存量+3 增量）、relations≥17（15 存量+增量）。

### 第 5 步：设计配色 【人物专属】

- **主色**：剑桥深青 `#0F4C5C`（预分配，勿改）；诺奖香槟金 `C9A227`。
- badgeA–D：badgeA 分析哲学/逻辑 — 靛蓝 `#4C5FD5`；badgeB 思想自由/宣言 — 青绿 `#0E7C7B`；badgeC 婚姻与道德风波 — 琥珀 `#E07B30`；badgeD 随笔与广播 — 玫瑰 `#C4204F`。
- 背景母题：集合圈自指线稿（罗素悖论）+ 签名页意象（宣言）。

### 第 6 步：规划幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 思想自由的旗手 / Bertrand Russell 1872–1970 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、伯爵封号、孤儿童年、四段婚姻、剑桥/CCNY、荣誉、核心领域）
03  核心著作概览 — 六大节点书影（数学原则→数学原理→论指称→婚姻与道德→西方哲学史→自传）
04  贵族孤儿与祖母 (1872–1890) — Pembroke Lodge、欧几里得、雪莱、失信仰之路
05  剑桥岁月 (1890–1910) — Tripos、Moore 与反观念论、Peano 与悖论
06  《数学原理》与逻辑主义 (1903–1913) — 与 Whitehead 合著、〈论指称〉、FRS
07  Wittgenstein 来投 (1910–1914) — 视其为衣钵传人、助其出版《逻辑哲学论》
08  一战与和平主义 (1914–1918) — 被开除、罚款、布里斯托监狱、狱中著述引文框
09  访苏与访华 (1920–1921) — 会列宁之幻灭、北京讲学、日本误发讣告
10  Beacon Hill 与《婚姻与道德》(1927–1935) — 实验教育、CCNY「道德不适合任教」风波（Dewey/Einstein 声援）
11  《西方哲学史》(1944–1945) — Barnes 讲稿、畅销终身
12  诺贝尔文学奖 (1950) — 官方理由引文框、与 Faulkner 同席、OM 上的君臣打趣
13  罗素—爱因斯坦宣言 (1955) — 核裁军、Pugwash 运动之源
14  晚年 (1962–1970) — 古巴导弹危机通电、三卷自传、最后声明、Plas Penrhyn
15  遗产：从分析哲学到公共良心 — Quine/维也纳学派一脉、九十七年的一生、结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用，人物专属内容】

- 版式：`p{}` 窄列用 `\newcolumntype{P}[1]`；哲学引文用小号斜体；frame 标题过长缩短即可；文学页用书影/引文框替代公式框（集合圈图示除外——可用简易 tikz 线稿作意象图式）。
- 陷阱：

| 陷阱 | 说明 |
|------|------|
| 跨库复用 | 库内 id=74 已有数学侧记录——name_en/primary_occupation/has_biography 保持现值；本篇只做 fields/relations 增量，勿重置主记录 |
| 奖项口径 | 1950 年度奖（1950-12 颁发）；与 1949 年度奖得主 Faulkner 同席但**非共享**——勿写「共享诺奖」 |
| 获奖理由 | 官方原文 "in recognition of his varied and significant writings…"；勿改写为「因哲学著作获奖」的泛称 |
| Mill 行遗留 | 库内 John Stuart Mill 为遗留 co-honored 类型（世俗教父）——本篇不重复加行，Review 时提示主控酌情归一为 influence |
| 政治红线 | 访苏印象、CCNY 判词、古巴导弹危机通电、最后声明等**只按 page.md 客观转述**，不作政治评价、不展开叙事；通电全文可引（实载大写电文） |
| 战时立场 | 一战和平主义下狱与「相对政治和平主义」（1943）转变按 page.md 双段并陈——勿只写一半 |
| 四段婚姻 | 1894 Alys／1921 Dora／1936 Patricia／1952 Edith，年份与「离异/成婚」方向勿混 |
| 子女口径 | infobox 明载 3 子（John、Kate、Conrad）；Dora 1930 年所生 Harriet Ruth 归属 page.md 未明言——不入子女行 |
| 生死地 | 生于威尔士蒙茅斯郡、逝于威尔士 Penrhyndeudraeth，但自认 English——口径并写勿简化 |
| 引语红线 | 监狱自述、Einstein「伟大的精神……」公开信、George VI 对答、受奖相关表述均为 page.md 实载可用；其余禁编 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| analytic philosophy | 分析哲学 | 与 Moore 共同奠基，非独自创立 |
| logicism | 逻辑主义 | 数学可化归为逻辑的论题 |
| Russell's paradox | 罗素悖论 | 「所有不包含自身的集合的集合」 |
| theory of types | 类型论 | 悖论之解，1910 系统化 |
| On Denoting | 〈论指称〉 | 1905，「哲学的范式」 |
| Principia Mathematica | 《数学原理》 | 与 Whitehead 合著，勿与牛顿书名混淆 |
| secular godfather | 世俗教父 | John Stuart Mill 之职分 |
| Beacon Hill School | 灯塔山学校 | 1927 与 Dora 共创的实验教育 |
| Marriage and Morals | 《婚姻与道德》 | 1929，CCNY 风波源头 |
| A History of Western Philosophy | 《西方哲学史》 | 1945 |
| Russell–Einstein Manifesto | 罗素—爱因斯坦宣言 | 1955，核裁军 |
| relative political pacifism | 相对政治和平主义 | 1943 年立场表述 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**：**PAST**（分批文件预分配，勿改）
- **匹配理由**：PAST 的「历史感/深沉」标签精准匹配罗素的文学身位——《西方哲学史》以一人之笔纵览两千余年思想史，获奖理由亦落在「人道主义理想与思想自由」的世纪长跑上；其九十七年的人生（维多利亚时代出生、见证两次大战与冷战、1970 年辞世）本身就是一部「过去从未过去」的历史长卷。
- **备选（未采用）**：Timeless（同批已分配 Faulkner，避撞曲）；The Flow of Time（时间感贴切但受众偏低）。
- **本地路径**：对照 `music_audio/curated_tracks.md` 取 PAST 音频复制到本目录，`make video` 时 ffmpeg `-shortest` 对齐。

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
