# 物理学家立传提示词（C. V. Raman）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖得主的「人物专属立传提示词」，以 Kenneth G. Wilson 篇为结构母本（0–11 节骨架一致）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Chandrasekhara Venkata Raman（钱德拉塞卡拉·文卡塔·拉曼，1930 诺贝尔物理学奖，拉曼效应/光散射）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Raman 篇的设计重心是**从声学到光学的实验物理人生**——他一生几乎没有离开过实验台，立传应以「仪器与光谱」为视觉主线。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Chandrasekhara Venkata Raman（1888-11-07 ~ 1970-11-21，享年 82 岁）
- **气质关键词**：**印度实验物理之父、光散射的征服者、自学成才的财政官教授** —— 1930 诺贝尔物理学奖获奖理由：
  > "for his work on the scattering of light and for the discovery of the effect named after him"（因其关于光散射的工作以及以其名字命名的效应的发现）
- **设计母题**：**光谱的分裂（splitting of light）**。一束单色光穿过物质后分裂出新的波长——这与「平凡生活中折射出非凡色彩」的人生叙事天然对应：财政官深夜的实验室里分裂出的那几条微弱谱线，最终成为分子结构的指纹。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/20th_century/Chandrasekhara_Venkata_Raman/page.md`（Wikipedia 全文已抓取）
- **待下载**：本目录尚无 `Chandrasekhara_Venkata_Raman.html` 与 `images/`，第 0 步需从 `https://en.wikipedia.org/wiki/Chandrasekhara_Venkata_Raman` 下载页面与肖像（infobox 有 1930 年照片）。
- **参考模板**：
  - 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- page.md 已在本地（见上），**事实基准如下**（以 page.md 为唯一依据）：
  - 生卒（1888-11-07 生于英属印度马德拉斯管辖区蒂鲁吉拉帕利 ~ 1970-11-21 逝于印度迈索尔邦班加罗尔，享年 82 岁）
  - 国籍（英属印度 → 印度；frontmatter: British Raj / India / Dominion of India）
  - 父母（父 R. Chandrasekhar Iyer 为当地中学教师、后任物理学教员；母 Parvathi Ammal；八个孩子中的次子）
  - 教育（St Aloysius' Anglo-Indian High School，11 岁通过入学考试、13 岁通过 First Examination in Arts；1902 入马德拉斯 Presidency College；1904 马德拉斯大学 B.A. 物理与英语双金牌；1906 首篇论文；1907 M.A. 最高荣誉；**无 PhD**，1921 获加尔各答大学荣誉 DSc）
  - 学术导师（infobox: Rhishard Llewellyn Jones，中学物理老师，力劝其赴英研究被体检拦下）
  - 任职机构（1907-1917 印度财政服务处 Calcutta 助理会计总长；1917 加尔各答大学 Rajabazar Science College 首任 Palit 物理学教授；1933 班加罗尔印度科学学院（IISc）首任印度籍院长；1948 卸任后创建拉曼研究所并任所长至逝世；1947 印度首任 National Professor）
  - 关键荣誉（Matteucci 1928、Nobel 1930、Hughes 1930、Knight Bachelor 1930、FRS 1924（1968 辞任）、Franklin 1941、Bharat Ratna 1954、Lenin Peace Prize 1957）
  - 知名学生（infobox 博士生：Sisir Kumar Mitra、Vikram Sarabhai；其他 notable：K. S. Krishnan、P. Krishnamurti；另 K. R. Ramanathan、G. N. Ramachandran 有正文明载）
  - 家庭（1907 娶 Lokasundari Ammal，两子：Chandrasekhar Raman 与射电天文学家 Venkatraman Radhakrishnan；1983 诺奖得主 Subrahmanyan Chandrasekhar 是其兄 C. Subrahmanya Ayyar 之子，即**侄子**）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1888 生 → 1902 Presidency College → 1904 B.A. 金牌 → 1906 首篇论文（衍射）→ 1907 M.A. + 入财政服务处 + 婚娶 + IACS 准入 → 1907 IACS 首篇 Nature 论文（偏振牛顿环）→ 1909-1911 仰光/那格浦尔调任 → 1915 首批研究生 → 1917 辞公职就任 Palit 教授 → 1916-1921 声学高产期 → 1921 荣誉 DSc + 首访牛津 + 地中海蓝色之谜（Nature 1921-11）→ 1922《Molecular Diffraction of Light》→ 1924 FRS → 1926 创刊 Indian Journal of Physics → 1927-12 康普顿获奖消息 → 1928-01-07 Krishnan 观察到偏振荧光 → 1928-02-28 获得分离光谱并向报界宣布 → 1928-03-16 "A new radiation" 班加罗尔报告 → 1928 Matteucci → 1930 封爵 + Nobel + Hughes（Rutherford 颁）→ 1932 与 Bhagavantam 测光子自旋 → 1933 就任 IISc 院长 → 1943 创办 Travancore Chemical → 1947 首任 National Professor → 1948-1949 建拉曼研究所 → 1954 Bharat Ratna → 1957 列宁和平奖 → 1968 辞任 FRS → 1970-11-21 班加罗尔逝世

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用本目录 `Chandrasekhara_Venkata_Raman/` 并创建 `images/`。

