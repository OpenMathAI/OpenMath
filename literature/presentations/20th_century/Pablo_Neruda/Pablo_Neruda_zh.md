# 文学家立传提示词（OpenLiterature · Pablo Neruda）

> **目标项目**：OpenLiterature —— 开放文学史（与 OpenPhysicist/OpenChemist 共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Pablo Neruda（巴勃罗·聂鲁达，1971 诺贝尔文学奖）。
> **设计哲学**：文学家立传沿用「身份信息页 + 结构化研究领域」骨架；本篇无公式框，以**代表作书影/名句引文框/意象图式**替代。

---

## 一、模板定位

- **目标人物**：Pablo Neruda，1971 年诺贝尔文学奖得主，智利国民诗人。
- **一句话定位**：从情诗到史诗、从外交官到参议员——用诗歌「唤醒一个大陆的命运与梦想」的智利诗人-外交官。
- **适配说明**：物理学家的「公式框」在本篇一律替换为「名句引文框」（page.md 载有两段英译原诗，可直接用，见第 8 步）。

---

## 二、背景信息 【人物专属】

- **姓名**：Pablo Neruda（本名 Ricardo Eliécer Neftalí Reyes Basoalto）；中文通译 巴勃罗·聂鲁达。
- **生卒**：1904-07-12 生于 Parral（智利 Maule 大区）～ 1973-09-23 逝于圣地亚哥 Santa María 诊所，享年 69 岁。
  - ⚠️ metadata 死亡日期含 "1973-00-00" 噪声值，以正文 09-23 为准。
  - ⚠️ 官方死因列为中心力衰竭/前列腺癌并发症，但死因至今存争议（2013 起开棺调查、2023 报告称牙齿检出肉毒杆菌、2024 法院重启调查）——**立传中只客观陈述「官方死因 + 存在长期争议与司法调查」一句，不展开、不作结论**。
- **获奖**：1971 年诺贝尔文学奖（评选不易，瑞典学院内部分歧，瑞典译者 Artur Lundkvist 力推促成）。官方获奖理由（EN 原文，禁止改写）：
  > "for a poetry that with the action of an elemental force brings alive a continent's destiny and dreams"
  > 中译（名录 CITATION_ZH）：「表彰其诗歌，以原初之力般的行动唤醒了一个大陆的命运与梦想」。
  - 斯德哥尔摩受奖演说名句："A poet is at the same time a force for solidarity and for solitude."
