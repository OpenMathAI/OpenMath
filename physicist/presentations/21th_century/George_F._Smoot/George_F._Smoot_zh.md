# 物理学家立传提示词（George F. Smoot）

> 本文件是 OpenPhysicist 21 世纪批次人物专属立传提示词，目标人物：George Fitzgerald Smoot III（2006 诺贝尔物理学奖，CMB 各向异性）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：George Fitzgerald Smoot III（乔治·菲茨杰拉德·斯穆特三世）。
- **设计哲学**：物理学家立传必须有「身份信息页」+「研究领域」结构化表达，此骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：George Fitzgerald Smoot III（1945-02-20 生于佛罗里达州尤康 ~ 2025-09-18 逝于法国巴黎，享年 80 岁）
- **气质关键词**：**宇宙涟漪的发现者、各向异性的测绘者、大爆炸的见证人** —— 2006 诺贝尔物理学奖获奖理由：
  > "for their discovery of the black body form and anisotropy of the cosmic microwave background radiation"（因其发现宇宙微波背景辐射的黑体形态和各向异性）
- **设计母题**：**宇宙涟漪（ripples of the early universe）**。COBE-DMR 测得的十万分之一量级温度涨落斑图——「宇宙婴儿时期的照片」，今日所有星系结构的种子；配合名言「if you're religious, it's like looking at God」的震撼意象。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/George_F._Smoot/page.md`（已有本地）
- **第 0 步素材状态**：`George_F._Smoot.html` 与 `images/` **待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/George_F._Smoot`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（frontmatter + infobox + 正文已核对，事实基准如下）
- 🔲 待下载：`https://en.wikipedia.org/wiki/George_F._Smoot` → `George_F._Smoot.html`；肖像（infobox 照片，2006 诺奖庆祝照）→ `images/`
- **事实基准**（全部取自 page.md）：
  - 生卒：1945-02-20 生于佛罗里达州尤康；2025-09-18 逝于巴黎（心脏病，享年 80；巴黎天体粒子与宇宙学实验室 9 月 25 日讣告）
  - 国籍：美国
  - 家庭：父亲为美国地质调查局水文学家；母亲是教师兼校长；妹妹 Sharon；外祖父 Johnson Tal Crawford；全家曾住阿拉斯加后迁俄亥俄
  - 教育：1962 Upper Arlington High School（俄亥俄）；1966 MIT 数学+物理双学士；1970 MIT 粒子物理 PhD（infobox 论文条目标 1971，两说见陷阱表）
  - 博士论文：《Charge exchange of positive Kaon on platinum at three GeV/C》；博士导师：David H. Frisch（frontmatter + infobox 明载）
  - 任职：1970 起 UC Berkeley + Lawrence Berkeley National Laboratory（LBNL）；巴黎宇宙学物理中心「Physics of the Universe」捐赠基金主席；机构列表另有巴黎第七大学（Paris Diderot）、香港科技大学；2023-01 加入哈萨克斯坦国家科技委员会；晚年任 GTA Foundation AI 科学家
  - 关键荣誉（含年份）：NASA Exceptional Scientific Achievement Medal（正文 1991 / infobox 1992，两说见陷阱表）；Kilby Award 1993；Golden Plate Award 1994；Ernest Orlando Lawrence Award（infobox 1994 / 正文 1995，两说见陷阱表）；Einstein Medal 2003；Nobel 2006；Gruber 宇宙学奖 2006；Daniel Chalonge Medal 2006；Oersted Medal 2009；NAS 院士 + APS Fellow
  - 知名学生：page.md 无载（勿写）
  - 核心贡献清单（4–6 条）：①与 Alvarez/Muller 研制 U-2 机载差分辐射计，测得 CMB 偶极各向异性（多普勒效应解释）并确定宇宙整体旋转为零；②提出 COBE-DMR（微分微波辐射计）方案并主导 CMB 微小温度涨落测量；③1992-04-23 宣布发现 CMB 各向异性——早期宇宙结构种子的直接证据；④后续参与 MAXIMA 平流层气球实验、Planck 卫星合作、SNAP 暗能量探测设计、Spitzer 远红外背景分析；⑤2007 捐 50 万美元设立 Berkeley Center for Cosmological Physics
  - 关键时间线（15–20 节点）：1945 生于尤康 → 童年阿拉斯加 → 1962 Upper Arlington HS → 1966 MIT 双学士 → 1970 MIT 粒子物理 PhD（Frisch 门下）→ 1970 入 Berkeley/LBNL → 1970s 与 Alvarez 合作高空反物质气球实验 → U-2 差分辐射计测 CMB 偶极 → 1970s 末提出 COBE 卫星提案 → 1986 挑战者号失事致 COBE 延期 → 1989-11-18 COBE 发射 → 1992-04-23 DMR 各向异性宣布（名言「looking at God」）→ 1994《Wrinkles in Time》出版 → 2003 Einstein Medal → 2006 Nobel + Gruber + Chalonge → 2007 捐资伯克利宇宙学中心 → 2009 Oersted +《生活大爆炸》客串 → 2014 TEDx 模拟假说演讲 → 2023 哈萨克斯坦国家科技委 → 2025-09-18 逝于巴黎

