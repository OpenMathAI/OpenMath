# 文学家立传提示词（OpenLiterature 批次实例：Miguel Ángel Asturias）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Miguel Ángel Asturias（1967 诺贝尔文学奖，魔幻现实主义先驱）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 数学家/物理学家/化学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson 提示词骨架）+ 文学家适配（无公式框，以名句引文框/意象图式/书影替代）。
- **本实例**：Miguel Ángel Asturias Rosales（米格尔·安赫尔·阿斯图里亚斯），危地马拉诗人-外交官、小说家、剧作家、记者。
- **设计哲学**：文学家立传保留「身份信息页」与「领域结构化表达」骨架；视觉重心转向**玉米神话与热带巴洛克**——本篇以「玉米与图腾」贯穿。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Miguel Ángel Asturias（1899-10-19 ~ 1974-06-09，享年 74 岁）
- **1967 诺贝尔文学奖官方获奖理由**：
  > "for his vivid literary achievement, deep-rooted in the national traits and traditions of Indian peoples of Latin America"
  > （中译：表彰其鲜明的文学成就，深深植根于拉丁美洲印第安民族的特质与传统）
- **气质关键词**：**魔幻现实主义的先驱、玛雅神话的复述者、独裁小说的开创者**
- **设计母题**：**玉米与图腾（maize & totem）**。玉米人是玛雅创世神话的核心（《Popol Vuh》：最初的人由玉米造成）；版式可用玉米叶脉状细线、图腾柱式竖排元素与热带浓色的意象图式贯穿——热带巴洛克（barroquismo tropical）。
- **本地数据源**：`literature/presentations/pages/20th_century/Miguel_Ángel_Asturias/page.md`（Wikipedia 全文 + frontmatter）+ 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Miguel_%C3%81ngel_Asturias
- **肖像**：第 0 步待下载（infobox 1968 年照片）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `literature/presentations/pages/20th_century/Miguel_Ángel_Asturias/`（第一轮已核对，事实基准如下）：
  - 生卒（1899-10-19 生于危地马拉城 ~ 1974-06-09 逝于西班牙马德里，享年 74 岁；葬巴黎拉雪兹公墓第 10 区；2024-06-09 总统 Bernardo Arévalo 宣布家族同意遗骸迁回危地马拉并启「阿斯图里亚斯年」125 周年诞辰/50 周年忌辰）
  - 国籍（危地马拉；1954-67 流亡期间被剥夺国籍，1966 年恢复）
  - 家庭（长子，父 Ernesto Asturias Girón 律师兼法官、母 María Rosales de Asturias 教师，西班牙裔；弟弟 Marco Antonio；1939 与首任妻子 Clemencia Amado（1915–1979）成婚、育二子 Miguel 与 Rodrigo、1947 离异；1950 与第二任妻子 Blanca Mora y Araujo（1904–2000，阿根廷人）成婚至终老；《Week-end en Guatemala》题献给 Blanca）
  - 教育（San Carlos 大学医学一年转法学 1923 获学位，毕业论文「The Social Problem of the Indian」获 Gálvez Prize；巴黎索邦（巴黎大学）随 Georges Raynaud 研究民族学，研究基切玛雅文化；1926 完成玛雅圣典《Popol Vuh》西班牙语译本——此后该项目持续 40 年）
  - 政治与流亡（父因反对独裁者 Estrada Cabrera 失业迁居 Salamá，与原住民保姆 Lola Reyes 的神话故事是其最初养分；1920 参与 La Generación del 20 推翻 Cabrera；支持 Arbenz 政府任大使；1954 Arbenz 倒台后被 Castillo Armas 驱逐、剥夺国籍，居布宜诺斯艾利斯/智利八年后赴欧；1966 Méndez Montenegro 恢复其国籍并任命为驻法大使至 1970）
  - 关键荣誉（Nobel 1967——第二位拉美文学奖得主，Mistral 1945 之后；Lenin Peace Prize 1966（因香蕉三部曲）；Gálvez/Premio Falla 1923；Sylla Monsegur Prize 1931（Leyendas 法译）/ 1963（Mulata）；Prix du Meilleur Livre Étranger 1952（El Señor Presidente）；兰斯大学/西布列塔尼大学荣誉博士）
  - 核心作品与贡献（4–6 条）：①《Leyendas de Guatemala》（1930，九篇玛雅神话复述，"historia-sueño-poemas"，魔幻现实主义先声）；②《El Señor Presidente》（1933 完稿 1946 墨西哥出版，独裁小说开创之作、恐惧的研究）；③《Hombres de maíz》（Men of Maize，1949，通常视为其代表作，玉米人神话寓言）；④香蕉三部曲（Viento fuerte 1950 / El Papa Verde 1954 / Los ojos de los enterrados 1960，批判联合果品公司）；⑤《Mulata de tal》（1963，玛雅神话与天主教寓言）；⑥《Popol Vuh》西译工程
  - 关键时间线（15–20 节点）：1899 生于危地马拉城 / 1904 父亲与独裁者冲突 / 1905 迁居 Salamá 原住民农庄 / 1908 返城开杂货铺 / 1920 反 Cabrera 学生运动 / 1923 法学毕业论文获奖 / 1923 赴欧转巴黎 / 索邦随 Raynaud 学民族学 / 受 André Breton 影响成超现实主义者 / 1925 起《Popol Vuh》翻译 / 1930《Leyendas de Guatemala》/ Valéry 赞其「热带之梦」/ 1933 回国 / 1939 与 Clemencia 成婚 / 1946《El Señor Presidente》出版 / 1949《Hombres de maíz》/ 1950 离婚并再婚 Blanca / 1950-60 香蕉三部曲 / 1954 流亡 / 1963《Mulata de tal》/ 1966 列宁和平奖+恢复国籍 / 1967 诺贝尔奖 / 1967-70 驻法大使 / 1974-06-09 逝于马德里

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下创建 `Miguel_Ángel_Asturias/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同类目录既有 Makefile，设置 `MAIN=Miguel_Ángel_Asturias_zh`、`VIDEO_NAME=Miguel_Ángel_Asturias_zh`（注意 xelatex 主文件名含重音字符可能引问题——如遇编译障碍可将 MAIN 用 ASCII 别名 `Asturias_zh`，并汇报）

### 第 3 步：收集图片 【人物专属】

- 肖像待下载（infobox 1968 照；images.txt 有 URL 直接用，250px 改 500px；404 用装饰圆占位）
- 可选插图：玛雅陶瓶（Maya vase Branly）、《El Señor Presidente》书影、布宜诺斯艾利斯半身像

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | magical realism | 魔幻现实主义 | 先驱，将其术语与玛雅叙事传统联结 | 核心页 |
| 1 | dictator novel | 独裁者小说 | 《El Señor Presidente》开创之作 | 独裁页 |
| 2 | mayan mythology | 玛雅神话 | Popol Vuh 翻译与《玉米人》神话寓言 | 玛雅页 |
| 3 | ethnology | 民族学 | 索邦 Raynaud 门下的人类学训练 | 巴黎页 |
| 4 | poetry | 诗歌 | Sonetos 等大量诗集，诗人-外交官 | 诗歌页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Georges Raynaud | 师→生（对方为导师） | 索邦民族学老师，基切玛雅文化专家 |
| influence | André Breton | 对方→本人 | 巴黎时期超现实主义影响来源 |
| colleague | Pablo Neruda | 无向 | 1940 墨西哥相识的挚友 |
| colleague | Alejo Carpentier | 无向 | 巴黎写作 El Señor Presidente 时期同道，拉美现代主义 ABC 之一 |
| colleague | Arturo Uslar Pietri | 无向 | 同期巴黎拉美作家同道 |
| spouse | Clemencia Amado | 无向 | 第一任妻子 1939–1947，育二子后离异 |
| spouse | Blanca Mora y Araujo | 无向 | 第二任妻子 1950–1974，Week-end en Guatemala 题献对象 |
| parent-child | Rodrigo Asturias | 父→子 | 之子，化名 Gaspar Ilom（取自 Men of Maize 人物），后为 URNG 主席 |

#### 4.5.1 入库操作

- 写入 `MySQL/data/Miguel_Ángel_Asturias.yaml`，`python3 seed_person.py data/Miguel_Ángel_Asturias.yaml` 幂等入库
- 方向约定：advisor-student 写 `direction: advisor`（对方是导师）；influence 为对方影响本人；spouse 无向；parent-child 按 from<to 归一不写 direction
- **政治内容红线**：Banana Trilogy 与 Lenin Peace Prize 只按 page.md 客观表述（冷战语境一笔带过），不作政治评价

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：浓烈、热带、神话与现实互渗
- **配色**：深青（主色，预分配 `#0E4D64`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeMagic` 魔幻现实主义 — 深青 `#0E4D64`
  - `badgeDictator` 独裁者小说 — 暗红 `#8C2B2B`
  - `badgeMaya` 玛雅神话 — 玉米金 `#C98F27`
  - `badgeEthno` 民族学 — 苔绿 `#4E6E3D`
