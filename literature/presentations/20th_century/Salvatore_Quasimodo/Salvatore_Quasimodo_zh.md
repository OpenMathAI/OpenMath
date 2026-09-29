# 文学家立传提示词（OpenLiterature：Salvatore Quasimodo）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Salvatore Quasimodo（1959 诺贝尔文学奖，意大利隐逸派诗人）为传主。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）+ 数学家/化学家侧黄金骨架的文学适配版。
- **本实例**：Salvatore Quasimodo（萨瓦多尔·夸西莫多）。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」骨架，但**无公式框**——以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Salvatore Quasimodo（1901-08-20 ~ 1968-06-14，享年 66 岁）
- **气质关键词**：**隐逸派的封闭语言、古典火焰的译者、西西里-希腊之子** —— 1959 诺贝尔文学奖获奖理由：
  > "for his lyrical poetry, which with classical fire expresses the tragic experience of life in our own times"（表彰其抒情诗，以古典的火焰表达我们时代生活的悲剧性经验）
- **设计母题**：**古典火焰与西西里岩岸（Classical Fire & Sicilian Rock）**。西西里石砌村镇、希腊古典译笔、"以古典的火焰"——用熔岩暗红、石灰岩米白与爱奥尼亚海蓝构成视觉语言。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Salvatore_Quasimodo/page.md`（Wikipedia 全文）
  - `literature/presentations/pages/20th_century/Salvatore_Quasimodo/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Salvatore_Quasimodo
- **肖像**：第 0 步待下载（1968 年照片，images.txt / Commons 回退；404 则装饰圆占位）。

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：研究领域（第 4 步）+ 社会关系（第 4.5 步）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已核对】

- **生卒**：1901-08-20 生于西西里莫迪卡（Modica，意大利王国）～ 1968-06-14 卒于那不勒斯（阿马尔菲演讲期间脑溢血，享年 66 岁）；葬于米兰纪念公墓（Cimitero Monumentale）
- **国籍**：意大利王国 → 意大利（变迁分两条）
- **家庭**：西西里-希腊血统家庭；祖母 Rosa（娘家姓 Papandreou）来自希腊帕特雷；自称 "Siculo-Greco"（西西里-希腊人）；妹夫为作家 Elio Vittorini（Vittorini 娶其妹）
- **教育**：墨西拿技术学院（1919 毕业）；罗马工程学学习未竟（经济所迫任技术制图员）；自学希腊语与拉丁语
- **文学师承与影响**：隐逸派（Hermeticism）代表；1930 年 Reggio Calabria 遇 **Misefari 兄弟**鼓励其继续写作（page.md 明载，未具全名不入库）；与《Circoli》杂志的 **Camillo Sbarbaro** 等合作（明载）
- **任职/经历**：意大利土木工程军团职员（1930 Reggio Calabria → 1931 Imperia/Genoa → 1934 米兰）；1938 起全职写作（与 **Cesare Zavattini** 合作，为隐逸派官方评论《Letteratura》撰稿）；1945 短期加入意大利共产党；战后任多家意大利大报戏剧评论记者；多次欧陆与美洲巡讲
- **关键荣誉**：Premio San Babila（1950）、Etna-Taormina（1953）、Premio Viareggio（1958）、1959 诺贝尔文学奖；墨西拿大学荣誉博士（1960）、牛津大学荣誉博士（1967）；1959-12-11 诺奖演讲《诗人与政治家》
- **核心作品与贡献**（4–6 条）：
  1. 《水与土》Acque e terre（1930，首部诗集）
  2. 《沉没的欧勃》Oboe sommerso（1932）
  3. 《希腊诗歌译集》Lirici Greci（1939）+ 二战期译《约翰福音》、卡图卢斯、《奥德赛》选段
  4. 《日复一日》Giorno dopo giorno（1946）——道德介入与史诗性社会批评的转向
  5. 《生活不是梦》La vita non è sogno / 《假与真之绿》/ 《无与伦比的大地》
  6. 与 Ungaretti、Montale 并称 20 世纪意大利诗坛三杰（page.md 明载）
