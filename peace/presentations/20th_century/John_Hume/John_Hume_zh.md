# 和平奖得主立传提示词（OpenPeace · John Hume）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」**，以 John Hume（1998 诺贝尔和平奖，北爱尔兰和平进程建筑师）为实例。
> 结构对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 凡标注 `【模板通用】` 的部分可复用到任何和平奖得主；标注 `【人物专属】` 的部分为本人物专属内容。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **模板来源**：综合 OpenPhysicist / OpenChemist / OpenMedic 各侧标杆提示词与 Beamer 实战经验。
- **本实例**：John Hume（约翰·休姆）。
- **设计哲学**：和平奖得主立传必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：John Hume（1937-01-18 ~ 2020-08-03，享年 83 岁）
- **获奖**：1998 诺贝尔和平奖（与 David Trimble 共享），官方获奖理由：
  > "for their efforts to find a peaceful solution to the conflict in Northern Ireland."
  > （中译照抄名录：表彰他们为和平解决北爱尔兰冲突所做的努力）
- **气质关键词**：**宪政民族主义的谈判者、信用社运动的先行者、跨社群和解的坚持者**
- **设计母题**：**桥梁（bridge）**。Hume 一生的方法是把「分割」替换为「多样性」——在北爱尔兰两个传统之间、在南北爱尔兰之间、在伦敦-都柏林-华盛顿之间架设对话之桥；欧洲议会经历又让他把「分裂社会未必暴力」的欧洲和解经验带回北爱。视觉母题用桥拱/连接结构呼应。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/John_Hume/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 项目首页：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，第一轮已核对】

