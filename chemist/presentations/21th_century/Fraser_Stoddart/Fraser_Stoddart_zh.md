# Fraser Stoddart（弗雷泽·斯托达特）立传提示词

> qid=Q376243 · 1942-05-24 – 2024-12-30 · 英国/美国化学家 · 21 世纪 · 诺贝尔化学奖（2016，与 Jean-Pierre Sauvage、Bernard L. Feringa 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Fraser_Stoddart/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本次执行的版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像位**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 `images.txt` **无单人真实肖像**（仅 2016 白宫奥巴马接见合影与若干晶体结构图）——封面用主色装饰圆占位（圆内 `\faIcon{cog}` 呼应机械键），图注注明「装饰圆占位 · 页面无单人肖像」；正文可用轮烷晶体结构图（Eur. J. Org. Chem. 1998）与分子 Borromean 环图（Science 2004）作插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace 机械键的缔造者\enspace·\enspace 英国 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（西北大学 · 轮烷/分子开关 · 2016 诺贝尔化学奖）。
3. **必须有身份信息页**（★ 必做）：左侧头像（装饰圆）+ 右侧 2×2 信息网格，至少含：生卒（1942-05-24 Edinburgh – 2024-12-30 Melbourne）、本名 James Fraser Stoddart（Sir）、国籍（United Kingdom / United States）、教育（University of Edinburgh BSc 1964 / PhD 1966）、博士导师（Edmund Langley Hirst / D M W Anderson）、核心领域（supramolecular chemistry / 机械键）、机构（Northwestern）、荣誉。事实取自本地 page.md，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「互锁 / 穿线」母题——大圆套小圆暗示轮烷的环-轴穿线。
5. **表格语义化 + 公式框**（★ 桑格版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir James Fraser Stoddart（FRS FRSE HonFRSC；中文惯称：弗雷泽·斯托达特/詹姆斯·弗雷泽·斯托达特爵士）
- **生卒**：1942-05-24 生于苏格兰爱丁堡 → 2024-12-30 逝于澳大利亚墨尔本（探望女儿期间于心梗/心脏骤停离世于酒店，享年 82；page.md 明载）
- **国籍**：United Kingdom（英国）、United States（美国，后入籍）
- **身份**：化学家；香港大学化学讲席教授（Chair Professor，2023 起）；美国西北大学化学系 Board of Trustees Professor、Stoddart 机械立体化学组（Mechanostereochemistry Group）负责人
- **家庭**：Tom 与 Jean Stoddart 的独子；在 Edgelaw 农场（三户人家的小社区）以佃农之子长大；幼年痴迷拼图与建构玩具——自认这是分子建构兴趣的源头；1968 年娶 Norma Agnes Scholan（生化学博士，曾在 Sheffield/Birmingham/UCLA 支持其研究），2004 年她因癌症去世；两女 Fiona Jane 与 Alison Margaret
- **教育轨迹**：
  - Carrington, Midlothian 村立小学 → 爱丁堡 Melville College
  - 1960 入爱丁堡大学（初学化学/物理/数学）
  - 1964 BSc（化学）；1966 PhD（*Studies on plant gums of the Acacia group*，金合欢属植物天然树胶研究）
  - 1980 爱丁堡大学 DSc（*Some adventures in stereochemistry*，「分子之外的立体化学」）
