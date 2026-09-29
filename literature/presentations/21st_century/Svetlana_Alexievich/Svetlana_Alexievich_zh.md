# 文学家立传提示词（OpenLiterature 21 世纪批次：Svetlana Alexievich）

> **本文件是 Svetlana Alexievich（2015 诺贝尔文学奖）的人物专属立传提示词**，供后续 Beamer 立传 agent 直接复制到新对话中按步执行。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（内容适配文学家）。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 旗下，与 mathematician/physicist/chemist 侧同构）。
- **本实例**：Svetlana Alexandrovna Alexievich（斯韦特兰娜·阿列克西耶维奇），白俄罗斯调查记者与纪实作家，2015 诺贝尔文学奖得主——首位获此奖的白俄罗斯作家，也常被称为首位获奖记者。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」两大骨架；文学家无公式框——用**名句引文框 / 代表作书影 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Svetlana Alexandrovna Alexievich（1948-05-31 生于乌克兰苏维埃社会主义共和国斯坦尼斯拉夫（今 Ivano-Frankivsk），在世）
- **官方获奖理由**（2015，Wikipedia 原文照录，禁止改写）：
  > "for her polyphonic writings, a monument to suffering and courage in our time"（中译照录 `generate_21st_century_list.py` CITATION_ZH：表彰其复调式写作，是我们时代苦难与勇气的纪念碑）
- **气质关键词**：**复调之声、口述历史的拼贴者、乌托邦的记录者** —— 以数百普通人的独白拼出苏联与后苏联个体的情感史。
- **设计母题**：**众声合唱（a chorus of individual voices）**。其书是「个体声音的合唱 + 日常细节的拼贴」——视觉语言取「多条声波纹样/引语条块拼贴」：以红与暗色的条带层叠，呼应复调式写作。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Svetlana_Alexievich/page.md`（Wikipedia 全文 + frontmatter）
  - `literature/presentations/pages/21st_century/Svetlana_Alexievich/metadata.json`、`images.txt`
  - Wikipedia URL: https://en.wikipedia.org/wiki/Svetlana_Alexievich （肖像：infobox「Alexievich in 2024」或 2013 照，第 0 步待下载）

---

## 三、任务流程 【逐步执行】

> 数据库同步要求：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 greatminds 库（MySQL），yaml 路径 `MySQL/data/Svetlana_Alexievich.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已下载（事实基准如下，第一轮已核对）
- 肖像待下载：infobox 照片（Alexievich in 2024）
- **事实基准**：
  - 生年：1948-05-31 生于乌克兰西部的斯坦尼斯拉夫（1962 年起名 Ivano-Frankivsk）；白俄罗斯父亲与乌克兰母亲均为教师，父兼任村小校长；幼年在乌克兰，后举家迁白俄罗斯
  - 国籍：白俄罗斯（生于苏联，frontmatter 两说并列）
  - 语言：俄语写作（兼通白俄罗斯语）
  - 教育：高中毕业后任地方报纸记者 → 1972 白俄罗斯国立大学新闻系毕业 → 1976 明斯克《Nyoman》文学杂志记者
  - 首部书稿 "I left the village"（我离开了村庄）被苏联审查机关封禁
  - 关键荣誉：荣誉勋章 1984 · 列宁共青团奖 1986 · Tucholsky 奖 1996 · 莱比锡欧洲理解图书奖 1998 · 赫尔德奖 1999 · 美国书评人协会奖 2005 · 德国书业和平奖 2013 · 美第奇评论奖 2013 · 萨哈罗夫奖 2020 · 松宁奖 2021 · Nobel 2015 等
  - 婚姻子女：page.md 无载——禁写
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列展开）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Svetlana_Alexievich/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已完成人物目录的 Makefile，设置 `MAIN=Svetlana_Alexievich_zh`、`VIDEO_NAME=Svetlana_Alexievich_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：infobox 照片（curl -A "Mozilla/5.0"，500px）；404 则用 images.txt 兜底（另有 2013 年 Commons 照可试），再不行用装饰圆占位
- 可选插图：《Voices from Chernobyl》/《Secondhand Time》书影或声波纹样意象

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | oral history | 口述历史 | 数百受访者独白构成其书的基本材料 | 方法页 |
| 1 | documentary literature | 纪实文学 | 其体裁的通行称谓（本人不认可是新闻） | 风格页 |
| 2 | polyphonic writing | 复调书写 | 诺奖理由核心词，个体声音的合唱 | 核心页 |
| 3 | literary reportage | 报告文学 | 获 Kapuściński reportage 奖的口径 | 作品页 |
| 4 | investigative journalism | 调查新闻 | 其记者出身与调查方法 | 早年页 |

- 入库：`fields` 写入 `person_field`（带 rank）；缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> 只收 page.md 明载关系；yaml 与本表完全一致。本人婚姻子女 page.md 无载，禁写。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Ales Adamovich | 无向 | 白俄罗斯作家，见证者证言方法之思想来源，被称其「文学教父」 |
| influence | Vasil Bykaŭ | 无向 | 白俄罗斯作家，本人确认的影响者 |
| influence | Varlam Shalamov | 无向 | 本人视其为 20 世纪最佳作家 |
| influence | Ryszard Kapuściński | 无向 | 本人自述早期影响者（2015 访谈） |
| influence | Hanna Krall | 无向 | 本人自述早期影响者（2015 访谈） |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深红 `#A31621`（战火、牺牲与「苦难与勇气的纪念碑」）
- **诺奖香槟金**：`C9A227`
- 四分类色（badgeA–D）：
  - `badgeA` 复调书写 — 靛蓝 `#4C5FD5`
  - `badgeB` 口述历史 — 青绿 `#0E7C7B`
  - `badgeC` 战争与切尔诺贝利 — 琥珀 `#E07B30`
  - `badgeD` 流亡与自由 — 玫瑰 `#C4204F`
