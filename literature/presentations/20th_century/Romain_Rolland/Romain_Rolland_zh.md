# 文学家立传提示词（Romain Rolland，1915 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Kenneth G. Wilson 提示词骨架为母本，适配文学家侧。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人文史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）骨架 + 文学家适配（无公式框——用名句引文框/代表作书影/意象图式替代）。
- **本实例**：Romain Rolland（罗曼·罗兰，1915 年诺贝尔文学奖得主，《约翰·克利斯朵夫》作者、"欧洲的道德良知"）。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」（Identity / Bio 速览页），核心页用代表作与引文框承载文学成就。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Romain Rolland（1866-01-29 ~ 1944-12-30，享年 78 岁）
- **官方获奖理由（EN 原文，禁止改写）**：
  > "as a tribute to the lofty idealism of his literary production and to the sympathy and love of truth with which he has described different types of human beings"
- **官方获奖理由（中译，取自 `literature/generate_20th_century_list.py` CITATION_ZH，key=("1915","Romain Rolland")，禁止改写）**：
  > 表彰其文学作品中的崇高理想主义，以及其描写各类人物时所怀有的同情心与对真理的热爱
- **气质关键词**：**长河小说的建造者、音乐史的教授、超然于混战之上的人**
- **设计母题**：**河流与钟声（the river and the bell）**。Jean-Christophe 以莱茵河—塞纳河的"河"贯穿十卷——用河流分叉汇合的线束承载长河小说结构；克利斯朵夫是音乐天才，用五线谱与钟（Vézelay 晚年隐居地）意象呼应其音乐学教授身份与贝多芬传记。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Romain_Rolland/page.md`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Romain_Rolland
- **肖像**：待下载（page.md 内嵌 1914 家中阳台照 `Romain_Rolland_au_balcon,_Meurisse,_1914_retouche.jpg`，取此帧）
- **参考模板**：`literature/presentations/cover/`；成品骨架参照 15 页结构

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载到 `literature/presentations/pages/20th_century/Romain_Rolland/`
- 肖像待下载（第 3 步）
- 事实基准（以 page.md 正文为准）：
  - 生卒（1866-01-29 生于 Clamecy, Nièvre ~ 1944-12-30 逝于 Vézelay，享年 78 岁；自认"古老物种"的代表，祖先入 Colas Breugnon）
  - 国籍（法国；一战中移居瑞士（日内瓦湖畔 Villeneuve），1937 返 Vézelay，1940 德占期闭门独处）
  - 家庭（家世兼有市镇富人与农民两支；妹 Madeleine Rolland；1892 与 Clothilde Bréal 成婚、1901 离异；1934 与 Marie 再婚相伴至终）
  - 教育（1886 入 École normale supérieure——先学哲学，因不甘屈从主流意识形态转史；1889 史学学位；罗马两年；1895 博士论文《现代抒情剧的起源——吕利与斯卡拉蒂之前的欧洲歌剧史》，另有一篇论 16 世纪意大利油画衰落的拉丁语论文）
  - 文学师承与影响（罗马遇 **Malwida von Meysenbug**——尼采与瓦格纳之友，对其思想形成"决定性"；**Swami Vivekananda** 的吠檀多著作——印度哲学影响的主源；人民剧院理念承 **Maurice Pottecher** 并将 The People's Theatre 题献给他；卢梭的人民节庆观）
  - 任职（里昂 Henri IV 与 Louis-le-Grand 中学史教员 → École française de Rome 成员 → 索邦音乐史教授（1903 首任讲席）→ École Normale Supérieure 史学教授 → 1902-1911 任 École des Hautes Études Sociales 新设音乐学校主任 → 1912 辞教职专事写作）
  - 关键荣誉（Nobel 1915；Prix Femina；Grand prix de littérature de l'Académie française；博士论文获法兰西学术院奖）
  - 和平主义事迹（一战移居瑞士抗议、Au-dessus de la mêlée (1915)；1920 提出 "Pessimism of the intellect, optimism of the will"（后被 Gramsci 采为格言）；1922 签国际进步艺术家联合创始宣言；1928 与 Edmund Bordeaux Szekely 创立 International Biogenic Society；1932 World Committee Against War and Fascism 首批成员（对 Münzenberg 的控制不满））
  - 争议（1935 应 Maxim Gorky 邀访莫斯科并会斯大林，赞其"当代最伟大的人"；为 Victor Serge 与 Bukharin 求情；Serge《笔记》斥其为暴政阿谀者，传记家 Duchatelet 力驳——**两说并存，只陈述事实，不作政治评价**）
  - 核心作品与贡献（4-6 条）：Jean-Christophe (1904–1912，十卷三部曲长河小说)；人民剧院理论与实践（Le Théâtre du peuple 1903、Danton 1900、Le Quatorze Juillet 1902）；伟人传记系列（Vie de Beethoven 1903、Vie de Michel-Ange 1907、Haendel 1910、La Vie de Tolstoï 1911）；第二部长河小说 L'Âme enchantée 七卷 (1922–1933)；印度灵魂三部随笔（Vie de Ramakrishna 1929、Vie de Vivekananda 1930、L'Inde vivante）与 Mahatma Gandhi 传 (1924)；1938 话剧 Robespierre、1942 回忆录 Le Voyage intérieur、身后 Péguy (1945)）
  - 通信网络（Richard Strauss 1899 起的 239 页通信——191 处 Salome 法文改编建议；Freud 1923-1939 通信——"海洋感"（oceanic feeling）经 Freud《文明及其不满》开篇流传；Stefan Zweig 1921 为其作传并称"欧洲的道德良知"；Hermann Hesse 将《悉达多》题献"我亲爱的朋友"）
  - 关键时间线（约 18 节点，见第 6 步幻灯片序列年份锚点）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下已有 `Romain_Rolland/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制邻近成品 `Makefile`，设置 `MAIN=Romain_Rolland_zh`、`VIDEO_NAME=Romain_Rolland_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载：1914 阳台照优先，Commons `Special:FilePath` 加 `?width=600`
- 可选插图：Jean-Christophe 初版卷首、苏联 1966 百年纪念邮票、Piscator 1922 柏林节目单

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | roman-fleuve | 长河小说 | Jean-Christophe 十卷与 L'Âme enchantée 七卷 | 核心页 |
| 1 | people's theatre | 人民剧院 | 理论与实践：Le Théâtre du peuple 与革命剧 | 戏剧页 |
| 2 | musicology | 音乐学 | 索邦首任音乐史讲席、歌剧史博士论文 | 音乐页 |
| 3 | biography | 伟人传记 | 贝多芬/米开朗琪罗/托尔斯泰/甘地系列 | 传记页 |
| 4 | pacifist essay | 和平主义政论 | Au-dessus de la mêlée 与一战后论著 | 政论页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Malwida von Meysenbug | 对方→本人 | 罗马岁月的决定性相遇，尼采与瓦格纳之友 |
| influence | Swami Vivekananda | 对方→本人 | 吠檀多哲学经其著作影响罗兰的印度观 |
| colleague | Maurice Pottecher | 无向 | 人民剧院先行者，The People's Theatre 题献对象 |
| colleague | Stefan Zweig | 无向 | 密友，1921 为其作传，誉之为欧洲的道德良知 |
| colleague | Sigmund Freud | 无向 | 1923-1939 通信，海洋感概念启文明及其不满开篇 |
| colleague | Richard Strauss | 无向 | 1899 起通信，191 条 Salome 法文歌词建议 |
| colleague | Hermann Hesse | 无向 | 密友，悉达多题献于罗兰 |
| colleague | Maxim Gorky | 无向 | 通信多年，1935 邀其访莫斯科 |
| colleague | Rabindranath Tagore | 无向 | 钦佩者与通信者（1919-1940），甘地传记作者亦敬慕其人 |
| influence | Mahatma Gandhi | 对方→本人 | 仰慕并作传（1924），1931 会面 |
| spouse | Clothilde Bréal | 无向 | 1892 成婚，1901 离异 |
| spouse | Marie Romain Rolland | 无向 | 1934 再婚，相伴至 1944 年终 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：胭脂红 `#A31621`（分批文件预分配）
- **配色**：主色 + 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 长河小说 — 靛蓝 `#4C5FD5`
  - `badgeB` 人民剧院 — 琥珀 `#E07B30`
  - `badgeC` 音乐学与传记 — 青绿 `#0E7C7B`
  - `badgeD` 和平主义政论 — 玫瑰 `#C4204F`
