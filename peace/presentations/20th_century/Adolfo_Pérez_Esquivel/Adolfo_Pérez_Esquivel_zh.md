# 和平奖得主立传提示词（OpenPeace：Adolfo Pérez Esquivel / 阿道弗·佩雷斯·埃斯基维尔）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Adolfo Pérez Esquivel（1980 诺贝尔和平奖，拉美人权与非暴力运动者）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth G. Wilson 提示词 + Beamer 立传骨架；和平奖侧沿用「身份信息页 + 领域结构化」骨架。
- **本实例**：Adolfo Pérez Esquivel（阿道弗·佩雷斯·埃斯基维尔，1931-11-26 生，在世）。
- **设计哲学**：和平奖得主立传与科学家立传的核心差异，在于「事业领域」以**抗争方式与行动网络**呈现（艺术家出身的非暴力组织者），必须保留「身份信息页」；本篇以「从雕塑家到 SERPAJ 协调人」的转向为主线。

---

## 二、背景信息 【人物专属】

- **目标人物**：Adolfo Pérez Esquivel（1931-11-26 生于布宜诺斯艾利斯，在世，2022 年 1 月曾因中风住院）
- **官方获奖理由**（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > 英文原文（nobel_peace_citations.json，清理引注噪声后）："for being a source of inspiration to repressed people, especially in Latin America."
  > 中译：表彰他成为受压迫民众（尤其是拉丁美洲民众）的精神源泉
- **气质关键词**：**雕塑家出身的非暴力组织者、失踪者家庭的同行者、拉美良知的支点**。
- **设计母题**：**石头与握手（sculpted hands）**——他用手造碑纪念难民、用石头刻拉美受难十四处苦路；视觉母题取「青铜/石材的浮雕质感」与伸出的手。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Adolfo_Pérez_Esquivel/page.md`（Wikipedia 全文 + frontmatter，QID Q206505）。
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 和平奖项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（已核对 page.md，禁止杜撰） 【人物专属】

- 生卒：1931-11-26 生于阿根廷布宜诺斯艾利斯，在世（frontmatter 无 date_of_death；2022-01 中风住院有载，仅作事实记录）。
- 国籍：阿根廷。父为西班牙加利西亚 Poio 移民阿根廷的渔夫；母在他 3 岁时去世，家境贫寒。
- 家庭：妻 Amanda（仅见 page.md 注释：1980-11-17 为其致信 IFOR Hildegard Goss-Mayr）；其余家庭细节页面无载，禁写。
- 教育：Manuel Belgrano 美术学校 + 拉普拉塔国立大学（National University of La Plata），受训为画家与雕塑家。
- 任职：被聘为建筑学教授，从小学到大学各层次任教共 25 年；1974 辞去教职，出任拉美基层社群网络（以非暴力促进穷人解放）总协调人；1998 获聘布宜诺斯艾利斯大学「和平与人权研究教授」，现为该校社科学院常驻讲师，主持「和平与人权文化」研讨班。
- 组织：1974 共同创立 NGO **Servicio Paz y Justicia**（SERPAJ，和平与正义服务社）并任总协调人；SERPAJ 是国际和解 fellowship（IFOR）成员，IFOR 自始支持其工作；后任拉美和平与正义基金会荣誉理事会主席、国际人权与民族解放联盟（米兰）主席、常设人民法庭成员。
- 被捕记录：1975 被巴西军警拘押；1976 在厄瓜多尔与拉美及北美主教一同入狱；1977 在布宜诺斯艾利斯被阿根廷联邦警察拘押、受酷刑、未经审判关押 14 个月（其间获 Pope John XXIII Peace Memorial）。
- 关键荣誉：**Nobel Peace Prize 1980**（1980-12-10 领奖，由 1976 年得主 Mairead Corrigan 与 Betty Williams 提名；「以我最贫穷最小的兄弟姐妹的名义」领奖并将奖金捐给慈善）；Pacem in Terris Award 1999；圣马科斯国立大学荣誉博士、加泰罗尼亚议会荣誉勋章（frontmatter）。
- 核心事业清单：
  1. 1970 年代起投身拉美基层基督教和平主义（Christian pacifist）团体网络。
  2. 1974 共创 SERPAJ，支持脏战（Dirty War）受害者家属、串联人权组织。
  3. 1980 获奖后继续支持五月广场母亲（Mothers of the Plaza de Mayo），尽管独裁持续骚扰。
  4. 后期投身阿根廷原住民权益、环保运动，反对紧缩政策与美洲自由贸易区。
  5. 2010 反对 Esquel 警方训练少年准军事队伍（其类比须照原文转述，不展开）。
  6. 艺术创作：1992 拉美受难十四处苦路（纪念征服美洲 500 周年）；联合国难民署（UNHCR）日内瓦总部《难民纪念碑》；厄瓜多尔里奥班巴大教堂拉美人民壁画（献给 Proaño 蒙席与原住民）；巴塞罗那甘地广场甘地青铜像。
- 关键时间线（16 节点）：1931 生于布宜诺斯艾利斯 → 幼年丧母 → 就读 Manuel Belgrano 美术学校 → 拉普拉塔国立大学受训画家/雕塑家 → 任建筑学教授 25 年 → 1960s 投身拉美基层基督教和平主义团体 → 1974 辞教职任网络总协调人、共创 SERPAJ → 1975 巴西被拘 → 1976-03 政变、Videla 军政府上台 → 1976 厄瓜多尔入狱 → 1977 布宜诺斯艾利斯被捕，受刑拘押 14 个月 → 1980-12-10 获诺贝尔和平奖 → 持续支持五月广场母亲 → 1995 出版 Caminando Junto al Pueblo → 1998 任 UBA 和平与人权研究教授 → 1999 Pacem in Terris Award / 2010 Esquel 行动 / 2022 中风住院。
- 可用引语（仅限 page.md 载有英文原文者）：领奖辞「in the name of the poorest and smallest of my brothers and sisters」；关于 9/11 的言论（若引用须整句照录并标注为其个人立场，只作事实记录）。

### 第 4 步：事业领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | human rights | 人权 | 1980 诺奖核心，脏战受害者家庭与失踪者 | 核心页 |
| 1 | nonviolent resistance | 非暴力抗争 | 拉美基层基督教和平主义网络 | 核心页 |
| 2 | peace activism | 和平运动 | SERPAJ 总协调人、和平与人权教授 | 核心页 |
| 3 | community organizing | 基层社群组织 | 串联拉美社群网络与教会资源 | 核心页 |
| 4 | monumental sculpture | 纪念性雕塑 | 难民纪念碑、甘地像、苦路组雕 | 艺术页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Servicio Paz y Justicia | 创始人→机构 | 1974 共同创立并任总协调人 |
| colleague | Mairead Corrigan | 无向 | 1976 和平奖得主，1980 提名人 |
| colleague | Betty Williams | 无向 | 1976 和平奖得主，1980 提名人 |
| influence | Hildegard Goss-Mayr | 无向 | IFOR 巡回秘书，其妻信中称其为本人的第一位老师 |
| influence | Mahatma Gandhi | 无向 | 曾为巴塞罗那甘地广场塑铜像致敬 |
| controversy | Jorge Videla | 无向 | 1976 政变军政府，本人受刑拘押 14 个月 |
| spouse | Amanda | 无向 | 妻子，1980 致信 IFOR 详述非暴力启蒙 |

> 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Adolfo_Pérez_Esquivel.yaml`；校验 has_social_data=1、fields=5、relations=7。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：`#37474F`（manifest 预分配，蓝灰石色——雕塑的石材与布宜诺斯艾利斯的沉静），勿改。
- **辅助**：诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 人权 — 深红 `#8C2F1B`
  - `badgeB` 非暴力 — 橄榄绿 `#4E6B4E`
  - `badgeC` 和平组织 — 蓝灰 `#37474F`
  - `badgeD` 艺术创作 — 赭金 `#B08A3E`
