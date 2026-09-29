# 物理学家立传提示词（John C. Mather）

> 本文件是 OpenPhysicist 21 世纪批次人物专属立传提示词，目标人物：John Cromwell Mather（2006 诺贝尔物理学奖，COBE 黑体谱）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Cromwell Mather（约翰·克伦威尔·马瑟）。
- **设计哲学**：物理学家立传必须有「身份信息页」+「研究领域」结构化表达，此骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Cromwell Mather（1946-08-07 生于弗吉尼亚州罗阿诺克，在世）
- **气质关键词**：**宇宙黑体谱的测绘者、精确宇宙学的开创者、JWST 的守护者** —— 2006 诺贝尔物理学奖获奖理由：
  > "for their discovery of the black body form and anisotropy of the cosmic microwave background radiation"（因其发现宇宙微波背景辐射的黑体形态和各向异性）
- **设计母题**：**完美谱线（the perfect spectrum）**。COBE-FIRAS 测得的黑体谱与理论曲线严丝合缝——一条跨越 48 个 octaves 的平滑曲线，是宇宙大爆炸最直接的画面；各向异性斑点则是后来一切结构的种子。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/John_C._Mather/page.md`（已有本地）
- **第 0 步素材状态**：`John_C._Mather.html` 与 `images/` **待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/John_C._Mather`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（frontmatter + infobox + 正文已核对，事实基准如下）
- 🔲 待下载：`https://en.wikipedia.org/wiki/John_C._Mather` → `John_C._Mather.html`；肖像（infobox 照片，Mather in 2015）→ `images/`
- **事实基准**（全部取自 page.md）：
  - 生卒：1946-08-07 生于弗吉尼亚州罗阿诺克；在世（death_date 留白）
  - 国籍：美国
  - 教育：1964 新泽西州 Newton High School；1968 Swarthmore College 物理学 BS（Highest Honors）；1974 UC Berkeley 物理学 PhD
  - 博士论文：《Far Infrared Spectrometry of the Cosmic Background Radiation》(1974)
  - 博士导师：Paul L. Richards（page.md infobox 明载）
  - 博士后：1974–1976 NRC Fellow，Columbia University Goddard Institute for Space Studies
  - 任职：NASA Goddard Space Flight Center 高级天体物理学家；University of Maryland 物理学兼职教授；机构列表另有 Columbia
  - 关键荣誉（含年份）：Heineman 天体物理奖 1993；John Scott Award 1995；Rumford Prize 1996；NAS 院士 1997；Marc Aaronson Memorial Prize 1998；Benjamin Franklin Medal 1999；Gruber 宇宙学奖 2006；**Nobel 2006**；Time 100（2007）；SPIE Fellow 2007；AAS Legacy Fellow 2020；Joseph Priestley Award 2023
  - 知名学生：page.md 无载（勿写）
  - 核心贡献清单（4–6 条）：①COBE-FIRAS 首席，测得与普朗克黑体谱完美吻合的 CMB 黑体谱；②COBE 项目科学家，CMB 偶极各向异性与微小各向异性（结构种子）的确证；③证明宇宙微波背景是大爆炸理论的奠基性证据，诺奖委员会称 COBE 是「作为精确科学的宇宙学的起点」；④JWST 高级项目科学家 1995–2023；⑤CMB 远红外光谱测量方法（博士论文）开创
  - 关键时间线（15–20 节点）：1946 生于罗阿诺克 → 1964 Newton HS → 1968 Swarthmore BS（Highest Honors；1967 Putnam 全国第 30 名；1968 GRE 物理满分 990）→ 1968–1970 NSF Fellowship + Woodrow Wilson Fellowship → 1970–1974 Hertz Fellow → 1974 Berkeley PhD（导师 Paul L. Richards）→ 1974–1976 Columbia GISS NRC 博士后 → 1976 入 NASA GSFC，COBE 立项 → 1974 提出宇宙背景探索者卫星构想（COBE 起源）→ 1989-11 COBE 发射 → 1990 FIRAS 黑体谱发表（完美黑体）→ 1992 DMR 各向异性结果 → 1993 Heineman → 1995 起 JWST 高级项目科学家 → 1996 Rumford → 1997 NAS 院士 → 1999 Franklin Medal → 2006 Nobel + Gruber → 2007 Time 100 → 2021-12 JWST 发射 → 2023 由 Jane Rigby 接任 JWST 项目科学家

### 第 0.5 步：事实核对清单（执行立传前逐项打勾，page.md ↔ 本提示词）【人物专属】

- [ ] 1946-08-07 生于弗吉尼亚州罗阿诺克；在世（death_date 留白）
- [ ] 1964 Newton High School（新泽西州牛顿）
- [ ] 1968 Swarthmore 物理学 BS（Highest Honors）
- [ ] 1967 Putnam 数学竞赛全国第 30 名；1968 GRE 物理满分 990
- [ ] 1968–1970 NSF Fellowship + 名誉 Woodrow Wilson Fellowship；1970–1974 Hertz Fellow
- [ ] 1974 UC Berkeley 物理学 PhD；博士导师 Paul L. Richards
- [ ] 博士论文《Far Infrared Spectrometry of the Cosmic Background Radiation》
- [ ] 1974–1976 NRC 博士后（Columbia University Goddard Institute for Space Studies）
- [ ] NASA GSFC 高级天体物理学家；University of Maryland 物理学兼职教授
- [ ] 2006 诺贝尔物理学奖与 George Smoot 共享；citation 双要素（black body form + anisotropy）
- [ ] Heineman 1993 / Rumford 1996 / NAS 1997 / Aaronson 1998 / Franklin 1999 / Gruber 2006
- [ ] JWST 高级项目科学家 1995–2023；2023 由 Jane Rigby 接任

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `John_C._Mather/` 与 `images/`（第 0 步已建则复用）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设置 `MAIN=John_C._Mather_zh`、`VIDEO_NAME=John_C._Mather_zh`

### 第 3 步：收集图片 【人物专属，待下载】

- 肖像：Wikipedia infobox「Mather in 2015」照片 → `images/portrait.jpg`；下载后 `file` 验证为真实图片（JFIF density 1x1 异常时用 sips 改 72dpi，防 xelatex Dimension too large）
- Commons 直链 404 时回退：Wikipedia REST API `page/summary` 查 infobox 原图名，或 `Special:FilePath/<文件名>?width=600`
- 可选插图：COBE 卫星示意 / FIRAS 黑体谱测量曲线 / CMB 全天空图 / JWST 展开状态图

### 第 9.5 步：交付前自查清单 【模板通用，第 9 步完成后逐项核对】

- [ ] 编译 0 error；vbox ≤ 10pt、hbox ≤ 50pt（取真实 xelatex 日志核对，勿被 latexmk -c 误判）
- [ ] 页数与第 6 步规划一致（pdfinfo 数页数，页数不符 = 可能有帧未渲染或被合并）
- [ ] 逐页 pdftoppm 目检溢出/重叠；修复优先级：删 \plainbar → 缩 inner sep → 缩字号 → 减行距
- [ ] 引语逐条对照白名单；陷阱表「无载禁写」逐条核对
- [ ] 批内主色互查不重复；BGM 曲名批内唯一
- [ ] 术语清单中译逐条核对；结尾页品牌口径 OpenMathAI

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

**Mather 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | astrophysics | 天体物理学 | 职业主线，NASA GSFC 高级天体物理学家 | 封面、身份页 |
| 1 | cosmology | 宇宙学 | 诺奖委员会：COBE 是精确宇宙学起点 | 核心页 |
| 2 | cosmic microwave background | 宇宙微波背景 | 黑体谱 + 各向异性两大测量 | 黑体谱页 |
| 3 | infrared astronomy | 红外天文学 | 博士论文远红外光谱测量 | 求学页 |
| 4 | observational cosmology | 观测宇宙学 | COBE/JWST 两大旗舰观测任务 | JWST 页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul L. Richards | 师→生（博士导师） | UC Berkeley 博士导师，远红外宇宙背景光谱测量 |
| co-honored | George Smoot | 无向 | 2006 诺贝尔物理学奖共享（黑体形态与各向异性） |
| colleague | Jane Rigby | 无向 | 2023 接任 JWST 高级项目科学家 |

- 仅收 page.md 明载关系；Mather 的学生、Boslough（科普书合著者）等不做关系入库。

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深邃、精确、宇宙尺度
- **配色**：深空蓝（主色）+ 香槟金（诺奖 `C9A227`）+ 四分类色
  - 主色 `mainclr` 深空蓝 `#0F3057`
  - `badgeCMB` 黑体谱 — 星蓝 `#3E6FB0`
  - `badgeAniso` 各向异性 — 玫瑰 `#C2466B`
  - `badgeIR` 红外天文 — 琥珀 `#D08A2E`
  - `badgeJWST` JWST — 青绿 `#1F8A70`
