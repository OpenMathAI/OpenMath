# 文学家立传提示词（OpenLiterature 实例：Eugenio Montale）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Eugenio Montale（1975 诺贝尔文学奖，意大利隐逸派诗歌巨匠）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按文学家适配：无公式框——以名句引文框、代表作书影、意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Eugenio Montale（欧金尼奥·蒙塔莱），意大利诗人、散文家、编辑、翻译家，1975 诺贝尔文学奖得主，隐逸派（Hermeticism）代表。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」骨架；本篇以「峭壁上的鳗鱼」为设计母题——在无幻觉的人生观下阐释人的价值，冷硬岩岸与顽强生命力的意象统一全篇。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Eugenio Montale（1896-10-12 ~ 1981-09-12，享年 84 岁）
- **气质关键词**：**隐逸派宗匠、冷峻的现代主义者、诗人兼乐评人** —— 1975 诺贝尔文学奖获奖理由：
  > "for his distinctive poetry, which, with great artistic sensitivity, has interpreted human values under the sign of an outlook on life with no illusions"（表彰其独特的诗歌，以巨大的艺术敏感性在无幻觉的人生观之下阐释人的价值）
- **设计母题**：**利古里亚的岩岸（Ligurian rocky coast）**。童年度假的 Monterosso 海岸风景是其诗歌底色——干燥的石缝、海风与灌木，对应「无幻觉人生观」的冷峻诗学；主色深绿呼应利古里亚的松柏与意大利国旗绿。
- **本地数据源**：`literature/presentations/pages/20th_century/Eugenio_Montale/page.md`（Wikipedia 全文 + frontmatter）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Eugenio_Montale
- **肖像**：第 0 步待下载（Wikipedia infobox 照；404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，以正文为准）

