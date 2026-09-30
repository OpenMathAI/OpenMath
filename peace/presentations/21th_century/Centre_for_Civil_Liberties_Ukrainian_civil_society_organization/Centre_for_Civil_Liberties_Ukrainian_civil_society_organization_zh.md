# 和平奖得主立传提示词（OpenPeace 21 世纪：Centre for Civil Liberties）

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 家族项目，品牌口径统一 `OpenMathAI`）。
- **结构标杆**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节 + 身份信息页骨架）。
- **本实例**：Centre for Civil Liberties（公民自由中心，2022 诺贝尔和平奖，乌克兰基辅人权组织）——**组织机构条目**，按 20 世纪工作流第 2 节机构规则执行：省 gender/nationalities，birth_date 用成立日期，「机构概览页」替代身份信息页。
- **设计哲学**：立传以「追问的名字（The Question Needs a Name）」为设计母题——该组织的标志性主张是为战争中每一桩罪行留下可追责的名字；页面视觉以名单长卷与蓝色勋章线贯穿。

---

## 二、背景信息 【人物专属】

- **目标机构**：Centre for Civil Liberties / Центр Громадянських Свобод（2007-05-30 成立于基辅；章程全称 Centre for Civil Liberties Civil Society Organisation）
- **官方获奖理由（2022，与 Ales Bialiatski、Memorial 共享）**：
  > "The Peace Prize laureates represent civil society in their home countries. They have for many years promoted the right to criticise power and protect the fundamental rights of citizens. They have made an outstanding effort to document war crimes, human right abuses and the abuse of power. Together they demonstrate the significance of civil society for peace and democracy."
  > （本届和平奖得主是其母国民间社会的代表。他们多年来倡导批评权力的权利、维护公民的基本权利，并为记录战争罪行、侵犯人权与滥用权力做出了杰出努力。他们共同彰显了民间社会对和平与民主的重要意义。）
- **气质关键词**：**乌克兰首个诺奖、Euromaidan SOS 的发起者、战争罪行的记录者**
- **设计母题**：**追问的名字（a name for every crime）**——Euromaidan 广场的帐篷与法律援助台、克里米亚与顿巴斯的失踪者名单长卷、基辅的蓝色与黄色。
- **本地数据源**：`peace/presentations/pages/21th_century/Centre_for_Civil_Liberties_Ukrainian_civil_society_organization/page.md`

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准 【人物专属，第一轮已核对】

- 成立：2007-05-30（基辅，乌克兰）
- 性质：人权组织（civil society organization）；主席（chairwoman）：Oleksandra Matviichuk（乌克兰律师）
- 名称口径：章程全称 Centre for Civil Liberties Civil Society Organisation，缩写 Centre for Civil Liberties；官网多自称 **Center** for Civil Liberties——立传统一用 manifest 名 Centre for Civil Liberties，"Center/Centre" 拼写在陷阱表注明即可，勿全篇强行统一
- 宗旨与活动：推动乌克兰立法修订使国家更民主；加强对执法机构与司法机关的公众监督；推动《乌克兰刑法典》修订
- 关键节点行动：① 2013–2014 Euromaidan 期间发起 **Euromaidan SOS** 项目（为抗议者提供法律援助、监测亚努科维奇安全部队的滥用行为）；② 2014 克里米亚被吞并与顿巴斯战争开始后，记录克里米亚的政治迫害与 Luhansk/Donetsk 人民共和国控制区的罪行，发起释放被非法关押者的国际运动；③ 2022 俄入侵后记录战争罪行（挪威诺奖委员会 2022 评价其 "playing a pioneering role in holding guilty parties accountable for their crimes"）
- 关键荣誉：Right Livelihood Award（frontmatter 载，年份 page.md 未展开——展示时只列奖项名，不标年份）；Nobel Peace Prize 2022（三人共享，2022-10-07 公布）；2022-10-08 Matviichuk 记者会表示泽连斯基及政府官员尚未致贺（原因猜测照录其本人说法）；2024-03/04（"spring 2024"）被俄罗斯列 "undesirable organization"
- 时间线（12–15 节点）：2007-05-30 成立（基辅）→ 推动刑法典与执法监督立法 → 2013–2014 Euromaidan SOS → 2014 克里米亚/顿巴斯记录与释放运动 → 2022-02 俄入侵后记录战争罪行 → 2022-10-07 诺贝尔和平奖（乌克兰公民或组织首获诺奖）→ 2022-10-08 记者会（致贺情况）→ 2022-11 Matviichuk 呼吁各国提供武器解放被占领土（其公开立场，照录）→ 2024 春 被俄列"不受欢迎组织"
- 页面极短（约 50 行）：幻灯片规划**宁缺毋滥**（12 页即可），事实全部来自 page.md，不得外扩

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Centre_for_Civil_Liberties_Ukrainian_civil_society_organization/` 与 `images/`（目录名含消歧义后缀，manifest 已定，勿截短）
- 数据源已在 `peace/presentations/pages/21th_century/Centre_for_Civil_Liberties_Ukrainian_civil_society_organization/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已立传目录的 Makefile，设置 `MAIN=Centre_for_Civil_Liberties_Ukrainian_civil_society_organization_zh`（名称过长时 Makefile 变量仍须全名，勿截短以免产物名与目录名错位）
- 共享封面 `\input{../../cover/openpeace_page.tex}`（若 21 世纪目录暂无 cover，沿用 20 世纪共享封面，主控统一收口）

