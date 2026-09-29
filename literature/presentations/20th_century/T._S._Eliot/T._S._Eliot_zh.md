# 文学家立传提示词（OpenLiterature：T. S. Eliot）

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，与数学/物理/化学侧同构）。
- **本实例**：Thomas Stearns Eliot（托马斯·斯特恩斯·艾略特），1948 年诺贝尔文学奖得主，英语现代主义诗歌领袖、批评家与剧作家。
- **设计哲学**：文学家立传以「身份信息页 + 研究领域表」为骨架（与物理学家模板同构），但以**代表作书影 / 名句引文框 / 意象图式**替代公式框——艾略特的视觉母题是「荒原与四重奏」：断片拼贴的现代荒原、走向「静止点」的宗教沉思。

## 二、背景信息 【人物专属】

- **目标文学家**：T. S. Eliot（1888-09-26 ~ 1965-01-04，享年 76 岁）
- **姓名**：Thomas Stearns Eliot ／ 托马斯·斯特恩斯·艾略特（yaml name_en 用 frontmatter 形式）
- **诺奖年份**：1948 年诺贝尔文学奖，官方获奖理由（禁止改写）：
  > "for his outstanding, pioneer contribution to present-day poetry"（表彰其对当代诗歌的杰出开创性贡献）
- **气质关键词**：现代主义的立法者、断片的拼贴师、改宗的古典主义者
- **设计母题**：**「荒原与四重奏」**——《荒原》的断片引文拼贴（"四月是最残忍的月份"）、《四个四重奏》的四元素（气/土/水/火）与「静止点」；辅以圣路易斯密西西比河与东科克教堂，构成「始与终互嵌」（In my beginning is my end）的视觉语言。
- **本地数据源**：`literature/presentations/pages/20th_century/T._S._Eliot/page.md`（+ metadata.json、images.txt）
- **Wikipedia**：https://en.wikipedia.org/wiki/T._S._Eliot （肖像第 0 步下载：infobox 用 1934 年照；备选 Ottoline Morrell 1923 照 File:T.S._Eliot,_1923.JPG、Wyndham Lewis 1938 肖像画）

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇歧义先征求意见。含「研究领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库（MySQL）。

### 第 0 步：事实基准（已核对，以正文为准）

