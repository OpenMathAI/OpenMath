# OpenPeace 21 世纪和平奖得主立传提示词（实例：Juan Manuel Santos）

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他学科侧共享体系）。
- **本实例**：Juan Manuel Santos（胡安·曼努埃尔·桑托斯），2016 诺贝尔和平奖得主，哥伦比亚第 33 任总统。
- **设计哲学**：政治家立传以「转折」为母题——从铁腕国防部长到和平谈判者，人物弧线本身即叙事核心。

---

## 二、背景信息 【人物专属】

- **目标人物**：Juan Manuel Santos Calderón（1951-08-10 生于波哥大，在世）
- **气质关键词**：**铁腕转型的和平缔造者、技术官僚出身的总统、媒体世家的改革者**
- **2016 官方获奖理由**（照抄名录，禁止改写）：
  > "for his resolute efforts to bring the country's more than 50-year-long civil war to an end."
  > （表彰他坚定不移地结束该国长达 50 余年的内战）
  > page.md 荣誉节另载诺贝尔奖全文（内战「夺去至少 22 万哥伦比亚人的生命、使近 600 万人流离失所」），可在诺奖页作补充数据。
- **设计母题**：**握手与钢笔（从战场到谈判桌）**。左页军事蓝调、右页橄榄枝暖调的左右分色，呼应国防部长→和平谈判者的身份转折。
- **本地数据源**：`peace/presentations/pages/21th_century/Juan_Manuel_Santos/page.md`
- **结构标杆**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构）
- **yaml 母本**：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属】

- 生卒：1951-08-10 生于哥伦比亚波哥大，在世。全名 Juan Manuel Santos Calderón。
- 家庭：桑托斯家族自 1913 至 2007 是《El Tiempo》（哥伦比亚记录报）大股东。父 Enrique Santos Castillo（该报主编），母 Clemencia Calderón Nieto；兄弟 Enrique、Luis Fernando、Felipe。曾叔祖父 Eduardo Santos Montejo（1938–1942 年任总统，购入《El Tiempo》）；堂兄 Francisco Santos Calderón（2002–2010 副总统）。曾叔祖母辈 María Antonia Santos Plata 是独立运动烈士。
- 婚姻：首婚 Silvia Amaya Londoño（电影导演、主持人，三年后离异无子女）；1987 与工业设计师 María Clemencia Rodríguez Múnera 成婚，育三子女：Martín（1989）、María Antonia（1991）、Esteban（1993）。
- 教育：Colegio San Carlos；1967 入哥伦比亚海军，卡塔赫纳 Admiral Padilla 海军军校 1969 毕业，1967–1971 服役；堪萨斯大学经济学与工商管理学士（1973）；伦敦政经学院经济发展硕士（1975）；哈佛肯尼迪学院公共管理硕士（1981）；1981 富布赖特访问学者（Tufts Fletcher School）；1988 哈佛 Nieman Fellow。
- 任职：全国咖啡种植者联合会驻国际咖啡组织（伦敦）首席执行官；《El Tiempo》副社长；Inter-American Dialogue 成员（1990 起，曾任董事会联席主席）；美洲报业协会言论自由委员会主席。
- 政界履历：外贸部长（1991–1994，Gaviria 总统，首任）、总统指定继承人（1993–1994）、UNCTAD 第八届大会主席（1992）、财政与公共信贷部长（2000–2002，Pastrana 总统）、2005 与人共创 Social Party of National Unity（Party of the U）、国防部长（2006–2009，Uribe 总统）、总统（2010-08-07–2018-08-07，第 33 任）、太平洋联盟轮值主席（2013–2014、2017 起）。
- 关键荣誉：2016 诺贝尔和平奖；英国名誉巴斯爵级大十字勋章（2016）；西班牙伊莎贝拉天主教大项链（2015）；葡萄牙恩里克王子大项链（2012）、自由勋章大项链（2017）；Chatham House Prize；哈佛法学院 2017 Great Negotiator Award；Tipperary 国际和平奖 2017；Kew 国际奖章（生物多样性保护）；2012 Shalom Prize；新植物物种 Espeletia praesidentis 以其和平努力命名。
- 核心事业清单：
  1. 与 FARC 的和平谈判（2012-08-27 宣布探索性谈判，2016 达成最终协议）
  2. 结束哥伦比亚 50 余年内战（Indepaz 统计战争代价 1520 亿美元、22 万人死亡）
  3. 国防部长任内对 FARC 的系列打击（Ingrid Betancourt 营救、Raúl Reyes 之死）
  4. 创党与经济治理（外贸、财政部长任内）
  5. 卸任后哈佛肯尼迪学院 Angelopoulos 全球公共领袖研究员
