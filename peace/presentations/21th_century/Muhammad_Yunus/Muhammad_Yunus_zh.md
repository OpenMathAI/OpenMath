# OpenPeace 立传提示词（模板实例：Muhammad Yunus 穆罕默德·尤努斯）

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与 OpenPeace 20 世纪 104 位得主批次的实战经验。
- **本实例**：Muhammad Yunus（穆罕默德·尤努斯）—— 孟加拉国经济学家、小额信贷之父、Grameen Bank 创始人，2006 年诺贝尔和平奖得主（与其创办的 Grameen Bank 共享），首位孟加拉国诺贝尔奖得主。
- **设计哲学**：实践型经济学家立传必须有「身份信息页」，并以「观念 → 机构 → 全球扩散」为叙事主线：一句话的理念（穷人值得信贷）、一家机构（Grameen Bank）、一场运动（约 100 国复制的小额金融），构成全篇骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Muhammad Yunus（1940-06-28 ~ 在世，生于 Hathazari，时属英属孟加拉）
- **气质关键词**：**小额信贷之父、穷人的银行家、社会企业理念的推广者** —— 2006 年诺贝尔和平奖获奖理由：
  > "for their efforts to create social and economic development from below"（表彰他们自下而上促进社会与经济发展的努力）
- **官方获奖理由中译**（照抄名录 `OpenPeace_21st_Century_Nobel_Laureates.md`，禁止改写）：表彰他们自下而上促进社会与经济发展的努力。
- **设计母题**：**一粒稻种到一片田野（seed & field）**——27 美元起始的微型贷款长成覆盖数百万借款人的网络；视觉上以点阵扩散、田野纹理呼应「自下而上（from below）」的获奖理由；背景沿用柔和气泡母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Muhammad_Yunus/page.md`（Wikipedia 全文 + frontmatter，事实基准以此为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1940-06-28 生于 Bathua 村（Hathazari，吉大港专区，时属英属孟加拉）；在世，卒日留白。九个孩子中排行第三。
- **家庭**：父 Haji Muhammad Dula Mia Saudagar（珠宝匠）；母 Sufia Khatun（1949 年起患精神疾病）；兄 Muhammad Ibrahim（达卡大学物理学前教授，CMES 创始人）；兄 Muhammad Jahangir（2019 年去世，电视主持人）；第一任妻 Vera Forostenko（1970 结婚、1977 离异，俄裔，Vanderbilt 俄国文学学生）；长女 Monica Yunus（纽约歌剧女高音）；第二任妻 Afrozi Yunus（1980 结婚，物理学研究者，后任 Jahangirnagar 大学物理学教授）；次女 Dina Afroz Yunus（1986 生）。
- **国籍变迁（infobox 口径）**：British subject（1940–1947）→ Pakistan（1947–1971）→ Bangladesh（1971 起）。
- **教育**：Chattogram Collegiate School（matriculation，39,000 人中列第 16）→ Chittagong College（intermediate；1961 起任经济学讲师）→ Dhaka University 经济学 BA（1960）/ MA（1961）→ Fulbright 奖学金（1965）赴美 → Vanderbilt University 经济学博士（1969，Graduate Program in Economic Development）。
- **任职机构（含年份）**：Dhaka University Bureau of Economics 研究助理 → Chittagong College 讲师（1961）→ Middle Tennessee State University 经济学助理教授（1969–1972）→ 政府计划委员会（1972，旋即辞职）→ Chittagong University 经济学系主任 → Glasgow Caledonian University 校监（2012–2018）。
- **政治任职**：1996-04-03 ~ 1996-06-23 看护政府顾问（主管初等与大众教育、科技、环境森林三部门，首席顾问 Muhammad Habibur Rahman）；2024-08-08 ~ 2026-02-17 孟加拉国临时政府首席顾问（第五任）。
- **关键荣誉**：Nobel Peace Prize 2006；Presidential Medal of Freedom 2009；Congressional Gold Medal 2010；Ramon Magsaysay Award 1984；World Food Prize；Sydney Peace Prize 1998；Seoul Peace Prize 2006；Prince of Asturias Award；Olympic Laurel 2020；72 个荣誉博士学位（27 国）；"七位集齐诺奖+自由勋章+国会金章者之一"。
- **核心事业清单（6 条）**：
  1. 1976 Jobra 实验：自掏 27 美元借给 42 名制竹器村妇，验证穷人信贷可行性
  2. Grameen Bank（1983-10-01 正式建行）：团结小组（solidarity groups）联保模式，至 2007-07 累计放贷 63.8 亿美元、借款人 740 万
  3. 女性信贷优先：Grameen 贷款逾 94% 给女性
  4. 格莱珉家族企业群：Grameen Trust / Fund / Telecom / Phone（Village Phone 计划，1997-03 起 260,000 农村穷人拥有手机）等
  5. 社会企业（social business）理念：Yunus Centre（2008，达卡）与 Global Social Business Summit；Grameen Danone 营养酸奶合资
  6. 著述：《Banker to the Poor》（1999）、《Creating a World without Poverty》（2007）、《A World of Three Zeroes》（2017：零贫困/零失业/零碳排放）
- **关键时间线（20 节点）**：
  1. 1940-06-28 生于 Bathua 村（英属孟加拉 Hathazari）
  2. 1944 全家迁居吉大港市；1949 母亲患病
  3. 1950s Chattogram Collegiate School matriculation（39,000 人列第 16）；童军活动（1952/1955 出访）
  4. 1957 入 Dhaka University 经济系
  5. 1960 BA 毕业；1961 MA；同年任 Chittagong College 经济学讲师
  6. 1965 获 Fulbright 奖学金赴美
  7. 1967 在 Vanderbilt 遇 Vera Forostenko（1970 结婚）
  8. 1969 Vanderbilt 经济学博士；同年起任 Middle Tennessee State University 助理教授（1969–1972）
  9. 1971 独立战争期间在美创建公民委员会、运营 Bangladesh Information Center、出版 Bangladesh Newsletter
  10. 1972 回国，短暂任职计划委员会后转任 Chittagong University 经济学系主任
  11. 1974 大饥荒观察后投身扶贫，建农村经济研究项目（Tebhaga Khamar 三分田）
  12. 1976 Jobra 村实验：27 美元借给 42 名村妇；12 月获 Janata Bank 支持放贷
  13. 1977 与 Vera 离异（Monica 出生后）；项目扩至周边村庄
  14. 1979 项目获央行支持扩展至 Tangail 地区
  15. 1980 与 Afrozi Yunus 结婚
  16. 1983-10-01 试点项目依政府法令转为独立银行 Grameen Bank
  17. 1987 获 Independence Award；1989 获 Aga Khan 建筑奖（住房贷款项目）
  18. 1996 看护政府顾问（三个月）；1997-02 微额信贷峰会共同主席（与希拉里等）
  19. 2006-10-13 与 Grameen Bank 共获诺贝尔和平奖（12-10 奥斯陆领奖）；奖金用于 Grameen Danone、Yunus 科技大学与穷人眼科医院
  20. 2007–2026 The Elders 创始成员（2007–2009）→ 2011 被政府免去 Grameen Bank 行长职务（年龄理由）→ 多项诉讼（2024-01 判刑后保释，2024-08 上诉推翻）→ 2024-08-08 出任临时政府首席顾问 → 2026-02-28 卸任离官邸

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Muhammad_Yunus/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 OpenPeace 已完成篇目 Makefile，设置 `MAIN=Muhammad_Yunus_zh`、`VIDEO_NAME=Muhammad_Yunus_zh`

### 第 3 步：收集图片 【人物专属】

- page.md 内嵌图可用：Yunus 2026 官方照（infobox）、Young Yunus Boy Scout 1953、Grameen Bank Head Office、奥斯陆诺奖全家照（2006）等
- 封面肖像优先用 2006 诺奖前后的正装照；图源 404 则装饰圆占位

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microcredit | 小额信贷 | 1976 Jobra 实验起源，团结小组联保 | 核心贡献页 |
| 1 | microfinance | 小额金融 | Grameen Bank 体系的行业化表达 | 机构页 |
| 2 | social business | 社会企业 | 非分红社会企业理念与 Yunus Centre | 社会企业页 |
| 3 | poverty reduction | 扶贫 | 1974 饥荒后的终生志业 | 扶贫页 |
| 4 | development economics | 发展经济学 | Vanderbilt 博士训练与学术底色 | 教育页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Grameen Bank | 无向 | 创始人，1976 年 Jobra 研究项目起步，1983 年正式建行 |
| co-honored | Grameen Bank | 无向 | 2006 诺贝尔和平奖共同得主 |
| spouse | Vera Forostenko | 无向 | 第一任妻子（1970 结婚、1977 离异），俄国文学学生 |
| spouse | Afrozi Yunus | 无向 | 第二任妻子（1980 结婚），物理学研究者 |
| parent-child | Monica Yunus | 无向 | 长女，纽约歌剧女高音 |
| colleague | Nelson Mandela | 无向 | The Elders 共同发起成员（2007） |
| colleague | Desmond Tutu | 无向 | The Elders 共同发起成员（2007） |
| controversy | Sheikh Hasina | 无向 | 2007 年起关系恶化，2011 被免 Grameen Bank 行长职务，多项诉讼后获判无罪或撤销 |

- **不 入 库（仅叙述）**：次女 Dina（无独立条目）；兄 Muhammad Ibrahim/Jahangir（家族叙述）；Rehman Sobhan/Nurul Islam（研究助理与计划委员会任职，属雇佣非师承）；Graça Machel（The Elders 召集人之一）；Mary Robinson（Friends of Grameen 声援）；Bill Clinton（公开倡导者）。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：田野的绿意、朴素的 hope、经济学的克制
- **配色**：主色 `#1E4D3B`（深林绿，乡村田野与「自下而上」的生命力，manifest 预分配勿改）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeCredit` 小额信贷 — 青绿 `#0E7C7B`
  - `badgeWomen` 女性赋权 — 玫瑰 `#C4204F`
  - `badgeSocial` 社会企业 — 靛蓝 `#4C5FD5`
  - `badgeNobel` 诺贝尔 — 香槟金 `#C9A227`（强调用）