- **导师**：Edmund Langley Hirst 与 D M W Anderson（爱丁堡大学，共同指导）
- **研究领域**：超分子化学、物理有机化学、机械立体化学——机械键（mechanical bond）、轮烷/索烃、分子开关与分子梭、模板导向合成、化学拓扑、MOF

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **农场上的拼图少年（1942）**：三户人家的 Edgelaw 农场；拼图与建构玩具——「分子建构」的最早启蒙。
2. **爱丁堡树人胶博士（1960–1966）**：金合欢树胶研究获 PhD；导师 Hirst 是糖化学名家。
3. **加拿大博士后（1967）**：女王大学（金斯顿）国家研究委员会博士后。
4. **谢菲尔德起步（1970–）**：以 ICI Research Fellow 身份转入 Sheffield，后任化学讲师。
5. **ICI Runcorn 的种子（1978–1981）**：借调 ICI 企业实验室三年——**正是在这里开始研究机械互锁分子**，日后分子机器的伏笔。
6. **伯明翰讲席（1990）**：出任有机化学讲席教授，1993–97 任化学学院院长。
7. **UCLA：接棒 Cram（1997）**：任 Saul Winstein 化学讲席教授，接替诺奖得主 Donald Cram；2002–2007 领导加州纳米系统研究院（CNSI，2003 起任 Fred Kavli 讲席教授兼院长）。
8. **西北大学机械立体化学组（2008）**：建立 Mechanostereochemistry Group，任 Board of Trustees Professor；2010 年出任集成系统化学中心（CCIS）主任。
9. **机械键合成学**：以 cyclobis(paraquat-p-phenylene)（「小蓝盒」）与富电子芳香客体的分子识别为基础，建立轮烷/索烃的高效模板导向合成——分子梭、分子开关随之而来。
10. **Borromean 分子环（2004）**：以动态共价化学合成分子 Borromean 环（Science 2004, 304, 1308–1312）——三环相扣、任意两环不互锁的拓扑奇迹。
11. **卡通配色语言**：自 1980 年代末发展「solid circle + 彩色标注」的标志性画法（蓝=缺电子识别单元、红=富电子），被全领域沿用——「little blue box」因此得名。
12. **2016 诺贝尔化学奖**：与 Jean-Pierre Sauvage、Bernard L. Feringa 共享，理由 "for the design and synthesis of molecular machines"；同年获 RSC Haworth Memorial Lectureship。
13. **桃李与产业（35 年近 300 名博士生/博后）**：知名学生 David Leigh、Douglas Philp、Narayanaswamy Jayaraman；2019 创办护肤品牌 Noble Panacea，2021 共同创办储氢初创 H2MOF，2014 兼职天津大学、2017 兼职 UNSW、2023 加入香港大学——晚年辗转东西方的「分子建筑师」。

