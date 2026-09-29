# 物理学家立传提示词（Michel Mayor）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」。
> 目标人物：Michel Mayor（2019 诺贝尔物理学奖，51 Pegasi b 发现者，第一颗绕类日恒星运行的系外行星）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Michel Gustave Édouard Mayor（米歇尔·古斯塔夫·爱德华·马约尔），2019 年诺贝尔物理学奖（与 Queloz 共享一半），日内瓦大学天文系荣休教授、系外行星探测的仪器大师。
- **设计哲学**：保留「身份信息页 + 结构化研究领域」骨架；Mayor 篇叙事主线是「为看不见的行星造尺子」——CORAVEL → ELODIE → HARPS 三代视向速度仪器步步进逼米每秒。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Michel Gustave Édouard Mayor（1942-01-12 生于瑞士洛桑；在世）
- **气质关键词**：**系外行星开门人、视向速度仪器大师、日内瓦学派宗师**
- **官方获奖理由（2019，与 Queloz 共享一半）**：
  > "for the discovery of an exoplanet orbiting a solar-type star"（因发现绕太阳型恒星运行的系外行星）
  - 另一半授予 Jim Peebles（物理宇宙学理论发现）；本篇重心在 51 Pegasi b 与仪器长线。
- **设计母题**：**新世界（new worlds）**。从 CORAVEL 的 1 km/s 到 HARPS 的 1 m/s，把「古老梦想」变成「天体物理现实」——视觉以恒星光谱线的周期性摆动为核心意象。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Michel_Mayor/page.md`（**已有本地**）
- **待下载**：`{Dir}.html` 与 `images/` 肖像待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Michel_Mayor`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1942-01-12 生于瑞士洛桑；在世（death_date 留白）
- **国籍**：瑞士
- **教育**：洛桑大学物理学 MS 1966 → 日内瓦天文台/日内瓦大学天文学 PhD 1971（论文 *The kinematical properties of stars in the solar vicinity: possible relation with the galactic spiral structure*；博士论文主题为星系旋臂结构）
- **博士导师**：page.md 无载（infobox 无 doctoral_advisor 字段），**禁写**
- **任职机构**：剑桥大学天文研究所研究员 1971 → 日内瓦天文台研究助理 1971–1984 → 日内瓦大学副教授 1984 → 正教授 1988–2007（2007 正式退休，仍以研究员身份活跃于日内瓦天文台）→ 日内瓦天文台台长 1998–2004；荣休教授；学术假：ESO（智利北部）与夏威夷大学天文研究所
- **关键荣誉（年份齐全）**：Marcel Benoist Prize 1998；Prix Jules Janssen 1998；Balzan Prize 2000；Albert Einstein Medal 2004；法国荣誉军团骑士 2004；Shaw Prize 天文学 2005（与美国天体物理学家 Geoffrey Marcy）；Viktor Ambartsumian International Prize 2010；BBVA Foundation Frontiers of Knowledge Award（基础科学）2011（与 former student Didier Queloz）；RAS Gold Medal 2015；Kyoto Prize（基础科学）2015；Wolf Prize 物理学 2017；Nobel 2019（与 Queloz 共享一半）；Tycho Brahe Medal / Officer of the Legion of Honour / Nature's 10 / Clarivate Citation Laureates / 列日大学荣誉博士（frontmatter 有载、正文无年份）
- **荣誉博士（8 所，年份齐全）**：鲁汶 2001、EPFL 2002、北里奥格兰德联邦大学 2006、乌普萨拉 2007、巴黎天文台 2008、布鲁塞尔自由大学 2009、普罗旺斯大学 2011、约瑟夫·傅里叶大学 2014
- **知名学生**：Didier Queloz（infobox Doctoral students + 正文 graduate student / former student 明载）
- **核心贡献清单**：
  1. 1995-07 与博士生 Queloz 用 ELODIE 光谱仪发现 51 Pegasi b——首颗绕主序（类日）恒星运行的系外行星，后归类热木星；引发系外行星搜索热潮（至 2022-03-21 确认第 5000 颗）
  2. CORAVEL：与马赛天文台 André Baranne 研制的光电视向速度分光计（承接 Roger Griffin 1967 可行性工作），可测恒星运动、双星轨道周期乃至自转速度
  3. ELODIE：与 Baranne、Queloz 研制，精度 15 m/s（较 CORAVEL 的 1 km/s 大幅提升），专为判定次恒星级伴星是褐矮星还是巨行星
  4. HARPS：2003 年装于 La Silla ESO 3.6 m 望远镜，精度提至 1 m/s，Mayor 领队用于系外行星搜索
  5. 2007 为发现 Gliese 581c（首颗位于宜居带的系外行星）的 11 位欧洲科学家之一；2009 团队发现绕主序星的最轻系外行星 Gliese 581e
  6. 双星统计特性研究（1991 与 Antoine Duquennoy：部分「双星」实为带次恒星级伴星的单星系统）
- **关键时间线（18 节点）**：1942 生于洛桑 → 1966 洛桑大学 MS → 1971 日内瓦天文台 PhD（星系旋臂结构）→ 1971 剑桥天文研究所 → 1971–84 日内瓦天文台研究助理 → CORAVEL 研制（与 Baranne）→ 1984 副教授 → 1988 正教授 → 1988–91 IAU 第 33 委员会主席 → 1990–92 ESO 科技委员会主席 → 1991 与 Duquennoy 双星研究 → 1998–2004 日内瓦天文台台长 → 1995-07 发现 51 Pegasi b → 2000 Balzan → 2003 HARPS 上线 → 2005 Shaw（与 Marcy）→ 2007 Gliese 581c / 正式退休 → 2015 京都奖 + RAS 金奖 → 2017 Wolf → 2019-10-08 获诺奖 → 2019-12-08 诺奖演讲 *Plurality of Worlds in the Cosmos: A Dream of Antiquity, A Modern Reality of Astrophysics*

### 第 4 步：研究领域表 【人物专属，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | extrasolar planets | 系外行星 | 51 Pegasi b，2019 诺奖核心 | 核心页 |
| 1 | Doppler spectroscopy | 多普勒光谱学 / 视向速度 | CORAVEL-ELODIE-HARPS 主线 | 仪器页 |
| 2 | astronomical instrumentation | 天文仪器 | 三代光谱仪研制者 | 仪器页 |
| 3 | stellar kinematics | 恒星运动学 | 太阳附近恒星运动性质（博士论文起点） | 早年页 |
| 4 | galactic structure | 银河系结构 | 博士论文星系旋臂结构、研究兴趣明载 | 早年页 |

### 第 4.5 步：社会关系表 【人物专属，与 yaml relations 一致；只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Didier Queloz | Mayor → 学生 | 博士生，51 Pegasi b 共同发现人，2019 诺奖共享 |
| co-honored | Didier Queloz | 无向 | 2019 诺贝尔物理学奖共享一半（Peebles 得另一半）；BBVA 2011 亦共享 |
| co-honored | Jim Peebles | 无向 | 2019 诺贝尔物理学奖共享（Peebles 得一半，Mayor/Queloz 共享另一半） |
| co-honored | Geoffrey Marcy | 无向 | 2005 Shaw Prize 天文学共同得主 |
| colleague | André Baranne | 无向 | 马赛天文台合作者，CORAVEL 与 ELODIE 共同研制者 |
| colleague | Antoine Duquennoy | 无向 | 1991 双星/次恒星级伴星统计研究合作者 |
| colleague | Pierre-Yves Frei | 无向 | 合著法语科普书 Les Nouveaux mondes du Cosmos |

### 第 5 步：配色方案 【人物专属】

- **气质**：精准、耐性、开门见山
- **主色**：深绿 `#146B3A`（日内瓦湖畔与「新世界」的生机）+ 诺奖香槟金 `C9A227`
  - `badgeExo` 系外行星 — 琥珀 `#E07B30`
  - `badgeRV` 视向速度 — 电光青 `#0E7C9B`
  - `badgeInstr` 仪器 — 深紫 `#4A3B8C`
  - `badgeSurvey` 巡天 — 苔绿 `#3E7C4F`
- **背景母题**：柔和气泡 + 一条正弦摆动的谱线（视向速度周期信号）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；无真实肖像则用装饰圆占位。
2. 封面有国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）。
4. 结尾页品牌标注统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 系外行星开门人 / Michel Mayor 1942– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 51 Pegasi b / CORAVEL / ELODIE / HARPS
04  洛桑到日内瓦 (1942–1971) — 星系旋臂结构博士论文、剑桥一年
05  仪器之路 I：CORAVEL — 与 Baranne、Griffin 1967 可行性工作（公式框放视向速度多普勒公式）
06  仪器之路 II：ELODIE — 15 m/s、为褐矮星还是巨行星之问而生
07  1995：51 Pegasi b（核心贡献页）— 首颗绕类日恒星的系外行星、热木星
08  仪器之路 III：HARPS — 1 m/s、La Silla 3.6 m 望远镜
09  宜居带与最轻行星 — Gliese 581c (2007) / Gliese 581e (2009)
10  2019 诺贝尔奖 — 与 Queloz 共享一半、Peebles 得另一半
11  荣誉长廊 — Benoist/Janssen 1998 · Balzan 2000 · Einstein Medal 2004 · Shaw 2005 · Kyoto 2015 · Wolf 2017
12  学会服务 — IAU 委员会主席、ESO 代表、八所荣誉博士
13  「太远了」——对新世界的清醒（引语页，仅用白名单引语）
14  遗产：5000 颗系外行星的世界
15  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖份额 | Mayor 与 Queloz **共享一半**，Peebles 得另一半（工作互不相关）；勿写成三人平分 |
| 获奖理由 | 官方措辞 "for the discovery of an exoplanet orbiting a solar-type star"；强调**太阳型恒星**，勿泛化为「发现第一颗系外行星」（绕脉冲星的行星更早，page.md 亦明言 51 Peg b 是首颗绕 main-sequence/sun-like star 的行星） |
| 「第一」口径 | 正确说法：first exoplanet orbiting a sun-like / main-sequence star；禁写成「人类发现的第一颗系外行星」 |
| 博士导师 | page.md 无载，**禁写**；论文主题是星系旋臂结构，勿写成系外行星研究 |
| Queloz 关系 | 博士生（infobox + 正文两处）+ 共同获奖 + BBVA 2011 共享——师生与 co-honored 两行并列，勿合并 |
| Griffin 定位 | Roger Griffin 是 1967 光电视向速度可行性先驱（"Following preliminary work"），Mayor 是承接者，**勿写成师生或联合研制 CORAVEL** |
| CORAVEL/ELODIE 精度 | CORAVEL 1 km/s → ELODIE 15 m/s → HARPS 1 m/s，三个数字与三台仪器勿错配 |
| Gliese 581c | Mayor 是「11 位欧洲科学家之一」；勿写成他个人发现 |
| 引语白名单 | 仅 page.md 英文原句可用："much, much too far away … [and would take] hundreds of millions of days using the means we have available today"；**其余禁杜撰**（含「人类永不移民」的表述须贴合原句） |
| 书名 | Les Nouveaux mondes du Cosmos（与 Pierre-Yves Frei 合著，Seuil，260 页，获 Livre de l'astronomie 2001）——法语书名斜体勿转译成另造中文书名 |
| 小行星 | 125076 Michelmayor（Michel Ory 2001 发现，2013-08-21 正式命名）；勿与 Peebles 的小行星 18242 混淆 |
| 退休口径 | 2007 正式退休但仍在日内瓦天文台任研究员；「荣休教授」为现衔，勿写成已完全离岗 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| exoplanet / extrasolar planet | 系外行星 | 「太阳型恒星」限定语勿丢 |
| 51 Pegasi b | 飞马座 51b | 首颗绕类日主序星的行星；热木星 |
| hot Jupiter | 热木星 | 51 Peg b 的归类 |
| radial velocity | 视向速度 | 多普勒法的观测量 |
| Doppler spectroscopy | 多普勒光谱学 | 视向速度法学名 |
| CORAVEL / ELODIE / HARPS | 三代仪器名 | 专名大写勿译；精度 1 km/s / 15 m/s / 1 m/s |
| brown dwarf | 褐矮星 | ELODIE 立项的科学问题 |
| main-sequence star | 主序星 | 「第一」口径关键词 |
| habitable zone | 宜居带 | Gliese 581c 属性 |
| globular cluster dynamics | 球状星团动力学 | 研究兴趣列表项 |
| double stars / binary stars | 双星 | 统计特性研究 |
| Saas-Fee Advanced Courses | 萨斯费高阶课程 | 九届出版与组织者 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（高受众/史诗/开阔）
- **匹配理由**：「新陆地」直译其一生主题——为宇宙打开一片新大陆（5000 颗系外行星的世界）；开阔史诗感匹配「古老梦想成为现代现实」的诺奖演讲标题。
- **备选**（未采用）：Expedition（远征感贴切但已被多篇使用）；SEA（平稳流动，弱于「发现新世界」的开阔感）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Michel_Mayor/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Michel_Mayor.yaml` | 社会关系/领域入库数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
