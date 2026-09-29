# 文学家立传提示词（OpenLiterature：André Gide）

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，与数学/物理/化学侧同构）。
- **本实例**：André Paul Guillaume Gide（安德烈·纪德），1947 年诺贝尔文学奖得主，法国作家、「文坛斗士」。
- **设计哲学**：文学家立传以「身份信息页 + 研究领域表」为骨架（与物理学家模板同构），但以**代表作书影 / 名句引文框 / 意象图式**替代公式框——纪德的视觉母题是「镜中镜」（mise en abyme）与「窄门」：真我与面具、戒律与欲望的永恒对峙。

## 二、背景信息 【人物专属】

- **目标文学家**：André Gide（1869-11-22 ~ 1951-02-19，享年 81 岁）
- **姓名**：André Paul Guillaume Gide ／ 安德烈·纪德
- **诺奖年份**：1947 年诺贝尔文学奖，官方获奖理由（禁止改写）：
  > "for his comprehensive and artistically significant writings, in which human problems and conditions have been presented with a fearless love of truth and keen psychological insight"（表彰其广博而具艺术意义的写作，以无畏的爱真理之心与敏锐的心理洞察呈现人的问题与处境）
- **气质关键词**：无畏的爱真理者、自我的审问者、法国文坛的良心
- **设计母题**：**「镜中镜」（mise en abyme）与「窄门」**——《伪币犯》的嵌套结构、《窄门》的光缝意象、《日记》的终生自省；辅以诺曼底居维尔墓地与刚果旅途地图，构成「真我之争」的视觉语言。
- **本地数据源**：`literature/presentations/pages/20th_century/André_Gide/page.md`（+ metadata.json、images.txt）
- **Wikipedia**：https://en.wikipedia.org/wiki/André_Gide （肖像第 0 步下载：infobox 用 File:Gide_1920_cropped.jpg（Ottoline Morrell 摄 1924）或 1893 照片 File:Gide_1893.jpg；备选 Paul Albert Laurens 1924 油画像）

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇歧义先征求意见。含「研究领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库（MySQL）。

### 第 0 步：事实基准（已核对，以正文为准）

- **生卒**：1869-11-22 生于巴黎（法兰西第二帝国）～ 1951-02-19 逝于巴黎，享年 81 岁；葬于滨海塞纳省居维尔（Cuverville）公墓。frontmatter 死亡日期有 1951-12-19/1922-02-19 噪声，以正文 02-19 为准。
- **国籍**：法国（终其一国）。
- **家庭**：巴黎新教中产家庭；父 Jean Paul Guillaume Gide 为巴黎大学法学教授（1880 年去世，时纪德 11 岁）；母 Juliette Maria Rondeaux；叔父为政治经济学家 Charles Gide；父系祖上是 16 世纪改宗新教而离意赴法的 Guido 家族。1895 年母丧后与表妹 Madeleine Rondeaux 成婚（婚姻未圆，1938 年妻逝）；1923 年与 Elisabeth van Rysselberghe 生女 Catherine Gide（唯一血亲后代，呼其为「白衣夫人」）。1916 年（约 47 岁）与 15 岁的 Marc Allégret 相恋，携其赴伦敦，妻 Madeleine 焚毁其全部书信报复。
- **教育**：École alsacienne；Lycée Henri-IV（infobox Education）。
- **文学师承与影响（仅收 page.md 明载）**：早年属象征派；1895 年在巴黎结识流亡的爱尔兰剧作家 Oscar Wilde（1895 年阿尔及尔重逢）；1907 年泽西岛与 Jacques Copeau、Théo van Rysselberghe 同游；1923 年著陀思妥耶夫斯基论；1920 年代成为加缪与萨特等人的精神启发者。
- **任职/流亡**：1896 年当选诺曼底拉罗克-班雅尔（La Roque-Baignard）市长；1908 年与友人共创《新法兰西评论》（NRF）；1939 年成为首位在世作者入选「七星文库」（Bibliothèque de la Pléiade）；1942 年离法赴非洲，1942-12 起居突尼斯，1943-05 突尼斯光复后转阿尔及尔至二战结束。
- **关键荣誉**：1947 诺贝尔文学奖；哥特铭牌（Goethe Plaque of the City of Frankfurt）；歌德艺术与科学奖章；上半世纪最佳小说大奖（infobox award_received，正文未载年份禁写）。
- **核心作品与贡献（4–6 条）**：
  1. 《人间食粮》（Les nourritures terrestres，1897，青年一代的自由宣言）
  2. 《背德者》（The Immoralist，1902）与《窄门》（Strait Is the Gate，1909，欲望与戒律的双生对题）
  3. 《梵蒂冈地窖》（Les caves du Vatican，1914，英语版名 Lafcadio's Adventures，「掷币入海」的无动机行为）
  4. 《田园交响曲》（La Symphonie Pastorale，1919）
  5. 《伪币犯》（Les faux-monnayeurs，1925，唯一长篇「全知小说」，mise en abyme 结构）
  6. 《刚果之行》（Voyage au Congo，1927）与《乍得归来》（Retour du Tchad，1927）——抨击大型特许制殖民剥削，推动法国反殖民思潮；《从苏联归来》（Retour de l'U.R.S.S.，1936）与《续从苏联归来》（1937）
