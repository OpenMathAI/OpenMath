# 和平奖得主立传提示词（OpenPeace：Alfonso García Robles / 阿方索·加西亚·罗夫莱斯）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Alfonso García Robles（1982 诺贝尔和平奖，《特拉特洛尔科条约》推动者）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth G. Wilson 提示词 + Beamer 立传骨架；和平奖侧沿用「身份信息页 + 领域结构化」骨架。
- **本实例**：Alfonso García Robles（1911-03-20 ~ 1991-09-02，享年 80 岁）。
- **设计哲学**：本篇页面篇幅短（Wikipedia 正文仅一节），立传主线收束为**一部条约**——《特拉特洛尔科条约》建立拉美与加勒比无核武器区；以「法律人的耐心外交」为叙事骨架，克制、不铺陈。

---

## 二、背景信息 【人物专属】

- **目标人物**：Alfonso García Robles（1911-03-20 生于米却肯州萨莫拉 ~ 1991-09-02 逝于墨西哥城，享年 80 岁）
- **官方获奖理由**（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写；与 Alva Myrdal 共享同句）：
  > 英文原文（nobel_peace_citations.json，清理引注噪声后）："for their work for disarmament and nuclear and weapon-free zones."
  > 中译：表彰他们在裁军以及无核武器区与无武器区方面的工作
- **气质关键词**：**无核武器区的总工程师、外交席上的法律人、耐心的多边主义者**。
- **设计母题**：**空白的核弹剪影（treaty cartography）**——拉美地图上被条约「抹去」的核武意象；视觉母题取「条约文本的墨线 + 拉美地图轮廓」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Alfonso_García_Robles/page.md`（Wikipedia 全文 + frontmatter，QID Q203843）。
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 和平奖项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（已核对 page.md，禁止杜撰） 【人物专属】

- 生卒：1911-03-20 生于米却肯州萨莫拉（Zamora, Michoacán）～ 1991-09-02 逝于墨西哥城，享年 80 岁。
- 国籍：墨西哥（名录口径）。
- 家庭：妻子姓名页面无载（仅载「其遗孀 2005 年去世，享年 83 岁」）——**禁写姓名、禁建 spouse 关系**。
- 教育：墨西哥国立自治大学（UNAM）法学士（LLB）；1936 巴黎高等国际研究院（IHEI）；1938 海牙国际法学院；1939 加入墨西哥外事系统。
- 任职/外交履历：
  1. 1945 旧金山会议（联合国成立大会）墨西哥代表团代表。
  2. 1962–1964 驻巴西大使。
  3. 1964–1970 外交部国务秘书（state secretary）。
  4. 1971–1975 驻联合国代表（Permanent Representative）；infobox 口径驻 UN 代表 1970-12-14 就任至 1976-01-01；1975-12-29 至 1976-11-30 任外交部长（Secretary of Foreign Affairs，Echeverría 总统任内）。
  5. 卸任外长后出任墨西哥驻联合国裁军委员会常任代表。
- 关键荣誉：**Nobel Peace Prize 1982**（与 Alva Myrdal 共享）；1972 入选墨西哥学院（Colegio Nacional）；南十字勋章指挥官级（巴西）、阿兹特克雄鹰勋章大十字（墨西哥）、秘鲁太阳勋章大十字；2003 名字镌刻于圣拉萨罗立法宫荣誉墙（众议院所在地）。
- 核心事业清单：
  1. **《特拉特洛尔科条约》**（Treaty of Tlatelolco）：建立拉美与加勒比无核武器区，1967 年区域多数国家签署（部分国家批准较迟）——诺奖即表彰其为此条约的推动力。
  2. 1945 参与创建联合国的旧金山会议。
  3. 联合国裁军委员会的多边裁军外交。
- 关键时间线（14 节点）：1911 生于萨莫拉 → UNAM 法学士 → 1936 巴黎 IHEI → 1938 海牙国际法学院 → 1939 入外事系统 → 1945 旧金山会议 → 1962–64 驻巴西大使 → 1964–70 外交部国务秘书 → 1967《特拉特洛尔科条约》签署 → 1970/71–75/76 驻联合国代表 → 1972 入选墨西哥学院 → 1975–76 外交部长 → 卸任后任驻联合国裁军委员会常任代表 → 1982 诺贝尔和平奖 → 1991-09-02 逝于墨西哥城（2003 荣誉墙）。
- 可用引语：页面无直接引语——**全文禁用引语，一律转述**。

### 第 4 步：事业领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | disarmament | 裁军 | 驻联合国裁军委员会常任代表，1982 诺奖核心 | 核心页 |
| 1 | nuclear-weapon-free zones | 无核武器区 | 《特拉特洛尔科条约》：拉美与加勒比无核区 | 核心页 |
| 2 | international law | 国际法 | UNAM 法学 + 海牙国际法学院 + 法学家身份 | 早年页 |
| 3 | diplomacy | 外交 | 1939 入外事系统，历任大使/外长 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alva Myrdal | 无向 | 1982 诺贝尔和平奖共同得主 |
| colleague | Luis Echeverría | 无向 | 任职于其总统任内（驻联合国代表 1970/71-75 与外长 1975-76） |

> 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Alfonso_García_Robles.yaml`；校验 has_social_data=1、fields=4、relations=2。
> **note**：page.md 篇幅短、个人化关系少，relations=2 为诚实值（配偶无名禁写，无导师/学生有载）；此为工作流允许的例外，验证以 fields≥4、relations≥2 达标。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：`#0E4D64`（manifest 预分配，深青蓝——条约文本的墨色与加勒比海），勿改。
- **辅助**：诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 裁军 — 深青 `#0E4D64`
  - `badgeB` 无核区 — 青绿 `#1B6B5A`
  - `badgeC` 国际法 — 暖金 `#C9A227`
  - `badgeD` 多边外交 — 蓝灰 `#2F4F4F`
