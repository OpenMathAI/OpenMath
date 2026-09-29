# Scipione del Ferro（斯皮奥内·德尔·费罗）立传提示词

> qid=Q318083 · 1465-02-06 – 1526-11-05 · 意大利数学家（博洛尼亚） · 16 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Scipione_del_Ferro/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**del Ferro 无真实肖像**（`images.txt` 仅数学公式 SVG，无肖像文件）——用装饰圆 `\faIcon{user}` 占位，图注注明「无存世肖像」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆占位）+ 右侧信息网格，至少含：生卒、国籍、出生地、教育、任职、主要成就、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「手稿 / 密写」的守密母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Scipione del Ferro（中文惯称：斯皮奥内·德尔·费罗）
- **生卒**：1465-02-06 生于博洛尼亚（Bologna，北意大利）→ 1526-11-05 逝于博洛尼亚，享年 61
- **国籍**：意大利（现代口径）；出生政权为 Lordship of Bologna / Papal States（教皇国）——历史政权见 §5 裁定
- **身份**：数学家、大学教师（博洛尼亚大学算术与几何讲师）、发明家（metadata occupation）
- **家庭**：父 Floriano Ferro（造纸业从业者，造纸业因 1450 年代印刷术的发明而兴起，可能因此使 del Ferro 早年得以接触各类书籍）；母 Filippa；他已婚并有一女，女随祖母名亦名 Filippa，嫁给数学家 Annibale della Nave
- **教育轨迹**：很可能就读于博洛尼亚大学（University of Bologna）；1496 年获聘博洛尼亚大学算术与几何讲师（lecturer in Arithmetic and Geometry）；晚年还从事商业事务
- **导师**：page.md 无载——**禁写导师**
- **研究领域**：数学（代数——缺二次项的三次方程、分数有理化、定角圆规几何）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **首解三次方程**：历史上第一个发现缺二次项的三次方程（depressed cubic，含 `x³+px=q` 与 `x³=px+q` 两类）解法的人。
2. **化归思想**：一般三次方程总可通过代换 `x=x'+a` 消去二次项，化为缺二次项型——这是他解题框架的前提。
3. **可能的推导路线**：今已确知其方法，据推测他从二次型恒等式 `x=√(a+√b)+√(a−√b)` 类比猜想三次对应式 `x=∛(a+√b)+∛(a−√b)` 成立，由此导出求解公式。
4. **求根公式**：即后世所称的卡尔达诺公式雏形 `∛(q/2+√(q²/4+p³/27)) + ∛(q/2−√(q²/4+p³/27))`。
5. **极端守密**：无任何著作存世——他拒绝发表，只向极少数亲友与学生展示。据信这是为防备当时数学家之间的公开挑战决斗（输了会失去资助或教席），把最强成果留作自卫武器。
6. **笔记本传承**：他有一本记录全部重要发现的笔记本；1526 年去世后由女婿兼学生 Annibale della Nave 继承，della Nave 并接替他在博洛尼亚大学的教席。
7. **1543 博洛尼亚之行**：Cardano 与其学生 Ferrari 专程赴博洛尼亚拜访 della Nave，见到了笔记本——其中载有缺二次项三次方程的解法。
8. **《大术》归名**：Cardano 在 1545 年《Ars Magna》中明确写道：**是 del Ferro 第一个解出三次方程**，书中给出的解法即 del Ferro 的方法——这是优先权的第一手书面证据。
9. **1925 Bortolotti 手稿**：1925 年 Ettore Bortolotti 发现的手稿载有 del Ferro 的方法，使他猜测 del Ferro 可能两类缺二次项方程都解出了。
10. **其他贡献**：分母含立方根和的分数有理化；用定角圆规研究几何问题（所知甚少）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（博洛尼亚赭红） | `#6E2B2B` | 博洛尼亚古城 / 15-16 世纪之交的厚重 |
| 强调色（手稿羊皮金） | `#C9A227` | 未发表的手稿笔记本 / 珍稀发现 |
| 分类色 1（三次方程 — 靛蓝） | `#2F4470` | 缺二次项三次方程 / 求根公式 |
| 分类色 2（守密文化 — 石板灰） | `#54626F` | 挑战决斗制度 / 守密策略 |
| 分类色 3（传承 — 深绿） | `#1B4D3E` | 笔记本 / della Nave / 《大术》归名 |
| 分类色 4（考据 — 琥珀） | `#B8860B` | 1925 Bortolotti 手稿发现 |
| 背景 | `#F7F5F2` | 浅米白（羊皮纸感） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「密写手稿 / 封存的笔记本」意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**PAST**（Alex-Productions，本地文件 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`）
- **风格定调**：**历史感 / 深沉 / 稳重**（15-16 世纪之交、守密一生的先行者）
- **匹配理由**：
  - del Ferro 是三次方程的**第一位**解法者，但其成果生前从未发表、身后才经手稿流传——「历史感 / 深沉」正匹配这种被时间掩埋又终被确认的首创者气质
  - 「稳重」匹配他博洛尼亚大学终身讲席的沉稳形象；曲目适合「人物回顾」型叙事，与本篇「首解—守密—手稿—归名」的回顾结构一致
  - 本组三人（del Ferro / Tartaglia / Cardano）分别用 PAST / Lonesome / Cinematic Experience，互不重复
- 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「三次方程的首解者 · 守密的博洛尼亚教授」+ Scipione del Ferro 1465–1526 + 右上装饰圆占位 + 国籍行（意大利）+ 底部三要素状态栏（意大利 | 博洛尼亚大学 | 首解缺二次项三次方程）+ 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右信息网格（生卒 / 国籍 / 出生地 / 教育 / 任职 / 主要成就 / 核心领域）
3. **德尔·费罗的一生：时间线**（`\timelineslide`）：1465 博洛尼亚出生 → 1496 博洛尼亚大学算术与几何讲师 → （解出缺二次项三次方程，日期无载禁编）→ 1526-11-05 去世，笔记本传女婿 della Nave → 1543 Cardano/Ferrari 博洛尼亚之行 → 1545《大术》归名
4. **早年与博洛尼亚**（`\earlyslide`）：造纸业之父与印刷术时代、博洛尼亚大学、1496 讲席、晚年商业事务
5. **三次方程问题**（核心贡献页，表格 + 公式框）：Pacioli 在《Summa》宣称三次方程不可解激发学界兴趣；一般三次方程经 `x=x'+a` 代换化为缺二次项两类 `x³+px=q` 与 `x³=px+q`
6. **首解与可能的路线**（核心贡献页，表格 + 公式框）：二次恒等式到三次猜想的类比、求根公式 `∛(q/2+√(q²/4+p³/27))+∛(q/2−√(q²/4+p³/27))`
7. **守密文化与挑战决斗**（`\contextslide`，表格）：无存世著作、只向少数亲友学生展示、挑战决斗制度（败者失去资助或教席）、留一手自卫的理性计算
8. **笔记本的传承**（核心贡献页，表格）：della Nave（学生兼女婿）继承笔记本并接任教席
9. **1543 博洛尼亚之行与《大术》**（核心贡献页，表格）：Cardano 与 Ferrari 到访、1545《Ars Magna》明文归名「del Ferro 首解、书中方法即其法」
10. **其他贡献**（核心贡献页，表格 + 公式框）：立方根分母分数有理化、定角圆规几何
11. **两个悬案**（表格）：是否两类都解出（1925 Bortolotti 手稿的猜测）；是否受 Pacioli 1501-1502 短暂任教博洛尼亚的刺激（页面明载为 conjecture，须保留「推测」措辞）
12. **历史坐标**（表格）：从 Pacioli「不可能」到首解再到《大术》公开的时间纵深；「卡尔达诺公式」背后的第一贡献者
13. **遗产与评价**（表格）：守密者的悖论——为自保而沉默，却因此让首解之名差点湮没，靠对手的诚实归名才留于青史
14. **终章**：61 岁、"三次方程的首解者"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **国籍**：metadata 国籍为 Lordship of Bologna、Papal States（历史政权）；封面与正文用现代「意大利」口径。DB 入库用历史政权加 `era_note: historical`。
- **生卒**：1465-02-06 生、1526-11-05 卒（享年 61），两者 page.md infobox 与 metadata 首值一致；metadata 死亡日有噪声第二值 `1526-00-00`，**以 1526-11-05 为准**。
- **禁写导师**：page.md 无载任何导师——身份信息页「师承」处留白或写「无载」。
- **禁写具体解出年份**：page.md 只说"first discovered"，未给出解出三次方程的年份——时间线上该事件**不带年份**。
- **Pacioli 刺激说**：page.md 原文是 "There are conjectures about whether..."——是**推测**，必须保留「据推测 / 猜测」措辞，禁写成既定事实。
- **方法不可知**：page.md 明言 "it is not known today with certainty what method del Ferro used"——第 6 页必须写「据推测的路线」，禁写「他的方法就是」。
- **两类是否都解出**：未知；1925 Bortolotti 手稿使 Bortolotti **怀疑**（suspect）两类都解出——措辞保持「猜测 / 怀疑」。
- **与 Tartaglia 的关系**：del Ferro 的 page.md **完全未提 Tartaglia 与 Fiore**——本篇禁写优先权之争细节（那是 Tartaglia / Cardano 篇的内容），只写 page.md 实载的「Cardano 在《大术》中归名 del Ferro 首解」。
- **归名的表述**：Cardano 在《大术》中**主动署名** del Ferro 为首解者——这是 Cardano 侧的诚实行为，勿写成「抢功」叙事。
- **配偶**：page.md 只说 "He married"，无妻子姓名——禁写妻子名字，不入库。
- **名字细节**：女婿 Annibale della Nave，page.md 中亦简称 Nave——正文统一用全名 Annibale della Nave（首次出现后可简称 della Nave）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q318083 | 待写入 |
| name_zh | 斯皮奥内·德尔·费罗 | 待写入 |
| name_en | Scipione del Ferro | 待写入 |
| birth_date | 1465-02-06 | 待写入 |
| death_date | 1526-11-05 | 待写入 |
| nationality | Lordship of Bologna / Papal States（historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / algebra / arithmetic / geometry | 待写入 |
| has_biography | 0 | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

