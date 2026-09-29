# 物理学家立传提示词（Alain Aspect，2022 诺贝尔物理学奖）

> **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Alain Jean Aspect（阿兰·阿斯佩），2022 诺贝尔物理学奖得主（纠缠光子实验）。
> **设计哲学**：骨架照搬 Kenneth_G_Wilson_zh.md 标杆；Aspect 的立传主线是「用一个实验回答爱因斯坦——局域实在论的终审」。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史。
- **本实例**：Alain Jean Aspect（阿兰·让·阿斯佩）。
- **设计哲学**：Aspect 是实验量子光学大师——从 Bell 不等式检验到激光冷却再到单光子物理，立传强调「实验物理学家如何把思想实验变成判决性测量」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Alain Jean Aspect（1947-06-15 生于法国洛特-加龙省阿让，在世）
- **气质关键词**：**Bell 不等式的终审法官、纠缠光子的驯兽师、量子信息科学的先驱** —— 2022 诺贝尔物理学奖获奖理由（官方原文，page.md 载）：
  > "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science"（因纠缠光子实验、确立 Bell 不等式的违背并开创量子信息科学）
  - 注：2022 年奖由 Aspect、John Clauser、Anton Zeilinger 三人共享（等额，无半奖之分）。
- **设计母题**：**纠缠对（entangled pair）**。两个偏振关联的光子向相反方向飞去、无论相距多远仍保持关联——视觉上可用「从中心光源分出的两条光线与关联偏振箭头」呼应 EPR 纠缠。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Alain_Aspect/page.md`
- **html/images**：**待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Alain_Aspect`（第 0 步下载 html 与 infobox 肖像到本目录 `images/`；正文另有多张活动照可选插图）
- **参考模板**：
  - 物理学家标杆骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⬜ html 与 images **待下载**：`https://en.wikipedia.org/wiki/Alain_Aspect`
