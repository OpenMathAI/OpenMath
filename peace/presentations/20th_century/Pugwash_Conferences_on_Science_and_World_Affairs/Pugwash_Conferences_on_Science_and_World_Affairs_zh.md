# 和平奖得主立传提示词（OpenPeace 批次 20 · Pugwash Conferences on Science and World Affairs）

> 本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」之一，对象为**组织机构**：
> 帕格沃什科学与世界事务会议（Pugwash Conferences on Science and World Affairs，1995 诺贝尔和平奖共同得主）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **本实例**：Pugwash Conferences on Science and World Affairs（帕格沃什科学与世界事务会议），**组织机构条目**。
- **设计哲学**：组织机构立传与个人立传的核心差异，在于用**「机构概览页」（Organization Overview）替代身份信息页**，且强调「使命领域」的结构化表达——这两点构成机构模板的骨架，务必保留。

---

## 二、背景信息 【机构专属】

- **目标机构**：Pugwash Conferences on Science and World Affairs（1957 年成立至今，国际组织）
- **气质关键词**：**科学家跨国对话的灯塔、核裁军的长期推手、二轨外交的开创范例** —— 1995 诺贝尔和平奖获奖理由：
  > "for their efforts to diminish the part played by nuclear arms in international politics and, in the longer run, to eliminate such arms"
  > （中译照抄名录：表彰他们为削弱核武器在国际政治中的作用、并在长远上消除核武器所做的努力）
- **设计母题**：**圆桌对话（round table）**。Pugwash 的核心运作方式是把敌对阵营的科学家聚在私人场合自由交换意见——「圆桌」隐喻超越阵营的平等对话，是比「天平」「握手」更贴合其视觉语言的概念。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Pugwash_Conferences_on_Science_and_World_Affairs/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（OpenPeace 共享封面由主控统一建，若已有 `peace/presentations/cover/` 则优先用之）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：本批已完成「使命领域 + 社会关系入库」（见第 4 / 4.5 步表格），立传时以库内与 yaml 为准，不要另起炉灶。

### 第 0 步：下载并核对数据页面 【机构专属】