### 第 2 步：复制 Makefile 【模板通用】

- 复制参照成品 `Makefile`，设置 `MAIN=Chandrasekhara_Venkata_Raman_zh`、`VIDEO_NAME=Chandrasekhara_Venkata_Raman_zh`。

### 第 3 步：收集图片 【人物专属】

- 从 `https://en.wikipedia.org/wiki/Chandrasekhara_Venkata_Raman` 下载 infobox 1930 年肖像到 `images/`；404 则用 Commons `Special:FilePath`，再失败用装饰圆占位。可补插图：拉曼能级图（Raman energy levels）、1928 苯光谱图。

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Raman 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | light scattering | 光散射 | 一生主线：海水蓝色之谜 → 拉曼效应 | 核心页 |
| 1 | Raman spectroscopy | 拉曼光谱学 | 1928 发现奠定的分析工具，分子指纹 | 核心页 |
| 2 | acoustics | 声学 | 弦振动、印度鼓与小提琴的科学研究（1916-1921） | 早年页 |
| 3 | optics | 光学 | 分子衍射、晶体光学、虹彩物质 | 中后期页 |
| 4 | crystallography | 晶体学 | 金刚石结构（1944-1968）与晶格动力学 | 晚年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rhishard Llewellyn Jones | 导师→本人 | 中学物理老师，力劝其赴英深造 |
| advisor-student | K. S. Krishnan | 本人→学生 | 拉曼效应共同发现者，1928 全部论文合作者 |
| advisor-student | Sisir Kumar Mitra | 本人→学生 | infobox 博士生 |
| advisor-student | Vikram Sarabhai | 本人→学生 | infobox 博士生，印度航天之父 |
| spouse | Lokasundari Ammal | 无向 | 1907 年结婚 |
| parent-child | Venkatraman Radhakrishnan | 本人→子 | 射电天文学家 |
| colleague | Ernest Rutherford | 无向 | 1930 提名其诺奖、以皇家学会主席身份颁休斯勋章、推荐其任 IISc 院长 |
| influence | Arthur Compton | 无向 | 康普顿效应直接启发其寻找光的对应现象 |
| controversy | Max Born | 无向 | 1933-34 起晶格动力学理论论战持续数十年 |

> **注**：侄子 Subrahmanyan Chandrasekhar（1983 诺奖）因关系类型白名单所限不入库，仅在立传「家庭」页按 page.md 明载表述（兄之子）。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深邃、炽热、光谱感
- **配色**：深海蓝（主色 `#1B4D6B`，呼应海水蓝色之谜）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeLS` 光散射 — 深海蓝 `#1B4D6B`
  - `badgeSpec` 拉曼光谱 — 青绿 `#0E7C7B`
  - `badgeAcou` 声学 — 赭金 `#C0762C`
  - `badgeCry` 晶体学 — 紫红 `#8E3B7B`