- 已核对 page.md，**事实基准如下**：
  - 生卒：1947-06-15 生于阿让（Agen, Lot-et-Garonne），在世
  - 国籍：法国
  - 教育：ENS Cachan（今属巴黎-萨克雷大学）毕业；1969 通过物理教师会考（agrégation）；1971 获 Orsay 高等光学学院（École supérieure d'optique，后为 Institut d'Optique Graduate School / 巴黎-南大学）博士学位，论文《Contribution à l'étude de la spectrographie de Fourier par holographie》（全息傅里叶光谱）；随后以替代兵役形式在喀麦隆任教三年；1983 在巴黎-南大学答辩国家博士（doctorat d'État，等同特许任教资格），论文《Trois tests expérimentaux des inégalités de Bell par mesure de corrélation de polarisation de photons》
  - 博士导师：Serge Lowenthal（infobox 明载，1971 博士）
  - 任职机构（含年份）：高等光学学院副院长（至 1994）；CNRS 研究主任；École polytechnique 教授；Institut d'Optique（巴黎-萨克雷大学）；Kastler-Brossel 实验室（激光冷却/BEC 阶段）；香港城市大学香港高等研究院
  - 关键荣誉（含年份）：Prix Servant 1983；ICO 奖 1985；Holweck Medal 1991；Max Born Award 1999；Gay-Lussac–Humboldt Prize 1999；**CNRS 金质奖章 2005**；**Wolf Prize 2010**（与 Clauser、Zeilinger）；Albert Einstein Medal 2012；Herbert Walther Award 2012；2013 一年三奖——Niels Bohr 国际金奖 + UNESCO Niels Bohr 奖章 + Balzan Prize（量子信息处理与通信）+ Frederic Ives Medal；荣誉军团骑士 2005 → 军官 2014 → 司令官 2022；ForMemRS 2015；**Nobel Prize in Physics 2022**；荣誉博士学位一长串（蒙特利尔 2006、ANU 2008、Heriot-Watt 2008、Glasgow 2010、Haifa 2011、Waterloo 2014、香港城市 2018、Sherbrooke 2023、Minho 2024、台大 2025）；**2025-06-26 当选法兰西学术院（Académie Française）**
  - 核心贡献清单：
    1. **Aspect 实验（1980–1982）**：三组 Bell 不等式实验检验（CHSH 版本），以快速切换偏振分析器关闭局域性漏洞——继 Freedman–Clauser 1972 首个实验之后的关键支持
    2. 激光冷却中性原子（Kastler-Brossel 实验室）与玻色–爱因斯坦凝聚
    3. 单光子波粒二象性的首次实验演示（ForMemRS 证书明载）
    4. 共同发明速度选择相干布居囚禁（VSCOP）技术
    5. 首次在同等条件下比较费米子与玻色子的 Hanbury Brown–Twiss 关联
    6. 首次在超冷原子系统中演示 Anderson 局域化
  - 关键时间线（1947 阿让出生 → 1969 agrégation → 1971 Orsay 博士（全息光谱）→ 1971–74 喀麦隆任教 → 1970s 末转 Bell 检验 → 1980–82 Aspect 实验 → 1983 国家博士答辩 → 至 1994 高等光学学院副院长 → 1990s 激光冷却 → 2005 CNRS 金奖 → 2010 Wolf 奖 → 2013 Niels Bohr+Balzan → 2015 ForMemRS → 2022 诺贝尔奖 → 2022 荣誉军团司令官 → 2025 法兰西学术院）
  - 其他：小行星 33163 Alainaspect（1998 年发现，2019-11-08 正式命名）以其命名

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Alain_Aspect/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Makefile`，设置 `MAIN=Alain_Aspect_zh`、`VIDEO_NAME=Alain_Aspect_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 下载 infobox 肖像到 `images/`（infobox 用 2016 年照；2013 高等光学学院照、2013 布达佩斯照可作插图）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum optics | 量子光学 | Aspect 实验、单光子物理 | 核心页 |
| 1 | quantum entanglement | 量子纠缠 | Bell 不等式违背实验 | Bell 检验页 |
| 2 | laser cooling | 激光冷却 | 中性原子冷却、Lévy 统计 | 冷原子页 |
| 3 | atomic physics | 原子物理 | BEC、Anderson 局域化 | 冷原子页 |
| 4 | quantum information science | 量子信息科学 | 诺奖理由"开创"的领域 | 遗产页 |

- 入库：`MySQL/seed_person.py data/Alain_Aspect.yaml`（幂等；person_field 带 rank）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Serge Lowenthal | 师→生（博士导师） | Orsay 高等光学学院博士导师（1971） |
| co-honored | John F. Clauser | 无向 | 2022 诺贝尔物理学奖共同得主；2010 Wolf Prize 亦三人共享 |
| co-honored | Anton Zeilinger | 无向 | 2022 诺贝尔物理学奖共同得主；2010 Wolf Prize 亦三人共享 |

- 入库：同一 yaml `relations` 段；仅收 page.md 明载关系（Freedman 仅"1972 首个实验"叙述、Cohen-Tannoudji 仅书目合著，均不入库）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：法兰西蓝、光的精确、关联之美
- **主色**：法兰西蓝 `#2A4B7C`（光学与理性）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeBell` Bell 检验 — 靛蓝 `#4C5FD5`
  - `badgePhoton` 单光子 — 青绿 `#0E7C7B`
  - `badgeCool` 激光冷却 — 琥珀 `#E07B30`
  - `badgeQInfo` 量子信息 — 玫瑰 `#C4204F`