- **背景母题**：柔和气泡 + 点阵扩散纹理（27 美元到 740 万借款人的视觉隐喻）

### 第 6 步：规划幻灯片序列 【人物专属，15 页 + 项目首页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 穆罕默德·尤努斯 / Muhammad Yunus 1940– + 四色 badge + 右上头像
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍变迁/教育/任职/荣誉/核心领域）
03  事业概览 — 小额信贷 / Grameen Bank / 社会企业 / 公共服务
04  早年与求学 — Bathua 村 → 达卡大学 → Fulbright → Vanderbilt 博士（1969）
05  归国与饥荒（1971–1976）— 信息中心 → 计划委员会 → 吉大港经济学系主任
06  Jobra 实验（1976）— 27 美元与 42 名村妇（核心贡献页）
07  Grameen Bank 建行（1983）— 团结小组与「穷人的银行」
08  模式运作 — 联保、周还款、妇女优先（94%+）
09  全球扩散 — 约 100 国复制与 Village Phone 计划
10  社会企业 — Yunus Centre、Grameen Danone、Three Zeroes
11  2006 诺贝尔和平奖 — 官方理由 + 领奖与奖金去向
12  争议与免职（2011–2024）— 免职、诉讼与洗清（两说并陈、全部客观）
13  首席顾问岁月（2024–2026）— 临时政府、改革议程（客观时间线）
14  荣誉与著述 — 三冠得主、72 个荣誉博士、Banker to the Poor
15  结尾
```

### 第 7 步：版式要点 【模板通用】

- 身份信息页参照个人篇 `\profileslide` 实现模式：左头像右信息网格，事实取自 infobox，不得杜撰。
- 时间线页 20 节点拆两页（1983 建行分界），`\foreach` 分隔符必须 ASCII 逗号。
- 数字密集页（63.8 亿美元/740 万借款人/94% 女性）用大数字框 + 短说明，`arraystretch 0.78`。
- 引文框仅用 page.md 明载英文原文（1974 饥荒自述引语、诺奖委员会评语），配中文翻译；委员会评语 "From modest beginnings three decades ago..." 可整段引用。
- 编译硬指标：0 error、vbox ≤10pt、hbox ≤50pt，每写一页即 make 并 `pdftoppm` 目检。

### 第 8 步：史实审查 + 人物专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 在世留白 | 无卒日，封面/概览页/结尾三处统一「1940–」留白 |
| 27 美元口径 | 借给 42 人（Grameen Bank 篇作「mostly bamboo stool makers」，Yunus 篇作 42 名村妇），两篇均按本人页面口径书写，勿混 |
| 建行日期 | 1983-10-01 试点运营 / 10-02 政府法令日期（Grameen Bank 篇 infobox 口径），本人篇用 1983 年建行即可，两说勿在同篇混用 |
| 博士年份 | Vanderbilt PhD 1969（非 1970s 初）；Fulbright 1965 赴美 |
| 首位孟加拉诺奖得主 | page.md 明载 "first Bangladeshi to win the Nobel Peace Prize"，可写；勿扩大成「首位孟加拉籍诺贝尔奖」（口径以页面为准是和平奖首位） |
| 诺奖共享结构 | 理由句主语 "their"，本人篇与 Grameen Bank 机构篇共用同一 EN+中译 |
| Hasina 争议 | 1997 合作（微额信贷峰会共同主席）与 2007 起交恶（免职、174 起诉讼、2024-01 判刑后保释、2024-08 上诉推翻、贪腐案判无罪）均 page.md 明载：全部客观两说并陈，禁政治评价 |
| 政治敏感 | 临时政府任期（2024–2026）、少数群体争议、India 关系叙述：只按 page.md 客观事实简述或回避，不作立场表述；引语只取明载英文原文 |
| 引语使用 | 1974 饥荒自述引语（"In 1974 we ended up with a famine..."）page.md 有完整英文原文，可用；The Economist 反对意见引语须注明出处为该刊观点 |
| 同名区分 | 无同名干扰；Bengali 全名 মুহাম্মদ ইউনূস 仅首页出现一次 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| microcredit | 小额信贷 | 勿译「微贷款」 |
| microfinance | 小额金融 | 行业总称，与 microcredit 有层级差 |
| solidarity lending / groups | 团结小组联保 | 无正式连带责任的运行机制 |
| Grameen | 格莱珉（孟加拉语「乡村」） | Bank 前缀音译统一 |
| social business | 社会企业 | 非分红模式，勿与 social enterprise 混 |
| Chief Adviser | 首席顾问（临时政府首脑） | 孟加拉特有职衔 |
| The Elders | 元老会 | 2007 Mandela 召集 |
| Banker to the Poor | 《穷人的银行家》 | 1999 自传，中译书名通行 |
| Three Zeroes | 三个零 | 零贫困/零失业/零碳排放 |
| Jobra | 乔布拉村 | 1976 实验地，勿拼写 Jobro |

---

## 四、背景音乐选择 ✅ 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Nostalgy** — AShamaluevMusic（inspiring-electronic 合集）
- **风格**: 忧郁 / 温情 / 纪录片
- **匹配理由**:
  - 「温情」匹配从 27 美元善意起步、以信任而非抵押放贷的叙事底色
  - 「忧郁中带希望」呼应 1974 饥荒创伤与半个世纪的持久改良
  - 纪录片气质匹配「观念 → 机构 → 运动」的演进叙事
- **备选**（未采用，仅记录）: The Flow of Time（时间感强但已占用）、SEA（开阔但偏集体叙事）
- **本地路径**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`
- **时长处理**: 曲目时长 > 15 页 × 7 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Muhammad_Yunus/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 获奖理由中译照抄来源 |
| `peace/PROMPTS_WORKFLOW.md` + `peace/PROMPTS_WORKFLOW_21ST.md` | 工作流与政治敏感红线 |
| `MySQL/data/Muhammad_Yunus.yaml` | 入库 yaml（与本文件第 4/4.5 步同步） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
