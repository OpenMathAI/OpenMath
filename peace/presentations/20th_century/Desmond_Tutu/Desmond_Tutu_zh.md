# 和平奖得主立传提示词（OpenPeace 实例：Desmond Tutu）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」的批次实例**，
> 以 Desmond Tutu（1984 诺贝尔和平奖，南非反种族隔离运动领袖）为对象。
> 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节标杆）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath 数学侧、OpenPhysicist 物理侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck）与物理学家侧标杆（Kenneth G. Wilson）的提示词 + tex 结构。
- **本实例**：Desmond Mpilo Tutu（德斯蒙德·图图）。
- **设计哲学**：和平奖得主立传与科学家立传的核心差异，在于**和平事业是「行动史」而非「成果史」**——版面强调立场、演讲、谈判与和解进程的时间线叙事，同时保留科学家模板的「身份信息页」与「事业领域结构化表达」骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：Desmond Mpilo Tutu（1931-10-07 ~ 2021-12-26，享年 90 岁）
- **诺奖年份与官方获奖理由**：1984 年诺贝尔和平奖（独得）：
  > "for his role as a unifying leader figure in the non-violent campaign to resolve the problem of apartheid in South Africa"
  > （表彰他作为统一性领袖人物，在以非暴力运动解决南非种族隔离问题中发挥的作用）
  > ※ 中译以名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` 为准，禁止改写。
- **气质关键词**：**非暴力抗争的统一者、真相与和解的主持人、彩虹之国的牧者**
- **设计母题**：**彩虹（rainbow）与和解（reconciliation）**。Tutu 把后种族隔离的南非称为「彩虹之国」（Rainbow Nation）——版面以彩虹色带与握手/对话意象贯穿，呼应「黑人与白人共同构成一个家庭」的核心理念；辅助母题为 *ubuntu*（"a person is a person through other persons"）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Desmond_Tutu/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：核对本地页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Desmond_Tutu` 四件套到 `peace/presentations/pages/20th_century/Desmond_Tutu/`
- 事实基准（以本地 page.md 为准）：
  - 生卒（1931-10-07 生于德兰士瓦克勒克斯多普 ~ 2021-12-26 逝于开普敦 Oasis Frail Care Centre，享年 90 岁；2022-01-01 圣乔治座堂葬礼，水葬/静水礼 aquamation，骨灰安放于圣乔治座堂）
  - 家庭（父 Zachariah Zelilo Tutu 为卫理公会小学校长；母 Aletta Dorothea Mavoertsek Mathlare；科萨族与茨瓦纳族混血；妻 Nomalizo Leah Shenxane，1955-06-02 成婚——page.md 个人生活节明载「On 2 July 1955」，infobox 作 m. 1955；四子女 Trevor Thamsanqa / Theresa Thandeka / Naomi Nontombi / Mpho Andrea）
  - 教育（Pretoria Bantu Normal College 教师文凭 1951–1953；UNISA 函授 BA；St Peter's Theological College 神学执照 1960；King's College London 荣誉神学士 1965 + 硕士 1965-1966，硕士论文论西非伊斯兰教）
  - 任职履历（教师 1954–1955；1960-12 按立圣职/1961 司铎；1962–1966 赴伦敦；Fedsem 讲师 1967–1970；UBLS 教员 1970–1972；TEF 非洲主任 1972–1975；约翰内斯堡圣玛丽座堂主任牧长 1975–1976；莱索托主教 1976–1978；南非教会理事会 SACC 秘书长 1978–1985；约翰内斯堡主教 1985–1986；开普敦大主教 1986–1996；真相与和解委员会 TRC 主席 1996–1998；Emory 访问教授 1998–2000；The Elders 主席 2007–2013）
  - 关键荣誉（Nobel Peace Prize 1984-10-16；Martin Luther King, Jr. Nonviolent Peace Prize 1986；Pacem in Terris Award 1987；Templeton Prize 2013（£110 万）；总统自由勋章；圣雄甘地和平奖；悉尼和平奖；约 100 个荣誉学位）
  - 核心事业清单（见第 4 步）
  - 关键时间线（15–20 节点：1931 出生 → 1951 师范 → 1954 执教 → 1955 成婚 → 1960 按立 → 1962 赴伦敦 KCL → 1966 回南非 Fedsem → 1972 TEF 主任 → 1975 座堂主任牧长 → 1976 莱索托主教 → 1976-06 致信 Vorster 警告、六周后索韦托起义 → 1977 Biko 葬礼致辞 → 1978 SACC 秘书长 → 1980 护照被没收 → 1983 UDF 赞助人 → 1984-10-16 诺奖 → 1985 约翰内斯堡主教 → 1986-09-07 开普敦大主教（首位黑人） → 1988 政府禁止 17 组织、发起「你们已经输了」演讲 → 1989 开普敦和平游行 3 万人 → 1990 曼德拉获释 → 1994 大选 → 1996–1998 TRC 主席 → 1996 荣休大主教 → 2007–2013 The Elders 主席 → 2021-12-26 辞世）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Desmond_Tutu/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成例的 `Makefile`，设置 `MAIN=Desmond_Tutu_zh`、`VIDEO_NAME=Desmond_Tutu_zh`

### 第 3 步：收集图片 【人物专属】

- 优先从 `images.txt` 选真实肖像（page.md 配图含 1986 年旧金山照、1997 年华盛顿照、2007 年科隆照等，选 infobox 同源肖像 c. 2004 照）
- 下载失败则用装饰圆占位（参考历批经验：Commons `Special:FilePath` → Wikipedia REST API 回退）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Tutu 的事业领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | anti-apartheid activism | 反种族隔离运动 | 非暴力抗争与国际经济施压，1984 诺奖核心 | 封面、抗争页 |
| 1 | human rights | 人权 | SACC 时期的人权倡导与晚年全球议题 | SACC 页 |
| 2 | reconciliation | 和解 | TRC 主席、restorative justice 与 ubuntu 神学 | TRC 页 |
| 3 | Anglican theology | 圣公会神学 | 黑人神学与非洲神学的融合 | 神学页 |
| 4 | conflict mediation | 冲突调解 | 1990 转型期调停黑人派系与 ANC–Inkatha 暴力 | 转型页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en='Desmond Tutu'`），`primary_occupation='clergyman'`、`has_social_data=1`、`has_biography=0`
- 关联职业 `clergyman`（rank 0）、`theologian`（rank 1）、`writer`（rank 2，non-fiction writer）；国籍 `South Africa`
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Nomalizo Leah Shenxane | 无向 | 1955 年成婚，教师出身 |
| parent-child | Mpho Tutu van Furth | 父→女 | 四子女中最知名者，合著者与牧者 |
| influence | Trevor Huddleston | 对方→Tutu | Sophiatown 时期神长，传记家称其一生最大影响者 |
| colleague | Nelson Mandela | 无向 | 1951 辩论会初识；1980s 联名请愿；1990 调停；1995 任命其任 TRC 主席 |
| colleague | Allan Boesak | 无向 | 反种族隔离同侪，共同调解冲突与组织抗议活动 |
| colleague | F. W. de Klerk | 无向 | 1989 允许和平游行、1990 废禁令，转型期多次对话 |
| colleague | Tenzin Gyatso, 14th Dalai Lama | 无向 | 两位和平奖得主好友，《The Book of Joy》合著者 |

#### 4.5.1 入库操作

- 以 `name_en='Desmond Tutu'` 为中心写入 `person_relation`
- 方向约定：influence（Huddleston → Tutu 为思想影响者）、parent-child 有向；其余无向自动 from<to 归一
- 对手方 name_en 先查库（`SELECT id,name_en FROM people WHERE name_en LIKE '%关键词%'`）沿用库内形式；缺失人物先建占位（`has_biography=0`）
- 无载禁写：Dubai/Reagan 等仅是对立或接触关系者不入库；Huddleston 用 influence 而非 advisor-student（非神学导师）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：温暖、坚定、彩虹般的包容
- **配色**：manifest 预分配主色 **深青蓝 `#0F4C5C`** + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeAct` 反种族隔离运动 — 深红 `#A63A2B`
  - `badgeHR` 人权 — 青绿 `#0E7C7B`
  - `badgeRec` 和解/TRC — 琥珀 `#E07B30`
  - `badgeTheol` 圣公会神学 — 紫 `#52307C`