- 关键时间线（16–20 节点）：
  - 1951-08-10 生于波哥大
  - 1967–1971 哥伦比亚海军服役
  - 1973 堪萨斯大学毕业
  - 1975 LSE 硕士
  - 1981 哈佛肯尼迪学院 MPA；回哥伦比亚任《El Tiempo》副社长
  - 1991–1994 首任外贸部长（Gaviria 总统）
  - 1992 出任 UNCTAD 第八届大会主席
  - 1994 创立 Good Government Foundation（曾提出非军事区与 FARC 和谈方案）
  - 2000–2002 财政部长（Pastrana 总统）
  - 2005 与人共创 Party of the U
  - 2006-07–2009-05 国防部长（Uribe 总统）；2008 Ingrid Betancourt 获救
  - 2008-11-04 公开承认军方存在法外处决并承诺处理（"false positives" 丑闻）
  - 2010-06-20 当选总统（2010-08-07 就职）
  - 2012-08-27 宣布与 FARC 展开探索性和谈
  - 2014-06-15 决选 50.95% 击败 Zuluaga 连任
  - 2016-09 宣布与 FARC 达成全面协议；2016-10-02 公投以微弱差距否决
  - 2016-10-07 获 2016 诺贝尔和平奖
  - 2016-11-24 修订版和平协议签署；2016-11-29/30 国会参众两院批准
  - 2017-03-14 承认 2010 竞选收受 Odebrecht 非法捐款；2017-11 巴拿马文件式天堂文件风波
  - 2018-08-07 卸任（继任者 Uribe 系的 Iván Duque）；赴哈佛肯尼迪学院任研究员

### 第 1 步：建立目录 【模板通用】

- 确认 `peace/presentations/21th_century/Juan_Manuel_Santos/` 目录与 `images/` 子目录。

### 第 2 步：复制 Makefile 【模板通用】

- 复制同世纪已完工篇目的 Makefile，设 `MAIN=Juan_Manuel_Santos_zh`、`VIDEO_NAME` 同名。

### 第 3 步：收集图片 【人物专属】

- page.md 有 Santos 2016 年官方肖像（`Juan_Manuel_Santos_2.jpg`）与 2018 版本，下载 500px 真实肖像。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace negotiation | 和平谈判 | 与 FARC 谈判，2016 诺奖核心 | 和谈页 |
| 1 | conflict resolution | 冲突解决 | 真相与和解式转型安排 | 协议页 |
| 2 | public governance | 公共治理 | 总统任内政策与制度改革 | 总统页 |
| 3 | economic policy | 经济政策 | 外贸/财政部长与经济学家训练 | 早年页 |
| 4 | journalism | 新闻业 | 《El Tiempo》副社长与媒体世家 | 家族页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | María Clemencia Rodríguez Múnera | 无向 | 1987 成婚，工业设计师 |
| spouse | Silvia Amaya Londoño | 无向 | 首婚，后离异 |
| parent-child | Enrique Santos Castillo | 无向 | 父亲，《El Tiempo》主编 |
| parent-child | Clemencia Calderón Nieto | 无向 | 母亲 |
| founder | Social Party of National Unity | 无向 | 2005 与人共创并领导（Party of the U） |
| founder | Good Government Foundation | 无向 | 1994 创立，曾提出与 FARC 和谈方案 |
| colleague | Álvaro Uribe | 无向 | 2006–2009 任其政府国防部长，后成为其最强政治对手 |
| colleague | Tony Blair | 无向 | 1999 合著《La Tercera Vía》 |

- 入库操作：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Juan_Manuel_Santos.yaml`

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深海蓝的克制与橄榄绿的和解；主色 `#0E4D64`（manifest 预分配，勿改）+ 诺奖香槟金 `#C9A227` + 四分类色：
  - `badgePeace` 和谈 — 橄榄绿 `#1B5E20`
  - `badgeGov` 治理 — 深海蓝 `#0E4D64`
  - `badgeEcon` 经济 — 琥珀 `#E07B30`
  - `badgeMedia` 媒体 — 玫瑰 `#C4204F`
- **背景母题**：握手轮廓线 + 橄榄枝，左右分色呼应军政与和平两段人生。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 2016 诺贝尔和平奖 / Juan Manuel Santos 1951– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、家族、教育、军旅、三任部长、总统任期、主要荣誉）
03  事业概览 — 军旅 / 部长 / 总统 / 和谈 / 卸任研究员
04  媒体世家与求学 (1951–1981) — El Tiempo 家族、海军军校、KU/LSE/哈佛三学位
05  部长岁月 (1991–2002) — 首任外贸部长、UNCTAD 主席、财政部长
06  国防部长 (2006–2009) — Uribe 治下对 FARC 打击、Betancourt 营救、false positives 丑闻与承认
07  总统第一任期 (2010–2014) — 就职、2012-08-27 宣布和谈、2014 险胜连任
08  与 FARC 的和平谈判 (2012–2016) — 探索性谈判、真相与和解式安排、战争代价数据
09  公投与协议 (2016) — 10-02 否决、10-07 获诺奖、11-24 修订协议、国会批准
10  2016 诺贝尔和平奖 — 官方理由全文、22 万死亡与 600 万流离失所的背景数据
11  荣誉与认可 — Chatham House Prize、Great Negotiator、巴斯勋章、Espeletia praesidentis
12  卸任之后 (2018– ) — 哈佛肯尼迪学院 Angelopoulos 研究员、遗产与争议并陈
13  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式硬要求：封面右上肖像（draw=coveraccent!50 细边框 + 姓名小字注）+ 底部状态栏「国籍 | 机构 | 主要奖项」三要素；身份信息页左肖像右信息网格；履历页三任部长用三列时间轴；每页写完即编译，vbox 溢出 ≤10pt、hbox ≤50pt。

**Santos 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 2016 独得 | Santos 独享 2016 和平奖，无共享得主，勿造 co-honored |
| 诺奖理由主语 | 官方为 "his"（单数）；名录中译「表彰他坚定不移地……」照抄勿改 |
| 政治红线 | FARC 内战、false positives、Odebrecht/天堂文件、Trump 与委内瑞拉议题一律按 page.md 客观记录两说，不作评价性语句；同婚表态只客观引述 |
| false positives | 是其国防部长任期「污点」，Santos 2008-11-04 公开承认并处理（27 名军官被撤、陆军司令辞职），须与诺贝尔和平事业并陈，勿单侧叙事 |
| 乌里韦关系 | 一句话双面事实：由 Uribe 提携（protégé）当选，数月后 Uribe 成最强对手——勿写成单纯师徒或单纯政敌 |
| 公投与诺奖时序 | 2016-10-02 公投否决在前、10-07 诺奖在后、修订协议绕开公投经国会批准——因果链按时间客观呈现 |
| 争议并陈 | 2017 Odebrecht 承认与天堂文件两事必写，勿因诺奖光环隐去 |
| 卸任支持率 | 「以史上最低支持率之一卸任」是 page.md 明载事实，客观写 |
| 家族 | 兄弟三人仅具名不入库；曾叔祖父 Eduardo Santos Montejo 与堂兄 Francisco Santos 可叙述不建关系 |
| 引语红线 | 引语框仅收 page.md 载英文原文语句（如 2014 连任夜 "This is the end of 50 years of conflict"） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| FARC | 哥伦比亚革命武装力量 | 全称 Revolutionary Armed Forces of Colombia |
| Party of the U | 民族团结社会党 | 全称 Social Party of National Unity |
| false positives | 「假阳性」丑闻 | 法外处决事件的专名，须加引号 |
| referendum | 和平协议公投 | 2016-10-02 |
| truth and reconciliation | 真相与和解 | 转型正义机制 |
| El Tiempo | 《时代报》 | 哥伦比亚记录报 |
| Nieman Fellowship | 尼曼学者 | 哈佛新闻奖学金 |
| UNCTAD | 联合国贸发会议 | 第八届大会主席 |
| Pacific Alliance | 太平洋联盟 | 拉美区域组织 |
| Angelopoulos Fellowship | Angelopoulos 全球公共领袖研究员 | 哈佛肯尼迪学院 |
| Admiral Padilla Naval Cadet School | 阿米拉尔·帕迪利亚海军军校 | 卡塔赫纳，1969 毕业 |

### 第 9 步：史实审查 + 术语审查 【人物专属】

- 核对官方理由与名录逐字一致；核对国防部长任期两写法（infobox 07-18 / 正文 19 July 2006，取 2006-07）；确认无任何评价性政治语句。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配，勿改）
- **风格**：远征 / 开拓 / 大气叙事
- **匹配理由**：从军旅到谈判桌的远征弧线——半个世纪的战争在他任内画上句点，「远征」曲目匹配其跨越铁与橄榄枝的征程叙事。
- **本地路径**：`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Juan_Manuel_Santos/page.md` | 本地 Wikipedia 事实基准 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译照抄 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **执行顺序**：提示词 → yaml → seed_person.py 入库 → 验证（has_social_data=1、fields≥4、relations≥2）。
