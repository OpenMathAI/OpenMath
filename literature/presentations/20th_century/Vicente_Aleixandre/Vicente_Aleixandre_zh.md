# 文学家立传提示词（OpenLiterature 实例：Vicente Aleixandre）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Vicente Aleixandre（1977 诺贝尔文学奖，西班牙二七年一代超现实主义诗人）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按文学家适配：无公式框——以名句引文框、代表作书影、意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Vicente Pío Marcelino Cirilo Aleixandre y Merlo（维森特·阿莱克桑德雷），西班牙诗人，二七年一代成员，1977 诺贝尔文学奖得主。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」骨架；本篇以「照亮宇宙中的境况」为设计母题——大地与海洋的象征、爱与毁灭的张力，对应其从纯诗到超现实主义再到「天堂之影」的诗学三阶段。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Vicente Aleixandre（1898-04-26 ~ 1984-12-14，享年 86 岁）
- **气质关键词**：**二七年一代巨匠、超现实主义诗人、西班牙诗歌两战革新者** —— 1977 诺贝尔文学奖获奖理由：
  > "for a creative poetic writing, which illuminates man's condition in the cosmos and in present-day society, at the same time representing the great renewal of the traditions of Spanish poetry between the wars"（表彰其创造性的诗歌写作，照亮了人在宇宙与当代社会中的境况，同时代表了两战之间西班牙诗歌的伟大革新）
- **设计母题**：**大地与海（earth and sea）**。其早期诗以象征大地与海洋的意象礼赞自然之美——将「毁灭或爱」的自然力意象贯穿全篇视觉语言。
- **本地数据源**：`literature/presentations/pages/20th_century/Vicente_Aleixandre/page.md`（Wikipedia 全文 + frontmatter）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Vicente_Aleixandre
- **肖像**：第 0 步待下载（Wikipedia infobox 1977 年照；404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，以正文为准）

- 生卒：1898-04-26 生于塞维利亚（Seville）~ 1984-12-14 逝于马德里，享年 86 岁
- 全名 Vicente Pío Marcelino Cirilo Aleixandre y Merlo
- 教育：马德里大学（Complutense）法学；frontmatter educated_at 载 Residencia de Estudiantes（二七年一代的摇篮）
- 职业面向：poet / writer / teacher（frontmatter）；1944 年后转向友爱、温情与精神统一主题
- 私生活：双性恋为其朋友圈内周知但终身未公开承认；与诗人 Carlos Bousoño 有长期恋情（page.md 明载）
- 流派：Generation of '27（二七年一代）；早期多自由体诗、高度超现实主义
- 与 Cernuda、Lorca 并称西班牙文学最伟大诗人之列（page.md 明载 alongside）
- 1950-01-22 当选西班牙皇家语言学院（Real Academia Española）O 席，至 1984 年去世
- 荣誉：Nobel 1977、National Prizes for Literature、Premio de la Crítica Española（两度）、Charles III 大十字勋章、Concurso Nacional de Literatura
- 核心作品：《Ámbito》(1928)、《Espadas como labios / Swords like Lips》(1932)、《La destrucción o el amor / Destruction or Love》(1933/1935)、《Pasión de la tierra / Passion of the Earth》(1935)、《Sombra del paraíso / Shadow of Paradise》(1944)、《Historia del corazón / History of the Heart》(1954)、《En un vasto dominio / In a Vast Dominion》(1962)
- 西班牙内战期间为共和派文化杂志《El Mono Azul》撰稿人
- 译介：Lewis Hyde 译《Twenty Poems》(1977)、《A Longing for the Light》(1979)
- 关键时间线（13 节点）：1898 塞维利亚出生 → 1924–1927 写《Ámbito》→ 1928 首部诗集出版（马拉加）→ 1928–1932 诗风剧变转向超现实主义 → 1932 《Espadas como labios》→ 1933 《La destrucción o el amor》→ 1935 《Pasión de la tierra》→ 内战期间为《El Mono Azul》撰稿 → 1944 《Sombra del paraíso》主题转向 → 1950 入选皇家语言学院 O 席 → 1954 《Historia del corazón》→ 1962 《En un vasto dominio》→ 1977 诺贝尔奖 → 1984 马德里去世

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Vicente_Aleixandre/` 与 `images/`

### 第 2 步：复制 Makefile

- 复制同世纪已立传者目录的 Makefile，设置 `MAIN=Vicente_Aleixandre_zh`、`VIDEO_NAME=Vicente_Aleixandre_zh`

### 第 3 步：收集图片

- 肖像下载（curl -A "Mozilla/5.0" + file 验证）；404 则装饰圆占位；另备《La destrucción o el amor》书影

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | surrealist poetry | 超现实主义诗歌 | 1928–1932 剧变后主航道；愿景式意象与自由体 | 核心页 |
| 1 | Generation of '27 | 二七年一代 | 西班牙白银时代诗歌群体 | 流派页 |
| 2 | free verse | 自由诗 | 早期诗主要体式 | 体式页 |
| 3 | love poetry | 爱情诗 | 爱是不可驾驭的自然力，批判社会驯化 | 主题页 |
| 4 | prose poetry | 散文诗 | 《Pasión de la tierra》(1935) | 体式页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Juan Ramón Jiménez | 无向 | 《Ámbito》时期 art for art's sake 美学的先声（1956 诺奖得主） |
| influence | Jorge Guillén | 无向 | 《Ámbito》时期纯粹诗美学的先声（二七年一代） |
| influence | Arthur Rimbaud | 无向 | 超现实主义转向的主要灵感来源（page.md 明载 especially） |
| influence | Lautréamont | 无向 | 超现实主义转向的主要灵感来源（page.md 明载 especially） |
| influence | Sigmund Freud | 无向 | 弗洛伊德精神分析启发其超现实主义诗学 |
| colleague | Federico García Lorca | 无向 | page.md 并称西班牙文学最伟大诗人之列（二七年一代） |
| colleague | Luis Cernuda | 无向 | page.md 并称西班牙文学最伟大诗人之列；Cernuda 赞语 Your verse is like nothing else |
| colleague | Carlos Bousoño | 无向 | 诗人，长期伴侣（page.md 明载 long-term love relationship） |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：地中海的深蓝、爱与毁灭的暗红、塞维利亚的暖土
- **主色**：深海军蓝 `#16324F`（预分配）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeSurreal` 超现实 — 靛蓝 `#4C5FD5`
  - `badgeGen27` 二七一代 — 青绿 `#0E7C7B`
  - `badgeLove` 爱与毁灭 — 玫瑰 `#C4204F`
  - `badgeEarth` 大地与海 — 琥珀 `#E07B30`
