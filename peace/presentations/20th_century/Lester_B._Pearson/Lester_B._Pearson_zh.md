# 和平奖得主立传提示词（OpenPeace：Lester Bowles Pearson）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Lester Bowles Pearson（1957 诺贝尔和平奖，苏伊士危机与联合国紧急部队；后任加拿大第 14 任总理）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Lester Bowles Pearson（莱斯特·鲍尔斯·皮尔逊，1957 诺贝尔和平奖）——外交官出身的政治家，现代维和概念之父之一，也是唯一获诺贝尔和平奖的加拿大总理。
- **设计哲学**：保留「身份信息页」与「事业领域结构化表达」两大骨架；本篇叙事重心是**从外交官到维和之父再到国内改革者**：苏伊士危机的斡旋与加拿大福利国家的奠基构成双线。

---

## 二、背景信息 【人物专属】

- **目标人物**：Lester Bowles Pearson（1897-04-23 ~ 1972-12-27，享年 75 岁；昵称 Mike）
- **气质关键词**：**维和之父、斡旋大师、学者型总理** —— 1957 诺贝尔和平奖获奖理由：
  > "for his crucial contribution to the deployment of a United Nations Emergency Force in the wake of the Suez Crisis"（表彰他在苏伊士危机后为部署联合国紧急部队做出的关键贡献）
- **设计母题**：**蓝盔与枫叶（blue helmet & maple leaf）**。以联合国蓝盔轮廓、枫叶、多边会议圆桌构成视觉语言，呼应「把国家军队变成国际和平工具」的核心创意。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Lester_B._Pearson/page.md`
- **参考模板**：标杆提示词 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页模板 `peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：核对本地页面，建立事实基准 【人物专属】

