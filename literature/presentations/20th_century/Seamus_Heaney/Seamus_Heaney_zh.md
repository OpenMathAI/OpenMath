# 文学家立传提示词（OpenLiterature：Seamus Heaney）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Seamus Heaney（谢默斯·希尼），1995 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对希尼，即「铁锹与笔」：以泥炭沼泽、农场劳作与北爱尔兰乡村的声音质地承载「日常的奇迹与活着的过去」；其一生亦是抒情之美与伦理深度的双重证明，北爱尔兰时局仅作背景**客观简述、不作政治评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Seamus Justin Heaney（谢默斯·希尼，1939-04-13 ~ 2013-08-30），爱尔兰诗人、剧作家、翻译家，1995 年诺贝尔文学奖得主；Robert Lowell 称其为「自叶芝以来最重要的爱尔兰诗人」；2013 年逝世时《独立报》称其为「大概是世界上最著名的诗人」。
- **设计哲学**：以「用笔挖掘」为核心叙事——《挖掘》（Digging）中「粗短的笔 resting 在拇指与食指之间，我将用它挖掘」是全部创作的自况；泥炭、马铃薯、农场与「活着的过去」构成视觉母题。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Seamus Justin Heaney（谢默斯·希尼，1939-04-13 ~ 2013-08-30，享年 74 岁）
- **官方获奖理由（Nobel 1995，禁止改写）**：
  > "for works of lyrical beauty and ethical depth, which exalt everyday miracles and the living past"
  > （表彰其兼具抒情之美与伦理深度的作品，颂扬日常的奇迹与活着的过去）
- **气质关键词**：**泥炭的挖掘者、北爱尔兰的声音、日常奇迹的颂者**
- **设计母题**：**铁锹与笔（the spade & the pen）**。祖父与父亲在 Toner's bog 挖掘泥炭的画面与「我将用笔挖掘」的诗行对位；莫斯鲍恩（Mossbawn）农舍、四英尺棺木（Mid-Term Break）、沼泽里的船骸与都柏林桑迪蒙特的书房构成时间纵深的意象链。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Seamus_Heaney/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Seamus_Heaney
- **肖像**：第 0 步优先用 page.md 内嵌图 `SeamusHeaneyLowRes.jpg`（1970）或 `Seamus_Heaney_Photograph_Edit.jpg`（2009）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1939-04-13 生于北爱尔兰 Londonderry 郡 Castledawson 附近 Tamniaran 的家宅 Mossbawn ~ 2013-08-30 逝于都柏林 Blackrock Clinic（短期病痛；在都柏林一家餐厅外摔倒后入院，手术前晨 7:30 去世），享年 74 岁；创作期 1966–2013。
- **家庭与童年**：九子女中的长子；父 Patrick Heaney（1986-10 卒）为农民兼牛贩（James 与 Sarah Heaney 十个孩子中的第八个）；母 Margaret Kathleen McCann（1911–1984）娘家在亚麻作坊做工——希尼自陈「父系代表的乡村盖尔过去与母系代表的工业化阿尔斯特之间的内在张力」；1953 年幼弟 Christopher 车祸身亡（四岁），《Mid-Term Break》即写此事；同年全家迁往邻近的 Bellaghy。
- **教育**：Anahorish 小学 → 12 岁获奖学金入 Derry 的 St Columb's College（天主教寄宿学校）→ 1957 入贝尔法斯特女王大学英语语言文学，1961 一等荣誉毕业 → St Joseph's 师范学院教师认证。
- **文学起点**：在女王大学读到 Ted Hughes 的 *Lupercal*，「当代诗歌的素材忽然就是我自己生活的素材」；任教 St Thomas' 中学期间结识校长 Michael McLaverty（Monaghan 郡作家），经其引介了解 Patrick Kavanagh 的诗歌，1962 年首次发表诗作；McLaverty「如养父一般」——《North》组诗 Singing School 中的 Fosterage 一诗即题献给他。
- **婚姻**：1962 在 St Joseph's 结识 Marie Devlin（Ardboe 人，教师兼作家，著爱尔兰神话传说集 *Over Nine Waves*，1994），1965-08 结婚，育三子（Michael 1966、Christopher 1968，女 Catherine Ann 1973）。
- **贝尔法斯特小组与生涯**：1963 起 St Joseph's 讲师，加入 Philip Hobsbaum 组织的 Belfast Group，结识 Derek Mahon、Michael Longley；1966 出版首部诗集 *Death of a Naturalist*（Faber and Faber 出版，此后终身合作），同年任女王大学现代英语文学讲师；1968 与 Longley 巡回朗诵 Room to Rhyme；1972 辞去讲师职迁往爱尔兰共和国 Wicklow 全职写作；1976 任都柏林 Carysfort College 英语部主任并迁居 Sandymount（居至去世）。
- **北美与牛津（1981–2006）**：1981 起哈佛访问教授（Adams House），1985–1997 Boylston 修辞与演说教授，1998–2006 Ralph Waldo Emerson 驻校诗人；1989–1994 牛津诗歌教授（Professor of Poetry，五年任期）；1981 年当选 Aosdána（爱尔兰艺术院）首批成员，1997 当选五长老之一 Saoi。
- **关键荣誉（节选）**：Gregory Award、Geoffrey Faber Prize 1966；Somerset Maugham Award；**诺贝尔文学奖 1995**；Whitbread（Costa）年度图书 1996（The Spirit Level）与 1999（贝奥武甫新译）；T. S. Eliot Prize 2006（District and Circle）；Forward 最佳诗集 2010（Human Chain）；皇家爱尔兰学院院士 1996；Griffin 终身成就奖 2012；Commandeur des Arts et des Lettres 1996；David Cohen Prize 2009。
- **诺奖时刻**：消息传来时与妻子在希腊度假；被问及加入 Yeats、Shaw、Beckett 的爱尔兰诺奖先贤时自答「像置身山脉脚下的一座小丘，但愿你配得上它」；在私人交流中把诺奖称作「the N thing」。
- **父亲之死与挽歌**：父 1986 年（获 Bates College Litt.D. 同年）去世，两年内失怙恃；1987 出版商组诗 *Clearances* 献给母亲。
- **贝奥武甫与晚期**：1999 出版 *Beowulf: A New Verse Translation*（古英语史诗新译，Whitbread 年度图书）；2006-08 中风（康复后自嘲「装起搏器的人有福了」）；2010 出版第十二部诗集 *Human Chain*（Forward 最佳诗集）；2013-08-30 逝世，弥留前以拉丁语 *Noli timere*（勿惧）短信给妻子；2016 遗作《埃涅阿斯纪》卷六译本出版。
- **身后**：葬于故乡 Bellaghy 圣玛丽教堂墓地，与父母幼弟同园；墓志铭取自其诗 The Gravel Walks：「Walk on air against your better judgement」；女王大学 2003 年设立 Seamus Heaney Centre for Poetry；Emory 大学藏其 1964–2003 文献档案（最大 repository）；爱尔兰书店其诗集旋即售罄。
- **核心作品与贡献（5 条）**：
  1. *Death of a Naturalist*（1966）——首部重要诗集，《挖掘》自况铁锹与笔；Mid-Term Break 写幼弟之死；
  2. *North*（1975）——沼泽考古与语言的政治重量，Singing School 组诗含 Fosterage（题献 McLaverty）；
  3. *Field Work*（1979）与 *Seeing Things*（1991）——从阿尔斯特回到更轻盈的幻视书写；
  4. *The Cure at Troy*（1990）——据索福克勒斯 Philoctetes 改写的剧作；
  5. *Beowulf* 新译（1999）与《埃涅阿斯纪》卷六遗译（2016）——古典翻译的两大工程。
- **关键时间线（16 节点）**：1939 生于 Mossbawn → 1953 幼弟车祸身亡、迁 Bellaghy → 1957 入女王大学 → 1961 一等荣誉毕业 → 1962 首次发表诗作（McLaverty 引导）→ 1963 加入 Belfast Group → 1965 与 Marie Devlin 结婚 → **1966《Death of a Naturalist》**、任女王大学讲师 → 1972 辞职迁 Wicklow 全职写作 → 1975《North》→ 1976 迁都柏林 → 1979《Field Work》→ 1981 哈佛、Aosdána 首批 → 1989–94 牛津诗歌教授 → **1995 诺贝尔文学奖** → 1999 贝奥武甫新译 → 2010《Human Chain》→ 2013-08-30 逝世。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | contemporary poetry | 当代诗歌 | 「自叶芝以来最重要的爱尔兰诗人」的评价语境 | 核心页 |
| 1 | irish poetry | 爱尔兰诗歌 | 北爱乡村、盖尔过去与工业化阿尔斯特的双重张力 | 早年页 |
| 2 | literary translation | 文学翻译 | 贝奥武甫新译、《埃涅阿斯纪》卷六遗译 | 翻译页 |
| 3 | literary criticism | 文学批评 | Preoccupations、The Government of the Tongue | 散文页 |
| 4 | elegy | 挽歌传统 | Mid-Term Break、Clearances 等哀悼书写 | 挽歌页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael McLaverty | 师→生（文学导师） | St Thomas' 校长、如养父般的导师，引其发表诗作并介绍卡瓦纳 |
| influence | Patrick Kavanagh | 经 McLaverty 引介 | 其诗歌由 McLaverty 介绍给希尼 |
| influence | Ted Hughes | Lupercal 唤醒 | 在女王大学读 Lupercal 唤起写诗之志 |
| colleague | Ted Hughes | 无向 | 合编选集 The Rattle Bag 与 The School Bag |
| colleague | Philip Hobsbaum | 无向 | 贝尔法斯特小组组织者 |
| colleague | Michael Longley | 无向 | 贝尔法斯特小组同侪，1968 Room to Rhyme 朗诵巡演 |
| colleague | Derek Mahon | 无向 | 贝尔法斯特小组同侪诗人 |
| colleague | Brian Friel | 无向 | 1981 加入其 Field Day 剧团董事会 |
| colleague | Paul Muldoon | 无向 | 爱尔兰后辈诗人，交谊深厚（Emory 档案同藏） |
| spouse | Marie Devlin | 无向 | 1965 年结婚，育三子女；作家，著 Over Nine Waves |

> 叶芝仅系 Lowell 评价中的比较对象**不入库**；索福克勒斯仅系剧作底本**不入库**；Aeneid 系维吉尔作品翻译**不入库**；Robert Lowell/John Sutherland/Pinsky 仅系评价者**不入库**。

### 第 4.6 步：代表作品年表 【人物专属，取自 page.md】

| 年份 | 书名 | 备注 |
|------|------|------|
| 1965 | Eleven Poems | 首本小书（女王大学节出版） |
| 1966 | Death of a Naturalist | 首部重要诗集；Gregory Award、Geoffrey Faber Prize |
| 1969 | Door into the Dark | 第二部主要诗集 |
| 1972 | Wintering Out | 辞职迁 Wicklow 当年出版 |
| 1975 | North | 含 Singing School 组诗（Fosterage 题献 McLaverty） |
| 1979 | Field Work | 都柏林时期 |
| 1980 | Preoccupations: Selected Prose 1968–1978 | 批评文集 |
| 1987 | （Clearances 组诗） | 八首十四行诗悼母 |
| 1990 | The Cure at Troy | 据索福克勒斯 Philoctetes 改写 |
| 1991 | Seeing Things | 更轻盈的幻视书写 |
| 1996 | The Spirit Level | Whitbread 年度图书 |
| 1999 | Beowulf: A New Verse Translation | Whitbread 年度图书 |
| 2006 | District and Circle | T. S. Eliot Prize |
| 2010 | Human Chain | Forward 最佳诗集；第十二部诗集 |
| 2016 | The Aeneid: Book VI | 遗作译本（身后出版） |

### 第 5 步：设计配色 【人物专属】

- **主色**：沼泽深绿 `#1E4D3B`（泥炭、苔藓与爱尔兰的绿）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeBog` 沼泽与挖掘 — 泥褐 `#6B4A2E`
  - `badgePen` 笔与语言 — 幽蓝 `#2C4A6E`
  - `badgeClassics` 古典翻译 — 竹青 `#3E6B5A`
  - `badgeElegy` 挽歌 — 铁灰 `#4A4A55`
