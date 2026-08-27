# Adrien-Marie Legendre（阿德里安-马里·勒让德）立传提示词

> qid=Q191021 · 1752-09-18 – 1833-01-09 · 法国数学家 · 19 世纪（生年早于 1850，核心贡献横跨 18 世纪末–19 世纪初）
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Adrien-Marie_Legendre/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「正交 / 对称」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Adrien-Marie Legendre（中文惯称：勒让德）
- **生卒**：1752-09-18 生于巴黎（法兰西王国）→ 1833-01-09 逝于巴黎，享年 80（长期病痛）
- **国籍**：France（法国，出生时属法兰西王国 Kingdom of France）
- **身份**：数学家（数论、椭圆函数、几何、分析、最小二乘法）
- **家庭**：出身富裕家庭；1793 年娶 Marguerite-Claudine Couhin（其妻协助整理财务，身后悉心保存遗物以纪念）
- **教育轨迹**：
  - 就读巴黎 Collège Mazarin（马扎兰学院 / 四国学院）
  - 1770 年答辩物理与数学论文
  - 1775–1780 任教于 École Militaire（军事学校）
  - 1795 起任教于 École Normale（高等师范学校）
  - 同期与 Bureau des Longitudes（经度局）相关
- **师承 / 引路人**：Joseph-Louis Lagrange（1782 年柏林科学院抛射体论文获奖后引起拉格朗日注意，受其赏识）
- **研究领域**：数论、椭圆函数、几何、分析、最小二乘法（统计学）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **勒让德多项式（Legendre polynomials）**：勒让德微分方程的解，广泛用于物理与工程（静电学、球谐函数）——其 1783 年《Sur l'attraction des Sphéroïdes homogènes》即奠基性工作。
2. **勒让德符号（Legendre symbol）**：为表述二次互反律引入的符号；Legendre **猜想**了二次互反律（后由 Gauss 证明）。
3. **勒让德变换（Legendre transformation）**：连接拉格朗日力学与哈密顿力学的桥梁；热力学中用于由内能导出焓、亥姆霍兹自由能、吉布斯自由能。
4. **最小二乘法（method of least squares）**：1806 年作为彗星轨道书附录**首次正式发表**（法文 "méthode des moindres carrés" 即"最小二乘法"直译来源）；但 Gauss 更早发现——这是数学史上有名的优先权公案。
5. **素数分布**：1798 年**猜想**素数定理（prime number theorem），1896 年由 Hadamard 与 de la Vallée-Poussin 严格证明。
6. **椭圆积分分类**：完成大量椭圆积分分类工作（《Traité des Fonctions Elliptiques》三卷 1825/1826/1830），但完整解决（双周期性）由 Abel 与 Jacobi 在其基础上完成。
7. **Γ 函数符号**：《Exercices de Calcul Intégral》（1811/1817/1819 三卷）引入 Γ 符号，并归一化为 Γ(n+1)=n!；同时研究 β、γ 函数及其在力学（地球自转、椭球引力）中的应用。
8. **费马大定理 n=5**：1830 年给出 n=5 情形证明（Dirichlet 于 1828 年亦独立证明）。
9. **《Éléments de géométrie》（1794）**：重排并简化欧几里得《几何原本》的命题，成为此后约 100 年居主导地位的初等几何教科书。
10. **偏导符号 ∂**：引入偏微分符号 ∂。
11. **身后荣誉**：名字刻于埃菲尔铁塔 72 位法国科学家之一；月球环形山 Legendre、小行星 26950 Legendre 以其命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国深蓝） | `#1F3A93` | 法兰西理性 / 王室蓝 |
| 强调色（法国金） | `#C9A227` | 埃菲尔塔 / 荣誉军团 |
| 分类色 1（数论 — 靛蓝） | `#4C5FD5` | 勒让德符号 / 二次互反律 / 素数 |
| 分类色 2（椭圆函数 — 青绿） | `#0E7C7B` | 椭圆积分分类 |
| 分类色 3（分析/几何 — 琥珀） | `#E07B30` | 勒让德多项式 / 变换 / 几何原本 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「勒让德多项式的正交性 / 球谐函数对称」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 启蒙理性**（18 世纪启蒙时代法国学者的严谨与典雅）
- **匹配理由**：
  - Legendre 是法国大革命前后过渡期的学者，其数学严谨、典雅、影响深远——需要**庄重、古典、理性**的配乐，呼应启蒙时代法兰西的学术气象
  - "典雅" 匹配其《几何原本》教科书百年不衰的教育影响
  - "庄重" 匹配其身后刻名埃菲尔塔的殊荣与 80 岁高寿的完整一生
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：古典 / 庄重 / 典雅风格曲目（呼应启蒙时代法国学者）
  - 备选：历史感深沉曲目（呼应 18-19 世纪之交的时代背景）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「数论与椭圆函数的先驱 · 最小二乘法的发表者」+ 勒让德 1752–1833 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：数论 / 椭圆函数 / 几何与分析 / 最小二乘法 四分类