### 第 0.5 步：事实核对清单（执行立传前逐项打勾，page.md ↔ 本提示词）【人物专属】

- [ ] 1945-02-20 生于佛罗里达州尤康；2025-09-18 卒于巴黎（心脏病，享年 80，9-25 讣告）
- [ ] 父 USGS 水文学家；母教师兼校长；妹 Sharon；外祖父 Johnson Tal Crawford
- [ ] 童年阿拉斯加 → 俄亥俄；1962 Upper Arlington High School
- [ ] 1966 MIT 数学+物理双学士；1970 粒子物理 PhD（infobox 论文条目作 1971，两说加注）
- [ ] 博士导师 David H. Frisch；论文《Charge exchange of positive Kaon on platinum at three GeV/C》
- [ ] 远亲 Oliver R. Smoot（长度单位 smoot 由其身高定义），勿与父系混淆
- [ ] 1970 起 UC Berkeley + LBNL；与 Alvarez 合作高空反物质气球实验
- [ ] 与 Richard A. Muller 研制 U-2 差分辐射计：偶极各向异性 + 宇宙整体旋转为零
- [ ] 1989-11-18 COBE 发射（挑战者号失事致延期）；1992-04-23 DMR 各向异性宣布
- [ ] NASA 奖章（正文 1991 / infobox 1992 两说）；Lawrence Award（正文 1995 / infobox 1994 两说）
- [ ] Kilby 1993 / Golden Plate 1994 / Einstein Medal 2003 / Nobel + Gruber + Chalonge 2006 / Oersted 2009
- [ ] 2007 捐 50 万美元设 Berkeley Center for Cosmological Physics；2023 哈萨克斯坦国家科技委

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `George_F._Smoot/` 与 `images/`（第 0 步已建则复用）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设置 `MAIN=George_F._Smoot_zh`、`VIDEO_NAME=George_F._Smoot_zh`

### 第 3 步：收集图片 【人物专属，待下载】

- 肖像：infobox「Smoot at Ithaka Science Center in 2009」或 2006-10-03 LBNL 诺奖庆祝照 → `images/portrait.jpg`；下载后 `file` 验证（JFIF density 异常时 sips 改 72dpi）
- Commons 直链 404 时回退：Wikipedia REST API `page/summary` 查 infobox 原图名，或 `Special:FilePath/<文件名>?width=600`
- 可选插图：COBE 涨落全天空图（page.md 内嵌 commons 图）/ U-2 差分辐射计示意 / 宇宙偶极图示