- **批内主色查重**：#0F3057 仅本篇使用（Smoot #8C2F39 / Fert #1B4D3E / Grünberg #2F4F4F / Nambu #4E3D6E）
- **背景母题**：深邃底色上稀疏排布多尺度光斑圆点，呼应 CMB 各向异性温度涨落斑图

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 宇宙黑体谱的测绘者 / John C. Mather 1946– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — CMB 黑体谱 / 各向异性 / 精确宇宙学 / JWST
04  早年：罗阿诺克到新泽西 (1946–1964) — Newton HS
05  Swarthmore 与 Berkeley (1964–1974) — Putnam 第 30、GRE 990、Hertz Fellow
06  博士论文：宇宙背景的远红外光谱 (1974) — Richards 门下
07  COBE：从构想到发射 (1974–1989) — GISS 博士后、GSFC、立项周折
08  FIRAS：完美黑体谱（核心贡献页，公式框放普朗克黑体辐射公式 B_ν(T)）
09  DMR 与各向异性：结构的种子 — 偶极 + 微小涨落（概念图式：温度涨落斑图）
10  2006 诺贝尔奖 — 与 Smoot 共享、precision cosmology 口径
11  JWST 时代 (1995–2023) — 高级项目科学家、2021 发射、Rigby 接任
12  荣誉与认可 — Heineman 1993 · Rumford 1996 · NAS 1997 · Franklin 1999 · Gruber 2006
13  遗产：作为精确科学的宇宙学
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

- 版式复用标杆骨架（`\plainbar` / `\deckbackground` / `\profileslide`）；每写一页 make 并截图查溢出。
- **Mather 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由双要素 | 官方措辞 "black body form **and anisotropy**"，黑体谱与各向异性并列，勿只写黑体谱 |
| 仪器分工 | Mather 领导 FIRAS（黑体谱），Smoot 领导 DMR（各向异性），两人是 COBE 内并列的仪器负责人，勿写「Mather 是 Smoot 的上司/下属」 |
| 同名区分（P0） | 库内 id=426 "John Mather" 是**数学家** John N. Mather（Milnor 学生、奇点理论），与本人物理学家**无关**；物理学家 yaml 用 `John C. Mather` 新建独立记录，严禁沿用 id=426 |
| 在世口径 | 1946 生、在世，death_date 留白；享年/卒年禁写 |
| 出生地 | 生于弗吉尼亚州罗阿诺克，高中在新泽西 Newton，勿混淆 |
| 引语白名单 | 可引诺奖委员会 "the COBE-project can also be regarded as the starting point for cosmology as a precision science"；其余中文叙述勿加引号当原话 |
| 2008 致总统信 | page.md 明载 20 位诺奖得主联名函，如写仅客观一句（科学经费倡导），勿展开政治叙事 |
| 学生 | page.md 无博士学生记载，门生页禁写 |
| 诺奖演讲标题 | "From the Big Bang to the Nobel Prize and Beyond"（2006-12-08），可作引言页点缀 |

### 第 9 步：术语审查 【人物专属】

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| cosmic microwave background (CMB) | 宇宙微波背景 | 勿与「宇宙背景辐射」泛称混用 |
| black body form | 黑体形态/黑体谱 | 获奖理由原文用 form |
| anisotropy | 各向异性 | 微小温度涨落，结构种子 |
| FIRAS | 远红外绝对分光光度计 | COBE 仪器，Mather 负责 |
| DMR | 微分微波辐射计 | COBE 仪器，Smoot 负责 |
| COBE | 宇宙背景探测者 | Cosmic Background Explorer |
| JWST | 詹姆斯·韦布空间望远镜 | James Webb Space Telescope |
| far infrared spectrometry | 远红外光谱测量 | 博士论文题目 |
| precision cosmology | 精确宇宙学 | 诺奖委员会口径 |
| Big Bang | 大爆炸 | 理论名词首字母规范 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（探索 / 史诗）
- **匹配理由**: 从博士论文提出卫星构想到 COBE 发射再到 JWST 时代，是横跨半个世纪的「远征式」观测宇宙学叙事；「探索」标签贴合仪器建造者气质。
- **批内查重**: Expedition 仅本篇使用（Smoot=The Invisible Light / Fert=Through the Darkness / Grünberg=New Lands / Nambu=Eternals）
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/John_C._Mather/page.md` | 本地事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/John_C._Mather.yaml` | 社会关系入库源 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
