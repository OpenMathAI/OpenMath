# OpenPeace 立传提示词：Maria Ressa（玛丽亚·雷萨，2021 诺贝尔和平奖）

> 本文件是 OpenPeace 21 世纪批次的人物专属立传提示词，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：Maria Angelita Ressa（玛丽亚·雷萨），2021 年诺贝尔和平奖得主（与 Dmitry Muratov 共享），菲律宾/美国双籍记者、Rappler 联合创始人兼 CEO；1935 年以来首批获诺贝尔和平奖的记者之一。
- **设计哲学**：以**「真相的防线」**为叙事主线——从 CNN 亚洲调查记者到 Rappler 数字新闻创业，再到法庭上的新闻自由之辩；法律战线（网络诽谤案时间线）是本篇的独有结构。

---

## 二、背景信息 【人物专属】

- **目标人物**：Maria Angelita Ressa（1963-10-02 生于菲律宾马尼拉，在世）
- **气质关键词**：**无畏的调查者、数字新闻创业者、法庭上的新闻自由捍卫者** —— 2021 年诺贝尔和平奖获奖理由（与 Muratov 共享）：
  > "for their efforts to safeguard freedom of expression, which is a precondition for democracy and lasting peace."（表彰他们为捍卫言论自由所做的努力——言论自由是民主与持久和平的前提条件）
- **设计母题**：**不灭的屏幕光（the unyielding screen）**——新闻编辑室的屏幕与法庭的天平叠影；视觉可用手机屏幕光束穿透阴暗的意象。
- **本地数据源**：`peace/presentations/pages/21th_century/Maria_Ressa/page.md`
- **参考模板**： physicist 侧标杆 `Kenneth_G_Wilson_zh.tex` 骨架。

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 出生：1963-10-02 马尼拉；本名 Maria Angelita Delfin Aycardo；1 岁丧父（Manuel Phil Aycardo III）；10 岁随母与继父 Peter Ames Ressa 移居新泽西 Toms River 并改姓；公立 Toms River High School North（三次班长；2021 学校礼堂以其命名）
- 教育：Princeton 大学英语文学学士 *cum laude*（1986，辅修戏剧与舞蹈；毕业论文 "Sagittarius" 为隐喻菲律宾政治的寓言剧）；Fulbright 奖学金赴菲律宾大学迪利曼分校研究政治戏剧并在该校任教新闻课程
- 职业轨迹：首份工作 PTV 4 → 1987 共同创办独立制作公司 Probe → CNN 马尼拉分社长（至 1995）→ CNN 雅加达分社长（1995–2005）→ 亚洲首席调查记者近 20 年，专攻恐怖主义网络调查 → 新加坡南洋理工 S. Rajaratnam 国际研究学院 ICPVTR 驻作作家 → 2004 起执掌 ABS-CBN 新闻部（同时为 CNN 与《华尔街日报》撰稿；2010 因批评阿基诺三世人质危机报道离职之议）→ 2011-08 MovePH Facebook 页 → 2012-01-01 Rappler 正式上线（另三位女性共同创始人+12 人小团队）→ 执行编辑兼 CEO
- 学术任职：Princeton 东南亚政治与新闻课程、UP 迪利曼广播新闻课程；MIT 数字经济计划研究员；哈佛肯尼迪学院 2021 Joan Shorenstein Fellow + Hauser Leader；2023 起哥伦比亚大学全球政治研究所杰出研究员（主导 AI 与民主项目）、2024-07 起 SIPA 实务教授；2023 加入 The Intercept 董事会
- 法律战线（Rappler 案件谱系，page.md 明载）：
  - 2018-01-22 NBI 就网络诽谤指控接受传唤（Wilfredo Keng 2017-10 起诉；2012 年报道 2014 年更正错字被认定"重新发布"）
  - 2018-01 SEC 撤销 Rappler 注册（2017-07 杜特尔特国情咨文指控 Rappler 美资违宪之后）；上诉法院裁定发回
  - 2018-11 逃税指控（涉 2015 Omidyar Network 投资；BIR 认定欠税 1.33 亿比索；本人否认）
  - 2019-02-13 逮捕（保释金不足一度拘于 NBI；次日 10 万比索保释获释）；2019-07 开庭
  - 2020-06-15 马尼拉 RTC 裁定网络诽谤罪成立（六个月至六年刑期+40 万比索罚款；上诉中）
  - 2023-01-15 十二位诺奖得主（含 Muratov 与全部 2022 得主）致函马科斯总统
  - 2023-01/09 税案 4+1 项全部无罪；2025-06-13 反傀儡法（外资持股限制）Pasig 法院判 Ressa 及五位 Rappler 高管无罪
  - 网络诽谤定罪与 SEC 关停令截至 2023-09 仍在上诉
