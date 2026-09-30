# 和平奖得主立传提示词（OpenPeace 21 世纪批次：Ellen Johnson Sirleaf）

> 本文件是 OpenPeace 项目 21 世纪诺贝尔和平奖批次的人物专属立传提示词。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（OpenMathAI 共享仓库 `peace/` 侧）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词结构）与和平奖侧 20 世纪批次实战经验。
- **本实例**：Ellen Eugenia Johnson Sirleaf（埃伦·约翰逊·瑟利夫，2011 诺贝尔和平奖，与 Leymah Gbowee、Tawakkol Karman 共享）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Ellen Eugenia Johnson Sirleaf（1938-10-29 生于蒙罗维亚，在世）
- **官方获奖理由（照抄，禁止改写）**：
  > "for their non-violent struggle for the safety of women and for women's rights to full participation in peace-building work."
  > 表彰她们以非暴力方式维护妇女安全、争取妇女充分参与和平建设工作的权利
  - ★ 主语是 **"their"**：2011 年三人共享（Sirleaf / Leymah Gbowee / Tawakkol Karman），理由为同一句；2011-12-10 三人同台领奖（page.md 领奖照片图注明载）。
- **气质关键词**：**非洲首位民选女总统、"铁娘子"、战后重建的经济学家**
- **设计母题**：**废墟上的重建（rebuilding）**。两场内战后的利比里亚——用「脚手架上的新墙 + 女性侧影」构图，呼应 "peace-building work" 的原词意象。
- **本地数据源**：`peace/presentations/pages/21th_century/Ellen_Johnson_Sirleaf/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 和平奖侧成品参照：`peace/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（第一轮已核对，来源 = 本地 page.md） 【人物专属】

- 生卒：1938-10-29 生于蒙罗维亚（在世，无卒日）；父 Jahmale Carney Johnson（戈拉族，首位当选国会议员的土著利比里亚人，因忠于总统 Hilary R. W. Johnson 改姓 Johnson）；母出身克鲁族与德裔混血家庭，外祖母 Juah Sarwee，由 Americo-Liberian 名门 Cecilia Dunbar 抚养
- 国籍：利比里亚
- 教育：College of West Africa 预科（1948–1955）；17 岁成婚后 1961 随夫赴美；Madison Business College 会计副学士（AA）；University of Colorado Boulder 经济学 BA（1970）；Harvard Kennedy School 经济学与公共政策，MPA（1969–1971）
- 早年职业：汽修店记账员→财政部任职→助理财政部长（1972–1973，Tolbert 政府；因政府开支分歧辞职前曾以"炸弹式"演讲批评企业囤积利润海外输送）
- 财政部长（1979–1980-04-12）：Tolbert 政府内阁成员
- 1980 政变与流亡：Samuel Doe 1980-04-12 军事政变处决 Tolbert 内阁成员；Sirleaf 短暂出任利比里亚发展投资银行行长后，1980-11 因公开批评 Doe 与人民救赎委员会而流亡
- 流亡银行家岁月：World Bank（华盛顿）；1981–1985 Citibank 非洲区域办公室副总裁（内罗毕）；Equator Bank（汇丰子公司）
- 1985 年回国参选：被软禁、以煽动罪被判十年（国际呼吁下 9 月获特赦）；11-13 再度被捕监禁，1986-07 获释后流亡美国；参选蒙察拉多县参议员获胜但拒绝就任以抗议选举舞弊
- 联合国开发计划署（1992–1997）：非洲区域局主任（助理秘书长级）；1999 年被非洲统一组织指定为卢旺达种族灭绝调查七人国际知名人士之一；Inter-Congolese Dialogue 五位委员会主席之一；UNIFEM 选定的两名国际专家之一；OSIWA 首任主席；GIMPA 治理访问教授
- 1997 年大选：团结党候选人，得票约 10% 居第二（Charles Taylor 75%）；随后流亡阿比让
- 2005 年大选：首轮居 George Weah 之后，决选 59% vs 40% 胜出；2005-11-23 确认当选——**非洲首位民选女性国家元首**；2006-01-16 就任第 24 任利比里亚总统
- 总统任期（2006–2018，2011 连任）：债务减免主线（2006 年国债约 49 亿美元→2010-06 完成 HIPC 完成点、巴黎俱乐部注销 12.6 亿+双边 1.07 亿——发展中国家最大折扣率回购）；2006 真相与和解委员会（TRC）运作，2009-06 报告建议其因内战初期资助 Taylor 而禁任公职 30 年，2011-01 最高法院 Williams v. Tah 裁定该建议违宪；2009-07-26 其为早年支持 Taylor 公开道歉；2010-10-04 签署西非首个信息自由法；2014–2015 埃博拉疫情应对；2016-06 当选西非国家经济共同体（ECOWAS）主席（首位女性）
- 诺贝尔和平奖：2011-10-13 前后（大选前四天）公布获奖，反对党 Winston Tubman 称 "undeserved"、"a political interference"——Sirleaf 称获奖时机纯属巧合并避免在竞选最后几天提及该奖（**两说并陈**）；2011-12-10 与 Gbowee、Karman 同台领奖
- 卸任后：2017 跨党派支持 George Weah；2018-01-13 被团结党开除党籍；2018 创立 Ellen Johnson Sirleaf Presidential Center for Women and Development；2019 任世卫组织卫生人力亲善大使；2020 与 Helen Clark 共同主持世卫独立疫情防范与应对小组（IPPR）；2017 Ibrahim Prize（非洲领导力成就奖，2018 颁发）
- 关键荣誉：诺贝尔和平奖 2011；Presidential Medal of Freedom 2007（小布什颁）；Indira Gandhi Prize 2012；Ibrahim Prize 2017（2018 授）；Roosevelt Institute 言论自由奖 1988；多所大学荣誉博士（Harvard 2011/Yale 2010/Brown 等）
- 家庭：1956（17 岁）与 James Sirleaf 成婚，育四子，1961 因家暴离异；子 Robert Sirleaf（国家石油公司负责人）、Charles Sirleaf（央行高级职位，2024-06 去世）、继子 Fombah Sirleaf（国家安全署负责人）；子 James Sirleaf 2021-12 去世（**与前夫同名，勿混淆**）；侄女 Retta（美国演员）
- 关键时间线（15–20 节点）：1938 出生 → 1948–55 College of West Africa → 1956 成婚 → 1961 赴美 → 会计 AA → 1970 CU Boulder BA → 1971 Harvard MPA → 1972 助理财政部长 → 1979 财政部长 → 1980 政变流亡 → 1981–85 Citibank → 1985 回国参选与监禁 → 1986 再流亡 → 1992 UNDP → 1997 大选败选 → 2005 当选 → 2006 就任 → 2007 总统自由勋章 → 2010 债务完成点 → 2011 诺奖+连任 → 2016 ECOWAS 主席 → 2018 卸任+总统中心创立

