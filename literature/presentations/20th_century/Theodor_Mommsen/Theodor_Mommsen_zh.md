# 文学家立传提示词（OpenLiterature：Theodor Mommsen）

> **本文件是特奥多尔·蒙森（1902 诺贝尔文学奖）的人物专属立传提示词**，结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容按文学家适配：无公式框，以**代表作书影/名句引文框/意象图式**替代。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各学科侧共享体系）。
- **本实例**：Theodor Mommsen（特奥多尔·蒙森），1902 诺贝尔文学奖得主，**极少数以非虚构（史学）写作获文学奖者**，19 世纪最伟大的古典学家之一。
- **设计哲学**：文学家立传以**作品意象与文学史脉络**替代公式与实验——身份信息页（★ 必做）与「文学领域」结构化表达仍须保留。蒙森的特例性（史学家得文学奖）本身即是全篇叙事主轴，须首尾呼应。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Theodor Mommsen（本名 Christian Matthias Theodor Mommsen，1817-11-30 加尔丁 ~ 1903-11-01 柏林夏洛滕堡，享年 85 岁）
- **气质关键词**：**罗马史的立法者、碑铭学的开创者、议会中的学者** —— 1902 诺贝尔文学奖官方获奖理由：
  > EN: "the greatest living master of the art of historical writing, with special reference to his monumental work, A History of Rome"
  > 中译：表彰其为当今最伟大的历史写作艺术大师，尤以其巨著《罗马史》为代表（引自 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）
- **设计母题**：**碑铭与罗马（epigraphy）**。他开创碑铭学（autopsy 校勘原则），《拉丁铭文集成》（CIL）至今仍在续编——视觉母题用「石刻罗马大写字母 + 大理石纹理 + 铭文拓片」，与《罗马史》的书影并置。
- **本地数据源**：`literature/presentations/pages/20th_century/Theodor_Mommsen/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Theodor_Mommsen （肖像：第 0 步**待下载**，正文插图有 Ludwig Knaus 1881 油画像）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面已抓取到上述路径（本提示词即其事实基准，第一轮已核对）：
  - 生卒：1817-11-30 生于加尔丁（石勒苏益格公国，时属丹麦）~ 1903-11-01 卒于夏洛滕堡（普鲁士王国），享年 85；在 Bad Oldesloe（荷尔斯泰因）长大，父为信义会牧师
  - 教育：Gymnasium Christianeum（阿尔托纳）四年；基尔大学 1838–1843 习法学，获罗马法博士学位（付不起哥廷根学费而入基尔）；基尔室友为诗人 Theodor Storm，与兄弟 Tycho 三人合出诗集《Liederbuch dreier Freunde》
  - 任职：莱比锡（1848 法学教授，1851 因抗议萨克森新宪法被迫辞职）→ 苏黎世（1852 罗马法教授，流亡数年）→ 布雷斯劳（1854，结识 Jakob Bernays）→ 柏林科学院研究教授（1857）/ 柏林大学罗马史教授（1861，讲学至 1887）；柏林科学院史语班秘书（1874–1895），协创并管理罗马德国考古研究院
  - 政治：1848 革命时任战地记者；普鲁士众议院议员（1863–1866、1873–1879）、帝国议会议员（1881–1884），先后属进步党/民族自由党/脱离派；1881 年与社会政策问题上激烈抨击俾斯麦，险遭起诉；1879 起在柏林反犹论战中著小册子驳斥特赖奇克，1890 年参与创建反犹防御协会（Abwehrverein）
  - 关键荣誉：Nobel 文学奖 1902（普鲁士科学院 18 位成员联名提名）；Pour le Mérite 民事类（1868）；荷兰皇家艺术与科学院外籍院士（1859）；罗马荣誉市民；美国文物学会会员（1870）；美国哲学学会会员（1873）
  - 家庭：妻 Marie（莱比锡出版人 Karl Reimer 之女），育有十六子；长女 Maria 嫁古典学家 Ulrich von Wilamowitz-Moellendorff；孙 Theodor Ernst Mommsen 为美国中世纪史教授；曾孙 Hans 与 Wolfgang Mommsen 均为德国史学家
  - 1880-07-07 凌晨柏林自宅书房火灾，抢救文献时烧伤，多部珍贵手稿焚毁（含剑桥三一学院借阅件）
  - 关键时间线（18 节点）：1817 生于加尔丁 → 基尔大学法学（1838–1843，罗马法博士）→ 与 Storm 合出诗集 → 丹麦王室资助赴法意研究罗马铭文 → 1848 革命战地记者 → 1848 莱比锡法学教授 → 1851 辞职抗议 → 1852 苏黎世 → 1854 布雷斯劳 → 1857 柏林科学院 → 1858 入选柏林科学院 → 1861 柏林大学罗马史教授 → 1868 Pour le Mérite → 《罗马史》三卷（1854–1856，Dickson 英译 1862–1866）→ 1867–1870《Digesta》校勘 → 1871–1888《罗马公法》三卷 → 1874–1895 科学院秘书（组织 CIL 等工程）→ 1880 书房火灾 → 1881–1884 帝国议员 → 1885《罗马行省志》（即《罗马史》第 5 卷）→ 1899《罗马刑法》→ 1902 诺贝尔文学奖 → 1903-11-01 逝世

### 第 1–3 步：建目录 / 复制 Makefile / 收图 【模板通用】

- 在 `literature/presentations/20th_century/Theodor_Mommsen/` 建目录与 `images/`；Makefile `MAIN=Theodor_Mommsen_zh`；肖像第 0 步下载。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | roman history | 罗马史 | 《罗马史》三卷 + 《罗马行省志》，获奖核心 | 核心页 |
| 1 | classical philology | 古典语文学 | 19 世纪最伟大古典学家之一 | 定位页 |
| 2 | epigraphy | 碑铭学 | 开创 autopsy 校勘法，主持 CIL 十七卷工程 | 碑铭页 |
| 3 | roman law | 罗马法 | 《罗马公法》《罗马刑法》影响德国民法典 | 法学页 |
| 4 | numismatics | 钱币学 | 得 Borghesi 训练推动的治学门类 | 编辑页 |

#### 4.1 入库操作

- `MySQL/data/Theodor_Mommsen.yaml`（name_en=`Theodor Mommsen`，qid=Q25351，primary_occupation=`writer`），`python3 seed_person.py data/Theodor_Mommsen.yaml`。
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id JOIN people p ON p.id=pf.person_id WHERE p.qid='Q25351' ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marie Mommsen | 无向 | 妻（娘家姓 Reimer），Karl Reimer 之女，育有十六子 |
| colleague | Theodor Storm | 无向 | 基尔大学室友，三人合出诗集，后成著名诗人 |
| colleague | Bartolomeo Borghesi | 无向 | CIL 碑铭计划受其训练与推动 |
| advisor-student | Wilhelm Dilthey | 蒙森→学生 | infobox 知名学生 |
| advisor-student | Francis J. Haverfield | 蒙森→学生 | infobox 知名学生 |
| advisor-student | Eduard Schwartz | 蒙森→学生 | infobox 知名学生 |
| advisor-student | Otto Seeck | 蒙森→学生 | infobox 知名学生 |
| controversy | Heinrich von Treitschke | 无向 | 柏林反犹论战（Berliner Antisemitismusstreit）中的对手，著小册子驳斥其观点 |
| controversy | Otto von Bismarck | 无向 | 1881 社会政策问题上激烈冲突，险遭起诉 |

> **不入库并注明**：Jakob Bernays 仅「结识」无实载关系类型；兄弟 August Mommsen（合著《罗马年代学》）无兄弟关系类型；女婿 Wilamowitz-Moellendorff 经女儿 Maria 关联，无姻亲关系类型；George Bernard Shaw（引其恺撒诠释写《恺撒与克莉奥佩特拉》）、Alfred Thayer Mahan（读《罗马史》成稿）、Heiner Müller（写《Mommsens Block》）属后世接受史，非本人社会关系，均不入库。

#### 4.5.1 入库操作

- yaml `relations` 与上表完全一致；父辈/学生辈 stub 不编造 qid。
- 校验：`SELECT r.type, p2.name_en FROM person_relation r JOIN people p ON p.id=r.from_id JOIN people p2 ON p2.id=r.to_id WHERE p.qid='Q25351' OR p2.qid='Q25351'`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：大理石般的冷峻、学术的厚重、公民的孤直
- **配色**：主色普鲁士蓝 `#1E4E79` + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 罗马史 — 酒红 `#7A1E28`（罗马军团红）
  - `badgeB` 碑铭学 — 石灰灰 `#6B6B5E`
  - `badgeC` 罗马法 — 深金 `#A6791D`
  - `badgeD` 政治/论战 — 铁灰蓝 `#3D5A73`
- **背景母题**：稀疏「铭文石板」矩形残片 + 刻字横线，四档错落（呼应碑铭学）。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像（Knaus 1881 油画像优先）+ 姓名小字注；底部状态栏 `国籍 | 机构 | 主要奖项`。
2. **身份信息页（★ 必做）**：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
4. 无公式框：以**《罗马史》书影/拉丁铭文拓片图式**替代；Mark Twain 柏林晚宴见闻段（1892「全场起立高呼 MOMMSEN!」）可作名场面引文框。

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 罗马史的立法者 / Theodor Mommsen 1817–1903 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 罗马史 / 碑铭学 / 罗马法 / 编辑组织四徽章
04  石勒苏益格少年 (1817–1843) — 牧师家庭、Christianeum、基尔法学博士、与 Storm 合出诗集
05  意大利铭文之旅 — 丹麦王室资助、Borghesi 训练、autopsy 方法
06  1848 革命与教授漂泊 — 战地记者、莱比锡辞职、苏黎世流亡、布雷斯劳
07  柏林岁月 (1857–1887) — 科学院研究教授、柏林大学罗马史讲席
08  《罗马史》核心贡献页 — 三卷结构、Dickson 英译、「未写的第四卷」
09  碑铭与法学工程 — CIL 十七卷、Digesta、罗马公法/刑法、MGH 与教会文献
10  议会中的学者 — 两院议员、反对俾斯麦、反犹论战与 Abwehrverein（客观简述，不作政治评价）
11  1902：史学家的文学奖 — 官方理由 EN+中译引文框、18 人提名、Mark Twain 晚宴名场面
12  家庭与身后 — Marie 与十六子、Wilamowitz 联姻、1903 逝世、Garding「Mommsen 城」
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 make 编译，pdftoppm 截图检查溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Mommsen 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 国籍口径 | 生于石勒苏益格公国（**当时属丹麦王国**），德意志属性按正文「German parents / German nationalism」口径；勿写成「丹麦作家」 |
| 获奖身份 | 以**历史写作**获文学奖，正文明言「极少数非虚构作家获文学奖」之一，这是全篇主轴勿含糊 |
| 政治内容 | 议会活动、与俾斯麦冲突、反犹论战：只按 page.md 客观事实简述，**不作政治评价、不展开政治叙事**；1897 致维也纳报纸信中反捷克言论为正文实载争议，可一笔客观带过或回避，禁展开 |
| 《罗马史》卷数 | 三卷（1854–1856）为其主体；第 4 卷（帝国通史）终生未写；1885《罗马行省志》即第 5 卷；1992 年据学生笔记整理的《Römische Kaisergeschichte》是后人复原，勿写成遗稿亲笔 |
| 学生名单 | Dilthey/Haverfield/Schwartz/Seeck 出自 infobox「Notable students」，注明口径 |
| Jakob Bernays | 仅「met」，勿写成师承或合作 |
| 火灾细节 | 1880-07-07 凌晨、Marchstraße 6、抢救文件时烧伤、焚毁多部手稿——数字勿混 |
| 子女数 | 十六个子女（与 Marie），勿写成「众多」 |
| 产量数字 | 著述超过 1500 种（Zangemeister 1887 目录 900 余种，Jacobs 1905 增至 1500+），两个数字勿混 |
| 同名区分 | 孙辈 Theodor Ernst Mommsen（中世纪史教授）与本人同名区分；曾孙 Hans/Wolfgang Mommsen 为后世史学家，本篇一句带过 |

**术语清单**：

| 英文/原文 | 中文 | 风险 |
|------|------|------|
| Corpus Inscriptionum Latinarum (CIL) | 《拉丁铭文集成》 | 十七卷工程，1986 出最后一卷 |
| autopsy | 目验校勘法 | CIL 基本原则，勿译「尸检」 |
| Römische Geschichte | 《罗马史》 | 获奖代表作 |
| Roman Constitutional Law | 《罗马公法》 | 1871–1888 三卷 |
| Roman Criminal Law | 《罗马刑法》 | 1899 |
| Monumenta Germaniae Historica | 《德意志史料集成》 | 参与出版 |
| Codex Theodosianus | 《狄奥多西法典》 | 1905 遗出校勘本 |
| Pour le Mérite | 功勋勋章（民事类） | 1868 |
| Berliner Antisemitismusstreit | 柏林反犹论战 | 1879 起，客观表述 |
| Gymnasium Christianeum | 克里斯蒂安内姆中学 | 阿尔托纳 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions
- **匹配理由**：
  - 「超越时代」匹配 CIL 至今续编、《罗马史》跨越近两百年仍在阅读的恒久性
  - 沉稳纪录片气质匹配学者型得主：从基尔宿舍到柏林讲席，八十五年学术长跑
  - 「长期纲领」匹配其组织者身份——以一己之力搭建 19 世纪古典学的基础设施
- **本地路径**：对照 `music_audio/curated_tracks.md` 中 alex-productions Timeless 条目复制到本目录。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Theodor_Mommsen/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 官方理由中译（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |
