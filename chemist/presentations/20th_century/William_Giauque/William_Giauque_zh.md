# William Giauque（威廉·吉奥克）立传提示词

> qid=Q110073 · 1895-05-12 – 1982-03-28 · 美国化学家（生于加拿大） · 20 世纪 · 诺贝尔化学奖（1949，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/William_Giauque/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（页面实载图为 "Giauque in 1949" 照——images/ 有图则用真照，缺图用装饰圆占位并注「肖像暂缺」）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{snowflake}\enspace 追逐绝对零度的人\enspace·\enspace 美国（生于加拿大）`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（William Francis Giauque）、国籍（美/加双线）、出生地/去世地、教育（UC Berkeley BS/PhD）、博士导师（George Ernest Gibson）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「低温粒子 / 磁畴」母题——冷色圆点暗示接近绝对零度时趋于静止的分子。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如磁制冷（绝热退磁）原理式。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：William Francis Giauque（发音 /dʒiˈoʊk/ "johk"；中文惯称：威廉·吉奥克）
- **生卒**：1895-05-12 生于加拿大安大略省 Niagara Falls → 1982-03-28 逝于美国加州 Berkeley，享年 86
- **国籍**：United States（美国）+ Canada（加拿大出生）——父 William Tecumseh Giauque 为美国公民，故其生而获美国国籍
- **身份**：化学家（chemist；1949 年诺贝尔化学奖独享得主；低温化学热力学先驱）
- **家庭**：1932 年娶 Muriel Frances Ashley 医生（Dr.），育二子
- **教育轨迹**：
  - University of California, Berkeley：BS 与 PhD（infobox 明载两个学位；**入学/毕业年份页面无载，勿补**）
- **博士导师**：George Ernest Gibson（infobox 与 frontmatter 明载）
- **研究领域**：物理化学——低温化学热力学、磁制冷（magnetic refrigeration）、接近绝对零度的物质性质、热力学第三定律相关验证

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **尼亚加拉瀑布城的加拿大出生者（1895）**：生于安大略 Niagara Falls；因父为美国公民，生而具美国国籍——"生于加拿大的美国人"（Canadian-born American）贯穿一生口径。
2. **伯克利一生（教育+职业）**：教育与职业生涯几乎全部在 UC Berkeley 度过——"spend virtually all of his educational and professional career at Berkeley" 的单校一生。
3. **Gibson 门下（BS → PhD）**：师从 George Ernest Gibson——伯克利物理化学谱系的传承点。
4. **1926 年的大胆提案**：提出观测远低于 1 K 温度的方法（页面同时给出换算注：1 K 即 −457.87 °F 或 −272.15 °C）——彼时许多科学家认为不可能。
5. **磁制冷装置（自行设计）**：亲手设计制造磁制冷（magnetic refrigeration）装置，抵达比多数人设想更近绝对零度的低温——绝热退磁降温的实验落地。
6. **基础定律与工业红利**：这一开拓性工作除了验证自然界基本定律之一，还带来更强的钢、更好的汽油与一系列更高效的工业过程——纯科学与工程的同一条链。
7. **三院院士（1936/1940/1950）**：1936 美国国家科学院、1940 美国哲学学会、1950 美国艺术与科学院——低温王国在本土的全面承认。
8. **1949 诺贝尔化学奖（独享）**："recognized in 1949, for his studies in the properties of matter, at temperatures close to absolute zero"——页面口径即"对极近绝对零度下物质性质的研究"；诺奖演说 "Some Consequences of Low Temperature Research in Chemical Thermodynamics"（1949-12-12）。
9. **Elliott Cresson Medal（1937）**：获奖链上最早的重量级奖项——比诺奖早 12 年。
10. **Willard Gibbs Award（1951）**：诺奖次年再获吉布斯奖章——热力学同行的加冕。
11. **低温化学热力学讲席**：以诺奖演说标题为纲——低温研究与化学热力学的交汇是他一生的学科坐标。
12. **家庭与谢幕**：1932 年与 Muriel Frances Ashley 医生结婚，二子；1982-03-28 逝于 Berkeley——出生与谢幕隔着一整个大陆与 86 年。
13. **名字的读音**：Giauque 读作 /dʒiˈoʊk/（"johk"）——页面专辟发音注，立传中可作趣闻小注。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（低温绿 pine green） | `#146B3A` | 绝对零度附近的深冷与热力学的严谨（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（磁制冷 badgeMagnetocaloric） | `#1B4F72` | 深蓝绝热退磁 / 1926 提案 |
| 分类色 2（热力学 badgeThermo） | `#7D6608` | 琥珀第三定律域 / 化学热力学 |
| 分类色 3（伯克利单校生涯 badgeBerkeley） | `#935116` | 赭石 BS→PhD→教授 一生一校 |
| 分类色 4（工业回响 badgeIndustry） | `#4A5B8C` | 灰蓝更强的钢 / 更好的汽油 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），冷色调为主，呼应「低温粒子趋于静止」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`；不要复制 wav 文件，Makefile 直接引用路径）
- **风格**：空灵 / 恒常 / 冷峻壮美
- **匹配理由**：
  - "空灵" 匹配绝对零度附近的物理图景——分子趋于静止、熵趋于极小的世界
  - "恒常" 匹配其一生一校的长期主义——伯克利从学生到诺奖再到谢幕
  - "冷峻壮美" 匹配磁制冷的开拓气质——在"不可能"处凿出一条通往 1 K 以下的路
- **时长**：以实际文件为准；ffmpeg `-shortest` 自动对齐幻灯片时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 追逐绝对零度的人 / William Giauque 1895–1982 + 四色 badge + 右上头像 + 国籍行（美国·生于加拿大）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名+发音/国籍双线/教育/博士导师/出生地/去世地/领域/荣誉）
03  吉奥克的一生 — Sanger 式时间线（10 节点：1895→1926→1932→1936→1937→1940→1949→1950→1951→1982）
04  加拿大出生，美国公民 (1895–) — 表格「事件|口径|结果」（父籍→国籍 / Canadian-born American）
05  伯克利：一生一校 — 表格「阶段|身份|结果」（BS→PhD→Gibson 门下→执教）
06  1926：低于 1 K 的提案 — 表格「问题|方法|结果」+ 公式框：绝热退磁制冷原理
07  磁制冷装置 — 表格「设计|验证|意义」（自行设计制造 / 抵近绝对零度）
08  从低温到工业 — 表格「发现|应用|结果」（更强的钢 / 更好的汽油 / 高效过程）
09  1949 诺贝尔化学奖（独享） — 表格「年份|奖项|口径」+ 公式框：T→0 的物质性质研究
10  三院院士 — Sanger 式「年份|学会|意义」表格（NAS 1936 / APS 1940 / AAAS 1950）
11  荣誉清单 — 表格「奖项|年份|意义」（Cresson 1937 / Nobel 1949 / Gibbs 1951）
12  家庭与晚年 — 表格「时间|事件|结果」（1932 婚 / 二子 / 1982-03-28 Berkeley 谢幕）
13  遗产：低温化学热力学 — 四分类遗产盒 + 公式框：低温研究 × 化学热力学（诺奖演说题眼）
14  结尾 — 「他把温度的地图，一直画到绝对零度的门前。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1949 获奖口径 | **独享**；页面口径 "for his studies in the properties of matter, at temperatures close to absolute zero"——页面**无载诺贝尔官方 citation 英文原句**，勿杜撰官方措辞，照页面口径转述 |
| 国籍口径 | Canadian-born American：生于加拿大、因父为美国公民而生而获美国籍——勿写"移民美国"或"归化"；nationalities 双条（US rank 0 / Canada rank 1） |
| 教育年份 | infobox 只载 Berkeley BS 与 PhD，**入学/毕业年份页面无载**——身份页留空或写「年份无载」，禁脑补 1920/1922 |
| "低于 1 K" | 页面明载 "temperatures considerably below 1 Kelvin"，且附换算 1 K = −457.87 °F / −272.15 °C——数字照抄勿自算改写 |
| 磁制冷 | "developed a magnetic refrigeration device of his own design"——自行设计制造；勿写"发明磁制冷原理"（页面口径是装置与方法） |
| 博士生 | infobox 仅 **Theodore H. Geballe** 一人；metadata 另有 David A. Shirley、Thomas Reichert 与一条 Q 编号——**metadata-only 禁入库** |
| 配偶身份 | Muriel Frances Ashley 带 Dr. 头衔（页面明载）——1932 年结婚、二子；婚礼地点等页面无载勿补 |
| 三院年份 | NAS 1936 / APS 1940 / AAAS 1950——勿与 Stanley（1940/1941/1949）或 Robinson（1934/1944/1948）串档 |
| 姓氏发音 | /dʒiˈoʊk/——可作小注；勿用中译音替代正文首现的英文名 |
| 去世地 | Berkeley, California——与出生地 Niagara Falls, Ontario 对仗，勿混淆 |
| 同名区分 | William Giauque 无常见重名；与 Giauque–Hampson 循环等工程名词页面无载，勿写 |
| 引语红线 | 页面**无任何直接引语**——全书改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110073 | ✅ |
| name_zh | 威廉·吉奥克 | ✅ |
| name_en | William Giauque | ✅ |
| birth_date | 1895-05-12 | ✅ |
| death_date | 1982-03-28 | ✅ |
| nationality | United States（rank 0）+ Canada（rank 1，出生地） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：physical chemistry / chemical thermodynamics / cryogenics，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George Ernest Gibson | 师→生（博士导师） | UC Berkeley；infobox 与 frontmatter 明载 |
| advisor-student | Theodore H. Geballe | Giauque→学生 | infobox Doctoral students 唯一明载 |
| spouse | Muriel Frances Ashley | 无向 | 1932 年结婚；医生（Dr.）；育二子 |

> **禁入库名单（metadata-only，页面 infobox 无）**：David A. Shirley、Thomas Reichert、Q101498726（metadata doctoral_student 三条——虽 Shirley 曾为 Giauque 讣告合著者亦不入库，页面正文未载师生关系）；Kenneth S. Pitzer（仅参考文献讣告作者，非关系载述）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1949，独享）
- Elliott Cresson Medal（1937）
- Willard Gibbs Award（1951）
- 美国 NAS 成员（1936）；美国哲学学会（1940）；美国艺术与科学院（1950）

## 9. 机构清单

- 教育/任职（单校一生）：University of California, Berkeley——BS、PhD（Gibson 门下）、执教生涯全程
- 学会：美国国家科学院（1936）、美国哲学学会（1940）、美国艺术与科学院（1950）
- 出生地/去世地：加拿大安大略 Niagara Falls → 美国加州 Berkeley

## 10. 终审清单

- [ ] 生卒 1895-05-12 / 1982-03-28，享年 86，出生地 Niagara Falls（安大略）、去世地 Berkeley（加州）
- [ ] 1949 独享；获奖理由按页面口径转述、不杜撰官方 citation
- [ ] 国籍双线（美 rank 0 / 加 rank 1）与 "Canadian-born American" 口径一致
- [ ] 1926 提案 / 磁制冷装置 / 三院 1936-1940-1950 / 诺奖 1949 / Gibbs 1951 年份链准确
- [ ] 教育年份留空（页面无载）；博士生只入 Geballe 一人
- [ ] 全书无杜撰引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/William_Giauque/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：页面实载 "Giauque in 1949" 照核对（images/ 缺图则装饰圆占位并注记）
- [ ] 国籍：封面顶部明示「美国（生于加拿大）」
- [ ] 引语核对：全书无杜撰"原话"（页面无直接引语）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
> **最重要的事：每写一页就 make，看到溢出就修。**
