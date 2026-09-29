# 文学家立传提示词（Rabindranath Tagore，1913 诺贝尔文学奖）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Kenneth G. Wilson 提示词骨架为母本，适配文学家侧。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人文史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）骨架 + 文学家适配（无公式框——用名句引文框/代表作书影/意象图式替代）。
- **本实例**：Rabindranath Tagore（罗宾德拉纳特·泰戈尔，1913 年诺贝尔文学奖得主，首位非欧洲文学奖得主，《吉檀迦利》作者）。
- **设计哲学**：文学家立传强调「文学领域」的结构化表达与「身份信息页」（Identity / Bio 速览页），核心页用代表作与引文框承载文学成就。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Rabindranath Tagore（1861-05-07 ~ 1941-08-07，享年 80 岁；别号 Bhanusimha，尊称 Gurudeb / Kobiguru / Bishwokobi，"孟加拉的吟游诗人"）
- **官方获奖理由（EN 原文，禁止改写）**：
  > "because of his profoundly sensitive, fresh and beautiful verse, by which, with consummate skill, he has made his poetic thought, expressed in his own English words, a part of the literature of the West"
- **官方获奖理由（中译，取自 `literature/generate_20th_century_list.py` CITATION_ZH，key=("1913","Rabindranath Tagore")，禁止改写）**：
  > 因其诗意深邃、清新而美丽，并以高超的技巧使其以英文表达的诗思成为西方文学的一部分
- **气质关键词**：**孟加拉文艺复兴的旗手、金鸟与飞鸟集、跨文化的对话者**
- **设计母题**：**金色的船与飞鸟（the Golden Boat and wild geese）**。Sonar Tari（金船）+ Balaka（飞雁）取自其诗集意象——用孟加拉乡村水路（Padma 河驳船）与迁徙雁阵承载「乡村孟加拉 → 世界舞台」的视觉叙事；引文框用 Stray Birds 第 292 句（Clouds come floating into my life...）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Rabindranath_Tagore/page.md`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Rabindranath_Tagore
- **肖像**：待下载（page.md 内嵌 1926 Autochrome 彩照、1879 伦敦青年照、1931 德国照、1941 最后留影——取 1926 Autochrome 正装一帧）
- **参考模板**：`literature/presentations/cover/`；成品骨架参照 15 页结构

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载到 `literature/presentations/pages/20th_century/Rabindranath_Tagore/`
- 肖像待下载（第 3 步）
- 事实基准（以 page.md 正文为准）：
  - 生卒（1861-05-07 生于加尔各答 Jorasanko Thakur Bari ~ 1941-08-07 逝于同一宅邸楼上房间，享年 80 岁；frontmatter 生日双值 05-07/05-06 以正文 05-07 为准；最后一首诗 1941-07-30 口授予 A. K. Sen）
  - 国籍（英属印度，British Indian 护照；孟加拉 Pirali Brahmin 家族，原姓 Kushari，祖籍 Bardhaman）
  - 家庭（13 个存活子女中最幼，昵称 Rabi；父 Debendranath Tagore (1817–1905)；母 Sarada Devi (1830–1875) 早逝；兄 Dwijendranath 哲学家诗人、Satyendranath 首位入 ICS 的印度人、Jyotirindranath 音乐家剧作家、姐 Swarnakumari 小说家；嫂 Kadambari Devi 为挚友与强力影响，1884 自杀令其多年悲恸）
  - 婚姻与子女（1883 与 9 岁的 Mrinalini Devi（本名 Bhabatarini，1874–1902）成婚——当时常见做法，客观表述；育五子女，二名夭折，含 Rathindranath Tagore）
  - 教育（主要避课堂：八岁写诗；1873 随父游历印度（Santiniketan/阿姆利则金庙/Dalhousie）；1878 赴布莱顿与伦敦，UCL 短暂读法后离去，自主研读莎士比亚与 Thomas Browne；1880 无学位返孟加拉）
  - 文学师承与影响（Shelaidaha 时期经 Gagan Harkara 熟悉 Baul 游方诗人 **Lalon** 的民歌并致力推广——其诗风的孟加拉乡村民间音乐根基；诗脉上承 15-16 世纪 Vaishnava 诗人、Vyasa 与奥义书 rishi、Bhakti-Sufi 神秘主义者 Kabir、Ramprasad Sen）
  - 任职/机构（1890 起管理 Shelaidaha 庄园（zamindar babu，驾 Padma 驳船巡行）；1901 迁 Santiniketan 办 ashram 实验学校；1918-12-24 Visva-Bharati 奠基、1921 落成，捐诺奖奖金办学；1921 与农业经济学家 Leonard Elmhirst 创立乡村重建学院（后名 Sriniketan））
  - 关键荣誉（Nobel 1913——首位印度籍与非欧洲文学奖得主、第二位非欧洲诺奖得主（继 Roosevelt）；1915 受封 Knight Bachelor，1919 因 Jallianwala Bagh 惨案致函总督 Chelmsford 声明放弃；FRAS；加尔各答大学名誉博士）
  - 争议/事件（1912 英译 Gitanjali 经 Yeats/Pound 等推崇；1916 旧金山险遭印度侨民暗杀未遂；墨索里尼 1926 会面后公开谴责法西斯（Manchester Guarder 文章）；1934 比哈尔地震驳 Gandhi 的"业报"说；1937 昏迷、1940 复发不愈；1937 画作被纳粹从柏林王储宫撤下、1941-42 列入"堕落艺术"清单；2004 诺奖奖章在 Visva-Bharati 被盗，2004-12-07 瑞典学院补赠金/铜复制品）
  - 核心作品与贡献（4-6 条）：Gitanjali（孟加拉 1910 / 英译 Song Offerings 1912）；短篇 Galpaguchchha 三卷 84 篇（1891-95 Sadhana 时期过半），开创孟加拉语短篇文体；长篇 Gora (1907-10)、Ghare Baire (1916)、Chokher Bali (1902-03)、Shesher Kabita (1929)；歌词约 2230 首（Rabindra Sangeet），两首成为印度与孟加拉国国歌、斯里兰卡国歌受其启发；戏剧/舞剧 Valmiki Pratibha (1881)、Visarjan (1890)、Dak Ghar (1912)、Raktakarabi (1926)；六十岁起绘画，巴黎首展，印度国家现代美术馆藏 102 件）
  - 环球旅程（1878–1932 足迹五大洲 30 余国：1912 英美、1916-17 日美、1924 秘鲁/墨西哥/阿根廷（Victoria Ocampo 接待）、1926 欧洲、1927 东南亚（Suniti Kumar Chatterji 随行）、1930 欧美（Hibbert Lectures、与爱因斯坦对谈 1930-04-14、见 Bergson/Frost/Thomas Mann/Shaw/Wells）、1932 波斯/伊拉克、1933 锡兰）
  - 关键时间线（约 18 节点，见第 6 步幻灯片序列年份锚点）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下已有 `Rabindranath_Tagore/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制邻近成品 `Makefile`，设置 `MAIN=Rabindranath_Tagore_zh`、`VIDEO_NAME=Rabindranath_Tagore_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载：1926 Autochrome 彩照优先，Commons `Special:FilePath` 加 `?width=600`
- 可选插图：Gitanjali 1913 Macmillan 书名页、与爱因斯坦 1930 合影、与甘地 1940 圣蒂尼克坦合影、Manasi/金船意象

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | Gitanjali / Manasi / Sonar Tari / Balaka | 核心页 |
| 1 | short story | 短篇小说 | Galpaguchchha 84 篇，开创孟加拉语短篇文体 | 短篇页 |
| 2 | songwriting | 歌曲创作 | Rabindra Sangeet 约 2230 首，两国国歌 | 音乐页 |
| 3 | drama | 戏剧与舞剧 | Dak Ghar、Raktakarabi、Rabindra Nritya Natya | 戏剧页 |
| 4 | painting | 绘画 | 六十岁始画，国家现代美术馆藏 102 件 | 绘画页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Debendranath Tagore | parent | 父亲 (1817–1905)，宗教哲学家，1873 携子游历印度 |
| spouse | Mrinalini Devi | 无向 | 1883 成婚，1902 病逝，育五子女 |
| influence | Lalon | 对方→本人 | Baul 游方诗人民歌深刻影响其诗风，泰戈尔致力推广其歌 |
| influence | Kadambari Devi | 对方→本人 | 嫂子，挚友与强力影响，1884 自尽令其多年悲恸 |
| colleague | William Butler Yeats | 无向 | 为英译 Gitanjali 作序，1912 伦敦推介其诗 |
| colleague | Leonard Elmhirst | 无向 | 1921 共创乡村重建学院（Sriniketan） |
| colleague | Mahatma Gandhi | 无向 | 圣蒂尼克坦接待，就 Swadeshi 运动持保留，1932 调停 Ambedkar 分离选举人争议 |
| colleague | Albert Einstein | 无向 | 1930 对谈，Nature of Reality 札记收入 The Religion of Man 附录 |
| colleague | Romain Rolland | 无向 | 钦佩其 Nationalism in India 的和平主义者，通信多年 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深蓝 `#16324F`（分批文件预分配）
- **配色**：主色 + 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 抒情诗 — 琥珀 `#E07B30`
  - `badgeB` 短篇小说 — 青绿 `#0E7C7B`
  - `badgeC` 歌曲创作 — 玫瑰 `#C4204F`
  - `badgeD` 戏剧与绘画 — 靛蓝 `#4C5FD5`
- **背景母题**：孟加拉水乡驳船剪影 + 雁阵弧线（呼应设计母题）

### 第 6 步：规划幻灯片序列 【人物专属，14-16 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 孟加拉的吟游诗人 / Rabindranath Tagore 1861–1941 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、别号、国籍、出生地、家庭、教育、影响者、机构、荣誉、核心领域）
03  核心贡献概览 — 抒情诗 / 短篇 / 歌曲 / 戏剧 / 绘画
04  Jorasanko 童年 (1861–1873) — 泰戈尔家族与孟加拉文艺复兴、仆人带大、兄姐群像、Kadambari
05  游历与伦敦 (1873–1880) — 随父行旅、金庙 gurbani、Brighton 与 UCL、Bhanusimha 笔名
06  Shilaidaha 岁月 (1890–1901) — Zamindar Babu、Padma 驳船、Manasi、Sadhana 时期与 Galpaguchchha
07  Gitanjali（核心贡献页·引文框替代公式框）— 孟加拉 1910 / 英译 1912、Yeats 序、India Society 限量本
08  诺贝尔 1913 — 首位非欧洲文学奖得主、颁奖词原文、骑士称号 1915 与 1919 放弃（Jallianwala Bagh）
09  圣蒂尼克坦与 Visva-Bharati (1901–1932) — 实验学校、1918 奠基、Sriniketan 乡村重建、树下授课
10  Rabindra Sangeet（音乐页）— 2230 首歌、两国国歌、thumri 与 raga、Baul 之根
11  环球对话者 — Einstein 1930 对谈、Bergson/Mann/Shaw、墨索里尼 1926 与公开谴责
12  绘画的迟到 — 六十岁始画、Malanggan 与 Haida 影响、巴黎首展、被纳粹列为堕落艺术
13  晚年 (1932–1941) — 五卷新作、科学随笔 Visva-Parichay、病榻诗章、1941-08-07 卒于 Jorasanko
14  遗产与结尾 — 全球纪念、译介网络（Gide/Akhmatova/Jiménez）、奖章失窃与复制品
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Tagore 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生卒双值 | 生日 05-07/05-06 双值以正文 05-07 为准；卒日 1941-08-07 无争议 |
| 国别口径 | 获奖时为英属印度（British Raj），名录国家口径 "India (British Raj)"；勿写"印度国歌作者"时的年代错位（Jana Gana Mana 1950 才正式采納） |
| 婚姻表述 | 1883 与 9 岁 Mrinalini Devi 成婚——page.md 原文明载 "this was a common practice at the time"，客观一句带过，不渲染 |
| 与甘地关系 | 既有尊重（1940 接待）也有分歧（Swaraj/Swadeshi 保留、1934 地震"业报"说之争）——双面如实，**不作政治评价** |
| 放弃骑士 | 1919 Jallianwala Bagh 惨案后致函 Chelmsford 放弃；两段信件原文 page.md 均有（选一即可），引用须注出处 |
| 与叶芝的张力 | Yeats 既作序推崇、后又有 "Damn Tagore" 批评（Radice/ Greene 评语亦载）——两面并存，勿只写褒或只写贬 |
| 国歌数量 | 亲作印度、孟加拉国两国国歌；斯里兰卡国歌是"受其启发"；西孟加拉邦邦歌 Banglar Mati Banglar Jol——四个层次勿混 |
| 锡克题材 | 1873 阿姆利则金庙经历与六首锡克题材诗——page.md 专段载明，可设彩蛋页 |
| 引语红线 | Stray Birds 292、最后的生日诗、Bedouin 酋长对谈等均为 page.md 英文原文可引；"profoundly sensitive, fresh and beautiful" 来自 Yeats 序/颁奖词转述，注明归属 |
| Galpaguchchha | 三卷 84 篇、Sadhana 时期（1891-95）写就过半——数字勿混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Gitanjali | 吉檀迦利 | 保留原名，Song Offerings 为英译名 |
| Rabindra Sangeet | 泰戈尔歌曲 | 歌曲体裁专名 |
| Baul | 巴乌尔游方歌手 | 孟加拉民间神秘主义传统 |
| Lalon | 拉隆 | Baul 吟游诗人 |
| Santiniketan | 圣蒂尼克坦 | 静修地与学校 |
| Visva-Bharati | 国际大学 | 字面"印度与世界" |
| zamindar | 田庄主 | 殖民地土地制度名目 |
| Kadambari Devi | 卡丹芭丽 | 嫂子，勿与妻子混淆 |
| Jallianwala Bagh | 阿姆利则惨案 | 1919 事件名 |
| Sadhana | 萨达纳时期 | 1891-95 高产期，杂志名 |
| Galpaguchchha | 短篇集萃 | 84 篇三卷 |
| Shesher Kabita | 最后的诗 | 1929 抒情小说 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Cinematic Experience** — Alex-Productions（分批文件预分配）
- **匹配理由**:
  - "Cinematic Experience" 的史诗跨度匹配其五大洲 30 余国的环球旅程与 80 年生命——驳船、金庙、伦敦沙龙、圣蒂尼克坦树下的授课、与爱因斯坦的对谈，天然是分镜式的影像叙事
  - 曲名的电影感贴合其作品被 Satyajit Ray 改编（Charulata 1964 / Ghare Baire 1984）的银幕缘分
  - 悠长的弦乐与人声空间感适配 Rabindra Sangeet 的歌唱传统与 Gitanjali 的祈祷气质
- **本地路径**: 从 `music_audio/` 曲库复制对应曲目到 `presentations/20th_century/Rabindranath_Tagore/`（对照 `curated_tracks.md`）
- **时长**: 按页数 × 7 秒估算，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Rabindranath_Tagore/page.md` | 本地 Wikipedia 正文（事实基准，628 行长文须通读） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Rabindranath_Tagore.yaml` | 社会关系/领域入库 yaml（与本文件同步） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
