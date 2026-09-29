# 文学家立传提示词（Herta Müller · 2009 诺贝尔文学奖）

> **本文件是 OpenLiterature 21 世纪批次的「人物专属立传提示词」**，目标人物 Herta Müller（赫塔·米勒）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–9 步骨架），内容适配文学家：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Herta Müller（赫塔·米勒），2009 年诺贝尔文学奖得主，罗马尼亚德裔作家——「以诗的凝练与散文的坦率」书写被剥夺者风景的语言猎人。
- **设计哲学**：文学家立传以「作品与意象」代替「定理与公式」——身份信息页（★ 必做）与文学领域结构化表达两点保留，公式框一律换成**名句引文框**。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Herta Müller（1953-08-17 生于罗马尼亚蒂米什县尼采希多夫，在世）
- **气质关键词**：**语言的猎人、被剥夺者的绘图员、剪报拼贴的诗人** —— 2009 年获奖理由（官方 EN 原文，禁止改写）：
  > "who, with the concentration of poetry and the frankness of prose, depicts the landscape of the dispossessed"（表彰其以诗的凝练与散文的坦率，描绘了被剥夺者的风景）
- **设计母题**：**剪报拼贴与德语字母的流亡**。主色深褐承载巴纳特土地与流放列车；前景散落的纸片字母（呼应其剪刀拼贴的工作方式——诺奖博物馆至今悬挂她的指甲刀），远景一列雪中火车剪影呼应《饥饿天使》。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/Herta_Müller/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **参考模板**：
  - 提示词母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`）
  - yaml 母本：`MySQL/data/Kenneth_G_Wilson.yaml`

---

## 三、任务流程 【逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Herta_M%C3%BCller` 四件套到 `literature/presentations/pages/21st_century/Herta_Müller/`（事实基准如下）：
  - 生卒（1953-08-17 生于尼采希多夫，Banat Swabian 天主教农家；在世）；国籍：**德国 + 罗马尼亚**（1987 移居西柏林）
  - 家庭：祖父为富农兼商人、财产被共产主义政权没收；父亲二战期间为武装党卫军成员、战后以卡车司机为生；母亲 Katarina Gion（1928 年生）17 岁时（1945）被流放苏联强制劳动营、1950 获释——德国少数民族约 10 万人遭流放之一
  - 语言与教育：母语德语、中学才学罗马尼亚语；Nikolaus Lenau 高中 → 蒂米什瓦拉西部大学日耳曼文学 + 罗马尼亚文学
  - 早年工作：1976 工程厂翻译，1979 因拒绝与国家安全局（Securitate）合作被辞退，此后以幼儿园教学与私人德语课谋生
  - 团体：Aktionsgruppe Banat 成员（罗德语裔作家团体，争取言论自由对抗审查）；1985 移民西德被拒、1987 与时任丈夫、小说家 Richard Wagner 获准离开，定居西柏林（二人至今仍居柏林）
  - 学术/团体事件：1995 入选德国语言与文学学院；1997 退出德国 PEN（抗议其与原东德分会合并）；2008-07 致罗马尼亚文化学院院长 Patapievici 公开信（抗议院方资助前线人参加罗德夏季学校）；Securitate 军官 Radu Tinu 否认曾迫害她（与 2009-07《时代周报》她本人的叙述相左）
  - 核心作品：《低地》(Niederungen, 1982 罗审查版 / 1984 德国完整版)、《压制的探戈》(1984)、《人是世界上一只巨大的野鸡》(The Passport, 1986)、《独腿旅行》(1989)、《心兽》(The Land of Green Plums, 1994)、《今天我宁愿没遇见自己》(The Appointment, 1997)、《饥饿天使》(Atemschaukel, 2009)；拼贴诗《发髻里住着一位女士》(2000)、《苍白先生们的摩卡杯》(2005)、《父亲给苍蝇打电话》(2012)；访谈录《我的祖国是一粒苹果核》(2014)
  - 关键荣誉：Aspekte 1984、Rauris 1985、Kleist 1994、Aristeion 1995、**都柏林国际文学奖 1998（绿李子之地）**、Carl Zuckmayer 奖章 2002、Joseph-Breitbach 2003（与 Meckel/Weinrich 同获）、**2009 诺贝尔文学奖**、**Franz Werfel 人权奖 2009（《饥饿天使》）**、Pour le Mérite 2021、柏林犹太博物馆「理解与宽容奖」2022；获译入超过二十种语言
  - 关键时间线（15–20 节点）：1953 生于尼采希多夫 → 1945 母亲被流放（先于她出生）→ 1976–79 工厂翻译被辞 → 1981 Adam Müller-Guttenbrunn 奖 → 1982《低地》审查版 → 1984 德国完整版 + Aspekte 奖 → 1985 移民被拒 → 1987 移居西柏林 → 1986《护照》→ 1989 德语奖（七人同获）→ 1994《心兽》+ Kleist 奖 → 1997 退出 PEN → 1998 都柏林奖 → 2009《饥饿天使》+ Werfel 奖 → 2009-10-08 诺奖 → 2009-12-07 诺奖演说 Jedes Wort weiß etwas vom Teufelskreis → 2020 假死讯辟谣 → 2021 Pour le Mérite

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Herta_Müller/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已立传目录的 `Makefile`，设置 `MAIN=Herta_Müller_zh`、`VIDEO_NAME=Herta_Müller_zh`

