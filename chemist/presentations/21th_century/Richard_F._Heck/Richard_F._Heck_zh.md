# Richard F. Heck（理查德·F·赫克）立传提示词

> qid=Q106471 · 1931-08-15 – 2015-10-09 · 美国化学家 · 21 世纪 · 诺贝尔化学奖（2010，与 Ei-ichi Negishi、Akira Suzuki 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Richard_F._Heck/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次执行的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `images/`；infobox 2010 年照片可用；若无真实肖像则用装饰圆占位，图注注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 钯催化偶联的开路人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「钯催化循环 / C–C 键」母题——离散圆点暗示氧化加成-迁移插入-还原消除的循环节点。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），Heck 反应通式（芳基卤 + 烯烃 → 取代烯烃，Pd 催化）即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Frederick Heck（中文惯称：理查德·F·赫克）
- **生卒**：1931-08-15 生于美国马萨诸塞州 Springfield → 2015-10-09 逝于菲律宾马尼拉公立医院，享年 84
- **国籍**：United States（美国）
- **身份**：化学家；特拉华大学化学与生物化学系 Willis F. Harrington 荣休教授
- **家庭**：八岁随家迁洛杉矶；娶 Socorro Nardo-Heck，退休后夫妇移居菲律宾 Quezon City；妻子 2012 年先逝；**无子女**
- **教育轨迹**：UCLA（BS 1952 → PhD 1954，芳基磺酸酯的取代与重排化学）
- **导师**：Saul Winstein（博士导师）；博士后随 Vladimir Prelog 在瑞士 ETH Zurich（Prelog 为 1975 诺贝尔化学奖得主）
- **博士论文**：*Methoxyl and aryl groups in substitution and rearrangement*（1955；infobox 系年，正文作 1954 获 PhD——见 §5）
- **研究领域**：有机化学——有机钯化学、钯催化交叉偶联（Heck 反应）、有机合成方法学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **斯普林菲尔德到洛杉矶（1931–1939）**：生于马萨诸塞州 Springfield，八岁西迁洛杉矶——与 UCLA 的一生羁绊自此开始。
2. **UCLA 双学位（1952/1954）**：本科与博士一气呵成，师从物理有机名家 Saul Winstein 研究芳基磺酸酯。
3. **ETH 博士后（Prelog）**：随 1975 年诺奖得主 Vladimir Prelog 在苏黎世做博士后，后回 UCLA——欧洲学脉的注入。
4. **Hercules 工业实验室（1956）**：加入特拉华州 Wilmington 的 Hercules 公司，最初做高分子化学——产业实验室出身的方法学大师。
5. **转向有机金属（1950s 末–1960s）**：与 David S. Breslow 合作有机钴化学，从此迷上有机金属。
6. **Heck 反应（1960s 末）**：研究芳基汞试剂与烯烃在钯催化下的偶联，成果以 **七篇连发、唯一作者** 的 JACS 论文系列发表——一人一系。
7. **工业价值**：止痛药萘普生（naproxen）即用 Heck 反应工业制备（page.md 明载）。
8. **Mizoroki 的独立改进（1970s 初）**：Tsutomu Mizoroki 独立报道用毒性更低的芳基卤代烃作偶联对象——该反应史称 Mizoroki–Heck 反应。
9. **特拉华教授（1971）**：任特拉华大学化学与生物化学系教授，继续把该反应打磨成有机合成的强力方法。
10. **从 45 页到 377 页**：1982 年他能在 *Organic Reactions* 一章 45 页写尽全部已知实例；到 2002 年仅分子内 Heck 反应一章就达 377 页——指数级扩散的明证。
11. **延伸贡献**：首个完整表征 π-烯丙基金属配合物；首个阐明烯烃氢甲酰化机理；芳基卤-炔偶联被 Sonogashira 加铜改进后用于荧光染料标记 DNA 碱基——自动化 DNA 测序与人类基因组计划的化学底层。
12. **2010 诺贝尔化学奖**：与 Ei-ichi Negishi、Akira Suzuki 共享 "for palladium-catalyzed cross couplings in organic synthesis"（2010-10-06 瑞典皇家科学院宣布）。
13. **晚年与谢幕**：1989 退休（Willis F. Harrington 荣休教授）；2011 获 Glenn T. Seaborg Medal；2012 受聘马尼拉 De La Salle University 兼职教授；2015-10-09 在马尼拉公立医院去世，享年 84。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深红 darkcrimson） | `#7E1E23` | 钯催化循环的深红基调 / 工业化学的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Heck 反应 badgeHeck） | `#2E5A9E` | 蓝芳基卤 × 烯烃偶联 |
| 分类色 2（机理与配合物 badgeMech） | `#1B7A43` | 绿 π-烯丙基配合物 / 氢甲酰化 |
| 分类色 3（工业与药物 badgeInd） | `#D97B29` | 琥珀萘普生 / DNA 测序染料 |
| 分类色 4（偶联家族 badgeFam） | `#C0395B` | 玫瑰 Suzuki–Miyaura / Stille / Kumada / Negishi |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「催化循环」节点式排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（文件 `music_audio/inspiring-electronic/03-qtNSLNUd1VE-...Falling Apart.wav`；不要复制 wav 文件）
- **风格**：情感化 / 低回而坚韧 / 后摇滚式铺陈
- **匹配理由**：
  - 低回坚韧的气质匹配其叙事弧线——工业实验室里孤独开路、被学界冷落多年、晚年方获诺奖
  - "Falling Apart" 的张力匹配 C–C 键的断裂与重构——偶联化学本质即"拆开再接上"
  - 结尾的推进感匹配 2010 年迟来的加冕与合成化学世界的全面采纳
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 钯催化偶联的开路人 / Richard F. Heck 1931–2015 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  赫克的一生 — Sanger 式时间线（10 节点：1931→1952→1954→1956→1960s→1971→1982→1989→2010→2015）
04  早年：从 Springfield 到洛杉矶 (1931–1952) — 表格「时间|事件|结果」
05  UCLA：Winstein 门下 (1952–1955) — 表格「阶段|方向|结果」+ 公式框：芳基磺酸酯取代/重排
06  ETH 与 Hercules (1955–1971) — 表格「地点|课题|结果」（Prelog / 高分子 / 有机钴）
07  Heck 反应诞生 (1960s 末) — 表格「问题|方法|结果」+ 公式框：芳基汞 × 烯烃，Pd 催化，JACS 七连发
08  Mizoroki 改进与特拉华岁月 (1970s–1989) — 表格「人物|贡献|结果」+ 公式框：芳基卤版本（Mizoroki–Heck）
09  从 45 页到 377 页 (1982→2002) — Sanger FFT 页式流程（扩散史）+ 公式框：分子内 Heck 377 页
10  家族与延伸 — 表格「反应|试剂|创立者」（Suzuki–Miyaura / Stille / Kumada / Hiyama / Negishi / Sonogashira / Buchwald–Hartwig）
11  2010 诺贝尔化学奖 — 公式框：官方理由 "for palladium-catalyzed cross couplings in organic synthesis"；Seaborg Medal 2011
12  萘普生与基因组 — 表格「应用|化学|意义」（naproxen / 荧光染料标记 DNA 碱基 / 蛋白质示踪）
13  晚年与遗产 — 四分类遗产盒（菲律宾岁月 / 荣誉讲席 / Heck Lectureship 2004 / Carothers & Brown 奖）
14  结尾 — 「一根钯线，缝起了碳与碳之间的千万种可能。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2010 诺奖口径 | 与 Negishi、Suzuki **三人共享**；官方理由原文 "for palladium-catalyzed cross couplings in organic synthesis"（page.md 明载）；勿写"独享"，勿把三人合成一人 |
| 年代分工 | Heck 反应 1960s 末（芳基汞版本）；Negishi 偶联（有机锌）与 Suzuki 偶联（有机硼）1970s——三人贡献**方向不同**：Heck 开创钯催化烯烃芳基化，另两位是金属试剂偶联；勿写成"同一反应的三个名字" |
| PhD 年份 | 正文作 1954 获 PhD；infobox 论文系年 1955——**以正文 1954 为准**，论文年份如引用须注明 infobox 口径 |
| Mizoroki | 1970s 初**独立**报道芳基卤版本（毒性低于汞试剂）——是"独立改进者"而非 Heck 学生/下属；反应通称 Mizoroki–Heck 反应；页面对 Mizoroki 生卒无载，禁写 |
| 首创归属 | page.md 明载 Heck 是**第一个**完整表征 π-烯丙基金属配合物、第一个阐明烯烃氢甲酰化机理的人——"first" 两处页面明载可写，勿扩散到其他"第一次" |
| Sonogashira | Sonogashira 在 Heck 报道的炔偶联程序上加 Cu(I) 盐——主从关系如实写，勿倒置 |
| 死因 | 死于马尼拉**公立医院**（in a public hospital），2015-10-09；享年 84——"公立医院"是页面明载细节，可如实写；死因病名页面无载禁写 |
| 卒日双值 | frontmatter date_of_death 有 2015-10-10 / 2015-10-09 两值——**以正文 10 月 9 日为准** |
| 无子女 | 夫妇无子女（page.md 明载）；妻 Socorro Nardo-Heck 2012 年先逝——家庭页如实一笔 |
| 公司 | 终身无公司创立叙事（那是 Steitz 篇）；Hercules 是工业雇主非创业——勿混淆 |
| 引语红线 | 页面正文无第一人称直接引语——中文引号内不得出现任何"原话"；2010 官方理由是唯一可引的英文原句 |
| 同名 | 与足球运动员等无关；infobox Commons 分类作 "Richard Fred Heck"——正文全名统一 Richard Frederick Heck |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106471 | ✅（新建 #NEW） |
| name_zh | 理查德·F·赫克 | ✅ |
| name_en | Richard F. Heck（page.md 规范名） | ✅ |
| birth_date | 1931-08-15 | ✅ |
| death_date | 2015-10-09 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：organometallic chemistry / palladium-catalyzed cross-coupling / organic synthesis，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Saul Winstein | 师→生（博士导师） | UCLA PhD 1954，芳基磺酸酯化学（库内已有记录） |
| advisor-student | Vladimir Prelog | 师→生（博士后导师） | ETH Zurich 博士后；1975 诺贝尔化学奖（库内已有记录） |
| colleague | David S. Breslow | 无向 | Hercules 期间合作有机钴化学 |
| co-honored | Ei-ichi Negishi | 无向 | 2010 诺贝尔化学奖共同得主 |
| co-honored | Akira Suzuki | 无向 | 2010 诺贝尔化学奖共同得主 |
| spouse | Socorro Nardo-Heck | 无向 | 移居菲律宾；2012 先逝；无子女 |
| other | Tsutomu Mizoroki | 无向 | 1970s 初独立报道芳基卤偶联（Mizoroki–Heck 反应） |