- 生卒：1896-10-12 生于热那亚（Genoa，时属意大利王国）~ 1981-09-12 逝于米兰，享年 84 岁
- 家世：化工品公司商人 Domenico Montale 之幼子，六兄妹中最小；母 Giuseppina Ricci
- 教育：热那亚小学；1911 入技术学校，1915 获会计文凭；同年随男中音 Ernesto Sivori 学声乐；一战步兵服役；1923 Sivori 去世后弃音乐转诗——大致自学成才
- 想象力深受 Dante Alighieri 等作家与外语（尤其英语）学习影响
- 1927 迁佛罗伦萨任 Bemporad 出版社编辑；1929 任 Gabinetto Vieusseux 图书馆馆长；1938 被法西斯政府开除该职
- 1925 首部诗集《Ossi di seppia》（乌贼骨）出版；同年签署《反法西斯知识分子宣言》
- 政治倾向：Piero Gobetti 与 Benedetto Croce 的自由主义；为 Gobetti 的《Il Baretti》撰稿、与《Solaria》杂志合作；常去佛罗伦萨文学咖啡馆 Le Giubbe Rosse，成为 Gadda、Loria、Vittorini 等人圈子的中心人物
- 1933–1938 与但丁学者 Irma Brandeis 恋爱；Brandeis 化名 Clizia（senhal，普罗旺斯行吟传统中的化名）进入《Le occasioni》
- 1948 起定居米兰；任《晚邮报》（Corriere della Sera）音乐编辑、驻外记者（曾随教皇保罗六世访以色列报道）；记者文集《Fuori di casa》(1969)
- 1950 年代与青年诗人 Maria Luisa Spaziani 相恋，化名 La Volpe（狐狸）进入《La bufera e altro》
- 妻：Drusilla Tanzi；《Satura》(1971) 收有著名的悼亡诗
- 1967-06-13 起任意大利参议院终身参议员
- 荣誉：米兰(1961)、剑桥(1967)、罗马(1974) 荣誉博士；1973 斯特鲁加诗歌之夜金桂冠；1975 诺贝尔文学奖
- 核心作品：《Ossi di seppia》(1925)、《Le occasioni》(1939)、《Finisterre》(1943)、《La bufera e altro》(1956)、《Xenia》(1966)、《Satura》(1971)、《Diario del '71 e del '72》(1973)
- 关键时间线（15 节点）：1896 热那亚出生 → 1915 会计文凭+学声乐 → 一战步兵 → 1923 Sivori 去世转诗 → 1925 《Ossi di seppia》+反法西斯宣言 → 1927 迁佛罗伦萨 → 1929 Vieusseux 馆长 → 1933–38 Brandeis 恋情 → 1938 被法西斯解职+《Le occasioni》→ 1948 迁米兰 → 1956 《La bufera e altro》→ 1966 《Xenia》→ 1967 终身参议员 → 1971 《Satura》→ 1975 诺贝尔奖 → 1981 米兰去世

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Eugenio_Montale/` 与 `images/`

### 第 2 步：复制 Makefile

- 复制同世纪已立传者目录的 Makefile，设置 `MAIN=Eugenio_Montale_zh`、`VIDEO_NAME=Eugenio_Montale_zh`

### 第 3 步：收集图片

- 肖像下载（curl -A "Mozilla/5.0" + file 验证）；404 则装饰圆占位；另备《Ossi di seppia》书影

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hermetic poetry | 隐逸派诗歌 | infobox Movement 明载 Hermeticism，意大利 20 世纪诗歌主流 | 核心页 |
| 1 | modernist poetry | 现代主义诗歌 | 反法西斯语境下的反 conformism 新诗 | 反抗页 |
| 2 | poetry translation | 诗歌翻译 | 《Quaderno di traduzioni》(1948) 等大量译作 | 译笔页 |
| 3 | literary criticism | 文学批评 | 两部批评专著与大量书评 | 批评页 |
| 4 | music criticism | 音乐评论 | 《晚邮报》音乐编辑，业余男中音出身 | 乐评页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Dante Alighieri | 无向 | 自幼想象力的来源；曾为《神曲》作序言；化名 Clizia 承 Beatrice 传统 |
| influence | T. S. Eliot | 无向 | page.md 明载「重要影响」，客观对应物（objective correlative）概念可能源于 Eliot；1948 作《Eliot and Ourselves》贺其六十寿 |
| influence | Ernesto Sivori | 无向 | 男中音声乐教师，1923 年去世促使他弃音乐转诗 |
| spouse | Drusilla Tanzi | 无向 | 妻，《Satura》收有悼其亡妻的沉痛诗篇 |
| colleague | Carlo Emilio Gadda | 无向 | Le Giubbe Rosse 咖啡馆文学圈同人 |
| colleague | Elio Vittorini | 无向 | Le Giubbe Rosse 文学圈同人、《Solaria》创办者之一 |
| colleague | Gianfranco Contini | 无向 | 文学批评家挚友，1943 将其诗集《Finisterre》走私带入瑞士出版 |
| influence | Irma Brandeis | 无向 | 犹太裔美国但丁学者，1933–1938 恋人，化名 Clizia 成为《Le occasioni》的女神形象 |
| influence | Joseph Brodsky | 无向 | 布罗茨基专文《In the Shadow of Dante》致敬蒙塔莱抒情诗 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：冷峻、干燥、岩岸的深绿与海的青灰
- **主色**：深绿 `#1E4D3B`（预分配）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeHermetic` 隐逸派 — 靛蓝 `#4C5FD5`
  - `badgeLiguria` 利古里亚 — 青绿 `#0E7C7B`
  - `badgeClizia` Clizia 诗章 — 玫瑰 `#C4204F`
  - `badgeMusic` 乐评 — 琥珀 `#E07B30`
- **背景母题**：干笔触岩岸纹理块面，稀疏点缀露珠状小圆（呼应其短诗的精确观察）

### 第 6 步：规划幻灯片序列（12–15 页）

