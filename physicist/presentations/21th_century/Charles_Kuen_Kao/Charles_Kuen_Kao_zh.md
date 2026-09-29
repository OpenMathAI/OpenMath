# 物理学家立传提示词（Charles Kuen Kao 高锟）

> **OpenPhysicist 21 世纪批次**人物专属立传提示词。以 Kenneth_G_Wilson_zh.md 为结构母本（0–11 节），
> 本文件为 Charles Kuen Kao（2009 诺贝尔物理学奖，光纤通信）定制。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir Charles Kuen Kao（高锟，1933-11-04 ~ 2018-09-23，享年 84 岁）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Charles Kuen Kao（高錕/高锟，1933-11-04 生于上海 ~ 2018-09-23 逝于香港沙田），爵士（2010 KBE）、GBM、FRS、FREng
- **气质关键词**：**光纤之父、宽带的教父、被不相信照亮的人** —— 2009 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for groundbreaking achievements concerning the transmission of light in fibres for optical communication"（关于光在光纤中传输用于光通信的开创性成就；独得 1/2 奖金）
- **设计母题**：**光在细如发丝的玻璃中穿行**。一束激光沿发丝细玻璃纤维传播的视觉——可用「暗背景中一束亮色折线贯穿全页」的视觉语言，呼应 20 dB/km 阈值与超透明玻璃。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Charles_Kuen_Kao/page.md`（已有本地）
- **待下载**：`Charles_Kuen_Kao.html` 与 `images/` 待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Charles_Kuen_Kao`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，page.md 已核对】

- 生卒：1933-11-04 生于上海（上海法租界，本名 Kao Kuen）~ 2018-09-23 逝于香港沙田 Bradbury Hospice（末期失智症，享年 84 岁）。
- 国籍/居留：香港永久居民；英国与美国公民（frontmatter 国籍序列 Republic of China / United Kingdom / United States / British Hong Kong）；2010 夫妇公开信自述「香港属于我」（a Hong Kong belonger）。
- 家庭：父高君湘（Kao Chun-Hsiang）1925 年密歇根大学法学院 JD，上海会审公廨法官、东吴大学比较法学院教授；祖父高（Kao Hsieh）学者诗人画家；父亲的堂弟为天文学家高平子（Kao Ping-tse，月球环形山 Kao 以其命名）；弟高鋙（Timothy Wu Kao）土木工程学者；作家高（Gao Xu）、姚光等亦为近亲。
- 教育：上海家中读中文经典 + 上海世界学校（蔡元培等创办）学英文法文；1949 举家定居香港；圣若瑟书院 5 年、1952 毕业；港大会考高分但港大无电机工程，1953 赴伦敦，1955 A-Level；Woolwich Polytechnic（今格林威治大学）1957 B.Sc.；在 STL 工作同时在 UCL 攻博，1965 电机工程 PhD，论文《Waveguides for millimetric and submillimetric electromagnetic waves》。
- 博士导师：Harold Barlow（UCL，page.md 明载）。
- 博士后：page.md 无载。
- 任职机构：
  - Standard Telecommunication Laboratories（STL，STC 研究中心，英国 Harlow）：1960 年代入职光通信组，1963 加入光通信研究、同年任 STL 电光学研究组负责人；1964-12 接掌 STL 光通信计划（Karbowiak 赴 UNSW 后）
  - 1966-01 向 IEE 报告、1966-07 与 Hockham 发表光纤通信奠基论文
  - 1970 香港中文大学创系（电子学系，后电子工程系），Reader → 讲座教授
  - 1974 回美国 ITT（STC 母公司，Roanoke, Virginia）：Chief Scientist → Director of Engineering
  - 1982 首任 ITT Executive Scientist（常驻康涅狄格先进技术中心）；兼任耶鲁大学兼职教授、Trumbull College Fellow
  - 1985 西德 SEL 研究中心一年；1986 ITT Corporate Director of Research
  - 1987–1996 香港中文大学副校长（Vice-Chancellor）
  - 1997–2002 帝国理工 London 电子工程系访问教授
  - 2000 联合创办 Independent Schools Foundation Academy 并任创校主席（至 2008-12）
  - 晚年 Transtech Services 主席兼 CEO、ITX Services 创办人
- 关键荣誉（Awards 表精选）：Stuart Ballantine Medal 1977；Rank Prize for Optoelectronics 1978（与 Hockham 等）；IEEE Liebmann Award 1978；Marconi Prize 1985；IEEE Bell Medal 1985；C&C Prize 1987；Faraday Medal 1989；APS 国际新材料奖 1989（与 MacChesney/Maurer 共享）；SPIE 金奖 1992；CBE 1993；Japan Prize 1996；Prince Philip Medal 1996；Charles Stark Draper Prize 1999；小行星 3463 Kaokuen 1996 命名；诺贝尔物理学奖 2009（独得 1/2）；KBE 2010；大紫荆勋章 2010；FRS 1997、美国工程院院士 1990、中研院院士 1992；Asian of the Century 1999（科技类）。
- 知名学生：page.md 无载（禁写）。
- 核心贡献清单：
  1. 1966 年与 Hockham 论文《Dielectric-fibre surface waveguides for optical frequencies》——提出玻璃纤维用于光通信；
  2. 证明既有光纤高损耗源于玻璃杂质而非技术本身（当时普遍归咎散射等基本物理效应）；
  3. 1965/1966 断定玻璃光衰减基本极限低于 20 dB/km（当时实际光纤高达 1000 dB/km）；
  4. 指出高纯度熔融石英（SiO2）是长距离光通信理想材料，引发全球高纯玻璃纤维研究生产；1969 与 Jones 实测石英本体损耗 4 dB/km——首证超透明玻璃；
  5. 坚定主张单模光纤用于长距离通信，日后成为几乎唯一方案；预言并推动海底光缆（1983 预言，五年后成真）；
  6. 首任 ITT Executive Scientist，发起 Terabit Technology 计划——「太比特技术概念之父」；100+ 论文、30+ 专利（含与 Maklad 的防水高强度纤维）。