### 第 9.5 步：交付前自查清单 【模板通用，第 9 步完成后逐项核对】

- [ ] 编译 0 error；vbox ≤ 10pt、hbox ≤ 50pt（取真实 xelatex 日志核对，勿被 latexmk -c 误判）
- [ ] 页数与第 6 步规划一致（pdfinfo 数页数，页数不符 = 可能有帧未渲染或被合并）
- [ ] 逐页 pdftoppm 目检溢出/重叠；修复优先级：删 \plainbar → 缩 inner sep → 缩字号 → 减行距
- [ ] 引语逐条对照白名单；陷阱表「无载禁写」逐条核对
- [ ] 批内主色互查不重复；BGM 曲名批内唯一
- [ ] 术语清单中译逐条核对；结尾页品牌口径 OpenMathAI

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

**Smoot 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | astrophysics | 天体物理学 | frontmatter field_of_work 首项 | 封面、身份页 |
| 1 | cosmology | 宇宙学 | 职业主线，COBE/Planck/暗能量 | 核心页 |
| 2 | cosmic microwave background | 宇宙微波背景 | 偶极与各向异性测量 | 核心贡献页 |
| 3 | particle physics | 粒子物理 | MIT 博士阶段与早期气球实验 | 求学页 |
| 4 | observational cosmology | 观测宇宙学 | U-2/COBE/MAXIMA/Planck 观测链 | 观测页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | David H. Frisch | 师→生（博士导师） | MIT 博士导师，粒子物理（正 K 介子电荷交换） |
| co-honored | John C. Mather | 无向 | 2006 诺贝尔物理学奖共享（CMB 黑体形态与各向异性） |
| colleague | Luis Walter Alvarez | 无向 | 伯克利同事，高空反物质气球实验合作（1968 诺奖得主） |
| colleague | Richard A. Muller | 无向 | 共同研制 U-2 机载差分辐射计，测得 CMB 偶极各向异性 |
| controversy | John C. Mather | 无向 | 《The Very First Light》载 COBE 发布纪律争议（抢先向媒体披露），后和解 |

- 仅收 page.md 明载关系；科普书合著者 Keay Davidson 不做关系入库。

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深邃、震撼、宇宙原生
- **配色**：深砖红（主色）+ 香槟金（诺奖 `C9A227`）+ 四分类色
  - 主色 `mainclr` 深砖红 `#8C2F39`
  - `badgeDipole` 偶极各向异性 — 星蓝 `#2E5E8C`
  - `badgeAniso` 结构种子 — 琥珀 `#D08A2E`
  - `badgeCOBE` COBE — 青绿 `#1F7A6D`
  - `badgePlanck` 后 COBE 时代 — 紫灰 `#5C4A72`
- **批内主色查重**：#8C2F39 仅本篇使用（Mather #0F3057 / Fert #1B4D3E / Grünberg #2F4F4F / Nambu #4E3D6E）
- **背景母题**：深邃底色上散布细微明暗斑块，呼应 COBE-DMR 温度涨落全天空图

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 宇宙涟漪的发现者 / George F. Smoot 1945–2025 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — CMB 偶极 / 各向异性 / COBE-DMR / 后 COBE 观测
04  早年：从尤康到俄亥俄 (1945–1962) — 水文学家之子、阿拉斯加岁月
05  MIT：数学+物理双学士到粒子物理博士 (1962–1970) — Frisch 门下
06  转向宇宙学：伯克利与 Alvarez (1970–) — 反物质气球实验、稳态理论检验
07  U-2 差分辐射计：偶极与宇宙零旋转（核心贡献页一，公式框放偶极温度 ΔT/T = v/c·cosθ 概念式）
08  COBE-DMR：十万分之一的涟漪（核心贡献页二，概念图式：全天空温度涨落斑图）
09  1992 宣布与「looking at God」 — 结构种子、团队 1000+ 人
10  2006 诺贝尔奖 — 与 Mather 共享、COBE 双仪器分工
11  争议与和解 — 《Wrinkles in Time》vs《The Very First Light》、披露风波、后释怀
12  后 COBE 时代 — MAXIMA、Planck、SNAP、Spitzer 远红外背景
13  荣誉与大众文化 — Einstein Medal 2003 · Gruber 2006 · Oersted 2009 ·《生活大爆炸》客串
14  遗产：精确宇宙学的奠基者之一
15  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

