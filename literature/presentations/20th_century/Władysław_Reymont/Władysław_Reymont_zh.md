# 文学家立传提示词（OpenLiterature 实例：Władysław Reymont）

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：Władysław Reymont（弗瓦迪斯瓦夫·雷蒙特，1924 诺贝尔文学奖，波兰民族史诗《农民》的作者）。
- **设计哲学**：文学家立传以「名句引文框 + 四季意象图式」替代公式框；身份信息页与领域结构化表达保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Władysław Stanisław Reymont（本名 Stanisław Władysław Rejment，1867-05-07 生于 Kobiele Wielkie，时属俄罗斯帝国波兰会议王国 ~ 1925-12-05 卒于华沙，享年 58 岁）
- **1924 官方获奖理由**（禁止改写）：
  > EN（nobelprize.org 官方口径）: "for his great national epic, The Peasants"
  > 中译（CITATION_ZH, key=("1924","Władysław Reymont")）：表彰其伟大的民族史诗《农民》
- **气质关键词**：**自学成才的土地歌者、工业城市的批判者、四季循环的史诗建筑师**
- **设计母题**：**四季之环（The Peasants 四卷：夏秋冬春）**。小说以乡村一年四季为结构——用麦穗、犁铧、雪原与教堂历法的环形图式统摄封面与章节页。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Władysław_Reymont/page.md`（事实基准）
  - `literature/presentations/pages/20th_century/Władysław_Reymont/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/W%C5%82adys%C5%82aw_Reymont
  - 肖像（第 0 步待下载）：真实照片充足——1897 照（infobox）、Wyczółkowski 绘肖像、Malczewski 1905 绘肖像、《农民·秋》手稿照（插图）

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1867-05-07 生于 Kobiele Wielkie（近 Radomsko）；1925-12-05 卒于华沙，享年 58；葬 Powązki 公墓；心脏瓮安放于华沙圣十字教堂立柱
- **国籍**：Russian Empire（生）→ Second Polish Republic（frontmatter 双值按变迁分条）
- **家庭**：九子之一；父 Józef Rejment 为管风琴师；母 Antonina Kupczyńska 擅讲故事（出身克拉科夫地区没落贵族）；1902 娶 Aurelia Szacnajder Szabłowska（1900 铁路事故疗养期间照护他的看护，婚前先为其解除前一段婚姻）
- **教育与经历**：父送其学裁缝，1885 通过出师考试（唯一正式学历证书）；却一天裁缝也没做过——省巡游剧团演员、铁路道口看守（Koluszki，月薪 16 卢布）、1888 随德国灵媒赴巴黎/伦敦、两度出走、一度想入 Częstochowa 保禄会
- **文学师承与影响**：无师承（自学成才，page.md 将其与 Mikołaj Rej、Aleksander Fredro 并列为波兰自学作家）；1892 年《Głos》刊其通讯后返华沙，结识赏识其才华的作家（含 Świętochowski）
- **文学运动**：Realism（infobox Genre）；归属 Young Poland（青年波兰）运动——颓废与文学印象主义底色；自然主义是亲历生活的记录而非「借来的」
- **关键荣誉**：Nobel 1924；Polonia Restituta 官勋章（军官/指挥官/大十字）；白鹰勋章；荣誉军团指挥官
- **核心作品与贡献（4–6 条）**：
  1. 《Komediantka》（The Deceiver，1895/96）——外省少女与巡游剧团
  2. 《Ziemia obiecana》（The Promised Land，1898/99）——罗兹工业城的生存竞技场（德/犹/波三主角），至少 15 种语言、两次电影改编（1927、1975 Wajda）
  3. 《Chłopi》（The Peasants，1904–1909 四卷）——民族史诗，方言入叙述，至少 27 种语言、两次拍片；1924 诺奖核心
  4. 《Rok 1794》三部曲（1911–1917/1914–1919）——科希丘什科起义史诗
  5. 《Bunt》（Revolt，1922 连载/1924 成书）——动物夺农场寓言，暗喻 1917 布尔什维克革命，1945–1989 在共产主义波兰与《动物庄园》同遭查禁（政治内容只客观一笔）
  6. 报告文学《Pielgrzymka do Jasnej Góry》（1895）——琴斯托霍瓦朝圣经典游记
