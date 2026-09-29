# 和平奖得主立传提示词（OpenPeace 实例：United Nations Peace-Keeping Forces）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」的批次实例**，
> 以 United Nations Peace-Keeping Forces（联合国维持和平部队，1988 诺贝尔和平奖）为对象。
> **本对象为组织机构（is_org=true）**：第 6 步用「机构概览页」替代身份信息页；yaml 省略 gender/nationalities。
> 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：United Nations Peace-Keeping Forces（联合国维持和平部队）——1988 年诺贝尔和平奖集体得主，"蓝盔"即联合国维和的代名词；机构史立传（传统维和 → 多维维和 → 强力维和三个世代）。
- **设计哲学**：机构立传以**「组织史世代演化」为主线**——版面用蓝盔/蓝贝雷帽与 UN 蓝色为主视觉，时间线按「世代」分层而非个人生平，人物（秘书长、 force commander）作为机制演化的推手出现。

---

## 二、背景信息 【人物专属】

- **机构名称**：United Nations Peace-Keeping Forces（联合国维持和平部队；条目主题为 United Nations peacekeeping 维持和平行动）
- **成立**：1948 年（首个维和特派团 UNTSO 联合国停战监督组织）
- **性质**：联合国安理会授权、和平行动部（Department of Peace Operations, DPO）管理的国际军事/警察/文职人员部署机制（联合国宪章未载明，"第六章半"）
- **诺奖年份与官方获奖理由**：1988 年诺贝尔和平奖（集体授予）：
  > "for preventing armed clashes and creating conditions for negotiations"
  > （表彰其防止武装冲突并为谈判创造条件）
  > ※ 中译以名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` 为准，禁止改写。
  > ※ 挪威诺奖委员会另称维和部队 "represent the manifest will of the community of nations" 并 "made a decisive contribution"——两句均为 page.md 实载，可引用。
- **气质关键词**：**蓝盔的中立守望者、第六章半的 improvisation、集体安全的手术刀**
- **设计母题**：**蓝盔与停火线（blue helmet & ceasefire line）**——UN 蓝（#5B92E5）+ 蓝盔剪影 + 停火线/缓冲区地图意象；"自 1948 年以来 125 国逾 200 万人次、72 项行动"的集体性是版面的叙事底色。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/United_Nations_peacekeeping/page.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地页面与事实基准 【人物专属】

- 事实基准（以本地 page.md 为准）：
  - 机制定位（安理会授权、DPO 管理；与 peacemaking / peace enforcement / peacebuilding 三概念区分；宪章无维和条款，冷战催生的"临时制度发明"）
  - 三原则（当事方同意 / 公正 impartiality / 除自卫与卫护授权外不使用武力——Hammarskjöld 1958 提出，2008 Capstone Doctrine 成典）
  - 组织数据（1948 年以来 125 国逾 200 万人次、72 项行动；2026 年 11 项行动在役、预算 56.6 亿美元、约 5.3 万人、117 国出兵，前五出兵国尼泊尔/卢旺达/孟加拉/印度/巴基斯坦；DPO 现任主管 Jean-Pierre Lacroix，2017-04-01 就任；SG António Guterres）
  - 三代演化（详见关键时间线）
  - 关键时间线（15–20 节点：1948 UNTSO（监督 1948 阿以战争停火，至今仍在）→ 1951 UNMOGIP（印巴军事观察组）→ 1956 苏伊士危机、Pearson 建议 + Hammarskjöld 方案、首支武装隔离部队 UNEF → 1960–64 ONUC 刚果 → 1964 至今 UNFICYP 塞浦路斯 → 1974 至今 UNDOF 戈兰 → 1958 Hammarskjöld 三原则 → 1988 诺贝尔和平奖（此前共 13 项行动获授权）→ 1988–89 一年再批 5 项 → 1989–90 UNTAG 纳米比亚独立 → 1991 ONUSAL 萨尔瓦多 → 1992《和平纲领》An Agenda for Peace、DPKO 成立 → 1992–93 UNTAC 柬埔寨 → 1992–94 ONUMOZ 莫桑比克 → 1993–95 UNOSOM II 索马里受挫 → 1994 UNAMIR 卢旺达大屠杀 80 万+ → 1995 斯雷布雷尼察（UNPROFOR"安全区"内）→ 1996 UNTAES 东斯拉沃尼亚"十年最成功"→ 1999 安南双报告 → 1999 Res 1265/1270 首次明确保护平民授权（UNAMSIL）→ 2000 布拉希米报告 → 2013 Res 2098 MONUSCO 进攻性授权 → 2019 Guterres 改组 DPO → 2023 MINUSMA 应东道国要求关闭 → 2017 年后无新授权（2026 视角，1980 年代以来最长空窗））
- 司法与争议类内容（索马里/卢旺达/斯雷布雷尼察失败、POC 执行不力 2014 OIOS 报告、维和人员性剥削指控若正文实载）**一律只作客观事实记录，禁加评价**

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `United_Nations_peacekeeping/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=UN_peacekeeping_zh`（长名可用缩写 MAIN，Makefile 注明映射）、`VIDEO_NAME=UN_peacekeeping_zh`

### 第 3 步：收集图片 【人物专属】

- 机构无人物肖像：用 UN 蓝盔照片（page.md 配图：孟加拉部队 MINUSMA、挪威维和士兵萨拉热窝 1992-93、印度军医刚果、意大利 UNIFIL 巡逻、Bastille Day 多国营）
- 下载失败则用装饰圆占位

### 第 4 步：使命领域梳理 + 入库 【模板通用，组织机构内容】

**UN 维和部队的使命领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peacekeeping | 维和行动 | 隔离、缓冲、停火监督的集体安全机制，1988 诺奖核心 | 封面、概览页 |
| 1 | ceasefire monitoring | 停火监督 | UNTSO/UNMOGIP 起家的观察员传统 | 传统页 |
| 2 | civilian protection | 保护平民 | 1999 起的核心任务，95% 现役兵力在 POC 授权下 | 强力页 |
| 3 | peacebuilding | 建设和平 | DDR、选举援助、安全部门改革、过渡行政 | 多维页 |
| 4 | humanitarian aid | 人道主义援助 | 任务组合中的民生与医疗支持 | 任务页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en='United Nations Peace-Keeping Forces'`），`primary_occupation='un agency'`、`has_social_data=1`、`has_biography=0`
- **组织机构省略 gender 与 nationalities**；`birth_date` 用 `1948`
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先建字典项

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，组织机构内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| other | United Nations | 无向 | 联合国体系内的维和机制，安理会授权、和平行动部管理 |
| colleague | Dag Hammarskjöld | 无向 | 秘书长，"第六章半"定名、1958 三原则、1956 UNEF 方案 |
| colleague | Lester Bowles Pearson | 无向 | 加拿大外长，1956 首支维和部队 UNEF 建议人 |
| colleague | Boutros Boutros-Ghali | 无向 | 秘书长，1992《和平纲领》与 DPKO 设立推手 |
| colleague | Kofi Annan | 无向 | 秘书长，1999 卢旺达与斯雷布雷尼察两份自我批评报告 |
| colleague | Roméo Dallaire | 无向 | UNAMIR 部队指挥官（卢旺达），"pull 逻辑"描述维和机制 |

