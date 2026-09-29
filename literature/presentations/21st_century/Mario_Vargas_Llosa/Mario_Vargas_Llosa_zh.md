# 文学家立传提示词（Mario Vargas Llosa · 2010 诺贝尔文学奖）

> **本文件是 OpenLiterature 21 世纪批次的「人物专属立传提示词」**，目标人物 Mario Vargas Llosa（马里奥·巴尔加斯·略萨）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–9 步骨架），内容适配文学家：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Jorge Mario Pedro Vargas Llosa（第一代巴尔加斯·略萨侯爵），2010 年诺贝尔文学奖得主，拉美文学爆炸主将——「权力结构的绘图师」。
- **设计哲学**：文学家立传以「作品与意象」代替「定理与公式」——身份信息页（★ 必做）与文学领域结构化表达两点保留，公式框一律换成**名句引文框**。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Mario Vargas Llosa（1936-03-28 生于阿雷基帕 ~ 2025-04-13 逝于利马，享年 89 岁）
- **气质关键词**：**权力的绘图师、对话的编织者、从左到自由的思想远征者** —— 2010 年获奖理由（官方 EN 原文，禁止改写）：
  > "for his cartography of structures of power and his trenchant images of the individual's resistance, revolt, and defeat"（表彰其权力结构的图谱，以及其对个人的抗拒、反叛与失败的有力刻画）
- **设计母题**：**权力的地图与对话的编织**。主色深藏青承载其政治小说的冷峻；背景以经纬线勾勒「秘鲁—马德里—利马」的权力地图；前景两条交错的对话丝带呼应其标志性的「对话编织」技法（交织对话）。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/Mario_Vargas_Llosa/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **参考模板**：
  - 提示词母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`）
  - yaml 母本：`MySQL/data/Kenneth_G_Wilson.yaml`

---

## 三、任务流程 【逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Mario_Vargas_Llosa` 四件套到 `literature/presentations/pages/21st_century/Mario_Vargas_Llosa/`（事实基准如下）：
  - 生卒（1936-03-28 生于阿雷基帕 ~ 2025-04-13 逝于利马，享年 89；遗体私人仪式火化）；国籍：**秘鲁 + 西班牙（1993 起）+ 多米尼加（2023 起）**；2011 受封「巴尔加斯·略萨侯爵」
  - 家庭：父 Ernesto Vargas Maldonado（航空公司无线电员）、母 Dora Llosa Ureta（克里奥尔世家）；父母离异、幼年被谎称「父亲已死」；童年随外祖家在玻利维亚科恰班巴与秘鲁皮乌拉度过，1946 年 10 岁赴利马与父重逢
  - 教育：莱昂西奥·普拉多军事学校（14 岁被父送入，后转学皮乌拉）→ 圣马科斯国立大学法律与文学（1953）；1958 毕业、获马德里康普卢腾斯大学奖学金
  - 婚姻：1955 娶舅舅的妻妹 Julia Urquidi（长他 10 岁，1964 离婚）；1965 娶表妹 Patricia Llosa（2015 分居）；子女 Álvaro（1966，作家/编辑）、Gonzalo（1967）、Morgana（1974，摄影师）；2015–2022 与社交名媛 Isabel Preysler 相伴
  - 文坛事件：1971 康普卢腾斯博士论文《加西亚·马尔克斯：弑神者的故事》；1976-02 墨西哥城美术宫一拳绝交（原因双方终身未言， mutual friend Guillermo Angulo 另有一说）；2007 授权其论著作《百年孤独》40 周年版引言
  - 政治（只客观简述）：早年支持古巴革命 → 1971 Padilla 事件后转向古典自由主义 → 1987 创自由运动党 → 1990 以 FREDEMO 联盟竞选秘鲁总统、首轮 34% 但 runoff 大败于藤森 → 此后以写作与国际演讲继续公共生涯（1983 乌丘拉加西调查委员会受舆论批评）
  - 学术职务：1969–70 伦敦大学国王学院西语美洲文学讲师、1977–78 剑桥 Simón Bolívar 讲席/丘吉尔学院海外研究员、1988 雪城大学访问教授、1992–93 哈佛访问教授；1976–79 国际笔会会长；1994 入选西班牙皇家语言学院（L 席，1996-01-15 就座）；2021 当选法兰西学士院
  - 核心作品：《城市与狗》(1963/1966)、《绿房子》(1965/1968)、《酒吧长谈》(1969/1975)、《潘达雷昂上尉与劳军女郎》(1973)、《胡莉亚姨妈与剧作家》(1977)、《世界末日之战》(1981)、《狂人玛伊塔》(1984)、《谁杀死了帕洛米诺·莫雷罗？》(1986)、《安第斯山上的死神》(1993)、《水中鱼》(1993 自传)、《山羊的盛宴》(2000)、《天堂在别的街角》(2003)、《坏女孩的恶作剧》(2006)、《艰难时代》(2019)、《我献给你我的沉默》(2023，宣布为最后一部小说并退休)；批评专著《加西亚·马尔克斯：弑神者的故事》(1971)、《永恒的狂欢》（论福楼拜）、《古老的乌托邦》（论阿格达斯，1996）
  - 关键荣誉：Premio de la Crítica Española 1963、**罗慕洛·加列戈斯奖首任 1967**、阿斯图里亚斯亲王奖 1986、**塞万提斯奖 1994**、耶路撒冷奖 1995、德国书业和平奖、全美书评人协会批评奖、**2010 诺贝尔文学奖**、Carlos Fuentes 奖 2012、聂鲁达艺术文化功绩勋章 2018
  - 关键时间线（15–20 节点）：1936 生于阿雷基帕 → 1946 赴利马见父 → 1950 入军事学校 → 1953 入圣马科斯 → 1955 首婚 + 首部剧作上演 → 1957 首批短篇小说发表 → 1958 毕业、奖学金赴马德里 → 1960 移居巴黎 → 1963《城市与狗》→ 1964 离婚 → 1965 再婚 → 1967《绿房子》加列戈斯奖 → 1969《酒吧长谈》→ 1971 博士论文 + 与卡斯特罗决裂 → 1976 一拳绝交 + 任笔会会长 → 1977《胡莉亚姨妈》→ 1981《世界末日之战》→ 1983 调查委员会 → 1987 组党 → 1990 竞选败于藤森 → 1993 入籍西班牙 + 《水中鱼》→ 2000《山羊的盛宴》→ 2010-10-07 诺奖 → 2011 受封侯爵 → 2021 法兰西学士院 → 2023 宣布退休 → 2025-04-13 逝世于利马

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Mario_Vargas_Llosa/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已立传目录的 `Makefile`，设置 `MAIN=Mario_Vargas_Llosa_zh`、`VIDEO_NAME=Mario_Vargas_Llosa_zh`

### 第 3 步：收集图片 【人物专属】

- 从 `images.txt` 取 infobox 肖像（1986 年照 `Mariovargasllosa.jpg` 等，250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 时用 Commons `Special:FilePath/<文件名>?width=600`；再失败用装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | political novel | 政治小说 | 独裁与权力结构：《酒吧长谈》《山羊的盛宴》 | 核心页 |
| 1 | latin american boom | 拉美文学爆炸 | 与 García Márquez 等并列主将 | 爆炸页 |
| 2 | historical novel | 历史小说 | 《世界末日之战》（卡努杜斯） | 历史页 |
| 3 | literary criticism | 文学批评 | 《弑神者的故事》《永恒的狂欢》 | 批评页 |
| 4 | interlacing dialogues | 对话编织技法 | 时空交错的对话蒙太奇 | 技法页 |

#### 4.1 入库操作（`MySQL/seed_person.py data/Mario_Vargas_Llosa.yaml`）

- **UPD 复用库内既有 stub**（id=5544，马尔克斯 yaml 所建）：`name_en='Mario Vargas Llosa'`、`qid='Q39803'`，设置 `primary_occupation='writer'`、`has_biography: false`、`has_social_data=1`，回填生卒/描述字段；**勿另建别名记录**
- 关联职业 `writer`（rank 0）+ `novelist`/`essayist`；国籍 `Peru`（rank 0）+ `Spain`（rank 1）
- 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Julia Urquidi | 无向 | 首任妻子，1955 结婚，1964 离婚 |
| spouse | Patricia Llosa | 无向 | 次任妻子（表妹），1965 结婚，2015 分居 |
| parent-child | Álvaro Vargas Llosa | 无向 | 长子（1966 年生），作家、编辑 |
| parent-child | Gonzalo Vargas Llosa | 无向 | 次子（1967 年生），国际公务员 |
| parent-child | Morgana Vargas Llosa | 无向 | 女（1974 年生），摄影师 |
| colleague | Gabriel García Márquez | 无向 | 博士论文《加西亚·马尔克斯：弑神者的故事》(1971) 研究对象，曾为挚友 |
| controversy | Gabriel García Márquez | 无向 | 1976-02 墨西哥城美术宫一拳绝交，原因双方终身未言 |
| influence | Jean-Paul Sartre | 无向 | 对话技巧来源，《城市与狗》题词取自其作 |
| influence | Gustave Flaubert | 无向 | 著有《永恒的狂欢》研究其美学 |
| influence | William Faulkner | 无向 | 自称其"完善现代小说方法的作家"，《八月之光》影响《城市与狗》 |
| colleague | José María Arguedas | 无向 | 著有长篇研究《古老的乌托邦》(1996) |
| influence | Euclides da Cunha | 无向 | 《腹地》纪实为《世界末日之战》蓝本 |

