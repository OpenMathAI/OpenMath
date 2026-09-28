# 物理学家立传提示词（模板标杆实例：Johannes Stark）

> **本文件是 OpenPhysicist 的「物理学家立传提示词模板标杆」的人物专属实例**，目标人物为 Johannes Stark（1919 诺贝尔物理学奖，斯塔克效应的发现者；后为「德意志物理学」运动主将——本篇必须同时如实呈现其科学成就与纳粹劣迹）。
> 凡标注 `【模板通用】` 的部分可原样复用到任何物理学家；标注 `【人物专属】` 的部分需按本文件内容替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck 的提示词 + tex 结构）与物理学家侧首例（Eugene Wigner）的实战经验。
- **本实例**：Johannes Stark（约翰内斯·斯塔克）。
- **设计哲学**：物理学家立传与数学家立传的核心差异，在于**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达——这两点构成物理学家模板的骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Johannes Stark（1874-04-15 ~ 1957-06-21，享年 83 岁）
- **气质关键词**：**斯塔克效应的发现者、阴极射线与极隧射线的实验家、德意志物理学运动的推手** —— 1919 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for his discovery of the Doppler effect in canal rays and the splitting of spectral lines in electric fields"（因发现极隧射线中的多普勒效应以及电场中谱线的分裂）
- **设计母题**：**分裂的谱线（splitting of spectral lines）**。电场使一条谱线分裂为数条——这既是他 1913 年的实验发现，也隐喻其一生：科学成就与政治劣迹在同一人身上「分裂」。视觉语言可用「一条谱线在电场下裂为多条」贯穿全篇。
- **本地 Wikipedia**：`physicist/presentations/20th_century/20th_century/Johannes_Stark/page.md`（已有全文）
  - `{Dir}.html` 与 `images/`：**待下载**（Wikipedia URL: `https://en.wikipedia.org/wiki/Johannes_Stark`）
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 数学家标杆：`mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- `{Dir}.html` **待下载**：`https://en.wikipedia.org/wiki/Johannes_Stark`（page.md 已有全文可先建立事实基准）
- 头像 **待下载**（Wikipedia infobox 照片，1919 年 Stark 像；下载到 `images/`）
- 提取 infobox 与正文，事实基准如下（源自 page.md）：
  - 生卒日期（1874-04-15 生于希肯霍夫 Schickenhof，今属 Freihung，巴伐利亚王国 ~ 1957-06-21 逝于上巴伐利亚特劳恩施泰因 Traunstein 附近自家庄园，享年 83 岁；葬于舍瑙 am Königssee 山地墓园）
  - 国籍（德国；出生时巴伐利亚王国属德意志帝国）
  - 家庭（妻 Luise Uepler，育五子；爱好果树栽培与林业）
  - 教育（拜罗伊特与雷根斯堡文理中学；1894 入慕尼黑大学，学物理、数学、化学与结晶学；1897 在 Eugen von Lommel 指导下以《烟炱的若干物理尤其是光学性质研究》获物理学博士；1897–1900 留校任 von Lommel 助手）
  - 博士导师（Eugen von Lommel）
  - 博士后（无载）
  - 主要任职机构（1900 格丁根大学无俸讲师；1906 汉诺威皇家技术学院 Extraordinary Professor；1909 亚琛工业大学教授；1917–1922 格赖夫斯瓦尔德大学与维尔茨堡大学教授；1933–1939 帝国物理技术研究所（PTR）所长，兼德国科学紧急联合会主席）
  - 关键荣誉（Nobel 物理学奖 1919；Matteucci Medal 1915；维也纳科学院 Baumgartner Prize 1910；格丁根科学院 Vahlbruch Prize 1914；月球背面环形山 1970 命名——2020-08-12 撤名）
  - 知名学生（page.md 无载，禁编）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（约 15 个节点）：1874 生于 Schickenhof → 拜罗伊特/雷根斯堡中学 → 1894 入慕尼黑大学 → 1897 博士（烟炱光学性质，von Lommel 门下）→ 1897–1900 慕尼黑助教 → 1900 格丁根 Privatdozent → 1906 汉诺威 extraordinary professor → 1909 亚琛教授 → 1910 Baumgartner Prize → 1914 Vahlbruch Prize → 1915 Matteucci Medal → 1917–1922 格赖夫斯瓦尔德/维尔茨堡教授 → 1919 诺贝尔奖 → 1920-06-03 诺贝尔演讲《Structural and Spectral Changes of Chemical Atoms》→ 1922《德国物理学的彻底危机》→ 1924 开始支持希特勒（与 Lenard 合著《Hitlergeist und Wissenschaft》）→ 1933–1939 帝国物理技术研究所所长兼科学紧急联合会主席 → 1934-08-21 致 Max von Laue 威胁信（"Heil Hitler" 落款）→ 1934《Nationalsozialismus und Wissenschaft》→ 1938《Nature》刊文 → 二战后在上巴伐利亚自建私人实验室（用诺奖奖金）研究电场中光的偏转 → 1947 去纳粹化法庭判「主犯」4 年监禁（后缓刑）→ 1949 慕尼黑上诉改判「从犯」、罚款 1000 马克 → 1957-06-21 逝于 Traunstein → 1970 月球环形山命名 / 2020-08-12 撤名

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Johannes_Stark/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录 `Eugene_Wigner/Makefile`，设置 `MAIN=Johannes_Stark_zh`、`VIDEO_NAME=Johannes_Stark_zh`

