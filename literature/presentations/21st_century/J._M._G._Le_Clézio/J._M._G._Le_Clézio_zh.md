# 文学家立传提示词（J. M. G. Le Clézio · 2008 诺贝尔文学奖）

> **本文件是 OpenLiterature 21 世纪批次的「人物专属立传提示词」**，目标人物 Jean-Marie Gustave Le Clézio（让-马里·古斯塔夫·勒克莱齐奥）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–9 步骨架），内容适配文学家：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Jean-Marie Gustave Le Clézio（通称 J. M. G. Le Clézio），2008 年诺贝尔文学奖得主，法毛双重国籍的「游牧书写者」。
- **设计哲学**：文学家立传以「作品与意象」代替「定理与公式」——身份信息页（★ 必做）与文学领域结构化表达两点保留，公式框一律换成**名句引文框**。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Jean-Marie Gustave Le Clézio（1940-04-13 生于尼斯，在世）
- **气质关键词**：**沙漠的游牧者、主流文明之外的探索者、童年与放逐的书写人** —— 2008 年获奖理由（官方 EN 原文，禁止改写）：
  > "author of new departures, poetic adventure and sensual ecstasy, explorer of a humanity beyond and below the reigning civilization"（表彰这位新出发、诗意冒险与感官狂喜的作者，在主流文明之外与之下探索人性）