- **关键时间线（15–20 节点）**：
  1. 1867-05-07 生于 Kobiele Wielkie，管风琴师之家
  2. 童年随父迁 Tuszyn（近罗兹）
  3. 1885 华沙裁缝出师考试通过
  4. 弃职加入省巡游剧团
  5. 铁路道口看守（Koluszki）
  6. 1888 随德国灵媒赴巴黎、伦敦
  7. 再度加入剧团，无成而返
  8. 1892 《Głos》刊 Korespondencje，返华沙
  9. 1894 十一天琴斯托霍瓦朝圣
  10. 1895 《Pielgrzymka do Jasnej Góry》刊出；《Komediantka》
  11. 1896/1897 《Fermenty》
  12. 1898/1899 《Ziemia obiecana》（Kurier Codzienny 约稿，罗兹取材）
  13. 1900 华沙-维也纳铁路事故重伤，获 40,000 卢布赔偿，写作中断至 1904
  14. 1902 娶 Aurelia Szabłowska
  15. 1901–1908 部分在法国写作《Chłopi》；1904–1909 四卷出齐
  16. 1911/1912 《Wampir》（评论冷淡）；Sieradz 购地经营失败
  17. 1911–1917 《Rok 1794》三部曲
  18. 1919 应波兰政府资助访美
  19. 1920 于 Kołaczkowo（波兹南附近）购宅邸
  20. 1922/1924 《Bunt》
  21. 1924-11 获诺贝尔文学奖（Österling 提名）；因心脏病不能赴典，奖章与 116,718 克朗支票寄至养病的法国
  22. 1925 赴 Wierzchosławice 农民集会（Witos 迎为 Piast 党人）；旋即病重
  23. 1925-12-05 卒于华沙；葬 Powązki；心脏瓮入圣十字教堂

### 第 1 步：建立目录 【模板通用】

- 创建 `literature/presentations/20th_century/Władysław_Reymont/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设 `MAIN=Władysław_Reymont_zh`、`VIDEO_NAME=Władysław_Reymont_zh`

### 第 3 步：收集图片 【人物专属】

- 主肖像：1897 照 500px（curl -A + file 验证）；插图可选 Wyczółkowski/Malczewski 绘肖像与《农民·秋》手稿照（图注注明）

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | realism | 现实主义 | infobox Genre；亲历生活的记录 | 核心页 |
| 1 | epic novel | 史诗小说 | 《农民》四部曲，诺奖理由核心 | 史诗页 |
| 2 | social criticism | 社会批评 | 《应许之地》的工业化批判 | 批判页 |
| 3 | naturalism | 自然主义 | 评论界指认但强调非「借来的」 | 风格页 |
| 4 | reportage | 报告文学 | 朝圣游记与通讯 | 游记页 |

- 入库：`MySQL/data/Władysław_Reymont.yaml` → `python3 seed_person.py data/Władysław_Reymont.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Aurelia Szabłowska | 无向 | 1902 结婚；1900 铁路事故疗养期间照护他 |
| colleague | Aleksander Świętochowski | 无向 | 1892 返华沙后赏识其才华的作家 |
| colleague | Stefan Żeromski | 无向 | 巴黎流亡波兰作家圈交往；1924 波兰舆论曾支持其获奖但奖归 Reymont |
| colleague | Stanisław Przybyszewski | 无向 | 巴黎流亡波兰作家圈交往 |
| colleague | Lucjan Rydel | 无向 | 巴黎流亡波兰作家圈交往 |
| colleague | Jan Lorentowicz | 无向 | 巴黎流亡波兰作家圈交往 |

