# 文学家立传提示词（OpenLiterature：Saint-John Perse）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Saint-John Perse（1960 诺贝尔文学奖，诗人外交官 Alexis Leger）为传主。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）+ 数学家/化学家侧黄金骨架的文学适配版。
- **本实例**：Saint-John Perse（圣琼·佩斯，本名 Alexis Leger）。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」骨架，但**无公式框**——以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Alexis Leger（Saint-John Perse）（1887-05-31 ~ 1975-09-20，享年 88 岁）
- **气质关键词**：**诗人外交官、大西洋的孩子、流亡中的颂歌** —— 1960 诺贝尔文学奖获奖理由：
  > "for the soaring flight and the evocative imagery of his poetry which in a visionary fashion reflects the conditions of our time"（表彰其诗歌的高扬气势与引人遐想的意象，以先知般的方式反映我们时代的境况）
- **设计母题**：**季风与加勒比（Winds & the Caribbean）**。瓜德罗普的种植园童年、戈壁的幻境、《风》与《雨》《雪》——以季风线、海岛轮廓与信笺留白构成视觉语言。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Saint-John_Perse/page.md`（Wikipedia 全文）
  - `literature/presentations/pages/20th_century/Saint-John_Perse/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Saint-John_Perse
- **肖像**：第 0 步待下载（1960 年照片，images.txt / Commons 回退；404 则装饰圆占位）。

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：研究领域（第 4 步）+ 社会关系（第 4.5 步）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已核对】

- **生卒**：1887-05-31 生于瓜德罗普皮特尔角（Pointe-à-Pitre）～ 1975-09-20 卒于法国普罗旺斯吉昂半岛（Giens Peninsula，享年 88 岁）
- **国籍**：法国（1940 年被维希政府褫夺公民身份与荣誉军团勋章，战后恢复）
- **姓名**：本名 Alexis Leger；笔名 **Saint-John Perse**（亦作 Saint-Leger Leger）；后自改姓氏为更贵族气的 "St Léger-Léger"（自称古老贵族后裔，实为公证人家庭）
- **家庭**：曾祖 Prosper Louis Léger 1815 年定居瓜德罗普；祖父与父亲皆公证人，父兼任市议员；家有两处种植园（咖啡园 La Joséphine、糖园 Bois-Debut）；与母亲亲近而疏于严父；1958 与美国人 **Dorothy Milburn Russell** 结婚
- **教育**：Pau 路易-巴尔杜中学（Lycée Louis-Barthou）会考荣誉等；波尔多大学法学（1910 毕业，期间任《Pau-Gazette》音乐评论）
- **文学师承与影响**：1904 年奥尔特兹结识诗人 **Francis Jammes**（挚友）；出入文化沙龙结识 Claudel、Redon、Larbaud、Gide；1912 当选伦敦"约翰·多恩俱乐部"，赴伦敦遇 **Joseph Conrad**（大受鼓励）；《颂歌集》几乎无人问津时获 **Proust** 赞许；早年诗受鲁滨逊漂流记启发（*Images à Crusoe*），并着手译 **Pindar**
- **外交生涯**：1914 入法国外交部（先派驻西班牙/德国/英国）；**1916–1921 驻北京公使馆秘书**（住道观、游戈壁，写成史诗《阿纳巴斯》）；1921 华盛顿裁军会议被 **Aristide Briand** 看中→1921–1932 任其首席助理；**1932–1940 任法国外交部秘书长**（贝特洛 Philippe Berthelot 的被选接班人）；1940 年 5 月失势（Reynaud 时期被排斥）
- **流亡与荣归**：1940 维希政府将其从荣誉军团除名、褫夺法国公民身份、没收财产（战后恢复）；巴黎寓所遭德军洗劫、未刊诗稿被焚；流亡华盛顿（MacLeish 援助）；1957 美国友人赠吉昂半岛别墅；1958 与 Dorothy Milburn Russell 结婚；1960 获诺贝尔文学奖
- **关键荣誉**：1960 诺贝尔文学奖；荣誉军团多级勋位（骑士→军官→指挥官→大军官）；Grand prix national des Lettres
- **核心作品与贡献**（4–6 条）：
  1. 《颂歌集》Éloges（1910）——瓜德罗普童年记忆，Proust 亦加称许
  2. 《阿纳巴斯》Anabase（1924）——北京写就的史诗；T. S. Eliot 1930 年英译
  3. 流亡组诗：《流放》Exil（1942）、《雨》Pluies（1943）、《雪》Neiges（1944）、《风》Vents（1946）
  4. 《航标》Amers（1957）——归法前夕的海洋颂诗
  5. 《编年史》Chronique（1960）、《鸟》Oiseaux（1963，Braque 作插图）、《为分点而歌》Chant pour un équinoxe（1971）、《夜曲》Nocturne（1973）、《旱》Sécheresse（1974）
  6. 《作品全集》Œuvres complètes（Pléiade，1972）——由其本人设计编辑
