# 文学家立传提示词（OpenLiterature 实例：Sigrid Undset）

> 本文件是 OpenLiterature 的「文学家立传提示词」人物专属实例，以 Sigrid Undset（1928 诺贝尔文学奖，中世纪北方生活书写者）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；文学家适配：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sigrid Undset（西格丽德·温塞特）。
- **设计哲学**：保留「身份信息页」骨架；以**文学领域表**替代研究领域表、以**引文框/书影/意象图式**替代公式框。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Sigrid Undset（1882-05-20 ~ 1949-06-10，享年 67 岁）
- **气质关键词**：**中世纪史诗的重铸者、皈依者、抵抗的声音** —— 1928 诺贝尔文学奖获奖理由：
  > "principally for her powerful descriptions of Northern life during the Middle Ages"
  > （官方中译，照 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）：主要表彰其对中世纪北方生活的有力描写
  > 注：page.md 正文未载英文 citation 原句，EN 以 Nobel 官方口径为准、中译照 CITATION_ZH，禁止改写
- **设计母题**：**十字架与峡湾**。中世纪挪威的木教堂、雪原、峡湾与黑十字（她墓前的三重黑十字）——三个 badge 圆可做成燃烧的烛光、羊皮卷与峡湾冷色调同心圆，呼应 Kristin Lavransdatter 从婚礼花冠到十字架的一生。
- **本地数据源**：`literature/presentations/pages/20th_century/Sigrid_Undset/page.md`（Wikipedia 全文，事实基准已核对）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Sigrid_Undset
- **肖像**：第 0 步待下载（Commons `Sigrid_Undset_young.jpg` 等多帧可用）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1882-05-20 生于丹麦卡伦堡（Kalundborg，母亲娘家）～ 1949-06-10 逝于挪威利勒哈默尔（肾炎），享年 67 岁；葬于 Mesnali，墓立三重黑十字
- 国籍：挪威（丹麦出生，两岁随家迁挪威/克里斯蒂安尼亚）
- 家庭：父 Ingvald Martin Undset（挪威考古学家，1893 年病逝，时年 40，她 11 岁）；母 Charlotte Gyth；长女，下有两妹；丈夫 Anders Castus Svarstad（挪威画家，1912 年结婚，1927 年离异），三子女；长子 Anders Svarstad（1940-04-27 于 Gausdal Segalstad Bridge 阵亡，27 岁）
- 教育：无大学教育——一年秘书课程，16 岁起在克里斯蒂安尼亚工程公司任秘书 10 年（自言厌恶此工作）
- 文学师承与影响（page.md 明载）：1917 年前后痴迷 Robert Hugh Benson 的著作并翻译多部；1928 年访英格兰拜访 G. K. Chesterton 与 Hilaire Belloc，后翻译二人著作（*The Everlasting Man* 1931）；译冰岛萨迦；论 Brontë 姐妹与 D. H. Lawrence 的长文
- 任职/流亡：挪威作家协会会员 1907、文学委员会主席 1933–1935、协会主席 1935–1940；1940 年因反纳粹（30 年代初起公开批评，著作在德被禁、名字在首批逮捕名单）出逃瑞典→横穿西伯利亚→美国（Brooklyn Heights），1945 年战后回国
- 关键荣誉：Nobel Literature 1928（挪威科学与文学院 Helga Eng 提名）；圣奥拉夫大十字骑士勋章；冰岛猎鹰勋章；平信徒多明我会第三会（TOSD）；2026 年奥斯陆教区启动封圣程序（Servant of God）
- 核心作品与贡献（4–6 条）：
  1. *Marta Oulie*（1907，25 岁出道作，写通奸的写实小说，一鸣惊人）
  2. *Gunnar's Daughter*（1909，首部历史小说，萨迦时代）
  3. *Jenny*（1911）与 *Vaaren*（1914）——写实期双峰
  4. *Kristin Lavransdatter* 三部曲（1920–1922，《花冠》《女主人》《十字架》）——代表作
  5. *The Master of Hestviken* 四部曲（1925–1927，Olav/Audunssøn）
  6. *Saga of Saints*（以圣徒生平写挪威史）与自传 *Eleven Years Old*（1934）