- **背景母题**：浮雕质感块面（低饱和石纹矩形与圆弧错落，隐喻纪念碑与苦路石雕）。

### 第 6 步：规划幻灯片序列（12 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 受压迫者的精神源泉 / Adolfo Pérez Esquivel 1931– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/教育/组织/荣誉/核心事业）
03  核心事业概览 — SERPAJ / 人权网络 / 原住民与环保 / 艺术纪念碑
04  早年：渔夫之子 (1931–1960s) — 加利西亚移民、丧母、美术学校与拉普拉塔大学
05  从教席到街头 (1960s–1974) — 25 年执教、基督教和平主义网络、1974 辞职
06  SERPAJ 与脏战年代 (1974–1977) — 共创组织、受害者家属、三次拘押与 14 个月监禁
07  1980 诺贝尔和平奖（核心贡献页）— 提名人、领奖辞、奖金捐献
08  五月广场母亲与后续抗争 — 独裁骚扰下的坚持
09  石头上的和平 — 难民纪念碑、苦路组雕、甘地像
10  荣誉与认可 — Nobel 1980 · Pacem in Terris 1999 · 荣誉博士
11  遗产：拉美非暴力的支点 — UBA 讲席与和平文化研讨班
12  结尾
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 在世者口径 | 生于 1931-11-26，在世；所有「生卒」处写 1931–，勿编卒年；2022 中风住院仅作事实 |
| 国籍口径 | Argentina（名录口径）；父为西班牙加利西亚移民，勿写双国籍 |
| 诺奖理由 | 官方原文 "for being a source of inspiration to repressed people, especially in Latin America."，勿改写 |
| 提名人 | 1976 得主 Mairead Corrigan 与 Betty Williams 联名提名，勿写成「自荐」或「IFOR 提名」 |
| 组织名 | SERPAJ = Servicio Paz y Justicia（和平与正义服务社），勿与 IFOR 混同——SERPAJ 是 IFOR 成员组织 |
| 政治敏感红线 | 军政府拘押/脏战只作客观事实记录；2010 Esquel 类比、9/11 言论、Maduro 表态、Pope Francis 评语等当代政治内容**只转述事实、不评价、不评论性展开**；建议幻灯片层面直接回避 Maduro/9-11 段落 |
| 妻子姓名 | 仅「Amanda」有名（出自 page.md 注释），无姓氏有载，勿补全 |
| 艺术作品 | 难民纪念碑在 UNHCR 日内瓦总部；甘地青铜像在巴塞罗那甘地广场；勿混淆地点 |
| 无载禁写 | 博士导师、兄弟姐妹、出生地街区等页面无载内容一律不写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Servicio Paz y Justicia (SERPAJ) | 和平与正义服务社 | 勿译「和平正义服务」后漏缩写 |
| Dirty War | 肮脏战争 | 仅作专名客观使用 |
| Mothers of the Plaza de Mayo | 五月广场母亲 | 机构类专名词 |
| International Fellowship of Reconciliation (IFOR) | 国际和解 fellowship | 组织名 |
| Christian pacifism | 基督教和平主义 | 非「和平主义基督教」 |
| non-violence | 非暴力 | 页面连字符拼法 |
| Pacem in Terris Award | 「地上和平」奖 | 拉丁语原名 |
| Via Crucis | 苦路（受难十四处） | 1992 组雕 |
| UNHCR | 联合国难民署 | 纪念碑所在地 |
| Permanent Peoples' Tribunal | 常设人民法庭 | 其成员身份 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 觉醒 / 上扬 / 希望感
- **匹配理由**: 从雕塑家到非暴力组织者的「觉醒」转向、军政府阴影后领奖时刻的上扬、以及「受压迫者的精神源泉」这一定位——希望感曲式正合其鼓舞意象。
- **本地路径**: `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → `presentations/20th_century/Adolfo_Pérez_Esquivel/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Adolfo_Pérez_Esquivel/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与官方获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实全部锚定 page.md，无载禁写；当代政治内容只作客观记录。**