- **学生兼女婿**：Annibale della Nave（继承笔记本、1526 接替博洛尼亚教席）
- **家庭**：父 Floriano Ferro（造纸业）、母 Filippa、女 Filippa（嫁 della Nave；入库名用 Filippa della Nave，避免与其母 Filippa Ferro 同名 stub 撞键）
- **影响（influence）**：Gerolamo Cardano（1543 获知手稿、《大术》归名）、Lodovico Ferrari（1543 陪同到访）
- **不入库**：Luca Pacioli（其 1501-1502 任教刺激 del Ferro 研究三次方程系页面明载之 conjecture，非确证关系）、妻子（无姓名）。

## 8. 奖项清单

- page.md 无载任何奖项与荣誉——**本节为空，禁杜撰**。

## 9. 机构清单

- 教育：University of Bologna（博洛尼亚大学，page.md 作 "likely studied"——教育关系可入库，起止年份无载不写）
- 任职：University of Bologna（博洛尼亚大学算术与几何讲师，1496–1526）

## 10. 终审清单

- [ ] 生卒 1465-02-06 / 1526-11-05，享年 61，出生地 Bologna
- [ ] 国籍封面用「意大利」，历史政权表述准确
- [ ] 无导师、无解出年份、无奖项——三处留白
- [ ] Pacioli 刺激说、方法路线、两类全解说均保留「推测」措辞
- [ ] 《大术》归名表述：del Ferro 首解、Cardano 主动署名
- [ ] 禁写 Tartaglia/Fiore 优先权之争（本篇 page.md 无载）
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像（装饰圆占位）+ 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Scipione_del_Ferro/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无真实肖像，确认使用装饰圆占位且图注注明「无存世肖像」
- [ ] **国籍**：封面顶部徽章明示意大利
- [ ] **引语核对**：本篇无直接引语可用——禁编造引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 16 世纪数学家（Tartaglia / Cardano）格式对齐

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
