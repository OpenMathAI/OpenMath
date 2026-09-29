# Stanford Moore（斯坦福德·穆尔）立传提示词

> qid=Q110952 · 1913-09-04 – 1982-08-23 · 美国生物化学家 · 诺贝尔化学奖（1972，与 Anfinsen、Stein 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Stanford_Moore/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 公式展示框，是本次执行的版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` 就位；若无真实肖像则按模板装饰圆占位，图注如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 氨基酸密码的破译者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士（导师/论文）、师承（博士后环境）、核心领域、机构。事实取自本地 Wikipedia infobox，不得杜撰；页面无载字段如实标「页面无载」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「色谱洗脱峰 / 氨基酸序列」母题——离散圆点暗示层析柱上被逐一分开的氨基酸。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「氨基酸分析仪 → RNase 全序列 124 残基」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Stanford Moore（中文惯称：斯坦福德·穆尔）
- **生卒**：1913-09-04 生于伊利诺伊州芝加哥 → 1982-08-23 逝于纽约市，享年 68
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist；1972 诺贝尔化学奖共同得主）
- **家庭**：**页面无载**（本地 page.md 与 infobox 均无父母/配偶/子女记载——立传时如实留白，禁止编造）
- **教育轨迹**：
  - Peabody Demonstration School（今 University School of Nashville）
  - 1935 Vanderbilt University 毕业，**summa cum laude**（最优等），Phi Kappa Sigma 兄弟会成员
  - 1938 University of Wisconsin–Madison 有机化学博士
- **导师**：Karl Paul Link（博士导师，infobox 明载）
- **博士论文**：1938，《The identification of carbohydrates as benzimidazole derivatives》
- **师承/博士后环境**：1939 加入洛克菲勒研究所 Max Bergmann 实验室（正文明载 Moore joined Bergmann's lab in 1939），在此与 William H. Stein 开始终生合作
- **研究领域**：生物化学——核糖核酸酶（ribonuclease）、氨基酸层析、蛋白质序列

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **纳什维尔少年（1913）**：生于芝加哥，在 Peabody Demonstration School（今 University School of Nashville）完成中学教育。
2. **Vanderbilt 最优等毕业（1935）**：summa cum laude；Phi Kappa Sigma 成员。
3. **威斯康星有机化学博士（1938）**：师从 Karl Paul Link，论文以苯并咪唑衍生物鉴定碳水化合物——糖化学的严格训练。
4. **洛克菲勒的起点（1939）**：加入 Max Bergmann 实验室，与 Stein 相遇；据 Moore 自述，"During the early years of our cooperation, Stein and I worked out a system of collaboration that lasted for a lifetime."（此引语见于 Stein 篇正文，为 Moore 回忆）。
5. **战时分离（1942–1945）**：二战爆发，两人暂时分开参加战时工作；Bergmann 1944 年去世后，所长 Herbert S. Gasser 让他们接续氨基酸研究。
6. **淀粉柱层析定量氨基酸**：以土豆淀粉为固定相的柱层析 + 自动收集器 + 茚三酮（ninhydrin）显色反应定量——两周期/蛋白的慢分析起步。
7. **离子交换加速（2 周 → 5 天）**：引入离子交换层析把单蛋白分析时间从约两周缩到 5 天。
8. **第一台自动氨基酸分析仪（1958）**：与 Stein 及 Daryl Spackman 合作完成——蛋白质序列测定的工程前提。
9. **首个酶的全序列（1959）**：Moore 与 Stein 宣布测定核糖核酸酶（ribonuclease）的完整氨基酸序列——**第一个被测出完整序列的酶**，此项工作被写入诺贝尔授奖理由。
10. **结构与催化活性（1960s）**：序列 + RNase 晶体 X 射线分析结合，确定活性部位——阐明化学结构与催化活性的联系（1972 授奖理由的核心）。
11. **1952 正教授**：任 Rockefeller（Institute→University）生物化学教授；除二战政府服务期外，职业生涯全部在洛克菲勒。
12. **1972 诺贝尔化学奖**：与 Christian B. Anfinsen、William Howard Stein 共享；授奖理由（见 Stein 篇引文）"for their contribution to the understanding of the connection between chemical structure and catalytic activity of the ribonuclease molecule"；诺奖演讲 1972-12-11《The Chemical Structures of Pancreatic Ribonuclease and Deoxyribonuclease》。
13. **沉默的另一半**：本页篇幅极短（仅 infobox + 一段正文），两人的获奖理由、分工与友谊须与 Stein 篇互为镜像——Moore 篇侧重「仪器与分析化学」，Stein 篇侧重「序列与生命历程」。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深砖红 madder） | `#7E1E23` | 层析柱与洗脱峰的暗红——分析化学的严谨（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（氨基酸层析 badgeChrom） | `#1E4E79` | 蓝淀粉柱 / 离子交换 |
| 分类色 2（自动分析仪 badgeAuto） | `#1B7A43` | 绿 1958 分析仪 / Spackman |
| 分类色 3（RNase 序列 badgeRNase） | `#D97B29` | 琥珀 1959 全序列 / 活性部位 |
| 分类色 4（结构-功能 badgeCatal） | `#7A3E9D` | 紫1972 诺奖 / 催化活性 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「洗脱峰 / 氨基酸逐一分离」的层析意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（文件 `12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`）
- **风格**：戏剧性 / 沉重铺底 / 史诗弦乐
- **匹配理由**：
  - "Empire Collapse" 的厚重铺底匹配洛克菲勒学派的宏大叙事——从 Bergmann 到 Moore/Stein 的分析化学帝国
  - 戏剧性弦乐匹配「2 周→5 天→自动化」的持续突破与 1959 年首个酶全序列的历史时刻
  - 暗色基调也映照本页史料的极简——英雄叙事的留白
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 氨基酸密码的破译者 / Stanford Moore 1913–1982 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/导师/机构/领域/荣誉）
03  穆尔的一生 — Sanger 式时间线（10 节点：1913→1935→1938→1939→1952→1958→1959→1960s→1972→1982）
04  早年与教育 (1913–1935) — 表格「时间|事件|结果」（Nashville / Vanderbilt summa cum laude）
05  威斯康星博士 (1935–1938) — 表格「导师|论文|结果」+ 公式框：苯并咪唑衍生物鉴定碳水化合物
06  洛克菲勒：Bergmann 实验室 (1939–1944) — 表格「人物|事件|结果」（Bergmann/Stein/战时分离）
07  淀粉柱层析与离子交换 — 表格「问题|方法|结果」+ 公式框：2 周 → 5 天
08  第一台自动氨基酸分析仪 (1958) — 表格「问题|协作|结果」（Stein / Spackman）
09  RNase 全序列 (1959–1960) — 表格「挑战|方法|结果」+ 公式框：ribonuclease 完整氨基酸序列
10  结构与催化活性 — 表格「证据|方法|结论」（序列 + X 射线 → 活性部位）
11  1972 诺贝尔化学奖 — 三人共享（Anfinsen / Moore / Stein）+ 诺奖演讲页式表格
12  荣誉与学会 — Sanger 式「类别|代表|意义」表格（doctor honoris causa Paris 等）
13  遗产：序列测定的工程学 — 四分类遗产盒 + 公式框：分析仪→蛋白质时代
14  结尾 — 「把蛋白质拆成一个个氨基酸，生命的催化之谜从此有了化学答案。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1972 诺奖口径 | 三人共享：Christian B. Anfinsen、Stanford Moore、William Howard Stein；授奖理由英文以 Stein 篇正文引文为准 "for their contribution to the understanding of the connection between chemical structure and catalytic activity of the ribonuclease molecule"——本页 page.md 未载三人份额比例，**勿编 1/2·1/4·1/4** |
| 1959 vs 1960 | 正文口径：1959 Moore 与 Stein 宣布（announced）首个酶全序列；Stein 篇正文口径"by 1960"测完——两篇各忠于本人页面，勿混写同一年份断言 |
| 首个 vs 第一个 | "first determination of the complete amino acid sequence of an enzyme"（第一个被测全序列的**酶**）——勿扩大成"第一个蛋白质"（胰岛素序列是 Sanger 1955，先于此） |
| 自动分析仪年份 | **1958** 与 Stein 研制第一台自动氨基酸分析仪——勿写 1959 |
| 博士论文题目 | 《The identification of carbohydrates as benzimidazole derivatives》(1938)——勿与 Stein 的《The Composition of Elastin》混淆 |
| 家庭信息 | 本页 page.md **无载**家庭/配偶/子女——身份信息页如实留白，禁止编造 |
| 导师区分 | Moore 导师 = Karl Paul Link（威斯康星）；Stein 导师 = Hans Thacher Clarke（哥伦比亚）——勿互换 |
| Spackman | Daryl Spackman 是分析仪共同研制者（正文明载）——勿写成学生或下属之外的杜撰头衔 |
| 同名区分 | Stanford Moore 无常见同名陷阱，但注意勿与 Stein 篇引语张冠李戴；Rockefeller Institute → Rockefeller University 1965 改名口径以两页实载为准 |
| 引语红线 | 本页 page.md 无直接引语——中文引号内不得出现无法在 page.md 溯源的"原话"，Moore 的合作感言只可间接转述并注明出处页 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110952 | ✅ |
| name_zh | 斯坦福德·穆尔 | ✅ |
| name_en | Stanford Moore | ✅ |
| birth_date | 1913-09-04 | ✅ |
| death_date | 1982-08-23 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | biochemistry | 生物化学 |
| 1 | ribonuclease | 核糖核酸酶 |
| 2 | chromatography | 色谱法 |
| 3 | protein sequencing | 蛋白质测序 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Karl Paul Link | 师→生（direction=advisor） | 威斯康星博士导师，1938 有机化学博士 |
| colleague | Max Bergmann | 无向 | 1939 加入其洛克菲勒研究所实验室 |
| colleague | William Howard Stein | 无向 | 1939 起终生合作；1958 自动氨基酸分析仪、1959 RNase 全序列 |
| colleague | Daryl Spackman | 无向 | 自动氨基酸分析仪共同研制 |
| co-honored | Christian B. Anfinsen | 无向 | 1972 诺贝尔化学奖共同得主 |
| co-honored | William Howard Stein | 无向 | 1972 诺贝尔化学奖共同得主 |

