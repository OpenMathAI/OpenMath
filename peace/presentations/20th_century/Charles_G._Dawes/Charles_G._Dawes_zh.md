# 政治家立传提示词（OpenPeace 批次 6 实例：Charles G. Dawes）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Charles G. Dawes（1925 诺贝尔和平奖，《道威斯计划》主持者、美国第 30 任副总统）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Charles Gates Dawes（查尔斯·盖茨·道威斯）。
- **设计哲学**：和平奖得主（银行家/政治家类）立传的骨架与科学家版一致（身份信息页 + 事业领域结构化），但叙事重心是「经济外交与战后重建」；本例的独特性在于其音乐家副业——唯一有冠军单曲署名的美国副总统，可做一页彩蛋。

---

## 二、背景信息 【人物专属】

- **目标人物**：Charles Gates Dawes（1865-08-27 生于俄亥俄州 Marietta ~ 1951-04-23 卒于伊利诺伊州 Evanston 自宅，享年 85 岁，死因冠状动脉血栓）
- **气质关键词**：**战火中的银行家、道威斯计划的总设计师、会作曲的副总统**
- **诺奖**：1925 诺贝尔和平奖（co-recipient），获奖理由（Nobel 官方英文原文照抄）：
  > "for his crucial role in bringing about the Dawes Plan"（表彰他在促成《道威斯计划》中的关键作用）
- **设计母题**：**流动与平衡（flow & balance）**。道威斯计划的本质是让美国资本重新流入德国、让赔偿链条重新转动、让法德从对峙走向结算桌——视觉语言采用资产负债表、天平、货币流通与铁路时刻表意象。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Charles_G._Dawes/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）；`peace/presentations/cover/`（项目首页）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1865-08-27 生于 Marietta, Ohio ~ 1951-04-23 卒于 Evanston, Illinois（85 岁，coronary thrombosis）；葬于芝加哥 Rosehill Cemetery
- 国籍：美国（共和党）
- 家庭：父 Rufus Dawes（内战准将，Iron Brigade 第 6 威斯康星团指挥）；母 Mary Beman Gates；兄弟 Rufus C. / Beman Gates / Henry May Dawes 均为实业家或政治家；先祖含五月花号乘客 Edward Doty 与与 Paul Revere 同骑报信的 William Dawes
- 教育：Marietta College 学士 1884 → Cincinnati Law School 法学士 1886（Delta Upsilon 兄弟会）
- 任职（含年份）：内布拉斯加州执业律师 1887–1894；燃气公司总裁（La Crosse Gas Light / Northwestern Gas Light and Coke）；1896 主持 McKinley 伊利诺伊竞选；货币监理官 1898–1901；Central Trust Company of Illinois 总裁 1902–1921；一战任军需采购委员会主席（准将，1917–1919，Distinguished Service Medal + 法国 Croix de Guerre）；预算局首任局长 1921–1922；盟国赔偿委员会 1923 → 道威斯计划；副总统 1925–1929（柯立芝任内）；驻英大使 1929–1931；复兴金融公司（RFC）总裁 1932（数月）；City National Bank and Trust 总裁 1932–1951
- 关键荣誉：1925 诺贝尔和平奖；Distinguished Service Medal；World War I Victory Medal；英国巴斯勋章 Companion / 法国荣誉军团勋章 Commander / 比利时利奥波德勋章 Commander / 法国 Croix de Guerre（棕榈）
- 配偶：Caro Blymyer（1889-01-24 结婚）；亲子 Rufus Fearing（1890–1912，Geneva Lake 溺亡，21 岁）与 Carolyn；养子 Dana、Virginia
- 核心事业清单：①主持制定道威斯计划（美国银行贷款德国→赔偿法比→法比撤出鲁尔）②预算局首任局长（联邦预算制度奠基）③一战 AEF 军需采购体系④副总统任内抨击参议院冗长辩论、力推 McNary–Haugen 农业法案⑤自学者作曲——Melody in A Major（1912 闻名，1951 Carl Sigman 填词为 It's All in the Game，1958 冠军单曲）
- 关键时间线（15 节点）：1865 Marietta 生 / 1884 Marietta College / 1886 律师 / 1894 转营燃气业 / 1896 McKinley 竞选操盘 / 1898 货币监理官 / 1902 Central Trust 总裁 / 1912 长子溺亡·建收容所纪念 / 1917–1919 一战军需准将 / 1921 预算局首任局长 / 1923 盟国赔偿委员会·道威斯计划 / 1925 诺奖+就任副总统 / 1929–1931 驻英大使 / 1932 RFC 与银行重组 / 1951 卒于 Evanston

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `peace/presentations/20th_century/Charles_G._Dawes/images/`；Makefile 设 `MAIN=Charles_G._Dawes_zh`
- 肖像：page.md infobox 无直链；正文图有 1918 军装照（NARA）与 Coolidge–Dawes 合影。优先军装照或 1920s 正装照；404 则装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | public finance | 公共财政 | 预算局首任局长、战后财政重建 | 预算页 |
| 1 | banking | 银行业 | Central Trust / City National 总裁 | 银行页 |
| 2 | international diplomacy | 国际外交 | 道威斯计划、驻英大使 | 诺奖页 |
| 3 | politics | 政治 | 副总统 1925–1929 | 副总统页 |
| 4 | music composition | 音乐创作 | Melody in A Major / It's All in the Game | 彩蛋页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Rufus Dawes | 无向 | 父亲，内战准将，Iron Brigade 指挥官 |
| spouse | Caro Blymyer | 无向 | 1889 结婚，1 子 1 女加 2 养子女 |
| co-honored | Sir Austen Chamberlain | 无向 | 1925 诺贝尔和平奖同年共同得主 |
| colleague | John Pershing | 无向 | 内布拉斯加相识的终身挚友，一战并肩 |
| colleague | Calvin Coolidge | 无向 | 1925–1929 在柯立芝政府任副总统 |
| colleague | Herbert Hoover | 无向 | 1929 任命驻英大使，1932 引其执掌 RFC |

