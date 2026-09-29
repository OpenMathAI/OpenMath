# OpenPeace 人物立传提示词（实例：Louis Renault (jurist)）

> **本文件是 OpenPeace 项目（诺贝尔和平奖得主立传）的人物立传提示词**，
> 以路易·勒诺（Louis Renault，法学家，1907 诺贝尔和平奖）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Louis Renault（1843–1918，法国法学家与教育家，1907 与 Ernesto Teodoro Moneta 共享诺贝尔和平奖）。
- **设计哲学**：法学家型得主立传以「学术—外交—仲裁」三条线索并进；和平奖是其国际法职业生涯的顶点，叙事重心放在海牙会议与仲裁实践。

---

## 二、背景信息 【人物专属】

- **目标人物**：Louis Renault（1843-05-21 Autun ~ 1918-02-08 Barbizon，享年 74 岁）
- **气质关键词**：**国际法教授、外交部的法律良知、海牙的设计师**
- **诺奖年份与官方获奖理由**：1907 年诺贝尔和平奖（与 Ernesto Teodoro Moneta 共享）
  > 中文获奖理由（照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > **「表彰他对海牙会议与日内瓦会议的进程和成果发挥了决定性影响」**
- **设计母题**：**天平与条约卷轴（scales & treaty scrolls）**——两次海牙会议与五大仲裁案的条文视觉，以「卷轴上的天平」贯穿
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Louis_Renault_jurist/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1843-05-21 生于 Autun（法国，七月王朝）~ 1918-02-08 逝于 Barbizon（法国，法兰西第三共和国），享年 74 岁
- 国籍：France
- 教育：frontmatter educated_at 作 University of Burgundy Europe（第戎大学系统）
- 任职履历（含年份）：
  - 1868–1873 第戎大学（University of Dijon）罗马法与商法教授
  - 1873 起直至去世：巴黎政治学院（Sciences Po）与巴黎大学法学院教授；1881 任国际法教授
  - 1890 任外交部法律顾问（jurisconsult，**为其专设的职位**），以国际法审查法国外交政策
- 国际会议：以该身份出席 numerous conferences，**尤以两次海牙会议（1899、1907）与 1908–09 伦敦海军会议著称**
- 仲裁名案（page.md 明载五件）：1905 日本屋税案（Japanese House Tax）、1909 卡萨布兰卡案（Casa Blanca）、1911 萨瓦卡尔案（Sarvarkar Case，常设仲裁法院）、1913 卡尔塔哥案（Carthage）、1913 马努巴案（Manouba）
- 著作：与挚友兼同事 **C. Lyon-Caen** 合著多部商法著作（两卷 compendium、八卷 treatise、再版多次的 manual）；1879 出版《Introduction to the Study of International Law》；1917 出版《First Violations of International Law by Germany》（论德国入侵比利时与卢森堡违反条约义务）
- 关键荣誉：1907 诺贝尔和平奖（与 Moneta 共享）；Leiden 大学荣誉博士；荣誉军团指挥官勋章（Commander of the Legion of Honour，frontmatter award_received 明载）
- 诺奖演讲：1908-05-18 *The Work at The Hague in 1899 and in 1907*
- 关键时间线（10–15 节点）：1843 生于欧坦 → 1868 任教第戎 → 1873 转巴黎（Sciences Po 与巴黎大学）→ 1879 《国际法研究导论》 → 1881 国际法教授 → 1890 外交部法律顾问（专设职位）→ 1899 第一次海牙会议 → 1905 日本屋税案仲裁 → 1907 第二次海牙会议+诺贝尔和平奖 → 1908-05-18 诺奖演讲 → 1908–09 伦敦海军会议 → 1909 卡萨布兰卡案 → 1911 萨瓦卡尔案 → 1913 卡尔塔哥案/马努巴案 → 1917 《德国对国际法的首次违反》 → 1918-02-08 卒于巴比松

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Louis_Renault_jurist/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 Makefile，设置 `MAIN=Louis_Renault_jurist_zh`、`VIDEO_NAME=Louis_Renault_jurist_zh`

### 第 3 步：收集图片 【人物专属】

- page.md infobox 有 1907 年肖像（`Renault in 1907`）；经 Commons Special:FilePath 取 500px，失败则装饰圆+天平纹章占位

### 第 4 步：事业领域梳理 + 入库（fields，与 yaml 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international law | 国际法 | 1881 巴黎大学国际法教授、外交部法律顾问，获奖核心 | 概览页 |
| 1 | international arbitration | 国际仲裁 | 五大名案（1905–1913） | 仲裁页 |
| 2 | diplomatic conferences | 外交会议 | 两次海牙会议、伦敦海军会议 | 海牙页 |
| 3 | commercial law | 商法 | 与 Lyon-Caen 合著系列 | 著作页 |
| 4 | roman law | 罗马法 | 第戎大学教席起点 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | C. Lyon-Caen | 无向 | 挚友兼同事，合著两卷 compendium、八卷 treatise 与多次再版商法 manual |
| co-honored | Ernesto Teodoro Moneta | 无向 | 1907 诺贝尔和平奖共同得主 |

