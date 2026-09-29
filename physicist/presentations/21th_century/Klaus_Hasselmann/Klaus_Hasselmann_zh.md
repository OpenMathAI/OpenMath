# 物理学家立传提示词（Klaus Hasselmann，2021 诺贝尔物理学奖）

> **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Klaus Ferdinand Hasselmann（克劳斯·哈塞尔曼），2021 诺贝尔物理学奖得主（气候物理建模）。
> **设计哲学**：物理学家立传必须有「身份信息页」与「研究领域结构化表达」，骨架照搬 Kenneth_G_Wilson_zh.md 标杆。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史。
- **本实例**：Klaus Ferdinand Hasselmann（克劳斯·费迪南德·哈塞尔曼）。
- **设计哲学**：Hasselmann 是从流体力学/海洋波浪「转行」气候物理的建模大师——立传主线是「随机性如何连接天气与气候」，强调跨领域方法迁移（费曼图形式主义 → 经典随机波场 → 气候随机强迫）。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Klaus Ferdinand Hasselmann（1931-10-25 生于德国汉堡，在世）
- **气质关键词**：**随机气候建模的开创者、海洋波浪的方程诗人、人为气候变化指纹的侦测者** —— 2021 诺贝尔物理学奖获奖理由（官方原文，page.md 载）：
  > "for groundbreaking contributions to the physical modeling of earth's climate, quantifying variability and reliably predicting global warming"（因其对地球气候物理建模、量化变率并可靠预测全球变暖的开创性贡献）
  - 注：2021 年奖一半授 Manabe 与 Hasselmann（气候建模），另一半授 Giorgio Parisi（复杂系统）。
- **设计母题**：**噪声与信号（noise → signal）**。Hasselmann 模型的核心是「海洋这个长记忆系统把白噪声天气强迫积分成红噪声气候信号」，指纹法则从强变率背景中提取系统性变暖信号——视觉上可用白噪声散点渐变为红噪声轨迹、再浮现清晰趋势线的母题。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Klaus_Hasselmann/page.md`
- **html/images**：**待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Klaus_Hasselmann`（第 0 步下载 html 与 infobox 肖像到本目录 `images/`）
- **参考模板**：
  - 物理学家标杆骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⬜ html 与 images **待下载**：`https://en.wikipedia.org/wiki/Klaus_Hasselmann`
