# Sidney Altman（西德尼·奥尔特曼）立传提示词

> qid=Q102266 · 1939-05-07 – 2022-04-05 · 加拿大/美国分子生物学家 · 20 世纪 · 诺贝尔化学奖（1989，与 Thomas Cech 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Sidney_Altman/`（page.md + metadata.json）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像若无本地文件则下载 Wikipedia 头像（Altman in 2011）；下载失败用装饰圆占位并如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspaceRNA 也可以是酶\enspace·\enspace 加拿大 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「RNA 链 / 剪切」母题——离散圆点暗示核苷酸序列与被剪下的片段。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如 RNase P = RNA 亚基 + 蛋白亚基 → 单独 RNA 亚基即有催化活性）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sidney Altman（中文惯称：西德尼·奥尔特曼）
- **生卒**：1939-05-07 生于加拿大魁北克省蒙特利尔 → 2022-04-05 逝于美国新泽西州 Rockleigh（久病之后），享年 82
- **国籍**：加拿大出生；1984 年入籍美国，此后为美加双重国籍
- **身份**：分子生物学家；耶鲁大学 Sterling Professor（分子、细胞与发育生物学及化学教授）
- **家庭**：父母是 1920 年代移居加拿大的东欧犹太移民——母 Ray（娘家姓 Arlin）生于波兰比亚韦斯托克（Białystok），18 岁随姐妹来加拿大，纺织厂做工；父 Victor Altman 生于乌克兰，曾在苏联集体农场做工，来加拿大后在蒙特利尔经营小杂货店。奥尔特曼把父母的人生看作劳动价值观的写照。
- **配偶与子女**：1972 年娶 Ann M. Körner（哲学家 Stephan Körner 之女）；育有 Daniel 与 Leah 二人；2018 年离婚（infobox：m. 1972; div. 2018）
- **教育轨迹**：
  - MIT 学物理，1960 年获学士学位（在校是冰球队成员）
  - 1960 后在哥伦比亚大学读物理研究生约 18 个月，因个人原因与缺乏实验室机会辍学
  - 后入科罗拉多大学医学中心改学生物物理
- **博士**：1967 年科罗拉多大学（University of Colorado）生物物理学博士；导师 Leonard Lerman；论文《Bacteriophage T4 DNA replication in the absence and presence of 9-aminoacrine》（吖啶类对 T4 噬菌体 DNA 复制的影响）
- **研究领域**：分子生物学——RNase P、核酶（ribozyme）、tRNA 成熟

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **移民杂货店之子（1939）**：蒙特利尔犹太移民家庭，母亲纺织工、父亲杂货店店主；自述从中习得"稳定环境中的努力终有回报，哪怕只是极小的增量"。
2. **从物理转向生物（1958–1967）**：MIT 物理 → 哥伦比亚辍学 → 科罗拉多改学生物物理；吖啶对 T4 噬菌体 DNA 复制的效应成为博士课题。
3. **追随导师迁徙（1967–1969）**：Lerman 1967 年转往 Vanderbilt，奥尔特曼随行短期做分子生物学研究，随后赴哈佛。
4. **哈佛 Meselson 实验室**：研究参与 T4 DNA 复制与重组的 DNA 内切酶——第一个博士后站点。
5. **MRC LMB（剑桥）**：开启通往 RNase P 的研究路线；John D. Smith 及多位博士后同事给了他关键建议，使其得以验证想法。
6. **命运的 tRNA 前体（1971 前）**："第一个放射性化学纯的 tRNA 前体分子的发现，使我能拿到 1971 年耶鲁助理教授的职位——那是个任何工作都难找的年头。"
7. **耶鲁学术阶梯（1971–1989）**：1971 助理教授 → 1980 正教授 → 1983–85 系主任 → 1985 出任 Yale College 院长四年 → 1989-07-01 回归全职教授。
8. **RNase P 之谜**：RNase P 是核糖核蛋白颗粒（细菌中 1 个 RNA 亚基 + 1 个蛋白质亚基），负责 tRNA 前体成熟；传统观点认为催化活性来自蛋白亚基。
9. **RNA 即酶（1980s）**：试管重建实验中发现——**单独的 RNA 亚基**即可执行全部催化活性：RNA 本身具有催化性质，与 Cech 的发现共同颠覆"酶必是蛋白质"的教条。
10. **真核的对照（后期工作）**：真核生物的 RNase P 恰好相反——蛋白亚基对催化活性必不可少；同一复合物在两界策略相反。
11. **1989 诺贝尔化学奖**：与 Thomas R. Cech 共享，"for their discovery of catalytic properties of RNA"（两人独立发现 RNA 的催化性质）。
12. **荣誉序列**：1988 美国艺术与科学院 Fellow；1990 美国国家科学院院士 + 美国哲学学会会员；Rosenstiel Award（1988）、Lomonosov 金质奖章（2016）；McGill 荣誉博士。
13. **双国籍的移民科学家**：1958 年离蒙市赴 MIT 后长居美国，1984 年入籍美国并保留加拿大国籍——一生横跨两国两种文化。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepsea） | `#0F4C5C` | 深海般的 RNA 世界——冷静、深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（RNase P badgeRnasep） | `#2E5A9E` | 蓝核糖核蛋白颗粒 / tRNA 成熟 |
| 分类色 2（核酶 badgeRibozyme） | `#1B7A43` | 绿RNA 自身催化 / 1989 诺奖 |
| 分类色 3（求学生涯 badgeEdu） | `#D97B29` | 琥珀MIT—哥伦比亚—科罗拉多 |
| 分类色 4（耶鲁岁月 badgeYale） | `#C0395B` | 玫瑰耶鲁执教 / 院长岁月 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「RNA 链被剪断 / 片段飞离」的瞬间。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（文件：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav`；不要复制 wav 文件，Makefile 引用绝对/相对路径即可）
- **风格**：克制抒情 / 电子氛围 / 静水深流
- **匹配理由**：
  - "静水深流" 匹配其气质——不是英雄式突破，而是几十年沉潜于一个酶的耐心
  - "克制抒情" 匹配 RNA 亚基独自催化的那一幕——旧教条（酶必是蛋白质）在安静的试管里分崩离析（Falling Apart 的字面呼应）
  - "电子氛围" 匹配分子生物学时代的纪录片质感：蒙特利尔杂货店 → MIT → 剑桥 LMB → 耶鲁 → 1989 斯德哥尔摩
- **时长**：以曲文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — RNA 也可以是酶 / Sidney Altman 1939–2022 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/配偶/出生地/去世地/领域/荣誉）
03  奥尔特曼的一生 — Sanger 式时间线（10 节点：1939→1960→1967→1969→1971→1980→1985→1989→1990→2022）
04  早年：蒙特利尔移民之子 (1939–1958) — 表格「时间|事件|结果」
05  从物理到生物物理 (1958–1967) — 表格「时间|事件|结果」（MIT/哥伦比亚/科罗拉多三段转折）
06  博士后岁月：Vanderbilt 与哈佛 (1967–1969) — 表格「站点|课题|结果」
07  MRC LMB 与 tRNA 前体 (1969–1971) — 表格「问题|方法|结果」+ 引语框："the first radiochemically pure precursor..."
08  耶鲁学术阶梯 (1971–1989) — 表格「时间|职位|职责」
09  RNase P 与 RNA 催化 — 表格「问题|方法|结果」+ 公式框：RNase P 复合物 → 单独 RNA 亚基仍有催化活性
10  1989 诺贝尔化学奖 — 与 Cech 共享；官方理由 "for their discovery of catalytic properties of RNA"
11  真核对照与后期工作 — 表格「对象|观察|意义」（细菌 vs 真核 RNase P 策略相反）
12  荣誉与学会 — Sanger 式「类别|代表|意义」表格（NAS/AAAS/APS/Rosenstiel/Lomonosov/McGill 荣誉博士）
13  遗产：核酶时代 — 四分类遗产盒 + 公式框：RNA 世界图景（RNA 既是信息又是催化剂的起点）
14  结尾 — 「打破教条的，往往是一支安静的试管。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1989 诺奖口径 | 与 Thomas R. Cech **共享**，官方理由 "for their discovery of catalytic properties of RNA"——两人**各自独立**发现 RNA 催化性质，勿写"共同做出同一发现" |
| 分工表述 | Altman 的贡献是 **RNase P 的 RNA 亚基单独具催化活性**；Cech 的贡献是 **rRNA 前体自剪接**——两条线勿混、勿写成同一种酶 |
| 官方获奖理由引语 | 页面正文只给出 "for their work on the catalytic properties of RNA"（导语）与 Cech 页的 "for their discovery of catalytic properties of RNA" 两种转述；引用时注明是 Nobel 官方口径的页面转述，勿再"润色" |
| 出生地/去世地 | 生于**加拿大蒙特利尔**、逝于**美国新泽西 Rockleigh**——勿互混；入籍美国年份 1984（此前 1958 年已赴美） |
| 博士导师 | **Leonard Lerman**（科罗拉多大学，1967）——勿写成哈佛的 Meselson（那是博士后站点）或 MRC 的 John D. Smith（后者是"提供关键建议"的同事） |
| 学位描述 | MIT 1960 是**物理学士**；哥伦比亚约 18 个月**未获学位**离开；博士 1967 在**科罗拉多大学**（生物物理）——"MIT 读博"是错的 |
| 配偶 | Ann M. Körner（1972 结婚，2018 离婚；哲学家 Stephan Körner 之女）；子 Daniel、女 Leah——年份勿改 |
| 博士生 | infobox Doctoral students 仅 **Benjamin C. Stark、Robin Reed** 两人；metadata.json 的 doctoral_student 只含 Benjamin C. Stark——Robin Reed 为页面 infobox 明载，可入库；除此之外（如 Wikidata 其他来源）一律不入库 |
| Sterling Professor | 耶鲁最高教职头衔（分子、细胞与发育生物学及化学教授）——是头衔不是奖项，勿混入奖项页 |
| Rosenstiel 年份 | infobox 与奖项表均作 **1988**——勿写 1989 |
| Lomonosov 金质奖章 | **2016**——勿写 1989 诺奖年 |
| 学会年份 | AAAS Fellow 1988；NAS + 美国哲学学会均 **1990**——勿并成一年 |
| "第一次/唯一"类断言 | 禁止。"第一个放射性纯 tRNA 前体"仅以本人引语形式出现，须标注为其自述 |
| 引语红线 | 仅两处可作直接引语：①父母劳动价值观句（"It was from them I learned..."）②"tRNA 前体使我拿到耶鲁职位"句；其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102266 | ✅ |
| name_zh | 西德尼·奥尔特曼 | ✅ |
| name_en | Sidney Altman | ✅ |
| birth_date | 1939-05-07 | ✅ |
| death_date | 2022-04-05 | ✅ |
| nationality | United States（rank 0）/ Canada（rank 1） | ✅ 双国籍 |
| primary_occupation | molecular biologist | ✅ |
| field_of_work | molecular biology（person_field 细分见下表） | ✅ |
| has_biography | false（立传 Beamer 完成后置 1） | ✅ |

person_field 细分（rank 表）：

| field | rank | 说明 |
|---|---|---|
| molecular biology | 0 | 页面 Fields 主字段 |
| RNA catalysis | 1 | 核酶 / RNase P RNA 亚基 |
| biochemistry | 1 | metadata field_of_work 第二项 |
| tRNA processing | 2 | tRNA 前体成熟 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Leonard Lerman | 师→生（博士导师） | 科罗拉多大学，1967 博士；导师 1967 年转 Vanderbilt，随行短期研究 |
| colleague | Matthew Meselson | 无向 | 博士后在哈佛 Meselson 实验室研究 T4 DNA 内切酶 |
| colleague | John D. Smith | 无向 | MRC LMB 期间提供关键建议的同事 |
| co-honored | Thomas Cech | 无向 | 1989 诺贝尔化学奖共同得主（对方 yaml name_en 同用 Thomas Cech） |
| spouse | Ann M. Körner | 无向 | 1972 结婚，2018 离婚；Stephan Körner 之女 |
| advisor-student | Benjamin C. Stark | Altman→学生 | infobox Doctoral students；正文亦称 doctoral students include Ben Stark |
| advisor-student | Robin Reed | Altman→学生 | infobox Doctoral students 明载（metadata 无，以页面为准） |

> **禁入库名单**：metadata.json 中未出现、且 page.md 无载的任何其他师承/合作者；奖 infobox 中出现的机构与奖章不构成人际不入库。Vanderbilt/Harvard/MRC/Yale 仅为机构字段。

## 8. 奖项清单

- Nobel Prize in Chemistry（1989，与 Thomas Cech 共享）
- Rosenstiel Award（1988）
- Fellow of the American Academy of Arts and Sciences（1988）
- Member, National Academy of Sciences（1990）
- Member, American Philosophical Society（1990）
- Lomonosov Gold Medal（2016）
- Sterling Professor（耶鲁最高教职头衔）
- Honorary doctorate, McGill University
- 诺奖演讲：Enzymatic Cleavage of RNA by RNA（Nobel Lecture，页面外链标题，可引用标题名）

## 9. 机构清单

- 教育：MIT（1958–1960，物理学士）、Columbia University（1960–1961，物理研究生，未获学位离开）、University of Colorado Medical Center（生物物理博士，1967）
- 任职：Vanderbilt University（1967–，短期研究员）、Harvard University（Meselson 实验室博士后）、MRC Laboratory of Molecular Biology（Cambridge，RNase P 起点）、Yale University（1971 助理教授 → 1980 教授 → 1983–85 系主任 → 1985–89 Yale College 院长 → 1989-07-01 回任全职教授；Sterling Professor）

## 10. 终审清单

- [ ] 生卒 1939-05-07 / 2022-04-05，享年 82；出生地蒙特利尔、去世地 Rockleigh, New Jersey
- [ ] 1989 与 Cech 共享；"各自独立发现 RNA 催化性质"表述准确
- [ ] 博士导师 Leonard Lerman（科罗拉多 1967）；Meselson=博士后站点、John D. Smith=同事
- [ ] MIT 物理学士 1960 / 哥伦比亚未获学位 / 科罗拉多博士 1967 三段表述准确
- [ ] Ann M. Körner 1972–2018；子女 Daniel、Leah
- [ ] Rosenstiel 1988 / Lomonosov 2016 / AAAS 1988 / NAS 与 APS 1990 年份准确
- [ ] 引语仅两处直接引用，均可回溯 page.md 原文
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Sidney_Altman/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：Wikipedia "Altman in 2011" 肖像或装饰圆占位（如实标注）
- [ ] 国籍：封面顶部明示 加拿大 / 美国
- [ ] 引语核对：两处直接引语须在 page.md 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本文件由 chem-batch-21 执行生成；`chemist/generate_20th_century_list.py` 状态列由主控统一收尾，本批次不改动。
