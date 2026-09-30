# 和平奖得主立传提示词（OpenPeace 21 世纪批次：Barack Obama）

> 本文件是 OpenPeace 项目 21 世纪诺贝尔和平奖批次的人物专属立传提示词。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（OpenMathAI 共享仓库 `peace/` 侧）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词结构）与和平奖侧 20 世纪批次实战经验。
- **本实例**：Barack Hussein Obama II（巴拉克·奥巴马，2009 诺贝尔和平奖，美国第 44 任总统）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Barack Hussein Obama II（1961-08-04 生于檀香山，在世）
- **官方获奖理由（照抄，禁止改写）**：
  > "for his extraordinary efforts to strengthen international diplomacy and cooperation between peoples."
  > 表彰他为加强国际外交与各国人民间合作所做的非凡努力
- **气质关键词**：**桥梁的建造者、演说家总统、历史的第一人**
- **设计母题**：**桥梁（bridge）**。获奖理由核心词是 "cooperation between peoples"——用「连接两岸的桥」作为贯穿封面与章节页的视觉母题（拱形元素、双岸对称构图）。
- **本地数据源**：`peace/presentations/pages/21th_century/Barack_Obama/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 和平奖侧成品参照：`peace/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（第一轮已核对，来源 = 本地 page.md） 【人物专属】

- 生卒：1961-08-04 生于檀香山 Kapiolani 妇幼医疗中心（在世，无卒日）；唯一一位出生在本土四十八州之外的美国总统
- 国籍：美国
- 家庭：父 Barack Hussein Obama Sr.（1934–1982，肯尼亚卢奥人，经济学家，1982 车祸去世）；母 Ann Dunham（1942–1995，堪萨斯州威奇托出身，人类学博士 1992）；父母 1960 在夏威夷大学俄语课上相识、1961-02-02 于 Wailuku 成婚、1964-03 离异；继父 Lolo Soetoro（1965-03-15 成婚）；同母异父妹 Maya Soetoro-Ng
- 教育：雅加达（1967–1971，St. Francis of Assisi 天主教小学、Menteng 01 公立小学 + 母亲 Calvert 函授）；1971 返回檀香山与外祖父母同住；Punahou School（奖学金，1979 毕业）；Occidental College（全额奖学金，1981 转学）；Columbia University（政治学，国际关系方向，1983 BA，GPA 3.7）；Harvard Law School（1988 入学，JD magna cum laude 1991，《哈佛法律评论》首位黑人主编）
- 早年职业：Business International Corporation 金融研究员；New York Public Interest Research Group 项目协调员；芝加哥南区 Developing Communities Project 主任（1985-06 – 1988-05，社区组织者）；Gamaliel Foundation 顾问；Project Vote 伊利诺伊州主任（1992，登记 15 万非裔选民）
- 学术：University of Chicago Law School 宪法学讲师（1992–1996）/高级讲师（1996–2004）；Laurence Tribe 的研究助理（哈佛期间）
- 政治生涯：伊利诺伊州参议员（第 13 选区，1997-01-08 – 2004-11-04）；2000 年联邦众议员初选败给 Bobby Rush；联邦参议员（伊利诺伊，2005-01-03 – 2008-11-16）；2008 年击败 Hillary Clinton 获民主党提名，搭档 Joe Biden，击败 John McCain/Sarah Palin 当选
- 美国第 44 任总统（2009-01-20 – 2017-01-20，首位非裔总统）：American Recovery and Reinvestment Act 2009；Dodd–Frank 法案；Affordable Care Act；任命大法官 Sonia Sotomayor（首位拉美裔）与 Elena Kagan；结束伊拉克战争；下令 Operation Neptune Spear（2011-05-02 击毙 Osama bin Laden）；2011 利比亚军事干预；2012 击败 Mitt Romney 连任；New START；巴黎协定；伊朗核协议（JCPOA）；美古关系正常化
- 诺贝尔和平奖：2009-10-09 宣布（就任仅九个月），获和平奖的是第四位美国总统、第三位在任获奖者；**该决定招致赞誉与批评并存**（"drew a mixture of praise and criticism from world leaders and media figures"）——两说并陈；本人称其为 "call to action"，并表示 "I do not view it as a recognition of my own accomplishments but rather an affirmation of American leadership on behalf of aspirations held by people in all nations"
- 卸任后：Obama Foundation（2017 首届峰会）；One America Appeal（2017，与 Jimmy Carter、George H. W. Bush、Bill Clinton、George W. Bush 五位前总统联手救灾）；Higher Ground Productions（2018 与米歇尔创立，American Factory 2020 获奥斯卡最佳纪录长片）；回忆录 A Promised Land（2020）；与 Bruce Springsteen 播客 Renegades
- 关键荣誉：诺贝尔和平奖 2009；Time 年度人物 2008/2012；两座 Grammy 最佳诵读专辑（2006/2008）；三座 Primetime Emmy 最佳旁白（2022/2023/2025）；Profile in Courage Award 2017；Ripple of Hope Award 2018；Ambassador of Humanity Award 2014
- 家庭：与 Michelle Robinson 于 1992-10-03 成婚（1989-06 在 Sidley Austin 相识，Robinson 曾任其三个月导师）；长女 Malia Ann（1998）、次女 Natasha "Sasha"（2001）
- 关键时间线（15–20 节点）：1961 檀香山出生 → 1967 迁雅加达 → 1971 返檀香山 → 1979 Punahou 毕业 → 1979–81 Occidental → 1981 转学哥伦比亚 → 1983 BA → 1985–88 社区组织者 → 1988 入哈佛法学院 → 1990 法律评论首位黑人主编 → 1991 JD → 1992 成婚+Project Vote → 1992–2004 芝加哥法学院执教 → 1996 当选州参议员 → 2004 联邦参议员 → 2008 当选总统 → 2009 诺贝尔和平奖 → 2011 击毙 bin Laden → 2012 连任 → 2015 巴黎协定 → 2017 卸任 → 2020 A Promised Land

