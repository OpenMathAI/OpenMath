# 文学家立传提示词（Mikhail Sholokhov）

> **OpenLiterature 人物专属立传提示词**：Mikhail Sholokhov（米哈伊尔·肖洛霍夫，1965 诺贝尔文学奖，苏联）。
> 执行 agent 按第三部分第 0–9 步逐步执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Mikhail Aleksandrovich Sholokhov（米哈伊尔·亚历山德罗维奇·肖洛霍夫），顿河哥萨克命运的史诗记录者。
- **设计哲学**：文学家立传无公式框，以**代表作书影、名句引文框、意象图式**替代物理公式表达；必须有「身份信息页」（Identity / Bio 速览页），务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Mikhail Sholokhov（1905-05-24 [儒略历 05-11] ~ 1984-02-21，享年 78 岁；出生日期 metadata 有 05-11/05-24 两值，取公历 05-24 并注旧历）
- **官方获奖理由（Nobel 官方 EN 原文 + 名录中译，禁止改写）**：
  > "for the artistic power and integrity with which, in his epic of the Don, he has given expression to a historic phase in the life of the Russian people"
  > 「表彰其《静静的顿河》史诗所展现的艺术力量与完整性，表达了俄罗斯人民生活中的一个历史阶段」（1965 授予）
- **气质关键词**：**顿河的史诗家、哥萨克命运的书记官、争议与荣光并行的诺奖得主**。
- **设计母题**：**顿河与草原（The Don & the Steppe）**。静静流淌的顿河、哥萨克村镇（stanitsa）的木屋、起伏的草原——用河流曲线、马蹄剪影与麦浪构成视觉母题。
- **本地数据源**：`literature/presentations/pages/20th_century/Mikhail_Sholokhov/page.md`（+ metadata.json / images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Mikhail_Sholokhov
- **肖像**：第 0 步待下载（images.txt 有 1960 照、1938–39 科夫里金肖像、1924 与妻合影等真实照片可用）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；封面 `\input` 项目共享首页。

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，直接使用）

