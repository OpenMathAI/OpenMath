# 文学家立传提示词（实例：Gao Xingjian）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Gao Xingjian（高行健，2000 诺贝尔文学奖，首位华语获奖者）为对象。
> 结构对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库 literature/ 侧）。
- **本实例**：Gao Xingjian（高行健），小说家、剧作家、批评家、翻译家、画家；流亡作家，1997 年入籍法国。
- **设计哲学**：文学家立传无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代；必须有「身份信息页」，并以**文学领域表**做结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Gao Xingjian（1940-01-04 生，在世，生卒年留白口径统一）
- **气质关键词**：**华语先锋戏剧的开路人、灵山的行走者、水墨的孤独旅人**
- **官方获奖理由**（2000，EN 原文照 `nobel_literature_citations.json`，禁止改写）：
  > "for an oeuvre of universal validity, bitter insights and linguistic ingenuity, which has opened new paths for the Chinese novel and drama"
  > 中译（照 `generate_20th_century_list.py` CITATION_ZH）：「表彰其具有普遍价值、刻骨洞察与语言巧思的作品，为中国小说与戏剧开辟了新的道路」
- **设计母题**：**灵山与水墨留白**——《灵山》的雪线群峰意象（我/你/他三重叙事声口）+ 水墨画的虚空留白（画家身份），配长江十个月行走的路线图式。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Gao_Xingjian/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Gao_Xingjian
- **肖像**：第 0 步待下载——Commons 直链 `Gao_Xingjian.jpg`（images.txt 第 4 条，infobox 用 2008 照；页面顶部另有 2012 照可选）；250px 改 500px，curl 加 `-A "Mozilla/5.0"`。
- **参考成品**：`literature/presentations/20th_century/` 下已完成的 16 页立传（封面 `\input` 共享 OpenLiterature 首页模板）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对，以此为准）

- **生卒**：1940-01-04 生于江西赣州（抗战时期）；父籍江苏泰州、母系浙江；战后随家迁南京。**在世，无卒日。**
- **国籍变迁（客观分条）**：infobox 载 Republic of China（1940–49）→ China（1949–98）→ France（1997 至今）；yaml 按 frontmatter 两条 `People's Republic of China` / `France` 入库。
- **家庭**：父为中国银行职员；母为基督教青年会（YMCA）成员，抗战演剧队演员——母亲是其绘画、写作与戏剧的启蒙；配偶 infobox 载 Wang Xuejun（王学筠，后离异）与 Céline Gao（西零）；父母未具名不入库。
- **教育**：南京第十中学（今金陵中学，1952 入学）；1957 遵母命弃中央美院选北京外国语学院，1962 法语系毕业。
- **绘画师承**：中学时期师从画家 Yun Zongying（郓宗嬴）学素描、水墨、油画与泥塑（page.md 明载，advisor-student 关系唯一来源）。
- **任职/流亡经历**：1962 毕业后入中国国际书店；1970 年代因上山下乡运动作为公共知识分子受迫害、被迫焚毁早期手稿、下放安徽宁国六年（曾在港口中学短期任教）；1975 回京任《中国建设》法文翻译组长；1977 入中国作家协会对外关系委员会；1980–1987 任北京人民艺术剧院编剧/驻院剧作家；1987 出走，定居巴黎近郊 Bagnolet；1997 获法国国籍。1989 剧作《逃亡》后作品在中国大陆全面禁演、本人被官方定为 persona non grata（客观简述）。
- **关键荣誉**：Nobel 2000；Chevalier de l'Ordre des Arts et des Lettres 1992；Legion of Honour（军官级，希拉克授予）2002；Premio Letterario Feronia 2000；香港中文大学/中山大学/交通大学/台大/台师大荣誉博士（2001/2001/2002/2005/2017）；NYPL Lions Award 2006；马赛"高行健年"2003；2012 起台师大讲席教授、2020 设高行健中心；2023 当选皇家文学学会 International Writer。
- **核心作品与贡献**（4–6 条）：
  1. 《绝对信号》（1982，又译 Signal Alarm）——中国实验戏剧突破之作。
  2. 《车站》（1983）与《野人》（1985）——荒诞派/先锋戏剧代表作；曹禺赞《车站》"wonderful"（page.md 载）。
  3. 《彼岸》（1986）——排演一个月后叫停，此后大陆未再公演其剧。
  4. 《灵山》*Soul Mountain*（1989 完成/1990 台北出版）——"我/你/他"三声口、文体混合；诺奖委员会特别引用 "one of those singular literary creations that seem impossible to compare with anything but themselves"。
  5. 《一个人的圣经》*One Man's Bible*（1999）。
  6. 现代小说技巧论与戏剧论（*Preliminary Explorations Into the Art of Modern Fiction* 1981；"没有主义"、《对一种现代戏剧的追求》）+ 水墨画家身份（Le goût de l'encre 2002、Return to Painting 2002 等展览）。