### 第 4 步：事业领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international diplomacy | 国际外交 | 获奖理由核心，New START/巴黎协定/JCPOA | 核心页 |
| 1 | civil rights | 民权 | 民权律师出身，LGBT 权利推进 | 民权页 |
| 2 | constitutional law | 宪法学 | 芝加哥法学院 12 年执教 | 学术页 |
| 3 | community organizing | 社区组织 | 芝加哥南区 DCP 主任（1985–1988） | 早年页 |
| 4 | public policy | 公共政策 | ACA/金融改革/医改立法 | 政策页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Michelle Obama | 无向 | 1992-10-03 成婚，1989 于 Sidley Austin 相识 |
| parent-child | Barack Obama Sr. | 无向 | 父亲，肯尼亚卢奥人经济学家（1934–1982） |
| parent-child | Ann Dunham | 无向 | 母亲，人类学家（1942–1995） |
| colleague | Joe Biden | 无向 | 2008 竞选搭档、两届副总统 |
| colleague | Jimmy Carter | 无向 | One America Appeal 五位前总统联手（库内 id=7114 复用） |
| rival | Hillary Clinton | 无向 | 2008 民主党初选对手 |
| rival | John McCain | 无向 | 2008 年大选对手 |

### 第 5 步：设计配色方案 【manifest 预分配，勿改】

- **主色**：`#2F4470`（华盛顿蓝——务实与外交）
- **诺奖香槟金**：`C9A227`
- badge 四分类色（建议）：国际外交 深蓝 `#1E4E79`；民权 深绯 `#7E1E23`；宪法学 靛蓝 `#4C5FD5`；社区组织 琥珀 `#E07B30`
- **背景母题**：桥拱与两岸对称构图（呼应「桥梁」母题）

### 第 6 步：规划幻灯片序列 【人物专属，可微调；共 15 页 = 共享封面 + 14 帧】

