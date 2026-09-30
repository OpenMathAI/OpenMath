# 和平奖得主立传提示词（OpenPeace 21 世纪批次 4：Tawakkol Karman）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Tawakkol Karman（2011 诺贝尔和平奖得主、也门记者与妇女权利活动家）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Tawakkol Abdel-Salam Khalid Karman（塔瓦库勒·卡曼，在世；页内另有 Tawakkul/Tawakel 拼写，统一用 manifest 形式 Tawakkol）。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「事业领域」的结构化表达；Karman 是「记者→广场组织者→诺贝尔奖得主→流亡发声者」的角色演进，扩音器与每周星期二的坚持是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：Tawakkol Karman（1979-02-07 生于也门塔伊兹省 Shara'b As Salam，当时属北也门，在世）
- **气质关键词**：**新闻自由的旗手、阿拉伯之春的女性面孔、铁娘子** —— 2011 诺贝尔和平奖获奖理由：
  > "for their non-violent struggle for the safety of women and for women's rights to full participation in peace-building work"（表彰她们以非暴力方式维护妇女安全、争取妇女充分参与和平建设工作的权利）
- **设计母题**：**扩音器与广场（megaphone and the square）**。萨那变革广场每周二的集会、2011 年她在广场上传用的那只扩音器（今陈列于诺贝尔博物馆）、摘下面纱换上的彩色头巾——这是比「和平鸽」更贴合 Karman 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Tawakkol_Karman/page.md`（含 frontmatter QID Q104622）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载四件套到 `peace/presentations/pages/21th_century/Tawakkol_Karman/`（**事实基准如下**）：
  - 出生（1979-02-07 生于塔伊兹省，当时属也门阿拉伯共和国/北也门，在世；全名 Tawakkol Abdel-Salam Khalid Karman）
  - 国籍（也门；2012-10-11 获土耳其国籍，土耳其外长达武特奥卢颁发）
  - 家庭（父亲 Abdel Salam Karman 律师兼政治人物，曾任萨利赫政府法律事务部长后辞职；弟 Tariq 诗人；妹 Safa 律师、首位毕业于哈佛法学院的也门人、半岛电视台记者；丈夫 Mohammed al-Nahmi；正文载三个孩子，infobox 载 4——两说并存，幻灯片只写"育有子女"或取正文口径）
  - 教育（也门科技与科学大学商学本科；萨那大学政治学研究生学位；马萨诸塞大学洛威尔分校国际安全硕士；2012 获加拿大阿尔伯塔大学国际法荣誉博士）
  - 任职（Al-Thawrah 报记者；WJWC 联合创始人兼领导人 2005；也门记者工会成员；Belqees TV 创立者 2014；Facebook 监督委员会成员 2020）
  - 关键荣誉（Nobel Peace Prize 2011；Foreign Policy 2011 全球百大思想家第一名；Time 2011 年度女性（2019 年 89 期特刊）；2019 Asian Awards 年度社会企业家）
  - 核心事业清单（①WJWC 与新闻自由倡导 2005 ②2007–2010 萨那变革广场每周示威 ③2011 也门起义的学生集会组织 ④童婚与妇女权利倡导 ⑤2014 Belqees TV ⑥伊斯坦布尔流亡后的发声与 2023 土耳其-叙利亚地震救援）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Tawakkol_Karman/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Tawakkol_Karman_zh`、`VIDEO_NAME=Tawakkol_Karman_zh`

### 第 3 步：收集图片 【人物专属】

- 查看 `images.txt`；2012 年照（infobox 主图）为首选主肖像；三人领奖合影、诺贝尔博物馆扩音器照片可作诺奖页插图
- 无肖像时用装饰圆占位（须在图注写明）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | press freedom | 新闻自由 | WJWC 创立缘起，SMS 新闻服务执照之争 | 事业页 |
| 1 | human rights | 人权 | frontmatter field_of_work 首项 | 全篇 |
| 2 | women's rights | 妇女权利 | 2011 诺奖核心理由 | 诺奖页 |
| 3 | democracy | 民主 | 2011 也门起义的诉求 | 广场页 |
| 4 | nonviolent resistance | 非暴力抵抗 | 每周静坐与学生集会 | 广场页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 6 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ellen Johnson Sirleaf | 无向 | 2011 诺贝尔和平奖共同得主 |
| co-honored | Leymah Gbowee | 无向 | 2011 诺贝尔和平奖共同得主 |
| spouse | Mohammed al-Nehmi | 无向 | 丈夫 |
| parent-child | Abdulsalam Khaled Karman | 无向 | 父亲，律师兼政治人物，曾任也门法律事务部长 |
| founder | Women Journalists Without Chains | 人→机构 | 2005 年与其他七名女记者共同创立并领导 |
| founder | Belqees TV | 人→机构 | 2014 年创立的新闻频道，2015 年迁至伊斯坦布尔 |

- 方向约定：founder 人→机构有向；co-honored/spouse/parent-child 无向自动 from<to 归一
- 对手方 name_en 用 manifest 规范名（Sirleaf 批次 3、Gbowee 本批次先建 stub，Karman yaml 沿用同名匹配）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：锐利、公开、广场上的声音
- **配色**：深海蓝（manifest 预分配主色 `#16324F`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgePress` 新闻自由 — 铅灰蓝 `#3E5C76`
  - `badgeSquare` 广场与起义 — 暖红 `#A34700`
  - `badgeWomen` 妇女权利 — 玫紫 `#8E4585`
  - `badgeNobel` 2011 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 扩音器声波弧线意象（低饱和），呼应「广场之声」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（Yemen / Turkey from 2012），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：出生、全名、国籍、家庭、教育、任职、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 阿拉伯之春的女性面孔 / Tawakkol Karman 1979– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（全名、家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — WJWC / 广场示威 / 2011 起义 / 妇女权利 / Belqees TV
04  早年与家学 (1979–2004) — 塔伊兹、父亲的法律事务部长与辞职、商人学位与政治学研究生
05  WJWC 的创立 (2005) — 八名女记者、原名单 Female Reporters Without Borders、Bilakoyood 执照之争
06  每周的广场 (2007–2010) — 萨那变革广场示威与静坐、2007 新闻自由报告、2009 针对记者的审判批评
07  2011 起义（上）— 01-22 被捕 36 小时、"愤怒日" 02-03、03-17 再度被捕、广场营地数月
08  2011 起义（下）— 联合国安理会第 2014 号决议游说、10 月诺奖揭晓时的营地回应
09  2011 诺贝尔和平奖 — 与 Sirleaf/Gbowee 三人共享、诺委会引 1325 号决议、最年轻得主与首位阿拉伯女性
10  身份的多重"第一" — 首位也门人、首位阿拉伯女性、第二位穆斯林女性诺奖得主；诺委会主席 Jagland 评语
11  后诺奖岁月 (2011–2015) — 卡塔尔之行与 Belqees TV 2014、土耳其国籍 2012、胡塞入萨那后流亡伊斯坦布尔
12  声音的延续 (2016–) — Facebook 监督委员会 2020、Project Raven 网络攻击受害 2019、2023 地震救援
13  争议与界限 — Al-Islah 党籍与 2018 被停职、对多方的批评立场各按 page.md 客观一行，不作评价
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Karman 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名拼写 | 页内混用 Tawakkol/Tawakkul/Tawakel——提示词、yaml、tex 全程统一用 manifest 规范名 Tawakkol Karman |
| 诺奖理由主语 | 官方理由主语 "their"（三人共享），勿写成个人独得；三人分工互不隶属 |
| 子女数 | 正文三个孩子 vs infobox 4——两说并存，幻灯片只写"育有子女"或取正文口径，勿写死数字并加注 |
| 政治敏感红线 | 涉萨利赫政府、沙特主导联军、美国无人机政策、埃及政变、巴以表态（含 2024 年加沙言论）等内容一律按 page.md 客观记录其"表达过/批评过"，不加任何评价性语句，不摘录政治性原话做强调 |
| 摘面纱 | 2004 年会议首次不穿 niqab、电视上公开改戴彩色 hijab——这是 page.md 明载的文化主张表达，可写；勿引申为"反伊斯兰" |
| 兄弟姐妹 | 具名者仅 Safa（哈佛法学院首位也门毕业生）与 Tariq（诗人）两人在 page.md 有独立信息，其余 infobox 列名者不入库不入片 |
| Belqees TV 结局 | 2025 年因摩洛哥申诉被土耳其停播——客观记录时间线即可，不写"镇压/迫害"等定性词 |
| 2011 获奖时点 | 诺奖宣布时她仍在萨那广场营地；"最年轻得主"指当时的和平奖最年轻得主（32 岁），措辞加"当时" |
| 无载禁写 | 不写其学位获得年份（page.md 未载）；不编造 WJWC 其余七位创始记者姓名（page.md 未载）；不写与 Gbowee/Sirleaf 的私下交往 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Women Journalists Without Chains | 无锁链女记者 | WJWC，2005 创立，勿译"无枷锁"以外的生造名 |
| Al-Thawrah | 《革命报》 | 也门报纸，她创 WJWC 时供职 |
| Tahrir Square, Sana'a | 萨那变革广场 | 每周二示威地点 |
| Day of Rage | 愤怒日 | 2011-02-03 集会 |
| UNSC Resolution 2014 | 安理会第 2014 号决议 | 2011-10-21，15:0 通过 |
| UNSC Resolution 1325 | 安理会第 1325 号决议 | 2000 年通过，诺委会引为妇女与和平依据 |
| niqab / hijab | 尼卡布面纱 / 希贾布头巾 | 她的主张是"覆盖属文化而非宗教规定" |
| Al-Islah | 改革党 | 也门政党，2018 年停其党籍 |
| Belqees TV | 贝尔基斯电视台 | 2014 创立，名取示巴女王 |
| Project Raven | 渡鸦计划 | 2019 年曝光的阿联酋网络监控行动 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 开拓 / 新纪元 / 前行感
- **匹配理由**:
  - "New Lands" 呼应她从塔伊兹到萨那广场、再到伊斯坦布尔流亡发声的地理与精神迁徙
  - 曲目的前行感匹配"革命未竟、希望不灭"的自述气质
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → `presentations/21th_century/Tawakkol_Karman/New_Lands.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Tawakkol_Karman/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/21th_century/Tawakkol_Karman/images.txt` | 肖像与插图 URL |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Tawakkol_Karman.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
