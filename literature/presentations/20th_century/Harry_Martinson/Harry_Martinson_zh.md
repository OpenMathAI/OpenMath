# 文学家立传提示词（OpenLiterature 实例：Harry Martinson）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Harry Martinson（1974 诺贝尔文学奖，瑞典现代主义诗歌与太空史诗《阿尼阿拉》）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按文学家适配：无公式框——以名句引文框、代表作书影、意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Harry Martinson（哈里·马丁松），瑞典作家、诗人、前水手，1974 诺贝尔文学奖得主（与 Eyvind Johnson 共享）。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」骨架；本篇以「露珠映照宇宙」为核心视觉母题——一滴露水里折射整个宇宙，正是 Martinson 从自然细察到太空史诗的诗学轨迹。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Harry Edmund Martinson（1904-05-06 ~ 1978-02-11，享年 73 岁）
- **气质关键词**：**瑞典现代主义诗歌的革新者、无产阶级文学的代表、太空史诗的先知** —— 1974 诺贝尔文学奖获奖理由：
  > "for writings that catch the dewdrop and reflect the cosmos"（表彰其捕捉露珠而映照宇宙的写作）
- **设计母题**：**露珠与宇宙（dewdrop and cosmos）**。微观的露珠（精确观察的自然短诗）与浩瀚的宇宙（《阿尼阿拉》失航飞船）构成 Martinson 的两极诗学——视觉语言用「水滴中倒映星空」的嵌套意象。
- **本地数据源**：`literature/presentations/pages/20th_century/Harry_Martinson/page.md`（Wikipedia 全文 + frontmatter）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Harry_Martinson
- **肖像**：第 0 步待下载（Wikipedia infobox 照；404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，以正文为准）

