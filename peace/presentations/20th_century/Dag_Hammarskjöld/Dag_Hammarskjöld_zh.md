# 和平奖得主立传提示词（OpenPeace 批次实例：Dag Hammarskjöld）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Dag Hammarskjöld（1961 诺贝尔和平奖，联合国第二任秘书长、史上唯一身后追授的和平奖得主）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（与 OpenPhysicist / OpenChemist 等共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：沿用物理学家侧标杆 Kenneth G. Wilson 提示词的 0–11 节骨架，适配和平奖得主叙事（身份信息页 + 研究领域/事业领域表 + 社会关系表）。
- **本实例**：Dag Hjalmar Agne Carl Hammarskjöld（达格·哈马舍尔德）。
- **设计哲学**：和平奖得主立传强调「国际公共服务与个人信念的交汇」——事业领域结构化 + 社会关系网（同僚、思想来源、争议对手），构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Dag Hammarskjöld（1905-07-29 ~ 1961-09-18，享年 56 岁）
- **气质关键词**：**唯一身后追授的和平奖得主、联合国缔造者、"行动中的圣徒"** —— 1961 诺贝尔和平奖获奖理由（身后追授）：
  > "for developing the UN into an effective and constructive international organization, capable of giving life to the principles and aims expressed in the UN Charter"（表彰他将联合国发展为一个能够践行《联合国宪章》原则与宗旨的、卓有成效的建设性国际组织）
- **设计母题**：**"路标"（Vägmärken / Markings）**。其唯一著作以路标为名——道路、界石、航线的视觉语言，契合他"行动中的内省者"气质；可用冷峻的蓝灰色几何路标线条 + 联合国蓝与香槟金呼应。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Dag_Hammarskjöld/page.md`（已抓取，事实基准见第 0 步）
- **参考模板**：
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构母本）
  - 同批成品参照：`peace/presentations/20th_century/Albert_Luthuli/Albert_Luthuli_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：社会关系已入库（第 4.5 步），立传 Beamer 完成后由主控将 `has_biography` 置 1。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `peace/presentations/pages/20th_century/Dag_Hammarskjöld/page.md`，**事实基准如下**：
  - 生卒：1905-07-29 生于瑞典延雪平（Jönköping）~ 1961-09-18 卒于北罗得西亚恩多拉（Ndola，今赞比亚）空难，享年 56 岁
  - 国籍：瑞典；贵族 Hammarskjöld 家族第四子，童年在乌普萨拉城堡
  - 家庭：父 Hjalmar Hammarskjöld（瑞典首相 1914–1917）；母 Agnes Hammarskjöld；终生未婚
  - 教育：Uppsala 大学（1930 年前获哲学副博士 Licentiate + 法学硕士）→ Stockholm 大学经济学博士（论文 "Konjunkturspridningen"）
  - 任职：失业委员会助理秘书（1930 起）→ Riksbank 秘书（1936）/央行总理事会主席（1941–1948）→ 财政部国务秘书（1936–1945）→ OEEC 瑞典代表（1947–1953）→ 外交部内阁秘书（1949–1951）→ Erlander 政府不管部大臣（1951–1953）→ **联合国第二任秘书长（1953-04-10 ~ 1961-09-18，47 岁当选为史上最年轻）**→ 瑞典学院院士（1954-12-20 继承其父空缺席位）
  - 关键荣誉：Nobel Peace Prize 1961（唯一身后追授）；北极星大十字勋章等外国勋衔；Carleton 大学首位荣誉博士（1954）；Oxford/Harvard/Yale/Princeton/Columbia 等十余所荣誉博士；2015 年起头像上 1000 克朗纸币
  - 核心事业清单：① 秘书处建设（4,000 名行政人员章程、冥想室）② 1955 访华促成 11 名美军飞行员获释 ③ 1956 UNEF 首支维和部队与苏伊士危机斡旋 ④ 以色列与阿拉伯国家间调停 ⑤ 1960 刚果危机 ONUC（近 2 万人、UN 最大行动之一）⑥ 遇难前口述 6,000 词最后报告
  - 关键时间线（15–20 节点）：1905 生于延雪平 → 1930 双学位 → 1936 央行秘书/财政部国务秘书 → 1941–1948 央行总理事会主席 → 1947–1953 OEEC 代表 → 1949 外交部内阁秘书 → 1951 不管部大臣 / 联大瑞典副代表（巴黎）→ 1952 联大瑞典首席代表（纽约）→ 1953-04-10 就任联合国秘书长 → 1954 入瑞典学院 → 1955 访华 → 1956 UNEF / 苏伊士危机 → 1957-09-26 全票连任 → 1960 刚果危机 ONUC / 苏联要求其辞职并主张"三驾马车" → 1961-02 联大授权维和部队动武 → 1961-09-17–18 恩多拉空难（DC-6 SE-BDY）→ 1961 身后追授诺贝尔和平奖 → 1963 遗作 *Vägmärken*（Markings）出版 → 1997 安理会 1121 号决议设 Dag Hammarskjöld Medal → 死因调查延续至 2010s（仍未定论）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Dag_Hammarskjöld/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 `Makefile`，设置 `MAIN=Dag_Hammarskjöld_zh`、`VIDEO_NAME=Dag_Hammarskjöld_zh`

