# Arthur Harden（阿瑟·哈登）立传提示词

> qid=Q189803 · 1865-10-12 – 1940-06-17 · 英国生物化学家 · 诺贝尔化学奖（1929，与 Hans von Euler-Chelpin 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Arthur_Harden/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 infobox 无肖像：先试 Commons `Special:FilePath/Arthur Harden.jpg?width=600`（404/HTML 则改 `ArthurHarden.jpg`），再退 Wikipedia REST API `page/summary` 查 infobox 原图名；全部失败用装饰圆占位（主色渐变 + 姓名首字母），并在 §11 Review 注明。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 磷酸与发酵之谜的破译者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「磷酸基团 / 发酵气泡」母题——离散圆点暗示酵母细胞中磷酸酯的逐级磷酸化。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Harden–Young 酯 = 果糖-1,6-二磷酸。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Arthur Harden（中文惯称：阿瑟·哈登；FRS，1926 年受封爵士）
- **生卒**：1865-10-12 生于英格兰兰开夏郡 Manchester → 1940-06-17 逝于英格兰白金汉郡 Bourne End，享年 74
- **国籍**：United Kingdom（英国）
- **身份**：生物化学家（biochemist；1929 诺贝尔化学奖共同得主）
- **家庭**：父 Albert Tyas Harden 为苏格兰长老会商人，母 Eliza Macalister；1900 年娶 Georgina Sydney Bridge（1928 年 1 月先逝），无子女；1896-04-14 当选 Manchester Literary and Philosophical Society 会员
- **教育轨迹**：
  - 幼年入 Manchester Victoria Park 的私立学校（Dr Ernest Adam 主办）
  - 1877（12 岁）入 Tettenhall College（Staffordshire）
  - 1882 入 Owens College（今 University of Manchester），1885 毕业；师从 Roscoe 教授学化学，受 J.B. Cohen（《The Owens College Course of Practical Organic Chemistry》作者）影响
  - 1886 获 Dalton Scholarship in Chemistry，赴 Erlangen 一年
