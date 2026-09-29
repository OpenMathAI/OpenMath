# 文学家立传提示词（Giorgos Seferis）

> **OpenLiterature 人物专属立传提示词**：Giorgos Seferis（乔治·塞菲里斯，1963 诺贝尔文学奖，希腊，首位希腊诺奖作家）。
> 执行 agent 按第三部分第 0–9 步逐步执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Giorgos Seferis（本名 Georgios Seferiadis），20 世纪最重要希腊诗人之一、职业外交官。
- **设计哲学**：文学家立传无公式框，以**代表作书影、名句引文框、意象图式**替代物理公式表达；必须有「身份信息页」（Identity / Bio 速览页），务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Giorgos Seferis（1900-03-13 [儒略历 02-28] ~ 1971-09-20，享年 71 岁；卒日 metadata 有 09-19/09-20 两值，以正文 09-20 为准）
- **官方获奖理由（Nobel 官方 EN 原文 + 名录中译，禁止改写）**：
  > "for his eminent lyrical writing, inspired by a deep feeling for the Hellenic world of culture"
  > 「表彰其杰出的抒情写作，由对希腊文化世界的深厚感情所激发」（1963 授予）
- **气质关键词**：**流亡的抒情者、希腊声音的守夜人、诗人外交官**。
- **设计母题**：**海与乡愁（Sea & Exile）**。士麦那失落的童年、奥德修斯的返乡航程、爱琴海的蓝——用海平线、船影与大理石头像（*Mythistorema* 名句意象）构成视觉母题。
- **本地数据源**：`literature/presentations/pages/20th_century/Giorgos_Seferis/page.md`（+ metadata.json / images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Giorgos_Seferis
- **肖像**：第 0 步待下载（images.txt 有 1921 照、1963 诺奖照等真实照片可用）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；封面 `\input` 项目共享首页。

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，直接使用）