4. **早年与教育**（1752–1780）：巴黎富裕家庭、Collège Mazarin、1770 答辩、École Militaire 任教
5. **数论贡献**（核心贡献页）：勒让德符号、二次互反律猜想、素数分布、费马大定理 n=5
6. **最小二乘法**（核心贡献页）：1806 首次发表、与 Gauss 的优先权公案、"moindres carrés" 直译
7. **椭圆函数与椭圆积分分类**：三卷《Traité des Fonctions Elliptiques》、与 Abel/Jacobi 的关系
8. **勒让德多项式与球谐函数**：勒让德微分方程、物理/工程应用
9. **勒让德变换**：力学（拉格朗日→哈密顿）与热力学（自由能）
10. **《几何原本》与教育影响**：1794 教科书、百年主导
11. **荣誉与身后**：埃菲尔塔 72 名、月球环形山、小行星、肖像错误轶事
12. **终章**：80 岁、横跨 18-19 世纪的遗产与历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **【最重要】肖像错误（Mistaken portrait）**：近 200 年（直到 2005 年发现错误）书籍、画作、文章都误把法国**政治家 Louis Legendre（1752–1797）的侧面肖像**当作数学家 Legendre 的肖像。错误源于草图仅标注 "Legendre" 且与 Lagrange 等数学家同书出现。**真正的 Legendre 肖像是 1820 年 Boilly 的水彩漫画（caricature）**（以及《Le Panthéon scientifique de la tour Eiffel》中另一幅）。**封面与身份信息页头像必须用正确肖像（Boilly 漫画 / `images.txt` 第一张 croquis Barral），绝不能用 Louis Legendre 侧面像**——若头像下载失败，宁可用装饰圆占位并注明，也不要用错误肖像。
- **最小二乘法归属**：Legendre 是**第一个正式发表**（1806）者，但 **Gauss 更早发现**——勿写 Legendre 独家发明，表述为"首次发表，Gauss 先发现"。
- **二次互反律**：Legendre **猜想**，Gauss **证明**——勿混淆。
- **素数定理**：Legendre 1798 **猜想**，Hadamard 与 de la Vallée-Poussin 1896 **证明**。
- **费马大定理 n=5**：Legendre 1830 证明，Dirichlet 1828 独立证明（Dirichlet 更早）——表述为"两人独立证明"。
- **椭圆积分**：Legendre 完成大量分类，但双周期性完整解决是 Abel/Jacobi——Abel 的工作**建立在其基础上**，勿写 Legendre 独占椭圆函数。
- **生卒日期**：出生日 metadata 有 1752-09-18 与 1752-00-00，以 Wikipedia infobox **1752-09-18** 为准；死亡日有 1833-01-09/01-10，以 **1833-01-09** 为准。
- **出生地**：metadata 有 Paris 与 Toulouse 两个值，以 Wikipedia infobox **Paris** 为准。
- **国籍表述**：封面顶部用「法国」作为现代对应（出生时属法兰西王国）。
- **导师**：18 世纪法国科学院体系无现代博士导师制，Lagrange 为**赏识者/引路人**（1782 论文获奖后引起注意），勿写成正式博士导师。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q191021 | 待写入 |
| name_zh | 勒让德（或 阿德里安-马里·勒让德） | 待写入 |
| name_en | Adrien-Marie Legendre | 待写入 |
| birth_date | 1752-09-18 | 待写入 |
| death_date | 1833-01-09 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | number theory / elliptic function / geometry / least squares | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **引路人 / 赏识者**：Joseph-Louis Lagrange（1782 年论文获奖后引起注意）
- **优先权 / 竞争**：Carl Friedrich Gauss（最小二乘法先发现者、二次互反律证明者）、Peter Gustav Lejeune Dirichlet（费马大定理 n=5 独立证明者）
- **椭圆函数承前启后**：Niels Henrik Abel、Carl Gustav Jacob Jacobi（在 Legendre 基础上完成双周期性）
- **素数定理后续**：Jacques Hadamard、Charles Jean de la Vallée-Poussin（1896 证明）
- **同期法国数学家**：Joseph Fourier（1820 年 Boilly 水彩漫画同框）
- **英法测量合作者**：Dominique comte de Cassini、Pierre Méchain（1787 访 Dover/London）、William Herschel（拜访，天王星发现者）
- **家族**：妻 Marguerite-Claudine Couhin（1793 年结婚）

## 8. 奖项清单

- 1782 年柏林科学院抛射体论文奖（Berlin Academy prize，引起 Lagrange 注意）
- 1789 年当选英国皇家学会 Fellow（Fellow of the Royal Society）
- 1831 年荣誉军团军官（Officer of the Legion of Honour）
- 1832 年美国艺术与科学院外籍荣誉会员（Foreign Honorary Member of AAAS）
- 爱丁堡皇家学会 Fellow
- 埃菲尔铁塔 72 位法国科学家刻名之一（身后纪念）

## 9. 机构清单

- 教育：Collège Mazarin（马扎兰学院 / 四国学院）
- 任职：École Militaire（1775–1780 任教，1799–1812 炮兵毕业生数学考官）、École Normale（1795 起）、École Polytechnique（1799–1815 常任数学考官）、Bureau des Longitudes（经度局）、Académie des Sciences（1783 adjoint、1785 associate、1795 重组后数学组六成员之一）

## 10. 终审清单

- [ ] 生卒 1752-09-18 / 1833-01-09，享年 80，出生地以 Paris 为准
- [ ] 【肖像错误】封面/身份信息页头像用正确肖像（Boilly 漫画 / croquis Barral），绝不用 Louis Legendre 侧面像
- [ ] 最小二乘法"Legendre 首发表、Gauss 先发现"表述准确
- [ ] 二次互反律"Legendre 猜想、Gauss 证明"表述准确
- [ ] 素数定理"1798 猜想、1896 证明"表述准确
- [ ] 费马大定理 n=5"Legendre 与 Dirichlet 独立证明"表述准确
- [ ] 椭圆积分"Legendre 分类、Abel/Jacobi 完整解决"表述准确
- [ ] Lagrange 为"引路人/赏识者"非正式博士导师
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Adrien-Marie_Legendre/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先正确肖像（`images.txt` 第一张 croquis Barral / Boilly 漫画）；**绝不用 Louis Legendre 侧面像**；无则用装饰圆占位并注明
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到，否则忠实转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Abel / Galois / Frobenius）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