```
00  OpenLiterature 项目首页（\input cover 共享页）
01  封面 — 无幻觉人生观下的价值阐释者 / Eugenio Montale 1896–1981 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、出生地、任职、荣誉、核心领域）
03  文学世界概览 — 隐逸派 / 现代主义 / 翻译 / 批评 / 乐评
04  热那亚与利古里亚（1896–1915）— 化学品商家幼子、Monterosso 夏日、会计文凭
05  弃乐从诗（1915–1925）— Sivori 门下、一战士兵、1923 转折、《Ossi di seppia》
06  反法西斯知识分子（1925–1927）— 宣言签名、Gobetti 与 Croce 自由主义
07  佛罗伦萨岁月（1927–1938）— Vieusseux 馆长、Le Giubbe Rosse 圈、《Solaria》
08  Clizia：《Le occasioni》（1933–1939）— Brandeis、senhal 传统、但丁 Beatrice 回声
09  战时与《La bufera e altro》（1943–1956）— Finisterre 走私出版、La Volpe
10  米兰晚年（1948–1981）— 晚邮报乐评、《Xenia》悼亡、《Satura》反讽
11  1975 诺贝尔奖 — 官方获奖理由原句引文框
12  荣誉与身后 — 终身参议员、金桂冠、Diario postumo 真伪之争
13  遗产 — Fortini 之评：20 世纪意大利诗歌的巅峰
14  结尾
```

### 第 7 步：编写 Beamer 源码

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide`。
- 名句引文框用获奖理由英文原句（page.md 明载），中文用官方中译对照。

### 第 8 步：布局检查

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删装饰 → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查

**Montale 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日 | page.md 正文 1896-10-12（frontmatter 另有 1896-01-12 噪声值），以 10-12 为准 |
| 国籍 | Italy + Kingdom of Italy（生于王国时期），按 page.md 口径分条 |
| Clizia 与 La Volpe | Clizia=Irma Brandeis（1933–38，前半期缪斯）；La Volpe=Maria Luisa Spaziani（1950s），两人勿混 |
| Diario postumo | 1996 年后出《Diario postumo》由 Annalisa Cima「整理」，批评家 Dante Isella 认为非真迹——只客观陈述争议，勿当正典 |
| objective correlative | page.md 用词为「可能受 Eliot 影响」（probably influenced），勿写成确证 |
| 政治内容 | 反法西斯宣言、被法西斯政府解职按 page.md 客观简述，不作政治评价展开 |
| Senator for life | 1967-06-13 起任终身参议员（infobox 明载 in office 起日），勿写「诺奖后获封」 |
| 作品年份 | 《Destrucción o amor》式的西语错记勿犯：《Destruction or Love》是 Aleixandre；Montale 对应物是《Le occasioni》——两篇诗人同名书目严禁串页 |
| 无载禁写 | 与 Ungaretti/Saba/Cardarelli 仅并列提及、无直接交往记载，勿建关系；与 Quasimodo 仅书名并列（《Lettere a Quasimodo》身后编），勿写师生 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Ossi di seppia | 《乌贼骨》 | 直译「墨鱼骨」，通行译名《乌贼骨》 |
| hermeticism | 隐逸派 | 亦译「密封诗派」，取通行译名 |
| objective correlative | 客观对应物 | 艾略特批评术语 |
| senhal | 化名（行吟诗传统） | 普罗旺斯行吟诗人对贵妇的隐称 |
| Le occasioni | 《 occasioni/境遇》 | 通行译名《莱奥卡齐奥尼》或《境遇》，统一即可 |
| Clizia | 克莉齐娅 | Brandeis 的诗中化名 |
| La Volpe | 狐狸 | Spaziani 的诗中化名 |
| Senator for life | 终身参议员 | 意大利荣誉职位 |
| Struga Poetry Evenings | 斯特鲁加诗歌之夜 | 金桂冠奖 1973 |
| Satura | 《萨图拉》 | 讽诗传统词源（satura lanx） |

---

## 四、背景音乐选择

- **选定曲目**: **Timeless** — Alex-Productions（132k views）
- **风格**: 高受众 / 沉稳 / 纪录片
- **匹配理由**:
  - "沉稳" 匹配 Montale 的冷峻诗学——无幻觉的人生观、干燥的意象、不动声色的精确
  - "纪录片" 匹配传记叙事——从热那亚岩岸到佛罗伦萨咖啡馆再到米兰晚邮报，八十五年思想演进
  - "长期纲领" 匹配其文学史地位——隐逸派主将、20 世纪意大利诗歌的高水位线，影响绵延
- **备选**（未采用）: PAST（历史感，受众略低）、The Flow of Time（时间感但情绪偏暖）
- **时长**: 需 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
