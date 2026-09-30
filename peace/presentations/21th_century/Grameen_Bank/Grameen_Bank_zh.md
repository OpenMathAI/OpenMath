# OpenPeace 机构立传提示词（本实例：Grameen Bank 格莱珉银行）

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与 OpenPeace 20 世纪 104 位得主批次的实战经验。
- **本实例**：Grameen Bank（গ্রামীণ ব্যাংক，格莱珉银行，意为「乡村银行」）—— 孟加拉国小额金融与社区发展银行，2006 年诺贝尔和平奖得主（与创始人 Muhammad Yunus 共享），**国家级机构篇**（所在国 Bangladesh 保留）。
- **设计哲学**：机构立传以「起源 → 建制 → 运作机制 → 全球扩散」替代个人生平；以**机构概览页**替代身份信息页；运作机制（团结小组联保、十六项决定、无抵押信贷）是本篇的灵魂，构成骨架，务必保留。

---

## 二、背景信息 【机构专属】

- **机构全称**：Grameen Bank（格莱珉银行；Bengali 原名 গ্রামীণ ব্যাংক），1976 年缘起于吉大港大学 Muhammad Yunus 的 Jobra 研究项目，1983-10-02 依政府法令转为独立银行；总部达卡。
- **获奖**：2006 年诺贝尔和平奖，与创始人 Muhammad Yunus 共享同一理由句；是 page.md 明载的「唯一获诺贝尔奖的商业企业（only business corporation to have won a Nobel Prize）」。
- **官方获奖理由 EN**（Nobel 官方原文，照抄勿改写）：
  > "for their efforts to create social and economic development from below"
