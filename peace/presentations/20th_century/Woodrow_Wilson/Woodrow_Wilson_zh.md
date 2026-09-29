# OpenPeace 和平奖得主立传提示词（人物：Woodrow Wilson）

> **本文件是 OpenPeace「诺贝尔和平奖得主立传提示词」的人物专属实例**，以 Woodrow Wilson（1919 诺贝尔和平奖，国际联盟缔造者）为对象。
> 结构母本沿用物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 的 0–11 节骨架，按和平奖人物特点适配。
> 凡标注【模板通用】可复用；标注【人物专属】按 Wilson 替换。直接复制本文件到新对话执行，逐步汇报。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Thomas Woodrow Wilson（托马斯·伍德罗·威尔逊），美国第 28 任总统，1919 诺贝尔和平奖得主。
- **设计哲学**：和平奖人物立传与科学家立传的核心差异，在于叙事重心是**事业与历史场域**（而非公式与实验），但「身份信息页」与「事业领域结构化表达」两块骨架务必保留；涉及政治与历史争议的内容一律只作 page.md 明载的客观事实记录。

---

## 二、背景信息 【人物专属】

- **目标人物**：Thomas Woodrow Wilson（1856-12-28 ~ 1924-02-03，享年 67 岁）
- **获奖理由（1919 诺贝尔和平奖，2020-12-10 颁发）**：
  > "for his role as founder of the League of Nations"（表彰他作为国际联盟缔造者所发挥的作用）
  > 英文原文取自 `peace/nobel_peace_citations.json`，中译照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写。
- **气质关键词**：**国际联盟的总设计师、十四点的提出者、学院派总统**
- **设计母题**：**国际秩序蓝图（blueprint of world order）**。从《国会政府》到十四点再到国联盟约，Wilson 一生都在为共同体起草「章程」——以契约线条、文件文本、地图轮廓为视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Woodrow_Wilson/page.md`（Wikipedia 全文 + frontmatter：QID Q34296）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/`（OpenPeace 统一 `\input`，如侧无现成文件则复用 openmath/openphysicist 首页骨架改品牌字样）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报；含「研究领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库。

### 第 0 步：通读 page.md 建立事实基准 【人物专属，已核对】

- 生卒：1856-12-28 生于弗吉尼亚州斯汤顿（长老会牧师宅）~ 1924-02-03 逝于华盛顿特区，享年 67 岁；安葬于华盛顿国家大教堂（唯一安息于首都的美国总统）
- 国籍：美国；生于南方，内战与重建时期在佐治亚/南卡罗来纳长大
- 家庭：父 Joseph Ruggles Wilson（长老会牧师，南卡哥伦比亚神学院教授）；母 Jessie Janet Woodrow；兄妹四人中排行第三、长子
- 教育：Davidson College（1873–74）→ 普林斯顿（时名新泽西学院，1879 AB，修政治哲学与历史）→ 弗吉尼亚大学法学院（因健康退学，自学法律，佐治亚州律师执照，1882 亚特兰大短暂开业）→ Johns Hopkins 博士（1883 入学，1886 历史学与政府学博士，**唯一拥有 PhD 的美国总统**）
- 学术任职：Bryn Mawr（1885–88）→ Wesleyan（1888–90，带橄榄球队）→ 普林斯顿法学与政治经济学讲座教授（1890，年薪 $3,000）→ 普林斯顿第 13 任校长（1902-10-25 ~ 1910-10）
- 政治任职：新泽西州第 34 任州长（1911-01-17 ~ 1913-03-01）→ 美国第 28 任总统（1913-03-04 ~ 1921-03-04，民主党）
- 关键荣誉：Nobel Peace Prize 1919；巴黎大学荣誉博士；华沙/克拉科夫雅盖隆大学荣誉博士；American Academy of Arts and Sciences Fellow；1897 美国哲学学会会员
- 核心事业清单：
  1. 政治学与公共行政奠基——《国会政府》(1885)、《行政学研究》(1887，公共行政学科开创性论文)、《国家》(The State)、《分裂与重聚》(1893)、《美国人民史》五卷 (1902)
  2. 普林斯顿改革——荣誉课程/导师制（preceptorial system）、筹款扩建、四合院计划受挫
  3. 「新自由」内政——1913《税收法》（现代所得税开端）、《联邦储备法》（美联储）、反托拉斯与劳工立法
  4. 一战外交——1914–17 中立斡旋，1917-04 对德宣战，1918-01-08 十四点演说
  5. 巴黎和会与国际联盟——1919 首位任内出访欧洲的在任总统，「四巨头」之一，亲自主持国联盟约起草委员会，《凡尔赛条约》 incorporated 国联盟约
  6. 晚年——1919-10-02 中风左瘫，1920-03-19 促成支持者否决带保留条件的条约批准，1921 离任后与 Bainbridge Colby 开律师事务所
- 关键时间线（15–20 节点）：1856 生 → 1873 Davidson → 1879 普林斯顿毕业 → 1882 亚特兰大开业律师 → 1883 进 Johns Hopkins + 订婚 Ellen → 1885《国会政府》出版 + 结婚 + Bryn Mawr任教 → 1886 PhD → 1887《行政学研究》→ 1890 普林斯顿讲座教授 → 1902 普林斯顿校长 → 1910 当选州长 → 1912 当选总统 → 1913 就职+税收/美联储立法 → 1915 续弦 Edith → 1916 连任 → 1917-04-06 对德宣战 → 1918-01-08 十四点 → 1918-11-11 停战 → 1919-06-28 签署凡尔赛条约 → 1919-10-02 中风 → 1920-12-10 领 1919 诺贝尔和平奖 → 1921-03 离任 → 1924-02-03 逝世

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Woodrow_Wilson/`；Makefile 设 `MAIN=Woodrow_Wilson_zh`
- 肖像：page.md/`images.txt` 有 1914 年官方照与 1875 年 Pach Bros 照等 URL，优先 250px 改 500px 下载；失败按兄弟项目经验走 Commons Special:FilePath 回退，再失败用装饰圆占位
- 项目 logo/BGM 文件按 `music_audio/` 曲库路径复制

### 第 4 步：事业领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international organization | 国际组织 | 国际联盟缔造者，诺奖理由核心 | 国联核心页 |
| 1 | diplomacy | 外交 | 一战中立斡旋、十四点、巴黎和会 | 外交页 |
| 2 | public administration | 公共行政 | 1887《行政学研究》，学科奠基人之一 | 学术页 |
| 3 | political science | 政治科学 | 《国会政府》、约翰·霍普金斯 PhD | 学术页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 只收 page.md 明载关系；方向约定：advisor-student 有向（direction: advisor=对方是导师 / student=对方是学生），其余无向自动 from<to 归一。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Herbert Baxter Adams | 对方是导师 | frontmatter 明载博士导师，Johns Hopkins 历史学与政府学博士项目 |
| advisor-student | Richard T. Ely | 对方是导师 | frontmatter 明载博士导师 |
| influence | Georg Wilhelm Friedrich Hegel | 无向 | 《行政学研究》受其法与国家学说影响（page.md 明载 influenced） |
| spouse | Ellen Axson | 无向 | 1885 结婚，1914 逝世；肖像画家 |
| spouse | Edith Bolling | 无向 | 1915-12-18 结婚 |
| parent-child | Joseph Ruggles Wilson | 无向 | 父亲，长老会牧师 |
| parent-child | Margaret Woodrow Wilson | 无向 | 长女，1886 生 |
| parent-child | Jessie Woodrow Wilson Sayre | 无向 | 次女，1887 生 |
| parent-child | Eleanor Wilson McAdoo | 无向 | 三女，1889 生 |
| colleague | Edward M. House | 无向 | 竞选经理与总统首席顾问，巴黎和会随行 |
| colleague | William Jennings Bryan | 无向 | 国务卿，1915 因对德政策辞职 |
| controversy | Henry Cabot Lodge | 无向 | 参议院条约批准之争对手，Wilson 拒绝其保留条件 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#2F4470`（深鸦蓝——外交的克制与秩序感，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- **四分类色（badgeA–D）**：`#4C5FD5`（国联/国际组织）· `#0E7C7B`（外交斡旋）· `#E07B30`（内政立法）· `#C4204F`（学术与写作）
- **背景母题**：契约文本横线 + 淡色地图经纬网格，呼应「国际秩序蓝图」

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input 项目首页模板）
01  封面 — 国际联盟缔造者 / Woodrow Wilson 1856–1924 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/本名/国籍/教育/师承/任职/荣誉/核心领域）
03  战后南方的牧师之子 (1856–1879) — 斯汤顿出生、内战记忆、Davidson、普林斯顿
04  学者之路：Johns Hopkins 博士 (1879–1886) — 律师转行、《国会政府》、唯一 PhD 总统
05  政治学奠基：《行政学研究》(1885–1890) — Bryn Mawr/Wesleyan、公共行政开创
06  普林斯顿教授与校长 (1890–1910) — 讲座教授、《美国人民史》、校长改革与受挫
07  新泽西州长 (1910–1913) — 与党机器决裂、初选法/反腐败/工伤赔偿
08  1912 大选与「新自由」— 三角对决 Taft/Roosevelt、Brandeis 影响、南方人首胜
09  总统内政：税收与美联储 (1913–1916) — Revenue Act、Federal Reserve Act、连任
10  中立与参战 (1914–1917) — Lusitania、无限制潜艇战、1917-04 宣战
11  十四点与国际联盟 (1918–1919) — ★核心页——1918-01-08 演说、国联盟约、巴黎和会「四巨头」
12  《凡尔赛条约》与参议院挫败 (1919–1920) — Lodge 之争、1920-03-19 否决、1919-10-02 中风
13  诺贝尔和平奖 (1919) — 理由原句、1920-12-10 领奖、第二位任内获奖的在任美国总统
14  晚年与遗产 (1921–1924) — 律所、Armistice Day 演说、逝世与安葬、国联→联合国
15  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式沿用标杆：`\plainbar`/`\deckbackground`/`\sectiontitle` 骨架可整体复用 Kenneth_G_Wilson_zh.tex；每写一页 make，溢出修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标
- 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方仅 "for his role as founder of the League of Nations"，勿掺入十四点/凡尔赛等引申；1919 年度奖 1920-12-10 才颁发 |
| 死亡日期 | frontmatter 有 1924-02-03 与 1924-02-23 双值，以 infobox/正文 **02-03** 为准 |
| PhD 表述 | 是「唯一拥有博士学位的美国总统」，勿写「首位」「史上仅有的学者总统」等 |
| 任内获奖次序 | Wilson 是继 Theodore Roosevelt 之后第二位获和平奖的在任美国总统，勿写「首位」 |
| 中风与执政 | 1919-10-02 中风后半身瘫痪，政务由夫人 Edith 与医生 Grayson 把关；有人称 Edith 为「首位女总统」系转述他人说法，须注明非正式 |
| 条约挫败 | 1920-03-19 是 Wilson 令支持者对带保留条款的批准案投反对票致其流产，属主动拒绝妥协，勿写「参议院否决了他」的笼统说法 |
| 种族记录 | 任内联邦机构种族隔离等史实 page.md 有详载，仅客观事实简述、不加评价性语句（红线） |
| 大女儿三女 | Margaret(1886)/Jessie(1887)/Eleanor(1889) 勿混；Eleanor 之夫 William Gibbs McAdoo 为财政部长，Jessie 之夫 Francis Bowes Sayre 后任驻菲律宾高级专员 |
| 父与祖父 | 父 Joseph Ruggles Wilson 是长老会牧师；祖父 James Wilson 是报人，勿混 |
| 博士导师 | Adams/Ely 仅 frontmatter 载，正文未展开，note 注明来源层级，勿杜撰细节 |
| 本名 | 本名 Thomas Woodrow Wilson，"Woodrow" 为中间名，封面与 DB 用 Woodrow Wilson |
| 巴黎和会 | 「四巨头」= Wilson/Lloyd George/Clemenceau/Orlando；Wilson 亲自主持国联盟约起草委员会，勿写「他单独起草盟约」 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| League of Nations | 国际联盟 | 简称「国联」，勿与联合国混 |
| Covenant of the League of Nations | 国联盟约 | 已并入《凡尔赛条约》 |
| Fourteen Points | 十四点 | 1918-01-08 演说 |
| Treaty of Versailles | 凡尔赛条约 | 1919-06-28 签署 |
| New Freedom | 新自由 | 竞选纲领 |
| Federal Reserve Act | 联邦储备法 | 设立美联储 |
| Revenue Act of 1913 | 1913 税收法 | 现代所得税开端 |
| Paris Peace Conference | 巴黎和会 | 1919，首位任内访欧总统 |
| Big Four | 四巨头 | Wilson/Lloyd George/Clemenceau/Orlando |
| preceptorial system | 导师制 | 普林斯顿改革 |
| Congressional Government | 《国会政府》 | 1885 博士论文成书 |
| The Study of Administration | 《行政学研究》 | 1887，公共行政奠基 |

### 引语白名单 【人物专属，仅 page.md 载有英文原文者可入引文框】

| 原文 | 场景 | 出处 |
|------|------|------|
| "a professorship was the only feasible place for me…" | 求学志向 | Johns Hopkins 入学前后 |
| "I am going to teach the South American republics to elect good men." | 1913 拉美政策 | 拉美干预节 |
| "there is such a thing as a man being too proud to fight…" | Lusitania 事件回应 | 1915 |
| "we have no selfish ends to serve…" | 1917-04-02 宣战演说 | 对德宣战 |
| "He Kept Us Out of War" | 1916 竞选口号 | 连任竞选 |

> 白名单之外的一律转述不引号；中文引号内不写「原话」除非 page.md 有英文原文（红线）。

### 第 10 步：完成判据 【模板通用】

- pdf 0 error、溢出达标（vbox ≤10pt / hbox ≤50pt）、逐页目检通过
- DB `has_social_data=1`、fields≥4、relations≥2；yaml 与提示词第 4/4.5 步完全一致
- 目录内临时目检图（preview/）最后清理

---

## 四、背景音乐 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction "Documentary Cinematic"（manifest 预分配，勿改）
- **风格**：纪录片 / 恢弘 / 电子
- **匹配理由**：纪录片质感匹配「学院派总统→战时领袖→国联设计师」的史诗叙事；「看不见的光」暗合其理念遗产——美国参议院拒绝国联，但国联的构想之光最终延续到联合国
- **本地路径**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Woodrow_Wilson/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Woodrow_Wilson.yaml` | 入库 yaml（第 4/4.5 步） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：史实全部锚定 page.md，无载禁写。**
