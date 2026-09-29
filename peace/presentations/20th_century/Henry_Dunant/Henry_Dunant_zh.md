# 和平奖得主立传提示词（OpenPeace 批次 1：Henry Dunant）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Henry Dunant（1901 首届诺贝尔和平奖得主、红十字国际委员会创始人）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Henry Dunant（亨利·杜南，本名 Jean-Henri Dunant）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页）与「事业领域」的结构化表达；Dunant 的一生有「巅峰—坠落—重生」的完整弧线，叙事节奏是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：Henry Dunant（1828-05-08 日内瓦 ~ 1910-10-30 海登，享年 82 岁）
- **气质关键词**：**红十字之父、索尔费里诺的见证者、被遗忘又被重新发现的理想主义者** —— 1901 首届诺贝尔和平奖获奖理由：
  > "for his humanitarian efforts to help wounded soldiers and create international understanding"（表彰他为救助伤员、增进国际理解所做出的人道主义努力）
- **设计母题**：**红十字与黎明（red cross and the dawn）**。一场战役的黄昏、一名过路商人的夜晚书写、一个中立救援组织的诞生——红十字的几何形态与「Tutti fratelli（人人皆兄弟）」的人道之光，构成比「和平鸽」更贴合 Dunant 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Henry_Dunant/page.md`（含 frontmatter QID Q12091）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Henry_Dunant` 四件套到 `peace/presentations/pages/20th_century/Henry_Dunant/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1828-05-08 生于日内瓦 ~ 1910-10-30 逝于瑞士海登 Heiden，享年 82 岁；本名 Jean-Henri Dunant，长名 Henry/Henri Dunant）
  - 国籍（瑞士；1859 起兼有法国国籍）
  - 家庭（父 Jean-Jacques Dunant 商人，救助孤儿与假释者；母 Antoinette Dunant-Colladon 服务病者贫者；虔诚加尔文宗家庭）
  - 教育（Collège de Genève，1849 年 21 岁因成绩不佳离校；后入货币兑换行 Lullin et Sautter 做学徒并留任）
  - 任职（商人/社会企业家：1853 Sétif 殖民公司差务；1856 创办 Mons-Djémila 磨坊金融工业公司；1867 破产）
  - 关键荣誉（Nobel Peace Prize 1901 首届；海德堡大学医学院荣誉博士 1903；多国红十字会名誉成员；Binet-Fendt 奖；多国勋章）
  - 核心事业清单（①索尔费里诺战场组织平民救护 ②《索尔费里诺回忆录》1862 ③五人委员会/ICRC 创始 1863 ④首届日内瓦公约外交会议 1864 ⑤1901 首届诺贝尔和平奖）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Henry_Dunant/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Henry_Dunant_zh`、`VIDEO_NAME=Henry_Dunant_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 有真实肖像：
  - 主肖像 `Henry_Dunant_1855.jpg`（1855 年照，下载时 250px 改 500px）
  - 备选 `Jean_Henri_Dunant.jpg`（1901 年诺奖时照）、`Committee_of_Five_Geneva_1863.jpg`（五人委员会画像，可作插图页）、`Battaglia_di_Solferino_(Henry_Dunant).jpg`（索尔费里诺场景画）
- 无肖像时用装饰圆占位（本篇不需要）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道主义救援 | 战场救护、无差别救治伤员 | 索尔费里诺页、核心页 |
| 1 | international humanitarian law | 国际人道法 | 首届日内瓦公约的发起背景 | 公约页 |
| 2 | red cross movement | 红十字运动 | ICRC 五人委员会创始成员 | 创始页 |
| 3 | social activism | 社会活动 | 基督教青年会日内瓦分会、济贫 | 早年页 |
| 4 | disarmament advocacy | 裁军倡导 | 普法战争后主张裁军谈判与国际仲裁法庭 | 晚期页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 8 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Frédéric Passy | 无向 | 1901 首届诺贝尔和平奖共同得主 |
| founder | International Committee of the Red Cross | 人→机构 | 1863 五人委员会创始成员，首任书记 |
| colleague | Gustave Moynier | 无向 | 五人委员会成员，长期理念分歧与冲突 |
| colleague | Henri Dufour | 无向 | 五人委员会成员，瑞士军队将领 |
| colleague | Louis Appia | 无向 | 五人委员会成员，医生 |
| colleague | Théodore Maunoir | 无向 | 五人委员会成员，医生 |
| colleague | Bertha von Suttner | 无向 | 1897 起通信往来 |
| colleague | Wilhelm Sonderegger | 无向 | 海登红十字分会，鼓励其记录生平 |

- 方向约定：founder 人→机构有向；co-honored/colleague 无向自动 from<to 归一
- 对手方 name_en 用 manifest 规范名；缺失人物由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：人道、救赎、废墟中的微光
- **配色**：深蓝（manifest 预分配主色 `#16324F`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeRed` 红十字与日内瓦 — 猩红 `#A31621`
  - `badgeSolferino` 索尔费里诺 — 战场赭 `#8C4A2F`
  - `badgeConv` 日内瓦公约 — 外交蓝 `#2E5E4E`
  - `badgeNobel` 首届诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 细红十字网格意象（低饱和），呼应「中立救援」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（Switzerland / France from 1859），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、家庭、教育、任职、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 红十字之父 / Henry Dunant 1828–1910 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含本名、家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 索尔费里诺 / 回忆录 / ICRC / 日内瓦公约 / 首届诺奖
