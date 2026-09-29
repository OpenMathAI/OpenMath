# 物理学家立传提示词（John F. Clauser，2022 诺贝尔物理学奖）

> **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：John Francis Clauser（约翰·克劳泽），2022 诺贝尔物理学奖得主（首个 Bell 不等式实验检验）。
> **设计哲学**：骨架照搬 Kenneth_G_Wilson_zh.md 标杆；Clauser 的立传主线是「把 Bell 定理搬进实验室的第一人——从天体物理博士生到量子基础先锋」。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史。
- **本实例**：John Francis Clauser（约翰·弗朗西斯·克劳泽）。
- **设计哲学**：Clauser 兼具理论与实验——CHSH/CH 不等式是理论武器，1972 Freedman–Clauser 实验是判决性测量；立传强调「一个人的偏执如何让量子力学基础重新成为可实验的科学」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Francis Clauser（1942-12-01 生于美国加州帕萨迪纳，在世）
- **气质关键词**：**Bell 定理的实验开路人、CH 不等式的缔造者、光子粒子性的铁证提供者** —— 2022 诺贝尔物理学奖获奖理由（官方原文，page.md 载）：
  > "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science"（因纠缠光子实验、确立 Bell 不等式的违背并开创量子信息科学）
  - 注：2022 年奖由 Clauser、Alain Aspect、Anton Zeilinger 三人共享（等额，无半奖之分）。
- **设计母题**：**第一个实验（the first test）**。1972 年 Freedman–Clauser 实验是人类第一次对 Bell 定理的实验判决——视觉上可用「孤零零的一台光学平台 vs 弥漫的『局域实在论』迷雾」的对比母题。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/John_F._Clauser/page.md`
- **html/images**：**待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/John_F._Clauser`（第 0 步下载 html 与 infobox 肖像到本目录 `images/`）
- **参考模板**：
  - 物理学家标杆骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⬜ html 与 images **待下载**：`https://en.wikipedia.org/wiki/John_F._Clauser`
