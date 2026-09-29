# 文学家立传提示词（OpenLiterature：Henryk Sienkiewicz）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Henryk Sienkiewicz（1905 诺贝尔文学奖，史诗作家）为实例。
> 结构对齐母本 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Henryk Adam Aleksander Pius Sienkiewicz（亨利克·显克维支），1905 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传强调「代表作与文学世界」的结构化表达 + 身份信息页；显克维支的核心视觉语言是**史诗叙事**——17 世纪波兰-立陶宛联邦的战火、尼禄治下罗马的早期基督徒、被瓜分的波兰民族精神。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Henryk Sienkiewicz（1846-05-05 ~ 1916-11-15，享年 70 岁）
- **气质关键词**：**史诗作家、民族叙事者、世界级畅销家** —— 1905 诺贝尔文学奖获奖理由：
  > EN 原文（官方，禁止改写）: "for his outstanding merits as an epic writer"（因其作为史诗作家的杰出功绩）
  > 中译（CITATION_ZH）: 表彰其作为史诗作家的杰出功绩
- **设计母题**：**战火与史诗（epic fire）**。《三部曲》的十七世纪战马与军刀、《你往何处去》尼禄罗马的大火、被瓜分波兰不灭的民族之火——以火焰/勋章/羊皮卷意象贯穿全篇。
- **本地数据源**：`literature/presentations/pages/20th_century/Henryk_Sienkiewicz/page.md`（+ `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Henryk_Sienkiewicz （肖像第 0 步**待下载**，infobox 有 c. 1885 照片与 1890 Pochwalski 肖像画）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）

---

## 三、任务流程 【逐步执行，每完成一步汇报】

### 第 0 步：事实基准（第一轮已核对 page.md）

- **生卒**：1846-05-05 生于 Wola Okrzejska（卢布林省，俄罗斯帝国治下的波兰会议王国）~ 1916-11-15 卒于瑞士沃韦（Vevey）Grand Hotel du Lac，死因缺血性心脏病；1924 年遗骸归葬华沙圣约翰主教座堂
- **国籍**：俄罗斯帝国（波兰会议王国）——1924 年归葬时波兰已复国
- **家庭**：没落波兰贵族（Szlachta），父 Józef Sienkiewicz、母 Stefania Cieciszowska；父系源自立陶宛鞑靼（Lipka Tatars）；兄 Kazimierz 死于 1863-64 一月起义
- **婚姻**：1881 娶 Maria Szetkiewicz（1885 死于肺结核，子女 Henryk Józef 与 Jadwiga Maria）；1893 娶 Maria Romanowska-Wołodkowicz（两周后离异，1895 教宗准予解除）；1904 娶侄女 Maria Babska
- **教育**：华沙大学（帝国大学）医学→法律→语文学与历史系；1871 完成学业但因古希腊语考试未过未获文凭
- **笔名**：Litwos
- **文学师承与影响**：无导师制师承；属波兰实证主义（Positivism）阵营但立场保守；与 Young Poland 运动交恶（page 明载）
- **任职/经历**：1869 步入新闻界（《Weekly Review》《Illustrated Weekly》《Gazeta Polska》《Niwa》）；1881-1887 任《Słowo》主编（至 1892 仍任文学版编辑）；1876-1878 赴美（随女演员 Helena Modrzejewska，加州阿纳海姆，为《Gazeta Polska》写旅行通信）
- **关键荣誉**：Nobel 1905（Hans Hildebrand 提名）；Légion d'honneur 1904；Jagiellonian 名誉博士 1900、Lwów 名誉博士 1911；Lwów 荣誉市民 1902；多国科学院院士（Polish Academy of Learning、俄、塞尔维亚等）；1900 写作 25 周年获全国赠 Oblęgorek 庄园
- **核心作品与贡献**：
  1. 小三部曲（Stary Sługa 1875 / Hania 1876 / Selim Mirza 1877）
  2. 《三部曲》：With Fire and Sword 1884 / The Deluge 1886 / Sir Michael 1888（17 世纪波兰-立陶宛联邦）
  3. 《Without dogma》（Bez dogmatu, 1891）——伪日记体自省小说实验
  4. 《Quo Vadis》（1896）——尼禄罗马与早期基督徒，国际畅销（至少 40 种语言，美国 18 个月 80 万册）
  5. 《条顿骑士团》（Krzyżacy, 1900）——1410 格伦瓦尔德之战
  6. 《In Desert and Wilderness》（1910-11）——青少年文学经典
- **关键时间线**（15–20 节点）：1846 生于 Wola Okrzejska → 1858 赴华沙求学 → 1866 中学毕业（医学→法律→语文史）→ 1869 新闻界出道 → 1872 小说处女作《Na Marne》→ 1874 合作翻译雨果《九三年》→ 1876-78 美国之旅（Modrzejewska 同行）→ 1879 归国巡回演讲 → 1881 与 Maria Szetkiewicz 成婚、任《Słowo》主编 → 1883-88 三部曲连载（Słowo）→ 1885 妻逝 → 1891《Without dogma》→ 1893 万吨卢布匿名赠金（化名 Michał Wołodyjowski）设结核救助基金 → 1895-96《Quo Vadis》→ 1900《条顿骑士团》+ 25 周年庆典得 Oblęgorek → 1904 Légion d'honneur、与 Maria Babska 成婚 → 1905 诺贝尔奖（受奖演说：波兰被宣告死亡——而她活着；被宣告战败——而她胜利）→ 1907 抗议德占区没收波兰土地 → 1914 赴瑞士战时救济（与 Paderewski 等）→ 1916-11-15 卒于沃韦 → 1924 归葬华沙

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | historical novel | 历史小说 | 三部曲/条顿骑士团，17 世纪波兰史诗 | 核心页 |
| 1 | epic fiction | 史诗小说 | 1905 诺奖官方理由的核心词 | 封面、诺奖页 |
| 2 | short story | 短篇小说 | 《灯塔看守人》《杨科·音乐家》等 | 短篇页 |
| 3 | travel literature | 旅行文学 | 美国通信/非洲通信 | 美国页 |
| 4 | literary journalism | 文学新闻写作 | 四十年报刊生涯，Litwos 专栏 | 早年页 |

#### 4.1 入库操作
- `MySQL/data/Henryk_Sienkiewicz.yaml` → `python3 MySQL/seed_person.py data/Henryk_Sienkiewicz.yaml`
- `primary_occupation='writer'`、occupations：writer(0)/novelist(1)/journalist(2)；nationalities：Russian Empire(0)/Poland(1)
- 校验 fields≥4、relations≥2、has_social_data=1

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Maria Szetkiewicz | 无向 | 1881-1885，死于肺结核，育二子女 |
| spouse | Maria Babska | 无向 | 1904 成婚，为其侄女 |
| colleague | Helena Modrzejewska | 无向 | 女演员挚友，1876 同赴美国 |
| colleague | Jeremiah Curtin | 无向 | 英译者，助其作品走向国际 |
| colleague | Ignacy Jan Paderewski | 无向 | 一战同创波兰战时救济组织 |

### 第 5 步：设计配色

- **主色**：深蓝 `#2A4B7C`（ partition 时代波兰的沉郁与史诗感）+ 诺奖香槟金 `C9A227`
- badgeA 史诗小说 — 猩红 `#8B1A1A`；badgeB 短篇 — 青绿 `#0E7C7B`；badgeC 旅行 — 琥珀 `#E07B30`；badgeD 新闻 — 玫瑰 `#C4204F`
- **背景母题**：羊皮卷纹理 + 稀疏余烬圆点（呼应"战火与史诗"）

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享封面）
01  封面 — 史诗作家 / Henryk Sienkiewicz 1846–1916 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/笔名/教育/婚姻/任职/荣誉/核心领域）
03  核心贡献概览 — 三部曲 / Quo Vadis / 条顿骑士团 / 短篇与旅行文学
04  早年：没落贵族之子 (1846–1869) — 五兄妹/一月起义/华沙求学/语文史转向
05  新闻界与 Litwos (1869–1876) — 三专栏/Niwa 共有/小三部曲
06  美国岁月 (1876–1878) — Modrzejewska/加州/旅行通信（引文框：书信体意象）
07  三部曲：十七世纪战火 (1883–1888) — With Fire and Sword / The Deluge / Sir Michael
08  Quo Vadis：尼禄罗马的大火 (1896) — 早期基督徒/国际畅销（名句引文框替代公式框）
09  条顿骑士团与格伦瓦尔德 (1900) — 1410/民族叙事
10  1905 诺贝尔奖 — 官方理由 EN+中译 / 受奖演说"波兰活着"
11  民族之声与慈善 — Germanization 抗争/Oblęgorek 学校/结核基金
12  晚年与一战 (1910–1916) — In Desert and Wilderness/瑞士救济/沃韦辞世
13  遗产：归葬与经典化 (1924–) — 圣约翰座堂/电影改编/波兰必读
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方为 "his outstanding merits as an epic writer"，**不点名 Quo Vadis**；page 明文 "often incorrectly asserted"——勿写成"因《你往何处去》获奖" |
| 出生地 | Wola Okrzejska 属俄罗斯帝国治下波兰会议王国（今波兰卢布林省），勿写"波兰共和国" |
| 卒日/卒地 | 1916-11-15 卒于瑞士 Vevey（非波兰）；1924 才归葬华沙 |
| 三部曲第三卷 | 英名 Sir Michael（Pan Wołodyjowski），勿写成其他 |
| 婚姻 | 共三次：Szetkiewicz(1881-85)/Romanowska(1893, 两周即离)/侄女 Babska(1904)，勿漏勿混 |
| 政治内容 | Germanization 抗争、1916 Act of 5th November 背书——按 page.md 客观事实一句带过，**不展开政治叙事、不作评价** |
| 引语红线 | 受奖演说引语仅限 page.md 英文原句（"She was pronounced dead – yet here is proof that she lives on...."）；Chekhov/Gombrowicz 负评仅可作小注，不得引申 |
| 同名区分 | Maria Romanowska-Wołodkowicz 与 Maria Babska 是两人；作家 Bolesław Prus 仅得他一篇书评（page 明载），**非密友禁建关系** |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| epic writer | 史诗作家 | 诺奖理由核心词，勿译"叙事作家" |
| the Trilogy | 三部曲 | 1884-1888 三卷 |
| Quo Vadis | 你往何处去 | 拉丁语"主啊，你往哪里去" |
| Positivism | （波兰）实证主义 | 19 世纪波兰文学运动，非哲学实证主义 |
| Litwos | Litwos（笔名） | 直用原名 |
| Szlachta | 波兰贵族 | 没落贵族 |
| Germanization | 日耳曼化 | 政治敏感，客观转述 |
| Congress Poland | 波兰会议王国 | 俄属，勿与今波兰混 |

---

## 四、BGM 建议

- **选定曲目**: **SEA** — Alex-Productions（75k views，高受众 / 流动 / 平稳）
- **匹配理由**: "流动/平稳" 匹配显克维支的史诗长卷气质——三部曲三十年连载、Quo Vadis 跨文明叙事，如江河奔涌而气度沉稳；"高受众" 匹配其 turn-of-the-century 世界级畅销作家身份（40 种语言译本、美国 18 个月 80 万册）
- **备选**（未采用）: Eternals（宏大/长期影响，但受众 49k 偏低）；The Flow of Time（时间感合适但留给 Kipling 篇）
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Henryk_Sienkiewicz/page.md` | 事实基准 |
| `MySQL/data/Henryk_Sienkiewicz.yaml` | 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每写一页就 make，看到溢出就修。**
