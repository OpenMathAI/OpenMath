# William Standish Knowles（威廉·斯坦迪什·诺尔斯）立传提示词

> qid=Q110947 · 1917-06-01 – 2012-06-13 · 美国化学家 · 21 世纪 · 诺贝尔化学奖（2001，与 Noyori 共享半奖；另一半 Sharpless）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/William_Standish_Knowles/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框。本地 images.txt **无单人肖像**（仅氢化反应图 Hydrogenation-Knowles1968.png 与 L-DOPA 合成路线图）——封面用**装饰圆占位**（主色渐变 + 姓名缩写 WSK），反应图作第 06/07 页插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace\ 手性催化的工业先驱\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（Harvard AB / Columbia PhD）、博士导师、任职机构、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「手性 / 镜像」母题——成对出现的对称圆点暗示对映异构体的镜像关系。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——如 15% ee 数值框、DIPAMP/L-DOPA 反应路线框。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：William Standish Knowles（中文惯称：威廉·斯坦迪什·诺尔斯）
- **生卒**：1917-06-01 生于美国马萨诸塞州 Taunton → 2012-06-13 逝于密苏里州 Chesterfield（圣路易斯郊区），享年 95
- **国籍**：United States（美国）
- **身份**：化学家（chemist；任职于工业界 Thomas and Hochwalt Laboratories / Monsanto Company）
- **家庭**：妻 Nancy——结婚 66 年，四子女 Elizabeth、Peter、Sarah、Lesley，四个孙辈；退休后住在妻子继承的 100 英亩农场，恢复本地草原植被；夫妻生前约定去世后把农场捐出改建为城市公园
- **教育轨迹**：
  - Berkshire School（Sheffield, Massachusetts）：学业全班第一，毕业后入 Harvard
  - 自觉年纪太小，先入 Phillips Academy（Andover）读一年预科——获第一个化学奖：学校 50 美元 Boylston Prize
  - Harvard University：化学主修（聚焦有机化学），1939 年 AB 学位
  - Columbia University：研究生院，1942 年 PhD
