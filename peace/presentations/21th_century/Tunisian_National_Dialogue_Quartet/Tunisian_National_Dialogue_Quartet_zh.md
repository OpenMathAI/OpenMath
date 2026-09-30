# OpenPeace 21 世纪和平奖得主立传提示词（实例：Tunisian National Dialogue Quartet）

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他学科侧共享体系）。
- **本实例**：Tunisian National Dialogue Quartet（突尼斯全国对话四方机制），2015 诺贝尔和平奖得主，公民社会组织联盟（**组织机构条目，is_org=true**）。
- **设计哲学**：机构立传以「机构概览页」替代个人身份信息页；以「四方会盟」为母题——四个独立组织在悬崖边缘把国家拉回对话桌。

---

## 二、背景信息 【人物专属】

- **目标机构**：Tunisian National Dialogue Quartet（2013 年夏成型，突尼斯）
- **气质关键词**：**危机调解者、宪政缔造者、公民社会四方联盟**
- **2015 官方获奖理由**（照抄名录，禁止改写）：
  > "for its decisive contribution to the building of a pluralistic democracy in Tunisia in the wake of the Jasmine Revolution of 2011."
  > （表彰其在 2011 年茉莉花革命后为突尼斯建设多元民主做出的决定性贡献）
- **设计母题**：**四方会盟（four pillars）**。四个支柱式几何元素共同托举一个圆桌/宪法文本，象征四个公民社会组织的联合斡旋。
- **本地数据源**：`peace/presentations/pages/21th_century/Tunisian_National_Dialogue_Quartet/page.md`
- **结构标杆**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构）
- **yaml 母本**：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属】

- 性质：四个突尼斯公民社会组织的联合体（non-party 中介方），2013 年夏（infobox 作 August 2013–January 2014）在政治危机中组建。
- 四大成员组织：
  1. Tunisian General Labour Union（UGTT，突尼斯总工会）
  2. Tunisian Confederation of Industry, Trade and Handicrafts（UTICA，突尼斯工商业手工业联合会）
  3. Tunisian Human Rights League（LTDH，突尼斯人权联盟）
  4. Tunisian Order of Lawyers（突尼斯全国律师公会）
- 四方领导人（infobox 明载）：Houcine Abassi（UGTT 总书记）、Abdessattar Ben Moussa（人权联盟主席）、Fadhel Mahfoudh（律师公会主席）、Wided/Ouided Bouchamaoui（UTICA 主席）。
- 目标：结束政治暴力、建立临时政府、批准宪法。
- 结果：Mehdi Jomaa 出任看守总理的技术官僚政府、2014 新宪法批准、总统与议会选举如期举行。
- 关键荣誉：2015 诺贝尔和平奖（2015-10-09 宣布）；法国荣誉军团指挥官勋章（Commander of the Legion of Honour，frontmatter 明载）。
- 关键时间线（15–18 节点）：
  - 2010-12 Mohamed Bouazizi 在 Sidi Bouzid 自焚，茉莉花革命爆发（背景）
  - 2011 Ben Ali 出走；制宪议会选举，Ennahda 领衔的 Troika（Ennahda+CPR+Ettakatol）执政
  - 2012-06-18 UGTT 发起「政治倡议」呼吁全国和解
  - 2012-10 四组织首次会商（Ennahda 与 CPR 缺席）
  - 2013-01-14 UGTT 与 UTICA 签署「社会契约」
  - 2013-02-06 反对派领导人 Chokri Belaid 遇刺
  - 2013-07-25 反对派领导人 Mohamed Brahmi 遇刺，多个反对党退出制宪会议
  - 2013-08-06 制宪会议主席 Moustapha Ben Jaafar 中止全部立法程序
  - 2013 夏 四方机制成型；UGTT 号召两日大罢工
  - 2013-10-25 第三次全国对话大会召开，24 个受邀政党中 21 个签署「路线图」
  - 2014-01 制宪会议通过新宪法；Mehdi Jomaa 出任看守总理
  - 2014-10-26 议会选举 Nidaa Tounes 获相对多数；2014-11-24 Essebsi 赢得总统选举
  - 2015-10-09 获 2015 诺贝尔和平奖
  - 2015-06 总理 Habib Essid 设立政府—UGTT—UTICA 三方「全国社会对话委员会」
  - 2016 四方机制在维也纳 OSCE 合影（页面 infobox 图）
  - 2025-07 四方机制提名联合国巴勒斯坦被占领土特别报告员 Francesca Albanese 竞逐诺贝尔和平奖
- 核心事业清单：
  1. 2013 政治危机中搭建全国对话平台，促成执政联盟与反对派坐到谈判桌
  2. 推动 2014 宪法的完成、通过与批准
  3. 确立技术官僚看守政府与选举时间表
  4. 维护公民社会在转型中的中介地位（罢工权、结社权写入宪法）

### 第 1 步：建立目录 【模板通用】

- 确认 `peace/presentations/21th_century/Tunisian_National_Dialogue_Quartet/` 目录与 `images/` 子目录。

### 第 2 步：复制 Makefile 【模板通用】

- 复制同世纪已完工篇目的 Makefile，设 `MAIN=Tunisian_National_Dialogue_Quartet_zh`、`VIDEO_NAME` 同名。

### 第 3 步：收集图片 【人物专属】

- page.md infobox 有四方领导人在维也纳 OSCE 的合影（2016），可用作插图；无机构徽标时用四方支柱几何母题装饰占位。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | national dialogue | 全国对话 | 四方机制的核心运作方式 | 对话页 |
| 1 | democratic transition | 民主转型 | 茉莉花革命后的宪政巩固 | 转型页 |
| 2 | conflict mediation | 冲突调解 | 政治危机斡旋、避免内战 | 危机页 |
| 3 | constitutional reform | 宪法改革 | 2014 宪法的促成 | 宪法页 |
| 4 | civil society | 公民社会 | 四组织的联合行动 | 成员页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| other | Tunisian General Labour Union | 无向 | 四大成员组织之一（UGTT） |
| other | Tunisian Confederation of Industry, Trade and Handicrafts | 无向 | 四大成员组织之一（UTICA） |
| other | Tunisian Human Rights League | 无向 | 四大成员组织之一（LTDH） |
| other | Tunisian Order of Lawyers | 无向 | 四大成员组织之一（全国律师公会） |
| colleague | Houcine Abassi | 无向 | UGTT 总书记，四方关键领导人，推动对话在关键节点前行 |
| colleague | Wided Bouchamaoui | 无向 | UTICA 主席，四方关键领导人 |
| colleague | Abdessattar Ben Moussa | 无向 | 突尼斯人权联盟主席，四方关键领导人 |
| colleague | Fadhel Mahfoudh | 无向 | 突尼斯律师公会主席，四方关键领导人 |

- 入库操作：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Tunisian_National_Dialogue_Quartet.yaml`

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：地中海红土色沉厚 + 香槟金；主色 `#8C1515`（manifest 预分配，勿改）+ 诺奖香槟金 `#C9A227` + 四分类色：
  - `badgeUGTT` 工会 — 砖红 `#8C1515`
  - `badgeUTICA` 商界 — 钢青 `#37474F`
  - `badgeLTDH` 人权 — 深绿 `#1B5E20`
  - `badgeLaw` 律师 — 靛蓝 `#283593`
- **背景母题**：四根立柱几何元素 + 橄榄枝细线，呼应「四方会盟」。

### 第 6 步：规划幻灯片序列 【人物专属，机构概览页替代身份信息页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 2015 诺贝尔和平奖 / Tunisian National Dialogue Quartet + 四色 badge + 四支柱母题
02  机构概览页（★ 必做）— 四大成员组织网格 + 成立背景 + 目标与结果 + 主要荣誉
03  背景：茉莉花革命 (2010–2011) — Bouazizi、Ben Ali 出走、Troika 执政
04  危机酝酿 (2012–2013) — 宪法进程停滞、Belaid 与 Brahmi 遇刺、制宪会议停摆
05  四方成型 (2013 夏) — UGTT 倡议、UGTT–UTICA 社会契约、四组织联合
06  全国对话 (2013-10) — 21/24 党签署路线图、四大目标
07  成果：2014 宪法与选举 — 技术官僚看守政府、议会与总统选举
08  2015 诺贝尔和平奖 — 官方理由全文、委员会主席 Kaci Kullmann Five 评语
09  四方领导人 — Abassi / Bouchamaoui / Ben Moussa / Mahfoudh
10  制度遗产 — 罢工权与结社权入宪、第 125 条反腐败机构、三方社会对话委员会
11  争议与评价 — 工联派批评、IMF 条件性贷款、精英技术官僚转型的学界讨论（客观并陈）
12  遗产：公民社会的示范 — 诺奖委员会期望突尼斯成为转型范例
13  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式硬要求：封面右上插 OSCE 合影（draw=coveraccent!50 细边框）+ 机构名小字注；机构概览页四成员组织用 2×2 网格 + 各自分类色顶边条；里程碑页时间线用 \foreach（分隔符必须 ASCII 逗号）；引语框用 tcolorbox 单框单引语；每页写完即编译，vbox 溢出 ≤10pt、hbox ≤50pt。
- 表格页预算：四领导人对照表 4 行 + arraystretch 0.62 + 顶部 −0.35cm；若加公式/引语框则再压 −0.2cm。

