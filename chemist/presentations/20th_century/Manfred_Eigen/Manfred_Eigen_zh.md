# Manfred Eigen（曼弗雷德·艾根）立传提示词

> qid=Q76600 · 1927-05-09 – 2019-02-06 · 德国生物物理化学家 · 20 世纪 · 诺贝尔化学奖（1967，与 Norrish、Porter 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Manfred_Eigen/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 黄金参照**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠ 肖像说明：本地 `images.txt` 仅含 1983 年荷兰女王 Beatrix 与五位诺奖得主合影（Eigen 在列）——**非个人标准肖像**；回退方案：经 Wikipedia REST API `page/summary` 查 infobox 原图名后用 `Commons Special:FilePath/<文件名>?width=600` 下载（curl -A "Mozilla/5.0" + file 验证）；404 则装饰圆占位，禁用合影裁剪充当肖像。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 把化学反应拍成快照的人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「脉冲—弛豫」母题——扰动之后的涟漪回稳，即弛豫法的物理图像。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Manfred Eigen（中文惯称：曼弗雷德·艾根）
- **生卒**：1927-05-09 生于德国波鸿 → 2019-02-06 逝于格丁根，享年 91
- **国籍**：Germany（德国）
- **身份**：生物物理化学家（biophysical chemist；兼物理学家）
- **家庭**：父 Ernst Eigen 为室内乐音乐家（chamber musician），母 Hedwig（娘家姓 Feld）；幼年深爱音乐、学钢琴。首任妻 Elfriede Müller，育一子一女；后娶 Ruthild Winkler-Oswatitsch——长期科学伙伴
- **教育轨迹**：
  - Gymnasium am Ostring（波鸿）；二战中断学业
  - 1945 徒步抵达格丁根：无入学证件，经考试证明学识后被录取——格丁根大学战后第一届学生
  - 想学物理，因复员军人优先改读地球物理学（Geophysics），本科毕业后转自然科学研究生
- **导师**：Arnold Eucken（博士导师，1951）；研究生阶段顾问之一为 Werner Heisenberg
- **博士**：1951，《Ermittlung der molekularen Struktur reiner Flüssigkeiten und Lösungen aus thermischen und kalorischen Eigenschaften》（由纯液体与溶液的热学、量热学性质确定其分子结构）
- **研究领域**：biophysical chemistry——快速化学反应动力学（弛豫法）、生命起源与分子演化（准种、超循环）、演化生物技术

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **音乐家之子（1927）**：波鸿室内乐手的儿子——终生的钢琴与音乐修养，科学之外的第二语言。
2. **战火中的少年（1942–1945）**：15 岁被征入德军高射炮部队；战争尾声被美军俘虏后逃脱（他后来说逃跑相对容易），徒步数百公里横穿战败的德国，1945 年抵达格丁根。
3. **战后第一届大学生**：无证件、凭考试入学；想学物理因老兵优先改地学——人生的第一次"弛豫"。
4. **博士（1951）**：师从 Arnold Eucken；Heisenberg 是顾问之一。
5. **马普研究所（1953–）**：入职格丁根马普物理化学研究所，1964 年任所长。
6. **弛豫法与温度跳变**：提出 relaxation methods（temperature jump method）——瞬间扰动平衡体系，追踪其弛豫回稳，从而测量过去"测不到"的快反应。
7. **纳秒世界（1964）**：在伦敦法拉第学会会议上首次证明：可以测定纳秒量级时间间隔内发生的化学反应速率。
8. **研究所整合（1964）**：任所长后推动物理化学所与光谱学所合并为**马普生物物理化学研究所**。
9. **1967 诺贝尔化学奖**：与 Ronald George Wreyford Norrish、George Porter 共享——"for their studies of extremely fast chemical reactions induced in response to very short pulses of energy"（页面明载 citation 句）；获奖方向是弛豫法（Norrish/Porter 是闪光光解）；诺奖演讲 *Immeasurably Fast Reactions*（1967-12-11）。
10. **生命起源纲领（1971–）**：发表 *Selforganization of matter and the evolution of biological macromolecules*；创立 quasispecies（准种）理论、error threshold（错误阈值）/ error catastrophe 概念、Eigen's paradox（艾根悖论）。
11. **超循环（1977）**：与 Peter Schuster 描述 hypercycle——反应环的循环耦合，解释前生物系统的自组织。
12. **演化生物技术之父**：其工作"被誉为开创了一个新的科技学科：evolutionary biotechnology"；创办 Evotec 与 Direvo 两家生物技术公司；1982–1993 任德国国家奖学金基金会（German National Merit Foundation）主席；《原子科学家公报》赞助委员会成员。
13. **荣誉与晚年**：Otto Hahn Prize（1962）、美国艺术与科学院（1964）、美国国家科学院（1966）、美国哲学学会（1968）、苏联科学院（1976）、ForMemRS（1973）、Pour le Mérite（1973）、Faraday Lectureship（1977）、下萨克森州奖（1980）、Paul Ehrlich 奖（1992）、Helmholtz 奖章（1994）、Wilhelm Exner 奖章（2011）、15 个荣誉博士；无神论者却是教皇科学院成员；2019-02-06 逝于格丁根。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松绿 deeppine） | `#175E54` | 弛豫回稳的深绿——从纳秒快反应到生命演化的时间纵深（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（弛豫法 badgeRelax） | `#1E4E79` | 蓝 temperature jump / 弛豫时间 |
| 分类色 2（快反应 badgeFast） | `#C0392B` | 红 纳秒速率 / 1967 诺奖 |
| 分类色 3（分子演化 badgeEvo） | `#1B7A43` | 绿 准种 / 超循环 / Eigen 悖论 |
| 分类色 4（马普与学院 badgeInst） | `#6B4C9A` | 紫 马普生物物理化学研究所 / 各国科学院 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「脉冲—弛豫」——扰动后的涟漪一圈圈回稳。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（`music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`；不要复制 wav 文件，make video 时引用路径）
- **风格**：强烈 / 紧张 / 竞速感
- **匹配理由**：
  - "Savage" 的爆发力匹配研究对象——皮秒纳秒级的化学"竞速"，把快反应逼到时间显微镜下
  - 紧张感匹配少年时代的战火徒步——15 岁穿越战败德国的求生行旅
  - 后段余韵留给生命起源的宏大叙事——从快反应到四十亿年演化的时间反差
