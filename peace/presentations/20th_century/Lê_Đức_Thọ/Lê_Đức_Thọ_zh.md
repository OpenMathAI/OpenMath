# 和平奖得主立传提示词（人物专属实例：Lê Đức Thọ）

> 本文件是 OpenPeace 的「和平奖得主立传提示词」，以 Lê Đức Thọ（黎德寿，1973 诺贝尔和平奖，拒绝领奖）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 旗下与 physicist/chemist/medic/literature 平级）。
- **模板来源**：Kenneth_G_Wilson_zh.md 结构母本 + 和平奖项目共享工作流 `peace/PROMPTS_WORKFLOW.md`。
- **本实例**：Lê Đức Thọ（黎德寿，1911–1990，越南革命家、外交家，本名 Phan Đình Khải）。
- **设计哲学**：和平奖立传同样需要「身份信息页」与「事业领域」结构化表达；涉及越南战争与政党职务**只作 page.md 明载的客观事实记录**，不加任何评价性语句；「拒绝领奖」为和平奖史上独特事实，须完整客观呈现。

---

## 二、背景信息 【人物专属】

- **目标人物**：Lê Đức Thọ（1911-10-14 ~ 1990-10-13，享年 78 岁，本名 Phan Đình Khải，绰号 "the Hammer" 铁锤——因其严厉）
- **诺奖年份与官方获奖理由**（1973，与 Henry Kissinger 共享；英文原文照抄 `peace/nobel_peace_citations.json`，中译照抄名录，禁止改写）：
  > "for jointly having negotiated a cease fire in Vietnam in 1973."（表彰二人共同谈判达成 1973 年越南停火）
- **气质关键词**：**铁笼中磨砺的革命者、巴黎谈判桌上的强硬对手、拒绝领奖的和平奖得主**
- **设计母题**：**谈判桌与潮汐（negotiation table & tide）**——巴黎和谈的长桌意象 + 时间线潮汐（攻势与停火交替），冷峻深红主色呼应其钢铁意志。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Lê_Đức_Thọ/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（已按 page.md 核对）

- **生卒**：1911-10-14 生于法属印度支那 Nam Định 省 Nam Trực（今 Ninh Bình），本名 Phan Đình Khải；1990-10-13 逝于河内（79 岁生日前夜，据报道患癌症）。
- **国籍**：越南（North Vietnam 口径，Nobel 名录 country=North Vietnam）。
- **政党**：印度支那共产党（1930–1945）→ 越南共产党（1945–1990）。
- **早年**：少年投身民族主义运动，青春期大部分在法国殖民监狱度过（1930–1936、1939–1944 两度入狱，关押于昆仑岛 Poulo Condore「虎笼」监狱）；狱中与其他政治犯研读文学、科学与外语，排演莫里哀戏剧。1930 参与创建印度支那共产党。
- **主要职务**：1948 年任南部党委组织委员会副主任；1955 入政治局（至 1986）；1956–1973、1976–1980 两度任党中央组织委员会主任；1960–1986 任书记处书记；1976–1980 任南方事务委员会主席；1980–1986 任书记处常务书记；1986-12 起任党中央委员会顾问（至 1990 去世）；1979–1982 任柬埔寨事务首席顾问。
- **关键荣誉**：Nobel Peace Prize 1973（**拒绝领奖**）；金星勋章、十月革命勋章（frontmatter award_received）。
- **核心事业清单**：① 1930 参与创建印度支那共产党；② 抗法独立运动（1945–1954 日内瓦协定）；③ 监督南方革命运动（1956 起）；④ 巴黎和谈（1968–1973，与 Kissinger 秘密会谈主导停火）；⑤ 1974–1975 战略指挥（胡志明小道公路化、1975 春季战役批准）；⑥ 晚年党政顾问。
- **关键时间线（17 节点）**：1911 生 Nam Định → 1930 参与创建印度支那共产党 → 1930–1936 首次入狱（虎笼）→ 1939–1944 再次入狱 → 1945 出狱后领导 Viet Minh 抗法 → 1948 南部党委组织副主任 → 1954 日内瓦协定 → 1955 入政治局 → 1956 任党中央组织委员会主任 → 1968-06 赴巴黎实际掌控和谈 → 1968-09-08 首会美方代表团团长 Harriman → 1970-02-21 与 Kissinger 首次秘密会谈 → 1972-10-08 达成停火框架草案 → 1973-01-23 与 Kissinger 签署巴黎和平协定 → 1973-12-10 获诺贝尔和平奖并**拒绝领奖** → 1974 胡志明小道公路化 → 1986–1990 任党中央顾问 → 1990-10-13 逝于河内。
- **拒奖声明要点**（page.md 明载原文，可客观引用）：拒绝理由为「巴黎协定签署以来美国与西贡政权严重违反协定多项关键条款、南越和平尚未真正建立」；并称一旦协定得到尊重、枪声沉寂、南越建立真正和平，将考虑接受该奖。

### 第 4 步：事业领域表（与 yaml `fields` 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 巴黎和谈实际主导者 | 核心页 |
| 1 | foreign policy | 外交政策 | 党内主管对外与理论事务 | 政务页 |
| 2 | peace negotiations | 和平谈判 | 1968–1973 巴黎会谈、巴黎和平协定 | 核心页 |
| 3 | revolutionary politics | 革命政治 | 独立运动、建党与组织工作 | 早年页 |