- **背景母题**：柔和气泡 + 一条自 Mossbawn 农舍经泥炭沼泽延伸至都柏林海岸的曲径；晚期页面（1995 之后）加入金色晨光渐变。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 铁锹与笔 / Seamus Heaney 1939–2013 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、出生地、教育、婚姻、荣誉、核心领域）
03  核心贡献概览 — 当代诗歌 / 爱尔兰诗歌 / 文学翻译 / 文学批评 / 挽歌
04  早年：Mossbawn 与 Bellaghy (1939–1956) — 九子女之首、幼弟之死、农场与亚麻的双重血统
05  女王大学与文学觉醒 (1957–1962) — Lupercal 的电流、McLaverty 引路、卡瓦纳
06  贝尔法斯特小组 (1963–1966) — Hobsbaum、Mahon、Longley、首部诗集 Death of a Naturalist
07  挖掘 (1966) — 「我将用笔挖掘」（引文框①：Digging 诗节原文）
08  北 (1975) — 沼泽考古与 Singing School（意象图式②：Toner's bog 剖面）
09  全职写作与迁都柏林 (1972–1981) — Wintering Out、Field Work、Carysfort、Clearances 前奏
10  哈佛与牛津 (1981–1994) — Boylston 教授、诗歌教授、Aosdána
11  1995 诺贝尔奖 — 「小丘与山脉」自答、日常的奇迹与活着的过去（引文框②：获奖理由 EN 原文）
12  贝奥武甫 (1999) — 古英语的当代表达、Whitbread 年度图书
13  中风与 Human Chain (2006–2010) — 「婴儿般」的经验、Forward 最佳诗集
14  身后与遗产 — Noli timere、Bellaghy 墓地墓志铭、Heaney Centre、全国悼念
15  结尾 — 日常的奇迹：最广为人知的世界级诗人
```

> 文学家无公式框：第 7/8/11 页用**诗节引文框 / 沼泽意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 身份口径 | 生于北爱尔兰（County Londonderry，勿写 Derry 郡为官方名），明言「我是爱尔兰人不是英国人」；The Observer「英国顶尖知识分子」曾更正致歉——写爱尔兰 |
| 获奖理由措辞 | 官方 "works of lyrical beauty and ethical depth, which exalt everyday miracles and the living past"，勿改写 |
| 罗马字 | Seamus Justin Heaney；引用 Lowell 评价时注明是 Lowell 的话（"the most important Irish poet since Yeats"） |
| 职位年份 | 哈佛 Boylston 教授 1985–1997、驻校诗人 1998–2006；牛津诗歌教授 1989–1994——三段勿混 |
| 贝奥武甫 | 1999 译本获 Whitbread 年度图书；勿写成「获诺奖理由之一」 |
| 幼弟之死 | 1953-02，四岁 Christopher；《Mid-Term Break》与《The Blackbird of Glanmore》相关；「a foot for every year」引文勿改 |
| 墓志铭 | "Walk on air against your better judgement"，出自 The Gravel Walks；临终短信 Noli timere 为拉丁语「勿惧」 |
| 中风年份 | 2006-08（非 2005）；「装起搏器的人有福了」自嘲原句 Blessed are the pacemakers |
| 政治内容 | 北爱时局仅作创作背景一句带过，不评价政治立场、不展开冲突叙事 |
| 首部作品 | 首本小书 Eleven Poems 1965（女王大学节），首部重要诗集 Death of a Naturalist 1966——两说勿混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| bog poetry | 沼泽诗 | 泥炭沼泽保存物与暴力的对位 |
| Belfast Group | 贝尔法斯特小组 | Hobsbaum 组织的诗人工作坊 |
| Professor of Poetry | 牛津诗歌教授 | 非常驻教席（不需居住牛津） |
| Death of a Naturalist | 《一个自然主义者之死》 | 1966 首部重要诗集 |
| Digging | 《挖掘》 | 「I'll dig with it」自况 |
| North | 《北方》 | 1975；含 Singing School 组诗 |
| The Cure at Troy | 《特洛伊的治疗》 | 1990，据 Philoctetes 改写 |
| Beowulf: A New Verse Translation | 《贝奥武甫：新译》 | 1999 |
| Aosdána / Saoi | 爱尔兰艺术院 / 至尊者 | 1981 入选、1997 Saoi |
| Noli timere | 勿惧 | 临终拉丁语短信 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions
- **匹配理由**:
  - "时间感" 精准匹配其获奖理由的核心词 **the living past（活着的过去）**——从 Mossbawn 的泥炭到贝奥武甫的古英语，希尼的全部写作是对时间层积的挖掘
  - "纪录片" 匹配其传记叙事 —— 农家长子 → 女王大学 → 贝尔法斯特小组 → 哈佛与牛津 → 诺奖 → Human Chain，是诗人一生的自然流动
  - "沉稳" 匹配其声口 —— 不事张扬的伦理深度，恰如「小丘与山脉」的自答
- **本地路径**: `music_audio/alex-productions/…/The Flow of Time.wav`（对照 `music_audio/curated_tracks.md` 取实际编号）→ `presentations/20th_century/Seamus_Heaney/The_Flow_of_Time.wav`
- **时长**: 约 130 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Seamus_Heaney/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 项目首页模板（统一 `\input`） |
| `MySQL/seed_person.py` | 人物主记录 + 研究领域 + 社会关系入库 |
| `MySQL/data/Seamus_Heaney.yaml` | 入库 yaml（复用库内 stub id=5173 回填 QID） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