- 关键时间线（15–20 节点）：
  1. 1882-05-20 生于丹麦卡伦堡
  2. 1884 随家迁克里斯蒂安尼亚（今奥斯陆）
  3. 1893 父病逝（她 11 岁）
  4. 16 岁任工程公司秘书（十年）
  5. 16 岁即试写中世纪题材小说；22 岁完成中世纪丹麦长篇被拒
  6. 1907 处女作 *Marta Oulie*；加入挪威作家协会
  7. 1909 *Gunnar's Daughter*；获写作奖学金赴欧陆
  8. 1909-12 抵罗马，居留九月，结识斯堪的纳维亚艺术家圈
  9. 1911 *Jenny*
  10. 1912 与 Svarstad 结婚，伦敦半年后返罗马
  11. 1913 长子 Anders 生于罗马
  12. 1914 *Vaaren*
  13. 1917 前后接触 Benson 著作，信仰危机始
  14. 1919 迁利勒哈默尔，婚姻破裂；八月产三胎；两年内建成 Bjerkebæk
  15. 1920–1922 *Kristin Lavransdatter* 三部曲
  16. 1924-11 42 岁皈依天主教，后入平信徒多明我会——在路德宗挪威引发轰动
  17. 1925–1927 *The Master of Hestviken* 四部曲
  18. 1928 诺贝尔文学奖；五月访 Chesterton 与 Belloc
  19. 1931 译 *The Everlasting Man*；1934 自传 *Eleven Years Old*；1939 *Madame Dorthea*（未完成系列首卷）
  20. 1940-01-25 捐出诺贝尔奖章声援芬兰（冬季战争）；四月流亡（长子阵亡）→ 美国；1945 回国不再出版；1949-06-10 卒于利勒哈默尔

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Sigrid_Undset/` 与 `images/`

### 第 2 步：复制 Makefile

- 设置 `MAIN=Sigrid_Undset_zh`、`VIDEO_NAME=Sigrid_Undset_zh`

### 第 3 步：收集图片

- 肖像：待下载（青年照 `Sigrid_Undset_young.jpg` 或 Bjerkebæk 工作照）
- 备选插图：Bjerkebæk 木屋（今属 Maihaugen 博物馆）

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | historical fiction | 历史小说 | 1907 年起首部作品即历史小说；代表作皆历史题材 | 核心页 |
| 1 | medieval fiction | 中世纪题材 | 萨迦时代与中世纪挪威；研读古诺尔斯语手稿与编年史 | 代表作页 |
| 2 | novel | 长篇小说 | 三部曲+四部曲的鸿篇结构 | 作品页 |
| 3 | realism | 现实主义 | 早期克里斯蒂安尼亚写实小说（Marta Oulie/Jenny） | 早期页 |
| 4 | hagiography | 圣徒传记 | Saga of Saints、Catherine of Siena；frontmatter 明载 | 皈依页 |

#### 4.1 入库操作（yaml 见 `MySQL/data/Sigrid_Undset.yaml`）

- 新建 people 主记录（`name_en='Sigrid Undset'`，qid=Q80889），`primary_occupation='writer'`、`has_social_data=1`
- 关联职业 writer(rank 0)/novelist/translator；国籍 Norway
- 5 个领域写入 `person_field`；校验同标杆第 4 步

### 第 4.5 步：社会关系梳理 + 入库

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Ingvald Martin Undset | 无向 | 父亲，挪威考古学家 |
| spouse | Anders Castus Svarstad | 无向 | 1912 年结婚，1927 年离异；挪威画家 |
| parent-child | Anders Svarstad | 无向 | 长子，1940 年抗战阵亡于 Segalstad Bridge |
| influence | Robert Hugh Benson | 无向 | 1917 年起痴迷其著作并译入挪威语，信仰转折的引路人 |
| colleague | G. K. Chesterton | 无向 | 1928 年拜访；后翻译其著作 |
| colleague | Hilaire Belloc | 无向 | 1928 年同访；后翻译其著作 |
| colleague | Marjorie Kinnan Rawlings | 无向 | 流亡佛罗里达时期挚友 |

#### 4.5.1 入库操作

- 以 `name_en='Sigrid Undset'` 为中心写入 `person_relation`；缺失人物建占位（不编造 qid）
- ⚠️ 同名区分：长子 Anders Svarstad 与丈夫 Anders Castus Svarstad 是两人，parent-child 对象是**儿子**（note 已写明「长子」）；勿建丈夫同名自环
- 次女（智障，战前去世）与幼子 Hans 不具名于正文标题、仅散见——不入库，防噪声

### 第 5 步：设计配色方案

- **气质**：峡湾冷冽、烛光温暖、羊皮卷古意
- **配色**：深苔绿（主色，预分配 `#145C54`）+ 香槟金 `C9A227` + 四分类色
  - `badgeA` historical fiction 历史小说 — 羊皮黄 `#B08D3E`
  - `badgeB` medieval fiction 中世纪题材 — 冷杉绿 `#2F5D46`
  - `badgeC` novel 长篇小说 — 峡湾蓝 `#1F4E6B`
  - `badgeD` hagiography 圣徒传记 — 烛火橙 `#C46A2B`

### 5.1 文学家格式硬要求

1. 封面有头像 + 细边框 + 姓名小字注。
2. 封面明示国籍；底部状态栏 `国籍 | 代表作 | 主要奖项`。
3. 必须有身份信息页（生卒、国籍、出生地、家庭、流亡、皈依、荣誉、核心领域）。
4. 品牌口径 `OpenMathAI`；引号半角。
5. 无公式框——引文框/意象图式可用「三重黑十字」与 Kristin 三卷书名花冠/女主人/十字架的意象递进。

### 第 6 步：规划幻灯片序列

```
00  OpenLiterature 项目首页
01  封面 — 中世纪北方生活的重铸者 / Sigrid Undset 1882–1949 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）
03  核心贡献概览 — 历史小说 / 中世纪挪威 / 皈依书写 / 抵抗之声
04  卡伦堡与克里斯蒂安尼亚 (1882–1907) — 父逝、秘书十年
05  早期现实主义 — Marta Oulie / Gunnar's Daughter / Jenny / Vaaren
06  罗马岁月与婚姻 (1909–1919) — 斯堪的纳维亚艺术家圈、Bjerkebæk
07  Kristin Lavransdatter（代表作书影 + 引文框）— 三部曲结构图
08  皈依与圣徒书写 (1924–1939) — Benson/Chesterton/Belloc、Saga of Saints
09  1928 诺贝尔奖 — Helga Eng 提名、"主要表彰"口径
10  流亡：从西伯利亚铁路到布鲁克林 (1940–1945) — 长子阵亡、捐奖章援芬
11  晚年与遗产 — Bjerkebæk、三重黑十字、封圣程序 2026
12  结尾
```

### 第 7–8 步：编写源码与布局检查 【模板通用】

- 每页定义 `\newcommand{\xxxslide}`；写完即 `make` + `pdftoppm` 目检。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Undset 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生地口径 | 生于**丹麦**卡伦堡、长于挪威——国籍徽章写 Norway，正文首句交代 Danish-born；勿写「丹麦作家」 |
| 获奖理由 | 官方措辞 "principally for her powerful descriptions..."，中文「主要表彰」不可删「主要」二字（其余成就亦被承认） |
| EN citation | page.md 正文未载英文原句，EN 用 Nobel 官方口径并加注，中译照 CITATION_ZH |
| 父亲职业 | 考古学家（archaeologist），勿写「历史学家」 |
| 长子/丈夫同名 | Anders Svarstad（子，1940 阵亡）≠ Anders Castus Svarstad（夫）；同名页必须分立并注身份 |
| 捐奖章时间 | 1940-01-25 捐给**芬兰**（冬季战争），勿写成捐给挪威抗战 |
| 流亡路线 | 挪威→瑞典→西伯利亚大铁路→美国；1945 回国——顺序勿乱 |
| 皈依年份 | 1924-11 受洗入天主教（42 岁）；1917 起只是接触 Benson 著作的信仰酝酿期，勿混 |
| 2026 封圣 | 奥斯陆教区启动 canonization 程序（Servant of God）——客观一句，勿写「已封圣」 |
| 月面山 | Mons Undset 因 IAU 未收录已改称 Lambert γ——勿写「月面山以其命名」作定论 |
| 引语红线 | page.md 无直接引语，全篇禁编「原话」 |
| 翻译家身份 | 译 Benson/Chesterton/Belloc/冰岛萨迦入挪威语——occupations 含 translator 的依据 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| *Kristin Lavransdatter* | 《克丽丝丁·拉夫兰斯达特》 | 三卷：The Wreath/The Wife/The Cross |
| *The Master of Hestviken* | 《赫斯特维肯的主人》 | 四部曲 1925–1927 |
| Bjerkebæk | 比克贝克 | 利勒哈默尔故居，今属 Maihaugen 博物馆 |
| Third Order of Saint Dominic | 平信徒多明我会第三会 | TOSD 头衔来源 |
| Saga of Saints | 《圣徒萨迦》 | 以圣徒生平写挪威全史 |
| Kalundborg | 卡伦堡 | 丹麦出生地 |
| canonization | 封圣程序 | 2026 年启动，进行中 |

---

## 四、背景音乐选择 【预分配】

- **选定曲目**: **Cinematic Experience**
- **风格**: 史诗 / 电影感 / 叙事张力
- **匹配理由**:
  - "史诗/电影感" 匹配 *Kristin Lavransdatter* 的三部曲体量与中世纪北方史诗气质（1995 年 Liv Ullmann 改编电影更添银幕联想）
  - 张力段落匹配流亡叙事——长子阵亡、捐奖章、西伯利亚铁路穿越，是全书最具镜头感的章节
  - 宏大而不失温暖的收束，呼应三重黑十字前的静默与封圣程序的历史回声
- **本地路径**: 曲库对应曲目拷贝至 `literature/presentations/20th_century/Sigrid_Undset/Cinematic Experience.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Sigrid_Undset/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | 官方获奖理由中译 CITATION_ZH（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。最重要的事：事实只写 page.md 明载内容；同名父子防自环。**