- **导师**：Otto Fischer（Erlangen 博士导师；注意与 Hermann Emil Fischer 是不同的人）
- **博士**：Erlangen 大学 PhD，β-nitroso-α-naphthylamine 的合成与性质研究
- **研究领域**：生物化学——糖的酒精发酵、发酵酶、磷酸在发酵中的作用、维生素

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **曼彻斯特商人之子（1865）**：苏格兰长老会商人的儿子，Tettenhall College → Owens College 的经典英式化学教育路线。
2. **Dalton 奖学金与德国深造（1886）**：获奖学金赴 Erlangen 跟随 Otto Fischer 合成 β-nitroso-α-naphthylamine，获 PhD。
3. **回到曼彻斯特（1887–1897）**：任讲师兼 demonstrator，与 Philip Hartog 同事；研究 John Dalton 的生平与工作；1895 与 F.C. Garrett 合著《Practical Organic Chemistry》教科书。
4. **光化学起步**：在曼彻斯特研究 CO₂ 与氯气混合物的光化学作用——这套方法后来被移植到生物学问题。
5. **入职 Lister Institute（1897）**：任新成立的 British Institute of Preventive Medicine（后更名 Lister Institute）化学家；1902 获 Victoria University D.Sc.；1907 任生化部主任直至 1930 年退休（退休后仍继续研究）。
6. **方法移植：从光化学到发酵**：把物理化学方法应用于细菌的化学作用与酒精发酵研究。
7. **Harden–Young 酯（与 William John Young 合作）**：酵母糖酵解研究中发现一种磷酸化酯，长期称 Harden–Young ester，后经化学分析证明是果糖-1,6-二磷酸（fructose 1,6-bisphosphate）。
8. **磷酸的发现**：证明 Buchner 发现的酶 zymase 只有在与辅酶 cozymase（即 NAD）相互作用时才产生发酵——辅酶概念的早期关键证据。
9. **发酵的磷酸化图景**：Harden–Young 酯由果糖-6-磷酸经 phosphofructokinase 磷酸化生成，再被 aldolase 裂解为 glyceraldehyde 3-phosphate 与 dihydroxyacetone phosphate——糖酵解路径的核心步骤。
10. **维生素研究**：发表一系列关于抗坏血病（antiscorbutic）与抗神经炎（anti-neuritic）维生素的论文。
11. **学术服务**：Biochemical Society 创始成员；任《Biochemical Journal》编辑长达 25 年。
12. **1929 诺贝尔化学奖**：与 Hans von Euler-Chelpin 共享，官方口径 "for their investigations on the fermentation of sugar and fermentative enzymes"；诺奖演讲 1929-12-12《The Function of Phosphate in Alcoholic Fermentation》。
13. **荣誉晚年**：1926 年受封爵士；FRS；1935 获 Davy Medal；1940 年逝于 Bourne End，享年 74。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绿 deepgreen） | `#1E5631` | 发酵与生命化学的沉稳底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（糖酵解 badgeGlyco） | `#2E7D5B` | 青绿 Harden–Young 酯 / 磷酸化 |
| 分类色 2（发酵酶 badgeZymase） | `#7A5C1E` | 赭金 zymase / cozymase |
| 分类色 3（维生素 badgeVitamin） | `#5B2A2A` | 深红抗坏血病 / 抗神经炎维生素 |
| 分类色 4（学术遗产 badgeLegacy） | `#31456E` | 藏青 Biochemical Journal / 学会 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「发酵气泡 / 磷酸基团」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（文件 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`，不要复制 wav 文件）
- **风格**：怀旧 / 纪录片 / 沉静忧伤
- **匹配理由**：
  - "怀旧" 匹配哈登的学术年代感——维多利亚晚期的曼彻斯特化学学派到两次大战之间的伦敦生化奠基时代
  - "纪录片" 匹配其研究的渐进性——磷酸作用不是灵光一现，而是 25 年编辑生涯与长期发酵实验的沉淀
  - "沉静" 匹配其气质——无子女、无争议、安安静静把辅酶概念做实的实验家
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐（15 页 × 7 秒 ≈ 105 秒）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 磷酸与发酵之谜的破译者 / Arthur Harden 1865–1940 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  哈登的一生 — 时间线（10 节点：1865→1877→1882→1886→1897→1907→1926→1929→1935→1940）
04  早年：曼彻斯特与 Dalton 奖学金 (1865–1886) — 表格「时间|事件|结果」
05  Erlangen 与回流 (1886–1897) — 表格「时间|事件|结果」+ 公式框：β-nitroso-α-naphthylamine
06  Lister Institute (1897–1930) — 表格「阶段|职责|结果」
07  Harden–Young 酯 (与 W.J. Young 合作) — 表格「问题|方法|结果」+ 公式框：Harden–Young ester = 果糖-1,6-二磷酸
08  磷酸与 cozymase — 表格「问题|方法|结果」+ 公式框：zymase + cozymase(NAD) → 发酵
09  1929 诺贝尔化学奖 — 表格「人物|贡献|结果」+ 官方获奖理由英文原句
10  维生素与学术服务 — 表格「领域|工作|结果」（antiscorbutic / anti-neuritic；Biochemical Journal 25 年）
11  荣誉与爵士 — 高斯式「类别|代表|意义」表格（FRS / 1926 爵士 / Davy Medal 1935）
12  科学遗产：糖酵解路径 — 流程图页（果糖-6-磷酸 → PFK → Harden–Young 酯 → aldolase → 两分子磷酸丙糖）
13  遗产：辅酶概念的奠基石 — 四分类遗产盒 + 公式框：糖酵解现代图景
14  结尾 — 「在发酵的泡沫里，他读出了磷酸的节拍。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| Fischer 同名 | 博士导师是 **Otto Fischer**（Erlangen），**不是** Hermann Emil Fischer（柏林）、Hans Fischer（1930 得主）、Ernst Otto Fischer（1973 得主）——四人勿混 |
| 1929 获奖口径 | 官方措辞 "for their investigations on the fermentation of sugar and fermentative enzymes"；与 Euler-Chelpin **共享**——勿写独享 |
| 两人分工 | Harden：发酵的化学与辅酶 cozymase；Euler-Chelpin：用物理化学解释糖发酵与酶的作用——勿互换 |
| zymase 归属 | zymase 是 **Eduard Buchner** 发现的，哈登的贡献是证明它需与 cozymase（NAD）协同——勿写哈登发现 zymase |
| Harden–Young 酯 | 长期名 Harden–Young ester，化学分析后证明为**果糖-1,6-二磷酸**——现代名勿省略 |
| 博士生名单 | 正文 infobox 的 Doctoral students 仅 **Roland Victor Norris、Ida Maclean** 两人——只入这两人 |
| 无子女 | 与 Georgina Sydney Bridge 结婚（1900），**无子女**——勿编造子嗣 |
| 生卒地 | 生于 Manchester，逝于 Bourne End（Buckinghamshire）——勿混淆 |
| 退休表述 | 1930 年退休（卸任生化部主任），**退休后仍在研究所继续科学工作**——勿写"停止研究" |
| 爵士 | 1926 年受封 Sir——infobox 与正文均有载，可写 |
| 获奖理由翻译 | 中文表述必须保留官方英文原句 + 忠实直译，不得扩写成"证明发酵的全部机理" |
| 页面无载禁写 | page.md **未载**其出生具体街巷、兄弟姊妹、死因细节——一律不写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q189803 | ✅ |
| name_zh | 阿瑟·哈登 | ✅ |
| name_en | Arthur Harden | ✅ |
| birth_date | 1865-10-12 | ✅ |
| death_date | 1940-06-17 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / enzymology / carbohydrate metabolism / vitamin research，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Fischer | 师→生（Erlangen 博士导师） | 1886 Dalton 奖学金资助下赴 Erlangen，研究 β-nitroso-α-naphthylamine |
| influence | Henry Roscoe | 无向 | Owens College 化学教授，哈登师从其学习化学 |
| influence | J.B. Cohen | 无向 | 《Owens College 实用有机化学》作者，对哈登有影响 |
| colleague | William John Young | 无向 | 共同发现 Harden–Young 酯（果糖-1,6-二磷酸） |
| co-honored | Hans von Euler-Chelpin | 无向 | 1929 诺贝尔化学奖共同得主 |

**门生（Harden → 学生，源自本地 Wikipedia 正文 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Roland Victor Norris | Harden → 学生 | infobox 明载博士生 |
| advisor-student | Ida Maclean | Harden → 学生 | infobox 明载博士生 |

**配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Georgina Sydney Bridge | 无向 | 1900 年结婚，无子女 |

> **禁入库名单（metadata/外部链接 only）**：Philip Hartog（正文仅"一同授课"同僚，未明载工作关系，不单独建关系行）、John Dalton（哈登研究其生平，非直接关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1929，与 Hans von Euler-Chelpin 共享）
- Fellow of the Royal Society，FRS
- Davy Medal（1935）
- Knight Bachelor（1926 受封爵士）
- 多个荣誉博士学位（正文泛称 "several honorary doctorates"，未列具体校名——勿杜撰）

## 9. 机构清单

- 教育：私立学校（Victoria Park, Dr Ernest Adam）→ Tettenhall College（1877–）→ Owens College / University of Manchester（1882–1885）→ University of Erlangen（1886–，PhD）；D.Sc.（Victoria University, 1902-06）
- 任职：University of Manchester 讲师兼 demonstrator（回曼彻斯特后–1897）；British Institute of Preventive Medicine / Lister Institute 化学家（1897–），生化部主任（1907–1930），退休后继续研究
- 学术服务：Biochemical Society 创始成员；《Biochemical Journal》编辑 25 年；Manchester Literary and Philosophical Society 会员（1896-04-14 当选）

## 10. 终审清单

- [ ] 生卒 1865-10-12 / 1940-06-17，享年 74，出生地 Manchester、去世地 Bourne End
- [ ] 1929 共享（Euler-Chelpin）表述准确；官方获奖理由英文原句完整呈现
- [ ] 博士导师 Otto Fischer（勿误写 Emil Fischer）；zymase 归 Buchner、辅酶贡献归 Harden
- [ ] Harden–Young 酯 = 果糖-1,6-二磷酸；糖酵解酶（PFK / aldolase）归属正确
- [ ] 博士生仅 Norris、Maclean 两人入库
- [ ] 无编造引语——page.md 无任何直接引语，全文用间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Arthur_Harden/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：检查 images/ 目录肖像是否就位；infobox 无图，若用装饰圆占位须在 Review 记录
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：全文不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
