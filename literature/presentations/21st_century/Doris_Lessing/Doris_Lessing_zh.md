# 文学家立传提示词（Doris Lessing · 2007 诺贝尔文学奖）

> **本文件是 OpenLiterature 21 世纪批次的「人物专属立传提示词」**，目标人物 Doris Lessing（多丽丝·莱辛）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–9 步骨架），内容适配文学家：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 直接复制本文件到新对话中执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Doris May Lessing（多丽丝·莱辛，本姓 Tayler），2007 年诺贝尔文学奖得主，**获奖时最年长的文学奖得主**（87 岁，page.md 明载）。
- **设计哲学**：文学家立传以「作品与意象」代替「定理与公式」——身份信息页（★ 必做）与文学领域结构化表达两点保留，公式框一律换成**名句引文框**。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Doris Lessing（1919-10-22 生于伊朗克尔曼沙阿 ~ 2013-11-17 逝于伦敦，享年 94 岁）
- **气质关键词**：**女性经验的史诗作家、三段式创作的马拉松者、苏菲主义的漫游者** —— 2007 年获奖理由（官方 EN 原文，禁止改写）：
  > "that epicist of the female experience, who with scepticism, fire and visionary power has subjected a divided civilisation to scrutiny"（表彰这位女性经验的史诗作家，以怀疑、火焰与远见之力使分裂的文明接受审视）
- **设计母题**：**三张地图（波斯—罗得西亚—伦敦）与金色笔记本**。以主色深蓝承载其横跨三大洲的迁徙人生；「金色笔记本」的四色分格（黑色/红色/黄色/蓝色笔记）作为 badge 母题；太空 fiction 阶段以星点纹理点缀。
- **本地 Wikipedia**：`literature/presentations/pages/21st_century/Doris_Lessing/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **参考模板**：
  - 提示词母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`literature/presentations/cover/`（统一 `\input`）
  - yaml 母本：`MySQL/data/Kenneth_G_Wilson.yaml`

---

## 三、任务流程 【逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Doris_Lessing` 四件套到 `literature/presentations/pages/21st_century/Doris_Lessing/`（事实基准如下）：
  - 生卒（1919-10-22 生于伊朗克尔曼沙阿，英裔家庭 ~ 2013-11-17 逝于伦敦西汉普斯特德家中，享年 94；死因肾衰竭、脓毒症与肺部感染）
  - 国籍：英国（早期作品被归为罗得西亚背景；2007 年时为英国籍）
  - 家庭：父 Alfred Tayler（一战失一腿的军官，战后任帝国银行波斯分行职员）、母 Emily Maude McVeagh（护士）；1925 全家迁南罗得西亚经营农场；笔名 Jane Somers
  - 教育：多米尼加修道会女校（索尔兹伯里）一年 + Girls High School 一年，13 岁辍学自修；15 岁离家做保姆
  - 婚姻：1939 嫁公务员 Frank Charles Wisdom（1943 离婚，子女 John/Jean 留给父亲）；1943 嫁 Gottfried Lessing（1949 离婚，子 Peter 随她赴英）
  - 政治：参加左翼读书会；1956 因反对种族隔离被南非与罗得西亚禁止入境；同年匈牙利事件后退出英共；1940 年代起被军情五处/六处监视约二十年（2015 解密）
  - 精神转向：1960 年代中期由「好友兼老师」Idries Shah 引入苏菲主义
  - 核心作品：《野草在歌唱》(1950)、《暴力的孩子们》五部曲 (1952–1969)、《金色笔记》(1962)、《坠入地狱简报》(1971)、《幸存者回忆录》(1974)、《好恐怖分子》(1985)、《五》/《Canopus in Argos》太空五部曲 (1979–1983)
  - 关键荣誉：Somerset Maugham 1954、Prix Médicis étranger 1976、奥地利国家欧洲文学奖 1981、WH Smith 1986、Grinzane Cavour 1989、James Tait Black 1995、David Cohen 2001、阿斯图里亚斯亲王奖 2001、**2007 诺贝尔文学奖**、Mapungubwe 金质勋章 2008；荣誉 Companion of Honour 1999；拒 DBE 1992 与 OBE 1977
  - 生涯数字：逾 50 部长篇；2008《泰晤士报》「1945 年以来 50 位最伟大英国作家」第五位；获奖消息传来时正从杂货店回家
  - 关键时间线（15–20 节点）：1919 生于波斯 → 1925 迁南罗得西亚 → 1937 移居索尔兹伯里做电话接线员 → 1939 首婚 → 1943 离婚、加入左翼读书会 → 1943 再婚 Gottfried Lessing → 1949 携 Peter 赴伦敦 → 1950《野草在歌唱》→ 1954 Somerset Maugham → 1956 被禁入境 + 退党 → 1962《金色笔记》→ 1979–1983 Canopus 五部曲 → 1983–84 Jane Somers 笔名实验 → 1999 Companion of Honour → 2007-10-11 诺奖 → 2013-11-17 逝世

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Doris_Lessing/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已立传目录的 `Makefile`，设置 `MAIN=Doris_Lessing_zh`、`VIDEO_NAME=Doris_Lessing_zh`

### 第 3 步：收集图片 【人物专属】

- 从 `images.txt` 取 infobox 肖像（`DorisLessing1984.jpg` 等，250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 时用 Commons `Special:FilePath/<文件名>?width=600`；再失败用装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | feminist classic | 女性主义经典 | 《金色笔记》（作者本人保留态度） | 核心页 |
| 1 | social fiction | 社会小说 | 罗得西亚种族议题、《好恐怖分子》 | 社会页 |
| 2 | space fiction | 太空小说 | Canopus in Argos 五部曲、苏菲观念 | 科幻页 |
| 3 | short story | 短篇小说 | 非洲故事集、《到十九号房》 | 短篇页 |
| 4 | autobiography | 自传 | 《皮下》《阴影中行走》 | 回忆页 |

#### 4.1 入库操作（`MySQL/seed_person.py data/Doris_Lessing.yaml`）

- 新建/更新 `people` 主记录（`name_en='Doris Lessing'`，`qid='Q40874'`），设置 `primary_occupation='writer'`、`has_biography: false`、`has_social_data=1`
- 关联职业 `writer`（rank 0）+ `novelist`/`poet`；国籍 `United Kingdom`
- 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Frank Charles Wisdom | 无向 | 首任丈夫（公务员），1939 结婚，1943 离婚 |
| spouse | Gottfried Lessing | 无向 | 次任丈夫，左翼读书会结识，1943 结婚，1949 离婚 |
| parent-child | John Wisdom | 无向 | 长子（1940–1992），首婚所生 |
| parent-child | Jean Wisdom | 无向 | 女儿（1941 年生），首婚所生 |
| parent-child | Peter Lessing | 无向 | 幼子（1946–2013），次婚所生，随母赴英 |
| influence | Idries Shah | 无向 | "good friend and teacher"，1960 年代中期引其入苏菲主义 |
| colleague | Joan Rodker | 无向 | 挚友，《金色笔记》Molly 部分原型 |
| colleague | Philip Glass | 无向 | 两部歌剧合作：Lessing 脚本、Glass 作曲（1986/1997） |

#### 4.5.1 入库操作

- 以 `name_en='Doris Lessing'` 为中心写入 `person_relation`；对手方均无库内记录则建 stub（`has_biography=0`，不编造 qid），note 加 `[材料待展开] ` 前缀

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：怀疑之火、殖民地的旱风、金色的洞见
- **配色**：主色深靛蓝 `#283593`（预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 女性主义经典 — 笔记金 `#B8860B`
  - `badgeB` 社会小说 — 非洲赭红 `#A34700`
  - `badgeC` 太空小说 — 深空紫 `#4A2A6A`
  - `badgeD` 短篇/自传 — 伦敦雾灰 `#5E6B73`
- **背景母题**：四色笔记本分格——柔和色块如四本笔记并排，边缘如手撕纸；远景稀疏星点呼应 Canopus 序列

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（右上角 + `draw=coveraccent!50` 细边框）与国籍行（`英国 | 伦敦 | 诺贝尔文学奖 2007`）。
2. **身份信息页 ★ 必做**：左肖像 + 右信息网格（生卒、国籍、教育、婚姻、核心作品、主要荣誉）。
3. 引号用半角 `" "`；结尾页品牌统一 `OpenMathAI`。
4. 引文框内容只用 page.md 载英文原文（瑞典学院授奖评语、1982 NYT 访谈对女权标签的回应段、获奖当日 "Oh Christ" 轶事叙述），禁止杜撰「中文原话」。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 女性经验的史诗作家 / Doris Lessing 1919–2013 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）
03  核心作品概览 — 野草在歌唱 / 金色笔记 / Canopus 五部曲 / 好恐怖分子
04  波斯与罗得西亚 (1919–1949) — 克尔曼沙阿、千英亩农场、13 岁辍学自修
05  左翼岁月与出走 (1943–1956) — 两段婚姻、左翼读书会、禁入境与退党
06  伦敦与《野草在歌唱》(1950) — 处女作的殖民地书写
07  《金色笔记》核心页（引文框 + 四色笔记意象图式）
08  苏菲转向 (1960s–) — Idries Shah、内空间小说、Briefing/Memoirs
09  Canopus in Argos：太空小说实验 (1979–1983) — 评论界毁誉参半、Worldcon 1987
10  Jane Somers 笔名实验 (1983–1984) — 新人投稿被拒的文学社会实验
11  2007 诺贝尔文学奖 — 官方理由 EN 原文 + 中译、最年长文学奖得主、杂货店轶事
12  荣誉与拒受 — 拒 OBE/DBE、Companion of Honour 1999、Mapungubwe 2008
13  档案与研究 — Doris Lessing Society、德州大学 Ransom Center、Tulsa
14  遗产：怀疑、火焰与远见 — 50 余部作品、2008 泰晤士报第五位
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；文学领域页用表格 + 意象色块替代公式框

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Lessing 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "that epicist of the female experience…" 禁止改写；中译用名录版「以怀疑、火焰与远见之力使分裂的文明接受审视」 |
| 年龄口径 | 获奖时 88 岁 52 天（page.md 正文 88 岁 52 天 / 导语 87 岁——**以正文 88 岁 52 天为准**，"oldest winner of the literature prize at the time of the award"） |
| 最年长 | 是当时文学奖得主中最年长者、史上第三年长诺奖得主（次于 Hurwicz 与 Raymond Davis Jr.），措辞勿过强 |
| 《金色笔记》 | 学者视为女性主义经典，但**作者本人明确保留**（NYT 1982 访谈），勿写成她自认的女性主义旗手 |
| 三阶段分期 | 共产主义期 1944–1956 → 心理期 1956–1969 → 苏菲期；勿混入其他划分 |
| 笔名实验 | Jane Somers 两部小说 1983/1984 出版，1984 合并再版署名恢复；年份勿写反 |
| 拒受勋章 | 拒 DBE 1992（理由"与不存在的帝国挂钩"）、拒 OBE 1977；接受 CH 1999——三者勿混 |
| 监视档案 | MI5/MI6 监视约二十年，2015-08-21 解密——只客观陈述 |
| 子女 | 首婚子女 John/Jean 留给父亲，次婚子 Peter 随母赴英；姓氏按各自父亲推断（John/Jean Wisdom、Peter Lessing），页内只写名 |
| 感情线 | John Whitehorn 恋情与九十封信无对应关系类型，不入库 |
| C.S. Lewis | 仅 page.md 转述其对 space fiction 称谓偏好，非关系，不入库 |
| 引语红线 | 只用 page.md 英文原文；"Oh Christ" 是叙述转述，可作叙事细节但非引语框 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Golden Notebook | 《金色笔记》 | 1962 年，四色笔记结构 |
| epicist | 史诗作家 | 授奖评语用词，勿译「史诗诗人」 |
| Canopus in Argos | 《天狼星试验》系列 | 五部曲统称，1979–1983 |
| space fiction | 太空小说 | 作者自称，区别于 science fiction 的译法 |
| Sufism | 苏菲主义 | 1960s 中期经 Idries Shah 引入 |
| Left Book Club | 左翼读书会 | 与第二任丈夫结识之处 |
| Jane Somers | 简·萨默斯 | 笔名实验，勿与真名混淆 |
| Children of Violence | 《暴力的孩子们》 | 五部曲 1952–1969 |
| Companion of Honour | 荣誉勋位成员 | 1999 年受，非 DBE |
| Southern Rhodesia | 南罗得西亚 | 今津巴布韦，早期作品背景 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（66k views，高受众）
- **风格标签**: 高受众 / 探索 / 史诗
- **匹配理由**:
  - 「史诗」直接呼应授奖评语的 "epicist"——她的一生与作品就是一部横跨波斯、非洲、伦敦与外太空的史诗
  - 「探索」匹配其三段式创作马拉松——从殖民地社会写实到心理内空间再到苏菲宇宙论，每十年换一次大陆的写作远征
  - 「高受众」匹配其广度——50 余部长篇、小说/短篇/戏剧/歌剧脚本/自传全谱系，是 20 世纪最全面的写作者之一
- **备选**（未采用）: ★★ The Flow of Time——时间感契合自传双卷，但已预分配给 Le Clézio 篇（同批避免撞曲）
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → `presentations/21st_century/Doris_Lessing/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Doris_Lessing/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物主记录 + 领域 + 关系入库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实以 page.md 为准，无载禁写；引语只用英文原文。**