#### 4.5.1 入库操作

- 以机构记录为中心写入 `person_relation`；对手方沿用库内形式（`Dag Hammarskjöld` id=6782、`Lester Bowles Pearson` id=7028 勿新建）
- 缺失人物先建占位（`has_biography=0`）
- 无载禁写：Jean-Pierre Lacroix / Guterres 仅现任职务（任职列表性事实，与机构非"紧密关系"）、UNTAG/UNTAC 等特派团名不入对手方、Annan/Dallaire 若后续批次有独立主张以彼方为准

### 第 5 步：设计配色方案 【模板通用，组织机构色彩】

- **配色**：manifest 预分配主色 **深棕 `#5C3A1E`** + 诺奖香槟金 `C9A227` + 四分类色（UN 蓝作辅助点缀 `#5B92E5`）：
  - `badgeTrad` 传统维和 — 深红 `#A63A2B`
  - `badgeMulti` 多维维和 — 青绿 `#0E7C7B`
  - `badgeRobust` 强力维和 — 琥珀 `#E07B30`
  - `badgeNow` 当代收缩 — 紫 `#52307C`
- **背景母题**：蓝盔剪影 + 世界地图停火线标记 + 柔和气泡

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页，机构概览页★】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 蓝盔：第六章半 / UN Peace-Keeping Forces 1948– + 四色 badge + 蓝盔图 + 「国际组织」行
02  机构概览页（★ 必做）— 左蓝盔照 + 右信息网格（成立、机制定位、三原则、规模数据、获奖）
03  机制概览 — 维和 vs. 建和/强制和平/缔造和平 + 三原则
04  起源：无宪章依据的发明 — 冷战瘫痪集体安全、"第六章半"（Hammarskjöld）
05  世代一：传统维和 (1948–1988) — UNTSO、UNMOGIP、1956 苏伊士与 UNEF、Pearson 建议
06  第一代模板 — 轻武装观察与隔离、不结盟国家出兵、ONUC/UNFICYP/UNDOF
07  1988 诺贝尔和平奖 — 获奖理由原句 + 委员会评语 + 13 项行动的集体履历
08  世代二：多维维和 (1988–1999) — 冷战结束、《和平纲领》、DPKO 成立
09  多维时代的成功 — UNTAG 纳米比亚、ONUSAL、ONUMOZ、UNTAC 柬埔寨
10  多维时代的失败 — 索马里 UNOSOM II、卢旺达 UNAMIR、斯雷布雷尼察（仅客观事实）
11  反思与改革 — 1999 安南双报告、2000 布拉希米报告、UNTAES 的"试验场"
12  世代三：强力维和 (1999–) — POC 授权（Res 1265/1270）、MONUSCO 2013 进攻性授权
13  当代收缩 (2019–2026) — DPO 改组、MINUSMA 关闭、2017 后无新授权
14  遗产：200 万人次的蓝线 — 数据总览 + scholars 研究结论（客观转述）
15  结尾 — OpenMathAI 品牌口径
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 机构概览页参照 `\profileslide`（左图右网格）；其余同个人立传骨架

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠

### 第 9 步：史实审查 + 术语审查 【人物专属】

**UN 维和部队特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | 1988 年**集体授予**维和部队（the forces were collectively awarded）——封面写"集体得主"，勿写成"个人得主"或"授予联合国" |
| 获奖理由 | 官方措辞 "for preventing armed clashes and creating conditions for negotiations"，两句委员会评语可引但勿拼成一句 |
| 成立年份 | 1948（UNTSO 首个行动）；不是 1945（联合国成立年）也不是 1956（UNEF） |
| 名称口径 | 条目主题为 United Nations peacekeeping（维持和平行动机制）；manifest/DATA 规范名 United Nations Peace-Keeping Forces；正文首现两者并注 |
| 三原则归属 | Hammarskjöld 1958 提出、2008 Capstone Doctrine 成典——两个年份勿混 |
| UNEF 归属 | 方案是 Hammarskjöld 提出，主意源自加拿大外长 Pearson（"Uniting for Peace"决议语境）——双人并列勿独占 |
| 失败叙事 | 索马里/卢旺达/斯雷布雷尼察只按 page.md 客观转述（80 万+ 死亡、Dutch UNPROFOR 营在场、'no peace to keep'）；禁渲染、禁归责个人 |
| POC 数据 | 16 项行动曾获 POC 授权、2026 年 5 项在役（MINUSCA/MONUSCO/UNMISS/UNIFIL/UNISFA）、95% 现役军警在 POC 下——数字勿错 |
| 2026 空窗 | 2017 年 MINUJUSTH（海地）后无新授权，为 1980 年代以来最长空窗——"2026 视角"表述 |
| 出兵国 | 前五：尼泊尔/卢旺达/孟加拉/印度/巴基斯坦（2026 数据）；勿写发达国家为主力 |
| 政治敏感红线 | 涉及具体国家与冲突方的表述一律按 page.md 原文客观转述；1948 阿以战争、印巴分治、两岸等语境禁加任何评价 |
| Dallaire 引语 | "pull 逻辑"引语为 page.md 实载原文可整段引用；其余引语须核对原文 |
| 机制 vs. 机构 | 维和不是 UN 的"一个部门"——由 DPO（部）管理、特派团逐项授权；勿写"UN 维和部 1948 年成立"（DPKO 1992 年才设立，2019 年改名 DPO） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| peacekeeping | 维持和平 | 与 peacemaking（缔造和平）区分 |
| blue helmet / blue beret | 蓝盔/蓝贝雷帽 | 维和代名词 |
| Chapter Six and a Half | 第六章半 | Hammarskjöld 语 |
| consent of the parties | 当事方同意 | 三原则之一 |
| impartiality | 公正 | 不等于中立 neutrality |
| Capstone Doctrine | 《纲领文件》 | 2008 维和原则成典 |
| UNTSO | 联合国停战监督组织 | 1948 首个特派团 |
| UNEF | 联合国紧急部队 | 1956 首支武装维和部队 |
| DPO / DPKO | 和平行动部/维和行动部 | 1992 设 DPKO，2019 改名 DPO |
| An Agenda for Peace | 《和平纲领》 | 1992 Boutros-Ghali 报告 |
| Brahimi Report | 布拉希米报告 | 2000 改革报告 |
| POC (protection of civilians) | 保护平民 | 1999 起核心任务 |
| DDR | 解除武装、复员、重返社会 | 多维维和任务组合 |
| robust peacekeeping | 强力维和 | 第三代维和形态 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 宏大 / 深远 / 长期主义
- **匹配理由**:
  - "Eternals"（永恒者）匹配维和机制的持久性——UNTSO 一项行动运行 75 年、200 万人次、横跨三代演化的"长期事业"
  - 宏大的集体感契合"集体得主"的诺奖口径——主角不是某位将军而是 125 国的共同意志
  - 深远基调亦可承载失败与反思段落（卢旺达/斯雷布雷尼察），收束于"维和与冲突复发率降低相关"的学术结论
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` → `presentations/20th_century/United_Nations_peacekeeping/Eternals.wav`
- **时长**: 以实际文件为准，16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/United_Nations_peacekeeping/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/presentations/cover/openpeace_page.tex` | 项目首页模板 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；政治敏感内容只作客观事实记录。**
