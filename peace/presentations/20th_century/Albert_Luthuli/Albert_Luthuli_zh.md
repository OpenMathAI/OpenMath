# 和平奖得主立传提示词（OpenPeace 批次实例：Albert Luthuli）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Albert Luthuli（1960 诺贝尔和平奖，南非非暴力反种族隔离运动领袖）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（与 OpenPhysicist / OpenChemist 等共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：沿用物理学家侧标杆 Kenneth G. Wilson 提示词的 0–11 节骨架，适配和平奖得主叙事（身份信息页 + 研究领域/事业领域表 + 社会关系表）。
- **本实例**：Albert John Luthuli（阿尔伯特·卢图利，亦拼 Lutuli）。
- **设计哲学**：和平奖得主立传强调「非暴力斗争的信念史」——事业领域结构化 + 社会关系网（同道、追随者、家庭），构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Albert John Luthuli（c. 1898 ~ 1967-07-21，享年 68–69 岁；生年 1898 为本人自认，具体日期不详）
- **气质关键词**：**非洲首位和平奖得主、非暴力抵抗的旗手、祖鲁人的"人民酋长"** —— 1960 诺贝尔和平奖获奖理由：
  > "for his non-violent struggle against apartheid"（表彰他以非暴力方式反对种族隔离制度的斗争）
