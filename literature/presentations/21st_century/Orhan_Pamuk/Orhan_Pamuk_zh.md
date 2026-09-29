# 文学家立传提示词（Orhan Pamuk · 2006 诺贝尔文学奖）

> **本文件是 OpenLiterature 21 世纪批次的「人物专属立传提示词」**，目标人物 Orhan Pamuk（奥尔罕·帕慕克）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–9 步骨架），内容适配文学家：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Ferit Orhan Pamuk（奥尔罕·帕慕克），2006 年诺贝尔文学奖得主，**首位土耳其诺奖得主**（page.md 明载）。
- **设计哲学**：文学家立传与物理学家立传的核心差异，在于以「作品与意象」代替「定理与公式」——身份信息页（★ 必做）与文学领域结构化表达两点保留，公式框一律换成**名句引文框**。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Orhan Pamuk（1952-06-07 生于伊斯坦布尔，在世）
- **气质关键词**：**呼愁的书写者、东西方的摆渡人、细密画与雪的调色师** —— 2006 年获奖理由（官方 EN 原文，禁止改写）：
  > "who in the quest for the melancholic soul of his native city has discovered new symbols for the clash and interlacing of cultures"（表彰其在探寻故乡城市忧郁灵魂的途中，为文化的冲突与交织发现了新的象征）
- **设计母题**：**呼愁（hüzün）——伊斯坦布尔的集体忧郁**。以深蓝主色 + 博斯普鲁斯雾灰色调承载「黑书」「雪」「纯真博物馆」三重意象：雪（白/冷）、红（细密画之红）、雾（灰色调）为三辅助意象，呼应其作品色谱。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/Orhan_Pamuk/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **参考模板**：
  - 提示词母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`）
  - yaml 母本：`MySQL/data/Kenneth_G_Wilson.yaml`

---

## 三、任务流程 【逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Orhan_Pamuk` 四件套到 `literature/presentations/pages/21st_century/Orhan_Pamuk/`（事实基准如下）：
  - 生卒（1952-06-07 生于伊斯坦布尔，在世）；国籍（土耳其）
  - 家庭：兄 Şevket Pamuk（博阿齐奇大学奥斯曼经济史教授，常以虚构角色出现在其作品中）；同父异母妹 Hümeyra Pamuk（记者）；祖母为切尔卡西亚人
  - 教育：Robert College 中学 → 伊斯坦布尔技术大学建筑系（三年后辍学转向写作）→ 伊斯坦布尔大学新闻学院 1976 毕业；自称「文化穆斯林」
  - 婚姻：1982-03-01 娶历史学家 Aylin Türegün（2002 离婚）；女儿 Rüya 1991 年生（土耳其语意为「梦」）；2022 娶 Aslı Akyavaş
  - 任职：哥伦比亚大学 Robert Yik-Fong Tam 人文讲席教授（写作与比较文学）；1985–88 以陪读学者身份在哥大 Butler Library 写《黑书》；爱荷华大学国际写作计划访问学人；2009 哈佛 Charles Eliot Norton 讲座「天真与感伤的小说家」；2018 当选美国哲学会
  - 核心作品：《杰夫代特先生》(1982)、《寂静的房子》(1983)、《白色城堡》(1985)、《黑书》(1990)、《新人生》(1994)、《我的名字叫红》(1998)、《雪》(2002)、《纯真博物馆》(2008)、《我脑袋里的怪东西》(2015)、《红发女人》(2017)、《瘟疫之夜》(2021)
  - 关键荣誉：2003 都柏林国际文学奖（《我的名字叫红》，与译者共同）、2005 德国书业和平奖 + Prix Médicis étranger、**2006 诺贝尔文学奖**、2006 法兰西艺术与文学勋章司令级、2012 松宁奖 + 荣誉军团勋章军官级；全球销量逾 1300 万册、63 种语言，土耳其最畅销作家
  - 关键时间线（15–20 节点）：1974 开始写作 → 1979 Milliyet 竞赛并列首奖 → 1982 首部长篇出版 → 1983 Orhan Kemal 奖 → 1985《白色城堡》→ 1990《黑书》+ 独立外国小说奖 → 1994《新人生》土耳其史上最快畅销 → 1995 因批评库尔德人待遇受审 → 1998《我的名字叫红》→ 2002《雪》→ 2003 都柏林奖 → 2005 被诉 → 2006-01 撤诉 → 2006-10-12 诺奖 → 2008《纯真博物馆》→ 2011 判赔 6000 里拉 → 2019「Balkon」摄影展 → 2026 Netflix 剧集

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Orhan_Pamuk/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已立传目录的 `Makefile`，设置 `MAIN=Orhan_Pamuk_zh`、`VIDEO_NAME=Orhan_Pamuk_zh`

