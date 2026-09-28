# 物理学家立传提示词（人物专属：Karl Ferdinand Braun）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖批量立传的**人物专属提示词**，结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Karl Ferdinand Braun（卡尔·费迪南德·布劳恩），1909 年诺贝尔物理学奖得主（与 Guglielmo Marconi 共享），布劳恩管（阴极射线管）、晶体检波器与无线电双回路发明的"三线天才"。
- **设计哲学**：保留物理学家模板两大骨架——「身份信息页」与「研究领域结构化表达」；本人物的设计重心是**一个物理学家点亮三条技术谱系**：显示（CRT→电视）、半导体（1874 单向导电→电子学）、无线电（双回路/相控阵→雷达与 MIMO）。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Karl Ferdinand Braun（1850-06-06 ~ 1918-04-20，享年 67 岁）
- **气质关键词**：**布劳恩管的父亲、半导体之路的起点、无线电的物理改良者**
- **官方获奖理由（禁止改写，与 Marconi 共享）**：
  > "in recognition of their contributions to the development of wireless telegraphy"（表彰他们对无线电极报发展的贡献）
- **设计母题**：**电子束与射线管（electron beam / Braun tube）**——荧光屏上的偏转光点；视觉语言用真空管轮廓、扫描线与定向波束。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Karl_Ferdinand_Braun/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页 `cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⏳ **待下载** `https://en.wikipedia.org/wiki/Karl_Ferdinand_Braun` 到 `{Dir}/Karl_Ferdinand_Braun.html`（本地暂只有 `page.md`）
- **事实基准**：
  - 生卒（1850-06-06 生于黑森选侯国富尔达 ~ 1918-04-20 卒于美国纽约布鲁克林，享年 67；信义宗教徒）
  - 教育（1868 入马尔堡大学习物理/化学/数学；1869 转柏林大学任 Heinrich Gustav Magnus 助手；Magnus 1870 去世后师从 Georg Hermann Quincke；1872 以振动弦论文获柏林大学博士；后随 Quincke 赴维尔茨堡任助教）
  - 任职（1874 莱比锡 Thomasschule 任教 → 1876 马尔堡理论物理特聘教授 → 1880 斯特拉斯堡 → 1883 卡尔斯鲁厄高等技术学校物理教授 → 1885 蒂宾根 → 1895 重返斯特拉斯堡任物理研究所所长）
  - 关键荣誉（Nobel 1909（奖章即其双回路设计图）；维也纳技术大学荣誉博士；法兰克福物理协会荣誉会员；1987 年 SID 设立 Karl Ferdinand Braun Prize 以其命名）
  - 知名学生（博士生：Richard Gans、Leonid Mandelstam、Nikolai Papaleksi、Godfrey Thomson；助手 Jonathan Zenneck）
  - 核心贡献清单：
    1. 1874 金属-半导体结单向导电（半导体电子学起点）
    2. 1897 布劳恩管（阴极射线管，示波器与电视之源）
    3. 无线电双回路发射机（振荡与辐射回路感应耦合分离）
    4. 晶体检波器（取代金屑检波器，提升接收灵敏度）
    5. 1905 相控阵定向天线（雷达/智能天线/MIMO 先声）
    6. Telefunken 共同创始（Stollwerck 资本联盟→1903 公司化）
  - 诺奖演讲（注记）：1909-12-11 *Electrical Oscillations and Wireless Telegraphy*
  - 核心时间线（1850 生 → 1868 马尔堡 → 1869 柏林/Magnus → 1872 博士 → 1874 半导体单向导电发现 + 莱比锡任教 → 1876 马尔堡教授 → 1883 卡尔斯鲁厄 → 1885 蒂宾根 → 1895 斯特拉斯堡所长 → 1897 布劳恩管 → 1897-98 转向无线电+晶体检波器 → 1899 Cuxhaven 北海实验+专利 → 1900-09-24 Cuxhaven–Helgoland 62 km → 1903 Telefunken 前身公司 → 1905 相控阵天线 → 1909 共享诺奖 → 1914 赴纽约为 Telefunken 专利诉讼作证 → 1917 美对德宣战后以敌侨身份滞留 → 1918 卒于布鲁克林）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下已有 `Karl_Ferdinand_Braun/`（本提示词所在），需新建 `images/` 子目录存放肖像与插图

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Karl_Ferdinand_Braun_zh`、`VIDEO_NAME=Karl_Ferdinand_Braun_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：page.md 内嵌 1904 年实验室照（KF_Braun.png）；优先 Commons `Special:FilePath/KF Braun.png?width=500`（布劳恩在实验室，1904）
- 备选：移动电台 1903 照、原始布劳恩管 1897 实物照（作插图更好）；再失败用装饰圆占位（主色边框圆 + 姓名缩写）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | wireless telegraphy | 无线电报 | 双回路发射机/晶体检波器，1909 诺奖核心 | 核心页 |
| 1 | electronics | 电子学 | 布劳恩管开启显示与示波器 | CRT 页 |
| 2 | semiconductor physics | 半导体物理 | 1874 金属-半导体结单向导电 | 半导体页 |
| 3 | antenna engineering | 天线技术 | 1905 相控阵→雷达/MIMO 先声 | 天线页 |

