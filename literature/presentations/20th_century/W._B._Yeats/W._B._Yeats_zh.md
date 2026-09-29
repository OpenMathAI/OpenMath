# 文学家立传提示词（OpenLiterature 实例：W. B. Yeats）

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：W. B. Yeats（威廉·巴特勒·叶芝，1923 诺贝尔文学奖，爱尔兰文学复兴旗手、20 世纪英语诗歌巨匠）。
- **设计哲学**：文学家立传以「名句引文框 + 意象图式」替代公式框；身份信息页与领域结构化表达保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：William Butler Yeats（1865-06-13 生于都柏林 Sandymount ~ 1939-01-28 逝于法国 Roquebrune-Cap-Martin，享年 73 岁）
- **1923 官方获奖理由**（禁止改写）：
  > EN: "for his always inspired poetry, which in a highly artistic form gives expression to the spirit of a whole nation"
  > 中译（CITATION_ZH, key=("1923","William Butler Yeats")）：表彰其始终充满灵感的诗歌，以高度艺术化的形式表达了整个民族的精神
- **气质关键词**：**凯尔特暮光的织梦者、塔楼上的象征主义者、以诗参与国族塑造的参议员**
- **设计母题**：**旋转的螺旋与塔楼（Gyres and Thoor Ballylee）**。螺旋（gyres）出自其夫妻通灵笔记发展成的《A Vision》体系；塔楼是其 1919 年起的夏季居所与《The Tower》(1928) 书名——象征「传统形式大师」的诗学。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/W._B._Yeats/page.md`（事实基准）
  - `literature/presentations/pages/20th_century/W._B._Yeats/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/W._B._Yeats
  - 肖像（第 0 步待下载）：真实肖像充足——1911 照（infobox）、1900 父绘、1903 Boughton 照、1908 Sargent 炭笔画、1933 Pirie MacDonald 照；任选其一 500px
- **name_en 口径**：yaml `name_en: W. B. Yeats`（统一缩写形；CITATION_ZH 的 key 姓名为 William Butler Yeats，引用获奖理由时按该 key 查）

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1865-06-13 生于都柏林 Sandymount（frontmatter 另有 03-13 噪声值，以正文/infobox 06-13 为准）；1939-01-28 逝于 Roquebrune-Cap-Martin（Hôtel Idéal Beauséjour），死因心力衰竭，享年 73；1948-09 遗骸由军舰 LÉ Macha 迎回，葬 County Sligo Drumcliff 圣哥伦巴教堂墓园；墓志铭取自《Under Ben Bulben》末三行（page.md 英文原文在载：Cast a cold Eye / On Life, on Death. / Horseman, pass by!）
- **国籍/身份**：爱尔兰新教徒、盎格鲁-爱尔兰裔（Protestant Ascendancy）；爱尔兰自由邦参议员（1922-12-11 就任，1928-09 因病卸任）
- **家庭**：父 John Butler Yeats（先法律后肖像画家）；母 Susan Mary Pollexfen（Sligo 富商之家，Sligo 成为其「心之乡」）；弟 Jack Butler Yeats 名画家；姐妹 Elizabeth/Lily 主持 Cuala Press；1917-10-20 娶 Georgie Hyde-Lees（1892–1968），子女 Anne 与 Michael
- **教育**：Godolphin School（1877 起 4 年）；都柏林 Erasmus Smith High School（1881 起）；1884–1886 Metropolitan School of Art（今 National College of Art and Design）
- **神秘主义**：1890 入赫尔墨斯黄金黎明会（法号 Daemon est Deus inversus），留 Stella Matutina 至 1921；1911 入 The Ghost Club；受 Swedenborg 与 Mohini Chatterjee 影响；1917 婚后自动书写通灵→《A Vision》（1925）
- **文学师承与影响（page.md 明载）**：早期诗受 John Keats、William Wordsworth、William Blake 影响；受惠于 Edmund Spenser、Percy Bysshe Shelley 与拉斐尔前派；美学理论受 Oscar Wilde 影响（面具论→The Player Queen）
- **关键荣誉**：Nobel 1923；Goethe Plaque of the City of Frankfurt；Royal Society of Literature Fellow；Doctor of Letters
- **核心作品与贡献（4–6 条）**：
  1. 《The Wanderings of Oisin》（1889）——首部诗集，芬尼亚循环题材
  2. 《The Wind Among the Reeds》（1899）——早期抒情巅峰
  3. 《Cathleen ni Houlihan》（1902）——民族戏剧（艾比开幕夜剧目）
  4. 《The Wild Swans at Coole》（1919）——库勒庄园时期
  5. 《The Tower》（1928）、《The Winding Stair》（1933）、《New Poems》（1938）——晚期巅峰意象
  6. 《A Vision》（1925）——螺旋象征体系；1936 主编《Oxford Book of Modern Verse》
- **关键时间线（16–20 节点）**：
  1. 1865-06-13 生于都柏林 Sandymount
  2. 1867 随家迁伦敦；母亲授爱尔兰民间故事
  3. 1877 入 Godolphin School
  4. 1881 入 Erasmus Smith High School；父画室结识文艺界
  5. 1885 首批诗刊于 Dublin University Review；参与 Dublin Hermetic Order
  6. 1886 《Mosada》自印 100 册
  7. 1889 《The Wanderings of Oisin》；识 Maud Gonne
  8. 1890 与 Ernest Rhys 共创 Rhymers' Club；入黄金黎明会
  9. 1891 起多次向 Gonne 求婚被拒（1891/1899/1900/1901，末次 1916）
  10. 1895–1919 居伦敦 Woburn Walk 5 号
  11. 1896 经 Edward Martyn 识 Lady Gregory
  12. 1899 与 Gregory、Martyn、George Moore 创 Irish Literary Theatre
  13. 1902 协创 Dun Emer Press（1904 改 Cuala Press，出书 70+，叶芝 48 种）
  14. 1904-12-27 艾比剧院开幕（Cathleen ni Houlihan 打头）
  15. 1909 识 Ezra Pound；1913–1916 冬季共居 Ashdown Forest 石屋
  16. 1916 复活节起义→「Easter, 1916」
  17. 1917 娶 Georgie Hyde-Lees
  18. 1922-12-11 就任爱尔兰自由邦参议员；1924 主持货币图案委员会
  19. 1923-12 获诺贝尔文学奖（答谢词称「欧洲欢迎自由邦的一部分」）
  20. 1925/1926 《A Vision》；1928 《The Tower》；因病卸任参议员
  21. 1934 Steinach 手术；晚年恋情与《New Poems》
  22. 1938 与 Shri Purohit Swami 合译《The Ten Principal Upanishads》；最后一次到艾比看《Purgatory》
  23. 1939-01-28 卒于 Roquebrune-Cap-Martin；1948 归葬 Drumcliff

### 第 1 步：建立目录 【模板通用】

- 创建 `literature/presentations/20th_century/W._B._Yeats/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设 `MAIN=W._B._Yeats_zh`、`VIDEO_NAME=W._B._Yeats_zh`

### 第 3 步：收集图片 【人物专属】

- 主肖像：1911 照或 1933 Pirie MacDonald 照（500px，curl -A + file 验证）；插图可选父绘 1900 肖像、Sargent 1908 炭笔画、Maud Gonne c.1900 照、Drumcliff 墓园照（图注注明）

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | symbolist poetry | 象征主义诗歌 | 意象与象征结构贯穿一生 | 核心页 |
| 1 | Irish Literary Revival | 爱尔兰文学复兴 | 驱动力之一、艾比剧院缔造者 | 剧院页 |
| 2 | modernist poetry | 现代主义诗歌 | 跨 19→20 世纪的过渡者 | 风格页 |
| 3 | poetic drama | 诗剧 | 民族戏剧至能剧式贵族戏剧 | 剧场页 |
| 4 | mysticism | 神秘主义 | 黄金黎明会与《A Vision》体系 | 神秘页 |

- 入库：`MySQL/data/W._B._Yeats.yaml` → `python3 seed_person.py data/W._B._Yeats.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Georgie Hyde-Lees | 无向 | 1917-10-20 结婚；子女 Anne 与 Michael；通灵笔记成《A Vision》 |
| influence | William Blake | Yeats 受其影响 | 早期诗歌转向布莱克；与 Edwin Ellis 合编布莱克全集 |
| influence | Percy Bysshe Shelley | Yeats 受其影响 | 少年习作与早期诗明载 |
| influence | Edmund Spenser | Yeats 受其影响 | 首部诗集的诗学范型 |
| influence | Oscar Wilde | Yeats 受其影响 | 美学理论（面具论）影响其剧作 |
| rival | John MacBride | 无向 | 慕恋 Maud Gonne 的情敌（1903 娶 Gonne）；1916 起义后被处决 |
| colleague | Lady Gregory | 无向 | 1896 结识；文学复兴与艾比剧院共同缔造者 |
| colleague | J. M. Synge | 无向 | 艾比剧院共同创建者 |
| colleague | Edward Martyn | 无向 | 1896 引荐 Gregory；1899 共创 Irish Literary Theatre |
| colleague | Ezra Pound | 无向 | 1913–1916 冬季共居石屋，Pound 名义上任其秘书 |
| colleague | Ernest Rhys | 无向 | 1890 共创 Rhymers' Club |
| colleague | Edwin Ellis | 无向 | 合作完成首部布莱克作品全集 |
| colleague | Rabindranath Tagore | 无向 | 1913 为其 Gitanjali 英译本作序 |

