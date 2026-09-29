# 物理学家立传提示词（21 世纪批次：Vitaly L. Ginzburg）

> **本文件是 OpenPhysicist「物理学家立传提示词」**，对象：Vitaly L. Ginzburg（2003 诺贝尔物理学奖，金兹堡–朗道理论）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 凡标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。

---

## 一、模板定位 【人物专属】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Vitaly Lazarevich Ginzburg（维塔利·拉扎列维奇·金兹堡），2003 诺贝尔物理学奖得主（三人共享之一）。
- **设计哲学**：保留物理学家模板「身份信息页 + 结构化研究领域」骨架；Ginzburg 是「超导理论 + 苏联核计划 + 天体物理 + 无神论斗士」多面人物，叙事主线取「1950 金兹堡–朗道理论 → 2003 迟到的诺奖」，辅线取「金兹堡清单」作为科学纲领页。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Vitaly Lazarevich Ginzburg（1916-10-04 [儒略历 09-21] ~ 2009-11-08，享年 93 岁）
- **获奖理由（官方英文原文 + 中译，page.md 导语引号原句，禁止改写）**：
  > "pioneering contributions to the theory of superconductors and superfluids"（对超导体和超流体理论的先驱性贡献）
- **共享格局**：2003 奖由 Ginzburg、Alexei Abrikosov（II 类超导体/涡旋晶格）与 Anthony J. Leggett（超流理论）三人共享。
- **气质关键词**：**金兹堡–朗道理论的共创者、苏联氢弹的幕后功臣、科学无神论的旗手**
- **设计母题**：**序参量（order parameter）**。金兹堡引入序参量刻画超导态——以「相变边界两侧的两种颜色域 + 连接域的场线」为核心视觉概念，呼应「正常态与超导态之间的过渡」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Vitaly_L._Ginzburg/page.md`
- **第 0 步状态**：page.md 已有本地；**html 与 images/ 待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Vitaly_L._Ginzburg`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`、`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 数据库同步含「研究领域 + 入库」（第 4 步）与「社会关系 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ☐ 待下载 `https://en.wikipedia.org/wiki/Vitaly_L._Ginzburg` 到 `{Dir}.html` 与 `images/` 肖像（Commons `Vitaly_Ginzburg.jpg` 1980 年莫斯科照 或 `Ginzburg_in_MSU.jpg`，250px 改 500px）
- 事实基准（以本地 page.md 为准，第一轮已核对）：
  - 生卒：1916-10-04（儒略历 09-21）生于莫斯科（俄罗斯帝国）~ 2009-11-08 逝于莫斯科（心脏骤停），享年 93 岁；葬新圣女公墓（11-11 下葬）
  - 国籍：苏联 → 俄罗斯
  - 家庭：犹太家庭——父 Lazar Yefimovich Ginzburg 工程师、母 Augusta Wildauer 医生；第一任妻 Olga Ivanovna Zamsha（1937 结婚，1946 离婚，育 1 子，MEPhI 副教授）；第二任妻 Nina Ivanovna Ginzburg（née Ermakova，1922-10-02 ~ 2019-05-19，实验物理学家，1946 结婚——曾因被诬 plot to assassinate Stalin 入狱一年余）
  - 教育：莫斯科大学物理系 1938 毕业；1940 Kandidat（副博士）论文；1942 Doktor Nauk（全博士）
  - 博士导师：infobox 明载 **Igor Tamm**（frontmatter 另列 Lev Landau——见陷阱表裁定：入库只写 Tamm）
  - 任职轨迹：1940 起任职于苏联/俄罗斯科学院列别杰夫物理研究所（FIAN）至终身；继承 Tamm 任该所理论物理室主任；1968 在莫斯科物理技术学院（MIPT/MEPhI）创建物理与天体物理问题教研室并任主任；期刊《Uspekhi Fizicheskikh Nauk》主编；下诺夫哥罗德（Lobachevsky）国立大学亦有任职
  - 苏联核计划：1948–1952 在 Igor Kurchatov 领导下参与氢弹研制；与 Tamm 各自提出可实现氢弹构想；项目迁往 Arzamas-16 后因背景未被准许随迁，留莫斯科远程支持、受监视，渐被移出项目
  - 关键荣誉：卫国战争英勇劳动奖章 1946；莫斯科 800 周年纪念奖章 1948；斯大林奖一等奖 1953；列宁勋章 1954；劳动荣誉勋章两次 1954/1975；劳动红旗勋章两次 1956/1986；列宁奖 1966；Marian Smoluchowski 奖章 1984；英国皇家学会外籍院士 ForMemRS 1987；RAS 金质奖章 1991；Wolf 物理学奖 1994/95；Vavilov 金质奖章 1995；罗蒙诺索夫金质奖章 1995；For Merit to the Fatherland 三级 1996/一级 2006；APS Fellow 2003；Nobel 2003；Ó Ceallaigh 奖章（IUPAP 宇宙线委员会）；Humboldt 奖；UNESCO Niels Bohr 奖章
  - 知名学生（infobox 明载）：Viatcheslav Mukhanov、Leonid Keldysh
  - 核心贡献清单（4–6 条）：①1950 与 Landau 共创金兹堡–朗道理论（超导唯象理论）；②引入序参量与金兹堡–朗道参数（I/II 类超导体判据）；③等离子体中电磁波传播理论（电离层）；④宇宙线起源理论；⑤过渡辐射与 undulator（波荡器）；⑥「金兹堡清单」——物理学未解问题清单（1971 年 17 题 → 1985 年 20 题 → 1999 年 30 题，2003 诺奖演讲展示）
  - 关键时间线（15–20 节点）：1916-10-04 生于莫斯科 → 1937 与 Olga Zamsha 结婚 → 1938 MSU 毕业 → 1940 Kandidat + 入列别杰夫研究所 → 1942 Doktor Nauk → 1944 加入苏共 → 1946 与 Nina 结婚 + 卫国战争奖章 → 1948–1952 Kurchatov 麾下氢弹研制 → 1950 金兹堡–朗道理论 → 1953 斯大林奖 → 1954 列宁勋章 → 1966 列宁奖 → 1968 创建 MIPT 教研室 → 1971 清单 17 题 → 1984 Smoluchowski 奖章 → 1987 ForMemRS → 1991 RAS 金章 → 1994/95 Wolf 奖 → 1995 Vavilov + 罗蒙诺索夫金章 → 1999 清单 30 题 → 2003 诺贝尔奖 + APS Fellow → 2006 一级祖国功绩勋章 → 2009-11-08 逝于莫斯科

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Vitaly_L._Ginzburg/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 20 世纪成品目录 Makefile，设 `MAIN=Vitaly_L._Ginzburg_zh`、`VIDEO_NAME=Vitaly_L._Ginzburg_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：Commons `Vitaly_Ginzburg.jpg`（1980 照）或 `Ginzburg_in_MSU.jpg`（诺奖演讲照）；404 则装饰圆占位

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | superconductivity | 超导电性 | 金兹堡–朗道理论，2003 诺奖核心 | 核心页 |
| 1 | theoretical physics | 理论物理 | infobox Fields 口径 | 概览页 |
| 2 | astrophysics | 天体物理 | 宇宙线起源理论、MIPT 天体物理教研室 | 天体页 |
| 3 | plasma physics | 等离子体物理 | 电磁波在等离子体（电离层）中的传播 | 等离子体页 |
| 4 | cosmic radiation | 宇宙辐射 | 宇宙线起源理论 | 天体页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> **只收 page.md 明载**；对手方 name_en 已查库，沿用库内/将建规范形式。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Igor Yevgenyevich Tamm | 师→生（博士导师） | 列别杰夫研究所博士导师，后继任其理论物理室主任，1958 诺奖得主 |
| colleague | Lev Landau | 无向 | 1950 共创金兹堡–朗道理论，引入序参量与 GL 参数 |
| colleague | Igor Kurchatov | 无向 | 1948–1952 在其领导下参与苏联氢弹研制 |
| co-honored | Alexei Abrikosov | 无向 | 2003 诺贝尔物理学奖共享（超导体理论） |
| co-honored | Anthony J. Leggett | 无向 | 2003 诺贝尔物理学奖共享（超流体理论） |
| advisor-student | Viatcheslav Mukhanov | Ginzburg → 学生 | infobox 明载博士生，宇宙学扰动理论 |
| advisor-student | Leonid Keldysh | Ginzburg → 学生 | infobox 明载博士生，凝聚态理论 |
| controversy | Trofim Lysenko | 无向 | 抵制李森科主义、使遗传学回归苏联的科学家群体成员 |
| spouse | Olga Ivanovna Zamsha | 无向 | 1937 结婚，1946 离婚，育 1 子 |
| spouse | Nina Ivanovna Ginzburg | 无向 | 1946 结婚，实验物理学家，1922–2019 |

- 入库注意：本人复用库内 stub `Vitaly Ginzburg`(id=2431, yaml name_en 沿用此形式回填 QID=Q104668)；Tamm 用库内 `Igor Yevgenyevich Tamm`(2189)、Landau 用 `Lev Landau`(2130)、Abrikosov 用库内 `Alexei Abrikosov`、Keldysh 复用 stub `Leonid Keldysh`(2450)；Mukhanov/Kurchatov/Lysenko/两位配偶新建 stub；Abrikosov/Leggett 关系与 batch 内 Abrikosov 篇互为镜像，撞 uq_rel 跳过即可。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：苏联深红、极低温、科学良知
- **配色**：苏联深红（主色，批内唯一）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `mainclr` 主色 — 苏联深红 `#8C1F28`
  - `badgeGL` 超导理论 — 暗金 `#B7950B`
  - `badgePlasma` 等离子体与电波 — 青 `#148F77`
  - `badgeAstro` 天体物理与宇宙线 — 深蓝 `#1A5276`
  - `badgeNuclear` 核计划年代 — 灰紫 `#6C3483`