- 已核对 page.md，**事实基准如下**：
  - 生卒：1931-10-25 生于汉堡（魏玛共和国），在世
  - 国籍：德国（1934–1949 童年随父母流亡英国，英语是其第一语言）
  - 父亲：Erwin Hasselmann，经济学家/记者/出版人，1920 年代起为德国社会民主党（SPD）活跃分子，1934 年全家为躲避纳粹迫害移民英国，居 Welwyn Garden City（非犹太人，但生活在德裔犹太移民社区，受英国贵格会帮助）
  - 教育：1949 A-levels（剑桥高中证书）；1949–1950 机械工程实践课程；1950 入汉堡大学物理与数学，1955 以各向同性湍流论文毕业（Diplom）；1955–1957 哥廷根大学 + 马普流体力学研究所博士，论文《Über eine Methode zur Bestimmung der Reflexion und Brechung von Stoßfronten und von beliebigen Wellen kleiner Wellenlängen an der Trennungsfläche zweier Medien》（1957）；1963 获物理学特许任教资格（Habilitation）
  - 博士导师：Walter Tollmien（page.md infobox 明载）
  - 任职机构（含年份）：汉堡大学助理教授 1957–1961；UCSD Scripps 海洋学研究所（IGPP）助理/副教授 1961–1964；汉堡大学地球物理与行星物理教授 1966 起；剑桥大学访问教授 1967–1968；Woods Hole 海洋研究所 Doherty 教授 1970–1972；汉堡大学理论地球物理教授 1972、地球物理研究所所长；**马普气象研究所创始所长 1975-02–1999-11**；德国气候计算中心（DKRZ）科学主任 1988-01–1999-11；European Climate Forum（今 Global Climate Forum）2001 与 Carlo Jaeger 共同创立、任副董事长至 2018
  - 关键荣誉（含年份）：Nobel 2021；BBVA Frontiers of Knowledge Award（气候变化类）2009；Sverdrup Gold Medal（美国气象学会）1971；Symons Memorial Medal（皇家气象学会）1997；Vilhelm Bjerknes Medal（欧洲地球物理学会）2002；Italgas/ENI 环境科学奖 1996；Körber 欧洲科学奖；James B. Macelwane Medal；德国联邦十字勋章指挥官级；AGU Fellow
  - 知名学生：Mojib Latif（page.md 明载 "was one of his PhD students"）
  - 配偶：Susanne Hasselmann（née Barthe），数学家，1957 年结婚，曾任马普气象研究所资深科学家，育有三子女
  - 核心贡献清单：
    1. **Hasselmann 模型（随机气候强迫理论）**：长记忆系统（海洋）对随机天气强迫的积分把白噪声变为红噪声，无需特殊假设解释气候中普遍存在的红噪声信号（1976 Tellus 经典论文）
    2. **海浪非线性相互作用**：把费曼图形式主义移植到经典随机波场，奠定海浪预报科学基础
    3. **人为气候变化「指纹法」**：用最优线性滤波从强气候变率中提取系统性变暖信号
    4. 跨领域方法迁移：因海浪工作重拾量子场论兴趣（"从后门进入量子场论"）
    5. 综合评估模型（integrated assessment）与气候政策研究
  - 关键时间线（1931 汉堡出生 → 1934 移英 → 1949 返汉堡 → 1955 汉堡大学 Diplom → 1957 哥廷根博士 → 1957–61 汉堡助理教授 → 1961–64 Scripps → 1963 Habilitation → 1966 汉堡教授 → 1967–68 剑桥访问 → 1970–72 Woods Hole → 1972 理论地球物理教授 → 1975 创立马普气象研究所 → 1976 随机气候模型 → 1988 DKRZ → 1993 最优指纹论文 → 2001 共创 European Climate Forum → 2009 BBVA → 2021 诺贝尔奖）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Klaus_Hasselmann/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Makefile`，设置 `MAIN=Klaus_Hasselmann_zh`、`VIDEO_NAME=Klaus_Hasselmann_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 下载 infobox 肖像到 `images/`（Commons `Special:FilePath/<文件名>?width=600`，404 则经 Wikipedia REST API `page/summary` 查实际文件名；再 404 用装饰圆占位）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | climate model | 气候模型 | 地球气候物理建模，2021 诺奖核心 | 核心页 |
| 1 | climate variability | 气候变率 | Hasselmann 模型解释红噪声信号 | 核心页 |
| 2 | ocean waves | 海浪 | 非线性相互作用、费曼图形式主义移植 | 海浪页 |
| 3 | stochastic processes | 随机过程 | 随机强迫理论（白噪声→红噪声） | 随机模型页 |
| 4 | climate change | 气候变化 | 指纹法检测人为变暖信号 | 指纹页 |

- 入库：`MySQL/seed_person.py data/Klaus_Hasselmann.yaml`（幂等；person_field 带 rank）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter Tollmien | 师→生（博士导师） | 哥廷根大学博士导师（1957） |
| advisor-student | Mojib Latif | Hasselmann→学生 | 博士生（page.md 明载） |
| co-honored | Syukuro Manabe | 无向 | 2021 诺贝尔物理学奖共同得主（气候物理建模一半） |
| co-honored | Giorgio Parisi | 无向 | 2021 诺贝尔物理学奖共同得主（另一半授复杂系统） |
| spouse | Susanne Hasselmann | 无向 | 数学家（née Barthe），1957 年结婚，马普气象研究所资深科学家 |

- 入库：同一 yaml `relations` 段；仅收 page.md 明载关系，无载禁写

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深海、流动、随机中的秩序
- **主色**：深海青 `#0F5257`（海洋与气候）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeClimate` 气候建模 — 海蓝 `#2E86AB`
  - `badgeWave` 海浪 — 琥珀 `#E07B30`
  - `badgeStoch` 随机过程 — 玫瑰 `#C4204F`
  - `badgeFingerprint` 指纹法 — 橄榄 `#6B8E23`