- **关键时间线（15–20 节点）**：1869 生于巴黎 → 1880 父逝 → 1891 处女作《安德烈·瓦尔特笔记》→ 1893–1894 北非之行、接纳自我 → 1895 结识 Wilde/阿尔及尔重逢、母丧后与表妹成婚 → 1896 当选市长 → 1897《人间食粮》→ 1902《背德者》→ 1907 泽西岛（写《窄门》第二章）→ 1908 共创 NRF → 1909《窄门》→ 1914《梵蒂冈地窖》→ 一战访英（友人 Rothenstein）、与 Du Bos 同办 Foyer Franco-Belge 救济比法难民 → 1916 与 Marc Allégret 相恋、赴伦敦、妻子焚信 → 1918 结识 Dorothy Bussy → 1919《田园交响曲》→ 1923 女儿 Catherine 出生/著陀氏论 → 1924《伪币犯》前夜：《科里东》公开版遭谴责、无缘法兰西学术院；自传《如果种子不死》/首出康拉德《黑暗的心》《吉姆爷》法译本 → 1925《伪币犯》→ 1926–1927 赤道非洲之行（Marc Allégret 同行）→ 1930《波瓦蒂埃幽禁记》→ 1930 年代同情共产主义（从未入党）、力营救 Victor Serge → 1936 应邀访苏、高尔基葬礼致辞、《从苏联归来》→ 1937《续从苏联归来》→ 1939 首位在世作者入七星文库 → 1938 妻逝（后作《于今且在你之中》追忆）→ 1942–1945 突尼斯/阿尔及尔 → 1947 诺贝尔奖 → 1951-02-19 逝于巴黎 → 1952 作品列入天主教会《禁书目录》。
- **晚年定论**：1946 年答 Pierre Herbert「若只留一书则为《日记》」；讣闻称其为「法兰西在世最伟大的文人」。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `literature/presentations/20th_century/André_Gide/`（+ `images/`），Makefile 设 `MAIN=André_Gide_zh`；肖像下载（curl `-A "Mozilla/5.0"`，file 验证；失败用 Commons Special:FilePath 回退）。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | novel | 长篇小说 | 《背德者》《窄门》《伪币犯》等虚构巅峰 | 作品页 |
| 1 | essay | 随笔/论辩文 | 《科里东》《从苏联归来》的论辩书写 | 论辩页 |
| 2 | autobiography | 自传 | 《如果种子不死》《于今且在你之中》 | 自传页 |
| 3 | drama | 戏剧 | 「偶一为之的剧作家」与萨特/加缪一代 | 戏剧页 |
| 4 | travel writing | 旅行文学 | 《刚果之行》《乍得归来》的殖民批判 | 非洲页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Madeleine Rondeaux | 无向 | 1895 成婚的表妹，1938 年去世 |
| parent-child | Catherine Gide | 纪德→女 | 1923 年生女，母为 Elisabeth van Rysselberghe |
| colleague | Oscar Wilde | 无向 | 巴黎结识、1895 阿尔及尔重逢的爱尔兰剧作家 |
| colleague | Marc Allégret | 无向 | 1916 年起的伴侣与旅伴（1926–27 非洲之行同行） |
| colleague | Jacques Copeau | 无向 | 泽西岛同游友人，NRF 共创圈核心 |
| colleague | Théo van Rysselberghe | 无向 | 友人，1907 年为其画像（其女 Elisabeth 生 Catherine） |
| colleague | William Rothenstein | 无向 | 一战访英结交的英国画家 |
| colleague | Charles Du Bos | 无向 | 挚友兼 Foyer Franco-Belge 同仁，1929 年后友谊破裂 |
| colleague | Ernst Robert Curtius | 无向 | 共同友人，曾撰信批评 Du Bos 之书 |
| colleague | Dorothy Bussy | 无向 | 1918 年起 30 余年挚友，多部作品英译者 |
| colleague | Victor Serge | 无向 | 纪德力倡释放的苏联作家，后为其提供苏联资讯 |
| colleague | Maxim Gorky | 无向 | 1936 年受邀在其葬礼上致辞 |
| influence | Fyodor Dostoyevsky | 影响→纪德 | 1923 年著陀思妥耶夫斯基论 |
| influence | Albert Camus / Jean-Paul Sartre | 纪德→影响 | 1920 年代成为两位后辈作家的精神启发者 |

