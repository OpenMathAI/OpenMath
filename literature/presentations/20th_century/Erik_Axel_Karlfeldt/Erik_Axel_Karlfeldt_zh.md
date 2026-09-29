# 文学家立传提示词（Erik Axel Karlfeldt）

> **OpenLiterature 人物专属立传提示词**：Erik Axel Karlfeldt（埃里克·阿克塞尔·卡尔费尔德，1931 诺贝尔文学奖，瑞典诗人）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用名句引文框/意象图式/书影替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Erik Axel Karlfeldt（本名 Erik Axel Eriksson），瑞典诗人，1931 年诺贝尔文学奖（身后追授）。
- **设计哲学**：文学家立传必须有「身份信息页」，并以**代表作书影/名句引文框/意象图式**替代物理学家侧的公式框——本篇设计母题为「北方的暮色与森林钟声」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Erik Axel Karlfeldt（1864-07-20 ~ 1931-04-08，享年 66 岁）
- **气质关键词**：**瑞典学院常任秘书、身后追授的桂冠诗人、达拉纳风土的象征主义者**
- **官方获奖理由（禁止改写）**：
  - EN: "The poetry of Erik Axel Karlfeldt"
  - 中译（取自 `literature/generate_20th_century_list.py` CITATION_ZH）：「埃里克·阿克塞尔·卡尔费尔德的诗歌」
  - 注：1931 为身后授奖（1931-04-08 去世后追授），由瑞典学院院士 Nathan Söderblom 提名。
- **设计母题**：**北方的暮色与森林钟声**。达拉纳（Dalarna）农庄出身、泛神论者，其诗被概括为「以地域主义面貌出现的象征主义」——视觉语言用北欧暮光、林间空地、农庄木屋与钟声波纹。
- **本地数据源**：`literature/presentations/pages/20th_century/Erik_Axel_Karlfeldt/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Erik_Axel_Karlfeldt
- **肖像**：第 0 步待下载（page.md 头图 "Karlfeldt in 1931"；images.txt 无 URL 则按 workflow 回退 REST API / Special:FilePath，404 用装饰圆占位）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：第 4 步研究领域入库 + 第 4.5 步社会关系入库，写入 greatminds 库（MySQL）。

### 第 0 步：事实基准 【人物专属】（已核对 page.md）

- 生卒：1864-07-20 生于瑞典卡尔博（Karlbo，达拉纳省）~ 1931-04-08 逝于斯德哥尔摩，享年 66 岁
- 本名与改名：原名 **Erik Axel Eriksson**，农家子弟；1889 年改姓 Karlfeldt，欲与曾受刑事定罪之辱的父亲拉开距离
- 教育：乌普萨拉大学（Uppsala University）；求学期间在多地教书自养（含斯德哥尔摩郊区 Djursholms samskola 与成人学校）
- 早期任职：毕业后在瑞典皇家图书馆（Royal Library of Sweden）任职五年
- 瑞典学院：1904-12-20 当选院士（第 11 席，前承 Clas Theodor Odhner，后继 Torsten Fogelqvist）；1905 入诺贝尔研究所；1907 入诺贝尔委员会；常任秘书——正文作 1912 年当选，infobox 就任栏作 1913 年 2 月（两口径并存，见第 9 步陷阱表），任职至 1931 年去世，后继 Per Hallström
- 荣誉：1931 诺贝尔文学奖（身后）；1917 乌普萨拉大学荣誉博士（doctor honoris causa）；Samfundet De Nio 大奖（frontmatter award_received）
- 信仰：泛神论者（pantheist）
- 1919 年曾被授予诺奖但**婉拒**（因身兼评奖机构常任秘书之职）
- 英译作品：Modern Swedish Poetry Part 1（1929，C. D. Locock 译）、Arcadia Borealis（1938，Charles Wharton Stork 译）、The North! To the North!（2001，Judith Moffett 等译）
- 关键时间线（15 节点示例）：1864 生于 Karlbo → 农家童年 → 1889 改名 → 乌普萨拉求学兼教书 → 皇家图书馆五年 → 1904 入瑞典学院 → 1905 诺贝尔研究所 → 1907 诺贝尔委员会 → 1912/1913 常任秘书 → 1917 荣誉博士 → 1919 拒奖 → 1931-04-08 去世 → 1931 身后授诺奖 → 1938 Arcadia Borealis 英译 → 2001 The North! To the North! 英译

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- `literature/presentations/20th_century/Erik_Axel_Karlfeldt/` + `images/`；Makefile 复制同侧成品改 `MAIN=Erik_Axel_Karlfeldt_zh`；肖像按第 0 步下载并 `file` 验证。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | 诗人身份核心（1931 授奖理由即"其诗歌"） | 核心页 |
| 1 | symbolist poetry | 象征主义诗歌 | 导语定评：以地域主义面貌出现的象征主义 | 核心页 |
| 2 | regionalism | 地域主义 | 达拉纳农庄风土书写的表层面貌 | 风土页 |
| 3 | Swedish literature | 瑞典文学 | 瑞典语写作；瑞典学院核心成员 | 学院页 |

- 入库：`MySQL/seed_person.py data/Erik_Axel_Karlfeldt.yaml`；校验 `person_field` rank 序。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 仅收 page.md 明载；Karlfeldt 无配偶/师承/门生记载，关系三条均为瑞典学院同僚。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Nathan Söderblom | 无向 | 瑞典学院院士，1931 年为其提名诺奖 |
| colleague | Per Hallström | 无向 | 瑞典学院常任秘书继任者（1931） |
| colleague | Torsten Fogelqvist | 无向 | 瑞典学院第 11 席位继任者 |

### 第 5 步：配色 【人物专属】

- 主色 `#17435B`（分批文件预分配，深瑞典蓝）+ 诺奖香槟金 `C9A227` + badgeA–D 四分类色（badgeA 抒情 `#3E7CB1` / badgeB 象征 `#7A5C9E` / badgeC 地域 `#5C8A4E` / badgeD 学院 `#B08A2E`）。
- 背景母题：稀疏暮色圆与林间光斑（呼应「北方暮色与森林钟声」）。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像+细边框）；封面国籍行 `Sweden`。
2. **身份信息页必做**：左头像+右信息网格（生卒/本名 Erik Axel Eriksson/国籍/出生地 Karlbo/教育/瑞典学院职务/主要荣誉/核心领域）。
3. 品牌口径：结尾页底部统一 `OpenMathAI`；引号半角 `" "`。
4. 无公式框——用名句引文框（Karlfeldt 诗句暂无 page.md 英文原文，引文框**只放 1931 官方获奖理由原句**或英文译本书目条目，禁编造诗句）、书影、意象图式替代。

### 第 6 步：幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 身后追授的桂冠诗人 / Erik Axel Karlfeldt 1864–1931 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心概览 — 抒情诗 / 象征主义 / 地域主义 / 瑞典学院
04  达拉纳农家子 (1864–1889) — 本名 Eriksson、父之耻与改名
05  乌普萨拉与皇家图书馆 (1880s–1900s) — 教书自养的求学岁月
06  瑞典学院三十年 (1904–1931) — 第 11 席 / 诺贝尔研究所 / 诺贝尔委员会
07  常任秘书：评奖席上的人 (1912/1913–1931) — 双口径标注
08  1919：从评奖者到拒绝者 — 婉拒诺奖的伦理处境
09  1931：身后追授 — Söderblom 提名 / 官方理由原句引文框
10  诗的世界：北方暮色与森林钟声 — 泛神论 / 达拉纳意象图式
11  英译与身后传播 — 1929/1938/2001 三部英译
12  遗产与结尾
```

### 第 7–8 步：Beamer 与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}`；头部宏（配色/plainbar/deckbackground/sectiontitle/lab/infob）复用同侧成品骨架；每写一页 make 并 pdftoppm 目检溢出。

### 第 9 步：史实 + 术语审查 【人物专属】

**Karlfeldt 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名 | 原名 Erik Axel Eriksson；改姓 1889 年，缘由是父亲受刑事定罪之辱——勿写成"笔名雅趣" |
| 常任秘书年份 | 正文作 1912 年当选，infobox 就任栏作 1913 年 2 月——两口径并列或取"1912 当选、1913 就任"，勿混写成同一年 |
| 1919 拒奖 | 曾被授予诺奖但因常任秘书身份婉拒——勿写成"落选后再获" |
| 身后授奖 | 1931 为去世后追授——勿添加"史上唯一/首次身后文学奖"等 page.md 未载之断言 |
| 获奖理由 | 官方仅一句 "The poetry of Erik Axel Karlfeldt"，禁扩写成"表彰其描绘瑞典农民生活"之类 |
| 瑞典语诗集名 | page.md 正文未载其瑞典语诗集（如 Fridolin 系列）任何书名——**禁编造作品名**，作品页只列三部英译 |
| 泛神论 | 仅写 pantheist 一词，勿展开神学叙事 |
| 无师承/门生 | page.md 无任何师承记载——禁从"象征主义"反推影响者 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Swedish Academy | 瑞典学院 | 授奖机构，勿与"诺贝尔委员会"混同 |
| permanent secretary | （瑞典学院）常任秘书 | 1912/1913 双口径 |
| seat No. 11 | 第 11 席 | 前承 Odhner、后继 Fogelqvist |
| posthumous | 身后追授 | 勿加"唯一" |
| pantheism | 泛神论 | 一词带过 |
| Dalarna | 达拉纳（省） | 出生地 Karlbo 所在 |
| doctor honoris causa | 荣誉博士 | 1917，乌普萨拉 |
| Samfundet De Nio | 九人社（瑞典文学社团） | frontmatter 获奖，非诺奖 |
| Arcadia Borealis | 《北方乐园》（英译本） | 1938，Stork 译 |
| regionalism | 地域主义 | 表层面貌 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions
- **匹配理由**: "历史感/深沉" 匹配 Karlfeldt 的双重返境——生前甘居评奖席后三十年的静默，与身后追授的历史回响；北欧暮色的庄重感与该曲的沉郁气质同构。
- **备选**（未采用）: Nostalgia（怀旧感强，但本篇主线是"迟到的桂冠"而非乡愁）；Timeless（受众更高但已被 turing 侧 2007-2015 批次多人使用）。
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/20th_century/Erik_Axel_Karlfeldt/PAST.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Erik_Axel_Karlfeldt/page.md` | 事实基准（已核对） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
