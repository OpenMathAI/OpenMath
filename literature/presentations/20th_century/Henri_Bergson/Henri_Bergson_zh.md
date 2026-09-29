# 文学家立传提示词（OpenLiterature 实例：Henri Bergson）

> 本文件是 OpenLiterature 的「文学家立传提示词」人物专属实例，以 Henri Bergson（1927 诺贝尔文学奖，生命哲学大师）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；文学家适配：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 特殊口径：Bergson 是**获文学奖的哲学家**，领域表与叙事须兼顾哲学与文学两面，获奖理由表彰「思想的丰富生命力与阐述技巧」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Henri-Louis Bergson（亨利·柏格森）。
- **设计哲学**：保留「身份信息页」骨架；以**文学领域表**替代研究领域表、以**引文框/书影/意象图式**替代公式框。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Henri Bergson（1859-10-18 ~ 1941-01-04，享年 81 岁）
- **气质关键词**：**绵延的哲学、直觉的方法、法兰西公学院的万人讲席** —— 1927 诺贝尔文学奖获奖理由：
  > "in recognition of his rich and vitalizing ideas and the brilliant skill with which they have been presented"
  > （官方中译，照 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）：表彰其丰富而有生命力的思想，以及阐述这些思想的辉煌技巧
- **设计母题**：**绵延（durée）**。时间不是可切分的钟点，而是相互渗透、永不回头的流动之流——视觉语言用螺旋上升的水流/光带、层层扩散的同心涟漪，呼应「纯粹运动不可用静止概念捕捉」的核心思想。
- **本地数据源**：`literature/presentations/pages/20th_century/Henri_Bergson/page.md`（Wikipedia 全文，事实基准已核对）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Henri_Bergson
- **肖像**：第 0 步待下载（1927 年照，images.txt 有线索）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1859-10-18 生于巴黎（第二帝国，Rue Lamartine）～ 1941-01-04 逝于被占领巴黎（支气管炎；正文一处作 01-03，见陷阱表），享年 81 岁；葬于 Garches 墓园
- 国籍：法国（波兰裔犹太父亲 + 英/爱尔兰裔犹太母亲，幼年随家旅居伦敦数年，9 岁前归化法国）
- 家庭：父 Michał Bergson（波兰犹太裔作曲家/钢琴家）、母 Katherine Levison；妻 Louise Neuberger（1891 年结婚，Marcel Proust 任伴郎）；女儿 Jeanne（1896 年生，先天失聪）
- 教育：孔多塞中学（Lycée Fontanes，1868–1878）→ 巴黎高等师范学院（19 岁入学，期间读 Herbert Spencer）→ 1881 agrégation de philosophie → 巴黎大学博士 1889（法语论文《时间与自由意志》+ 拉丁论文 *Quid Aristoteles de loco senserit*）
- 博士导师：Paul Janet（infobox 明载）
- 任职：昂热中学（1881）→ 克莱蒙费朗（1883，其间出版 *Extraits de Lucrèce* 1884）→ 亨利四世中学（1888）→ 高师讲师/教授（1898）→ 法兰西公学院希腊罗马哲学讲席（1900）→ 1904 接替 Gabriel Tarde 任近代哲学讲席（至 1920 年免授课专心著述，讲席由弟子 Édouard Le Roy 代讲）
- 文学师承与影响（page.md 明载）：对 Spencer 机械进化论的批判是绵延理论的起点；深受 Kant 刺激；与 William James 互为知音；影响 Whitehead/Deleuze/Prigogine 等后世
- 关键荣誉：Nobel Literature 1927（因风湿病未赴斯德哥尔摩，致辞文本后收入 *La Pensée et le mouvant*）；道德与政治科学院院士 1901（后任主席）；法兰西学术院院士 1914（1918 正式就座，继 Emile Ollivier）；荣誉军团大十字 1930；牛津 DSc 1911、剑桥 DLitt 1920、美国艺术与科学院外籍荣誉院士 1928
- 核心作品与贡献（4–6 条）：
  1. *Time and Free Will*（*Essai sur les données immédiates de la conscience*，1889，博士论文）
  2. *Matter and Memory*（1896，知觉—记忆—身心关系）
  3. *Laughter*（*Le rire*，1900，"生命之上覆着机械"的笑论）
  4. *Creative Evolution*（*L'Évolution créatrice*，1907，élan vital；1918 年前已出 21 版）
  5. *Duration and Simultaneity*（1922，与爱因斯坦时间论战）
  6. *The Two Sources of Morality and Religion*（1932）与 *The Creative Mind*（*La Pensée et le mouvant*，1934）
