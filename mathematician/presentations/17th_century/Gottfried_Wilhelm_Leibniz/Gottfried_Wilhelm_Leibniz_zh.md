# Gottfried Wilhelm Leibniz（戈特弗里德·威廉·莱布尼茨）立传提示词

> qid=Q9047 · 1646-07-01（旧历 1646-06-21）– 1716-11-14 · 德国数学家/哲学家 · 17 世纪（核心贡献跨 17–18 世纪）
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Gottfried_Wilhelm_Leibniz/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。images.txt 有肖像可用：**c. 1700 肖像**，下载至 `images/leibniz_portrait.jpg`。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒（注新旧历）、国籍、出生地、父亲职业、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「二进制 0/1 / ∫ 积分号」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Gottfried Wilhelm Leibniz（戈特弗里德·威廉·莱布尼茨，一拼 Leibnitz；自称常作 "Gottfried von Leibniz"，但"no document has ever been found"证明其获封贵族——身份页慎用"von"）
- **生卒**：**1646-07-01**（旧历 1646-06-21）生于莱比锡（萨克森选侯国）→ 1716-11-14 逝于汉诺威（汉诺威选侯国），享年 70；葬于 Neustädter Kirche——"His grave went unmarked for more than 50 years"（墓无标记逾 50 年）
- **国籍**：metadata 仅记 Electorate of Saxony；长期效力于 Brunswick-Lüneburg（布伦瑞克-吕讷堡/汉诺威宫廷，1676–1716）——现代对应德国
- **身份**：数学家、哲学家、科学家、外交官——"the last universal genius"（最后的通才）；metadata 另列法学家、历史学家、图书馆员、逻辑学家等
- **家庭**：父 Friedrich Leibniz（莱比锡大学道德哲学教授兼哲学院长，莱布尼茨 **6 岁时**去世——与牛顿"父死于出生前"不同，勿混淆）；母 Catharina Schmuck（1621–1664），由母亲和舅舅抚养；7 岁起自由使用父亲遗留的私人图书馆，12 岁通拉丁文，13 岁一早写出 300 行拉丁六音步诗；**终身未婚**——"Leibniz never married. He proposed to an unknown woman at age 50, but changed his mind when she took too long to decide."
- **信仰**：新教徒、philosophical theist，终身持三位一体信仰（与牛顿的异端立场相反）
- **教育轨迹**：Alte Nikolaischule → 莱比锡大学（1661 入学，14 岁）：BA 哲学 1662、MA 哲学 1664、LLB 1665 → 耶拿大学 1663 夏季学期（Erhard Weigel）→ **阿尔特多夫大学法学博士 1666**（莱比锡因他年轻拒绝授博士，故转投；随后拒绝该校教职）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **微积分（独立发明）**：1674 年开始研究，笔记本最早证据 **1675**（11 月 11 日首次用积分求曲线下面积）；**1684 年发表**《Nova methodus pro maximis et minimis》——"credited, alongside Isaac Newton, with the creation of calculus... independently of Newton's developments"。
2. **微积分记号**：积分号 `∫`（summa 的拉长 S）、微分 `dx`、导数 `dy/dx`——"Leibniz's notation has been favoured as the conventional and more exact expression of calculus"；乘积法则至今称 Leibniz's law。
3. **微积分基本定理表述（1693）**：《Supplementum geometriae dimensoriae》图示积分与微分互逆（Newton–Leibniz axiom）。
4. **二进制**：现代二进制记数系统缔造者之一（1679《De progressione dyadica》；1703 年发表）；并与《易经》六爻对应——1701 年白晋（Joachim Bouvet）寄来卦图。
5. **《论组合术》De Arte Combinatoria（1666，19 岁）**：characteristica universalis（普遍文字）与"人类思想字母表"的起点。
6. **单子论 Monadology（1714）**：宇宙由无部分的简单实体"单子"构成，依"前定和谐"运行；90 条格言，身后出版。
7. **"最好的可能世界"**：《神正论》Théodicée（1710）核心——"God assuredly always chooses the best"；后被伏尔泰《老实人》化名 Pangloss 讽刺（身后声名受损主因）。
8. **形式逻辑先驱**："one of the most important logicians between the times of Aristotle and Gottlob Frege"；calculus ratiocinator——"Let us calculate"。
9. **行列式**：Leibniz 行列式公式（按余因子展开）；1684 年已用行列式解线性方程组（早于 Cramer 1750）。
10. **vis viva（活力）之争**：`mv²`（动能的两倍）vs 动量守恒派——能量守恒原理先声。
11. **时空关系论**："I hold space to be something merely relative, as time is..."——Leibniz–Clarke 通信；爱因斯坦自称 "Leibnizian"。
12. **机械计算器**：stepped reckoner（可四则运算），1673 年据此当选皇家学会会员；Leibniz wheel；"may have been the first computer scientist"。
13. **柏林科学院创始院长（1700）**："Leibniz drew up its first statutes, and served as its first president for the remainder of his life"；晚年还倡议德累斯顿、维也纳、圣彼得堡科学院。
14. **莱布尼茨 π 级数**：`1 − 1/3 + 1/5 − 1/7 + ⋯ = π/4`；率先明确"函数"概念（1692/1694）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士蓝） | `#1F3A5F` | 德意志 / 普鲁士学术传统 |
| 强调色（通才金） | `#C9A227` | 最后的通才 / ∫ 符号 |
| 分类色 1（微积分 — 靛蓝） | `#4C5FD5` | ∫ dx / 莱布尼茨记号 |
| 分类色 2（二进制与计算 — 青绿） | `#0E7C7B` | 0/1 / stepped reckoner / 易经卦图 |
| 分类色 3（哲学 — 琥珀） | `#E07B30` | 单子论 / 最好的可能世界 / 时空之争 |
| 分类色 4（科学院与外交 — 玫红） | `#B76E79` | 柏林科学院 / 汉诺威宫廷 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「二进制 0/1 矩阵 / 积分号曲线下面积」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**巴洛克的繁复对位 / 通才的织体**（"最后的通才"）
- **匹配理由**：
  - 莱布尼茨是多线并行的通才——需**织体繁复、对位精妙**的配乐
  - "对位" 匹配其"前定和谐"与普遍文字的哲学
  - "繁复" 匹配其 15,000 封信、40,000 件遗稿的浩瀚
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 德国 17–18 世纪风格曲目（布克斯特胡德—巴赫气质）
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「微积分符号之父 · 最后的通才」+ 莱布尼茨 1646–1716 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒含新旧历 / 国籍 / 出生地 / 父亲职业 / 教育 / 核心领域）
3. **莱布尼茨的一生：时间线**（`\timelineslide`）：1646 莱比锡出生 → 1661 莱比锡大学（14 岁）→ 1666 《论组合术》/ 阿尔特多夫法学博士 → 1672 巴黎（惠更斯为师）→ 1673 FRS / 访伦敦 → 1676 定居汉诺威 → 1684 微积分发表 → 1700 柏林科学院院长 → 1710 《神正论》→ 1714 《单子论》→ 1716 去世
4. **早年与教育**（`\earlyslide`）：莱比锡、父亲的书房（7 岁起）、14 岁入学、1666 拒授博士转阿尔特多夫
5. **微积分的独立发明**（核心贡献页，表格 + 公式框）：1675 笔记、1684 《Nova methodus》先于牛顿出版
6. **莱布尼茨记号**（核心贡献页，表格 + 公式框）：`∫`、`dx`、`dy/dx`、乘积法则、Leibniz 积分法则
7. **二进制与《易经》**（核心贡献页，表格 + 公式框）：0/1 系统、1701 白晋卦图、"Explication de l'Arithmétique Binaire" 1703
8. **单子论与最好的可能世界**（核心贡献页，表格 + 公式框）：前定和谐、《神正论》1710、伏尔泰的 Pangloss 讽刺
9. **形式逻辑与普遍文字**（核心贡献页，表格 + 公式框）：calculus ratiocinator、"Let us calculate"
10. **行列式与 vis viva**（核心贡献页，表格 + 公式框）：行列式公式、`mv²` 与能量守恒先声
11. **计算器与"第一位计算机科学家"**（核心贡献页，表格 + 公式框）：stepped reckoner、Leibniz wheel、1673 FRS
12. **优先权之争**（表格）：牛顿 1665–66 手稿在先 / 莱布尼茨 1684 发表在先、1711 皇家学会裁决内幕、"1900 年后史学界趋于还其清白"、其自身倒填手稿日期的污点
13. **身后与冷清的葬礼**（表格）：柏林科学院首任院长、巴黎科学院外籍院士 1700（1675 申请被拒）、葬礼仅秘书一人出席、Fontenelle 悼词、Leibniz University Hannover / 莱布尼茨奖
14. **终章**：70 岁、"最后的通才"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **新旧历**：infobox "1 July 1646 [O.S. 21 June]"（新历在前）；metadata 只存旧历 1646-06-21——写"1646 年 7 月 1 日（儒略历 6 月 21 日）"。
- **谁先发表（双陈述）**：牛顿 1665–66 手稿在先（"Newton first developed his theory earlier in 1666, and which had been in circulation among mathematicians since 1668"）**且**莱布尼茨 1684 发表在先（"Leibniz did not publish anything about his calculus until 1684"）——只说一半即失实。
- **优先权之争口径**："Historians of mathematics writing since 1900 or so have tended to acquit Leibniz"；皇家学会 1711 调查 "In which Newton was an unacknowledged participant"（牛顿未署名参与者，且自写结论）。
- **莱布尼茨自身污点**："On several occasions, Leibniz backdated and altered personal manuscripts, actions which put him in a bad light during the calculus controversy"——不必回避，注明是"授人以柄"而非抄袭实锤。
- **1676 伦敦之行**：Newton "accused him of having seen his unpublished work on calculus in advance"——是**指控**非定论。
- **二进制优先权**："though the English astronomer Thomas Harriot had devised the same system decades before"——说"发明二进制"要加限定（系统化/阐明逻辑性质）。
- **与中国通信**：对象是耶稣会士白晋（Joachim Bouvet）；page.md 只写 "the Emperor of China"，**未出现"康熙"字样**——勿写康熙（或另行查证后加注）。
- **"最好的可能世界"**：必须与伏尔泰《老实人》(1759) 的 Pangloss 讽刺绑定叙述——这是其身后声名受损主因。
- **metadata 噪声**：doctoral_student 含 Nicolas Malebranche（实为巴黎结识的同辈哲学家，弃用）；nationality 仅 Saxony 未反映汉诺威效力——字段按事实补正。
- **葬礼冷清**："neither George I... nor any fellow courtier other than his personal secretary attended the funeral"；"His grave went unmarked for more than 50 years"；皇家学会与柏林科学院均未致哀——如实呈现。
- **1675 年巴黎科学院申请被拒**（"there were already enough foreigners there"），1700 年才当选外籍院士——两个年份都要写对。
- **称号**："最后的通才"（the last universal genius）为原文可用；"微积分符号之父"表意可，但要与"与牛顿各自独立"口径并列。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q9047 | 待写入 |
| name_zh | 戈特弗里德·威廉·莱布尼茨 | 待写入 |
| name_en | Gottfried Wilhelm Leibniz | 待写入 |
| birth_date | 1646-07-01（旧历 1646-06-21） | 待写入 |
| death_date | 1716-11-14 | 待写入 |
| nationality | Germany（Electorate of Saxony / Hanover） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / calculus / philosophy / logic / binary / diplomacy | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Jakob Thomasius（莱比锡，BA 论文导师）、Erhard Weigel（耶拿）、**Christiaan Huygens**（1672–1676 巴黎，数学自修的导师）
- **学生（通信弟子）**：Christian Wolff；与 **Johann Bernoulli** 长期通信（1695 分数微积分信件；1745 出版通信集）；Jacob Bernoulli 为其记号的早期拥护者
- **会面 / 通信**：Spinoza（1676 海牙深谈）、Malebranche、Antoine Arnauld、Henry Oldenburg、John Collins、Tschirnhaus、Bossuet、**Joachim Bouvet（白晋，易经卦图 1701）**
- **庇护人**：Sophia 选帝侯夫人、Sophia Charlotte 普鲁士王后、Caroline of Ansbach；George I（禁止其赴伦敦）
- **论战 / 竞争**：Isaac Newton 与 John Keill（微积分优先权之争）、Samuel Clarke（时空之争，Leibniz–Clarke 通信）
- **家庭**：父 Friedrich Leibniz（哲学教授，其 6 岁时去世）、母 Catharina Schmuck；终身未婚

## 8. 奖项清单

- FRS（1673，凭 stepped reckoner 演示）；柏林科学院创始院长（1700，终身）；巴黎科学院外籍院士（1700）；1712 起 Habsburg Imperial Court Councillor；身后：Leibniz University Hannover、莱布尼茨奖（1985）、UNESCO 世界记忆名录（2007 收其手稿）

## 9. 机构清单

- 教育：莱比锡大学（BA 1662 / MA 1664 / LLB 1665）；耶拿大学（1663，Weigel）；阿尔特多夫大学（法学博士 1666）
- 任职：美因茨选侯外交幕僚（1670s）；汉诺威宫廷（Brunswick-Lüneburg，1676–1716，宫廷顾问/图书馆员）；Wolfenbüttel Herzog August 图书馆馆长（1691 起）；柏林科学院首任院长（1700–1716）；彼得大帝顾问（1711 起）；维也纳帝国宫廷顾问（1712 起）

## 10. 终审清单

- [ ] 生卒 1646-07-01（O.S. 06-21）/ 1716-11-14，享年 70，出生地 Leipzig、逝世地 Hanover
- [ ] 国籍用「德国」，历史政权注明萨克森选侯国/汉诺威
- [ ] 微积分"牛顿更早、莱布尼茨 1684 先发表"双陈述完整
- [ ] "1900 年后史学界趋于还其清白"+ 倒填手稿污点两面表述
- [ ] 二进制加 Harriot 先例限定；易经通信对象白晋、勿写康熙（除非另行查证）
- [ ] 皇家学会 FRS 1673、柏林科学院 1700、巴黎科学院 1675 被拒/1700 当选——年份准确
- [ ] 葬礼冷清与"墓无标记逾 50 年"如实呈现
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Gottfried_Wilhelm_Leibniz/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 c. 1700 肖像（images.txt 已有链接）
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "Let us calculate"、"I hold space to be something merely relative..."）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（牛顿 / 雅各布·伯努利 / 惠更斯）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
