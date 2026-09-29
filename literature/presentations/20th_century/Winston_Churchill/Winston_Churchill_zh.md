# 文学家立传提示词（Winston Churchill / 温斯顿·丘吉尔）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir Winston Leonard Spencer Churchill（温斯顿·丘吉尔），英国政治家/军官/作家，1953 年诺贝尔文学奖得主。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**其作为"作家"的身份**——历史写作、传记、演说六卷二战回忆录；政治经历只按 page.md 客观事实简述，**不作政治评价、不展开政治叙事**。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Sir Winston Leonard Spencer Churchill（1874-11-30 ~ 1965-01-24，享年 90 岁）
- **诺奖年份**：1953 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for his mastery of historical and biographical description as well as for brilliant oratory in defending exalted human values"
  > （中译：表彰其对历史与传记描述的精湛掌握，以及捍卫崇高人类价值的辉煌演说）
- **气质关键词**：**历史巨笔、演说家、业余画家**
- **设计母题**：**笔与讲坛（the pen and the rostrum）**——以"鹅毛笔与讲坛剪影 + 旗帜意象"呼应其历史写作与演说双线；配色沉稳，政治内容一页带过。
- **本地数据源**：`literature/presentations/pages/20th_century/Winston_Churchill/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Winston_Churchill
- **肖像**：第 0 步待下载（1941 年 "The Roaring Lion"，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1874-11-30 生于牛津郡布莱尼姆宫（家族祖宅）~ 1965-01-24 逝于伦敦海德公园门 28 号，享年 90 岁；国葬（威斯敏斯特厅停灵三日，圣保罗大教堂仪式），葬于牛津郡 Bladon 圣马丁教堂家族墓地。
- 国籍：英国。1900–1964 年间约 62 年任下院议员，先后代表 5 个选区。
- 家庭：父 Lord Randolph Churchill（保守党议员）；母 Jeanette "Jennie" Jerome；弟 Jack；保姆 Elizabeth Everest（"我二十年中最亲密的朋友"，1895 卒——英文原文在 page.md，可引用）。1908 年娶 Clementine Hozier，育 5 子：Diana、Randolph、Sarah、Mary（Soames）等。
- 教育：Harrow School → 桑德赫斯特皇家军事学院（Royal Military College, Sandhurst）。
- 关键荣誉（与文学相关的取舍）：诺贝尔文学奖 1953；皇家学会 Fellow（FRS）；嘉德骑士；功绩勋章（Order of Merit）；美国荣誉公民（首位获授的八人之一）；2002 年 BBC "最伟大的英国人"投票第一（447,423 票）。
- 写作生涯（核心贡献，4–6 条）：
  1. 1897 随 Malakand Field Force 任随军记者（写作生涯起点），首部著作《The Story of the Malakand Field Force》（好评）；
  2. 唯一小说《Savrola》（罗曼司）；
  3. 《The River War》（1899，苏丹战役记述）；
  4. 《Marlborough: His Life and Times》（为祖先马尔博罗公爵一世作传，1929–32 动笔）；
  5. 六卷本回忆录《The Second World War》与四卷本《A History of the English-Speaking Peoples》——两部最著名作品；
  6. 笔名 "Winston S. Churchill" / "Winston Spencer Churchill"，以免与美国小说家 Winston Churchill 混淆（两人有友好通信）；多年靠报刊文章维持生计。
- 关键时间线（15–20 节点，写作线优先、政治线简述）：
  1. 1874 生于布莱尼姆宫；1876–80 随父驻都柏林；
  2. 1895 桑德赫斯特毕业、入第 4 女王 own 轻骑兵团；保姆 Everest 卒；
  3. 1897 印度 Malakand 随军记者——写作生涯开始；
  4. 1898 首书《The Story of the Malakand Field Force》；小说《Savrola》；
  5. 1898-09 奥姆杜尔曼战役（21 枪骑兵团，英军最后骑兵冲锋之一）；
  6. 1899 《The River War》出版；布尔战争任记者被俘（POW）后归队；
  7. 1900 当选下院议员（Oldham）；
  8. 1908 娶 Clementine Hozier；历任贸易委员会主席、内政大臣；
  9. 1911–15 第一任海军大臣；
  10. 1915 辞职后赴西线服役（皇家苏格兰燧发枪团 6 营营长）；
  11. 1917–19 军需大臣、陆军与空军大臣、殖民地事务大臣；
  12. 1924–29 财政大臣；1929–39 "荒野岁月"——靠写作对抗抑郁（"black dog"）；
  13. 1929–32 动笔《Marlborough: His Life and Times》；
  14. 1939-09 再任海军大臣；1940-05 出任首相至 1945；1951–55 再任首相；
  15. 1946 富尔顿"铁幕"演说；
  16. 1948–1954 六卷《The Second World War》陆续出版；
  17. 1953 获诺贝尔文学奖；
  18. 1956–1958 四卷《A History of the English-Speaking Peoples》；
  19. 1963 获美国荣誉公民；
  20. 1965-01-24 卒于伦敦，国葬。
- 二战名句（page.md 正文载有演讲文本者方可引用；引文框用 "we shall fight on the beaches" 一类需先核对本地文本，无原文禁引）。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | historical writing | 历史写作 | 六卷《The Second World War》、四卷《A History of the English-Speaking Peoples》 | 核心页 |
| 1 | biography | 传记 | 《Marlborough: His Life and Times》 | 传记页 |
| 2 | oratory | 演说 | 官方诺奖理由后半句"defending exalted human values" | 演说页 |
| 3 | memoir | 回忆录 | 二战六卷本（官方理由"historical description"主要载体） | 核心页 |
| 4 | journalism | 新闻写作 | 1897 起随军记者起步；多年以稿酬维生 | 早年页 |

#### 4.1 入库操作

- 新建 `people` 记录（name_en=`Winston Churchill`，qid=Q8016），`primary_occupation='writer'`、`has_social_data=1`
- occupations：writer(0)、historian(1)、politician(2)
- 5 个领域写入 `person_field`（historical writing / oratory 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。政治人物关系只收 page.md 明确合作者（战时盟友/副手），不展开政治叙事。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Clementine Hozier | 无向 | 1908 年结婚，相伴 57 年 |
| parent-child | Lord Randolph Churchill | 对方→本人 | 父，保守党议员 |
| parent-child | Jeanette "Jennie" Jerome | 对方→本人 | 母，美国人 |
| parent-child | Randolph Churchill | 本人→对方 | 子，记者作家 |
| parent-child | Mary Soames | 本人→对方 | 女（1973 年为议会广场雕像揭幕者） |
| colleague | Winston Churchill (novelist) | 无向 | 同名美国小说家，有友好通信；为避混淆用笔名 Winston S. Churchill |
| colleague | Franklin D. Roosevelt | 无向 | 二战同盟国首脑（"Special Relationship"雕像并立者） |
| colleague | Anthony Eden | 无向 | 战时与战后副首相、继任者 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#145C54`（深松绿——英伦庄重）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeHistory 靛蓝 `#4C5FD5`；badgeBio 青绿 `#0E7C7B`；badgeSpeech 琥珀 `#E07B30`；badgeArt 玫瑰 `#C4204F`
- **背景母题**：讲坛光束 + 旗帜剪影（低饱和、庄重）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 历史巨笔与讲坛 / Winston Churchill 1874–1965 + badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/教育/家庭/荣誉/核心领域）
03  核心创作概览 — 历史写作 / 传记 / 演说 / 新闻
04  写作起点：随军记者 (1897–1899)【书影：The Story of the Malakand Field Force】
05  唯一小说《Savrola》与《The River War》
06  荒野岁月与《Marlborough》 (1929–1939)【书影】
07  六卷《The Second World War》 (1948–1954)【书影：六卷本】
08  演说：捍卫崇高人类价值【引文框：官方诺奖理由后半句】
09  1953 诺贝尔文学奖 — 官方理由 EN 原文页（"作家诺奖"定位页）
10  四卷《A History of the English-Speaking Peoples》与画作（"Charles Morin"笔名）
11  晚年、国葬与遗产 (1955–1965)
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；书影框替代公式框；身份页 `\profileslide`。
- 陷阱表（★ 本篇最高优先级是"作家定位 + 政治克制"）：

| 陷阱 | 说明 |
|------|------|
| 定位 | 本篇是"文学家立传"：政治/军事经历只作时间线背景客观简述，不作评价、不设政治成就专页 |
| 政治红线 | 帝国主义/种族观点等争议段落（Legacy 节）一律不写、不评价 |
| 名言引用 | "iron curtain"、"fight on the beaches" 等，仅当 page.md 本地正文载有原文才可进引文框，否则以叙述转述 |
| 同名混淆 | 美国小说家 Winston Churchill（同姓同名，且友好通信）——关系表已列，引语/作品勿张冠李戴；笔名 Winston S. Churchill 即为此设 |
| 生卒双值 | frontmatter birth_date 有 "1874-01-01" 噪声值，以正文 1874-11-30 为准 |
| 国籍 | United Kingdom（frontmatter 另有 UK of GB & Ireland 历史值，yaml 取 United Kingdom） |
| 获奖 | 1953 诺奖是文学奖（非和平奖）；他从未获和平奖 |
| 头衔 | 尊称 KG OM CH TD DL FRS RA 一串可只写 KG/OM/FRS，勿杜撰顺序 |
| 《Savrola》 | 唯一小说，Ruritanian romance 题材，勿写成"科幻" |
| 第二次任相 | 1951-10-26 ~ 1955-04-05；第一次 1940-05-10 ~ 1945-07-26，勿颠倒 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| The Roaring Lion | 《怒狮》 | 1941 年 Karsh 肖像，infobox 图 |
| Marlborough: His Life and Times | 《马尔博罗：其人其时代》 | 为祖先作传 |
| The Second World War | 《第二次世界大战回忆录》 | 六卷本回忆录 |
| A History of the English-Speaking Peoples | 《英语民族史》 | 四卷本 |
| Savrola | 《萨伏罗拉》 | 唯一小说 |
| oratory | 演说术 | 诺奖理由关键词 |
| wilderness years | 荒野岁月 | 1929–1939 在野期 |
| Chartwell | 查特韦尔 | 私宅，画作多藏于此；砖瓦工/养蝶趣闻可作花絮 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions
- **匹配理由**：SEA 的辽阔史诗感匹配"英语民族史"与跨世纪的历史纵深；沉稳推进匹配六卷本回忆录的巨著气质，避开政治叙事的戏剧化。
- **本地路径**：`music_audio/alex-productions/` 下 SEA 对应 wav → `presentations/20th_century/Winston_Churchill/SEA.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Winston_Churchill/page.md` | 本地 Wikipedia 正文（事实基准，752 行长文——只按写作相关节取材） |
| `literature/presentations/pages/20th_century/Winston_Churchill/images.txt` | 肖像/插图 URL 清单（The Roaring Lion 1941） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_20th_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/Winston_Churchill.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（SEA 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（The Roaring Lion，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `Winston_Churchill/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=Winston_Churchill_zh`、`VIDEO_NAME=Winston_Churchill_zh`
4. ☐ 第 3 步：复制 SEA.wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2，已完成）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#145C54）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写；政治页零评价复核、名言引文核对本地原文）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