- **官方获奖理由中译**（照抄名录 `OpenPeace_21st_Century_Nobel_Laureates.md`，禁止改写）：表彰他们自下而上促进社会与经济发展的努力。
- **气质关键词**：**穷人的银行、信任抵押的发明者、微型金融的母版**。
- **设计母题**：**门槛与存折（doorstep & passbook）**——银行走进村口、贷款无需抵押、借款人即股东；视觉上以低门槛几何、存折格线、女性剪影点阵呼应「自下而上」；背景沿用柔和气泡母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Grameen_Bank/page.md`（Wikipedia 全文 + frontmatter，事实基准以此为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「使命领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【机构专属，已核对 page.md】

- **机构性质**：statutory public authority（法定公共机构）、小额金融专业社区发展银行；向无抵押能力的贫困者提供小额贷款（microcredit / grameencredit）。
- **成立**：1983-10-02（政府法令授权独立运营）；**起源** 1976 年 Jobra 村研究项目（孟加拉 1974 大饥荒后 Yunus 借出 27 美元给 42 人，多为竹凳匠人）。
- **总部与规模**：达卡（Mirpur-2 总办公大楼）；2,568 家分行（2022）；员工 18,203 人（2022）；借款人近 950 万（2022-01），96.81% 为女性；2021 年底覆盖 81,678 村（全国 87,223 村的约 94%）。
- **所有制**：借款人持股为主（政府股比 1983 年 60% → 2010 年代初降至个位数 → 2010 年代中回升 25%）。
- **运作机制**：
  1. 团结小组（solidarity groups）共同申请、互相扶助；还款责任仍归个人，无正式连带担保
  2. 与借款人不签正式契约——以信任运转；配套小组基金/应急基金小额储蓄
  3. 十六项决定（Sixteen Decisions；2023 年更新为十八项），借款人定期诵读
  4. 1995 年起 90% 贷款由利息收入与存款自筹
  5. 妇女借款人约 97%，借款人即股东
- **关键荣誉**：Nobel Peace Prize 2006（13 Oct 宣布；10 Dec 借款人董事 Mosammat Taslima Begum 代表领奖）；Independence Day Award 1994（孟加拉最高国家奖）；World Habitat Award 1998（低成本住房计划）；Aga Khan International Award for Architecture 1989（住房贷款项目）；Gandhi Peace Prize；Four Freedoms Award – Freedom from Want（frontmatter）；2004 Petersburg Prize（Village Phone，EUR 100,000）。
- **关键事件时间线（20 节点）**：
  1. 1974 孟加拉大饥荒；Yunus 借出 27 美元给 42 人（多为竹凳匠）
  2. 1976 Jobra 村成为项目首个服务点（与 Janata Bank 合作）
  3. 1977–1978 项目扩展至周边村庄
  4. 1979 获孟加拉央行支持扩展至 Tangail 地区
  5. 1982 项目成员达 28,000 人
  6. 1983-10-02 政府法令将项目转为独立银行 Grameen Bank
  7. 1983 年建行初期政府持股 60%
  8. 1984 住房贷款申请三度被央行驳回（$125 不可行/非创收贷款/改称「工厂贷款」仍被驳）
  9. 1983–1984 ShoreBank 银行家 Ron Grzywinski 与 Mary Houghton 协助完成银行注册（福特基金会资助）
  10. 1989 住房贷款项目获 Aga Khan 国际建筑奖；平均住房贷款增至 $300
  11. 1990s 借款人持股成主流（政府股比降至个位数）
  12. 1994 获 Independence Day Award（孟加拉最高国家奖）
  13. 1995 起 90% 贷款由利息与存款自筹
  14. 1998 大洪水冲击还款率，其后数年恢复；低成本住房计划获 World Habitat Award
  15. 2003 启动乞丐专属的 Struggling members program
  16. 2004 Village Phone 计划获 Petersburg Prize（EUR 100,000）
  17. 2005 年初累计放贷逾 47 亿美元；2005 Grameen America 起步
  18. 2006-10-13 与 Muhammad Yunus 共获诺贝尔和平奖
  19. 2011 政府以年龄为由迫使 Yunus 辞职；2013 Grameen Bank Act 取代 1983 法令
  20. 2022–2025 分行 2,568 家、累计放贷逾 2.5 万亿塔卡（约 337.7 亿美元）；2024 Chowdhury 出任董事长；2025 拟议修法降低政府持股（25%→5%）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Grameen_Bank/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 OpenPeace 已完成篇目 Makefile，设置 `MAIN=Grameen_Bank_zh`、`VIDEO_NAME=Grameen_Bank_zh`

### 第 3 步：收集图片 【机构专属】

- 可用 page.md 内嵌图：Grameen Bank Badge（机构徽识）、Grameen Bank Building in Dhaka（总部大楼）、Muhammad Yunus at weforum（创始人代表照）
- 封面用达卡总部大楼或徽识构图；机构无「肖像」，勿用领导人照冒充机构徽识

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microcredit | 小额信贷 | 无抵押小额贷款（grameencredit）核心业务 | 运作机制页 |
| 1 | microfinance | 小额金融 | 存贷一体的小微金融体系 | 运作机制页 |
| 2 | poverty reduction | 扶贫 | 「贷款胜于施舍」的减贫路线 | 使命页 |
| 3 | women's empowerment | 女性赋权 | 97% 借款人为女性的信贷优先 | 女性借款人页 |
| 4 | community development | 社区发展 | 十六项决定与乡村自我治理 | 十六项决定页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，机构专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Muhammad Yunus | 无向 | 创始人，1983 年依政府法令将研究项目转为独立银行 |
| co-honored | Muhammad Yunus | 无向 | 2006 诺贝尔和平奖共同得主 |
| colleague | Ron Grzywinski | 无向 | ShoreBank 银行家，协助完成银行注册组建 |
| colleague | Mary Houghton | 无向 | ShoreBank 银行家，协助完成银行注册组建 |

- **不 入 库（仅叙述）**：Taslima Begum（代表领奖的借款人董事）；Abdul Hannan Chowdhury / Sarder Akhter Hamed（现任领导层）；Grameen 家族企业群（Trust/Fund/Telecom 等为业务分支非人物）；Mjøs（诺奖委员会主席致辞）；Clinton 夫妇（背景叙述）。

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：田野紫的朴素、乡土的温度、制度的坚韧
- **配色**：主色 `#52307C`（深紫，孟加拉乡村黄昏与银行存折的庄重感，manifest 预分配勿改）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeCredit` 小额信贷 — 青绿 `#0E7C7B`
  - `badgeWomen` 女性赋权 — 玫瑰 `#C4204F`
  - `badgeHousing` 住房与社区 — 靛蓝 `#4C5FD5`
  - `badgeNobel` 诺贝尔 — 香槟金 `#C9A227`（强调用）
- **背景母题**：柔和气泡 + 存折格线与田野纹理（低密度）

