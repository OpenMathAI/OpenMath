# 物理学家立传提示词（人物专属：Guglielmo Marconi）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖批量立传的**人物专属提示词**，结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Guglielmo Marconi（古列尔莫·马可尼），1909 年诺贝尔物理学奖得主（与 Ferdinand Braun 共享），实用无线电报系统的缔造者。
- **设计哲学**：保留物理学家模板两大骨架——「身份信息页」与「研究领域结构化表达」；本人物是工程师/企业家型诺奖得主，叙事重心是**从阁楼实验到跨越大西洋**的距离递进（800 m → 2 km → 5 km → 16 km → 3500 km）。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Guglielmo Giovanni Maria Marconi（1874-04-25 ~ 1937-07-20，享年 63 岁）
- **气质关键词**：**电波的摆渡人、跨越海洋的连接者、无线电工业的奠基者**
- **官方获奖理由（禁止改写，与 Braun 共享）**：
  > "in recognition of their contributions to the development of wireless telegraphy"（表彰他们对无线电极报发展的贡献）
- **设计母题**：**电波跨越地平线（beyond the horizon）**——曲线电波越过直线视距；视觉语言用地弧、同心波纹与海岸线。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Guglielmo_Marconi/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页 `cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⏳ **待下载** `https://en.wikipedia.org/wiki/Guglielmo_Marconi` 到 `{Dir}/Guglielmo_Marconi.html`（本地暂只有 `page.md`）
- **事实基准**：
  - 生卒（1874-04-25 生于博洛尼亚 ~ 1937-07-20 卒于罗马，享年 63；葬于 Sasso Marconi 陵墓）
  - 家庭（父 Giuseppe 为博洛尼亚山地地主；母 Annie Jameson 为 Jameson 爱尔兰威士忌创始人孙女；兄 Alfonso）
  - 教育（**无正规学校教育**，家庭教师授课；Livorno 物理教师 Vincenzo Rosa 为重要导师；18 岁结识博洛尼亚大学物理学教授 Augusto Righi，被允许旁听并使用实验室与图书馆）
  - 任职/身份（1897 创办 The Wireless Telegraph & Signal Company（后 Marconi Company）；1914 任意大利王国参议员；1915 军中中尉→海军军衔→1936 预备役海军少将；1927 意大利国家研究委员会主席；1930-09-19 起任意大利皇家科学院院长直至去世；1929 获世袭侯爵封号；1931 建梵蒂冈电台）
  - 关键荣誉（Nobel 1909；Matteucci Medal 1901；Albert Medal 1914；Franklin Medal 1918；IRE Medal of Honor 1920；John Fritz Medal 1923；John Scott Medal 1931；Wilhelm Exner Medal 1934；英国皇家维多利亚勋章名誉大十字 1914）
  - 婚姻（1905 娶 Beatrice O'Brien，1927-04-27 婚姻废止；1927-06-12 娶 Maria Cristina Bezzi-Scali；子女 5 人）
  - 核心贡献清单：
    1. 实用无线电报系统（1895 单极天线+接地，越丘 2 km）
    2. 第一份无线电波通信专利（英国专利 12039，1896 申请）
    3. 跨海与跨大西洋链路（1897 布里斯托尔海峡 → 1901 Signal Hill，存技术争议）
    4. Marconi 公司与海上无线电影救援体系（1899 首例海上遇险信号、Titanic 世代）
    5. 无线电广播工业先声（1920 Melba、2MT/2LO）
    6. 梵蒂冈电台（1931）与军用无线电台战应用
  - 诺奖演讲（注记）：1909-12-11 *Wireless Telegraphic Communication*
  - 主要会员（注记）：美国哲学学会国际会员 1901、猞猁眼学院 1912、美国 NAS 国际会员 1932、宗座科学院院士 1936
  - 核心时间线（1874 生 → 1894 阁楼实验/风暴警报 → 1895 夏 2 km 越丘（单极天线+接地） → 1896 赴英+专利 12039 → 1897 布里斯托尔海峡跨海 4.8 km → 1898 Kingston Regatta 直播 → 1899 跨英吉利海峡+赴美报美洲杯 → 1899 East Goodwin 灯船首个海上求救信号 → 1901-12-12 纽芬兰收到越洋 S 信号（存技术争议） → 1902 SS Philadelphia 系统测试+磁性检波器 → 1903 罗斯福–爱德华七世跨洋互电 → 1907 Glace Bay–Clifden 商业跨洋业务 → 1909 共享诺奖 → 1912 Titanic 与英国调查听证 → 1914 参议员 → 1920 Melba 广播 → 1922 2MT/2LO → 1923 加入国家法西斯党 → 1927 再婚+NRC 主席 → 1929 侯爵 → 1930 皇家科学院院长 → 1931 梵蒂冈电台 → 1937 卒+全球电台两分钟静默）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下已有 `Guglielmo_Marconi/`（本提示词所在），需新建 `images/` 子目录存放肖像与插图

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Guglielmo_Marconi_zh`、`VIDEO_NAME=Guglielmo_Marconi_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：page.md 内嵌 infobox 像（Marconi in 1908）；优先 Commons `Special:FilePath/Guglielmo Marconi keksintöineen.jpg?width=500`（1897 年与其发明合影）或 infobox 原图
- 备选：portrait 照、1905 年 Vanity Fair 漫画像；再失败用装饰圆占位（主色边框圆 + 姓名缩写）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | wireless telegraphy | 无线电报 | 核心事业，1909 诺奖主题 | 主线页 |
| 1 | radio | 无线电 | 实用无线电系统缔造者 | 核心页 |
| 2 | electrical engineering | 电气工程 | 单极天线、调谐、工程化 | 技术页 |
| 3 | radio broadcasting | 无线电广播 | 1920 Melba、2MT/2LO、BBC 前奏 | 广播页 |

