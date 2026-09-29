# 文学家立传提示词（OpenLiterature：Albert Camus）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Albert Camus（1957 诺贝尔文学奖，荒诞主义作家/哲学家）为传主。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）+ 数学家/化学家侧黄金骨架的文学适配版。
- **本实例**：Albert Camus（阿尔贝·加缪）。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」骨架，但**无公式框**——以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Albert Camus（1913-11-07 ~ 1960-01-04，享年 46 岁）
- **气质关键词**：**荒诞的抵抗者、地中海的道德家、黑色小说里的阳光** —— 1957 诺贝尔文学奖获奖理由：
  > 表彰其重要的文学创作，以清明的认真态度照亮我们时代人类良知的问题（官方 EN："for his important literary production, which with clear-sighted earnestness illuminates the problems of the human conscience in our time"）
- **设计母题**：**烈日与荒诞（Sun & the Absurd）**。阿尔及尔的太阳、西西弗的巨石、奥兰的瘟疫——用高对比的日光金与深黑构成视觉语言，阳光下最明亮处恰是荒诞最清晰处。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Albert_Camus/page.md`（Wikipedia 全文）
  - `literature/presentations/pages/20th_century/Albert_Camus/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Albert_Camus
- **肖像**：第 0 步待下载（1957《纽约世界电讯报》肖像，images.txt / Commons 回退；404 则装饰圆占位）。

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：研究领域（第 4 步）+ 社会关系（第 4.5 步）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已核对】

- **生卒**：1913-11-07 生于法属阿尔及利亚蒙多维（Mondovi，今 Dréan）～ 1960-01-04 卒于法国维尔布勒万（Villeblevin，车祸，享年 46 岁）
- **国籍**：法国（生于法属阿尔及利亚的 pied-noir 家庭，法国公民）
- **家庭**：父 Lucien Camus 1914 年一战阵亡（时年加缪不足 1 岁）；母 Catherine Hélène Camus（娘家 Sintès，西班牙巴利阿里血统）聋哑且不识字；1934 与 Simone Hié 结婚（1936 离婚），1940-12-03 与钢琴家兼数学家 Francine Faure 结婚（1945 龙凤胎 Catherine 与 Jean）
- **教育**：阿尔及尔大学（University of Algiers），1936 普罗提诺论文获哲学业士（licence de philosophie）
- **文学师承与影响**：中学哲学教师 **Jean Grenier** 为导师（page.md 明载，infobox academic advisor）；哲学起点为古希腊哲学、**Nietzsche** 与 17 世纪道德家（明载）；**Simone Weil** 的著作被其视为虚无主义的"解毒剂"（明载）；受 Stendhal、Melville、Dostoyevsky、Kafka 等小说家-哲学家吸引（明载）
- **任职/经历**：《阿尔及尔共和报》（Alger républicain，1938）记者；二战参加抵抗运动，地下报纸《Combat》主编（用假名与假证件）；战后巡回演讲；伽利玛出版社 "Espoir" 主编；1952 因联合国接纳佛朗哥西班牙辞去 UNESCO 职务；1950-51 与爱因斯坦同为"人民世界公约"发起人之一
- **关键荣誉**：1957 诺贝尔文学奖（44 岁，史上第二年轻，仅次于 41 岁的 Kipling；首位出生于非洲的文学奖得主）
- **核心作品与贡献**（4–6 条）：
  1. 荒诞系列（第一循环）：《局外人》L'Étranger（1942）+《西西弗神话》（1942）+《卡利古拉》（1945 上演）
  2. 反抗系列（第二循环）：《鼠疫》La Peste（1947）+《反抗者》L'Homme révolté（1951）+《正义者》（1949）
  3. 《堕落》La Chute（1956）/《流放与王国》（1957）
  4. 《第一个人》Le Premier Homme（未完成自传体小说，1994 遗作出版）
  5. 荒诞主义（Absurdism）哲学的系统表述者——"我反抗，故我们存在"
  6. 《反思死刑》（与 Arthur Koestler 合著，1957）