- 2021 诺贝尔和平奖：挪威工党领袖 Jonas Gahr Støre 提名；2021-10-08 宣布与 Dmitry Muratov 共享；两人是 1935 年以来首批获和平奖的记者
- 荣誉：Time 2018 年度人物（"The Guardians"）；Time 100（2019）；UNESCO/Guillermo Cano 世界新闻自由奖（2021-04）；世界报业协会金笔奖（2018-06）；CPJ Gwen Ifill 新闻自由奖（2018-11）；Knight 国际新闻奖（2018-05）；哥伦比亚新闻学院奖（2019-05，最高荣誉）；BBC 100 Women（2019）；普林斯顿 Woodrow Wilson 奖（2022-02）；哈佛 2024 毕业典礼演讲嘉宾；戛纳 LionHeart（2024）；密苏里荣誉奖章（2025）
- 著作：*Seeds of Terror*（2003）、*From Bin Laden to Facebook*（2013）、*How to Stand Up to a Dictator*（2022）
- 其他：2020-09 加入 Real Facebook Oversight Board（25 人）；2022-08 联合国互联网治理论坛领导小组十成员；2022-10 Issue One 负责任社交媒体委员会；个人信息与民主委员会（RSF 发起）25 位领军人物之一；公开同性恋者
- 关键时间线（16 节点）：1963 生于马尼拉 → 1973 移居新泽西改姓 → 1986 Princeton 毕业 → 1987 共创 Probe → 1986–1995 CNN 马尼拉 → 1995–2005 CNN 雅加达 → 2003 *Seeds of Terror* → 2004–2010 ABS-CBN 新闻部 → 2011 MovePH → 2012-01-01 Rappler 上线 → 2017-07 杜特尔特国情咨文指控 → 2018-01 NBI 传唤+SEC 撤照 → 2019-02-13 逮捕/次日保释 → 2020-06-15 网络诽谤罪成立 → 2021-04-08 UNESCO 新闻自由奖 → 2021-10-08 诺贝尔和平奖 → 2023 税案全部无罪 → 2025-06 反傀儡法无罪

### 第 4 步：事业领域表（4–5 行）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | investigative journalism | 调查新闻 | CNN 亚洲首席调查记者近 20 年 | 核心页 |
| 1 | press freedom | 新闻自由 | 2021 诺奖核心议题 | 诺奖页 |
| 2 | disinformation | 假信息治理 | 打击网络操纵与假新闻 | Rappler 页 |
| 3 | terrorism research | 恐怖主义研究 | 两部东南亚恐袭专著 | 著作页 |
| 4 | digital media | 数字媒体 | Rappler 创业、AI 与民主项目 | 创业页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Dmitry Muratov | 无向 | 2021 诺贝尔和平奖共同得主；2023-01 联名致函马科斯总统 |
| founder | Rappler | — | 联合创始人（2012-01-01 上线），任执行编辑兼 CEO |
| controversy | Rodrigo Duterte | 无向 | Rappler 长期批评其禁毒战争等政策；2017 指控 Rappler 美资违宪，SEC 撤照，本人被捕定罪（官方否认政治动机） |

> 不入库（仅叙述）：Amal Clooney / Caoilfhionn Gallagher / Can Yeğinsu（国际律师团队，代理关系无类型）；Theodore Te（FLAG 主持法务）；Wilfredo Keng（原告）；Benigno Aquino III（采访对象/批评事件）；Jonas Gahr Støre（提名者）；Sheila Coronel（评论者）；各国际机构委员职务。

### 第 5 步：配色方案 【manifest 预分配，勿改主色】

- **主色**：深棕赭 `#5C3A1E`（坚韧、大地）
- **辅助**：诺奖香槟金 `C9A227`
- **badge 四色**（事业分类）：
  - `badgeIJ` 调查新闻 — 青绿 `#0E7C7B`
  - `badgePF` 新闻自由 — 玫瑰 `#C4204F`
  - `badgeDI` 假信息治理 — 琥珀 `#E07B30`
  - `badgeDM` 数字媒体 — 靛蓝 `#4C5FD5`
- **背景母题**：屏幕光束与天平剪影，主色渐变

### 第 6 步：规划幻灯片序列（13 页 = 共享封面 + 12 帧）

