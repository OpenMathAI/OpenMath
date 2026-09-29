# 文学家立传提示词（OpenLiterature：Gabriel García Márquez）

> **本文件是 OpenLiterature 的人物专属立传提示词**，以 Kenneth G. Wilson（OpenPhysicist 模板标杆）为骨架，适配文学家。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 García Márquez 定制内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合 OpenPhysicist 标杆（Kenneth G. Wilson 提示词 + tex 结构）与文学家侧实战经验。
- **本实例**：Gabriel García Márquez（加夫列尔·加西亚·马尔克斯，昵称 Gabo），1982 诺贝尔文学奖得主，魔幻现实主义的旗手与《百年孤独》的作者。
- **设计哲学**：文学家立传**没有公式框——以代表作书影 / 名句引文框 / 意象图式替代**；仍须保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Gabriel José García Márquez（1928-03-06 ~ 2014-04-17，享年 86 岁）
  > ⚠️ 生年口径：frontmatter/metadata 写 1927-03-06，**正文与 infobox 均为 1928-03-06**（"died... aged 87"/享年 86 岁亦与 1928 相符）——本篇一律取 **1928-03-06**，metadata 为噪声，Review 勿误改。
- **气质关键词**：**马孔多的缔造者、魔幻现实主义的旗手、加勒比说书传统的现代传人** —— 1982 诺贝尔文学奖获奖理由：
  > "for his novels and short stories, in which the fantastic and the realistic are combined in a richly composed world of imagination, reflecting a continent's life and conflicts"
  > （表彰其小说与短篇故事，将奇幻与现实结合于构造丰富的想象世界之中，反映了一个大陆的生活与冲突）
- **设计母题**：**马孔多与黄蝴蝶（Macondo and solitude）**。外祖母「把非凡之事当作再自然不过来讲」的 deadpan 叙述、外祖父的战争故事与香蕉园时代、拉美孤独主题——版式语言宜用热带植物色块、黄蝴蝶与雨水意象、报纸排版元素（新闻体出身）。
- **本地数据源**：`literature/presentations/pages/20th_century/Gabriel_García_Márquez/page.md` + 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Gabriel_García_Márquez （肖像第 0 步标「待下载」，infobox 有 2002/2009 年照）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面四件套已下载
- 肖像：**待下载**（infobox 照片 "García Márquez in 2002"；404 回退 Commons Special:FilePath / REST API，再失败装饰圆占位）
- **事实基准（正文优先）**：
  - 生卒：1928-03-06 生于哥伦比亚加勒比地区阿拉卡塔卡（Aracataca）~ 2014-04-17 逝于墨西哥城（肺炎），享年 86 岁（frontmatter 1927 为噪声，以正文为准）
  - 家庭：父 Gabriel Eligio García（药剂师，保守党人）；母 Luisa Santiaga Márquez Iguarán——父母恋爱受阻的悲喜剧故事后来化入《霍乱时期的爱情》；幼年由外祖父母抚养：外祖父上校 Nicolás Ricardo Márquez Mejía（「千日战争」自由党老兵，称其「我与历史和现实的脐带」，拒绝对香蕉屠杀沉默、善讲故事、教字典课、带看马戏、第一次给他看冰）；外祖母 Doña Tranquilina Iguarán Cotes（「魔法、迷信与超自然现实观的源头」，讲述风格直接影响《百年孤独》）
  - 教育：1947 入哥伦比亚国立大学法学部（波哥大）；1948 Bogotazo 骚乱后大学无限期关闭，转卡塔赫纳大学并任《宇宙报》记者；1950 弃法从文，赴巴兰基亚《先驱报》专栏（笔名 "Septimus"）
  - 新闻生涯：《宇宙报》（1948–49）→《先驱报》（1950–52）→《观察家报》波哥大（1954–55）；1955 年连载 14 篇《海难水手的故事》揭露军舰走私沉船真相引发争议，被报社派往欧洲任驻外记者；QAP 新闻节目创始合伙人（1992–1997 播出）
  - 巴兰基亚团体（Barranquilla Group）：文学激励源泉；Ramon Vinyes（书店老板，后化为《百年孤独》中的老加泰罗尼亚人）；此时接触 Woolf、Faulkner
  - 婚姻：1958 巴兰基亚与 Mercedes Barcha 成婚（14 岁时识她，时她 9 岁）；长子 Rodrigo（1959 生，影视导演）、次子 Gonzalo（1961 墨西哥城生，平面设计师）；1990 年代初与墨西哥作家 Susana Cato 有婚外情，2022 年报道其女 Indira Cato（纪录片制作人）
  - 流徙：1956–58 欧洲两年（巴黎 Rue Cujas 旅馆挂牌纪念）→ 加拉加斯 → 1961 灰狗巴士游美国南方（Faulkner 故地）→ 定居墨西哥城 →《百年孤独》成书后居巴塞罗那七年 → 1975 后回墨西哥城
  - 《百年孤独》（1967）：驱车赴阿卡普尔科途中顿悟，掉头回家、卖车写作 18 个月；妻赊账买食品与房租；每晚与 Mutis 夫妇、Elío/García Ascot 夫妇试读讨论；题献 Jomí García Ascot 与 María Luisa Elío；英译 Gregory Rabassa（1970）；销量逾 5000 万；获 1972 Rómulo Gallegos 奖；William Kennedy 称之「《创世记》之后第一部应当全人类必读的文学作品」
  - 1982-12 诺贝尔奖：拉丁美洲第四位得主（1945 Mistral、1967 Asturias、1971 Neruda 之后）；受奖演说《拉丁美洲的孤独》
  - 关键荣誉：Neustadt 国际文学奖 1972 · Rómulo Gallegos Prize 1972 · **Nobel 1982** · 法国荣誉军团勋章（Grand Officer）· 阿兹特克雄鹰勋章 · Simón Bolívar 奖等；哥伦比亚/墨西哥多所大学荣誉博士（含 Columbia）
  - 核心作品（5–6 条）：《枯枝败叶》（1955，首部中篇，七年才找到出版者）；《没有人给他写信的上校》（1961）；《百年孤独》（1967）；《族长的秋天》（1975，独裁者小说，「权力的孤独之诗」）；《一桩事先张扬的凶杀案》（1981，基于 1951 年苏克雷真实凶案，主人公原型挚友 Cayetano Gentile Chimento）；《霍乱时期的爱情》（1985）；《活着为了讲述》（2002，回忆录三部曲第一卷）
  - 晚年：1999 年误诊肺炎实为淋巴癌，化疗缓解——促使其闭门写回忆录；2000 年秘鲁报纸误报死讯与「告别诗」（实为墨西哥腹语者所作，本人否认）；2012 弟 Jaime 公布患失智症；2014-04-17 逝于墨西哥城，火葬，骨灰安放仪式于墨西哥城美术宫；哥伦比亚总统 Santos 称其「有史以来最伟大的哥伦比亚人」；身后遗稿《我们八月见》（Until August）2024-03-06（97 岁冥诞）违背本人销毁遗愿出版
  - 关键时间线（17 节点）：1928 生于阿拉卡塔卡 → 1937 祖父去世随父母迁苏克雷 → 1940 巴兰基亚寄宿中学 → 1947 国立大学法学部·《观察家报》刊处女作《第三次无奈》→ 1948 Bogotazo·转卡塔赫纳·《宇宙报》→ 1950 弃法从文·《先驱报》→ 1954–55 《观察家报》·海难连载 → 1955《枯枝败叶》·赴欧 → 1958 与 Mercedes 成婚 → 1959 长子 Rodrigo 生 → 1961 迁墨西哥城 → 1962《恶时》→ 1965–67 闭门 18 个月·《百年孤独》→ 1972 Neustadt 奖·Gallegos 奖 → 1975《族长的秋天》→ 1981《一桩事先张扬的凶杀案》→ 1982 诺贝尔奖 → 1985《霍乱时期的爱情》→ 1996《一个海难幸存者的故事》之外的《新闻》→ 1999 癌症·转写回忆录 → 2002《活着为了讲述》→ 2014 逝于墨西哥城