### 第 3 步：收集图片 【人物专属】

- 从 `images.txt` 取 infobox 肖像（2009 年签名照 `Herta_Müller.jpg` 等，250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 时用 Commons `Special:FilePath/<文件名>?width=600`；再失败用装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | dictatorship literature | 极权书写 | 齐奥塞斯库时期罗马尼亚经验 | 核心页 |
| 1 | minority language literature | 少数民族语言文学 | 巴纳特施瓦本德语书写、双重语言观 | 语言页 |
| 2 | collage poetry | 拼贴诗 | 剪报字母拼贴、指甲刀工作台 | 诗歌页 |
| 3 | gulag literature | 古拉格书写 | 《饥饿天使》，1945 德裔流放记忆 | 天使页 |
| 4 | autobiographical prose | 自传性散文 | 《低地》《饥饿与丝绸》 | 散文页 |

#### 4.1 入库操作（`MySQL/seed_person.py data/Herta_Müller.yaml`）

- 新建/更新 `people` 主记录（`name_en='Herta Müller'`，`qid='Q38049'`），设置 `primary_occupation='writer'`、`has_biography: false`、`has_social_data=1`
- 关联职业 `writer`（rank 0）+ `poet`/`translator`；国籍 `Germany`（rank 0）+ `Romania`（rank 1）
- 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Richard Wagner (novelist) | 无向 | 前夫，巴纳特德语作家；同出蒂米什瓦拉大学与 Aktionsgruppe Banat，1987 同移西柏林 |
| colleague | Oskar Pastior | 无向 | 《饥饿天使》取材于诗人 Pastior 的古拉格流放记忆（米勒为其记录笔记） |
| influence | Franz Kafka | 无向 | 瑞典学院将其德语少数语言运用与卡夫卡类比并指出其影响 |
| influence | Maria Tănase | 无向 | 罗马尼亚民歌对其语言感受力的影响（Influences 节自述初听震动） |
| colleague | Liu Xia | 无向 | 为其诗集首版作序（2015）、2014 年翻译并诵读其诗作 |

#### 4.5.1 入库操作

- 以 `name_en='Herta Müller'` 为中心写入 `person_relation`；Franz Kafka 库内已有记录（id=5139，勿另建）；其余建 stub（`has_biography=0`，不编造 qid），note 加 `[材料待展开] ` 前缀；**Richard Wagner 必须用消歧义名 `Richard Wagner (novelist)`**（库内 id=5050 裸名 Richard Wagner 为音乐家侧记录，严禁混用）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：被剥夺者的风景、双语的裂隙、剪贴的锋利
- **配色**：主色深褐 `#5C3A1E`（预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 极权书写 — 监听灰紫 `#52307C`
  - `badgeB` 少数民族语言文学 — 巴纳特麦金 `#B07A2A`
  - `badgeC` 拼贴诗 — 剪纸红 `#A31621`
  - `badgeD` 古拉格书写 — 雪夜蓝 `#2A3468`
- **背景母题**：飘落的报纸碎屑——大小错落的浅灰纸片从右上向左下飘散，个别纸片上有一两个「字母」色点；底部一线铁轨消失于雾中

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（右上角 + `draw=coveraccent!50` 细边框）与国籍行（`德国 / 罗马尼亚 | 柏林 | 诺贝尔文学奖 2009`）。
2. **身份信息页 ★ 必做**：左肖像 + 右信息网格（生卒、双重国籍、教育、团体、移居、核心作品、主要荣誉）。
3. 引号用半角 `" "`；结尾页品牌统一 `OpenMathAI`。
4. 引文框内容只用 page.md 载原文语句（瑞典学院授奖评语、两种语言看植物对比的自述段——**页内已注她将雪滴花与铃兰混淆，引用时须照录不「改正」**），禁止杜撰「中文原话」。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 语言的猎人 / Herta Müller 1953– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）
03  核心作品概览 — 低地 / 护照 / 心兽 / 饥饿天使
04  尼采希多夫 (1953–1976) — Banat Swabian 农家、母语德语、家族史（只客观陈述）
05  蒂米什瓦拉与翻译被辞 (1976–1987) — 拒绝合作 Securitate、幼儿园与私课
06  《低地》与审查 (1982/1984) — 「弄脏自家窝」的乡邻批评、Aspekte 奖
07  Aktionsgruppe Banat — 言论自由抗争团体、与 Richard Wagner 的同途岁月
08  《护照》核心页 (1986) — TLS 评语的「压抑密码」意象图式
09  西柏林 (1987–) — 移民获批、学院与 PEN 事件（1995/1997/2008）
10  2009 诺贝尔文学奖 — 官方理由 EN 原文 + 中译、卡夫卡类比
11  《饥饿天使》与 Pastior (2009) — 1945 德裔流放、Werfel 人权奖、诺奖演说
12  拼贴诗工作台 — 剪刀与报纸、Scheck 轶事、诺奖博物馆的指甲刀
13  荣誉与认可 — Kleist 1994 · 都柏林 1998 · Pour le Mérite 2021
14  遗产：词语知道恶的循环 — 二十余种语言、被剥夺者的文学地图
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；文学领域页用表格 + 意象色块替代公式框

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Müller 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "who, with the concentration of poetry and the frankness of prose…" 禁止改写；中译用名录版「描绘了被剥夺者的风景」 |
| 政治红线 | 齐奥塞斯库时期经历、Securitate 监视只按 page.md **客观简述**，不作政治评价、不展开政治叙事 |
| 迫害争议 | Securitate 军官 Radu Tinu 否认迫害 vs 她本人 2009《时代周报》叙述——两说并列，不得只取一方 |
| 同名区分 | 丈夫 Richard Wagner 是**德国小说家**，入库必须用 `Richard Wagner (novelist)`，与库内音乐家 Richard Wagner 严格区分 |
| 同奖名单 | 1989 德语奖七人同获（Csejka/Frauendorfer/Hensel/Lippet/Söllner/Totok/Wagner）、2003 Breitbach 三人同获——仅名单并列无合作叙事，**均不入库** |
| Mo Yan | 2012 对莫言「歌颂审查」的评论及后续政治评论（含 2023/24 时事表态）——**禁写**，不建关系 |
| Liu Xia | 作序/翻译诗作只客观陈述（2014 翻译诵读、2015 作序、2017 信件照片），note 保持中性 |
| 母亲流放 | 1945 年 17 岁流放、1950 获释；《饥饿天使》灵感 = Pastior 记忆 + 母亲经历，双重来源勿只写其一 |
| 语言引语 | 「两种语言看植物」自述须照录页内并保留「她将雪滴花与铃兰混淆」的注——不得替她纠正 |
| 《低地》双版 | 1982 罗审查版 / 1984 德国完整版，勿混为一次出版 |
| 都柏林奖 | 1998 年获，获奖作品《绿李子之地》(The Land of Green Plums / Herztier 1994)，年份勿错接到《饥饿天使》 |
| 演说标题 | 诺奖演说 Jedes Wort weiß etwas vom Teufelskreis（2009-12-07），德文原题照录 |
| 引语红线 | 无英文原文处禁伪造中文引号原话 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Banat Swabians | 巴纳特施瓦本人 | 德国少数民族，非「士瓦本」泛称 |
| Securitate | 国家安全局 | 罗马尼亚秘密警察，1989 前语境 |
| Aktionsgruppe Banat | 巴纳特行动小组 | 德语作家言论自由团体 |
| Niederungen | 《低地》 | 处女作，1982/1984 双版 |
| Atemschaukel | 《饥饿天使》 | 直译「呼吸摆动」，英译 The Hunger Angel |
| collage poetry | 拼贴诗 | 剪报字母构成 |
| Nicolae Ceaușescu | 齐奥塞斯库 | 只客观简述其时期背景 |
| Deutsche Akademie für Sprache und Dichtung | 德国语言与文学学院 | 1995 入选 |
| Franz Werfel Human Rights Award | 弗兰茨·韦弗尔人权奖 | 2009，《饥饿天使》 |
| vicious circle | 恶性循环 | 诺奖演说标题关键词 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Daylight** — Alex-Productions（53k views，高受众）
- **风格标签**: 高受众 / 明亮 / 轻快
- **匹配理由**:
  - 「明亮」构成与她书写创伤的**刻意反差**——米勒的方法恰是在至暗处守护词语的微光（「词语知道恶的循环」），Daylight 的清亮钢琴呼应这份语言的救赎感
  - 「轻快」匹配其拼贴诗工作台的日常性——剪刀、报纸、指甲刀，恐怖记忆被转化为近乎游戏的语言劳作
  - 「高受众」匹配其国际地位——二十余种语言译介、德国最著名的当代作家之一
- **备选**（未采用）: ★★ Tragedy——「深色/戏剧性」贴合题材，但整片叙事重心在语言与生存而非悲剧宣泄，且已预分配给同批其他篇目（避免撞曲）
- **本地路径**: `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` → `presentations/21st_century/Herta_Müller/Daylight.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Herta_Müller/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物主记录 + 领域 + 关系入库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实以 page.md 为准，无载禁写；政治内容只客观简述；引语只用原文。**
