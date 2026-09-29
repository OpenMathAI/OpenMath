# 文学家立传提示词（OpenLiterature：Hermann Hesse）

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，与数学/物理/化学侧同构）。
- **本实例**：Hermann Karl Hesse（赫尔曼·黑塞），1946 年诺贝尔文学奖得主，德裔瑞士诗人、小说家、画家。
- **设计哲学**：文学家立传以「身份信息页 + 研究领域表」为骨架（与物理学家模板同构），但以**代表作书影 / 名句引文框 / 意象图式**替代物理学的公式框——黑塞的视觉母题是「向内之路」：灵与肉、东方与西方的双重结构。

## 二、背景信息 【人物专属】

- **目标文学家**：Hermann Hesse（1877-07-02 ~ 1962-08-09，享年 85 岁）
- **姓名**：Hermann Karl Hesse ／ 赫尔曼·黑塞
- **诺奖年份**：1946 年诺贝尔文学奖，官方获奖理由（禁止改写）：
  > "for his inspired writings, which while growing in boldness and penetration, exemplify the classical humanitarian ideals and high qualities of style"（表彰其富于灵感的写作，在胆识与洞察力不断深化的同时，体现了古典的人道主义理想与高超的风格）
- **气质关键词**：向内的朝圣者、东西方之间的摆渡人、孤狼与圣徒的书写者
- **设计母题**：**「向内之路」（Weg nach Innen）**——《德米安》的该隐记号、《荒原狼》的魔法剧场门扉（"不为疯人而设"）、《悉达多》的河水与《玻璃珠游戏》的珠戏棋盘；辅以瑞士提契诺的山光水色，构成「双重自我」的视觉语言。
- **本地数据源**：`literature/presentations/pages/20th_century/Hermann_Hesse/page.md`（+ metadata.json、images.txt）
- **Wikipedia**：https://en.wikipedia.org/wiki/Hermann_Hesse （肖像第 0 步下载：infobox 用 File:Hermann_Hesse.jpg，1905 年 Ernst Würtenberger 肖像；备选 c. 1946 照片 File:Hermann_Hesse_1946.jpg）

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇歧义先征求意见。含「研究领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库（MySQL）。

### 第 0 步：事实基准（已核对，以正文为准）

- **生卒**：1877-07-02 生于德意志帝国符腾堡王国黑林山小镇卡尔夫（Calw）～ 1962-08-09 逝于瑞士提契诺州蒙塔尼奥拉（Montagnola），享年 85 岁；葬于 Gentilino 圣阿邦迪奥墓园（挚友兼传记作者 Hugo Ball、指挥家 Bruno Walter 同葬于此）。
- **国籍**：生于德意志帝国（出生时因父亲为爱沙尼亚籍而具德俄双重国籍）；1923 年获瑞士国籍。Nobel 官方口径 Germany / Switzerland。
- **家庭**：外祖父 Hermann Gundert 为巴塞尔传道会传教士、语言学家（编马来语语法与马英词典、参与圣经马来语翻译）；母亲 Marie Gundert 1842 年生于南印度传教站；父亲 Johannes Hesse 1847 年生于俄国爱沙尼亚省 Weissenstein，1893 年接任卡尔夫出版事务所；家庭为士瓦本敬虔派（Pietist）氛围。三段婚姻：Maria Bernoulli（1904–1923，数学世家伯努利家族）、Ruth Wenger（1924–1927，歌手，作家 Lisa Wenger 之女、Méret Oppenheim 之姨母）、Ninon Ausländer（1931–1962，艺术史学者）。三子（Bruno、Heiner、Martin）。
- **教育**：格平根拉丁学校 → 1891 年毛尔布隆修道院福音神学校（1892 年出逃、自杀未遂，经 Bad Boll 神学家 Christoph Friedrich Blumhardt 照护、Stetten 精神病院、巴塞尔男童机构、Cannstatt 文理中学，1893 年通过「一年制考试」结业）；此后埃斯林根书店学徒（三天即辞）、卡尔夫钟塔工厂 14 个月机械学徒、1895 年 10 月图宾根书店学徒。
- **文学师承与影响（仅收 page.md 明载）**：1895 年起读尼采（「激情与秩序的双重冲动」对多数小说影响深重）；德国浪漫派（Brentano、Eichendorff、Hölderlin、Novalis）；歌德、莱辛、席勒、希腊神话；1904 年重新关注叔本华与神智学（引向《悉达多》）；一战心理分析经历中结识卡尔·荣格本人。
- **任职/流亡**：无学院任职；1914 一战自请入伍判不适合作战、任战俘照护；1919 定居提契诺蒙塔尼奥拉 Casa Camuzzi；1931 年迁入友人赞助人 Hans C. Bodmer 为其建造的住宅，终老于此。
- **关键荣誉**：1906 Bauernfeld-Preis；1928 维也纳席勒基金会 Mejstrik-Preis；1936 Gottfried-Keller-Preis；1946 歌德奖 + 诺贝尔文学奖；1947 伯尔尼大学荣誉博士；1950 Wilhelm Raabe 文学奖；1954 Pour le Mérite；1955 德国书业和平奖。
- **核心作品与贡献（4–6 条）**：
  1. 《彼得·卡门青特》（1903/1904，Samuel Fischer 出版，成名作，弗洛伊德私爱读物之一）
  2. 《德米安》（1919，笔名 Emil Sinclair，1917 年 9–10 月三周写就，战后一代的精神圣经）
  3. 《悉达多》（1922，印度与佛教哲学叙事）
  4. 《荒原狼》（1927，魔力剧场）
  5. 《纳尔齐斯与歌尔德蒙》（1930）
  6. 《玻璃珠游戏》（1943，瑞士出版，十一年心血，最后一部长篇）