**禁写**：Maud Gonne 与 Yeats 之间不建关系行（恋慕对象不属白名单类型；其影响已在正文叙述，关系表经 rival MacBride 侧面体现）；Olivia Shakespear 及晚年恋情不入库；Swedenborg/Mohini Chatterjee 只正文叙述不建行；Seán O'Casey、Padraic Colum、Douglas Hyde、George Moore 一句带过不建行；Blueshirts 与欧洲威权政治一律禁写（workflow 红线）；1948 遗骸迁移的「遗骨重组」争议只客观一笔或不写。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：#0E4D64（凯尔特深青——塔楼暮色）+ 诺奖香槟金 `C9A227`
- **badgeA** 象征主义诗歌 — 深青 `#0E4D64`；**badgeB** 爱尔兰文学复兴 — 翡翠 `#1B6B5A`；**badgeC** 诗剧 — 琥珀 `#E07B30`；**badgeD** 神秘主义 — 紫罗兰 `#46356B`
- **背景母题**：细线螺旋（gyres）+ 塔楼剪影 + 天鹅群稀疏点缀

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 凯尔特暮光的织梦者 / W. B. Yeats 1865–1939 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、家世、教育、婚姻、参议员、荣誉）
03  核心贡献概览 — 象征诗歌 / 文学复兴 / 诗剧 / 神秘体系
04  Sligo 童年与都柏林学艺（1865–1886）— 心之乡、画家父亲、艺术学校
05  早期诗与前拉斐尔格调（1886–1899）— Oisin / Wind Among the Reeds
06  神秘主义底色 — 黄金黎明会、通灵、《A Vision》（螺旋意象图式页）
07  Maud Gonne：终生的缪斯（1889–1917）— 多度求婚、Easter 1916 回响
08  文学复兴与艾比剧院（1896–1904）— Gregory/Martyn/Synge、开幕夜
09  库勒与塔楼（1916–1928）— Wild Swans / The Tower（引文框：Easter, 1916 副歌）
10  1923 诺贝尔奖 — 官方理由 EN+中译；「欧洲欢迎自由邦」答谢
11  参议员岁月（1922–1928）— 离婚辩论、货币委员会
12  晚年（1929–1939）— The Winding Stair、奥义书合译、Roquebrune 辞世
13  归葬与墓志铭 — Under Ben Bulben 三行引文框 + Drumcliff 墓园
14  遗产：从 19 世纪跨入现代主义
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 身份页用 `\profileslide` 模式；引文框统一半角引号；英文诗句用窄行距 quote 环境

### 第 8 步：布局检查 【模板通用】

- 每页 make + pdftoppm 目检；诗句页防 hbox 溢出（长行可手动断行）

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Yeats 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日双值 | frontmatter 03-13 是噪声，用 06-13 |
| name_en 双形 | yaml 统一 W. B. Yeats；CITATION_ZH key 为 William Butler Yeats |
| 死亡地/归葬 | 卒于法国 Roquebrune-Cap-Martin；1948 归葬 Drumcliff——两地勿混 |
| Gonne 求婚次数 | 1891/1899/1900/1901 + 1916 末次，勿写成「一次」或漏 1916 |
| Abbey 开幕日 | 1904-12-27，勿写成 1903 |
| 参议员任期 | 1922-12-11 就任、1928-09 因病卸任 |
| 政治内容 | Blueshirts/威权同情一律禁写；民族主义只按文学复兴叙事 |
| 通灵 | 《A Vision》出自夫妻自动书写实验——客观描述，勿写成「迷信嘲笑」或「科学事实」 |
| Tagore 序 | 1913 年作序的是 Gitanjali 英译本，叶芝并非其获奖原因——因果勿倒置 |
| 墓志铭 | 三行英文原文在载，引用须完整 |
| 金钱 | 奖金使其首次还清自己与父亲的债——可写，体现其经济处境 |
| Pound 关系 | Pound 未授权改动其诗稿曾致不快——同事行 note 勿写成纯和睦 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Irish Literary Revival | 爱尔兰文学复兴 | 亦称爱尔兰文艺复兴 |
| Abbey Theatre | 艾比剧院 | 1904 开幕 |
| gyres | 螺旋 | 《A Vision》体系核心意象 |
| automatic writing | 自动书写 | 夫妻通灵实验 |
| Hermetic Order of the Golden Dawn | 黄金黎明会 | 法号 Daemon est Deus inversus |
| Anglo-Irish | 盎格鲁-爱尔兰 | 阶层背景勿写成英格兰人 |
| Protestant Ascendancy | 新教优势阶层 | 历史术语，勿简化 |
| Celtic Twilight | 凯尔特暮光 | 早期基调（设计语言可用） |
| Fenian Cycle | 芬尼亚循环 | Oisin 题材来源 |
| Cuala Press | 库拉出版社 | 姐妹主持，48 种叶芝书 |
| symbolist / symbolism | 象征主义 | Style 节定位 |
| Easter Rising | 复活节起义 | 1916；同名诗注意逗号 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（分批文件预分配）
- **匹配理由**：「白昼」匹配其始终充满灵感的诗歌气质——从凯尔特暮光的早期朦胧到塔楼晚期意象的澄澈有力；也暗合诺奖理由「表达整个民族的精神」所指向的公共性、敞亮感。
- **本地路径**：按 `music_audio/curated_tracks.md` 对应文件复制为本目录 `Daylight.wav`
- **时长**：以曲目实际长度与成片页数对齐（ffmpeg `-shortest`）
