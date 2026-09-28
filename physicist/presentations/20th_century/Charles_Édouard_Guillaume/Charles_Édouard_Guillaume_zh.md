# 物理学家立传提示词（模板标杆实例：Charles-Édouard Guillaume）

> **本文件是 OpenPhysicist 的「物理学家立传提示词模板标杆」的人物专属实例**，目标人物为 Charles-Édouard Guillaume（1920 诺贝尔物理学奖，因发现镍钢合金反常——不胀钢 invar 等——而获奖）。
> 凡标注 `【模板通用】` 的部分可原样复用到任何物理学家；标注 `【人物专属】` 的部分需按本文件内容替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck 的提示词 + tex 结构）与物理学家侧首例（Eugene Wigner）的实战经验。
- **本实例**：Charles-Édouard Guillaume（夏尔·爱德华·纪尧姆）。
- **设计哲学**：物理学家立传与数学家立传的核心差异，在于**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达——这两点构成物理学家模板的骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Charles-Édouard Guillaume（1861-02-15 ~ 1938-06-13，享年 77 岁）
- **气质关键词**：**不胀钢的发现者、米制国际局的掌门人、精密计量的守望者** —— 1920 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for the service he had rendered to precision measurements in physics by his discovery of anomalies in nickel steel alloys"（因其发现镍钢合金中的反常现象，为物理学精密测量所作贡献）
- **设计母题**：**不变之尺（invariance）**。invar 之名即取自 invariable——温度变化而尺寸几乎不变。视觉语言可用「温度曲线起伏、而尺长线保持水平」表达其毕生主题：为世界的测量找一个不变的基准。
- **本地 Wikipedia**：`physicist/presentations/20th_century/20th_century/Charles_Édouard_Guillaume/page.md`（已有全文）
  - `{Dir}.html` 与 `images/`：**待下载**（Wikipedia URL: `https://en.wikipedia.org/wiki/Charles-Édouard_Guillaume`）
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 数学家标杆：`mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- `{Dir}.html` **待下载**：`https://en.wikipedia.org/wiki/Charles-Édouard_Guillaume`（page.md 已有全文可先建立事实基准）
- 头像 **待下载**（可用 1920 年 infobox 照片；另有 1918 年 Auguste Léon 彩色 Autochrome 照与 1922 年 Marie-Louise Catherine Breslau 粉彩肖像，均 page.md 明载，下载到 `images/`）
- 提取 infobox 与正文，事实基准如下（源自 page.md）：
  - 生卒日期（1861-02-15 生于瑞士弗勒里耶 Fleurier ~ 1938-06-13 逝于法国塞夫勒 Sèvres（infobox 作 Paris），享年 77 岁）
  - 国籍（瑞士；出身法裔家庭，frontmatter 双列 Switzerland/France，正文口径为 Swiss physicist）
  - 家庭（瑞士钟表匠之子；1888 与 A. M. Taufflieb 结婚，育三子；基督徒）
  - 教育（纳沙泰尔接受早期教育；1883 年获苏黎世联邦理工学院（ETH Zurich）物理学博士——**博士导师 page.md 无载**）
  - 博士后（无载）
  - 主要任职机构（国际计量局 BIPM——1915–1936 任局长，前任 Justin-Mirande René Benoit、继任 Albert Pérard；曾在巴黎天文台默东分部任职并做恒温测量实验）
  - 关键荣誉（Nobel 物理学奖 1920；John Scott Medal 1914；Guthrie Lecture 1919；Duddell Medal and Prize 1928（frontmatter 记作 Dennis Gabor Medal——为该奖后用名）；法国荣誉军团军官/大军官；巴黎大学荣誉博士）
  - 知名学生（page.md 无载，禁编）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（约 17 个节点）：1861 生于 Fleurier（钟表匠之家）→ 纳沙泰尔早期教育 → 1883 ETH Zurich 物理学博士 → 1886《Études thermométriques》→ 1888 与 A. M. Taufflieb 结婚 → 1889《精密测温学论》→ 1894《Unités et Étalons》→ 1896《La Température de L'Espace》最早估计星际辐射温度 5–6 K → 1898《Recherches sur le nickel et ses alliages》→ 1904《Les applications des aciers au nickel》→ 1914 John Scott Medal → 1915–1936 任 BIPM 局长（继 Benoit）→ 1919 第五次 Guthrie Lecture《The Anomaly of the Nickel-Steels》→ 1920 诺贝尔奖 → 1920-12-11 诺贝尔演讲《Invar and Elinvar》→ 1928 Duddell Medal → 1936 卸任（继任 Pérard）→ 1938-06-13 逝于 Sèvres

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Charles_Édouard_Guillaume/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录 `Eugene_Wigner/Makefile`，设置 `MAIN=Charles_Édouard_Guillaume_zh`、`VIDEO_NAME=Charles_Édouard_Guillaume_zh`