### 第 3 步：收集图片 【人物专属】

- 头像 **待下载**：优先 Wikipedia infobox 照片（1919 年 Stark 像；Commons `Special:FilePath` 或 REST API 查实际文件名）
- 可用插图（page.md 明载）：月球背面 Stark 环形山图（IAU Gazetteer，注意须与 2020 撤名并提）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Stark 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | spectroscopy | 光谱学 | frontmatter 主领域；电场中谱线分裂 | 核心贡献页 |
| 1 | atomic physics | 原子物理 | 谱线分裂的原子结构意义 | 核心贡献页 |
| 2 | canal rays | 极隧射线 | 其中发现多普勒效应 | 极隧射线页 |
| 3 | optics | 光学 | 博士论文（烟炱光学性质）与晚年电场光偏转 | 早年页/晚年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eugen von Lommel | 师→生（博士导师） | 慕尼黑博士导师（1897 烟炱光学论文），1897–1900 任其助手 |
| colleague | Albert Einstein | 无向 | 1907 以《放射性与电子学年鉴》编辑身份约爱因斯坦写相对论综述；后成为攻击相对论的急先锋 |
| colleague | Philipp Lenard | 无向 | 「德意志物理学」运动共同主将（同为诺奖得主），1924 合著《Hitlergeist und Wissenschaft》 |
| controversy | Max von Laue | 施害→对方 | 1934-08-21 致信威胁 Laue 服从党路线，落款 "Heil Hitler" |
| controversy | Werner Heisenberg | 施害→对方 | 因 Heisenberg 为相对论辩护，在党卫机关报《Das Schwarze Korps》撰文称其为 "White Jew" |
| spouse | Luise Uepler | 无向 | 育五子 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：阴郁、紧张、双重性
- **配色**：深酒红（暗色传记基调）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeSpec` 光谱学 — 琥珀 `#E07B30`
  - `badgeAtom` 原子物理 — 靛蓝 `#4C5FD5`
  - `badgeCanal` 极隧射线 — 青绿 `#0E7C7B`
  - `badgePol` 「德意志物理学」— 铁灰 `#4A4A55`