> **禁入库名单**（页面无载或事件性提及，不入库）：Makoto Kumada / Kenkichi Sonogashira / John Stille / Buchwald / Hartwig（仅 See also 与反应命名链接，无人际关系明载）；Peter Diamond / Dale T. Mortensen / Christopher A. Pissarides / Andre Geim / Konstantin Novoselov（2010 年斯德哥尔摩集体合影，跨学科同届得主非人际关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2010，与 Negishi / Suzuki 共享）
- Wallace H. Carothers Award（2005；表彰有重大商业影响的创造性化学应用）
- Herbert C. Brown Award（2006；合成方法创造性研究）
- Glenn T. Seaborg Medal（2011）
- 名誉博士：Uppsala University 药学院（2011）、De La Salle University（2012）
- University of Delaware 年度讲席以他命名（2004，Willis F. Harrington 系讲席；其年度讲座 2004 年冠名 Heck）

## 9. 机构清单

- 教育：UCLA（BS 1952 / PhD 1954）
- 博士后：ETH Zurich（随 Prelog）→ UCLA（回炉）
- 产业：Hercules Corporation（Wilmington, Delaware，1956 入职，高分子化学起步）
- 任职：University of Delaware 化学与生物化学系教授（1971–1989 退休；Willis F. Harrington Professor Emeritus）；ETH Zurich / De La Salle University（2012 兼职教授）列于 infobox Workplaces
- 退休后：移居菲律宾 Quezon City；2012 受聘马尼拉 De La Salle University 化学系兼职教授

## 10. 终审清单

- [x] 生卒 1931-08-15 / 2015-10-09，享年 84，出生地 Springfield、去世地马尼拉公立医院
- [x] 2010 三人共享（Negishi / Suzuki）表述准确；诺奖理由英文原文口径正确
- [x] Heck 反应 1960s 末（芳基汞）→ Mizoroki 1970s 初（芳基卤）年代与主从关系正确
- [x] "first" 断言仅限 π-烯丙基配合物与氢甲酰化机理两处（页面明载）
- [x] 卒日双值取正文 10-09；无子女如实
- [x] 引语红线：全文无可引第一人称原话，仅 2010 官方理由英文原句
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Richard_F._Heck/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 内真实肖像已就位，否则装饰圆占位并注明
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：中文引号内原话必须能在 page.md 找到；无原话一律改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2010 另两篇（Negishi、Suzuki）口径互查：共享得主名、诺奖理由、年代分工一致