- 已核对 page.md，**事实基准如下**：
  - 生卒：1942-12-01 生于加州帕萨迪纳，在世
  - 国籍：美国
  - 家庭：父 Francis H. Clauser 为航空工程教授（在 Johns Hopkins 创立并主持航空系，后任 Caltech Clark Blanchard Millikan 工程讲座教授）；母 Catharine McMillan 为 Caltech 人文图书馆员，是 1951 诺贝尔化学奖得主 Edwin McMillan 的姐姐
  - 教育：Caltech 物理学士 1964（Dabney House 成员）；Columbia 物理硕士 1966、博士 1969（导师 Patrick Thaddeus）；博士论文《Measurement of the Cosmic Microwave Background by Optical Observations of Interstellar Molecules》（infobox 论文条目标 1970）
  - 任职机构（含年份）：UC Berkeley + Lawrence Berkeley 国家实验室博士后 1969–1975；Lawrence Livermore + Berkeley 研究物理学家 1975–1997；CO2 Coalition 董事会（2023 起，争议组织，见陷阱表）
  - 关键荣誉（含年份）：Clarivate Citation Laureates；Wolf Prize 2010（与 Aspect、Zeilinger）；**Nobel Prize in Physics 2022**（三人共享）
  - 核心贡献清单：
    1. **1972 与 Stuart Freedman 完成首个 CHSH-Bell 定理实验检验**——人类第一次实验观测到 Bell 不等式的违背
    2. **1974 与 Michael Horne 证明 Bell 定理的推广对所有局域实在论（objective local theories）构成严格约束**；提出 Clauser–Horne（CH）不等式与"CH 无增强假设"
    3. **1974 首次观测到光的亚泊松（sub-Poissonian）统计**（经由对经典电磁场 Cauchy–Schwarz 不等式的违背），首次无歧义证明光子的类粒子性
    4. 1976 完成世界上第二个 CHSH-Bell 定理实验检验
    5. 1973 起创办/发布通讯《Epistemological Letters》——因主流期刊不愿刊载量子力学哲学文章
  - 关键时间线（1942 帕萨迪纳出生 → 1964 Caltech BS → 1966 Columbia MA → 1969 Columbia PhD（CMB 测量论文）→ 1969–75 Berkeley/LBNL 博士后 → 1972 Freedman–Clauser 首验 → 1973 Epistemological Letters → 1974 CH 不等式 + 亚泊松光统计 → 1975–97 LLNL/Berkeley → 1976 世界第二次 CHSH 检验 → 2010 Wolf 奖 → 2022 诺贝尔奖 → 2023 CO2 Coalition 争议）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `John_F._Clauser/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Makefile`，设置 `MAIN=John_F._Clauser_zh`、`VIDEO_NAME=John_F._Clauser_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 下载 infobox 肖像到 `images/`（infobox 用 2024 年照）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum foundations | 量子力学基础 | Bell 检验、局域实在论约束 | 核心页 |
| 1 | quantum mechanics | 量子力学 | infobox Fields 载 | 概览页 |
| 2 | quantum optics | 量子光学 | 亚泊松光统计、光子类粒子性 | 光子页 |
| 3 | astrophysics | 天体物理 | 博士论文：星际分子光学观测 CMB | 博士页 |
| 4 | quantum information science | 量子信息科学 | 2022 诺奖理由"开创"领域 | 遗产页 |

- 入库：`MySQL/seed_person.py data/John_F._Clauser.yaml`（幂等；person_field 带 rank）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Patrick Thaddeus | 师→生（博士导师） | Columbia 博士导师（1969），CMB 测量论文 |
| colleague | Stuart Freedman | 无向 | 1972 年共同完成首个 CHSH-Bell 定理实验检验（时为 Berkeley 研究生） |
| colleague | Michael Horne | 无向 | 1974 年合作证明 Bell 定理推广、提出 Clauser–Horne（CH）不等式 |
| co-honored | Alain Aspect | 无向 | 2022 诺贝尔物理学奖共同得主；2010 Wolf Prize 亦三人共享 |
| co-honored | Anton Zeilinger | 无向 | 2022 诺贝尔物理学奖共同得主；2010 Wolf Prize 亦三人共享 |

- 入库：同一 yaml `relations` 段；仅收 page.md 明载关系（Shimony/Holt 仅以 CHSH 缩写出现，无合作叙事，不入库；Freedman 师承关系 page.md 未载 Claude 为其导师，只建 colleague）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：加州阳光、实验台的偏执、锈色金属
- **主色**：锈橙棕 `#8A3B12`（实验装置与倔强）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeBell` Bell 检验 — 靛蓝 `#4C5FD5`
  - `badgeCH` CH 不等式 — 青绿 `#0E7C7B`
  - `badgePhoton` 光子统计 — 琥珀 `#E07B30`
  - `badgeCMB` 天体物理 — 玫瑰 `#C4204F`
