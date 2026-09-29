# John Fenn（约翰·芬恩）立传提示词

> qid=Q106738 · 1917-06-15 – 2010-12-10 · 美国分析化学家 · 21 世纪 · 诺贝尔化学奖（2002，与 Tanaka 共享半奖·质谱电离；另一半 Wüthrich·NMR）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/John_Fenn_chemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框。本地 images.txt **无单人肖像**（仅 ESI 仪器照片 Fenn_ESI_Instrument.jpg 与 Berea College 荣誉墙照片 Honor_of_John_B._Fenn.jpg）——封面用**装饰圆占位**（主色渐变 + 姓名缩写 JF）；仪器照片作 ESI 页插图、荣誉墙作诺奖页插图（图注写明 Berea College 荣誉陈列）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace\ 电喷雾之父\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、本名 John Bennett Fenn、国籍、出生地/去世地、教育（Berea AB / Yale PhD 1940）、博士导师（Gosta Akerlof）、任职（Princeton / Yale / VCU）、核心领域（电喷雾电离 / 分子束 / 质谱）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「喷雾 / 荷电液滴」母题——由大到小蒸发收缩的圆点序列，暗示 ESI 液滴脱溶剂与电荷富集过程。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——如 ESI 原理框（大气压电喷雾 → 加热氮气脱溶剂 → 真空蒸发 → 多电荷态 → m/z 降低易测）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：John Bennett Fenn（中文惯称：约翰·芬恩；infobox 表头 John B. Fenn）
- **生卒**：1917-06-15 生于美国纽约市 → 2010-12-10 逝于弗吉尼亚州 Richmond，享年 93——**恰逢获诺奖整 8 年的同一天**
- **国籍**：United States（美国）
- **身份**：分析化学家（analytical chemist；获奖时任职 Virginia Commonwealth University）
- **家庭**：研究生第二学年末娶 Margaret Wilson，育两女一子；1992 年 Margaret 在新西兰车祸去世；再娶 Frederica Mullen；身后有三子女、七个孙辈、十一个曾孙辈
- **教育轨迹**：
  - 童年随家迁 Hackensack, New Jersey；大萧条前夕父亲曾在 Fokker 飞机公司短暂任制图员——林德伯格的「圣路易斯精神号」曾停放公司机库，10 岁的 Fenn 坐进过驾驶舱
  - 大萧条家道中落，迁肯塔基州 Berea（姑妈 Helen Dingman 在 Berea College 任教相助）
  - 15 岁修完高中课程，又多读一年才上大学
  - Berea College（AB；暑期赴 University of Iowa 补有机化学、Purdue 补物理化学）
  - Yale University（PhD 1940；Harvard 化学教授 Henry Bent 建议他补数学课，他自觉数学欠缺是终身短板）
- **导师**：Gosta Akerlof（Yale 物理化学博士导师）
- **博士论文**：1940，《The thermodynamics of hydrochloric acid in methanol-water mixtures》——45 页仅 3 页正文
- **研究领域**：分析化学——电喷雾电离（ESI）、分子束、喷气推进相关物理化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **大萧条中的少年（1917–1930s）**：纽约出生、Hackensack 长大；10 岁坐进「圣路易斯精神号」驾驶舱假装飞行——航空时代的第一颗种子。
2. **Berea 的救济与转机**：迁居肯塔基 Berea，靠姑妈 Helen Dingman（Berea College 教师）安家；15 岁读完高中。
3. **Yale 博士（1937–1940）**：师从 Gosta Akerlof 研究盐酸-甲醇水混合物热力学；45 页论文仅 3 页正文。
4. **工业界十年（1940–1952）**：Monsanto 磷酸盐部生产多氯联苯（PCBs）——「我们几乎在里面洗澡」（对 PCBs 无害性的天真认知，间接转述）；1943 与同事 James Mullen 一同辞职 → Sharples Chemicals → 1945 加入 Mullen 的创业公司 Experiment, Inc。
5. **迟到的第一篇论文（1949）**：研究生毕业 10 年后才发表第一篇论文（与 Mullen 合作）——学术界罕见的履历。
6. **Project SQUID（1952–1967）**：任普林斯顿大学 Project SQUID 主任（海军研究办公室资助的喷气推进研究计划）；开启超声速原子与分子束源研究——至今广泛用于化学物理。
7. **重返 Yale（1967–1987）**：化学与工程系联合聘任，Mason Laboratory 开展研究。
8. **强制退休（1987）**：70 岁触 Yale 强制退休线，成为荣休教授——失去大部分实验室与研究生。
9. **电喷雾电离 ESI**：半退休状态下发表电喷雾电离研究——液样在大气压下电喷雾、加热氮气脱溶剂、真空区蒸发富集电荷、大分子带多电荷后 m/z 骤降易测——**让质谱分析大分子成为可能**。
10. **蛋白质组学的「临门一脚」**：ESI 研究因蛋白质组学兴起获得「踢了一脚」的推动（间接转述）；2001 年逾 1700 篇蛋白质组学论文发表，多数用 ESI。
11. **与 Yale 的专利诉讼**：1989 年向校方淡化 ESI 潜力、自行申请专利并把许可卖给自家持股公司 Analytica of Branford；1996 年 Yale 反诉后成讼；2005 年联邦法官 Christopher Droney 判 Fenn 败诉——Yale 获 54.5 万美元特许费加 50 万美元律师费；判决书批语（原文）"Dr. Fenn only obtained the patent through fraud, civil theft, and breach of fiduciary duty."；部分同事与旧生致信 Yale Daily News 表达不满。
12. **2002 诺贝尔化学奖**：与 Koichi Tanaka 共享半奖（质谱电离方法），另一半 Kurt Wüthrich（NMR 溶液结构）；官方理由 "for the development of methods for identification and structure analyses of biological macromolecules."；诺奖演说题为 "Electrospray Wings for Molecular Elephants"；闻讯自述「像中了彩票，我还在发抖」（间接转述 "It's like winning the lottery, I'm still in shock."）。
13. **VCU 晚年与身后**：与 Yale 缘尽后赴里士满 Virginia Commonwealth University 化学系任分析化学教授，直到去世仍保持化学+工程双聘；80 多岁仍泡实验室——「我喜欢和年轻人混在一起」（间接转述）；2010-12-10 逝世，距获奖整整 8 年。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（墨蓝 inkblue） | `#123C5B` | 分析化学的冷静与精确（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（电喷雾 badgeESI） | `#2E5A9E` | 蓝电喷雾电离 / 多电荷态 |
| 分类色 2（分子束 badgeBeam） | `#1B7A43` | 绿分子束 / Project SQUID |
| 分类色 3（诺贝尔 badgeNobel） | `#D97B29` | 琥珀 2002 获奖理由 |
| 分类色 4（争议 badgeSuit） | `#C0395B` | 玫瑰专利诉讼 / ERIAD 争议 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落、由大渐小），呼应「喷雾液滴蒸发→电荷富集」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（`music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`；**不要复制 wav 文件，Makefile 直接引用该路径**）
- **风格**：怀旧 / 温情 / 大器晚成
- **匹配理由**：
  - "怀旧" 匹配其人生弧线——85 岁才戴上诺奖桂冠，回望横跨大萧条、喷气时代与蛋白质组学革命的一生
  - "温情" 匹配其晚年自述——「喜欢和年轻人混在一起」的赤子之心
  - "大器晚成" 匹配叙事节奏——毕业 10 年才发第一篇论文、半退休才做出 ESI，时间是这篇传记的主角
- **时长核对**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 电喷雾之父 / John Fenn 1917–2010 + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名 John Bennett Fenn/国籍/教育/博士导师/机构/领域/荣誉）
03  Fenn 的一生 — 时间线（10 节点：1917→Berea→1940 Yale PhD→Monsanto/Experiment Inc→1949 首篇论文→1952 SQUID→1967 Yale→1987 强制退休/ESI→2002 诺奖→2010 逝世）
04  大萧条与 Berea (1917–1937) — 表格「时间|事件|结果」
05  Yale 博士与工业十年 (1937–1952) — 表格「阶段|师从/东家|收获」（Akerlof/Monsanto/Experiment Inc）
06  Project SQUID 与分子束 (1952–1967) — 表格「问题|方法|结果」
07  Yale 岁月与强制退休 (1967–1987) — 表格「阶段|职务|转折」
08  电喷雾电离 ESI — 表格「问题|方法|结果」+ 公式框：ESI 原理链（插图 Fenn_ESI_Instrument）
09  蛋白质组学与大分子的质谱时代 — 表格「契机|发展|影响」（2001 年 1700+ 篇论文）
10  与 Yale 的专利诉讼 — 表格「时间线|焦点|结果」（1989→1996→2005 败诉）
11  ERIAD 争议与 Lidija Gall — 表格「时间|事实|评述」（1981 苏联谱图/1983 到访/1984 发表/Fenn 1984 未引用/2002 诺委会承认）
12  2002 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框：官方英文获奖理由（插图 Berea 荣誉墙）
13  VCU 晚年与遗产 — 「类别|代表|意义」表格（百篇论文/一本书/仪器入藏 Science History Institute）
14  结尾 — 「大器晚成：他让大象长上了翅膀。」（诺奖演说题目 Electrospray Wings for Molecular Elephants 的意象，须注明为演说标题）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | 官方英文 "for the development of methods for identification and structure analyses of biological macromolecules."（三人共享的整体表述）；Fenn 与 Tanaka 平分**半奖**（质谱电离），Wüthrich 得另一半（NMR）——勿写「Fenn/Tanaka/Wüthrich 三人均分」 |
| 份额表述 | Fenn 的贡献聚焦 ESI 电离技术、Tanaka 是软激光解吸、Wüthrich 是 NMR——三者方向勿混 |
| 诉讼叙事 | 2005 年法院认定 Fenn 败诉（误报潜力、自行专利、违反诚信义务）——**须如实呈现判决与批评意见**，同时呈现同事致信 Yale Daily News 的反弹，勿单方面洗白或丑化 |
| ERIAD 争议 | Lidija Gall 组 1981 年已记录肽/蛋白谱图、1983 年 Fenn 到访并有 "fruitful discussions"、1984-04 Gall 先发表 5 个月、Fenn 1984 论文未引用——**按 page.md 实载四点如实写**；Gall 2002 获诺委会承认、2022 获 Thomson Medal |
| 引语 | 页面实载引语：'practically bathed in the stuff'（PCBs）、'a kick in the pants'（蛋白质组学）、'fruitful discussions' / 'very promising'（Gall 之访）、'I like to mingle and exchange with the young people. It gets me out from underfoot at home.'、'It's like winning the lottery, I'm still in shock.'、法官批语——引号内须逐字；其余一律间接转述 |
| 卒日巧合 | 2010-12-10 恰为获奖 8 周年同日——页面明载（exactly 8 years to the day）可写 |
| 名字规范 | infobox John B. Fenn / 全名 John Bennett Fenn / 词条名 John Fenn (chemist)——**入库名用 John Fenn**（与 manifest 及跨批次对手方引用一致），行文首次出现可写全名 |
| 配偶区分 | 两任妻子 Margaret Wilson（1992 新西兰车祸去世）与 Frederica Mullen——勿混；分别以 spouse 入库 |
| Henry Bent | 仅建议补数学课的 Harvard 教授——**非导师**，禁以 advisor 入库 |
| Tanaka 份额 | Tanaka 与 Fenn「共享半奖」——勿写成 Tanaka 三分之一 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106738 | ✅ |
| name_zh | 约翰·芬恩 | ✅ |
| name_en | John Fenn | ✅（新建记录；全名 John Bennett Fenn 见行文） |
| birth_date | 1917-06-15 | ✅ |
| death_date | 2010-12-10 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | electrospray ionization | 电喷雾电离 |
| 1 | mass spectrometry | 质谱法 |
| 2 | molecular beams | 分子束 |
| 3 | analytical chemistry | 分析化学 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gosta Akerlof | 师→生（博士导师） | Yale 物理化学博士导师（1940） |
| spouse | Margaret Wilson | 无向 | 研究生第二学年末结婚，两女一子；1992 年新西兰车祸去世 |
| spouse | Frederica Mullen | 无向 | 再婚妻子；2010 年身后在世 |
| colleague | James Mullen | 无向 | Monsanto 同事，1943 一同辞职；后共事于 Experiment, Inc（Fenn 首篇 1949 论文合作者） |
| co-honored | Koichi Tanaka | 无向 | 2002 诺贝尔化学奖共同得主（共享半奖·质谱电离方法） |
| co-honored | Kurt Wüthrich | 无向 | 2002 诺贝尔化学奖共同得主（另一半·NMR 溶液结构分析） |
| controversy | Lidija Gall | 无向 | ERIAD 方法优先权争议：1983 到访交流、1984 年 Gall 先发表而 Fenn 论文未引用；2002 年获诺委会承认 |

> **禁入库名单**：Henry Bent（仅建议补课，非导师）；姑妈 Helen Dingman（家庭救助，非学术关系）；法官 Christopher Droney（诉讼当事人角色，非学术关系）；Motoharu Seiki 等为 Tanaka 篇合作关系（非 Fenn 关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2002，与 Tanaka 共享半奖；另一半 Wüthrich）
- Honorary President, Sixth International Symposium on Molecular Beams（1977）
- Alexander von Humboldt Foundation U.S. Senior Scientist Award（1982；infobox 记 Humboldt Prize）
- First Fellow of the International Molecular Beam Symposium（1985）
- American Society for Mass Spectrometry Award for Distinguished Contributions in Mass Spectrometry（1992）
- Thomson Medal（2000，International Society of Mass Spectrometry）
- ACS Award for Advancements in Chemical Instrumentation（2000）
- Fellow of the American Academy of Arts and Sciences（2000）
- ABRF Award（2002，Association of Biomolecular Resource Facilities）
- Wilbur Cross Medal（2003，Yale Graduate School Alumni Association 最高荣誉）
- Member of the National Academy of Sciences（2003）

## 9. 机构清单

- 教育：Berea College（AB，暑期 Iowa/Purdue 补课）→ Yale University（PhD 1940，Gosta Akerlof 组）
- 工业界：Monsanto（磷酸盐部/PCBs，1940–1943）→ Sharples Chemicals（戊基氯衍生物）→ Experiment, Inc（1945，Mullen 创业公司）
- 学界：Princeton University（Project SQUID 主任，1952–1967）→ Yale University（化学+工程联合聘任，1967–1987；1987 强制退休为荣休教授）→ Virginia Commonwealth University（分析化学教授，化学+工程双聘直至去世）
- 纪念：Berea College 荣誉陈列诺奖；ESI 原型仪器入藏费城 Science History Institute Museum

## 10. 终审清单

- [ ] 生卒 1917-06-15 / 2010-12-10，享年 93，卒日=获奖 8 周年同日
- [ ] 2002 表述：Fenn 与 Tanaka 共享半奖（质谱电离）、Wüthrich 另一半（NMR）；官方英文获奖理由逐字
- [ ] 诉讼叙事双向呈现（判决原文 + 同事反弹信）；ERIAD 四点实载如实
- [ ] 引语逐字对照 page.md；其余转述不加引号
- [ ] 两任妻子 Margaret Wilson / Frederica Mullen 不混
- [ ] 入库名 John Fenn；对手方名 Koichi Tanaka / Kurt Wüthrich / Lidija Gall / James Mullen / Gosta Akerlof（规范名）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Fenn_chemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；仪器照片与 Berea 荣誉墙仅作插图、图注准确
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全部引语在 page.md 原文找到（含法官批语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2002 批次（Tanaka / Wüthrich 篇）的份额与理由表述交叉一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