- **生卒**：1888-09-26 生于美国密苏里州圣路易斯 ～ 1965-01-04 逝于伦敦肯辛顿（肺气肿），享年 76 岁；Golders Green 火化，骨灰按遗愿归葬萨默塞特郡东科克（East Coker，其祖先离英赴美的村庄），教堂壁铭引《东科克》"In my beginning is my end. In my end is my beginning."；1967 年威斯敏斯特教堂「诗人角」立石。
- **国籍**：美国（至 1927）→ 英国（1927 年 11 月入英籍并放弃美国国籍）。Nobel 官方口径 UK (born in the US)。
- **家庭**：波士顿婆罗门（Boston Brahmin）名门；祖父 William Greenleaf Eliot 赴圣路易斯创建唯一神教会；父 Henry Ware Eliot 为砖业公司总裁；母 Charlotte Champe Stearns 写诗、系美国早期社工；幼名 Tom，六子中最幼。两段婚姻均无子女：Vivienne Haigh-Wood（1915-06-26 汉普斯特德登记处成婚，1933 正式分居，1938 被兄长 Maurice 送入精神病院，1947 死于心脏病）；Esmé Valerie Fletcher（1957-01-10 秘密婚礼，时 68 岁娶 30 岁的费伯旧秘书）。
- **教育**：Smith Academy（1898–1905）→ Milton Academy 预备年 → Harvard College 1906–1909（AB，选修制近比较文学）→ 1910 哈佛 MA（英国文学）→ 1910–1911 巴黎大学哲学（旁听柏格森、与 Alain-Fournier 读诗）→ 1911–1914 回哈佛研印度哲学与梵文 → 1914 奖学金入牛津 Merton College（一年后离开）；1916 完成哈佛博士论文《知识与经验——F. H. 布拉德雷哲学》，未返美答辩。
- **文学师承与影响（仅收 page.md 明载）**：1908 年读 Arthur Symons《文学的象征主义运动》而入法国象征派（Laforgue、Rimbaud、Verlaine，并经由 Verlaine 知 Corbière《Les amours jaunes》——"影响了艾略特一生的走向"）；14 岁因读 FitzGerald 译《鲁拜集》始写诗；《普鲁弗洛克》结构深受但丁影响；印度传统（《奥义书》、梵文）构成其思想底色；自认「教我用自己声音的诗只在法语中存在」（1940 论叶茨文）。
- **任职**：哈佛哲学助教（1909–1910）→ 1915 Birkbeck 学院英文教师 → Highgate School（教法文拉丁文，学生含 John Betjeman）与 High Wycombe 皇家文法学校 → 1917 劳埃德银行（外国账户）→ 1925 年起任费伯出版社（Faber and Gwyer → Faber & Faber）董事至终老；1922 创办评论季刊《标准》（The Criterion）；二战任空袭预警员（the Blitz）；1949 年客座普林斯顿高等研究院期间写《鸡尾酒会》。
- **关键荣誉**：1948 诺贝尔文学奖 + 功绩勋章（OM）；1950 Tony 最佳戏剧（《鸡尾酒会》百老汇版）；1955 汉萨歌德奖；1959 但丁奖章（佛罗伦萨）；1951 法国荣誉军团军官勋章；1960 法国艺术与文学指挥官勋章；1964 美国总统自由勋章；1983 两项 Tony（《猫》词曲，追授）+ 1982 Ivor Novello 奖（〈Memory〉）； Phi Beta Kappa（1935）、美国艺术与科学院（1954）、美国哲学学会（1960）、13 个荣誉博士（含牛津/剑桥/索邦/哈佛）。
- **核心作品与贡献（4–6 条）**：
  1. 《J. 阿尔弗雷德·普鲁弗洛克的情歌》（1915，Pound 推荐刊于 Poetry；22 岁写就，「被乙醚麻醉的病人」开场惊世）
  2. 《荒原》（1922，《标准》创刊号；献给 Pound "il miglior fabbro"——大砍手稿的「更好的匠人」；现代文学试金石，与同年《尤利西斯》并峙）
  3. 《空心人》（1925，「世界就这样终结/不是砰然一声，而是一声呜咽」）
  4. 《圣灰星期三》（1930，1927 年改宗后的「皈依之诗」）
  5. 《四个四重奏》（1936–1942 四首分刊：Burnt Norton/East Coker/The Dry Salvages/Little Gidding；自认巅峰之作，亦是得诺奖的最大推力）
  6. 诗剧《大教堂凶杀案》（1935，坎特伯雷戏剧节委约，贝克特殉道）与《鸡尾酒会》（1949）；谐趣诗《老负鼠的实用猫经》（1939，"Old Possum" 是 Pound 给他的绰号，后成音乐剧《猫》）
