# Pierre de Fermat（皮埃尔·德·费马）立传提示词

> qid=Q75655 · 1601-08-17 – 1665-01-12 · 法国数学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Pierre_de_Fermat/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。使用 images.txt 中的 17 世纪肖像（图注称 by Roland Lefebvre，下载至 `images/fermat_portrait.jpg`）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名演变、国籍、出生地、职业（法官）、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「页边批注 / 数论深渊」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Pierre de Fermat（皮埃尔·德·费马）。★ 姓氏中的 "de" 是 **1631 年购官后**才有资格加的——早年应作 "Pierre Fermat"
- **生卒**：1601-08-17 生于 Beaumont-de-Lomagne（法兰西王国，加斯科涅地区）→ 1665-01-12 逝于 Castres（今塔恩省），享年 63
- **国籍**：法国（Kingdom of France）
- **身份**：数学家、律师、法官（magistrate）、多语言学家、希腊语学者（Hellenist）；"a trained lawyer making mathematics more of a hobby than a profession"——**业余数学家之王**
- **家庭**：父 Dominique Fermat（富裕皮革商，曾任 Beaumont 四执政官之一）、母 Claire de Long；一兄两妹；1631-06-01 娶 Louise de Long（母亲的第四代表亲），育 8 子女（5 个成年：Clément-Samuel、Jean、Claire、Catherine、Louise）；其子 Samuel 于 1670 年出版父亲的《算术》页边批注
- **教育轨迹**：1623 年起奥尔良大学，1626 获民法学士（BCL）；无博士学位记载；1626 后移居波尔多开始严肃数学研究
- **学术影响源**：François Viète（波尔多时期深受其影响）；古典希腊数学文献（Anders Hald："The basis of Fermat's mathematics was the classical Greek treatises combined with Vieta's new algebraic methods"）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **解析几何（独立发明者之一）**：与笛卡尔并列为 17 世纪上半叶两大数学家；1636 年手稿《求极大极小与切线的方法》流通早于笛卡尔《La Géométrie》（1637）。
2. **拟等式法（adequality）**：求极值与切线的方法，"was equivalent to differential calculus"——**微积分前史核心**。
3. **一般幂函数积分**："Fermat was the first person known to have evaluated the integral of general power functions"——结果帮助牛顿与莱布尼茨建立微积分基本定理。
4. **费马大定理**：`aⁿ + bⁿ ≠ cⁿ (n>2)`，记于丢番图《算术》页边（*Observatio Domini Petri de Fermat*）；1670 年由其子刊出，1994 年 Andrew Wiles 证明（"using techniques unavailable to Fermat"）。
5. **费马小定理**：研究完全数时发现。
6. **费马数与费马分解法**：致 Carcavi 信中误称所有费马数皆素——欧拉指出 4,294,967,297 = 641 × 6,700,417。
7. **无穷递降法（infinite descent）**：用以证明费马直角三角形定理（含 n=4 情形）。
8. **平方和定理** 与**多边形数定理**（每数 = 三三角形数之和 = 四平方数之和 = ……）。
9. **概率论奠基**：1654 年与帕斯卡就"分赌注问题"通信，"joint founders of probability theory"；"Fermat is credited with carrying out the first-ever rigorous probability calculation"。
10. **费马原理（最短时间原理）**：光沿用时最短的路径传播——最小作用量原理史上的关键一步。
11. **数论之父**：André Weil 评 "Fermat essentially created the modern theory of numbers"。
12. **牛顿的证词**：牛顿自述其微积分早期想法直接来自"费马作切线的方法"。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（加斯科涅红） | `#8B1A1A` | 法国南部 / 图卢兹高等法院 |
| 强调色（数论金） | `#C9A227` | 现代数论之父 / 页边批注 |
| 分类色 1（数论 — 靛蓝） | `#4C5FD5` | 费马大定理 / 小定理 / 平方和 |
| 分类色 2（概率 — 青绿） | `#0E7C7B` | 与帕斯卡通信 / 分赌注问题 |
| 分类色 3（微积分前史 — 琥珀） | `#E07B30` | 拟等式法 / 幂函数积分 |
| 分类色 4（光学与几何 — 玫红） | `#B76E79` | 费马原理 / 解析几何 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「页边批注 / 书页」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**巴洛克典雅 / 深沉内敛**（业余之王、谜语式数学家）
- **匹配理由**：
  - 费马是大法官兼"业余数学家之王"——需**典雅、深沉**的配乐
  - "内敛" 匹配其"少证明、多断言"的谜语气质与页边批注传奇
  - "典雅" 匹配其法国法官身份与巴洛克时代
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 法国 17 世纪风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「业余数学家之王 · 费马大定理」+ 皮埃尔·德·费马 1601–1665 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 职业 / 教育 / 核心领域）
3. **费马的一生：时间线**（`\timelineslide`）：1601 出生 → 1623–26 奥尔良大学 BCL → 1631 购官图卢兹 / 成婚 → 1636 极值切线手稿 → 1654 与帕斯卡通信 → 1665 去世 → 1670 页边批注刊出 → 1994 Wiles 证明
4. **早年与教育**（`\earlyslide`）：博蒙-德洛马涅、奥尔良大学法学、波尔多时期受 Viète 影响起步
5. **费马大定理**（核心贡献页，表格 + 公式框）：`aⁿ+bⁿ≠cⁿ (n>2)`、页边批注传奇、1994 Wiles 证明
6. **费马小定理与费马数**（核心贡献页，表格 + 公式框）：完全数、费马数断言与欧拉的 641 反例
7. **拟等式法与极值切线**（核心贡献页，表格 + 公式框）："equivalent to differential calculus"、牛顿的证词
8. **幂函数积分**（核心贡献页，表格 + 公式框）：`∫xⁿ` 首算、为微积分基本定理铺路
9. **无穷递降法与平方和**（核心贡献页，表格 + 公式框）：递降法、两平方定理、多边形数定理
10. **概率论：与帕斯卡的通信**（核心贡献页，表格 + 公式框）：1654 分赌注问题、期望值、"joint founders"
11. **费马原理**（核心贡献页，表格 + 公式框）：光沿最短时间路径传播
12. **职业与通信网络**（表格）：图卢兹高等法院参事、与 Mersenne/Carcavi 通信、与笛卡尔/沃利斯的优先权之争
13. **身后与遗产**（表格）：1670 页边刊出、现代数论之父（Weil 评）、图卢兹费马中学与雕像
14. **终章**：63 岁、"数学在他是业余、成就在他是王者"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **出生年份之争**：原文 "Most sources give Fermat's birth year as 1601; Some sources give Fermat's birth year as 1607, however, recent research suggests this was the year a half-brother called Piere was born."——**用 1601**；用户排行榜表中的"1607"是错误来源，需修正。
- **生卒**：1601-08-17 / 1665-01-12，享年 63；死因 page.md 未载——勿杜撰。
- **页边批注**："the margin was too small to include the proof" 是 page.md 的**转述**——可引用但勿声称是拉丁原文直译。
- **费马并未证明一切**：原文 "Although Fermat claimed to have proven all his arithmetic theorems, few records of his proofs have survived. Many mathematicians, including Gauss, doubted several of his claims."——表述分寸：声称已证、鲜存证据、高斯等曾质疑。
- **费马数断言是错的**：致 Carcavi 信中称所有费马数皆素，欧拉举 641 反例——如实呈现。
- **"大定理"≠"最后提出的定理"**：1630s 写下、1670 刊出、1994 证明——时间线要清晰。
- **笛卡尔叶形线**：以笛卡尔命名（费马 infobox 列入 Known for 易误导）——勿作费马之物。
- **生前几乎全以书信发表**："He communicated most of his work in letters to friends, often with little or no proof"——《Ad Locos Planos et Solidos Isagoge》1679 年才遗世出版。
- **姓氏**：1631 年购官后才作 "de Fermat"——早年著作署名 Pierre Fermat。
- **称号**："业余数学家之王"（Prince of Amateurs）为通行称号可用；"现代数论之父"引 Weil 语注明出处。
- **metadata 冲突**：field_of_work 含 "statute"（疑为数据错误）弃用；educated_at "Old University of Orléans" 与 page.md "University of Orléans" 名称略异。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q75655 | 待写入 |
| name_zh | 皮埃尔·德·费马 | 待写入 |
| name_en | Pierre de Fermat | 待写入 |
| birth_date | 1601-08-17 | 待写入 |
| death_date | 1665-01-12 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / number theory / probability / analytic geometry / optics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **影响源**：François Viète（波尔多时期）、古典希腊数学文献
- **通信 / 学术**：Marin Mersenne（通信，未提大定理）、Pierre de Carcavi（通信）、Étienne d'Espagnet（波尔多数学同道）、Jean de Beaugrand
- **合作者**：Blaise Pascal（1654 概率通信，"joint founders of probability theory"）
- **论战 / 竞争**：René Descartes（解析几何优先权）、John Wallis（优先权之争）——原文 "Secrecy was common in European mathematical circles at the time. This naturally led to priority disputes with contemporaries such as Descartes and Wallis."
- **身后传播**：子 Samuel Fermat（1670 出版页边批注）
- **家庭**：父 Dominique Fermat（皮革商）、母 Claire de Long、妻 Louise de Long（8 子女）