- 本页 page.md 短篇（导语+两段正文），仅此两条明载关系（relations=2 为诚实值）
- ⚠️ 同名区分：本人与汽车工业家 Louis Renault（雷诺汽车创始人）**完全无关**，page.md 无任何关联表述，禁写「雷诺创始人」或其任何事迹；对手方 Moneta 命中本批 id=6955 既有记录（勿再建 stub）
- Lyon-Caen 名字按 page.md 载法（C. Lyon-Caen；通行为 Charles Lyon-Caen）stub 建档

### 第 5 步：配色方案（manifest 预分配，勿改）

- **主色**：`#2A4B7C`（普鲁士蓝——法度与外交的冷峻）
- **辅色**：诺奖香槟金 `C9A227`
- badgeA–D：badgeA 国际法（`#1F3A5F`）、badgeB 国际仲裁（`#1F6B4E`）、badgeC 外交会议（`#B08A2E`）、badgeD 商法与著述（`#8C3B2E`）

### 第 6 步：规划幻灯片序列（10–12 页，短篇页宜精不宜长）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 1907 诺贝尔和平奖 · 路易·勒诺 1843–1918 + 四色 badge + 右上肖像
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/教育/教席/外交部/荣誉/核心领域）
03  欧坦与第戎 (1843–1873) — 罗马法与商法讲席
04  巴黎双教席 (1873–1890) — Sciences Po 与巴黎大学、1881 国际法讲席
05  外交部法律顾问 (1890) — 为其专设的职位、以国际法审查外交政策
06  两次海牙会议 (1899/1907)（核心页）— 决定性影响
07  1907 诺贝尔和平奖 — 与 Moneta 共享、官方理由、1908 演讲
08  仲裁台上的五案 (1905–1913) — 日本屋税/卡萨布兰卡/萨瓦卡尔/卡尔塔哥/马努巴
09  商法合著与《国际法研究导论》 — Lyon-Caen 系列、1879/1917 两部专著
10  晚年与遗产 (1917–1918) — 战时著述、卒于巴比松
11  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 同名陷阱（最高优先） | 与雷诺汽车创始人 Louis Renault 同名：目录名/记录名均用消歧义 `Louis_Renault_jurist`，正文首次出现即注「法学家，非雷诺汽车创始人」 |
| 获奖理由 | 「对海牙会议与日内瓦会议的进程和成果发挥决定性影响」照抄名录；Moneta 的理由句（法意相互理解）**勿混入本篇** |
| 共享标注 | 1907 共享奖（Renault + Moneta）封面与诺奖页醒目标注；两人理由句不同 |
| 职位性质 | 1890 外交部法律顾问（jurisconsult）是「为他专设的职位」，勿写成常规编制 |
| Sarvarkar 案 | 1911 常设仲裁法院案例，客观列名即可，政治人物 Savarkar 背景不展开 |
| 1917 著作 | 《First Violations of International Law by Germany》主题为德国入侵比利时/卢森堡违反条约义务——一战语境只作书目事实记录 |
| 材料有限 | page.md 短篇：时间线/页数按上述规划，禁从外部记忆扩写（家庭、学位细节、海牙会议具体条款等均无载） |
| 无载禁写 | page.md 无载：婚姻、子女、生卒地以外的居住史、具体条约条款贡献——一律禁写 |
| 政治敏感红线 | 一战内容与萨瓦卡尔案只作 page.md 明载的客观事实记录，不加评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| jurisconsult | 法律顾问 | 外交部专设职位，1890 |
| Hague Conventions 1899/1907 | 海牙会议/公约（1899/1907） | 两次均出席 |
| London Naval Conference (1908–1909) | 伦敦海军会议 | 1908–09 |
| Japanese House Tax case | 日本屋税案 | 1905 |
| Casa Blanca Case | 卡萨布兰卡案 | 1909，勿与城市 Casablanca 拼写混（page.md 作 Casa Blanca） |
| Sarvarkar Case | 萨瓦卡尔案 | 1911，常设仲裁法院 |
| compendium / treatise / manual | 纲要 / 专著（八卷）/ 教科书 | 与 Lyon-Caen 合著三种 |
| Sciences Po | 巴黎政治学院 | 1873 起任教 |

---

## 四、背景音乐 ✅（manifest 预分配，勿改）

- **选定曲目**: **Savage** — Alex-Productions
- **匹配理由**: 冷峻的张力匹配外交谈判桌上的法理交锋——海牙与仲裁庭的暗流，恰如曲名的锋利质感
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐页数

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Louis_Renault_jurist/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Louis_Renault_jurist.yaml` | fields + relations 入库母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：同名区分与短篇页禁扩写。**
