# 物理学家立传提示词（Heike Kamerlingh Onnes）

> 本文件是 OpenPhysicist「人物专属立传提示词」，以 Kenneth G. Wilson 标杆结构为骨架，为 Heike Kamerlingh Onnes（1913 诺贝尔物理学奖，液氦与超导）定制。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分已按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Heike Kamerlingh Onnes（海克·卡末林·昂内斯）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇叙事重心是**"通往绝对零度的竞赛"与超导的偶然发现**，实验物理学家篇的样板。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Heike Kamerlingh Onnes（1853-09-21 生于荷兰格罗宁根 ~ 1926-02-21 逝于荷兰莱顿，享年 72 岁）
- **气质关键词**：**低温之王、实验巨匠、"通过测量达致知识"** —— 1913 诺贝尔物理学奖获奖理由：
  > "for his investigations on the properties of matter at low temperatures which led, inter alia, to the production of liquid helium"（因其对低温下物质性质的研究，这些研究最终促成了液氦的制备）
- **设计母题**：**温度阶梯（the ladder of cold）**。从 4.2 K 的沸点到 1.5 K 的极限，以逐级下降的温标、蓝色渐变与液氦雾气的视觉语言贯穿全篇。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Heike_Kamerlingh_Onnes/page.md`（Wikipedia 全文，事实基准已核对）
- **参考模板**：
  - 提示词标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 物理学家成品参照：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已随提示词同步入库 greatminds 库（MySQL），无需重复整理。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 本地 Wikipedia 已就位：`20th_century/20th_century/Heike_Kamerlingh_Onnes/` 下已有 `page.html` / `page.md` / `metadata.json` / `images.txt`（无需再下载）
- ⬜ **待下载头像**：images.txt 无正脸肖像（infobox「1913 年像」未入库）→ 用 Wikipedia REST API `page/summary` 查 infobox 原图名下载（404 则装饰圆占位）
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1853-09-21 生于 Groningen ~ 1926-02-21 逝于 Leiden，享年 72 岁
  - 国籍：荷兰
  - 父母：父 Harm Kamerlingh Onnes（砖厂主），母 Anna Gerdina Coers
  - 教育：1870 入格罗宁根大学（次年 B.Sc.）；1871–1873 海德堡大学师从 Robert Bunsen 与 Gustav Kirchhoff；1878 M.Sc.；1879 博士，论文《Nieuwe bewijzen voor de aswenteling der aarde》（地球自转的新证据）
  - 博士导师：Rudolf Adriaan Mees（frontmatter 明载）
  - 任职：1878 任 Delft Polytechnic 所长 Johannes Bosscha 的助理（1881/1882 代讲）；1882 起任莱顿大学实验物理与气象学教授；1904 创建大型低温实验室（今 Kamerlingh Onnes Laboratory）
  - 1908-07-10 首次液化氦：多级预冷 + Hampson–Linde 循环（基于 Joule–Thomson 效应），4.2 K；降压至约 1.5 K，为当时地球最低温
  - 1911-04-08 发现汞在 4.2 K 电阻消失（超导；初称 "supraconductivity"）；同日首次观察到氦浴的超流迹象
  - 氦气来源：早期自 monazite 加工，1911 起自 Welsbach 公司的 thorianite 副产品
  - 关键荣誉：Matteucci 1910、Rumford 1912、Nobel 1913、Franklin 1915；院士：荷兰皇家艺术与科学院 1883、美国哲学学会 1914、英国皇家学会外籍 1916、美国 NAS 1920
  - 知名学生（infobox 明载）：Jacob Clay、Wander Johannes de Haas、Johannes Kuenen、Frans Penning、Pieter Zeeman；学生兼实验室继任者 Willem Hendrik Keesom（1926 首次固化氦）
  - 其他：创造术语 enthalpy（焓）；月面环形山以他命名；超导发现 2011 年列为 IEEE Milestone；妹夫 Floris Verster、兄 Menso、外甥 Harm 均为画家
  - 家庭：1887 娶 Maria Adriana Wilhelmina Elisabeth Bijleveld，一子 Albert
  - 仪器现存莱顿 Boerhaave 博物馆；莱顿设备清单《Communications from the Kamerlingh Onnes Laboratory》

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用 `Heike_Kamerlingh_Onnes/` 并建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Heike_Kamerlingh_Onnes_zh`、`VIDEO_NAME=Heike_Kamerlingh_Onnes_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 肖像见第 0 步（REST API 回退）；插图取自 images.txt：`Leiden_-_Kamerlingh_Onnes_Building_-_Commemorative_plaque.jpg`（莱顿纪念铭牌）；液化氦装置照片可另行取自 Museum Boerhaave

### 第 4 步：研究领域 【模板通用，人物专属内容】

**Onnes 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | low-temperature physics | 低温物理 | 1913 诺奖核心 | 核心页 |
| 1 | superconductivity | 超导电性 | 1911 汞电阻消失 | 核心页 |
| 2 | cryogenics | 低温工程 | 1904 莱顿低温实验室 | 实验室页 |
| 3 | liquefaction of gases | 气体液化 | 1908-07-10 首液化氦 | 核心页 |
| 4 | experimental physics | 实验物理 | "通过测量达致知识"的定量传统 | 方法页 |

### 第 4.5 步：社会关系 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rudolf Adriaan Mees | 师→生（博士导师） | 格罗宁根大学博士导师，1879 论文地球自转 |
| advisor-student | Robert Bunsen | 师→生 | 1871–1873 海德堡大学求学师从 |
| advisor-student | Gustav Kirchhoff | 师→生 | 1871–1873 海德堡大学求学师从 |
| advisor-student | Pieter Zeeman | 生 | 博士生（infobox 明载） |
| advisor-student | Wander Johannes de Haas | 生 | 博士生（infobox 明载） |
| advisor-student | Jacob Clay | 生 | 博士生（infobox 明载） |
| advisor-student | Johannes Kuenen | 生 | 博士生（infobox 明载） |
| advisor-student | Frans Penning | 生 | 博士生（infobox 明载） |
| advisor-student | Willem Hendrik Keesom | 生 | 学生兼低温实验室继任主任，1926 首次固化氦 |
| spouse | Maria Bijleveld | 无向 | 1887 年结婚，一子 Albert |
| rival | James Dewar | 无向 | 液氦竞赛的主要竞争者（page.md 外部链接明载"the main competitor in the race to liquid helium"，两人有通信存世） |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：极寒、深蓝、精密
- **配色**：莱顿低温深蓝（主色 `#16325C`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 超导电性 — 冰蓝 `#3E92CC`
  - `badgeB` 液氦 — 群青 `#26418F`
  - `badgeC` 低温工程 — 钢青 `#1E7A8C`
  - `badgeD` 莱顿学派 — 暖金 `#C8963E`
