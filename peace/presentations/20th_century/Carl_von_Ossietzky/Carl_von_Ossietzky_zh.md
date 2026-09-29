# 和平奖得主立传提示词（OpenPeace：Carl von Ossietzky）

> **本文件是 OpenPeace 项目的人物专属立传提示词**，以 Carl von Ossietzky（1935 诺贝尔和平奖，揭露德国秘密重整军备的记者）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节 + 第 0–9 步）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenPhysicist / OpenMedic 同属 OpenMathAI 共享仓库）。
- **模板来源**：综合物理学家标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与医学/化学侧批量立传经验。
- **本实例**：Carl von Ossietzky（卡尔·冯·奥西茨基），《Die Weltbühne》主编、纳粹集中营中的和平奖得主。
- **设计哲学**：和平奖得主立传的核心骨架是「身份信息页 + 结构化事业领域」；记者型得主的主线是「笔—审判—狱中获奖」，务必保留身份信息页；本篇涉及纳粹迫害史实，**只作 page.md 明载的客观事实记录，不加评价性语句**。

---

## 二、背景信息 【人物专属】

- **目标人物**：Carl von Ossietzky（1889-10-03 ~ 1938-05-04，享年 48 岁）
- **气质关键词**：**《世界舞台》主编、秘密重整军备的揭露者、狱中的诺贝尔奖得主** —— 1935 诺贝尔和平奖获奖理由：
  > "for his burning love for freedom of thought and expression and his valuable contribution to the cause of peace."（表彰他对思想自由与言论自由的炽热之爱，以及他对和平事业的宝贵贡献）