- **背景母题**：地图轮廓线（低透明度的拉美大陆弧线 + 条约签署线的细金线）。

### 第 6 步：规划幻灯片序列（12 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 无核武器区的总工程师 / Alfonso García Robles 1911–1991 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/教育/任职/荣誉/核心事业）
03  核心事业概览 — 特拉特洛尔科条约 / 联合国旧金山会议 / 裁军委员会
04  早年：萨莫拉的法律学生 (1911–1939) — UNAM 法学士、巴黎 IHEI、海牙国际法学院
05  旧金山会议 (1945) — 参与创建联合国
06  外交阶梯 (1962–1970) — 驻巴西大使、外交部国务秘书
07  特拉特洛尔科条约 (1967)（核心贡献页）— 拉美与加勒比无核武器区、1967 签署
08  纽约与日内瓦 (1971–1976) — 驻联合国代表、外长、裁军委员会常任代表
09  1982 诺贝尔和平奖（核心页）— 与 Alva Myrdal 共享
10  荣誉与认可 — Colegio Nacional 1972 · 三国大十字 · 2003 立法宫荣誉墙
11  遗产：从特拉特洛尔科到今天的无核区
12  结尾
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 共享奖口径 | 1982 与 Alva Myrdal 共享，理由同一句 "for their work for disarmament and nuclear and weapon-free zones."；与 Myrdal 篇完全一致 |
| 驻 UN 年份张力 | 正文「1971–1975 驻联合国代表」，infobox 表格「1970-12-14 至 1976-01-01」——两个口径并列，立传取正文主线（1971–75）并在脚注/图注注 infobox 口径，勿混写 |
| 外长任期 | 1975-12-29 至 1976-11-30（Echeverría 总统任内），勿写成 1975–1977 |
| 条约批准 | 1967 年区域多数国家签署、部分国家批准较迟——勿写「1967 全部批准」 |
| 妻子禁写 | 妻子姓名页面无载（仅「遗孀 2005 年去世，享年 83」），禁写姓名、禁建 spouse 关系 |
| frontmatter 噪声 | frontmatter field_of_work 误载 "physics"，以正文外交/法学为准，禁写入 fields |
| 无载禁写 | 子女、导师、具体谈判细节、得票过程等页面无载一律不写；全文无直接引语 |
| 荣誉国别 | 南十字勋章=巴西、阿兹特克雄鹰=墨西哥、太阳勋章=秘鲁，三国勿错配 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Treaty of Tlatelolco | 《特拉特洛尔科条约》 | 1967，无核区核心 |
| nuclear-weapon-free zone | 无核武器区 | 理由原文用词 |
| weapon-free zone | 无武器区 | 与无核区并列 |
| San Francisco Conference | 旧金山会议 | 1945 建联合国 |
| Permanent Representative | 常驻代表 | 驻联合国 |
| Committee on Disarmament | 裁军委员会 | 联合国机构 |
| Colegio Nacional | 墨西哥学院 | 1972 入选 |
| Order of the Aztec Eagle | 阿兹特克雄鹰勋章 | 墨西哥 |
| Order of the Southern Cross | 南十字勋章 | 巴西 |
| Order of the Sun of Peru | 秘鲁太阳勋章 | 大十字 |
| Palacio Legislativo de San Lázaro | 圣拉萨罗立法宫 | 2003 荣誉墙 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 行进感 / 稳健 / 远征叙事
- **匹配理由**: 从萨莫拉到旧金山、巴黎、海牙、纽约的外交远征；条约谈判是漫长的行军，行进感曲式正合「总工程师」的一砖一石。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → `presentations/20th_century/Alfonso_García_Robles/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Alfonso_García_Robles/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与官方获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实全部锚定 page.md，无载禁写；全文无直接引语。**

---

## 六、第 1–3 步补充（模板通用） 【模板通用骨架】

### 第 1 步：建立目录

- 在 `peace/presentations/20th_century/` 下创建 `Alfonso_García_Robles/` 与 `images/`（提示词本文件已就位）。

### 第 2 步：复制 Makefile

- 复制同目录已立传成品的 `Makefile`（或标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`），设置 `MAIN=Alfonso_García_Robles_zh`、`VIDEO_NAME=Alfonso_García_Robles_zh`。

