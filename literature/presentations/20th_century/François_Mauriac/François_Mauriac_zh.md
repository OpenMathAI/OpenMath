# 文学家立传提示词（François Mauriac / 弗朗索瓦·莫里亚克）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：François Charles Mauriac（弗朗索瓦·莫里亚克），法国小说家/剧作家/批评家/诗人/记者，法兰西学院院士，1952 年诺贝尔文学奖得主。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**天主教小说中"罪与恩宠"的家庭心理戏剧**与其公共知识分子的双重形象上。

---

## 二、背景信息 【人物专属】

- **目标文学家**：François Charles Mauriac（1885-10-11 ~ 1970-09-01，享年 84 岁）
- **诺奖年份**：1952 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for the deep spiritual insight and the artistic intensity with which he has in his novels penetrated the drama of human life"
  > （中译：表彰其小说深入人生之戏剧所体现的精神洞察与艺术强度）
- **气质关键词**：**天主教小说家、波尔多的解剖者、抵抗的声音**
- **设计母题**：**毒蛇结中的恩宠（grace within the knot of vipers）**——以"阴暗宅邸内一束斜光"的意象图式呼应其小说世界的空间（波尔多的房产、家庭牢笼）与神学张力（罪/恩宠）。
- **本地数据源**：`literature/presentations/pages/20th_century/François_Mauriac/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Fran%C3%A7ois_Mauriac
- **肖像**：第 0 步待下载（1933 年照片，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1885-10-11 生于波尔多 ~ 1970-09-01 逝于巴黎，享年 84 岁；葬于瓦兹河谷省 Vémars 墓园。
- 国籍：法国。本名 François Charles Mauriac（奥克语形式 Francés Carles Mauriac）。
- 教育：波尔多大学文学（1905 年毕业）→ 巴黎文献学院（École des Chartes，1908 年短暂就读）。
- 家庭：子 Claude Mauriac（作家）；孙女 Anne Wiazemsky（演员/作家，让-吕克·戈达尔合作者及妻子）。妻子姓名 page.md 无载，**禁写**。波尔多以南约 50 km 的 Malagar 庄园现为国家古迹（Centre François Mauriac）。
- 关键荣誉：Grand Prix du roman de l'Académie française（1926，《Le Désert de l'amour》）；法兰西学院院士（1933-06-01 当选，接替 Eugène Brieux）；诺贝尔文学奖 1952；荣誉军团大十字（Grand Cross of the Légion d'honneur，1958）。
- 核心作品与贡献（4–6 条）：
  1. 诗集《Les Mains jointes》（1909）起步；
  2. 《Le Baiser au lépreux》（1922）、《Génitrix》（1923）——家庭牢笼中的罪与恩宠；
  3. 《Thérèse Desqueyroux》（1927）——最具国际知名度的小说（1947/2005 两度英译重出，1962 年电影）；
  4. 《Le Nœud de vipères》（1932）——毒蛇结，书信体忏悔小说；
  5. 剧作《Asmodée》（1938）；传记《Life of Jesus》（1937）、《De Gaulle》（1964）；
  6. 二战抵抗文本：1941-12 起加入抵抗运动，是唯一在 Editions de Minuit 出版抵抗文本的法兰西学院院士；战后在《Le Figaro》专栏、促成 Elie Wiesel 写出《Night》并作序。
- 关键时间线（15–20 节点）：
  1. 1885 生于波尔多；
  2. 1905 波尔多大学毕业；
  3. 1908 巴黎文献学院短暂就读；
  4. 1909 首部诗集《Les Mains jointes》；
  5. 1913 《L'Enfant chargé de chaînes》；
  6. 1922 《Le Baiser au lépreux》成名；
  7. 1925 《Le Désert de l'amour》→ 1926 获法兰西学院小说大奖；
  8. 1927 《Thérèse Desqueyroux》；
  9. 1932 《Le Nœud de vipères》；
  10. 1933-06-01 当选法兰西学院院士（接替 Eugène Brieux）；
  11. 1937 《Life of Jesus》；
  12. 1938 剧作《Asmodée》；
  13. 1941-12 加入抵抗运动；Editions de Minuit 抵抗文本（院士中唯一）；
  14. 战后与加缪关于清算（épuration）的著名论战（《Combat》vs《Le Figaro》）；为 Brasillach 求情免死；
  15. 1950–1956 十二卷本全集出版；
  16. 1952 获诺贝尔文学奖；同年小说《Galigaï》；
  17. 1953–58 与 Roger Peyrefitte 公开论战；
  18. 1958 获荣誉军团大十字；
  19. 1960 《Mémoires intérieurs》；1964 《De Gaulle》传记；
  20. 1970-09-01 卒于巴黎。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | catholic novel | 天主教小说 | 罪与恩宠的精神戏剧（官方诺奖理由核心） | 核心页 |
| 1 | psychological fiction | 心理小说 | 家庭牢笼中的欲望与压抑解剖 | 核心页 |
| 2 | literary criticism | 文学批评 | 专栏与批评文集 | 批评页 |
| 3 | poetry | 诗歌 | 《Les Mains jointes》起步 | 诗歌页 |
| 4 | drama | 戏剧 | 《Asmodée》《Les Mal Aimés》 | 戏剧页 |

#### 4.1 入库操作

- 新建 `people` 记录（name_en=`François Mauriac`，qid=Q81685），`primary_occupation='writer'`、`has_social_data=1`
- occupations：writer(0)、novelist(1)、journalist(2)
- 5 个领域写入 `person_field`（catholic novel / psychological fiction 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。妻子无名不入库；Georges Bernanos / Julien Green 仅 See also 相关链接，不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Claude Mauriac | 本人→对方 | 子，作家 |
| parent-child | Anne Wiazemsky | 本人→对方 | 孙女，演员/作家 |
| colleague | Eugène Brieux | 无向 | 1933 年接替其法兰西学院席位 |
| colleague | Elie Wiesel | 无向 | 鼓励其写下大屠杀经历，为《Night》作序 |
| colleague | Charles de Gaulle | 无向 | 为其作传记《De Gaulle》 |
| controversy | Albert Camus | 无向 | 解放后关于清算问题的公开论战（Combat vs Le Figaro） |
| controversy | Robert Brasillach | 无向 | 曾遭其恶评，但 Mauriac 为其求情免于死刑 |
| controversy | Roger Peyrefitte | 无向 | 关于教会批评的公开论战，Peyrefitte 发公开信攻讦 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#283593`（靛蓝——法兰西学院正装蓝与天主教内省）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeNovel 靛蓝 `#4C5FD5`；badgeFaith 青绿 `#0E7C7B`；badgePress 琥珀 `#E07B30`；badgeDrama 玫瑰 `#C4204F`
- **背景母题**：暗宅斜光（大面积深色 + 单侧金色光带）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 罪与恩宠的解剖者 / François Mauriac 1885–1970 + badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/教育/法兰西学院/荣誉/核心领域）
03  核心创作概览 — 天主教小说 / 心理小说 / 诗歌与戏剧 / 专栏与传记
04  早年：波尔多与巴黎 (1885–1909)
05  成名：《麻风病人的吻》与《母亲大人》 (1922–1927)【书影】
06  《苔蕾丝·德斯盖鲁》与《毒蛇结》 (1927–1932)【意象图式：毒蛇结】
07  法兰西学院院士与《基督生活》 (1933–1938)
08  占领与抵抗 (1940–1945)——Editions de Minuit、院士中唯一
09  战后论战：与加缪、为 Brasillach 求情 (1944–1952)——客观事实简述
10  1952 诺贝尔文学奖 — 官方理由 EN 原文页
11  晚年与遗产：Wiesel《Night》序、Malagar、两项 Mauriac 奖 (1958–1970)
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一 `mainclr/accentclr/badgeA..D/panelA..D`；引文框 tcolorbox；身份页 `\profileslide`。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 妻子无名 | page.md 未载妻子姓名（infobox 只有孙女），禁编名字与婚姻年份 |
| 政治立场演进 | "曾任 Action française 支持者→西班牙内战期间左转→短暂支持贝当→1941-12 加入抵抗"——按 page.md 时间线客观呈现，不作政治评价 |
| 阿尔及利亚/印度支那 | 反对法国在印度支那统治、谴责阿尔及利亚酷刑——一句话客观事实，不展开 |
| Brasillach 求情 | 是"曾遭其恶评却为其求情"——方向勿写反 |
| 与加缪论战 | 主题是清算（épuration）与民族和解，不是文学论战；Camus 编《Combat》，Mauriac 写《Le Figaro》专栏 |
| Thérèse 年份 | 1927 年小说；英译三版（1928/1947/2005）勿混 |
| 全集卷数 | 十二卷（1950–1956），勿写"10 卷" |
| Grand Prix 获奖作 | 1926 大奖是因《Le Désert de l'amour》(1925)，勿记成《Thérèse》 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Le Nœud de vipères | 毒蛇结 | 书信体忏悔小说 |
| Thérèse Desqueyroux | 苔蕾丝·德斯盖鲁 | 主人公姓名即书名 |
| Académie française | 法兰西学院 | 1933 当选，接替 Eugène Brieux |
| épuration | 战后清算 | 与加缪论战主题，政治术语慎用 |
| Éditions de Minuit | 子夜出版社 | 抵抗运动地下出版社 |
| Légion d'honneur | 荣誉军团勋章 | 1958 大十字 |
| Grand Prix du roman | 法兰西学院小说大奖 | 1926 |
| Malagar | 马拉加尔庄园 | 现为 Centre François Mauriac |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions
- **匹配理由**：Awaken 的"觉醒/晨光"气质对应 Mauriac 精神戏剧的核心——恩宠在罪性中的降临；由暗至明的推进匹配"毒蛇结中开出一束光"的设计母题。
- **本地路径**：`music_audio/alex-productions/` 下 Awaken 对应 wav → `presentations/20th_century/François_Mauriac/Awaken.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/François_Mauriac/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/François_Mauriac/images.txt` | 肖像/插图 URL 清单（含诺奖证书照片） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_20th_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/François_Mauriac.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（Awaken 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox 1933 年照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `François_Mauriac/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=François_Mauriac_zh`、`VIDEO_NAME=François_Mauriac_zh`
4. ☐ 第 3 步：复制 Awaken.wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2，已完成）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#283593）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写；政治页措辞复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

## 七、版式补遗 【人物专属】

- **作品表页排版**：Mauriac 作品跨小说/戏剧/诗歌/回忆录/传记/批评六类——每类取代表 2–3 行（小说类取 Le Baiser au lépreux / Thérèse Desqueyroux / Le Nœud de vipères / La Pharisienne），勿全量塞入；法语书名斜体 + 括注英译。
- **书影/插图素材**：诺奖证书照片（Le diplôme de François Mauriac，page.md 内嵌 250px 版，可取 Commons 原图）、Vémars 墓园照片（遗产页用）。
- **战后论战页排版**：与加缪、Peyrefitte、Brasillach 三条争议并列时用三栏 panel，每栏一句事实，标题中性（"解放后的论战"），避免渲染。
- **引文红线**：page.md 无 Mauriac 英文原话（无直接引语）——全篇禁用"他说"式引语，评述一律转述。
- **同类作家区分**：See also 中 Georges Bernanos / Julien Green（同为天主教小说家）仅可在"语境"页一提"与 Bernanos、Green 并列被视为法国天主教小说代表"（page.md 以 See also 呈现，措辞降为"常被并列提及"），关系不入库。

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