### 第 3 步：收集图片 【人物专属】

- 头像 **待下载**：优先 Wikipedia infobox 照片（1920 年像）；备选 1918 Autochrome 或 1922 粉彩肖像（Commons `Special:FilePath` / REST API）
- 可用插图（page.md 明载）：1918 年 Auguste Léon 彩色照（The Archives of the Planet）、1922 年 Breslau 粉彩肖像

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Guillaume 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | precision measurement | 精密测量 | 诺奖理由核心；BIPM 局长职守 | 全篇 |
| 1 | nickel-steel alloys | 镍钢合金 | invar/elinvar/platinite 的发现 | 合金页 |
| 2 | thermometry | 测温学 | 1886/1889 专著与恒温测量实验 | 早年页 |
| 3 | horology | 钟表学 | 家学渊源；Guillaume 摆轮、航海天文钟 | 钟表页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Kristian Birkeland | 无向 | 巴黎天文台默东分部共事，合作恒温测量实验 |
| colleague | Justin-Mirande René Benoit | 无向 | BIPM 前任局长，1915 年由其继任 |
| spouse | A. M. Taufflieb | 无向 | 1888 年结婚，育三子 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：沉稳、精准、金属质感
- **配色**：石板灰绿（钢与稳定）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeMetro` 精密测量 — 靛蓝 `#4C5FD5`
  - `badgeAlloy` 镍钢合金 — 琥珀 `#E07B30`
  - `badgeThermo` 测温学 — 玫瑰 `#C4204F`
  - `badgeHoro` 钟表学 — 青绿 `#0E7C7B`