- **设计母题**：**沙漠与洋流**。主色深绿承载「Désert（沙漠）」的浩瀚与「毛里求斯—尼斯—阿尔布卡克」三地洋流的流动；前景一弯沙丘弧线，远景星点与船帆意象呼应其游牧人生。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/J._M._G._Le_Clézio/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **参考模板**：
  - 提示词母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`）
  - yaml 母本：`MySQL/data/Kenneth_G_Wilson.yaml`

---

## 三、任务流程 【逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/J._M._G._Le_Cl%C3%A9zio` 四件套到 `literature/presentations/pages/21st_century/J._M._G._Le_Clézio/`（事实基准如下）：
  - 生卒（1940-04-13 生于尼斯，二战中父亲在尼日利亚服役英军）；国籍：**法国 + 毛里求斯双重国籍**（毛里求斯 1968 独立后入籍，自称其为「小小的祖国」）
  - 家族：先祖 François Alexis Le Clézio 1798 逃离法国定居毛里求斯；父系母系祖先均出自布列塔尼 Morbihan
  - 教育：布里斯托大学 (1958–59) → 尼斯文学院本科 → 1964 普罗旺斯大学硕士（论文论亨利·米修与神秘体验）→ 1983 佩皮尼昂大学博士（墨西哥殖民地史：米却肯州 Purépecha 人征服史，1985 出西班牙语版）
  - 行旅：1967 泰国服兵役因抗议童妓被逐、改派墨西哥 → 1970–74 与巴拿马 Embera-Wounaan 部落同住 → 1990 年代起分居阿尔布卡克、毛里求斯、尼斯
  - 婚姻：1975 娶摩洛哥裔 Jémia Jean（至今）；首婚 Rosalie Piquemal，育三女（含首婚一女）
  - 讲学：2007 学年首尔梨花女子大学法语文学、2013-11 受聘南京大学；常访韩国
  - 核心作品：《诉讼笔录》(1963)、《洪水》(1966)、《大地上的受难者》(1967)、《逃遁之书》(1969)、《战争》(1970)、《巨人》(1973)、《沙漠》(1980)、《金矿探求者》(1985)、《奥尼沙》(1991)、《流浪的星》(1992)、《饥馑回旋曲》(2008)、《乌拉尼亚》(2006)、《Alma》(2017)；非虚构《墨西哥之梦》《非洲人》(2004)；译作《奇拉姆·巴拉姆预言书》《米却肯纪事》
  - 关键荣誉：Renaudot 1963、Valery-Larbaud 1972、**Paul-Morand 大奖首任得主 1980（法兰西学士院颁）**、Jean Giono 1997、摩纳哥亲王奖 1998、Stig Dagerman 2008、**2008 诺贝尔文学奖**；荣誉军团勋章骑士 1991/军官 2009、国家功勋勋章军官 1996；瓦努阿图维拉港一所以其名命名的法国中学
  - 生涯数字：40 余部作品、译成 30 余种语言；1994《读书》杂志调查 13% 读者视其为「在世最伟大的法语作家」
  - 关键时间线（15–20 节点）：1940 生于尼斯 → 1948 赴尼日利亚与父团聚 → 7 岁开始写作（处女作关于海）→ 1958–59 布里斯托 → 1963《诉讼笔录》勒诺多奖 + 龚古尔决选 → 1964 硕士论文论米修 → 1967 泰国被逐改派墨西哥 → 1970–74 巴拿马部落生活 → 1975 再婚 → 1970s 后期风格转变 → 1980《沙漠》+ Paul-Morand → 1983 博士论文 → 1991《奥尼沙》→ 1994《读书》调查 → 2007 梨花女大 → 2008-10-09 诺奖 → 2008 诺奖演说《悖论的森林》→ 2013 南京大学

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `J._M._G._Le_Clézio/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已立传目录的 `Makefile`，设置 `MAIN=J._M._G._Le_Clézio_zh`、`VIDEO_NAME=J._M._G._Le_Clézio_zh`（宏名禁数字与特殊字符的规则见模板陷阱：`LeClézio` 重音在 XeLaTeX 下安全，`MAIN` 建议用 `Le_Clezio_zh` 防宏截断，输出文件名保持原目录名）

### 第 3 步：收集图片 【人物专属】

- 从 `images.txt` 取 infobox 肖像（Nobel 2008 新闻发布会照等，250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 时用 Commons `Special:FilePath/<文件名>?width=600`；再失败用装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nomadic novel | 游牧小说 | 流浪、迁徙与身份消解 | 核心页 |
| 1 | desert imagery | 沙漠书写 | 《沙漠》，1980 Paul-Morand | 沙漠页 |
| 2 | intercultural writing | 跨文化写作 | 墨西哥/巴拿马原住民、毛里求斯记忆 | 文化页 |
| 3 | autobiographical fiction | 自传性小说 | 《奥尼沙》《非洲人》 | 回忆页 |
| 4 | literary translation | 文学翻译 | 玛雅/原住民神话的法译 | 侧翼页 |

#### 4.1 入库操作（`MySQL/seed_person.py data/J._M._G._Le_Clézio.yaml`）

- 新建/更新 `people` 主记录（`name_en='Jean-Marie Gustave Le Clézio'`，`qid='Q42037'`），设置 `primary_occupation='writer'`、`has_biography: false`、`has_social_data=1`
- 关联职业 `writer`（rank 0）+ `novelist`/`translator`；国籍 `France`（rank 0）+ `Mauritius`（rank 1）
- 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Jémia Jean | 无向 | 摩洛哥裔，1975 年结婚至今 |
| spouse | Rosalie Piquemal | 无向 | 首任妻子 |
| influence | Henri Michaux | 无向 | 1964 硕士论文《亨利·米修与神秘体验》研究对象 |
| colleague | Georges Perec | 无向 | 1963–75 形式实验时期的同时代作家 |
| colleague | Michel Butor | 无向 | 1963–75 形式实验时期的同时代作家 |
| colleague | Juan Rulfo | 无向 | 为其短篇集法文版作序 |
| colleague | Robert Bresson | 无向 | 为其《电影书写札记》作序 |

#### 4.5.1 入库操作

- 以 `name_en='Jean-Marie Gustave Le Clézio'` 为中心写入 `person_relation`；Michel Butor 库内已有记录（id=5615，勿另建）；其余建 stub（`has_biography=0`，不编造 qid），note 加 `[材料待展开] ` 前缀

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：沙海的浩瀚、季风的流动、主流文明之外的目光
- **配色**：主色深绿 `#145C54`（预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 游牧小说 — 沙丘赭金 `#B8860B`
  - `badgeB` 沙漠书写 — 沙暴橙 `#C46A1F`
  - `badgeC` 跨文化写作 — 大西洋蓝 `#1B6B8C`
  - `badgeD` 自传/翻译 — 岛屿青 `#0E7C7B`
