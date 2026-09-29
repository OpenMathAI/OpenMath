# 文学家立传提示词（OpenLiterature：Boris Pasternak）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Boris Pasternak（1958 诺贝尔文学奖，被迫拒奖的俄罗斯诗人）为传主。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）+ 数学家/化学家侧黄金骨架的文学适配版。
- **本实例**：Boris Leonidovich Pasternak（鲍里斯·列昂尼多维奇·帕斯捷尔纳克）。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」骨架，但**无公式框**——以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Boris Pasternak（1890-02-10 ~ 1960-05-30，享年 70 岁）
- **气质关键词**：**抒情诗的雪暴、史诗的守夜人、拒领诺奖的诗人** —— 1958 诺贝尔文学奖获奖理由：
  > 表彰其在当代抒情诗与伟大的俄罗斯史诗传统领域的重要成就（官方 EN："for his notable achievement in both contemporary poetry and the field of the great Russian epic tradition"）
- **设计母题**：**雪原与烛火（Snow & Candle）**。佩列杰尔基诺的雪、《日瓦戈医生》中的烛光与哈姆雷特独白——用冷白、烛金与深蓝构成视觉语言。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Boris_Pasternak/page.md`（Wikipedia 全文）
  - `literature/presentations/pages/20th_century/Boris_Pasternak/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Boris_Pasternak
- **肖像**：第 0 步待下载（1959 年肖像，images.txt / Commons 回退；404 则装饰圆占位）。

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：研究领域（第 4 步）+ 社会关系（第 4.5 步）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。
> **政治红线**：涉苏内容（拒奖事件、大清洗、古拉格）只按 page.md 客观事实简述，**不作政治评价、不展开政治叙事**。

### 第 0 步：事实基准 【人物专属，已核对】

- **生卒**：1890-02-10（儒略历 01-29）生于莫斯科～ 1960-05-30 卒于佩列杰尔基诺（Peredelkino，肺癌，享年 70 岁）
- **国籍**：俄罗斯帝国 → 苏联（变迁分两条）
- **家庭**：父 **Leonid Pasternak** 后印象派画家（莫斯科绘画雕塑建筑学院教授，曾为托尔斯泰著作插图）；母 Rosa Kaufman 音乐会钢琴家；弟 Alex、妹 Lydia（Pasternak Slater）与 Josephine；1922 与 Evgeniya Lurye 结婚（1931 离婚，子 Yevgeny），1931 与 Zinaida Neuhaus 结婚；1946 起与 Olga Ivinskaya 为终身伴侣（育有事实上的关系，1949 年她被捕流产）
- **教育**：莫斯科音乐学院（作曲，1910 中途退学）；马尔堡大学（师从新康德主义者 **Hermann Cohen**、**Nicolai Hartmann**、**Paul Natorp**）
- **文学师承与影响**：家为文化沙龙——**Leo Tolstoy** 至交（托尔斯泰主义运动）、**Rachmaninoff / Scriabin / Rilke / Shestov** 常客；早年诗受 **Rilke、Lermontov、Pushkin** 及德语浪漫派影响（明载）；属俄国未来主义"Centrifuge"小组；与 **Rilke、Tsvetayeva** 1920s 三方通信；其诗改写了 Mandelstam、Tsvetayeva 等人的诗歌（明载）
- **任职/经历**：一战在佩尔姆附近化工厂任职（日后《日瓦戈医生》素材）；内战期间留居莫斯科卖书买面包；莫斯科空袭时任消防瞭望员；1943 获准赴前线读诗
- **关键荣誉**：1958 诺贝尔文学奖（**被政府强迫拒领**；1989 年由子 Yevgeny 代领）；Bancarella 文学奖；"保卫莫斯科"奖章等
- **核心作品与贡献**（4–6 条）：
  1. 《生活，我的姊妹》My Sister, Life（1917 年作，1922 年柏林出版）——革新俄语诗歌
  2. 《超越障碍》（1916）/《主题与变奏》（1917）/《第二次诞生》（1932）
  3. 《日瓦戈医生》Doctor Zhivago（1955 完成；苏联拒发，1957 米兰 Feltrinelli 出版；1988 年起入俄语学校课程）
  4. 自传性散文《安全证》Safe Conduct、《柳威尔斯的童年》
  5. 译作：莎士比亚（哈姆雷特/奥赛罗/李尔王等）、歌德《浮士德》、席勒、卡尔德隆、裴多菲、魏尔伦、里尔克
  6. 音乐：1909 《钢琴奏鸣曲》（斯克里亚宾影响）