- 关键时间线（15–20 节点）：
  1. 1859-10-18 生于巴黎
  2. 1868–1878 孔多塞中学；14–16 岁间因进化论失去宗教信仰
  3. 1877 18 岁解数学题，解法刊于 *Nouvelles Annales de Mathématiques*（首篇发表）
  4. 1879 入巴黎高师（在文科与理科间抉择，选文科）
  5. 1881 agrégation；赴昂热任教
  6. 1883 转克莱蒙费朗
  7. 1884 *Extraits de Lucrèce*（卢克莱修选注）
  8. 1888 回巴黎亨利四世中学
  9. 1889 巴黎大学博士（《时间与自由意志》）
  10. 1891 与 Louise Neuberger 结婚（Proust 任伴郎）
  11. 1896 《物质与记忆》
  12. 1898 高师讲师，同年升教授
  13. 1900 法兰西公学院希腊罗马哲学讲席；《笑》出版；首届国际哲学大会宣读论文
  14. 1901 道德与政治科学院院士
  15. 1904 接替 Tarde 任近代哲学讲席
  16. 1907 《创造进化论》——声望爆棚的转折点
  17. 1908 伦敦会 William James，成挚友；James 力荐于英语世界
  18. 1911 牛津演讲《变化的知觉》、伯明翰 Huxley 讲座；1913 访美（哥伦比亚大学）并任英国心灵研究会主席
  19. 1914 法兰西学术院院士；爱丁堡吉福德讲座（因战争只讲完第一系列）；三部著作被梵蒂冈列入禁书目录
  20. 1920–1925 任国联国际知识合作委员会主席（UNESCO 前身，委员含 Einstein 与 Marie Curie）；1922 《绵延与同时性》与爱因斯坦论战；1927 获诺奖；1932 《两个来源》；1937 遗嘱言向天主教之心；1940 拒绝维希豁免、警局登记；1941-01-04 卒

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Henri_Bergson/` 与 `images/`

### 第 2 步：复制 Makefile

- 设置 `MAIN=Henri_Bergson_zh`、`VIDEO_NAME=Henri_Bergson_zh`

### 第 3 步：收集图片

- 肖像：待下载（1927 年照）；备选：1917 与女儿 Jeanne 的 autochrome 彩照（page.md 有图）

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | metaphysics | 形而上学 | 直觉通往绝对的方法 | 核心页 |
| 1 | epistemology | 认识论 | 对康德—斯宾塞知识论的批判 | 方法页 |
| 2 | philosophy of life | 生命哲学 | élan vital 与创造进化 | 核心页 |
| 3 | process philosophy | 过程哲学 | 纯粹流动、新异性；影响 Whitehead | 遗产页 |
| 4 | philosophy of language | 语言哲学 | 概念之网 vs 隐喻表达 | 方法页 |

#### 4.1 入库操作（yaml 见 `MySQL/data/Henri_Bergson.yaml`）

- 新建 people 主记录（`name_en='Henri Bergson'`，qid=Q42156），`primary_occupation='writer'`、`has_social_data=1`
- 关联职业 philosopher(rank 0)/writer/professor；国籍 France
- 5 个领域写入 `person_field`；校验同标杆第 4 步

### 第 4.5 步：社会关系梳理 + 入库

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul Janet | 师→生 | 巴黎大学博士导师，infobox 明载 |
| advisor-student | Jean Wahl | 生 | 博士生，infobox 明载 |
| advisor-student | Émile Bréhier | 生 | 知名学生，infobox 明载 |
| advisor-student | Étienne Gilson | 生 | 知名学生，称其为「笛卡尔之后法国最伟大哲学家」 |
| advisor-student | Maurice Halbwachs | 生 | 知名学生，infobox 明载 |
| advisor-student | Vladimir Jankélévitch | 生 | 知名学生，1931 年著书论柏格森 |
| advisor-student | Alexandre Koyré | 生 | 知名学生，infobox 明载 |
| advisor-student | Gabriel Marcel | 生 | 知名学生，infobox 明载 |
| advisor-student | Jacques Maritain | 生 | 昔日门徒，后转托马斯主义并批判柏格森主义 |
| advisor-student | Roy Wood Sellars | 生 | 知名学生，infobox 明载 |
| influence | William James | 无向 | 1908 伦敦会面成挚友，James 力荐其哲学于英语世界 |
| influence | Édouard Le Roy | 无向 | 主要门徒，代讲其讲席并继任法兰西学术院席位 |
| influence | Gilles Deleuze | 无向 | 1966 年著 Le Bergsonisme 引发柏格森复兴 |
| influence | Nikos Kazantzakis | 无向 | 曾在巴黎师从听课，创作深受影响 |
| colleague | Gabriel Tarde | 无向 | 1904 年接替其法兰西公学院近代哲学讲席 |
| colleague | Marie Curie | 无向 | 国际知识合作委员会（1920-1925）共事 |
| controversy | Albert Einstein | 无向 | 1922 年关于时间本质的公开论战（Durée et simultanéité） |
| controversy | Bertrand Russell | 无向 | 1912 年发表 The Philosophy of Bergson 批评其数论与直觉主义 |
| spouse | Louise Neuberger | 无向 | 1891 年结婚，Marcel Proust 任伴郎 |

#### 4.5.1 入库操作

- 以 `name_en='Henri Bergson'` 为中心写入 `person_relation`；缺失人物建占位（不编造 qid；如 Bertrand Russell 库内已有记录则沿用）
- 同名区分：Paul Janet 为 19 世纪法国哲学家（非他人）；Gabriel Tarde 为社会学家/哲学家

### 第 5 步：设计配色方案

- **气质**：流动、澄澈、思辨之光
- **配色**：普鲁士紫蓝（主色，预分配 `#283593`）+ 香槟金 `C9A227` + 四分类色
  - `badgeA` metaphysics 形而上学 — 靛紫 `#5E35B1`
  - `badgeB` epistemology 认识论 — 青蓝 `#0277BD`
  - `badgeC` philosophy of life 生命哲学 — 生机绿 `#2E7D32`
  - `badgeD` process philosophy 过程哲学 — 琥珀 `#F57F17`