入库：`MySQL/data/Karl_Ferdinand_Braun.yaml`（已备好，`cd MySQL && python3 seed_person.py data/Karl_Ferdinand_Braun.yaml`）。
校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Georg Hermann Quincke | 师→生 | 柏林大学博士导师，1872 振动弦论文 |
| advisor-student | Richard Gans | 布劳恩→学生 | 博士生 |
| advisor-student | Leonid Mandelstam | 布劳恩→学生 | 博士生 |
| advisor-student | Nikolai Papaleksi | 布劳恩→学生 | 博士生 |
| advisor-student | Godfrey Thomson | 布劳恩→学生 | 博士生 |
| co-honored | Guglielmo Marconi | 无向 | 1909 年诺贝尔物理学奖共享 |
| colleague | Jonathan Zenneck | 无向 | 助手，1899 为布劳恩管引入 Y 偏转 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：真空管、射线、德意志工匠
- **配色**：电子管深褐（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 — 电子管深褐 `#4E342E`
  - `badgeTube` 阴极射线管 — `#B23A48`
  - `badgeCrystal` 晶体检波器 — `#3B7A57`
  - `badgeRadio` 双回路无线电 — `#4C5FD5`
  - `badgeAntenna` 相控阵 — `#C97B2D`
- **背景母题**：稀疏真空管轮廓 + 扫描线光点，呼应"荧光屏上被驱动的电子束"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（布劳恩：德国 | 斯特拉斯堡大学 | Nobel 1909）。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名（Karl Ferdinand Braun）、国籍、出生地（富尔达）、师承（Quincke）、任职（六站教职）、主要荣誉、核心领域。事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 布劳恩管之父 / Karl Ferdinand Braun 1850–1918 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — CRT / 半导体 / 双回路 / 相控阵（三条技术谱系）
04  富尔达求学路 (1850–1872) — Marburg→Berlin、Magnus→Quincke、振动弦博士
05  六站教职 (1874–1895) — Thomasschule→Marburg→Strassburg→Karlsruhe→Tübingen→Strassburg
06  1874：半导体的起点 — 金属-半导体结单向导电，点接触整流之基
07  1897：布劳恩管 — 冷阴极+10 万伏+旋转镜的"不完美"起点
08  无线电双回路 — 感应耦合分离振荡与辐射回路，续振与远距
09  晶体检波器与 62 km — 取代金屑检波器、Cuxhaven–Helgoland
10  1905：相控阵天线 — 三天线定向发射，雷达/MIMO 先声
11  1909 诺贝尔物理学奖 — 与 Marconi 共享；Marconi 自认"借用"（注记）
12  Telefunken 与产业 — Stollwerck 资本、Professor Braun's Telegraphy Company
13  纽约的晚年 (1914–1918) — 专利诉讼证人、敌侨、布鲁克林
14  遗产：从布劳恩管到每一块屏幕 — 电视/半导体/雷达三线传承
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Braun 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 共享句式 "in recognition of their contributions to the development of wireless telegraphy"，勿写 Braun 独得；其奖章图案即双回路设计 |
| 导师口径 | 博士导师 = **Quincke**（infobox+正文一致）；Magnus 是"其他学术导师/助手东家"；frontmatter 另列 August Kundt 但正文未提，禁写 Kundt |
| "电视之父" | 是与 Nipkow 等人**共享**的称谓，且 page 明载 Braun 本人认为布劳恩管不适合电视——禁写"电视发明人" |
| 1874 半导体 | 发现的是金属-半导体结**单向导电性质**（点接触整流之基），禁写成"发明二极管成品"；"every semiconductor 的曾祖父"是媒体比喻，可作注记勿当头衔 |
| CRT 细节 | 1897 第一版：冷阴极、中等真空、10 万伏加速、磁偏转仅一向+旋转镜——按"不完美起点"叙事，勿写成完善仪器 |
| 1901 跨洋 | Marconi 在纽芬兰用的是 Braun 电路发射机，但"是否真的收到"文献有争议（page 明载），禁写成确凿佐证 |
| Marconi 关系 | page 明载 Marconi 大量调谐专利用了 Braun 的专利并自认 "borrowed"——可客观注记，勿写成剽窃指控 |
| 学生同名 | Godfrey Thomson 与 J.J. Thomson / G.P. Thomson 无关，note 已注明，禁混淆 |
| 晚年身份 | 1917 美对德宣战后以"敌侨"身份被拘但可在布鲁克林自由活动，1918-04-20 卒——按 page 原口径 |
| 引语红线 | 全篇仅 Marconi "borrowed" 一词带引号（page 明载），其余禁引语；诺奖演讲标题 Electrical Oscillations and Wireless Telegraphy 可注 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| cathode-ray tube | 阴极射线管（布劳恩管） | 德语 Braunsche Röhre |
| crystal detector | 晶体检波器 | 取代金屑检波器 |
| inductive coupling | 感应耦合 | 双回路分离的关键 |
| phased array | 相控阵 | 1905 三天线定向发射 |
| semiconductor | 半导体 | 1874 单向导电发现 |
| point-contact rectifier | 点接触整流器 | 后续器件化 |
| damped oscillation | 阻尼振荡 | 火花系统问题 |
| cold cathode | 冷阴极 | 1897 版特征 |
| Leyden jar | 莱顿瓶 | 振荡回路储能 |
| oscilloscope | 示波器 | CRT 早期用途 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（纪录片 / 电影 / 稳重，2:34）
- **匹配理由**：阴极射线正是"看不见的光"——肉眼不可见却点亮荧光屏；曲名与 CRT/射线母题直接对应，纪录片气质匹配其三条技术谱系的沉稳叙事。
- **本地路径**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **备选**（未采用）：
  - ★★ Nostalgia — "温和/传记"匹配六站教职的辗转叙事，但"怀旧"气质弱于射线母题的直接对应
  - ★ PAST — "历史感/深沉"匹配其 1918 年客死纽约的晚年，但基调过沉，与其三条谱系的创造感不合
- **时长核验**：曲目 2:34 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐
- **备注**：批内 BGM 去重——Lippmann=Shine Like The Sun、Marconi=SEA、van der Waals=Eternals、Wien=The Flow of Time。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Karl_Ferdinand_Braun/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Karl_Ferdinand_Braun.yaml` | 入库 yaml（已按本提示词 §4/§4.5 备好） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
