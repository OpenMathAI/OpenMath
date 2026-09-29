# 政治家立传提示词（OpenPeace 批次 6 实例：Gustav Stresemann）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Gustav Stresemann（1926 诺贝尔和平奖，魏玛共和国总理兼外交部长）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Gustav Ernst Stresemann（古斯塔夫·恩斯特·施特雷泽曼）。
- **设计哲学**：和平奖得主（国务家类）立传保留「身份信息页 + 事业领域结构化」骨架；本例的叙事弧线是**从战时吞并主义者到法德和解者的转变**——魏玛共和的「理智共和派」，死时被视为"维持政治体系脆弱平衡的人"。

---

## 二、背景信息 【人物专属】

- **目标人物**：Gustav Ernst Stresemann（1878-05-10 生于柏林 ~ 1929-10-03 卒于柏林，享年 51 岁，死因一连串中风）
- **气质关键词**：**脆弱平衡的维持者、理智共和派、以经济换空间的现实主义者**
- **诺奖**：1926 诺贝尔和平奖（与法国外长 Briand 共享），获奖理由（Nobel 官方英文原文照抄，their 为共享口径）：
  > "for their crucial role in bringing about the Locarno Treaty"（表彰他们在促成《洛迦诺公约》中的关键作用）
- **设计母题**：**平衡与转变（balance & transformation）**。他在君主主义信念与魏玛现实之间、在赔偿重负与复兴空间之间走钢丝——视觉语言采用天平、钢丝与折返的轨迹线；「Stresemann 晨礼服」可作为页脚装饰彩蛋。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Gustav_Stresemann/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）；`peace/presentations/cover/`（项目首页）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1878-05-10 生于柏林 Köpenicker 大街 66 号 ~ 1929-10-03 卒于柏林（51 岁，series of strokes，就在说服国会接受杨格计划数小时后）；葬于柏林 Kreuzberg 的 Luisenstadt 墓园（Hugo Lederer 雕墓）
- 国籍：德国；党派轨迹：民族自由党 1907–1918 → 短暂德国民主党 1918 → 德国人民党（DVP，1918-12-15 创立并任主席至 1929）
- 家庭：家中 7 个孩子最幼；父为啤酒分装工兼小酒馆主；母 Mathilde 1895 去世；1903 娶 Käte Kleefeld（1883–1970，柏林富商之女，Kurt von Kleefeld 之妹）；两子 Wolfgang（后任柏林爱乐乐团经理）与 Hans-Joachim
- 教育：Andreas-Gymnasium（16 岁入学）；柏林大学 1897-04 起（改学政治经济学）；莱比锡大学 1898 起（历史与国际法），1901-01 博士论文论柏林瓶装啤酒业，导师经济学家 Karl Bücher
- 任职（含年份）：萨克森制造商协会 1902 创立；德累斯顿市议员 1906；德意志帝国国会议员 1907–1918（Saxony 21 → Hannover 2）；1917 接替 Ernst Bassermann 任民族自由党党魁；魏玛国会议员 1920–1929；总理 1923-08-13~11-30（大联合政府，兼任外长）；外交部长 1923-08-13~1929-10-03（连任七届政府至死）
- 关键荣誉：1926 诺贝尔和平奖
- 核心事业清单：①终结鲁尔消极抵抗（1923-09-26）与 Rentenmark 遏制恶性通胀②道威斯计划（1924，削减赔偿总额、重组帝国银行、结束鲁尔占领）③《洛迦诺公约》（1925-10，保证西部边界）④德国加入国联任常任理事（1926-09）⑤《柏林条约》（1926-04，对苏中立互保）⑥《凯洛格—白里安公约》签署（1928-08）⑦杨格计划（1929-02，进一步削减赔偿）
- 关键时间线（16 节点）：1878 柏林生 / 1897 柏林大学 / 1901 莱比锡博士 / 1902 萨克森制造商协会 / 1903 结婚 / 1907 入国会 / 1917 民族自由党党魁 / 1918 创立 DVP / 1923-08 总理兼外长 / 1923-09 终结消极抵抗·Rentenmark / 1923-11 不信任案辞总理 / 1924 道威斯计划 / 1925 洛迦诺 / 1926 柏林条约·入国联·诺奖 / 1928 非战公约 / 1929 杨格计划·10-03 卒

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `peace/presentations/20th_century/Gustav_Stresemann/images/`；Makefile 设 `MAIN=Gustav_Stresemann_zh`
- 肖像：正文有 1925 洛迦诺德国代表团 autochrome、1929 海牙 autochrome（Stéphane Passet）、1929-09 与妻儿合影。优先 1929 海牙 autochrome 正装肖像；404 则装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 洛迦诺、柏林条约、非战公约 | 外交页 |
| 1 | foreign policy | 外交政策 | 外长 1923–1929 连任七届政府 | 外交页 |
| 2 | economic diplomacy | 经济外交 | 道威斯/杨格计划、对美经济纽带 | 计划页 |
| 3 | european integration | 欧洲一体化 | 1929 年公开赞许欧洲联合构想 | 晚年页 |
| 4 | parliamentary politics | 议会政治 | 国会 22 年、DVP 党魁 | 政党页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Karl Bücher | 师→生（博士导师） | 莱比锡经济学家，1901 啤酒业博士论文 |
| spouse | Käte Kleefeld | 无向 | 1903 结婚，两子 |
| parent-child | Wolfgang Stresemann | 无向 | 长子，后任柏林爱乐乐团经理 |
| parent-child | Hans-Joachim Stresemann | 无向 | 次子 |
| co-honored | Aristide Briand | 无向 | 1926 诺贝尔和平奖共同得主，洛迦诺公约 |
| colleague | Aristide Briand | 无向 | 洛迦诺谈判对手方兼密友 |
| colleague | Sir Austen Chamberlain | 无向 | 洛迦诺三方缔造者，英国外长 |
| colleague | Hjalmar Schacht | 无向 | 与 Ebert 共同促成其任帝国银行行长，实施道威斯计划 |
| colleague | Owen D. Young | 无向 | 道威斯计划共同作者 |
| colleague | Herbert Hoover | 无向 | 1921–1928 商务部长任内起保持密切关系 |

- 方向约定：advisor-student 有向（Bücher=advisor），其余无向（seed 幂等归一 from<to）
- 不入库：Ernst Bassermann（党界前辈，非导师）、Wilhelm Marx / Friedrich Ebert / Hermann Müller（僚属）、Friedrich Naumann（协会成员经历）、Mathilde（母未具名姓仅载名）以外的早年亲属

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：灰蓝的克制、钢丝上的沉着、和解的微光
- **配色**：主色青灰 `#37474F`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeLocarno` 洛迦诺 — 金 `#C9A227`
  - `badgeDawes` 道威斯计划 — 靛 `#4C5FD5`
  - `badgeRepublic` 魏玛 — 玫瑰 `#C4204F`
  - `badgeEconomy` 经济 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点 + 钢丝般的细横线，呼应"脆弱平衡"

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，14 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 脆弱平衡的维持者 / Gustav Stresemann 1878–1929 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 通胀终结 / 道威斯 / 洛迦诺 / 入国联 / 杨格计划
04  早年：柏林小酒馆之子 (1878–1907) — 啤酒商家庭、莱比锡博士、行业协会
05  战前的民族自由党人 (1907–1914) — Bassermann 门下、社会立法立场
06  战争与转变 (1914–1918) — 吞并主义、战败冲击、思想转变
07  创立 DVP 与魏玛的艰难接受 (1918–1923) — 君主主义者到理智共和派
08  总理百日 (1923) — 终结消极抵抗、Rentenmark、不信任案
09  洛迦诺：保证西境 (1925)（核心贡献页）— 与 Briand、Chamberlain 的谈判
10  1926 诺贝尔和平奖与入国联 — 与 Briand 共享；柏林条约
11  道威斯与杨格：经济外交双璧 (1924–1929) — Schacht、Young、美国资本环流
12  健康恶化与最后冲刺 (1928–1929) — 大联合政府、杨格计划通过数小时后辞世
13  遗产：Stresemann 晨礼服与脆弱平衡 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Stresemann 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 与 Briand 口径 | 1926 共享同一理由（their）；正文明载 "close personal friends"，可写"密友"；Chamberlain 是 1925 年同一公约获奖者，三方年份勿混 |
| 转变叙事 | 战时吞并主义与战后和解**必须两段都写**，勿美化或跳过；转变契机=战败与霍亨索伦王朝崩塌的身心崩溃 |
| Chamberlain 引语 | Stresemann 曾写 "Chamberlain had never been our friend..."——是 Stresemann 对其的负面评价原文，引用须标注出处语境（战后书信），勿当作会议记录 |
| 东方洛迦诺 | "There will be no Locarno of the east"（1925）有原文可引；同时他签署了对波兰/捷克斯洛伐克的仲裁协定，两面口径须并列 |
| 亚美尼亚史料 | 1916 君士坦丁堡之行得知亚美尼亚人遭遇、支持召大使 Metternich——只作 page.md 明载客观事实记录，一句带过，禁展开评价 |
| 纳粹语境 | 杨格计划不满助长极右、纳粹党崛起、Mainz 纪念碑 1935 被纳粹拆毁——客观记录，禁当代政治评价 |
| 死亡时间 | 1929-10-03，"hours after convincing the Reichstag to accept the Young Plan"——因果措辞照原文，勿写成过劳死 |
| 博士论文 | 1901 论柏林瓶装啤酒业（遭同僚嘲讽），导师 Karl Bücher——frontmatter 与正文一致，可写 |
| 时装彩蛋 | Stresemann 式晨礼服（short lounge-suit jacket + morning dress）以他命名——可做页脚彩蛋，勿写成他"发明"西装 |
| 引语白名单 | "remove the strangler from our throat"、"There will be no Locarno of the east"、Briand 沙发反应转述、Craig 史家评语、Fehrenbach 演说观感——仅 page.md 有英文原文者可引 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Locarno Treaties | 《洛迦诺公约》 | 1925-10 |
| Dawes Plan | 道威斯计划 | 1924 |
| Young Plan | 杨格计划 | 1929 |
| Rentenmark | 地租马克 | 1923 抗通胀新币 |
| Occupation of the Ruhr | 鲁尔占领 | 法比占领，消极抵抗终结 |
| German People's Party (DVP) | 德国人民党 | 1918 创立 |
| National Liberal Party | 民族自由党 | 帝国时期 |
| Vernunftrepublikaner | 理智共和派 | 心向君主、接受共和 |
| Erfüllungspolitiker | 履约政治家 | 保守派对他的讥称 |
| Treaty of Berlin (1926) | 《柏林条约》 | 对苏中立互保，重申拉巴洛 |
| League of Nations | 国际联盟 | 1926-09 常任理事 |
| Kellogg-Briand Pact | 《凯洛格—白里安公约》 | 1928-08 签署 |
| Reichsbank | 帝国银行 | Schacht 行长 |
| grand coalition | 大联合政府 | 1923 与 1928 两次 |
| Stresemann (style) | 施特雷泽曼式晨礼服 | 服装史彩蛋 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 觉醒 / 上扬 / 转折
- **匹配理由**: "觉醒"精准匹配其人生主轴——从战时吞并主义者被战败击醒、转变为法德和解的建筑师；上扬的段落呼应 1924–1926 连续胜利（道威斯→洛迦诺→入国联→诺奖），结尾的回落则预示 1929 年的猝然离世与大萧条的阴影。
- **本地路径**: `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 复制为 `presentations/20th_century/Gustav_Stresemann/Awaken.wav`
- **时长**: 128 秒 > 14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Gustav_Stresemann/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Gustav_Stresemann.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；每写一页就 make，看到溢出就修。**