### 5.1 文学家格式硬要求

1. 封面有头像 + 细边框 + 姓名小字注。
2. 封面明示国籍；底部状态栏 `国籍 | 代表作 | 主要奖项`。
3. 必须有身份信息页（生卒、本名、国籍、出生地、师承、任职、荣誉、核心概念）。
4. 品牌口径 `OpenMathAI`；引号半角。
5. 无公式框——引文框用 James 1908 年书信与 1937 遗嘱原句（均有英文原文）。

### 第 6 步：规划幻灯片序列

```
00  OpenLiterature 项目首页
01  封面 — 绵延的哲学家 / Henri Bergson 1859–1941 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）
03  核心思想概览 — 绵延 / 直觉 / élan vital / 笑论
04  早年与高师 (1859–1881) — 数学解法处女作、文理抉择
05  博士论文：时间与自由意志 (1889) — 对 Kant 与 Spencer 的回应
06  物质与记忆 (1896) — 知觉与身心
07  法兰西公学院：万人讲席 (1900–1920) — Tarde 讲席、公共热潮与争议
08  创造进化论 (1907)（代表作书影 + 引文框）— 21 版神话
09  与 William James — 友谊与英语世界的桥
10  与 Einstein 论战 (1922) — 绵延 vs 物理时间
11  荣誉与诺奖 1927 — 因病未赴会、La Pensée et le mouvant
12  道德与宗教的两个来源 (1932) 与晚年
13  维希抉择 — 拒绝豁免、登记语引文框
14  遗产 — 从 Whitehead 到 Deleuze/Prigogine
15  结尾
```