- **时长**：以文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，Sanger 同构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把化学反应拍成快照的人 / Manfred Eigen 1927–2019 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  艾根的一生 — 高斯式时间线（10 节点：1927→1945→1951→1953→1964→1967→1971→1977→1982→2019）
04  音乐之子与战火童年 (1927–1945) — 表格「时间|事件|结果」（高射炮部队/被俘逃脱/徒步至格丁根）
05  战后格丁根与博士 (1945–1951) — 表格（考试入学/改地学/Eucken/Heisenberg 顾问之一）
06  弛豫法 (1953–1964) — 表格「问题|方法|结果」+ 公式框：温度跳变后体系按 τ 弛豫回稳（示意）
07  纳秒世界 (1964) — 表格 + 公式框：法拉第学会报告——首次测得纳秒级反应速率
08  1967 诺贝尔化学奖 — 三人共享；citation 原句 + 诺奖演讲 Immeasurably Fast Reactions（1967-12-11）
09  马普生物物理化学研究所 — 表格「阶段|事件|结果」（1953 入所/1964 所长/两所合并）
10  生命起源：准种与错误阈值 (1971–) — 表格 + 公式框：准种/错误阈值/Eigen 悖论（概念框，勿页外展开）
11  超循环 (1977) — 与 Peter Schuster；前生物自组织的环耦合示意（概念框）
12  演化生物技术 — Evotec / Direvo / 德国国家奖学金基金会主席（1982–1993）
13  荣誉与晚年 — 高斯式「类别|代表|意义」表格（15 荣誉博士/Pour le Mérite/ForMemRS）+ 2019 逝于格丁根
14  结尾 — 「先扰动，再看它如何回到平衡——这就是测量时间的方法。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1967 共享口径 | Eigen 以**弛豫法**（temperature jump）获奖；Norrish/Porter 以**闪光光解**获奖——三人获奖方向勿互换；citation 共同理由用页面原句 |
| citation 原句 | "for their studies of extremely fast chemical reactions induced in response to very short pulses of energy"——仅此句可引；页面奖项条目的另一表述（kinetics … with relaxation methods）是叙述非 citation 原文 |
| Heisenberg 身份 | 是研究生阶段"顾问之一（one of his advisors）"——博士导师是 Arnold Eucken；勿写"Heisenberg 的学生" |
| 改读地学 | 因**复员军人优先**改读地球物理——勿写"被物理系拒绝" |
| 战时经历 | 15 岁入高射炮部队、被美军俘虏、逃脱、徒步数百公里至格丁根（1945）——按页面实载，禁加未载细节 |
| 概念群 | quasispecies / error threshold / error catastrophe / Eigen's paradox / hypercycle 各为独立概念勿混；hypercycle 是 1977 与 Peter Schuster 共同描述 |
| Known for 名词 | Eigen cation（水合氢离子溶剂化相关）、Eigen-Wilkins mechanism、diffusion-limited enzyme 仅在 infobox Known for 列名，本地正文无展开——PPT 只列名词禁展开页外细节 |
| 两任妻 | Elfriede Müller（一子一女）→ Ruthild Winkler-Oswatitsch（长期科学伙伴）——先后关系，勿写成同时或漏写其一 |
| 宗教 | 无神论者却是教皇科学院成员——页面原载并置，勿演绎其宗教立场 |
| 荣誉博士 | 页面明载"15 honorary doctorates"且列表恰 15 行——勿夸大数目 |
| 博士生 | 正文 infobox 仅 Geoffrey Hoffmann 一人；Katja Nieselt-Struwe、Christoph Mayer、Petra Schwille 仅 metadata.json 有载——**不予入库**，PPT 禁写 |
| 去世 | 2019-02-06 逝于格丁根，享年 91——页面未载死因，禁编 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76600 | ✅ |
| name_zh | 曼弗雷德·艾根 | ✅ |
| name_en | Manfred Eigen | ✅ |
| birth_date | 1927-05-09 | ✅ |
| death_date | 2019-02-06 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | biophysical chemist | ✅ |
| field_of_work | chemical kinetics（person_field 细分：chemical kinetics / biophysics / origin of life / evolutionary biotechnology，带 rank） | ✅ |
| has_biography | false（立传 Beamer 完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 frontmatter 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arnold Eucken | 师→生 | 博士导师，1951 格丁根博士 |
| advisor-student | Werner Heisenberg | 师→生 | 研究生阶段顾问之一（one of his advisors） |
| advisor-student | Geoffrey Hoffmann | Eigen→学生 | 正文 infobox doctoral student |
| co-honored | Ronald George Wreyford Norrish | 无向 | 1967 诺贝尔化学奖共同得主 |
| co-honored | George Porter | 无向 | 1967 诺贝尔化学奖共同得主 |
| colleague | Peter Schuster | 无向 | 1977 共同描述超循环（hypercycle） |
| spouse | Elfriede Müller | 无向 | 首任妻，育一子一女 |
| spouse | Ruthild Winkler-Oswatitsch | 无向 | 第二任妻，长期科学伙伴 |

