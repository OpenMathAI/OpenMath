# Roger Y. Tsien（钱永健）立传提示词

> qid=Q200470 · 1952-02-01 生于纽约 – 2016-08-24 逝于俄勒冈州尤金 · 美国生物化学家 · 21 世纪 · 诺贝尔化学奖（2008，与 Shimomura / Chalfie 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Roger_Y._Tsien/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本篇的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用 `images/` 目录本地文件，若缺省用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{palette}\enspace 给细胞装上彩虹调色盘\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Roger Yonchien Tsien / 錢永健）、国籍、出生地/去世地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「彩虹荧光蛋白调色盘」母题——多色圆点象征 Tsien 实验室工程化的红/黄/青荧光蛋白。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 S65T 突变光谱特性、钙成像指示剂原理。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Roger Yonchien Tsien（錢永健；中文惯称：钱永健）
- **生卒**：1952-02-01 生于纽约市 → 2016-08-24 逝于俄勒冈州尤金（Eugene，Oregon），享年 64（死因未公开；曾抗癌成功、2013 年曾中风；事发于自行车道，page.md 口径）
- **国籍**：United States（美国）
- **身份**：美国生物化学家；UC San Diego 药理学教授、化学与生物化学教授；Howard Hughes Medical Institute（HHMI）研究员
- **家庭**：杭州钱氏后裔（自称吴越王钱镠第 34 代孙）；父 Hsue-Chu Tsien（钱学榘，MIT 与上海交大毕业，机械工程师，以全班第一毕业），母 Yi-Ying Li（李懿穎，护士，北京人）；兄 Richard W. Tsien 为纽约大学神经生物学家，弟 Louis Tsien 为软件工程师；妻子 Wendy Globe。★ 钱学森（Tsien Hsue-shen）是**其父的堂兄**——即钱永健为钱学森堂侄（page.md 明载，仅客观一句，家族叙事克制）
- **教育轨迹**：
  - Livingston High School（新泽西州）
  - 16 岁以"金属与硫氰酸盐结合"项目获全美 Westinghouse Science Talent Search 首奖
  - Harvard College（National Merit Scholarship；三年级入选 Phi Beta Kappa；1972 以最优等 summa cum laude 获化学与物理 BA）
  - Marshall Scholarship 赴剑桥大学生理学实验室，寄宿 Churchill College；1977 获生理学 PhD（论文 *The design and use of organic chemical tools in cellular physiology*）
- **导师**：Richard Adrian（博士导师，正式挂名；化学系 Jeremy Sanders 协助指导，另有 Andy Holmes、Gerry Smith）
- **研究领域**：生物化学——荧光蛋白工程、钙成像（calcium imaging）、荧光指示剂、分子工程

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **地下室化学家（1952–1968）**：幼年哮喘常年宅家，在自家地下室做化学实验；16 岁获 Westinghouse Science Talent Search 全美首奖。
2. **哈佛最优等（1968–1972）**：化学与物理双修，summa cum laude；室友、后来成为经济学家的 Herman Quirmbach 评价 "It's probably not an exaggeration to say he's the smartest person I ever met"（page.md 明载）。
3. **马歇尔学者赴剑桥（1972–1977）**：Churchill College；博士期间研制有机化学工具用于细胞生理学，正式导师 Richard Adrian、化学系 Jeremy Sanders 协助。
4. **剑桥研究员（1977–1981）**：Gonville and Caius College research fellow。
5. **伯克利教职（1982–1989）**：UC Berkeley faculty。
6. **UCSD 与 HHMI（1989–）**：药理学 + 化学与生物化学双聘教授、HHMI 研究员，直至去世。
7. **钙成像先驱（1985–1989）**：fura-2 广泛用于追踪细胞内钙浓度；indo-1（1985）与 fluo-3（1989）同为 Tsien 组开发；另有镁/锌/铜/铁/铅/镉/铝/镍/钴/汞等多种离子荧光指示剂；calmodulin 传感蛋白 Cameleon。
8. **1994：GFP 发光机理**：证明 GFP 色基由自身化学反应形成——需要氧但**不需要其他蛋白辅助**（自催化，page.md 明载）。
9. **1995：S65T 单点突变（Nature）**：大幅改善荧光强度与光稳定性，激发峰移至 488 nm（发射峰保持 509 nm），与常用 FITC 设备完美匹配——GFP 实用性的决定性一步。
10. **彩虹调色盘（1994–2002）**：遗传改造+结构调整造出黄/青/蓝荧光蛋白；2000–2002 制出单体化 DsRed（红/粉/橙），"彩虹的所有颜色"从此可标记活体大分子网络。
11. **超越水母（2009–2016）**：2009 从细菌光敏色素改造出红外荧光蛋白 IFP（需外源色基胆绿素）；2016 从蓝细菌藻胆蛋白进化出 smURFP（不需要氧、不产过氧化氢，亮度可与 eGFP 相比）。
12. **下一代测序的奠基专利（1990）**：1990-10-26 申请"可移除 3' 阻断基团的逐碱基测序 + DNA 阵列"专利——Illumina 将此概念与 DNA 克隆结合用于其新一代测序仪（page.md 明载）。
13. **发明家与企业家**：截至 2010 持有或共同持有约 100 项专利；1996 共同创办 Aurora Biosciences（1997 上市，2001 被 Vertex 收购）；1999 科学共同创办 Senomyx；2016-08-24 骑行途中去世；妻 Wendy 悼词 "He was ever the adventurer, the pathfinder, the free and soaring spirit"（page.md 明载）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（胭脂深红 deepcrimson） | `#7A1E28` | 荧光蛋白调色盘中的"红"——DsRed 与 smURFP 的母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（钙成像 badgeCa） | `#2C5F8A` | 蓝 fura-2 / indo-1 / fluo-3 |
| 分类色 2（GFP 工程 badgeGFPeng） | `#1B7A43` | 绿 S65T / 彩虹突变体 |
| 分类色 3（红色荧光 badgeRed） | `#A63A2B` | 橘红 DsRed / mRFP / "水果"系列 |
| 分类色 4（测序与发明 badgeInv） | `#5B4A2F` | 褐测序专利 / Aurora / Senomyx |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「彩虹荧光调色盘」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（文件 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`；不要复制 wav 文件，Makefile 直接引用）
- **风格**：宏大 / 戏剧性 / 悲怆尾声
- **匹配理由**：
  - "宏大" 匹配其多线开花的一生——钙成像、GFP 工程、测序专利、创业，一人打通化学与生物技术
  - "悲怆" 呼应 64 岁猝然离世的遗憾与 Rainbow 调色盘的绚烂对照
  - "Collapse/Drone" 的低回气质贴合通篇的追忆基调（2008 三人共享中唯一已故者之外的绚烂人生收束）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 给细胞装上彩虹调色盘 / Roger Y. Tsien 1952–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/领域/机构/荣誉）
03  钱永健的一生 — Sanger 式时间线（10 节点：1952→1968→1972→1977→1982→1989→1995→2004→2008→2016）
04  地下室化学家 (1952–1972) — 表格「时间|事件|结果」
05  剑桥岁月 (1972–1981) — 表格「时间|事件|结果」（Richard Adrian / Sanders 协助）
06  钙成像先驱 (1982–1989) — 表格「对象|方法|结果」+ 公式框：fura-2 细胞内钙指示
07  GFP 机理与 S65T (1994–1995) — 表格「问题|方法|结果」+ 公式框：色基自催化需氧 / 488→509 nm
08  彩虹调色盘 (1994–2002) — 表格「问题|方法|结果」+ 公式框：DsRed 共轭延伸红移
09  2008 诺贝尔化学奖 — 公式框：获奖理由原句 + 三人分工（发现 / 表达 / 发展）
10  测序专利与创业 (1990–2001) — 高斯式流程图（专利 → Aurora → Vertex 收购 → Senomyx）
11  荣誉长廊 — Sanger 式「类别|代表|意义」表格（Wolf Medicine 2004 / Gairdner 1995 / Heineken 2002 / ForMemRS 2006 itemize）
12  家族与传承 — 表格「人物|关系|领域」（Hsue-Chu / Richard / Wendy；学生 Lin、Miyawaki、Ting）
13  遗产：荧光照亮生物学 — 四分类遗产盒 + 公式框：smURFP 亮度参数
14  结尾 — 「他用彩虹标记生命，让分子在活细胞中无处遁形。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2008 获奖 | **三人共享**（Shimomura / Chalfie / Tsien）；本页引 Nobel 官方口径 "the green fluorescent protein: discovery, expression and development"；Tsien 的分工是 **改造与发展**（机理阐释 + 彩虹突变体）——勿写"发现 GFP" |
| 博士导师 | 正文 infobox Doctoral advisor 为 **Richard Adrian**（正式挂名，生理学系）；frontmatter/metadata 写 Jeremy Sanders 系化学系**协助指导**——以 infobox 为准，Sanders 不作博士导师入库 |
| S65T | 1995 年 *Nature* 报道，激发峰 488 nm、发射峰 509 nm——年份与波长勿错 |
| 钱学森 | page.md 明载"钱学森是钱永健父亲的堂兄"——只写这一句客观事实（堂侄关系），**不展开家族史叙事，不建数据库关系** |
| 兄弟 | 兄 **Richard W. Tsien**（NYU 神经生物学家）、弟 Louis（软件工程师）——Richard 勿与本篇主角混淆 |
| 死因 | 2016-08-24 逝于 Eugene 自行车道，**具体死因未公开**；曾抗癌、2013 中风——勿编造死因 |
| 去世年份 | 2016（享年 64）；smURFP 是 2016 年其团队成果——勿写身后发表 |
| 专利数 | "约 100 项"须注明：截至 2010 年（持有或共同持有） |
| 引语 | 仅可用 page.md 原载三处：获奖理由句、Quirmbach 评价、"I'm doomed by heredity to do this kind of work"、Wendy 悼词——其余一律间接转述 |
| 在世字段 | 已故：1952-02-01 / 2016-08-24，享年 64 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q200470 | ✅ |
| name_zh | 钱永健 | ✅ |
| name_en | Roger Y. Tsien | ✅ |
| birth_date | 1952-02-01 | ✅ |
| death_date | 2016-08-24 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | biochemistry | 生物化学 |
| 1 | fluorescent protein engineering | 荧光蛋白工程 |
| 2 | calcium imaging | 钙成像 |
| 3 | cell biology | 细胞生物学 |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Adrian | 师→生（博士导师） | 剑桥生理学系正式博士导师，1977 获博士 |
| other | Jeremy Sanders | 无向 | 化学系协助指导博士课题（infobox 博士导师为 Richard Adrian） |
| advisor-student | Michael Z. Lin | Tsien → 学生 | 正文 infobox Doctoral students 明载 |
| advisor-student | Atsushi Miyawaki | Tsien → 学生 | page.md 明载 former trainee（学位类型页面未载） |
| advisor-student | Alice Y. Ting | Tsien → 学生 | page.md 明载 former trainee（学位类型页面未载） |
| co-honored | Osamu Shimomura | 无向 | 2008 诺贝尔化学奖共同得主 |
| co-honored | Martin Chalfie | 无向 | 2008 诺贝尔化学奖共同得主（Rosenstiel 2006 与 E.B. Wilson 2008 亦共享） |
| spouse | Wendy Globe | 无向 | 妻子 |
| sibling | Richard W. Tsien | 无向 | 兄，纽约大学神经生物学家 |
| sibling | Louis Tsien | 无向 | 弟，软件工程师 |
| parent-child | Hsue-Chu Tsien | 父→钱永健 | 机械工程师，MIT 与上海交大毕业 |
| parent-child | Yi-Ying Li | 母→钱永健 | 护士，北京人 |

> 禁入库：钱学森（父之堂兄，page.md 明载但属远亲、关系类型字典无对应，家族叙事克制）；Roberto Malinow（metadata.json `doctoral_student` 有载而 page.md 正文无，**不予入库**）；Herman Quirmbach（室友非合作关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2008，与 Shimomura / Chalfie 三人共享）
- Wolf Prize in Medicine（2004）；Keio Medical Science Prize（2004）
- Gairdner Foundation International Award（1995）；Artois-Baillet Latour Health Prize（1995）
- Dr H.P. Heineken Prize for Biochemistry and Biophysics（2002）；Max Delbrück Medal（2002）
- ACS Award for Creative Invention（2002）；Pearse Prize（2000）
- Rosenstiel Award（2006，与 Chalfie 共享）；E. B. Wilson Medal（2008）
- ForMemRS 英国皇家学会外籍会士（2006）；NAS 院士（1998）；American Academy of Arts and Sciences（1998）；EMBO（2005）
- National First Prize, Westinghouse Science Talent Search（1968）；Marshall Scholarship（1972）
- Roger Tsien Day（2009-02-18，圣迭戈市宣布）；Academia Sinica 名誉院士（2008）
- 荣誉博士：Katholieke Universiteit Leuven（1995）、University of Hong Kong（2009）、Chinese University of Hong Kong（2009）
- 其余讲座讲席与奖项详见 page.md Honors 列表（逐条可溯源）

## 9. 机构清单

- 教育：Livingston High School；Harvard College（BA 1972 最优等）；Churchill College, Cambridge（PhD 1977 生理学）
- 任职：Gonville and Caius College, Cambridge research fellow（1977–1981）→ UC Berkeley（1982–1989）→ UC San Diego（1989–2016，药理学 + 化学与生物化学教授、HHMI 研究员）
- 创业：Aurora Biosciences（1996 共同创办，2001 被 Vertex 收购）；Senomyx（1999 科学共同创办）

## 10. 终审清单

- [x] 生卒 1952-02-01 / 2016-08-24，享年 64；去世地 Eugene, Oregon；死因未公开表述准确
- [x] 2008 三人共享；获奖理由按本页官方口径（discovery, expression and development）；发现/表达/发展分工准确
- [x] 博士导师以 infobox Richard Adrian 为准；Sanders 标注"协助指导"other 类型
- [x] 钱学森堂侄仅一句客观带过、不入库
- [x] S65T（1995, 488/509 nm）、fura-2/indo-1/fluo-3 年份准确
- [x] 引语仅 page.md 原载四处
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Roger_Y._Tsien/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 目录照片就位（缺省装饰圆占位）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：引语必须在 page.md 原文找到（四处原载）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
