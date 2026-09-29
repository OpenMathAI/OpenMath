# 和平奖得主立传提示词（OpenPeace 模板实例：Paul Henri d'Estournelles de Constant）

> **本文件是 OpenPeace 的「人物专属立传提示词」**，以 Kenneth_G_Wilson_zh.md（0–11 节结构母本）为结构标杆，
> 以 Frederick_Sanger.yaml 为 yaml 字段母本，为 Paul Henri d'Estournelles de Constant（1909 诺贝尔和平奖得主，法国外交官/参议员）定制。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 d'Estournelles de Constant 专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 体系，与 OpenPhysicist / OpenChemist / OpenMedic 平级）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的任务流程骨架 + 诺贝尔奖立传通用版式。
- **本实例**：Paul Henri Benjamin Balluet d'Estournelles de Constant, Baron de Constant de Rebecque（保罗·亨利·德埃斯特尔内勒·德·康斯坦，1909 诺贝尔和平奖得主之一，法国）。
- **设计哲学**：和平奖得主立传强调「事业与机构」的结构化表达——他是「外交官 → 议员 → 国际仲裁旗手 → 欧洲联合设想者」的多幕人生，且与共享得主的 Beernaert 同以海牙体系为事业核心，须以身份信息页与事业领域表呈现其「反殖民扩张 + 倡仲裁调停」的双重轮廓。

---

## 二、背景信息 【人物专属】

- **目标人物**：Paul Henri Benjamin Balluet d'Estournelles de Constant（1852-11-22 ~ 1924-05-15，享年 71 岁）
- **姓名**：英文 Paul Henri d'Estournelles de Constant（全名 Paul Henri Benjamin Balluet d'Estournelles de Constant de Rebecque；姓名变体极多，本篇统一用 BnF 规范形式）；中文 保罗·亨利·德埃斯特尔内勒·德·康斯坦
- **国籍**：法国（France）
- **诺奖年份**：1909（与比利时的 Auguste Beernaert 共享；1909-12-10 领奖）
- **官方获奖理由英文原文**（照抄 nobel_peace_citations.json，禁止改写）：
  > "for their prominent position in the international movement for peace and arbitration."
- **官方获奖理由中译**（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）：
  > 表彰他们在国际和平与仲裁运动中的杰出地位
- **气质关键词**：**反对殖民扩张的参议员、两次海牙和会的法国代表、欧洲联合的先声构想者**
- **设计母题**：**桥梁与橄榄枝（bridges）**。他一生在法英殖民争端、海牙和会、欧洲联合构想之间「搭桥」——封面可用跨越水面的连拱桥剪影，象征「以仲裁替代战争的外交工程」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Paul-Henri-Benjamin_d_Estournelles_de_Constant/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/`（OpenPeace 共享封面）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，全部取自 page.md，无载禁补】

- 生卒：1852-11-22 生于拉弗莱什（La Flèche，Sarthe 省，卢瓦尔河支流 Loir 河谷）~ 1924-05-15 逝于巴黎，享年 71 岁（frontmatter 另有 1852-01-22 / 1852-01-01 / 1924-01-01 噪声值，一律以正文 infobox **11-22 / 05-15** 为准）
- 出身：Constant de Rebecque 家族；法国大革命时期作家政治家 **Benjamin Constant 是其曾叔祖（great-uncle）**
- 教育：巴黎路易大帝中学（Lycée Louis-le-Grand），学法律与东方语言
- 任职机构与经历：
  - 1876 年开始外交官生涯；早期派驻门的内哥罗（Montenegro）、奥斯曼帝国、荷兰、英国、突尼斯
  - 1882 年回巴黎任外交部黎凡特司（Levant bureau）副司长
  - 1890 年派驻伦敦任法国代办（chargé d'affaires），在殖民争端中发挥作用、避免与英国开战
  - 1895 年转战议会，当选众议员（Chamber of Deputies）
  - 1904 年当选参议员（Senate），任期至 1924 年职业终点
- 议员主张（客观记录，不加评价）：
  - 反对第三共和国殖民政策；主张以保护国（protectorate）政策取代同化（assimilation）纲领；主张取消法国议会中的殖民地席位
  - 强烈反对在马达加斯加建立殖民统治、反对列强瓜分中国
  - 国内事务关注 "outrages against morality"（当日术语）；属德雷福斯派（Dreyfusard），主张将左拉遗骸移入先贤祠
- 和平与仲裁事业：
  - 1900 年起任常设仲裁法院（Permanent Court of Arbitration）成员
  - 代表法国出席两次海牙和会（与 Léon Bourgeois、Louis Renault 同为代表团成员），推动以调停特别是国际仲裁和平解决国际冲突
  - 1904 年起（更正式地自 1905 年）主持国际调解协会（Association de Conciliation Internationale）
  - 提出欧洲联合（European union）的构想
- 其他事业：
  - 1907 年当选美国哲学学会（American Philosophical Society）国际会员
  - 1908-08-08 ~ 1909-01-02 协助 Léon Bollée（美国航空先驱 Wilbur Wright 的主要支持者）在勒芒（Le Mans）与萨尔特进行航空试验
  - 著历史与政治作品，亦写剧本；定期为《Le Temps》《La Revue de Paris》《La Revue des deux mondes》撰稿
  - 妻子是美国人 Daisy Sedgwick Berend；多次游历美国并撰写美国题材
- 获奖：1909 年诺贝尔和平奖（与 Beernaert 共享，为建设国际法、特别是组织 1899 与 1907 年海牙会议促成常设仲裁法院之功）；是继 Frédéric Passy（1901）、Louis Renault（1907）之后第三位获此奖的法国人；法国国内报纸对此报道寥寥，仅《La Croix》头版刊出
- 身后：拉弗莱什有两所以其命名的学校（普通与技术高中、幼儿园）；曼恩大学（Université du Maine）法经管学院有以其命名的阶梯教室；勒芒雅各宾广场有其半身像（Paul Landowski 作）
- 关键时间线（20 节点，全部 page.md 明载）：
  1. 1852-11-22 生于 La Flèche
  2. 就读巴黎路易大帝中学（法律与东方语言）
  3. 1876 开始外交生涯
  4. 派驻门的内哥罗 / 奥斯曼帝国 / 荷兰 / 英国 / 突尼斯
  5. 1882 回巴黎任外交部黎凡特司副司长
  6. 1890 驻伦敦代办，化解对英殖民争端战祸
  7. 1895 当选众议员
  8. 反对第三共和国殖民政策（马达加斯加、列强瓜分中国）
  9. 德雷福斯派，主张左拉入先贤祠
  10. 1900 起任常设仲裁法院成员
  11. 1904 当选参议员（至 1924）
  12. 1904/1905 起主持国际调解协会
  13. 与 Bourgeois、Renault 同为海牙和会法国代表
  14. 提出欧洲联合构想
  15. 1907 当选美国哲学学会国际会员
  16. 1908-08 ~ 1909-01 协助 Bollée/Wright 勒芒航空试验
  17. 1909-12-10 获诺贝尔和平奖（与 Beernaert 共享）
  18. 法国史上第三位和平奖得主（Passy、Renault 之后）
  19. 为 Le Temps 等三大报刊撰稿、著述剧本
  20. 1924-05-15 逝于巴黎

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Paul-Henri-Benjamin_d_Estournelles_de_Constant/` 下建 `images/`
- Makefile 设置 `MAIN=Paul-Henri-Benjamin_d_Estournelles_de_Constant_zh`、`VIDEO_NAME` 同名
- 肖像：page.md 内嵌 Commons 图两幅——本人照片与 **Bernhard Österman 1907 年肖像画**（可作主肖像，画质感强）；250px 改 500px 下载；404 则用装饰圆占位

### 第 4 步：研究领域/事业领域表 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international arbitration | 国际仲裁 | 常设仲裁法院成员、海牙和会 | 仲裁页 |
| 1 | diplomacy | 外交 | 五国使馆历练、伦敦代办化解对英危机 | 外交页 |
| 2 | peace movement | 和平运动 | 主持国际调解协会 | 协会页 |
| 3 | politics | 政治 | 众议员 → 参议员三十年 | 议会页 |
| 4 | international relations | 国际关系 | 欧洲联合构想、反殖民扩张主张 | 构想页 |

- yaml `fields` 与上表一致（5 条）；入库 `person_field` 带 rank

### 第 4.5 步：社会关系表 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Auguste Beernaert | 无向 | 1909 诺贝尔和平奖共同得主 |
| spouse | Daisy Sedgwick Berend | 无向 | 妻子，美国人 |
| other | Benjamin Constant | 无向 | 曾叔祖（great-uncle），大革命时代作家政治家 |
| colleague | Permanent Court of Arbitration | 无向 | 1900 年起任成员；1909 诺奖表彰其海牙会议组织之功 |
| colleague | Association de Conciliation Internationale | 无向 | 1904 年起（正式 1905 年）主持 |
| colleague | Léon Bourgeois | 无向 | 同为海牙和会法国代表团成员 |
| colleague | Louis Renault | 无向 | 同为海牙和会法国代表团成员 |

- 对方 name_en 用 manifest 规范名 `Auguste Beernaert`；机构 stub 为 org 占位；`Léon Bourgeois` 为新建 stub（1920 诺贝尔和平奖得主，后续批次入库时回填）；`Louis Renault` 为新建 stub（1907 和平奖得主，法学家——注意与汽车业 Louis Renault 同名，note 已注「法学家」语境）
- Bollée/Wright 航空协助系事实叙述，非核心社会关系，不入库

### 第 5 步：配色方案 【模板通用，人物专属色彩】

- **气质**：外交辞令的优雅、跨海峡的视野、欧洲联合的先声
- **配色**：主色 `#14324F`（深海军蓝，manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + badgeA–D 四分类色
  - `badgeA` 国际仲裁 — 靛蓝 `#3F51B5`
  - `badgeB` 外交生涯 — 青绿 `#0E7C7B`
  - `badgeC` 和平运动 — 琥珀 `#E07B30`
  - `badgeD` 议会与构想 — 玫瑰 `#C4204F`
- **背景母题**：连拱桥剪影 + 稀疏的金色圆点，呼应「桥梁」母题

### 第 6 步：规划幻灯片序列 【人物专属，14–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 仲裁的架桥人 / Paul Henri d'Estournelles de Constant 1852–1924 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、全名、家族、教育、外交与议会履历、荣誉、诺奖）
03  事业概览 — 国际仲裁 / 外交 / 和平运动 / 议会 / 国际关系构想
04  家世与教育 (1852–1876) — Constant de Rebecque 家族、曾叔祖 Benjamin Constant、路易大帝中学
05  外交五站 (1876–1882) — 门的内哥罗 / 奥斯曼 / 荷兰 / 英国 / 突尼斯
06  黎凡特司与伦敦 (1882–1895) — 副司长、驻英代办、化解对英殖民危机
07  转战议会 (1895–1904) — 众议员、反殖民扩张主张
08  参议员三十年 (1904–1924) — 殖民议题、保护国政策主张
09  海牙和会与常设仲裁法院 — 法国代表、1900 起任 PCA 成员
10  国际调解协会 — 1904/1905 主持，推动仲裁、裁军与和平
11  欧洲联合的先声 — European union 构想
12  1909 诺贝尔和平奖 — 与 Beernaert 共享、法国第三位、国内报道寥寥
13  多面人生 — 著述剧本、三大报刊、美国之行与 Wright 勒芒试验
14  身后 — La Flèche 学校、Université du Maine、Landowski 半身像
15  结尾
```

### 第 7–8 步：Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`
- 每写完一页 `make distclean && make`，`pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- 表格页安全负间距：顶部 −0.35cm、`arraystretch` 0.78–0.82

### 第 9 步：史实审查 + 术语审查 【人物专属】

**d'Estournelles de Constant 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 生卒噪声 | frontmatter 生年三值（01-22 / 11-22 / 01-01）、卒年两值（05-15 / 01-01），一律以正文 infobox **1852-11-22 / 1924-05-15** 为准 |
| 姓名形式 | 姓名变体极多（page.md 明言），立传统一用标题形式 **Paul Henri d'Estournelles de Constant**，全名只在身份信息页出现一次 |
| 海牙年份两说 | 正文一处写 "Hague Peace Conferences (1898 and 1907)"、另一处写 "In 1899, then in 1907"——页内自相矛盾；通行口径为 **1899**，立传取 1899 并可加脚注「页内另有 1898 之说」 |
| 第三位法国人 | 「继 Passy（1901）、Renault（1907）之后第三位法国和平奖得主」系 page.md 明载，可写；勿扩写成「第三位法国诺奖得主」 |
| Benjamin Constant | 是其 **great-uncle（曾叔祖）**，非祖父非伯父；血缘关系仅此一句，勿展开「思想传承」等无载推断 |
| 同名 Louis Renault | 海牙代表团的 Louis Renault 是**法学家（1907 和平奖）**，与创办雷诺汽车的 Louis Renault 同名，note 与图注必须带语境 |
| 瓜分中国表述 | 「反对列强瓜分中国」系 page.md 明载的历史事实，客观转述即可，不加任何评价性语句；相关内容一律不与当代政治关联 |
| 获奖理由口径 | 官方理由是 "their prominent position"（二人共享、理由同句）；勿写成个人专属理由 |
| 无载禁写清单 | 具体出生日之外的家族成员、法律与东方语言的学位细节、五站外交的具体年份、参议员选区、著作书名清单（page.md 未列具体书目）——一律禁写 |
| 航空试验 | 勒芒协助 Bollée/Wright 试验日期为 1908-08-08 ~ 1909-01-02（page.md 明载精确日期），与诺奖同段出现时注意区分两件事 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| chargé d'affaires | 代办 | 外交职衔，勿译「大使」 |
| Chamber of Deputies | 众议院 | 法国第三共和国下院 |
| Senate | 参议院 | 1904 当选 |
| Permanent Court of Arbitration | 常设仲裁法院 | PCA，1899 海牙体系产物 |
| Association de Conciliation Internationale | 国际调解协会 | 法文原名保留 |
| protectorate | 保护国 | 与 assimilation（同化）对照 |
| Dreyfusard | 德雷福斯派 | 历史专有名词 |
| great-uncle | 曾叔祖 | 血缘辈分勿错 |
| European union | 欧洲联合 | 20 世纪初构想，勿与现代 EU 制度混同 |
| La Croix | 《十字架报》 | 法国报纸，唯一头版报道获奖的报纸 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配，勿改】

- **选定曲目**：**Cinematic Experience** — Alex-Productions
- **bgm_path**：`music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`
- **匹配理由**：史诗感的配器匹配其「五国外交、两届海牙、三十年议会」的多幕人生跨度；电影化叙事贴合从外交官到欧洲联合构想者的戏剧性弧线。
- **备选**（未采用，仅存档）：Eternals（已分配给 Beernaert，同批避曲）、New Lands（开拓感更贴殖民地议题但过于冒险气质）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Paul-Henri-Benjamin_d_Estournelles_de_Constant/page.md` | 本地 Wikipedia 正文（唯一事实来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参考 |
| `peace/presentations/cover/` | OpenPeace 共享封面 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |

> **开始执行。每完成一步汇报。**