- **气质关键词**：**情诗的火焰、大陆的史诗、政治的浪尖**。
- **设计母题**：**海洋与陆地（Sea & Continent）**——三座海边的房子（Isla Negra/La Sebastiana/La Chascona）、马丘比丘的石阶、安第斯山口；背景可用稀疏波浪线与大陆轮廓装饰。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Pablo_Neruda/page.md`（Wikipedia 全文，已核对）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL：https://en.wikipedia.org/wiki/Pablo_Neruda
- **肖像**：第 0 步待下载（page.md 内嵌 1963 年照等）。

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准（已核对 page.md，禁止再杜撰）

- **家庭**：父 José del Carmen Reyes Morales 铁路员工，反对儿子写作；母 Rosa Neftalí Basoalto Opazo 小学教师，在聂鲁达出生两个月后（1904-09-14）去世；在 Temuco 长大；无神论者。
- **笔名**：1920 年中起用 Pablo Neruda；来源一说捷克诗人 Jan Neruda，一说小提琴家 Wilma Neruda（见于柯南·道尔《血字的研究》）——两说并写勿定论。
- **少年成名**：13 岁（1917-07-18）在地方报 La Mañana 发表首作；1919 Juegos Florales del Maule 诗赛第三名；特木科当地学校负责人、后来的诺奖得主 Gabriela Mistral 曾鼓励其写作。
- **早期代表作**：1921 赴圣地亚哥智利大学修法语；1923 《Crepusculario》（借作家 Eduardo Barrios 之助结识出版商 Nascimento）；1924 《二十首情诗和一支绝望的歌》——至今仍是西班牙语最畅销诗集；1926 《tentativa del hombre infinito》与小说《El habitante y su esperanza》。
- **外交生涯**：1927 出于经济窘迫赴仰光任名誉领事，后 Colombo/Batavia/Singapore，写《Residencia en la tierra》超现实主义诗篇；后任布宜诺斯艾利斯、巴塞罗那领事，1935 接替 Gabriela Mistral 任马德里领事，成为文学圈中心（Alberti、García Lorca、Vallejo）；1940-43 墨西哥城总领事；1971-03 至 1973-02 驻法国大使（最后一任）。
- **西班牙内战与转向**：García Lorca 被杀是其政治化最重要催化剂；1937 出诗集《España en el corazón》并出席第二届国际作家大会（与 Malraux、Hemingway、Spender 同会）；1938 应总统 Aguirre Cerda 任命为巴黎西班牙移民事务专任领事，组织 Winnipeg 号轮船运送 2,000 名西班牙难民赴智利（自称「我此生最高贵的使命」）。
- **美洲史诗**：1943 秘鲁之行登马丘比丘 → 1945 完成《Alturas de Macchu Picchu》→ 1950 《Canto General》（惠特曼式南美史诗，逃亡马背上携 manuscript，地下时期写成大半）。
- **参议员与流亡**：1945-03-04 当选共产党参议员（Antofagasta/Tarapacá），四个月后正式入党；1948-01-06 参议院「Yo acuso」（我控诉）演讲；被通缉后匿藏 13 个月，1949-03 骑马翻越 Lilpela 山口流亡阿根廷三年（借友人 Miguel Ángel Asturias 护照赴欧，Picasso 安排入境巴黎）；1952-08 回国。
- **婚姻**：Maruca（Marijke Antonieta Hagenaar Vogelzang，荷兰银行职员，1930 巴塔维亚结婚，后离异）；Delia del Carril（阿根廷艺术家，年长 20 岁，1943 于墨西哥 Tetecala 结婚，1955 分离）；Matilde Urrutia（智利歌手，1949 墨西哥护理时相识，《Los versos del capitán》1952 匿名出版之缪斯，1966 结婚）。
- **子女**：独女 Malva Marina (Trinidad) Reyes，1934 生于马德里，患脑积水，1943 年 8 岁殁于纳粹占领下的荷兰。
- **晚年荣誉与死亡**：International Peace Prize 1950；Stalin Peace Prize 1953；Nobel 1971；Golden Wreath（Struga 诗歌之夜）1972；1973-09-11 智利政变后准备流亡墨西哥，09-23 病逝；葬礼成为大规模抗议场合；1974 遗作回忆录《I Confess I Have Lived》由 Matilde Urrutia 整理出版；与 Matilde 合葬 Isla Negra。
- **关键时间线（16 节点）**：1904 Parral 出生、母亲早逝 → 1914 冬写下首批诗 → 1917 首作见报 → 1920 启用笔名 → 1923 《Crepusculario》→ 1924 《二十首情诗》→ 1927 赴缅甸任领事 → 1935 马德里领事、文学圈中心 → 1937 西班牙内战诗集与作家大会 → 1939 Winnipeg 号救援 → 1943 马丘比丘 → 1945 当选参议员 → 1948 「Yo acuso」→ 1949 骑马流亡 → 1950 《Canto General》→ 1952 回国 → 1966 与 Matilde 结婚、访美录制国会图书馆 → 1970 转而支持 Allende 竞选 → 1971 诺贝尔奖 + 驻法大使 → 1972 金冠奖 → 1973-09-23 逝世。

### 第 4 步：文学领域表（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | love poetry | 情诗 | 《二十首情诗》《船长之歌》 | 核心页 |
| 1 | political poetry | 政治诗 | 《西班牙在我心中》《漫歌集》 | 内战页 |
| 2 | epic poetry | 史诗长诗 | 《漫歌集》《马丘比丘之巅》 | 美洲页 |
| 3 | surrealist poetry | 超现实主义诗 | 《Residencia en la tierra》 | 领事页 |
| 4 | autobiographical prose | 自传性散文 | 回忆录《I Confess I Have Lived》 | 晚年页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致，仅收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marijke Antonieta Hagenaar Vogelzang | 无向 | 1930 巴塔维亚结婚，后离异 |
| spouse | Delia del Carril | 无向 | 1943 墨西哥结婚，1955 分离，阿根廷艺术家 |
| spouse | Matilde Urrutia | 无向 | 1966 结婚，《船长之歌》缪斯，合葬 Isla Negra |
| parent-child | Malva Marina Reyes | 无向 | 独女（1934–1943） |
| influence | Gabriela Mistral | 无向 | 特木科学校负责人，少年时鼓励其写作 |
| colleague | Eduardo Barrios | 无向 | 作家，引荐出版商 Nascimento |
| colleague | Federico García Lorca | 无向 | 马德里文学圈挚友，其遇害成为政治转向催化剂 |
| colleague | Rafael Alberti | 无向 | 马德里文学圈友人 |
| colleague | César Vallejo | 无向 | 马德里文学圈友人，秘鲁诗人 |
| controversy | Octavio Paz | 无向 | 挚友因斯大林主义立场分歧而决裂 |
| colleague | Miguel Ángel Asturias | 无向 | 友人，1949 流亡中借其护照赴欧 |
| colleague | Salvador Allende | 无向 | 密切顾问，1970-73 任其政府驻法大使 |
| colleague | Arthur Miller | 无向 | 1966 国际笔会纽约会议主办方，促成赴美签证 |
| colleague | Sergio Ortega | 无向 | 1967 合作音乐剧《Joaquín Murieta 的光辉与死亡》 |

> 政治红线：斯大林颂诗、Stalin Peace Prize、托洛茨基案 Siqueiros 签证事件、1957 中国行观感等只按 page.md 客观简述一句，不作政治评价、不展开；Borges/Paz 的负面评价引语禁入正文。

### 第 5 步：配色方案

- **主色**（预分配）：深靛紫 `#283593`（海洋与大陆的深邃）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeLove` 情诗 — 玫瑰红 `#C2185B`
  - `badgePolitical` 政治诗 — 铁锈红 `#A63A2B`
  - `badgeEpic` 史诗长诗 — 暗金 `#B08A3E`
  - `badgeSurreal` 超现实主义 — 深青 `#00796B`