- 关键时间线（18 节点）：
  1. 1933-11-04 生于上海法租界
  2. 童年：家塾读中文经典，上海世界学校学英法文
  3. 1949 举家定居香港
  4. 1952 圣若瑟书院毕业
  5. 1953 赴伦敦；1955 A-Level
  6. 1957 Woolwich Polytechnic B.Sc.
  7. 入职 STC 标准电信实验室（STL，Harlow）
  8. 1959 与 Gwen Wong May-Wun 在伦敦结婚（STC 工程师同事）
  9. 1963 加入光通信研究组、任电光学组负责人
  10. 1964-12 Karbowiak 离任，接掌 STL 光通信计划
  11. 1965 UCL PhD（导师 Harold Barlow，波导论文）
  12. 1966-01 IEE 报告；1966-07 与 Hockham 发表奠基论文，20 dB/km 阈值
  13. 1966 春赴美未说服 Bell Labs，转赴日本获支持
  14. 1969 与 Jones 实测石英本体损耗 4 dB/km
  15. 1970 中大创电子学系；1974 回 ITT（Roanoke）
  16. 1982 首任 ITT Executive Scientist；1983 预言海底光缆
  17. 1987–1996 中大副校长；1999 Draper 奖
  18. 2009-10-06 获诺贝尔物理学奖（"I am absolutely speechless"）；2010 封爵 + 大紫荆；2010 创立高锟慈善基金（阿尔茨海默病）
  19. 2004 起患阿尔茨海默病；2018-09-23 逝于香港沙田
  20. 2021-11-04 Google Doodle 庆其 88 岁冥诞（二进制拼出 KAO）

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Charles_Kuen_Kao/` 与 `images/`；Makefile 设 `MAIN=Charles_Kuen_Kao_zh`、`VIDEO_NAME=Charles_Kuen_Kao_zh`。
- 肖像：Wikipedia infobox 有 2004 年照片（Commons `Charles Kao 2004.jpg` 一类）；404 则用装饰圆占位。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | fibre optics | 光纤 | 「光纤之父」的领域本体 | 封面、核心页 |
| 1 | optical communication | 光通信 | 1966 奠基论文主题 | 核心页 |
| 2 | electrical engineering | 电气工程 | 本科与 PhD 专业、infobox Fields | 身份页 |
| 3 | telecommunications | 电信 | 光纤取代铜线的产业变革 | 产业页 |
| 4 | waveguide | 波导 | 博士论文与毫米波/亚毫米波研究 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Harold Barlow | 师→生（博士导师） | UCL 电机工程博士导师（1965），波导论文 |
| colleague | George Hockham | 无向 | STL 同事，1966 年光纤通信奠基论文合作者 |
| colleague | Antoni E. Karbowiak | 无向 | STL 光通信组上司，1964 离任后高锟接掌光通信计划 |
| co-honored | Willard S. Boyle | 无向 | 2009 诺贝尔物理学奖（高锟独得 1/2，Boyle 与 Smith 共享另一半） |
| co-honored | George E. Smith | 无向 | 2009 诺贝尔物理学奖（高锟独得 1/2，Boyle 与 Smith 共享另一半） |
| spouse | Gwen Wong May-Wun | 无向 | 1959 年伦敦结婚，STC 工程师同事相识，育一子一女 |

> 无载禁写：Alec Reeves（Karbowiak 的上司，与高锟无直接关系叙述）；家族成员（父高君湘/祖父高/高平子/高鋙，逸闻不入库）；MacChesney/Maurer 仅 1989 材料奖共享方（可于荣誉页注记，关系库不建）；学生（页面未载）。

### 第 5 步：配色方案 【人物专属】

- **气质**：清澈、贯通、东酉交融
- **主色**：光纤青绿 `#0E7C7B`（玻璃中穿行的光）+ 诺奖香槟金 `C9A227`
  - `badgeFibre` 光纤通信 — 深青 `#0A5555`
  - `badgeCUHK` 中大岁月 — 深紫 `#5B2A86`
  - `badgeIndustry` ITT/STL 产业 — 琥珀 `#C87F2F`
  - `badgeHonor` 爵衔勋章 — 深红 `#8C1F28`
- **背景母题**：暗色背景中一条贯穿全页的亮青色折线（光在光纤中的全反射折线），端点缀以香槟金光点。