- **背景母题**：分裂谱线（一条竖线在下方分裂为三条错位短竖线，稀疏排布），呼应「谱线分裂」与「一生双重性」双重母题（与第 2 步设计母题一致）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自 page.md，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 斯塔克效应的发现者 / Johannes Stark 1874–1957 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含出生地 Schickenhof、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 极隧射线多普勒效应 / 电场谱线分裂 / 300+ 论文（概念图式：谱线分裂示意，page.md 无标志性公式）
04  早年：上普法尔茨与慕尼黑 (1874–1900) — 中学、1894 入学、1897 烟炱博士论文、Lommel 助教
05  游历教席：格丁根→汉诺威→亚琛 (1900–1917) — Privatdozent、extraordinary professor、教授
06  极隧射线中的多普勒效应（核心贡献页之一，概念图式）
07  斯塔克效应：电场中的谱线分裂（核心贡献页之二，概念图式）
08  荣誉与认可 — Nobel 1919 · Matteucci 1915 · Baumgartner 1910 · Vahlbruch 1914
09  1907 年的编辑：与爱因斯坦的交集 — 约稿相对论综述、e0=m0c2「基本能量量子」、日后的反讽
10  从《德国物理学的彻底危机》到支持希特勒 (1922–1933) — 1924 表态、与 Lenard 合著
11  「德意志物理学」：掌权与清洗 (1933–1939) — PTR 所长、攻击理论物理为「犹太的」、Laue/Heisenberg 事件
12  战后清算 — 私人实验室 Gut Eppenstatt、1947「主犯」、1949 改判「从犯」
13  纪念的撤销 — 1970 月球环形山命名、2020-08-12 IAU 撤名
14  遗产：斯塔克效应长存，评价两分
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Stark 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由两项并提 | 诺奖理由含两件事：极隧射线中的多普勒效应 + 电场中谱线分裂（后者即斯塔克效应）；勿写成「因发现斯塔克效应获奖」单项 |
| 发现年份 | 多普勒效应与谱线分裂的**具体发现年份 page.md 均未载**，禁写编造年份，用概念图式 |
| 与爱因斯坦的关系 | 必须两面并呈：1907 年 Stark 是约稿编辑（当时爱因斯坦尚不知名，且其约稿间接催生广义相对论思路）；1920s 后是「德意志物理学」反相对论急先锋——page.md 明言这是 "ironic"，勿只写一面 |
| 攻击对象口径 | 攻击爱因斯坦（"Jewish physics"）与 Heisenberg（非犹太人，因辩护相对论被称 "White Jew"，载于党卫机关报《Das Schwarze Korps》）；page.md 未载对 Planck/Sommerfeld 的攻击细节（见 Planck 页），本篇禁跨页引入 |
| 去纳粹化两审 | 1947 判「Major Offender」4 年监禁（后缓刑）→ 1949 慕尼黑上诉法庭改判「Lesser Offender」+ 罚款 1000 马克，两判勿混 |
| 月球环形山 | 1970 IAU 命名时**不知其纳粹活动**，2020-08-12 撤名——命名与撤名必须同时交代，禁只写命名 |
| 诺奖奖金去向 | 用诺奖奖金在上巴伐利亚自家庄园（Gut Eppenstatt）建私人实验室，战后研究电场中光的偏转；勿写成「隐居不研」 |
| 纳粹内容尺度 | 引用纳粹言论（如 "eradicate the Jewish spirit"）须克制、注明出处且用于批判性叙述；全篇定性词用「反犹主义运动」（antisemitic）——这是 page.md 原文定性，禁止中性化处理 |
| 同名区分 | Stark effect（物理效应）与 Stark crater（月球环形山，已撤名）勿混；Wilhelm Müller（1941《Jüdische und deutsche Physik》合著者，慕尼黑物理学家）若提及须限「合著者」身份，勿与其他同名者混淆 |
| 无载禁写 | 五名子女姓名、博士生、与 Sommerfeld 冲突细节、Stark effect 的理论解释者（Epstein/Schwarzschild）、Stark–Einstein 光化学当量律的正文细节（仅 See also 一提）——page.md 均无载 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Stark effect | 斯塔克效应 | 电场中谱线分裂，诺奖理由后半句 |
| canal rays | 极隧射线 | 多普勒效应的载体；勿译「隧道射线」 |
| Doppler effect | 多普勒效应 | 极隧射线中的运动光源频移 |
| spectral line splitting | 谱线分裂 | 电场中分裂，勿与磁场塞曼效应混淆 |
| Deutsche Physik | 德意志物理学 / 雅利安物理学 | 反犹运动名，保留德文原词并注明性质 |
| denazification | 去纳粹化 | 战后清算程序，两审判决勿混 |
| Privatdozent | 无俸讲师 | 德语学术职衔 |
| Physikalisch-Technische Reichsanstalt | 帝国物理技术研究所（PTR） | 1933–1939 所长职 |
| Notgemeinschaft der Deutschen Wissenschaft | 德国科学紧急联合会 | 1933 起任主席 |
| white Jew | 「白色犹太人」 | Stark 对 Heisenberg 的攻击用语，须带引号并注明出处 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Tragedy** — Alex-Productions
- **风格**: 深色 / 戏剧性
- **匹配理由**:
  - 「深色」匹配 Stark 的一生底色——诺奖桂冠与纳粹劣迹同在一身，是一部带罪的科学传记
  - 「戏剧性」匹配叙事的强烈反差——1907 年约稿爱因斯坦的编辑，二十年后的反相对论急先锋；1919 年诺奖，1947 年去纳粹化法庭
  - 谱线分裂的母题本身自带戏剧张力，配乐应承载而非冲淡这种沉重
- **本地路径**: `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` → `presentations/20th_century/Johannes_Stark/Tragedy.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Johannes_Stark/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex` | 数学家标杆参考 |
| `MySQL/seed_person.py` | 人物主记录 + fields/relations 入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