### 第 3 步：收集图片 【人物专属】

- **肖像**：`pages/Alfonso_García_Robles/images.txt` 仅有签名图与勋章图，无单人肖像。处理次序：①Wikipedia REST API `page/summary/Alfonso_García_Robles` 查 infobox 1981 年照片原图名，Commons `Special:FilePath/<文件名>?width=600` 下载 500px；②失败则装饰圆占位（主色描边）。curl 加 `-A "Mozilla/5.0"`，`file` 验证。
- **插图备选**：勋章图（秘鲁太阳勋章 Grand Cross BAR png）可作荣誉页小图；《特拉特洛尔科条约》文本/签署页无图，用文字版式，勿外抓。
- 404/HTML 时换文件名或用 REST API 回退。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；装饰圆占位时同样位置与尺寸。
2. **封面有国籍**：顶部副标题或底部状态栏明示 Mexico；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心事业之前；左头像 + 右信息网格，至少含生卒/国籍/教育/任职/主要荣誉/核心事业（含外长与驻 UN 代表年份），事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`；共享封面 `\input` 继承，子 deck 不重复。

---

## 七、执行清单（Checklist） 【模板通用】

1. 通读 `pages/Alfonso_García_Robles/page.md` 全文（本文件第 0 步已核对，本篇仅 65 行，须逐行精读）。
2. 建目录 + 复制 Makefile + 下载肖像（`file` 验证）。
3. 复制 BGM：`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 目录内 `Expedition.wav`。
4. 按 §4 领域表 + §4.5 关系表核对已入库 DB 字段（fields=4 / relations=2，勿加戏）。
5. 编写 Beamer 源码（每页 `\newcommand{\xxxslide}`，骨架参照标杆成品 tex）。
6. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt；每写完一页即 make + `pdftoppm` 目检。
7. 页数对账：按 §6 规划逐帧核对；本篇素材少，可用条约签署国地图式文字版式充实版面，但**不增无载事实**。
8. 引语红线：本篇无任何直接引语，全部转述。
9. 陷阱表逐条自查（驻 UN 年份张力、妻子禁写、frontmatter physics 噪声）。
10. `make images && make video` 出片后，提示词回写 Review 备注（肖像来源/事实修正）。