- **关键时间线**（17 节点）：1940 赣州出生 → 1950 迁南京 → 1952 入南京十中 → 师从郓宗嬴学画 → 1957 入北京外国语学院 → 1962 法语系毕业入国际书店 → 1970s 焚稿下放安徽六年 → 1975 回京任法文翻译组长 → 1979 随中国作家代表团（含巴金）访巴黎 → 1980–81 入北京人艺/《现代小说技巧初探》→ 1982《绝对信号》→ 1983《车站》争议、自我流放后 1984-11 返京 → 1985《野人》/DAAD 奖学金 → 1986 误诊肺癌、长江十个月行走/《彼岸》叫停 → 1987 出走法国 → 1989《逃亡》/作品全面禁演 → 1990《灵山》台北出版 → 1992 艺术与文学骑士勋章 → 1997 入籍法国 → 1999《一个人的圣经》→ 2000 诺贝尔文学奖 → 2002 军团荣誉勋章 → 2008 起台师大讲席 → 2023 RSL International Writer。

### 第 4 步：文学领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | absurdist drama | 荒诞派戏剧 | 中国荒诞派戏剧开路人 | 先锋页 |
| 1 | avant-garde theatre | 先锋戏剧 | 绝对信号/车站/野人/彼岸 | 北京人艺页 |
| 2 | novel | 小说 | 灵山/一个人的圣经 | 灵山页 |
| 3 | ink wash painting | 水墨画 | 画家身份、留白美学 | 水墨页 |
| 4 | literary criticism | 文学批评 | 现代小说技巧初探/戏剧论 | 理论页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致，仅收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Yun Zongying | 师→生（中学绘画指导） | 素描/水墨/油画/泥塑启蒙 |
| influence | Antonin Artaud | 无向 | page.md 明载影响来源，20 世纪欧洲戏剧 |
| colleague | Ba Jin | 无向 | 1979 年 5 月随中国作家代表团同访巴黎 |
| spouse | Wang Xuejun | 无向 | infobox 载配偶，后离异 |
| spouse | Céline Gao | 无向 | infobox 载配偶 |

### 第 5 步：配色方案 【人物专属】

- **主色**：石墨青灰 `#37474F`（分批文件预分配）
- **辅色**：诺奖香槟金 `#C9A227`
- **badge 四分类**：badgeA 荒诞派戏剧 — 戏台绛 `#7A2E2E`；badgeB 先锋戏剧 — 靛蓝 `#2C4A6E`；badgeC 小说（灵山）— 雪峰青 `#3E6B5C`；badgeD 水墨 — 墨灰 `#3B3B3B`
- **背景母题**：柔和气泡 + 水墨晕染式淡圆（留白感）；灵山页用三声口（我/你/他）三线图式