入库：`MySQL/data/Guglielmo_Marconi.yaml`（已备好，`cd MySQL && python3 seed_person.py data/Guglielmo_Marconi.yaml`）。
校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Karl Ferdinand Braun | 无向 | 1909 年诺贝尔物理学奖共享 |
| influence | Heinrich Hertz | 思想来源 | 1888 年电磁波实验是马可尼的物理基础 |
| influence | Augusto Righi | 思想来源 | 允许旁听/用实验室，指点其采用金屑检波器 |
| spouse | Beatrice O'Brien | 无向 | 1905 结婚，1927 废止 |
| spouse | Maria Cristina Bezzi-Scali | 无向 | 1927 结婚 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：开阔、电波、海天之间
- **配色**：电波午夜蓝（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 — 电波午夜蓝 `#16324F`
  - `badgeWireless` 无线电报 — `#2A9D8F`
  - `badgeAtlantic` 跨大西洋 — `#E76F51`
  - `badgeSea` 海上救援 — `#457B9D`
  - `badgeSenate` 政治与晚年 — `#6D597A`
- **背景母题**：地弧上的同心波纹 + 莫尔斯点划线（稀疏），呼应"S 信号越过大西洋"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（马可尼：意大利 | Marconi 公司/意大利参议院 | Nobel 1909）。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名（Guglielmo Giovanni Maria Marconi）、国籍、出生地（博洛尼亚）、教育（无正规学历/家庭教师）、任职、主要荣誉、核心领域。事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 无线电报的实用化者 / Guglielmo Marconi 1874–1937 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 实用无线电报 / 跨大西洋 / 海上救援 / 广播工业
04  博洛尼亚少年：没有学校的童年 — Rosa 与 Righi 的指点
05  阁楼实验室与 1895 突破 — 单极天线+接地、2 km 越丘
06  1896 赴英 — 专利 12039、Preece 与 GPO 的支持
07  跨海演示 (1897–1899) — 布里斯托尔海峡→英吉利海峡→美洲杯
08  跨大西洋 (1901–1907) — Poldhu→Signal Hill（注记技术争议）→商业业务
09  1909 诺贝尔物理学奖 — 与 Braun 共享，官方理由原句
10  Titanic 与海上无线电影 — Republic 1909、Titanic 1912、听证
11  商业帝国与广播时代 — Marconi 公司、Melba 1920、2MT/2LO
12  参议员、侯爵与梵蒂冈电台 — 政治身份客观呈现（见陷阱表）
13  荣誉与认可 — Nobel 1909 · Matteucci 1901 · Franklin 1918 · IRE 1920
14  遗产：全球无线电时代 — 两分钟静默、命名纪念
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Marconi 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 共享句式 "in recognition of their contributions to the development of wireless telegraphy"，勿写成马可尼独得或"发明无线电奖" |
| 1901 跨洋接收 | 无自动记录、仅耳听 S 信号，技术史长期存疑（波长/白天传播）——page 明载，须注"后世存在技术争论"，禁写成确凿史实 |
| "意大利海军检波器" | Science Museum 归属 1901 实验的检波器类型源自 Bose 1899 发明——只写"归属争议"，禁下结论 |
| 教育 | **无正规教育/学位**，博洛尼亚大学仅旁听与借用实验室；禁写"毕业于博洛尼亚大学"或"Righi 的博士生" |
| 发明优先权 | 无线电非一人发明（Lodge/Branly/Bose/Stone 等前驱，page 明载），用"实用无线电报系统的缔造者"口径，禁写"无线电唯一发明人"；1943 美最高法院仅判 763,772 权利要求无效（被 Stone 预见），禁写成"专利被全部推翻" |
| 法西斯时期 | 1923 入党、皇家科学院院长、Grand Council 成员、Capristo 研究/Guardian 报道的犹太候选人排斥——page 明载可**客观一句**呈现，禁政治评论、禁引法西斯演讲全文；梵蒂冈电台 1931 一句即可 |
| 婚姻 | 两段婚姻（1905 Beatrice 废止 / 1927 Maria）与 5 子女，遗产全归第二房——page 明载可写，一句带过 |
| 免乘 Titanic | 已获赠 Titanic 船票，提前三日乘 Lusitania 处理文书——page 明载，可作花絮 |
| 引语红线 | 可引："Have I done the world good, or have I added a menace?"（page 正文原句）；Postmaster-General Samuel 的 "saved through one man" 可引；其余转述 |
| 结尾花絮 | 1937-07-21 06pm 全球电台两分钟静默、英国邮局请广播船只同悼——page 明载，可作结尾页收束 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| wireless telegraphy | 无线电报 | 1909 诺奖主题 |
| coherer | 金屑检波器 | Branly 原型，Marconi 改良 |
| monopole antenna | 单极天线 | Marconi 标志性设计 |
| grounded transmitter | 接地发射机 | 1895 突破关键 |
| spark-gap transmitter | 火花发射机 | 早期技术，后被连续波取代 |
| magnetic detector | 磁性检波器 | 1902 取代金屑检波器 |
| distress signal | 遇险信号（CQD） | East Goodwin 1899 首例 |
| lightvessel | 灯船 | 海上救援节点 |
| marquess | 侯爵 | 1929 世袭封号 |
| continuous wave | 连续波 | 公司保守争论点 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（流动 / 平稳，75k views）
- **匹配理由**：无线电的叙事主线是"跨海"——布里斯托尔海峡、英吉利海峡、大西洋；SEA 的流动感与平稳推进匹配距离递进的结构化叙事。
- **本地路径**：`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`
- **备选**（未采用）：
  - ★★ New Lands — "开阔/史诗"匹配跨大西洋，但高优先曲宜留给总论篇，且 SEA 的流动感更贴海路叙事
  - ★ Expedition — "探索/远征"匹配工程远征线，但气质偏重，与马可尼商人工程师的敏捷感略隔
- **时长核验**：曲目时长 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐
- **备注**：批内 BGM 去重——Lippmann=Shine Like The Sun、Braun=The Invisible Light、van der Waals=Eternals、Wien=The Flow of Time。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Guglielmo_Marconi/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Guglielmo_Marconi.yaml` | 入库 yaml（已按本提示词 §4/§4.5 备好） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
