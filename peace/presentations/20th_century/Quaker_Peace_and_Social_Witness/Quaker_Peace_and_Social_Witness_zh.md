# 和平奖得主立传提示词（OpenPeace 批次 9：Friends Service Council）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Friends Service Council（公谊服务理事会，今 Quaker Peace & Social Witness，1947 诺贝尔和平奖得主、英国公谊会中央委员会）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业主体。
- **本实例**：Friends Service Council（公谊服务理事会，1927–1978），1979–2000 年更名 Quaker Peace and Service，2001 年起为 Quaker Peace & Social Witness（QPSW）。**本篇主体是机构（is_org=true），不是个人**。
- **设计哲学**：机构立传同样必须有「机构概览页」（替代个人身份信息页）与「事业领域」的结构化表达；本篇的叙事灵魂是「一套见证（testimonies）的制度化」——贵格会的平等、公义、和平、简朴、诚实五项见证，通过一个理事会变成学校、监狱、议会与世界各地的长期项目。

---

## 二、背景信息 【人物专属】

- **目标机构**：Friends Service Council（1927 年成立，今为 Quaker Peace & Social Witness，总部英国）
- **气质关键词**：**贵格见证的制度化者、和平教育的耕耘者、英美双支柱之一** —— 1947 诺贝尔和平奖获奖理由（与美国公谊服务委员会共享、代表贵格会获得）：
  > "for their pioneering work in the international peace movement and compassionate effort to relieve human suffering, thereby promoting the fraternity between nations"（表彰它们在国际和平运动中的开创性工作与减轻人类苦难的仁爱努力，从而促进各国人民之间的友爱）
- **设计母题**：**见证的织线（threads of testimony）**。五项见证（equality/justice/peace/simplicity/truth）如五色织线，贯穿和平教育、修复式司法、经济公义与全球项目——「织线成网」是比「和平鸽」更贴合本机构的视觉语言。本地有历史 logo（Friends_Council_Service_logo.png）可作时代标识。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Quaker_Peace_and_Social_Witness/page.md`（含 frontmatter QID Q677499；维基条目以今名 Quaker Peace and Social Witness 行文）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：事业领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Quaker_Peace_and_Social_Witness` 四件套到 `peace/presentations/pages/20th_century/Quaker_Peace_and_Social_Witness/`（**第一轮已核对，事实基准如下**）：
  - 机构沿革（前身 Friends' Foreign Mission Association 1868–1927 与 Council for International Service 1919–1927 合并组成 Friends Service Council 1927–1978；1979–2000 更名 Quaker Peace and Service；2001 年起为 Quaker Peace & Social Witness）
  - 隶属（英国公谊会年会 Britain Yearly Meeting 的中央委员会之一；英国贵格会〔Religious Society of Friends〕全国组织）
  - 使命（促进英国贵格会的五项见证——平等/公义/和平/简朴/诚实，并与大大小小本土与国际压力团体合作）
  - 1947 诺奖（时名 Friends Service Council，与美国公谊服务委员会 American Friends Service Committee 共享，代表贵格会获奖）
  - 英国和平工作（Peace Campaigning and Networking〔促进对和平见证的理解、推动裁军、反对军国主义〕/ Turning The Tide〔积极非暴力〕/ Peace Education〔支持学校和平教育、冲突解决与同伴调解〕）
  - 社会见证（Economic Issues〔推动英国政府、IMF、世界银行政策变革〕/ Crime & Community Justice〔修复式司法、Circles Scheme〕/ Circles of Support & Accountability〔2007–08 移交 Circles.uk〕/ Quaker Prison Ministers / Quaker Housing Trust / Parliamentary Liaison / Friends Educational Foundation）
  - 全球工作（乌干达和平建设、前南斯拉夫真相与和解促进、中东 EAPPI 项目、QUNO 日内瓦与纽约〔代表 Friends World Committee for Consultation 咨询联合国经社理事会〕、南亚非暴力运动联结）
  - 其他荣誉（Wateler Peace Prize〔frontmatter award_received〕）
  - 关键时间线（10–15 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Quaker_Peace_and_Social_Witness/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Quaker_Peace_and_Social_Witness_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 有历史 logo：`Friends_Council_Service_logo.png`（Friends Service Council 时期徽标）——机构概览页与「沿革」插图首选