### 第 6 步：幻灯片序列（14 页，含共享封面）

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 灵山的行走者 / Gao Xingjian 1940– + 四 badge + 右上头像 + 国籍行（中国 → 法国，1997 入籍）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒留白口径/出生地/国籍变迁/教育/师承/任职/荣誉/核心领域）
03  核心贡献概览 — 荒诞派戏剧 / 灵山 / 一个人的圣经 / 水墨画
04  赣南与金陵 (1940–1957) — 母亲启蒙、郓宗嬴绘画指导、南京十中
05  北外法语系与焚稿岁月 (1957–1975) — 弃美院选北外、下放安徽六年
06  北京人艺与先锋戏剧 (1980–1987) — 绝对信号/车站/野人/彼岸（引文框：曹禺 wonder 语）
07  灵山与长江之行 (1986–1990)（核心贡献页：意象图式 + 诺奖委员会 "singular literary creations" 引文框）
08  流亡巴黎 (1987– ) — Bagnolet、逃亡、1997 入籍（客观简述）
09  戏剧理论 — 三分法、中性演员观、"没有主义"
10  水墨与绘画 — ink and wash、展览年表（书影/画册替代公式框）
11  荣誉与认可 — Nobel 2000 · 艺术与文学骑士 1992 · 军团荣誉勋章 2002 · NTNU 讲席与高行健中心
12  遗产 — 东西方交汇点："between Western and Eastern cultures"、PDPD 心理疗法跨域影响
13  结尾 — 诺奖演说引文（"When writing is not a livelihood..."）
```

### 第 7–8 步：版式要点 + Gao 专属陷阱表

- 版式照 literature 侧既成 16 页骨架；引文框/意象图式替代公式框；水墨画可作大图页。

| 陷阱 | 说明 |
|------|------|
| 国籍口径 | infobox 三段变迁（ROC 1940–49 / China 1949–98 / France since 1997）；yaml 只按 frontmatter 两条（People's Republic of China / France）；时间线页可客观标注变迁，不评价 |
| 政治内容 | Bus Stop/Other Shore 停演与禁演、《逃亡》、官方 persona non grata 等**一律按 page.md 客观简述、不作评价、不展开**；朱镕基答问段属政治叙事，建议不进幻灯片 |
| 引语白名单 | 仅 page.md 载英文原文者：诺奖演说 "When writing is not a livelihood..."；"No matter whether it is in politics or literature, I do not believe in or belong to any party or school..."；诺奖委员会 "one of those singular literary creations..."；曹禺 "wonderful"；1987 自述 "meeting point between Western and Eastern cultures"。中文不造"原话" |
| 译者不入库 | Mabel Lee / Gilbert Fong / Noel Dutrait / Claire Conceison / Göran Malmqvist / Jo Riley 仅翻译关系，不入 person_relation（Singer 先例）；Beckett/Ionesco 仅为翻译对象，不入库 |
| 评论者不入库 | Cao Yu、Geremie Barmé、Leo Ou-fan Lee、Jessica Yeung 等仅为评论/表彰，不入 person_relation |
| 父母未具名 | 父（银行职员）、母（YMCA 成员）无姓名，不入库 |
| 剧名双译 | 《绝对信号》=Signal Alarm=Absolute Signal；《逃亡》=Fugitives=Exile；全篇口径统一并首现加注 |
| 《灵山》年份 | 作品表作 1989（完成）、出版 1990 台北——两说并存时写"1989 完成、1990 台北出版" |
| 生卒留白 | 在世，身份页卒日留白，全篇不出现卒年占位符 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| absurdist drama | 荒诞派戏剧 | 中国语境的先锋起点 |
| Theatre of the Absurd | 荒诞剧场 | 与上条区分：运动名 vs 文体 |
| Soul Mountain | 灵山 | 我/你/他三重声口 |
| One Man's Bible | 一个人的圣经 | 1999 |
| The Other Shore | 彼岸 | 1986 排演叫停 |
| meta-theatre | 元戏剧 | infobox Genre 项 |
| ink and wash painting | 水墨画 | 画家身份核心 |
| unreliable narrative voices | 变动的叙事声口 | 非一般 unreliable narrator |
| persona non grata | 不受欢迎的人 | 客观事实引用 |
| émigré | 流亡者 | 1987 出走/1997 入籍两节点 |
| Legion of Honour | 法兰西荣誉军团勋章 | 2002，希拉克授予 |
| Without -isms | 没有主义 | 论集名，勿写"无主义" |

---

## 四、BGM 建议 ✅

- **选定曲目**：**Eternals** — Alex-Productions（49k views，标签：宏大/深远/长期影响）
- **匹配理由**：
  - "宏大/深远" 匹配《灵山》的群山行走意象与流亡写作的精神纵深——一个人的路线横跨长江与欧罗巴
  - "长期影响" 匹配其"为中国小说与戏剧开辟新路径"的官方获奖理由与 PDPD 等跨域余波
  - 相比叙事性更强的曲目，Eternals 的静谧悠远更贴合水墨留白与灵山雪线的画面母题
- **本地路径**：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` → 复制为 `presentations/20th_century/Gao_Xingjian/Eternals.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Gao_Xingjian/page.md` | 事实基准（唯一数据源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Gao_Xingjian.yaml` | 入库 yaml（与本文件 §4/§4.5 一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | 获奖理由中译来源（禁止修改） |

## 六、执行清单（逐项打勾）

1. [ ] 下载肖像 `Gao_Xingjian.jpg`（Commons 直链，curl -A "Mozilla/5.0"，250px→500px，`file` 验证；404 则用装饰圆占位）
2. [ ] 建目录 `literature/presentations/20th_century/Gao_Xingjian/`（含 `images/`）
3. [ ] 复制既成立传 Makefile，改 `MAIN=Gao_Xingjian_zh`、`VIDEO_NAME=Gao_Xingjian_zh`
4. [ ] 复制 BGM：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` → `Eternals.wav`
5. [ ] 写 tex（配色 §5 / badge 四色 / 幻灯片序列 §6 共 14 帧含共享封面）
6. [ ] 编译循环：0 error；vbox ≤10pt；hbox ≤50pt；`latexmk -c` 清理（勿用 rm -f）
7. [ ] 取日志后重新 `make pdf`（单遍 xelatex 会破坏 remember picture）
8. [ ] `pdftoppm` 逐页目检（含身份信息页卒日留白、第 8 页流亡段客观简述口径）
9. [ ] `make images && make video` 出 mp4
10. [ ] Review-1 修正写回本提示词 §8 陷阱表

