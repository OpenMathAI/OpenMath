# 和平奖得主立传提示词（OpenPeace 模板实例：Auguste Beernaert）

> **本文件是 OpenPeace 的「人物专属立传提示词」**，以 Kenneth_G_Wilson_zh.md（0–11 节结构母本）为结构标杆，
> 以 Frederick_Sanger.yaml 为 yaml 字段母本，为 Auguste Beernaert（1909 诺贝尔和平奖得主，比利时前首相）定制。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Beernaert 专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 体系，与 OpenPhysicist / OpenChemist / OpenMedic 平级）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的任务流程骨架 + 诺贝尔奖立传通用版式。
- **本实例**：Auguste Marie François Beernaert（奥古斯特·贝尔纳特，比利时首相 1884–1894，1909 诺贝尔和平奖得主之一）。
- **设计哲学**：和平奖得主立传强调「事业与机构」的结构化表达——Beernaert 是「政坛耆宿转任国际调停人」的典型：首相任内治国，卸任后在海牙和会与国际仲裁领域再攀高峰，须以身份信息页与事业领域表呈现「国内政治 → 国际法」的双幕结构。

---

## 二、背景信息 【人物专属】

- **目标人物**：Auguste Marie François Beernaert（1829-07-26 ~ 1912-10-06，享年 83 岁）
- **姓名**：英文 Auguste Beernaert（全名 Auguste Marie François Beernaert）；中文 奥古斯特·贝尔纳特
- **国籍**：比利时（生于尼德兰联合王国奥斯坦德，今比利时）
- **诺奖年份**：1909（与法国的 Paul Henri d'Estournelles de Constant 共享）
- **官方获奖理由英文原文**（照抄 nobel_peace_citations.json，禁止改写）：
  > "for their prominent position in the international movement for peace and arbitration."
- **官方获奖理由中译**（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）：
  > 表彰他们在国际和平与仲裁运动中的杰出地位
- **气质关键词**：**治国十年的天主教派首相、海牙和会的比利时首席代表、海洋法统一的推动者**
- **设计母题**：**天平与锚（scales and anchor）**。天平象征其律师/法官出身与对国际仲裁的信仰，锚象征其公共工程任内改善铁路运河航道以及 1910 年海上碰撞救助公约——「法度与航道」的双重意象贴合其司法与海事两大事业；封面可用天平与锚的对称图形。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Auguste_Beernaert/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/`（OpenPeace 共享封面）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，全部取自 page.md，无载禁补】

- 生卒：1829-07-26 生于奥斯坦德（Ostend，时属尼德兰联合王国，今比利时）~ 1912-10-06 逝于瑞士卢塞恩（Lucerne），享年 83 岁
- 国籍：比利时（Nobel 官方口径）
- 家庭：page.md 无载（父母、配偶、子女禁写）
- 教育：17 岁进入鲁汶天主教大学（Catholic University of Leuven）法学院，五年后以最高荣誉（greatest distinction）毕业；另就学海德堡大学（frontmatter educated_at 明载；海德堡专业/年份无载禁写）
- 任职机构与经历（infobox 明载年份）：
  - 律师出身；1873 年当选众议院（Chamber of Deputies）议员
  - 在 Jules Malou 内阁任公共工程大臣，大幅改善铁路、运河与道路系统
  - 比利时首相 1884-10-26 ~ 1894-03-26（Catholic Party；兼任财政大臣 1884–1894；君主 Leopold II；前任 Jules Malou，继任 Jules de Burlet）
  - 众议院议长（President of the Chamber of Representatives）1896-01-30 ~ 1900-07-18
- 国际事务与和平事业：
  - 比利时出席 1899 与 1907 两次海牙和会的首席代表；1907 年海牙和平会议主席
  - 国际法协会（international law association）主席 1903–1905
  - 1909 年诺贝尔和平奖（与 d'Estournelles de Constant 共享），表彰其在常设仲裁法院（Permanent Court of Arbitration）的工作
  - 1911 年出任常设仲裁法院 Savarkar 案仲裁庭庭长
  - 统一国际海事法提案的主要推动者；1910 年起草的海上碰撞与救助公约很快被多国签署
- 关键荣誉：1909 诺贝尔和平奖；frontmatter 另载大量勋章（Legion of Honour Grand Cross、Order of Leopold Grand Cordon 等——展示时择要，不必全列）
- 晚年与去世：1912 年在卢塞恩住院，死于肺炎
- 关键时间线（18 节点，全部 page.md/infobox 明载）：
  1. 1829-07-26 生于奥斯坦德
  2. 17 岁入鲁汶天主教大学法学院
  3. 五年后以最高荣誉毕业
  4. 就学海德堡大学
  5. 律师执业
  6. 1873 当选众议院议员
  7. 出任公共工程大臣（Malou 内阁）
  8. 改善铁路、运河、道路系统
  9. 1884-10-26 出任比利时首相（兼财政大臣）
  10. 首相任期至 1894-03-26
  11. 1896-01-30 出任众议院议长
  12. 1900-07-18 卸任议长
  13. 1903–1905 任国际法协会主席
  14. 1899、1907 两度率比利时代表团出席海牙和会
  15. 1907 任海牙和平会议主席
  16. 1909-12-10 获诺贝尔和平奖（与 d'Estournelles de Constant 共享）
  17. 1910 海上碰撞与救助公约起草并被多国签署；1911 出任 Savarkar 案仲裁庭庭长
  18. 1912-10-06 逝于卢塞恩（肺炎）

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Auguste_Beernaert/` 下建 `images/`
- Makefile 设置 `MAIN=Auguste_Beernaert_zh`、`VIDEO_NAME=Auguste_Beernaert_zh`
- 肖像：page.md 内嵌 Commons 图 `Auguste_Beernaert.jpg`（c. 1900，250px 改 500px 下载）；404 则用装饰圆占位

### 第 4 步：研究领域/事业领域表 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international arbitration | 国际仲裁 | 常设仲裁法院工作、Savarkar 案庭长 | 仲裁页 |
| 1 | international law | 国际法 | 海牙和会、国际法协会主席 | 海牙页 |
| 2 | maritime law | 海事法 | 推动国际海事法统一，1910 公约 | 成就页 |
| 3 | diplomacy | 外交 | 比利时首席代表、和会主席 | 海牙页 |
| 4 | politics | 政治 | 首相十年、众议院议长 | 政坛页 |

- yaml `fields` 与上表一致（5 条）；入库 `person_field` 带 rank

### 第 4.5 步：社会关系表 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Paul Henri d'Estournelles de Constant | 无向 | 1909 诺贝尔和平奖共同得主 |
| colleague | Permanent Court of Arbitration | 无向 | 1909 诺奖表彰其在常设仲裁法院的工作；1911 任 Savarkar 案仲裁庭庭长 |
| colleague | International Law Association | 无向 | 1903–1905 任主席 |

- 对方 name_en 用 manifest 规范名 `Paul Henri d'Estournelles de Constant`；两个机构 stub 为 org 占位
- Jules Malou（上司/前任首相）、Leopold II（君主）系职务性关系，不入库

### 第 5 步：配色方案 【模板通用，人物专属色彩】

- **气质**：法度的庄重、执政的沉稳、晚年转向国际和平的从容
- **配色**：主色 `#5C3A1E`（深棕，manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + badgeA–D 四分类色
  - `badgeA` 国际仲裁 — 靛蓝 `#3F51B5`
  - `badgeB` 国际法与海牙 — 青绿 `#0E7C7B`
  - `badgeC` 海事法 — 琥珀 `#E07B30`
  - `badgeD` 政坛岁月 — 玫瑰 `#C4204F`
- **背景母题**：天平与锚的对称剪影 + 稀疏的金色圆点，呼应「法度与航道」母题

### 第 6 步：规划幻灯片序列 【人物专属，14–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 从首相到国际调停人 / Auguste Beernaert 1829–1912 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、全名、政党、教育、首相任期、议长任期、荣誉、诺奖）
03  事业概览 — 国际仲裁 / 国际法 / 海事法 / 外交 / 国内政坛
04  鲁汶与海德堡 (1829–1873) — 法学训练、最高荣誉毕业
05  入政坛 (1873–1884) — 众议员、公共工程大臣、基建改良
06  首相十年 (1884–1894) — Catholic Party、兼任财政大臣、Leopold II 朝
07  众议院议长 (1896–1900)
08  海牙和会 (1899 / 1907) — 比利时首席代表、1907 会议主席
09  国际仲裁与常设仲裁法院 — 1909 诺奖理由、1911 Savarkar 案庭长
10  海事法的统一 — 1910 碰撞与救助公约
11  1909 诺贝尔和平奖 — 与 d'Estournelles de Constant 共享，官方理由（二人同句）
12  荣誉与晚年 — 主要勋章择要、1912 卢塞恩
13  遗产 — 海牙传统与国际仲裁的奠基一代
14  结尾
```

### 第 7–8 步：Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`
- 每写完一页 `make distclean && make`，`pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- 荣誉页条目多，用 `itemize \itemsep -2.5pt + topsep 0 + arraystretch 0.6` 压缩，只列 3–4 项勋章

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Beernaert 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 出生地国别 | 生于奥斯坦德时属**尼德兰联合王国**（United Kingdom of the Netherlands，1829 年比利时尚未独立）；国籍栏按 Nobel 口径写比利时，出生地须注历史国名 |
| 首相起讫 | infobox 明载 1884-10-26 ~ 1894-03-26；正文又写 "October 1884 to March 1894"，两处一致，勿写成其他年份 |
| 财政大臣 | 首相任内**兼任**财政大臣 1884–1894，勿写成卸任首相后转任 |
| 议长 vs 议员 | 1873 当选的是众议员（Chamber of Deputies）；1896–1900 任的是众议院**议长**（President of the Chamber of Representatives），两职勿混 |
| 海牙年份口径 | 正文先写 "Hague conventions of 1899 and 1907"，后又写 "Hague Peace Conferences (1898 and 1907)"（d'Estournelles 篇亦有 1898/1899 两说）——本篇以 **1899** 为准（"Hague conventions of 1899 and 1907" 与 "first representative to the Hague peace conferences in 1899 and 1907" 两处均为 1899） |
| 机构名 | "president of the international law of association" 系 page.md 原文，规范名按 **International Law Association**（国际法协会），任期 1903–1905 |
| Savarkar 案 | 1911 年任常设仲裁法院 Savarkar 案仲裁庭庭长，系 page.md 明载，客观表述即可 |
| 获奖理由口径 | 官方理由是 "their prominent position"（二人共享、理由同句）；勿写成个人专属理由 |
| 无载禁写清单 | 家庭（父母/配偶/子女）、海德堡就读专业年份、勋章的具体获得年份、去世前的详细病情发展——page.md 无载一律禁写（死因肺炎有载可写） |
| 政治敏感红线 | 涉及君主制、教派政治（Catholic Party）只作客观事实记录，不加评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Permanent Court of Arbitration | 常设仲裁法院 | PCA，勿与海牙国际法院（ICJ）混淆 |
| Hague Peace Conference | 海牙和平会议 | 1899/1907 两届 |
| International Law Association | 国际法协会 | page.md 原文拼写不规范，入库用规范名 |
| maritime law | 海事法 | 与 international law（国际法）分列 |
| Chamber of Representatives | 众议院 | 比利时下院 |
| prime minister | 首相 | 1884–1894 |
| minister of public works | 公共工程大臣 | 升官前职 |
| Catholic Party | 天主教党 | 比利时历史政党 |
| Savarkar Case | Savarkar 案 | 1911 仲裁案 |
| greatest distinction | 最高荣誉 | 鲁汶毕业评级 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配，勿改】

- **选定曲目**：**Eternals** — Alex-Productions
- **bgm_path**：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`
- **匹配理由**：宏大而恒久的气质，匹配 Beernaert 横跨国内治理与国际法两个时代的漫长公共生涯（1873–1912 近四十年），以及海牙仲裁体系「永久法院」（Permanent Court）的恒常意味。
- **备选**（未采用，仅存档）：The Flow of Time（时间感重复用曲）、Pathfinder（开拓感更贴合外交场景但不及其国政厚度）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Auguste_Beernaert/page.md` | 本地 Wikipedia 正文（唯一事实来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参考 |
| `peace/presentations/cover/` | OpenPeace 共享封面 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |

> **开始执行。每完成一步汇报。**