- 生卒：1900-03-13 生于奥斯曼帝国艾丁州乌尔拉（Skala，士麦那/伊兹密尔近郊）~ 1971-09-20 逝于雅典（肺炎，两个月前溃疡手术后中风加重）；葬雅典第一公墓，葬礼上万人高唱狄奥多拉基斯为其诗作《拒绝》谱写的禁歌。
- 本名 Georgios Seferiadis，Seferis 为笔名；希腊语写作，通法语/英语。
- 家庭：父 Stelios Seferiadis——律师、后任雅典大学教授，兼诗人与翻译家，坚定的维尼泽洛斯派、主张民众语（demotic）取代官方语（katharevousa）——两者均影响其子。妻 Maria Zannou（'Maro'），1941-04-10 成婚（德军入侵希腊前夜）。
- 教育：1914 举家迁雅典完成中学 → 巴黎索邦大学法学 1918–1925。
- 流亡创伤：1922-09 士麦那陷落于土耳其军队，全家逃离安纳托利亚，直至 1950 才重访；「童年家园的流亡感」成为其诗歌底色，集中于奥德修斯母题。
- 外交生涯：1926 入希腊外交部 → 英国（1931–1934）→ 阿尔巴尼亚（1936–1938）→ 二战随流亡政府辗转克里特/埃及/南非/意大利 → 1944 回解放后的雅典 → 安卡拉（1948–1950）→ 伦敦（1951–1953）→ 兼驻黎巴嫩/叙利亚/约旦/伊拉克公使（1953–1956）→ **驻英国大使（1957–1961）**，雅典退休。
- 关键荣誉：**Nobel Literature 1963（首位希腊得主，其后为 1979 Elytis）**；四度提名（1955 Jenkins、1961 T. S. Eliot、1962 Johnson+Trypanis、1963 Johnson 获选）；1963 年其他终选人 Auden/Neruda/Beckett/三岛由纪夫/Sandemose；荣誉博士：Cambridge（1960）、Oxford（1964）、Thessaloniki（1964）、Princeton（1965），另有 Aix-Marseille doctor honoris causa。
- 核心作品（4–6 条）：*Mythistorema*（《神话与历史》，1935，代表作）；*Strophe*（1931，首部诗集）；航海日志三部曲 *Log Book I/II/III*（1940/1944/1955）；*The Thrush*（1947）；*Three Secret Poems*（1966）；散文三卷《试论》（*Dokimes*）与身后出版的九卷日记《日子》（1975–2019）。
- 关键时间线（15–20 节点）：1900 生乌尔拉 → 1914 迁雅典 → 1918–1925 索邦法学 → 1922 士麦那陷落、全家流亡 → 1925 回雅典 → 1926 入外交部 → 1931 *Strophe*、驻英 → 1932 *The Cistern* → 1935 *Mythistorema* → 1936–38 阿尔巴尼亚 → 1940 *Book of Exercises*/*Log Book I* → 1941-04-10 婚 Maria Zannou、德军入侵 → 1941–44 流亡政府随行 → 1944 *Log Book II* → 1947 *The Thrush* → 1948–50 安卡拉 → 1950 重访士麦那 → 1953 首访塞浦路斯、结束六年沉寂 → 1955 *Log Book III*、驻中东四国 → 1957–61 驻英大使 → 1960 剑桥荣誉博士 → 1963-10 诺奖、12-10 受奖演说（俄狄浦斯与斯芬克斯「人」之答）→ 1966 *Three Secret Poems* → 1967 军政府上台 → 1969-03-28 BBC 声明「This anomaly must end」→ 1971-09-20 逝于雅典 → 1974 军政府倒台（塞菲里斯未能亲见）→ 2004 雅典奥运开幕式引用 *Mythistorema* 名节。
- 受奖演说名句（page.md 有英文原文，可引用）："When on his way to Thebes Oedipus encountered the Sphinx, his answer to its riddle was: 'Man'. That simple word destroyed the monster. We have many monsters to destroy. Let us think of the answer of Oedipus."

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modern Greek poetry | 现代希腊诗歌 | 20 世纪希腊最重要诗人之一 | 核心贡献页 |
| 1 | lyric poetry | 抒情诗 | 诺奖理由核心：杰出的抒情写作 | 核心贡献页 |
| 2 | modernism | 现代主义 | Generation of the '30s 代表人物 | 流派页 |
| 3 | literary translation | 文学翻译 | 译介西方诗歌（*Antigraphes* 1965 等） | 翻译页 |
| 4 | literary essay | 文学随笔 | 三卷 *Dokimes* 与九卷日记《日子》 | 随笔页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Maria Zannou | 无向 | 1941-04-10 成婚（德军入侵希腊前夜），昵称 Maro |
| parent-child | Stelios Seferiadis | 本人→对方 | 父：律师/雅典大学教授，兼诗人翻译家，其维尼泽洛斯立场与民众语主张影响其子 |
| influence | Constantine P. Cavafy | 对方→本人 | page.md 明载对其影响深远的希腊诗人 |
| influence | T. S. Eliot | 对方→本人 | page.md 明载影响其诗歌；1961 诺贝尔提名者 |
| influence | Ezra Pound | 对方→本人 | page.md 明载影响其诗歌 |
| colleague | Philip Sherrard | 无向 | 英译者（*Collected Poems*），1946–1971 与其持续通信 |
| colleague | Mikis Theodorakis | 无向 | 作曲家，为其诗《拒绝》谱曲，1971 葬礼上万人传唱（时为禁歌） |

入库：`MySQL/seed_person.py data/Giorgos_Seferis.yaml`（幂等，QID 匹配）。

### 第 5 步：配色方案

- 主色：深青蓝 `#0B5351`（爱琴海深水与大理石冷光）；辅助：诺奖香槟金 `C9A227`。
- badgeA 抒情诗 — 海蓝 `#1B5E8C`；badgeB 现代主义 — 石灰 `#6E7B7B`；badgeC 翻译 — 赭金 `#8F7420`；badgeD 随笔 — 暗紫 `#52307C`。
- 背景母题：海平线细线、大理石头像剪影、飘散的诗行（低饱和，勿喧宾夺主）。

### 5.1 格式硬要求 【★ 必须满足】

1. 封面右上角肖像 + 细边框 + 姓名小字注；顶部/底部明示国籍（Greece）。
2. **身份信息页**：封面之后、核心贡献之前，左头像右信息网格（生卒/本名与笔名/国籍/教育/外交官经历/主要荣誉/核心领域）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。
4. 名句引文框替代公式框：1963 受奖演说俄狄浦斯句与 *Mythistorema* 大理石头像名节（page.md 有英文原文）。

### 第 6 步：幻灯片序列（14 页）

```
00 OpenLiterature 项目首页（共享封面 \input）
01 封面 — 希腊的抒情之声 / Giorgos Seferis 1900–1971 + 四色 badge + 右上头像 + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 现代希腊诗歌 / 抒情诗 / 现代主义 / 翻译与随笔
04 士麦那的童年与失落（1900–1922）— 乌尔拉 Skala、父亲的语言之争、1922 流亡
05 索邦与归途（1918–1926）— 巴黎法学、雅典入外交部
06 《神话与历史》专页 — 1935、奥德修斯母题、大理石头像（引文框）
07 航海日志三部曲（1940–1955）— 战时流亡政府岁月入诗
08 塞浦路斯与乡愁（1953–1959）— Log Book III、六年沉寂的终结
09 诗人外交官 — 从伦敦到驻英大使（1957–1961）
10 诺奖 1963 — 首位希腊得主、终选名单、受奖演说（俄狄浦斯引文框）
11 翻译与随笔 — Dokimes 三卷、日记《日子》
12 抗争晚年 — 1967 军政府、1969 BBC 声明、1971 葬礼与《拒绝》
13 遗产 — 2004 雅典奥运开幕式、伦敦蓝牌故居、Keeley/Sherrard 译本
14 结尾
```

### 第 7–8 步：Beamer 源码与布局检查

- 每页 `\newcommand{\xxxslide}` 定义；骨架复用 Kenneth_G_Wilson_zh.tex。
- 每写完一页 `latexmk -c` 清理后 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查

**Seferis 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日历法 | 公历 1900-03-13（儒略历 02-28）；infobox 表格行作 February 28 为旧历，以 N.S. 03-13 为准并标注 |
| 卒日 | 1971-09-20（正文），metadata 有 09-19 噪声值 |
| 驻英大使任期 | 导语作 1957–1962、正文作 1957–1961（退休前最后一任）——两说并存，页面以正文 1961 卸任为口径并注 |
| 流亡家园 | 乌尔拉（Skala）在士麦那/伊兹密尔近郊；1922 希土战争士麦那陷落，全家逃离——客观史实简述，不展开战争叙事 |
| 首位希腊诺奖 | 1963 首位希腊文学奖得主，其后 1979 Elytis——「首位」有载可写 |
| 军政府红线 | 1967–1974 军政府与 1969 BBC 声明：只按 page.md 客观简述（审查/拘押/ torture 一句带过），不作政治评价；塞浦路斯争端只写「投入外交努力」不展开 |
| Theodorakis 禁歌 | 葬礼传唱的是其时被禁的《拒绝》谱曲——「禁」指当时状态，勿写成「永久禁令」 |
| 提名人 | 四次提名人 Jenkins/Eliot/Johnson/Trypanis 为诺奖档案事实，写进事实页可，勿据此建关系（Johnson 等不建 colleague） |
| 终选人 | 1963 其他五名终选人含三岛由纪夫等，仅列名勿展开 |
| 无载禁写 | 与 Eliot/Cavafy/Pound 为「影响」明载，但无师承交往细节，勿写「受教于」；不给 Keeley/Sherrard 编造挚友情谊（Sherrard 仅通信明载） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Mythistorema | 《神话与历史》 | 通行译名，勿拆成「神话史」 |
| Log Book | 《航海日志》 | 三部曲 I/II/III |
| Strophe | 《转折》 | 1931 首部诗集 |
| Generation of the '30s | 三十年代一代 | 希腊现代主义群体 |
| demotic | 民众语 | 与 katharevousa（正式语）相对 |
| Smyrna | 士麦那 | 今伊兹密尔 |
| Hellenic world of culture | 希腊文化世界 | 诺奖理由核心词 |
| eminent lyrical writing | 杰出的抒情写作 | 诺奖理由核心词 |
| Dokimes | 《试论》 | 随笔三卷 |
| Denial | 《拒绝》 | 诗名，Theodorakis 谱曲 |

---

## 四、背景音乐建议

- **选定曲目**：**Timeless**（分批文件预分配）。
- **匹配理由**：沉稳/长期纲领气质匹配「希腊文化连续性中的人文主义」这一诺奖理由的纵深；纪录片感贴合外交官-流亡者-守夜人三重身份的缓慢命运。
- **备选**（未采用）：Nostalgia（乡愁感强但受众与史诗感不足）、Eternals（宏大但缺抒情）。
- **本地路径**：按 `music_audio/curated_tracks.md` 索引拷贝至 `presentations/20th_century/Giorgos_Seferis/Timeless.wav`。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Giorgos_Seferis/page.md` | 事实基准（唯一来源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录与中译理由 |
| `MySQL/data/Giorgos_Seferis.yaml` | 入库 yaml（本提示词第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
