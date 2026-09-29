# 物理学家立传提示词（OpenPhysicist 21 世纪批次：Ferenc Krausz）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主「人物专属立传提示词」，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Ferenc Krausz（费伦茨·克劳斯，2023 诺贝尔物理学奖三位得主之一，首个阿秒光源的研制者）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达，此两点为骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Ferenc Krausz（1962-05-17 生于匈牙利毛罗镇；在世，匈牙利/奥地利双国籍）
- **气质关键词**：**第一个阿秒光源的点燃者、电子运动的摄像师、马普量子光学所的掌舵人** —— 2023 诺贝尔物理学奖获奖理由（与 Pierre Agostini、Anne L'Huillier 共享）：
  > "for experimental methods that generate attosecond pulses of light for the study of electron dynamics in matter"（因产生阿秒光脉冲以研究物质中电子动力学的实验方法）
- **设计母题**：**电子快门（electron shutter）**。用阿秒脉冲给原子内电子运动「拍照」——视觉上可用「电子云 + 极短曝光快门」的概念图式表达。
- **本地数据源（已有）**：`physicist/presentations/21th_century/21st_century/Ferenc_Krausz/page.md`
- **待下载（第 0 步执行）**：`Ferenc_Krausz.html` 与 `images/` 肖像尚未下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Ferenc_Krausz`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对事实基准 【人物专属】

- page.md 已有本地，事实基准如下：
  - 生卒（1962-05-17 生于匈牙利人民共和国毛罗镇；在世）
  - 国籍（匈牙利 → 奥地利，双归属；frontmatter Austria + Hungary）
  - 教育（1981–1985 厄特沃什·罗兰大学理论物理 + 布达佩斯技术大学电气工程；1987–1991 维也纳工业大学博士，论文《Erzeugung ultrakurzer Lichtimpulse in Neodymium-Glaslasern》（钕玻璃激光中超短光脉冲的产生，1991）；1991–1993 同校 habilitation）
  - 博士导师（Arnold Schmidt，infobox 明载）
  - 任职机构（1996–1998 维也纳工业大学副教授、1999–2004 正教授（电气工程）；2003 起马普量子光学所（MPQ）所长；2004 慕尼黑大学（LMU）实验物理讲席教授；2025-11 香港大学物理系冠名讲座教授）
  - 关键荣誉（Leibniz 奖 2006；皇家摄影学会 Progress medal 2006；Optica Fellow 2009；Otto Hahn 奖 2013；Clarivate Citation Laureate 2015 与 Corkum；莱奥波尔迪纳院士 2016；Letokhov 奖章 2019；Wolf 物理学奖 2022 与 L'Huillier、Corkum；BBVA 前沿知识奖 2022 三人；2023 诺贝尔物理学奖；另有 King Faisal 奖、IEEE 量子电子学奖、维也纳科学奖、巴伐利亚马克西米利安科学与艺术勋章、匈牙利圣伊什特万勋章等 frontmatter 所载）
  - 知名学生（page.md 无载，禁写）
  - 核心贡献清单：
    1. 研究组产生并测量了第一个阿秒光脉冲（page.md 未载年份，禁写 2001）
    2. 用阿秒脉冲捕捉原子内部电子运动，标志阿托物理学（attophysics）的诞生
    3. 首个阿秒光源（infobox Known for）
    4. 2010 年 MPQ 实验揭示氖原子光电发射延迟理论与实验的偏差（2017 年由 L'Huillier 组解决）
  - 关键时间线（17 节点）：1962 生于毛罗 → 1981–1985 罗兰大学理论物理 + 布达佩斯技大电气工程 → 1987–1991 维也纳工业大学博士 → 1991–1993 habilitation → 1996–1998 副教授 → 1999–2004 正教授 → 2003 MPQ 所长 → 2004 LMU 讲席教授 → 2006 Leibniz 奖 + Progress medal → 2009 Optica Fellow → 2013 Otto Hahn 奖 → 2015 Clarivate 桂冠（与 Corkum） → 2016 莱奥波尔迪纳院士 → 2019 Letokhov 奖章 → 2022 Wolf 奖 + BBVA 奖 → 2023 诺贝尔奖 → 2025 香港大学冠名讲座教授

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Ferenc_Krausz/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品（如 `Serge_Haroche/Makefile`），设置 `MAIN=Ferenc_Krausz_zh`、`VIDEO_NAME=Ferenc_Krausz_zh`

### 第 3 步：收集图片 【人物专属】

- 下载 Krausz 2010 年 infobox 肖像（Commons `Special:FilePath` 或 Wikipedia REST API，250px 改 500px，curl 加 `-A "Mozilla/5.0"`，`file` 验证）；404 则装饰圆占位并注明

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | attosecond physics | 阿秒物理 | 2023 诺奖核心领域 | 封面、核心页 |
| 1 | ultrafast laser science | 超快激光科学 | 2022 Wolf 奖获奖领域 | 荣誉页 |
| 2 | laser physics | 激光物理 | 职业与博士论文主线 | 博士页 |
| 3 | electron dynamics | 电子动力学 | 诺奖 citation 用语 | 核心页 |
| 4 | theoretical physics | 理论物理 | 罗兰大学本科专业 | 早年页 |

- 入库：`cd MySQL && python3 seed_person.py data/Ferenc_Krausz.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；对手方无 qid 不编造。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arnold Schmidt | 师→生（博士导师） | 维也纳工业大学博士导师 |
| co-honored | Anne L'Huillier | 无向 | 2022 Wolf + 2022 BBVA + 2023 诺贝尔共同得主 |
| co-honored | Paul Corkum | 无向 | 2022 Wolf + 2022 BBVA 共同得主 |
| co-honored | Pierre Agostini | 无向 | 2023 诺贝尔物理学奖共同得主 |
| colleague | Paul Corkum | 无向 | 阿秒物理并肩者，2015 Clarivate 联合当选 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：极短与永恒、精确、突破
- **主色**：紫罗兰深色 `#52307C` + 诺奖香槟金 `C9A227`
- badgeA–D 四分类色：badgeAtto 阿秒光源 — 靛蓝 `#4C5FD5`；badgeLaser 激光科学 — 琥珀 `#E07B30`；badgeElec 电子动力学 — 青绿 `#0E7C7B`；badgeCareer 机构岁月 — 玫瑰 `#C4204F`
- **背景母题**：单发极短闪光（宽幅渐暗背景中一道极窄亮条），呼应"从连续激光中切出第一个阿秒脉冲"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏 `国籍 | 机构 | 主要奖项` 三要素（国籍写 Hungary / Austria）。
3. 必须有身份信息页：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md infobox。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 首个阿秒光源的研制者 / Ferenc Krausz 1962– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 首个阿秒光源 / 电子运动成像 / attophysics 诞生
04  早年：匈牙利双线学业 (1962–1985) — 毛罗镇、罗兰大学理论物理、布达佩斯技大电气工程
05  维也纳工业大学 (1987–1999) — 钕玻璃激光超短脉冲博士 1991、habilitation 1993、副教授
06  从维也纳到加兴 (2003–2004) — MPQ 所长 + LMU 实验物理讲席
07  第一个阿秒光脉冲（核心贡献页一）— 产生并测量、attophysics 诞生（概念图式，年份禁写）
08  给电子运动拍照（核心贡献页二）— 诺奖 citation 原句、阿秒"快门"
09  2010 氖原子光电发射延迟之争 — MPQ 实验与理论偏差、2017 L'Huillier 组 shake-up 电子解决
10  荣誉矩阵（高斯表格版式）— Leibniz 2006 / Otto Hahn 2013 / Wolf 2022 / BBVA 2022 / Nobel 2023
11  2023 诺贝尔物理学奖 — 三人共享、citation 原句
12  新篇章：香港大学 (2025–) — 冠名讲座教授
13  遗产：attophysics 的建制者
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）整体复用同目录成品骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Krausz 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 首个阿秒脉冲年份 | page.md 只说"generated and measured the first attosecond light pulse"，未载年份，禁写 2001（须另行核实后加注） |
| 双重教授职位 | 2003 MPQ 所长与 2004 LMU 讲席是两条独立任命，勿合并写成"2004 年起" |
| Wolf 奖三人 | 2022 Wolf 与 L'Huillier、Corkum 共享；2023 Nobel 是与 L'Huillier、Agostini 共享——两个"三人组"不同（Corkum 无诺奖、Agostini 无 Wolf），勿混 |
| 维也纳两段学位 | MSc、PhD、Dr. habil. 都在 TU Wien；本科理论物理在罗兰大学、MSc 电气工程在布达佩斯技大，勿错位 |
| 论文标题 | 德文原题《Erzeugung ultrakurzer Lichtimpulse in Neodymium-Glaslasern》，中文意译须注明"钕玻璃激光器" |
| 国籍表述 | 出生时为匈牙利人民共和国；获奖时匈牙利/奥地利双国籍，frontmatter 两国有载，勿只写其一 |
| 香港大学 | 2025 年 11 月起任港大物理系冠名讲座教授（Chair Professor），勿写"全职迁港" |
| 荣誉取舍 | 荣誉过多，幻灯片只列 page.md 荣誉节明载的年份条目，frontmatter 无年份的奖项不标年份 |
| 双本科 | 1981–1985 罗兰大学理论物理与布达佩斯技大电气工程是**并行双线**，勿写成先后顺序 |
| 荣誉缺口 | Clarivate Citation Laureate 2015 是"预测获奖"榜单而非奖项本身，表述勿与正式奖混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| attosecond | 阿秒 | 10⁻¹⁸ 秒 |
| attophysics | 阿托物理学 | page.md 用 attophysics/attosecond science 两写法，正文统一阿秒物理 |
| attosecond light pulse | 阿秒光脉冲 | 诺奖 citation 用语 |
| electron dynamics | 电子动力学 | 勿写"电子动态" |
| habilitation | 特许任教资格 | 德语区 Dr. habil.，勿译"博士后" |
| Max Planck Institute of Quantum Optics | 马普量子光学研究所 | 简称 MPQ，加兴（Garching） |
| Neodymium-Glas laser | 钕玻璃激光器 | 论文主题 |
| Max Born | — | 与 L'Huillier 篇 Max Born Award 无关，勿混 |
| Garching | 加兴 | MPQ 所在地，勿写"慕尼黑市内" |
| attoworld.de | — | 其课题组主页，备用信息源 |
| few-cycle pulse | 少周期脉冲 | 博士论文超短脉冲脉络的技术背景 |
| LMU Munich | 慕尼黑大学 | Ludwig-Maximilians-Universität，勿与 TU München 混淆 |
| 170 as | — | L'Huillier 组 2003 年纪录，与 Krausz 篇无直接关联，勿混入 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（inspiring-electronic 合辑）
- **风格**：科幻 / 史诗 / 上升
- **匹配理由**："开创性成果、升华"匹配"人类第一次点亮阿秒光源"的里程碑属性；上升感匹配从匈牙利小镇到加兴、再到 2023 诺奖的纵向轨迹。
- **本地路径**：`music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **备选** (未采用):
  - ★★ Last Hope — "革命性突破/高潮"匹配首个阿秒光源，但戏剧性浓于其沉稳的工程师气质
  - ★ Pathfinder — "探索/远征"匹配从匈牙利到加兴的远征式轨迹，但张力不足
- **批内去重**：本曲在本批（batch 13）内不与 Agostini / L'Huillier / Hopfield / Hinton 重复。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Ferenc_Krausz/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Ferenc_Krausz.yaml` | 社会关系 + 领域入库 yaml |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
