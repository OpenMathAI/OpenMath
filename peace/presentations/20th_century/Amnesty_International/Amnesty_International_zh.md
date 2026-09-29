# 和平奖得主立传提示词（OpenPeace：Amnesty International，组织机构篇）

> **本文件是 OpenPeace 的「诺贝尔和平奖得主立传提示词」组织机构版**，以 Amnesty International（1977 诺贝尔和平奖）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），按 OpenPeace 立传执行；组织机构特别规则见工作流第 2 节。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + tex 结构）与和平奖侧批次经验。
- **本实例**：Amnesty International（国际特赦组织，简称 Amnesty 或 AI）——本篇为**组织机构立传**。
- **设计哲学**：组织机构立传以「机构概览页」（Organization Overview）替代人物「身份信息页」，强调使命领域与运作结构的结构化表达。

---

## 二、背景信息 【机构专属】

- **目标机构**：Amnesty International（1961 年 7 月成立于英国伦敦，总部伦敦，全球性国际非政府组织）
- **官方获奖理由（1977）**：
  > "for worldwide respect for human rights."
  > （中译照抄名录：表彰其为在全世界尊重人权所做的贡献）
- **气质关键词**：**良心犯的代笔人、烛光与铁丝网的符号、十百万会员的全球良知网络**
- **设计母题**：**被铁丝网环绕的烛光（the candle behind barbed wire）**。组织以蜡烛与铁丝网为标志意象——烛光对应「一人一信」的写信运动，铁丝网对应良心犯的处境。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Amnesty_International/page.md`
- **参考模板**：
  - 立传成品参照：OpenMathAI 各侧 15–16 页 Beamer（封面 `\input` 项目首页）
  - 项目封面模板：OpenPeace 侧共享 `cover/` 目录

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已按 page.md 核对）【机构专属】

- 成立：1961 年 7 月，英国伦敦；1962-09-30 正式定名 Amnesty International（此前称 Amnesty）
- 创始：律师 Peter Benenson 发起；infobox 载创始人 Peter Benenson、Eric Baker、Seán MacBride 三人
- 起点事件：1960-11-19 Benenson 在伦敦地铁读到两名葡萄牙学生因「为自由干杯」被判 7 年监禁的报道；1961-05-28《观察家报》头版刊出 "The Forgotten Prisoners"（"An Appeal for Amnesty, 1961"），提出「Prisoners of Conscience（良心犯）」概念
- 性质：国际非政府组织（INGO），非营利；自称逾千万会员与支持者；2019 年有 63 个国家分会（sections）
- 结构：Global Assembly（最高决策）→ International Board（8 人）→ International Secretariat（秘书长主持日常）
- 历任首脑：主席 Peter Benenson（1961–1966）；秘书长 Eric Baker（1966–1968）、Martin Ennals（1968–1980）、Thomas Hammarberg（1980–1986）、Ian Martin（1986–1992）、Pierre Sané（1992–2001）、Irene Khan（2001–2010）、Salil Shetty（2010–2018）、Kumi Naidoo（2018–2020）、Agnès Callamard（2021– ）；国际理事会主席 Seán MacBride（1965–1974，首任）
- 经费：主要来自会员费与捐款，自称不接受政府或政府组织捐款
- 核心使命清单（六大领域）：妇女/儿童/少数群体/原住民权利、终结酷刑、废除死刑、难民权利、良心犯权利、人性尊严保护
- 关键荣誉：诺贝尔和平奖（1977，表彰其「对人性的捍卫、对抗酷刑」之功——Wikipedia 行文口径）；联合国人权奖（1978）；Erasmus Prize、Olof Palme Prize 等多项（frontmatter award_received 13 项）
- 关键时间线（16 节点）：1960-11-19 地铁读到报道 → 1961-05-28《观察家报》刊文发起「为特赦请命」 → 1961-07 伦敦第一次会议决定成立永久组织 → 1962-09-30 定名 Amnesty International → 1960 年代获联合国/欧洲委员会/UNESCO 咨询地位 → 1965 MacBride 任国际理事会首任主席 → 1966 Benenson 因 Aden 报告风波辞主席职 → 1968 Ennals 任秘书长 → 1970 年代议程扩展至司法不公与酷刑 → 1972 获美洲人权委员会咨询地位 → 1976 推动两项联合国人权公约获批准 → 1977 诺贝尔和平奖 → 1978 联合国人权奖 → 1979 会员从 1969 年 15,000 增至 200,000 → 1986/1988 两轮大型人权巡演（Conspiracy of Hope / Human Rights Now!） → 1990 年代推动设立联合国人权专员（1993）与国际刑事法院（2002） → 2021 Callamard 任秘书长至今

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Amnesty_International/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目近邻成品 Makefile，设 `MAIN=Amnesty_International_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【机构专属】

