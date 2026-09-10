# Hermann Emil Fischer（赫尔曼·埃米尔·费歇尔）立传提示词

> qid=Q70554 · 1852-10-09 – 1919-07-15 · 德国化学家（有机化学/生物化学） · 20 世纪 · 诺贝尔化学奖（1902，独享）
> 官方获奖理由（总名单措辞）：表彰他因在糖类和嘌呤合成方面的研究所作出的杰出贡献
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Hermann_Emil_Fischer/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像执行阶段下载，见 §11 Review-1 指引；page.md infobox 照片为 c. 1895 照）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 糖与嘌呤的建筑师\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox（page.md），不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「糖环 / 投影式 / 分子建筑」母题——圆点阵列暗示 Fischer projection 中纵横交错的碳链骨架。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——D-(+)-葡萄糖全合成、Fischer projection、肽键合成方程本身就是最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Hermann Emil Louis Fischer（中文惯称：赫尔曼·埃米尔·费歇尔；FRS FRSE FCS）——**终生不用第一个名字，一生以 Emil Fischer 行世**
- **生卒**：1852-10-09 生于普鲁士 Euskirchen（科隆附近）→ 1919-07-15 逝于柏林（魏玛共和国），享年 66
- **国籍**：German Empire / Germany（德国）
- **身份**：化学家 / 有机化学家 / 生物化学家（1902 年诺贝尔化学奖得主）
- **家庭**：商人 Laurenz Fischer 之子，母 Julie Poensgen；毕业后想读自然科学，被父亲强令先进入家族企业，直到父亲确认他不适合经商。1888 年娶 Agnes Gerlach；七年后（1895）妻子去世，留下三个儿子——幼二子死于第一次世界大战军役，长子 Hermann Otto Laurenz Fischer 成为有机化学家。新教徒（Protestant）
- **教育轨迹**：
  - 1871 入波恩大学（University of Bonn）
  - 1872 转学斯特拉斯堡大学（University of Strasbourg）
  - 1874 年在 Adolf von Baeyer 指导下获博士学位（博士论文研究酞类 phthaleins；infobox 博士导师另列 Friedrich August Kekulé）
- **师承**：Adolf von Baeyer（博士导师，斯特拉斯堡；1875 年随其赴慕尼黑）；infobox 另列 Kekulé
- **研究领域**：化学——糖类合成、嘌呤化学、肼类化合物、蛋白质/多肽、酶（锁钥模型）、染料化学

## 2. 核心叙事亮点（用于 Slide 4–13，约 13 条）