- **背景母题**：柔和气泡——左右两域颜色渐变（正常态/超导态）以一条明亮边界分隔，呼应序参量

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍，底部状态栏给 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 金兹堡–朗道理论共创者 / Vitaly L. Ginzburg 1916–2009 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — GL 理论 / 等离子体电波 / 宇宙线起源 / 金兹堡清单
04  莫斯科早年 (1916–1940) — 犹太工程师家庭、1938 MSU 毕业、入列别杰夫研究所
05  Tamm 门下与战时岁月 (1940–1947) — 1940 Kandidat、1942 Doktor Nauk、两任婚姻
06  氢弹年代 (1948–1952) — Kurchatov 麾下、与 Tamm 的构想、被移出项目的转折
07  1950：金兹堡–朗道理论（核心贡献页）— 序参量、GL 方程、GL 参数判 I/II 类超导体（公式框放 GL 序参量方程概念式，page.md 载「complex set of equations」未给具体式，注明）
08  广播天体物理 — 等离子体中电磁波传播（电离层）、宇宙线起源、过渡辐射与 undulator
09  科学良知 — 抵制李森科主义、直言无神论、开放信件、晚年为人权与自由派发声
10  金兹堡清单 — 1971 年 17 题 → 1999 年 30 题，2003 诺奖演讲展示（列表页）
11  2003 诺贝尔物理学奖 — 三人共享格局页（Ginzburg+Abrikosov 超导 / Leggett 超流）
12  荣誉与认可 — Stalin 奖 1953 · Lenin 奖 1966 · Wolf 1994/95 · ForMemRS 1987 · Lomonosov 1995
13  遗产：从序参量到 MRI 与磁悬浮
14  结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式；每写完一页 `make` 并 `pdftoppm` 截图检查；金兹堡清单页用分栏小字号防溢出。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Ginzburg 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日双值 | frontmatter 有 1916-09-21 与 1916-10-04 两值；正文口径 **1916-10-04**（儒略历 09-21），入库与立传均用 10-04 |
| 博士导师双值 | frontmatter doctoral_advisor 列 Tamm + Landau，infobox 正文只写 **Igor Tamm**；入库只收 Tamm（advisor），Landau 以 1950 GL 理论合作写 colleague——勿给 Landau 建 advisor 关系 |
| 诺奖理由 | 导语引号原句 "pioneering contributions to the theory of superconductors and superfluids"；正文另有转述句（"behavior of matter at extremely low temperatures"），勿混用；官方口径以本引号句为准 |
| 三人格局 | Ginzburg+Abrikosov=超导、Leggett=超流；与 Leggett/Abrikosov 仅为 co-honored，禁写合作 |
| 氢弹角色 | 1948–1952 在 Kurchatov **领导下**参与氢弹研制、与 Tamm 各自提出构想；项目迁 Arzamas-16 后**未被准许随迁**、留莫斯科远程支持并受监视、渐被移出——勿写成「主持氢弹设计」或「参与 RDS-37 具体设计」 |
| Landau 关系 | 1950 GL 理论是合作共创；Landau 1941 起研究超流氦并于 1962 获诺奖是 Landau 本人工作，勿写成 Ginzburg 参与 |
| 序参量归属 | 序参量概念由 **Ginzburg** 引入（正文明载 "Ginzburg introduced the concept of an order parameter"），GL 参数用于判 I/II 类；勿全部归给 Landau |
| 李森科 | 表述为「帮助终结李森科统治的科学家群体之一员」，勿写成个人单挑 |
| 无神论与政治 | 直言无神论、批评教权、2009 年批评 FSB、为人权运动与 Sutyagin/Danilov 辩护——立传从简客观，引语只用 page.md 原文（如临终前 "I cannot believe in resurrection after death" 段），勿扩写政治评论 |
| 妻子 | 两任婚姻均明载；Nina 曾因诬陷入狱一年余（涉及 Stalin 叙事客观转述即可）；Nina 卒于 2019-05-19，晚于 Ginzburg 十年，时间线别混 |
| 学生 | 仅收 infobox 明载的 Mukhanov 与 Keldysh 两人 |
| 机构口径 | 列别杰夫物理研究所（FIAN）1940 起至终身；MIPT 教研室 1968 创建；主编《Uspekhi Fizicheskikh Nauk》——三条勿混 |
| 库内记录 | 本人 name_en 用库内 stub 形式 `Vitaly Ginzburg`（非 `Vitaly L. Ginzburg`），防分裂 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Ginzburg–Landau theory | 金兹堡–朗道理论 | 1950 共创，超导唯象理论 |
| order parameter | 序参量 | Ginzburg 引入 |
| Ginzburg criterion | 金兹堡判据 | 涨落判据 |
| type-I / type-II superconductor | I / II 类超导体 | GL 参数判据 |
| transition radiation | 过渡辐射 | 匀速源辐射理论 |
| undulator | 波荡器 | 同步辐射装置部件 |
| cosmic radiation | 宇宙辐射/宇宙线 | 起源理论 |
| ionosphere | 电离层 | 电磁波传播场景 |
| Uspekhi Fizicheskikh Nauk | 《物理学进展》（俄） | 主编期刊 |
| Kandidat / Doktor Nauk | 副博士 / 全博士 | 1940 / 1942 |
| Arzamas-16 | 阿尔扎马斯-16 | 核武器秘密城市 |
| Ginzburg's list | 金兹堡清单 | 未解问题清单，30 题 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（史诗 / 黑暗 / 推进）
- **匹配理由**: 「黑暗中的推进」匹配其人生双重暗面——苏联氢弹年代的保密与监视、战后直言无神论与李森科主义的科学黑暗时期，而他始终以理论之光穿行其中。
- **备选**（未采用）: PAST（已被本批 Abrikosov 选用）；Empire Collapse（苏联题材契合但气质过紧）。
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`
- 批内 BGM 不重复备案：Giacconi=The Invisible Light、Abrikosov=PAST、Ginzburg=Through the Darkness、Leggett=SEA、Gross=Savage。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Vitaly_L._Ginzburg/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 关系入库引擎（幂等） |
| `MySQL/data/Vitaly_L._Ginzburg.yaml` | yaml 数据文件 |

> **开始执行。每完成一步汇报。**