- **设计母题**：**铁幕下的一支笔（the pen behind bars）**。其一生围绕「以新闻对抗军事秘密国家」——视觉上可用「审稿灯/监狱窗格/报纸铅字」呼应；配色深海军蓝呼应其沉着与悲剧。
- **本地 Wikipedia**：`peace/presentations/pages/20th_century/Carl_von_Ossietzky/page.md`（含 frontmatter QID Q76358 与 infobox）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - 名录（官方理由照抄源）：`peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（据本地 page.md，无载禁写） 【人物专属】

- 生卒：1889-10-03 生于汉堡 ~ 1938-05-04 逝于柏林 Pankow 区 Nordend 医院（肺结核及集中营虐待后遗症，警方监管中），享年 48 岁
- 国籍：German Reich / Germany
- 家庭：父 Carl Ignatius von Ossietzky（上西里西亚新教徒、速记员，Ossietzky 两岁时去世）；母 Rosalie（née Pratzka，虔诚天主教徒）；1889-11-10 汉堡受洗为天主教徒、1904-03-23 在 Lutheran Hauptkirche St Michaelis 坚信礼
- 姓氏 von 的来历：本人半开玩笑地解释为「勃兰登堡选帝侯欠饷、整团授爵」传说，来源不明
- 教育：未完成 Realschule 学业即入新闻业（选题从剧评到女性主义与早期汽车化问题）
- 家庭（自建）：1913 与 Maud Lichfield-Woods（曼彻斯特妇女参政论者、英国殖民官员之女、海得拉巴印度公主曾孙女）结婚；独女 Rosalinde von Ossietzky-Palm
- 任职/身份：1919 任 German Peace Society（Deutsche Friedensgesellschaft）秘书；1927 接替 Tucholsky 出任《Die Weltbühne》主编；「无家可归的左派」领袖之一
- 关键荣誉：Nobel Peace Prize 1935（1936 年颁发，被禁止赴奥斯陆领奖）
- 核心事业清单（4–6 条）：
  1. 反军国主义与和平主义（自称 1913 年起成为和平主义者）
  2. 《Die Weltbühne》主编：揭露违反《凡尔赛条约》的秘密重整军备（Abteilung M 报道 1929-03-12 刊出，作者 Walter Kreiser）
  3. 1931-11-23 被帝国法院以叛国与间谍罪判 18 个月监禁，1932 圣诞大赦获释
  4. 纳粹上台后继续发声：1933-02-28 国会纵火案后被捕，先后关押于 Spandau 监狱与 Esterwegen 集中营等地
  5. 1936 自医院发表声明接受和平奖（公民不服从行动）
  6. 对魏玛司法双重标准的统计披露与批判（1923 统计研究）
- 关键时间线（15–20 节点）：1889 出生 → 1891 丧父 → 1904 坚信礼 → 1913 结婚 → 一战被征入伍 → 1919 和平会社秘书 → 1920s 无家左派 → 1927 接任主编 → 1929 Abteilung M 报道 → 1931 定罪 → 1932 圣诞大赦 → 1933-02-28 被捕 → Esterwegen 集中营 → 1935 和平奖决定 → 1936 领奖声明 → 1936-05 西区医院 → 1938-05-04 去世

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Ossietzky 的事业领域（按 rank 排序，已入库 person_field，与 yaml fields 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pacifism | 和平主义 | 1919 和平会社秘书、一生反军国主义 | 核心页 |
| 1 | journalism | 新闻事业 | Die Weltbühne 主编 | 主编页 |
| 2 | freedom of expression | 言论自由 | 诺奖理由核心词 | 获奖页 |
| 3 | political commentary | 政治评论 | 魏玛司法与军国主义批判 | 评论页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Carl_von_Ossietzky.yaml` 完全一致；只收 page.md 明载关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Maud Lichfield-Woods | 无向 | 1913 结婚 |
| parent-child | Carl Ignatius von Ossietzky | 父→子 | 父亲，速记员，Ossietzky 两岁时去世 |
| parent-child | Rosalie Pratzka | 父→子 | 母亲 |
| parent-child | Rosalinde von Ossietzky-Palm | 父→女 | 独女，后向奥尔登堡大学捐献其档案与藏书 |
| colleague | Kurt Tucholsky | 无向 | 1927 Ossietzky 接替其出任 Die Weltbühne 主编 |
| colleague | Walter Kreiser | 无向 | Abteilung M 报道作者，1931 同案被判叛国罪 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：冷峻、坚忍、悲剧
- **配色**：深海军蓝（冷静与压迫下的尊严，manifest 预分配 `#14324F`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgePen` 新闻揭露 — 玫瑰 `#C4204F`
  - `badgeTrial` 审判 — 琥珀 `#E07B30`
  - `badgeCamp` 狱中岁月 — 靛蓝 `#4C5FD5`
  - `badgeNobel` 狱中获奖 — 青绿 `#0E7C7B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以「窗格分割的光斑」呼应狱中母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 共享封面）
01  封面 — 狱中的和平奖得主 / Carl von Ossietzky 1889–1938 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、国籍、职业、家庭、荣誉、核心领域）
03  核心事业概览 — 和平主义 / 新闻揭露 / 审判 / 狱中获奖
04  早年：汉堡岁月 (1889–1913) — 丧父、双亲宗教分野、未完成的 Realschule、von 姓氏传说
05  和平主义的起点 (1913–1919) — 结婚、一战被征入伍的震撼、1919 和平会社秘书
06  Die Weltbühne 与无家左派 (1920s) — 接替 Tucholsky、魏玛司法双重标准批判
07  Abteilung M 事件（核心页）— 1929 报道、秘密重整军备、Lipetsk 训练
08  审判与大赦 (1931–1932) — 叛国与间谍罪、18 个月、圣诞大赦
09  纳粹上台与集中营 (1933–1935) — 国会纵火案被捕、Spandau、Esterwegen
10  狱中的诺贝尔奖（核心页）— 1935 年度 1936 颁发、禁行、领奖声明引文、委员会两人辞职与国王缺席
11  家人 — Maud 与 Rosalinde、档案捐赠
12  遗产 — 1974 奥尔登堡大学冠名、1992 联邦法院裁定、Carl von Ossietzky 奖章与 Oldenburg / PEN Norway 各奖
13  遗产：言论自由的代价
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照物理学家标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆 tex 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Ossietzky 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 政治敏感红线 | 纳粹迫害史实按 page.md 客观记录（日期、罪名、监禁地点、禁令），**不加任何评价性语句**；Legacy 一节的当代政治比较（刘晓波、Snowden 等）**禁写** |
| 奖年口径 | 1935 年度和平奖于 **1936 年**颁发；正文统一「1935 诺贝尔和平奖（1936 年颁发）」 |
| 领奖声明 | page.md 载声明英文原文，可入引文框；Göring 劝其拒领是叙述背景 |
| 奖礼风波 | 委员会两名成员因政府职务辞职、挪威国王 Haakon VII 缺席——客观并列，勿加渲染 |
| 引文取舍 | Reichsbanner 1924 长引文与 1932 反犹主义长引文均 page.md 载原文，至多择一段入引文框，篇幅告警即删 |
| 名录石碑 | Legacy 称奖章 1963 年始颁、Awards 节称 since 1962——采用 Awards 节 since 1962 口径并加注 |
| 家庭细节 | 妻 Maud 的头衔拼写为 Maud Lichfield-Woods（婚后 Maud von Ossietzky）；岳家背景仅写 page.md 三要素 |
| 无载禁写 | 无大学教育；Tucholsky 只有「接任主编」一载，勿编两人交情；与 Red Cross 代表 1935 探视是转述见闻非关系 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Die Weltbühne | 《世界舞台》 | 杂志名保留斜体 |
| German rearmament | 德国重整军备 | 秘密/违反凡尔赛条约语境 |
| Treaty of Versailles | 凡尔赛条约 | 背景条约 |
| treason and espionage | 叛国罪与间谍罪 | 1931 罪名 |
| protective custody | 保护性监禁 | 纳粹用语，加引号 |
| concentration camp | 集中营 | Esterwegen 具名 |
| pacifism | 和平主义 | 核心词 |
| Black Reichswehr | 黑色国防军 | 秘密部队 |
| Feme murders | 秘密处决（Feme 谋杀） | 史实名词 |
| Reichsbanner Schwarz-Rot-Gold | 黑红金国旗队 | 社民党准军事组织 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Cinematic Experience** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 电影感 / 沉重 / 悲怆
- **匹配理由**:
  - 「电影感」匹配其命运的戏剧结构——揭露、审判、铁窗、获奖、死亡五个幕次
  - 「沉重」匹配集中营岁月与肺结核晚景的悲剧底色
- **本地路径**: `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐视频长度

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Carl_von_Ossietzky/page.md` | 本地 Wikipedia 正文（唯一事实源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Carl_von_Ossietzky.yaml` | 入库数据（fields/relations 与本文件一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
