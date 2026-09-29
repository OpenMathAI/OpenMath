# 文学家立传提示词（OpenLiterature：Rudolf Christoph Eucken）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Rudolf Christoph Eucken（1908 诺贝尔文学奖，唯二以哲学家身份获文学奖者之一）为实例。
> 结构对齐母本 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用**哲思金句框 / 概念图式 / 书影**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Rudolf Christoph Eucken（鲁道夫·克里斯托弗·奥伊肯），1908 年诺贝尔文学奖得主、德国哲学家。
- **设计哲学**：文学家立传强调「代表作与思想世界」+ 身份信息页；奥伊肯的核心视觉语言是**精神生活（Geistesleben）**——从哥廷然的语文学讲席到耶拿四十六年的讲台、伦理行动主义（ethical activism）的上升阶梯、大战前后国际学人共同体的兴衰。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Rudolf Christoph Eucken（1846-01-05 ~ 1926-09-15，享年 80 岁）
  - ★ 日期裁定：生 01-05、卒 09-15 以 infobox/正文为准（frontmatter 有 09-14 与 00-00 噪声，弃用）
- **气质关键词**：**理想主义人生哲学、伦理行动主义、讲坛哲人** —— 1908 诺贝尔文学奖获奖理由：
  > EN 原文（官方，禁止改写）: "in recognition of his earnest search for truth, his penetrating power of thought, his wide range of vision, and the warmth and strength in presentation with which in his numerous works he has vindicated and developed an idealistic philosophy of life"
  > 中译（CITATION_ZH）: 表彰其对真理的热切求索、深邃的思想力与开阔的视野，以及在众多著作中以温暖而有力的表述捍卫并发展理想主义人生哲学
