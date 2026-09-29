# 文学家立传提示词（OpenLiterature 实例：George Bernard Shaw）

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：George Bernard Shaw（萧伯纳，1925 诺贝尔文学奖，现代英语戏剧革新者与费边社一代宗师）。
- **设计哲学**：以「名句引文框 + 思想辩论图式」替代公式框；身份信息页与领域结构化表达保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：George Bernard Shaw（1856-07-26 生于都柏林 Portobello ~ 1950-11-02 卒于英格兰 Ayot St Lawrence，享年 94 岁）
- **1925 官方获奖理由**（禁止改写；EN 全句按 nobelprize.org 官方口径，page.md 引其后半）：
  > EN: "for his work which is marked by both idealism and humanity, its stimulating satire often being infused with a singular poetic beauty"
  > 中译（CITATION_ZH, key=("1925","George Bernard Shaw")）：表彰其作品兼具理想主义与人道主义，其犀利的讽刺常浸润着独特的诗意之美
- **气质关键词**：**辩论台上的戏剧家、音乐批评出身的剧坛旗手、九十四岁的终身写作者**
- **设计母题**：**旋转的写作小屋（The Rotating Hut）**。Shaw's Corner 花园中可随阳光旋转的小屋是他 1906 年后大部分作品的产出地——以「光轨 + 小屋剪影 + 台词气泡」统摄视觉。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/George_Bernard_Shaw/page.md`（事实基准）
  - `literature/presentations/pages/20th_century/George_Bernard_Shaw/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/George_Bernard_Shaw
  - 肖像（第 0 步待下载）：真实照片充足——1911 照（infobox）、1894 照、1879 照、1936 八十岁照

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1856-07-26 生于都柏林 Portobello（3 Upper Synge Street）；1950-11-02 卒于 Ayot St Lawrence（修剪树木摔倒致伤、肾衰竭），享年 94；1950-11-06 于 Golders Green 火化，骨灰与亡妻混撒花园圣女贞德像四周
- **国籍/身份**：生为英国臣民；1934 起英爱双重国籍；1876 后自称 Bernard Shaw（弃 George）
- **家庭**：幼子；父 George Carr Shaw 谷商失意酗酒；母 Bessie 有女中音嗓；家中常客 George John Lee（指挥/声乐教师），Shaw 终生疑其为生父（学者无共识，一句带过）；1898-06-01 娶 Charlotte Payne-Townshend（经 Webb 夫妇结识，两人皆 41 岁；无子女；「未 consummated」系普遍看法——转述即可）；Charlotte 1943-09 去世
- **教育**：1865–1871 四所学校皆厌恶；1871 起都柏林地产行职员至首出纳；1876 迁伦敦后靠大英博物馆阅览室自学
- **政治觉醒与费边社**：1882 听 Henry George 演讲并读 Progress and Poverty；1883 通读 Das Kapital（不加入 SDF）；1884-09 入费边社、年末执笔 Fabian Tract No. 2；1885 入执委会并引荐 Sidney Webb 与 Annie Besant；1889 主编 Fabian Essays in Socialism；后由马克思主义转向 gradualism
- **批评生涯**：1885 起书评/乐评（Archer 引荐）；1889 起 The Star 乐评（笔名 Corno di Bassetto）；1890–1894 The World「G.B.S.」专栏；1895–1898 Saturday Review 剧评（主编 Frank Harris）
- **关键荣誉**：Nobel 1925（受奖但**拒领奖金**）；1938 Pygmalion 剧本获奥斯卡最佳改编剧本——史上首位「诺奖+奥斯卡」双冠；1946 拒 Order of Merit；同年受都柏林荣誉市民
- **核心作品与贡献（4–6 条）**：
  1. 《Widowers' Houses》（1892）——首剧（源自 1884 与 Archer 合作未遂底稿）
  2. 《Arms and the Man》（1894）——首度财务成功（首年 £341，得以辞去受薪乐评）
  3. 《Man and Superman》（1902）、《Major Barbara》（1905）、《Caesar and Cleopatra》——皇家宫廷剧院时期（Vedrenne 与 Granville-Barker 五年上演 14 剧）
  4. 《Pygmalion》（1912 写/1913 首演/1914 伦敦）——1938 电影获奥斯卡
  5. 《Heartbreak House》（1920）、《Back to Methuselah》（1922 五联剧）、《Saint Joan》（1923，Broadway 12 月首演）
  6. 政论 The Intelligent Woman's Guide to Socialism and Capitalism（1928）
- **关键时间线（20 节点）**：1856 生 Portobello；1862 与 Lee 家合住；1871 地产行职员至首出纳；1876-03 迁伦敦不再定居爱尔兰；1878–1883 五部小说习作（两部出版滞销）；1881 素食；1882–1883 政治觉醒；1884-09 入费边社/1885 入执委会；1889 主编 Fabian Essays；1890–1894 G.B.S. 乐评；1892 Widowers' Houses；1894 Arms and the Man 弃受薪乐评；1895–1898 Saturday Review 剧评；1897 St Pancras 教区议员（至 1903）；1898 婚 Covent Garden + The Perfect Wagnerite；1904–1909 皇家宫廷五季 14 剧；1906 定居 Ayot；1914 Common Sense About the War 舆论反目；1920–1922 Heartbreak House/Methuselah；1923 Saint Joan；1925 诺奖拒奖金；1928 Guide/The Apple Cart；1931 访苏、1934 双重国籍、1938 奥斯卡；1943 Charlotte 去世；1946 拒 OM；1950-11-02 卒

### 第 1 步：建立目录 【模板通用】

- 创建 `literature/presentations/20th_century/George_Bernard_Shaw/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设 `MAIN=George_Bernard_Shaw_zh`、`VIDEO_NAME=George_Bernard_Shaw_zh`

### 第 3 步：收集图片 【人物专属】

- 主肖像：1911 照或 1894 照 500px（curl -A + file 验证）；插图可选出生地照、旋转小屋照（图注注明）

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modern drama | 现代戏剧 | 受易卜生影响引入英语戏剧新现实主义 | 核心页 |
| 1 | comedy of ideas | 观念喜剧 | 讨论剧/严肃闹剧，六十余剧 | 剧目页 |
| 2 | political theatre | 政治剧场 | 剧作作为政教社思传播载体 | 剧场页 |
| 3 | music criticism | 音乐批评 | Corno di Bassetto 与 G.B.S. 专栏 | 批评页 |
| 4 | Fabian socialism | 费边社会主义 | 宣言执笔人与头号小册子作者 | 费边页 |

- 入库：`MySQL/data/George_Bernard_Shaw.yaml` → `python3 seed_person.py data/George_Bernard_Shaw.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Charlotte Payne-Townshend | 无向 | 1898-06-01 结婚；1943-09 去世；无子女 |
| influence | Henrik Ibsen | Shaw 受其影响 | 受其影响引入英语戏剧新现实主义 |
| influence | Karl Marx | Shaw 受其影响 | 1883 通读 Das Kapital（后转向 gradualism） |
| influence | Henry George | Shaw 受其影响 | 1882 演讲与 Progress and Poverty 引发经济学兴趣 |
| influence | William Morris | Shaw 受其影响 | 美学观影响（艺术必须载道） |
| influence | John Ruskin | Shaw 受其影响 | 美学观影响（同上） |
| colleague | Sidney Webb | 无向 | 1880 Zetetical Society 结识，终生挚友；费边社核心同僚 |
| colleague | Beatrice Webb | 无向 | 费边社同僚；Charlotte 经 Webb 夫妇结识 |
| colleague | William Archer | 无向 | 1884 合作未遂后成为其批评生涯引路人 |
| colleague | H. G. Wells | 无向 | 费边社改革之争（Old Gang 对 Wells），Wells 1908 退社 |
| colleague | Frank Harris | 无向 | Saturday Review 主编好友，1895–1898 任其剧评人 |
| colleague | Harley Granville-Barker | 无向 | 1904–1909 皇家宫廷剧院上演其 14 剧的合作者 |
| colleague | W. B. Yeats | 无向 | 挚友；John Bull's Other Island 与 1909 艾比共导邀约 |
| colleague | Seán O'Casey | 无向 | 挚友；读 John Bull's Other Island 后立志写剧 |
| colleague | Edward Elgar | 无向 | Malvern 音乐节时期深交，互相敬重 |
| colleague | Gabriel Pascal | 无向 | Pygmalion（1938 电影）制片人 |

**禁写**：斯大林/墨索里尼/列宁/希特勒一律不建关系行，正文至多客观一笔不作政治评价（workflow 红线）；Nancy Astor、Michael Collins、Mrs Patrick Campbell（恋情）、Jenny Patterson、Florence Farr（恋情）不入关系行；Haig 邀访西线仅公务一笔。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：#0F4C5C（深孔雀青——辩论台的冷峻）+ 诺奖香槟金 `C9A227`
- **badgeA** 现代戏剧 — 深青 `#0F4C5C`；**badgeB** 观念喜剧 — 琥珀 `#E07B30`；**badgeC** 政治剧场 — 玫瑰 `#C4204F`；**badgeD** 音乐批评/费边 — 靛蓝 `#1E4E79`
- **背景母题**：旋转小屋剪影 + 台词气泡 + 一圈金色光轨

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 辩论台上的戏剧家 / George Bernard Shaw 1856–1950 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、出身、伦敦自学、婚姻、荣誉）
03  核心贡献概览 — 现代戏剧 / 观念喜剧 / 政治剧场 / 音乐批评
04  都柏林少年（1856–1876）— 画家乐师之家、地产行职员
05  伦敦长跑（1876–1884）— 滞销小说、大英博物馆阅览室、素食
06  政治觉醒（1882–1889）— Henry George、Das Kapital、费边社
07  批评家岁月（1885–1894）— Corno di Bassetto、G.B.S.、剧评
08  首捷（1892–1898）— Widowers' Houses、Arms and the Man、婚姻
09  皇家宫廷剧院时期（1904–1914）— 14 剧与 Pygmalion
10  战时孤声（1914–1918）— Common Sense About the War（引文框）
11  晚期高峰（1918–1923）— Heartbreak House / Methuselah / Saint Joan
12  1925 诺贝尔奖 — 官方理由 EN+中译；受奖拒奖金
13  双冠与费边余晖（1928–1938）— Guide、The Apple Cart、奥斯卡
14  Ayot 岁月与终点（1943–1950）— 亡妻、拒 OM、94 岁笔耕
15  遗产：Shavian 一词进入英语 + 结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 身份页用 `\profileslide` 模式；引文框半角引号；年代轴 `\foreach` 分隔符必须 ASCII 逗号

### 第 8 步：布局检查 【模板通用】

- 每页 make + pdftoppm 目检；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调 y

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Shaw 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 笔名 | 1876 后自称 Bernard Shaw；「George Bernard Shaw」为通称——正文口径统一 |
| 生父疑云 | Lee 生父说无共识——只写「终生疑虑、学者无共识」 |
| 婚姻细节 | 1898-06-01、双方 41 岁、无子女；「未 consummated」是转述非断言 |
| 拒领奖金 | 1925 受奖但拒奖金——勿写成拒绝领奖本身 |
| 双冠 | 1938 奥斯卡为最佳改编剧本（Pygmalion）；「首位诺奖+奥斯卡」表述在载可用 |
| 拒 OM | 1946 拒 Order of Merit（作者价值由历史定）——勿写成「拒封爵」 |

| 政治内容 | 斯大林/墨索里尼/希特勒评价一律禁写、禁关系行；苏联观感至多客观一笔 |
| 战争立场 | 1914 双方同咎论致众叛亲离——引文用 page.md 原文 |
| 五部小说 | 习作五部、出版两部——勿夸大小说成就 |
| LSE | 1895 年在 Hutchinson 遗产上创办，Shaw 由反对转为支持——勿写成其创办人 |
| Yeats 友谊 | John Bull's Other Island 曾令新盖尔运动不适，但两人仍为挚友——两面并写 |
| Wells 之争 | 「Old Gang 对 Wells」：Wells 1908 退社——勿写成单向打压或私怨 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Fabian Society | 费边社 | gradualism 渐进主义口径 |
| discussion drama | 讨论剧 | Weintraub 对其形式的命名 |
| Corno di Bassetto | 巴赛特号（笔名） | The Star 乐评笔名 |
| polemicist | 论战家 | 导语定位词 |
| Shavian | 萧氏的 | 已入英语词典的形容词 |
| Pygmalion | 《皮格马利翁》 | 1913 剧 + 1938 电影两轨 |
| Saint Joan | 《圣女贞德》 | 1923；封圣触动创作 |
| Back to Methuselah | 《回到玛土撒拉》 | 五联剧 Metabiological Pentateuch |
| Shaw's Corner | 萧氏角 | Ayot St Lawrence 宅邸 |
| rotating hut | 旋转写作小屋 | 设计母题实物 |
| vegetarianism | 素食主义 | 1881 起，终身信条（晚年肝剂治疗为破例） |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（分批文件预分配）
- **匹配理由**：曲名的庄重张力匹配其一生「以辩论直面时代悲剧」的姿态——战时孤声、众叛亲离而不改立场；亦是《Saint Joan》式悲剧英雄剧场的配乐底色；对 94 岁终身笔耕的落幕有一种肃穆的收束感。
- **本地路径**：按 `music_audio/curated_tracks.md` 对应文件复制为本目录 `Tragedy.wav`
- **时长**：以曲目实际长度与成片页数对齐（ffmpeg `-shortest`）



