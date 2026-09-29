# Jean-Marie Lehn（让-马里·莱恩）立传提示词

> qid=Q107690 · 1939-09-30 生于法国 Rosheim（阿尔萨斯）· 在世 · 法国化学家 · 诺贝尔化学奖（1987，与 Donald J. Cram、Charles J. Pedersen 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Jean-Marie_Lehn/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）。本页无现成肖像 URL——infobox 载 "Lehn in 2018" 照片但文件名未导出，执行时从 page.html 查 infobox 图文件名经 Commons Special:FilePath 下载（250px 改 500px）；404 则用装饰圆占位，插图可用 images.txt 的 `Supramolecular_Assembly_Lehn.jpg`（螺旋组装体，Angew 1996）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 超分子化学之父\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名、国籍、出生地、教育、博士导师、博士（论文题目）、核心领域、任职、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「分子识别 / 主客体」母题——大圆（宿主）内嵌小圆（客体）的包容意象。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jean-Marie Pierre Lehn（中文惯称：让-马里·莱恩）
- **生卒**：1939-09-30 生于法国阿尔萨斯 Bas-Rhin 省 Rosheim（在世，death_date 留白）
- **国籍**：France（法国）；阿尔萨斯德裔血统（Alsatian German descent）
- **身份**：化学家（chemist；超分子化学开创者）
- **家庭**：父 Pierre 为面包师，因热爱音乐后任市管风琴师；母 Marie；妻 Sylvie Lederer（1965 年结婚），两子 David 与 Mathias；无神论者
- **教育轨迹**：
  - 1950–1957 中学就读 Obernai（拉丁、希腊、德、英语 + 法国文学）
  - 1957 年 7 月获哲学业士（baccalauréat in philosophy）、同年 9 月又获自然科学业士
  - University of Strasbourg：本想学哲学，最终选了物理、化学与自然科学课程；听 Guy Ourisson 讲座后立志有机化学研究