### 第 3 步：收集图片 【人物专属】

- 优先用 `page.md` 正文 Commons 图（如 `Dag_Hammarskjold_outside_the_UN_building.jpg` 1953 年联合国总部照）；下载失败用装饰圆占位并在图注说明

### 第 4 步：研究领域/事业领域表 【已入库，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 调停苏伊士、访华、以色列-阿拉伯斡旋 | 秘书长页 |
| 1 | international organization | 国际组织 | 把联合国建成有效建设性机构（诺奖理由） | 核心页 |
| 2 | peacekeeping | 维和 | UNEF / ONUC 首批维和行动缔造者 | 危机页 |
| 3 | international economics | 国际经济 | 财政部/央行/OEEC/马歇尔计划会议 | 早年页 |
| 4 | literature | 文学 | 遗作 *Vägmärken*（Markings）随笔与俳句 | 晚年页 |

### 第 4.5 步：社会关系表 【已入库，与 yaml relations 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Hjalmar Hammarskjöld | 无向 | 父，瑞典首相（1914–1917），其院士席位由本人继承 |
| parent-child | Agnes Hammarskjöld | 无向 | 母 |
| colleague | Trygve Lie | 无向 | 联合国首任秘书长，1952 辞职后由其接任 |
| colleague | U Thant | 无向 | 第三任秘书长，1961 空难后接任 |
| colleague | W. H. Auden | 无向 | 友人，英语版 *Markings* 序言作者 |
| influence | Martin Buber | 对方→本人 | 遇难时正在翻译其《I and Thou》，灵性思想来源 |
| controversy | Patrice Lumumba | 无向 | 刚果危机中拒绝支持其民选政府，遭不结盟与社会主义阵营激烈批评 |

- 入库操作见 `MySQL/data/Dag_Hammarskjöld.yaml`（seed_person.py 幂等入库）
- **方向约定**：influence 为有向（对方影响本人）；colleague/spouse/parent-child/controversy 无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：冷峻、克制、国际主义
- **配色**：深青蓝（manifest 预分配主色 `#0F4C5C`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeUN` 联合国事业 — 联合国蓝 `#3B7DC4`
  - `badgePeacekeeping` 维和 — 橄榄绿 `#4E6B30`
  - `badgeNobel` 诺奖 — 香槟金 `#C9A227`
  - `badgeMarkings` 文学与灵性 — 暮紫 `#52307C`
- **背景母题**：稀疏冷色几何路标线条（大块圆 + 直线航迹），呼应「Vägmärken 路标」母题

### 5.1 和平奖得主格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无肖像用装饰圆占位。
2. **封面有国籍**：明示 Sweden，底部状态栏给出 `国籍 | 机构（联合国）| 主要奖项` 三要素。
3. **必须有身份信息页**：左侧头像 + 右侧信息网格，含至少：生卒、全名、国籍、出生地、教育、任职（瑞典文官系统→联合国）、主要荣誉、核心事业。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 封面模板）
01  封面 — 联合国缔造者 / Dag Hammarskjöld 1905–1961 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、全名、教育、瑞典文官任职、联合国、荣誉）
03  核心事业概览 — 国际组织建设 / 外交调停 / 维和 / 文学遗产
04  贵族之家与早年 (1905–1936) — 延雪平出生、乌普萨拉城堡、双学位
05  瑞典文官系统 (1936–1953) — 央行、财政部、OEEC、不管部大臣
06  秘书长当选 (1953) — 苏联意外支持、4 月愚人节电话、史上最年轻
07  组织建设者 — 4,000 人秘书处、冥想室、员工关系
08  危机调停 — 1955 访华救飞行员、以色列-阿拉伯、苏伊士与 UNEF
09  刚果危机 (1960–1961) — ONUC、苏联"三驾马车"要求、争议立场
10  恩多拉空难 (1961-09-18) — 停火谈判途中、死因悬案（多起调查仍未定论）
11  诺贝尔和平奖 — 唯一身后追授、获奖理由、Kennedy 与后世评价
12  Markings：行动中的内省者 — Vägmärken 1963 出版、Auden 序、Buber 与中世纪神秘主义
13  遗产 — Dag Hammarskjöld Library/Medal/基金会、1000 克朗纸币、第三世界争议并存
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