- ✅ 页面已抓取（frontmatter：QID Q128604 / 生卒 / 国籍 Canada / 职业 / 奖项 / 教育经历）
- **事实基准（第一轮已核对，全部以 page.md 为准）**：
  - 生卒：1897-04-23 生于安大略省多伦多 Newtonbrook（约克乡）~ 1972-12-27 逝于渥太华家中（癌症扩散至肝），享年 75 岁；葬魁北克 Wakefield 的 Maclaren Cemetery
  - 国籍：加拿大
  - 家庭：父 Edwin Arthur Pearson 为卫理公会（后加拿大联合教会）牧师；1925 娶 Maryon Moody（曾任其学生），育一子 Geoffrey（后为外交官）一女 Patricia
  - 教育：Hamilton Collegiate Institute 1913 → Victoria College（多伦多大学）BA 1919 → Massey 基金奖学金赴牛津 St John's College（1921–1923 现代史 BA 二等荣誉，1925 MA）
  - 一战：1915 以加拿大陆军医疗队列兵赴萨洛尼卡前线，后晋临时中尉并转入英国皇家飞行军团（RFC），飞行教官因其名 "Lester" 太温和而赐名 Mike——沿用终身
  - 任职主线：1927 以外交考试第一名入 External Affairs → 1931/1934 两皇家委员会 → 1935 驻英高级专员公署 → 1942 驻美使馆参赞 → 1945-01 加拿大第二任驻美大使（至 1946-09）→ 1948 外交部长（至 1957）→ 1952–1953 联大第七 session 主席 → 1958 自由党领袖 → 1963-04-22 第 14 任加拿大总理（1963–1968）→ 1968 退休
  - 关键荣誉：Nobel Peace Prize 1957；OBE；Order of Merit；Companion of the Order of Canada；多所大学荣誉博士；Canadian Baseball Hall of Fame
  - 核心事业清单：① 联合国与 NATO 的创建参与者；② 1952–1953 联大主席；③ 1956 苏伊士危机中提出联合国紧急部队（UNEF）方案——现代维和的起点；④ 总理任内：学生贷款/加拿大退休金计划/全民医保/枫叶旗/双语与二元文化皇家委员会/积分制移民；⑤ 让加拿大不参加越战；⑥ 退休后任 World Bank 赞助的 Pearson 委员会主席（1968–1969）与 IDRC 首任董事会主席（1970–1972）
  - 关键时间线（15–20 节点）：1897 出生 → 1913 入 Victoria College → 1915 医疗队赴欧 → 1917 转 RFC 得名 Mike → 1919 多伦多 BA → 1921–1923 牛津 → 1923 Oxford 冰球队夺首届 Spengler Cup → 1925 结婚 → 1927 入外交部 → 1935 驻伦敦 → 1942 驻华盛顿 → 1945 驻美大使 → 1948 外交部长+国会议员 → 1948–1949 参与创建 NATO → 1952 联大主席 → 1953 竞选联合国秘书长被苏联否决 → 1956-11 五天环球穿梭组建 UNEF → 1957 诺贝尔和平奖 → 1958 自由党领袖 → 1958/1962 两败于 Diefenbaker → 1963-04 任总理 → 1965 枫叶旗确立 → 1967 宣布退休 → 1968 卸任 → 1968–1969 Pearson 委员会 → 1970 摘除右眼肿瘤 → 1972-12-27 逝世

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- 在 `peace/presentations/20th_century/Lester_B._Pearson/` 下建 `images/`；Makefile 复制同项目成品并设 `MAIN=Lester_B._Pearson_zh`
- 肖像：优先 page.md/images.txt 中的 c. 1963 正式肖像；下载失败用装饰圆占位并记录

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peacekeeping | 维和 | UNEF 方案，现代维和概念之父之一 | 苏伊士页 |
| 1 | diplomacy | 外交 | 驻美大使、外交部长 9 年 | 外交页 |
| 2 | international relations | 国际关系 | 联大主席、UN/NATO 创建参与 | 国际页 |
| 3 | multilateralism | 多边主义 | 以多边机制化解大国对抗 | 苏伊士页 |
| 4 | social policy | 社会政策 | 医保/退休金/枫叶旗/积分移民 | 总理页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Maryon Moody | 无向 | 1925 结婚，曾任其在多伦多大学的学生 |
| parent-child | Geoffrey Pearson | 无向 | 独子，后为外交官 |
| colleague | Dag Hammarskjöld | 无向 | 1956 共同组织联合国紧急部队，现代维和之父并称 |
| colleague | Louis St. Laurent | 无向 | 外交部长任内共事，1958 支持其接任自由党领袖 |
| colleague | Vincent Massey | 无向 | 驻英高级专员公署任职时上司 |
| rival | John Diefenbaker | 无向 | 1958/1962 大选两度落败，1963 击败之 |

