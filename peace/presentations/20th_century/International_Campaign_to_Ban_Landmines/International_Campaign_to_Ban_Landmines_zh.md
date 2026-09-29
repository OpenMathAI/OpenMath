# 和平奖得主立传提示词（OpenPeace 批次 20 · International Campaign to Ban Landmines）

> 本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」之一，对象为**组织机构**：
> 国际禁止地雷运动（International Campaign to Ban Landmines，ICBL，1997 诺贝尔和平奖共同得主）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **本实例**：International Campaign to Ban Landmines（国际禁止地雷运动，NGO 联盟）——**组织机构条目**。
- **设计哲学**：组织机构立传用**「机构概览页」（Organization Overview）替代身份信息页**，且强调「使命领域」的结构化表达——这两点构成机构模板的骨架，务必保留。

---

## 二、背景信息 【机构专属】

- **目标机构**：International Campaign to Ban Landmines（1992 年 10 月成立至今，总部日内瓦）
- **气质关键词**：**公民社会的条约引擎、从六家 NGO 到百国网络、幸存者声音的放大器** —— 1997 诺贝尔和平奖获奖理由：
  > "for their work for the banning and clearing of anti-personnel mines"
  > （中译照抄名录：表彰他们为禁止与清除杀伤人员地雷所做的工作）
- **设计母题**：**清雷的白手套（clearing the field）**。把布满地雷的大地还原为可耕可居的家园——「清场」隐喻公民社会把无序军备逐条变成条约义务，是比「断链」更贴合其使命的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/International_Campaign_to_Ban_Landmines/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（OpenPeace 共享封面由主控统一建，若已有 `peace/presentations/cover/` 则优先用之）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：本批已完成「使命领域 + 社会关系入库」（见第 4 / 4.5 步表格），立传时以库内与 yaml 为准，不要另起炉灶。

### 第 0 步：下载并核对数据页面 【机构专属】

- ✅ 已抓取 Wikipedia 页面到 `peace/presentations/pages/20th_century/International_Campaign_to_Ban_Landmines/`（四件套）
- 提取 infobox 与正文，**事实基准如下**（第一轮已核对）：
  - 机构性质：NGO 联盟（coalition of NGOs），非营利；总部瑞士日内瓦（另有里昂、巴黎、渥太华办公点，共 14 名员工）
  - 成立：1992 年 10 月，由六家志同道合组织在纽约结盟——法国 Handicap International、德国 Medico International、英国 Mines Advisory Group、美国 Human Rights Watch / Physicians for Human Rights / Vietnam Veterans of America Foundation；创始人 Jody Williams（首任协调员）
  - 使命：禁止杀伤人员地雷与集束炸弹的使用和扩散；活动遍及约 100 国
  - 里程碑：1997-09 《渥太华条约》在奥斯陆通过 → 1997-12-03 于渥太华由 122 国签署（截至 2018-03 有 164 个缔约国）；条约禁止使用、生产、储存与转让杀伤人员地雷，要求 4 年内销毁库存、10 年内清除雷区
  - 诺奖：1997 与创始协调员 Jody Williams 共同获奖；代表领奖者为共同创始人 Rae McGrath（MAG）与柬埔寨受害者 Tunn Channareth；戴安娜王妃是著名支持者
  - 组织架构：2011 与 Cluster Munition Coalition（CMC）合并为 ICBL-CMC（两运动保持独立并行）；治理委员会（Governance Board）+ 顾问委员会；四位亲善大使：Jody Williams、Tun Channareth、Song Kosal（均为柬埔寨受害者）、Margaret Arech Orech（乌干达受害者）
  - 监测机制：Landmine and Cluster Munition Monitor（1998 创建，ICBL-CMC 研究监测臂），de facto 监测渥太华条约与 2008 集束弹药公约的履约——NGO 首次协调持续监测人道法/裁军条约的「公民社会核证」实践
  - 关键时间线（15–20 节点）：1992-10 六组织结盟 → 1992–1998 Williams 任协调员 → 1997-09 奥斯陆通过条约 → 1997-12-03 渥太华 122 国签署 → 1997 诺奖 → 1998 Monitor 创建 → 1999 条约生效 → 2008 集束弹药公约 → 2011 与 CMC 合并 → 2018 164 缔约国 → 今日倡导、监测、幸存者援助三线并行
- 图片资源：领奖现场照片（1997 Friedensnobelpreisverleihung）与斯里兰卡受地雷伤害的大象照片已在 page.md

### 第 1 步：建立目录 【模板通用】

- `peace/presentations/20th_century/International_Campaign_to_Ban_Landmines/` 已在（提示词所在），建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 参照 OpenPeace 已完成成品或 Kenneth_G_Wilson/Makefile，设置 `MAIN=International_Campaign_to_Ban_Landmines_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【机构专属】

- 下载领奖现场照片（250px 改 600px）到 `images/` 并 `file` 验证；404 则用 Commons `Special:FilePath/<文件名>?width=600` 回退；再失败用装饰图形占位（机构条目可用领奖照当主视觉）

### 第 4 步：使命领域梳理（已入库） 【模板通用，机构专属内容】

**ICBL 的使命领域（按 rank 排序，与 yaml/DB 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | disarmament | 裁军 | 禁止杀伤人员地雷与集束弹药 | 使命页 |
| 1 | humanitarian mine action | 人道主义扫雷行动 | 面向雷患社区的清除与援助 | 行动页 |
| 2 | international law | 国际法 | 渥太华条约与集束弹药公约监测 | 条约页 |
| 3 | public advocacy | 公共倡导 | 倡议、传播与媒体动员 | 倡导页 |

### 第 4.5 步：社会关系（已入库） 【模板通用，机构专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Jody Williams | Williams→机构 | 创始人兼首任协调员（1992–1998） |
| founder | Rae McGrath | McGrath→机构 | 共同创始人（Mines Advisory Group），代表领奖 |
| co-honored | Jody Williams | 无向 | 1997 诺贝尔和平奖共同得主 |
| other | Cluster Munition Coalition | 无向（合并） | 2011 合并组建 ICBL-CMC，两运动保持独立并行 |

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：紧迫、公民行动的力度、大地的归还
- **配色**：主色深绛红 `#7A1E28`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeTreaty` 条约进程 — 靛蓝 `#4C5FD5`
  - `badgeMonitor` 监测核证 — 青绿 `#0E7C7B`
  - `badgeSurvivor` 幸存者网络 — 琥珀 `#E07B30`
  - `badgeAdvocacy` 公共倡导 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「清雷的白手套」母题——深色圆点渐次褪去象征雷区被逐块清除