- **背景母题**：一台孤立光学平台发出的两束逆向光路穿过坐标网格（第一个 Bell 实验的仪式感），边缘散布"被证伪的局域隐变量"褪色散点

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — Bell 定理的实验开路人 / John F. Clauser 1942– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地、科学世家、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 1972 首验 / CH 不等式 / 亚泊松光统计 / 1976 第二次检验
04  早年：帕萨迪纳的科学世家 (1942–1964) — 父 Hopkins/Caltech 航空工程、母 McMillan 家族、Caltech BS
05  Columbia 博士：测量宇宙微波背景 (1964–1969) — Thaddeus 门下、星际分子光学观测
06  Berkeley 博士后与 1972 首验（核心贡献页）— Freedman–Clauser 实验、首个 Bell 不等式违背观测（概念图式：级联光源+双偏振分析器，page.md 无公式）
07  CHSH 与 CH 不等式 — 1974 与 Horne：局域实在论的普遍约束、无增强假设（概念图式）
08  亚泊松统计：光子的粒子性铁证 (1974) — Cauchy–Schwarz 违背、首次无歧义类粒子性
09  Epistemological Letters — 主流期刊不愿刊载量子哲学、私人通讯网络 (1973 起)
10  LLNL 岁月与 1976 第二次检验 — 1975–97 研究物理学家
11  荣誉年表 — Nobel 2022 · Wolf 2010 · Citation Laureates
12  争议：气候变化立场 (2023) — CO2 Coalition、客观一句带过（见陷阱表口径）
13  遗产：从偏执的检验到第二次量子革命
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Clauser 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 2022 奖三人**等额共享**（Clauser/Aspect/Zeilinger），勿写半奖 |
| 获奖理由措辞 | 用 "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science" 原文 |
| CHSH 缩写 | C=Clauser、H=Horne、S=Shimony、H=Holt；但四人如何形成 CHSH 的合作过程 page.md **无载**，勿编叙事；Shimony/Holt 不入关系库 |
| 首验 vs 二验 | 1972 Freedman–Clauser 是**世界第一个**实验检验；1976 是他本人的**世界第二个**；勿把 1976 写成"重复 1972" |
| 博士论文方向 | CMB 测量（天体物理）与量子基础无关；"为何转向 Bell 定理"的心路历程 page.md 无载，勿编"读到 Bell 论文豁然开朗"之类故事 |
| PhD 年份两说 | 正文作 1969，infobox 论文条目作 (1970)；PhD 年份以正文 1969 为准，论文年份存疑注记 |
| 母系家族 | 母 Catharine McMillan 是 **1951 诺贝尔化学奖**得主 Edwin McMillan 的姐姐——是"chemist 舅舅"不是物理学家；父 Francis H. Clauser 是航空工程教授，勿混 |
| 气候争议 | 2023 加入 CO2 Coalition、自称 "climate denier"、"there is no climate crisis" 引语 page.md 有载，其观点被描述为 pseudoscience——争议页**客观一句带过或整节省略**，禁引申评论、禁与量子基础工作混写 |
| 个人生活 | 无神论、青年吸烟致肺气肿仅 page.md 一句，立传不必展开；如用须中性转述 |
| Freedman 身份 | 1972 时为 **Berkeley 研究生**；Clauser 与其是合作者（colleague），page.md 未载师生关系，禁建 advisor-student |
| 在世口径 | 1942-12-01 生、在世，death_date 留白，勿编卒年 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bell's theorem | Bell 定理 | 勿与 Bell 不等式混用（定理→不等式是推论链） |
| CHSH inequality | CHSH 不等式 | 四人缩写，注意两 H 不同人 |
| CH inequality | CH 不等式 | Clauser–Horne，首个完全一般的实验要求 |
| local realism | 局域实在论 | 又称 objective local theories |
| no-enhancement assumption | 无增强假设 | CH 归约到 CHSH 的条件 |
| sub-Poissonian statistics | 亚泊松统计 | 光强统计量子性的标志 |
| Cauchy–Schwarz inequality | 柯西–施瓦茨不等式 | 经典电磁场约束，违背即非经典 |
| cosmic microwave background | 宇宙微波背景（CMB） | 博士论文主题 |
| Epistemological Letters | 《认识论通讯》 | 私人通讯刊物，勿译"书信集" |
| entangled photons | 纠缠光子 | 诺奖理由用语 |
| postdoctoral researcher | 博士后 | Berkeley/LBNL 1969–75 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（66k views，探索/史诗）
- **匹配理由**: "探索/远征" 直接对应"第一个实验检验"的开路者身份——在无人看好的量子基础荒原上蹚出一条实验路径；史诗感承载科学世家出身与 B 计划（CMB→量子基础）的转折叙事。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 复制为 `presentations/21th_century/John_F._Clauser/Expedition.wav`
- **备选**: Savage（强推进/紧张，匹配判决性实验）；Winds Of Freedom（英雄/史诗，匹配终审时刻）

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/John_F._Clauser/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