#### 4.5.1 入库操作

- `MySQL/data/André_Gide.yaml` + `cd MySQL && python3 seed_person.py data/André_Gide.yaml`（幂等）；校验 fields≥4、relations≥2。

### 第 5 步：设计配色 【人物专属】

- **主色**：纪德深蓝 `#1E4E79`（预分配，勿改）；诺奖香槟金 `C9A227`。
- badgeA–D：badgeA 伪币犯/镜中镜 — 靛蓝 `#4C5FD5`；badgeB 窄门 — 青绿 `#0E7C7B`；badgeC 非洲/殖民批判 — 琥珀 `#E07B30`；badgeD 日记/自省 — 玫瑰 `#C4204F`。
- 背景母题：嵌套方框「镜中镜」线稿 + 窄门光缝（细长矩形光带）。

### 第 6 步：规划幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 真我的审问者 / André Gide 1869–1951 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名、国籍、教育、婚姻、市长/NRF、荣誉、核心领域）
03  核心作品概览 — 六大代表年表书影（食粮→背德者/窄门→梵蒂冈→田园→伪币犯→刚果）
04  新教童年与巴黎 (1869–1891) — 法学教授之父、诺曼底孤僻成长、21 岁处女作
05  北非与 Wilde (1893–1900) — 接纳自我、阿尔及尔重逢
06  人间食粮与双生对题 (1897–1909) — 背德者/窄门、市长任期、NRF 创刊
07  一战岁月 (1914–1918) — 访英、Foyer Franco-Belge 难民救济、焚信之痛
08  《田园交响曲》与《梵蒂冈地窖》 — 无动机行为与伪装的信仰
09  科里东风波 (1924) — 「我最重要的作品」、无缘法兰西学术院、自传《如果种子不死》
10  《伪币犯》(1925) — mise en abyme、Edouard 的日记、唯一长篇
11  刚果之行 (1926–1927) — 大型特许制批判、反殖民影响
12  从苏联归来 (1936–1937) — 应邀访苏、文化萧条之察、《上帝失败了》文集渊源（仅客观转述）
13  突尼斯与阿尔及尔 (1942–1945) — 战时流寓、七星文库第一人（1939）
14  荣誉与认可 — Nobel 1947 · 官方理由引文框 · 《日记》「若只留一书」
15  遗产：禁书目录之后 — 1952 Index、加缪/萨特一脉、「法国世纪文豪」之评、结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用，人物专属内容】

