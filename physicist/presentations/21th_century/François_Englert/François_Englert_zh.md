# 物理学家立传提示词（François Englert · 2013 诺贝尔物理学奖）

> **本文件是 OpenPhysicist 21 世纪批次的人物专属立传提示词**，以 François Englert（2013 诺贝尔物理学奖，Brout–Englert–Higgs 机制）为目标人物。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：François, Baron Englert（弗朗索瓦·恩格勒），2013 诺贝尔物理学奖（与 Peter Higgs 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇另需突出**真空结构的统一叙事**——铁磁体类比下的真空、有质量与无质量规范玻色子并存，一条从统计物理通向电弱理论基石的思辨长卷。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：François Englert（1932-11-06 生于布鲁塞尔埃特尔贝克 ~ 2026-06-18 逝于布鲁塞尔于克勒，享年 93 岁）
- **气质关键词**：**真空结构的破译者、大屠杀幸存的科学家、电弱理论的奠基人之一** —— 2013 诺贝尔物理学奖获奖理由：
  > "for the theoretical discovery of a mechanism that contributes to our understanding of the origin of mass of subatomic particles, and which recently was confirmed through the discovery of the predicted fundamental particle, by the ATLAS and CMS experiments at CERN's Large Hadron Collider"（因其对亚原子粒子质量起源机制的理论发现，该机制最近由 CERN 大型强子对撞机 ATLAS 与 CMS 实验发现所预言的基本粒子而获得证实）
- **设计母题**：**有结构的真空（structured vacuum）**。铁磁体中原子磁矩的自发排列类比空无一物的真空——对称在日常世界中"破缺"，是比泛泛「上帝粒子」更贴合 Englert 的视觉语言。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/François_Englert/page.md`（✅ 已有本地）
- **html/images**：待下载 —— Wikipedia URL：`https://en.wikipedia.org/wiki/François_Englert`（第 0 步下载 `François_Englert.html` 与 infobox 肖像到 `images/`）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（事实基准如下）；html 与 images/ 待下载（URL 见上）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1932-11-06 生于布鲁塞尔埃特尔贝克（Etterbeek）~ 2026-06-18 逝于布鲁塞尔于克勒（Uccle），享年 93 岁
  - 国籍：比利时（frontmatter 另列 France；主讲比利时）
  - 早年：比利时犹太家庭，二战德占期间隐匿犹太身份，先后藏身迪南（Dinant）、卢斯坦（Lustin）、斯图蒙（Stoumont）、安纳瓦-鲁永（Annevoie-Rouillon）的孤儿院与儿童之家，这些城镇后被美军解放——大屠杀幸存者
  - 教育：布鲁塞尔自由大学（ULB）1955 电机工程师 → 1959 物理科学博士
  - 任职机构：Cornell 1959–1961（先任 Robert Brout 的研究助理，后任助理教授）→ 1961 回 ULB 任教授 → 1980 与 Brout 共同执掌理论物理组 → 1998 荣休教授（professor emeritus）→ 1984 起特拉维夫大学 Sackler 特聘教授 → 2011 加入 Chapman 大学量子研究所（杰出访问教授）；Service de Physique Théorique 成员
  - 关键荣誉：Gravity Research Foundation 作文一等奖 1978（与 Brout、Gunzig）；Francqui Prize 1982（四年一度精确科学）；EPS High Energy and Particle Physics Prize 1997（与 Brout、Higgs）；Wolf Prize 2004（与 Brout、Higgs）；J. J. Sakurai Prize 2010（与 Guralnik、Hagen、Kibble、Higgs、Brout 六人）；Prince of Asturias Award 2013（与 Higgs、CERN）；Nobel 2013（与 Higgs）；2013-07-08 王室敕令受封男爵（King Albert II）；Clarivate Citation Laureates；多所大学荣誉博士（Mons、北京大学、Edinburgh、Bar-Ilan、VUB、Miami、Blaise-Pascal）
  - 知名学生：page.md 无载（禁写）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点，见幻灯片序列）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Englert 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | spontaneous symmetry breaking | 自发对称性破缺 | 1964 BEH 机制，规范玻色子获得质量 | 核心贡献页 |
| 1 | quantum field theory | 量子场论 | 带电有质量矢量玻色子自洽理论 | 机制页 |
| 2 | statistical physics | 统计物理 | 铁磁体类比与早期贡献 | 早年/机制页 |
| 3 | cosmology | 宇宙学 | 广义相对论与宇宙学贡献 | 晚期研究页 |
| 4 | string theory | 弦论 | 含超弦与超引力 | 晚期研究页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Robert Brout | 无向 | 康奈尔研究助理时期上司，后 ULB 理论物理组共同主任（1980），1964 BEH 论文合作者 |
| co-honored | Robert Brout | 无向 | 1997 EPS 高能与粒子物理奖、2004 Wolf Prize、2010 Sakurai Prize 共同得主 |
| co-honored | Peter Higgs | 无向 | 2013 诺贝尔物理学奖共享；1997 EPS、2004 Wolf、2010 Sakurai、2013 Asturias 亦共同 |
| co-honored | Gerald Guralnik | 无向 | 2010 J. J. Sakurai Prize 共同得主（GHK 第三篇 1964 论文作者） |
| co-honored | C. R. Hagen | 无向 | 2010 J. J. Sakurai Prize 共同得主（GHK 第三篇 1964 论文作者） |
| co-honored | Tom Kibble | 无向 | 2010 J. J. Sakurai Prize 共同得主（GHK 第三篇 1964 论文作者） |

#### 4.5.1 入库操作