- **关键时间线**（15 节点）：
  1. 1901-08-20 生于莫迪卡
  2. 童年在 Roccalumera
  3. 1908 全家迁墨西拿（父亲参与地震救灾，自然伟力留下深刻印象）
  4. 1908s 被父亲引入苏格兰礼共济会（"Arnaldo da Brescia"分会；意大利大东方总会承认其为杰出会员）
  5. 1917 创办短命诗刊《Nuovo giornale letterario》，发表首批诗作
  6. 1919 罗马工程学学习；制图员谋生
  7. 1929 应 Elio Vittorini 之邀迁佛罗伦萨；结识 Bonsanti、Montale
  8. 1930 Reggio Calabria；首部诗集《Acque e terre》
  9. 1931–1932 Imperia/Genoa；《Circoli》合作；1932《Oboe sommerso》
  10. 1934 迁米兰
  11. 1938 全职写作；与 Zavattini 合作；1939《Lirici Greci》
  12. 二战译《约翰福音》/卡图卢斯/《奥德赛》；1945 短期入党
  13. 1946《Giorno dopo giorno》——公民诗转向
  14. 1950s 获奖：1950/1953/1958 → 1959 诺贝尔
  15. 1968-06 阿马尔菲演讲突发脑溢血，卒于那不勒斯

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hermetic poetry | 隐逸派诗歌 | 其战前核心风格，"closed" 语言 | 核心页 |
| 1 | lyric poetry | 抒情诗 | 诺奖理由主体 | 封面、核心页 |
| 2 | civic poetry | 公民诗 | 战后《日复一日》起的道德介入转向 | 战后页 |
| 3 | literary translation | 文学翻译 | 希腊古典/卡图卢斯/《奥德赛》/《约翰福音》 | 翻译页 |
| 4 | poetry criticism | 诗歌与戏剧评论 | 战后任记者写戏剧评论 | 记者页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Elio Vittorini | 无向 | 妹夫，1929 邀其迁佛罗伦萨 |
| colleague | Eugenio Montale | 无向 | 1929 佛罗伦萨结识，并称三杰 |
| colleague | Giuseppe Ungaretti | 无向 | 与其、蒙塔莱并称 20 世纪意大利诗坛三杰 |
| colleague | Cesare Zavattini | 无向 | 1938 起全职写作期的合作者 |
| colleague | Camillo Sbarbaro | 无向 | 热那亚《Circoli》杂志圈合作 |
| colleague | Giorgio La Pira | 无向 | 墨西拿少年挚友，后任佛罗伦萨市长 |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：古典、凝重、火山与海
- **配色**：主色 **#16324F**（分批文件预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 隐逸派 — 石灰岩白 `#B8AF9E`
  - `badgeB` 公民诗 — 熔岩红 `#9E3B2B`
  - `badgeC` 古典翻译 — 爱琴蓝 `#2E6E8E`
  - `badgeD` 诺奖 — 香槟金 `#C9A227`
- **背景母题**：细密石纹底 + 一束火焰光晕（"classical fire"）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 古典的火焰 / Salvatore Quasimodo 1901–1968 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍变迁、血统、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 隐逸派 / 抒情诗 / 公民诗 / 古典翻译
04  西西里少年 (1901–1919) — 莫迪卡/Roccalumera、1908 墨西拿地震、共济会家世
05  工程师的诗人 (1919–1930) — 罗马、制图员、希腊拉丁自学
06  佛罗伦萨与《Acque e terre》(1929–1930) — Vittorini、隐逸派起点
07  Circoli 与《Oboe sommerso》(1931–1934) — 热那亚、封闭语言（意象图式）
08  米兰与《Letteratura》(1934–1939) — 全职写作、Zavattini、《Lirici Greci》
09  战争与转向 (1940–1946) — 古典翻译避世、《日复一日》公民诗（书影页）
10  战后成熟期 — 《生活不是梦》/《无与伦比的大地》、巡讲与荣誉博士
11  1959 诺贝尔 — 获奖理由、《诗人与政治家》演讲、晚年（1968 那不勒斯）
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

**陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生地 | 出生于**莫迪卡**（Modica）；他本人曾把出生地改写为叙拉古（Syracuse）——以史实为准写 Modica，可注其自述轶事 |
| "Siculo-Greco" | 自称"西西里-希腊人"，祖母 Rosa 娘家 Papandreou 来自帕特雷——勿写"希腊裔诗人"泛称 |
| 共济会 | 由父亲引入苏格兰礼分会 "Arnaldo da Brescia"，意大利大东方总会承认——客观一笔即可 |
| 并称三杰 | 与 Ungaretti、Montale 并称是 page.md 原文明载的评价句，可用；勿再加第四人 |
| 反法西斯与入党 | 自称反法西斯但未参加抵抗运动；1945 短期加入意大利共产党——客观简述，不作政治评价 |
| 两段时期 | 传统批评分为"隐逸派时期（至二战）"与"战后时期"——但 page.md 强调"同一场诗性求索"，勿割裂成两人 |
| Misefari 兄弟 | 鼓励其写作，未具全名——不入库（提示词可提及） |
| 世界宪法 | 世界宪法大会签名发起人之一——可入荣誉/活动，不入关系表 |
| 获奖理由 | "classical fire"（古典的火焰）为官方措辞，勿改写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Hermeticism | 隐逸派（埃尔梅蒂科） | 意大利诗歌运动，勿与炼金术 hermeticism 混 |
| Acque e terre | 《水与土》 | 1930 首部诗集 |
| Oboe sommerso | 《沉没的欧勃》 | 1932 |
| Giorno dopo giorno | 《日复一日》 | 1946，公民诗转向 |
| Lirici Greci | 《希腊诗歌译集》 | 1939 |
| classical fire | 古典的火焰 | 诺奖理由关键词 |
| Letteratura | 《文学》杂志 | 隐逸派官方评论 |
| Circoli | 《环》杂志 | 热那亚文学圈 |
| Siculo-Greco | 西西里-希腊人 | 自称 |
| Cimitero Monumentale | 米兰纪念公墓 | 安葬地 |
| The Poet and the Politician | 《诗人与政治家》 | 1959 诺奖演讲 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（分批文件预分配）
- **风格**：内省 / 沉静 / 陪伴感
- **匹配理由**：隐逸派"封闭语言"的内省气质与 With Me 的静谧内聚力同构；"以古典的火焰表达悲剧性经验"需要克制的温度而非外放的悲怆。
- **备选**：Timeless（古典纵深感，但同项目使用频率高）。

---

> **开始执行。每完成一步汇报。**
> **最重要的事：文学家无公式框——用书影/名句引文框/意象图式；每写一页就 make。**