- **关键时间线**（15 节点）：
  1. 1890-02-10 生于莫斯科富有的犹太家庭
  2. 1904–1908 波恰伊夫修道院寄读（同窗 Minchakievich，后成斯特列利尼科夫原型素材）
  3. 1903–1910 莫斯科音乐学院作曲（受 Scriabin 激励）
  4. 1910 马尔堡大学哲学（Cohen/Hartmann/Natorp）
  5. 1912 向 Ida Wissotzkaya 求婚被拒（诗《马尔堡》）
  6. 1914 加入未来主义 Centrifuge；首批诗集
  7. 1917 一战化工厂任职；《生活，我的姊妹》成诗
  8. 1917 十月革命后选择留俄
  9. 1922 柏林出版《生活，我的姊妹》；与 Evgeniya Lurye 结婚
  10. 1931 与 Zinaida Neuhaus 结婚；自传《安全证》
  11. 1934 Mandelstam 朗诵《斯大林讽刺诗》；Pasternak 向 Bukharin 求情；斯大林电话
  12. 1937 拒签支持处决的联名声明（"别动这个云中居民"）
  13. 1946 结识 Olga Ivinskaya（拉拉原型）；《日瓦戈医生》写作
  14. 1955–1957 小说完成→Novy Mir 拒刊→米兰出版→1958-10-23 获诺奖→10-29 被迫拒领
  15. 1960-05-30 卒于佩列杰尔基诺；葬礼成自发示威（有人朗诵禁诗《哈姆雷特》）；1989 子代领诺奖

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | 诺奖理由主体，《生活，我的姊妹》 | 封面、核心页 |
| 1 | epic novel | 史诗小说 | 诺奖理由另一半：《日瓦戈医生》与"伟大的俄罗斯史诗传统" | 核心页 |
| 2 | literary translation | 文学翻译 | 莎士比亚/歌德/卡尔德隆等，供家计亦成经典 | 翻译页 |
| 3 | Russian Futurism | 俄国未来主义 | Centrifuge 小组成员 | 早年页 |
| 4 | autobiographical prose | 自传性散文 | 《安全证》《柳威尔斯的童年》 | 散文页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Evgeniya Lurye | 无向 | 1922 结婚，1931 离婚 |
| spouse | Zinaida Neuhaus | 无向 | 1931 结婚 |
| influence | Leo Tolstoy | 无向 | 家庭至交，托尔斯泰主义运动 |
| influence | Rainer Maria Rilke | 无向 | 家庭常客、最爱诗人、1920s 三方通信 |
| influence | Marina Tsvetayeva | 无向 | 1920s 三方通信，其诗风被《生活，我的姊妹》改写 |
| influence | Olga Ivinskaya | 无向 | 1946 起终身伴侣与文学助手，《日瓦戈医生》拉拉原型 |
| colleague | Osip Mandelstam | 无向 | 1934 听其朗诵讽刺诗后为其奔走 |
| colleague | Vladimir Mayakovsky | 无向 | 密友，1920s 后期因艺术观疏远 |
| colleague | Anna Akhmatova | 无向 | 日瓦戈事件期间与其深交 |
| colleague | Rabindranath Tagore | 无向 | 与 Ivinskaya 合作译其诗作入俄语 |
| controversy | Alexander Solzhenitsyn | 无向 | 在《橡子和牛犊》中批评其拒奖与致赫鲁晓夫信 |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：雪暴、烛火、克制的哀恸
- **配色**：主色 **#372A75**（分批文件预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 抒情诗 — 雪白蓝 `#7E96C4`
  - `badgeB` 史诗小说 — 烛金 `#C9A227`
  - `badgeC` 翻译 — 鼠尾草绿 `#6E8B74`
  - `badgeD` 诺奖与拒领 — 深紫 `#5C3A6E`