- 方向约定：全部无向（seed 幂等归一 from<to）
- 不入库（无类型可归或仅具名）：Owen Young（杨格计划继任者，非合作）、Frank O. Lowden（政治同盟）、William Jennings Bryan（因自由白银分歧仍为友——无稳定类型）、兄弟四人、子女四人

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：账簿的严谨、军装的硬朗、旋律的抒情
- **配色**：主色深红 `#7A1E28`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgePlan` 道威斯计划 — 金 `#C9A227`
  - `badgeBudget` 预算 — 靛 `#4C5FD5`
  - `badgeArmy` 军旅 — 军绿 `#4A5D3A`
  - `badgeMusic` 音乐 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点，账本行距般的横向节奏

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 道威斯计划总设计师 / Charles G. Dawes 1865–1951 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 银行 / 预算 / 军旅 / 外交 / 音乐
04  早年：内战将领之子 (1865–1896) — Marietta、律师、燃气实业
05  货币监理官与银行家 (1898–1921) — McKinley 操盘、Central Trust
06  一战：AEF 军需采购体系 (1917–1919) — 准将、DSM、Croix de Guerre
07  预算局首任局长 (1921–1922) — 联邦预算制度奠基
08  道威斯计划：让欧洲重新流动 (1923–1925)（核心贡献页）— 赔偿委员会、鲁尔撤军、诺奖
09  副总统：与参议院的战争 (1925–1929) — 就职演说抨击 rule XXII、Warren 提名风波、McNary–Haugen
10  驻英大使与 RFC (1929–1932) — 拒穿及膝裤、大萧条中的银行救援
11  彩蛋页：会作曲的副总统 — Melody in A Major → It's All in the Game（1958 冠军单曲）
12  遗产：唯一的诺贝尔奖+冠军单曲双冠者 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Dawes 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 与 Chamberlain 的关系 | 1925 和平奖两人**同年各自获奖、理由分立**（Dawes Plan vs Locarno Treaty），正文明载 "co-recipient … shared the Nobel Peace Prize"；勿写成"共享同一理由"，页面正文与纪念页均无两人同框记录，禁写共同颁奖场景 |
| 就职日期张力 | 就职演说抨击参议院 rule XXII 与 Warren 提名失败均在 1925-03-04 任职当日前后（3-04 与 3-10），年份勿错写为 1924 |
| 音乐事实 | Melody in A Major 1912 走红、1951 Carl Sigman 填词、1958 Tommy Edwards 版 Billboard 冠军六周——三个年份勿混；他是唯一有冠军单曲署名的美国副总统，与 Bob Dylan 是仅有的两位"诺奖+冠军单曲署名"者 |
| 儿子之死 | Rufus Fearing 1912-09-05 溺亡于 Geneva Lake，时年 21 岁，普林斯顿学生；收容所与 Lawrenceville 宿舍为纪念所建 |
| 死因 | 1951-04-23 卒于 Evanston 自宅，coronary thrombosis（page.md 明载可写） |
| RFC 争议 | 政敌指控 RFC 优待其自任主席的 Central Republic Bank——客观记录，不加评价 |
| 俚语绰号 | "Hell and Maria Dawes" 来自 1921 参议院听证语出，他自称实为 "Helen Maria"——两种口径并存须同时写 |
| 引语 | 就职演说句 "I should hate to think that the Senate was as tired of me …" 与 1921 听证句 "Hell and Maria, we weren't trying to keep a set of books …" 仅此两条 page.md 有英文原文可引 |
| 政治红线 | 反 KKK 演讲、攻击 La Follette 等只作客观事实记录，禁当代政治评价 |
| 军衔时间线 | 1917-06 少校 → 1917-07 中校 → 1918-01 上校 → 1918-10 准将，逐级勿跳 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Dawes Plan | 道威斯计划 | 1924–1929，杨格计划取代 |
| Young Plan | 杨格计划 | 1929，Owen Young 主持 |
| Bureau of the Budget | 预算局 | 今 OMB 前身，勿写"现名" |
| Comptroller of the Currency | 货币监理官 | 1898–1901 |
| Vice President | 副总统 | 第 30 任 |
| Reconstruction Finance Corporation | 复兴金融公司（RFC） | 1932，数月即辞 |
| Allied Reparations Commission | 盟国赔偿委员会 | 1923 |
| Occupation of the Ruhr | 鲁尔占领 | 1923-01 起，道威斯计划后撤军 |
| Versailles Treaty | 《凡尔赛条约》 | 赔偿义务来源 |
| Melody in A Major | A 大调旋律 | 1912 |
| It's All in the Game | 《一切皆游戏》 | 1951 填词、1958 冠军 |
| filibuster | 冗长辩论 | rule XXII |
| Distinguished Service Medal | 优异服役勋章 | 美国陆军 |
| Croix de Guerre | 战争十字勋章 | 法国 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 历史感 / 深沉 / 追忆
- **匹配理由**: "历史感/深沉"匹配一战军旅与大萧条银行救援的厚重叙事；"追忆"呼应其journal 系列著述习惯（A Journal of the Great War / Notes as Vice President / Journal as Ambassador），一位用日记丈量时代的记录者。
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/20th_century/Charles_G._Dawes/PAST.wav`
- **时长**: 128 秒 > 13 页 × 7 秒 ≈ 91 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Charles_G._Dawes/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Charles_G._Dawes.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；每写一页就 make，看到溢出就修。**
