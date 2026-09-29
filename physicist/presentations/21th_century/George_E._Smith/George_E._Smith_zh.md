# 物理学家立传提示词（George E. Smith 乔治·史密斯）

> **OpenPhysicist 21 世纪批次**人物专属立传提示词。以 Kenneth_G_Wilson_zh.md 为结构母本（0–11 节），
> 本文件为 George E. Smith（2009 诺贝尔物理学奖，CCD 电荷耦合器件）定制。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：George Elwood Smith（乔治·埃尔伍德·史密斯，1930-05-10 ~ 2025-05-28，享年 95 岁）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：George Elwood Smith（1930-05-10 生于纽约州白原市 ~ 2025-05-28 逝于新泽西州巴内加特镇），美国应用物理学家
- **气质关键词**：**CCD 共同发明人、环球航海的发明家、贝尔实验室的专利大户** —— 2009 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the invention of an imaging semiconductor circuit - the CCD sensor"（发明成像半导体电路——CCD 传感器；与 Willard Boyle 共享 1/2 奖金）
- **设计母题**：**电荷的接力（charge transfer）**。CCD 的本质是电荷沿硅面逐位传递——可用「一排发光单元中亮点逐格移动」的视觉语言，与 Boyle 篇的「像素点亮」母题呼应但区分。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/George_E._Smith/page.md`（已有本地）
- **待下载**：`George_E._Smith.html` 与 `images/` 待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/George_E._Smith`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，page.md 已核对】

- 生卒：1930-05-10 生于纽约州白原市 ~ 2025-05-28 逝于新泽西州巴内加特镇家中（享年 95 岁）。
- 国籍：美国。
- 家庭/个人：退役后与生活伴侣 Janet 环球航海 17 年，2003 年为「免让老骨头再受风暴」收帆；定居新泽西州 Waretown（Ocean Township）；与 Boyle 同为狂热水手，多次同船远航。
- 教育：美国海军服役 4 年 + 迈阿密大学修课；1952 以插班二年级资格入宾夕法尼亚大学，1955 B.S.；芝加哥大学助教，1959 PhD，论文《The Anomalous Skin Effect in Bismuth》（铋中的反常趋肤效应）。
- 博士导师：Andrew Werner Lawson（芝加哥大学，infobox 明载；正文无更多叙述）。
- 博士后：page.md 无载。
- 任职机构：1959–1986 Bell Telephone Laboratories（Murray Hill, New Jersey）——领导新型激光器与半导体器件研究；获数十项专利；后任 VLSI 器件部门主管；1986 退休。
- 关键荣誉：Stuart Ballantine Medal 1973（与 Boyle 共享）；IEEE Liebmann Award 1974（与 Boyle 共享）；C&C Prize 1999；Edwin H. Land Medal 2001；Charles Stark Draper Prize 2006（与 Boyle 共享）；诺贝尔物理学奖 2009（与 Boyle 共享 1/2）；皇家摄影学会 Progress Medal 2015；伊丽莎白女王工程奖 2017（与 Eric Fossum、Nobukazu Teranishi、Michael Tompsett 共享）；美国工程院院士 1983；National Inventors Hall of Fame（frontmatter）。
- 知名学生：page.md 无载（禁写；工业实验室无博士生）。
- 核心贡献清单：
  1. 1969 与 Willard Boyle 发明电荷耦合器件（CCD）——成像半导体电路；
  2. Bell Labs 期间领导新型激光器与半导体器件研究，获数十项专利；
  3. 执掌 VLSI 器件部门——大规模集成电路时代的中坚；
  4. CCD 之名言："After making the first couple of imaging devices, we knew for certain that chemistry photography was dead."（引语出自 Boyle 篇转述，立传引用时注明语境）。