1. **商人之子的化学转身（1852–1871）**：Euskirchen 商人之家；被父亲按进家族企业，直到父亲确认"不适合经商"——然后才是波恩、斯特拉斯堡。
2. **斯特拉斯堡与苯肼（1874–1875）**：留 Baeyer 身边任有机实验室助手；1875 年发现并命名肼类（hydrazines），包括偏二甲肼（unsymmetrical dimethylhydrazine——多年后在太空竞赛中大放异彩）与苯肼（phenylhydrazine）。
3. **苯肼：打开糖化学的钥匙**：苯肼与醛/酮生成结晶固体；糖的苯腙（phenylhydrazones）与腙类（osazones）高度结晶、易于鉴定——糖类与嘌呤合成工作（1902 诺奖）由此起航。
4. **三苯甲烷染料（1878–1879）**：与表兄弟 Otto Fischer 合作发表论文，确立品红（fuchsine/magenta）染料是三苯甲烷（triphenylmethane）的衍生物。
5. **嘌呤化学（1881–1882）**：在 Baeyer 开辟的基础上大步推进——确立尿酸、黄嘌呤、咖啡因（**首次合成**）、可可碱等化合物的分子式；嘌呤本体分离后又制备一系列衍生物，部分因潜在治疗应用而申请专利。
6. **糖类合成与 16 种立体异构（1884–）**：糖的 osazone 鉴定法；**全合成 D-(+)-葡萄糖**；推导 16 种立体异构葡萄糖的分子式并制备多种异构体——反过来确证了 Le Bel–Van 't Hoff 不对称碳原子法则。
7. **Fischer projection**：表示不对称碳原子的一种符号画法——沿用至今的糖化学通用语言。
8. **锁钥模型（酶学）**：提出底物结合的 "lock and key"（锁钥）机制假说——酶学的奠基性思想。
9. **酯化与命名反应群**：发现 Fischer esterification（infobox 级成就）；以他命名：Fischer indole synthesis、Fischer oxazole synthesis、Fischer peptide synthesis、Fischer–Speier esterification、Fischer glycosidation、Kiliani–Fischer synthesis 等。
10. **第一个巴比妥类药物（1904）**：与医生 Josef von Mering 合作推出首个巴比妥类镇静剂 barbital。
11. **蛋白质与多肽（1899–1907）**：把复杂白蛋白分解为氨基酸，再重组——1901 年合成第一个游离二肽（甘氨酸-甘氨酸）；1906 年组里已制备约 65 种不同链长与组成的肽；1907 年出版 *Untersuchungen über Aminosauren, Polypeptides und Proteine*；三年后肽总数超过 100，最长为 18 肽（15 甘氨酸 + 3 亮氨酸），通过缩二脲试验、盐沉淀、蛋白酶酶切等蛋白质标准检验。
12. **1902 诺贝尔化学奖**：独享；官方理由 "in recognition of the extraordinary services he has rendered by his work on sugar and purine syntheses"（表彰他因在糖类和嘌呤合成方面的研究所作出的杰出贡献）；1902-12-12 诺贝尔演讲《嘌呤与糖群的合成》。
13. **学术遗产**：1897 年提议创建国际原子量委员会；ForMemRS（1899）；柏林建有 Emil Fischer 纪念碑。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深咖啡棕 deepcocoa） | `#4E342E` | 糖与焦糖的经典有机化学气质——厚重、手作式的分子建筑（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（糖类化学 badgeSugar） | `#2E7D32` | 绿葡萄糖全合成 / osazone / Fischer projection |
| 分类色 2（嘌呤化学 badgePurine） | `#5E35B1` | 紫咖啡因首次合成 / 尿酸 / 黄嘌呤 |
| 分类色 3（蛋白质与多肽 badgePeptide） | `#0277BD` | 蓝二肽 Gly-Gly / 18 肽 / 氨基酸重组 |
| 分类色 4（酶与药物 badgeEnzyme） | `#C0395B` | 玫瑰锁钥模型 / barbital |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **选择理由**：深咖啡棕取自「糖 / 焦糖」的直觉意象——糖类合成是其诺奖理由的第一关键词；又与深藏青（Sanger #1E3A5F）、深孔雀蓝（van 't Hoff）等已用主色明确区分。
- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「糖环与投影式的骨架节点」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（本地文件 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`）
- **风格**：强推进 / 紧张 / 难题攻克
- **匹配理由**：
  - "难题攻克" 匹配其贡献本质——在糖与嘌呤这两片前人未至的化学荒原上系统攻坚：16 种立体异构葡萄糖的全谱推演、咖啡因首次合成
  - "强推进" 匹配其方法论——把有机合成从零散反应升级为可规划的系统工程（合成 → 投影 → 构型确证），并由此跨入生物化学（酶、蛋白质）
  - 与既有选曲不重复：New Lands 已由 Rutherford 选用，Expedition 已由 van 't Hoff 选用，Sanger 用 Timeless
- **注意**：**不要复制 wav 文件**——wav 复制在执行立传阶段进行（`cp` 到本目录后 `make video` 自动检测）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 糖与嘌呤的建筑师 / Hermann Emil Fischer 1852–1919 + 四色 badge + 右上头像 + 国籍行（德国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  费歇尔的一生 — 高斯式时间线（10 节点：1852 Euskirchen → 1871 波恩 → 1874 博士（Baeyer）→ 1875 苯肼 → 1881 嘌呤分子式 → 1882 埃尔朗根教授 → 1892 接掌柏林 → 1902 诺贝尔化学奖 → 1907 Faraday 讲席奖 → 1919 逝于柏林）
04  早年：商人之子的化学转身 (1852–1871) — 表格「时间|事件|结果」
05  波恩—斯特拉斯堡—拜耳门下 (1871–1875) — 表格「时间|事件|结果」+ 公式框：苯肼与糖的 osazone 反应
06  染料与吲哚 (1878–1886) — 表格「问题|合作|结果」（三苯甲烷染料与表兄弟 Otto Fischer；吲哚合成）
07  嘌呤化学 (1881–1900) — 表格「问题|方法|结果」+ 公式框：咖啡因 / 尿酸 / 黄嘌呤分子式
08  糖类合成 (1884–) — 表格「问题|方法|结果」+ 公式框：D-(+)-葡萄糖全合成 / 16 种立体异构
09  Fischer projection 与立体化学确证 — 表格「问题|方法|结果」+ 公式框：不对称碳投影式 / Le Bel–Van 't Hoff rule 的实验确证
10  锁钥模型与巴比妥 (1894–1904) — 表格「问题|方法|结果」+ 公式框：lock and key / barbital（与 von Mering）
11  蛋白质与多肽 (1899–1907) — 表格「问题|方法|结果」+ 公式框：第一个游离二肽 Gly-Gly（1901）/ 18 肽
12  荣誉 — 高斯式「类别|代表|意义」表格（Nobel 1902 / Davy 1890 / Faraday 1907 / ForMemRS 1899 / Elliott Cresson 1913 + 会员清单）
13  遗产 — 四分类遗产盒 + 公式框：以他命名的反应群（indole/projection/glycosidation/Kiliani–Fischer…）
14  结尾 — 金句页（建议从其工作本质提炼：「他把糖与嘌呤，一砖一瓦砌成了有机化学的殿堂。」——编者提炼结语，非其原话，不得加引号呈现为引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 同名区分（最重要） | **Hans Fischer**（1930 年化学诺奖，血红素）是另一人，仅出现在 metadata.json `doctoral_student` 列表中，page.md 正文无载其师承——Beamer 中勿把 Hans Fischer 的事迹与本篇混写；**Franz Emil Fischer**（Fischer–Tropsch process，马克斯·普朗克煤炭研究所所长）与本人**无关**（page.md 明文 unrelated）；**Edmund Fischer** 无载——一律勿写 |
| 本名与称呼 | 出生名 Hermann Emil Louis Fischer，**终生不用第一个名字**，世称 Emil Fischer——勿写"笔名/化名"，也不要把 Hermann 当常用名 |
| 诺奖理由 | 官方措辞：糖类和嘌呤合成（"in recognition of the extraordinary services he has rendered by his work on sugar and purine syntheses"）——勿写成"因糖化学"或"因酶锁钥模型获奖"；Fischer projection 与锁钥模型**均不在**获奖理由内 |
| 任职年份冲突 | 正文：1882 任埃尔朗根教授、**1885** 任维尔茨堡教授、1892 接掌柏林（接替 von Hofmann）；infobox Institutions 却写 Erlangen 1881–88、Würzburg 1888–92——**以 page.md 正文为准**（1882 / 1885 / 1892），并在 §5 记录冲突 |
| 博士导师 | 正文仅 Baeyer（1874，斯特拉斯堡，酞类研究）；infobox Doctoral advisor 另列 **Friedrich August Kekulé**，metadata.json 只列 Baeyer——写"博士导师 Adolf von Baeyer（infobox 另列 Kekulé）"，勿凭空增删 |
| 咖啡因首次合成 | "achieving the first synthesis" 专指 **caffeine**（1881–1882 嘌呤工作）——勿推广成"首次合成嘌呤全家族" |
| 16 种立体异构葡萄糖 | 他是**推导分子式并制备数种异构体**、从而确证 Le Bel–Van 't Hoff rule——勿写"合成了全部 16 种"，也勿写成"推翻"该法则 |
| UDMH 与太空竞赛 | 1875 年发现偏二甲肼，page.md 说它"很久之后在太空竞选中变得重要"——是后世回望，**勿写成"为航天而发明"** |
| barbital 与 veronal | 正文：与 Josef von Mering 于 **1904** 推出首个巴比妥类镇静剂 **barbital**；veronal 为 Further reading 文献中的商品名——正文统一用 barbital，勿混写年份 1905 |
| 二肽与肽的数字 | 第一个游离二肽 Gly-Gly = **1901**；1906 年约 **65** 种肽；1907 年出版论文集；三年后总数**超过 100**，最长 18 肽（15 Gly + 3 Leu）——数字勿张冠李戴 |
| 家庭悲剧 | 妻 Agnes Gerlach 1888 年结婚、七年后去世；幼二子死于**一战军役**；长子 Hermann Otto Laurenz Fischer 成为有机化学家——勿把长子与 Hans Fischer 混淆 |
| 引语纪律 | **page.md 全文无任何 Fischer 本人直接引语**——中文引号内不得出现任何"费歇尔说过"的原话；诺贝尔演讲标题《Syntheses in the Purine and Sugar Group》（1902-12-12）只能作为事实引用，不得虚构其内容引文 |
| 学生名单分歧 | page.md 正文 infobox：Alfred Stock、Otto Diels、Otto Ruff、Walter A. Jacobs、Ludwig Knorr、Oskar Piloty、Julius Tafel；metadata.json：Otto Diels、Hans Fischer、Otto Heinrich Warburg、Hans von Euler-Chelpin、Carl Harries、Max Bergmann、Oskar Piloty——两份名单**仅重叠 Diels 与 Piloty**；入库口径见 §7，Beamer 学生页优先用正文名单 |
| 表兄弟 Otto Fischer | 合作发表 1878/1879 三苯甲烷染料论文的是其**表兄弟（cousin）Otto Fischer**——勿写"兄弟"或"另一位化学家 Fischer" |
| 命名反应归属 | Fischer–Speier esterification 是与 Speier 共同命名；Kiliani–Fischer synthesis 是与 Kiliani 并列——勿写成单人命名 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q70554 | ✅ |
| name_zh | 赫尔曼·埃米尔·费歇尔 | ✅ |
| name_en | Hermann Emil Fischer | ✅ |
| birth_date | 1852-10-09 | ✅ |
| death_date | 1919-07-15 | ✅ |
| nationality | German Empire / Germany | ✅ |
| primary_occupation | chemist（metadata 另含 biochemist / organic chemist 带 rank） | ✅ |
| field_of_work | chemistry（metadata；person_field 细分：sugar chemistry / purine chemistry / peptide & protein chemistry / enzymology，带 rank） | ✅ |
| has_biography | 1（执行立传后置 1） | 🔲 待置 |

## 7. 社会关系入库清单

**师长 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Adolf von Baeyer | 师→生（博士导师） | 1874 年斯特拉斯堡大学博士（酞类研究）；1875 随其赴慕尼黑 |
| advisor-student | Friedrich August Kekulé | 师→生（infobox 博士导师之一） | metadata 未载，正文未提；入库时 note 注明"仅 infobox 有载" |
| colleague | Otto Fischer | 无向 | 表兄弟；1878/1879 合著三苯甲烷染料论文 |
| colleague | Josef von Mering | 无向 | 1904 合作推出首个巴比妥类镇静剂 barbital |

**门生（Fischer → 学生，源自 page.md 正文 infobox Doctoral students）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Diels | Fischer → 学生 | 正文 infobox 与 metadata 均载 |
| advisor-student | Oskar Piloty | Fischer → 学生 | 正文 infobox 与 metadata 均载 |
| advisor-student | Alfred Stock | Fischer → 学生 | 仅正文 infobox 载 |
| advisor-student | Otto Ruff | Fischer → 学生 | 仅正文 infobox 载 |
| advisor-student | Walter A. Jacobs | Fischer → 学生 | 仅正文 infobox 载 |
| advisor-student | Ludwig Knorr | Fischer → 学生 | 仅正文 infobox 载 |
| advisor-student | Julius Tafel | Fischer → 学生 | 仅正文 infobox 载 |

> metadata.json `doctoral_student` 另含 Hans Fischer、Otto Heinrich Warburg、Hans von Euler-Chelpin、Carl Harries、Max Bergmann 五人，但 **page.md 正文无载**——如按 metadata 口径一并入库，note 必须注明"仅 Wikidata/metadata 有载"；且 **Hans Fischer 为 1930 年诺奖另一人，入库时姓名字段务必核对 qid，防止同名合并**。Beamer 学生页只用正文名单。

## 8. 奖项清单

- Nobel Prize in Chemistry（1902，独享）
- Davy Medal，Royal Society（1890）
- Faraday Lectureship Prize（1907）
- Elliott Cresson Medal（1913）
- Foreign Member of the Royal Society，ForMemRS（1899）
- International Member of the US National Academy of Sciences（1904）
- International Honorary Member of the American Academy of Arts and Sciences（1908）
- International Member of the American Philosophical Society（1909）
- Helmholtz Medal / Cothenius Medal / Baly Medal / Pour le Mérite（含 Pour le Mérite for Sciences and Arts order）/ Bavarian Maximilian Order for Science and Art / honorary member of the Physics Association (Frankfurt am Main)（metadata 载，年份无）
- FRSE（皇家爱丁堡学会会士）、FCS（化学学会会士）——姓名后缀有载

## 9. 机构清单

- 教育：University of Bonn（1871）、University of Strasbourg（1872–，PhD 1874）
- 任职：University of Strasbourg（有机实验室助手，1874/1875 起）；Ludwig-Maximilians-Universität München（1875–81：1875 助手、1878 Privatdozent、1879 分析化学副教授）；University of Erlangen（1882 教授，正文）；University of Würzburg（1885 教授，正文 / infobox 1888–92，见 §5 冲突）；Friedrich Wilhelm University of Berlin（1892–1919，接替 von Hofmann）
- 命名与纪念：Fischer indole synthesis、Fischer projection、Fischer oxazole synthesis、Fischer peptide synthesis、Fischer phenylhydrazine and oxazone reaction、Fischer–Speier esterification、Fischer glycosidation、Kiliani–Fischer synthesis；International Atomic Weights Commission（1897 年他提议创建）；柏林 Emil Fischer 纪念碑
- 注意：Fischer–Tropsch process 以 **Franz Emil Fischer** 命名，与本篇人物无关

## 10. 终审清单

- [ ] 生卒 1852-10-09 / 1919-07-15，享年 66，出生地 Euskirchen（普鲁士）、去世地柏林
- [ ] 1902 诺奖**独享**；获奖理由用总名单措辞「表彰他因在糖类和嘌呤合成方面的研究所作出的杰出贡献」
- [ ] 与 Hans Fischer（1930 得主）、Franz Emil Fischer（Fischer–Tropsch）、Otto Fischer（表兄弟）全部区分无误
- [ ] 任职年份以正文为准：慕尼黑 1875–81 / 埃尔朗根 1882 / 维尔茨堡 1885 / 柏林 1892–1919，并在文中不出现自相矛盾的 infobox 年份
- [ ] 咖啡因首次合成（1881–1882）；16 种异构葡萄糖为"推导分子式并制备数种"；确证 Le Bel–Van 't Hoff rule
- [ ] 二肽 Gly-Gly 1901；1906 约 65 肽；18 肽 = 15 Gly + 3 Leu
- [ ] barbital 1904 与 Josef von Mering；锁钥模型为假说提出、非诺奖理由
- [ ] 学生页只用正文 infobox 名单；Hans Fischer 同名风险已核查
- [ ] 引语纪律：全篇无 Fischer 直接引语（page.md 无载）；无中文引号内虚构"原话"
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Hermann_Emil_Fischer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 仅载柏林纪念碑照片 `https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Hermann_Emil_Fischer_berlin.jpg/250px-Hermann_Emil_Fischer_berlin.jpg`（雕像照，改 `250px`→`500px` 可用但非本人肖像）；infobox 实际肖像为 "Fischer c. 1895" 照片——优先走 **Commons Special:FilePath / Wikipedia REST API page/summary 查 infobox 原图名** 检索 1895 年照，404 则回退纪念碑照，再 404 则装饰圆占位（须核对图注：纪念碑照必须标注"柏林纪念碑"而非肖像）
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：全篇不得出现加引号的 Fischer 原话（正文无载）；获奖理由英文原文可引
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；德语人名（Baeyer / Würzburg / Euskirchen）断行不断字
- [ ] 与数学家侧（高斯）及化学家侧既有格式对齐（Sanger 版、van 't Hoff 版）

---

> **名单状态**：本提示词已完成；Beamer 立传**待执行**。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（立传完成后由主流程同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
