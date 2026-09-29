# 文学家立传提示词（OpenLiterature：Wole Soyinka）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Wole Soyinka（1986 诺贝尔文学奖，首位非洲得主）为执行实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 〇、批次信息 【人物专属】

| 项 | 值 |
|----|----|
| 分批 | `literature/prompt_batches_lit.json` batch 17（agent：lit-batch-17） |
| dir / qid | Wole_Soyinka / Q41488 |
| 获奖年份 | 1986 |
| 主色（预分配） | `#0E4D64` |
| BGM（预分配） | Eternals |
| page.md | `literature/presentations/pages/20th_century/Wole_Soyinka/page.md` |
| prompt / yaml | `literature/presentations/20th_century/Wole_Soyinka/Wole_Soyinka_zh.md` / `MySQL/data/Wole_Soyinka.yaml` |

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆与文学家侧首例（Knut Hamsun 等）的实战经验。
- **本实例**：Akinwande Oluwole Babatunde Soyinka（沃莱·索因卡）。
- **设计哲学**：文学家立传无公式框——用**剧作书影、名句引文框、约鲁巴面具意象图式**替代；保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Wole Soyinka（1934-07-13 生，在世）
- **气质关键词**：**首位非洲诺奖得主、约鲁巴神话的戏剧家、从不沉默的公共知识分子** —— 1986 诺贝尔文学奖获奖理由（官方原文 + 中译，禁止改写）：
  > "who in a wide cultural perspective and with poetic overtones fashions the drama of existence"
  > （表彰其以广阔的文化视野与诗意色彩塑造了存在之戏剧）
- **设计母题**：**存在之戏剧（the drama of existence）**。舞台、面具、鼓点——约鲁巴祭祀剧与希腊悲剧在他笔下合流；「广阔的文化视野」对应双文化并置的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Wole_Soyinka/page.md`（同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Wole_Soyinka
- **肖像**：⏳ 第 0 步待下载（images.txt 有 `WoleSoyinka2015.jpg` 250px 缩略图，建议取 500px 原图；失败则装饰圆占位）
- **参考模板**：
  - 文学家成品参照：`literature/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`literature/presentations/cover/`（以主控实际封面文件为准）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- 生卒：1934-07-13 生于阿贝奥库塔 Ake（时属英属尼日利亚）；在世（享年留白三处一致）
- 国籍：尼日利亚
- 家庭：约鲁巴基督徒（圣公会）家庭，七子女中排行第二；父 Samuel Ayodele Soyinka 为圣公会牧师兼校长（Isara-Remo 王室后裔）；母 Grace Soyinka（娘家 Jenkins-Harrison）为店主与活动家，出自 Ransome-Kuti 家族
- 教育：St. Peters 小学（父亲任校长）→ Abeokuta Grammar School → Government College Ibadan（1946–51）→ University College Ibadan（1952–54，英语文学/希腊语/西方历史）→ **University of Leeds，在 G. Wilson Knight 指导下学习**，1957 获英语一等文学士；Leeds 期间任校园讽刺杂志 *The Eagle* 主编；1957 获全校演讲比赛冠军
- 结社：大学期间与同学共创 Pyrate Confraternity（National Association of Seadogs，尼日利亚第一个学生社团）
- 任职轨迹：Royal Court Theatre 剧本审读 → 1959 Rockefeller 研究奖学金返尼 → 1962 Ifẹ 讲师 → 1964 抗议当局辞职、组 Orisun 剧社 → University of Lagos 高级讲师 → Ibadan 戏剧系主任（1967 因入狱未就任）→ 1975 起任 Ife（后 Obafemi Awolowo University）比较文学教授至 1999 → Cornell Goldwin Smith 讲席教授（1988–91）→ Emory Robert W. Woodruff 讲席教授（1996）→ UNLV/NYU/Loyola Marymount/剑桥/牛津/哈佛/耶鲁等任教；2022 任 NYU Abu Dhabi 戏剧教授
- 关键经历（客观简述，不作政治评价）：1965 首次被捕（电台换带事件）约数月后因国际作家声援获释；**1966–67 内战斡旋后被联邦当局逮捕，监禁 22 个月**，狱中写大量诗与笔记；1969-10 大赦获释；1971-04 辞去 Ibadan 职务、开始多年自愿流亡；**1994-11 骑摩托经贝宁边境流亡美国**；1997 被阿巴查政府以叛国罪起诉；1997–2000 任国际作家议会（IPW）第二任主席
- 关键荣誉：Nobel 1986（**首位非洲得主**，也是「新英语文学」首位得主）；1967 John Whiting Award（与 Tom Stoppard 共享）；1968 Jock Campbell-New Statesman 奖；1983 Anisfield-Wolf 奖（*Aké*）；1986 Agip 文学奖；1994 UNESCO 亲善大使；2014 国际人道主义奖；2017 欧洲戏剧奖特别奖；尼日利亚联邦共和国司令勋章等
- 核心作品与贡献（4–6 条）：
  1. *A Dance of the Forests*（1960）——尼日利亚独立日官方剧目，1960-10-01 拉各斯首演
  2. *The Lion and the Jewel*（1959）、*The Trials of Brother Jero*（1960）——早期喜剧代表作（Royal Court 剧目体系）
  3. *The Interpreters*（1965）——首部长篇小说；*Season of Anomy*（1973）
  4. *Death and the King's Horseman*（1975）——约鲁巴悲剧杰作，2022 改编电影 *Elesin Oba*（首部约鲁巴语电影入围 TIFF）
  5. 狱中写作：*Poems from Prison*（1969）、*The Man Died: Prison Notes*（1972）
  6. 自传三部曲：*Aké: The Years of Childhood*（1981）、*Ibadan*（1994）、*You Must Set Forth at Dawn*（2006）；2021 五十年来首部长篇 *Chronicles from the Land of the Happiest People on Earth*
- 关键时间线（约 18 节点）：1934 生于阿贝奥库塔 → 1946–51 Government College → 1952–54 University College Ibadan、创 Pyrate Confraternity → 1954 赴 Leeds（G. Wilson Knight 指导）→ 1957 BA 一等、*The Invention* 上演 Royal Court → 1958–59 *The Swamp Dwellers*/*The Lion and the Jewel* → 1959 Rockefeller 奖学金、接任 *Black Orpheus* 联合主编 → 1960 独立日剧《森林之舞》 → 1962 Ifẹ 讲师 → 1964 辞职组 Orisun 剧社 → 1965 *The Interpreters*、首次被捕 → 1966–67 内战斡旋、监禁 22 个月 → 1967 John Whiting 奖（与 Stoppard 共享）→ 1969 大赦获释、*The Bacchae of Euripides* → 1971 流亡开始、*A Shuttle in the Crypt* → 1973 荣誉博士（Leeds）、Churchill College 访问研究员 → 1975 *Death and the King's Horseman*、主编 *Transition*、回归 Ife → 1981 *Aké* → 1986 诺贝尔奖（首位非洲得主）→ 1988–91 Cornell → 1994 流亡美国、UNESCO 亲善大使 → 1997 叛国指控、IPW 主席 → 2001 *King Baabu* → 2006 回忆录 → 2017 欧洲戏剧奖 → 2021 *Chronicles* → 2022 NYUAD

### 第 1–3 步：目录、Makefile 与肖像收集 【模板通用】

- 第 1 步：在 `literature/presentations/20th_century/` 下确认/创建 `Wole_Soyinka/` 与 `images/`
- 第 2 步：复制邻近已立传目录的 Makefile，改 `MAIN=Wole_Soyinka_zh`、`VIDEO_NAME=Wole_Soyinka_zh`
- 第 3 步：肖像下载——images.txt 有 URL 直接取（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 则改用 Commons `Special:FilePath` 或 Wikipedia REST API `page/summary` 查 infobox 原图名；仍失败用装饰圆占位，图注注明「肖像暂缺」

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | drama | 戏剧 | 25 部剧作；Royal Court/国家剧院/欧洲戏剧奖 | 全篇 |
| 1 | African theatre | 非洲戏剧 | Rockefeller 奖学金研究方向；1960s Mask/Orisun 剧社 | 剧场页 |
| 2 | Yoruba mythology | 约鲁巴神话 | Oriṣa 作为创作源泉；*Death and the King's Horseman* | 神话页 |
| 3 | poetry | 诗歌 | 七部诗集：*Idanre*、*A Shuttle in the Crypt*、*Mandela's Earth* 等 | 诗集页 |
| 4 | satire | 讽刺文学 | *The Eagle* 主编起步；*Kongi's Harvest*/*King Baabu*/*Chronicles* | 讽刺页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | G. Wilson Knight | direction: advisor | Leeds 英语文学学习指导教师（1954–57） |
| spouse | Barbara Dixon | 无向 | 1958–1963，英国作家，长子 Olaokun 之母 |
| spouse | Olaide Idowu | 无向 | 1963–1989，尼日利亚图书馆员 |
| spouse | Folake Doherty | 无向 | 1989 年结婚 |
| co-honored | Tom Stoppard | 无向 | 1967 John Whiting Award 共同得主 |
| colleague | Toni Morrison | 无向 | 本人自述挚友 |
| colleague | Henry Louis Gates Jr. | 无向 | 本人自述挚友 |
| colleague | D. O. Fagunwa | 无向 | 英译其约鲁巴语小说（*The Forest of a Thousand Demons*，1968） |
| colleague | Bertolt Brecht | 无向 | 将其《三分钱歌剧》改编为约鲁巴语 *Opera Wọnyọsi*（1977） |
| colleague | Janheinz Jahn | 无向 | 1959 接任《Black Orpheus》联合主编 |

**诚实注记**：Joyce M. Green（引荐 Leeds 的老师）虽 page.md 有载，但仅为「写信推荐」而非导师关系，不入库；政治人物（Obasanjo/Ojukwu/Banjo 等）一律不入库。

### 第 5 步：设计配色 【人物专属】

- **气质**：大地的赭、面具的黑、鼓点的红
- **配色**：主色 `#0E4D64`（预分配深青）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 戏剧 — 深青 `#0E4D64`
  - `badgeB` 约鲁巴神话 — 陶赭 `#B4632C`
  - `badgeC` 诗歌 — 玫瑰 `#C4204F`
  - `badgeD` 讽刺 — 琥珀 `#E07B30`
- **背景母题**：面具轮廓与鼓面同心圆（稀疏、抽象、不涉及宗教符号细节）；舞台追光的窄长条呼应「戏剧」母题。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 存在之戏剧的塑造者 / Wole Soyinka 1934– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 生卒（在世留白）、出生地、约鲁巴家庭、教育（Ibadan/Leeds）、任职、荣誉、核心领域
03  核心创作概览 — 戏剧 / 诗歌 / 小说 / 自传 / 讽刺
04  早年：Ake 与约鲁巴家庭 (1934–1954) — 校长父亲、Ransome-Kuti 家族、Pyrate Confraternity
05  Leeds 与 Royal Court (1954–1959) — G. Wilson Knight 指导、*The Eagle* 主编、*The Invention*
06  独立年代 (1959–1965) — Rockefeller 奖学金、*Black Orpheus*、《森林之舞》、Orisun 剧社、*The Interpreters*
07  监禁与狱中写作 (1966–1969) — 22 个月监禁、*Poems from Prison*（客观简述）
08  流亡与回归 (1971–1975) — Churchill College、*Death and the King's Horseman*、*Transition* 主编
09  代表作页：《Death and the King's Horseman》（引文框/面具意象图式替代公式框）
10  自传与晚年小说 — *Aké* / *Ibadan* / *You Must Set Forth at Dawn* / 2021 *Chronicles*
11  荣誉与认可 — Whiting 1967 · Anisfield-Wolf 1983 · 欧洲戏剧奖 2017 · UNESCO 1994
12  1986 诺贝尔奖 — citation 官方原句引文框；「首位非洲得主」的里程碑意义
13  师友与传承 — Morrison/Gates 挚友、Fagunwa/Brecht 译介
14  遗产：非洲文学的世纪坐标
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

**Soyinka 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方原句 "who in a wide cultural perspective and with poetic overtones fashions the drama of existence"；中译从 CITATION_ZH 原样取，禁止改写 |
| 在世口径 | 1934-07-13 生，无卒日，享年留白三处一致（身份页/封面/结尾） |
| 「首位」限定 | 「首位非洲文学奖得主」成立；「首位黑人诺奖得主」之类扩大表述**禁写** |
| 监禁表述 | 只写 page.md 事实（22 个月、狱中写作、1969-10 大赦获释）；斡旋细节一句带过，**不评价内战双方、不展开政治叙事** |
| 时政禁写清单 | Trump/签证争议、CIA 资金章节争议、2023 Isese 争议、对尼日利亚时局评论——一律不写 |
| 译介关系方向 | 对 Fagunva/Brecht 是「索因卡译/改编对方作品」，colleague 类型，note 写清方向，勿写成其影响者 |
| 三任妻子 | Barbara Dixon（英）、Olaide Idowu（尼）、Folake Doherty，年份按 page.md；子女数量（8+2）勿展开个人细节 |
| Leeds 指导 | page.md 原文 "under the supervision of G. Wilson Knight"，是本科学习指导，勿拔高为「博导」 |
| 奖项年份 | John Whiting Award 1967（与 Stoppard 共享，获奖作品 page.md 两处口径不一——1967 节说戏剧创作、Honours 节说 *The Interpreters*，tex 中按 1967 年共享呈现、作品名可略）；*The Man Died* 1972 出版、1984 遭禁——年份勿混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| the drama of existence | 存在之戏剧 | 获奖理由核心短语 |
| Yoruba | 约鲁巴 | 民族/语言双义 |
| Oriṣa | 奥里莎（神灵） | 创作源泉表述，勿写成宗教皈依 |
| Pyrate Confraternity | 海盗会（学生社团） | 后身 National Association of Seadogs |
| Black Orpheus | 《黑色俄耳甫斯》（杂志） | 西非文学重要刊物 |
| Death and the King's Horseman | 《死亡与国王的骑马人》 | 通行中译名 |
| The Man Died | 《人未死》 | 狱中笔记，书名勿意译过度 |
| Aké: The Years of Childhood | 《阿凯：童年岁月》 | 自传 |
| Opera Wọnyọsi | 恶歌剧（三分钱歌剧约鲁巴改编） | 1977 |
| GCON | 尼日尔河大司令勋章 | 荣衔，infobox 头衔 |

---

### 第 9 步：执行终检清单 【模板通用】

- [ ] 页数与第 6 步序列一致（`pdftoppm` 逐页目检；出 mp4 后核时长）
- [ ] 获奖理由 EN 原句与 CITATION_ZH 中译逐字核对（含标点）
- [ ] 在世口径三处留白一致（封面、身份页、结尾页）
- [ ] 溢出：vbox ≤10pt、hbox ≤50pt；引文框不破行
- [ ] yaml 关系与第 4.5 步表逐行一致；note 无裸冒号/引号头
- [ ] 品牌口径：结尾页底部 `OpenMathAI`，引号半角

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（预分配）
- **风格**: 宏大 / 深远 / 长期影响
- **匹配理由**:
  - "宏大/深远" 匹配「存在之戏剧」的仪式感与命运纵深 —— 约鲁巴祭祀剧与希腊悲剧的合流天然需要史诗底色
  - "长期影响" 匹配其 70 年创作跨度与「首位非洲得主」的世纪坐标 —— 从 1957 Royal Court 到 2021 *Chronicles*
  - 避开本批已用曲（Tragedy/With Me/Cinematic Experience/New Lands），无撞曲
- **备选** (未采用): ★★ Timeless（长跨度纲领感，但同批 Seifert 侧避让其他高频曲）；★ Expedition（探索感匹配非洲戏剧研究，史诗性略弱于 Eternals）
- **本地路径**: `music_audio/alex-productions/` 下 Eternals 对应 wav（复制到 `literature/presentations/20th_century/Wole_Soyinka/Eternals.wav`）
- **时长**: 以实际文件为准，ffmpeg `-shortest` 自动对齐

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：引语只用 page.md 英文原句；无载禁写；时政内容客观一句带过不评价；关系表与 yaml 完全一致。**