- **背景母题**：彩虹色带弧线 + 柔和实心圆（呼应「彩虹之国」与「彩虹神子民」）

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 非暴力抗争的统一者 / Desmond Tutu 1931–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、家庭、教育、任职、荣誉、核心领域）
03  核心事业概览 — 反种族隔离 / 人权 / 和解 / 神学 / 调解
04  早年：克勒克斯多普 (1931–1950) — 贫困童年、小儿麻痹症、Huddleston 的影响、结核病
05  教师岁月 (1951–1955) — 师范学院、UNISA 函授、1953《班图教育法》后弃教从神
06  伦敦岁月 (1962–1966) — KCL 神学、Golders Green 白人堂区、硕士论文
07  Fedsem 与莱索托 (1966–1972) — 首位黑人教员、Fort Hare 学潮、UBLS
08  TEF 非洲主任与 SACC 秘书长 (1972–1985) — 黑人神学论文、索韦托起义警告、护照风波
09  1984 诺贝尔和平奖 — 获奖理由原句 + 「这个奖属于……」获奖演说 + 奖金分配
10  首位黑人主教与大主教 (1985–1994) — 约翰内斯堡、开普敦、女性司铎按立、制裁呼吁
11  转型与调停 (1990–1994) — 曼德拉获释、ANC–Inkatha 暴力、1994 大选
12  真相与和解委员会 (1996–1998) — 三重路径（坦白/宽恕/补偿）、restorative justice、五卷报告
13  神学与 ubuntu — 黑人神学融合非洲神学、Rainbow Nation 概念、同性恋权利立场
14  The Elders 与晚年 (2007–2021) — 主席任内使命、Templeton 2013、荣休岁月
15  遗产与结尾 — 「非洲式共同体」的世纪遗产 + OpenMathAI 品牌口径
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）复用同目录既有成例骨架

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Tutu 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方措辞强调 "unifying leader figure in the non-violent campaign"，勿写成"因反种族隔离活动"的泛化表述；1984 为独得年份，无共同得主 |
| 获奖日期 | 1984-10-16 授奖（page.md Honours 节明载），颁奖典礼 12 月在奥斯陆，勿混 |
| 首位黑人 | 约翰内斯堡主教（1985）与开普敦大主教（1986）两职均为首位黑人担任，勿写成"南非圣公会首位黑人大主教"的模糊口径 |
| SACC 时间 | 1978-03 接任 SACC 秘书长（John Rees→John Thorne→Tutu 接替链），任期 1978–1985，勿写成 1976 |
| 莱索托主教 | 1976-03 当选、1976-08 于 Maseru 登位，7 个月座堂主任牧长任期勿并入主教任期 |
| 获奖演说引语 | "This award is for mothers..." 为 page.md 实载原文，可整段引用；其余引语须核对原文 |
| 政治敏感 | 批评里根/撒切尔/姆贝基/祖马、以色列–巴勒斯坦议题、反犹争议指控等一律只作 page.md 明载的客观事实记录，不加评价；避免大段政治引语 |
| TRC 三重路径 | confession / forgiveness(amnesty) / restitution 三分法是 Tutu 本人提出，勿写错层次；TRC 17 名委员、Boraine 为副手 |
| Rainbow Nation | 首次使用于 1989（"rainbow people of God"），勿把概念发明权写成 Mandela |
| The Elders | Tutu 是主席（2007–2013）而非创始人，勿把"put together"写成"由他创办" |
| 子女 | 四子女均具名，但除 Mpho Tutu van Furth 外无独立事迹展开，个人生活页一句带过 |
| 去世细节 | 2021-12-26 逝于开普敦 Oasis Frail Care Centre；aquamation（水葬）与骨灰安放圣乔治座堂，勿写"火葬" |
| 著作 | 《No Future Without Forgiveness》1999 写 TRC；《The Book of Joy》2016 与达赖喇嘛合著，勿漏 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| apartheid | 种族隔离 | 南非专用制度名，勿泛译"隔离政策" |
| ubuntu | 乌班图 | "a person is a person through other persons" |
| Truth and Reconciliation Commission | 真相与和解委员会 | 缩写 TRC，南非 1995–1998 |
| Archbishop of Cape Town | 开普敦大主教 | 南非圣公会最高圣职 |
| South African Council of Churches | 南非教会理事会 | 缩写 SACC，勿译"南非常理会" |
| Black theology | 黑人神学 | 与 African theology（非洲神学）区分 |
| restorative justice | 恢复式司法 | 与报应式司法（retributive）相对 |
| Rainbow Nation | 彩虹之国 | 1989 "rainbow people of God" 的延伸 |
| non-violent campaign | 非暴力运动 | 诺奖理由核心词 |
| consecration | 主教祝圣 | 1976 由 Bill Burnett 主礼 |
| Dean of St Mary's Cathedral | 圣玛丽座堂主任牧长 | 1975 首位黑人担任 |
| Disinvestment | 撤资运动 | 国际经济施压手段 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Daylight** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 明亮 / 温暖 / 希望
- **匹配理由**:
  - "Daylight"（白昼/破晓）契合 Tutu 的核心气质——在最黑暗的种族隔离岁月中坚持非暴力与希望，并最终迎来 1994 的「彩虹之国」破晓
  - 温暖明亮的基调匹配其幽默、亲和、牧者式的人格（Du Boulay 所谓 "typical African warmth"）
  - 纪录片感适合「教师→司铎→SACC→大主教→TRC→The Elders」的行动史叙事
- **本地路径**: `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` → `presentations/20th_century/Desmond_Tutu/Daylight.wav`
- **时长**: 以实际文件为准，16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Desmond_Tutu/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/presentations/cover/openpeace_page.tex` | 项目首页模板 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID → name_en 匹配） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；政治敏感内容只作客观事实记录。**