### 第 1 步：建立目录 【模板通用】

- 已在 `literature/presentations/20th_century/Gabriel_García_Márquez/`（本提示词所在目录）

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=Gabriel_García_Márquez_zh`、`VIDEO_NAME=Gabriel_García_Márquez_zh`

### 第 3 步：收集图片 【人物专属】

- 下载肖像到 `images/Gabo.jpg`（infobox 2002 年照），`curl -A "Mozilla/5.0"` + `file` 验证；失败装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**García Márquez 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | magic realism | 魔幻现实主义 | 「以 deadpan 口吻讲最骇人的奇事」；Remedios 升天为常引例 | 封面、核心页 |
| 1 | epic novel | 史诗性长篇 | 《百年孤独》——布恩迪亚家族与马孔多百年兴衰 | 核心页 |
| 2 | Latin American Boom | 拉美文学 Boom | 与 Cortázar/Fuentes/Vargas Llosa 并列定义该运动 | 诗派页 |
| 3 | journalism | 新闻写作 | 记者出身；《一桩事先张扬的凶杀案》=新闻+写实+侦探；《一个海难幸存者的故事》连载 | 新闻页 |
| 4 | dictator novel | 独裁者小说 | 《族长的秋天》——「权力的孤独之诗」 | 主题页 |

#### 4.1 入库操作

- `python3 seed_person.py data/Gabriel_García_Márquez.yaml`（幂等；主记录 `primary_occupation='writer'`、`has_social_data=1`）
- 职业关联：writer（rank 0）、novelist（rank 1）、journalist（rank 2）
- 校验 person_field / person_relation 计数

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Franz Kafka | 单向 | 1947 年读《变形记》深受启发，被视为开笔契机 |
| influence | William Faulkner | 单向 | 叙事技巧/历史主题/乡土背景的影响；1961 年专程游美国南方 |
| influence | Virginia Woolf | 单向 | 巴兰基亚时期接触；《恶时》形式结构本于《达洛维夫人》 |
| influence | Ramon Vinyes | 单向 | 巴兰基亚团体激励人物；《百年孤独》中老加泰罗尼亚人原型 |
| colleague | Carlos Fuentes | 无向 | 合写首个电影剧本（El gallo de oro）；称其为塞万提斯以来最受欢迎的西语作家 |
| colleague | Plinio Apuleyo Mendoza | 无向 | 挚友记者作家，多次对谈（孤独主题、魔幻现实主义之辩） |
| colleague | Álvaro Mutis | 无向 | 挚友，《百年孤独》写作 18 个月间每夜共同试读讨论 |
| colleague | Julio Cortázar | 无向 | 拉美文学 Boom 同侪 |
| controversy | Mario Vargas Llosa | 无向 | 1976 年在墨西哥被其当众挥拳，现代文学最大公开决裂之一；两人同属 Boom |
| spouse | Mercedes Barcha | 无向 | 1958 年巴兰基亚成婚，相守至 2014 年 |
| parent-child | Rodrigo García | — | 长子（1959 生），影视导演 |
| parent-child | Gonzalo García | — | 次子（1961 生），墨西哥城平面设计师 |

> **不入库说明**：Fidel Castro 与 Mario Vargas Llosa 之外的政要关系（Clinton 解禁、Santos 悼词等）非文学圈关系；Castro 的「细腻友谊」涉政且无文学职业交集类型，仅提示词与正文客观简述；Reinaldo Arenas（批评其与 Castro 友谊）、Jorge Amado（仅合影）、Jorge Luis Borges（仅并列评价，非个人互动）、Gregory Rabassa（译者工作关系可不入库）、电影合作者 Ruy Guerra/Francesco Rosi、Susana Cato/Indira Cato（婚外情与报道级事实，客观简述即可）均不入库。

#### 4.5.1 入库操作

- 以 `name_en='Gabriel García Márquez'`（Q5878）为中心写入 `person_relation`；库内既有裸 stub（id=5542）将被 UPD 回填 QID
- 对手方沿用库内记录：Franz Kafka(5139)、William Faulkner(5293)、Virginia Woolf(5171)、Mario Vargas Llosa(5544)；其余自动建 stub
- parent-child 不写 direction；influence 用 note 注明影响方向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：热带湿热、金黄与深蓝、孤独的诗意
- **配色**：深海蓝（主色 `#1F3A5F`）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeMacondo` 马孔多与《百年孤独》— 芭蕉绿 `#3E6B3A`
  - `badgeMagic` 魔幻现实主义 — 金黄 `#C9A227`
  - `badgeBoom` 拉美文学 Boom — 深红 `#A31621`
  - `badgePress` 新闻生涯 — 报纸灰 `#5A5F58`
