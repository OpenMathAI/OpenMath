# 和平奖得主立传提示词（OpenPeace：Lech Wałęsa / 莱赫·瓦文萨）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Lech Wałęsa（1983 诺贝尔和平奖，团结工会领袖、波兰首任民选总统）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth G. Wilson 提示词 + Beamer 立传骨架；和平奖侧沿用「身份信息页 + 领域结构化」骨架。
- **本实例**：Lech Wałęsa（1943-09-29 生，在世）。
- **设计哲学**：和平奖得主立传与科学家立传的核心差异，在于「事业领域」以**社会运动与制度转型**呈现；本篇三段式主线——「造船厂电工 → 团结工会领袖 → 波兰首任民选总统」，1983 诺奖落在第二段中点。

---

## 二、背景信息 【人物专属】

- **目标人物**：Lech Wałęsa（1943-09-29 生于波普沃 Popowo，在世）
- **官方获奖理由**（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > 英文原文（nobel_peace_citations.json，清理引注噪声后）："for non-violent struggle for free trade unions and human rights in Poland."
  > 中译：表彰他为波兰自由工会与人权进行的非暴力斗争
- **气质关键词**：**翻越船厂围栏的电工、千万人的工会主席、带着特大号钢笔的谈判者**。
- **设计母题**：**栏杆与钢笔（the fence, the pen）**——1980-08-14 翻越列宁造船厂围栏、1980-08-31 用巨型钢笔签署格但斯克协议；视觉母题取「锈红钢栏 + 签字笔的金色弧线」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Lech_Wałęsa/page.md`（Wikipedia 全文 + frontmatter，QID Q444）。
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 和平奖项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（已核对 page.md，禁止杜撰） 【人物专属】

- 生卒：1943-09-29 生于 Popowo（Lipno 县，今库亚维-滨海省），时值纳粹德国占领；在世。
- 国籍：波兰（名录口径）。
- 家庭：父 Bolesław Wałęsa（1909–1945，木匠，被德占当局强征入 Młyniec 劳改营，战后两个月病逝）；母 Feliksa Wałęsa（née Kamieńska；1915–1976）；母改嫁其叔 Stanisław Wałęsa（1917–1981）；三位亲兄姐（Izabela/Edward/Stanisław）+ 三位同母异父弟弟（Tadeusz/Zygmunt/Wojciech）。1969-11-08 与 **Mirosława Danuta Gołoś**（Danuta Wałęsa）结婚，育有八子女（Bogdan 1970 / Sławomir 1972–2025 / Przemysław 1974–2017 / Jarosław 1976 / Magdalena 1978 / Anna 1980 / Maria-Wiktoria 1982 / Brygida 1984）；Jarosław 为欧洲议会议员（2009–2019）。
- 教育：1961 于 Chalin/Lipno 完成小学与职业学校，成为合格电工；无高等教育学历（页面明载 ex-electrician with no higher education，勿升格）。
- 职业线：1962–64 汽车修理工 → 两年义务兵役（至上等兵下士）→ 1967-07-12 入格但斯克列宁造船厂（今格但斯克造船厂）任电工。
- 任职/政治：
  1. 1968 鼓动工友抵制官方谴责学生罢工的集会；1970 组织格但斯克造船厂非法抗议（三十余名工人死亡）。
  2. 1976 因持续参与非法工会/罢工被造船厂解雇；与 KOR（工人保卫委员会）密切合作；1978-06 加入地下沿海自由工会。
  3. 1980-08-14 列宁造船厂罢工，翻越围栏成为罢工领袖，领导厂际罢工委员会；1980-08-31 以特大号钢笔签署**格但斯克协议**（政府获准工人罢工权与独立工会）——团结工会（Solidarność）成立，当选全国协调委员会主席（任至 1991-02-23），会员超千万（逾波兰人口四分之一）。
  4. 1981-12-13 雅鲁泽尔斯基宣布军管，被捕；羁押 11 个月（Chylice/Otwock/Arłamów），1982-11-14 获释；1982-10-08 团结工会被取缔。
  5. 1983 申请重返造船厂任电工；同年获诺贝尔和平奖，因担心当局不许其回国，**由妻子 Danuta 代为领奖**。
  6. 1986 大赦后共创团结工会临时委员会；1988 中再启格但斯克罢工。
  7. 1989-02–04 圆桌谈判（非官方方面领导人）→ 半自由议会选举团结工会横扫 → 1989-08 促成第一个非共产党联合政府（Mazowiecki 任总理）；1989-11 在美国国会发表「We the People」演讲（首位非国家元首对美国国会联席会议演讲）。
  8. 1990-12-09 当选总统（1990-12-22 就任至 1995-12-22）——1922 年以来首位民选国家元首、首位普选产生的波兰总统；任内 Balcerowicz 计划市场化转型、1993 谈成苏军撤出波兰、支持入约入盟；提出 NATO bis 设想（受邻国冷遇）。
  9. 1995 创立 Lech Wałęsa Institute（智库）；1995 总统选举败给 Kwaśniewski（第二轮 48.28%）；1997 创立波兰第三共和国基督教民主党；2000 总统选举仅得 1.01% 退出政坛；2006 因团结工会支持法律与公正党而退出该工会；2008 设立 Lech Wałęsa Award。
- 关键荣誉：**Nobel Peace Prize 1983**；Time 年度风云人物 1981；Time 百大人物 1999；费城自由勋章首位得主 1989；欧洲人权奖 1989；总统自由勋章 1989；45+ 荣誉博士（Harvard/Fordham/Columbia/Sorbonne 等）；骑士大十字级巴斯勋章（英）、法国荣誉军团大十字、德国联邦功绩勋章等 30+ 国勋章；2004 格但斯克机场以他命名。
- 核心事业清单：
  1. 团结工会的缔造与领导（1980–1991 主席）。
  2. 非暴力抗争：罢工组织、地下活动（motto「Solidarity will not be divided or destroyed」刊于每期地下刊物 Tygodnik Mazowsze）。
  3. 圆桌谈判与 1989 转型。
  4. 总统任内的市场化与亲西方外交。
  5. 卸任后的 Lech Wałęsa Institute 与全球讲学（三讲 portfolio，出场费约 £50,000）。
- 关键时间线（18 节点）：1943 生于被占领的波普沃 → 1945 父病逝 → 1961 电工职业资格 → 1967 入列宁造船厂 → 1968 抵制官方集会 → 1970 组织抗议 → 1976 被解雇 → 1978 加入地下自由工会 → 1980-08-14 翻栏领导罢工 → 1980-08-31 签格但斯克协议、任团结工会主席 → 1981 Time 风云人物 → 1981-12-13 军管被捕（羁押 11 个月）→ 1983 诺贝尔和平奖（妻代领）→ 1989 圆桌谈判与六月选举 → 1990-12 当选总统 → 1993 苏军撤出 → 1995 竞选连任失利 → 1995 创立研究所 / 2000 退出政坛。
- 可用引语（仅限 page.md 载有英文原文者）：「I don't want to, but I have to」（Nie chcę, ale muszę，竞选口号）；「Solidarity will not be divided or destroyed」（motto）；「We the People」（演讲标题）；1981 对 Jaruzelski 的两段对谈原话。**其余不得补引。**

### 第 4 步：事业领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | trade unionism | 工会运动 | 团结工会缔造者与主席（1980–1991） | 核心页 |
| 1 | nonviolent resistance | 非暴力抗争 | 1983 诺奖理由：自由工会与人权的非暴力斗争 | 核心页 |
| 2 | democracy movement | 民主运动 | 圆桌谈判、1989 转型、首任民选总统 | 核心页 |
| 3 | human rights | 人权 | 诺奖理由并列关键词 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Danuta Wałęsa | 无向 | 1969-11-08 结婚，1983 代夫领诺贝尔和平奖 |
| parent-child | Bolesław Wałęsa | 无向 | 父亲，木匠，1945 病逝 |
| parent-child | Feliksa Wałęsa | 无向 | 母亲，塑造其信念与韧性 |
| parent-child | Jarosław Wałęsa | 无向 | 子，1976 生，欧洲议会议员 2009–2019 |
| founder | Solidarity | 创始人→机构 | 1980 共同创立团结工会并任主席至 1991 |
| founder | Lech Wałęsa Institute | 创始人→机构 | 1995 创立的智库 |
| colleague | Wojciech Jaruzelski | 无向 | 1981 军管宣布者，1981 会面与 1989 圆桌谈判对手方 |
| colleague | Tadeusz Mazowiecki | 无向 | 1989 圆桌后首任非共产党总理，1990 总统选举对手 |
| colleague | Václav Havel | 无向 | 1991-02 共同创立维谢格拉德集团 |
| rival | Aleksander Kwaśniewski | 无向 | 1995 总统选举第二轮对手（48.28% 对 51.72%） |

> 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Lech_Wałęsa.yaml`；校验 has_social_data=1、fields=4、relations=10。
> **裁定**：八名子女中仅 Jarosław Wałęsa 入库（页面有独立条目链接且为政治人物）；其余七名仅具名（无独立词条指向），防 stub 噪声不入库。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：`#4E342E`（manifest 预分配，锈褐——造船厂的钢栏与工装），勿改。
- **辅助**：诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 工会运动 — 锈红 `#8C3A2B`
  - `badgeB` 非暴力 — 橄榄绿 `#4E6B4E`
  - `badgeC` 民主转型 — 皇家蓝 `#2A4B7C`
  - `badgeD` 人权 — 暖金 `#C9A227`
