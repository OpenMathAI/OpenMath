# 政治家立传提示词（OpenPeace 批次 6 实例：Sir Austen Chamberlain）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Sir Austen Chamberlain（1925 诺贝尔和平奖，《洛迦诺公约》主要缔造者之一）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Sir Joseph Austen Chamberlain（约瑟夫·奥斯汀·张伯伦爵士，KG）。
- **设计哲学**：和平奖得主（政治家/外交家类）与科学家立传的核心差异，在于必须有「身份信息页」，且叙事重心从「学术贡献」转向「外交事业与条约遗产」；「研究领域」相应替换为「事业领域」结构化表达，务必保留骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：Joseph Austen Chamberlain（1863-10-16 生于伯明翰 ~ 1937-03-16 卒于伦敦，享年 73 岁）
- **气质关键词**：**洛迦诺的缔造者、优雅的老派政治家、从未登顶的保守党领袖**
- **诺奖**：1925 诺贝尔和平奖，获奖理由（Nobel 官方英文原文照抄）：
  > "for his crucial role in bringing about the Locarno Treaty"（表彰他在促成《洛迦诺公约》中的关键作用）
- **设计母题**：**担保与仲裁（guarantee & arbitration）**。《洛迦诺公约》的核心是「相互保证西欧边界、以仲裁代替战争」——视觉语言采用条约文书、握手、界碑与天平意象；柔和圆点背景呼应欧洲新秩序的「宁静假象」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Austen_Chamberlain/page.md`
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1863-10-16 生于伯明翰 ~ 1937-03-16 卒于伦敦 24 Egerton Terrace 自宅，享年 73 岁（frontmatter 双值 03-16/03-17，**取正文与 infobox 的 03-16**）；葬于伦敦 East Finchley Cemetery
- 国籍：英国
- 家庭：父 Joseph Chamberlain（伯明翰实业家/市长，自由统一党领袖）；母 Harriet Kenrick（因生他难产去世）；姐 Beatrice Chamberlain（教育家）；同父异母弟 Neville Chamberlain（1937 年任首相，恰在其死后）
- 教育：Rugby School → Trinity College, Cambridge（剑桥辩论社副主席、1884 政治学会首讲）→ 巴黎政治学院（Sciences Po，9 个月）→ 柏林大学（12 个月，曾与俾斯麦共餐；因 Treitschke 讲座对德意志民族主义起戒心）
- 任职（含年份）：下议院议员 45 年（East Worcestershire 1892–1914；Birmingham West 1914–1937）；海军民政大臣 1895–1900；财政部政务次官 1900–1902；邮政总长 1902–1903；财政大臣两任（1903–1905、1919–1921）；印度事务大臣 1915–1917（因库特之败担责辞职）；不管部大臣 1918.4 入战时内阁；枢密院长兼下议院领袖 1921–1922（卡尔顿俱乐部会议后辞去党魁）；外交大臣 1924–1929（鲍德温第二届政府）；海军 First Lord 1931.8–11（因 Invergordon 哗变辞职）
- 关键荣誉：1925 诺贝尔和平奖；1925 嘉德勋章（KG，伊丽莎白时代以来首位未受封贵族而卒的普通嘉德骑士，第 871 位）；里昂大学荣誉博士（frontmatter 载）；自由十字勋章 1 师 3 等（frontmatter 载）
- 配偶：Ivy Muriel Dundas（1906 结婚，Henry Dundas 上校之女，1925 获 GBE）；子女 2 子 1 女：Joseph、Lawrence、Diane
- 核心事业清单：①主持《洛迦诺公约》谈判（1925.10，与 Stresemann、Briand 会于洛迦诺）②促成英国加入《凯洛格—白里安公约》③两任战时财政重建（1919）④库特之败引咎辞职的「原则性担当」⑤1934–1937 与 Churchill、Keyes、Amery 同为呼吁重整军备的少数议员
- 关键时间线（15 节点）：1863 伯明翰生 / 1892 当选议员（自由统一党） / 1893 处女演说获 Gladstone 盛赞 / 1902 邮政总长入阁 / 1903 财政大臣 / 1906 父中风后接掌关税改革运动 / 1911 与 Long 退选让位 Bonar Law / 1915 印度事务大臣 / 1917 因库特辞职 / 1919 再任财政大臣 / 1921 党魁兼枢密院长 / 1922 卡尔顿俱乐部辞职 / 1924–1929 外交大臣 / 1925 洛迦诺+诺奖+嘉德 / 1931 海军大臣辞职 / 1934–37 呼吁重整军备 / 1937 卒

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Austen_Chamberlain/` 下建 `images/`；Makefile 设 `MAIN=Austen_Chamberlain_zh`、`VIDEO_NAME=Austen_Chamberlain_zh`
- 肖像：page.md infobox 无直链肖像；正文图有 Vanity Fair 1899 讽刺画像（Spy 画）、1930 彩色 autochrome 肖像（Georges Chevalier 摄）、洛迦诺三巨头合影（Bundesarchiv）。优先 1930 autochrome 正装肖像；404 则用洛迦诺合影或装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 《洛迦诺公约》谈判与保证体系 | 洛迦诺页 |
| 1 | foreign policy | 外交政策 | 外交大臣任期（1924–1929）主线 | 外交页 |
| 2 | international relations | 国际关系 | 《凯洛格—白里安公约》、国联语境 | 公约页 |
| 3 | parliamentary politics | 议会政治 | 45 年议员、党魁、多次内阁职务 | 生平页 |
| 4 | public finance | 财政 | 两任财政大臣、战后财政重建 | 财政页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Joseph Chamberlain | 无向 | 父亲，自由统一党领袖，1892 引其入政坛 |
| spouse | Ivy Muriel Dundas | 无向 | 1906 结婚，育 2 子 1 女 |
| co-honored | Charles G. Dawes | 无向 | 1925 诺贝尔和平奖同年共同得主 |
| colleague | Gustav Stresemann | 无向 | 1925 洛迦诺谈判的德国对手方外长 |
| colleague | Aristide Briand | 无向 | 1925 洛迦诺谈判的法国外长 |
| colleague | Winston Churchill | 无向 | 1934–1937 同为呼吁重整军备的少数议员 |

- 方向约定：parent-child / spouse / colleague / co-honored 均无向（seed 幂等归一 from<to）
- 不入库（无载或无类型可归）：Neville Chamberlain（同父异母弟，无 sibling 类型）、Bonar Law / Walter Long（党魁竞争者，非 page.md 明载 rival）、Beatrice Chamberlain（姐妹）、三名子女（仅具名）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：老派的庄重、绅士的克制、条约时代的优雅
- **配色**：主色深紫 `#372A75`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeLocarno` 洛迦诺 — 金 `#C9A227`
  - `badgeDiplo` 外交 — 靛 `#4C5FD5`
  - `badgeParl` 议会 — 青绿 `#0E7C7B`
  - `badgeFin` 财政 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点，疏朗庄重，呼应「担保体系下的西欧宁静」

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**（左头像 + 右信息网格：生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 洛迦诺的缔造者 / Sir Austen Chamberlain 1863–1937 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 外交 / 议会 / 财政 / 重整军备
04  早年：父亲的政治继承人 (1863–1888) — 伯明翰、Rugby、剑桥、巴黎与柏林游学
05  议会岁月 (1892–1914) — 处女演说、连番升迁、关税改革传人
06  战时内阁 (1915–1918) — 印度事务大臣、库特之败引咎辞职
07  财政大臣与党魁 (1919–1922) — 战后财政、卡尔顿俱乐部退隐
08  外交大臣：洛迦诺的诞生 (1924–1925) — 与 Stresemann、Briand 的三边谈判（核心贡献页）
09  洛迦诺之后 — 凯洛格—白里安公约、嘉德勋章、诺奖
10  荣誉与认可 — 1925 诺贝尔和平奖 · KG · 时代封面
11  最后的呐喊 (1931–1937) — Invergordon 辞职、与 Churchill 同呼重整军备
12  遗产：他总是遵守规则，也总是输掉比赛（Churchill 评语）+ 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Chamberlain 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日双值 | frontmatter 1937-03-17 与正文 1937-03-16 并存，**取 03-16**（infobox 与正文一致） |
| 与 Neville 关系 | Neville 是**同父异母弟**（父 1868 续娶 Florence 所生），1937 年才任首相，勿写成"弟弟时任首相"；两人非 sibling 数据库类型，不入库仅叙述 |
| 洛迦诺叙事 | 促成洛迦诺的是 Chamberlain+Stresemann+Briand 三方（另邀比利时、意大利代表），勿写成他一人缔造；1925 和平奖他与 Dawes 各自获奖、理由分立（his crucial role vs Dawes Plan），勿写"共享同一理由" |
| 母亲 | Harriet Kenrick 因生他难产去世，父亲因此 25 年疏远长子——家庭创伤线索，勿略 |
| 同名区分 | 勿与 Neville Chamberlain（首相）、Houston Chamberlain 混淆；他是 Joseph Chamberlain 之**长子** |
| 党魁纪录 | 在 William Hague 之前唯一未当过首相的 20 世纪保守党领袖（正文口径），且未率党参加过大选 |
| 引语 | Gladstone 评处女演说 "one of the best speeches which has been made"、Churchill 调侃 "he always played the game, and he always lost it"、对 Mussolini "a man with whom business could be done"——仅此三条 page.md 有英文原文可引；Attlee 对质演说可转述勿整段 |
| Mussolini 评价 | 按客观事实记录（Chamberlain 曾如此评价），不加任何评价性语句 |
| 政治红线 | 爱尔兰自治、关税改革、重整军备等均只作 page.md 明载的客观事实记录，禁当代政治评价 |
| 死因 | page.md 未载死因，只写 "survived in good health until March 1937"，禁编 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Locarno Treaty | 《洛迦诺公约》 | 1925，保证西欧边界+仲裁 |
| Kellogg-Briand Pact | 《凯洛格—白里安公约》 | 勿译"白里安—凯洛格"颠倒主宾 |
| Chancellor of the Exchequer | 财政大臣 | 两任（1903–05、1919–21） |
| Foreign Secretary | 外交大臣 | 1924–1929 |
| Liberal Unionist | 自由统一党 | 1912 与保守党正式合并 |
| Carlton Club meeting | 卡尔顿俱乐部会议 | 1922.10.19，结束劳合·乔治联合政府 |
| Order of the Garter | 嘉德勋章 | 1925，KG |
| Invergordon Mutiny | 因弗戈登哗变 | 1931 辞职导火索 |
| Tariff Reform | 关税改革 | 其父发起、其接掌 |
| entente cordiale | 亲善协约 | 英法协约语境 |
| cordon sanitaire | 防疫地带 | 法国东欧同盟体系，转述 Chamberlain 设想 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**: "沉稳"匹配老派绅士政治家的克制气质；"纪录片"匹配 45 年议会生涯的时间纵深；"长期纲领"呼应洛迦诺体系作为两次大战间欧洲和平框架的历史地位——尽管它最终未能阻止战争，其缔造过程本身构成一部外交纪录。
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → 复制为 `presentations/20th_century/Austen_Chamberlain/Timeless.wav`
- **时长**: 128 秒 > 13 页 × 7 秒 ≈ 91 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Austen_Chamberlain/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Austen_Chamberlain.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；每写一页就 make，看到溢出就修。**