### 第 6 步：规划幻灯片序列 【机构专属，可微调】

```
00  OpenPeace 项目首页（\input 共享封面）
01  封面 — 公民社会的条约引擎 / ICBL 1992– + 四色 badge + 领奖照 + 「国际组织」行
02  机构概览页（★ 必做，替代身份信息页）— 左领奖照 + 右信息网格（成立、创始人、
    六家创始组织、总部、使命、规模 100 国、核心成就）
03  使命概览 — 裁军 / 人道主义扫雷 / 国际法 / 公共倡导
04  起点：六组织的结盟 (1992) — 法德英美六家 NGO 纽约结盟、Williams 首任协调员
05  从两人办公室到百国网络 — 1,300 家 NGO、受害者/妇女/宗教/环境团体联合
06  渥太华进程 (1997) — 奥斯陆通过、渥太华 122 国签署、条约五大义务
07  1997 诺贝尔和平奖 — 与 Williams 共享、McGrath 与 Channareth 代表领奖
08  条约生命线 — 4 年销毁库存/10 年清除雷区/幸存者援助/缔约扩散
09  Monitor：公民社会核证 (1998–) — 首个 NGO 协调监测人道法条约的机制
10  集束弹药与合并 (2008–2011) — CMC、ICBL-CMC 统一架构、两运动并行
11  幸存者的声音 — Tun Channareth、Song Kosal、Margaret Arech Orech 三大使
12  盟友与支持者 — 戴安娜王妃的声援、各国政府与红十字体系合作
13  遗产：从渥太华条约到今天的雷患地图
14  结尾
```

### 第 7–8 步：版式要点 + 机构专属陷阱表 【模板通用 + 机构专属】

**ICBL 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 创始结构 | 1992 由**六家组织**结盟，Jody Williams 为创始**协调员**（founding coordinator）——勿写成她一人创办组织，也勿漏六组织名单 |
| 创始人双口径 | infobox 写 Founder=Jody Williams；正文又载代表领奖者是「its co-founder Rae McGrath」——两者并列客观呈现，勿取舍定谳 |
| 领奖代表 | 1997 代表领奖的是 Rae McGrath 与柬埔寨受害者 **Tunn** Channareth——勿写成 Williams 代表组织领奖 |
| 诺奖「共同」 | 1997 是 ICBL（组织）与 Williams（个人）共同获奖，理由句 "for their work for the banning and clearing of anti-personnel mines" |
| 条约通过/签署 | 1997-09 奥斯陆**通过**、1997-12-03 渥太华**签署**（122 国）——两城两日期勿互换；164 缔约国是 2018-03 口径 |
| 条约别称 | 官方全名 The Convention on the Prohibition...，通称 Mine Ban Treaty / Ottawa Treaty / Ottawa Convention——篇内统一一种并首次注明 |
| 合并表述 | 2011 是 ICBL 与 CMC **合并为统一架构 ICBL-CMC**，但两运动保持独立——勿写成「并入」或「解散」 |
| 集束弹药公约 | 是 2008 年另一公约（CMC 主导成果），Monitor 同时监测两约——勿把集束弹药写成渥太华条约内容 |
| 政治红线 | 涉及具体国家履约争议只作 page.md 明载客观事实记录，不加评价性语句 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| anti-personnel mine | 杀伤人员地雷 | 勿译「反人员地雷」 |
| Mine Ban Treaty | 禁雷条约 | 通称渥太华条约 |
| Ottawa Treaty | 渥太华条约 | 1997-12-03 签署 |
| coalition | 联盟 | NGO 联合体，非单一组织 |
| founding coordinator | 创始协调员 | Williams 的准确头衔 |
| cluster munition | 集束弹药 | 2008 公约对象 |
| Landmine and Cluster Munition Monitor | 地雷与集束弹药监测 | ICBL-CMC 监测臂 |
| civil society-based verification | 公民社会核证 | Monitor 的机制意义 |
| humanitarian mine action | 人道主义扫雷行动 | 清除+援助总称 |
| explosive remnants of war | 战争遗留爆炸物（ERW） | Monitor 监测对象之一 |
| universalization | 普遍化 | 争取非缔约国加入的术语 |
| non-State armed groups | 非国家武装团体 | 禁雷规范约束对象 |

---

## 四、背景音乐选择 【机构专属，manifest 预分配勿改】

- **选定曲目**: **PAST** — Alex-Productions
- **风格**: 历史感 / 深沉 / 追溯
- **匹配理由**: 「往昔」匹配 20 世纪战争遗留地雷的漫长阴影与其为历史创伤缔结条约的使命感；深沉感匹配幸存者叙事的庄重；历史感匹配从 1992 结盟到 1997 条约五年冲刺的奠基时代
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`
- **时长**: 与 14–16 页成片用 ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/International_Campaign_to_Ban_Landmines/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/International_Campaign_to_Ban_Landmines.yaml` | 领域/关系入库母本 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