### 第 7–8 步：编写源码与布局检查 【模板通用】

- 每页定义 `\newcommand{\xxxslide}`；写完即 `make` + `pdftoppm` 目检。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Bergson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日冲突 | 正文段落作 1941-01-03，infobox/frontmatter 作 1941-01-04；立传以 1941-01-04 为准并加注 |
| 生年双值 | frontmatter 另有 1859-01-01 噪声值，以 infobox 1859-10-18 为准 |
| 国籍口径 | 「法国哲学家」；波兰犹太裔父 + 英/爱裔母、幼年归化法国——勿写「波兰哲学家」 |
| 获文学奖的哲学家 | 获奖理由表彰思想及其呈现技巧，勿写「跨界获奖的意外」之类评价 |
| 与 Einstein | 1922 年是哲学立场之争（Merleau-Ponty 曾为 Bergson 辩护）；勿写「被科学打脸」或反向拔高 |
| 与 Russell | 1912 批评客观存在；controversy 关系 note 保持中性 |
| 禁书目录 | 1914 年三部著作入 Index——客观一句，不引申宗教评判 |
| 维希时期 | 放弃全部荣誉/职务不享反犹法豁免；登记语 "Academic. Philosopher. Nobel Prize winner. Jew." 有英文原文可引；遗嘱欲皈依天主教但不愿离开受迫害的犹太人——只按 page.md 客观简述，不作政治评价 |
| 讲席年代 | 1900 希腊罗马哲学讲席、1904 接 Tarde 近代哲学讲席、1920 起免授课（Le Roy 代讲）——三个年份勿混 |
| 女儿 | Jeanne 生于 1896、先天失聪——infobox 未列子女细节，仅正文一处，措辞从简 |
| ICC | 主席 1920–1925，是 UNESCO 前身机构；「创立 UNESCO」勿写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| duration (durée) | 绵延 | 非「持续时间」；不可切分的异质之流 |
| intuition | 直觉 | Bergson 专用义：回到事物本身的方法 |
| élan vital | 生命冲动 | 非「活力论」标签——他本人明确批评 vitalism |
| Creative Evolution | 《创造进化论》 | 1907 |
| Matter and Memory | 《物质与记忆》 | 1896 |
| Time and Free Will | 《时间与自由意志》 | 1889 博士论文 |
| The Two Sources of Morality and Religion | 《道德与宗教的两个来源》 | 1932 |
| mechanical encrusted on the living | 「机械镶嵌于生命之上」 | 笑论核心句 |

---

## 四、背景音乐选择 【预分配】

- **选定曲目**: **Eternals**
- **风格**: 宏大 / 深远 / 长期影响
- **匹配理由**:
  - "宏大/深远" 匹配绵延哲学的宇宙论气质——创造进化、生命冲动的整全视野
  - "长期影响" 匹配其遗产曲线——1920 年英语期刊被引第一的哲学家，沉寂半个世纪后经 Deleuze 复兴，Eternals 的「永恒回响」语义正合
  - 舒缓的推进感匹配法兰西公学院讲席四十年如一日的思想长征
- **本地路径**: 曲库对应曲目拷贝至 `literature/presentations/20th_century/Henri_Bergson/Eternals.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Henri_Bergson/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | 官方获奖理由中译 CITATION_ZH（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。最重要的事：事实只写 page.md 明载内容；争议关系（Einstein/Russell）保持中性措辞。**