### 第 3 步：收集图片 【人物专属】

- 从 `images.txt` 取 infobox 肖像（`Orhan_Pamuk.jpg`，250px 改 500px 下载，`curl -A "Mozilla/5.0"` + `file` 验证）；404 时用 Commons `Special:FilePath/Orhan_Pamuk.jpg?width=600`；再失败用装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | postmodern novel | 后现代小说 | 互文性、元小说与多声部叙事 | 核心页 |
| 1 | east-west cultural identity | 东西方文化认同 | 传统/现代、世俗/信仰的张力 | 主题页 |
| 2 | historical fiction | 历史小说 | 《我的名字叫红》1591 奥斯曼画坊 | 作品页 |
| 3 | memoir | 回忆录与非虚构 | 《伊斯坦布尔》《父亲的手提箱》 | 非虚构页 |
| 4 | screenwriting | 电影编剧 | 《秘密脸》剧本（据《黑书》） | 侧翼页 |

#### 4.1 入库操作（`MySQL/seed_person.py data/Orhan_Pamuk.yaml`）

- 新建/更新 `people` 主记录（`name_en='Orhan Pamuk'`，`qid='Q241248'`），设置 `primary_occupation='writer'`、`has_biography: false`、`has_social_data=1`
- 关联职业 `writer`（rank 0）+ `novelist`/`essayist`；国籍 `Turkey`
- 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | José Saramago | 无向 | 欧洲作家议会由帕慕克与其联合提议；2005-12 八作家联署声援 |
| colleague | Gabriel García Márquez | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | Günter Grass | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | Umberto Eco | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | Carlos Fuentes | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | Juan Goytisolo | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | John Updike | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | Mario Vargas Llosa | 无向 | 2005-12 八作家联署声援帕慕克审判 |
| colleague | Mehmet Eroğlu | 无向 | 1979 Milliyet 报长篇小说竞赛共同首奖 |
| colleague | Erdağ M. Göknar | 无向 | 《我的名字叫红》英译者，2003 都柏林奖共同获得 |
| colleague | Maureen Freely | 无向 | 《雪》《纯真博物馆》等多部作品英译者 |
| colleague | Ömer Kavur | 无向 | 《秘密脸》导演，剧本由帕慕克据《黑书》撰写 |
| spouse | Aylin Türegün | 无向 | 历史学家，1982-03-01 结婚，2002 离婚 |
| spouse | Aslı Akyavaş | 无向 | 2022 结婚 |
| parent-child | Rüya Pamuk | 无向 | 女儿（1991 年生），名意为「梦」，《我的名字叫红》献给她 |

#### 4.5.1 入库操作

- 以 `name_en='Orhan Pamuk'` 为中心写入 `person_relation`；对手方库内已有规范记录（José Saramago / Gabriel García Márquez / Günter Grass / Carlos Fuentes / Mario Vargas Llosa 均已存在，勿另建别名）；其余建 stub（`has_biography=0`，不编造 qid），note 加 `[材料待展开] ` 前缀

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：忧郁、雾中城邦、细密画的浓烈与雪的克制
- **配色**：主色深蓝 `#2A4B7C`（预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 后现代小说 — 细密画红 `#A31621`
  - `badgeB` 东西方认同 — 博斯普鲁斯青 `#1B6B8C`
  - `badgeC` 历史小说 — 雪灰 `#5E6B73`
  - `badgeD` 非虚构/编剧 — 暖赭 `#B07A2A`