- **背景母题**：竖向栏杆条纹（低透明度锈红竖线阵列 + 一条斜越的金线，隐喻翻越围栏）。

### 第 6 步：规划幻灯片序列（13 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 从船厂电工到民选总统 / Lech Wałęsa 1943– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/家庭/教育/任职/荣誉/核心事业）
03  核心事业概览 — 团结工会 / 非暴力抗争 / 圆桌谈判 / 总统任期
04  早年：被占领年代的波普沃 (1943–1967) — 父亡、电工训练、入伍
05  列宁造船厂 (1967–1980) — 1968/1970 抗议、1976 解雇、KOR 与地下工会
06  翻越围栏的八月 (1980)（核心贡献页一）— 罢工、格但斯克协议、特大号钢笔
07  团结工会：千万人的工会 — 主席岁月、地下刊物 motto
08  军管与诺贝尔奖 (1981–1983)（核心贡献页二）— 11 个月羁押、妻子代领奖
09  圆桌谈判与 1989 (1988–1990) — 谈判、六月选举、首任非共产党总理
10  总统岁月 (1990–1995) — Balcerowicz 计划、苏军撤出、亲西方外交
11  荣誉与认可 — Nobel 1983 · Time 1981/1999 · 45+ 荣誉博士
12  遗产：团结的全球回响 — Lech Wałęsa Institute、机场命名、影视与流行文化
13  结尾
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 在世者口径 | 1943-09-29 生，在世；生卒处写 1943–，勿编卒年 |
| 诺奖口径 | 1983 获奖因担心无法回国**由妻子 Danuta 代领**；获奖时已申请重返造船厂任电工（不是「仍被监禁」——1982-11 已获释） |
| 诺贝尔年份口径 | 获奖为 1983（1982 年度奖，1982-10 公布/1983-12 领奖同一口径写 1983 即可，全篇一致） |
| 政治敏感红线 | 冷战/军管/共产党执政/秘密警察指控/当代波兰政治（PiS、Kaczyński、Trump/Obama 评价、LGBT 言论、乌克兰战争言论）**一律只作 page.md 明载的客观事实记录，不加评价**；幻灯片层面建议：秘密警察指控只写「2000 特别法庭裁定证据不足洗清指控；争议至今存在」一句带过，其余回避 |
| 秘密警察指控 | 双方证据对立（2008 Cenckiewicz/Gontarczyk 书 vs 2018 INR 调查终止认定「行为未发生」），禁止单侧定论；Bolek 代号仅作事实引用 |
| 同名区分 | 父 Bolesław Wałęsa ≠ 子 Bogdan/Sławomir 等；Stanisław Wałęsa 既是亲兄也是继父（叔父），注意两个 Stanisław（兄 1940–2001 / 继父 1917–1981） |
| 子女入库 | 八子女仅 Jarosław 入库（独立词条）；其余七名仅具名禁建关系 |
| 选举数字 | 1995 第二轮 48.28%（对手 Kwaśniewski）；2000 年仅 1.01%；勿与 1990 得票混淆（页面未载具体百分比，勿编） |
| 无载禁写 | 具体博士学位授予年表、1980 罢工日细节之外的谈判内幕、家庭财产等无载内容一律不写 |
| 影视 | 《铁人》(1981) 与《瓦文萨：希望之人》(2013) 均为 Wajda 作品，前者其本人客串；年份勿混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Solidarity (Solidarność) | 团结工会 | 专名，勿译「团结工会运动」后漏组织名 |
| Gdańsk Agreement | 格但斯克协议 | 1980-08-31 |
| Lenin Shipyard | 列宁造船厂 | 今格但斯克造船厂 |
| Inter-Enterprise Strike Committee | 厂际罢工委员会 | 1980-08 |
| Martial law in Poland | 波兰军管 | 1981-12-13 |
| Round Table Agreement | 圆桌协议 | 1989-02–04 |
| Workers' Defence Committee (KOR) | 工人保卫委员会 | 1976 后合作 |
| Sejm | 波兰议会下院（瑟姆） | 勿泛译国会 |
| lustration | 除垢审查 | 2000 法庭语境 |
| Wałęsisms | 瓦文萨式妙语 | 流行文化节 |
| Visegrád Group | 维谢格拉德集团 | 1991-02 共创 |
| Free Trade Unions of the Coast | 沿海自由工会 | 1978 地下组织 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 时间流动感 / 史诗 / 沉稳
- **匹配理由**: 五十年跨度（被占领的童年 → 船厂 → 团结 → 总统府 → 讲台）是典型的时间之流叙事；前半克制、后半上扬的结构正合 1980 八月与 1989 六月两个高点。
- **本地路径**: `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` → `presentations/20th_century/Lech_Wałęsa/The-Flow-of-Time.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Lech_Wałęsa/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与官方获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实全部锚定 page.md，无载禁写；当代政治内容只作客观事实记录。**

---

## 六、第 1–3 步补充（模板通用） 【模板通用骨架】

### 第 1 步：建立目录

- 在 `peace/presentations/20th_century/` 下创建 `Lech_Wałęsa/` 与 `images/`（提示词本文件已就位）。

### 第 2 步：复制 Makefile

- 复制同目录已立传成品的 `Makefile`（或标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`），设置 `MAIN=Lech_Wałęsa_zh`、`VIDEO_NAME=Lech_Wałęsa_zh`。