- **背景母题**：白噪声散点渐变为红噪声轨迹（随机小圆渐聚成波浪形趋势带），呼应设计母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 随机气候建模开创者 / Klaus Hasselmann 1931– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地、流亡英国童年、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 随机气候模型 / 海浪 / 指纹法 / 综合评估
04  早年：汉堡与伦敦之间的童年 (1931–1949) — 父亲 SPD、1934 流亡、Welwyn Garden City、英语第一语言
05  求学：从机械工程到哥廷根博士 (1949–1957) — 汉堡大学湍流论文、冲击波反射折射博士论文
06  美国岁月：Scripps 与 Woods Hole (1961–1972) — 地球物理教授、剑桥访问
07  海浪的非线性相互作用 — 费曼图形式主义移植到随机波场（概念图式页，page.md 无具体公式）
08  Hasselmann 模型：天气是噪声，气候是信号（核心贡献页）— 白噪声→红噪声，重粒子受随机撞击类比
09  指纹法：从变率中揪出人为变暖 — 最优线性滤波、多元时空信号提取
10  建所与计算：马普气象研究所与 DKRZ — 1975 创始所长、1988 DKRZ 科学主任
11  荣誉与认可 — Nobel 2021 · BBVA 2009 · Sverdrup 1971 · Bjerknes 2002
12  气候政策与公众声音 — European Climate Forum、"问题完全可以解决"引语
13  遗产：从随机强迫到气候归因科学
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hasselmann 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 2021 奖一半授 Manabe+Hasselmann（气候建模），**另一半授 Parisi（复杂系统）**；Hasselmann 与 Parisi 是同届共同得主但工作方向不同，勿写成"三人共同完成气候建模" |
| 获奖理由措辞 | 用 page.md 载的 "physical modeling of earth's climate, quantifying variability and reliably predicting global warming"；勿自行改写为"证明全球变暖由人类引起" |
| 国籍口径 | 德国；1934–1949 童年流亡英国是重要经历（父亲 SPD 背景），勿省略也勿写成"英德双重国籍" |
| 博士论文语言 | 论文题目为德文（冲击波与波的反射折射），勿译成湍流——湍流是 1955 汉堡大学 Diplom 论文题目 |
| 机构归属 | 马普气象研究所是 Hasselmann **1975 年参与创立并任创始所长**（至 1999）；勿写成"马普流体力学研究所"（那是他读博的单位） |
| Hasselmann 模型 | 核心是"海洋（长记忆系统）积分随机天气强迫，白噪声→红噪声"；勿写成"预报天气"——它解释的是气候变率统计性质 |
| 指纹法 | 是"检测（detection）与归因（attribution）"的统计方法（最优滤波），勿写成直接观测证据 |
| 同名区分 | 配偶 Susanne Hasselmann 是数学家（née Barthe），与学生 Mojib Latif 勿混淆；合作者 Carlo Jaeger（European Climate Forum 共同创立人）是页内人名但无师生/合作论文关系，勿入库 |
| 引语红线 | "I felt very happy in England"、量子场论"从后门进入"、气候可解性三处引语 page.md 有英文原文可引；其余一律转述 |
| 在世口径 | 1931 年生、在世，生卒页 death_date 留白，勿编卒年 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| stochastic climate forcing | 随机气候强迫 | 非"随机气候预报" |
| red noise / white noise | 红噪声/白噪声 | 频谱颜色隐喻，需图示 |
| Hasselmann model | Hasselmann 模型 | 长记忆系统积分随机强迫 |
| fingerprint method | 指纹法 | 最优滤波信号检测 |
| detection and attribution | 检测与归因 | 气候变化科学标准术语对 |
| non-linear wave interaction | 非线性波浪相互作用 | 海浪谱演化 |
| Feynman diagram formalism | 费曼图形式主义 | 移植到经典随机波场 |
| integrated assessment | 综合评估 | 气候-经济耦合模型 |
| Habilitation | 特许任教资格 | 德语学术制度，勿译"博士后" |
| Max Planck Institute for Meteorology | 马普气象研究所 | 他创立的单位，区别于流体力学所 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（75k views，流动/平稳）
- **匹配理由**: "流动/平稳" 匹配海洋学家的母题——海浪、随机强迫、长记忆海洋；平稳叙事节奏贴合"噪声中见信号"的纪录片式立传主线（汉堡→伦敦→汉堡→Scripps→马普所，跨大西洋的流动人生）。
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → 复制为 `presentations/21th_century/Klaus_Hasselmann/SEA.wav`
- **备选**: The Flow of Time（时间感/纪录片，匹配气候时间尺度）；The Invisible Light（纪录片/稳重）

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Klaus_Hasselmann/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
