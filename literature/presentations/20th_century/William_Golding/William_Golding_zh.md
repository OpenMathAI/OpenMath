# 文学家立传提示词（OpenLiterature：William Golding）

> **本文件是 OpenLiterature 的人物专属立传提示词**，以 Kenneth G. Wilson（OpenPhysicist 模板标杆）为骨架，适配文学家。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Golding 定制内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合 OpenPhysicist 标杆（Kenneth G. Wilson 提示词 + tex 结构）与文学家侧实战经验。
- **本实例**：William Golding（威廉·戈尔丁），1983 诺贝尔文学奖得主，《蝇王》的作者，人性幽暗面的寓言家。
- **设计哲学**：文学家立传**没有公式框——以代表作书影 / 名句引文框 / 意象图式替代**；仍须保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Sir William Gerald Golding（1911-09-19 ~ 1993-06-19，享年 81 岁）
- **气质关键词**：**人性暗面的解剖者、古典学与海洋的寓言家、康沃尔的凯尔特之子** —— 1983 诺贝尔文学奖获奖理由：
  > "for his novels, which with the perspicuity of realistic narrative art and the diversity and universality of myth, illuminate the human condition in the world of today"
  > （表彰其小说，以现实主义叙事艺术的明晰与神话的多样性及普遍性，照亮了当今世界中的人类境况）