### 第 4.5 步：社会关系表（与 yaml `relations` 完全一致）

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| co-honored | Henry Kissinger | 无向 | 1973 诺贝尔和平奖共同得主，Thọ 拒绝领奖 |
| colleague | Xuân Thuỷ | 无向 | 北越官方代表团团长，Thọ 实际掌控谈判 |

### 第 5 步：配色方案 【manifest 预分配，勿改】

- **主色**：`#7E1E23`（铁锈深红——革命与钢铁意志）
- **诺奖香槟金**：`#C9A227`
- **四分类色（badgeA–D）**：badgeA 巴黎和谈 `#1E4E79`；badgeB 革命早年 `#5C3A21`；badgeC 军事战略 `#2F4F4F`；badgeD 拒奖事件 `#8B6914`
- **背景母题**：淡色长桌横线 + 潮汐波纹（呼应谈判桌与攻势/停火的时间潮汐）

### 第 6 步：幻灯片序列（13 页规划，含身份信息页★必做）

```
00  OpenPeace 项目首页（共享封面）
01  封面 — 铁锤与谈判桌 / Lê Đức Thọ 1911–1990 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（本名、生卒、政党、职务、荣誉、核心领域）
03  早年与铁笼岁月 (1911–1945) — Nam Định 出身、两度入狱、虎笼中的莫里哀
04  抗法独立运动 (1945–1954) — Viet Minh、南部组织工作、日内瓦协定
05  党内组织者 (1955–1967) — 政治局、中央组织委员会
06  巴黎和谈：从公开到秘密 (1968–1971) — Harriman 会谈、1970 与 Kissinger 首会
07  巴黎和平协定 (1972–1973)（核心页）— 1972-10 框架、1973-01-23 签署
08  1973 诺贝尔和平奖与拒绝领奖（★ 必做专页）— 获奖理由、拒奖声明要点、首位获和平奖的亚洲人
09  1974–1975 战略指挥 — 胡志明小道公路化、1975 春季战役（客观事实记录）
10  晚年党政职务 (1976–1990) — 书记处常务书记、中央顾问、柬埔寨事务顾问
11  遗产：和平奖史上唯一的拒奖得主
12  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- **版式**：对齐 Kenneth_G_Wilson 模板骨架；vbox≤10pt、hbox≤50pt；越南语变音符（Đ/ệ/ọ 等）须 XeLaTeX + 完整 Unicode 字体，编译前先单页试渲染。
- **陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方仅 "for jointly having negotiated a cease fire in Vietnam in 1973."，勿扩写 |
| 拒奖归属 | 拒奖的是 Thọ 本人；Kissinger 是未出席典礼+捐奖金+提出退还奖章——两篇各忠于本人页面，勿交叉写错 |
| 本名 | Phan Đình Khải，「Lê Đức Thọ」为化名；绰号 "the Hammer" 可用（page.md 明载） |
| 首位亚洲得主口径 | Thọ 是首位**获**和平奖的亚洲人（拒绝领奖）；佐藤荣作 1974 是首位**接受**和平奖的亚洲人——两者勿混 |
| 越南战争内容 | 一律按 page.md 客观叙述（时间线、谈判、战役），不作评价、不引侮辱性原话（1973 会谈冲突原话禁引） |
| 政党职务 | 只写 page.md 明载的职务与年份；党内清洗（Anti-Party Affair）等仅客观一句话带过或不写 |
| 卒日 | 1990-10-13，79 岁生日（10-14）前夜，勿写错前后 |
| 与 Kissinger 关系 | 仅 co-honored 一条入库；谈判桌上的对抗属史实叙述不建 rivalry 关系 |

### 第 9 步：术语审查

| 英文 | 中文 | 风险 |
|------|------|------|
| Paris Peace Accords | 巴黎和平协定 | 1973-01-27「关于在越南结束战争、恢复和平的协定」 |
| cease fire | 停火 | 获奖理由用词，勿写 armistice |
| Viet Minh | 越盟 | 抗法独立运动 |
| Indochinese Communist Party | 印度支那共产党 | 1930 参与创建 |
| Politburo | 政治局 | 1955–1986 |
| tiger cage | 虎笼牢 | 昆仑岛监狱 |
| Vietnamization | 战争越南化 | Thọ 断言其注定失败（page.md 明载转述） |
| declined the award | 拒绝领奖 | 和平奖史上独有事实 |
| Ho Chi Minh Trail | 胡志明小道 | 1974 公路化 |
| Xuân Thuỷ | 春水 | 北越官方代表团团长，与人名勿混 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Empire Collapse** — Cold Cinema（inspiring-electronic 曲库）
- **匹配理由**：宏大而阴郁的 Drone Orchestra 配乐，匹配 20 世纪殖民帝国解体与冷战大国角力的历史纵深；曲名「帝国崩塌」呼应其一生主线——从反殖民监狱到巴黎谈判桌，见证旧秩序的终结。
- **本地路径**：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`
- **时长处理**：ffmpeg `-shortest` 自动对齐视频长度。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Lê_Đức_Thọ/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录（中译获奖理由照抄源） |
| `peace/nobel_peace_citations.json` | 官方英文获奖理由 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/PROMPTS_WORKFLOW.md` | 共享工作流与红线 |
| `MySQL/data/Lê_Đức_Thọ.yaml` | 入库 yaml（fields/relations 与本文一致） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：政治敏感内容只作客观事实记录，每写一页就 make，看到溢出就修。**
