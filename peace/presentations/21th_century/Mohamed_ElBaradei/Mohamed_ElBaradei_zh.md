# OpenPeace 立传提示词（模板实例：Mohamed ElBaradei 穆罕默德·巴拉迪）

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与 OpenPeace 20 世纪 104 位得主批次的实战经验。
- **本实例**：Mohamed Mostafa ElBaradei（穆罕默德·巴拉迪）—— 埃及法学家、外交官，国际原子能机构第四任总干事，2005 年诺贝尔和平奖得主（与 IAEA 共享）。
- **设计哲学**：外交官立传必须有「身份信息页」（Identity / Bio 速览页），并强调「事业领域」的结构化表达——核查外交（verification diplomacy）是贯穿其生涯的主线，构成全篇骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Mohamed Mostafa ElBaradei（1942-06-17 ~ 在世，生于开罗，时为埃及王国）
- **气质关键词**：**核查外交的践行者、多边核不扩散的守门人、埃及变革的参与 commentator 之外的客观记录者** —— 2005 年诺贝尔和平奖获奖理由：
  > "for their efforts to prevent nuclear energy from being used for military purposes and to ensure that nuclear energy for peaceful purposes is used in the safest possible way"（表彰他们为防止核能被用于军事目的、并确保和平利用核能以最安全的方式进行所做的努力）