- **设计母题**：**燃烧的通行证（burning passbooks）与非暴力之火**。1960 年 Sharpeville 惨案后，Luthuli 与同道当众焚烧通行证——火既是抗争的意象，也是其基督教信仰与甘地式非暴力信念的视觉隐喻；可用多组大小错落的暖色圆与炭色线条呼应。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Albert_Luthuli/page.md`（已抓取，事实基准见第 0 步）
- **参考模板**：
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构母本）
  - 数学家成品参照：`mathematician/presentations/20th_century/` 下黄金骨架（封面/身份页版式）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：社会关系已入库（第 4.5 步），立传 Beamer 完成后由主控将 `has_biography` 置 1。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `peace/presentations/pages/20th_century/Albert_Luthuli/page.md`，**事实基准如下**：
  - 生卒：c. 1898 生于罗得西亚布拉瓦约 Solusi 传教站（今津巴布韦）~ 1967-07-21 卒于南非 Stanger，享年 68–69 岁；**2025-10-30 南非法院裁定其为种族隔离警察殴打致死（非官方当时的"被火车撞击"说法）**
  - 国籍：南非；祖鲁家族，幼年丧父，由母亲 Mtonya 抚养
  - 家庭：妻 Nokukhanya Bhengu（1927 结婚，Adams College 同为教师、祖鲁酋长孙女）；子女 7 人（含 Albertina Luthuli）
  - 教育：ABM 传教学校 → Ohlange Institute（两学期）→ Edendale 卫理公会学校（1917 教学文凭）→ Adams College 高级教师文凭（1920–1922）
  - 任职：Blaauwbosch 乡村学校校长（1917 起）→ Adams College 教师（首批非洲教师之一，教祖鲁历史/音乐/文学）→ Natal Native Teachers' Association 秘书（1928）/主席（1933）→ Groutville（Umvoti River Reserve）酋长（1936-01 就任，1952-11 被政府废黜）→ Natal ANC 主席（1951）→ ANC President-General（1952-12 ~ 1967）
  - 关键荣誉：Nobel Peace Prize 1960（1961-12-10 奥斯陆领取，非洲首位）、Isitwalandwe Medal 1955（缺席授予）、Glasgow 大学 Rector（1962–1965，首位非洲/非白人提名人）、联合国人权奖（United Nations Prize in the Field of Human Rights）
  - 核心事业清单：① Defiance Campaign（1952，抗议通行证法）② Congress Alliance 多种族联盟与 Freedom Charter（1955）③ Treason Trial 被捕与开释（1956–1961）④ Sharpeville 惨案后焚烧通行证（1960）⑤ 四次禁令（banning orders）下坚守非暴力立场 ⑥ 1962 Appeal For Action Against Apartheid（与 Martin Luther King Jr.）
  - 关键时间线（15–20 节点）：c.1898 生于布拉瓦约 → 1908 前后回 Groutville 就学 → 1917 教学文凭/Blaauwbosch 任教 → 1920–1922 Adams College 进修 → 1927 与 Nokukhanya 结婚 → 1928 教师协会秘书 → 1933 教师协会主席 → 1935 当选酋长（1936 就任）→ 1944 加入 ANC → 1946 入 Natives Representative Council → 1951 Natal ANC 主席 → 1952 Defiance Campaign / 被废黜酋长职 / 当选 ANC President-General（Mandela 任副手）→ 1953 首次禁令 → 1955 Isitwalandwe / Freedom Charter → 1956-12-05 Treason Trial 被捕（1957-12 对其撤诉）→ 1959 第三次禁令（五年）→ 1960 Sharpeville / 焚烧通行证 / 被判缓刑 → 1961-10 获 1960 和平奖 / 12-10 奥斯陆领奖 → 1961-12-16 uMkhonto we Sizwe 首次行动 → 1962 当选 Glasgow Rector / 与 King 联合呼吁 → 1964 第四次禁令 → 1966 Robert F. Kennedy 直升机探望 → 1967-07-21 遇害 → 2025-10-30 法院改判谋杀

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Albert_Luthuli/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 `Makefile`，设置 `MAIN=Albert_Luthuli_zh`、`VIDEO_NAME=Albert_Luthuli_zh`

### 第 3 步：收集图片 【人物专属】

- 优先用 `page.md` 正文 Commons 图（如 `55075_Albert_Lutuli.jpg` 奥斯陆领奖演讲照）；下载失败用装饰圆占位并在图注说明

### 第 4 步：研究领域/事业领域表 【已入库，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nonviolent resistance | 非暴力抵抗 | 甘地式公民不服从，Defiance Campaign | 斗争页 |
| 1 | anti-apartheid movement | 反种族隔离运动 | ANC President-General 1952–1967 | 领袖页 |
| 2 | human rights | 人权 | 种族平等、普选权诉求 | 诺奖页 |
| 3 | political leadership | 政治领导 | ANC 全国主席、Congress Alliance | 领袖页 |
| 4 | education | 教育 | 教师/教师协会，教育是抗争起点 | 早年页 |

### 第 4.5 步：社会关系表 【已入库，与 yaml relations 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Mahatma Gandhi | 对方→本人 | Defiance Campaign 非暴力策略取法甘地 |
| influence | John Dube | 对方→本人 | Ohlange Institute 校长，Luthuli 因敬重老校长而加入 ANC |
| colleague | Nelson Mandela | 无向 | Mandela 任其 ANC 副手（1952–1958），后主导转向武装斗争 |
| colleague | Z. K. Matthews | 无向 | Natal 教师协会共事，Treason Trial 同案被告 |
| colleague | Martin Luther King Jr. | 无向 | 1962 联合发布 Appeal For Action Against Apartheid，King 视其为导师 |
| spouse | Nokukhanya Bhengu | 无向 | 1927 结婚，Adams College 教师同事 |

- 入库操作见 `MySQL/data/Albert_Luthuli.yaml`（seed_person.py 幂等入库）
- **方向约定**：influence 为有向（对方影响本人）；colleague/spouse 无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：厚重、坚忍、大地感
- **配色**：深褐（manifest 预分配主色 `#4E342E`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeNonviolence` 非暴力抵抗 — 暖赭 `#B4552D`
  - `badgeANC` 反种族隔离 — 深绿 `#1B5E20`
  - `badgeNobel` 诺奖 — 香槟金 `#C9A227`
  - `badgeHeritage` 祖鲁传统 — 靛蓝 `#283593`
- **背景母题**：柔和暖色圆（炭火/大地图形错落），呼应「燃烧的通行证与非暴力之火」母题