- **关键时间线**（15 节点）：
  1. 1887-05-31 生于皮特尔角
  2. 1899 "多难之年"后举家返法，定居 Pau
  3. 1904 奥尔特兹结识 Francis Jammes
  4. 1907 父亡，家道暂困
  5. 1910 波尔多大学法学毕业；首部诗集《Éloges》出版
  6. 1911/1912 《Éloges》刊行（1911 版本）；1912 伦敦约翰·多恩俱乐部，遇 Conrad
  7. 1914 入外交部
  8. 1916–1921 驻北京秘书；《阿纳巴斯》成诗
  9. 1921 华盛顿裁军会议；被 Briand 罗致
  10. 1924 《阿纳巴斯》经 Larbaud/Gide 在 NRF 出版
  11. 1932–1940 外交部秘书长（Quai d'Orsay）
  12. 1940 维希褫夺公民身份；流亡华盛顿
  13. 1942–1946 《流放》《雨》《雪》《风》相继问世
  14. 1957 获赠吉昂别墅；1958 与 Dorothy Milburn Russell 结婚
  15. 1960 诺贝尔文学奖；1975-09-20 卒于吉昂半岛

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist poetry | 现代主义诗歌 | 20 世纪法诗重镇 | 封面、核心页 |
| 1 | long poem | 长诗 | 《阿纳巴斯》《风》《航标》等史诗体长诗 | 核心页 |
| 2 | visionary poetry | 幻象诗歌 | 诺奖理由 "in a visionary fashion" | 核心页 |
| 3 | literary translation | 文学翻译 | 译 Pindar；其作被 Eliot 等译入英文 | 翻译页 |
| 4 | poetic prose | 诗性散文 | 《颂歌集》的散文诗质地 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Dorothy Milburn Russell | 无向 | 1958 年结婚，美国人 |
| colleague | Francis Jammes | 无向 | 1904 奥尔特兹结识的诗人挚友 |
| colleague | André Gide | 无向 | NRF 主编时期促成《阿纳巴斯》发表 |
| colleague | Valery Larbaud | 无向 | 挚友，出力促成《阿纳巴斯》出版 |
| colleague | Aristide Briand | 无向 | 1921 看中其才干，1921–32 任其首席助理 |
| colleague | Philippe Berthelot | 无向 | 外交恩主，1932 由其接任外交部秘书长 |
| colleague | T. S. Eliot | 无向 | 1930 年英译《阿纳巴斯》 |
| colleague | Archibald MacLeish | 无向 | 流亡华盛顿时期援手，长信往还 |
| influence | Joseph Conrad | 无向 | 1912 伦敦会面，鼓励其以诗为业 |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：高远、开阔、史诗的季风
- **配色**：主色 **#A31621**（分批文件预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 颂歌与童年 — 加勒比绿 `#1B6B5A`
  - `badgeB` 史诗长诗 — 季风蓝 `#2E6E8E`
  - `badgeC` 外交岁月 — 雾灰蓝 `#5C6B73`
  - `badgeD` 诺奖 — 香槟金 `#C9A227`
- **背景母题**：横向季风线条 + 岛屿轮廓剪影；大量留白呼应"高扬气势"

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 诗人外交官 / Saint-John Perse（Alexis Leger）1887–1975 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名与笔名、国籍、出生地、婚姻、任职、荣誉、核心领域）
03  核心贡献概览 — 现代主义诗歌 / 长诗 / 幻象诗 / 翻译
04  加勒比少年 (1887–1899) — 种植园童年、"多难之年"、举家返法
05  Pau 与波尔多 (1899–1910) — 户外少年、法学、《Pau-Gazette》乐评
06  《颂歌集》与文人圈 (1904–1914) — Jammes、Gide/Larbaud/Claudel、多恩俱乐部与 Conrad
07  北京岁月 (1916–1921) — 道观、戈壁、《阿纳巴斯》成诗（意象图式页）
08  Briand 麾下 (1921–1932) — 华盛顿会议、NRF 出版《阿纳巴斯》、Eliot 英译
09  外交部秘书长 (1932–1940) — Quai d'Orsay、1940 失势（客观简述）
10  流亡组诗 (1940–1957) — 《流放》《雨》《雪》《风》《航标》；"le grand absent"
11  荣归与诺奖 (1957–1960) — 吉昂别墅、1958 婚礼、1960 斯德哥尔摩
12  最后的颂歌 (1960–1975) — 《编年史》《鸟》《为分点而歌》《夜曲》；Pléiade 全集
13  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

**陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名 | 本名 Alexis Leger（又拼 Léger），笔名 Saint-John Perse（亦作 Saint-Leger Leger）——封面用笔名，身份页双名并写；yaml name_en 用 frontmatter 形式 `Saint-John Perse` |
| 家世美化 | 其"古老贵族后裔"自称系本人后来 embellish（美化），实为公证人家庭——按 page.md 写"自称"，勿当史实 |
| 种植园与奴隶制 | 《颂歌集》对家族蓄奴史的回避是学者指出的话题——可客观提及，不作道德评判 |
| 北京经历 | 1916–1921 驻京公使馆秘书；与裕容龄（Nellie Yu Roung Ling）的私人关系按 page.md 客观一笔即可（其说法与对方相左），**不入库** |
| 外交评价 | 1930s 绥靖/洛迦诺体系立场争议只按 page.md 客观转述，**不作政治评价**（政治红线） |
| 维希时期 | 1940 被褫夺勋章与公民身份（战后恢复）——写明"维希政府"所为 |
| 《阿纳巴斯》年份 | 1924 年出版（北京写作期在前）；Eliot 英译 1930；"第三版" Faber & Faber 1959——三个年份勿混 |
| 并非"圣约翰" | 笔名 Saint-John Perse 勿意译成"圣约翰"；通行中译"圣琼·佩斯" |
| 婚年 | 1958 与 Dorothy Milburn Russell 结婚（68 岁），诺奖前两年——勿写"诺奖后" |
| 无载禁写 | 不写家族子嗣（page.md 无载）；不写与 Claudel 的具体合作（仅"结识"与 Cahiers 撰稿，关系太弱不入库） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Alexis Leger | 阿列克西·莱热 | 本名，与笔名双轨 |
| Saint-John Perse | 圣琼·佩斯 | 笔名，通行中译 |
| Anabase | 《阿纳巴斯》 | 希腊语"远征"，勿译"长征" |
| Éloges | 《颂歌集》 | 1910/1911 |
| Exil | 《流放》 | 1942 |
| Vents | 《风》 | 1946 |
| Amers | 《航标》 | 1957 |
| Oiseaux | 《鸟》 | 1963，Braque 插图 |
| Quai d'Orsay | 凯道赛（法国外交部） | 秘书长=头号文官 |
| League of Nations | 国际联盟 | 其外交理念依托 |
| outre-mer / outre-songe | 海外/梦外 | 《颂歌集》核心意象 |
| John Donne Club | 约翰·多恩俱乐部 | 1912 伦敦 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（分批文件预分配）
- **风格**：宏大 / 深远 / 时间纵深
- **匹配理由**："高扬气势"（soaring flight）的史诗长诗与外交生涯的双重纵深，与 Eternals 的宏大时间感同构；流亡与荣归的弧光需要跨世纪的气象承载。
- **备选**：Cinematic Experience（画面感强，但本篇母题以"气势"为先）。

---

> **开始执行。每完成一步汇报。**
> **最重要的事：文学家无公式框——用书影/名句引文框/意象图式；涉政治内容客观简述不评价；每写一页就 make。**