- **背景母题**：热带植物叶片、黄蝴蝶、雨季色块与报纸字栏交叠

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + 细边框 + 姓名小字注（可加 "Gabo" 昵称）。
2. 封面明示国籍（Colombia）；底部状态栏 `国籍 | 语言 | 主要奖项`。
3. **必须有身份信息页**：左头像 + 右信息网格（生卒、外祖父母养育、法学转新闻、流徙地图、荣誉、核心领域）。
4. **无公式框**：用《百年孤独》书影 /《拉丁美洲的孤独》受奖演说引文框（page.md 有英文原文）/ 黄蝴蝶意象图式替代。
5. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页
01  封面 — 马孔多的缔造者 / Gabriel García Márquez 1928–2014 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（外祖父母、教育、流徙、荣誉、核心领域）
03  核心贡献概览 — 《百年孤独》/ 魔幻现实主义 / 新闻写作 / 独裁者小说
04  阿拉卡塔卡童年 (1928–1937) — 外祖父上校与外祖母的讲述术、香蕉屠杀与冰块
05  法学与新闻 (1947–1955) — Kafka《变形记》、Bogotazo、巴兰基亚团体
06  《枯枝败叶》与海难连载 (1955) — 首部中篇七年求出版、14 篇连载风波、赴欧
07  《百年孤独》(1967)（核心页·书影）— 18 个月卖车写作、5000 万册、题献挚友
08  魔幻现实主义（核心页·意象图式）— deadpan 口吻、Remedios 升天、与 Carpentier「神奇现实」
09  《族长的秋天》(1975) — 独裁者小说、「权力的孤独之诗」
10  诺贝尔奖 (1982) — 拉美第四人、《拉丁美洲的孤独》受奖演说
11  《霍乱时期的爱情》(1985) — 父母恋爱故事的化用
12  新闻与电影 — QAP、哈瓦那电影学院、剧本与改编
13  晚年 (1999–2014) — 癌症与回忆录、《活着为了讲述》、身后《我们八月见》
14  荣誉与认可 — Neustadt 1972 · Gallegos 1972 · Nobel 1982 · 荣誉军团勋章
15  遗产：一个大陆的生活与冲突
16  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；宏名禁数字；`\foreach` 分隔符 ASCII 逗号；tex 文件名建议转写 `Gabriel_Garcia_Marquez_zh.tex`（目录保持原文），避免 xelatex/shell 对 í/á 的兼容问题。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；单遍取日志后须重新 `make pdf`。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**García Márquez 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生年噪声 | frontmatter 1927-03-06 为噪声，**正文/infobox 一致 1928-03-06**；享年 86（1928–2014）自洽；Review 勿回改 |
| 香蕉屠杀 | 发生于其出生次年（1928 年末），外祖父「拒绝沉默」是素材源头；勿写发生于其童年记忆年 |
| 《百年孤独》年份 | 写作 18 个月（1965–66）、1967 出版、英译 Rabassa 1970；Neustadt 与 Rómulo Gallegos 奖**同为 1972**——勿错位到 1967 或 1982 |
| Vargas Llosa 决裂 | 1976 年墨西哥电影院当众挥拳，具体起因两人终生未详言——按 page.md 只写「现代文学最大公开决裂之一」，禁编造和解或纠纷细节 |
| Castro 友谊 | 「以文学为基础的知识友谊+批评古巴治理某些方面」的 nuanced 口径；Arenas 的批评客观一句带过；禁政治评价 |
| 遗作 | 《我们八月见》2024-03-06 遗世出版，**违背其销毁遗愿**——须如实标注 |
| 记忆三部曲 | 《活着为了讲述》(2002) 是「计划三部曲」的第一卷，勿写「自传完成」 |
| 死亡误报 | 2000 年秘鲁报纸误报+伪托告别诗「La Marioneta」——本人否认、实为墨西哥腹语者作品；勿当成真事 |
| 引语红线 | Style 节致 Claudia Dreifus 关于 Castro 的对谈、关于《百年孤独》「signals to close friends」的评论、Aracataca 广告牌铭文均有英文原文可引；中文「原话」禁杜撰 |
| 涉政内容 | 左翼立场、FARC/M-19 调停、美签被拒与 Clinton 解禁、Pinochet 罢笔宣言、《新闻》与 Escobar 绑架案——一律按 page.md 客观简述，**不作政治评价、不展开政治叙事** |
| 同名区分 | 儿子 Rodrigo García（导演）与其本人及父亲 Gabriel Eligio García 三代同名，注意谁是谁；《没人写信给上校》主人公無名不与其混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| One Hundred Years of Solitude | 《百年孤独》 | Cien años de soledad；通行译名 |
| magic realism | 魔幻现实主义 | 亦译「魔幻写实主义」；与 Carpentier「神奇现实」（lo real maravilloso）区分 |
| Macondo | 马孔多 | 虚构村镇，名源自香蕉园站名（一种类似木棉的热带树） |
| Latin American Boom | 拉美文学 Boom | 与 Cortázar/Fuentes/Vargas Llosa 同侪 |
| dictator novel | 独裁者小说 | 《族长的秋天》所属类型 |
| Leaf Storm | 《枯枝败叶》 | La Hojarasca，首部中篇 |
| No One Writes to the Colonel | 《没有人给他写信的上校》 | 通行译名 |
| Chronicle of a Death Foretold | 《一桩事先张扬的凶杀案》 | 通行译名（一作《预知死亡纪事》） |
| Living to Tell the Tale | 《活着为了讲述》 | 回忆录三部曲第一卷 |
| Bogotazo | 波哥大大暴动 | 1948-04-09，Gaitán 遇刺引发 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Daylight** — Alex-Productions
- **风格**: 明亮 / 温暖 / 叙事感
- **匹配理由**:
  - "明亮" 对应加勒比阳光与热带色彩——马孔多的金合欢树、黄蝴蝶与连绵雨季的光感
  - "叙事感" 匹配外祖母式的说书传统——把最奇幻的事讲得像确凿的事实
  - 温暖底色呼应《霍乱时期的爱情》式的绵长情感与读者对 Gabo 的普遍 affection
- **本地路径**: `music_audio/alex-productions/` 下 Daylight 曲目 → `presentations/20th_century/Gabriel_García_Márquez/Daylight.wav`
- **时长**: 以实际曲目为准，`ffmpeg -shortest` 自动对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；生年取 1928；涉政内容只客观简述。**