- **背景母题**：水平基准线（温度曲线上下起伏、一条水平线恒定不动，稀疏排布），呼应「温度变化而尺长不变」的 invar 思想（与第 2 步设计母题一致）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域。事实取自 page.md，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 不胀钢的发现者 / Charles-Édouard Guillaume 1861–1938 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含出生地 Fleurier、教育、任职、荣誉、核心领域）
03  核心贡献概览 — invar / elinvar / platinite / 太空温度估计（概念图式：温度-长度曲线，page.md 无标志性公式）
04  早年：钟表匠之家 (1861–1883) — Fleurier、纳沙泰尔、1883 ETH 博士
05  计量人生：国际计量局 — BIPM 职守、1915–1936 局长、米制系统著作
06  测温学 — 1886/1889 专著、巴黎天文台默东分部恒温实验（与 Birkeland 共事）
07  invar：不胀钢（核心贡献页之一，概念图式：近零热膨胀系数）
08  elinvar 与 platinite — 弹性模量温度系数近零、航海天文钟游丝、非磁性、红铂
09  钟表学：Guillaume 摆轮 — 补偿摆轮、消除中温误差、负二次膨胀系数变体
10  1896：太空的温度 — 最早估计星际辐射 5–6 K、后世所知的宇宙微波背景概念先驱
11  荣誉与认可 — Nobel 1920 · Guthrie Lecture 1919 · John Scott 1914 · Duddell 1928 · 荣誉军团
12  遗产：从度量衡到精密时代 — BIPM 二十年、invar 至今仍在精密仪器中
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Guillaume 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 死亡日期噪声 | frontmatter 有 1938-06-13 与 1938-05-13 两值，infobox 与正文确认 **1938-06-13**，以正文为准 |
| 卒地口径 | 正文作 **Sèvres, Paris**（塞夫勒，亦为 BIPM 所在地），infobox 简作 Paris——写「塞夫勒（巴黎）」并注明，勿只写巴黎 |
| 国籍口径 | 瑞士物理学家（法裔家庭），frontmatter 双列 Switzerland/France；deck 全篇口径「瑞士物理学家」，勿写成法国人 |
| 发现年份禁写 | **invar/elinvar/platinite 的具体发现年份 page.md 均未载**（常见资料误写 invar 为 1896），禁编年份 |
| BIPM 入职年份 | page.md 只载 1915–1936 任局长，**入职 BIPM 的年份无载**，禁编（勿从诺奖传记反推 1883） |
| 博士导师 | page.md 无载，身份信息页该栏写「page.md 无载」，禁编 |
| 太空温度表述 | 1896 年估计 5–6 K 是「最早估计星际辐射温度」的先驱记载；page.md 说该概念「后来被称为宇宙微波背景」——勿拔高为「预言/发现了 CMB」，也勿提 Penzias & Wilson 得奖细节（page.md 未展开） |
| Birkeland 共事 | 仅载「在巴黎天文台默东分部共事、做恒温测量实验」，勿展开 Birkeland 的极光/宇宙学理论 |
| 奖章名称辨析 | infobox 作 **Duddell Medal and Prize 1928**；frontmatter 记作 Dennis Gabor Medal（IOP 后用名）——以 infobox 为主，可加注「今名 Gabor Medal」；Guthrie Lecture 是 1919 年第五讲，勿与 Duddell 混 |
| 姓名拼写 | 正文连字符形式 **Charles-Édouard Guillaume**；frontmatter/分批文件作 Charles Édouard Guillaume——deck 内统一连字符形式，勿混用 |
| 无载禁写 | 三名子女姓名、宗教细节（仅载 "He was a Christian" 一句）、platinite 的成分与用途展开（红铂别名有载）、与 Ibáñez e Ibáñez de Ibero 的交往（仅 See also 一提）——page.md 均无载 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| invar | 不胀钢 / 因瓦合金 | 近零热膨胀系数；名称取自 invariable |
| elinvar | 恒弹合金 / 埃林瓦尔 | 弹性模量温度系数近零；勿与 invar 混 |
| platinite | 红铂 | 镍钢合金别名「红铂」，勿与真铂混淆 |
| coefficient of thermal expansion | 热膨胀系数 | invar 的核心指标 |
| modulus of elasticity | 弹性模量 | elinvar 的核心指标 |
| marine chronometer | 航海天文钟 | elinvar 游丝的应用场景 |
| compensation balance | 补偿摆轮 | Guillaume 摆轮的用途 |
| Guillaume balance | 纪尧姆摆轮 | 以其命名的钟表部件 |
| BIPM | 国际计量局 | 国际米制公约机构，驻塞夫勒 |
| nickel steel | 镍钢 | 诺奖理由的 "nickel steel alloys" |
| middle-temperature error | 中温误差 | 摆轮的温度中间段误差，Guillaume 变体消除之 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions
- **风格**: 温和 / 稳定
- **匹配理由**:
  - 「稳定」正是 Guillaume 一生的主题词——invar 的不变、BIPM 二十一年的守望、精密计量的恒常
  - 「温和」匹配其低戏剧性的人生——没有革命性对抗，只有日复一日的测量与改进，是一部「工匠型科学家」的传记
  - 相比高张力曲目，本篇节奏应如基准线般平稳
- **备选** (未采用):
  - ★★ SEA — 「流动/平稳」匹配测量的连续性，但气质偏冷，弱于 With Me 的稳定感
- **本地路径**: `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` → `presentations/20th_century/Charles_Édouard_Guillaume/With Me.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Charles_Édouard_Guillaume/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex` | 数学家标杆参考 |
| `MySQL/seed_person.py` | 人物主记录 + fields/relations 入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