- 版式：`p{}` 窄列用 `\newcolumntype{P}[1]`；法语书名斜体+意译对照；frame 标题过长缩短即可；文学页用书影/引文框替代公式框。
- 陷阱：

| 陷阱 | 说明 |
|------|------|
| 死亡日期 | frontmatter 有 1951-12-19/1922-02-19 噪声，以正文 1951-02-19 为准 |
| 全名 | André Paul Guillaume Gide，勿漏 Guillaume；勿与叔父 Charles Gide（经济学家）混淆 |
| 出生地说法 | infobox 作 "Second French Empire"（法兰西第二帝国时期的巴黎），写「巴黎」即可，勿写「帝国」作为国名 |
| 婚姻口径 | 与表妹 Madeleine 未圆房为 page.md 明载；Catherine 之母为 Elisabeth van Rysselberghe（勿与画家父 Théo 混淆） |
| Marc Allégret | 1916 年相恋时 Marc 15 岁——按 page.md 客观转述，不展开渲染；Élie Allégret 是其父兼傧相 |
| 苏联内容红线 | 只按 page.md 客观事实简述（应邀访苏、两书出版、苏方批评），不作政治评价、不展开政治叙事 |
| 学院口径 | 「无缘法兰西学术院」是因《科里东》谴责声浪被挡（page.md 明载），勿写成「落选」 |
| 上半世纪大奖 | infobox 有载但正文无年份——年份禁写 |
| Wilde 方向 | Wilde 曾误以为是自己「引介」了纪德，而纪德此前已然接纳自我——因果勿反 |
| 引语红线 | 《从苏联归来》英文引语仅引 page.md 实载段落；Journal 1930 「真我之争」段为英译明载可用 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| mise en abyme | 纹心结构/镜中镜 | 《伪币犯》核心技法，勿译「深渊投射」 |
| Nouvelle Revue Française | 《新法兰西评论》 | 1908 共创，缩写 NRF |
| Bibliothèque de la Pléiade | 七星文库 | 1939 首位在世作者入选 |
| Les faux-monnayeurs | 《伪币犯》 | 唯一长篇（1925） |
| Strait Is the Gate | 《窄门》 | 1909，勿译「窄的是门」 |
| Les nourritures terrestres | 《人间食粮》 | 1897，亦有译「地粮」 |
| Corydon | 《科里东》 | 1924 公开版，作者自视最重要著作 |
| Si le grain ne meurt | 《如果种子不死》 | 1924 自传 |
| Retour de l'U.R.S.S. | 《从苏联归来》 | 1936，续篇 1937 |
| Foyer Franco-Belge | 法比之家 | 一战难民救济组织 |
| fellow traveler | 同路人 | 未正式入党（page.md 明载） |
| Index Librorum Prohibitorum | 《禁书目录》 | 1952 列入，天主教会口径 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience**（分批文件预分配，勿改）
- **匹配理由**：Cinematic Experience 的「电影感/戏剧张力」标签匹配纪德的文学生命形态——他的每部作品都在「挑战前作与自身」（perpetual renewal of values），从象征派到反殖民到《从苏联归来》的转向，是一次次戏剧性的自我翻案；其 Journal 的自省独白与 mise en abyme 的嵌套结构，本身即具镜头感。
- **备选（未采用）**：The Flow of Time（时间感匹配《日记》六十年书写，但受众偏低）；Eternals（已分配 Hesse 同批，避撞曲）。
- **本地路径**：对照 `music_audio/curated_tracks.md` 取 Cinematic Experience 音频复制到本目录，`make video` 时 ffmpeg `-shortest` 对齐。

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