- **关键时间线（15–20 节点）**：1877 生于卡尔夫 → 1881–1886 随家迁巴塞尔 → 1891 入毛尔布隆神学校 → 1892 危机出逃/自杀未遂 → 1893 结业 → 1894 钟塔工厂学徒 → 1895 图宾根书店学徒、始读尼采 → 1896 首诗〈Madonna〉刊出 → 1898《浪漫之歌》/《午夜后一小时》→ 1899 巴塞尔古旧书店 → 1900 因眼疾免服兵役 → 1901 首次意大利之行 → 1903/1904《彼得·卡门青特》成名、与 Maria Bernoulli 成婚、定居博登湖畔 Gaienhofen → 1906《在轮下》→ 1911 锡兰/荷属东印度之旅 → 1912 迁伯尔尼 → 1914 一战、〈哦，朋友们，不要这种声调〉遭德国报界围攻 → 1915 Rolland 到访声援 → 1916 父亲去世/幼子重病/妻子精神分裂、接受心理分析 → 1917 三周写就《德米安》→ 1919 迁提契诺 Casa Camuzzi、开始作画 → 1922《悉达多》→ 1923 入瑞士籍 → 1924 与 Ruth Wenger 成婚（1927 离异）→ 1927《荒原狼》、Hugo Ball 首部传记 → 1930《纳尔齐斯与歌尔德蒙》→ 1931 与 Ninon 成婚、迁新居 → 1933 助 Brecht/Thomas Mann 流亡、评论推介遭禁犹太作家（含卡夫卡）→ 1943《玻璃珠游戏》瑞士出版 → 1946 歌德奖 + 诺贝尔奖 → 1947 伯尔尼大学荣誉博士 → 1955 德国书业和平奖 → 1962-08-09 逝于蒙塔尼奥拉。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `literature/presentations/20th_century/Hermann_Hesse/`（+ `images/`），Makefile 设 `MAIN=Hermann_Hesse_zh`；肖像下载（curl `-A "Mozilla/5.0"`，file 验证；失败用 Commons Special:FilePath 回退）。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | novel | 长篇小说 | 五大长篇构成其文学主体 | 作品页 |
| 1 | poetry | 诗歌 | 1898《浪漫之歌》起终生写诗 | 早年页 |
| 2 | bildungsroman | 成长小说 | 《德米安》《在轮下》的教育危机母题 | 核心页 |
| 3 | Eastern philosophy | 东方哲学 | 祖父印度经历、叔本华、佛教 →《悉达多》 | 悉达多页 |
| 4 | psychoanalysis and literature | 心理分析与文学 | 荣格式分析塑造《德米安》《荒原狼》 | 荣格页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Friedrich Nietzsche | 影响→黑塞 | 1895 年起阅读，「激情与秩序的双重冲动」影响多数小说 |
| influence | Arthur Schopenhauer | 影响→黑塞 | 1904 年重新关注，引向《悉达多》 |
| influence | Carl Jung | 影响→黑塞 | 一战接受心理分析并结识本人，荣格式分析塑造其创作 |
| influence | Hermann Gundert | 影响→黑塞 | 外祖父，世界文学藏书塑造其世界观 |
| colleague | Romain Rolland | 无向 | 一战论战中公开声援，1915 年到访 |
| colleague | Theodor Heuss | 无向 | 挚友，论战时期给予支持 |
| colleague | Thomas Mann | 无向 | 1933 年流亡途中得其帮助 |
| colleague | Bertolt Brecht | 无向 | 1933 年流亡途中得其帮助 |
| colleague | Hugo Ball | 无向 | 挚友兼传记作者（1927 首部传记） |
| colleague | Miguel Serrano | 无向 | 智利作家外交官，与黑塞和荣格均有通信 |
| colleague | Richard Strauss | 无向 | 《最后四首歌》（1948）采用黑塞三首诗谱曲 |
| spouse | Maria Bernoulli | 无向 | 1904 成婚，数学世家伯努利家族 |
| spouse | Ruth Wenger | 无向 | 1924 成婚，1927 离异，歌手 |
| spouse | Ninon Hesse | 无向 | 1931 成婚（本名 Ninon Ausländer），陪伴至终老 |

#### 4.5.1 入库操作

- `MySQL/data/Hermann_Hesse.yaml` + `cd MySQL && python3 seed_person.py data/Hermann_Hesse.yaml`（幂等）；校验 fields≥4、relations≥2。

### 第 5 步：设计配色 【人物专属】

- **主色**：卡尔夫酒红 `#8B1A1A`（预分配，勿改）；诺奖香槟金 `C9A227`。
- badgeA–D：badgeA 玻璃珠游戏/结构 — 靛蓝 `#4C5FD5`；badgeB 东方之旅 — 青绿 `#0E7C7B`；badgeC 荒原狼/魔力剧场 — 琥珀 `#E07B30`；badgeD 诗歌 — 玫瑰 `#C4204F`。
- 背景母题：柔和气泡 + 细线「门扉」意象（呼应魔法剧场门与向内之路）。

### 第 6 步：规划幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 向内之路的书写者 / Hermann Hesse 1877–1962 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名、国籍、出生地、教育、三段婚姻、任职、荣誉、核心领域）
03  核心作品概览 — 五大长年表书影（卡门青特→德米安→悉达多→荒原狼→玻璃珠游戏）
04  早年：卡尔夫的敬虔派之家 (1877–1895) — 传教士家族、双语世界、尼古拉斯桥
05  毛尔布隆危机与学徒岁月 (1891–1895) — 出逃、自杀未遂、钟塔工厂、图宾根书店
06  浪漫派阅读与初登文坛 (1895–1903) — 尼采、荷尔德林、Novalis、《浪漫之歌》
07  突破：《彼得·卡门青特》与博登湖 (1904–1911) — Fischer 出版、Gaienhofen、弗洛伊德的赏识
08  东方之旅与《悉达多》(1911–1922) — 锡兰/东印度、叔本华与佛教
09  一战与〈哦，朋友们，不要这种声调〉(1914–1919) — 反战檄文、报界围攻、Rolland 声援
10  《德米安》与荣格 — 心理分析、Emil Sinclair 笔名、三周写就
11  蒙塔尼奥拉：Casa Camuzzi 与绘画 (1919–1931) — 克林格索尔的夏天、水彩
12  《荒原狼》与《纳尔齐斯与歌尔德蒙》(1925–1930) — 魔力剧场、双重自我
13  纳粹年代与《玻璃珠游戏》(1931–1946) — 助流亡、推介禁书、十一年心血、诺奖
14  荣誉与认可 — Nobel 1946 · 歌德奖 · 书业和平奖 · 名句引文框
15  遗产：1960s 黑塞热与《最后四首歌》 — 反文化浪潮、一亿册、Strauss 谱曲、结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用，人物专属内容】

- 版式：`p{}` 窄列用 `\newcolumntype{P}[1]`；表内长德文书名断行；frame 标题过长产生隐形 overfull 就缩短标题；文学页用书影/引文框替代公式框。
- 陷阱：

| 陷阱 | 说明 |
|------|------|
| 生卒双值 | frontmatter 有 1877-01-01/1962-01-01 噪声，以正文 07-02/08-09 为准 |
| 国籍口径 | 生于德意志帝国、出生即德俄双重国籍（父为爱沙尼亚裔）、1923 入籍瑞士——勿写「德国作家」单口径 |
| 三段婚姻 | 1904 Maria Bernoulli／1924 Ruth Wenger／1931 Ninon Ausländer，年份与对象勿混 |
| 《德米安》年份 | 1917 年 9–10 月三周写就、1919 停战后以笔名 Emil Sinclair 出版——勿写 1917 出版 |
| 迷幻误读 | 《荒原狼》魔力剧场被反文化解读为迷幻体验，无证据黑塞使用迷幻药——禁写 |
| 纳粹口径 | 从未被官方查禁或焚书，仅被视作「undesirable」；「政治超然」（politics of detachment）口径，勿写公开谴责 |
| 诺奖理由 | 官方原文 "inspired writings … classical humanitarian ideals and high qualities of style"，勿改写 |
| 荣格关系 | page.md 明载「结识本人 + 接受心理分析」；具体治疗细节无载禁写 |
| Strauss | 是斯特劳斯采用黑塞三首诗（1948《最后四首歌》），非二人合作——表述方向勿反 |
| 同名区分 | Hugo Ball（达达主义创始人、其传记作者）勿与音乐家混淆；Theodor Heuss 后为德国首任总统（page.md 未载禁写总统身份） |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Pietism | 敬虔主义 | 士瓦本家庭宗教氛围，非清教 |
| Bildungsroman | 成长小说 | 《在轮下》《德米安》母题 |
| Steppenwolf | 荒原狼 | 1927 长篇，勿与乐队/剧院同名混淆 |
| Magic Theatre | 魔力剧场 | "不为疯人而设" 仅引原文语境 |
| Siddhartha | 悉达多 | 与佛陀同名但为小说人物，需注明 |
| The Glass Bead Game | 玻璃珠游戏 | 又名 Magister Ludi |
| Emil Sinclair | 埃米尔·辛克莱 | 《德米安》笔名（非黑塞真名） |
| Jungian analysis | 荣格心理分析 | 结识本人，接受分析 |
| Casa Camuzzi | 卡穆齐宅 | 蒙塔尼奥拉 1919–1931 居所 |
| Four Last Songs | 《最后四首歌》 | 理查·施特劳斯 1948 声乐套曲，采用黑塞三首诗 |
| Peace Prize of the German Book Trade | 德国书业和平奖 | 1955，勿译「书商和平奖」 |
| Hesse Boom | 黑塞热 | 1960 年代美国反文化阅读浪潮 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**：**Eternals**（分批文件预分配，勿改）
- **匹配理由**：Eternals 的「宏大/深远/长期影响」标签匹配黑塞的身后声誉曲线——生前在德语世界广受阅读、1950 年代一度沉寂、死后经 1960 年代反文化浪潮成为全球现象（累计逾一亿册），是典型的「永恒回响」型作家；曲名的跨越时间感亦贴合《玻璃珠游戏》十一年长跑与「向内之路」的永恒母题。
- **备选（未采用）**：Nostalgia（怀旧感匹配卡尔夫童年，但弱于遗产维度）；Timeless（稳健但已分配他人批次，避撞曲）。
- **本地路径**：对照 `music_audio/curated_tracks.md` 取 Eternals 音频复制到本目录，`make video` 时 ffmpeg `-shortest` 对齐。

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