### 第 6 步：幻灯片序列（10–16 页规划）【人物专属】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 光纤之父 / Sir Charles K. Kao 1933–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/出生地/师承/任职/荣誉/核心领域）
03  核心贡献概览 — 杂质理论 / 20 dB/km / 石英 / 单模与海底光缆
04  上海·香港·伦敦 (1933–1957) — 法租界、圣若瑟、Woolwich
05  STL 岁月：Karbowiak 之后 (1957–1965) — 电光学组、接掌光通信
06  1966 奠基论文（核心贡献页，公式框放衰减阈值示意/波导概念图式并注明）
07  被不相信的人 — Bell Labs 碰壁、日本获支持、1969 4 dB/km 实测
08  单模的远见与海底光缆 — 1983 预言五年后成真
09  中大与 ITT 双线 (1970–1986) — 创系、Executive Scientist、Terabit
10  副校长时代 (1987–1996) — 中大、ISF 创校
11  荣誉长廊 — Draper 1999 · Nobel 2009 · KBE/GBM 2010 · Kaokuen 小行星
12  高锟慈善基金与晚年 — 阿尔茨海默病抗争、2018 沙田辞世
13  遗产：互联网的玻璃脊柱 — Harlow 博物馆评语、Google Doodle
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 得奖份额 | 2009 年高锟**独得 1/2**，Boyle 与 Smith 共享另一半（CCD）；勿写成「三人平分」 |
| 获奖理由 | 官方措辞 "groundbreaking achievements concerning the transmission of light in fibres for optical communication"；勿改写成 "inventing optical fiber" |
| 名字 | 中文简体高锟/繁体高錕，本名 Kao Kuen；英文 Sir Charles K. Kao（2010 封爵）；勿与其他 Kao 混淆 |
| 国籍口径 | 香港永久居民 + 英美双籍；frontmatter 另有 Republic of China / British Hong Kong 出生与居留口径——行文写「生于上海、定居香港、英美公民」即可，勿单一化 |
| Hockham 分工 | 高锟主攻材料光损耗，Hockham 研究纤维不连续性与弯曲损耗（Notes 2）；论文 1966-01 报告、1966-07 发表 |
| Karbowiak | 是 STL 光通信组上司（1964 赴 UNSW 后高锟接任），非博士导师；博士导师是 UCL 的 Harold Barlow，勿混 |
| 20 dB/km | 关键阈值是「低于 20 dB/km」；当时实际光纤损耗高达 1000 dB/km，勿把两数字写反 |
| 归属 | 高损耗主因是杂质而非散射（当时许多物理学家误以为基本效应所致）——这是高锟的核心洞见，勿写成「共同结论」 |
| 奖项共享注记 | Rank Prize 1978 与 Hockham 共享；APS 国际新材料奖 1989 与 MacChesney/Maurer 共享（Notes 4/5）；引用奖项时注明 |
| 政治敏感 | page.md 涉 1949 迁港、香港事务顾问（1994–1997）等表述——立传按 0 步事实基准客观一句话带过，不展开评述 |
| 病史 | 阿尔茨海默病 2004 年起（其父同病）；2010 创立 Charles K. Kao Foundation；诺奖奖金主要用于其医疗开支（其妻语）——客观记录，勿煽情 |
| 家族 | 父/祖父/高平子/高鋙 仅作轶事素材，不入社会关系库 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| optical fibre / fiber | 光纤 | 英式 fibre 为主，引用奖项保持原文拼写 |
| attenuation | 衰减 | dB/km 计量 |
| fused silica | 熔融石英 | SiO2，理想通信材料 |
| single-mode fiber | 单模光纤 | 高锟的坚持，勿写多模 |
| 20 dB/km | 每公里 20 分贝 | 关键阈值 |
| waveguide | 波导 | 博士论文主题 |
| STL | 标准电信实验室 | STC 的 Harlow 研究中心，勿与 Bell Labs 混淆 |
| submarine cable | 海底光缆 | 1983 预言 |
| Vice-Chancellor | 校长（中大） | 港制副校长=行政首长，勿误译「副校监」 |
| Alzheimer's disease | 阿尔茨海默病 | 2004 起 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（史诗/美丽/振奋）
- **匹配理由**：「如日之光」直接呼应光纤把光送入千家万户的主题——从被不相信到点亮世界；史诗/振奋基调匹配 1966 论文→全球产业变革→2009 诺奖的弧线，美丽段落贴合其清澈温润的气质。
- **备选**：New Lands（开阔/时代转折）、Eternals（长期影响）。
- 批内不重复：本批 Kobayashi=The Invisible Light、Maskawa=Cinematic Experience、Boyle=Daylight、Smith=Ascension。

---

## 五、执行红线 【模板通用】

- 只收 page.md 明载的关系；yaml note 含 ": " 或以引号开头时整体单引号包裹。
- 对手方入库用规范名：Harold Barlow、George Hockham、Antoni E. Karbowiak、Willard S. Boyle、George E. Smith、Gwen Wong May-Wun；不给对手方编造 qid。
- 禁止修改 generate_21st_century_list.py、名录 md、模板文件。