### 第 3 步：收集图片 【人物专属】

- **肖像**：✅ `pages/Lech_Wałęsa/images.txt` 第 2 条即 2019 布拉格 FORUM 2000 单人照 `Lech_Wałęsa_(2019),_FORUM_2000,_Prague_(2).jpg`，下载 500px 使用；curl 加 `-A "Mozilla/5.0"`，`file` 验证。
- **插图备选**（images.txt 有 URL 的直接用，250px 改 500px）：
  - 1980-08 列宁造船厂罢工照（Strajk sierpniowy…22.jpg，翻栏叙事配图）
  - 1980-08 罢工签名照（Stakingsleider Lech Walesa…）
  - 1981-01 与 Alojzy Mazewski 合影
  - 1985-10 Popieluszko 追思弥撒照（与 Mazowiecki 同框）
- 404/HTML 时换文件名或用 Wikipedia REST API `page/summary` 回退；仍失败则装饰圆占位。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示 Poland；底部状态栏给出 `国籍 | 组织/职务 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心事业之前；左头像 + 右信息网格，至少含生卒/国籍/家庭（妻/父/母/子女数）/教育/任职（船厂/团结工会/总统任期）/主要荣誉/核心事业，事实取自 page.md infobox，不得杜撰；在世者卒年栏写「在世」。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`；共享封面 `\input` 继承，子 deck 不重复。

---

## 七、执行清单（Checklist） 【模板通用】

1. 通读 `pages/Lech_Wałęsa/page.md` 全文（312 行，本文件第 0 步已核对，执行时复核即可）。
2. 建目录 + 复制 Makefile + 下载肖像与罢工插图（`file` 验证）。
3. 复制 BGM：`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` → 目录内 `The-Flow-of-Time.wav`。
4. 按 §4 领域表 + §4.5 关系表核对已入库 DB 字段（fields=4 / relations=10，勿改）。
5. 编写 Beamer 源码（每页 `\newcommand{\xxxslide}`，骨架参照标杆成品 tex）。
6. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt；每写完一页即 make + `pdftoppm` 目检。
7. 页数对账：按 §6 规划逐帧核对（缺帧/合并帧都要能对上页数）。
8. 引语逐条核对 §0 白名单；无原文一律转述。
9. 陷阱表逐条自查（秘密警察指控双列、诺贝尔代领口径、当代政治红线）。
10. `make images && make video` 出片后，提示词回写 Review 备注（肖像来源/事实修正）。