### 5.1 和平奖得主格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无肖像用装饰圆占位。
2. **封面有国籍**：明示 South Africa，底部状态栏给出 `国籍 | 机构（ANC）| 主要奖项` 三要素。
3. **必须有身份信息页**：左侧头像 + 右侧信息网格，含至少：生卒、本名（Albert John Luthuli）、国籍、出生地、教育、任职、主要荣誉、核心事业。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 封面模板）
01  封面 — 非暴力抵抗的旗手 / Albert Luthuli c.1898–1967 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名、教育、酋长任职、ANC、荣誉）
03  核心事业概览 — 非暴力抵抗 / ANC 领袖 / 多种族联盟 / 诺奖
04  早年：从罗得西亚到 Groutville (c.1898–1917) — 传教站出生、丧父、Ohlange/Edendale
05  教师生涯 (1917–1935) — Blaauwbosch 校长、Adams College、教师协会
06  酋长岁月 (1936–1952) — Ubuntu 治理、"人民酋长"、被政府废黜
07  Defiance Campaign (1952) — 甘地式公民不服从、8,500 志愿者
08  ANC President-General (1952–) — Mandela 副手、四次禁令、Treason Trial
09  Freedom Charter 与多种族联盟 (1955) — Congress Alliance、Isitwalandwe
10  Sharpeville 与焚烧通行证 (1960) — 惨案、抗议、缓刑判决
11  诺贝尔和平奖 (1961 领奖) — 非洲首位、奥斯陆演讲、政府敌意
12  晚年与禁令下 (1962–1967) — Glasgow Rector、与 King 的联合呼吁、RFK 探望
13  身后：真相与遗产 — 2025 法院改判谋杀、Luthuli House、Luthuli Museum
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

**Luthuli 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生年口径 | c. 1898（本人自认 1898，**具体日期不详**），勿编造出生日期；享年写 68–69 岁 |
| 死因口径 | 官方当时说法是被货运火车撞击；**2025-10-30 南非法院裁定被种族隔离警察殴打致死**——两说必须按时间线分别呈现，勿混用 |
| 获奖理由 | 官方为 "for his non-violent struggle against apartheid"；Wikipedia 正文另有 "for his use of nonviolent methods in his fight against racial discrimination" 的转述，勿混用 |
| 武装斗争立场 | Luthuli **最初反对、后来逐步接受**武装抵抗，但个人始终信守非暴力；勿写成"始终反对"或"亲自领导 MK" |
| uMkhonto we Sizwe | 由 Mandela 于 1961-12-16 发起；Luthuli 建议的是"两条斗争溪流"（ANC 保持非暴力 + 独立军事 organ），勿写成其创建者 |
| 首位口径 | 他是**首位非洲人（first African person）**获和平奖，勿泛化为"首位黑人诺奖得主" |
| 叔父关系 | 监护人 Martin Luthuli 是**叔父**，非父子，禁入 parent-child 关系 |
| 领奖年份 | 1960 年度奖 1961-12-10 于奥斯陆领取（护照需政府特批），两处年份勿混 |
| 政治敏感红线 | 种族隔离只作 page.md 明载的客观事实记录，不加评价性语句；南非政府官员只按事实呈现 |
| 无载禁写 | 1962 Appeal 为 King 与 Luthuli 联合发布（page.md 明载）；除此之外勿给 King/Luthuli 编造更多互动 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| apartheid | 种族隔离 | 制度名，勿译"种族隔离政策"以外的评价性表述 |
| Defiance Campaign | 蔑视不公正法运动 | 1952，公民不服从 |
| pass laws | 通行证法 | 非洲人须随身携带通行证 |
| banning order | 禁令 | 政府限制人身/言论的行政命令 |
| Congress Alliance | 大会联盟 | 多种族反种族隔离联盟 |
| Freedom Charter | 自由宪章 | 1955 Kliptown 通过 |
| Treason Trial | 叛国罪审判 | 1956–1961，156 人被捕 |
| Sharpeville massacre | 沙佩维尔惨案 | 1960-03-21，69 人死亡 |
| President-General | 全国主席 | ANC 职务头衔 |
| Inkosi | 酋长 | 祖鲁语头衔 |
| uMkhonto we Sizwe | "民族之矛" | ANC 武装组织，1961 成立 |
| Ubuntu | 乌班图 | "人性共享"的祖鲁伦理概念 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 时间感 / 纪录片 / 坚忍
- **匹配理由**:
  - "时间感" 匹配其一生跨度——从罗得西亚传教站到奥斯陆领奖台，再到 2025 年迟到六十年的真相裁决
  - "纪录片" 匹配叙事——教师 → 酋长 → ANC 领袖 → 禁令下的坚守，是信念演进的纪录而非戏剧化英雄史诗
  - "坚忍" 匹配其气质——四次禁令下不改其志的沉静力量
- **本地路径**: `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` → `presentations/20th_century/Albert_Luthuli/The-Flow-of-Time.wav`
- **时长**: 以实际音频时长为准，15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Albert_Luthuli/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Albert_Luthuli.yaml` | 研究领域 + 社会关系入库文件 |
| `peace/nobel_peace_citations.json` | 获奖理由英文原文 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
