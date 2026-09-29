# 物理学家立传提示词（21 世纪批次：Riccardo Giacconi）

> **本文件是 OpenPhysicist「物理学家立传提示词」**，对象：Riccardo Giacconi（2002 诺贝尔物理学奖，X 射线天文学奠基人）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 凡标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。

---

## 一、模板定位 【人物专属】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Riccardo Giacconi（里卡尔多·贾科尼），2002 诺贝尔物理学奖得主（三人共享之一）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达，此骨架务必保留；Giacconi 是「观测天文学 + 大科学装置管理」双线人物，叙事上突出「从火箭探测器到空间望远镜」的装备演进链。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Riccardo Giacconi（1931-10-06 ~ 2018-12-09，享年 87 岁）
- **获奖理由（官方英文原文 + 中译，禁止改写）**：
  > "for pioneering contributions to astrophysics, which have led to the discovery of cosmic X-ray sources"（因其对天体物理学的开创性贡献，这些贡献导致了宇宙 X 射线源的发现）
- **共享格局**：2002 奖半数授予 Giacconi（X 射线天文学），另半数由 Raymond Davis Jr. 与 Masatoshi Koshiba 共享（中微子天文学）——两条工作线**互不相关**，勿写成同一发现。
- **气质关键词**：**X 射线天文学奠基人、空间望远镜的开创者、大科学装置的掌舵人**
- **设计母题**：**不可见光的视野（vision beyond visible light）**。地球大气吸收宇宙 X 射线，必须把望远镜送上天——以「大气层屏障 + 轨道上的眼睛」为核心视觉概念（稀疏同心圆弧代表大气层，圆弧外的星点代表 X 射线源）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Riccardo_Giacconi/page.md`
- **第 0 步状态**：page.md 已有本地；**html 与 images/ 待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Riccardo_Giacconi`
- **参考模板**：
  - 物理学家成品参照：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报；数据库同步含「研究领域 + 入库」（第 4 步）与「社会关系 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ☐ 待下载 `https://en.wikipedia.org/wiki/Riccardo_Giacconi` 到 `{Dir}.html` 与 `images/` 肖像（Commons `Giacconi_lg2.jpg` 250px 改 500px；404 则走 Wikipedia REST API `page/summary` 查 infobox 原图名）