> 只收 page.md 明载的关系；1946/1953 两度被苏联否决联合国秘书长提名是事件非关系，不入关系表；Trudeau/Turner/Chrétien 系其招揽的继任者，属党内谱系，不入库。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色（manifest 预分配，勿改）**：石板灰蓝 `#37474F`
- 辅色：诺奖香槟金 `#C9A227` + 枫叶红 `#B0413E`（点缀）
- 四分类色：`badgeUN` 维和 — 联合国蓝 `#2E5E8C`；`badgeDip` 外交 — 青绿 `#0E7C7B`；`badgePM` 总理施政 — 枫叶红 `#B0413E`；`badgeSport` 运动与学界 — 琥珀 `#E07B30`
- **背景母题**：柔和气泡 + 蓝盔轮廓与枫叶剪影，呼应「蓝盔与枫叶」设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页（★）：左头像 + 右信息网格（生卒、本名与昵称、国籍、出生地、教育、任职、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 维和之父 / Lester B. Pearson 1897–1972 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心事业概览 — UNEF / 联大主席 / UN·NATO 创建 / 总理施政
04  早年：牧师之家与多伦多 (1897–1919) — Mike 昵称之前的学生时代
05  一战与牛津 (1915–1925) — 萨洛尼卡担架兵、RFC 飞行员、Spengler Cup
06  外交官之路 (1927–1948) — 驻伦敦/华盛顿、UN 与 NATO 创建
07  联大主席与秘书长之憾 (1952–1953) — 苏联两度否决
08  苏伊士危机与 UNEF (1956)（核心贡献页）— 五天环球穿梭、现代维和起点
09  诺贝尔和平奖 1957 — 获奖理由 + 委员会「saved the world」评价的争议并陈
10  反对党岁月 (1958–1963) — 两败于 Diefenbaker
11  总理：福利国家与枫叶旗 (1963–1968) — 医保/CPP/双语委员会/积分移民
12  家庭与晚年 — Maryon 与 Geoff、Pearson 委员会、Carleton 校长、去世
13  荣誉与认可 — Nobel 1957 · Order of Merit · Order of Canada
14  遗产：维和观念与加拿大身份
15  结尾
```

### 第 7–8 步：Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Pearson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方为 "for his crucial contribution to the deployment of a United Nations Emergency Force in the wake of the Suez Crisis"，强调「部署联合国紧急部队」，勿写成「调解阿拉伯-以色列冲突」 |
| 诺奖与批评并陈 | 评选委员会称其「saved the world」，但同时有批评者指责他「背叛宗主国」（加英关系）——两面都要呈现，勿只写一面 |
| 维和之父并称 | page.md 明载 Pearson 与 UN 秘书长 Dag Hammarskjöld 被视为现代维和概念之父（fathers of peacekeeping），勿写成 Pearson 独享 |
| 秘书长之憾 | 1946 与 1953 两度是联合国秘书长首选候选人、均被苏联否决（1953 年安理会 10/11 票）；哈马舍尔德当选后秘书长均出自中立国——年份勿混 |
| 昵称 | Mike 是 RFC 飞行教官所赐（"Lester" 太温和），官方文件用 Lester、亲友称 Mike——勿颠倒 |
| 女儿 Patricia | page.md 明载育一女 Patricia，但无独立链接与生平——正文可一句带过，不入关系表 |
| 军衔口径 | 一战终衔为临时中尉（1917 授）+ RFC flying officer；勿写「参加战斗飞行部队作战」夸大——1918 在伦敦被公共汽车撞伤后遣返 |
| 冰球口径 | Oxford University Ice Hockey Club 夺 1923 首届 Spengler Cup 是集体荣誉；"Herr Zig-Zag" 是瑞士人给他的绰号——两事勿混为一段 |
| 退休职务 | 1968–1969 World Bank 赞助的 Pearson 委员会主席；1970–1972 IDRC 首任董事会主席；1969–1972 Carleton 校长——三职年份勿混 |
| 同名区分 | 与统计学家 Karl Pearson 无关；儿子 Geoffrey Pearson 与其同名家族勿混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| United Nations Emergency Force (UNEF) | 联合国紧急部队 | 第一支联合国维和部队，勿与 general peacekeeping 混 |
| Suez Crisis | 苏伊士危机 | 1956，获奖直接背景 |
| peacekeeping | 维和 | 现代维和概念之父并称 |
| Secretary of State for External Affairs | （加拿大）外交事务国务秘书/外交部长 | 旧译「外交国务秘书」，实为外长 |
| President of the UN General Assembly | 联合国大会主席 | 第七届（1952–1953） |
| Leader of the Official Opposition | 官方反对党领袖 | 1958–1963 |
| Canada Pension Plan | 加拿大退休金计划 | CPP，总理任内施政 |
| universal health care | 全民医保 | 总理任内奠基 |
| Great Canadian flag debate | 加拿大国旗大辩论 | 1965 枫叶旗 |
| points-based immigration system | 积分制移民体系 | 加拿大为全球首个 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 苏醒 / 上扬 / 纪录片
- **匹配理由**:
  - 「苏醒」匹配其历史角色——在苏伊士危机的炮火中唤醒「以国际部队替代对抗」的现代维和观念
  - 「上扬」匹配其外交官到总理的上升曲线——驻美大使 → 外交部长 → 联大主席 → 诺奖 → 总理
  - 「纪录片」匹配双线叙事——国际维和线与国内改革线并行推进
- **本地路径**: `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 复制为 `presentations/20th_century/Lester_B._Pearson/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Lester_B._Pearson/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `peace/prompt_manifest.json` | batch=peace-batch-11（主色/BGM 预分配） |
| `MySQL/data/Lester_B._Pearson.yaml` | 研究领域+社会关系入库文件 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