- **背景母题**：自上而下逐级变深的温标色带与氦气泡，呼应"温度阶梯"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框）。
2. 封面明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项`。
3. 必须有身份信息页（左头像 + 右信息网格）。
4. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，14 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 低温之王 / Heike Kamerlingh Onnes 1853–1926 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 液氦 / 超导 / 莱顿低温实验室
04  格罗宁根与海德堡 (1853–1882) — Bunsen/Kirchhoff 门下、地转博士论文
05  莱顿教授与低温实验室 (1882–1908) — Bosscha 助理、1904 建室开门迎客
06  1908-07-10：液氦之夜（核心贡献页，无公式 → 概念图式：多级预冷温标阶梯）
07  1911-04-08：超导的发现 — 汞在 4.2 K 电阻消失、supraconductivity 旧称
08  氦从何处来 — monazite 与 thorianite、与 Welsbach 公司的交易
09  与 Dewar 的竞赛 — 液氢之后谁先到 4.2 K
10  莱顿学派与门生 — Zeeman、de Haas、Keesom（1926 首固化氦）
11  荣誉与认可 — Nobel 1913 · Rumford 1912 · 四国院士
12  遗产：从焓（enthalpy）到超导世纪 — IEEE Milestone、月面环形山
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`。
- 头部宏整体复用 `Kenneth_G_Wilson_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Onnes 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方措辞强调"低温物质性质研究 + 液氦制备"，**超导（1911）不在 1913 获奖理由中**，勿写成"因发现超导获奖" |
| 两个日期 | 液氦 1908-07-10；超导 1911-04-08（百年后笔记本才被解读），勿混 |
| 温度数值 | 液氦沸点 4.2 K（−269 °C）；降压后约 1.5 K 为当时地球最低温；汞超导转变 4.2 K，勿写成"1.5 K 发现超导" |
| 博士论文 | 1879 论文是**地球自转的证明**，勿写成低温主题 |
| 导师分层 | 博士导师 = Rudolf Adriaan Mees；Bunsen/Kirchhoff 是海德堡求学导师（"studied under"），勿写成博士导师 |
| 技术路线 | 液氦用 Hampson–Linde 循环 + Joule–Thomson 效应、多级预冷，勿写成"绝热膨胀" |
| Dewar 关系 | "主要竞争者"仅出自 page.md 外部链接标题，表述留有余地，勿杜撰冲突情节 |
| 超流表述 | 1911-04-08 同日观察到的氦浴现象是"超流的首次迹象"，勿写成"发现超流"（超流定名在后人） |
| 词汇遗产 | enthalpy（焓）一词系其创造，可写但注明"创造术语" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| superconductivity | 超导电性 | 旧称 supraconductivity |
| liquid helium | 液氦 | 4.2 K 沸点 |
| cryogenics | 低温工程/制冷学 | 与低温物理区分 |
| Hampson–Linde cycle | 汉普森–林德循环 | 节流液化回路 |
| Joule–Thomson effect | 焦耳–汤姆孙效应 | 液化原理 |
| boiling point | 沸点 | 液氦 4.2 K |
| superfluidity | 超流性 | 1911 仅为"首次迹象" |
| resistance | 电阻 | 汞丝 4.2 K 突降为零 |
| enthalpy | 焓 | Onnes 造词 |
| thorianite / monazite | 方钍石/独居石 | 氦气来源矿物 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（流动 / 平稳，`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`）
- **匹配理由**: "流动"匹配液氦、超流体与温度逐级下降的液态意象；平稳的叙事感匹配实验物理学家"以测量求知识"的沉静气质。
- **批内查重**: batch 2 内无人复用此曲。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Heike_Kamerlingh_Onnes/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Heike_Kamerlingh_Onnes.yaml` | 已入库的领域/关系数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