- **背景母题**：玉米叶脉状细线 + 大而稀疏的暖色实心圆（图腾/太阳意象）

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 流亡地 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后，左头像 + 右信息网格（生卒/国籍/教育/流亡经历/主要荣誉/核心领域）。
4. **文学家无公式框**：用名句引文框（仅限 page.md 有原文者，如 "Oí mucho, supuse un poco más e inventé el resto" 或 "El tropico es el sexo de la tierra"）、书影或意象图式替代。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 魔幻现实主义先驱 / Miguel Ángel Asturias 1899–1974 + badge + 头像
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 魔幻现实主义 / 独裁者小说 / 玛雅神话 / 香蕉三部曲
04  危地马拉童年 (1899–1923) — 父亲与独裁者的冲突、Salamá 奶妈的神话故事
05  学生岁月与「二十年代一代」— 反 Cabrera 运动、Popular University、法学论文获奖
06  巴黎：民族学与超现实主义 — Raynaud 门下、Breton 影响、Popol Vuh 翻译开端
07  《Leyendas de Guatemala》(1930) — Valéry 引文框、historia-sueño-poemas
08  《El Señor Presidente》(1946) — 独裁小说开创、恐惧的气候（书影）
09  《Hombres de maíz》(1949) — 玉米人神话、nahualism 变形意象图式
10  香蕉三部曲 (1950–1960) — 联合果品公司批判、客观一句带过冷战语境
11  流亡与重返 — 1954 驱逐/剥夺国籍、Mulata de tal、1966 恢复国籍
12  1967 诺贝尔奖 — 引文框、第二位拉美得主（Mistral 1945 之后）、1966 列宁和平奖一笔带过
13  外交官与诗人-外交官传统 — 驻法大使、诗歌与剧作概览
14  遗产 — 拉美 Boom 的先声、国家奖与国家剧院以其命名、ABC writers
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照已有文学侧成品的 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Asturias 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 魔幻现实主义归属 | 他是先驱/先声（precursor），但「magic realism」一词他用指征服前的玛雅故事而非自己的作品——勿写「他发明了魔幻现实主义一词来形容自己小说」 |
| 玛雅语言 | 他不会任何玛雅语言，自承对原住民心灵的解释是直觉+想象的——此为 page.md 明载的自我裁定，Review 勿当作缺漏补写 |
| 诺奖获奖作品 | 诺贝尔奖通常与 Hombres de maíz 关联（page.md 口径），勿单写「因 El Señor Presidente 获奖」 |
| 国籍变动 | 1954 被剥夺国籍、1966 恢复并被任命驻法大使至 1970——年份勿混 |
| Cabrera 叙事 | 父亲 1904 与独裁者冲突是家族创伤源；《El Señor Presidente》的总统「从未被点名」但影射 Cabrera——勿写「直接描写 Cabrera 生平」 |
| 政治内容 | 香蕉三部曲/列宁和平奖/Arbenz 只客观一句，不展开冷战政治评价；儿子 Rodrigo 的 URNG 岗位仅入 parent-child note，不展开 |
| 索邦 | 当时称 University of Paris（索邦）；Raynaud 是「随其研究/学习」的老师，写 advisor-student 时 note 注明是巴黎民族学学习时期，勿升格为「博士导师」 |
| 两位妻子 | 顺序与年份勿混：Clemencia 1939–1947、Blanca 1950–1974；Blanca 是阿根廷人（流亡布宜诺斯艾利斯的原因） |
| 死亡地 | 逝于马德里、葬巴黎拉雪兹；勿写「死于巴黎」 |
| 无载禁写 | 与 Borges/Carpentier 的「ABC writers」是批评家 Gerald Martin 的归类，非个人交往；Kafka/Joyce/Faulkner 的比较是评论界类比，勿入关系库 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| magical realism | 魔幻现实主义 | 非「魔幻写实主义」混译；注意归属先声 |
| dictator novel | 独裁者小说 | 拉美文类 |
| Popol Vuh | 《波波尔·乌》 | 玛雅基切圣典 |
| Hombres de maíz | 《玉米人》 | 1949 |
| nahualism / nagual | 纳瓦尔主义 / 护身兽 | 人可化为守护动物 |
| barroquismo tropical | 热带巴洛克 | 学者 Royano Gutiérrez 的命名 |
| Leyendas de Guatemala | 《危地马拉传说》 | 1930 |
| Banana Trilogy | 香蕉三部曲 | 1950/1954/1960 |
| ladino / mestizo | 拉迪诺人 / 混血人 | 身份叙事语境词 |
| poet-diplomat | 诗人-外交官 | 传统称谓 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Expedition**（预分配）
- **风格**: 远征 / 探索 / 大陆尺度
- **匹配理由**:
  - "Expedition" 匹配其一生横跨危地马拉—巴黎—布宜诺斯艾利斯—巴黎—马德里的远行叙事与「写美洲是我的天职」的大陆抱负
  - 探索感对应民族学田野与《Popol Vuh》四十年翻译工程的耐心跋涉
  - 节奏的行进感适配香蕉三部曲的批判力量与流亡迁移
- **备选** (未采用): Daylight（明亮但弱于大陆尺度）、Cinematic Experience（戏剧化但已高频使用）
- **本地路径**: `music_audio/` 下 Expedition 曲目 → 复制到 `presentations/20th_century/Miguel_Ángel_Asturias/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Miguel_Ángel_Asturias/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Miguel_Ángel_Asturias/metadata.json` | properties 辅助（冲突以正文为准） |
| `literature/presentations/pages/20th_century/Miguel_Ángel_Asturias/images.txt` | 肖像 URL 清单（第 3 步下载源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录（获奖理由中译） |
| `literature/generate_20th_century_list.py` 的 CITATION_ZH | 官方获奖理由中译（key=(年份,姓名)） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/data/Miguel_Ángel_Asturias.yaml` | 本人社会关系/领域 yaml（已入库） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