- 生卒：1905-05-24 生于俄罗斯帝国顿河军州克鲁日林村（维申斯卡亚镇辖区）~ 1984-02-21 逝于维申斯卡亚（喉癌），享年 78 岁；葬于自宅院内，与妻 Maria 合葬。
- 家庭：非顿河哥萨克出身，而是「外来户」（*inogorodnye*，无哥萨克选举权）；父 Aleksander Mikhailovich Sholokhov（1865–1925），俄罗斯人，务农/贩牛/磨坊为生；母 Anastasia Danilovna Chernikova（1871–1942），乌克兰契尔尼戈夫农民之女、哥萨克遗孀，成年后才为与儿子通信学会读写——**1942 年维申斯卡亚遭轰炸时丧生**。妻 Maria Petrovna Gromoslavskaia（1924 年成婚，布卡诺夫斯卡亚村阿塔曼 Pyotr Gromoslavsky 之女；生年页内 1901/1902 两说），育二女二子。
- 教育：卡金卡亚/莫斯科/博古恰尔/维申斯卡亚等地学校，1918 年 13 岁辍学参加俄国内战（红军/布尔什维克一方，1917–1922 兵役栏）。
- 早年谋生：1922 赴莫斯科当记者，同时做码头工/石匠/会计（1922–1924）；17 岁开始写作，19 岁完成首篇短篇《胎记》。
- 关键荣誉：State Stalin Prize 1st degree（1941，《静静的顿河》）；**Lenin Prize（1960，《被开垦的处女地》）**；**Nobel Literature 1965**；两度 Hero of Socialist Labour（1967、1980）；六枚 Order of Lenin（1939/1955/1965/1967/1975/1980）；Order of the October Revolution（1972）；卫国战争勋章（1945 一级）；保加利亚季米特洛夫勋章/基里尔与梅多迪勋章、东德人民友谊之星、蒙古苏赫巴托勋章；Alexander Fadeyev Medal；1939 当选苏联科学院院士；1961 任苏共中央委员；最高苏维埃成员；苏联作家协会副理事长。
- 核心作品（4–6 条）：《静静的顿河》*And Quiet Flows the Don*（4 卷，1928–1940，历时 14 年，哥萨克在战前/一战/内战中的命运，1957–58 Gerasimov 三部曲电影）；《被开垦的处女地》*Virgin Soil Upturned*（两部：《种子》1932、《顿河收成》1960，历时 28 年，集体化题材，被誉社会主义现实主义典范，在中译后对中国社会主义文学有影响）；《顿河故事》*Tales from the Don*（1926，首部书）；《一个人的遭遇》*Fate of a Man*（1956–57，1959 Bondarchuk 电影）；未竟的《他们为祖国而战》（1942/1959，1975 电影）；《仇恨的科学》（1942）。
- 关键时间线（15–20 节点）：1905 生克鲁日林村 → 1918 13 岁参加内战 → 1922 赴莫斯科做记者与苦力 → 1923-10-19 首篇刊出《考验》 → 1924 回维申斯卡亚专事写作、与 Maria 成婚 → 1926 《顿河故事》、始写《静静的顿河》 → 1928 前两卷出版、首现抄袭传闻 → 1929 《真理报》专门委员会认定其作者身份 → 1930 初见 Stalin → 1930s 多次致信 Stalin 陈述顿河集体农庄惨状（1931-01「情况是灾难性的」；1933-04-04 长信点名两名 OGPU 官员刑讯）→ 1932 入党 → 1932 《被开垦的处女地》第一部 → 1937 当选最高苏维埃；好友 Lugovoi 被捕、拒不出国声援、致信 Stalin 后 11-04 获释 → 1938 遭监视与叶若夫纠葛（10-23/10-31 两见 Stalin）→ 1939 科学院院士、六枚列宁勋章之始 → 1941 前线采访（与 Fadeyev 同行）、Stalin 奖 → 1942 母亲死于轰炸、《他们为祖国而战》 → 1956–57 《一个人的遭遇》 → 1959 陪同 Khrushchev 访欧美 → 1960 列宁奖 → 1961 苏共中央委员 → 1965-10 诺奖（奖金用于全家欧洲与日本自驾旅行）→ 1967/1980 两度社会主义劳动英雄 → 1969 后几乎搁笔 → 1972 批评 Yakovlev《反对非历史主义》致其去职 → 1984-02-21 逝于维申斯卡亚 → 1987 手稿数百页发现、1999 俄罗斯科学院认定作者身份、手稿入藏普希金之家。
- 授奖现场：1965 由苏联大使 Belokhvostikov 陪同出席（page.md 有照片说明）。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | epic novel | 史诗长篇 | 《静静的顿河》：诺奖理由核心「epic of the Don」 | 核心贡献页 |
| 1 | socialist realism | 社会主义现实主义 | 《被开垦的处女地》被誉典范 | 流派页 |
| 2 | Cossack literature | 哥萨克文学 | 顿河哥萨克生活与命运 | 题材页 |
| 3 | war prose | 战争文学 | 一战/内战/卫国战争书写与前线报道 | 战争页 |
| 4 | short story | 短篇小说 | 《顿河故事》《一个人的遭遇》 | 短篇页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Maria Petrovna Gromoslavskaia | 无向 | 1924 成婚，哥萨克阿塔曼之女，育二女二子，1984 年后与夫合葬 |
| controversy | Aleksandr Solzhenitsyn | 无向 | 1960s 其为《静静的顿河》抄袭论著名鼓吹者（或系报复肖洛霍夫对该书《伊凡·杰尼索维奇的一天》的尖锐批评）；客观并置 |
| colleague | Alexander Fadeyev | 无向 | 1941-09 东线前线同行记者；苏联作协体系内同侪（另有以其命名的 Fadeyev Medal 授予肖洛霍夫） |
| colleague | Nikita Khrushchev | 无向 | 1959 陪同其出访欧洲与美国 |

入库：`MySQL/seed_person.py data/Mikhail_Sholokhov.yaml`（幂等，QID 匹配）。

### 第 5 步：配色方案

- 主色：暗酒红 `#6E2B2B`（顿河落日与哥萨克披风）；辅助：诺奖香槟金 `C9A227`。
- badgeA 史诗长篇 — 深棕 `#5C3A1E`；badgeB 社会主义现实主义 — 钢灰红 `#8A4A3A`；badgeC 哥萨克文学 — 草原金 `#8F7420`；badgeD 战争文学 — 铁灰 `#4A4E54`。
- 背景母题：顿河水平线、草原地平线、马群剪影（低饱和，勿喧宾夺主）。

### 5.1 格式硬要求 【★ 必须满足】

1. 封面右上角肖像 + 细边框 + 姓名小字注；顶部/底部明示国籍（Soviet Union）。
2. **身份信息页**：封面之后、核心贡献之前，左头像右信息网格（生卒/全名/国籍变迁/「外来户」出身/妻子与子女/主要荣誉/核心领域）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。
4. 名句引文框替代公式框：1931-01 致 Stalin 信句 "Comrade Stalin, without exaggeration, conditions are catastrophic!"（page.md 有英文原文，作为史实引文框使用，注意语境说明）。

### 第 6 步：幻灯片序列（14 页）

