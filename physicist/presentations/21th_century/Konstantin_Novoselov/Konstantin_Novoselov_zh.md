# 物理学家立传提示词（Konstantin Novoselov / 康斯坦丁·诺沃肖洛夫）

> **OpenPhysicist 21 世纪批次 · batch 6-2**。本文件为 Konstantin Novoselov（2010 诺贝尔物理学奖，石墨烯共同发现者）的人物专属立传提示词，结构对齐标杆 `Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir Konstantin Sergeevich Novoselov（康斯坦丁·谢尔盖耶维奇·诺沃肖洛夫，昵称 Kostya），2010 诺贝尔物理学奖得主（与 Andre Geim 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与研究领域结构化表达；Novoselov 篇另需突出「最年轻诺奖得主之一 + 科学与艺术跨界」的双重气质。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Konstantin Novoselov（1974-08-23 生于苏联下塔吉尔，在世）
- **气质关键词**：**石墨烯联合发现者、最年轻的当代物理学诺奖得主、艺术家型科学家** —— 2010 诺贝尔物理学奖官方获奖理由：
  > "For groundbreaking experiments regarding the two-dimensional material graphene"（因 regarding 二维材料石墨烯的开创性实验）
- **设计母题**：**二维与立体的对话（2D/3D）**。从原子级二维平面到三维艺术创作，Novoselov 的世界在维度之间穿行——石墨烯是纸，世界是画布。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Konstantin_Novoselov/page.md`（**page.md 已有本地**）
- **待下载**：`Konstantin_Novoselov.html` 与 `images/`（第 0 步执行）；Wikipedia URL：`https://en.wikipedia.org/wiki/Konstantin_Novoselov`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地；❌ html 与 images/ 待下载（Wikipedia URL 见上）
- 事实基准（以 page.md 为准）：
  - 生卒：1974-08-23 生于下塔吉尔（苏联俄罗斯苏维埃联邦），在世；昵称 Kostya
  - 国籍：苏联 → 俄罗斯 + 英国双重
  - 教育：莫斯科物理技术学院（MIPT）MSc 1997；奈梅亨大学 PhD 2004（导师 Andre Geim），论文《Development and Applications of Mesoscopic Hall Microprobes》
  - 博士导师（frontmatter 明载两位）：Andre Geim、Jan Kees Maan
  - 任职：曼彻斯特大学（Langworthy Professor，2013 受聘；2012 接棒 Geim 的讲席）→ 国家石墨烯研究所首任所长 → 2019 加入新加坡国立大学先进二维材料中心（首位加入新加坡大学的诺奖得主）→ Constructor University（不来梅）校长
  - 关键荣誉：Nicholas Kurti Prize 2007；TR35 2008；EPS Europhysics Prize 2008（与 Geim 共享）；IUPAP Young Scientist Prize 2008；Nobel 2010；荷兰狮骑士指挥官 2010；FRS 2011；Knight Bachelor 2012；Leverhulme Medal 2013；Onsager Medal 2014；Carbon Medal 2016；Dalton Medal 2016；美国科学院外籍院士 2019；Otto Warburg Prize 2019；von Neumann Professor 2022；中国科学院外籍院士 2023；EPFL Fellow 2026
  - 年龄纪录：2010 获奖时是 1973 年 Brian Josephson 之后最年轻的物理学诺奖得主
  - 配偶：Irina Barbolina（妻子，两个女儿）
- 关键时间线（18 节点）：