- **生卒**：1937-01-18 生于北爱尔兰德里（Derry）工人阶级天主教家庭 ~ 2020-08-03 凌晨逝于德里一家养老院，享年 83 岁；2015 确诊阿尔茨海默病（1990 年代末已现症状）。
- **国籍**：Ireland / United Kingdom（frontmatter 两值；北爱尔兰德里人，爱尔兰民族主义者）。
- **家庭**：七子之长；父 Samuel Hume（退伍军人、造船厂工人），母 Anne "Annie"（娘家姓 Doherty，缝纫工）；姓氏源自一位迁居多尼戈尔的苏格兰长老会曾祖父。1960 与小学教师 Patricia "Pat" Hone（1938-02-22 ~ 2021-09-02）结婚，育有五子女（Thérèse、Áine、Aidan、John、Mo）、16 孙辈；1973 年女儿 Áine 曾遭临时派 IRA 绑架未遂（错绑同学）。
- **教育**：受 1947 年《教育法》奖学金惠及，先后就读 St Columb's College（文法学校）与 St Patrick's College, Maynooth（爱尔兰首席天主教修院/国立大学认可学院，师从 Tomás Ó Fiaich，转向阿尔斯特地方史）；1958 获法语与历史学士，未完成神职学业；1964 以 19 世纪德里移民问题论文获 Maynooth 硕士。
- **任职**：1958 回德里任母校 St Columb's 教师；1960（23 岁）协助创建德里信用社（北爱第一家合作社区银行），四年内成为爱尔兰信用联盟（Irish League of Credit Unions）史上最年轻主席（至 1968）；1969-02 当选北爱议会议员（Foyle）；1970-08 与 Gerry Fitt 等五名 Stormont 议员共创 SDLP 任副领袖，1979-05-06 接任领袖（至 2001-11-06）；1974 权力共享行政当局商务部长（Sunningdale 协议签署者）；1979-2004 连任五届欧洲议会议员（北爱尔兰选区，社会党团）；1983-2005 英国下议院 Foyle 议员；1998-06 新北爱议会议员（Foyle），1998-07 把副首席部长职务让与 Seamus Mallon。
- **关键荣誉**：Nobel Peace Prize 1998（共同得主）；Martin Luther King Award 1999；International Gandhi Peace Prize 2001（唯一同时集齐诺贝尔+马丁·路德·金+甘地三大和平奖者）；Légion d'Honneur 军官勋位 1999；Hessian Peace Prize 1995；Four Freedoms 言论自由奖 1996；Golden Plate 2002；RTÉ "Ireland's Greatest" 观众票选第一 2010；教宗本笃十六世授圣额我略骑士团指挥官勋章（KCSG）2012；44 个荣誉博士学位（1995 Boston College LL.D. 为其中之一）。
- **核心事业清单**：① 信用社运动（自称最引以为傲的事业）；② 1960 年代民权与住房运动（1965 大学争取委员会主席、Duke Street 游行后任公民行动委员会副主席）；③ 创立并领导 SDLP（宪政民族主义路线，反对"武装斗争"）；④ 北美游说（与"四骑士"Tip O'Neill、Ted Kennedy、Moynihan、Hugh Carey 合作促成 1977 卡特声明、劝阻 NORAID 捐款）；⑤ 与 Adams 的危险对话（1988 起，换取停火与和平进程）；⑥ 耶稣受难日协议的建筑师（挪威诺奖委员会 1998 授奖词口径）。
- **关键时间线（17 节点）**：1937 生于德里 → 1958 Maynooth 学士、回德里任教 → 1960 结婚、创建德里信用社 → 1964 爱尔兰信用联盟主席、《The Northern Catholic》两篇 → 1965 大学争取委员会主席、Stormont 万人抗议 → 1968-10-05 Duke Street 游行遭警棍驱散 → 1969-02 当选 Stormont 议员 → 1970-08 SDLP 副领袖 → 1971-07 带领 SDLP 退出 Stormont → 1972-01-22 Magilligan 海滩抗议；Bloody Sunday（1972-01-30）后坚持非暴力 → 1973-12-09 签署 Sunningdale 协议、1974-01-01 任商务部长 → 1974-05 工人委员会大罢工、行政当局垮台 → 1979-05 任 SDLP 领袖、1979-06 当选欧洲议员 → 1981 绝食选举中让 SDLP 按兵不动 → 1985-11 Anglo-Irish 协议（Mallon 归功其华盛顿游说）→ 1988-01 与 Adams 在 Clonard 修道院首谈 → 1994-08 IRA 停火 → 1998-04-10 贝尔法斯特（耶稣受难日）协议、1998-10 诺贝尔和平奖 → 2004-02-04 宣布彻底退休 → 2020-08-03 逝世。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace process | 和平进程 | 1998 耶稣受难日协议建筑师，1998 诺奖核心 | 核心页 |
| 1 | politics | 政治 | SDLP 创党人/领袖、四层议会任职 | 身份页 |
| 2 | conflict resolution | 冲突解决 | 「以多样性取代分裂」的欧洲经验移植 | 欧洲页 |
| 3 | european integration | 欧洲一体化 | 五届欧洲议员，少数语言保护倡导者 | 欧洲页 |
| 4 | credit union movement | 信用社运动 | 1960 创建德里信用社，自称最自豪事业 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| co-honored | David Trimble | 无向 | 1998 诺贝尔和平奖共同得主 |
| spouse | Pat Hume | 无向 | 1960 结婚，小学教师，2021 逝世 |
| colleague | Gerry Fitt | 无向 | SDLP 首任领袖，Hume 为副领袖并于 1979 接任 |
| colleague | Seamus Mallon | 无向 | SDLP 副领袖，并肩 22 年，1998 接任副首席部长 |
| colleague | Gerry Adams | 无向 | 1988 起就结束冲突对话，1994 联合声明 |
| colleague | Ian Paisley | 无向 | 1983 北美投资推广之旅同行的欧洲议员同僚 |
| colleague | George Mitchell | 无向 | Hume 提议其主持国际解除武装委员会 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：沉稳、务实、跨社群
- **配色**：主色石板灰蓝 `#37474F`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 和平进程 — 深青 `#0E7490`
  - `badgeB` 政治 — 靛蓝 `#4C5FD5`
  - `badgeC` 冲突解决 — 青绿 `#0E7C7B`
  - `badgeD` 信用社/欧洲 — 琥珀 `#E07B30`
