# Eric Betzig（埃里克·贝齐格）立传提示词

> qid=Q1351105 · 1960-01-13 生于美国密歇根州安娜堡 · 在世 · 美国 · 诺贝尔化学奖（2014，与 Hell/Moerner 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Eric_Betzig/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md` §0-§11 结构标杆（高斯式：身份信息页 + 时间线 + 表格语义化 + 公式框）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `pages/Eric_Betzig/images.txt` 中 2018 年宗座科学院照 `Eric_Betzig_2018.jpg`；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{camera}\enspace 看见纳米的眼睛\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Robert Eric Betzig、国籍、出生地、教育、博士导师、领域、任职、家庭、荣誉。事实取自本地 page.md infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「光学显微」母题——弥散圆点暗示荧光分子被逐个点亮定位。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（Abbe 极限 d = λ/(2NA)、PALM 单分子定位精度等）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Eric Betzig（中文惯称：埃里克·贝齐格）
- **生卒**：1960-01-13 生于密歇根州安娜堡（Ann Arbor）· 在世
- **国籍**：United States（美国）
- **身份**：物理学家；UC Berkeley 物理学教授 + 分子与细胞生物学教授（双聘）；Janelia Farm 研究园区资深研究员
- **家庭**：母亲 Helen Betzig、父亲工程师 Robert Betzig。两婚：第一任 Ruby Ghosh（凝聚态物理学家，二子 Cayden、Ravi）；第二任 Na Ji（纪楠/生物物理学家，子女 Max、Mia、Zoe——名字按 page.md 原文，不加中文名）
- **教育轨迹**：
  - 志向航天工业 → 加州理工学院读物理，1983 BS
  - 康奈尔大学：1985 MS、1988 PhD（应用物理与工程物理）；导师 Michael Isaacson，另与 Aaron Lewis 合作
  - 博士论文 *Near-field Scanning Optical Microscopy*（1988）：发展突破 0.2 μm 理论极限的高分辨光学显微镜
- **研究领域**：荧光显微、光激活定位显微（PALM）、晶格光片显微（lattice light-sheet）、应用物理

## 2. 核心叙事亮点（约 13 条）

1. **安娜堡工程师之子（1960）**：生于密歇根安娜堡，父为工程师——立志进入航天工业。
2. **加州理工物理学（–1983）**：物理 BS 毕业，随后转入显微成像方向。
3. **康奈尔近场光学（1985–1988）**：师从 Michael Isaacson，与 Aaron Lewis 合作；博士论文聚焦突破 0.2 μm 衍射极限的近场扫描光学显微镜。
4. **贝尔实验室（1989）**：加入 AT&T Bell Labs 半导体物理研究部。
5. **Moerner 的启发（1989）**：同事 William E. Moerner 制成首台超越 Abbe 极限（0.2 μm）的光学显微镜，但只能在近绝对零度工作——Betzig 由此获得灵感。
6. **室温单分子成像（1993）**：成为**第一个在室温下对单个荧光分子成像**并定位精度优于 0.2 μm 的人；因此获 William O. Baker Award（原 NAS Award for Initiatives in Research）。
7. **McMillan 奖（1992）**：获 William L. McMillan Award。
8. ** disillusioned 与「退隐」（1994–1996）**：1994 因学界受挫与贝尔实验室公司架构的不确定性而离开；做了几年全职奶爸。
9. **家族公司弯路（1996–2002）**：任家族参股的 Ann Arbor Machine Company 研发副总裁，开发柔性自适应伺服液压技术（FAST）——耗资数百万美元只卖出两台。
10. **PALM 复出（2002）**：在密歇根 Okemos 创办 New Millennium Research；受 Mike Davidson 荧光蛋白工作启发，与老贝尔实验室搭档 Harald Hess 在其**客厅里**造出第一台 PALM 原型机——不到两个月建成，广受关注；同年 10 月 HHMI Janelia 签下他（实验室尚未建成）。
11. **Janelia 群组长（2006）**：正式加入 Janelia 任 group leader，发展超高分辨荧光显微；用于研究人类胚胎细胞分裂。2010 年婉拒 Max Delbruck Prize（该奖改授 Xiaowei Zhuang）。
12. **2014 诺贝尔化学奖**：与 Stefan Hell、康奈尔校友 William E. Moerner 共享，官方理由 "for the development of super-resolved fluorescence microscopy"（超高分辨荧光显微技术之发展）。
13. **宗座院士与伯克利（2016–2017）**：2016-05-31 获教宗方济各任命为宗座科学院院士；2017 年夏加入 UC Berkeley 教员，兼劳伦斯伯克利国家实验室联合聘任。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫堇 violaceous） | `#372A75` | 荧光分子的深紫与显微镜的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（近场光学 badgeNear） | `#5E35B1` | 蓝紫近场扫描 / 博士论文 |
| 分类色 2（单分子 badgeSingle） | `#00897B` | 青单分子室温成像 1993 |
| 分类色 3（PALM badgePalm） | `#F2994A` | 橙光激活定位 / Janelia |
| 分类色 4（光片显微 badgeSheet） | `#C0395B` | 玫瑰晶格光片 / 胚胎成像 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「荧光分子逐点定位」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，勿复制 wav，Makefile 直接引用路径）
- **风格**：辽阔 / 起伏 / 电影感
- **匹配理由**：
  - "SEA" 的辽阔感匹配「从衍射极限的近海驶入纳米深蓝」的显微革命叙事
  - 起伏匹配其人生曲线——贝尔实验室巅峰 → 退隐奶爸 → 家族公司弯路 → 客厅造出 PALM 复出封神
  - 电影感匹配 Janelia 时期的工程浪漫（两个月客厅造机）
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 看见纳米的眼睛 / Eric Betzig 1960– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/家庭/领域/任职/荣誉）
03  贝齐格的一生 — 高斯式时间线（10 节点：1960→1983→1988→1989→1993→1994→2002→2006→2014→2017）
04  早年与加州理工 (1960–1983) — 表格「时间|事件|结果」
05  康奈尔：近场光学 (1985–1988) — 表格「问题|方法|结果」
06  贝尔实验室：室温单分子 (1989–1993) — 表格「挑战|方法|结果」+ 公式框：Abbe 极限 d=λ/2NA
07  退隐与弯路 (1994–2001) — 表格「阶段|处境|结果」（奶爸岁月 / FAST 只卖两台）
08  客厅里的 PALM (2002) — 表格「问题|方法|结果」+ 公式框：PALM 定位精度 ∝ 1/√N
09  Janelia 群组长 (2006–) — 表格「方向|技术|结果」
10  2014 诺贝尔化学奖 — 三人共享页（Hell / Moerner / Betzig）+ citation 原句公式框
11  技术谱系：三条路线 — 表格「人物|路线|结果」（Hell=STED 受激发射损耗；Betzig/Moerner=单分子/光开关蛋白——分工勿混）
12  荣誉与家庭 — 高斯式「类别|代表|意义」表格（NAS 2015 / Baker Award / McMillan Award；两婚五子女）
13  遗产：伯克利与光片未来 — 四分类遗产盒（Berkeley 双聘 / lattice light-sheet 2014 / 宗座院士）
14  结尾 — 「让荧光分子自己开口说话。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2014 获奖理由 | 官方原句 "for the development of super-resolved fluorescence microscopy"；三人**共享**（Betzig / Hell / Moerner），勿写独享 |
| 三人分工 | **Hell = STED（受激发射损耗）**；**Betzig = PALM（光激活定位显微）**；**Moerner = 单分子光谱/光开关蛋白基础**——技术路线分工勿混 |
| 康奈尔校友口径 | Betzig 页称 Moerner 为 "fellow Cornell alumnus"——写「康奈尔校友」即可，勿展开二人在康奈尔重叠时段细节 |
| 博士导师 | Michael Isaacson（infobox + 正文「supervisor」）；Aaron Lewis 是**合作者**（正文 "also worked with"）——勿写成第二导师 |
| Moerner 关系 | 1989 年 Moerner 是 Betzig 的**贝尔实验室同事**且其仪器需近绝对零度——「受其研究启发」；勿写「Moerner 指导 Betzig」 |
| 1993 首创 | 首创点是「**室温下**对单个荧光分子成像并定位 <0.2 μm」——勿省略「室温」限定 |
| FAST 结果 | 耗资数百万只卖出**两台**——如实写，勿美化 |
| 2010 退奖 | Betzig **婉拒** Max Delbruck Prize，奖改授 Xiaowei Zhuang——勿写「落选」 |
| 家庭 | 第一任 Ruby Ghosh（凝聚态物理学家）、第二任 Na Ji（生物物理学家）；子女 Cayden/Ravi/Max/Mia/Zoe 五人——人数与归属勿混 |
| 宗座科学院 | 2016-05-31 由教宗方济各任命为院士——事实陈述 |
| 引语红线 | page.md 无 Betzig 直接引语——全部改间接转述，不得编造「原话」 |
| 中文译名 | 埃里克·贝齐格；Na Ji 不加中文译名（page.md 未载中文名） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q1351105 | ✅ |
| name_zh | 埃里克·贝齐格 | ✅ |
| name_en | Eric Betzig | ✅ |
| birth_date | 1960-01-13 | ✅ |
| death_date | null（在世） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | chemistry（frontmatter）/ 荧光显微（person_field 细分见下表） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | super-resolution fluorescence microscopy | 超高分辨荧光显微 |
| 1 | photoactivated localization microscopy (PALM) | 光激活定位显微 |
| 2 | single-molecule imaging | 单分子成像 |
| 3 | lattice light-sheet microscopy | 晶格光片显微 |
| 4 | applied physics | 应用物理 |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主 / 家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael Isaacson | 师→生（博士导师） | 康奈尔博士导师（1988 近场光学论文），infobox+正文双载 |
| colleague | Aaron Lewis | 无向 | 康奈尔合作者（正文 "also worked with"） |
| colleague | William E. Moerner | 无向 | 贝尔实验室同事（1989，正文明载 colleague），其近绝对零度单分子显微镜启发 Betzig |
| colleague | Harald Hess | 无向 | 贝尔实验室旧搭档，客厅共造首台 PALM 原型机 |
| influence | Mike Davidson | 无向 | 其荧光蛋白工作直接启发 PALM（正文 "Inspired by"） |
| co-honored | Stefan Hell | 无向 | 2014 诺贝尔化学奖共同得主 |
| co-honored | William E. Moerner | 无向 | 2014 诺贝尔化学奖共同得主（康奈尔校友） |
| spouse | Ruby Ghosh | 无向 | 第一任妻子，凝聚态物理学家，二子 Cayden/Ravi |
| spouse | Na Ji | 无向 | 第二任妻子，生物物理学家，子女 Max/Mia/Zoe |