- **背景母题**：河流线束分合 + 远山钟楼剪影（呼应设计母题）

### 第 6 步：规划幻灯片序列 【人物专属，13-15 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 欧洲的良心 / Romain Rolland 1866–1944 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、出生地、教育、影响者、任职、荣誉、核心领域）
03  核心贡献概览 — 长河小说 / 人民剧院 / 音乐学与传记 / 和平主义政论
04  Clamecy 与高师 (1866–1889) — 两支家世、哲学转史学、antique species 自白
05  罗马岁月 (1889–1895) — Meysenbug 的决定性相遇、歌剧史博士论文、法兰西学术院奖
06  讲坛与音乐 (1895–1903) — 中学教员、索邦首任音乐史讲席、Hautes Études Sociales 音乐学校
07  人民剧院（核心贡献页一·引文框替代公式框）— 题献 Pottecher、Danton 与七月十四日、卢梭式节庆观
08  Jean-Christophe (1904–1912)（核心贡献页二）— 十卷三部曲结构图、音乐天才跨越莱茵与塞纳
09  伟人列传 — Beethoven 1903 / Michel-Ange 1907 / Haendel 1910 / Tolstoï 1911
10  超然于混战 (1914–1918) — 移居瑞士、Au-dessus de la mêlée、诺奖 1915、悲观之智与乐观之志
11  通信的宇宙 — Strauss 之 Salome、Freud 之海洋感、Zweig 之作传、Hesse 之题献
12  印度灵魂 — Tagore 通信、Vivekananda 吠檀多、甘地传与 1931 会面
13  晚年 (1922–1944) — L'Âme enchantée 七卷、Biogenic Society、莫斯科之行两说、Vézelay 终章
14  遗产与结尾 — 长河小说体例的后继、1966 苏联百年纪念邮票、Péguy 遗作
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Rolland 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖年份与发表 | 1915 年度奖（因一战 1916 才正式宣布授予的背景 page.md 未载，**勿自行补充**）；1915 同时出版 Au-dessus de la mêlée——年份并列勿写成因果 |
| 莫斯科之行 | 1935 访苏、赞斯大林与为 Serge/Bukharin 求情、Serge 遗文与 Duchatelet 反驳——**四件事实并列，两说并存，绝不下政治判断、不写"亲苏"或"反苏"定性** |
| 政治红线 | World Committee、Münzenberg 分歧、Gramsci 采撷格言——只陈述 page.md 客观事实，不展开政治叙事 |
| 格言归属 | "Pessimism of the intellect, optimism of the will" 1920 由罗兰先写，Gramsci 采用——归属写"罗兰提出、葛兰西采用" |
| 妻子姓名 | 第二任妻子在 infobox 红链作 "Marie Romain Rolland"——yaml 照录此形式，note 注明 1934 再婚；勿写成其他史料中的名字 |
| 海洋感 | oceanic feeling 是罗兰经东方神秘主义研究发展、经 Freud《文明及其不满》(1929) 开篇流传——是"罗兰给了 Freud"，勿写成 Freud 自创 |
| Jean-Christophe 卷次 | 十卷分三部（Jean-Christophe / à Paris / Fin du voyage），1904-1912，Cahiers de la Quinzaine 初刊——三部曲结构勿错 |
| Strauss 通信 | 1899 起、英译 239 页、Salome 建议条数 191——三个数字勿混 |
| 人民剧院年份 | Le Théâtre du peuple 内容 1900-1903 陆续发表于 Revue d'Art Dramatique、成书 1913 出版——两日期并存 |
| 引语红线 | 人民剧院卷首语与扶椅段（若用）均为 page.md 英文/译文原文可引并注出处；Zweig "欧洲的道德良知" 属转述评价，注明 Zweig |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| roman-fleuve | 长河小说 | 十卷体例专名 |
| Jean-Christophe | 约翰·克利斯朵夫 | 保留原名 |
| L'Âme enchantée | 被蛊惑的灵魂 | 第二部长河小说 |
| people's theatre | 人民剧院 | 与大众剧场区分 |
| oceanic feeling | 海洋感 | 宗教心理学概念 |
| Au-dessus de la mêlée | 超越混战 | 保留法语名 |
| Vedanta | 吠檀多 | 印度哲学学派 |
| École normale supérieure | 巴黎高等师范学院 | 机构名保留 |
| Quinze Chansons / （无） | — | 属 Maeterlinck，勿误植 |
| Gottbegnadeten（无） | — | 属 Hauptmann，勿误植 |
| Cahiers de la Quinzaine | 双周刊丛刊 | 初刊载体 |
| International Biogenic Society | 国际生元学会 | 1928 共创 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（分批文件预分配）
- **匹配理由**:
  - "New Lands" 的开拓气质匹配其"新大陆"式的一生——从 Clamecy 到罗马到索邦讲席到日内瓦湖畔的流亡写作，每一站都是精神疆域的推进
  - 曲名的辽阔贴合 Jean-Christophe 的跨河叙事——德国音乐天才在法国找到第二故乡，两个民族借艺术互认
  - 尾段的沉静适配其 1937-1944 在 Vézelay 的孤独终章与身后的 Péguy 遗响
- **本地路径**: 从 `music_audio/` 曲库复制对应曲目到 `presentations/20th_century/Romain_Rolland/`（对照 `curated_tracks.md`）
- **时长**: 按页数 × 7 秒估算，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Romain_Rolland/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Romain_Rolland.yaml` | 社会关系/领域入库 yaml（与本文件同步） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