- 关键时间线（15 节点）：
  1. 1930-05-10 生于纽约州白原市
  2. 美国海军服役 4 年
  3. 迈阿密大学修课
  4. 1952 插班宾夕法尼亚大学二年级
  5. 1955 宾大 B.S.
  6. 芝加哥大学助教
  7. 1959 芝加哥大学 PhD（铋的反常趋肤效应，导师 Andrew Werner Lawson）
  8. 1959 入职 Bell Labs（Murray Hill）
  9. 领导新型激光器与半导体器件研究
  10. 1969 与 Boyle 发明 CCD
  11. 1973 Ballantine · 1974 Liebmann
  12. 执掌 VLSI 器件部门；1983 美国工程院院士
  13. 1986 自 Bell Labs 退休
  14. 退休后与 Janet 环球航海 17 年（2003 收帆）
  15. 1999 C&C · 2001 Land · 2006 Draper · 2015 Progress Medal · 2017 伊丽莎白女王工程奖
  16. 2009-10 诺贝尔物理学奖（与 Boyle 共享 1/2）
  17. 2025-05-28 逝于新泽西州巴内加特镇家中，享年 95 岁

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `George_E._Smith/` 与 `images/`；Makefile 设 `MAIN=George_E._Smith_zh`、`VIDEO_NAME=George_E._Smith_zh`。
- 肖像：Wikipedia infobox 有 2009 年照片；404 则用装饰圆占位。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | charge-coupled device | 电荷耦合器件（CCD） | 1969 共同发明，2009 诺奖核心 | 核心页 |
| 1 | physics | 物理学 | infobox Fields，应用物理 | 身份页 |
| 2 | semiconductor devices | 半导体器件 | Bell Labs 主研方向 | 生涯页 |
| 3 | image processing | 图像处理 | CCD 成像应用 | 应用页 |
| 4 | video technology | 视频技术 | field_of_work 明载 | 应用页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Andrew Werner Lawson | 师→生（博士导师） | 芝加哥大学博士导师（1959） |
| colleague | Willard S. Boyle | 无向 | Bell Labs 同事，1969 年 CCD 共同发明人，同好航海 |
| co-honored | Willard S. Boyle | 无向 | 2009 诺贝尔物理学奖共享 1/2 |
| co-honored | Charles Kuen Kao | 无向 | 2009 诺贝尔物理学奖另一半得主（光纤通信） |
| co-honored | Eric Fossum | 无向 | 2017 伊丽莎白女王工程奖共同得主（数码成像传感器） |
| co-honored | Nobukazu Teranishi | 无向 | 2017 伊丽莎白女王工程奖共同得主（数码成像传感器） |
| co-honored | Michael Francis Tompsett | 无向 | 2017 伊丽莎白女王工程奖共同得主（数码成像传感器） |

> 无载禁写：Janet 为「生活伴侣」（life partner）非配偶，不入 spouse；Don Nelson（红宝石激光是 Boyle 与 Nelson 之事，Smith 页面未载）；学生（页面未载）。

### 第 5 步：配色方案 【人物专属】

- **气质**：硬朗、航海、工程师本色
- **主色**：深红 `#7A1E28`（硅与信号）+ 诺奖香槟金 `C9A227`
  - `badgeCCD` CCD — 深青 `#0A5555`
  - `badgeBell` 贝尔实验室 — 靛蓝 `#2B3A67`
  - `badgeSail` 环球航海 — 海蓝 `#1F6F8B`
  - `badgeQEPrize` 女王工程奖 — 紫红 `#5B2A4D`
- **背景母题**：一排矩形感光单元中一枚亮点逐格移动（电荷转移），右下角以细线航迹呼应环球航海。