- **背景母题**：柔和气泡中以「一束光分裂成多色细线」的抽象线条呼应设计母题。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页：左侧头像 + 右侧信息网格（生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
3. 结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 光散射的征服者 / C. V. Raman 1888–1970 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含教育、任职、荣誉、家庭、核心领域）
03  核心贡献概览 — 光散射 / 拉曼光谱 / 声学 / 晶体学
04  神童与 presidency（1888–1907）— 11/13/16 岁三连跳、双金牌、首篇论文
05  财政官的深夜实验室（1907–1917）— IACS、"very unusual hours"、声学研究
06  Palit 教授（1917–1933）— "supreme sacrifice"、Indian Journal of Physics
07  地中海的蓝色（1921）— Nicol 棱镜、反驳 Rayleigh、Molecular Diffraction of Light
08  1928：拉曼效应的 28 天（核心贡献页）— Krishnan、2-28 光谱、 "A new radiation"
09  公式框页 — 拉曼位移 Δν = ν₀ ± νᵢ（拉曼线频移示意；page.md 无公式，此为概念图式并注明）
10  争议页 — Landsberg/Mandelstam 独立发现、Krishnan 的角色（按 page.md 呈现）
11  印度科学建制者 — IISc 首任印度籍院长、印度科学院、拉曼研究所
12  门生与家族 — Sarabhai、Krishnan、侄子 Chandrasekhar（按 page.md 表述）
13  荣誉与认可 — Nobel 1930 · Hughes 1930 · Bharat Ratna 1954 · Lenin 1957
14  遗产：国家科学日与分子指纹
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；头部宏定义整体复用结构母本骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make distclean && make pdf`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Raman 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "for his work on the scattering of light and for the discovery of the effect named after him"，勿改写为泛化的"因发现拉曼效应" |
| 独立发现争议 | Landsberg 与 Mandelstam 1928-02-21 观察到谱线（Mandelstam 信件），1930 同获提名，但委员会裁定五点理由后只提 Raman；须按 page.md 呈现，勿单方面偏向 |
| Krishnan 的角色 | Krishnan 是主要研究者、除两篇外全部论文合作者，却未获提名；"the greatest tragedy of my life" 是 Krishnan 语，Raman 晚年敌对态度 page.md 明载；禁止写成"Raman 独自发现" |
| 无 PhD | Raman 终身无博士学位（1921 为荣誉 DSc），勿写"博士毕业" |
| 婚龄与婚期 | 妻子婚龄 13 岁（Parameswaran 考证）与 15 岁两说并存；婚期流行记载 5 月 6 日、考证实为 1907-06-02，两说并写 |
| 侄子身份 | Subrahmanyan Chandrasekhar 是**兄 C. Subrahmanya Ayyar 之子（侄子）**；Sivaramakrishna Chandrasekhar 才是姐妹 Sitalakshmi 之子（外甥），勿混 |
| 印度科学院年份 | 导语作 1933、正文作 1934，两说并存，正文口径优先 |
| 拉曼研究所年份 | 1948 从 IISc 退休、次年（1949）建所，勿写成同年 |
| 第一人口径 | 首位亚洲及首位非白人诺贝尔物理学奖得主；Tagore 1913 为文学奖在前，勿写"印度首位诺奖得主" |
| 政治争议 | 摔 Nehru 半身像/砸 Bharat Ratna 奖章、拒绝政府资助、Kamala Sohonie 事件均为 page.md 明载，可中性呈现但勿渲染演绎 |
| FRS 辞任 | 1968 辞任皇家学会会士（唯一辞任的印度 FRS），原因未载，勿编造 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Raman effect | 拉曼效应 | 原始称呼为 modified scattering |
| Raman scattering | 拉曼散射 | 与 Rayleigh 散射（弹性）区分 |
| Raman spectroscopy | 拉曼光谱学 | 分子"指纹"分析工具 |
| Raman–Nath theory | 拉曼–纳斯理论 | 声光效应理论（与 Nagendra Nath） |
| acousto-optic effect | 声光效应 | 光被声波散射 |
| spectrograph | 摄谱仪 | Raman 自制，勿译"光谱仪"泛称 |
| IACS | 印度科学培育协会 | India's first research institute (1876) |
| National Science Day | （印度）全国科学日 | 2 月 28 日纪念 1928 发现 |
| Palit Professor of Physics | Palit 物理学讲席教授 | 首任，勿译作普通"教授" |
| Bharat Ratna | 印度国宝勋章 | 1954，勿与列宁和平奖混淆年份 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions（79k views）
- **风格**: 鼓舞 / 明亮 / 突破
- **匹配理由**: 1928-02-28 从廉价比色计里抓出分子指纹，是教科书级的"突破性发现"时刻；Awaken 的明亮推进匹配"财政官→诺奖"的逆袭弧线，也呼应 2 月 28 日国家科学日的欢庆气质。
- **备选**（未采用）: Shine Like The Sun（史诗/光明，但与本批他篇撞车风险高）；SEA（流动/平稳，匹配海蓝母题但戏剧张力不足）。
- **本地路径**: `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → `presentations/20th_century/Chandrasekhara_Venkata_Raman/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Chandrasekhara_Venkata_Raman/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库引擎 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