| 时间 | 事件 |
|------|------|
| 1974-08-23 | 生于苏联下塔吉尔 |
| 1997 | MIPT 获 MSc |
| 1997–2004 | 奈梅亨读博（Geim 与 Maan 门下），介观 Hall 微探针 |
| 2004 | PhD（奈梅亨）；石墨烯论文发表于 Science |
| 2007 | Nicholas Kurti European Science Prize |
| 2008 | TR35；与 Geim 共享 Europhysics Prize；IUPAP Young Scientist Prize；曼大年度研究者 |
| 2010-10-05 | 诺贝尔物理学奖；荷兰狮骑士指挥官 |
| 2010 | HonFRSC；MIPT 名誉教授 |
| 2011 | 当选 FRS；W. L. Bragg Lecture Prize；曼大荣誉博士 |
| 2012 | Knight Bachelor 爵士；接棒 Geim 的 Langworthy 讲席 |
| 2013 | 正式受聘 Langworthy Professor；Leverhulme Medal；曼大城市荣誉自由 |
| 2014 | Onsager Medal；高被引研究者 |
| 2015 | Academia Europaea 院士；Whitworth 美术馆与 Cornelia Parker 合作 |
| 2016 | Carbon Medal；Dalton Medal |
| 2019 | 加入新加坡国立大学；美国科学院外籍院士 |
| 2021 | 与 Castro Neto 共建 IFIM 中心（2 亿新元/10 年） |
| 2022–2023 | von Neumann Professor 2022；中科院外籍院士 2023；蒙古科学院 Kublai Khan Medal |
| 2024–2026 | IOM3 白金奖章 2024（与 Geim 共享）；EPFL Fellow 2026 |

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Konstantin_Novoselov/` 与 `images/` 子目录（提示词文件已就位）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，仅改 `MAIN=Konstantin_Novoselov_zh`、`VIDEO_NAME=Konstantin_Novoselov_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像为 2013 年照片；优先 Wikipedia REST API `page/summary` 查 infobox 原图名后经 Special:FilePath 下载 500px 到 `images/`
- 下载后 `file` 验证格式（JFIF density 异常需 sips 改 72dpi）；404 则用装饰圆占位并在提示词补记
- 插图可选：`Konstantin_Novoselov_in_lab.jpg`（实验室照）与 `Konstantin_Novoselov_Chinese_painting_2015.jpg`（艺术页用）

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | graphene | 石墨烯 | 2004 Science 论文，2010 诺奖核心 | 核心页 |
| 1 | two-dimensional materials | 二维材料 | 异质结构、其他二维晶体 | 遗产页 |
| 2 | condensed matter physics | 凝聚态物理 | infobox Fields 固体物理大类 | 领域页 |
| 3 | mesoscopic physics | 介观物理 | 博士论文 Hall 微探针 | 早年页 |
| 4 | functional intelligent materials | 功能智能材料 | 2021 新加坡 IFIM 中心方向 | 新篇页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致，只收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Andre Geim | 师→生（博士导师） | 奈梅亨博士导师，2010 诺奖共同得主 |
| advisor-student | Jan Kees Maan | 师→生（博士导师） | frontmatter 明载的另一位博士导师 |
| spouse | Irina Barbolina | 无向 | 妻子 |
| co-honored | Andre Geim | 无向 | 2010 诺贝尔物理学奖共同得主，2008 Europhysics Prize 共同得主 |
| colleague | Antonio H. Castro Neto | 无向 | 2021 在新加坡国立大学共同创建 IFIM 研究中心 |

### 第 5 步：设计配色方案

- **气质**：年轻、跨界、二维之美
- **主色**：深湖蓝 `#1E4E79`（批内唯一）+ 诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeGraphene` 石墨烯 — 青绿 `#0E7C7B`
  - `badge2D` 二维材料 — 靛蓝 `#4C5FD5`
  - `badgeMeso` 介观物理 — 琥珀 `#E07B30`
  - `badgeArt` 艺术跨界 — 玫瑰 `#C4204F`