> **禁入库名单**（正文仅事件提及、非关系实体）：Xiaowei Zhuang（2010 退奖事件受奖人）、教宗方济各（任命行为）、Patterson/Sougrat/Trautman/Chichester（论文合作者，正文仅列名于论文清单）、Kiehart/Seydoux/Tulu（同前）。父亲 Robert Betzig、母亲 Helen 为家庭背景不入社会关系表。

## 8. 奖项清单

- Nobel Prize in Chemistry（2014，与 Hell/Moerner 共享）
- William L. McMillan Award（1992）
- William O. Baker Award for Initiatives in Research（原 NAS Award for Initiatives in Research）
- Newcomb Cleveland Prize（metadata 有载；正文未展开——如写须核对 AAAS 出处，否则略去）
- Member, US National Academy of Sciences（2015）
- Academician, Pontifical Academy of Sciences（2016-05-31，教宗方济各任命）

## 9. 机构清单

- 教育：California Institute of Technology（BS 1983）、Cornell University（MS 1985 / PhD 1988）
- 任职：AT&T Bell Laboratories 半导体物理研究部（1989–1994）→ Ann Arbor Machine Company 研发副总裁（1996–）→ New Millennium Research 创办人（2002，Okemos, Michigan）→ HHMI Janelia Farm Research Campus（2002-10 加入；2006 group leader；资深研究员）→ UC Berkeley 物理学 + 分子与细胞生物学双聘教授，兼 Lawrence Berkeley National Laboratory（2017–）

## 10. 终审清单

- [x] 生卒 1960-01-13 / 在世；出生地安娜堡
- [x] 2014 三人共享表述准确；citation 英文原句完整
- [x] 三人技术路线分工（STED / PALM / 单分子基础）表述准确
- [x] 博士导师仅 Isaacson；Lewis 为合作者
- [x] 2010 婉拒 Max Delbruck Prize 表述准确
- [x] 引语全部间接转述（page.md 无直接引语）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 读取 `pages/Eric_Betzig/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先 `Eric_Betzig_2018.jpg`（Commons），404 则装饰圆占位
- [ ] 国籍：封面明示美国
- [ ] 引语核对：无直接引语，全篇间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger/高斯模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2014 三人共享另两篇（Hell / Moerner）口径交叉对齐