- 生卒：1904-05-06 生于瑞典布莱金厄省耶姆舍格（Jämshög, Blekinge County）~ 1978-02-11 逝于斯德哥尔摩卡罗林斯卡大学医院，享年 73 岁
- 原名 Harry Edmund Olofsson；中产家庭经营小店，六兄妹（四姐两妹/排行第五）
- 父 1910 死于肺结核；母 1911 移民美国俄勒冈州波特兰弃子女而去；此后作为市政寄养儿童（Kommunalbarn）辗转乡下
- 16 岁出走哥德堡当水手；流浪 18 个月至 Umeå、特罗姆瑟；1921 卢德流浪被捕；1922 司炉，先后随船到法国、爱尔兰、苏格兰、美国、巴西、开普敦、孟买
- 1927-05-23 岁生日因肺病在瑞典上岸，开始文学生涯
- 1929 与无产阶级小说家 Moa Martinson 结婚（经斯德哥尔摩无政府主义报纸 Brand 相识；1934 同游苏联；1940 因政治分歧离婚）；1942 娶 Ingrid Lindcrantz（1916–1994）
- 教育：无正规高等教育，完全靠流浪与阅读自学
- 文学师承与影响（page.md 明载）：经 Artur Lundkvist 引入现代主义诗人 Elmer Diktonius、Carl Sandburg、Edgar Lee Masters；Passad（1945）受中国诗歌影响
- 1949 当选瑞典学院院士——首位无产阶级作家入选
- 关键荣誉：Nobel 1974（共享）、Dobloug Prize、Samfundet De Nio's Grand Prize、Bellman Prize、Sveriges Radio's Poetry Prize
- 核心作品：诗集《Spökskepp》(1929)、《Nomad》(1931)、《Passad》(1945)、《Cikada》(1953)、《Aniara》(1956)；小说《Kap farväl!》(1933)、《Nässlorna blomma / Flowering Nettle》(1935)、《Vägen ut》(1936)、《Vägen till Klockrike / The Road》(1948)；剧作《Tre knivar från Wei》(1964)
- 关键时间线（15 节点）：1910 丧父 → 1911 母移民 → 1920 出走当水手 → 1921 流浪被捕 → 1922 司炉远航 → 1927 上岸开始写作 → 1929 《Spökskepp》+《Fem unga》+ 与 Moa 结婚 → 1931 《Nomad》突破 → 1933 《Kap farväl!》→ 1935 《Flowering Nettle》→ 1937–1939 自然随笔三部曲 → 1939–40 芬兰冬季战争志愿者 → 1945 《Passad》→ 1949 入瑞典学院 → 1956 《Aniara》→ 1959 Blomdahl 歌剧版 → 1964 Bergman 执导《Tre knivar från Wei》→ 1971 复出诗集 → 1974 诺贝尔奖 → 1978-02-11 自杀辞世

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Harry_Martinson/` 与 `images/`

### 第 2 步：复制 Makefile

- 复制同世纪已立传者目录的 Makefile，设置 `MAIN=Harry_Martinson_zh`、`VIDEO_NAME=Harry_Martinson_zh`

### 第 3 步：收集图片

- 肖像下载（curl -A "Mozilla/5.0" + file 验证）；404 则用装饰圆占位；另备《Aniara》书影/歌剧海报插图

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist poetry | 现代主义诗歌 | 《Fem unga》(1929) 引入瑞典文学现代主义；《Nomad》突破 | 文坛页 |
| 1 | proletarian literature | 无产阶级文学 | 首位入选瑞典学院的无产阶级作家（1949） | 成名页 |
| 2 | science fiction | 科幻诗剧 | 《Aniara》太空史诗，1959 歌剧化 | 核心页 |
| 3 | nature writing | 自然书写 | 自然随笔三部曲（1937–1939）与精确观察短诗 | 自然页 |
| 4 | autobiographical novel | 自传性小说 | 《Flowering Nettle》写寄养童年 | 小说页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Moa Martinson | 无向 | 1929–1940，无产阶级小说家，经报纸 Brand 相识，1940 因其批评他缺乏政治承诺离婚 |
| co-honored | Eyvind Johnson | 无向 | 1974 诺贝尔文学奖共享，两位瑞典学院院士同时获奖引发争议 |
| influence | Elmer Diktonius | 无向 | 经 Lundkvist 引入的现代主义诗人 |
| influence | Carl Sandburg | 无向 | 经 Lundkvist 引入的美国现代主义诗人 |
| influence | Edgar Lee Masters | 无向 | 经 Lundkvist 引入的美国诗人 |
| colleague | Artur Lundkvist | 无向 | 引路人与《Fem unga》(1929) 同人 |
| colleague | Gustav Sandgren | 无向 | 《Fem unga》(1929) 五人同人 |
| colleague | Erik Asklund | 无向 | 《Fem unga》(1929) 五人同人 |
| colleague | Josef Kjellgren | 无向 | 《Fem unga》(1929) 五人同人 |
| colleague | Karl-Birger Blomdahl | 无向 | 《Aniara》歌剧作曲家（1959，与 Erik Lindegren 合作台本） |
| colleague | Ingmar Bergman | 无向 | 1964 皇家剧院执导其剧作《Tre knivar från Wei》 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：波罗的海的青蓝、露水的清澈、太空的深邃
- **主色**：深海蓝 `#17435B`（预分配）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgePoem` 现代主义诗 — 靛蓝 `#4C5FD5`
  - `badgeSea` 航海岁月 — 青绿 `#0E7C7B`
  - `badgeNature` 自然书写 — 琥珀 `#E07B30`
  - `badgeAniara` 太空史诗 — 玫瑰 `#C4204F`
- **背景母题**：稀疏水滴圆斑（大小错落），呼应「露珠映照宇宙」

### 第 6 步：规划幻灯片序列（12–15 页）