### 第 4 步：事业领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | women in peacebuilding | 妇女与和平建设 | 官方获奖理由核心词 | 核心页 |
| 1 | women's rights | 妇女权利 | 内阁性别部长设置、妇女参政推动 | 权利页 |
| 2 | democratic governance | 民主治理 | 选举、反贪、信息自由法 | 治理页 |
| 3 | economic development | 经济发展 | 战后重建、外资回归 | 经济页 |
| 4 | public finance | 公共财政 | 财政部长出身、债务减免主线 | 财政页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | James Sirleaf | 无向 | 1956 成婚（时年 17 岁），1961 离异 |
| co-honored | Leymah Gbowee | 无向 | 2011 诺贝尔和平奖共同得主（共享理由句） |
| co-honored | Tawakkol Karman | 无向 | 2011 诺贝尔和平奖共同得主（共享理由句） |
| parent-child | Robert Sirleaf | 无向 | 子，曾任国家石油公司负责人 |
| parent-child | Charles Sirleaf | 无向 | 子，央行高级职位（2024-06 去世） |
| parent-child | Fombah Sirleaf | 无向 | 继子，国家安全署负责人 |
| colleague | Joseph Boakai | 无向 | 两届副总统与竞选搭档 |
| controversy | Charles Taylor | 无向 | 1989 年内战初期曾资助并共创 NPFL，后决裂反对，2009 公开道歉 |

- ★ 与 Gbowee/Karman 的 co-honored 为**两两双向**：batch-04（Gbowee/Karman 侧）也会写，靠 name_en 规范名幂等去重（INSERT IGNORE），不会分裂。

### 第 5 步：设计配色方案 【manifest 预分配，勿改】

- **主色**：`#1B4D6B`（利比里亚海蓝——战后重建的沉稳）
- **诺奖香槟金**：`C9A227`
- badge 四分类色（建议）：妇女与和平建设 深绛 `#7E1E23`；妇女权利 深青 `#0B5351`；民主治理 靛蓝 `#4C5FD5`；公共财政 琥珀 `#E07B30`
- **背景母题**：脚手架新墙 + 女性侧影（重建母题）

### 第 6 步：规划幻灯片序列 【人物专属，可微调；共 15 页 = 共享封面 + 14 帧】