- **导师**：Robert Elderfield（博士导师）
- **博士论文**：1942，《A preliminary investigation of the constituents of Astragalus wootoni. Β-substituted-Δα, Β-butenolides of the naphthalene, indene and norcholane series》——黄芪属植物成分与烯醇内酯系列（**与氢化无关**）
- **研究领域**：化学——不对称氢化、手性膦配体催化、对映选择性合成、L-DOPA 工业生产

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **Taunton 之子（1917）**：生于马萨诸塞州 Taunton，新英格兰求学路线。
2. **预科一年与第一个奖（约 1935）**：自觉太小不上大学，Phillips Academy 一年——50 美元 Boylston Prize 是他人生第一个化学奖。
3. **Harvard 化学本科（1935–1939）**：主修化学、聚焦有机化学，1939 年毕业。
4. **Columbia 博士（1939–1942）**：师从 Robert Elderfield，论文是天然产物成分研究（Astragalus wootoni 成分 + 萘/茚/甾族系列烯醇内酯）。
5. **工业界化学家**：入职 Thomas and Hochwalt Laboratories（Monsanto Company）——与多数诺奖得主不同，他的获奖工作在**工业实验室**完成。
6. **改造 Wilkinson 催化剂（1968）**：把非手性的三苯基膦配体换成**手性膦配体**，做出最早的不对称氢化催化剂之一——对映选择性合成有效，但 ee 只有适度的 **15%**。
7. **DIPAMP 与 L-DOPA**：在 Monsanto 开发 DIPAMP 配体的不对称氢化步骤，用于生产帕金森病药物 L-DOPA——**首个把对映选择性金属催化推向工业规模**的应用。
8. **氢化 vs 氧化的三分格局（2001）**：2001 诺贝尔化学奖——他与 Noyori **平分一半**（手性催化氢化反应），另一半给 Sharpless（催化不对称氧化）。
9. **官方获奖理由**：英文原文 "for their work on chirally catalysed hydrogenation reactions"。
10. ** Chemical Pioneer Award（1983）**：美国化学家学会（American Institute of Chemists）授予，诺奖前的业界认可。
11. **退休与草原（1986）**：1986 年退休，定居 Chesterfield；在 100 英亩农场上恢复本地草原草种。
12. **66 年婚姻与公园之约**：与 Nancy 结婚 66 年；夫妻约定身后把农场捐作城市公园——科学家身后仍在回馈社区。
13. **迟来的致敬（2008）**：圣路易斯科学院 Peter H. Raven Lifetime Achievement Award；2012-06-13 逝于 Chesterfield，享年 95。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#1E3A5F` | 工业化学的严谨与深度（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（不对称氢化 badgeHydro） | `#2E5A9E` | 蓝手性膦配体 / 15% ee |
| 分类色 2（L-DOPA 工业 badgeDopa） | `#1B7A43` | 绿 DIPAMP / 工业生产 |
| 分类色 3（诺贝尔 badgeNobel） | `#D97B29` | 琥珀 2001 获奖理由 |
| 分类色 4（遗产 badgeLegacy） | `#C0395B` | 玫瑰手性药物 / 草原农场 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「手性 / 镜像」的成对对称关系。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`；**不要复制 wav 文件，Makefile 直接引用该路径**）
- **风格**：开阔 / 探索 / 稳步前行
- **匹配理由**：
  - "新大陆" 匹配其贡献本质——把手性催化从学术实验室带入**工业新大陆**（L-DOPA 规模化生产是史上首次）
  - "开阔" 匹配其工业化学家气质——不在象牙塔，而在工厂车间里改变制药业
  - "稳步前行" 匹配其叙事节奏——预科一年 → Harvard → Columbia → Monsanto → 三十年磨一剑 → 2001 诺奖
- **时长核对**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 手性催化的工业先驱 / William Standish Knowles 1917–2012 + 四色 badge + 右上装饰圆头像 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/机构/领域/荣誉）
03  Knowles 的一生 — 时间线（10 节点：1917→Phillips/Boylston→1939 Harvard→1942 Columbia→Monsanto→1968 手性膦→L-DOPA→1983→2001 诺奖→2012）
04  早年与求学 (1917–1942) — 表格「时间|事件|结果」（Berkshire/Phillips/Harvard/Columbia）
05  Monsanto：工业实验室里的化学家 — 表格「阶段|工作|意义」
06  1968：手性膦配体改造 Wilkinson 催化剂 — 表格「问题|方法|结果」+ 公式框：手性膦替换三苯基膦 · 15% ee
07  DIPAMP 与 L-DOPA 工业合成 — 表格「问题|方法|结果」+ 公式框：DIPAMP 不对称氢化 → L-DOPA（插图 L-dopaSyn）
08  2001 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框：官方英文获奖理由
09  氢化 vs 氧化：2001 的三分格局 — 表格「方向|代表人物|贡献」（Knowles+Noyori 氢化 / Sharpless 氧化）
10  晚年与家庭 — 表格「主题|事实|意义」（1986 退休 / 66 年婚姻 / 草原农场捐作公园）
11  荣誉与致敬 — 「类别|代表|意义」表格 + itemize（1983 Chemical Pioneer / 2001 Nobel / 2008 Raven 奖）
12  遗产：不对称催化的工业时代 — 四分类遗产盒 + 公式框：手性药物合成的开端
13  （备用扩展页）从 15% ee 到制药工业 — 表格「阶段|突破|影响」（按 page.md 实载展开，无载内容禁写）
14  结尾 — 「手性世界的第一扇工业之门，由一位工业实验室的化学家推开。」
```