- **官方获奖理由中译**（照抄名录 `OpenPeace_21st_Century_Nobel_Laureates.md`，禁止改写）：表彰他们为防止核能被用于军事目的、并确保和平利用核能以最安全的方式进行所做的努力。
- **设计母题**：**天平与放大镜（scale & lens）**——法律人的天平 + 核查员的放大镜，象征「以法律与证据而非武力解决争端」的职业底色；背景沿用柔和气泡母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Mohamed_ElBaradei/page.md`（Wikipedia 全文 + frontmatter，事实基准以此为准）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1942-06-17 生于开罗（Giza Governorate / Greater Cairo，时为埃及王国）；在世，卒日留白。
- **家庭**：父 Mostafa ElBaradei 为律师、曾任埃及律师公会（Bar Association）主席，支持新闻自由与司法独立；ElBaradei 为五个孩子之一；妻 Aida El Kashef（前幼儿教育教师），育有二子（不具名，不入库）。
- **教育**：Cairo University 法学学士（1962）→ New York University School of Law LLM（1971）→ JSD 国际法（1974），博士论文《The right of passage through straits in time of peace》；infobox 另列 Graduate Institute of International and Development Studies。
- **语言**：阿拉伯语母语，流利英语、法语，懂基本德语（维也纳语境）。
- **任职机构（含年份）**：
  - 1964 入埃及外交部，任职驻联合国常驻代表团（纽约、日内瓦），主管政治、法律与军控事务
  - 1974–1978 外交部长特别助理
  - 1980 UNITAR 国际法项目高级研究员
  - 1981–1987 NYU 法学院国际法兼职教授
  - 1984 入 IAEA 秘书处：法律顾问（1984–1993）、对外关系助理总干事（1993–1997）
  - 1997-12-01 ~ 2009-11-30 IAEA 第四任总干事（三任期，2001、2005 两度连任；2005-06-13 理事会一致通过第三任期，此前美国反对、6-09 放弃）
  - 2013-07-14 ~ 2013-08-14 埃及临时副总统（主管国际关系）
- **关键荣誉**：Nobel Peace Prize 2005；Indira Gandhi Prize 2008；Four Freedoms Award – Freedom Medal 2006；德国联邦十字大十字勋章（2010，Grand Cross with Star and Sash）；尼罗河勋章大绶带（Grand Cordon of the Order of the Nile，埃及最高文职勋章）；奥地利共和国功绩荣誉装饰（2009）；Delta Prize for Global Understanding 2009 等；另获十余所大学荣誉博士（Trinity College Dublin / NYU / Tsinghua / Cairo 等）。
- **核心事业清单（6 条）**：
  1. IAEA 强化保障监督体系：整合综合保障监督（integrated safeguards）与 Model Additional Protocol（1997 通过），至 2009-11 已有 93 国生效
  2. 伊拉克核查（2002–2003）：与 Hans Blix 共同领导联合国核查团队，2003-03 向安理会指出尼日尔铀采购文件不实
  3. 核安全计划：2001 九一一事件后设立核安全计划与 Nuclear Security Fund
  4. PACT 癌症治疗行动计划（2004 发起）：用 IAEA 2005 诺奖份额训练发展中国家科学家以核技术抗癌与抗营养不良
  5. 核燃料循环多边管控主张（2003 Economist 撰文提出限制武器级材料加工于多边管控设施）
  6. 埃及公共事务：National Association for Change（2010-02 宣布成立）→ 2011 革命期间回国 → Constitution Party（2012-04-28 创立）→ 临时副总统（2013-07）→ Rabaa 事件后辞职（2013-08-14）
- **著述**：《The Age of Deception: Nuclear Diplomacy in Treacherous Times》（2011，译成波兰/德/荷/阿拉伯语）；《The International Law of Nuclear Energy: Basic Documents》（1993，合编）；《Atoms for Peace: A Pictorial History of the IAEA, 1957-2007》（2007）。
- **关键时间线（20 节点）**：
  1. 1942-06-17 生于开罗（时为埃及王国），在吉萨长大
  2. 1962 Cairo University 法学学士毕业
  3. 1964 入外交部，派驻纽约/日内瓦联合国使团
  4. 1971 NYU 法学院 LLM
  5. 1974 NYU 法学院 JSD（国际法），论文论和平时期海峡通过权
  6. 1974–1978 埃及外长特别助理
  7. 1980 UNITAR 国际法项目高级研究员
  8. 1981–1987 NYU 法学院国际法兼职教授
  9. 1984 入 IAEA 秘书处任法律顾问（至 1993）
  10. 1993–1997 任 IAEA 对外关系助理总干事
  11. 1997-12-01 就任 IAEA 第四任总干事（继 Hans Blix）
  12. 2001 连任第二任期；九一一后设核安全计划与 Nuclear Security Fund
  13. 2002–2003 与 Blix 共同领导伊拉克核查；2003-03-07 向安理会判定尼日尔文件不实
  14. 2004 发起 PACT 癌症治疗行动计划
  15. 2005-06-13 美国反对下仍获理事会一致连任第三任期
  16. 2005-10-07 与 IAEA 共获诺贝尔和平奖（12-10 奥斯陆领奖并发表演讲）
  17. 2005 之后：个人奖金全数捐建开罗孤儿院；IAEA 份额用于培训发展中国家科学家
  18. 2007 与伊朗达成秘密核协议，美英法德四国正式抗议（客观记录）
  19. 2009-11-30 卸任总干事；继任者 Yukiya Amano（2009-07-03 当选）
  20. 2010–2013 回国从事政治：2010-02 National Association for Change → 2011-01-27 回国 → 2012-04-28 创 Constitution Party → 2013-07-14 就任副总统 → 2013-08-14 辞职后返维也纳

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Mohamed_ElBaradei/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 OpenPeace 已完成篇目 Makefile，设置 `MAIN=Mohamed_ElBaradei_zh`、`VIDEO_NAME=Mohamed_ElBaradei_zh`

### 第 3 步：收集图片 【人物专属】

- page.md 内嵌图可用：ElBaradei 2005 官方照（infobox）、ElBaredei during Friday of Anger（2011）、Indira Gandhi Prize 颁奖照（2008）等
- 优先 2005 年前后的外交正装照作封面肖像；图源 404 则装饰圆占位

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international law | 国际法 | JSD 专业背景，UNITAR/NYU 执教 | 教育与早年页 |
| 1 | nuclear non-proliferation | 核不扩散 | IAEA 总干事任内主线 | 核查外交页 |
| 2 | arms control verification | 军备控制核查 | 保障监督与 Additional Protocol | 保障监督页 |
| 3 | diplomacy | 外交 | 1964 起外交部与驻 UN 使团 | 早年页 |
| 4 | human rights advocacy | 人权倡导 | 回国后的变革参与与辞职立场 | 埃及岁月页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | International Atomic Energy Agency | 无向 | 2005 诺贝尔和平奖共同得主（本人与其执掌的 IAEA） |
| colleague | International Atomic Energy Agency | 无向 | 第四任总干事（1997–2009） |
| colleague | Hans Blix | 无向 | IAEA 前任总干事，2002–2003 伊拉克核查搭档 |
| colleague | Yukiya Amano | 无向 | IAEA 继任总干事（2009 当选） |
| spouse | Aida El Kashef | 无向 | 妻子，前幼儿教育教师 |
| parent-child | Mostafa ElBaradei | 无向 | 父亲，律师、埃及律师公会主席 |

- **不 入 库（仅叙述）**：两名子女（不具名）；Kofi Annan（祝贺事件）；Colin Powell/Bolton/Rice（美国官方对手方，属事件非关系）；Laban Coblentz（撰稿人）；Soros（机构资助背景叙述）。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：克制、法律理性、外交灰调中的暖意
- **配色**：主色 `#17435B`（外交蓝，沉稳与核查者的冷静，manifest 预分配勿改）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeLaw` 国际法 — 靛蓝 `#4C5FD5`
  - `badgeVerify` 核查监督 — 青绿 `#0E7C7B`
  - `badgeNobel` 诺贝尔 — 香槟金 `#C9A227`（强调用）
  - `badgeEgypt` 埃及岁月 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡 + 天平/放大镜几何线条（克制化）