```
00  OpenPeace 项目首页（\input cover 共享页）
01  封面 — 非洲首位民选女总统 / Ellen Johnson Sirleaf b. 1938 + badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心事业概览 — 妇女与和平建设 / 妇女权利 / 民主治理 / 公共财政
04  早年与家庭 (1938–1961) — 蒙罗维亚、17 岁成婚、赴美求学
05  留美求学 (1961–1971) — 会计 AA、CU Boulder 经济学、Harvard MPA
06  从财政部到政变流亡 (1972–1986) — 助理部长/部长、Doe 政变、监禁与流亡
07  流亡银行家岁月 (1980–1992) — 世行/Citibank/Equator Bank
08  联合国开发计划署 (1992–1997) — 非洲区域局主任、卢旺达调查七人组
09  1997 与 2005 两次大选 — 败选流亡→决选 59% 当选、非洲首位民选女元首
10  总统任期：债务减免与重建 (2006–2011) — 49 亿债务出清、HIPC、信息自由法
11  诺贝尔和平奖 (2011) — 三人共享、官方理由 EN+中译、大选前四天的争议两说并陈
12  第二任期与卸任 (2012–2018) — 埃博拉应对、ECOWAS 首位女主席、Weah 交接
13  卸任后与荣誉 — 总统中心、IPPR、Ibrahim Prize、总统自由勋章
14  遗产与结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照已有和平奖成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用同项目已立传目录骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Sirleaf 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 共享奖主语 | 2011 理由是 "their"（三人同句）；标题与正文勿写"独得"，三人同台领奖照片图注可注 |
| ★ 大选前获奖争议两说并陈 | 反对党 Tubman 称 "undeserved"/"political interference" vs 本人称巧合并回避提及——**两面并写**，勿单边定性 |
| 同名父子陷阱 | 前夫 James Sirleaf 与四子之一的 James Sirleaf **同名**——yaml 只建前夫一行；子 James（2021-12 去世）不建 stub，行文用"其子 James"并加注 |
| 继子 Fombah | Fombah Sirleaf 是**继子**（stepson）——note 注明，勿写成亲子 |
| 非洲首位口径 | "first elected female head of state in Africa"（2006 就任）为 page.md 明载口径；2016 ECOWAS 主席是"该职位首位女性"，两个"首位"勿混 |
| 债务数字 | 2006 年国债约 49 亿美元；美国减免 3.91 亿（2007）；G-8/IMF 3.245 亿；2010 完成点后巴黎俱乐部 12.6 亿+双边 1.07 亿——勿混 |
| TRC 段落 | 2009 报告 30 年禁任公职建议 + 2011 最高法院违宪裁定 + 2009-07-26 道歉——三者按时间客观并陈，勿遗漏裁定结果 |
| 同名奖章 | 2007 年 Presidential Medal of Freedom（小布什颁）与 Al Gore 2024 年同名奖章——各归各篇 |
| 无载禁写 | page.md 未载的内阁人物细节、2017 年后家族司法案详情（仅一句客观）禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| peace-building | 和平建设 | 官方理由原词，勿改"维和" |
| first elected female head of state in Africa | 非洲首位民选女性国家元首 | 2006 就任口径 |
| Unity Party | 团结党 | 1997–2018 党籍 |
| HIPC initiative | 重债穷国倡议 | 2008 合格、2010 完成点 |
| Truth and Reconciliation Commission (TRC) | 真相与和解委员会 | 2006 运作、2009 报告 |
| ECOWAS | 西非国家经济共同体 | 2016 首位女性主席 |
| UNDP Regional Bureau for Africa | 联合国开发计划署非洲区域局 | 1992–1997 |
| Iron Lady of Africa | 非洲铁娘子 | 国际通行称号（frontmatter nickname） |
| Ibrahim Prize | 易卜拉欣非洲领导力成就奖 | 2017 年度奖项、2018 授予 |
| Ellen Johnson Sirleaf Presidential Center | 瑟利夫总统妇女与发展中心 | 2018 创立 |

---

## 四、背景音乐选择 【manifest 预分配，勿改】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（inspiring-electronic 曲库）
- **风格**: 情感叙事 / 钢琴底色 / 重建感
- **匹配理由**：
  - "Falling Apart（碎裂与重建）" 匹配利比里亚两场内战的崩塌与其当选后的国家重建主线——曲名是起点，曲目走向是重建
  - 情感叙事匹配其个人弧线：17 岁成婚的家暴离异、两度流亡、两度监禁，到 67 岁就职总统
  - 钢琴底色克制，匹配本篇"两说并陈"的客观基调
- **本地路径**: `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Ellen_Johnson_Sirleaf/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
