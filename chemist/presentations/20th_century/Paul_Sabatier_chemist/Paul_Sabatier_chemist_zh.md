# Paul Sabatier（保罗·萨巴捷）立传提示词

> qid=Q104575 · 1854-11-05 – 1941-08-14 · 法国化学家 · 20 世纪 · 诺贝尔化学奖（1912，与 Victor Grignard 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Paul_Sabatier_chemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取本地 images/ 目录 1912 年诺奖照；404 则用装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{industry}\enspace 催化氢化的开拓者\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地（Carcassonne）/去世地（Toulouse）、教育（École Normale Supérieure / Collège de France）、博士导师（Marcellin Berthelot）、核心领域（多相催化 / 无机化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「催化 / 镍表面吸附」母题——离散圆点暗示金属催化剂表面上的分子吸附与氢化。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），Sabatier 反应 CO₂ + 4H₂ → CH₄ + 2H₂O 是天然公式素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul Sabatier（中文惯称：保罗·萨巴捷；FRS For / HFRSE 头衔，法语音 [sabatje]）
- **生卒**：1854-11-05 生于法国 Carcassonne（卡尔卡松）→ 1941-08-14 逝于法国 Toulouse（图卢兹），享年 86；天主教徒
- **国籍**：France（法国）
- **身份**：化学家（多相催化 / 氢化；图卢兹科学界耆宿）
- **家庭**：已婚，四女；其中一女嫁给意大利化学家 Emilio Pomilio
- **教育轨迹**：1874 入 École Normale Supérieure（巴黎高师）→ 1877 以全班第一毕业 → 1880 获 Collège de France 科学博士（Doctor of Science）
- **导师**：Marcellin Berthelot（infobox 博士导师）
- **博士**：1880，Doctor of Science（Collège de France）；最早研究为硫与金属硫酸盐的热化学（博士论文主题）
- **研究领域**：无机化学、有机化学、催化（heterogeneous catalysis / 氢化）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **卡尔卡松出身（1854）**：高师第一毕业、Collège de France 博士——巴黎科班训练打底。
2. **博士论文（1880）**：硫与金属硫酸盐的热化学——一生的热化学与硫酸盐兴趣由此发端。
3. **扎根图卢兹（1883）**：接替 Édouard Filhol 出任 Faculty of Science 教席，此后一生教学于图卢兹。
4. **与 Senderens 的黄金搭档（1883 起）**：与 Jean-Baptiste Senderens 合作之深"难以区分彼此的工作"——合著科学院 Comptes Rendus 短文 34 篇、法国化学会通报 11 篇、《化学与物理年鉴》合著 2 篇。
5. **羰基镍之后（1890 年代）**：1890 羰基镍被发现后，两人尝试以氮氧化物合成类似物，只得各类氧化产物；直到 1912 Sabatier 仍相信可得"真正的亚硝基金属"，后被证明只是吸附了 NO₂ 的金属氧化物。
6. **乙炔氢化课题接棒（1896）**：Moissan 与 Charles Moureu 发现乙炔可与某些过渡金属反应；叠加 Prosper de Wilde 1874 年铂黑上加氢先例——Sabatier 与 Senderens 承接此方向。
7. **微量镍催化（1897）**：借鉴美国化学家 James F. Boyce 的生化工作，发现**痕量镍**即可催化大多数碳化合物加氢——工业氢化的关键。
8. **甲烷化反应（1902）**：COₓ 的 methanation 反应由 Sabatier 与 Senderens 于 1902 年首先发现（CO₂ + 4H₂ → CH₄ + 2H₂O，∆H = −165.0 kJ/mol，需初始引发能量；今用于空间站与火前燃料工艺叙述时仅限页面事实）。
9. **Jecker 奖（1905）**：因 Sabatier–Senderens Process 与 Senderens 共享科学院 Jecker Prize；1905–06 后两人合著骤减——共同工作贡献认定的经典难题（页面原话口径）。
10. **理学院长（1905）**：任 University of Toulouse 理学院长（Dean）。
11. **1912 诺贝尔化学奖（共享）**：与同胞 Victor Grignard 共享；"Sabatier was honoured for his work improving the hydrogenation of organic species in the presence of metals"——页面口径；同年《La Catalyse en Chimie Organique》出版（1913）系统化其催化思想。
12. **Sabatier 原理**：催化领域的 Sabatier principle 以其命名（催化剂–反应物相互作用须适中）——页面仅一句，展开需谨慎。
13. **晚年与身后**：1941-08-14 逝于图卢兹；图卢兹 Paul Sabatier University 与卡尔卡松一所中学以其命名；亦为《Annales de la Faculté des Sciences de Toulouse》共同创办人（与数学家 Thomas Joannes Stieltjes）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（墨青 deep teal） | `#0E4D64` | 金属镍催化剂的冷峻与工业化学的务实（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（催化氢化 badgeHyd） | `#2E5A9E` | 蓝镍催化加氢 |
| 分类色 2（Sabatier 反应 badgeMeth） | `#1B7A43` | 绿 CO₂ 甲烷化 |
| 分类色 3（师承与搭档 badgeCollab） | `#D97B29` | 琥珀 Berthelot / Senderens |
| 分类色 4（制度与传承 badgeInst） | `#C0395B` | 玫瑰图卢兹理学院 / 大学命名 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「催化 / 金属表面吸附」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（清单指定 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`）
- **风格**：怀旧 / 温厚 / 长时间沉淀的回望
- **匹配理由**：
  - "PAST" 匹配其生涯节奏——1883 到 1941 近一甲子扎根图卢兹，是"一生做一件事"的典范
  - "温厚" 匹配其合作气质——与 Senderens 数十年不分彼此的合作与 1905 年后的体面收场
  - "回望" 匹配传记叙事——高师第一 → 巴黎博士 → 图卢兹教席 → 1912 诺奖 → 大学以其命名
- **时长对齐**：以曲目实际时长 > 15 页 × 7 秒为宜，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 催化氢化的开拓者 / Paul Sabatier 1854–1941 + 四色 badge + 右上头像 + 国籍行（法国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  萨巴捷的一生 — 高斯式时间线（10 节点：1854→1874→1880→1883→1897→1902→1905→1912→1913→1941）
04  卡尔卡松与巴黎高师 (1854–1880) — 表格「时间|事件|结果」
05  图卢兹：接棒 Filhol (1883–1896) — 表格「时间|事件|结果」
06  与 Senderens 的黄金搭档 — 表格「人物|合作|成果」（34 篇短文 / 11 篇通报 / 2 篇年鉴）
07  微量镍催化 (1897) — 表格「问题|方法|结果」+ 公式框：痕量 Ni 催化加氢
08  Sabatier 反应与甲烷化 (1902) — 表格「反应物|条件|产物」+ 公式框：CO₂+4H₂→CH₄+2H₂O
09  1912 诺贝尔化学奖 — 表格「得主|理由|史实」+ 公式框：共享得主（与 Grignard）页面口径
10  《La Catalyse en Chimie Organique》(1913) — 表格「著作|内容|意义」
11  师承与合作网络 — 表格「人物|方向|结果」（Berthelot / Senderens / Grignard / Moissan-Moureu 接棒线）
12  荣誉 — 高斯式「类别|代表|意义」表格（Davy 1915 / Albert 1926 / Franklin 1933 / FRS For）
13  遗产：Sabatier 大学与Sabatier 原理 — 四分类遗产盒 + 公式框：Sabatier 原理一句话 + 命名机构
14  结尾 — 「痕量的镍，撬动了整个氢化工业。」（无出处意境句）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1912 共享 | 与 Victor Grignard **共享**——Sabatier 因金属存在下改进有机物氢化、Grignard 因格氏试剂，理由不同勿混 |
| 1912 获奖理由 | 页面口径 "his work improving the hydrogenation of organic species in the presence of metals"——**页面无载诺贝尔官方全句 citation**，禁杜撰完整官方措辞 |
| 甲烷化叙述边界 | CO₂ + 4H₂ → CH₄ + 2H₂O、∆H = −165.0 kJ/mol、需初始能量均为页面实载；**空间站/火星应用页面未载，禁写** |
| Senderens 关系 | 1883 起"合作之深难以区分彼此"（页面原话可引）；1905–06 后合著骤减归因于"共同工作贡献认定的经典难题"——页面推测语气（perhaps），保留推测语气勿写死 |
| 亚硝基金属 | 1912 年他仍相信"true nitro metals"存在、后被证伪——如实写"曾误"而非回避 |
| Boyce 定位 | 1897 镍催化"借鉴美国化学家 James F. Boyce 的生化工作"（building on）——勿写成 Boyce 首创或 Sabatier 独创 |
| de Wilde / Moissan / Moureu | 都是课题渊源（1874 铂黑氢化先例 / 1896 乙炔-过渡金属发现），**非个人直接关系，不入库** |
| Filhol | 1883 接替其教席——职位继承关系，非师承/同事合作，不入库 |
| 家庭口径 | 已婚、四女、一女嫁 Emilio Pomilio——妻子姓名页面无载，禁写 |
| 宗教 | 天主教徒——一句带过或省略，勿展开 |
| 同名区分 | Sabatier reaction（CO₂ 甲烷化）/ Sabatier principle（催化原理）/ Sabatier–Senderens Process 三者并立；勿与作家 Paul Sabatier（《Life of St. Francis》作者同名）混淆 |
| 机构口径 | infobox Institutions：Collège de France / University of Bordeaux / University of Toulouse；正文仅实载 Toulouse——Bordeaux 一事正文无载，引用需谨慎 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q104575 | ✅ |
| name_zh | 保罗·萨巴捷 | ✅ |
| name_en | Paul Sabatier | ✅（清单 db_id 为空，按 page.md 规范名新建；目录名 Paul_Sabatier_chemist 仅为消歧义） |
| birth_date | 1854-11-05 | ✅ |
| death_date | 1941-08-14 | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | heterogeneous catalysis（person_field 细分：catalysis / hydrogenation / inorganic chemistry，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Marcellin Berthelot | 师→生（博士导师） | infobox 明载；1880 Collège de France 科学博士 |
| colleague | Jean-Baptiste Senderens | 无向 | 1883 起"合作之深难以区分彼此"；Sabatier–Senderens Process；1905 共享 Jecker Prize |
| co-honored | Victor Grignard | 无向 | 1912 诺贝尔化学奖共同得主 |
| other | Emilio Pomilio | 无向 | 意大利化学家，其女婿（一女嫁之） |

> 禁入库名单（课题渊源/职位继承，非个人直接关系）：Henri Moissan、Charles Moureu（1896 乙炔课题先发现者）、Prosper de Wilde（1874 铂黑氢化先例）、James F. Boyce（1897 借鉴其生化工作）、Édouard Filhol（1883 教席继任关系）、Thomas Joannes Stieltjes（期刊共同创办人）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1912，与 Victor Grignard 共享；获奖理由页面口径 "his work improving the hydrogenation of organic species in the presence of metals"）
- Jecker Prize（1905，与 Senderens 共享，因 Sabatier–Senderens Process）
- Davy Medal（1915）
- Albert Medal（1926，Royal Society of Arts）
- Franklin Medal（1933）
- Legion of Honour：Knight → Officer → Commander → Grand Officer（frontmatter 载 Grand Officer）
- Foreign Member of the Royal Society（FRS For）；Honorary doctorate of the University of Porto
- La Caze Prize of the Academy of Sciences（frontmatter 载，正文无细节）
- 诺贝尔演讲：1912-12-11《The Method of Direct Hydrogenation by Catalysis》

## 9. 机构清单

- 教育：lycée Pierre-de-Fermat（frontmatter 载）、École Normale Supérieure（1874–1877，全班第一毕业）、Collège de France（1880 科学博士）
- 任职：University of Bordeaux（infobox 列，正文无细节）；University of Toulouse（1883 接替 Filhol 教席；1905 理学院长；一生教学于此）
- 期刊：Annales de la Faculté des Sciences de Toulouse 共同创办人（与 Thomas Joannes Stieltjes）
- 命名机构：Paul Sabatier University（Toulouse）；Carcassonne 一所中学以其命名

## 10. 终审清单

- [ ] 生卒 1854-11-05 / 1941-08-14，享年 86，出生地 Carcassonne、去世地 Toulouse
- [ ] 1912 与 Grignard 共享表述准确；获奖理由只用页面口径、不杜撰官方全句
- [ ] 1902 甲烷化 / 1905 Jecker 奖 / 1905 院长 / 1913 专著年份准确
- [ ] Senderens 合作与 1905 后疏远的"推测语气"保留；亚硝基金属误判如实写
- [ ] Moissan / Moureu / de Wilde / Boyce / Filhol 均不入库（课题渊源与职位继承）
- [ ] 无引语杜撰（可引原话仅"难以区分彼此的工作"一句）；全文无页面无载引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Paul_Sabatier_chemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（1912 诺奖照）；404 用装饰圆占位并注明
- [ ] **国籍**：封面顶部明示法国
- [ ] **引语核对**：仅"难以区分彼此的工作"为页面可溯源表述；其余全部间接转述
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