- **背景母题**：波浪与大陆轮廓的稀疏装饰圆。

### 第 6 步：幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 唤醒一个大陆的诗人 / Pablo Neruda 1904–1973 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名/生卒/三段婚姻/外交任职/荣誉/核心领域）
03  核心贡献概览 — 情诗 / 政治诗 / 史诗长诗 / 超现实主义
04  少年诗人：Temuco 与笔名 (1904–1924) — 13 岁发表、Mistral 鼓励、二十首情诗
05  东方领事：孤独与《居住在地球上》(1927–1935) — 仰光/科伦坡/巴塔维亚
06  马德里文学圈 (1935–1937) — Lorca/Alberti/Vallejo、内战转向（名句引文框）
07  Winnipeg 号：最高贵的使命 (1939) — 2000 名西班牙难民
08  马丘比丘与《漫歌集》(1943–1950)（核心贡献页·书影替代公式框）
09  参议员与「我控诉」(1945–1948) — 共产党参议员、Lota 矿工
10  骑马越安第斯：流亡三年 (1949–1952) — Asturias 护照、Picasso、Matilde
11  《船长之歌》与爱情三重奏（名句引文框）— 三段婚姻与 Matilde
12  诺贝尔奖 1970-71 — 评选波折、Lundkvist、斯德哥尔摩演说
13  驻法大使与最后岁月 (1971–1973) — 三座博物馆故居、逝世争议一笔带过
14  遗产：国民诗人 — 三故居、被谱曲的诗、《Il Postino》
15  结尾
```

### 第 7 步：版式要点

- 身份信息页含本名（Ricardo Eliécer Neftalí Reyes Basoalto）——「笔名」是本篇身份页的天然亮点。
- 引文框可用 page.md 两段英译原诗（"Poetry" / "Full Woman, Fleshly Apple, Hot Moon"），斜体排版，注明译者在 page.md 的标注（Alastair Reid / Stephen Mitchell）。
- 政治内容页（09/10）克制：只陈述职务、演讲名、逃亡路线，不引争议言论。

### 第 8 步：专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 本名与笔名 | 全篇需区分本名 Reyes Basoalto 与笔名 Neruda；笔名来源两说（Jan Neruda/Wilma Neruda）并写勿定论 |
| 获奖年份 | 1971 获奖且亲赴斯德哥尔摩受奖（与 Solzhenitsyn 1970 未亲领不同） |
| 死因 | 只写「官方死因 + 长期争议与司法调查存续」，禁写「被毒杀」定论 |
| 离婚年份 | 第一段婚姻 infobox 作 1942、正文作 1943 墨西哥判决——以「后离异」模糊处理或双口径注 |
| 政治红线 | 斯大林颂诗/Stalin Peace Prize/Siqueiros/卡斯特罗等内容一句话客观带过，不作评价；Borges「不钦佩其为人」与 Paz 的批评引语禁入正文 |
| 回忆录争议段 | 1929 Ceylon 性侵段落引发 2018 机场命名抗议——立传中禁展开，不入片 |
| Winnipeg 数字 | 2,000 名难民（聂鲁达亲自遴选仅数百人，其余由 Negrín 机构遴选） |
| 《España en el corazón》年份 | page.md 作品列表作 1937（正文另作 1938 出版），以作品列表 1937 为准并可加注 |
| 女儿 | Malva Marina 1934 生 1943 殁，page.md 载聂鲁达对其疏离——如提及须忠于原文，不渲染 |
| 无载禁写 | García Márquez「20 世纪任何语言中最伟大的诗人」是评价引语非关系，禁建关系；与 Whitman 仅 "Whitmanesque" 一词的风格形容，禁建 influence 关系；与 Picasso 仅「安排入境」事实，无深交记载不入库 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| Veinte poemas de amor | 《二十首情诗和一支绝望的歌》 | 1924，西语最畅销诗集 |
| Residencia en la tierra | 《居住在地球上》 | 超现实主义时期 |
| España en el corazón | 《西班牙在我心中》 | 1937 内战诗集 |
| Canto General | 《漫歌集》 | 1950 南美史诗 |
| Alturas de Macchu Picchu | 《马丘比丘之巅》 | 《漫歌集》第二部，12 节长诗 |
| Los versos del capitán | 《船长之歌》 | 1952 匿名出版，缪斯 Matilde |
| Odas elementales | 《元素颂》 | 1954 |
| Yo acuso | 「我控诉」 | 1948-01-06 参议院演讲 |
| Winnipeg | 「温尼伯号」 | 1939 难民船 |
| poet-diplomat | 诗人-外交官 | 其职业双重性的通称 |
| Stalin Peace Prize | 斯大林和平奖 | 1953，须客观语境 |
| Golden Wreath | 金冠奖 | 1972 Struga 诗歌之夜 |
| La Chascona / La Sebastiana / Isla Negra | 三座故居 | 现均为博物馆，Isla Negra 为安葬地 |

---

## 四、BGM 建议

- **选定曲目**：**Tragedy** — Alex-Productions（预分配）。
- **匹配理由**：曲名的悲剧张力匹配聂鲁达一生的高潮与骤停——1971 登顶诺奖与 1973 政变后 12 日内离世；低沉弦乐质感匹配马丘比丘石阶与安第斯流亡的厚重；起伏幅度大，匹配情诗与政治诗的双声部。
- **备选**（未采用）：Cinematic Experience（过于宏大，弱化悲剧收束）；Savage（已分配给 Solzhenitsyn，批内不重复）。
- **时长**：以 `music_audio/curated_tracks.md` 为准，>16 页 × 7 秒即可，ffmpeg `-shortest` 对齐。

---

## 五、数据入库说明（已完成）

- **yaml**：`MySQL/data/Pablo_Neruda.yaml`，name_en=`Pablo Neruda`（frontmatter 原形），qid=Q34189，primary_occupation=`writer`，fields 5 条（第 4 步表），relations 14 条（第 4.5 步表）。
- **入库**：`python3 seed_person.py data/Pablo_Neruda.yaml`（幂等，按 QID → name_en 匹配）。
- **验证**：has_social_data=1、person_field≥4、person_relation≥2。

> **开始执行 Beamer 立传时，每写一页就 make，看到溢出就修。**