- page.md 载多幅实景图（分会活动、WorldPride、Rouen 标牌等）；按 images.txt 下载组织标志或活动照，404 则用装饰圆占位

### 第 4 步：使命领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | human rights | 人权 | 组织总使命 | 核心页 |
| 1 | prisoners of conscience | 良心犯 | 组织核心原则与起点议题 | 起源页 |
| 2 | torture prevention | 终结酷刑 | 1970 年代起的核心议程 | 议程页 |
| 3 | abolition of death penalty | 废除死刑 | 视死刑为对人权的最终否定 | 议程页 |
| 4 | refugee rights | 难民权利 | 六大领域之一 | 议程页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致；组织机构按工作流第 2 节）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Peter Benenson | 本人→组织（创始人） | 1961 发起人、首任主席（1961–1966） |
| founder | Eric Baker | 本人→组织（创始人） | infobox 载共同创始人，第二任秘书长 |
| founder | Seán MacBride | 本人→组织（创始人） | infobox 载创始人、首任国际理事会主席（1965–1974） |
| colleague | Martin Ennals | 无向 | 1968–1980 任秘书长，1970 年代与 MacBride 一道推动议程扩展 |

### 第 5 步：设计配色方案 【机构专属，勿改主色】

- **主色**：`#16324F`（深藏青——国际组织的庄重与法治感）
- **辅色**：诺奖香槟金 `C9A227` + 四分类色：badgeA 良心犯 `#2E5F7A`；badgeB 反酷刑 `#7A3E48`；badgeC 废死刑 `#8C6A2F`；badgeD 难民与少数群体 `#2E7D6B`
- **背景母题**：烛光与铁丝网

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有组织标志（或装饰圆占位）+ 机构名小字注；顶部/底部明示总部（United Kingdom）。
2. 必须有**机构概览页**（替代身份信息页）：左标志 + 右信息网格（成立时间、创始人、总部、性质、规模、历任首脑、使命领域）。
3. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【机构专属，10–16 页】

```
00 OpenPeace 项目首页（\input cover 共享页）
01 封面 — 1977 诺贝尔和平奖 / Amnesty International 1961– + badge + 总部行
02 机构概览页（★ 必做，替代身份信息页）
03 核心使命概览 — 良心犯 / 反酷刑 / 废死刑 / 难民 / 人性尊严
04 起源：一杯为自由干杯的酒 (1960–1961) — Benenson、《观察家报》社论、良心犯概念
05 从 Appeal 到正式组织 (1961–1962) — 定名、三大政党议员入会、Sections 制
06 原则与结构 — 不介入政治问题、不评判暴力是否正当、Global Assembly/Board/Secretariat
07 议程扩展与咨询地位 (1960s–1970s) — UN/Europe/UNESCO 咨询地位、司法不公与酷刑
08 诺贝尔和平奖 (1977) — 理由句、1978 联合国人权奖、会员 15,000→200,000
09 写信运动与音乐 — The Secret Policeman's Balls、Conspiracy of Hope、Human Rights Now!
10 1990 年代：走向全球机制 — 联合国人权专员（1993）、国际刑事法院（2002）
11 2000 年代以来 — 全球化与经济文化权利、反恐年代的人权坚守、Amnesty Academy
12 创始人与首脑传承 — Benenson/Baker/MacBride、历任秘书长谱系
13 荣誉与认可 — Nobel 1977、UN Human Rights Prize 1978、Erasmus 等
14 争议与批评（客观记录） — 各方批评按 page.md 双方并列、不加评价
15 遗产：千万会员的良知网络
16 结尾
```

### 第 7–8 步：Beamer 编写 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；写完即 make，`pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【机构专属】

**Amnesty International 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 创始人口径 | 正文叙述为 Benenson 创立，infobox 列 Benenson/Baker/MacBride 三人为 Founders；勿把首任理事会主席 MacBride 或秘书长 Ennals 误写成"创始人"；Baker 是 infobox 明载的共同创始人 |
| 获奖理由口径 | 官方 citation 为 "for worldwide respect for human rights."；Wikipedia 正文另有 "defence of human dignity against torture" 行文——引文框用官方句，正文转述可写后者，勿混标 |
| 组织性质 | 是独立 INGO，**不是**联合国机构；与 UN 的关系仅为咨询地位（consultative status），勿写成"联合国下属机构" |
| 定名时间 | 1961-07 成立时称 Amnesty，1962-09-30 才定名 Amnesty International——勿把定名日当成立日 |
| 良心犯定义 | 仅指因意见/宗教被囚者；主张或默许暴力的囚犯（如 Mandela 一案）不适用此名——委员会一致裁定，按 page.md 记录 |
| 政治红线 | 各国政府与媒体的批评、内部争议（2019 职场报告等）只按 page.md 客观并列记录，禁任何评价性语句；争议内容不进入引文框 |
| 引文框白名单 | Benenson "The Forgotten Prisoners" 段落原文（page.md 明载）与 2005 章程愿景句——其余禁入 |
| 秘书长谱系 | Benenson 的职务是主席（1961–1966）；首任秘书长一般从 Baker（1966）计——两列勿混；1986–1992 任者是 Ian Martin（表格内 Avery Brundage 为页面噪声，弃） |
| 数字口径 | 会员 15,000（1969）→ 200,000（1979）→ 1990 年代逾 700 万 → 现自称逾千万——各年代数字勿互换 |
| 与 Seán MacBride | MacBride 亦是 1974 诺贝尔和平奖得主（另一条目），本篇只写其在 AI 的角色，勿展开其个人生平 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| prisoner of conscience | 良心犯 | 组织核心概念，非普通"政治犯" |
| Appeal for Amnesty | 为特赦请命 | 1961 年发起文告 |
| The Forgotten Prisoners | 《被遗忘的囚犯》 | 社论标题 |
| section | 分会（Sections） | 国家级会员组织，勿译"部门" |
| consultative status | 咨询地位 | UN/Europe/UNESCO 授予 |
| urgent action | 紧急行动 | 国际秘书处快速反应机制 |
| INGO | 国际非政府组织 | 区别于政府间组织 |
| miscarriage of justice | 司法不公 | 1970 年代新增议程 |
| Universal Declaration of Human Rights | 《世界人权宣言》（UDHR） | 使命参照系 |
| International Secretariat | 国际秘书处 | 日常执行机构 |

---

## 四、背景音乐 ✅ 【机构专属，manifest 预分配，勿改】

- **选定曲目**: **New Lands** — Alex-Productions
- **匹配理由**: 「新大陆」对应 1961 年从一版社论起步、把「良心犯」概念带入世界每一个角落的开疆叙事——半个多世纪从伦敦一小群人成长为逾千万会员的全球网络。
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → 复制为 `presentations/20th_century/Amnesty_International/New_Lands.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Amnesty_International/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译（照抄，禁改写） |
| `MySQL/data/Amnesty_International.yaml` | 入库 yaml（第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