- **关键时间线**（15 节点）：
  1. 1913-11-07 生于蒙多维
  2. 1914 父亲阵亡；贫民区童年（Belcourt）
  3. 1924 小学教师 Louis Germain 助其获奖学金进入中学
  4. 1928–1930 Racing Universitaire d'Alger 青年队守门员
  5. 1930 17 岁确诊肺结核；转投哲学，受教于 Jean Grenier
  6. 1933–1936 阿尔及尔大学；普罗提诺论文
  7. 1935 加入法国共产党（次年离开；后加入阿尔及利亚共产党并被开除）
  8. 1937 首部随笔集《反与正》；"Théâtre de l'Equipe"
  9. 1938–1940 《阿尔及尔共和报》→《巴黎晚报》
  10. 1942 《局外人》《西西弗神话》出版
  11. 1943–1944 巴黎；结识 Sartre；《Combat》抵抗运动主编
  12. 1947 《鼠疫》
  13. 1951–1952 《反抗者》→ 与 Sartre 最终决裂
  14. 1957-12 诺贝尔文学奖；斯德哥尔摩演讲献给 Louis Germain
  15. 1960-01-04 Villeblevin 车祸身亡（出版商 Michel Gallimard 5 日后亦亡）；《第一个人》手稿 144 页幸存于废车中；葬于 Lourmarin

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | absurdism | 荒诞主义 | 其哲学-文学核心概念，Notable ideas 明载 | 核心页 |
| 1 | existentialism | 存在主义 | 常被归入但他本人终生拒绝此标签 | 哲学页 |
| 2 | moral philosophy | 道德哲学 | 道德家立场；自杀问题/反抗的限度 | 哲学页 |
| 3 | theatre | 戏剧 | 卡利古拉/误解/正义者；第三循环转向戏剧 | 剧作页 |
| 4 | engaged journalism | 介入式新闻 | Combat 主编、阿尔及利亚报道 | 记者页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jean Grenier | 师→生（direction: advisor） | 中学哲学教师/阿尔及尔大学导师 |
| influence | Louis Germain | 无向 | 小学教师，1924 助其获奖学金，诺奖演说献词 |
| influence | Friedrich Nietzsche | 无向 | 自述哲学起点之一 |
| influence | Simone Weil | 无向 | 为其出版遗著，视其著作为虚无主义解毒剂 |
| colleague | Jean-Paul Sartre | 无向 | 1943 巴黎结识成友 |
| controversy | Jean-Paul Sartre | 无向 | 1952 《反抗者》引发最终决裂 |
| colleague | Simone de Beauvoir | 无向 | 战后巴黎知识分子圈 |
| colleague | Arthur Koestler | 无向 | 1957 合著《反思死刑》 |
| colleague | William Faulkner | 无向 | 加缪改编其《修女安魂曲》(1956)；福克纳为其撰讣告 |
| spouse | Simone Hié | 无向 | 1934 结婚，1936 离婚 |
| spouse | Francine Faure | 无向 | 1940 结婚，钢琴家兼数学家，育龙凤胎 |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：烈日、清峻、道德的冷光
- **配色**：主色 **#1E4D3B**（分批文件预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 荒诞 — 赭黄 `#D9A441`
  - `badgeB` 反抗 — 砖红 `#A3452E`
  - `badgeC` 地中海记忆 — 湛蓝 `#2E6E8E`
  - `badgeD` 诺奖 — 香槟金 `#C9A227`