```
00 OpenLiterature 项目首页（共享封面 \input）
01 封面 — 顿河的史诗 / Mikhail Sholokhov 1905–1984 + 四色 badge + 右上头像 + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 史诗长篇 / 社会主义现实主义 / 哥萨克题材 / 战争书写
04 顿河外来户之子（1905–1922）— inogorodnye 出身、13 岁参战、母亲的一生
05 莫斯科苦力与起步（1922–1926）— 码头工/石匠/会计、《考验》、《顿河故事》、成婚
06 《静静的顿河》专页 — 14 年四卷、葛利高里与阿克西妮亚、1957 电影（引文框）
07 抄袭公案（1928–1999）— 传闻、1929 委员会、Solzhenitsyn 质疑、Kjetsaa 统计分析、1999 定谳（客观并置）
08 《被开垦的处女地》专页 — 28 年两部、集体化题材、中译影响
1930s 直言 —— 致 Stalin 的信（引文框）、Lugovoi 获释、1938 监视风波（客观简述）
10 战争岁月（1941–1945）— 前线记者、母亲之死、《他们为祖国而战》
11 《一个人的遭遇》与战后 — 1956 短篇、Bondarchuk 电影、列宁奖
12 诺奖 1965 — 苏联官方口径、奖金用途、两度劳动英雄、六枚列宁勋章
13 晚年与遗产 — 维申斯卡亚隐居、1972 Yakovlev 事件（客观一句）、小行星 2448、博物馆保护区
14 结尾
```

### 第 7–8 步：Beamer 源码与布局检查

- 每页 `\newcommand{\xxxslide}` 定义；骨架复用 Kenneth_G_Wilson_zh.tex。
- 每写完一页 `latexmk -c` 清理后 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查

**Sholokhov 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生日期 | 公历 1905-05-24（儒略历 05-11），metadata 两值并存取 N.S. 并注 |
| 妻子生年 | Maria Gromoslavskaia 页内 1901 与 1902 两说（infobox 系 1901、葬段作 1902）——幻灯片写生年不注或加注两说，勿硬定 |
| 出身 | 「外来户」*inogorodnye* 而非哥萨克——这是其内战立场（支持红军）与《静静的顿河》视角的关键背景，勿写「哥萨克之子」 |
| 抄袭公案 | 1929 委员会认定、1984 Kjetsaa 统计支持、1987 手稿发现、1999 俄科院定谳——时间线须完整；Solzhenitsyn 系质疑方代表人物之一，双方观点客观并置不作裁决性措辞（页内 1999 结论可陈述） |
| 政治红线 | 与 Stalin/Khrushchev 的交往、大清洗中营救友人、1938 叶若夫夫妇纠葛、Sinyavsky-Daniel 审判言论：只按 page.md 客观简述事实，**不作政治评价、不展开政治叙事**；1938 窃听事件一笔带过或不入幻灯片 |
| 受害与受益并存 | 其信件救下 OGPU 官员与 Lugovoi（客观事实），同时其 Sinyavsky 言论致 Chukovskaya/Galanskov 公开信反对——两面都按事实写，勿单面化 |
| 奖金用途 | 诺奖奖金用于全家欧洲与日本自驾游、列宁勋章奖金建当地学校——两笔用途分开，勿混 |
| 电影改编 | 《静静的顿河》1957–58 Gerasimov、《一个人的遭遇》1959 Bondarchuk、《他们为祖国而战》1975——导演勿错配 |
| 未竟之作 | 《他们为祖国而战》为未完成小说；1942/1959 两个版本年代分开写 |
| 无载禁写 | 四名子女页内未具名，不建 parent-child；与 Stalin 仅为书信/会面关系，不建 influence；不编造与 Gorky/Sholokhov 同代作家的私交 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| And Quiet Flows the Don | 《静静的顿河》 | 又译《静静的顿河》四部曲；勿译「顿河静流」 |
| Virgin Soil Upturned | 《被开垦的处女地》 | 两部：《种子》《顿河收成》 |
| Tales from the Don | 《顿河故事》 | 1926 首部书 |
| Fate of a Man | 《一个人的遭遇》 | 又译《人的命运》 |
| Don Cossacks | 顿河哥萨克 | 题材主体 |
| inogorodnye | 外来户 | 关键出身背景 |
| stanitsa | 镇（哥萨克村镇） | Vyoshenskaya 维申斯卡亚 |
| socialist realism | 社会主义现实主义 | 流派口径 |
| ataman | 阿塔曼 | 哥萨克首领（岳父职衔） |
| Hero of Socialist Labour | 社会主义劳动英雄 | 1967/1980 两度 |
| epic of the Don | 顿河史诗 | 诺奖理由核心词 |

---

## 四、背景音乐建议

- **选定曲目**：**Nostalgia**（分批文件预分配）。
- **匹配理由**：怀旧/乡愁气质匹配顿河故土一生不离的写作姿态（几乎终身居维申斯卡亚）；舒缓的旋律贴合草原史诗的辽阔与苍凉，避开英雄颂歌式的浮夸。
- **备选**（未采用）：Through the Darkness（暗色调偏重但已被他人占用更多）、Timeless（沉稳但乡愁感弱）。
- **本地路径**：按 `music_audio/curated_tracks.md` 索引拷贝至 `presentations/20th_century/Mikhail_Sholokhov/Nostalgia.wav`。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Mikhail_Sholokhov/page.md` | 事实基准（唯一来源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录与中译理由 |
| `MySQL/data/Mikhail_Sholokhov.yaml` | 入库 yaml（本提示词第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
