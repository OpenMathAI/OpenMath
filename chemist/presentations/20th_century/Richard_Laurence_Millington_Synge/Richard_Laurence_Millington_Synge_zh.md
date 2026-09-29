# Richard Laurence Millington Synge（理查德·劳伦斯·米林顿·辛格）立传提示词

> qid=Q48979 · 1914-10-28 – 1994-08-18 · 英国生物化学家 · 20 世纪 · 诺贝尔化学奖（1952，与 Archer Martin 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Richard_Laurence_Millington_Synge/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景，是本次撰写的核心版式语言。
> ⚠️ 数据源提示：本页 page.md 较短（infobox + Life/Personal life 两节），**一切以实载为准，页面无载的事实一律禁写**（尤其博士信息、获奖年表细节）。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠️ 本地 images.txt 为空、page.md 无肖像图——**用装饰圆占位**，图注写「肖像暂缺·装饰占位」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{tint}\enspace 分配色谱的共创者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（Winchester / Trinity College）、配偶、核心领域、荣誉。**本页无博士导师字段——信息网格不设师承项**。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「两相分离」母题——圆点像液-液两相中各归其位的分子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——逆流液-液萃取与分配系数（Rf 值）是全篇视觉锚点；FRS 候选引文长句可入原文框。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Laurence Millington Synge（中文惯称：理查德·劳伦斯·米林顿·辛格；FRS FRSE FRIC FRSC）
- **生卒**：1914-10-28 生于 West Kirby（⚠️ 正文载 West Kirby，infobox 载 Liverpool——两说并存，以正文 West Kirby 为口径并注记）→ 1994-08-18 逝于 Norwich，享年 79
- **国籍**：United Kingdom（英国；英格兰）
- **身份**：生物化学家（biochemist, university teacher, chemist）——分配色谱法共同发明人
- **家庭**：父 Lawrence Millington Synge 为利物浦股票经纪人，母 Katherine C. Swan；1943 年娶 Ann Davies Stephen（1916–1997）——心理学家 Karin Stephen 与精神分析学家 Adrian Stephen 之女；Ann 的姐姐 Judith（1918–1972）嫁给纪录片艺术家/摄影师 Nigel Henderson
- **教育轨迹**：The Old Hall（Wellington, Shropshire）→ Winchester College → Trinity College, Cambridge（攻读化学）
- **导师**：**页面无载**——禁写
- **研究领域**：生物化学（biochemistry）——分配色谱、纸色谱、gramicidin 短肽、蛋白质组成与结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **股票经纪人之子（1914）**：一战爆发之秋生于默西河畔 West Kirby——父亲是利物浦股票经纪人，他却在实验室找到了自己的行当。
2. **Winchester 与 Trinity**：The Old Hall → Winchester College → 剑桥 Trinity College 攻读化学——古典公学教育与剑桥化学训练。
3. **一生只做研究的履历**：职业生涯全在研究机构——Leeds 羊毛工业研究协会（1941–1943）→ Lister 医学研究所（伦敦，1943–1948）→ Rowett 研究所（阿伯丁，1948–1967）→ 食品研究所（Norwich，1967–1976）。
4. **利兹：与 Martin 的相遇（1941–1943）**：在 Wool Industries Research Association 与 Archer Martin 合作发展**分配色谱法**——让相似化学品的混合物在两液相间分离，就此革命性地改变了分析化学。
5. **逆流萃取的起点**：FRS 候选引文载明——他「最先展示了用逆流液-液萃取分离 N-乙酰氨基酸的可能性」（counter-current liquid-liquid extraction），这正是分配色谱的理论前身。
6. **gramicidin 短肽（1942–1948）**：研究 gramicidin 组的肽——这项工作后来被 **Frederick Sanger** 用于测定胰岛素结构——方法学间接催生了蛋白质测序时代的到来。
7. **FRS 候选引文（1950-03）**：当选皇家学会会士，引文盛赞其与 Martin「在蛋白质组成与结构问题上的卓著成功，特别是羊毛角蛋白」以及「gramicidin 的组成与结构研究生动体现了他们两人技术上的伟大进展」——原文整句可入原文框。
8. **1952 诺贝尔化学奖**：与 Archer Martin 共享，理由是**发明分配色谱法**——方法学诺奖：给全世界的化学家一双新的眼睛。
9. **FRSE（1963）**：当选爱丁堡皇家学会会士，推荐人为 Magnus Pyke、Andrew Phillipson、David Cuthbertson 爵士与 John Andrew Crichton。
10. **Norwich 岁月（1967–1976）**：食品研究所；1968–1984 兼任东英吉利大学（UEA）生物科学荣誉教授；1977 获 UEA 荣誉理学博士（ScD）、1980 获乌普萨拉大学荣誉博士。
11. **四会会士**：FRS、FRSE、FRIC、FRSC——皇家学会、爱丁堡皇家学会、皇家化学研究院、皇家化学学会一体加身；另任皇家化学会化学信息组司库数年。
12. **斯蒂芬家的姻缘（1943）**：娶 Ann Davies Stephen——布鲁姆斯伯里圈子的家族（Karin/Adrian Stephen）与实验室的联结。
13. **谢幕（1994）**：1994-08-18 逝于 Norwich，享年 79——他留下的分配色谱法已成为从氨基酸分析到 HPLC 的整个技术谱系的源头。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（赭红 ochre-red） | `#A63A2B` | 液相色带在纸面晕开的赭红（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分配色谱 badgePC） | `#2E5A9E` | 蓝两相分配 / 逆流萃取 |
| 分类色 2（短肽研究 badgePep） | `#1B7A43` | 绿 gramicidin / 肽化学 |
| 分类色 3（荣誉·会士 badgeFRS） | `#B8860B` | 金 FRS/FRSE 引文 |
| 分类色 4（机构足迹 badgeInst） | `#6B4E9E` | 紫 Leeds→London→Aberdeen→Norwich 四站 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「两相分离」——液-液体系中各归其位的分子。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（文件：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`；**不要复制 wav 文件**）
- **风格**：电影感 / 戏剧性 / 恢弘 drone
- **匹配理由**：
  - "Empire Collapse" 的宏大质地匹配方法学革命——色谱法终结了「分离靠运气」的旧时代
  - "电影感" 匹配其漂移的职业生涯地图——利兹→伦敦→阿伯丁→诺里奇，四站皆为纯研究机构
  - 低音 drone 与「辛格甘居幕后、方法传世」的气质相合——诺奖颁给工具的缔造者
- **时长**：以文件实际时长为准（须 > 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 分配色谱的共创者 / R.L.M. Synge 1914–1994 + 四色 badge + 装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/配偶/领域/荣誉）
03  辛格的一生 — Sanger 式时间线（10 节点：1914→1936→1941→1943→1948→1950→1952→1963→1967→1994）
04  West Kirby 与剑桥 (1914–1941) — 表格「时间|事件|结果」
05  利兹：与 Martin 共创分配色谱 (1941–1943) — 表格「问题|方法|结果」+ 公式框：分配系数 K = Cs/Cm · Rf 值
06  逆流液-液萃取 — 表格「问题|方法|结果」+ 公式框：N-乙酰氨基酸分离示意（FRS 引文对应工作）
07  gramicidin 短肽 (1942–1948) — 表格「对象|方法|意义」+ 原文框：为 Sanger 胰岛素结构测定所用
08  FRS 与候选引文 (1950) — 表格「维度|内容|意义」+ 原文框：candidature citation 英文整句
09  1952 诺贝尔化学奖 — 表格「理由|口径|意义」（与 Martin 共享「发明分配色谱法」）
10  研究机构的一生 — 表格「机构|城市|年份」四站足迹
11  荣誉与四会会士 — Sanger 式「类别|代表|意义」表格（FRS 1950 / Nobel 1952 / Wetherill 1959 / FRSE 1963 / UEA·Uppsala 荣誉博士）
12  家庭与布鲁姆斯伯里 — 表格「人物|关系|结果」（Ann Davies Stephen / Karin·Adrian Stephen——姻亲仅叙述不入库）
13  遗产：从分配色谱到 HPLC — 四分类遗产盒 + 公式框：色谱技术谱系（分配→纸→气液→HPLC）
14  结尾 — 「他把分离变成了科学，后人才能看清生命的分子。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由 | page.md 口径 "shared the 1952 Nobel Prize in Chemistry for the invention of partition chromatography"（与 Archer Martin 共享）——勿写独享，勿泛化为「发明色谱法」 |
| 出生地口径 | 正文 "born in West Kirby"、infobox "Liverpool"——**两说并存**：叙事以 West Kirby 为口径，身份信息页可加小字注「infobox 作 Liverpool」 |
| 博士/导师 | page.md **无载**博士信息与导师——禁写；身份信息页不设师承字段 |
| gramicidin | page.md 原文 "peptides of the protein group gramicidin"——写「gramicidin 组的短肽」，勿写「蛋白质 gramicidin」或「抗生素 gramicidin S」等引申 |
| 与 Sanger 关系 | 是「其短肽研究**被 Sanger 用于**测定胰岛素结构」——对 Sanger 而言是方法/材料来源，**勿写成师生**；入库用 influence 类型 |
| FRS 引文 | 候选引文（candidature citation）是皇家学会官方文本、page.md 整段实载——可整句引用原文；此为「官方评语」非个人引语，勿当作 Synge 自述 |
| 家庭 | 妻 Ann Davies Stephen（1916–1997）；岳父母 Karin/Adrian Stephen 与连襟 Nigel Henderson 仅作背景叙述——**姻亲不入库** |
| Wetherill Medal | 1959 年获奖（infobox Awards 行）——与 Martin 两篇页面口径一致，勿改 |
| 引语 | 除 FRS 引文外无直接引语——中文引号内禁编造「原话」；Nobel lecture 标题 "Applications of Partition Chromatography" 可用作文献信息 |
| 肖像 | images.txt 为空——装饰圆占位，图注「肖像暂缺」 |
| 同名区分 | 本篇全篇用 Richard Laurence Millington Synge；对手方用 Archer Martin（frontmatter 名，与 Martin 篇 yaml 一致，防分裂 stub） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48979 | ✅ |
| name_zh | 理查德·劳伦斯·米林顿·辛格 | ✅ |
| name_en | Richard Laurence Millington Synge | ✅ |
| birth_date | 1914-10-28 | ✅ |
| death_date | 1994-08-18 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / partition chromatography / paper chromatography / peptide chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**共同得主 / 影响关系 / 配偶**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Archer Martin | 无向 | 1952 诺贝尔化学奖共同得主（发明分配色谱法，Leeds 时期合作发展） |
| influence | Frederick Sanger | 影响→被影响 | 其 gramicidin 短肽研究被 Sanger 用于测定胰岛素结构；库内 #1122 |
| spouse | Ann Davies Stephen | 配偶 | 1943 年结婚；Karin Stephen 与 Adrian Stephen 之女 |

> **禁入库名单**（page.md 明载但判定为噪声/非入库关系）：Lawrence Millington Synge、Katherine C. Swan（父母，亲属不入库）；Magnus Pyke、Andrew Phillipson、David Cuthbertson、John Andrew Crichton（FRSE 推荐人，礼仪性关系）；Karin Stephen、Adrian Stephen、Nigel Henderson、Judith Stephen（姻亲，不入库）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1952，与 Archer Martin 共享）
- Fellow of the Royal Society（1950-03 当选）
- John Price Wetherill Medal（1959）
- Fellow of the Royal Society of Edinburgh（1963）；FRIC、FRSC（infobox 头衔）
- Honorary ScD, University of East Anglia（1977）
- Honorary doctorate, Uppsala University（1980）
- Honorary Fellow of the Royal Society Te Apārangi（infobox award_received，年份页面无载——勿写具体年份）

## 9. 机构清单

- 教育：The Old Hall（Wellington, Shropshire）；Winchester College；Trinity College, Cambridge
- 任职：Wool Industries Research Association, Leeds（1941–1943）；Lister Institute for Preventive Medicine, London（1943–1948）；Rowett Research Institute, Aberdeen（1948–1967）；Food Research Institute, Norwich（1967–1976）；University of East Anglia 荣誉教授（1968–1984）；皇家化学会化学信息组司库（数年）

## 10. 终审清单

- [ ] 生卒 1914-10-28 / 1994-08-18，享年 79，出生地 West Kirby（注记 infobox Liverpool）、去世地 Norwich
- [ ] 1952 与 Martin 共享、理由「发明分配色谱法」表述准确
- [ ] gramicidin 短肽与 Sanger 的关系方向正确（影响非师生）
- [ ] FRS 引文整句可溯源；无编造个人引语
- [ ] 四站机构年份准确；荣誉年份（1950/1959/1963/1977/1980）无误
- [ ] 姻亲与 FRSE 推荐人不入库；禁入库名单执行
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误、溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 page.md 逐页对照 Beamer tex 全部事实（页面短，重点核对无外溢）
- [ ] 头像：确认装饰圆占位 + 图注「肖像暂缺」
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：FRS 引文须在 page.md 原文找到，无其他编造引号内容
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（本页无师承字段，其余对齐）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：由 chem-batch-09 执行；`chemist/generate_20th_century_list.py` 由主控统一收尾，本篇不改动。
