# OpenPeace 机构立传提示词（本实例：International Atomic Energy Agency 国际原子能机构）

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与 OpenPeace 20 世纪 104 位得主批次的实战经验。
- **本实例**：International Atomic Energy Agency（IAEA，国际原子能机构）—— 2005 年诺贝尔和平奖得主（与其时任总干事 Mohamed ElBaradei 共享），**政府间组织机构篇**。
- **设计哲学**：机构立传与个人立传的核心差异，在于以「使命 + 治理结构 + 历任领导」替代个人生平；以**机构概览页**替代身份信息页承载基本盘，并把三大使命（和平利用 / 保障监督 / 核安全）做成结构化领域表——这两点构成机构篇骨架，务必保留。

---

## 二、背景信息 【机构专属】

- **机构全称**：International Atomic Energy Agency（IAEA，国际原子能机构），1957-07-29 依《国际原子能机构规约》生效而成立，总部奥地利维也纳。
- **获奖**：2005 年诺贝尔和平奖，与其时任总干事 Mohamed ElBaradei 共享同一理由句。
- **官方获奖理由 EN**（Nobel 官方原文，照抄勿改写）：
  > "for their efforts to prevent nuclear energy from being used for military purposes and to ensure that nuclear energy for peaceful purposes is used in the safest possible way"
- **官方获奖理由中译**（照抄名录 `OpenPeace_21st_Century_Nobel_Laureates.md`，禁止改写）：表彰他们为防止核能被用于军事目的、并确保和平利用核能以最安全的方式进行所做的努力。
- **气质关键词**：**核安全的守望者、防扩散的技术基石、维也纳的多边论坛**。
- **设计母题**：**原子与盾（atom & shield）**——克制化的放射符号与原子轨道细线、条约文本纹理、全球监测站点连线，呼应「让核能只用于和平」的机构使命；背景沿用柔和气泡母题，避免任何武备化视觉。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/International_Atomic_Energy_Agency/page.md`（Wikipedia 全文 + frontmatter，事实基准以此为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「使命领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【机构专属，已核对 page.md】

- **机构性质**：政府间组织；联合国体系内的自主组织，有自己的创始条约（IAEA Statute），同时向联合国大会与安全理事会报告；与经社理事会不同，大量工作对接安理会。
- **成立日期**：《规约》1956-10-23 批准，**1957-07-29 生效**（infobox Formation 口径，统一采用此日）。
- **成立背景**：冷战核军备竞赛；艾森豪威尔总统 1953 年联大「Atoms for Peace」演讲被公认催化了机构建立，条约在美国批准后于 1957-07-29 生效。
- **总部与全球站点**：维也纳（总部，UN Office at Vienna）；日内瓦（联络处）、纽约（联络处）、多伦多（区域保障监督办）、东京（区域保障监督办）、摩纳哥（实验室）、Seibersdorf（实验室）、的里雅斯特（实验室）。
- **规模**：181 个成员国（正文口径）；2022 年专业与一般服务人员 2556 人。
- **三大使命**：Peaceful uses（促进核能和平利用）/ Safeguards（保障监督，核查核能不被用于军事目的）/ Nuclear safety（推动高水准核安全，含辐射防护）。
- **治理结构**：三大主体——Board of Governors（理事会，35 国规模、负责政策与预算）、General Conference（大会，全体成员国一年一会）、Secretariat（秘书处，总干事领导六大部门：核能、核安全与安保、核科学与应用、保障监督、技术合作、管理）。
- **预算**：2014 年正规预算约 3.44 亿欧元 + 自愿捐款的技术合作基金（目标约 9000 万美元量级）。
- **关键荣誉**：Nobel Peace Prize 2005（与 Mohamed ElBaradei 共享）。
- **关键时间线（20 节点）**：
  1. 1946 联合国原子能委员会（UNAEC）成立
  2. 1949 UNAEC 停止工作，1952 正式解散
  3. 1953-12 艾森豪威尔联大「Atoms for Peace」演讲
  4. 1954-09 美国向联大提议创设国际机构管控裂变材料
  5. 1955-08 日内瓦和平利用原子能国际会议
  6. 1956-10-23 《IAEA 规约》获批准（12 国谈判起草，1955–1957）
  7. 1957-07-29 《规约》生效，机构成立
  8. 1957-12 W. Sterling Cole 出任首任总干事（1957–1961）
  9. 1961-12 Sigvard Eklund 出任第二任总干事（1961–1981，任职 20 年）
  10. 1968 《不扩散核武器条约》（NPT）通过，非核武国须与 IAEA 签保障监督协定
  11. 1981-12 Hans Blix 出任第三任总干事（1981–1997）
  12. 1986 切尔诺贝利事故后全面强化核安全工作
  13. 1997-12 Mohamed ElBaradei 出任第四任总干事（1997–2009）；同年 Model Additional Protocol 通过
  14. 2001 九一一事件后设立核安全计划与 Nuclear Security Fund
  15. 2003 伊拉克核查；3 月向安理会指出尼日尔铀文件不实
  16. 2004 发起 PACT（Programme of Action for Cancer Therapy）癌症治疗行动计划
  17. 2005 与 ElBaradei 共获诺贝尔和平奖
  18. 2009-12 Yukiya Amano 出任第五任总干事（2009–2019）
  19. 2011 福岛第一核电站事故后加强国际安全审议
  20. 2019-12 Rafael Grossi 出任第六任总干事（首位拉丁美洲总干事）；2022-09 赴扎波罗热核电站完成战区首次核查

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `International_Atomic_Energy_Agency/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 OpenPeace 已完成篇目 Makefile，设置 `MAIN=International_Atomic_Energy_Agency_zh`、`VIDEO_NAME=International_Atomic_Energy_Agency_zh`