### 第 6 步：规划幻灯片序列 【人物专属，14 页 + 项目首页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 穆罕默德·巴拉迪 / Mohamed ElBaradei 1942– + 四色 badge + 右上头像
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/教育/师承线/任职/荣誉/核心领域）
03  事业概览 — 外交官 / 法学家 / 核查外交 / 埃及变革参与
04  早年与法学教育 — 开罗 1962 → NYU LLM 1971 → JSD 1974
05  外交起步（1964–1984）— 驻 UN 使团、外长特别助理、UNITAR、NYU 兼职教授
06  IAEA 内部岁月（1984–1997）— 法律顾问 → 助理总干事
07  总干事任期（1997–2009）— 三任期，2005 美国反对下连任
08  强化保障监督 — integrated safeguards 与 Additional Protocol（93 国生效）
09  伊拉克核查（2002–2003）— 尼日尔文件不实判定（客观记录）
10  核安全与 PACT — Nuclear Security Fund（2001）、PACT（2004）、诺奖份额用途
11  2005 诺贝尔和平奖 — 官方理由 + 奥斯陆演讲要点 + 捐赠孤儿院
12  埃及岁月（2010–2013）— NAC → 2011 革命 → 宪政党 → 副总统 → 辞职（全部客观）
13  荣誉与著述 — Indira Gandhi Prize 2008、Order of the Nile、《The Age of Deception》
14  结尾
```

### 第 7 步：版式要点 【模板通用】

- 身份信息页参照个人篇 `\profileslide` 实现模式：左头像右信息网格（生卒/本名/国籍/教育/任职/荣誉/核心领域），事实取自 infobox，不得杜撰。
- 时间线页 20 节点拆两页（1984 前后分界），`\foreach` 分隔符必须 ASCII 逗号。
- 荣誉页条目多（20+ 勋章），只取 6–8 条代表项，其余「等」收束；`itemsep -2.5pt` + `arraystretch 0.62` 防溢出。
- 引文框仅用 page.md 明载英文原文（2003 Cairo Times 访谈、2004 NYT 投稿、辞职信节选），配中文翻译；无原文者禁用引号。
- 编译硬指标：0 error、vbox ≤10pt、hbox ≤50pt，每写一页即 make 并 `pdftoppm` 目检。

### 第 8 步：史实审查 + 人物专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 在世留白 | 无卒日，封面/概览页/结尾三处统一「1942–」留白 |
| 学位口径 | LLM 1971 与 JSD 1974 均出自 NYU School of Law；本科 Cairo 1962；勿写成「开罗大学博士」 |
| IAEA 起止 | 1997-12-01 ~ 2009-11-30（三任期）；「连任三次」表述勿写成「任期十二年连续无间断当选」——2005 第三任期曾遭美国公开反对 |
| 尼日尔文件 | 2003-03 向安理会指出文件不实是 page.md 明载事实；「伊拉克战争立场」相关叙述一律客观，不加评价 |
| 诺奖共享结构 | 理由句主语是 "their"，本人篇与 IAEA 机构篇共用同一 EN+中译，勿改写成个人理由 |
| 第四位埃及诺奖得主 | 顺序 Sadat（1978 和平）→ Mahfouz（1988 文学）→ Zewail（1999 化学）→ ElBaradei（2005），page.md 明载 |
| 捐赠口径 | 个人奖金捐开罗孤儿院；IAEA 份额用于训练发展中国家科学家（抗癌/抗营养不良），两者勿混 |
| 2013 辞职 | 2013-08-14 Rabaa 镇压（至少 525 死，page.md 明载数字）后辞副总统、返维也纳；按事实记录，不作政治评价 |
| 政治敏感 | 伊朗秘密协议（2007）、加沙言论（2010）、对美英法的批评、2011/2013 埃及政局：全部按 page.md 客观记录，禁评价性语句；引语只取明载英文原文 |
| 同名区分 | 无同名干扰；阿拉伯语全名 محمد مصطفى البرادعي 仅首页出现一次 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Director General | 总干事 | IAEA 职衔，勿译「署长」 |
| safeguards | 保障监督 | 与 nuclear security（核安保）区分 |
| Additional Protocol | 附加议定书 | 1997 Model 版本语境 |
| non-proliferation | 核不扩散 | NPT 框架 |
| JSD | 法律科学博士 | 勿与 PhD/LLD 混 |
| verification | 核查 | 军控语境译「核查」 |
| PACT | 癌症治疗行动计划 | Programme of Action for Cancer Therapy |
| Rabaa | 拉巴阿（广场/事件名） | 2013-08-14，仅事实记录 |
| National Association for Change | 变革全国协会 | 2010-02 成立 |
| The Age of Deception | 《欺骗的年代》 | 2011 回忆录，书名照原文 |

---

## 四、背景音乐选择 ✅ 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Lonesome** — AShamaluevMusic（inspiring-electronic 合集）
- **风格**: 沉郁 / 情感叙事 / 纪录片
- **匹配理由**:
  - 「沉郁」匹配其职业底色——在美苏对立、核查争议与华盛顿批评的夹缝中独自坚持核查路线的孤独感
  - 「情感叙事」匹配晚年从国际舞台转向故国变革又再度离场的复杂收束
  - 纪录片气质与全篇「证据先于立场」的克制叙事一致
- **备选**（未采用，仅记录）: Timeless（偏制度史诗）、The Flow of Time（时间感强但已在多曲轮转中占用）
- **本地路径**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`
- **时长处理**: 曲目时长 > 14 页 × 7 秒，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Mohamed_ElBaradei/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 获奖理由中译照抄来源 |
| `peace/PROMPTS_WORKFLOW.md` + `peace/PROMPTS_WORKFLOW_21ST.md` | 工作流与政治敏感红线 |
| `MySQL/data/Mohamed_ElBaradei.yaml` | 入库 yaml（与本文件第 4/4.5 步同步） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