## 3. 配色方案（桑格式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绿 forest-deep） | `#146B3A` | 机械立体化学的沉稳底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（小蓝盒 badgeBlueBox） | `#2E5A9E` | 蓝·cyclobis(paraquat-p-phenylene) / 缺电子识别单元 |
| 分类色 2（轮烷与分子梭 badgeRotaxane） | `#B0722A` | 铜·穿线 / 分子梭与开关 |
| 分类色 3（Borromean 环 badgeBorromean） | `#7A1E28` | 深红·三环拓扑 / 动态共价化学 |
| 分类色 4（纳米器件 badgeNano） | `#4A5D23` | 橄榄·NEMS / 纳电子器件 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），大圆套小圆暗示轮烷的环-轴互锁。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`；不要复制 wav 文件，Makefile 里直接引用原路径）
- **风格**：恢弘 / 追思 / 建构感
- **匹配理由**：
  - 「建构感」匹配拼图少年 → 机械键大师的一生主线
  - 「追思」匹配纪念性质——2024-12-30 墨尔本辞世，本篇为纪念性立传
  - 「恢弘」匹配其跨越大西洋与太平洋的学术版图（Sheffield → Birmingham → UCLA → Northwestern → 天津/UNSW/港大）
- **时长**：按 Makefile 默认 `-shortest` 对齐 15 页即可

## 4. Slide 规划（15 页，桑格式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 机械键的缔造者 / Sir Fraser Stoddart 1942–2024 + 四色 badge + 右上头像占位 + 国籍行「英国 / 美国」
02  身份信息页（★ 必做）— 左头像占位 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/机构/荣誉）
03  斯托达特的一生 — 桑格式时间线（10 节点：1942→1964→1966→1967→1970→1978→1990→1997→2008→2016→2024）
04  早年：Edgelaw 农场的拼图少年 (1942–1960) — 表格「时间|事件|结果」
05  爱丁堡：树胶与立体化学 (1960–1980) — 表格「阶段|内容|结果」+ 公式框：DSc 1980「分子之外的立体化学」
06  ICI Runcorn：机械互锁的种子 (1978–1981) — 表格「问题|方法|结果」
07  机械键合成学：小蓝盒与轮烷 (1990s) — 表格「问题|方法|结果」+ 公式框：识别单元 ⊂ 小蓝盒 → 轮烷；配 1998 轮烷晶体结构图
08  Borromean 分子环 (2004) — 表格「挑战|方法|结果」+ 公式框：三环相扣·任意两环不互锁；配 Science 2004 结构图
09  2016 诺贝尔化学奖 — 公式框：官方获奖理由 "for the design and synthesis of molecular machines"（与 Sauvage / Feringa 共享，三人三步：索烃→轮烷→马达）
10  卡通配色与「小蓝盒」 — 表格「元素|约定|意义」（蓝=缺电子/红=富电子/solid circle）；David Leigh 评语（间接转述）
11  荣誉与学会 — 桑格式「类别|代表|意义」表格 + itemize 清单（FRS 1994 / Knight Bachelor 2007 / Davy Medal 2008 / NAS 2014 / Nobel 2016）
12  五所大学的长跑 — 桑格 LMB 页式流程图（Sheffield 1970 → Birmingham 1990 → UCLA 1997 → Northwestern 2008 → 天津 2014/UNSW 2017/港大 2023）
13  遗产：机械键开启的纳米世界 — 四分类遗产盒 + 公式框：35 年近 300 名博士生/博后；Fraser & Norma Stoddart Prize（爱丁堡，2013 首颁）
14  结尾 — 「先学会把环穿到轴上，才谈得上让分子做工。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2016 获奖理由 | 官方措辞 "for the design and synthesis of molecular machines"；**勿泛化成「发明分子机器」** |
| 共享口径 | 2016 为**三人共享**——Sauvage（索烃，第一步）/ Stoddart（轮烷与分子开关）/ Feringa（分子马达）；对另两人一律用规范全名 Jean-Pierre Sauvage / Bernard L. Feringa |
| 生卒 | 1942-05-24 Edinburgh – 2024-12-30 Melbourne，享年 82；死因**心脏骤停**（cardiac arrest）、探望女儿期间在酒店——三要素（日期/地点/原因）须全文一致，勿写「病逝」 |
| 双名 | 本名 **James** Fraser Stoddart，惯称 Fraser Stoddart；2007 年受勋后称 **Sir**；勿把「Sir」写成爵位名目以外的头衔（Knight Bachelor） |
| 双博士导师 | PhD 导师为 **Edmund Langley Hirst 与 D M W Anderson 两人**（共同指导）——勿只写一人；infobox 另列 Other academic advisors（J K N Jones、W D Ollis）——**仅 infobox、正文无载，不入库** |
| 学位年份 | BSc 1964 / PhD 1966 / DSc 1980（爱丁堡）——PhD 论文是树胶研究、DSc 论文是立体化学，勿混 |
| ICI Runcorn | 1978–1981 借调三年才开始研究机械互锁分子——勿提前到 Sheffield 讲师时期 |
| 接棒 Cram | 1997 年接替 Donald Cram 的 Saul Winstein 讲席——**仅同事性承接，非师承，不入库** |
| 学生口径 | Notable students 仅 infobox 三人 David Leigh / Narayanaswamy Jayaraman / Douglas Philp；「35 年近 300 名博士生/博后」是总量表述——勿把 David Leigh 写成「共同发展机械键的合作者」之外的关系（Leigh 评语系他人对其的评价引文，转述时注明是 Leigh 所言） |
| 引语红线 | 页面仅有 David Leigh 评语与一句无主引文（"His work bridged the gap..."）——引用时**注明出处/或改为间接转述**；中文引号内不得出现无法溯源的「原话」 |
| 商业与兼职 | Noble Panacea（2019）、H2MOF（2021）、天津大学（2014）、UNSW（2017）、香港大学（2023）均页面明载——可客观列举，勿加评价 |
| 合影图注 | 白宫合影为 2016-11-30 接见美国诺奖得主场景——仅作插图可用，**勿据此写与奥巴马的个人关系** |
| h-index | 168（2024）；发表 1200+ 篇（2023）——引用须注明来源年份 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q376243 | ✅ |
| name_zh | 弗雷泽·斯托达特 | ✅ |
| name_en | Fraser Stoddart | ✅ |
| birth_date | 1942-05-24 | ✅ |
| death_date | 2024-12-30 | ✅ |
| nationality | United Kingdom（rank 0）/ United States（rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | supramolecular chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh |
|---|---|---|
| supramolecular chemistry | 0 | 超分子化学 |
| molecular machines | 1 | 分子机器 |
| stereochemistry | 2 | 立体化学 |
| organic chemistry | 3 | 有机化学 |
| nanotechnology | 4 | 纳米技术 |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edmund Langley Hirst | 师→生（博士导师） | 爱丁堡大学博士导师之一，1966 树胶论文 |
| advisor-student | Douglas M W Anderson | 师→生（博士导师） | 爱丁堡大学共同博士导师（infobox Doctoral advisor 行并列） |
| advisor-student | David Leigh | Stoddart → 学生 | 知名学生（infobox）；后评述其「让化学家看见分子机器的可能性」 |
| advisor-student | Douglas Philp | Stoddart → 学生 | 知名学生（infobox Notable students） |
| advisor-student | Narayanaswamy Jayaraman | Stoddart → 学生 | 知名学生（infobox Notable students） |
| co-honored | Jean-Pierre Sauvage | 无向 | 2016 诺贝尔化学奖共同得主 |
| co-honored | Ben Feringa | 无向 | 2016 诺贝尔化学奖共同得主 |
| spouse | Norma Agnes Scholan | 无向 | 1968 结婚，2004 因癌症去世；生化学博士，曾在 Sheffield/Birmingham/UCLA 支持其研究 |

> **禁入库名单**（页面明载但不入库）：Donald Cram（仅讲席承接关系，非师承/合作）；J K N (Ken) Jones、W David Ollis（infobox Other academic advisors，正文无载）；父 Tom、母 Jean、女儿 Fiona Jane / Alison Margaret（家庭成员）；Barack Obama（合影场景）；Saul Winstein（讲席名号来源）。
> **对手方命名红线**：Sauvage 用规范名 Jean-Pierre Sauvage（库内既有记录 id=4020，勿写变体）；Feringa 用 Ben Feringa。

## 8. 奖项清单

- International Izatt-Christensen Award in Macrocyclic Chemistry（1993）
- Fellow of the Royal Society of London，FRS（1994）
- Arthur C. Cope Scholar Award（ACS，1999）
- Nagoya Gold Medal in Organic Chemistry（2004）
- King Faisal International Prize in Science（2007）
- Albert Einstein World Award of Science（2007）
- Feynman Prize in Nanotechnology（Experimental，2007）
- Tetrahedron Prize for Creativity in Organic Chemistry（2007）
- Knight Bachelor（2006 年末新年授勋名单，2007 授勋）
- Arthur C. Cope Award（ACS，2008）
- Davy Medal（Royal Society of London，2008）
- Fellow of the Royal Society of Edinburgh，FRSE（2008）
- Royal Medal of the Royal Society of Edinburgh（2010）
- Centenary Prize（RSC，2014）
- Member of the National Academy of Sciences，US（2014）
- Haworth Memorial Lectureship（RSC，2016）
- Nobel Prize in Chemistry（2016，与 Sauvage / Feringa 共享）
- Fray International Sustainability Award（2018）
- Fellow of the National Academy of Inventors（2019）
- 会士/院士：AAAS 会士（2005）、荷兰皇家艺术与科学院外籍会员（2006）、Leopoldina（1999）、American Academy of Arts and Sciences（2012）、澳大利亚科学院会士
- 荣誉博士：University of Birmingham、Laval University

## 9. 机构清单

- 教育：Carrington 村立小学、Melville College（爱丁堡）、University of Edinburgh（BSc 1964 / PhD 1966 / DSc 1980）
- 任职：Queen's University at Kingston 博士后（1967–1969）；University of Sheffield（1970–，ICI Research Fellow → 讲师 → 1982 Readership）；ICI Corporate Laboratory, Runcorn（1978–1981 借调）；UCLA 访问（1978 年初 SRC Senior Visiting Fellow）；University of Birmingham（1990–1997，有机化学讲席、化学学院院长 1993–97）；UCLA（1997–2007，Saul Winstein 讲席；CNSI 代理共同主任 2002-07、Fred Kavli 讲席 2003、院长至 2007-08）；Northwestern University（2008–，Board of Trustees Professor；CCIS 主任 2010）；University of New South Wales（2017 兼职）；Tianjin University（2014）；University of Hong Kong（2023，化学讲席教授）
- 创办/命名：Fraser & Norma Stoddart Prize（爱丁堡大学博士生奖，2013 首颁）；Noble Panacea（2019）；H2MOF（2021 共同创办）

## 10. 终审清单

- [ ] 生卒 1942-05-24 Edinburgh / 2024-12-30 Melbourne，享年 82，死因心脏骤停——三处一致
- [ ] 2016 三人共享（Sauvage / Feringa）表述准确；获奖理由 "for the design and synthesis of molecular machines" 口径准确
- [ ] 三人分工不串位：Sauvage=索烃（1983）/ Stoddart=轮烷/分子梭 / Feringa=分子马达
- [ ] 双博士导师 Hirst + Anderson；Other advisors 不入库
- [ ] 学位年份 BSc 1964 / PhD 1966 / DSc 1980 准确
- [ ] 机构轨迹 Sheffield→Birmingham→UCLA→Northwestern→港大（含天津/UNSW 兼职）准确
- [ ] 全篇引语仅 Leigh 评语且注明出处；无编造引语
- [ ] 正文采用桑格式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make pdf` 编译通过，0 错误、vbox≤10pt、hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Fraser_Stoddart/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆占位（页面无单人肖像），图注注明；轮烷（1998）与 Borromean（2004）结构图就位
- [ ] 国籍：封面顶部明示英国 / 美国
- [ ] 引语核对：Leigh 评语须可溯源且注明说话人
- [ ] 编译验证：`make distclean && make pdf`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Modrich / Sancar / Sauvage / Feringa）及桑格既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，执行者不改。
> **数据事实来源唯一**：`chemist/presentations/21th_century/pages/Fraser_Stoddart/page.md`；页面无载的数据如实标注「页面无载」，禁止编造。