- **背景母题**：原子级蜂窝网格渐变 + 水墨笔触点缀（呼应其中国书画创作）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）、封面有国籍（底部状态栏三要素）。
2. 必须有身份信息页：左头像 + 右信息网格（生卒、本名、国籍、教育、师承、任职、荣誉、核心领域），事实取自 page.md，不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 石墨烯联合发现者 / Konstantin Novoselov 1974– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 石墨烯 / 二维异质结构 / Hall 微探针 / 智能材料
04  早年：下塔吉尔到莫斯科 (1974–1997) — MIPT MSc
05  奈梅亨读博 (1997–2004) — Geim 与 Maan 门下、Hall 微探针
06  石墨烯：2004 年那篇 Science（核心贡献页）
07  荣誉加速 (2007–2009) — Kurti/Europhysics/IUPAP/TR35
08  2010 诺贝尔奖 — Josephson 之后最年轻物理学得主
09  曼彻斯特与国家石墨烯研究所 — 首任所长、Langworthy 讲席
10  新篇：新加坡与 IFIM (2019– ) — NUS、功能智能材料
11  科学与艺术 — 中国书画、Whitworth 2015、威尼斯双年展
12  荣誉与认可 — FRS 2011 · Onsager 2014 · 中科院外籍院士 2023
13  遗产：二维材料时代
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 表格页负间距：顶部 −0.35cm、arraystretch 0.78–0.82；拥挤页 darkcode 可降字号。

| 陷阱 | 说明 |
|------|------|
| 政治敏感 | 「个人生活/政治立场」节内容（2022 俄罗斯科学家公开信、与外国政要相关的画作收藏记述）一律**禁写** |
| 博士导师 | frontmatter 明载两位：Andre Geim 与 Jan Kees Maan；正文第 38 行明示 PhD 由 Geim 监督——两人均入库 advisor，note 写清口径 |
| PhD 学校 | 2004 PhD 是**奈梅亨大学**（不是曼彻斯特）；曼彻斯特是 2001 年起的任职地 |
| 年龄纪录 | 「1973 年 Josephson 之后最年轻的物理学诺奖得主」按 page.md 口径写；勿自行扩展到"史上最年轻" |
| Langworthy 时间 | Geim 2007–2013 持有该讲席、2012 让位 Novoselov，Novoselov 2013 正式受聘——三个年份勿混 |
| Europhysics 归属 | 2008 Europhysics Prize 与 Geim **共享**，勿写独得 |
| 中科院院士 | 2023 当选**外籍**院士，勿漏"外籍" |
| 艺术材料 | 2015 Whitworth 展品石墨烯提取自 Blake 画作中的石墨——注意是"石墨→石墨烯"，不是从画上撕胶带 |
| 荣誉年份 | Warner 奖项无；Nicholas Kurti 2007 / IUPAP 2008 / Onsager 2014 / Dalton 2016 各归其年，勿串 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| graphene | 石墨烯 | 单原子层碳 |
| two-dimensional materials | 二维材料 | 含异质结构 |
| Hall microprobe | 霍尔微探针 | 博士论文工具 |
| mesoscopic | 介观 | 介于微观与宏观 |
| heterostructure | 异质结构 | 二维材料垂直堆叠 |
| Graphene Flagship | 石墨烯旗舰计划 | 欧盟 10 亿欧元项目 |
| Langworthy Professor | 兰沃西讲席教授 | 曼彻斯特捐赠讲席 |
| Onsager Medal | 昂萨格奖章 | 2014 |
| exfoliation | 机械剥离 | 胶带法的学名 |
| IFIM | 功能智能材料中心 | 2021 新加坡共建 |
| Constructor University | 构造者大学（不来梅） | 现任校长职务 |
| hot paper | 热点论文 | 2007–2009 多榜在列口径 |

---

## 四、背景音乐选择 【人物专属建议】

- **选定曲目**：**Expedition** — Alex-Productions（66k views，高受众 / 探索 / 史诗）
- **匹配理由**："远征"匹配其从下塔吉尔经莫斯科、奈梅亨、曼彻斯特到新加坡的地理与学术双重旅程；石墨烯发现本身就是对未知维度（二维世界）的探险；曲风年轻有推进感，匹配最年轻诺奖得主的锐气。
- **本地路径**：`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`
- **备选**：Daylight（明亮/轻快，匹配年轻气质）、Shine Like The Sun（振奋，匹配新星崛起）

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Konstantin_Novoselov/page.md` | 事实基准（唯一数据源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Konstantin_Novoselov.yaml` | 社会关系/领域入库（本批新建） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
