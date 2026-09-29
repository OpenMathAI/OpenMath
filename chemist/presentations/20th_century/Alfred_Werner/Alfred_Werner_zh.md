# Alfred Werner（阿尔弗雷德·维尔纳）立传提示词

> qid=Q123014 · 1866-12-12 – 1919-11-15 · 瑞士化学家 · 20 世纪 · 诺贝尔化学奖（1913，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Alfred_Werner/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取本地 images/ 目录 c. 1915 照；404 则用装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 配位化学之父\enspace·\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（生于法国阿尔萨斯 / 1894 入瑞士籍）、出生地（Mulhouse）/去世地（Zürich）、教育（ETH Zurich / University of Zurich）、博士导师（Arthur Rudolf Hantzsch）、核心领域（配位化学 / 无机化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「八面体配位 / 配体」母题——离散圆点环绕中心，暗示中心金属离子周围排布的六个配体顶点。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），CoCl₃·6NH₃ → [Co(NH₃)₆]Cl₃ 八面体解说是天然公式素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Alfred Werner（中文惯称：阿尔弗雷德·维尔纳）
- **生卒**：1866-12-12 生于 Mulhouse, Haut-Rhin, Alsace（时属法国；1871 年被德国吞并）→ 1919-11-15 逝于苏黎世一家精神病院，享年 52，死因为动脉硬化（arteriosclerosis，尤以脑部为甚，长年酗酒与过劳加重）
- **国籍**：Switzerland（1894 入籍）；frontmatter 亦列 France（出生地阿尔萨斯时属法国）——立传口径「生于法国阿尔萨斯 · 瑞士籍」
- **身份**：化学家（配位化学奠基人；苏黎世大学教授）
- **家庭**：四子中最幼；父 Jean-Adam Werner 为铸工厂工人，母 Salomé Jeannette Werner（第二任妻子）出身富裕家庭；罗马天主教家庭长大；妻 Emma Werner（infobox）
- **教育轨迹**：赴瑞士入 Swiss Federal Institute（polytechnikum，今 ETH Zurich）学化学——该学院 1909 年前无博士学位授予权，故其 1890 博士学位由 University of Zürich 正式授予 → 巴黎博士后 → 1892 回 ETH 任教
- **导师**：Arthur Rudolf Hantzsch（infobox 博士导师）；Marcellin Berthelot（infobox 并列博士导师；正文对应"巴黎博士后"经历）
- **博士**：1890（University of Zürich 正式授予）
- **研究领域**：无机化学——配位化学、过渡金属配合物构型、立体化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **阿尔萨斯铸工厂之子（1866）**：生于法属阿尔萨斯、长于德占年代、成于瑞士——三国边界的科学人生。
2. **ETH 与苏黎世双校（1885–1890）**：ETH 读书、苏黎世大学拿学位——因 ETH 1909 年前不能授博士。
3. **巴黎博士后（1890–1892）**：随 Marcellin Berthelot（infobox 并列导师）巴黎深造后回 ETH 任教（1892）。
4. **苏黎世大学（1893–1895）**：1893 转入 University of Zurich，1895 晋教授；1894 入瑞士籍。
5. **1893：配位化合物的第一个正确结构**：首次提出含配离子的配位化合物正确结构——中心过渡金属原子被中性或阴离子配体包围；这是配位化学（coordination chemistry）的现代基础。
6. **CoCl₃·6NH₃ 之谜（1893）**：钴"复合物" CoCl₃•6NH₃ 中圆点的性质成谜——Werner 提出 [Co(NH₃)₆]Cl₃：Co³⁺ 被六个 NH₃ 围成八面体顶点，三个 Cl⁻ 以自由离子解离；用电导测量与硝酸银沉淀氯离子分析证实，后磁性磁化率分析亦佐证。
7. **主价与副价**：Co–Cl 键是"主价"（primary valence，今氧化态）；Co–NH₃ 键是"副价"（secondary valence，今配位数）——他也发现配位数 4 或 8 的其他配合物。
8. **几何异构（cis/trans）**：解释两种四氨合物"Co(NH₃)₄Cl₃"（一绿一紫）为 [Co(NH₃)₄Cl₂]Cl 的两种几何异构体——绿者是 trans（两 Cl 对位）、紫者是 cis（两 Cl 邻位），由电导测量确认一个 Cl⁻ 解离。
9. **旋光异构与 hexol（1914）**：制备含旋光异构体的配合物；1914 报道第一个**不含碳**的合成手性化合物 hexol（[Co(Co(NH₃)₄(OH)₂)₃]Br₆）。
10. **理论辐射：Abegg 规则（1904）**：Richard Abegg 基于 Werner 这类观点提出 Abegg's rule（元素最高正负价差常为八）；1916 年 Gilbert N. Lewis 的"八隅体规则"又使用了 Abegg 规则——维尔纳的副价概念层层递进进入近代键合理论。
11. **1913 诺贝尔化学奖（独享）**：因其提出过渡金属配合物的八面体构型（页面口径 "for proposing the octahedral configuration of transition metal complexes"）；他是**第一位获诺贝尔奖的无机化学家**，也是 1973 年之前唯一的一位。
12. **著作**：《Lehrbuch der Stereochemie》（Fischer, Jena, 1904）；诺贝尔演讲 1913-12-11《On the Constitution and Configuration of Higher-Order Compounds》。
13. **晚年悲剧（1919）**：进行性全身动脉硬化（尤其脑部），长年酗酒与过劳加重——1919-11-15 逝于苏黎世精神病院，年仅 52。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 indigo） | `#123C5B` | 配位八面体的结构感与理论化学的冷峻（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（配位结构 badgeCoord） | `#2E5A9E` | 蓝 [Co(NH₃)₆]Cl₃ 八面体 |
| 分类色 2（异构 badgeIso） | `#1B7A43` | 绿 cis/trans 几何异构 |
| 分类色 3（手性 badgeChiral） | `#D97B29` | 琥珀 hexol 无碳手性 |
| 分类色 4（理论辐射 badgeTheory） | `#C0395B` | 玫瑰主价/副价 → Abegg → Lewis 八隅 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「八面体配位 / 配体环绕」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（清单指定 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`）
- **风格**：怀旧 / 忧郁 / 追思
- **匹配理由**：
  - "Nostalgia" 匹配其命运底色——52 岁病逝于精神病院的悲剧收场，天才与陨落的挽歌气质
  - "追思" 匹配其学术遗产——1893 年的正确结构主张起初逆主流而行，回顾时方见其奠基意义
  - "忧郁" 匹配叙事节奏——阿尔萨斯 → 苏黎世 → 1913 巅峰 → 1919 早逝
- **时长对齐**：以曲目实际时长 > 15 页 × 7 秒为宜，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 配位化学之父 / Alfred Werner 1866–1919 + 四色 badge + 右上头像 + 国籍行（生于法国阿尔萨斯 · 瑞士籍）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  维尔纳的一生 — 高斯式时间线（10 节点：1866→1885→1890→1892→1893→1894→1895→1904→1913→1919）
04  阿尔萨斯与苏黎世求学 (1866–1890) — 表格「时间|事件|结果」
05  巴黎博士后与 ETH (1890–1893) — 表格「时间|事件|结果」
06  1893：配位化合物的正确结构 — 表格「问题|方法|结果」+ 公式框：CoCl₃·6NH₃ → [Co(NH₃)₆]Cl₃
07  主价与副价 — 表格「概念|今名|含义」+ 公式框：primary valence = 氧化态 · secondary = 配位数
08  cis/trans 几何异构 — 表格「异构体|颜色|构型」+ 公式框：[Co(NH₃)₄Cl₂]Cl 绿 trans / 紫 cis
09  hexol 与无碳手性 (1914) — 表格「挑战|方法|结果」+ 公式框：[Co(Co(NH₃)₄(OH)₂)₃]Br₆
10  1913 诺贝尔化学奖 — 表格「得主|理由|史实」+ 公式框：独享 · 首位无机化学诺奖得主（1973 前唯一）
11  理论辐射：Abegg 与 Lewis — 表格「人物|承继|结果」（Abegg 规则 1904 / 八隅规则 1916）
12  荣誉 — 高斯式「类别|代表|意义」表格（1913 诺奖 / 法兰克福物理学会荣誉会员）
13  遗产：配位化学的奠基 — 四分类遗产盒 + 公式框：配位化学基石一句话
14  结尾 — 「圆点之谜的圆点，被他在纸上排成了八面体。」（无出处意境句）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1913 独享 | **独享**（页面无共同得主）；获奖口径页面作 "for proposing the octahedral configuration of transition metal complexes"——**页面无载诺贝尔官方全句 citation**，禁杜撰完整官方措辞 |
| "第一"断言 | 页面明载可写：第一位获诺奖的无机化学家、1973 年前唯一一位；配位化合物正确结构 1893 年"第一个提出"（first to propose）——其余"第一次/唯一"禁写 |
| 双博士导师 | infobox 载 Hantzsch 与 Berthelot 并列；正文只明载"巴黎博士后"对应 Berthelot——两行都要写、各自注明来源口径，勿合并成一人 |
| ETH 无授予权 | 1890 博士由 University of Zürich 正式授予（ETH 1909 年前无授予权）——勿写"ETH 博士" |
| 国籍口径 | 生于 Mulhouse（时属法国，1871 被德吞并）；1894 入瑞士籍——勿写"德国人"或漏掉入籍年份 |
| 圆点之谜 | CoCl₃•6NH₃ 的圆点性质当年成谜；Werner 的答案是配位结构 + 三个自由 Cl⁻——电导测量与 AgNO₃ 沉淀是证据，磁性磁化率是后来佐证 |
| 颜色对应 | **绿 = trans（两 Cl 对位）、紫 = cis（两 Cl 邻位）**——勿写反 |
| hexol | 1914 年第一个合成的不含碳手性化合物——勿写"第一个手性化合物"（天然手性早已知） |
| Abegg/Lewis 链条 | Werner 观点 → Abegg 规则（1904）→ Lewis 八隅规则（1916）——Lewis 是**间接承继**（经 Abegg），勿写 Lewis 直接受 Werner 影响 |
| 死因口径 | 动脉硬化（酗酒与过劳加重）、逝于苏黎世精神病院——如实记载，勿美化或渲染 |
| 家庭口径 | 妻 Emma Werner 仅 infobox 一行——页面无婚后细节，禁展开；父 Jean-Adam 铸工厂工人、母为续弦出身富裕——infobox/正文有载可写 |
| 著作口径 | 《Lehrbuch der Stereochemie》1904——立体化学教科书；勿与配位化学专著混淆 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q123014 | ✅ |
| name_zh | 阿尔弗雷德·维尔纳 | ✅ |
| name_en | Alfred Werner | ✅（清单 db_id 为空，按 page.md 规范名新建） |
| birth_date | 1866-12-12 | ✅ |
| death_date | 1919-11-15 | ✅ |
| nationality | Switzerland / France | ✅（瑞士为主 rank 0，法国为出生地口径 rank 1） |
| primary_occupation | chemist | ✅ |
| field_of_work | coordination chemistry（person_field 细分：coordination chemistry / inorganic chemistry / stereochemistry，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 理论承继 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arthur Rudolf Hantzsch | 师→生（博士导师） | infobox 博士导师 |
| advisor-student | Marcellin Berthelot | 师→生（博士后指路人） | infobox 并列博士导师；正文对应 1890–92 巴黎博士后经历 |
| influence | Richard Abegg | Werner → Abegg | Abegg 1904 年基于其配位/价键观点提出 Abegg's rule |
| spouse | Emma Werner | 无向 | 其妻（infobox） |

> 禁入库名单：Gilbert N. Lewis（经 Abegg 间接承继，非直接关系）；法兰克福物理学会（机构非人物）；page.md 与 metadata.json 均无 Werner 的 doctoral_student 条目（本人页面无载，本批不建学生关系）。**库内既有入边**：Paul Karrer→Werner 的 advisor-student（Karrer yaml 所建，Karrer 1911 年苏黎世大学 PhD 导师为 Werner）——非本批产生，保留不动。Berthelot 同时是 Paul Sabatier 的博士导师（同一批次入库，对手方名用规范全名 Marcellin Berthelot 防分裂）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1913，独享；首位获奖的无机化学家，1973 年前唯一）
- Honorary member of the Physics Association（Frankfurt am Main, Germany）——frontmatter 载
- 诺贝尔演讲：1913-12-11《On the Constitution and Configuration of Higher-Order Compounds》

## 9. 机构清单

- 教育：Swiss Federal Institute / ETH Zurich（本科学业）；University of Zurich（1890 博士）
- 任职：ETH Zurich 教师（1892 起）；University of Zurich 教授（1893 起，1895 晋正教授）
- 其他：1914 hexol 论文；苏黎世精神病院去世（1919）
- 备注：page.md 与 metadata.json 均无本科生源中学信息——禁写

## 10. 终审清单

- [ ] 生卒 1866-12-12 / 1919-11-15，享年 52，出生地 Mulhouse、去世地苏黎世精神病院
- [ ] 1913 独享表述准确；获奖理由只用页面口径、不杜撰官方全句
- [ ] 1893 结构 / 1904 教科书 / 1914 hexol 年份准确；绿 trans / 紫 cis 颜色对应正确
- [ ] 双博士导师（Hantzsch + Berthelot）并列口径正确；ETH 博士授予问题表述准确
- [ ] Abegg 1904 / Lewis 1916 间接承继链正确；Lewis 不入库
- [ ] 死因如实（动脉硬化 + 酗酒过劳 + 精神病院），不渲染
- [ ] 无引语杜撰（全文页面无直接引语）；"第一"断言均有页面明载
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Alfred_Werner/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（c. 1915 照）；404 用装饰圆占位并注明
- [ ] **国籍**：封面顶部明示「生于法国阿尔萨斯 · 瑞士籍」
- [ ] **引语核对**：全文无直接引语（页面无载）——如有引号内容须改为间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾；本文件由 chem-batch-01 agent 维护。
> **最重要的事：每写一页就 make，看到溢出就修。**