---

## 六、第 1–3 步补充（模板通用） 【模板通用骨架】

### 第 1 步：建立目录

- 在 `peace/presentations/20th_century/` 下创建 `Adolfo_Pérez_Esquivel/` 与 `images/`（提示词本文件已就位）。

### 第 2 步：复制 Makefile

- 复制同目录已立传成品的 `Makefile`（或标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`），设置 `MAIN=Adolfo_Pérez_Esquivel_zh`、`VIDEO_NAME=Adolfo_Pérez_Esquivel_zh`。

### 第 3 步：收集图片 【人物专属】

- **肖像**：✅ `pages/Adolfo_Pérez_Esquivel/images.txt` 第 2 条即 1983 年单人照 `Adolfo_Pérez_Esquivel_1983.jpg`，直接下载 500px 使用；curl 加 `-A "Mozilla/5.0"`，`file` 验证。
- **插图备选**：签名图（Firma Pérez Esquivel，可用作身份页装饰）；艺术作品页若需插画（难民纪念碑/甘地像），images.txt 无载则用文字版式，勿从他处抓图。
- 404/HTML 时换文件名或用 Wikipedia REST API `page/summary` 回退；仍失败则装饰圆占位。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示 Argentina；底部状态栏给出 `国籍 | 组织 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心事业之前；左头像 + 右信息网格，至少含生卒/国籍/教育/组织/任职/主要荣誉/核心事业，事实取自 page.md infobox，不得杜撰；在世者卒年栏写「在世」。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`；共享封面 `\input` 继承，子 deck 不重复。

---

## 七、执行清单（Checklist） 【模板通用】

1. 通读 `pages/Adolfo_Pérez_Esquivel/page.md` 全文（本文件第 0 步已核对，执行时复核即可）。
2. 建目录 + 复制 Makefile + 下载肖像（`file` 验证）。
3. 复制 BGM：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 目录内 `Awaken.wav`。
4. 按 §4 领域表 + §4.5 关系表核对已入库 DB 字段（fields=5 / relations=7，勿改）。
5. 编写 Beamer 源码（每页 `\newcommand{\xxxslide}`，骨架参照标杆成品 tex）。
6. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt；每写完一页即 make + `pdftoppm` 目检。
7. 页数对账：按 §6 规划逐帧核对（缺帧/合并帧都要能对上页数）。
8. 引语逐条核对 §0 白名单；无原文一律转述。
9. 陷阱表逐条自查（尤其在世者口径与当代政治红线）。
10. `make images && make video` 出片后，提示词回写 Review 备注（肖像来源/事实修正）。