- 以 `name_en='François Englert'`（qid Q151746，库内无记录，seed 新建）为中心写入 `person_relation`
- 对手方：`Peter Higgs`、`Robert Brout`、`Gerald Guralnik`、`C. R. Hagen`、`Tom Kibble` 均库内无记录，seed 以规范全名建 stub（勿给对方编造 qid）
- 方向约定：全部无向（同事/共同荣誉）；种子会自动 from<to 归一

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深沉、思辨、从至暗岁月走向理论之光
- **配色**：深红（Brussels 的沉郁与荣光）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeBEH` BEH 机制 — 深红 `#A63A2B`
  - `badgeVacuum` 真空结构 — 靛蓝 `#4C5FD5`
  - `badgeEw` 电弱理论 — 青绿 `#0E7C7B`
  - `badgeCosmo` 宇宙学/弦论 — 琥珀 `#E07B30`
- **主色**：`#7A1E28`（深红，批内唯一）
- **背景母题**：柔和气泡——铁磁畴的自发排列图案，呼应「真空对称性自发破缺」

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）：左头像 + 右信息网格（生卒、出生地、国籍、教育、任职、主要荣誉、核心领域；师承 page.md 无载，勿填）。
4. 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — BEH 机制共同奠基人 / François Englert 1932–2026 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地 Etterbeek、ULB、Cornell→ULB、Tel Aviv/Chapman、Nobel 2013、核心领域）
03  核心贡献概览 — 自发对称性破缺 / 统计物理 / 宇宙学 / 弦论
04  至暗岁月：藏身的童年 (1932–1945) — 犹太家庭、四镇孤儿院、美军解放（大屠杀幸存者）
05  ULB 学子：从电机工程师到物理学家 (1950s) — 1955 工程师、1959 博士
06  康奈尔岁月：与 Brout 相遇 (1959–1961) — 研究助理→助理教授
07  回到 ULB：理论物理组 (1961–1998) — 1980 与 Brout 共同执掌
08  1964：三篇里程碑论文（核心贡献页）— Brout-Englert 先行，Higgs、GHK 各自独立，PRL 50 周年齐认
09  铁磁体类比：有质量的真空 — 短程/长程相互作用统一于一个机制
10  从机制到证实 — 可重整化（'t Hooft/Veltman 1999）与 LHC 2012 发现
11  荣誉与认可 — Nobel 2013 · Wolf 2004 · Sakurai 2010 · Francqui 1982 · 男爵 2013
12  遗产：电弱理论的基石
13  结尾
```

- 公式框：page.md 无公式，用**概念图式**——「铁磁畴自发排列 ↔ 真空结构类比图」，并注明"示意图，非 page.md 公式"。

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

- 版式：每页写完 `make clean && make`，pdftoppm 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

**Englert 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖归属 | 2013 诺奖**只颁给 Englert 与 Higgs 两人**；Guralnik/Hagen/Kibble 未获诺奖，勿写"六人共享诺奖" |
| 机制命名 | 页面节标题为 Brout–Englert–Higgs–Guralnik–Hagen–Kibble mechanism；通称"Higgs mechanism"时须注明 Brout/Englert 在先，勿让 Higgs 独占 |
| 1964 三篇论文 | Brout–Englert、Higgs、GHK 三篇**各自独立**、路径相似但贡献有别（PRL 50 周年均认定为里程碑），勿写"谁基于谁" |
| 't Hooft/Veltman | 1999 诺奖是**可重整化的证明**，属理论链条而非个人合作关系，禁建 Englert–'t Hooft/Veltman 关系 |
| 大屠杀经历 | 只写 page.md 明载四镇（Dinant/Lustin/Stoumont/Annevoie-Rouillon）与美军解放，勿加戏编造细节 |
| 1978 Gravity Contest | 与 Brout、Gunzig 获 Gravity Research Foundation 作文一等奖（《The Causal Universe》），属征文性质，未入关系库，幻灯片可作趣闻 |
| 双奖同处 2013 | Nobel（与 Higgs）与 Prince of Asturias（与 Higgs + CERN 机构）是两个奖，口径勿混；7 月受封男爵是第三件事 |
| 卒地 | 2026-06-18 逝于布鲁塞尔于克勒（Uccle），勿与出生地 Etterbeek 混淆 |
| 国籍口径 | 主讲比利时（Belgium）；frontmatter 另列 France，yaml 分条记录，正文以 Belgian theoretical physicist 为准 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| spontaneous symmetry breaking | 自发对称性破缺 | 非"对称性自发破坏" |
| Higgs mechanism | 希格斯机制 | 规范玻色子获质量的机制，全名 BEH–GHK |
| gauge vector boson | 规范矢量玻色子 | 机制的作用对象 |
| scalar field | 标量场 | 常称 Higgs field，页面对照写 |
| fermion condensate | 费米子凝聚 | 机制的替代载体 |
| electroweak theory | 电弱理论 | 机制的基石地位 |
| renormalizable | 可重整化 | Englert/Brout 猜想、't Hooft/Veltman 证明 |
| ferromagnet | 铁磁体 | 真空结构的核心类比 |
| Goldstone theorem | 戈德斯通定理 | Higgs 路线的切入点 |
| mass generation | 质量起源 | Wolf Prize 措辞核心词 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Last Hope** — Victor Cooper（戏剧性 / 力量 / 史诗）
- **匹配理由**:
  - "戏剧性/力量" 匹配 Englert 的人生弧线——藏身孤儿院的至暗童年到 81 岁摘取诺奖，最后希望成真
  - "革命性突破" 匹配 1964 年被冷落近半个世纪后由 LHC 证实的机制
- **备选**（未采用）: Through the Darkness（意象合但已预留给批内 Akasaki）、Tragedy（过暗，盖过荣光）
- **本地路径**: `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/François_Englert/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
