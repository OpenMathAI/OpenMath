# 文学家立传提示词（OpenLiterature：Frédéric Mistral）

> **本文件是弗雷德里克·米斯特拉尔（1904 诺贝尔文学奖）的人物专属立传提示词**，结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容按文学家适配：无公式框，以**代表作书影/名句引文框/意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各学科侧共享体系）。
- **本实例**：Frédéric Mistral（弗雷德里克·米斯特拉尔），1904 诺贝尔文学奖得主（与 José Echegaray 共享），**普罗旺斯语（奥克语）诗人、词书编纂家、菲列布里什（Félibrige）创始人**。
- **设计哲学**：文学家立传以**作品意象与文学史脉络**替代公式与实验——身份信息页（★ 必做）与「文学领域」结构化表达仍须保留。米斯特拉尔的特例性在于「以方言写史诗、以词典救语言」——全篇以「一人复兴一门语言」为主线。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Joseph Étienne Frédéric Mistral（奥克语名 Frederi Mistral，1830-09-08 马亚纳 ~ 1914-03-25 马亚纳，享年 83 岁——生于斯葬于斯）
- **气质关键词**：**普罗旺斯的荷马、语言的复活者、罗讷河畔的农夫诗人** —— 1904 诺贝尔文学奖官方获奖理由：
  > EN: "in recognition of the fresh originality and true inspiration of his poetic production, which faithfully reflects the natural scenery and native spirit of his people, and, in addition, his significant work as a Provençal philologist"
  > 中译：表彰其诗作的新颖独创与真切灵感，忠实反映了其民族的自然风光与本土精神；并表彰其作为普罗旺斯语文学家的杰出工作（引自 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）
- **设计母题**：**密史脱拉北风与罗讷河谷（Mistral 风 + Crau 平原 + 阿尔勒）**。其姓氏即普罗旺斯著名的北风——视觉母题用「被风吹弯的橄榄树/稻浪 + 罗讷河蓝 + 阿尔勒石城暖色」，呼应《Mirèio》中阳光与热病交织的乡土史诗。
- **本地数据源**：`literature/presentations/pages/20th_century/Frédéric_Mistral/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Mistral （肖像：第 0 步**待下载**，正文有职业期肖像；另有阿维尼翁 plaque、阿尔勒/戛纳雕像插图）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面已抓取到上述路径（本提示词即其事实基准，第一轮已核对）：
  - 生卒：1830-09-08 生于马亚纳（罗讷河口省）~ 1914-03-25 卒于马亚纳，享年 83；父 François Mistral 来自圣雷米（富有的农场主），母 Adelaide Poulinet；「Frederi」之名为纪念早逝的信差少年；1471 年先祖 Mermet Mistral 已居马亚纳
  - 教育：约 9 岁才入学，逃学后被送圣米歇尔-德里戈莱寄宿学校（Donnat 先生主办）；尼姆获业士；1848–1851 在艾克斯普罗旺斯习法律
  - 语言：法语、奥克语（普罗旺斯语）；本名两种拼写（Mistralian 正字法 Frederi Mistral / 古典正字法 Frederic Mistral）
  - 运动：1854-05-21 与师友七人共创 **Félibrige**（菲列布里什）文学文化协会，主保圣女 Estelle，接纳被伊莎贝尔二世驱逐的加泰罗尼亚诗人；七创始人为 Roumaniho（Roumanille）、Frederi Mistral、Teodor Aubanel、Ansèume Matiéu、Jan Brunet、Anfos Tavan、Paul Giera；Félibrige 存续至今（「奥克语区」32 省）；另为马赛学院（Académie de Marseille）成员
  - 词书：《Lou Tresor dóu Felibrige》（1878–1886）两卷本奥克-法双语词典，收录 oc 全部方言，至今最全面可靠的奥克语词典；排版与修订之功归于 François Vidal
  - 名作：**《Mirèio》**（Mireille，1859，八年磨一剑）十二歌长诗：Mireille 与贫篮匠 Vincent 之恋，家长阻挠后奔往圣玛丽-德拉梅尔祈祝，忘带遮阳帽中暑而死；诗中织入塔拉斯克龙、阿尔勒维纳斯等地志民俗；题献拉马丁（献词：It is my heart and my soul...）；译成约 15 种欧洲语言（含米斯特拉尔自译法文）；1863 古诺改编为歌剧《Mireille》
  - 诺贝尔：1904（乌普萨拉大学两位教授提名），与埃切加赖**平分奖金**；米斯特拉尔将其一半捐建阿尔勒博物馆 **Museon Arlaten**（最重要的普罗旺斯民俗收藏）；另获 Légion d'honneur（以纯地方性成就获此国家级荣誉，殊例）
  - 家庭：1876 在第戎主教座堂娶勃艮第女子 Marie-Louise Rivière（1857–1943），无子女
  - 身后：1930-04-06 诞辰百年，戛纳立 Tuby Victor 雕像（普罗旺斯寓意像向其献书）
  - 关键时间线（16 节点）：1830 生于马亚纳 → 约 9 岁入学/寄宿 Frigolet → 尼姆业士 → 1848–1851 艾克斯习法律 → 立志复兴普罗旺斯语（「以神圣诗歌之气焰恢复普罗旺斯」）→ 1854-05-21 共创 Félibrige → 1859《Mirèio》→ 拉马丁盛赞（Cours familier de littérature 第 40 期）→ 1867《Calendau》/《Coupo Santa》→ 1875《Lis Isclo d'or》→ 1876 娶 Marie-Louise Rivière → 1878–1886《Lou Tresor dóu Felibrige》→ 1884《Nerto》→ 1890《La Rèino Jano》→ 1897《Lou Pouèmo dóu Rose》→ 1904 诺贝尔文学奖（与 Echegaray 平分）+ 捐建 Museon Arlaten → 1906《Moun espelido, Memòri e Raconte》（回忆录）→ 1910《La Genèsi》→ 1912《Lis óulivado》→ 1914-03-25 卒于马亚纳

### 第 1–3 步：建目录 / 复制 Makefile / 收图 【模板通用】

- 在 `literature/presentations/20th_century/Frédéric_Mistral/` 建目录与 `images/`；Makefile `MAIN=Frédéric_Mistral_zh`；肖像第 0 步下载。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | provençal poetry | 普罗旺斯语诗歌 | 以奥克语普罗旺斯方言写史诗 | 核心页 |
| 1 | occitan philology | 奥克语语文学 | 获奖理由明载的「普罗旺斯语文学家」工作 | 语文学页 |
| 2 | lexicography | 词典学 | 《Lou Tresor dóu Felibrige》两卷双语词典 | 词书页 |
| 3 | epic poetry | 史诗 | 《Mirèio》十二歌，拉马丁称「真荷马」 | 史诗页 |
| 4 | folklore | 民俗学 | Museon Arlaten 普罗旺斯民俗博物馆创设 | 遗产页 |

#### 4.1 入库操作

- `MySQL/data/Frédéric_Mistral.yaml`（name_en=`Frédéric Mistral`，qid=Q42596，primary_occupation=`writer`），`python3 seed_person.py 'data/Frédéric_Mistral.yaml'`。
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id JOIN people p ON p.id=pf.person_id WHERE p.qid='Q42596' ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | José Echegaray | 无向 | 1904 诺贝尔文学奖共同得主，平分奖金 |
| spouse | Marie-Louise Rivière | 无向 | 1876 年第戎成婚，无子女 |
| advisor-student | Joseph Roumanille | 师→生（老师） | 其老师之一，后并肩共创 Félibrige |
| colleague | Joseph Roumanille | 无向 | 1854 Félibrige 七创始人之一 |
| colleague | Teodor Aubanel | 无向 | Félibrige 七创始人之一 |
| colleague | Anselme Matthieu | 无向 | Félibrige 七创始人之一 |
| colleague | Jan Brunet | 无向 | Félibrige 七创始人之一 |
| colleague | Anfos Tavan | 无向 | Félibrige 七创始人之一 |
| colleague | Paul Giera | 无向 | Félibrige 七创始人之一 |
| colleague | Alphonse Daudet | 无向 | 终生挚友，《磨坊书简》中〈诗人米斯特拉尔〉一文盛赞 |
| colleague | François Vidal | 无向 | 《Lou Tresor dóu Felibrige》排版与修订功臣 |
| influence | Alphonse de Lamartine | 对方为思想影响者 | 因其盛赞《Mirèio》而成名，《米瑞伊》即题献给他 |

> **不入库并注明**：Charles Gounod（1863 据其诗改编歌剧《Mireille》）属作品改编关系；乌普萨拉两位提名教授、罗曼维尔人氏等无实载个人互动，均不入库。

#### 4.5.1 入库操作

- yaml `relations` 与上表完全一致；stub 不编造 qid；对手方用规范全名。
- 校验：`SELECT r.type, p2.name_en FROM person_relation r JOIN people p ON p.id=r.from_id JOIN people p2 ON p2.id=r.to_id WHERE p.qid='Q42596' OR p2.qid='Q42596'`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：南法烈日、河谷金黄、方言之根
- **配色**：主色普罗旺斯赭褐 `#4E342E` + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 普罗旺斯语诗歌 — 烈日橙 `#D97B29`
  - `badgeB` 奥克语语文学 — 橄榄绿 `#5B6E3A`
  - `badgeC` 史诗 — 罗讷蓝 `#2E5E77`
  - `badgeD` 民俗/博物馆 — 陶土红 `#A34A2A`
- **背景母题**：稀疏暖色大圆（日光/麦垛）+ 斜向风纹线条（密史脱拉北风），四档错落。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + 姓名小字注；底部状态栏 `国籍 | 语言 | 主要奖项`。
2. **身份信息页（★ 必做）**：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、运动、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`；法文字符 é/è 与奥克语字符 ó/ò 直接 XeLaTeX 排版。
4. 无公式框：以**《Mirèio》题献拉马丁献词引文框**（page.md 实载英文译文）与**《Lou Tresor dóu Felibrige》书影/词典条目图式**替代。

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 普罗旺斯的荷马 / Frédéric Mistral 1830–1914 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 诗歌 / 语文学 / 词典 / 民俗四徽章
04  马亚纳少年 (1830–1851) — 农场主之家、Frigolet 寄宿、尼姆业士、艾克斯习法
05  立志：复兴普罗旺斯语 — 「第一文学语言」宣言、race 之释义（语言·土地·历史）
06  Félibrige 创建 (1854) — 七创始人、主保圣女、加泰罗尼亚诗人来投
07  《Mirèio》核心贡献页 — 十二歌梗概、题献引文框、十五年译语传播
08  拉马丁的发现 — Cours familier 盛赞原文、「当代真荷马」、成名之由
09  词书工程 — Lou Tresor dóu Felibrige、七方言收录、François Vidal 之功
10  1904：诺贝尔文学奖 — 官方理由 EN+中译引文框、与埃切加赖平分、捐建 Museon Arlaten
11  晚年与身后 — 回忆录、戛纳百年像、1914 卒于故乡马亚纳
12  遗产：一门语言的复活 — Félibrige 存续至今、32 省奥克语区
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 make 编译，pdftoppm 截图检查溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Mistral 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 共享与分工 | 1904 与 **Echegaray 平分奖金**（each half），两人理由完全不同（诗与语文学 vs 西班牙戏剧传统）——本篇只写己方理由，勿写「共同获奖理由」；**必须**建 co-honored 双向关系 |
| 奖金去向 | 米斯特拉尔将其一半捐建 Museon Arlaten（阿尔勒博物馆），勿写成「捐出全部奖金」 |
| 语言身份 | 他是**法国**（国籍）**奥克语（普罗旺斯语）**作家——勿写成「法国文学」叙事主体；获奖理由明载「忠实反映其民族的自然风光与本土精神」 |
| 名字拼写 | 本名 Joseph Étienne Frédéric Mistral；奥克语名两种正字法（Frederi Mistralian / Frederic classical）——全篇以法文 Frédéric Mistral 为主，正文注一次即可 |
| Roumanille 双重关系 | 既是其**老师**又是 Félibrige **共同创始人**——两行关系（advisor-student + colleague）都要建 |
| Gounod | 歌剧改编是作品关系，勿写成师承/合作往来 |
| 拉马丁 | 盛赞与题献是实载双向互动，用 influence 类型，note 写清「因盛赞而成名、题献对象」，勿写成导师 |
| 七创始人名 | 用 Provençal 名（Jóusè Roumaniho / Teodor Aubanel / Ansèume Matiéu / Jan Brunet / Anfos Tavan / Paul Giera），yaml person 字段统一用规范法文形式 Joseph Roumanille、Teodor Aubanel、Anselme Matthieu、Jan Brunet、Anfos Tavan、Paul Giera |
| 无载禁写 | page.md 无「密史脱拉风笔名由来」的明文记载（姓氏与风同名只是语言事实），禁写；无 1904 颁奖演说细节引语；除题献词（英译实载）外勿编造中文「原话」 |
| 同名区分 | **切勿**与 Gabriela Mistral（1945 文学奖得主，智利诗人）混淆——两人仅笔名渊源传闻，本篇不展开 |

**术语清单**：

| 英文/原文 | 中文 | 风险 |
|------|------|------|
| Félibrige | 菲列布里什 | 七创始人文学协会，勿译「费利布里热派」泛称 |
| Mirèio / Mireille | 《米瑞伊》 | 普罗旺斯文/法文两形 |
| Lou Tresor dóu Felibrige | 《菲列布里什宝库》 | 1878–1886 两卷词典 |
| Provençal | 普罗旺斯语 | 奥克语方言 |
| Occitan | 奥克语 | 上位语言名 |
| Museon Arlaten | 阿尔勒博物馆 | 普罗旺斯民俗收藏 |
| Mistral (wind) | 密史脱拉北风 | 设计母题，姓氏同名 |
| Cours familier de littérature | 《文学家常谈》 | 拉马丁期刊，第 40 期盛赞 |
| Coupo Santa | 《圣杯歌》 | 1867，Félibrige 之歌 |
| Mes Origines / Moun espelido | 《我的出身》回忆录 | 1906（1907 英译 Memoirs of Mistral） |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions
- **匹配理由**：
  - 「怀旧」贴合全篇母题——为一种「正在死去的语言」招魂，普罗旺斯的旧日荣光是全书的乡愁
  - 温暖悠长的旋律匹配《Mirèio》的田园史诗气质与罗讷河谷的日光
  - 「回望」气质匹配回忆录作者身份与「生于斯卒于斯」的一生闭环
- **本地路径**：对照 `music_audio/curated_tracks.md` 中 alex-productions Nostalgia 条目复制到本目录。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Frédéric_Mistral/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 官方理由中译（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |
