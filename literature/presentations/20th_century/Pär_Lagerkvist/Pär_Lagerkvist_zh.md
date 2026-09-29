# 文学家立传提示词（Pär Lagerkvist / 帕尔·拉格奎斯特）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Pär Fabian Lagerkvist（帕尔·拉格奎斯特），瑞典诗人/剧作家/小说家，1951 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传保留物理学家模板的「身份信息页 + 研究领域结构化」骨架，但叙事重心放在**创作母题（善恶之问、宗教意象、极简文体）**与代表作演进上。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Pär Fabian Lagerkvist（1891-05-23 ~ 1974-07-11，享年 83 岁）
- **诺奖年份**：1951 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for the artistic vigour and true independence of mind with which he endeavours in his poetry to find answers to the eternal questions confronting mankind"
  > （中译：表彰其在诗歌中力求回答人类面临的永恒问题时所展现的艺术活力与真正独立的精神）
- **气质关键词**：**善恶之问的道德家、圣经意象的驯服者、古典简净的现代主义者**
- **设计母题**：**旷野中的永恒之问（the eternal question）**——以「一盏灯 / 旷野地平线 / 十字剪影」的极简意象图式呼应其"以最少的词语表达最深之物"的文体（瑞典批评家将其与使徒约翰并举）。
- **本地数据源**：`literature/presentations/pages/20th_century/Pär_Lagerkvist/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/P%C3%A4r_Lagerkvist
- **肖像**：第 0 步待下载（1951 年获奖时照片，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1891-05-23 生于瑞典韦克舍（Växjö，斯莫兰）~ 1974-07-11 逝于斯德哥尔摩，享年 83 岁。
- 国籍：瑞典。
- 家庭：传统宗教家庭——"很幸运在一个家里只知道《圣经》与《赞美诗集》两本书的地方长大"（英文原文在 page.md，可引用）；青少年时脱离基督教信仰，但从未激烈反宗教；一生政治立场偏社会主义。
- 婚姻：1916《Ångest》十年后第二次结婚，此段婚姻直到妻子 1967 年去世（约四十年）；妻子姓名 page.md 无载，**禁写**。
- 教育：乌普萨拉大学（Uppsala University，frontmatter）。
- 关键荣誉：诺贝尔文学奖 1951；瑞典学院院士（1940-09 当选，12 月入坐第 8 席，接替 Verner von Heidenstam）；Bellman Prize；哥德堡大学荣誉博士；Samfundet De Nio 大奖。
- 核心作品与贡献（4–6 条）：
  1. 《Ordkonst och bildkonst》（1913）——现代主义美学宣言，支持表现主义激进主张；
  2. 《Ångest》（Anguish，1916）——幻灭诗集，战争与死亡恐惧的呐喊；
  3. 《Hjärtats sånger》（1926）——献给第二任妻子，确立其一代最伟大瑞典诗人之列；
  4. 《Bödeln》（The Hangman，1933）——寓言小说/剧本，直指极权主义，遭《冲锋报》恶评；《Mannen utan själ》（1936）续批法西斯；二战期间参加反纳粹组织 Tisdagsklubben，被盖世太保列入死亡名单；
  5. 《Dvärgen》（The Dwarf，1944）——关于"恶"的讽喻小说，首个获得北欧以外国际声誉的作品；
  6. 《Barabbas》（1950）——圣经外传小说，安德烈·纪德等盛赞，1951 获奖直接推手；晚年"救赎系列"《Sibyllan》(1956)、《Ahasverus död》(1960)、《Pilgrim på havet》(1962)、《Det heliga landet》(1964)、《Mariamne》(1967)。
- 关键时间线（15–20 节点）：
  1. 1891 生于韦克舍宗教家庭；
  2. 1912 首部短篇集《Människor》；
  3. 1913 现代主义宣言《Ordkonst och bildkonst》；
  4. 1916 诗集《Ångest》（战争恐惧与幻灭）；
  5. 1917–19 剧作《Sista mänskan》《Himlens hemlighet》；
  6. 1920 《Det eviga leendet》（文风转向古典简净）；
  7. 约 1926 前后第二次结婚（妻 1967 卒）；《Hjärtats sånger》；
  8. 1930 《Själarnas maskerad》；
  9. 1933 《Bödeln》——纳粹主义为主要靶标；
  10. 1936 《Mannen utan själ》批法西斯；
  11. 二战期间加入反纳粹组织 Tisdagsklubben；被盖世太保列入死亡名单；
  12. 1940-09 当选瑞典学院院士（12 月入第 8 席，接替 Heidenstam）；
  13. 1944 《Dvärgen》（国际声誉）；
  14. 1949/50 剧本《Låt människan leva》；
  15. 1950 《Barabbas》（纪德盛赞为杰作；1950 年曾是热门人选）；
  16. 1947 首次获提名；1951 年获 9 项提名（含纪德、罗歇·马丁·杜·加尔）；
  17. 1951 获诺贝尔文学奖；
  18. 1953 《Aftonland》（Evening Land，W. H. Auden 与 Leif Sjöberg 英译）；
  19. 1955 短篇集英译《The Marriage Feast》；
  20. 1961/2012 《Barabbas》三度搬上银幕（1961 Anthony Quinn 主演）；1974 卒于斯德哥尔摩。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist poetry | 现代主义诗歌 | 1913 宣言与《Ångest》为瑞典现代诗开山 | 早年页、诗歌页 |
| 1 | religious fiction | 宗教题材小说 | Barabbas/The Dwarf——善恶与信仰之问 | 核心页 |
| 2 | moral parable | 道德讽喻 | 以圣经人物外传追问"人被神离弃后的处境" | 核心页 |
| 3 | drama | 戏剧 | 《Bödeln》《Låt människan leva》等舞台剧 | 戏剧页 |
| 4 | novella | 中短篇叙事 | 极简文体：以最少词语写最深之物 | 文体页 |

#### 4.1 入库操作

- 新建 `people` 记录（name_en=`Pär Lagerkvist`，qid=Q93137），`primary_occupation='writer'`、`has_social_data=1`
- occupations：writer(0)、poet(1)、playwright(2)
- 5 个领域写入 `person_field`（fields 字典缺失项先补建：modernist poetry / religious fiction / moral parable 等）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。妻子（无名）、Tisdagsklubben 成员 metadata 无名，均不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Verner von Heidenstam | 无向 | 1940 接替其瑞典学院第 8 席 |
| colleague | André Gide | 无向 | 盛赞《Barabbas》为杰作；1951 年提名诺奖 |
| colleague | Roger Martin du Gard | 无向 | 1951 年提名其诺奖 |
| colleague | W. H. Auden | 无向 | 《Aftonland》（Evening Land）英译者 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#2A4B7C`（深湖蓝——北欧旷野与宗教静穆）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgePoetry 靛蓝 `#4C5FD5`；badgeParable 青绿 `#0E7C7B`；badgeDrama 琥珀 `#E07B30`；badgeEthics 玫瑰 `#C4204F`
- **背景母题**：旷野地平线上一盏孤灯（大圆低饱和）——呼应"永恒之问"

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 善恶之问的道德家 / Pär Lagerkvist 1891–1974 + badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/教育/瑞典学院/荣誉/核心领域）
03  核心创作概览 — 诗歌 / 讽喻小说 / 戏剧 / 救赎系列
04  早年：韦克舍的圣经与赞美诗 (1891–1912)
05  现代主义宣言与《Ångest》 (1913–1916)【名句引文框：Anguish, anguish is my heritage…】
06  转向古典简净：《永恒的微笑》与《心之歌》 (1920–1926)【意象图式：灯火】
07  《刽子手》：刺向极权的寓言 (1933–1944)【书影：The Dwarf】
08  瑞典学院与盖世太保名单 (1940–1945)
09  《巴拉巴》：替代者的一生 (1950)【名句引文框/书影】
10  1951 诺贝尔文学奖 — 官方理由 EN 原文页
11  救赎系列与遗产 (1956–1974)
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式：`mainclr/accentclr/badgeA..D/panelA..D` 宏名统一；身份页参照 `\profileslide`；引文框用 tcolorbox 半透明主色。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 妻子无名 | page.md 未载两任妻子姓名，只写"第二次婚姻约 1926 前后、妻 1967 卒"，禁编名字 |
| Låt människan leva 年份 | Works 列表作 1950，正文作 1949——写 1949/1950 两说或取 1950（获奖前后），勿单写 1944 |
| Bödeln 定性 | 是"小说后被改编为舞台剧（1934）"，勿写成纯剧本 |
| 纪德的角色 | Gide 是"盛赞者 + 1951 提名人"，勿写成"导师"或"共同获奖" |
| 政治立场 | 一生社会主义者 + 反纳粹（Tisdagsklubben、盖世太保死亡名单），客观简述即可，不展开政治评价 |
| 宗教立场 | "脱离信仰但不敌视宗教、不以宗教为鸦片"，用 page.md 措辞，勿写成"虔诚"或"无神论" |
| 诺奖理由 | 官方措辞强调 poetry 中的"艺术活力与真正独立精神"，勿泛化成"代表作 Barabbas 获奖" |
| 保守主义导航框 | page.md 含 Swedish conservatism 导航模板，Lagerkvist 仅是"Intellectuals 列表中出现"，非保守派作家，勿采信 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Barabbas | 巴拉巴 | 被释放代替耶稣者，勿写成"强盗"单义（novel 原文为 convicted thief and murderer） |
| The Dwarf | 侏儒 | Dvärgen，第一人称恶之叙事 |
| Ahasuerus | 阿哈斯维鲁斯 | 流浪的犹太人（Wandering Jew） |
| moralist | 道德家 | page.md 原词，非"说教者" |
| naivism | 朴素主义 | 文风近似而非内容天真 |
| Swedish Academy | 瑞典学院 | 颁奖机构，第 8 席 |
| expressionism | 表现主义 | 早期路径，1920 后弃 |
| Tisdagsklubben | 星期二俱乐部 | 反纳粹组织（正文拼写 Tisdagsklubbe） |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions
- **匹配理由**： nostalgi­c / 深沉的弦乐气质匹配 Lagerkvist 晚年"救赎系列"的回望语调与《Ångest》→古典简净的创作弧线；纪录片式推进匹配"旷野之问"母题。
- **本地路径**：`music_audio/alex-productions/` 下 Nostalgia 对应 wav → `presentations/20th_century/Pär_Lagerkvist/Nostalgia.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Pär_Lagerkvist/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Pär_Lagerkvist/images.txt` | 肖像/插图 URL 清单 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_20th_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/Pär_Lagerkvist.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（Nostalgia 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox 1951 年照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `Pär_Lagerkvist/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=Pär_Lagerkvist_zh`、`VIDEO_NAME=Pär_Lagerkvist_zh`
4. ☐ 第 3 步：复制 Nostalgia.wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2，已完成）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#2A4B7C）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

## 七、版式补遗 【人物专属】

- **引文框素材（page.md 载英文原文，可直接入框）**：
  1. "had had the good fortune to grow up in a home where the only books known were the Bible and the Book of Hymns"（童年宗教底色）；
  2. "Anguish, anguish is my heritage / the wound of my throat / the cry of my heart in the world."（《Anguish》1916）；
  3. "Love is nothing. Anguish is everything / the anguish of living."（《Love is nothing》1916）；
  4. 瑞典批评家评语 "Lagerkvist and John the Evangelist are two masters at expressing profound things with a highly restricted choice of words"（文体定音句，注明"瑞典批评家"）。
- **作品表页排版**：Works 清单极长（短篇集/长篇/戏剧三组）——只取每类代表 3–4 行，勿全量塞入；书名用斜体原语种 + 括注英译。
- **救赎系列页**：Sibyllan → Ahasverus död → Pilgrim på havet → Det heliga landet → Mariamne 用一条 1956–1967 时间线串起，配 Barabbas 书影做锚。
- **emoji/符号**：★/· 等 U+2605 符号在 lmodern 斜体下缺字（数学侧经验），正文避免；用 tikz 小圆点代替装饰符。

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