- **设计母题**：**海岛与深渊（island and darkness）**。《蝇王》的荒岛、贝壳与猪头、《塔尖》的螺旋石塔、海三部曲的帆船——版式语言宜用深色海水色块、海岛剪影、贝壳与苍蝇王的暗红意象，明暗对比强烈。
- **本地数据源**：`literature/presentations/pages/20th_century/William_Golding/page.md` + 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/William_Golding （肖像第 0 步标「待下载」，infobox 有 1983 年照）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面四件套已下载
- 肖像：**待下载**（infobox 照片 "Golding in 1983"；404 回退 Commons Special:FilePath / REST API，再失败装饰圆占位）
- **事实基准（正文优先）**：
  - 生卒：1911-09-19 生于康沃尔纽基（Newquay）外祖母家（Karenza，康沃尔语「爱」）~ 1993-06-19 逝于康沃尔 Perranarworthal（心力衰竭），享年 81 岁；葬于威尔特郡 Bowerchalke 教区教堂墓地
  - 家庭：父 Alec Golding（马尔堡文法学校理科教师，1905–退休）；母 Mildred（Curnoe，康沃尔人，女性选举权运动者，被其称为「迷信的凯尔特人」——讲康沃尔鬼故事）；兄 Joseph
  - 婚姻：曾与 Mollie Evans 订婚后解除；**1939-09-30 与分析化学家 Ann Brookfield 成婚**；子 David（1940-09 生）、女 Judith（1945-07 生，后为 Judy Carver，整理出版父亲研究材料）；远房表亲 Simon William Golding 亦为小说家/编剧
  - 教育：马尔堡文法学校 → 1930 入牛津 Brasenose College，**先读两年自然科学后转英语文学**（首任导师为化学家 Thomas Taylor）；1934 夏获二等荣誉 BA；同年诗集《Poems》经牛津友人、人智学者 Adam Bittleston 协助由 Macmillan 出版
  - 教师生涯：1935–37 伦敦 Streatham 的 Steiner-Waldorf 学校 Michael Hall 教英语 → 牛津一年教育文凭 → 1938–40 Maidstone 文法学校（英语+音乐）→ 1940-04 起 Bishop Wordsworth's School（索尔兹伯里，教英语/哲学/希腊语/戏剧），战后返校至 1961 年辞职专事写作
  - 早年污点与「危机」：青少年时期一次对少女未遂性侵的自述（私人日志，2009 Carey 传记披露）；终生与酗酒挣扎（「the old, old anodyne」）；1963 希腊写作《塔尖》期间的豪饮；1967《金字塔》后严重写作停滞（家庭焦虑+失眠+沮丧），十二年无小说；靠研读荣格著作走出危机——自称「admission of discipleship」，1971 年赴瑞士亲访荣格足迹；1971 起记梦日记 22 年直至去世前夜（约 240 万词）；1979《可见的黑暗》复出
  - 军旅：1940-12-18 入皇家海军（HMS Raleigh 报到）；驱逐舰参与追击击沉「俾斯麦号」；诺曼底 D-Day 指挥火箭登陆艇向滩头齐射；1944 年 10–11 月瓦尔赫伦岛战役（27 艘突击艇沉 10 艘）；升至少尉军衔（lieutenant）
  - 写作突破：1951 年在 Bishop Wordsworth's 执教时写下手稿《Strangers from Within》；1953 年 9 月投稿 Faber and Faber——初审读者 Jan Perkins 批「Rubbish & dull. Pointless」，新编辑 **Charles Monteith** 力挺并促修改，1954-09 以《蝇王》（Lord of the Flies）出版；此前已被七家出版社拒绝
  - 写作两大影响（George 论）：一是战争与海军服役，二是学习古希腊语
  - 盖亚假说：1958 年迁 Bowerchalke 后与同村散步伙伴 **James Lovelock** 讨论，Golding 建议以其设想中之地球生命体假说借用希腊神话大地之母命名为「盖亚假说」（Gaia hypothesis）；学者 Mantion 论证他更是该假说最早的文学鼓吹者（"Gaia Lives, OK?" 1976、"The Earth's Revenge" 1990）
  - 1961–62 美国 Hollins College 驻校作家
  - 关键荣誉：James Tait Black 纪念奖 1979（Darkness Visible）· 布克奖 1980（Rites of Passage）· **Nobel 1983**（据 ODNB 是「意外甚至有争议的选择」）· CBE（1966 元旦授勋）· 下级勋位爵士（Knight Bachelor，1988 生日授勋）· 皇家文学学会会士 FRSL · 巴黎第三大学荣誉博士；2008《泰晤士报》「1945 年以来 50 位最伟大的英国作家」第 3 位
  - 核心作品（5–6 条）：《蝇王》（1954，男孩荒岛堕落寓言；1963/1990 两次拍片）；《继承者》（1955，尼安德特人遇见智人）；《品彻·马丁》（1956，溺水水手的临终之思）；《自由堕落》（1959，自由意志之问）；《塔尖》（1964，中世纪大教堂不可能之塔尖，通常认为原型索尔兹伯里大教堂）；海三部曲《航向极限》：Rites of Passage（1980，布克奖）+ Close Quarters（1987）+ Fire Down Below（1989）；遗作《双舌》（The Double Tongue，德尔斐题材，1995 年身后出版）
  - 关键时间线（17 节点）：1911 生于纽基 → 1930 入牛津（自然科学两年→英语两年）→ 1934 BA·诗集出版 → 1935–38 Steiner 学校与教育文凭 → 1939 与 Ann Brookfield 成婚 → 1940 入皇家海军 → 1941 参与追击「俾斯麦号」 → 1944 D-Day 火箭艇·瓦尔赫伦 → 1945 复教职 → 1951 动笔《Strangers from Within》 → 1954《蝇王》出版 → 1955《继承者》→ 1958 迁 Bowerchalke·识 Lovelock → 1961 辞教·Hollins 驻校 → 1964《塔尖》→ 1966 CBE → 1967–79 写作停滞与荣格疗愈·梦日记 → 1979《可见的黑暗》·James Tait Black 奖 → 1980《航程祭礼》布克奖 → 1983 诺贝尔奖 → 1985 迁康沃尔 Tullimaar → 1988 授爵 → 1993-06-19 逝于康沃尔

### 第 1 步：建立目录 【模板通用】