**Quartet 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 2015 独得 | 四方机制独享 2015 和平奖，无共享得主，勿造 co-honored |
| 机构条目 | is_org=true：yaml 省 gender/nationalities，birth_date 用 '2013'（仅到年，勿编造月日） |
| 勿把领导人写成创始人 | 四方领导人只是成员组织负责人，机构由四组织联合组建，勿写「创始人」关系 |
| 成员组织是「成员」非「前身」 | 用 type: other 注明「四大成员组织之一」，勿用 founder |
| Bouchamaoui 拼写 | page.md 混用 Wided/Ouided 两种拼法，yaml 对手方统一用 Wided Bouchamaoui |
| 政治红线 | Ennahda 与世俗派的教俗对立、遇刺案、IMF 争议一律按 page.md 客观记录，不作立场表述；2025 提名 Francesca Albanese 只写事实一句 |
| 引语红线 | 引语框仅收 page.md 载英文原文的语句（Kaci Kullmann Five 评语、Essebsi/Omri 等已译语句慎用）；四方获奖演讲引文用页面所载英译 |
| 缩写 | UGTT/UTICA/LTDH 首次出现给全称；UTICA 全称是工商业手工业联合会，勿简写为「工业联盟」 |
| 批评节 | Critiques 节（工会立场、IMF 贷款、精英转型）须两说并陈，勿单侧叙事 |
| 成立日期 | infobox 作 August 2013–January 2014，正文作「2013 年夏」，提示词与 yaml 统一取 2013 年 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Jasmine Revolution | 茉莉花革命 | 2010–2011 突尼斯革命 |
| UGTT | 突尼斯总工会 | Union Générale Tunisienne du Travail |
| UTICA | 突尼斯工商业手工业联合会 | 雇主组织 |
| LTDH | 突尼斯人权联盟 | La Ligue Tunisienne pour la Défense des Droits de l'Homme |
| Troika | 三党执政联盟 | Ennahda+CPR+Ettakatol，勿与俄乌「三驾马车」混淆 |
| roadmap | 路线图 | 2013-10 全国对话纲领 |
| Constituent Assembly | 制宪议会 | 2011 选出 |
| pacted transition | 协定式转型 | 政治学术语，客观引述 |
| irhal | 「离开」 | 阿拉伯语抗议口号 |
| Mehdi Jomaa | 迈赫迪·朱马 | 看守总理 |
| National Salvation Front | 全国救亡阵线 | 世俗派反对联盟 |
| Moustapha Ben Jaafar | 穆斯塔法·本·贾法尔 | 制宪会议主席，2013-08-06 中止立法 |
| Nidaa Tounes | 呼唤突尼斯党 | 2014 议会选举相对多数 |

### 第 9 步：史实审查 + 术语审查 【人物专属】

- 核对官方理由与名录逐字一致；确认四个成员组织英文名与 page.md 一致；确认无任何评价性政治语句。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配，勿改）
- **风格**：辽阔 / 深沉 / 纪录片
- **匹配理由**：从革命惊涛到对话上岸的「渡海」意象，匹配机构在国家危机中稳住航向的集体叙事。
- **本地路径**：`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Tunisian_National_Dialogue_Quartet/page.md` | 本地 Wikipedia 事实基准 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译照抄 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **执行顺序**：提示词 → yaml → seed_person.py 入库 → 验证（has_social_data=1、fields≥4、relations≥2）。
