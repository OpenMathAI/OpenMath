# 文学家立传提示词（OpenLiterature：José Echegaray）

> **本文件是何塞·埃切加赖（1904 诺贝尔文学奖）的人物专属立传提示词**，结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容按文学家适配：无公式框，以**代表作书影/名句引文框/意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各学科侧共享体系）。
- **本实例**：José Echegaray（何塞·埃切加赖），1904 诺贝尔文学奖得主（与 Frédéric Mistral 共享），**西班牙首位诺奖得主**——土木工程师、数学家、政治家与剧作家的罕见四重身份。
- **设计哲学**：文学家立传以**作品意象与文学史脉络**替代公式与实验——身份信息页（★ 必做）与「文学领域」结构化表达仍须保留。埃切加赖的特例性在于「几何头脑写 melodrama」：全篇以「责任与道德的戏剧」为主线，用工程/数学元素做视觉点缀。

---

## 二、背景信息 【人物专属】

- **目标文学家**：José Echegaray y Eizaguirre（1832-04-19 马德里 ~ 1916-09-14 马德里，享年 84 岁）
- **气质关键词**：**西班牙首位诺奖、黄金时代的复兴者、写剧的工程师** —— 1904 诺贝尔文学奖官方获奖理由：
  > EN: "in recognition of the numerous and brilliant compositions which, in an individual and original manner, have revived the great traditions of the Spanish drama"
  > 中译：表彰其大量辉煌的创作，以个人化而独创的方式复兴了西班牙戏剧的伟大传统（引自 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）