- **背景母题**：声波条带 + 引语纸条拼贴，呼应「众声合唱」母题

### 5.1 文学家格式硬要求 【★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 身份 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心内容之前。左头像 + 右信息网格，含至少：生年、全名、国籍、出生地（乌克兰/白俄罗斯血统）、教育、职业（作家/调查记者/口述历史家）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注 `OpenMathAI`；引号用半角 `" "`；中文引号内不写「原话」，除非 page.md 有英文原文。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 复调之声 / Svetlana Alexievich 1948– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  教师家庭 (1948–1972) — 乌克兰出生、白俄罗斯成长、新闻系毕业、《Nyoman》记者
04  方法之诞生 — 首部书稿遭审查封禁；「实际人声与忏悔、证词与文献」体裁的自白（引文框）
05  战争的无女性面孔 — 1985《War's Unwomanly Face》五年 200 万册；女性与儿童眼中的二战
06  锌皮娃娃兵 — 1989 苏阿战争口述实录；1992–1996 被诉四起（三起驳回一起部分胜诉）客观简述
07  切尔诺贝利的祈祷 — 1997；核灾难题材，NBCC 2005
08  二手时间与「乌托邦之声」 — 2013；苏联与后苏联个体的情感史总纲
09  方法（核心贡献页）— 复调/拼贴/口述；自称「写作、记者、社会学者、心理学者、布道者」五位一体
10  流亡与归返 — 2000 因卢卡申科当局政治迫害离国（巴黎/哥德堡/柏林），2011 回明斯克；客观简述
11  荣誉长廊 — 德国书业和平奖 2013 · 美第奇奖 2013 · Nobel 2015 · 萨哈罗夫奖 2020
12  遗产与结尾 — 首位白俄罗斯诺奖文学作家；「第一位获诺奖的记者」之说与其本人异议
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现参照成品 `\profileslide`。
- 引文框/意象图式替代公式框：page.md 明载英文原话三段可入引文框——方法自白（"I've been searching for a literary method..."）、Boys in Zinc 开篇（"After the great wars..."）、主题自述（"If you look back at the whole of our history..."）——逐字照录勿改。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删装饰元素 → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Alexievich 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 政治红线 | 卢卡申科迫害与流亡（2000–2011）、2020 协调委员会与刑事立案、2014 克里米亚表态、2022 入侵评论、2021 教材除名、2026 引语集被列极端主义材料——**只按 page.md 客观简述一页/一段，不作政治评价、不展开叙事、引语克制使用** |
| 获奖理由口径 | "for her polyphonic writings, a monument to suffering and courage in our time"，勿改写 |
| 「记者」身份 | 被称为首位获诺奖记者，但**本人不认同**其作是新闻——两种口径并写 |
| 姓氏转写 | 亦作 Aleksievich / Aleksiyevich；白俄罗斯语与俄语拼写并存——选定 Alexievich 全篇统一 |
| 作品双英译 | Zinky Boys（UK 1992）/ Boys in Zinc（US 2016）同名异译；Chernobyl Prayer / Voices from Chernobyl 同理——注记版本 |
| Adamovich 定性 | 思想影响者（influence）：见证者证言优于虚构的方法论来源；「文学教父」系 Uladzimir Nyaklyayew 之语，注明转述 |
| 《我来自火焚的村庄》 | Adamovich/Bryl/Kalesnik 合著，被指为影响其文学观的单一最重要的书——叙事呈现，作者不逐个入库 |
| 诉讼事实 | 1992–1996 四名受访者起诉，三起驳回一起部分胜诉——数字勿错，客观陈述 |
| 婚姻子女 | page.md 无载——禁写（勿从其他来源补） |
| 无载禁写 | 具体受访人数、各书页数等 page.md 未载者不写；「200 万册/五年」是明载数字可用 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| polyphonic writings | 复调式写作 | 诺奖理由原词，勿意译「多声部小说」 |
| oral history | 口述历史 | 其方法核心 |
| documentary literature | 纪实文学 | 体裁通行称谓 |
| Zinky Boys / Boys in Zinc | 锌皮娃娃兵 | 英译双版本名 |
| Voices from Chernobyl / Chernobyl Prayer | 切尔诺贝利的祈祷 | 英译双版本名 |
| Secondhand Time | 二手时间 | 2013，副题 The Last of the Soviets |
| Voices of Utopia | 乌托邦之声 | 其全部作品的统称项目 |
| historian of the untraceable | 无迹可寻者的历史学家 | 其自称 |
| censors / censorship | 审查 | 首部书稿被封禁等，客观措辞 |
| Coordination Council | 协调委员会 | 2020 事件客观简述用，不展开 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（152k views，高受众 / 史诗 / 开阔）
- **匹配理由**:
  - 「史诗/开阔」匹配其题材体量 —— 从二战、阿富汗战争到切尔诺贝利与苏联解体，是帝国兴衰的口述总史
  - 「高受众」配「纪念碑」气质 —— 诺奖理由的 monument 一词需要开阔庄重的声音底座
  - 流亡与重归的叙事弧线与「新大陆」的迁徙意象暗合（巴黎—哥德堡—柏林—明斯克）
- **备选**（未采用）：★★ Tragedy（深色/戏剧性，同批已用于 Tranströmer；且本篇更重「证言的公共性」而非个人悲剧）
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → 复制到本目录 `NewLands.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Svetlana_Alexievich/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `literature/generate_21st_century_list.py` | 获奖理由中译（CITATION_ZH）对照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