**禁写**：Thomas Mann / George Bernard Shaw / Thomas Hardy 是 1924 评奖竞争者（page.md 原文 rivals）——属评奖过程事实，**不建 rival 关系行**，只在诺奖页一句带过；Anders Österling 系提名院士，不建行；Wincenty Witos 与 Piast 党一事只客观一笔，不建行；George Orwell《动物庄园》是平行作品对照，非二人关系，不建行；共产主义波兰时期的流行与查禁只客观陈述，不作政治评价。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：#4E342E（大地棕——泥土与木犁）+ 诺奖香槟金 `C9A227`
- **badgeA** 史诗小说 — 深棕 `#4E342E`；**badgeB** 现实主义 — 青绿 `#0E7C7B`；**badgeC** 社会批评 — 琥珀 `#E07B30`；**badgeD** 报告文学 — 靛蓝 `#1E4E79`
- **背景母题**：四季环形图（春耕/夏收/秋藏/冬雪四扇区）+ 麦穗剪影稀疏点缀

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 四季之环的史诗歌手 / Władysław Reymont 1867–1925 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名 Rejment、生卒、裁缝出师、婚姻、荣誉）
03  核心贡献概览 — 现实主义 / 史诗 / 社会批评 / 报告文学
04  出走者（1867–1892）— 裁缝出师证、剧团演员、道口看守、灵媒随行
05  华沙起点（1892–1898）— Głos 通讯、Komediantka / Fermenty
06  《应许之地》（1898/99）— 罗兹工业城三主角（社会批评页）
07  事故与转机（1900–1904）— 铁路重伤、赔偿金、婚姻
08  《农民》四卷（1904–1909）— 四季环形结构图式页（诺奖核心）
09  《农民》何以伟大 — 方言入叙述、永恒轮回的时间观、27 种语言
10  历史与寓言 — Rok 1794 三部曲 / Bunt（客观一笔：1945–1989 查禁）
11  1924 诺贝尔奖 — 官方理由 EN+中译；缺席受奖（奖章寄法国）
12  最后一年（1925）— Wierzchosławice 集会、病重、华沙辞世；心脏瓮入圣十字教堂
13  遗产：波兰民族史诗的坐标
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 身份页用 `\profileslide` 模式；四季图式页用 tikz 扇形环；引文框半角引号

### 第 8 步：布局检查 【模板通用】

- 每页 make + pdftoppm 目检；书目表格页防 vbox 溢出（itemize 压行距）

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Reymont 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名 | Stanisław Władysław Rejment（Reymont 为笔名化用），勿混 |
| 学历 | 唯一正式证书是 1885 裁缝出师证——自学成才叙事的锚点，勿写成「受过文学教育」 |
| 四卷顺序 | 《农民》按 夏/秋/冬/春 出卷（Chłopi 卷序以原文为准），叙事季节从秋起——注意与「四季之环」图式页区分 |
| 事故年份 | 1900 铁路事故、40,000 卢布赔偿——写作中断至 1904，勿写成年份错位 |
| 婚姻 | 婚前为 Aurelia 解除前婚——细节可略，勿编造成浪漫故事 |
| 评奖竞争 | Mann/Shaw/Hardy 是竞争者，禁写成「击败的对手朋友」 |
| 缺席受奖 | 因心脏病未赴斯德哥尔摩，奖章与支票寄至法国——勿写成「拒绝领奖」 |
| Bunt | 查禁时段 1945–1989；与《动物庄园》平行——只客观陈述 |
| 心脏瓮 | 葬 Powązki、心脏入圣十字教堂——两处勿混 |
| 心脏/宗教细节 | 保禄会念头只是早年一段，勿写成皈依事件 |
| 政治内容 | 苏俄革命暗喻与共产主义波兰评价一律不作展开（workflow 红线） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Chłopi / The Peasants | 《农民》 | 四卷民族史诗，1924 诺奖核心 |
| Ziemia obiecana / The Promised Land | 《应许之地》 | 罗兹工业城题材 |
| Young Poland | 青年波兰 | 文学运动归属 |
| realism / naturalism | 现实主义/自然主义 | 并存而非等号 |
| literary impressionism | 文学印象主义 | Young Poland 底色 |
| reportage | 报告文学 | 朝圣游记体裁 |
| Congress Poland | 波兰会议王国 | 出生地时属俄罗斯帝国 |
| szlachta | 波兰贵族（没落） | 母系出身背景 |
| Jasna Góra | 光明山（琴斯托霍瓦） | 1894 朝圣目的地 |
| Powązki Cemetery | 波瓦兹基公墓 | 安葬地 |
| Wierzchosławice | 维尔霍斯瓦维采 | 1925 农民集会地 |
| Bunt / Revolt | 《叛乱》 | 动物寓言，查禁史客观处理 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（分批文件预分配）
- **匹配理由**：粗粝原始的器乐质感匹配《农民》直面土地、劳作与生存野性的史诗力量，也匹配《应许之地》工业丛林「弱肉强食」的暗面书写——Reymont 的现实主义从不粉饰。
- **本地路径**：按 `music_audio/curated_tracks.md` 对应文件复制为本目录 `Savage.wav`
- **时长**：以曲目实际长度与成片页数对齐（ffmpeg `-shortest`）