- **导师**：Guy Ourisson（博士导师，斯特拉斯堡）
- **博士**：1963，论文 *Résonance magnétique nucléaire de triterpènes*（三萜的核磁共振）；期间负责实验室第一台 NMR 谱仪，首篇论文提出甾体衍生物质子 NMR 信号取代基诱导位移的加和性规则
- **研究领域**：超分子化学（supramolecular chemistry）、主客体化学、分子识别

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **面包师之子（1939）**：Rosheim 阿尔萨斯小城，父为面包师兼市管风琴师——音乐成为莱恩终生爱好，自述科学之外音乐是最大兴趣，职业科学家生涯中持续演奏管风琴。
2. **双业士（1957）**：同年先取哲学、再取自然科学业士——人文与科学的双重起点；入斯特拉斯堡大学后一度还想读哲学。
3. **Ourisson 实验室（1957–1963）**：从听众到博士生；掌管全实验室第一台 NMR 谱仪；首篇论文提出甾体质子 NMR 位移加和性规则；1963 以三萜 NMR 论文获博士。
4. **哈佛一年（1963–1966 间）**：博士毕业后赴 Robert Burns Woodward 的哈佛实验室工作一年，参与维生素 B12 全合成。
5. **回斯特拉斯堡（1966）**：任化学系 maître de conférences（助理教授），研究分子的物理性质——合成为展现特定性质而设计的化合物，以理解性质与结构之关联。
6. **穴醚问世（1968）**：合成出内部有腔穴、可容纳另一分子的笼状分子（cryptands）——有机化学使他得以按需定制笼子形状，只允许特定分子入住。
7. **超分子化学的命名**：穴醚成为其研究中心，进而定义了全新化学门类 "supramolecular chemistry"——不再研究分子内键，而研究分子间相互作用，以及后来所称的 "fragile objects"（胶束、聚合物、黏土）。
8. **传感器与分子生物学的桥**：这类识别机制开辟了化学传感器方向，也在分子生物学中扮演重要角色——例如药物 "know" 该摧毁哪个细胞、放过哪个细胞（Wikipedia 原文句式，可用转述）。
9. **法兰西公学院（1980）**：当选入主 prestigious 的 Collège de France 讲席。
10. **1987 诺贝尔化学奖**：与 Donald Cram、Charles Pedersen 共享，表彰其在穴醚合成上的工作；诺奖演讲 1987-12-08 *Supramolecular Chemistry – Scope and Perspectives Molecules – Supermolecules – Molecular Devices*。
11. **卡尔斯鲁厄（1998）**：在 Karlsruhe Institute of Technology 纳米技术研究所建立并领导研究组。
12. **多产与影响**：据其向诺贝尔基金会提供的信息（2006 年 1 月），课题组已发表 790 篇同行评审论文；2021 年 Google Scholar h-index 154（Scopus 137，946 篇）。
13. **科学与音乐的交响**：1987 年 Pierre Boulez 为其诺奖献上极短钢琴曲 *Fragment d'une ébauche*——分子识别与先锋音乐在同一人身上相遇。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#5B2A86` | 超分子化学的深邃与包容（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（穴醚 badgeCrypt） | `#7B3FA0` | 紫穴醚合成 / 笼状分子 |
| 分类色 2（分子识别 badgeRecog） | `#2E5A9E` | 蓝主客体 / 传感器 |
| 分类色 3（自组装 badgeSelfAsm） | `#1B7A43` | 绿螺旋组装体 / 折叠体 |
| 分类色 4（分子生物学 badgeBio） | `#C0395B` | 玫瑰药物识别 / 生命过程 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——大圆含小圆，呼应「宿主–客体」包容结构。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（清单预分配，勿复制 wav 文件，Makefile 引用源路径）
- **文件**：`music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`
- **风格**：戏剧性 / 有力 / 史诗感
- **匹配理由**：
  - "Last Hope" 匹配其开创全新化学门类的拓荒叙事——从穴醚到超分子化学，是从零定义一个领域的孤勇
  - "有力 / 史诗" 匹配 790 篇论文、h-index 154 的长程学术力量
  - 结尾在 Boulez 献曲的科学与音乐交汇处收束，音乐性呼应其管风琴人生
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 超分子化学之父 / Jean-Marie Lehn 1939– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/教育/博士导师/博士/领域/任职/家庭/荣誉）
03  莱恩的一生 — 高斯式时间线（10 节点：1939→1957→1963→1966→1968→1980→1987→1998→2021→在世）
04  早年：面包师与管风琴师之子 (1939–1957) — 表格「时间|事件|结果」（双业士）
05  斯特拉斯堡：从哲学到化学 (1957–1963) — 表格「时间|事件|结果」+ NMR 位移加和性规则
06  哈佛一年与回国任教 (1963–1966) — 表格「阶段|内容|结果」（Woodward / B12 / maître de conférences）
07  穴醚合成 (1968) — 表格「问题|方法|结果」+ 公式框：笼状分子容纳客体分子
08  超分子化学的诞生 — 表格「传统化学|超分子化学|意义」三列对照
09  分子识别与传感器 — 表格「问题|方法|结果」+ 公式框：宿主–客体识别
10  1987 诺贝尔化学奖 — 表格「得主|贡献|方向」（Pedersen 冠醚 / Cram 三维 / Lehn 穴醚）+ 获奖口径
11  法兰西公学院与卡尔斯鲁厄 — 高斯式「类别|代表|意义」表格（1980 Collège de France / 1998 KIT）
12  多产与传承 — 高斯 FFT 页式流程图或数据面板（790 篇 / h-index 154 / 学生 Jean-Pierre Sauvage 2016 诺奖）
13  科学与音乐 — 四分类遗产盒 + Boulez 献曲 *Fragment d'une ébauche*
14  结尾 — 「从分子到超分子，化学从此学会了识别。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1987 诺奖口径 | 与 Donald Cram、Charles Pedersen **三人共享**，理由按 Wikipedia 原文口径 "for his synthesis of cryptands"（穴醚合成）；勿写"独享"或"发明超分子化学获奖" |
| 获奖理由英文 | 官方精确措辞以 Nobel Foundation 页面为准；本地 page.md 只载 "for his synthesis of cryptands" 与 "for his works on cryptands" 两处口径，勿杜撰更长的 citation 全句 |
| 三人分工 | Pedersen 发现冠醚、Cram 拓展到三维分子、Lehn 穴醚与超分子化学——分工勿混（详见 Pedersen 页 "Associations with other chemists" 节口径） |
| 博士年份 | 1963（论文 *Résonance magnétique nucléaire de triterpènes*）；infobox 无单独毕业年份冲突 |
| 哈佛年份 | 页面仅载 "He obtained his Ph.D., and went to work for a year at Woodward's laboratory"——**未载具体年份**，勿写 "1963–1964" |
| 双业士顺序 | 1957-07 哲学业士在前、1957-09 自然科学业士在后——勿颠倒 |
| 哲学情节 | "本想学哲学"是 Wikipedia 明载（considered studying philosophy），可写；但勿扩写其哲学观点 |
| 妻子与子女 | 1965 娶 Sylvie Lederer，两子 David、Mathias——名字页面明载可写；子女入库另行裁定（仅 spouse 入库） |
| 无神论者 | 页面明载 "Lehn is an atheist"，如需提及仅作客观一句 |
| Sauvage 关系 | infobox Doctoral students 仅 **Jean-Pierre Sauvage** 一人（2016 诺奖）；Wikidata 其余学生名单本地页面无载——不予入库 |
| h-index | 154 为 Google Scholar 2021 年口径、137（946 documents）为 Scopus 口径——两个数字勿混用 |
| 790 篇论文 | 须注明：据莱恩本人向诺贝尔基金会提供的信息、截至 2006 年 1 月 |
| 中文引语 | page.md 无直接引语，全篇禁用引号原话，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q107690 | ✅ |
| name_zh | 让-马里·莱恩 | ✅ |
| name_en | Jean-Marie Lehn | ✅ |
| birth_date | 1939-09-30 | ✅ |
| death_date | （在世，留白） | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | supramolecular chemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 后置 1） | ✅ |