### 第 6 步：规划幻灯片序列 【机构专属，13 页 + 项目首页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 格莱珉银行 / Grameen Bank 1983– + 四色 badge + 总部图
02  机构概览页（★ 必做）— 性质/成立/总部/分行数/借款人数/女性占比/所有权结构
03  起源（1974–1976）— 大饥荒、27 美元、Jobra 村研究项目
04  建制（1979–1983）— Tangail 扩展、政府法令、独立银行
05  运作机制 — 团结小组联保、周还款、无契约信任
06  十六项决定 — 诵读条文与生活方式改变（2023 更新为十八项）
07  女性借款人 — 97% 女性、借款人即股东
08  住房贷款 — 三次被驳与州长面谈、Aga Khan 建筑奖
09  多元化 — Village Phone（Petersburg Prize）、乞丐计划（Struggling members）
10  全球扩散 — 64+ 国复制、World Bank 计划、Grameen America
11  2006 诺贝尔和平奖 — 官方理由、Taslima Begum 代表领奖、唯一商业企业口径
12  争议与治理（2011–2025）— Yunus 免职、2013 法案、批评两说并陈（全部客观）
13  结尾
```

### 第 7 步：版式要点 【模板通用】

- 机构概览页参照个人篇 `\profileslide` 实现模式：左侧机构图 + 右侧信息网格（性质/成立/总部/规模/所有权/荣誉），事实取自 infobox，不得杜撰。
- 时间线页 20 节点拆两页（1983 建行分界），`\foreach` 分隔符必须 ASCII 逗号。
- 数字密集页（950 万借款人/2,568 分行/97% 女性/98% 回收率）用大数字框 + 短说明。
- 十六项决定页只取 4–6 条代表条文（原文摘译），其余「等」收束，防溢出。
- 编译硬指标：0 error、vbox ≤10pt、hbox ≤50pt，每写一页即 make 并 `pdftoppm` 目检。

### 第 8 步：史实审查 + 机构专属陷阱表 【机构专属】

| 陷阱 | 说明 |
|------|------|
| 勿把领导人写成创始人 | 创始人仅 Muhammad Yunus（page.md 明载 Founder）；Chowdhury/Hamed 是现任领导层，勿写「缔造者」 |
| 两个日期 | 起源 1976（Jobra 项目）≠ 成立 1983-10-02（政府法令）；「成立于」统一用 1983-10-02，1976 写「缘起」 |
| 27 美元口径 | 借给 42 人「mostly bamboo stool makers」（本篇口径）；与 Yunus 篇「42 名村妇」表述各自忠于本页面，勿混改 |
| 名字含义 | Grameen = 孟加拉语「乡村的」；页面明载 "Rural" or "Village" Bank，勿译「格莱美」 |
| 唯一商业企业 | "only business corporation to have won a Nobel Prize" 是 page.md 明载事实，可写 |
| 领奖代表 | 10 Dec 2006 由借款人董事 Mosammat Taslima Begum 在奥斯陆市政厅代表领奖（用 1992 年 16 欧元贷款买羊起家），勿写成 Yunus 代表银行领奖 |
| 回收率口径 | 银行自报回收率约 95–98%，WSJ 2001 曾报五分之一贷款逾期逾一年、Roodman 质疑统计口径：两说并陈，禁单侧叙事 |
| 政治敏感 | 2011 Yunus 免职、2013 Grameen Bank Act、Norad 纪录片风波（2010-12 挪威官方调查后澄清无违规）、2025 修法动议：全部按 page.md 客观记录，不作政治评价 |
| 批评节 | 微贷债务螺旋、Peter Singer 质疑等按 page.md 归属各批评者观点呈现，禁替机构辩护或附和 |
| 机构身份 | 国家级机构篇保留所在国 Bangladesh；页面底部品牌标注统一 `OpenMathAI` |

### 第 9 步：术语清单 【机构专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| microcredit | 小额信贷 | 与 microfinance 层级区分 |
| grameencredit | 格莱珉信贷 | 机构自命名，照写 |
| solidarity lending | 团结小组联保 | 个人责任为核、小组互助为形 |
| Sixteen Decisions | 十六项决定 | 2023 年更新为十八项 |
| statutory public authority | 法定公共机构 | 勿译成「国企」 |
| Village Phone | 村庄电话计划 | 2004 Petersburg Prize |
| Struggling members program | 乞丐（挣扎成员）计划 | 2003 年启动 |
| repayment rate | 贷款回收率 | 自报口径与质疑并陈 |
| ordinance | 政府法令 | 1983 年建行依据 |
| Mosammat Taslima Begum | 塔斯利玛·贝古姆 | 2006 代表领奖人，拼写照原文 |

---

## 四、背景音乐选择 ✅ 【机构专属，manifest 预分配勿改】

- **选定曲目**: **Through the Darkness** — Audiomachine
- **风格**: 戏剧性 / 从黑暗走向光明 / 史诗
- **匹配理由**:
  - 「从黑暗走向光明」精准呼应 1974 大饥荒的起点到 2006 诺奖的叙事弧线
  - 「戏剧性」匹配三度被驳回的住房贷款、2011 免职风波等冲突节点
  - 史诗底色承载「950 万借款人」的规模感，而不掩盖个体村妇的故事
- **备选**（未采用，仅记录）: Nostalgy（已配 Yunus 本人篇）、Last Hope（留待 IPCC 篇）
- **本地路径**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`
- **时长处理**: 曲目时长 > 13 页 × 7 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Grameen_Bank/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 获奖理由中译照抄来源 |
| `peace/PROMPTS_WORKFLOW.md` + `peace/PROMPTS_WORKFLOW_21ST.md` | 工作流与红线（第 2 节机构规则） |
| `MySQL/data/Grameen_Bank.yaml` | 入库 yaml（与本文件第 4/4.5 步同步） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