#### 4.5.1 入库操作

- 以 `name_en='Mario Vargas Llosa'`（id=5544）为中心写入 `person_relation`；对手方 Gabriel García Márquez（id=5542）、Jean-Paul Sartre（id=4996）、William Faulkner（id=5293）库内已有记录勿另建；其余建 stub（`has_biography=0`，不编造 qid），note 加 `[材料待展开] ` 前缀；与 Pamuk yaml 所建 Vargas Llosa–Orhan Pamuk 联署行撞 uq_rel 属正常幂等跳过

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：权力的冷峻、对话的密度、安第斯的硬朗
- **配色**：主色深藏青 `#14324F`（预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 政治小说 — 独裁铁灰 `#37474F`
  - `badgeB` 拉美文学爆炸 — 热带翡翠 `#0B5351`
  - `badgeC` 历史小说 — 高原赭红 `#A34700`
  - `badgeD` 批评/技法 — 学院深蓝 `#1E4E79`
- **背景母题**：经纬线权力地图——细线勾勒模糊的大陆轮廓，两条金色丝带在画面中央交错（对话编织），右下角一枚王冠剪影（侯爵）

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（右上角 + `draw=coveraccent!50` 细边框）与国籍行（`秘鲁 / 西班牙 | 马德里–利马 | 诺贝尔文学奖 2010`）。
2. **身份信息页 ★ 必做**：左肖像 + 右信息网格（生卒、三重国籍、教育、婚姻、任职、核心作品、主要荣誉）。
3. 引号用半角 `" "`；结尾页品牌统一 `OpenMathAI`。
4. 引文框内容只用 page.md 载英文原文（官方获奖理由；诺奖演说自述 "I carry Peru deep inside me…" 段与 "I love Spain as much as Peru…" 段；"Literature is Fire" 早期口号与获奖演说 In Praise of Reading and Writing 的对照），禁止杜撰「中文原话」。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 权力的绘图师 / Mario Vargas Llosa 1936–2025 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）
03  核心作品概览 — 城市与狗 / 绿房子 / 酒吧长谈 / 山羊的盛宴
04  「父亲已死」的童年 (1936–1953) — 阿雷基帕、科恰班巴、皮乌拉、1946 重逢
05  圣马科斯与记者岁月 (1953–1960) — 法律与文学、首批短篇、巴黎
06  《城市与狗》核心页 (1963) — 军校经验、Critical 奖、秘鲁军界风波
07  拉美文学爆炸 (1965–1975) — 《绿房子》加列戈斯首奖、与 Boom 同代人
08  《酒吧长谈》与对话编织 (1969) — 交织对话技法意象图式
09  加西亚·马尔克斯：挚友与决裂 (1971–2007) — 博士论文、一拳绝交、2007 转折（只客观陈述）
10  思想的远征 (1971–1990) — Padilla 事件转向、自由运动党、1990 竞选与败于藤森（只客观简述）
11  2000 年代的巅峰 — 《山羊的盛宴》《天堂在别的街角》《坏女孩》
12  2010 诺贝尔文学奖 — 官方理由 EN 原文 + 中译、"Literature is Fire" 与演说对照
13  荣誉与晚年 — 塞万提斯 1994 · RAE 1994 · 侯爵 2011 · 法兰西学士院 2021
14  遗产与谢幕 (2023–2025) — 最后一部小说、2025-04-13 利马逝世、多国致哀
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；文学领域页用表格 + 意象色块替代公式框

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Vargas Llosa 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "for his cartography of structures of power…" 禁止改写；中译用名录版「权力结构的图谱……有力的刻画」 |
| UPD 入库 | 库内 id=5544 为马尔克斯 yaml 所建 stub（qid 空）——必须 UPD 复用回填 Q39803，**勿新建** |
| 决裂叙事 | 1976 一拳事件：官方无解释 + Guillermo Angulo 私说（夺妻说）两说并列；2007 授权引言是公开的缓和迹象——均只客观陈述 |
| 政治红线 | 政治立场演变（卡斯特罗→Padilla→古典自由主义）、1990 竞选、各国政治表态**只按 page.md 客观简述、不作评价**；Plan Verde 军政细节**禁写** |
| 政治人物 | Fujimori/Keiko/Castro/Pinochet/Bolsonaro/Milei 等一律不建关系、不展开 |
| 合著与智库 | 《Política razonable》五位合著者、Mont Pelerin Society、Irving Kristol 奖等政治性关联**不入库**（防政治叙事扩散） |
| 巴拿马/天堂文件 | 2016/2021 两份文件争议**禁写**（非文学主线，涉及在世/刚逝者财务指控） |
| 《绿房子》年份 | 西语 1965 / 英译 1968；1967 获加列戈斯奖（首届），「与 Onetti、García Márquez 同台竞逐」为 page.md 明载可写 |
| 表妹婚姻 | Patricia Llosa 是其 first cousin（page.md 明载，可写）；Isabel Preysler 是伴侣（2015–2022）非配偶，不入 spouse |
| Julia 回忆录 | Julia Urquidi 另著《瓦吉塔斯没说的》指控其叙述夸大——只客观并置 |
| 姓氏口径 | 全名 Jorge Mario Pedro Vargas Llosa；「巴尔加斯·略萨」为复合姓，勿拆分称「略萨教授」式混用 |
| 子女 | 三人全具名入库（ Álvaro/Gonzalo/Morgana），职业照录页面 |
| 引语红线 | 只用 page.md 英文原文；演说两句引文须成对出现（秘鲁句+西班牙句） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| cartography of power | 权力的图谱 | 获奖理由核心词 |
| Latin American Boom | 拉美文学爆炸 | 专有文学史术语 |
| interlacing dialogues | 对话编织（交织对话） | 其标志性叙事技法 |
| La ciudad y los perros | 《城市与狗》 | 西语原题直译「城市与狗」 |
| La casa verde | 《绿房子》 | 1965 |
| Conversación en La Catedral | 《酒吧长谈》 | 独裁题材代表作 |
| La guerra del fin del mundo | 《世界末日之战》 | 1981，卡努杜斯战争 |
| La fiesta del chivo | 《山羊的盛宴》 | 2000，特鲁希略独裁 |
| deicide | 弑神 | 博士论文标题关键词 |
| Marquess of Vargas Llosa | 巴尔加斯·略萨侯爵 | 2011 西班牙王室册封 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions（52k views，高受众）
- **风格标签**: 高受众 / 强推进 / 紧张
- **匹配理由**:
  - 「强推进」匹配其叙事引擎——《城市与狗》《酒吧长谈》的时间线穿插与对话蒙太奇本就是高压推进的叙事机器
  - 「紧张」匹配其政治小说的张力场——独裁、密谋、审讯与反叛，权力结构的图谱需要一支带锋芒的配乐
  - 「革命性转折」标签呼应其生平的两次大转折——与卡斯特罗决裂的思想转折与 1990 竞选的人生转折
- **备选**（未采用）: ★★ Cinematic Experience——「电影感」契合其多部改编电影，但同批已用且张力不及 Savage 贴合政治小说主线
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` → `presentations/21st_century/Mario_Vargas_Llosa/Savage.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Mario_Vargas_Llosa/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物主记录 + 领域 + 关系入库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实以 page.md 为准，无载禁写；政治内容只客观简述不评价；引语只用英文原文。**