### 第 6 步：幻灯片序列（10–16 页规划）【人物专属】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — CCD 共同发明人 / George E. Smith 1930–2025 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/出生地/师承/任职/荣誉/核心领域）
03  核心贡献概览 — CCD / 半导体器件 / VLSI / 数十项专利
04  早年：白原市与海军 (1930–1952) — 服役 4 年、迈阿密修课
05  宾大与芝加哥 (1952–1959) — B.S.、反常趋肤效应 PhD
06  Bell Labs 三十年 (1959–1986) — 新型激光器、半导体器件、专利
07  1969：CCD 诞生（核心贡献页，公式框放 CCD 电荷转移概念图式并注明）
08  与 Boyle 的双人舞 — 同事、同船、共享半座诺奖
09  VLSI 部门与工程师本色 — 数十项专利
10  荣誉长廊 — Ballantine 1973 · Draper 2006 · Nobel 2009 · QEPrize 2017
11  收帆之后 — Janet、环球航海 17 年、"creaky bones"
12  遗产：从胶片到传感器 — 化学摄影的终结、数码成像时代
13  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 得奖份额 | Smith 与 Boyle **共享 1/2**，Kao 独得另 1/2；勿写成「三人平分」 |
| 获奖理由 | 官方措辞 "for the invention of an imaging semiconductor circuit - the CCD sensor"；勿写成 "inventing the digital camera" |
| 生卒 | 1930-05-10 ~ 2025-05-28（新泽西州巴内加特镇家中，享年 95）；2025 年辞世为新近事实，在世者禁写卒日的规则对本篇不适用，但勿写成 2024 |
| 博士导师 | infobox 作 Andrew Werner Lawson（芝加哥大学 1959）；论文《The Anomalous Skin Effect in Bismuth》；勿杜撰导师事迹 |
| 教育口径 | 宾大 1955 B.S.（1952 插班二年级）；芝加哥 1959 PhD 且任助教；中间有海军 4 年 + 迈阿密修课——年份链条勿错位 |
| 同名区分 | George E. Smith 勿与其他 Smith 混淆；Michael Tompsett 与 Boyle 篇作 Michael Francis Tompsett 为**同一人**（QEPrize 共同得主兼 CCD 争议方），关系库统一用 Michael Francis Tompsett |
| QEPrize | 2017 伊丽莎白女王工程奖与 Eric Fossum、Nobukazu Teranishi、Michael Tompsett 共享，获奖理由 "For their work on Digital Imaging Sensors"——四人共享，勿写成 Smith 独得 |
| 引语 | "chemistry photography was dead" 一语在 page.md 中出自 Boyle 篇的 Smith 转述——本篇引用需注明「Smith 语，转引自 Boyle 条目」语境，勿标成本页直引 |
| 航海伴侣 | Janet 是生活伴侣（life partner）非配偶——禁写 spouse；「与 Boyle 同为水手多次同行」可作轶事页 |
| 与 Boyle 分工 | page.md 未载二人分工细节（Boyle 页 Notes 有 Hockham 式分工注记，Smith 页无）——勿杜撰「Boyle 出想法、Smith 动手」之类说法 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| charge-coupled device (CCD) | 电荷耦合器件 | 1969 共同发明 |
| imaging semiconductor circuit | 成像半导体电路 | 诺奖理由原词 |
| anomalous skin effect | 反常趋肤效应 | PhD 主题，铋 |
| VLSI | 超大规模集成电路 | Smith 执掌其器件部门 |
| Murray Hill | 默里山 | Bell Labs 所在地 |
| Queen Elizabeth Prize for Engineering | 伊丽莎白女王工程奖 | 2017，四人共享 |
| Stuart Ballantine Medal | 巴兰坦奖章 | 1973，与 Boyle 共享 |
| Charles Stark Draper Prize | 德雷珀奖 | 2006，与 Boyle 共享 |
| Progress Medal | （皇家摄影学会）进步奖章 | 2015 |
| circumnavigation | 环球航海 | 退休后 17 年 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（科幻/史诗/上升）
- **匹配理由**：「上升」匹配其生涯弧线——海军水兵到 CCD 发明家再到诺贝尔奖；史诗感也贴合环球航海 17 年的自由叙事与 CCD 把人类视野送上太空的意象。
- **备选**：Expedition（探索感）、Daylight（明亮收束）。
- 批内不重复：本批 Kobayashi=The Invisible Light、Maskawa=Cinematic Experience、Kao=Shine Like The Sun、Boyle=Daylight。

---

## 五、执行红线 【模板通用】

- 只收 page.md 明载的关系；yaml note 含 ": " 或以引号开头时整体单引号包裹。
- 对手方入库用规范名：Andrew Werner Lawson、Willard S. Boyle（库内 id=3026 复用）、Charles Kuen Kao（库内 id=3022 复用）、Eric Fossum、Nobukazu Teranishi、Michael Francis Tompsett（沿用 Boyle 篇已建 stub 名）；不给对手方编造 qid。
- 禁止修改 generate_21st_century_list.py、名录 md、模板文件。