- **背景母题**：中心光源分出两条光线，偏振箭头随距离保持关联（EPR 纠缠对视觉化），叠加干涉条纹

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — Bell 不等式的终审法官 / Alain Aspect 1947– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地、教育双学位、师承、任职、荣誉、核心领域）
03  核心贡献概览 — Aspect 实验 / 激光冷却 / 单光子 / 量子信息
04  早年：从阿让到 ENS Cachan (1947–1969) — agrégation 1969
05  Orsay 博士与喀麦隆岁月 (1971–1974) — 全息傅里叶光谱论文、替代兵役任教
06  Aspect 实验（核心贡献页）— 1980–82 三组 Bell 检验、快速切换分析器关闭局域性漏洞（概念图式：CHSH 关联测量示意，page.md 无公式）
07  EPR 之问与 Bell 定理 — 爱因斯坦"幽灵般的超距作用"、Freedman–Clauser 1972 首验背景
08  从纠缠到冷原子 — Kastler-Brossel 实验室、激光冷却、BEC、Lévy 统计（与 Cohen-Tannoudji 合著书）
09  单光子的波粒二象性与 HBT 关联 — ForMemRS 证书载四项"第一"
10  荣誉年表 — Nobel 2022 · Wolf 2010 · CNRS 金奖 2005 · Balzan 2013 · 荣誉军团三级
11  法兰西学术院与写作 (2025) — Einstein 与量子革命三部曲著作
12  遗产：量子信息科学的开端 — 从基础检验到第二次量子革命
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Aspect 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 2022 奖三人**等额共享**（Aspect/Clauser/Zeilinger），与 2021 年"一半/一半"结构不同，勿写半奖 |
| 获奖理由措辞 | 用 "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science" 原文；勿自行改写 |
| 首个 Bell 实验归属 | 首个实验是 **Freedman–Clauser 1972**；Aspect 实验是"继其后"的关键支持并部分关闭局域性漏洞；结果"并非完全结论性"（仍有漏洞允许局域实在论解释），勿夸大为"一锤定音" |
| 两个学位 | 1971 博士论文是**全息傅里叶光谱**（与 Bell 无关）；Bell 检验是 1983 **国家博士（doctorat d'État）**论文，实验在其间 1980–82 完成——两个论文/年代勿混 |
| 喀麦隆三年 | 替代强制性兵役的任教，勿写成"博士后"或"访问学者" |
| 两个"法兰西学院" | 2025 当选的是**法兰西学术院（Académie Française，40 席文学语言院）**，不是法国科学院（Académie des sciences，他 2003 前后已任成员）；勿混淆 |
| 博士导师 | Serge Lowenthal 仅 infobox 一行，无其他叙事，勿展开其生平 |
| ForMemRS 证书 | 2015 皇家学会当选证书引语 page.md 有英文原文（四项"第一"），可直接引用；勿据此扩写未载细节 |
| 书目合著 | 与 Grynberg/Fabre、Bardou/Bouchaud/Cohen-Tannoudji 的合著仅书目证据，不入关系库；书影可作插图 |
| 在世口径 | 1947-06-15 生、在世，death_date 留白，勿编卒年 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bell inequalities | Bell 不等式 | 勿译"贝尔不等式"外的随意变体 |
| CHSH | CHSH 情形 | Clauser–Horne–Shimony–Holt 四人缩写 |
| locality loophole | 局域性漏洞 | 快速切换分析器部分关闭 |
| entangled photons | 纠缠光子 | 级联衰变产生的光子对 |
| EPR paradox | EPR 悖论 | Einstein–Podolsky–Rosen |
| doctorat d'État | 国家博士 | 法国旧制最高学位，近似 Habilitation |
| agrégation | 教师会考 | 法国高教资格考试，勿译"博士资格考试" |
| laser cooling | 激光冷却 | 中性原子 |
| Hanbury Brown–Twiss | HBT 关联 | 强度干涉，量子类比 |
| velocity-selective coherent population trapping | 速度选择相干布居囚禁 | VSCOP，共发明 |
| Anderson localization | 安德森局域化 | 超冷原子系统首演 |
| quantum information science | 量子信息科学 | 诺奖理由用语 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（2:34，纪录片/电影/稳重）
- **匹配理由**: "看不见的光" 直接呼应纠缠光子与量子光学的母题——光既是实验对象又是隐喻；纪录片质感贴合"思想实验→判决性测量"的立传主线。
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav` → 复制为 `presentations/21th_century/Alain_Aspect/TheInvisibleLight.wav`
- **备选**: Winds Of Freedom（英雄/史诗，匹配终审时刻）；Ascension（上升/科幻，匹配量子革命）

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Alain_Aspect/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