- 事实基准（以本地 page.md 为准，第一轮已核对）：
  - 生卒：1931-10-06 生于意大利热那亚（时为意大利王国）~ 2018-12-09 逝于美国加州圣地亚哥，享年 87 岁
  - 国籍：意大利 → 意大利/美国（Italian-American）
  - 教育：米兰大学物理系 Laurea（博士导师 page.md **无载**）
  - 1956 年 Fulbright Fellowship 赴美，与印第安纳大学物理学教授 R. W. Thompson 合作
  - 任职轨迹：火箭载探测器（1950s 末–1960s 初）→ Uhuru（1970s，首颗轨道 X 射线天文卫星）→ Einstein Observatory（1978，首台 fully imaging 空间 X 射线望远镜）→ STScI 首任常任所长（1981–1993，哈勃科学运行中心）→ ESO 总干事（1993–1999，主持 VLT 建设）→ Associated Universities, Inc. 主席（1999–2004，管理 ALMA 早期）→ Johns Hopkins 物理与天文教授（1982–1997）、研究教授（1998–2018 去世）、university professor；2000s 任 Chandra Deep Field-South 项目 PI
  - 关键荣誉：Helen B. Warner Prize 1966；NAS 院士 1971；American Academy of Arts and Sciences 1971；Elliott Cresson Medal 1980；Bruce Medal 1981；Henry Norris Russell Lectureship 1981；Dannie Heineman Prize for Astrophysics 1981；RAS Gold Medal 1982；Wolf Prize 1987；American Philosophical Society 2001；Nobel 2002；National Medal of Science 2003；小行星 3371 Giacconi；意大利共和国功绩勋章大十字
  - 知名学生：page.md **无载**，禁写
  - 核心贡献清单（4–6 条）：①奠定 X 射线天文学基础；②火箭载 X 射线探测器（1950s–60s）；③Uhuru 首颗 X 射线天文卫星；④Einstein Observatory 首台成像 X 射线望远镜；⑤Chandra 与 Chandra Deep Field-South；⑥执掌 STScI/ESO/AUI 三大天文机构
  - 关键时间线（15–20 节点）：1931 生于热那亚 → 米兰大学 Laurea → 1956 Fulbright 赴美（印第安纳大学，与 R. W. Thompson 合作）→ 1950s 末–1960s 初火箭载探测器 → 1966 Warner Prize → 1970s Uhuru 上天 → 1971 NAS + 美国艺术与科学院 → 1978 Einstein Observatory → 1980 Cresson 奖 → 1981 Bruce / Russell / Heineman 三奖 → 1981–1993 STScI 首任所长 → 1982 JHU 教授 + RAS 金章 → 1987 Wolf 奖 → 1993–1999 ESO 总干事（VLT）→ 1998 JHU 研究教授 → 1999 Chandra 发射 → 1999–2004 AUI 主席（ALMA）→ 2000s Chandra Deep Field-South PI → 2001 美国哲学学会 → 2002 诺贝尔物理学奖 → 2003 National Medal of Science → 2018-12-09 逝于圣地亚哥

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Riccardo_Giacconi/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 20 世纪成品目录 Makefile，设 `MAIN=Riccardo_Giacconi_zh`、`VIDEO_NAME=Riccardo_Giacconi_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：Commons `Giacconi_lg2.jpg`（page.md 正文插图，2003 年照）；404 则 REST API 回退；再不行装饰圆占位

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | x-ray astronomy | X 射线天文学 | 奠基人，2002 诺奖核心 | 核心页 |
| 1 | astrophysics | 天体物理学 | 官方获奖理由主词 | 诺奖页 |
| 2 | astronomy | 天文学 | 职业口径主领域 | 概览页 |
| 3 | cosmic radiation | 宇宙辐射 | frontmatter field_of_work 载明 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> **只收 page.md 明载**；对手方入库用规范 name_en（已查库核对）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Raymond Davis Jr. | 无向 | 2002 诺贝尔物理学奖共享（中微子天文学半数） |
| co-honored | Masatoshi Koshiba | 无向 | 2002 诺贝尔物理学奖共享（中微子天文学半数） |
| colleague | R. W. Thompson | 无向 | 1956 年 Fulbright 赴美，在印第安纳大学与之合作 |

- 入库注意：Giacconi 本人为新建记录（qid=Q186481）；Koshiba / Davis 由 batch 1 并行入库，撞 uq_rel 跳过即可；Tananbaum/Weisskopf/Canizares 仅见于合影图注，**不入库**。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深空、屏障之外、观测者的冷峻
- **配色**：深空紫（主色，批内唯一）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `mainclr` 主色 — 深空紫 `#2E1A47`
  - `badgeXR` X 射线天文 — 电紫 `#8E44AD`
  - `badgeSat` 空间探测 — 青绿 `#148F77`
  - `badgeInst` 大科学管理 — 琥珀 `#B9770E`
  - `badgeNobel` 诺奖与荣誉 — 玫瑰 `#A93226`