- **背景母题**：海浪线与大地色块的水平分层，偶见倒置明喻的镜像图形（呼应其「倒置明喻」修辞发明）

### 第 6 步：规划幻灯片序列（12–14 页）

```
00  OpenLiterature 项目首页（\input cover 共享页）
01  封面 — 照亮人在宇宙中的境况 / Vicente Aleixandre 1898–1984 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、全名、国籍、出生地、学院席位、流派、核心领域）
03  文学世界概览 — 超现实主义 / 二七一代 / 爱情诗 / 散文诗
04  塞维利亚与马德里（1898–1924）— 法学教育、Residencia de Estudiantes 氛围
05  纯诗起点：《Ámbito》（1928）— Jiménez 与 Guillén 的美学先声
06  剧变：走向超现实（1928–1935）— Rimbaud/Lautréamont/Freud、倒置明喻、散文诗
07  《毁灭或爱》（1933）— 爱作为不可驾驭的自然力
08  内战与《El Mono Azul》（1936–1939）— 共和派文化杂志撰稿人（客观简述）
09  《天堂之影》（1944）— 主题转向友爱与精神统一
10  成熟与学院（1950–1962）— 皇家语言学院 O 席、《Historia del corazón》《En un vasto dominio》
11  1977 诺贝尔奖 — 官方获奖理由原句引文框
12  遗产 — 马德里主广场纪念像、邮票、瑞典电视台纪录片
13  结尾
```

### 第 7 步：编写 Beamer 源码

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide`。
- 名句引文框：获奖理由英文原句（page.md 明载）+ Cernuda 赞语 "Your verse is like nothing else"（page.md 明载英文原文）。

### 第 8 步：布局检查

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删装饰 → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查

**Aleixandre 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 书名年份 | 《La destrucción o el amor》正文表述有 1933 与 1935 两处（英文小节作 1933、总介作 1935）——两说并写加注，勿擅自择一 |
| 超现实主义灵感 | Rimbaud 与 Lautréamont 是「surrealism 的先驱（especially）」+ Freud——三人并列引用，勿漏 Freud |
| 私生活 | 双性恋与 Bousoño 长期恋情为 page.md 明载事实——客观一句带过，不展开叙事、不作评价 |
| 内战经历 | 仅《El Mono Azul》撰稿人一事，客观简述，不作政治叙事 |
| 名字 | 全名四段式（Pío Marcelino Cirilo），标题与正文统一用 Vicente Aleixandre，勿写 Vicente Alejandro |
| 与 Jiménez 关系 | 是《Ámbito》时期「美学先声」式影响，非师承——勿写师生 |
| 与 Lorca/Cernuda | 仅「并称伟大」与引语，无师承/共同作品记载，用 colleague |
| 无载禁写 | page.md 无其诺奖演说内容、无与 Machado 交往、无战后流亡记载（他留在西班牙）——一律不写 |
| 术语 | Real Academia Española 译「西班牙皇家语言学院」（通行），勿写「皇家科学院」 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Generation of '27 | 二七年一代 | 纪念贡戈拉逝世三百周年得名 |
| La destrucción o el amor | 《毁灭或爱》 | 通行译名 |
| Sombra del paraíso | 《天堂之影》 | 通行译名 |
| inverted simile | 倒置明喻 | 其修辞发明之一（Swords like Lips） |
| equivalent disjunctive nexus | 等价析取连接 | 其修辞发明之一（Destruction or Love） |
| El Mono Azul | 《蓝罩衫》 | 共和派文化杂志 |
| ultraism | 极端主义 | 西班牙语先锋诗运动 |
| Seat O | O 席 | 皇家语言学院席位编号 |

---

## 四、背景音乐选择

- **选定曲目**: **Nostalgia** — Alex-Productions（80k views）
- **风格**: 高受众 / 怀旧 / 温和
- **匹配理由**:
  - "怀旧/温和" 匹配其诗中挥之不去的忧郁气质——逝去的爱、失落的激情与自然的自由精神
  - 匹配「两战之间西班牙诗歌」的历史纵深——白银时代的回声与内战前后的挽歌
  - 与批内其他曲目错开（New Lands 史诗 / Timeless 沉稳 / PAST 历史感 / Awaken 明亮）
- **备选**（未采用）: The Flow of Time（时间感，偏纪录片叙事）、Lonesome（孤独感可备选，受众更低）
- **时长**: 需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐
