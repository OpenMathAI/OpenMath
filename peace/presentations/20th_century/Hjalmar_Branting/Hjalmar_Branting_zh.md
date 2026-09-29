# OpenPeace 和平奖得主立传提示词（人物：Hjalmar Branting）

> **本文件是 OpenPeace「诺贝尔和平奖得主立传提示词」的人物专属实例**，以 Hjalmar Branting（1921 诺贝尔和平奖，瑞典社会民主党领袖）为对象。
> 结构母本沿用标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 骨架，按和平奖人物特点适配。
> 凡标注【模板通用】可复用；标注【人物专属】按 Branting 替换。直接复制本文件到新对话执行，逐步汇报。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Karl Hjalmar Branting（亚尔马·布兰廷），瑞典政治家，1921 诺贝尔和平奖共享得主。
- **设计哲学**：和平奖人物立传以**事业与历史场域**为叙事重心，但「身份信息页」与「事业领域结构化表达」骨架务必保留；涉及政治意识形态与种族争议的内容一律只作 page.md 明载的客观事实记录，不加评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Karl Hjalmar Branting（1860-11-23 ~ 1925-02-24，享年 64 岁）
- **获奖理由（1921 诺贝尔和平奖，与 Christian Lange 共享）**：
  > "for their lifelong contributions to the cause of peace and organized internationalism"（表彰他们毕生对和平事业与有组织的国际主义的贡献）
  > 英文原文取自 `peace/nobel_peace_citations.json`，中译照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写。
- **气质关键词**：**瑞典社会民主党的缔造者、普选权的旗手、把争端交给国联的总理**
- **设计母题**：**选票与仲裁席（ballot and arbitration）**。从「和平过渡」的政治信条到把奥兰群岛争端交国联裁决，其事业母线是「以制度程序代替武力」——投票箱、议会席位、国联议事圆桌为视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Hjalmar_Branting/page.md`（Wikipedia 全文 + frontmatter：QID Q53620）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 同批实例：`peace/presentations/20th_century/Woodrow_Wilson/Woodrow_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报；含「事业领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库。

### 第 0 步：通读 page.md 建立事实基准 【人物专属，已核对】

- 生卒：1860-11-23 生于斯德哥尔摩 ~ 1925-02-24 逝于斯德哥尔摩，享年 64 岁
- 国籍：瑞典
- 家庭：父 Lars Gabriel Branting（教授）；母 Emma af Georgii（贵族出身钢琴家）；配偶 Anna Branting（本姓 Jäderin）；子女 Georg Branting、Sonja Branting-Westerståhl
- 教育：斯德哥尔摩 + 乌普萨拉大学；数学天文学科班出身，曾任斯德哥尔摩天文台助理
- 核心事业清单：
  1. 从天文台到新闻界——1884 转行记者，主编党报《Social-Demokraten》与《Tiden》；1888 因刊发 Axel Danielsson 文章被判亵渎罪监禁三个月
  2. 缔造瑞典社会民主党（SAP）——1889 与 August Palm 共同组织建党；1896 起任议员，最初六年是 SAP 在议会唯一议员
  3. 1905 挪威危机——反对以战争维持瑞挪联盟，提出口号 "Hands off Norway, King!"，组织抵制预备役征召并准备总罢工，史家视为挪威和平独立的重要因素
  4. 修正主义路线——接受 Eduard Bernstein 对马克思主义的修正，主张经普选权与议会立法和平过渡
  5. 1917 年立场——支持俄国二月革命、声援孟什维克与克伦斯基政府并亲赴彼得格勒探访；谴责十月革命夺权；党内分裂，青年联盟在 Zeth Höglund 带领下出走另组左翼党（后改组为瑞典共产党）；Höglund 在 Branting 身后回党并著两卷本传记
  6. 三度出任首相——1920-03-10 ~ 1920-10-27；1921-10-13 ~ 1923-04-19（兼任外交大臣）；1924-10-18 起第三任期（1924 大选获胜后组阁），1925-02-24 任内病逝；另于 1917-10-19 ~ 1918-01-05 在 Edén 内阁任财政大臣
  7. 国际联盟——把瑞典带入国联并亲身任代表；奥兰群岛争端交国联裁决（群岛成为芬兰自治区）；1921 与挪威人 Christian Lous Lange（各国议会联盟秘书长）共享诺贝尔和平奖
- 关键时间线（15–20 节点）：1860 生斯德哥尔摩 → 乌普萨拉大学数学天文 → 斯德哥尔摩天文台助理 → 1884 转行记者 → 1888 亵渎罪监禁三月 → 1889 与 Palm 建党 SAP → 1896 首入议会（唯一议员）→ 1905 「别碰挪威」反战 → 1908 创刊《Tiden》→ 1917-10 财政大臣 → 1917 访克伦斯基+党内分裂 → 1920-03-10 首任首相 → 1921-10-13 再任首相兼外相 → 1921 诺贝尔和平奖（与 Lange 共享）→ 1923-04-19 下台 → 1924-10-18 第三任组阁 → 1925-02-24 任内逝世

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Hjalmar_Branting/`；Makefile 设 `MAIN=Hjalmar_Branting_zh`
- 肖像：page.md 有 1917 年照与斯德哥尔摩 Branting Monument 照，走 Commons Special:FilePath 500px 下载；失败按兄弟项目经验换文件名回退，再失败用装饰圆占位
- 项目 logo/BGM 文件按 `music_audio/` 曲库路径复制

### 第 4 步：事业领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international organization | 国际组织 | 力推瑞典加入国联、奥兰争端交国联裁决，诺奖理由核心 | 国联核心页 |
| 1 | universal suffrage | 普选权 | 毕生倡导普选与议会道路 | 政治页 |
| 2 | social democracy | 社会民主主义 | 接受 Bernstein 修正主义、改良主义路线 | 思想页 |
| 3 | labor rights | 劳工权利 | 八小时工作制等劳工立法倡导 | 政治页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 只收 page.md 明载关系；对手方 name_en 用 manifest `name` 字段（Lange 用 "Christian Lange"）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Christian Lange | 无向 | 1921 诺贝尔和平奖共同得主 |
| influence | Eduard Bernstein | 无向 | 接受其对马克思主义的修正，转向改良主义 |
| colleague | August Palm | 无向 | 1889 共同组织创建瑞典社会民主党 |
| colleague | Nils Edén | 无向 | 1917–1918 Edén 内阁任财政大臣 |
| controversy | Zeth Höglund | 无向 | 1917 党内分裂，青年联盟出走由其领衔；Höglund 身后回党并著两卷本传记 |
| spouse | Anna Branting | 无向 | 配偶，本姓 Jäderin |
| parent-child | Lars Gabriel Branting | 无向 | 父亲，教授 |
| parent-child | Emma af Georgii | 无向 | 母亲，贵族出身钢琴家 |
| parent-child | Georg Branting | 无向 | 儿子 |
| parent-child | Sonja Branting-Westerståhl | 无向 | 女儿 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#1B4D6B`（北欧海蓝——瑞典社民的沉稳与秩序感，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- **四分类色（badgeA–D）**：`#4C5FD5`（国联与国际主义）· `#0E7C7B`（普选与议会道路）· `#E07B30`（劳工权利）· `#C4204F`（党内论战与分裂）
- **背景母题**：选票方格与圆桌同心圆 + 淡色北欧经纬线

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input 项目首页模板）
01  封面 — 瑞典社会民主党领袖 / Hjalmar Branting 1860–1925 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/全名/国籍/教育/任职/荣誉/核心领域）
03  天文台里的转向 (1860–1884) — 乌普萨拉数学天文、斯德哥尔摩天文台助理、弃学从笔
04  党的缔造者 (1884–1896) — 党报主编、1888 亵渎罪三月、与 Palm 建党、唯一议员六年
05  「别碰挪威，国王！」(1905) — 反对战争维护联盟、总罢工准备、挪威和平独立
06  修正主义与和平过渡 — Bernstein 影响、普选权信条、议会道路
07  1917：彼得格勒与党内分裂 — 支持克伦斯基、谴责十月革命、Höglund 出走
08  首任首相与国联 (1920) — 奥兰群岛争端交国联裁决
09  诺贝尔和平奖 (1921) — 与 Lange 共享、获奖理由原句 ★核心页
10  三度组阁 (1921–1925) — 兼任外交大臣、1924 大选胜利
11  任内病逝与身后 (1925) — Sandler 接任首相、Hansson 接掌党务、斯德哥尔摩纪念碑
12  遗产：北欧社会民主道路的开端
13  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式沿用标杆：`\plainbar`/`\deckbackground`/`\sectiontitle` 骨架可整体复用 Kenneth_G_Wilson_zh.tex；每写一页 make，溢出修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标
- 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 共享句 "for their lifelong contributions…"（they 复数指 Branting+Lange 两人），中英均照抄名录，勿改成 his |
| 死亡日期 | frontmatter 有 02-24 与 02-21 双值，以 infobox/正文 **02-24** 为准 |
| 共享对手方 | Lange 是挪威人、各国议会联盟（Inter-Parliamentary Union）秘书长；DB 对手方名用 manifest 规范名 "Christian Lange" |
| 全名 | Karl Hjalmar Branting；DB/封面用 Hjalmar Branting |
| 莱茵争议 | page.md 明载其支持关于法属殖民地部队的虚假说法（Black Horror on the Rhine），仅客观一句记录该事实，禁引原文、禁展开渲染（红线） |
| 亵渎罪 | 1888 监禁三月缘于刊发 Danielsson 文章，宗教敏感仅客观记录刑罚事实，不复述文章内容 |
| 意识形态 | 「接受 Bernstein 修正主义/改良主义」是 page.md 明载事实，只作立场陈述、不加褒贬；对二月革命/十月革命的立场同理 |
| 三任首相 | 三段任期日期（1920 / 1921–23 / 1924–25）与兼职（第二任兼外交大臣、1917 财政大臣）勿混 |
| 奥兰群岛 | 是「他把争端交国联裁决」、群岛成为芬兰自治区，勿写成「瑞典收回」或「芬兰并入瑞典」 |
| Höglund | 1917 分裂后另组政党；Branting 死后 Höglund 回党并写两卷本传记——两件事分属两时态，勿混为同期 |
| 身后接任 | 首相由 Rickard Sandler 接任、党魁由 Per Albin Hansson 接任，勿互换 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Swedish Social Democratic Party | 瑞典社会民主党 | 缩写 SAP |
| universal suffrage | 普选权 | 其议会道路核心 |
| eight-hour workday | 八小时工作制 | 劳工权利主张 |
| Inter-Parliamentary Union | 各国议会联盟 | Lange 任秘书长 |
| revisionism | 修正主义 | Bernstein 一脉 |
| Riksdag | 瑞典议会 | 勿译「国会大厦」 |
| Åland Islands | 奥兰群岛 | 国联裁决归芬兰自治 |
| blasphemy | 亵渎罪 | 1888 判刑缘由 |
| Tiden | 《时代》 | 1908 创刊月刊 |
| League of Nations | 国际联盟 | 简称国联 |

### 引语白名单 【人物专属，仅 page.md 载有英文原文者可入引文框】

| 原文 | 场景 | 出处 |
|------|------|------|
| "Hands off Norway, King!" | 1905 挪威危机口号 | 反战运动 |

> 白名单之外一律转述不引号；中文引号内不写「原话」除非 page.md 有英文原文（红线）。

### 第 10 步：完成判据 【模板通用】

- pdf 0 error、溢出达标（vbox ≤10pt / hbox ≤50pt）、逐页目检通过
- DB `has_social_data=1`、fields≥4、relations≥2；yaml 与提示词第 4/4.5 步完全一致
- 目录内临时目检图（preview/）最后清理

### 第 0.5 步：OpenPeace 品牌口径 【模板通用】

- 封面右上肖像带 `draw=coveraccent!50` 细边框 + 姓名小字注；封面国籍行 `\faIcon{globe}\enspace Sweden`
- 身份信息页信息网格至少含：生卒、全名、国籍、出生地、教育、任职、主要荣誉、核心领域，事实取自 page.md infobox
- 结尾页底部品牌统一 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复
- 共享年份得主（Branting/Lange）封面 badge 区加「Shared with Christian Lous Lange」小字标注

---

## 四、背景音乐 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（manifest 预分配，勿改）
- **风格**：情感 / 电子 / 张力
- **匹配理由**：曲目名「崩解与重组」暗合其一生主题——旧联盟的解体（1905 瑞挪和平分家）、旧党的分裂（1917 出走潮）与旧帝国的瓦解，而他始终以制度与和平方式承接每一次「崩解」；低回的情感质感亦贴合其任内病逝的结尾
- **本地路径**：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Hjalmar_Branting/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Hjalmar_Branting.yaml` | 入库 yaml（第 4/4.5 步） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

---

## 六、与同批人物的交叉注记 【人物专属，Review 对照用】

- **Christian Lange 篇**：两人 1921 共享和平奖，co-honored 关系双向各写一条（同句理由），note 措辞保持一致；Lange 身份固定为「挪威人、各国议会联盟秘书长」。
- **Wilson/Bourgeois 篇**：Branting 的国联叙事是「把瑞典带入国联 + 奥兰裁决案例」，与 Wilson 的「缔造者」、Bourgeois 的「大会首任主席」三层角色互不重叠，勿混写。