```
00  OpenPeace 项目首页（\input cover 共享页）
01  封面 — 第 44 任总统的和平奖 / Barack Obama b. 1961 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心事业概览 — 国际外交 / 民权 / 宪法学 / 社区组织
04  早年：檀香山与雅加达 (1961–1979) — 双重文化童年、Punahou
05  哥伦比亚与社区组织者 (1979–1988) — 芝加哥南区 DCP
06  哈佛法学院与芝加哥讲席 (1988–2004) — 法律评论首位黑人主编、宪法学 12 年
07  从州参议员到联邦参议员 (1996–2008) — 2004 党代会主题演讲之后
08  2008 年大选 — 击败初选对手与McCain、当选首位非裔总统
09  诺贝尔和平奖 (2009) — 就任九个月获奖、"赞誉与批评并存"两说并陈
10  总统任期与外交 (2009–2017) — New START、巴黎协定、JCPOA、美古破冰
11  国内政策里程碑 — ACA、Dodd–Frank、两位大法官任命
12  卸任后：Obama Foundation 与写作 — 五前总统 One America Appeal、A Promised Land
13  荣誉与认可 — 诺贝尔奖/两 Grammy/三 Emmy/Profile in Courage
14  遗产与结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照已有和平奖成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用同项目已立传目录骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Obama 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| ★ 获奖争议两说并陈 | page.md 明载 "drew a mixture of praise and criticism"——**必须两面并写**：一面是获奖理由原文与"第四位获和平奖总统/第三位在任获奖者"事实，一面是"就任仅九个月、决定引发布评"的客观记录；勿单边定性，勿替委员会或批评者代言 |
| 本人回应口径 | 其原话 "call to action" 与 "affirmation of American leadership..." 为 page.md 明载英文原文，可引用；其余引语禁编 |
| 父亲同名 | 父 Barack Hussein Obama **Sr.**，本人 II（the second）——行文注意 Sr./II 后缀，勿混 |
| 米歇尔婚前姓 | Michelle **Robinson**（婚后从夫姓）；Sidley Austin 时期她曾任其三个月导师——这段写相遇即可，勿写成"上司下属"以外的定性 |
| 宗教争议 | Jeremiah Wright 争议正文有载，但与和平奖主线无关——幻灯片**不设**该页；若提及只客观一句 |
| 当代政治评价 | 特朗普相关段落（2024/2026 交锋等）一律**禁写**；卸任后政治活动只写 One America Appeal、基金会、著作等建设性事实 |
| 大法官任命 | Sotomayor 是**首位拉美裔**大法官；Kagan 同任——两人都是任命而非"提名未遂" |
| 名字书写 | 全名 Barack Hussein Obama II；切勿漏掉 Hussein 以外的中名，也勿把 II 写成 Jr. |
| 无载禁写 | page.md 未载的颁奖细节（如领奖演说全文、具体日期场合）禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| international diplomacy | 国际外交 | 获奖理由原词 |
| cooperation between peoples | 各国人民间合作 | 获奖理由原词，勿改写 |
| Developing Communities Project | 社区发展计划 | 芝加哥南区，1985–1988 |
| Harvard Law Review | 《哈佛法律评论》 | 首位黑人主编（1990） |
| constitutional law | 宪法学 | 芝加哥法学院执教领域 |
| Affordable Care Act | 平价医疗法案（ACA） | 常被称 Obamacare——提示词建议用官方名 |
| New START | 新削减战略武器条约 | 2010 与俄签署 |
| JCPOA | 伊朗核协议 | 联合全面行动计划 |
| Operation Neptune Spear | 海神之矛行动 | 2011-05-02 |
| One America Appeal | 美国一体呼吁 | 2017 五位前总统联合赈灾 |

---

## 四、背景音乐选择 【manifest 预分配，勿改】

- **选定曲目**：**The Invisible Light** — Infraction（inspiring-electronic 曲库）
- **风格**: 纪录片 / 沉稳 / 希望
- **匹配理由**：
  - "不可见的光" 匹配其获奖理由的本质——「加强外交与合作」是看不见的努力，却在九个月后被看见
  - 纪录片气质匹配其叙事结构：檀香山→雅加达→芝加哥→哈佛→白宫，一部跨文化成长纪录片
  - 沉稳底色匹配两说并陈的克制基调——本篇不渲染、不辩论，让事实自己说话
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Barack_Obama/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