- **背景母题**：高对比日光放射线 + 巨石剪影（西西弗意象）；克制使用，避免花哨

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 荒诞的抵抗者 / Albert Camus 1913–1960 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、出生地、导师、任职、荣誉、核心领域）
03  核心贡献概览 — 荒诞 / 反抗 / 戏剧 / 介入式新闻
04  阿尔及尔少年 (1913–1930) — 贫民区、Germain 奖学金、守门员、肺结核
05  大学与导师 Grenier (1930–1936) — 普罗提诺论文、尼采与古希腊
06  记者 (1938–1940) — 阿尔及尔共和报、卡比利报道
07  抵抗与《Combat》(1940–1944) — 假名主编、致德国友人的信
08  荒诞三部曲（核心贡献页）— 《局外人》书影 + 名句引文框
09  《鼠疫》与《反抗者》 — 反抗系列、与 Sartre 决裂
10  戏剧与第三循环 — Caligula、改编《群魔》、Nemesis
11  1957 诺贝尔 — 44 岁第二年轻、斯德哥尔摩演讲、献给 Germain
12  车祸与遗产 (1960) — Villeblevin、《第一个人》手稿、福克纳讣告
13  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

**陷阱**：

| 陷阱 | 说明 |
|------|------|
| 存在主义标签 | Camus **本人终生拒绝**"存在主义者"标签——领域表可列 existentialism 但必须带此注记，勿写成"存在主义代表人物" |
| 获奖年龄口径 | 44 岁、史上第二年轻（仅次于 41 岁的 Kipling）、首位生于非洲的文学奖得主——三句并列勿混 |
| 决裂时点 | 与 Sartre 1943 结识为友，1952 年《反抗者》之后最终决裂——两段关系分开写，勿写成"毕生死敌" |
| 车祸细节 | 1960-01-04 死于 Villeblevin 车祸；同车出版商 Michel Gallimard 5 天后身亡；《第一个人》手稿在残车内被发现 |
| 出生国籍 | 生于法属阿尔及利亚但为法国公民（pied-noir），国籍表只写 France，勿写 Algeria |
| 共产党经历 | 1935 入法共 1936 年离开、后入阿尔及利亚共产党并被开除——按 page.md 客观简述，不作政治评价 |
| 阿尔及利亚战争 | "民事休战"立场被双方拒绝、被左翼及后殖民批评者批评——客观转述，不站队 |
| 引语红线 | 名句只在 page.md 有英文/法文原文时引用（如 "I revolt, therefore we exist"、Germain 信）；无原文处用忠实转述 |
| 荒诞定义 | "confrontation between human need and the unreasonable silence of the world" 为 page.md 明载表述，可用 |
| KGB 推测 | 2011 年 Catelli 的暗杀假说是**未经证实的推断**，如提必须写明系其主张 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| absurdism | 荒诞主义 | Camus 的"Notable ideas" |
| the Absurd | 荒诞 | 人生无意义的 confrontation |
| revolt / rebellion | 反抗 | 区别于 revolution（革命） |
| pied-noir | 黑脚（法属阿尔及利亚欧裔） | 身份背景，勿译"黑脚杆"等戏称 |
| L'Étranger | 《局外人》 | 英译 The Stranger/The Outsider 两版 |
| La Peste | 《鼠疫》 | 1947 |
| L'Homme révolté | 《反抗者》 | 1951，决裂导火索 |
| Le Premier Homme | 《第一个人》 | 遗作 1994 |
| cycle of the absurd | 荒诞循环 | 小说+随笔+戏剧三件套 |
| Combat | 《战斗报》 | 地下抵抗报纸 |
| French Resistance | 法国抵抗运动 | 二战背景 |
| civil truce | 民事休战 | 阿尔及利亚战争主张 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（分批文件预分配）
- **风格**：硬朗 / 张力 / 冷峻
- **匹配理由**：荒诞与反抗的张力、烈日下的道德冷光，与 Savage 的坚硬质感同构；1940s 巴黎抵抗岁月的历史重量亦需此等力度承载。
- **备选**：The Invisible Light（清冷但张力不足）。

---

> **开始执行。每完成一步汇报。**
> **最重要的事：文学家无公式框——用书影/名句引文框/意象图式；每写一页就 make。**