## 8. 奖项清单

- 无奖项/院士身份记载；荣誉体现为：费马大定理/小定理/费马数以他命名、图卢兹 Lycée Pierre-de-Fermat、Capitole 雕像 *Hommage à Pierre Fermat*、Beaumont-de-Lomagne 纪念碑

## 9. 机构清单

- 教育：University of Orléans（BCL 1626）
- 任职：Parlement de Toulouse 参事（1630 购官、1631 就任，终身）；Chambre de l'Édit 参事（1665，墓碑铭文）

## 10. 终审清单

- [ ] 生卒 1601-08-17 / 1665-01-12，享年 63，出生地 Beaumont-de-Lomagne、逝世地 Castres（排行榜表"1607"需修正为 1601）
- [ ] 国籍用「法国」
- [ ] "de" 1631 购官后才有——早年署名 Pierre Fermat
- [ ] 费马大定理"1630s 页边断言 / 1670 刊出 / 1994 Wiles 证明"时间线准确
- [ ] 费马数断言错误（欧拉 641 反例）如实呈现
- [ ] "声称已证、鲜存证据、高斯等曾质疑"表述分寸到位
- [ ] 与帕斯卡"joint founders of probability theory"表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Pierre_de_Fermat/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 images.txt 的 Roland Lefebvre 肖像（下载至 `images/`）
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如牛顿"费马作切线的方法"、Weil "created the modern theory of numbers"）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（笛卡尔 / 帕斯卡）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