- **设计母题**：**舞台上的几何（theatre + geometry）**。工程师出身的剧作家——视觉母题用「戏剧舞台拱框 + 透视作图线（descriptive geometry）」，深蓝幕布衬金色直线，呼应其「以理性之笔写激情悲剧」的双面人生。
- **本地数据源**：`literature/presentations/pages/20th_century/José_Echegaray/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Jos%C3%A9_Echegaray （肖像：第 0 步**待下载**，正文有 JoseEchegaray.jpg 1904 照）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面已抓取到上述路径（本提示词即其事实基准，第一轮已核对）：
  - 生卒：1832-04-19 生于马德里 ~ 1916-09-14 卒于马德里，享年 84；葬圣伊西德罗公墓；父为医生兼中学希腊文教师（阿拉贡人），母纳瓦拉人；童年在穆尔西亚度过
  - 教育：自幼在穆尔西亚学院爱上数学（读 Goethe/Homer/Balzac 与 Gauss/Legendre/Lagrange 交替）；14 岁赴马德里考入道路运河港埠工程学校（Escuela de Caminos, Canales y Puertos），20 岁以**全班第一**获土木工程学位；首份工作赴阿尔梅里亚与格拉纳达
  - 学术：1854 起在工程学校任教（数学、立体几何、画法几何、水力学、微分与物理演算，至 1868），兼秘书；1858–1860 兼公共工程助理学校教授；著作《Problemas de geometría analítica》（1865）、《Teorías modernas de la física. Unidad de las fuerzas materiales》（1867）颇获好评；政治经济学会会员，协创杂志《La Revista》，鼓吹自由贸易
  - 政治：1868 光荣革命后弃教从政，共和激进民主党创始成员，历任教育大臣、公共工程大臣、财政大臣（1867–1874 间相继任职），1874 波旁复辟后退出政坛
  - 文学：1867 已有《La Hija natural》《La Última Noche》，1874 年起真正成为剧作家；主题母题是**责任与道德的困境**；复现西班牙黄金时代成就，多产剧作家
  - 关键荣誉：Nobel 文学奖 1904（西班牙学院成员提名，**西班牙首位诺奖得主**，与 Mistral 共享）；西班牙皇家学院 e 席（1894-05-20 就任至 1916 卒）；金羊毛骑士勋章等
  - 身后：马德里「文学街区」Calle Echegaray 等多条街道命名；1971 西班牙银行 1000 比塞塔纸币
  - 关键时间线（16 节点）：1832 生于马德里 → 穆尔西亚童年（数学启蒙）→ 14 岁赴马德里 → 20 岁工程学校第一名毕业 → 阿尔梅里亚/格拉纳达工程任职 → 1854 工程学校教席（至 1868）→ 1865《Problemas de geometría analítica》→ 1867《Teorías modernas de la física》+ 早期两剧 → 1868 光荣革命入阁 → 1869–1874 教育大臣/公共工程大臣/财政大臣 → 1874 波旁复辟退出政坛 → 1874《El libro talonario》《La esposa del vengador》（剧作家元年）→ 1877《O locura o santidad》→ 1881《El gran Galeoto》→ 1894 西班牙皇家学院 e 席 → 1904 诺贝尔文学奖（与 Mistral 共享）→ 晚年 25–30 卷数学物理著作 → 1916-09-14 卒于马德里

### 第 1–3 步：建目录 / 复制 Makefile / 收图 【模板通用】

- 在 `literature/presentations/20th_century/José_Echegaray/` 建目录与 `images/`；Makefile `MAIN=José_Echegaray_zh`；肖像第 0 步下载。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | spanish drama | 西班牙戏剧 | 复兴黄金时代伟大传统，获奖核心 | 核心页 |
| 1 | moral dilemma drama | 道德困境剧 | 责任与道德困境为其剧作母题 | 母题页 |
| 2 | melodrama | 情节剧 | 《El gran Galeoto》的十九世纪 grand manner | 名作页 |
| 3 | mathematics | 数学 | 工程学校教授、解析几何与物理理论著作 | 学者页 |
| 4 | mathematical physics | 数学物理 | 晚年 25–30 卷数学物理著述 | 晚年页 |

#### 4.1 入库操作

- `MySQL/data/José_Echegaray.yaml`（name_en=`José Echegaray`，qid=Q127349，primary_occupation=`writer`），`python3 seed_person.py 'data/José_Echegaray.yaml'`。
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id JOIN people p ON p.id=pf.person_id WHERE p.qid='Q127349' ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Frédéric Mistral | 无向 | 1904 诺贝尔文学奖共同得主，平分奖金 |

> **入库例外说明（relations=1）**：page.md 明载的个人社会关系仅此一条——正文无配偶、无师承、无明载同人社群（西班牙皇家学院/政治经济学会为机构任职，RaE 前后任 Mesonero Romanos/Burell 为席位传承非个人关系）。按 workflow「实在无载者除外并注明」执行。童年阅读的 Goethe/Homer/Balzac 与 Gauss/Legendre/Lagrange 属阅读对象非关系；Verónica Echegui 为现代远亲无关系类型。

#### 4.5.1 入库操作

- yaml `relations` 与上表一致；Mistral 已由本批先行入库（Q42596），按名匹配幂等。
- 校验：`SELECT r.type, p2.name_en FROM person_relation r JOIN people p ON p.id=r.from_id JOIN people p2 ON p2.id=r.to_id WHERE p.qid='Q127349' OR p2.qid='Q127349'`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：幕布的深邃、理性的锋利、黄金时代的余晖
- **配色**：主色深海蓝 `#0F4C5C` + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 西班牙戏剧 — 斗牛红 `#A31621`
  - `badgeB` 道德困境剧 — 暮紫 `#52307C`
  - `badgeC` 数学/工程 — 钢青 `#2E6E8E`
  - `badgeD` 政治/大臣岁月 — 石板灰 `#5A6470`