person_field 细分 rank 表：

| name_en | rank | name_zh |
|---|---|---|
| supramolecular chemistry | 0 | 超分子化学 |
| host–guest chemistry | 1 | 主客体化学 |
| organic chemistry | 2 | 有机化学 |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Guy Ourisson | 师→生（博士导师） | 斯特拉斯堡，1963 博士 |
| advisor-student | Jean-Pierre Sauvage | Lehn→学生 | infobox Doctoral students；2016 诺贝尔化学奖得主 |
| co-honored | Donald J. Cram | 无向 | 1987 诺贝尔化学奖共同得主 |
| co-honored | Charles J. Pedersen | 无向 | 1987 诺贝尔化学奖共同得主 |
| spouse | Sylvie Lederer | 无向 | 1965 结婚 |
| other | Robert Burns Woodward | 无向 | 博士后在 Woodward 哈佛实验室一年，参与维生素 B12 合成 |

> metadata.json-only 一律不入库并在下方禁入库名单注明。本页 metadata 另载 educated_at 有 University of Toronto Mississauga 等，正文无载的机构关系不入库；子女 David/Mathias 仅正文家族叙述、无独立人物条目信息，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1987，与 Cram、Pedersen 共享）
- CNRS Bronze Medal（1963）、Silver Medal（1972）、Gold Medal（1981）
- 美国国家科学院国际院士（1980）；American Academy of Arts and Sciences 院士（1980）
- Humboldt Prize（1983）
- 荣誉军团骑士（1983）→ 军官（1988）→ 指挥官（1996）→ 大军官（2014）
- Ordre national du Mérite 军官（1993；骑士 1976）；Palmes académiques 骑士（1989）
- Pour le Mérite for Sciences and Arts（1990）
- 皇家学会外籍院士 ForMemRS（1993）
- American Philosophical Society 院士（1987）
- Davy Medal（1997）
- Austrian Cross of Honour for Science and Art, 1st class（2001）；罗马尼亚文化功绩大军官（2004）
- Gutenberg Lecture Award（2006）；ISA Medal for Science（2006）
- 联邦德国功绩勋章指挥官十字（2009）；日本旭日金银星章（2019）
- 60+ 荣誉博士学位（希伯来大学 1984 至布拉格化工大学 2019；含中国多所高校名誉教授：中科大 1998、东南大学 1998、上海交大 2003、南京大学 2003、北大 2005、浙大 2007、陕师大 2007、厦门大学 2012、吉大 2013、山西大学 2013 等）
- Onsager Medal；Karl Ziegler Prize；Lavoisier Medal；Centenary Prize；Paracelsus Prize；Robert Robinson Award；Sir Derek Barton Gold Medal；Marie Curie Medal（metadata 载，年份以官方页面为准）

## 9. 机构清单

- 教育：Obernai 中学（1950–1957）→ University of Strasbourg（PhD 1963）
- 博士后：Harvard University，Robert Burns Woodward 实验室（一年，维生素 B12 合成）
- 任职：University of Strasbourg 化学系 maître de conférences（1966–）；Collège de France 讲席教授（1980–）；Karlsruhe Institute of Technology 纳米技术研究所研究组（1998–）
- 委员：Reliance Innovation Council（Reliance Industries，印度）

## 10. 终审清单

- [ ] 生卒 1939-09-30 / 在世留白，出生地 Rosheim（阿尔萨斯）
- [ ] 1987 三人共享（Cram、Pedersen）表述准确；获奖理由只写 "synthesis of cryptands" 口径
- [ ] 博士导师 Guy Ourisson、博士 1963、论文题目正确
- [ ] 双业士 1957（7 月哲学、9 月自然科学）顺序正确
- [ ] 哈佛年份留白处理；1968 穴醚、1980 法兰西公学院、1998 KIT 年份准确
- [ ] 790 篇注明"截至 2006-01、本人向诺奖基金会提供"；h-index 双口径不混
- [ ] 引语全部间接转述（page.md 无直接引语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Jean-Marie_Lehn/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：infobox "Lehn in 2018" 文件名经 page.html 查得后经 Commons 下载；404 则装饰圆占位
- [ ] 国籍：封面顶部明示法国
- [ ] 引语核对：全篇无引号原话（间接转述）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/prompt_manifest.json` chem-batch-20 · Jean-Marie Lehn（1987，BGM Last Hope，主色 #5B2A86）。
> **开始执行。每完成一步向主控汇报。**