> **metadata-only 禁入库名单**：Katja Nieselt-Struwe、Christoph Mayer、Petra Schwille（doctoral_student 仅 metadata.json，正文 infobox 无）——不予入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1967，与 Norrish、Porter 共享）
- Otto Hahn Prize（1962）
- American Academy of Arts and Sciences（1964 当选）
- United States National Academy of Sciences（1966 当选）
- American Philosophical Society（1968 当选）
- Soviet Academy of Sciences（1976，今俄罗斯科学院）
- Foreign Member of the Royal Society，ForMemRS（1973）
- Pour le Mérite（1973）
- Faraday Lectureship Prize（1977，英国皇家化学会）
- Austrian Decoration for Science and Art
- Lower Saxony State Prize for Science（1980）
- Paul Ehrlich and Ludwig Darmstaedter Prize（1992）
- Helmholtz Medal（柏林-勃兰登堡科学院，1994）
- Max Planck Research Award（1994，与 Karolinska 研究所 Rudolf Rigler 共同）
- Wilhelm Exner Medal（2011）
- 15 个荣誉博士（1966 Harvard / Washington Univ. St. Louis / Chicago；1968 Nottingham；1973 Hebrew Univ. Jerusalem；1976 Hull；1978 Bristol；1982 Debrecen / Cambridge；1983 TU Munich；1985 Bielefeld；1990 Utah State / Alicante；2007 Coimbra；2011 Scripps）
- Ruhr University Bochum 荣誉会员（2001）；Institute of Human Virology 终身成就奖（2005）

## 9. 机构清单

- 教育：Gymnasium am Ostring（波鸿）；University of Göttingen（战后首届；PhD 1951）
- 任职：Max Planck Institute for Physical Chemistry（格丁根，1953 入所，1964 任所长）→ 两所合并为 Max Planck Institute for Biophysical Chemistry；Braunschweig University of Technology 荣誉教授
- 社会任职：German National Merit Foundation 主席（1982–1993）；The Bulletin of the Atomic Scientists 赞助委员会成员；教皇科学院成员
- 创业：Evotec、Direvo 两家生物技术公司创始人

## 10. 终审清单

- [ ] 生卒 1927-05-09 / 2019-02-06，享年 91，出生地波鸿、去世地格丁根
- [ ] 1967 三人共享表述准确；Eigen=弛豫法、Norrish/Porter=闪光光解，方向不混
- [ ] citation 原句逐字与页面一致；诺奖演讲日期 1967-12-11
- [ ] 博士导师 Eucken；Heisenberg 仅"顾问之一"；改读地学原因=复员军人优先
- [ ] 概念群（准种/错误阈值/悖论/超循环）各自独立表述，hypercycle 归 1977 与 Schuster
- [ ] 两任妻先后关系准确；博士生仅 Geoffrey Hoffmann
- [ ] 引语核对：citation 句之外，任何引号文本必须在 page.md 溯源，否则改间接转述
- [ ] 正文采用 Sanger 同构：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Manfred_Eigen/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：REST API 回退下载结果核对（非合影裁剪）；404 则装饰圆占位并在 §0 注记
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：任何引号文本必须在 Wikipedia 原文找到（citation 原句为准绳）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt / hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger/Fischer 等）及同批 Norrish/Porter 篇章口径一致（三人互指一致）