- **背景母题**：细雪与雾——大块柔和圆斑如雪片飘落，右下角一枚红色小圆（细密画之红）点睛

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（右上角 + `draw=coveraccent!50` 细边框）与国籍行（`土耳其 | 伊斯坦布尔 | 哥伦比亚大学`）。
2. **身份信息页 ★ 必做**：左肖像 + 右信息网格（生卒、国籍、教育、任职、婚姻、核心作品、主要荣誉）。
3. 引号用半角 `" "`；结尾页品牌统一 `OpenMathAI`。
4. 引文框内容只用 page.md 载英文原文（如 "A new star has risen in the east—Orhan Pamuk."、inner music 段），禁止杜撰「中文原话」。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 呼愁的书写者 / Orhan Pamuk 1952– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）
03  核心作品概览 — 红书 / 雪 / 纯真博物馆 / 黑书
04  尼尚塔什的童年 (1952–1976) — 富裕而没落的中产家族、建筑系辍学、新闻学院
05  从建筑到写作 (1974–1985) — Milliyet 并列首奖、Cevdet Bey、白色城堡
06  《黑书》与后现代转向 (1990) — 哥大 Butler Library 写作岁月
07  《我的名字叫红》核心页（引文框 + 1591 画坊意象图式）
08  《雪》与卡尔斯 (2002) — 伊斯兰主义与西方主义的冲突、NYT 十佳
09  审判风波 (2005–2011) — Article 301、八作家联署、撤诉与判赔（只客观陈述）
10  2006 诺贝尔文学奖 — 官方理由 EN 原文 + 中译、首位土耳其得主
11  《纯真博物馆》 — 小说与实体博物馆、小说—物件互文
12  讲席与写作课 — 哥大 Tam 讲席、诺顿讲座《天真与感伤的小说家》
13  荣誉与认可 — 都柏林 2003 · 德国书业和平奖 2005 · 松宁奖 2012 · 荣誉军团勋章
14  遗产：呼愁与伊斯坦布尔 — 摄影展 Balkon、Netflix 剧集、63 种语言
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；文学领域页用表格 + 意象色块替代公式框

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Pamuk 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "who in the quest for the melancholic soul…" 禁止改写；中译用名录版「为文化的冲突与交织发现了新的象征」 |
| 首位 | 首位土耳其诺奖得主（page.md 明载），可写 |
| 审判结局 | 2005 被诉 → 2006-01-22 撤诉（司法部拒批）→ 2011-03-27 判令赔付 6000 里拉；不得写成「无罪释放」 |
| 八作家联署 | 2005-12-13 联署 8 人名单（Saramago/García Márquez/Grass/Eco/Fuentes/Goytisolo/Updike/Vargas Llosa）须与关系表一致，勿增删 |
| 恋情 | Kiran Desai 恋情仅叙述；Karolin Fişekçi 指控已被帕慕克明确否认——两者均不建关系、不写成事实 |
| 《雪》年份 | 土耳其语 2002 出版，英译 2004；NYT 十佳针对 2004 英译本 |
| 都柏林奖 | 2003 年获，与译者 Erdağ M. Göknar 共同；勿写成个人独得 |
| 教育 | 建筑系辍学 + 新闻学院毕业；勿写「文学科班出身」 |
| 政治内容 | 亚美尼亚/库尔德议题与言论自由争议只按 page.md 客观简述，不作政治评价、不展开叙事 |
| 荣誉博士 | 16 所荣誉博士（柏林自由/耶鲁/圣彼得堡国立等）取 3–4 所列示，勿全列致溢出 |
| 引语红线 | 只用 page.md 英文原文（NYT 书评句、inner music 句、"the other" 句等），无英文原文处不得伪造中文引号原话 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| hüzün | 呼愁 / 忧郁 | 诺奖理由核心词，勿译成泛泛的「悲伤」 |
| Ottoman miniature | 奥斯曼细密画 | 《我的名字叫红》核心意象 |
| intertextuality | 互文性 | 后现代技法，抄袭指控的辩护语境 |
| Article 301 | 土耳其刑法第 301 条 | 「侮辱土耳其性」罪，年份口径 2005 |
| My Name Is Red | 《我的名字叫红》 | 1591 年设定，Murat III 时期 |
| Museum of Innocence | 纯真博物馆 | 小说与实体博物馆同名双义 |
| Nobel lecture | 诺奖演说《父亲的手提箱》 | 2006-12 颁奖演说 |
| Charles Eliot Norton Lectures | 诺顿讲座 | 哈佛 2009，非诺奖演说，勿混 |
| comparative literature | 比较文学 | 哥大教职 |
| cultural Muslim | 文化穆斯林 | 自述用语，勿演绎成宗教立场 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（75k views，高受众）
- **风格标签**: 高受众 / 流动 / 平稳
- **匹配理由**:
  - 「流动」呼应博斯普鲁斯海峡与伊斯坦布尔海城的水意象——SEA 的平稳律动如海峡上终年不歇的渡轮，是「呼愁」的声音底色
  - 「高受众」匹配其身份——1300 万册、63 种语言、土耳其最畅销作家，大众性与文学性的罕见平衡
  - 「平稳」匹配叙事节奏——从尼尚塔什到哥大再到诺奖，是城市与作家的双城纪录，而非戏剧化的英雄叙事
- **备选**（未采用）: ★★ The Flow of Time——「时间感/纪录片」契合城市记忆主题，但已预分配给 Le Clézio 篇（同批避免撞曲）
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → `presentations/21st_century/Orhan_Pamuk/SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Orhan_Pamuk/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物主记录 + 领域 + 关系入库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实以 page.md 为准，无载禁写；引语只用英文原文。**