- **背景母题**：柔和气泡——底部一组同心圆弧代表大气吸收层，圆弧外散布四色星点，呼应「不可见光的视野」

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍（顶部副标题或底部状态栏），底部状态栏给 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前，左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域），事实取自 page.md，不得杜撰。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — X 射线天文学奠基人 / Riccardo Giacconi 1931–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 火箭探测 / Uhuru / Einstein / Chandra / 三大机构
04  早年：热那亚与米兰 (1931–1956) — 热那亚出生、米兰大学 Laurea
05  富布赖特赴美与火箭探测 (1956–1960s) — 印第安纳大学 R. W. Thompson、火箭载探测器
06  Uhuru：第一颗 X 射线天文卫星 (1970s) — 大气吸收问题 → 上天的必要性（概念图式：page.md 无公式，公式框放「大气吸收 → 空间望远镜」图式并注明）
07  Einstein Observatory (1978) — 首台 fully imaging X 射线望远镜
08  大科学掌舵人 — STScI 1981–1993 / ESO 1993–1999（VLT）/ AUI 1999–2004（ALMA）
09  Chandra 与 Deep Field-South — 1999 发射、2000s 任 PI、JHU 1982–2018
10  2002 诺贝尔物理学奖 — 三人共享格局页（Giacconi 半数 / Davis+Koshiba 半数·中微子，两条线互不相关）
11  荣誉与认可 — Warner 1966 · Wolf 1987 · Nobel 2002 · National Medal of Science 2003 · 小行星 3371
12  遗产：从火箭到 Chandra 的 X 射线视野
13  结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。
- 每写完一页 `make`，`pdftoppm` 截图检查；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Giacconi 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 2002 年 Giacconi 独得**半数**，Davis+Koshiba 共享**另一半**；获奖理由是「宇宙 X 射线源的发现」，与中微子天文学**无关**，勿写「因中微子天文学获奖」 |
| 三人关系 | 与 Davis/Koshiba 仅为同年共享诺奖（co-honored），无师生/同事关系，禁写合作 |
| 博士导师 | page.md **无载**，禁写（勿从米兰学派反推） |
| 学生 | page.md **无载**，禁写 |
| Tananbaum/Weisskopf/Canizares | 仅出现在合影图注，不算明载关系，禁入关系表 |
| STScI 头衔 | 「first permanent director」——首任**常任**所长（1981–1993），是哈勃的科学运行中心，勿写成「哈勃望远镜总设计师」 |
| ESO 任期 | 1993–1999 总干事，主持 VLT 建设；ALMA 是 AUI 主席任内（1999–2004）「管理早期年代」，勿写成「主持建设 ALMA」 |
| JHU 任职 | 教授 1982–1997、研究教授 1998–2018（至去世）、university professor，三段勿混 |
| Chandra | 1999 年发射、「仍在运行」为 page.md 口径；Deep Field-South 是 2000s 的 PI 项目 |
| Einstein Observatory | 1978，是「首台 fully imaging X 射线望远镜入空」；Uhuru 是「首颗轨道 X 射线天文卫星」——两个「第一」勿互换 |
| 国籍 | 出生时为意大利王国（Kingdom of Italy），热那亚；殁于美国——国籍写「意大利 / 美国」 |
| 配偶/家庭 | page.md 无载，禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| X-ray astronomy | X 射线天文学 | 诺奖理由核心词 |
| cosmic X-ray sources | 宇宙 X 射线源 | 官方理由原词 |
| rocket-borne detectors | 火箭载探测器 | 早期手段 |
| Uhuru | 乌呼鲁卫星 | 首颗 X 射线天文卫星 |
| Einstein Observatory | 爱因斯坦天文台 | 首台成像 X 射线望远镜 |
| Chandra X-ray Observatory | 钱德拉 X 射线天文台 | 1999 发射 |
| Space Telescope Science Institute | 空间望远镜科学研究所 | STScI，哈勃运行中心 |
| European Southern Observatory | 欧洲南方天文台 | ESO |
| Very Large Telescope | 甚大望远镜 | VLT |
| Atacama Large Millimeter Array | 阿塔卡马大型毫米波阵列 | ALMA |
| Fulbright Fellowship | 富布赖特奖学金 | 1956 赴美契机 |
| Laurea | （意）劳雷亚学位 | 米兰大学物理系 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（纪录片 / 电影 / 稳重）
- **匹配理由**: 曲名「不可见光」与 Giacconi 的设计母题**字面契合**——X 射线正是人眼不可见的光；「纪录片/稳重」匹配其「火箭 → 卫星 → 望远镜 → 大科学机构」的长线叙事。
- **备选**（未采用）: New Lands（开阔/史诗，但更适时代转折页）；Eternals（宏大/深远，受众偏低）。
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- 批内 BGM 不重复备案：Giacconi=The Invisible Light（其余四人另选）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Riccardo_Giacconi/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 关系入库引擎（幂等） |
| `MySQL/data/Riccardo_Giacconi.yaml` | yaml 数据文件 |

> **开始执行。每完成一步汇报。**
