# 和平奖得主立传提示词（OpenPeace 批次 9：Emily Greene Balch）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Emily Greene Balch（艾米莉·格林·巴尔奇，1946 诺贝尔和平奖得主、WILPF 首任国际司库）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Emily Greene Balch（艾米莉·格林·巴尔奇，1867–1961），美国经济学家、社会学家与和平主义者。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页）与「事业领域」的结构化表达；Balch 的一生有「学院经济学者 → 和平运动中枢 → 终生国际主义者」的长弧叙事，以「从讲台到国际和平组织」为叙事主轴——1919 年被 Wellesley 终止合约，反而把她推向世界舞台，这是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：Emily Greene Balch（1867-01-08 波士顿 Jamaica Plain ~ 1961-01-09 剑桥，享年 94 岁，卒于 94 岁生日次日）
- **气质关键词**：**学院派和平主义者、WILPF 首任国际司库、跨越国界的经济学者** —— 1946 诺贝尔和平奖获奖理由：
  > "for her lifelong work for the cause of peace"（表彰她毕生为和平事业所做的工作）
- **设计母题**：**跨越国界的教室（classroom without borders）**。从 Wellesley 讲台到 WILPF 的和平暑期学校、从 50 余国的分部网络到《走向人类大同》的诺奖演讲——「教育与组织的网络」是比「和平鸽」更贴合 Balch 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Emily_Greene_Balch/page.md`（含 frontmatter QID Q215139）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Emily_Greene_Balch` 四件套到 `peace/presentations/pages/20th_century/Emily_Greene_Balch/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1867-01-08 生于马萨诸塞州 Boston Jamaica Plain ~ 1961-01-09 逝于马萨诸塞州 Cambridge，享年 94 岁；卒于 94 岁生日次日）
  - 家庭（出身名门 Yankee 家庭；父 Francis V. Balch 为成功律师、曾任联邦参议员 Charles Sumner 的秘书；母 Ellen née Noyes；终身未婚）
  - 教育（Bryn Mawr College 1889 年毕业，广读古典学与语言、专注经济学；巴黎研究生工作，成果 1893 年出版 *Public Assistance of the Poor in France*；后就读 Harvard University、University of Chicago、University of Berlin；波士顿睦邻安置工作）
  - 任职（Wellesley College 1896 年起任教；1913 年继 Katharine Coman 辞职后任经济学教授——由副教授升任政治经济学与政治及社会科学教授；多个州委员会委员，含首个女性最低工资委员会；妇女工会联盟领导人；1919 年 Wellesley 终止其合约；后任 *The Nation* 编辑）
  - 核心事业清单（①移民/消费/女性经济角色的研究与《Our Slavic Fellow Citizens》1910 ②一战爆发后转入和平运动，与 Jane Addams 合作创建 Woman's Peace Party ③1919 国际妇女大会核心人物，组织更名 WILPF 定址日内瓦，任首任国际司库 ④创办和平教育暑期学校、在 50 余国建立新分部 ⑤与国际联盟合作（药物管制/航空/难民/裁军）⑥1946 诺贝尔和平奖，奖金捐给 WILPF）
  - 关键荣誉（Nobel Peace Prize 1946，与 John Mott 共享；诺奖演讲 1948-04-07 *Toward Human Unity or Beyond Nationalism*）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Emily_Greene_Balch/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Emily_Greene_Balch_zh`、`VIDEO_NAME=Emily_Greene_Balch_zh`

### 第 3 步：收集图片 【人物专属】

- ⚠️ 本地 `images.txt` **无真实肖像**（仅 Wiki 徽标图）——封面与身份信息页用**装饰圆占位**（主色环 + 姓名首字母或和平鸽/地球意象）
- 陷阱：勿把 Wikiquote/Wikisource 徽标误作肖像下载

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international peace movement | 国际和平运动 | WILPF 首任国际司库、50 余国分部 | WILPF 页 |
| 1 | peace education | 和平教育 | 创办和平暑期学校 | WILPF 页 |
| 2 | immigration studies | 移民研究 | 《Our Slavic Fellow Citizens》1910、移民/消费研究 | 学术页 |
| 3 | women's labor rights | 女性劳动权利 | 妇女工会联盟领导人、首个女性最低工资委员会 | 社会改革页 |
| 4 | economics | 经济学 | Wellesley 政治经济学教授、法国公共救助研究 | 学院页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 6 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | John Mott | 无向 | 1946 诺贝尔和平奖共同得主 |
| colleague | Jane Addams | 无向 | Woman's Peace Party 与多个团体的合作者；《Women at the Hague》合著者 |
| colleague | Katharine Coman | 无向 | Wellesley 经济学系创始者；1913 Balch 继其辞职后任经济学教授 |
| colleague | Alice Hamilton | 无向 | 《Women at the Hague》1915 三合著者之一 |
| parent-child | Francis V. Balch | 无向 | 父亲，成功律师，曾任参议员 Charles Sumner 秘书 |
| parent-child | Ellen Noyes Balch | 无向 | 母亲（née Noyes） |