> 页面内容较短时（13 页备用页），**以 page.md 实载为准，严禁脑补**；无足够实载就砍掉备用页并保持 15 页总数由其余页承担（需在 Review 时确认）。

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | 官方英文 "for their work on chirally catalysed hydrogenation reactions"（他与 Noyori 共享的半奖）；勿泛化成「发明不对称合成」 |
| 奖项分配 | 页面口径：Knowles 与 Noyori **平分一半**，另一半给 Sharpless（氧化反应）——勿写「三人平分」或「Knowles 独得一半」 |
| Sharpless 份额 | Sharpless 的另一半是「催化不对称氧化的发展」（development of a range of catalytic asymmetric oxidations）——勿并入氢化理由 |
| 15% ee | 首个催化剂 ee 仅 **modest 15%**——勿夸大效率；「有效」指 proof of concept |
| DIPAMP/L-DOPA | 「首个工业规模对映选择性金属催化应用」为页面明载（"first to apply enantioselective metal catalysis to industrial-scale synthesis"）——可写；但勿延伸写「手性药物时代开启」之类页面无载的宏大断言 |
| Wilkinson 催化剂 | 是**催化剂名称**（以人名命名），非个人关系——禁写与 Wilkinson 本人有师承/同事/合作 |
| 博士论文 | 论文是 Astragalus wootoni 成分与烯醇内酯——勿写成氢化/催化相关 |
| 妻子姓名 | 页面仅写 "his wife, Nancy"——**无姓氏与全名**，勿编造 |
| 享年 | 1917-06-01 → 2012-06-13，享年 95——勿写错卒日（06-13 非 06-12） |
| 入库名规范 | 页面行文作 "K. Barry Sharpless"，**入库对手方名用 Karl Barry Sharpless**；Noyori 入库名用 Ryōji Noyori（库内 #3511 形式） |
| 页面较薄 | 本地 page.md 无童年家庭细节、无研究生轶事、无引语原话——**全文不得出现中文引号内的"原话"**，一律间接转述 |
| metadata 噪声 | frontmatter award_received 含 "ACS Award for Creative Invention"，正文 Awards 节**未列**——§8 只作存疑注记，勿当实载荣誉展开 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110947 | ✅ |
| name_zh | 威廉·斯坦迪什·诺尔斯 | ✅ |
| name_en | William Standish Knowles | ✅（新建记录） |
| birth_date | 1917-06-01 | ✅ |
| death_date | 2012-06-13 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | asymmetric hydrogenation | 不对称氢化 |
| 1 | asymmetric catalysis | 不对称催化 |
| 2 | enantioselective synthesis | 对映选择性合成 |
| 3 | pharmaceutical process chemistry | 药物工艺化学 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Elderfield | 师→生（博士导师） | 哥伦比亚大学博士导师（1942 论文） |
| spouse | Nancy | 无向 | 结婚 66 年，四子女；约定身后捐赠农场建城市公园 |
| co-honored | Ryōji Noyori | 无向 | 2001 诺贝尔化学奖共同得主（共享手性催化氢化半奖） |
| co-honored | Karl Barry Sharpless | 无向 | 2001 诺贝尔化学奖（Sharpless 得另一半·不对称氧化） |

> **禁入库名单**：metadata.json 无额外人物关系；正文提到的 Wilkinson's catalyst 为催化剂名称非人物；四名子女（Elizabeth/Peter/Sarah/Lesley）与孙辈不入库（仅亲属罗列，无学术关系实载）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2001，与 Noyori 共享半奖；另一半 Sharpless）
- Chemical Pioneer Award（1983，American Institute of Chemists）
- Peter H. Raven Lifetime Achievement Award（2008，Academy of Science, St. Louis）
- Boylston Prize（Phillips Academy 就读期间，学校 50 美元奖——人生第一个化学奖）
- （存疑注记：frontmatter 另列 "ACS Award for Creative Invention"，正文未展开——不单独成页）

## 9. 机构清单

- 教育：Berkshire School（Sheffield, MA）→ Phillips Academy（Andover，预科一年）→ Harvard University（AB 1939）→ Columbia University（PhD 1942）
- 任职：Thomas and Hochwalt Laboratories（Monsanto Company）；1986 年退休，定居密苏里州 Chesterfield

## 10. 终审清单

- [ ] 生卒 1917-06-01 / 2012-06-13，享年 95，出生地 Taunton、去世地 Chesterfield
- [ ] 2001 表述：与 Noyori 平分一半（氢化）、Sharpless 另一半（氧化）；获奖理由英文原文准确
- [ ] 15% ee 与 "modest" 限定词保留；L-DOPA "first industrial-scale" 表述忠实页面
- [ ] 博士论文主题（Astragalus/烯醇内酯）不被误写为催化研究
- [ ] 全文无中文引号内无溯源"原话"（Knowles 页面无直接引语）
- [ ] 入库对手方名：Ryōji Noyori / Karl Barry Sharpless（规范全名）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/William_Standish_Knowles/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无单人肖像——确认装饰圆占位样式统一、反应插图清晰
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：Knowles 页面无直接引语——全文不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2001 批次（Noyori / Sharpless 篇）的获奖格局表述交叉一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
