# 和平奖得主立传提示词（OpenPeace 批次 1：Charles Albert Gobat）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Charles Albert Gobat（1902 诺贝尔和平奖共同得主、各国议会联盟与国际和平局的瑞士管理者）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Charles Albert Gobat（夏尔·阿尔贝·戈巴）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」与「事业领域」的结构化表达；Gobat 是「法律人出身的和平建制派」——律师、教育行政官、议员三线并行，最终以国际组织管理者的身份获奖，结构化表达的重点是「三种职业的合流」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Charles Albert Gobat（1843-05-21 特拉梅兰 ~ 1914-03-16 伯尔尼，享年 70 岁）
- **气质关键词**：**各国议会联盟的实际管理者、伯尔尼的教育改革者、倒在和平会议席上的法学家** —— 1902 诺贝尔和平奖获奖理由：
  > "for his eminently practical administration of the Inter-Parliamentary Union"（表彰他对各国议会联盟卓有实效的管理）
- **设计母题**：**法典与议事槌（codex and gavel）**。法学训练 + 议会程序 + 教育行政，三重制度感叠加——用「书脊线条 + 议席弧形」的几何意象替代空泛的橄榄枝。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Charles_Albert_Gobat/page.md`（含 frontmatter QID Q179458）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Charles_Albert_Gobat` 四件套到 `peace/presentations/pages/20th_century/Charles_Albert_Gobat/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1843-05-21 生于特拉梅兰 Tramelan ~ 1914-03-16 逝于伯尔尼，享年 70 岁；逝因：伯尔尼和平会议发言起立时倒下，约一小时后去世）
  - 国籍（瑞士）
  - 家庭（新教牧师之子；叔父 Samuel Gobat 为传教士、耶路撒冷主教）
  - 教育（巴塞尔大学、海德堡大学、伯尔尼大学、巴黎大学；1867 海德堡大学法学博士 summa cum laude）
  - 任职（伯尔尼执业律师 + 伯尔尼大学法国民法典讲师 → Delémont 开业、成为地区首要律所 → 1882 出任伯尔尼州公共教育总监三十年 → 1882 大议会、1884–1890 联邦院（Council of States）、1890–1914 国民院）
  - 关键荣誉（Nobel Peace Prize 1902 与 Ducommun 共享；其领导期间国际和平局 1910 获诺贝尔和平奖）
  - 核心事业清单（①律师与法学讲师 ②伯尔尼州公共教育改革三十年 ③联邦两院议员 ④1902 商务条约仲裁原则立法 ⑤Bureau Interparlementaire 秘书长 ⑥1906 起接掌国际和平局）
  - 关键时间线（15 节点为宜，勿凑数虚增）
- **⚠ 素材量警示**：本篇 page.md 正文约 58 行，短于 Dunant/Passy 篇。幻灯片按 12–13 页规划（见第 6 步），每页以 page.md 明载为限，宁缺毋滥。

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Charles_Albert_Gobat/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Charles_Albert_Gobat_zh`、`VIDEO_NAME=Charles_Albert_Gobat_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 仅有签名图（Albert_Gobat_Unterschrift.png），无真实肖像
- **处理方式**：封面与身份页用装饰圆占位（中央姓名首字母 C.G. 或天平/议事槌矢量图形）；签名图可作身份信息页的趣味插图（注明 signature），全篇不出现"肖像照"字样

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 4 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international arbitration | 国际仲裁 | 1902 商务条约仲裁立法、议会联盟工作 | 议会页、联盟页 |
| 1 | peace movement | 和平运动 | 国际和平局 1906 起的领导 | 和平局页 |
| 2 | education administration | 教育行政 | 伯尔尼州公共教育总监三十年 | 教育页 |
| 3 | law | 法学 | 海德堡法学博士、执业律师、民法典讲师 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 2 条与 yaml 完全一致，已入库（仅收 page.md 明载关系；本页正文极短，诚实值 relations=2）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Élie Ducommun | 无向 | 1902 诺贝尔和平奖共同得主，1906 接任其国际和平局方向 |
| colleague | William Randal Cremer | 无向 | Cremer 1889 创立各国议会联盟，Gobat 与其共事并任 Bureau Interparlementaire 秘书长 |

- 方向约定：co-honored/colleague 无向自动 from<to 归一
- **禁写清单**：叔父 Samuel Gobat（叔侄关系无类型可挂，不入库）；不编造导师/学生/妻子；国际和平局（机构）无 founder 关系（Gobat 是接任者非创始人）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：严谨、务实、法学的深绿
- **配色**：深绿（manifest 预分配主色 `#1B4D3E`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeIPU` 各国议会联盟 — 议事蓝 `#1F5F8B`
  - `badgeBureau` 国际和平局 — 枢纽红 `#A31621`
  - `badgeEdu` 教育改革 — 学院绿 `#2E7D52`
  - `badgeNobel` 1902 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 议席弧形意象（低饱和同心弧线），呼应「议事槌」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面无头像时**：装饰圆占位 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（Switzerland），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧装饰圆（或签名插图）+ 右侧信息网格，含至少：生卒、国籍、出生地、家庭（父/叔父）、教育（四校 + 1867 博士）、任职序列、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调；素材有限按 12 页规划】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 议会联盟的实干管理者 / Charles Albert Gobat 1843–1914 + 四色 badge + 装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆（签名插图）+ 右信息网格（含家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 法学与教育 / 议会生涯 / Bureau Interparlementaire / 国际和平局 / 1902 诺奖
04  特拉梅兰与求学 (1843–1867) — 牧师之家、耶路撒冷主教的叔父、四校游学、海德堡法学博士 summa cum laude
05  律师与法学讲师 — 伯尔尼执业、伯尔尼大学法国民法典讲师、Delémont 律所
06  教育改革三十年 (1882–1912) — 公共教育总监、师范培养改革、生师比预算、现代语言、职业课程
07  议会生涯 (1882–1914) — 大议会 1882、联邦院 1884–1890、国民院 1890–1914、自由改革派
08  仲裁立法 (1902) — 商务条约仲裁原则的多项立法提案
09  各国议会联盟 (1889–) — Cremer 创立背景、1892 伯尔尼第四届会议主席、Bureau Interparlementaire 秘书长
10  1902 诺贝尔和平奖 — 与 Ducommun 共享、获奖理由、1906-07-18 诺奖演讲 "The Development of the Hague Conventions of July 29, 1899"
11  掌舵国际和平局与最后一天 (1906–1914) — 接替 Ducommun 任局长、局 1910 获诺奖、1914 伯尔尼会议倒下
12  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。素材少时用大字号 + 留白，禁注水。

**Gobat 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 页面素材较少 | page.md 正文约 58 行，正文页禁编造生平细节；一切以明载三线事业（法律/教育/议会）为限 |
| 诺奖理由措辞 | 官方理由 "for his eminently practical administration of the Inter-Parliamentary Union"，强调**对各国议会联盟的管理**；获奖年份 1902，勿写 1901 |
| 共同得主 | 与 Élie Ducommun 共享 1902；1906 Ducommun 去世后 Gobat 接任国际和平局——本篇可写接任事实，勿写成"共同领导和平局获奖" |
| 机构名 | IPU 的常设局为 Bureau Interparlementaire（Gobat 任秘书长）；国际和平局（International Peace Bureau）是另一机构（1891 罗马第三届会议设立、1910 获诺奖时 Gobat 任局长）——两局勿混 |
| 两院区分 | 联邦院（Council of States）1884–1890 与国民院（National Council）1890–1914，勿混写任期 |
| 获奖归属 | 1910 诺贝尔和平奖得主是国际和平局（机构）而非 Gobat 本人，表述为"其领导期间获 1910 诺奖" |
| 叔父 | Samuel Gobat 是叔父（missionary、bishop of Jerusalem），可作早年叙述，禁建亲属关系行 |
| 死因 | 1914-03-16 伯尔尼和平会议上起立欲发言时倒下、约一小时后去世——客观记录 |
| 诺奖演讲 | 1906-07-18 "The Development of the Hague Conventions of July 29, 1899"，只写标题与日期，禁引用未载原文 |
| 无载禁写 | 不写婚姻/子女、不写政治党派细节（仅 liberal reformer 口径）、不编造与 Cremer 会面细节 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Inter-Parliamentary Union | 各国议会联盟 | 简称 IPU；获奖理由机构 |
| Bureau Interparlementaire | 议会间局 | IPU 常设信息局，Gobat 任秘书长 |
| International Peace Bureau | 国际和平局 | 与 Bureau Interparlementaire 是两个机构 |
| Council of States | 联邦院（瑞士） | 1884–1890 |
| National Council | 国民院（瑞士） | 1890–1914 |
| superintendent of public instruction | 公共教育总监 | 伯尔尼州，1882 起 30 年 |
| summa cum laude | 最优等 | 1867 海德堡法学博士 |
| international arbitration | 国际仲裁 | 1902 立法核心词 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Nostalgia** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 怀旧 / 温厚 / 制度记忆
- **匹配理由**:
  - "Nostalgia" 的温厚怀旧感匹配 Gobat 的「三十年教育行政 + 三十年议会」的长时段坚守
  - 曲目的制度记忆气质贴合其「把和平变成可操作的建制」的一生
- **本地路径**: `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → `presentations/20th_century/Charles_Albert_Gobat/Nostalgia.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Charles_Albert_Gobat/page.md` | 本地 Wikipedia 正文（事实基准，素材较短） |
| `peace/presentations/pages/20th_century/Charles_Albert_Gobat/images.txt` | 仅签名图（装饰圆占位） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Charles_Albert_Gobat.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