- 已在 `literature/presentations/20th_century/William_Golding/`（本提示词所在目录）

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=William_Golding_zh`、`VIDEO_NAME=William_Golding_zh`

### 第 3 步：收集图片 【人物专属】

- 下载肖像到 `images/Golding.jpg`（infobox 1983 年照），`curl -A "Mozilla/5.0"` + `file` 验证；失败装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Golding 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | allegorical fiction | 寓言小说 | 《蝇王》——文明表皮下的野性 | 封面、核心页 |
| 1 | survivalist fiction | 荒岛求生小说 | robinsonade 传统，《蝇王》反其道而行 | 核心页 |
| 2 | sea story | 海洋小说 | 海三部曲 To the Ends of the Earth（布克奖） | 三部曲页 |
| 3 | historical fiction | 历史小说 | 《塔尖》《继承者》《双舌》的历史与史前题材 | 主题页 |
| 4 | poetry | 诗歌 | 1934 年首部出版物即诗集《Poems》 | 早年页 |

#### 4.1 入库操作

- `python3 seed_person.py data/William_Golding.yaml`（幂等；主记录 `primary_occupation='writer'`、`has_social_data=1`）
- 职业关联：writer（rank 0）、novelist（rank 1）、playwright（rank 2）
- 校验 person_field / person_relation 计数

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Carl Jung | 单向 | 研读荣格著作走出酗酒危机，自称「admission of discipleship」，1971 年赴瑞士寻访其足迹 |
| colleague | James Lovelock | 无向 | Bowerchalke 同村散步伙伴；建议其地球生命体假说命名「盖亚假说」 |
| colleague | Charles Monteith | 无向 | Faber and Faber 编辑，力排初审否定促成《蝇王》1954 年出版 |
| colleague | Adam Bittleston | 无向 | 牛津友人（人智学者），协助 1934 年诗集《Poems》出版 |
| spouse | Ann Brookfield | 无向 | 1939-09-30 成婚，分析化学家 |
| parent-child | David Golding | — | 子（1940-09 生） |
| parent-child | Judith Golding | — | 女（1945-07 生），整理出版其研究材料 |

> **不入库说明**：Mollie Evans（解除的婚约）、John Carey（传记作者，获准查阅未刊文件，非生前交游）、Jean-Paul Sartre/Artur Lundkvist（仅 1963 列宁格勒作家大会合影）、Nigel Williams（舞台改编者）、Thomas Taylor（牛津首任导师，教学关系且非文学师承）、Simon William Golding（远房表亲）均不入库。

#### 4.5.1 入库操作

- 以 `name_en='William Golding'`（Q44183）为中心写入 `person_relation`（库内此前无该人记录，本次新建）
- Jung 沿用库内既有记录 'Carl Jung'（id=1105）；其余自动建 stub
- parent-child 不写 direction；influence 用 note 注明影响方向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深色海水、文明与野蛮的明暗交界、古典寓言
- **配色**：暗酒红（主色 `#6E2B2B`）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeIsland` 荒岛与《蝇王》— 深海蓝绿 `#0E4D64`
  - `badgeSea` 海三部曲 — 海军蓝 `#1F3A5F`
  - `badgeSpire` 《塔尖》与古典 — 石灰金 `#9A8B4F`
  - `badgeCrisis` 危机与荣格 — 暗紫 `#46356B`