### 第 3 步：收集图片 【人物专属】

- page.md 无内嵌图像、infobox 无徽标——本篇**无真实图像可用**，全篇用装饰元素：蓝黄双色圆 + 金色名单长卷条带
- 如 Review 阶段需要实景图，仅可自 Wikimedia Commons 查 Euromaidan 自由许可照片（图注标明摄影师与许可），且不与 page.md 事实绑定
- 禁用 CCL 官网版权图片

### 第 4 步：使命领域表 【人物专属（机构）】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | civil liberties | 公民自由 | 机构名称即使命、立法倡导核心 | 使命页 |
| 1 | human rights | 人权 | 三阶段行动（广场/占领区/战争）主线 | 行动页 |
| 2 | democracy promotion | 民主促进 | 推动乌克兰立法与公众监督 | 立法页 |
| 3 | war crimes documentation | 战争罪行记录 | 2022 起核心工作、诺奖理由词 | 记录页 |
| 4 | rule of law | 法治 | 刑法典修订、执法与司法公众监督 | 法治页 |

### 第 4.5 步：社会关系表 【与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ales Bialiatski | 无向 | 2022 诺贝尔和平奖共同得主 |
| co-honored | Memorial | 无向 | 2022 诺贝尔和平奖共同得主 |
| colleague | Oleksandra Matviichuk | 无向 | 主席（chairwoman），乌克兰律师，获奖后该组织公开形象代表 |

### 第 5 步：配色方案 【人物专属】

- **主色**：`#52307C`（manifest 预分配深紫——庄重、追问、公民抗命；勿改）
- **辅助**：诺奖香槟金 `#C9A227`
- **四分类色**：badgeA 公民自由 `#7A5CA3`；badgeB 人权记录 `#2E7D9A`；badgeC 民主法治 `#C9A227`；badgeD 战争罪行档案 `#8B4A3A`
- **背景母题**：深紫底上拉长的名单长卷条带与细金线（追问的名字意象），疏密错落

### 第 6 步：幻灯片序列（12 页规划，机构概览页替代身份信息页；页面短，宁缺毋滥）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 追问需要一个名字 / Centre for Civil Liberties 2007– + 四色 badge
02  机构概览页（★ 必做）— 信息网格（成立、总部、性质、主席、荣誉、使命）
03  使命概览 — 公民自由 / 人权 / 民主促进 / 战争罪行记录 / 法治
04  起源 (2007) — 基辅、立法倡导、刑法典与公众监督
05  Euromaidan SOS (2013–2014) — 法律援助、滥用监测
06  占领区记录 (2014–2021) — 克里米亚与顿巴斯、释放运动
07  战争罪行记录 (2022–) — 诺奖委员会"追责先锋"评价照录
08  2022 诺贝尔和平奖 — 三人共享（与 Bialiatski、Memorial 并列；乌克兰首获诺奖）
09  压迫与延续 — 2024 被俄列"不受欢迎组织"、工作继续
10  遗产：公民社会的追问
11  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