```
00  OpenLiterature 项目首页（\input cover 共享页）
01  封面 — 捕捉露珠映照宇宙 / Harry Martinson 1904–1978 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、原名、国籍、出生地、婚姻、瑞典学院、核心领域）
03  文学世界概览 — 现代主义诗歌 / 无产阶级文学 / 自然书写 / 太空史诗
04  苦难童年（1904–1920）— 丧父、母弃养、寄养岁月 → 《Flowering Nettle》
05  水手与流浪汉（1920–1927）— 哥德堡出海、流浪、司炉远航全球
06  登上文坛（1929–1933）— 《Fem unga》《Spökskepp》《Nomad》
07  无产阶级小说家（1935–1936）— 《Flowering Nettle》《Vägen ut》
08  自然三部曲与冬季战争（1937–1941）— 随笔三部曲、《Verklighet till döds》
09  成熟与登堂（1945–1949）— 《Passad》中国诗风、《The Road》、1949 瑞典学院
10  《Aniara》：太空史诗（1953–1959）— 失航飞船、Blomdahl 歌剧、2018 电影
11  沉默与复出（1960–1973）— 《Vagnen》受挫宣布封笔、Bergman 执导、1971 复出
12  1974 诺贝尔奖与争议 — 学院自颁争议、Martinson 的敏感与痛苦
13  遗产 — Cikada Prize、瑞典诗篇集、百年纪念
14  结尾
```

### 第 7 步：编写 Beamer 源码

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照成品 `\profileslide`。
- 公式框以名句引文框替代：封底可引获奖理由原句 "for writings that catch the dewdrop and reflect the cosmos"（page.md 明载英文原文）。

### 第 8 步：布局检查

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删装饰 → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查

**Martinson 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日 | page.md 正文 1904-05-06（frontmatter 另有 1904-01-01 噪声值），以 05-06 为准 |
| 诺贝尔奖共享 | 1974 与 Eyvind Johnson 共享；两位都是瑞典学院院士，媒体抨击「学院自颁」——客观陈述，不展开评价 |
| 自杀描述 | 1978-02-11 于卡罗林斯卡医院用剪刀自戕（"hara-kiri-like manner"），如实简述、不作渲染 |
| 中国诗歌影响 | 《Passad》明载受 Chinese poetry 影响，勿写成「中国之旅」——他从未去中国 |
| 剧作背景 | 《Tre knivar från Wei》以 7 世纪中国为背景，Bergman 执导于皇家剧院（1964），勿与歌剧《Aniara》混淆 |
| Aniara 前身 | 先有 1953《Cikada》末章 "Sången om Doris och Mima"，后扩展为 1956《Aniara》，顺序勿倒 |
| 第一部英译 | 《Kap farväl!》→ Cape Farewell（1934）是首部译英著作 |
| 政治经历 | 1934 与 Moa 访苏联、1939–40 芬兰冬季战争志愿者（Salla 前线 9 天传令兵）只按 page.md 客观简述 |
| 无载禁写 | 与 Tranströmer/Ekelöf 无师承关系（仅同见于 Bly 1975 译集《Friends, you drank some darkness》）；勿编造弟子 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Aniara | 《阿尼阿拉》 | 太空史诗诗剧，勿译作「安妮亚拉」小说 |
| proletarian writers | 无产阶级作家 | 瑞典文学史流派标签，非政治身份 |
| Fem unga | 《五个青年》 | 1929 五人诗选，瑞典现代主义起点 |
| Swedish Academy | 瑞典学院 | 诺奖颁授机构，1949 入选 |
| Kommunalbarn | 市政寄养儿童 | 自传小说核心经验 |
| trade wind | 信风 | 《Passad》书名本义 |
| senhal | （不用） | 本篇无此概念 |

---

## 四、背景音乐选择

- **选定曲目**: **New Lands** — Alex-Productions（152k views，曲库最高受众）
- **风格**: 高受众 / 史诗 / 开阔
- **匹配理由**:
  - "史诗/开阔" 匹配《Aniara》的太空史诗气质——失航飞船漂向无垠宇宙，是瑞典诗中最开阔的意象
  - "高受众" 匹配 Martinson 在瑞典的国宝地位——生辰纪念碑、诗篇集收录、百年纪念
  - 波澜壮阔的开阔感也契合水手岁月的远洋叙事（哥德堡—里约—开普敦—孟买）
- **备选**（未采用）: SEA（流动/平稳，匹配水手但史诗感不足）、The Flow of Time（时间感，偏沉思）
- **时长**: 需 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