### 第 3 步：收集图片 【机构专属】

- 可用 page.md 内嵌图：Vienna International Center（总部所在地）、IAEA member states 分布图、IAEA Expert Mission（2022 扎波罗热核查照）等
- 机构无「肖像」概念，封面用维也纳国际中心照片或机构徽识构图；图源 404 则装饰圆占位，勿用领导人照片冒充机构徽识

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear safeguards | 核保障监督 | 技术性核查成员国核申报的正确与完整 | 使命页·保障监督 |
| 1 | nuclear non-proliferation | 核不扩散 | NPT 框架下对核计划的监督执行 | 历史/使命页 |
| 2 | nuclear safety | 核安全 | 切尔诺贝利（1986）与福岛（2011）后两度强化 | 使命页·核安全 |
| 3 | peaceful use of nuclear energy | 核能和平利用 | 三大使命之首，含核科学研发与培训 | 使命页·和平利用 |
| 4 | technical cooperation | 技术合作 | 对成员国（尤其发展中国家）的项目援助 | 技术合作页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，机构专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Mohamed ElBaradei | 无向 | 2005 诺贝尔和平奖共同得主（机构与其时任总干事） |
| colleague | Mohamed ElBaradei | 无向 | 第四任总干事（1997–2009） |
| colleague | Hans Blix | 无向 | 第三任总干事（1981–1997） |
| other | United Nations | 无向 | 1957 年起为联合国体系内自主组织，向联大与安理会报告 |

- **不 入 库（仅叙述）**：Eisenhower（演讲催化，非创始人）；Cole/Eklund/Amano/Grossi/Feruță（历任总干事仅 ElBaradei/Blix 入库，其余在时间线呈现）；181 成员国不建关系。

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：克制、制度感、技术理性
- **配色**：主色 `#14324F`（深海蓝，机构威仪与核安全议题的克制感，manifest 预分配勿改）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeSafeguards` 保障监督 — 青绿 `#0E7C7B`
  - `badgeSafety` 核安全 — 琥珀 `#E07B30`
  - `badgePeaceful` 和平利用 — 靛蓝 `#4C5FD5`
  - `badgeGovernance` 治理结构 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡 + 极细原子轨道弧线，疏密呼应「全球监测网络」的空间感

### 第 6 步：规划幻灯片序列 【机构专属，12 页 + 项目首页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 国际原子能机构 / IAEA 1957– + 四色 badge + 总部图
02  机构概览页（★ 必做）— 成立时间/性质/总部/成员国数/三大使命/历任总干事速览
03  诞生背景 — 冷战核阴影与 Atoms for Peace（1946–1957）
04  三大使命 — 和平利用 / 保障监督 / 核安全
05  治理结构 — 理事会 / 大会 / 秘书处（含六大部门）
06  保障监督与 NPT — 1968 之后的世界核查网络（Additional Protocol 1997）
07  核安全强化 — 切尔诺贝利（1986）与福岛（2011）
08  历任总干事 — Cole → Eklund → Blix → ElBaradei → Amano → Grossi
09  ElBaradei 时代与 2005 诺奖（与个人篇互链）
10  全球站点与技术合作 — PACT 癌症治疗行动计划、区域协作协定
11  2005 诺贝尔和平奖 — 官方理由 + 奥斯陆演讲要点
12  结尾
```

### 第 7 步：版式要点 【模板通用】

- 机构概览页参照个人篇 `\profileslide` 实现模式：左侧机构图 + 右侧信息网格（成立/性质/总部/成员国/三大使命/历任领导）。
- 时间线页 20 节点拆两栏或分两页，`\foreach` 分隔符必须 ASCII 逗号。
- 治理结构页用三栏框（理事会/大会/秘书处），每栏 ≤4 行要点，`arraystretch 0.78` 起。
- 历任总干事表 7 行，`arraystretch 0.62` + 顶部 `-0.35cm` 防溢出。
- 编译硬指标：0 error、vbox ≤10pt、hbox ≤50pt，每写一页即 make 并 `pdftoppm` 目检。

### 第 8 步：史实审查 + 机构专属陷阱表 【人物/机构专属】

| 陷阱 | 说明 |
|------|------|
| 勿写创始人 | IAEA 依条约设立，**无个人创始人**；Eisenhower 演讲只是「催化」，禁写「创立者/奠基人」 |
| 勿把领导人写成创始人 | 历任总干事是行政首长；首任 Cole 是「首任总干事」不是缔造者 |
| 成立日期 | 《规约》1956-10-23 批准、1957-07-29 生效；「成立」统一用 1957-07-29，勿混用两日 |
| 成员国数 | 正文口径 181 个成员国，勿写 UN 193 或其他口径 |
| 诺奖共享结构 | 2005 由 IAEA 与 ElBaradei 共享同一理由句；与 ElBaradei 个人篇共用同一 EN+中译，勿各自改写 |
| 演讲内容 | ElBaradei 奥斯陆演讲要点（军费 1% 可养活世界等）为 page.md 明载转述，按事实呈现，慎用整句引语 |
| 政治敏感 | 伊拉克/伊朗/朝鲜核查、以色列相关争议、俄乌战争中的核电站核查，一律按 page.md 客观记录，不加任何评价性语句 |
| 事故年份 | 切尔诺贝利 1986（乌克兰境内），福岛 2011（日本），两节点年份勿互换 |
| 机构身份 | 页面底部品牌标注统一 `OpenMathAI`；NAFTA/OPCW 等同属 UN 系列的机构仅在系列导航出现，勿混淆 |

### 第 9 步：术语清单 【机构专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| safeguards | 保障监督 | 不是「安保」 |
| Additional Protocol | 附加议定书 | 1997 Model Additional Protocol 语境 |
| Board of Governors | 理事会 | 勿译「管理委员会」 |
| General Conference | 大会 | 每年九月召开 |
| Director General | 总干事 | 勿译「署长/主任」 |
| Statute | 《国际原子能机构规约》 | 1956 批准 / 1957 生效两日期 |
| non-proliferation | 核不扩散 | NPT 语境专用 |
| nuclear security | 核安保 | 与 nuclear safety（核安全）严格区分 |
| PACT | 癌症治疗行动计划 | 2004 年发起，非诺奖理由本体 |
| Atoms for Peace | 「原子为了和平」演讲 | 1953 年艾森豪威尔联大演讲 |

---

## 四、背景音乐选择 ✅ 【机构专属，manifest 预分配勿改】

- **选定曲目**: **Cinematic Experience** — Alex-Productions
- **风格**: 电影感 / 宏大 / 制度叙事
- **匹配理由**:
  - 「宏大」匹配机构近七十年、覆盖全球的核查网络与多边制度长时段演化
  - 「电影感/纪录片气质」匹配从冷战核阴影到战区核查的叙事弧线
  - 庄重克制，呼应核安全议题的严肃性，不喧宾夺主
- **备选**（未采用，仅记录）: PAST（历史感强但受众偏低）、New Lands（开阔但偏探索感）
- **本地路径**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`
- **时长处理**: 曲目时长 > 12 页 × 7 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/International_Atomic_Energy_Agency/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 获奖理由中译照抄来源 |
| `peace/PROMPTS_WORKFLOW.md` + `peace/PROMPTS_WORKFLOW_21ST.md` | 工作流与红线（第 2 节机构规则） |
| `MySQL/data/International_Atomic_Energy_Agency.yaml` | 入库 yaml（与本文件第 4/4.5 步同步） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