## 七、版式补遗（literature 侧沉淀经验）

- **身份信息页**：左 40% 头像 + 右信息网格 `\infob` 行式；**卒日行写「——（在世）」留白**，国籍行分三段客观标注（ROC 1940–49 / China 1949–98 / France since 1997），不评价。
- **引文框**：替代公式框——`beamercolorbox` + 左侧 2.5pt 主色竖线，字号 `\small`；两条诺奖演说/自述引语（英文原文）首现配中译，中文侧不造"原话"。
- **意象图式**：第 7 页《灵山》用三线图式（我/你/他三声口）替代数据图表；第 10 页水墨页可大图 + 留白，忌堆满。
- **表格页预算**：剧作年表 4 行 + 引文框顶满时 `arraystretch 0.60~0.62` + 顶部 `-0.45cm`；`tabularx` X 列内禁 `\\`，须用 `\newline`。
- **时间线**：`\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）；17 节点可拆两栏或两页。
- **宏名**：`\newcommand` 名禁数字（如 `\gao2000slide` 会截断），用 `\gaosoulmountainslide` 语义命名。
- **剧名双译**：《绝对信号》（Signal Alarm / Absolute Signal）、《逃亡》（Fugitives / Exile）首现处加注，此后全篇统一。
- **结尾品牌**：底部品牌统一 `OpenLiterature`（共享仓库口径为 OpenMathAI），引号半角 `" "`。
- **涉政红线**：禁演、流亡、入籍等仅客观一行带过；朱镕基答问、海外民主运动评价等政治叙事一律不进幻灯片。

## 八、附录：校验与备选

- **BGM 备选**（未采用）：★★ The Flow of Time（时间感/纪录片，匹配长江十个月行走，但受众偏低）；★ PAST（历史感，匹配焚稿与流亡段落，但基调偏沉郁，弱于 Eternals 的山水纵深）。
- **肖像备选**：页面顶部 2012 照（若 2008 照下载失败可换）；均无处置权问题，Commons 直链即可。
- **行数校验**：本文件目标 190–230 行；Beamer 成品 14 帧 + 共享封面 = 15 页，与 §6 序列一致。
- **DB 校验语句**：`SELECT id,name_en,has_social_data FROM people WHERE qid='Q18143'`；`SELECT COUNT(*) FROM person_relation WHERE from_id=<id> OR to_id=<id>`。
- **yaml 对照**：`MySQL/data/Gao_Xingjian.yaml` 与 §4 领域表、§4.5 关系表逐行一致，入库后 diff 校验。
- **同名风险**：库内无重名 "Gao Xingjian" 记录（入库前已 SELECT 核查）；对手方 Yun Zongying / Wang Xuejun / Céline Gao / Ba Jin / Antonin Artaud 均为 stub，不编造 qid。
- **汇报格式**：`✅ Gao Xingjian | prompt✅ | yaml✅ | DB id=5844 fields=5 relations=5 | 主色#37474F BGM Eternals`。

> **开始执行。每完成一步汇报。最重要的事：事实只出自 page.md，无载禁写；涉政内容客观简述不评价。**