- 方向约定：co-honored/colleague/parent-child 无向自动 from<to 归一
- 对手方 name_en 用 manifest 规范名；缺失人物由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：坚韧、克制、绵长的理想主义
- **配色**：深绯红（manifest 预分配主色 `#7E1E23`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeWILPF` 国际和平运动 — 深蓝 `#1F4E79`
  - `badgeEdu` 和平教育 — 青绿 `#0E6B5C`
  - `badgeMigrant` 移民与劳动 — 赭金 `#8C6A2F`
  - `badgeNobel` 1946 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 低饱和的越洋信笺与分部网络连线意象，呼应「跨越国界的教室」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有视觉主体**：右上角装饰圆占位（主色环 + 姓名首字母），`draw=coveraccent!50` 细边框。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（United States），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧装饰圆 + 右侧信息网格，含至少：生卒、出生地、国籍、家庭（父/母）、教育（Bryn Mawr/巴黎/Harvard/Chicago/Berlin）、任职、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 毕生和平事业 / Emily Greene Balch 1867–1961 + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右信息网格（含家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 学院经济学者 / 社会改革 / WILPF / 和平教育 / 1946 诺奖
04  早年：Jamaica Plain 的名门之女 (1867–1889) — 律师父亲与 Sumner 秘书家世、Bryn Mawr 1889
05  求学欧洲与社会工作 (1889–1896) — 巴黎研究 1893 出版、Harvard/Chicago/Berlin、波士顿睦邻安置
06  Wellesley 讲台 (1896–1913) — 移民/消费/女性经济角色、1910《Our Slavic Fellow Citizens》
07  教授与社会改革 (1913–1919) — 继 Coman 任教授、州最低工资委员会、妇女工会联盟
08  转入和平运动 (1914–1919) — 与 Jane Addams 合作、Woman's Peace Party、Ford 调停委员会、反征兵立场
09  讲台的终点与新生 (1919) — Wellesley 终止合约、*The Nation* 编辑、1921 版依贵格会
10  WILPF 首任国际司库 (1919–) — 日内瓦总部、50 余国分部、和平暑期学校、与国际联盟合作
11  二战中的立场 (1939–1945) — 支持盟国、不批评战争努力、维护良心拒服兵役者权利（客观呈现）
12  1946 诺贝尔和平奖 — 与 John Mott 共享、Randall 夫妇与五团体提名运动、奖金捐给 WILPF
13  晚年与遗产 — 1948 诺奖演讲《Toward Human Unity or Beyond Nationalism》、终身未婚、卒于 94 岁生日次日
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Balch 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由拆分 | 1946 与 John Mott 共享但**理由各写各的**——Balch 用 "for her lifelong work for the cause of peace"，Mott 的宗教兄弟会理由是另一句，勿混入本篇 |
| 共享获奖者 | 与 Mott 事业互不隶属（一位是 WILPF 经济学者、一位是 YMCA/WSCF 领袖），勿写「与 Mott 合作获奖」 |
| WILPF 成立口径 | 1919 国际妇女大会（International Congress of Women）更名 WILPF、定址日内瓦；Balch 任**首任国际司库（Secretary-Treasurer）**，勿写成「创始人」或「主席」 |
| 离职口径 | Wellesley 1919 年终止其合约（terminated her contract）；勿写成「辞职」或「被解雇镇压」的评价性表述 |
| 版依贵格 | 1921 年由 Unitarianism 改宗 Quakerism；信中 "the ways of Jesus" 与贵格崇拜引语为 page.md 明载英文原文，可直接引用；宗教内容客观记录不加评价 |
| 二战立场 | 支持盟国且不批评战争努力、同时支持良心拒服兵役者权利——两组事实并列呈现，勿简化为单一立场 |
| 提名运动 | John Randall 与 Mercedes Randall 发起、五团体组成提名委员会（WILPF/National Federation of Settlements/Women's Trade Union League of America/National Council of Women of the US/NAACP），数字与名单勿增删 |
| 奖金去向 | 她把自己那份奖金捐给 WILPF；勿写「捐出全部奖金」或「捐给红十字会」 |
| 无载禁写 | 不编造导师（三校进修无导师记载）、不写恋情与婚约（终身未婚）、不从诺奖颁奖词反推关系、不写 WILPF 内部人事纠纷 |
| 术语 | 政治敏感内容（战争、征兵、审查立法）只作 page.md 明载的客观事实记录，不加任何评价性语句 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| WILPF | 妇女国际和平与自由联盟 | Women's International League for Peace and Freedom，1919 定名 |
| Secretary-Treasurer | 国际司库 | Balch 是首任，非主席 |
| Woman's Peace Party | 妇女和平党 | 与 Jane Addams 合作创建 |
| settlement movement | 睦邻安置运动 | 波士顿安置工作与穷苦移民帮扶 |
| Our Slavic Fellow Citizens | 《我们的斯拉夫同胞》 | 1910 社会学专著，536 页 |
| conscientious objector | 良心拒服兵役者 | 一战与二战两度为其权利发声 |
| neutral mediation | 中立调停 | Ford 国际调停委员会（中立持续调停会议的后续组织） |
| Toward Human Unity or Beyond Nationalism | 《走向人类大同》 | 1948-04-07 诺奖演讲标题 |
| Public Assistance of the Poor in France | 《法国的贫民公共救助》 | 1893，巴黎研究生成果 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Empire Collapse** — Cold Cinema（manifest 预分配，勿改）
- **风格**: 史诗鼓阵 / 沉郁 / 时代转折感
- **匹配理由**:
  - "Empire Collapse" 呼应 Balch 的事业时代底色——旧帝国秩序在两次世界大战中崩塌，她以「超越国族主义」（Beyond Nationalism）回应废墟，WILPF 是新秩序的草稿
  - 曲名的沉郁感匹配其气质：从被学院除名到国际运动中枢，理想主义在低谷中绵长推进
- **本地路径**: `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` → `presentations/20th_century/Emily_Greene_Balch/Empire_Collapse.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Emily_Greene_Balch/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/Emily_Greene_Balch/images.txt` | 插图 URL（无肖像，用装饰圆占位） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Emily_Greene_Balch.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