04  早年：日内瓦的觉醒年代 (1828–1852) — Réveil 宗教觉醒、济贫会、周四协会、基督教青年会日内瓦分会 1852
05  商人杜南：阿尔及利亚的磨坊 (1853–1859) — Sétif 差务、《突尼斯摄政记》1858、Mons-Djémila 公司
06  索尔费里诺之夜 (1859-06-24) — 四万伤亡、组织平民救护、Tutti fratelli、争取奥军医生获释
07  《索尔费里诺回忆录》(1862) — 自费印行 1600 册、中立救援组织的构想、寄送欧洲政要
08  五人委员会与 ICRC 的诞生 (1863) — Moynier/Dufour/Appia/Maunoir、02-17 首次会议、10 月 14 国会议
09  首届日内瓦公约 (1864-08-22) — 瑞士政府召集、12 国签署、杜南负责会务
10  坠落：破产与放逐 (1867–1886) — Crédit Genevois 破产、退出委员会、被逐出基督教青年会、流亡多年
11  海登的隐士 (1887–1895) — 疗养院、Sonderegger 夫妇、荣誉会长 1890
12  重新发现 (1895–1901) — Baumberger 文章、Müller 撰史正名、Daae 四年奔走
13  1901 首届诺贝尔和平奖 — 与 Passy 共享、两类获奖先例（人道主义/和平会议）、奖金存入挪威银行
14  晚年与遗产 — 荣誉博士 1903、临终之问、World Red Cross Day、Dunantspitze 2014 更名
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Dunant 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名与称呼 | 本名 Jean-Henri Dunant，通行 Henry/Henri Dunant；封面用 Henry Dunant，身份页注本名 |
| 诺奖理由措辞 | 官方理由 "for his humanitarian efforts to help wounded soldiers and create international understanding"，强调**人道主义努力**，勿改写成"因创立红十字而获奖"的转述口径 |
| 共同得主 | 1901 与 Frédéric Passy 共享（Passy 独立半份），两人事业互不隶属，勿写"Passy 帮助 Dunant 获奖"；Müller 建议分奖是游说过程事实 |
| ICRC 创始日期 | 五人委员会首次会议 1863-02-17 被视为 ICRC 创立日；勿写成 Dunant 一人创会 |
| Moynier 关系 | 既有合作（委员会同僚）又有理念冲突；中立呈现，勿单侧美化或丑化；"Moynier 阻挠资助"为 page.md 明载事实可写 |
| 退出委员会 | 1867-08-25 辞书记、1867-09-08 完全除名、1868-08-17 商事法院判决，三个日期勿混 |
| 国籍 | 瑞士人，1859 起兼法国国籍；勿写"法国人" |
| 死因与晚年 | 患抑郁症与被害妄想（要求厨师先尝食）；晚年抨击加尔文宗与组织化宗教、自称不可知论者——按 page.md 客观记录，不加评价 |
| 临终引语 | "Where has humanity gone?" 为 page.md 明载的最后的话，可直接引用；ICRC 贺电引语可整段引用 |
| 无载禁写 | 不写"诺奖委员会内部争论细节"、不编造妻子与子嗣（Dunant 终身未婚 page.md 未载，禁写）、不写杜南与拿破仑三世会面成行（仅写前往求见） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Battle of Solferino | 索尔费里诺战役 | 1859-06-24，勿与年份/地点混淆 |
| A Memory of Solferino | 《索尔费里诺回忆录》 | 法文原名 Un Souvenir de Solferino，1862 |
| International Committee of the Red Cross | 红十字国际委员会 | 1863 五人委员会，非 Dunant 独创 |
| First Geneva Convention | 首届日内瓦公约 | 1864-08-22，12 国签署 |
| Tutti fratelli | 人人皆兄弟 | Castiglione 妇女所创口号，非 Dunant 原话 |
| YMCA | 基督教青年会 | 1852 创日内瓦分会，1868 被除名 |
| humanitarian aid | 人道主义救援 | 与 pacifism（和平主义）区分 |
| neutral organization | 中立组织 | 回忆录核心构想 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 开拓 / 新纪元 / 史诗感
- **匹配理由**:
  - "New Lands" 呼应 Dunant 开创的人道主义新疆域——红十字、日内瓦公约、首届诺奖，每一步都是"从未有人走过的新大陆"
  - 曲名的黎明感与设计母题「索尔费里诺的黎明」互文：从战场废墟到人道之光
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → `presentations/20th_century/Henry_Dunant/New_Lands.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Henry_Dunant/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/Henry_Dunant/images.txt` | 肖像与插图 URL |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Henry_Dunant.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