> 禁入库名单（metadata.json 有载但 page.md 正文/infobox 无载）：无家庭关系可入库（页面无载）；`doctor honoris causa from the University of Paris` 属奖项非关系。其余 metadata 字段（award_received 等）不产生关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1972，与 Anfinsen、Stein 共享）
- doctor honoris causa，University of Paris（metadata.json 明载）

> 本页 page.md 正文仅载诺奖；其余奖项除上列外页面无载——立传荣誉页如实从简，禁止扩写。

## 9. 机构清单

- 教育：University School of Nashville（Peabody Demonstration School）、Vanderbilt University（1935，summa cum laude）、University of Wisconsin–Madison（PhD 1938）
- 任职：Rockefeller Institute（1939 加入 Bergmann 实验室；后为 Rockefeller University），1952 任生物化学教授；二战期间政府服务；除战时外整个职业生涯在洛克菲勒
- 学术共同体：NAS Biographical Memoirs 收录（外部链接佐证，立传可注明）

## 10. 终审清单

- [ ] 生卒 1913-09-04 / 1982-08-23，享年 68；出生地芝加哥、去世地纽约市
- [ ] 1972 三人共享表述准确；授奖理由英文以 page.md 实载口径为准，不编份额比例
- [ ] 1958 自动分析仪 / 1959 宣布首个酶全序列（Stein 篇口径 by 1960）年份不混
- [ ] 博士导师 Karl Paul Link、论文题目准确
- [ ] 家庭信息留白（页面无载），无编造
- [ ] 引语全部可在本地 Wikipedia 原文找到；无直接引语时不出现引号原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Stanford_Moore/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 核对肖像；无真实肖像用装饰圆占位并如实标注
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：本页无直接引语；涉及 Moore 感言只可间接转述并注明出处页
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 Stein 篇互查：1972 共享口径、引语归属、年份口径两篇一致