```
00  OpenPeace 项目首页（\input cover 共享首页）
01  封面 — 真相的防线 / Maria Ressa 1963– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 生卒/出生地/教育/职业轨迹/任职/主要荣誉/核心领域
03  核心事业概览 — 调查新闻 / 新闻自由 / 假信息治理 / 恐怖主义研究 / 数字媒体
04  早年与 Princeton (1963–1986) — 马尼拉→新泽西、改姓、英语文学 cum laude
05  CNN 岁月 (1987–2005) — Probe、马尼拉/雅加达分社长、恐怖主义网络调查
06  ABS-CBN 与著作 (2004–2011) — 新闻部掌门、两部恐袭专著
07  Rappler 创业 (2011–2012) — MovePH→上线、四位女性创始人+12 人团队
08  法律战线 I (2017–2019) — 国情咨文指控、SEC 撤照、Keng 网络诽谤案、被捕与保释
09  法律战线 II (2020–2025) — 定罪与国际反响（HRW/大赦/RSF"卡夫卡式"）、
    2023 税案无罪、2025 反傀儡法无罪——两说并陈（官方立场 vs 国际批评）
10  诺贝尔和平奖 2021 — 与 Muratov 共享；1935 年以来首批获奖记者
11  荣誉与学术任职 — Time Guardians、UNESCO 奖、哥伦比亚/MIT/哈佛
12  著作与结语 — *How to Stand Up to a Dictator*（2022）+ 三部曲书影
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表

- 法律时间线页（08/09）信息密集：用 tabularx 两栏（年份|事件），arraystretch 0.62 + 顶部 −0.4cm 控高；指控/判决措辞逐字对照 page.md，勿加形容词。

| 陷阱 | 说明 |
|------|------|
| ★政治敏感红线 | 杜特尔特禁毒战争、Rappler 案件、2024 哈佛毕业演讲引发的加沙战争争议（含"把以色列比作希特勒"的社论指控与反犹指控之争）——**全程按 page.md 客观记录、零评价；加沙相关一节禁写（政治敏感红线，幻灯片直接省略该事件）** |
| 两说并陈 | 逮捕/定罪的政治动机之争：反对派与国际社会视作政治打压 vs 马拉坎南宫称系私人诉讼；NPCL 与 National Press Club 各有表态——双方观点并列注明归属，勿采信单方 |
| 引语白名单 | 可用原文引语仅限：诺奖理由 EN；庭审首日语 "This case of cyberlibel stretches the rule of law until it breaks."（page.md 明载）。判决书/杜特尔特言论转述即可，尽量不作装饰性引用 |
| 判决细节 | 2020-06-15 定罪：刑期六个月至六年+罚款 40 万比索；保释金 2019-02-13 当日 6 万比索不足、次日 10 万比索获释——数字勿混 |
| 税案数字 | BIR 认定 1.33 亿比索；2023-01 四项+2023-09 一项全部无罪；2025-06-13 反傀儡法无罪——时间线顺序勿倒 |
| 出生名 | 本名 Maria Angelita Delfin Aycardo，10 岁随继父改姓 Ressa——勿写成"笔名" |
| 双籍 | Citizenship Philippines + U.S.（infobox 明载），国籍行写"Philippines / United States" |
| 共享奖主语 | 获奖理由主语 "their"（与 Muratov 共享），中英引用勿改单数 |
| 1935 口径 | "1935 年以来首批获诺贝尔和平奖的记者"（page.md 明载），勿写"史上首位记者" |
| 提名人 | 提名者 Jonas Gahr Støre 时为挪威工党领袖（后任首相的表述 page.md 未载，勿加） |

### 第 9 步：术语清单（8–12 条）

| 英文 | 中文 | 风险点 |
|------|------|------|
| freedom of expression | 言论自由 | 诺奖理由核心词 |
| cyberlibel | 网络诽谤 | Cybercrime Prevention Act of 2012 框架下 |
| Rappler | 拉普勒（新闻网站） | 勿拆译；2012-01-01 上线 |
| disinformation | 假信息 | 与 misinformation 勿混用 |
| bureau chief | 分社社长 | CNN 马尼拉/雅加达两站 |
| investigative journalism | 调查新闻 | 与深度报道区分 |
| Golden Pen of Freedom Award | 新闻自由金笔奖 | 世界报业协会，2018 |
| UNESCO/Guillermo Cano Prize | 联合国教科文组织吉列尔莫·卡诺世界新闻自由奖 | 2021-04，全称勿缩错 |
| Time Person of the Year 2018 | 时代 2018 年度人物 | "The Guardians" 群体 |
| Real Facebook Oversight Board | 真脸书监督委员会 | 独立监察组织，非 Meta 官方 |
| Anti-Dummy Law | 反傀儡法 | 外资持股限制案件，2025-06 无罪 |

---

## 四、背景音乐选择 ✅ 【manifest 预分配，勿改】

- **选定曲目**: **Eternals** — Alex-Productions
- **bgm_path**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`
- **匹配理由**: 绵长不屈的行进感，匹配"多年法律拉锯中持续发声"的坚韧叙事——冷峻而有力量。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Maria_Ressa/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/Maria_Ressa.yaml` | 社会关系/领域入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；法律案件两说并陈；政治敏感事件（加沙争议）禁写。**