- **背景母题**：桥拱与连接线条（呼应设计母题「桥梁」）。

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 北爱尔兰和平的建筑师 / John Hume 1937–2020 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  早年与教育：德里少年 (1937–1958) — 1947 教育法奖学金、Maynooth、转向阿尔斯特地方史
04  信用社运动：最自豪的事业 (1960–1968) — 德里信用社、最年轻联盟主席
05  民权浪潮 (1963–1969) — The Northern Catholic、大学争取委员会、Duke Street 游行
06  创党与 Stormont (1969–1972) — SDLP 成立、退出 Stormont、Bloody Sunday 后坚持非暴力
07  Sunningdale 与 1974 (1973–1974) — 商务部长、爱尔兰委员会、行政当局垮台
08  欧洲经验 (1979–2004) — 五届欧洲议员、「多样性取代分裂」
09  华盛顿游说 (1977–1998) — 四骑士、卡特声明、NORAID 劝阻
10  与 Adams 的对话 (1988–1998) — Clonard 会谈、联合声明、1994 停火
11  耶稣受难日协议与诺贝尔奖 (1998) — D'Hondt 选择性纳入原则、授奖词
12  晚年与遗产 — 退休、John and Pat Hume 基金会、John Hume Peace Prize（2026 设立）
13  结尾
```

### 第 7 步：版式要点 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。
- 每写完一页 `make` 编译，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。

### 第 8 步：专属陷阱表 【人物专属，红线】

| 陷阱 | 说明 |
|------|------|
| 政治敏感红线 | 北爱冲突、准军事组织、英爱关系一律只按 page.md 客观事实记录，禁任何评价性语句；引语仅限 page.md 载有英文原文者 |
| 共享奖措辞 | 1998 与 Trimble 共享，获奖理由主语是 "their efforts"（他们），勿写成单人；两人为共享得主而非合作者 |
| 与 Trimble 关系 | page.md 明载两人存在 "reserved"（疏淡）关系，仅事实陈述，勿渲染为不和 |
| Bloody Sunday 数字 | 1972-01-30 中弹 26 人、死 14 人（官方调查后确认 13 起杀害全部不正当），数字勿混 |
| 绝食选举评价 | SDLP 让路被视为助推新芬党走上政治道路，page.md 用的是「被视为」，转述时保留限定语 |
| 信用社身份 | Hume 希望以信用社运动先行者身份被记住（page.md 明载），勿漏 |
| 无博士学位 | 无任何研究生学位记载，禁编造「博士」；Maynooth 1964 硕士（移民论文） |
| 家庭数字 | 七子之长、五子女（具名 Thérèse/Áine/Aidan/John/Mo）、16 孙辈；1973 Áine 绑架未遂 |
| 奖项年份 | MLK Award 1999、Gandhi Peace Prize 2001、KCSG 2012、「唯一三奖集齐」表述按 page.md |
| 目录名一致 | 输出目录 `John_Hume/`，Makefile `MAIN=John_Hume_zh` |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Good Friday Agreement | 耶稣受难日协议 | 又称贝尔法斯特协议，全篇统一 |
| SDLP | 社会民主工党 | 全称 Social Democratic and Labour Party |
| credit union | 信用社 | 非「信贷联盟」混用 |
| power-sharing | 权力共享 | 1974 与 1998 两次机制勿混 |
| Council of Ireland | 爱尔兰委员会 | 1974 垮台导火索之一 |
| Anglo-Irish Agreement | 英爱协议 | 1985，撒切尔与 FitzGerald 签署 |
| internment | 未经审判的拘禁 | 1971-08 起 |
| decommissioning | 解除武装 | 国际委员会由 Hume 提议、Mitchell 主持 |
| D'Hondt system | d'Hondt 制 | 部长职位比例分配，Hume 团队首创提案 |
| Sunningdale Agreement | 桑宁代尔协议 | 1973-12-09 签署 |
| abstentionism | 弃权主义 | 老民族主义政策，Hume 主张放弃 |
| témoignage 相关词 | — | 本篇无；勿从 MSF 篇串词 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions（manifest 预分配，勿改）
- **匹配理由**: 「觉醒/新生」匹配 Hume 的事业本质——从信用社唤醒社区自助，到以对话唤醒北爱走出三十余年冲突；1998 耶稣受难日协议正是「觉醒」后的制度新生。
- **本地路径**: `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 复制为 `presentations/20th_century/John_Hume/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/John_Hume/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/John_Hume.yaml` | 社会关系/领域入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