- 版式复用标杆骨架（`\plainbar` / `\deckbackground` / `\profileslide`）；每写一页 make 并截图查溢出。
- **Smoot 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由双要素 | 官方措辞 "black body form **and anisotropy**"；本篇主角是各向异性侧，黑体谱是 Mather/FIRAS 侧，分工勿颠倒 |
| 学位年份两说 | 正文作 1970 年 PhD，infobox 论文条目作 (1971)；建议正文用 1970 并加注 |
| NASA 奖章年份两说 | 正文 1991，infobox 1992；Lawrence Award 正文 1995，infobox 1994；各页须前后一致并加注 |
| Mather 分工 | Mather 协调整个项目并负责 FIRAS 黑体谱；Smoot 负责温度涨落测量；勿写「Smoot 领导 COBE」 |
| 争议表述 | Mather/Boslough 书中指其抢先向媒体泄露 COBE 结果；Smoot 道歉、后 Mather 承认其「为 COBE 带来世界性关注」——争议与和解都要写，勿单边叙事 |
| 引语白名单 | "if you're religious, it's like looking at God"（1992 宣布）可引；诺奖委员会 "the COBE project ... starting point for cosmology as a precision science" 可引；其余勿加引号 |
| 出生地名 | 生于佛罗里达州尤康（Yukon, Florida），勿与加拿大育空混淆 |
| 同名/亲属区分 | 远亲 Oliver R. Smoot（MIT 学生，长度单位 smoot 由其身高定义）非本传主父亲；父亲是 USGS 水文学家 |
| 卒地 | 2025-09-18 卒于巴黎（心脏病），享年 80；勿与出生地混淆 |
| 晚年身份 | GTA Foundation「AI 科学家」、哈萨克斯坦国家科技委是 page.md 明载，可写但勿夸大 |
| 模拟假说 | 2014 TEDx 提出 physics 支持模拟假说，page.md 明载可客观一句，勿展开为本人立场定论 |

### 第 9 步：术语审查 【人物专属】

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| anisotropy | 各向异性 | 获奖理由核心词，十万分之一量级 |
| dipole | 偶极 | 地球运动多普勒效应所致，非宇宙学涨落 |
| differential radiometer | 差分辐射计 | U-2 与 DMR 一脉相承 |
| COBE-DMR | 微分微波辐射计 | Smoot 负责 |
| last scattering surface | 最后散射面 | 偶极解释背景 |
| steady state theory | 稳态理论 | 已被否定，早期气球实验检验对象 |
| Great Attractor | 巨引源 | 银河系 600 km/s 相对运动的可能成因 |
| MAXIMA | 毫米各向异性成像阵列 | 后 COBE 气球实验 |
| Planck satellite | 普朗克卫星 | 第三代 CMB 各向异性观测 |
| simulation hypothesis | 模拟假说 | 2014 TEDx 提及，客观表述 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（纪录片 / 电影 / 稳重）
- **匹配理由**: CMB 是肉眼不可见的「隐形之光」，宇宙婴儿时期的照片由微波刻画；纪录片气质匹配从 U-2 到 COBE 到 Planck 的观测叙事长线。
- **批内查重**: The Invisible Light 仅本篇使用（Mather=Expedition / Fert=Through the Darkness / Grünberg=New Lands / Nambu=Eternals）
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/George_F._Smoot/page.md` | 本地事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/George_F._Smoot.yaml` | 社会关系入库源 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