- **背景母题**：细雪点 + 一枚暖烛光晕；克制、留白多

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 抒情与史诗 / Boris Pasternak 1890–1960 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍变迁、父母、教育、伴侣、荣誉、核心领域）
03  核心贡献概览 — 抒情诗 / 史诗小说 / 翻译 / 自传散文
04  艺术家之家 (1890–1910) — 画家父亲、钢琴家母亲、托尔斯泰与斯克里亚宾
05  音乐与哲学 (1910–1914) — 音乐学院退学、马尔堡新康德主义、《马尔堡》诗
06  未来主义与《生活，我的姊妹》(1917–1922) — Centrifuge、柏林出版、革新俄诗
07  1920s–1930s — 三方通信、风格转型、《第二次诞生》、与 Mayakovsky 疏远
08  翻译岁月 — 莎士比亚/浮士德/裴多菲；"我沉默是因为不给我出版"
09  Olga Ivinskaya (1946–) — 拉拉原型、其被捕与流放（客观简述）
10  《日瓦戈医生》(1955–1957) — 苏联拒刊、米兰 Feltrinelli、世界畅销
11  1958 诺贝尔与拒领 — 获奖电文、被迫拒领、1989 代领（客观简述）
12  最后的雪 (1958–1960) — 《天气放晴》《盲美人》未竟、葬礼示威、遗产
13  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

**陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生卒双历 | 1890-02-10（格里历）/儒略历 01-29；yaml 取 1890-02-10 |
| 拒奖表述 | 必须写"被苏联政府强迫拒领"（page.md 口径 "forced him to decline"），1989 年由子 Yevgeny 代领——勿写"自愿放弃" |
| 获奖理由 | "当代抒情诗 + 伟大的俄罗斯史诗传统"两半并列，勿只写《日瓦戈医生》 |
| CIA 出版线 | 《日瓦戈医生》出版含 CIA 秘密购书运作——按 page.md 客观一笔带过，不展开 |
| Ivinskaya 关系 | 终身伴侣而非配偶（Pasternak 未离 Zinaida）——关系类型用 influence，勿写 spouse |
| 同名区分 | Boris Pasternak 与其父 Leonid Pasternak；Son "Yevgeny Borisovich"；勿混 |
| 斯大林电话/清洗 | 1934 电话与 1937 拒签按 page.md 客观叙述，不加渲染、不作评价 |
| 引语红线 | "别动这个云中居民"等引语 page.md 有英文原文可用；俄文诗句须附英译或用忠实转述 |
| 《哈姆雷特》诗 | 葬礼上被朗诵的是 Pasternak 的禁诗《哈姆雷特》（本人所作），非莎士比亚 |
| 无载禁写 | 不写"获 1946-1950/1957 年度提名"细节之外的自创时间线；不写 Nobel lecture（未赴席） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| My Sister, Life | 《生活，我的姊妹》 | 1917 年作 1922 年出版 |
| Doctor Zhivago | 《日瓦戈医生》 | 1957 米兰首发 |
| Yuri Zhivago | 尤里·日瓦戈 | 主人公，与作者勿混 |
| Lara | 拉拉 | 原型 Olga Ivinskaya |
| Hamlet | 《哈姆雷特》 | Pasternak 诗作/莎剧译作双重身份，注意区分 |
| Peredelkino | 佩列杰尔基诺 | 疗养地与墓地 |
| Centrifuge | "离心机"小组 | 俄国未来主义分支 |
| neo-Kantian | 新康德主义 | 马尔堡学派 Cohen/Natorp/Hartmann |
| samizdat | 地下出版 | 《日瓦戈医生》苏联境内流传方式 |
| Feltrinelli | 费尔特里内利 | 米兰出版商 |
| Tolstoyan | 托尔斯泰主义 | 家庭信仰背景 |
| safe conduct | 《安全证》 | 自传 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（分批文件预分配）
- **风格**：悲怆 / 深沉 / 历史
- **匹配理由**：拒奖事件的悲剧重量、雪原葬礼与烛火意象，与 Tragedy 的悲怆质感一致；但须避免煽情——剪辑时以冷色留白平衡。
- **备选**：Through the Darkness（氛围合，但已在同项目多处使用）。

---

> **开始执行。每完成一步汇报。**
> **最重要的事：文学家无公式框——用书影/名句引文框/意象图式；涉苏内容客观简述不评价；每写一页就 make。**