**Hammarskjöld 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 身后追授口径 | 他是和平奖**唯一身后追授**得主（posthumous），1961 年度奖于其 9 月遇难后颁发，勿写"生前领奖" |
| 获奖理由 | 官方为 "for developing the UN into an effective and constructive international organization..."，强调**组织建设**，勿写成"为维和"或"为调停" |
| 死因 | 空难原因至今未定论——1962 罗得西亚调查归因飞行员失误、后续调查无法确定、另有击落假说（Operation Celeste 文件真伪无法证实）——只按 page.md 时间线客观罗列各说，勿下结论 |
| 刚果危机评价 | 西方高度评价与第三世界激烈批评（Lumumba 事件）**并存**，必须双面呈现，勿单侧叙事；"communist puppet" 一语是对英外交官 Patrick Dean 所言，仅可作事实转述 |
| 恋情/性向 | Trygve Lie 的传闻被 Urquhart 传记否定，禁写；终生未婚是事实，"秘书长不应结婚"是其私人手稿原话，仅可注明出处转述 |
| 当选悬念 | 1953-04-01 他以为记者电话是愚人节玩笑——时间线（3-31 安理会投票 → 4-7 联大 57-1-1 → 4-10 就任）勿混 |
| 父亲席位 | 1954 他继承的是**其父空出的瑞典学院席位**，勿写成"其父提名" |
| 政治敏感红线 | 冷战、刚果去殖民化、苏联"三驾马车"等内容一律只作 page.md 明载的客观事实记录，不加评价性语句 |
| 无载禁写 | 与 Trygve Lie 的传闻风波属他人传记转述、Kennedy 赞语是事后评价——均不建关系；中世纪神秘主义者 Eckhart/Ruysbroek 仅思想背景，不入库 |
| 德文姓氏 | Hammarskjöld 含 ö，LaTeX 需正确渲染（xelatex 直接支持），目录/文件名沿用 manifest 的 `Dag_Hammarskjöld` |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Secretary-General | （联合国）秘书长 | 勿与政府"秘书长"混译 |
| UN Charter | 《联合国宪章》 | 诺奖理由核心文本 |
| peacekeeping | 维和 | UNEF 为首支维和部队 |
| UNEF | 第一支紧急部队 | 1956 设立 |
| ONUC | 联合国刚果行动 | 1960 设立，UN 最大行动之一 |
| Congo Crisis | 刚果危机 | 1960–61，其身死与争议的背景 |
| troika | 三驾马车 | 苏联主张的三人轮值方案 |
| Katanga | 加丹加 | 分离主义政权，Tshombe 领导 |
| Vägmärken / Markings | 《路标》 | 1963 遗作，散文与俳句合集 |
| meditation room | 冥想室 | 联合国总部内的静思空间 |
| Swedish Academy | 瑞典学院 | 1954 当选院士 |
| posthumous award | 身后追授 | 和平奖史上唯一 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Daylight** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 明亮 / 志向 / 纪录片
- **匹配理由**:
  - "明亮" 匹配其"行动中的内省者"气质——把光明带入国际秩序的黑暗角落（苏伊士、刚果、访华）
  - "志向" 匹配其事业本质——把新生的联合国锻造成有效机构，是一次未竟而影响深远的制度建设
  - "纪录片" 匹配叙事——瑞典文官 → 史上最年轻秘书长 → 危机调停 → 恩多拉空难，是公共服务的纪录
- **本地路径**: `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` → `presentations/20th_century/Dag_Hammarskjöld/Daylight.wav`
- **时长**: 以实际音频时长为准，15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Dag_Hammarskjöld/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Dag_Hammarskjöld.yaml` | 研究领域 + 社会关系入库文件 |
| `peace/nobel_peace_citations.json` | 获奖理由英文原文 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