- **背景母题**：海岛剪影、贝壳与暗红太阳、石塔螺旋线条；明暗对比强烈

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + 细边框 + 姓名小字注（Sir William Golding）。
2. 封面明示国籍（United Kingdom）；底部状态栏 `国籍 | 语言 | 主要奖项`。
3. **必须有身份信息页**：左头像 + 右信息网格（生卒、教育、军旅、教职、荣誉、核心领域）。
4. **无公式框**：用《蝇王》书影 / 海岛意象图式 / 盖亚假说手迹语境替代。
5. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页
01  封面 — 人性暗面的寓言家 / William Golding 1911–1993 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含自然科学转英语、海军、教职、荣誉）
03  核心贡献概览 — 《蝇王》/ 寓言与神话 / 海三部曲 / 盖亚假说之缘
04  康沃尔童年 (1911–1930) — Karenza、理科教师之子、「迷信的凯尔特人」母亲
05  牛津与教师岁月 (1930–1940) — 自然科学转英语、诗集 1934、三校执教
06  海军军官 (1940–1945) — 俾斯麦号、D-Day 火箭艇、瓦尔赫伦
07  《蝇王》(1954)（核心页·书影）— 七次退稿与 Monteith、课堂两群对垒的素材
08  五十年代五连发 — 《继承者》《品彻·马丁》《自由堕落》《塔尖》
09  危机与荣格 (1967–1979) — 酗酒与写作停滞、admission of discipleship、梦日记
10  复出与海三部曲 — Darkness Visible 1979 · Rites of Passage 布克奖 1980
11  盖亚假说 — 与 Lovelock 的同村散步、命名的由来、文学鼓吹
12  荣誉与认可 — Nobel 1983（有争议的选择）· 布克奖 1980 · CBE 1966 · 爵士 1988
13  康沃尔晚境与身后 — Tullimaar、1993 辞世、《双舌》1995
14  遗产：神话的多样性与普遍性
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；宏名禁数字；`\foreach` 分隔符 ASCII 逗号。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；单遍取日志后须重新 `make pdf`。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Golding 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 牛津专业 | **自然科学两年 → 英语文学两年**（首任导师化学家 Thomas Taylor）——勿写成一路英语文学 |
| 《蝇王》出版史 | 手稿原名 Strangers from Within；被七家出版社拒；Faber 初审读者批「Rubbish & dull. Pointless」，编辑 Charles Monteith 力挺——三个环节勿混 |
| 课堂素材 | 日志载其把学生分成两群互斗的实验，是《蝇王》素材之一；勿写成「亲历海难」 |
| 盖亚假说 | Golding 是**命名建议者**（Gaia），Lovelock 是提出者；Mantion 论证他还做了文学鼓吹——勿写成「共同提出」 |
| 军衔 | 升至 lieutenant（海军中尉/少尉），勿写成上尉以上 |
| 布克奖 | 1980 年 Rites of Passage；CBE 1966 元旦授勋、爵位 1988 生日授勋——年份勿错位 |
| 诺贝尔争议 | ODNB 称 1983 得主是「unexpected and even contentious choice」——如实呈现争议评价，不裁断 |
| 未遂性侵自述 | 出自其私人日志、2009 年 Carey 传记披露——提示词与正文均客观一句带过，不渲染细节 |
| 酗酒叙事 | 「crisis」是本人自述用语；1967–1979 十二年无小说是事实；荣格疗愈与「admission of discipleship」有明载 |
| 女儿名字 | Judith（Judy Carver）——Carver 是婚后姓，写关系表用 Judith Golding |
| 遗作 | The Double Tongue 1995 年身后出版（1996 Faber 再版），德尔斐题材 |
| 同名区分 | 马尔堡文法学校（Marlborough Grammar School，父亲任教）≠ 马尔堡公学（Marlborough College）——page.md 注 8 明示勿混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Lord of the Flies | 《蝇王》 | 通行译名；别称《苍蝇王》 |
| robinsonade | 鲁滨逊式题材 | 荒岛漂流文学传统，《蝇王》是反转 |
| allegory | 寓言 | 人物与情节承载抽象观念 |
| Rites of Passage | 《航程祭礼》 | 海三部曲首卷，布克奖；通行一作《过界的仪式》 |
| The Spire | 《塔尖》 | 原型通常认为索尔兹伯里大教堂 |
| Darkness Visible | 《可见的黑暗》 | 典出《失乐园》 |
| Gaia hypothesis | 盖亚假说 | Lovelock 提出、Golding 命名 |
| admission of discipleship | 「自认门徒」 | 其对研读荣格的自述 |
| Knight Bachelor | 下级勋位爵士 | 1988 生日授勋，称 Sir |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions
- **风格**: 原始张力 / 暗色 / 冲击感
- **匹配理由**:
  - "原始张力" 直接对应《蝇王》主题——文明少年在荒岛上坠回野性
  - "暗色" 匹配其作品的明暗对照与「人性暗面解剖者」的气质
  - 冲击感呼应战时经历（D-Day 火箭艇）与寓言叙事的紧迫
- **本地路径**: `music_audio/alex-productions/` 下 Savage 曲目 → `presentations/20th_century/William_Golding/Savage.wav`
- **时长**: 以实际曲目为准，`ffmpeg -shortest` 自动对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；盖亚假说只写「命名建议者」。**