- 机构无「肖像」，封面右上角用装饰圆 + 五见证织线意象占位；勿把 Commons 徽标误作肖像

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace education | 和平教育 | 支持学校和平教育、冲突解决与同伴调解 | 英国和平工作页 |
| 1 | disarmament | 裁军 | 和平运动与联络网络，推动裁军、反对军国主义 | 英国和平工作页 |
| 2 | humanitarian aid | 人道主义援助 | 贵格会救援传统——1947 诺奖理由的「减轻人类苦难」口径 | 诺奖页 |
| 3 | restorative justice | 修复式司法 | Crime & Community Justice、Circles Scheme | 社会见证页 |
| 4 | economic justice | 经济公义 | Economic Issues 项目，影响英国政府、IMF、世界银行政策 | 社会见证页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 4 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | American Friends Service Committee | 无向 | 1947 诺贝尔和平奖共同得主（代表贵格会共享） |
| other | Britain Yearly Meeting | — | 本机构是英国公谊会年会的中央委员会之一 |
| other | Friends' Foreign Mission Association | — | 前身机构之一（1868–1927），1927 年合并组建 Friends Service Council |
| other | Council for International Service | — | 前身机构之一（1919–1927），1927 年合并组建 Friends Service Council |

- 方向约定：co-honored 无向；other 为机构谱系关系，note 写清语义
- 对手方 name_en 用 manifest 规范名（American Friends Service Committee 为批次 10 manifest 名，本 yaml 建占位记录供其 UPD 回填 QID）；缺失主体由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：简朴、坚韧、绵长的服务传统
- **配色**：青灰蓝（manifest 预分配主色 `#2F4470`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeEdu` 和平教育 — 青绿 `#0E6B5C`
  - `badgeJustice` 修复式司法 — 赭金 `#8C6A2F`
  - `badgeGlobal` 全球项目 — 深紫 `#52307C`
  - `badgeNobel` 1947 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 低饱和的五色织线与贵格会议圆环意象，呼应「见证的织线」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有机构视觉**：右上角装饰圆（主色环 + 五见证织线意象），`draw=coveraccent!50` 细边框；机构概览页可配历史 logo。
