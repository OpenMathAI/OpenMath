# Paul D. Boyer（保罗·博耶）立传提示词

> qid=Q102395 · 1918-07-31 – 2018-06-02 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1997，与 Walker 共享一半）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Paul_D._Boyer/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 为空（页面注明 "Boyer in 2016" 但无 URL）：先经 Wikipedia REST API `page/summary` 查 infobox 实际文件名下载，404 则用装饰圆占位（图注须如实）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 解码生命的能量货币\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「ATP / 能量货币」母题——圆点暗示旋转催化亚基与磷酸基团的循环。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 `ADP + Pi → ATP`（结合变化机制：能量输入主要用于促进 Pi 结合与紧密结合的 ATP 释放，而非直接合成 ATP）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul Delos Boyer（中文惯称：保罗·德洛斯·博耶；UCLA 化学与生物化学教授）
- **生卒**：1918-07-31 生于犹他州 Provo（美国）→ 2018-06-02 逝于洛杉矶家中（呼吸衰竭；差不到两个月满 100 岁），享年 99
- **国籍**：United States（美国）
- **身份**：生物化学家、分析化学家（UCLA 教授；1997 诺贝尔化学奖得主；**首位犹他州出生的诺贝尔奖得主**——页面明载）
- **家庭**：出生于不实践的摩门教家庭（荷兰、德国、法国、英国血统）；1939 年赴威斯康星前五天娶 Lyda Whicker，婚姻近 80 年——**页面称其为"结婚最久的诺贝尔奖得主"**；育三子。在威斯康星接触摩门社区但自称"走在歧途边缘"，经唯一神教派试验后最终成为无神论者；2003 年为 22 位签署 Humanist Manifesto 的诺奖得主之一
- **教育轨迹**：
  - Provo High School（学生会活跃分子、辩论队、致告别辞的毕业生代表、校内外篮球）
  - Brigham Young University（化学 BS 1939）
  - Wisconsin Alumni Research Foundation 奖学金赴威斯康星读研
  - University of Wisconsin–Madison（生物化学 PhD 1943）
- **导师**：**页面未载博士导师姓名——禁写**
- **博士**：1943，生物化学（University of Wisconsin–Madison）
- **研究领域**：生物化学、酶学机理（动力学/同位素/化学方法）、ATP 合酶结合变化机制、分子生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **犹他少年（1918–1939）**：Provo 高中的辩论队与毕业生代表；BYU 化学 BS——1939 年带着奖学金与新娘奔赴威斯康星。
2. **近乎 80 年的婚姻（1939–2018）**：出发前五天娶 Lyda Whicker；页面称其为结婚最久的诺贝尔奖得主——她后来还是 UCLA 职业编辑，助其编 *The Enzymes* 丛书。
3. **战时血清白蛋白（1943–1945）**：PhD 后在 Stanford 参与战时输血用血清白蛋白稳定化研究。
4. **明尼苏达独立起步（1945–1963）**：引入动力学、同位素与化学方法研究酶机理——现代酶学方法论的一块基石。
5. **斯德哥尔摩访学（1955）**：Guggenheim Fellowship 赴瑞典与 Hugo Theorell 合作研究醇脱氢酶机理（Theorell 为 1955 年诺贝尔生理学或医学奖得主）。
6. **学术服务两任（1959–1970）**：ACS 生物化学分会主席（1959–60）；美国生物化学家学会主席（1969–70）。
7. **UCLA 与分子生物学研究所（1963–1990）**：1963 年任 UCLA 化学与生物化学教授；1965 年创建分子生物学研究所并任首任所长，主持大楼建设与跨系博士项目。
8. **编辑生涯（1963–1990）**：*Annual Review of Biochemistry* 编辑/副编辑（1963–89）；经典丛书 *The Enzymes* 主编（infobox 口径 1971–90）——由妻子 Lyda 协助编辑。
9. **ATP 合酶三假说（核心贡献）**：①能量输入主要用于促进磷酸结合、尤其是释放紧密结合的 ATP，而非直接用于合成 ATP；②三个相同的催化位点经历强制性顺序结合变化；③环形排列的催化亚基之结合变化由较小的内部亚基旋转驱动——**结合变化机制**。
10. **同位素交换证据**：18O 交换反应研究（ATP 酶催化）——页面 Publications 节实载其 18O-exchange 方法路线，可作方法学佐证页素材。
11. **1997 诺贝尔化学奖**：与 John E. Walker 共享一半（"for research on the 'enzymatic mechanism underlying the biosynthesis of adenosine triphosphate'"——引号内短语为页面实载官方口径）；另一半授予丹麦化学家 Jens Christian Skou（Na+/K+-ATPase 的发现）——**勿写成三人平等共享同一工作**。
12. **诺奖演讲（1997-12-08）**：题为 "Energy, Life, and ATP"（页面外部链接实载）——可作结尾页引语性素材。
13. **近乎百岁的谢幕（2018）**：呼吸衰竭逝于洛杉矶家中，99 岁、差不到两个月满百——与 1939 年的婚姻一样，跨越了一个世纪。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（ATP 深红 energyred） | `#7A1E28` | 生命能量货币与百年长旅的深红（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（酶学方法 badgeEnzyme） | `#1E4E79` | 蓝动力学 / 同位素 / 化学方法 |
| 分类色 2（ATP 机制 badgeATP） | `#B07A2A` | 琥珀结合变化机制 / 旋转催化 |
| 分类色 3（机构与编辑 badgeUCLA） | `#5B2A86` | 紫 UCLA / MBI / The Enzymes |
| 分类色 4（荣誉与谢幕 badgeHonor） | `#1E5631` | 绿诺奖 1997 / Seaborg 奖章 1998 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「ATP 循环 / 旋转催化」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（清单指定，文件 `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；不要复制 wav 文件）
- **风格**：深沉 / 追忆 / 纪念碑感
- **匹配理由**：
  - "深沉" 匹配其一生的长线坚持——同一条酶机理问题钻了半个多世纪
  - "追忆" 匹配纪念基调——99 岁谢幕、近 80 年婚姻，"Tragedy" 在此是挽歌式庄重而非悲情
  - "纪念碑感" 匹配其学术遗产——ATP 合酶三假说是写入教科书的精神纪念碑
- **时长**：以实际曲目时长为准，不足/超出由 ffmpeg `-shortest` 对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 解码生命的能量货币 / Paul D. Boyer 1918–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  博耶的一生 — Sanger 式时间线（10 节点：1918→1939→1943→1945→1955→1963→1965→1981→1997→2018）
04  犹他少年与 BYU (1918–1939) — 表格「时间|事件|结果」
05  威斯康星与战时研究 (1939–1945) — 表格「时间|事件|结果」（PhD 1943 / Stanford 血清白蛋白）
06  酶学方法论 (1945–1963) — 表格「对象|方法|结果」（动力学 / 同位素 / 化学方法；1955 Theorell 访学）
07  UCLA 与分子生物学研究所 (1963–1990) — 表格「举措|内容|结果」（MBI 1965 / Annual Review / The Enzymes）
08  ATP 合酶三假说 — 表格「问题|推理|结果」+ 公式框：ADP + Pi → ATP 结合变化机制
09  1997 诺贝尔化学奖 — 共享结构页（Boyer/Walker 半 + Skou 半）+ 公式框：官方口径 "enzymatic mechanism underlying the biosynthesis of ATP"
10  同位素交换证据 — 表格「问题|方法|结果」（18O 交换反应 / ATP 酶催化）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Pfizer 1955 → Nobel 1997 → Seaborg 1998）
12  学术服务与编辑生涯 — 流程图页（ACS 分会主席 1959-60 → ASBC 主席 1969-70 → MBI 首任所长 1965）
13  遗产：能量与生命 — 四分类遗产盒 + "Energy, Life, and ATP" 诺奖演讲题 + 首位犹他出生诺奖得主
14  结尾 — 「他证明了：生命不制造能量，生命释放能量。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1997 共享结构 | **Boyer 与 Walker 共享一半**（ATP 合酶酶学机理）、**Skou 独得另一半**（Na+/K+-ATPase）——勿写"三人共享同一奖项平分" |
| 官方 citation | 页面实载口径为 "for research on the 'enzymatic mechanism underlying the biosynthesis of adenosine triphosphate'"——引号内短语可引；整句如需扩展须 Review 时经 nobelprize.org 核对 |
| "首位犹他出生诺奖得主" | 页面明载（making Boyer the first Utah-born Nobel laureate）——**有页面依据的"第一"，可写** |
| "结婚最久的诺奖得主" | 页面明载（nearly eighty years... longest-married Nobel laureate）——同样有据可写 |
| 博士导师 | 页面**未载博士导师姓名**——身份信息页"师承"栏写"页面无载"，**严禁编造 Wisconsin 导师** |
| 两个编辑年份 | *Annual Review of Biochemistry* 编辑为 **1963–89**（正文）、*The Enzymes* 主编为 **1971–90**（infobox Known for）——两处对象不同勿混写 |
| 奖项名 | 1955 年奖页面作 **Paul-Lewis Award in Enzyme Chemistry**（括注即 Pfizer Award in Enzyme Chemistry）——两名为同一奖，照页面主用名 |
| Theorell 关系 | 1955 年 Guggenheim 赴瑞典与 **Hugo Theorell** 合作研究醇脱氢酶——是访学合作（colleague），勿写师生；Theorell 系 1955 诺贝尔生理学或医学奖得主 |
| 宗教轨迹 | 不实践的摩门家庭 → 威斯康星"歧途边缘"→ 唯一神教派试验 → 无神论者；2003 Humanist Manifesto 署名——页面明载可写，保持客观转述 |
| 死亡细节 | 2018-06-02 呼吸衰竭逝于**洛杉矶家中**，享年 99、差不到两个月满百岁——享年勿写 100 |
| 战时工作 | Stanford 是**战时相关项目**（输血用血清白蛋白稳定化）——勿写成普通博士后/教职 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102395 | ✅ |
| name_zh | 保罗·德洛斯·博耶 | ✅ |
| name_en | Paul D. Boyer | ✅ |
| birth_date | 1918-07-31 | ✅ |
| death_date | 2018-06-02 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / enzyme mechanism / bioenergetics / analytical chemistry，带 rank） | ✅ |
| has_biography | false（立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**同事 / 共同得主 / 配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Hugo Theorell | 无向 | 1955 年 Guggenheim 赴瑞典合作研究醇脱氢酶机理 |
| co-honored | John E. Walker | 无向 | 1997 诺贝尔化学奖共同得主（共享一半，ATP 合酶机理） |
| co-honored | Jens Christian Skou | 无向 | 1997 同年另一半得主（Na+/K+-ATPase 的发现） |
| spouse | Lyda Whicker | 无向 | 1939 年结婚近 80 年，协助编辑 The Enzymes |

> **禁入库名单（metadata.json-only 或防噪声）**：三名子女（页面未具名）；Norman N. Royall Jr.（母亲的启发者，非本人直接关系）；John E. Walker / Jens Christian Skou 之外的诺奖关联人物无；Stanford 战时项目无具名合作者可入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1997，与 Walker 共享一半；同年另一半授予 Skou）
- Paul-Lewis Award in Enzyme Chemistry / Pfizer Award in Enzyme Chemistry（1955）
- Guggenheim Fellowship（1955，赴瑞典）
- Fellow, American Academy of Arts and Sciences（1968）
- Member, National Academy of Sciences（1970）
- Stockholm University 荣誉博士（1974）
- McCoy Award, UCLA（1976）
- Tolman Award, ACS Southern California Section（1981）
- UCLA Faculty Research Lecturer（1981）
- William C. Rose Award, ASBMB（1989）
- University of Minnesota 荣誉博士（1996）
- Glenn T. Seaborg Medal, UCLA（1998）
- University of Wisconsin 荣誉博士（1998）
- Golden Plate Award, American Academy of Achievement（1998）
- Member, American Philosophical Society（1998）

## 9. 机构清单

- 教育：Provo High School → Brigham Young University（BS 1939）→ University of Wisconsin–Madison（PhD 1943）
- 任职：Stanford University（1943–45，战时血清白蛋白项目）→ University of Minnesota, St. Paul（1945–46）→ University of Minnesota, Minneapolis（1956–63，Hill Foundation 讲席）→ UCLA（1963–90，化学与生物化学教授；1990 退休口径以页面为准，页面作 1963–90 任职区间）
- 创建/服务：UCLA Molecular Biology Institute（1965 创建并任所长至 1983，infobox 口径 1965–83）；UC 大学系统生物技术研究与培训项目（1985–89）
- 编辑：*Annual Review of Biochemistry*（1963–89）；*The Enzymes* 丛书主编（1971–90）

## 10. 终审清单

- [x] 生卒 1918-07-31 / 2018-06-02，享年 99，出生地 Provo、去世地洛杉矶家中
- [x] 1997 共享结构（Boyer/Walker 一半 + Skou 一半）表述准确，未写成三人平分
- [x] "首位犹他出生诺奖得主"与"结婚最久的诺奖得主"两处均页面明载
- [x] 博士导师"页面无载"已注明；Theorell 为访学合作（勿写师生）
- [x] 两个编辑年份（Annual Review 1963–89 / The Enzymes 1971–90）未混淆
- [x] ATP 三假说逐条忠实页面表述；"Energy, Life, and ATP" 演讲题有据
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Paul_D._Boyer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 §0.1 回退处理（REST API → 装饰圆），图注如实
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：官方口径短语 "enzymatic mechanism underlying the biosynthesis of adenosine triphosphate" 须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐（对照 Frederick_Sanger_zh.tex）

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