- **关键时间线（15–20 节点）**：1888 生于圣路易斯 → 1898–1905 Smith Academy（首诗〈A Fable For Feasters〉1905 刊出）→ 1906–1910 哈佛（1908 读 Symons 入象征派）→ 1909–1910 哲学助教 → 1910–1911 巴黎大学 → 1911–1914 哈佛（印度哲学/梵文；恋 Emily Hale）→ 1914 奖学金赴牛津；9-22 经 Aiken 引荐访 Pound 伦敦寓所（"worth watching"）→ 1915 〈普鲁弗洛克〉刊出、6-26 与 Vivienne 成婚（新婚借住 Russell 公寓）→ 1916 完成博士论文未答辩 → 1917《普鲁弗洛克及其观察》首部诗集、入劳埃德银行 → 1920 巴黎初见乔伊斯 → 1922《荒原》刊于《标准》创刊号 → 1925 入费伯出版社、《空心人》 → 1927-06-29 改宗英国国教（Anglo-Catholic：「文学上的古典主义者、政治上的保皇派、宗教上的英国国教徒」）、11 月入英籍 → 1930《圣灰星期三》 → 1932–1933 哈佛 Norton 讲席、回国后与 Vivienne 正式分居 → 1934《磐石》→ 1935《大教堂凶杀案》→ 1936–1942《四个四重奏》四首 → 1938 Vivienne 被送精神病院、Lewis 为其画像 → 1939《老负鼠的实用猫经》→ 1947 Vivienne 去世 → 1948 诺贝尔奖 + 功绩勋章 → 1949《鸡尾酒会》（1950 Tony）→ 1957 与 Valerie Fletcher 秘密成婚（与友 John Davy Hayward 合住的 Carlyle Mansions 岁月结束）→ 1965-01-04 逝于伦敦 → 骨灰归葬东科克 → 1981 音乐剧《猫》西区首演。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `literature/presentations/20th_century/T._S._Eliot/`（+ `images/`），Makefile 设 `MAIN=T._S._Eliot_zh`；肖像下载（curl `-A "Mozilla/5.0"`，file 验证；失败用 Commons Special:FilePath 回退）。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist poetry | 现代主义诗歌 | 改变英语诗歌语言与结构的领袖人物 | 荒原页 |
| 1 | poetry | 诗歌 | 少而精的总体创作观 | 作品页 |
| 2 | literary criticism | 文学批评 | 《传统与个人才能》/客观对应物，深刻影响新批评派 | 批评页 |
| 3 | verse drama | 诗剧 | 《大教堂凶杀案》《鸡尾酒会》 | 戏剧页 |
| 4 | light verse | 谐趣诗 | 《老负鼠的实用猫经》→《猫》 | 猫页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Ezra Pound | 无向 | 1914 年起的关键推手，《荒原》大砍手稿并题献 il miglior fabbro |
| colleague | Conrad Aiken | 无向 | 哈佛同窗终生挚友，1914 年引荐 Pound |
| colleague | James Joyce | 无向 | 1920 巴黎初见后成为挚友 |
| colleague | Wyndham Lewis | 无向 | 挚友，1938 年为其作著名肖像画 |
| colleague | Scofield Thayer | 无向 | Milton 同学，《荒原》刊行者，并引其识 Vivienne |
| colleague | Bertrand Russell | 无向 | 新婚时借住其公寓，Russell 对 Vivienne 表示关注（绯闻未经证实） |
| colleague | John Davy Hayward | 无向 | 1946–1957 合住 Chelsea，自称「艾略特档案保管人」 |
| colleague | Geoffrey Faber | 无向 | 1925 年经 Whibley 引荐入费伯出版社任董事 |
| colleague | Andrew Lloyd Webber | 无向 | 《猫》（1981）取材《实用猫经》，1983 追授 Tony 与其共享 |
| spouse | Vivienne Haigh-Wood | 无向 | 1915 成婚，1933 正式分居，1947 去世 |
| spouse | Esmé Valerie Fletcher | 无向 | 1957 秘密成婚，旧秘书，后为其遗稿编纂者 |
| advisor-student | John Betjeman | 艾略特→学生 | Highgate School 任教时的学生 |
| influence | Jules Laforgue | 影响→艾略特 | 1908 经 Symons 之书发现，象征派口音之源 |
| influence | Arthur Rimbaud / Paul Verlaine / Tristan Corbière | 影响→艾略特 | 法国象征派谱系，Corbière《Les amours jaunes》影响其一生走向 |
| influence | Dante Alighieri | 影响→艾略特 | 《普鲁弗洛克》至《四个四重奏》的但丁底色 |
| influence | F. H. Bradley | 影响→艾略特 | 哈佛博士论文研究对象（未答辩） |
| influence | Henri Bergson | 影响→艾略特 | 1910–1911 巴黎大学旁听其讲座 |
| influence | Virginia Woolf | 艾略特→影响 | 页面明载受其影响的作家之一 |
| influence | George Seferis | 艾略特→影响 | 1936 年出版《荒原》现代希腊语译本 |
| influence | Seamus Heaney / Derek Walcott | 艾略特→影响 | 两位后来获诺奖的诗人明载受其影响 |

#### 4.5.1 入库操作

- `MySQL/data/T._S._Eliot.yaml` + `cd MySQL && python3 seed_person.py data/T._S._Eliot.yaml`（幂等）；校验 fields≥4、relations≥2。

### 第 5 步：设计配色 【人物专属】

- **主色**：荒原青蓝 `#0E4D64`（预分配，勿改）；诺奖香槟金 `C9A227`。
- badgeA–D：badgeA 荒原 — 靛蓝 `#4C5FD5`；badgeB 四重奏/静止点 — 青绿 `#0E7C7B`；badgeC 诗剧 — 琥珀 `#E07B30`；badgeD 批评 — 玫瑰 `#C4204F`。
- 背景母题：断片引文条（错落小纸片，呼应《荒原》拼贴）+ 四元素小徽记。