2. **封面有属性标注**：顶部副标题或底部状态栏明示 `United Kingdom | Britain Yearly Meeting central committee`，底部状态栏给出 `属性 | 隶属 | 主要奖项` 三要素。
3. **必须有机构概览页**（替代个人身份信息页）：封面之后、核心贡献之前。左历史 logo + 右信息网格，含至少：成立年份（1927，Friends Service Council）、三次更名沿革、隶属（英国公谊会年会）、使命（五项见证）、主要项目板块、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 贵格见证的织线 / Friends Service Council 1927 + 四色 badge + 国别行
02  机构概览页（★ 必做，替代身份信息页）— 左历史 logo + 右信息网格（沿革、隶属、使命、项目板块）
03  核心贡献概览 — 和平教育 / 裁军倡导 / 人道救援传统 / 修复式司法 / 经济公义
04  沿革：从海外传教协会到服务理事会 (1868–1927) — FFMA 与 CIS 合并组建 Friends Service Council
05  1947 诺贝尔和平奖 — 与美国公谊服务委员会共享、代表贵格会获奖、理由逐句呈现
06  贵格见证：五条织线 — 平等/公义/和平/简朴/诚实的见证体系
07  英国和平工作 — Peace Campaigning / Turning The Tide 积极非暴力 / 学校和平教育
08  社会见证：从监狱到议会 — 修复式司法与 Circles、贵格监狱牧灵、住房信托、议会联络
09  经济公义项目 — 与草根组织合作推动英国政府、IMF、世界银行政策变革
10  全球工作版图 — 乌干达、前南斯拉夫、南亚；QUNO 代表 FWCC 咨询联合国经社理事会
11  三次更名，一条主线 (1978–2001) — Quaker Peace and Service 1979、QPSW 2001
12  遗产：服务即见证 — 与 AFSC 的英美双支柱、Wateler Peace Prize、今日 QPSW
13  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**本机构特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 机构名称 | 1947 年获奖时的名字是 **Friends Service Council**（名录与诺奖口径）；今名 Quaker Peace & Social Witness 只是 2001 年起的现名。全篇以获奖时名为主线，沿革页交代两次更名 |
| 共享得主 | 1947 与 American Friends Service Committee（美国公谊服务委员会，批次 10 篇）共享、**代表贵格会**（on behalf of the Quakers）获奖；勿写「英国方独享」或「两个机构各自得奖」 |
| 成立年份 | Friends Service Council 成立于 **1927**（前身机构合并年）；勿把前身 FFMA 的 1868 当作成立年，也勿用 QPSW 的 2001 |
| 创始人 | 本机构无个人创始人——由两个前身机构合并组建、隶属英国公谊会年会；勿把任何领导人写成创始人，也不写领导人名单（page.md 未载） |
| 隶属方向 | 本机构是 Britain Yearly Meeting 的中央委员会之一（下属关系）；勿写成「英国年会隶属本机构」 |
| QUNO 归属 | page.md 明载 QUNO 代表 **Friends World Committee for Consultation**（非本机构）咨询联合国经社理事会；QUNO 仅作为全球工作版图的条目提及，不建库关系 |
| 中东项目 | EAPPI 等海外项目只写 page.md 明载的项目名与事实（「派人权观察员陪同和平活动人士的非暴力行动」），不加任何立场与评价性语句 |
| Circles 移交 | Circles of Support & Accountability 于 2007–08 移交 Circles.uk，贵格会志愿者可继续参与——按 page.md 客观记录 |
| 无载禁写 | 不写成立大会日期与首任书记姓名、不编造救助数字与年代清单、不从诺奖颁奖词反推组织架构、不写 AFSC 与本机构的人员往来细节（page.md 未载） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Friends Service Council | 公谊服务理事会 | 1927–1978 用名，1947 获奖时名 |
| Quaker Peace & Social Witness | 贵格和平与社会见证（QPSW） | 2001 年起现名 |
| Britain Yearly Meeting | 英国公谊会年会 | 英国贵格会全国组织，本机构隶属之 |
| Religious Society of Friends | 公谊会/贵格会 | 与美国分支 AFSC 区分 |
| testimonies | （贵格）见证 | 平等/公义/和平/简朴/诚实五项，勿译作「证词」 |
| American Friends Service Committee | 美国公谊服务委员会 | 1917 成立，1947 共同得主 |
| restorative justice | 修复式司法 | 与报应性司法（retributive）相对 |
| Turning The Tide | 「力挽狂澜」项目 | 积极非暴力培训项目 |
| QUNO | 贵格联合国办事处 | 代表 FWCC 而非本机构咨询经社理事会 |
| Wateler Peace Prize | 瓦特勒和平奖 | frontmatter 明载的另一奖项 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（manifest 预分配，勿改）
- **风格**: 纪录片 / 深潜 / 微光感
- **匹配理由**:
  - "The Invisible Light" 呼应贵格会的气质——不事声张的服务传统像一束看不见的光，从 1927 年的理事会照进学校、监狱与世界各地的项目现场
  - 曲名的纪录片质感匹配机构立传的叙事：三次更名、一条主线，织线绵延百年
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav` → `presentations/20th_century/Quaker_Peace_and_Social_Witness/The_Invisible_Light.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Quaker_Peace_and_Social_Witness/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/Quaker_Peace_and_Social_Witness/images.txt` | 插图 URL（历史 logo） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Quaker_Peace_and_Social_Witness.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