- **背景母题**：沙丘弧线与洋流——底部两道柔和弧（一道沙色一道海色）交汇于左下角，右上稀疏星点

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（右上角 + `draw=coveraccent!50` 细边框）与国籍行（`法国 / 毛里求斯 | 尼斯 | 诺贝尔文学奖 2008`）。
2. **身份信息页 ★ 必做**：左肖像 + 右信息网格（生卒、双重国籍、教育、行旅、婚姻、核心作品、主要荣誉）。
3. 引号用半角 `" "`；结尾页品牌统一 `OpenMathAI`。
4. 引文框内容只用 page.md 载英文/原文语句（瑞典学院授奖评语即诺奖理由原句），禁止杜撰「中文原话」；诺奖演说标题 `Dans la forêt des paradoxes`（In the forest of paradoxes）可入引文框。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 沙漠的游牧者 / J. M. G. Le Clézio 1940– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）
03  核心作品概览 — 诉讼笔录 / 沙漠 / 奥尼沙 / 墨西哥之梦
04  战时尼斯与尼日利亚 (1940–1958) — 1948 全家渡海与父团聚、《非洲人》的记忆
05  布里斯托与尼斯 (1958–1963) — 英伦一年、文学院、23 岁的勒诺多奖
06  《诉讼笔录》核心页（引文框 + 龚古尔决选意象图式）
07  实验时期 (1963–1975) — 疯狂/语言/自然/写作、Perec 与 Butor 的同代人
08  泰国与巴拿马 (1967–1974) — 兵役被逐、Embera-Wounaan 部落岁月
09  《沙漠》与风格转变 (1980) — Paul-Morand 首奖、童年/少年/旅行的新声
10  2008 诺贝尔文学奖 — 官方理由 EN 原文 + 中译、Claude Simon 之后首位法语作家
11  诺奖演说《悖论的森林》 — 信息贫困议题、标题归名 Dagerman
12  毛里求斯：小小的祖国 — 1798 先祖流亡、双重国籍
13  讲学与荣誉 — 梨花女大/南京大学、荣誉军团勋章、Vanuatu 中学命名
14  遗产：在主流文明之外 — 40 余部作品、30 余种语言
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；文学领域页用表格 + 意象色块替代公式框

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Le Clézio 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "author of new departures…" 禁止改写；中译用名录版「在主流文明之外与之下探索人性」 |
| 姓名口径 | 正式全名 Jean-Marie Gustave Le Clézio，通称 J. M. G. Le Clézio；目录名 `J._M._G._Le_Clézio` 与 yaml name_en 均用全名形式，勿混用缩写 |
| 双重国籍 | 法国 + 毛里求斯（名录口径 France / Mauritius）；「小小的祖国」是其自述措辞，可写 |
| French "first" | 是 1985 Claude Simon 之后首位获文学奖的**法语作家**、Sully Prudhomme 以来第十四位；Gao Xingjian 是前一位**法国公民**（2000）——两个口径句勿混 |
| 米修 | Henri Michaux 是其硕士论文研究对象（influence 入库理由），不是导师 |
| Foucault/Deleuze | 仅「被称赞」——评价性提及，非合作关系，**不入库** |
| Stig Dagerman | 诺奖演说标题归其名下，非师承非合作，不入库（其 2008 获 Dagerman 奖是另一事） |
| 泰国被逐 | 1967 抗议童妓被逐、改派墨西哥——客观简述即可 |
| Mama Rosa 争议 | 2014 为墨西哥庇护所负责人辩护（Le Monde 撰文）——只客观陈述，不作评价 |
| 子女 | 三女未具名（仅「首婚一女」），**不入库** |
| 童年起点 | 7 岁开始写作、处女作关于海；首部小说 23 岁获勒诺多——两个年龄勿混 |
| Lycée 命名 | 瓦努阿图维拉港 Lycée Français J. M. G. Le Clézio——冷知识页可用，勿写成毛里求斯 |
| 引语红线 | 无英文引语可框处用瑞典学院评语原句；其余禁伪造 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Le Procès-Verbal | 《诉讼笔录》 | 1963 勒诺多奖作品，英译 The Interrogation |
| Désert | 《沙漠》 | 1980，Paul-Morand 首任大奖 |
| nomadism | 游牧性 | 其书写核心范畴 |
| Embera-Wounaan | 恩贝拉-沃南安人 | 巴拿马原住民部落，1970–74 |
| Purépecha | 普雷佩查人 | 米却肯州，博士论文对象 |
| Chilam Balam | 奇拉姆·巴拉姆预言书 | 玛雅文献法译 |
| Stig Dagerman Prize | 斯蒂格·达格曼奖 | 2008 年获，勿与演说标题混 |
| Grand Prix Paul-Morand | 保罗·莫朗大奖 | 法兰西学士院 1980 新设、首任得主 |
| Prix Renaudot | 勒诺多奖 | 1963 |
| information poverty | 信息贫困 | 诺奖演说议题 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions（56k views，高受众）
- **风格标签**: 高受众 / 时间感 / 纪录片
- **匹配理由**:
  - 「时间感」匹配其创作纵深——从 1963 勒诺多的实验狂徒到 1980《沙漠》的抒情转向再到 2008 诺奖，45 年写作史本身就是一条时间之河
  - 「纪录片」匹配其行旅叙事——尼斯→尼日利亚→布里斯托→墨西哥→巴拿马→毛里求斯，每一步都是地理与记忆的影像志
  - 「高受众」匹配其地位——1994《读书》杂志「在世最伟大法语作家」调查的 13%、30 余种语言的译介广度
- **备选**（未采用）: ★★ SEA——「流动」契合洋流母题，但已预分配给 Pamuk 篇（同批避免撞曲）
- **本地路径**: `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` → `presentations/21st_century/J._M._G._Le_Clézio/The-Flow-of-Time.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/J._M._G._Le_Clézio/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物主记录 + 领域 + 关系入库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实以 page.md 为准，无载禁写；引语只用原文。**