- 版式：页面短 → 每帧信息密度低，用大字号引语与留白撑版面；禁编造细节填充。
- **陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 拼写双口径 | 章程/manifest 用 **Centre**，官网自称 **Center**——正文统一 Centre，概览页可注"官网亦作 Center"，勿全篇混用 |
| 获奖理由 | 2022 三人共享长句主语 "The Peace Prize laureates"（复数），照录全段，勿改单人句；EN 含 "human right abuses"（原文如此），禁"纠正" |
| 首个诺奖 | "first ever Nobel Prize awarded to a Ukrainian citizen or organization"（page.md 明载）——照录"乌克兰公民或组织首次获诺奖"，勿写成"乌克兰人首次提名/获奖"泛化 |
| 致贺事件 | 2022-10-08 Matviichuk 说泽连斯基等未致贺、原因仅其本人猜测（"刚出差回来"）——照录其说法与语境，禁写成事实断言或引申 |
| 武器呼吁 | 2022-11 Matviichuk 呼吁提供武器解放被占领土——系其公开立场，照录归属，不加评价；涉及俄乌战争全部内容仅客观记录 |
| Right Livelihood 年份 | frontmatter 载获奖但 page.md 正文未展开年份——展示只列奖项名不标年份，禁编造 |
| 姊妹条目混淆 | 与 Memorial 是两个独立机构（俄/乌各一），共享诺奖但无隶属/合并关系，禁写"乌克兰分支"之类表述 |
| 成立时间 | 2007-05-30，infobox 与正文一致；勿与 2013 Euromaidan SOS 启动年混写"2013 成立" |
| Sakharov 奖区分 | 本组织无欧洲议会 Sakharov Prize；勿与 Memorial（2009）、Mohammadi（APS 2018）的萨哈罗夫奖混淆 |
| 无载禁写 | 创始人姓名（page.md 未载除 Matviichuk 外的创始人）、员工数、具体获释者名单、Euromaidan SOS 具体案例——一律不写 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Centre for Civil Liberties | 公民自由中心 | 章程缩写 CCL；官网 Center 拼写并存 |
| Euromaidan SOS | 广场之春 SOS | 2013–2014 法律援助项目名，保留 SOS 原文 |
| Euromaidan | 欧洲迈丹（亲欧盟示威） | 2013–2014 基辅抗议运动通称 |
| chairwoman | 主席 | Oleksandra Matviichuk，乌克兰律师 |
| undesirable organization | 不受欢迎组织 | 俄罗斯 2024 认定，加引号使用 |
| war crimes | 战争罪行 | 诺奖理由核心词，记录主体限定 page.md 载明范围 |
| Criminal Code of Ukraine | 乌克兰刑法典 | 立法倡导对象 |
| accountability | 追责 | 诺奖委员会评价用词，照录 |
| civil society | 公民社会 | 三得主共享理由核心词 |
| prisoner release campaign | 释放被非法关押者运动 | 2014 起，克里米亚/顿巴斯语境 |
| public control | 公众监督 | 对执法机构与司法机关，立法倡导语境 |
| document | 记录/存档 | 本组织核心动词，诺奖理由 "document war crimes" |
| Kyiv | 基辅 | 官方英文转写用 Kyiv，不用 Kiev（页面口径） |
| founding year | 成立年份 | 2007-05-30（infobox 与正文一致，无噪声） |
| ZMINA | ZMINA 人权中心 | 仅在 Memorial 篇 OSCE 奖语境出现，本篇禁写 |

---

## 四、背景音乐选择 【manifest 预分配，勿改】

- **选定曲目**：**Through the Darkness** — Audiomachine（inspiring-electronic）
- **匹配理由**：
  - "穿越黑暗" 直接对应其十年三阶段记录（广场→占领区→全面战争）的行动弧线
  - Audiomachine 的推进感匹配"追问"的持续性与名单长卷的累积意象
  - 曲末上扬留给 2022 诺奖页——黑暗中的高光时刻
- **备选**（未采用，勿替换）：
  - ★★ Empire Collapse（更宏大，但已分配 Nihon Hidankyo，禁撞曲）
  - ★ The Invisible Light（意象近，已分配 2009 得主，禁撞曲）
  - ★ Ascension（上扬感强，已分配 2008/2025 得主，禁撞曲）
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → 立传目录 `Through the Darkness.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Centre_for_Civil_Liberties_Ukrainian_civil_society_organization/page.md` | 本地 Wikipedia 正文（事实基准，约 50 行极短页） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本（机构条目省 gender/nationalities） |
| `peace/PROMPTS_WORKFLOW_21ST.md` | 21 世纪工作流（红线） |

---

## 六、执行清单 【逐项交付物，完成一项勾一项】

1. ☐ 通读 `page.md`（已完成事实核对，本文件第 0 步即基准）；页面极短，**宁可页面少，不可事实注水**
2. ☐ 建目录 `peace/presentations/21th_century/Centre_for_Civil_Liberties_Ukrainian_civil_society_organization/images/`；page.md 无内嵌图，infobox 头像缺位——用蓝黄双色装饰圆 + 金线长卷元素占位
3. ☐ 复制 BGM 到立传目录，`file` 验证音频
4. ☐ 按 manifest 主色 `#52307C` 写 tex，头部宏注释写明语义；封面国籍行「乌克兰」
5. ☐ 按第 6 步序列写 12 帧：机构概览页 ★ 必做；每页编译 0 error、vbox≤10pt、hbox≤50pt
6. ☐ `pdftoppm` 逐页目检溢出/重叠/缺字（★ U+2605 缺字、带圈数字 `\xeCJKDeclareCharClass`）
7. ☐ yaml 已入库（`MySQL/seed_person.py data/Centre_for_Civil_Liberties_Ukrainian_civil_society_organization.yaml`，幂等），验证 `has_social_data=1`、fields=5、relations=3
8. ☐ Review-1 对照第 8 步陷阱表逐条核查（重点：Centre/Center 拼写、致贺事件归属、共享理由复数主语）
9. ☐ make images + make video 出 mp4
10. ☐ 向主控汇报一行（格式见第 3 节）

---

## 七、版式补遗 【本篇专属排版要点】

- **第 2 页机构概览页**：信息网格六行（成立/总部/性质/主席/荣誉/使命），右侧放蓝黄装饰圆；无徽标可用 Unicode 纹样替代，禁用站外 logo 版权图。
- **第 5–7 页（三阶段）**：统一用「时间 + 地点 + 行动」三行卡片式排版，左列年份 24pt 粗体，视觉连续性即"长卷"母题。
- **第 8 页诺奖页**：citation 长句 quote 环境 8.5pt；"乌克兰首获诺奖"做金色高亮徽章；三得主 badge 并列。
- **第 9 页**：'undesirable organization' 术语加引号；「工作继续」一句收尾即可，禁渲染。
- **引语红线**：Matviichuk 记者会发言与武器呼吁均为 page.md 明载但系转述语境，作转述不入引文框；诺奖委员会 "pioneering role" 评价系 page.md 直接引语，可入引文框并标注委员会归属。
- **结尾页品牌**：底部统一 `OpenMathAI`；引号用半角 `" "`。
- **短页纪律**：page.md 仅约 50 行，本篇 12 页是下限而非目标；执行中发现任何一帧无 page.md 事实可依，直接删帧合并，宁少勿编。
- **三阶段视觉锚**：第 5/6/7 页左上角统一放「Ⅰ 广场 / Ⅱ 占领区 / Ⅲ 战争」罗马数字徽标（避免带圈数字缺字问题）。

> **开始执行。每完成一步汇报。最重要的事：无载禁写、政治敏感内容只作客观事实记录（俄乌战争相关全部内容无立场表述）。**
