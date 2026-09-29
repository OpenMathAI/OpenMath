# 物理学家立传提示词（OpenPhysicist 21 世纪批次：Pierre Agostini）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主「人物专属立传提示词」，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Pierre Agostini（皮埃尔·阿戈斯蒂尼，2023 诺贝尔物理学奖三位得主之一，阿秒物理先驱）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达，此两点为骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Pierre Agostini（1941-07-23 生于突尼斯城，时为法国保护地突尼斯；在世）
- **气质关键词**：**阈上电离的首次观测者、阿秒脉冲串的制备者、强场激光物理的铺路人** —— 2023 诺贝尔物理学奖获奖理由（与 Anne L'Huillier、Ferenc Krausz 共享）：
  > "for experimental methods that generate attosecond pulses of light for the study of electron dynamics in matter"（因产生阿秒光脉冲以研究物质中电子动力学的实验方法）
- **设计母题**：**时间切片（attosecond slicing）**。1 as = 10⁻¹⁸ s——把连续的光波切成一串 250 阿秒的脉冲再重新组合干涉，视觉上可用「波列被光栅切分为等距短脉冲」的重复结构表达。
- **本地数据源（已有）**：`physicist/presentations/21th_century/21st_century/Pierre_Agostini/page.md`
- **待下载（第 0 步执行）**：`Pierre_Agostini.html` 与 `images/` 肖像尚未下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Pierre_Agostini`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：核对事实基准 【人物专属】

- page.md 已有本地（frontmatter + infobox + 正文），第一轮核对基准如下：
  - 生卒（1941-07-23 生于突尼斯城；在世，无卒日）
  - 国籍（法国）
  - 教育（Prytanée national militaire 拉弗莱什军校预科 1959 会考；艾克斯-马赛大学物理学 BEd/licence 1961、MAS/DEA 1962、博士 1968，论文为紫外多层介质滤光片《Appareillage permettant la réalisation de filtres multidiélectriques UV: Étude des couches Sb2O3 cryolithe》，1967 答辩目录年份与正文 1968 并存时以正文为准）
  - 博士导师（page.md 无载，禁写）
  - 任职机构（1969–2002 CEA Saclay 研究员，在 Gérard Mainfray 与 Claude Manus 实验室做多光子电离；2002–2004 布鲁克海文国家实验室访问学者，在 Louis F. DiMauro 组；2005 俄亥俄州立大学物理教授，与 DiMauro 共建实验室；2018 荣休）
  - 关键荣誉（Gustave Ribaud 奖 1995 法国科学院；Gay-Lussac–Humboldt 奖 2003；Joop Los fellowship 2003；William F. Meggers 光谱学奖 2007；OSA Fellow 2008；Humboldt Fellow；2023 诺贝尔物理学奖；荣誉军团勋章指挥官级）
  - 知名学生（page.md 无载，禁写）
  - 核心贡献清单：
    1. 1979 年在氙气中首次观测阈上电离（ATI，与 CEA Saclay 团队）
    2. 2001 年与 FOM 的 Harm Geert Muller 合作产生 250 阿秒脉冲串
    3. 发明 RABBITT（双光子跃迁干涉重建阿秒拍频）技术表征阿秒脉冲
    4. 强场激光物理与非线性原子分子响应动力学的系列创新实验
  - 关键时间线（16 节点）：1941 生于突尼斯城 → 1959 Prytanée 会考 → 1961 licence → 1962 MAS → 1968 博士（多层介质滤光片） → 1969 入 CEA Saclay → 1979 首测 ATI → 1995 Gustave Ribaud 奖 → 2001 250 as 脉冲串 + RABBITT → 2002–2004 BNL 访问 → 2003 Gay-Lussac–Humboldt + Joop Los → 2005 OSU 教授 → 2007 Meggers 奖 → 2008 OSA Fellow → 2018 荣休 → 2023 诺贝尔奖

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Pierre_Agostini/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品（如 `Serge_Haroche/Makefile`），设置 `MAIN=Pierre_Agostini_zh`、`VIDEO_NAME=Pierre_Agostini_zh`

### 第 3 步：收集图片 【人物专属】

- 从 Wikipedia infobox 下载 Agostini 2023 年肖像（Commons `Special:FilePath` 或 Wikipedia REST API page/summary，250px 改 500px，curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证）；404 则用装饰圆占位并注明

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | attosecond physics | 阿秒物理 | 2023 诺奖核心领域 | 封面、核心页 |
| 1 | strong-field laser physics | 强场激光物理 | 强红外激光下原子分子非线性响应 | 核心页 |
| 2 | above-threshold ionization | 阈上电离 | 1979 年首次观测 | ATI 页 |
| 3 | multiphoton ionization | 多光子电离 | CEA Saclay 时期主线 | CEA 页 |
| 4 | ultrafast optics | 超快光学 | RABBITT 阿秒脉冲表征 | RABBITT 页 |

- 入库：`cd MySQL && python3 seed_person.py data/Pierre_Agostini.yaml`（yaml 见第 4.5 步后说明，fields 与本表一致）

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；对手方无 qid 不编造。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Anne L'Huillier | 无向 | 2023 诺贝尔物理学奖共同得主 |
| co-honored | Ferenc Krausz | 无向 | 2023 诺贝尔物理学奖共同得主 |
| colleague | Louis F. DiMauro | 无向 | BNL 访问在其组内，2005 起俄亥俄州立共建实验室 |
| colleague | Harm Geert Muller | 无向 | 2001 年 250 as 脉冲串实验合作（荷兰 FOM） |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：精准、瞬逝、光的切片
- **主色**：法国深蓝 `#0F4C81` + 诺奖香槟金 `C9A227`
- badgeA–D 四分类色：badgeATI 阈上电离 — 青绿 `#0E7C7B`；badgeRAB 阿秒表征 — 琥珀 `#E07B30`；badgeMultip 多光子电离 — 玫瑰 `#C4204F`；badgeCareer 机构岁月 — 靛蓝 `#4C5FD5`
- **背景母题**：等距短脉冲串（一列被切分的窄矩形/短线段），呼应 250 as 脉冲串与 RABBITT 干涉拍频

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页：封面之后、核心贡献之前，左头像 + 右信息网格（生卒、出生地、国籍、教育、任职、荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 阿秒物理先驱 / Pierre Agostini 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — ATI / 250 as 脉冲串 / RABBITT / 强场激光物理
04  早年：突尼斯到拉弗莱什 (1941–1959) — 法国保护地出生、军校预科会考
05  艾克斯-马赛求学 (1959–1968) — licence 1961、MAS 1962、紫外多层介质滤光片博士
06  CEA Saclay 三十三年 (1969–2002) — Mainfray-Manus 实验室、强激光多光子电离
07  1979：阈上电离的首次观测（核心贡献页一）— 氙气实验、超越阈值的额外光子吸收
08  2001：250 阿秒脉冲串与 RABBITT（核心贡献页二）— 与 Muller 合作、红外+紫外再结合干涉
09  RABBITT 技术解析 — 双光子跃迁干涉重建阿秒拍频（概念图式，page.md 无公式）
10  跨越大西洋 (2002–2018) — BNL DiMauro 组、OSU 共建实验室、2018 荣休
11  荣誉与认可 — Ribaud 1995 / Gay-Lussac–Humboldt 2003 / Meggers 2007 / OSA Fellow 2008
12  2023 诺贝尔物理学奖 — 三人共享、citation 原句
13  遗产：阿秒物理的实验基石
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）整体复用同目录成品骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Agostini 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生国籍 | 1941 生于法国保护地突尼斯（French Tunisia），国籍是法国；勿写"突尼斯裔" |
| 博士年份 | infobox 论文目录标 1967，正文作 1968 完成博士学位；以正文 1968 为准并加注 |
| 博士导师 | page.md 无载，禁写（勿从 CEA 机构反推 Mainfray/Manus 为导师——他们是实验室负责人） |
| ATI 归属 | "They are the first to observe"——首次观测是 CEA Saclay 团队集体成果，勿写成个人独得 |
| RABBITT 语义 | 全称 Reconstruction of Attosecond Beating by Interference of Two-photon Transitions，是表征技术而非脉冲产生技术 |
| 250 as | 2001 年脉冲串每个脉冲 250 阿秒，勿与 L'Huillier 2003 年 170 as 世界纪录混淆 |
| 诺奖共享 | 2023 与 L'Huillier、Krausz 三人共享同一 citation；勿写"独享"或改写 citation |
| 荣誉军团勋章 | 军团勋章指挥官级（Commander of the Legion of Honour）在 frontmatter 有载但 page.md 正文未给年份，年份禁写 |
| 机构名混写 | CEA Saclay 在 page.md 正文链接作 CEA Paris-Saclay，统一写 CEA Saclay 并勿混用两个名义 |
| BNL 头衔 | 2002–2004 是 visiting scientist（访问学者），勿写成"研究员入职"或"客座教授" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| attosecond | 阿秒 | 10⁻¹⁸ 秒，勿写成"阿托秒" |
| above-threshold ionization (ATI) | 阈上电离 | 吸收光子数超过电离所需最少光子数 |
| RABBITT | 双光子跃迁干涉重建阿秒拍频 | 缩写不翻译，首现给全称 |
| pulse train | 脉冲串 | 一串等间隔短脉冲，非"脉冲列车" |
| multilayer dielectric filter | 多层介质滤光片 | 博士论文主题 |
| strong-field laser physics | 强场激光物理 | 与强场物理（QED）区分 |
| xenon | 氙 | 1979 ATI 实验气体 |
| electron dynamics | 电子动力学 | 诺奖 citation 用语 |
| emeritus professor | 荣休教授 | 2018 年 OSU 荣休 |
| Prytanée national militaire | 国家军事预备学校 | 拉弗莱什，1959 会考就读地 |
| optical Society (Optica) | 美国光学学会 | Meggers 奖与 Fellow 均由其颁发，今名 Optica |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（inspiring-electronic 合辑）
- **风格**：纪录片 / 电影 / 稳重
- **匹配理由**：阿秒脉冲是不可见的极紫外瞬光，"看不见的光"与 ATI/RABBITT 的探测本质同构；纪录片稳重感匹配 CEA 三十三年的长线实验生涯。
- **本地路径**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **备选** (未采用):
  - ★★ SEA — "流动/平稳"匹配激光连续到脉冲的切换，但流动感弱于"看不见的光"的意象贴合度
  - ★ Mirage — "梦幻/抽象"匹配阿秒尺度的不可见性，但受众与沉稳感不足
- **批内去重**：本曲在本批（batch 13）内不与 Krausz / L'Huillier / Hopfield / Hinton 重复。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Pierre_Agostini/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Pierre_Agostini.yaml` | 社会关系 + 领域入库 yaml |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