- **设计母题**：**精神阶梯（spiritual ascent）**——人立于自然与精神之交、以持续努力克服非精神性本性的意象；用阶梯/光柱/书店与讲坛的图式替代物理学的公式框。
- **本地数据源**：`literature/presentations/pages/20th_century/Rudolf_Christoph_Eucken/page.md`（+ `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Rudolf_Christoph_Eucken （肖像第 0 步**待下载**；注意 infobox 本身无照片，需从 images.txt/Wikidata P18 或装饰圆占位）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）

---

## 三、任务流程 【逐步执行，每完成一步汇报】

### 第 0 步：事实基准（第一轮已核对 page.md）

- **生卒**：1846-01-05 生于 Aurich（汉诺威王国，今下萨克森）~ 1926-09-15 卒于耶拿
- **国籍**：德国（历经普鲁士/德意志帝国/魏玛共和国；出生时为汉诺威王国）
- **家庭**：父 Ammo Becker Eucken 早逝，由母 Ida Maria（née Gittermann）抚养成人；1882 娶 Irene Passow，育一女二子——子 Walter Eucken（秩序自由主义经济学奠基人）、子 Arnold Eucken（化学家兼物理学家）
- **教育**：Aurich 就学（教师含古典语文学家 Reuter）→ 哥廷根大学 1863-1866 → 柏林大学（Trendelenburg 的伦理倾向与哲学史讲法深引其心）
- **师承**（page 明载）：Hermann Lotze（哥廷根教师，infobox 列于 academic advisors）、Gustav Teichmüller（哥廷根教师，后其在巴塞尔讲席的前任）、F. A. Trendelenburg（柏林）
- **弟子**（page 明载）：Max Scheler（infobox doctoral students）
- **任职**：Husum/柏林/法兰克福中学教师五年 → 1871 巴塞尔大学哲学教授（竞选中击败 Nietzsche 而获任，接任其师 Teichmüller）→ 1874 转耶拿大学直至 1920 退休 → 1912-13 哈佛交换教授、1913 NYU Deem 讲座 → 1911 赴英讲学
- **关键荣誉**：Nobel 1908（瑞典学院成员提名）；Kiel 哲学奖（Beiträge 1905 版获奖——page 未载者禁写）
- **哲学立场**：哲学即人生哲学（philosophy of life）；构造"伦理行动主义"（ethical activism / Aktivismus）；人具灵魂、处于自然与精神之交；一战中为其国家立场强烈发声——大战摧毁了原本的国际学者共同体（page 原句）
- **核心作品与贡献**：
  1. *Die Methode der aristotelischen Forschung*（1872）
  2. *Die Einheit des Geisteslebens*（1888）
  3. *Die Lebensanschauungen der großen Denker*（1890；英译 The Problem of Human Life, 1909）——最负盛名之作
  4. *Der Kampf um einen geistigen Lebensinhalt*（1896）
  5. *Der Wahrheitsgehalt der Religion*（1901）/ *Thomas von Aquino und Kant*（1901）
  6. *Grundlinien einer neuen Lebensanschauung*（1907）
  7. *Der Sinn und Wert des Lebens*（1908）——诺奖当年之作
  8. *Können wir noch Christen sein?*（1911）
  9. *Der Sozialismus und seine Lebensgestaltung*（1920）
- **关键时间线**（15–20 节点）：1846 生于 Aurich → 幼年丧父 → 1863 入哥廷根（Lotze 执教）→ 1866 博士论文 *De Aristotelis dicendi ratione* → 柏林听 Trendelenburg → 1866-71 中学教员（Husum/柏林/法兰克福）→ 1871 巴塞尔教授（胜 Nietzsche）→ 1874 转耶拿 → 1882 与 Irene Passow 成婚 → 1888《Die Einheit des Geisteslebens》→ 1890《大思想家的人生观》成名 → 1896《为一种精神生活内容而斗争》→ 1901《宗教的真理内涵》→ 1907《新人生观基本线条》→ 1908 诺贝尔文学奖 +《人生的意义与价值》→ 1911 英国讲学 → 1912-13 哈佛/NYU → 一战为国家立场发声 → 1920 耶拿退休、《社会主义及其生活塑造》→ 1926-09-15 卒于耶拿

### 第 4 步：研究领域梳理 + 入库（哲学家按领域条目入库）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ethics | 伦理学 | infobox main interests；伦理行动主义的落点 | 核心页 |
| 1 | philosophy of life | 生命哲学/人生哲学 | infobox school；"一切哲学皆是人生哲学" | 核心页 |
| 2 | German idealism | 德国唯心主义 | infobox school，理想主义人生哲学的谱系 | 思想页 |
| 3 | philosophy of religion | 宗教哲学 | 《宗教的真理内涵》《我们还能是基督徒吗》 | 宗教页 |
| 4 | history of philosophy | 哲学史 | 亚里士多德方法/哲学术语史/大思想家系列 | 早年页 |

#### 4.1 入库操作
- `MySQL/data/Rudolf_Christoph_Eucken.yaml` → `python3 MySQL/seed_person.py data/Rudolf_Christoph_Eucken.yaml`
- `primary_occupation='writer'`（文学奖口径）、occupations：writer(0)/philosopher(1)/university teacher(2)；nationality：Germany
- 校验 fields≥4、relations≥2、has_social_data=1

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Lotze | 师→生 | 哥廷根教师，infobox academic advisors |
| advisor-student | Gustav Teichmüller | 师→生 | 哥廷根教师，后任其巴塞尔讲席前任 |
| advisor-student | F. A. Trendelenburg | 师→生 | 柏林教师，伦理倾向与哲学史讲法吸引之 |
| advisor-student | Max Scheler | 本人→学生 | infobox doctoral students，现象学与价值伦理学家 |
| spouse | Irene Passow | 无向 | 1882 成婚 |
| parent-child | Walter Eucken | 本人→对方 | 子，秩序自由主义（ordoliberalism）奠基人 |
| parent-child | Arnold Eucken | 本人→对方 | 子，化学家兼物理学家 |

### 第 5 步：设计配色

- **主色**：赭褐 `#5C3A1E`（哥特讲坛与老书卷）+ 诺奖香槟金 `C9A227`
- badgeA 伦理 — 靛蓝 `#4C5FD5`；badgeB 生命哲学 — 青绿 `#0E7C7B`；badgeC 宗教哲学 — 琥珀 `#E07B30`；badgeD 哲学史 — 玫瑰 `#C4204F`
- **背景母题**：上升阶梯 + 稀疏光柱（精神克服本性的行动主义图式）

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享封面）
01  封面 — 理想主义人生哲学家 / Rudolf Christoph Eucken 1846–1926 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/师承/讲席/子女/荣誉/核心领域）
03  核心贡献概览 — 伦理行动主义 / 精神生活的统一 / 宗教哲学 / 大思想家系列
04  早年与哥廷根 (1846–1866) — 丧父/Aurich 语文学/博士论文 De Aristotelis dicendi ratione
05  三位老师 — Lotze / Teichmüller / Trendelenburg（师承结构页）
06  巴塞尔讲席：击败尼采 (1871–1874) — 接任 Teichmüller/竞争轶事（仅按 page 一句）
07  耶拿四十六年 (1874–1920) — 讲台哲人/精神生活三部曲
08  大思想家的人生观 (1890) — 成名作（书影/概念图式页）
09  伦理行动主义 — 人处自然与精神之交/灵魂/持续努力（概念框替代公式框）
10  1908 诺贝尔奖 — 官方理由 EN+中译/哲学家得文学奖的独特性
11  宗教哲学双作 — Der Wahrheitsgehalt der Religion (1901) / Können wir noch Christen sein? (1911)
12  跨越大西洋 (1911–1913) — 英国讲学/哈佛交换教授/NYU Deem 讲座
13  一战与学人共同体 — 为国家立场发声/国际学者共同体之毁（客观一句，不展开政治评价）
14  遗产：两条支流 — 子 Walter 的秩序自由主义与 Arnold 的科学/理想主义人生哲学的余响 + 结尾
```

### 第 7–8 步：版式要点 + 专属陷阱

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 全句四要素（求真理/思想力/视野/表述的温度与力量 + 理想主义人生哲学）；勿写"因哲学著作获奖"泛化 |
| 生卒双值 | 卒日 frontmatter 09-14/09-15 两说——**以 infobox 与正文 09-15 为准**，页内不并列 |
| 国籍口径 | 出生时为汉诺威王国（1866 才并入普鲁士）；yaml 用 Germany，页面正文写明出生地沿革即可，勿写"生于普鲁士" |
| 击败尼采 | 仅"在巴塞尔教席竞争中击败 Friedrich Nietzsche"一句事实，**勿引申为两人有交恶/交往** |
| 一战立场 | page 原句 "took a strong line in favor of the causes with which his country had associated itself"+学人共同体之毁——客观转述一句，**不展开政治叙事、不作评价** |
| 子女 | Walter=经济学家（ordoliberalism 奠基人）、Arnold=化学家/物理学家，方向勿互换 |
| 引语红线 | 除获奖理由 EN 原句外无其他直接引语；"ethical activism" 是其术语可译述，**勿杜撰中文名言** |
| 同名区分 | Max Scheler 系其博士生（infobox），勿与现象学圈其他关系混写；Trendelenburg 用全名 Friedrich Adolf Trendelenburg |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| ethical activism | 伦理行动主义 | 其自铸术语 Aktivismus，勿译"道德行动" |
| philosophy of life | 生命哲学/人生哲学 | Philosophie des Lebens |
| Geistesleben | 精神生活 | 多作著作标题语素 |
| idealistic philosophy of life | 理想主义人生哲学 | 获奖理由原词 |
| ordoliberalism | 秩序自由主义 | Walter Eucken 的学派，勿混入父亲思想 |
| Deem lecturer | Deem 讲座人 | NYU 讲席名，保留原名 |
| Hermeneutik 与 philology | 古典语文学 | 其博士论文领域 |

---

## 四、BGM 建议

- **选定曲目**: **Daylight** — Alex-Productions（53k views，高受众 / 明亮 / 轻快）
- **匹配理由**: "明亮/轻快" 匹配奥伊肯的理想主义底色——"以温暖而有力的表述捍卫并发展理想主义人生哲学"（官方理由），光明战胜非精神性本性的伦理行动主义；结尾轻收匹配其 1920 年功成身退于耶拿讲台
- **备选**（未采用）: Timeless（沉稳但被其他批次风格占用）；Eternals（思想遗产贴切但受众 49k 偏低）
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Rudolf_Christoph_Eucken/page.md` | 事实基准 |
| `MySQL/data/Rudolf_Christoph_Eucken.yaml` | 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每写一页就 make，看到溢出就修。**