- ✅ 已抓取 Wikipedia 页面到 `peace/presentations/pages/20th_century/Pugwash_Conferences_on_Science_and_World_Affairs/`（page.md / page.html / metadata.json / images.txt 四件套）
- 提取 infobox 与正文，**事实基准如下**（第一轮已核对）：
  - 机构性质：国际组织（international organization），总部设罗马（国际秘书处）、伦敦、日内瓦、华盛顿特区四办公室
  - 成立：1955-07-09《罗素—爱因斯坦宣言》呼吁 → 1957 年 7 月首届会议于加拿大新斯科舍省帕格沃什「思想家小屋」（Thinkers' Lodge）
  - 创始人：Joseph Rotblat 与 Bertrand Russell；出资人兼东道主：实业家 Cyrus Eaton（其故乡即帕格沃什）
  - 首届会议：22 位科学家与会（美 7、苏 3、日 3、英 2、加 2、澳/奥/中/法/波各 1），罗素因健康未能出席
  - 宗旨（明文）：消除一切大规模杀伤性武器（核、化、生）并把战争从国际争端解决手段中剔除；会议原则上非公开举行
  - 组织架构：主席（president）+ 秘书长（secretary-general）+ 理事会（Pugwash Council，五年一任）；现任主席 Hussain al-Shahristani，现任秘书长 Karen Hallberg
  - 秘书长序列：Rotblat 1957–1973 / Feld 1973–1978 / Kaplan 1978–1989 / Calogero 1989–1997 / Rathjens 1997–2002 / Cotta-Ramusino 2002–2024 / Hallberg 2024–
  - 主席序列（1967 年设正式主席职）：Cockcroft 1967（当选十日后去世）/ Florey（旋即去世，改轮值一年）/ Perrin 1968 / Millionshchikov 1969 / Rabinowitch 1970 / Alfvén 1970–1975 / Hodgkin 1976–1988 / Rotblat 1988–1997 / Atiyah 1997–2002 / Swaminathan 2002–2007 / Dhanapala 2007–2017 / Duarte 2017–2024 / al-Shahristani 2024–
  - 制度贡献：为《部分禁止核试验条约》(1963)、《不扩散核武器条约》(1968)、《反弹道导弹条约》(1972)、《生物武器公约》(1972)、《化学武器公约》(1993) 提供背景工作；McNamara 认可代号 PENNSYLVANIA 的后渠道倡议为结束越战谈判铺路；戈尔巴乔夫承认该组织对他的影响
  - 关键荣誉：1995 诺贝尔和平奖（与 Rotblat 共同获得，时值广岛长崎轰炸 50 周年、罗素—爱因斯坦宣言签署 40 周年）
  - 其他：1988 达戈梅斯会议发表《环境退化达戈梅斯宣言》；1965 年会议催生国际科学基金会（IFS）建议；2008 年 Thinkers' Lodge 列为加拿大国家历史遗址；2017 年阿斯塔纳 62 届会议
  - 关键时间线（15–20 节点）：1955 宣言 → 1957 首届会议 → 1963 部分禁试条约 → 1967 设正式主席职 → 1968 NPT → 1972 ABM/BWC → 冷战期间二轨渠道 → 1980 美众院情报委员会报告争议 → 1988 达戈梅斯宣言 → 1995 诺奖 → 1998 Monitor 时代 → 2017 阿斯塔纳 60 周年 → 2024 新届领导层

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下已有 `Pugwash_Conferences_on_Science_and_World_Affairs/`（提示词所在），建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 参照最近一位已完成 OpenPeace 成品的 Makefile（或物理学家侧 Kenneth_G_Wilson/Makefile），设置 `MAIN=Pugwash_Conferences_on_Science_and_World_Affairs_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【机构专属】

- page.md 已有真实图片 URL：Thinkers' Lodge 照片（首届会议会址，维基 Commons，330px 可改 600px）与 Cyrus Eaton 照片、1970 年 Fermilab Pugwash 合影
- 下载到 `images/` 并 `file` 验证格式；404 则改用 Commons `Special:FilePath/<文件名>?width=600`；再失败用装饰图形占位（机构条目可用会址照片当主视觉，无需人物肖像）

### 第 4 步：使命领域梳理（已入库） 【模板通用，机构专属内容】

**Pugwash 的使命领域（按 rank 排序，与 yaml/DB 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear disarmament | 核裁军 | 1995 诺奖核心使命 | 核心页 |
| 1 | arms control | 军备控制 | 五大条约的背景工作 | 制度贡献页 |
| 2 | international security | 国际安全 | 全球安全威胁应对 | 宗旨页 |
| 3 | track ii diplomacy | 二轨外交 | 非官方科学家渠道 | 二轨外交页 |
| 4 | conflict resolution | 冲突解决 | 通过对话与相互理解和平解决争端 | 宗旨页 |

### 第 4.5 步：社会关系（已入库） 【模板通用，机构专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Joseph Rotblat | Rotblat→机构 | 创始人之一；秘书长 1957–1973、主席 1988–1997 |
| founder | Bertrand Russell | Russell→机构 | 创始人之一；罗素—爱因斯坦宣言发起人 |
| founder | Cyrus Eaton | Eaton→机构 | 出资人兼东道主，首届会议在其实业家故乡举办 |
| co-honored | Joseph Rotblat | 无向 | 1995 诺贝尔和平奖共同得主 |
| colleague | John Cockcroft | 无向 | 1967 年首位正式主席，当选十日后去世 |
| colleague | Dorothy Crowfoot Hodgkin | 无向 | 主席 1976–1988，1964 化学奖得主 |

> 同一人（Rotblat）可同时有 founder 与 co-honored 两条关系，类型不同不冲突。

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：深邃、理性、跨国对话的克制感
- **配色**：主色深紫罗兰 `#46356B`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeDisarm` 核裁军 — 靛蓝 `#4C5FD5`
  - `badgeTreaty` 条约进程 — 青绿 `#0E7C7B`
  - `badgeTrackII` 二轨外交 — 琥珀 `#E07B30`
  - `badgeScience` 科学家网络 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「圆桌对话」母题——不同大小的圆象征不同国籍与阵营的科学家围坐一桌

### 第 6 步：规划幻灯片序列 【机构专属，可微调】

```
00  OpenPeace 项目首页（\input 共享封面）
01  封面 — 科学家跨国对话的灯塔 / Pugwash 1957– + 四色 badge + 会址图 + 「国际组织」行
02  机构概览页（★ 必做，替代身份信息页）— 左会址照 + 右信息网格（成立、创始人、宗旨、
    总部四办公室、现任领导、会员规模 3500+ Pugwashites、核心使命）
03  使命概览 — 核裁军 / 军备控制 / 国际安全 / 二轨外交 / 冲突解决
04  起源：罗素—爱因斯坦宣言 (1955) — 宣言内容、Eaton 出资、印度会议流产、摩纳哥被拒
05  首届会议：思想家小屋 (1957-07) — 22 位科学家、六国分布、罗素缺席、非公开运作模式
06  组织架构 — 主席/秘书长/理事会、四办公室、50 个国家小组、ISYP 学生网络
07  冷战中的二轨渠道 — 柏林危机、古巴导弹危机、越南战争期间的沟通桥梁
08  条约进程的幕后推手 — 1963/1968/1972/1972/1993 五大条约背景工作
09  PENNSYLVANIA 渠道与戈尔巴乔夫 — 越战谈判铺路、苏联领导人的承认
10  争议与回应 — 冷战「苏联前台」指控、1980 情报委员会报告、Rotblat 1998 回应（客观并列）
11  领导人谱系 — 主席 14 人与秘书长 7 人的传承（选代表人物）
12  1995 诺贝尔和平奖 — 广岛长崎 50 周年、宣言 40 周年、"Remember your humanity"
13  延伸遗产 — 达戈梅斯宣言、IFS、Thinkers' Lodge 国家历史遗址、阿斯塔纳会议
14  遗产：从帕格沃什到今日核裁军议程
15  结尾
```

### 第 7–8 步：版式要点 + 机构专属陷阱表 【模板通用 + 机构专属】

**Pugwash 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 创始人归属 | page.md 明文「founded in 1957 by Joseph Rotblat and Bertrand Russell」——勿写成 Eaton 创立（他是出资人/东道主）；也勿漏掉 Russell 因健康缺席首届 |
| 勿把领导人写成创始人 | Cockcroft 是 1967 首位**正式**主席（此前 Russell 为天然领袖），Hodgkin/Alfvén 均为主席而非创始人 |
| 诺奖「共同」 | 1995 是 Rotblat 与 Pugwash **共同**获奖，理由句用 "for their efforts..."（their=两者）；罗素未获奖系诺奖不追授，notes 明载 |
| 首届会议国别数 | 22 位科学家：美 7 苏 3 日 3 英 2 加 2 澳奥中法波各 1——合计恰 22，勿数错；另有 Eaton、Burhop 等非与会出席者 |
| 条约措辞 | Pugwash 的角色是「提供背景工作」（provided background work），勿写成「主导谈判」或「起草」 |
| 冷战争议 | 「苏联前台会议」是**被指控**（claimed），且 Rotblat 1998 讲话有反驳——只客观并列双方说法，不加评价 |
| PENNSYLVANIA | 是 Robert McNamara 认可的后渠道倡议，助力**结束越战谈判**，勿写成官方和谈 |
| 姓名全称 | Bertrand Russell 曾获 1950 文学奖；John Cockcroft 为 1951 物理奖；Dorothy Crowfoot Hodgkin 为 1964 化学奖——引述时用全名勿混淆 |
| ISYP | International Student/Young Pugwash 与国际 Pugwash 合作但独立，勿写成下属机构 |
| 政治敏感 | 涉及冷战阵营、中东/朝核等当代议题只作 page.md 明载的客观事实记录，不加任何评价性语句 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Russell–Einstein Manifesto | 罗素—爱因斯坦宣言 | 1955-07-09 发布，破折号连接符 |
| Track II diplomacy | 二轨外交 | 非官方渠道，勿译「第二轨道」 |
| weapons of mass destruction | 大规模杀伤性武器 | 核生化统称 |
| Thinkers' Lodge | 思想家小屋 | 首届会议会址，撇号位置 |
| Pugwash Council | 帕格沃什理事会 | 五年一任，勿译委员会 |
| secretary-general | 秘书长 | 与 president 主席分立 |
| Pugwashite | 帕格沃什与会者 | 3500+，非正式会员称谓 |
| Partial Test Ban Treaty | 部分禁止核试验条约 | 1963，勿漏「部分」 |
| Dagomys Declaration | 达戈梅斯宣言 | 1988，环境议题 |
| front conference | 前台会议/幌子组织 | 争议指控词，须带 claimed |
| National Historic Site of Canada | 加拿大国家历史遗址 | 2008，会址荣誉 |
| quinquennial conference | 五年一度大会 | 1967 设主席职的场合 |

---

## 四、背景音乐选择 【机构专属，manifest 预分配勿改】

- **选定曲目**: **Mirage** — Notan Nigres
- **风格**: 迷离 / 纪录片 / 长程叙事
- **匹配理由**: 「海市蜃楼」般若隐若现的核战争阴影与二轨外交的幕后感；纪录片气质匹配「科学家在私人场合悄然改写历史」的叙事；长程感匹配 1957 至今近七十年的持续运动
- **本地路径**: `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`
- **时长**: 与 15–16 页成片用 ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Pugwash_Conferences_on_Science_and_World_Affairs/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/Pugwash_Conferences_on_Science_and_World_Affairs.yaml` | 领域/关系入库母本 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