### 第 6 步：规划幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 现代主义诗歌的立法者 / T. S. Eliot 1888–1965 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名、国籍变迁、教育、两段婚姻、Faber、荣誉、核心领域）
03  核心作品概览 — 五大节点年表书影（普鲁弗洛克→荒原→空心人→圣灰星期三→四重奏）
04  圣路易斯与哈佛 (1888–1914) — 密西西比河、Smith Academy、1908 象征派之门
05  巴黎与印度 (1910–1914) — 旁听柏格森、梵文与《奥义书》、Merton 一年
06  Pound 与伦敦 (1914–1917) — "worth watching"、〈普鲁弗洛克〉、劳埃德银行
07  《荒原》(1922) — 大砍手稿、il miglior fabbro、断片拼贴引文框
08  改宗与入籍 (1927) — Anglo-Catholic 三合一自白、《圣灰星期三》
09  《空心人》与费伯岁月 (1925–1939) — 出版人生涯、《标准》季刊、Auden/Hughes 皆出自其门
10  《四个四重奏》(1936–1942) — 四元素、静止点、东科克引文
11  诗剧 (1934–1958) — 大教堂凶杀案、鸡尾酒会、Tony 1950
12  《实用猫经》与《猫》 — Old Possum、West End 1981、Memory、追授 Tony
13  两段婚姻 — Vivienne 之痛与荒原心境、1957 秘密婚礼（客观转述）
14  荣誉与认可 — Nobel 1948 · OM · 名句引文框（诗人角铭文）
15  遗产：从「艾略特时代」到《猫》 — 批评与再评、Walcott/Heaney/Seferis 一脉、结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用，人物专属内容】

- 版式：`p{}` 窄列用 `\newcolumntype{P}[1]`；英语诗句引文框用小号斜体；frame 标题过长缩短即可；文学页用书影/引文框替代公式框。
- 陷阱：

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | yaml name_en 用 frontmatter "Thomas Stearns Eliot"；展示名可用 T. S. Eliot，但勿写「托马斯·斯特恩斯·艾略特」以外的中文译名 |
| 国籍变迁 | 美国至 1927、1927-11 入英籍并放弃美国籍——三段口径（美国→英国/生于美国）勿混用 |
| 《荒原》署谢 | 献辞 "il miglior fabbro" 是 Pound 的大砍之功——勿写成 Eliot 自拟 |
| Old Possum | 是 Pound 给 Eliot 的绰号——方向勿反 |
| Russell 一节 | 仅写 page.md 明载（新婚借住其公寓、关注 Vivienne、绯闻「未经证实」），不作渲染 |
| Vivienne 后事 | 1938 由其兄 Maurice 违愿送入精神病院、1947 死于心脏病、Eliot 未曾探视——按 page.md 客观转述 |
| 反犹争议 | Anthony Julius 等批评与 Raine/Eagleton 等辩护并存——只按 page.md 并列客观转述，不作评判、不引整段争议诗句 |
| 四重奏元素 | air/earth/water/fire 依次对应 Burnt Norton/East Coker/The Dry Salvages/Little Gidding——次序勿乱 |
| Tony 年份 | 《鸡尾酒会》1950 最佳戏剧（在世）；《猫》两项 Tony 1983 为追授——勿混 |
| 诺奖推力 | page.md 明载《四个四重奏》「最直接导向诺奖」——可写，但勿写成「获奖理由即四重奏」（官方理由是对当代诗歌的开创性贡献） |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| modernist poetry | 现代主义诗歌 | 与象征派传统衔接 |
| objective correlative | 客观对应物 | 《哈姆雷特及其问题》提出的批评概念 |
| Tradition and the Individual Talent | 《传统与个人才能》 | 1919 经典论文 |
| New Criticism | 新批评派 | 受其深刻影响的学派，非其创立 |
| The Waste Land | 《荒原》 | 1922 |
| il miglior fabbro | 更好的匠人 | 但丁语，献予 Pound |
| Four Quartets | 《四个四重奏》 | 1936–1942 |
| Anglo-Catholic | 英国国教高教会派 | 1927 改宗口径 |
| Boston Brahmin | 波士顿婆罗门 | 新英格兰名门雅称 |
| Old Possum's Book of Practical Cats | 《老负鼠的实用猫经》 | 1939 |
| Faber & Faber | 费伯出版社 | 1925–1965 供职 |
| Poets' Corner | 诗人角 | 威斯敏斯特教堂，1967 立石 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**：**New Lands**（分批文件预分配，勿改）
- **匹配理由**：New Lands 的「开拓/新境」标签精准匹配诺奖官方理由 "outstanding, pioneer contribution"——艾略特以〈普鲁弗洛克〉与《荒原》为英语诗歌开辟新大陆，1927 年改宗与入籍又是人生疆界的新陆；曲目的「启程感」贴合 25 岁离美赴英、在异邦语言中重建自身传统的传记弧线。
- **备选（未采用）**：The Flow of Time（时间主题贴合《四重奏》，但受众偏低且已在他批出现频次高）；Eternals（已分配同批 Hesse，避撞曲）。
- **本地路径**：对照 `music_audio/curated_tracks.md` 取 New Lands 音频复制到本目录，`make video` 时 ffmpeg `-shortest` 对齐。

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