- **背景母题**：深蓝大圆（幕布灯晕）+ 细金色透视线（几何作图），四档错落。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像（1904 照）+ 姓名小字注；底部状态栏 `国籍 | 身份 | 主要奖项`。
2. **身份信息页（★ 必做）**：左头像 + 右信息网格（生卒、国籍、出生地、教育、多重职业、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`；西文字符 é/í 直接 XeLaTeX 排版。
4. 无公式框：以**《El gran Galeoto》剧名题版书影**与**83 岁自况引文框**（page.md 实载英文原句：I cannot die, because if I am going to write my mathematical physics encyclopedia, I need at least 25 more years）替代。

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 写剧的工程师 / José Echegaray 1832–1916 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 西班牙戏剧 / 道德困境剧 / 数学 / 数学物理四徽章
04  穆尔西亚少年 (1832–1846) — 医生之家、数学启蒙、文学与算学交替阅读
05  工程师之路 — 14 岁赴马德里、20 岁第一名毕业、外省工程岁月
06  工程学校教授 (1854–1868) — 画法几何与水力学、两部专著、自由贸易论战
07  革命与大臣 (1868–1874) — 三任大臣、波旁复辟退场（客观简述）
08  剧作家元年 (1874) — 政坛谢幕与文学登场、责任与道德的母题
09  《El gran Galeoto》核心贡献页 — melodrama 群像、流言之毒、默片《The World and His Wife》
10  剧作星表 — O locura o santidad、Mariana、La duda、El loco Dios（精选 5 部）
11  1904：诺贝尔文学奖 — 官方理由 EN+中译引文框、西班牙首位、与 Mistral 共享
12  晚年与身后 — 83 岁自况引文、25–30 卷数学物理、皇家学院 e 席、1916 卒、街道与纸币
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 make 编译，pdftoppm 截图检查溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Echegaray 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 共享与分工 | 1904 与 **Mistral 平分奖金**，理由完全不同（西班牙戏剧传统 vs 普罗旺斯诗歌与语文学）——本篇只写己方理由；**必须**建 co-honored 双向关系 |
| 西班牙首位 | 正文明载 "making him the first Spaniard to win the prize"，全篇锚点勿漏 |
| 早期剧作年份 | 叙事说《La Hija natural》《La Última Noche》均 1867，而书目列表作 1865/1875——两说并存，叙事页按正文 1867 口径、书目页照实列出，加注即可 |
| 《Locura o santidad》 | 书目有 1876《Locura o santidad》与 1877《O locura o santidad》两条，叙事页用 1877《O locura o santidad》（Saint or Madman?），勿混 |
| 大臣年份 | 正文称三职 "between 1867 and 1874"，1868 革命后入阁为实载主线——勿写成「1867 前已任大臣」的具体年份序列 |
| 政治内容 | 共和激进民主党、光荣革命、复辟退场：只按 page.md 客观事实简述，**不作政治评价** |
| 引语红线 | 全篇仅 83 岁自况一句（英文原句实载）；此外勿编造「戏剧是毕生之爱」之外的直接引语（该句为叙述转述，可转述不可加引号） |
| 关系稀缺 | page.md 无配偶/师承/明载社团同侪——**勿从「复兴黄金时代」反推与黄金时代剧作家的「影响关系」**；DB relations=1 是诚实值 |
| 同名区分 | 埃切加赖奖章（Echegaray Medal）在 awards 列表中，勿写成他设立的奖项 |

**术语清单**：

| 英文/原文 | 中文 | 风险 |
|------|------|------|
| El gran Galeoto | 《大伽利奥托》 | 1881 名剧，默片改名 The World and His Wife |
| O locura o santidad | 《疯癫抑或圣洁》 | 1877 代表剧 |
| melodrama | 情节剧 | 十九世纪 grand manner，勿译「音乐剧」 |
| Spanish Golden Age | 西班牙黄金时代 | 戏剧传统所指 |
| Escuela de Caminos, Canales y Puertos | 道路运河港埠工程学校 | 全班第一名毕业 |
| descriptive geometry | 画法几何 | 教学内容 |
| Real Academia Española | 西班牙皇家学院 | e 席，1894 就任 |
| Glorious Revolution (Spain) | 光荣革命（1868） | 政坛转折，客观表述 |
| La Revista | 《评论》杂志 | 协创刊物 |
| Maria Stuart note | — | 本篇无此条目（属比昂松篇），勿串场 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions
- **匹配理由**：
  - 「唤醒」贴合获奖理由的核心动词——**复兴（revived）**西班牙戏剧的伟大传统
  - 曲目的序曲感匹配「革命之年弃教从政、复辟之年登台写剧」的人生两幕转折
  - 昂扬而克制的气质匹配工程师剧作家的理性底色与晚年数学物理长跑
- **本地路径**：对照 `music_audio/curated_tracks.md` 中 alex-productions Awaken 条目复制到本目录。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/José_Echegaray/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 官方理由中译（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |
