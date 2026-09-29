# 政治家立传提示词（OpenPeace 批次 6 实例：Aristide Briand）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Aristide Briand（1926 诺贝尔和平奖，《洛迦诺公约》与《非战公约》缔造者、11 任法国总理）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Aristide Pierre Henri Briand（阿里斯蒂德·皮埃尔·亨利·白里安）。
- **设计哲学**：和平奖得主（国务家/外交家类）立传保留「身份信息页 + 事业领域结构化」骨架；本例的叙事主轴是**战间期法德和解与欧洲联邦构想**——从社会主义记者到 11 任总理的漫长弧线，重心放在 1925–1932 年的外交遗产。

---

## 二、背景信息 【人物专属】

- **目标人物**：Aristide Pierre Henri Briand（1862-03-28 生于南特 ~ 1932-03-07 卒于巴黎，享年 69 岁）
- **气质关键词**：**和解的政治家、欧洲联邦的先知、十一任总理**
- **诺奖**：1926 诺贝尔和平奖（与德国外长 Stresemann 共享），获奖理由（Nobel 官方英文原文照抄，their 为共享口径）：
  > "for their crucial role in bringing about the Locarno Treaty"（表彰他们在促成《洛迦诺公约》中的关键作用）
- **设计母题**：**和解与欧洲联邦（reconciliation & European federation）**。洛迦诺之手、非战公约的一纸誓言、1929 年国联讲台上的欧洲合众国构想——视觉语言采用握手、相框式边界与星环意象（欧洲一体化的先声）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Aristide_Briand/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）；`peace/presentations/cover/`（项目首页）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1862-03-28 生于南特（Loire-Atlantique）~ 1932-03-07 卒于巴黎（69 岁）
- 国籍：法国；党派轨迹：法国社会党 1902–1904 → 独立社会党人 1904–1911 → 共和社会党 1911–1932；本人公开的无神论者
- 教育：南特中学（1877 与 Jules Verne 结成忘年交）；巴黎大学法学院
- 新闻业：为工团主义刊物 *Le Peuple* 撰稿、主持 *Lanterne*、办 *Petite République*，后与 Jean Jaurès 合作创办 *L'Humanité*（1904）
- 任职（含年份）：众议员 1902–1932（Loire 1902–09、Loire-Inférieure 1909–32）；司法部长三任（1908、1912–13、1914–15）；公共教育与文化部长 1906（Sarrien 内阁，执行政教分离法，因此 1906-03 被统一社会党开除）；总理 11 任（1909–11、1913、1915–17、1921–22、1925–26、1929 等六个时段）；外交部长 1926–1932 连任至死（1925 年重返外交部，一生入阁 14 届、4 届亲自组阁）
- 关键荣誉：1926 诺贝尔和平奖；Cross of Liberty 3 师 1 等；三星勋章（Order of the Three Stars）
- 核心事业清单：①1905 政教分离法主笔与报告人②1910 工人与农民养老金法案、疾病与养老强制保险③一战战时总理（萨洛尼卡远征推手、1916 重组政府）④洛迦诺公约（1925，与 Stresemann、Chamberlain）⑤《凯洛格—白里安公约》（1927 提议 → 1928 巴黎非战公约）⑥白里安欧洲联邦计划（1929-09-05 国联演讲、1930 备忘录）
- 关键时间线（15 节点）：1862 南特生 / 1877 南特中学识 Verne / 1894 南特工人大会确立工会思想 / 1902 当选众议员 / 1904 与 Jaurès 创办 L'Humanité / 1905 政教分离法 / 1906 入阁被社会党开除 / 1909 首任总理 / 1910 养老金立法 / 1915–17 战时总理 / 1921–22 华盛顿海军会议·戛纳会议 / 1925 重返外交部·洛迦诺 / 1926 诺奖 / 1928 非战公约 / 1929 欧洲联邦演讲 / 1930 备忘录 / 1932 卒于巴黎任上

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `peace/presentations/20th_century/Aristide_Briand/images/`；Makefile 设 `MAIN=Aristide_Briand_zh`
- 肖像：正文有 Marcel Baschet 油画肖像（330px）与洛迦诺法国代表团合影（1925 autochrome）、Briand–Stresemann 合影。优先 Baschet 油画；404 则装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 洛迦诺、非战公约、欧洲联邦计划 | 外交页 |
| 1 | foreign policy | 外交政策 | 1926–1932 连任外交部长 | 外交页 |
| 2 | european integration | 欧洲一体化 | 白里安计划，战后 EU 思想先声 | 联邦页 |
| 3 | international law | 国际法 | 非战公约废除战争、政教分离法 | 公约页 |
| 4 | parliamentary politics | 议会政治 | 众议员 30 年、11 任总理 | 生平页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Gustav Stresemann | 无向 | 1926 诺贝尔和平奖共同得主，洛迦诺公约 |
| colleague | Gustav Stresemann | 无向 | 法德和解的主要对手方与支持者，其 1929 去世致白里安计划夭折 |
| colleague | Sir Austen Chamberlain | 无向 | 洛迦诺三方缔造者，Chamberlain 1925 获和平奖 |
| colleague | Frank Billings Kellogg | 无向 | 1927 共同提议、1928 缔结非战公约 |
| colleague | Jean Jaurès | 无向 | 合作创办 L'Humanité，后社会主义路线分歧 |
| colleague | David Lloyd George | 无向 | 一战盟国协作与 1922 戛纳会议的英国对手方 |

- 方向约定：全部无向（seed 幂等归一 from<to）
- 不入库（无稳定类型或无载）：Jules Verne（少年挚友，非同事非导师）、Jules Guesde（1894 大会思想对手，争议强度不足）、Maurice Sarrail / Joffre / Poincaré（僚属与政敌，仅叙述）、希腊王妃 George 亲王妃（1916 "widely suspected" 绯闻，禁写成确证关系）、配偶 page.md 无载禁写

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：第三共和国的庄重、和解的暖意、乌托邦的蓝
- **配色**：主色深绿 `#1B4D3E`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeLocarno` 洛迦诺 — 金 `#C9A227`
  - `badgePact` 非战公约 — 靛 `#4C5FD5`
  - `badgeUnion` 欧洲联邦 — 群青 `#3B6FB6`
  - `badgeRep` 共和国 — 玫瑰 `#C4204F`
- **背景母题**：柔和圆点 + 细网格线，呼应欧洲地图与国联讲台

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，14 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 和解的政治家 / Aristide Briand 1862–1932 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 社会立法 / 战时总理 / 洛迦诺 / 非战公约 / 欧洲联邦
04  早年：南特与巴黎 (1862–1902) — Verne 忘年交、法学、工团主义新闻业
05  政教分离法与社会立法 (1905–1910) — 主笔 1905 法、养老金与保险、被社会党开除
06  战时总理 (1915–1917) — 萨洛尼卡、凡尔登危机、政府重组
07  华盛顿与戛纳 (1921–1922) — 海军会议、高尔夫风波
08  洛迦诺：法德和解的诞生 (1925)（核心贡献页）— Chamberlain、Stresemann 三方
09  1926 诺贝尔和平奖 — 与 Stresemann 共享（Chamberlain 前一年同一公约获奖）
10  非战公约 (1927–1928) — 与 Kellogg 的巴黎公约
11  白里安计划：欧洲联邦的先声 (1929–1930) — 国联演讲、备忘录、夭折与遗产
12  十一任总理的纪录 — 六时段年表一览
13  遗产：从洛迦诺到欧盟 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Briand 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 1926 与 Stresemann **共享同一理由**（their）；Chamberlain 是**前一年（1925）**因同一公约获奖——三人口径勿混写同年共享 |
| 总理任数 | 正文口径 **11 任**（six 个时段），infobox 列 6 段任职勿写"6 任" |
| 外交部长任期 | 1925 年回外交部 → 1926-07-23 起连续任至 1932-03-12 卒，正文口径 "remain foreign minister until his death"；勿写 1932 年离任 |
| 政教分离法 | 1905 法的报告人与主要作者；清点教会财产条款引发的骚乱非其负责——因果勿张冠李戴 |
| L'Humanité | 与 Jaurès 合作创办（1904）；后与 Jaurès 路线分歧（主张与激进党合作）——既合作又分歧，双向表述 |
| 共济会 | 1887 Le Trait d'Union 仪式缺席未被登记、1889 被宣布 "unworthy"、1895 加入 Les Chevaliers du Travail——三段细节勿简化成"共济会员"一句 |
| 欧洲联邦 | 1929-09-05 国联演讲 + 1930 备忘录两步；计划因 Stresemann 死亡与大萧条夭折，但 "suggested an economic framework for developments after World War II"——是"先声/启发"而非"直接缔造 EU"，措辞降级 |
| 绯闻 | 1916 与希腊王妃 "widely suspected"——写"受到广泛怀疑"即可，禁写成确证情史 |
| 无配偶 | page.md 无妻子记载，禁编 |
| 引语 | page.md 无 Briand 本人英文原话，全篇禁直接引语（"unité de front" 是政策口号转述） |
| 政治红线 | 战时决策、法西斯/纳粹兴起背景只作 page.md 明载客观事实记录，禁当代政治评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Locarno Treaties | 《洛迦诺公约》 | 1925，法德和解 |
| Kellogg-Briand Pact | 《凯洛格—白里安公约》 | 又称《非战公约》/ Pact of Paris，1928 |
| Briand plan | 白里安计划 | 1929–1930 欧洲联邦构想 |
| League of Nations | 国际联盟 | 1929 演讲舞台 |
| separation of church and state | 政教分离 | 1905 法国法律 |
| President of the Council | 部长会议主席 | 第三共和国总理称谓 |
| Chamber of Deputies | 众议院 | 1902–1932 |
| L'Humanité | 《人道报》 | 1904 与 Jaurès 创办 |
| Washington Naval Conference | 华盛顿海军会议 | 1921–22，5:5:3:1.7:1.7 |
| Cannes Conference | 戛纳会议 | 1922，高尔夫风波 |
| Quai d'Orsay | 法国外交部 | 1925–1932 |
| Briand-Ceretti Agreement | 白里安—切雷蒂协定 | 与梵蒂冈，主教任命 |
| Salonika front | 萨洛尼卡战线 | 1915 远东推手 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Nostalgia** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 怀旧 / 抒情 / 回望
- **匹配理由**: "怀旧/回望"匹配白里安的双重身份——既是旧世纪社会主义记者，又是两次大战间和解外交的化身；他的欧洲联邦计划在当时夭折、战后才开花，正是"为未来写下的怀旧曲"。
- **本地路径**: `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → 复制为 `presentations/20th_century/Aristide_Briand/Nostalgia.wav`
- **时长**: 128 秒 > 14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Aristide_Briand/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Aristide_Briand.yaml` | 入库 yaml（第 4 / 4.5 步落地，库内 id=5602 沿用） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；每写一页就 make，看到溢出就修。**
